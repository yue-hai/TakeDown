# 一、tomcat

## 1、首次创建容器

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 数据目录：`/home/docker/docker/volumes/tomcat/tomcat9`
2. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射

```shell
docker run -d \
-p 8080:8080 \
--name code-tomcat9 \
tomcat:jre21
```

## 2、复制数据，并设置映射目录

1. 将容器内的 `/usr/local/tomcat` 目录复制到宿主机上：

```shell
docker cp code-tomcat9:/usr/local/tomcat/ /home/docker/docker/volumes/tomcat/tomcat9/
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163352.png)

2. 停止并删除容器：

```shell
# 停止：
docker stop code-tomcat9

# 删除：
docker rm code-tomcat9
```

3. 重新启动容器，并设置映射目录：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 8080:8080 \
-v /home/docker/docker/volumes/tomcat/tomcat9/tomcat:/usr/local/tomcat \
--privileged=true \
--restart=unless-stopped
--name code-tomcat9 \
tomcat:jre21
```

## 3、访问

4. 访问测试：[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## 4、显示 404 的解决方法

1. 若是显示 404，则查看防火墙 10100 端口；若端口已开放，则：
2. 查看映射目录的 `webapps` 和 `webapps.dist` 目录；若 `webapps` 为空 `webapps.dist` 不为空

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163443.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163500.png)

3. 删除 `webapps` 目录，将 `webapps.dist` 目录重命名为 `webapps`

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163523.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163538.png)

4. 再次访问：[http://www.yue-hai.top:8080/](http://172.17.0.1:8080/)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107163621.png)

# 二、mysql

## 1、创建容器，并设置映射目录

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/mysql/conf/`
	2. 数据目录：`/home/docker/docker/volumes/mysql/data/`
	3. 日志目录：`/home/docker/docker/volumes/mysql/log/`
2. 在 `/home/docker/docker/volumes/mysql/conf/` 目录下创建配置文件  `my.cnf`，并填入以下配置：

```shell
cd /home/docker/docker/volumes/mysql/conf/

nano my.cnf
```

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

3. 启动容器时映射容器数据卷：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `-e MYSQL_ROOT_PASSWORD=123456`：设置 root 密码
	5. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	6. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-v /home/docker/docker/volumes/mysql/log:/var/log/mysql \
-v /home/docker/docker/volumes/mysql/data:/var/lib/mysql \
-v /home/docker/docker/volumes/mysql/conf/my.cnf:/etc/mysql/my.cnf \
--privileged=true \
--restart=unless-stopped \
--name code-mysql \
mysql:8.2.0
```

7. 使用 Navicat 连接

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107164736.png)

## 2、测试连接以及创建数据库与表

1. 创建数据库

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107164810.png)

2. 创建表

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107164827.png)

3. 添加数据

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107164845.png)

4. 进入 mysql 容器

```shell
docker@yuehai:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
bfab03cebaac   mysql     "docker-entrypoint.s…"   22 minutes ago   Up 22 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   code-mysql
docker@yuehai:~$ docker exec -it bfab03cebaac bash

bash-4.4# 
```

5. 进入 mysql，输入密码：123456

```shell
bash-4.4# mysql -u root -p       
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 8.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

6. 查看数据库与表

```shell
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| yuehai             |
+--------------------+
5 rows in set (0.00 sec)

mysql> use yuehai
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------+
| Tables_in_yuehai |
+------------------+
| user             |
+------------------+
1 row in set (0.00 sec)

mysql> select * from user;
+----+------+
| id | name |
+----+------+
|  1 | ??   |
|  2 | ?    |
+----+------+
2 rows in set (0.00 sec)

mysql> exit
Bye

bash-4.4# exit
exit
docker@yuehai:~$ 
```

## 3、插入中文报错

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

# 三、openJdk 21

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 配置目录：`/home/docker/docker/volumes/openjdk/jar/00_TEST/`
2. 上传 jar 程序到 `00_TEST` 目录中，测试 jar 包名称为：`TEST-0.0.1-SNAPSHOT.jar`，请对应修改名称

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250107165410.png)

3. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器
	6. `java -jar /container/path/jar/00_TEST/TEST-0.0.1-SNAPSHOT.jar`：容器启动时执行该命令，即启动指定 java 程序
	
```shell
docker run -d \
-p 8080:8080 \
-v /home/docker/docker/volumes/openjdk/:/container/path \
--privileged=true \
--restart=unless-stopped
--name code-java-test \
openjdk:21 \
java -jar /container/path/jar/00_TEST/TEST-0.0.1-SNAPSHOT.jar
```

4. 访问接口测试

# 四、使用 shell 脚本执行多个 jar 程序

1. 准备 jar 程序：
	1. springboot 测试包：`TEST-0.0.1-SNAPSHOT.jar`，请对应修改名称
	2. y_chat 的 WebSockets 消息转发：`y-chat-WebSocket-server-1.0-SNAPSHOT-jar-with-dependencies.jar`，请对应修改名称
	3. y_chat 的 springboot 后台服务器 user 模块：`user-1.0-SNAPSHOT.jar`，请对应修改名称
2. 创建映射目录，并将这三个 jar 包上传到指定目录：
	1. `/home/docker/docker/volumes/openjdk/jar/00_TEST/`
	2. `/home/docker/docker/volumes/openjdk/jar/y-chat-WebSocket-server/`
	3. `/home/docker/docker/volumes/openjdk/jar/y-chat-back-server/user/`
3. 进入 `/home/docker/docker/volumes/openjdk` 目录，创建 `run_jar.sh` 文件，并写入下面的内容：

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

# 8082 y-chat WebSocket 消息转发服务器 (后台)
start_app "${main_path}/jar/y-chat-WebSocket-server" \
          "y-chat-WebSocket-server-1.0-SNAPSHOT-jar-with-dependencies.jar" \
          "y_chat_ws.log" \
          "yes"

# 8081 user y-chat springboot 后台数据服务器 (后台)
start_app "${main_path}/jar/y-chat-back-server/user" \
          "user-1.0-SNAPSHOT.jar" \
          "user.log" \
          "yes"

# 8080 测试 (前台)
start_app "${main_path}/jar/00_TEST" \
          "TEST-0.0.1-SNAPSHOT.jar" \
          "test.log" \
          "no"
```

4. 启动容器：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `-v`：指定挂载目录
	4. `--privileged=true`：扩大容器的权限解决挂载目录没有权限的问题
	5. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器
	6. `/container/path/run_jar.sh`：容器启动时执行该命令，即执行指定脚本
	
```shell
docker run -d \
-p 8080-8082:8080-8083 \
-e NACOS_SERVER_ADDR="127.0.0.1:8848" \
-e NACOS_NAMESPACE="******" \
-e NACOS_USERNAME="nacos" \
-e NACOS_PASSWORD="nacos" \
-e NACOS_GROUP="DEFAULT_GROUP" \
-e NACOS_FILE_EXTENSION="yml" \
-v /home/docker/docker/volumes/openjdk/:/container/path \
--privileged=true \
--name code-java \
openjdk:21 \
/container/path/run_jar.sh
```

5. 访问接口测试

# 五、使用 Docker-compose 容器编排执行多个 jar 程序

1. 准备 jar 程序：
	1. springboot 测试包：`TEST-0.0.1-SNAPSHOT.jar`，请对应修改名称
	2. y_chat 的 WebSockets 消息转发：`y-chat-WebSocket-server-1.0-SNAPSHOT-jar-with-dependencies.jar`，请对应修改名称
	3. y_chat 的 springboot 后台服务器 user 模块：`user-1.0-SNAPSHOT.jar`，请对应修改名称
2. 创建映射目录，并将这三个 jar 包上传到指定目录：
	1. `/home/docker/docker/volumes/openjdk/jar/00_TEST/`
	2. `/home/docker/docker/volumes/openjdk/jar/y-chat-WebSocket-server/`
	3. `/home/docker/docker/volumes/openjdk/jar/y-chat-back-server/user/`
3. 进入 `/home/docker/docker/volumes/openjdk` 目录，创建 `docker-compose.yml` 文件，并写入下面的内容：

```yaml
# 版本信息，定义关乎于 docker 的兼容性，Compose 文件格式有 3 个版本,分别为 1、2.x 和 3.x
version : '3.8'

# 所有的 docker 容器
services:
  # code-java 容器
  code-java:
    # 容器名称
    container_name: code-java
    # 指定使用的镜像
    image: openjdk:21
    # 映射的端口号；可指定多组
    ports:
      - "8080:8080"
      - "8081:8081"
      - "8082:8082"
    # 映射挂载的目录；可指定多组
    volumes: 
      - "/home/docker/docker/volumes/openjdk/:/container/path"
    # 设置全局变量；可指定多组
    environment:
      # 10310 user y-chat springboot 后台数据服务器所需变量
	  - NACOS_SERVER_ADDR="127.0.0.1:8848"
	  - NACOS_NAMESPACE="******"
	  - NACOS_USERNAME="nacos"
	  - NACOS_PASSWORD="nacos"
	  - NACOS_GROUP="DEFAULT_GROUP"
	  - NACOS_FILE_EXTENSION="yml"
      # 8082 y-chat WebSocket 消息转发服务器 (后台)
      - y_char_ws_app=/container/path/jar/yuehai-chat-WebSocket-server/y-chat-WebSocket-server-1.0-SNAPSHOT-jar-with-dependencies.jar
      - y_char_ws_log=/container/path/jar/yuehai-chat-WebSocket-server/y_char_ws.log
      # 8081 user y-chat springboot 后台数据服务器 (后台)
      - y_char_back_server_user_app=/container/path/jar/y-chat-back-server/user/user-1.0-SNAPSHOT.jar
      - y_char_back_server_user_log=/container/path/jar/y-chat-back-server/user/user.log
      # 8080 测试 (前台)
      - test_app=/container/path/jar/00_TEST/TEST-0.0.1-SNAPSHOT.jar
      - test_log=/container/path/jar/00_TEST/test.log
    # 容器启动时执行的命令，该命令只能指定一行，不过可以使用 sh -c 来变相实现多行
    # 变量引用使用 $$ 的原因是为了转义特殊字符，以确保变量在命令字符串中被正确地解析而不是被 Compose 文件本身解析
    command: >
      sh -c "
        java -jar $${y_char_ws_app} > $${y_char_ws_log} 2>&1 &
        java -jar $${y_char_back_server_user_app} > $${y_char_back_server_user_log} 2>&1 &
        java -jar $${test_app} > $${test_log} 2>&1
      "
```

4. 启动 docker-compose 服务并后台运行：`docker-compose up -d`

```shell
docker@yuehai:~/docker/volumes/openjdk$ docker compose up -d
[+] Running 1/1
 ✔ Container code-java  Started                                                      0.0s 
docker@yuehai:~/docker/volumes/openjdk$ 
```

5. 如果嫌 `docker-compose.yml` 文件中的 `command` 属性的命令写起来太繁琐，也可以直接在 `command` 属性中调用上面的 `run_jar.sh` 脚本
6. 访问接口测试
7. 这种方式感觉好麻烦

# 六、consul 分布式系统的服务发现和配置

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
	1. 配置目录：`/home/docker/docker/volumes/consul/config`
	2. 数据目录：`/home/docker/docker/volumes/consul/data`
2. 进入配置目录，创建 `consul.hcl` 文件，并写入以下内容：
	1. `enabled = true`：开启 ACL 系统。只有当这一项被设置为 true 时，ACL 的功能才会被激活。
	2. `default_policy = "deny"`：设置了默认的ACL策略。如果设置为 `deny`，则默认情况下拒绝所有的请求，除非有明确的规则允许这些请求。这是一个保守的安全设置，确保没有明确许可的操作都不会被执行。
	3. `enable_token_persistence = true`：当这一项设置为 true 时，会在本地持久化存储 ACL 令牌。这意味着，即使 Consul 重启，令牌的信息也会被保存并在重启后恢复。
	4. `tokens`：这是一个配置令牌的部分。
		1. `master = "c5165092-af61-48e8-acf9-eda32a6e4b70"`：master 令牌是一个具有高级权限的令牌，通常用于 ACL 系统的初始化和管理。这里配置的是 master 令牌的值。它应当被妥善保护，因为持有者可以进行广泛的控制操作。

```shell
cd /home/docker/docker/volumes/consul/config

nano consul.hcl
```

```shell
acl {
  enabled = true
  default_policy = "deny"
  enable_token_persistence = true
  tokens {
    master = "c5165092-af61-48e8-acf9-eda32a6e4b70"
  }
}
```

3. 使用 docker 部署：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
		1. `8300`：TCP 协议，用于 Consul 集群中各个节点相互连结通信的端口
		2. `8301`：TCP 或者 UDP 协议，用于 Consul 节点之间相互使用 Gossip 协议健康检查等交互
		3. `8302`：TCP 或者 UDP 协议，用于单个或多个数据中心之间的服务器节点的信息同步
		4. `8500`：HTTP 协议，用于 API 接口或者我们上述的网页管理界面访问
		5. `8600`：TCP 或者 UDP 协议，作为 DNS 服务器，用于通过节点名查询节点信息
	3. `-v`：指定挂载目录
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。
	5. 除此之外，我们来看一下命令最后的几个参数：
		1. `agent`：表示启动一个 Agent 进程
		2. `-server`：指定该节点为服务器模式
		3. `-bootstrap=true`：开启引导模式，适用于单节点 Consul
		4. `-ui`：开启网页可视化管理界面
		5. `-client='0.0.0.0'`：指定可以外部连接的地址，0.0.0.0 表示外网全部可以连接
		6. `-data-dir=/consul/data`：指定数据存储路径为 `/consul/data`
		7. 除此之外，还可以加上 `-datacenter` 参数自定义一个数据中心名，同一个数据中心的节点数据中心名应当指定为一样！

```shell
docker run -d \
-p 8300:8300 \
-p 8301:8301 \
-p 8302:8302 \
-p 8500:8500 \
-p 8600:8600 \
-v /home/docker/docker/volumes/consul/data:/consul/data \
-v /home/docker/docker/volumes/consul/config:/consul/config \
--restart=unless-stopped
--name=code-consul \
hashicorp/consul \
agent -server -bootstrap=true -ui -client='0.0.0.0' -data-dir=/consul/data
```

## 3、访问

1. 访问：[http://127.0.0.1:8500](http://127.0.0.1:8500)
2. 需要输入配置文件中定义的 master 令牌进行登录

## 4、使用 HTTP API 获取配置

1. 进入 consul 管理后台，创建几个配置，比如 `test/test.json`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164636.png)

2. 点击 Tokens，点击复制 Secret ID

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164417.png)

3. 使用 HTTP 接口请求数据：
	1.  请求方式：GET
	2. 接口请求：`/v1/kv/<配置路径和文件名>`
	3. 验证方式：在请求头中添加：`X-Consul-Token` 属性，值为刚才复制的 Secret ID

```shell
curl --location --request GET 'http://ip:8500/v1/kv/test/test.json' \
--header 'X-Consul-Token: c5165092-af61-48e8-acf9-eda32a6e4b70' \
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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164725.png)

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164822.png)

9. 保存后，策略中就会增加刚才保存的配置：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164847.png)

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

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164905.png)

2. name：该角色的名称，不和其他的角色重复即可
3. Description (Optional)：该角色的描述，可随意填写
4. Policies：执行的策略，选择刚才创建的策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114164945.png)

5. 保存后，角色中就会增加刚才保存的配置：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114165010.png)

### ③、创建新 token

1. 1. 点击 Tokens -> Create

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114165023.png)

2. Description (Optional)：该 token 的描述，可随意填写
3. Roles：选择角色，选择刚才创建的角色
4. Policies：选择策略，因为配置了角色，可以不选择策略
5. 设置完毕后，点击 Save 保存即可
 
![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114165055.png)

6. 保存后，token 中就会增加刚才保存的配置：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114165120.png)

### ④、使用新创建的 token 获取配置

1. 选择刚才创建的 Token，点击复制 Secret ID

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fattachments%2FPasted%20image%2020250114165142.png)

3. 使用 HTTP 接口请求数据：
	1.  请求方式：GET
	2. 接口请求：`/v1/kv/<配置路径和文件名>`，此处的配置要在策略配置的目录下
	3. 验证方式：在请求头中添加：`X-Consul-Token` 属性，值为刚才复制的 Secret ID

```shell
curl --location --request GET 'http://ip:8500/v1/kv/test/test.json' \
--header 'X-Consul-Token: c5165092-af61-48e8-acf9-eda32a6e4b70' \
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

# 七、

# 八、

# 九、

# 十、





