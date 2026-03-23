# 一、安装系统

## 1、默认账号密码

1. 账号：`root
2. 密码：`password`

## 2、


# 二、分区挂载磁盘

## 1、分区说明

1. `/dev/root` 挂载在 `/rom`
	1. 角色：系统的基石 (只读层)
	2. 解释：这里存放的是路由器出厂时的固件文件
	3. 特点：它是只读的 (Read-Only)。无论怎么折腾，哪怕把系统玩坏了，这一层永远不会变。当执行恢复出厂设置时，系统其实就是把其他层都扔掉，只保留这一层
2. `/dev/loop0` (或之后你的 28GB 分区) 挂载在 `/overlay`
	1. 角色：笔记本 (可写层)
	2. 解释：这是真正存储数据的地方。修改的密码、安装的插件 (Docker)、配置的宽带账号，全部都保存在这里
	3. 现状：在截图中，它是 `/dev/loop0` (那个 234MB 的小空间)。等完成分区挂载磁盘的操作后，这里就会变成那个 28GB 的大分区
3. `/dev/mmcblk2p1` 挂载在 `/mnt/mmcblk2p1`
	1. 角色：启动引导分区
	2. 解释：这是 SD 卡/硬盘的第一个分区，通常存放着让路由器能够开机的引导文件 `Bootloader/Kernel`
	3. 特点：平时一般用不到，系统自动把它挂载起来而已，不需要去动它
4. `overlayfs:/tmp/root` 挂载在 `/`
	1. 角色：最终的合成视图
	2. 解释：这是系统呈现的最终样子。OpenWrt 使用一种叫 OverlayFS 的技术，把底下的 `/rom` (教科书) 和上面的 `/overlay` (笔记纸) 合并在一起，变成了根目录 `/`
	3. 逻辑：
		1. 如果读取一个文件，系统先看 `/overlay` (笔记) 里有没有；如果有，就读它的
		2. 如果没有，就去读 `/rom` (教科书) 里的
5. `tmpfs` 挂载在 `/tmp`
	1. 角色：内存盘 (临时草稿纸)
	2. 解释：`tmpfs` 不是硬盘，它是内存 (RAM)
	3. 特点：速度极快，但断电即失。系统用它来存放运行时的临时文件、缓存、或者解压的安装包
6. `cgroup` 挂载在 `/sys/fs/cgroup`
	1. cgroup 全称是 Control Groups（控制组）。它是 Linux 内核的一项高级功能，用来限制和隔离进程对系统资源的使用（比如 CPU、内存、磁盘 I/O）
	2. 它不是硬盘，它是内存里的虚拟文件系统
		1. 3.76 GB：这个数字是路由器物理内存（RAM）的总大小
		2. 这并不代表它占用了 3.76 GB 空间，而是表示它有权管理这 3.76 GB 的内存资源
7. 最后 28.39G 的空间并没有被使用，现在需要将他格式化并挂载到 `/overlay`，他才会被真正使用

![|700](attachments/Pasted%20image%2020251205085409.png)

![|700](attachments/Pasted%20image%2020251205085850.png)

## 2、备份数据

1. 将这 28.39G 的空间格式化并挂载到 `/overlay` 后，就会使用这个新的空间
2. 如果之前已经在 openwrt 系统上配置过，就需要备份数据，之后进行恢复，<font color="#c00000">否则之前的配置都会丢失</font>
3. 点击系统 -> 备份/升级 -> 生成备份，下载备份文件
4. 恢复时，点击恢复配置即可

![|700](attachments/Pasted%20image%2020251205090840.png)

## 3、创建分区并格式化

1. 点击系统 -> 磁盘管理，点击最大的分区 `/dev/mmcblk2` 后面的修改

![|700](attachments/Pasted%20image%2020251205091349.png)

2. 进入后，点击最大的分区 `mmcblk2p3` 后面的新建，在弹出的弹窗中选择分区类型 `ext4`，然后确认格式化

![|700](attachments/Pasted%20image%2020251205091557.png)

3. 成功后的样子：

![|700](attachments/Pasted%20image%2020251205092238.png)

4. 上面那两个小的 32 MB 的空闲空间它们是安全间距
	1. 在嵌入式设备（如路由器、树莓派）的分区表中，为了保证数据写入的对齐（4K对齐）以及给系统引导程序（Bootloader/U-Boot）留出位置，系统通常会自动保留一些微小的间隙
	2. 直接忽略忽略就好，它们就像是打印纸边缘的页边距。虽然也是纸（空间），你不能在上面写字
	3. 它们太小了，没有任何使用价值，千万不要去动它们，也不要尝试在上面新建分区，否则可能破坏系统的启动引导

## 4、挂载磁盘

1. 点击系统 -> 挂载点，向下翻找到挂载点，点击添加

![|700](attachments/Pasted%20image%2020251205092451.png)

2. 进入后：
	1. 启用此挂载点：✅ 勾选
	2. UUID：点击下拉菜单，选择新建的 `/dev/mmcblk2p3` 28 GB 的设备
	3. 挂载点（<font color="#c00000">最重要</font>）：作为外部 overlay 使用 (/overlay)

![|700](attachments/Pasted%20image%2020251205092857.png)

3. 设置完毕后，点击保存并应用，然后重启设备
4. 设备重启后会数据会重置，使用默认账号密码进行发登录，然后使用之前的备份进行恢复即可

# 三、安装使用 docker

## 1、安装 docker

1. 使用 ssh 连接 openwrt，输入以下命令，需保证可以连接外网

```shell
# 更新软件包列表
opkg update

# 安装 Docker 核心、Compose 和图形化管理界面
opkg install dockerd docker-compose luci-app-dockerman

# 设置开机自启
service dockerd enable
# 立即启动
service dockerd start
```

2. 验证是否安装成功，如果看到输出了 Client 和 Server 的版本信息（没有报错），那就是安装成功了

```shell
docker version
```

3. 返回 openwrt 网页端，会发现多了一个 Docker 的页面

![|700](attachments/Pasted%20image%2020251205093749.png)

## 2、修改路径，解决镜像无法下载

1. 默认情况下，拉取镜像可能提示：`code:200 failed to register layer: operation not supported`

![|700](attachments/Pasted%20image%2020251205104815.png)

2. 原因：现在的系统结构就像是千层饼：
	1. 第一层（系统层）：把 28GB 硬盘挂载为 `/overlay`，所以现在的系统根目录 `/` 本身就是一个 OverlayFS 文件系统
	2. 第二层（Docker层）：Docker 默认的存储驱动也是 Overlay2
	3. 冲突：Docker 试图在已经是由 OverlayFS 组成的系统上，再创建一个 OverlayFS 层。Linux 内核默认不支持这种 Overlay 套 Overlay 的操作，所以报错不支持
3. 解决：给 Docker 实地，告诉 Docker：不要把数据存那个虚拟的系统层里，而是直接存到那个 28GB 硬盘的实体目录里去
4. 进入 Dockers -> 配置，Docker Root Dir 的默认值应该是 `/opt/docker/`
	1. 将其修改为：`/overlay/docker/`
	2. 然后点击下方的保存并应用
	3. 最后重启 Docker 即可

![](attachments/Pasted%20image%2020251205104808.png)

## 3、


# 四、使用 openlist 挂载 openwrt 文件

## 1、确保 OpenWrt 支持 SFTP

1. 要使用 openlist 挂载 openwrt 文件，最简单、最稳定的方式是使用 SFTP 协议
2. 因为 OpenWrt 本身就已经开启了 SSH 服务（端口 22），只需要确保它支持 SFTP 文件传输即可
3. OpenWrt 默认的 SSH 服务（通常是 Dropbear）主要用于命令行，对 SFTP 文件传输的支持可能不完整。为了让 openlist 能顺利连接，建议安装一个 SFTP 服务端插件：

```shell
# 更新软件包列表
opkg update
# 安装 SFTP 服务端插件
opkg install openssh-sftp-server
```

4. 不用重启路由，安装完即生效。这个插件非常小，不占空间

## 2、在 openlist 中添加 openwrt 存储

1. 进入 openlist，点击存储 -> 添加，驱动选择 SFTP

![|443](attachments/Pasted%20image%2020251205100823.png)

2. 输入储存信息：
	1. 地址：openwrt 的地址和端口，一般是 `192.168.1.1:22`
	2. 用户名：登录账号
	3. 密码：登录密码
	4. 根文件夹路径：建议填 `/`，这样能管理整个系统

![|700](attachments/Pasted%20image%2020251205101047.png)

3. 点击保存，如果没有报错成功的话，就可以进入首页访问了

![|700](attachments/Pasted%20image%2020251205101331.png)


# 五、

# 六、

# 七、

# 八、

# 九、

# 十、问题记录

## 1、NAT 回环 失效

#### Ⅰ、报错现象

1. openwrt 的 ip 是 `192.168.1.1`，另一台在同噫局域网中的服务器 ip 是 `192.168.1.5`，现在：
2. 内网：可以通过内网 ip 访问服务器上的服务，但是通过 nginx 代理的服务通过域名无法访问
3. 外网：可以通过域名访问，但是连上家里的 wifi 之后，也无法通过域名访问

#### Ⅱ、原因

1. 外网访问时：数据包从外网 -> 路由器 WAN 口 -> 端口转发 -> 内网服务器 192.168.1.5。路径清晰，成功
2. 内网访问时：客户端在 `192.168.1.x` 呼叫域名（解析为路由器的公网 IP）。数据包发给路由器：“喂，我要访问你的公网 IP”。路由器发现请求来自内网，又指向自己，处理逻辑容易混乱，导致数据包被丢弃，失败
3. 首先进行 Ping 测试，假设域名为：`a.openwrt.com`
	1. 这里可以看到，电脑把域名解析到了公网 IP `234.159.158.94`，而不是预期的内网 IP `192.168.1.5`

```shell
Microsoft Windows [版本 10.0.19044.6575]
(c) Microsoft Corporation。保留所有权利。

C:\Users\yan>ping a.openwrt.com
正在 Ping a.openwrt.com [234.159.158.94] 具有 32 字节的数据:
来自 124.129.158.94 的回复: 字节=32 时间<1ms TTL=64
来自 124.129.158.94 的回复: 字节=32 时间<1ms TTL=64
来自 124.129.158.94 的回复: 字节=32 时间<1ms TTL=64
来自 124.129.158.94 的回复: 字节=32 时间<1ms TTL=64

234.159.158.94 的 Ping 统计信息:
    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 0ms，最长 = 0ms，平均 = 0ms
```

#### Ⅲ、解决

1. 使用 ssh 连接 openwrt，输入以下命令

```shell
# 添加泛域名解析规则 (uci 是 OpenWrt 的标准配置工具)
# 将泛域名 openwrt.com 指定解析到 192.168.1.5
uci add_list dhcp.@dnsmasq[0].address='/openwrt.com/192.168.1.5'
# 提交保存修改
uci commit dhcp
# 重启 DNS 服务让配置生效
service dnsmasq restart
```

2. 查看所有泛域名解析规则

```shell
uci show dhcp.@dnsmasq[0].address
```

3. 返回刚才行 Ping 测试的电脑，刷新 DNS 缓存：

```sdhell
ipconfig /flushdns
```

4. 重新进行 Ping 测试，发现电脑把域名解析到了预期的内网 IP `192.168.1.5`，配置成功

```shell
Microsoft Windows [版本 10.0.14393]
(c) 2016 Microsoft Corporation。保留所有权利。
C:\Users\yan>ping onenav.yuehai.fun

正在 Ping onenav.yuehai.fun [192.168.1.5] 具有 32 字节的数据:
来自 192.168.1.5 的回复: 字节=32 时间<1ms TTL=64
来自 192.168.1.5 的回复: 字节=32 时间<1ms TTL=64
来自 192.168.1.5 的回复: 字节=32 时间<1ms TTL=64
来自 192.168.1.5 的回复: 字节=32 时间<1ms TTL=64

192.168.1.5 的 Ping 统计信息:
    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 0ms，最长 = 0ms，平均 = 0ms

C:\Users\yan>
```

## 2、


# 三、

# 四、

# 五、
