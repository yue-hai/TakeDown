# 1、openJdk

## 1、openJdk 21

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/services/backend/yuehai-tool`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 8080:8080 \
-e TZ=Asia/Shanghai \
-v /vol1/1000/docker/services/backend/yuehai-tool:/container/path \
--network yuehai-net \
--restart=unless-stopped \
--name code-java-yuehai-tool \
openjdk:21 \
java -jar /container/path/tool-1.0-SNAPSHOT-jar-with-dependencies.jar
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-java-yuehai-tool 的服务
    code-java-yuehai-tool:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: openjdk:21
        # 设置容器的固定名称，方便识别和管理
        container_name: code-java-yuehai-tool
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 启用特权模式
        privileged: true
        # 定义端口映射规则
        ports:
            # Java 应用监听的端口
            - "8080:8080"
        # 定义环境变量
        environment:
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则
        volumes:
            # jar 包目录
            - /vol1/1000/docker/services/backend/yuehai-tool:/container/path
        # 指定容器启动时执行的命令：运行指定的 Jar 文件
        command: java -jar /container/path/tool-1.0-SNAPSHOT-jar-with-dependencies.jar
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


## 2、openJdk 21 使用 shell 脚本执行多个 jar 程序

1. 创建映射目录，并将 jar 包上传到指定目录：
	1. 程序 1 的目录：`/vol1/1000/docker/services/backend/yuehai-tool/01`
	2. 程序 2 的目录：`/vol1/1000/docker/services/backend/yuehai-tool/02`
2. 进入 `/vol1/1000/docker/services/backend/yuehai-tool` 目录，创建 `run_jar.sh` 文件，并写入下面的内容：

```shell
#!/bin/bash

# 容器内映射目录所在的路径
main_path="/container/path"

start_app() {
    local app_path=$1 # 程序所在的路径
    local app_name=$2 # 程序的名称
    local log_name=$3 # 程序日志的名称
    local background=$4  # 用于判断是否需要在后台运行

    # yes 便是需要在后台运行
    if [ "$background" == "yes" ]; then
        java -jar "${app_path}/${app_name}" > "${app_path}/${log_name}" 2>&1 &
    else
        java -jar "${app_path}/${app_name}" > "${app_path}/${log_name}" 2>&1
    fi
}

# 01 程序，后台
start_app "${main_path}/01" \
          "01.jar" \
          "01.log" \
          "yes"

# 02 程序，前台
start_app "${main_path}/02" \
          "02.jar" \
          "02.log" \
          "no"
```

3. 使用 docker run 部署：

```shell
docker run -d \
-p 8080-8081:8080-8081 \
-e TZ=Asia/Shanghai \
-v /vol1/1000/docker/services/backend/yuehai-tool:/container/path \
--network yuehai-net \
--privileged=true \
--restart=unless-stopped \
--name code-java \
openjdk:21 \
/container/path/run_jar.sh
```

4. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-java 的服务
    code-java:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: openjdk:21
        # 设置容器的固定名称，方便识别和管理
        container_name: code-java
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 启用特权模式
        privileged: true
        # 定义端口映射规则
        ports:
            # 将主机的 8080-8081 端口范围映射到容器的 8080-8081 端口范围
            - "8080-8081:8080-8081"
        # 定义环境变量
        environment:
            # 设置容器的时区为亚洲/上海
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则 (格式：主机路径:容器路径)
        volumes:
            # jar 包目录
            - /vol1/1000/docker/services/backend/openjdk/yuehai-tool:/container/path
        # 指定容器启动时执行的命令：运行位于挂载卷中的启动脚本
        command: /container/path/run_jar.sh
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


# 2、tomcat

## 1、首次创建容器

1. 使用 docker 部署：

```shell
docker run -d \
-p 8080:8080 \
--name code-tomcat9 \
tomcat:jre21
```

## 2、复制数据，并设置映射目录

1. 在宿主机创建目录：`/home/docker/docker/volumes/tomcat/tomcat9`
2. 将容器内的 `/usr/local/tomcat` 目录复制到宿主机上：

```shell
docker cp code-tomcat9:/usr/local/tomcat/ /home/docker/docker/volumes/tomcat/tomcat9/
```

![](attachments/Pasted%20image%2020250107163352.png)

3. 停止并删除容器：

```shell
# 停止：
docker stop code-tomcat9

# 删除：
docker rm code-tomcat9
```

4. 使用 docker run 部署，重新启动容器，并设置映射目录：

```shell
docker run -d \
-p 8080:8080 \
-v /home/docker/docker/volumes/tomcat/tomcat9/tomcat:/usr/local/tomcat \
--network yuehai-net \
--restart=unless-stopped
--name code-tomcat9 \
tomcat:jre21
```

5. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-tomcat9 的服务
    code-tomcat9:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: tomcat:jre21
        # 设置容器的固定名称，方便识别和管理
        container_name: code-tomcat9
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Tomcat 的默认 HTTP 端口
            - "8080:8080"
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /home/docker/docker/volumes/tomcat/tomcat9/tomcat:/usr/local/tomcat
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

1. 访问测试：[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## 4、显示 404 的解决方法

1. 若是显示 404，则查看防火墙 10100 端口；若端口已开放，则：
2. 查看映射目录的 `webapps` 和 `webapps.dist` 目录；若 `webapps` 为空 `webapps.dist` 不为空

![](attachments/Pasted%20image%2020250107163443.png)

![](attachments/Pasted%20image%2020250107163500.png)

3. 删除 `webapps` 目录，将 `webapps.dist` 目录重命名为 `webapps`

![](attachments/Pasted%20image%2020250107163523.png)

![](attachments/Pasted%20image%2020250107163538.png)

4. 再次访问：[http://172.17.0.1:8080/](http://172.17.0.1:8080/)

![|700](attachments/Pasted%20image%2020250107163621.png)


# 10、pgadmin4 PostgreSQL 的 web 管理工具


> 1. 项目 github：https://github.com/pgadmin-org/pgadmin4
> 2. dockerHub 地址：https://hub.docker.com/r/dpage/pgadmin4

## 1、介绍

1. dpage/pgadmin4 是 pgAdmin 4 的官方 Docker 镜像。pgAdmin 4 本身是 PostgreSQL 最流行和功能最全面的开源管理和开发平台，它提供了一个基于 Web 的用户界面，允许用户通过浏览器与 PostgreSQL 数据库进行交互
2. 它的主要特点包括：
	1. 现代化的 Web 用户界面：pgAdmin 4 提供了一个美观且响应迅速的 Web 界面，取代了旧版 pgAdmin III 的桌面应用程序形态，方便用户随时随地通过浏览器访问和管理数据库
	2. 全面的数据库对象管理：提供了一个直观的对象浏览器，可以轻松地查看、创建、修改和删除数据库、模式、表、视图、函数、触发器等各种数据库对象
	3. 强大的 SQL 开发工具：内置了一个功能丰富的 SQL 编辑器，支持语法高亮、代码自动完成、SQL 代码格式化、查询历史记录，以及一个图形化的查询构建器，帮助用户编写和执行 SQL 查询
	4. 图形化查询计划分析器 (Explain)：可以显示和分析 SQL 查询的执行计划，帮助开发者理解查询的性能瓶颈并进行优化
	5. 服务器监控仪表盘：提供实时的服务器状态信息，包括会话、锁、预备事务以及 CPU、内存、磁盘I/O等系统资源的使用情况
	6. 数据导入/导出与备份/恢复：支持以多种格式（如 CSV、Text、SQL）导入和导出数据，并提供了方便的备份和恢复工具界面
	7. 通过 Docker 轻松部署：dpage/pgadmin4 Docker 镜像使得部署和运行 pgAdmin 4 变得非常简单和快捷，无需在宿主机上进行复杂的安装和配置

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/services/frontend/pgadmin4/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 80:80 \
-e "PGADMIN_DEFAULT_EMAIL=xxx@qq.com" \
-e "PGADMIN_DEFAULT_PASSWORD=xxx" \
-v /vol1/1000/docker/services/frontend/pgadmin4/data:/var/lib/pgadmin \
--network yuehai-net \
--restart=unless-stopped \
--name code-pgadmin4 \
dpage/pgadmin4:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-pgadmin4 的服务
    code-pgadmin4:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: dpage/pgadmin4:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: code-pgadmin4
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # pgAdmin 4 默认的 Web 访问端口
            - "80:80"
        # 定义环境变量
        environment:
            # 设置 pgAdmin 4 初始登录的默认邮箱地址
            - PGADMIN_DEFAULT_EMAIL=xxx0@qq.com
            # 设置 pgAdmin 4 初始登录的默认密码
            - PGADMIN_DEFAULT_PASSWORD=xxx
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/services/frontend/pgadmin4/data:/var/lib/pgadmin
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

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)
2. 输入上面设定的账号密码即可

## 5、使用 nginx 代理

1. 基础代理部分：

![](attachments/Pasted%20image%2020251202165648.png)

2. 高级自定义 Nginx 配置填入以下内容，注意修改转发地址：

![](attachments/Pasted%20image%2020251202164206.png)

```nginx
# 定义一个 location 块，匹配所有进入的请求 (/)
location / {
  # 使用 Docker 内部 DNS(127.0.0.11)解析器，可以使用他通过容器名字找到对应的动态 IP 地址
  # valid=30s 表示每 30 秒重新解析一次 IP，这样即使服务重启换了 IP 也能自动恢复
  resolver 127.0.0.11 valid=30s;
  
  # 设置真实的容器名和端口
  set $upstream_proto http;
  set $upstream_host code-pgadmin4;
  set $upstream_port 80;
  # 使用变量请求代理到指定服务，所有匹配此 location 块的请求都将被转发到指定地址
  # Nginx 看到变量时，不会在启动时检查域名，而是在有人访问网站时才去解析
  proxy_pass $upstream_proto://$upstream_host:$upstream_port;
  
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

  # 强制使用 HTTP/1.1
  # Nginx 代理默认使用 HTTP/1.0，而 WebSocket 协议强制要求 HTTP/1.1，长连接 (Keep-Alive) 也需要它
  proxy_http_version 1.1;
  # 传递 Upgrade 头部
  # WebSocket 连接建立时，客户端会发送 Upgrade: websocket 头，必须透传给后端，否则后端不知道要升级协议
  proxy_set_header Upgrade $http_upgrade;
  # 设置 Connection 头部
  # 告诉后端这是一个需要升级协议的连接，通常设置为 upgrade
  proxy_set_header Connection "upgrade";

  # 关闭代理重定向处理，off 表示 Nginx 不会修改后端服务器返回的 Location 和 Refresh 头部中的 URL
  # 这通常在后端应用自己能正确处理重定向 URL 时使用
  proxy_redirect off;
  # 设置客户端请求体的最大允许大小，一般推荐设置为 20000m (即 20000MB 或约 19.5GB)，以支持大文件上传
  # 如果上传的文件超过此大小，Nginx 会返回 "413 Request Entity Too Large" 错误
  client_max_body_size 20000m;
}
```


# 11、Hoppscotch API 调用工具

> 1. 项目 github：https://github.com/hoppscotch/hoppscotch
> 2. dockerHub 地址：https://hub.docker.com/r/hoppscotch/hoppscotch

## 1、介绍

1. 一款完全开源、基于 Web 的 API 测试工具，响应速度极快，界面简洁美观
2. 无需安装：作为一款 Web 应用，您可以直接在浏览器中使用，非常轻量
3. 功能全面：支持 REST、GraphQL 和 WebSocket 等多种协议
4. 易于迁移：支持导入 Postman 的数据集合，方便快速上手
5. PWA 支持：可以作为渐进式 Web 应用（PWA）安装到桌面，实现类似原生应用的体验，同时保持低资源占用

## 2、docker 部署

1. 在宿主机创建目录，作为配置文件存放目录：`/vol1/1000/docker/services/frontend/hoppscotch`
2. 在该目录下创建配置文件：`hoppscotch.env`，并输入以下内容，需自己对应修改

```env
#----------------------- Backend Config (后端配置) ------------------------------#

# 数据库配置
# 格式: postgresql://<用户>:<密码>@<主机服务名>:<端口>/<数据库名>
DATABASE_URL="postgresql://xxx@xxx:5432/xxx"

# 认证令牌配置
# JWT 密钥，用于用户会话安全，请务必保密
JWT_SECRET="xxx"
# 会话密钥，同样需要保密
SESSION_SECRET="xxx"
# 数据加密密钥，用于加密数据库中的敏感信息
DATA_ENCRYPTION_KEY="xxx"
# 令牌盐复杂度，默认值通常即可
TOKEN_SALT_COMPLEXITY=12
# 令牌有效期（毫秒），默认值通常即可
MAGIC_LINK_TOKEN_VALIDITY=900000     # 15分钟
REFRESH_TOKEN_VALIDITY=2592000000    # 30天
ACCESS_TOKEN_VALIDITY=900000         # 15分钟

# 应用域名配置
# 访问 Hoppscotch 的公网域名
REDIRECT_URL=https://xxx
# 允许的请求来源列表，多个域名用逗号分隔
WHITELISTED_ORIGINS=https://xxx,https://xxx/admin,https://xxx/backend
# 允许的重定向域名列表，多个域名用逗号分隔
VITE_ALLOWED_AUTH_PROVIDERS=EMAIL

# 第三方登录配置，可选，如不需要可留空
GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""
GITHUB_CLIENT_ID=""
GITHUB_CLIENT_SECRET=""
MICROSOFT_CLIENT_ID=""
MICROSOFT_CLIENT_SECRET=""

# 邮件服务配置，填写自己的 SMTP 服务信息，这是实现邮箱登录功能的关键，必须填写
# 格式: smtp://<用户名>:<密码>@<SMTP服务器地址>:<端口>
MAILER_SMTP_URL="smtp://xxx:xxx@smtp.qq.com:587"
# 希望邮件中显示的发件人地址
MAILER_ADDRESS_FROM="xxx"

# 速率限制配置
RATE_LIMIT_TTL=60 # 单位: 秒
RATE_LIMIT_MAX=100 # 每个 IP 每分钟的最大请求数

#----------------------- Frontend Config (前端配置) ------------------------------#

# 基础 URL 配置
VITE_BASE_URL=https://xxx
VITE_SHORTCODE_BASE_URL=https://xxx
VITE_ADMIN_URL=https://xxx/admin

# 后端接口 URL 配置，这里会告诉前端界面去哪里找后端服务
VITE_BACKEND_GQL_URL=https://xxx/backend/graphql
VITE_BACKEND_WS_URL=wss://xxx/backend/graphql
VITE_BACKEND_API_URL=https://xxx/backend/v1

# 服务条款链接，可选
VITE_APP_TOS_LINK=https://docs.hoppscotch.io/support/terms
VITE_APP_PRIVACY_POLICY_LINK=https://docs.hoppscotch.io/support/privacy

# 子路径访问模式，必须为 true
# 这是为了让 hoppscotch/hoppscotch 一体化镜像能正常工作
ENABLE_SUBPATH_BASED_ACCESS=true
```

3. 使用 docker run 部署数据库迁移服务：

```shell
docker run --rm \
--env-file /vol1/1000/docker/services/frontend/hoppscotch/hoppscotch.env \
--entrypoint sh \
--network yuehai-net \
--name hoppscotch-migrate \
hoppscotch/hoppscotch:latest \
-c "npx prisma migrate deploy"
```

4. 使用 docker run 部署 Hoppscotch 主服务：

```shell
docker run -d \
-p 80:80 \
--env-file /vol1/1000/docker/services/frontend/hoppscotch/hoppscotch.env \
--network yuehai-net \
--restart=unless-stopped \
--name hoppscotch-app \
hoppscotch/hoppscotch:latest
```

5. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 数据库迁移服务，用于在启动主应用前执行数据库迁移、初始化等任务
    hoppscotch-migrate:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: hoppscotch/hoppscotch:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: hoppscotch-migrate
        # 定义容器的重启策略：运行一次就退出
        restart: "no"
        # 指定外部环境变量文件的路径。容器将从这个文件中加载所有配置
        env_file:
            - ./hoppscotch.env
        # 覆盖镜像的默认入口点。这里设置为 sh，意味着容器启动后会运行一个 shell 解释器
        entrypoint: sh
        # 指定容器启动时执行的命令：执行数据库结构同步
        command: -c "npx prisma migrate deploy"
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络
            - yuehai-net
    
    # Hoppscotch 主服务，用于提供 API 测试和管理功能
    hoppscotch:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: hoppscotch/hoppscotch:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: hoppscotch-app
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Web 访问端口
            - "80:80"
        # 指定外部环境变量文件的路径。容器将从这个文件中加载所有配置
        env_file:
            - ./hoppscotch.env
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络
            - yuehai-net
        # 定义服务间的依赖关系
        depends_on:
            # 此服务依赖于 hoppscotch-migrate 服务
            hoppscotch-migrate:
                # 启动条件：只有当 hoppscotch-migrate 服务成功执行完毕并退出（退出码为0）后，此服务才会开始启动
                condition: service_completed_successfully

# 在文件末尾定义此 Compose 文件中使用的所有网络
networks:
    # 定义一个名为 yuehai-net 的网络配置
    yuehai-net:
        # 将此网络声明为外部网络
        # external: true 的意思是：不要创建这个网络，而是去使用一个已经存在的、名字完全相同的网络
        external: true
```

## 3、访问

1. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)，可进入匿名首页，此时可临时使用，数据不会保存
2. 访问：[http://127.0.0.1:80/admin](http://127.0.0.1:80/admin)，进入管理员后台，初次访问会进行初始化设置
3. 选择 SMTP

![](attachments/Pasted%20image%2020251128161348.png)

4. 输入项目发送邮件的邮箱地址和 SMTP 连接信息，输入的信息和配置文件上的一样，这个邮箱会作为初始的管理员

![](attachments/Pasted%20image%2020251128161417.png)

5. 配置后成功，等待重启，
6. 重启完成后，输入邮箱进行登录，会收到一条邮件，点击邮件中的地址即可登录，登录成功后进入管理员后台，可进行设置
7. 访问：[http://127.0.0.1:80](http://127.0.0.1:80)，再次进入首页，此时可正常使用，

![](attachments/Pasted%20image%2020251128161720.png)

## 4、问题记录

### ①、无法继承父集合参数设置

#### Ⅰ、报错现象

1. 父目录中设置了请求头、授权等信息

![](attachments/Pasted%20image%2020251128162542.png)

2. 目录中的接口也设置了继承父目录中设置，但是实际请求中并没有携带这些参数

![](attachments/Pasted%20image%2020251128162605.png)

#### Ⅱ、原因

1. 不知道

#### Ⅲ、解决

1. 将这个接口移动到其他目录，再移动回来就可以了

### ②、

# 20、postgres 数据库

## 1、介绍

1. PostgreSQL (通常简称为 Postgres) 是一个功能强大、开源的对象关系型数据库系统 (ORDBMS)。它拥有超过 35 年的活跃开发历史，并在可靠性、功能健壮性和性能方面赢得了良好声誉
2. 它的主要特点包括：
	1. 高度的 SQL 标准兼容性：严格遵循 SQL 标准，并支持众多现代 SQL 特性
	2. 强大的数据类型支持：除了常见的数字、字符串、日期/时间类型外，还支持 JSON/JSONB、XML、数组、范围类型、地理空间数据 (通过 PostGIS 扩展) 等复杂数据类型
	3. 卓越的扩展性：用户可以定义自己的数据类型、函数、操作符、聚合函数、索引方法和过程语言 (如 PL/pgSQL, PL/Python, PL/Perl 等)
	4. 并发控制与事务处理：采用多版本并发控制 (MVCC) 技术，有效处理高并发读写操作，并提供完整的 ACID (原子性、一致性、隔离性、持久性) 事务保证
	5. 可靠性与灾难恢复：支持预写式日志 (WAL)、时间点恢复 (PITR)、流复制和逻辑复制等多种高可用和数据备份恢复机制
	6. 丰富的索引选项：支持 B-tree、Hash、GiST、SP-GiST、GIN 和 BRIN 等多种索引类型，以适应不同的查询负载
	7. 活跃的社区和生态系统：拥有一个庞大且活跃的全球社区，提供丰富的文档、工具和第三方扩展支持

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置和数据目录：`/vol1/1000/docker/services/databases/postgres/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 5432:5432 \
-e POSTGRES_USER=xxx \
-e POSTGRES_PASSWORD=xxx \
-v /vol1/1000/docker/services/databases/postgres/data:/var/lib/postgresql/data \
--network yuehai-net \
--restart=unless-stopped \
--name code-postgres \
postgres:latest
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-postgres 的服务
    code-postgres:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: postgres:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: code-postgres
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # PostgreSQL 的默认数据库端口
            - "5432:5432"
        # 定义环境变量
        environment:
            # 设置 PostgreSQL 的默认用户名
            - POSTGRES_USER=xxx
            # 设置 PostgreSQL 的默认用户密码 (警告：直接在 yml 中写密码不安全，建议使用 .env 文件或 Docker Secrets)
            - POSTGRES_PASSWORD=xxx
        # 定义数据卷挂载规则
        volumes:
            # 数据目录
            - /vol1/1000/docker/services/databases/postgres/data:/var/lib/postgresql/data
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

1. 我这里使用 heidisql 进行连接，其他不再做说明，这里要注意一下<font color="#00b0f0">蓝色箭头</font>数据库这里
2. 使用 heidisql 连接 postgres 时，每次只能连接一个数据库，如果不指定数据库名称，默认连接到 `postgres` 数据库，想要连接到其他数据库，这里一定要指定一个数据库的名，比如：`test`

![](attachments/Pasted%20image%2020250121105335.png)

3. 连接进去后，可以使用以下命令查询当前连接的数据库名称，确定是不是想要连接的数据库

```sql
SELECT current_database();
```

4. 在 heidisql 中，新创建的数据库时不会显示的，只能在连接数据库时选择新建的数据库，可以使用以下命令查询 PostgreSQL 中所有数据库的名称

```sql
SELECT datname FROM pg_database;
```

5. 使用以下命令建一个新的数据库：

```
CREATE DATABASE my_database;
```

6. 可以使用以下命令建一个新的架构：

```sql
CREATE SCHEMA schema_name;
```

7. 不想使用命令，也可以使用 idea 自带的数据库管理工具来创建：

![](attachments/Pasted%20image%2020250121105443.png)

## 4、从 mysql 迁移到 postgres

1. 使用的工具为 pgloader，使用 docker 的方式
2. 在宿主机创建目录：
	1. 迁移脚本目录：`/home/docker/docker/volumes/pgloader/config`
3. 在 `/home/docker/docker/volumes/pgloader/config` 中创建脚本文件 `load_command.load`，并输入以下内容：
	1. 可设置多组，在最后追加即可

```sql
LOAD DATABASE
	-- 从 MySQL 数据库中导入数据
    -- 该语句定义了数据源为 MySQL 数据库，其中包括用户、密码、主机和数据库名称
    FROM mysql://mysql_user:mysql_password@mysql_host/nextcloud

    -- 将数据导入到 PostgreSQL 数据库
    -- 定义目标数据库为 PostgreSQL，目标数据库信息包括用户、密码、主机和数据库名称
    INTO postgresql://postgre_user:postgre_password@postgre_host/yan

-- 指定导入操作的一些选项
WITH 
    -- 包括丢弃现有数据库的结构（如表、索引等），以确保新的数据结构能完全匹配源数据库
    include drop, 
    -- 创建表结构，将源数据库中的表结构复制到目标数据库中
    create tables, 
    -- 不截断表，这表示不会清空现有表中的数据
    no truncate,
    -- 创建表时一并创建对应的索引，以提升查询性能
    create indexes, 
    -- 重置序列，确保主键序列等能正确从导入的数据中继续
    reset sequences, 
    -- 在目标数据库中创建外键约束，以确保数据完整性
    foreign keys

-- 设置数据库导入时的内存使用参数
SET 
    -- 设置用于排序操作的内存大小（如索引创建等），此处设置为 16MB
    work_mem to '16MB', 
    -- 设置维护任务（如索引重建、分析）的内存大小，此处设置为 512MB
    maintenance_work_mem to '512 MB';
```

4. 使用 docker 部署：
	1. `--rm`：在容器运行结束后自动删除容器
	2. `-v`：指定挂载目录，使其可以执行迁移脚本
	3. `pgloader /pgloader/load_command.load`：在容器启动后，执行该迁移脚本

```shell
docker run --rm \
-v /home/docker/docker/volumes/pgloader/config:/pgloader \
--name pgloader \
dimitri/pgloader \
pgloader /pgloader/load_command.load
```

5. 执行成功的情况：

```shell
docker@yuehai:~/docker/volumes/pgloader/config$ docker run --rm -v /home/docker/docker/volumes/pgloader/config:/pgloader --name pgloader dimitri/pgloader pgloader /pgloader/load_command.load
2025-01-21T02:42:07.008000Z LOG pgloader version "3.6.7~devel"
2025-01-21T02:42:07.012000Z LOG Data errors in '/tmp/pgloader/'
2025-01-21T02:42:07.012000Z LOG Parsing commands from file #P"/pgloader/load_command.load"
2025-01-21T02:42:07.112005Z LOG Migrating from #<MYSQL-CONNECTION mysql://
2025-01-21T02:42:07.112005Z LOG Migrating into #<PGSQL-CONNECTION pgsql://
2025-01-21T02:42:08.608060Z LOG report summary reset
                              table name     errors       rows      bytes      total time
----------------------------------------  ---------  ---------  ---------  --------------
                         fetch meta data          0         37                     0.216s
                          Create Schemas          0          0                     0.004s
                        Create SQL Types          0          0                     0.008s
                           Create tables          0         24                     0.080s
                          Set Table OIDs          0         12                     0.008s
----------------------------------------  ---------  ---------  ---------  --------------
     y_chat_nacos_config.his_config_info          0         21    13.5 kB          0.124s
         y_chat_nacos_config.config_info          0         14     9.6 kB          0.116s
               y_chat_nacos_config.roles          0          4     0.1 kB          0.088s
         y_chat_nacos_config.permissions          0          4     0.2 kB          0.120s
               y_chat_nacos_config.users          0          4     0.3 kB          0.096s
         y_chat_nacos_config.tenant_info          0          4     0.5 kB          0.084s
    y_chat_nacos_config.config_info_aggr          0          0                     0.240s
    y_chat_nacos_config.config_info_beta          0          0                     0.112s
y_chat_nacos_config.config_tags_relation          0          0                     0.100s
     y_chat_nacos_config.tenant_capacity          0          0                     0.120s
     y_chat_nacos_config.config_info_tag          0          0                     0.088s
      y_chat_nacos_config.group_capacity          0          0                     0.088s
----------------------------------------  ---------  ---------  ---------  --------------
                 COPY Threads Completion          0          4                     0.644s
                          Create Indexes          0         25                     0.236s
                  Index Build Completion          0         25                     0.052s
                         Reset Sequences          0          9                     0.048s
                            Primary Keys          0         10                     0.024s
                     Create Foreign Keys          0          0                     0.000s
                         Create Triggers          0          0                     0.004s
                        Install Comments          0         88                     0.248s
----------------------------------------  ---------  ---------  ---------  --------------
                       Total import time          ✓         51    24.1 kB          1.256s
docker@yuehai:~/docker/volumes/pgloader/config$ 
```

6. 如果有报错，继续往下看

### ①、Condition QMYND:MYSQL-UNSUPPORTED-AUTHENTICATION was signalled.

#### Ⅰ、报错现象

```shell
docker@yuehai:~/docker/volumes/pgloader/config$ docker run --rm -v /home/docker/docker/volumes/pgloader/config:/pgloader --name pgloader dimitri/pgloader pgloader /pgloader/load_command.cmd
2025-01-21T01:40:56.012000Z LOG pgloader version "3.6.7~devel"
2025-01-21T01:40:56.096003Z LOG Migrating from #<MYSQL-CONNECTION mysql://
2025-01-21T01:40:56.096003Z LOG Migrating into #<PGSQL-CONNECTION pgsql://
2025-01-21T01:40:56.316011Z ERROR mysql: Failed to connect to mysql at "127.0.0.1" (port 3306) as user "admin": Condition QMYND:MYSQL-UNSUPPORTED-AUTHENTICATION was signalled.
2025-01-21T01:40:56.316011Z LOG report summary reset
       table name     errors       rows      bytes      total time
-----------------  ---------  ---------  ---------  --------------
  fetch meta data          0          0                     0.000s
-----------------  ---------  ---------  ---------  --------------
-----------------  ---------  ---------  ---------  --------------
docker@yuehai:~/docker/volumes/pgloader/config$
```

#### Ⅱ、原因

1. pgloader 不支持 caching_sha2_password 的连接方式，修改 mysql 即可

#### Ⅲ、解决

1. 在 mysql 的配置文件 `/etc/my.cnf` 中增加：

```shell
default-authentication-plugin=mysql_native_password
```

2. 修改完毕后，重启 mysql 即可


# 21、pgvector 带向量插件的 postgres 数据库

## 1、介绍

1. pgvector/pgvector (通常简称为 pgvector) 是一个针对 PostgreSQL 的开源扩展，它使得 PostgreSQL 数据库能够高效地存储和搜索向量嵌入 (vector embeddings)。这对于构建涉及机器学习、人工智能、相似性搜索和推荐系统的应用程序至关重要。
2. 它的主要特点包括：
	1. 向量数据类型支持：引入了一个新的 vector 数据类型，可以直接在 PostgreSQL 中存储高维浮点数向量
	2. 精确相似性搜索：支持使用 L2 距离 (欧氏距离)、内积 (inner product) 和余弦相似度 (cosine similarity/distance) 来计算向量之间的相似性，并进行精确的 k-最近邻 (k-NN) 搜索
	3. 近似最近邻 (ANN) 搜索：为了加速大规模向量集的搜索，pgvector 支持创建近似最近邻 (ANN) 索引，如 IVFFlat 和 HNSW (Hierarchical Navigable Small World)，可以在保证召回率的同时大幅提升查询速度
	4. 与 PostgreSQL 无缝集成：作为 PostgreSQL 扩展，pgvector 可以与 PostgreSQL 的所有现有功能完美结合，包括事务、索引、备份、复制以及丰富的 SQL 查询能力。这意味着您可以将向量数据与其他结构化数据存储在同一个数据库中，并进行复杂的联合查询
	5. 易用性：提供了简单直观的 SQL 接口来创建向量列、插入向量数据和执行相似性搜索
	6. 多语言客户端支持：由于它建立在 PostgreSQL 之上，任何支持 PostgreSQL 的编程语言和客户端库都可以与 pgvector 交互

## 2、docker 部署 

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置和数据目录：`/vol1/1000/docker/services/databases/postgres-pgvector/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 5432:5432 \
-e POSTGRES_USER=xxx \
-e POSTGRES_PASSWORD=xxx \
-v /vol1/1000/docker/services/databases/postgres-pgvector/data:/var/lib/postgresql/data \
--network yuehai-net \
--restart=unless-stopped \
--name code-postgres-pgvector \
pgvector/pgvector:0.8.0-pg17
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 pgvector-db 的服务
    pgvector-db:
        # 指定该服务使用的 Docker 镜像及其标签（版本），因为没有 latest 标签，所以指定 0.8.0-pg17
        image: pgvector/pgvector:0.8.0-pg17
        # 设置容器的固定名称，方便识别和管理
        container_name: code-postgres-pgvector
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # PostgreSQL 的默认数据库端口
            - "5432:5432"
        # 定义环境变量
        environment:
            # 设置 PostgreSQL 的默认用户名
            - POSTGRES_USER=xxx
            # 设置 PostgreSQL 的默认用户密码 (警告：直接在 yml 中写密码不安全)
            - POSTGRES_PASSWORD=xxx
        # 定义数据卷挂载规则 (格式：主机路径:容器路径)
        volumes:
            # 数据目录
            - /vol1/1000/docker/services/databases/postgres-pgvector/data:/var/lib/postgresql/data
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

4. 查看 pgvector 是否开启：

```sql
SELECT * FROM pg_extension WHERE extname = 'vector';

SELECT extname FROM pg_extension;
```

5. 如果执行第一条命令后，结果区域显示了一行或多行数据（通常会显示 vector 的相关信息，如 extname, extowner, extversion 等），那么说明 pgvector 扩展已经在当前选择的数据库中启用了。如果执行第一条命令后，结果区域为空（或者执行第二条命令后，结果列表中没有 vector），那么说明 pgvector 尚未在当前数据库中启用
6. 如果未在特定数据库中启用，可以执行以下命令来启用它：

```sql
CREATE EXTENSION vector;
```

7. 再次执行第一条命令查询，如果结果中显示 `vector` 则代表启用成功

| extname |
| ------- |
| plpgsql |
| vector  |

8. 在当前数据库中移除 pgvector 扩展，执行以下命令：

```sql
DROP EXTENSION vector;
```

9. 需要注意的是，如果数据库中有任何对象（例如表中的列、索引、函数等）正在使用 pgvector 提供的功能（比如 vector 数据类型），那么直接执行 `DROP EXTENSION vector;` 将会失败，并报错提示存在依赖关系。这是为了防止意外破坏数据库


# 22、mysql

## 1、介绍

1. MySQL 是世界上最流行的开源关系型数据库管理系统 (RDBMS) 之一。它以其易用性、可靠性和高性能而闻名，被广泛应用于各种规模的应用程序，尤其是 Web 应用程序开发。MySQL 最初由瑞典公司 MySQL AB 开发，目前由 Oracle 公司拥有和赞助
2. 它的主要特点包括：
	1. 广泛的流行度和社区支持：作为最受欢迎的开源数据库之一，MySQL 拥有庞大而活跃的用户社区，提供了丰富的文档、教程和第三方工具
	2. 跨平台性：MySQL 可以在多种操作系统上运行，包括 Linux、Windows、macOS 等，具有良好的可移植性
	3. 多种存储引擎：支持多种存储引擎，最著名的是 InnoDB 和 MyISAM。InnoDB 提供事务安全 (ACID 兼容)、行级锁定和外键约束，而 MyISAM 则在某些只读或读密集型场景下可能提供更高的性能
	4. 复制和高可用性：支持多种复制方式（如主从复制、半同步复制、组复制），可以用于数据备份、负载均衡和实现高可用性解决方案
	5. 安全特性：提供了强大的安全功能，包括基于权限的用户账户管理、SSL 加密连接、数据加密等，以保护数据安全
	6. 易用性和丰富的工具：MySQL 易于安装、配置和使用。有大量图形化管理工具（如 phpMyAdmin, MySQL Workbench）和命令行工具可供选择，方便数据库的管理和开发
	7. 可扩展性和性能：能够处理大量数据和高并发连接，通过适当的配置和优化，可以满足不同应用场景的性能需求


## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/mysql/conf/`
	2. 数据目录：`/home/docker/docker/volumes/mysql/data/`
	3. 日志目录：`/home/docker/docker/volumes/mysql/log/`
2. 在 `/home/docker/docker/volumes/mysql/conf/` 目录下创建配置文件  `my.cnf`：

```shell
cd /home/docker/docker/volumes/mysql/conf/

nano my.cnf
```

3. 填入以下配置：

```shell
[client]
#设置客户端默认字符集utf8mb4
default-character-set=utf8mb4
[mysql]
#设置服务器默认字符集为utf8mb4
default-character-set=utf8mb4
[mysqld]
#配置服务器的服务号，具备日后需要集群做准备
server-id = 1
#开启MySQL数据库的二进制日志，用于记录用户对数据库的操作SQL语句，具备日后需要集群做准备
log-bin=mysql-bin
#设置清理超过30天的日志，以免日志堆积造过多成服务器内存爆满。2592000秒等于30天的秒数
binlog_expire_logs_seconds = 2592000
#解决MySQL8.0版本GROUP BY问题
sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'
#允许最大的连接数
max_connections=1000
# 禁用符号链接以防止各种安全风险
symbolic-links=0
# 设置东八区时区
default-time_zone = '+8:00'
```

4. 使用 docker run 部署：

```shell
docker run -d \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=xxx \
-v /home/docker/docker/volumes/mysql/log:/var/log/mysql \
-v /home/docker/docker/volumes/mysql/data:/var/lib/mysql \
-v /home/docker/docker/volumes/mysql/conf/my.cnf:/etc/mysql/my.cnf \
--network yuehai-net \
--restart=unless-stopped \
--name code-mysql \
mysql:8.2.0
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-mysql 的服务
    code-mysql:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: mysql:8.2.0
        # 设置容器的固定名称，方便识别和管理
        container_name: code-mysql
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # MySQL 的默认端口
            - "3306:3306"
        # 定义环境变量
        environment:
            # 设置 MySQL root 用户的密码
            - MYSQL_ROOT_PASSWORD=xxx
        # 定义数据卷挂载规则
        volumes:
            # 日志文件
            - /home/docker/docker/volumes/mysql/log:/var/log/mysql
            # 数据库文件 (非常重要
            - /home/docker/docker/volumes/mysql/data:/var/lib/mysql
            # 配置文件
            - /home/docker/docker/volumes/mysql/conf/my.cnf:/etc/mysql/my.cnf
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

1. 使用 Navicat 连接

![|700](attachments/Pasted%20image%2020250107164736.png)

## 4、插入中文报错

1. 进入容器，查看编码

```shell
docker@yuehai:~$ docker exec -it bfab03cebaac bash
bash-4.4# mysql -u root -p   
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 8.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW VARIABLES LIKE 'character%';
+--------------------------+--------------------------------+
| Variable_name            | Value                          |
+--------------------------+--------------------------------+
| character_set_client     | latin1                         |
| character_set_connection | latin1                         |
| character_set_database   | utf8mb4                        |
| character_set_filesystem | binary                         |
| character_set_results    | latin1                         |
| character_set_server     | utf8mb4                        |
| character_set_system     | utf8mb3                        |
| character_sets_dir       | /usr/share/mysql-8.2/charsets/ |
+--------------------------+--------------------------------+
8 rows in set (0.01 sec)

mysql>
```

2. 在容器内 `/etc/mysql/conf.d` 目录或者宿主机内被映射的目录 `/home/docker/docker/mysql/test/conf` 中创建 `my.cnf`，并输入内容

```shell
docker@VM-8-15-ubuntu:~$ sudo vim /home/docker/docker/mysql/test/conf/my.cnf
[sudo] password for docker: 

[client]
default_character_set=utf8
[mysqld]
collation_server=utf8_general_ci
character_set_server=utf8
```

3. 重新进入容器查看编码

```shell
docker@yuehai:~$ docker exec -it bfab03cebaac bash
bash-4.4# mysql -u root -p   
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 8.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW VARIABLES LIKE 'character%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)

mysql> 
```


# 30、redis 高性能的开源内存数据存储

## 1、介绍

1. Redis 是一个高性能的开源内存数据存储，广泛用于缓存、数据存储、消息队列等场景。它支持多种数据结构，具有快速读写能力，并能通过持久化保证数据安全。
2. 内存存储：数据存储在内存中，读取和写入速度非常快，适用于需要高吞吐量和低延迟的场景。
3. 多种数据结构支持：支持多种数据类型，包括：
	1. 字符串（String）
	2. 哈希（Hash）
	3. 列表（List）
	4. 集合（Set）
	5. 有序集合（Sorted Set）
	6. 位图（Bitmap）
	7. HyperLogLog、地理空间索引（Geo）等
4. 持久化选项：
	8. RDB：周期性快照备份，适合大规模备份和恢复。
	9. AOF：记录所有写操作，提供更强的数据持久性。
	10. 混合持久化：结合 RDB 和 AOF 的优势。
5. 高可用与分布式：
	1. 主从复制：支持一主多从架构，数据冗余和负载均衡。
	2. Sentinel：自动故障转移和高可用性保障。
	3. Redis Cluster：支持水平扩展和数据分片。
6. 支持事务：支持通过 MULTI、EXEC、DISCARD 和 WATCH 实现事务性操作。
7. 发布/订阅：支持 Pub/Sub 模型，可以实现消息队列功能。
8. 高效的缓存：通过内存管理和多种淘汰策略（如 LRU）管理缓存，避免内存溢出。
9. Lua 脚本支持：可以在 Redis 上运行 Lua 脚本，保证原子操作。
10. 简单易用：提供了丰富的命令和客户端，支持多种编程语言，易于集成和使用。
11. 安全性：提供密码保护（requirepass）、ACL 访问控制和 TLS 加密通信等功能，保障数据和通信的安全性。
12. Redis 由于其高性能、灵活性和易用性，已经成为现代系统架构中不可或缺的组件，广泛应用于缓存、实时分析、队列管理等场景。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/services/nosql/redis/config`
	2. 数据目录：`/vol1/1000/docker/services/nosql/redis/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 6379:6379 \
-v /vol1/1000/docker/services/nosql/redis/config/redis.conf:/usr/local/etc/redis/redis.conf \
-v /vol1/1000/docker/services/nosql/redis/data:/data \
--network yuehai-net \
--restart=unless-stopped \
--name code-redis \
redis:latest \
redis-server /usr/local/etc/redis/redis.conf
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-redis 的服务
    code-redis:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: redis:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: code-redis
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Redis 的默认端口
            - "6379:6379"
        # 定义数据卷挂载规则
        volumes:
            # 配置目录
            - /vol1/1000/docker/services/nosql/redis/config/redis.conf:/usr/local/etc/redis/redis.conf
            # 数据目录
            - /vol1/1000/docker/services/nosql/redis/data:/data
        # 指定容器启动时执行的命令：使用指定的配置文件启动 redis-server
        command: redis-server /usr/local/etc/redis/redis.conf
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

1. 可使用 `Another-Redis-Desktop-Manager` 进行连接
2. 密码在配置文件中设置，用户名默认为 `default`


# 31、minio 开源的 S3 兼容对象存储服务器

> 1. 项目 github：https://github.com/minio/minio
> 2. dockerHub 地址：https://hub.docker.com/r/minio/minio

## 1、介绍

1. minio/minio 是 MinIO 的官方 Docker 镜像。MinIO 是一个高性能、与 Amazon S3 API 兼容的开源对象存储服务器。它允许在自己的硬件上构建私有的、自托管的对象存储服务，类似于 AWS S3，但完全由自己控制
2. 它的主要特点包括：
3. S3 API 兼容性：完全实现了 Amazon S3 的 API 接口，这意味着为 S3 设计的大量应用程序、库和工具（如备份软件、SDKs 等）都可以无缝地与 MinIO 一起使用
4. 高性能：专为高性能工作负载设计，能够处理大量的并发读写操作，非常适合用于数据分析、机器学习、日志存储、备份归档等场景
5. 可伸缩性与弹性：支持从单节点部署到跨多个服务器的大型分布式集群部署，可以通过简单地添加更多节点来水平扩展存储容量和性能
6. 数据保护与冗余：提供了强大的数据保护机制，如纠删码（Erasure Coding），即使部分硬盘或服务器发生故障，也能保证数据的完整性和可用性，同时还能检测并修复静默数据损坏（Bitrot protection）
7. 简洁的管理界面：内置了一个简单易用的 Web 管理控制台，方便您创建存储桶（Buckets）、上传/下载对象（文件）、管理用户和访问策略

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/vol1/1000/docker/services/nosql/minio/data`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 9001:9001 \
-v /vol1/1000/docker/services/nosql/minio/data:/data \
-e MINIO_ROOT_USER= \
-e MINIO_ROOT_PASSWORD= \
-e MINIO_CORS_ALLOW_ORIGIN= \
-e MINIO_COMPATIBILITY_ACL=on \
--network yuehai-net \
--restart unless-stopped \
--name code-minio \
minio/minio:RELEASE.2025-04-22T22-12-26Z \
server /data --console-address ":9001"
```

3. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 minio 的服务
    code-minio:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: minio/minio:RELEASE.2025-04-22T22-12-26Z
        # 设置容器的固定名称，方便识别和管理
        container_name: code-minio
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # S3 API 端口，防止泄露，关闭该端口，只使用经过代理的方式
            # - "9000:9000"
            # MinIO Web 控制台端口
            - "9001:9001"
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # 数据目录
            - /vol1/1000/docker/services/nosql/minio/data:/data
        # 定义环境变量
        environment:
            # 设置 MinIO 管理员用户名
            - MINIO_ROOT_USER=
            # 设置 MinIO 管理员密码
            - MINIO_ROOT_PASSWORD=
            # 关键：CORS 跨域许可，允许来自指定域的请求访问 MinIO 服务
            - MINIO_CORS_ALLOW_ORIGIN=
            # 告诉 MinIO 重新启用 ACL 功能
            - MINIO_COMPATIBILITY_ACL=on
        # 指定容器启动时执行的命令和参数：启动服务器并指定控制台使用 9001 端口
        command: server /data --console-address ":9001"
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

1. 访问：[http://127.0.0.1:9001](http://127.0.0.1:9001)
2. 初次访问需设定管理员账号密码

## 4、创建储存桶

1. 进入 web 页面后，点击左侧 Buckets

![](attachments/Pasted%20image%2020251024083111.png)

2. 在新页面中输入储存桶名称后，点击 Create Bucket 即可创建

![](attachments/Pasted%20image%2020251024083202.png)

3. 创建完成后，再次点击左侧 Buckets，选择刚才创建的储存桶

![](attachments/Pasted%20image%2020251024083402.png)

4. 进入后可以进行一些管理操作

![|700](attachments/Pasted%20image%2020251024083402.png)


# 40、consul 分布式系统的服务发现和配置

## 1、介绍

1. Consul 是一款由 HashiCorp 公司开发的开源工具，主要用于实现分布式系统的服务发现和配置。在微服务架构中，Consul 提供关键的服务支持，使得各个服务组件能够互相发现并高效地进行通信。
2. 主要功能：
	1. 服务发现：Consul 允许服务通过一个HTTP API、DNS 或者 Consul的命令行接口注册自己，并让其他服务通过Consul查询已注册的服务。
	2. 健康检查：Consul 客户端可以提供任意数量的健康检查，既可以是某个特定服务的，也可以是与节点相关的。这帮助在分布式系统中维护服务的健康状态，并保证请求不会被转发到不健康的服务实例上。
	3. 键值存储：Consul 提供一个简单的键值存储功能，可用于存放服务的配置信息或其他共享数据。
	4. 多数据中心：Consul 支持多数据中心，这使得它可以用于构建跨地域的高可用服务。
3. 架构组成：
	1. Consul 服务器：维护服务的注册信息和健康状态，处理客户端的查询请求。在一个生产环境中，通常会部署多个 Consul 服务器实例以形成一个高可用的集群。
	2. Consul 客户端：运行在服务实例旁边，负责注册服务到 Consul 服务器，并定期进行健康检查。它也会把服务请求转发给相应的服务实例。
4. 使用场景：
	1. 微服务架构：在微服务架构中，服务众多且动态变化，Consul 的服务发现和健康检查功能可以极大地简化服务间的通信。
	2. 配置管理：通过键值存储功能，可以集中管理应用配置，实现配置的动态更新和共享。
	3. 多云和跨数据中心：Consul 的多数据中心支持使其能够在多云或跨数据中心环境中进行无缝部署和管理。
5. Consul 以其稳定性和广泛的适用性，在现代云计算和容器化环境中被广泛采用，是构建大规模分布式系统的重要工具之一。

## 2、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/vol1/1000/docker/services/infra/consul/config`
	2. 数据目录：`/vol1/1000/docker/services/infra/consul/data`
2. 进入配置目录，创建 `consul.hcl` 文件

```shell
cd /vol1/1000/docker/services/infra/consul/config

nano consul.hcl
```

3. 进入配置目录，创建 `consul.hcl` 文件，并写入以下内容：
	1. `enabled = true`：开启 ACL 系统。只有当这一项被设置为 true 时，ACL 的功能才会被激活。
	2. `default_policy = "deny"`：设置了默认的ACL策略。如果设置为 `deny`，则默认情况下拒绝所有的请求，除非有明确的规则允许这些请求。这是一个保守的安全设置，确保没有明确许可的操作都不会被执行。
	3. `enable_token_persistence = true`：当这一项设置为 true 时，会在本地持久化存储 ACL 令牌。这意味着，即使 Consul 重启，令牌的信息也会被保存并在重启后恢复。
	4. `tokens`：这是一个配置令牌的部分。
		1. `master = "xxx"`：master 令牌是一个具有高级权限的令牌，通常用于 ACL 系统的初始化和管理。这里配置的是 master 令牌的值。它应当被妥善保护，因为持有者可以进行广泛的控制操作。

```shell
acl {
  enabled = true
  default_policy = "deny"
  enable_token_persistence = true
  tokens {
    master = "xxx"
  }
}
```


4. 使用 docker run 部署：

```shell
docker run -d \
-p 8300:8300 \
-p 8301:8301/tcp \
-p 8301:8301/udp \
-p 8302:8302/tcp \
-p 8302:8302/udp \
-p 8500:8500 \
-p 8600:8600/tcp \
-p 8600:8600/udp \
-v /vol1/1000/docker/services/infra/consul/config:/consul/config \
-v /vol1/1000/docker/services/infra/consul/data:/consul/data \
--network yuehai-net \
--restart=unless-stopped \
--name=code-consul \
hashicorp/consul:latest \
agent -server -bootstrap-expect=1 -ui -client='0.0.0.0' -data-dir=/consul/data
```

5. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 code-consul 的服务
    code-consul:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: hashicorp/consul:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: code-consul
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Server RPC 端口 (用于 Server 之间通信)
            - "8300:8300"
            # Serf LAN 端口 (TCP, 用于局域网内 Gossip 协议)
            - "8301:8301/tcp"
            # Serf LAN 端口 (UDP, 用于局域网内 Gossip 协议)
            - "8301:8301/udp"
            # Serf WAN 端口 (TCP, 用于广域网/跨数据中心 Gossip 协议)
            - "8302:8302/tcp"
            # Serf WAN 端口 (UDP, 用于广域网/跨数据中心 Gossip 协议)
            - "8302:8302/udp"
            # HTTP API & UI 端口 (用于访问 Consul 的 API 和 Web 界面)
            - "8500:8500"
            # DNS 端口 (TCP, 用于 Consul 的 DNS 服务)
            - "8600:8600/tcp"
            # DNS 端口 (UDP, 用于 Consul 的 DNS 服务)
            - "8600:8600/udp"
        # 定义数据卷挂载规则
        volumes:
            # 配置目录
            - /vol1/1000/docker/services/infra/consul/config:/consul/config
            # 数据目录
            - /vol1/1000/docker/services/infra/consul/data:/consul/data
        # 指定容器启动时执行的命令和参数
        # agent：表示启动一个 Agent 进程
        # -server：指定该节点为服务器模式
        # -bootstrap-expect=1：表示期望有 1 个服务器节点（通常在单节点测试环境中使用）
        # -ui：开启网页可视化管理界面
        # -client=0.0.0.0：指定可以外部连接的地址，0.0.0.0 表示外网全部可以连接
        # -data-dir=/consul/data：指定数据存储路径为 /consul/data
        # 除此之外，还可以加上 -datacenter 参数自定义一个数据中心名，同一个数据中心的节点数据中心名应当指定为一样！
        command: agent -server -bootstrap-expect=1 -ui -client=0.0.0.0 -data-dir=/consul/data
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

1. 访问：[http://127.0.0.1:8500](http://127.0.0.1:8500)
2. 需要输入配置文件中定义的 master 令牌进行登录

## 4、使用 HTTP API 获取配置

1. 进入 consul 管理后台，创建几个配置，比如 `test/test.json`

![|700](attachments/Pasted%20image%2020250114164636.png)

2. 点击 Tokens，点击复制 Secret ID

![|700](attachments/Pasted%20image%2020250114164417.png)

3. 使用 HTTP 接口请求数据：
	1.  请求方式：GET
	2. 接口请求：`/v1/kv/<配置路径和文件名>`
	3. 验证方式：在请求头中添加：`X-Consul-Token` 属性，值为刚才复制的 Secret ID

```shell
curl --location --request GET 'http://ip:8500/v1/kv/test/test.json' \
--header 'X-Consul-Token: xxx' \
```

4. 得到的数据中，`Value` 中是配置的值，其内容被 Base64 编码了，可使用该网址进行解码：[Base64 编码/解码](https://www.toolhelper.cn/EncodeDecode/Base64)

```shell
[
    {
        "LockIndex": 0,
        "Key": "test/test.json",
        "Flags": 0,
        "Value": "************************",
        "CreateIndex": 43,
        "ModifyIndex": 43
    }
]
```

## 5、创建新 token、策略、角色

### ①、创建新策略 Policy

1. 点击 Policies -> Create

![|700](attachments/Pasted%20image%2020250114164725.png)

2. name：该策略的名称，不和其他的策略重复即可
3. Description (Optional)：该策略的描述，可随意填写
4. Rules (HCL Format)：策略的规则，此处使用 json 格式，示例：

```shell
{
	"key_prefix": {
		"test/": {
			"policy": "read"
		}
	}
}
```

5. `key_prefix`：资源类型，作为 JSON 对象的键
6. `test/`：我所定义的资源目录，表示该目录下的所有配置，可以配置多组
7. `"policy": "read"`：只读
	1. `read`：只读
	2. `write`：读写
	3. `deny`：拒绝访问
8. 整体设置，点击 Save 保存即可

![|700](attachments/Pasted%20image%2020250114164822.png)

9. 保存后，策略中就会增加刚才保存的配置：

![](attachments/Pasted%20image%2020250114164847.png)

#### Ⅰ、资源类型说明

1. `key_prefix`：用于控制对 Consul 的键值存储(Key/Value Store)中特定键前缀的访问权限，例如：

```shell
{
	"key_prefix": {
		"foo/": {
			"policy": "write"
		},
		"bar/": {
			"policy": "read"
		}
	}
}
```

2. `service`：用于控制对服务的访问权限，例如：

```shell
{
	"service": {
		"web": {
			"policy": "write"
		},
		"api": {
			"policy": "read"
		}
	}
}
```

3. `agent`：用于控制对 Consul 代理的访问权限，包括节点的读取、服务和检查的注册等，例如：

```shell
{
	"agent": {
		"": {
			"policy": "read"
		},
		"foo": {
			"policy": "write"
		}
	}
}
```

4. `node`：用于控制对节点的访问权限
5. `session`：用于控制对会话(Session)的访问权限
6. `event`：用于控制对事件(Event)的访问权限
7. `query`：用于控制对预备查询(Prepared Query)的访问权限
8. `keyring`：用于控制对 Consul 的加密密钥环(Keyring)的访问权限
9. `operator`：用于控制对 Consul 的操作员(Operator)功能的访问权限,如执行快照和还原操作等

### ②、创建新角色 Roles

1. 1. 点击 Roles -> Create

![|700](attachments/Pasted%20image%2020250114164905.png)

2. name：该角色的名称，不和其他的角色重复即可
3. Description (Optional)：该角色的描述，可随意填写
4. Policies：执行的策略，选择刚才创建的策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](attachments/Pasted%20image%2020250114164945.png)

5. 保存后，角色中就会增加刚才保存的配置：

![](attachments/Pasted%20image%2020250114165010.png)

### ③、创建新 token

1. 1. 点击 Tokens -> Create

![|700](attachments/Pasted%20image%2020250114165023.png)

2. Description (Optional)：该 token 的描述，可随意填写
3. Roles：选择角色，选择刚才创建的角色
4. Policies：选择策略，因为配置了角色，可以不选择策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](attachments/Pasted%20image%2020250114165055.png)

6. 保存后，token 中就会增加刚才保存的配置：

![](attachments/Pasted%20image%2020250114165120.png)

### ④、使用新创建的 token 获取配置

1. 选择刚才创建的 Token，点击复制 Secret ID

![|700](attachments/Pasted%20image%2020250114165142.png)

3. 使用 HTTP 接口请求数据：
	1.  请求方式：GET
	2. 接口请求：`/v1/kv/<配置路径和文件名>`，此处的配置要在策略配置的目录下
	3. 验证方式：在请求头中添加：`X-Consul-Token` 属性，值为刚才复制的 Secret ID

```shell
curl --location --request GET 'http://ip:8500/v1/kv/test/test.json' \
--header 'X-Consul-Token: xxx' \
```

4. 得到的数据中，`Value` 中是配置的值，其内容被 Base64 编码了，可使用该网址进行解码：[Base64 编码/解码](https://www.toolhelper.cn/EncodeDecode/Base64)

```shell
[
    {
        "LockIndex": 0,
        "Key": "test/test.json",
        "Flags": 0,
        "Value": "************************************",
        "CreateIndex": 43,
        "ModifyIndex": 43
    }
]
```


# 82、redroid 在 Docker 中运行的安卓系统

> 1. 项目 github：[https://github.com/remote-android/redroid-doc](https://github.com/remote-android/redroid-doc)
> 2.  dockerHub 地址：[https://hub.docker.com/r/erstt/redroid](https://hub.docker.com/r/erstt/redroid)
> 3. 教程地址：https://club.fnnas.com/forum.php?mod=viewthread&tid=36386

## 1、介绍

1.  `redroid` 是一个创新的项目，它允许在 Docker 容器中运行一个完整的安卓操作系统。这使得在服务器或个人电脑上部署、管理和访问安卓环境变得前所未有的简单和高效。
2.  它的主要特点包括：
    1.  **容器化安卓**：将安卓系统封装在容器中，实现了快速部署、资源隔离和易于迁移的特性。
    2.  **高性能与 GPU 加速**：通过直接映射宿主机的 `/dev/dri` 等设备，`redroid` 可以利用宿主机的 GPU 进行硬件加速渲染，为图形密集型应用和游戏提供流畅的体验。
    3.  **无缝的 ADB 访问**：通过标准的 ADB (Android Debug Bridge) 协议进行连接和管理，开发者和用户可以像操作实体安卓设备一样安装应用、执行命令和调试程序。
    4.  **高度可定制**：社区提供了多种预构建的镜像，可以根据需求选择是否包含 Magisk、Google 服务等，满足不同的使用场景。
    5.  **云原生友好**：非常适合在云服务器上部署，用于云游戏、应用自动化测试、移动应用托管等场景。
3. 需要先安装一个驱动 `androidboot.use_memfd=memfd`，具体请看教程，飞牛的话直接在应用商店安装 `binder_linux` 即可

![](attachments/Pasted%20image%2020251111125436.png)

## 2、Docker 部署

1.  为防止容器意外停止后数据丢失，首先在宿主机创建目录：
    1.  数据目录：`/vol1/1000/docker/services/other/redroid/data`
2.  使用 `docker run` 部署：

```shell
docker run -d -it \
-p 5555:5555 \
-v /vol1/1000/docker/services/other/redroid/data:/data \
--device /dev/dri \
--device /dev/binder \
--privileged \
--network yuehai-net \
--restart unless-stopped \
--name redroid \
erstt/redroid:11.0.0_ndk_magisk_litegapps_ChromeOS \
androidboot.redroid_gpu_mode=host \
androidboot.use_memfd=1
```

3.  使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 redroid 的服务
    redroid:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: erstt/redroid:11.0.0_ndk_magisk_ChromeOS
        # 设置容器的固定名称，方便识别和管理
        container_name: redroid
        # 定义容器的重启策略：除非手动停止，否则总是在退出或宿主机重启时自动重启
        restart: unless-stopped
        # 启用特权模式，赋予容器几乎所有主机的 root 能力（请谨慎使用，仅在必要时开启）
        privileged: true
        # 保持容器的终端开启，以便能与之交互
        tty: true
        # 允许与容器的标准输入进行交互。tty 和 stdin_open 通常需要同时设置为 true，以确保可以附加(attach)到容器并进行操作
        stdin_open: true
        # 将宿主机的设备文件映射到容器内部。这是实现硬件加速的关键
        devices:
            # 映射 DRI (Direct Rendering Infrastructure) 设备。这是 Linux 系统中 GPU 的标准接口，允许容器直接将图形渲染指令提交给宿主机的 GPU 驱动
            - /dev/dri
            # 映射 binder 设备。这是安卓系统独有的进程间通信（IPC）机制，是所有APP和服务能够互相沟通的基石。将宿主机的 binder 驱动映射进去，可以获得比容器内模拟 binder 更高的性能和稳定性
            - /dev/binder
        # 定义端口映射规则
        ports:
            # adb 端口映射
            - 5555:5555
        # 定义数据卷挂载规则，用于持久化存储数据
        volumes:
            # # 数据目录
            - /vol1/1000/docker/services/other/redroid/data:/data
        # 指定容器启动时执行的命令和参数
        command:
            # 关键参数：设置 GPU 模式为 host，即直接使用宿主机的 GPU 进行渲染，实现硬件加速
            - androidboot.redroid_gpu_mode=host
            # 使用 memfd (memory file descriptor) 来替代老旧的 ashmem 共享内存机制，以兼容较新的 Linux 内核，提高内存管理效率
            - androidboot.use_memfd=1
            # 启用 ARM 架构原生桥接执行能力（针对64位应用）
            #- ro.enable.native.bridge.exec64=1
            # 指定用于实现原生桥接的具体库文件为 libhoudini.so。这两条命令组合起来，就是告诉安卓系统：“当你遇到 ARM 架构的应用时，请调用 houdini 这个翻译程序来运行它。”
            #- ro.dalvik.vm.native.bridge=libhoudini.so
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

1. `redroid` 容器本身没有图形界面访问端口，需要通过 ADB (Android Debug Bridge) 连接它，然后可以使用 `scrcpy` 等工具来显示和控制其图形界面
2.  连接 ADB：
```shell
adb connect 192.168.1.5:5555
```

3. scrcpy 控制：

```shell
scrcpy --tcpip=192.168.1.5:5555
```

## 4、问题记录

### ①、设置代理

1. 可能是我设备硬件的问题，部署的这个 redroid 无法打开 wifi，clash 等软件也不能使用，不过还好有另外的办法
2. 首先需要有可以使用的代理地址，比如部署在别处的 clash，假设代理地址是：`192.168.1.1:5555`
3. 通过 adb 连接 redroid：

```shell
adb connect 192.168.1.5:5555
```

4. 设置代理，执行后，整个 Redroid 系统的网络流量（包括浏览器、B站等所有应用）都会开始通过设置的代理服务器

```shell
adb shell settings put global http_proxy 192.168.1.1:7890
```

5. 取消代理：

```shell
adb shell settings put global http_proxy ""
```

### ②、无法登录谷歌商店

#### Ⅰ、报错现象

1. redroid 中登录谷歌商店提示：此设备未获得 Play 保护机制认证

![](attachments/Pasted%20image%2020251030112022.png)

#### Ⅱ、原因

1. 这是一个在非标准或未经授权的 Android 环境中比较常见的问题，这通常是由以下几个核心原因造成的：
2. 什么是 Play 保护机制认证？
	1. 这是 Google 用来确保安卓设备安全、可靠并能正确运行 Google 应用和服务的一套标准流程
	2. 所有正规的手机、平板制造商（如三星、小米、OPPO等）在发布设备前，都必须通过 Google 的一系列兼容性测试（CTS - Compatibility Test Suite）。通过测试后，设备才能预装 Google Play 商店及其他 GMS (Google Mobile Services) 应用
	3. 这个认证确保了设备的软硬件符合 Google 的规范，保护用户免受恶意软件的侵害，并保证应用生态的一致性
3. 为什么 redroid 会触发这个提示？
	1. Redroid 本质上是一个在 Linux 容器（Docker/LXC）中运行的安卓系统。它提供了一个虚拟化的、非物理的安卓环境
	2. 这种环境没有经过 Google 官方的硬件认证流程。在 Google 看来，您的这个“设备”是未知的、未经认证的
	3. 因此，当您尝试登录 Google Play 商店时，Google 的服务器会检查设备的认证状态，发现它不在认证列表中，便会出于安全考虑，阻止 Google 服务在其上运行

#### Ⅲ、解决

1. Google 为开发者和高级用户提供了一个后门，允许手动将未经认证的设备 ID 注册到自己的 Google 账户下
2. 获取 GSF ID (Google Service Framework ID)：需要在 redroid 容器中找到这个唯一的设备标识符。通常可以通过安装一个名为 Device ID 的应用来获取，或者使用 adb 命令：

```shell
# 进入 redroid 的 adb shell
adb shell

# 执行以下命令查询 GSF ID
settings get secure android_id
```

3. 请注意，有时 android_id 并不直接是 GSF ID，但通常可以通过一些应用查询到
4. 访问 Google 注册页面：在浏览器中打开 Google 的设备注册页面：https://www.google.com/android/uncertified/
5. 提交 ID：登录自己的 Google 账户，然后将获取到的 GSF ID 输入并提交
6. 重启并清除数据: 注册成功后，通常需要几分钟到几小时才能生效。之后，可能需要清除 Google Play 商店和 Google 服务框架的缓存和数据，然后重启 redroid 容器再尝试登录

### ③、设置分辨率

1. 确保有超级管理员权限，打开终端模拟器

![](attachments/PixPin_2025-11-04_15-51-38.png)

2. 输入以下命令

```shell
# 获取 root 权限
su
# 设置横纵尺寸
wm size 1080x1920
# 设置 dpi
wm density 420
```

![](attachments/PixPin_2025-11-04_15-56-13.png)

### ④、

## 5、


# 83、n2n 虚拟局域网

> 1. 项目 github：https://github.com/ntop/n2n/tree/3.0
> 2. dockerHub 地址：https://hub.docker.com/r/jonnyan404/n2n-v3
> 3. N2N 服务端软件 n2n-3.0：
> 	1. github 下载地址：https://github.com/ntop/n2n/releases/tag/3.0
> 	2. 本地下载：[n2n-3.0.zip](attachments/n2n-3.0.zip)
> 4. N2N 客户端软件 EasyN2N：
> 	1. 下载地址：https://bugxia.com/357.html
> 	2. 本地下载：[EasyN2N_3.3.zip](attachments/EasyN2N_3.3.zip)
> 5.  java 查询程序：[yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar)

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
3. 创建目录：`/home/yan/app/internet/NetworkTools/n2n/`，下载 N2N 服务端：[n2n-3.0.zip](attachments/n2n-3.0.zip) 放入其中
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

2. 下载 EasyN2N 客户端：[EasyN2N_3.3.zip](attachments/EasyN2N_3.3.zip)，解压后双击 `EasyN2N.exe` 打开（若是被杀毒软件删除，请将其加入白名单）<font color="#ff0000">若是被杀毒软件误删，请加入白名单</font>

![](attachments/Pasted%20image%2020251111143000.png)

3. 配置：
	1. 服务器：`服务器ip:41984`
	2. 小组名称：所有人需要是一样的名称
	3. 虚拟网 ip：最好设置为同一网段（也可以选择自动分配，分配的若不是同一网段，再自行修改）
	4. 点击启动

![](attachments/Pasted%20image%2020251111134832.png)

4. 服务器右侧显示绿色对号即为连接成功

![](attachments/Pasted%20image%2020251107161831.png)

5. 启动后，点击小组名称后的按钮，可打开已连接的主机列表，双击列表项可显示延迟

![](attachments/Pasted%20image%2020251111131138.png)

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
	1. jar 包目录：`/home/docker/volumes/services/other/n2n-query-yuehai-tool/`，下载 java 工具类 [yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
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

1. 创建目录：`/home/docker/volumes/services/other/n2n-query-yuehai-tool`，下载 java 工具类 [yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar](attachments/yuehai-tool-1.0-SNAPSHOT-jar-with-dependencies.jar) 放入其中
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
> 4. 本地下载：[gnb_udp_over_tcp.zip](attachments/gnb_udp_over_tcp.zip)

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

2. 下载上面的 [gnb_udp_over_tcp.zip](attachments/gnb_udp_over_tcp.zip)，上传到服务器的对应目录中，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`
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

1. 下载上面的 [gnb_udp_over_tcp.zip](attachments/gnb_udp_over_tcp.zip)，解压，进入目录 `bin\Window10_x86_64`
2. 在目录中，按住键盘的 shift 键，然后点击鼠标右键，选择：在此处打开 Powershell 窗口

![](attachments/Pasted%20image%2020251111131416.png)

3. 之后会弹出一个窗口，在其中输入以下内容并回车：
	1. `-u`：表示启用 UDP 模式，即将接收到的 TCP 数据转换为 UDP 数据
	2. `-l 41984`：<font color="#ff0000">n2n 使用的端口</font>，`-l` 参数后跟的是监听的 UDP 端口号，这里设置为 41984，表示该服务将监听端口 41984 上的 UDP 数据
	3. `83.229.120.176`：这是 TCP 源地址，即服务端的 IP 地址；<font color="#ff0000">请根据要连接的服务端自行修改这个参数</font>
	4. `41985`：这是服务端监听的 TCP 端口号

```shell
.\gnb_udp_over_tcp.exe -u -l 41984 83.229.120.176 41985
```

![](attachments/Pasted%20image%2020251111131819.png)

4. 若是不想手动输入上面的命令，也可以直接双击目录的脚本 `run_gnb_udp_over_tcp.bat`，会自动执行该命令；但是这种脚本的方式有时会失败，如果失败，需手动输入命令

![](attachments/Pasted%20image%2020251111132220.png)

5. 打开 n2n，服务端填写：`127.0.0.1:41984`，点击启动，等待时间会稍长一点，大概六七秒
6. 等待右侧出现绿色对号，即为连接成功

![](attachments/Pasted%20image%2020251111132524.png)

#### Ⅱ、ubuntu 客户端配置

1. 客户端先正常编译安装 n2n 客户端
2. 下载上面的 [gnb_udp_over_tcp.zip](attachments/gnb_udp_over_tcp.zip)，上传到服务器的对应目录中，比如 `/home/docker/volumes/services/other/n2n_gnb_udp_over_tcp/`
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

![](attachments/Pasted%20image%2020251111143709.png)

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

![](attachments/Pasted%20image%2020251111144005.png)

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

![](attachments/Pasted%20image%2020251111144121.png)

### ⑤、

### ⑥、

## 8、





