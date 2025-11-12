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

2. 下载 EasyN2N 客户端：[EasyN2N_3.3.zip](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/EasyN2N_3.3.zip)，解压后双击 `EasyN2N.exe` 打开（若是被杀毒软件删除，请将其加入白名单）<font color="#ff0000">若是被杀毒软件误删，请加入白名单</font>

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020251111143000.png)

3. 配置：
	1. 服务器：`服务器ip:41984`
	2. 小组名称：所有人需要是一样的名称
	3. 虚拟网 ip：最好设置为同一网段（也可以选择自动分配，分配的若不是同一网段，再自行修改）
	4. 点击启动

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020251111134832.png)

4. 服务器右侧显示绿色对号即为连接成功

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020251107161831.png)

5. 启动后，点击小组名称后的按钮，可打开已连接的主机列表，双击列表项可显示延迟

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020251111131138.png)

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






