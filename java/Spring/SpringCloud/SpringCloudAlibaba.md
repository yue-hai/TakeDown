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
    
        <!--SpringCloud ailibaba nacos -->
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

![](attachments/Pasted%20image%2020230301134603.png)
### ③、服务注册中心对比
#### Ⅰ、Nacos 全景图

![](attachments/Pasted%20image%2020230301134845.png)

#### Ⅱ、Nacos 和 CAP

![](attachments/Pasted%20image%2020230301135007.png)

![](attachments/Pasted%20image%2020230301135023.png)

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

![](attachments/Pasted%20image%2020230301140738.png)

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
    
        <!-- SpringCloud ailibaba nacos-config-->
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

![](attachments/Pasted%20image%2020230301144452.png)

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

![](attachments/Pasted%20image%2020230301144823.png)

4. 历史配置：Nacos 会记录配置文件的历史版本默认保留 30 天，此外还有一键回滚功能，回滚操作将会触发配置更新
5. 回滚：

![](attachments/Pasted%20image%2020230301145024.png)
#### Ⅲ、测试
1. 查看 Data ID 是否对应
2. 启动 3377
3. 访问测试：http://localhost:3377/getConfig

![](attachments/Pasted%20image%2020230301145759.png)

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
![](attachments/Pasted%20image%2020230301153705.png)

2. 命名空间 Namespace：

![](attachments/Pasted%20image%2020230301153747.png)
#### Ⅲ、Namespace + Group + DataID 三者关系？为什么这么设计？
1.  是什么：类似 Java 里面的 package 名和类名；最外层的 namespace 是可以用于区分部署环境的，Group 和 DataID 逻辑上区分两个目标对象。
2. 三者情况：

![](attachments/Pasted%20image%2020230301154303.png)

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

![](attachments/Pasted%20image%2020230301160629.png)

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

![](attachments/Pasted%20image%2020230301161103.png)
##### （2）、Group 方案
1. 新建两个 Group，分别为：`DEV_GROUP`、`TEST_GROUP`

![](attachments/Pasted%20image%2020230301162046.png)

2. 两个新的配置文件创建

![](attachments/Pasted%20image%2020230301162228.png)

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

![](attachments/Pasted%20image%2020230301163047.png)
##### （3）、Namespace 方案
1. 新建 dev/test 的 Namespace

![](attachments/Pasted%20image%2020230301163329.png)

2. 创建完成之后

![](attachments/Pasted%20image%2020230301163405.png)

3. 回到服务管理-服务列表查看

![](attachments/Pasted%20image%2020230301163442.png)

4. 新建配置 nacos-config-client-info.yaml

![](attachments/Pasted%20image%2020230301165958.png)

5. 创建完成

![](attachments/Pasted%20image%2020230301165156.png)

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

![](attachments/Pasted%20image%2020230302085924.png)

## 5、Nacos 集群和持久化配置（重要）
### ①、官网说明
> https://nacos.io/zh-cn/docs/cluster-mode-quick-start.html

#### Ⅰ、官网集群部署说明
1. 集群部署架构图：
2. 因此开源的时候推荐用户把所有服务列表放到一个vip下面，然后挂到一个域名下面
3. http://ip1:port/openAPI 直连ip模式，机器挂则需要修改ip才可以使用。
4. http://SLB:port/openAPI 挂载SLB模式(内网SLB，不可暴露到公网，以免带来安全风险)，直连SLB即可，下面挂server真实ip，可读性不好。
5. http://nacos.com:port/openAPI 域名 + SLB模式(内网SLB，不可暴露到公网，以免带来安全风险)，可读性好，而且换ip方便，推荐模式

![](attachments/Pasted%20image%2020230302091737.png)

#### Ⅱ、上图官网翻译，真实情况

![](attachments/Pasted%20image%2020230302091758.png)

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

![](attachments/Pasted%20image%2020230302105504.png)

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

![](attachments/Pasted%20image%2020230303085001.png)

6. 创建数据库：nacos-config

![](attachments/Pasted%20image%2020230302111311.png)

7. 执行刚才的 sql 脚本，查看生成的表

![](attachments/Pasted%20image%2020230302111524.png)

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

![](attachments/Pasted%20image%2020230302134154.png)

10. 添加一个配置：

![](attachments/Pasted%20image%2020230302134528.png)

11. 查看数据库：

![](attachments/Pasted%20image%2020230302134728.png)

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

![](attachments/Pasted%20image%2020230303091257.png)

![](attachments/Pasted%20image%2020230303091322.png)
#### Ⅲ、1 个 Nginx
1. 创建 `/home/docker/docker/VOLUME/nginx-nacos/` 目录，并进入：`cd /home/docker/docker/VOLUME/nginx-nacos/`，并在其中创建 `conf` 目录

![](attachments/Pasted%20image%2020230303101659.png)

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

![](attachments/Pasted%20image%2020230303102410.png)

7. 登录进入，添加配置：`nacos-config-client-info.yaml`

![](attachments/Pasted%20image%2020230303102703.png)

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

![](attachments/Pasted%20image%2020230303103120.png)

### ④、高可用小总结

![](attachments/Pasted%20image%2020230303103235.png)

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

## 1、

## 2、

## 3、

## 4、

## 5、

## 6、

## 7、

## 8、

## 9、

---

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

### ⑩、

### ⑪、⑫、⑬、⑭、⑮、⑯、⑰、⑱、⑲、⑳

### ㉑、㉒、㉓、㉔、㉕、㉖、㉗、㉘、㉙、㉚

### ㉛、㉜、㉝、㉞、㉟、㊱、㊲、㊳、㊴、㊵

### ㊶、㊷、㊸、㊹、㊺、㊻、㊼、㊽、㊾、㊿

#### Ⅰ、

#### Ⅱ、

#### Ⅲ、

#### Ⅳ、

#### Ⅴ、

#### Ⅵ、

#### Ⅶ、

#### Ⅷ、

#### Ⅸ、

#### Ⅹ、