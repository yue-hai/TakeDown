> [https://www.bilibili.com/video/BV1gr4y1U7CY](https://www.bilibili.com/video/BV1gr4y1U7CY)
> 
> [Docker2022.docx](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FDocker2022.docx)

# 一、Docker 简介

## 1、为什么会有 docker 出现

1. 假定您在开发一个尚硅谷的谷粒商城，您使用的是一台笔记本电脑而且您的开发环境具有特定的配置。其他开发人员身处的环境配置也各有不同。您正在开发的应用依赖于您当前的配置且还要依赖于某些配置文件。此外，您的企业还拥有标准化的测试和生产环境，且具有自身的配置和一系列支持文件。您希望尽可能多在本地模拟这些环境而不产生重新创建服务器环境的开销。请问？
2. 您要如何确保应用能够在这些环境中运行和通过质量检测？并且在部署过程中不出现令人头疼的版本、配置问题，也无需重新编写代码和进行故障修复？
3. 答案就是使用容器。Docker之所以发展如此迅速，也是因为它对此给出了一个标准化的解决方案-----系统平滑移植，容器虚拟化技术。
4. 环境配置相当麻烦，换一台机器，就要重来一次，费力费时。很多人想到，能不能从根本上解决问题，软件可以带环境安装？也就是说，安装的时候，把原始环境一模一样地复制过来。开发人员利用 Docker 可以消除协作编码时“在我的机器上可正常工作”的问题。

 ![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-54-941--qYVcwgsYMPP9_Q.png)

5. 之前在服务器配置一个应用的运行环境，要安装各种软件，就拿尚硅谷电商项目的环境来说，Java/RabbitMQ/MySQL/JDBC驱动包等。安装和配置这些东西有多麻烦就不说了，它还不能跨平台。假如我们是在 Windows 上安装的这些环境，到了 Linux 又得重新装。况且就算不跨操作系统，换另一台同样操作系统的服务器，要移植应用也是非常麻烦的。
6. 传统上认为，软件编码开发/测试结束后，所产出的成果即是程序或是能够编译执行的二进制字节码等(java为例)。而为了让这些程序可以顺利执行，开发团队也得准备完整的部署文件，让维运团队得以部署应用程式，开发需要清楚的告诉运维部署团队，用的全部配置文件+所有软件环境。不过，即便如此，仍然常常发生部署失败的状况。Docker的出现使得Docker得以打破过去「程序即应用」的观念。透过镜像(images)将作业系统核心除外，运作应用程式所需要的系统环境，由下而上打包，达到应用程式跨平台间的无缝接轨运作。

## 2、docker 理念

1. Docker 是基于 Go 语言实现的云开源项目。
2. Docker 的主要目标是“Build，Ship and Run Any App,Anywhere”，也就是通过对应用组件的封装、分发、部署、运行等生命周期的管理，使用户的APP（可以是一个WEB应用或数据库应用等等）及其运行环境能够做到“一次镜像，处处运行”。

 ![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-389--s7CFyZXxaQjCQg.png)

3. Linux容器技术的出现就解决了这样一个问题，而 Docker 就是在它的基础上发展过来的。将应用打成镜像，通过镜像成为运行在Docker容器上面的实例，而 Docker容器在任何操作系统上都是一致的，这就实现了跨平台、跨服务器。只需要一次配置好环境，换到别的机子上就可以一键部署好，大大简化了操作
4. 解决了运行环境和配置问题的软件容器， 方便做持续集成并有助于整体发布的容器虚拟化技术

## 3、容器与虚拟机比较

### ①、容器发展简史

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-411--bsLIxHzb5ApRLQ.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-430--S5PhAew7b5onLQ.png)

### ②、传统虚拟机技术

虚拟机（virtual machine）就是带环境安装的一种解决方案。
它可以在一种操作系统里面运行另一种操作系统，比如在Windows10系统里面运行Linux系统CentOS7。应用程序对此毫无感知，因为虚拟机看上去跟真实系统一模一样，而对于底层系统来说，虚拟机就是一个普通文件，不需要了就删掉，对其他部分毫无影响。这类虚拟机完美的运行了另一套系统，能够使应用程序，操作系统和硬件三者之间的逻辑不变。  

| Win10 | VMWare | Centos7 | 各种cpu、内存网络额配置+各种软件 | 虚拟机实例 |
| --- | --- | --- | --- | --- |

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-463--Hsss7NYFVVYV6Q.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-479--dZsQIIEg-erEHw.png)

- 虚拟机的缺点：
1. 资源占用多
2. 冗余步骤多
3. 启动慢

### ③、容器虚拟化技术

1. 由于前面虚拟机存在某些缺点，Linux 发展出了另一种虚拟化技术：
2. Linux 容器(Linux Containers，缩写为 LXC)
3. Linux 容器是与系统其他部分隔离开的一系列进程，从另一个镜像运行，并由该镜像提供支持进程所需的全部文件。容器提供的镜像包含了应用的所有依赖项，因而在从开发到测试再到生产的整个过程中，它都具有可移植性和一致性。
4. Linux 容器不是模拟一个完整的操作系统而是对进程进行隔离。有了容器，就可以将软件运行所需的所有资源打包到一个隔离的容器中。容器与虚拟机不同，不需要捆绑一整套操作系统，只需要软件工作所需的库资源和设置。系统因此而变得高效轻量并保证部署在任何环境中的软件都能始终如一地运行。

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-497--ClK2kw-a-jp2YQ.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-513--8OqIPPXTIE8Uow.png)

### ④、对比

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-524--EPKoEEksVp_Y9A.png)

- 比较了 Docker 和传统虚拟化方式的不同之处：
1. 传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；
2. 容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。
3. 每个容器之间互相隔离，每个容器有自己的文件系统 ，容器之间进程不会相互影响，能区分计算资源。

## 4、能干嘛

1. 技术职级变化
   1. coder
   2. programmer
   3. software engineer
   4. DevOps engineer
2. 开发/运维（DevOps）新一代开发工程师
   1. 一次构建、随处运行
   2. 更快速的应用交付和部署：传统的应用开发完成后，需要提供一堆安装程序和配置说明文档，安装部署后需根据配置文档进行繁杂的配置才能正常运行。Docker化之后只需要交付少量容器镜像文件，在正式生产环境加载镜像并运行即可，应用安装配置在镜像里已经内置好，大大节省部署配置和测试验证时间。
   3. 更便捷的升级和扩缩容：随着微服务架构和Docker的发展，大量的应用会通过微服务方式架构，应用的开发构建将变成搭乐高积木一样，每个Docker容器将变成一块“积木”，应用的升级将变得非常容易。当现有的容器不足以支撑业务处理时，可通过镜像运行新的容器进行快速扩容，使应用系统的扩容从原先的天级变成分钟级甚至秒级
   4. 更简单的系统运维：应用容器化运行后，生产环境运行的应用可与开发、测试环境的应用高度一致，容器会将应用程序相关的环境和状态完全封装起来，不会因为底层基础架构和操作系统的不一致性给应用带来影响，产生新的BUG。当出现程序异常时，也可以通过测试环境的相同容器进行快速定位和修复。
   5. 更高效的计算资源利用：Docker是内核级虚拟化，其不像传统的虚拟化技术一样需要额外的Hypervisor支持，所以在一台物理机上可以运行很多个容器实例，可大大提升物理服务器的CPU和内存的利用率。
   6. Docker 应用场景：

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-540--0AhOQVwDqBZeIw.png)

3. 哪些企业在使用
   1. 新浪

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-564--_kZs9aGMRUT9Wg.png)

   2. 美团

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-586--eDNctxftQXFPLA.png)

   3. 蘑菇街

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-629--UWP0Uvw_rLWBcQ.png)

   4. ...

## 5、去哪下

1. 官网：docker官网：[http://www.docker.com](http://www.docker.com)
2. 仓库：Docker Hub官网: [https://hub.docker.com/](https://hub.docker.com/)

# 二、Docker 安装

1. 官网：docker官网：[http://www.docker.com](http://www.docker.com)
2. 仓库：Docker Hub官网: [https://hub.docker.com/](https://hub.docker.com/)

## 1、前提说明

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-666--70VVdU_QzRKrAQ.png)

### ①、前提条件

1. 目前，CentOS 仅发行版本中的内核支持 Docker。Docker 运行在CentOS 7 (64-bit)上，
2. 要求系统为64位、Linux系统内核版本为 3.8以上，这里选用 Centos7.x

### ②、查看自己的内核

`uname` 命令用于打印当前系统相关信息（内核版本号、硬件架构、主机名称和操作系统类型等）。

```shell
docker@VM-8-15-ubuntu:~$ cat /proc/version
Linux version 5.4.0-126-generic (buildd@lcy02-amd64-072) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #142-Ubuntu SMP Fri Aug 26 12:12:57 UTC 2022
docker@VM-8-15-ubuntu:~$ uname -r
5.4.0-126-generic
docker@VM-8-15-ubuntu:~$ 
```

## 2、Docker 的基本组成

### ①、镜像(image)

1. Docker 镜像（Image）就是一个只读的模板。镜像可以用来创建 Docker 容器，一个镜像可以创建很多容器。
2. 它也相当于是一个 root 文件系统。比如官方镜像 centos:7 就包含了完整的一套 centos:7 最小系统的 root 文件系统。
3. 相当于容器的“源代码”，docker 镜像文件类似于 Java 的类模板，而 docker 容器实例类似于 java 中 new 出来的实例对象。

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-679--HGw7pQCFgfnoJg.png)

### ②、容器(container)

#### Ⅰ、从面向对象角度

1. Docker 利用容器（Container）独立运行的一个或一组应用，应用程序或服务运行在容器里面，容器就类似于一个虚拟化的运行环境，容器是用镜像创建的运行实例。
2. 就像是 Java 中的类和实例对象一样，镜像是静态的定义，容器是镜像运行时的实体。
3. 容器为镜像提供了一个标准的和隔离的运行环境，它可以被启动、开始、停止、删除。每个容器都是相互隔离的、保证安全的平台

#### Ⅱ、从镜像容器角度

可以把容器看做是一个简易版的 Linux 环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。

### ③、仓库(repository)

1. 仓库（Repository）是集中存放镜像文件的场所。
2. 类似于：
   1. Maven仓库，存放各种jar包的地方；
   2. github仓库，存放各种git项目的地方；
   3. Docker公司提供的官方registry被称为Docker Hub，存放各种镜像模板的地方。
3. 仓库分为公开仓库（Public）和私有仓库（Private）两种形式。
4. 最大的公开仓库是 Docker Hub([https://hub.docker.com/)](https://hub.docker.com/))，
5. 存放了数量庞大的镜像供用户下载。国内的公开仓库包括阿里云 、网易云等

### ④、小总结

1. 需要正确的理解仓库/镜像/容器这几个概念:
   1. Docker 本身是一个容器运行载体或称之为管理引擎。我们把应用程序和配置依赖打包好形成一个可交付的运行环境，这个打包好的运行环境就是image镜像文件。只有通过这个镜像文件才能生成Docker容器实例(类似Java中new出来一个对象)。
   2. image文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。
2. 镜像文件：image 文件生成的容器实例，本身也是一个文件，称为镜像文件。
3. 容器实例：一个容器运行一种服务，当我们需要的时候，就可以通过docker客户端创建一个对应的运行实例，也就是我们的容器
4. 仓库：就是放一堆镜像的地方，我们可以把镜像发布到仓库中，需要的时候再从仓库中拉下来就可以了。

## 3、Docker平台架构图解(架构版)

- Docker 是一个 C/S 模式的架构，后端是一个松耦合架构，众多模块各司其职

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-690--jq5nZSsGTuTidw.png)

![image.png|693](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-703--XL7HGwI9oVMkAw.png)

## 4、Ubuntu Docker 安装步骤

> Ubuntu Docker 安装：[https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository](https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository)
  
1. 添加 Docker 的官方 GPG 密钥：
 
```shell
# 更新软件包索引
sudo apt-get update

# 安装必要的软件包
sudo apt-get install ca-certificates curl
# 创建一个名为 /etc/apt/keyrings 的目录，用于存放 Docker 的 GPG 密钥
sudo install -m 0755 -d /etc/apt/keyrings
# 使用 curl 从 Docker 官方站点下载 GPG 密钥文件，并将其保存到 /etc/apt/keyrings/docker.asc
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# 修改 GPG 密钥文件的权限，确保所有用户都可以读取这个文件
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

2. 将 Docker 存储库添加到系统的 APT 源列表中：

```shell
# 将 Docker 存储库添加到系统的 APT 源列表中
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 再次更新软件包索引
sudo apt-get update
```

3. 安装最新版本：

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. 通过运行 hello-world 镜像来验证 Docker Engine 安装是否成功：

```shell
sudo docker run hello-world
```

4. 一旦安装完成，Docker 服务将会自动启动。可以输入下面的命令，验证它：

```shell
sudo systemctl status docker
```

5. 输出将会类似下面这样：

```shell
root@yuehai:~# sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-11-07 12:59:04 CST; 3min 23s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 43894 (dockerd)
      Tasks: 9
     Memory: 36.9M
        CPU: 381ms
     CGroup: /system.slice/docker.service
             └─43894 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.495521002+08:00" level=info msg="Loading conta>
Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.516508229+08:00" level=warning msg="WARNING: b>
Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.516535567+08:00" level=warning msg="WARNING: b>
Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.516557451+08:00" level=info msg="Docker daemon>
Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.516676131+08:00" level=info msg="Daemon has co>
Nov 07 12:59:04 yuehai dockerd[43894]: time="2024-11-07T12:59:04.562565302+08:00" level=info msg="API listen on>
Nov 07 12:59:04 yuehai systemd[1]: Started Docker Application Container Engine.
Nov 07 12:59:28 yuehai dockerd[43894]: time="2024-11-07T12:59:28.689764563+08:00" level=warning msg="Error gett>
Nov 07 12:59:28 yuehai dockerd[43894]: time="2024-11-07T12:59:28.689834866+08:00" level=info msg="Attempting ne>
Nov 07 12:59:28 yuehai dockerd[43894]: time="2024-11-07T12:59:28.694079980+08:00" level=error msg="Handler for >
lines 1-22/22 (END)
```

6. 当一个新的 Docker 发布时，可以使用标准的 `sudo apt update && sudo apt upgrade` 流程来升级 Docker 软件包
7. 如果想阻止 Docker 自动更新，锁住它的版本：`sudo apt-mark hold docker-ce`

## 5、将用户添加到 docker 组

1. 创建 docker 用户，回车后数据密码，之后一直回车：

```shell
# 创建 docker 用户
adduser docker

# 如果提示 docker 组已经存在，使用 --ingroup 参数：创建一个新用户，不自动创建与用户名同名的用户组
sudo adduser --ingroup docker docker
```

2. 如果非 root 用户要使用 docker（比如 `docker` 用户），则应考虑使用类似以下方式将用户添加到 docker 组：`sudo usermod -aG docker 用户名`

```shell
sudo usermod -aG docker docker
```

3. 查看 docker：`docker version`
4. 启动 docker：`systemctl start docker`
5. 关闭 docker：`systemctl stop docker`
6. 测试：`docker run hello-world`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-756--5mlEv7rc6mEhoA.png)

7. 输出这段提示以后，hello world就会停止运行，容器自动终止
8. run 干了什么

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-767--5c9JEykQ9y4Dmg.png)

## 6、阿里云镜像加速

- 需注册账号
- [https://cr.console.aliyun.com/](https://cr.console.aliyun.com/)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-780--37QMi-ZlHNr9MA.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-798--xzE-ij_j-Me2sA.png)

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://0pnwnafi.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## 7、底层原理

- 为什么 docker 会比 VM 虚拟机快
1. docker 有着比虚拟机更少的抽象层：由于 docker 不需要 Hypervisor(虚拟机) 实现硬件资源虚拟化，运行在 docker 容器上的程序直接使用的都是实际物理机的硬件资源。因此在CPU、内存利用率上 docker 将会在效率上有明显优势。
2. docker 利用的是宿主机的内核，而不需要加载操作系统 OS 内核：当新建一个容器时，docker 不需要和虚拟机一样重新加载一个操作系统内核。进而避免引寻、加载操作系统内核返回等比较费时费资源的过程，当新建一个虚拟机时，虚拟机软件需要加载 OS，返回新建过程是分钟级别的。而 docker 由于直接利用宿主机的操作系统,则省略了返回过程，因此新建一个 docker 容器只需要几秒钟

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-810--WNpRlVNfCGLZ6w.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-835--yh1rhpFp5_8qpw.png)

# 三、Docker 常用命令

## 1、帮助启动类命令

1. 启动 docker： `systemctl start docker`
2. 停止 docker： `systemctl stop docker`
3. 重启 docker： `systemctl restart docker`
4. 查看 docker 状态： `systemctl status docker`
5. 开机启动： `systemctl enable docker`
6. 查看 docker 概要信息： `docker info`
7. 查看 docker 总体帮助文档：`docker --help`
8. 登录：`docker login -u 用户名 -p 密码`
9. 退出登录：`docker logout`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-858--ma7h6aaKYv2BKQ.png)

## 2、镜像命令

### ①、`docker images [参数]` 列出本地主机上的镜像

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-867--R_t0L0LkyJnSjw.png)

- 各个选项说明：
  
| 参数 | 说明 |
| --- | --- |
| REPOSITORY | 表示镜像的仓库源；同一仓库源可以有多个 TAG 版本，代表这个仓库源的不同个版本，我们使用 `REPOSITORY:TAG` 来定义不同的镜像。 |
| TAG | 镜像的标签版本号；如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker 将默认使用 `ubuntu:latest` 镜像 |
| IMAGE ID | 镜像ID |
| CREATED | 镜像创建时间 |
| SIZE | 镜像大小 |

- 参数说明：
1. `-a`：列出本地所有的镜像（含历史映像层）
2. `-q`：只显示镜像 ID。

### ②、`docker search [参数] 镜像名/ID` 搜索镜像

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-912--7m6f0y1Br0n4HA.png)

- 各个选项说明：
  
| 参数 | 说明 |
| --- | --- |
| NAME | 镜像名称 |
| DESCRIPTION | 镜像说明 |
| STARS | 点赞数量 |
| OFFICIAL | 是否是官方的 |
| AUTOMATED | 是否是自动构建的 |

- 参数说明：
1. `--limit` : 只列出 N 个镜像，默认 25 个

### ③、`docker pull 镜像名/ID` 下载镜像

- 下载时可以加版本号也可以不加版本号，添加版本号时没有该版本则会下载失败，不添加版本号时默认下载最新版

1. `docker pull 镜像名字[:TAG]`
2. `docker pull 镜像名字` 等价于：`docker pull 镜像名字:latest`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
supermanito/helloworld   latest    d0d4aeb91dbf   13 months ago   181MB
hello-world              latest    feb5d9fea6a5   16 months ago   13.3kB
docker@VM-8-15-ubuntu:~$ docker search vue3
NAME                                 DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
webdevomandam/vue3-vite              Vue3 TS + Vite                                  1                    
lvxiaocong/vue3-learning                                                             0                    
minchao/vue3-realworld-example-app                                                   0                    
efabrica/vue3                                                                        0                    
vincenthe1981/vue3                   nodejs vue3 cli                                 0                    
chaojian/vue3-elem                                                                   0                    
stanfoot/vue3-dev                                                                    0                    
wrapit/vue3cli_demo                  A running vue3 cli web application  , with a…   0                    
lostimever/vue3-ts                                                                   0                    
cloudhack/vue3-template                                                              0                    
codemunha/vue3-ts                                                                    0                    
venkatasaikatepalli/vue3saibase                                                      0                    
qq809481244/vue3doc                  vue3 doc in chinese                             0                    
demonzhangzhe/vue3                                                                   0                    
jcloudyu/vue3-node14                 A tiny image based on node14 that is used to…   0                    
spiderxman/vue30old                                                                  0                    
buqiyuan/vue3-antd-admin                                                             0                    
xh2958915385/vue3                                                                    0                    
amberish/vue3-app                                                                    0                    
imqdcn/vue3projectdocker             vue3+vite项目的镜像                                  0                    
monikacy/vue3                                                                        0                    
singhang/vue3-cli                                                                    0                    
wmt1030/vue3-admin                   vue3 + ts + naiveui 后台管理系统                      0                    
renato1958/vue3-nginx                                                                0                    
kjhun/vue3-vite-quasar                                                               0                    
docker@VM-8-15-ubuntu:~$ docker pull webdevomandam/vue3-vite
Using default tag: latest
latest: Pulling from webdevomandam/vue3-vite
4e9f2cdf4387: Retrying in 1 second 
6cac039d45af: Download complete 
7bbb5e46b36d: Retrying in 12 seconds 
39f6d17c9d38: Retrying in 1 second 
a5f9fd374d3b: Waiting 
7d84628ff318: Waiting 
408d5eeebbf1: Waiting 
latest: Pulling from webdevomandam/vue3-vite
4e9f2cdf4387: Pull complete 
6cac039d45af: Pull complete 
7bbb5e46b36d: Pull complete 
39f6d17c9d38: Pull complete 
a5f9fd374d3b: Pull complete 
7d84628ff318: Pull complete 
408d5eeebbf1: Pull complete 
Digest: sha256:95efce6e01c140369ead56dca3aae22cb12375183484ce4c16d7b0eefbb31bab
Status: Downloaded newer image for webdevomandam/vue3-vite:latest
docker.io/webdevomandam/vue3-vite:latest
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
supermanito/helloworld    latest    d0d4aeb91dbf   13 months ago   181MB
hello-world               latest    feb5d9fea6a5   16 months ago   13.3kB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB
docker@VM-8-15-ubuntu:~$ 
```

### ④、`docker rmi [参数] 镜像名/ID` 删除镜像

1. 删除单个：`docker rmi -f 镜像ID`
2. 删除多个：`docker rmi -f 镜像名1:TAG 镜像名2:TAG`
3. 删除全部：`docker rmi -f $(docker images -qa)`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-922--66ubiBCmUmGB9Q.png)

- 参数说明：`-f`：强制删除；若镜像已被使用则不可以被删除，使用此参数可以强制删除

### ⑤、`docker system df`  查看镜像/容器/数据卷所占的空间

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-930--BK1ZufKAf6AZGw.png)

## 3、容器命令

- 有镜像才能创建容器， 这是根本前提(下载一个 CentOS 或者 ubuntu 镜像演示)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-935--kaS2B-Jndd3jdA.png)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-944--Ne9wsP8sB48giw.png)

### ①、新建并启动容器 `docker run [参数] 镜像名` 

1. 以命令行模式进入容器：`docker run [-itd] [--name] [为容器指定一个名称] 镜像名 [/bin/bash]`，不指定则会随机分配一个名称
2. 为容器指定端口：`docker run -itd -p 3000:80 webdevomandam/vue3-vite`，启动后通过 `[http://服务器IP:3000/](http://43.138.106.181:7777/)` 即可访问
3. 要加参数 `-it`，直接 run 的话，里面没有端口或进程，docker 会认为他死掉了，自动 stop

- 参数说明：

| 参数 | 说明 |
| --- | --- |
| `--name` | 为容器指定一个名称 |
| `-d` | 后台运行容器并返回容器ID，也即启动守护式容器(后台运行) |
| `-i` | 以交互模式运行容器，通常与 -t 同时使用 |
| `-t` | 为容器重新分配一个伪输入终端，通常与 -i 同时使用；也即启动交互式容器(前台有伪终端，等待交互) |
| `-P` | 随机端口映射 |
| `-p` | 指定端口映射；可指定多组 |
| `/bin/bash`或`bash` | 放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash |

1. 创建时直接进入容器：`docker run -it ubuntu /bin/bash`
2. 后台创建容器：`docker run -itd ubuntu /bin/bash`，后返回 id
   1. 列出当前所有正在运行的容器：`docker ps`，查看 id
   2. 进入创建的容器：`docker exec -it 容器id /bin/bash`

### ②、退出容器

1. 指令：`exit`，会退出容器并停止容器
2. 组合键：`ctrl + p + q`，只会退出容器，不会停止容器
3. 组合键：`ctrl + a 然后 ctrl + d`，和上面的好像一样

### ③、列出当前所有正在运行的容器 `docker ps [参数]` 

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-957--b3atknSGYJq_Pw.png)

- 参数 OPTIONS 说明：

| 参数 | 说明 |
| --- | --- |
| `-a` | 列出当前所有正在运行的容器 + 已停止的 |
| `-l ` | 显示最近创建的容器 |
| `-n` | 显示最近n个创建的容器 |
| `-q` | 静默模式，只显示容器编号 |

### ④、进入容器

1. `docker attach 容器id`：attach 是直接进入容器启动命令的终端，如果使用 `exit` 从这个容器退出，会导致容器的停止
2. `docker exec -it 容器id bash`：exec 是在容器中打开新的终端，使用 `exit` 不会导致容器的停止，推荐使用这个命令

### ⑤、启动/重启/停止容器

1. 启动：`docker start 容器ID或容器名`
2. 重启：`docker restart 容器ID或者容器名`
3. 停止：`docker stop 容器ID或者容器名`
4. 强制停止：`docker kill 容器ID或容器名`

### ⑥、删除已停止的容器

1. 删除一个：`docker rm 容器ID`
2. 一次性删除多个容器实例
   1. `docker rm -f $(docker ps -a -q)`
   2. `docker ps -a -q | xargs docker rm`

### ⑦、查看容器日志 `docker logs 容器ID`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-964--O1fWiVcKyCkJRg.png)

### ⑧、查看容器内运行的进程 `docker top 容器ID`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-975--tdPfDXkhj8Suew.png)

### ⑨、查看容器内部细节 `docker inspect 容器ID`

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
68d7ed83bc37   webdevomandam/vue3-vite   "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:3000->80/tcp, :::3000->80/tcp   quizzical_jennings
docker@VM-8-15-ubuntu:~$ docker inspect 68d7ed83bc37
[
    {
        "Id": "68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6",
        "Created": "2023-01-30T00:24:52.111957691Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 25555,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-30T00:24:52.532413337Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:6704ecc7efed64b6cd5679a9d34cc65307c9357aa31e80de6434e958da0530a9",
        "ResolvConfPath": "/var/lib/docker/containers/68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6/hostname",
        "HostsPath": "/var/lib/docker/containers/68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6/hosts",
        "LogPath": "/var/lib/docker/containers/68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6/68d7ed83bc37cd4858c9f5cdf12cab400de075f94c61aab07b607c1bebd97bd6-json.log",
        "Name": "/quizzical_jennings",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "3000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e6657029fdf696468c2fc0829ae78bfbb3b85789c0bf8bb3a30e587694d5a2a6-init/diff:/var/lib/docker/overlay2/588a280e94a0e42bb1f225aa18eefea686c93d2ff1eb9c106ae1e3f1454a19bd/diff:/var/lib/docker/overlay2/9c74cac76f7ebbac69e94be2fb30585f4e2fa6adb2f4531659a0f80cd1375eb2/diff:/var/lib/docker/overlay2/cf80dde1fe35579ccf61e53702d3b2a80a03d27d8cc72f4a2390e84412fdb2b6/diff:/var/lib/docker/overlay2/273ac2840200049b9a6c4d6d9039b3c78d3ce3fdc8ebe2127a902b4d3fe7ddce/diff:/var/lib/docker/overlay2/c947ce9af741a912106aeaa796d218196825cc490877fdd55da39aebce8db19f/diff:/var/lib/docker/overlay2/31859cfebe5aba1c384ec25e6151dd47a0c102de332e07e91998bd97e9cc1576/diff:/var/lib/docker/overlay2/e65fae3030886e6dd70f3d142eb4b5103b64c8081681d09abee9801e0901028b/diff",
                "MergedDir": "/var/lib/docker/overlay2/e6657029fdf696468c2fc0829ae78bfbb3b85789c0bf8bb3a30e587694d5a2a6/merged",
                "UpperDir": "/var/lib/docker/overlay2/e6657029fdf696468c2fc0829ae78bfbb3b85789c0bf8bb3a30e587694d5a2a6/diff",
                "WorkDir": "/var/lib/docker/overlay2/e6657029fdf696468c2fc0829ae78bfbb3b85789c0bf8bb3a30e587694d5a2a6/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "68d7ed83bc37",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.20.1",
                "NJS_VERSION=0.5.3",
                "PKG_RELEASE=1"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "webdevomandam/vue3-vite",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "08440a99ee89ee3d63a5709825aa1dfed778a165253a790050a51314176c8d89",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "3000"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "3000"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/08440a99ee89",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "aa82565aaa36570ac98a04c52eb0f68875a2f1ba72949bb674ef94d3a30d6fd6",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "f250811a3aa73853f24f8fbaeb6913d25035c947140ee2fc077e7494d94abdc0",
                    "EndpointID": "aa82565aaa36570ac98a04c52eb0f68875a2f1ba72949bb674ef94d3a30d6fd6",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
docker@VM-8-15-ubuntu:~$ 
```

### ⑪、从容器内拷贝文件到主机上 `docker cp 容器ID:容器内路径 拷贝到的主机路径`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
hello-world               latest    feb5d9fea6a5   16 months ago   13.3kB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker run -it ubuntu bash

root@8f3c2446699c:/# ll
total 56
drwxr-xr-x   1 root root 4096 Jan 30 01:32 ./
drwxr-xr-x   1 root root 4096 Jan 30 01:32 ../
-rwxr-xr-x   1 root root    0 Jan 30 01:32 .dockerenv*
lrwxrwxrwx   1 root root    7 Oct  6  2021 bin -> usr/bin/
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot/
drwxr-xr-x   5 root root  360 Jan 30 01:32 dev/
drwxr-xr-x   1 root root 4096 Jan 30 01:32 etc/
drwxr-xr-x   2 root root 4096 Apr 15  2020 home/
lrwxrwxrwx   1 root root    7 Oct  6  2021 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root   10 Oct  6  2021 libx32 -> usr/libx32/
drwxr-xr-x   2 root root 4096 Oct  6  2021 media/
drwxr-xr-x   2 root root 4096 Oct  6  2021 mnt/
drwxr-xr-x   2 root root 4096 Oct  6  2021 opt/
dr-xr-xr-x 247 root root    0 Jan 30 01:32 proc/
drwx------   2 root root 4096 Oct  6  2021 root/
drwxr-xr-x   5 root root 4096 Oct  6  2021 run/
lrwxrwxrwx   1 root root    8 Oct  6  2021 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Oct  6  2021 srv/
dr-xr-xr-x  13 root root    0 Jan 30 01:32 sys/
drwxrwxrwt   2 root root 4096 Oct  6  2021 tmp/
drwxr-xr-x  13 root root 4096 Oct  6  2021 usr/
drwxr-xr-x  11 root root 4096 Oct  6  2021 var/

root@8f3c2446699c:/# echo yuehai > test.txt

root@8f3c2446699c:/# ll
total 60
drwxr-xr-x   1 root root 4096 Jan 30 01:33 ./
drwxr-xr-x   1 root root 4096 Jan 30 01:33 ../
-rwxr-xr-x   1 root root    0 Jan 30 01:32 .dockerenv*
lrwxrwxrwx   1 root root    7 Oct  6  2021 bin -> usr/bin/
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot/
drwxr-xr-x   5 root root  360 Jan 30 01:32 dev/
drwxr-xr-x   1 root root 4096 Jan 30 01:32 etc/
drwxr-xr-x   2 root root 4096 Apr 15  2020 home/
lrwxrwxrwx   1 root root    7 Oct  6  2021 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root   10 Oct  6  2021 libx32 -> usr/libx32/
drwxr-xr-x   2 root root 4096 Oct  6  2021 media/
drwxr-xr-x   2 root root 4096 Oct  6  2021 mnt/
drwxr-xr-x   2 root root 4096 Oct  6  2021 opt/
dr-xr-xr-x 230 root root    0 Jan 30 01:32 proc/
drwx------   2 root root 4096 Oct  6  2021 root/
drwxr-xr-x   5 root root 4096 Oct  6  2021 run/
lrwxrwxrwx   1 root root    8 Oct  6  2021 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Oct  6  2021 srv/
dr-xr-xr-x  13 root root    0 Jan 30 01:32 sys/
-rw-r--r--   1 root root    7 Jan 30 01:33 test.txt
drwxrwxrwt   2 root root 4096 Oct  6  2021 tmp/
drwxr-xr-x  13 root root 4096 Oct  6  2021 usr/
drwxr-xr-x  11 root root 4096 Oct  6  2021 var/

root@8f3c2446699c:/# cat test.txt
yuehai

root@8f3c2446699c:

docker@VM-8-15-ubuntu:~$ 

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8f3c2446699c   ubuntu                    "bash"                   2 minutes ago    Up 2 minutes                                            kind_neumann
281dfbee431f   webdevomandam/vue3-vite   "/docker-entrypoint.…"   37 minutes ago   Up 37 minutes   0.0.0.0:7777->80/tcp, :::7777->80/tcp   keen_elion

docker@VM-8-15-ubuntu:~$ docker cp 8f3c2446699c:/test.txt ~/export

docker@VM-8-15-ubuntu:~$ cat ~/export/test.txt
yuehai

docker@VM-8-15-ubuntu:~$ 
```

### ⑫、导入和导出容器

1. 导出：`docker export 容器ID > 导出的目录/文件名.tar`

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande
8f3c2446699c   ubuntu                    "bash"                   27 minutes ago       Up 27 minutes                                               kind_neumann

docker@VM-8-15-ubuntu:~$ docker export 7f369e1defc4 > ~/export/vue3-vite.tar

docker@VM-8-15-ubuntu:~$ ll ./export
total 23968
drwxr-xr-x 2 docker docker     4096 Jan 30 10:01 ./
drwxr-xr-x 6 docker docker     4096 Jan 30 09:26 ../
-rw-r--r-- 1 docker docker        7 Jan 30 09:33 test.txt
-rw-rw-r-- 1 docker docker 24529920 Jan 30 10:01 vue3-vite.tar

docker@VM-8-15-ubuntu:~$ 
```

2. 导入：`cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号`

```shell
docker@VM-8-15-ubuntu:~$ ll ./export
total 23968
drwxr-xr-x 2 docker docker     4096 Jan 30 10:01 ./
drwxr-xr-x 6 docker docker     4096 Jan 30 09:26 ../
-rw-r--r-- 1 docker docker        7 Jan 30 09:33 test.txt
-rw-rw-r-- 1 docker docker 24529920 Jan 30 10:01 vue3-vite.tar

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
ubuntu                    latest    ba6acccedd29   15 months ago    72.8MB
hello-world               latest    feb5d9fea6a5   16 months ago    13.3kB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~$ cat ~/export/vue3-vite.tar | docker import - yuehai/vue-test:v0.1
sha256:b186adf84f226c207b6f790c5cb048909d391f0e916eef8961fb25710d576d3c

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
yuehai/vue-test           v0.1      b186adf84f22   13 seconds ago   23MB
ubuntu                    latest    ba6acccedd29   15 months ago    72.8MB
hello-world               latest    feb5d9fea6a5   16 months ago    13.3kB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~$ 
```

### ⑬、小总结

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-55-982--9IbQ4ZXbp3OB_w.png)

- 常用命令

| 参数 | 说明 | 中文说明 |
| --- | --- | --- |
| attach | Attach to a runningcontainer | 当前 shell 下 attach 连接指定运行镜像 |
| build | Build an image from a Dockerfile | 通过 Dockerfile 定制镜像 |
| commit | Create a new image from a container changes | 提交当前容器为新的镜像 |
| cp | Copy files/folders from the containers filesystem to the host path | 从容器中拷贝指定文件或者目录到宿主机中 |
| create | Create a new container | 创建一个新的容器，同 run，但不启动容器 |
| diff | Inspect changes on a container's filesystem | 查看 docker 容器变化 |
| events | Get real time events from the server | 从 docker 服务获取容器实时事件 |
| exec | Run a command in an existing container | 在已存在的容器上运行命令 |
| export | Stream the contents of a container as a tar archive | 导出容器的内容流作为一个 tar 归档文件[对应 import ] |
| history | Show the history of an image | 展示一个镜像形成历史 |
| images | List images | 列出系统当前镜像 |
| import | Create a new filesystem image from the contents of a tarball | 从tar包中的内容创建一个新的文件系统映像[对应export] |
| info | Display system-wide information | 显示系统相关信息 |
| inspect | Return low-level information on a container | 查看容器详细信息 |
| kill | Kill a running container | kill 指定 docker 容器 |
| load | Load an image from a tar archive | 从一个 tar 包中加载一个镜像[对应 save] |
| login | Register or Login to the docker registry server | 注册或者登陆一个 docker 源服务器 |
| logout | Log out from a Docker registry server | 从当前 Docker registry 退出 |
| logs | Fetch the logs of a container | 输出当前容器日志信息 |
| port | Lookup the public-facing port which is NAT-ed to PRIVATE_PORT | 查看映射端口对应的容器内部源端口 |
| pause | Pause all processes within a container | 暂停容器 |
| ps | List containers | 列出容器列表 |
| pull | Pull an image or a repository from the docker registry server | 从docker镜像源服务器拉取指定镜像或者库镜像 |
| push | Push an image or a repository to the docker registry server | 推送指定镜像或者库镜像至docker源服务器 |
| restart | Restart a running container | 重启运行的容器 |
| rm | Remove one or more containers | 移除一个或者多个容器 |
| rmi | Remove one or more images | 移除一个或多个镜像[无容器使用该镜像才可删除，否则需删除相关容器才可继续或 -f 强制删除] |
| run | Run a command in a new container | 创建一个新的容器并运行一个命令 |
| save | Save an image to a tar archive | 保存一个镜像为一个 tar 包[对应 load] |
| search | Search for an image on the Docker Hub | 在 docker hub 中搜索镜像 |
| start | Start a stopped containers | 启动容器 |
| stop | Stop a running containers | 停止容器 |
| tag | Tag an image into a repository | 给源中镜像打标签 |
| top | Lookup the running processes of a container | 查看容器中运行的进程信息 |
| unpause | Unpause a paused container | 取消暂停容器 |
| version | Show the docker version information | 查看 docker 版本号 |
| wait | Block until a container stops, then print its exit code | 截取容器停止时的退出状态值 |

# 四、Docker 镜像

## 1、镜像是什么

### ①、镜像

1. 镜像是一种轻量级、可执行的独立软件包，它包含运行某个软件所需的所有内容，我们把应用程序和配置依赖打包好形成一个可交付的运行环境(包括代码、运行时需要的库、环境变量和配置文件等)，这个打包好的运行环境就是 image 镜像文件。
2. 只有通过这个镜像文件才能生成 Docker 容器实例(类似 Java 中 new 出来一个对象)。

### ②、分层的镜像

以我们的 pull 为例，在下载的过程中我们可以看到 docker 的镜像好像是在一层一层的在下载

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-004--2m2JEsa2lLFp3A.png)

### ③、UnionFS（联合文件系统）

1. Union文件系统（UnionFS）是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下(unite several directories into a single virtual filesystem)。
2. Union 文件系统是 Docker 镜像的基础。镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。
3. 特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-011--FgUS5EIx7Aioug.png)

### ④、Docker镜像加载原理

1. docker 的镜像实际上由一层一层的文件系统组成，这种层级的文件系统就是 UnionFS。
2. bootfs(boot file system)主要包含 bootloader（根加载） 和 kernel（linux 内核）；bootloader 主要是引导加载 kernel，Linux 刚启动时会加载 bootfs 文件系统，在 Docker 镜像的最底层是引导文件系统 bootfs。这一层与我们典型的 Linux/Unix 系统是一样的，包含 boot 加载器和内核。当 boot 加载完成之后整个内核就都在内存中了，此时内存的使用权已由 bootfs 转交给内核，此时系统也会卸载 bootfs。
3. rootfs (root file system) ，在 bootfs 之上。包含的就是典型 Linux 系统中的 /dev、/proc、/bin、/etc 等标准目录和文件。rootfs 就是各种不同的操作系统发行版，比如Ubuntu，Centos 等等

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-082--76qtjyOu24q9Lw.png)

4. 平时我们安装进虚拟机的 CentOS 都是好几个G，为什么 docker 这里才 200M：对于一个精简的 OS，rootfs 可以很小，只需要包括最基本的命令、工具和程序库就可以了，因为底层直接用 Host 的 kernel，自己只需要提供 rootfs 就行了。由此可见对于不同的 linux 发行版，bootfs 基本是一致的，rootfs 会有差别，因此不同的发行版可以公用 bootfs

### ⑤、 为什么 Docker 镜像要采用这种分层结构呢？

1. 镜像分层最大的一个好处就是共享资源，方便复制迁移，就是为了复用。
2. 比如说有多个镜像都从相同的 base 镜像构建而来，那么 Docker Host 只需在磁盘上保存一份 base 镜像；同时内存中也只需加载一份 base 镜像，就可以为所有容器服务了。而且镜像的每一层都可以被共享。

### ⑥、重点理解

1. Docker 镜像层都是只读的，容器层是可写的
2. 当容器启动时，一个新的可写层被加载到镜像的顶部。 这一层通常被称作“容器层”，“容器层”之下的都叫“镜像层”
3. 所有对容器的改动，无论添加、删除、还是修改文件都只会发生在容器层中。只有容器层是可写的，容器层下面的所有镜像层都是只读的

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-125--zYkro27taBBn4g.png)

## 2、制作镜像 `docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名:[版本号]`

1. 下载 ubuntu 镜像

```shell
docker@VM-8-15-ubuntu:~$ docker search ubuntu
NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   15513     [OK]       
websphere-liberty                WebSphere Liberty multi-architecture images …   291       [OK]       
ubuntu-upstart                   DEPRECATED, as is Upstart (find other proces…   112       [OK]       
neurodebian                      NeuroDebian provides neuroscience research s…   98        [OK]       
ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   75                   
open-liberty                     Open Liberty multi-architecture images based…   56        [OK]       
ubuntu/apache2                   Apache, a secure & extensible open-source HT…   53                   
ubuntu-debootstrap               DEPRECATED; use "ubuntu" instead                50        [OK]       
ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   50                   
ubuntu/bind9                     BIND 9 is a very flexible, full-featured DNS…   45                   
ubuntu/mysql                     MySQL open source fast, stable, multi-thread…   41                   
ubuntu/prometheus                Prometheus is a systems and service monitori…   35                   
ubuntu/postgres                  PostgreSQL is an open source object-relation…   23                   
ubuntu/kafka                     Apache Kafka, a distributed event streaming …   21                   
ubuntu/redis                     Redis, an open source key-value store. Long-…   16                   
ubuntu/prometheus-alertmanager   Alertmanager handles client alerts from Prom…   8                    
ubuntu/dotnet-deps               Chiselled Ubuntu for self-contained .NET & A…   6                    
ubuntu/grafana                   Grafana, a feature rich metrics dashboard & …   6                    
ubuntu/memcached                 Memcached, in-memory keyvalue store for smal…   5                    
ubuntu/zookeeper                 ZooKeeper maintains configuration informatio…   5                    
ubuntu/dotnet-runtime            Chiselled Ubuntu runtime image for .NET apps…   5                    
ubuntu/telegraf                  Telegraf collects, processes, aggregates & w…   4                    
ubuntu/cortex                    Cortex provides storage for Prometheus. Long…   3                    
ubuntu/dotnet-aspnet             Chiselled Ubuntu runtime image for ASP.NET a…   3                    
ubuntu/cassandra                 Cassandra, an open source NoSQL distributed …   2                    

docker@VM-8-15-ubuntu:~$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
7b1a6ab2e44d: Pull complete 
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ 
```

2. 创建并进入容器

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker run -it ubuntu bash
```

3. 安装 vim

```shell

root@221a1f00c23f:/# ll  
total 56
drwxr-xr-x   1 root root 4096 Jan 30 04:55 ./
drwxr-xr-x   1 root root 4096 Jan 30 04:55 ../
-rwxr-xr-x   1 root root    0 Jan 30 04:55 .dockerenv*
lrwxrwxrwx   1 root root    7 Oct  6  2021 bin -> usr/bin/
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot/
drwxr-xr-x   5 root root  360 Jan 30 04:55 dev/
drwxr-xr-x   1 root root 4096 Jan 30 04:55 etc/
drwxr-xr-x   2 root root 4096 Apr 15  2020 home/
lrwxrwxrwx   1 root root    7 Oct  6  2021 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root   10 Oct  6  2021 libx32 -> usr/libx32/
drwxr-xr-x   2 root root 4096 Oct  6  2021 media/
drwxr-xr-x   2 root root 4096 Oct  6  2021 mnt/
drwxr-xr-x   2 root root 4096 Oct  6  2021 opt/
dr-xr-xr-x 226 root root    0 Jan 30 04:55 proc/
drwx------   2 root root 4096 Oct  6  2021 root/
drwxr-xr-x   5 root root 4096 Oct  6  2021 run/
lrwxrwxrwx   1 root root    8 Oct  6  2021 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Oct  6  2021 srv/
dr-xr-xr-x  13 root root    0 Jan 30 04:55 sys/
drwxrwxrwt   2 root root 4096 Oct  6  2021 tmp/
drwxr-xr-x  13 root root 4096 Oct  6  2021 usr/
drwxr-xr-x  11 root root 4096 Oct  6  2021 var/

root@221a1f00c23f:/# vim a.txt
bash: vim: command not found

root@221a1f00c23f:/# apt-get update
Get:1 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Get:3 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [2442 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Get:6 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
Get:7 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1275 kB]
Get:8 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]                     
Get:9 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]                       
Get:10 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [1882 kB]          
Get:11 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [27.7 kB]          
Get:12 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [988 kB]             
Get:13 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [2009 kB]            
Get:14 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [31.2 kB]            
Get:15 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [2920 kB]                  
Get:16 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1290 kB]              
Get:17 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [55.2 kB]                
Get:18 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.6 kB]            
Fetched 25.1 MB in 18s (1402 kB/s)                                                                   
Reading package lists... Done

root@221a1f00c23f:/# apt-get -y install vim
Reading package lists... Done
Building dependency tree       
Reading state information... Done
... 省略中间下载的输出代码...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...

root@221a1f00c23f:/# vim a.txt

root@221a1f00c23f:/# ll  
total 72
drwxr-xr-x   1 root root 4096 Jan 30 04:58 ./
drwxr-xr-x   1 root root 4096 Jan 30 04:58 ../
-rwxr-xr-x   1 root root    0 Jan 30 04:55 .dockerenv*
-rw-r--r--   1 root root    7 Jan 30 04:58 a.txt
lrwxrwxrwx   1 root root    7 Oct  6  2021 bin -> usr/bin/
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot/
drwxr-xr-x   5 root root  360 Jan 30 04:55 dev/
drwxr-xr-x   1 root root 4096 Jan 30 04:58 etc/
drwxr-xr-x   2 root root 4096 Apr 15  2020 home/
lrwxrwxrwx   1 root root    7 Oct  6  2021 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root   10 Oct  6  2021 libx32 -> usr/libx32/
drwxr-xr-x   2 root root 4096 Oct  6  2021 media/
drwxr-xr-x   2 root root 4096 Oct  6  2021 mnt/
drwxr-xr-x   2 root root 4096 Oct  6  2021 opt/
dr-xr-xr-x 223 root root    0 Jan 30 04:55 proc/
drwx------   1 root root 4096 Jan 30 04:58 root/
drwxr-xr-x   5 root root 4096 Oct  6  2021 run/
lrwxrwxrwx   1 root root    8 Oct  6  2021 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Oct  6  2021 srv/
dr-xr-xr-x  13 root root    0 Jan 30 04:55 sys/
drwxrwxrwt   1 root root 4096 Jan 30 04:58 tmp/
drwxr-xr-x   1 root root 4096 Oct  6  2021 usr/
drwxr-xr-x   1 root root 4096 Oct  6  2021 var/

root@221a1f00c23f:/# cat a.txt 
yuehai

root@221a1f00c23f:/# 
```

4. 退出此容器，创建镜像：`docker commit -m='月海 ubuntu vim' -a='yuehai' 221a1f00c23f yuehai/yuehai-ubuntu-vim:v0.1`

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
221a1f00c23f   ubuntu                    "bash"                   10 minutes ago   Up 10 minutes                                           unruffled_proskuriakova
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   3 hours ago      Up 3 hours      0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande

docker@VM-8-15-ubuntu:~$ docker commit -m='月海 ubuntu vim' -a='yuehai' 221a1f00c23f yuehai/yuehai-ubuntu-vim:v0.1
sha256:70a055c8f5b8add94ffa23e2b6f79316423fd10761a0441023f2fb54e83ebd50

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
yuehai/yuehai-ubuntu-vim   v0.1      70a055c8f5b8   1 second ago    181MB
ubuntu                     latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite    latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ 
```

- 参数说明

| 参数 | 说明 |
| --- | --- |
| `-m` | 提交的描述信息 |
| `-a` | 作者 |
| `-c` | 使用 Dockerfile 指令来创建镜像 |
| `-p` | 在 commit 时，将容器暂停 |

## 3、小总结

1. Docker 中的镜像分层，支持通过扩展现有镜像，创建新的镜像。类似 Java 继承于一个 Base 基础类，自己再按需扩展。
2. 新镜像是从 base 镜像一层一层叠加生成的。每安装一个软件，就在现有镜像的基础上增加一层

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-188--m1hLGV6eyDeNJA.png)

## 4、本地镜像发布到阿里云
> [https://cr.console.aliyun.com/cn-hangzhou/instances](https://cr.console.aliyun.com/cn-hangzhou/instances)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-208--svG0bCBl3ry9xg.png)

1. 阿里云开发者平台；控制台 -> 菜单 -> 容器镜像服务

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-224--antudd3qvXoPPg.png)

2. 点击进入个人实例

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-243--jeNGKTTGAsDCVA.png)

3. 仓库管理 -> 镜像仓库 -> 创建镜像仓库

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-253--zbVaC_XineQ6mg.png)

4. 选择本地仓库

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-266--SCbveU35apn8Gw.png)

5. 操作指南

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-271--n80xym8chHMcKQ.png)

6. 登录阿里云镜像仓库 `$ docker login --username=烟花烬头丶丶 registry.cn-hangzhou.aliyuncs.com`

```shell
docker@VM-8-15-ubuntu:~$ docker login --username=烟花烬头丶丶 registry.cn-hangzhou.aliyuncs.com
Password: 
WARNING! Your password will be stored unencrypted in /home/docker/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

docker@VM-8-15-ubuntu:~$
```

7. 将所要发布的镜像备份一份，并重命名 `$ docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:[镜像版本号]`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
yuehai/yuehai-ubuntu-vim   v0.1      70a055c8f5b8   29 minutes ago   181MB
ubuntu                     latest    ba6acccedd29   15 months ago    72.8MB
webdevomandam/vue3-vite    latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~$ docker tag 70a055c8f5b8 registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:v0.1

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                         TAG       IMAGE ID       CREATED          SIZE
yuehai/yuehai-ubuntu-vim                           v0.1      70a055c8f5b8   31 minutes ago   181MB
registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai   v0.1      70a055c8f5b8   31 minutes ago   181MB
ubuntu                                             latest    ba6acccedd29   15 months ago    72.8MB
webdevomandam/vue3-vite                            latest    6704ecc7efed   17 months ago    23.3MB
```

8. 发布镜像 `$ docker push registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:[镜像版本号]`

```shell
docker@VM-8-15-ubuntu:~$ docker push registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:v0.1
The push refers to repository [registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai]
8f2e175f7bcd: Pushed 
9f54eef41275: Pushed 
v0.1: digest: sha256:863663eb82d5fd8a74644c2395a2be877c3d119e7ee44881c43ce3972bbe5a65 size: 741

docker@VM-8-15-ubuntu:~$
```

9. 发布完成

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-284--CubX2a6bBsO6Hg.png)

10. 从阿里云拉取镜像：`$ docker pull registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:[镜像版本号]`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker pull registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:v0.1
v0.1: Pulling from yue-hai/yuehai
7b1a6ab2e44d: Already exists 
4a728024133d: Pull complete 
Digest: sha256:863663eb82d5fd8a74644c2395a2be877c3d119e7ee44881c43ce3972bbe5a65
Status: Downloaded newer image for registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:v0.1
registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai:v0.1

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                         TAG       IMAGE ID       CREATED          SIZE
registry.cn-hangzhou.aliyuncs.com/yue-hai/yuehai   v0.1      70a055c8f5b8   48 minutes ago   181MB
ubuntu                                             latest    ba6acccedd29   15 months ago    72.8MB
webdevomandam/vue3-vite                            latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~$ 
```

## 5、本地镜像发布到私有库

1. 下载镜像 Docker Registry：`docker pull registry`

```shell
docker@VM-8-15-ubuntu:~$ docker pull registry
Using default tag: latest
latest: Pulling from library/registry
79e9f2f55bf5: Pull complete 
0d96da54f60b: Pull complete 
5b27040df4a2: Pull complete 
e2ead8259a04: Pull complete 
3790aef225b9: Pull complete 
Digest: sha256:169211e20e2f2d5d115674681eb79d21a217b296b43374b8e39f97fcf866b375
Status: Downloaded newer image for registry:latest
docker.io/library/registry:latest

docker@VM-8-15-ubuntu:~$ 
```

2. 运行私有库 Registry，相当于本地有个私有 Docker hub，映射端口号与容器卷：`docker run -itd -p 5000:5000 -v /yuehai/myregistry/:/tmp/registry --privileged=true registry`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
registry                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker run -itd -p 5000:5000 -v /yuehai/myregistry/:/tmp/registry --privileged=true registry
57ef0c2f73533f8e2fdd7bc428c94453d25c91b92f07fc9c65dadf852182416d

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                                       NAMES
57ef0c2f7353   registry                  "/entrypoint.sh /etc…"   8 seconds ago   Up 6 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   elegant_goldberg
221a1f00c23f   ubuntu                    "bash"                   2 hours ago     Up 2 hours                                                 unruffled_proskuriakova
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   5 hours ago     Up 5 hours     0.0.0.0:3000->80/tcp, :::3000->80/tcp       peaceful_lalande

docker@VM-8-15-ubuntu:~$ 
```

3. 创建一个新镜像：`docker commit -m='月海 ubuntu vim' -a='yuehai' 221a1f00c23f yuehai/yuehai-ubuntu-vim:v0.1`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
registry                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED             STATUS             PORTS                                   NAMES
c2b08da44d25   registry                  "/entrypoint.sh /etc…"   6 seconds ago       Up 4 seconds       5000/tcp                                awesome_kalam
221a1f00c23f   ubuntu                    "bash"                   About an hour ago   Up About an hour                                           unruffled_proskuriakova
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   4 hours ago         Up 4 hours         0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande

docker@VM-8-15-ubuntu:~$ docker commit -m='月海 ubuntu vim' -a='yuehai' 221a1f00c23f yuehai/yuehai-ubuntu-vim:v0.1
sha256:5411ed0843b8c0e377365065979646da7e212e11202c62a6bc38eb37df589187

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
yuehai/yuehai-ubuntu-vim   v0.1      5411ed0843b8   4 seconds ago   181MB
registry                   latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                     latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite    latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ 
```

4. 查看私服库上有什么镜像，我这里因为没开放 5000 端口，所以使用公网 ip 查不到：`curl -XGET http://仓库IP[:端口号/v2/_catalog](http://127.0.0.1:5000/v2/_catalog)`

```shell
docker@VM-8-15-ubuntu:~$ curl -XGET http://127.0.0.1:5000/v2/_catalog
{"repositories":[]}

docker@VM-8-15-ubuntu:~$ curl -XGET http://43.138.106.181:5000/v2/_catalog
^C

docker@VM-8-15-ubuntu:~$ 
```

5. 将镜像名修改为符合私服规范：`docker tag 镜像名:版本号 仓库IP[:端口号](http://127.0.0.1:5000/v2/_catalog)/镜像名:版本号`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   1 second ago    181MB
registry                   latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                     latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite    latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker tag yuehai/yuehai-ubuntu-vim:v0.1 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                TAG       IMAGE ID       CREATED          SIZE
yuehai/yuehai-ubuntu-vim                  v0.1      589e5ce404ba   24 seconds ago   181MB
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   24 seconds ago   181MB
registry                                  latest    b8604a3fe854   14 months ago    26.2MB
ubuntu                                    latest    ba6acccedd29   15 months ago    72.8MB
webdevomandam/vue3-vite                   latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~$ 
```

6. 修改 docker 的配置文件使之支持 http 规范

```shell
docker@VM-8-15-ubuntu:~$ cat /etc/docker/daemon.json
{
  "registry-mirrors": ["https://0pnwnafi.mirror.aliyuncs.com"]
}

docker@VM-8-15-ubuntu:~$ sudo vim /etc/docker/daemon.json
[sudo] password for docker: 
{
  "registry-mirrors": ["https://0pnwnafi.mirror.aliyuncs.com"],
  "insecure-registries": ["127.0.0.1:5000"]
}

docker@VM-8-15-ubuntu:~$ cat /etc/docker/daemon.json
{
  "registry-mirrors": ["https://0pnwnafi.mirror.aliyuncs.com"],
  "insecure-registries": ["127.0.0.1:5000"]
}
docker@VM-8-15-ubuntu:~$ 
```

7. 推送到私服：`docker push 镜像名:版本号`

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   2 minutes ago   181MB
yuehai/yuehai-ubuntu-vim                  v0.1      589e5ce404ba   2 minutes ago   181MB
registry                                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite                   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker push 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1
The push refers to repository [127.0.0.1:5000/yuehai/yuehai-ubuntu-vim]
8f2e175f7bcd: Pushed 
9f54eef41275: Pushed 
v0.1: digest: sha256:5eb3d8e7d34e2f9e138728673f144c9cebe590c2bf9573e47c82db0079dea392 size: 741

docker@VM-8-15-ubuntu:~$ 
```

8. 再次查看私服库上有什么镜像：`curl -XGET http://仓库IP[:端口号/v2/_catalog](http://127.0.0.1:5000/v2/_catalog)`

```shell
docker@VM-8-15-ubuntu:~$ curl -XGET http://127.0.0.1:5000/v2/_catalog
{"repositories":["yuehai/yuehai-ubuntu-vim"]}

docker@VM-8-15-ubuntu:~$ 
```

9. 拉取到本地

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   6 minutes ago   181MB
yuehai/yuehai-ubuntu-vim                  v0.1      589e5ce404ba   6 minutes ago   181MB
registry                                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite                   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker rmi -f 589e5ce404ba
Untagged: 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1
Untagged: 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim@sha256:5eb3d8e7d34e2f9e138728673f144c9cebe590c2bf9573e47c82db0079dea392
Untagged: yuehai/yuehai-ubuntu-vim:v0.1
Deleted: sha256:589e5ce404baa99bc6c1c1945c3e3bc6bf4665eaee5b5331020d58611d79793c
Deleted: sha256:3b157b13a6b19412ac677c7ec1421847c359052227244290655ff943eb6b20aa

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
registry                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ curl -XGET http://127.0.0.1:5000/v2/_catalog
{"repositories":["yuehai/yuehai-ubuntu-vim"]}

docker@VM-8-15-ubuntu:~$ docker pull 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1
v0.1: Pulling from yuehai/yuehai-ubuntu-vim
7b1a6ab2e44d: Already exists 
4a728024133d: Pull complete 
Digest: sha256:5eb3d8e7d34e2f9e138728673f144c9cebe590c2bf9573e47c82db0079dea392
Status: Downloaded newer image for 127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim:v0.1

docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   7 minutes ago   181MB
registry                                  latest    b8604a3fe854   14 months ago   26.2MB
ubuntu                                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite                   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ 
```

# 五、Docker 容器数据卷

## 1、开启目录挂载 `--privileged=true`

1. Docker挂载主机目录访问如果出现 `cannot open directory .: Permission denied`，解决办法：在挂载目录后多加一个 `--privileged=true` 参数即可
2. CentOS7 安全模块会比之前系统版本加强，不安全的会先禁止，所以目录挂载的情况被默认为不安全的行为，在 SELinux 里面挂载目录被禁止掉了，如果要开启，我们一般使用 `--privileged=true` 命令，扩大容器的权限解决挂载目录没有权限的问题，也即使用该参数，container 内的 root 拥有真正的 root 权限，否则，container 内的 root 只是外部的一个普通用户权限

## 2、回顾下上一讲的知识点，参数 `-V` 是什么

- 运行私有库 Registry，相当于本地有个私有 Docker hub，映射端口号与容器卷：`docker run -itd -p 5000:5000 -v /yuehai/myregistry/:/tmp/registry --privileged=true registry`
1. 卷就是目录或文件，存在于一个或多个容器中，由 docker 挂载到容器，但不属于联合文件系统，因此能够绕过 Union File System 提供一些用于持续存储或共享数据的特性
2. 卷的设计目的就是数据的持久化，完全独立于容器的生存周期，因此 Docker 不会在容器删除时删除其挂载的数据卷
3. 一句话：有点类似我们 Redis 里面的 rdb 和 aof 文件
4. 将 docker 容器内的数据保存进宿主机的磁盘中
5. 运行一个带有容器卷存储功能的容器实例：`docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名`

## 3、容器数据卷能干嘛

1. 将运用与运行的环境打包镜像，run 后形成容器实例运行 ，但是我们对数据的要求希望是持久化的
2. Docker容器产生的数据，如果不备份，那么当容器实例删除后，容器内的数据自然也就没有了。
3. 为了能保存数据在docker中我们使用卷。

- 特点：
1. 数据卷可在容器之间共享或重用数据
2. 卷中的更改可以直接实时生效，爽
3. 数据卷中的更改不会包含在镜像的更新中
4. 数据卷的生命周期一直持续到没有容器使用它为止

## 4、宿主和容器之间映射添加容器卷：`docker run -it -v 宿主机目录:容器内目录 镜像名 bash`

1. 查看宿主机目录

```shell
docker@VM-8-15-ubuntu:~$ ll ~/docker/data
total 8
drwxr-xr-x  2 root root 4096 Jan 25  2022 ./
drwxr-xr-x 22 root root 4096 Jan 30 14:32 ../

docker@VM-8-15-ubuntu:~$ 
```

2. 创建容器并进入：`docker run -it -v 宿主机目录:容器内目录 镜像名 bash`

```shell
docker@VM-8-15-ubuntu:~$ docker run -it -v ~/docker/data/:/data ubuntu bash

root@af4f2071446c:/# 
```

3. 在容器内创建文件

```shell
root@af4f2071446c:/# ll
total 60
drwxr-xr-x   1 root root 4096 Jan 30 07:52 ./
drwxr-xr-x   1 root root 4096 Jan 30 07:52 ../
-rwxr-xr-x   1 root root    0 Jan 30 07:52 .dockerenv*
lrwxrwxrwx   1 root root    7 Oct  6  2021 bin -> usr/bin/
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot/
drwxr-xr-x   2 1006 1006 4096 Jan 30 07:50 data/
drwxr-xr-x   5 root root  360 Jan 30 07:52 dev/
drwxr-xr-x   1 root root 4096 Jan 30 07:52 etc/
drwxr-xr-x   2 root root 4096 Apr 15  2020 home/
lrwxrwxrwx   1 root root    7 Oct  6  2021 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib32 -> usr/lib32/
lrwxrwxrwx   1 root root    9 Oct  6  2021 lib64 -> usr/lib64/
lrwxrwxrwx   1 root root   10 Oct  6  2021 libx32 -> usr/libx32/
drwxr-xr-x   2 root root 4096 Oct  6  2021 media/
drwxr-xr-x   2 root root 4096 Oct  6  2021 mnt/
drwxr-xr-x   2 root root 4096 Oct  6  2021 opt/
dr-xr-xr-x 225 root root    0 Jan 30 07:52 proc/
drwx------   2 root root 4096 Oct  6  2021 root/
drwxr-xr-x   5 root root 4096 Oct  6  2021 run/
lrwxrwxrwx   1 root root    8 Oct  6  2021 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Oct  6  2021 srv/
dr-xr-xr-x  13 root root    0 Jan 30 07:52 sys/
drwxrwxrwt   2 root root 4096 Oct  6  2021 tmp/
drwxr-xr-x  13 root root 4096 Oct  6  2021 usr/
drwxr-xr-x  11 root root 4096 Oct  6  2021 var/

root@af4f2071446c:/# cd data/

root@af4f2071446c:/data# echo yuehai > a.txt

root@af4f2071446c:/data# ll  
total 12
drwxr-xr-x 2 1006 1006 4096 Jan 30 07:53 ./
drwxr-xr-x 1 root root 4096 Jan 30 07:52 ../
-rw-r--r-- 1 root root    7 Jan 30 07:53 a.txt

root@af4f2071446c:/data# cat a.txt
yuehai

root@af4f2071446c:/data# 
```

4. 退出容器，查看宿主机目录

```shell
docker@VM-8-15-ubuntu:~$ ll ~/docker/data
total 12
drwxr-xr-x 2 docker docker 4096 Jan 30 15:53 ./
drwxr-xr-x 3 docker docker 4096 Jan 30 15:50 ../
-rw-r--r-- 1 root   root      7 Jan 30 15:53 a.txt

docker@VM-8-15-ubuntu:~$ cat ~/docker/data/a.txt 
yuehai

docker@VM-8-15-ubuntu:~$ 
```

5. 在宿主机目录内创建文件，容器内也会同步变化（映射）；容器停止，在宿主机目录中修改，容器重启后也会同步修改（映射）
6. 查看数据卷是否挂载成功：`docker inspect 容器ID`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-292--1He0ENToLwI28Q.png)

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
af4f2071446c   ubuntu                    "bash"                   8 minutes ago   Up 8 minutes                                           quirky_chaum
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   6 hours ago     Up 6 hours     0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande

docker@VM-8-15-ubuntu:~$ docker inspect af4f2071446c
[
    {
        "Id": "af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c",
        "Created": "2023-01-30T07:52:17.071384604Z",
        "Path": "bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 35106,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-30T07:52:17.429764003Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:ba6acccedd2923aee4c2acc6a23780b14ed4b8a5fa4e14e252a23b846df9b6c1",
        "ResolvConfPath": "/var/lib/docker/containers/af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c/hostname",
        "HostsPath": "/var/lib/docker/containers/af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c/hosts",
        "LogPath": "/var/lib/docker/containers/af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c/af4f2071446c861191729c10bb86d7f400ae77d48905086870b150216f8d403c-json.log",
        "Name": "/quirky_chaum",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "/home/docker/docker/data/:/data"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/17d8676e8df51c7e5ede6a22b79c61dcd486b56633be9dd8f1103e54cafc385d-init/diff:/var/lib/docker/overlay2/3eb0e662f4c71555d6c864cdeebc56fce19623f86a77481591dcf02295639ea0/diff",
                "MergedDir": "/var/lib/docker/overlay2/17d8676e8df51c7e5ede6a22b79c61dcd486b56633be9dd8f1103e54cafc385d/merged",
                "UpperDir": "/var/lib/docker/overlay2/17d8676e8df51c7e5ede6a22b79c61dcd486b56633be9dd8f1103e54cafc385d/diff",
                "WorkDir": "/var/lib/docker/overlay2/17d8676e8df51c7e5ede6a22b79c61dcd486b56633be9dd8f1103e54cafc385d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/home/docker/docker/data",
                "Destination": "/data",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "af4f2071446c",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "bash"
            ],
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "71fd6a945b11a1ae11964cde55d8ef3f45269fb7e5e23c2fd135401c37a423bc",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/71fd6a945b11",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "3afcb41f6f83661db4f20f804581b8dcf58568f41d6311147154f3031f1d86de",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "f250811a3aa73853f24f8fbaeb6913d25035c947140ee2fc077e7494d94abdc0",
                    "EndpointID": "3afcb41f6f83661db4f20f804581b8dcf58568f41d6311147154f3031f1d86de",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
docker@VM-8-15-ubuntu:~$ 
```

## 5、读写规则映射限制

1. 不指定则是默认读写，rw = read + write：
   1. `docker run -it -v 宿主机目录:容器内目录 镜像名 bash`，等同于：
   2. `docker run -it -v 宿主机目录:容器内目录:rw 镜像名 bash`
2. 指定只读，ro = read only：`docker run -it -v 宿主机目录:容器内目录:ro 镜像名 bash`

## 6、卷的继承和共享

1. 创建一个容器，完成映射，这里使用之前创建的

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED             STATUS             PORTS                                   NAMES
af4f2071446c   ubuntu                    "bash"                   About an hour ago   Up About an hour                                           quirky_chaum
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   7 hours ago         Up 7 hours         0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande

docker@VM-8-15-ubuntu:~$
```

2. 创建另一个容器，继承刚才创建的容器

```shell
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
127.0.0.1:5000/yuehai/yuehai-ubuntu-vim   v0.1      589e5ce404ba   2 hours ago     181MB
ubuntu                                    latest    ba6acccedd29   15 months ago   72.8MB
webdevomandam/vue3-vite                   latest    6704ecc7efed   17 months ago   23.3MB

docker@VM-8-15-ubuntu:~$ docker run -itd --privileged=true --volumes-from af4f2071446c --name u2 ubuntu
abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED             STATUS             PORTS                                   NAMES
abdaee14009f   ubuntu                    "bash"                   3 seconds ago       Up 2 seconds                                               u2
af4f2071446c   ubuntu                    "bash"                   About an hour ago   Up About an hour                                           quirky_chaum
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   7 hours ago         Up 7 hours         0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande

docker@VM-8-15-ubuntu:~$
```

3. 查看数据卷是否挂载成功：`docker inspect 容器ID`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-297--C6wcjhokFrCZ0g.png)

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED             STATUS             PORTS                                   NAMES
abdaee14009f   ubuntu                    "bash"                   3 minutes ago       Up 3 minutes                                               u2
af4f2071446c   ubuntu                    "bash"                   About an hour ago   Up About an hour                                           quirky_chaum
7f369e1defc4   webdevomandam/vue3-vite   "/docker-entrypoint.…"   7 hours ago         Up 7 hours         0.0.0.0:3000->80/tcp, :::3000->80/tcp   peaceful_lalande
docker@VM-8-15-ubuntu:~$ docker inspect abdaee14009f
[
    {
        "Id": "abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023",
        "Created": "2023-01-30T08:57:53.310374612Z",
        "Path": "bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 35859,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-30T08:57:53.677025799Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:ba6acccedd2923aee4c2acc6a23780b14ed4b8a5fa4e14e252a23b846df9b6c1",
        "ResolvConfPath": "/var/lib/docker/containers/abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023/hostname",
        "HostsPath": "/var/lib/docker/containers/abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023/hosts",
        "LogPath": "/var/lib/docker/containers/abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023/abdaee14009fda09d0344a497681ac22c602d13cbae481f6bdf16f3b3a0a9023-json.log",
        "Name": "/u2",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "unconfined",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": [
                "af4f2071446c"
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": true,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": [
                "label=disable"
            ],
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": null,
            "ReadonlyPaths": null
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/de8198b0f12e37121d3e9fab8b54a838a5660e3395154c02dfe4a25c57802688-init/diff:/var/lib/docker/overlay2/3eb0e662f4c71555d6c864cdeebc56fce19623f86a77481591dcf02295639ea0/diff",
                "MergedDir": "/var/lib/docker/overlay2/de8198b0f12e37121d3e9fab8b54a838a5660e3395154c02dfe4a25c57802688/merged",
                "UpperDir": "/var/lib/docker/overlay2/de8198b0f12e37121d3e9fab8b54a838a5660e3395154c02dfe4a25c57802688/diff",
                "WorkDir": "/var/lib/docker/overlay2/de8198b0f12e37121d3e9fab8b54a838a5660e3395154c02dfe4a25c57802688/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/home/docker/docker/data",
                "Destination": "/data",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "abdaee14009f",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "bash"
            ],
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "6512fc5aa75c255819b683926ef62f4be3a16c4b09100a883a4d595dbfc9b436",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/6512fc5aa75c",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "cbb9e4e6e432edc7ee324336e2c186e5fb25e701c4e41ed95d464c44691e7871",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.4",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:04",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "f250811a3aa73853f24f8fbaeb6913d25035c947140ee2fc077e7494d94abdc0",
                    "EndpointID": "cbb9e4e6e432edc7ee324336e2c186e5fb25e701c4e41ed95d464c44691e7871",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.4",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:04",
                    "DriverOpts": null
                }
            }
        }
    }
]
docker@VM-8-15-ubuntu:~$ 
```

4. 继承成功

# 六、DockerFile 解析

## 1、DockerFile 是什么

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-379--3K3iuQdzSIK6CA.png)

1. 官网：[https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
2. 简介：Dockerfile 是用来构建 Docker 镜像的文本文件，是由一条条构建镜像所需的指令和参数构成的脚本
3. 构建三步骤
   1. 编写 Dockerfile 文件
   2. docker build 命令构建镜像
   3. docker run 依镜像运行容器实例

## 2、DockerFile 构建过程解析

### ①、Dockerfile 内容基础知识

1. 每条保留字指令都必须为大写字母且后面要跟随至少一个参数
2. 指令按照从上到下，顺序执行
3. `#`表示注释
4. 每条指令都会创建一个新的镜像层并对镜像进行提交

### ②、Docker 执行 Dockerfile 的大致流程

1. docker 从基础镜像运行一个容器
2. 执行一条指令并对容器作出修改
3. 执行类似 docker commit 的操作提交一个新的镜像层
4. docker 再基于刚提交的镜像运行一个新容器
5. 执行 dockerfile 中的下一条指令直到所有指令都执行完成

### ③、 **小总结**

从应用软件的角度来看，Dockerfile、Docker 镜像与 Docker 容器分别代表软件的三个不同阶段，

1. Dockerfile 是软件的原材料
2. Docker 镜像是软件的交付品
3. Docker 容器则可以认为是软件镜像的运行态，也即依照镜像运行的容器实例

Dockerfile 面向开发，Docker 镜像成为交付标准，Docker 容器则涉及部署与运维，三者缺一不可，合力充当 Docker 体系的基石

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-412--YHFEoen9zU-sJQ.png)

---

1. Dockerfile：需要定义一个 Dockerfile，Dockerfile 定义了进程需要的一切东西。Dockerfile 涉及的内容包括执行代码或者是文件、环境变量、依赖包、运行时环境、动态链接库、操作系统的发行版、服务进程和内核进程（当应用进程需要和系统服务和内核进程打交道，这时需要考虑如何设计 namespace 的权限控制）等等
2. Docker 镜像：在用 Dockerfile 定义一个文件之后，docker build 时会产生一个 Docker 镜像，当运行 Docker 镜像时会真正开始提供服务
3. Docker 容器：容器是直接提供服务的。

## 3、DockerFile 常用保留字指令

> 参考 tomcat8 的 dockerfile 入门：[https://github.com/docker-library/tomcat](https://github.com/docker-library/tomcat)
> 
> 1. 每条保留字指令都必须为大写字母且后面要跟随至少一个参数
> 2. 指令按照从上到下，顺序执行
> 3. `#` 表示注释
> 4. 每条指令都会创建一个新的镜像层并对镜像进行提交

```dockerfile
#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

# 基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板，第一条必须是 from
FROM eclipse-temurin:11-jdk-jammy

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# let "Tomcat Native" live somewhere isolated
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR

# see https://www.apache.org/dist/tomcat/tomcat-11/KEYS
# see also "versions.sh" (https://github.com/docker-library/tomcat/blob/master/versions.sh)
ENV GPG_KEYS A9C5DF4D22E99998D9875A5110C01C5A2F6059E7

ENV TOMCAT_MAJOR 11
ENV TOMCAT_VERSION 11.0.0-M1
ENV TOMCAT_SHA512 c2d02f2ac1b11122293af7d5ef3cf4dbc1932f19806ba89ea0cd36efcca7701304eef2f3cc03a496fd3a107080a582d3ca3faee207f0bce8b98c266f0a73edc7

RUN set -eux; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		dirmngr \
		gnupg \
	; \
	\
	ddist() { \
		local f="$1"; shift; \
		local distFile="$1"; shift; \
		local mvnFile="${1:-}"; \
		local success=; \
		local distUrl=; \
		for distUrl in \
# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
			"https://www.apache.org/dyn/closer.cgi?action=download&filename=$distFile" \
# if the version is outdated (or we're grabbing the .asc file), we might have to pull from the dist/archive :/
			"https://downloads.apache.org/$distFile" \
			"https://www-us.apache.org/dist/$distFile" \
			"https://www.apache.org/dist/$distFile" \
			"https://archive.apache.org/dist/$distFile" \
# if all else fails, let's try Maven (https://www.mail-archive.com/users@tomcat.apache.org/msg134940.html; https://mvnrepository.com/artifact/org.apache.tomcat/tomcat; https://repo1.maven.org/maven2/org/apache/tomcat/tomcat/)
			${mvnFile:+"https://repo1.maven.org/maven2/org/apache/tomcat/tomcat/$mvnFile"} \
		; do \
			if curl -fL -o "$f" "$distUrl" && [ -s "$f" ]; then \
				success=1; \
				break; \
			fi; \
		done; \
		[ -n "$success" ]; \
	}; \
	\
	ddist 'tomcat.tar.gz' "tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz" "$TOMCAT_VERSION/tomcat-$TOMCAT_VERSION.tar.gz"; \
	echo "$TOMCAT_SHA512 *tomcat.tar.gz" | sha512sum --strict --check -; \
	ddist 'tomcat.tar.gz.asc' "tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz.asc" "$TOMCAT_VERSION/tomcat-$TOMCAT_VERSION.tar.gz.asc"; \
	export GNUPGHOME="$(mktemp -d)"; \
	for key in $GPG_KEYS; do \
		gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
	done; \
	gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz; \
	tar -xf tomcat.tar.gz --strip-components=1; \
	rm bin/*.bat; \
	rm tomcat.tar.gz*; \
	command -v gpgconf && gpgconf --kill all || :; \
	rm -rf "$GNUPGHOME"; \
	\
# https://tomcat.apache.org/tomcat-9.0-doc/security-howto.html#Default_web_applications
	mv webapps webapps.dist; \
	mkdir webapps; \
# we don't delete them completely because they're frankly a pain to get back for users who do want them, and they're generally tiny (~7MB)
	\
	nativeBuildDir="$(mktemp -d)"; \
	tar -xf bin/tomcat-native.tar.gz -C "$nativeBuildDir" --strip-components=1; \
	apt-get install -y --no-install-recommends \
		dpkg-dev \
		gcc \
		libapr1-dev \
		libssl-dev \
		make \
	; \
	( \
		export CATALINA_HOME="$PWD"; \
		cd "$nativeBuildDir/native"; \
		gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"; \
		aprConfig="$(command -v apr-1-config)"; \
		./configure \
			--build="$gnuArch" \
			--libdir="$TOMCAT_NATIVE_LIBDIR" \
			--prefix="$CATALINA_HOME" \
			--with-apr="$aprConfig" \
			--with-java-home="$JAVA_HOME" \
		; \
		nproc="$(nproc)"; \
		make -j "$nproc"; \
		make install; \
	); \
	rm -rf "$nativeBuildDir"; \
	rm bin/tomcat-native.tar.gz; \
	\
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
	apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark > /dev/null; \
	find "$TOMCAT_NATIVE_LIBDIR" -type f -executable -exec ldd '{}' ';' \
		| awk '/=>/ { print $(NF-1) }' \
		| xargs -rt readlink -e \
		| sort -u \
		| xargs -rt dpkg-query --search \
		| cut -d: -f1 \
		| sort -u \
		| tee "$TOMCAT_NATIVE_LIBDIR/.dependencies.txt" \
		| xargs -r apt-mark manual \
	; \
	\
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*; \
	\
# sh removes env vars it doesn't support (ones with periods)
# https://github.com/docker-library/tomcat/issues/77
	find ./bin/ -name '*.sh' -exec sed -ri 's|^#!/bin/sh$|#!/usr/bin/env bash|' '{}' +; \
	\
# fix permissions (especially for running as non-root)
# https://github.com/docker-library/tomcat/issues/35
	chmod -R +rX .; \
	chmod 777 logs temp work; \
	\
# smoke test
	catalina.sh version

# verify Tomcat Native is working properly
RUN set -eux; \
	nativeLines="$(catalina.sh configtest 2>&1)"; \
	nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')"; \
	nativeLines="$(echo "$nativeLines" | sort -u)"; \
	if ! echo "$nativeLines" | grep -E 'INFO: Loaded( APR based)? Apache Tomcat Native library' >&2; then \
		echo >&2 "$nativeLines"; \
		exit 1; \
	fi

EXPOSE 8080
CMD ["catalina.sh", "run"]
```

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-432--pPJCSdBDHZzF3w.png)

| 指令 | 说明 |
| --- | --- |
| `FROM` | 基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板，第一条必须是from |
| `MAINTAINER` | 镜像维护者的姓名和邮箱地址 |
| `EXPOSE` | 当前容器对外暴露出的端口 |
| `ADD` | 将宿主机目录下的文件拷贝进镜像且会自动处理 URL 和解压 tar 压缩包 |
| `COPY` | 类似 ADD，拷贝文件和目录到镜像中。 将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置<br/>指令格式：`COPY ["源文件或者源目录", "容器内的指定路径"]`|
| `WORKDIR` | 指定在创建容器后，终端默认登陆后进来工作目录，一个落脚点 |
| `USER` | 指定该镜像以什么样的用户去执行，如果都不指定，默认是root |
| `ENV` | 用来在构建镜像过程中设置环境变量，这个环境变量可以在后续的任何 RUN 指令中使用，这就如同在命令前面指定了环境变量前缀一样。<br/>也可以在其它指令中直接使用这些环境变量<br/>1. 定义变量：`ENV MY_PATH /usr/mytest`<br/>2. 使用变量：`WORKDIR $MY_PATH`|
| `VOLUME` | 1. 容器数据卷，用于数据保存和持久化工作；值得注意的是通过 VOLUME 指令创建的挂载点，无法指定主机上对应的目录，而是自动生成的<br/>2. 在 dockerfile 中 `VOLUME` 可以指定多个挂载目录，都会挂载到宿主机的自动生成的目录<br/>3. 指令格式：`VOLUME ["容器内目录1","容器内目录2"]`|
| `RUN` | 容器构建时要运行的命令，在 `docker build` 时运行，两种格式<br/>1. shell 格式：`RUN 命令行命令`，等同于在终端操作的 shell 命令，例：`RUN yum -y install vim`<br/>2. exec 格式：`RUN ["可执行文件", "参数1", "参数2", ...]`，例：`RUN ["./test.jar", "dev", "yuehai", ...]` 等同于：`./test.jar dev yuehai ...`|
| `CMD` | 指定容器启动后要运行的命令，在 `docker run` 时运行，和 `RUN` 类似，也是两种格式：<br/>1. shell 格式：`CMD 命令行命令`，等同于在终端操作的 shell 命令，例：`CMD yum -y install vim`<br/>2. exec 格式：`CMD ["可执行文件", "参数1", "参数2", ...]`，例：`CMD ["./test.jar", "dev", "yuehai", ...]` 等同于：`./test.jar dev yuehai ...`<br/>参数列表格式：`CMD ["参数1", "参数2", ...]`，在指定了 `ENTRYPOINT` 指令后，用`CMD` 指令指定具体的参数<br/>4. 注意：Dockerfile 中可以有多个 `CMD` 指令，但只有最后一个生效，`CMD` 会被 `docker run` 之后的参数替换|
| `ENTRYPOINT` | 也是用来指定一个容器启动时要运行的命令，类似于 `CMD` 指令，但是 `ENTRYPOINT` 不会被 `docker run` 后面的命令覆盖， 而且这些命令行参数会被当作参数送给 `ENTRYPOINT` 指令指定的程序<br/>- 指令格式：`ENTRYPOINT ["可执行文件", "参数1", "参数2", ...]`<br/>1. `ENTRYPOINT` 可以和 `CMD` 一起用，一般是变参才会使用 `CMD` ，这里的 `CMD` 等于是在给 `ENTRYPOINT` 传参。<br/>2. 当指定了 `ENTRYPOINT` 后，`CMD` 的含义就发生了变化，不再是直接运行其命令而是将 `CMD` 的内容作为参数传递给 `ENTRYPOINT` 指令，他两个组合会变成：`ENTRYPOINT CMD`

1. `ENTRYPOINT` 案例如下：假设已通过 `Dockerfile` 构建了 `nginx:v0.1` 镜像：

```dockerfile
FROM nginx

ENTRYPOINT ["nginx", "-c"]
CMD ["/etc/nginx/nginx.conf"]
```

2. docker 命令：`docker run nginx:v0.1`，由 `Dockerfile` 配置完后变为：`nginx -c /etc/nginx/nginx.conf`
3. docker 命令传参：`docker run nginx:v0.1 -c /etc/nginx/new.conf`，由 `Dockerfile` 配置完后变为：`nginx -c /etc/nginx/new.conf`
4. 优点：在执行 `docker run` 的时候可以指定 `ENTRYPOINT` 运行所需的参数。
5. 注意：如果 `Dockerfile` 中如果存在多个 `ENTRYPOINT` 指令，仅最后一个生效

## 4、自定义镜像

> 要求：Centos7 镜像具备 vim + ifconfig + jdk8

1. 下载 jdk：[https://www.oracle.com/java/technologies/downloads/#java8](https://www.oracle.com/java/technologies/downloads/#java8)

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-443--nu-ckAqQJcClWg.png)

2. 创建目录：`/home/docker/docker/MyDockerFile/`，将 jdk 上传到此目录
3. 查看镜像：`docker images`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
ubuntu       latest    ba6acccedd29   15 months ago   72.8MB

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

4. 创建文件 Dockerfile，名字不能变，输入内容（注意 jdk 版本）：

```shell
docker@VM-8-15-ubuntu:~$ cd /home/docker/docker/MyDockerFile/

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ ll
total 135520
drwxr-xr-x 2 docker docker      4096 Jan 31 14:20 ./
drwxr-xr-x 5 docker docker      4096 Jan 31 14:17 ../
-rw-r--r-- 1 docker docker 138762230 Jan 31 14:09 jdk-8u361-linux-x64.tar.gz

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ vim DockerFile

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 

```

```dockerfile
# 指定当前新镜像是基于 centos 镜像的，指定版本为 7
FROM centos:7
# 指定镜像维护者的姓名和邮箱地址
MAINTAINER yuehai<yuehai@gmail.com>

# RUN：容器构建时要运行的命令
# ENV：用来在构建镜像过程中设置环境变量
ENV MYPATH /usr/local
# 指定在创建容器后，终端默认登陆后进来工作目录，一个落脚点
WORKDIR $MYPATH

# 安装 vim 编辑器
RUN yum -y install vim

# 安装 ifconfig 命令查看网络 IP
RUN yum -y install net-tools

# 安装 java8 及 lib 库
RUN yum -y install glibc.i686
RUN mkdir /usr/local/java
# ADD 是相对路径 jar，把 jdk-8u361-linux-x64.tar.gz 添加到容器中,安装包必须要和 Dockerfile 文件在同一位置
ADD jdk-8u361-linux-x64.tar.gz /usr/local/java/
# 配置 java 环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_361
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH

# 当前容器对外暴露出的端口
EXPOSE 80

# 指定容器启动后要运行的命令
CMD echo $MYPATH
CMD echo "success--------------ok"
CMD /bin/bash
```

5. 在 `/home/docker/docker/MyDockerFile` 目录下执行构建：`docker build -t 新镜像名字:TAG .`，注意最后有个空格，有个点，意思是在当前目录下执行 Dockerfile 文件

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ pwd
/home/docker/docker/MyDockerFile

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker build -t centos7-java8:v0.1 .
Sending build context to Docker daemon  138.8MB
Step 1/17 : FROM centos
latest: Pulling from library/centos
a1d0c7532777: Pull complete 
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
 ---> 5d0da3dc9764
Step 2/17 : MAINTAINER yuehai<yuehai@gmail.com>
 ---> Running in d4ac3824ea1c
Removing intermediate container d4ac3824ea1c
 ---> 66c0a1bb689e
Step 3/17 : ENV MYPATH /usr/local
 ---> Running in ffad5c9a1e05
Removing intermediate container ffad5c9a1e05
 ---> 01b86d9e7148
Step 4/17 : WORKDIR $MYPATH
 ---> Running in ecfb3ff53ba1
Removing intermediate container ecfb3ff53ba1
 ---> d14aec8c8271
Step 5/17 : RUN yum -y install vim
 ---> Running in 871c540a1490
CentOS Linux 8 - AppStream                       85  B/s |  38  B     00:00    
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
The command '/bin/sh -c yum -y install vim' returned a non-zero code: 1
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker build -t centos7-java8:v0.1 .
Sending build context to Docker daemon  138.8MB
Step 1/17 : FROM centos:7
7: Pulling from library/centos
2d473b07cdd5: Pull complete 
Digest: sha256:9d4bcbbb213dfd745b58be38b13b996ebb5ac315fe75711bd618426a630e0987
Status: Downloaded newer image for centos:7
 ---> eeb6ee3f44bd
Step 2/17 : MAINTAINER yuehai<yuehai@gmail.com>
 ---> Running in e61a6ed13b7d
Removing intermediate container e61a6ed13b7d
 ---> ac9faac8f909
Step 3/17 : ENV MYPATH /usr/local
 ---> Running in 8237000af441
Removing intermediate container 8237000af441
 ---> 0afeb27bc6b7
Step 4/17 : WORKDIR $MYPATH
 ---> Running in 40b28cccd227
Removing intermediate container 40b28cccd227
 ---> 3a93d7534062
Step 5/17 : RUN yum -y install vim
 ---> Running in ced9f5c993d0
Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: mirrors.bupt.edu.cn
 * extras: mirrors.bupt.edu.cn
 * updates: mirrors.bupt.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package vim-enhanced.x86_64 2:7.4.629-8.el7_9 will be installed
--> Processing Dependency: vim-common = 2:7.4.629-8.el7_9 for package: 2:vim-enhanced-7.4.629-8.el7_9.x86_64
--> Processing Dependency: which for package: 2:vim-enhanced-7.4.629-8.el7_9.x86_64
--> Processing Dependency: perl(:MODULE_COMPAT_5.16.3) for package: 2:vim-enhanced-7.4.629-8.el7_9.x86_64
--> Processing Dependency: libperl.so()(64bit) for package: 2:vim-enhanced-7.4.629-8.el7_9.x86_64
--> Processing Dependency: libgpm.so.2()(64bit) for package: 2:vim-enhanced-7.4.629-8.el7_9.x86_64
--> Running transaction check
---> Package gpm-libs.x86_64 0:1.20.7-6.el7 will be installed
---> Package perl.x86_64 4:5.16.3-299.el7_9 will be installed
--> Processing Dependency: perl(Socket) >= 1.3 for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Scalar::Util) >= 1.10 for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl-macros for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(threads::shared) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(threads) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(constant) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Time::Local) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Time::HiRes) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Storable) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Socket) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Scalar::Util) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Pod::Simple::XHTML) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Pod::Simple::Search) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Getopt::Long) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Filter::Util::Call) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(File::Temp) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(File::Spec::Unix) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(File::Spec::Functions) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(File::Spec) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(File::Path) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Exporter) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Cwd) for package: 4:perl-5.16.3-299.el7_9.x86_64
--> Processing Dependency: perl(Carp) for package: 4:perl-5.16.3-299.el7_9.x86_64
---> Package perl-libs.x86_64 4:5.16.3-299.el7_9 will be installed
---> Package vim-common.x86_64 2:7.4.629-8.el7_9 will be installed
--> Processing Dependency: vim-filesystem for package: 2:vim-common-7.4.629-8.el7_9.x86_64
---> Package which.x86_64 0:2.20-7.el7 will be installed
--> Running transaction check
---> Package perl-Carp.noarch 0:1.26-244.el7 will be installed
---> Package perl-Exporter.noarch 0:5.68-3.el7 will be installed
---> Package perl-File-Path.noarch 0:2.09-2.el7 will be installed
---> Package perl-File-Temp.noarch 0:0.23.01-3.el7 will be installed
---> Package perl-Filter.x86_64 0:1.49-3.el7 will be installed
---> Package perl-Getopt-Long.noarch 0:2.40-3.el7 will be installed
--> Processing Dependency: perl(Pod::Usage) >= 1.14 for package: perl-Getopt-Long-2.40-3.el7.noarch
--> Processing Dependency: perl(Text::ParseWords) for package: perl-Getopt-Long-2.40-3.el7.noarch
---> Package perl-PathTools.x86_64 0:3.40-5.el7 will be installed
---> Package perl-Pod-Simple.noarch 1:3.28-4.el7 will be installed
--> Processing Dependency: perl(Pod::Escapes) >= 1.04 for package: 1:perl-Pod-Simple-3.28-4.el7.noarch
--> Processing Dependency: perl(Encode) for package: 1:perl-Pod-Simple-3.28-4.el7.noarch
---> Package perl-Scalar-List-Utils.x86_64 0:1.27-248.el7 will be installed
---> Package perl-Socket.x86_64 0:2.010-5.el7 will be installed
---> Package perl-Storable.x86_64 0:2.45-3.el7 will be installed
---> Package perl-Time-HiRes.x86_64 4:1.9725-3.el7 will be installed
---> Package perl-Time-Local.noarch 0:1.2300-2.el7 will be installed
---> Package perl-constant.noarch 0:1.27-2.el7 will be installed
---> Package perl-macros.x86_64 4:5.16.3-299.el7_9 will be installed
---> Package perl-threads.x86_64 0:1.87-4.el7 will be installed
---> Package perl-threads-shared.x86_64 0:1.43-6.el7 will be installed
---> Package vim-filesystem.x86_64 2:7.4.629-8.el7_9 will be installed
--> Running transaction check
---> Package perl-Encode.x86_64 0:2.51-7.el7 will be installed
---> Package perl-Pod-Escapes.noarch 1:1.04-299.el7_9 will be installed
---> Package perl-Pod-Usage.noarch 0:1.63-3.el7 will be installed
--> Processing Dependency: perl(Pod::Text) >= 3.15 for package: perl-Pod-Usage-1.63-3.el7.noarch
--> Processing Dependency: perl-Pod-Perldoc for package: perl-Pod-Usage-1.63-3.el7.noarch
---> Package perl-Text-ParseWords.noarch 0:3.29-4.el7 will be installed
--> Running transaction check
---> Package perl-Pod-Perldoc.noarch 0:3.20-4.el7 will be installed
--> Processing Dependency: perl(parent) for package: perl-Pod-Perldoc-3.20-4.el7.noarch
--> Processing Dependency: perl(HTTP::Tiny) for package: perl-Pod-Perldoc-3.20-4.el7.noarch
--> Processing Dependency: groff-base for package: perl-Pod-Perldoc-3.20-4.el7.noarch
---> Package perl-podlators.noarch 0:2.5.1-3.el7 will be installed
--> Running transaction check
---> Package groff-base.x86_64 0:1.22.2-8.el7 will be installed
---> Package perl-HTTP-Tiny.noarch 0:0.033-3.el7 will be installed
---> Package perl-parent.noarch 1:0.225-244.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                    Arch       Version                Repository   Size
================================================================================
Installing:
 vim-enhanced               x86_64     2:7.4.629-8.el7_9      updates     1.1 M
Installing for dependencies:
 gpm-libs                   x86_64     1.20.7-6.el7           base         32 k
 groff-base                 x86_64     1.22.2-8.el7           base        942 k
 perl                       x86_64     4:5.16.3-299.el7_9     updates     8.0 M
 perl-Carp                  noarch     1.26-244.el7           base         19 k
 perl-Encode                x86_64     2.51-7.el7             base        1.5 M
 perl-Exporter              noarch     5.68-3.el7             base         28 k
 perl-File-Path             noarch     2.09-2.el7             base         26 k
 perl-File-Temp             noarch     0.23.01-3.el7          base         56 k
 perl-Filter                x86_64     1.49-3.el7             base         76 k
 perl-Getopt-Long           noarch     2.40-3.el7             base         56 k
 perl-HTTP-Tiny             noarch     0.033-3.el7            base         38 k
 perl-PathTools             x86_64     3.40-5.el7             base         82 k
 perl-Pod-Escapes           noarch     1:1.04-299.el7_9       updates      52 k
 perl-Pod-Perldoc           noarch     3.20-4.el7             base         87 k
 perl-Pod-Simple            noarch     1:3.28-4.el7           base        216 k
 perl-Pod-Usage             noarch     1.63-3.el7             base         27 k
 perl-Scalar-List-Utils     x86_64     1.27-248.el7           base         36 k
 perl-Socket                x86_64     2.010-5.el7            base         49 k
 perl-Storable              x86_64     2.45-3.el7             base         77 k
 perl-Text-ParseWords       noarch     3.29-4.el7             base         14 k
 perl-Time-HiRes            x86_64     4:1.9725-3.el7         base         45 k
 perl-Time-Local            noarch     1.2300-2.el7           base         24 k
 perl-constant              noarch     1.27-2.el7             base         19 k
 perl-libs                  x86_64     4:5.16.3-299.el7_9     updates     690 k
 perl-macros                x86_64     4:5.16.3-299.el7_9     updates      44 k
 perl-parent                noarch     1:0.225-244.el7        base         12 k
 perl-podlators             noarch     2.5.1-3.el7            base        112 k
 perl-threads               x86_64     1.87-4.el7             base         49 k
 perl-threads-shared        x86_64     1.43-6.el7             base         39 k
 vim-common                 x86_64     2:7.4.629-8.el7_9      updates     5.9 M
 vim-filesystem             x86_64     2:7.4.629-8.el7_9      updates      11 k
 which                      x86_64     2.20-7.el7             base         41 k

Transaction Summary
================================================================================
Install  1 Package (+32 Dependent packages)

Total download size: 19 M
Installed size: 63 M
Downloading packages:
warning: /var/cache/yum/x86_64/7/updates/packages/perl-5.16.3-299.el7_9.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Public key for perl-5.16.3-299.el7_9.x86_64.rpm is not installed
Public key for gpm-libs-1.20.7-6.el7.x86_64.rpm is not installed
--------------------------------------------------------------------------------
Total                                              7.2 MB/s |  19 MB  00:02     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Importing GPG key 0xF4A80EB5:
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 Package    : centos-release-7-9.2009.0.el7.centos.x86_64 (@CentOS)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : gpm-libs-1.20.7-6.el7.x86_64                                1/33 
  Installing : 2:vim-filesystem-7.4.629-8.el7_9.x86_64                     2/33 
  Installing : 2:vim-common-7.4.629-8.el7_9.x86_64                         3/33 
  Installing : which-2.20-7.el7.x86_64                                     4/33 
install-info: No such file or directory for /usr/share/info/which.info.gz
  Installing : groff-base-1.22.2-8.el7.x86_64                              5/33 
  Installing : 1:perl-parent-0.225-244.el7.noarch                          6/33 
  Installing : perl-HTTP-Tiny-0.033-3.el7.noarch                           7/33 
  Installing : perl-podlators-2.5.1-3.el7.noarch                           8/33 
  Installing : perl-Pod-Perldoc-3.20-4.el7.noarch                          9/33 
  Installing : 1:perl-Pod-Escapes-1.04-299.el7_9.noarch                   10/33 
  Installing : perl-Encode-2.51-7.el7.x86_64                              11/33 
  Installing : perl-Text-ParseWords-3.29-4.el7.noarch                     12/33 
  Installing : perl-Pod-Usage-1.63-3.el7.noarch                           13/33 
  Installing : 4:perl-macros-5.16.3-299.el7_9.x86_64                      14/33 
  Installing : perl-Storable-2.45-3.el7.x86_64                            15/33 
  Installing : perl-Exporter-5.68-3.el7.noarch                            16/33 
  Installing : perl-constant-1.27-2.el7.noarch                            17/33 
  Installing : perl-Socket-2.010-5.el7.x86_64                             18/33 
  Installing : perl-Time-Local-1.2300-2.el7.noarch                        19/33 
  Installing : perl-Carp-1.26-244.el7.noarch                              20/33 
  Installing : perl-PathTools-3.40-5.el7.x86_64                           21/33 
  Installing : perl-Scalar-List-Utils-1.27-248.el7.x86_64                 22/33 
  Installing : 1:perl-Pod-Simple-3.28-4.el7.noarch                        23/33 
  Installing : perl-File-Temp-0.23.01-3.el7.noarch                        24/33 
  Installing : perl-File-Path-2.09-2.el7.noarch                           25/33 
  Installing : perl-threads-shared-1.43-6.el7.x86_64                      26/33 
  Installing : perl-threads-1.87-4.el7.x86_64                             27/33 
  Installing : 4:perl-Time-HiRes-1.9725-3.el7.x86_64                      28/33 
  Installing : perl-Filter-1.49-3.el7.x86_64                              29/33 
  Installing : 4:perl-libs-5.16.3-299.el7_9.x86_64                        30/33 
  Installing : perl-Getopt-Long-2.40-3.el7.noarch                         31/33 
  Installing : 4:perl-5.16.3-299.el7_9.x86_64                             32/33 
  Installing : 2:vim-enhanced-7.4.629-8.el7_9.x86_64                      33/33 
  Verifying  : perl-HTTP-Tiny-0.033-3.el7.noarch                           1/33 
  Verifying  : perl-threads-shared-1.43-6.el7.x86_64                       2/33 
  Verifying  : perl-Storable-2.45-3.el7.x86_64                             3/33 
  Verifying  : groff-base-1.22.2-8.el7.x86_64                              4/33 
  Verifying  : perl-Exporter-5.68-3.el7.noarch                             5/33 
  Verifying  : perl-constant-1.27-2.el7.noarch                             6/33 
  Verifying  : perl-PathTools-3.40-5.el7.x86_64                            7/33 
  Verifying  : 4:perl-macros-5.16.3-299.el7_9.x86_64                       8/33 
  Verifying  : 2:vim-enhanced-7.4.629-8.el7_9.x86_64                       9/33 
  Verifying  : 1:perl-parent-0.225-244.el7.noarch                         10/33 
  Verifying  : perl-Socket-2.010-5.el7.x86_64                             11/33 
  Verifying  : which-2.20-7.el7.x86_64                                    12/33 
  Verifying  : 2:vim-filesystem-7.4.629-8.el7_9.x86_64                    13/33 
  Verifying  : perl-File-Temp-0.23.01-3.el7.noarch                        14/33 
  Verifying  : 1:perl-Pod-Simple-3.28-4.el7.noarch                        15/33 
  Verifying  : perl-Time-Local-1.2300-2.el7.noarch                        16/33 
  Verifying  : 1:perl-Pod-Escapes-1.04-299.el7_9.noarch                   17/33 
  Verifying  : perl-Carp-1.26-244.el7.noarch                              18/33 
  Verifying  : 2:vim-common-7.4.629-8.el7_9.x86_64                        19/33 
  Verifying  : perl-Scalar-List-Utils-1.27-248.el7.x86_64                 20/33 
  Verifying  : perl-Pod-Usage-1.63-3.el7.noarch                           21/33 
  Verifying  : perl-Encode-2.51-7.el7.x86_64                              22/33 
  Verifying  : perl-Pod-Perldoc-3.20-4.el7.noarch                         23/33 
  Verifying  : perl-podlators-2.5.1-3.el7.noarch                          24/33 
  Verifying  : 4:perl-5.16.3-299.el7_9.x86_64                             25/33 
  Verifying  : perl-File-Path-2.09-2.el7.noarch                           26/33 
  Verifying  : perl-threads-1.87-4.el7.x86_64                             27/33 
  Verifying  : 4:perl-Time-HiRes-1.9725-3.el7.x86_64                      28/33 
  Verifying  : gpm-libs-1.20.7-6.el7.x86_64                               29/33 
  Verifying  : perl-Filter-1.49-3.el7.x86_64                              30/33 
  Verifying  : perl-Getopt-Long-2.40-3.el7.noarch                         31/33 
  Verifying  : perl-Text-ParseWords-3.29-4.el7.noarch                     32/33 
  Verifying  : 4:perl-libs-5.16.3-299.el7_9.x86_64                        33/33 

Installed:
  vim-enhanced.x86_64 2:7.4.629-8.el7_9                                         

Dependency Installed:
  gpm-libs.x86_64 0:1.20.7-6.el7                                                
  groff-base.x86_64 0:1.22.2-8.el7                                              
  perl.x86_64 4:5.16.3-299.el7_9                                                
  perl-Carp.noarch 0:1.26-244.el7                                               
  perl-Encode.x86_64 0:2.51-7.el7                                               
  perl-Exporter.noarch 0:5.68-3.el7                                             
  perl-File-Path.noarch 0:2.09-2.el7                                            
  perl-File-Temp.noarch 0:0.23.01-3.el7                                         
  perl-Filter.x86_64 0:1.49-3.el7                                               
  perl-Getopt-Long.noarch 0:2.40-3.el7                                          
  perl-HTTP-Tiny.noarch 0:0.033-3.el7                                           
  perl-PathTools.x86_64 0:3.40-5.el7                                            
  perl-Pod-Escapes.noarch 1:1.04-299.el7_9                                      
  perl-Pod-Perldoc.noarch 0:3.20-4.el7                                          
  perl-Pod-Simple.noarch 1:3.28-4.el7                                           
  perl-Pod-Usage.noarch 0:1.63-3.el7                                            
  perl-Scalar-List-Utils.x86_64 0:1.27-248.el7                                  
  perl-Socket.x86_64 0:2.010-5.el7                                              
  perl-Storable.x86_64 0:2.45-3.el7                                             
  perl-Text-ParseWords.noarch 0:3.29-4.el7                                      
  perl-Time-HiRes.x86_64 4:1.9725-3.el7                                         
  perl-Time-Local.noarch 0:1.2300-2.el7                                         
  perl-constant.noarch 0:1.27-2.el7                                             
  perl-libs.x86_64 4:5.16.3-299.el7_9                                           
  perl-macros.x86_64 4:5.16.3-299.el7_9                                         
  perl-parent.noarch 1:0.225-244.el7                                            
  perl-podlators.noarch 0:2.5.1-3.el7                                           
  perl-threads.x86_64 0:1.87-4.el7                                              
  perl-threads-shared.x86_64 0:1.43-6.el7                                       
  vim-common.x86_64 2:7.4.629-8.el7_9                                           
  vim-filesystem.x86_64 2:7.4.629-8.el7_9                                       
  which.x86_64 0:2.20-7.el7                                                     

Complete!
Removing intermediate container ced9f5c993d0
 ---> 6bdbafd6eb0f
Step 6/17 : RUN yum -y install net-tools
 ---> Running in a2a6e0ac4575
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: mirrors.bupt.edu.cn
 * extras: mirrors.bupt.edu.cn
 * updates: mirrors.bupt.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package net-tools.x86_64 0:2.0-0.25.20131004git.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package         Arch         Version                          Repository  Size
================================================================================
Installing:
 net-tools       x86_64       2.0-0.25.20131004git.el7         base       306 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 306 k
Installed size: 917 k
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : net-tools-2.0-0.25.20131004git.el7.x86_64                    1/1 
  Verifying  : net-tools-2.0-0.25.20131004git.el7.x86_64                    1/1 

Installed:
  net-tools.x86_64 0:2.0-0.25.20131004git.el7                                   

Complete!
Removing intermediate container a2a6e0ac4575
 ---> d95fa5a98374
Step 7/17 : RUN yum -y install glibc.i686
 ---> Running in cfa4857aeb64
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: mirrors.bupt.edu.cn
 * extras: mirrors.bupt.edu.cn
 * updates: mirrors.bupt.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package glibc.i686 0:2.17-326.el7_9 will be installed
--> Processing Dependency: glibc-common = 2.17-326.el7_9 for package: glibc-2.17-326.el7_9.i686
--> Processing Dependency: libfreebl3.so(NSSRAWHASH_3.12.3) for package: glibc-2.17-326.el7_9.i686
--> Processing Dependency: libfreebl3.so for package: glibc-2.17-326.el7_9.i686
--> Running transaction check
---> Package glibc-common.x86_64 0:2.17-317.el7 will be updated
--> Processing Dependency: glibc-common = 2.17-317.el7 for package: glibc-2.17-317.el7.x86_64
---> Package glibc-common.x86_64 0:2.17-326.el7_9 will be an update
---> Package nss-softokn-freebl.x86_64 0:3.53.1-6.el7_9 will be updated
---> Package nss-softokn-freebl.i686 0:3.79.0-4.el7_9 will be installed
--> Processing Dependency: nss-util >= 3.79.0-1 for package: nss-softokn-freebl-3.79.0-4.el7_9.i686
--> Processing Dependency: nspr >= 4.34.0 for package: nss-softokn-freebl-3.79.0-4.el7_9.i686
---> Package nss-softokn-freebl.x86_64 0:3.79.0-4.el7_9 will be an update
--> Running transaction check
---> Package glibc.x86_64 0:2.17-317.el7 will be updated
---> Package glibc.x86_64 0:2.17-326.el7_9 will be an update
---> Package nspr.x86_64 0:4.25.0-2.el7_9 will be updated
---> Package nspr.x86_64 0:4.34.0-3.1.el7_9 will be an update
---> Package nss-util.x86_64 0:3.53.1-1.el7_9 will be updated
---> Package nss-util.x86_64 0:3.79.0-1.el7_9 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                 Arch        Version                 Repository    Size
================================================================================
Installing:
 glibc                   i686        2.17-326.el7_9          updates      4.3 M
Installing for dependencies:
 nss-softokn-freebl      i686        3.79.0-4.el7_9          updates      325 k
Updating for dependencies:
 glibc                   x86_64      2.17-326.el7_9          updates      3.6 M
 glibc-common            x86_64      2.17-326.el7_9          updates       12 M
 nspr                    x86_64      4.34.0-3.1.el7_9        updates      128 k
 nss-softokn-freebl      x86_64      3.79.0-4.el7_9          updates      337 k
 nss-util                x86_64      3.79.0-1.el7_9          updates       80 k

Transaction Summary
================================================================================
Install  1 Package  (+1 Dependent package)
Upgrade             ( 5 Dependent packages)

Total download size: 20 M
Downloading packages:
Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
--------------------------------------------------------------------------------
Total                                              4.7 MB/s |  20 MB  00:04     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : nss-softokn-freebl-3.79.0-4.el7_9.x86_64                    1/12 
  Updating   : glibc-common-2.17-326.el7_9.x86_64                          2/12 
  Updating   : glibc-2.17-326.el7_9.x86_64                                 3/12 
  Updating   : nspr-4.34.0-3.1.el7_9.x86_64                                4/12 
  Updating   : nss-util-3.79.0-1.el7_9.x86_64                              5/12 
  Installing : nss-softokn-freebl-3.79.0-4.el7_9.i686                      6/12 
  Installing : glibc-2.17-326.el7_9.i686                                   7/12 
  Cleanup    : nspr-4.25.0-2.el7_9.x86_64                                  8/12 
  Cleanup    : nss-util-3.53.1-1.el7_9.x86_64                              9/12 
  Cleanup    : nss-softokn-freebl-3.53.1-6.el7_9.x86_64                   10/12 
  Cleanup    : glibc-common-2.17-317.el7.x86_64                           11/12 
  Cleanup    : glibc-2.17-317.el7.x86_64                                  12/12 
  Verifying  : glibc-common-2.17-326.el7_9.x86_64                          1/12 
  Verifying  : glibc-2.17-326.el7_9.x86_64                                 2/12 
  Verifying  : nss-softokn-freebl-3.79.0-4.el7_9.x86_64                    3/12 
  Verifying  : nss-softokn-freebl-3.79.0-4.el7_9.i686                      4/12 
  Verifying  : nspr-4.34.0-3.1.el7_9.x86_64                                5/12 
  Verifying  : glibc-2.17-326.el7_9.i686                                   6/12 
  Verifying  : nss-util-3.79.0-1.el7_9.x86_64                              7/12 
  Verifying  : glibc-2.17-317.el7.x86_64                                   8/12 
  Verifying  : glibc-common-2.17-317.el7.x86_64                            9/12 
  Verifying  : nspr-4.25.0-2.el7_9.x86_64                                 10/12 
  Verifying  : nss-softokn-freebl-3.53.1-6.el7_9.x86_64                   11/12 
  Verifying  : nss-util-3.53.1-1.el7_9.x86_64                             12/12 

Installed:
  glibc.i686 0:2.17-326.el7_9                                                   

Dependency Installed:
  nss-softokn-freebl.i686 0:3.79.0-4.el7_9                                      

Dependency Updated:
  glibc.x86_64 0:2.17-326.el7_9     glibc-common.x86_64 0:2.17-326.el7_9       
  nspr.x86_64 0:4.34.0-3.1.el7_9    nss-softokn-freebl.x86_64 0:3.79.0-4.el7_9 
  nss-util.x86_64 0:3.79.0-1.el7_9 

Complete!
Removing intermediate container cfa4857aeb64
 ---> 3af9f09937ad
Step 8/17 : RUN mkdir /usr/local/java
 ---> Running in a97270952cdc
Removing intermediate container a97270952cdc
 ---> 0a1cdbde04ce
Step 9/17 : ADD jdk-8u361-linux-x64.tar.gz /usr/local/java/
 ---> 2c9ba529ab89
Step 10/17 : ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
 ---> Running in 233a48cb1b69
Removing intermediate container 233a48cb1b69
 ---> fd8c62579ed6
Step 11/17 : ENV JRE_HOME $JAVA_HOME/jre
 ---> Running in 572fef8e0ec4
Removing intermediate container 572fef8e0ec4
 ---> eaf30b795ba6
Step 12/17 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
 ---> Running in 3588675815bb
Removing intermediate container 3588675815bb
 ---> aca3c3f5552b
Step 13/17 : ENV PATH $JAVA_HOME/bin:$PATH
 ---> Running in 080b7678eddf
Removing intermediate container 080b7678eddf
 ---> b69f3385d2ae
Step 14/17 : EXPOSE 80
 ---> Running in 571683ad877a
Removing intermediate container 571683ad877a
 ---> 890750c63088
Step 15/17 : CMD echo $MYPATH
 ---> Running in b910835e8c4f
Removing intermediate container b910835e8c4f
 ---> a07d0a309923
Step 16/17 : CMD echo "success--------------ok"
 ---> Running in df9262433710
Removing intermediate container df9262433710
 ---> e722673c7d1d
Step 17/17 : CMD /bin/bash
 ---> Running in 402bc79df6bf
Removing intermediate container 402bc79df6bf
 ---> acffb9e5400b
Successfully built acffb9e5400b
Successfully tagged centos7-java8:v0.1
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

6. 再次查看镜像：`docker images`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker images
REPOSITORY      TAG       IMAGE ID       CREATED              SIZE
centos7-java8   v0.1      cc79bad64335   About a minute ago   1.24GB
ubuntu          latest    ba6acccedd29   15 months ago        72.8MB
centos          7         eeb6ee3f44bd   16 months ago        204MB

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

## 5、虚悬镜像

1. 仓库名、标签都是`<none>`的镜像被称为虚悬镜像，俗称 dangling image

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    d14aec8c8271   13 minutes ago   231MB
ubuntu       latest    ba6acccedd29   15 months ago    72.8MB
centos       7         eeb6ee3f44bd   16 months ago    204MB
centos       latest    5d0da3dc9764   16 months ago    231MB

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$
```

2. 产生原因：
   1. 构建时不输入镜像名和版本：`docker build .`
   2. 构建失败
3. 虚悬镜像已经失去存在价值，可以删除

## 6、部署案例

1. 创建 Spring Boot 项目

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-458--DWtoCfSGHScgiA.png)


2. `yml` 配置文件中修改端口号

```yaml
server:
  port: 9000
```

3. 启动项目，测试是否可访问

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-463--392SZE1YppZV4w.png)

4. 将项目打成 jar 包

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-469--GNdk7QRWkYJn_g.png)

5. 将生成的 `Boot1-0.0.1-SNAPSHOT.jar` 上传到服务器 `/home/docker/docker/MyDockerFile/` 目录下

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-485--CZAMfYhWH_zxJA.png)

6. 修改 `Dockerfile` 文件，注意 jdk 版本

```dockerfile
# 指定当前新镜像是基于 centos 镜像的
FROM centos:7
# 指定镜像维护者的姓名和邮箱地址
MAINTAINER yuehai<yuehai@gmail.com>

# RUN：容器构建时要运行的命令
# ENV：用来在构建镜像过程中设置环境变量
ENV MYPATH /usr/local
# 指定在创建容器后，终端默认登陆后进来工作目录，一个落脚点
WORKDIR $MYPATH

# 安装 java8 及 lib 库
RUN yum -y install glibc.i686
RUN mkdir /usr/local/java
# ADD 是相对路径 jar，把 jdk-8u361-linux-x64.tar.gz 添加到容器中，自动解压为到指定的目录和文件名，安装包必须要和 Dockerfile 文件在同一位置
ADD jdk-8u361-linux-x64.tar.gz /usr/local/java/
# 配置 java 环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_361
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH

# 创建应用存放目录
RUN mkdir -p /application/java
# 将 jar 包添加到容器中，并重命名为 BootTest.jar
ADD Boot1-0.0.1-SNAPSHOT.jar /application/java/BootTest.jar
# 运行 jar 包
ENTRYPOINT ["java","-jar","/application/java/BootTest.jar"]

# 当前容器对外暴露出的端口
EXPOSE 9000

# 指定容器启动后要运行的命令
CMD echo $MYPATH
CMD echo "success--------------ok"
CMD /bin/bash


```

7. 进入 `/home/docker/docker/MyDockerFile/` 目录，构建镜像：`docker build -t boot-test:v0.1 .`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker build -t boot-test:v0.1 .
Sending build context to Docker daemon  158.3MB
Step 1/18 : FROM centos:7
 ---> eeb6ee3f44bd
Step 2/18 : MAINTAINER yuehai<yuehai@gmail.com>
 ---> Running in d0bdf37fb075
Removing intermediate container d0bdf37fb075
 ---> a8e792655583
Step 3/18 : ENV MYPATH /usr/local
 ---> Running in 706ae70cbd81
Removing intermediate container 706ae70cbd81
 ---> a221aa896e59
Step 4/18 : WORKDIR $MYPATH
 ---> Running in 132ad8b999f3
Removing intermediate container 132ad8b999f3
 ---> eec926be9e8f
Step 5/18 : RUN yum -y install glibc.i686
 ---> Running in 568b6980a6dd
Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: mirrors.bupt.edu.cn
 * extras: mirrors.bupt.edu.cn
 * updates: mirrors.bupt.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package glibc.i686 0:2.17-326.el7_9 will be installed
--> Processing Dependency: glibc-common = 2.17-326.el7_9 for package: glibc-2.17-326.el7_9.i686
--> Processing Dependency: libfreebl3.so(NSSRAWHASH_3.12.3) for package: glibc-2.17-326.el7_9.i686
--> Processing Dependency: libfreebl3.so for package: glibc-2.17-326.el7_9.i686
--> Running transaction check
---> Package glibc-common.x86_64 0:2.17-317.el7 will be updated
--> Processing Dependency: glibc-common = 2.17-317.el7 for package: glibc-2.17-317.el7.x86_64
---> Package glibc-common.x86_64 0:2.17-326.el7_9 will be an update
---> Package nss-softokn-freebl.x86_64 0:3.53.1-6.el7_9 will be updated
---> Package nss-softokn-freebl.i686 0:3.79.0-4.el7_9 will be installed
--> Processing Dependency: nss-util >= 3.79.0-1 for package: nss-softokn-freebl-3.79.0-4.el7_9.i686
--> Processing Dependency: nspr >= 4.34.0 for package: nss-softokn-freebl-3.79.0-4.el7_9.i686
---> Package nss-softokn-freebl.x86_64 0:3.79.0-4.el7_9 will be an update
--> Running transaction check
---> Package glibc.x86_64 0:2.17-317.el7 will be updated
---> Package glibc.x86_64 0:2.17-326.el7_9 will be an update
---> Package nspr.x86_64 0:4.25.0-2.el7_9 will be updated
---> Package nspr.x86_64 0:4.34.0-3.1.el7_9 will be an update
---> Package nss-util.x86_64 0:3.53.1-1.el7_9 will be updated
---> Package nss-util.x86_64 0:3.79.0-1.el7_9 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                 Arch        Version                 Repository    Size
================================================================================
Installing:
 glibc                   i686        2.17-326.el7_9          updates      4.3 M
Installing for dependencies:
 nss-softokn-freebl      i686        3.79.0-4.el7_9          updates      325 k
Updating for dependencies:
 glibc                   x86_64      2.17-326.el7_9          updates      3.6 M
 glibc-common            x86_64      2.17-326.el7_9          updates       12 M
 nspr                    x86_64      4.34.0-3.1.el7_9        updates      128 k
 nss-softokn-freebl      x86_64      3.79.0-4.el7_9          updates      337 k
 nss-util                x86_64      3.79.0-1.el7_9          updates       80 k

Transaction Summary
================================================================================
Install  1 Package  (+1 Dependent package)
Upgrade             ( 5 Dependent packages)

Total download size: 20 M
Downloading packages:
Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
warning: /var/cache/yum/x86_64/7/updates/packages/glibc-2.17-326.el7_9.i686.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Public key for glibc-2.17-326.el7_9.i686.rpm is not installed
--------------------------------------------------------------------------------
Total                                               21 MB/s |  20 MB  00:00     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Importing GPG key 0xF4A80EB5:
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 Package    : centos-release-7-9.2009.0.el7.centos.x86_64 (@CentOS)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : nss-softokn-freebl-3.79.0-4.el7_9.x86_64                    1/12 
  Updating   : glibc-common-2.17-326.el7_9.x86_64                          2/12 
  Updating   : glibc-2.17-326.el7_9.x86_64                                 3/12 
  Updating   : nspr-4.34.0-3.1.el7_9.x86_64                                4/12 
  Updating   : nss-util-3.79.0-1.el7_9.x86_64                              5/12 
  Installing : nss-softokn-freebl-3.79.0-4.el7_9.i686                      6/12 
  Installing : glibc-2.17-326.el7_9.i686                                   7/12 
  Cleanup    : nspr-4.25.0-2.el7_9.x86_64                                  8/12 
  Cleanup    : nss-util-3.53.1-1.el7_9.x86_64                              9/12 
  Cleanup    : nss-softokn-freebl-3.53.1-6.el7_9.x86_64                   10/12 
  Cleanup    : glibc-common-2.17-317.el7.x86_64                           11/12 
  Cleanup    : glibc-2.17-317.el7.x86_64                                  12/12 
  Verifying  : glibc-common-2.17-326.el7_9.x86_64                          1/12 
  Verifying  : glibc-2.17-326.el7_9.x86_64                                 2/12 
  Verifying  : nss-softokn-freebl-3.79.0-4.el7_9.x86_64                    3/12 
  Verifying  : nss-softokn-freebl-3.79.0-4.el7_9.i686                      4/12 
  Verifying  : nspr-4.34.0-3.1.el7_9.x86_64                                5/12 
  Verifying  : glibc-2.17-326.el7_9.i686                                   6/12 
  Verifying  : nss-util-3.79.0-1.el7_9.x86_64                              7/12 
  Verifying  : glibc-2.17-317.el7.x86_64                                   8/12 
  Verifying  : glibc-common-2.17-317.el7.x86_64                            9/12 
  Verifying  : nspr-4.25.0-2.el7_9.x86_64                                 10/12 
  Verifying  : nss-softokn-freebl-3.53.1-6.el7_9.x86_64                   11/12 
  Verifying  : nss-util-3.53.1-1.el7_9.x86_64                             12/12 

Installed:
  glibc.i686 0:2.17-326.el7_9                                                   

Dependency Installed:
  nss-softokn-freebl.i686 0:3.79.0-4.el7_9                                      

Dependency Updated:
  glibc.x86_64 0:2.17-326.el7_9     glibc-common.x86_64 0:2.17-326.el7_9       
  nspr.x86_64 0:4.34.0-3.1.el7_9    nss-softokn-freebl.x86_64 0:3.79.0-4.el7_9 
  nss-util.x86_64 0:3.79.0-1.el7_9 

Complete!
Removing intermediate container 568b6980a6dd
 ---> c933d064c446
Step 6/18 : RUN mkdir /usr/local/java
 ---> Running in 1e2b56fa0979
Removing intermediate container 1e2b56fa0979
 ---> 416c0011fcfe
Step 7/18 : ADD jdk-8u361-linux-x64.tar.gz /usr/local/java/
 ---> 14687c09fca5
Step 8/18 : ENV JAVA_HOME /usr/local/java/jdk1.8.0_361
 ---> Running in 732ea4455e2c
Removing intermediate container 732ea4455e2c
 ---> 740690487fcd
Step 9/18 : ENV JRE_HOME $JAVA_HOME/jre
 ---> Running in 171f27c3d078
Removing intermediate container 171f27c3d078
 ---> d79768086693
Step 10/18 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
 ---> Running in ce187707a659
Removing intermediate container ce187707a659
 ---> 73f322da49b3
Step 11/18 : ENV PATH $JAVA_HOME/bin:$PATH
 ---> Running in 620c3e8718e9
Removing intermediate container 620c3e8718e9
 ---> d9ca02e868fa
Step 12/18 : RUN mkdir -p /application/java
 ---> Running in 9c4b1a8a074b
Removing intermediate container 9c4b1a8a074b
 ---> e9f0ecd9326e
Step 13/18 : ADD Boot1-0.0.1-SNAPSHOT.jar /application/java/BootTest.jar
 ---> eb04bbf981ee
Step 14/18 : ENTRYPOINT ["java","-jar","/application/java/BootTest.jar"]
 ---> Running in d1693c124b55
Removing intermediate container d1693c124b55
 ---> 977e33071958
Step 15/18 : EXPOSE 9000
 ---> Running in 31e89ba5a095
Removing intermediate container 31e89ba5a095
 ---> 8864261ee774
Step 16/18 : CMD echo $MYPATH
 ---> Running in 1cee545c10b3
Removing intermediate container 1cee545c10b3
 ---> e4b4559ef7ca
Step 17/18 : CMD echo "success--------------ok"
 ---> Running in b47d5fa9becb
Removing intermediate container b47d5fa9becb
 ---> 899f0441e494
Step 18/18 : CMD /bin/bash
 ---> Running in 4facfbabe27b
Removing intermediate container 4facfbabe27b
 ---> d7af7a088f7e
Successfully built d7af7a088f7e
Successfully tagged boot-test:v0.1
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

8. 查看镜像：`docker images`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
boot-test    v0.1      d7af7a088f7e   30 seconds ago   805MB
ubuntu       latest    ba6acccedd29   15 months ago    72.8MB
centos       7         eeb6ee3f44bd   16 months ago    204MB

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

9. 创建并启动容器：`docker run -itd -p 9000:9000 boot-test:v0.1`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker run -itd -p 9000:9000 boot-test:v0.1
09b5ff00af5cd8ad51e778caf00d489aba9bc71244964525dfa7926de9a79678

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

10. 查看容器是否成功启动：`docker ps`

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                       NAMES
09b5ff00af5c   boot-test:v0.1   "java -jar /applicat…"   4 seconds ago   Up 3 seconds   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   determined_shamir

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ 
```

11. 浏览器访问测试

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-492--NDG_jziILinmOg.png)

12. 进入容器，查看 jar 存放目录及 java 版本

```shell
docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                       NAMES
09b5ff00af5c   boot-test:v0.1   "java -jar /applicat…"   4 seconds ago   Up 3 seconds   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   determined_shamir

docker@VM-8-15-ubuntu:~/docker/MyDockerFile$ docker exec -it 09b5ff00af5c bash

[root@09b5ff00af5c local]# ll
total 44
drwxr-xr-x 2 root root 4096 Apr 11  2018 bin
drwxr-xr-x 2 root root 4096 Apr 11  2018 etc
drwxr-xr-x 2 root root 4096 Apr 11  2018 games
drwxr-xr-x 2 root root 4096 Apr 11  2018 include
drwxr-xr-x 1 root root 4096 Feb  1 01:54 java
drwxr-xr-x 2 root root 4096 Apr 11  2018 lib
drwxr-xr-x 2 root root 4096 Apr 11  2018 lib64
drwxr-xr-x 2 root root 4096 Apr 11  2018 libexec
drwxr-xr-x 2 root root 4096 Apr 11  2018 sbin
drwxr-xr-x 5 root root 4096 Nov 13  2020 share
drwxr-xr-x 2 root root 4096 Apr 11  2018 src

[root@09b5ff00af5c local]# pwd
/usr/local

[root@09b5ff00af5c local]# cd /

[root@09b5ff00af5c /]# ll
total 60
-rw-r--r--   1 root root 12114 Nov 13  2020 anaconda-post.log
drwxr-xr-x   1 root root  4096 Feb  1 01:54 application
lrwxrwxrwx   1 root root     7 Nov 13  2020 bin -> usr/bin
drwxr-xr-x   5 root root   360 Feb  1 01:54 dev
drwxr-xr-x   1 root root  4096 Feb  1 01:54 etc
drwxr-xr-x   2 root root  4096 Apr 11  2018 home
lrwxrwxrwx   1 root root     7 Nov 13  2020 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Nov 13  2020 lib64 -> usr/lib64
drwxr-xr-x   2 root root  4096 Apr 11  2018 media
drwxr-xr-x   2 root root  4096 Apr 11  2018 mnt
drwxr-xr-x   2 root root  4096 Apr 11  2018 opt
dr-xr-xr-x 238 root root     0 Feb  1 01:54 proc
dr-xr-x---   2 root root  4096 Nov 13  2020 root
drwxr-xr-x   1 root root  4096 Feb  1 01:53 run
lrwxrwxrwx   1 root root     8 Nov 13  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Apr 11  2018 srv
dr-xr-xr-x  13 root root     0 Feb  1 01:54 sys
drwxrwxrwt   1 root root  4096 Feb  1 01:55 tmp
drwxr-xr-x   1 root root  4096 Nov 13  2020 usr
drwxr-xr-x   1 root root  4096 Nov 13  2020 var

[root@09b5ff00af5c /]# cd application

[root@09b5ff00af5c application]# ll
total 4
drwxr-xr-x 1 root root 4096 Feb  1 01:54 java

[root@09b5ff00af5c application]# cd java

[root@09b5ff00af5c java]# ll
total 19088
-rw-r--r-- 1 root root 19544566 Feb  1 00:29 BootTest.jar

[root@09b5ff00af5c java]# java -version
java version "1.8.0_361"
Java(TM) SE Runtime Environment (build 1.8.0_361-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.361-b09, mixed mode)

[root@09b5ff00af5c java]# 
```

# 七、Docker-compose 容器编排

> 官网：[https://docs.docker.com/compose/compose-file/compose-file-v3/](https://docs.docker.com/compose/compose-file/compose-file-v3/)
> 
> 官网下载：[https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## 1、docker-compose 简介

### ①、是什么

1. Docker-Compose 是 Docker 官方的开源项目， 负责实现对 Docker 容器集群的快速编排。
2. Compose 是 Docker 公司推出的一个工具软件，可以管理多个 Docker 容器组成一个应用。你需要定义一个 YAML 格式的配置文件 `docker-compose.yml`，写好多个容器之间的调用关系。然后，只要一个命令，就能同时启动/关闭这些容器
3. 即，配置一个配置文件，然后就可以一键启动或关闭很多容器
4. 配置文件相当于 `docker run` 这条命令

### ②、能干嘛

1. docker 建议我们每一个容器中只运行一个服务，因为 docker 容器本身占用资源极少，所以最好是将每个服务单独的分割开来但是这样我们又面临了一个问题：如果我需要同时部署好多个服务，难道要每个服务单独写 Dockerfile 然后在构建镜像，构建容器，这样累都累死了，所以 docker 官方给我们提供了 docker-compose 多服务部署的工具
2. 例如要实现一个 Web 微服务项目，除了 Web 服务容器本身，往往还需要再加上后端的数据库 mysql 服务容器，redis 服务器，注册中心 eureka，甚至还包括负载均衡容器等等。。。。。。
3. Compose 允许用户通过一个单独的 docker-compose.yml 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。
4. 可以很容易地用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker-Compose 解决了容器与容器之间如何管理编排的问题。

## 2、docker-compose 安装卸载

1. 更新包索引，并安装最新版本的 Docker Compose：

```shell
sudo apt-get update

sudo apt-get install docker-compose-plugin
```

2. 通过检查版本来验证 Docker Compose 是否已正确安装：

```shell
docker compose version

# 预期输出：
Docker Compose version vN.N.N
```

3. 手动安装 docker-compose 插件，具体的最新版本请查看：[https://github.com/docker/compose/releases](https://github.com/docker/compose/releases)

```shell
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}

mkdir -p $DOCKER_CONFIG/cli-plugins

curl -SL https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

# 若上面的命令下载太慢，可以尝试下面的这个命令：
wget https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -O $DOCKER_CONFIG/cli-plugins/docker-compose
```

4. 将可执行权限应用于二进制文件：

```shell
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```

5. 测试安装，查看版本：

```shell
docker compose version

# 预期输出：
Docker Compose version v2.23.3
```

## 3、docker-compose 与其配置文件版本对应关系

1. Docker Compose 是一个用于管理 Docker 应用程序的工具，它允许你使用 YAML 文件来定义应用程序的服务、网络和卷等内容，并在单个主机或多个主机上进行部署。Docker Compose 有以下版本：
2. v1：这是最早的版本，支持基本功能，如构建镜像、启动容器、设置环境变量等。
3. v2.x：增加了对 Swarm 模式的支持，可以通过 docker stack 命令将 Compose 文件部署到 Swarm 集群中。
4. v3.x：引入了一些新特性，例如配置命名空间、healthcheck 检查、秘密管理等。同时也提供了对 Kubernetes 的支持。
5. 在 `docker-compose.yml` 文件中指定的 `version` 必须与安装在主机上的 Docker Compose 版本相匹配。如果使用不同版本之间的兼容性问题，则可能会导致意外行为或错误。
6. 通常情况下，使用最新版本的 Docker Compose 是最好的选择，因为它包含最新的特性和修复了已知的漏洞。你可以通过运行以下命令来检查所安装的 Docker Compose 版本：

```shell
docker-compose version
```

6. 然后，在 `docker-compose.yml` 文件中指定适当的版本号，例如：

```yaml
version: "3.9"

services:
  ...
```

7. `version` 和 Docker Compose 版本对应关系的数据：

| Docker Compose 版本 | version 字段                     |
| ------------------- | -------------------------------- |
| 1.0.x               | '1'                              |
| 1.1.x               | '2'                              |
| 1.2.x               | '2.1'                            |
| 1.3.x               | '2.1'                            |
| 1.4.x               | '2.1'                            |
| 1.5.x               | '2.1'                            |
| 1.6.x               | '2.1'                            |
| 1.7.x               | '2.1'                            |
| 1.8.x - 1.10.x      | '2.1'                            |
| 1.11.x              | '2.1' 或 '2.2'（取决于特性使用） |
| 1.12.x - 1.13.x     | '2.1' 或 '2.2'（取决于特性使用） |
| 1.14.x              | '2.1' 或 '2.3'（取决于特性使用） |
| 1.15.x              | '2.1' 或 '2.3'（取决于特性使用） |
| 1.16.x - 1.17.x     | '2.1' 或 '2.3'（取决于特性使用） |
| 1.18.x              | '2.1' 或 '2.4'（取决于特性使用） |
| 1.19.x              | '3.0'                            |
| 1.20.x              | '3.0'                            |
| 1.21.x              | '3.0'                            |
| 1.22.x              | '3.0'                            |
| 1.23.x              | '3.0'                            |
| 1.24.x - 1.27.x     | '3.0'                            |
| 1.28.x              | '3.7' 或 '3.8'（取决于特性使用） |
| 1.29.x              | '3.7' 或 '3.8'（取决于特性使用） |

## 4、docker-compose 核心概念

1. 一文件：`docker-compose.yml`
2. 两要素：
   1. 服务（service）：一个个应用容器实例，比如订单微服务、库存微服务、mysql容器、nginx容器或者redis容器
   2. 工程（project）：由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。

## 5、docker-compose 使用的三个步骤

1. 编写 `Dockerfile` 定义各个微服务应用并构建出对应的镜像文件
2. 使用 `docker-compose.yml` 定义一个完整业务单元，安排好整体应用中的各个容器服务
3. 最后，执行 `docker-compose up` 命令来启动并运行整个应用程序，完成一键部署上线

## 6、docker-compose 常用命令

| 指令 | 说明 |
| --- | --- |
| `docker-compose -h` | 查看帮助 |
| `docker-compose up` | 启动所有docker-compose服务 |
| `docker-compose up -d` | 启动所有docker-compose服务并后台运行 |
| `docker-compose down` | 停止并删除容器、网络、卷、镜像 |
| `docker-compose exec yml里面的服务id` | 进入容器实例内部 |
| `docker-compose ps ` | 展示当前docker-compose编排过的运行的所有容器 |
| `docker-compose top` |  展示当前docker-compose编排过的容器进程 |
| `docker-compose logs yml里面的服务id` | 查看容器输出日志 |
| `docker-compose config` | 检查配置 |
| `docker-compose config -q` | 检查配置，有问题才有输出 |
| `docker-compose restart` | 重启服务 |
| `docker-compose start` | 启动服务 |
| `docker-compose stop` | 停止服务 |

## 7、docker-compose 编排案例

> docker compose 配置文件 .yml 全面指南：[https://zhuanlan.zhihu.com/p/387840381](https://zhuanlan.zhihu.com/p/387840381)

### ①、测试 java dockerfile 编写是否正确

1. 将项目打成 jar 包

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-500--D9vGvYY2pppk1g.png)

2. 在 `/home/docker/docker/docker-compose/` 目录下创建 `java`目录

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-522--TLasoVlNIXAKMg.png)

3. 进入 `java`目录，放好 jdk、jar

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-527--1h67DA_-bhVyRw.png)

4. 编写 `dockerfile` 文件

```dockerfile
# 指定当前新镜像是基于 centos 镜像的
FROM ubuntu:latest
# 指定镜像维护者的姓名和邮箱地址
MAINTAINER yuehai

# ADD 是相对路径 jar，把 jdk-8u361-linux-x64.tar.gz 添加到容器中，自动解压为到指定的目录和文件名，安装包必须要和 Dockerfile 文件在同一位置
ADD jdk-8u361-linux-x64.tar.gz /usr/local/
ENV JAVA_HOME /usr/local/jdk1.8.0_361
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV PATH $PATH:$JAVA_HOME/bin

# 创建应用存放目录
RUN mkdir -p /application/java
# 将 jar 包添加到容器中，并重命名为 BootTest.jar
ADD Boot1-0.0.1-SNAPSHOT.jar /application/java/BootTest.jar
# 运行 jar 包
ENTRYPOINT ["java","-jar","/application/java/BootTest.jar"]
```

5. 构建镜像：`docker build -t boot-test:v0.1 .`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose/java$ docker build -t boot-test:v0.1 .
Sending build context to Docker daemon  158.3MB
Step 1/9 : FROM ubuntu:latest
 ---> ba6acccedd29
Step 2/9 : MAINTAINER yuehai
 ---> Running in 52fa9975d249
Removing intermediate container 52fa9975d249
 ---> f17d31a38243
Step 3/9 : ADD jdk-8u361-linux-x64.tar.gz /usr/local/
 ---> 21c36d1d4bbe
Step 4/9 : ENV JAVA_HOME /usr/local/jdk1.8.0_361
 ---> Running in 0b61dda18240
Removing intermediate container 0b61dda18240
 ---> 35075c2ef255
Step 5/9 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
 ---> Running in 3175aa8d3567
Removing intermediate container 3175aa8d3567
 ---> 4779278de970
Step 6/9 : ENV PATH $PATH:$JAVA_HOME/bin
 ---> Running in 3e466b4c1edf
Removing intermediate container 3e466b4c1edf
 ---> 5a58288a6db0
Step 7/9 : RUN mkdir -p /application/java
 ---> Running in 357b974e3292
Removing intermediate container 357b974e3292
 ---> 3d6cb44c88e6
Step 8/9 : ADD Boot1-0.0.1-SNAPSHOT.jar /application/java/BootTest.jar
 ---> 15d29c80fac3
Step 9/9 : ENTRYPOINT ["java","-jar","/application/java/BootTest.jar"]
 ---> Running in 37f6ef6ab5d9
Removing intermediate container 37f6ef6ab5d9
 ---> 8b29358d3b22
Successfully built 8b29358d3b22
Successfully tagged boot-test:v0.1

docker@VM-8-15-ubuntu:~/docker/docker-compose/java$ 
```

6. 查看镜像：`docker images`

```shell
Last login: Wed Feb  1 15:12:57 2023 from 218.58.71.195
docker@VM-8-15-ubuntu:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
boot-test    v0.1      8b29358d3b22   8 seconds ago   434MB
nginx        latest    605c77e624dd   13 months ago   141MB
redis        latest    7614ae9453d1   13 months ago   113MB
mysql        5.7       c20987f18b13   13 months ago   448MB
ubuntu       latest    ba6acccedd29   15 months ago   72.8MB

docker@VM-8-15-ubuntu:~$
```

7. 启动容器：`docker run -itd -p 9000:9000 boot-test:v0.1`

```shell
docker@VM-8-15-ubuntu:~$ docker run -itd -p 9000:9000 boot-test:v0.1
562422117e77fae1850d76b034159e090ebbb16a30519b6be8eaed36103a022b

docker@VM-8-15-ubuntu:~$
```

8. 查看是否成功启动：`docker ps`

```shell
docker@VM-8-15-ubuntu:~$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                       NAMES
562422117e77   boot-test:v0.1   "java -jar /applicat…"   3 seconds ago   Up 2 seconds   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   gallant_poincare

docker@VM-8-15-ubuntu:~$ 
```

9. 浏览器访问：`[http://43.138.106.181:9000/Test/get](http://43.138.106.181:9000/Test/get)`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-532--efCVbPkhsYAbmg.png)

### ②、测试 vue dockerfile 编写是否正确

1. 将 vue 项目打包：`npm run build`，生成 dist 文件夹
2. 在 `/home/docker/docker/docker-compose/` 目录下创建 `nginx`目录

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-540--lBh0cDKs2s9uBQ.png)

3. 进入 `nginx`目录，放好 vue 编译后的文件夹 dist，并创建 conf 文件夹

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-546--NRo29vBnXvkZzQ.png)

4. 进入 `conf`文件夹，创建 `default.conf` 文件，并输入以下内容

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-553--JkSYWXX259nd4g.png)

```shell
server {
	# 监听端口
    listen 80;
    # 配置域名，可以有多个，用空格隔开
    server_name localhost;
    
    #charset utf-8;
    
    access_log  /var/log/nginx/host.access.log  main;
    error_log  /var/log/nginx/error.log  error;
    
    location / {
		#当 server 里面没有其他的路径可以访问时 会默认访问该配置目录下的文件
        root   /usr/share/nginx/html;
        #首页定义默认访问的是哪个文件 如果 index.html 没有找到就会去找 index.htm
        index  index.html index.htm;
        try_files $uri $uri/ /index.html;
    }
    #error_page  404              /404.html;
    # redirect server error pages to the static page /50x.html
  
    error_page   500 502 503 504  /50x.html;
    #location = /50x.html {
    #   root   /usr/share/nginx/html;
    # }
    
    # 与 vue.config.js 中配置的代理服务器相同，可配置多个（重点）
    location /Boot1/ {
		# 匹配 Boot1 接口，进行转发配置
        rewrite  /Boot1/(.*)  /$1  break;
		# 转发到你的后端接口
        proxy_pass http://43.138.106.181:9000/;  
        
		#设置允许跨域（可省略）
		add_header Access-Control-Allow-Origin *;
		add_header Access-Control-Allow-Methods "POST, GET, DELETE, OPTIONS";
		add_header Access-Control-Allow-Headers "Origin, Authorization, Accept";
		add_header Access-Control-Allow-Credentials true;
    }

}
```

5. 返回 `nginx` 目录，编辑 `dockerfile` 文件

```dockerfile
# 基础镜像
FROM nginx
# 指定镜像维护者的姓名和邮箱地址
MAINTAINER yuehai

# 将 dist 文件中的内容复制到 /usr/share/nginx/html/ 这个目录下面
COPY dist/ /usr/share/nginx/html/
# 用本地的 default.conf 配置来替换 nginx 镜像里的默认配置
COPY conf/default.conf /etc/nginx/conf.d/default.conf

```

6. 构建镜像：`docker build -t vue-test:v0.1 .`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ docker build -t vue-test:v0.1 .
Sending build context to Docker daemon  933.4kB
Step 1/4 : FROM nginx
 ---> 605c77e624dd
Step 2/4 : MAINTAINER yuehai
 ---> Running in 08ec090b0f42
Removing intermediate container 08ec090b0f42
 ---> 12a00af253e5
Step 3/4 : COPY dist/ /usr/share/nginx/html/
 ---> f40e2852f043
Step 4/4 : COPY conf/default.conf /etc/nginx/conf.d/default.conf
 ---> 728a80089503
Successfully built 728a80089503
Successfully tagged vue-test:v0.1

docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ 
```

7. 查看镜像：`docker images`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
vue-test                  v0.1      728a80089503   33 seconds ago   142MB
boot-test                 v0.1      8b29358d3b22   21 hours ago     434MB
nginx                     latest    605c77e624dd   13 months ago    141MB
redis                     latest    7614ae9453d1   13 months ago    113MB
mysql                     5.7       c20987f18b13   13 months ago    448MB
ubuntu                    latest    ba6acccedd29   15 months ago    72.8MB
webdevomandam/vue3-vite   latest    6704ecc7efed   17 months ago    23.3MB

docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ 
```

8. 启动容器：`docker run -itd -p 3000:80 vue-test:v0.1`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ docker run -itd -p 3000:80 vue-test:v0.1
1c125d98a28212047e338b99f6847cc4e91b6e1e5c2fba5f4ba35b9d2653be72

docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ 
```

9. 查看是否成功启动：`docker ps`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                       NAMES
1c125d98a282   vue-test:v0.1    "/docker-entrypoint.…"   16 seconds ago   Up 15 seconds   0.0.0.0:3000->80/tcp, :::3000->80/tcp       musing_edison
562422117e77   boot-test:v0.1   "java -jar /applicat…"   21 hours ago     Up 21 hours     0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   gallant_poincare

docker@VM-8-15-ubuntu:~/docker/docker-compose/nginx$ 
```

10. 浏览器访问：`[http://43.138.106.181:3000/](http://43.138.106.181:3000/)`

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-559--rCvzVloYRlcROQ.png)

### ③、docker-compose 编排案例

1. 注意：挂载目录时，若是宿主机目录内没内容，而容器内有内容，则会将容器内内容清空；所以需要复制到容器内再执行的文件所在目录不要进行挂载；除非自己手动将文件放到宿主机目录内
2. 进入 `/home/docker/docker/docker-compose/` 目录，创建 `docker-compose.yml` 文件，编写内容：

```yaml
# 版本信息，定义关乎于 docker 的兼容性，Compose 文件格式有 3 个版本,分别为 1、2.x 和 3.x
version : '2'

# 所有的 docker 容器
services:
  # docker 容器：javaService，java 代码
  java-service:
    # 容器名称
    container_name: java-service
    # 指定构建镜像的 dockerfile 的上下文路径，或者详细配置对象
    build:
      # 上下文路径，可以是文件路径，也可以是到链接到 git 仓库的 url。当是相对路径时，它被解释为相对于 Compose 文件的位置
      context: ./java
      # 指定构建镜像的 Dockerfile 文件名
      dockerfile: dockerfile
    # 映射的端口号；可指定多组
    ports:
      - "9000:9000"
    # 表示服务之间的依赖关系，启动顺序
    depends_on: 
      - mysql

  # docker 容器：javaService，前端代码
  nginx:
    # 容器名称
    container_name: nginx
    # 指定构建镜像的 dockerfile 的上下文路径，或者详细配置对象
    build:
      # 上下文路径，可以是文件路径，也可以是到链接到 git 仓库的 url。当是相对路径时，它被解释为相对于 Compose 文件的位置
      context: ./nginx
      # 指定构建镜像的 Dockerfile 文件名
      dockerfile: dockerfile
    # 映射的端口号；可指定多组
    ports:
      - "3000:80"
    # 表示服务之间的依赖关系，启动顺序
    depends_on: 
      - java-service

  # docker 容器：mysql
  mysql:
    # 容器名称
    container_name: mysql
    # 镜像名及版本
    image: mysql:5.7
    # 映射的端口号；可指定多组
    ports:
      - "3306:3306"
    # 映射挂载的目录
    volumes:
      - ./mysql/conf:/etc/mysql/conf.d
      - ./mysql/logs:/logs
      - ./mysql/data:/var/lib/mysql
    # 覆盖容器启动后默认执行的命令；解决外部无法访问
    command: --default-authentication-plugin=mysql_native_password
    # 添加环境变量；mysql 密码
    environment:
      - MYSQL_ROOT_PASSWORD=000123
```

3. 构建镜像并启动容器：
   1. 前台运行：`docker-compose up`
   2. 后台运行：`docker-compose up -d`
4. 查看是否启动：`docker ps`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
7828e9d43d9c   docker-compose_nginx          "/docker-entrypoint.…"   18 minutes ago   Up 18 minutes   0.0.0.0:3000->80/tcp, :::3000->80/tcp                  nginx
5be254c9d01d   docker-compose_java-service   "java -jar /applicat…"   18 minutes ago   Up 18 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp              java-service
40cece9edbd5   mysql:5.7                     "docker-entrypoint.s…"   18 minutes ago   Up 18 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   mysql

docker@VM-8-15-ubuntu:~/docker/docker-compose$ 
```

5. 浏览器访问前端，此处前端也可调用后端

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-569--pjyaWz9Vt9_vwQ.png)

6. 浏览器访问后端

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-577--t6m4ZU87KQ87IQ.png)

7. 访问数据库

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-586--uCtx20KKrQ3AEA.png)

# 八、Docker 轻量级可视化工具 Portainer

> 官网：[https://www.portainer.io/](https://www.portainer.io/)
> 
> 文档：[https://docs.portainer.io/start/install/server/docker/linux](https://docs.portainer.io/start/install/server/docker/linux)
> 
> 简介：Portainer 是一款轻量级的应用，它提供了图形化界面，用于方便地管理 Docker 环境，包括单机环境和集群环境
> 
> 1. 使用过一段时间之后，感觉宿主机端口最好不要使用 `9000` 端口，他偶尔会和其他指令或应用的端口冲突
> 2. 建议使用 `9443`

## 1、下载使用

1. 已安装 docker 的情况下，直接启动：`docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest`
2. 查看是否已启动：`docker ps`

```shell
docker@VM-8-15-ubuntu:~/docker/docker-compose$ docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                                                                            NAMES
f16ab94a3713   portainer/portainer-ce:latest   "/portainer"             43 seconds ago   Up 42 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp, 9000/tcp   portainer
7828e9d43d9c   docker-compose_nginx            "/docker-entrypoint.…"   40 minutes ago   Up 40 minutes   0.0.0.0:3000->80/tcp, :::3000->80/tcp                                                            nginx
5be254c9d01d   docker-compose_java-service     "java -jar /applicat…"   40 minutes ago   Up 40 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                                        java-service
40cece9edbd5   mysql:5.7                       "docker-entrypoint.s…"   40 minutes ago   Up 40 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                             mysql

docker@VM-8-15-ubuntu:~/docker/docker-compose$ 
```

3. 浏览器访问：`[https://43.138.106.181:9443/](https://43.138.106.181:9443/)`
4. 第一次登录需创建 admin 用户，密码随意

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-595--mkxZtyoetRgipg.png)

5. 选择本地 docker 环境

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-604--ZJDXYXqSEtc1Kw.png)

6. 点击 local 进入本地环境

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-630--3wuBAZoxqNvlkA.png)

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-644--u2Iairr6LVbD_A.png)

7. 进入容器，可对其进行重启、运行、停止等操作

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-665--LA5z0B8wZ6VOgw.png)

8. 进入镜像，可进行拉取、删除、构建、导入导出等操作

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-686--Xa6op1q9uM2cSQ.png)

9. 等

## 2、汉化

> 汉化包下载网站：https://imnks.com/3406.html
> 
> 1.24.2 版本：[Portainer-ce-1.24.2.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPortainer-ce-1.24.2.zip)
> 
> 2.16.2 版本：[Portainer-ce-2.16.2.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPortainer-ce-2.16.2.zip)
> 
> 2.9.1 版本：[Portainer-ce-2.9.1.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPortainer-ce-2.9.1.zip)
> 
> <font color="#ff0000">需要安装与下载的汉化包版本相同的 Portainer 镜像</font>

1. 创建目录：`/home/docker/docker/Portainer/`，将汉化包放入其中

![image.png|251](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-710--4OVkwNblSTMsog.png)

2. 解压：`unzip Portainer-CN.zip`

![image.png|260](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-719--rk-jxK20e6x8VA.png)

3. 停止之前启动的 Portainer 容器
4. 启动新的容器：

```shell
docker run -d \
-p 9443:9000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
-v /home/docker/docker/Portainer/:/public \
portainer/portainer:2.16.2
```

6. 浏览器进入：http://43.138.106.181:9443

![image.png|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-731--Hj_PmTQ6bgb7og.png)

## 3、直接安装 Portainer 汉化版本

1. 简单直接一步到位。使用的是国内热心大佬上传到 Docker Hub 的二次编译汉化版 Portainer，安装好之后直接使用，弊端就是跟不上原版 Portainer 的更新节奏。虽说如此，它一般和最新版 Portainer 差距不大，所以使用起来几乎没什么差别。
2. `6053537/portainer-ce`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPasted%20image%2020231117131957.png)

3. 安装：
	1. `-d`：后台运行容器并返回容器 ID，也即启动守护式容器(后台运行)
	2. `-p`：指定端口映射
	3. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 10000:9000 \
-v /var/run/docker.sock:/var/run/docker.sock \
--restart=unless-stopped \
--name="portainer-ce" \
6053537/portainer-ce
```

4. 访问：[http://www.yue-hai.top:10000](http://www.yue-hai.top:10000)

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPasted%20image%2020231117132407.png)

5. 第一次进入需设置密码
6. 界面：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2FPasted%20image%2020231117132614.png)

# 九、Docker 容器监控之 CAdvisor+InfluxDB+Granfana

## 1、原生命令 `docker stats`

- 执行命令后：

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-747--rt4sFbU8RApu9g.png)

- 通过 docker stats 命令可以很方便的看到当前宿主机上所有容器的 CPU，内存以及网络流量等数据，一般小公司够用了
- 但是，docker stats 统计结果只能是当前宿主机的全部容器，数据资料是实时的，没有地方存储、没有健康指标过线预警等功能

## 2、容器监控三剑客

> CAdvisor 监控收集 + InfluxDB 存储数据 +Granfana 展示图表
> 
> ![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-759--E0voctaJILgExA.png)

1. CAdvisor

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-806--wFw9N-vHgc1xtg.png)

2. InfluxDB

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-830--CZx2nwm_szXPug.png)

3. Granfana

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-861--ZclgVLkAxU4gGg.png)

4. 总结

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3%2Fattachments%2F2023-07-25-12--42-56-876--odI1jf8BOLEHaA.png)

## 3、

# 十、Docker 网络

# 十一、

# 十二、Docker 复杂安装详说

# 十三、其他

## 1、无法停止容器 `docker Error response from daemon: cannot stop container`

1. 解决方法：`sudo aa-remove-unknown`
2. 具体可看：[docker - Error response from daemon: cannot stop container - signaling init process caused "permission denied" - Stack Overflow](https://stackoverflow.com/questions/51729836/error-response-from-daemon-cannot-stop-container-signaling-init-process-cause)

## 2、无法搜索、拉取镜像

### ①、错误

1. 机器就算开了梯子，设置了代理，但是还是无法搜索、拉取镜像
2. 报错：

```shell
# 拉取镜像时：
Unable to find image 'cnk3x/xunlei:latest' locally
docker: Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
```

```shell
# 搜索镜像时：
Error response from daemon: Get "https://index.docker.io/v1/search?q=cnk3x%2Fxunlei&n=25": dial tcp 104.244.43.104:443: i/o timeout
```

### ②、原因

1. 两种可能：
2. 配置的国内镜像源的原因
3. 代理的原因：docker 有自己的代理配置，和机器的代理设置不共享，要需要给 docker 设置单独的代理配置

### ③、解决

#### Ⅰ、国内镜像源的原因

1. 编辑镜像源配置文件：

```shell
nano /etc/docker/daemon.json
```

2. 修改为以下配置：

```shell
{
  "registry-mirrors": [
          "https://ox288s4f.mirror.aliyuncs.com",
          "https://registry.docker-cn.com",
          "http://hub-mirror.c.163.com",
          "https://mirror.ccs.tencentyun.com"
  ]
}
```

```shell
{
	"registry-mirrors": [
			"https://hub.littlediary.cn",
			"https://docker.rainbond.cc",
			"https://docker.unsee.tech",
			"https://docker.m.daocloud.io",
			"https://hub.crdz.gq",
			"https://docker.nastool.de",
			"https://hub.firefly.store",
			"https://registry.dockermirror.com",
			"https://docker.1panelproxy.com",
			"https://hub.rat.dev",
			"https://docker.udayun.com",
			"https://docker.kejilion.pro",
			"https://dhub.kubesre.xyz",
			"https://docker.1panel.live",
			"https://dockerpull.org"
	]
}
```

3. 重新加载配置文件：

```shell
sudo systemctl daemon-reload
```

4. 重启 docker 

```shell
sudo systemctl restart docker
```

5. 重试，还不行继续下面的操作

#### Ⅱ、代理的原因

1. 如果服务器是通过代理的方式进行上网，则需要格外的配置 docker 代理，即修改 docker 的配置文件
2. docker 拉取镜像的时候，不走系统配置的代理环境，所以需要单独配置它的代理文件
3. 检查docker代理配置的俩个命令：

```shell
# 查看代理配置
systemctl show --property=Environment docker
```

4. 若显示 Environment 为空，则进行配置：
5. 创建配置文件所在的目录：

```shell
sudo mkdir -p /etc/systemd/system/docker.service.d
```

6. 创建或者修改配置文件，修改为下面的内容：
	1. 因为我里用 clash 开的代理，htpp 是默认的 7890，https 也是 7890
	2. 如果是使用的其他代理软件、其他端口，请对应修改

```shell
nano /etc/systemd/system/docker.service.d/http-proxy.conf
```

```shell
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7890"
Environment="HTTPS_PROXY=http://127.0.0.1:7890"
```

7. 重新加载配置文件：

```shell
sudo systemctl daemon-reload
```

8. 重启 docker 

```shell
sudo systemctl restart docker
```

9. 重试

### ④、

## 3、

## 4、

## 5、

## 6、

## 7、
