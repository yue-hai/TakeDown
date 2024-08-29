> [https://www.bilibili.com/video/BV1Rv41177Af](https://www.bilibili.com/video/BV1Rv41177Af)，感觉不太好
> 
> [尚硅谷_Redis6课件.docx](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F尚硅谷_Redis6课件.docx)
> 
> 可视化工具 AnotherRedisDesktopManager：[https://gitee.com/qishibo/AnotherRedisDesktopManager/releases](https://gitee.com/qishibo/AnotherRedisDesktopManager/releases)
> 
> 启动 docker redis 容器：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:6379 --name redis -v /home/docker/docker/VOLUME/redis/config:/etc/redis -v /home/docker/docker/VOLUME/redis/data:/data -v /home/docker/docker/VOLUME/redis/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`

# 一、NoSQL 数据库简介

## 1、技术发展

### ①、技术的分类

1. 解决功能性的问题：Java、Jsp、RDBMS、Tomcat、HTML、Linux、JDBC、SVN
2. 解决扩展性的问题：Struts、Spring、SpringMVC、Hibernate、Mybatis
3. 解决性能的问题：NoSQL、Java线程、Hadoop、Nginx、MQ、ElasticSearch

### ②、Web1.0 时代

- Web1.0 的时代，数据访问量很有限，用一夫当关的高性能的单点服务器可以解决大部分问题

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-40-813--4GURRM3fIJOicw.png)

### ③、Web2.0 时代

- 随着 Web2.0 的时代的到来，用户访问量大幅度提升，同时产生了大量的用户数据。加上后来的智能移动设备的普及，所有的互联网平台都面临了巨大的性能挑战

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-41-425--1ZWzTgoe5fdOjQ.png)

### ④、解决 CPU 及内存压力

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-41-606--5xE5e0HcW1wIkg.png)

### ⑤、解决 IO 压力

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-41-797--Gri0e6FA7JXPrw.png)

## 2、NoSQL 数据库

### ①、NoSQL 数据库概述

NoSQL(NoSQL = Not Only SQL )，意即“不仅仅是 SQL”，泛指非关系型的数据库。 
NoSQL 不依赖业务逻辑方式存储，而以简单的 key-value 模式存储。因此大大的增加了数据库的扩展能力。

1. 不遵循 SQL 标准
2. 不支持 ACID
3. 远超于 SQL 的性能

### ②、NoSQL 适用场景

1. 对数据高并发的读写
2. 海量数据的读写
3. 对数据高可扩展性的

### ③、NoSQL 不适用场景

1. 需要事务支持
2. 基于 sql 的结构化查询存储，处理复杂的关系，需要即席查询。
3. （用不着 sql 的和用了 sql 也不行的情况，请考虑用 NoSql）

### ④、Memcache

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-42-025--dB2OpUeZCzfVpA.png)

1. 很早出现的 NoSql 数据库
2. 数据都在内存中，一般不持久化
3. 支持简单的 key-value 模式，支持类型单一
4. 一般是作为缓存数据库辅助持久化的数据库

### ⑤、Redis

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-42-317--e7GJu72189rVQw.png)


1. 几乎覆盖了 Memcached 的绝大部分功能
2. 数据都在内存中，支持持久化，主要用作备份恢复
3. 除了支持简单的 key-value 模式，还支持多种数据结构的存储，比如 list、set、hash、zset 等。
4. 一般是作为缓存数据库辅助持久化的数据库

### ⑥、MongoDB

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-42-463--gkCHm0K3ayczRA.png)


1. 高性能、开源、模式自由(schema  free)的**文档型数据库**
2. 数据都在内存中， 如果内存不足，把不常用的数据保存到硬盘
3. 虽然是 key-value 模式，但是对 value（尤其是**json**）提供了丰富的查询功能
4. 支持二进制数据及大型对象
5. 可以根据数据的特点**替代 RDBMS**，成为独立的数据库。或者配合 RDBMS，存储特定的数据。

## 3、行式存储数据库（大数据时代）

### ①、行式数据库

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-42-596--CwUL7F8kDw0RrQ.png)

### ②、列式数据库

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-42-783--X8oOCu2D3tcWdA.png)

#### Ⅰ、Hbase

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-43-132--km6iHRrg3AJIdQ.png)

1. HBase 是 Hadoop 项目中的数据库。它用于需要对大量的数据进行随机、实时的读写操作的场景中。
2. HBase 的目标就是处理数据量非常庞大的表，可以用普通的计算机处理超过 10 亿行数据，还可处理有数百万列元素的数据表。

#### Ⅱ、Cassandra[kəˈsændrə]

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-43-414--JQsUXpfL9I5C5w.png)


- Apache Cassandra 是一款免费的开源 NoSQL 数据库，其设计目的在于管理由大量商用服务器构建起来的庞大集群上的海量数据集(数据量通常达到 PB 级别)。在众多显著特性当中，Cassandra 最为卓越的长处是对写入及读取操作进行规模调整，而且其不强调主集群的设计思路能够以相对直观的方式简化各集群的创建与扩展流程。

## 4、图关系型数据库

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-43-693--KZT1kYKTvxa3kw.png)

- 主要应用：社会关系，公共交通网络，地图及网络拓谱(n*(n-1)/2)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-43-833--rBD_Ko4UXluSiQ.png)

## 5、DB-Engines 数据库排名
> [https://db-engines.com/en/ranking](https://db-engines.com/en/ranking)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-44-150--pDmkQ7xobkH4OA.png)

# 二、Redis 概述安装
## 1、概述

1. Redis 是一个开源的 key-value 存储系统。
2. 和 Memcached 类似，它支持存储的 value 类型相对更多，包括 string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和 hash（哈希类型）。
3. 这些数据类型都支持 push/pop、add/remove 及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。
4. 在此基础上，Redis 支持各种不同方式的排序。
5. 与 memcached 一样，为了保证效率，数据都是缓存在内存中。
6. 区别的是 Redis 会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件。
7. 并且在此基础上实现了 master-slave(主从) 同步。

## 2、应用场景

### ①、配合关系型数据库做高速缓存

1. 高频次，热门访问的数据，降低数据库 IO
2. 分布式架构，做 session 共享

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-44-321--7aV58gqNJVOhQA.png)

### ②、多样的数据结构存储持久化数据

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-44-485--QKvl9kd2V00R4A.png)

## 3、Redis 安装
> Redis 官方网站：[http://redis.io](http://redis.io)
> Redis 中文官方网站：[http://redis.cn/](http://redis.cn/)

- 这里我是用 docker 安装的

1. 搜索镜像：`docker search redis`

```shell
docker@VM-8-15-ubuntu:~$ docker search redis
NAME                                DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
redis                               Redis is an open source key-value store that…   11761     [OK]       
bitnami/redis                       Bitnami Redis Docker Image                      236                  [OK]
redislabs/redisinsight              RedisInsight - The GUI for Redis                79                   
redislabs/redisearch                Redis With the RedisSearch module pre-loaded…   56                   
redislabs/rejson                    RedisJSON - Enhanced JSON data type processi…   52                   
redislabs/redis                     Clustered in-memory database engine compatib…   36                   
redis/redis-stack                   redis-stack installs a Redis server with add…   33                   
redislabs/redismod                  An automated build of redismod - latest Redi…   32                   [OK]
redislabs/redisgraph                A graph database module for Redis               25                   [OK]
redislabs/rebloom                   A probablistic datatypes module for Redis       22                   [OK]
redis/redis-stack-server            redis-stack-server installs a Redis server w…   16                   
redislabs/redistimeseries           A time series database module for Redis         12                   
redislabs/operator                                                                  7                    
redislabs/redis-py                                                                  5                    
redislabs/redisai                                                                   4                    
redislabs/redisgears                An automated build of RedisGears                4                    
redislabs/redisml                   A Redis module that implements several machi…   3                    [OK]
redislabs/redis-webcli              A tiny Flask app to provide access to Redis …   3                    [OK]
redislabs/k8s-controller                                                            2                    
redislabs/operator-internal         This repository contains pre-released versio…   1                    
redislabs/memtier_benchmark         Docker image to run memtier_benchmark           0                    
redislabs/ng-redis-raft             Redis with redis raft module                    0                    
redislabs/olmtest                   Test artefact for OLM CSV                       0                    
redislabs/olm-bundle                                                                0                    
redislabs/k8s-controller-internal                                                   0

docker@VM-8-15-ubuntu:~$ 
```

2. 拉取镜像：`docker pull redis:6.2.1`
```shell
docker@VM-8-15-ubuntu:~$ docker pull redis:6.2.1
6.2.1: Pulling from library/redis
f7ec5a41d630: Pull complete 
a36224ca8bbd: Pull complete 
7630ad34dcb2: Pull complete 
dd0ea236b03b: Pull complete 
ed6ed4f2f5a6: Pull complete 
8788804112c6: Pull complete 
Digest: sha256:08e282682a708eb7f51b473516be222fff0251cdee5ef8f99f4441a795c335b6
Status: Downloaded newer image for redis:6.2.1
docker.io/library/redis:6.2.1

docker@VM-8-15-ubuntu:~$
```

3. 查看镜像：`docker images`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
docker-compose_nginx          latest    4203f1f50355   18 hours ago    142MB
docker-compose_java-service   latest    62f45903b396   18 hours ago    453MB
nginx                         latest    605c77e624dd   13 months ago   141MB
mysql                         5.7       c20987f18b13   13 months ago   448MB
ubuntu                        latest    ba6acccedd29   15 months ago   72.8MB
redis                         6.2.1     de974760ddb2   22 months ago   105MB
portainer/portainer           1.20.2    19d07168491a   3 years ago     74.1MB
docker@VM-8-15-ubuntu:~$ 
```

4. 创建目录：`/home/docker/docker/VOLUME/redis/`，作为挂载目录，在其中创建 `config`、`data`、`log`文件夹

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-44-728--TT0MwAtdSiSoBQ.png)

5. 在 `config` 目录内创建 `redis.conf` 文件，编辑内容

```shell
# Redis configuration file example

# Note on units: when memory size is needed, it is possible to specify
# it in the usual form of 1k 5GB 4M and so forth:
#
# 当你需要为某个配置项指定内存大小的时候，必须要带上单位，
# 通常的格式就是 1k 5gb 4m 等酱紫：
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# 单位是不区分大小写的，你写 1K 5GB 4M 也行
################################## INCLUDES ###################################
# 假如说你有一个可用于所有的 redis server 的标准配置模板，
# 但针对某些 server 又需要一些个性化的设置，
# 你可以使用 include 来包含一些其他的配置文件，这对你来说是非常有用的。
#
# 但是要注意哦，include 是不能被 config rewrite 命令改写的
# 由于 redis 总是以最后的加工线作为一个配置指令值，所以你最好是把 include 放在这个文件的最前面，
# 以避免在运行时覆盖配置的改变，相反，你就把它放在后面（外国人真啰嗦）。
# 
# include /path/to/local.conf
# include /path/to/other.conf
################################ GENERAL #####################################

# 是否在后台执行，yes：后台运行；no：不是后台运行（老版本默认）
# 由于 docker 容器在启动时，需要任务在前台运行，否则会启动后立即退出，因此导致 redis 容器启动后立即退出问题.
daemonize no

# 指定 redis 只接收来自于该 IP 地址的请求，如果不进行设置，那么将处理所有请求
#bind 127.0.0.1

# 3.2 里的参数，是否开启保护模式，默认开启。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 要是开启了密码 和 bind，可以开启。否 则最好关闭，设置为 no。
protected-mode no

#redis 的进程文件
pidfile /var/run/redis/redis-server.pid

#redis 监听的端口号。
port 6379

# 此参数确定了 TCP 连接中已完成队列(完成三次握手之后)的长度， 当然此值必须不大于 Linux 系统定义的/proc/sys/net/core/somaxconn 值，默认是 511，而 Linux 的默认参数值是 128。
# 当系统并发量大并且客户端速度缓慢的时候，可以将这二个参数一起参考设定。该内核参数默认值一般是 128，对于负载很大的服务程序来说大大的不够。
# 一般会将它修改为 2048 或者更大。在/etc/sysctl.conf 添加:net.core.somaxconn = 2048，然后在终端中执行 sysctl -p。
tcp-backlog 511

# 配置 unix socket 来让 redis 支持监听本地连接。
# unixsocket /var/run/redis/redis.sock

# 配置 unix socket 使用文件的权限
# unixsocketperm 700

# 此参数为设置客户端空闲超过 timeout，服务端会断开连接，为 0 则服务端不会主动断开连接，不能小于 0。
timeout 0

# tcp keepalive 参数。如果设置不为 0，就使用配置 tcp 的 SO_KEEPALIVE 值，
# 使用 keepalive 有两个好处：检测挂掉的对端。降低中间设备出问题而导致网络看似连接却已经与对端端口的问题。在 Linux内核中，设置了 keepalive，redis 会定时给对端发送 ack。检测到对端关闭需要两倍的设置值。
tcp-keepalive 0

# 指定了服务端日志的级别。级别包括：debug（很多信息，方便开发、测试），verbose（许多有用的信息，但是没有 debug 级别信息多），notice（适当的日志级别，适合生产环境），warn（只有非常重要的信息）
loglevel notice

# 指定了记录日志的文件。空字符串的话，日志会打印到标准输出设备。后台运行的 redis 标准输出是/dev/null。
logfile /var/log/redis/redis-server.log

#是否打开记录 syslog 功能
# syslog-enabled no

#syslog 的标识符。
# syslog-ident redis

#日志的来源、设备
# syslog-facility local0

#数据库的数量，默认使用的数据库是 DB 0。可以通过”SELECT “命令选择一个 db
databases 16

################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
save 300 10
save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data

################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master# slaveof <masterip> <masterport>
# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
# masterauth <master-password#当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。slave-serve-stale-data ye#作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。slave-priority 100
# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.

################################## SECURITY ###################################

# requirepass 配置可以让用户使用 AUTH 命令来认证密码，才能使用其他命令。这让 redis 可以使用在不受信任的网络中。
# 为了保持向后的兼容性，可以注释该命令，因为大部分用户也不需要认证。使用requirepass 的时候需要注意，因为 redis 太快了，每秒可以认证 15w 次密码，简单的密码很容易被攻破，所以最好使用一个更复杂的密码。
requirepass 000123

# 把危险的命令给修改成其他名称。比如 CONFIG 命令可以重命名为一个很难被猜到的命令，这样用户不能使用，而内部工具还能接着使用。
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52

# 设置成一个空的值，可以禁止一个命
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置能连上 redis 的最大客户端连接数量。默认是 10000 个客户端连接。
# 由于 redis 不区分连接是客户端连接还是内部打开文件或者和 slave 连接等，所以 maxclients 最小建议设置到 32。如果超过了maxclients，redis 会给新的连接发送’max number of clients reached’，并关闭连接。
# maxclients 10000

# redis 配置的最大内存容量。当内存满了，需要配合 maxmemory-policy 策略进行处理。
# 注意 slave 的输出缓冲区是不计算在 maxmemory 内的。所以为了防止主机内存使用完，建议设置的 maxmemory 要更小一些。
# maxmemory <bytes>

# 内存容量超过 maxmemory 后的处理策略。
# volatile-lru：利用 LRU 算法移除设置过过期时间的 key。
# volatile-random：随机移除设置过过期时间的 key。
# volatile-ttl：移除即将过期的 key，根据最近过期时间来删除（辅以 TTL）
# allkeys-lru：利用 LRU 算法移除任何 key。
# allkeys-random：随机移除任何 key。
# noeviction：不移除任何 key，只是返回一个写错误。
# 上面的这些驱逐策略，如果 redis 没有合适的 key 驱逐，对于写命令，还是会返回错误。redis 将不再接收写请求，只接收 get 请求。
# 写命令包括：set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort。
# maxmemory-policy noeviction

# lru 检测的样本数。使用 lru 或者 ttl 淘汰算法，从需要淘汰的列表中随机选择 sample 个 key，选出闲置时间最长的 key 移除。
# maxmemory-samples 5

############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

################################ LUA SCRIPTING ###############################

# 如果达到最大时间限制（毫秒），redis 会记个 log，然后返回 error。
# 当一个脚本超过了最大时限。只有 SCRIPT KILL 和 SHUTDOWN NOSAVE 可以用。第一个可以杀没有调 write 命令的东西。要是已经调用了 write，只能用第二个命令杀。
lua-time-limit 5000

################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
# cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
# cluster-config-file nodes-6379.conf

# 节点互连超时的阀值。集群节点超时毫秒数
# cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes

################################## SLOW LOG ###################################

# slog log 是用来记录 redis 运行中执行比较慢的命令耗时。当命令的执行超过了指定时间，就记录在 slow log 中，slog log 保存在内存中，所以没有 IO 操作。
# 执行时间比 slowlog-log-slower-than 大的请求记录到 slowlog 里面，单位是微秒，所以 1000000就是 1 秒。
# 注意，负数时间会禁用慢查询日志，而 0 则会强制记录所有命令。
# slowlog-log-slower-than 1000

# 慢查询日志长度。当一个新的命令被写进日志的时候，最老的那个记录会被删掉。这个长度没有限制。只要有足够的内存就行。你可以通过 SLOWLOG RESET 来释放内存。
slowlog-max-len 128

################################ LATENCY MONITOR ##############################

# 延迟监控功能是用来监控 redis 中执行比较缓慢的一些操作，用 LATENCY 打印 redis 实例在跑命令时的耗时图表。
# 只记录大于等于下边设置的值的操作。0 的话，就是关闭监视。默认延迟监控功能是关闭的，如果你需要打开，也可以通过 CONFIG SET 命令动态设置。
latency-monitor-threshold 0

############################# EVENT NOTIFICATION ##############################

# 键空间通知使得客户端可以通过订阅频道或模式，来接收那些以某种方式改动了 Redis 数据集的事件。因为开启键空间通知功能需要消耗一些 CPU ，所以在默认配置下，该功能处于关闭状态。
#notify-keyspace-events 的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知：
##K 键空间通知，所有通知以 __keyspace@__ 为前缀
##E 键事件通知，所有通知以 __keyevent@__ 为前缀
##g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知
##$ 字符串命令的通知
##l 列表命令的通知
##s 集合命令的通知
##h 哈希命令的通知
##z 有序集合命令的通知
##x 过期事件：每当有过期键被删除时发送
##e 驱逐(evict)事件：每当有键因为 maxmemory 政策而被删除时发送
##A 参数 g$lshzxe 的别名
# 输入的参数中至少要有一个 K 或者 E，否则的话，不管其余的参数是什么，都不会有任何 通知被分发。
# 详细使用可以参考 http://redis.io/topics/notifications
notify-keyspace-events ""

############################### ADVANCED CONFIG ###############################

# 数据量小于等于 hash-max-ziplist-entries 的用 ziplist，大于 hash-max-ziplist-entries用 hash
hash-max-ziplist-entries 512

# value 大小小于等于 hash-max-ziplist-value 的ziplist，大于 hash-max-ziplist-value 用 hash。
hash-max-ziplist-value 64

# 数据量小于等于 list-max-ziplist-entries 用 ziplist，大于 list-max-ziplist-entries用 list。
list-max-ziplist-entries 512

# value 大小小于等于 list-max-ziplist-value 的用ziplist，大于 list-max-ziplist-value 用 list。
list-max-ziplist-value 64

# 数据量小于等于 set-max-intset-entries 用 iniset，大于 set-max-intset-entries 用 set。
set-max-intset-entries 51

# 数据量小于等于 zset-max-ziplist-entries 用 ziplist，大于 zset-max-ziplist-entries用 zset。
zset-max-ziplist-entries 128

# value 大小小于等于 zset-max-ziplist-value 用 ziplist，大于 zset-max-ziplist-value 用 zset。
zset-max-ziplist-value 64


# value 大小小于等于 hll-sparse-max-bytes 使用稀疏数据结构（sparse），大于hll-sparse-max-bytes 使用稠密的数据结构（dense）。
# 一个比 16000 大的 value 是几乎没用的，建议的 value 大概为 3000。如果对 CPU 要求不高，对空间要求较高的，建议设置到 10000 左右。
hll-sparse-max-bytes 3000

# Redis 将在每 100 毫秒时使用 1 毫秒的 CPU 时间来对 redis 的 hash 表进行重新 hash，可以降低内存的使用。
# 当你的使用场景中，有非常严格的实时性需要，不能够接受 Redis 时不时的对请求有 2 毫秒的迟的话，把这项配置为 no。如果没有这么严格的实时性要求，可以设置为 yes，以便能够尽可能快的释放内存。activerehashing yes
## 对客户端输出缓冲进行限制可以强迫那些不从服务器读取数据的客户端断开连接，用来强制关闭传输缓慢的客户端。
# 对于 normal client，第一个 0 表示取消 hard limit，第二个 0 和第三个 0 表示取消 soft limit，normal client 默认取消限制，因为如果没有寻问，他们是不会接收数据的。
client-output-buffer-limit normal 0 0 0

# 对于 slave client 和 MONITER client，如果client-output-buffer 一旦超过 256mb，又或者超过 64mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit slave 256mb 64mb 60

# 对于 pubsub client，如果client-output-buffer 一旦超过 32mb，又或者超过 8mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit pubsub 32mb 8mb 60


# redis 执行任务的频率为 1s 除以 hzhz 10
# 在 aof 重写的时候，如果打开了 aof-rewrite-incremental-fsync 开关，系统会每 32MB 执行一次 fsync。这对于把文件写入磁盘是有帮助的，可以避免过大的延迟峰值。
aof-rewrite-incremental-fsync yes
```

6. 进入 `log` 文件夹，创建 `redis-server.log` 文件，给予读写权限：`666`
7. 启动容器：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:6379 --name redis -v /home/docker/docker/VOLUME/redis/config:/etc/redis -v /home/docker/docker/VOLUME/redis/data:/data -v /home/docker/docker/VOLUME/redis/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
   1. `–restart=always` 总是开机启动
   2. `–log` 是日志方面的
   3. `-p 3360:6379` 将宿主机的3360端口映射到容器的6379端口出去
   4. `–name` 给这个容器取一个名字
   5. `-v` 数据卷挂载
   6. `-d` 表示后台启动redis
   7. `redis:6.2.1` 表示启动 redis 的 6.2.1 版本
   8. `redis-server /etc/redis/redis.conf` 以配置文件启动 redis，加载容器内的 conf 文件，最终找到的是挂载的目录 /etc/redis/redis.conf 也就是 liunx 下的 `/home/docker/docker/VOLUME/redis/config/redis.conf`

```shell
docker@VM-8-15-ubuntu:~$ docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:6379 --name redis -v /home/docker/docker/VOLUME/redis/config:/etc/redis -v /home/docker/docker/VOLUME/redis/data:/data -v /home/docker/docker/VOLUME/redis/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf
61f0938de5f4a65a03328ad296f1e562ee299b039fe845e26d08d1aa56d720d5

docker@VM-8-15-ubuntu:~$ 
```

8. 查看是否启动成功：`docker ps`

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                       NAMES
61f0938de5f4   redis:6.2.1                   "docker-entrypoint.s…"   3 seconds ago   Up 3 seconds   0.0.0.0:3306->6379/tcp, :::3306->6379/tcp   redis
d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   47 hours ago    Up 47 hours    0.0.0.0:80->80/tcp, :::80->80/tcp           nginx
7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   47 hours ago    Up 47 hours    0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   java-service
9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             3 days ago      Up 3 days      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp   naughty_kowalevski

docker@VM-8-15-ubuntu:~$ 
```

9. 进入容器：`docker exec -it 61f0938de5f4 bash`

```shell
docker@VM-8-15-ubuntu:~$ docker exec -it 61f0938de5f4 bash

root@61f0938de5f4:/data# 
```

10. 访问 redis：`redis-cli`

```shell
root@61f0938de5f4:/data# redis-cli

127.0.0.1:6379>
```

11. 进行身份验证，输入密码：`AUTH 000123`

```shell
127.0.0.1:6379> AUTH 000123
OK

127.0.0.1:6379>
```

12. 测试验证，显示 `PONG` 则为正常的连通状态：`ping`

```shell
127.0.0.1:6379> ping
PONG

127.0.0.1:6379> 
```

13. 关闭
   1. 进入 redis 后关闭：`SHUTDOWN`

```shell
127.0.0.1:6379> SHUTDOWN
not connected> docker@VM-8-15-ubuntu:~$ 
```

   2. 不进入 redis 关闭：`redis-cli shutdown`

```shell
root@59d3e13e8f52:/data# redis-cli shutdown
```

13. 启动：`redis-server /etc/redis/redis.conf`，不过使用 docker 容器输入 `SHUTDOWN` 就直接退出容器了，重新进入容器 redis 依然是启动的

## 4、Redis 介绍相关知识

1. 端口 6379 从何而来：非智能机（九宫格键盘）merz（Alessia  Merz） 所对应的数字

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-44-889--AEAJ06nqmrw20g.png)


2. 默认 16 个数据库，类似数组下标从 0 开始，初始默认使用 0 号库
3. 使用命令 `select <dbid>` 来切换数据库。如：`select 8`
4. 统一密码管理，所有库同样密码。
5. `dbsize`：查看当前数据库的 key 的数量
6. `flushdb` 清空当前库
7. `flushall` 通杀全部库

- Redis 是单线程 + 多路 IO 复用技术：

1. 多路复用是指使用一个线程来检查多个文件描述符（Socket）的就绪状态，比如调用 select 和 poll 函数，传入多个文件描述符，如果有一个文件描述符就绪，则返回，否则阻塞直到超时。得到就绪状态后进行真正的操作可以在同一个线程里执行，也可以启动线程执行（比如使用线程池）
2. 串行 vs 多线程 + 锁（memcached） vs 单线程 + 多路 IO 复用(Redis)
3. 与 Memcache 三点不同：支持多数据类型，支持持久化，单线程 + 多路IO复用

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F图片1.gif)

# 三、常用五大数据类型

> redis 命令中心：[http://www.redis.cn/commands.html](http://www.redis.cn/commands.html)
> 菜鸟教程：[https://www.runoob.com/redis/redis-sorted-sets.html](https://www.runoob.com/redis/redis-sorted-sets.html)

## 1、Redis 键(key）

| 命令 | 说明 |
| --- | --- |
| `set <key> <value>` | 添加 key-value 键值对到数据库 |
| `get <key>` | 根据 key 获取 value |
| `keys *` | 查看当前库所有key（查看指定库：`keys *1`） |
| `exists <key>` | 判断某个 key 是否存在 |
| `type <key>` | 查看你的 key 是什么类型 |
| `del <key>` | 删除指定的 key |
| `unlink <key>` | 根据value选择非阻塞删除；仅将 keys 从 keyspace 元数据中删除，真正的删除会在后续异步操作。 |
| `expire <key> <10>` | 10秒钟：为给定的key设置过期时间 |
| `ttl <key> ` | 查看还有多少秒过期，-1表示永不过期，-2表示已过期 |
| `select <库编号>` | 命令切换数据库（0-15） |
| `dbsize` | 查看当前数据库的key的数量 |
| `flushdb` | 清空当前库 |
| `flushall` | 通杀（清空）全部库 |

## 2、Redis 字符串(String)

### ①、简介

1. String 是 Redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value
2. String 类型是二进制安全的。意味着 Redis 的 string 可以包含任何数据。比如 jpg 图片或者序列化的对象
3. String 类型是 Redis 最基本的数据类型，一个 Redis 中字符串 value 最多可以是 512M

### ②、常用命令

| 命令 | 说明 |
| --- | --- |
| `set <key> <value>` | 添加 key-value 键值对到数据库；若是 `set key1 100` 则会识别为数字值<br/>![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-099--hJer3yiUpFz7hQ.png)<br/>1. `*EX`：key 的超时秒数<br/>2. `*PX`：key 的超时毫秒数，与 EX 互斥<br/>3. `*EXAT`：：设置 key 过期的指定 Unix 时间（以秒为单位）；<br/>4. `*PXAT`：设置 key 过期的指定 Unix 时间（以毫秒为单位）；<br/>5. `*NX`：当数据库中 key 不存在时，可以将 key-value 添加数据库<br/>6. `*XX`：当数据库中 key 存在时，可以将 key-value 添加数据库，与 NX 参数互斥<br/>|
| `get <key>` | 根据 key 获取 value |
| `setnx <key><value>` | 只有在 key 不存在时，才设置 key 的值 |
| `mset <key1> <value1> <key2> <value2> ... ` | 同时设置一个或多个 key-value 对   |
| `mget <key1> <key2> <key3> ...` | 同时获取一个或多个 value   |
| `msetnx <key1> <value1> <key2> <value2> ... ` | 同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。 |
| `keys *` | 查看当前库所有key（查看指定库：`keys *1`） |
| `append <key> <value>` | 将给定的 `<value>` 追加到原值的末尾 |
| `strlen <key>` | 获得值的长度 |
| `incr <key>` | 将 key 中储存的数字值增1；只能对数字值操作，如果为空，新增值为 1 |
| `decr <key>` | 将 key 中储存的数字值减1；只能对数字值操作，如果为空，新增值为 -1 |
| `incrby / decrby <key> <步长>` | 将 key 中储存的数字值增减。自定义步长（增减的数值）。 |
| `getrange <key> <起始位置> <结束位置>` | 获得值的范围，类似 java 中的 substring，前包，后包 |
| `setrange <key> <起始位置> <value>` | 用 `<value>`  覆写 `<key>` 所储存的字符串值，从 `<起始位置>` 开始(索引从0开始)。 |
| `setex <key> <过期时间> <value>` | 设置键值的同时，设置过期时间，单位秒。 |
| `getset <key> <value>` | 以新换旧，设置了新值同时获得旧值。 |

- 原子性：所谓原子操作是指不会被线程调度机制打断的操作；这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。

1. 在单线程中， 能够在单条指令中完成的操作都可以认为是"原子操作"，因为中断只能发生于指令之间。
2. 在多线程中，不能被其它进程（线程）打断的操作就叫原子操作。
3. Redis 单命令的原子性主要得益于 Redis 的单线程。

### ③、数据结构

1. String 的数据结构为简单动态字符串(Simple Dynamic String，缩写SDS)。是可以修改的字符串，内部结构实现上类似于 Java 的 ArrayList，采用预分配冗余空间的方式来减少内存的频繁分配.
2. 如图中所示，内部为当前字符串实际分配的空间 capacity 一般要高于实际字符串长度 en。当字符串长度小于 1M 时，扩容都是加倍现有的空间，如果超过 1M，扩容时一次只会多扩 1M 的空间。需要注意的是字符串最大长度为 512M。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-190--PCKjuygzkfJUVw.png)

## 3、Redis 列表(List)

### ①、简介

1. 单键多值，有序可重复
2. Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
3. 它的底层实际是个双向链表，对两端的操作性能很高，通过索引下标的操作中间的节点性能会较差。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-305--Hcg04ubRlIAeWQ.png)

### ②、常用命令

| 命令 | 说明 |
| --- | --- |
| `lpush/rpush <key> <value1> <value2> <value3> .... ` | 从左边/右边插入一个或多个值。 |
| `lpop/rpop <key>` | 从左边/右边吐出一个值（输出并删除这个值）。值在键在，值光键亡。 |
| `rpoplpush <key1> <key2>` | 从 key1 列表右边吐出一个值，插到 key2 列表左边；<br/>即将key1 的最后一个值放到 key2 的第一个值 |
| `lrange <key> <start> <stop>` | 按照索引下标获得一个或多个元素(从左到右)<br/>`lrange <key> 0 -1`： 0 左边第一个，-1右边第一个，（0 -1表示获取所有） |
| `lindex <key> <index>` | 按照索引下标获得指定位置的元素 |
| `llen <key>` | 获得列表长度 |
| `linsert <key> before <value> <newvalue>` | 在指定 key 的指定 value 的前面插入新值 newvalue；有相同的 value 则只在最左边前面加 |
| `linsert <key> after <value> <newvalue>` | 在指定 key 的指定 value 的后面插入新值 newvalue；有相同的 value 则只在最左边后面加 |
| `lrem <key> <n> <value>` | 从左边删除 n 个指定的 value(从左到右) |
| `lset <key> <index> <value>` | 将列表 key下标为 index 的值替换成 value |

### ③、数据结构

1. List 的数据结构为快速链表 quickList。
2. 首先在列表元素较少的情况下会使用一块连续的内存存储，这个结构是 ziplist，也即是压缩列表。
3. 它将所有的元素紧挨着一起存储，分配的是一块连续的内存。
4. 当数据量比较多的时候才会改成 quicklist。
5. 因为普通的链表需要的附加指针空间太大，会比较浪费空间。比如这个列表里存的只是 int 类型的数据，结构上还需要两个额外的指针 prev 和 next。
6. Redis 将链表和 ziplist 结合起来组成了 quicklist。也就是将多个 ziplist 使用双向指针串起来使用。这样既满足了快速的插入删除性能，又不会出现太大的空间冗余。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-452--c5PCsS87YJ9BAg.png)

## 4、Redis 集合(Set)

### ①、简介

1. 无序不可重复
2. Redis set 对外提供的功能与 list 似是一个列表的功能，特殊之处在于 set 是可以自动排重（不可重复）的，当你需要存储一个列表数据，又不希望出现重复数据时，set 是一个很好的选择，并且 set 提供了判断某个成员是否在一个 set 集合内的重要接口，这个也是 list 所不能提供的。
3. Redis 的 Set 是 string 类型的无序集合。它底层其实是一个 value 为 null 的 hash 表，所以添加，删除，查找的复杂度都是O(1)。
4. 一个算法，随着数据的增加，执行时间的长短，如果是O(1)，数据增加，查找数据的时间不变

### ②、常用命令

| 命令 | 描述 |
| --- | --- |
| `SADD key member1 [member2]` | 向集合添加一个或多个成员 |
| `SCARD key` | 获取指定集合的成员数量 |
| `SMEMBERS key` | 返回指定集合中的所有成员 |
| `SISMEMBER key member` | 判断 member 元素是否是指定集合 key 的成员 |
| `SPOP key` | 移除并返回指定集合中的一个随机元素 |
| `SRANDMEMBER key [count]` | 返回指定集合中一个或多个随机数 |
| `SREM key member1 [member2]` | 移除指定集合中一个或多个成员 |
| `SSCAN key cursor [MATCH pattern] [COUNT count]` | 迭代指定集合中的元素 |
| `SMOVE source destination member` | 将 member 元素从 source 集合移动到 destination 集合 |
| `SINTER key1 [key2]` | 返回给定所有集合的交集 |
| `SUNION key1 [key2]` | 返回所有给定集合的并集 |
| `SDIFF key1 [key2]` | 返回第一个集合与其他集合之间的差异。 |
| `SDIFFSTORE destination key1 [key2]` | 返回给定所有集合的差集并存储在 destination 中 |
| `SINTERSTORE destination key1 [key2]` | 返回给定所有集合的交集并存储在 destination 中 |
| `SUNIONSTORE destination key1 [key2]` | 所有给定集合的并集存储在 destination 集合中 |

### ③、数据结构

1. Set 数据结构是 dict 字典，字典是用哈希表实现的。
2. Java 中 HashSet 的内部实现使用的是 HashMap，只不过所有的 value 都指向同一个对象。
3. Redis 的 set 结构也是一样，它的内部也使用 hash 结构，所有的 value 都指向同一个内部值。

## 5、Redis 哈希(Hash)

### ①、简介

1. Redis hash 是一个键值对集合。
2. Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
3. 类似 Java 里面的 Map<String, Object>
4. 用户 ID 为查找的 key，存储的 value 用户对象包含姓名，年龄，生日等信息，如果用普通的 key/value 结构来存储
5. 主要有以下2种存储方式：
   1. 每次修改用户的某个属性需要，先反序列化改好后再序列化回去。开销较大。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-562--4Lr-r_deF1Rlew.png)

   2. 用户 ID 数据冗余

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-708--zE-F9xKr2Gd01A.png)

6. 通过 key(用户ID) + field(属性标签) 就可以操作对应属性数据了，既不需要重复存储数据，也不会带来序列化和并发修改控制的问题

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-905--l2WBKwXhtfrZLA.png)

### ②、常用命令

| 序号 | 命令及描述 |
| --- | --- |
| `HSET key field value [field value]` | 将哈希表 key 中的字段 field 的值设为 value 。<br/>![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-45-955--wbELlivSsASKTg.png)|
| `HSETNX key field value` | 只有在键 field 不存在时，设置哈希表字段的值。 |
| `HGET key field` | 获取存储在哈希表中指定字段的值。 |
| `HLEN key` | 获取指定哈希表中字段的数量 |
| `HKEYS key` | 获取指定哈希表中所有 field  |
| `HGETALL key` | 获取哈希表中指定 key 的所有字段和值 |
| `HVALS key` | 获取哈希表中所有值。 |
| `HMGET key field1 [field2]` | 获取所有给定字段的值 |
| `HEXISTS key field` | 查看哈希表 key 中，指定的字段是否存在。 |
| `HINCRBY key field increment` | 为哈希表 key 中的指定字段的整数值加上增量 increment 。 |
| `HINCRBYFLOAT key field increment` | 为哈希表 key 中的指定字段的浮点数值加上增量 increment 。 |
| `HDEL key field1 [field2]` | 删除一个或多个哈希表字段 |
| `HSCAN key cursor [MATCH pattern] [COUNT count]` | 迭代哈希表中的键值对。 |

### ③、数据结构

1. Hash类型对应的数据结构是两种：ziplist（压缩列表），hashtable（哈希表）。
2. 当field-value长度较短且个数较少时，使用ziplist，否则使用hashtable。

## 6、Redis 有序集合 Zset(sorted set) 

### ①、简介

1. Redis 有序集合 zset 与普通集合 set 非常相似，是一个没有重复元素的字符串集合。
2. 不同之处是有序集合的每个成员都关联了一个评分（score），这个评分（score）被用来按照从最低分到最高分的方式排序集合中的成员。
3. 集合的成员是唯一的，但是评分可以是重复了的。
4. 因为元素是有序的, 所以你也可以很快的根据评分（score）或者次序（position）来获取一个范围的元素。
5. 访问有序集合的中间元素也是非常快的，因此你能够使用有序集合作为一个没有重复成员的智能列表。

### ②、常用命令

| 序号 | 命令及描述 |
| --- | --- |
| `zadd <key> <score1> <value1> <score2> <value2> …` | 将一个或多个 member 元素及其 score 值加入到有序集 key 当中。<br/><br/>127.0.0.1:6379> zadd yuehai 100 java 200 vue 300 mysql 400 php<br/>(integer) 4<br/><br/>127.0.0.1:6379> zrange yuehai <br/>|
| `zrange <key> <start><stop> [WITHSCORES]` | 返回有序集 key 中，下标在 `<start><stop>` 之间的元素带 WITHSCORES，可以让分数一起和值返回到结果集。<br/><br/>127.0.0.1:6379> zrange yuehai 0 1<br/>1) "java"<br/>2) "vue"<br/><br/>127.0.0.1:6379> zrange yuehai 0 -1<br/>1) "java"<br/>2) "vue"<br/>3) "mysql"<br/>4) "php"<br/><br/>127.0.0.1:6379> zrange yuehai 0 -1 withscores<br/>1) "java"<br/>2) "100"<br/>3) "vue"<br/>4) "200"<br/>5) "mysql"<br/>6) "300"<br/>7) "php"<br/>8) "400"<br/><br/>127.0.0.1:6379> <br/>|
| `zrangebyscore key min max [withscores] [limit offset count]` | 返回有序集 key 中，所有 score 值介于 min 和 max 之间(包括等于 min 或 max )的成员。<br/>有序集成员按 score 值递增(从小到大)次序排列。 <br/><br/>127.0.0.1:6379> ZRANGEBYSCORE yuehai 100 300<br/>1) "java"<br/>2) "vue"<br/>3) "mysql"<br/><br/>127.0.0.1:6379> ZRANGEBYSCORE yuehai 100 300 WITHSCORES<br/>1) "java"<br/>2) "100"<br/>3) "vue"<br/>4) "200"<br/>5) "mysql"<br/>6) "300"<br/><br/>127.0.0.1:6379> <br/>|
| `zrevrangebyscore key max min [withscores] [limit offset count]` | 同上，改为从大到小排列。  |
| `zincrby <key><increment><value>` | 为元素的score加上增量 |
| `zrem  <key><value>` | 删除该集合下，指定值的元素  |
| `zcount <key><min><max>` | 统计该集合，分数区间内的元素个数  |
| `zrank <key><value>` | 返回该值在集合中的排名，从0开始。 |

### ③、数据结构

1. SortedSet(zset) 是 Redis 提供的一个非常特别的数据结构，一方面它等价于 Java 的数据结构 Map<String, Double>，可以给每一个元素 value 赋予一个权重 score，另一方面它又类似于 TreeSet，内部的元素会按照权重 score 进行排序，可以得到每个元素的名次，还可以通过 score 的范围来获取元素的列表。
2. zset 底层使用了两个数据结构
   1. hash：hash 的作用就是关联元素 value 和权重 score，保障元素 value 的唯一性，可以通过元素 value 找到相应的 score 值。
   2. 跳跃表：跳跃表的目的在于给元素 value 排序，根据 score 的范围获取元素列表。

### ④、跳跃表（跳表）

#### Ⅰ、简介

1. 有序集合在生活中比较常见，例如根据成绩对学生排名，根据得分对玩家排名等。
2. 对于有序集合的底层实现，可以用数组、平衡树、链表等。
   1. 数组不便元素的插入、删除；
   2. 平衡树或红黑树虽然效率高但结构复杂；
   3. 链表查询需要遍历所有效率低。
3. Redis 采用的是跳跃表。跳跃表效率堪比红黑树，实现远比红黑树简单。

#### Ⅱ、实例

- 对比有序链表和跳跃表，从链表中查询出 51
1. 有序链表：要查找值为51的元素，需要从第一个元素开始依次查找、比较才能找到。共需要 6 次比较

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-068--f85CBSDn_l7lxg.png)

2. 跳跃表
   1. 从第 2 层开始，1 节点比 51 节点小，向后比较。
   2. 21 节点比 51 节点小，继续向后比较，后面就是 NULL 了，所以从 21 节点向下到第1层
   3. 在第 1 层，41 节点比 51 节点小，继续向后，61 节点比 51 节点大，所以从 41 向下
   4. 在第 0 层，51 节点为要查找的节点，节点被找到，共查找 4 次。
   5. 从此可以看出跳跃表比有序链表效率要高

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-170--u6xGAXwPm0OyLw.png)

# 四、Redis 配置文件介绍

> [https://blog.csdn.net/weixin_36065860/article/details/109025668](https://blog.csdn.net/weixin_36065860/article/details/109025668)

```shell
# Redis configuration file example

# Note on units: when memory size is needed, it is possible to specify
# it in the usual form of 1k 5GB 4M and so forth:
#
# 当你需要为某个配置项指定内存大小的时候，必须要带上单位，
# 通常的格式就是 1k 5gb 4m 等酱紫：
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# 单位是不区分大小写的，你写 1K 5GB 4M 也行
################################## INCLUDES ###################################
# 假如说你有一个可用于所有的 redis server 的标准配置模板，
# 但针对某些 server 又需要一些个性化的设置，
# 你可以使用 include 来包含一些其他的配置文件，这对你来说是非常有用的。
#
# 但是要注意哦，include 是不能被 config rewrite 命令改写的
# 由于 redis 总是以最后的加工线作为一个配置指令值，所以你最好是把 include 放在这个文件的最前面，
# 以避免在运行时覆盖配置的改变，相反，你就把它放在后面（外国人真啰嗦）。
# 
# include /path/to/local.conf
# include /path/to/other.conf
################################ GENERAL #####################################

# 是否在后台执行，yes：后台运行；no：不是后台运行（老版本默认）
# 由于 docker 容器在启动时，需要任务在前台运行，否则会启动后立即退出，因此导致 redis 容器启动后立即退出问题.
daemonize no

# 指定 redis 只接收来自于该 IP 地址的请求，如果不进行设置，那么将处理所有请求
#bind 127.0.0.1

# 3.2 里的参数，是否开启保护模式，默认开启。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 要是开启了密码 和 bind，可以开启。否 则最好关闭，设置为 no。
protected-mode no

#redis 的进程文件
pidfile /var/run/redis/redis-server.pid

#redis 监听的端口号。
port 6379

# 此参数确定了 TCP 连接中已完成队列(完成三次握手之后)的长度， 当然此值必须不大于 Linux 系统定义的/proc/sys/net/core/somaxconn 值，默认是 511，而 Linux 的默认参数值是 128。
# 当系统并发量大并且客户端速度缓慢的时候，可以将这二个参数一起参考设定。该内核参数默认值一般是 128，对于负载很大的服务程序来说大大的不够。
# 一般会将它修改为 2048 或者更大。在/etc/sysctl.conf 添加:net.core.somaxconn = 2048，然后在终端中执行 sysctl -p。
tcp-backlog 511

# 配置 unix socket 来让 redis 支持监听本地连接。
# unixsocket /var/run/redis/redis.sock

# 配置 unix socket 使用文件的权限
# unixsocketperm 700

# 此参数为设置客户端空闲超过 timeout，服务端会断开连接，为 0 则服务端不会主动断开连接，不能小于 0。
timeout 0

# tcp keepalive 参数。如果设置不为 0，就使用配置 tcp 的 SO_KEEPALIVE 值，
# 使用 keepalive 有两个好处：检测挂掉的对端。降低中间设备出问题而导致网络看似连接却已经与对端端口的问题。在 Linux内核中，设置了 keepalive，redis 会定时给对端发送 ack。检测到对端关闭需要两倍的设置值。
tcp-keepalive 0

# 指定了服务端日志的级别。级别包括：debug（很多信息，方便开发、测试），verbose（许多有用的信息，但是没有 debug 级别信息多），notice（适当的日志级别，适合生产环境），warn（只有非常重要的信息）
loglevel notice

# 指定了记录日志的文件。空字符串的话，日志会打印到标准输出设备。后台运行的 redis 标准输出是/dev/null。
logfile /var/log/redis/redis-server.log

#是否打开记录 syslog 功能
# syslog-enabled no

#syslog 的标识符。
# syslog-ident redis

#日志的来源、设备
# syslog-facility local0

#数据库的数量，默认使用的数据库是 DB 0。可以通过”SELECT “命令选择一个 db
databases 16

################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
save 300 10
save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data

################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master# slaveof <masterip> <masterport>
# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
# masterauth <master-password#当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。slave-serve-stale-data ye#作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。slave-priority 100
# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.

################################## SECURITY ###################################

# requirepass 配置可以让用户使用 AUTH 命令来认证密码，才能使用其他命令。这让 redis 可以使用在不受信任的网络中。
# 为了保持向后的兼容性，可以注释该命令，因为大部分用户也不需要认证。使用requirepass 的时候需要注意，因为 redis 太快了，每秒可以认证 15w 次密码，简单的密码很容易被攻破，所以最好使用一个更复杂的密码。
requirepass 000123

# 把危险的命令给修改成其他名称。比如 CONFIG 命令可以重命名为一个很难被猜到的命令，这样用户不能使用，而内部工具还能接着使用。
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52

# 设置成一个空的值，可以禁止一个命
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置能连上 redis 的最大客户端连接数量。默认是 10000 个客户端连接。
# 由于 redis 不区分连接是客户端连接还是内部打开文件或者和 slave 连接等，所以 maxclients 最小建议设置到 32。如果超过了maxclients，redis 会给新的连接发送’max number of clients reached’，并关闭连接。
# maxclients 10000

# redis 配置的最大内存容量。当内存满了，需要配合 maxmemory-policy 策略进行处理。
# 注意 slave 的输出缓冲区是不计算在 maxmemory 内的。所以为了防止主机内存使用完，建议设置的 maxmemory 要更小一些。
# maxmemory <bytes>

# 内存容量超过 maxmemory 后的处理策略。
# volatile-lru：利用 LRU 算法移除设置过过期时间的 key。
# volatile-random：随机移除设置过过期时间的 key。
# volatile-ttl：移除即将过期的 key，根据最近过期时间来删除（辅以 TTL）
# allkeys-lru：利用 LRU 算法移除任何 key。
# allkeys-random：随机移除任何 key。
# noeviction：不移除任何 key，只是返回一个写错误。
# 上面的这些驱逐策略，如果 redis 没有合适的 key 驱逐，对于写命令，还是会返回错误。redis 将不再接收写请求，只接收 get 请求。
# 写命令包括：set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort。
# maxmemory-policy noeviction

# lru 检测的样本数。使用 lru 或者 ttl 淘汰算法，从需要淘汰的列表中随机选择 sample 个 key，选出闲置时间最长的 key 移除。
# maxmemory-samples 5

############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

################################ LUA SCRIPTING ###############################

# 如果达到最大时间限制（毫秒），redis 会记个 log，然后返回 error。
# 当一个脚本超过了最大时限。只有 SCRIPT KILL 和 SHUTDOWN NOSAVE 可以用。第一个可以杀没有调 write 命令的东西。要是已经调用了 write，只能用第二个命令杀。
lua-time-limit 5000

################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
# cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
# cluster-config-file nodes-6379.conf

# 节点互连超时的阀值。集群节点超时毫秒数
# cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes

################################## SLOW LOG ###################################

# slog log 是用来记录 redis 运行中执行比较慢的命令耗时。当命令的执行超过了指定时间，就记录在 slow log 中，slog log 保存在内存中，所以没有 IO 操作。
# 执行时间比 slowlog-log-slower-than 大的请求记录到 slowlog 里面，单位是微秒，所以 1000000就是 1 秒。
# 注意，负数时间会禁用慢查询日志，而 0 则会强制记录所有命令。
# slowlog-log-slower-than 1000

# 慢查询日志长度。当一个新的命令被写进日志的时候，最老的那个记录会被删掉。这个长度没有限制。只要有足够的内存就行。你可以通过 SLOWLOG RESET 来释放内存。
slowlog-max-len 128

################################ LATENCY MONITOR ##############################

# 延迟监控功能是用来监控 redis 中执行比较缓慢的一些操作，用 LATENCY 打印 redis 实例在跑命令时的耗时图表。
# 只记录大于等于下边设置的值的操作。0 的话，就是关闭监视。默认延迟监控功能是关闭的，如果你需要打开，也可以通过 CONFIG SET 命令动态设置。
latency-monitor-threshold 0

############################# EVENT NOTIFICATION ##############################

# 键空间通知使得客户端可以通过订阅频道或模式，来接收那些以某种方式改动了 Redis 数据集的事件。因为开启键空间通知功能需要消耗一些 CPU ，所以在默认配置下，该功能处于关闭状态。
#notify-keyspace-events 的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知：
##K 键空间通知，所有通知以 __keyspace@__ 为前缀
##E 键事件通知，所有通知以 __keyevent@__ 为前缀
##g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知
##$ 字符串命令的通知
##l 列表命令的通知
##s 集合命令的通知
##h 哈希命令的通知
##z 有序集合命令的通知
##x 过期事件：每当有过期键被删除时发送
##e 驱逐(evict)事件：每当有键因为 maxmemory 政策而被删除时发送
##A 参数 g$lshzxe 的别名
# 输入的参数中至少要有一个 K 或者 E，否则的话，不管其余的参数是什么，都不会有任何 通知被分发。
# 详细使用可以参考 http://redis.io/topics/notifications
notify-keyspace-events ""

############################### ADVANCED CONFIG ###############################

# 数据量小于等于 hash-max-ziplist-entries 的用 ziplist，大于 hash-max-ziplist-entries用 hash
hash-max-ziplist-entries 512

# value 大小小于等于 hash-max-ziplist-value 的ziplist，大于 hash-max-ziplist-value 用 hash。
hash-max-ziplist-value 64

# 数据量小于等于 list-max-ziplist-entries 用 ziplist，大于 list-max-ziplist-entries用 list。
list-max-ziplist-entries 512

# value 大小小于等于 list-max-ziplist-value 的用ziplist，大于 list-max-ziplist-value 用 list。
list-max-ziplist-value 64

# 数据量小于等于 set-max-intset-entries 用 iniset，大于 set-max-intset-entries 用 set。
set-max-intset-entries 51

# 数据量小于等于 zset-max-ziplist-entries 用 ziplist，大于 zset-max-ziplist-entries用 zset。
zset-max-ziplist-entries 128

# value 大小小于等于 zset-max-ziplist-value 用 ziplist，大于 zset-max-ziplist-value 用 zset。
zset-max-ziplist-value 64


# value 大小小于等于 hll-sparse-max-bytes 使用稀疏数据结构（sparse），大于hll-sparse-max-bytes 使用稠密的数据结构（dense）。
# 一个比 16000 大的 value 是几乎没用的，建议的 value 大概为 3000。如果对 CPU 要求不高，对空间要求较高的，建议设置到 10000 左右。
hll-sparse-max-bytes 3000

# Redis 将在每 100 毫秒时使用 1 毫秒的 CPU 时间来对 redis 的 hash 表进行重新 hash，可以降低内存的使用。
# 当你的使用场景中，有非常严格的实时性需要，不能够接受 Redis 时不时的对请求有 2 毫秒的迟的话，把这项配置为 no。如果没有这么严格的实时性要求，可以设置为 yes，以便能够尽可能快的释放内存。activerehashing yes
## 对客户端输出缓冲进行限制可以强迫那些不从服务器读取数据的客户端断开连接，用来强制关闭传输缓慢的客户端。
# 对于 normal client，第一个 0 表示取消 hard limit，第二个 0 和第三个 0 表示取消 soft limit，normal client 默认取消限制，因为如果没有寻问，他们是不会接收数据的。
client-output-buffer-limit normal 0 0 0

# 对于 slave client 和 MONITER client，如果client-output-buffer 一旦超过 256mb，又或者超过 64mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit slave 256mb 64mb 60

# 对于 pubsub client，如果client-output-buffer 一旦超过 32mb，又或者超过 8mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit pubsub 32mb 8mb 60


# redis 执行任务的频率为 1s 除以 hzhz 10
# 在 aof 重写的时候，如果打开了 aof-rewrite-incremental-fsync 开关，系统会每 32MB 执行一次 fsync。这对于把文件写入磁盘是有帮助的，可以避免过大的延迟峰值。
aof-rewrite-incremental-fsync yes
```

# 五、Redis 新数据类型

## 1、位 Bitmaps

### ①、简介

1. 现代计算机用二进制（位） 作为信息的基础单位， 1 个字节等于 8 位， 例如“abc”字符串是由 3 个字节组成， 但实际在计算机存储时将其用二进制表示， “abc”分别对应的 ASCII 码分别是 97、 98、 99， 对应的二进制分别是 01100001、 01100010 和 01100011，如下图

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-296--qdoJvGiNtKLvXQ.png)

2. 合理地使用操作位能够有效地提高内存使用率和开发效率。
3. Redis 提供了 Bitmaps 这个“数据类型”可以实现对位的操作：
4. Bitmaps 本身不是一种数据类型， 实际上它就是字符串（key-value） ， 但是它可以对字符串的位进行操作。
5. Bitmaps 单独提供了一套命令， 所以在 Redis 中使用 Bitmaps 和使用字符串的方法不太相同。 可以把 Bitmaps 想象成一个以位为单位的数组， 数组的每个单元只能存储 0 和 1， 数组的下标在 Bitmaps 中叫做偏移量。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-514--To6pB9ElCddVfA.png)

### ②、常用命令

#### Ⅰ、setbit

1. 功能：设置 Bitmaps 中某个偏移量的值（0或1）
2. 格式：`setbit <key> <offset> <value>`
3. 实例

```shell
127.0.0.1:6379> SETBIT user 1 1
(integer) 0

127.0.0.1:6379> SETBIT user 2 0
(integer) 0

127.0.0.1:6379> SETBIT user 5 0
(integer) 0

127.0.0.1:6379> SETBIT user 6 1
(integer) 0

127.0.0.1:6379> SETBIT user 9 1
(integer) 0

127.0.0.1:6379>
```

4. 设置键的第 offset 个位的值（从0算起） ， 假设现在有20个用户，userid=1， 6， 11， 15， 19的用户对网站进行了访问， 那么当前 Bitmaps 初始化结果如图

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-649--D1Tu2Py13e6JoQ.png)

5. 在第一次初始化 Bitmaps 时， 假如偏移量非常大， 那么整个初始化过程执行会比较慢， 可能会造成 Redis 的阻塞。

#### Ⅱ、getbit

1. 功能：获取 Bitmaps 中某个偏移量的值
2. 格式：`getbit <key> <offset>`
3. 实例：因为 8 和 100 根本不存在，所以也是返回 0

```shell
127.0.0.1:6379> GETBIT user 1
(integer) 1

127.0.0.1:6379> GETBIT user 9
(integer) 1

127.0.0.1:6379> GETBIT user 8
(integer) 0

127.0.0.1:6379> GETBIT user 5
(integer) 0

127.0.0.1:6379> GETBIT user 100
(integer) 0

127.0.0.1:6379> 
```

#### Ⅲ、bitcount

1. 功能：统计字符串从 start 字节到 end 字节比特值为 1 的数量
   1. 一般情况下，给定的整个字符串都会被进行计数，通过指定额外的 start 或 end 参数，可以让计数只在特定的位上进行。
   2. start 和 end 参数的设置，都可以使用负数值：比如 -1 表示最后一个位，而 -2 表示倒数第二个位，start、end 是指 bit 组的字节的下标数，二者皆包含。
2. 格式：`bitcount <key> [start end]`
3. 实例

```shell
127.0.0.1:6379> BITCOUNT user
(integer) 3

127.0.0.1:6379> BITCOUNT user 1 5
(integer) 1

127.0.0.1:6379> 
```

#### Ⅳ、bitop

1. 功能：bitop 是一个复合操作， 它可以做多个 Bitmaps 的 and（交集） 、 or（并集） 、 not（非） 、 xor（异或） 操作并将结果保存在 destkey 中。
2. 格式：`bitop and(or/not/xor) <destkey> [key…]`
3. 实例
   1. 2020-11-04 日访问网站的userid=1,2,5,9。
      1. setbit unique:users:20201104 1 1
      2. setbit unique:users:20201104 2 1
      3. setbit unique:users:20201104 5 1
      4. setbit unique:users:20201104 9 1
   2. 2020-11-03 日访问网站的userid=0,1,4,9。	
      1. setbit unique:users:20201103 0 1
      2. setbit unique:users:20201103 1 1
      3. setbit unique:users:20201103 4 1
      4. setbit unique:users:20201103 9 1
   3. 计算出两天都访问过网站的用户数量：`bitop and unique:users:and:20201104_03 unique:users:20201103 unique:users:20201104`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-787--K0ddPXbSSdXVlQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-46-924--ku8uhvQnHAbISw.png)

   4. 计算出任意一天都访问过网站的用户数量（例如月活跃就是类似这种） ， 可以使用or求并集

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-109--zI6VlTZhzXwU3Q.png)

### ③、Bitmaps 与 set 对比

1. 假设网站有1亿用户，每天独立访问的用户有5千万，如果每天用集合类型和 Bitmaps 分别存储活跃用户可以得到表

| set 和 Bitmaps 存储一天活跃用户对比 |  |  |  |
| --- | --- | --- | --- |
| 数据类型 | 每个用户id占用空间 | 需要存储的用户量 | 全部内存量 |
| 集合类型 | 64位 | 50000000 | `64位*50000000 = 400MB` |
| Bitmaps | 1位 | 100000000 | 1位*100000000 = 12.5MB |

2. 很明显，这种情况下使用 Bitmaps 能节省很多的内存空间，尤其是随着时间推移节省的内存还是非常可观的

| set 和 Bitmaps 存储独立用户空间对比 |  |  |  |
| --- | --- | --- | --- |
| 数据类型 | 一天 | 一个月 | 一年 |
| 集合类型 | 400MB | 12GB | 144GB |
| Bitmaps | 12.5MB | 375MB | 4.5GB |

3. 但 Bitmaps 并不是万金油，假如该网站每天的独立访问用户很少，例如只有10万（大量的僵尸用户），那么两者的对比如下表所示，很显然，这时候使用 Bitmaps 就不太合适了，因为基本上大部分位都是0。

| set和Bitmaps存储一天活跃用户对比（独立用户比较少） |  |  |  |
| --- | --- | --- | --- |
| 数据类型 | 每个userid占用空间 | 需要存储的用户量 | 全部内存量 |
| 集合类型 | 64位 | 100000 | 64位*100000 = 800KB |
| Bitmaps | 1位 | 100000000 | 1位*100000000 = 12.5MB |

## 2、基数 HyperLogLog

### ①、简介

1. 在工作当中，我们经常会遇到与统计相关的功能需求，比如统计网站 PV（PageView页面访问量）,可以使用 Redis 的 incr、incrby 轻松实现。
2. 但像 UV（UniqueVisitor，独立访客）、独立IP数、搜索记录数等需要去重和计数的问题如何解决？这种求集合中不重复元素个数的问题称为基数问题。
3. 解决基数问题有很多种方案：
   1. 数据存储在 MySQL 表中，使用 distinct count 计算不重复个数
   2. 使用 Redis 提供的 hash、set、bitmaps 等数据结构来处理
4. 以上的方案结果精确，但随着数据不断增加，导致占用空间越来越大，对于非常大的数据集是不切实际的。
5. 能否能够降低一定的精度来平衡存储空间？Redis 推出了 HyperLogLog
6. Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定的、并且是很小的。
7. 在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。
8. 但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。
9. 什么是基数：比如数据集 {1, 3, 5, 7, 5, 7, 8}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8}，基数(不重复元素)为 5。 基数估计就是在误差可接受的范围内，快速计算基数。

### ②、常用命令

#### Ⅰ、pfadd

1. 功能：添加指定元素到 HyperLogLog 中
2. 格式：`pfadd <key> <element> [element ...]`
3. 实例：将所有元素添加到指定 HyperLogLog 数据结构中。如果执行命令后 HLL 估计的近似基数发生变化，则返回 1，否则返回 0

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-221---x2gLHPvs_JjZw.png)

#### Ⅱ、pfcount

1. 功能：计算 HLL 的近似基数，可以计算多个 HLL，比如用 HLL 存储每天的 UV，计算一周的 UV 可以使用 7 天的 UV 合并计算即可
2. 格式：`pfcount <key> [key ...]`
3. 实例：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-373--VxmPa6_ZzjQF9Q.png)

#### Ⅲ、pfmerge

1. 功能：将一个或多个 HLL 合并后的结果存储在另一个 HLL 中，比如每月活跃用户可以使用每天的活跃用户来合并计算可得
2. 格式：`pfmerge <destkey> <sourcekey> [sourcekey ...]`
3. 实例：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-503--qW3xVH4O3z1aXw.png)

## 3、地理信息 Geospatial

### ①、简介

1. Redis 3.2 中增加了对 GEO 类型的支持。
2. GEO，Geographic，地理信息的缩写。
3. 该类型，就是元素的 2 维坐标，在地图上就是经纬度。redis 基于该类型，提供了经纬度设置，查询，范围查询，距离查询，经纬度 Hash 等常见操作

### ②、常用命令

#### Ⅰ、geoadd

1. 功能：添加地理位置（经度，纬度，名称）
2. 格式：`geoadd<key>< longitude><latitude><member> [longitude latitude member...]`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-643--mKibOINZsb8cNQ.png)

3. 实例：
   1. 两极无法直接添加，一般会下载城市数据，直接通过 Java 程序一次性导入。
   2. 有效的经度从 -180 度到 180 度。有效的纬度从 -85.05112878 度到 85.05112878 度。
   3. 当坐标位置超出指定范围时，该命令将会返回一个错误。
   4. 已经添加的数据，是无法再次往里面添加的

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-844--AbrrB1pf32hJ0Q.png)

#### Ⅱ、geopos

1. 功能：获得指定地区的坐标值
2. 格式：`geopos <key> <member> [member...]`
3. 实例：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-47-960--6OIMf5ZBxRct1A.png)

#### Ⅲ、geodist

1. 功能：获取两个位置之间的直线距离
2. 格式：`geodist <key> <member1> <member2> [m|km|ft|mi ]`
3. 实例：获取两个位置之间的直线距离
   1. m 表示单位为米[默认值]。
   2. km 表示单位为千米。
   3. mi 表示单位为英里。
   4. ft 表示单位为英尺。
   5. 如果用户没有显式地指定单位参数， 那么 GEODIST 默认使用米作为单位

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-097--zWeAPMjH7QSewg.png)

#### Ⅳ、georadius

1. 功能：以给定的经纬度为中心，找出某一半径内的元素
2. 格式：`georadius <key> <longitude> <latitude> radius  m|km|ft|mi`，经度 纬度 距离 单位
3. 实例：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-178--ifRRDBRL2Wa8aQ.png)

# 六、Redis Jedis 测试

## 1、创建项目

1. 父项目开始时设置依赖

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-323--QC7GMv3etzNPCA.png)

2. 创建子项目

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-379--tykaDVK_sKgAFQ.png)

3. 父项目 pom.xml 设置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.11</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>SpringBoot_redis</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>SpringBoot_redis</name>
    <description>SpringBoot_redis</description>
    <!--  packaging 的默认打包类型是 jar，所有的父工程打包方式都需要设置成 pom -->
    <packaging>pom</packaging>
    <!-- 子项目 -->
    <modules>
        <module>01_Jedis_Test</module>
    </modules>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <!-- 依赖配置：目前这里的配置的依赖所引入的jar包在此工程下的所有子工程都会被引入 -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

4. 子项目 pom.xml 设置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <!-- 父项目：groupId 组 -->
        <groupId>com.yuehai</groupId>
        <!-- 父项目：artifactId 名 -->
        <artifactId>SpringBoot_redis</artifactId>
        <!-- 父项目：version 版本 -->
        <version>0.0.1-SNAPSHOT</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>Jedis_Test</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>01_Jedis_Test</name>
    <description>01_Jedis_Test</description>
    <packaging>jar</packaging>
</project>

```

5. 创建控制器类

```java
package com.yuehai.jedis_test.controller;

import com.yuehai.jedis_test.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/2/6 14:33
 */
@RestController
@RequestMapping("/test")
public class TestController {

    @GetMapping("/get")
    public JsonResult getTest(){
        return JsonResult.success("OK");
    }

}

```

6. 启动项目，访问测试：[http://127.0.0.1:9000/test/get](http://127.0.0.1:9000/test/get)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-464--ddDAi7tIE6KBig.png)

## 2、添加依赖

- 子项目添加 Jedis 所需要的 jar 包

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <!-- 父项目：groupId 组 -->
        <groupId>com.yuehai</groupId>
        <!-- 父项目：artifactId 名 -->
        <artifactId>SpringBoot_redis</artifactId>
        <!-- 父项目：version 版本 -->
        <version>0.0.1-SNAPSHOT</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>Jedis_Test</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>01_Jedis_Test</name>
    <description>01_Jedis_Test</description>
    <packaging>jar</packaging>

    <dependencies>
        <!-- Jedis 所需要的jar包 -->
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
            <version>4.3.1</version>
        </dependency>
    </dependencies>
</project>

```

## 3、连接 Redis 注意事项

1. 禁用 Linux 的防火墙：Linux(CentOS7)里执行命令：`systemctl stop/disable firewalld.service`
2. redis.conf 中注释掉：`bind 127.0.0.1`
3. 然后修改：`protected-mode no`

## 4、Jedis 常用操作

### ①、创建测试程序

1. 创建控制器，编写代码

```java
package com.yuehai.jedis_test.controller;

import com.yuehai.jedis_test.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import redis.clients.jedis.Jedis;

/**
 * @author 月海
 * @create 2023/2/6 14:54
 */
@RestController
@RequestMapping("/redis")
public class JedisController {

    @GetMapping("/test")
    public JsonResult test(){
        // 连接 redis
        Jedis jedis = new Jedis("43.138.106.181", 3306);
        // 设置密码
        jedis.auth("000123");

        String ping = jedis.ping();
        System.out.println(ping);

        return JsonResult.success(ping);
    }

}

```

2. 访问测试：[http://127.0.0.1:9000/redis/test](http://127.0.0.1:9000/redis/test)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-540--pe6tMI5uO1kREA.png)

### ②、测试相关数据类型：Key

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：Key
 * @return
 */
@GetMapping("/key")
public JsonResult testKey(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// keys *： 查看当前库所有key（查看指定库：keys *1）
	jedis.set("k1", "v1");
	jedis.set("k2", "v2");
	jedis.set("k3", "v3");

	// 获取
	// get <key> 根据 key 获取 value
	Set<String> keys = jedis.keys("*");

	return JsonResult.success(keys);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/key](http://127.0.0.1:9000/redis/key)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-629--6PQpB7ZbAqNroQ.png)

### ③、测试相关数据类型：String

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：String
 * @return
 */
@GetMapping("/string")
public JsonResult testString(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// mset <key1> <value1> <key2> <value2> ...  同时设置一个或多个 key-value 对
	jedis.mset("String-k1", "String-v1", "String-k1", "String-v2");

	// 获取
	// mget <key1> <key2> <key3> ... 同时获取一个或多个 value
	List<String> stringList = jedis.mget("String-k1", "String-k1");

	return JsonResult.success(stringList);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/string](http://127.0.0.1:9000/redis/string)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-751--u_fOg85kU9t76g.png)

### ④、测试相关数据类型：List

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：List
 * @return
 */
@GetMapping("/list")
public JsonResult testList(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// lpush/rpush <key> <value1> <value2> <value3> ....  从左边/右边插入一个或多个值。
	jedis.lpush("list-k1", "list-v1", "list-v2", "list-v3", "list-v4");

	// 获取
	// lrange <key> <start> <stop> 按照索引下标获得一个或多个元素(从左到右)
	// lrange <key> 0 -1：0 左边第一个，-1右边第一个，（0 -1表示获取所有）
	List<String> lrange = jedis.lrange("list-k1", 0, -1);

	return JsonResult.success(lrange);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/list](http://127.0.0.1:9000/redis/list)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-890--U2VYQQz-RBJI7w.png)

### ⑤、测试相关数据类型：set

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：set
 * @return
 */
@GetMapping("/set")
public JsonResult testSet(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// SADD key member1 [member2] 向集合添加一个或多个成员
	jedis.sadd("set-k1", "set-v1", "set-v2", "set-v3", "set-v4", "set-v5");

	// 获取
	// SMEMBERS key 返回指定集合中的所有成员
	Set<String> smembers = jedis.smembers("set-k1");

	return JsonResult.success(smembers);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/set](http://127.0.0.1:9000/redis/set)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-48-983--Dn7CKAKcLd6Y0w.png)

### ⑥、测试相关数据类型：hash

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：hash
 * @return
 */
@GetMapping("/hash")
public JsonResult testHash(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// HSET key field value [field value] 将哈希表 key 中的字段 field 的值设为 value 。
	jedis.hset("hash-string-k1", "name", "月海");
	jedis.hset("hash-string-k1", "age", "16");

	Map<String, String> map = new HashMap<>();
	map.put("name", "言");
	map.put("age", "16");
	jedis.hset("hash-map-k1", map);

	// 获取
	// HVALS key 获取哈希表中所有值。
	List<String> hvalsString = jedis.hvals("hash-string-k1");
	List<String> hvalsMap = jedis.hvals("hash-map-k1");

	return JsonResult.success(hvalsString).put("hvalsMap", hvalsMap);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/hash](http://127.0.0.1:9000/redis/hash)t，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-077--A_z5V9xfZjz1Nw.png)

### ⑦、测试相关数据类型：zset

1. 在控制器中添加方法

```java
/**
 * 测试相关数据类型：zset
 * @return
 */
@GetMapping("/zset")
public JsonResult testZset(){
	// 连接 redis
	Jedis jedis = new Jedis("43.138.106.181", 3306);
	// 设置密码
	jedis.auth("000123");

	// 设置 key
	// zadd <key> <score1> <value1> <score2> <value2> …
	// 将一个或多个 member 元素及其 score 值加入到有序集 key 当中。
	// 多个参数需要使用 map 插入
	Map<String, Double> map = new HashMap<>();
	map.put("zset-100", 100.0);
	map.put("zset-400", 400.0);
	map.put("zset-200", 200.0);
	map.put("zset-300", 300.0);
	jedis.zadd("zset-k1", map);

	// 获取
	// zrangebyscore key min max [withscores] [limit offset count]
	// 返回有序集 key 中，所有 score 值介于 min 和 max 之间(包括等于 min 或 max )的成员。有序集成员按 score 值递增(从小到大)次序排列。
	List<String> zrangeByScore = jedis.zrangeByScore("zset-k1", 1, 500);

	return JsonResult.success(zrangeByScore);
}
```

2. 访问测试：[http://127.0.0.1:9000/redis/zset](http://127.0.0.1:9000/redis/zset)，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-164--x1UTTUn6_mF94A.png)

## 5、完成一个手机验证码功能

> 要求：
> 1、输入手机号，点击发送后随机生成 6 位数字码，2 分钟有效
> 2、输入验证码，点击验证，返回成功或失败
> 3、每个手机号每天只能输入 3 次

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726091818.png)

### ①、创建项目，导入依赖

1. 创建项目

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-287--9eGChkrczrof5g.png)


2. 父项目依赖，新增了 spring-boot-starter-thymeleaf

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.11</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>SpringBoot_redis</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>SpringBoot_redis</name>
    <description>SpringBoot_redis</description>
    <!--  packaging 的默认打包类型是 jar，所有的父工程打包方式都需要设置成 pom -->
    <packaging>pom</packaging>
    <!-- 子项目 -->
    <modules>
        <module>01_Jedis_Test</module>
        <module>02_Jedis_VerificationCode</module>
    </modules>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <!-- 依赖配置：目前这里的配置的依赖所引入的jar包在此工程下的所有子工程都会被引入 -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

3. 本项目依赖

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <!-- 父项目：groupId 组 -->
        <groupId>com.yuehai</groupId>
        <!-- 父项目：artifactId 名 -->
        <artifactId>SpringBoot_redis</artifactId>
        <!-- 父项目：version 版本 -->
        <version>0.0.1-SNAPSHOT</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>Jedis_VerificationCode</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>02_Jedis_VerificationCode</name>
    <description>02_Jedis_VerificationCode</description>
    
    <dependencies>
        <!-- Jedis 所需要的jar包 -->
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
            <version>4.3.1</version>
        </dependency>
    </dependencies>
</project>

```

### ②、编写前端页面

- 在 resources 下创建 templates 目录，在其中创建 index.html 文件

```html
<!DOCTYPE html>
<html lang="zh_CN">
<head>
    <meta charset="UTF-8">
    <title>验证码</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <style>
        body {
            background-color: #e8e8e8;
        }

        .cell-phone-number input {
            border: none;
            outline: none;
            border-radius: 15px;
            padding: 1em;
            background-color: #ccc;
            box-shadow: inset 2px 5px 10px rgba(0,0,0,0.3);
            transition: 300ms ease-in-out;
        }

        .cell-phone-number input:focus {
            background-color: white;
            transform: scale(1.05);
            box-shadow: 13px 13px 100px #969696,
            -13px -13px 100px #ffffff;
        }

        .Verification-Code {
            position: relative;
            font-family: Arial, Helvetica, sans-serif;
        }

        .Verification-Code input {
            border: solid 1.9px #9e9e9e;
            border-radius: 1.3rem;
            background: none;
            padding: 1rem;
            font-size: 1rem;
            color: #000000;
            transition: border 150ms cubic-bezier(0.4,0,0.2,1);
        }

        .textUser {
            position: absolute;
            left: 15px;
            color: #666666;
            pointer-events: none;
            transform: translateY(1rem);
            transition: 150ms cubic-bezier(0.4,0,0.2,1);
        }

        .Verification-Code input:focus, input:valid {
            outline: none;
            box-shadow: 1px 2px 5px rgba(133, 133, 133, 0.523);
            background-image: linear-gradient(to top, rgba(182, 182, 182, 0.199), rgba(252, 252, 252, 0));
            transition: background 4s ease-in-out;
        }

        .Verification-Code input:focus ~ label, input:valid ~ label {
            transform: translateY(-95%) scale(0.9);
            padding: 0 .2em;
            color: #000000be;
            left: 80px;
        }

        .Verification-Code input:hover {
            border: solid 1.9px #000002;
            transform: scale(1.03);
            box-shadow: 1px 1px 5px rgba(133, 133, 133, 0.523);
            transition: border-color 1s ease-in-out;
        }

        .btn {
            position: relative;
            font-size: 17px;
            text-transform: uppercase;
            text-decoration: none;
            padding: 1em 2.5em;
            display: inline-block;
            border-radius: 6em;
            transition: all .2s;
            border: none;
            font-family: inherit;
            font-weight: 500;
            color: black;
            background-color: white;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .btn:active {
            transform: translateY(-1px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        }

        .btn::after {
            content: "";
            display: inline-block;
            height: 100%;
            width: 100%;
            border-radius: 100px;
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
            transition: all .4s;
        }

        .btn::after {
            background-color: #fff;
        }

        .btn:hover::after {
            transform: scaleX(1.4) scaleY(1.6);
            opacity: 0;
        }
    </style>
</head>
<body>
    <div class="cell-phone-number">
        <input type="text" autocomplete="off" name="text" placeholder="Username">
        <button id="getCode" class="btn">发送</button>
    </div>

    <br>

    <div class="Verification-Code">
        <input name="text" type="text" required="">
        <label class="textUser">Click Here</label>
        <button id="verifyCode" class="btn">确定</button>
    </div>

</body>

<script>

    // 网页加载完毕立即执行
    $(function (){
        // 选择 id 为 getCode 的元素，获取验证码
        $("#getCode").click(function (){
            // 获取上一个元素
            let phone = $(this).prev().val();
            // 进行 ajax 请求
            $.get(`http://localhost:9000/code/getCode?phone=${phone}`, function (result){
                console.log(`验证码为：${result.data}`);
            })
        })

        // 选择 id 为 verifyCode 的元素，验证验证码
        $("#verifyCode").click(function (){
            // 获取：父元素 的上一个元素 的上一个元素的 的第一个子元素
            let phone = $(this).parent().prev().prev().children().val();

            // 获取上一个元素 的上一个元素
            let code = $(this).prev().prev().val();
            // 进行 ajax 请求
            $.get(`http://localhost:9000/code/verifyCode?phone=${phone}&code=${code}`, function (result){
                console.log(result.data);
            })

            console.log(phone, code)
        })
    })

</script>

</html>
```

### ③、编写后台页面

-  创建 VerificationCodeController

```java
package com.yuehai.jedis_verificationcode.contriller;

import com.yuehai.jedis_verificationcode.utils.JsonResult;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import redis.clients.jedis.Jedis;

import java.util.Calendar;
import java.util.Date;
import java.util.Random;

/**
 * @author 月海
 * @create 2023/2/6 16:51
 */
@Controller
@RequestMapping("/code")
public class VerificationCodeController {

    /**
     * 跳转页面
     */
    @GetMapping("/{page}")
    public String toPage(@PathVariable String page){
        return page;
    }

    /**
     * 生成并发送验证码
     */
    @ResponseBody
    @GetMapping("/getCode")
    public JsonResult getCode(String phone){
        // 1、连接 redis；设置密码
        Jedis jedis = new Jedis("43.138.106.181", 3306);
        jedis.auth("000123");

        // 拼接 手机号 key，保存验证次数
        String phoneKey = "verify" + phone + ":count";
        // 拼接 验证码 key，保存验证码
        String codeKey = "verify" + phone + ":code";

        // 2、每个手机号每天只能发送 3 次
        String count = jedis.get(phoneKey);
        if (count == null || count.equals("")){
            // 为空，今天第一次发送，发送次数的值设置为 1，过期时间为到今天 0 点
            jedis.setex(phoneKey, getTimeDifferenceToZero(), "1");
        } else if (Integer.parseInt(count) <= 2) {
            // 次数 <= 2，发送次数的值加 1
            jedis.incr(phoneKey);
        }else {
            // 次数 > 2，不可发送
            jedis.close();
            return JsonResult.success("次数 > 2，不可发送");
        }

        // 3.1、生成 6 位数数字
        String verifyCode = String.format("%06d", new Random().nextInt(1000000));
        // 3.2、将验证码放到 redis 中，有效时间为 2 分钟
        jedis.setex(codeKey, 120, verifyCode);

        // 返回验证码
        return JsonResult.success(verifyCode);
    }

    /**
     * 验证验证码
     */
    @ResponseBody
    @GetMapping("/verifyCode")
    public JsonResult verifyCode(String phone, String code){
        // 4、连接 redis；设置密码
        Jedis jedis = new Jedis("43.138.106.181", 3306);
        jedis.auth("000123");

        // 拼接 验证码 key，保存验证码
        String codeKey = "verify" + phone + ":code";

        // 5、获取验证码
        String codeRedis = jedis.get(codeKey);

        // 6、比较获取的验证码和用户发送的验证码
        if(code.equals(codeRedis)){
            // 相同
            return JsonResult.success("验证码正确！！！！");
        }else {
            // 不同
            return JsonResult.success("错误");
        }
    }

    /**
     * 获取当前时间与当天 0 点差值（相差的秒数）
     */
    public int getTimeDifferenceToZero(){
        // 当前时间
        Date nowDate = new Date();
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(nowDate);

        // 设置一天中的第几个小时
        calendar.set(Calendar.HOUR_OF_DAY, 24);
        // 第几分钟
        calendar.set(Calendar.MINUTE, 0);
        // 第几秒
        calendar.set(Calendar.SECOND, 0);
        // 设置结果为零点
        Date zero = calendar.getTime();

        // 当前时间减去设置的零点的时间
        Long differ = zero.getTime() - nowDate.getTime();

        // intValue() 方法用于返回此 Integer 对象表示的值，该值转换为 int 类型(通过强制转换)。
        return differ.intValue() / 1000 ;
    }


}

```

### ④、测试

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-421--H9OcKbY9IKSN_g.png)

# 七、Redis 与 Spring Boot 简单整合

## 1、创建项目

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-544--m8H4vKQg-u8X0g.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-626--w2oe9kds1IvYfg.png)

## 2、修改依赖文件

1. 修改父项目依赖文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.11</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>SpringBoot_redis</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>SpringBoot_redis</name>
    <description>SpringBoot_redis</description>
    <!--  packaging 的默认打包类型是 jar，所有的父工程打包方式都需要设置成 pom -->
    <packaging>pom</packaging>
    <!-- 子项目 -->
    <modules>
        <module>01_Jedis_Test</module>
        <module>02_Jedis_VerificationCode</module>
        <module>03_redis_SpringBoot</module>
    </modules>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <!-- 依赖配置：目前这里的配置的依赖所引入的jar包在此工程下的所有子工程都会被引入 -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

2. 修改本项目依赖文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <!-- 父项目：groupId 组 -->
        <groupId>com.yuehai</groupId>
        <!-- 父项目：artifactId 名 -->
        <artifactId>SpringBoot_redis</artifactId>
        <!-- 父项目：version 版本 -->
        <version>0.0.1-SNAPSHOT</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <artifactId>redis_SpringBoot</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>03_redis_SpringBoot</name>
    <description>03_redis_SpringBoot</description>
    
    <dependencies>
        <!-- redis -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <!-- spring2.X 集成 redis 所需 common-pool2 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-pool2</artifactId>
            <version>2.11.1</version>
        </dependency>

    </dependencies>

</project>

```

## 3、将之前的前端页面复制到本项目

- 在 resources 下创建 templates 目录，在其中创建 index.html 文件

```html
<!DOCTYPE html>
<html lang="zh_CN">
<head>
    <meta charset="UTF-8">
    <title>验证码</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <style>
        body {
            background-color: #e8e8e8;
        }

        .cell-phone-number input {
            border: none;
            outline: none;
            border-radius: 15px;
            padding: 1em;
            background-color: #ccc;
            box-shadow: inset 2px 5px 10px rgba(0,0,0,0.3);
            transition: 300ms ease-in-out;
        }

        .cell-phone-number input:focus {
            background-color: white;
            transform: scale(1.05);
            box-shadow: 13px 13px 100px #969696,
            -13px -13px 100px #ffffff;
        }

        .Verification-Code {
            position: relative;
            font-family: Arial, Helvetica, sans-serif;
        }

        .Verification-Code input {
            border: solid 1.9px #9e9e9e;
            border-radius: 1.3rem;
            background: none;
            padding: 1rem;
            font-size: 1rem;
            color: #000000;
            transition: border 150ms cubic-bezier(0.4,0,0.2,1);
        }

        .textUser {
            position: absolute;
            left: 15px;
            color: #666666;
            pointer-events: none;
            transform: translateY(1rem);
            transition: 150ms cubic-bezier(0.4,0,0.2,1);
        }

        .Verification-Code input:focus, input:valid {
            outline: none;
            box-shadow: 1px 2px 5px rgba(133, 133, 133, 0.523);
            background-image: linear-gradient(to top, rgba(182, 182, 182, 0.199), rgba(252, 252, 252, 0));
            transition: background 4s ease-in-out;
        }

        .Verification-Code input:focus ~ label, input:valid ~ label {
            transform: translateY(-95%) scale(0.9);
            padding: 0 .2em;
            color: #000000be;
            left: 80px;
        }

        .Verification-Code input:hover {
            border: solid 1.9px #000002;
            transform: scale(1.03);
            box-shadow: 1px 1px 5px rgba(133, 133, 133, 0.523);
            transition: border-color 1s ease-in-out;
        }

        .btn {
            position: relative;
            font-size: 17px;
            text-transform: uppercase;
            text-decoration: none;
            padding: 1em 2.5em;
            display: inline-block;
            border-radius: 6em;
            transition: all .2s;
            border: none;
            font-family: inherit;
            font-weight: 500;
            color: black;
            background-color: white;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .btn:active {
            transform: translateY(-1px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        }

        .btn::after {
            content: "";
            display: inline-block;
            height: 100%;
            width: 100%;
            border-radius: 100px;
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
            transition: all .4s;
        }

        .btn::after {
            background-color: #fff;
        }

        .btn:hover::after {
            transform: scaleX(1.4) scaleY(1.6);
            opacity: 0;
        }
    </style>
</head>
<body>
    <div class="cell-phone-number">
        <input type="text" autocomplete="off" name="text" placeholder="Username">
        <button id="getCode" class="btn">发送</button>
    </div>

    <br>

    <div class="Verification-Code">
        <input name="text" type="text" required="">
        <label class="textUser">Click Here</label>
        <button id="verifyCode" class="btn">确定</button>
    </div>

</body>

<script>

    // 网页加载完毕立即执行
    $(function (){
        // 选择 id 为 getCode 的元素，获取验证码
        $("#getCode").click(function (){
            // 获取上一个元素
            let phone = $(this).prev().val();
            // 进行 ajax 请求
            $.get(`http://localhost:9000/code/getCode?phone=${phone}`, function (result){
                console.log(`验证码为：${result.data}`);
            })
        })

        // 选择 id 为 verifyCode 的元素，验证验证码
        $("#verifyCode").click(function (){
            // 获取：父元素 的上一个元素 的上一个元素的 的第一个子元素
            let phone = $(this).parent().prev().prev().children().val();

            // 获取上一个元素 的上一个元素
            let code = $(this).prev().prev().val();
            // 进行 ajax 请求
            $.get(`http://localhost:9000/code/verifyCode?phone=${phone}&code=${code}`, function (result){
                console.log(result.data);
            })

            console.log(phone, code)
        })
    })

</script>

</html>
```

## 4、修改配置文件

1. application.yml

```yaml
server:
    port: 9000

spring:
    # Redis 配置
    redis:
        # Redis 配置服务器地址
        host: 43.138.106.181
        # Redis 服务器连接端口
        port: 3306
        # Redis 数据库索引（默认为 0）
        database: 0
        # Redis 密码
        password: "000123"
        # 连接超时时间（毫秒）
        timeout: 1800000
        lettuce:
            pool:
                # 连接池最大连接数（使用负值表示没有限制）
                max-active: 20
                # 最大阻塞等待时间(负数表示没限制)
                max-wait: -1
                # 连接池中的最大空闲连接
                max-idle: 5
                # 连接池中的最小空闲连接
                min-idle: 0
```

2. 创建 config/RedisConfig 类

```java
package com.yuehai.redis_springboot.config;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.interceptor.KeyGenerator;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.RedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.lang.reflect.Method;
import java.time.Duration;

@Configuration
@EnableCaching
public class RedisConfig {

    /**
     * 自定义key规则
     * @return
     */
    @Bean
    public KeyGenerator keyGenerator() {
        return new KeyGenerator() {
            @Override
            public Object generate(Object target, Method method, Object... params) {
                StringBuilder sb = new StringBuilder();
                sb.append(target.getClass().getName());
                sb.append(method.getName());
                for (Object obj : params) {
                    sb.append(obj.toString());
                }
                return sb.toString();
            }
        };
    }

    /**
     * 设置RedisTemplate规则
     */
    @Bean
    public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
        RedisTemplate<Object, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory);
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);

        //解决查询缓存转换异常的问题
        ObjectMapper om = new ObjectMapper();
        // 指定要序列化的域，field,get和set,以及修饰符范围，ANY是都有包括private和public
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        // 指定序列化输入的类型，类必须是非final修饰的，final修饰的类，比如String,Integer等会跑出异常
        om.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(om);

        //序列号key value
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);
        redisTemplate.setHashKeySerializer(new StringRedisSerializer());
        redisTemplate.setHashValueSerializer(jackson2JsonRedisSerializer);

        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }

    /**
     * 设置CacheManager缓存规则
     * @param factory
     * @return
     */
    @Bean
    public CacheManager cacheManager(RedisConnectionFactory factory) {
        RedisSerializer<String> redisSerializer = new StringRedisSerializer();
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);

        //解决查询缓存转换异常的问题
        ObjectMapper om = new ObjectMapper();
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        om.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(om);

        // 配置序列化（解决乱码的问题）,过期时间600秒
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
                .entryTtl(Duration.ofSeconds(600))
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(redisSerializer))
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(jackson2JsonRedisSerializer))
                .disableCachingNullValues();

        RedisCacheManager cacheManager = RedisCacheManager.builder(factory)
                .cacheDefaults(config)
                .build();
        return cacheManager;
    }
}
```

## 5、编写业务类

- controller/VerificationCodeController

```java
package com.yuehai.redis_springboot.contriller;

import com.yuehai.redis_springboot.utils.JsonResult;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.Calendar;
import java.util.Date;
import java.util.Random;
import java.util.concurrent.TimeUnit;

/**
 * @author 月海
 * @create 2023/2/6 16:51
 */
@Controller
@RequestMapping("/code")
public class VerificationCodeController {

    /**
     * 自动注入 RedisTemplate
     */
    @Resource
    private RedisTemplate redisTemplate;

    /**
     * 跳转页面
     */
    @GetMapping("/{page}")
    public String toPage(@PathVariable String page){
        return page;
    }

    /**
     * 生成并发送验证码
     */
    @ResponseBody
    @GetMapping("/getCode")
    public JsonResult getCode(String phone){
        // 拼接 手机号 key，保存验证次数
        String phoneKey = "verify" + phone + ":count";
        // 拼接 验证码 key，保存验证码
        String codeKey = "verify" + phone + ":code";

        // 1、每个手机号每天只能发送 3 次；hasKey()：判断某个 key 是否存在；有则返回true，没有则返回false；
        if (!redisTemplate.hasKey(phoneKey)){
            // 为空，今天第一次发送，发送次数的值设置为 1，过期时间为到今天 0 点
            redisTemplate.opsForValue().set(phoneKey, "1", getTimeDifferenceToZero(), TimeUnit.SECONDS);
        } else if (((Integer) redisTemplate.opsForValue().get(phoneKey)) <= 2) {
            // 次数 <= 2，发送次数的值加 1
            redisTemplate.opsForValue().increment(phoneKey);
        }else {
            // 次数 > 2，不可发送
            return JsonResult.success("次数 > 2，不可发送");
        }

        // 2.1、生成 6 位数数字
        String verifyCode = String.format("%06d", new Random().nextInt(1000000));
        // 2.2、将验证码放到 redis 中，有效时间为 2 分钟
        redisTemplate.opsForValue().set(codeKey, verifyCode, 120, TimeUnit.SECONDS);

        // 返回验证码
        return JsonResult.success(verifyCode);
    }

    /**
     * 验证验证码
     */
    @ResponseBody
    @GetMapping("/verifyCode")
    public JsonResult verifyCode(String phone, String code){
        // 拼接 验证码 key，保存验证码
        String codeKey = "verify" + phone + ":code";

        // 3、获取验证码
        String codeRedis = (String) redisTemplate.opsForValue().get(codeKey);

        // 4、比较获取的验证码和用户发送的验证码
        if(code.equals(codeRedis)){
            // 相同
            return JsonResult.success("验证码正确！！！！");
        }else {
            // 不同
            return JsonResult.success("错误");
        }
    }

    /**
     * 获取当前时间与当天 0 点差值（相差的秒数）
     */
    public int getTimeDifferenceToZero(){
        // 当前时间
        Date nowDate = new Date();
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(nowDate);

        // 设置一天中的第几个小时
        calendar.set(Calendar.HOUR_OF_DAY, 24);
        // 第几分钟
        calendar.set(Calendar.MINUTE, 0);
        // 第几秒
        calendar.set(Calendar.SECOND, 0);
        // 设置结果为零点
        Date zero = calendar.getTime();

        // 当前时间减去设置的零点的时间
        Long differ = zero.getTime() - nowDate.getTime();

        // intValue() 方法用于返回此 Integer 对象表示的值，该值转换为 int 类型(通过强制转换)。
        return differ.intValue() / 1000 ;
    }


}

```

## 6、测试

- [https://blog.csdn.net/lydms/article/details/105224210](https://blog.csdn.net/lydms/article/details/105224210)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-777--WxUpf_3XZg1_JQ.png)

# 八、Redis 事务

> [http://doc.redisfans.com/transaction/exec.html](http://doc.redisfans.com/transaction/exec.html)

## 1、Redis 的事务定义

1. Redis 事务是一个单独的隔离操作：事务中的所有命令都会序列化、按顺序地执行。事务在执行的过程中，不会被其他客户端发送来的命令请求所打断。
2. Redis 事务的主要作用就是串联多个命令防止别的命令插队。

## 2、`Multi`、`Exec`、`discard`

1. 从输入 `Multi` 命令开始，输入的命令都会依次进入命令队列中，但不会执行
2. 直到输入 `Exec` 后，Redis 会将之前的命令队列中的命令依次执行
3. 组队的过程中可以通过 `discard` 来放弃组队

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-49-974--xwbmQ6hTb-qSsQ.png)

---

1. 组队成功，提交成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-094--34KntDRrVrPdCw.png)

2. 组队阶段报错，提交失败

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-227--VsuyY9EzIbuv-A.png)

3. 组队成功，提交有成功有失败情况

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-375--h1rqL--GUv8PSw.png)

## 3、事务的错误处理

1. 组队阶段某个命令出现了报告错误，执行时整个队列都会被取消（编译时异常）。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-490--V-2w2YbnsoSScQ.png)

2. 执行阶段某个命令报出了错误，则只有报错的命令不会被执行，而其他的命令都会执行，不会回滚（执行时异常）。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-686--XMUFhLKUgnpHsA.png)

## 4、事务锁

### ①、例子

> 一个请求想给金额减8000
> 一个请求想给金额减5000
> 一个请求想给金额减1000


![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-804--at3aGpP-fkfxMg.png)

### ②、悲观锁

1. 悲观锁(Pessimistic Lock)
2. 顾名思义，就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会 block 直到它拿到锁。
3. 传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-50-953--vNnjf7UiH8uItw.png)

### ③、乐观锁

1. 乐观锁(Optimistic Lock)
2. 顾名思义，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，可以使用版本号等机制。
3. 乐观锁适用于多读的应用类型，这样可以提高吞吐量。
4. Redis 就是利用这种 check-and-set 机制实现事务的。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-097--bGilIlGmTgWrew.png)

### ④、监视 `WATCH key [key ...]`

1. 在执行 `multi` 之前，先执行 `watch key1 [key2]` 可以监视一个(或多个) key
2. 如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。

---

1. 开启窗口 1：开启乐观锁，开始事务，给 key 1 加 10

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-257--vnIt5v37eBpomg.png)

2. 开启窗口 2：开启乐观锁，开始事务，给 key 1 加 10

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-315--GM5oGS58tln49Q.png)

3. 在窗口 1 提交事务，成功

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-432--xGnlWBGxXNkCEw.png)

4. 在窗口 2 提交事务，报错

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-541--ZPW0fTc2BWZtGg.png)

### ⑤、取消监视 `unwatch`

1. 取消 `WATCH` 命令对所有 key 的监视。
2. 如果在执行 WATCH 命令之后，EXEC 命令或 DISCARD 命令先被执行了的话，那么就不需要再执行 UNWATCH 了。

## 5、Redis 事务三特性

1. 单独的隔离操作：事务中的所有命令都会序列化、按顺序地执行。事务在执行的过程中，不会被其他客户端发送来的命令请求所打断。 
2. 没有隔离级别的概念：队列中的命令没有提交之前都不会实际被执行，因为事务提交前任何指令都不会被实际执行
3. 不保证原子性：事务中如果有一条命令执行失败，其后的命令仍然会被执行，没有回滚

# 九、持久化

## 1、Redis 持久化之 RDB

> 官网介绍：[http://www.redis.io](http://www.redis.io)

### ①、RDB 是什么

- 在指定的时间间隔内将内存中的数据集快照写入磁盘， 也就是行话讲的 Snapshot 快照，它恢复时是将快照文件直接读到内存里

### ②、备份是如何执行的

1. Redis 会单独创建（fork）一个子进程来进行持久化，会先将数据写入到 一个临时文件中，待持久化过程都结束了，再用这个临时文件替换上次持久化好的文件。 
2. 整个过程中，主进程是不进行任何 IO 操作的，这就确保了极高的性能
3. 如果需要进行大规模数据的恢复，且对于数据恢复的完整性不是非常敏感，那 RDB 方式要比 AOF 方式更加的高效。
4. RDB的缺点是最后一次持久化后的数据可能丢失。

### ③、Fork

1. Fork 的作用是复制一个与当前进程一样的进程。新进程的所有数据（变量、环境变量、程序计数器等） 数值都和原进程一致，但是是一个全新的进程，并作为原进程的子进程
2. 在 Linux 程序中，fork() 会产生一个和父进程完全相同的子进程，但子进程在此后多会 exec 系统调用，出于效率考虑，Linux 中引入了“写时复制技术”
3. 一般情况父进程和子进程会共用同一段物理内存，只有进程空间的各段的内容要发生变化时，才会将父进程的内容复制一份给子进程。

### ④、RDB 持久化流程

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-613--XhZUqqJ84Nr-Ow.png)

### ⑤、配置文件中的 RDB 配置

```bash
################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
save 300 10
save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data
```

### ⑥、命令 `save` VS `bgsave`

1. `save`：save 时只管保存，其它不管，全部阻塞。手动保存。不建议。
2. `bgsave`：Redis 会在后台异步进行快照操作， 快照同时还可以响应客户端请求。
3. 可以通过 `lastsave` 命令获取最后一次成功执行快照的时间
4. `flushall` 命令：执行 `flushall` 命令，也会产生dump.rdb文件，但里面是空的，无意义

### ⑦、优势

1. 适合大规模的数据恢复
2. 对数据完整性和一致性要求不高更适合使用
3. 节省磁盘空间
4. 恢复速度快

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-741--_na2z9Ryg6LKMw.png)

### ⑧、劣势

1. Fork 的时候，内存中的数据被克隆了一份，大致 2 倍的膨胀性需要考虑
2. 虽然 Redis 在 fork 时使用了写时拷贝技术,但是如果数据庞大时还是比较消耗性能。
3. 在备份周期在一定间隔时间做一次备份，所以如果 Redis 意外 down 掉的话，就会丢失最后一次快照后的所有修改。

### ⑨、如何停止

1. 修改配置文件， save 后给空值，表示禁用保存策略；或者注释掉
2. 命令：`redis-cli config set save ""`，本质也是修改配置文件

### ⑩、小总结

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-51-868--FU1uwuBbXDqsiw.png)

## 2、Redis 持久化之 AOF

> 官网介绍：[http://www.redis.io](http://www.redis.io)

### ①、AOF 是什么

1. 以日志的形式来记录每个写操作（增量保存），将 Redis 执行过的所有写指令记录下来（读操作不记录）， 只许追加文件但不可以改写文件
2. redis 启动之初会读取该文件重新构建数据，换言之，redis 重启的话就根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作

### ②、AOF 持久化流程

1. 客户端的请求写命令会被 append 追加到 AOF 缓冲区内；
2. AOF 缓冲区根据 AOF 持久化策略 [always,everysec,no] 将操作 sync 同步到磁盘的 AOF 文件中；
3. AOF 文件大小超过重写策略或手动重写时，会对 AOF 文件 rewrite 重写，压缩 AOF 文件容量；
4. Redis 服务重启时，会重新 load 加载 AOF 文件中的写操作达到数据恢复的目的；

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-047--6b2LF4L0jqbbsA.png)

### ③、AOF 默认不开启

1. 可以在 redis.conf 中配置文件名称，默认为 appendonly.aof
2. AOF 文件的保存路径，同 RDB 的路径一致。

### ④、AOF 和 RDB 同时开启，redis 听谁的？

- AOF 和 RDB 同时开启，系统默认取 AOF 的数据（数据不会存在丢失）

### ⑤、AOF 启动/修复/恢复

1. AOF 的备份机制和性能虽然和 RDB 不同, 但是备份和恢复的操作同 RDB 一样，都是拷贝备份文件，需要恢复时再拷贝到 Redis 工作目录下，启动系统即加载。
2. 正常恢复
   1. 修改默认的 appendonly no，改为 yes
   2. 将有数据的 aof 文件复制一份保存到对应目录(查看目录：config get dir)
   3. 恢复：重启 redis 然后重新加载
3. 异常恢复
   1. 修改默认的 appendonly no，改为 yes
   2. 如遇到 AOF 文件损坏，通过 `/usr/local/bin/redis-check-aof --fix appendonly.aof` 进行恢复
   3. 备份被写坏的 AOF 文件
   4. 恢复：重启 redis，然后重新加载

### ⑥、AOF 配置文件设置

```bash
############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

```

### ⑦、Rewrite 压缩

#### Ⅰ、是什么

1. AOF 采用文件追加方式，文件会越来越大。
2. 为避免出现此种情况，新增了重写机制，当 AOF 文件的大小超过所设定的阈值时，Redis 就会启动 AOF 文件的内容压缩， 只保留可以恢复数据的最小指令集
3. 可以使用命令 `bgrewriteaof`

#### Ⅱ、重写原理，如何实现重写

1. AOF 文件持续增长而过大时，会 fork 出一条新进程来将文件重写(也是先写临时文件最后再 rename)，redis4.0 版本后的重写，是指上就是把 rdb 的快照，以二级制的形式附在新的aof 头部，作为已有的历史数据，替换掉原来的流水账操作。
2. `no-appendfsync-on-rewrite`：
   1. 如果 no-appendfsync-on-rewrite=yes，不写入 aof 文件只写入缓存，用户请求不会阻塞，但是在这段时间如果宕机会丢失这段时间的缓存数据。（降低数据安全性，提高性能）
   2. 如果 no-appendfsync-on-rewrite=no,  还是会把数据往磁盘里刷，但是遇到重写操作，可能会发生阻塞。（数据安全，但是性能降低）
3. 触发机制，何时重写：
   1. Redis 会记录上次重写时的 AOF 大小，默认配置是当 AOF 文件大小是上次 rewrite 后大小的一倍且文件大于 64M 时触发
   2. 重写虽然可以节约大量磁盘空间，减少恢复时间。但是每次重写还是有一定的负担的，因此设定 Redis 要满足一定条件才会进行重写。 
4. `auto-aof-rewrite-percentage`：设置重写的基准值，文件达到 100% 时开始重写（文件是原来重写后文件的2倍时触发）
5. `auto-aof-rewrite-min-size`：
   1. 设置重写的基准值，最小文件 64MB。达到这个值开始重写。
   2. 例如：文件达到 70MB 开始重写，降到 50MB，下次什么时候开始重写？100MB
6. 系统载入时或者上次重写完毕时，Redis 会记录此时 AOF 大小，设为 base_size，如果 Redis 的 AOF 当前大小 >= base_size +base_size*100% (默认) 且当前大小 >=64mb(默认)的情况下，Redis 会对 AOF 进行重写。

#### Ⅲ、重写流程

1. bgrewriteaof 触发重写，判断是否当前有 bgsave 或 bgrewriteaof 在运行，如果有，则等待该命令结束后再继续执行。
2. 主进程 fork 出子进程执行重写操作，保证主进程不会阻塞。
3. 子进程遍历 redis 内存中数据到临时文件，客户端的写请求同时写入 aof_buf 缓冲区和 aof_rewrite_buf 重写缓冲区保证原 AOF 文件完整以及新 AOF 文件生成期间的新的数据修改动作不会丢失。
4. 子进程写完新的 AOF 文件后，向主进程发信号，父进程更新统计信息
5. 主进程把 aof_rewrite_buf 中的数据写入到新的 AOF 文件。
6. 使用新的 AOF 文件覆盖旧的 AOF 文件，完成 AOF 重写。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-220--5EFUaiVwGKNOdA.png)

### ⑧、优势

1. 备份机制更稳健，丢失数据概率更低。
2. 可读的日志文本，通过操作AOF稳健，可以处理误操作。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-370--N6ocH2zvPNPjBQ.png)

### ⑨、劣势

1. 恢复备份速度要慢。
2. 每次读写都同步的话，有一定的性能压力。
3. 存在个别 Bug，造成恢复不能。
### ⑩、小总结

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-515--jxNzT_zIm899Qw.png)

## 3、用哪个好

> 官方推荐两个都启用。
> 如果对数据不敏感，可以选单独用 RDB。
> 不建议单独用 AOF，因为可能会出现 Bug。
> 如果只是做纯内存缓存，可以都不用。

1. RDB 持久化方式能够在指定的时间间隔能对你的数据进行快照存储
2. AOF 持久化方式记录每次对服务器写的操作，当服务器重启的时候会重新执行这些命令来恢复原始的数据，AOF 命令以 redis 协议追加保存每次写的操作到文件末尾. 
3. Redis 还能对 AOF 文件进行后台重写，使得 AOF 文件的体积不至于过大
4. 只做缓存：如果你只希望你的数据在服务器运行的时候存在，你也可以不使用任何持久化方式.
5. 同时开启两种持久化方式
6. 在这种情况下，当 redis 重启的时候会优先载入 AOF 文件来恢复原始的数据， 因为在通常情况下 AOF 文件保存的数据集要比 RDB 文件保存的数据集要完整.
7. RDB 的数据不实时，同时使用两者时服务器重启也只会找 AOF 文件。那要不要只使用 AOF 呢？ 
8. 建议不要，因为 RDB 更适合用于备份数据库(AOF 在不断变化不好备份)， 快速重启，而且不会有 AOF 可能潜在的 bug，留着作为一个万一的手段。
9. 性能建议：
   1. 因为 RDB 文件只用作后备用途，建议只在 Slave 上持久化 RDB 文件，而且只要 15 分钟备份一次就够了，只保留 `save 900 1` 这条规则。
   2. 如果使用 AOF，好处是在最恶劣情况下也只会丢失不超过两秒数据，启动脚本较简单只 load 自己的 AOF 文件就可以了。
   3. 代价，一是带来了持续的 IO，二是 AOF rewrite 的最后将 rewrite 过程中产生的新数据写到新文件造成的阻塞几乎是不可避免的。
   4. 只要硬盘许可，应该尽量减少 AOF rewrite 的频率，AOF 重写的基础大小默认值 64M 太小了，可以设到 5G 以上。
   5. 默认超过原大小 100% 大小时重写可以改到适当的数值。

# 十、Redis 主从复制

> 主机数据更新后根据配置和策略， 自动同步到备机的 master/slaver 机制，Master 以写为主，Slave 以读为主

## 1、作用

1. 读写分离，性能扩展
2. 容灾快速恢复

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-713--RXKdD8CDLALzUw.png)

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726091909.png)

## 2、如何使用

> 依然是使用 docker

1. 复制挂载的 redis 目录与其中的文件，记住 log 中的文件需要读写权限

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-52-855--nJF-ng7WWNzBDA.png)

2. redis 作为主机（master）的挂载目录，redis2、redis3 作为从机（slaver）的挂载目录
3. 修改 redis2、redis3 目录下 config 中的 redis.conf 文件，主要修改：
   1. `slaveof 43.138.106.181 3306`，主机对应的 ip 和 端口
   2. `masterauth 000123`，主机对应的密码
   3. 若是不配置这两个配置项，则启动后也可使用命令来配型配置：`slaveof 127.0.0.1 6379`，设置主机的 ip 和 端口；但是这样的话每次重启之后都要重新配置

```bash
################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master
slaveof 43.138.106.181 3306

# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
masterauth 000123

# 当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。
slave-serve-stale-data yes

# 作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。
slave-priority 100

# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。
# 这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.
```

4. 启动主机：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:6379 --name redis -v /home/docker/docker/VOLUME/redis/config:/etc/redis -v /home/docker/docker/VOLUME/redis/data:/data -v /home/docker/docker/VOLUME/redis/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
5. 启动从机 1：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3000:6379 --name redis2 -v /home/docker/docker/VOLUME/redis2/config:/etc/redis -v /home/docker/docker/VOLUME/redis2/data:/data -v /home/docker/docker/VOLUME/redis2/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
6. 启动从机 2：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 9000:6379 --name redis3 -v /home/docker/docker/VOLUME/redis3/config:/etc/redis -v /home/docker/docker/VOLUME/redis3/data:/data -v /home/docker/docker/VOLUME/redis3/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
7. 查看是否启动成功：`docker ps`

```bash
docker@VM-8-15-ubuntu:~/docker/VOLUME$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                       NAMES
a887b7cca8ab   redis:6.2.1                  "docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:9000->6379/tcp, :::9000->6379/tcp   redis3
73ae88dffbae   redis:6.2.1                  "docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:3000->6379/tcp, :::3000->6379/tcp   redis2
8d512d2cd388   redis:6.2.1                  "docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:3306->6379/tcp, :::3306->6379/tcp   redis
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             5 days ago       Up 5 days       0.0.0.0:9443->9000/tcp, :::9443->9000/tcp   naughty_kowalevski

docker@VM-8-15-ubuntu:~/docker/VOLUME$ 
```

8. 查看主机运行状态：`info replication`

```bash
# Replication
# 角色：主
role:master

# 已连接从属设备：2
connected_slaves:2

# 从属设备 1：ip、端口、状态=在线、偏移量、延迟
slave0:ip=43.138.106.181,port=6379,state=online,offset=5083,lag=0
# 从属设备 2
slave1:ip=43.138.106.181,port=6379,state=online,offset=5083,lag=0

# 无故障转移
master_failover_state:no-failover

master_replid:6a7dd14f6d2602f56975837d628e79d826dec186
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:5083
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:5083
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-010--nzL29SyoX5K5wg.png)

9. 查看从机运行状态

```bash
# Replication
# 角色：从属
role:slave

# 主设备：ip、端口、状态、、、、偏移量、从属优先级、从属只读、已连接从属设备
master_host:43.138.106.181
master_port:3306
master_link_status:up
master_last_io_seconds_ago:9
master_sync_in_progress:0
slave_repl_offset:5083
slave_priority:100
slave_read_only:1
connected_slaves:0

# 无故障转移
master_failover_state:no-failover

master_replid:6a7dd14f6d2602f56975837d628e79d826dec186
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:5083
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:5083
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-124--F9cQ4gKnSB9nCg.png)

## 3、测试主从复制

1. 查看主机数据：无

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-233--2_UpRGUvBEKVyQ.png)

2. 查看从机 1 数据：无

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-358--dgqwXvEjs9uwIA.png)

3. 查看从机 2 数据：无

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-502--Er122bUGWU07YQ.png)

4. 在主机中新增数据

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-584--n6ptsY3jjE_1LA.png)

5. 查看从机 1 数据，同步新增

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-709--GgetBvNoi9n-yw.png)

6. 查看从机 2 数据，同步新增

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-847--mzrpCs2Y-LcyZQ.png)

7. 删除主机中的数据

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-53-974--E-Q8QrgmEEbv-w.png)

8. 查看从机 1 数据，同步删除

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-083--h1qUAxAHv-1zPQ.png)

9. 查看从机 2 数据，同步删除

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-176--hubvknD5cThFNw.png)

## 4、常用 3 招

### ①、一主二仆

1. 切入点问题：slave1、slave2 是从头开始复制还是从切入点开始复制？比如从 k4 进来，那之前的 k1、k2、k3 是否也可以复制？从头复制
2. 从机是否可以写？set 可否？ 不可写，可以配置成写的，但是没有这么做的
3. 主机 shutdown 后情况如何？从机是上位还是原地待命？原地待命
4. 主机又回来了后，主机新增记录，从机还能否顺利复制？ 能
5. 其中一台从机 down 后情况如何？依照原有它能跟上大部队吗？
   1. 若是配置文件配置的，则重启后依然是从机，可以正常同步
   2. 若是命令配置的，则需重新进行配置

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-320--aJUtBRja7zuAhg.png)

### ②、**薪火相传**

1. 上一个 Slave 可以是下一个 Slave 的 Master，Slave 同样可以接收其他 slaves 的连接和同步请求，那么该 slave 作为了链条中下一个的 master，可以有效减轻 master 的写压力，去中心化降低风险。
2. 中途变更转向：`slaveof <ip> <port>`，会清除之前的数据，重新建立拷贝最新的
3. 风险是一旦某个 slave 宕机，后面的 slave 都没法备份
4. 主机挂了，从机还是从机，无法写数据了

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-451--cOJ_8vDtKs5gJA.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-621--TmIpJGIDrztpEg.png)

### ③、反客为主

1. 当一个 master 宕机后，后面的 slave 可以立刻升为 master，其后面的 slave 不用做任何修改。
2. 用 `slaveof  no one`  将从机变为主机。
3. 配置文件中：`slave-priority 100`，当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-771--saN12l3YhBol5w.png)

## 5、复制原理

1. Slave 启动成功连接到 master 后会发送一个 sync 命令，要求进行数据同步
2. Master 接到命令启动后台的存盘进程（保存 RDB），同时收集所有接收到的用于修改数据集命令；在后台进程执行完毕之后，master 将传送整个数据文件（RDB）发送到 slave，以完成一次完全同步
3. 全量复制：slave 服务在接收到数据库文件数据后，将其存盘并加载到内存中。
4. 增量复制：Master 继续将新的所有收集到的修改命令依次传给 slav，完成同步
5. 但是只要是重新连接 master，一次完全同步（全量复制）将被自动执行

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-54-942--ji-eGOxqRUz35w.png)

## 6、哨兵模式（sentinel）
### ①、是什么
反客为主的自动版，能够后台监控主机是否故障，如果故障了根据投票数自动将从库转换为主库

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-103--nYROm8IJEL2Kzw.png)

### ②、如何使用

> 1. 若是使用的 docker，一定要把 redis 的端口号修改为与 docker 的映射端口相同
> 2. 主机与从机的密码一定要相同
> 3. `sentinel monitor mymaster 43.138.106.181 3306 1`，最后的投票数量要小于从机数量

1. 检查主机的配置文件配置；并将端口设置为 3000：`port 3306`

```bash
# Redis configuration file example

# Note on units: when memory size is needed, it is possible to specify
# it in the usual form of 1k 5GB 4M and so forth:
#
# 当你需要为某个配置项指定内存大小的时候，必须要带上单位，
# 通常的格式就是 1k 5gb 4m 等酱紫：
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# 单位是不区分大小写的，你写 1K 5GB 4M 也行
################################## INCLUDES ###################################
# 假如说你有一个可用于所有的 redis server 的标准配置模板，
# 但针对某些 server 又需要一些个性化的设置，
# 你可以使用 include 来包含一些其他的配置文件，这对你来说是非常有用的。
#
# 但是要注意哦，include 是不能被 config rewrite 命令改写的
# 由于 redis 总是以最后的加工线作为一个配置指令值，所以你最好是把 include 放在这个文件的最前面，
# 以避免在运行时覆盖配置的改变，相反，你就把它放在后面（外国人真啰嗦）。
# 
# include /path/to/local.conf
# include /path/to/other.conf
################################ GENERAL #####################################

# 是否在后台执行，yes：后台运行；no：不是后台运行（老版本默认）
# 由于 docker 容器在启动时，需要任务在前台运行，否则会启动后立即退出，因此导致 redis 容器启动后立即退出问题.
daemonize no

# 指定 redis 只接收来自于该 IP 地址的请求，如果不进行设置，那么将处理所有请求
#bind 127.0.0.1

# 3.2 里的参数，是否开启保护模式，默认开启。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 要是开启了密码 和 bind，可以开启。否 则最好关闭，设置为 no。
protected-mode no

#redis 的进程文件
pidfile /var/run/redis/redis-server.pid

#redis 监听的端口号。
port 3306

# 此参数确定了 TCP 连接中已完成队列(完成三次握手之后)的长度， 当然此值必须不大于 Linux 系统定义的/proc/sys/net/core/somaxconn 值，默认是 511，而 Linux 的默认参数值是 128。
# 当系统并发量大并且客户端速度缓慢的时候，可以将这二个参数一起参考设定。该内核参数默认值一般是 128，对于负载很大的服务程序来说大大的不够。
# 一般会将它修改为 2048 或者更大。在/etc/sysctl.conf 添加:net.core.somaxconn = 2048，然后在终端中执行 sysctl -p。
tcp-backlog 511

# 配置 unix socket 来让 redis 支持监听本地连接。
# unixsocket /var/run/redis/redis.sock

# 配置 unix socket 使用文件的权限
# unixsocketperm 700

# 此参数为设置客户端空闲超过 timeout，服务端会断开连接，为 0 则服务端不会主动断开连接，不能小于 0。
timeout 0

# tcp keepalive 参数。如果设置不为 0，就使用配置 tcp 的 SO_KEEPALIVE 值，
# 使用 keepalive 有两个好处：检测挂掉的对端。降低中间设备出问题而导致网络看似连接却已经与对端端口的问题。在 Linux内核中，设置了 keepalive，redis 会定时给对端发送 ack。检测到对端关闭需要两倍的设置值。
tcp-keepalive 0

# 指定了服务端日志的级别。级别包括：debug（很多信息，方便开发、测试），verbose（许多有用的信息，但是没有 debug 级别信息多），notice（适当的日志级别，适合生产环境），warn（只有非常重要的信息）
loglevel notice

# 指定了记录日志的文件。空字符串的话，日志会打印到标准输出设备。后台运行的 redis 标准输出是/dev/null。
logfile /var/log/redis/redis-server.log

#是否打开记录 syslog 功能
# syslog-enabled no

#syslog 的标识符。
# syslog-ident redis

#日志的来源、设备
# syslog-facility local0

#数据库的数量，默认使用的数据库是 DB 0。可以通过”SELECT “命令选择一个 db
databases 16

################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
# save 300 10
# save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data

################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master
# slaveof <masterip> <masterport>

# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
# masterauth <master-password>

#当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。
slave-serve-stale-data yes

# 作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。
# slave-priority 100

# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。
# 这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.

################################## SECURITY ###################################

# requirepass 配置可以让用户使用 AUTH 命令来认证密码，才能使用其他命令。这让 redis 可以使用在不受信任的网络中。
# 为了保持向后的兼容性，可以注释该命令，因为大部分用户也不需要认证。使用requirepass 的时候需要注意，因为 redis 太快了，每秒可以认证 15w 次密码，简单的密码很容易被攻破，所以最好使用一个更复杂的密码。
requirepass 000123

# 把危险的命令给修改成其他名称。比如 CONFIG 命令可以重命名为一个很难被猜到的命令，这样用户不能使用，而内部工具还能接着使用。
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52

# 设置成一个空的值，可以禁止一个命
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置能连上 redis 的最大客户端连接数量。默认是 10000 个客户端连接。
# 由于 redis 不区分连接是客户端连接还是内部打开文件或者和 slave 连接等，所以 maxclients 最小建议设置到 32。如果超过了maxclients，redis 会给新的连接发送’max number of clients reached’，并关闭连接。
# maxclients 10000

# redis 配置的最大内存容量。当内存满了，需要配合 maxmemory-policy 策略进行处理。
# 注意 slave 的输出缓冲区是不计算在 maxmemory 内的。所以为了防止主机内存使用完，建议设置的 maxmemory 要更小一些。
# maxmemory <bytes>

# 内存容量超过 maxmemory 后的处理策略。
# volatile-lru：利用 LRU 算法移除设置过过期时间的 key。
# volatile-random：随机移除设置过过期时间的 key。
# volatile-ttl：移除即将过期的 key，根据最近过期时间来删除（辅以 TTL）
# allkeys-lru：利用 LRU 算法移除任何 key。
# allkeys-random：随机移除任何 key。
# noeviction：不移除任何 key，只是返回一个写错误。
# 上面的这些驱逐策略，如果 redis 没有合适的 key 驱逐，对于写命令，还是会返回错误。redis 将不再接收写请求，只接收 get 请求。
# 写命令包括：set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort。
# maxmemory-policy noeviction

# lru 检测的样本数。使用 lru 或者 ttl 淘汰算法，从需要淘汰的列表中随机选择 sample 个 key，选出闲置时间最长的 key 移除。
# maxmemory-samples 5

############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

################################ LUA SCRIPTING ###############################

# 如果达到最大时间限制（毫秒），redis 会记个 log，然后返回 error。
# 当一个脚本超过了最大时限。只有 SCRIPT KILL 和 SHUTDOWN NOSAVE 可以用。第一个可以杀没有调 write 命令的东西。要是已经调用了 write，只能用第二个命令杀。
lua-time-limit 5000

################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
# cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
# cluster-config-file nodes-6379.conf

# 节点互连超时的阀值。集群节点超时毫秒数
# cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes

################################## SLOW LOG ###################################

# slog log 是用来记录 redis 运行中执行比较慢的命令耗时。当命令的执行超过了指定时间，就记录在 slow log 中，slog log 保存在内存中，所以没有 IO 操作。
# 执行时间比 slowlog-log-slower-than 大的请求记录到 slowlog 里面，单位是微秒，所以 1000000就是 1 秒。
# 注意，负数时间会禁用慢查询日志，而 0 则会强制记录所有命令。
# slowlog-log-slower-than 1000

# 慢查询日志长度。当一个新的命令被写进日志的时候，最老的那个记录会被删掉。这个长度没有限制。只要有足够的内存就行。你可以通过 SLOWLOG RESET 来释放内存。
slowlog-max-len 128

################################ LATENCY MONITOR ##############################

# 延迟监控功能是用来监控 redis 中执行比较缓慢的一些操作，用 LATENCY 打印 redis 实例在跑命令时的耗时图表。
# 只记录大于等于下边设置的值的操作。0 的话，就是关闭监视。默认延迟监控功能是关闭的，如果你需要打开，也可以通过 CONFIG SET 命令动态设置。
latency-monitor-threshold 0

############################# EVENT NOTIFICATION ##############################

# 键空间通知使得客户端可以通过订阅频道或模式，来接收那些以某种方式改动了 Redis 数据集的事件。因为开启键空间通知功能需要消耗一些 CPU ，所以在默认配置下，该功能处于关闭状态。
#notify-keyspace-events 的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知：
##K 键空间通知，所有通知以 __keyspace@__ 为前缀
##E 键事件通知，所有通知以 __keyevent@__ 为前缀
##g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知
##$ 字符串命令的通知
##l 列表命令的通知
##s 集合命令的通知
##h 哈希命令的通知
##z 有序集合命令的通知
##x 过期事件：每当有过期键被删除时发送
##e 驱逐(evict)事件：每当有键因为 maxmemory 政策而被删除时发送
##A 参数 g$lshzxe 的别名
# 输入的参数中至少要有一个 K 或者 E，否则的话，不管其余的参数是什么，都不会有任何 通知被分发。
# 详细使用可以参考 http://redis.io/topics/notifications
notify-keyspace-events ""

############################### ADVANCED CONFIG ###############################

# 数据量小于等于 hash-max-ziplist-entries 的用 ziplist，大于 hash-max-ziplist-entries用 hash
hash-max-ziplist-entries 512

# value 大小小于等于 hash-max-ziplist-value 的ziplist，大于 hash-max-ziplist-value 用 hash。
hash-max-ziplist-value 64

# 数据量小于等于 list-max-ziplist-entries 用 ziplist，大于 list-max-ziplist-entries用 list。
list-max-ziplist-entries 512

# value 大小小于等于 list-max-ziplist-value 的用ziplist，大于 list-max-ziplist-value 用 list。
list-max-ziplist-value 64

# 数据量小于等于 set-max-intset-entries 用 iniset，大于 set-max-intset-entries 用 set。
set-max-intset-entries 51

# 数据量小于等于 zset-max-ziplist-entries 用 ziplist，大于 zset-max-ziplist-entries用 zset。
zset-max-ziplist-entries 128

# value 大小小于等于 zset-max-ziplist-value 用 ziplist，大于 zset-max-ziplist-value 用 zset。
zset-max-ziplist-value 64


# value 大小小于等于 hll-sparse-max-bytes 使用稀疏数据结构（sparse），大于hll-sparse-max-bytes 使用稠密的数据结构（dense）。
# 一个比 16000 大的 value 是几乎没用的，建议的 value 大概为 3000。如果对 CPU 要求不高，对空间要求较高的，建议设置到 10000 左右。
hll-sparse-max-bytes 3000

# Redis 将在每 100 毫秒时使用 1 毫秒的 CPU 时间来对 redis 的 hash 表进行重新 hash，可以降低内存的使用。
# 当你的使用场景中，有非常严格的实时性需要，不能够接受 Redis 时不时的对请求有 2 毫秒的迟的话，把这项配置为 no。如果没有这么严格的实时性要求，可以设置为 yes，以便能够尽可能快的释放内存。activerehashing yes
## 对客户端输出缓冲进行限制可以强迫那些不从服务器读取数据的客户端断开连接，用来强制关闭传输缓慢的客户端。
# 对于 normal client，第一个 0 表示取消 hard limit，第二个 0 和第三个 0 表示取消 soft limit，normal client 默认取消限制，因为如果没有寻问，他们是不会接收数据的。
client-output-buffer-limit normal 0 0 0

# 对于 slave client 和 MONITER client，如果client-output-buffer 一旦超过 256mb，又或者超过 64mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit slave 256mb 64mb 60

# 对于 pubsub client，如果client-output-buffer 一旦超过 32mb，又或者超过 8mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit pubsub 32mb 8mb 60


# redis 执行任务的频率为 1s 除以 hzhz 10
# 在 aof 重写的时候，如果打开了 aof-rewrite-incremental-fsync 开关，系统会每 32MB 执行一次 fsync。这对于把文件写入磁盘是有帮助的，可以避免过大的延迟峰值。
aof-rewrite-incremental-fsync yes
```

2. 检查从机 1 的配置文件配置，`slave-priority 5`：设置优先级为 5；并将端口设置为 3000：`port 3000`
```bash
# Redis configuration file example

# Note on units: when memory size is needed, it is possible to specify
# it in the usual form of 1k 5GB 4M and so forth:
#
# 当你需要为某个配置项指定内存大小的时候，必须要带上单位，
# 通常的格式就是 1k 5gb 4m 等酱紫：
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# 单位是不区分大小写的，你写 1K 5GB 4M 也行
################################## INCLUDES ###################################
# 假如说你有一个可用于所有的 redis server 的标准配置模板，
# 但针对某些 server 又需要一些个性化的设置，
# 你可以使用 include 来包含一些其他的配置文件，这对你来说是非常有用的。
#
# 但是要注意哦，include 是不能被 config rewrite 命令改写的
# 由于 redis 总是以最后的加工线作为一个配置指令值，所以你最好是把 include 放在这个文件的最前面，
# 以避免在运行时覆盖配置的改变，相反，你就把它放在后面（外国人真啰嗦）。
# 
# include /path/to/local.conf
# include /path/to/other.conf
################################ GENERAL #####################################

# 是否在后台执行，yes：后台运行；no：不是后台运行（老版本默认）
# 由于 docker 容器在启动时，需要任务在前台运行，否则会启动后立即退出，因此导致 redis 容器启动后立即退出问题.
daemonize no

# 指定 redis 只接收来自于该 IP 地址的请求，如果不进行设置，那么将处理所有请求
#bind 127.0.0.1

# 3.2 里的参数，是否开启保护模式，默认开启。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 要是开启了密码 和 bind，可以开启。否 则最好关闭，设置为 no。
protected-mode no

#redis 的进程文件
pidfile /var/run/redis/redis-server.pid

#redis 监听的端口号。
port 3000

# 此参数确定了 TCP 连接中已完成队列(完成三次握手之后)的长度， 当然此值必须不大于 Linux 系统定义的/proc/sys/net/core/somaxconn 值，默认是 511，而 Linux 的默认参数值是 128。
# 当系统并发量大并且客户端速度缓慢的时候，可以将这二个参数一起参考设定。该内核参数默认值一般是 128，对于负载很大的服务程序来说大大的不够。
# 一般会将它修改为 2048 或者更大。在/etc/sysctl.conf 添加:net.core.somaxconn = 2048，然后在终端中执行 sysctl -p。
tcp-backlog 511

# 配置 unix socket 来让 redis 支持监听本地连接。
# unixsocket /var/run/redis/redis.sock

# 配置 unix socket 使用文件的权限
# unixsocketperm 700

# 此参数为设置客户端空闲超过 timeout，服务端会断开连接，为 0 则服务端不会主动断开连接，不能小于 0。
timeout 0

# tcp keepalive 参数。如果设置不为 0，就使用配置 tcp 的 SO_KEEPALIVE 值，
# 使用 keepalive 有两个好处：检测挂掉的对端。降低中间设备出问题而导致网络看似连接却已经与对端端口的问题。
# 在 Linux内核中，设置了 keepalive，redis 会定时给对端发送 ack。检测到对端关闭需要两倍的设置值。
tcp-keepalive 0

# 指定了服务端日志的级别。级别包括：
# debug（很多信息，方便开发、测试），verbose（许多有用的信息，但是没有 debug 级别信息多），notice（适当的日志级别，适合生产环境），warn（只有非常重要的信息）
loglevel notice

# 指定了记录日志的文件。空字符串的话，日志会打印到标准输出设备。后台运行的 redis 标准输出是/dev/null。
logfile /var/log/redis/redis-server.log

#是否打开记录 syslog 功能
# syslog-enabled no

#syslog 的标识符。
# syslog-ident redis

#日志的来源、设备
# syslog-facility local0

#数据库的数量，默认使用的数据库是 DB 0。可以通过”SELECT “命令选择一个 db
databases 16

################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
# save 300 10
# save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data

################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master
slaveof 43.138.106.181 3306

# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
masterauth 000123

# 当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。
slave-serve-stale-data yes

# 作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。
slave-priority 5

# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。
# 这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.

################################## SECURITY ###################################

# requirepass 配置可以让用户使用 AUTH 命令来认证密码，才能使用其他命令。这让 redis 可以使用在不受信任的网络中。
# 为了保持向后的兼容性，可以注释该命令，因为大部分用户也不需要认证。使用requirepass 的时候需要注意，因为 redis 太快了，每秒可以认证 15w 次密码，简单的密码很容易被攻破，所以最好使用一个更复杂的密码。
requirepass 000123

# 把危险的命令给修改成其他名称。比如 CONFIG 命令可以重命名为一个很难被猜到的命令，这样用户不能使用，而内部工具还能接着使用。
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52

# 设置成一个空的值，可以禁止一个命
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置能连上 redis 的最大客户端连接数量。默认是 10000 个客户端连接。
# 由于 redis 不区分连接是客户端连接还是内部打开文件或者和 slave 连接等，所以 maxclients 最小建议设置到 32。如果超过了maxclients，redis 会给新的连接发送’max number of clients reached’，并关闭连接。
# maxclients 10000

# redis 配置的最大内存容量。当内存满了，需要配合 maxmemory-policy 策略进行处理。
# 注意 slave 的输出缓冲区是不计算在 maxmemory 内的。所以为了防止主机内存使用完，建议设置的 maxmemory 要更小一些。
# maxmemory <bytes>

# 内存容量超过 maxmemory 后的处理策略。
# volatile-lru：利用 LRU 算法移除设置过过期时间的 key。
# volatile-random：随机移除设置过过期时间的 key。
# volatile-ttl：移除即将过期的 key，根据最近过期时间来删除（辅以 TTL）
# allkeys-lru：利用 LRU 算法移除任何 key。
# allkeys-random：随机移除任何 key。
# noeviction：不移除任何 key，只是返回一个写错误。
# 上面的这些驱逐策略，如果 redis 没有合适的 key 驱逐，对于写命令，还是会返回错误。redis 将不再接收写请求，只接收 get 请求。
# 写命令包括：set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort。
# maxmemory-policy noeviction

# lru 检测的样本数。使用 lru 或者 ttl 淘汰算法，从需要淘汰的列表中随机选择 sample 个 key，选出闲置时间最长的 key 移除。
# maxmemory-samples 5

############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

################################ LUA SCRIPTING ###############################

# 如果达到最大时间限制（毫秒），redis 会记个 log，然后返回 error。
# 当一个脚本超过了最大时限。只有 SCRIPT KILL 和 SHUTDOWN NOSAVE 可以用。第一个可以杀没有调 write 命令的东西。要是已经调用了 write，只能用第二个命令杀。
lua-time-limit 5000

################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
# cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
# cluster-config-file nodes-6379.conf

# 节点互连超时的阀值。集群节点超时毫秒数
# cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes

################################## SLOW LOG ###################################

# slog log 是用来记录 redis 运行中执行比较慢的命令耗时。当命令的执行超过了指定时间，就记录在 slow log 中，slog log 保存在内存中，所以没有 IO 操作。
# 执行时间比 slowlog-log-slower-than 大的请求记录到 slowlog 里面，单位是微秒，所以 1000000就是 1 秒。
# 注意，负数时间会禁用慢查询日志，而 0 则会强制记录所有命令。
# slowlog-log-slower-than 1000

# 慢查询日志长度。当一个新的命令被写进日志的时候，最老的那个记录会被删掉。这个长度没有限制。只要有足够的内存就行。你可以通过 SLOWLOG RESET 来释放内存。
slowlog-max-len 128

################################ LATENCY MONITOR ##############################

# 延迟监控功能是用来监控 redis 中执行比较缓慢的一些操作，用 LATENCY 打印 redis 实例在跑命令时的耗时图表。
# 只记录大于等于下边设置的值的操作。0 的话，就是关闭监视。默认延迟监控功能是关闭的，如果你需要打开，也可以通过 CONFIG SET 命令动态设置。
latency-monitor-threshold 0

############################# EVENT NOTIFICATION ##############################

# 键空间通知使得客户端可以通过订阅频道或模式，来接收那些以某种方式改动了 Redis 数据集的事件。因为开启键空间通知功能需要消耗一些 CPU ，所以在默认配置下，该功能处于关闭状态。
#notify-keyspace-events 的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知：
##K 键空间通知，所有通知以 __keyspace@__ 为前缀
##E 键事件通知，所有通知以 __keyevent@__ 为前缀
##g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知
##$ 字符串命令的通知
##l 列表命令的通知
##s 集合命令的通知
##h 哈希命令的通知
##z 有序集合命令的通知
##x 过期事件：每当有过期键被删除时发送
##e 驱逐(evict)事件：每当有键因为 maxmemory 政策而被删除时发送
##A 参数 g$lshzxe 的别名
# 输入的参数中至少要有一个 K 或者 E，否则的话，不管其余的参数是什么，都不会有任何 通知被分发。
# 详细使用可以参考 http://redis.io/topics/notifications
notify-keyspace-events ""

############################### ADVANCED CONFIG ###############################

# 数据量小于等于 hash-max-ziplist-entries 的用 ziplist，大于 hash-max-ziplist-entries用 hash
hash-max-ziplist-entries 512

# value 大小小于等于 hash-max-ziplist-value 的ziplist，大于 hash-max-ziplist-value 用 hash。
hash-max-ziplist-value 64

# 数据量小于等于 list-max-ziplist-entries 用 ziplist，大于 list-max-ziplist-entries用 list。
list-max-ziplist-entries 512

# value 大小小于等于 list-max-ziplist-value 的用ziplist，大于 list-max-ziplist-value 用 list。
list-max-ziplist-value 64

# 数据量小于等于 set-max-intset-entries 用 iniset，大于 set-max-intset-entries 用 set。
set-max-intset-entries 51

# 数据量小于等于 zset-max-ziplist-entries 用 ziplist，大于 zset-max-ziplist-entries用 zset。
zset-max-ziplist-entries 128

# value 大小小于等于 zset-max-ziplist-value 用 ziplist，大于 zset-max-ziplist-value 用 zset。
zset-max-ziplist-value 64


# value 大小小于等于 hll-sparse-max-bytes 使用稀疏数据结构（sparse），大于hll-sparse-max-bytes 使用稠密的数据结构（dense）。
# 一个比 16000 大的 value 是几乎没用的，建议的 value 大概为 3000。如果对 CPU 要求不高，对空间要求较高的，建议设置到 10000 左右。
hll-sparse-max-bytes 3000

# Redis 将在每 100 毫秒时使用 1 毫秒的 CPU 时间来对 redis 的 hash 表进行重新 hash，可以降低内存的使用。
# 当你的使用场景中，有非常严格的实时性需要，不能够接受 Redis 时不时的对请求有 2 毫秒的迟的话，把这项配置为 no。如果没有这么严格的实时性要求，可以设置为 yes，以便能够尽可能快的释放内存。activerehashing yes
## 对客户端输出缓冲进行限制可以强迫那些不从服务器读取数据的客户端断开连接，用来强制关闭传输缓慢的客户端。
# 对于 normal client，第一个 0 表示取消 hard limit，第二个 0 和第三个 0 表示取消 soft limit，normal client 默认取消限制，因为如果没有寻问，他们是不会接收数据的。
client-output-buffer-limit normal 0 0 0

# 对于 slave client 和 MONITER client，如果client-output-buffer 一旦超过 256mb，又或者超过 64mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit slave 256mb 64mb 60

# 对于 pubsub client，如果client-output-buffer 一旦超过 32mb，又或者超过 8mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit pubsub 32mb 8mb 60


# redis 执行任务的频率为 1s 除以 hzhz 10
# 在 aof 重写的时候，如果打开了 aof-rewrite-incremental-fsync 开关，系统会每 32MB 执行一次 fsync。这对于把文件写入磁盘是有帮助的，可以避免过大的延迟峰值。
aof-rewrite-incremental-fsync yes
```

3. 检查从机 2 的配置文件配置，`slave-priority 10`：设置优先级为 10；并将端口设置为 9000：`port 9000`

```bash
# Redis configuration file example

# Note on units: when memory size is needed, it is possible to specify
# it in the usual form of 1k 5GB 4M and so forth:
#
# 当你需要为某个配置项指定内存大小的时候，必须要带上单位，
# 通常的格式就是 1k 5gb 4m 等酱紫：
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# 单位是不区分大小写的，你写 1K 5GB 4M 也行
################################## INCLUDES ###################################
# 假如说你有一个可用于所有的 redis server 的标准配置模板，
# 但针对某些 server 又需要一些个性化的设置，
# 你可以使用 include 来包含一些其他的配置文件，这对你来说是非常有用的。
#
# 但是要注意哦，include 是不能被 config rewrite 命令改写的
# 由于 redis 总是以最后的加工线作为一个配置指令值，所以你最好是把 include 放在这个文件的最前面，
# 以避免在运行时覆盖配置的改变，相反，你就把它放在后面（外国人真啰嗦）。
# 
# include /path/to/local.conf
# include /path/to/other.conf
################################ GENERAL #####################################

# 是否在后台执行，yes：后台运行；no：不是后台运行（老版本默认）
# 由于 docker 容器在启动时，需要任务在前台运行，否则会启动后立即退出，因此导致 redis 容器启动后立即退出问题.
daemonize no

# 指定 redis 只接收来自于该 IP 地址的请求，如果不进行设置，那么将处理所有请求
#bind 127.0.0.1

# 3.2 里的参数，是否开启保护模式，默认开启。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 要是开启了密码 和 bind，可以开启。否 则最好关闭，设置为 no。
protected-mode no

#redis 的进程文件
pidfile /var/run/redis/redis-server.pid

#redis 监听的端口号。
port 9000

# 此参数确定了 TCP 连接中已完成队列(完成三次握手之后)的长度， 当然此值必须不大于 Linux 系统定义的/proc/sys/net/core/somaxconn 值，默认是 511，而 Linux 的默认参数值是 128。
# 当系统并发量大并且客户端速度缓慢的时候，可以将这二个参数一起参考设定。该内核参数默认值一般是 128，对于负载很大的服务程序来说大大的不够。
# 一般会将它修改为 2048 或者更大。在/etc/sysctl.conf 添加:net.core.somaxconn = 2048，然后在终端中执行 sysctl -p。
tcp-backlog 511

# 配置 unix socket 来让 redis 支持监听本地连接。
# unixsocket /var/run/redis/redis.sock

# 配置 unix socket 使用文件的权限
# unixsocketperm 700

# 此参数为设置客户端空闲超过 timeout，服务端会断开连接，为 0 则服务端不会主动断开连接，不能小于 0。
timeout 0

# tcp keepalive 参数。如果设置不为 0，就使用配置 tcp 的 SO_KEEPALIVE 值，
# 使用 keepalive 有两个好处：检测挂掉的对端。降低中间设备出问题而导致网络看似连接却已经与对端端口的问题。
# 在 Linux内核中，设置了 keepalive，redis 会定时给对端发送 ack。检测到对端关闭需要两倍的设置值。
tcp-keepalive 0

# 指定了服务端日志的级别。级别包括：
# debug（很多信息，方便开发、测试），verbose（许多有用的信息，但是没有 debug 级别信息多），notice（适当的日志级别，适合生产环境），warn（只有非常重要的信息）
loglevel notice

# 指定了记录日志的文件。空字符串的话，日志会打印到标准输出设备。后台运行的 redis 标准输出是/dev/null。
logfile /var/log/redis/redis-server.log

#是否打开记录 syslog 功能
# syslog-enabled no

#syslog 的标识符。
# syslog-ident redis

#日志的来源、设备
# syslog-facility local0

#数据库的数量，默认使用的数据库是 DB 0。可以通过”SELECT “命令选择一个 db
databases 16

################################ SNAPSHOTTING ################################

# 快照配置
# 注释掉“save”这一行配置项就可以让保存数据库功能失效
# 设置 sedis 进行数据库镜像的频率。
# 900 秒（15 分钟）内至少 1 个 key 值改变（则进行数据库保存--持久化）
# 300 秒（5 分钟）内至少 10 个 key 值改变（则进行数据库保存--持久化）
# 60 秒（1 分钟）内至少 10000 个 key 值改变（则进行数据库保存--持久化）
save 900 1
# save 300 10
# save 60 10000

# 当 RDB 持久化出现错误后，是否依然进行继续进行工作，yes：不能进行工作，no：可以继续进行工作，可以通过 info 中的 rdb_last_bgsave_status 了解 RDB 持久化是否有错误
stop-writes-on-bgsave-error yes

# 使用压缩 rdb 文件，rdb 文件压缩使用 LZF 压缩算法，yes：压缩，但是需要一些 cpu 的消耗。no：不压缩，需要更多的磁盘空间
rdbcompression yes

# 是否校验 rdb 文件。从 rdb 格式的第五个版本开始，在 rdb 文件的末尾会带上 CRC64 的校验和。这跟有利于文件的容错性，但是在保存 rdb 文件的时候，会有大概 10%的性能损耗，所以如果你追求高性能，可以关闭该配置。
rdbchecksum yes

# rdb 文件的名称
dbfilename dump.rdb

# 数据目录，数据库的写入会在这个目录。rdb、aof 文件也会写在这个目录
dir /data

################################# REPLICATION #################################

# 复制选项，slave 复制对应的 master
slaveof 43.138.106.181 3306

# 如果 master 设置了 requirepass，那么 slave 要连上 master，需要有 master 的密码才行。masterauth 就是用来配置 master 的密码，这样可以在连上 master 后进行认证。
masterauth 000123

# 当从库同主机失去连接或者复制正在进行，从机库有两种运行方式：
# 1：如果slave-serve-stale-data 设置为 yes(默认设置)，从库会继续响应客户端的请求。
# 2：如果slave-serve-stale-data 设置为 no，除去 INFO 和 SLAVOF 命令之外的任何请求都会返回一个错误”SYNC with master in progress”。
slave-serve-stale-data yes

# 作为从服务器，默认情况下是只读的（yes），可以修改成 NO，用于写（不建议）。
slave-read-only yes

# 是否使用 socket 方式复制数据。目前 redis 复制提供两种方式，disk 和 socket。如果新的 slave连上来或者重连的 slave 无法部分同步，就会执行全量同步，master 会生成 rdb 文件。
# 有 2 种方式：
# 1：disk 方式是 master 创建一个新的进程把 rdb 文件保存到磁盘，再把磁盘上的 rdb 文件传递给 slave。
# 2：socket 是 master 创建一个新的进程，直接把 rdb 文件以 socket 的方式发给 slave。
# disk 方式的时候，当一个 rdb 保存的过程中，多个 slave 都能共享这个 rdb 文件。
# socket 的方式就的一个个 slave顺序复制。在磁盘速度缓慢，网速快的情况下推荐用 socket 方式。
repl-diskless-sync no

# diskless 复制的延迟时间，防止设置为 0。一旦复制开始，节点不会再接收新 slave 的复制请求直到下一个 rdb 传输。所以最好等待一段时间，等更多的 slave 连上来。
repl-diskless-sync-delay 5

# slave 根据指定的时间间隔向服务器发送 ping 请求。时间间隔可以通过 repl_ping_slave_period 来设置，默认 10 秒。
# repl-ping-slave-period 10

# 复制连接超时时间。master 和 slave 都有超时时间的设置。
# master 检测到 slave 上次发送的时间超过 repl-timeout，即认为 slave 离线，清除该 slave 信息。
# slave 检测到上次和 master 交互的时间超过 repl-timeout，则认为 master 离线。
# 需要注意的是 repl-timeout 需要设置一个比repl-ping-slave-period 更大的值，不然会经常检测到超时。
# repl-timeout 60

# 是否禁止复制 tcp 链接的 tcp nodelay 参数，可传递 yes 或者 no。默认是 no，即使用 tcp nodelay。
# 如果 master 设置了 yes 来禁止 tcp nodelay 设置，在把数据复制给 slave 的时候，会减少包的数量和更小的网络带宽。
# 但是这也可能带来数据的延迟。默认我们推荐更小的延迟，但是在数据量传输很大的场景下，建议选择 yes。
repl-disable-tcp-nodelay no

# 复制缓冲区大小，这是一个环形复制缓冲区，用来保存最新复制的命令。
# 这样在 slave 离线的时候，不需要完全复制 master 的数据，如果可以执行部分同步，只需要把缓冲区的部分数据复制给 slave，就能恢复正常复制状态。
# 缓冲区的大小越大，slave 离线的时间可以更长，复制缓冲区只有在有 slave 连接的时候才分配内存。没有 slave 的一段时间，内存会被释放出来，默认 1m。
# repl-backlog-size 5mb

# master 没有 slave 一段时间会释放复制缓冲区的内存，repl-backlog-ttl 用来设置该时间长度。单位为秒。
# repl-backlog-ttl 3600

# 当 master 不可用，Sentinel 会根据 slave 的优先级选举一个 master。最低的优先级的 slave，当选 master。而配置成 0，永远不会被选举。
slave-priority 10

# redis 提供了可以让 master 停止写入的方式，如果配置了 min-slaves-to-write，健康的 slave的个数小于 N，mater 就禁止写入。
# master 最少得有多少个健康的 slave 存活才能执行写命令。
# 这个置虽然不能保证 N 个 slave 都一定能接收到 master 的写操作，但是能避免没有足够健康的 slave 的候，master 不能写入来避免数据丢失。设置为 0 是关闭该功能。
# min-slaves-to-write 3

# 延迟小于 min-slaves-max-lag 秒的 slave 才认为是健康的 slave。
# min-slaves-max-lag 10

# 设置 1 或另一个设置为 0 禁用这个特性。
# Setting one or the other to 0 disables the feature.
# By default min-slaves-to-write is set to 0 (feature disabled) and
# min-slaves-max-lag is set to 10.

################################## SECURITY ###################################

# requirepass 配置可以让用户使用 AUTH 命令来认证密码，才能使用其他命令。这让 redis 可以使用在不受信任的网络中。
# 为了保持向后的兼容性，可以注释该命令，因为大部分用户也不需要认证。使用requirepass 的时候需要注意，因为 redis 太快了，每秒可以认证 15w 次密码，简单的密码很容易被攻破，所以最好使用一个更复杂的密码。
requirepass 000123

# 把危险的命令给修改成其他名称。比如 CONFIG 命令可以重命名为一个很难被猜到的命令，这样用户不能使用，而内部工具还能接着使用。
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52

# 设置成一个空的值，可以禁止一个命
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置能连上 redis 的最大客户端连接数量。默认是 10000 个客户端连接。
# 由于 redis 不区分连接是客户端连接还是内部打开文件或者和 slave 连接等，所以 maxclients 最小建议设置到 32。如果超过了maxclients，redis 会给新的连接发送’max number of clients reached’，并关闭连接。
# maxclients 10000

# redis 配置的最大内存容量。当内存满了，需要配合 maxmemory-policy 策略进行处理。
# 注意 slave 的输出缓冲区是不计算在 maxmemory 内的。所以为了防止主机内存使用完，建议设置的 maxmemory 要更小一些。
# maxmemory <bytes>

# 内存容量超过 maxmemory 后的处理策略。
# volatile-lru：利用 LRU 算法移除设置过过期时间的 key。
# volatile-random：随机移除设置过过期时间的 key。
# volatile-ttl：移除即将过期的 key，根据最近过期时间来删除（辅以 TTL）
# allkeys-lru：利用 LRU 算法移除任何 key。
# allkeys-random：随机移除任何 key。
# noeviction：不移除任何 key，只是返回一个写错误。
# 上面的这些驱逐策略，如果 redis 没有合适的 key 驱逐，对于写命令，还是会返回错误。redis 将不再接收写请求，只接收 get 请求。
# 写命令包括：set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort。
# maxmemory-policy noeviction

# lru 检测的样本数。使用 lru 或者 ttl 淘汰算法，从需要淘汰的列表中随机选择 sample 个 key，选出闲置时间最长的 key 移除。
# maxmemory-samples 5

############################## APPEND ONLY MODE ###############################

# 默认 redis 使用的是 rdb 方式持久化，这种方式在许多应用中已经足够用了。
# 但是 redis 如果中途宕机，会导致可能有几分钟的数据丢失，根据 save 来策略进行持久化，Append Only File 是另一种持久化方式，可以提供更好的持久化特性。
# Redis 会把每次写入的数据在接收后都写入 appendonly.aof 文件，每次启动时 Redis 都会先把这个文件的数据读入内存里，先忽略 RDB 文件。
appendonly yes

# aof 文件名
appendfilename "appendonly.aof"

# aof 持久化策略的配置
# no 表示不执行 fsync，由操作系统保证数据同步到磁盘，速度最快。
# always 表示每次写入都执行 fsync，以保证数据同步到磁盘。
# everysec 表示每秒执行一次 fsync，可能会导致丢失这 1s 数据。
appendfsync everysec

# 在 aof 重写或者写入 rdb 文件的时候，会执行大量 IO，此时对于 everysec 和 always 的 aof 模式来说，执行 fsync 会造成阻塞过长时间，no-appendfsync-on-rewrite 字段设置为默认设置为 no。
# 如果对延迟要求很高的应用，这个字段可以设置为 yes，否则还是设置为 no，这样对持久化特性来说这更安全的选择。
# 设置为 yes 表示 rewrite 期间对新写操作不 fsync,暂时存在内存中,等 rewrite 完成后再写入，默认为 no，建议 yes。Linux 的默认 fsync 策略是 30 秒。可能丢失 30 秒数据。
no-appendfsync-on-rewrite no

# aof 自动重写配置。当目前 aof 文件大小超过上一次重写的 aof 文件大小的百分之多少进行重写，即当aof 文件增长到一定大小的时候 Redis 能够调用 bgrewriteaof 对日志文件进行重写。
# 当前 AOF 文件大小是上次日志重写得到 AOF 文件大小的二倍（设置为 100）时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100

# 设置允许重写的最小 aof 文件大小，避免了达到约定百分比但尺寸仍然很小的情况还要重写
auto-aof-rewrite-min-size 64mb

# aof 文件可能在尾部是不完整的，当 redis 启动的时候，aof 文件的数据被载入内存。
# 重启可能发生在redis 所在的主机操作系统宕机后，尤其在 ext4 文件系统没有加上 data=ordered 选项（redis 宕机或者异常终止不会造成尾部不完整现象。）
# 出现这种现象，可以选择让 redis 退出，或者导入尽可能多的数据。
# 如果选择的是 yes，当截断的 aof 文件被导入的时候，会自动发布一个 log 给客户端然后 load。如果是 no，用户必须手动 redis-check-aof 修复 AOF 文件才可以
# aof-load-truncated yes

################################ LUA SCRIPTING ###############################

# 如果达到最大时间限制（毫秒），redis 会记个 log，然后返回 error。
# 当一个脚本超过了最大时限。只有 SCRIPT KILL 和 SHUTDOWN NOSAVE 可以用。第一个可以杀没有调 write 命令的东西。要是已经调用了 write，只能用第二个命令杀。
lua-time-limit 5000

################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
# cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
# cluster-config-file nodes-6379.conf

# 节点互连超时的阀值。集群节点超时毫秒数
# cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes

################################## SLOW LOG ###################################

# slog log 是用来记录 redis 运行中执行比较慢的命令耗时。当命令的执行超过了指定时间，就记录在 slow log 中，slog log 保存在内存中，所以没有 IO 操作。
# 执行时间比 slowlog-log-slower-than 大的请求记录到 slowlog 里面，单位是微秒，所以 1000000就是 1 秒。
# 注意，负数时间会禁用慢查询日志，而 0 则会强制记录所有命令。
# slowlog-log-slower-than 1000

# 慢查询日志长度。当一个新的命令被写进日志的时候，最老的那个记录会被删掉。这个长度没有限制。只要有足够的内存就行。你可以通过 SLOWLOG RESET 来释放内存。
slowlog-max-len 128

################################ LATENCY MONITOR ##############################

# 延迟监控功能是用来监控 redis 中执行比较缓慢的一些操作，用 LATENCY 打印 redis 实例在跑命令时的耗时图表。
# 只记录大于等于下边设置的值的操作。0 的话，就是关闭监视。默认延迟监控功能是关闭的，如果你需要打开，也可以通过 CONFIG SET 命令动态设置。
latency-monitor-threshold 0

############################# EVENT NOTIFICATION ##############################

# 键空间通知使得客户端可以通过订阅频道或模式，来接收那些以某种方式改动了 Redis 数据集的事件。因为开启键空间通知功能需要消耗一些 CPU ，所以在默认配置下，该功能处于关闭状态。
#notify-keyspace-events 的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知：
##K 键空间通知，所有通知以 __keyspace@__ 为前缀
##E 键事件通知，所有通知以 __keyevent@__ 为前缀
##g DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知
##$ 字符串命令的通知
##l 列表命令的通知
##s 集合命令的通知
##h 哈希命令的通知
##z 有序集合命令的通知
##x 过期事件：每当有过期键被删除时发送
##e 驱逐(evict)事件：每当有键因为 maxmemory 政策而被删除时发送
##A 参数 g$lshzxe 的别名
# 输入的参数中至少要有一个 K 或者 E，否则的话，不管其余的参数是什么，都不会有任何 通知被分发。
# 详细使用可以参考 http://redis.io/topics/notifications
notify-keyspace-events ""

############################### ADVANCED CONFIG ###############################

# 数据量小于等于 hash-max-ziplist-entries 的用 ziplist，大于 hash-max-ziplist-entries用 hash
hash-max-ziplist-entries 512

# value 大小小于等于 hash-max-ziplist-value 的ziplist，大于 hash-max-ziplist-value 用 hash。
hash-max-ziplist-value 64

# 数据量小于等于 list-max-ziplist-entries 用 ziplist，大于 list-max-ziplist-entries用 list。
list-max-ziplist-entries 512

# value 大小小于等于 list-max-ziplist-value 的用ziplist，大于 list-max-ziplist-value 用 list。
list-max-ziplist-value 64

# 数据量小于等于 set-max-intset-entries 用 iniset，大于 set-max-intset-entries 用 set。
set-max-intset-entries 51

# 数据量小于等于 zset-max-ziplist-entries 用 ziplist，大于 zset-max-ziplist-entries用 zset。
zset-max-ziplist-entries 128

# value 大小小于等于 zset-max-ziplist-value 用 ziplist，大于 zset-max-ziplist-value 用 zset。
zset-max-ziplist-value 64


# value 大小小于等于 hll-sparse-max-bytes 使用稀疏数据结构（sparse），大于hll-sparse-max-bytes 使用稠密的数据结构（dense）。
# 一个比 16000 大的 value 是几乎没用的，建议的 value 大概为 3000。如果对 CPU 要求不高，对空间要求较高的，建议设置到 10000 左右。
hll-sparse-max-bytes 3000

# Redis 将在每 100 毫秒时使用 1 毫秒的 CPU 时间来对 redis 的 hash 表进行重新 hash，可以降低内存的使用。
# 当你的使用场景中，有非常严格的实时性需要，不能够接受 Redis 时不时的对请求有 2 毫秒的迟的话，把这项配置为 no。如果没有这么严格的实时性要求，可以设置为 yes，以便能够尽可能快的释放内存。activerehashing yes
## 对客户端输出缓冲进行限制可以强迫那些不从服务器读取数据的客户端断开连接，用来强制关闭传输缓慢的客户端。
# 对于 normal client，第一个 0 表示取消 hard limit，第二个 0 和第三个 0 表示取消 soft limit，normal client 默认取消限制，因为如果没有寻问，他们是不会接收数据的。
client-output-buffer-limit normal 0 0 0

# 对于 slave client 和 MONITER client，如果client-output-buffer 一旦超过 256mb，又或者超过 64mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit slave 256mb 64mb 60

# 对于 pubsub client，如果client-output-buffer 一旦超过 32mb，又或者超过 8mb 持续 60 秒，那么服务器就会立即断开客户端连接。
client-output-buffer-limit pubsub 32mb 8mb 60


# redis 执行任务的频率为 1s 除以 hzhz 10
# 在 aof 重写的时候，如果打开了 aof-rewrite-incremental-fsync 开关，系统会每 32MB 执行一次 fsync。这对于把文件写入磁盘是有帮助的，可以避免过大的延迟峰值。
aof-rewrite-incremental-fsync yes
```

4. 在从机的 config 目录下创建 `sentinel.conf` 文件，输入内容
```bash
# 哨兵模式配置

# 禁止保护模式。要是配置里没有指定 bind 和密码。开启该参数后，redis 只会本地进行访问，拒绝外部访问。
# 使用主从复制一定要禁止
protected-mode no

# 配置监听的主服务器，这里 sentinel monitor 代表监控，mymaster 代表服务器的名称，可以自定义
# 43.138.106.181 代表监控的主服务器，3306 代表端口，2 代表只有两个或两个以上的哨兵认为主服务器不可用的时候，才会进行 failover 操作。
sentinel monitor mymaster 43.138.106.181 3306 1

# sentinel author-pass 定义服务的密码，mymaster 是服务名称，123456 是 Redis 服务器密码
sentinel auth-pass mymaster 000123
```

5. 启动主机：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:3306 --name redis -v /home/docker/docker/VOLUME/redis/config:/etc/redis -v /home/docker/docker/VOLUME/redis/data:/data -v /home/docker/docker/VOLUME/redis/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
6. 启动从机 1：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3000:3000 --name redis2 -v /home/docker/docker/VOLUME/redis2/config:/etc/redis -v /home/docker/docker/VOLUME/redis2/data:/data -v /home/docker/docker/VOLUME/redis2/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
7. 进入 redis 终端后， 启动从机 1 的哨兵：`redis-sentinel /etc/redis/sentinel.conf`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-279--rpi9rM-QWfei3w.png)

8. 启动从机 2：`docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 9000:9000 --name redis3 -v /home/docker/docker/VOLUME/redis3/config:/etc/redis -v /home/docker/docker/VOLUME/redis3/data:/data -v /home/docker/docker/VOLUME/redis3/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf`
9. 进入 redis 终端后，启动从机 2 的哨兵：`redis-sentinel /etc/redis/sentinel.conf`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-469--YSnLIQ70obOhtg.png)

10. 查看运行状态：`info replication`；进入指定端口号的服务：`redis-cli -p 3000`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-564--hYGVoC1VOIpUuQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-633--_-mk-CawsTIXxQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-782--ciEGLEm7Qdiw-w.png)

11. 关闭主机

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-55-940--zvH4RZCZTix_gA.png)

12. 从机反应

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-062--PVwtQAlm2aK1WQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-179--dQZw0SFQIGs-rg.png)

13. 再次查看运行状态：`info replication`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-310--yJKGDIMz8LYOcw.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-465--CDo-hx0hXmjwbg.png)

14. 重启主机

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-629--w_fzuZkpJ3jFTw.png)

15. 查看主机运行状态：`info replication`，主机变为了从机

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-695--pL5LQGqYJOYqlQ.png)

## 7、缺点：复制延时

由于所有的写操作都是先在 Master 上操作，然后同步更新到 Slave 上，所以从 Master 同步到 Slave 机器有一定的延迟，当系统很繁忙的时候，延迟问题会更加严重，Slave 机器数量的增加也会使这个问题更加严重。

## 8、故障恢复

1. 优先级在 redis.conf 中默认：`slave-priority 100`，值越小优先级越高
2. 偏移量是指获得原主机数据最全的
3. 每个 redis 实例启动后都会随机生成一个 40 位的 runid

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-799--AXp65v29rLK6Nw.png)

# 十一、Redis 集群

## 1、问题

1. 容量不够，redis 如何进行扩容？
2. 并发写操作， redis 如何分摊？
3. 另外，主从模式，薪火相传模式，主机宕机，导致 ip 地址发生变化，应用程序中配置需要修改对应的主机地址、端口等信息。
4. 之前通过代理主机来解决，但是 redis3.0 中提供了解决方案。就是无中心化集群配置。

## 2、什么是集群

1. Redis 集群实现了对 Redis 的水平扩容，即启动 N 个 redis 节点，将整个数据库分布存储在这 N 个节点中，每个节点存储总数据的 1/N。
2. Redis 集群通过分区（partition）来提供一定程度的可用性（availability）： 即使集群中有一部分节点失效或者无法进行通讯， 集群也可以继续处理命令请求。

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726091936.png)

## 3、集群的使用

```bash
################################ REDIS CLUSTER ###############################

# 集群开关，默认是不开启集群模式
cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
cluster-config-file nodes-3000.conf

# 节点互连超时的阀值。集群节点超时毫秒数
cluster-node-timeout 15000

# 在进行故障转移的时候，全部 slave 都会请求申请为 master，但是有些 slave 可能与 master 断开连接一段时间了，导致数据过于陈旧，这样的 slave 不应该被提升为 master。
# 该参数就是用来判断 slave 节点与 master 断线的时间是否过长。判断方法是：
# 比较 slave 断开连接的时间和(node-timeout * slave-validity-factor) + repl-ping-slave-period
# 如果节点超时时间为三十秒, 并且 slave-validity-factor 为 10，假设默认的 repl-ping-slave-period 是 10 秒，即如果超过 310 秒 slave 将不会尝试进行故障转移
# cluster-slave-validity-factor 10

# master 的 slave 数量大于该值，slave 才能迁移到其他孤立 master 上，如这个参数若被设为 2，那么只有当一个主节点拥有 2 个可工作的从节点时，它的一个从节点会尝试迁移。
# cluster-migration-barrier 1

# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes
```

### ①、先创建 6 个 redis 服务

> 三主三从
> 本次使用的端口：3000、3306、7777、7778、80、9000
> 集群也需要所有密码相同

1. 创建 6 个映射目录

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-56-915--3kY7jVPhAOsHug.png)

2. 修改配置文件；例子是 3000 端口，其他也要修改

```bash
#redis 监听的端口号。
port 3000

# 集群开关，默认是不开启集群模式
cluster-enabled yes

# 集群配置文件的名称，每个节点都有一个集群相关的配置文件，持久化保存集群的信息。
# 这个文件并不需要手动配置，这个配置文件有 Redis 生成并更新，每个 Redis 集群节点需要一个单独的配置文件，请确保与实例运行的系统中配置文件名称不冲突
cluster-config-file nodes-3000.conf

# 节点互连超时的阀值。集群节点超时毫秒数
cluster-node-timeout 15000
```

3. 启动容器

```bash
docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3000:3000 --name redis3000 -v /home/docker/docker/VOLUME/redis3000/config:/etc/redis -v /home/docker/docker/VOLUME/redis3000/data:/data -v /home/docker/docker/VOLUME/redis3000/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:3306 --name redis3306 -v /home/docker/docker/VOLUME/redis3306/config:/etc/redis -v /home/docker/docker/VOLUME/redis3306/data:/data -v /home/docker/docker/VOLUME/redis3306/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 7777:7777 --name redis7777 -v /home/docker/docker/VOLUME/redis7777/config:/etc/redis -v /home/docker/docker/VOLUME/redis7777/data:/data -v /home/docker/docker/VOLUME/redis7777/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 7778:7778 --name redis7778 -v /home/docker/docker/VOLUME/redis7778/config:/etc/redis -v /home/docker/docker/VOLUME/redis7778/data:/data -v /home/docker/docker/VOLUME/redis7778/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 80:80 --name redis80 -v /home/docker/docker/VOLUME/redis80/config:/etc/redis -v /home/docker/docker/VOLUME/redis80/data:/data -v /home/docker/docker/VOLUME/redis80/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 9000:9000 --name redis9000 -v /home/docker/docker/VOLUME/redis9000/config:/etc/redis -v /home/docker/docker/VOLUME/redis9000/data:/data -v /home/docker/docker/VOLUME/redis9000/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-055--kYYfLx_Tyav1WQ.png)

### ②、构建集群

1. 进入任意一个 redis 容器：`docker exec -it 4096974ccb6c bash`

```bash
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
fd992d6652a9   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   6379/tcp, 0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   redis9000
ab91da8c825b   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp, 6379/tcp           redis80
5bc13c71ccce   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   6379/tcp, 0.0.0.0:7778->7778/tcp, :::7778->7778/tcp   redis7778
736d7af5901b   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   6379/tcp, 0.0.0.0:7777->7777/tcp, :::7777->7777/tcp   redis7777
cd4838cad245   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 6379/tcp   redis3306
4096974ccb6c   redis:6.2.1                  "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp, 6379/tcp   redis3000
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             6 days ago       Up 6 days       0.0.0.0:9443->9000/tcp, :::9443->9000/tcp             naughty_kowalevski

docker@VM-8-15-ubuntu:~$ docker exec -it 4096974ccb6c bash

root@4096974ccb6c:/data# 
```

2. 使用命令创建集群：`redis-cli --cluster create --cluster-replicas 1 -a 000123 43.138.106.181:3000 43.138.106.181:3306 43.138.106.181:7777 43.138.106.181:7778 43.138.106.181:80 43.138.106.181:9000`，
   1. `redis-cli --cluster`：创建集群
   2. `create --cluster-replicas 1`：创建集群的方式，`1` 表示每个主节点需要1个从节点
   3. `-a 000123`：密码
3. 输入 `yes` 确认

## 4、卡在等待集群加入

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-165--_ml2b7s8xuj1sQ.png)

### ①、原因

1. 遇到这种情况大部分是因为集群总线的端口没有开放！
2. 每个 Redis 集群中的节点都需要打开两个 TCP 连接。一个连接用于正常的给 Client 提供服务，比如 6379，还有一个额外的端口（通过在这个端口号上加10000）作为数据端口，例如：redis 的端口为 6379，那么另外一个需要开通的端口是：6379 + 10000， 即需要开启 16379。16379 端口用于集群总线，这是一个用二进制协议的点对点通信信道。这个集群总线（Cluster bus）用于节点的失败侦测、配置更新、故障转移授权，等等。

### ②、解决方法

1. 防火墙中打开对应端口，如：13000、13306、17777、17778、10080、19000
2. 关闭并删除容器
3. 重新启动容器时增加映射的端口

```bash
docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3000:3000 -p 13000:13000 --name redis3000 -v /home/docker/docker/VOLUME/redis3000/config:/etc/redis -v /home/docker/docker/VOLUME/redis3000/data:/data -v /home/docker/docker/VOLUME/redis3000/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 3306:3306 -p 13306:13306 --name redis3306 -v /home/docker/docker/VOLUME/redis3306/config:/etc/redis -v /home/docker/docker/VOLUME/redis3306/data:/data -v /home/docker/docker/VOLUME/redis3306/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 7777:7777 -p 17777:17777 --name redis7777 -v /home/docker/docker/VOLUME/redis7777/config:/etc/redis -v /home/docker/docker/VOLUME/redis7777/data:/data -v /home/docker/docker/VOLUME/redis7777/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 7778:7778 -p 17778:17778 --name redis7778 -v /home/docker/docker/VOLUME/redis7778/config:/etc/redis -v /home/docker/docker/VOLUME/redis7778/data:/data -v /home/docker/docker/VOLUME/redis7778/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 80:80 -p 10080:10080 --name redis80 -v /home/docker/docker/VOLUME/redis80/config:/etc/redis -v /home/docker/docker/VOLUME/redis80/data:/data -v /home/docker/docker/VOLUME/redis80/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf


docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 9000:9000 -p 19000:19000 --name redis9000 -v /home/docker/docker/VOLUME/redis9000/config:/etc/redis -v /home/docker/docker/VOLUME/redis9000/data:/data -v /home/docker/docker/VOLUME/redis9000/log:/var/log/redis -d redis:6.2.1 redis-server /etc/redis/redis.conf
```

## 5、如何分配这六个节点

1. 一个集群至少要有三个主节点。
2. 选项 `--cluster-replicas 1` 表示我们希望为集群中的每个主节点创建一个从节点。
3. 分配原则尽量保证每个主数据库运行在不同的 IP 地址，每个从库和主库不在一个IP地址上。

## 6、数据操作

### ①、插槽 slots

1. 一个 Redis 集群包含 16384 个插槽（hash slot）， 数据库中的每个键都属于这 16384 个插槽的其中一个， 
2. 集群使用公式 `CRC16(key) % 16384` 来计算键 key 属于哪个槽， 其中 CRC16(key) 语句用于计算键 key 的 CRC16 校验和 。
3. 集群中的每个节点负责处理一部分插槽。 举个例子， 如果一个集群可以有主节点， 其中：
   1. 节点 A 负责处理 0 号至 5460 号插槽。
   2. 节点 B 负责处理 5461 号至 10922 号插槽。
   3. 节点 C 负责处理 10923 号至 16383 号插槽。

### ②、在集群中录入值

1. 在 redis-cli 每次录入、查询键值，redis 都会计算出该 key 应该送往的插槽，如果不是该客户端对应服务器的插槽，redis 会报错，并告知应前往的 redis 实例地址和端口。
2. redis-cli 客户端提供了 `–c` 参数实现自动重定向。
3. 如 `redis-cli  -c –p 6379` 登入后，再录入、查询键值对可以自动重定向。
4. 不在一个 slot 下的键值，是不能使用 mget、mset 等多键操作。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-317--pq-EmlCPoN_Vgg.png)

5. 可以通过 `{组名}` 来定义组的概念，从而使 key 中 `{}` 内相同内容的键值对放到一个 slot 中去。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-427--nysB7PzXDYb__Q.png)

### ③、查询集群中的值

`CLUSTER GETKEYSINSLOT <slot> <count>`：返回 count 个 slot 槽中的键。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-532--nmms0WZ1z-7B9g.png)

## 7、故障恢复

1. 如果主节点下线，从节点能否自动升为主节点？注意：15秒超时

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-630--J3LE6_VXZZFBuQ.png)

2. 主节点恢复后，主从关系会如何？主节点回来变成从机。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-782--cB25de7Vq9aG-w.png)

3. 如果所有某一段插槽的主从节点都宕掉，redis服务是否还能继续?
   1. 如果某一段插槽的主从都挂掉，而 `cluster-require-full-coverage` 为 `yes` ，那么 ，整个集群都挂掉
   2. 如果某一段插槽的主从都挂掉，而 `cluster-require-full-coverage` 为 `no` ，那么，该插槽数据全都不能使用，也无法存储，其他插槽依然可以使用
4. redis.conf 中的参数  `cluster-require-full-coverage`

```bash
# 默认情况下，集群全部的 slot 有节点负责，集群状态才为 ok，才能提供服务。设置为 no，可以在 slot 没有全部分配的时候提供服务。
# 不建议打开该配置，这样会造成分区的时候，小分区的 master 一直在接受写请求，而造成很长时间数据不一致。
# cluster-require-full-coverage yes
```

## 8、集群的优缺点

### ①、有点

1. 实现扩容
2. 分摊压力
3. 无中心配置相对简单

### ②、缺点

1. 多键操作是不被支持的 
2. 多键的 Redis 事务是不被支持的。lua 脚本不被支持
3. 由于集群方案出现较晚，很多公司已经采用了其他的集群方案，而代理或者客户端分片的方案想要迁移至 redis cluster，需要整体迁移而不是逐步过渡，复杂度较大。

# 十二、Redis 应用问题解决

## 1、缓存穿透

### ①、问题描述

1. key 对应的数据在数据源并不存在，每次针对此 key 的请求从缓存获取不到，请求都会压到数据源，从而可能压垮数据源。
2. 比如用一个不存在的用户 id 获取用户信息，不论缓存还是数据库都没有，若黑客利用此漏洞进行攻击可能压垮数据库。

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726091955.png)

### ②、解决方案

一个一定不存在缓存及查询不到的数据，由于缓存是不命中时被动写的，并且出于容错考虑，如果从存储层查不到数据则不写入缓存，这将导致这个不存在的数据每次请求都要到存储层去查询，失去了缓存的意义。

- 解决方案：

1. 对空值缓存：如果一个查询返回的数据为空（不管是数据是否不存在），我们仍然把这个空结果（null）进行缓存，设置空结果的过期时间会很短，最长不超过五分钟
2. 设置可访问的名单（白名单）：使用 bitmaps 类型定义一个可以访问的名单，名单 id 作为 bitmaps 的偏移量，每次访问和bitmap里面的id进行比较，如果访问 id 不在 bitmaps 里面，进行拦截，不允许访问。
3. 采用布隆过滤器：(布隆过滤器（Bloom Filter）是 1970 年由布隆提出的。它实际上是一个很长的二进制向量（位图）和一系列随机映射函数（哈希函数）。
   1. 布隆过滤器可以用于检索一个元素是否在一个集合中。它的优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难。
   2. 将所有可能存在的数据哈希到一个足够大的 bitmaps 中，一个一定不存在的数据会被这个 bitmaps 拦截掉，从而避免了对底层存储系统的查询压力。
4. 进行实时监控：当发现 Redis 的命中率开始急速降低，需要排查访问对象和访问的数据，和运维人员配合，可以设置黑名单限制服务

## 2、缓存击穿

### ①、问题描述

key 对应的数据存在，但在 redis 中过期，此时若有大量并发请求过来，这些请求发现缓存过期一般都会从后端 DB 加载数据并回设到缓存，这个时候大并发的请求可能会瞬间把后端 DB 压垮。

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092015.png)

### ②、解决方案

key 可能会在某些时间点被超高并发地访问，是一种非常“热点”的数据。这个时候，需要考虑一个问题：缓存被“击穿”的问题。

- 解决问题：

1. 预先设置热门数据：在 redis 高峰访问之前，把一些热门数据提前存入到 redis 里面，加大这些热门数据 key 的时长
2. 实时调整：现场监控哪些数据热门，实时调整 key 的过期时长
3. 使用锁：
   1. 就是在缓存失效的时候（判断拿出来的值为空），不是立即去 load db。
   2. 先使用缓存工具的某些带成功操作返回值的操作（比如 Redis 的 SETNX）去 set 一个 mutex key
   3. 当操作返回成功时，再进行 load db 的操作，并回设缓存，最后删除 mutex key；
   4. 当操作返回失败，证明有线程在 load db，当前线程睡眠一段时间再重试整个 get 缓存的方法。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-57-934--3eyDwu3K2jaMnw.png)

## 3、缓存雪崩

### ①、问题描述

key 对应的数据存在，但在 redis 中过期，此时若有大量并发请求过来，这些请求发现缓存过期一般都会从后端 DB 加载数据并回设到缓存，这个时候大并发的请求可能会瞬间把后端 DB 压垮。
缓存雪崩与缓存击穿的区别在于这里针对很多 key 缓存，前者则是某一个 key

- 正常访问

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-053--DknH4Z0-ocxhTg.png)

- 缓存失效瞬间

![](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092035.png)

### ②、解决方案

缓存失效时的雪崩效应对底层系统的冲击非常可怕！

- 解决方案：

1. 构建多级缓存架构：nginx 缓存 + redis 缓存 + 其他缓存（ehcache 等）
2. 使用锁或队列：用加锁或者队列的方式来保证不会有大量的线程对数据库一次性进行读写，从而避免失效时大量的并发请求落到底层存储系统上。不适用高并发情况
3. 设置过期标志更新缓存：记录缓存数据是否过期（设置提前量），如果过期会触发通知另外的线程在后台去更新实际 key 的缓存。
4. 将缓存失效时间分散开：比如我们可以在原有的失效时间基础上增加一个随机值，比如 1-5 分钟随机，这样每一个缓存的过期时间的重复率就会降低，就很难引发集体失效的事件。

## 4、分布式锁

### ①、问题描述

随着业务发展的需要，原单体单机部署的系统被演化成分布式集群系统后，由于分布式系统多线程、多进程并且分布在不同机器上，这将使原单机部署情况下的并发控制锁策略失效，单纯的 Java API 并不能提供分布式锁的能力。为了解决这个问题就需要一种跨 JVM 的互斥机制来控制共享资源的访问，这就是分布式锁要解决的问题！分布式锁主流的实现方案：

1. 基于数据库实现分布式锁
2. 基于缓存（Redis 等）；性能：redis 最高
3. 基于 Zookeeper； 可靠性：zookeeper 最高

### ②、解决方案：使用 redis 实现分布式锁

- 使用 `setnx <key> <value>` 命令实现分布式锁，使用 `setex <key> <过期时间> <value>` 或者 `expire <key> <过期时间>` 设置过期时间
   - 为了避免使用 `setnx` 上完锁后，设备出问题不能使用 `setex` 命令设置过期时间，可以使用 `set` 命令
   - `set <key> <value> NX EX <过期时间>`：上锁的时同时设置过期时间
- 使用 `del <key>` 命令实现解锁
- 即：所有 redis 操作开始前都使用 `setnx` 设置一个指定名称的 key，设置成功即为加锁成功，设置失败即为加锁失败

| 命令                | 说明                                                                |
| ------------------- | ------------------------------------------------------------------- |
| `set <key> <value>` | 添加 key-value 键值对到数据库；若是 `set key1 100` 则会识别为数字值<br/><br/>![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-220--arZF0StkMgXC6g.png)<br/>1. `*EX`：key 的超时秒数；效果等同于 `SETEX key second value`<br/>2. `*PX`：key 的超时毫秒数，与 EX 互斥；效果等同于 `PSETEX key millisecond value`<br/>3. `*EXAT`：：设置 key 过期的指定 Unix 时间（以秒为单位）；<br/>4. `*PXAT`：设置 key 过期的指定 Unix 时间（以毫秒为单位）；<br/>5. `*NX`：当数据库中 key 不存在时，可以将 key-value 添加数据库<br/>6. `*XX`：当数据库中 key 存在时，可以将 key-value 添加数据库，与 NX 参数互斥<br/> |
| `setex <key> <过期时间> <value>` | 设置键值的同时，设置过期时间，单位秒。 |
| `setnx <key> <value>` | 只有在 key 不存在时，才设置 key 的值 |
| `del <key>` | 删除指定的 key |

- 使用 redis 实现分布式锁过程：

1. 多个客户端同时获取锁：使用 `set` 或 `setnx` 命令设置；设置成功即加锁成功，设置失败即加锁失败
2. 某一个客户端获取成功，执行业务逻辑：从 db 获取数据，放入缓存，执行完成释放锁 `del`
3. 其他客户端等待重试，重新获取锁

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-225--oSIYmG4Y4Jsr4Q.png)

### ③、优化：使用 UUID 防误删

> 场景：如果业务逻辑的执行时间是 7s。执行流程如下
> 1. 1 业务逻辑没执行完，3 秒后锁被自动释放。
> 2. 2 获取到锁，执行业务逻辑，3 秒后锁被自动释放。
> 3. 3 获取到锁，执行业务逻辑
> 4. 1 业务逻辑执行完成，开始调用 del 释放锁，这时释放的是 3 的锁，导致 3 的业务只执行 1s 就被别人释放。
> 5. 最终等于没锁的情况。

解决：setnx 获取锁时，设置一个指定的唯一值（例如：uuid）；释放前获取这个值，判断是否自己的锁

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-381--L8oU-EDEigs42g.png)

### ④、优化：LUA 脚本保证删除的原子性

> - 场景：
> 1. 1 执行删除时，查询到的 lock 值确实和 uuid 相等，接下来要进行删除操作
> 2. 1 执行删除前，lock 刚好过期时间已到，被 redis 自动释放，在redis中没有了 lock，没有了锁
> 3. 2 获取了 lock，开始执行方法
> 4. 1 执行删除，此时会把 2 的 lock 删除（因为第一步 1 查到了 lock 值和 uuid 相等）
> 5. 1 执行删除成功，删除了 2 的锁

#### Ⅰ、LUA 脚本

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-538--mHzQ1w065A6gsQ.png)


1. Lua 是一个小巧的脚本语言，Lua 脚本可以很容易的被 C/C++ 代码调用，也可以反过来调用 C/C++ 的函数，Lua 并没有提供强大的库，一个完整的 Lua 解释器不过 200k，所以 Lua 不适合作为开发独立应用程序的语言，而是作为嵌入式脚本语言。
2. 很多应用程序、游戏使用 LUA 作为自己的嵌入式脚本语言，以此来实现可配置性、可扩展性。
3. 这其中包括魔兽争霸地图、魔兽世界、博德之门、愤怒的小鸟等众多游戏插件或外挂。
4. [https://www.w3cschool.cn/lua/](https://www.w3cschool.cn/lua/)

#### Ⅱ、LUA 脚本在 Redis 中的优势

1. 将复杂的或者多步的 redis 操作，写为一个脚本，一次提交给 redis 执行，减少反复连接 redis 的次数。提升性能。
2. LUA 脚本是类似 redis 事务，有一定的原子性，不会被其他命令插队，可以完成一些 redis 事务性的操作。
3. 但是注意 redis 的 lua 脚本功能，只有在 Redis 2.6 以上的版本才可以使用。
4. redis 2.6 版本以后，通过 lua 脚本解决争抢问题，实际上是 redis 利用其单线程的特性，用任务队列的方式解决多任务并发问题。
5. Lua 脚本详解：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-674--DdOMh1--5PyQIQ.png)

#### Ⅲ、SptingBoot 中使用 LUA 脚本

```java
package com.yuehai.redis_springboot.contriller;

import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.script.DefaultRedisScript;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.thymeleaf.util.StringUtils;

import javax.annotation.Resource;
import java.util.Arrays;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

/**
 * @author 月海
 * @create 2023/2/9 12:34
 *
 * 分布式锁
 */

@Controller
@RequestMapping("/lock")
public class LockController {

    /**
     * 自动注入 RedisTemplate
     */
    @Resource
    private RedisTemplate redisTemplate;

    /**
     *
     */
    @ResponseBody
    @GetMapping("/testLockLua")
    public void testLockLua() {
        // 1、声明一个uuid ,将做为一个value 放入我们的key所对应的值中
        String uuid = UUID.randomUUID().toString();

        // 2、定义一个锁：lua 脚本可以使用同一把锁，来实现删除！
        // 访问 skuId 为 25 号的商品
        String skuId = "25";
        // 锁住的是所有 25 号商品的数据
        String locKey = "lock:" + skuId;

        // 3、获取锁
        Boolean lock = redisTemplate.opsForValue().setIfAbsent(locKey, uuid, 3, TimeUnit.SECONDS);

        // 第一种： lock 与过期时间中间不写任何的代码。
        // redisTemplate.expire("lock",10, TimeUnit.SECONDS);//设置过期时间

        // 如果 true，加锁成功
        if (lock) {
            // 执行的业务逻辑开始
            // 获取缓存中的 num 数据
            Object value = redisTemplate.opsForValue().get("num");

            // 如果是空直接返回
            if (StringUtils.isEmpty((String) value)) {
                return ;
            }

            // 不是空 如果说在这出现了异常！ 那么 delete 就删除失败！ 也就是说锁永远存在！
            int num = Integer.parseInt(value + "");
            // 使 num 每次 +1 放入缓存
            redisTemplate.opsForValue().set("num", String.valueOf(++num));

            /**
             * 使用 lua 脚本来锁
             */
            // 定义lua 脚本
            String script = "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end";
            // 使用 redis 执行 lua 执行
            DefaultRedisScript<Long> redisScript = new DefaultRedisScript<>();
            redisScript.setScriptText(script);
            /**
             * 设置一下返回值类型为 Long
             * 因为删除判断的时候，返回的0,给其封装为数据类型。如果不封装那么默认返回String 类型，
             * 那么返回字符串与0 会有发生错误。
             */
            redisScript.setResultType(Long.class);
            // 第一个要是 script 脚本 ，第二个需要判断的 key，第三个就是 key 所对应的值。
            redisTemplate.execute(redisScript, Arrays.asList(locKey), uuid);
        } else {
            // 其他线程等待
            try {
                // 睡眠
                Thread.sleep(1000);
                // 睡醒了之后，调用方法。
                testLockLua();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}

```

### ⑤、总结

1. 加锁

```java
// 1. 从 redis 中获取锁，set k1 v1 px 20000 nx
String uuid = UUID.randomUUID().toString();
Boolean lock = this.redisTemplate.opsForValue().setIfAbsent("lock", uuid, 2, TimeUnit.SECONDS);
```

2. 解锁

```java
String script = "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end";
// 设置 lua 脚本返回的数据类型
DefaultRedisScript<Long> redisScript = new DefaultRedisScript<>();
// 设置 lua 脚本返回类型为 Long
redisScript.setResultType(Long.class);
redisScript.setScriptText(script);
redisTemplate.execute(redisScript, Arrays.asList("lock"),uuid);

```

3. 重试

```java
Thread.sleep(500);
// 重新执行该方法
testLock();
```

4. 为了确保分布式锁可用，我们至少要确保锁的实现同时满足以下四个条件：
   1. 互斥性。在任意时刻，只有一个客户端能持有锁。
   2. 不会发生死锁。即使有一个客户端在持有锁的期间崩溃而没有主动解锁，也能保证后续其他客户端能加锁。
   3. 解铃还须系铃人。加锁和解锁必须是同一个客户端，客户端自己不能把别人加的锁给解了。
   4. 加锁和解锁必须具有原子性。

# 十三、Redis6.0 新功能

## 1、ACL

### ①、简介

> 参考官网：[https://redis.io/topics/acl](https://redis.io/topics/acl)

1. Redis ACL 是 Access Control List（访问控制列表）的缩写，该功能允许根据可以执行的命令和可以访问的键来限制某些连接。
2. 在 Redis 5 版本之前，Redis 安全规则只有密码控制，还有通过 rename 来调整高危命令比如 flushdb、KEYS*、shutdown 等。
3. Redis 6 则提供 ACL 的功能对用户进行更细粒度的权限控制 ：
   1. 接入权限：用户名和密码 
   2. 可以执行的命令 
   3. 可以操作的 KEY

### ②、命令

#### Ⅰ、`acl list` 展现用户权限列表

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-58-891--rzWllFM5mLrArw.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-012--_MM3TuIKsv73ug.png)

#### Ⅱ、`acl cat` 查看添加权限指令类别

1. 查看添加权限指令类别

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-111--RSDCi89gyKrRTw.png)

2. 加参数类型名可以查看类型下具体命令

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-214--fAryg548zf2MiQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-330--DsvRrFNOQDi8gw.png)

#### Ⅲ、`acl whoami` 命令查看当前用户

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-416--5yWEeCkMX2fxRA.png)

#### Ⅳ、`acl setuser` 命令创建和编辑用户 ACL

1. ACL 规则：下面是有效 ACL 规则的列表。某些规则只是用于激活或删除标志，或对用户 ACL 执行给定更改的单个单词。其他规则是字符前缀，它们与命令或类别名称、键模式等连接在一起。

| ACL规则 |  |  |
| --- | --- | --- |
| 类型 | 参数 | 说明 |
| 启动和禁用用户 | on | 激活某用户账号 |
|  | off | 禁用某用户账号。<br/>注意，已验证的连接仍然可以工作。<br/>如果默认用户被标记为 off，则新连接将在未进行身份验证的情况下启动，并要求用户使用 AUTH 选项发送 AUTH 或 HELLO，以便以某种方式进行身份验证。 |
| 权限的添加删除 | +<command> | 将指令添加到用户可以调用的指令列表中 |
|  | -<command> | 从用户可执行指令列表移除指令 |
|  | `+@<category>` | 添加该类别中用户要调用的所有指令，有效类别为@admin、@set、@sortedset…等，通过调用ACL CAT命令查看完整列表。<br/>特殊类别 @all 表示所有命令，包括当前存在于服务器中的命令，以及将来将通过模块加载的命令。 |
| | `-@<actegory>` | 从用户可调用指令中移除类别 |
| | allcommands | +@all 的别名 |
| | nocommand | -@all 的别名 |
| | 可操作键的添加或删除 | `~<pattern>` | 添加可作为用户可操作的键的模式。例如 ~* 允许所有的键 |

2. 通过命令创建新用户默认权限：`acl setuser yuehai`
   1. 本次没有指定任何规则。如果用户不存在，这将使用 just created 的默认属性来创建用户。
   2. 如果用户已经存在，则这个命令将不执行任何操作。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-683--WH44fsl7L_Kqzg.png)

3. 设置用户名、密码、ACL 权限、并启用用户：`acl setuser yan on >123456 ~cached:* +get`
   1. 参数 1 ：用户名
   2. 参数 2 ：启用该用户
   3. 参数 3 ：设置 123456 为密码
   4. 参数 4 ：可操作的键为：`cached:*`
   5. 参数 5 ：添加 get 指令到该用户可调用的指令中

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-780--mnGIAXNJ1nz0BQ.png)

4. 切换用户：`auth 用户名 密码`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--22-59-913--k-gT6DigMjLXJQ.png)

5. 验证权限

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-032--jNdyu1kPiTq_Pw.png)

## 2、IO 多线程

### ①、简介

1. Redis6 终于支撑多线程了，告别单线程了吗？
2. IO 多线程其实指客户端交互部分的网络 IO 交互处理模块多线程，而非执行命令多线程。
3. Redis6 执行命令依然是单线程。

### ②、原理架构

1. Redis 6 加入多线程，但跟 Memcached 这种从 IO 处理到数据访问多线程的实现模式有些差异。
2. Redis 的多线程部分只是用来处理网络数据的读写和协议解析，执行命令仍然是单线程。之所以这么设计是不想因为多线程而变得复杂，需要去控制 key、lua、事务，LPUSH/LPOP 等等的并发问题。
3. 整体的设计大体如下：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-130--Nx8qyahH2uDdJQ.png)

### ③、开启 IO 多线程

多线程 IO 默认也是不开启的，需要在配置文件中配置：

```java
io-threads-do-reads  yes 
io-threads 4
```

## 3、工具支持 Cluster

1. 之前老版 Redis 想要搭集群需要单独安装 ruby 环境，Redis 5 将 redis-trib.rb 的功能集成到 `redis-cli`
2. 另外官方 redis-benchmark 工具开始支持 cluster 模式了，通过多线程的方式对多个分片进行压测。

```bash
root@f31a8d0a5c1a:/data# redis-benchmark --help
Usage: redis-benchmark [-h <host>] [-p <port>] [-c <clients>] [-n <requests>] [-k <boolean>]

 -h <hostname>      Server hostname (default 127.0.0.1)
 -p <port>          Server port (default 6379)
 -s <socket>        Server socket (overrides host and port)
 -a <password>      Password for Redis Auth
 --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
 -c <clients>       Number of parallel connections (default 50)
 -n <requests>      Total number of requests (default 100000)
 -d <size>          Data size of SET/GET value in bytes (default 3)
 --dbnum <db>       SELECT the specified db number (default 0)
 --threads <num>    Enable multi-thread mode.
 --cluster          Enable cluster mode.
 --enable-tracking  Send CLIENT TRACKING on before starting benchmark.
 -k <boolean>       1=keep alive 0=reconnect (default 1)
 -r <keyspacelen>   Use random keys for SET/GET/INCR, random values for SADD,
                    random members and scores for ZADD.
  Using this option the benchmark will expand the string __rand_int__
  inside an argument with a 12 digits number in the specified range
  from 0 to keyspacelen-1. The substitution changes every time a command
  is executed. Default tests use this to hit random keys in the
  specified range.
 -P <numreq>        Pipeline <numreq> requests. Default 1 (no pipeline).
 -e                 If server replies with errors, show them on stdout.
                    (no more than 1 error per second is displayed)
 -q                 Quiet. Just show query/sec values
 --precision        Number of decimal places to display in latency output (default 0)
 --csv              Output in CSV format
 -l                 Loop. Run the tests forever
 -t <tests>         Only run the comma separated list of tests. The test
                    names are the same as the ones produced as output.
 -I                 Idle mode. Just open N idle connections and wait.
 --tls              Establish a secure TLS connection.
 --sni <host>       Server name indication for TLS.
 --cacert <file>    CA Certificate file to verify with.
 --cacertdir <dir>  Directory where trusted CA certificates are stored.
                    If neither cacert nor cacertdir are specified, the default
                    system-wide trusted root certs configuration will apply.
 --insecure         Allow insecure TLS connection by skipping cert validation.
 --cert <file>      Client certificate to authenticate with.
 --key <file>       Private key file to authenticate with.
 --tls-ciphers <list> Sets the list of prefered ciphers (TLSv1.2 and below)
                    in order of preference from highest to lowest separated by colon (":").
                    See the ciphers(1ssl) manpage for more information about the syntax of this string.
 --tls-ciphersuites <list> Sets the list of prefered ciphersuites (TLSv1.3)
                    in order of preference from highest to lowest separated by colon (":").
                    See the ciphers(1ssl) manpage for more information about the syntax of this string,
                    and specifically for TLSv1.3 ciphersuites.
 --help             Output this help and exit.
 --version          Output version and exit.

Examples:

 Run the benchmark with the default configuration against 127.0.0.1:6379:
   $ redis-benchmark

 Use 20 parallel clients, for a total of 100k requests, against 192.168.1.1:
   $ redis-benchmark -h 192.168.1.1 -p 6379 -n 100000 -c 20

 Fill 127.0.0.1:6379 with about 1 million keys only using the SET test:
   $ redis-benchmark -t set -n 1000000 -r 100000000

 Benchmark 127.0.0.1:6379 for a few commands producing CSV output:
   $ redis-benchmark -t ping,set,get -n 100000 --csv

 Benchmark a specific command line:
   $ redis-benchmark -r 10000 -n 10000 eval 'return redis.call("ping")' 0

 Fill a list with 10000 random elements:
   $ redis-benchmark -r 10000 -n 10000 lpush mylist __rand_int__

 On user specified command lines __rand_int__ is replaced with a random integer
 with a range of values selected by the -r option.

root@f31a8d0a5c1a:/data# 
```

## 4、Redis 新功能持续关注

Redis6新功能还有：

1. RESP3 新的 Redis 通信协议：优化服务端与客户端之间通信
2. Client side caching 客户端缓存：基于 RESP3 协议实现的客户端缓存功能。为了进一步提升缓存的性能，将客户端经常访问的数据 cache 到客户端。减少 TCP 网络交互。
3. Proxy 集群代理模式：Proxy 功能，让 Cluster 拥有像单实例一样的接入方式，降低大家使用 cluster 的门槛。不过需要注意的是代理不改变 Cluster 的功能限制，不支持的命令还是不会支持，比如跨 slot 的多 Key 操作。
4. Modules API：Redis 6 中模块 API 开发进展非常大，因为 Redis Labs 为了开发复杂的功能，从一开始就用上 Redis 模块。Redis 可以变成一个框架，利用 Modules 来构建不同系统，而不需要从头开始写然后还要 BSD 许可。Redi s一开始就是一个向编写各种系统开放的平台。

# 十四、Redis 与 Spring Boot 整合

## 1、创建项目，引入依赖

### ①、引入基本依赖

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-275--2JlXm9iI6Xk1pA.png)

### ②、引入 `commons-pool2` 连接池

1. SpringBoot 2.0 默认采用 Lettuce 客户端来连接 Redis 服务
2. 默认是不使用连接池的，只有配置 redis.lettuce.pool 下的属性的时候才可以使用到 redis 连接池
3. 采用 Lettuce 使用连接池，要依赖 commons-pool2
```xml
<!-- redis 连接池 commons-pool -->
<dependency>
		<groupId>org.apache.commons</groupId>
		<artifactId>commons-pool2</artifactId>
</dependency>
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.11</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.yuehai</groupId>
    <artifactId>redis_SpringBoot_02</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>04_redis_SpringBoot_02</name>
    <description>04_redis_SpringBoot_02</description>
    
    <properties>
        <java.version>1.8</java.version>
    </properties>
    
    <dependencies>
        <!-- redis -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <!-- web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- fastjson -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.72</version>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

### ③、项目结构

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-393--ybBH_K9hAtwuWg.png)

## 2、修改配置文件

> 本次依然使用单机

### ①、单机

```yaml
server:
    port: 9000

spring:
    # Redis 配置
    redis:
        # Redis 配置服务器地址
        host: 43.138.106.181
        # Redis 服务器连接端口
        port: 3306
        # Redis 数据库索引（默认为 0）
        database: 0
        # Redis 密码
        password: "000123"
        # 连接超时时间（毫秒）
        timeout: 1800000
        lettuce:
            pool:
                # 连接池最大连接数（使用负值表示没有限制）
                max-active: 20
                # 最大阻塞等待时间(负数表示没限制)
                max-wait: -1
                # 连接池中的最大空闲连接
                max-idle: 5
                # 连接池中的最小空闲连接
                min-idle: 0
```

### ②、集群

- 增加了集群的 ip 配置

```yaml
server:
    port: 9000

spring:
    # Redis 配置
    redis:
        # Redis 配置服务器地址
        host: 43.138.106.181
        # Redis 服务器连接端口
        port: 3306
        # Redis 密码
        password: "000123"
        # 连接超时时间（毫秒）
        timeout: 1800000
        # redis 集群的 ip 配置
        cluster:
            nodes: 192.168.1.26:7001,192.168.1.26:7002,192.168.1.26:7003,192.168.1.26:7004,192.168.1.26:7005,192.168.1.26:7006
        # 连接池配置
        lettuce:
            pool:
                # 连接池最大连接数（使用负值表示没有限制）
                max-active: 20
                # 最大阻塞等待时间(负数表示没限制)
                max-wait: -1
                # 连接池中的最大空闲连接
                max-idle: 5
                # 连接池中的最小空闲连接
                min-idle: 0
```

## 3、编写配置类

编写 redis 配置类，设置了常用的 RedisTemplate 规则、CacheManager 缓存规则

```java
package com.yuehai.redis_springboot_02.config;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.interceptor.KeyGenerator;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.RedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.lang.reflect.Method;
import java.time.Duration;

@Configuration
@EnableCaching
public class RedisConfig {

    /**
     * 用于生成缓存对象的唯一标识 key
     */
    @Bean
    public KeyGenerator keyGenerator() {
        return new KeyGenerator() {
            @Override
            public Object generate(Object target, Method method, Object... params) {
                StringBuilder sb = new StringBuilder();
                sb.append(target.getClass().getName());
                sb.append(method.getName());
                for (Object obj : params) {
                    sb.append(obj.toString());
                }
                return sb.toString();
            }
        };
    }

    /**
     * 设置 RedisTemplate 规则
     */
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
        // 我们为了自己开发方便，一般直接使用 <String, Object>
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory);

        /*
          Json 序列化配置
         */
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);
        // 解决查询缓存转换异常的问题
        ObjectMapper om = new ObjectMapper();
        // 指定要序列化的域，field、get 和 set，以及修饰符范围，ANY 是都有包括 private 和 public
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        // 指定序列化输入的类型，类必须是非 final 修饰的，final 修饰的类，比如 String,Integer 等会跑出异常
        om.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(om);

        /*
          序列化 key value
         */
        // key 采用 String 的序列化方式
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        // value 序列化方式采用 jackson
        redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);

        // hash 的 key 也采用 String 的序列化方式
        redisTemplate.setHashKeySerializer(new StringRedisSerializer());
        // hash 的 value 序列化方式采用 jackson
        redisTemplate.setHashValueSerializer(jackson2JsonRedisSerializer);

        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }

    /**
     * 设置 CacheManager 缓存规则
     * @param factory
     * @return
     */
    @Bean
    public CacheManager cacheManager(RedisConnectionFactory factory) {
        // 创建序列化对象
        RedisSerializer<String> redisSerializer = new StringRedisSerializer();
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);

        // 解决查询缓存转换异常的问题
        ObjectMapper om = new ObjectMapper();
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        om.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(om);

        // 配置序列化（解决乱码的问题）,过期时间 600 秒
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
                // 设置缓存管理器管理的缓存的默认过期时间
                .entryTtl(Duration.ofSeconds(600))
                // 设置 key 为 string 序列化
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(redisSerializer))
                // 设置 value 为 json 序列化
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(jackson2JsonRedisSerializer))
                // 不缓存空值
                .disableCachingNullValues();

        RedisCacheManager cacheManager = RedisCacheManager.builder(factory)
                .cacheDefaults(config)
                .build();
        return cacheManager;
    }
}
```

## 4、RedisTemplate 介绍

1. spring 封装了 RedisTemplate 对象来进行对 redis 的各种操作，它支持所有的 redis 原生的 api
2. 模板中的 Redis key 的类型（通常为String）如：`RedisTemplate<String, Object>`；注意：如果没特殊情况，切勿定义成 `RedisTemplate<Object, Object>`，否则根据里氏替换原则，使用的时候会造成类型错误 。
3. RedisTemplate 中定义了对 5 种数据结构操作：

```java
// 操作字符串
redisTemplate.opsForValue();

// 操作 hash
redisTemplate.opsForHash();

// 操作 list
redisTemplate.opsForList();

// 操作 set
redisTemplate.opsForSet();

// 操作有序 set（zset）
redisTemplate.opsForZSet();
```

4. `StringRedisTemplate` 与 `RedisTemplate` 的区别：
   1. 两者的关系是 `StringRedisTemplate` 继承 `RedisTemplate`
   2. 两者的数据是不共通的；也就是说 `StringRedisTemplate` 只能管理 `StringRedisTemplate` 里面的数据；`RedisTemplate` 只能管 `RedisTemplate` 中的数据。
   3. SDR 默认采用的序列化策略有两种，一种是 String 的序列化策略，一种是 JDK 的序列化策略。
   4. `StringRedisTemplate` 默认采用的是 String 的序列化策略，保存的 key 和 value 都是采用此策略序列化保存的。
   5. `RedisTemplate` 默认采用的是 JDK 的序列化策略，保存的 key 和 value 都是采用此策略序列化保存的。

## 5、小例子

> spring 封装了 RedisTemplate 对象来进行对 redis 的各种操作，它支持所有的 redis 原生的 api

```java
package com.yuehai.redis_springboot_02.controller;

import com.yuehai.redis_springboot_02.bean.User;
import com.yuehai.redis_springboot_02.utils.JsonResult;
import org.springframework.data.redis.connection.DataType;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.Map;
import java.util.Set;

/**
 * @author 月海
 * @create 2023/2/9 16:15
 */

@RestController
public class TestController {

    /**
     * 自动注入 RedisTemplate
     */
    @Resource
    private RedisTemplate<String, Object> redisTemplate;
    @Resource
    private StringRedisTemplate stringRedisTemplate;

    /**
     * 对 key 的操作
     * http://172.20.2.88:9000/testKey
     */
    @GetMapping("/testKey")
    public JsonResult testKey(){

        /**
         * 命令	说明
         * set <key> <value>	添加 key-value 键值对到数据库
         * get <key>	        根据 key 获取 value
         * keys *	            查看当前库所有key（查看指定库：keys *1）
         * exists <key>	        判断某个 key 是否存在
         * type <key>	        查看你的 key 是什么类型
         * del <key>	        删除指定的 key
         * unlink <key>	        根据value选择非阻塞删除；仅将 keys 从 keyspace 元数据中删除，真正的删除会在后续异步操作。
         * expire <key> <10>	10秒钟：为给定的key设置过期时间
         * ttl <key> 	        查看还有多少秒过期，-1表示永不过期，-2表示已过期
         * select <库编号>	    命令切换数据库（0-15）
         * dbsize	            查看当前数据库的key的数量
         * flushdb	            清空当前库
         * flushall	            通杀（清空）全部库
         */

        // 循环添加
        for (int i = 0; i < 1000; i++) {
            // 定义数据 key
            String key = "key:" + i;
            // 定义数据 value
            String value = String.valueOf(i);

            // set <key> <value>	添加 key-value 键值对到数据库
            stringRedisTemplate.opsForValue().set(key, value);
        }

        // keys *	            查看当前库所有key（查看指定库：keys *1）
        Set<String> keys = stringRedisTemplate.keys("*");

        // exists <key>	        判断某个 key 是否存在
        Boolean hasKey = stringRedisTemplate.hasKey("key:999");

        // type <key>	        查看你的 key 是什么类型
        DataType type = stringRedisTemplate.type("key:999");

        // del <key>	        删除指定的 key
        // unlink <key>	        根据value选择非阻塞删除；仅将 keys 从 keyspace 元数据中删除，真正的删除会在后续异步操作。
        // expire <key> <10>	10秒钟：为给定的key设置过期时间
        // ttl <key> 	        查看还有多少秒过期，-1表示永不过期，-2表示已过期
        // select <库编号>	    命令切换数据库（0-15）
        // dbsize	            查看当前数据库的key的数量
        // flushdb	            清空当前库
        // flushall	            通杀（清空）全部库

        return JsonResult.success(keys)
                .put("key:999 是否存在：", hasKey)
                .put("key:999 是什么类型", type);
    }

    /**
     * 对 hash 的操作
     * http://172.20.2.88:9000/testHash
     */
    @GetMapping("/testHash")
    public JsonResult testHash(){

        /**
         * HSET key field value [field value]   将哈希表 key 中的字段 field 的值设为 value 。
         * HSETNX key field value	            只有在键 field 不存在时，设置哈希表字段的值。
         * HGET key field	                    获取存储在哈希表中指定字段的值。
         * HLEN key	                            获取指定哈希表中字段的数量
         * HKEYS key	                        获取指定哈希表中所有 field
         * HGETALL key	                        获取哈希表中指定 key 的所有字段和值
         * HVALS key	                        获取哈希表中所有值。
         * HMGET key field1 [field2]	        获取所有给定字段的值
         * HEXISTS key field	                查看哈希表 key 中，指定的字段是否存在。
         * HINCRBY key field increment	        为哈希表 key 中的指定字段的整数值加上增量 increment 。
         * HINCRBYFLOAT key field increment	为   哈希表 key 中的指定字段的浮点数值加上增量 increment 。
         * HDEL key field1 [field2]	             删除一个或多个哈希表字段
         * HSCAN key cursor [MATCH pattern] [COUNT count]	迭代哈希表中的键值对。
         */

        // HSET key field value [field value]   将哈希表 key 中的字段 field 的值设为 value 。
        redisTemplate.opsForHash().put("HashKey:1", "user", new User("月海", 16));
        redisTemplate.opsForHash().put("HashKey:1", "user2", new User("月海", 16));

        // HGET key field	                    获取存储在哈希表中指定字段的值。
        User user = (User) redisTemplate.opsForHash().get("HashKey:1", "user");

        // HGETALL key	                        获取哈希表中指定 key 的所有字段和值
        Map<Object, Object> entries = redisTemplate.opsForHash().entries("HashKey:1");

        return JsonResult.success("OK")
                .put("获取存储在哈希表中指定字段的值：", user)
                .put("获取哈希表中指定 key 的所有字段和值：", entries);
    }


}
```

### ①、对 key 的操作

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-503--kT4jGT8MdfAWzA.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-598--Tq9nXDEsXf7SRA.png)

### ②、对 hash 的操作

```java
package com.yuehai.redis_springboot_02.bean;

import lombok.*;

/**
 * @author 月海
 * @create 2023/2/10 8:31
 */

// lombok，编译时可生成 无参构造器 方法
@NoArgsConstructor
// lombok，编译时可生成 有参构造器（有所有参数） 方法
@AllArgsConstructor
// lombok，编译时可生成 get/set 方法
@Data
// lombok，编译时可生成 toString 方法
@ToString
// lombok，编译时可生成 重写HashCode 方法
@EqualsAndHashCode
public class User {
    // 姓名
    private String name;
    // 年龄
    private Integer age;
}

```
```java
/**
 * 对 hash 的操作
 * http://172.20.2.88:9000/testHash
 */
@GetMapping("/testHash")
public JsonResult testHash(){

	/**
	 * HSET key field value [field value]   将哈希表 key 中的字段 field 的值设为 value 。
	 * HSETNX key field value	            只有在键 field 不存在时，设置哈希表字段的值。
	 * HGET key field	                    获取存储在哈希表中指定字段的值。
	 * HLEN key	                            获取指定哈希表中字段的数量
	 * HKEYS key	                        获取指定哈希表中所有 field
	 * HGETALL key	                        获取哈希表中指定 key 的所有字段和值
	 * HVALS key	                        获取哈希表中所有值。
	 * HMGET key field1 [field2]	        获取所有给定字段的值
	 * HEXISTS key field	                查看哈希表 key 中，指定的字段是否存在。
	 * HINCRBY key field increment	        为哈希表 key 中的指定字段的整数值加上增量 increment 。
	 * HINCRBYFLOAT key field increment	为   哈希表 key 中的指定字段的浮点数值加上增量 increment 。
	 * HDEL key field1 [field2]	             删除一个或多个哈希表字段
	 * HSCAN key cursor [MATCH pattern] [COUNT count]	迭代哈希表中的键值对。
	 */

	// HSET key field value [field value]   将哈希表 key 中的字段 field 的值设为 value 。
	redisTemplate.opsForHash().put("HashKey:1", "user", new User("月海", 16));
	redisTemplate.opsForHash().put("HashKey:1", "user2", new User("月海", 16));

	// HGET key field	                    获取存储在哈希表中指定字段的值。
	User user = (User) redisTemplate.opsForHash().get("HashKey:1", "user");

	// HGETALL key	                        获取哈希表中指定 key 的所有字段和值
	Map<Object, Object> entries = redisTemplate.opsForHash().entries("HashKey:1");

	return JsonResult.success("OK")
			.put("获取存储在哈希表中指定字段的值：", user)
			.put("获取哈希表中指定 key 的所有字段和值：", entries);
}
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-705--FIXha4i1aoUsKg.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F2023-07-25-13--23-00-838--CRRg6B-bTN0l5w.png)

























