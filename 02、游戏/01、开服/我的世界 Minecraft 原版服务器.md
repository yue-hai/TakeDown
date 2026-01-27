# 一、游戏服务器信息

1. 端口号：`25565`
2. 不需要通过 SteamCmd 进行下载
3. 首先进行：[服务器设置](游戏服务器购买和设置.md)

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

![|700](attachments/Pasted%20image%2020240227141724.png)

3. 上传到服务器目录：`/home/steam/IDE/Java/JDK/`
4. 解压缩：`tar -zxvf jdk-21_linux-x64_bin.tar.gz`

### ②、本地下载

1. java 21 压缩包下载：[jdk-21_linux-x64_bin.zip](attachments_lfs/jdk-21_linux-x64_bin.zip)
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

# 三、下载游戏服务器

1. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

2. 在根目录下创建 `game/Minecraft` 目录，仅是为了方便管理

```shell
mkdir -p game/Minecraft
```

3. 进入 `game/Minecraft` 文件夹

```shell
cd game/Minecraft
```

4. 下载 Minecraft；MC 服务端核心分为官方版本和其他版本，下面是部分服务端下载链接：
	1. 官方服务端：https://minecraft.net/zh-hans/download/server/
	2. 官方服务端：https://mcversions.net/
	3. papermc服务端：https://papermc.io/downloads
	4. spigot服务端：https://hub.spigotmc.org/jenkins/job/BuildTools/
	5. sponge服务端：https://www.spongepowered.org/
5. 这里使用 papermc 服务端，访问 papermc 官网，选择版本下载；此处以 `1.20.1` 版本进行演示
	1. paper-1.20.1-196 版本下载：[paper-1.20.1-196.jar](attachments/paper-1.20.1-196.jar)

![|700](attachments/Pasted%20image%2020240226163637.png)

![|700](attachments/Pasted%20image%2020240227090220.png)

7. 将上面下载的文件上传到 `/home/steam/game/Minecraft` 目录中，此时该目录只有 `paper-1.20.1-196.jar` 这一个文件
8. 赋予权限：

```shell
chmod 755 paper-1.20.1-196.jar
```

# 六、启动游戏服务器

1. 进入 `/home/steam/game/Minecraft` 目录

```shell
cd /home/steam/game/Minecraft
```

2. 执行文件：
	1. `-Xms`：初始启动分配的内存（-Xms1024m）
	2. `-Xmx`：最大分配的内存（-Xmx2048m）
	3. `nogui`：用于以基于文本的界面来显示，可减少内存使用。如果使用图形化界面，移除 nogui 选项。

```shell
java -Xmx1024M -Xms1024M -jar paper-1.20.1-196.jar nogui
```

3. 首次启动会失败，配置文件目录下会生成一个 `eula.txt` 文件，用 nano 打开：`nano eula.txt`

```shell
# 将
eula=false

# 修改为：表示同意许可协议
eula=true
```

4. 创建启动脚本：

```shell
touch start_server.sh
```

5. 打开启动脚本：`nano start_server.sh`，输入以下内容：

```shell
#!/bin/bash

# 脚本所在路径
path="/home/steam/game/Minecraft"

java -Xmx8192M -Xms1024M -jar paper-1.20.1-196.jar nogui
```

6. 赋予权限：

```shell
chmod 755 start_server.sh
```

7. 执行脚本：

```shell
./start_server.sh
```

8. 此时服务器启动完成，即可通过客户端尝试加入；但是此时有正版验证，也不可使用 `littleskin` 皮肤站
9. 若想关闭正版验证，则首先按 `ctrl + c` 关闭服务器
10. 打开主配置文件 `server.properties`：`nano server.properties`：

```shell
# 将
online-mode=true

# 修改为：表示关闭正版验证
online-mode=false
```

11. 此时没有购买正版的玩家，使用离线登录可以加入此服务器

# 七、使用 `littleskin` 皮肤站

> 在 Minecraft 服务端使用 authlib-injector 的[参考文档与下载地址](https://github.com/yushijinhun/authlib-injector/wiki/%E5%9C%A8-Minecraft-%E6%9C%8D%E5%8A%A1%E7%AB%AF%E4%BD%BF%E7%94%A8-authlib-injector)，
> 
> 我使用的皮肤站：https://littleskin.cn

1. 下载 `authlib-injector`，将其上传至 `/home/steam/game/Minecraft/plugins/` 中
	1. authlib-injector-1.2.5 下载：[authlib-injector-1.2.5.jar](attachments/authlib-injector-1.2.5.jar)
2. 进入 `/home/steam/game/Minecraft` 目录

```shell
cd /home/steam/game/Minecraft
```

3. 打开主配置文件 `server.properties`：`nano server.properties`：

```shell
# 将
online-mode=false

# 修改为：
online-mode=true
```

4. 修改启动脚本：`nano start_server.sh`

```shell
#!/bin/bash

# 脚本所在路径
path="/home/steam/game/Minecraft"
# authlib-injector.jar 所在路径
path_authlib="/home/steam/game/Minecraft/plugins/authlib-injector-1.2.5.jar"
# 验证服务器的 URL
url="https://littleskin.cn/api/yggdrasil"

java -Xmx1024M -Xms1024M -javaagent:$path_authlib=$url -jar paper-1.20.1-196.jar nogui
```

5. 此时重新启动服务器即可；当然还需要客户端同样加载 `authlib-injector`，这个后面说

# 八、使用 screen 后台运行服务器

1. 进入服务器目录

```shell
cd /home/steam/game/Minecraft
```

2. 输入命令创建终端，ttr为终端名称，可任意更改，输入完毕后会进入一个新的页面

```shell
screen -S mc
```

3. 执行脚本，启动服务器；按 `Ctrl + a + d` 可退出终端：

```shell
/home/steam/game/Minecraft/start_server.sh
```

4. 此时会有大量输出，待出现类似以下内容时，即为启动成功：

```shell
steam@yan:~/apply/game/Minecraft$ ./start_server.sh
Starting org.bukkit.craftbukkit.Main
*** Warning, you've not updated in a while! ***
*** Please download a new build as per instructions from https://papermc.io/downloads/paper ***
System Info: Java 21 (Java HotSpot(TM) 64-Bit Server VM 21.0.2+13-LTS-58) Host: Linux 6.2.0-26-generic (amd64)
Loading libraries, please wait...
[09:17:37 INFO]: Environment: authHost='https://authserver.mojang.com', accountsHost='https://api.mojang.com', sessionHost='https://sessionserver.mojang.com', servicesHost='https://api.minecraftservices.com', name='PROD'
[09:17:37 INFO]: Found new data pack file/bukkit, loading it automatically
[09:17:38 INFO]: Loaded 7 recipes
[09:17:38 INFO]: Starting minecraft server version 1.20.1
[09:17:38 INFO]: Loading properties
[09:17:38 INFO]: This server is running Paper version git-Paper-196 (MC: 1.20.1) (Implementing API version 1.20.1-R0.1-SNAPSHOT) (Git: 773dd72)
[09:17:39 INFO]: Server Ping Player Sample Count: 12
[09:17:39 INFO]: Using 4 threads for Netty based IO
[09:17:39 WARN]: [!] The timings profiler has been enabled but has been scheduled for removal from Paper in the future.
    We recommend installing the spark profiler as a replacement: https://spark.lucko.me/
    For more information please visit: https://github.com/PaperMC/Paper/issues/8948
[09:17:39 INFO]: [ChunkTaskScheduler] Chunk system is using 1 I/O threads, 4 worker threads, and gen parallelism of 4 threads
[09:17:39 INFO]: Default game type: SURVIVAL
[09:17:39 INFO]: Generating keypair
[09:17:39 INFO]: Starting Minecraft server on *:25565
[09:17:39 INFO]: Using epoll channel type
[09:17:39 INFO]: Paper: Using libdeflate (Linux x86_64) compression from Velocity.
[09:17:39 INFO]: Paper: Using OpenSSL 3.0.x (Linux x86_64) cipher from Velocity.
[09:17:39 INFO]: Preparing level "world"
[09:17:41 INFO]: Preparing start region for dimension minecraft:overworld
[09:17:42 INFO]: Time elapsed: 56 ms
[09:17:42 INFO]: Preparing start region for dimension minecraft:the_nether
[09:17:42 INFO]: Time elapsed: 45 ms
[09:17:42 INFO]: Preparing start region for dimension minecraft:the_end
[09:17:42 INFO]: Time elapsed: 41 ms
[09:17:42 INFO]: Running delayed init tasks
[09:17:42 INFO]: Done (3.523s)! For help, type "help"
[09:17:42 INFO]: Timings Reset
> 
```

5. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.mc</font> 的进程

```shell
screen -ls
```

6. 输入进程名字即可进入终端

```shell
screen -r XXX.mc
```

7. 结束进程

```shell
screen -S XXX.mc -X quit
```

# 九、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

1. 授权确认文件：`~/game/Minecraft/eula.txt`
2. 主配置文件：`~/game/Minecraft/server.properties`
3. 用于存储被封禁的IP地址列表：`~/game/Minecraft/banned-ips.json`
4. 记录被封禁的玩家名单：`~/game/Minecraft/banned-players.json`
5. 服务器管理员（OP）列表：`~/game/Minecraft/ops.json`
6. 白名单文件，当服务器启用白名单时，只有列在此文件中的玩家才能加入：`~/game/Minecraft/whitelist.json`
8. 缓存最近登录过服务器的玩家信息，用于快速验证玩家身份：`~/game/Minecraft/usercache.json`

### ②、重要路径

1. 主世界和人物存档目录：`~/game/Minecraft/world/`
2. 地狱和人物存档目录：`~/game/Minecraft/world_nether/`
3. 末地和人物存档目录：`~/game/Minecraft/world_the_end/`
4. 存放服务器的日志文件：`~/game/Minecraft/logs/`
5. 如果服务器是基于Spigot或Bukkit等插件系统运行的，这个目录用于存放服务器插件：`~/game/Minecraft/plugins/`
6. 当服务器发生崩溃时，崩溃报告将会保存在这个目录下：`~/game/Minecraft/crash-reports/`
7. 一些插件或模组可能会在这个目录下生成配置文件，用于自定义插件或模组的行为：`~/game/Minecraft/config/`

## 2、主配置文件 `~/game/Minecraft/server.properties` 参数说明

```shell
# 世界生成器的特定设置，留空为默认
generator-settings= 
# 重新登录时是否强制玩家回到默认游戏模式
force-gamemode=false 
# 是否允许玩家进入地狱
allow-nether=true 
# 是否强制白名单（只有白名单上的玩家才能加入）
enforce-whitelist=false 
# 默认的游戏模式（0为生存，1为创造，2为冒险，3为观察者）
gamemode=0 
# 是否允许使用GameSpy4协议的服务器监听器
enable-query=false 
# 玩家空闲多久后踢出服务器，0为不踢出
player-idle-timeout=0 
# 游戏难度（0为和平，1为简单，2为普通，3为困难）
difficulty=1 
# 是否生成怪物
spawn-monsters=true 
# OP（管理员）的权限等级
op-permission-level=4 
# 是否允许玩家间PVP（玩家对战）
pvp=true 
# 是否允许服务器发送数据到snoop服务器
snooper-enabled=true 
# 世界类型（DEFAULT, FLAT, LARGEBIOMES, AMPLIFIED, CUSTOMIZED, BUFFET）
level-type=DEFAULT 
# 是否为极限模式（死亡后自动封禁）
hardcore=false 
# 是否启用命令方块
enable-command-block=false 
# 最大玩家数
max-players=20 
# 数据包压缩阈值，小于该大小的数据包不会被压缩
network-compression-threshold=256 
# 资源包的SHA-1校验和
resource-pack-sha1= 
# 世界边界最大大小
max-world-size=29999984 
# 服务器端口
server-port=25565 
# 绑定的服务器IP地址
server-ip= 
# 是否生成NPC（村民）
spawn-npcs=true 
# 是否允许玩家飞行
allow-flight=false 
# 世界名称
level-name=world 
# 玩家能看到的区块距离
view-distance=10 
# 服务器资源包的URL
resource-pack= 
# 是否生成动物
spawn-animals=true 
# 是否启用白名单
white-list=false 
# 是否生成结构（如村庄）
generate-structures=true 
# 是否启用验证玩家的正版账号
online-mode=true 
# 允许建造的最高高度
max-build-height=256 
# 世界生成的种子
level-seed= 
# 是否阻止通过代理连接的玩家
prevent-proxy-connections=false 
# 是否使用Linux的epoll（更高效的网络处理方式）
use-native-transport=true 
# 服务器的消息（在多人游戏服务器列表中显示）
motd=A Minecraft Server 
# 是否启用远程访问命令（Remote Command）
enable-rcon=false 
```

# 十、管理服务器

## 1、指令

> wiki 网站：https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4

1. 服务端指令前不需要加 `/`
2. 客户端按 `t` 打开聊天框，指令前需要加 `/`

# 十一、客户端启动器

## 1、官方启动器

> 官方网站：https://www.minecraft.net/

## 2、HMCL 启动器使用

### ①、下载

1. 下载地址：https://hmcl.huangyuhui.net/download/
2. 下载最新版本即可
3. 本地 HMCL-3.5.5 下载：[HMCL-3.5.5.exe](attachments/HMCL-3.5.5.exe)

### ②、登录 `littleskin` 皮肤站

1. 在皮肤站账册账号，使用皮肤：https://littleskin.cn
2. HMCL 启动器中点击设置

![|700](attachments/Pasted%20image%2020240305194424.png)

3. 进入设置页后，点击下载，取消自动选择下载源，选择 BMCLAPI

![|700](attachments/Pasted%20image%2020240305194522.png)

4. 然后将按钮拖动至启动器，登录即可

![](attachments/Pasted%20image%2020240305194713.png)

### ③、使用启动器下载游戏本体

1. 点击版本列表

![|700](attachments/Pasted%20image%2020240305200733.png)

2. 点击安装新游戏版本，下载指定版本的游戏即可

![|700](attachments/Pasted%20image%2020240305200811.png)
