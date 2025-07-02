# 1、tomcat

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

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163352.png)

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

4. 访问测试：[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## 4、显示 404 的解决方法

1. 若是显示 404，则查看防火墙 10100 端口；若端口已开放，则：
2. 查看映射目录的 `webapps` 和 `webapps.dist` 目录；若 `webapps` 为空 `webapps.dist` 不为空

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163443.png)

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163500.png)

3. 删除 `webapps` 目录，将 `webapps.dist` 目录重命名为 `webapps`

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163523.png)

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163538.png)

4. 再次访问：[http://172.17.0.1:8080/](http://172.17.0.1:8080/)

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107163621.png)


# 2、openJdk

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

1. 只设定基础的 nginx 代理，登录后可能提示：`Failed to load preferences`
2. 此时需要添加如下配置：

```nginx
# 定义一个 location 块，匹配所有进入的请求 (/)
location / {
  # 关键：将请求代理到指定服务
  # proxy_pass 指令指定了后端服务器的地址和端口
  # 所有匹配此 location 块的请求都将被转发到 http://code-pgadmin4:80
  proxy_pass http://code-pgadmin4:80;
  
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
}
```


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

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250121105335.png)

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

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250121105443.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250107164736.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164636.png)

2. 点击 Tokens，点击复制 Secret ID

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164417.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164725.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164822.png)

9. 保存后，策略中就会增加刚才保存的配置：

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164847.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164905.png)

2. name：该角色的名称，不和其他的角色重复即可
3. Description (Optional)：该角色的描述，可随意填写
4. Policies：执行的策略，选择刚才创建的策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114164945.png)

5. 保存后，角色中就会增加刚才保存的配置：

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114165010.png)

### ③、创建新 token

1. 1. 点击 Tokens -> Create

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114165023.png)

2. Description (Optional)：该 token 的描述，可随意填写
3. Roles：选择角色，选择刚才创建的角色
4. Policies：选择策略，因为配置了角色，可以不选择策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114165055.png)

6. 保存后，token 中就会增加刚才保存的配置：

![](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114165120.png)

### ④、使用新创建的 token 获取配置

1. 选择刚才创建的 Token，点击复制 Secret ID

![|700](https://openlist.yuehai.fun:63/d/TakeDown/Docker/attachments/Pasted%20image%2020250114165142.png)

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

# 八、

# 九、

# 十、





