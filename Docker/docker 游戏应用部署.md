# 1、minecraft 我的世界

> 1. 项目 github：https://github.com/itzg/docker-minecraft-server
> 2. dockerHub 地址：https://hub.docker.com/r/itzg/minecraft-server

## 1、介绍

1. itzg/minecraft 是目前最流行和事实上的标准 Minecraft 服务端 Docker 镜像。它是一个功能极其强大且高度可配置的容器化解决方案，允许用户通过简单的方式部署和管理几乎所有类型的 Minecraft Java 版服务器。
2. 它的主要特点包括：
	1. 广泛的服务端支持：无缝支持官方原版 (Vanilla)、Paper、Spigot、Forge、Fabric、Bukkit 等几乎所有主流的服务端类型，只需一个环境变量即可轻松切换，满足从纯净生存到大型模组整合包的各种需求
	2. 极致简化的配置：服务器的所有设置，如游戏模式、难度、内存分配、世界种子、管理员(OP)等，均可通过 Docker 的环境变量进行配置，无需手动修改 server.properties 文件，实现了一次配置，到处运行
	3. 自动化管理：容器启动时会自动下载指定版本的服务端文件，并能自动同意 EULA 协议。它还能处理版本升级，极大地简化了服务器的初始设置和日常维护工作
	4. 数据持久化与备份：通过挂载数据卷，可以轻松地将世界、插件、模组等关键数据保存在宿主机上，确保容器更新或重建后数据不丢失。同时，它还内置了自动备份功能
	5. 强大的扩展功能：原生支持 RCON（远程管理协议），方便进行自动化管理和与第三方工具集成。此外，还包含了健康检查机制，确保服务器稳定运行

## 2、常用参数

### ①、核心与必要参数

| 参数  | 示例     | 说明                                                                                       |
| --- | ------ | ---------------------------------------------------------------------------------------- |
| -p  | -p     | `25565:25565` 端口映射<br>将主机的 25565 端口映射到容器的 25565 端口，这是 Minecraft Java 版的默认端口，用于玩家连接       |
| -v  | -v     | `/path/to/data:/data`	数据持久化<br>将容器内保存所有游戏数据（世界、插件、日志等）的 /data 目录挂载到你主机的指定路径，防止容器删除后数据丢失  |
| -e  | EULA   | `-e EULA="TRUE"`	同意最终用户许可协议。必需！ 设为 "TRUE" 才能启动服务器                                        |
| -e  | MEMORY | `-e MEMORY="4G"`	分配内存<br>指定分配给 Minecraft 服务器的 Java 内存大小，例如 512M, 2G, 4G。根据玩家数量和 Mod 数量调整 |

### ②、服务器与世界配置参数

| 参数  | 示例                         | 说明                                                                                                               |     |
| --- | -------------------------- | ---------------------------------------------------------------------------------------------------------------- | --- |
| -e  | TYPE                       | `-e TYPE="PAPER"`	服务端类型，决定使用哪种服务端<br>原版或原版改版：VANILLA (官方原版)、PAPER(推荐, 性能好)、SPIGOT<br>mod 版：FABRIC、FORGE、NEOFORGE |     |
| -e  | VERSION                    | `-e VERSION="1.20.4"`	游戏版本<br>指定要运行的 Minecraft 版本。设为 LATEST 可自动使用最新稳定版                                           |     |
| -e  | WORLD_NAME                 | `-e WORLD_NAME="MyWorld"`	世界名称<br>指定世界文件夹的名称。如果该世界不存在，服务器会使用此名称创建一个新世界                                           |     |
| -e  | SEED                       | `-e SEED="dockercraft"`	世界种子。用于生成新世界的种子码                                                                         |     |
| -e  | BACKUP_INTERVAL            | `-e BACKUP_INTERVAL="24h"` 开启内置备份，并设置间隔为24小时                                                                     |     |
| -e  | RCON_CMDS_ON_BACKUP_START  | `-e RCON_CMDS_ON_BACKUP_START="【服务器正在准备备份】"`<br>备份开始时在游戏内发送的通知                                                   |     |
| -e  | RCON_CMDS_ON_BACKUP_FINISH | `-e RCON_CMDS_ON_BACKUP_FINISH="【备份完成】"`<br>备份结束后在游戏内发送的通知                                                       |     |

### ③、玩家与权限管理参数

| 参数  | 示例                | 说明                                                                 |
| --- | ----------------- | ------------------------------------------------------------------ |
| -e  | OPS               | `-e OPS="player1,player2"`	设置管理员 (OP)。将一个或多个玩家设置为管理员，用逗号分隔         |
| -e  | WHITELIST         | `-e WHITELIST="player1,player2"`	设置白名单。将玩家添加到白名单中，同样用逗号分隔          |
| -e  | ENFORCE_WHITELIST | `-e ENFORCE_WHITELIST="TRUE"`	强制开启白名单。设为 "TRUE" 后，只有白名单中的玩家才能进入服务器 |
| -e  | MAX_PLAYERS       | `-e MAX_PLAYERS="20"`	最大玩家数。设置服务器能同时容纳的最大玩家数量                      |

### ④、`server.properties` 参数设置

1. itzg/minecraft 镜像非常智能，它遵循一个简单的转换规则：可以通过环境变量来设置 `server.properties` 文件中的任何一个参数。规则是：将配置文件中的参数名全部转换为大写，并将破折号 `-` 替换为下划线 `_`
2. 因此，对于 `server.properties` 文件中参数，比如飞行：`allow-flight`，对应的环境变量就是 `ALLOW_FLIGHT`
3. 设置方法：在 docker run 命令中加入一行 `-e ALLOW_FLIGHT="TRUE"` 即可
4. 常用参数：

```shell
# 服务器标语，会显示在游戏的多人游戏列表中
-e MOTD="A Minecraft Server"
# 默认游戏模式: "survival", "creative", "adventure", "spectator"
-e GAMEMODE="survival"
# 游戏难度: "peaceful", "easy", "normal", "hard"
-e DIFFICULTY="normal"
# 是否开启极限模式: "TRUE" 或 "FALSE"
-e HARDCORE="FALSE"
# 是否允许玩家间互相攻击 (PvP): "TRUE" 或 "FALSE"
-e PVP="TRUE"
# 是否允许飞行 (对于鞘翅或Mod飞行道具至关重要): "TRUE" 或 "FALSE"
-e ALLOW_FLIGHT="TRUE"
# 是否启用命令方块: "TRUE" 或 "FALSE"
-e ENABLE_COMMAND_BLOCK="TRUE"
# 是否强制玩家每次登录都设为默认游戏模式: "TRUE" 或 "FALSE"
-e FORCE_GAMEMODE="TRUE"
```

5. 主配置文件 `server.properties` 参数说明：

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

## 3、docker 部署

1. 为防止容器意外停止后数据丢失，首先在宿主机创建目录：
	1. 游戏数据目录：`/vol1/1000/docker/game/minecraft/BMC4-v36`
2. 使用 docker run 部署：

```shell
docker run -d \
-p 25565:25565 \
-e EULA="TRUE" \
-e TYPE="FORGE" \
-e VERSION="1.20.1" \
-e MEMORY="8G" \
-e STOP_TIMEOUT="180" \
-e BACKUP_INTERVAL="24h" \
-e RCON_CMDS_ON_BACKUP_START="say 【服务器正在准备内置备份】" \
-e RCON_CMDS_ON_BACKUP_FINISH="say 【备份完成】" \
-e MOTD="欢迎来到月海的 bmc4 世界" \
-e MAX_PLAYERS="10" \
-e VIEW_DISTANCE="10" \
-e ALLOW_FLIGHT="TRUE" \
-e OPS="yuehai-,chenpi" \
-e TZ=Asia/Shanghai \
-v /vol1/1000/docker/game/minecraft/BMC4-v36:/data \
--privileged=true \
--network yuehai-net \
--restart=unless-stopped  \
--name game-mc-bmc4 \
itzg/minecraft-server:latest
```

1. 使用 `docker-compose.yml` 部署：

```yaml
# 定义所有要管理的服务（容器）
services:
    # 定义一个名为 game-mc-bmc4 的服务
    game-mc-bmc4:
        # 指定该服务使用的 Docker 镜像及其标签（版本）
        image: itzg/minecraft-server:latest
        # 设置容器的固定名称，方便识别和管理
        container_name: game-mc-bmc4
        # 定义容器的重启策略
        restart: unless-stopped
        # 定义端口映射规则
        ports:
            # Minecraft 游戏服务器的标准端口
            - "25565:25565"
        # 定义容器内部的环境变量，用于配置游戏服务器
        environment:
            # 接受 Minecraft 最终用户许可协议 (EULA)
            - EULA=TRUE
            # 设置服务器类型为 Forge，以支持 Mod
            - TYPE=FORGE
            # 设置游戏版本为 1.20.1
            - VERSION=1.20.1
            # 分配给 Minecraft 服务器的内存大小
            - MEMORY=8G
            # 将关服的等待时间从默认的 60 秒延长到 180 秒 (3分钟)
            - STOP_TIMEOUT=180
            # 开启内置备份，并设置间隔为24小时
            - BACKUP_INTERVAL=24h
            # 设置在备份开始时通过 RCON 发送的服务器消息
            - RCON_CMDS_ON_BACKUP_START=say 【服务器正在准备内置备份】
            # 设置在备份完成后通过 RCON 发送的服务器消息
            - RCON_CMDS_ON_BACKUP_FINISH=say 【备份完成】
            # 设置服务器在玩家列表中的欢迎信息
            - MOTD=欢迎来到月海的 bmc4 世界
            # 设置最大玩家数量
            - MAX_PLAYERS=10
            # 设置服务器的视距
            - VIEW_DISTANCE=10
            # 允许玩家飞行（通常需要作弊或特定插件支持）
            - ALLOW_FLIGHT=TRUE
            # 设置服务器的管理员（OP）列表，用逗号分隔
            - OPS=yuehai-,chenpi
            # 添加时区以确保日志时间戳正确
            - TZ=Asia/Shanghai
        # 定义数据卷挂载规则，用于持久化存储游戏世界和配置
        volumes:
            # 数据目录
            - /vol1/1000/docker/game/minecraft/BMC4-v36:/data
        # 定义此服务要连接的网络
        networks:
            # 将此服务连接到名为 yuehai-net 的网络
            - yuehai-net

# 在文件末尾定义此 Compose 文件中使用的所有网络
networks:
    # 定义一个名为 yuehai-net 的网络配置
    yuehai-net:
        # 将此网络声明为外部网络
        # external: true 的意思是：不要创建这个网络，而是去使用一个已经存在的、名字完全相同的网络
        external: true
```

## 4、服务器管理脚本

1. 选择一个目录，比如 `/vol1/1000/docker/script/cronicle/scripts/game/minecraft`：
   
```shell
cd /vol1/1000/docker/script/cronicle/scripts/game/minecraft
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch minecraft_server_manager.sh
```

3. 编写服务器管理脚本代码：`nano minecraft_server_manager.sh`

```shell
#!/bin/bash

# 获取第 1 个参数：执行方式（启动=start、重启=restart、停止=stop、备份=backup），默认是启动
mode=${1:-start}
# 获取第 2 个参数：Minecraft Docker 容器的名称
docker_container_name=$2
# 获取第 3 个参数：服务器目录
service_path=$3

# 检查是否提供了操作参数
if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "用法: $0 {start|stop|restart|backup} <docker_container_name> <service_path>"
    exit 1
fi

# 设定要备份的目录
backup_dir="$service_path/world"
# 设定备份文件存放的目录
backup_storage_dir="$service_path/backup"
# 日志文件路径
log_file="$service_path/minecraft_server_manager.log"


# 向日志文件中追加日志
logging() {
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】 - $1" | tee -a "${log_file}"
}

# 定义启动函数
start_server() {
    logging "启动 Minecraft 服务器 (${docker_container_name})..."

    # 检查容器是否【已经在运行】。如果是，就直接退出
    if [ "$(docker ps -q -f name="${docker_container_name}")" ]; then
        logging "服务器已经在运行中，无需操作。"
        return 0
    fi

    # 如果没在运行，再检查容器【是否存在】（无论是 created 还是 exited 状态）
    # `docker ps -a` 会列出所有状态的容器，只要有输出，就证明容器存在。
    if [ "$(docker ps -aq -f name="${docker_container_name}")" ]; then
        logging "找到一个已停止或刚创建的容器，正在启动..."
        docker start "${docker_container_name}"
        logging "服务器容器已启动。"
    else
        # 第三步：如果既没在运行，也根本不存在，就明确报错。
        logging "错误：找不到名为 ${docker_container_name} 的容器。请先使用 docker run 或 docker-compose 创建它。"
        return 1
    fi
}

# 定义停止函数
stop_server() {
    logging "停止 Minecraft 服务器 (${docker_container_name})..."

    # 检查 Docker 容器是否正在运行，如果没有运行，则直接返回
    if [ ! "$(docker ps -q -f name="${docker_container_name}")" ]; then
        logging "服务器已经处于停止状态。"
        return 0
    fi

    # 如果容器正在运行，则发送关服通知
    docker exec "${docker_container_name}" rcon-cli say "服务器将在 60 秒后关闭维护，请尽快下线！"
    sleep 60

    # 通过 RCON 确保所有数据被写入硬盘
    logging "通过 RCON 命令确保数据完全保存..."
    docker exec "${docker_container_name}" rcon-cli save-off
    docker exec "${docker_container_name}" rcon-cli save-all flush
    sleep 15
    
    # 给予 180 秒的超时时间，让 docker stop 来完成最后的清理工作
    docker stop -t 180 "${docker_container_name}"
    # 执行最直接的强制停止
    # docker kill "${docker_container_name}"

    logging "服务器容器已停止。"
}

# 定义重启函数
restart_server() {
    logging "重启 Minecraft 服务器 (${docker_container_name})..."

    # 直接调用 stop_server 函数
    stop_server
    
    # 确保在启动前有一点延迟
    sleep 200
    
    # 调用 start_server 函数
    start_server
}

# 定义备份存档函数
backup_server() {
    logging "备份 Minecraft 服务器 (${docker_container_name}) 的世界数据..."

    # 检查服务器是否正在运行，备份只能在运行时执行以确保数据一致性
    if [ ! "$(docker ps -q -f name="${docker_container_name}")" ]; then
        logging "错误：服务器未在运行，无法执行安全的在线备份。请先启动服务器。"
        return 1
    fi

    # 定义备份文件名，格式为 mc-backup-YYYY-MM-DD_HHMMSS.tar.gz
    local backup_filename
    backup_filename="mc-backup-$(date +%Y-%m-%d_%H%M%S).tar.gz"

    logging "通知服务器并暂停自动保存..."
    docker exec "${docker_container_name}" rcon-cli say "世界数据备份开始，可能会有短暂卡顿..."
    docker exec "${docker_container_name}" rcon-cli save-off
    docker exec "${docker_container_name}" rcon-cli save-all flush
    sleep 10 # 确保文件写入完成

    logging "正在创建压缩备份文件: ${backup_filename}"
    # 使用 -C 参数来避免在压缩包中包含长路径
    # --exclude 用来排除不需要备份的目录
    tar -czvf "${backup_storage_dir}/${backup_filename}" \
        -C "${backup_dir}" \
        --exclude='./logs' \
        --exclude='./crash-reports' \
        --exclude='./backups' \
        --exclude='./session.lock' \
        . # <-- 这个点号代表打包当前目录所有内容
    # 检查 tar 命令的退出状态，值为 0 表示成功
    local tar_exit_code=$?

    logging "重新开启服务器的自动保存..."
    docker exec "${docker_container_name}" rcon-cli save-on
    
    # 检查备份是否成功
    if [ ${tar_exit_code} -eq 0 ]; then
        logging "备份成功: ${backup_filename}"
        docker exec "${docker_container_name}" rcon-cli say "世界数据备份完成！"
    else
        logging "错误：备份打包失败！Tar 命令退出码: ${tar_exit_code}"
        docker exec "${docker_container_name}" rcon-cli say "§c错误：世界数据备份失败！请检查后台日志。"
        return 1
    fi

    logging "清理超过7天的旧备份..."
    find "${backup_storage_dir}" -name "mc-backup-*.tar.gz" -mtime +7 -delete
    logging "旧备份清理完成。"

}

# 检查执行方式，进行相应的操作
case "$mode" in
    start)
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        restart_server
        ;;
    backup)
        backup_server
        ;;
    *)
        echo "无效的参数: $1"
        echo "用法: $0 {start|stop|restart|backup}"
        exit 1
        ;;
esac

echo "" | tee -a "${log_file}"
echo "-------------------------------------------" | tee -a "${log_file}"

exit 0
```

4. 设置脚本权限：

```shell
chmod 755 minecraft_server_manager.sh
```

5. 用方式：
	1. 参数 1：执行方式，启动=start、重启=restart、停止=stop、备份=backup
	2. 参数 2：docker 容器名称
	3. 参数 3：游戏服务器所在目录

```shell
/vol1/1000/docker/script/cronicle/scripts/game/minecraft/minecraft_server_manager.sh start game-mc-bmc4 /vol1/1000/docker/game/minecraft/BMC4-v36
```

6. 使用 crontab 设置定时执行：
	1. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
	2. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 我的世界 forge BMC4-v36 服务器开启，周一至周五，每天 18 点
0 18 * * 1-5 /vol1/1000/docker/script/cronicle/scripts/game/minecraft/minecraft_server_manager.sh start game-mc-bmc4 /vol1/1000/docker/game/minecraft/BMC4-v36
# 我的世界 forge BMC4-v36 服务器开启，周六和周日，每天 9 点
0 9 * * 6,0 /vol1/1000/docker/script/cronicle/scripts/game/minecraft/minecraft_server_manager.sh start game-mc-bmc4 /vol1/1000/docker/game/minecraft/BMC4-v36
# 我的世界 forge BMC4-v36 服务器关闭，每天 23 点
0 23 * * * /vol1/1000/docker/script/cronicle/scripts/game/minecraft/minecraft_server_manager.sh stop game-mc-bmc4 /vol1/1000/docker/game/minecraft/BMC4-v36
# 我的世界 forge BMC4-v36 备份存档，每天 23:30
30 23 * * * /vol1/1000/docker/script/cronicle/scripts/game/minecraft/minecraft_server_manager.sh backup game-mc-bmc4 /vol1/1000/docker/game/minecraft/BMC4-v36
```

7. 使用 cronicle 设置定时执行：

![]https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FDocker%2Fattachments%2FPasted%20image%2020250617131001.png)








