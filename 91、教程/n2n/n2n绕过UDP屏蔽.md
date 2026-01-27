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
