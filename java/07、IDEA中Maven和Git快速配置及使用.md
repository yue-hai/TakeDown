# 一、安装 Maven 核心程序

1. 下载地址：http://maven.apache.org/
2. 检查 JAVA_HOME 环境变量。Maven 是使用 Java 开发的，所以必须知道当前系统环境中 JDK 的安装目录。
3. 解压 Maven 的核心程序。将 apache-maven-3.6.3-bin.zip 解压到一个非中文无空格的目录下。
4. 配置环境变量。

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/03、配置环境变量1.png)

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/04、配置环境变量2.png)

5. 查看 Maven 版本信息验证安装是否正确
```java
    C:\Users\ccj77>mvn -v
    Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
    Maven home: D:\Java\apache-maven\apache-maven-3.6.3\bin\..
    Java version: 1.8.0_202, vendor: Oracle Corporation, runtime: D:\Java\Java8\JDK\jre
    Default locale: zh_CN, platform encoding: GBK
    OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"

    C:\Users\ccj77>
```

# 二、配置本地仓库和阿里云镜像

## 1、配置本地仓库

1. Maven 的核心程序并不包含具体功能，仅负责宏观调度。具体功能由插件来完成。Maven 核心程序会到本地仓库中查找插件。如果本地仓库中没有就会从远程中央仓库下载。此时如果不能上网则无法执行 Maven 的具体功能。为了解决这个问题，我们可以将 Maven 的本地仓库指向一个在联网情况下下载好的目录。
2. Maven 默认的本地仓库：~\.m2\repository 目录。
   - Tips：~表示当前用户的家目录。
3. 找到 Maven 的核心配置文件 settings.xml 文件：

```java
    D:\Java\apache-maven\apache-maven-3.6.3\conf\settings.xml
```

4. 设置方式

```xml
    <!-- localRepository
    | The path to the local repository maven will use to store artifacts.
    |
    | Default: ${user.home}/.m2/repository
    <localRepository>/path/to/local/repo</localRepository>
    -->
	<localRepository>D:\Java\apache-maven\localRepository</localRepository>
```

## 2、配置阿里云镜像

- 为了下载 jar 包方便，在 Maven 的核心配置文件 settings.xml 文件的< mirrors >< /mirrors >标签里面配置以下标签：

```xml
    <mirrors>
        <!-- mirror
        | Specifies a repository mirror site to use instead of a given repository. The repository that
        | this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are used
        | for inheritance and direct lookup purposes, and must be unique across the set of mirrors.
        |
        <mirror>
        <id>mirrorId</id>
        <mirrorOf>repositoryId</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://my.repository.com/repo/path</url>
        </mirror>
        -->
        <mirror>
            <id>nexus-aliyun</id>
            <mirrorOf>central</mirrorOf>
            <name>Nexus aliyun</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        </mirror>
    </mirrors>
```

# 三、在 Idea 中配置 Maven

## 1、配置自带的 Maven 插件

1. Idea 自带的 Maven 在 Idea 的安装目录的 plugins 目录中

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/02、Idea自带的Maven在Idea的安装目录的plugins目录中.png)

2. 在自带的 Maven 里配置了本地仓库之后，打开 Idea 配置为我们自己配置的 Maven

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/05、配置我们自己安装的Maven.png)

3. 设置 Maven 自动导包

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/06、设置Maven自动导包.png)

# 四、在 Idea 中创建 Maven 项目
1. 创建 Java 工程

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/07、创建Java工程.png)

2. 点击 Next，配置要继承的模块（如果直接创建的是 Project 不存在这一项）、坐标（GAV）、路径。不同的 Idea 版本可能有所差别，我使用的是 2019.3.3的版本

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/08、创建Java工程2.png)

3. 点击 Finish 即可创建成功
4. 配置 Maven 的核心配置文件 pom.xml

```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>com.yuehai.maven</groupId>
        <artifactId>07_Maven和Git</artifactId>
        <version>1.0-SNAPSHOT</version>

        <dependencies>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.12</version>
                <scope>test</scope>
            </dependency>
        </dependencies>

    </project>
```

5. 点击右侧 Maven 查看依赖

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/09、配置Maven的核心配置文件pom.xml.png)

6. 使用 Maven 的方式运行 Maven 工程

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/10、使用Maven的方式运行Maven工程.png)

# 五、创建 Web 工程（了解）

1. 创建简单的 Maven 工程，打包方式为 war 包

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/11、创建简单的Maven工程.png)

```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>com.yuehai.mavenWeb</groupId>
        <artifactId>07_MavenWeb</artifactId>
        <version>1.0-SNAPSHOT</version>
        <!-- Web 工厂打包方式为 war -->
        <packaging>war</packaging>

    </project>
```

2. 点击 Project Structure

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/12、点击ProjectStructure.png)

3. 选择对应的 Module，设置 Web 目录

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/13、选择对应的Module设置Web目录.png)

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/14、选择对应的Module设置Web目录2.png)

4. 弹出提示框，选择版本后点击 OK

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/15、弹出提示框选择版本后点击OK.png)

5. 生成 web.xml 文件

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/16、生成web.xml文件.png)

6. 设置存放 web 页面文件的目录后点击 OK

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/17、设置存放页面的目录的位置和名称.png)

7. 发现项目中多了一个 web 目录，而且目录上有一个蓝点

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/18、发现项目中多了一个web目录而且目录上有一个蓝点.png)

8. 在 web 目录下创建 index.jsp 页面

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/19、在web目录下创建index.jsp页面.png)

9.  部署到 Tomcat 上运行

# 六、在 Idea 中导入 Maven 项目

1. 点击 Project Structure

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/20、点击ProjectStructure.png)

2. 点击 Modules→➕→Import Module

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/21、点击%20Modules→➕→Import%20Module.png)

3. 找到项目所在的位置

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/22、找到项目所在的位置.png)

4. 选择 Import module from external model（从外部模型导入模块）→Maven→Finish

![](https://openlist.yuehai.fun:63/d/TakeDown/java/attachments/23、选择%20Import%20module%20from%20external%20model（从外部模型导入模块）→Maven→Finish.png)



# 七、



# 八、



# 九、



# 十、



# 十一、



# 十二、



# 十三、



# 十四、



# 十五、



# 十六、



# 十七、



# 十八、



# 十九、



# 二十、
