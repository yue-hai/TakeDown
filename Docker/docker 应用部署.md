# 0、nginx-proxy-manager 基于 Nginx 的反向代理管理工具

> 1. 项目 github：https://github.com/xiaoxinpro/nginx-proxy-manager-zh
> 2. 原项目 github：https://github.com/NginxProxyManager/nginx-proxy-manager
> 3. dockerHub 地址：https://hub.docker.com/r/chishin/nginx-proxy-manager-zh

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
	1. 文件目录：`/vol1/1000/docker/code/nginx-proxy-manager/data`
	2. 证书目录：`/vol1/1000/docker/code/nginx-proxy-manager/letsencrypt`
2. 原镜像是：`jc21/nginx-proxy-manager`，此处使用的是汉化版
3. 使用 docker run 部署：

```shell
docker run -d \
-p 81:81 \
-p 80:80 \
-p 443:443 \
-v /vol1/1000/docker/code/nginx-proxy-manager/data:/data \
-v /vol1/1000/docker/code/nginx-proxy-manager/letsencrypt:/etc/letsencrypt \
--network yuehai-net \
--restart=unless-stopped \
--name=nginx-proxy-manager-zh \
chishin/nginx-proxy-manager-zh:latest
```

4. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 nginx-proxy-manager-zh 的服务
    nginx-proxy-manager-zh:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: chishin/nginx-proxy-manager-zh:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: nginx-proxy-manager-zh
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Nginx Proxy Manager 的 Web 管理界面
            - "81:81"
            # 用于代理 HTTP 流量
            - "80:80"
            # 用于代理 HTTPS 流量
            - "443:443"
        # 定义数据卷挂载规则
        volumes:
            # 文件目录
            - /vol1/1000/docker/code/nginx-proxy-manager/data:/data
            # 证书目录
            - /vol1/1000/docker/code/nginx-proxy-manager/letsencrypt:/etc/letsencrypt
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

## 3、访问

1. 访问：[http://127.0.0.1:81](http://127.0.0.1:81)
2. 初始管理员账号：`admin@example.com`
3. 初始管理员密码：`changeme`

## 4、申请 ssl 证书

> 这里只演示阿里云，因为我只在阿里云有域名

### ①、获取阿里云 AccessKey

> 此处获取 AccessKey 的方式与 ddns-go 中基本相同，只是要多设置一些权限

1. 申请并配置阿里云 DNS 访问密钥：会进入 [RAM 访问控制](https://ram.console.aliyun.com/profile/access-keys) 页面；点击左侧的授权，然后点击新增授权

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108083754.png)

2. 在右侧弹窗中：
	1. 授权主体勾选 **RAM 用户**类型的角色
	2. 权限策略中搜索 `AliyunDNSFullAccess`，然后勾选（我这里已经有了所以不能勾选）
	3. 点击确认新增授权

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108083825.png)

3. 权限设置完成后，进入 [RAM 访问控制](https://ram.console.aliyun.com/profile/access-keys) 页面：
	1. 若是其他应用（比如 ddns-go）使用时已经创建过了，直接使用之前创建的 AccessKey ID 和 AccessKey Secret 即可
	2. 若是没有，继续下面的步骤进行创建：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108083857.png)

4. 勾选**我确认知晓云账号 AccessKey 安全风险**，然后点击**继续使用云账号AccessKey**

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108083922.png)

5. 选择**创建AccessKey**，同样确认风险

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108083957.png)

6. 验证身份后，记得保存 AccessKey ID 和 AccessKey Secret，否则一旦关闭页面，只能重新创建

### ②、申请 ssl 证书

1. 进入 nginx-proxy-manager 页面后，点击 **SSL 证书**，然后点击**添加 SSL 证书**，再选择 **Let's Encrypt**

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084028.png)

2. 在添加 Let's Encrypt 证书弹窗中：
	1. 域名可以设置泛域名，如：`*.yuehai.fun`
	2. Let's Encrypt 处填写自己的邮箱
	3. 使用 DNS 认证：勾选，一般家用宽带的 80 和 443 端口都是被封禁的，所以只能使用 DNS 认证
	4. DNS 提供者：选择自己的域名提供商、DNS 解析商，我的是阿里云，所以这里选择阿里云
	5. 证书内容：填入上一节创建的 AccessKey ID 和 AccessKey Secret
	6. 等待时间(秒)：120 ~ 240 即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084109.png)

3. 点击保存，等待几分钟即可

## 5、设置代理服务，使用 bridge 网关的方式

1. 如果需要代理的服务和 nginx 都在同一台服务上，且需要代理的服务是使用 docker 部署的，则使用以下命令获取 docker 中指向宿主机的 ip：

```shell
ip addr show docker0
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084146.png)

2. 点击主机 -> 代理服务 -> 添加代理服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084201.png)

3. 比如我给部署的迅雷设置一个代理：
	1. 域名：外部访问时的域名；因为是泛解析的域名，所以三级域名可以随便设置，指向迅雷即可
	2. 协议：选择部署的迅雷原本的协议，即 http
	3. 转发主机/IP：上面获取的 `172.17.0.1`
	4. 转发端口：部署的迅雷的端口，迅雷默认是 `2345`
	5. 缓存资源、阻止常见漏洞、支持 WebSockets 一般都开启即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084347.png)

4. 点击 SSL，选择上面申请的证书

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084403.png)

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

## 7、设置代理静态资源

> 1. 代理的资源是 vue3 打包后的静态资源
> 2. 本次代理域名是 ip + 路径，因为阿里云没有备案不能被解析为域名

1. nginx 挂载的路径是：`/home/docker/docker/volumes/nginx-proxy-manager/data:/data`，我们需要将静态资源的目录放在 `/data` 下
2. 在 `/data` 下创建目录： `/web/oneNav-theme-yuehai/`，将 vue 打包后的文件放入其中

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250218123840.png)

3. 点击主机 -> 代理服务 -> 添加代理服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084201.png)

4. 设置一个代理：
	1. 域名：本服务器的 ip
	2. 协议：http；没有域名，无法设置证书，也就没有 https
	3. 转发主机/IP：本服务器的 ip
	4. 转发端口：80，如果不可用，自定义其他的端口也可以
	5. 缓存资源、阻止常见漏洞、支持 WebSockets 不要开启

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250220162617.png)

5. 点击自定义位置：
	1. 定义位置：`/oneNav`，根据自定需求更改
	2. 协议：http
	3. 转发主机/IP：`127.0.0.1`，因为是读取本地资源
	4. 转发端口：`80`
6. 然后点击定义位置后的齿轮按钮，在输入框中输入以下内容：
	1. `location /oneNav {}`：匹配访问路径 `/oneNav` 的请求
	2. `alias /data/web/oneNav-theme-yuehai;`：alias 设定了路径映射，表示 当请求 `/oneNav/xxx` 时，Nginx 实际访问 `/data/web/oneNav-theme-yuehai/xxx`
	3. `index index.html;`：当访问 `/oneNav/` 目录时，默认返回 `index.html`

```nginx
location /oneNav {
    alias /data/web/oneNav-theme-yuehai;
    index index.html;
}
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250218123921.png)

7. 设置完毕后，点击保存即可
8. 最后访问：http://127.0.0.1/oneNav

## 8、代理权限设置

1. 点击通信规则 -> 添加通信规则

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084713.png)

2. 详情页面：
	1. 名字：这个通信规则的名字，仅作为标识符使用
	2. 满足任何要求：规则页面中满足任意即可访问
	3. 授权访问主机：暂不知作用

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084741.png)

3. 授权用户页面：
	1. 账号：启用时需要输入的账号
	2. 密码：启用时需要输入的密码
	3. 可以设置多个，有一个输入正确了即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084759.png)

4. 规则页面：
	1. allow：**允许**；设置为 `all` 表示允许所有 ip，单独设置则为白名单
	2. deny：**禁止**； 设置为 `all` 表示禁止所有 ip，单独设置则为黑名单
	3. 可以设置多个，规则将按照它们定义的顺序执行

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084825.png)

5. 设置完成后，点击保存即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084841.png)

6. 进入代理服务页面，选择一个代理设置

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084855.png)

7. 点击编辑，通信规则选择刚刚设置的规则名称，然后点击保存即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084915.png)

8. 访问上面设置了通信规则的代理服务地址，浏览器上方会弹出账号密码输入框，输入上面在授权用户页面设置的账号密码即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084933.png)

## 10、设置代理服务，使用自定义网络的方式

1. 如果 docker 中已经定义了网络 `yuehai-net`，并且 nginx 容器和需要代理的容器创建时已经指定了使用该网络 `--network yuehai-net`，那么就可以使用自定义网络的方式进行代理；当然名字不是固定的，自定义即可

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617092724.png)

1. 同样是点击主机 -> 代理服务 -> 添加代理服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108084201.png)

1. 其他设置都和上面相同，不同的地方：
	1. 转发主机/IP：使用容器的名称，比如：xunlei
	2. 转发端口：使用容器的内部端口，比如迅雷的内部端口是 2345

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617092837.png)


# 1、docker 可视化 portainer-ce

> 1. 项目 github：https://github.com/eysp/portainer-ce
> 2. 原项目 github：https://github.com/portainer/portainer
> 3. dockerHub 地址：https://hub.docker.com/r/6053537/portainer-ce

## 1、介绍

1. Portainer 是一款轻量级的应用，它提供了图形化界面，用于方便地管理 Docker 环境，包括单机环境和集群环境
2. 这里使用的是国内热心大佬上传到 Docker Hub 的二次编译汉化版 Portainer，安装好之后直接使用
3. 弊端就是跟不上原版 Portainer 的更新节奏。虽说如此，它一般和最新版 Portainer 差距不大，所以使用起来几乎没什么差别。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/code/portainer-ce/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 9000:9000 \
-v /vol1/1000/docker/code/portainer-ce/data:/data \
-v /var/run/docker.sock:/var/run/docker.sock \
--restart=unless-stopped \
--name="portainer-ce" \
6053537/portainer-ce:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 portainer-ce 的服务
    portainer-ce:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: 6053537/portainer-ce:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: portainer-ce
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Portainer 的 Web 管理界面端口
            - "9000:9000"
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 数据目录
            - /vol1/1000/docker/code/portainer-ce/data:/data
            # 将主机的 Docker Socket 挂载到容器，这是 Portainer 能够管理 Docker 的核心，也意味着此容器拥有很高的主机权限
            - /var/run/docker.sock:/var/run/docker.sock
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络，以便它可以识别和管理网络内的其他容器
            - yuehai-net

# 在文件末尾定义此 Compose 文件中使用的所有网络
networks:
    # 定义一个名为 yuehai-net 的网络配置
    yuehai-net:
        # 将此网络声明为外部网络
        # external: true 的意思是：不要创建这个网络，而是去使用一个已经存在的、名字完全相同的网络
        external: true
```
## 3、访问及设置

1. 访问：[http://127.0.0.1:9000](http://127.0.0.1:9000)
2. 初次访问需设定管理员账号密码


# 2、chromium 谷歌开源的浏览器核心项目

> 1. 项目 github：https://github.com/linuxserver/docker-chromium
> 2. dockerHub 地址：https://hub.docker.com/r/linuxserver/chromium

## 1、介绍

1. linuxserver/chromium 是由 linuxserver.io 团队维护的一个 Docker 镜像，它提供了一个在容器内运行的 Chromium 浏览器实例。Chromium 是 Google Chrome 浏览器的开源基础
2. 这个镜像的主要特点和用途是：
	1. 远程访问浏览器：它通常内置了一个 Web 服务器，允许通过浏览器访问另一个浏览器界面（通常是通过 KasmVNC 或类似的 Web VNC/RDP 技术）。这对于在没有图形界面的服务器上运行浏览器，或者需要一个隔离的、干净的浏览器环境非常有用
	2. 安全性/隔离性：在容器中运行浏览器可以将其与主机系统隔离开，增强安全性
	3. 自动化测试：也可用于浏览器自动化测试场景
	4. 易于配置：linuxserver.io 的镜像通常提供标准的 PUID、PGID 和 TZ 等环境变量，方便进行权限和时区配置

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/tool/chromium/config`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 3000:3000 \
-p 3001:3001 \
-e PUID=1000 \
-e PGID=1000 \
-e TZ=Asia/Shanghai \
-e HTTP_PROXY=http://clash:7890 \
-e HTTPS_PROXY=http://clash:7890 \
-e NO_PROXY=localhost,127.0.0.1,172.17.0.0/16,192.168.0.0/16,10.0.0.0/8,.local \
-v /vol1/1000/docker/tool/chromium/config:/config \
--shm-size="1gb" \
--network yuehai-net \
--restart unless-stopped \
--name=chromium \
linuxserver/chromium:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 chromium 的服务
    chromium:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: linuxserver/chromium:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: chromium
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Chromium Web UI HTTP 端口
            - "3000:3000"
            # Chromium Web UI HTTPS 端口 (可选)
            - "3001:3001"
        # 定义环境变量
        environment:
            - PUID=1000
            - PGID=1000
            - TZ=Asia/Shanghai
            # 设置 HTTP 代理端口
            - HTTP_PROXY=http://clash:7890
            # 设置 HTTPS 代理端口
            - HTTPS_PROXY=http://clash:7890
            # 设置不进行代理的 ip
            - NO_PROXY=localhost,127.0.0.1,172.17.0.0/16,192.168.0.0/16,10.0.0.0/8,.local,172.20.0.0/16
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/chromium/config:/config
        shm_size: '1gb'
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

## 3、访问

1. 访问：[http://127.0.0.1:3000](http://127.0.0.1:3000)

## 4、下载使用中文字库

1. 进入容器命令行，执行下面的命令：

```shell
apt-get update && apt-get install -y fonts-wqy-zenhei fonts-arphic-ukai
```

1. 进入 linuxserver/chromium web 端，访问 `chrome://flags`
2. 搜索 Reduce Accept-Language
3. 设置为 Enabled 后重启

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617093427.png)


# 3、clash

> 1. 项目 github：https://github.com/ShangjinTang/clash-core
> 2. dockerHub 地址：https://hub.docker.com/r/dreamacro/clash

## 1、介绍

1. dreamacro/clash 是一个流行的代理规则引擎的 Docker 镜像。Clash 本身是一个基于规则的跨平台代理客户端，支持多种代理协议（如 Shadowsocks, Vmess, Trojan, Snell 等），并且可以通过自定义规则实现灵活的分流策略
2. 使用 dreamacro/clash Docker 镜像，可以方便地在服务器或任何支持 Docker 的环境中部署 Clash 代理服务。它通常用于：
	1. 网络访问控制：根据规则决定哪些流量走代理，哪些直连
	2. 隐私保护：通过代理隐藏您的真实 IP 地址
	3. 访问特定资源：绕过地理限制或网络审查
	4. 这个镜像是 Clash 官方或社区维护的，非常适合需要一个稳定、可配置代理服务的场景

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/tool/chromium/config`，并配置为下面的格式

```yaml
# config.yaml
port: 7890       # HTTP 代理端口，原 7890
socks-port: 7891 # SOCKS5 代理端口，原 7891
redir-port: 7892 # 透明代理端口 (如果需要)
mixed-port: 7893 # 混合代理端口 (如果需要)

allow-lan: true      # 关键：允许来自局域网的连接
bind-address: '*'    # 关键：监听所有网络接口，0.0.0.0 也可以

# ... 其他配置，例如 proxies, proxy-groups, rules 等 ...

# (可选) 外部控制 UI (Clash Dashboard)
external-controller: '0.0.0.0:9090' # 监听所有接口，允许从外部访问 Dashboard，原 9090
secret: '' # (可选) 设置访问密码
```

2. 使用 docker run 部署：

```shell
docker run -d \
-p 9090:9090 \
-p 7890:7890 \
-p 7891:7891 \
-v /vol1/1000/docker/vpn/clash/config/config.yaml:/root/.config/clash/config.yaml \
--network yuehai-net \
--restart=unless-stopped \
--name clash \
dreamacro/clash:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 clash 的服务
    clash:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: dreamacro/clash:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: clash
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # web ui API 端口，原 9090
            - "9090:9090"
            # HTTP 代理端口，原 7890
            - "7890:7890"
            # SOCKS5 代理端口，原 7891
            - "7891:7891"
        # 定义数据卷挂载规则
        volumes:
            # 配置文件
            - /vol1/1000/docker/vpn/clash/config/config.yaml:/root/.config/clash/config.yaml
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

## 3、访问

1. 没有 web 端口，需通过 clash-yacd 或其他 clash 前端访问


# 4、clash-yacd

> 1. 项目 github：https://github.com/haishanh/yacd
> 2. dockerHub 地址：https://hub.docker.com/r/haishanh/yacd

## 1、介绍

1. haishanh/yacd 是一个为 Clash 提供的网页用户界面（Web UI）的 Docker 镜像。YACD 代表  Yet Another Clash Dashboard （又一个 Clash 控制面板）
2. 它的主要作用是提供一个图形化的界面，可以更直观地：
	1. 查看 Clash 的运行状态：包括当前的代理服务器、延迟、流量等信息
	2. 切换代理节点和策略组：无需修改配置文件即可快速更换代理服务器
	3. 查看连接信息：了解哪些应用或设备正在通过 Clash 联网
	4. 配置 Clash：在某些版本中，可能支持部分配置的修改

## 2、docker 部署

1. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
--network yuehai-net \
--restart=unless-stopped
--name clash-yacd \
haishanh/yacd:latest
```

2. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 clash-yacd 的服务
    clash-yacd:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: haishanh/yacd:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: clash-yacd
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # web 访问端口
            - "80:80"
        # 定义数据卷挂载规则
        volumes:
            # 配置文件
            - /vol1/1000/docker/vpn/clash/config/config.yaml:/root/.config/clash/config.yaml
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

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 填入 clash 的 api 地址即可


# 5、ddns-go 一款轻量级、开源的动态域名解析服务

> 1. 项目 github：https://github.com/jeessy2/ddns-go
> 2. dockerHub 地址：https://hub.docker.com/r/jeessy/ddns-go

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
	2. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	3. `-p`：指定端口映射
	4. `-v`：指定挂载目录
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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111017.png)

2. 勾选**我确认知晓云账号 AccessKey 安全风险**，然后点击**继续使用云账号AccessKey**

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111030.png)

3. 选择**创建AccessKey**，同样确认风险

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111041.png)

4. 验证身份后，保存创建的 AccessKey ID 和 AccessKey Secret，否则一旦关闭，只能重新创建

#### Ⅱ、添加解析

1. 拿到 AccessKey ID 和 AccessKey Secret 后，填入 ddns-go 中，TTL 保持自动即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111057.png)

2. IPv4 设置中：
	1. 是否启用：勾选表示启用
	2. 获取 IP 方式：选择**通过接口获取**即可，会通过下面默认的接口获取当前 ip
	3. Domains：想要解析的域名列表，此处我设置的是泛域名
	4. IPv6 选择性启用，因为我有 IPv4 地址，所以这里没设置

```shell
# 通过接口获取
https://myip.ipip.net, https://ddns.oray.com/checkip, https://ip.3322.net, https://4.ipw.cn, https://v4.yinghualuo.cn/bejson
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111126.png)

## 5、通知渠道

#### Ⅰ、Server 酱

1. URL 为：

```shell
https://sctapi.ftqq.com/[SendKey].send?title=域名更新结果：#{ipv4Result}&desp=当前IPv4地址：#{ipv4Addr}；当前域名：#{ipv4Result}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111149.png)

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111217.png)

3. 当 ip 变化时，ddns-go 会重新解析域名并发送通知


# 100、OpenList 网盘整合挂载工具

> 1. 项目 github：https://github.com/OpenListTeam/OpenList
> 2. dockerHub 地址：https://hub.docker.com/r/openlistteam/openlist
> 3. 官网：https://oplist.org/zh/guide/
> 4. 操作系统版本为：Ubuntu 22.04.3 LTS

## 1、介绍

1. OpenListTeam/OpenList 是 OpenList 的官方 Docker 镜像，OpenList 是 AList 的一个分支版本
2. OpenList 支持多种存储的文件列表程序，它允许将各种云存储、对象存储、WebDAV 甚至本地目录统一管理起来，并通过一个清爽的网页界面进行浏览、预览、下载甚至上传（取决于存储后端支持）
3. 它的主要特点包括：
	1. 广泛的存储支持：支持阿里云盘、OneDrive、Google Drive、夸克网盘、百度网盘、S3、FTP、SFTP 等数十种国内外流行的存储服务
	2. WebDAV 服务：可以将挂载的所有存储通过 WebDAV 协议暴露出来，方便其他应用（如播放器、阅读器）直接访问
	3. 在线预览：支持视频、音频、文档、图片、PDF 等多种格式的在线预览
	4. 美观的界面：提供现代化的 Web 用户界面，支持暗黑模式和自定义
	5. 灵活的权限控制：可以设置不同路径的访问权限

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/file/file-management/openlist/data`
	2. 宿主机挂载目录 1：`/vol1/1000/固态盘`
	3. 宿主机挂载目录 2：`/vol2/1000/raid组`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 5244:5244  \
-e PUID=0  \
-e PGID=0  \
-e UMASK=022  \
-v /vol1/1000/docker/file/file-management/openlist/data:/opt/openlist/data \
-v /vol1/1000:/vol1/1000 \
-v /vol2/1000:/vol2/1000 \
--privileged=true \
--network yuehai-net \
--restart=unless-stopped  \
--name=openlist  \
openlistteam/openlist:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 openlist 的服务
    openlist:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: openlistteam/openlist:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: openlist
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 启用特权模式，赋予容器几乎所有主机的 root 能力（请谨慎使用，仅在必要时开启）
        privileged: true
        # 定义端口映射规则
        ports:
            # openlist 的 Web 访问端口
            - "5244:5244"
        # 定义环境变量
        environment:
            # 设置容器内运行 openlist 进程的用户 ID (0 代表 root)
            - PUID=0
            # 设置容器内运行 openlist 进程的用户组 ID (0 代表 root)
            - PGID=0
            # 设置创建文件的默认权限掩码
            - UMASK=022
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/file/file-management/openlist/data:/opt/openlist/data
            # 将主机的 /vol1/1000/固态盘 目录挂载到容器的 /vol1/1000/固态盘 目录，以便 openlist 可以访问和管理该路径下的文件
            - /vol1/1000:/vol1/1000
            # 将主机的 /vol2/1000/raid组 目录挂载到容器的 /vol2/1000/raid组 目录，以便 openlist 可以访问和管理该路径下的文件
            - /vol2/1000:/vol2/1000
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

## 3、访问

1. 部署成功后，随机生成一个密码：

```shell
docker exec -it openlist ./openlist admin random
```

2. 手动设置一个密码，`NEW_PASSWORD` 是指需要设置的密码：

```shell
docker exec -it openlist ./openlist admin set NEW_PASSWORD
```

3. 访问：`http://127.0.0.1:5244`，进入主页面；输入账号 `admin` 以及刚才设置的密码进行登录
4. 点击管理可进行网盘的设置等，具体查看文档

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108091446.png)

## 4、nginx 代理配置

1. 代理配置不变，高级中自定义 Nginx 配置填入以下内容，注意修改转发地址：

```nginx
# 定义一个 location 块，匹配所有进入的请求 (/)
location / {
  # 关键：将请求代理到指定服务
  # proxy_pass 指令指定了后端服务器的地址和端口
  # 所有匹配此 location 块的请求都将被转发到 http://openlist:5244
  proxy_pass http://openlist:5244;
  
  # 设置 HTTP 头部 X-Forwarded-For，包含了客户端的原始 IP 地址以及代理服务器的 IP 地址列表
  # $proxy_add_x_forwarded_for 变量会自动将 $remote_addr（直接连接到 Nginx 的客户端 IP）附加到已有的 X-Forwarded-For 头部（如果存在）
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  # 设置 HTTP 头部 X-Forwarded-Proto，告诉后端应用客户端最初是使用 HTTP 还是 HTTPS 协议访问的
  # $scheme 变量的值是 http 或 https
  proxy_set_header X-Forwarded-Proto $scheme;
  # 设置 HTTP 头部 Host，将原始请求中的 Host 头部传递给后端服务器
  # $http_host 变量包含了客户端请求中的 Host 头部信息
  proxy_set_header Host $http_host;
  # 设置 HTTP 头部 X-Real-IP，传递了直接连接到 Nginx 的客户端的真实 IP 地址
  # $remote_addr 变量的值是直接连接到 Nginx 的客户端的 IP 地址
  proxy_set_header X-Real-IP $remote_addr;
  # 设置 HTTP 头部 Range，用于支持部分内容请求，例如视频拖动播放或断点续传
  # $http_range 变量包含了客户端请求中的 Range 头部信息
  proxy_set_header Range $http_range;
  # 设置 HTTP 头部 If-Range，与 Range 头部配合使用，用于条件性的部分内容请求
  # $http_if_range 变量包含了客户端请求中的 If-Range 头部信息
  proxy_set_header If-Range $http_if_range;

  # 关闭代理重定向处理，off 表示 Nginx 不会修改后端服务器返回的 Location 和 Refresh 头部中的 URL
  # 这通常在后端应用自己能正确处理重定向 URL 时使用
  proxy_redirect off;
  # 设置客户端请求体的最大允许大小
  # openlist 官方文档推荐设置为 20000m (即 20000MB 或约 19.5GB)，以支持大文件上传
  # 如果上传的文件超过此大小，Nginx 会返回 "413 Request Entity Too Large" 错误
  client_max_body_size 20000m;

  # --- 以下是针对 WebSocket 的可选配置 ---
  # 如果 openlist 使用 WebSockets (例如某些实时功能)，
  # 并且 NPM 的 "支持 WebSockets" 开关没有自动处理好，可以手动添加：

  # 设置代理使用的 HTTP 版本为 1.1
  # WebSocket 协议需要 HTTP/1.1 或更高版本
  # proxy_http_version 1.1;

  # 设置 HTTP 头部 Upgrade
  # 这个头部用于请求协议升级，例如从 HTTP 升级到 WebSocket
  # $http_upgrade 变量包含了客户端请求中的 Upgrade 头部信息
  # proxy_set_header Upgrade $http_upgrade;

  # 设置 HTTP 头部 Connection
  # 当进行协议升级时，Connection 头部通常设置为 "upgrade"
  # 这告诉服务器连接将被用于不同的协议
  # proxy_set_header Connection "upgrade";
}
```

## 5、AList-desktop ubuntu gui 桌面版的安装

> 1. 一开始我以为桌面版有单独的控制面板，单独的挂载、管理方式，结果只是一个启动按钮
> 2. 不如直接安装 docker 版

1. 桌面版需要购买，50元，请在 AList-desktop gui 桌面版官网选择购买
2. 在官网下载对应的 linux 版本到目录，比如我放在了：`/home/yan/apply/file/alist-desktop/` 目录下，或点击此处下载：[alist-desktop_3.38.0_amd64.deb](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Falist-desktop_3.38.0_amd64.deb)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108091543.png)

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

## 6、alist-desktop gui 桌面版安装后，点击桌面图标没反应

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

> 1. [libssl.so.1.1](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Flibssl.so.1.1)
> 2. [libcrypto.so.1.1](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Flibcrypto.so.1.1)

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

> [openssl-1.1.1g.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Fopenssl-1.1.1g.tar.gz)

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


# 101、TaoSync （桃桃的自动同步工具）基于 OpenList 的网盘同步工具

> 1. 项目 github：https://github.com/dr34m-cn/taosync
> 2. dockerHub 地址：https://hub.docker.com/r/dr34m/tao-sync

## 1、介绍

1. 同步备份：
	1. 把本地文件备份到多个网盘或 FTP 之类的存储，或者在多个网盘之间同步文件等；
	2. 可以定时扫描指定目录下文件差异，让目标目录与源目录相同（全同步模式）；或仅新增存在于源目录，却不存在于目标目录的文件（仅新增模式）
2. 定时下载：可以设置一次性任务（cron方式设置年月日时分秒，将在指定时间执行一次），可在闲时自动从特定网盘下载文件到本地

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/file/file-management/tao-sync/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 8023:8023 \
-v /vol1/1000/docker/file/file-management/tao-sync/data:/app/data \
--network yuehai-net \
--restart=unless-stopped \
--name=tao-sync \
dr34m/tao-sync:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 tao-sync 的服务
    tao-sync:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: dr34m/tao-sync:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: tao-sync
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # TaoSync 的 Web 访问或 API 端口
            - "8023:8023"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/file/file-management/tao-sync/data:/app/data
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

## 3、访问

1. 部署成功后，会随机生成一个密码，在日志中查看：

```shell
docker logs taoSync
```

1. 访问：[http://127.0.0.1:8023](http://127.0.0.1:8023)
2. 进入主页面，输入账号 `admin` 以及刚才查看的密码进行登录
3. 登录成功后，点击系统设置，通过刚才查看的密码，修改新密码

# 102、qBittorrent BitTorrent 客户端

> 1. 项目 github：https://github.com/linuxserver/docker-qbittorrent
> 2. dockerHub 地址：https://hub.docker.com/r/linuxserver/qbittorrent

## 1、介绍

1. qBittorrent 是一个开源的、跨平台的 BitTorrent 客户端，支持 Web UI
2. 具有图形用户界面（GUI）和强大的功能，如种子管理、搜索引擎、RSS 支持和带宽管理等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/file/file-management/qbittorrent/config`
	2. 下载目录：`/vol1/1000/docker/file/file-management/qbittorrent/downloads`
2. 使用 docker run 部署：

```shell
docker run -d \
-e TZ=Asia/Shanghai \
-e WEBUI_PORT=8081 \
-p 8081:8081 \
-p 6881:6881 \
-p 6881:6881/udp \
-v /vol1/1000/docker/file/file-management/qbittorrent/config:/config \
-v /vol1/1000/docker/file/file-management/qbittorrent/downloads:/downloads \
--network yuehai-net \
--restart unless-stopped \
--name=qbittorrent \
linuxserver/qbittorrent
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 qbittorrent 的服务
    qbittorrent:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: linuxserver/qbittorrent:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: qbittorrent
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则 (格式：主机端口:容器端口)
        ports:
            # qBittorrent Web UI 端口，由 WEBUI_PORT 环境变量指定
            - "8081:8081"
            # 将主机的 41013 端口映射到容器的 6881 端口 (BT 传入连接 TCP 端口)
            - "6881:6881"
            # 将主机的 41013 端口映射到容器的 6881 端口 (BT 传入连接 UDP 端口)
            - "6881:6881/udp"
        # 定义环境变量
        environment:
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
            # 指定 qBittorrent Web UI 使用的端口（需要与 ports 中的映射一致）
            - WEBUI_PORT=8081
        # 定义数据卷挂载规则 (格式：主机路径:容器路径)
        volumes:
            # 数据目录
            - /vol1/1000/docker/file/file-management/qbittorrent/config:/config
            # 下载目录
            - /vol1/1000/docker/file/file-management/qbittorrent/downloads:/downloads
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

## 3、访问

1. 部署成功后，会随机生成一个密码，在日志中查看：

```shell
docker logs qbittorrent
```

2. 访问：[http://127.0.0.1:8081](http://127.0.0.1:8081)，进入主页面，输入账号 admin 以及刚才查看的密码进行登录
3. 登录成功后，点击工具 -> 选项 -> WebUI，通过刚才查看的密码，修改新密码

## 4、使用 nginx 代理

1. 如果 nginx 和 qbittorrent 加入了同一个 docker 网络，那么代理起来会方便很多
2. 填入 qbittorrent 的容器名和端口号即可

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617095408.png)

## 5、使用 nginx 代理 2

1. 确保启动参数无误，尤其是配置文件的目录，必须是 qbittorrent 的父级目录，不可以到 qbittorrent 这一层
2. 如果是在外网通过 IP 访问内网服务器，则需查看 `qbittorrent.conf` 中，是否设置了 `WebUI\HostHeaderValidation=true` 参数，如有，请改为 false
3. 如果是在外网通过域名访问内网服务器，则第二条同样适用；但安全起见，建议改为 true 并把值设置为域名
4. 如果并未配置 HTTPS 证书，或未安装相关组件，则需查看 `qbittorrent.conf` 中，是否设置了 `WebUI\HTTPS\Enabled=ture` 参数，如有，请改为 false
5. 在 nginx-proxy-manager 中设置代理，然后点击高级，设置以下内容：

```nginx
# 定义一个 location 块，匹配所有进入的请求 (/)
location / {
	# 关键：将请求代理到指定服务
	# proxy_pass 指令指定了后端服务器的地址和端口
	# 所有匹配此 location 块的请求都将被转发到 http://172.17.0.1:8081
	proxy_pass http://172.17.0.1:8081/;
	
	# 设置 HTTP 头部 Host，将原始请求中的 Host 头部传递给后端服务器
	# $http_host 变量包含了客户端请求中的 Host 头部信息
	proxy_set_header Host $http_host;
	# 设置 HTTP 头部 X-Forwarded-For，包含了客户端的原始 IP 地址以及代理服务器的 IP 地址列表
	# $proxy_add_x_forwarded_for 变量会自动将 $remote_addr（直接连接到 Nginx 的客户端 IP）附加到已有的 X-Forwarded-For 头部（如果存在）
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	# 设置 HTTP 头部 X-Forwarded-Proto，告诉后端应用客户端最初是使用 HTTP 还是 HTTPS 协议访问的
	# $scheme 变量的值是 http 或 https
	proxy_set_header X-Forwarded-Proto $scheme;
	proxy_set_header X-Forwarded-Host $http_host;
	
	# 设置 HTTP 头部 X-Real-IP，传递了直接连接到 Nginx 的客户端的真实 IP 地址
	# $remote_addr 变量的值是直接连接到 Nginx 的客户端的 IP 地址
	proxy_set_header X-Real-IP $remote_addr;
	# 设置 HTTP 头部 Range，用于支持部分内容请求，例如视频拖动播放或断点续传
	# $http_range 变量包含了客户端请求中的 Range 头部信息
	proxy_set_header Range $http_range;
	# 设置 HTTP 头部 If-Range，与 Range 头部配合使用，用于条件性的部分内容请求
	# $http_if_range 变量包含了客户端请求中的 If-Range 头部信息
	proxy_set_header If-Range $http_if_range;

	# 从 4.2.2 版本起，若在 qBittorrent 内部设置了 HTTPS，则不需要设置该参数。否则，必须设置该参数用以保证 Cookie 的安全性
	proxy_cookie_path / "/; Secure";
	# 可选，设置后可一次性添加 100M 的种子
	# client_max_body_size 100M;
	
	# proxy_http_version 1.1;
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

## 6、使用 nginx 代理方式 3

1. 如果经过上面的方式依然无法访问，访问时 qbittorrent 日志可能提示：

```shell
(W) 2024-12-25T14:01:42 - WebUI: 请求 Header 中 Referer 与 XFH/Host 不匹配！来源 IP: '::ffff:172.17.0.1'。Referer: 'https://qbittorrent.yuehai.fun:8080/'。XFH/Host: 'qbittorrent.yuehai.fun'
```

2. 我找了找，没找到解决办法，这里再提供另一个解决办法
3. 上面 4 中的配置不再需要，nginx 中仅配置代理即可

![|474](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108100020.png)

4. 本地进入 qbittorrent 的管理页，点击设置 -> WebUI，勾选**对 IP 子网白名单中的客户端跳过身份验证**，并设置如下内容：
	1. 最重要的是 `172.17.0.0/16` 这一条，对 docker 应用的 ip 设置白名单
	2. 下面的两条是对内网访问的放行，仅方便内网不同电脑的调用，可以不设置

```shell
172.17.0.0/16
192.168.31.0/24
127.0.0.1/32
```

5. 向下翻，取消勾选**启用跨站请求伪造 (CSRF) 保护**

![|550](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108100058.png)

6. 点击保存即可


# 103、迅雷群晖提取版

> 1. 项目 github：https://github.com/cnk3x/xunlei
> 2. dockerHub 地址：https://hub.docker.com/r/cnk3x/xunlei

## 1、介绍

1. 该项目提取自群晖平台的迅雷下载套件，用于其他 Linux 机器上的迅雷远程下载服务
2. 需要已经安装完毕 docker，如果没有，请先进行 docker 的安装

## 2、docker 部署


1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/file/file-management/xunlei/data`
	2. 下载目录：`/vol1/1000/docker/file/file-management/xunlei/downloads`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 2345:2345 \
-v /vol1/1000/docker/file/file-management/xunlei/data:/xunlei/data \
-v /vol1/1000/docker/file/file-management/xunlei/downloads:/xunlei/downloads \
--privileged=true \
--network yuehai-net \
--restart=unless-stopped \
--name=xunlei \
cnk3x/xunlei:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 xunlei 的服务
    xunlei:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: cnk3x/xunlei:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: xunlei
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 启用特权模式，赋予容器几乎所有主机的 root 能力（迅雷可能需要此权限进行 P2P 连接或文件操作）
        privileged: true
        # 定义端口映射规则
        ports:
            # 迅雷 Web UI 端口
            - "2345:2345"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/file/file-management/xunlei/data:/xunlei/data
            # 下载目录
            - /vol1/1000/docker/file/file-management/xunlei/downloads:/xunlei/downloads
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

## 3、访问

1. 访问迅雷迅雷群晖提取版网页： [http://127.0.0.1:2345](http://127.0.0.1:2345)
2. 扫码或使用账号密码登录

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108091117.png)

3. 输入内测邀请码（经过测试 <font color="#ff0000">迅雷牛通</font> 内测码有效）

![|425](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108091129.png)

4. 登录完成后，点击新建任务，就可以添加连接进行下载

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108091142.png)


# 104、syncthing 中心化的、点对点的文件同步应用

> 1. 项目 github：https://github.com/syncthing/syncthing
> 2. dockerHub 地址：https://hub.docker.com/r/syncthing/syncthing

## 1、介绍

1. syncthing/syncthing 是一个流行的开源文件同步工具的 Docker 镜像。Syncthing 本身是一个去中心化的、点对点 (P2P) 的文件同步应用程序，它允许在多个设备之间安全地同步文件和文件夹，而无需依赖中央服务器
2. 使用 syncthing 镜像，可以方便地在服务器、NAS 设备或任何支持 Docker 的环境中部署 Syncthing 服务。它通常用于：
	1. 私有文件同步：在个人电脑、笔记本、服务器和移动设备之间保持文件夹的最新状态
	2. 数据备份的替代方案：作为一种实时或近乎实时的方式，将重要数据同步到另一台设备上
	3. 团队协作 (小型)：在小团队成员之间共享和同步项目文件，无需第三方云存储
	4. 取代云存储服务：对于希望完全掌控自己数据、不依赖商业云服务的用户，提供一个私有的同步解决方案
	5. 这个镜像是 Syncthing 官方团队维护的，非常适合需要一个安全、可靠、可配置且私有的文件同步服务的场景

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/file/file-management/syncthing/config`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 8384:8384 \
-p 22000:22000/tcp \
-p 22000:22000/udp \
-p 21027:21027/udp \
-e TZ=Asia/Shanghai
-v /vol1/1000/docker/file/file-management/syncthing/config:/var/syncthing/config \
-v /vol1/1000:/var/syncthing/vol1/1000 \
--user 1000:1000 \
--network yuehai-net \
--restart unless-stopped \
--name=syncthing \
syncthing/syncthing:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 syncthing 的服务
    syncthing:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: syncthing/syncthing:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: syncthing
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 指定运行容器内进程的用户和组 (UID:GID)
        user: "1000:1000"
        # 定义端口映射规则
        ports:
            # Syncthing Web UI 访问端口
            - "8384:8384"
            # Syncthing 同步协议端口
            - "22000:22000/tcp"
            # Syncthing 同步协议端口 - 用于发现
            - "22000:22000/udp"
            # Syncthing 本地发现端口
            - "21027:21027/udp"
        # 定义环境变量
        environment:
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/file/file-management/syncthing/config:/var/syncthing/config
            # 固态盘同步目录
            - /vol1/1000:/var/syncthing/vol1/1000
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

4. 想要连接上面部署的 syncthing，需要在其他设备的：`操作 -> 高级 -> 设备 -> 上面部署的 syncthing 的设备名 -> Addresses` 中，进行如下设置：
5. 外网设备，需要保证已经开放了 22000 端口：

```shell
tcp://ip:22000, quic://ip:22000
```

6. 局域网设备：

```shell
tcp://127.0.0.1:22000, quic://127.0.0.1:22000
```

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617095915.png)

## 3、访问

1. 访问迅雷迅雷群晖提取版网页： [http://127.0.0.1:41014](http://127.0.0.1:41014)
2. 扫码或使用账号密码登录


# 200、Nextcloud 自托管云存储和协作平台

> 1. 项目 github：https://github.com/55190116/nextcloud-docker
> 2. dockerHub 地址：https://hub.docker.com/r/nextcloud
> 3. 该项目需要关联一个数据库作为数据的存取

## 1、介绍

1. Nextcloud 是一个开源的私人云存储解决方案，它可以在本地或托管的环境中部署，为用户提供类似 Google Drive、Dropbox 的功能，支持文件存储、共享、协作等特性
2. Nextcloud 的核心功能：
3. **文件管理**：上传、下载、删除、共享文件。
4. **用户管理**：支持多用户系统和权限控制。
5. **扩展功能**：通过应用商店安装插件（如日历、任务管理、在线文档编辑）。
6. **设备同步**：支持 Windows、macOS、Linux 和移动端的客户端同步。
7. **加密和安全**：支持端到端加密，保障数据隐私。

## 2、docker 部署

1. 首先需要一个数据库，本次使用的是 postgres，不论在本地或者其他服务器都可
2. 在数据库中创建一个 `nextcloud` 库：

```shell
CREATE DATABASE nextcloud;
```

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/file/document-processing/nextcloud/config`
	2. 数据目录：`/vol1/1000/docker/file/document-processing/nextcloud/data`
	3. 应用插件目录：`/vol1/1000/docker/file/document-processing/nextcloud/custom_apps`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-v /vol1/1000/docker/file/document-processing/nextcloud/config:/var/www/html/config \
-v /vol1/1000/docker/file/document-processing/nextcloud/data:/var/www/html/data \
-v /vol1/1000/docker/file/document-processing/nextcloud/custom_apps:/var/www/html/custom_apps \
--network yuehai-net \
--restart=unless-stopped \
--name nextcloud \
nextcloud:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 nextcloud 的服务
    nextcloud:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: nextcloud:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: nextcloud
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Nextcloud Web 的 HTTP 服务端口映射
            - "80:80"
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 配置目录
            - /vol1/1000/docker/file/document-processing/nextcloud/config:/var/www/html/config
            # 数据目录
            - /vol1/1000/docker/file/document-processing/nextcloud/data:/var/www/html/data
            # 应用插件目录
            - /vol1/1000/docker/file/document-processing/nextcloud/custom_apps:/var/www/html/custom_apps
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

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 第一次进入需设置账号、密码、数据库信息
3. 数据库选择 postgres，然后填入以下参数：
4. 数据库账号
5. 数据库密码
6. 数据库名称
7. 数据库地址：如果都在同一个 docker 网络中，可以输入：docker容器名:5432

## 4、使用 Nginx 反向代理 Nextcloud 并配置 HTTPS 访问

1. 在 nginx 中点击添加代理，详细内容中和其他代理相同，不再详细说明

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617100922.png)

2. 配置完成后，访问d代理地址会出现如下提示：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101208.png)

3. 这是代理成功了，但是我们需要修改 Nextcloud 的配置文件，添加信任域名并修改配置
	1. 此处假设代理后的地址为：`https://nextcloud.demo.com:8080`
4. 进入挂载目录：`/vol1/1000/docker/file/document-processing/nextcloud/config`

```shell
cd /vol1/1000/docker/file/document-processing/nextcloud/config
```

5. 打开文件 `config.php` 并编辑：

```shell
nano config.php
```

6. 修改 `trusted_domains`，添加域名为信任域名，将 `nextcloud.demo.com` 替换为 Nginx 代理的域名；<font color="#ff0000">下面设置的域名都要和这个相同</font>

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
    '::1', // IPv6 回环地址
    'nextcloud.demo.com', // 可以访问 Nextcloud 的域名
    'nextcloud.demo.com:8080', // 可以访问 Nextcloud 的域名
    '172.20.0.0/16', // docker 网络 IP
  ],
```

7. 修改 `overwrite.cli.url`，设置基础 URL：

```php
  /**
   * overwrite.cli.url 是一个手动设置的基础 URL，用于生成命令行工具（例如 cron 任务或 occ 工具）中使用的链接
   * 确保当 Nextcloud 后台任务（例如 cron）生成 URL 时，使用的是正确的主机和路径
   * 避免在某些代理或特定网络环境中生成错误的 URL
   */
  'overwrite.cli.url' => 'https://nextcloud.demo.com:8080',
```

8. 在最后一行 `);` 前添加如下内容

```php
  /**
   * overwritehost 用于覆盖 Nextcloud 自动检测的主机名，通常在代理（reverse proxy）设置中使用
   * 强制 Nextcloud 使用指定的主机名，而不是从请求中自动检测的主机名
   * 解决代理场景中，因主机名不匹配导致生成错误链接的问题
   */
  'overwritehost' => 'nextcloud.demo.com:8080',
  /**
   * overwriteprotocol 用于指定请求是通过 http 或 https 协议访问的
   * 强制生成 HTTPS 链接，而不是根据请求的协议动态检测
   * 解决代理场景中，代理处理 HTTPS 请求，但传递给后端时为 HTTP 的问题
   */
  'overwriteprotocol' => 'https',
```

9. 修改完毕后，修改配置文件的用户组：

```shell
chown -R 33:33 /vol1/1000/docker/file/document-processing/nextcloud/config/config.php
```

10. 修改完毕后，重启容器，即可成功访问

## 5、其他配置修改

1. 推荐对 Nextcloud 进行一些优化设置并执行必要的维护命令，以确保其安全、高效和稳定地运行
2. 依然是进入挂载目录，打开文件 `config.php` 并编辑：

```shell
cd /vol1/1000/docker/file/document-processing/nextcloud/config

nano config.php
```

3. 在最后一行 `);` 前添加如下内容；如果有同名设置记得要先将其删除：

```php
  /**
   * 设置后台维护任务的执行窗口，例如设置为凌晨 1 点
   * 避免在白天用户使用高峰期执行资源密集型任务，影响性能
   */
  'maintenance_window_start' => 1,
  /**
   * 将所有缓存机制统一指向 Redis，以获得最佳性能和稳定性
   * 这对于 OnlyOffice 等实时协作应用尤其重要
   */
  'memcache.local' => '\\OC\\Memcache\\Redis',
  'memcache.distributed' => '\\OC\\Memcache\\Redis',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => [
    'host' => 'redis', // Redis 容器的服务名
    'port' => 6379, // Redis 容器的端口号
    'dbindex' => 1, // 为 Nextcloud 分配一个独立的数据库
    'password' => 'xxxxxxxxxxxxxxxxxxxxx', // Redis 密码
  ],
  // 为电话号码设置默认的国家/地区代码，例如中国
  'default_phone_region' => 'CN',
```

4. 修改完毕后，修改配置文件的用户组：

```shell
chown -R 33:33 /vol1/1000/docker/file/document-processing/nextcloud/config/config.php
```

5. 以下命令需要通过 docker exec 在 nextcloud 容器内部执行。它们用于修复一些安装或升级后常见的小问题，并优化数据库
6. 添加数据库缺失的索引；这个命令会扫描数据库，并为缺失的索引进行补充，可以极大地提升数据库的查询性能，让的 Nextcloud 运行更流畅：

```php
// 容器外直接使用 docker exec 执行
docker exec --user www-data nextcloud php occ db:add-missing-indices

// 容器执行
php occ db:add-missing-indices
```

7. 执行后台修复与 Mimetype 更新；
	1. 这个命令会执行一系列后台修复任务，包括修复文件缓存、更新文件类型（mimetype）定义等
	2. `--include-expensive` 参数表示执行一些耗时较长的检查，建议在首次配置完成后执行一次

```php
// 容器外直接使用 docker exec 执行
docker exec --user www-data nextcloud php occ maintenance:repair --include-expensive

// 容器执行
php occ maintenance:repair --include-expensive
```

8. 修改完毕后，重启容器即可，然后在 Nextcloud 管理设置 -> 概览页面中看到的大部分安全及设置警告都应该会消失

## 6、Nextcloud 集成 Onlyoffice

> 1. 需要部署 Onlyoffice
> 2. 这里采用离线安装的方式，因为我的应用商店无法访问，插件下载：[onlyoffice.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Fonlyoffice.tar.gz)
> 3. 如果可以访问应用商店，直接搜索 Onlyoffice 安装

1. 进入 Nextcloud 应用商店下载插件：https://apps.nextcloud.com/
2. 搜索 Onlyoffice

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108100948.png)

3. 向下拉，选择一个版本进行下载

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101004.png)

4. 下载完成后，将其上传到挂载的 `/vol1/1000/docker/file/document-processing/nextcloud/custom_apps` 目录中
5. 进入该目录，然后将 Onlyoffice 插件解压：

```shell
cd /vol1/1000/docker/file/document-processing/nextcloud/custom_apps/

tar -zxvf onlyoffice.tar.gz
```

6. 修改解压后文件的用户组：

```shell
chown -R 33:33 onlyoffice
```

7. 在 onlyoffice 7.2 版本之后，需要使用秘钥才能连接上，使用下面的命令获取 onlyoffice 的秘钥：

```shell
sudo docker exec onlyoffice /var/www/onlyoffice/documentserver/npm/json -f /etc/onlyoffice/documentserver/local.json 'services.CoAuthoring.secret.session.string' 
```

8. 进入 Nextcloud 页面，点击头像 -> 应用 -> 你的应用，会多出来一个 ONLYOFFICE，点击后面的启用来启用插件

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101034.png)

9. 启用成功后，点击头像 -> 管理设置，也会多出来一个 ONLYOFFICE，点击进入，填写 ONLYOFFICE Docs 地址和密钥
	1. ONLYOFFICE Docs 地址：表示外网可以访问的 ONLYOFFICE 地址，即 nginx 代理之后的地址
	2. 秘钥(留空为关闭)：`xxxxxxxxxxxxxxxxxxxxxxxx`
	3. 授权标头 (留空以使用默认的标头)：`Authorization`
	4. 服务器内部请求 ONLYOFFICE Docs 的地址：即 ONLYOFFICE 的局域网地址：`http://onlyoffice/`
	5. ONLYOFFICE Docs 内部请求服务器的地址：即 nextcloud 的地址，从这里获取文件：`http://nextcloud/`

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617102332.png)

10. 点击保存即可集成，成功后下方会显示常用设置等

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617102348.png)

## 7、修改 Nextcloud 集成 Onlyoffice 后的页面的样式

1. Nextcloud 集成 Onlyoffice 后默认的页面是这样的，上面还有一个工具栏，看着很不舒服，现在把他去掉

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101122.png)

2. 进入挂载目录：`/vol1/1000/docker/file/document-processing/nextcloud/custom_apps/onlyoffice/css/editor.css`，编辑：
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

5. 修改文件的用户组：

```shell
chown -R 33:33 /vol1/1000/docker/file/document-processing/nextcloud/custom_apps/onlyoffice/css/editor.css
```

6. 修改后的页面显示：按住 shift 刷新浏览器：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101143.png)

## 7、应用整理

> 对应的 nextcloud 版本是 30

### ①、Notes

1. 介绍：笔记，支持 markdown
2. 商店地址：https://apps.nextcloud.com/apps/notes
3. 本地下载：[notes-v4.11.0.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Fnotes-v4.11.0.tar.gz)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101326.png)

### ②、Draw.io

1. 介绍：在线图表工具，文件直接保存到 Nextcloud
2. 商店地址：https://apps.nextcloud.com/apps/drawio
3. 本地下载：[drawio-v3.0.3.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Fdrawio-v3.0.3.tar.gz)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101434.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101444.png)

### ③、Mind Map

1. 介绍：思维导图
2. 商店地址：https://apps.nextcloud.com/apps/files_mindmap
3. 本地下载：[files_mindmap-0.0.31.tar.gz](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Ffiles_mindmap-0.0.31.tar.gz)

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101527.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101536.png)

### ④、快捷命令

1. 全部解压：

```shell
tar -zxvf drawio-v3.1.0.tar.gz;
tar -zxvf files_mindmap-0.0.33.tar.gz;
tar -zxvf notes-v4.12.1.tar.gz;
tar -zxvf onlyoffice.tar.gz;
```

2. 全部修改权限：

```shell
chown -R 33:33 drawio files_mindmap notes onlyoffice
```


# 201、Onlyoffice 提供文档、电子表格、演示文稿等工具

> 1. 项目 github：https://github.com/ONLYOFFICE/Docker-DocumentServer
> 2. dockerHub 地址：https://hub.docker.com/r/onlyoffice/documentserver

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
2. 日志目录：`/vol1/1000/docker/file/document-processing/onlyoffice/log`
3. 文档目录：`/vol1/1000/docker/file/document-processing/onlyoffice/data`
4. 配置文件目录：`/vol1/1000/docker/file/document-processing/onlyoffice/config`

### ①、临时部署，获取配置文件

> 此步骤是为了获取 onlyoffice 的配置文件 default.json

1. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-e JWT_ENABLED=true \
-e JWT_SECRET=xxxxxxxxxxxxxxxxxxxxxxx \
-e JWT_HEADER=Authorization \
--network yuehai-net \
--restart=unless-stopped \
--name onlyoffice \
onlyoffice/documentserver:latest
```

2. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 onlyoffice 的服务
    onlyoffice:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: onlyoffice/documentserver:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: onlyoffice
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义要在容器内设置的内核参数 (sysctls)，这是一项高级配置
        sysctls:
            # 为容器内当前所有的网络接口禁用 IPv6 协议
            net.ipv6.conf.all.disable_ipv6: 1
            # 为容器内未来可能创建的任何新网络接口设置默认禁用 IPv6，这确保了即使在容器运行中添加了新网络，IPv6 依然是禁用的
            net.ipv6.conf.default.disable_ipv6: 1
        # 定义端口映射规则
        ports:
            # ONLYOFFICE Document Server 的 hTTP 服务端口映射
            - "80:80"
        # 定义容器内部的环境变量
        environment:
            # 启用 JWT (JSON Web Token)，用于保护 ONLYOFFICE 服务，防止未经授权的访问
            - JWT_ENABLED=true
            # 设置 JWT 密钥
            - JWT_SECRET=xxxxxxxxxxxxxxxxxxxxxxx
            # 设置 JWT 请求头
            - JWT_HEADER=Authorization
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

3. 容器启动成功后，将配置文件复制到宿主机

```shell
sudo docker cp onlyoffice:/etc/onlyoffice/documentserver/default.json /vol1/1000/docker/file/document-processing/onlyoffice/config/default.json
```

### ②、修改配置文件内容和权限

1. 打开配置文件，将其中的 `allowPrivateIPAddress` 和 `allowMetaIPAddress` 都修改为 `true`：

```json
"request-filtering-agent" : {
	"allowPrivateIPAddress": true,
	"allowMetaIPAddress": true
},
```

2. 修改权限:

```shell
chown -R 999:999 /vol1/1000/docker/file/document-processing/onlyoffice/
```

### ③、正式部署，挂载配置文件

1. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-e JWT_ENABLED=true \
-e JWT_SECRET=xhiNbpVz7zmszBSUNBeWTTtyColkmGYE \
-e JWT_HEADER=Authorization \
-v /vol1/1000/docker/file/document-processing/onlyoffice/log:/var/log/onlyoffice  \
-v /vol1/1000/docker/file/document-processing/onlyoffice/data:/var/www/onlyoffice/Data  \
-v /vol1/1000/docker/file/document-processing/onlyoffice/config/default.json:/etc/onlyoffice/documentserver/default.json
--network yuehai-net \
--restart=unless-stopped \
--name onlyoffice \
onlyoffice/documentserver:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 onlyoffice 的服务
    onlyoffice:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: onlyoffice/documentserver:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: onlyoffice
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义要在容器内设置的内核参数 (sysctls)，这是一项高级配置
        sysctls:
            # 为容器内当前所有的网络接口禁用 IPv6 协议
            net.ipv6.conf.all.disable_ipv6: 1
            # 为容器内未来可能创建的任何新网络接口设置默认禁用 IPv6，这确保了即使在容器运行中添加了新网络，IPv6 依然是禁用的
            net.ipv6.conf.default.disable_ipv6: 1
        # 定义端口映射规则
        ports:
            # ONLYOFFICE Document Server 的 hTTP 服务端口映射
            - "80:80"
        # 定义容器内部的环境变量
        environment:
            # 启用 JWT (JSON Web Token)，用于保护 ONLYOFFICE 服务，防止未经授权的访问
            - JWT_ENABLED=true
            # 设置 JWT 密钥
            - JWT_SECRET=xhiNbpVz7zmszBSUNBeWTTtyColkmGYE
            # 设置 JWT 请求头
            - JWT_HEADER=Authorization
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 日志目录
            - /vol1/1000/docker/file/document-processing/onlyoffice/log:/var/log/onlyoffice
            # 文档目录
            - /vol1/1000/docker/file/document-processing/onlyoffice/data:/var/www/onlyoffice/Data
            # 挂载单个配置文件，用于自定义
            - /vol1/1000/docker/file/document-processing/onlyoffice/config/default.json:/etc/onlyoffice/documentserver/default.json
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

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)，出现下面页面则部署成功

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108101959.png)

1. 执行下面两条命令，启动 onlyoffice 的测试示例页面；<font color="#ff0000">这仅是测试示例页面，正式环境不要开启</font>：

```shell
docker exec onlyoffice sudo supervisorctl start ds:example

docker exec onlyoffice sudo sed 's,autostart=false,autostart=true,' -i /etc/supervisor/conf.d/ds-example.conf
```

3. 点击 `GO TOTESTEXAMPLE` 按钮，可进入测试示例页面

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108102030.png)

4. 在测试示例页面，可选择语言，选择后地址栏上会带上参数：`lang=zh`，建议将此时的地址存为书签，因为语言的设置并不会保存，只能以地址参数设置

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108102044.png)

5. 可尝试新建或上传一个文档，测试可用性

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108102100.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108102112.png)

## 4、Nginx 代理 配置

1. 在 nginx 中点击添加代理，详细内容中和其他代理相同，不再详细说明

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617103017.png)

1. 点击高级，填入以下自定义 Nginx 配置

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617103038.png)

```nginx
# 定义一个 location 块，匹配所有进入的请求 (/)
location / {
  # 关键：将请求代理到指定服务
  # proxy_pass 指令指定了后端服务器的地址和端口
  # 所有匹配此 location 块的请求都将被转发到 http://onlyoffice
  proxy_pass http://onlyoffice;
  
  # 设置 HTTP 头部 X-Forwarded-For，包含了客户端的原始 IP 地址以及代理服务器的 IP 地址列表
  # $proxy_add_x_forwarded_for 变量会自动将 $remote_addr（直接连接到 Nginx 的客户端 IP）附加到已有的 X-Forwarded-For 头部（如果存在）
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  # 设置 HTTP 头部 X-Forwarded-Proto，告诉后端应用客户端最初是使用 HTTP 还是 HTTPS 协议访问的
  # $scheme 变量的值是 http 或 https
  proxy_set_header X-Forwarded-Proto $scheme;
  # 设置 HTTP 头部 Host，将原始请求中的 Host 头部传递给后端服务器
  # $http_host 变量包含了客户端请求中的 Host 头部信息
  proxy_set_header Host $http_host;
  # 设置 HTTP 头部 X-Real-IP，传递了直接连接到 Nginx 的客户端的真实 IP 地址
  # $remote_addr 变量的值是直接连接到 Nginx 的客户端的 IP 地址
  proxy_set_header X-Real-IP $remote_addr;
  # 设置 HTTP 头部 Range，用于支持部分内容请求，例如视频拖动播放或断点续传
  # $http_range 变量包含了客户端请求中的 Range 头部信息
  proxy_set_header Range $http_range;
  # 设置 HTTP 头部 If-Range，与 Range 头部配合使用，用于条件性的部分内容请求
  # $http_if_range 变量包含了客户端请求中的 If-Range 头部信息
  proxy_set_header If-Range $http_if_range;

  # 关闭代理重定向处理，off 表示 Nginx 不会修改后端服务器返回的 Location 和 Refresh 头部中的 URL
  # 这通常在后端应用自己能正确处理重定向 URL 时使用
  proxy_redirect off;
  # 设置客户端请求体的最大允许大小
  # 如果上传的文件超过此大小，Nginx 会返回 "413 Request Entity Too Large" 错误
  client_max_body_size 20000m;

  # 设置代理使用的 HTTP 版本为 1.1
  # WebSocket 协议需要 HTTP/1.1 或更高版本
  proxy_http_version 1.1;
  # 设置 HTTP 头部 Upgrade
  # 这个头部用于请求协议升级，例如从 HTTP 升级到 WebSocket
  # $http_upgrade 变量包含了客户端请求中的 Upgrade 头部信息
  proxy_set_header Upgrade $http_upgrade;
}
```

## 5、设置 OnlyOffice 自动保存

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108102127.png)

5. 重启即可


# 202、filebrowser 极简的文件管理工具

> 1. 项目 github：https://github.com/filebrowser/filebrowser
> 2. dockerHub 地址：https://hub.docker.com/r/filebrowser/filebrowser

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


# 300、navidrome 开源的、自托管的音乐流媒体服务器

> 1. 项目 github：https://github.com/navidrome/navidrome
> 2. dockerHub 地址：https://hub.docker.com/r/deluan/navidrome

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
	1. 配置目录：`/vol1/1000/docker/multimedia/navidrome/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 4533:4533 \
-e ND_SCANINTERVAL=1h \
-v /vol1/1000/docker/multimedia/navidrome/data:/data \
-v /vol1/1000/固态盘/内存/音乐:/music \
--network yuehai-net \
--restart unless-stopped \
--name=navidrome \
deluan/navidrome:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 navidrome 的服务
    navidrome:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: deluan/navidrome:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: navidrome
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Navidrome 的 Web UI 端口
            - "4533:4533"
        # 定义环境变量
        environment:
            # 设置 Navidrome 音乐库的扫描间隔为 24 小时
            - ND_SCANINTERVAL=24h
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/multimedia/navidrome/data:/data
            # 音乐目录
            - /vol1/1000/固态盘/内存/音乐:/music
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

## 3、访问

1. 访问：[http://127.0.0.1:4533](http://127.0.0.1:4533)
2. 初次访问需设定管理员账号密码


# 301、Jellyfin 媒体服务器

> 1. 项目 github：https://github.com/jellyfin/jellyfin
> 2. dockerHub 地址：https://hub.docker.com/r/jellyfin/jellyfin

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
	4. Jellyfin 可以部署在多种平台上，包括 Windows、Linux、macOS 以及 Docker 容器
	5. 提供多种客户端应用程序，支持智能电视、手机、平板、浏览器、Roku、Fire TV 等设备
7. **流媒体播放：**
	1. 支持多种流媒体协议（如 DLNA 和 Chromecast），可以直接将内容推送到其他设备
	2. 支持实时转码（transcoding），确保即使设备不支持某种格式也能正常播放
	3. 提供多用户支持，可以为每个家庭成员创建独立的配置和媒体收藏
8. **隐私保护：**
	4. Jellyfin 是完全本地化的服务，不需要连接外部服务器，也不会收集用户数据
	5. 用户完全控制自己的数据和服务器
9. **插件支持：**
	1. 提供丰富的插件生态系统，允许用户扩展 Jellyfin 的功能
	2. 插件功能包括直播电视（通过兼容的 TV 卡）、字幕同步（如 OpenSubtitles）、第三方媒体数据整合等

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 缓存目录：`/home/docker/docker/volumes/jellyfin/cache`
	2. 配置目录：`/home/docker/docker/volumes/jellyfin/config`
	3. 媒体目录：`/home/docker/docker/volumes/jellyfin/media`
2. 使用 docker 部署：
	4. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	5. `-p`：指定端口映射
	6. `-v`：指定挂载目录
	7. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	8. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108104150.png)

2. 之后选择类型、名称、文件夹、各种设置即可

## 5、访问媒体库

> 各种客户端下载：https://jellyfin.org/downloads/clients/

1. 各种客户端可点击上面的链接进行下载
2. 若是想在浏览器观看，则进入服务器后，点击服务器名称

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108104208.png)

3. 即可查看设定的媒体库

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108104221.png)

## 6、https 设置

> 获取证书的方式：[使用 Let's Encrypt 免费获取证书](https://github.com/yue-hai/TakeDown/blob/master/%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/%E7%BD%91%E7%BB%9C%E7%9B%B8%E5%85%B3.md#1%E4%BD%BF%E7%94%A8-lets-encrypt-%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%AF%81%E4%B9%A6)

1. 将生成的 `mykeystore.p12` 文件复制到挂载的目录下，比如 `/home/docker/docker/volumes/jellyfin/config/certificate/`
2. jellyfin 控制台中，选择网络，点击启用 https

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108104244.png)

3. 在 HTTPS 设置中，选择刚才复制的 `mykeystore.p12` 文件，填入证书密码，然后重启服务器即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108104304.png)

4. 成功后访问 https 端口：[https://127.0.0.1:8920](https://127.0.0.1:8920)


# 400、2FAuth 基于 Web 的自托管 2FA 双因素认证替代方案

> 1. 项目 github：https://github.com/Bubka/2FAuth
> 2. dockerHub 地址：https://hub.docker.com/r/2fauth/2fauth

## 1、介绍

1. 2FA 即双因素认证。一般来说，在大多数场景下都是使用帐号和密码来进行身份验证，而 2FA 就是除了建立帐号密码之外的第二个关卡。就算账号和密码不小心外泄了，也不至于账号马上被盗用。
2. 2FA 又分为硬件型和软件型。像在 App Store 上购买 App 时需要指纹，或者网银转账时需要用到的 U 盾，只有通过那只随身携带在身上的硬件才能通过验证，这些都属于硬件型的 2FA。而 OTP(One Time Password) 就是软件型的 2FA 。像大部分 APP 在风险操作时都会要求你输入验证码、或者当你要从新电脑登陆时，也需要到手机查看验证码，当然这些都是免费的。
3. 2FAuth 是一种基于 Web 的自托管替代方案，可替代 Google Authenticator 等一次性密码 （OTP） 生成器，专为移动设备和桌面设备设计。它能够通过 web 方式获取 OTP，并且将 2FA 帐户存储在一个独立的数据库中，利于数据的备份和恢复。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/tool/2fauth/2fauth`
2. 修改目录权限：

```shell
chown 1000:1000 /vol1/1000/docker/tool/2fauth/2fauth
```

3. 使用 docker run 部署：

```shell
docker run -d \
-p 8000:8000 \
-e APP_DEBUG=true \
-e APP_NAME=2FAuth \
-e APP_KEY=DkGUEbEZfdExAhSN5Bv7hZRtUJE4sCEJ \
-e APP_URL=https://2fauth.demo.com:8080 \
-e IS_DEMO_APP=false \
-e LOG_CHANNEL=daily \
-e LOG_LEVEL=notice \
-e CACHE_DRIVER=file \
-e SESSION_DRIVER=file \
-e AUTHENTICATION_GUARD=web-guard \
-v /vol1/1000/docker/tool/2fauth/2fauth:/2fauth \
--network yuehai-net \
--restart=unless-stopped \
--name 2fauth \
2fauth/2fauth:latest
```

4. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 2fauth 的服务
    2fauth:
        # 指定该服务使用的 Docker 镜像及其标签（版本），如果未指定标签，默认为 latest
        image: 2fauth/2fauth:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: 2fauth
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # 2FAuth 的 Web UI 端口
            - "8000:8000"
        # 定义环境变量
        environment:
            # 启用调试模式 (生产环境建议设为 false)
            - APP_DEBUG=true
            # 设置应用名称
            - APP_NAME=2FAuth
            # 设置应用密钥 (重要：请使用自己生成的强密钥！)
            - APP_KEY=DkGUEbEZfdExAhSN5Bv7hZRtUJE4sCEJ
            # 设置应用的访问 URL
            - APP_URL=https://2fauth.demo.com:8080
            # 设置是否为演示模式
            - IS_DEMO_APP=false
            # 设置日志通道为每日轮换
            - LOG_CHANNEL=daily
            # 设置日志级别
            - LOG_LEVEL=notice
            # 设置缓存驱动为文件
            - CACHE_DRIVER=file
            # 设置会话驱动为文件
            - SESSION_DRIVER=file
            # 设置认证守卫
            - AUTHENTICATION_GUARD=web-guard
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/2fauth/2fauth:/2fauth
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

## 3、访问

1. 因为设定了 `APP_URL=https://2fauth.demo.com:8080`，所以访问地址只能是：`https://2fauth.demo.com:8080/start`
2. 这是通过 nginx 代理之后的地址
3. 初次访问需注册管理员账号密码


# 401、LobeChat  AI 前端工具

> 1. 官网：https://lobehub.com/zh/docs/self-hosting/start
> 2. 项目 github：https://github.com/lobehub/lobe-chat
> 3. dockerHub 地址：https://hub.docker.com/r/lobehub/lobe-chat

## 1、介绍

1. LobeChat 是一款由 LobeHub 团队开发的开源聊天前端，专为对接大语言模型（如 OpenAI、DeepSeek 等）设计。它以简洁美观的界面、强大的自定义能力和丰富的插件系统著称，支持通过 Docker 快速本地化部署。
2. 核心功能：
3. 多模型支持：
	1. 可无缝切换 OpenAI、DeepSeek、Claude 等主流模型（需兼容 OpenAI API 格式）。
	2. 支持自定义模型名称（如 deepseek-chat）。
4. 插件系统：
	1. 内置插件市场，支持联网搜索、图像生成、代码解释器等扩展功能。
	2. 可开发自定义插件（基于 TypeScript + React）。
5. 对话管理：
	1. 会话历史记录自动保存，支持多标签页管理。
	2. 可导出/导入对话数据（Markdown 或 JSON 格式）。
6. 界面与交互：
	1. 响应式设计，适配 PC、平板和手机端。
	2. 支持 Markdown 渲染、代码高亮、LaTeX 公式。
	3. 主题切换（亮色/暗色模式）。
7. 安全控制：
	1. 支持密码保护、IP 白名单限制访问。
	2. 敏感词过滤和对话内容审查机制。

| 组件          | 说明                                                                 |
|---------------|----------------------------------------------------------------------|
| 前端框架      | Next.js（React） + Ant Design                                       |
| 状态管理      | Zustand                                                             |
| 插件系统      | 基于 `@lobehub/chat-plugins` SDK                                    |
| 部署方式      | Docker 容器化 / Vercel 一键部署                                     |
| 兼容性        | 要求模型 API 兼容 OpenAI 的 `/v1/chat/completions` 接口格式         |

## 2、docker 部署

1. 该应用所有数据都保存在浏览器，所以不需要配置挂载目录
2. 使用 docker run 部署：

```shell
docker run -d \
-p 3210:3210 \
--network yuehai-net \
--restart=unless-stopped \
--name lobe-chat \
lobehub/lobe-chat:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 lobe-chat 的服务
    lobe-chat:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: lobehub/lobe-chat:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: lobe-chat
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Lobe Chat 的 Web UI 端口
            - "3210:3210"
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

## 4、访问

1. 访问：[http://127.0.0.1:3210](http://127.0.0.1:3210)


# 402、Memos 开源、轻量级的备忘录服务

> 1. 项目 github：https://github.com/usememos/memos
> 2. dockerHub 地址：https://hub.docker.com/r/neosmemo/memos

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
	1. 数据目录：`/vol1/1000/docker/tool/memos/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 5230:5230 \
-v /vol1/1000/docker/tool/memos/data:/var/opt/memos \
--network yuehai-net \
--restart=unless-stopped \
--name memos \
neosmemo/memos:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 memos 的服务
    memos:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: neosmemo/memos:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: memos
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Memos 的 Web UI 端口
            - "41042:5230"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/memos/data:/var/opt/memos
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

## 3、访问

1. 访问：[http://127.0.0.1:5230](http://127.0.0.1:5230)
2. 初次访问需设定管理员账号密码


# 403、onenav 开源的导航管理工具

> 1. 项目 github：https://github.com/helloxz/onenav
> 2. dockerHub 地址：https://hub.docker.com/r/helloz/onenav

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
	1. 配置目录：`/vol1/1000/docker/tool/onenav/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-v /vol1/1000/docker/tool/onenav/data:/data/wwwroot/default/data \
--network yuehai-net \
--restart=unless-stopped
--name onenav \
helloz/onenav:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 onenav 的服务
    onenav:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: helloz/onenav:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: onenav
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # OneNav 的 Web UI 端口
            - "80:80"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/onenav/data:/data/wwwroot/default/data
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

## 3、访问

1. 访问：[http://101.200.86.248:80/](http://101.200.86.248:80/)
2. 初次访问需注册管理员账号密码

# 404、Nexterm 基于浏览器的服务器管理工具

> 1. 项目 github：https://github.com/gnmyt/Nexterm
> 2. dockerHub 地址：https://hub.docker.com/r/germannewsmaker/nexterm

## 1、介绍

1.  Nexterm 是一个多功能的终端应用程序，专为提高开发者在使用命令行时的效率而设计。它通常包括如下几个关键功能：
2. **多标签和拆分视图**：用户可以在一个窗口中打开多个标签，每个标签可以进一步拆分为多个视图，方便同时监控和操作多个会话
3. **高度可定制**：Nexterm 提供丰富的定制选项，包括主题、快捷键和布局等，用户可以根据个人喜好调整这些设置
4. **集成开发环境功能**：此应用程序可能集成了代码编辑器、版本控制系统以及其他开发工具，使其不仅仅是一个简单的终端模拟器，而是一个全面的开发环境
5. **插件和扩展支持**：通过支持插件和扩展，Nexterm 允许用户添加新功能或集成其他工具，以扩展其核心功能
6. **跨平台兼容性**：Nexterm 设计之初就考虑到了跨平台使用的需求，通常支持 Windows、MacOS 和各种 Linux 发行版
7. **高级命令行功能**：可能包括内置的命令行搜索、历史记录管理和自动完成等功能，以提升用户的工作效率
8. Nexterm 旨在为开发者提供一个强大而高效的工作环境，通过以上的功能帮助用户简化和优化日常的开发任务。不过需要注意的是，关于 Nexterm 的具体信息可能因版本和开发社区的持续更新而有所变动

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/tool/nexterm/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 6989:6989 \
-e ENCRYPTION_KEY="xxx" \
-v /vol1/1000/docker/tool/nexterm/data:/app/data \
--network yuehai-net \
--restart=unless-stopped \
--name nexterm \
germannewsmaker/nexterm:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 nexterm 的服务
    nexterm:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: germannewsmaker/nexterm:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: nexterm
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # NextSSH/NexTerm 的 Web UI 端口
            - "6989:6989"
        # 定义环境变量
        environment:
            # 加密密钥，可以使用 openssl rand -hex 32 生成
            - ENCRYPTION_KEY=xxx
		# 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/nexterm/data:/app/data
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

## 3、访问

1. 访问：[http://127.0.0.1:6989](http://127.0.0.1:6989)
2. 初次访问需设定管理员账号密码


# 405、vaultwarden 密码管理器

> 1. 项目 github：https://github.com/dani-garcia/vaultwarden
> 2. dockerHub 地址：https://hub.docker.com/r/vaultwarden/server

## 1、介绍

1. Vaultwarden 是一个用 Rust 语言编写的、非官方的 Bitwarden 服务器实现（曾用名 bitwarden_rs）。它与官方的 Bitwarden 客户端完全兼容，但对系统资源的要求极低，非常适合个人、家庭或小型团队进行自托管密码管理
2. 它的主要特点包括：
	1. 轻量高效：这是 Vaultwarden 最核心的优势。与官方使用 .NET 和 Microsoft SQL Server 的多容器、资源密集型方案不同，Vaultwarden 作为一个单一的、极小的程序运行，内存和 CPU 占用都非常低，甚至可以在树莓派等低功耗设备上流畅运行
	2. 完全兼容：不需要任何特殊的客户端。所有官方的 Bitwarden 客户端（包括浏览器扩展、桌面应用、iOS 和 Android 移动应用）都可以直接连接到自托管的 Vaultwarden 服务器，只需在登录时将服务器地址指向您的域名或 IP 即可
	3. 解锁高级功能：Vaultwarden 免费提供了许多在官方 Bitwarden 服务中需要付费订阅才能使用的功能。这包括：
		1. TOTP 身份验证器密钥存储和代码生成（即它本身可以作为一个 2FA 应用）
		2. 创建和管理组织（Organizations），方便与家人或团队成员安全地共享密码
		3. 密码健康报告，用于检查弱密码、重复使用的密码等
		4. 文件附件和紧急访问功能
	4. 数据自托管与安全：通过自托管 Vaultwarden，所有的敏感密码数据都存储在自己的服务器上，完全掌控，无需信任任何第三方云服务提供商。同时，它也是一个开源项目，代码公开可审计
	5. 易于部署：通常通过一个非常简单的 Docker 容器来部署，整个安装和配置过程比官方的 Bitwarden 服务器要简单得多

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/tool/vaultwarden/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-e DOMAIN="https://vaultwarden.demo.com:8080" \
-e WEBSOCKET_ENABLED="true" \
-e ADMIN_TOKEN='xxxxxxxxxxxxxxx' \
-e SIGNUPS_ALLOWED='true' \
-e TZ="Asia/Shanghai" \
-v/vol1/1000/docker/tool/vaultwarden/data:/data/ \
--network yuehai-net \
--restart=unless-stopped  \
--name vaultwarden \
vaultwarden/server:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 vaultwarden 的服务
    vaultwarden:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: vaultwarden/server:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: vaultwarden
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Vaultwarden 的主 Web 界面
            - "80:80"
        # 定义环境变量
        environment:
            # Vaultwarden 服务的公开访问地址，客户端会使用这个地址连接
            - DOMAIN=https://vaultwarden.demo.com:8080
            # 启用 WebSocket 功能
            - WEBSOCKET_ENABLED=true
            # 设置管理员页面的访问令牌
            - ADMIN_TOKEN=xxxxxxxxxxxxxxx
            # 禁止新用户自行注册；先设置为 true，注册完自己的账号后再设置为 false
            - SIGNUPS_ALLOWED=true
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/tool/vaultwarden/data:/data
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

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 初次访问创建自己的账号，之后关闭允许新用户注册
3. 管理员页面，输入上面的管理员密钥进入：https://vaultwarden.demo.com:8080/admin


# 406、vlmcsd windows 激活 KMS 服务器

> 1. 项目 github：https://github.com/mikolatero/docker-vlmcsd
> 2. dockerHub 地址：https://hub.docker.com/r/mikolatero/vlmcsd

## 1、介绍

1. mikolatero/vlmcsd 是 vlmcsd 的一个流行 Docker 镜像。vlmcsd 是一个用 C 语言编写的、轻量级的密钥管理服务（KMS）模拟器，它用于在局域网内模拟微软的 KMS 主机，以激活支持批量许可的 Windows 和 Office 等产品
2. 它的主要特点包括：
	1. 轻量高效：完全由 C 语言编写，无任何依赖，程序体积小，运行时占用的内存和 CPU 资源极低，非常适合在低功耗设备或家庭服务器上 24 小时运行
	2. 广泛的兼容性：完整地模拟了微软的 KMS v4、v5 和 v6 激活协议，能够激活市面上绝大多数的批量许可版（Volume License）Windows 操作系统和 Office 套件
	3. 零配置启动：在默认模式下，无需任何复杂配置即可启动。容器运行后会自动在标准 KMS 端口（1688）上开始监听激活请求
	4. 跨平台部署：通过 Docker 容器化，可以轻松地部署在任何支持 Docker 的操作系统上（如 Linux, Windows, macOS），为各种环境提供激活服务
	5. 无状态服务：服务本身是无状态的，不记录客户端的激活历史，这使得服务的维护、迁移和备份都非常简单

## 2、docker 部署

1. 使用 docker run 部署：

```shell
docker run -d \
-p 1688:1688 \
-e "TZ=Asia/Shanghai" \
--log-driver json-file \
--log-opt max-size=10m \
--log-opt max-file=3 \
--network yuehai-net \
--restart=unless-stopped \
--name kms-vlmcsd:latest \
mikolatero/vlmcsd:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 kms-vlmcsd 的服务
    kms-vlmcsd:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: mikolatero/vlmcsd:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: kms-vlmcsd
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # KMS 服务的标准端口
            - "1688:1688"
        # 定义容器内部的环境变量
        environment:
            # 设置容器的时区
            - TZ=Asia/Shanghai
        # 使用 Docker 的日志驱动来管理和持久化日志
        logging:
            driver: "json-file"
            options:
                # 单个日志文件最大10MB
                max-size: "10m"
                # 最多保留3个日志文件
                max-file: "3"
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

## 3、使用

### ①、激活 Windows

1. 所有 GVLK 密钥都由微软官方提供，在 [官方文档](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys) 中，根据操作系统版本，找到对应的密钥
2. 一部分 Windows 激活密钥：

```shell
# win10 企业版
NPPR9-FWDCX-D2C8J-H872K-2YT43

# win10 专业版
W269N-WFGWX-YVC9B-4J6C9-T83GX

# win10 家庭版
TX9XD-98N7V-6WMQ6-BX7FG-H8Q99

# Windows Server 2019 Datacenter
WMDGN-G9PQG-XVVXX-R3X43-63DFG

# Windows Server 2019 Standard
N69G4-B89J2-4G8F4-WWYCC-J464C

# Windows Server 2019 Essential
WVDHN-86M7X-466 P 6-VHXV7-YY726
```

1. Windows 激活方式：

```shell
# 安装 Windows 11 专业版对应的 GVLK 密钥
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX

# 指定 KMS 服务器的 IP 地址和端口
slmgr /skms 127.0.0.1:1688

# 立即执行激活
slmgr /ato

# 检查激活状态 (可选)
slmgr /xpr
```

### ②、激活 office

1. office 同样需要使用微软官方提供的 GVLK，在 [官方文档](https://learn.microsoft.com/zh-cn/office/volume-license-activation/gvlks) 中，根据 office 版本，找到对应的密钥
2. 一部分 office 激活密钥：

| 版本                                 | 密钥                            |
| ---------------------------------- | ----------------------------- |
| Office LTSC 专业增强版 2024             | XJ2XN-FW8RK-P4HMP-DKDBV-GCVGB |
| Office LTSC 标准版 2024               | V28N4-JG22K-W66P8-VTMGK-H6HGR |
| Office LTSC Professional Plus 2021 | FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH |
| Office LTSC Standard 2021          | KDX7X-BNVR8-TXXGX-4Q7Y8-78VT3 |

1. office 激活方式：
2. 进入 office 的安装目录，这个目录通常是下面中的一个（取决于 office 版本和位数）：
	1. 64位 office: `C:\Program Files\Microsoft Office\Office16`
	2. 32位 office: `C:\Program Files (x86)\Microsoft Office\Office16`

```shell
# 进入 office 安装目录
cd C:\Program Files\Microsoft Office\Office16

# 安装 GVLK 密钥
cscript ospp.vbs /inpkey:FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH
# 设置 KMS 服务器 IP 地址
cscript ospp.vbs /sethst:127.0.0.1
#  设置 KMS 服务器端口
cscript ospp.vbs /setprt:1688
#  立即执行激活
cscript ospp.vbs /act
# 查看激活状态(可选) 
cscript ospp.vbs /dstatus
```

## 4、KMS 激活报错

### ①、报错：0x80080005

1. 有两个解决方案：
2. 方案一：删除注册表项：`KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SppExtComObj.exe`
	1. win+R 键打开运行窗口，输入：regedit

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617105718.png)

1. 方案二：下载 Office Tool 运行起来，按照下面图片所示点击操作就可以了：

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617105733.png)

### ②、

### ③、


# 407、NextChat AI 前端工具

> 1. 项目 github：https://github.com/ChatGPTNextWeb/NextChat
> 2. dockerHub 地址：https://hub.docker.com/r/yidadaa/chatgpt-next-web

## 1、介绍

1. NextChat 是一个开源的聊天应用，旨在为用户提供类似 ChatGPT 的交互体验
2. 基于现代前后端架构：NextChat 是基于 Next.js 构建的，利用其最新的特性（例如 Server Actions 和 API 路由）来实现高效、动态的前后端交互。这使得开发者可以更轻松地进行定制和扩展。
3. 多 API 集成支持：除了常见的 OpenAI API 外，NextChat 还支持 DeepSeek 等其他 API 服务。这样一来，用户和开发者可以根据需求灵活选择不同的语言模型或搜索服务，提升应用的智能化水平。
4. 灵活的部署方式：通过 Docker 部署可以快速搭建运行环境，支持使用 docker run 或 docker-compose 部署，简化了环境配置和运维管理。开发者可以通过环境变量配置数据库连接、认证参数和 API 密钥，满足不同生产环境的需求。
5. 安全认证与会话管理：NextChat 集成了 NextAuth 等认证方案，能够对用户会话进行安全管理，确保数据传输安全。这对于涉及用户数据和敏感信息的应用尤为重要。
6. 良好的扩展性和定制化：开源的特性和模块化设计使得开发者可以根据自己的业务需求定制和扩展功能，例如添加新的对话接口、调整 UI 界面以及接入更多第三方服务。

## 2、docker 部署

1. 该应用所有数据都保存在浏览器，或者通过 WebDAV 同步，所以不需要配置挂载目录
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3.  `-e`：设置环境变量
		1. `OPENAI_API_KEY`：<font color="#ff0000">必填</font>，OpenAI 密钥，可使用英文逗号隔开多个 key，即使不用 OpenAI 也需要填写
		2. `CODE`：访问密码；如果不填写此项，则任何人都可以直接使用部署后的网站，可能会导致 token 被急速消耗完毕，建议填写此选项
		3. `DEEPSEEK_URL`：deepseek 的 base_url，因为我要使用 deepseek 所以填写，如果要使用其他的 ai，可以设定其他的
		4. `DEEPSEEK_API_KEY`：deepseek 的 api_key
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 3000:3000 \
-e CODE=123,456,789 \
-e OPENAI_API_KEY=sk-xxx \
-e DEEPSEEK_URL=https://api.deepseek.com \
-e DEEPSEEK_API_KEY=sk-xxx \
--restart=unless-stopped \
--name nextchat \
yidadaa/chatgpt-next-web:latest
```

## 3、访问

1. 访问：[http://127.0.0.1:3000](http://127.0.0.1:3000)
2. 进入网址后会自动弹出提示，点击箭头处提示：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250312101212.png)

3. 输入密码，仅在第一行填入部署时使用 CODE 设置的密码即可：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250312101227.png)

4. 登录成功后即可正常使用
5. 因为上面部署时只配置了 deepseek 的 api_key，所以只能使用 deepseek，要使用其他 ai，可以增加其他 ai 的配置

## 4、nginx 配置

> 1. 如果 nginx 代理使用的 80 或者 443 端口可以不进行此配置
> 2. 如果使用的其他端口比如 1443，则需要进行此配置

1. 代理服务设置：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250312101259.png)

2. 因为 Next.js 的 Server Actions 安全验证机制与反向代理配置的可能冲突，增加以下配置：
	1. 主要的配置项为：`proxy_set_header X-Forwarded-Host $host:1443;`

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250312101623.png)

```nginx
location / {
	proxy_pass http://172.17.0.1:3000; # 指向容器映射的端口
	proxy_set_header Host $host:$server_port; # 保留端口信息
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header X-Forwarded-Proto $scheme;
	proxy_set_header X-Forwarded-Host $host:1443; # 关键：包含端口
	proxy_set_header X-Forwarded-Port $server_port;
}
```

3. 这样配置完成后，就不会报错了，可正常对话


# 500、QD 一个 HTTP 定时任务自动执行 Web 框架

> 1. 项目 github：https://github.com/qd-today/qd
> 2. dockerHub 地址：https://hub.docker.com/r/qdtoday/qd

## 1、介绍

1. QD（全称：Quick Deployment）是一个基于 HAR 编辑器和 Tornado 服务器的 HTTP 定时任务自动执行 Web 框架。 它允许用户通过上传抓包得到的 HAR 文件，快速创建并执行 HTTP 请求任务，常用于自动签到等场景。
2. 主要特性：
3. 基于 HAR 文件： 用户只需上传通过抓包工具（如 Chrome 开发者工具）获取的 HAR 文件，即可生成对应的 HTTP 请求任务模板，简化了任务创建过程
4. Tornado 服务器： 采用 Tornado 作为服务器框架，实现异步响应前端请求和发起 HTTP 请求，提高了并发处理能力
5. API 与插件支持： 内置多种 API 和过滤器供模板制作使用，未来计划提供自定义插件支持，增强框架的扩展性
6. 开源项目： QD 基于 MIT 许可证开源，用户可以自由使用、修改和分发

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/script/qd-qiandao/config`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-v /vol1/1000/docker/script/qd-qiandao/config:/usr/src/app/config \
--network yuehai-net \
--restart unless-stopped \
--name qd-qiandao \
qdtoday/qd:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 qd-qiandao 的服务
    qd-qiandao:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: qdtoday/qd:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: qd-qiandao
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # QD 框架的 Web UI 端口
            - "80:80"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/script/qd-qiandao/config:/usr/src/app/config
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

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 初次访问需设定管理员账号密码

## 4、脚本仓库整理

1. 各平台签到：https://github.com/wjf0214/qd-templates

## 5、使用 pushplus 进行消息推送

> pushplus 网址：https://www.pushplus.plus/

1. 点击工具箱 -> 推送设置，选择自定义推送，然后下面的任务结果通知选择、任务推送开关全部打开

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617110004.png)

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108110714.png)

7. 点击测试可查看是否设置成功，点击提交进行保存
8. 设置完成后，可以执行一个任务查看是否可以正常推送


# 501、qinglong 青龙定时任务管理

> 1. 项目 github：https://github.com/whyour/qinglong
> 2. dockerHub 地址：https://hub.docker.com/r/whyour/qinglong

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
	1. 数据目录：`/vol1/1000/docker/script/qinglong/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-e QlBaseUrl="/" \
-e QlPort="5700" \
-p 5700:5700 \
-v /vol1/1000/docker/script/qinglong/data:/ql/data \
--network yuehai-net \
--restart unless-stopped \
--hostname qinglong \
--name qinglong \
whyour/qinglong:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 qinglong 的服务
    qinglong:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: whyour/qinglong:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: qinglong
        # 设置容器的主机名
        hostname: qinglong
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # 青龙面板的 Web UI 端口
            - "5700:5700"
        # 定义环境变量
        environment:
            # 设置青龙面板的基础 URL (如果通过反向代理访问，可能需要修改)
            - QlBaseUrl=/
            # 设置青龙面板监听的端口 (需要与 ports 中的容器端口一致)
            - QlPort=5700
        # 定义数据卷挂载规则 (格式：主机路径:容器路径)
        volumes:
            # 数据目录
            - /vol1/1000/docker/script/qinglong/data:/ql/data
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

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108110424.png)

7. 如果添加依赖库出现安装失败和提示源问题，使用 ssh 工具进入青龙面板容器，执行下面的代码：

```shell
npm config set registry https://registry.npmmirror.com/
```

8. 耐心等待安装即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108110442.png)

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

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108110459.png)

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


# 502、cronicle 轻量的定时任务工具

> 1. 项目 github：https://github.com/soulteary/docker-cronicle
> 2. dockerHub 地址：https://hub.docker.com/r/soulteary/cronicle

## 1、介绍

1. soulteary/cronicle 是 Cronicle 的一个流行 Docker 镜像。Cronicle 是一个功能强大的任务调度与运行器，可以把它看作是一个带有现代化 Web 界面的、分布式的 cron（Linux 系统中的定时任务服务）替代品，用于集中管理和监控您的所有自动化脚本
2. 它的主要特点包括：
	1. 可视化管理：提供一个功能完善的 Web 界面，您可以在浏览器中轻松地创建、编辑、禁用和手动运行您的定时任务，无需再手动编辑复杂的 crontab 文件
	2. 分布式执行：支持主从（Master-Slave）架构，一个主节点可以管理多个从节点，并将任务分派到不同的服务器上执行，非常适合多服务器环境
	3. 实时监控与日志：在 Web 界面上可以实时查看每个任务的运行状态、进度和性能图表，并为每一次执行都保存了完整的日志，方便审计和排错
	4. 丰富的插件与事件链：支持插件来扩展功能，并且可以设置事件链，例如当一个任务成功（或失败）后，自动触发另一个任务的执行
	5. 灵活的调度选项：除了支持标准的 cron 时间表达式，还支持更易于理解的自然语言调度（例如，"every 2 hours"），并可以处理时区转换

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/script/cronicle/data`
	2. 日志目录：`/vol1/1000/docker/script/cronicle/logs`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 3012:3012 \
-e TZ="Asia/Shanghai" \
-v /vol1/1000/docker/script/cronicle/data:/opt/cronicle/data \
-v /vol1/1000/docker/script/cronicle/logs:/opt/cronicle/logs \
-v /vol1/1000:/vol1/1000
-v /etc/localtime:/etc/localtime:ro \
-v /etc/timezone:/etc/timezone:ro \
-v /var/run/docker.sock:/var/run/docker.sock \
--health-cmd "wget --no-verbose --tries=1 --spider localhost:3012/api/app/ping || exit 1" \
--health-interval=30s \
--health-timeout=5s \
--health-retries=3 \
--log-driver json-file \
--log-opt max-size=10m \
--log-opt max-file=3 \
--network yuehai-net \
--restart unless-stopped \
--name cronicle \
soulteary/cronicle:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 cronicle 的服务
    cronicle:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: soulteary/cronicle:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: cronicle
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Cronicle 的 Web UI 访问端口
            - "3012:3012"
        # 定义容器内部的环境变量
        environment:
            # 设置容器的时区
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 数据目录
            - /vol1/1000/docker/script/cronicle/data:/opt/cronicle/data
            # 日志目录
            - /vol1/1000/docker/script/cronicle/logs:/opt/cronicle/logs
            # 添加挂载目录，使 cronicle 可以操作其中的内容
            - /vol1/1000:/vol1/1000
            # 通过挂载文件来同步时区
            - /etc/localtime:/etc/localtime:ro
            - /etc/timezone:/etc/timezone:ro
            #将主机的 Docker Socket 挂载到容器，允许 Cronicle 直接与 Docker 守护进程交互
            - /var/run/docker.sock:/var/run/docker.sock
        # 定义容器的健康检查，Docker 会定期执行此命令来判断容器是否仍在正常工作
        healthcheck:
            # 用于检查健康的命令。这里通过 wget 尝试访问自身的 API，如果失败则容器状态会变为 "unhealthy"
            test: "wget --no-verbose --tries=1 --spider localhost:3012/api/app/ping || exit 1"
            # 每隔 30 秒执行一次健康检查
            interval: 30s
            # 每次检查的超时时间为 5 秒
            timeout: 5s
            # 在标记为 unhealthy 之前，允许 3 次连续的检查失败
            retries: 3
        # 定义此容器的日志记录方式
        logging:
            # 使用 json-file 驱动程序
            driver: json-file
            # 为驱动程序提供额外选项
            options:
                # 单个日志文件的最大尺寸为 10MB
                max-size: "10m"
                # 最多保留 3 个轮换的日志文件
                max-file: "3"
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络
            - yuehai-net

# 在文件末尾定义此 Compose 文件中使用的所有网络
networks:
    # 定义一个名为 yuehai-net 的网络配置
    yuehai-net:
        # 将此网络声明为外部网络
        external: true
```

## 3、访问

1. 访问：[http://127.0.0.1:3012](http://127.0.0.1:3012)
2. 默认账号：admin
3. 默认密码：admin

## 4、使 cronicle 可以执行 docker 命令

1. 命令行进入容器，执行：

```
apk add --no-cache docker-cli
```

2. 具体说明：
3. Docker 分为守护进程（Daemon）和客户端（Client）：
	1. Docker 守护进程是后台运行的核心引擎，负责实际创建、运行和管理所有容器、镜像及网络
	2. Docker 客户端是用户交互的命令行工具，负责接收命令（如 docker ps）并将其发送给守护进程去执行
4. 两者的通信机制为客户端-服务器模式：在 Linux 上，客户端默认通过一个名为 Unix Socket 的文件 `/var/run/docker.sock`，向守护进程发送 API 指令
5. 所以在 Cronicle 容器中安装 docker-cli 之后，它就拥有了自己的客户端。通过将宿主机的 `/var/run/docker.sock` 文件挂载到容器内，这个新的客户端就能连接到宿主机上唯一的 Docker 守护进程，从而获得与在宿主机上执行 docker 命令完全相同的容器管理能力


# 503、NapCatQQ 基于 TypeScript 构建的 QQ Node 模块

> 1. 项目 github：https://github.com/NapNeko/NapCatQQ
> 2. 项目 Docker 版本 github：https://github.com/NapNeko/NapCat-Docker
> 3. dockerHub 地址：https://hub.docker.com/r/mlikiowa/napcat-docker
> 4. 官网：https://napneko.github.io/
> -------- 
> 1. 本来想将 NapCatQQ 和 nonebot-bison 都部署在阿里云上，但是阿里云的 WebSocket 好像要收费才能开通，所以 nonebot-bison 部署后连接不上
> 2. 但是不知道为什么 NapCatQQ 可以启动，WebSocket 的客户端和服务端都可以正常启动并连接，为什么 nonebot-bison 不行？
> 3. 具体原因到底是不是这个，还有待考证；[WebSocket 官网计费说明](https://help.aliyun.com/zh/edge-security-acceleration/dcdn/configure-websocket)
> 4. 所以现在 NapCatQQ 部署在阿里云上，nonebot-bison 部署在自己的实体机上
> -------- 
> 1. 经过尝试，阿里云上部署之后有可以链接上了，参数都没变，只是将我实体机上使用的镜像导出，上传到了阿里云的服务器上使用
> 2. 难道是上一次镜像下载时出错了？还有待考证

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
	4. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	5. `-p`：指定端口映射
		1. 3000、3001：NapCatQQ 与 QQ 服务器通信的端口
		2. 6099：NapCatQQ 的 web 端口
		3. 3003、3004：预留的，NapCatQQ 服务器端口；只使用反向连接的话，不要这两个端口也可以
	6. `-e WEBUI_TOKEN`：TOKEN，登录 web 后台时需要提供，作为密码
	7. `-v`：指定挂载目录
	8. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

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

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105258.png)

4. 扫描并且确认后，等待几面就会自动进入管理页面

## 4、日志查看

1. 点击日志查看，可以看到登录的 QQ 号接收的消息，私聊和群聊都可以看到

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105417.png)

## 5、将 NapCatQQ 作为 java 端的 WebSocket 服务器

1. 点击网络配置 -> 添加配置
	1. 名称：比如：`将 NapCatQQ 作为 java 端的 WebSocket 服务器`
	2. 类型：WebSocket 服务器

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105436.png)

2. 勾选启用
3. 主机使用默认 `0.0.0.0`，不用修改
4. 端口修改为 3003、3004 其中之一；如果想使用别的端口，需在创建 docker 容器时指定
5. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105626.png)

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

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250110092528.png)

2. 勾选启用
3. 端口修改为 3003、3004 其中之一；如果想使用别的端口，需在创建 docker 容器时指定
4. 主机使用默认 `0.0.0.0`，不用修改
5. CORS 和 WS 可以关闭
6. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250110092539.png)

7. 开启后，可通过 ip 和 端口，调用其接口，实现各种操作

## 7、将 NapCatQQ 接入 nonebot11 的服务端

1. 继续看下面的 nonebot-bison 的部署和使用

# 504、nonebot-bison 通用订阅推送插件机器人

> 1. 项目 github：https://github.com/MountainDash/nonebot-bison
> 2. dockerHub 地址：https://hub.docker.com/r/felinae98/nonebot-bison

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
	2. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	3. `-p`：指定端口映射
	4. `-e`：设置环境变量
		1. `SUPERUSERS`：管理员 QQ，可管理、配置机器人 QQ
		2. `BISON_CONFIG_PATH`：配置文件目录
		3. `BISON_OUTER_URL`：从外部访问服务器的地址，因为 nonebot-bison 并不能自动识别 IP，所以需要手动指定；
		4. `BISON_FILTER_LOG`：是否过滤来自 nonebot 的 warning 级以下的 log，如果你的 bot 只运行了这个插件可以考虑 开启，默认关
		5. `BISON_USE_PIC`：将几乎所有文字渲染成图片后进行发送，多用于规避风控
	5. `-v`：指定挂载目录
	6. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

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

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105850.png)

2. 勾选启用
3. URL 填入：`ws://172.17.0.1:8080/onebot/v11/ws`
	1. IP 和端口根据 nonebot-bison 所在主机的地址进行修改
	2. 我是在同一个机器的 docker 下部署的，所以 `172.17.0.1` 指向本机地址，即类似 `127.0.0.1`
4. 其他默认，不用修改，点击确定

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105926.png)

5. NapCatQQ 与 nonebot-bison 成功建立链接时，日志上会显示 connect open

```shell
01-07 07:46:40 [INFO] uvicorn | ('172.17.0.1', 37354) - "WebSocket /onebot/v11/ws" [accepted]
01-07 07:46:40 [INFO] websockets | connection open
```

## 5、后台管理

1. NapCatQQ 与 nonebot-bison 成功建立链接后，可以私聊 `/后台管理` 获取后台管理地址

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108105948.png)

2. 也可以直接在群里 @，然后发送指令进行管理：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250107151702.png)




# 【----------------主机模式 ----------------】


# 1000、vnstat 轻量的流量统计工具

> 1. 项目 github：https://github.com/vergoh/vnstat
> 2. dockerHub 地址：https://hub.docker.com/r/vergoh/vnstat

## 1、介绍

1. vnStat 是一个基于控制台的轻量级网络流量监控工具，它以守护进程方式在后台持续记录选定网络接口的历史流量数据，并提供详细的使用情况报告
2. 它的主要特点包括：
	1. 持久化统计：所有流量数据被存储在数据库中，即使系统或容器重启，历史数据（如每日、每月、每年流量）也不会丢失，非常适合长期流量跟踪
	2. 轻量级监控：以守护进程（vnstatd）模式在后台运行，资源占用极低，几乎不影响系统性能
	3. 图形化 Web 界面：该镜像内置了一个轻量级 Web 服务器，可以通过浏览器直观地查看由 vnstati 生成的流量图表报告，让数据一目了然
	4. 多种报告模式：除了 Web 界面，底层的 vnstat 工具本身也支持在命令行生成实时、每日、每月等多种维度的文本报告
	5. 自动接口检测：在 host 网络模式下部署后，能自动检测主机上的网络接口并开始监控，配置简单

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/code/vnstat/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-e TZ=Asia/Shanghai \
-e LANG=zh_CN.UTF-8 \
-v /vol1/1000/docker/code/vnstat/data:/var/lib/vnstat \
--network host \
--restart unless-stopped \
--name vnstat \
vergoh/vnstat:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 vnstat 的服务
    vnstat:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: vergoh/vnstat:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: vnstat
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 直接使用主机的网络堆栈，让 vnstatd 守护进程可以直接发现并监控主机的网络接口
        network_mode: host
        # 定义环境变量
        environment:
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
            # 设置容器的语言环境，以支持中文字符
            - LANG=zh_CN.UTF-8
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/code/vnstat/data:/var/lib/vnstat
```

## 3、访问

1. 访问：[http://127.0.0.1:8685](http://127.0.0.1:8685)


# 1001、netdata 实时性能监控和可视化工具

> 1. 项目 github：https://github.com/netdata/netdata
> 2. dockerHub 地址：https://hub.docker.com/r/netdata/netdata

## 1、介绍

1. netdata/netdata 是 Netdata 的官方 Docker 镜像。Netdata 是一个功能极为强大的、分布式的、实时的性能与健康监控系统，它能够以每秒一次的高精度收集数千个指标，帮助您深入了解服务器、容器和应用程序的运行状况
2. 它的主要特点包括：
	1. 实时高精度监控：以秒级为单位收集和展示数千个系统和应用指标，提供极低延迟的实时性能图表，非常适合快速诊断和发现瞬时问题
	2. 零配置与自动发现：启动后能自动检测运行在主机或 Docker 中的各种服务（如数据库、Web服务器等），并立即开始收集对应的性能指标，无需手动配置
	3. 强大的可视化：提供一个信息密度极高且完全交互式的 Web 仪表盘，预置了数百个精心设计的图表，并按逻辑分组，让您轻松浏览和分析系统性能
	4. 内置健康警报：自带数百个预先配置好的健康警报规则，可以主动监测系统异常状态（如CPU过高、磁盘将满），并通过多种方式（如邮件、Slack、Telegram）发送通知
	5. 分布式与云端集成：每个 Netdata 代理都是一个独立的监控节点，但可以将它们全部连接到免费的 Netdata Cloud 服务，在一个统一的界面上集中查看和管理您所有的服务器状态

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 用户配置目录：`/vol1/1000/docker/code/netdata/config`
	2. 监控历史目录：`/vol1/1000/docker/code/netdata/lib`
	3. 缓存文件目录：`/vol1/1000/docker/code/netdata/cache`
2. 使用 docker run 部署：

```shell
docker run -d \
-e TZ="Asia/Shanghai" \
-e PUID=1000 \
-e PGID=1000 \
-v /etc/passwd:/host/etc/passwd:ro \
-v /etc/group:/host/etc/group:ro \
-v /proc:/host/proc:ro \
-v /sys:/host/sys:ro \
-v /vol1/1000/docker/code/netdata/config:/etc/netdata
-v /vol1/1000/docker/code/netdata/lib:/var/lib/netdata
-v /vol1/1000/docker/code/netdata/cache:/var/cache/netdata
--network=host \
--cap-add SYS_PTRACE \
--security-opt apparmor=unconfined \
--restart=unless-stopped \
--name=netdata \
netdata/netdata:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 netdata 的服务
    netdata:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: netdata/netdata:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: netdata
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 直接使用主机的网络堆栈，这意味着容器将共享主机的 IP 地址和端口空间
        network_mode: host
        # 增加容器的 Linux 能力，SYS_PTRACE 是 Netdata 进行深度监控所必需的
        cap_add:
            - SYS_PTRACE
        # 设置安全选项，解除 AppArmor 的限制，以允许 Netdata 访问必要的系统信息
        security_opt:
            - apparmor:unconfined
        # 定义环境变量
        environment:
            # 设置容器的时区
            - TZ=Asia/Shanghai
            # 设置运行用户和组的 ID，以避免权限问题
            - PUID=1000
            - PGID=1000
        # 定义数据卷挂载规则
        volumes:
            # 用户配置目录
            - /vol1/1000/docker/services/monitoring/netdata/config:/etc/netdata
            # 监控历史目录
            - /vol1/1000/docker/services/monitoring/netdata/lib:/var/lib/netdata
            # 缓存文件目录
            - /vol1/1000/docker/services/monitoring/netdata/cache:/var/cache/netdata
            # 将主机的 /etc/passwd 文件以只读方式挂载到容器中，用于用户和进程监控
            - /etc/passwd:/host/etc/passwd:ro
            # 将主机的 /etc/group 文件以只读方式挂载到容器中，用于用户组和进程监控
            - /etc/group:/host/etc/group:ro
            # 将主机的 /proc 目录以只读方式挂载到容器中，用于监控系统进程和内核信息
            - /proc:/host/proc:ro
            # 将主机的 /sys 目录以只读方式挂载到容器中，用于监控系统硬件和设备信息
            - /sys:/host/sys:ro
```

## 3、访问

1. 访问：[http://127.0.0.1:19999](http://127.0.0.1:19999)


# 1002、homeassistant 智能家居平台

> 1. 项目 github：https://github.com/home-assistant/core
> 2. dockerHub 地址：https://hub.docker.com/r/homeassistant/home-assistant

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111608.png)

4. 正常的话，已发现中就会有 Network UPS Tools (NUT)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111622.png)

5. 点击添加，输入完参数后点击提交即可
	1. 主机：`172.17.0.1`
	2. 端口：`3493`
	3. 用户名：ups 的用户名
	4. 密码：ups 的密码

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111640.png)

6. 添加成功后，会显示在设备中

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111736.png)

7. 点击概览，也会显示 ups 的信息

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111705.png)

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
	2. 本地  v2.0.1 版下载：[hacs.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2Fhacs.zip)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111816.png)

2. 在挂载目录 `/home/docker/docker/volumes/homeassistant/config` 下再创建 `custom_components` 目录，将下载的文件上传到此目录中：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111831.png)

3. 解压 hacs.zip

```shell
unzip hacs.zip -d hacs/
```

4. 解压完毕后，重启容器，进入 homeassistant 管理页面，点击设置 -> 设备与服务

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111847.png)

5. 点击添加集成：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111857.png)

6. 搜索 `hacs`，选择后勾选所有选项，然后点击提交：

![|499](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111908.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111918.png)

7. 等待一段时间后，提示需要点击中间的链接跳转到 GitHub 进行验证，复制下面验证码填入 GitHub 进行验证

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111932.png)

8. 验证完成后，刷新一下，左侧出现 HACS 选项，进入即可安装各种插件与设备链接

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108111944.png)

## 7、集成米家

> 需完成上面的集成 hacs

1. 在 hacs 中搜索 `Xiaomi Miot Auto`，进入后点击 download

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108112003.png)

2. 下载完成后，点击设置 -> 小米模块，会提示需要重启容器

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108112017.png)

3. 重新容器后，进入设置 -> 添加集成，搜索 `xiaomi`，选择 `Xiaomi Miot Auto`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108112031.png)

4. 选择账号集成，再选择排除模式，不选择任何设备，点击提交，就可以成功添加

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250108112043.png)
