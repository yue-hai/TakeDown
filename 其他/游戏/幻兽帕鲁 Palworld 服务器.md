# 一、购买服务器

1. ~~推荐阿里云学生机~~
2. 阿里云新用户优惠网址：https://www.aliyun.com/minisite/goods
3. 选择轻量型服务器，4 核 16G 可以使用
    - 地域：随意
    - 镜像类型：系统镜像
    - 系统镜像：Ubuntu 22.04（或 Ubuntu 的其他版本）
4. 付款

# 二、设置服务器

## 1、重置密码

1. 进入云服务器 ECS 后，点击实例 ID

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093536.png)

2. 点击实例 ID 后，会进入实例详情，点击重置密码

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093423.png)

3. 输入想要设置的密码，点击确定

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093648.png)

## 2、在云服务器网站中进行防火墙设置

1. 在实例详情中，点击安全组。然后点击管理规则

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093923.png)

2. 进入后点击手动添加，下方会出现设置
	1. 授权策略：`允许`
	2. 优先级：`1`；1 为最高优先级
	3. 协议类型：~~`自定义 TCP`~~，<font color="#ff0000">0.1.5.1 之后变成 UDP 了</font>（所以最好这两个都开，万一以后又变了），或者全部；若是选择了全部则代表开放了所有的端口，那么下面的端口范围无法选择
	4. 端口范围：若是选择了全部则不需输入；若是选择的自定义 ~~TCP~~（<font color="#ff0000">0.1.5.1 之后需选择 UDP</font>），<font color="#ff0000">则输入游戏的端口号</font> `8211`
	5. 授权对象：`0.0.0.0/0`
	6. 描述：随意
	7. 操作：上面的都设置好后，点击保存

![|600](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094029.png)

5. 在云服务器网站中进行防火墙设置完成

## 3、在命令行中进行防火墙设置

1. 在概览中点击远程连接

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092751.png)

2. 在弹出来的窗口中点击通过 Workbench 远程连接

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092854.png)

3. 可以选择密码认证，然后输入刚才设置的密码；也可以选择进士 SSH 密钥认证；点击确定进行连接

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094251.png)

3. 连接成功后，执行以下命令开放端口：

```shell
sudo ufw allow from any to any port 8211
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
dd if=/dev/zero of=/root/swapfile bs=1M count=16384
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

# 四、安装服务器的基本条件

1. 更新软件源

```shell
sudo apt update
```

2. 安装远程管理工具 screen

```shell
apt install -y screen
```

3. 安装 SteamCmd 运行所需环境

```shell
# 这些操作要在 root 中进行，根据你的系统选择不同指令。

# Ubuntu/Debian 64 位
apt -y install lib32gcc-s1

# RedHat/CentOS 32 位
yum -y install glibc libstdc++

# RedHat/CentOS 64 位
yum -y install glibc.i686 libstdc++.i686
```

# 五、创建用户，下载游戏服务器

1. 创建用户 steam，设置密码

```shell
adduser steam
```
   
2. 进入 steam 用户，创建 `steamcmd` 文件夹，再进入 `steamcmd` 目录

```shell
su steam && cd ~ && mkdir steamcmd && cd steamcmd
```

3. 下载 steamcmd

```shell
wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
```

4. 解压 steamcmd

```shell
tar -zxvf steamcmd_linux.tar.gz
```

5. 启动 SteamCMD，以 `Steam>` 开头的就代表进入了 SteamCMD

```shell
./steamcmd.sh
```
   
```shell
Redirecting stderr to '/root/Steam/logs/stderr.txt'
[  0%] Checking for available updates...
[----] Verifying installation...
Steam Console Client (c) Valve Corporation
  -- type 'quit' to exit --
Loading Steam API...OK

Steam>
```

6. 匿名登录 steam
	1. 若是想自定义下载目录，需在登陆前设置：`force_install_dir /home/steam/game/PalWorld`

```shell
login anonymous
```

7. 下载幻兽帕鲁，更新游戏时同样使用此命令
 
```shell
app_update 2394010 validate
```

8. 等待下载完后输入 quit 或者 （ctrl + c） 退出 SteamCMD，至此服务器已经下载好了，接下来就是配置服务器

# 六、使用 screen 后台运行服务器

### ①、启动服务器

1. 进入幻兽帕鲁服务端根目录

```shell
cd /home/steam/Steam/steamapps/common/PalServer/
```

2. 启动服务器；按 `Ctrl + a + d` 可退出终端；这几个参数据官方所说可以实现多线程加速，建议加上，更多参数可以查看：[官方指南](https://tech.palworldgame.com/dedicated-server-guide)

```shell
screen -S PalWorld

./PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS 
```

3. 获取 screen 列表，会有一个 `XXX.PalWorld` 的进程
 
```
screen -ls
```

4. 输入进程名字即可进入终端

```
screen -r PalWorld
```

5. 结束进程
 
```
screen -S PalWorld -X quit
```

### ②、修改配置

1. 服务器初次启动时，配置文件是空的；
2. 此时需要关闭服务器，然后：
	1. 修改 `/home/steam/Steam/steamapps/common/PalServer/DefaultPalWorldSettings.ini` 中的配置，
	2. 修改完毕后，将这个文件中的内容全部复制到 `/home/steam/Steam/steamapps/common/PalServer/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini` 中
	3. 然后重新启动服务器
3. 配置的说明在下方

### ③、自动重启脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/Steam/steamapps/common/PalServer
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch pal_server_restart.sh

# 创建日志文件：
touch pal_server.log
```

3. 编写自动重启脚本代码：`nano pal_server_restart.sh`

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="PalWorld"
# 脚本所在路径
path="/home/steam/Steam/steamapps/common/PalServer"

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

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 5

# 发送启动 PalServer 命令，包括运行参数，将命令发送到会话中，并模拟按下回车键；等待 20 秒，确保 PalServer 启动完成
send_command "$path/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDSD\r"

# 向日志文件中追加内容
echo "$(date)：帕鲁服务器重启已完成" >> $path/pal_server.log
```

4. 设置脚本权限：

```shell
chmod 755 pal_server_restart.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令。比如要在每天凌晨 1 点执行命令：

```shell
# 帕鲁服务器重启，晚上 1 点
00 1 * * * /home/steam/Steam/steamapps/common/PalServer/pal_server_restart.sh
```

8. 在 cron 表达式中，参数用于指定定时任务的执行时间。一个标准的 cron 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
9. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置

### ④、自动关服脚本

> 1. 这游戏写的太差了，连续开一天 32G 内存都能吃光
> 2. 所以根据上面的代码改了一下，分成了两个脚本，一个开服一个关服
> 3. 只有在玩的时间段内开启，其他时间关闭
> 4. 这里设定的关服时间是晚上 1 点，开服时间是 早上 9:30

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/Steam/steamapps/common/PalServer
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch pal_server_close.sh

# 创建日志文件：
touch pal_server.log
```

3. 编写自动关服脚本代码：`nano pal_server_close.sh`

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="PalWorld"
# 脚本所在路径
path="/home/steam/Steam/steamapps/common/PalServer"
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

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03'

# 向 pal_server.log 文件中追加日志
echo "【${current_time}】帕鲁服务器已关闭" >> $path/pal_server.log
echo "" >> $path/pal_server.log
```

4. 设置脚本权限：

```shell
chmod 755 pal_server_close.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令。比如要在每天凌晨 1 点执行命令：

```shell
# 帕鲁服务器关闭，晚上 1 点
00 1 * * * /home/steam/Steam/steamapps/common/PalServer/pal_server_close.sh
```

### ⑤、自动开服脚本

1. 进入游戏服务器目录：
   
```shell
cd /home/steam/Steam/steamapps/common/PalServer
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch pal_server_start.sh

# 创建日志文件：
touch pal_server.log
```

3. 编写开服脚本代码：`nano pal_server_start.sh`

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="PalWorld"
# 脚本所在路径
path="/home/steam/Steam/steamapps/common/PalServer"
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

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 5

# 发送启动 PalServer 命令，包括运行参数，将命令发送到会话中，并模拟按下回车键；等待 20 秒，确保 PalServer 启动完成
send_command "$path/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDSD\r"

# 向 pal_server.log 文件中追加日志
echo "【${current_time}】帕鲁服务器已启动" >> $path/pal_server.log
```

4. 设置脚本权限：

```shell
chmod 755 pal_server_start.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令。比如要在每天 9:30 执行命令：

```shell
# 帕鲁服务器启动，早上 9 点 30
30 9 * * * /home/steam/Steam/steamapps/common/PalServer/pal_server_start.sh
```

# 七、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

1. 服务端配置文件：`~/Steam/steamapps/common/PalServer/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini`

### ②、重要路径

1. 服务端主目录：`~/Steam/steamapps/common/PalServer/`

## 2、主配置文件 `PalWorldSettings.ini` 参数说明

| 参数                                                        | 说明                                                                                       |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Difficulty=3,                                             | 难度：1、2、3整数<br>简单、普通、困难，影响怪物血量之类的数值                                                       |
| DayTimeSpeedRate=1.000000,                                | 白天流逝速度 0.1~5 之间                                                                          |
| NightTimeSpeedRate=1.000000,                              | 夜晚流逝速度 0.1~5 之间                                                                          |
| ExpRate=3.000000,                                         | 经验倍率 0.1~3 之间                                                                            |
| PalCaptureRate=2.000000,                                  | 帕鲁捕捉概率倍率，0.5~2 之间                                                                        |
| PalSpawnNumRate=2.000000,                                 | 帕鲁出现数量倍率，0.5~3 之间，比如 2，boss 也会出现 2 个。                                                    |
| PalDamageRateAttack=1.000000,                             | 全部帕鲁攻击伤害（友方帕鲁和野怪帕鲁同时生效）<br>倍率 0.1~5 之间，越高伤害越高，自行抉择                                       |
| PalDamageRateDefense=1.000000,                            | 全部帕鲁承受伤害（友方帕鲁和野怪帕鲁同时生效）<br>倍率 0.1~5 之间，越低越抗揍，自行抉择                                        |
| PlayerDamageRateAttack=2.0000000,                         | 玩家攻击伤害倍率 0.1~5 之间，越高输出越高                                                                 |
| PlayerDamageRateDefense=0.1000000,                        | 玩家承受伤害倍率 0.1~5 之间，越低越抗揍                                                                  |
| PlayerStomachDecreaceRate=0.1000000,                      | 玩家饱食度降低倍率 0.1~5 之间，越低越耐饿                                                                 |
| PlayerStaminaDecreaceRate=0.1000000,                      | 玩家耐力降低倍率 0.1~5 之间，数值越低 耐力降低越慢                                                            |
| PlayerAutoHPRegeneRate=5.000000,                          | 玩家生命值恢复倍率 0.1~5 之间，数值越高自动回复越快                                                            |
| PlayerAutoHpRegeneRateInSleep=5.000000,                   | 玩家睡眠生命值恢复倍率 0.1~5 之间，数值越高睡觉回血越快                                                          |
| PalStomachDecreaceRate=0.1000000,                         | 帕鲁饱食度降低倍率 0.1~5 之间，越低越耐饿                                                                 |
| PalStaminaDecreaceRate=0.1000000,                         | 帕鲁耐力降低倍率 0.1~5 之间，数值越低 耐力降低越慢                                                            |
| PalAutoHPRegeneRate=5.000000,                             | 帕鲁生命值恢复倍率 0.1~5 之间，数值越高自动回复越快                                                            |
| PalAutoHpRegeneRateInSleep=5.000000,                      | 帕鲁睡眠时生命值恢复倍率 0.1~5 之间，数值越高自动回复越快                                                         |
| BuildObjectDamageRate=1.000000,                           | 对建筑物伤害倍率 0.5~3 之间，建议调低，调高了会不小心拆掉自己的房子                                                    |
| BuildObjectDeteriorationDamageRate=0.1000000,             | 建筑物劣化速度倍率 0~10 之间，建议调 0，建筑不会自己损坏。                                                        |
| CollectionDropRate=3.000000,                              | 可采集物品掉落倍率 0.5~3 之间，调高了树木和矿物获取一次性获取更多                                                     |
| CollectionObjectHpRate=0.5000000,                         | 可采集物品生命值倍率 0.5~3 之间，调低可以加快挖矿速度                                                           |
| CollectionObjectRespawnSpeedRate=0.5000000,               | 可采集物品刷新间隔，0.5~3 之间，调低可加快野矿刷新速度                                                           |
| EnemyDropItemRate=3.000000,                               | 道具掉落量倍率，0.5~3 之间<br>如果调到 3，比如击杀掉黑市商人，默认掉一把钥匙，会变成三把，金币掉落量也会三倍。                            |
| DeathPenalty=None,                                        | 死亡惩罚：None 不掉落，Item 只掉物品不掉装备，ItemAndEquipment 掉物品和装备，All 全都掉<br>建议 None 提高游戏舒适性，不然每次死都得跑尸 |
| bEnablePlayerToPlayerDamage=False,                        | 启用玩家对玩家伤害功能，True 或者 False                                                                |
| bEnableFriendlyFire=True,                                 | 该参数意义待定，实测不是友伤（同一工会的，这个参数为False或者True都不会友伤），也不是火焰伤害。                                     |
| bEnableInvaderEnemy=True,                                 | 是会发生袭击事件（野怪入侵基地），True 是开启，改为 False 关闭。                                                   |
| bActiveUNKO=False,                                        | UNKO 应该是日语指代的粪便，个人理解是否开启帕鲁粪便吧好像，建议 False 不动；                                             |
| bEnableAimAssistPad=True,                                 | 启用平板辅助瞄准 True 是开启，False 关闭                                                               |
| bEnableAimAssistKeyboard=False,                           | 启用键盘辅助瞄准 True 是开启，False 关闭                                                               |
| DropItemMaxNum=5000,                                      | 世界内掉落物品数量上限，指代野外可以捡到的东西数量上限，数量多了吃服务器性能。默认是 3000，上限 5000，看自己需要修改                          |
| DropItemMaxNum_UNKO=100,                                  | 帕鲁屎掉落上限？不确定。可以不管                                                                         |
| BaseCampMaxNum=128,                                       | 大本营最大数，128 默认即可，多人游戏时如果有多个工会，会限制所有工会加起来的营地上限。                                            |
| BaseCampWorkerMaxNum=20,                                  | 可分派至据点工作的帕鲁数量上限，1~20 之间整数。默认 15。<br>01-28 更新：实测该参数目前不生效，既不是营地可指派帕鲁上限，也不是玩家可扔出干活的帕鲁上限）    |
| DropItemAliveMaxHours=2.000000,                           | 掉落物品存在最大时长，默认 1，上限不确定                                                                    |
| bAutoResetGuildNoOnlinePlayers=False,                     | 自动重置没有在线玩家的公会，默认 False 即可。                                                               |
| AutoResetGuildTimeNoOnlinePlayers=72.000000,              | 无在线玩家时自动重置生成时间，默认 72 即可。                                                                 |
| GuildPlayerMaxNum=20,                                     | 公会成员最大数量，默认 20 即可                                                                        |
| PalEggDefaultHatchingTime=0.0000000,                      | 帕鲁蛋默认孵化时间，默认 72 是小时，调成0即可没有孵化时间。<br>0.1~72 之间可以自己输入                                      |
| WorkSpeedRate=3.000000,                                   | 工作速率，影响流水线物品生产速度，默认 1，建议 3                                                               |
| bIsMultiplay=False,                                       | 多人游戏，默认 false，如果是局域网创建服务器玩家不影响，False 即可。                                                 |
| bIsPvP=False,                                             | PVP 是否开启                                                                                 |
| bCanPickupOtherGuildDeathPenaltyDrop=False,               | 可拾取其他公会的死亡掉落物，默认 False 即可                                                                |
| bEnableNonLoginPenalty=True,                              | 启用不登录惩罚，应该指代的是无人在线时是否会出现袭击事件，默认 True 应该也没影响，担心出问题的可以改 False                              |
| bEnableFastTravel=True,                                   | 启用快速旅行，默认 True 即可                                                                        |
| bIsStartLocationSelectByMap=True,                         | 通过地图选择起始位置默认 True 即可，如果改为 False 则全部出生在初始台地                                               |
| bExistPlayerAfterLogout=False,                            | 注销后玩家仍然存在，就是是否删注销玩家的档，跟朋友一起玩的默认 False 即可                                                 |
| bEnableDefenseOtherGuildPlayer=False,                     | 启用防御其他公会玩家功能，默认 False 即可。                                                                |
| CoopPlayerMaxNum=4,                                       | 邀请码服务器玩家最大人数                                                                             |
| ServerPlayerMaxNum=32,                                    | 服务器玩家最大人数                                                                                |
| ServerName="Default Palworld Server",                     | 服务器名称                                                                                    |
| ServerDescription="",                                     | 服务器简介                                                                                    |
| AdminPassword="",                                         | 管理员密码                                                                                    |
| ServerPassword="",                                        | 服务器密码                                                                                    |
| PublicPort=8211,                                          | 服务器对外端口                                                                                  |
| PublicIP="",                                              | 服务器 IP                                                                                   |
| RCONEnabled=False,                                        | 启用 RCON                                                                                  |
| RCONPort=25575,                                           | RCON 端口                                                                                  |
| Region="",                                                | 地区                                                                                       |
| bUseAuth=True,                                            | 使用授权                                                                                     |
| BanListURL="https://api.palworldgame.com/api/banlist.txt" | 封禁玩家名单（需外网）                                                                              |

# 八、管理服务器

1. 客户端进入游戏服务器后，按下回车键打开聊天框，输入 `/AdminPassword 管理员密码` 来认证为管理员
2. 管理员密码是配置文件 `PalWorldSettings.ini` 中的 `` 字段
3. 管理员指令

| 管理员指令                               | 指令说明                                                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| /Shutdown {Seconds} {MessageText}        | 使用可选的计时器和/或消息正常关闭服务器，以通知服务器中的玩家。                                          |
| /DoExit                                  | 立即强制关闭服务器。不建议使用此选项，除非您遇到技术问题或可以接受可能丢失数据的情况。                   |
| /Broadcast {MessageText}                 | 向服务器中的所有玩家广播消息。                                                                           |
| /KickPlayer {PlayerUID or SteamID}       | 将玩家踢出服务器。                                                                                       |
| /BanPlayer {PlayerUID or SteamID}        | 禁止玩家进入服务器。玩家在解禁之前将无法重新加入服务器。                                                 |
| /TeleportToPlayer {PlayerUID or SteamID} | 仅限游戏内，立即传送到目标玩家                                                                           |
| /TeleportToMe {PlayerUID or SteamID}     | 仅限游戏内，立即将目标玩家传送到您身边。                                                                 |
| /ShowPlayers                             | 显示所有已连接玩家的信息                                                                                 |
| /Info                                    | 显示服务器信息                                                                                           |
| /Save                                    | 将世界数据保存到磁盘。有助于确保您的好友、玩家和其他数据在停止服务器或执行有风险的游戏选项之前得到保存。 |

# 九、问题

## 1、启动服务器时显示没有文件 `steamclient.so`

### ①、问题

- 启动服务器时显示：

```shell
.steam/sdk64/steamclient.so: cannot open shared object file: No such file or directory
```

### ②、解决

1. 创建目录 `/.steam/sdk64/`

```shell
mkdir -p ~/.steam/sdk64/
```

2. 匿名登录 steam，下载 `Steamworks SDK Redist`

```shell
cd /home/steam/steamcmd/

login anonymous 

app_update 1007 

quit
```

3. 复制 `steamclient.so` 文件

```shell
cp "/home/steam/Steam/steamapps/common/Steamworks SDK Redist/linux64/steamclient.so" ~/.steam/sdk64/
```

## 2、启动服务器时显示 FAIL

1. 启动服务器时显示如下提示：

```shell
steam@yan:~/Steam/steamapps/common/PalServer$ /home/steam/Steam/steamapps/common/PalServer/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDSD
Shutdown handler: initalize.
Increasing per-process limit of core file size to infinity.
dlopen failed trying to load:
steamclient.so
with error:
steamclient.so: cannot open shared object file: No such file or directory
[S_API] SteamAPI_Init(): Loaded '/home/steam/.steam/sdk64/steamclient.so' OK.  (First tried local 'steamclient.so')
CAppInfoCacheReadFromDiskThread took 6 milliseconds to initialize
dlmopen steamservice.so failed: steamservice.so: cannot open shared object file: No such file or directory
Setting breakpad minidump AppID = 2394010
[S_API FAIL] Tried to access Steam interface SteamUser021 before SteamAPI_Init succeeded.
[S_API FAIL] Tried to access Steam interface SteamFriends017 before SteamAPI_Init succeeded.
[S_API FAIL] Tried to access Steam interface STEAMAPPS_INTERFACE_VERSION008 before SteamAPI_Init succeeded.
[S_API FAIL] Tried to access Steam interface SteamNetworkingUtils004 before SteamAPI_Init succeeded.
```

2. 此处显示 `[S_API FAIL]` 没有影响，可以正常进入游戏即可

## 3、

