> 1. 项目 github：https://github.com/ntop/n2n/tree/3.0
> 2. dockerHub 地址：https://hub.docker.com/r/jonnyan404/n2n-v3
> 3. N2N 服务端软件 n2n-3.0：
> 	1. github 下载地址：https://github.com/ntop/n2n/releases/tag/3.0
> 	2. 本地下载：[n2n-3.0.zip](../../../Docker/attachments/n2n-3.0.zip)
> 4. N2N 客户端软件 EasyN2N：
> 	1. 下载地址：https://bugxia.com/357.html
> 	2. 本地下载：[EasyN2N_3.3.zip](../../../Docker/attachments/EasyN2N_3.3.zip)
> 5.  java 查询程序：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](../../../Docker/attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar)

## 1、端口说明

1. 端口：41900、41983、41984
2. 41900：java 查询程序使用端口
3. 41983 (TCP, Supernode 的 -t 端口)：
	1. 角色：Supernode (超级节点) 的管理和协调端口
	2. 用途：Edge (边缘) 节点启动时，必须主动连接此 TCP 端口。它专门用于处理控制信令：包括节点注册、上报状态、获取网络中其他节点的地址信息，以及在 Supernode 协助下协商 P2P 通信。这个端口不传输实际的 VPN 业务数据
4. 41984 (UDP, Edge 的 -p 端口)：
	1. 角色：Edge (边缘节点) 的本地数据端口
	2. 用途：这是 Edge 节点在自己设备上绑定的 UDP 端口，用于收发所有实际的 VPN 业务数据。当两个 Edge 节点成功建立 P2P 连接后，它们加密后的数据流就通过各自的这个端口（或其 NAT 映射端口）直接传输

## 2、介绍

1. N2N（Node to Node）是一种点对点（P2P）网络连接协议，用于在网络中直接连接节点（计算机或设备），而无需通过中心服务器。N2N 协议允许网络中的节点之间直接通信，这种直接连接方式可以提供更高的性能和更好的隐私保护。
2. N2N 协议的特点包括：
	1. **点对点连接**：N2N 允许节点之间直接建立连接，无需经过中心服务器，从而减少了网络通信的中间环节，提高了通信效率。
	2. **加密通信**：N2N 支持对通信数据进行加密，保护通信内容的隐私和安全。
	3. **灵活性**：N2N 协议可以在不同的网络环境中使用，包括局域网、广域网和互联网，提供了灵活的网络连接方式。
	4. **开放性**：N2N 是一个开放的协议，可以被集成到各种应用和系统中，为不同的场景提供点对点连接的能力。
3. N2N 协议可以用于构建各种点对点的网络应用，例如直接设备之间的通信、对等网络文件共享、实时音视频通话等。在实际应用中，N2N 协议通常与其他网络技术和安全机制结合使用，以构建更加安全、高效的点对点通信系统。
4. 当然也可以用来改善游戏联机网络
5. 本次安装配置基于 N2N 的 V3 版本，具体区别请参考：[N2N版本选择介绍（v1\v2\v2s\v3区别\使用方法教程\免费服务器）](https://bugxia.com/n2n_version_intro)
6. 本次配置主要是以 Linux ubuntu 为服务端、Windows 为客户端

## 3、服务端超级节点部署

### ①、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/volumes/services/other/n2n/config/`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 41900:41900 \
-p 41983:5645/udp \
-p 41984:7777/tcp \
-p 41984:7777/udp \
-e START_TYPE=supernode \
-v /home/docker/volumes/services/other/n2n/config:/app/config \
--network yuehai-net \
--name n2n-supernode \
jonnyan404/n2n-v3:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 n2n-supernode 的服务
    n2n-supernode:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: jonnyan404/n2n-v3:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: n2n-supernode
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # java 查询程序使用端口
            - "41900:41900"
            # Supernode (超级节点) 的管理和协调端口
            - "41983:5645/udp"
            # Edge (边缘节点) 的本地数据端口
            - "41984:7777/tcp"
            - "41984:7777/udp"
        # 定义环境变量
        environment:
            # 设置 n2n 的启动类型为 supernode，即表明此容器将作为超级节点运行
            - START_TYPE=supernode
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 配置目录
            - /home/docker/volumes/services/other/n2n/config:/app/config
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络
            - yuehai-net

# 在文件末尾定义此 Compose 文件中使用的所有网络
networks:
    # 定义一个名为 yuehai-net 的网络配置
    yuehai-net:
        # 将此网络声明为外部网络
        # external: true 的意思是：不要创建这个网络，而是去使用一个已经存在的、名字完全相同的网络
        external: true
```

### ②、ubuntu 直接安装

1. 服务端操作系统为：Ubuntu 22.04.3 LTS
2. 开放端口：`41983`、`41984`
	1. `sudo ufw allow from any to any port 41983`
	2. `sudo ufw allow from any to any port 41984`
3. 创建目录：`/home/yan/app/internet/NetworkTools/n2n/`，下载 N2N 服务端：[n2n-3.0.zip](../../../Docker/attachments/n2n-3.0.zip) 放入其中
4. 解压压缩包：`unzip n2n-3.0.zip`
5. 更新软件源、安装 vim、安装配置工具：``

```shell
# 更新软件源：
sudo apt-get update

# 安装 vim：
sudo apt-get install -y vim

# 安装配置工具：
sudo apt-get install -y autoconf automake libtool make pkg-config
```

6. 进入 n2n 目录：

```shell
cd /home/yan/app/internet/NetworkTools/n2n/
```

7. 依次进行下述每一行命令：

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

8. 创建并编辑配置文件：`vim supernode.conf`，写入下述内容，然后保存退出：

```shell
-t=41983
-p=41984
```

9. 运行 supernode：

```shell
sudo supernode ./supernode.conf
```

10. 检查 supernode 是否在后台运行：

```shell
ps -ef|grep supernode
```

```shell
root@f279e3b2bb3f:/# ps -ef|grep supernode
nobody      1711       1  0 08:34 ?        00:00:00 supernode ./supernode.conf
root        1725    1715  0 08:47 pts/1    00:00:00 grep --color=auto supernode
root@f279e3b2bb3f:/# 
```

## 4、客户端边缘节点使用

### ①、服务器列表

| 服务器地址                | 更新时间       | 归属  | 是否需要 udp 转发 | 备注                     |
| -------------------- | ---------- | --- | ----------- | ---------------------- |
| 101.200.86.248:41984 | 2024/12/17 | 月海  | 否           | 可用，但是只有 3m 带宽，人多了可能会卡顿 |

### ②、windows 客户端使用

1. 防火墙规则允许 `ipv4\ipv6` 入站：输入快捷键 `windows + x + a` 以<font color="#ff0000">管理员模式</font>打开 powershell，执行下面命令就可以开启 v4 和 v6 的入站规则，出站默认就开启的不需要操作

```shell
netsh advfirewall firewall add rule name= "All ICMP V4" protocol=icmpv4:any,any dir=in action=allow

netsh advfirewall firewall add rule name= "All ICMP V6" protocol=icmpv6:any,any dir=in action=allow
```

2. 下载 EasyN2N 客户端：[EasyN2N_3.3.zip](../../../Docker/attachments/EasyN2N_3.3.zip)，解压后双击 `EasyN2N.exe` 打开（若是被杀毒软件删除，请将其加入白名单）<font color="#ff0000">若是被杀毒软件误删，请加入白名单</font>

![](../../../Docker/attachments/Pasted%20image%2020251111143000.png)

3. 配置：
	1. 服务器：`服务器ip:41984`
	2. 小组名称：所有人需要是一样的名称
	3. 虚拟网 ip：最好设置为同一网段（也可以选择自动分配，分配的若不是同一网段，再自行修改）
	4. 点击启动

![](../../../Docker/attachments/Pasted%20image%2020251111134832.png)

4. 服务器右侧显示绿色对号即为连接成功

![](../../../Docker/attachments/Pasted%20image%2020251107161831.png)

5. 启动后，点击小组名称后的按钮，可打开已连接的主机列表，双击列表项可显示延迟

![](../../../Docker/attachments/Pasted%20image%2020251111131138.png)

### ③、linux 客户端使用

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/services/other/n2n/config/`
2. 使用 docker run 部署：

```shell
docker run -d \
-e N2N_SERVER_HOST=服务器IP:41984 \
-e N2N_IP=192.168.2.2 \
-e N2N_COMMUNITY=000123 \
-e N2N_KEY=000123 \
-v /vol1/1000/docker/services/other/n2n/config:/app/config \
--device /dev/net/tun:/dev/net/tun \
--net=host \
--cap-add=NET_ADMIN \
--name n2n-edge \
jonnyan404/n2n-v3:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 n2n-edge 的服务
    n2n-edge:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: jonnyan404/n2n-v3:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: n2n-edge
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 直接使用主机的网络堆栈，容器将共享主机的 IP 地址和端口空间
        network_mode: host
        # 添加 Linux 内核能力
        cap_add:
            # 赋予容器进行网络相关管理操作的权限，例如创建网络接口
            - NET_ADMIN
        # 将宿主机的设备映射到容器内部
        devices:
            # 映射 TUN 设备，这是 VPN 类应用所必需的虚拟网络接口
            - /dev/net/tun:/dev/net/tun
        # 定义环境变量
        environment:
            # 设置 Supernode (超级节点) 的地址和端口
            - N2N_SERVER_HOST=服务器IP:41984
            # 设置此 edge 节点在 n2n 网络中的静态 IP 地址
            - N2N_IP=192.168.2.2
            # 设置 n2n 网络的社区名称（相当于群组名）
            - N2N_COMMUNITY=000123
            # 设置 n2n 网络的加密密钥，一般和社区名称相同
            - N2N_KEY=000123
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 配置目录
            - /vol1/1000/docker/services/other/n2n/config:/app/config
```

## 5、查询 n2n edge 节点信息

### ①、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. jar 包目录：`/home/docker/volumes/services/other/n2n-query-yuehai-tool/`，下载 java 工具类 [yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](../../../Docker/attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
2. 使用 docker run 部署：

```shell
docker run -d \
-e TZ=Asia/Shanghai \
-v /home/docker/volumes/services/other/n2n-query-yuehai-tool:/container/path \
--network=container:n2n-supernode \
--restart=unless-stopped \
--name n2n-query-yuehai-tool \
openjdk:21 \
java -jar /container/path/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 n2n-query-yuehai-tool 的服务
    n2n-query-yuehai-tool:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: openjdk:21
        # 设置容器的固定名称，方便识别和管理
        container_name: n2n-query-yuehai-tool
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 设置网络模式，此容器将直接使用 n2n-supernode 服务的网络，共享同一个 IP 地址和端口空间
        # 请确保 n2n-supernode 这个容器名称正确
        network_mode: "service:n2n-supernode"
        # 定义环境变量
        environment:
            # 设置容器的时区为上海
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则
        volumes:
            # jar 包目录
            - /home/docker/volumes/services/other/n2n-query-yuehai-tool:/container/path
        # 指定容器启动时执行的命令：运行指定的 Jar 文件
        command: java -jar /container/path/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar
```

### ②、ubuntu 直接安装

1. 创建目录：`/home/docker/volumes/services/other/n2n-query-yuehai-tool`，下载 java 工具类 [yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](../../../Docker/attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
2. 安装 JDK 21；若是安装过程中让选择时区，第一次选择 5 是亚洲，第二次选择 69 是上海

```shell
apt install openjdk-21-jdk
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

5. 进入 `/home/docker/volumes/services/other/n2n-query-yuehai-tool` 目录

```shell
cd /home/docker/volumes/services/other/n2n-query-yuehai-tool
```

6. 启动 jar：

```shell
nohup java -jar yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar >> yuehai-tool.log 2>&1 &
```

### ③、访问

1. 访问测试：http://ip:41900/static/n2n-edge-query.html

## 6、绕过 UDP 屏蔽

> 1. 如果服务器在大陆外或国外，或者是家用网络，有可能会出现 UDP 屏蔽或 QoS
> 2. 下面是一种解决方法：使用 gnb_udp_over_tcp 这个工具，实现将 UDP 数据转换为 TCP 进行传输，绕开 UDP 限制
> 3. github 地址：https://github.com/gnbdev/gnb_udp_over_tcp
> 4. 本地下载：[gnb_udp_over_tcp.zip](../../../Docker/attachments/gnb_udp_over_tcp.zip)

### ⓪、gnb_udp_over_tcp 命令解释

1. udp 转为 tcp；服务端使用，用于将 n2n 的 udp 数据转为 tcp，经由监听的 TCP 端口发出

```shell
gnb_udp_over_tcp -t -l 监听的TCP端口 UDP源地址 UDP源端口
```

2. tcp 转为 udp；客户端使用，用于将接收的服务端发送过来的的 tcp 数据转为 udp，然后转发给本地的 n2n 使用

```shell
gnb_udp_over_tcp -u -l 监听的UDP端口 TCP源地址 TCP源端口
```

### ①、服务端超级节点配置

#### Ⅰ、ubuntu 服务端配置

1. 服务端先正常编译安装 n2n 服务端，然后开启 `41985` 端口，作为转发端口

```shell
sudo ufw allow from any to any port 41985
```

2. 下载上面的 [gnb_udp_over_tcp.zip](../../../Docker/attachments/gnb_udp_over_tcp.zip)，上传到服务器的对应目录中，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`
3. 进入对应目录

```shell
cd /home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/
```

4. 解压：

```shell
unzip gnb_udp_over_tcp.zip
```

5. 进入目录 `gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
cd gnb_udp_over_tcp/bin/Linux_x86_64/
```

6. 给予权限：

```shell
chmod 755 gnb_udp_over_tcp
```

7. 创建日志文件：

```shell
touch gnb_udp_over_tcp.log
```

8. 使用 nohup 后台运行：
	1. `-t`：表示启用 TCP 模式，即将 UDP 数据转换为 TCP 数据
	2. `-l 41985`：`-l` 参数后跟的是监听的 TCP 端口号，这里设置为 41985，表示该服务将监听端口 41985 上的 TCP 连接
	3. `127.0.0.1`：这是 UDP 源地址，这里使用的是本地回环地址（localhost），指的是本机
	4. `41984`：<font color="#ff0000">n2n 使用的端口</font>，即监听的 UDP 源端口，UDP 数据将从这个端口接收

```shell
nohup ./gnb_udp_over_tcp -t -l 41985 127.0.0.1 41984 >> gnb_udp_over_tcp.log 2>&1 &
```

9. 查看进程的详细信息：

```shell
ps aux | grep gnb_udp_over_tcp
```

```shell
ps aux | grep gnb_udp_over_tcp
yan        56574  1.3  0.0   2940  1624 pts/0    S    08:51   0:01 ./gnb_udp_over_tcp -t -l 41985 127.0.0.1 41984
yan        56680  0.0  0.0   6432   712 pts/0    S+   08:53   0:00 grep --color=auto gnb_udp_over_tcp

yan@yuehai:~/apply/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ 
```

10. 结束后台进程：

```shell
kill 56574
```

11. 但是这个办法有一个问题，就是长时间运行后，n2n 就无法连接成功了，现在的解决办法是定时重启

#### Ⅱ、ubuntu 服务端定时重启脚本

1. 进入对应目录，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`

```shell
cd /home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/
```

2. 创建脚本 `restart_process.sh` 和日志文件 `restart_process.log`：

```shell
touch restart_process.sh restart_process.log
```

3. 编写内容（注意程序路径）：

```shell
#!/bin/bash

# 定义程序路径
file_path="/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/gnb_udp_over_tcp/bin/Linux_x86_64"

# 杀死现有的后台程序进程
pkill -f 'gnb_udp_over_tcp -t -l 41985'

# 等待几秒确保进程已完全停止
sleep 5

# 添加一个空行
echo "" >> "${file_path}/gnb_udp_over_tcp.log"
# 分隔符
echo "----------------------------------------------------------------" >> "${file_path}/gnb_udp_over_tcp.log"
# 向文件中写入重启时间
echo "【$(date "+%Y-%m-%d %H:%M:%S")】重启完成" >> "${file_path}/gnb_udp_over_tcp.log"

# 重新启动程序
nohup ${file_path}/gnb_udp_over_tcp -t -l 41985 127.0.0.1 41984 >> "${file_path}/gnb_udp_over_tcp.log" 2>&1 &

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
*/30 * * * * /home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/gnb_udp_over_tcp/bin/Linux_x86_64/restart_process.sh
```

### ②、客户端边缘节点配置

#### Ⅰ、windows 客户端配置

1. 下载上面的 [gnb_udp_over_tcp.zip](../../../Docker/attachments/gnb_udp_over_tcp.zip)，解压，进入目录 `bin\Window10_x86_64`
2. 在目录中，按住键盘的 shift 键，然后点击鼠标右键，选择：在此处打开 Powershell 窗口

![](../../../Docker/attachments/Pasted%20image%2020251111131416.png)

3. 之后会弹出一个窗口，在其中输入以下内容并回车：
	1. `-u`：表示启用 UDP 模式，即将接收到的 TCP 数据转换为 UDP 数据
	2. `-l 41984`：<font color="#ff0000">n2n 使用的端口</font>，`-l` 参数后跟的是监听的 UDP 端口号，这里设置为 41984，表示该服务将监听端口 41984 上的 UDP 数据
	3. `83.229.120.176`：这是 TCP 源地址，即服务端的 IP 地址；<font color="#ff0000">请根据要连接的服务端自行修改这个参数</font>
	4. `41985`：这是服务端监听的 TCP 端口号

```shell
.\gnb_udp_over_tcp.exe -u -l 41984 83.229.120.176 41985
```

![](../../../Docker/attachments/Pasted%20image%2020251111131819.png)

4. 若是不想手动输入上面的命令，也可以直接双击目录的脚本 `run_gnb_udp_over_tcp.bat`，会自动执行该命令；但是这种脚本的方式有时会失败，如果失败，需手动输入命令

![](../../../Docker/attachments/Pasted%20image%2020251111132220.png)

5. 打开 n2n，服务端填写：`127.0.0.1:41984`，点击启动，等待时间会稍长一点，大概六七秒
6. 等待右侧出现绿色对号，即为连接成功

![](../../../Docker/attachments/Pasted%20image%2020251111132524.png)

#### Ⅱ、ubuntu 客户端配置

1. 客户端先正常编译安装 n2n 客户端
2. 下载上面的 [gnb_udp_over_tcp.zip](../../../Docker/attachments/gnb_udp_over_tcp.zip)，上传到服务器的对应目录中，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`
3. 进入对应目录：

```shell
cd /home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/
```

4. 解压：

```shell
unzip gnb_udp_over_tcp.zip
```

5. 进入目录 `gnb_udp_over_tcp/bin/Linux_x86_64/`

```shell
cd gnb_udp_over_tcp/bin/Linux_x86_64/
```

6. 给予权限：

```shell
chmod 755 gnb_udp_over_tcp
```

7. 创建日志文件：

```shell
touch gnb_udp_over_tcp.log
```

8. 使用 nohup 后台运行：
	1. `-u`：表示启用 UDP 模式，即将 TCP 数据转换为 UDP 数据
	2. `-l 41985`：`-l` 参数后跟的是监听的 TCP 端口号，这里设置为 41985，表示该服务将监听端口 41985 上的 TCP 连接
	3. `127.0.0.1`：这是 UDP 源地址，这里使用的是本地回环地址（localhost），指的是本机
	4. `41984`：<font color="#ff0000">n2n 使用的端口</font>，即监听的 UDP 源端口，UDP 数据将从这个端口接收

```shell
nohup ./gnb_udp_over_tcp -u -l 41984 83.229.120.176 41985 > gnb_udp_over_tcp.log 2>&1 &
```

9. 查看进程的详细信息：

```shell
ps aux | grep gnb_udp_over_tcp
```

```shell
yan@yan:~/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ ps aux | grep gnb_udp_over_tcp
yan       983515  1.8  0.0   3076  1664 ?        S    15:31   0:09 /home/yan/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64/gnb_udp_over_tcp -u -l 41984 83.229.120.176 41985
yan       984195  0.0  0.0  17888  2560 pts/0    S+   15:39   0:00 grep --color=auto gnb_udp_over_tcp

yan@yan:~/apply/game/n2n/gnb_udp_over_tcp/bin/Linux_x86_64$ 
```

10. 结束后台进程：

```shell
kill 983515
```

#### Ⅲ、ubuntu 客户端定时重启脚本

1. 进入对应目录，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`

```shell
cd /home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/
```

2. 创建脚本 `restart_process.sh` 和日志文件 `restart_process.log`：

```shell
touch restart_process.sh restart_process.log
```

3. 编写内容：

```shell
#!/bin/bash

# 定义文件路径
file_path="/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/gnb_udp_over_tcp/bin/Linux_x86_64"

# 杀死现有的后台程序进程
pkill -f 'gnb_udp_over_tcp -u -l 41984'

# 等待几秒确保进程已完全停止
sleep 5

# 重新启动程序
nohup ${file_path}/gnb_udp_over_tcp -u -l 41984 83.229.120.176 41985 > "${file_path}/gnb_udp_over_tcp.log" 2>&1 &

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

## 7、n2n 的常见问题解决

### ①、点击启动后没有马上显示成功

1. 连接时，从点击启动到连接成功有时等待时间会稍长一点，等待 10 秒左右看看
2. 当在连接成功的状态下，点击停止断开连接后马上再点击启动（或点击重启），并不会马上重连，需要等待 1 ~ 2 分钟，这是服务器机制问题，等待即可

### ②、NAT 类型问题

1. 点击测试工具 -> NAT 检测，点击开始检测

![](../../../Docker/attachments/Pasted%20image%2020251111143709.png)

2. 若是显示检测失败或结果不是下面的四种，请点击切换服务器，然后多次测试
3. 若检测结果是 `Symmetric NAT`，说明当前机器是不可以使用 n2n 的，若想使用，请自行修改光猫，百度搜索：NAT 类型修改
	1. [家用路由器修改NAT1](https://www.bilibili.com/read/cv22212682/)
	2. [网络类型NAT3改NAT1 基于（联通）光猫桥接、路由器红米AX5、win10系统](https://blog.csdn.net/qq_46648437/article/details/113747066)
	3. [如何提升NAT类型，NAT提升至full_cone，设置光猫](https://blog.csdn.net/weixin_42168194/article/details/106037065)
4. 若不是 `Symmetric NAT`，而是其他三种，说明无法连接的原因不在这里
5. 几种常见的 NAT 类型：
	4. Full Cone
	5. Restricted Cone
	6. Port Restricted Cone
	7. Symmetric NAT

### ③、虚拟 ip 冲突

1. 进入下面的网址查看一下 ip 是不是已经被使用了：
	1. 若是使用服务器地址 101.200.86.248 连接：[查询 n2n edge 节点列表](http://101.200.86.248:41900/static/n2n-edge-query.html)
	2. 其他的服务器地址，则修改下面连接中的 ip 进行访问：http://ip:41900/static/n2n-edge-query.html
2. ip 是唯一的，ip 相同时即使小组不同也会导致冲突，无法连接
3. 和朋友一起联机的话，ip 前三位需要相同，比如：`192.168.1`，最后一位可选 `1 ~ 254`
4. 挑一个没有被使用的就可以了

![](../../../Docker/attachments/Pasted%20image%2020251111144005.png)

### ④、windows 防火墙的问题

1. 右键开始菜单，选择以**管理员模式**打开 `powershell`，执行下面命令就可以开启 v4 和 v6 的入站规则
2. 开启 v4 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V4" protocol=icmpv4:any,any dir=in action=allow
```

3. 开启 v6 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V6" protocol=icmpv6:any,any dir=in action=allow
```

![](../../../Docker/attachments/Pasted%20image%2020251111144121.png)

### ⑤、

### ⑥、

## 8、

