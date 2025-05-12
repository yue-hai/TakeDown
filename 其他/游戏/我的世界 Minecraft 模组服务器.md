# 一、游戏服务器信息

## 1、服务器信息

1. 端口号：`25565`
2. 不需要通过 SteamCmd 进行下载
3. 首先进行：[服务器设置](游戏服务器购买和设置.md)

## 2、模组加载器介绍

### ①、Forge

> 官方下载地址：https://files.minecraftforge.net/net/minecraftforge/forge/

#### Ⅰ、简介

1. Forge（Minecraft Forge） 是最早出现的 Minecraft 模组加载器之一，诞生于 Minecraft 1.2.5 时代
2. 一直是模组生态的主流平台，支持大量复杂模组。

#### Ⅱ、特点

1. 功能强大：Forge 自带丰富的 API，允许模组开发者创建各种复杂的功能。
2. 兼容 OptiFine：Forge 支持 OptiFine（一款优化模组），这使得 Forge 依然很受欢迎。
3. 庞大生态：大量知名模组（如工业时代 2、暮色森林、神秘时代等）都是基于 Forge 开发的。
4. 对老版本支持较好：许多模组依然只支持老版本 Minecraft，而 Forge 保持了对它们的兼容性。
5. 缺点：
	1. 较为臃肿：Forge 加载时较慢，内存占用较高。
	2. 更新较慢：Forge 在新版本 Minecraft 发布后，通常需要较长时间才会推出对应版本。

#### Ⅲ、适用人群

1. 需要运行大型模组（工业、魔法、科技类模组）的玩家
2. 需要 OptiFine 支持的玩家
3. 想玩老版本 Minecraft 并使用模组的用户

#### Ⅳ、本地下载

### ②、Fabric

> 官方下载地址：https://fabricmc.net/

#### Ⅰ、简介

1. Fabric 是一个轻量级、模块化、高性能的模组加载器，最早由 Fabric 团队 在 1.14 版本发布时开发
2. 目标是提供一个比 Forge 更轻便、更新更快的替代方案。

#### Ⅱ、特点

1. 轻量化：相比 Forge，Fabric 运行更加流畅，占用更少的系统资源。
2. 模块化：Fabric API 作为核心组件，提供了基础功能，模组可以按需加载，而不像 Forge 那样自带大量 API。
3. 快速更新：Fabric 在新 Minecraft 版本发布后，通常会迅速更新并提供支持。
4. 兼容性强：Fabric 能与 Sodium（性能优化模组）等高性能模组兼容，而 Forge 版的 OptiFine 可能会有问题。
5. 独立性：Fabric 不能直接运行 Forge 模组，二者生态不兼容。

#### Ⅲ、适用人群

1. 追求高性能的玩家
2. 喜欢快速更新版本的用户
3. 使用 Sodium、Lithium、Phosphor 等优化模组的玩家

#### Ⅳ、本地下载

### ③、NeoForge

> 官方下载地址：https://neoforged.net/

#### Ⅰ、简介

1. NeoForge 是 2023 年由 Forge 社区的一部分成员 分裂出来的新模组加载器
2. 目标是改进 Forge 的架构，提升其性能，并加速对新版本 Minecraft 的支持。

#### Ⅱ、特点

1. 源自 Forge：NeoForge 直接基于 Forge 代码库开发，但进行了优化。
2. 更现代化：修复了一些 Forge 旧架构导致的问题，提高了模组兼容性和加载速度。
3. 更快的更新：NeoForge 试图比 Forge 更快地适配 Minecraft 新版本。
4. 与 Forge 高度兼容：许多 Forge 模组可以直接运行在 NeoForge 上，但仍需开发者适配。

#### Ⅲ、适用人群

1. 想要使用 Forge 生态但希望获得更好性能的玩家
2. 需要较快更新支持新版本的用户

#### Ⅳ、本地下载

1. NeoForge 1.20.1：[NeoForge-1.21.1-21.1.116.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FNeoForge-1.21.1-21.1.116.jar)

### ④、总结

| 特性              | Forge       | Fabric        | NeoForge       |
| --------------- | ----------- | ------------- | -------------- |
| **性能**          | ⭐⭐⭐         | ⭐⭐⭐⭐          | ⭐⭐⭐⭐           |
| **生态**          | ⭐⭐⭐⭐        | ⭐⭐            | ⭐⭐⭐            |
| **更新速度**        | ⭐⭐          | ⭐⭐⭐⭐          | ⭐⭐⭐            |
| **OptiFine 支持** | ✅           | ❌             | ✅              |
| **大型模组支持**      | ✅           | ❌             | ✅              |
| **兼容性**         | 支持 Forge 模组 | 仅支持 Fabric 模组 | 兼容大部分 Forge 模组 |

1. 选择建议：
2. 如果想要高性能和快速更新，选择 Fabric
3. 如果想要使用经典的大型模组，选择 Forge
4. 如果想要比 Forge 更好的性能，同时兼容 Forge 生态，选择 NeoForge
5. 一般来说，现在都是使用 NeoForge 了

# 二、环境配置

## 1、使用包管理器安装 java

1. 使用包管理器安装 java，需使用 root 用户：

```shell
# 更新包索引：
apt update

# 安装特定版本的 OpenJDK，例如 OpenJDK 8：
apt install openjdk-8-jdk

# 安装特定版本的 OpenJDK，例如 OpenJDK 11：
apt install openjdk-11-jdk

# 安装特定版本的 OpenJDK，例如 OpenJDK 17：
apt install openjdk-17-jdk
```

## 2、手动配置 java 环境

### ①、从 oracle 下载

1. 下载地址：https://www.oracle.com/cn/java/technologies/downloads/
2. 下载想要使用的版本，此处使用 java 21，选择 `x64 Compressed Archive`：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227141724.png)

3. 上传到服务器目录：`/home/steam/IDE/Java/JDK/`
4. 解压缩：`tar -zxvf jdk-21_linux-x64_bin.tar.gz`

### ②、本地下载

1. java 21 压缩包下载：[jdk-21_linux-x64_bin.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fjdk-21_linux-x64_bin.zip)
2. 上传到服务器目录：`/home/steam/IDE/Java/JDK/`
3. 解压缩：`unzip jdk-21_linux-x64_bin.zip`

### ③、配置 jdk 环境变量

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

## 3、查看 jdk 配置是否生效：

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

# 四、下载游戏服务器

1. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

2. 在根目录下创建 `game/Minecraft-forge` 目录，仅是为了方便管理

```shell
mkdir -p game/Minecraft-forge
```

3. 进入 `game/Minecraft-forge` 文件夹

```shell
cd game/Minecraft-forge
```

4. 下载指定版本的模组加载器：https://files.minecraftforge.net/net/minecraftforge/forge/
	1. 此处以 Forge `1.20.1` 版本进行演示
	2. forge-1.20.1-47.2.0-installer 版本下载：[forge-1.20.1-47.2.0-installer.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fforge-1.20.1-47.2.0-installer.jar)

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227103945.png)

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240227104008.png)

5. 将上面下载的文件上传到 `/home/steam/game/Minecraft-forge` 目录中，此时该目录只有 `forge-1.20.1-47.2.0-installer.jar` 这一个文件
6. 赋予权限：

```shell
chmod 755 forge-1.20.1-47.2.0-installer.jar
```

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

> 我使用的皮肤站：https://littleskin.cn

### ①、CustomSkinLoader（推荐）

> 1. 下载地址：https://littleskin.cn/user/config
> 2. 根据不同的模组加载器和其版本下载对应的 CustomSkinLoader

1. LittleSkin 建议使用 CustomSkinLoader 作为皮肤加载 Mod，同时也支持其他所有支持 CustomSkinAPI 和传统皮肤加载方式的皮肤 Mod
2. 将下载的 CustomSkinLoader 放入客户端的 Mod 目录，然后：[登录 littleskin 皮肤站](#12-2-2) 即可
3. Forge 加载器 CustomSkinLoader 下载：
	1. 1.20.6 +：[CustomSkinLoader_ForgeV3-14.22.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_ForgeV3-14.22.jar)
	2. 1.17.1 ~ 1.20.4：[CustomSkinLoader_ForgeV2-14.22.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_ForgeV2-14.22.jar)
	3. 1.8 ~ 1.16.5：[CustomSkinLoader_ForgeV1-14.22.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_ForgeV1-14.22.jar)
	4. 1.7.10：[CustomSkinLoader_14.6a.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_14.6a.jar)；该版本及以下 CustomSkinLoader 需要手动配置后才可加载来自 LittleSkin 的材质，请参考 LittleSkin 用户使用手册中的相关页面对 CustomSkinLoader 进行配置。 [点击这里查看 >>>](https://manual.littlesk.in/newbee/csl#%E7%89%88%E6%9C%AC-%E6%97%A9%E6%9C%9F)
	5. 1.7.2：[CustomSkinLoader_12.9-HD.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_12.9-HD.jar)
	6. 1.6.4：[CustomSkinLoader_12.9-HD.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_12.9-HD.jar)
4. Fabric 加载器 CustomSkinLoader 下载：
	1. 1.14 +：[CustomSkinLoader_Fabric-14.22.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_Fabric-14.22.jar)
5. NeoForge 加载器 CustomSkinLoader 下载：
	1. 1.20.2 +：[CustomSkinLoader_ForgeV3-14.22.jar](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FCustomSkinLoader_ForgeV3-14.22.jar)

### ②、authlib-injector（不推荐）

> 在 Minecraft 服务端使用 authlib-injector 的[参考文档与下载地址](https://github.com/yushijinhun/authlib-injector/wiki/%E5%9C%A8-Minecraft-%E6%9C%8D%E5%8A%A1%E7%AB%AF%E4%BD%BF%E7%94%A8-authlib-injector)

1. 下载 `authlib-injector`，将其上传至 `/home/steam/game/Minecraft-forge/plugins/` 中
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

5. 此时服务器配置完毕，重新启动即可
6. 当然还需要客户端同样加载 `authlib-injector`，放在 Mod 目录，然后：[登录 littleskin 皮肤站](#12-2-2)

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

### ②、服务器管理脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/game/Minecraft-forge/NFWC-Beta-0.3.2-server/
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch minecraft_server_manager.sh
```

1. 编写服务器管理脚本代码：`nano minecraft_server_manager.sh`

```shell
#!/bin/bash

# 获取第一个参数：执行方式（启动=start、重启=restart、停止=stop、备份=backup），默认是启动
mode=${1:-start}

# 启动脚本名称，一般有 run.sh、start.sh
script_name="start.sh"
# screen 会话名称，每个会话中可能有多个窗口
screen_name="1359342.BMC4-v36"
# 脚本所在路径
path="/home/steam/game/Minecraft-forge/BMC4-v36"

# 获取当前时间，用于日志记录、备份文件名
current_time=$(date "+%Y-%m-%d_%H%M%S")
# 日志内容
log_content=""
# 设置备份的目录
backup_dir="$path/world"
# 设置备份存放的目录
backup_storage_dir="$path/backup"
# 生成备份文件的名称，包含日期
backup_filename="backup_$current_time.tar.gz"

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

# 向日志文件中追加日志
logging() {
    echo "----------------------------------------------------------------" >> $path/minecraft_server.log
    echo "$log_content" >> $path/minecraft_server.log
    echo "" >> $path/minecraft_server.log
}

# 定义启动函数
start_server() {
    # 进入游戏服务器目录，不在此目录执行启动脚本会导致报错
    send_command "cd $path\r" 2
    # 发送启动命令，包括运行参数，将命令发送到会话中，并模拟按下回车键
    send_command "./$script_name\r"

    # 向日志内容中添加信息
    log_content="【${current_time}】我的世界服务器已启动"
}

# 定义停止函数
stop_server() {
    # 发送指令，保存服务器世界状态到硬盘，并模拟按下回车键；等待 60 秒
    send_command "save-all\r" 60
    # 发送指令，关闭服务器，并模拟按下回车键；等待 20 秒
    send_command "stop\r" 20

    # 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 20 秒；执行 3 次
    send_command $'\x03' 20
    send_command $'\x03' 5
    send_command $'\x03' 5

    # 向日志内容中添加信息
    log_content="【${current_time}】我的世界服务器已停止"
}

# 定义重启函数
restart_server() {
    # 调用停止函数
    stop_server
    # 调用启动函数
    start_server

    # 向日志内容中添加信息
    log_content="【${current_time}】我的世界服务器已重启"
}

# 定义备份存档函数
backup_world() {
    echo "----------------------------------------------------------------" >> $path/minecraft_server.log
    # 检查备份存放目录是否存在，不存在则创建
    if [ ! -d "$backup_storage_dir" ]; then
        mkdir -p "$backup_storage_dir" || { 
            echo "【${current_time}】错误：创建备份目录失败！" >> "$path/minecraft_server.log"
            exit 1
        }
        echo "【${current_time}】创建备份目录 $backup_storage_dir 成功" >> $path/minecraft_server.log
    fi
    # 进入备份目录
    cd "$backup_dir" || { 
        echo "【${current_time}】错误：无法进入 $backup_dir，备份中止。" >> "$path/minecraft_server.log"
        exit 1
    }

    # 打包并压缩指定目录，排除 session.lock 和 logs 文件
    tar --exclude='./session.lock' --exclude='./logs' -czf "$backup_storage_dir/$backup_filename" . || { 
        echo "【${current_time}】错误：备份失败！" >> "$path/minecraft_server.log"
        exit 1
    }
    # 记录成功备份日志
    echo "【${current_time}】Minecraft 服务器备份成功：$backup_filename" >> "$path/minecraft_server.log"

    # 删除一周前的备份
    # find "$backup_storage_dir"：指定了 find 命令开始搜索的目录路径，即备份文件存放的目录
    # -name "backup_*.tar.gz"：这个选项让 find 命令查找名称匹配模式 backup_*.tar.gz 的文件
    # -type f：指定 find 只应查找类型为普通文件的条目。它排除了目录、链接或其他特殊类型的文件，确保只处理实际的备份文件
    # -mtime +7：这个选项基于文件的修改时间来过滤搜索结果。mtime 是文件内容最后修改的时间。+7 表示选择那些最后修改时间在七天前或更早的文件
    # -exec rm {} \;：这是一个执行动作，指示 find 命令对每个找到的文件执行 rm（删除）命令。在 find 命令中，{} 用作匹配文件的占位符，而 \; 是该 -exec 动作的结束标志
    find "$backup_storage_dir" -name "backup_*.tar.gz" -type f -mtime +7 -exec rm {} \;
    # 向 minecraft_server.log 文件中追加日志
    echo "【${current_time}】我的世界 neoforge atm-10 备份存档和清理一周前备份已完成" >> $path/minecraft_server.log
    echo "" >> $path/minecraft_server.log
}



# 检查执行方式，进行相应的操作
if [ "$mode" == "start" ]; then
    # 如果是启动或重启，则调用启动函数，并向日志文件中追加日志
    start_server
    logging
elif [ "$mode" == "restart" ]; then
    # 如果是重启，则调用重启函数，并向日志文件中追加日志
    restart_server
    logging
elif [ "$mode" == "stop" ]; then
    # 如果是停止，则调用停止函数，并向日志文件中追加日志
    stop_server
    logging
elif [ "$mode" == "backup" ]; then
    # 如果是备份，则调用备份函数
    backup_world
else
    echo "无效的执行方式，请使用 start、restart、stop 或 backup。"
fi
```

4. 设置脚本权限：

```shell
chmod 755 minecraft_server_manager.sh
```

1. 脚本使用：使用时需传入执行方式：启动=start、重启=restart、停止=stop、备份=backup
2. 每个服务器对应的修改：
	1. script_name：启动脚本的名称，一般有 run.sh、start.sh
	2. screen_name：screen 会话名称，通过命令 `screen -ls` 查看
	3. path：服务器、服务器启动脚本所在目录
3. 设置定时执行：
	1. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
	2. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 我的世界 forge BMC4-v36 服务器开启，周一至周五，每天 18 点
0 18 * * 1-5 /home/steam/game/Minecraft-forge/BMC4-v36/minecraft_server_manager.sh start
# 我的世界 forge BMC4-v36 服务器开启，周六和周日，每天 9 点
0 9 * * 6,0 /home/steam/game/Minecraft-forge/BMC4-v36/minecraft_server_manager.sh start
# 我的世界 forge BMC4-v36 服务器关闭，每天 23 点
0 23 * * * /home/steam/game/Minecraft-forge/BMC4-v36/minecraft_server_manager.sh stop
# 我的世界 forge BMC4-v36 备份存档，每天 23:30
30 23 * * * /home/steam/game/Minecraft-forge/BMC4-v36/minecraft_server_manager.sh backup
```

8. 在 cron 表达式中，参数用于指定定时任务的执行时间。一个标准的 cron 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
9. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置

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

# 十、服务器添加 mod

> 首先在客户端下载和安装 mod，具体说明在十二节

1. 客户端点击游戏版本：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211640.png)

2. 然后点击 MOD 文件夹，会打开一个文件夹

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211741.png)

3. 将其中的所有文件上传至游戏服务器根目录中的 `mods` 目录，启动服务器即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305211909.png)

4. 若是启动时报错，可能是因为这些 mod 中有客户端专属，而服务器不能安装的 mod，根据提示删除即可

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

#### Ⅱ、给玩家管理员权限

1. 命令格式为：`op <玩家名>`。
	1. `<玩家名>`：要给与管理员权限的玩家的用户名
2. 收回管理员权限：`deop <玩家名>`
3. 例子：给予玩家 `chenpi` 管理员权限

```shell
# 给予管理员权限
op chenpi

# 收回管理员权限
deop chenpi
```

#### Ⅲ、关闭死亡掉落

1. 命令格式为：

```shell
gamerule keepInventory true
```

2. 恢复掉落：

```shell
gamerule keepInventory false
```

#### Ⅳ、

#### Ⅴ、

## 2、客户端指令

## 3、远程控制台（RCON）使用

# 十二、客户端启动器

## 1、官方启动器

> 官方网站：https://www.minecraft.net/

## 2、HMCL 启动器使用

### ①、下载

1. 下载地址：https://hmcl.huangyuhui.net/download/
2. 下载最新版本即可
3. 本地 HMCL-3.5.5 下载：[HMCL-3.5.5.exe](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FHMCL-3.5.5.exe)

### ②、<span id="12-2-2">登录 `littleskin` 皮肤站</span>

1. 在皮肤站账册账号，使用皮肤：https://littleskin.cn
2. HMCL 启动器中点击设置

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194424.png)

3. 进入设置页后，点击下载，取消自动选择下载源，选择 BMCLAPI

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194522.png)

4. 然后将按钮拖动至启动器，登录即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305194713.png)

### ③、使用启动器下载游戏本体

1. 点击版本列表

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200733.png)

2. 点击安装新游戏版本，下载指定版本的游戏即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200811.png)

### ④、使用启动器下载整合包

1. 点击版本列表

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200733.png)

2. 点击安装新游戏版本，下载指定版本的游戏即

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305200811.png)

3. 选择整合包

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202013.png)

4. 可以搜索指定的整合包，点击整合包进入

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202403.png)

5. 选择对应游戏本体版本的整合包，然后点击下载

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202456.png)

6. 下载完成后，点击返回，选择安装整合包

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202744.png)

7. 导入本地整合包，然后选择刚才下载的整合包

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202911.png)

8. 点击安装

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305202955.png)

9. 安装完选中即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240305204819.png)
