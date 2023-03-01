# 一、SpringCloud Alibaba 入门简介
> 官网：https://spring.io/projects/spring-cloud-alibaba#overview
> 
> 英文：https://github.com/alibaba/spring-cloud-alibaba
> 
> https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html
> 
> 中文：https://github.com/alibaba/spring-cloud-alibaba/blob/master/README-zh.md
> 
## 1、为什么会出现 SpringCloud Alibaba
<font color="#c00000">Spring Cloud Netflix 项目进入维护模式</font>

![](attachments/Pasted%20image%2020230301095557.png)

1.  什么是维护模式：将模块置于维护模式，意味着 Spring Cloud 团队将不会再向模块添加新功能。我们将修复 block 级别的 bug 以及安全问题，我们也会考虑并审查社区的小型 pull request。

![](attachments/Pasted%20image%2020230301095456.png)

2.  进入维护模式意味着什么呢：
	1.  Spring Cloud Netflix 将不再开发新的组件：我们都知道 Spring Cloud 版本迭代算是比较快的，因而出现了很多重大 ISSUE 都还来不及 Fix 就又推另一个 Release 了。进入维护模式意思就是目前一直以后一段时间 Spring Cloud Netflix 提供的服务和功能就这么多了，不在开发新的组件和功能了。以后将以维护和 Merge分支Full Request为主
	2.  新组件功能将以其他替代平代替的方式实现

![](attachments/Pasted%20image%2020230301095846.png)

## 2、SpringCloud alibaba 带来了什么
### ①、是什么

-   诞生：2018.10.31，Spring Cloud Alibaba 正式入驻了 Spring Cloud 官方孵化器，并在 Maven 中央库发布了第一个版本。

![](attachments/Pasted%20image%2020230301100546.png)

### ②、能干嘛
1.  服务限流降级：默认支持 Servlet、Feign、RestTemplate、Dubbo 和 RocketMQ 限流降级功能的接入，可以在运行时通过控制台实时修改限流降级规则，还支持查看限流降级 Metrics 监控。
2.  服务注册与发现：适配 Spring Cloud 服务注册与发现标准，默认集成了 Ribbon 的支持。
3.  分布式配置管理：支持分布式系统中的外部化配置，配置更改时自动刷新。
4.  消息驱动能力：基于 Spring Cloud Stream 为微服务应用构建消息驱动能力。
5.  阿里云对象存储：阿里云提供的海量、安全、低成本、高可靠的云存储服务。支持在任何应用、任何时间、任何地点存储和访问任意类型的数据。
6.  分布式任务调度：提供秒级、精准、高可靠、高可用的定时（基于 Cron 表达式）任务调度服务。同时提供分布式的任务执行模型，如网格任务。网格任务支持海量子任务均匀分配到所有 Worker（schedulerx-client）上执行。
### ③、怎么用

![](attachments/Pasted%20image%2020230301100615.png)

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

![](attachments/Pasted%20image%2020230301101226.png)

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

1.  创建文件夹：`/home/docker/docker/VOLUME/nacos/`

![](attachments/Pasted%20image%2020230301101430.png)

4.  配置文件和日志复制：`docker cp nacos:/home/nacos/conf/ ~/docker/VOLUME/nacos/`、`docker cp nacos:/home/nacos/logs/ ~/docker/VOLUME/nacos/`

![](attachments/Pasted%20image%2020230301101555.png)

5.  单机版部署：
	```bash
	docker run -d \
	  -e MODE=standalone \
	  -e TIME_ZONE='Asia/Shanghai' \
	  -v ~/docker/VOLUME/nacos/conf:/home/nacos/conf \
	  -v ~/docker/VOLUME/nacos/logs:/home/nacos/logs \
	  -p 8848:8848 \
	  --name nacos \
	  nacos/nacos-server:latest
	```

1.  `-e MODE=standalone`：以单机模式启动
2.  `-e TIME_ZONE='Asia/Shanghai'`：设置时区为上海

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

1.  访问：[http://43.138.106.181:8848/nacos/#/login](http://43.138.106.181:8848/nacos/#/login)

![](attachments/Pasted%20image%2020230301105146.png)

7.  输入账号密码 nacos 登录

![](attachments/Pasted%20image%2020230301105211.png)

## 3、Nacos 作为服务注册中心演示
官网文档：[https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_nacos_config](https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_nacos_config)
### ①、基于 Nacos的 服务提供者

1.  新建模块 cloudalibaba-provider-payment9001

![](attachments/Pasted%20image%2020230301111239.png)

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
    
        <!--SpringCloud ailibaba nacos -->
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

![](attachments/Pasted%20image%2020230301105945.png)

8.  启动项目，查看控制台：[http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=](http://43.138.106.181:8848/nacos/#/serviceManagement?dataId=&group=&appName=&namespace=)

![](attachments/Pasted%20image%2020230301110012.png)

9.  参照 9001 新建 9002

![](attachments/Pasted%20image%2020230301112205.png)

10. 启动两个模块

![](attachments/Pasted%20image%2020230301123726.png)
### ②、基于 Nacos 的服务消费者

1. 新建模块 cloudalibaba-consumer-nacos-order83

![](attachments/Pasted%20image%2020230301124753.png)

2. 修改 pom.xml

```xml

```

3. 修改 application.yml 配置文件

```yml

```

4. 修改主启动类

```java

```

5. 创建业务类

```java

```

6. 1
7. 1

### ③、服务注册中心对比
## 4、Nacos 作为服务配置中心演示
## 5、Nacos 集群和持久化配置（重要）
### ①、集群版部署
1.  集群版部署：
	```bash
	docker run -d --name nacos-cluster -p 8848:8848 \
	  --env NACOS_SERVERS=192.168.56.102,192.168.56.104,192.168.56.105 \
	  --env NACOS_SERVER_IP=192.168.56.102 \
	  --env SPRING_DATASOURCE_PLATFORM=mysql \
	  --env MYSQL_SERVICE_HOST=192.168.56.103 \
	  --env MYSQL_SERVICE_DB_NAME=nacos \
	  --env MYSQL_SERVICE_USER=root \
	  --env MYSQL_SERVICE_PASSWORD=123456 \
	  --env MYSQL_DATABASE_NUM=1 \
	  nacos/nacos-server
	```

	1.  `NACOS_SERVERS`：集群节点信息
	2.  `NACOS_SERVER_IP`：服务 IP，多网卡模式下建议指定
	3.  `SPRING_DATASOURCE_PLATFORM`：使用数据库类型
	4.  `MYSQL_SERVICE_HOST`：MySQL 数据库地址
	5.  `MYSQL_SERVICE_DB_NAM`：数据库名称
	6.  `MYSQL_SERVICE_DB_NAME`：数据库用户名
	7.  `MYSQL_SERVICE_PASSWORD`：数据库密码
	8.  `MYSQL_DATABASE_NUM`：数据库数量，默认就是 1，可以不填写

# 三、Sentinel 实现熔断与限流
# 四、Seata 处理分布式事务
# 五、

1. 新建模块 cloudalibaba-consumer-nacos-order83



2. 修改 pom.xml

```xml

```

3. 修改 application.yml 配置文件

```yml

```

4. 修改主启动类

```java

```

5. 创建业务类

```java

```

6. 1
7. 1
