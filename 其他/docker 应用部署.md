# nginx-proxy-manager 基于 Nginx 的反向代理管理工具

## 1、介绍

1. Nginx Proxy Manager（NPM）是一个基于 Nginx 的反向代理管理工具，旨在简化 Nginx 的配置和管理。 它提供了直观的 Web 界面，使用户无需深入了解 Nginx，即可轻松设置和管理反向代理、SSL 证书、访问控制等功能。
2. 主要特性：
3. 美观安全的管理界面： 基于 Tabler 构建，界面简洁直观，用户体验良好
4. 简化的反向代理设置： 用户无需掌握 Nginx 配置，即可轻松创建转发域、重定向、流和 404 主机
5. SSL 证书管理： 支持 Let's Encrypt 的免费 SSL 证书，或用户自定义的 SSL 证书，方便地为网站启用 HTTPS
6. 访问控制： 提供主机的访问列表和基本 HTTP 身份验证，增强安全性
7. 高级 Nginx 配置： 超级用户可进行高级 Nginx 配置，满足特定需求
8. 用户管理与权限控制： 支持用户管理、权限分配和审核日志，便于团队协作

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 文件目录：`/home/docker/docker/volumes/nginx-proxy-manager/data`
2. 原镜像是：`jc21/nginx-proxy-manager`，此处使用的是汉化版
3. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射；因为家庭宽带的 80、443 端口一般都是被封的，所以这里一般修改为其他端口
		1. `8081`：nginx-proxy-manager 的 web 访问端口
		2. `8080`：http 代理端口，访问代理的 http 地址时，需要加上这个端口
		3. `8553`：https 代理端口，访问代理的 https 地址时，需要加上这个端口
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8081:81 \
-p 8080:80 \
-p 8443:443 \
-v /home/docker/docker/volumes/nginx-proxy-manager/data:/data \
-v /ssl/:/etc/letsencrypt \
--name=nginx-proxy-manager-zh \
chishin/nginx-proxy-manager-zh:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:8081](http://127.0.0.1:8081)
2. 初次访问需设定管理员账号密码

## 4、申请 ssl 证书

> 这里只演示阿里云，因为我只在阿里云有域名

### ①、获取阿里云 AccessKey

> 此处获取 AccessKey 的方式与 ddns-go 中基本相同，只是要多设置一些权限

1. 申请并配置阿里云 DNS 访问密钥：会进入 [RAM 访问控制](https://ram.console.aliyun.com/profile/access-keys) 页面；点击左侧的授权，然后点击新增授权

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108083754.png)

2. 在右侧弹窗中：
	1. 授权主体勾选 **RAM 用户**类型的角色
	2. 权限策略中搜索 `AliyunDNSFullAccess`，然后勾选（我这里已经有了所以不能勾选）
	3. 点击确认新增授权

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108083825.png)

3. 权限设置完成后，进入 [RAM 访问控制](https://ram.console.aliyun.com/profile/access-keys) 页面：
	1. 若是其他应用（比如 ddns-go）使用时已经创建过了，直接使用之前创建的 AccessKey ID 和 AccessKey Secret 即可
	2. 若是没有，继续下面的步骤进行创建：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108083857.png)

4. 勾选**我确认知晓云账号 AccessKey 安全风险**，然后点击**继续使用云账号AccessKey**

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108083922.png)

5. 选择**创建AccessKey**，同样确认风险

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108083957.png)

6. 验证身份后，记得保存 AccessKey ID 和 AccessKey Secret，否则一旦关闭页面，只能重新创建

### ②、申请 ssl 证书

1. 进入 nginx-proxy-manager 页面后，点击 **SSL 证书**，然后点击**添加 SSL 证书**，再选择 **Let's Encrypt**

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084028.png)

2. 在添加 Let's Encrypt 证书弹窗中：
	1. 域名可以设置泛域名，如：`*.yuehai.fun`
	2. Let's Encrypt 处填写自己的邮箱
	3. 使用 DNS 认证：勾选，一般家用宽带的 80 和 443 端口都是被封禁的，所以只能使用 DNS 认证
	4. DNS 提供者：选择自己的域名提供商、DNS 解析商，我的是阿里云，所以这里选择阿里云
	5. 证书内容：填入上一节创建的 AccessKey ID 和 AccessKey Secret
	6. 等待时间(秒)：120 ~ 240 即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084109.png)

3. 点击保存，等待几分钟即可

## 5、设置代理服务

1. 如果需要代理的服务和 nginx 都在同一台服务上，且需要代理的服务是使用 docker 部署的，则使用以下命令获取 docker 中指向宿主机的 ip：

```shell
ip addr show docker0
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084146.png)

2. 点击主机 -> 代理服务 -> 添加代理服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084201.png)

3. 比如我给部署的迅雷设置一个代理：
	1. 域名：外部访问时的域名；因为是泛解析的域名，所以三级域名可以随便设置，指向迅雷即可
	2. 协议：选择部署的迅雷原本的协议，即 http
	3. 转发主机/IP：上面获取的 `172.17.0.1`
	4. 转发端口：部署的迅雷的端口，迅雷默认是 `2345`
	5. 缓存资源、阻止常见漏洞、支持 WebSockets 一般都开启即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084347.png)

4. 点击 SSL，选择上面申请的证书

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084403.png)

5. 强制SSL、支持HTTP/2、启用了HSTS、HSTS 子域一般都开启即可
6. 点击保存，即可；因为端口号我们修改过，所以要加上 8080 或者 8443 的端口号：
7. 访问 http：`xunlei.yuehai.fun:8080`
8. 访问 https：`xunlei.yuehai.fun:8443`

## 6、设置内网端口可访问

1. 如果设置完上面的代理服务，但是通过 `xunlei.yuehai.fun` 不可以访问，可能是 nginx 无法访问 `172.17.0.1` 网段的端口
2. 查看已经开启的端口：

```shell
sudo ufw status numbered
```

3. 开启 `192.0.0.0/8` 和 `172.0.0.0/8` 的内网端口：

```shell
# 开放内网端口：
sudo ufw allow from 192.168.1.0/8

# 开放 docker 端口：
sudo ufw allow from 172.0.0.0/8
```

4. 再次查看已经开启的端口：

```shell
[1] Anywhere                   ALLOW IN    192.0.0.0/8               
[2] Anywhere                   ALLOW IN    172.0.0.0/8  
```

5. 开启完毕后，可再次尝试访问 `xunlei.yuehai.fun` 

## 7、代理权限设置

1. 点击通信规则 -> 添加通信规则

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084713.png)

2. 详情页面：
	1. 名字：这个通信规则的名字，仅作为标识符使用
	2. 满足任何要求：规则页面中满足任意即可访问
	3. 授权访问主机：暂不知作用

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084741.png)

3. 授权用户页面：
	1. 账号：启用时需要输入的账号
	2. 密码：启用时需要输入的密码
	3. 可以设置多个，有一个输入正确了即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084759.png)

4. 规则页面：
	1. allow：**允许**；设置为 `all` 表示允许所有 ip，单独设置则为白名单
	2. deny：**禁止**； 设置为 `all` 表示禁止所有 ip，单独设置则为黑名单
	3. 可以设置多个，规则将按照它们定义的顺序执行

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084825.png)

5. 设置完成后，点击保存即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084841.png)

6. 进入代理服务页面，选择一个代理设置

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084855.png)

7. 点击编辑，通信规则选择刚刚设置的规则名称，然后点击保存即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084915.png)

8. 访问上面设置了通信规则的代理服务地址，浏览器上方会弹出账号密码输入框，输入上面在授权用户页面设置的账号密码即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108084933.png)

# 零、docker 可视化 portainer-ce

## 1、介绍

1. Portainer 是一款轻量级的应用，它提供了图形化界面，用于方便地管理 Docker 环境，包括单机环境和集群环境
2. 这里使用的是国内热心大佬上传到 Docker Hub 的二次编译汉化版 Portainer，安装好之后直接使用
3. 弊端就是跟不上原版 Portainer 的更新节奏。虽说如此，它一般和最新版 Portainer 差距不大，所以使用起来几乎没什么差别。

## 2、docker 部署

1. 镜像名：`6053537/portainer-ce`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108090528.png)

2. 安装：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 9000:9000 \
-v /var/run/docker.sock:/var/run/docker.sock \
--restart=unless-stopped \
--name="portainer-ce" \
6053537/portainer-ce
```

## 3、访问及设置

1. 访问：[http://127.0.0.1:9000](http://127.0.0.1:9000)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108090730.png)

2. 第一次进入需设置密码
3. 界面：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108090706.png)

# 一、迅雷群晖提取版

> github 项目地址：https://github.com/cnk3x/xunlei
> 
> dockerHub 地址：https://hub.docker.com/r/cnk3x/xunlei

## 1、介绍

1. 该项目提取自群晖平台的迅雷下载套件，用于其他 Linux 机器上的迅雷远程下载服务
2. 需要已经安装完毕 docker，如果没有，请先进行 docker 的安装

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/xunlei/data/`
	2. 下载文件保存目录：`/home/docker/docker/volumes/xunlei/downloads/`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射；如果想要指定迅雷的端口号，可配置环境变量 `XL_DASHBOARD_PORT`
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 2345:2345 \
-v /home/docker/docker/volumes/xunlei/data:/xunlei/data \
-v /home/docker/docker/volumes/xunlei/downloads:/xunlei/downloads \
--privileged=true \
--restart=unless-stopped \
--name=xunlei \
cnk3x/xunlei:latest
```

## 3、访问

1. 访问迅雷迅雷群晖提取版网页： [http://127.0.0.1:2345](http://127.0.0.1:2345)
2. 扫码或使用账号密码登录

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108091117.png)

3. 输入内测邀请码（经过测试 <font color="#ff0000">迅雷牛通</font> 内测码有效）

![|425](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108091129.png)

10. 登录完成后，点击新建任务，就可以添加连接进行下载

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108091142.png)

# 二、AList 网盘整合挂载工具

> 1. AList 官网：https://alist.nn.ci/zh/guide/install/desktop.html
> 2. AList-desktop gui 桌面版官网：https://ad.nn.ci/zh
> 3. github：https://github.com/AlistGo/alist
> 4. 操作系统版本为：Ubuntu 22.04.3 LTS

## 1、AList docker 版安装

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/alist`
	2. 宿主机硬盘数据目录：`/media/yan`
	3. alist 挂载到的目录：`/mnt/alist`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 5244:5244  \
-e PUID=0  \
-e PGID=0  \
-e UMASK=022  \
-v /home/docker/docker/volumes/alist:/opt/alist/data \
-v /media/yan:/media/yan \
-v /mnt/alist:/mnt/alist \
--privileged=true \
--restart=unless-stopped  \
--name="alist"  \
xhofe/alist:latest
```

3. 部署成功后，随机生成一个密码：

```shell
docker exec -it alist ./alist admin random
```

4. 手动设置一个密码，`NEW_PASSWORD` 是指需要设置的密码：

```shell
docker exec -it alist ./alist admin set NEW_PASSWORD
```

5. 访问：`http://127.0.0.1:5244`，进入主页面；输入账号 `admin` 以及刚才设置的密码进行登录
6. 点击管理可进行网盘的设置等，具体查看文档

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108091446.png)

## 2、AList-desktop ubuntu gui 桌面版的安装

> 1. 一开始我以为桌面版有单独的控制面板，单独的挂载、管理方式，结果只是一个启动按钮
> 2. 不如直接安装 docker 版

1. 桌面版需要购买，50元，请在 AList-desktop gui 桌面版官网选择购买
2. 在官网下载对应的 linux 版本到目录，比如我放在了：`/home/yan/apply/file/alist-desktop/` 目录下，或点击此处下载：[alist-desktop_3.38.0_amd64.deb](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Falist-desktop_3.38.0_amd64.deb)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108091543.png)

3. 更新软件源：

```shell
sudo apt update
```

4. 进入软件包所在目录：

```shell
cd /home/yan/apply/file/alist-desktop/
```

5. 使用 dpkg 安装:

```shell
sudo dpkg -i alist-desktop_3.38.0_amd64.deb
```

6. 处理依赖项：

```shell
sudo apt --fix-broken install
```

7. 此时桌面应该会出现 alist-desktop 的图标，点击即可进入
8. 启动成功后，访问：`http://127.0.0.1:port`，进入主页面

## 3、alist-desktop gui 桌面版安装后，点击桌面图标没反应

### ①、问题排查

1. 处理依赖项：

```shell
sudo apt --fix-broken install
```

2. 检查桌面文件配置，一般路径为 `/usr/share/applications/alist-desktop.desktop` 或 `~/.local/share/applications/alist-desktop.desktop`：

```shell
cat /usr/share/applications/alist-desktop.desktop
```

3. 内容一般为下面的这样，检查 `Exec=` 行是否正确指向 `alist-desktop` 的安装路径：

```shell
[Desktop Entry]
Categories=
Comment=A Tauri App
Exec=alist-desktop
Icon=alist-desktop
Name=alist-desktop
Terminal=false
Type=Application
```

4. 运行 `Exec=` 行指向的程序，查看其报错：

```shell
yan@yan:~$ alist-desktop
alist-desktop: error while loading shared libraries: libssl.so.1.1: cannot open shared object file: No such file or directory
```

5. 看报错是缺少 `libssl.so.1.1` 库，该库是 OpenSSL 1.1 的一部分，但在较新的 Ubuntu 版本中可能已经不再默认安装，若是已经安装了更高版本的 OpenSSL，也会导致这个问题，比如我安装的是 OpenSSL 3.0.2

```shell
root@yan:~# openssl version
OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)
```

6. 接下来进行安装，下面的两种方法使用其中的一种即可

### ②、仅引用  `libssl.so.1.1` 库

> 1. [libssl.so.1.1](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Flibssl.so.1.1)
> 2. [libcrypto.so.1.1](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Flibcrypto.so.1.1)

1. 下载上方的 libssl.so.1.1 和 libcrypto.so.1.1，上传到目录，比如我放在了：`/home/yan/apply/file/alist-desktop/` 目录下
2. 创建符号链接；前面的路径是文件所在的路径，后面的路径是要连接到的路径

```shell
sudo ln -s /home/yan/apply/file/alist-desktop/libssl.so.1.1 /usr/lib/x86_64-linux-gnu/libssl.so.1.1
sudo ln -s /home/yan/apply/file/alist-desktop/libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
```

3. 重新尝试运行 `alist-desktop`：

```shell
alist-desktop
```

4. 成功启动

### ③、安装  `libssl.so.1.1` 库

> [openssl-1.1.1g.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Fopenssl-1.1.1g.tar.gz)

1. 进入目录：

```shell
cd /home/yan/apply/file/alist-desktop/
```

2. 直接下载上面的 `openssl-1.1.1g.tar.gz` 到此目录中，或者在官网进行下载：

```shell
wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz
```

3. 解压：

```shell
tar -xvf openssl-1.1.1g.tar.gz
```

4. 进入解压后的目录：

```shell
cd openssl-1.1.1g
```

5. 创建要将 openssl 安装到的目录：

```shell
sudo mkdir -p /usr/local/openssl
```

6. 设置编译选项：
	1. `./config`：在当前目录下执行 config 配置脚本。通常在编译 OpenSSL 时，先运行 config 来生成 Makefile，以便后续的编译步骤。
	2. `shared`：指定生成共享库（即动态链接库）。默认情况下，OpenSSL 会生成静态库和一些可执行文件，但如果指定 shared，则会生成 .so（动态链接库）文件。这样可以减少重复使用时的内存占用，并且便于在多个程序之间共享该库。
	3. `--openssldir=/usr/local/openssl`：设置 OpenSSL 的默认路径。在编译后，OpenSSL 将会把证书、配置文件等默认文件存放在 `/usr/local/openssl` 路径下，这个路径也会成为默认的查找路径。
	4. `--prefix=/usr/local/openssl`：指定安装路径。编译完成后，执行 make install 命令时，OpenSSL 的文件将会被安装到该路径下，即 `/usr/local/openssl`。这样可以将 OpenSSL 安装在用户指定的目录中，而不会覆盖系统默认的 OpenSSL 版本，方便多个版本共存。

```shell
./config shared --openssldir=/usr/local/openssl --prefix=/usr/local/openssl
```

7. 编译并安装：

```shell
sudo make && make install
```

8. 重新尝试运行 `alist-desktop`：

```shell
alist-desktop
```

9. 如果还不行，查看对应安装目录下是否有相应的文件：

```shell
root@yan:~# ll /usr/local/openssl/lib/
总计 10544
drwxr-xr-x 4 root root    4096 10月 29 12:39 ./
drwxr-xr-x 9 root root    4096 10月 29 12:39 ../
drwxr-xr-x 2 root root    4096 10月 29 12:39 engines-1.1/
-rw-r--r-- 1 root root 5628978 10月 29 12:39 libcrypto.a
lrwxrwxrwx 1 root root      16 10月 29 12:39 libcrypto.so -> libcrypto.so.1.1*
-rwxr-xr-x 1 root root 3396552 10月 29 12:39 libcrypto.so.1.1*
-rw-r--r-- 1 root root 1037384 10月 29 12:39 libssl.a
lrwxrwxrwx 1 root root      13 10月 29 12:39 libssl.so -> libssl.so.1.1*
-rwxr-xr-x 1 root root  705272 10月 29 12:39 libssl.so.1.1*
drwxr-xr-x 2 root root    4096 10月 29 12:39 pkgconfig/
root@yan:~# 
```

10. 可以看到，`/usr/local/openssl/lib/` 目录下有 `libssl.so` 和 `libcrypto.so.1.1` 文件，给他们建立符号连接（这点和上面一样了）：

```shell
sudo ln -s /usr/local/openssl/lib/libssl.so.1.1 /usr/lib/x86_64-linux-gnu/libssl.so.1.1
sudo ln -s /usr/local/openssl/lib/libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
```

11. 重新尝试运行 `alist-desktop`：

```shell
alist-desktop
```

# 三、TaoSync （桃桃的自动同步工具）基于 AList 的网盘同步工具

> github 项目地址：https://github.com/dr34m-cn/taosync

## 1、介绍

1. 同步备份：
	1. 把本地文件备份到多个网盘或 FTP 之类的存储，或者在多个网盘之间同步文件等；
	2. 可以定时扫描指定目录下文件差异，让目标目录与源目录相同（全同步模式）；或仅新增存在于源目录，却不存在于目标目录的文件（仅新增模式）
2. 定时下载：可以设置一次性任务（cron方式设置年月日时分秒，将在指定时间执行一次），可在闲时自动从特定网盘下载文件到本地

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/taosync`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8023:8023 \
-v /home/docker/docker/volumes/taosync:/app/data \
--restart=unless-stopped \
--name=taoSync \
dr34m/tao-sync:latest
```

## 3、访问

1. 部署成功后，会随机生成一个密码，在日志中查看：

```shell
docker logs taoSync
```

2. 访问：[http://127.0.0.1:8023](http://127.0.0.1:8023)
3. 进入主页面，输入账号 `admin` 以及刚才查看的密码进行登录
4. 登录成功后，点击系统设置，通过刚才查看的密码，修改新密码

# 四、qBittorrent BitTorrent 客户端

> github 项目地址：https://github.com/linuxserver/docker-qbittorrent

## 1、介绍

1. qBittorrent 是一个开源的、跨平台的 BitTorrent 客户端，支持 Web UI
2. 具有图形用户界面（GUI）和强大的功能，如种子管理、搜索引擎、RSS 支持和带宽管理等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/qbittorrent/config`
	2. 下载目录：`/home/docker/docker/volumes/qbittorrent/downloads`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器

```shell
docker run -d \
-e TZ=Asia/Shanghai \
-e WEBUI_PORT=8081 \
-p 8081:8081 \
-p 6881:6881 \
-p 6881:6881/udp \
-v /home/docker/docker/volumes/qbittorrent/config:/config \
-v /home/docker/docker/volumes/qbittorrent/downloads:/downloads \
--restart unless-stopped \
--name=qbittorrent \
linuxserver/qbittorrent
```

## 3、访问

1. 部署成功后，会随机生成一个密码，在日志中查看：

```shell
docker logs qbittorrent
```

2. 访问：[http://127.0.0.1:8081](http://127.0.0.1:8081)，进入主页面，输入账号 admin 以及刚才查看的密码进行登录
3. 登录成功后，点击工具 -> 选项 -> WebUI，通过刚才查看的密码，修改新密码

## 4、使用 nginx 代理

1. 确保启动参数无误，尤其是配置文件的目录，必须是 qbittorrent 的父级目录，不可以到 qbittorrent 这一层
2. 如果是在外网通过 IP 访问内网服务器，则需查看 `qbittorrent.conf` 中，是否设置了 `WebUI\HostHeaderValidation=true` 参数，如有，请改为 false
3. 如果是在外网通过域名访问内网服务器，则第二条同样适用；但安全起见，建议改为 true 并把值设置为域名
4. 如果并未配置 HTTPS 证书，或未安装相关组件，则需查看 `qbittorrent.conf` 中，是否设置了 `WebUI\HTTPS\Enabled=ture` 参数，如有，请改为 false
5. 在 nginx-proxy-manager 中设置代理，然后点击高级，设置以下内容：

```nginx
location / {
	proxy_pass http://172.17.0.1:8081/; # 根据 IP 地址和端口号修改
	proxy_http_version 1.1;
	proxy_set_header Host 172.17.0.1:8081; # 根据 IP 地址和端口号修改
	proxy_set_header X-Forwarded-Host $http_host;
	proxy_set_header X-Forwarded-For $remote_addr;

	proxy_cookie_path / "/; Secure"; # 从 4.2.2 版本起，若在 qBittorrent 内部设置了 HTTPS，则不需要设置该参数。否则，必须设置该参数用以保证 Cookie 的安全性
	# 可选，设置后可一次性添加 100M 的种子
	#client_max_body_size 100M;
}
```

6. 以下参数不适用于 qBittorrent，若是有请务必移除：

```nginx
location / {
	#  以下参数不适用于 qBittorrent，若是有请务必移除
	#proxy_set_header   X-Forwarded-Proto  $scheme;
	#proxy_set_header   X-Real-IP          $remote_addr;
}
```

7. 其中 3、5 条最重要，修改完毕后重启即可

## 5、使用 nginx 代理方式 2

1. 如果经过上面的方式依然无法访问，访问时 qbittorrent 日志可能提示：

```shell
(W) 2024-12-25T14:01:42 - WebUI: 请求 Header 中 Referer 与 XFH/Host 不匹配！来源 IP: '::ffff:172.17.0.1'。Referer: 'https://qbittorrent.yuehai.fun:8080/'。XFH/Host: 'qbittorrent.yuehai.fun'
```

2. 我找了找，没找到解决办法，这里再提供另一个解决办法
3. 上面 4 中的配置不再需要，nginx 中仅配置代理即可

![|474](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108100020.png)

4. 本地进入 qbittorrent 的管理页，点击设置 -> WebUI，勾选**对 IP 子网白名单中的客户端跳过身份验证**，并设置如下内容：
	1. 最重要的是 `172.17.0.0/16` 这一条，对 docker 应用的 ip 设置白名单
	2. 下面的两条是对内网访问的放行，仅方便内网不同电脑的调用，可以不设置

```shell
172.17.0.0/16
192.168.31.0/24
127.0.0.1/32
```

5. 向下翻，取消勾选**启用跨站请求伪造 (CSRF) 保护**

![|550](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108100058.png)

6. 点击保存即可

# 五、Nexterm 基于浏览器的服务器管理工具

> github 项目地址：https://github.com/gnmyt/Nexterm

## 1、介绍

1.  Nexterm 是一个多功能的终端应用程序，专为提高开发者在使用命令行时的效率而设计。它通常包括如下几个关键功能：
1. **多标签和拆分视图**：用户可以在一个窗口中打开多个标签，每个标签可以进一步拆分为多个视图，方便同时监控和操作多个会话
2. **高度可定制**：Nexterm 提供丰富的定制选项，包括主题、快捷键和布局等，用户可以根据个人喜好调整这些设置
3. **集成开发环境功能**：此应用程序可能集成了代码编辑器、版本控制系统以及其他开发工具，使其不仅仅是一个简单的终端模拟器，而是一个全面的开发环境
4. **插件和扩展支持**：通过支持插件和扩展，Nexterm 允许用户添加新功能或集成其他工具，以扩展其核心功能
5. **跨平台兼容性**：Nexterm 设计之初就考虑到了跨平台使用的需求，通常支持 Windows、MacOS 和各种 Linux 发行版
6. **高级命令行功能**：可能包括内置的命令行搜索、历史记录管理和自动完成等功能，以提升用户的工作效率
7. Nexterm 旨在为开发者提供一个强大而高效的工作环境，通过以上的功能帮助用户简化和优化日常的开发任务。不过需要注意的是，关于 Nexterm 的具体信息可能因版本和开发社区的持续更新而有所变动

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/nexterm/data`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 6989:6989 \
-v /home/docker/docker/volumes/nexterm/data:/app/data \
--restart=unless-stopped \
--name nexterm \
germannewsmaker/nexterm:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:6989](http://127.0.0.1:6989)
2. 初次访问需设定管理员账号密码

# 六、Nextcloud 自托管云存储和协作平台

> 1. github 项目地址：https://github.com/55190116/nextcloud-docker
> 2. 该项目需要关联一个数据库作为数据的存取

## 1、介绍

1. Nextcloud 是一个开源的私人云存储解决方案，它可以在本地或托管的环境中部署，为用户提供类似 Google Drive、Dropbox 的功能，支持文件存储、共享、协作等特性
2. Nextcloud 的核心功能：
3. **文件管理**：上传、下载、删除、共享文件。
4. **用户管理**：支持多用户系统和权限控制。
5. **扩展功能**：通过应用商店安装插件（如日历、任务管理、在线文档编辑）。
6. **设备同步**：支持 Windows、macOS、Linux 和移动端的客户端同步。
7. **加密和安全**：支持端到端加密，保障数据隐私。

## 2、docker 部署

1. 首先需要一个数据库，不论在本地或者其他服务器都可
2. 在数据库中创建一个 `nextcloud` 库，然后创建一个 `nextcloud` 用户名，允许其创建和修改 `nextcloud` 库中的表

```shell
CREATE DATABASE nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE USER 'nextcloud'@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@'%';
GRANT CREATE ON *.* TO 'nextcloud'@'%';

FLUSH PRIVILEGES;
```

3. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/nextcloud/config`
	2. 数据目录：`/home/docker/docker/volumes/nextcloud/data`
	3. 应用目录：`/home/docker/docker/volumes/nextcloud/apps`
4. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 80:80 \
-v /home/docker/docker/volumes/nextcloud/data:/var/www/html/data \
-v /home/docker/docker/volumes/nextcloud/config:/var/www/html/config \
-v /home/docker/docker/volumes/nextcloud/apps:/var/www/html/apps \
-v /home/docker/docker/volumes/nextcloud/html:/var/www/html \
--privileged=true \
--restart=unless-stopped \
--name nextcloud \
nextcloud:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 第一次进入需设置账号、密码、数据库信息

## 4、Nextcloud 集成 Onlyoffice

> 1. 需要部署 Onlyoffice
> 2. 这里采用离线安装的方式，因为我的应用商店无法访问，插件下载：[onlyoffice.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Fonlyoffice.tar.gz)
> 3. 如果可以访问应用商店，直接搜索 Onlyoffice 安装

1. 进入 Nextcloud 应用商店下载插件：https://apps.nextcloud.com/
2. 搜索 Onlyoffice

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108100948.png)

3. 向下拉，选择一个版本进行下载

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101004.png)

4. 下载完成后，将其上传到挂载的 `/home/docker/docker/volumes/nextcloud/apps` 目录中

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101018.png)

5. 进入该目录，然后将 Onlyoffice 插件解压：

```shell
cd /home/docker/docker/volumes/nextcloud/apps/

tar -zxvf onlyoffice.tar.gz
```

6. 修改解压后文件的用户组：

```shell
chown -R www-data:www-data onlyoffice
```

7. 进入 Nextcloud 页面，点击头像 -> 应用 -> 你的应用，会多出来一个 ONLYOFFICE，点击后面的启用来启用插件

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101034.png)

8. 在 onlyoffice 7.2 版本之后，需要使用秘钥才能连接上，使用下面的命令获取 onlyoffice 的秘钥：

```shell
sudo docker exec onlyoffice /var/www/onlyoffice/documentserver/npm/json -f /etc/onlyoffice/documentserver/local.json 'services.CoAuthoring.secret.session.string' 
```

9. 启用成功后，点击头像 -> 管理设置，也会多出来一个 ONLYOFFICE，点击进入，填写 ONLYOFFICE Docs 地址和密钥
	1. ONLYOFFICE Docs 地址就是部署的 Onlyoffice 的 ip 和端口号。如：`http://ip:port/`
	2. 密钥就是上面使用命令获取的密钥

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101059.png)

10. 点击保存即可集成，成功后下方会显示常用设置等

## 5、修改 Nextcloud 集成 Onlyoffice 后的页面的样式

1. Nextcloud 集成 Onlyoffice 后默认的页面是这样的，上面还有一个工具栏，看着很不舒服，现在把他去掉

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101122.png)

2. 进入挂载目录：`/home/docker/docker/volumes/nextcloud/html/custom_apps/onlyoffice/css/editor.css`，编辑：
3. 在顶部添加：

```css
/* 强制隐藏 Header */
#header {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    overflow: hidden !important;
}
```

4. 修改：

```css
/* 原样式： */
#content.app-onlyoffice #app > iframe {
    height: calc(100dvh - 50px);
    margin-top: 0px;
}

/* 修改后： */
#content.app-onlyoffice #app > iframe {
    height: 100dvh;
    margin-top: -50px;
}
```

5. 修改后的页面显示：按住 shift 刷新浏览器：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101143.png)

## 6、使用 Nginx 反向代理 Nextcloud 并配置 HTTPS 访问

1. 在 nginx 上的配置不在详细说明；配置完成后，访问：`https://nextcloud.yuehai.fun:8080` 会出现如下提示：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101208.png)

2. 这是代理成功了，但是我们需要修改 Nextcloud 的配置文件，添加信任域名并修改配置
3. 进入挂载目录：`/home/docker/docker/volumes/nextcloud/config/`

```shell
cd /home/docker/docker/volumes/nextcloud/config/
```

4. 打开文件 `config.php` 并编辑：

```shell
nano config.php
```

5. 修改 `trusted_domains`，添加域名为信任域名：
	1. 主要是格式和 `nextcloud.yuehai.fun`、`172.17.0.1` 两项
	2. 将 `nextcloud.yuehai.fun` 替换为 Nginx 代理的域名；<font color="#ff0000">下面设置的域名都要和这个相同</font>

```php
  /**
   * trusted_domains 是一个列表，指定可以被信任的域名或 IP 地址。只有请求的主机名或 IP 匹配此列表中的条目时，Nextcloud 才会响应请求
   * 支持的格式：
   *  - 精确的主机名（如 example.com）
   *  - 包含端口号的主机名（如 example.com:443）
   *  - IP 地址（IPv4 或 IPv6）
   *  - 使用通配符的子域名（如 *.example.com）
   */
  'trusted_domains' => 
  [
    'localhost', // 本机 IP
    '127.0.0.1', // 本机 IP
    'nextcloud.yuehai.fun', // 可以访问 Nextcloud 的域名
    '172.17.0.1',  // Docker 容器 IP
  ],
```

6. 修改 `overwrite.cli.url`，设置基础 URL：

```php
  /**
   * overwrite.cli.url 是一个手动设置的基础 URL，用于生成命令行工具（例如 cron 任务或 occ 工具）中使用的链接
   * 确保当 Nextcloud 后台任务（例如 cron）生成 URL 时，使用的是正确的主机和路径
   * 避免在某些代理或特定网络环境中生成错误的 URL
   */
  'overwrite.cli.url' => 'https://nextcloud.yuehai.fun:8080',
```

7. 在最后一行 `);` 前添加如下内容

```php
  /**
   * overwritehost 用于覆盖 Nextcloud 自动检测的主机名，通常在代理（reverse proxy）设置中使用
   * 强制 Nextcloud 使用指定的主机名，而不是从请求中自动检测的主机名
   * 解决代理场景中，因主机名不匹配导致生成错误链接的问题
   */
  'overwritehost' => 'nextcloud.yuehai.fun:8080',
  /**
   * overwriteprotocol 用于指定请求是通过 http 或 https 协议访问的
   * 强制生成 HTTPS 链接，而不是根据请求的协议动态检测
   * 解决代理场景中，代理处理 HTTPS 请求，但传递给后端时为 HTTP 的问题
   */
  'overwriteprotocol' => 'https',
```

8. 修改完毕后，重启容器，即可成功访问

## 7、应用整理

> 对应的 nextcloud 版本是 30

### ①、Notes

1. 介绍：笔记，支持 markdown
2. 商店地址：https://apps.nextcloud.com/apps/notes
3. 本地下载：[notes-v4.11.0.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Fnotes-v4.11.0.tar.gz)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101326.png)

### ②、Draw.io

1. 介绍：在线图表工具，文件直接保存到 Nextcloud
2. 商店地址：https://apps.nextcloud.com/apps/drawio
3. 本地下载：[drawio-v3.0.3.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Fdrawio-v3.0.3.tar.gz)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101434.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101444.png)

### ③、Mind Map

1. 介绍：思维导图
2. 商店地址：https://apps.nextcloud.com/apps/files_mindmap
3. 本地下载：[files_mindmap-0.0.31.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Ffiles_mindmap-0.0.31.tar.gz)

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101527.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101536.png)

### ④、

# 七、Onlyoffice 提供文档、电子表格、演示文稿等工具

## 1、介绍

1. nlyOffice 是一套强大的在线办公套件，支持文档、表格和幻灯片的创建、编辑和协作。
2. 并与多种平台（如 Nextcloud、OwnCloud）无缝集成，用于构建在线办公环境
3. 1. OnlyOffice 的核心功能：
4. **文档编辑功能**：兼容 Microsoft Office 格式（DOCX、XLSX、PPTX），支持常见的文件格式（如 ODT、ODS、ODP）
5. **协作编辑**：实时多人协作，支持评论、版本历史和变更跟踪
6. **可扩展性**：与其他系统（如 Nextcloud、OwnCloud、Confluence 等）集成，支持插件扩展功能
7. **部署灵活**：提供社区版（免费）和企业版（付费），可满足不同规模用户需求

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 日志目录：`/home/docker/docker/volumes/Onlyoffice/log`
	2. 文档目录：`/home/docker/docker/volumes/Onlyoffice/data`
	3. 缓存数据：`/home/docker/docker/volumes/Onlyoffice/lib`
	4. 数据库文件：`/home/docker/docker/volumes/Onlyoffice/db`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-e JWT_ENABLED`：启用 JWT 验证和密钥等
	3. `-p`：指定端口映射
	4. `-v`：指定挂载目录
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 80:80 \
-e JWT_ENABLED=true \
-e JWT_SECRET=xhiNbpVz7zmszBSUNBeWTTtyColkmGYE \
-e JWT_HEADER=Authorization \
-v /home/docker/docker/volumes/Onlyoffice/log:/var/log/onlyoffice  \
-v /home/docker/docker/volumes/Onlyoffice/data:/var/www/onlyoffice/Data  \
-v /home/docker/docker/volumes/Onlyoffice/lib:/var/lib/onlyoffice \
-v /home/docker/docker/volumes/Onlyoffice/db:/var/lib/postgresql  \
--restart=unless-stopped \
--name onlyoffice \
onlyoffice/documentserver
```

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)，出现下面页面则部署成功

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108101959.png)

2. 执行下面两条命令，启动 onlyoffice 的测试示例页面：

```shell
docker exec onlyoffice sudo supervisorctl start ds:example

docker exec onlyoffice sudo sed 's,autostart=false,autostart=true,' -i /etc/supervisor/conf.d/ds-example.conf
```

3. 点击 `GO TOTESTEXAMPLE` 按钮，可进入测试示例页面

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102030.png)

4. 在测试示例页面，可选择语言，选择后地址栏上会带上参数：`lang=zh`，建议将此时的地址存为书签，因为语言的设置并不会保存，只能以地址参数设置

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102044.png)

5. 可尝试新建或上传一个文档，测试可用性

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102100.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102112.png)

## 4、设置 OnlyOffice 自动保存

1. 进入容器：

```shell
docker exec -it onlyoffice bash
```

2. 进入 `/etc/onlyoffice/documentserver/` 目录：

```shell
cd /etc/onlyoffice/documentserver
```

3. 编辑 `local.json` 文件：

```shell
nano local.json
```

4. 在 `CoAuthoring` 字段中添加配置：

```shell
"autoAssembly": { "enable": true, "interval": "5m" },
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102127.png)

5. 重启即可

## 5、OnlyOffice 开启 ssl

1. 我一开始使用 nginx 进行代理，但是因为各种验证问题、配置问题、路径问题，始终无法和 nextcloud 在 ssl 的状态下进行连接，所以这里直接开启 onlyoffice 原生的 ssl 
2. 首先停止并删除之前的容器

```shell
# 停止
docker stop onlyoffice

# 删除
docker rm onlyoffice
```

3. 在 nginx-proxy-manager 中下载证书：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102246.png)

4. 将下载的压缩文件解压，得到下面的四个文件：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102258.png)

5. 在服务器的挂载路径 `/home/docker/docker/volumes/Onlyoffice/data` 目录下创建一个 `certs` 目录

```shell
mkdir /home/docker/docker/volumes/Onlyoffice/data/certs
```

6. 将上面四个文件中的 `cert1.pem` 和 `privkey1.pem` 上传到 `certs` 目录中，并且：
	1. 将 `cert1.pem` 改名为：`onlyoffice.crt`
	2. 将 `privkey1.pem` 改名为：`onlyoffice.key`
	3. 一定要改名，否则启动会报错

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102325.png)

7. 重新启动容器，将原本映射的 `80` 端口号改为 `443`：``

```shell
docker run -d \
-p 443:443 \
-e JWT_ENABLED=true \
-e JWT_SECRET=xhiNbpVz7zmszBSUNBeWTTtyColkmGYE \
-e JWT_HEADER=Authorization \
-v /home/docker/docker/volumes/Onlyoffice/log:/var/log/onlyoffice  \
-v /home/docker/docker/volumes/Onlyoffice/data:/var/www/onlyoffice/Data  \
-v /home/docker/docker/volumes/Onlyoffice/lib:/var/lib/onlyoffice \
-v /home/docker/docker/volumes/Onlyoffice/db:/var/lib/postgresql  \
--restart=unless-stopped \
--name onlyoffice \
onlyoffice/documentserver
```

8. 访问：[https://127.0.0.1:443](https://127.0.0.1:443)，出现下面页面则部署成功

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108102354.png)

# 八、Memos 开源、轻量级的备忘录服务

## 1、介绍

1. Memos 是一个轻量级的开源备忘录应用，适合用于个人知识管理、日记记录或团队协作等场景。
2. 它以其简单易用、轻量化、高度定制化的特点，成为许多用户钟爱的工具
3. Memos 的核心功能：
4. **简洁的用户界面**：以简约风格设计，专注于高效记录。
5. **富文本支持**：支持 Markdown 语法，方便格式化内容。
6. **多终端同步**：支持多设备无缝访问。
7. **数据私有化**：用户可以完全掌控数据，特别适合需要隐私保护的场景。
8. **插件支持**：提供多种扩展功能，比如搜索、分类、标签管理等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/Memos/data`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录

```shell
docker run -d \
-p 5230:5230 \
-v /home/docker/docker/volumes/Memos/data:/var/opt/memos \
--name memos \
neosmemo/memos:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:5230](http://127.0.0.1:5230)
2. 初次访问需设定管理员账号密码

# 九、2FAuth 基于 Web 的自托管 2FA 双因素认证替代方案

## 1、介绍

1. 2FA 即双因素认证。一般来说，在大多数场景下都是使用帐号和密码来进行身份验证，而 2FA 就是除了建立帐号密码之外的第二个关卡。就算账号和密码不小心外泄了，也不至于账号马上被盗用。
2. 2FA 又分为硬件型和软件型。像在 App Store 上购买 App 时需要指纹，或者网银转账时需要用到的 U 盾，只有通过那只随身携带在身上的硬件才能通过验证，这些都属于硬件型的 2FA。而 OTP(One Time Password) 就是软件型的 2FA 。像大部分 APP 在风险操作时都会要求你输入验证码、或者当你要从新电脑登陆时，也需要到手机查看验证码，当然这些都是免费的。
3. 2FAuth 是一种基于 Web 的自托管替代方案，可替代 Google Authenticator 等一次性密码 （OTP） 生成器，专为移动设备和桌面设备设计。它能够通过 web 方式获取 OTP，并且将 2FA 帐户存储在一个独立的数据库中，利于数据的备份和恢复。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/2fauth/2fauth`
2. 修改目录权限：

```shell
chown 1000:1000 /home/docker/docker/volumes/2fauth/2fauth
```

3. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `-e APP_DEBUG`：是否启用调试模式
	5. `-e APP_NAME`：设置应用的显示名称
	6. `-e APP_KEY`：应用加密密钥；用于加密敏感数据，例如用户认证信息，必须是一个长度为 32 的随机字符串
	7. `-e APP_URL`：应用的基础 URL，设置应用的访问地址
	8. `-e IS_DEMO_APP`：是否为演示模式；启用演示模式，可能会限制某些操作（如禁止修改核心配置）
	9. `-e LOG_CHANNEL`：日志记录方式；`daily`：按天分隔日志文件
	10. `-e LOG_LEVEL`：日志记录级别，控制记录哪些日志级别的信息；常见级别：
		1. `debug`：调试信息。
		2. `info`：普通信息。
		3. `notice`：重要信息但非错误。
		4. `warning`：警告信息。
		5. `error`：错误信息。
		6. `critical`：严重错误信息。
	11. `-e CACHE_DRIVER`：缓存驱动；设置应用的缓存存储方式：`file`：将缓存存储在文件中。
	12. `-e SESSION_DRIVER`：会话存储驱动；设置用户会话存储的方式：`file`：将会话存储在文件中。
	13. `-e AUTHENTICATION_GUARD`：认证守卫；指定认证方式：`web-guard` 可能是一个为此应用预定义的认证方式，用于处理用户登录状态
	14. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	15. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8000:8000 \
-e APP_DEBUG=true \
-e APP_NAME=2FAuth \
-e APP_KEY=******************************** \
-e APP_URL=https://***.yuehai.fun:8080 \
-e IS_DEMO_APP=false \
-e LOG_CHANNEL=daily \
-e LOG_LEVEL=notice \
-e CACHE_DRIVER=file \
-e SESSION_DRIVER=file \
-e AUTHENTICATION_GUARD=web-guard \
-v /home/docker/docker/volumes/2fauth/2fauth:/2fauth \
--privileged=true \
--restart=unless-stopped \
--name 2fauth \
2fauth/2fauth
```

## 3、访问

1. 因为设定了 `APP_URL=https://***.yuehai.fun:8080`，所以访问地址只能是：`https://***.yuehai.fun:8080/start`
2. 这是通过 nginx 代理之后的地址
3. 初次访问需注册管理员账号密码

# 十、filebrowser 极简的文件管理工具

## 1、介绍

1. Filebrowser 是一个开源的文件管理服务，它允许用户通过浏览器管理本地或远程的文件系统。
2. 它可以通过简单的界面完成文件上传、下载、删除、移动、复制等操作，同时支持用户权限管理、认证等功能，非常适合用于个人、团队文件管理或嵌入其他项目中
3. 主要功能：
4. 文件管理：
	1. 支持上传、下载、移动、删除、复制、重命名文件和文件夹。
	2. 可通过直观的用户界面浏览文件结构。
5. 多用户支持：
	1. FileBrowser 支持多个用户，并为每个用户提供单独的文件夹和权限设置。
	2. 可限制用户对某些目录的访问权限。
6. 文件预览与编辑：
	1. 内置支持多种文件格式的预览（如图片、视频、文档等）。
	2. 提供简单的文本编辑功能，可直接修改文本文件。
7. 文件共享：
	1. 支持通过链接分享文件或文件夹。
	2. 可以设置分享链接的过期时间和访问权限。
8. 跨平台支持：
	1. 支持多种操作系统，包括 Windows、macOS、Linux 和 Docker。
	2. 可用于 NAS 设备或 Web 服务器环境。
9. 安全性：
	1. 提供用户认证机制，支持基本认证和 JWT。
	2. HTTPS 支持，保证数据传输安全。
10. API 集成：
	1. 提供 RESTful API，方便与其他系统或应用集成。
11. 扩展性和定制化：
	1. 支持通过配置文件（YAML 或 JSON）进行自定义。
	2. 用户界面可自定义，支持换主题或定制登录页面。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 文件目录：`/home/docker/docker/volumes/filebrowser/files`
	2. 数据目录：`/home/docker/docker/volumes/filebrowser/database`
	3. 配置目录：`/home/docker/docker/volumes/filebrowser/config`
	4. ssl 证书目录：`/home/docker/docker/volumes/filebrowser/ssl`，不启用 ssl 证书的话可以不设置
2. 在数据目录：`/home/docker/docker/volumes/filebrowser/database` 中提前创建一个空的 db 文件用于存储：

```shell
# 进入目录
cd /home/docker/docker/volumes/filebrowser/database

# 创建文件
touch database.db
```

3. 在配置目录：`/home/docker/docker/volumes/filebrowser/config` 中创建配置文件 `filebrowser.json`，并填入以下内容
	1. 不启用 ssl 证书的话可以不设置 `cert` 和 `key` 两个字段

```shell
# 进入目录
cd /home/docker/docker/volumes/filebrowser/config

# 创建或编辑文件
nano filebrowser.json
```

```shell
{
  "address": "0.0.0.0",
  "port": 8080,
  "locale": "zh-cn",
  "baseURL": "/",
  "log": "stdout",
  "database": "/database.db",
  "root": "/srv",
  "cert": "/ssl/cert.pem",
  "key": "/ssl/privkey.pem"
}
```

4. 若是要启用 ssl 的话，将 `cert.pem` 和 `privkey.pem` 复制到 ssl 证书目录：`/home/docker/docker/volumes/filebrowser/ssl`，不启用 ssl 证书的话可以不设置；获取证书的方式：[使用 Let's Encrypt 免费获取证书](https://github.com/yue-hai/TakeDown/blob/master/%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/%E7%BD%91%E7%BB%9C%E7%9B%B8%E5%85%B3.md#1%E4%BD%BF%E7%94%A8-lets-encrypt-%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%AF%81%E4%B9%A6)
5. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `health` 的这几个设置是如果开启了 ssl 的话，会导致 docker 的健康检查出问题，容器的状态为 `unhealthy`，现在这样改为手动指定检测方式；不启用 ssl 证书的话可以不设置这几个配置
	5. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	6. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8080:8080 \
-v /home/docker/docker/volumes/filebrowser/files:/srv \
-v /home/docker/docker/volumes/filebrowser/database/database.db:/database.db \
-v /home/docker/docker/volumes/filebrowser/config/filebrowser.json:/.filebrowser.json \
-v /home/docker/docker/volumes/filebrowser/ssl:/ssl \
--health-cmd "curl -k https://localhost:8080 || exit 1" \
--health-interval=30s \
--health-timeout=5s \
--health-retries=3 \
--privileged=true \
--restart unless-stopped \
--name filebrowser \
filebrowser/filebrowser
```

## 3、访问

1. 访问：[http://127.0.0.1:8080](http://127.0.0.1:8080)
2. 初始账号密码都为 `admin`

# 十一、Jellyfin 媒体服务器

## 1、介绍

1. Jellyfin 是一个开源的媒体服务器软件，旨在提供类似 Plex 和 Emby 的家庭媒体管理和流媒体功能。
2. Jellyfin 不同于其他类似软件的最大特点是它完全免费且没有任何订阅费用，并且尊重用户的隐私，不会收集或存储用户数据。
3. Jellyfin 与 Plex、Emby 和相比完全开源免费，不过性能和稳定性略低于其他两个
4. Jellyfin 核心功能：
5. **媒体管理：**
	1. 支持管理多种类型的媒体内容，包括电影、电视剧、音乐、照片、有声书等
	2. 自动从网络上抓取元数据，例如封面、演员信息、剧情简介等
	3. 支持多种媒体格式，能处理大多数主流的音视频文件
6. **跨平台支持：**
	1. Jellyfin 可以部署在多种平台上，包括 Windows、Linux、macOS 以及 Docker 容器
	2. 提供多种客户端应用程序，支持智能电视、手机、平板、浏览器、Roku、Fire TV 等设备
7. **流媒体播放：**
	1. 支持多种流媒体协议（如 DLNA 和 Chromecast），可以直接将内容推送到其他设备
	2. 支持实时转码（transcoding），确保即使设备不支持某种格式也能正常播放
	3. 提供多用户支持，可以为每个家庭成员创建独立的配置和媒体收藏
8. **隐私保护：**
	1. Jellyfin 是完全本地化的服务，不需要连接外部服务器，也不会收集用户数据
	2. 用户完全控制自己的数据和服务器
9. **插件支持：**
	1. 提供丰富的插件生态系统，允许用户扩展 Jellyfin 的功能
	2. 插件功能包括直播电视（通过兼容的 TV 卡）、字幕同步（如 OpenSubtitles）、第三方媒体数据整合等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 缓存目录：`/home/docker/docker/volumes/jellyfin/cache`
	2. 配置目录：`/home/docker/docker/volumes/jellyfin/config`
	3. 媒体目录：`/home/docker/docker/volumes/jellyfin/media`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-e TZ=Asia/Shanghai \
-p 8096:8096 \
-p 8920:8920 \
-v /home/docker/docker/volumes/jellyfin/cache:/cache \
-v /home/docker/docker/volumes/jellyfin/config:/config \
-v /media/yan/hc330-10t-A/备份:/media \
--privileged=true \
--restart unless-stopped \
--name=jellyfin \
jellyfin/jellyfin:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:8096](http://127.0.0.1:8096)
2. 初次访问需设定管理员账号密码

## 4、设置媒体库

1. 进入控制台后，点击媒体库，然后点击添加媒体库

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108104150.png)

2. 之后选择类型、名称、文件夹、各种设置即可

## 5、访问媒体库

> 各种客户端下载：https://jellyfin.org/downloads/clients/

1. 各种客户端可点击上面的链接进行下载
2. 若是想在浏览器观看，则进入服务器后，点击服务器名称

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108104208.png)

3. 即可查看设定的媒体库

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108104221.png)

## 6、https 设置

> 获取证书的方式：[使用 Let's Encrypt 免费获取证书](https://github.com/yue-hai/TakeDown/blob/master/%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/%E7%BD%91%E7%BB%9C%E7%9B%B8%E5%85%B3.md#1%E4%BD%BF%E7%94%A8-lets-encrypt-%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%AF%81%E4%B9%A6)

1. 将生成的 `mykeystore.p12` 文件复制到挂载的目录下，比如 `/home/docker/docker/volumes/jellyfin/config/certificate/`
2. jellyfin 控制台中，选择网络，点击启用 https

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108104244.png)

3. 在 HTTPS 设置中，选择刚才复制的 `mykeystore.p12` 文件，填入证书密码，然后重启服务器即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108104304.png)

4. 成功后访问 https 端口：[https://127.0.0.1:8920](https://127.0.0.1:8920)

# 十二、navidrome 开源的、自托管的音乐流媒体服务器

## 1、介绍

1. Navidrome 是一个开源的、自托管的音乐流媒体服务器
2. 它专注于轻量级、高性能和用户友好的体验，使用户可以随时随地通过任何设备访问和播放自己的音乐库
3. Navidrome 是 Subsonic API 的兼容替代品，因此可以与许多现有的 Subsonic 客户端应用一起使用。
4. 核心功能：
5. **多设备支持**：
	1. 支持通过 Web 界面、移动设备（iOS/Android）、桌面客户端等访问音乐。
	2. 与 Subsonic API 兼容，可以使用现有的 Subsonic 客户端应用。
6. **媒体管理**：
	1. 自动扫描和索引音乐文件，支持多种文件格式（如 MP3、FLAC、AAC 等）。
	2. 提取和显示专辑封面、艺术家信息、元数据等。
	3. 支持智能播放列表和离线下载。
7. **流媒体功能**：
	1. 实时转码以适应设备和网络条件，提供无缝播放体验。
	2. 支持多用户同时播放，并允许创建独立用户账户。
8. **轻量级与跨平台**：
	1. 资源占用极低，适合运行在小型设备上（如树莓派）。
	2. 支持多种操作系统，包括 Windows、Linux、macOS 和 Docker。
9. **本地化与多语言支持**：
	1. 提供多个语言选项，方便全球用户使用。
	2. 界面现代且易于导航。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/Navidrome/config`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 4533:4533 \
-e ND_SCANINTERVAL=1h \
-v /media/yan/hc330-10t-A/内存/音乐:/music \
-v /home/docker/docker/volumes/Navidrome/config:/data \
--privileged=true \
--restart unless-stopped \
--name=navidrome \
deluan/navidrome:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:4533](http://127.0.0.1:4533)
2. 初次访问需设定管理员账号密码

# 十三、NapCatQQ 基于 TypeScript 构建的 QQ Node 模块

> 1. github 地址：https://github.com/NapNeko/NapCatQQ
> 2. 官方 Docker 版本 github 地址：https://github.com/NapNeko/NapCat-Docker
> 3. 官网：https://napneko.github.io/
> -------- 
> 4. 本来想将 NapCatQQ 和 nonebot-bison 都部署在阿里云上，但是阿里云的 WebSocket 好像要收费才能开通，所以 nonebot-bison 部署后连接不上
> 5. 但是不知道为什么 NapCatQQ 可以启动，WebSocket 的客户端和服务端都可以正常启动并连接，为什么 nonebot-bison 不行？
> 6. 具体原因到底是不是这个，还有待考证；[WebSocket 官网计费说明](https://help.aliyun.com/zh/edge-security-acceleration/dcdn/configure-websocket)
> 7. 所以现在 NapCatQQ 部署在阿里云上，nonebot-bison 部署在自己的实体机上
> -------- 
> 8. 经过尝试，阿里云上部署之后有可以链接上了，参数都没变，只是将我实体机上使用的镜像导出，上传到了阿里云的服务器上使用
> 9. 难道是上一次镜像下载时出错了？还有待考证

## 1、介绍

1. 基于 TypeScript 构建的 Bot 框架，通过相应的启动器或者框架，主动调用 QQ Node 模块提供给客户端的接口，实现 Bot 的功能
2. 框架通过魔法的手段获得了 QQ 的发送消息、接收消息等接口
3. 为了方便使用，框架通过一种名为 OneBot 的约定将 HTTP / WebSocket 请求按照规范读取，再去调用框架所获得的QQ发送接口之类的接口。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录 1：`/home/docker/docker/volumes/napcat-docker/config`
	2. 配置目录 2：`/home/docker/docker/volumes/napcat-docker/.config`
	3. 日志目录：`/home/docker/docker/volumes/napcat-docker/logs`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
		1. 3000、3001：NapCatQQ 与 QQ 服务器通信的端口
		2. 6099：NapCatQQ 的 web 端口
		3. 3003、3004：预留的，NapCatQQ 服务器端口；只使用反向连接的话，不要这两个端口也可以
	3. `-e WEBUI_TOKEN`：TOKEN，登录 web 后台时需要提供，作为密码
	4. `-v`：指定挂载目录
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 3000:3000 \
-p 3001:3001 \
-p 6099:6099 \
-p 3003:3003 \
-p 3004:3004 \
-e NAPCAT_GID=$(id -g) \
-e NAPCAT_UID=$(id -u) \
-e WEBUI_TOKEN='***' \
-v /home/docker/docker/volumes/napcat-docker/config:/app/napcat/config \
-v /home/docker/docker/volumes/napcat-docker/.config:/app/.config/QQ \
-v /home/docker/docker/volumes/napcat-docker/logs:/app/napcat/logs \
--restart=unless-stopped \
--name napcat \
mlikiowa/napcat-docker:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:6099/webui](http://127.0.0.1:6099/webui)
2. TOKEN 是创建 docker 容器时指定的，如果没有指定，查找挂载目录的 `/config/webui.json` 文件中，填入 `token` 字段的值即可
3. 登录成功后，点击 `QR Code`，使用想要作为机器人的 QQ 扫描登录即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105258.png)

4. 扫描并且确认后，等待几面就会自动进入管理页面

## 4、日志查看

1. 点击日志查看，可以看到登录的 QQ 号接收的消息，私聊和群聊都可以看到

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105417.png)

## 5、将 NapCatQQ 作为 java 端的 WebSocket 服务器

1. 点击网络配置 -> 添加配置
	1. 名称：比如：`将 NapCatQQ 作为 java 端的 WebSocket 服务器`
	2. 类型：WebSocket 服务器

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105436.png)

2. 勾选启用
3. 主机使用默认 `0.0.0.0`，不用修改
4. 端口修改为 3003、3004 其中之一；如果想使用别的端口，需在创建 docker 容器时指定
5. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105626.png)

6. 在 java 中，使用 `ws://ip:3003` 连接服务器

```java
URI uri = new URI("ws://ip:3003");
NapcatQQWebSocketServer client = new NapcatQQWebSocketServer(uri);
client.connect();
```

7. 使用 `Java-WebSocket` 库接收、发送消息

```maven
<!-- Java-WebSocket 是一个 Java 实现的 WebSocket 协议的开源项目 -->
<!-- https://mvnrepository.com/artifact/org.java-websocket/Java-WebSocket -->
<dependency>
	<groupId>org.java-websocket</groupId>
	<artifactId>Java-WebSocket</artifactId>
	<version>1.5.4</version>
</dependency>
```

```java
package com.yuehai.tool.handler.websocket;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;


/**
 * websocket Server 类
 *
 * @author 月海
 * @date 2025/1/5 15:45
 * @description websocket Server 类
 */
public class NapcatQQWebSocketServer extends WebSocketClient {
    
    public NapcatQQWebSocketServer(URI serverUri) {
        super(serverUri);
    }
    
    @Override
    public void onOpen(ServerHandshake serverHandshake) {
        System.out.println("连接成功");
    }
    
    @Override
    public void onMessage(String message) {
        System.out.println("收到消息：" + message);
    }
    
    @Override
    public void onClose(int code, String reason, boolean remote) {
        System.out.println("连接关闭");
    }
    
    @Override
    public void onError(Exception ex) {
        System.out.println("发生错误：" + ex.getMessage());
    }
}
```

8. 启动后，连接上 ws 后，即可发送、接收消息

## 6、将 NapCatQQ 作为 java 端的 http 服务器

> 1. 可通过 ip 和 端口，调用其接口，实现各种操作
> 2. api 文档：https://napcat.apifox.cn/

1. 点击网络配置 -> 添加配置
	1. 名称：比如：`将 NapCatQQ 作为 java 端的 http 服务器`
	2. 类型：HTTP 服务器

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250110092528.png)

2. 勾选启用
3. 端口修改为 3003、3004 其中之一；如果想使用别的端口，需在创建 docker 容器时指定
4. 主机使用默认 `0.0.0.0`，不用修改
5. CORS 和 WS 可以关闭
6. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250110092539.png)

7. 开启后，可通过 ip 和 端口，调用其接口，实现各种操作

## 7、将 NapCatQQ 接入 onebot11 的服务端

1. 继续看下面的 nonebot-bison 的部署和使用

# 十四、nonebot-bison 通用订阅推送插件机器人

## 1、介绍

1. NoneBot-Bison 是 NoneBot 的一个扩展插件，专注于多种消息源（例如 RSS、B 站、推特等）的订阅与推送功能
2. 它的主要功能是帮助用户自动获取指定消息源的内容，并根据需求推送到指定的平台，如 QQ 群聊、Telegram 群组等
3. 主要功能：
4. 多消息源支持：
	1. RSS 订阅
	2. Bilibili 动态
	3. Twitter 帖子
	4. 更多消息源通过插件扩展实现
5. 灵活的推送目标：
	1. 支持将订阅内容推送至：
	2. QQ（通过 OneBot 协议）
	3. Telegram
	4. Discord 等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/nonebot-bison/data`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-e`：设置环境变量
		1. `SUPERUSERS`：管理员 QQ，可管理、配置机器人 QQ
		2. `BISON_CONFIG_PATH`：配置文件目录
		3. `BISON_OUTER_URL`：从外部访问服务器的地址，因为 nonebot-bison 并不能自动识别 IP，所以需要手动指定；
		4. `BISON_FILTER_LOG`：是否过滤来自 nonebot 的 warning 级以下的 log，如果你的 bot 只运行了这个插件可以考虑 开启，默认关
		5. `BISON_USE_PIC`：将几乎所有文字渲染成图片后进行发送，多用于规避风控
	4. `-v`：指定挂载目录
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8080:8080 \
-e SUPERUSERS='["123456"]' \
-e BISON_CONFIG_PATH='/data' \
-e BISON_OUTER_URL='http://ip:8080/bison' \
-e BISON_FILTER_LOG='true' \
-e BISON_USE_PIC='false' \
-v /home/docker/docker/volumes/nonebot-bison/data:/data \
--restart=unless-stopped \
--name nonebot-bison \
felinae98/nonebot-bison
```

## 3、访问

1. 无法直接访问，关联上面的 NapCatQQ 后，通过管理员 QQ 发送 `/后台管理` 才可以获取访问地址

## 4、将 NapCatQQ 接入 onebot11 的服务端

1. 进入 NapCatQQ 的管理后台，点击网络配置 -> 添加配置
	1. 名称：比如：`接入 onebot11 的服务端`
	2. 类型：WebSocket 客户端

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105850.png)

2. 勾选启用
3. URL 填入：`ws://172.17.0.1:8080/onebot/v11/ws`
	1. IP 和端口根据 nonebot-bison 所在主机的地址进行修改
	2. 我是在同一个机器的 docker 下部署的，所以 `172.17.0.1` 指向本机地址，即类似 `127.0.0.1`
4. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105926.png)

5. NapCatQQ 与 nonebot-bison 成功建立链接时，日志上会显示 connect open

```shell
01-07 07:46:40 [INFO] uvicorn | ('172.17.0.1', 37354) - "WebSocket /onebot/v11/ws" [accepted]
01-07 07:46:40 [INFO] websockets | connection open
```

## 5、后台管理

1. NapCatQQ 与 nonebot-bison 成功建立链接后，可以私聊 `/后台管理` 获取后台管理地址

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108105948.png)

2. 也可以直接在群里 @，然后发送指令进行管理：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107151702.png)

# 十五、qinglong 青龙定时任务管理

## 1、介绍

1. 青龙（Qinglong） 是一个支持多种脚本语言的定时任务管理平台，旨在简化和自动化任务调度。
2. 核心功能：
3. **多语言支持**：兼容 Python3、JavaScript、Shell、Typescript 等脚本语言，满足不同用户的需求。
4. **在线管理**：提供在线管理脚本、环境变量和配置文件的功能，方便用户操作。
5. **日志查看**：支持在线查看任务日志，便于监控和调试。
6. **秒级任务设置**：允许用户设置精确到秒的任务调度，提高任务执行的灵活性。
7. **系统通知**：具备系统级通知功能，及时反馈任务状态。
8. **暗黑模式**：提供暗黑模式，提升用户体验。
9. **移动端支持**：支持手机端操作，随时随地管理任务。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/qinglong/data`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-e QlBaseUrl="/" \
-e QlPort="5700" \
-p 5700:5700 \
-v /home/docker/docker/volumes/qinglong/data:/ql/data \
--name qinglong \
--hostname qinglong \
--restart unless-stopped \
whyour/qinglong:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:5700](http://127.0.0.1:5700)
2. 初次访问需设定管理员账号密码

## 4、脚本仓库整理

1. 各平台签到：https://github.com/Sitoi/dailycheckin
2. 京东任务：https://github.com/6dylan6/jdpro
3. 天翼网盘自动签到：https://github.com/Aijiaobin/Cloud189Checkin

## 5、添加依赖

1. 青龙面板部署完毕后，并不可以直接拉库进行使用，还需要安装依赖
2. 进入面板后，点击依赖管理，类型分三种：NodeJs、Python3、Linux，下面分别对其进行添加
3. NodeJs 依赖库

```shell
crypto-js
prettytable
dotenv
jsdom
date-fns
tough-cookie
tslib
ws@7.4.3
ts-md5
jsdom -g
jieba
fs
form-data
json5
global-agent
png-js
@types/node
require
typescript
js-base64
axios
moment
ds
```

4. Python3 依赖库

```shell
requests
canvas  
ping3
jieba
aiohttp
```

5. Linux 依赖库

```shell
bizCode
bizMsg  
lxml
```

6. 安装方式：点击创建依赖，选择对应的依赖类型，勾选自动拆分，将上面的依赖名复制进名称中即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108110424.png)

7. 如果添加依赖库出现安装失败和提示源问题，使用 ssh 工具进入青龙面板容器，执行下面的代码：

```shell
npm config set registry https://registry.npmmirror.com/
```

8. 耐心等待安装即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108110442.png)

9. 如果有的任务执行失败，可以查看日志是不是依赖报错：

```shell
## 开始执行... 2024-12-10 16:58:24


node:internal/modules/cjs/loader:1148
  throw err;
  ^

Error: Cannot find module 'cloud189-sdk'
Require stack:
- /ql/data/scripts/Aijiaobin_Cloud189Checkin_main/src/app.js
    at Module._resolveFilename (node:internal/modules/cjs/loader:1145:15)
    at Module._load (node:internal/modules/cjs/loader:986:27)
    at Module.require (node:internal/modules/cjs/loader:1233:19)
    at require (node:internal/modules/helpers:179:18)
    at Object.<anonymous> (/ql/data/scripts/Aijiaobin_Cloud189Checkin_main/src/app.js:23:25)
    at Module._compile (node:internal/modules/cjs/loader:1358:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1416:10)
    at Module.load (node:internal/modules/cjs/loader:1208:32)
    at Module._load (node:internal/modules/cjs/loader:1024:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:174:12) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '/ql/data/scripts/Aijiaobin_Cloud189Checkin_main/src/app.js' ]
}

Node.js v20.15.1

## 执行结束... 2024-12-10 16:58:24  耗时 1 秒　
```

10. 此处报错 `Error: Cannot find module 'cloud189-sdk'`，说明没有 `cloud189-sdk` 的依赖
11. 此时就下载这个依赖即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108110459.png)

12. 如果不知道是什么类型的依赖，都试试就好了

## 6、青龙面板定时规则

1. 6个数字的定时规则，时间格式：`* * * * * *` （五/六位 cron 时间格式）

| `*(0-59)` | `*(0-59)` | `*(0-23)` | `*(1-31)` | `*(1-12)` | `*(0-7)` |
| --------- | --------- | --------- | --------- | --------- | -------- |
| 秒（可选）     | 分         | 时         | 日         | 月         | 星期       |

2. 第 1 个是秒，第 2 个是分，第 3 个是时，第 4 个是每月的哪日，第 5 个是哪月，第 6 个是每周的周几
3. 数字之间空格隔开
4. 不限制的用 `*` 号替代，定期的时间用 `?` 替代，间隔运行时间用 `*/数字` 替代
5. 同一个时间位多个选项用 `,` 连接，同一个时间位一个区间用 `-` 连接
6. 每天执行，在天位或者周位用 `?` 都行
7. 一般设置每天执行一次就行 `0 0 1 * * ?`
8. 具体示例如下：

| 示例                     | 说明                                         |
| ---------------------- | ------------------------------------------ |
| `0 0 1 * * ?`          | 每天 1 点触发                                   |
| `0 10 1 ? * *`         | 每天 1:10 触发                                 |
| `*/5 * * * * ?`        | 每隔 5 秒执行一次                                 |
| `0 */1 * * * ?`        | 每隔 1 分钟执行一次                                |
| `0 0 2 1 * ? *`        | 每月 1 日的凌晨 2 点执行一次                          |
| `0 0 1 * * ?`          | 每天 23 点执行一次                                |
| `0 0 1 * * ?`          | 每天凌晨 1 点执行一次                               |
| `0 0 1 1 ? *`          | 每月 1 日凌晨 1 点执行一次                           |
| `0 26,29,33 * * * ?`   | 在 26 分、29 分、33 分执行一次                       |
| `0 0 0,13,18,21 * * ?` | 每天的 0 点、13 点、18 点、21 点都执行一次                |
| `0 0 10,14,16 * * ?`   | 每天上午 10 点，下午 2 点，4 点执行一次                   |
| `0 0/30 9-17 * * ?`    | 每天朝九晚五工作时间内每半小时执行一次                        |
| `0 * 14 * * ?`         | 每天下午 2 点到 2:59 期间的每 1 分钟触发                 |
| `0 */5 14 * * ?`       | 每天下午 2 点到 2:55 期间的每 5 分钟触发                 |
| `0 */5 14,18 * * ?`    | 每天下午 2 点到 2:55 期间和下午 6 点到 6:55 期间的每 5 分钟触发 |
| `0 0-5 14 * * ?`       | 每天下午 2 点到 2:05 期间的每 1 分钟触发                 |
| `0 15 10 15 ? *`       | 每月 15 日上午 10:15 触发                         |

# 十六、QD 一个 HTTP 定时任务自动执行 Web 框架

## 1、介绍

1. QD（全称：Quick Deployment）是一个基于 HAR 编辑器和 Tornado 服务器的 HTTP 定时任务自动执行 Web 框架。 它允许用户通过上传抓包得到的 HAR 文件，快速创建并执行 HTTP 请求任务，常用于自动签到等场景。
2. 主要特性：
3. 基于 HAR 文件： 用户只需上传通过抓包工具（如 Chrome 开发者工具）获取的 HAR 文件，即可生成对应的 HTTP 请求任务模板，简化了任务创建过程
4. Tornado 服务器： 采用 Tornado 作为服务器框架，实现异步响应前端请求和发起 HTTP 请求，提高了并发处理能力
5. API 与插件支持： 内置多种 API 和过滤器供模板制作使用，未来计划提供自定义插件支持，增强框架的扩展性
6. 开源项目： QD 基于 MIT 许可证开源，用户可以自由使用、修改和分发

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/qd-qiandao/config`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录

```shell
docker run -d \
-p 80:80 \ 
-v /home/docker/docker/volumes/qd-qiandao/config:/usr/src/app/config \
--name qd-qiandao \ 
qdtoday/qd:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 初次访问需设定管理员账号密码

## 4、脚本仓库整理

1. 各平台签到：https://github.com/wjf0214/qd-templates

## 5、使用 pushplus 进行消息推送

> pushplus 网址：https://www.pushplus.plus/

1. 点击工具箱 -> 推送设置，选择自定义推送，然后下面的任务结果通知选择、任务推送开关全部打开

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108110632.png)

2. 点击工具箱 -> 自定义推送：
3. 请求方法选择 `POST`
4. url 设置为：

```shell
http://www.pushplus.plus/send/
```

5. 请求体格式选择 `application/json`
6. 请求体内容设置为：
	1. token 在 pushplus 的个人中心查看

```json
{
	"token":"****",
	"title":"签到消息",
	"content":"{t}\r\n----------------\r\n{log}"
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108110714.png)

7. 点击测试可查看是否设置成功，点击提交进行保存
8. 设置完成后，可以执行一个任务查看是否可以正常推送

# 十七、ddns-go 一款轻量级、开源的动态域名解析服务

## 1、介绍

1. DDNS-GO 是一款轻量级、开源的动态域名解析服务（Dynamic DNS），主要用于自动将本地的 IP 地址（如家庭宽带的动态 IP）与域名进行绑定，方便外网访问内网服务。它支持多种 DNS 服务商，且跨平台运行，适合个人和小型企业使用。
2. **核心功能**：
3. 动态更新 IP 地址：
	1. 自动检测本地公网 IP 地址的变化。
	2. 定期将最新的 IP 地址更新到 DNS 服务商的解析记录中。
4. 多种 DNS 服务商支持，支持多个主流的域名解析服务商，如：
	1. 阿里云 DNS
	2. 腾讯云 DNS
	3. Cloudflare
	4. 华为云 DNS
	5. GoDaddy 等。
5. 多平台支持，支持主流操作系统，包括：
	1. Windows
	2. macOS
	3. Linux
	4. Docker 环境。
6. 轻量级与开源：
	1. 软件设计简单易用，占用资源少。
	2. 开源项目，代码透明，可供开发者定制。
7. 安全性：
	1. 支持 HTTPS 和加密连接。
	2. 用户凭证通过配置文件安全存储。
8. 通知功能：IP 更新成功后，可通过邮箱或其他方式通知用户。
9. **适用场景**：
10. 家庭网络：
	1. 家庭用户通过宽带拨号获取的公网 IP 通常是动态的，DDNS-GO 可以解决公网 IP 频繁变动的问题。
	2. 方便用户通过自定义域名远程访问家中设备（如 NAS、路由器、监控系统）。
11. 企业内网穿透：小型企业可以使用 DDNS-GO 实现公网域名与内网服务器的绑定，方便外网办公。
12. 开发者与测试环境：对需要经常测试外网访问本地服务的开发者尤为有用。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 文件目录：`/home/docker/docker/volumes/ddns-go/root`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 9876:9876 \
-v /home/docker/docker/volumes/ddns-go/root:/root \
--restart=unless-stopped \
--name ddns-go \
jeessy/ddns-go
```

## 3、访问

1. 访问：[http://127.0.0.1:9876](http://127.0.0.1:9876)
2. 初始账号：`admin@example.com`
3. 初始密码 `changeme`

## 4、使用

> 这里只演示阿里云，因为的只在阿里云有域名

#### Ⅰ、获取阿里云 AccessKey

1. 进入页面后，选择阿里云，然后点击 `创建 AccessKey`，会进入 [RAM 访问控制](https://ram.console.aliyun.com/profile/access-keys) 页面

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111017.png)

2. 勾选**我确认知晓云账号 AccessKey 安全风险**，然后点击**继续使用云账号AccessKey**

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111030.png)

3. 选择**创建AccessKey**，同样确认风险

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111041.png)

4. 验证身份后，保存创建的 AccessKey ID 和 AccessKey Secret，否则一旦关闭，只能重新创建

#### Ⅱ、添加解析

1. 拿到 AccessKey ID 和 AccessKey Secret 后，填入 ddns-go 中，TTL 保持自动即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111057.png)

2. IPv4 设置中：
	1. 是否启用：勾选表示启用
	2. 获取 IP 方式：选择**通过接口获取**即可，会通过下面默认的接口获取当前 ip
	3. Domains：想要解析的域名列表，此处我设置的是泛域名
	4. IPv6 选择性启用，因为我有 IPv4 地址，所以这里没设置

```shell
# 通过接口获取
https://myip.ipip.net, https://ddns.oray.com/checkip, https://ip.3322.net, https://4.ipw.cn, https://v4.yinghualuo.cn/bejson
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111126.png)

## 5、通知渠道

#### Ⅰ、Server 酱

1. URL 为：

```shell
https://sctapi.ftqq.com/[SendKey].send?title=域名更新结果：#{ipv4Result}&desp=当前IPv4地址：#{ipv4Addr}；当前域名：#{ipv4Result}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111149.png)

2. 当 ip 变化时，ddns-go 会重新解析域名并发送通知

#### Ⅱ、pushplus

1. URL 为：

```shell
http://www.pushplus.plus/send/
```

2. RequestBody 为：

```json
{     
    "token":"[pushplus_token]",     
    "title":"ddns-go 域名解析",     
    "content":"域名更新结果：#{ipv4Result}\r\n当前IPv4地址：#{ipv4Addr}\r\n当前域名：#{ipv4Result}" 
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111217.png)

3. 当 ip 变化时，ddns-go 会重新解析域名并发送通知

## 6、测试

1. 上面的配置都完毕后，点击保存即可
2. 选择一个域名查询网址，如：https://site.ip138.com/
3. 输入域名进行查询，即可看到解析的 ip 地址：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111238.png)

# 十八、onenav 开源的导航管理工具

## 1、介绍

1. OneNav 是一个基于 PHP + SQLite 开发的简洁、轻量级的书签管理导航系统。它的设计目标是提供一个简洁高效的导航页面，适用于个人或团队使用，方便管理和访问常用网站。
2. OneNav 的主要特点：
	1. 轻量级：使用 PHP 作为后端，无需复杂的配置，直接可用。
	2. 数据库支持：支持 SQLite 和 MySQL，适应不同的使用需求。
	3. 简洁 UI：前端采用简洁美观的设计，用户体验良好。
	4. 支持分类管理：可以对书签进行分类管理，方便查找和使用。
	5. 多用户支持：部分版本支持多用户管理，可用于团队协作。
	6. 开源项目：OneNav 是一个开源项目，可以自由修改和扩展。
3. 适用场景：
	1. 个人导航页：用于管理个人常用的网站链接，提高访问效率。
	2. 公司/团队内部导航：作为团队内部的书签管理工具，方便共享常用资源。
	3. 开发者工具集合：可以整理各种 API 文档、开发工具网站等，提高开发效率。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/onenav/data`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 80:80 \
-v /home/docker/docker/volumes/onenav/data:/data/wwwroot/default/data \
--restart=unless-stopped
--name onenav \
helloz/onenav:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:80/](http://127.0.0.1:80/)
2. 初次访问需注册管理员账号密码

# 十九、

# 二十、

# 二十一、

# 一百、homeassistant 智能家居平台

## 1、介绍

1. Home Assistant 是一个开源的智能家居平台，它允许用户自动化和控制家中的各种设备。这个平台特别注重隐私和本地控制，不依赖云服务，因此非常受隐私意识强的用户欢迎。
2. 核心功能：
3. 设备集成：Home Assistant 支持超过 1000 种不同的设备和服务，包括照明系统（如 Philips Hue）、智能插座、安全摄像头、气候控制设备、媒体播放器（如 Spotify 和 Kodi）以及各种传感器。
4. 自动化：用户可以通过简单的图形界面或 YAML 文件编写自动化规则，使设备根据时间、位置、传感器读数或其他触发条件自动操作。
5. 隐私保护：所有数据都存储在本地，不依赖云服务处理，确保用户数据的隐私和安全。
6. 易用性：提供一个用户友好的网页界面，支持手机和平板电脑访问，使得设备的管理和控制变得简单方便。
7. 社区支持：拥有一个活跃的社区，社区成员不断地开发新的集成和功能，同时提供帮助和支持。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/homeassistant/config`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-v`：指定挂载目录
		1. `-v /etc/localtime:/etc/localtime:ro`：将宿主机的本地时间文件挂载到容器中的相同位置，确保两者的时间一致
		2. `-v /run/dbus:/run/dbus:ro`：允许容器以只读方式访问宿主机的 /run/dbus 目录，从而可以使用 DBus 服务；DBus 是 Linux 中用于进程间通信的系统，许多硬件访问功能，包括蓝牙服务，依赖于 DBus 服务
	3. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。
	5. `--net=host`：使容器使用宿主机的网络；如果不启用此选项，则无法获取路由器信息

```shell
docker run -d \
-e TZ="Asia/Shanghai" \
-v /home/docker/docker/volumes/homeassistant/config:/config \
-v /run/dbus:/run/dbus:ro \
--device=/dev/bus/usb:/dev/bus/usb \
--device=/dev/ttyAMA0:/dev/ttyAMA0 \
--device=/dev/ttyACM0:/dev/ttyACM0 \
--device=/dev/hci0:/dev/hci0 \
--privileged=true \
--restart=unless-stopped \
--net=host \
--name=home-assistant \
homeassistant/home-assistant
```

## 3、访问

1. 默认端口为 `8123`，访问：[http://127.0.0.1:8123](http://127.0.0.1:8123)
2. 初次访问需设定管理员账号密码

## 4、设置 nginx 代理

> 直接配置 nginx 后访问会提示：`400: Bad Request`

1. 先停止容器，然后在挂载目录 `/home/docker/docker/volumes/homeassistant/config` 中找到文件 `configuration.yaml` 并编辑，再末尾加入以下内容，设置信任 ip：
	1. `192.168.31.0/24`：家里的其他设备
	2. `172.17.0.0/16`：docker，比如 nginx 
	3. `127.0.0.1`：本地访问

```shell
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 192.168.31.0/24
    - 172.17.0.0/16
    - 127.0.0.1
```

2. 完整的 `configuration.yaml` 文件

```shell

# Loads default set of integrations. Do not remove.
default_config:

# Load frontend themes from the themes folder
frontend:
  themes: !include_dir_merge_named themes

automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 192.168.31.0/24
    - 172.17.0.0/16
    - 127.0.0.1
```

3. 保存后，重新启动容器，就可以通过 nginx 代理的地址访问了

## 5、连接 Network UPS Tools

1. 编辑 `upsd.conf` 文件

```shell
sudo nano /etc/nut/upsd.conf
```

2. 在文件中找到 `LISTEN` 指令。默认情况下，可只设置为监听本地接口，如 `127.0.0.1` 或 `::1`，将 `LISTEN` 指令修改（或新增）为：

```shell
# ipv4
LISTEN 0.0.0.0 3493
# ipv6
LISTEN :: 3493
```

3. 保存修改后，进入 homeassistant 管理页面，点击设置 -> 设备与服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111608.png)

4. 正常的话，已发现中就会有 Network UPS Tools (NUT)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111622.png)

5. 点击添加，输入完参数后点击提交即可
	1. 主机：`172.17.0.1`
	2. 端口：`3493`
	3. 用户名：ups 的用户名
	4. 密码：ups 的密码

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111640.png)

6. 添加成功后，会显示在设备中

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111736.png)

7. 点击概览，也会显示 ups 的信息

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111705.png)

## 6、集成 hacs

#### Ⅰ、hacs 介绍

1. HACS (Home Assistant Community Store) 是一个为 Home Assistant 提供的第三方集成管理工具，它允许用户轻松安装、更新和管理社区开发的集成、插件、主题和自定义卡片。
2. 通过 HACS，用户可以访问不在官方 Home Assistant 集成目录中的众多额外内容，这些内容通常由独立开发者或者爱好者社区提供。
3. HACS 的主要特点包括：
	1. 易于安装和管理：HACS 提供了一个用户友好的界面，使得安装、更新和浏览社区开发的集成和插件变得简单。
	2. 广泛的可用内容：用户可以通过 HACS 安装各种自定义集成和插件，包括天气插件、设备控制、社交媒体集成等。
	3. 自动更新：HACS 可以自动检测安装的集成和插件的更新，使得维护和更新变得更加便捷。
	4. 社区支持：由于 HACS 是一个社区驱动的项目，用户可以得到社区的支持和指导，同时也能贡献自己的创建。

#### Ⅱ、集成 hacs

1.  下载 hacs 源码：
	1. github 最新版下载：[Releases · hacs/integration](https://github.com/hacs/integration/releases)
	2. 本地  v2.0.1 版下载：[hacs.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2Fhacs.zip)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111816.png)

2. 在挂载目录 `/home/docker/docker/volumes/homeassistant/config` 下再创建 `custom_components` 目录，将下载的文件上传到此目录中：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111831.png)

3. 解压 hacs.zip

```shell
unzip hacs.zip -d hacs/
```

4. 解压完毕后，重启容器，进入 homeassistant 管理页面，点击设置 -> 设备与服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111847.png)

5. 点击添加集成：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111857.png)

6. 搜索 `hacs`，选择后勾选所有选项，然后点击提交：

![|499](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111908.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111918.png)

7. 等待一段时间后，提示需要点击中间的链接跳转到 GitHub 进行验证，复制下面验证码填入 GitHub 进行验证

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111932.png)

8. 验证完成后，刷新一下，左侧出现 HACS 选项，进入即可安装各种插件与设备链接

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108111944.png)

## 7、集成米家

> 需完成上面的集成 hacs

1. 在 hacs 中搜索 `Xiaomi Miot Auto`，进入后点击 download

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108112003.png)

2. 下载完成后，点击设置 -> 小米模块，会提示需要重启容器

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108112017.png)

3. 重新容器后，进入设置 -> 添加集成，搜索 `xiaomi`，选择 `Xiaomi Miot Auto`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108112031.png)

4. 选择账号集成，再选择排除模式，不选择任何设备，点击提交，就可以成功添加

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250108112043.png)
