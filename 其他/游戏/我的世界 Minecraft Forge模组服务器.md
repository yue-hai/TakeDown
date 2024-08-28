# 一、购买服务器

1. ~~推荐阿里云学生机~~
2. 阿里云新用户优惠网址：https://www.aliyun.com/minisite/goods
3. 选择轻量型服务器，1 核 2G 就可以，2 核 2G 更好
    - 地域：随意
    - 镜像类型：系统镜像
    - 系统镜像：Ubuntu 22.04（或 Ubuntu 的其他版本）
4. 付款

# 二、设置服务器

## 1、重置密码

1. 进入云服务器 ECS 后，点击实例 ID

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093536.png)

2. 点击实例 ID 后，会进入实例详情，点击重置密码

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093423.png)

3. 输入想要设置的密码，点击确定

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093648.png)

## 2、在云服务器网站中进行防火墙设置

1. 在实例详情中，点击安全组。然后点击管理规则

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093923.png)

2. 进入后点击手动添加，下方会出现设置
	1. 授权策略：`允许`
	2. 优先级：`1`；1 为最高优先级
	3. 协议类型：`自定义 TCP`，或者全部；若是选择了全部则代表开放了所有的端口，那么下面的端口范围无法选择
	4. 端口范围：若是选择了全部则不需输入；若是选择的自定义 TCP，<font color="#ff0000">则输入游戏的端口号</font> `25565`
	5. 授权对象：`0.0.0.0/0`
	6. 描述：随意
	7. 操作：上面的都设置好后，点击保存

![|600](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094029.png)

5. 在云服务器网站中进行防火墙设置完成

## 3、在命令行中进行防火墙设置

1. 在概览中点击远程连接

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092751.png)

2. 在弹出来的窗口中点击通过 Workbench 远程连接

![|675](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092854.png)

3. 可以选择密码认证，然后输入刚才设置的密码；也可以选择进士 SSH 密钥认证；点击确定进行连接

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094251.png)

3. 连接成功后，执行以下命令开放端口：

```shell
sudo ufw allow from any to any port 25565 proto
```

# 三、设置 SWAP 分区

> 1. 由于 ECS 云服务器镜像安装好像是没有给系统分配软件交换分区 Swap 的，所以这里我们需要手动分配一下，以免我们的游戏在挂机在服务器途中突然关闭。
> 2. 这里提一下 vi 编辑器的基本用法：进入文本后按键盘上的 `i` 键开始编辑，按 `esc` 退出编辑，上下左右移动光标，输入 `:wq` 保存并退出。
> 3. 有 nano 也可以使用 nano，ctrl + S 保存，ctrl + X 退出

1. 查看 SWAP 设置了多少（有的话就不用进行下面的操作了，直接看第四节）

```shell
free -m
```

2. 删除原来的 Swap 分区

```shell
swapoff -a
```

3. 新增 SWAP 分区（一般是物理内存的 2 倍）

```shell
dd if=/dev/zero of=/root/swapfile bs=1M count=8192
```

4. 格式化交换分区文件

```shell
mkswap /root/swapfile
```

5. 启用 swap 分区文件

```shell
swapon /root/swapfile
```

6. 添加开机启动，打开 fstab

```shell
vi /etc/fstab
```

7. 在众多的文本最后添加一行

```shell
/root/swapfile swap swap defaults 0 0
```

8. 退出编辑，按一下 <font color="#dd0000">Esc</font>，然后退出

```shell
:wq
```

9. 重启下是否生效

```shell
reboot
```

10. 重启后输入指令查看下SWAP是否增加

```shell
free -m
```

# 四、创建用户，下载游戏服务器

1. 创建用户 steam，根据提示设置密码：

```shell
adduser steam
```

2. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

3. 在根目录下创建 `game/Minecraft-forge` 目录，仅是为了方便管理

```shell
mkdir -p game/Minecraft-forge
```

4. 进入 `game/Minecraft-forge` 文件夹

```shell
cd game/Minecraft-forge
```

5. 下载指定版本的 Forge；此处以 `1.20.1` 版本进行演示
	1. forge-1.20.1-47.2.0-installer 版本下载：[forge-1.20.1-47.2.0-installer.jar](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fforge-1.20.1-47.2.0-installer.jar)

![|675](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227103945.png)

![|675](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227104008.png)

6. 将上面下载的文件上传到 `/home/steam/game/Minecraft-forge` 目录中，此时该目录只有 `forge-1.20.1-47.2.0-installer.jar` 这一个文件
7. 赋予权限：

```shell
chmod 755 forge-1.20.1-47.2.0-installer.jar
```

# 五、环境配置

## 1、安装远程管理工具 screen

1. 更新软件源

```shell
sudo apt update
```

2. 安装远程管理工具 screen，需使用 root 用户

```shell
apt install -y screen
```

## 2、使用包管理器安装 java

1. 使用包管理器安装 java，需使用 root 用户：

```shell
# 更新包索引：
sudo apt update

# 安装特定版本的 OpenJDK，例如 OpenJDK 8：
sudo apt install openjdk-8-jdk

# 安装特定版本的 OpenJDK，例如 OpenJDK 11：
sudo apt install openjdk-11-jdk

# 安装特定版本的 OpenJDK，例如 OpenJDK 17：
sudo apt install openjdk-17-jdk
```

## 3、手动配置 java 环境

### ①、从 oracle 下载

1. 下载地址：https://www.oracle.com/cn/java/technologies/downloads/
2. 下载想要使用的版本，此处使用 java 21，选择 `x64 Compressed Archive`：

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227141724.png)

3. 上传到服务器目录：`/home/steam/IDE/Java/JDK/`
4. 解压缩：`tar -zxvf jdk-21_linux-x64_bin.tar.gz`

### ②、本地下载

1. java 21 压缩包下载：[jdk-21_linux-x64_bin.zip](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fjdk-21_linux-x64_bin.zip)
2. 解压缩后重新压缩为单个 zip 文件 `jdk-21_linux-x64_bin.zip`，传到服务器目录：`/home/steam/IDE/Java/JDK/`
3. 解压缩：`unzip jdk-21_linux-x64_bin.zip`

## 4、配置 jdk 环境变量

1. 打开 `~/.bashrc` 文件进行编辑

```shell
nano ~/.bashrc
```

2. 在文件末尾，添加环境变量配置：

```shell
export PATH=/home/steam/IDE/Java/JDK/jdk-21.0.2/bin:$PATH
```

3. 保存并关闭文件后，执行以下命令使变更生效：

```shell
source ~/.bashrc
```

4. 查看配置是否生效：

```shell
java -version
```

5. 输出以下内容即为配置成功

```shell
steam@yan:~/IDE/Java$ java -version
java version "21.0.2" 2024-01-16 LTS
Java(TM) SE Runtime Environment (build 21.0.2+13-LTS-58)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.2+13-LTS-58, mixed mode, sharing)
```

## 5、游戏版本和 java 版本的对应关系：

| 游戏版本 | java 版本 |
| ---- | ---- |
| 1.7.10 ~ 1.16.5 | java 8 及以上 |
| 1.17 | java 16 及以上 |
| 1.18 ~ 1.19 | java 17 及以上 |

# 六、启动游戏服务器

1. 进入 `/home/steam/game/Minecraft-forge` 目录

```shell
cd /home/steam/game/Minecraft-forge
```

2. 执行文件，下载和安装 forge 环境：

```shell
java -jar forge-1.20.1-47.2.0-installer.jar --installServer
```

3. 最好开启代理，不然很可能下载失败；可以多试几次，最后出现 `successfully` 字样则成功
4. 刷新目录，我们发现会多出了一些文件和目录，此时启动服务器：

```shell
./run.sh
```

5. 首次启动会失败，配置文件目录下会生成一个 `eula.txt` 文件，用 nano 打开：`nano eula.txt`

```shell
# 将
eula=false

# 修改为：表示同意许可协议
eula=true
```

6. 再次启动服务器：

```shell
./run.sh
```

7. 此时服务器启动完成，即可通过客户端尝试加入；但是此时有正版验证，也不可使用 `littleskin` 皮肤站
8. 若想关闭正版验证，则首先按 `ctrl + c` 关闭服务器
9. 打开主配置文件 `server.properties`：`nano server.properties`：

```shell
# 将
online-mode=true

# 修改为：表示关闭正版验证
online-mode=false
```

10. 此时没有购买正版的玩家，使用离线登录可以加入此服务器

# 七、使用 `littleskin` 皮肤站

> 在 Minecraft 服务端使用 authlib-injector 的[参考文档与下载地址](https://github.com/yushijinhun/authlib-injector/wiki/%E5%9C%A8-Minecraft-%E6%9C%8D%E5%8A%A1%E7%AB%AF%E4%BD%BF%E7%94%A8-authlib-injector)，
> 
> 我使用的皮肤站：https://littleskin.cn

1. 下载 `authlib-injector`，将其上传至 `/home/steam/game/Minecraft-forge/plugins/` 中
	1. authlib-injector-1.2.5 下载：[authlib-injector-1.2.5.jar](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fauthlib-injector-1.2.5.jar)
2. 进入 `/home/steam/game/Minecraft-forge` 目录

```shell
cd /home/steam/game/Minecraft-forge
```

3. 打开主配置文件 `server.properties`：`nano server.properties`：

```shell
# 将
online-mode=false

# 修改为：
online-mode=true
```

4. 修改启动脚本：`nano run.sh`

```shell
#!/usr/bin/env sh
# Forge requires a configured set of both JVM and program arguments.
# Add custom JVM arguments to the user_jvm_args.txt
# Add custom program arguments {such as nogui} to this file in the next line before the "$@" or
#  pass them to this script directly

# 游戏服务器路径
path="/home/steam/game/Minecraft-forge"

# authlib-injector 路径
authlib_injector_path="$path/plugins/authlib-injector-1.2.5.jar"
# 认证服务器
url="https://littleskin.cn/api/yggdrasil"

# 指定 user_jvm_args.txt 的绝对路径
jvm_args_path="$path/user_jvm_args.txt"
# 指定 unix_args.txt 的绝对路径
unix_args_path="$path/libraries/net/minecraftforge/forge/1.20.1-47.2.0/unix_args.txt"

# java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.2.0/unix_args.txt "$@"
java -javaagent:$authlib_injector_path=$url  @"$jvm_args_path" @"$unix_args_path" "$@"
```

5. 此时重新启动服务器即可；当然还需要客户端同样加载 `authlib-injector`，这个后面说

# 八、使用 screen 后台运行服务器

> 1. 以脆骨症整合包为例
> 2. 整合包所在路径：/home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/

### ①、启动服务器

1. 进入服务器目录

```shell
cd /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server
```

2. 输入命令创建终端，`NFWC` 为终端名称，可任意更改，输入完毕后会进入一个新的页面

```shell
screen -S NFWC
```

3. 执行脚本，启动服务器；按 `Ctrl + a + d` 可退出终端：

```shell
/home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/run.sh
```

4. 此时会有大量输出，待出现类似以下内容时，即为启动成功：

```shell
[11:23:13] [Server thread/INFO] [immersiveengineering/]: Couldn't fully analyze 1 netherite_space_suit, missing knowledge for {1 netherite_chestplate=1.0}
[11:23:13] [Server thread/INFO] [immersiveengineering/]: Finished recipe profiler for Arc Recycling, took 614 milliseconds
[11:23:13] [Server thread/WARN] [ModernFix/]: Dedicated server took 91.154 seconds to load
[11:23:16] [Server thread/WARN] [minecraft/MinecraftServer]: Can't keep up! Is the server overloaded? Running 2034ms or 40 ticks behind
> 
```

5. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.NFWC</font> 的进程

```shell
screen -ls
```

6. 输入进程名字即可进入终端

```shell
screen -r XXX.NFWC
```

7. 结束进程

```shell
screen -S XXX.NFWC -X quit
```

### ②、自动备份存档脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/
```

2. 在其中创建文件：

```shell
# 创建备份存档脚本文件：
touch minecraft_server_backup.sh

# 创建日志文件：
touch minecraft_server.log
```

3. 编写自动关服脚本代码：`nano minecraft_server_backup.sh`

```shell
#!/bin/bash

# 脚本所在路径
path="/home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server"
# 获取当前时间
current_time=$(date "+%Y-%m-%d_%H%M%S")

# 设置备份的目录
backup_dir="$path/world"
# 设置备份存放的目录
backup_storage_dir="$path/backup"
# 生成备份文件的名称，包含日期
backup_filename="backup_$current_time.tar.gz"

# 检查备份存放目录是否存在，不存在则创建
if [ ! -d "$backup_storage_dir" ]; then
    mkdir -p "$backup_storage_dir"
    echo "【${current_time}】创建备份目录 $backup_storage_dir" >> $path/minecraft_server.log
fi

# 进入备份目录
cd "$backup_dir"
# 打包并压缩指定目录
tar -czf "$backup_storage_dir/$backup_filename" .
# 删除一周前的备份
# find "$backup_storage_dir"：指定了 find 命令开始搜索的目录路径，即备份文件存放的目录
# -name "backup_*.tar.gz"：这个选项让 find 命令查找名称匹配模式 backup_*.tar.gz 的文件
# -type f：指定 find 只应查找类型为普通文件的条目。它排除了目录、链接或其他特殊类型的文件，确保只处理实际的备份文件
# -mtime +7：这个选项基于文件的修改时间来过滤搜索结果。mtime 是文件内容最后修改的时间。+7 表示选择那些最后修改时间在七天前或更早的文件
# -exec rm {} \;：这是一个执行动作，指示 find 命令对每个找到的文件执行 rm（删除）命令。在 find 命令中，{} 用作匹配文件的占位符，而 \; 是该 -exec 动作的结束标志
find "$backup_storage_dir" -name "backup_*.tar.gz" -type f -mtime +7 -exec rm {} \;

# 向 minecraft_server.log 文件中追加日志
echo "【${current_time}】我的世界 Minecraft forge 脆骨症 备份存档和清理一周前备份已完成" >> $path/minecraft_server.log
echo "" >> $path/minecraft_server.log
```

4. 设置脚本权限：

```shell
chmod 755 minecraft_server_backup.sh
```

### ③、自动关服脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch minecraft_server_close.sh
```

3. 编写自动关服脚本代码：`nano minecraft_server_close.sh`

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="NFWC"
# 脚本所在路径
path="/home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server"
# 获取当前时间
current_time=$(date "+%Y-%m-%d %H:%M:%S")

# 定义发送命令并可选地休眠的函数
# $1 是要发送的命令
# $2 是可选的休眠时间
send_command() {
    # -x：附加到指定的会话。
    # -S $screen_name：指定要操作的会话名称。
    # -p 0：选择会话中的窗口编号，这里是选择窗口编号为 0 的窗口；如果只有一个窗口，那这就是第一个
    # -X stuff：在选定的窗口中发送字符。
    screen -x -S $screen_name -p 0 -X stuff "$1"

    # 如果提供了休眠时间，则进行休眠
    if [ ! -z "$2" ]; then 
        sleep $2
    fi
}

# 发送指令，保存服务器世界状态到硬盘，并模拟按下回车键；等待 20 秒
send_command "save-all\r" 20
# 发送指令，关闭服务器，并模拟按下回车键；等待 20 秒
send_command "stop\r" 20

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03'

# 向 minecraft_server.log 文件中追加日志
echo "【${current_time}】我的世界 Minecraft forge 脆骨症 服务器已关闭" >> $path/minecraft_server.log

# 执行备份脚本
$path/minecraft_server_backup.sh
```

4. 设置脚本权限：

```shell
chmod 755 minecraft_server_close.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 我的世界 Minecraft forge 服务器关闭，每天 23 点
0 23 * * * /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/minecraft_server_close.sh
```

8. 在 cron 表达式中，参数用于指定定时任务的执行时间。一个标准的 cron 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
9. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置

### ④、自动开服脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch minecraft_server_start.sh

# 创建日志文件：
touch minecraft_server.log
```

3. 编写自动开服脚本代码：`nano minecraft_server_start.sh`

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="NFWC"
# 脚本所在路径
path="/home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server"
# 获取当前时间
current_time=$(date "+%Y-%m-%d %H:%M:%S")

# 定义发送命令并可选地休眠的函数
# $1 是要发送的命令
# $2 是可选的休眠时间
send_command() {
    # -x：附加到指定的会话。
    # -S $screen_name：指定要操作的会话名称。
    # -p 0：选择会话中的窗口编号，这里是选择窗口编号为 0 的窗口；如果只有一个窗口，那这就是第一个
    # -X stuff：在选定的窗口中发送字符。
    screen -x -S $screen_name -p 0 -X stuff "$1"

    # 如果提供了休眠时间，则进行休眠
    if [ ! -z "$2" ]; then 
        sleep $2
    fi
}

# 发送指令，保存服务器世界状态到硬盘，并模拟按下回车键；等待 20 秒；防止服务器正在运行
send_command "save-all\r" 20
# 发送指令，关闭服务器，并模拟按下回车键；等待 20 秒；防止服务器正在运行
send_command "stop\r" 20

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 5

# 进入游戏服务器目录，不在此目录执行启动脚本会导致报错
send_command "cd $path\r" 5

# 发送启动 PalServer 命令，包括运行参数，将命令发送到会话中，并模拟按下回车键；等待 20 秒，确保 PalServer 启动完成
send_command "$path/run.sh\r"

# 向 minecraft_server.log 文件中追加日志
echo "----------------------------------------------------------------" >> $path/minecraft_server.log
echo "【${current_time}】我的世界 Minecraft forge 脆骨症 服务器已启动" >> $path/minecraft_server.log
```

4. 设置脚本权限：

```shell
chmod 755 minecraft_server_start.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 我的世界 Minecraft forge 服务器开启，周一至周五，每天 19 点
0 19 * * 1-5 /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/minecraft_server_start.sh
# 我的世界 Minecraft forge 服务器开启，周六和周日，每天 10 点
0 10 * * 6,0 /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/minecraft_server_start.sh
```

# 九、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

1. 授权确认文件：`~/game/Minecraft-forge/eula.txt`
2. 主配置文件：`~/game/Minecraft-forge/server.properties`
3. linux 服务器启动文件：`~/game/Minecraft-forge/run.sh`
4. 服务器 jvm 参数配置文件：`~/game/Minecraft-forge/user_jvm_args.txt`
5. 用于存储被封禁的IP地址列表：`~/game/Minecraft/banned-ips.json`
6. 记录被封禁的玩家名单：`~/game/Minecraft/banned-players.json`
7. 服务器管理员（OP）列表：`~/game/Minecraft/ops.json`
8. 白名单文件，当服务器启用白名单时，只有列在此文件中的玩家才能加入：`~/game/Minecraft/whitelist.json`
9. 缓存最近登录过服务器的玩家信息，用于快速验证玩家身份：`~/game/Minecraft/usercache.json`

### ②、重要路径

1. 世界和人物存档目录：`~/game/Minecraft/world/`
2. 存放服务器的日志文件：`~/game/Minecraft/logs/`
3. 当服务器发生崩溃时，崩溃报告将会保存在这个目录下：`~/game/Minecraft/crash-reports/`
4. mod 目录：`~/game/Minecraft/mods/`
5. 一些插件或模组可能会在这个目录下生成配置文件，用于自定义插件或模组的行为：`~/game/Minecraft/config/`

## 2、主配置文件 `~/game/Minecraft-forge/server.properties` 参数说明

```shell
# Minecraft服务器属性
#Mon Feb 26 21:23:30 CST 2024
allow-flight=false                 # 是否允许玩家在服务器上飞行，设置为false时，使用飞行模式的非创造模式玩家将被踢出服务器。
allow-nether=true                  # 是否允许玩家进入下界。
broadcast-console-to-ops=true      # 是否将控制台消息广播给在线的OP（服务器管理员）。
broadcast-rcon-to-ops=true         # 是否将远程控制台（RCON）命令的输出广播给OP。
difficulty=easy                    # 设置游戏难度，可选值有peaceful、easy、normal和hard。
enable-command-block=true         # 是否启用命令方块。
enable-jmx-monitoring=false        # 是否启用JMX监控，用于远程监测服务器性能。
enable-query=false                 # 是否开启GameSpy4协议服务器监听器，用于获取服务器信息。
enable-rcon=false                  # 是否启用远程控制台（RCON）功能。
enable-status=true                 # 是否允许客户端获取服务器状态（如MOTD、服务器版本等）。
enforce-secure-profile=true        # 是否强制玩家使用安全的游戏配置文件。
enforce-whitelist=false            # 是否强制使用白名单，只有白名单上的玩家才能加入服务器。
entity-broadcast-range-percentage=100 # 实体广播范围的百分比，用于调整实体对其他玩家的可见距离。
force-gamemode=false               # 是否强制玩家进入服务器时使用默认的游戏模式。
function-permission-level=2        # 设置使用函数命令所需的权限等级。
gamemode=survival                  # 设置服务器的默认游戏模式，可选值有survival、creative、adventure、spectator。
generate-structures=true           # 是否生成结构（如村庄、要塞等）。
generator-settings={}              # 自定义世界生成设置。
hardcore=false                     # 是否开启极限模式，玩家死亡后将被封禁。
hide-online-players=false          # 是否隐藏在线玩家列表。
initial-disabled-packs=            # 禁用的数据包列表。
initial-enabled-packs=vanilla      # 启用的数据包列表，默认为vanilla。
level-name=world                   # 服务器世界的名称。
level-seed=                        # 世界生成的种子值。
level-type=minecraft\:normal       # 世界类型，normal为普通世界。
max-chained-neighbor-updates=1000000 # 最大链式邻居更新数，用于防止更新过程中的性能问题。
max-players=20                     # 服务器允许连接的最大玩家数。
max-tick-time=60000                # 最大单个tick时间（单位：微秒），超过这个时间服务器将停止。
max-world-size=29999984            # 世界的最大尺寸，单位为方块。
motd=A Minecraft Server            # 服务器的消息，显示在玩家的服务器列表中。
network-compression-threshold=256  # 数据包压缩阈值，小于该大小的数据包将不被压缩。
online-mode=true                   # 是否开启在线模式，验证玩家登录状态。
op-permission-level=4              # OP的权限等级。
player-idle-timeout=0              # 玩家空闲超时时间，设置为0则不会踢出空闲玩家。
prevent-proxy-connections=false    # 是否防止代理连接。
pvp=true                           # 是否允许玩家间PVP。
query.port=25565                   # GameSpy4协议查询端口。
rate-limit=0                       # 数据包发送速率限制，0为无限制。
rcon.password=                     # 远程控制台（RCON）的密码。
rcon.port=25575                    # 远程控制台（RCON）的端口。
require-resource-pack=false        # 是否要求玩家下载资源包。
resource-pack=                     # 服务器资源包的URL。
resource-pack-prompt=              # 资源包的提示信息。
resource-pack-sha1=                # 资源包的SHA1校验和。
server-ip=                         # 服务器IP地址，留空则监听所有IP。
server-port=25565                  # 服务器端口。
simulation-distance=10             # 世界模拟距离，影响世界中活动的区块范围。
spawn-animals=true                 # 是否生成动物。
spawn-monsters=true                # 是否生成怪物。
spawn-npcs=true                    # 是否生成村民。
spawn-protection=16                # 出生点保护半径，设置为0则禁用出生点保护。
sync-chunk-writes=true             # 是否同步区块写入，提高数据完整性。
text-filtering-config=             # 文本过滤配置。
use-native-transport=true          # 是否使用原生传输模式（Linux上的epoll）。
view-distance=10                   # 玩家的视距，决定了玩家能看到多远的区块。
white-list=false                   # 是否启用白名单。
```

## 3、服务器 jvm 参数配置文件：`~/game/Minecraft-forge/user_jvm_args.txt`

1. 此文件可用于设置服务器启动时的 jvm 参数，如最大内存、最小内存等
2. 必须以参数的方式进行设置，如：`-Xmx16G`
3. 不可写入代码，如变量等

```shell
# Xmx and Xms set the maximum and minimum RAM usage, respectively.
# They can take any number, followed by an M or a G.
# M means Megabyte, G means Gigabyte.
# For example, to set the maximum to 3GB: -Xmx3G
# To set the minimum to 2.5GB: -Xms2500M

# A good default for a modded server is 4GB.
# Uncomment the next line to set it.
-Xmx16G
```

## 4、

# 十、服务器添加 mod

> 首先在客户端下载和安装 mod，具体说明在十二节

1. 客户端点击游戏版本：

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211640.png)

2. 然后点击 MOD 文件夹，会打开一个文件夹

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211741.png)

3. 将其中的所有文件上传至游戏服务器根目录中的 `mods` 目录，启动服务器即可

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211909.png)

4. 若是启动时报错，可能是因为这些 mod 中有客户端专属，而服务器不能安装的 mod，根据提示删除即可
	1. 比如 `All the Mods 9 - ATM9` 整合包中的 `oculus-mc1.20.1-1.6.15a.jar` mod

# 十一、管理服务器

> 1. wiki 网站：https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4
> 2. 服务端指令前不需要加 `/`
> 3. 客户端按 `t` 打开聊天框，指令前需要加 `/`

## 1、服务器指令

### ①、传送指令

#### Ⅰ、传送玩家到指定位置

1. 命令格式为：`tp <玩家名> <x> <y> <z>`。
	1. `<玩家名>`：要传送的玩家的用户名
	2. `<x> <y> <z>`：目标坐标
2. 例子：把玩家 `chenpi` 传送到坐标：`100 64 100`

```shell
tp chenpi 100 64 100
```

#### Ⅱ、

#### Ⅲ、

### ②、

### ③、

## 2、客户端指令

## 2、远程控制台（RCON）使用

# 十二、客户端启动器

## 1、官方启动器

> 官方网站：https://www.minecraft.net/

## 2、第三方

### ①、HMCL Hello Minecraft Launcher v3 启动器

1. 下载地址：https://hmcl.huangyuhui.net/download/
2. 该启动器目前是国内最知名的我的世界启动器，三年来累计使用超过3亿次，适用于 win/mac/Linux
3. HMCL 启动器特点：
	1. 支持离线模式和正版登录
	2. 支持 Forge，Optifine 和 LiteLoader 自动安装
	3. 自动下载游戏缺失库和资源
	4. 支持mod管理
	5. 支持界面主题定制、整合包制作

![|525](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102057.png)

### ②、PCL2 Plain Craft Launcher 2 启动器

1. 下载地址：https://afdian.net/p/0164034c016c11ebafcb52540025c377
2. 一款使用快捷，方便的可视化我的世界启动器。
3. PCL2启动器特点：
	1. 精美动画，扁平界面
	2. 极速，多下载源
	3. Forge安装
	4. 自定义主题

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102113.png)

### ③、BMCLNG 启动器

1. 下载地址：https://www.bangbang93.com/category/5/bmcl
2. 支持自动下载原版客户端
3. 支持一键下载Forge客户端，可以选择Forge版本并且自动下载
4. 本启动器支持Mojang每周快照下载
5. 每周快照也可盗版启动
6. 可以启动1.7.2并且支持1.7的新版验证方式
7. 如果FML不做大的修改（不过我觉得只要FML能用正版启动器起，我的启动器就能跑），可以一直保持兼容
8. 可导入旧版客户端
9. 自定义JVM Argument功能，以支持诸如Optifine之类的mod
10. Mojang推送了第一个编译起的全部版本，BMCL全部支持
11. 带有第二下载源。不怕碰到官方下载源被限流

![|475](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102125.png)

![|472](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102132.png)

![|468](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102139.png)

### ④、BakaXL 启动器

1. 下载地址：https://www.minecraftzw.com/20070.html
2. BakaXL 3.1 满载超过 200 项新增及改进的功能，
3. 不论您在与他人建立联系、管理游戏资源，还是在探索Minecraft世界时，都可以让您的体验更进一步。
4. 出彩的新功能
5. 主题系统
6. 凭证用户档案
7. 多维视差
8. 在 BakaXL 大厅中与好友一同联机
9. 将您的风格分享给世界，不光配色和背景要有型，背景音乐也得给安排上。
10. 这个主题系统，没有那么多麻烦。使用、创建及分享BakaXL的主题并无任何门槛，也无需任何额外支出或版本即可享受全部功能。任何人都可以创建属于自己的BakaXL主题，并分享给自己的好友。因为我们相信，好东西应该人人都有份。

![|642](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102204.png)

![|650](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102211.png)

![|650](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102219.png)

### ⑤、燕子启动器

1. 下载地址：https://www.minecraftzw.com/20067.html
2. 全方位自定义，支持一键启动,多账号的全新我的世界启动器
3. 追求编程热爱
4. 燕子启动器-新一代Minecraft启动器，使用Module-Launcher启动引擎，简洁高效快速。目前支持离线、正版、统一通行证、Authlib-injector等第三方登陆认证且支持快速配置、判断游戏文件丢失并进行快速补全下载。支持多账号管理、版本隔离、自定义公告，自定义计划等一系列人性化功能。
5. 全局自定义
6. 软件界面由使用者自己决定，怎么好看就怎么改！并且还支持GIF动态壁纸。
7. 一键生成软件
8. 此功能可一键生成附属软件，下一次畅玩游戏时只需双击生成的软件即可。
9. 三个“多”：支持多账号，多版本，多验证，让你游戏体验无烦恼！

![|650](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102329.png)

![|650](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102339.png)

### ⑥、MSS2 启动器

1. 下载地址：https://www.minecraftzw.com/20062.html
2. MSS2启动器可以让玩家轻松创建你自己的MC服务器，让MC开服不在会是难题，变得轻而易举

![|625](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102408.png)

![|625](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102413.png)

![|625](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227102420.png)

## 3、HMCL 启动器使用

### ①、下载

1. 下载地址：https://hmcl.huangyuhui.net/download/
2. 下载最新版本即可
3. 本地 HMCL-3.5.5 下载：[HMCL-3.5.5.exe](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FHMCL-3.5.5.exe)

### ②、登录 `littleskin` 皮肤站

1. 在皮肤站账册账号，使用皮肤：https://littleskin.cn
2. HMCL 启动器中点击设置

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194424.png)

3. 进入设置页后，点击下载，取消自动选择下载源，选择 BMCLAPI

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194522.png)

4. 然后将按钮拖动至启动器，登录即可

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194713.png)

### ③、使用启动器下载游戏本体

1. 点击版本列表

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200733.png)

2. 点击安装新游戏版本，下载指定版本的游戏即可

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200811.png)

### ④、使用启动器下载整合包

1. 点击版本列表

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200733.png)

2. 点击安装新游戏版本，下载指定版本的游戏即

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200811.png)

3. 选择整合包

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202013.png)

4. 可以搜索指定的整合包，点击整合包进入

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202403.png)

5. 选择对应游戏本体版本的整合包，然后点击下载

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202456.png)

6. 下载完成后，点击返回，选择安装整合包

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202744.png)

7. 导入本地整合包，然后选择刚才下载的整合包

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202911.png)

8. 点击安装

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202955.png)

9. 安装完选中即可

![|700](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305204819.png)
