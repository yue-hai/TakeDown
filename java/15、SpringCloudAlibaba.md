# 一、SpringCloud Alibaba 入门简介

> 官网：https://spring.io/projects/spring-cloud-alibaba#overview
> 
> 英文：https://github.com/alibaba/spring-cloud-alibaba
> 
> https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html
> 
> 中文：https://github.com/alibaba/spring-cloud-alibaba/blob/master/README-zh.md
> 
> 版本对应说明：https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E
> 
> [Spring Cloud Alibaba.xmind](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FSpring%20Cloud%20Alibaba.xmind)
> 
> ![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230323101342.png)

## 1、为什么会出现 SpringCloud Alibaba
<font color="#c00000">Spring Cloud Netflix 项目进入维护模式</font>

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301095557.png)

1.  什么是维护模式：将模块置于维护模式，意味着 Spring Cloud 团队将不会再向模块添加新功能。我们将修复 block 级别的 bug 以及安全问题，我们也会考虑并审查社区的小型 pull request。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301095456.png)

2.  进入维护模式意味着什么呢：
	1.  Spring Cloud Netflix 将不再开发新的组件：我们都知道 Spring Cloud 版本迭代算是比较快的，因而出现了很多重大 ISSUE 都还来不及 Fix 就又推另一个 Release 了。进入维护模式意思就是目前一直以后一段时间 Spring Cloud Netflix 提供的服务和功能就这么多了，不在开发新的组件和功能了。以后将以维护和 Merge分支Full Request为主
	2.  新组件功能将以其他替代平代替的方式实现

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301095846.png)

## 2、SpringCloud alibaba 带来了什么
### ①、是什么

-   诞生：2018.10.31，Spring Cloud Alibaba 正式入驻了 Spring Cloud 官方孵化器，并在 Maven 中央库发布了第一个版本。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301100546.png)

### ②、能干嘛
1.  服务限流降级：默认支持 Servlet、Feign、RestTemplate、Dubbo 和 RocketMQ 限流降级功能的接入，可以在运行时通过控制台实时修改限流降级规则，还支持查看限流降级 Metrics 监控。
2.  服务注册与发现：适配 Spring Cloud 服务注册与发现标准，默认集成了 Ribbon 的支持。
3.  分布式配置管理：支持分布式系统中的外部化配置，配置更改时自动刷新。
4.  消息驱动能力：基于 Spring Cloud Stream 为微服务应用构建消息驱动能力。
5.  阿里云对象存储：阿里云提供的海量、安全、低成本、高可靠的云存储服务。支持在任何应用、任何时间、任何地点存储和访问任意类型的数据。
6.  分布式任务调度：提供秒级、精准、高可靠、高可用的定时（基于 Cron 表达式）任务调度服务。同时提供分布式的任务执行模型，如网格任务。网格任务支持海量子任务均匀分配到所有 Worker（schedulerx-client）上执行。
### ③、怎么用

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301100615.png)

### ④、组件版本对应关系

1. Spring Cloud Alibaba、Spring Cloud、Spring Boot 版本对应关系：由于 Spring Boot 3.0，Spring Boot 2.7~2.4 和 2.4 以下版本之间变化较大，目前企业级客户老项目相关 Spring Boot 版本仍停留在 Spring Boot 2.4 以下，为了同时满足存量用户和新用户不同需求，社区以 Spring Boot 3.0 和 2.4 分别为分界线，同时维护 2022.x、2021.x、2.2.x 三个分支迭代。如果不想跨分支升级，如需使用新特性，请升级为对应分支的新版本。 为了规避相关构建过程中的依赖冲突问题，我们建议可以通过 [云原生应用脚手架](https://start.aliyun.com/) 进行项目创建

- 2022.x 分支：适配 Spring Boot 3.0，Spring Cloud 2022.x 版本及以上的 Spring Cloud Alibaba 版本按从新到旧排列如下表（最新版本用*标记）： (注意，该分支 Spring Cloud Alibaba 版本命名方式进行了调整，未来将对应 Spring Cloud 版本，前三位为 Spring Cloud 版本，最后一位为扩展版本，比如适配 Spring Cloud 2022.0.0 版本对应的 Spring Cloud Alibaba 第一个版本为：2022.0.0.0，第个二版本为：2022.0.0.1，依此类推)

| Spring Cloud Alibaba Version | Spring Cloud Version  | Spring Boot Version |
| ---------------------------- | --------------------- | ------------------- |
| 2022.0.0.0-RC*               | Spring Cloud 2022.0.0 | 3.0.0                    |

- 2021.x 分支：适配 Spring Boot 2.4，Spring Cloud 2021.x 版本及以上的 Spring Cloud Alibaba 版本按从新到旧排列如下表（最新版本用*标记）：

| Spring Cloud Alibaba Version | Spring Cloud Version  | pring Boot Version |
| ---------------------------- | --------------------- | ------------------ |
| 2021.0.4.0*                  | Spring Cloud 2021.0.4 | 2.6.11             |
| 2021.0.1.0                   | Spring Cloud 2021.0.1 | 2.6.3              |
| 2021.1                       | Spring Cloud 2020.0.1 | 2.4.2              |

- 2021.x 分支：适配 Spring Boot 为 2.4，Spring Cloud Hoxton 版本及以下的 Spring Cloud Alibaba 版本按从新到旧排列如下表（最新版本用*标记）：

| Spring Cloud Alibaba Version      | Spring Cloud Version        | Spring Boot Version |
| --------------------------------- | --------------------------- | ------------------- |
| 2.2.10-RC1*                       | Spring Cloud Hoxton.SR12    | 2.3.12.RELEASE      |
| 2.2.9.RELEASE                     | Spring Cloud Hoxton.SR12    | 2.3.12.RELEASE      |
| 2.2.8.RELEASE                     | Spring Cloud Hoxton.SR12    | 2.3.12.RELEASE      |
| 2.2.7.RELEASE                     | Spring Cloud Hoxton.SR12    | 2.3.12.RELEASE      |
| 2.2.6.RELEASE                     | Spring Cloud Hoxton.SR9     | 2.3.2.RELEASE       |
| 2.2.1.RELEASE                     | Spring Cloud Hoxton.SR3     | 2.2.5.RELEASE       |
| 2.2.0.RELEASE                     | Spring Cloud Hoxton.RELEASE | 2.2.X.RELEASE       |
| 2.1.4.RELEASE                     | Spring Cloud Greenwich.SR6  | 2.1.13.RELEASE      |
| 2.1.2.RELEASE                     | Spring Cloud Greenwich      | 2.1.X.RELEASE       |
| 2.0.4.RELEASE(停止维护，建议升级) | Spring Cloud Finchley       | 2.0.X.RELEASE       |
| 1.5.1.RELEASE(停止维护，建议升级) | Spring Cloud Edgware        | 1.5.X.RELEASE       |

2. Spring Cloud Alibaba 各组件对应关系：每个 Spring Cloud Alibaba 版本及其自身所适配的各组件对应版本如下表所示（注意，Spring Cloud Dubbo 从 2021.0.1.0 起已被移除出主干，不再随主干演进）：

| Spring Cloud Alibaba Version                              | Sentinel Version | Nacos Version | RocketMQ Version | Dubbo Version | Seata Version |
| --------------------------------------------------------- | ---------------- | ------------- | ---------------- | ------------- | ------------- |
| 2.2.10-RC1                                                | 1.8.6            | 2.2.0         | 4.9.4            | ~             | 1.6.1         |
| 2022.0.0.0-RC1                                            | 1.8.6            | 2.2.1-RC      | 4.9.4            | ~             | 1.6.1         |
| 2.2.9.RELEASE                                             | 1.8.5            | 2.1.0         | 4.9.4            | ~             | 1.5.2         |
| 2021.0.4.0                                                | 1.8.5            | 2.0.4         | 4.9.4            | ~             | 1.5.2         |
| 2.2.8.RELEASE                                             | 1.8.4            | 2.1.0         | 4.9.3            | ~             | 1.5.1         |
| 2021.0.1.0                                                | 1.8.3            | 1.4.2         | 4.9.2            | ~             | 1.4.2         |
| 2.2.7.RELEASE                                             | 1.8.1            | 2.0.3         | 4.6.1            | 2.7.13        | 1.3.0         |
| 2.2.6.RELEASE                                             | 1.8.1            | 1.4.2         | 4.4.0            | 2.7.8         | 1.3.0         |
| 2021.1 or <br>2.2.5.RELEASE or <br>2.1.4.RELEASE or <br>2.0.4.RELEASE | 1.8.0            | 1.4.1         | 4.4.0            | 2.7.8         | 1.3.0         |
| 2.2.3.RELEASE or <br>2.1.3.RELEASE or <br>2.0.3.RELEASE   | 1.8.0            | 1.3.3         | 4.4.0            | 2.7.8         | 1.3.0         |
| 2.2.1.RELEASE or <br>2.1.2.RELEASE or <br>2.0.2.RELEASE   | 1.7.1            | 1.2.1         | 4.4.0            | 2.7.6         | 1.2.0         |
| 2.2.0.RELEASE                                             | 1.7.1            | 1.1.4         | 4.4.0            | 2.7.4.1       | 1.0.0         |
| 2.1.1.RELEASE or <br>2.0.1.RELEASE or <br>1.5.1.RELEASE   | 1.7.0            | 1.1.4         | 4.4.0            | 2.7.3         | 0.9.0         |
| 2.1.0.RELEASE or <br>2.0.0.RELEASE or <br>1.5.0.RELEASE   | 1.6.3            | 1.1.1         | 4.4.0            | 2.7.3         | 0.7.1         |

# 二、Nacos 服务注册和配置中心
> github：https://github.com/alibaba/Nacos
> 
> 官网文档：https://nacos.io/zh-cn/index.html
> 
> https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_nacos_discovery

## 1、Nacos 简介

### ①、为什么叫 Nacos

前四个字母分别为 Naming 和 Configuration 的前两个字母，最后的 s 为 Service。

### ②、是什么

1.  一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。
2.  Nacos：Dynamic Naming and Configuration Service
3.  Nacos 就是注册中心 + 配置中心的组合
4.  等价于：Nacos = Eureka + Config + Bus

### ③、能干嘛

1.  替代 Eureka 做服务注册中心
2.  替代 Config 做服务配置中心

### ④、各种注册中心比较

据说 Nacos 在阿里巴巴内部有超过 10 万的实例运行，已经过了类似双十一等各种大型流量的考验

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301101226.png)

## 2、安装并运行单机版 Nacos
> 依然是使用 docker，默认账户密码都为：nacos

1.  搜索拉取 nacos

```bash
docker@VM-8-15-ubuntu:~$ docker search nacos
NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
nacos/nacos-server               This project contains a Docker image meant t…   353                  [OK]
zhusaidong/nacos-server-m1       Nacos Server for Apple MacOS M1                 17                   
nacos/nacos-mysql-master         nacos-mysql-master                              6                    
nacos/nacos-mysql                                                                6                    
paderlol/nacos                   Nacos-quick-start-https://nacos.io/en-us/doc…   5                    
chenfengwei/nacos                nacos服务镜像,nacos版本1.3.2，同时兼任arm64…               3                    
nacos/nacos-operator                                                             2                    
nacos/nacos-peer-finder-plugin   scale plugin for nacos k8s                      2                    
king019/nacos                                                                    2                    
tanyi/nacos-server               nacos-server官方包制作而成的镜像                          1                    
nacos/nacos-mysql-slave                                                          1                    
loads/nacos-server                                                               0                    
jude95/nacos-server-mysql8       nacos with mysql8                               0                    
nacosta/node-5.5.0-base                                                          0                    
nacosta/redis                                                                    0                    
centralx/nacos-server            Multi CPU architectures support for nacos/na…   0                    
nacosta/nodejs                                                                   0                    
dockerlishijie/nacos-server                                                      0                    
tonychen0716/nacos-server        Multi-arch image for Alibaba Nacos              0                    
lizexiong/nacos                                                                  0                    
eduosi/nacos-server                                                              0                    
paderlol/nacos-mysql-master                                                      0                    
paderlol/nacos-mysql-slave                                                       0                    
lijiahao1995/nacos                                                               0                    
daixijun1990/nacos-initial                                                       0                    

docker@VM-8-15-ubuntu:~$ docker pull nacos/nacos-server
Using default tag: latest
latest: Pulling from nacos/nacos-server
5ad559c5ae16: Pull complete 
5746ca7cf180: Pull complete 
d709fe221c89: Pull complete 
e88fdcf257b1: Pull complete 
eb573b28173c: Pull complete 
a71625257ced: Pull complete 
26e7e7836838: Pull complete 
30f7d6851c4a: Pull complete 
d565cd94c625: Pull complete 
Digest: sha256:87a3d8b78ec24c253a4db7c093097a7b256327eb5117cd9498e289b896918153
Status: Downloaded newer image for nacos/nacos-server:latest
docker.io/nacos/nacos-server:latest

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
docker-compose_nginx          latest    524bf968c7e3   3 weeks ago     142MB
docker-compose_java-service   latest    4bd1f84ef9cc   3 weeks ago     453MB
nginx                         latest    605c77e624dd   14 months ago   141MB
zookeeper                     3.6       3e9dd32cd767   14 months ago   277MB
mysql                         5.7       c20987f18b13   14 months ago   448MB
ubuntu                        latest    ba6acccedd29   16 months ago   72.8MB
nacos/nacos-server            latest    bdf60dc2ada3   19 months ago   1.05GB
redis                         6.2.1     de974760ddb2   22 months ago   105MB
portainer/portainer           1.20.2    19d07168491a   3 years ago     74.1MB

docker@VM-8-15-ubuntu:~$ 
```
	
 2.  创建临时容器用于拷贝配置文件和日志：`docker run -p 8848:8848 --name nacos -d nacos/nacos-server:latest`

```bash
docker@VM-8-15-ubuntu:~$ docker run -p 8848:8848 --name nacos -d nacos/nacos-server:latest
15398e7a45700016de86263468f9a2172dc09581b430b26bbaf80aff9cd9e846

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
15398e7a4570   nacos/nacos-server:latest     "bin/docker-startup.…"   5 seconds ago   Up 3 seconds   0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos
890052e7a032   mysql:5.7                     "docker-entrypoint.s…"   2 weeks ago     Up 2 weeks     0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sharp_kare
d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   3 weeks ago     Up 2 weeks     0.0.0.0:80->80/tcp, :::80->80/tcp                      nginx
7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   3 weeks ago     Up 2 weeks     0.0.0.0:9000->9000/tcp, :::9000->9000/tcp              java-service
9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             3 weeks ago     Up 3 weeks     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~$ 
```

3.  创建文件夹：`/home/docker/docker/VOLUME/nacos/`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301101430.png)

4.  配置文件和日志复制：
	1. `docker cp nacos:/home/nacos/conf/ ~/docker/VOLUME/nacos/nacos/`
	2. `docker cp nacos:/home/nacos/logs/ ~/docker/VOLUME/nacos/nacos/`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301101555.png)

5.  单机版部署：
	1. `-e MODE=standalone`：以单机模式启动
	2. `-e TIME_ZONE='Asia/Shanghai'`：设置时区为上海

	```bash
	docker run -d \
	  -e MODE=standalone \
	  -e TIME_ZONE='Asia/Shanghai' \
	  -v ~/docker/VOLUME/nacos/nacos/conf:/home/nacos/conf \
	  -v ~/docker/VOLUME/nacos/nacos/logs:/home/nacos/logs \
	  -p 8848:8848 \
	  --name nacosStandalone \
	  nacos/nacos-server:latest
	```

	```bash
	docker@VM-8-15-ubuntu:~$ docker run -d \
    >   -e MODE=standalone \
    >   -e TIME_ZONE='Asia/Shanghai' \
    >   -v ~/docker/VOLUME/nacos/conf:/home/nacos/conf \
    >   -v ~/docker/VOLUME/nacos/logs:/home/nacos/logs \
    >   -p 8848:8848 \
    >   --name nacos \
    >   nacos/nacos-server:latest
	b02d84bba4c7419ef055aa6dd8edcc7b8e6a4c68fa2b21735cbcc27d5d26f862
	
	docker@VM-8-15-ubuntu:~$ docker ps
	CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
	b02d84bba4c7   nacos/nacos-server:latest     "bin/docker-startup.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos
	890052e7a032   mysql:5.7                     "docker-entrypoint.s…"   2 weeks ago     Up 2 weeks     0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sharp_kare
	d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   3 weeks ago     Up 2 weeks     0.0.0.0:80->80/tcp, :::80->80/tcp                      nginx
	7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   3 weeks ago     Up 2 weeks     0.0.0.0:9000->9000/tcp, :::9000->9000/tcp              java-service
	9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             3 weeks ago     Up 3 weeks     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski
	
	docker@VM-8-15-ubuntu:~$ docker logs b02d84bba4c7
	+ export CUSTOM_SEARCH_NAMES=application,custom
	+ CUSTOM_SEARCH_NAMES=application,custom
	+ export CUSTOM_SEARCH_LOCATIONS=/home/nacos/init.d/,file:/home/nacos/conf/
	+ CUSTOM_SEARCH_LOCATIONS=/home/nacos/init.d/,file:/home/nacos/conf/
	+ export MEMBER_LIST=
	+ MEMBER_LIST=
	+ PLUGINS_DIR=/home/nacos/plugins/peer-finder
	+ [[ standalone == \s\t\a\n\d\a\l\o\n\e ]]
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true'
	+ [[ all == \c\o\n\f\i\g ]]
	+ [[ all == \n\a\m\i\n\g ]]
	+ [[ ! -z '' ]]
	+ [[ ! -z '' ]]
	+ [[ ! -z '' ]]
	+ [[ ! -z '' ]]
	+ [[ ! -z '' ]]
	+ [[ ip == \h\o\s\t\n\a\m\e ]]
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list='
	++ /usr/lib/jvm/java-1.8.0-openjdk/bin/java -version
	++ sed -E -n 's/.* version "([0-9]*).*$/\1/p'
	+ JAVA_MAJOR_VERSION=1
	+ [[ 1 -ge 9 ]]
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar '
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar  --spring.config.additional-location=/home/nacos/init.d/,file:/home/nacos/conf/'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar  --spring.config.additional-location=/home/nacos/init.d/,file:/home/nacos/conf/ --spring.config.name=application,custom'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar  --spring.config.additional-location=/home/nacos/init.d/,file:/home/nacos/conf/ --spring.config.name=application,custom --logging.config=/home/nacos/conf/nacos-logback.xml'
	+ JAVA_OPT=' -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar  --spring.config.additional-location=/home/nacos/init.d/,file:/home/nacos/conf/ --spring.config.name=application,custom --logging.config=/home/nacos/conf/nacos-logback.xml --server.max-http-header-size=524288'
	+ echo 'Nacos is starting, you can docker logs your container'
	Nacos is starting, you can docker logs your container
	+ exec /usr/lib/jvm/java-1.8.0-openjdk/bin/java -Xms1g -Xmx1g -Xmn512m -Dnacos.standalone=true -Dnacos.member.list= -Djava.ext.dirs=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext:/usr/lib/jvm/java-1.8.0-openjdk/lib/ext:/home/nacos/plugins/health:/home/nacos/plugins/cmdb:/home/nacos/plugins/mysql -Xloggc:/home/nacos/logs/nacos_gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dnacos.home=/home/nacos -jar /home/nacos/target/nacos-server.jar --spring.config.additional-location=/home/nacos/init.d/,file:/home/nacos/conf/ --spring.config.name=application,custom --logging.config=/home/nacos/conf/nacos-logback.xml --server.max-http-header-size=524288
	
	2023-02-28 16:24:11,309 INFO Bean 'org.springframework.security.access.expression.method.DefaultMethodSecurityExpressionHandler@328572f0' of type [org.springframework.security.access.expression.method.DefaultMethodSecurityExpressionHandler] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
	
	2023-02-28 16:24:11,322 INFO Bean 'methodSecurityMetadataSource' of type [org.springframework.security.access.method.DelegatingMethodSecurityMetadataSource] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
	
	2023-02-28 16:24:11,862 INFO Tomcat initialized with port(s): 8848 (http)
	
	2023-02-28 16:24:12,671 INFO Root WebApplicationContext: initialization completed in 8255 ms
	
	2023-02-28 16:24:21,379 INFO Initializing ExecutorService 'applicationTaskExecutor'
	
	2023-02-28 16:24:21,591 INFO Adding welcome page: class path resource [static/index.html]
	
	2023-02-28 16:24:22,452 INFO Creating filter chain: Ant [pattern='/**'], []
	
	docker@VM-8-15-ubuntu:~$ 
	```

6.  访问：[http://43.138.106.181:8848/nacos/#/login](http://43.138.106.181:8848/nacos/#/login)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301105146.png)

7.  输入账号密码 nacos 登录

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301105211.png)

## 3、Nacos 作为服务注册中心演示
官网文档：[https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_nacos_config](https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_nacos_config)
### ①、基于 Nacos的 服务提供者

1.  新建模块 cloudalibaba-provider-payment9001

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301111239.png)

2.  修改父 pom.xml，增加依赖 `spring-cloud-alibaba-dependencies` （之前好像就加上了）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.yuehai</groupId>
    <artifactId>SpringCloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <!-- 子项目 -->
    <modules>
        <module>cloud-provider-payment8001</module>
        <module>cloud-consumer-order80</module>
        <module>cloud-api-commons</module>
        <module>cloud-eureka-server7001</module>
        <module>cloud-eureka-server7002</module>
        <module>cloud-provider-payment8002</module>
        <module>cloud-provider-payment8004</module>
        <module>cloud-consumerzk-order80</module>
        <module>cloud-consumer-feign-order80</module>
        <module>cloud-provider-hystrix-payment8007</module>
        <module>cloud-consumer-feign-hystrix-order80</module>
        <module>cloud-provider-hystrix-payment8008</module>
        <module>cloud-consumer-hystrix-dashboard9001</module>
        <module>cloud-gateway-gateway9527</module>
        <module>cloud-config-center3344</module>
        <module>cloud-config-client3355</module>
        <module>cloudalibaba-provider-payment9001</module>
    </modules>
    
    <!-- 统一管理 jar 包版本 -->
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    
        <junit.version>4.12</junit.version>
        <log4j.version>1.2.17</log4j.version>
        <lombok.version>1.16.18</lombok.version>
        <mysql.version>5.1.47</mysql.version>
        <druid.version>1.1.16</druid.version>
        <mybatis-plus.spring.boot.version>3.5.1</mybatis-plus.spring.boot.version>
    
        <hutool-all>5.8.11</hutool-all>
    </properties>
    
    <!-- 子模块继承之后，提供作用：锁定版本 + 子 modlue 不用写 groupId 和 version  -->
    <dependencyManagement>
        <dependencies>
            <!--spring boot 2.2.2-->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.2.2.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--spring cloud Hoxton.SR1-->
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Hoxton.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--spring cloud alibaba 2.1.0.RELEASE-->
            <dependency>
                <groupId>com.alibaba.cloud</groupId>
                <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                <version>2.1.0.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            
            <!-- mysql -->
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
            <!-- mybatis-plus -->
            <dependency>
                <groupId>com.baomidou</groupId>
                <artifactId>mybatis-plus-boot-starter</artifactId>
                <version>${mybatis-plus.spring.boot.version}</version>
            </dependency>
    
            <!-- hutool 工具包 -->
            <dependency>
                <groupId>cn.hutool</groupId>
                <artifactId>hutool-all</artifactId>
                <version>${hutool-all}</version>
            </dependency>
            
            <!-- junit Test -->
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>${junit.version}</version>
            </dependency>
            <!-- log4j -->
            <dependency>
                <groupId>log4j</groupId>
                <artifactId>log4j</artifactId>
                <version>${log4j.version}</version>
            </dependency>
            <!-- lombok -->
            <dependency>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>${lombok.version}</version>
                <optional>true</optional>
            </dependency>
        </dependencies>
    </dependencyManagement>
    
</project>
```

3.  修改 9001 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-provider-payment9001</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
    </dependencies>

</project>
```

4.  修改 yml 配置文件

```yml
# 服务端口号
server:
    port: 9001

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloudalibaba-provider-payment9001
        name: nacos-payment-provider
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: '*'
```

5.  修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务提供者支付模块 cloud-provider-payment8001
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class NacosPayment9001 {

    public static void main(String[] args) {
        SpringApplication.run(NacosPayment9001.class, args);
    }

}
```

6.  编写业务类 controller

```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/2/28 11:03
 *
 * { @RefreshScope }：配置动态刷新
 */

@RestController
@RefreshScope
public class PaymentNacos9001Controller {

    @Value("${server.port}")
    private String port;

    @Value("${spring.application.name}")
    private String applicationName;

    @Value("${spring.cloud.nacos.discovery.server-addr}")
    private String serverAddr;

    @GetMapping("/getConfig")
    public JsonResult getConfig(){
        return JsonResult.success("端口号："+ port +"\r\n服务名："+ applicationName +"\r\nnacos 地址：" + serverAddr);
    }
}

```

7.  启动 9001 之前，查看控制台：[http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=](http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301105945.png)

8.  启动项目，查看控制台：[http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=](http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301110012.png)

9.  参照 9001 新建 9002

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301112205.png)

10. 启动两个模块

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301123726.png)
### ②、基于 Nacos 的服务消费者

1. 新建模块 cloudalibaba-consumer-nacos-order83

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301124753.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-consumer-nacos-order83</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 83

# spring 配置
spring:
    application:
        # 服务名称 微服务消费者用户模块 cloudalibaba-consumer-nacos-order83
        name: nacos-order-consumer
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848

# 消费者将要去访问的微服务名称（注册成功进 nacos 的微服务提供者），这个不是配置项，只是为了方便获取值
service-url:
    nacos-user-service: http://nacos-payment-provider
```

4. 修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务提供者支付模块 cloudalibaba-provider-payment9001
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class NacosOrder83 {

    public static void main(String[] args) {
        SpringApplication.run(NacosOrder83.class, args);
    }

}

```

5. 创建 RestTemplate 类

```java
package com.yuehai.config;

import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * @author 月海
 * @create 2023/3/1 13:08
 */

@Configuration
public class ApplicationContextBean {

    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate(){
        return new RestTemplate();
    }

}

```

6. 创建业务类

```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.HashMap;

/**
 * @author 月海
 * @create 2023/2/28 11:03
 *
 * { @RefreshScope }：配置动态刷新
 */

@RestController
public class OrderNacos83Controller {

    /**
     * Spring 框架提供的一个工具类，可远程调用一个 HTTP 接口
     */
    @Resource
    private RestTemplate restTemplate;

    /**
     * 获取服务名
     */
    @Value("${service-url.nacos-user-service}")
    private String serverURL;

    @GetMapping("/getPayment")
    public JsonResult getConfig(){
        return JsonResult.success(restTemplate.getForEntity(serverURL + "/getConfig", JsonResult.class));
    }
}

```

6. 访问测试：http://localhost:83/getPayment，多次刷新端口号会发生变化，可知<font color="#c00000">负载均衡已启用</font>

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301134603.png)
### ③、服务注册中心对比
#### Ⅰ、Nacos 全景图

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301134845.png)

#### Ⅱ、Nacos 和 CAP

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301135007.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301135023.png)

#### Ⅲ、Nacos 支持AP和CP模式的切换
1. <font color="#c00000">C是所有节点在同一时间看到的数据是一致的；而A的定义是所有的请求都会收到响应。</font> 
2. 何时选择使用何种模式？
3. 一般来说，如果不需要存储服务级别的信息且服务实例是通过nacos-client注册，并能够保持心跳上报，那么就可以选择AP模式。当前主流的服务如 Spring cloud 和 Dubbo 服务，都适用于AP模式，AP模式为了服务的可能性而减弱了一致性，因此AP模式下只支持注册临时实例。
4. 如果需要在服务级别编辑或者存储配置信息，那么 CP 是必须，K8S服务和DNS服务则适用于CP模式。CP模式下则支持注册持久化实例，此时则是以 Raft 协议为集群运行模式，该模式下注册实例之前必须先注册服务，如果服务不存在，则会返回错误。
5. 切换： `curl -X PUT '$NACOS_SERVER:8848/nacos/v1/ns/operator/switches?entry=serverMode&value=CP'`
## 4、Nacos 作为服务配置中心演示
### ①、基础配置
#### Ⅰ、创建模块
1. 新建模块 cloudalibaba-config-nacos-client3377

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301140738.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-config-nacos-client3377</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务配置中心-->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 yml 配置文件，需要配置两个：Nacos 同 springcloud-config 一样，在项目初始化时，要保证先从配置中心进行配置拉取，拉取配置之后，才能保证项目的正常启动。springboot 中配置文件的加载是存在优先级顺序的，bootstrap 优先级高于 application
	1. bootstrap
	```yml
	# nacos 配置
	server:
	    port: 3377
	
	spring:
	    application:
	        name: nacos-config-client
	    cloud:
	        nacos:
	            discovery:
	                # Nacos 服务注册中心地址
	                server-addr: 43.138.106.181:8848
	            config:
	                # Nacos 作为配置中心地址
	                server-addr: 43.138.106.181:8848
	                # 指定 yaml 格式的配置
	                file-extension: yaml
	                # bootstrap.yml 和 application.yml 结合起来就是：
	                # ${spring.application.name}-${spring.profile.active}.${spring.cloud.nacos.config.file-extension}
	                # 43.138.106.181:8848 下的：nacos-config-client-dev.yaml
	```
	2. application

	```yml
	# spring 配置
	spring:
	    # 显式激活指定的配置文件；
	    # SpringBoot 在启动加载配置文件时，如没有明确指定 spring.profiles.active 属性，默认是加载 application.yml 或 application.properties 文件
	    profiles:
	        # 表示开发环境
	        active: dev
	```

4. 修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务提供者支付模块 cloudalibaba-provider-payment9001
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class NacosConfigClient3377 {

    public static void main(String[] args) {
        SpringApplication.run(NacosConfigClient3377.class, args);
    }

}

```

5. 创建业务类

```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/1 14:30
 *
 * { @RefreshScope }：配置动态刷新
 */

@RestController
@RefreshScope
public class ConfigClientController {

    @Value("${spring.datasource.username}")
    private String datasourceUsername;

    @Value("${spring.datasource.password}")
    private String datasourcePassword;

    @Value("${spring.datasource.url}")
    private String datasourceUrl;

    @GetMapping("/getConfig")
    public JsonResult getConfig(){
        return JsonResult.success("账号："+ datasourceUsername +"\r\n密码："+ datasourcePassword +"\r\n连接地址：" + datasourceUrl);
    }

}

```
#### Ⅱ、在 Nacos 中添加配置信息
> Nacos 中的 dataid 的组成格式及与 SpringBoot 配置文件中的匹配规则：
> 
> https://nacos.io/zh-cn/docs/quick-start-spring-cloud.html
> 
> 之所以需要配置 `spring.application.name` ，是因为它是构成 Nacos 配置管理 dataId 字段的一部分，在 Nacos Spring Cloud 中，dataId 的完整格式为：<font color="#c00000">`${prefix}-${spring.profiles.active}.${file-extension}`</font>
> 
> 最后公式：<font color="#c00000">`<font color="#c00000">${spring.application.name}-${spring.profiles.active}.${spring.cloud.nacos.config.file-extension}</font>`</font>
1. 新增对应配置：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301144452.png)

2. 输入配置 DataID：`nacos-config-client-dev.yaml`
3. 输入配置内容：

```yml
# spring 配置
spring:
    datasource:
        # mysql驱动包 com.mysql.jdbc.Driver
        driver-class-name: com.mysql.jdbc.Driver
        # 连接信息
        # characterEncoding=UTF-8：指定所处理字符的解码和编码的格式
        # useSSL=false：不进行 SSL 连接
        # allowPublicKeyRetrieval=true：允许恶意代理执行MITM攻击以获取明文密码，因此它在默认情况下为False，必须显式启用
        # serverTimezone=GMT：格林尼治标准时间
        url: jdbc:mysql://43.138.106.181:3306/SpringCloud??characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=GMT
        # 用户名
        #username: root
        username: yuehai
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301144823.png)

4. 历史配置：Nacos 会记录配置文件的历史版本默认保留 30 天，此外还有一键回滚功能，回滚操作将会触发配置更新
5. 回滚：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301145024.png)
#### Ⅲ、测试
1. 查看 Data ID 是否对应
2. 启动 3377
3. 访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301145759.png)

4. 自带动态刷新：修改下 Nacos 中的 yaml 配置文件，再次调用查看配置的接口，就会发现配置已经刷新
### ②、分类配置
#### Ⅰ、多环境多项目管理
 
1. 问题 1：实际开发中，通常一个系统会准备：
	1. dev 开发环境
	2. test 测试环境
	3. prod 生产环境。
	4. 如何保证指定环境启动时服务能正确读取到 Nacos 上相应环境的配置文件呢？
2. 问题 2：
	1. 一个大型分布式微服务系统会有很多微服务子项目，
	2. 每个微服务项目又都会有相应的开发环境、测试环境、预发环境、正式环境......
	3. 那怎么对这些微服务配置进行管理呢？
#### Ⅱ、Nacos 的图形化管理界面
1. 配置管理：
![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301153705.png)

2. 命名空间 Namespace：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301153747.png)
#### Ⅲ、Namespace + Group + DataID 三者关系？为什么这么设计？
1.  是什么：类似 Java 里面的 package 名和类名；最外层的 namespace 是可以用于区分部署环境的，Group 和 DataID 逻辑上区分两个目标对象。
2. 三者情况：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301154303.png)

3. 默认情况：Namespace=public，Group=DEFAULT_GROUP，默认 Cluster 是 DEFAULT
	1. Nacos 默认的命名空间是 public，Namespace 主要用来实现隔离。
	2. 比方说我们现在有三个环境：开发、测试、生产环境，我们就可以创建三个 Namespace，不同的 Namespace 之间是隔离的。
4. Group 默认是 DEFAULT_GROUP，Group 可以把不同的微服务划分到同一个分组里面去
5. Service 就是微服务；一个 Service 可以包含多个 Cluster（集群），Nacos 默认 Cluste r是 DEFAULT，Cluster 是对指定微服务的一个虚拟划分。
	1. 比方说为了容灾，将 Service 微服务分别部署在了杭州机房和广州机房
	2. 这时就可以给杭州机房的 Service 微服务起一个集群名称（HZ），给广州机房的 Service 微服务起一个集群名称（GZ）
	3. 还可以尽量让同一个机房的微服务互相调用，以提升性能。
6. 最后是 Instance，就是微服务的实例。
#### Ⅳ、三种方案加载配置
##### （1）、DataID 方案
1. 指定 `spring.profile.active` 和配置文件的 DataID 来使不同环境下读取不同的配置
2. 默认空间+默认分组+新建 dev 和 test 两个 DataID
	1. 新建 dev 配置 DataID（之前配过了）
	2. 新建 test 配置 DataID：`nacos-config-client-test.yaml`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301160629.png)

3. 配置 application.yml 文件的 spring.profile.active 属性就能进行多环境下配置文件的读取

```yml
# spring 配置
spring:
    # 显式激活指定的配置文件；
    # SpringBoot 在启动加载配置文件时，如没有明确指定 spring.profiles.active 属性，默认是加载 application.yml 或 application.properties 文件
    profiles:
        # 表示开发环境
        # active: dev
        # 表示测试环境
        active: test
```

4. 重新启动，访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301161103.png)
##### （2）、Group 方案
1. 新建两个 Group，分别为：`DEV_GROUP`、`TEST_GROUP`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301162046.png)

2. 两个新的配置文件创建

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301162228.png)

3. bootstrap.yml 配置

```yml
# nacos 配置
server:
    port: 3377

spring:
    application:
        name: nacos-config-client
    cloud:
        nacos:
            discovery:
                # Nacos 服务注册中心地址
                server-addr: 43.138.106.181:8848
            config:
                # Nacos 作为配置中心地址
                server-addr: 43.138.106.181:8848
                # 指定 yaml 格式的配置
                file-extension: yaml
                # 指定 nacos 组
                group: DEV_GROUP
                # bootstrap.yml 和 application.yml 结合起来就是：
                # ${spring.application.name}-${spring.profile.active}.${spring.cloud.nacos.config.file-extension}
                # 43.138.106.181:8848 下的：nacos-config-client-info.yaml
```

4. application.yml 配置

```yml
# spring 配置
spring:
    # 显式激活指定的配置文件；
    # SpringBoot 在启动加载配置文件时，如没有明确指定 spring.profiles.active 属性，默认是加载 application.yml 或 application.properties 文件
    profiles:
        # 表示开发环境
        # active: dev
        # 表示测试环境
        # active: test
        # 表示已配置 group
        active: info
```

5. 重启项目，访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301163047.png)
##### （3）、Namespace 方案
1. 新建 dev/test 的 Namespace

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301163329.png)

2. 创建完成之后

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301163405.png)

3. 回到服务管理-服务列表查看

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301163442.png)

4. 新建配置 nacos-config-client-info.yaml

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301165958.png)

5. 创建完成

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230301165156.png)

6. bootstrap.yml 配置

```yml
# nacos 配置
server:
    port: 3377

spring:
    application:
        name: nacos-config-client
    cloud:
        nacos:
            discovery:
                # Nacos 服务注册中心地址
                server-addr: 43.138.106.181:8848
            config:
                # Nacos 作为配置中心地址
                server-addr: 43.138.106.181:8848
                # 指定 yaml 格式的配置
                file-extension: yaml
                # 指定 nacos 组
                # group: DEV_GROUP
                # 指定命名空间，只能输入命名空间的 id
                namespace: a7294fe4-a205-44de-b24e-dd06c71fecaa
                # bootstrap.yml 和 application.yml 结合起来就是：
                # ${spring.application.name}-${spring.profile.active}.${spring.cloud.nacos.config.file-extension}
                # 43.138.106.181:8848 下 dev 命名空间下的的：nacos-config-client-info.yaml
```

7. application.yml 配置

```yml
# spring 配置
spring:
    # 显式激活指定的配置文件；
    # SpringBoot 在启动加载配置文件时，如没有明确指定 spring.profiles.active 属性，默认是加载 application.yml 或 application.properties 文件
    profiles:
        # 表示已配置 group 或 namespace
        active: info
        # 表示开发环境
        # active: dev
        # 表示测试环境
        # active: test
```

8. 重启项目，访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302085924.png)

## 5、Nacos 集群和持久化配置（重要）
### ①、官网说明
> https://nacos.io/zh-cn/docs/cluster-mode-quick-start.html

#### Ⅰ、官网集群部署说明
1. 集群部署架构图：
2. 因此开源的时候推荐用户把所有服务列表放到一个vip下面，然后挂到一个域名下面
3. http://ip1:port/openAPI 直连ip模式，机器挂则需要修改ip才可以使用。
4. http://SLB:port/openAPI 挂载SLB模式(内网SLB，不可暴露到公网，以免带来安全风险)，直连SLB即可，下面挂server真实ip，可读性不好。
5. http://nacos.com:port/openAPI 域名 + SLB模式(内网SLB，不可暴露到公网，以免带来安全风险)，可读性好，而且换ip方便，推荐模式

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302091737.png)

#### Ⅱ、上图官网翻译，真实情况

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302091758.png)

#### Ⅲ、说明

1. 默认 Nacos 使用嵌入式数据库实现数据的存储。所以，如果启动多个默认配置下的 Nacos 节点，数据存储是存在一致性问题的。
2. 为了解决这个问题，Nacos 采用了<font color="#c00000">集中式存储的方式来支持集群化部署，目前只支持 MySQL 的存储</font>。
3. Nacos 支持三种部蓍模式：
	1. 单机模式：用于测试和单机试用。
	2. 集群模式：用于生产环境，确保高可用。
	3. 多集群模式：用于多数据中心场景。
4. 单机模式支持 mysql
	1. 0.7 版本之前，在单机模式时 nacos 使用嵌入式数据库实现数据的存储，不方便观察数据存储的基本情况。
	2. 0.7 版本增加了支持 mysql 数据源能力，具体的操作步骤：
		1. 安装数据库，版本要求：5.6.5+
		2. 初始化 mysql 数据库，数据库初始化文件：nacos-mysql.sql
		3. 修改 conf/application.properties 文件，增加支持 mysql 数据源配置(目前只支持 mysql)，添加 mysql 数据源的 url、用户名和密码。
5. 再以单机模式启动 nacos，nacos 所有写嵌入式数据库的数据都写到了 mysql

### ②、Nacos 持久化配置解释
> Nacos 默认自带的是嵌入式数据库 derby：https://github.com/alibaba/nacos/blob/develop/config/pom.xml

derby 到 mysql 切换配置步骤：
1. 停止并删除之前启动的 nacos 容器：

```bash
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
ff7339913c65   redis:latest                 "docker-entrypoint.s…"   23 minutes ago   Up 23 minutes   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp              redis
4c456c76fc29   mysql:latest                 "docker-entrypoint.s…"   35 minutes ago   Up 35 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   mysql
b02d84bba4c7   nacos/nacos-server:latest    "bin/docker-startup.…"   42 hours ago     Up 42 hours     0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             3 weeks ago      Up 3 weeks      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~$ docker stop b02d84bba4c7
b02d84bba4c7

docker@VM-8-15-ubuntu:~$ docker rm b02d84bba4c7
b02d84bba4c7

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
ff7339913c65   redis:latest                 "docker-entrypoint.s…"   23 minutes ago   Up 23 minutes   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp              redis
4c456c76fc29   mysql:latest                 "docker-entrypoint.s…"   35 minutes ago   Up 35 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   mysql
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             3 weeks ago      Up 3 weeks      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~$ 
```

2. 创建下列 sql 脚本，在 mysql 数据库中执行，以创建 nacos 所需的数据库与表：

```sql
/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = config_info   */
/******************************************/
CREATE TABLE `config_info` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` VARCHAR(255) NOT NULL COMMENT 'data_id',
  `group_id` VARCHAR(255) DEFAULT NULL,
  `content` LONGTEXT NOT NULL COMMENT 'content',
  `md5` VARCHAR(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` TEXT COMMENT 'source user',
  `src_ip` VARCHAR(50) DEFAULT NULL COMMENT 'source ip',
  `app_name` VARCHAR(128) DEFAULT NULL,
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT '租户字段',
  `c_desc` VARCHAR(256) DEFAULT NULL,
  `c_use` VARCHAR(64) DEFAULT NULL,
  `effect` VARCHAR(64) DEFAULT NULL,
  `type` VARCHAR(64) DEFAULT NULL,
  `c_schema` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfo_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info';

/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = config_info_aggr   */
/******************************************/
CREATE TABLE `config_info_aggr` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` VARCHAR(255) NOT NULL COMMENT 'data_id',
  `group_id` VARCHAR(255) NOT NULL COMMENT 'group_id',
  `datum_id` VARCHAR(255) NOT NULL COMMENT 'datum_id',
  `content` LONGTEXT NOT NULL COMMENT '内容',
  `gmt_modified` DATETIME NOT NULL COMMENT '修改时间',
  `app_name` VARCHAR(128) DEFAULT NULL,
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT '租户字段',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfoaggr_datagrouptenantdatum` (`data_id`,`group_id`,`tenant_id`,`datum_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='增加租户字段';


/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = config_info_beta   */
/******************************************/
CREATE TABLE `config_info_beta` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` VARCHAR(255) NOT NULL COMMENT 'data_id',
  `group_id` VARCHAR(128) NOT NULL COMMENT 'group_id',
  `app_name` VARCHAR(128) DEFAULT NULL COMMENT 'app_name',
  `content` LONGTEXT NOT NULL COMMENT 'content',
  `beta_ips` VARCHAR(1024) DEFAULT NULL COMMENT 'betaIps',
  `md5` VARCHAR(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` TEXT COMMENT 'source user',
  `src_ip` VARCHAR(50) DEFAULT NULL COMMENT 'source ip',
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT '租户字段',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfobeta_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_beta';

/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = config_info_tag   */
/******************************************/
CREATE TABLE `config_info_tag` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` VARCHAR(255) NOT NULL COMMENT 'data_id',
  `group_id` VARCHAR(128) NOT NULL COMMENT 'group_id',
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT 'tenant_id',
  `tag_id` VARCHAR(128) NOT NULL COMMENT 'tag_id',
  `app_name` VARCHAR(128) DEFAULT NULL COMMENT 'app_name',
  `content` LONGTEXT NOT NULL COMMENT 'content',
  `md5` VARCHAR(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` TEXT COMMENT 'source user',
  `src_ip` VARCHAR(50) DEFAULT NULL COMMENT 'source ip',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfotag_datagrouptenanttag` (`data_id`,`group_id`,`tenant_id`,`tag_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_tag';

/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = config_tags_relation   */
/******************************************/
CREATE TABLE `config_tags_relation` (
  `id` BIGINT(20) NOT NULL COMMENT 'id',
  `tag_name` VARCHAR(128) NOT NULL COMMENT 'tag_name',
  `tag_type` VARCHAR(64) DEFAULT NULL COMMENT 'tag_type',
  `data_id` VARCHAR(255) NOT NULL COMMENT 'data_id',
  `group_id` VARCHAR(128) NOT NULL COMMENT 'group_id',
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT 'tenant_id',
  `nid` BIGINT(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `uk_configtagrelation_configidtag` (`id`,`tag_name`,`tag_type`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_tag_relation';

/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = group_capacity   */
/******************************************/
CREATE TABLE `group_capacity` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `group_id` VARCHAR(128) NOT NULL DEFAULT '' COMMENT 'Group ID，空字符表示整个集群',
  `quota` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数，，0表示使用默认值',
  `max_aggr_size` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_group_id` (`group_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='集群、各Group容量信息表';

/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = his_config_info   */
/******************************************/
CREATE TABLE `his_config_info` (
  `id` BIGINT(64) UNSIGNED NOT NULL,
  `nid` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `data_id` VARCHAR(255) NOT NULL,
  `group_id` VARCHAR(128) NOT NULL,
  `app_name` VARCHAR(128) DEFAULT NULL COMMENT 'app_name',
  `content` LONGTEXT NOT NULL,
  `md5` VARCHAR(32) DEFAULT NULL,
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `src_user` TEXT,
  `src_ip` VARCHAR(50) DEFAULT NULL,
  `op_type` CHAR(10) DEFAULT NULL,
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT '租户字段',
  PRIMARY KEY (`nid`),
  KEY `idx_gmt_create` (`gmt_create`),
  KEY `idx_gmt_modified` (`gmt_modified`),
  KEY `idx_did` (`data_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='多租户改造';


/******************************************/
/*   数据库全名 = nacos-config   */
/*   表名称 = tenant_capacity   */
/******************************************/
CREATE TABLE `tenant_capacity` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `tenant_id` VARCHAR(128) NOT NULL DEFAULT '' COMMENT 'Tenant ID',
  `quota` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数',
  `max_aggr_size` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_id` (`tenant_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='租户容量信息表';


CREATE TABLE `tenant_info` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `kp` VARCHAR(128) NOT NULL COMMENT 'kp',
  `tenant_id` VARCHAR(128) DEFAULT '' COMMENT 'tenant_id',
  `tenant_name` VARCHAR(128) DEFAULT '' COMMENT 'tenant_name',
  `tenant_desc` VARCHAR(256) DEFAULT NULL COMMENT 'tenant_desc',
  `create_source` VARCHAR(32) DEFAULT NULL COMMENT 'create_source',
  `gmt_create` BIGINT(20) NOT NULL COMMENT '创建时间',
  `gmt_modified` BIGINT(20) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_info_kptenantid` (`kp`,`tenant_id`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='tenant_info';

CREATE TABLE `users` (
    `username` VARCHAR(50) NOT NULL PRIMARY KEY,
    `password` VARCHAR(500) NOT NULL,
    `enabled` BOOLEAN NOT NULL
);

CREATE TABLE `roles` (
    `username` VARCHAR(50) NOT NULL,
    `role` VARCHAR(50) NOT NULL,
    UNIQUE INDEX `idx_user_role` (`username` ASC, `role` ASC) USING BTREE
);

CREATE TABLE `permissions` (
    `role` VARCHAR(50) NOT NULL,
    `resource` VARCHAR(255) NOT NULL,
    `action` VARCHAR(8) NOT NULL,
    UNIQUE INDEX `uk_role_permission` (`role`,`resource`,`action`) USING BTREE
);

INSERT INTO users (username, PASSWORD, enabled) VALUES ('nacos', '$2a$10$EuWPZHzz32dJN7jexM34MOeYirDdFAZm2kuWj7VEOJhhZkDrxfvUu', TRUE);

INSERT INTO roles (username, role) VALUES ('nacos', 'ROLE_ADMIN');
```

3. 创建 mysql 挂载目录：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302105504.png)

4. 启动 mysql 容器：`docker run -d -p 3306:3306 --privileged=true -v /home/docker/docker/VOLUME/mysql/log:/var/log/mysql -v /home/docker/docker/VOLUME/mysql/data:/var/lib/mysql -v /home/docker/docker/VOLUME/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=000123 --name yuehai-mysql mysql`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d -p 3306:3306 --privileged=true -v /home/docker/docker/VOLUME/mysql/log:/var/log/mysql -v /home/docker/docker/VOLUME/mysql/data:/var/lib/mysql -v /home/docker/docker/VOLUME/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=000123 --name yuehai-mysql mysql
a8c5a95cfbef6fbfd999a6d960e11e9a1e27f435418b6a730749f88b6d1a7e65

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
a8c5a95cfbef   mysql                        "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   yuehai-mysql
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             4 weeks ago     Up 4 weeks     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~$ 
```

5. 使用 DataGrip 连接 mysql

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303085001.png)

6. 创建数据库：nacos-config

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302111311.png)

7. 执行刚才的 sql 脚本，查看生成的表

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302111524.png)

8. 启动 nacos 容器，添加 mysql 参数：
	1. `MODE=standalone`：以单机模式启动
	2. `SPRING_DATASOURCE_PLATFORM` : 使用的数据库类型
	3. `MYSQL_SERVICE_HOST`：数据库地址
	4. `MYSQL_SERVICE_PORT`：数据库端口号
	5. `MYSQL_SERVICE_DB_NAME`：数据库用户名
	6. `MYSQL_SERVICE_PASSWORD`：数据库密码
	7. `MYSQL_SERVICE_DB_NAME` : 数据库名称
	8. `TIME_ZONE='Asia/Shanghai'`：时区
	9. `MYSQL_DATABASE_NUM`：数据库数量，默认就是1，可以不填写

	```bash
	docker run -d \
		-e MODE=standalone \
		-e SPRING_DATASOURCE_PLATFORM=mysql \
		-e MYSQL_SERVICE_HOST=43.138.106.181 \
		-e MYSQL_SERVICE_PORT=3306 \
		-e MYSQL_SERVICE_USER=root \
		-e MYSQL_SERVICE_PASSWORD=000123 \
		-e MYSQL_SERVICE_DB_NAME=nacos-config \
		-e TIME_ZONE='Asia/Shanghai' \
		-v ~/docker/VOLUME/nacos/conf:/home/nacos/conf \
	    -v ~/docker/VOLUME/nacos/logs:/home/nacos/logs \
		-p 8848:8848 \
		--name nacos \
		--restart=always \
		nacos/nacos-server:latest
	```

	```bash
	docker@VM-8-15-ubuntu:~$ docker run -d \
	>     -e MODE=standalone \
	>     -e SPRING_DATASOURCE_PLATFORM=mysql \
	>     -e MYSQL_SERVICE_HOST=43.138.106.181 \
	>     -e MYSQL_SERVICE_PORT=3306 \
	>     -e MYSQL_SERVICE_USER=root \
	>     -e MYSQL_SERVICE_PASSWORD=000123 \
	>     -e MYSQL_SERVICE_DB_NAME=nacos-config \
	>     -e TIME_ZONE='Asia/Shanghai' \
	>     -v ~/docker/VOLUME/nacos/conf:/home/nacos/conf \
	>     -v ~/docker/VOLUME/nacos/logs:/home/nacos/logs \
	>     -p 8848:8848 \
	>     --name nacos \
	>     --restart=always \
	>     nacos/nacos-server:latest
	a41cea0d1d0367983b093cb306c98657b9e16c22c2a3773099801de47563d24a
	docker@VM-8-15-ubuntu:~$ docker ps
	CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
	a41cea0d1d03   nacos/nacos-server:latest    "bin/docker-startup.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos
	a8c5a95cfbef   mysql                        "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   yuehai-mysql
	9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             3 weeks ago     Up 3 weeks     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski
	docker@VM-8-15-ubuntu:~$ 
	```

9. 访问 nacos：http://43.138.106.181:8848/nacos

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302134154.png)

10. 添加一个配置：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302134528.png)

11. 查看数据库：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230302134728.png)

### ③、1 个 MySQL + 3 个 Nacos + 1 个 Nginx 集群生产环境配置
> 3 个或以上的 nacos 节点才能构成集群

#### Ⅰ、1 个 MySQL
- 这里使用刚才配好的 7778 的 mysql
#### Ⅱ、3 个 Nacos

1. 分别启动 3 个 nacos，可以像这里一样传递参数，也可以直接修改配置文件：application.properties

```bash
docker run -d \
	-e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
    -e SPRING_DATASOURCE_PLATFORM=mysql \
    -e MYSQL_SERVICE_HOST=43.138.106.181 \
    -e MYSQL_SERVICE_PORT=3306 \
    -e MYSQL_SERVICE_USER=root \
    -e MYSQL_SERVICE_PASSWORD=000123 \
    -e MYSQL_SERVICE_DB_NAME=nacos-config \
    -e TIME_ZONE='Asia/Shanghai' \
    -v ~/docker/VOLUME/nacos/nacos1/conf:/home/nacos/conf \
    -v ~/docker/VOLUME/nacos/nacos1/logs:/home/nacos/logs \
    -p 8848:8848 \
    --name nacos1 \
    --restart=always \
    nacos/nacos-server:latest
```

```bash
docker run -d \
	-e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
    -e SPRING_DATASOURCE_PLATFORM=mysql \
    -e MYSQL_SERVICE_HOST=43.138.106.181 \
    -e MYSQL_SERVICE_PORT=3306 \
    -e MYSQL_SERVICE_USER=root \
    -e MYSQL_SERVICE_PASSWORD=000123 \
    -e MYSQL_SERVICE_DB_NAME=nacos-config \
    -e TIME_ZONE='Asia/Shanghai' \
    -v ~/docker/VOLUME/nacos/nacos2/conf:/home/nacos/conf \
    -v ~/docker/VOLUME/nacos/nacos2/logs:/home/nacos/logs \
    -p 8849:8848 \
    --name nacos2 \
    --restart=always \
    nacos/nacos-server:latest
```

```bash
docker run -d \
	-e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
    -e SPRING_DATASOURCE_PLATFORM=mysql \
    -e MYSQL_SERVICE_HOST=43.138.106.181 \
    -e MYSQL_SERVICE_PORT=3306 \
    -e MYSQL_SERVICE_USER=root \
    -e MYSQL_SERVICE_PASSWORD=000123 \
    -e MYSQL_SERVICE_DB_NAME=nacos-config \
    -e TIME_ZONE='Asia/Shanghai' \
    -v ~/docker/VOLUME/nacos/nacos3/conf:/home/nacos/conf \
    -v ~/docker/VOLUME/nacos/nacos3/logs:/home/nacos/logs \
    -p 8850:8848 \
    --name nacos3 \
    --restart=always \
    nacos/nacos-server:latest
```

```bash
	docker@VM-8-15-ubuntu:~$ docker run -d \
	>     -e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
	>     -e SPRING_DATASOURCE_PLATFORM=mysql \
	>     -e MYSQL_SERVICE_HOST=43.138.106.181 \
	>     -e MYSQL_SERVICE_PORT=3306 \
	>     -e MYSQL_SERVICE_USER=root \
	>     -e MYSQL_SERVICE_PASSWORD=000123 \
	>     -e MYSQL_SERVICE_DB_NAME=nacos-config \
	>     -e TIME_ZONE='Asia/Shanghai' \
	>     -v ~/docker/VOLUME/nacos/nacos1/conf:/home/nacos/conf \
	>     -v ~/docker/VOLUME/nacos/nacos1/logs:/home/nacos/logs \
	>     -p 8848:8848 \
	>     --name nacos1 \
	>     --restart=always \
	>     nacos/nacos-server:latest
	92b508e5292aaca3ecc225e97aede5425797b7f8d77a4910feefb3f30f87b274
	
	docker@VM-8-15-ubuntu:~$ docker run -d \
	>     -e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
	>     -e SPRING_DATASOURCE_PLATFORM=mysql \
	>     -e MYSQL_SERVICE_HOST=43.138.106.181 \
	>     -e MYSQL_SERVICE_PORT=3306 \
	>     -e MYSQL_SERVICE_USER=root \
	>     -e MYSQL_SERVICE_PASSWORD=000123 \
	>     -e MYSQL_SERVICE_DB_NAME=nacos-config \
	>     -e TIME_ZONE='Asia/Shanghai' \
	>     -v ~/docker/VOLUME/nacos/nacos2/conf:/home/nacos/conf \
	>     -v ~/docker/VOLUME/nacos/nacos2/logs:/home/nacos/logs \
	>     -p 8849:8848 \
	>     --name nacos2 \
	>     --restart=always \
	>     nacos/nacos-server:latest
	c085a883654b3a51b7cf9fc096e3506deda204cf201c86da078c866b9300f980
	
	docker@VM-8-15-ubuntu:~$ docker run -d \
	>     -e NACOS_SERVERS=43.138.106.181:8848,43.138.106.181:8849,43.138.106.181:8850 \
	>     -e SPRING_DATASOURCE_PLATFORM=mysql \
	>     -e MYSQL_SERVICE_HOST=43.138.106.181 \
	>     -e MYSQL_SERVICE_PORT=3306 \
	>     -e MYSQL_SERVICE_USER=root \
	>     -e MYSQL_SERVICE_PASSWORD=000123 \
	>     -e MYSQL_SERVICE_DB_NAME=nacos-config \
	>     -e TIME_ZONE='Asia/Shanghai' \
	>     -v ~/docker/VOLUME/nacos/nacos3/conf:/home/nacos/conf \
	>     -v ~/docker/VOLUME/nacos/nacos3/logs:/home/nacos/logs \
	>     -p 8850:8848 \
	>     --name nacos3 \
	>     --restart=always \
	>     nacos/nacos-server:latest
	b1b9c5e968ffd2d63d60e4463117d63c1786fa5d96fd8b40d36921cac3676346
	
	docker@VM-8-15-ubuntu:~$ docker ps
	CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
	b1b9c5e968ff   nacos/nacos-server:latest    "bin/docker-startup.…"   5 seconds ago    Up 4 seconds    0.0.0.0:8850->8848/tcp, :::8850->8848/tcp              nacos3
	c085a883654b   nacos/nacos-server:latest    "bin/docker-startup.…"   11 seconds ago   Up 10 seconds   0.0.0.0:8849->8848/tcp, :::8849->8848/tcp              nacos2
	92b508e5292a   nacos/nacos-server:latest    "bin/docker-startup.…"   18 seconds ago   Up 17 seconds   0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos1
	a8c5a95cfbef   mysql                        "docker-entrypoint.s…"   19 minutes ago   Up 19 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   yuehai-mysql
	9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             4 weeks ago      Up 4 weeks      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski
	
	docker@VM-8-15-ubuntu:~$ 
```

2. 访问测试：http://43.138.106.181:8848/nacos、http://43.138.106.181:8849/nacos、http://43.138.106.181:8850/nacos

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303091257.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303091322.png)
#### Ⅲ、1 个 Nginx
1. 创建 `/home/docker/docker/VOLUME/nginx-nacos/` 目录，并进入：`cd /home/docker/docker/VOLUME/nginx-nacos/`，并在其中创建 `conf` 目录

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303101659.png)

2. 在 `conf` 目录中创建文件 default.conf：

```conf
# nacos：使用此 nginx 作为 nacos 负载均衡服务器
upstream  nacosServer{
    server 43.138.106.181:8848;
    server 43.138.106.181:8849;
    server 43.138.106.181:8850;
}
server {
	# 监听 4000 端口，外部分配为 4000：4000
    listen       4000;
    server_name  43.138.106.181;
    
	location / {
		### 指定上游服务器负载均衡服务器
		proxy_pass http://nacosServer/;
		index  index.html index.htm;
	}
}
```

3. 在 `/home/docker/docker/VOLUME/nginx-nacos/` 目录中创建 dockerfile 文件

```dockerfile
# 基础镜像
FROM nginx
# 指定镜像维护者的姓名和邮箱地址
MAINTAINER yuehai

# 用本地的 default.conf 配置来替换 nginx 镜像里的默认配置
COPY conf/default.conf /etc/nginx/conf.d/default.conf
```

4. 在 `/home/docker/docker/VOLUME/nginx-nacos/` 目录下执行构建镜像命令：`docker build -t yuehai-nginx-nacos:v0.1 .`

```bash
docker@VM-8-15-ubuntu:~/docker/VOLUME/nginx-nacos$ docker build -t yuehai-nginx-nacos:v0.1 .
Sending build context to Docker daemon  3.584kB
Step 1/3 : FROM nginx
 ---> 605c77e624dd
Step 2/3 : MAINTAINER yuehai
 ---> Using cache
 ---> 748d0e8dcba8
Step 3/3 : COPY conf/default.conf /etc/nginx/conf.d/default.conf
 ---> e988bcbf0734
Successfully built e988bcbf0734
Successfully tagged yuehai-nginx-nacos:v0.1

docker@VM-8-15-ubuntu:~/docker/VOLUME/nginx-nacos$
```

5. 启动容器：`docker run -itd -p 4000:4000 --name yuehai-nginx-nacos yuehai-nginx-nacos:v0.1`

```bash
docker@VM-8-15-ubuntu:~/docker/VOLUME/nginx-nacos$ docker run -itd -p 4000:4000 --name yuehai-nginx-nacos yuehai-nginx-nacos:v0.1
3c43c96f17a3742da0a127953f6e3444bbd25a99bf569abf817f3e68319e4055

docker@VM-8-15-ubuntu:~/docker/VOLUME/nginx-nacos$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED              STATUS              PORTS                                                  NAMES
3c43c96f17a3   yuehai-nginx-nacos:v0.1      "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:4000->4000/tcp, :::4000->4000/tcp      yuehai-nginx-nacos
714f2ad125fa   yuehai-vue:v0.1              "/docker-entrypoint.…"   7 minutes ago        Up 7 minutes        0.0.0.0:3000->80/tcp, :::3000->80/tcp                  yuehai-vue
56fb21a2b129   yuehai-java:v0.1             "java -jar /applicat…"   23 minutes ago       Up 23 minutes       0.0.0.0:9000->9000/tcp, :::9000->9000/tcp              yuehai-java
826c3713519d   nacos/nacos-server:latest    "bin/docker-startup.…"   About an hour ago    Up About an hour    0.0.0.0:8850->8848/tcp, :::8850->8848/tcp              nacos3
9291e995b982   nacos/nacos-server:latest    "bin/docker-startup.…"   About an hour ago    Up About an hour    0.0.0.0:8849->8848/tcp, :::8849->8848/tcp              nacos2
b367b432e8ce   nacos/nacos-server:latest    "bin/docker-startup.…"   About an hour ago    Up About an hour    0.0.0.0:8848->8848/tcp, :::8848->8848/tcp              nacos1
a8c5a95cfbef   mysql                        "docker-entrypoint.s…"   2 hours ago          Up 2 hours          0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   yuehai-mysql
9c710fd9a47a   portainer/portainer:1.20.2   "/portainer"             4 weeks ago          Up 4 weeks          0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~/docker/VOLUME/nginx-nacos$ 
```

6. 访问测试：http://43.138.106.181:4000/nacos/#/login

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303102410.png)

7. 登录进入，添加配置：`nacos-config-client-info.yaml`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303102703.png)

#### Ⅳ、修改代码，连接集群
1. 修改 bootstrap.yml 文件，地址修改为 nginx 的地址

```yml
# nacos 配置
server:
    port: 3377

spring:
    application:
        name: nacos-config-client
    cloud:
        nacos:
            discovery:
                # Nacos 服务注册中心地址
                server-addr: 43.138.106.181:4000
            config:
                # Nacos 作为配置中心地址
                server-addr: 43.138.106.181:4000
                # 指定 yaml 格式的配置
                file-extension: yaml
                # 指定 nacos 组
                # group: DEV_GROUP
                # 指定命名空间，只能输入命名空间的 id
                # namespace: a7294fe4-a205-44de-b24e-dd06c71fecaa
                # bootstrap.yml 和 application.yml 结合起来就是：
                # ${spring.application.name}-${spring.profile.active}.${spring.cloud.nacos.config.file-extension}
                # 43.138.106.181:8848 下 dev 命名空间下的的：nacos-config-client-info.yaml
```

2. 修改 controller

```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/1 14:30
 *
 * { @RefreshScope }：配置动态刷新
 */

@RestController
@RefreshScope
public class ConfigClientController {

    // @Value("${spring.datasource.username}")
    // private String datasourceUsername;
    //
    // @Value("${spring.datasource.password}")
    // private String datasourcePassword;
    //
    // @Value("${spring.datasource.url}")
    // private String datasourceUrl;

    // @GetMapping("/getConfig")
    // public JsonResult getConfig(){
    //     return JsonResult.success("账号："+ datasourceUsername +"\r\n密码："+ datasourcePassword +"\r\n连接地址：" + datasourceUrl);
    // }

    @Value("${name}")
    private String name;

    @GetMapping("/getConfig")
    public JsonResult getConfig(){
        return JsonResult.success("name：" + name);
    }

}

```

3. 启动项目，访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303103120.png)

### ④、高可用小总结

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230303103235.png)

# 三、Sentinel 实现熔断与限流

> 官网：https://github.com/alibaba/Sentinel
> 
> 中文：https://github.com/alibaba/Sentinel/wiki/%E4%BB%8B%E7%BB%8D
> 
> 下载：https://github.com/alibaba/Sentinel/releases

## 1、简介

1. 是什么：类似 Hystrix，服务降级断路器，但是有自带的 web 界面
2. 能干嘛：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230313154914.png)

3. 怎么用：https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_sentinel
4. 服务使用中的各种问题：
	1. 服务雪崩
	2. 服务降级
	3. 服务熔断
	4. 服务限流
5. 分为两个部分：
	1. 核心库(Java 客户端8）：不依赖任何框架/库，能够运行于所有 Java 运行时环境，同时对 Dubbo / Spring Cloud 等框架也有较好的支持。
	2. 控制台(Dashboard)：基于 Spring Boot 开发，打包后可以直接运行，不需要额外的 Tomcat 等应用容器。

## 2、安装

> 还是 docker

1. 拉取镜像：`docker pull bladex/sentinel-dashboard`

```bash
docker@VM-8-15-ubuntu:~$ docker search Sentinel
NAME                                   DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
bladex/sentinel-dashboard              Alibaba Cloud Sentinel Dashboard (阿里巴巴流…        72                   
bitnami/redis-sentinel                 Bitnami Docker Image for Redis Sentinel         43                   [OK]
sentinelofficial/sentinel-vpn-node                                                     7                    
sentinelhub/eolearn                    Official eo-learn Docker images with Jupyter…   4                    
thrashr888/sentinel-simulator          An image for Hashicorp's Sentinel https://ww…   3                    [OK]
fredboat/sentinel                      https://github.com/FredBoat/sentinel            3                    
hashicorp/sentinel                                                                     2                    
hashicorp/sentinel-website                                                             2                    
cooperaj/sentinel-broker               Small, use once webservice to hookup a Redis…   1                    [OK]
sentinelofficial/sentinel-ikev2-node                                                   1                    
thalesgroupsm/sentinel_ldk_rte         Docker image with Sentinel LDK Runtime versi…   1                    
gatblau/sentinel-snapshot              Development snapshots for Sentinel              0                    
dashpay/sentinel                       Dash Sentinel                                   0                    [OK]
filecoin/sentinel-visor                This repository is deprecated. New tags will…   0                    
arilot/sentinel                        Argo Sentinel.  An all-powerful toolset for …   0                    [OK]
sentinelone/elasticsearch                                                              0                    
sentinelone/filebeat                                                                   0                    
iandavis/sentinel-airflow-spark                                                        0                    
sentinelofficial/stt1-dvpn-openvpn                                                     0                    
seandooher/sentinel-iot                Sentinel IoT docker image                       0                    
c0ff3e/sentinel-proxy                  to run a sentinel proxy                         0                    
tsuyoshiushio/sentinel                                                                 0                    
sentinelsec/sentinel-rubocop                                                           0                    
sentinelwatch/aws-amplify              AWS Amplify                                     0                    
sentinelsec/sentinel-brakeman                                                          0                    

docker@VM-8-15-ubuntu:~$ docker pull bladex/sentinel-dashboard
Using default tag: latest
latest: Pulling from bladex/sentinel-dashboard
169185f82c45: Pull complete 
4346af5b5a4f: Pull complete 
28ac9c6decc7: Pull complete 
4ca458a82bd5: Pull complete 
Digest: sha256:c596d19cd68b6f140a2230f5f7f16a4203fd3241d3f507e5513de5d28c897b8a
Status: Downloaded newer image for bladex/sentinel-dashboard:latest
docker.io/bladex/sentinel-dashboard:latest

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                                TAG       IMAGE ID       CREATED         SIZE
yuehai-nginx-nacos                                        v0.1      e988bcbf0734   10 days ago     141MB
yuehai-vue                                                v0.1      402b842b0461   10 days ago     142MB
yuehai-java                                               v0.1      6bf178479b40   10 days ago     453MB
nginx                                                     latest    605c77e624dd   14 months ago   141MB
zookeeper                                                 latest    36c607e7b14d   14 months ago   278MB
openjdk                                                   8         e24ac15e052e   14 months ago   526MB
redis                                                     latest    7614ae9453d1   14 months ago   113MB
mysql                                                     latest    3218b38490ce   14 months ago   516MB
rabbitmq                                                  latest    d445c0adc9a5   15 months ago   220MB
ubuntu                                                    latest    ba6acccedd29   17 months ago   72.8MB
nacos/nacos-server                                        latest    bdf60dc2ada3   19 months ago   1.05GB
bladex/sentinel-dashboard                                 latest    aa398704ebd3   2 years ago     147MB
portainer/portainer                                       1.20.2    19d07168491a   4 years ago     74.1MB

docker@VM-8-15-ubuntu:~$ 
```

2. 启动：`docker run -d -p 8849:8858 --name yuehai-sentinel bladex/sentinel-dashboard`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d -p 8849:8858 --name yuehai-sentinel bladex/sentinel-dashboard
56bf2c813dd09fb84c674c652224491cbb5a59386989fd05d19fac9bff25932c

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS             PORTS                                                 NAMES
56bf2c813dd0   bladex/sentinel-dashboard    "java -Djava.securit…"   23 seconds ago   Up 22 seconds      0.0.0.0:8849->8858/tcp, :::8849->8858/tcp             yuehai-sentinel
86486e02b952   portainer/portainer:1.20.2   "/portainer"             11 days ago      Up About an hour   0.0.0.0:9443->9000/tcp, :::9443->9000/tcp             Portainer

docker@VM-8-15-ubuntu:~$ 
```

3. 访问：http://43.138.106.181:8849

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314091152.png)

4. 登录，账号密码都为 sentinel

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314162843.png)

## 3、初始化演示工程

> 需启动 nacos 和 sentinel

### ①、单机版 nacos 配置

1. 我这里换了单机版 nacos

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314110239.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314110811.png)

2. 修改模块 cloudalibaba-config-nacos-client3377 的配置文件 bootstrap.yml

```yaml
# nacos 配置
server:
    port: 3377

spring:
    application:
        name: nacos-config-client
    cloud:
        nacos:
            discovery:
                # Nacos 服务注册中心地址；nginx
                # server-addr: 43.138.106.181:4000
                # 单机 Nacos 服务注册中心地址
                server-addr: 43.138.106.181:8848
            config:
                # Nacos 作为配置中心地址；nginx
                # server-addr: 43.138.106.181:4000
                # 单机 Nacos 作为配置中心地址
                server-addr: 43.138.106.181:8848
                # 指定 yaml 格式的配置
                file-extension: yaml
                # 指定 nacos 组
                # group: DEV_GROUP
                # 指定命名空间，只能输入命名空间的 id
                namespace: abcb1ba7-07aa-4eeb-96d7-a53381cd3958
                # bootstrap.yml 和 application.yml 结合起来就是：
                # ${spring.application.name}-${spring.profile.active}.${spring.cloud.nacos.config.file-extension}
                # 43.138.106.181:8848 下 dev 命名空间下的的：nacos-config-client-info.yaml
```

3. 修改模块 cloudalibaba-config-nacos-client3377 的业务类 ConfigClientController

```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/1 14:30
 *
 * { @RefreshScope }：配置动态刷新
 */

@RestController
@RefreshScope
public class ConfigClientController {

    @Value("${name}")
    private String name;

    @GetMapping("/getConfig")
    public JsonResult getConfig(){
        return JsonResult.success("name：" + name);
    }

}
```

4. 访问测试：http://localhost:3377/getConfig

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314110837.png)

### ②、新建模块 cloudalibaba-sentinel-server8401

1. 新建模块 cloudalibaba-sentinel-server8401

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314110943.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-sentinel-server8401</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        
        <!--SpringCloud ailibaba sentinel 熔断与限流 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <!--SpringCloud ailibaba sentinel-datasource-nacos 后续做持久化用到-->
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-nacos</artifactId>
        </dependency>
    
        <!-- openfeign 服务调用 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 8401

# spring 配置
spring:
    application:
        # 服务名称 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
        name: cloudalibaba-sentinel-server
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
        # sentinel 配置
        sentinel:
            transport:
                # 指定 sentinel dashboard 控制台地址
                dashboard: 43.138.106.181:8849
                # 指定本项目和控制台通信的 IP，若不配置，会自动选择一个 IP 注册
                # client-ip: 127.0.0.1
                # 指定本项目和控制台通信的端口，默认值 8719；若不配置，会自动扫猫从 8719 开始扫猫，依次 +1，直到找到未被占用的端口
                port: 8849
                # 心跳发送周期，默认值 null；但在 SimpleHttpHeartbeatSender 会用默认值 10秒
                # heartbeat-interval-ms: 10000

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: "*"
```

4. 修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class SentinelServer8401 {

    public static void main(String[] args) {
        SpringApplication.run(SentinelServer8401.class, args);
    }

}
```

5. 创建业务类

```java
package com.yuehai.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/14 12:38
 */

@RestController
public class FlowLimitController {

    @GetMapping("/testA")
    public String testA(){
        return "------testA";
    }

    @GetMapping("/testB")
    public String testB(){
        return "------testB";
    }

}
```

6. 启动微服务 nacos 与 sentinel
7. 查看 sentienl 控制台（此时没有本项目显示），访问一下接口：http://localhost:8401/testA，再次查看 sentienl 控制台

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230314170038.png)

8. 虽然这里显示我的项目机器，但是监控什么的是没有的，因为项目是在内网运行的，所以项目可以访问到 sentinel，但是 sentinel 访问不到这个项目，我的解决办法是吧项目打个包部署到服务器上

### ③、修改模块 cloudalibaba-sentinel-server8401，部署到服务器

1. 修改 pom 文件，增加 maven 打包插件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-sentinel-server8401</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        
        <!--SpringCloud ailibaba sentinel 熔断与限流 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <!--SpringCloud ailibaba sentinel-datasource-nacos 后续做持久化用到-->
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-nacos</artifactId>
        </dependency>
    
        <!-- openfeign 服务调用 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该Main Class为全局的唯一入口 -->
                    <mainClass>com.yuehai.SentinelServer8401</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal><!--可以把依赖的包都打包到生成的Jar包中-->
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

2. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 8401

# spring 配置
spring:
    application:
        # 服务名称 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
        name: cloudalibaba-sentinel-server
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
        # sentinel 配置
        sentinel:
            transport:
                # 指定 sentinel dashboard 控制台地址
                dashboard: 43.138.106.181:8849
                # 指定本项目和控制台通信的 IP，若不配置，会自动选择一个 IP 注册
                client-ip: 43.138.106.181
                # 指定本项目和控制台通信的端口，默认值 8719；若不配置，会自动扫猫从 8719 开始扫猫，依次 +1，直到找到未被占用的端口
                port: 12001
                # 心跳发送周期，默认值 null；但在 SimpleHttpHeartbeatSender 会用默认值 10秒
                heartbeat-interval-ms: 10000

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: "*"
```

3. 在 maven 中打包

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315092747.png)

4. 将打包后的 jar 包改名为 cloudalibaba-sentinel-server8401.jar，并上传到服务器的 /home/docker/docker/VOLUME/java/jar/ 目录下
5. 启动 docker 容器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar
7f4d76195e6feeab51b24c711d4d9faa93dcd4f1f080657b7b7ef3f367132161

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                                                                        NAMES
7f4d76195e6f   openjdk:8                    "java -jar /usr/src/…"   9 seconds ago   Up 8 seconds   0.0.0.0:12001->12001/tcp, :::12001->12001/tcp, 0.0.0.0:12000->8401/tcp, :::12000->8401/tcp   java-cloud-sentinel
97b24f34e6cd   bladex/sentinel-dashboard    "java -Djava.securit…"   17 hours ago    Up 17 hours    8719/tcp, 0.0.0.0:8849->8858/tcp, :::8849->8858/tcp                                          sentinel
c7641a57950f   nacos/nacos-server:latest    "bin/docker-startup.…"   25 hours ago    Up 21 hours    0.0.0.0:8848->8848/tcp, :::8848->8848/tcp                                                    nacosStandalone
86486e02b952   portainer/portainer:1.20.2   "/portainer"             11 days ago     Up 22 hours    0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                                    Portainer

docker@VM-8-15-ubuntu:~$ docker logs 7f4d76195e6f

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.2.2.RELEASE)

2023-03-15 01:30:20.399  INFO 1 --- [           main] com.yuehai.SentinelServer8401            : No active profile set, falling back to default profiles: default
2023-03-15 01:30:21.318  WARN 1 --- [           main] o.s.boot.actuate.endpoint.EndpointId     : Endpoint ID 'nacos-discovery' contains invalid characters, please migrate to a valid format.
2023-03-15 01:30:21.593  WARN 1 --- [           main] o.s.boot.actuate.endpoint.EndpointId     : Endpoint ID 'service-registry' contains invalid characters, please migrate to a valid format.
2023-03-15 01:30:21.815  INFO 1 --- [           main] o.s.cloud.context.scope.GenericScope     : BeanFactory id=35df7532-e278-33be-a8a8-2afb807ce8e0
2023-03-15 01:30:22.306  INFO 1 --- [           main] trationDelegate$BeanPostProcessorChecker : Bean 'spring.cloud.sentinel-com.alibaba.cloud.sentinel.SentinelProperties' of type [com.alibaba.cloud.sentinel.SentinelProperties] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
2023-03-15 01:30:22.607  INFO 1 --- [           main] trationDelegate$BeanPostProcessorChecker : Bean 'com.alibaba.cloud.sentinel.custom.SentinelAutoConfiguration' of type [com.alibaba.cloud.sentinel.custom.SentinelAutoConfiguration$$EnhancerBySpringCGLIB$$8b56057] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
2023-03-15 01:30:23.070  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8401 (http)
2023-03-15 01:30:23.085  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-03-15 01:30:23.085  INFO 1 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.29]
2023-03-15 01:30:23.155  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-03-15 01:30:23.155  INFO 1 --- [           main] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 2727 ms
2023-03-15 01:30:23.171  INFO 1 --- [           main] c.a.c.s.SentinelWebAutoConfiguration     : [Sentinel Starter] register Sentinel CommonFilter with urlPatterns: [/*].
2023-03-15 01:30:23.917  WARN 1 --- [           main] c.n.c.sources.URLConfigurationSource     : No URLs will be polled as dynamic configuration sources.
2023-03-15 01:30:23.917  INFO 1 --- [           main] c.n.c.sources.URLConfigurationSource     : To enable URLs as dynamic configuration sources, define System property archaius.configurationSource.additionalUrls or make config.properties available on classpath.
2023-03-15 01:30:23.927  WARN 1 --- [           main] c.n.c.sources.URLConfigurationSource     : No URLs will be polled as dynamic configuration sources.
2023-03-15 01:30:23.929  INFO 1 --- [           main] c.n.c.sources.URLConfigurationSource     : To enable URLs as dynamic configuration sources, define System property archaius.configurationSource.additionalUrls or make config.properties available on classpath.
2023-03-15 01:30:24.152  INFO 1 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'
2023-03-15 01:30:24.393  INFO 1 --- [           main] o.s.s.c.ThreadPoolTaskScheduler          : Initializing ExecutorService
2023-03-15 01:30:24.671  INFO 1 --- [           main] o.s.b.a.e.web.EndpointLinksResolver      : Exposing 19 endpoint(s) beneath base path '/actuator'
2023-03-15 01:30:24.800  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8401 (http) with context path ''
2023-03-15 01:30:24.978  INFO 1 --- [           main] c.a.c.n.registry.NacosServiceRegistry    : nacos registry, cloudalibaba-sentinel-server 172.17.0.4:8401 register finished
2023-03-15 01:30:24.986  INFO 1 --- [           main] com.yuehai.SentinelServer8401            : Started SentinelServer8401 in 6.475 seconds (JVM running for 7.193)

docker@VM-8-15-ubuntu:~$ 
```

6. 再次进入 sentinel 控制台查看：http://43.138.106.181:8849/#/dashboard/app/cloudalibaba-sentinel-server

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315093513.png)

7. 多次请求服务接口：http://43.138.106.181:12000/testA
8. 查看 sentinel 控制台实时监控：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315093624.png)

## 4、流控规则

### ①、基本介绍

1. 资源名：唯一名称，默认请求路径
2. 针对来源：Sentinel 可以针对调用者进行限流，填写微服务名，默认 default (不区分来源)
3. 阈值类型/单机阈值：
	1. QPS(每秒钟的请求数量)：当调用该 api 的 QPS 达到阈值的时候，进行限流。
	2. 线程数：当调用该 api 的线程数达到阈值的时候，进行限流
4. 是否集群：不需要集群
5. 流控模式：
	1. 直接：api 达到限流条件时，直接限流
	2. 关联：当关联的资源达到阈值时，就限流自己
6. 链路：只记录指定链路上的流量（指定资源从入口资源进来的流量，如果达到阈值，就进行限流)【api级别的针对来源】
7. 流控效果：
	1. 快速失败：直接失败
	2. Warm Up：根据 codeFactor (冷加载因子，默认3)的值，从阈值 /codeFactor，经过预热时长，才达到设置的 QPS 阈值
	3. 排队等待：匀速排队，让请求以匀速的速度通过，阈值类型必须设置为 QPS，否则无效

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315095838.png)

### ②、流控模式

#### Ⅰ、 直接（默认）

1. 默认模式
2. 下图表示 1 秒钟内查询 1 次就是 OK，若超过次数 1，就直接：快速失败，报默认错误，抛异常：Blocked by Sentinel (flow limiting)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315100635.png)

3. 思考：直接调用默认报错信息，技术方面OK，但是是否应该有我们自己的后续处理？类似有个 fallback 的兜底方法？

#### Ⅱ、关联

1. 是什么：
	1. 当关联的资源达到阈值时，就限流自己
	2. 当与 A 关联的资源 B 达到阀值后，就限流 A 自己
	3. B 惹事，A 挂了
2. 配置 A：当关联资源 /testB 的 qps 阀值超过 1 时，就限流 /testA 的 Rest 访问地址，<font color="#ff0000">当关联资源（/testB）到阈值后限制配置好的资源名（/testA）</font>

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315101857.png)

3. 模拟并发密集访问 testB，运行后发现 testA 挂了（testB 还是好的）

#### Ⅲ、链路

1. 只针对从指定链路访问到本资源的请求做统计，判断是否超过阈值。
2. 假设有讲个请求：`test1/common`、`test2/common`，只希望统计 `test1/common` 从 test1 到 common 的请求，可以这样设置：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315103524.png)

### ③、流控效果

#### Ⅰ、 快速失败

1. 直接失败，抛出异常：Blocked by Sentinel (flow limiting)
2. 源码：com.alibaba.csp.sentinel.slots.block.flow.controller.DefaultController

#### Ⅱ、Warm Up（预热/冷启动方式）

1. 公式：默认 coldFactor 为 3，即请求 QPS 从 threshold（阈值） / 3 开始，经预热时长逐渐升至设定的 QPS 阈值。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315112115.png)

2. 官网：限流/冷启动：https://github.com/alibaba/Sentinel/wiki/%E9%99%90%E6%B5%81---%E5%86%B7%E5%90%AF%E5%8A%A8
3. 应用场景：如：秒杀系统在开启的瞬间，会有很多流量上来，很有可能把系统打死，预热方式就是把为了保护系统，可慢慢的把流量放进来，慢慢的把阀值增长到设置的阀值。

#### Ⅲ、排队等待

1. 匀速排队，让请求以均匀的速度通过，阀值类型必须设成 QPS，否则无效。
2. 设置含义：/testA 每秒 1 次请求，超过的话就排队等待，等待的超时时间为 20000 毫秒。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315123536.png)

3. 官网：https://github.com/alibaba/Sentinel/wiki/%E6%B5%81%E9%87%8F%E6%8E%A7%E5%88%B6

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315123613.png)

## 5、降级规则

> 官网：https://github.com/alibaba/Sentinel/wiki/%E7%86%94%E6%96%AD%E9%99%8D%E7%BA%A7

### ①、基本介绍

1. RT（平均响应时间，秒级）
	1. 平均响应时间<font color="#0070c0">超出阈值</font>且<font color="#0070c0">在时间窗口内通过的请求>=5</font>，两个条件同时满足后触发降级
	2. 窗口期过后关闭断路器
	3. RT 最大 4900（更大的需要通过-Dcsp.sentinel.statistic.max.rt=XXXX才能生效）
2. 异常比列（秒级）
	1. <font color="#0070c0">QPS >= 5</font>且<font color="#0070c0">异常比例（秒级统计）超过阈值</font>时，触发降级
	2. 时间窗口结束后，关闭降级
3. 异常数（分钟级）
	1. <font color="#0070c0"> 异常数（分钟统计）超过阈值</font>时，触发降级
	2. 时间窗口结束后，关闭降级
4. Sentinel 熔断降级会在调用链路中某个资源出现不稳定状态时（例如调用超时或异常比例升高），对这个资源的调用进行限制，让请求快速失败，避免影响到其它的资源而导致级联错误。
5. 当资源被降级后，在接下来的降级时间窗口之内，对该资源的调用都自动熔断（默认行为是抛出 DegradeException）。
6. Sentinel 的断路器是<font color="#ff0000">没有</font><font color="#0070c0">半开</font>状态的：半开的状态系统自动去检测是否请求有异常，没有异常就关闭断路器恢复使用，有异常则继续打开断路器不可用。具体可以参考 Hystrix

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315124805.png)

### ②、熔断策略

#### Ⅰ、慢调用比例

1. 慢调用比例：`RT`
2. 当资源的响应时间超过<font color="#0070c0">最大 RT</font>（以 ms 为单位，最大 RT 即最大响应时间）之后，资源进入准降级状态。如果接下来 1s 内<font color="#0070c0">持续进入 5 个请求</font>（最小请求数），它们的 RT 都持续超过这个阈值，那么在接下来的<font color="#0070c0">熔断时长</font>之内，就会对这个方法进行服务熔断。
3.  1s 内持续进入的请求数 = 最小请求数 / 比例阈值

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315131125.png)

4. 注意 Sentinel 默认统计的 RT 上限是 4900 ms，超出此阈值的都会算作 4900 ms，若需要变更此上限可以通过启动配置项 `-Dcsp.sentinel.statistic.max. rt=xxx` 来配置。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315125654.png)

#### Ⅱ、异常比例

1. 当资源的每秒请求数大于等于<font color="#0070c0">最小请求数</font>，并且异常总数占通过量的比例超过<font color="#0070c0">比例阈值</font>时，资源进入熔断状态

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315131815.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315131828.png)

#### Ⅲ、异常数

1. 当资源近<font color="#ff0000"> 1 分钟</font>的异常数目超过阈值（异常数）之后会进行服务熔断。
2. 注意由于统计熔断时长是分钟级别的，若熔断时长小于 60s，则结束熔断状态后仍可能再次进入熔断状态，故<font color="#ff0000">熔断时长一定要大于等于60秒</font>

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315132007.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315132023.png)

## 6、热点规则

> 官网：https://github.com/alibaba/Sentinel/wiki/%E7%83%AD%E7%82%B9%E5%8F%82%E6%95%B0%E9%99%90%E6%B5%81

### ①、基本介绍

1. 何为热点：热点即经常访问的数据，很多时候我们希望统计或者限制某个热点数据中访问频次最高的 TopN 数据，并对其访问进行限流或者其它操作
2. 承上启下复习 start：
	1. 兜底方法：分为<font color="#0070c0">系统默认</font>和<font color="#0070c0">客户自定义</font>两种
	2. 之前的 case，限流出问题后，都是用 sentinel 系统默认的提示：Blocked by Sentinel (flow limiting)
	3.  我们能不能自定义？类似 hystrix，某个方法出问题了，就找对应的兜底降级方法？
	4. 结论：从 `@HystrixCommand` 到 `@SentinelResource`

### ②、代码修改

1. 修改 8401 的业务类，增加 testHotKey 和 dealHandler_testHotKey 方法

```java
    /**
     * { @SentinelResource } 用于定义资源，并提供可选的异常处理和fallback配置项，其主要参数如下：
     * value：资源名称
     * entryType：entry 类型，标记流量的方向，取值 IN/OUT，默认是OUT
     * blockHandler：处理 BlockException 的函数名称，函数要求：
     *      1、必须是 public
     *      2、返回类型参数与原方法一致
     *      3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置blockHandlerclass，并指定blockHandlerClass里面的方法。
     * blockHandlerClass：存放 blockHandler 的类，对应的处理函数必须 static 修饰。
     * fallback：用于在抛出异常的时候提供 fallback 处理逻辑。fallback 函数可以针对所有类型的异常(除了exceptionsToIgnore里面排除掉的异常类型)进行处理。函数要求:
     *      1、返回类型与原方法—致
     *      2、参数类型需要和原方法相匹配
     *      3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置fa11backc1ass，并指定fallbackClass里面的方法。
     * fallbackClass：存放 fallback 的类。对应的处理函数必须static修饰。
     * defaultFallback：用于通用的 fallback逻辑。默认fallback函数可以针对所有类型的异常进行处理。若同时配置了 fallback和defaultFallback，以fallback为准。函数要求:
     *      1、返回类型与原方法—致
     *      2、方法参数列表为空，或者有一个Throwab1e类型的参数。
     *      3、默认需要和原方法在同一个类中。若希望使用其他类的函数，可配置fa11backc1ass，并指定fa1lbackclass里面的方法。
     * exceptionsTolgnore：指定排除掉哪些异常。排除的异常不会计入异常统计，也不会进入fallback逻辑，而是原样抛出。
     * exceptionsToTrace：需要 trace 的异常
     */
    @SentinelResource(value = "testHotKey", blockHandler = "dealHandler_testHotKey")
    @GetMapping("/testHotKey")
    public JsonResult testHotKey(@RequestParam(value = "p1", required = false) String p1,
                                 @RequestParam(value = "p2", required = false) String p2){
        return JsonResult.success("热点搜索为：" + p1 + "，" + p2);
    }
    public JsonResult dealHandlerTestHotKey(String p1, String p2, BlockException exception){
        return JsonResult.error("500", "热点信息【" + p1 + "，" + p2 + "】请求失败：" + exception);
    }
```

2. 将项目打包，部署到服务器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`
3. 访问测试：http://43.138.106.181:12000/testHotKey?p1=%E6%9C%88%E6%B5%B7&p2=%E8%A8%80

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315151550.png)

### ③、sentinel 配置

1. 资源名：`@SentinelResource` 注解的 value 值
2. 限流模式：只支持 QPS 模式，固定写死了（这才叫热点）
3. 参数索引：`@SentinelResource`  注解的方法参数索引，0 代表第一个参数，1 代表第二个参数，以此类推
4. 单机阀值以及统计窗口时长表示在此窗口时间超过阀值就限流。
5. 下图就是第一个参数有值的话，1 秒的 QPS 为 2，超过就限流，限流后调用 `dealHandler_testHotKey` 支持方法。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152123.png)

### ④、测试

1. 两个参数都传，正常访问：http://43.138.106.181:12000/testHotKey?p1=%E6%9C%88%E6%B5%B7&p2=%E8%A8%80

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152608.png)

2. 两个参数都传，1 秒内访问超过 2 次：：http://43.138.106.181:12000/testHotKey?p1=%E6%9C%88%E6%B5%B7&p2=%E8%A8%80

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152513.png)

3. 只传第一个参数，正常访问：http://43.138.106.181:12000/testHotKey?p1=%E6%9C%88%E6%B5%B7

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152706.png)

4. 只传第一个参数，1 秒内访问超过 2 次：http://43.138.106.181:12000/testHotKey?p1=%E6%9C%88%E6%B5%B7

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152807.png)

5. 只传第二个参数，正常访问：http://43.138.106.181:12000/testHotKey?p2=%E6%9C%88%E6%B5%B7

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152849.png)

6. 只传第二个参数，1 秒内访问超过 2 次，不会被限流：http://43.138.106.181:12000/testHotKey?p2=%E6%9C%88%E6%B5%B7

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315152855.png)

### ⑤、参数例外项

1. 上述案例演示了第一个参数的 QPS 超过 1 秒 2 次点击后马上被限流
2. 我们期望当参数它是某个特殊值时，它的限流值和平时不一样，假如当参数的值为 <font color="#ff0000">言</font> 时，它的阈值可以达到 200
3. 热点参数的注意点，<font color="#ff0000">参数必须是基本类型或者 String</font>
4. 配置：点击高级选项，设置<font color="#0070c0">参数值</font>和<font color="#0070c0">限流阈值</font>后，点击<font color="#ff0000">添加</font>

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315145841.png)

5. 再次测试：http://43.138.106.181:12000/testHotKey?p1=%E8%A8%80

### ⑥、其它：运行时异常

1. `@SentinelResource`：处理的是 Sentinel 控制台配置的违规情况，有 `blockHandler` 方法配置的兜底处理；
2. `int age = 10/0` 这个是 java 运行时报出的运行时异常 `RunTimeException`，`@SentinelResource` 不管
3. 总结：`@SentinelResource` 主管配置出错，运行出错该走异常走异常

## 7、系统规则

> 官网：https://github.com/alibaba/Sentinel/wiki/%E7%B3%BB%E7%BB%9F%E8%87%AA%E9%80%82%E5%BA%94%E9%99%90%E6%B5%81

1. 系统保护规则是从应用级别的入口流量进行控制，从单台机器的 load、CPU使用率、平均RT、入口 QPS 和并发线程数等几个维度监控应用指标，让系统尽可能跑在最大吞吐量的同时保证系统整体的稳定性。
2. 系统保护规则是应用整体维度的，而不是资源维度的，并且仅对入口流量生效。入口流量指的是进入应用的流量（ EntryType.IN )，比如 Web 服务或 Dubbo 服务端接收的请求，都属于入口流量。
3. 系统规则支持以下的模式:
	1. Load 自适应（仅对 Linux/Unix-like 机器生效）：系统的 load1 作为启发指标，进行自适应系统保护。当系统 load1 超过设定的启发值，且系统当前的并发线程数超过估算的系统容量时才会触发系统保护（BBR 阶段）。系统容量由系统的 `maxQps * minRt` 估算得出。设定参考值一般是 `CPU cores * 2.5`。
	2. 平均 RT：当单台机器上所有入口流量的平均 RT 达到阈值即触发系统保护，单位是毫秒。
	3. 并发线程数：当单台机器上所有入口流量的并发线程数达到阈值即触发系统保护。
	4. 入口 QPS：当单台机器上所有入口流量的 QPS 达到阈值即触发系统保护。
	5. CPU usage（1.5.0+ 版本）：当系统 CPU 使用率超过阈值即触发系统保护（取值范围 0.0-1.0），比较灵敏。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315154107.png)

## 8、`@SentinelResource` 注解

 `@SentinelResource` 注解参数介绍：

| 属性               | 作用                                                                                                                                                                                                                                                                                                                                                |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value              | 资源名称                                                                                                                                                                                                                                                                                                                                            |
| entryType          | entry 类型，标记流量的方向，取值 IN/OUT，默认是OUT                                                                                                                                                                                                                                                                                                  |
| blockHandler       | 处理 BlockException 的函数名称，只负责在 sentinel 里面配置的降级限流，函数要求：<br />1、必须是 public<br />2、返回类型参数与原方法一致<br/>3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置blockHandlerclass，并指定blockHandlerClass里面的方法。                                                                                                                           |
| blockHandlerClass  | 存放 blockHandler 的类，对应的处理函数必须 static 修饰。                                                                                                                                                                                                                                                                                            |
| fallback           | 用于在抛出异常的时候提供 fallback 处理逻辑。fallback 函数可以针对所有类型的异常(除了exceptionsToIgnore里面排除掉的异常类型)进行处理。函数要求: <br>1、返回类型与原方法—致<br />2、参数类型需要和原方法相匹配<br />3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置fallbackClass，并指定fallbackClass里面的方法。                       |
| fallbackClass      | 存放 fallback 的类。对应的处理函数必须static修饰。                                                                                                                                                                                                                                                                                                  |
| defaultFallback    | 用于通用的 fallback逻辑。默认fallback函数可以针对所有类型的异常进行处理。若同时配置了 fallback和defaultFallback，以fallback为准。函数要求: <br />1、返回类型与原方法—致<br/>2、方法参数列表为空，或者有一个Throwab1e类型的参数。<br />3、默认需要和原方法在同一个类中。若希望使用其他类的函数，可配置fa11backc1ass，并指定fa1lbackclass里面的方法。 |
| exceptionsTolgnore | 指定排除掉哪些异常。排除的异常不会计入异常统计，也不会进入fallback逻辑，而是原样抛出。                                                                                                                                                                                                                                                              |
| exceptionsToTrace  | 需要 trace 的异常                                                                                                                                                                                                                                                                                                                                   |

### ①、按资源名称限流 + 后续处理

1. 创建新业务类 RateLimitController

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/15 16:09
 */

@RestController
public class RateLimitController {

    @GetMapping("/byResource")
    @SentinelResource(value = "byResource",blockHandler = "handleException")
    public JsonResult byResource(){
        return JsonResult.success("按资源名称限流测试OK");
    }
    public JsonResult handleException(BlockException exception){
        return JsonResult.error("error", "服务不可用：" + exception);
    }

}
```

2. 打包部署到服务器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`
3. 配置流控规则：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315162115.png)

4. 流控规则配置和代码关系

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315162442.png)

5. 1 秒钟内查询次数大于 1，就会执行我们自定义限流：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315162613.png)

6. <font color="#ff0000">此时关闭微服务 8401</font>
7. Sentinel 控制台里的流控规则消失了

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315162802.png)

### ②、按照 Url 地址限流 + 后续处理

1. 通过访问的 URL 来限流，会返回 Sentinel 自带默认的限流处理信息
2. 修改业务类 RateLimitController

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.yuehai.entities.Payment;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author 月海
 * @create 2023/3/15 16:09
 */

@RestController
public class RateLimitController {

    @GetMapping("/byResource")
    @SentinelResource(value = "byResource",blockHandler = "handleException")
    public JsonResult byResource(){
        return JsonResult.success("按资源名称限流测试 OK");
    }
    public JsonResult handleException(BlockException exception){
        return JsonResult.error("error", "服务不可用：" + exception);
    }

    @GetMapping("/rateLimit/byUrl")
    @SentinelResource(value = "byUrl")
    public JsonResult byUrl(){
        return JsonResult.success("按 url 限流测试 OK");
    }

}
```

3. 打包部署到服务器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`
4. 配置流控规则：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315163545.png)

5. 1 秒钟内查询次数大于 1，就会执行 Sentinel 自带默认的限流处理信息

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315163659.png)

### ③、上面兜底方案面临的问题

1. 系统默认的，没有体现我们自己的业务要求。
2. 依照现有条件，我们自定义的处理方法又和业务代码耦合在一块，不直观。
3. 每个业务方法都添加一个兜底的，那代码膨胀加剧。
4. 全局统一的处理方法没有体现。

### ④、<font color="#ff0000">客户自定义限流处理逻辑</font>

1. 创建 CustomerBlockHandler 类用于自定义限流处理逻辑，在其中创建静态方法

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230315164723.png)

```java
package com.yuehai.myHandeler;

import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.yuehai.utils.JsonResult;

/**
 * @author 月海
 * @create 2023/3/15 16:45
 */
public class CustomerBlockHandler {

    /**
     * 自定义通用的限流处理 handleException
     */
    public static JsonResult handleException(BlockException exception){
        return JsonResult.success("自定义的限流处理信息：handleException");
    }

    /**
     * 自定义通用的限流处理 handleException2
     */
    public static JsonResult handleException2(BlockException exception){
        return JsonResult.success("自定义的限流处理信息：handleException2");
    }

}
```

2. 修改 RateLimitController，新增方法

```java
/**
     * 使用自定义通用的限流处理逻辑
     * blockHandlerClass = CustomerBlockHandler.class：使用 CustomerBlockHandler 类
     * blockHandler = "handleException2：使用  CustomerBlockHandler 类中的 handleException2 方法
     */
    @GetMapping("/rateLimit/customerBlockHandler")
    @SentinelResource(value = "customerBlockHandler", blockHandlerClass = CustomerBlockHandler.class, blockHandler = "handleException2")
    public JsonResult customerBlockHandler(){
        return JsonResult.success("按客戶自定义限流处理逻辑");
    }
```

3. 打包部署到服务器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`
4. 配置流控规则：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316082921.png)

5. 1 秒钟内查询次数大于 1，就会执行自定义限流处理信息：http://43.138.106.181:12000/rateLimit/customerBlockHandler

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316083108.png)

6. 配置联系：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316083634.png)

## 9、服务熔断功能

> sentinel 整合 ribbon + openFeign + fallback

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316094720.png)

### ①、负载均衡服务调用 Ribbon 系列

#### Ⅰ、提供者 9003 / 9004

1. 新建 cloudalibaba-provider-payment9003/9004，两个一样的做法
2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-provider-payment9003</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
    </dependencies>

	<build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该Main Class为全局的唯一入口 -->
                    <mainClass>com.yuehai.NacosPayment9003</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal><!--可以把依赖的包都打包到生成的Jar包中-->
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 9003

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloudalibaba-provider-payment9003
        name: nacos-payment-provider
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: '*'
```

4. 修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务提供者支付模块 cloudalibaba-provider-payment9003
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class NacosPayment9003 {

    public static void main(String[] args) {
        SpringApplication.run(NacosPayment9003.class, args);
    }

}
```

5. 创建业务类

```java
package com.yuehai.controller;

import com.yuehai.entities.Payment;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

/**
 * @author 月海
 * @create 2023/3/16 9:21
 */

@RestController
public class PaymentController {

    @Value("${server.port}")
    private String serverPort;

    @GetMapping(value = "/paymentSQL/{id}")
    public JsonResult paymentSql(@PathVariable("id") Long id){
        HashMap<Long,Payment> hashMap = new HashMap<>(3);
        hashMap.put(1L,new Payment(1L,"28a8c1e3bc2742d8848569891fb42181"));
        hashMap.put(2L,new Payment(2L,"bba8c1e3bc2742d8848569891ac32182"));
        hashMap.put(3L,new Payment(3L,"6ua8c1e3bc2742d8848569891xt92183"));

        Payment payment = hashMap.get(id);
        return JsonResult.success("查询成功，结果为：" + payment + "，端口号为：" + serverPort );
    }

}
```

6. 访问测试：http://localhost:9003/paymentSQL/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316093646.png)

7. 访问测试：http://localhost:9004/paymentSQL/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316093700.png)

#### Ⅱ、消费者 84

##### （1）、基础配置

1. 新建模块 cloudalibaba-consumer-nacos-order84

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316093851.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-consumer-nacos-order84</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
    
        <!--SpringCloud ailibaba sentinel 熔断与限流 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该Main Class为全局的唯一入口 -->
                    <mainClass>com.yuehai.NacosOrder84</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal><!--可以把依赖的包都打包到生成的Jar包中-->
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 84

# spring 配置
spring:
    application:
        # 服务名称 微服务消费者模块 cloudalibaba-consumer-nacos-order84
        name: nacos-order-consumer
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
        # sentinel 配置
        sentinel:
            transport:
                # 指定 sentinel dashboard 控制台地址
                dashboard: 43.138.106.181:8849
                # 指定本项目和控制台通信的 IP，若不配置，会自动选择一个 IP 注册
                client-ip: 43.138.106.181
                # 指定本项目和控制台通信的端口，默认值 8719；若不配置，会自动扫猫从 8719 开始扫猫，依次 +1，直到找到未被占用的端口
                port: 12003
                # 心跳发送周期，默认值 null；但在 SimpleHttpHeartbeatSender 会用默认值 10秒
                heartbeat-interval-ms: 10000

# 消费者将要去访问的微服务名称（注册成功进 nacos 的微服务提供者），这个不是配置项，只是为了方便获取值
service-url:
    nacos-user-service: http://nacos-payment-provider

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: '*'
```

4. 修改主启动类

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务消费者模块 cloudalibaba-consumer-nacos-order84
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class NacosOrder84 {

    public static void main(String[] args) {
        SpringApplication.run(NacosOrder84.class, args);
    }

}
```

5. 创建 RestTemplate 类

```java
package com.yuehai.config;

import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * @author 月海
 * @create 2023/3/1 13:08
 */

@Configuration
public class ApplicationContextBean {

    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate(){
        return new RestTemplate();
    }

}
```

##### （2）、`@SentinelResource` 没有任何配置，原生 error 页面

1. 创建业务类

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/16 9:58
 */
public class CircleBreakerController {

    /**
     * Spring 框架提供的一个工具类，可远程调用一个 HTTP 接口
     */
    @Resource
    private RestTemplate restTemplate;

    /**
     * 获取服务名
     */
    @Value("${service-url.nacos-user-service}")
    private String serverURL;

    @RequestMapping("/consumer/fallback/{id}")
    @SentinelResource(value = "fallback")
    public JsonResult fallback(@PathVariable Long id){
        // 通过服务名访问微服务提供者的指定接口，传递参数
        JsonResult result = restTemplate.getForEntity(serverURL + "/paymentSQL/" + id, JsonResult.class).getBody();

        if (id >= 4) {
            throw new IllegalArgumentException ("IllegalArgumentException，非法参数异常....");
        }

        return JsonResult.success(result);
    }

}

```

2. 正常访问：http://localhost:84/consumer/fallback/1，刷新后端口号会改变，说明负载均衡已启用

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316103509.png)

3. 错误访问：http://localhost:84/consumer/fallback/5

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316103535.png)

4. 本例 sentinel 无配置

##### （3）、`@SentinelResource` 只配置 `fallback`

1. 配置：`@SentinelResource(value = "fallback", fallback = "handlerFallback")`，新增 handlerFallback 方法

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.yuehai.entities.Payment;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/16 9:58
 */

@RestController
public class CircleBreakerController {

    /**
     * Spring 框架提供的一个工具类，可远程调用一个 HTTP 接口
     */
    @Resource
    private RestTemplate restTemplate;

    /**
     * 获取服务名
     */
    @Value("${service-url.nacos-user-service}")
    private String serverURL;

	/**
     * { @SentinelResource } 用于定义资源，并提供可选的异常处理和 fallback 配置项
     * value：资源名称
     * fallback：用于在抛出异常的时候提供 fallback 处理逻辑。fallback 函数可以针对所有类型的异常(除了exceptionsToIgnore里面排除掉的异常类型)进行处理。函数要求:
     *      1、返回类型与原方法—致
     *      2、参数类型需要和原方法相匹配
     *      3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置fa11backc1ass，并指定fallbackClass里面的方法。
     */
    @GetMapping("/consumer/fallback/{id}")
    @SentinelResource(value = "fallback", fallback = "handlerFallback")
    public JsonResult fallback(@PathVariable Long id){
        // 通过服务名访问微服务提供者的指定接口，传递参数
        JsonResult result = restTemplate.getForEntity(serverURL + "/paymentSQL/" + id, JsonResult.class).getBody();

        if (id >= 4) {
            throw new IllegalArgumentException ("IllegalArgumentException，非法参数异常....");
        }

        return JsonResult.success(result);
    }
    public JsonResult handlerFallback(@PathVariable  Long id,Throwable e) {
        Payment payment = new Payment(id,"null");
        return JsonResult.error("444", "兜底异常 handlerFallback，结果为：" + payment + "，\n异常为：" + e.getMessage());
    }

}
```

2. 正常访问：http://localhost:84/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316105605.png)

3. 错误访问：http://localhost:84/consumer/fallback/5

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316105533.png)

4. 本例 sentinel 无配置

##### （4）、`@SentinelResource` 只配置 `blockHandler`

1. 配置：`@SentinelResource(value = "fallback", blockHandler = "blockHandler")`，新增 blockHandler 方法

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.yuehai.entities.Payment;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.Map;

/**
 * @author 月海
 * @create 2023/3/16 9:58
 */

@RestController
public class CircleBreakerController {

    /**
     * Spring 框架提供的一个工具类，可远程调用一个 HTTP 接口
     */
    @Resource
    private RestTemplate restTemplate;

    /**
     * 获取服务名
     */
    @Value("${service-url.nacos-user-service}")
    private String serverURL;

    @GetMapping("/test")
    public JsonResult test(){
        return JsonResult.success("test");
    }

    /**
     * { @SentinelResource } 用于定义资源，并提供可选的异常处理和 fallback 配置项
     * value：资源名称
     * blockHandler：处理 BlockException 的函数名称，只负责在 sentinel 里面配置的降级限流，函数要求：
     *      1、必须是 public
     *      2、返回类型参数与原方法一致
     *      3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置blockHandlerclass，并指定blockHandlerClass里面的方法。
     */
    @GetMapping("/consumer/fallback/{id}")
    // @SentinelResource(value = "fallback", fallback = "handlerFallback")
    @SentinelResource(value = "fallback", blockHandler = "blockHandler")
    public JsonResult fallback(@PathVariable Long id){
        // 通过服务名访问微服务提供者的指定接口，传递参数
        // 这里将接收的数据改为 map 的原因是使用 JsonResult 会发生序列化异常，没有找到原因（本地不会报错，放到服务器上就会报错）
        // 返回的全部数据：<200,{msg=ok, data=查询成功，结果为：Payment(id=1, serial=28a8c1e3bc2742d8848569891fb42181)，端口号为：9004, code=200},[Content-Type:"application/json", Transfer-Encoding:"chunked", Date:"Thu, 16 Mar 2023 07:14:07 GMT", Keep-Alive:"timeout=60", Connection:"keep-alive"]>
        // getBody() 为返回的数据
        Map body = restTemplate.getForEntity(serverURL + "/paymentSQL/" + id, Map.class).getBody();

        if (id >= 4) {
            throw new IllegalArgumentException ("IllegalArgumentException，非法参数异常....");
        }

        return JsonResult.success(body.get("data"));
    }
    public JsonResult handlerFallback(@PathVariable  Long id,Throwable e) {
        Payment payment = new Payment(id,"null");
        return JsonResult.error("444", "兜底异常 handlerFallback，结果为：" + payment + "，\n异常为：" + e.getMessage());
    }
    public JsonResult blockHandler(@PathVariable  Long id, BlockException e) {
        Payment payment = new Payment(id,"null");
        return JsonResult.error("444", "限流 blockException，结果为：" + payment + "，\n异常为：" + e.getMessage());
    }

}
```

2. 进入服务器 `/home/docker/docker/VOLUME/java/jar/` 目录，创建脚本文件：`start_cloud.sh`：

```sh
#!/bin/bash

# 删除日志文件
rm /usr/src/myapp/order84.log /usr/src/myapp/payment9003.log /usr/src/myapp/payment9004.log
# 创建日志文件
touch /usr/src/myapp/order84.log /usr/src/myapp/payment9003.log /usr/src/myapp/payment9004.log

# 执行 jar 包
java -jar /usr/src/myapp/payment9003.jar > /usr/src/myapp/payment9003.log &
java -jar /usr/src/myapp/payment9004.jar > /usr/src/myapp/payment9004.log &
java -jar /usr/src/myapp/order84.jar > /usr/src/myapp/order84.log
```

3. 将三个项目打包改名，并上传到服务器：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316152851.png)

4. 启动容器：`docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh`

```bash
docker@VM-8-15-ubuntu:~/docker/VOLUME/java/jar$ docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh
148521b2bb142e1be77709cb503573b342fd066df17f5b9cbeea64ce7d1b9899

docker@VM-8-15-ubuntu:~/docker/VOLUME/java/jar$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                                              NAMES
148521b2bb14   openjdk:8                    "bash /usr/src/myapp…"   6 seconds ago   Up 5 seconds   0.0.0.0:12003->12003/tcp, :::12003->12003/tcp, 0.0.0.0:12002->84/tcp, :::12002->84/tcp, 0.0.0.0:12004->9003/tcp, :::12004->9003/tcp, 0.0.0.0:12005->9004/tcp, :::12005->9004/tcp   java-cloud-sentinel-order
97b24f34e6cd   bladex/sentinel-dashboard    "java -Djava.securit…"   47 hours ago    Up 47 hours    8719/tcp, 0.0.0.0:8849->8858/tcp, :::8849->8858/tcp                                                                                                                                sentinel
c7641a57950f   nacos/nacos-server:latest    "bin/docker-startup.…"   2 days ago      Up 2 days      0.0.0.0:8848->8848/tcp, :::8848->8848/tcp                                                                                                                                          nacosStandalone
86486e02b952   portainer/portainer:1.20.2   "/portainer"             13 days ago     Up 2 days      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                                                                                                                          Portainer

docker@VM-8-15-ubuntu:~/docker/VOLUME/java/jar$ 
```

5. 访问 9003，映射到了 12004：http://43.138.106.181:12004/paymentSQL/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316153155.png)

6. 访问 9004，映射到了 12005：http://43.138.106.181:12005/paymentSQL/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316153210.png)

7. 正常访问 84，映射到了 12002：http://43.138.106.181:12002/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316153441.png)

8. 错误访问 84，映射到了 12002：http://43.138.106.181:12002/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316153537.png)

9. 配置 sentinel 降级规则：1 秒内异常超过 2 次后，断路器打开，断电跳闸 70 秒，系统被保护

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316154006.png)

10. 1 秒内进行两次错误请求：http://43.138.106.181:12002/consumer/fallback/5，成功熔断，调用 `blockHandler` 方法

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316154106.png)

##### （5）、`@SentinelResource` 配置 `fallback` 和  `blockHandler`

1. `fallback` 和  `blockHandler` 一起配置：`@SentinelResource(value = "fallback", fallback = "handlerFallback", blockHandler = "blockHandler")`

```java
package com.yuehai.controller;

import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.yuehai.entities.Payment;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.Map;

/**
 * @author 月海
 * @create 2023/3/16 9:58
 */

@RestController
public class CircleBreakerController {

    /**
     * Spring 框架提供的一个工具类，可远程调用一个 HTTP 接口
     */
    @Resource
    private RestTemplate restTemplate;

    /**
     * 获取服务名
     */
    @Value("${service-url.nacos-user-service}")
    private String serverURL;

    @GetMapping("/test")
    public JsonResult test(){
        return JsonResult.success("test");
    }

    /**
     * { @SentinelResource } 用于定义资源，并提供可选的异常处理和 fallback 配置项
     * value：资源名称
     * blockHandler：处理 BlockException 的函数名称，只负责在 sentinel 里面配置的降级限流，函数要求：
     *      1、必须是 public
     *      2、返回类型参数与原方法一致
     *      3、默认需和原方法在同一个类中。若希望使用其他类的函数，可配置blockHandlerclass，并指定blockHandlerClass里面的方法。
     */
    @GetMapping("/consumer/fallback/{id}")
    @SentinelResource(value = "fallback", fallback = "handlerFallback", blockHandler = "blockHandler")
    public JsonResult fallback(@PathVariable Long id){
        // 通过服务名访问微服务提供者的指定接口，传递参数
        // 这里将接收的数据改为 map 的原因是使用 JsonResult 会发生序列化异常，没有找到原因（本地不会报错，放到服务器上就会报错）
        // 返回的全部数据：<200,{msg=ok, data=查询成功，结果为：Payment(id=1, serial=28a8c1e3bc2742d8848569891fb42181)，端口号为：9004, code=200},[Content-Type:"application/json", Transfer-Encoding:"chunked", Date:"Thu, 16 Mar 2023 07:14:07 GMT", Keep-Alive:"timeout=60", Connection:"keep-alive"]>
        // getBody() 为返回的数据
        Map body = restTemplate.getForEntity(serverURL + "/paymentSQL/" + id, Map.class).getBody();

        if (id >= 4) {
            throw new IllegalArgumentException ("IllegalArgumentException，非法参数异常....");
        }

        return JsonResult.success(body.get("data"));
    }
    public JsonResult handlerFallback(@PathVariable  Long id,Throwable e) {
        Payment payment = new Payment(id,"null");
        return JsonResult.error("444", "兜底异常 handlerFallback，结果为：" + payment + "，\n异常为：" + e.getMessage());
    }
    public JsonResult blockHandler(@PathVariable  Long id, BlockException e) {
        Payment payment = new Payment(id,"null");
        return JsonResult.error("444", "限流 blockException，结果为：" + payment + "，\n异常为：" + e.getMessage());
    }

}
```

2. 进入服务器 `/home/docker/docker/VOLUME/java/jar/` 目录，创建脚本文件：`start_cloud.sh`：

```sh
#!/bin/bash

# 进入 /usr/src/myapp 目录
cd /usr/src/myapp

# 删除日志文件
rm order84.log payment9003.log payment9004.log
# 创建日志文件
touch order84.log payment9003.log payment9004.log

# 执行 jar 包；& 的意思是后台运行
java -jar payment9003.jar > payment9003.log &
java -jar payment9004.jar > payment9004.log &
java -jar order84.jar > order84.log
```

3. 将三个项目打包改名，并上传到服务器：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316152851.png)

4. 启动容器：`docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh
f5ab4d502e7148cd7f285ca5fc85d804bc2f9c2aa046a15d152ba2b1c2832f4e

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                              NAMES
f5ab4d502e71   openjdk:8                    "bash /usr/src/myapp…"   52 seconds ago   Up 52 seconds   0.0.0.0:12003->12003/tcp, :::12003->12003/tcp, 0.0.0.0:12002->84/tcp, :::12002->84/tcp, 0.0.0.0:12004->9003/tcp, :::12004->9003/tcp, 0.0.0.0:12005->9004/tcp, :::12005->9004/tcp   java-cloud-sentinel-order
97b24f34e6cd   bladex/sentinel-dashboard    "java -Djava.securit…"   2 days ago       Up 2 days       8719/tcp, 0.0.0.0:8849->8858/tcp, :::8849->8858/tcp                                                                                                                                sentinel
c7641a57950f   nacos/nacos-server:latest    "bin/docker-startup.…"   2 days ago       Up 2 days       0.0.0.0:8848->8848/tcp, :::8848->8848/tcp                                                                                                                                          nacosStandalone
86486e02b952   portainer/portainer:1.20.2   "/portainer"             13 days ago      Up 2 days       0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                                                                                                                          Portainer

docker@VM-8-15-ubuntu:~$ 
```

5. 配置 sentinel 流控规则：1 秒内访问超过 2 次后，进行限流

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316155918.png)

6. 配置 sentinel 降级规则：1 秒内异常超过 2 次后，断路器打开，断电跳闸 70 秒，系统被保护

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316155953.png)

7. 正常访问，1 秒内访问超过 2 次后，进行限流：http://43.138.106.181:12002/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316160058.png)

8. 错误访问，1 秒内异常超过 2 次后，断路器打开，断电跳闸 70 秒，系统被保护：http://43.138.106.181:12002/consumer/fallback/4

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316160152.png)

### ②、服务接口调用 Feign 系列

1. 修改 84 模块，因为 Feign 组件一般是在消费侧
2. 修改 pom.xml，增加 openfeign 依赖

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-consumer-nacos-order84</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
    
        <!--SpringCloud ailibaba sentinel 熔断与限流 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
    
        <!-- openfeign 服务调用 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该Main Class为全局的唯一入口 -->
                    <mainClass>com.yuehai.NacosOrder84</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal><!--可以把依赖的包都打包到生成的Jar包中-->
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

3. 修改 application.yml 配置文件，激活 Sentinel 对 Feign 的支持

```yml
# 服务端口号
server:
    port: 84

# spring 配置
spring:
    application:
        # 服务名称 微服务消费者模块 cloudalibaba-consumer-nacos-order84
        name: nacos-order-consumer
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
        # sentinel 配置
        sentinel:
            transport:
                # 指定 sentinel dashboard 控制台地址
                dashboard: 43.138.106.181:8849
                # 指定本项目和控制台通信的 IP，若不配置，会自动选择一个 IP 注册
                client-ip: 43.138.106.181
                # 指定本项目和控制台通信的端口，默认值 8719；若不配置，会自动扫猫从 8719 开始扫猫，依次 +1，直到找到未被占用的端口
                port: 12003
                # 心跳发送周期，默认值 null；但在 SimpleHttpHeartbeatSender 会用默认值 10秒
                heartbeat-interval-ms: 10000

# 激活 Sentinel 对 Feign 的支持
feign:
    sentinel:
        enabled: true

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: '*'

# 消费者将要去访问的微服务名称（注册成功进 nacos 的微服务提供者），这个不是配置项，只是为了方便获取值
service-url:
    nacos-user-service: http://nacos-payment-provider
```

4. 修改主启动类。添加注解：`@EnableFeignClients`

```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;

/**
 * 微服务消费者模块 cloudalibaba-consumer-nacos-order84
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * { @EnableDiscoveryClient }：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 * { @EnableFeignClients }：告诉框架扫描所有使用注解 @FeignClient 定义的 feign 客户端，并把 feign 客户端注册到 IOC 容器中
 */

@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
public class NacosOrder84 {

    public static void main(String[] args) {
        SpringApplication.run(NacosOrder84.class, args);
    }

}
```

5. 创建 OpenFeign 接口类 PaymentService

```java
package com.yuehai.service;

import com.yuehai.service.impl.PaymentFallbackServiceImpl;
import com.yuehai.utils.JsonResult;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

/**
 * @author 月海
 * @create 2023/3/16 16:29
 *
 * { @FeignClient：主要用于客户端服务发现，实际就是调用其他的服务 }
 *      value = "nacos-payment-provider"：调用 nacos-payment-provider 的接口 }
 *      fallback = PaymentFallbackService.class：用于在抛出异常的时候提供 fallback 处理逻辑，PaymentFallbackService 要实现本类
 */

@FeignClient(value = "nacos-payment-provider", fallback = PaymentFallbackServiceImpl.class)
public interface PaymentService {

    /**
     * 调用 nacos-payment-provider 服务的 /paymentSQL/{id} 接口
     */
    @GetMapping(value = "/paymentSQL/{id}")
    JsonResult paymentSql(@PathVariable("id") Long id);

}

```

6. 创建 OpenFeign 接口类 PaymentService  的实现类 PaymentFallbackServiceImpl，增加 `@Component` 注解，编写兜底容错的方法

```java
package com.yuehai.service.impl;

import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.stereotype.Component;

/**
 * @author 月海
 * @create 2023/3/16 16:39
 */

@Component
public class PaymentFallbackServiceImpl implements PaymentService {

    /**
     * 调用 nacos-payment-provider 服务的 /paymentSQL/{id} 接口
     */
    @Override
    public JsonResult paymentSql(Long id) {
        return JsonResult.error("444", "----因服务降级返回，没有信息----");
    }

}

```

7. 创建业务类 OpenFeignFallbackController

```java
package com.yuehai.controller;

import com.yuehai.entities.Payment;
import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/16 16:43
 */

@RestController
public class OpenFeignFallbackController {

    @Resource
    private PaymentService paymentService;

    @GetMapping(value = "/consumer/openfeign/{id}")
    public JsonResult paymentSQL(@PathVariable("id") Long id){
        if(id >= 4){
            throw new RuntimeException("没有该id");
        }

        return paymentService.paymentSql(id);
    }

}
```

8. 进入服务器 `/home/docker/docker/VOLUME/java/jar/` 目录，创建脚本文件：`start_cloud.sh`：

```sh
#!/bin/bash

# 进入 /usr/src/myapp 目录
cd /usr/src/myapp

# 删除日志文件
rm order84.log payment9003.log payment9004.log
# 创建日志文件
touch order84.log payment9003.log payment9004.log

# 执行 jar 包；& 的意思是后台运行
java -jar payment9003.jar > payment9003.log &
java -jar payment9004.jar > payment9004.log &
java -jar order84.jar > order84.log
```

9. 将三个项目打包改名，并上传到服务器：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230316152851.png)

10. 启动容器：`docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d --name java-cloud-sentinel-order -p 12002:84 -p 12003:12003 -p 12004:9003 -p 12005:9004 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 bash /usr/src/myapp/start_cloud.sh
f5ab4d502e7148cd7f285ca5fc85d804bc2f9c2aa046a15d152ba2b1c2832f4e

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                              NAMES
f5ab4d502e71   openjdk:8                    "bash /usr/src/myapp…"   52 seconds ago   Up 52 seconds   0.0.0.0:12003->12003/tcp, :::12003->12003/tcp, 0.0.0.0:12002->84/tcp, :::12002->84/tcp, 0.0.0.0:12004->9003/tcp, :::12004->9003/tcp, 0.0.0.0:12005->9004/tcp, :::12005->9004/tcp   java-cloud-sentinel-order
97b24f34e6cd   bladex/sentinel-dashboard    "java -Djava.securit…"   2 days ago       Up 2 days       8719/tcp, 0.0.0.0:8849->8858/tcp, :::8849->8858/tcp                                                                                                                                sentinel
c7641a57950f   nacos/nacos-server:latest    "bin/docker-startup.…"   2 days ago       Up 2 days       0.0.0.0:8848->8848/tcp, :::8848->8848/tcp                                                                                                                                          nacosStandalone
86486e02b952   portainer/portainer:1.20.2   "/portainer"             13 days ago      Up 2 days       0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                                                                                                                          Portainer

docker@VM-8-15-ubuntu:~$ 
```

11. 访问 84 端口：http://43.138.106.181:12002/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317082817.png)

12. 关闭 9003 和 9004 的项目进程

```bash
root@f5ab4d502e71:/# jps -l
853 sun.tools.jps.Jps
9 payment9003.jar
10 payment9004.jar
11 order84.jar

root@f5ab4d502e71:/# kill -9 9 10

root@f5ab4d502e71:/# jps -l
11 order84.jar
877 sun.tools.jps.Jps

root@f5ab4d502e71:/#
```

13. 再次访问 84 端口：http://43.138.106.181:12002/consumer/fallback/1

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317083622.png)

14. 可以看到 84 端口已自动降级，即使没有服务可调用也不会被耗死

### ③、熔断框架比较

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317083655.png)

## 10、规则持久化

### ①、介绍

1. 为什么要配置持久化：一旦我们重启应用，sentinel 规则将消失，所以生产环境需要将配置规则进行持久化
2. 持久化原理：将限流配置规则持久化进 Nacos 保存，只要刷新 8401 某个 rest 地址，sentinel 控制台的流控规则就能看到，只要 Nacos 里面的配置不删除，针对 8401 上 sentinel 上的流控规则持续有效

### ②、配置持久化

1. 修改 cloudalibaba-sentinel-service8401
2. 修改父 pom.xml，增加 maven 插件 `spring-boot-maven-plugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.yuehai</groupId>
    <artifactId>SpringCloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <!-- 子项目 -->
    <modules>
        <module>cloud-provider-payment8001</module>
        <module>cloud-consumer-order80</module>
        <module>cloud-api-commons</module>
        <module>cloud-eureka-server7001</module>
        <module>cloud-eureka-server7002</module>
        <module>cloud-provider-payment8002</module>
        <module>cloud-provider-payment8004</module>
        <module>cloud-consumerzk-order80</module>
        <module>cloud-consumer-feign-order80</module>
        <module>cloud-provider-hystrix-payment8007</module>
        <module>cloud-consumer-feign-hystrix-order80</module>
        <module>cloud-provider-hystrix-payment8008</module>
        <module>cloud-consumer-hystrix-dashboard9001</module>
        <module>cloud-gateway-gateway9527</module>
        <module>cloud-config-center3344</module>
        <module>cloud-config-client3355</module>
        <module>cloudalibaba-provider-payment9001</module>
        <module>cloudalibaba-provider-payment9002</module>
        <module>cloudalibaba-consumer-nacos-order83</module>
        <module>cloudalibaba-config-nacos-client3377</module>
        <module>cloudalibaba-sentinel-server8401</module>
        <module>cloudalibaba-provider-payment9003</module>
        <module>cloudalibaba-provider-payment9004</module>
        <module>cloudalibaba-consumer-nacos-order84</module>
    </modules>
    
    <!-- 统一管理 jar 包版本 -->
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    
        <junit.version>4.12</junit.version>
        <log4j.version>1.2.17</log4j.version>
        <lombok.version>1.16.18</lombok.version>
        <mysql.version>5.1.47</mysql.version>
        <druid.version>1.1.16</druid.version>
        <mybatis-plus.spring.boot.version>3.5.1</mybatis-plus.spring.boot.version>
    
        <hutool-all>5.8.11</hutool-all>
    </properties>
    
    <!-- 子模块继承之后，提供作用：锁定版本 + 子 modlue 不用写 groupId 和 version  -->
    <dependencyManagement>
        <dependencies>
            <!--spring boot 2.2.2-->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.2.2.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--spring cloud Hoxton.SR1-->
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Hoxton.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--spring cloud alibaba 2.1.0.RELEASE-->
            <dependency>
                <groupId>com.alibaba.cloud</groupId>
                <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                <version>2.1.0.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            
            <!-- mysql -->
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
            <!-- mybatis-plus -->
            <dependency>
                <groupId>com.baomidou</groupId>
                <artifactId>mybatis-plus-boot-starter</artifactId>
                <version>${mybatis-plus.spring.boot.version}</version>
            </dependency>
    
            <!-- hutool 工具包 -->
            <dependency>
                <groupId>cn.hutool</groupId>
                <artifactId>hutool-all</artifactId>
                <version>${hutool-all}</version>
            </dependency>
            
            <!-- junit Test -->
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>${junit.version}</version>
            </dependency>
            <!-- log4j -->
            <dependency>
                <groupId>log4j</groupId>
                <artifactId>log4j</artifactId>
                <version>${log4j.version}</version>
            </dependency>
            <!-- lombok -->
            <dependency>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>${lombok.version}</version>
                <optional>true</optional>
            </dependency>
        </dependencies>
    </dependencyManagement>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该 Main Class 为全局的唯一入口 -->
                    <!--suppress UnresolvedMavenProperty -->
                    <mainClass>${Application}</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <!-- 可以把依赖的包都打包到生成的 Jar 包中 -->
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    
</project>
```

3. 修改 cloudalibaba-sentinel-service8401 pom.xml，增加 `sentinel-datasource-nacos` 依赖（之前就加上过了）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloudalibaba-sentinel-server8401</artifactId>
    
    <!-- 统一管理 jar 包版本 -->
    <properties>
        <!-- 主启动类，maven 插件打包使用 -->
        <Application>com.yuehai.SentinelServer8401</Application>
    </properties>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        
        <!--SpringCloud ailibaba sentinel 熔断与限流 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <!--SpringCloud ailibaba sentinel-datasource-nacos 后续做持久化用到-->
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-nacos</artifactId>
        </dependency>
    
        <!-- openfeign 服务调用 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
    </dependencies>
    
</project>
```

4. 修改 application.yml 配置文件，增加 sentinel 的持久化数据源配置

```yml
# 服务端口号
server:
    port: 8401

# spring 配置
spring:
    application:
        # 服务名称 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
        name: cloudalibaba-sentinel-server
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
        # sentinel 配置
        sentinel:
            transport:
                # 指定 sentinel dashboard 控制台地址
                dashboard: 43.138.106.181:8849
                # 指定本项目和控制台通信的 IP，若不配置，会自动选择一个 IP 注册
                client-ip: 43.138.106.181
                # 指定本项目和控制台通信的端口，默认值 8719；若不配置，会自动扫猫从 8719 开始扫猫，依次 +1，直到找到未被占用的端口
                port: 12001
                # 心跳发送周期，默认值 null；但在 SimpleHttpHeartbeatSender 会用默认值 10秒
                heartbeat-interval-ms: 10000
            # sentinel 持久化数据源配置
            datasource:
                # 自定义数据源名称
                ds1:
                    # 以 nacos 作为数据源的配置
                    nacos:
                        # 当前 sentinel 模块的微服务名称
                        data-id: cloudalibaba-sentinel-server
                        # 配置 nacos 地址
                        server-addr: 43.138.106.181:8848
                        # 指定命名空间，只能输入命名空间的 id
                        namespace: abcb1ba7-07aa-4eeb-96d7-a53381cd3958
                        # nacos 分组名称
                        # group-id: DEFAULT_GROUP
                        # 数据保存格式
                        data-type: json
                        # 表示数据源中规则属于哪种类型
                        rule-type: flow

# 暴露监控端点
management:
    endpoints:
        web:
            exposure:
                # 暴露所有端点 默认是 info, health
                include: "*"
```

5. 在 dev 命名空间下新建配置 cloudalibaba-sentinel-server ：
	1. `resource`：资源名称；
	2. `limitApp`：来源应用；
	3. `grade`：阈值类型，0表示线程数，1表示QPS；
	4. `count`：单机阈值；
	5. `strategy`：流控模式，0表示直接，1表示关联，2表示链路；
	6. `controlBehavior`：流控效果，0表示快速失败，1表示Warm Up，2表示排队等待；
	7. `clusterMode`：是否集群。

```json
[
    {
        "resource": "/rateLimit/byUrl",
        "limitApp": "default",
        "grade": 1,
        "count": 1,
        "strategy": 0,
        "controlBehavior": 0,
        "clusterMode": false
    }
]
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317091759.png)

6. 打包部署，启动 docker 容器：`docker run -d --name java-cloud-sentinel -p 12000:8401 -p 12001:12001 -v /home/docker/docker/VOLUME/java/jar/:/usr/src/myapp openjdk:8 java -jar /usr/src/myapp/cloudalibaba-sentinel-server8401.jar`
7. 访问 8401 ：http://43.138.106.181:12000/rateLimit/byUrl

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110114.png)

8. 访问 sentinel，发现自带流控规则：http://43.138.106.181:8849/#/dashboard/flow/cloudalibaba-sentinel-server

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317105814.png)

9. 多次刷新 8401 接口，触发降级规则：http://43.138.106.181:12000/rateLimit/byUrl

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110338.png)

10. 停止 8401，再看 sentinel，流控规则没有了

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110511.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110627.png)

11. 重启 8401，再看 sentinel，流控规则又出现了

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110719.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317110748.png)

# 四、Seata 处理分布式事务

## 1、分布式事务问题

1. 分布式前是一个应用，使用一个数据源，连接一个数据库，使用自己的事务即可，不会发生问题
2. 分布式后单体应用被拆分成微服务应用，原来的三个模块被拆分成三个独立的应用，分别使用三个独立的数据源
3. 业务操作需要调用三个服务来完成。此时每个服务内部的数据一致性由本地事务来保证，但是全局的数据一致性问题没法保证。
4. 一句话：一次业务操作需要跨多个数据源或需要跨多个系统进行远程调用，就会产生分布式事务问题

## 2、Seata 简介

> 官网：http://seata.io/zh-cn/
> 
> 发布说明：https://github.com/seata/seata/releases
> 
> 下载地址：https://github.com/seata/seata/releases

### ①、是什么

1. Seata 是一款开源的分布式事务解决方案，致力于提供高性能和简单易用的分布式事务服务。
2. Seata 将为用户提供了 AT、TCC、SAGA 和 XA 事务模式，为用户打造一站式的分布式解决方案
3. 2019 年 1 月份蚂蚁金服和阿里巴巴共同开源的分布式事务解决方案
4. Simple Extensible Autonomous Transaction Architecture，简单可扩展自治事务框架

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317153544.png)

### ②、能干嘛

1. 一 ID ：Transaction ID XID：全局唯一的事务 ID
2. 三组件模型：
	1. TC (Transaction Coordinator) - 事务协调者：维护全局和分支事务的状态，驱动全局事务提交或回滚。
	2. TM (Transaction Manager) - 事务管理器：定义全局事务的范围：开始全局事务、提交或回滚全局事务。
	3. RM (Resource Manager) - 资源管理器：管理分支事务处理的资源，与TC交谈以注册分支事务和报告分支事务的状态，并驱动分支事务提交或回滚。

### ③、处理过程

1. TM 向 TC 申请开启一个全局事务，全局事务创建成功并生成一个全局唯一的 XID；
2. XID 在微服务调用链路的上下文中传播；
3. RM 向 TC 注册分支事务，将其纳入 XID 对应全局事务的管辖；
4. TM 向 TC 发起针对 XID 的全局提交或回滚决议；
5. TC 调度 XID 下管辖的全部分支事务完成提交或回滚请求。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317153959.png)

### ④、怎么用

1. 本地 `@Transactional`
2. 全局 `@GlobalTransactional`
3. SEATA 的分布式交易解决方案：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317155344.png)

## 3、下载安装

> 还是用的 docker，各版本选择为：
> 1. Spring Boot：2.3.12.RELEASE
> 2. Spring Cloud：Spring Cloud Hoxton.SR12
> 3. Spring Cloud Alibaba：2.2.10-RC1
> 4. Nacos：2.2.0
> 5. Seata：1.6.1
> 6. mysql：5.7，Seata 1.6.1 不支持 8.0 以上的 mysql（好吧其实是支持的）
> 
> <font color="#ff0000">避免直接拉取 latest 版本镜像，latest 版本并不一定是 released 版本，为避免不必要的问题，请到 docker 镜像仓库确定要拉取的镜像版本。</font>

### ①、部署 mysql

1. 拉取镜像：`docker pull mysql:latest`
2. 启动临时容器，复制文件：`docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=000123 --name yuehai-mysql mysql:latest`
3. 复制文件：
	1. 数据：`docker cp yuehai-mysql:/var/lib/mysql /home/docker/docker/VOLUME/mysql/mysql/data`
	2. 配置文件：`docker cp yuehai-mysql:/etc/mysql/conf.d /home/docker/docker/VOLUME/mysql/mysql/conf`
	3. 日志文件：创建 log 目录即可
4. 删除容器重新创建：`docker run -d -p 3306:3306 --privileged=true -v ~/docker/VOLUME/mysql/mysql/log:/var/log/mysql -v ~/docker/VOLUME/mysql/mysql/data:/var/lib/mysql -v ~/docker/VOLUME/mysql/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=000123 --name yuehai-mysql mysql:latest`
5. 连接测试：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321091050.png)

### ②、部署 nacos

1. 创建数据库 `nacos-config`，在其中执行下面的 sql 脚本，以创建 nacos 所需的数据库与表：

```sql
/*
 * Copyright 1999-2018 Alibaba Group Holding Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info   */
/******************************************/
CREATE TABLE `config_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) DEFAULT NULL,
  `content` longtext NOT NULL COMMENT 'content',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  `app_name` varchar(128) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `c_desc` varchar(256) DEFAULT NULL,
  `c_use` varchar(64) DEFAULT NULL,
  `effect` varchar(64) DEFAULT NULL,
  `type` varchar(64) DEFAULT NULL,
  `c_schema` text,
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfo_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_aggr   */
/******************************************/
CREATE TABLE `config_info_aggr` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `datum_id` varchar(255) NOT NULL COMMENT 'datum_id',
  `content` longtext NOT NULL COMMENT '内容',
  `gmt_modified` datetime NOT NULL COMMENT '修改时间',
  `app_name` varchar(128) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfoaggr_datagrouptenantdatum` (`data_id`,`group_id`,`tenant_id`,`datum_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='增加租户字段';


/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_beta   */
/******************************************/
CREATE TABLE `config_info_beta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL COMMENT 'content',
  `beta_ips` varchar(1024) DEFAULT NULL COMMENT 'betaIps',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfobeta_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_beta';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_tag   */
/******************************************/
CREATE TABLE `config_info_tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `tenant_id` varchar(128) DEFAULT '' COMMENT 'tenant_id',
  `tag_id` varchar(128) NOT NULL COMMENT 'tag_id',
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL COMMENT 'content',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfotag_datagrouptenanttag` (`data_id`,`group_id`,`tenant_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_tag';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_tags_relation   */
/******************************************/
CREATE TABLE `config_tags_relation` (
  `id` bigint(20) NOT NULL COMMENT 'id',
  `tag_name` varchar(128) NOT NULL COMMENT 'tag_name',
  `tag_type` varchar(64) DEFAULT NULL COMMENT 'tag_type',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `tenant_id` varchar(128) DEFAULT '' COMMENT 'tenant_id',
  `nid` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `uk_configtagrelation_configidtag` (`id`,`tag_name`,`tag_type`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_tag_relation';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = group_capacity   */
/******************************************/
CREATE TABLE `group_capacity` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `group_id` varchar(128) NOT NULL DEFAULT '' COMMENT 'Group ID，空字符表示整个集群',
  `quota` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数，，0表示使用默认值',
  `max_aggr_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='集群、各Group容量信息表';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = his_config_info   */
/******************************************/
CREATE TABLE `his_config_info` (
  `id` bigint(20) unsigned NOT NULL,
  `nid` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `data_id` varchar(255) NOT NULL,
  `group_id` varchar(128) NOT NULL,
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL,
  `md5` varchar(32) DEFAULT NULL,
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `src_user` text,
  `src_ip` varchar(50) DEFAULT NULL,
  `op_type` char(10) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`nid`),
  KEY `idx_gmt_create` (`gmt_create`),
  KEY `idx_gmt_modified` (`gmt_modified`),
  KEY `idx_did` (`data_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='多租户改造';


/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = tenant_capacity   */
/******************************************/
CREATE TABLE `tenant_capacity` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `tenant_id` varchar(128) NOT NULL DEFAULT '' COMMENT 'Tenant ID',
  `quota` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数',
  `max_aggr_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='租户容量信息表';


CREATE TABLE `tenant_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `kp` varchar(128) NOT NULL COMMENT 'kp',
  `tenant_id` varchar(128) default '' COMMENT 'tenant_id',
  `tenant_name` varchar(128) default '' COMMENT 'tenant_name',
  `tenant_desc` varchar(256) DEFAULT NULL COMMENT 'tenant_desc',
  `create_source` varchar(32) DEFAULT NULL COMMENT 'create_source',
  `gmt_create` bigint(20) NOT NULL COMMENT '创建时间',
  `gmt_modified` bigint(20) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_info_kptenantid` (`kp`,`tenant_id`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='tenant_info';

CREATE TABLE `users` (
	`username` varchar(50) NOT NULL PRIMARY KEY,
	`password` varchar(500) NOT NULL,
	`enabled` boolean NOT NULL
);

CREATE TABLE `roles` (
	`username` varchar(50) NOT NULL,
	`role` varchar(50) NOT NULL,
	UNIQUE INDEX `idx_user_role` (`username` ASC, `role` ASC) USING BTREE
);

CREATE TABLE `permissions` (
    `role` varchar(50) NOT NULL,
    `resource` varchar(255) NOT NULL,
    `action` varchar(8) NOT NULL,
    UNIQUE INDEX `uk_role_permission` (`role`,`resource`,`action`) USING BTREE
);

INSERT INTO users (username, password, enabled) VALUES ('nacos', '$2a$10$EuWPZHzz32dJN7jexM34MOeYirDdFAZm2kuWj7VEOJhhZkDrxfvUu', TRUE);

INSERT INTO roles (username, role) VALUES ('nacos', 'ROLE_ADMIN');
```

2. 拉取镜像：`docker pull nacos/nacos-server:v2.2.0`
3. 临时启动容器，用于拷贝配置文件和日志：`docker run -p 8848:8848 -e MODE=standalone --name nacos -d nacos/nacos-server:v2.2.0`
4. 配置文件和日志复制：`docker cp nacos:/home/nacos/conf/ ~/docker/VOLUME/nacos/nacos/`、`docker cp nacos:/home/nacos/logs/ ~/docker/VOLUME/nacos/nacos/`
5. 再次启动容器，设定参数：
	1. `MODE=standalone`：以单机模式启动
	2. `TIME_ZONE='Asia/Shanghai'`：时区
	3. `SPRING_DATASOURCE_PLATFORM` : 使用的数据库类型
	4. `MYSQL_SERVICE_HOST`：数据库地址
	5. `MYSQL_SERVICE_PORT`：数据库端口号
	6. `MYSQL_SERVICE_DB_NAME`：数据库用户名
	7. `MYSQL_SERVICE_PASSWORD`：数据库密码
	8. `MYSQL_SERVICE_DB_NAME` : 数据库名称
	9. `MYSQL_DATABASE_NUM`：数据库数量，默认就是1，可以不填写
	10. <font color="#ff0000">注意：</font>Nacos2.0 版本相比 1.X 新增了 gRPC 的通信方式，因此需要增加 2 个端口。新增端口是在配置的主端口(server.port)基础上，进行一定偏移量自动生成。
		1. 主端口 + 1000：客户端 gRPC 请求服务端端口，用于客户端向服务端发起连接和请求
		2. 主端口 + 1001：服务端 gRPC 请求服务端端口，用于服务间同步等

```bash
docker run -d \
	-e MODE=standalone \
	-e TIME_ZONE='Asia/Shanghai' \
	-e SPRING_DATASOURCE_PLATFORM=mysql \
	-e MYSQL_SERVICE_HOST=43.138.106.181 \
	-e MYSQL_SERVICE_PORT=3306 \
	-e MYSQL_SERVICE_USER=root \
	-e MYSQL_SERVICE_PASSWORD=000123 \
	-e MYSQL_SERVICE_DB_NAME=nacos-config \
	-v ~/docker/VOLUME/nacos/nacos/conf:/home/nacos/conf \
	-v ~/docker/VOLUME/nacos/nacos/logs:/home/nacos/logs \
	-p 8848:8848 \
	-p 9848:9848 \
	-p 9849:9849 \
	--name yuehai-nacosStandalone \
	nacos/nacos-server:v2.2.0
```

6. 访问测试：http://43.138.106.181:8848/nacos/

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321094625.png)

### ③、部署 seata

1. 拉取镜像：`docker pull seataio/seata-server:1.6.1`

```bash
docker@VM-8-15-ubuntu:~$ docker search seata
NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
seataio/seata-server                    Distributed transaction solution with high p…   61                   
seatable/seatable                       Note: this docker repository is no longer up…   25                   
seatable/seatable-developer             Beyond Spreadsheet – official Docker image f…   13                   
seatable/seatable-enterprise            Beyond Spreadsheet – official Docker image f…   7                    
seatable/python-runner                  Beyond Spreadsheet – official Docker image f…   2                    
zhaoyunxing/seata                       分布式事物中间件-seata                                  1                    
fancyfong/seata                                                                         1                    
hellowoodes/seata                       Seata Server for Alibaba Seata                  0                    
seatable/seatable-faas-scheduler-test                                                   0                    
guaiwolo/seata-server                                                                   0                    
vqui/seatable-python-runner             https://github.com/vquie/seatable-python-run…   0                    
vqui/seatable-faas-scheduler            https://github.com/vquie/seatable-faas-sched…   0                    
seatable/seatable-syncer-test                                                           0                    
wjq1028cs2/seata-server                 fix a bug from seataio/seata-server             0                    
ssgssg/seata                            seata                                           0                    
stackfuel/seatable-dump-db                                                              0                    
shuogesha/seata1.1.0                    seata1.1.0                                      0                    
seatable/seatable-enterprise-testing                                                    0                    
seatable/dtable-server-proxy                                                            0                    
infinivision/seata                                                                      0                    
seatabay/ubuntu-nodejs                                                                  0                    
majiajue/seata                          seata-server                                    0                    
wildwind113/seata                                                                       0                    
seatable/seatable-faas-scheduler        Beyond Spreadsheet – official Docker image f…   0                    
chaiyd/seata                                                                            0                    

docker@VM-8-15-ubuntu:~$ docker pull seataio/seata-server:1.6.1
1.6.1: Pulling from seataio/seata-server
001c52e26ad5: Pull complete 
d9d4b9b6e964: Pull complete 
2068746827ec: Pull complete 
9daef329d350: Pull complete 
d85151f15b66: Pull complete 
52a8c426d30b: Pull complete 
8754a66e0050: Pull complete 
5ed2ec2d6ee2: Pull complete 
b71086c56a63: Pull complete 
1181f8e565af: Pull complete 
6d058363682a: Pull complete 
adc1f51855c8: Pull complete 
5b571cda842d: Pull complete 
Digest: sha256:07796d3dff51cc34f4980d55ecde87c5271a34824fe1eeea9ddb57dbfee6b9e6
Status: Downloaded newer image for seataio/seata-server:1.6.1
docker.io/seataio/seata-server:1.6.1

docker@VM-8-15-ubuntu:~/docker$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED         SIZE
yuehai-nginx-nacos     v0.1      e988bcbf0734   2 weeks ago     141MB
yuehai-vue             v0.1      402b842b0461   2 weeks ago     142MB
yuehai-java            v0.1      6bf178479b40   2 weeks ago     453MB
seataio/seata-server   1.6.1     c38467c57235   2 months ago    632MB
nacos/nacos-server     v2.2.0    440657d52bc3   2 months ago    1.07GB
nginx                  latest    605c77e624dd   14 months ago   141MB
openjdk                8         e24ac15e052e   15 months ago   526MB
redis                  latest    7614ae9453d1   15 months ago   113MB
mysql                  5.7       c20987f18b13   15 months ago   448MB
ubuntu                 latest    ba6acccedd29   17 months ago   72.8MB
portainer/portainer    1.20.2    19d07168491a   4 years ago     74.1MB

docker@VM-8-15-ubuntu:~/docker$ 
```

2. 临时启动容器，用于拷贝配置文件：`docker run -d --name yuehai-seata-server -p 7091:7091 -p 8091:8091 seataio/seata-server:1.6.1`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d --name yuehai-seata-server -p 7091:7091 -p 8091:8091 seataio/seata-server:1.6.1
442c1c4dda929e2cf72d05aef5108ed67212b5b0c7e62e8052d4ac91e942d700

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                                                  NAMES
442c1c4dda92   seataio/seata-server:1.6.1   "java -Djava.securit…"   45 seconds ago   Up 45 seconds   0.0.0.0:7091->7091/tcp, :::7091->7091/tcp, 0.0.0.0:8091->8091/tcp, :::8091->8091/tcp   yuehai-seata-server
5e139fe31f89   nacos/nacos-server:latest    "bin/docker-startup.…"   2 days ago       Up 2 days       0.0.0.0:8848->8848/tcp, :::8848->8848/tcp                                              yuehai-nacosStandalone
86486e02b952   portainer/portainer:1.20.2   "/portainer"             2 weeks ago      Up 5 days       0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                              Portainer
a8c5a95cfbef   mysql                        "docker-entrypoint.s…"   2 weeks ago      Up 37 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                   yuehai-mysql

docker@VM-8-15-ubuntu:~$ 
```

3. 拷贝配置文件到宿主机：`docker cp yuehai-seata-server:/seata-server/resources/ ~/docker/VOLUME/seata/`

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230317165527.png)

4. 修改配置文件：application.yml

```yml
#  Copyright 1999-2019 Seata.io Group.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

server:
    # seata  端口号
    port: 7091

spring:
    application:
        # seata 微服务名
        name: seata-server

logging:
    config: classpath:logback-spring.xml
    file:
        path: ${user.home}/logs/seata
    extend:
        logstash-appender:
            destination: 127.0.0.1:4560
        kafka-appender:
            bootstrap-servers: 127.0.0.1:9092
            topic: logback_to_logstash

console:
    user:
        username: admin
        password: admin

# seata 配置
seata:
    # 配置中心配置
    config:
        # 配置中心类型，支持：file，nacos, consul, apollo, zk, etcd3
        type: nacos
        # nacos 作为配置中心配置
        nacos:
            # nacos 地址
            server-addr: 43.138.106.181:8848
            # 命名空间
            namespace: 
            # 配置分组，默认为 SEATA_GROUP
            group: SEATA_GROUP
            # nacos 账号
            username: nacos
            # nacos 密码
            password: nacos
            # nacos 中的配置文件名
            data-id: seataServer.properties

    # 注册中心配置
    registry:
        # 注册中心类型，支持：file，nacos, eureka, redis, zk, consul, etcd3, sofa
        type: nacos
        # nacos 作为注册中心配置配置
        nacos:
            # seata 服务名
            application: seata-server
            # nacos 地址
            server-addr: 43.138.106.181:8848
            # 命名空间
            namespace: 
            # 服务分组，默认为 SEATA_GROUP
            group: SEATA_GROUP
            #
            cluster: default
            # nacos 账号
            username: nacos
            # nacos 密码
            password: nacos

    #  server:
    #    service-port: 8091 #If not configured, the default is '${server.port} + 1000'
    security:
        secretKey: SeataSecretKey0c382ef121d778043159209298fd40bf3850a017
        tokenValidityInMilliseconds: 1800000
        ignore:
            urls: /,/**/*.css,/**/*.js,/**/*.html,/**/*.map,/**/*.svg,/**/*.png,/**/*.ico,/console-fe/public/**,/api/v1/auth/login
```

5. 在 nacos 中新增配置文件：`seataServer.properties`，分组为：`SEATA_GROUP`，命名空间为：`public`

```properties
# 存储模式
store.mode=db
 
store.db.datasource=druid
store.db.dbType=mysql
# 需要根据mysql的版本调整driverClassName
# mysql8及以上版本对应的driver：com.mysql.cj.jdbc.Driver
# mysql8以下版本的driver：com.mysql.jdbc.Driver
store.db.driverClassName=com.mysql.cj.jdbc.Driver
# 注意根据生产实际情况调整参数host和port
store.db.url=jdbc:mysql://43.138.106.181:3306/seata?rewriteBatchedStatements=true&useUnicode=true&characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true&useSSL=false
# 数据库用户名
store.db.user=root
# 用户名密码
store.db.password=000123
# 微服务里配置与这里一致
service.vgroupMapping.order_tx_group=default
service.vgroupMapping.storage_tx_group=default
service.vgroupMapping.account_tx_group=default
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230323103921.png)

6. 进入 mysql，创建数据库 seata，并执行以下 sql：
	1. 下载完整版 seata：http://seata.io/zh-cn/blog/download.html
	2. 解压后所在目录：`seata-1.6.1\script\server\db`

```sql
-- -------------------------------- The script used when storeMode is 'db' --------------------------------
-- the table to store GlobalSession data
CREATE TABLE IF NOT EXISTS `global_table`
(
    `xid`                       VARCHAR(128) NOT NULL,
    `transaction_id`            BIGINT,
    `status`                    TINYINT      NOT NULL,
    `application_id`            VARCHAR(32),
    `transaction_service_group` VARCHAR(32),
    `transaction_name`          VARCHAR(128),
    `timeout`                   INT,
    `begin_time`                BIGINT,
    `application_data`          VARCHAR(2000),
    `gmt_create`                DATETIME,
    `gmt_modified`              DATETIME,
    PRIMARY KEY (`xid`),
    KEY `idx_status_gmt_modified` (`status` , `gmt_modified`),
    KEY `idx_transaction_id` (`transaction_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- the table to store BranchSession data
CREATE TABLE IF NOT EXISTS `branch_table`
(
    `branch_id`         BIGINT       NOT NULL,
    `xid`               VARCHAR(128) NOT NULL,
    `transaction_id`    BIGINT,
    `resource_group_id` VARCHAR(32),
    `resource_id`       VARCHAR(256),
    `branch_type`       VARCHAR(8),
    `status`            TINYINT,
    `client_id`         VARCHAR(64),
    `application_data`  VARCHAR(2000),
    `gmt_create`        DATETIME(6),
    `gmt_modified`      DATETIME(6),
    PRIMARY KEY (`branch_id`),
    KEY `idx_xid` (`xid`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- the table to store lock data
CREATE TABLE IF NOT EXISTS `lock_table`
(
    `row_key`        VARCHAR(128) NOT NULL,
    `xid`            VARCHAR(128),
    `transaction_id` BIGINT,
    `branch_id`      BIGINT       NOT NULL,
    `resource_id`    VARCHAR(256),
    `table_name`     VARCHAR(32),
    `pk`             VARCHAR(36),
    `status`         TINYINT      NOT NULL DEFAULT '0' COMMENT '0:locked ,1:rollbacking',
    `gmt_create`     DATETIME,
    `gmt_modified`   DATETIME,
    PRIMARY KEY (`row_key`),
    KEY `idx_status` (`status`),
    KEY `idx_branch_id` (`branch_id`),
    KEY `idx_xid` (`xid`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS `distributed_lock`
(
    `lock_key`       CHAR(20) NOT NULL,
    `lock_value`     VARCHAR(20) NOT NULL,
    `expire`         BIGINT,
    primary key (`lock_key`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

INSERT INTO `distributed_lock` (lock_key, lock_value, expire) VALUES ('AsyncCommitting', ' ', 0);
INSERT INTO `distributed_lock` (lock_key, lock_value, expire) VALUES ('RetryCommitting', ' ', 0);
INSERT INTO `distributed_lock` (lock_key, lock_value, expire) VALUES ('RetryRollbacking', ' ', 0);
INSERT INTO `distributed_lock` (lock_key, lock_value, expire) VALUES ('TxTimeoutCheck', ' ', 0);
```

6. 删除此 seata 容器重新启动：`docker run -d --name yuehai-seata-server -p 7091:7091 -p 8091:8091 -e SEATA_IP=43.138.106.181 -e SEATA_PORT=8091 -v /home/docker/docker/VOLUME/seata/resources/:/seata-server/resources/ seataio/seata-server:1.6.1`
	1. `seata-server` 支持以下环境变量：
	2. `SEATA_IP`：可选，指定 seata-server 启动的 IP，该 IP 用于向注册中心注册时使用，如 eureka 等
	3. `SEATA_PORT`：可选，指定 seata-server 启动的端口，默认为 `8091`，该 IP 用于向注册中心注册时使用
	4. `STORE_MODE`：可选，指定 seata-server 的事务日志存储方式，支持 `db`，`file`，`redis`(Seata-Server 1.3 及以上版本支持)，默认是 `file`
	5. `SERVER_NODE`：可选，用于指定 seata-server 节点 ID，如 `1`，`2`，`3`...，默认为 根据 `ip` 生成
	6. `SEATA_ENV`：可选，指定 seata-server 运行环境，如 `dev`，`test` 等，服务启动时会使用 `registry-dev.conf` 这样的配置
	7. `SEATA_CONFIG_NAME`：可选，指定配置文件位置，如 `file:/root/registry`，将会加载，`/root/registry.conf` 作为配置文件，如果需要同时指定 `file.conf` 文件，需要将 `registry.conf` 的 `config.file.name` 的值改为类似 `file:/root/file.conf:`

```bash
docker@VM-8-15-ubuntu:~$ docker run -d --name yuehai-seata-server -p 7091:7091 -p 8091:8091 -e SEATA_IP=43.138.106.181 -e SEATA_PORT=8091 -v /home/docker/docker/VOLUME/seata/resources/:/seata-server/resources/ seataio/seata-server:1.6.1
f4f89d38d4874178fbf20f4eb5c10e5f79d2ab1c1ead87703fd76fdde003b92d

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                                                                  NAMES
f4f89d38d487   seataio/seata-server:1.6.1   "java -Djava.securit…"   19 hours ago   Up 18 hours   0.0.0.0:7091->7091/tcp, :::7091->7091/tcp, 0.0.0.0:8091->8091/tcp, :::8091->8091/tcp                       yuehai-seata-server
bd094cc0f788   nacos/nacos-server:v2.2.0    "bin/docker-startup.…"   20 hours ago   Up 19 hours   0.0.0.0:8848->8848/tcp, :::8848->8848/tcp, 0.0.0.0:9848-9849->9848-9849/tcp, :::9848-9849->9848-9849/tcp   yuehai-nacosStandalone
e31941de323d   mysql:5.7                    "docker-entrypoint.s…"   25 hours ago   Up 25 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                                       yuehai-mysql
86486e02b952   portainer/portainer:1.20.2   "/portainer"             2 weeks ago    Up 7 days     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                                                  Portainer
docker@VM-8-15-ubuntu:~$ 
```

7. 进入 nacos 服务管理查看：

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230320102154.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230320102216.png)

## 4、订单/库存/账户业务数据库准备

### ①、分布式事务业务说明

1. 这里我们会创建三个服务，一个订单服务，一个库存服务，一个账户服务。
	1. 当用户下单时，会在订单服务中创建一个订单，然后通过远程调用库存服务来扣减下单商品的库存
	2. 再通过远程调用账户服务来扣减用户账户里面的余额
	3. 最后在订单服务中修改订单状态为已完成。
2. 该操作跨越三个数据库，有两次远程调用，很明显会有分布式事务问题。
3. 下订单 --> 扣库存 --> 减账户(余额)

### ②、创建业务数据库

1. seata_order：存储订单的数据库；
2. seata_storage：存储库存的数据库；
3. seata_account：存储账户信息的数据库。
4. 建库 SQL：

```sql
CREATE DATABASE seata_order;
 
CREATE DATABASE seata_storage;
 
CREATE DATABASE seata_account;
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230320103049.png)

### ③、按照上述 3 库分别建对应业务表

1. seata_order 库下建 t_order 表，订单表

```sql
CREATE TABLE t_order (
  `id` BIGINT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` BIGINT(11) DEFAULT NULL COMMENT '用户id',
  `product_id` BIGINT(11) DEFAULT NULL COMMENT '产品id',
  `count` INT(11) DEFAULT NULL COMMENT '数量',
  `money` DECIMAL(11,0) DEFAULT NULL COMMENT '金额',
  `status` INT(1) DEFAULT NULL COMMENT '订单状态：0：创建中；1：已完结' 
) ENGINE=INNODB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
```

2. seata_storage 库下建 t_storage 表，商品表

```sql
CREATE TABLE t_storage (
 `id` BIGINT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 `product_id` BIGINT(11) DEFAULT NULL COMMENT '产品id',
 `total` INT(11) DEFAULT NULL COMMENT '总库存',
 `used` INT(11) DEFAULT NULL COMMENT '已用库存',
 `residue` INT(11) DEFAULT NULL COMMENT '剩余库存'
) ENGINE=INNODB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO seata_storage.t_storage(`id`, `product_id`, `total`, `used`, `residue`) VALUES ('1', '1', '100', '0', '100');
```

3. seata_account 库下建 t_account 表，用户表

```sql
CREATE TABLE t_account (
  `id` BIGINT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
  `user_id` BIGINT(11) DEFAULT NULL COMMENT '用户id',
  `total` DECIMAL(10,0) DEFAULT NULL COMMENT '总额度',
  `used` DECIMAL(10,0) DEFAULT NULL COMMENT '已用余额',
  `residue` DECIMAL(10,0) DEFAULT '0' COMMENT '剩余可用额度'
) ENGINE=INNODB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
 
INSERT INTO seata_account.t_account(`id`, `user_id`, `total`, `used`, `residue`)  VALUES ('1', '1', '1000', '0', '1000');
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230320103609.png)

### ④、按照上述 3 库分别建对应的回滚日志表

1. 订单-库存-账户 3 个库下都需要建各自的回滚日志表
2. 下载完整版 seata：http://seata.io/zh-cn/blog/download.html，解压后所在目录：`seata-1.6.1\script\client\at\db`
3. 建表 SQL：

```sql
-- for AT mode you must to init this sql for you business database. the seata server not need it.
CREATE TABLE IF NOT EXISTS `undo_log`
(
    `branch_id`     BIGINT       NOT NULL COMMENT 'branch transaction id',
    `xid`           VARCHAR(128) NOT NULL COMMENT 'global transaction id',
    `context`       VARCHAR(128) NOT NULL COMMENT 'undo_log context,such as serialization',
    `rollback_info` LONGBLOB     NOT NULL COMMENT 'rollback info',
    `log_status`    INT(11)      NOT NULL COMMENT '0:normal status,1:defense status',
    `log_created`   DATETIME(6)  NOT NULL COMMENT 'create datetime',
    `log_modified`  DATETIME(6)  NOT NULL COMMENT 'modify datetime',
    UNIQUE KEY `ux_undo_log` (`xid`, `branch_id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4 COMMENT ='AT transaction mode undo table';
```

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230320104611.png)

## 5、订单/库存/账户业务微服务准备

> 业务需求：下订单 -> 减库存 -> 扣余额 -> 改(订单)状态
> 
> 因为之前的项目 springCloud 版本太低，这里重新创建，使用：
> 1. Spring Boot：2.3.12.RELEASE
> 2. Spring Cloud：Spring Cloud Hoxton.SR12
> 3. Spring Cloud Alibaba：2.2.10-RC1

### ①、新建父工程 SpringCloud_alibaba_seata

- pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- 父项目 -->
    <parent>
        <!--spring boot 2.3.12.RELEASE -->
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-dependencies</artifactId>
        <version>2.3.12.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    
    <!-- 本项目的详细信息 -->
    <groupId>com.yuehai</groupId>
    <artifactId>SpringCloud_alibaba_seata</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>cloud-api-commons</module>
        <module>seata-order-service2001</module>
        <module>seata-storage-service2002</module>
    </modules>
    
    <!-- 统一管理 jar 包版本 -->
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <!-- 子模块继承之后，提供作用：锁定版本 + 子 modlue 不用写 groupId 和 version  -->
    <dependencyManagement>
        <dependencies>
            <!-- Spring Cloud Hoxton.SR12-->
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Hoxton.SR12</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--spring cloud alibaba 2.2.10-RC1 -->
            <dependency>
                <groupId>com.alibaba.cloud</groupId>
                <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                <version>2.2.10-RC1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
    
            <!-- druid 数据连接池 -->
            <dependency>
                <groupId>com.alibaba</groupId>
                <artifactId>druid-spring-boot-starter</artifactId>
                <version>1.2.5</version>
            </dependency>
            <!-- mybatis-plus -->
            <dependency>
                <groupId>com.baomidou</groupId>
                <artifactId>mybatis-plus-boot-starter</artifactId>
                <version>3.5.1</version>
            </dependency>
            <!-- hutool 工具包 -->
            <dependency>
                <groupId>cn.hutool</groupId>
                <artifactId>hutool-all</artifactId>
                <version>5.8.11</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.7.3</version>
                <configuration>
                    <!-- 指定该 Main Class 为全局的唯一入口 -->
                    <mainClass>com.yuehai.Application</mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <!-- 可以把依赖的包都打包到生成的 Jar 包中 -->
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

### ②、新建通用 api 模块

1. pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud_alibaba_seata</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-api-commons</artifactId>
    <packaging>jar</packaging>
    
    <dependencies>
        <!-- web 场景 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- springboot 的监控 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
    
        <!--jdbc-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <!-- mysql -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!-- druid 数据连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
        </dependency>
    
        <!-- hutool 工具包 -->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
        </dependency>
        
        <!-- junit Test -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
        <!-- log4j2 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-log4j2</artifactId>
        </dependency>
        <!-- lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
    </dependencies>
    
</project>
```

2. JsonResult 工具类

```java
package com.yuehai.utils;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;

/**
 * @author 月海
 * @create 2022/9/20 15:20
 *
 * 使用 @RestController 或 @ResponseBody 时，可直接返回该对象，
 * Spring Boot 默认使用 Jackson 会自动将该对象转换为 json 字符串
 * 如 {"code": 0,"msg": "","data": [{}, {}]}
 */
public class JsonResult extends HashMap<String, Object> implements Serializable {
    private static final long serialVersionUID = 1L;
    /**
     * 成功
     */
    private static final int SUCCESS = 200;
    /**
     * 失败
     */
    private static final int FAIL = 1;
    /**
     * 错误
     */
    private static final int ERROR = 2;
    /**
     * 未登录
     */
    private static final int LOGOUT = 1001;

    public JsonResult() {

    }

    /**
     * 构造器
     * @param code 状态码
     * @param msg 提示消息
     * @param data 数据
     */
    public JsonResult(int code, String msg, Object data) {
        // 继承自 Map，设置初始容量
        super(3);
        // 状态码，layui 中 code=0 表示成功
        this.put("code", code);
        // 提示消息
        this.put("msg", msg);
        // 数据体
        this.put("data", data);
    }
    /**
     * 构造器
     * @param code 状态码
     * @param msg 提示消息
     */
    public JsonResult(int code, String msg) {
        // 状态码
        this.put("code", code);
        // 提示消息
        this.put("msg", msg);
    }

    /**
     * 一般返回 code、msg 和 data 这三个即可，但 layui 加载 table 时还要求 count 值
     * 添加额外的返回值
     * @param key 额外信息 - key
     * @param value 额外信息 - value
     * @return 返回 额外信息
     */
    @Override
    public JsonResult put(String key, Object value) {
        super.put(key, value);
        return this;
    }


    /**
     * 快速返回请求成功
     * @param data 数据
     * @return 快速返回请求成功
     */
    public static JsonResult success(Object data) {
        return new JsonResult(SUCCESS, "ok", data);
    }

    /**
     * 快速返回请求失败
     * @param msg 提示消息
     * @return 快速返回请求失败
     */
    public static JsonResult fail(String msg) {
        return new JsonResult(FAIL, msg, null);
    }

    /**
     * 快速返回请求错误
     * @param msg 提示消息
     * @param data 数据
     * @return 快速返回请求失败
     */
    public static JsonResult error(String msg, Object data) {
        return new JsonResult(ERROR, msg, data);
    }
    /**
     * 快速返回请求错误 - 自定义状态码和错误信息
     * @param code 状态码
     * @param msg 提示消息
     * @return 快速返回请求错误 - 自定义状态码和错误信息
     */
    public static JsonResult error(int code, String msg) {
        return new JsonResult(code, msg);
    }

    /**
     * 快速返回未登录
     * @return 快速返回未登录
     */
    public static JsonResult logout() {
        return new JsonResult(LOGOUT, "未登录", null);
    }

    /**
     * 快速生成一个 Map 键值对
     * @param key 额外信息 - key
     * @param value 额外信息 - value
     * @return 快速生成一个 Map 键值对
     */
    public static Map<String, Object> fastMap(String key, Object value) {
        Map<String, Object> data = new HashMap<>(1);
        data.put(key, value);
        return data;
    }
}
```

### ③、新建库存模块 seata-storage-service2002

1. 新建模块 seata-storage-service2002

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321135316.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud_alibaba_seata</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>seata-storage-service2002</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包 -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        <!-- seata 分布式事务-->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 2002

# spring 配置
spring:
    application:
        # 服务名称 微服务 商品 模块 seata-storage-service2002
        name: seata-storage-service
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
    # 数据源配置
    datasource:
        druid:
            db-type: com.alibaba.druid.pool.DruidDataSource
            # 连接信息
            # characterEncoding=UTF-8：指定所处理字符的解码和编码的格式
            # useSSL=false：不进行 SSL 连接
            # allowPublicKeyRetrieval=true：允许恶意代理执行MITM攻击以获取明文密码，因此它在默认情况下为False，必须显式启用
            # serverTimezone=GMT：格林尼治标准时间
            url: jdbc:mysql://43.138.106.181:3306/seata_storage?characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=GMT
            # 用户名
            username: root
            # 密码（以 0 开头要加引号）
            password: "000123"

# feign 日志客户端配置
logging:
    level:
        # feign 日志以什么级别监控哪个接口
        com.yuehai.service.PaymentFeignService: debug
        io:
            seata: info

# seata 设置
seata:
    # seata 注册中心设置
    registry:
        # seata 注册中心类型
        type: nacos
        # seata 注册中心的 nacos 设置
        nacos:
            namespace:
            server-addr: 43.138.106.181:8848
            group: SEATA_GROUP
            username: nacos
            password: nacos
```

4. 创建实体类

```java
package com.yuehai.bean;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @author 月海
 * @create 2023/3/21 13:59
 */

@TableName("t_storage")
@Data
public class Storage {
    private Long id;
    /**
     * 产品id
     */
    private Long productId;
    /**
     * 总库存
     */
    private Integer total;
    /**
     * 已用库存
     */
    private Integer used;
    /**
     * 剩余库存
     */
    private Integer residue;
}

```

5. 创建 mapper 接口

```java
package com.yuehai.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.yuehai.bean.Storage;

/**
 * @author 月海
 * @create 2023/3/21 14:00
 */
public interface StorageMapper extends BaseMapper<Storage> {
}

```

6. 创建 service 接口

```java
package com.yuehai.service;

/**
 * @author 月海
 * @create 2023/3/21 14:02
 */
public interface StorageService {
    /**
     * 扣减库存
     */
    void decrease(Long productId, Integer count);
}

```

7. 创建 service 实现类

```java
package com.yuehai.service.impl;

import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import com.yuehai.bean.Storage;
import com.yuehai.mapper.StorageMapper;
import com.yuehai.service.StorageService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/21 14:03
 */

@Slf4j
@Service
public class StorageServiceImpl implements StorageService {

    @Resource
    private StorageMapper storageMapper;

    /**
     * 扣减库存
     */
    @Override
    public void decrease(Long productId, Integer count) {
        log.info("------->storage-service中扣减库存开始");

        // 查
        Storage storage = storageMapper.selectById(productId);
        // 改
        LambdaUpdateWrapper<Storage> wrapper = new LambdaUpdateWrapper<>();
        wrapper.set(Storage::getUsed, storage.getUsed() + count)
                .set(Storage::getResidue, storage.getResidue() - count)
                        .eq(Storage::getProductId, productId);
        storageMapper.update(null, wrapper);

        log.info("------->storage-service中扣减库存结束");
    }
}

```

8. 创建业务类 controller

```java
package com.yuehai.controller;

import com.yuehai.service.StorageService;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/21 14:09
 */

@RestController
public class StorageController {

    @Resource
    private StorageService storageService;

    /**
     * 扣减库存
     */
    @GetMapping("/storage/decrease")
    public JsonResult decrease(Long productId, Integer count) {
        storageService.decrease(productId, count);
        return JsonResult.success("扣减库存成功！");
    }

}

```

9. 修改主启动类

```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * { @EnableDiscoveryClient }：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 * { @MapperScan("com.yuehai.mapper") }：扫描指定包下面的 mapper 接口
 */

@SpringBootApplication
@EnableDiscoveryClient
@MapperScan("com.yuehai.mapper")
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}

```

10. 查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321143206.png)

11. 启动项目，访问接口：http://localhost:2002/storage/decrease?productId=1&count=2

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321143223.png)

13. 再次查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230321143252.png)

14. 将数据修改回去
15. 查看 nacos

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322090326.png)

### ④、新建账户模块 seata-account-service2003

1. 新建模块 seata-account-service2003

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322083018.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud_alibaba_seata</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>seata-account-service2003</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包 -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        <!-- seata 分布式事务-->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 2003

# spring 配置
spring:
    application:
        # 服务名称 微服务 账户 模块 seata-account-service2003
        name: seata-account-service
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
    # 数据源配置
    datasource:
        druid:
            db-type: com.alibaba.druid.pool.DruidDataSource
            # 连接信息
            # characterEncoding=UTF-8：指定所处理字符的解码和编码的格式
            # useSSL=false：不进行 SSL 连接
            # allowPublicKeyRetrieval=true：允许恶意代理执行MITM攻击以获取明文密码，因此它在默认情况下为False，必须显式启用
            # serverTimezone=GMT：格林尼治标准时间
            url: jdbc:mysql://43.138.106.181:3306/seata_account?characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=GMT
            # 用户名
            username: root
            # 密码（以 0 开头要加引号）
            password: "000123"

# feign 日志客户端配置
logging:
    level:
        # feign 日志以什么级别监控哪个接口
        com.yuehai.service.PaymentFeignService: debug
        io:
            seata: info

# seata 设置
seata:
    # seata 注册中心设置
    registry:
        # seata 注册中心类型
        type: nacos
        # seata 注册中心的 nacos 设置
        nacos:
            namespace:
            server-addr: 43.138.106.181:8848
            group: SEATA_GROUP
            username: nacos
            password: nacos
```

4. 创建实体类

```java
package com.yuehai.bean;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 8:36
 */
@TableName("t_account")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account {
    private Long id;
    /**
     * 用户id
     */
    private Long userId;
    /**
     * 总额度
     */
    private BigDecimal total;
    /**
     * 已用额度
     */
    private BigDecimal used;
    /**
     * 剩余额度
     */
    private BigDecimal residue;
}

```

5. 创建 mapper 接口

```java
package com.yuehai.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.yuehai.bean.Account;

/**
 * @author 月海
 * @create 2023/3/22 8:37
 */
public interface AccountMapper extends BaseMapper<Account> {
}

```

6. 创建 service 接口

```java
package com.yuehai.service;

import org.springframework.web.bind.annotation.RequestParam;

import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 8:40
 */
public interface AccountService {
    /**
     * 扣减账户余额
     * @param userId 用户id
     * @param money 金额
     */
    void decrease(@RequestParam("userId") Long userId, @RequestParam("money") BigDecimal money);
}

```

7. 创建 service 实现类

```java
package com.yuehai.service.impl;

import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import com.yuehai.bean.Account;
import com.yuehai.mapper.AccountMapper;
import com.yuehai.service.AccountService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 8:42
 */

@Slf4j
@Service
public class AccountServiceImpl implements AccountService {

    @Resource
    private AccountMapper accountMapper;

    /**
     * 扣减账户余额
     */
    @Override
    public void decrease(Long userId, BigDecimal money) {
        log.info("------->account-service中扣减账户余额开始");
        // 模拟超时异常，全局事务回滚
        // 暂停几秒钟线程
        // try { TimeUnit.SECONDS.sleep(3000); } catch (InterruptedException e) { e.printStackTrace(); }

        // 查
        Account account = accountMapper.selectById(userId);
        // 改
        LambdaUpdateWrapper<Account> wrapper = new LambdaUpdateWrapper<>();
        wrapper.set(Account::getResidue, account.getResidue().subtract(money))
                .set(Account::getUsed, account.getUsed().add(money))
                .eq(Account::getUserId, userId);
        accountMapper.update(null, wrapper);

        log.info("------->account-service中扣减账户余额结束");
    }
}

```

8. 创建业务类 controller

```java
package com.yuehai.controller;

import com.yuehai.service.AccountService;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 8:51
 */

@RestController
public class AccountController {

    @Resource
    private AccountService accountService;

    /**
     * 扣减账户余额
     */
    @RequestMapping("/account/decrease")
    public JsonResult decrease(@RequestParam("userId") Long userId, @RequestParam("money") BigDecimal money){
        accountService.decrease(userId,money);
        return JsonResult.success("扣减账户余额成功！");
    }

}

```

9. 修改主启动类

```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * { @EnableDiscoveryClient }：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 * { @MapperScan("com.yuehai.mapper") }：扫描指定包下面的 mapper 接口
 */

@SpringBootApplication
@EnableDiscoveryClient
@MapperScan("com.yuehai.mapper")
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}

```

10. 查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322085641.png)

11. 启动项目，访问接口：http://localhost:2003/account/decrease?userId=1&money=2

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322090122.png)

13. 再次查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322090134.png)

14. 将数据修改回去
15. 查看 nacos

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322090243.png)

### ⑤、新建订单模块 seata-order-service2001

1. 新建模块 seata-order-service2001

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322090637.png)

2. 修改 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud_alibaba_seata</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <!-- 本项目的详细信息 -->
    <artifactId>seata-order-service2001</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包 -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- Nacos 作为服务注册与发现中心 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        <!-- feign 服务接口调用 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
        <!-- seata 分布式事务-->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>

    </dependencies>

</project>
```

3. 修改 application.yml 配置文件

```yml
# 服务端口号
server:
    port: 2001

# spring 配置
spring:
    application:
        # 服务名称 微服务 订单 模块 seata-order-service2001
        name: seata-order-service
    cloud:
        # nacos 配置
        nacos:
            discovery:
                # 配置 nacos 地址
                server-addr: 43.138.106.181:8848
    # 数据源配置
    datasource:
        # mysql驱动包 com.mysql.jdbc.Driver
        driver-class-name: com.mysql.jdbc.Driver
        # 连接信息
        # characterEncoding=UTF-8：指定所处理字符的解码和编码的格式
        # useSSL=false：不进行 SSL 连接
        # allowPublicKeyRetrieval=true：允许恶意代理执行MITM攻击以获取明文密码，因此它在默认情况下为False，必须显式启用
        # serverTimezone=GMT：格林尼治标准时间
        url: jdbc:mysql://43.138.106.181:3306/seata_order?characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=GMT
        # 用户名
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# openFeign 配置
feign:
    hystrix:
        # hystrix 熔断功能
        enabled: false

# feign 日志客户端配置
logging:
    level:
        # feign 日志以什么级别监控哪个接口
        com.yuehai.service.PaymentFeignService: debug
        io:
            seata: info

# seata 设置
seata:
    # seata 注册中心设置
    registry:
        # seata 注册中心类型
        type: nacos
        # seata 注册中心的 nacos 设置
        nacos:
            namespace:
            server-addr: 43.138.106.181:8848
            group: SEATA_GROUP
            username: nacos
            password: nacos
```

4. 创建实体类

```java
package com.yuehai.bean;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 9:11
 */

@TableName("t_order")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Order {
    private Long id;
    /**
     * 用户id
     */
    private Long userId;
    /**
     * 产品id
     */
    private Long productId;
    /**
     * 数量
     */
    private Integer count;
    /**
     * 金额
     */
    private BigDecimal money;
    /**
     * 订单状态：0：创建中；1：已完结
     */
    private Integer status;
}

```

5. 创建 mapper 接口

```java
package com.yuehai.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.yuehai.bean.Order;

/**
 * @author 月海
 * @create 2023/3/22 9:14
 */
public interface OrderMapper extends BaseMapper<Order> {
}

```

6. 创建 service 接口 OrderService

```java
package com.yuehai.service;

import com.yuehai.bean.Order;

/**
 * @author 月海
 * @create 2023/3/22 9:15
 */
public interface OrderService {
    /**
     * 创建订单
     */
    void create(Order order);
}

```

7. 创建 service 接口 StorageService

```java
package com.yuehai.service;

import com.yuehai.utils.JsonResult;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * @author 月海
 * @create 2023/3/22 9:22
 */

@FeignClient(value = "seata-storage-service")
public interface StorageService {

    /**
     * 扣减库存
     */
    @GetMapping(value = "/storage/decrease")
    JsonResult decrease(@RequestParam("productId") Long productId, @RequestParam("count") Integer count);

}

```

8. 创建 service 接口 AccountService

```java
package com.yuehai.service;

import com.yuehai.utils.JsonResult;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.math.BigDecimal;

/**
 * @author 月海
 * @create 2023/3/22 9:22
 */

@FeignClient(value = "seata-account-service")
public interface AccountService {

    /**
     * 扣减账户余额
     */
    @GetMapping("/account/decrease")
    JsonResult decrease(@RequestParam("userId") Long userId, @RequestParam("money") BigDecimal money);

}

```

9. 创建 OrderService 实现类 OrderServiceImpl，<font color="#ff0000">添加注解：`@GlobalTransactional(name = "fsp-create-order",rollbackFor = Exception.class)`</font>

```java
package com.yuehai.service.impl;

import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import com.yuehai.bean.Order;
import com.yuehai.mapper.OrderMapper;
import com.yuehai.service.AccountService;
import com.yuehai.service.OrderService;
import com.yuehai.service.StorageService;
import io.seata.spring.annotation.GlobalTransactional;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/22 9:20
 */

@Slf4j
@Service
public class OrderServiceImpl implements OrderService {

    @Resource
    private OrderMapper orderMapper;

    @Resource
    private StorageService storageService;

    @Resource
    private AccountService accountService;

    /**
     * 创建订单 -> 调用库存服务扣减库存 -> 调用账户服务扣减账户余额 -> 修改订单状态
     * 简单说：下订单 -> 减库存 -> 减余额 -> 改状态
     */
    @Override
    @GlobalTransactional(name = "fsp-create-order",rollbackFor = Exception.class)
    public void create(Order order) {

        log.info("------->下单开始");
        // 本应用创建订单
        orderMapper.insert(order);

        // 远程调用库存服务扣减库存
        log.info("------->order-service 中扣减库存开始");
        storageService.decrease(order.getProductId(), order.getCount());
        log.info("------->order-service 中扣减库存结束");

        // 远程调用账户服务扣减余额
        log.info("------->order-service 中扣减余额开始");
        accountService.decrease(order.getUserId(), order.getMoney());
        log.info("------->order-service 中扣减余额结束");

        // 修改订单状态为已完成；若不改，因为不传递状态这个参数，则为空
        log.info("------->order-service中修改订单状态开始");
        LambdaUpdateWrapper<Order> wrapper = new LambdaUpdateWrapper<>();
        wrapper.set(Order::getStatus, 1)
                        .eq(Order::getUserId, order.getUserId());
        orderMapper.update(null, wrapper);
        log.info("------->order-service中修改订单状态结束");

        // 下单结束
        log.info("------->下单结束");

    }
}

```

10. 创建业务类 controller

```java
package com.yuehai.controller;

import com.yuehai.bean.Order;
import com.yuehai.service.OrderService;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/22 9:31
 */

@RestController
public class OrderController {

    @Resource
    private OrderService orderService;

    /**
     * 创建订单 -> 调用库存服务扣减库存 -> 调用账户服务扣减账户余额 -> 修改订单状态
     */
    @GetMapping("/order/create")
    public JsonResult create(Order order) {
        orderService.create(order);
        return JsonResult.success("订单创建成功!");
    }

}

```

11. 修改主启动类

```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;

/**
 * 微服务 熔断与限流 cloudalibaba-sentinel-server8401 模块
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * { @EnableDiscoveryClient }：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 * { @EnableFeignClients：告诉框架扫描所有使用注解} @FeignClient 定义的 feign 客户端，并把 feign 客户端注册到 IOC 容器中
 * { @MapperScan("com.yuehai.mapper") }：扫描指定包下面的 mapper 接口
 */

@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
@MapperScan("com.yuehai.mapper")
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}

```

12. 查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322093521.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322093859.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322093504.png)

13. 启动项目，访问接口：http://localhost:2001/order/create?userId=1&productId=1&count=2&money=4

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322094422.png)

14. 再次查看数据库数据

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322094444.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322094455.png)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322094530.png)

### ⑥、模拟报错，查看事务是否正常

1. 在订单模块 seata-order-service2001 的 service 实现类中添加 `@GlobalTransactional(name = "fsp-create-order",rollbackFor = Exception.class)` 注解，之前已添加

```java
package com.yuehai.service.impl;

import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import com.yuehai.bean.Order;
import com.yuehai.mapper.OrderMapper;
import com.yuehai.service.AccountService;
import com.yuehai.service.OrderService;
import com.yuehai.service.StorageService;
import io.seata.spring.annotation.GlobalTransactional;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/3/22 9:20
 */

@Slf4j
@Service
public class OrderServiceImpl implements OrderService {

    @Resource
    private OrderMapper orderMapper;

    @Resource
    private StorageService storageService;

    @Resource
    private AccountService accountService;

    /**
     * 创建订单 -> 调用库存服务扣减库存 -> 调用账户服务扣减账户余额 -> 修改订单状态
     * 简单说：下订单 -> 减库存 -> 减余额 -> 改状态
     */
    @Override
    @GlobalTransactional(name = "fsp-create-order",rollbackFor = Exception.class)
    public void create(Order order) {

        log.info("------->下单开始");
        // 本应用创建订单
        orderMapper.insert(order);

        // 远程调用库存服务扣减库存
        log.info("------->order-service 中扣减库存开始");
        storageService.decrease(order.getProductId(), order.getCount());
        log.info("------->order-service 中扣减库存结束");

        // 远程调用账户服务扣减余额
        log.info("------->order-service 中扣减余额开始");
        accountService.decrease(order.getUserId(), order.getMoney());
        log.info("------->order-service 中扣减余额结束");

        // 修改订单状态为已完成；若不改，因为不传递状态这个参数，则为空
        log.info("------->order-service中修改订单状态开始");
        LambdaUpdateWrapper<Order> wrapper = new LambdaUpdateWrapper<>();
        wrapper.set(Order::getStatus, 1)
                        .eq(Order::getUserId, order.getUserId());
        orderMapper.update(null, wrapper);
        log.info("------->order-service中修改订单状态结束");

        // 下单结束
        log.info("------->下单结束");

    }
}

```

2. 在账户模块 seata-account-service2003  的 service 实现类中模拟超时异常

```java
package com.yuehai.service.impl;

import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import com.yuehai.bean.Account;
import com.yuehai.mapper.AccountMapper;
import com.yuehai.service.AccountService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.math.BigDecimal;
import java.util.concurrent.TimeUnit;

/**
 * @author 月海
 * @create 2023/3/22 8:42
 */

@Slf4j
@Service
public class AccountServiceImpl implements AccountService {

    @Resource
    private AccountMapper accountMapper;

    /**
     * 扣减账户余额
     */
    @Override
    public void decrease(Long userId, BigDecimal money) {
        log.info("------->account-service中扣减账户余额开始");
        // 模拟超时异常，全局事务回滚
        // 暂停几秒钟线程
        try { TimeUnit.SECONDS.sleep(3000); } catch (InterruptedException e) { e.printStackTrace(); }

        // 查
        Account account = accountMapper.selectById(userId);
        // 改
        LambdaUpdateWrapper<Account> wrapper = new LambdaUpdateWrapper<>();
        wrapper.set(Account::getResidue, account.getResidue().subtract(money))
                .set(Account::getUsed, account.getUsed().add(money))
                .eq(Account::getUserId, userId);
        accountMapper.update(null, wrapper);

        log.info("------->account-service中扣减账户余额结束");
    }
}

```

3. 重启三个项目，访问测试：http://localhost:2001/order/create?userId=1&productId=1&count=2&money=4，报错

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322102150.png)

4. 查看数据库，发现数据没有发生改变，分布式事务启用成功

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322102415.png)

## 6、一部分补充

### ①、再看 TC/TM/RM 三大组件

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322104936.png)

### ②、分布式事务的执行流程

1. TM 开启分布式事务（TM 向 TC 注册全局事务记录）；
2. 按业务场景，编排数据库、服务等事务内资源（RM 向 TC 汇报资源准备状态 ）；
3. TM 结束分布式事务，事务一阶段结束（TM 通知 TC 提交/回滚分布式事务）；
4. TC 汇总事务信息，决定分布式事务是提交还是回滚；
5. TC 通知所有 RM 提交/回滚 资源，事务二阶段结束。​

### ③、AT 模式如何做到对业务的无侵入

> http://seata.io/zh-cn/docs/overview/what-is-seata.html

#### Ⅰ、是什么

1. 前提：
	1. 基于支持本地 ACID 事务的关系型数据库。
	2. Java 应用，通过 JDBC 访问数据库。
2. 整体机制：两阶段提交协议的演变：
	1. 一阶段：业务数据和回滚日志记录在同一个本地事务中提交，释放本地锁和连接资源。
	2. 二阶段：
		1. 提交异步化，非常快速地完成。
		2. 回滚通过一阶段的回滚日志进行反向补偿。

#### Ⅱ、一阶段加载

- 在一阶段，Seata 会拦截“业务 SQL”：
1. 解析 SQL 语义，找到“业务 SQL”要更新的业务数据，在业务数据被更新前，将其保存成“before image”，
2. 执行“业务 SQL”更新业务数据，在业务数据更新之后，
3. 其保存成“after image”，最后生成行锁。
4. 以上操作全部在一个数据库事务内完成，这样保证了一阶段操作的原子性。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322105816.png)

#### Ⅲ、二阶段提交

1. 二阶段如果是顺利提交的话
2. 因为“业务 SQL”在一阶段已经提交至数据库，所以 Seata 框架只需将一阶段保存的快照数据和行锁删掉，完成数据清理即可。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322105901.png)

#### Ⅳ、二阶段回滚

- 二阶段回滚：
1. 二阶段如果是回滚的话，Seata 就需要回滚一阶段已经执行的“业务 SQL”，还原业务数据。
2. 回滚方式便是用“before image”还原业务数据；但在还原前要首先要校验脏写，对比“数据库当前业务数据”和 “after image”，
3. 如果两份数据完全一致就说明没有脏写，可以还原业务数据，如果不一致就说明有脏写，出现脏写就需要转人工处理。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322105944.png)

### ④、补充

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020230322110000.png)

# 五、容器安装整理

## 0、停止容器脚本

```shell
#!/bin/bash

# 定义一个函数来停止容器
stop_container() {
    # 从函数参数获取容器名称；local 关键字用于将变量限制在函数内部
    local container_name=$1
    # 输出一条消息，指示正在停止容器
    echo "正在停止容器中 $container_name ..."

    # 使用 docker stop 命令停止容器
    docker stop $container_name

    # 检查停止操作的状态
    if [ $? -eq 0 ]; then
        # 如果停止操作成功，则将停止成功的消息输出到 stop_containers.log 文件
        echo "$(date): docker 容器停止成功：$container_name " >> stop_containers.log
    else
        # 如果停止操作失败，则将停止失败的消息输出到 stop_containers.log 文件
        echo "$(date): docker 容器停止失败：$container_name " >> stop_containers.log
    fi
}

# 停止 code-sentinel-1 容器
stop_container code-sentinel-1
# 停止 code-redis-1 容器
stop_container code-nacos-1
```

## 1、nacos

### ①、v2.2.1

1. `v2.2.1` 的版本使用之前的容器命令启动不了，报错如下：

```shell
nested exception is java.lang.IllegalArgumentException: Could not resolve placeholder 'NACOS_AUTH_IDENTITY_KEY' in value "${NACOS_AUTH_IDENTITY_KEY}"
```

2. 原因：查询 [关于Nacos默认token.secret.key及server.identity风险说明及解决方案公告](https://nacos.io/zh-cn/blog/announcement-token-secret-key.html)，得知 2.2.1版本需要配置 `NACOS_AUTH_TOKEN`、`NACOS_AUTH_IDENTITY_KEY以` 及 `NACOS_AUTH_IDENTITY_VALUE` 这三个属性
3. 2.x 版本之后增加了 grpc 通信并且增加 nacos 的集群端口上下偏移 1000，即创建容器时除了 8848 还需要把 9848 也暴露出来。如：`-p 8848:8848 -p 9848:9848`，各个端口偏移量说明：

|端口|与主端口的偏移量|描述|
|----|----|----|
|8848|0|主端口，客户端、控制台及OpenAPI所使用的HTTP端口|
|9848|1000|客户端gRPC请求服务端端口，用于客户端向服务端发起连接和请求|
|9849|1001|服务端gRPC请求服务端端口，用于服务间同步等|
|7848|-1000|Jraft请求服务端端口，用于处理服务端间的Raft相关请求|

#### Ⅰ、NACOS_AUTH_TOKEN

> 文件md5在线计算：https://www.metools.info/other/o21.html

1. 可以直接用 md5 获取，但是单个 md5 值太短，如果只配了单个的话，启动会被告知

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020240314100603.png)

2. 说白了就是单个 md5 值太短了，那么我们把 `NACOS_AUTH_TOKEN` 设置成 2 个 md5 值拼起来就好

#### Ⅱ、NACOS_AUTH_IDENTITY_KEY 及 NACOS_AUTH_IDENTITY_VALUE

> JWT Token在线编码生成：https://tooltt.com/jwt-encode/

1. 通过下图可知 `NACOS_AUTH_IDENTITY_KEY` 及 `NACOS_AUTH_IDENTITY_VALUE` 是通过 `JWT` 方式自定义生成的：

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020240314100927.png)

2. 通过上面的网址 `jwt` 秘钥生成可以获取自定义 `jwt` 密钥：设置图中三个红框中的值
	1. `NACOS_AUTH_IDENTITY_KEY=y_chat_nacos_auth_identity_key`
	2. `NACOS_AUTH_IDENTITY_VALUE=y_chat_nacos_auth_identity_value`

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020240314101623.png)

3. 点击编码按钮即可获取秘钥

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fjava%2Fattachments%2FPasted%20image%2020240314101707.png)

4. 此次密钥为：`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjpbeyJ5X2NoYXRfbmFjb3NfYXV0aF9pZGVudGl0eV9rZXkiOiJ5X2NoYXRfbmFjb3NfYXV0aF9pZGVudGl0eV92YWx1ZSJ9XSwiaWF0IjoxNzEwMzgyNjEzLCJleHAiOjI1MjQ0OTI3OTksImF1ZCI6IiIsImlzcyI6IiIsInN1YiI6IiJ9.ybcX8tnTigKG1rGDUQ7ckTGowtepxDuRYhfGi0koT0Q`

#### Ⅲ、创建配置文件

1. 创建文件：`touch /home/docker/docker/volumes/nacos/nacos1/app-config/application.properties`
2. 输入以下内容：`nano /home/docker/docker/volumes/nacos/nacos1/app-config/application.properties`
3. 记得修改对应的配置信息

```shell                                           
### 如果使用 MySQL 作为数据源：
spring.datasource.platform=mysql
 
### 数据源数量:
db.num=1
 
### 数据源连接信息:
### characterEncoding=utf8：设置字符编码为 UTF-8，确保数据在数据库和应用程序之间传输时正确处理 Unicode 字符。
### connectTimeout=10000：设置建立数据库连接的超时时间，单位是毫秒。这里设置为 10000 毫秒（10 秒），如果在这段时间内无法建立连接，将抛出超时异常。
### socketTimeout=30000：设置套接字读取数据的超时时间，单位是毫秒。这里设置为 30000 毫秒（30 秒），用于控制等待数据的最长时间。
### autoReconnect=true：当数据库连接意外中断时，设置为 true 将自动尝试重新连接。
### useUnicode=true：设置为 true 表示使用 Unicode 字符集。通常与 characterEncoding 参数配合使用，确保应用程序可以正确处理国际字符。
### useSSL=false：设置为 false 表示不使用 SSL 加密连接数据库。这在内部网络环境中可以减少加密解密的性能开销。
### serverTimezone=UTC：设置数据库服务器的时区为 UTC。这有助于解决服务器和客户端时区不一致时可能出现的时间相关问题。
### allowPublicKeyRetrieval=true：设置为 true 允许客户端从服务器获取公钥，这通常用于安全的密码验证。
db.url.0=jdbc:mysql://www.yue-hai.top:10200/y_chat_nacos_config?characterEncoding=utf8&connectTimeout=10000&socketTimeout=30000&autoReconnect=true&useUnicode=true&useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
db.user.0=yan
db.password.0=Ccj19960920...

### 鉴权配置，不加的话启动会报错
nacos.core.auth.plugin.nacos.token.secret.key=5d94126de34a6a9cffd67c234919dbdacbac694da5841d5e3af07c8ce1154537
# 启用或禁用 Nacos 的认证功能。设置为 true 时，Nacos 将开启用户认证
nacos.core.auth.enabled=true

# 设置认证服务的标识键（identity key）。这是一个自定义的键，用于在进行服务之间的认证或通信时标识请求的来源或类别
nacos.core.auth.server.identity.key=y_chat_nacos_auth_identity_key
# 对应于上面的 identity key，这是该键的值。它的内容也是自定义的，用于与 identity key 配合使用，形成一个键值对，标识特定的服务或请求类型
nacos.core.auth.server.identity.value=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjpbeyJ5X2NoYXRfbmFjb3NfYXV0aF9pZGVudGl0eV9rZXkiOiJ5X2NoYXRfbmFjb3NfYXV0aF9pZGVudGl0eV92YWx1ZSJ9XSwiaWF0IjoxNzEwMzgyNjEzLCJleHAiOjI1MjQ0OTI3OTksImF1ZCI6IiIsImlzcyI6IiIsInN1YiI6IiJ9.ybcX8tnTigKG1rGDUQ7ckTGowtepxDuRYhfGi0koT0Q

# 控制是否启用基于用户代理（User-Agent）的白名单认证。当设置为 true 时，Nacos 会根据预定义的用户代理白名单来认证请求，允许在白名单中的用户代理绕过正常的用户认证
#nacos.core.auth.enable.userAgentAuthWhite=false
```

#### Ⅳ、启动命令

1. 不映射目录做持久化

```shell
docker run -d \
    -p 15000:8848 \
	-p 16000:9848 \
	-p 16001:9849 \
	-p 14000:7848 \
    -e MODE=standalone \
	-v /home/docker/docker/volumes/nacos/nacos1/app-config/application.properties:/home/nacos/conf/application.properties \
    --name code-nacos-1 \
    --restart=always \
    nacos/nacos-server:v2.2.1
```

2. 配置文件和日志复制：

```shell
docker cp code-nacos-1:/home/nacos/conf/ /home/docker/docker/volumes/nacos/nacos1/

docker cp code-nacos-1:/home/nacos/logs/ /home/docker/docker/volumes/nacos/nacos1/

docker cp code-nacos-1:/home/nacos/data/ /home/docker/docker/volumes/nacos/nacos1/
```


3. 停止并删除刚才启动的 nacos 容器：

```shell
# 停止容器
docker stop code-nacos-1

# 删除容器
docker rm code-nacos-1
```

4. 映射目录做持久化

```shell
docker run -d \
    -p 15000:8848 \
	-p 16000:9848 \
	-p 16001:9849 \
	-p 14000:7848 \
    -e MODE=standalone \
	-v /home/docker/docker/volumes/nacos/nacos1/conf/:/home/nacos/conf \
    -v /home/docker/docker/volumes/nacos/nacos1/logs/:/home/nacos/logs \
    -v /home/docker/docker/volumes/nacos/nacos1/data/:/home/nacos/data \
    --name code-nacos-1 \
    --restart=always \
    nacos/nacos-server:v2.2.1
```

3. 访问测试：[http://www.yue-hai.top:15000/nacos/#/login](http://www.yue-hai.top:15000/nacos/#/login)

#### Ⅴ、对应的数据表

```sql
/*
 * Copyright 1999-2018 Alibaba Group Holding Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info   */
/******************************************/
CREATE TABLE `config_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) DEFAULT NULL,
  `content` longtext NOT NULL COMMENT 'content',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  `app_name` varchar(128) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `c_desc` varchar(256) DEFAULT NULL,
  `c_use` varchar(64) DEFAULT NULL,
  `effect` varchar(64) DEFAULT NULL,
  `type` varchar(64) DEFAULT NULL,
  `c_schema` text,
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfo_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_aggr   */
/******************************************/
CREATE TABLE `config_info_aggr` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `datum_id` varchar(255) NOT NULL COMMENT 'datum_id',
  `content` longtext NOT NULL COMMENT '内容',
  `gmt_modified` datetime NOT NULL COMMENT '修改时间',
  `app_name` varchar(128) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfoaggr_datagrouptenantdatum` (`data_id`,`group_id`,`tenant_id`,`datum_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='增加租户字段';


/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_beta   */
/******************************************/
CREATE TABLE `config_info_beta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL COMMENT 'content',
  `beta_ips` varchar(1024) DEFAULT NULL COMMENT 'betaIps',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfobeta_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_beta';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_info_tag   */
/******************************************/
CREATE TABLE `config_info_tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `tenant_id` varchar(128) DEFAULT '' COMMENT 'tenant_id',
  `tag_id` varchar(128) NOT NULL COMMENT 'tag_id',
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL COMMENT 'content',
  `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `src_user` text COMMENT 'source user',
  `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_configinfotag_datagrouptenanttag` (`data_id`,`group_id`,`tenant_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info_tag';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = config_tags_relation   */
/******************************************/
CREATE TABLE `config_tags_relation` (
  `id` bigint(20) NOT NULL COMMENT 'id',
  `tag_name` varchar(128) NOT NULL COMMENT 'tag_name',
  `tag_type` varchar(64) DEFAULT NULL COMMENT 'tag_type',
  `data_id` varchar(255) NOT NULL COMMENT 'data_id',
  `group_id` varchar(128) NOT NULL COMMENT 'group_id',
  `tenant_id` varchar(128) DEFAULT '' COMMENT 'tenant_id',
  `nid` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `uk_configtagrelation_configidtag` (`id`,`tag_name`,`tag_type`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_tag_relation';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = group_capacity   */
/******************************************/
CREATE TABLE `group_capacity` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `group_id` varchar(128) NOT NULL DEFAULT '' COMMENT 'Group ID，空字符表示整个集群',
  `quota` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数，，0表示使用默认值',
  `max_aggr_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='集群、各Group容量信息表';

/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = his_config_info   */
/******************************************/
CREATE TABLE `his_config_info` (
  `id` bigint(20) unsigned NOT NULL,
  `nid` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `data_id` varchar(255) NOT NULL,
  `group_id` varchar(128) NOT NULL,
  `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
  `content` longtext NOT NULL,
  `md5` varchar(32) DEFAULT NULL,
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `src_user` text,
  `src_ip` varchar(50) DEFAULT NULL,
  `op_type` char(10) DEFAULT NULL,
  `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
  `encrypted_data_key` text NOT NULL COMMENT '秘钥',
  PRIMARY KEY (`nid`),
  KEY `idx_gmt_create` (`gmt_create`),
  KEY `idx_gmt_modified` (`gmt_modified`),
  KEY `idx_did` (`data_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='多租户改造';


/******************************************/
/*   数据库全名 = nacos_config   */
/*   表名称 = tenant_capacity   */
/******************************************/
CREATE TABLE `tenant_capacity` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `tenant_id` varchar(128) NOT NULL DEFAULT '' COMMENT 'Tenant ID',
  `quota` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '配额，0表示使用默认值',
  `usage` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '使用量',
  `max_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个配置大小上限，单位为字节，0表示使用默认值',
  `max_aggr_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '聚合子配置最大个数',
  `max_aggr_size` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '单个聚合数据的子配置大小上限，单位为字节，0表示使用默认值',
  `max_history_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最大变更历史数量',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='租户容量信息表';


CREATE TABLE `tenant_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `kp` varchar(128) NOT NULL COMMENT 'kp',
  `tenant_id` varchar(128) default '' COMMENT 'tenant_id',
  `tenant_name` varchar(128) default '' COMMENT 'tenant_name',
  `tenant_desc` varchar(256) DEFAULT NULL COMMENT 'tenant_desc',
  `create_source` varchar(32) DEFAULT NULL COMMENT 'create_source',
  `gmt_create` bigint(20) NOT NULL COMMENT '创建时间',
  `gmt_modified` bigint(20) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_tenant_info_kptenantid` (`kp`,`tenant_id`),
  KEY `idx_tenant_id` (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='tenant_info';

CREATE TABLE `users` (
	`username` varchar(50) NOT NULL PRIMARY KEY,
	`password` varchar(500) NOT NULL,
	`enabled` boolean NOT NULL
);

CREATE TABLE `roles` (
	`username` varchar(50) NOT NULL,
	`role` varchar(50) NOT NULL,
	UNIQUE INDEX `idx_user_role` (`username` ASC, `role` ASC) USING BTREE
);

CREATE TABLE `permissions` (
    `role` varchar(50) NOT NULL,
    `resource` varchar(255) NOT NULL,
    `action` varchar(8) NOT NULL,
    UNIQUE INDEX `uk_role_permission` (`role`,`resource`,`action`) USING BTREE
);

INSERT INTO users (username, password, enabled) VALUES ('nacos', '$2a$10$EuWPZHzz32dJN7jexM34MOeYirDdFAZm2kuWj7VEOJhhZkDrxfvUu', TRUE);

INSERT INTO roles (username, role) VALUES ('nacos', 'ROLE_ADMIN');
```

### ②、

### ③、

## 2、sentinel

```shell
docker run -d -p 11000:8858 --name code-sentinel-1 bladex/sentinel-dashboard:1.8.7
```

## 3、

## 4、
