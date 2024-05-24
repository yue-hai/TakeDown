#!/usr/bin/env python3
# 指定脚本解释器和许可证信息
# Licensed under GPLv3
#
# 创建一个简单的HTTP服务器来允许用户控制n2n网络边缘节点（edge nodes）
# Simple http server to allow user control of n2n edge nodes
#
# 目前仅用于演示：
# - 需要编写更好看的 HTML
# - 需要在 edge 端增加更多的 JSON 接口
# Currently only for demonstration
# - needs nicer looking html written
# - needs more json interfaces in edge
#
# 使用以下 URL 测试服务器：
# Try it out with
#   http://localhost:8080/
#   http://localhost:8080/edge/edges
#   http://localhost:8080/edge/supernodes

# 引入 argparse 模块，用于处理命令行参数
import argparse
# 引入 socket 模块，用于网络通信
import socket
# 引入 json 模块，用于处理JSON数据格式
import json
# 引入 socketserver 模块，简化网络服务器的创建
import socketserver
# 引入 http.server 模块，用于创建 HTTP 服务器
import http.server
# 引入 signal 模块，用于处理操作系统信号
import signal
# 引入 functools 模块，用于高阶函数和可调用对象的操作
import functools
# 引入 base64 模块，用于处理 Base64 编码
import base64

# 从 http 模块导入 HTTPStatus，用于提供 HTTP 状态代码
from http import HTTPStatus


class JsonUDP:
    """封装与 edge 的通信"""
    """encapsulate communication with the edge"""
    
    # 初始化方法；self 代表类的实例，而不是类；port 为端口号
    def __init__(self, address, port):
        # 设置地址；默认为 127.0.0.1
        self.address = address
        # 设置端口；默认为 10001
        self.port = port
        # 初始化消息标签；默认为 0
        self.tag = 0
        # 初始化认证密钥；默认为 None
        self.key = None
        # 初始化调试模式；默认为 False
        self.debug = False
        # 创建 UDP 套接字；使用 IPv4 和 UDP 协议
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 设置套接字的超时时间为1秒
        self.sock.settimeout(1)
    
    # 生成新的消息标签，用于跟踪响应；
    def _next_tag(self):
        """为每个通信生成一个新标签以跟踪响应。"""
        """Generate a new tag for each communication to track responses."""
        
        # 将标签转换为字符串
        tagstr = str(self.tag)
        # 递增标签，取模 1000；生成一个新的消息标签，用于跟踪响应，每次递增，最高到999后重置为0
        self.tag = (self.tag + 1) % 1000
        
        # 返回标签字符串
        return tagstr
    
    # 生成完整的命令字符串，用于发送；
    def _cmdstr(self, msgtype, cmdline):
        """创建要发送的完整命令字符串"""
        """Create the full command string to send"""
        
        # 生成新的标签
        tagstr = self._next_tag()
        # 创建选项列表，首先包含标签
        options = [tagstr]
        
        # 如果设置了密钥，则添加密钥
        if self.key is not None:
            # 添加选项，用于认证密钥字段
            options += ['1']
            # 如果设置了密钥，则添加密钥
            options += [self.key]
        
        # 将选项列表连接成字符串，用":"分隔
        optionsstr = ':'.join(options)
        
        # 返回标签和完整的命令字符串，命令字符串包括消息类型、选项字符串和命令行
        return tagstr, ' '.join((msgtype, optionsstr, cmdline))
    
    # 等待接收数据包；
    def _rx(self, tagstr):
        """等待接收数据包"""
        """Wait for rx packets"""
        
        # 需要注意的是，此处recv调用没有设置超时
        # TODO: there are no timeouts with any of the recv calls
        
        # 从套接字接收数据，缓冲区大小为 1024 字节
        data, _ = self.sock.recvfrom(1024)
        # 解码并解析接收到的 JSON 数据
        data = json.loads(data.decode('utf8'))
        
        # 假设我们收到的第一个数据包将带有我们的标签，并且是“错误”或“开始”的类型
        # TODO: We assume the first packet we get will be tagged for us and be either an "error" or a "begin"
        
        # 断言接收到的数据包的标签与我们发送的标签相匹配
        assert (data['_tag'] == tagstr)
        
        # 如果数据类型是“错误”，则抛出异常
        if data['_type'] == 'error':
            raise ValueError('Error: {}'.format(data['error']))
        
        # 断言数据类型为“开始”
        assert (data['_type'] == 'begin')
        
        # 理想情况下，我们会确认这是我们的“开始”数据包，但这需要传递命令到此方法中
        # 并且可能需要解析传递给我们的 cmdline ：-（
        # Ideally, we would confirm that this is our "begin", but that
        # would need the cmd passed into this method, and that would
        # probably require parsing the cmdline passed to us :-(
        
        # 初始化结果列表
        result = list()
        # 初始化错误变量
        error = None
        
        # 循环接收数据
        while True:
            # 从套接字接收数据，缓冲区大小为 1024 字节
            data, _ = self.sock.recvfrom(1024)
            
            # 解码并解析 JSON 数据
            data = json.loads(data.decode('utf8'))
            
            # 如果接收到的数据包标签不是我们的标签，则忽略它
            if data['_tag'] != tagstr:
                continue
            
            # 如果数据类型是“错误”
            if data['_type'] == 'error':
                # 记录错误信息，继续接收数据
                error = ValueError('Error: {}'.format(data['error']))
                continue
            
            # 如果数据类型是“结束”
            if data['_type'] == 'end':
                # 如果之前记录了错误信息，则抛出错误
                if error:
                    raise error
                
                # 返回结果列表
                return result
            
            # 如果数据类型既不是“行”也不是已知类型，则抛出异常
            if data['_type'] != 'row':
                raise ValueError('Unknown data type {} from edge'.format(data['_type']))
            
            # 删除数据中的元数据标签和类型信息
            del data['_tag']
            del data['_type']
            
            # 如果处于调试模式，则打印数据
            if self.debug:
                # 打印数据
                print(data)
                # 打印换行符
                print()
                # 打印分隔符
                print('-' * 40)
                # 打印换行符
                print()
            
            # 将数据添加到结果列表中
            result.append(data)
    
    # 执行 RPC 调用；当页面请求时，执行 RPC 调用，使用 http.server.BaseHTTPRequestHandler 的 do_GET 和 do_POST 方法
    def _call(self, msgtype, cmdline):
        """执行 rpc 调用"""
        """Perform a rpc call"""
        
        # 生成命令字符串
        tagstr, msgstr = self._cmdstr(msgtype, cmdline)
        # 发送数据到指定的地址和端口
        self.sock.sendto(msgstr.encode('utf8'), (self.address, self.port))
        
        # 接收响应并返回
        return self._rx(tagstr)
    
    # 读取数据的方法
    def read(self, cmdline):
        # 执行读取命令
        return self._call('r', cmdline)
    
    # 写入数据的方法
    def write(self, cmdline):
        # 执行写入命令
        return self._call('w', cmdline)


# 创建一个简单的 HTTP 处理器，用于通过 Web 界面管理 n2n 边缘和超级节点设置
class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """自定义 HTTP 处理程序，用于通过 Web 界面管理 n2n 边缘和超级节点设置。"""
    """Custom HTTP handler to manage n2n edge and supernode settings via a web interface."""
    
    # 初始化方法；rpc 为与 edge 节点通信的 JsonUDP 实例，snrpc 为与 supernode 节点通信的 JsonUDP 实例
    # *args 和 **kwargs 是 Python 中的可变参数，用于接收不定数量的参数
    def __init__(self, rpc, snrpc, *args, **kwargs):
        # RPC 对象，用于与 edge 节点通信
        self.rpc = rpc
        # RPC 对象，用于与 supernode 节点通信
        self.snrpc = snrpc
        
        # 调用父类构造器
        super().__init__(*args, **kwargs)
    
    # 自定义请求日志方法，不记录日志
    def log_request(self, code='-', size='-'):
        pass
    
    # 发送简单的 HTTP 响应
    def _simplereply(self, number, message):
        # 设置响应状态码
        self.send_response(number)
        # 结束 HTTP 头部
        self.end_headers()
        
        # 发送响应内容
        self.wfile.write(message.encode('utf8'))
    
    # 发送 JSON 格式的响应
    def _replyjson(self, data):
        # 设置状态码为 200
        self.send_response(HTTPStatus.OK)
        # 设置内容类型为 JSON
        self.send_header('Content-type', 'application/json')
        # 结束头部
        self.end_headers()
        
        # 发送JSON数据
        self.wfile.write(json.dumps(data).encode('utf8'))
    
    # 发送未授权的响应
    def _replyunauth(self):
        # 设置状态码为 401 未授权
        self.send_response(HTTPStatus.UNAUTHORIZED)
        # 设置认证方式为基本认证
        self.send_header('WWW-Authenticate', 'Basic realm="n2n"')
        # 结束头部
        self.end_headers()
    
    # 提取认证信息
    def _extractauth(self, rpc):
        # 初始化密钥为空
        rpc.key = None
        # 获取认证头部
        header = self.headers.get('Authorization')
        
        # 如果提供了认证头部
        if header is not None:
            # 分割认证头部，获取认证类型和编码后的信息
            authtype, encoded = header.split(' ')
            
            # 如果认证类型为基本认证
            if authtype == 'Basic':
                # 解码认证信息，获取用户和密钥
                user, key = base64.b64decode(encoded).decode('utf8').split(':')
                # 设置RPC的密钥
                rpc.key = key
        
        # 如果没有提供密钥
        if rpc.key is None:
            # 使用默认密钥
            rpc.key = rpc.defaultkey
    
    # 执行 RPC 调用
    def _rpc(self, method, cmdline):
        try:
            # 调用 RPC 方法
            data = method(cmdline)
        
        # 捕获异常
        except ValueError as e:
            # 如果是认证错误
            if str(e) == "Error: badauth":
                # 发送未授权响应
                self._replyunauth()
                return
            
            # 如果是其他错误，发送 400 坏请求
            self._simplereply(HTTPStatus.BAD_REQUEST, 'Bad Command')
            return
        
        # 如果超时
        except socket.timeout as e:
            # 发送 408 请求超时
            self._simplereply(HTTPStatus.REQUEST_TIMEOUT, str(e))
            return
        
        # 发送成功的响应
        self._replyjson(data)
        return
    
    # 执行读操作的 RPC 调用
    def _rpc_read(self, rpc):
        # 提取认证信息
        self._extractauth(rpc)
        # 分割 URL 路径
        tail = self.path.split('/')
        # 获取命令
        cmd = tail[2]
        # 执行读命令
        self._rpc(rpc.read, cmd)
    
    # 执行写操作的 RPC 调用
    def _rpc_write(self, rpc):
        # 提取认证信息
        self._extractauth(rpc)
        # 获取内容长度
        content_length = int(self.headers['Content-Length'])
        # 读取 POST 数据
        post_data = self.rfile.read(content_length).decode('utf8')
        # 分割 URL 路径
        tail = self.path.split('/')
        
        # 获取命令
        cmd = tail[2]
        # 构造命令行
        cmdline = cmd + ' ' + post_data
        
        # 执行写命令
        self._rpc(rpc.write, cmdline)
    
    # 处理 GET 请求
    def do_GET(self):
        # 如果路径以 .css 结尾，说明请求的是 CSS 文件
        if self.path.endswith(".css"):
            try:
                # 打开 CSS 文件，这里假设文件位于服务器的同级目录下
                with open(self.path[1:], 'rb') as file:  # 使用 [1:] 去除路径前的 '/'
                    # 设置响应状态码为 200
                    self.send_response(HTTPStatus.OK)
                    # 设置内容类型为 CSS
                    self.send_header('Content-type', 'text/css')
                    # 结束 HTTP 头部
                    self.end_headers()
                    # 读取文件内容并发送
                    self.wfile.write(file.read())
            except FileNotFoundError:
                # 文件未找到，发送 404 响应
                self._simplereply(HTTPStatus.NOT_FOUND, 'File Not Found')
            return
        
        # 如果路径以 /edge/ 开头
        if self.path.startswith("/edge/"):
            # 执行 edge 节点的读操作
            self._rpc_read(self.rpc)
            return
        
        # 如果路径以 /supernode/ 开头
        if self.path.startswith("/supernode/"):
            # 执行 supernode 节点的读操作
            self._rpc_read(self.snrpc)
            
            return
        
        # 如果请求的是根目录，返回 HTML 页面
        if self.path == '/':
            # 设置响应状态码为 200
            self.send_response(HTTPStatus.OK)
            # 设置内容类型为 HTML
            self.send_header('Content-type', 'text/html; charset=utf-8')
            # 结束头部
            self.end_headers()
            
            # 指定 HTML 文件的位置
            html_path = 'n2n-edge-query-front.html'
            # 打开文件为二进制读模式
            with open(html_path, 'rb') as file:
                # 读取文件内容并发送
                self.wfile.write(file.read())
            return
        
        # 如果找不到页面，发送 404 未找到
        self._simplereply(HTTPStatus.NOT_FOUND, 'Not Found')
        return
    
    # 处理 POST 请求
    def do_POST(self):
        # 如果路径以 /edge/ 开头
        if self.path.startswith("/edge/"):
            # 执行 edge 节点的写操作
            self._rpc_write(self.rpc)
            return
        
        # 如果路径以 /supernode/ 开头
        if self.path.startswith("/supernode/"):
            # 执行 supernode 节点的写操作
            self._rpc_write(self.snrpc)
            return


def main():
    """主函数，解析参数并启动 HTTP 服务器."""
    """Main function to parse arguments and start the HTTP server."""
    
    # 创建一个解析器对象，并设置描述信息；argparse.ArgumentParser 用于解析命令行参数
    ap = argparse.ArgumentParser(description='通过 http 控制正在运行的本地 n2n edge 节点')
    # 添加管理 ip 参数，指定管理命令的 IP 地址
    ap.add_argument('-a', '--mgmtip', action='store', default='127.0.0.1', help='管理 IP 地址（默认值 =127.0.0.1）')
    # 添加管理端口参数，指定端口用于管理命令；add_argument 方法用于添加参数
    ap.add_argument('-t', '--mgmtport', action='store', default=10001, help='管理端口（默认值 = 10001）', type=int)
    # 添加超级节点管理端口参数，指定端口用于超级节点的管理命令
    ap.add_argument('--snmgmtport', action='store', default=10002, help='超级节点管理端口（默认=10002）', type=int)
    # 添加密钥参数，用于管理命令的验证
    ap.add_argument('-k', '--key', action='store', help='管理命令的密码')
    # 添加调试参数，如果指定，将显示原始的内部数据
    ap.add_argument('-d', '--debug', action='store_true', help='显示原始的内部数据')
    # 添加 HTTP 服务的端口参数，指定 HTTP 服务器监听的端口
    ap.add_argument('port', action='store', default=10003, type=int, nargs='?', help='在 TCP 端口上处理请求（默认为 10003）')
    # 解析命令行输入的参数
    args = ap.parse_args()
    
    # 创建一个 JsonUDP 实例，用于 edge 节点的管理；指定管理 IP 和端口
    rpc = JsonUDP(args.mgmtip, args.mgmtport)
    # 设置调试模式
    rpc.debug = args.debug
    # 设置默认的管理密钥
    rpc.defaultkey = args.key
    
    # 创建一个 JsonUDP 实例，用于 supernode 节点的管理；指定管理 IP 和端口
    snrpc = JsonUDP(args.mgmtip, args.snmgmtport)
    # 设置调试模式
    snrpc.debug = args.debug
    # 设置默认的管理密钥
    snrpc.defaultkey = args.key
    
    # 处理 SIGPIPE 信号，避免进程意外退出
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    # 设置 TCP 服务器允许地址重用
    socketserver.TCPServer.allow_reuse_address = True
    # 创建处理 HTTP 请求的处理器实例
    handler = functools.partial(SimpleHandler, rpc, snrpc)
    # 创建 TCP 服务器，绑定到指定端口
    httpd = socketserver.TCPServer(("", args.port), handler)
    
    try:
        # 启动服务器，永久运行
        httpd.serve_forever()
    
    # 捕获键盘中断异常
    except KeyboardInterrupt:
        # 退出程序
        return


# 如果直接运行此脚本，执行 main 函数
if __name__ == '__main__':
    main()
