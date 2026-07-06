# 一、openwrt

## 1、安装系统

### ①、下载系统

1. 下载地址：https://github.com/coolsnowwolf/lede/releases/tag/20230609

### ②、默认账号密码

1. 账号：`root
2. 密码：`password`

## 2、分区挂载磁盘

### ①、分区说明

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

### ②、备份数据

1. 将这 28.39G 的空间格式化并挂载到 `/overlay` 后，就会使用这个新的空间
2. 如果之前已经在 openwrt 系统上配置过，就需要备份数据，之后进行恢复，<font color="#c00000">否则之前的配置都会丢失</font>
3. 点击系统 -> 备份/升级 -> 生成备份，下载备份文件
4. 恢复时，点击恢复配置即可

![|700](attachments/Pasted%20image%2020251205090840.png)

### ③、创建分区并格式化

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

### ④、挂载磁盘

1. 点击系统 -> 挂载点，向下翻找到挂载点，点击添加

![|700](attachments/Pasted%20image%2020251205092451.png)

2. 进入后：
	1. 启用此挂载点：✅ 勾选
	2. UUID：点击下拉菜单，选择新建的 `/dev/mmcblk2p3` 28 GB 的设备
	3. 挂载点（<font color="#c00000">最重要</font>）：作为外部 overlay 使用 (/overlay)

![|700](attachments/Pasted%20image%2020251205092857.png)

3. 设置完毕后，点击保存并应用，然后重启设备
4. 设备重启后会数据会重置，使用默认账号密码进行发登录，然后使用之前的备份进行恢复即可

## 3、安装使用 docker

### ①、安装 docker

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


### ②、修改路径，解决镜像无法下载

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


### ③、


## 4、使用 openlist 挂载 openwrt 文件

### ①、确保 OpenWrt 支持 SFTP

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

### ②、在 openlist 中添加 openwrt 存储

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


## 5、NAT 回环 失效

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

# 二、ImmortalWrt

## 1、安装系统

### ①、下载系统

1. 下载地址：https://firmware-selector.immortalwrt.org/
2. 进入后输入 `r6s` 进行搜索
3. 展开自定义预安装软件包和/或首次启动脚本，然后在预安装的软件包中新起一行，输入以下内容：

```shell
bash curl wget-ssl ca-certificates unzip tar openssh-sftp-server
luci-app-diskman luci-i18n-diskman-zh-cn 
luci-i18n-firewall-zh-cn
docker docker-compose luci-app-dockerman luci-i18n-dockerman-zh-cn 
luci-app-homeproxy luci-i18n-homeproxy-zh-cn
```

4. 预安装的软件包说明：
	1. 命令行基础环境：
		1. `bash`：高级命令行解释器。OpenWrt 默认为了省空间用的是简陋的 `ash`，但很多高端的一键安装脚本必须用 bash 才能运行
		2. `curl`：网络请求神器。用于在没有浏览器的命令行里，向服务器发送请求或下载文件
		3. `wget-ssl`：带安全加密的网络下载工具。原版 `wget` 只能下载 `http://` 的文件，加上 `-ssl` 才能下载现在满大街都是的 `https://` 加密链接文件
		4. `ca-certificates`：根证书信任库。这就是软路由的身份证鉴别器，没有它，`curl` 和 `wget-ssl` 哪怕能上网，也会因为不认识网站的 HTTPS 安全证书而拒绝下载并报错
		5. `unzip`：用于解压 `.zip` 格式的压缩包
		6. `tar`：用于解压 `.tar.gz` 格式的 Linux 专属压缩包
		7. `openssh-sftp-server`：sftp 文件传输服务
	2. 磁盘与挂载管理：
		1. `luci-app-diskman`：精美的磁盘管理控制台
		2. `luci-i18n-diskman-zh-cn`：Diskman 的汉化包
	3. 三、 基础系统界面汉化
		1. `luci-i18n-firewall-zh-cn`：系统内置防火墙的中文包。由于系统本身已经内置了防火墙的核心底层，不需要再装 `luci-app-firewall`
	4. 容器生态管理：
		1. `docker`：Docker 的核心引擎
		2. `docker-compose`：容器编排工具
		3. `luci-app-dockerman`：OpenWrt 专属的 Docker 网页控制台
		4. `luci-i18n-dockerman-zh-cn`：Dockerman 控制台的汉化包
	6. 现代科学代理服务
		1. `luci-app-homeproxy`：基于最新的 `Sing-box` 核心开发的代理客户端图形界面。它比旧时代的 Passwall 和 OpenClash 架构更先进
		2. `luci-i18n-homeproxy-zh-cn`：HomeProxy 的汉化包
5. 输入后点击：请求构建
6. 构建完成后，点击最底部的：SYSUPGRADE (SQUASHFS) 下载即可

![|700](attachments/Pasted%20image%2020260624143445.png)

### ②、安装系统

> 1. 我是在已有的 openwrt 系统上安装的
> 2. 如果是原先没有安装系统，直接使用 Rufus 烧录即可

1. <font color="#ff0000">一定要提前备份数据</font>
2. 将系统上传到软路由指定的目录，比如 `/root`
3. 然后直接执行下面的进行安装：

```shell
# 进入系统安装文件所在的目录
cd /root

# 执行安装
sysupgrade -F -n /sysupgrade.img.gz
```

![](attachments/Pasted%20image%2020260624142312.png)

### ③、登录系统

1. 安装完成后，浏览器访问：http://192.168.1.1/cgi-bin/luci/
2. 初次访问需设定管理员账号密码

## 2、分区挂载磁盘

> 1. 格式化时 mmcblk1p3 下没有数据可以不用进行打包、docker 等操作
> 2. 这里是之前已经在 mmcblk1p3 下设置了 docker 目录、存放了数据的处理流程

1. 在 web 端删除挂载点 `/mnt/data`

![|700](attachments/Pasted%20image%2020260705165350.png)

2. 登录 ssh 终端，停止 Docker 服务：

```shell
service dockerd stop
```

3. 进入数据目录：

```shell
cd /mnt/data
```

4. 打包数据，带 `-p` 参数完美保留文件读写权限，这对数据库至关重要：
	1. 如果原先有数据的话则执行这一步
	2. 打包完毕后将生成的 `docker_backup.tar.gz` 下载到电脑

```shell
tar -czpvf docker_backup.tar.gz --exclude=docker_backup.tar.gz .
```

5. 彻底禁用 Docker 开机自启：

```shell
service dockerd disable || service docker disable
```

6. 重启路由器，刷新系统底层：

```shell
reboot
```

7. 路由器重启完毕后，重新连接 SSH，卸载目标分区：

```shell
umount /dev/mmcblk1p3
```

8. 强制格式化为 f2fs：
	1. 使用命令而不是 web 端的原因是 web 端显示不全，没有 f2fs 格式

```shell
mkfs.f2fs -f /dev/mmcblk1p3
```

9. 进入 web 端可以看到 mmcblk1p3 被格式化为了 f2fs

![|700](attachments/Pasted%20image%2020260705165322.png)

10. 然后进入系统 -> 挂载点 -> 添加，
	1. UUID：选择 mmcblk1p3
	2. 挂载点：输入 `/mnt/data`
	3. 点击保存

![|700](attachments/Pasted%20image%2020260705165435.png)

11. 进入  `/mnt` 目录，其中可能同时有 `data` 和 `mmcblk1p3` 两个目录，挂载  `/mnt/data` 完成后直接删除 `mmcblk1p3` 目录即可
12. 进入数据目录：

```shell
cd /mnt/data
```

13. 上传之前打包的 `docker_backup.tar.gz` 到 `/mnt/data` 目录下
14. 解压并恢复权限：

```shell
tar -xzpvf docker_backup.tar.gz
```

15. 清理压缩包释放空间：

```shell
rm docker_backup.tar.gz
```

16. 重新设置 docker 服务开机自启动：

```shell
service dockerd enable
```

17. 启动 docker 服务

```shell
service dockerd start
```

## 3、网络配置

### ①、接口配置

1. 进入网络 -> 接口，然后点击 wan 后面的编辑按钮

![|700](attachments/Pasted%20image%2020260626125229.png)

2. 常规设置中，协议勾选 `PPPoE`，PAP/CHAP 用户名、PAP/CHAP 密码 中输入宽带的账号、密码

![|700](attachments/Pasted%20image%2020260626125528.png)

3. 高级设置中，禁用 获取 IPV6 地址

![|700](attachments/Pasted%20image%2020260626125404.png)

![|700](attachments/Pasted%20image%2020260626125430.png)

4. 防火墙设置此处不用修改，一会在防火墙中配置

![|700](attachments/Pasted%20image%2020260626125439.png)

5. DHCP 服务器不用修改

![|700](attachments/Pasted%20image%2020260626125446.png)

### ②、防火墙配置

#### Ⅰ、端口转发

1. 进入网络 -> 防火墙 -> 端口转发，点击添加按钮
2. 常规设置根据端口用途自定义，保证：
	1. 源区域：`wan`
	2. 外部端口：外网访问的端口
	3. 目标区域：`lan`
	4. 内部 IP 地址：转发到的内网设备的 IP
	5. 内部端口：转发到的内网设备的端口

![|700](attachments/Pasted%20image%2020260629130308.png)

3. 高级设置中，大部分不用改，保证：
	1. 启用 NAT 环回：勾选
	2. 环回源 IP：使用内部 IP 地址

![|700](attachments/Pasted%20image%2020260629130339.png)

4. 点击 保存，然后点击 保存并应用

#### Ⅱ、通信规则

1. 进入网络 -> 防火墙 -> 通信规则，点击添加按钮
2. 常规设置中：
	1. 名称：随意
	2. 协议：根据端口用途选择
	3. 源区域：`wan`
	4. 源地址：留空；发起请求的客户端 IP，若是填入表示仅限使用填入 IP 的设备访问
	5. 源端口：留空；发起请求的客户端端口，若是填入表示仅限使用填入端口的设备访问
	6. 目标区域：`lan`
	7. 内部 IP 地址：转发到的内网设备的 IP
	8. 内部端口：转发到的内网设备的端口
	9. 操作：接受

![|700](attachments/Pasted%20image%2020260629132955.png)

3. 高级设置不用修改

![|700](attachments/Pasted%20image%2020260629133004.png)

4. 时间限制不用修改

![|700](attachments/Pasted%20image%2020260629133010.png)

5. 端口转发、通信规则设置完毕后，就可以外网访问了


### ③、

### ④、

## 4、docker 配置

### ①、安装 docker

1. 构建系统时已经将 docker 相关的包安装了：

```shell
docker docker-compose luci-app-dockerman luci-i18n-dockerman-zh-cn 
```

2. 如果当时没有安装，可以使用 `apk` 命令安装：

```shell
apk add docker docker-compose luci-app-dockerman luci-i18n-dockerman-zh-cn
```

### ②、配置 docker 目录

1. 先停止当前 Docker 服务：

```shell
service dockerd stop
```

2. 创建 docker 核心目录：

```shell
mkdir -p /mnt/data/docker/root
mkdir -p /mnt/data/docker/volumes
```

3. 将 Docker 的数据根目录重新定向：

```shell
uci set dockerd.globals.data_root='/mnt/data/docker/root'
uci commit dockerd
```

4. 启动 Docker 服务：

```shell
service dockerd start
```

5. 验证引擎路径是否正确：

```shell
docker info | grep "Root Dir"
```

6. 如果输出显示 `Docker Root Dir: /mnt/data/docker/root`，说明配置 docker 目录成功

### ③、添加 docker 防火墙

> 不添加会导致 docker 容器无法连接外部网络

1. 进入 网络 -> 防火墙 -> 常规设置，在最下面区域中点击添加

![|700](attachments/Pasted%20image%2020260626165853.png)

2. 常规设置中：
	1. 名称：`docker`
	2. 输入：接受
	3. 出站数据：接受
	4. 区域内转发：接受
	5. IP 动态伪装：勾选
	6. TCP MSS 钳制：勾选
	7. 涵盖的网络：先不选择
	8. 允许转发到目标区域：选择 `lan`、`wan`
	9. 允许来自源区域的转发：选择 `lan`、`wan`

![|700](attachments/Pasted%20image%2020260626165903.png)

3. 高级设置中，IPV6 伪装不勾选

![|700](attachments/Pasted%20image%2020260626165911.png)

4. 连接跟踪设置不用修改

![|700](attachments/Pasted%20image%2020260626165920.png)

5. 点击 保存，然后点击 保存并应用

### ④、添加 docker 接口

> 此步骤需要在上面：添加 docker 防火墙 完成后

1. 创建 docker 网络，然后查看所有网络：

```shell
# 创建指定网络
docker network create yuehai-net

# 查看所有网络
docker network ls
```

2. 记录下结果中创建的网络 ID：`fa7595556700`

```shell
root@ImmortalWrt:~# docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
edc4486cac29   bridge       bridge    local
115ebe22f587   host         host      local
821a51b86f68   none         null      local
fa7595556700   yuehai-net   bridge    local
```

3. 获取准确的网桥名称：

```shell
ip -o link show | awk -F': ' '{print $2}' | grep br-
```

4. 记录下结果中和上面 `fa7595556700` 一样的值：`br-fa7595556700`

```shell
root@ImmortalWrt:~# ip -o link show | awk -F': ' '{print $2}' | grep br-
br-lan
br-fa7595556700
root@ImmortalWrt:~# 
```

5. 登录 ssh，查看防火墙配置：

```shell
cat /etc/config/firewall | grep -A 5 "config zone"
```

6. 可以看到防火墙 `docker` 区域的配置没有绑定设备：

```shell
root@ImmortalWrt:~# cat /etc/config/firewall | grep -A 5 "config zone"
config zone
        option name 'lan'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'ACCEPT'
        list network 'lan'
--
config zone
        option name 'wan'
        option input 'REJECT'
        option output 'ACCEPT'
        option forward 'DROP'
        option masq '1'
--
config zone
        option name 'docker'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'ACCEPT'
        option masq '1'
root@ImmortalWrt:~# 
```

7. 执行以下命令，将 `docker0` 绑定到防火墙 `docker` 区域：

```shell
# 向名为 docker 的 firewall zone 附加默认网桥设备 docker0
uci add_list firewall.@zone[-1].device='docker0'
# 向名为 docker 的 firewall zone 附加你的自定义网络网桥 br-fa7595556700
uci add_list firewall.@zone[-1].device='br-fa7595556700'

# 保存更改
uci commit firewall

# 重启防火墙服务以重载规则
service firewall restart
```

8. 再次查看防火墙配置，区域 `docker` 中出现了 `list network 'docker'`：

```shell
root@ImmortalWrt:~# cat /etc/config/firewall | grep -A 5 "config zone"
config zone
        option name 'lan'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'ACCEPT'
        list network 'lan'
--
config zone
        option name 'wan'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'ACCEPT'
        option masq '1'
--
config zone 'docker'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'ACCEPT'
        option name 'docker'
        list network 'docker'
root@ImmortalWrt:~# 
```

9. 进入 网络 -> 接口 -> 接口，会发现多出来了一个 `docker` 接口

![|700](attachments/Pasted%20image%2020260629125044.png)

10. 点击 `docker` 接口的编辑按钮，在常规设置中，设备是：`docker0`，即为成功

![|700](attachments/Pasted%20image%2020260629125100.png)

11. 此时 docker 容器就可以连接外部网络了


### ⑤、DNS 地址重定向

1. 进入网络 -> DNS -> 常规
2. DNS 重定向：勾选
3. 扩展 HOSTS 文件：勾选
4. 地址：`/yuehai.fun/192.168.1.1`，表示告诉路由器，只要查询任何 `*.yuehai.fun` 的域名，全部解析为 `192.168.1.1`
5. 然后点击 保存并应用 即可，这样内网就可以使用域名访问内网服务了

![|700](attachments/Pasted%20image%2020260629133604.png)

### ⑥、

## 5、HomeProxy 配置

### ①、安装 HomeProxy

1. 构建系统时已经将 HomeProxy 相关的包安装了：

```shell
luci-app-homeproxy luci-i18n-homeproxy-zh-cn
```

2. 如果当时没有安装，可以使用 `apk` 命令安装：

```shell
apk add luci-app-homeproxy luci-i18n-homeproxy-zh-cn
```

### ②、订阅配置

1. 进入机场网站，点击：复制 SS 订阅链接

![|700](attachments/Pasted%20image%2020260626151717.png)

2. 在 ImmortalWrt 中，选择 服务 -> HomeProxy -> 节点设置 -> 订阅，将复制的 SS 订阅链接 填入订阅地址中，然后点击：保存当前设置

![|700](attachments/Pasted%20image%2020260626152244.png)

3. 保存后，节点设置中应该会多出来一个新的标签页，点击进入后会显示订阅的节点

![|700](attachments/Pasted%20image%2020260626153222.png)

### ③、启动代理

1. 订阅配置完成后，点击 客户端设置 -> 路由设置
2. 主节点选择：`URLTest`，他会自动检测节点延迟，然后选择一个延迟最低的节点使用
3. URLTest 节点：选择一些想要自动检测、自动切换的节点

![|700](attachments/Pasted%20image%2020260626154507.png)

4. 测试间隔、测试容差 默认即可
5. DNS 服务器：访问国外节点的 DNS 服务器
6. 国内 DNS 服务器：访问国内节点的 DNS 服务器
7. 路由模式：大陆白名单，表示访问国内网站时不进行代理
8. IPv6 支持：取消勾选

![|700](attachments/Pasted%20image%2020260626154532.png)

9. 配置完成后点击保存并应用

### ④、直连域名列表

1. 点击 客户端设置 -> 路由设置 -> 访问控制 -> 直连域名列表

```shell
api.deepseek.com

digicert.com
plex.tv
playartifact.com
s.team
steam-chat.com
steamcontent.com
steamgames.com
steampowered.com
steamstatic.com
steamusercontent.com
steamcommunity.com
underlords.com
valvesoftware.com
csgo.wmsj.cn
dota2.wmsj.cn
wmsjsteam.com
dl.steam.clngaa.com
dl.steam.ksyna.com
st.dl.bscstorage.net
st.dl.eccdnx.com
st.dl.pinyuncloud.com
steampipe.steamcontent.tnkjmec.com
steampowered.com.8686c.com
steamstatic.com.8686c.com
steambroadcast.akamaized.net
steamcdn-a.akamaihd.net
steamcommunity-a.akamaihd.net
steamstore-a.akamaihd.net
steamusercontent-a.akamaihd.net
steamuserimages-a.akamaihd.net
steamvideo-a.akamaihd.net
steamchina.com
apple.cn
apple.com.cn
apple-store.cn
applestore.cn
applestore.com.cn
apple-appstore.cn
appleappstore.cn
appstoreapple.cn
iphone-8.com.cn
ipod.com.cn
macbookair.cn
macbookair.com.cn
applepaycash.cn
applepaycash.com.cn
applepaysupplies.cn
applepaysupplies.com.cn
appletv4.cn
appletv4.com.cn
apple-dns.cn
apple-dns.com.cn
apple-ibooks.cn
apple-maps.cn
applecenter.cn
applecenter.com.cn
applecomputer.cn
applecomputer.com.cn
appledns.cn
appledns.com.cn
applesiri.cn
ecgapp.com.cn
faceshift.cn
homepod.cn
insidear.cn
livephotos.cn
livephotos.com.cn
xn--ohq11k7pl25iyo8a.cn
amp-api-search-edge.apps.apple.com
amp-api.apps.apple.com
aod.itunes.apple.com
api-edge.apps.apple.com
apptrailers.itunes.apple.com
bag.itunes.apple.com
bookkeeper.itunes.apple.com
client-api.itunes.apple.com
cma.itunes.apple.com
communities.apple.com
discussionschinese.apple.com
downloaddispatch.itunes.apple.com
fides-pol.apple.com
gspe11-2-cn-ssl.ls.apple.com
gspe12-cn-ssl.ls.apple.com
gspe85-cn-ssl.ls.apple.com
init.itunes.apple.com
iosapps.itunes.apple.com
js-cdn.music.apple.com
km.support.apple.com
maps.apple.com
osxapps.itunes.apple.com
pd.itunes.apple.com
play.itunes.apple.com
se-edge.itunes.apple.com
se2.itunes.apple.com
search.itunes.apple.com
sf-api-token-service.itunes.apple.com
sp.itunes.apple.com
stocks-sparkline.apple.com
streamingaudio.itunes.apple.com
su.itunes.apple.com
sync.itunes.apple.com
upp.itunes.apple.com
weather-data.apple.com
a1.mzstatic.com
a2.mzstatic.com
a3.mzstatic.com
a4.mzstatic.com
a5.mzstatic.com
adcdownload.apple.com.akadns.net
adcdownload.apple.com
appldnld.apple.com
appldnld.g.aaplimg.com
apps.mzstatic.com
cdn-cn1.apple-mapkit.com
cdn-cn2.apple-mapkit.com
cdn-cn3.apple-mapkit.com
cdn-cn4.apple-mapkit.com
cdn.apple-mapkit.com
cdn1.apple-mapkit.com
cdn2.apple-mapkit.com
cdn3.apple-mapkit.com
cdn4.apple-mapkit.com
cds-cdn.v.aaplimg.com
cds.apple.com.akadns.net
cds.apple.com
cl1-cdn.origin-apple.com.akadns.net
cl1.apple.com
cl2-cn.apple.com
cl2.apple.com.edgekey.net.globalredir.akadns.net
cl2.apple.com
cl3-cdn.origin-apple.com.akadns.net
cl3.apple.com
cl4-cdn.origin-apple.com.akadns.net
cl4-cn.apple.com
cl4.apple.com
cl5-cdn.origin-apple.com.akadns.net
cl5.apple.com
clientflow.apple.com.akadns.net
clientflow.apple.com
configuration.apple.com.akadns.net
configuration.apple.com
cstat.apple.com
dd-cdn.origin-apple.com.akadns.net
download.developer.apple.com
gs-loc-cn.apple.com
gs-loc.apple.com
gsp10-ssl-cn.ls.apple.com
gsp11-cn.ls.apple.com
gsp12-cn.ls.apple.com
gsp13-cn.ls.apple.com
gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net
gsp4-cn.ls.apple.com.edgekey.net
gsp4-cn.ls.apple.com
gsp5-cn.ls.apple.com
gsp85-cn-ssl.ls.apple.com
gspe19-cn-ssl.ls.apple.com
gspe19-cn.ls-apple.com.akadns.net
gspe19-cn.ls.apple.com
gspe21-ssl.ls.apple.com
gspe21.ls.apple.com
gspe35-ssl.ls.apple.com
iadsdk.apple.com
icloud-cdn.icloud.com.akadns.net
icloud.cdn-apple.com
images.apple.com.akadns.net
images.apple.com.edgekey.net.globalredir.akadns.net
images.apple.com
init-p01md-lb.push-apple.com.akadns.net
init-p01md.apple.com
init-p01st-lb.push-apple.com.akadns.net
init-p01st.push.apple.com
init-s01st-lb.push-apple.com.akadns.net
init-s01st.push.apple.com
iosapps.itunes.g.aaplimg.com
iphone-ld.apple.com
is1-ssl.mzstatic.com
is1.mzstatic.com
is2-ssl.mzstatic.com
is2.mzstatic.com
is3-ssl.mzstatic.com
is3.mzstatic.com
is4-ssl.mzstatic.com
is4.mzstatic.com
is5-ssl.mzstatic.com
is5.mzstatic.com
itunes-apple.com.akadns.net
itunes.apple.com
itunesconnect.apple.com
mesu-cdn.apple.com.akadns.net
mesu-china.apple.com.akadns.net
mesu.apple.com
music.apple.com
ocsp-lb.apple.com.akadns.net
ocsp.apple.com
oscdn.apple.com
oscdn.origin-apple.com.akadns.net
pancake.apple.com
pancake.cdn-apple.com.akadns.net
phobos.apple.com
prod-support.apple-support.akadns.net
reserve-prime.apple.com
s.mzstatic.com
stocks-sparkline-lb.apple.com.akadns.net
store.apple.com.edgekey.net.globalredir.akadns.net
store.apple.com.edgekey.net
store.apple.com
store.storeimages.apple.com.akadns.net
store.storeimages.cdn-apple.com
support-china.apple-support.akadns.net
support.apple.com
swcatalog-cdn.apple.com.akadns.net
swcatalog.apple.com
swcdn.apple.com
swcdn.g.aaplimg.com
swdist.apple.com.akadns.net
swdist.apple.com
swscan-cdn.apple.com.akadns.net
swscan.apple.com
updates-http.cdn-apple.com.akadns.net
updates-http.cdn-apple.com
valid.apple.com
valid.origin-apple.com.akadns.net
www.apple.com.edgekey.net.globalredir.akadns.net
www.apple.com.edgekey.net
www.apple.com
bing.com.cn
cn.bing.com
cn.bing.net
ditu.live.com
bj1.api.bing.com
emoi-cncdn.bing.com
bitpt.cn
byr.pt
ccfbits.org
et8.org
hdchina.org
hdhome.org
hdsky.me
hudbt.hust.edu.cn
lemonhd.org
m-team.cc
nanyangpt.com
npupt.com
open.cd
ourbits.club
pterclub.com
ptsbao.club
pt.eastgame.org
pt.hd4fans.org
pt.keepfrds.com
pt.nwsuaf6.edu.cn
pt.xauat.edu.cn
springsunday.net
tjupt.org
totheglory.im
www.pthome.net
dbank.com
dbankcdn.com
harmonyos.com
hicloud.com
hihonor.com
honor.cn
huawei.com
huaweicloud.com
vmall.com
vmallres.com
alibabacloud.co.in
alibabacloud.com
alibabacloud.com.au
alibabacloud.com.hk
alibabacloud.com.my
alibabacloud.com.sg
alibabacloud.com.tw
alicloud.com
blizzard.cn
blizzardgames.cn
blzstatic.cn
battlenet.com.cn
bnet.163.com
di.res.netease.com
diablo3.nosdn.127.net
hearthstone.nosdn.127.net
hearthstone.nosdn.127.net
heroes.nos.netease.com
overwatch.nosdn.127.net
sc2.nosdn.127.net
wowchina.com
wow.nosdn.127.net
blz.nosdn.127.net
cn.actual.battle.net
gog.qtlglb.com
gogalaxy.gog-statics.com
menu-static.gog-statics.com
productcard.gog-statics.com
static-login.gog-statics.com
www4-static.gog-statics.com
legendofzelda.cn
legendofzelda.com.cn
miitomo.com.cn
nintendolabo.cn
supersmashbros.cn
supersmashbros.com.cn
xn--mts47c3w9b1qr.cn
mariokart.cn
mariokart.com.cn
supermariobros.com.cn
leagueoflegends.cn
lpl.com.cn
csgo.wmsj.cn
dota2.wmsj.cn
wmsjsteam.com
dl.steam.clngaa.com
dl.steam.ksyna.com
st.dl.bscstorage.net
st.dl.eccdnx.com
st.dl.pinyuncloud.com
steampipe.steamcontent.tnkjmec.com
steampowered.com.8686c.com
steamstatic.com.8686c.com
steamchina.com
uplaypc-s-ubisoft.cdn.ubi.com
xboxlive.cn
researchkit.cn
researchkit.com.cn
beats1.cn
beats1.com.cn
beats2.com.cn
beats4.cn
beatsep.cn
apple-icloud.cn
appleicloud.cn
icloud-apple.cn
icloud.com.cn
icloud.net.cn
icloudapple.cn
apple-itunes.cn
itunes-apple.cn
itunesapple.cn
itunesradio.cn
itunesradio.com.cn
swiftui.cn
swiftui.com.cn
cdnst.net
cellmaps.com
ekahau.cloud
ekahau.com
ookla.com
ooklaserver.net
pingtest.net
speedtest.co
speedtest.net
speedtestcustom.com
webtest.net
swiftui.cn
swiftui.com.cn
```

### ⑤、

### ⑥、

## 6、

## 7、

## 8、

# 三、

# 四、

# 五、

# 六、

# 七、

# 八、

# 九、

# 十、

