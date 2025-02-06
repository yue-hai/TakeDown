# 一、N2N V3 安装配置

> N2N 服务端软件 n2n-3.0 下载地址：https://github.com/ntop/n2n/releases/tag/3.0
> 
> N2N 服务端：[n2n-3.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-3.0.zip)
> 
> N2N 客户端软件 EasyN2N 下载地址：https://bugxia.com/357.html
> 
> N2N 客户端：[n2n_client_windows_3.12_Pack_2.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n_client_windows_3.12_Pack_2.zip)

## 1、n2n 简介

1. N2N（Node to Node）是一种点对点（P2P）网络连接协议，用于在网络中直接连接节点（计算机或设备），而无需通过中心服务器。N2N 协议允许网络中的节点之间直接通信，这种直接连接方式可以提供更高的性能和更好的隐私保护。
2. N2N 协议的特点包括：
	1. **点对点连接**：N2N 允许节点之间直接建立连接，无需经过中心服务器，从而减少了网络通信的中间环节，提高了通信效率。
	2. **加密通信**：N2N 支持对通信数据进行加密，保护通信内容的隐私和安全。
	3. **灵活性**：N2N 协议可以在不同的网络环境中使用，包括局域网、广域网和互联网，提供了灵活的网络连接方式。
	4. **开放性**：N2N 是一个开放的协议，可以被集成到各种应用和系统中，为不同的场景提供点对点连接的能力。
3. N2N 协议可以用于构建各种点对点的网络应用，例如直接设备之间的通信、对等网络文件共享、实时音视频通话等。在实际应用中，N2N 协议通常与其他网络技术和安全机制结合使用，以构建更加安全、高效的点对点通信系统。
4. 当然也可以用来改善游戏联机网络

## 2、说明

1. 本次安装配置基于 N2N 的 V3 版本，具体区别请参考：[N2N版本选择介绍（v1\v2\v2s\v3区别\使用方法教程\免费服务器）](https://bugxia.com/n2n_version_intro)
2. 本次配置主要是以 Linux ubuntu 为服务端、Windows 为客户端

## 3、ubuntu 服务端配置

### ①、<span id="1-3-1">使用 docker 安装服务端</span>

#### Ⅰ、使用 docker 安装服务端

1. 服务端操作系统为：Ubuntu 22.04.3 LTS
2. 开放端口：`10091`、`10092`、`10093`
	1. `sudo ufw allow from any to any port 10091`
	2. `sudo ufw allow from any to any port 10092`
	3. `sudo ufw allow from any to any port 10093`
3. 这里假设 docker 已经安装好了，并且拉取了 ubuntu 的镜像
4. 创建目录：`/home/docker/docker/volumes/n2n/n2n`，下载 N2N 服务端：[n2n-3.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-3.0.zip) 放入其中
5. 解压压缩包：`unzip n2n-3.0.zip`
6. 创建容器，包括后台运行、端口映射、授权等：
	1. 其中，`10091` 是作为 Manage 端口，而 `10092` 作为主要端口
	2. `10093` 作为查询 n2n edge 节点信息程序端口
	3. 实测的时候发现 `10092` 端口既需要开放 UDP 也需要开放 TCP

```shell
docker run -itd \
-p 10091:10091/tcp \
-p 10091:10091/udp \
-p 10092:10092/tcp \
-p 10092:10092/udp \
-p 10093:10093 \
-v /home/docker/docker/volumes/n2n:/home \
--privileged=true \
--name ubuntu-n2n-server \
ubuntu /bin/bash
```

7. 进入该 ubuntu-n2n-server 容器：

```shell
docker exec -it ubuntu-n2n-server /bin/bash
```

8. 更新软件源、安装 vim、安装配置工具：

```shell
# 更新软件源：
apt-get update

# 安装 vim：
apt-get install -y vim

# 安装配置工具：
apt-get install -y autoconf automake libtool make pkg-config
```

9. 进入 n2n 目录：

```shell
cd /home/n2n
```

10. 依次进行下述每一行命令：

```shell
# 将 autogen.sh 脚本设为可执行
chmod +x autogen.sh

# 执行 autogen.sh 脚本，这个脚本通常负责设置或预处理编译环境，生成配置脚本等
./autogen.sh

# 执行 configure 脚本，这个脚本根据系统环境和用户提供的选项，生成适合当前系统的 Makefile 文件
./configure

# 编译源代码并安装
# 'make' 命令根据前面生成的 Makefile 来编译源代码，生成可执行文件或库文件
# 'make install' 命令则是将编译好的文件安装到指定位置，通常是系统的标准目录下，比如 /usr/local/bin
make && make install
```

11. 创建并编辑配置文件：`vim supernode.conf`，写入下述内容，然后保存退出：

```shell
-t=10091
-p=10092
```

12. 运行 supernode：

```shell
supernode ./supernode.conf
```

13. 检查 supernode 是否在后台运行：

```shell
ps -ef|grep supernode
```

```shell
root@f279e3b2bb3f:/# ps -ef|grep supernode
nobody      1711       1  0 08:34 ?        00:00:00 supernode ./supernode.conf
root        1725    1715  0 08:47 pts/1    00:00:00 grep --color=auto supernode
root@f279e3b2bb3f:/# 
```

14. 根据进程号关闭进程

```shell
kill 1711
```

15. 如果想要确保进程被强制终止，可以使用 kill -9 命令：

```shell
kill -9 1711
```

#### Ⅱ、查询 n2n edge 节点信息（使用 java 实现）

> 1. 改为使用 java 实现的原因是之前的 py 脚本经常自己停止
> 2. java 工具类：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fyuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar)
> 3. 若是使用 docker 部署的 n2n，需要将该程序部署到 docker 中

1. 创建目录：`/home/docker/docker/volumes/n2n/n2n-query-yuehai-tool`，下载 java 工具类：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fyuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
2. 进入 ubuntu-n2n-server 容器：

```shell
docker exec -it ubuntu-n2n-server /bin/bash
```

3. 安装 JDK 21；若是安装过程中让选择时区，第一次选择 5 是亚洲，第二次选择 69 是上海

```shell
apt install openjdk-21-jdk
```


4. 通过检查 Java 版本来验证是否成功安装了 JDK

```shell
java -version
```

5. 出现如下输出表示安装成功

```shell
root@734c23cee573:/# java -version
openjdk version "21.0.4" 2024-07-16
OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu224.04)
OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu224.04, mixed mode, sharing)
root@734c23cee573:/# 
```

6. 进入 `/home/n2n-query-yuehai-tool` 目录

```shell
cd /home/n2n-query-yuehai-tool
```

7. 启动 jar：

```shell
nohup java -jar yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar >> yuehai-tool.log 2>&1 &
```

8. 访问测试：http://ip:10093/static/n2n-edge-query.html

#### Ⅲ、查询 n2n edge 节点信息（弃用）

> 1. 使用的服务端脚本是 n2n 服务器自带的，文件在：`/n2n/scripts/n2n-httpd`，直接使用这个也可以
> 2. 下方的脚本和页面等文件需在同一个目录下，且需和 n2n 服务端在同一个设备上
> 3. 开启 10093 端口：`sudo ufw allow from any to any port 10093`
> 4. 若是使用 docker 部署的 n2n，需要将该程序部署到 docker 中

1. 在 `/home/yan/apply/n2n/` 下创建目录 `n2n-edge-query`
2. 在目录 `n2n-edge-query` 下上传服务端脚本文件：[n2n-edge-query-back.py](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-edge-query-back.py)
3. 在目录 `n2n-edge-query` 下上传服务端页面文件：[n2n-edge-query-front.html](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-edge-query-front.html)
4. 在目录 `n2n-edge-query` 下上传服务端页面样式文件：[n2n-edge-query-front-css.css](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-edge-query-front-css.css)
5. 若是没有安装 `python` 环境，则先安装：`sudo apt install python3`
6. 打开一个 `screen` 终端：

```shell
screen -S n2n-edge-query
```

6. 执行服务端脚本：

```shell
# 进入脚本所在目录
cd /home/yan/apply/n2n/n2n-edge-query/

# 启动脚本
python3 n2n-edge-query-back.py -d >> n2n-edge-query-back.log && echo "" >> n2n-edge-query-back.log
```

7. 按 `Ctrl + a + d` 可退出终端
8. 访问测试：http://ip:10093/

![|600](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240523165008.png)

#### Ⅳ、查询 n2n edge 节点信息经常停止的解决（弃用）

> 若是使用 docker 部署的 n2n，需要将该程序部署到 docker 中

1. 创建 `n2n-edge-query-check` 目录用于存放检查接口是否可以访问以及重启后台服务脚本
2. 在其中创建脚本 `check-n2n-edge-query-back.sh` ，用于检查接口是否可以访问

```shell
touch check-n2n-edge-query-back.sh
```

```shell
#!/bin/bash

# API URL
API_URL="http://83.229.120.176:10093"
# 重启【查询 n2n edge 节点信息】后台服务脚本所在路径
restart_path="/home/yan/apply/n2n/n2n-edge-query-check/"

# 分隔符
echo "----------------------------------------------------------------" >> $restart_path/check-n2n-edge-query-back.log
# 换行符
echo "" >> $restart_path/check-n2n-edge-query-back.log

# 尝试访问 API，设置超时时间为 30 秒
if curl --fail --silent --output /dev/null --max-time 30 "$API_URL"; then
    # API 访问成功，保存日志
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】：API 访问成功，不重启【查询 n2n edge 节点信息】后台服务" >> $restart_path/check-n2n-edge-query-back.log
else
    # API 访问失败，重启【查询 n2n edge 节点信息】后台服务
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】：API 访问失败，重启【查询 n2n edge 节点信息】后台服务" >> $restart_path/check-n2n-edge-query-back.log
    # 调用重启脚本
    bash $restart_path/restart-n2n-edge-query-back.sh
fi
```

3. 再创建脚本 `restart-n2n-edge-query-back.sh` ，用于重启后台服务

```shell
touch restart-n2n-edge-query-back.sh
```

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="n2n-edge-query"
# 【查询 n2n edge 节点信息】后台服务所在路径
back_path="/home/yan/apply/n2n/n2n-edge-query/"
# 重启【查询 n2n edge 节点信息】后台服务脚本所在路径
restart_path="/home/yan/apply/n2n/n2n-edge-query-check/"

# 定义发送命令并可选地休眠的函数
# $1 是要发送的命令
# $2 是可选的休眠时间
send_command() {
    # -x：附加到指定的会话。
    # -S $screen_name：指定要操作的会话名称。
    # -p 0：选择会话中的窗口编号，这里是选择窗口编号为 0 的窗口；如果只有一个窗口，那这就是第一个
    # -X stuff：在选定的窗口中发送字符。
    screen -x -S $screen_name -p 0 -X stuff "$1"

    # 如果提供了休眠时间，则进行休眠
    if [ ! -z "$2" ]; then 
        sleep $2
    fi
}

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 5

# 进入服务器目录
send_command "cd $back_path\r" 5

# 发送启动命令，包括运行参数，将命令发送到会话中，并模拟按下回车键
send_command "python3 n2n-edge-query-back.py -d >> n2n-edge-query-back.log && echo "" >> n2n-edge-query-back.log\r"

# 向日志文件中追加日志
echo "【$(date '+%Y-%m-%d %H:%M:%S')】：【查询 n2n edge 节点信息】后台服务已重启" >> $restart_path/check-n2n-edge-query-back.log
```

4. 设置定时执行：
5. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
6. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 检查【查询 n2n edge 节点信息】接口是否可以访问的脚本，每天 8 点执行
0 8 * * * /home/yan/apply/n2n/n2n-edge-query-check/check-n2n-edge-query-back.sh
# 检查【查询 n2n edge 节点信息】接口是否可以访问的脚本，每天 12 点执行
0 12 * * * /home/yan/apply/n2n/n2n-edge-query-check/check-n2n-edge-query-back.sh
# 检查【查询 n2n edge 节点信息】接口是否可以访问的脚本，每天 18 点执行
0 18 * * * /home/yan/apply/n2n/n2n-edge-query-check/check-n2n-edge-query-back.sh
```

### ②、<span id="1-3-2">不使用 docker 安装服务端</span>

#### Ⅰ、不使用 docker 安装服务端

1. 服务端操作系统为：Ubuntu 22.04.3 LTS
2. 开放端口：`10091`、`10092`
	1. `sudo ufw allow from any to any port 10091`
	2. `sudo ufw allow from any to any port 10092`
3. 使用 root 用户给予 yan 用户 `sudo` 权限

```shell
sudo usermod -aG sudo yan
```

4. 创建目录：`/home/yan/apply/n2n/n2n/`，下载 N2N 服务端：[n2n-3.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-3.0.zip) 放入其中
5. 解压压缩包：`unzip n2n-3.0.zip`
6. 更新软件源、安装 vim、安装配置工具：``

```shell
# 更新软件源：
sudo apt-get update

# 安装 vim：
sudo apt-get install -y vim

# 安装配置工具：
sudo apt-get install -y autoconf automake libtool make pkg-config
```

7. 进入 n2n 目录：

```shell
cd /home/yan/apply/n2n/n2n/
```

8. 依次进行下述每一行命令：

```shell
# 将 autogen.sh 脚本设为可执行
chmod +x autogen.sh

# 执行 autogen.sh 脚本，这个脚本通常负责设置或预处理编译环境，生成配置脚本等
./autogen.sh

# 执行 configure 脚本，这个脚本根据系统环境和用户提供的选项，生成适合当前系统的 Makefile 文件
./configure

# 编译源代码并安装
# 'make' 命令根据前面生成的 Makefile 来编译源代码，生成可执行文件或库文件
# 'make install' 命令则是将编译好的文件安装到指定位置，通常是系统的标准目录下，比如 /usr/local/bin
make && sudo make install
```

9. 创建并编辑配置文件：`vim supernode.conf`，写入下述内容，然后保存退出：

```shell
-t=10091
-p=10092
```

10. 运行 supernode：

```shell
sudo supernode ./supernode.conf
```

11. 检查 supernode 是否在后台运行：

```shell
ps -ef|grep supernode
```

```shell
root@f279e3b2bb3f:/# ps -ef|grep supernode
nobody      1711       1  0 08:34 ?        00:00:00 supernode ./supernode.conf
root        1725    1715  0 08:47 pts/1    00:00:00 grep --color=auto supernode
root@f279e3b2bb3f:/# 
```

#### Ⅱ、查询 n2n edge 节点信息（使用 java 实现）

> 1. 改为使用 java 实现的原因是上面的 py 脚本经常自己停止
> 2. java 工具类：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fyuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar)

1. 创建目录：`/home/yan/apply/n2n/n2n-query-yuehai-tool`，下载 java 工具类：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fyuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
2. 安装 JDK 21；若是安装过程中让选择时区，第一次选择 5 是亚洲，第二次选择 69 是上海

```shell
sudo apt install openjdk-21-jdk
```

3. 通过检查 Java 版本来验证是否成功安装了 JDK

```shell
java -version
```

4. 出现如下输出表示安装成功

```shell
root@734c23cee573:/# java -version
openjdk version "21.0.4" 2024-07-16
OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu224.04)
OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu224.04, mixed mode, sharing)
root@734c23cee573:/# 
```

5. 进入 `/home/yan/apply/n2n/n2n-query-yuehai-tool` 目录

```shell
cd /home/yan/apply/n2n/n2n-query-yuehai-tool
```

6. 启动 jar：

```shell
nohup java -jar yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar >> yuehai-tool.log 2>&1 &
```

7. 访问测试：http://ip:10093/static/n2n-edge-query.html

## 4、windows 客户端配置

1. 防火墙规则允许 `ipv4\ipv6` 入站：输入快捷键 `windows + x + a` 以<font color="#ff0000">管理员模式</font>打开 powershell，执行下面命令就可以开启 v4 和 v6 的入站规则，出站默认就开启的不需要操作

```shell
netsh advfirewall firewall add rule name= "All ICMP V4" protocol=icmpv4:any,any dir=in action=allow

netsh advfirewall firewall add rule name= "All ICMP V6" protocol=icmpv6:any,any dir=in action=allow
```

2. 下载 EasyN2N 客户端：[n2n_client_windows_3.12_Pack_2.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n_client_windows_3.12_Pack_2.zip)，解压后双击 `n2n.exe` 打开（若是被杀毒软件删除，请将其加入白名单）
3. 配置：
	1. 服务器：`服务器ip:10092`
	2. 小组名称：所有人需要是一样的名称
	3. 虚拟网 ip：最好设置为同一网段（也可以选择自动分配，分配的若不是同一网段，再自行修改）
	4. 点击启动

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108093650.png)

5. 服务器右侧显示绿色对号即为连接成功

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108093723.png)

6. 启动后，点击小组名称后的按钮，可打开已连接的主机列表，双击列表项可显示延迟

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108093757.png)

## 5、linux 客户端配置

1. 服务端操作系统为：Ubuntu 22.04.3 LTS
2. 开放端口：`10091`、`10092`
3. 这里假设 docker 已经安装好了，并且拉取了 ubuntu 的镜像，当然如果不用 docker 也可以选择跳过这一大步
4. 创建目录：`/home/docker/docker/volumes/n2n/n2n`，下载 N2N 服务端：[n2n-3.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fn2n-3.0.zip) 放入其中
5. 解压压缩包：`unzip n2n-3.0.zip`
6. 创建容器，包括后台运行、端口映射、授权等：
	1. 其中，`10091` 是作为 Manage 端口，而 `10092` 作为主要端口
	2. 实测的时候发现 `10092` 端口既需要开放 UDP 也需要开放 TCP

```shell
docker run -itd \
-p 10091:10091/tcp \
-p 10091:10091/udp \
-p 10092:10092/tcp \
-p 10092:10092/udp \
--privileged=true \
-v /home/docker/docker/volumes/n2n:/home \
--name ubuntu-n2n-client ubuntu /bin/bash
```

7. 进入该 ubuntu-n2n-client 容器：

```shell
docker exec -it ubuntu-n2n-client /bin/bash
```

8. 更新软件源、安装配置工具：

```shell
# 更新软件源：
apt-get update

# 安装配置工具：
apt-get install -y autoconf automake libtool make
```

9. 进入 n2n 目录：

```shell
cd /home/n2n
```

10. 依次进行下述每一行命令：

```shell
# 将 autogen.sh 脚本设为可执行
chmod +x autogen.sh

# 执行 autogen.sh 脚本，这个脚本通常负责设置或预处理编译环境，生成配置脚本等
./autogen.sh

# 执行 configure 脚本，这个脚本根据系统环境和用户提供的选项，生成适合当前系统的 Makefile 文件
./configure

# 编译源代码并安装
# 'make' 命令根据前面生成的 Makefile 来编译源代码，生成可执行文件或库文件
# 'make install' 命令则是将编译好的文件安装到指定位置，通常是系统的标准目录下，比如 /usr/local/bin
make && make install
```

11. 根据上面知道服务器 ip：`yu.yue-hai.top:10092`，和应该加入的小组：`000123`，则启动命令为：

```shell
edge -d n2n0 -c 000123 -a 192.168.1.2 -l yu.yue-hai.top:10092
```

12. 参数的含义为：
	1. `-d n2n0`：表示创建名为 n2n0 的虚拟网络接口。
	2. `-c 000123`：要加入的网络社区名称。
	3. `-a 192.168.1.2`：分配给虚拟网络接口的 IP 地址。请确保这个地址不会与本地网络冲突。
	4. `-l yu.yue-hai.top:10092`：指定服务端的 IP 地址和端口。

13. 命令行输出：

```shell
root@a45399aeccce:/home/n2n# edge -d n2n0 -c 000123 -a 192.168.1.2 -l yu.yue-hai.top:10092
15/Mar/2024 06:29:54 [edge_utils.c:3774] adding supernode = yu.yue-hai.top:10092
15/Mar/2024 06:29:54 [edge.c:1085] starting n2n edge 3.0.0 Mar 15 2024 06:29:19
15/Mar/2024 06:29:54 [edge.c:1091] using compression: none.
15/Mar/2024 06:29:54 [edge.c:1092] using null cipher.
15/Mar/2024 06:29:54 [edge_utils.c:392] number of supernodes in the list: 1
15/Mar/2024 06:29:54 [edge_utils.c:394] supernode 0 => yu.yue-hai.top:10092
15/Mar/2024 06:29:54 [edge_utils.c:467] WARNING: encryption is disabled in edge
15/Mar/2024 06:29:54 [edge_utils.c:483] successfully created resolver thread
15/Mar/2024 06:29:54 [edge.c:1116] use manually set IP address
15/Mar/2024 06:29:54 [edge.c:1231] created local tap device IP: 192.168.1.2, Mask: 255.255.255.0, MAC: 52:A0:4F:7C:B6:26
root@a45399aeccce:/home/n2n# 
```

14. 检查 edge 是否在后台运行：

```shell
ps -ef|grep edge
```

```shell
yan@yan:~/apply/game/n2n/n2n$ ps -ef|grep edge
nobody    970705       1  0 12:46 ?        00:00:00 edge -d n2n0 -c 000123 -a 192.168.1.2 -l 127.0.0.1:10092
yan       970897  961863  0 12:48 pts/0    00:00:00 grep --color=auto edge

yan@yan:~/apply/game/n2n/n2n$ 
```

15. 此时在 windows 系统上同时连接上 n2n 客户端，点击小组名称后的按钮，打开已连接的主机列表，发现多了一个客户端，且虚拟 ip 与刚才设置的相同，即为连接成功，双击列表项查看延迟

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108093757.png)

## 6、绕过 UDP 屏蔽

> 1. 如果服务器在大陆外或国外，或者是家用网络，有可能会出现 UDP 屏蔽或 QoS
> 2. 下面是一种解决方法：使用 gnb_udp_over_tcp 这个工具，实现将 UDP 数据转换为 TCP 进行传输，绕开 UDP 限制
> 3. github 地址：https://github.com/gnbdev/gnb_udp_over_tcp
> 4. 本地下载：[gnb_udp_over_tcp.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fgnb_udp_over_tcp.zip)

### ⓪、gnb_udp_over_tcp 命令解释

1. udp 转为 tcp；服务端使用，用于将 n2n 的 udp 数据转为 tcp，经由监听的 TCP 端口发出

```shell
gnb_udp_over_tcp -t -l 监听的TCP端口 UDP源地址 UDP源端口
```

2. tcp 转为 udp；客户端使用，用于将接收的服务端发送过来的的 tcp 数据转为 udp，然后转发给本地的 n2n 使用

```shell
gnb_udp_over_tcp -u -l 监听的UDP端口 TCP源地址 TCP源端口
```

### ①、ubuntu 服务器配置

1. 服务器开启 `10095` 端口，作为转发端口

```shell
sudo ufw allow from any to any port 10095
```

2. ubuntu 服务端先正常编译安装 n2n：
	1. [使用 docker 安装服务端](#1-3-1)
	2. [不使用 docker 安装服务端](#1-3-2)
3. 下载上面的 [gnb_udp_over_tcp.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fgnb_udp_over_tcp.zip)，上传到服务器的对应目录中：
	1.  若是使用 docker 安装的，上传到：`/home/docker/docker/volumes/n2n/`
	2. 若是不是使用 docker 安装的，上传到：`/home/yan/apply/n2n/`
4. 进入对应目录

```shell
# 若是使用 docker 安装的，进入：
cd /home/docker/docker/volumes/n2n/

# 若是不是使用 docker 安装的，进入：
cd /home/yan/apply/n2n/
```

5. 解压：

```shell
unzip gnb_udp_over_tcp.zip
```

4. 进入目录 `gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
cd gnb_udp_over_tcp/bin/Linux_x86_64/
```

5. 给予权限：

```shell
chmod 755 gnb_udp_over_tcp
```

6. 创建日志文件：

```shell
touch gnb_udp_over_tcp.log
```

7. 使用 nohup 后台运行：
	1. `-t`：表示启用 TCP 模式，即将 UDP 数据转换为 TCP 数据。
	2. `-l 10095`：`-l` 参数后跟的是监听的 TCP 端口号，这里设置为 10095，表示该服务将监听端口 10095 上的 TCP 连接
	3. `127.0.0.1`：这是 UDP 源地址，这里使用的是本地回环地址（localhost），指的是本机
	4. `10092`：<font color="#ff0000">n2n 使用的端口</font>，即监听的 UDP 源端口，UDP 数据将从这个端口接收

```shell
nohup ./gnb_udp_over_tcp -t -l 10095 127.0.0.1 10092 >> gnb_udp_over_tcp.log 2>&1 &
```

7. 查看进程的详细信息：

```shell
ps aux | grep gnb_udp_over_tcp
```

```shell
ps aux | grep gnb_udp_over_tcp
yan        56574  1.3  0.0   2940  1624 pts/0    S    08:51   0:01 ./gnb_udp_over_tcp -t -l 10095 127.0.0.1 10092
yan        56680  0.0  0.0   6432   712 pts/0    S+   08:53   0:00 grep --color=auto gnb_udp_over_tcp

yan@yuehai:~/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ 
```

8. 结束后台进程：

```shell
kill 56574
```

9. 但是这个办法有一个问题，就是长时间运行后，n2n 就无法连接成功了，现在的解决办法是定时重启

### ②、ubuntu 服务端定时重启脚本

1. 进入对应目录：
	1. 若是使用 docker 安装的，进入：`/home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/`
	2. 若是不是使用 docker 安装的，进入：`/home/yan/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
# 若是使用 docker 安装的，进入：
cd /home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/

# 若是不是使用 docker 安装的，进入：
cd /home/yan/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/
```

2. 创建脚本 `restart_process.sh` 和日志文件 `restart_process.log`：

```shell
touch restart_process.sh restart_process.log
```

3. 编写内容（注意程序路径）：

```shell
#!/bin/bash

# 定义程序路径
file_path="/home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64"

# 杀死现有的后台程序进程
pkill -f 'gnb_udp_over_tcp -t -l 10095'

# 等待几秒确保进程已完全停止
sleep 5

# 添加一个空行
echo "" >> "${file_path}/gnb_udp_over_tcp.log"
# 分隔符
echo "----------------------------------------------------------------" >> "${file_path}/gnb_udp_over_tcp.log"
# 向文件中写入重启时间
echo "【$(date "+%Y-%m-%d %H:%M:%S")】重启完成" >> "${file_path}/gnb_udp_over_tcp.log"

# 重新启动程序
nohup ${file_path}/gnb_udp_over_tcp -t -l 10095 127.0.0.1 10092 >> "${file_path}/gnb_udp_over_tcp.log" 2>&1 &

# 向文件中写入重启时间
echo "【$(date "+%Y-%m-%d %H:%M:%S")】重启完成" >> "${file_path}/restart_process.log"
```

4. 给予权限：

```shell
chmod 755 restart_process.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令（注意程序路径）：

```shell
# 定时重启 gnb_udp_over_tcp，每天每 30 分钟执行一次
*/30 * * * * /home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/restart_process.sh
```

### ③、windows 客户端配置

1. 下载上面的 [gnb_udp_over_tcp.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fgnb_udp_over_tcp.zip)，解压，进入目录 `bin\Window10_x86_64`
2. 在目录中，按住键盘的 shift 键，然后点击鼠标右键，选择：在此处打开 Powershell 窗口

![|625](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240809134147%201.png)

3. 之后会弹出一个窗口，在其中输入以下内容并回车：
	1. `-u`：表示启用 UDP 模式，即将接收到的 TCP 数据转换为 UDP 数据。
	2. `-l 10092`：<font color="#ff0000">n2n 使用的端口</font>，`-l` 参数后跟的是监听的 UDP 端口号，这里设置为 10092，表示该服务将监听端口 10092 上的 UDP 数据。
	3. `83.229.120.176`：这是 TCP 源地址，即服务端的 IP 地址；<font color="#ff0000">请根据要连接的服务端自行修改这个参数</font>
	4. `10095`：这是服务端监听的 TCP 端口号。

```shell
.\gnb_udp_over_tcp.exe -u -l 10092 83.229.120.176 10095
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240809131849.png)

4. 若是不想手动输入上面的命令，也可以直接双击目录的脚本 `run_gnb_udp_over_tcp.bat`，会自动执行该命令

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240809134324.png)

5. 打开 n2n，服务端填写：`127.0.0.1:10092`，点击启动，等待时间会稍长一点，大概六七秒
6. 等待右侧出现绿色对号，即为连接成功

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108103751.png)

### ④、ubuntu 客户端配置

1. ubuntu 客户端先正常编译安装 n2n：
	1. [使用 docker 安装服务端](#1-3-1)
	2. [不使用 docker 安装服务端](#1-3-2)
2. 下载上面的 [gnb_udp_over_tcp.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2Fgnb_udp_over_tcp.zip)，上传到服务器的对应目录中
	1.  若是使用 docker 安装的，上传到：`/home/docker/docker/volumes/n2n/`
	2. 若是不是使用 docker 安装的，上传到：`/home/yan/apply/n2n/`
3. 进入对应目录：

```shell
# 若是使用 docker 安装的，进入：
cd /home/docker/docker/volumes/n2n/

# 若是不是使用 docker 安装的，进入：
cd /home/yan/apply/n2n/
```

4. 解压：

```shell
unzip gnb_udp_over_tcp.zip
```

4. 进入目录 `gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
cd gnb_udp_over_tcp/bin/Linux_x86_64/
```

5. 给予权限：

```shell
chmod 755 gnb_udp_over_tcp
```

6. 创建日志文件：

```shell
touch gnb_udp_over_tcp.log
```

7. 使用 nohup 后台运行：
	1. `-t`：表示启用 TCP 模式，即将 UDP 数据转换为 TCP 数据。
	2. `-l 10095`：`-l` 参数后跟的是监听的 TCP 端口号，这里设置为 10095，表示该服务将监听端口 10095 上的 TCP 连接
	3. `127.0.0.1`：这是 UDP 源地址，这里使用的是本地回环地址（localhost），指的是本机
	4. `10092`：<font color="#ff0000">n2n 使用的端口</font>，即监听的 UDP 源端口，UDP 数据将从这个端口接收

```shell
nohup ./gnb_udp_over_tcp -u -l 10092 83.229.120.176 10095 > gnb_udp_over_tcp.log 2>&1 &
```

7. 查看进程的详细信息：

```shell
ps aux | grep gnb_udp_over_tcp
```

```shell
yan@yan:~/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ ps aux | grep gnb_udp_over_tcp
yan       983515  1.8  0.0   3076  1664 ?        S    15:31   0:09 /home/yan/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/gnb_udp_over_tcp -u -l 10092 83.229.120.176 10095
yan       984195  0.0  0.0  17888  2560 pts/0    S+   15:39   0:00 grep --color=auto gnb_udp_over_tcp

yan@yan:~/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ 
```

8. 结束后台进程：

```shell
kill 983515
```

### ⑤、ubuntu 客户端定时重启脚本

1. 进入对应目录：
	1. 若是使用 docker 安装的，进入：`/home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/`
	2. 若是不是使用 docker 安装的，进入：`/home/yan/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
# 若是使用 docker 安装的，进入：
cd /home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/

# 若是不是使用 docker 安装的，进入：
cd /home/yan/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/
```

2. 创建脚本 `restart_process.sh` 和日志文件 `restart_process.log`：

```shell
touch restart_process.sh restart_process.log
```

3. 编写内容：

```shell
#!/bin/bash

# 定义文件路径
file_path="/home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64"

# 杀死现有的后台程序进程
pkill -f 'gnb_udp_over_tcp -u -l 10092'

# 等待几秒确保进程已完全停止
sleep 5

# 重新启动程序
nohup ${file_path}/gnb_udp_over_tcp -u -l 10092 83.229.120.176 10095 > "${file_path}/gnb_udp_over_tcp.log" 2>&1 &

# 向文件中写入重启时间
echo "【$(date "+%Y-%m-%d %H:%M:%S")】重启完成" >> "${file_path}/restart_process.log"
```

4. 给予权限：

```shell
chmod 755 restart_process.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 定时重启 gnb_udp_over_tcp，每天每 30 分钟执行一次
*/30 * * * * /home/docker/docker/volumes/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/restart_process.sh
```

# 二、

# 三、

# 四、

# 五、

# 六、

# 七、

# 八、