> 尚硅谷 2020 SpringCloud 框架开发教程：[https://www.bilibili.com/video/BV18E411x7eT/](https://www.bilibili.com/video/BV18E411x7eT/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676868390430-ab1bfae0-604f-456b-aeb9-beea7e713ee7.png#averageHue=%23fefdfd&clientId=u427792cf-17a4-4&from=paste&height=421&id=q5I3S&name=image.png&originHeight=432&originWidth=1313&originalType=binary&ratio=1&rotation=0&showTitle=false&size=58723&status=done&style=stroke&taskId=ud439b08d-aa52-4e19-83a1-35c9d3c0628&title=&width=1279)
# 一、SpringCloud 简介
> 1. Spring Cloud 官方文档：[https://cloud.spring.io/spring-cloud-static/Hoxton.SR1/reference/htmlsingle/](https://cloud.spring.io/spring-cloud-static/Hoxton.SR1/reference/htmlsingle/)
> 2. Spring Cloud 中文文档：[https://www.bookstack.cn/read/spring-cloud-docs/docs-index.md](https://www.bookstack.cn/read/spring-cloud-docs/docs-index.md)

## 1、优质集成项目
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676860544050-06e09ecb-ff1e-4ef3-a3b8-0aeb5efdced6.png#averageHue=%23b9bc80&clientId=u427792cf-17a4-4&from=paste&height=733&id=u27d22e4c&name=image.png&originHeight=733&originWidth=1352&originalType=binary&ratio=1&rotation=0&showTitle=false&size=708169&status=done&style=stroke&taskId=ua806a6fb-ec53-40b7-822d-9f044b59e37&title=&width=1352)
## 2、技术栈

- 里面的是官方的，外面的是第三方的

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676860919584-fcf94b57-b314-44ce-8014-2b688acd4e67.png#averageHue=%23cdc68d&clientId=u427792cf-17a4-4&from=paste&height=790&id=u4e74e485&name=image.png&originHeight=790&originWidth=1415&originalType=binary&ratio=1&rotation=0&showTitle=false&size=538644&status=done&style=stroke&taskId=u49e209dd-98c8-4923-bf81-fab1dd6a462&title=&width=1415)
## 3、核心技术栈
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676861063870-5034a489-75e6-4bd7-8323-34f9da145603.png#averageHue=%23072945&clientId=u427792cf-17a4-4&from=paste&height=476&id=udd29a4e6&name=image.png&originHeight=476&originWidth=967&originalType=binary&ratio=1&rotation=0&showTitle=false&size=237339&status=done&style=stroke&taskId=u438f825e-a609-481a-bbb2-d5a825607de&title=&width=967)
## 4、Springcloud 和 Springboot 之间的依赖关系如何看

1. 版本依赖关系：[https://spring.io/projects/spring-cloud#overview](https://spring.io/projects/spring-cloud#overview)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676867958623-90fb1467-c74d-41c2-928a-3b8c9945be43.png#averageHue=%23fcf4f2&clientId=u427792cf-17a4-4&from=paste&height=643&id=u92166a41&name=image.png&originHeight=643&originWidth=737&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84598&status=done&style=stroke&taskId=u541be3c1-d55f-42e7-ac9d-427438bf8cc&title=&width=737)

2. 详细的版本对应查看方法：[https://start.spring.io/actuator/info](https://start.spring.io/actuator/info)
```json
{
    "git": {
        "branch": "62b85c970273a427d709d044edacec0ea8c6917a",
        "commit": {
            "id": "62b85c9",
            "time": "2023-02-14T16:04:15Z"
        }
    },
    "build": {
        "version": "0.0.1-SNAPSHOT",
        "artifact": "start-site",
        "versions": {
            "spring-boot": "3.0.2",
            "initializr": "0.20.0-SNAPSHOT"
        },
        "name": "start.spring.io website",
        "time": "2023-02-14T16:49:14.707Z",
        "group": "io.spring.start"
    },
    "bom-ranges": {
        "codecentric-spring-boot-admin": {
            "2.4.3": "Spring Boot >=2.3.0.M1 and <2.5.0-M1",
            "2.5.6": "Spring Boot >=2.5.0.M1 and <2.6.0-M1",
            "2.6.8": "Spring Boot >=2.6.0.M1 and <2.7.0-M1",
            "2.7.4": "Spring Boot >=2.7.0.M1 and <3.0.0-M1",
            "3.0.0-M4": "Spring Boot >=3.0.0-M1 and <3.1.0-M1"
        },
        "solace-spring-boot": {
            "1.1.0": "Spring Boot >=2.3.0.M1 and <2.6.0-M1",
            "1.2.2": "Spring Boot >=2.6.0.M1 and <3.0.0-M1"
        },
        "solace-spring-cloud": {
            "1.1.1": "Spring Boot >=2.3.0.M1 and <2.4.0-M1",
            "2.1.0": "Spring Boot >=2.4.0.M1 and <2.6.0-M1",
            "2.3.2": "Spring Boot >=2.6.0.M1 and <3.0.0-M1"
        },
        "spring-cloud": {
            "Hoxton.SR12": "Spring Boot >=2.2.0.RELEASE and <2.4.0.M1",
            "2020.0.6": "Spring Boot >=2.4.0.M1 and <2.6.0-M1",
            "2021.0.0-M1": "Spring Boot >=2.6.0-M1 and <2.6.0-M3",
            "2021.0.0-M3": "Spring Boot >=2.6.0-M3 and <2.6.0-RC1",
            "2021.0.0-RC1": "Spring Boot >=2.6.0-RC1 and <2.6.1",
            "2021.0.5": "Spring Boot >=2.6.1 and <3.0.0-M1",
            "2022.0.0-M1": "Spring Boot >=3.0.0-M1 and <3.0.0-M2",
            "2022.0.0-M2": "Spring Boot >=3.0.0-M2 and <3.0.0-M3",
            "2022.0.0-M3": "Spring Boot >=3.0.0-M3 and <3.0.0-M4",
            "2022.0.0-M4": "Spring Boot >=3.0.0-M4 and <3.0.0-M5",
            "2022.0.0-M5": "Spring Boot >=3.0.0-M5 and <3.0.0-RC1",
            "2022.0.0-RC1": "Spring Boot >=3.0.0-RC1 and <3.0.0-RC2",
            "2022.0.0-RC2": "Spring Boot >=3.0.0-RC2 and <3.0.0",
            "2022.0.1": "Spring Boot >=3.0.0 and <3.1.0-M1"
        },
        "spring-cloud-azure": {
            "4.6.0": "Spring Boot >=2.5.0.M1 and <3.0.0-M1",
            "5.0.0": "Spring Boot >=3.0.0-M1 and <3.1.0-M1"
        },
        "spring-cloud-gcp": {
            "2.0.11": "Spring Boot >=2.4.0-M1 and <2.6.0-M1",
            "3.4.4": "Spring Boot >=2.6.0-M1 and <3.0.0-M1",
            "4.1.0": "Spring Boot >=3.0.0-M1 and <3.1.0-M1"
        },
        "spring-cloud-services": {
            "2.3.0.RELEASE": "Spring Boot >=2.3.0.RELEASE and <2.4.0-M1",
            "2.4.1": "Spring Boot >=2.4.0-M1 and <2.5.0-M1",
            "3.3.0": "Spring Boot >=2.5.0-M1 and <2.6.0-M1",
            "3.4.0": "Spring Boot >=2.6.0-M1 and <2.7.0-M1",
            "3.5.0": "Spring Boot >=2.7.0-M1 and <3.0.0-M1",
            "4.0.0": "Spring Boot >=3.0.0 and <3.1.0-M1"
        },
        "spring-shell": {
            "2.1.6": "Spring Boot >=2.7.0 and <3.0.0-M1",
            "3.0.0": "Spring Boot >=3.0.0 and <3.1.0-M1"
        },
        "vaadin": {
            "14.9.6": "Spring Boot >=2.1.0.RELEASE and <2.6.0-M1",
            "23.2.15": "Spring Boot >=2.6.0-M1 and <2.7.0-M1",
            "23.3.5": "Spring Boot >=2.7.0-M1 and <2.8.0-M1"
        },
        "wavefront": {
            "2.0.2": "Spring Boot >=2.1.0.RELEASE and <2.4.0-M1",
            "2.1.1": "Spring Boot >=2.4.0-M1 and <2.5.0-M1",
            "2.2.2": "Spring Boot >=2.5.0-M1 and <2.7.0-M1",
            "2.3.4": "Spring Boot >=2.7.0-M1 and <3.0.0-M1",
            "3.0.1": "Spring Boot >=3.0.0-M1 and <3.1.0-M1"
        }
    },
    "dependency-ranges": {
        "okta": {
            "1.4.0": "Spring Boot >=2.2.0.RELEASE and <2.4.0-M1",
            "1.5.1": "Spring Boot >=2.4.0-M1 and <2.4.1",
            "2.0.1": "Spring Boot >=2.4.1 and <2.5.0-M1",
            "2.1.6": "Spring Boot >=2.5.0-M1 and <3.0.0-M1",
            "3.0.2": "Spring Boot >=3.0.0-M1 and <3.1.0-M1",
            "managed": "Spring Boot >=3.1.0-M1"
        },
        "mybatis": {
            "2.1.4": "Spring Boot >=2.1.0.RELEASE and <2.5.0-M1",
            "2.2.2": "Spring Boot >=2.5.0-M1 and <2.7.0-M1",
            "2.3.0": "Spring Boot >=2.7.0-M1 and <3.0.0-M1",
            "3.0.0": "Spring Boot >=3.0.0-M1"
        },
        "camel": {
            "3.5.0": "Spring Boot >=2.3.0.M1 and <2.4.0-M1",
            "3.10.0": "Spring Boot >=2.4.0.M1 and <2.5.0-M1",
            "3.13.0": "Spring Boot >=2.5.0.M1 and <2.6.0-M1",
            "3.17.0": "Spring Boot >=2.6.0.M1 and <2.7.0-M1",
            "3.20.2": "Spring Boot >=2.7.0.M1 and <3.0.0-M1",
            "4.0.0-M1": "Spring Boot >=3.0.0-M1 and <3.1.0-M1"
        },
        "picocli": {
            "4.7.0": "Spring Boot >=2.5.0.RELEASE and <3.1.0-M1"
        },
        "open-service-broker": {
            "3.2.0": "Spring Boot >=2.3.0.M1 and <2.4.0-M1",
            "3.3.1": "Spring Boot >=2.4.0-M1 and <2.5.0-M1",
            "3.4.1": "Spring Boot >=2.5.0-M1 and <2.6.0-M1",
            "3.5.0": "Spring Boot >=2.6.0-M1 and <2.7.0-M1"
        }
    }
}
```

3. 本次使用的版本

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676863746252-47c26fbd-dd9a-4c4f-8eb5-afb417825179.png#averageHue=%23f9f9f9&clientId=u427792cf-17a4-4&from=paste&height=303&id=u3e2320a3&name=image.png&originHeight=303&originWidth=414&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20587&status=done&style=stroke&taskId=u05c92511-40ee-4125-8f89-8a6a3464fee&title=&width=414)

4. 同时用 boot 和 cloud，需要照顾 cloud，由 cloud 决定 boot 版本
5. 2.X 版本常用的组件 pom

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676863807929-5a8120ed-f2d3-4b56-9bbb-7a9ff2f922c3.png#averageHue=%23f9f2f0&clientId=u427792cf-17a4-4&from=paste&height=554&id=u0abbbd9b&name=image.png&originHeight=554&originWidth=667&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52466&status=done&style=stroke&taskId=ue0710a97-7392-4e79-9450-aaca28a0a37&title=&width=667)
## 5、关于 Cloud 各种组件的停更/升级/替换

- 停更不停用
1. 以前

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676868382632-19f2115f-d3a6-4862-8dc0-819b52b10eea.png#averageHue=%23032740&clientId=u427792cf-17a4-4&from=paste&height=508&id=u9ee048ab&name=image.png&originHeight=508&originWidth=1052&originalType=binary&ratio=1&rotation=0&showTitle=false&size=210707&status=done&style=stroke&taskId=ufb319093-3beb-4249-aaff-f472d7db46e&title=&width=1052)

2. 2020年

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676868390430-ab1bfae0-604f-456b-aeb9-beea7e713ee7.png#averageHue=%23fefdfd&clientId=u427792cf-17a4-4&from=paste&height=421&id=uf0c3203e&name=image.png&originHeight=432&originWidth=1313&originalType=binary&ratio=1&rotation=0&showTitle=false&size=58723&status=done&style=stroke&taskId=ud439b08d-aa52-4e19-83a1-35c9d3c0628&title=&width=1279)
# 二、微服务架构编码构建
> 约定 > 配置 > 编码

## 1、创建父项目

1. 创建父项目 SpringCloud

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676869622506-2218664c-a0ac-4690-9771-7a344013b57f.png#averageHue=%233d4144&clientId=u427792cf-17a4-4&from=paste&height=634&id=uc1aca9fa&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48650&status=done&style=stroke&taskId=u560d7bba-09c1-483e-be1c-03371b373a5&title=&width=784)

2. 字符编码

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676869874510-1f2769bf-3538-41e0-8d48-fbc2823397cb.png#averageHue=%233d4146&clientId=u427792cf-17a4-4&from=paste&height=712&id=udb6bca5b&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66810&status=done&style=stroke&taskId=u0033c38b-775d-415e-813c-0162f86c6d4&title=&width=982)

3. 注解生效激活

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676869841052-3ce44f3d-6cae-4f75-b45c-a261a1fd0d85.png#averageHue=%233e4247&clientId=u427792cf-17a4-4&from=paste&height=712&id=ue3373814&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77736&status=done&style=stroke&taskId=u11ff7723-8a3d-4fb9-ac00-67aa4e303a4&title=&width=982)

4. 修改 jdk 版本为 8

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676870060791-a9547667-5cdb-4361-9041-659af4354c33.png#averageHue=%233d4246&clientId=u427792cf-17a4-4&from=paste&height=712&id=u8b72f7c7&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=70292&status=done&style=stroke&taskId=ubf518b90-7c61-4bb7-91ca-402bc6f1a2e&title=&width=982)

5. 删除 src 目录

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676871168384-e5ea5d47-c6c1-4b57-b959-6523f3c1e0de.png#averageHue=%23414d5f&clientId=u427792cf-17a4-4&from=paste&height=82&id=ud6661b56&name=image.png&originHeight=82&originWidth=385&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6933&status=done&style=stroke&taskId=ua628749f-da45-40aa-949e-8c4f93c1484&title=&width=385)

6. 修改 pom 文件
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

7. 执行 mvn:install 将父工程发布到仓库方便子工程继承

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676872286262-7ca2668d-8bb8-4184-9c0b-6e0d30e6f793.png#averageHue=%233b4043&clientId=u427792cf-17a4-4&from=paste&height=349&id=u490ad678&name=image.png&originHeight=349&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14814&status=done&style=stroke&taskId=u5eb2cc3d-66df-492f-a517-cda22223419&title=&width=349)
## 2、创建微服务提供者支付模块 cloud-provider-payment8001

1. 创建子模块 cloud-provider-payment8001

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676873088883-33ae374c-d4b3-4c1f-b380-e4137318ac8b.png#averageHue=%233d4145&clientId=u427792cf-17a4-4&from=paste&height=634&id=u4e0b46ce&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50490&status=done&style=stroke&taskId=ufc831f0c-47e5-459e-a420-a0e2301b009&title=&width=784)![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676873172918-1d89ea07-6267-4fd4-adc5-81a44f8fcf34.png#averageHue=%233e454d&clientId=u427792cf-17a4-4&from=paste&height=247&id=u7c24e7a2&name=image.png&originHeight=247&originWidth=370&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12440&status=done&style=stroke&taskId=u974f4086-6d8a-494f-b357-ee8c7b96b5a&title=&width=370)

   1. 子项目 pom 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8001</artifactId>
    
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

</project>
```

   2. 父项目 pom 文件
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
            <!-- druid 数据连接池 -->
            <dependency>
                <groupId>com.alibaba</groupId>
                <artifactId>druid</artifactId>
                <version>${druid.version}</version>
            </dependency>
            <!-- mybatis-plus -->
            <dependency>
                <groupId>com.baomidou</groupId>
                <artifactId>mybatis-plus-boot-starter</artifactId>
                <version>${mybatis-plus.spring.boot.version}</version>
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

2. 修改子项目 POM 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8001</artifactId>
    
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
        <!--mysql-connector-java-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
        </dependency>
        <!-- druid 数据连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
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

</project>
```

3. 写 YML
```yaml
# 服务端口号
server:
    port: 8001

# spring 配置
spring:
    application:
        # 服务名称
        name: cloud-payment-service
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
        username: root
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

4. 创建数据库、数据表（payment）、插入数据；这里 id 的类型要设置为 `bigint(20)`

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676878893259-e1f14753-bfca-41ac-9016-eb5e25d32755.png#averageHue=%2383a085&clientId=u427792cf-17a4-4&from=paste&height=354&id=ub16e2714&name=image.png&originHeight=354&originWidth=642&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28924&status=done&style=stroke&taskId=u7be1b3bb-e64a-4c4f-9c33-c055dd457f1&title=&width=642)

5. 创建实体类
```java
package com.yuehai.entities;

import lombok.*;

/**
 * @author 月海
 * @create 2023/2/20 15:31
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
public class Payment {
    private Long id;
    private String serial;
}

```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676878737131-f8034057-a62d-482d-bd44-b0569240d765.png#averageHue=%2322741d&clientId=u427792cf-17a4-4&from=paste&height=565&id=u9659e33f&name=image.png&originHeight=565&originWidth=1018&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77626&status=done&style=stroke&taskId=u242ad716-986f-4a9e-9b3d-87e1ccb4ddf&title=&width=1018)

6. 创建 mapper 接口
```java
package com.yuehai.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.yuehai.entities.Payment;

/**
 * @author 月海
 * @create 2023/2/20 15:37
 */
public interface PaymentMapper extends BaseMapper<Payment> {
}

```

7. 在启动类中设置 mapper 接口所在的包
```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
/**
 * @MapperScan：扫描指定包下面的 mapper 接口
 */
@MapperScan("com.yuehai.mapper")
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}

```

8. 创建 service 接口与 serviceImpl 实现类

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676879803740-b1f8b7c0-1434-416e-b1b7-0cd98de64625.png#averageHue=%233d4348&clientId=u427792cf-17a4-4&from=paste&height=573&id=u8874c575&name=image.png&originHeight=573&originWidth=481&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27787&status=done&style=stroke&taskId=u3f95d15b-4c07-44ea-8f67-d9308a27641&title=&width=481)
```java
package com.yuehai.service;

import com.yuehai.entities.Payment;

import java.util.List;

/**
 * @author 月海
 * @create 2023/2/20 15:51
 */
public interface PaymentService {
    List<Payment> getPayment();
}

```
```java
package com.yuehai.service.impl;

import com.yuehai.entities.Payment;
import com.yuehai.mapper.PaymentMapper;
import com.yuehai.service.PaymentService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
 * @author 月海
 * @create 2023/2/20 15:52
 */

@Service
public class PaymentServiceImpl implements PaymentService {

    @Resource
    private PaymentMapper paymentMapper;

    @Override
    public List<Payment> getPayment() {
        return paymentMapper.selectList(null);
    }
}

```

9. 业务类
```java
package com.yuehai.controller;

import com.yuehai.entities.Payment;
import com.yuehai.mapper.PaymentMapper;
import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.List;

/**
 * @author 月海
 * @create 2023/2/20 14:35
 */

@RestController
public class _01_TestController {

    @Resource
    private PaymentService paymentService;

    @GetMapping("/getTest")
    public JsonResult getTest(){
        return JsonResult.success(paymentService.getPayment());
    }

}

```

10. 测试：[http://localhost:8001/getTest](http://localhost:8001/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676878935699-73d06c2c-a4ab-4d71-ab13-6012dbdc1194.png#averageHue=%2374aaed&clientId=u427792cf-17a4-4&from=paste&height=355&id=u2249e066&name=image.png&originHeight=355&originWidth=341&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19625&status=done&style=stroke&taskId=u1a77b133-0347-484e-83c6-858473491db&title=&width=341)
## 3、使用 spring-boot-devtools 进行热部署

1. 开启自动构建项目

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676881198218-8cb87822-cd42-4561-81d1-ab2a809eb50e.png#averageHue=%233e4246&clientId=u427792cf-17a4-4&from=paste&height=712&id=u780b005e&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=91566&status=done&style=stroke&taskId=ub33b5bdd-84e4-44b9-a153-619d79b568f&title=&width=982)

2. 间隔 1 秒保存文件

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676881240085-d0e0f869-5e38-4cb3-ba73-2b84115556fe.png#averageHue=%233d4145&clientId=u427792cf-17a4-4&from=paste&height=712&id=u49cddfc5&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63858&status=done&style=stroke&taskId=u96f026d8-4a01-4a77-8725-5548bad12e8&title=&width=982)

3. 添加依赖
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
```

4. 完成
## 4、创建公共通用模块 cloud-api-commons
> 问题：接下来会创建新模块，也会用到 entities、pom.xml 等，导致重复
> 这个模块解决的就是这种重复的问题

### ①、创建公共通用模块 cloud-api-commons

1. 创建模块

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676882708232-ed4f3349-88a8-4d2d-9c10-f535fbd034c6.png#averageHue=%233d4145&clientId=u427792cf-17a4-4&from=paste&height=634&id=u7d7f81be&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49596&status=done&style=stroke&taskId=u5eb15f2c-79a3-4d51-8b3a-cc7cfa94978&title=&width=784)

2. 修改 pom.xml 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-api-commons</artifactId>
    
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
    
        <!-- hutool 工具包 -->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
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
    </dependencies>

</project>
```

3. 将 entities 和 utils 包与其中的内容复制到此项目中

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676938911740-92183f39-b86e-4e70-a9ed-5c2200bcbb5c.png#averageHue=%233e4245&clientId=u4f9c3c22-6d80-4&from=paste&height=279&id=u634c7027&name=image.png&originHeight=279&originWidth=264&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9391&status=done&style=stroke&taskId=uc6eee213-b27e-432a-b7b8-55c212fbf6d&title=&width=264)
### ②、修改微服务提供者支付模块 cloud-provider-payment8001

1. 修改 pom.xml 文件，删除通用模块中有的依赖，并将通用包作为依赖引入其中
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8001</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        
        <!--jdbc-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <!--mysql-connector-java-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
        </dependency>
        <!-- druid 数据连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
</project>
```

2. 删除 entities 和 utils 包与其中的内容

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676939089817-350febc2-78e4-4982-b58a-646c89e69ce8.png#averageHue=%233b4144&clientId=u4f9c3c22-6d80-4&from=paste&height=419&id=u495a8fb7&name=image.png&originHeight=419&originWidth=319&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15958&status=done&style=stroke&taskId=u9a29b889-9e28-490c-b02c-64b491cefa3&title=&width=319)

3. 启动 8001 模块，测试

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676939133608-aad50f94-da1b-49a8-ad44-7af6e39f9030.png#averageHue=%2375aaec&clientId=u4f9c3c22-6d80-4&from=paste&height=331&id=uac93badb&name=image.png&originHeight=331&originWidth=339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19525&status=done&style=stroke&taskId=uf2086d12-1765-4bb7-8750-04c34fced84&title=&width=339)
## 5、创建微服务消费者订单模块 cloud-consumer-order80
> **RestTemplate：**
> 1. 官网地址：[https://docs.spring.io/spring-framework/docs/5.2.2.RELEASE/javadoc-api/org/springframework/web/client/RestTemplate.html](https://docs.spring.io/spring-framework/docs/5.2.2.RELEASE/javadoc-api/org/springframework/web/client/RestTemplate.html)
> 2. 使用 restTemplate 访问 restful get 接口：`url, responseType, uriVariables` 这三个参数分别代表：请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
> 
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676944698646-19d0de17-8ce5-4b3a-a3d0-156741948dc3.png#averageHue=%23525658&clientId=u4f9c3c22-6d80-4&from=paste&height=70&id=u4d4351e3&name=image.png&originHeight=70&originWidth=450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8083&status=done&style=stroke&taskId=u2b992e8a-c068-4eef-9258-ea37b1b46ac&title=&width=450)
> 3. 使用 restTemplate 访问 restful post 接口：`url , request, responseType, uriVariables` 这四个参数分别代表：请求地址、请求参数（放到请求体中）、HTTP 响应转换被转换成的对象类型、url占位参数
> 
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676944720426-f38c4646-15a4-46b6-8135-ba72be1a115a.png#averageHue=%23535659&clientId=u4f9c3c22-6d80-4&from=paste&height=69&id=u09f4e44c&name=image.png&originHeight=69&originWidth=599&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10227&status=done&style=stroke&taskId=u2d096541-8bcf-4ef1-ab69-97fb3124ade&title=&width=599)
> 4. 此处 HTTP 响应转换被转换成的对象类型是 `HashMap.class` 的原因是 `JsonResult` 类继承了 `HashMap<String, Object>`

1. 创建模块

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676882080972-d9c36ed0-bb46-49d4-87bc-f093c48dfce1.png#averageHue=%233d4144&clientId=u427792cf-17a4-4&from=paste&height=634&id=uea930b45&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51954&status=done&style=stroke&taskId=u82416bf1-7633-41cb-81e6-1345a5ed227&title=&width=784)

2. 修改 pom 文件，并将通用包作为依赖引入其中
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
    
    <artifactId>cloud-consumer-order80</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>

</project>
```

3. 修改 yml 文件
```yaml
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumer-order80
        name: cloud-consumer-order
```

4. 修改主启动类
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * 微服务消费者订单模块 cloud-consumer-order80
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
public class ConsumerOrder80 {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerOrder80.class, args);
    }

}
```

5. 创建 config 配置类
```java
package com.yuehai.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * @author 月海
 * @create 2023/2/21 8:48
 */

@Configuration
public class ApplicationContextConfig {

    @Bean
    public RestTemplate restTemplate(){
        return new RestTemplate();
    }

}
```

6. 创建 controller ，通过该类从 80 调用 8001
```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.HashMap;

/**
 * @author 月海
 * @create 2023/2/21 8:40
 */

@RestController
public class OrderController {

    public static final String PaymentSrv_URL = "http://localhost:8001";

    @Resource
    private RestTemplate restTemplate;

    /**
     * 客户端用浏览器是 get 请求，底层实质也是发送 get 调用服务端 8001
     */
    @GetMapping("/getOrder/payment/get")
    public JsonResult getOrder(){
        /**
         * 使用 restTemplate 访问 restful get 接口：
         *      url, responseType, uriVariables) 这三个参数分别代表：
		 *		请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
         */
        return JsonResult.success(restTemplate.getForObject(PaymentSrv_URL + "/test/getTest", HashMap.class));
    }

}
```

7. 在 8001 模块中创建新 post 方法
```java
/**
 * 测试 post，新增
 */
@PostMapping("/postTest")
public JsonResult postTest(@RequestBody String serial){
    return JsonResult.success(paymentService.addPayment(serial));
}
```
```java
// 新增
int addPayment(String serial);
```
```java
// 新增
@Override
public int addPayment(String serial) {
    return paymentMapper.insert(new Payment(null, serial));
}
```

8. 从 80 调用 8001 的 post 接口
```java
/**
 * 客户端用浏览器是 get 请求，但是底层实质发送 post 调用服务端8001
 */
@GetMapping("/postOrder/payment/post")
public JsonResult postOrder(String serial){
    /**
     * 使用 restTemplate 访问 restful post 接口：
     *      url , request, responseType, uriVariables) 这四个参数分别代表：
     *      请求地址、请求参数（放到请求体中）、HTTP 响应转换被转换成的对象类型、url占位参数
     */
    return JsonResult.success(restTemplate.postForEntity(PaymentSrv_URL + "/test/postTest", serial, HashMap.class));
}
```

9. 测试 getOrder：[http://localhost/getOrder/payment/get](http://localhost/getOrder/payment/get)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676945537411-b14e059d-2af8-49cb-b0b6-302fe943f362.png#averageHue=%23f7f8fe&clientId=u4f9c3c22-6d80-4&from=paste&height=414&id=uf1f49a18&name=image.png&originHeight=414&originWidth=407&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25259&status=done&style=stroke&taskId=u55684b78-a4bb-443e-8be7-613d645772b&title=&width=407)

10. 测试 postOrder：[http://localhost/postOrder/payment/post?serial=2](http://localhost/postOrder/payment/post?serial=2)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676945559572-6e383a78-61e9-43e8-99a9-b3c9fc5e2cd8.png#averageHue=%23f7f8fe&clientId=u4f9c3c22-6d80-4&from=paste&height=602&id=ueac63f9c&name=image.png&originHeight=602&originWidth=476&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51314&status=done&style=stroke&taskId=ubee8a3d6-614b-46dd-8823-70d999c0f26&title=&width=476)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676945571289-8d4e25a9-6c7c-4322-9084-46bfca14ea7a.png#averageHue=%23897557&clientId=u4f9c3c22-6d80-4&from=paste&height=217&id=u48ecfc2a&name=image.png&originHeight=217&originWidth=479&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12896&status=done&style=stroke&taskId=uc6c88380-f78c-475b-8cf4-c1e9ed3279e&title=&width=479)
## 6、目前工程样图
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676957017591-84045f5f-4dc8-458e-8b7f-d6ce79022c8d.png#averageHue=%23404954&clientId=u4f9c3c22-6d80-4&from=paste&height=167&id=u393ef22c&name=image.png&originHeight=167&originWidth=352&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10681&status=done&style=stroke&taskId=ub4979364-672a-4ffc-ae4f-c16c6aac95a&title=&width=352)
# 三、服务注册与发现 Eureka、Zookeeper、Consul
## 1、Eureka
### ①、Eureka 基础知识
#### Ⅰ、什么是服务治理

1. Spring Cloud 封装了 Netflix 公司开发的 Eureka 模块来实现服务治理
2. 在传统的 rpc 远程调用框架中，管理每个服务与服务之间依赖关系比较复杂，管理比较复杂，所以需要使用服务治理，管理服务于服务之间依赖关系，可以实现服务调用、负载均衡、容错等，实现服务发现与注册。
#### Ⅱ、什么是服务注册与发现

1. Eureka 采用了 CS 的设计架构，Eureka Server 作为服务注册功能的服务器，它是服务注册中心。而系统中的其他微服务，使用 Eureka的客户端连接到 Eureka Server 并维持心跳连接。这样系统的维护人员就可以通过 Eureka Server 来监控系统中各个微服务是否正常运行。
2. 在服务注册与发现中，有一个注册中心。
   1. 当服务器启动的时候，会把当前自己服务器的信息比如服务地址通讯地址等以别名方式注册到注册中心上。
   2. 另一方（消费者|服务提供者），以该别名的方式去注册中心上获取到实际的服务通讯地址，然后再实现本地 RPC 调用 RPC 远程调用框架核心设计思想：在于注册中心，因为使用注册中心管理每个服务与服务之间的一个依赖关系(服务治理概念)。
   3. 在任何 rpc 远程框架中，都会有一个注册中心(存放服务地址相关信息(接口地址))
3. 下左图是 Eureka 系统架构，右图是 Dubbo 的架构，请对比

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676955709782-0c39bc6c-a31b-47c1-b38c-00a3629d594c.png#averageHue=%23fbfaf5&clientId=u4f9c3c22-6d80-4&from=paste&height=380&id=u5ebdb02d&name=image.png&originHeight=380&originWidth=1236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73223&status=done&style=stroke&taskId=u421b424c-d18a-4353-9734-f04f51bfdc0&title=&width=1236)
#### Ⅲ、Eureka 两组件

1. Eureka Server 提供服务注册服务：各个微服务节点通过配置启动后，会在 EurekaServer 中进行注册，这样 EurekaServer 中的服务注册表中将会存储所有可用服务节点的信息，服务节点的信息可以在界面中直观看到。
2. EurekaClient 通过注册中心进行访问：是一个 Java 客户端，用于简化 Eureka Server 的交互，客户端同时也具备一个内置的、使用轮询(round-robin)负载算法的负载均衡器。在应用启动后，将会向 Eureka Server 发送心跳(默认周期为30秒)。如果 Eureka Server 在多个心跳周期内没有接收到某个节点的心跳，EurekaServer 将会从服务注册表中把这个服务节点移除（默认90秒）
### ②、单机 Eureka 构建步骤
#### Ⅰ、创建服务注册中心 cloud-eureka-server7001

1. 建 Module

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676957101033-b9205475-9da1-4a96-9757-2c21cc06881d.png#averageHue=%233d4145&clientId=u4f9c3c22-6d80-4&from=paste&height=634&id=ue5afe67c&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50293&status=done&style=stroke&taskId=u8a1077fb-1461-401f-a2d5-c2f30968510&title=&width=784)![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676957185129-56fa0919-fa9d-4807-84f1-75879945cf56.png#averageHue=%233e444a&clientId=u4f9c3c22-6d80-4&from=paste&height=369&id=u8b0f7457&name=image.png&originHeight=369&originWidth=380&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17965&status=done&style=stroke&taskId=u2e44d2e8-1d7b-44ca-bd55-fd3b0d5423c&title=&width=380)

2. 改 POM
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-eureka-server7001</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- eureka-server 服务发现 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 写 YML
```yaml
# 服务端口号
server:
    port: 7001
eureka:
    instance:
        # eureka 服务端的实例名称
        hostname: localhost
    client:
        # false 表示不向注册中心注册自己。
        register-with-eureka: false
        # false 表示自己端就是注册中心，我的职责就是维护服务实例，并不需要去检索服务
        fetch-registry: false
        service-url:
            # 设置与 Eureka Server 交互的地址查询服务和注册服务都需要依赖这个地址。
            defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/

```

4. 主启动类，添加 `@EnableEurekaServer` 注解
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

/**
 * 服务注册中心 cloud-eureka-server7001
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
// 将项目作为 SpringCloud 中的注册中心
@EnableEurekaServer
public class EurekaServer7001 {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServer7001.class, args);
    }

}
```

5. 启动所有模块

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676958068323-408fb508-1d49-4f65-8c44-f20ebb164ec0.png#averageHue=%23404a58&clientId=u4f9c3c22-6d80-4&from=paste&height=119&id=ub00a9763&name=image.png&originHeight=119&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6629&status=done&style=stroke&taskId=ubcb88f20-375b-4e78-a015-31274eee4f4&title=&width=293)

6. 访问 7001 端口（此时还没有实例显示）

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676958093077-a5ec77aa-c140-49a1-a340-17eb8ef7dc9b.png#averageHue=%23d5d4d3&clientId=u4f9c3c22-6d80-4&from=paste&height=984&id=ua9b92545&name=image.png&originHeight=984&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=86099&status=done&style=stroke&taskId=ud18326a4-b394-4e16-99a0-94a454eef33&title=&width=1013)
#### Ⅱ、将 cloud-provider-payment8001 注册进 EurekaServer 成为服务提供者

1. 修改模块 cloud-provider-payment8001 的 pom，引入：`spring-cloud-starter-netflix-eureka-client`
```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8001</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- eureka-client 服务注册 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        
        <!--jdbc-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <!--mysql-connector-java-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
        </dependency>
        <!-- druid 数据连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
</project>
```

2. 修改 yml 文件
```java
# 服务端口号
server:
    port: 8001

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            defaultZone: http://localhost:7001/eureka

```

3. 修改主启动类，添加注解： `@EnableEurekaClient`
```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

/**
 * 微服务提供者支付模块 cloud-provider-payment8001
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
// 扫描指定包下面的 mapper 接口
@MapperScan("com.yuehai.mapper")
// 作为微服务的服务提供者
@EnableEurekaClient
public class ProviderPayment8001 {

    public static void main(String[] args) {
        SpringApplication.run(ProviderPayment8001.class, args);
    }

}

```

4. 重启 8001 与 7001 模块，测试，已发现 8001 实例

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676959446990-a9d581e1-59dc-4065-8401-9f0c1ac701ec.png#averageHue=%23d2d1d0&clientId=u4f9c3c22-6d80-4&from=paste&height=916&id=ub0f1d719&name=image.png&originHeight=916&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84470&status=done&style=stroke&taskId=ub22248a4-c487-4c20-a9c8-e556c3b6f76&title=&width=1013)

5. 微服务注册名配置说明

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676959510899-75f8f001-bb15-4372-9961-1b9a079fbcad.png#averageHue=%238f8d8c&clientId=u4f9c3c22-6d80-4&from=paste&height=916&id=u9b25a66b&name=image.png&originHeight=916&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=188713&status=done&style=stroke&taskId=u008b1312-0594-4970-a5ae-c961b481318&title=&width=1013)

6. 自我保护机制

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676959843364-3411e8a3-a771-44f2-b6b9-ba8561b04f56.png#averageHue=%23e2dddc&clientId=u4f9c3c22-6d80-4&from=paste&height=513&id=u57ba781d&name=image.png&originHeight=513&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81851&status=done&style=stroke&taskId=u9110a989-77e1-44a3-aff2-866247ad0cd&title=&width=982)
#### Ⅲ、将 cloud-consumer-order80 注册进 EurekaServer 成为服务消费
> 与上面相同

1. 修改模块 cloud-consumer-order80 的 pom，引入：`spring-cloud-starter-netflix-eureka-client`
```java
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
    
    <artifactId>cloud-consumer-order80</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- eureka-client 服务注册 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
    
</project>
```

2. 修改 yml 文件
```java
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumer-order80
        name: cloud-consumer-order
        
eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            defaultZone: http://localhost:7001/eureka
```

3. 修改主启动类，添加注解： `@EnableEurekaClient`
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

/**
 * 微服务消费者订单模块 cloud-consumer-order80
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
// 作为微服务的服务提供者
@EnableEurekaClient
public class ConsumerOrder80 {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerOrder80.class, args);
    }

}
```

4. 重启 80 与 7001 模块，测试，已发现 80 实例

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676959968556-84ca06e2-5bfc-4b6c-bdd5-6243f25f3d53.png#averageHue=%23d1d0cf&clientId=u4f9c3c22-6d80-4&from=paste&height=916&id=uda91c9c3&name=image.png&originHeight=916&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=91325&status=done&style=stroke&taskId=u770ddd5d-cfd4-4376-a091-8e36e6c5f3b&title=&width=1013)
### ③、集群 Eureka 构建步骤
#### Ⅰ、Eureka 集群原理说明

- 问题：微服务RPC远程服务调用最核心的是什么
1. 高可用
2. 试想你的注册中心只有一个 only one， 它出故障了那就呵呵(￣▽￣)"了，会导致整个为服务环境不可用，所以：
3. 解决办法：搭建 Eureka 注册中心集群 ，实现负载均衡+故障容错

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676960420716-87282ad9-7ab0-4e64-a0a9-5fbb63919f1f.png#averageHue=%23fefdf8&clientId=u4f9c3c22-6d80-4&from=paste&height=327&id=u14f3140e&name=image.png&originHeight=351&originWidth=1141&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52056&status=done&style=stroke&taskId=u04d8d56b-1f00-473f-a966-62c326a93ba&title=&width=1062)
#### Ⅱ、EurekaServer 集群环境构建步骤

1. 修改映射配置：找到 `C:\Windows\System32\drivers\etc` 路径下的 hosts 文件，修改映射配置添加进 hosts 文件；因为要将一台机器当作两台机器用

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676961541144-6185b363-87f3-4f57-a5b4-6046602cf16e.png#averageHue=%23f7f6f5&clientId=u4f9c3c22-6d80-4&from=paste&height=229&id=u98035b6c&name=image.png&originHeight=229&originWidth=397&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15581&status=done&style=stroke&taskId=u8670fd62-799c-46b4-8b08-9b2733ad981&title=&width=397)![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676961805075-edff5cae-3dae-4c7a-99d7-5ba841a96ff6.png#averageHue=%23f7f6f5&clientId=u4f9c3c22-6d80-4&from=paste&height=625&id=u2939e9bd&name=image.png&originHeight=625&originWidth=905&originalType=binary&ratio=1&rotation=0&showTitle=false&size=83078&status=done&style=stroke&taskId=uee6cd714-040b-4e6c-b2b8-81bdfd76ed5&title=&width=905)
```java
127.0.0.1		eureka7001.com
127.0.0.1		eureka7002.com 
```

2. 参考 cloud-eureka-server7001 新建 cloud-eureka-server7002

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676961904736-f3762b37-f1c8-444d-9629-a6371f16c99f.png#averageHue=%233e4345&clientId=u4f9c3c22-6d80-4&from=paste&height=219&id=u1ae16106&name=image.png&originHeight=219&originWidth=218&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7596&status=done&style=stroke&taskId=u20acc902-2661-45b7-8897-96cbda9e43b&title=&width=218)

3. 修改 7002 的 pom 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-eureka-server7002</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- eureka-server 服务发现 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
        </dependency>
    </dependencies>

</project>
```

4. 修改 7001 与 7002 的 yml 文件
```yaml
# 服务端口号
server:
    port: 7001

eureka:
    instance:
        # eureka 服务端的实例名称
        hostname: eureka7001.com
    client:
        # false 表示不向注册中心注册自己。
        register-with-eureka: false
        # false 表示自己端就是注册中心，我的职责就是维护服务实例，并不需要去检索服务
        fetch-registry: false
        # 指定 eureka 服务端的注册地址
        service-url:
            # eureka 服务相互注册，在其中注册除自己以外的其他 eureka 服务
            defaultZone: http://eureka7002.com:7002/eureka/

```
```yaml
# 服务端口号
server:
    port: 7002

eureka:
    instance:
        # eureka 服务端的实例名称
        hostname: eureka7002.com
    client:
        # false 表示不向注册中心注册自己。
        register-with-eureka: false
        # false 表示自己端就是注册中心，我的职责就是维护服务实例，并不需要去检索服务
        fetch-registry: false
        # 指定 eureka 服务端的注册地址
        service-url:
            # eureka 服务相互注册，在其中注册除自己以外的其他 eureka 服务
            defaultZone: http://eureka7001.com:7001/eureka/

```

5. 修改 7002 的主启动类
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

/**
 * 服务注册中心 cloud-eureka-server7001
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
// 将项目作为 SpringCloud 中的注册中心
@EnableEurekaServer
public class EurekaServer7002 {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServer7002.class, args);
    }

}
```
#### Ⅲ、将支付服务 8001 微服务发布到上面 2 台 Eureka 集群配置中

- 修改 `defaultZone` 属性，添加新增的 Eureka
```yaml
# 服务端口号
server:
    port: 8001

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka

```
#### Ⅳ、将订单服务 80 微服务发布到上面 2 台 Eureka 集群配置中

- 修改 `defaultZone` 属性，添加新增的 Eureka
```yaml
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumer-order80
        name: cloud-consumer-order

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
```
#### Ⅴ、测试 Eureka 集群 1

1. 先启动 EurekaServer，7001/7002 服务
2. 再启动服务提供者 provider，8001 服务
3. 最后启动消费者，80 服务
4.  EurekaServer，7001：[http://eureka7001.com:7001/](http://eureka7001.com:7001/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676963590456-ab65b8df-a55b-415f-9a15-143eb6b00fef.png#averageHue=%23d4d3d2&clientId=u4f9c3c22-6d80-4&from=paste&height=984&id=u88637eab&name=image.png&originHeight=984&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106545&status=done&style=stroke&taskId=uac193e65-fdcf-4aa3-a6c5-de30365f3a5&title=&width=1013)

5.  EurekaServer，7002：[http://eureka7002.com:7002/](http://eureka7002.com:7002/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676963611618-c8caf0ba-a402-434b-b4e2-175cdaa95c01.png#averageHue=%23d4d3d2&clientId=u4f9c3c22-6d80-4&from=paste&height=986&id=ue3210263&name=image.png&originHeight=986&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106017&status=done&style=stroke&taskId=u8ac52d48-3338-4124-a8e5-91fe9f7d6cd&title=&width=1013)
#### Ⅵ、支付服务提供者集群环境构建 cloud-provider-payment8002

1. 参考 cloud-provider-payment8001 新建 cloud-provider-payment8002

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676964215392-fd708896-9806-40fd-b355-8a9695158062.png#averageHue=%233d4144&clientId=u4f9c3c22-6d80-4&from=paste&height=634&id=u5abe9c10&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50578&status=done&style=stroke&taskId=ufd27c5cb-786c-46aa-8b7f-00b4e8a30fe&title=&width=784)

2. 改 POM
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8002</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        
        <!-- eureka-client 服务注册 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        
        <!--jdbc-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <!--mysql-connector-java-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
        </dependency>
        <!-- druid 数据连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
        </dependency>
    </dependencies>

</project>
```

3. 写 YML
```yaml
# 服务端口号
server:
    port: 8002

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka

```

4. 主启动
```java
package com.yuehai;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

/**
 * 微服务提供者支付模块 cloud-provider-payment8001
 * @author 月海
 * @create ${DATE} ${TIME}
 */

@SpringBootApplication
// 扫描指定包下面的 mapper 接口
@MapperScan("com.yuehai.mapper")
// 作为微服务的服务提供者
@EnableEurekaClient
public class ProviderPayment8002 {

    public static void main(String[] args) {
        SpringApplication.run(ProviderPayment8002.class, args);
    }

}

```

5. 业务类
- 从 8001 复制的一样的
6. 修改 8001 与 8002 的 Controller
```java
package com.yuehai.controller;

import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/2/20 14:35
 */

@RestController
@RequestMapping("/test")
public class PaymentController {

    @Value("${server.port}")
    private String serverPort;

    @Resource
    private PaymentService paymentService;

    /**
     * 测试 get，查询全部
     */
    @GetMapping("/getTest")
    public JsonResult getTest(){
        return JsonResult.success(paymentService.getPayment()).put("服务端口为：", serverPort);
    }

    /**
     * 测试 post，新增
     */
    @PostMapping("/postTest")
    public JsonResult postTest(@RequestBody String serial){
        return JsonResult.success(paymentService.addPayment(serial)).put("服务端口为：", serverPort);
    }

}

```
```java
package com.yuehai.controller;

import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

/**
 * @author 月海
 * @create 2023/2/20 14:35
 */

@RestController
@RequestMapping("/test")
public class PaymentController {

    @Value("${server.port}")
    private String serverPort;

    @Resource
    private PaymentService paymentService;

    /**
     * 测试 get，查询全部
     */
    @GetMapping("/getTest")
    public JsonResult getTest(){
        return JsonResult.success(paymentService.getPayment()).put("服务端口为：", serverPort);
    }

    /**
     * 测试 post，新增
     */
    @PostMapping("/postTest")
    public JsonResult postTest(@RequestBody String serial){
        return JsonResult.success(paymentService.addPayment(serial)).put("服务端口为：", serverPort);
    }


}

```

7. 重新启动 5 个微服务

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965494693-5d2b4316-def1-4280-a721-dbea5c94e33f.png#averageHue=%23404751&clientId=u4f9c3c22-6d80-4&from=paste&height=189&id=ubabc4fbe&name=image.png&originHeight=189&originWidth=280&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9591&status=done&style=stroke&taskId=u6c1907aa-22fa-491a-a870-d0b8b53e4b9&title=&width=280)

8. 测试 7001：[http://eureka7001.com:7001/](http://eureka7001.com:7001/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965587152-0997f310-85df-4fae-8279-9beb6b0d3dc0.png#averageHue=%23d5d4d3&clientId=u4f9c3c22-6d80-4&from=paste&height=1037&id=u68af35e1&name=image.png&originHeight=1037&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129193&status=done&style=stroke&taskId=u83cbe36a-2949-4a9d-8bc4-912cd6d5951&title=&width=1920)

9. 测试 7002：[http://eureka7002.com:7002/](http://eureka7002.com:7002/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965611526-f5909e06-2b13-4ead-938b-0912bbd3e32d.png#averageHue=%23d5d4d3&clientId=u4f9c3c22-6d80-4&from=paste&height=1033&id=u667447e2&name=image.png&originHeight=1033&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129113&status=done&style=stroke&taskId=u7c88946c-c3bc-4f4a-a6b7-99e0e7e7c02&title=&width=1920)

10. 测试 8001：[http://localhost:8001/test/getTest](http://localhost:8001/test/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965711644-4bd46f13-8859-451e-bec5-63720d49bb48.png#averageHue=%237bb3e1&clientId=u4f9c3c22-6d80-4&from=paste&height=468&id=u64db9b63&name=image.png&originHeight=468&originWidth=411&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35614&status=done&style=stroke&taskId=ud5526ee3-77ea-46e4-ae53-258963cb847&title=&width=411)

11. 测试 8002：[http://localhost:8002/test/getTest](http://localhost:8002/test/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965742365-392e5118-bb2c-469d-83ab-8ba0e45b5d43.png#averageHue=%237bb2e1&clientId=u4f9c3c22-6d80-4&from=paste&height=477&id=u0530c3e8&name=image.png&originHeight=477&originWidth=412&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36001&status=done&style=stroke&taskId=ua411104c-dd92-4228-ae9b-6ca4be388ab&title=&width=412)

12. 测试 80：[http://localhost/getOrder/payment/get](http://localhost/getOrder/payment/get)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965838927-73e96067-9261-48ec-9fdf-8895a0d4a376.png#averageHue=%236ea0ee&clientId=u4f9c3c22-6d80-4&from=paste&height=555&id=u171d41d8&name=image.png&originHeight=555&originWidth=541&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42474&status=done&style=stroke&taskId=u70f5b58e-3f3a-4b69-a6f9-2628adbd622&title=&width=541)

13. 问题：不论怎么刷新 80 端口，他调用的支付端口都是 8001，因为在 controller 调用时被写死 8001 了
14. 解决：在下面解决
#### Ⅶ、负载均衡

1. 解决上面的问题：修改 80 端口的 controller 类，将端口号更改为服务名
```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.HashMap;

/**
 * @author 月海
 * @create 2023/2/21 8:40
 */

@RestController
public class OrderController {

    /**
     * 调用微服务中名为 CLOUD-PAYMENT-SERVICE 的服务
     */
    public static final String PAYMENT_SRV_URL = "http://CLOUD-PAYMENT-SERVICE";

    @Resource
    private RestTemplate restTemplate;

    /**
     * 客户端用浏览器是 get 请求，底层实质也是发送 get 调用服务端 8001
     */
    @GetMapping("/getOrder/payment/get")
    public JsonResult getOrder(){
        /**
         * 使用 restTemplate 访问 restful get 接口：
         *      url, responseType, uriVariables) 这三个参数分别代表：
         *      请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
         */
        return JsonResult.success(restTemplate.getForObject(PAYMENT_SRV_URL + "/test/getTest", HashMap.class));
    }

    /**
     * 客户端用浏览器是 get 请求，但是底层实质发送 post 调用服务端8001
     */
    @GetMapping("/postOrder/payment/post")
    public JsonResult postOrder(String serial){
        /**
         * 使用 restTemplate 访问 restful post 接口：
         *      url , request, responseType, uriVariables) 这四个参数分别代表：
         *      请求地址、请求参数（放到请求体中）、HTTP 响应转换被转换成的对象类型、url占位参数
         */
        return JsonResult.success(restTemplate.postForEntity(PAYMENT_SRV_URL + "/test/postTest", serial, HashMap.class));
    }

}
```

2. 在 80 端口的 ApplicationContextConfig 类中的 RestTemplate 方法上添加 `@LoadBalanced` 注解，赋予 RestTemplate 负载均衡的能力；提前说一下 Ribbon 的负载均衡功能
```java
package com.yuehai.config;

import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * @author 月海
 * @create 2023/2/21 8:48
 */

@Configuration
public class ApplicationContextConfig {

    @Bean
    /**
     * 使用 @LoadBalanced 注解赋予 RestTemplate 负载均衡的能力
     */
    @LoadBalanced
    public RestTemplate restTemplate(){
        return new RestTemplate();
    }

}

```
#### Ⅷ、测试 Eureka 集群 2

1. 先启动 EurekaServer，7001/7002 服务
2. 再启动服务提供者 provider，8001/8002 服务
3. 最后启动消费者，80 服务

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676966864761-9f9d54c6-59d0-489b-9dcf-fe8da1e7abaf.png#averageHue=%23404954&clientId=u4f9c3c22-6d80-4&from=paste&height=144&id=ua9ac59b5&name=image.png&originHeight=144&originWidth=309&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8578&status=done&style=stroke&taskId=u5f7459b1-c601-4f19-86bd-01138373a28&title=&width=309)

4.  测试 7001：[http://eureka7001.com:7001/](http://eureka7001.com:7001/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965587152-0997f310-85df-4fae-8279-9beb6b0d3dc0.png#averageHue=%23d5d4d3&clientId=u4f9c3c22-6d80-4&from=paste&height=1037&id=CZbdU&name=image.png&originHeight=1037&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129193&status=done&style=stroke&taskId=u83cbe36a-2949-4a9d-8bc4-912cd6d5951&title=&width=1920)

5. 测试 7002：[http://eureka7002.com:7002/](http://eureka7002.com:7002/)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965611526-f5909e06-2b13-4ead-938b-0912bbd3e32d.png#averageHue=%23d5d4d3&clientId=u4f9c3c22-6d80-4&from=paste&height=1033&id=CraDG&name=image.png&originHeight=1033&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129113&status=done&style=stroke&taskId=u7c88946c-c3bc-4f4a-a6b7-99e0e7e7c02&title=&width=1920)

6. 测试 8001：[http://localhost:8001/test/getTest](http://localhost:8001/test/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965711644-4bd46f13-8859-451e-bec5-63720d49bb48.png#averageHue=%237bb3e1&clientId=u4f9c3c22-6d80-4&from=paste&height=468&id=pj34r&name=image.png&originHeight=468&originWidth=411&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35614&status=done&style=stroke&taskId=ud5526ee3-77ea-46e4-ae53-258963cb847&title=&width=411)

7. 测试 8002：[http://localhost:8002/test/getTest](http://localhost:8002/test/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965742365-392e5118-bb2c-469d-83ab-8ba0e45b5d43.png#averageHue=%237bb2e1&clientId=u4f9c3c22-6d80-4&from=paste&height=477&id=JB7Dl&name=image.png&originHeight=477&originWidth=412&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36001&status=done&style=stroke&taskId=ua411104c-dd92-4228-ae9b-6ca4be388ab&title=&width=412)

8. 测试 80：[http://localhost/getOrder/payment/get](http://localhost/getOrder/payment/get)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676965838927-73e96067-9261-48ec-9fdf-8895a0d4a376.png#averageHue=%236ea0ee&clientId=u4f9c3c22-6d80-4&from=paste&height=555&id=gPHxi&name=image.png&originHeight=555&originWidth=541&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42474&status=done&style=stroke&taskId=u70f5b58e-3f3a-4b69-a6f9-2628adbd622&title=&width=541)

9. 测试 80，多刷新几次：[http://localhost/getOrder/payment/get](http://localhost/getOrder/payment/get)，8001/8002 端口交替出现，负载均衡效果达到

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676967004861-52b69166-5da8-4fc2-bcb4-c06f83ed4c5a.png#averageHue=%2377b2e1&clientId=u4f9c3c22-6d80-4&from=paste&height=544&id=u917ca1ae&name=image.png&originHeight=544&originWidth=541&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43408&status=done&style=stroke&taskId=ue7cfce7a-d003-4b0e-8b4a-cde66b49853&title=&width=541)

10. Ribbon 和 Eureka 整合后 Consumer 可以直接调用服务而不用再关心地址和端口号，且该服务还有负载功能了。O(∩_∩)O
### ④、actuator 微服务信息完善
#### Ⅰ、主机名称：服务名称修改

1. 当前问题：状态指示会带着主机名

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676967819966-6a1d7085-b86a-4819-852c-2f018a84b8c6.png#averageHue=%23c6c4c2&clientId=u4f9c3c22-6d80-4&from=paste&height=169&id=u8f3d9845&name=image.png&originHeight=169&originWidth=1424&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36877&status=done&style=stroke&taskId=u4d247242-0cdb-4ae2-8464-0968f9e568f&title=&width=1424)

2. 修改 yml 文件，添加 `instance-id` 属性
```yaml
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumer-order80
        name: cloud-consumer-order

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: order80
```
```yaml
# 服务端口号
server:
    port: 8001

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: payment8001

```
```yaml
# 服务端口号
server:
    port: 8002

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: payment8002

```

3. 修改之后：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676968400558-399acae7-ff7e-49a5-a617-dd97e3bb3806.png#averageHue=%23c9c7c6&clientId=u4f9c3c22-6d80-4&from=paste&height=178&id=ufe96bd77&name=image.png&originHeight=178&originWidth=1454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31631&status=done&style=stroke&taskId=u542bc158-0c83-45d5-becb-856cd15780e&title=&width=1454)
#### Ⅱ、访问信息有 IP 信息提示

1. 当前问题：访问路径不会显示 IP 地址
2. 修改 yml 文件，添加 `instance-id` 属性
```yaml
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumer-order80
        name: cloud-consumer-order

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: order80
        # 访问路径可以显示 IP 地址
        prefer-ip-address: true
```
```yaml
# 服务端口号
server:
    port: 8001

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: payment8001
        # 访问路径可以显示 IP 地址
        prefer-ip-address: true

```
```yaml
# 服务端口号
server:
    port: 8002

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8001
        name: cloud-payment-service
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
        username: root
        # 密码（以 0 开头要加引号）
        password: "000123"

# 配置 MyBatis-Plus 规则
mybatis-plus:
    configuration:
        # 是否开启自动驼峰命名规则映射
        map-underscore-to-camel-case: true
        # 开启 mybatis 的 sql 执行日志打印，可以在控制台打印输出 sql 语句
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

eureka:
    client:
        # 表示是否将自己注册进 EurekaServer 默认为 true。
        register-with-eureka: true
        # 是否从 EurekaServer 抓取已有的注册信息，默认为 true。单节点无所谓，集群必须设置为 true 才能配合 ribbon使 用负载均衡
        fetchRegistry: true
        # 指定 eureka 服务端的注册地址 (Eureka Server 的分区地址)
        service-url:
            # 集群 eureka 间使用 , 分隔
            defaultZone: http://eureka7001.com:7001/eureka, http://eureka7002.com:7002/eureka
    instance:
        # 指定状态名
        instance-id: payment8002
        # 访问路径可以显示 IP 地址
        prefer-ip-address: true

```

3. 修改之后：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1676968779234-d8e26166-d39e-4c3c-ad0b-1b306b8ff5a0.png#averageHue=%23dad9d8&clientId=u4f9c3c22-6d80-4&from=paste&height=916&id=ucb34ff62&name=image.png&originHeight=916&originWidth=1019&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77245&status=done&style=stroke&taskId=u9d3c5fba-f3de-481f-9fef-060346204c1&title=&width=1019)
### ⑤、服务发现 Discovery
> 对于注册进 eureka 里面的微服务，可以通过服务发现来获得该服务的信息

1. 修改 cloud-provider-payment8001 的 Controller，注入 DiscoveryClient，并新增 discovery 方法
```java
package com.yuehai.controller;

import com.yuehai.service.PaymentService;
import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.discovery.DiscoveryClient;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * @author 月海
 * @create 2023/2/20 14:35
 */

@RestController
@RequestMapping("/test")
public class PaymentController {

    @Value("${server.port}")
    private String serverPort;
    /**
     * DiscoveryClient：服务发现
     */
    @Resource
    private DiscoveryClient discoveryClient;

    @Resource
    private PaymentService paymentService;

    /**
     * 测试 get，查询全部
     */
    @GetMapping("/getTest")
    public JsonResult getTest(){
        return JsonResult.success(paymentService.getPayment()).put("服务端口为：", serverPort);
    }

    /**
     * 测试 post，新增
     */
    @PostMapping("/postTest")
    public JsonResult postTest(@RequestBody String serial){
        return JsonResult.success(paymentService.addPayment(serial)).put("服务端口为：", serverPort);
    }

    /**
     * DiscoveryClient：服务发现测试
     */
    @GetMapping(value = "/DCTest")
    public JsonResult discovery(){
        // 获取所有在 Eureka 中注册的服务，返回集合，其中保存的是服务名
        List<String> services = discoveryClient.getServices();

        // 获取指定服务名的微服务详细信息
        List<ServiceInstance> instances = discoveryClient.getInstances("cloud-payment-service");

        return JsonResult.success("OK").put("services：", services).put("instances：", instances);
    }
}

```

2. 返回内容：[http://localhost:8001/test/DCTest](http://localhost:8001/test/DCTest)
```json
{
    "msg": "ok",
    "instances：": [
        {
            "host": "172.20.2.88",
            "port": 8001,
            "metadata": {
                "management.port": "8001"
            },
            "secure": false,
            "uri": "http://172.20.2.88:8001",
            "serviceId": "CLOUD-PAYMENT-SERVICE",
            "instanceId": "payment8001",
            "instanceInfo": {
                "instanceId": "payment8001",
                "app": "CLOUD-PAYMENT-SERVICE",
                "appGroupName": null,
                "ipAddr": "172.20.2.88",
                "sid": "na",
                "homePageUrl": "http://172.20.2.88:8001/",
                "statusPageUrl": "http://172.20.2.88:8001/actuator/info",
                "healthCheckUrl": "http://172.20.2.88:8001/actuator/health",
                "secureHealthCheckUrl": null,
                "vipAddress": "cloud-payment-service",
                "secureVipAddress": "cloud-payment-service",
                "countryId": 1,
                "dataCenterInfo": {
                    "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                    "name": "MyOwn"
                },
                "hostName": "172.20.2.88",
                "status": "UP",
                "overriddenStatus": "UNKNOWN",
                "leaseInfo": {
                    "renewalIntervalInSecs": 30,
                    "durationInSecs": 90,
                    "registrationTimestamp": 1677024411541,
                    "lastRenewalTimestamp": 1677024531484,
                    "evictionTimestamp": 0,
                    "serviceUpTimestamp": 1677024411541
                },
                "isCoordinatingDiscoveryServer": false,
                "metadata": {
                    "management.port": "8001"
                },
                "lastUpdatedTimestamp": 1677024411541,
                "lastDirtyTimestamp": 1677024411451,
                "actionType": "ADDED",
                "asgName": null
            },
            "scheme": null
        },
        {
            "host": "172.20.2.88",
            "port": 8002,
            "metadata": {
                "management.port": "8002"
            },
            "secure": false,
            "uri": "http://172.20.2.88:8002",
            "serviceId": "CLOUD-PAYMENT-SERVICE",
            "instanceId": "payment8002",
            "instanceInfo": {
                "instanceId": "payment8002",
                "app": "CLOUD-PAYMENT-SERVICE",
                "appGroupName": null,
                "ipAddr": "172.20.2.88",
                "sid": "na",
                "homePageUrl": "http://172.20.2.88:8002/",
                "statusPageUrl": "http://172.20.2.88:8002/actuator/info",
                "healthCheckUrl": "http://172.20.2.88:8002/actuator/health",
                "secureHealthCheckUrl": null,
                "vipAddress": "cloud-payment-service",
                "secureVipAddress": "cloud-payment-service",
                "countryId": 1,
                "dataCenterInfo": {
                    "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                    "name": "MyOwn"
                },
                "hostName": "172.20.2.88",
                "status": "UP",
                "overriddenStatus": "UNKNOWN",
                "leaseInfo": {
                    "renewalIntervalInSecs": 30,
                    "durationInSecs": 90,
                    "registrationTimestamp": 1677024399834,
                    "lastRenewalTimestamp": 1677024549693,
                    "evictionTimestamp": 0,
                    "serviceUpTimestamp": 1677024399836
                },
                "isCoordinatingDiscoveryServer": false,
                "metadata": {
                    "management.port": "8002"
                },
                "lastUpdatedTimestamp": 1677024399836,
                "lastDirtyTimestamp": 1677024399545,
                "actionType": "ADDED",
                "asgName": null
            },
            "scheme": null
        }
    ],
    "services：": [
        "cloud-consumer-order",
        "cloud-payment-service"
    ],
    "code": 200,
    "data": "OK"
}
```
### ⑥、Eureka 自我保护
#### Ⅰ、概述

1. 保护模式主要用于一组客户端和 Eureka Server 之间存在网络分区场景下的保护。
2. 一旦进入保护模式，Eureka Server 将会尝试保护其服务注册表中的信息，不再删除服务注册表中的数据，也就是不会注销任何微服务。
3. 如果在 Eureka Server 的首页看到以下这段提示，则说明 Eureka 进入了保护模式：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677025472780-53b62282-e092-48e4-96b2-ad7be09a1094.png#averageHue=%23f3e4e4&clientId=uc8e9057c-b58a-4&from=paste&height=98&id=u0f5cc5bd&name=image.png&originHeight=98&originWidth=1008&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37258&status=done&style=stroke&taskId=ub04335a8-3e11-49ac-9342-c55409d3ce7&title=&width=1008)

4. 为什么会产生 Eureka 自我保护机制：防止了虽然 EurekaClient 在正常运行，但是其与 EurekaServer 网络不通的情况下，EurekaServer 会立刻将 EurekaClient 服务剔除
#### Ⅱ、什么是自我保护模式

1. 默认情况下，如果 EurekaServer 在一定时间内没有接收到某个微服务实例的心跳，EurekaServer 将会注销该实例（默认90秒）。但是当网络分区故障发生(延时、卡顿、拥挤)时，微服务与 EurekaServer 之间无法正常通信，以上行为可能变得非常危险了：因为微服务本身其实是健康的，此时本不应该注销这个微服务
2. Eureka 通过“自我保护模式”来解决这个问题：当 EurekaServer 节点在短时间内丢失过多客户端时（可能发生了网络分区故障），那么这个节点就会进入自我保护模式。
3. 在自我保护模式中，Eureka Server 会保护服务注册表中的信息，不再注销任何服务实例。
4. 它的设计哲学就是宁可保留错误的服务注册信息，也不盲目注销任何可能健康的服务实例。一句话讲解：好死不如赖活着
5. 综上，自我保护模式是一种应对网络异常的安全保护措施。它的架构哲学是宁可同时保留所有微服务（健康的微服务和不健康的微服务都会保留）也不盲目注销任何健康的微服务。使用自我保护模式，可以让 Eureka 集群更加的健壮、稳定。
6. 一句话：某时刻某一个微服务不可用了，Eureka 不会立刻清理，依旧会对该微服务的信息进行保存
7. 属于 CAP 里面的 AP 分支

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677025671962-10942c20-3053-4c8f-a462-edb2257558ed.png#averageHue=%23f4f0eb&clientId=uc8e9057c-b58a-4&from=paste&height=423&id=uf0406bcf&name=image.png&originHeight=423&originWidth=736&originalType=binary&ratio=1&rotation=0&showTitle=false&size=200851&status=done&style=stroke&taskId=uaba1d1b0-f82a-42e7-9d28-37d474f577e&title=&width=736)
#### Ⅲ、怎么禁止自我保护

1. 在服务注册中心的配置文件 application.yml 中新增配置：`eureka.server.enable-self-preservation=true`
```yaml
# 服务端口号
server:
    port: 7001

eureka:
    instance:
        # eureka 服务端的实例名称
        hostname: eureka7001.com
    client:
        # false 表示不向注册中心注册自己。
        register-with-eureka: false
        # false 表示自己端就是注册中心，我的职责就是维护服务实例，并不需要去检索服务
        fetch-registry: false
        # 指定 eureka 服务端的注册地址
        service-url:
            # eureka 服务相互注册，在其中注册除自己以外的其他 eureka 服务
            defaultZone: http://eureka7002.com:7002/eureka/
    server:
        # 关闭自我保护机制，保证不可用服务被及时踢除（默认开启）
        enable-self-preservation: false
```

2. 关闭之后的效果：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677026975557-431ee1fe-a01a-4931-9bfb-0666d92394f4.png#averageHue=%23ddd8d7&clientId=uc8e9057c-b58a-4&from=paste&height=338&id=u8cb8dd93&name=image.png&originHeight=338&originWidth=965&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53983&status=done&style=stroke&taskId=u87f5f80b-23f1-4154-a2b9-338f60ed94e&title=&width=965)

3. 微服务提供者可以修改配置文件，新增以下属性：
   1. `eureka.instance.lease-renewal-interval-in-seconds=30`：Eureka 客户端向服务端发送心跳的时间间隔，单位为秒(默认是30秒)
   2. `eureka.instance.lease-expiration-duration-in-seconds=90`：Eureka 客户端向服务端发送心跳的时间间隔，单位为秒(默认是30秒)
## 2、Zookeeper
> Eureka停止更新了你怎么办：[https://github.com/Netflix/eureka/wiki](https://github.com/Netflix/eureka/wiki)
> SpringCloud 整合 Zookeeper 代替 Eureka

### ①、Zookeeper 简介

1. zookeeper 是一个分布式协调工具，可以实现注册中心功能
2. 关闭 Linux 服务器防火墙后启动 zookeeper 服务器
3. zookeeper 服务器取代 Eureka 服务器，zookeeper 作为服务注册中心
### ②、安装 zookeeper
> 本次使用的是 docker

1. 下载 zookeeper 镜像 3.5.3 版，版本的对应关系在 maven 依赖中查看；当然也可以自己指定 maven 依赖中的 zookeeper 版本

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677031293227-0a9c0c9d-aecf-4e70-85da-a888ade726b1.png#averageHue=%233e4349&clientId=uc8e9057c-b58a-4&from=paste&height=625&id=ub6c305eb&name=image.png&originHeight=625&originWidth=616&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59749&status=done&style=stroke&taskId=ub46a5660-c027-46a0-a297-d0bf52c2522&title=&width=616)
```bash
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
docker-compose_nginx          latest    524bf968c7e3   2 weeks ago     142MB
docker-compose_java-service   latest    4bd1f84ef9cc   2 weeks ago     453MB
nginx                         latest    605c77e624dd   13 months ago   141MB
mysql                         5.7       c20987f18b13   14 months ago   448MB
ubuntu                        latest    ba6acccedd29   16 months ago   72.8MB
redis                         6.2.1     de974760ddb2   22 months ago   105MB
portainer/portainer           1.20.2    19d07168491a   3 years ago     74.1MB

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED       STATUS       PORTS                                                  NAMES
890052e7a032   mysql:5.7                     "docker-entrypoint.s…"   7 days ago    Up 7 days    0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sharp_kare
d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   2 weeks ago   Up 12 days   0.0.0.0:80->80/tcp, :::80->80/tcp                      nginx
7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   2 weeks ago   Up 12 days   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp              java-service
9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             2 weeks ago   Up 2 weeks   0.0.0.0:9443->9000/tcp, :::9443->9000/tcp              naughty_kowalevski

docker@VM-8-15-ubuntu:~$ docker search zookeeper
NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
zookeeper                        Apache ZooKeeper is an open-source server wh…   1323      [OK]       
wurstmeister/zookeeper                                                           178                  [OK]
jplock/zookeeper                 Builds a docker image for Zookeeper version …   165                  [OK]
bitnami/zookeeper                ZooKeeper is a centralized service for distr…   89                   [OK]
mesoscloud/zookeeper             ZooKeeper                                       73                   [OK]
digitalwonderland/zookeeper      Latest Zookeeper - clusterable                  23                   [OK]
debezium/zookeeper               Zookeeper image required when running the De…   17                   [OK]
thefactory/zookeeper-exhibitor   Exhibitor-managed ZooKeeper with S3 backups …   6                    [OK]
ubuntu/zookeeper                 ZooKeeper maintains configuration informatio…   5                    
emccorp/zookeeper                Zookeeper                                       2                    
dabealu/zookeeper-exporter       zookeeper exporter for prometheus               2                    [OK]
rancher/zookeeper                                                                1                    
bitnami/zookeeper-exporter                                                       1                    
objectscale/zookeeper-operator                                                   0                    
kope/zookeeper                                                                   0                    
semoss/zookeeper                                                                 0                    
rancher/zookeeper-config                                                         0                    
objectscale/zookeeper                                                            0                    
rapidfort/zookeeper-official     RapidFort optimized, hardened image for Zook…   0                    
pravega/zookeeper                                                                0                    
ibmcom/zookeeper-ppc64le         Apache ZooKeeper is an open-source server wh…   0                    
rapidfort/zookeeper              RapidFort optimized, hardened image for Zook…   0                    
phenompeople/zookeeper           Apache ZooKeeper is an open-source server wh…   0                    [OK]
rapidfort/zookeeper-ib           RapidFort optimized, hardened image for Zook…   0                    
pravega/zookeeper-operator       Kubernetes operator for Zookeeper               0                    

docker@VM-8-15-ubuntu:~$ docker pull zookeeper:3.6
3.6: Pulling from library/zookeeper
a2abf6c4d29d: Already exists 
2bbde5250315: Pull complete 
202a34e7968e: Pull complete 
4e4231e30efc: Pull complete 
707593b95343: Pull complete 
b070e6dedb4b: Pull complete 
d48cebe29194: Pull complete 
50c693a72fee: Pull complete 
Digest: sha256:f3d4d6e63f221599408fda5a99c8e05132e15b865b25fb18b5e5ef43158a6df5
Status: Downloaded newer image for zookeeper:3.6
docker.io/library/zookeeper:3.6

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
docker-compose_nginx          latest    524bf968c7e3   2 weeks ago     142MB
docker-compose_java-service   latest    4bd1f84ef9cc   2 weeks ago     453MB
nginx                         latest    605c77e624dd   13 months ago   141MB
zookeeper                     3.6       3e9dd32cd767   14 months ago   277MB
mysql                         5.7       c20987f18b13   14 months ago   448MB
ubuntu                        latest    ba6acccedd29   16 months ago   72.8MB
redis                         6.2.1     de974760ddb2   22 months ago   105MB
portainer/portainer           1.20.2    19d07168491a   3 years ago     74.1MB
docker@VM-8-15-ubuntu:~$ 
```

2. 新建目录：`/home/docker/docker/VOLUME/zookeeper/`
3. 启动容器：`docker run -d -e TZ="Asia/Shanghai" -p 7777:2181 -v /home/docker/docker/VOLUME/zookeeper:/data --name zookeeper zookeeper:3.6`
   1. `-d`：表示在一直在后台运行容器 
   2. `-e TZ="Asia/Shanghai"`：指定上海时区 
   3. `-p 7777:2181`：对端口进行映射，将本地 7777 端口映射到容器内部的 2181 端口
   4. `-v`：将本地目录(文件)挂载到容器指定目录；
   5. `--name`：设置创建的容器名称
```bash
docker@VM-8-15-ubuntu:~$ docker run -d -e TZ="Asia/Shanghai" -p 7777:2181 -v /home/docker/docker/VOLUME/zookeeper:/data --name zookeeper zookeeper:3.6
e04b697ebd06f9111342abaa8b00fae09452fb2e39e4b879b5668c0f7466d850

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                                                     NAMES
e04b697ebd06   zookeeper:3.6                 "/docker-entrypoint.…"   4 seconds ago   Up 2 seconds   2888/tcp, 3888/tcp, 8080/tcp, 0.0.0.0:7777->2181/tcp, :::7777->2181/tcp   zookeeper
890052e7a032   mysql:5.7                     "docker-entrypoint.s…"   7 days ago      Up 7 days      0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                      sharp_kare
d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   2 weeks ago     Up 13 days     0.0.0.0:80->80/tcp, :::80->80/tcp                                         nginx
7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   2 weeks ago     Up 13 days     0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                 java-service
9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             2 weeks ago     Up 2 weeks     0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                 naughty_kowalevski

docker@VM-8-15-ubuntu:~$ 
```

4. 查看运行日志
```bash
docker@VM-8-15-ubuntu:~$ docker logs e04b697ebd06
ZooKeeper JMX enabled by default
Using config: /conf/zoo.cfg
2023-02-22 10:17:06,830 [myid:] - INFO  [main:QuorumPeerConfig@174] - Reading configuration from: /conf/zoo.cfg
2023-02-22 10:17:06,835 [myid:] - INFO  [main:QuorumPeerConfig@451] - clientPort is not set
2023-02-22 10:17:06,836 [myid:] - INFO  [main:QuorumPeerConfig@464] - secureClientPort is not set
2023-02-22 10:17:06,836 [myid:] - INFO  [main:QuorumPeerConfig@480] - observerMasterPort is not set
2023-02-22 10:17:06,838 [myid:] - INFO  [main:QuorumPeerConfig@497] - metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider
2023-02-22 10:17:06,844 [myid:] - ERROR [main:QuorumPeerConfig@722] - Invalid configuration, only one server specified (ignoring)
2023-02-22 10:17:06,848 [myid:1] - INFO  [main:DatadirCleanupManager@78] - autopurge.snapRetainCount set to 3
2023-02-22 10:17:06,848 [myid:1] - INFO  [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 0
2023-02-22 10:17:06,849 [myid:1] - INFO  [main:DatadirCleanupManager@101] - Purge task is not scheduled.
2023-02-22 10:17:06,849 [myid:1] - WARN  [main:QuorumPeerMain@138] - Either no config or no quorum defined in config, running in standalone mode
2023-02-22 10:17:06,854 [myid:1] - INFO  [main:ManagedUtil@44] - Log4j 1.2 jmx support found and enabled.
2023-02-22 10:17:06,863 [myid:1] - INFO  [main:QuorumPeerConfig@174] - Reading configuration from: /conf/zoo.cfg
2023-02-22 10:17:06,864 [myid:1] - INFO  [main:QuorumPeerConfig@451] - clientPort is not set
2023-02-22 10:17:06,864 [myid:1] - INFO  [main:QuorumPeerConfig@464] - secureClientPort is not set
2023-02-22 10:17:06,864 [myid:1] - INFO  [main:QuorumPeerConfig@480] - observerMasterPort is not set
2023-02-22 10:17:06,865 [myid:1] - INFO  [main:QuorumPeerConfig@497] - metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider
2023-02-22 10:17:06,870 [myid:1] - ERROR [main:QuorumPeerConfig@722] - Invalid configuration, only one server specified (ignoring)
2023-02-22 10:17:06,872 [myid:1] - INFO  [main:ZooKeeperServerMain@122] - Starting server
2023-02-22 10:17:06,893 [myid:1] - INFO  [main:ServerMetrics@62] - ServerMetrics initialized with provider org.apache.zookeeper.metrics.impl.DefaultMetricsProvider@5ea434c8
2023-02-22 10:17:06,897 [myid:1] - INFO  [main:FileTxnSnapLog@124] - zookeeper.snapshot.trust.empty : false
2023-02-22 10:17:06,911 [myid:1] - INFO  [main:ZookeeperBanner@42] - 
2023-02-22 10:17:06,912 [myid:1] - INFO  [main:ZookeeperBanner@42] -   ______                  _                                          
2023-02-22 10:17:06,912 [myid:1] - INFO  [main:ZookeeperBanner@42] -  |___  /                 | |                                         
2023-02-22 10:17:06,912 [myid:1] - INFO  [main:ZookeeperBanner@42] -     / /    ___     ___   | | __   ___    ___   _ __     ___   _ __   
2023-02-22 10:17:06,912 [myid:1] - INFO  [main:ZookeeperBanner@42] -    / /    / _ \   / _ \  | |/ /  / _ \  / _ \ | '_ \   / _ \ | '__|
2023-02-22 10:17:06,912 [myid:1] - INFO  [main:ZookeeperBanner@42] -   / /__  | (_) | | (_) | |   <  |  __/ |  __/ | |_) | |  __/ | |    
2023-02-22 10:17:06,913 [myid:1] - INFO  [main:ZookeeperBanner@42] -  /_____|  \___/   \___/  |_|\_\  \___|  \___| | .__/   \___| |_|
2023-02-22 10:17:06,913 [myid:1] - INFO  [main:ZookeeperBanner@42] -                                               | |                     
2023-02-22 10:17:06,913 [myid:1] - INFO  [main:ZookeeperBanner@42] -                                               |_|                     
2023-02-22 10:17:06,913 [myid:1] - INFO  [main:ZookeeperBanner@42] - 
2023-02-22 10:17:06,915 [myid:1] - INFO  [main:Environment@98] - Server environment:zookeeper.version=3.6.3--6401e4ad2087061bc6b9f80dec2d69f2e3c8660a, built on 04/08/2021 16:35 GMT
2023-02-22 10:17:06,915 [myid:1] - INFO  [main:Environment@98] - Server environment:host.name=e04b697ebd06
2023-02-22 10:17:06,915 [myid:1] - INFO  [main:Environment@98] - Server environment:java.version=11.0.13
2023-02-22 10:17:06,916 [myid:1] - INFO  [main:Environment@98] - Server environment:java.vendor=Oracle Corporation
2023-02-22 10:17:06,916 [myid:1] - INFO  [main:Environment@98] - Server environment:java.home=/usr/local/openjdk-11
2023-02-22 10:17:06,916 [myid:1] - INFO  [main:Environment@98] - Server environment:java.class.path=/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/target/classes:/apache-zookeeper-3.6.3-bin/bin/../build/classes:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/target/lib/*.jar:/apache-zookeeper-3.6.3-bin/bin/../build/lib/*.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-prometheus-metrics-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-jute-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/snappy-java-1.1.7.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/slf4j-log4j12-1.7.25.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/slf4j-api-1.7.25.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_servlet-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_hotspot-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_common-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-native-unix-common-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-native-epoll-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-resolver-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-handler-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-common-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-codec-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-buffer-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/metrics-core-3.2.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/log4j-1.2.17.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/json-simple-1.1.1.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jline-2.14.6.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-util-ajax-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-util-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-servlet-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-server-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-security-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-io-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-http-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/javax.servlet-api-3.1.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-databind-2.10.5.1.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-core-2.10.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-annotations-2.10.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/commons-cli-1.2.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/audience-annotations-0.5.0.jar:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-*.jar:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/src/main/resources/lib/*.jar:/conf:
2023-02-22 10:17:06,916 [myid:1] - INFO  [main:Environment@98] - Server environment:java.library.path=/usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib
2023-02-22 10:17:06,916 [myid:1] - INFO  [main:Environment@98] - Server environment:java.io.tmpdir=/tmp
2023-02-22 10:17:06,917 [myid:1] - INFO  [main:Environment@98] - Server environment:java.compiler=<NA>
2023-02-22 10:17:06,917 [myid:1] - INFO  [main:Environment@98] - Server environment:os.name=Linux
2023-02-22 10:17:06,917 [myid:1] - INFO  [main:Environment@98] - Server environment:os.arch=amd64
2023-02-22 10:17:06,917 [myid:1] - INFO  [main:Environment@98] - Server environment:os.version=5.4.0-126-generic
2023-02-22 10:17:06,917 [myid:1] - INFO  [main:Environment@98] - Server environment:user.name=zookeeper
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:Environment@98] - Server environment:user.home=/home/zookeeper
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:Environment@98] - Server environment:user.dir=/apache-zookeeper-3.6.3-bin
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:Environment@98] - Server environment:os.memory.free=46MB
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:Environment@98] - Server environment:os.memory.max=1000MB
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:Environment@98] - Server environment:os.memory.total=56MB
2023-02-22 10:17:06,918 [myid:1] - INFO  [main:ZooKeeperServer@129] - zookeeper.enableEagerACLCheck = false
2023-02-22 10:17:06,919 [myid:1] - INFO  [main:ZooKeeperServer@137] - zookeeper.digest.enabled = true
2023-02-22 10:17:06,919 [myid:1] - INFO  [main:ZooKeeperServer@141] - zookeeper.closeSessionTxn.enabled = true
2023-02-22 10:17:06,919 [myid:1] - INFO  [main:ZooKeeperServer@1461] - zookeeper.flushDelay=0
2023-02-22 10:17:06,919 [myid:1] - INFO  [main:ZooKeeperServer@1470] - zookeeper.maxWriteQueuePollTime=0
2023-02-22 10:17:06,920 [myid:1] - INFO  [main:ZooKeeperServer@1479] - zookeeper.maxBatchSize=1000
2023-02-22 10:17:06,920 [myid:1] - INFO  [main:ZooKeeperServer@243] - zookeeper.intBufferStartingSizeBytes = 1024
2023-02-22 10:17:06,921 [myid:1] - INFO  [main:BlueThrottle@141] - Weighed connection throttling is disabled
2023-02-22 10:17:06,923 [myid:1] - INFO  [main:ZooKeeperServer@1273] - minSessionTimeout set to 4000
2023-02-22 10:17:06,923 [myid:1] - INFO  [main:ZooKeeperServer@1282] - maxSessionTimeout set to 40000
2023-02-22 10:17:06,924 [myid:1] - INFO  [main:ResponseCache@45] - Response cache size is initialized with value 400.
2023-02-22 10:17:06,924 [myid:1] - INFO  [main:ResponseCache@45] - Response cache size is initialized with value 400.
2023-02-22 10:17:06,925 [myid:1] - INFO  [main:RequestPathMetricsCollector@109] - zookeeper.pathStats.slotCapacity = 60
2023-02-22 10:17:06,926 [myid:1] - INFO  [main:RequestPathMetricsCollector@110] - zookeeper.pathStats.slotDuration = 15
2023-02-22 10:17:06,926 [myid:1] - INFO  [main:RequestPathMetricsCollector@111] - zookeeper.pathStats.maxDepth = 6
2023-02-22 10:17:06,926 [myid:1] - INFO  [main:RequestPathMetricsCollector@112] - zookeeper.pathStats.initialDelay = 5
2023-02-22 10:17:06,926 [myid:1] - INFO  [main:RequestPathMetricsCollector@113] - zookeeper.pathStats.delay = 5
2023-02-22 10:17:06,926 [myid:1] - INFO  [main:RequestPathMetricsCollector@114] - zookeeper.pathStats.enabled = false
2023-02-22 10:17:06,945 [myid:1] - INFO  [main:ZooKeeperServer@1498] - The max bytes for all large requests are set to 104857600
2023-02-22 10:17:06,945 [myid:1] - INFO  [main:ZooKeeperServer@1512] - The large request threshold is set to -1
2023-02-22 10:17:06,946 [myid:1] - INFO  [main:ZooKeeperServer@339] - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 clientPortListenBacklog -1 datadir /datalog/version-2 snapdir /data/version-2
2023-02-22 10:17:06,988 [myid:1] - INFO  [main:Log@169] - Logging initialized @699ms to org.eclipse.jetty.util.log.Slf4jLog
2023-02-22 10:17:07,072 [myid:1] - WARN  [main:ContextHandler@1660] - o.e.j.s.ServletContextHandler@3c41ed1d{/,null,STOPPED} contextPath ends with /*
2023-02-22 10:17:07,073 [myid:1] - WARN  [main:ContextHandler@1671] - Empty contextPath
2023-02-22 10:17:07,096 [myid:1] - INFO  [main:Server@375] - jetty-9.4.39.v20210325; built: 2021-03-25T14:42:11.471Z; git: 9fc7ca5a922f2a37b84ec9dbc26a5168cee7e667; jvm 11.0.13+8
2023-02-22 10:17:07,156 [myid:1] - INFO  [main:DefaultSessionIdManager@334] - DefaultSessionIdManager workerName=node0
2023-02-22 10:17:07,156 [myid:1] - INFO  [main:DefaultSessionIdManager@339] - No SessionScavenger set, using defaults
2023-02-22 10:17:07,158 [myid:1] - INFO  [main:HouseKeeper@132] - node0 Scavenging every 600000ms
2023-02-22 10:17:07,163 [myid:1] - WARN  [main:ConstraintSecurityHandler@759] - ServletContext@o.e.j.s.ServletContextHandler@3c41ed1d{/,null,STARTING} has uncovered http methods for path: /*
2023-02-22 10:17:07,182 [myid:1] - INFO  [main:ContextHandler@916] - Started o.e.j.s.ServletContextHandler@3c41ed1d{/,null,AVAILABLE}
2023-02-22 10:17:07,201 [myid:1] - INFO  [main:AbstractConnector@331] - Started ServerConnector@5b239d7d{HTTP/1.1, (http/1.1)}{0.0.0.0:8080}
2023-02-22 10:17:07,202 [myid:1] - INFO  [main:Server@415] - Started @918ms
2023-02-22 10:17:07,202 [myid:1] - INFO  [main:JettyAdminServer@191] - Started AdminServer on address 0.0.0.0, port 8080 and command URL /commands
2023-02-22 10:17:07,207 [myid:1] - INFO  [main:ServerCnxnFactory@169] - Using org.apache.zookeeper.server.NIOServerCnxnFactory as server connection factory
2023-02-22 10:17:07,208 [myid:1] - WARN  [main:ServerCnxnFactory@309] - maxCnxns is not configured, using default value 0.
2023-02-22 10:17:07,209 [myid:1] - INFO  [main:NIOServerCnxnFactory@666] - Configuring NIO connection handler with 10s sessionless connection timeout, 1 selector thread(s), 4 worker threads, and 64 kB direct buffers.
2023-02-22 10:17:07,211 [myid:1] - INFO  [main:NIOServerCnxnFactory@674] - binding to port /0.0.0.0:2181
2023-02-22 10:17:07,232 [myid:1] - INFO  [main:WatchManagerFactory@42] - Using org.apache.zookeeper.server.watch.WatchManager as watch manager
2023-02-22 10:17:07,232 [myid:1] - INFO  [main:WatchManagerFactory@42] - Using org.apache.zookeeper.server.watch.WatchManager as watch manager
2023-02-22 10:17:07,233 [myid:1] - INFO  [main:ZKDatabase@132] - zookeeper.snapshotSizeFactor = 0.33
2023-02-22 10:17:07,234 [myid:1] - INFO  [main:ZKDatabase@152] - zookeeper.commitLogCount=500
2023-02-22 10:17:07,236 [myid:1] - INFO  [main:SnapStream@61] - zookeeper.snapshot.compression.method = CHECKED
2023-02-22 10:17:07,237 [myid:1] - INFO  [main:FileSnap@85] - Reading snapshot /data/version-2/snapshot.0
2023-02-22 10:17:07,240 [myid:1] - WARN  [main:DataTree@1767] - Got EOF exception while reading the digest, likely due to the reading an older snapshot.
2023-02-22 10:17:07,243 [myid:1] - INFO  [main:ZKDatabase@289] - Snapshot loaded in 9 ms, highest zxid is 0x0, digest is 1371985504
2023-02-22 10:17:07,243 [myid:1] - INFO  [main:FileTxnSnapLog@470] - Snapshotting: 0x0 to /data/version-2/snapshot.0
2023-02-22 10:17:07,244 [myid:1] - INFO  [main:ZooKeeperServer@529] - Snapshot taken in 1 ms
2023-02-22 10:17:07,258 [myid:1] - INFO  [main:RequestThrottler@74] - zookeeper.request_throttler.shutdownTimeout = 10000
2023-02-22 10:17:07,258 [myid:1] - INFO  [ProcessThread(sid:0 cport:2181)::PrepRequestProcessor@136] - PrepRequestProcessor (sid:0) started, reconfigEnabled=false
2023-02-22 10:17:07,297 [myid:1] - INFO  [main:ContainerManager@83] - Using checkIntervalMs=60000 maxPerMinute=10000 maxNeverUsedIntervalMs=0
2023-02-22 10:17:07,298 [myid:1] - INFO  [main:ZKAuditProvider@42] - ZooKeeper audit is disabled.
2023-02-22 10:17:07,392 [myid:1] - INFO  [SyncThread:0:FileTxnLog@284] - Creating new log file: log.1
```
### ③、服务提供者 cloud-provider-payment8004
> zookeeper 节点是临时节点，即一段时间获取不到心跳就会移除节点，相当于关闭了保护模式的 Eureka

1. 新建模块 cloud-provider-payment8004

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677029410530-1d716ed8-9d70-4e80-b481-783348637d97.png#averageHue=%233d4144&clientId=uc8e9057c-b58a-4&from=paste&height=634&id=u829e94e0&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50804&status=done&style=stroke&taskId=u82264bdb-20e4-4926-8a2f-e70fe01aae2&title=&width=784)![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677034318390-0b8dd800-bc41-4f0e-9ba2-57525177bd13.png#averageHue=%233d4144&clientId=uc8e9057c-b58a-4&from=paste&height=257&id=u43cfeea2&name=image.png&originHeight=257&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10965&status=done&style=stroke&taskId=u56b911ce-329e-426f-a06e-258f4ef3a09&title=&width=293)

2. 修改 pom.xml，删除：`spring-cloud-starter-netflix-eureka-client`，新增：`spring-cloud-starter-zookeeper-discovery`，另数据操作的包暂时不需要
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 父项目 -->
    <parent>
        <groupId>com.yuehai</groupId>
        <artifactId>SpringCloud</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    
    <artifactId>cloud-provider-payment8004</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- SpringBoot整合zookeeper客户端 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-zookeeper-discovery</artifactId>
        </dependency>

    </dependencies>

</project>
```

3. 修改 application.yml 配置文件，新增属性：`spring.cloud.zookeeper`
```yaml
# 服务端口号
server:
    port: 8004

# spring 配置
spring:
    application:
        # 服务名称 微服务提供者支付模块 cloud-provider-payment8004
        name: cloud-payment-service
    cloud:
        # 指定 zookeeper 服务端的注册地址
        zookeeper:
            # 集群 zookeeper 间使用 , 分隔
            connect-string: 43.138.106.181:7777
```

4. 修改主启动类，新增注解：`@EnableDiscoveryClient`，用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务提供者支付模块 cloud-provider-payment8004
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */
@SpringBootApplication
@EnableDiscoveryClient
public class ProviderPayment8004 {

    public static void main(String[] args) {
        SpringApplication.run(ProviderPayment8004.class, args);
    }

}

```

5. 编写业务类 controller
```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

/**
 * @author 月海
 * @create 2023/2/20 14:35
 */

@RestController
@RequestMapping("/test")
public class PaymentController {

    @Value("${server.port}")
    private String serverPort;

    /**
     * 测试 get，查询全部
     */
    @GetMapping("/getTest")
    public JsonResult getTest(){
        return JsonResult.success("OK SpringCloud with zookeeper").put("服务端口为：", serverPort).put("生成随机数：", UUID.randomUUID().toString());
    }

}

```

6. 访问测试：[http://localhost:8004/test/getTest](http://localhost:8004/test/getTest)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677032479637-90c15fba-672d-449c-8ba4-004fba940712.png#averageHue=%2391d4bf&clientId=uc8e9057c-b58a-4&from=paste&height=298&id=ub33d889d&name=image.png&originHeight=298&originWidth=486&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35970&status=done&style=stroke&taskId=ua4b1c4fb-c144-4c74-bab6-dc206a359d6&title=&width=486)

7. 查看 zookeeper：
8. 进入容器：
```bash
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                                                                     NAMES
e04b697ebd06   zookeeper:3.6                 "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   2888/tcp, 3888/tcp, 8080/tcp, 0.0.0.0:7777->2181/tcp, :::7777->2181/tcp   zookeeper
890052e7a032   mysql:5.7                     "docker-entrypoint.s…"   7 days ago       Up 7 days       0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                      sharp_kare
d2cca7634535   docker-compose_nginx          "/docker-entrypoint.…"   2 weeks ago      Up 13 days      0.0.0.0:80->80/tcp, :::80->80/tcp                                         nginx
7ed99735286d   docker-compose_java-service   "java -jar /applicat…"   2 weeks ago      Up 13 days      0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                 java-service
9c710fd9a47a   portainer/portainer:1.20.2    "/portainer"             2 weeks ago      Up 2 weeks      0.0.0.0:9443->9000/tcp, :::9443->9000/tcp                                 naughty_kowalevski

docker@VM-8-15-ubuntu:~$ docker exec -it e04b697ebd06 bash

root@e04b697ebd06:/apache-zookeeper-3.6.3-bin#
```

9. 进入 zookeeper 命令行界面 Cli
```bash
oot@e04b697ebd06:/apache-zookeeper-3.6.3-bin# pwd
/apache-zookeeper-3.6.3-bin
root@e04b697ebd06:/apache-zookeeper-3.6.3-bin# ls -l
total 40
-rw-r--r-- 1 zookeeper zookeeper 11358 Apr  9  2021 LICENSE.txt
-rw-r--r-- 1 zookeeper zookeeper   432 Apr  9  2021 NOTICE.txt
-rw-r--r-- 1 zookeeper zookeeper  1963 Apr  9  2021 README.md
-rw-r--r-- 1 zookeeper zookeeper  3166 Apr  9  2021 README_packaging.md
drwxr-xr-x 2 zookeeper zookeeper  4096 Apr  9  2021 bin
drwxr-xr-x 2 zookeeper zookeeper  4096 Dec 23  2021 conf
drwxr-xr-x 5 zookeeper zookeeper  4096 Apr  9  2021 docs
drwxr-xr-x 2 zookeeper zookeeper  4096 Dec 23  2021 lib
root@e04b697ebd06:/apache-zookeeper-3.6.3-bin# cd bin
root@e04b697ebd06:/apache-zookeeper-3.6.3-bin/bin# ls -l
total 64
-rwxr-xr-x 1 zookeeper zookeeper   232 Apr  9  2021 README.txt
-rwxr-xr-x 1 zookeeper zookeeper  2066 Apr  9  2021 zkCleanup.sh
-rwxr-xr-x 1 zookeeper zookeeper  1158 Apr  9  2021 zkCli.cmd
-rwxr-xr-x 1 zookeeper zookeeper  1620 Apr  9  2021 zkCli.sh
-rwxr-xr-x 1 zookeeper zookeeper  1843 Apr  9  2021 zkEnv.cmd
-rwxr-xr-x 1 zookeeper zookeeper  3690 Apr  9  2021 zkEnv.sh
-rwxr-xr-x 1 zookeeper zookeeper  4559 Apr  9  2021 zkServer-initialize.sh
-rwxr-xr-x 1 zookeeper zookeeper  1286 Apr  9  2021 zkServer.cmd
-rwxr-xr-x 1 zookeeper zookeeper 11332 Apr  9  2021 zkServer.sh
-rwxr-xr-x 1 zookeeper zookeeper   988 Apr  9  2021 zkSnapShotToolkit.cmd
-rwxr-xr-x 1 zookeeper zookeeper  1377 Apr  9  2021 zkSnapShotToolkit.sh
-rwxr-xr-x 1 zookeeper zookeeper   996 Apr  9  2021 zkTxnLogToolkit.cmd
-rwxr-xr-x 1 zookeeper zookeeper  1385 Apr  9  2021 zkTxnLogToolkit.sh
root@e04b697ebd06:/apache-zookeeper-3.6.3-bin/bin# ./zkCli.sh
Connecting to localhost:2181
2023-02-22 10:32:15,986 [myid:] - INFO  [main:Environment@98] - Client environment:zookeeper.version=3.6.3--6401e4ad2087061bc6b9f80dec2d69f2e3c8660a, built on 04/08/2021 16:35 GMT
2023-02-22 10:32:15,991 [myid:] - INFO  [main:Environment@98] - Client environment:host.name=e04b697ebd06
2023-02-22 10:32:15,992 [myid:] - INFO  [main:Environment@98] - Client environment:java.version=11.0.13
2023-02-22 10:32:16,007 [myid:] - INFO  [main:Environment@98] - Client environment:java.vendor=Oracle Corporation
2023-02-22 10:32:16,007 [myid:] - INFO  [main:Environment@98] - Client environment:java.home=/usr/local/openjdk-11
2023-02-22 10:32:16,008 [myid:] - INFO  [main:Environment@98] - Client environment:java.class.path=/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/target/classes:/apache-zookeeper-3.6.3-bin/bin/../build/classes:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/target/lib/*.jar:/apache-zookeeper-3.6.3-bin/bin/../build/lib/*.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-prometheus-metrics-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-jute-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/zookeeper-3.6.3.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/snappy-java-1.1.7.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/slf4j-log4j12-1.7.25.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/slf4j-api-1.7.25.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_servlet-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_hotspot-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient_common-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/simpleclient-0.6.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-native-unix-common-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-native-epoll-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-transport-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-resolver-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-handler-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-common-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-codec-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/netty-buffer-4.1.63.Final.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/metrics-core-3.2.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/log4j-1.2.17.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/json-simple-1.1.1.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jline-2.14.6.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-util-ajax-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-util-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-servlet-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-server-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-security-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-io-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jetty-http-9.4.39.v20210325.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/javax.servlet-api-3.1.0.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-databind-2.10.5.1.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-core-2.10.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/jackson-annotations-2.10.5.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/commons-cli-1.2.jar:/apache-zookeeper-3.6.3-bin/bin/../lib/audience-annotations-0.5.0.jar:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-*.jar:/apache-zookeeper-3.6.3-bin/bin/../zookeeper-server/src/main/resources/lib/*.jar:/conf:
2023-02-22 10:32:16,009 [myid:] - INFO  [main:Environment@98] - Client environment:java.library.path=/usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib
2023-02-22 10:32:16,010 [myid:] - INFO  [main:Environment@98] - Client environment:java.io.tmpdir=/tmp
2023-02-22 10:32:16,010 [myid:] - INFO  [main:Environment@98] - Client environment:java.compiler=<NA>
2023-02-22 10:32:16,010 [myid:] - INFO  [main:Environment@98] - Client environment:os.name=Linux
2023-02-22 10:32:16,011 [myid:] - INFO  [main:Environment@98] - Client environment:os.arch=amd64
2023-02-22 10:32:16,011 [myid:] - INFO  [main:Environment@98] - Client environment:os.version=5.4.0-126-generic
2023-02-22 10:32:16,012 [myid:] - INFO  [main:Environment@98] - Client environment:user.name=root
2023-02-22 10:32:16,013 [myid:] - INFO  [main:Environment@98] - Client environment:user.home=/root
2023-02-22 10:32:16,013 [myid:] - INFO  [main:Environment@98] - Client environment:user.dir=/apache-zookeeper-3.6.3-bin/bin
2023-02-22 10:32:16,014 [myid:] - INFO  [main:Environment@98] - Client environment:os.memory.free=48MB
2023-02-22 10:32:16,018 [myid:] - INFO  [main:Environment@98] - Client environment:os.memory.max=256MB
2023-02-22 10:32:16,019 [myid:] - INFO  [main:Environment@98] - Client environment:os.memory.total=56MB
2023-02-22 10:32:16,023 [myid:] - INFO  [main:ZooKeeper@1006] - Initiating client connection, connectString=localhost:2181 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@735b478
2023-02-22 10:32:16,028 [myid:] - INFO  [main:X509Util@77] - Setting -D jdk.tls.rejectClientInitiatedRenegotiation=true to disable client-initiated TLS renegotiation
2023-02-22 10:32:16,036 [myid:] - INFO  [main:ClientCnxnSocket@239] - jute.maxbuffer value is 1048575 Bytes
2023-02-22 10:32:16,044 [myid:] - INFO  [main:ClientCnxn@1736] - zookeeper.request.timeout value is 0. feature enabled=false
Welcome to ZooKeeper!
JLine support is enabled
2023-02-22 10:32:16,077 [myid:localhost:2181] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1181] - Opening socket connection to server localhost/127.0.0.1:2181.
2023-02-22 10:32:16,081 [myid:localhost:2181] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1183] - SASL config status: Will not attempt to authenticate using SASL (unknown error)
2023-02-22 10:32:16,108 [myid:localhost:2181] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1013] - Socket connection established, initiating session, client: /127.0.0.1:60482, server: localhost/127.0.0.1:2181
2023-02-22 10:32:16,125 [myid:localhost:2181] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1448] - Session establishment complete on server localhost/127.0.0.1:2181, session id = 0x1007b0e7d0a0004, negotiated timeout = 30000

WATCHER::

WatchedEvent state:SyncConnected type:None path:null

[zk: localhost:2181(CONNECTED) 0]
```

10. 查看节点、获得基本信息 json
```bash
[zk: localhost:2181(CONNECTED) 0] ls /services 
[cloud-payment-service]
[zk: localhost:2181(CONNECTED) 1] get /services 

[zk: localhost:2181(CONNECTED) 2] ls /
services    zookeeper   
[zk: localhost:2181(CONNECTED) 2] ls /services/cloud-payment-service
[356dc6a2-d686-4f92-be62-40de373b02de]
[zk: localhost:2181(CONNECTED) 3] ls /services/cloud-payment-service/356dc6a2-d686-4f92-be62-40de373b02de 
[]
[zk: localhost:2181(CONNECTED) 4] get /services/cloud-payment-service/356dc6a2-d686-4f92-be62-40de373b02de 
{"name":"cloud-payment-service","id":"356dc6a2-d686-4f92-be62-40de373b02de","address":"host.docker.internal","port":8004,"sslPort":null,"payload":{"@class":"org.springframework.cloud.zookeeper.discovery.ZookeeperInstance","id":"application-1","name":"cloud-payment-service","metadata":{}},"registrationTimeUTC":1677032412134,"serviceType":"DYNAMIC","uriSpec":{"parts":[{"value":"scheme","variable":true},{"value":"://","variable":false},{"value":"address","variable":true},{"value":":","variable":false},{"value":"port","variable":true}]}}
[zk: localhost:2181(CONNECTED) 5] 
[zk: localhost:2181(CONNECTED) 5] 
[zk: localhost:2181(CONNECTED) 5] 
```

11. json 格式化：
```json
{
    "name": "cloud-payment-service",
    "id": "356dc6a2-d686-4f92-be62-40de373b02de",
    "address": "host.docker.internal",
    "port": 8004,
    "sslPort": null,
    "payload": {
        "@class": "org.springframework.cloud.zookeeper.discovery.ZookeeperInstance",
        "id": "application-1",
        "name": "cloud-payment-service",
        "metadata": {}
    },
    "registrationTimeUTC": 1677032412134,
    "serviceType": "DYNAMIC",
    "uriSpec": {
        "parts": [
            {
                "value": "scheme",
                "variable": true
            },
            {
                "value": "://",
                "variable": false
            },
            {
                "value": "address",
                "variable": true
            },
            {
                "value": ":",
                "variable": false
            },
            {
                "value": "port",
                "variable": true
            }
        ]
    }
}
```
### ④、服务消费者 cloud-consumerzk-order80

1. 新建模块 cloud-consumerzk-order80

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677034278534-e46c60e5-bf14-49cd-9cbe-f56394226707.png#averageHue=%233d4145&clientId=uc8e9057c-b58a-4&from=paste&height=634&id=u251ec106&name=image.png&originHeight=634&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50300&status=done&style=stroke&taskId=u512d0003-d98f-4229-aa0a-c5ba09e6580&title=&width=784)

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
    
    <artifactId>cloud-consumerzk-order80</artifactId>
    
    <dependencies>
        <!-- 引入自己定义的 api 通用包，可以使用 Payment 支付 Entity -->
        <dependency>
            <groupId>com.yuehai</groupId>
            <artifactId>cloud-api-commons</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    
        <!-- SpringBoot 整合 zookeeper 客户端 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-zookeeper-discovery</artifactId>
        </dependency>
    </dependencies>

</project>
```

3. 修改 application.yml 配置文件
```yaml
# 服务端口号
server:
    port: 80

# spring 配置
spring:
    application:
        # 服务名称  微服务消费者订单模块 cloud-consumerzk-order80
        name: cloud-consumer-order
    cloud:
        # 指定 zookeeper 服务端的注册地址
        zookeeper:
            # 集群 zookeeper 间使用 , 分隔
            connect-string: 43.138.106.181:7777
```

4. 修改主启动类
```java
package com.yuehai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * 微服务消费者订单模块 cloud-consumzk-order80
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableDiscoveryClient：该注解用于向使用 consul 或者 zookeeper 作为注册中心时注册服务
 */

@SpringBootApplication
@EnableDiscoveryClient
public class ConsumzkOrder80 {
    public static void main(String[] args) {
        SpringApplication.run(ConsumzkOrder80.class, args);
    }

}
```

5. 复制之前模块 cloud-consumer-order80 的配置类
```java
package com.yuehai.config;

import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * @author 月海
 * @create 2023/2/21 8:48
 */

@Configuration
public class ApplicationContextConfig {

    @Bean
    /**
     * 使用 @LoadBalanced 注解赋予 RestTemplate 负载均衡的能力
     */
    @LoadBalanced
    public RestTemplate restTemplate(){
        return new RestTemplate();
    }

}

```

6. 编写业务类 controller
```java
package com.yuehai.controller;

import com.yuehai.utils.JsonResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.util.HashMap;

/**
 * @author 月海
 * @create 2023/2/21 8:40
 */

@RestController
public class OrderController {

    /**
     * 调用微服务中名为 CLOUD-PAYMENT-SERVICE 的服务
     */
    public static final String PAYMENT_SRV_URL = "http://cloud-payment-service";

    @Resource
    private RestTemplate restTemplate;

    /**
     * 客户端用浏览器是 get 请求，底层实质也是发送 get 调用服务端 8001
     */
    @GetMapping("/getOrder/payment/get")
    public JsonResult getOrder(){
        /**
         * 使用 restTemplate 访问 restful get 接口：
         *      url, responseType, uriVariables) 这三个参数分别代表：
         *      请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
         */
        return JsonResult.success(restTemplate.getForObject(PAYMENT_SRV_URL + "/test/getTest", HashMap.class));
    }


}
```

7. 访问测试：[http://localhost/getOrder/payment/get](http://localhost/getOrder/payment/get)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677035584499-b3f37a6d-8c5c-442c-9948-791997f8054b.png#averageHue=%2378b2e0&clientId=uc8e9057c-b58a-4&from=paste&height=319&id=u716f190a&name=image.png&originHeight=319&originWidth=490&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34524&status=done&style=stroke&taskId=ud84c0e41-1530-436a-9fae-c92c56a5550&title=&width=490)
## 3、Consul
### ①、Consul 简介
#### Ⅰ、是什么
> [https://www.consul.io/intro/index.html](https://www.consul.io/intro/index.html)

1. Consul 是一套开源的分布式服务发现和配置管理系统，由 HashiCorp 公司用 Go 语言开发。
2. 提供了微服务系统中的服务治理、配置中心、控制总线等功能。
3. 这些功能中的每一个都可以根据需要单独使用，也可以一起使用以构建全方位的服务网格，总之 Consul 提供了一种完整的服务网格解决方案。
4. 它具有很多优点。包括： 
   1. 基于 raft 协议，比较简洁；
   2. 支持健康检查
   3. 支持 HTTP 和 DNS 协议
   4. 支持跨数据中心的 WAN 集群
   5. 提供图形界面
   6. 跨平台，支持 Linux、Mac、Windows
#### Ⅱ、能干嘛

1. 服务发现
2. 健康监测
3. KV 存储
4. 多数据中心
5. 可视化 Web 界面

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677040533344-40c1e081-7e4b-49cf-8ed3-f366a162f057.png#averageHue=%23fcfaf7&clientId=uc8e9057c-b58a-4&from=paste&height=589&id=ue2836c81&name=image.png&originHeight=589&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=116062&status=done&style=stroke&taskId=u8da7a108-936e-41ba-bb2e-6de887d0a49&title=&width=860)
#### Ⅲ、去哪下
> [https://www.consul.io/downloads.html](https://www.consul.io/downloads.html)

#### Ⅳ、怎么玩
> [https://www.springcloud.cc/spring-cloud-consul.html](https://www.springcloud.cc/spring-cloud-consul.html)

### ②、
## 4、三个注册中心异同点
### ①、CAP 是什么

1. C：Consistency（强一致性）
2. A：Availability（可用性）
3. P：Partition tolerance（分区容错性）
4. CAP 理论关注粒度是数据，而不是整体系统设计的策略
### ②、经典 CAP 图

1. 最多只能同时较好的满足两个。
2.  CAP 理论的核心是：一个分布式系统不可能同时很好的满足一致性，可用性和分区容错性这三个需求，因此，根据 CAP 原理将 NoSQL 数据库分成了三大类：
   1. 满足 CA 原则：单点集群，满足一致性，可用性的系统，通常在可扩展性上不太强大。
   2. 满足 CP 原则：满足一致性，分区容错性的系统，通常性能不是特别高。
   3. 满足 AP 原则：满足可用性，分区容错性的系统，通常可能对一致性要求低一些。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677041100149-e6318d76-cae3-4f27-9a12-85f38f6df27a.png#averageHue=%2327445f&clientId=uc8e9057c-b58a-4&from=paste&height=584&id=u76832f34&name=image.png&originHeight=584&originWidth=671&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48746&status=done&style=stroke&taskId=u8b179117-cca2-4367-bf9e-2e0d7f9a236&title=&width=671)
### ③、AP 架构：Eureka

1. 当网络分区出现后，为了保证可用性，系统 B 可以返回旧值，保证系统的可用性。
2. 结论：违背了一致性C的要求，只满足可用性和分区容错，即AP

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677041238601-b2759e08-c3ea-4dbd-8223-ddac0e49742d.png#averageHue=%23edede8&clientId=uc8e9057c-b58a-4&from=paste&height=509&id=u3fb81732&name=image.png&originHeight=509&originWidth=635&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109020&status=done&style=stroke&taskId=u3fcf6430-6abe-47f7-9634-e2edf073256&title=&width=635)
### ④、CP 架构：Zookeeper/Consul

1. 当网络分区出现后，为了保证一致性，就必须拒接请求，否则无法保证一致性
2. 结论：违背了可用性 A 的要求，只满足一致性和分区容错，即 CP

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677041267949-cb2ca4c0-8e90-4cbe-b177-86bd7d1862cd.png#averageHue=%23fcfbfb&clientId=uc8e9057c-b58a-4&from=paste&height=505&id=udad564fb&name=image.png&originHeight=505&originWidth=646&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59219&status=done&style=stroke&taskId=u18a7d2e8-d5c0-4755-a7d3-0792b9ae3b6&title=&width=646)
# 四、负载均衡服务调用 Ribbon
> 官网：[https://github.com/Netflix/ribbon/wiki/Getting-Started](https://github.com/Netflix/ribbon/wiki/Getting-Started)
> Ribbon 目前也进入维护模式，未来替换方案：LoadBalancer

## 1、Ribbon
### ①、简介
#### Ⅰ、Ribbon 是什么

1. Spring Cloud Ribbon 是基于 Netflix Ribbon 实现的一套客户端负载均衡的工具。
2. 简单的说，Ribbon 是 Netflix 发布的开源项目，主要功能是提供客户端的软件负载均衡算法和服务调用。Ribbon 客户端组件提供一系列完善的配置项如连接超时，重试等。
3. 简单的说，就是在配置文件中列出 Load Balancer（简称LB）后面所有的机器，Ribbon 会自动的帮助你基于某种规则（如简单轮询，随机连接等）去连接这些机器。
4. 我们很容易使用 Ribbon 实现自定义的负载均衡算法。
#### Ⅱ、能干嘛
> 负载均衡 + RestTemplate 调用

##### （1）、LB（负载均衡）

1. LB负载均衡(Load Balance)是什么：简单的说就是将用户的请求平摊的分配到多个服务上，从而达到系统的 HA（高可用）。常见的负载均衡有软件 Nginx，LVS，硬件 F5 等。
2. Ribbon 本地负载均衡客户端 VS Nginx 服务端负载均衡区别：
   1. Nginx 是服务器负载均衡，客户端所有请求都会交给 nginx，然后由 nginx 实现转发请求。即负载均衡是由服务端实现的。
   2. Ribbon 本地负载均衡，在调用微服务接口时候，会在注册中心上获取注册信息服务列表之后缓存到 JVM 本地，从而在本地实现 RPC 远程服务调用技术。
3. 集中式 LB：即在服务的消费方和提供方之间使用独立的 LB 设施(可以是硬件，如 F5, 也可以是软件，如 nginx)，由该设施负责把访问请求通过某种策略转发至服务的提供方；
4. 进程内 LB：将 LB 逻辑集成到消费方，消费方从服务注册中心获知有哪些地址可用，然后自己再从这些地址中选择出一个合适的服务器。
5. Ribbon 就属于进程内 LB，它只是一个类库，集成于消费方进程，消费方通过它来获取到服务提供方的地址。
##### （2）、轮询负载访问

1. 轮询算法是最简单的一种负载均衡算法。它的原理是把来自用户的请求轮流分配给内部的服务器：从服务器 1 开始，直到服务器 N，然后重新开始循环。
2. 算法的优点是其简洁性，它无需记录当前所有连接的状态，所以它是一种无状态调度。
### ②、Ribbon 负载均衡演示
#### Ⅰ、架构说明

1. Ribbon 在工作时分成两步：
2. 第一步先选择 EurekaServer，它优先选择在同一个区域内负载较少的 server
3. 第二步再根据用户指定的策略，在从 server 取到的服务注册列表中选择一个地址。
4. 其中 Ribbon 提供了多种策略：比如轮询、随机和根据响应时间加权。
5. 总结：Ribbon 其实就是一个软负载均衡的客户端组件， 他可以和其他所需请求的客户端结合使用，和 eureka 结合只是其中的一个实例。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677047962628-dc8d4f1d-0215-4ed2-8497-47b4a113a1e3.png#averageHue=%23fefef8&clientId=u92554e7e-b38e-4&from=paste&height=481&id=vn0W7&name=image.png&originHeight=481&originWidth=890&originalType=binary&ratio=1&rotation=0&showTitle=false&size=146245&status=done&style=stroke&taskId=uf24fe799-2c0f-4d51-aa66-cf56044d34e&title=&width=890)
#### Ⅱ、为什么之前并没有引入 Ribbon 依赖也可以使用负载均衡

- 原因：`spring-cloud-starter-netflix-eureka-client` 自带了 `spring-cloud-starter-ribbon` 引用

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677048343155-c7ffe156-40fe-432a-ba37-bbfad411380f.png#averageHue=%233c4144&clientId=u92554e7e-b38e-4&from=paste&height=560&id=ADr0r&name=image.png&originHeight=560&originWidth=717&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59699&status=done&style=stroke&taskId=uc9c9c9af-f462-4dcc-941d-97936274196&title=&width=717)
#### Ⅲ、二说 RestTemplate 的使用
##### （1）、官网
> [https://docs.spring.io/spring-framework/docs/5.2.2.RELEASE/javadoc-api/org/springframework/web/client/RestTemplate.html](https://docs.spring.io/spring-framework/docs/5.2.2.RELEASE/javadoc-api/org/springframework/web/client/RestTemplate.html)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677048408213-e1fa3220-f90e-4a9f-9cc5-5efaa1073917.png#averageHue=%233e433c&clientId=u92554e7e-b38e-4&from=paste&height=329&id=WEwhh&name=image.png&originHeight=329&originWidth=926&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26077&status=done&style=stroke&taskId=ue19ee78d-479b-4028-bac3-c8baa435d2c&title=&width=926)
##### （2）、`getForObjec`、`getForEntity` 方法 

1. `getForObjec`：返回对象为响应体中数据转化成的对象，基本上可以理解为Json
```java
/**
 * 客户端用浏览器是 get 请求，底层实质也是发送 get 调用服务端 8001
 */
@GetMapping("/getOrder/payment/getForObject")
public JsonResult getForObject(){
    /**
     * 使用 restTemplate 访问 restful get 接口：
     *      url, responseType, uriVariables) 这三个参数分别代表：
     *      请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
     */
    return JsonResult.success(restTemplate.getForObject(PAYMENT_SRV_URL + "/test/getTest", HashMap.class));
}
```
```json
{
    "msg": "ok",
    "data": {
        "msg": "ok",
        "code": 200,
        "data": [
            {
                "id": 1,
                "serial": "月海"
            },
            {
                "id": 2,
                "serial": "言"
            },
            {
                "id": 1627853700842143746,
                "serial": "2"
            }
        ],
        "服务端口为：": "8002"
    },
    "code": 200
}
```

2. `getForEntity`：返回对象为 ResponseEntity 对象，包含了响应中的一些详细的重要信息，比如响应头、响应状态码、响应体等
```java
/**
 * 客户端用浏览器是 get 请求，底层实质也是发送 get 调用服务端 8001
 */
@GetMapping("/getOrder/payment/getForEntity")
public JsonResult getForEntity(){
    /**
     * 使用 restTemplate 访问 restful get 接口：
     *      url, responseType, uriVariables) 这三个参数分别代表：
     *      请求地址、HTTP 响应转换被转换成的对象类型、url占位参数
     */
    return JsonResult.success(restTemplate.getForEntity(PAYMENT_SRV_URL + "/test/getTest", HashMap.class));
}
```
```json
{
    "msg": "ok",
    "data": {
        "headers": {
            "Content-Type": [
                "application/json"
            ],
            "Transfer-Encoding": [
                "chunked"
            ],
            "Date": [
                "Wed, 22 Feb 2023 07:11:04 GMT"
            ],
            "Keep-Alive": [
                "timeout=60"
            ],
            "Connection": [
                "keep-alive"
            ]
        },
        "body": {
            "msg": "ok",
            "code": 200,
            "data": [
                {
                    "id": 1,
                    "serial": "月海"
                },
                {
                    "id": 2,
                    "serial": "言"
                },
                {
                    "id": 1627853700842143746,
                    "serial": "2"
                }
            ],
            "服务端口为：": "8001"
        },
        "statusCodeValue": 200,
        "statusCode": "OK"
    },
    "code": 200
}
```
##### （3）、`postForObject`、`postForEntity` 方法

1. `postForObject`：与 `getForObjec` 类似，返回对象为响应体中数据转化成的对象，基本上可以理解为Json
```java
/**
 * 客户端用浏览器是 get 请求，但是底层实质发送 post 调用服务端8001
 */
@GetMapping("/postOrder/payment/postForObject")
public JsonResult postForObject(String serial){
    /**
     * 使用 restTemplate 访问 restful post 接口：
     *      url , request, responseType, uriVariables) 这四个参数分别代表：
     *      请求地址、请求参数（放到请求体中）、HTTP 响应转换被转换成的对象类型、url占位参数
     */
    return JsonResult.success(restTemplate.postForObject(PAYMENT_SRV_URL + "/test/postTest", serial, HashMap.class));
}
```
```json
{
    "msg": "ok",
    "data": {
        "msg": "ok",
        "code": 200,
        "data": 1,
        "服务端口为：": "8002"
    },
    "code": 200
}
```

2. `postForEntity`：与 `postForEntity` 类似，返回对象为 ResponseEntity 对象，包含了响应中的一些详细的重要信息，比如响应头、响应状态码、响应体等
```java
/**
 * 客户端用浏览器是 get 请求，但是底层实质发送 post 调用服务端8001
 */
@GetMapping("/postOrder/payment/postForEntity")
public JsonResult postForEntity(String serial){
    /**
     * 使用 restTemplate 访问 restful post 接口：
     *      url , request, responseType, uriVariables) 这四个参数分别代表：
     *      请求地址、请求参数（放到请求体中）、HTTP 响应转换被转换成的对象类型、url占位参数
     */
    return JsonResult.success(restTemplate.postForEntity(PAYMENT_SRV_URL + "/test/postTest", serial, HashMap.class));
}
```
```json
{
    "msg": "ok",
    "data": {
        "headers": {
            "Content-Type": [
                "application/json"
            ],
            "Transfer-Encoding": [
                "chunked"
            ],
            "Date": [
                "Wed, 22 Feb 2023 07:21:07 GMT"
            ],
            "Keep-Alive": [
                "timeout=60"
            ],
            "Connection": [
                "keep-alive"
            ]
        },
        "body": {
            "msg": "ok",
            "code": 200,
            "data": 1,
            "服务端口为：": "8001"
        },
        "statusCodeValue": 200,
        "statusCode": "OK"
    },
    "code": 200
}
```
### ③、Ribbon 核心组件 IRule
> IRule：根据特定算法中从服务列表中选取一个要访问的服务

#### Ⅰ、IRule 具体算法

1. `com.netflix.loadbalancer.RoundRobinRule`：轮询
2. `com.netflix.loadbalancer.RandomRule`：随机
3. `com.netflix.loadbalancer.RetryRule`：先按照 RoundRobinRule 的策略获取服务，如果获取服务失败则在指定时间内会进行重试，获取可用的服务
4. `WeightedResponseTimeRule`：对 RoundRobinRule 的扩展，响应速度越快的实例选择权重越大，越容易被选择
5. `BestAvailableRule`：会先过滤掉由于多次访问故障而处于断路器跳闸状态的服务，然后选择一个并发量最小的服务
6. `AvailabilityFilteringRule`：先过滤掉故障实例，再选择并发较小的实例
7. `ZoneAvoidanceRule`：默认规则，复合判断 server 所在区域的性能和 server 的可用性选择服务器
#### Ⅱ、如何替换算法
> 修改 cloud-consumer-order80

##### （1）、注意配置细节
官方文档明确给出了警告：这个自定义配置类不能放在 `@ComponentScan` 所扫描的当前包下以及子包下，否则我们自定义的这个配置类就会被所有的 Ribbon 客户端所共享，达不到特殊化定制的目的了。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677052349663-6d04c33d-705e-4c22-ae83-235508688a0b.png#averageHue=%23e9c991&clientId=u1b4568ff-b543-4&from=paste&height=548&id=zjDVU&name=image.png&originHeight=548&originWidth=910&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66774&status=done&style=stroke&taskId=u3b3398fb-605f-4c59-b0df-f1208d7861f&title=&width=910)
##### （2）、创建新包与配置类

1. 创建新包与配置类

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677052606060-679418c5-944f-413d-bc5e-ed0208853fb7.png#averageHue=%233a4044&clientId=u1b4568ff-b543-4&from=paste&height=299&id=sdHVI&name=image.png&originHeight=299&originWidth=276&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11721&status=done&style=stroke&taskId=ub78a4c5b-2a8c-4f28-84eb-818afb4ee46&title=&width=276)

2. 编写配置类
```java
package com.rule;

import com.netflix.loadbalancer.IRule;
import com.netflix.loadbalancer.RandomRule;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author 月海
 * @create 2023/2/22 15:54
 *
 * 修改 IRule 算法
 */
@Configuration
public class MySelfRule {
    @Bean
    public IRule myRule(){
        // 定义为使用随机算法
        return new RandomRule();
    }
}

```

3. 主启动类添加 `@RibbonClient`
```java
package com.yuehai;

import com.rule.MySelfRule;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.cloud.netflix.ribbon.RibbonClient;

/**
 * 微服务消费者订单模块 cloud-consumer-order80
 * @author 月海
 * @create ${DATE} ${TIME}
 *
 * @EnableEurekaClient：作为微服务的服务提供者
 * @RibbonClient：修改 IRule 算法；参数 1：指定要修改的服务提供者，参数 2：指定修改配置类
 */
@SpringBootApplication
@EnableEurekaClient
@RibbonClient(name = "cloud-payment-service", configuration = MySelfRule.class)
public class ConsumerOrder80 {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerOrder80.class, args);
    }

}
```

4. 启动 7001、80、8001、8002

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1677053176031-a863ba42-1929-48de-85a3-454021b3586b.png#averageHue=%233a4146&clientId=u1b4568ff-b543-4&from=paste&height=201&id=LJOx1&name=image.png&originHeight=201&originWidth=271&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13013&status=done&style=stroke&taskId=u5399a636-028e-49b9-92cf-336a9577aec&title=&width=271)

5. 测试，发现  8001 和 8002 是随机出现，不再是交替出现
### ④、Ribbon 负载均衡算法原理

1. 轮询负载均衡算法：rest 接口第几次请求数 % 服务器集群总数量 = 实际调用服务器位置下标，每次服务重启动后 rest 接口计数从 1 开始。
```java
// 获取全部的集群服务
List<ServiceInstance> instances = discoveryClient.getInstances("CLOUD-PAYMENT-SERVICE");

// 如：
List [0] instances = 127.0.0.1:8002
List [1] instances = 127.0.0.1:8001
```

2. 8001+ 8002 组合成为集群，它们共计 2 台机器，集群总数为 2， 按照轮询算法原理：
   1. 当总请求数为 1 时： 1 % 2 =1 对应下标位置为1 ，则获得服务地址为 127.0.0.1:8001
   2. 当总请求数位 2 时： 2 % 2 =0 对应下标位置为0 ，则获得服务地址为 127.0.0.1:8002
   3. 当总请求数位 3 时： 3 % 2 =1 对应下标位置为1 ，则获得服务地址为 127.0.0.1:8001
   4. 当总请求数位 4 时： 4 % 2 =0 对应下标位置为0 ，则获得服务地址为 127.0.0.1:8002
   5. 如此类推......
# 五、服务接口调用 OpenFeign
## 1、OpenFeign
### ①、简介
#### Ⅰ、OpenFeign 是什么
> 官网解释：[https://cloud.spring.io/spring-cloud-static/Hoxton.SR1/reference/htmlsingle/#spring-cloud-openfeign](https://cloud.spring.io/spring-cloud-static/Hoxton.SR1/reference/htmlsingle/#spring-cloud-openfeign)
> GitHub：[https://github.com/spring-cloud/spring-cloud-openfeign](https://github.com/spring-cloud/spring-cloud-openfeign)

1. Feign 是一个声明式 WebService 客户端。使用 Feign 能让编写 Web Service 客户端更加简单。
2. 它的使用方法是定义一个服务接口然后在上面添加注解。
3. Feign 也支持可拔插式的编码器和解码器。Spring Cloud 对 Feign 进行了封装，使其支持了 Spring MVC 标准注解和 HttpMessageConverters。
4. Feign 可以与 Eureka 和 Ribbon 组合使用以支持负载均衡
#### Ⅱ、能干嘛

1.  Feign 旨在使编写 Java Http 客户端变得更容易。
2. 前面在使用 Ribbon + RestTemplate 时，利用 RestTemplate 对 http 请求的封装处理，形成了一套模版化的调用方法。
3. 但是在实际开发中，由于对服务依赖的调用可能不止一处，往往一个接口会被多处调用，所以通常都会针对每个微服务自行封装一些客户端类来包装这些依赖服务的调用。所以，Feign 在此基础上做了进一步封装，由他来帮助我们定义和实现依赖服务接口的定义。
4. 在 Feign 的实现下，我们只需创建一个接口并使用注解的方式来配置它(以前是 Dao 接口上面标注 Mapper 注解，现在是一个微服务接口上面标注一个 Feign 注解即可)，即可完成对服务提供方的接口绑定，简化了使用 Spring cloud Ribbon 时，自动封装服务调用客户端的开发量。
5. Feign 集成了 Ribbon：利用 Ribbon 维护了 Payment 的服务列表信息，并且通过轮询实现了客户端的负载均衡。而与 Ribbon 不同的是，通过 feign 只需要定义服务绑定接口且以声明式的方法，优雅而简单的实现了服务调用
#### Ⅲ、Feign 和 OpenFeign 两者区别
| **Feign** | **OpenFeign** |
| --- | --- |
| Feign 是 Spring Cloud 组件中的一个轻量级 RESTful 的 HTTP 服务客户端
Feign内置了Ribbon，用来做客户端负载均衡，去调用服务注册中心的服务。Feign的使用方式是：使用Feign的注解定义接口，调用这个接口，就可以调用服务注册中心的服务 | OpenFeign是Spring Cloud 在Feign的基础上支持了SpringMVC的注解，如@RequesMapping等等。OpenFeign的@FeignClient可以解析SpringMVC的@RequestMapping注解下的接口，并通过动态代理的方式产生实现类，实现类中做负载均衡并调用其他服务。 |
| ```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-feign</artifactId>
</dependency>
```
 | ```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
 |

#### Ⅳ、
## 2、
## 3、
## 4、
## 5、
## 6、
# 六、服务降级断路器 Hystrix
# 七、路由网关 zuul、Gateway
# 八、配置中心 Config
# 九、消息总线 Bus
# 十、消息驱动 Stream
# 十一、分布式请求链路跟踪 Sleuth
# 十二、SpringCloud Alibaba 入门简介
# 十三、Nacos 服务注册和配置中心
# 十四、Sentinel 实现熔断与限流
# 十五、Seata 处理分布式事务

1. 新建模块 cloud-provider-payment8004
2. 修改 pom.xml
3. 修改 yml 配置文件
4. 修改主启动类
5. 编写业务类 controller
6. 

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
