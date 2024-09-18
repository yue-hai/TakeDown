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

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093536.png)

2. 点击实例 ID 后，会进入实例详情，点击重置密码

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093423.png)

3. 输入想要设置的密码，点击确定

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093648.png)

## 2、在云服务器网站中进行防火墙设置

1. 在实例详情中，点击安全组。然后点击管理规则

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093923.png)

2. 进入后点击手动添加，下方会出现设置
	1. 授权策略：`允许`
	2. 优先级：`1`；1 为最高优先级
	3. 协议类型：`自定义 TCP`，或者全部；若是选择了全部则代表开放了所有的端口，那么下面的端口范围无法选择
	4. 端口范围：若是选择了全部则不需输入；若是选择的自定义 TCP，<font color="#ff0000">则输入游戏的端口号</font> `7777`
	5. 授权对象：`0.0.0.0/0`
	6. 描述：随意
	7. 操作：上面的都设置好后，点击保存

![|600](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094029.png)

5. 在云服务器网站中进行防火墙设置完成

## 3、在命令行中进行防火墙设置

1. 在概览中点击远程连接

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092751.png)

2. 在弹出来的窗口中点击通过 Workbench 远程连接

![|675](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092854.png)

3. 可以选择密码认证，然后输入刚才设置的密码；也可以选择进士 SSH 密钥认证；点击确定进行连接

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094251.png)

3. 连接成功后，执行以下命令开放端口：

```shell
sudo ufw allow from any to any port 7777 proto tcp
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

# 四、环境配置

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

4. 下载 dotnet 6.0.0，泰拉联机依赖 dotnet
	1. 建议 Windows 下载后上传到 linux，因为 linux 下载太慢了：https://dotnet.microsoft.com/en-us/download/dotnet/6.0
	2. 愿意等待的话，启动 tModLoader 服务器时会自动下载

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230517084849.png)

5. dotnet 6.0.418 下载：[dotnet-sdk-6.0.418-linux-x64.tar.gz](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fdotnet-sdk-6.0.418-linux-x64.tar.gz)

# 五、创建用户，下载游戏服务器

1. 创建用户 steam，根据提示设置密码：

```shell
adduser steam
```

2. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

3. 在根目录下创建 `game/TShock` 目录，仅是为了方便管理

```shell
mkdir -p game/TShock
```

4. 进入 `game/TShock` 文件夹

```shell
cd game/TShock
```

5. 下载最新版本 5.2 的 TShock，Github 地址：https://github.com/Pryaxis/TShock/releases/download/v5.2.0/TShock-5.2-for-Terraria-1.4.4.9-linux-x64-Release.zip

```shell
wget https://github.com/Pryaxis/TShock/releases/download/v5.2.0/TShock-5.2-for-Terraria-1.4.4.9-linux-x64-Release.zip
```

6. 也可以本地下载后上传到 linux：
	1. <font color="#ff0000">若是版本更新了，请注意并修改版本号</font>
	2. TShock 压缩包下载：[TShock-5.2-for-Terraria-1.4.4.9-linux-x64-Release](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FTShock-5.2-for-Terraria-1.4.4.9-linux-x64-Release.zip)
7. 创建与 TShock 版本对应的目录，仅是为了方便管理

```shell
mkdir -p v5.2.0
```

8. 将下载好的压缩包解压到 `v5.2.0` 目录，会得到打包文件 `TShock-Beta-linux-x64-Release.tar`

```shell
unzip TShock-5.2-for-Terraria-1.4.4.9-linux-x64-Release.zip -d /home/steam/game/TShock/v5.2.0/
```

9. 继续解压文件 `TShock-Beta-linux-x64-Release.tar`

```shell
tar -xvf TShock-Beta-linux-x64-Release.tar
```

10. 将之前下载的 dotnet 6.0.0 上传到此目录；若是愿意等待的话，一会会自动下载
11. 运行 `TShock.Installer` 文件，安装 dotnet 环境
12. 下载成功后，会显示此页面：

```shell
TShock was improperly shut down. Please use the exit command in the future to prevent this.
TShock 5.2.0.0 (Intensity) now running.
AutoSave Enabled
Backups Enabled
Welcome to TShock for Terraria!
TShock comes with no warranty & is free software.
You can modify & distribute it under the terms of the GNU GPLv3.
[Server API] Info Plugin TShock v5.2.0.0 (by The TShock Team) initiated.
Terraria Server v1.4.4.9

n               New World
d <number>      Delete World

Choose World: 
```

# 六、使用 screen 后台运行泰拉瑞亚服务器

1. 输入命令创建终端，ttrts 为终端名称，可任意更改，输入完毕后会进入一个新的页面

```shell
screen -S ttrts
```

2. 启动服务器

```shell
/home/steam/game/TShock/v5.2.0/TShock.Installer
```

3. 输入 `n` 为创建新世界，`d + 世界ID` 为删除世界，回车确认
	1. 输入 `n` 创建新地图，回车确认

```shell
[Server API] Info Plugin TShock v5.2.0.0 (by The TShock Team) initiated.
Terraria Server v1.4.4.9

n               New World
d <number>      Delete World

Choose World: 
```

4. 选择地图大小，大地图耗费的服务器资源也就更多，请根据自己服务器配置来选择，回车确认
	1. 1：小型
	2. 2：中型
	3. 3：大型

```shell
Terraria Server v1.4.4.9                                                                       

1       Small                                                                                  
2       Medium                                                                                 
3       Large                                                                                  

Choose size:      
```

5. 选择难度，回车确认
	1. 1：经典
	2. 2：专家
	3. 3：大师
	4. 4：旅途

```shell
Terraria Server v1.4.4.9                                                                       

1       Classic                                                                                
2       Expert                                                                                 
3       Master                                                                                 
4       Journey                                                                                

Choose difficulty:      
```

6. 选择腐化形式，回车确认
	1. 1：随机
	2. 2：腐化
	3. 3：猩红

```shell
Terraria Server v1.4.4.9                                                                       

1       Random                                                                                 
2       Corrupt                                                                                
3       Crimson                                                                                

Choose world evil:    
```

7. 给世界取名，回车确认

```shell
Terraria Server v1.4.4.9                                                                       

Enter world name:     
```

8. 输入种子，一般不输入；继续回车则开始创建世界，创建成功后会返回主页

```shell
Terraria Server v1.4.4.9                                                                       

Enter Seed (Leave Blank For Random):   
```

9. 世界创建成功后，输入我们刚创建的新世界前面的序号，回车确认

```shell
Terraria Server v1.4.4.9

1               1
n               New World
d <number>      Delete World

Choose World: 
```

10. 选择最大人数，默认 16，回车确认

```shell
Terraria Server v1.4.4.9

Max players (press enter for 16): 
```

11. 服务器端口号，默认7777，与前面开放端口设置的要相同，最好不要改，回车确认

```shell
Terraria Server v1.4.4.9

Server port (press enter for 7777): 
```

12. 是否自动转发端口，默认是，回车确认

```shell
Terraria Server v1.4.4.9

Automatically forward port? (y/n): 
```

13. 设置服务器密码，输入密码后，回车确认

```shell
Terraria Server v1.4.4.9

Server password (press enter for none): 
```

14. 如果出现出现这些表示服务器启动成功

```shell
Terraria Server v1.4.4.9

Listening on port 7778
Type 'help' for a list of commands.

!!! UUID login is enabled. If a user's UUID matches an account, the server password will be bypassed.
!!! > Set DisableUUIDLogin to true in the config file and /reload if this is a problem.
!!! Login before join is enabled. Existing accounts can login & the server password will be bypassed.
!!! > Set DisableLoginBeforeJoin to true in the config file and /reload if this is a problem.
Login before join enabled. Users may be prompted for an account specific password instead of a server password on connect.
Login using UUID enabled. Users automatically login via UUID.
A malicious server can easily steal a user's UUID. You may consider turning this option off if you run a public server.
To setup the server, join the game and type /setup 6062438
This token will display until disabled by verification. (/setup)
: Server started

```

15. 记下上面黄字中的：`/setup 6062438`，里面的数字是服务器管理员密码，可以获得获得一段时间的超管特权
16. 不要关闭终端，打开游戏输入 ip 进入服务器
17. 成为临时超管：进入游戏后输入回车打开聊天栏，输入

```shell
/setup 6062438
```

18. 成为临时超管后，注册管理员账号，在liunx服务器终端输入：

```shell
user add 账号 密码 superadmin
```

19. 登录管理员账号，在游戏输入刚才注册的管理员账号密码；已登录过普通账户的用户不可登录管理员账号

```shell
/login 账号 密码
```

20. 普通玩家注册与登录，中间都要有空格，密码是自己自定义的，什么数字都可以
	1. 注册：`/register 密码`
	2. 登录：`/login 密码`
21. 保存并退出服务器，在服务器端输入：

```shell
exit
```

22. 按 `Ctrl + a + d` 可退出终端

# 七、服务器查看关闭等

1. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.ttrts</font> 的进程

```shell
screen -ls
```

2. 输入进程名字即可进入终端

```shell
screen -r XXX.ttrts
```

3. 结束进程

```shell
screen -S XXX.ttrts -X quit
```

# 八、更改服务器配置
## 1、基本配置文件，强制开荒与初始背包等

1. 文件位置：`/home/steam/game/TShock/v5.2.0/tshock/sscconfig.json`

```json
{
	"Settings": {
		"Enabled": false,                   // 强制开荒，false 为禁用，true 为启用
		"ServerSideCharacterSave": 5,       // 服务端角色存档数据的保存间隔时间，以分钟为单位
		"LogonDiscardThreshold": 250,       // 开启强制开荒后，检测到玩家背包里有违规物品时将提示
		"StartingHealth": 100,              // 初始生命值
		"StartingMana": 20,                 // 初始魔法值
		"StartingInventory": [              // 初始背包
		{
			"netID": -15,                   // 物品 ID
			"prefix": 0,                    // 前缀
			"stack": 1                      // 物品数量
		},
		{
			"netID": -13,
			"prefix": 0,
			"stack": 1
		},
		{
			"netID": -16,
			"prefix": 0,
			"stack": 1
		}
      ],
      "WarnPlayersAboutBypassPermission": true
	}
}
```

## 2、详细配置文件

1. 文件位置：`/home/steam/game/TShock/v5.2.0/tshock/config.json`

```json
{
    "Settings": {
        "ServerPassword": "000123",                     // 服务器的密码，不设置表示无密码
        "ServerPort": 7777,                             // 服务器端口【默认】
        "MaxSlots": 32,                                 // 服务器人数上限
        "ReservedSlots": 20,                            // 预留给管理员的通道数量
        "ServerName": "月海 TShock",                    // 服务器名称
        "UseServerName": false,                         // 是否使用服务器名称
        "LogPath": "tshock/logs",                       // 日志文件存放路径
        "DebugLogs": false,                             // 插件 调试是否开启，建议不要开，不然会刷屏
        "DisableLoginBeforeJoin": false,                // 踢出登录失败的玩家
        "IgnoreChestStacksOnLoad": false,               // 加载地图的时候是否检测箱子里物品堆叠上线
        "AutoSave": true,                               // 是否自动保存地图，强烈建议开启
        "AnnounceSave": true,                           // 自动保存提示（开启后自动保存会在聊天框里显示 saving world...）
        "ShowBackupAutosaveMessages": true,             // 自动保存提示（显示自动保存消息）
        "BackupInterval": 10,                           // 地图备份时间间隔/分钟
        "BackupKeepFor": 240,                           // 备份的地图保留时间
        "SaveWorldOnCrash": true,                       // 服务器崩溃时是否及时保存地图
        "SaveWorldOnLastPlayerExit": true,              // 在最后一个玩家退出后保存世界
        "InvasionMultiplier": 1,                        // 入侵规模，计算公式：入侵怪物数量=100+（X*HP＞200的玩家）
        "DefaultMaximumSpawns": 5,                      // 怪物刷新最大数值（设置越高怪物越多）
        "DefaultSpawnRate": 600,                        // 刷新怪物时间间隔，数值越大刷新越慢
        "InfiniteInvasion": false,                      // 是否无限制怪物入侵【开启后使用命令召唤的怪物入侵将达到200万只左右】
        "PvPMode": "normal",                            // PVP模式【normal表示可以正常使用PVP，always表示强制PVP，disabled表示强制PVE】
        "SpawnProtection": true,                        // 是否保护出生点【强烈建议设置】
        "SpawnProtectionRadius": 10,                    // 出生点保护范围【一格一个】
        "RangeChecks": true,                            // 范围检查（检查超出数组范围）（物品堆叠和其他的）
        "HardcoreOnly": false,                          // 仅允许困难模式的玩家进入服务器
        "MediumcoreOnly": false,                        // 仅允许中等模式的玩家进入服务器
        "SoftcoreOnly": false,                          // 仅允许软核模式的玩家进入服务器
        "DisableBuild": false,                          // 是否禁止建筑【开启后将无法破坏地图里任何东西】
        "DisableHardmode": false,                       // 禁止让世界进入困难模式（即肉山后）
        "DisableDungeonGuardian": false,                // 禁止攻打地牢守护者，与old man对话将会被立即传送到出生点
        "DisableClownBombs": false,                     // 禁止小丑（日食怪）扔炸弹爆炸
        "DisableSnowBalls": false,                      // 禁止雪人军团爆炸
        "DisableTombstones": true,                      // 关闭在玩家死亡时掉落的墓碑
        "DisablePrimeBombs": false,                     // 禁用炸弹
        "ForceTime": "normal",                          // 世界【normal表示昼夜正常交替，day表示出现极昼现象，night表示出现极夜现象】
        "DisableInvisPvP": false,                       // PVP状态下是否使隐身药水失效
        "MaxRangeForDisabled": 10,                      // 被冻结后最大移动距离
        "RegionProtectChests": false,                   // 领地内的箱子是否受到保护，PVE服务器强烈建议设置成true
        "RegionProtectGemLocks": true,                  // 领地内宝石锁保护
        "IgnoreProjUpdate": false,                      // 玩家是否可以忽略更新抛射物检查
        "IgnoreProjKill": false,                        // 玩家是否可以忽略击毁抛射物检查
        "AllowCutTilesAndBreakables": false,            // 允许玩家破坏易碎方块（草或者花）
        "AllowIce": false,                              // 允许玩家在无法建筑的地方放冰块
        "AllowCrimsonCreep": true,                      // 是否允许血腥之地扩散，PVE强烈建议设置成false
        "AllowCorruptionCreep": true,                   // 是否允许腐化之地扩散
        "AllowHallowCreep": true,                       // 是否允许神圣之地扩散
        "StatueSpawn200": 3,                            // 雕像在停止生成之前可以在200像素內生成多少个NPC
        "StatueSpawn600": 6,                            // 雕像在停止生成之前可以在600像素內生成多少个NPC
        "StatueSpawnWorld": 10,                         // 雕像生成NPC的最高上限
        "PreventBannedItemSpawn": false,                // 是否禁止用item指令和give指令获得被封禁（ban）掉的物品
        "PreventDeadModification": true,                // 防止玩家在死亡时与世界互动
        "PreventInvalidPlaceStyle": true,               // 防止玩家放置无效样式的方块
        "ForceXmas": true,                              // 是否开启圣诞节
        "ForceHalloween": true,                         // 是否开启万圣节
        "AllowAllowedGroupsToSpawnBannedItems": false,  // 是否允许有权限使用被封禁（ban）物品的用户组使用被封禁（ban）的物品
        "RespawnSeconds": 0,                            // 玩家死亡后复活时间/秒
        "RespawnBossSeconds": 0,                        // boss战时，玩家死亡复活时间
        "AnonymousBossInvasions": true,                 // 是否公告Boss重生或入侵事件开始
        "MaxHP": 500,                                   // 最大生命值（不算装备增益）
        "MaxMP": 200,                                   // 最大魔法值（不算装备增益）
        "BombExplosionRadius": 5,                       // 炸弹影响范围
        "GiveItemsDirectly": false,                     // 是否直接赠送物品
        "DefaultRegistrationGroupName": "default",      // 注册用户的默认用户组【如不了解组的规划请暂时不要改动】
        "DefaultGuestGroupName": "guest",               // 未注册用户的默认用户组
        "RememberLeavePos": true,                       // 记录离开位置，再次登录服务器将传送到上一次离开服务器的位置
        "MaximumLoginAttempts": 5,                      // 登录次数尝试最大限制，尝试次数过多将被移除（kick）服务器
        "KickOnMediumcoreDeath": false,                 // 移除（kick）死亡的中等难度的玩家
        "MediumcoreKickReason": "中等难度死亡后被移除",     // 中等难度的玩家被移除（kick）时的理由
        "BanOnMediumcoreDeath": false,                  // 封禁（ban）死亡的中等难度的玩家
        "MediumcoreBanReason": "中等难度死亡后被封禁",      // 中等难度的玩家被封禁（ban）时的理由
        "DisableDefaultIPBan": false,                   // 禁用默认ip
        "EnableWhitelist": false,                       // 是否开启白名单【true代表是，false代表否，以下都是】
        "WhitelistKickReason": "您不在白名单中",           // 因不在白名单而被拒绝进入服务器的提示
        "ServerFullReason": "Server is full",           // 因服务器人满而被拒绝进入服务器的提示
        "ServerFullNoReservedReason": "服务器已满，没有保留的空位",  // 因服务器人满并预留给管理员的位置也满的情况下被拒绝进入服务器的提示
        "KickOnHardcoreDeath": false,                   // 是否踢出死亡的硬核玩家
        "HardcoreKickReason": "硬核难度死亡后被移除",       // 踢出死亡的硬核玩家时给出的提示
        "BanOnHardcoreDeath": false,                    // 是否在硬核玩家死亡后封锁他
        "HardcoreBanReason": "硬核难度死亡后被封禁",        // 封锁死亡的硬核玩家时给出的提示
        "KickProxyUsers": true,                         // 如果GeoIP可用，禁止使用代理进入服务器的玩家
        "RequireLogin": false,                          // 是否开启强制注册登录
        "AllowLoginAnyUsername": true,                  // 允许玩家登录的账号与角色名不符
        "AllowRegisterAnyUsername": false,              // 是否允许注册任何用户名，PVE服务器强烈建议设置成false
        "MinimumPasswordLength": 4,                     // 新账号密码的最短长度
        "BCryptWorkFactor": 7,                          // 决定使用的 BCrypt工作因子,增加此值会改变玩家密码的加密算法
        "DisableUUIDLogin": false,                      // 是否禁止UUID登录
        "KickEmptyUUID": false,                         // 是否移除（kick）空UUID的玩家
        "TilePaintThreshold": 15,                       // 一秒刷漆上限
        "KickOnTilePaintThresholdBroken": false,        // 当玩家超过设置的刷漆阈值时是否踢出服务器
        "MaxDamage": 1175,                              // 玩家可以造成的最大伤害
        "MaxProjDamage": 1175,                          // 射弹最大伤害
        "KickOnDamageThresholdBroken": false,           // 超过最大伤害是否踢出服务器
        "TileKillThreshold": 60,                        // 一秒挖掘，破坏物块的上限
        "KickOnTileKillThresholdBroken": false,         // 当玩家超过设置的挖掘物块阈值时是否踢出服务器
        "TilePlaceThreshold": 32,                       // 一秒摆放物块的上限
        "KickOnTilePlaceThresholdBroken": false,        // 当玩家超过设置的摆放物块阈值时是否踢出服务器
        "TileLiquidThreshold": 50,                      // 一秒释放液体的上限
        "KickOnTileLiquidThresholdBroken": false,       // 当玩家超过设置的液体阈值时是否踢出服务器
        "ProjIgnoreShrapnel": true,                     // 计算弹药使用上限是否忽略爆炸产生的碎片
        "ProjectileThreshold": 50,                      // 一秒使用弹药数量的上限【包括魔法攻击】
        "KickOnProjectileThresholdBroken": false,       // 当玩家超过设置的弹药阈值时是否踢出服务器
        "HealOtherThreshold": 50,                       // 一秒内发送超过治疗（绿字）数据包上限
        "KickOnHealOtherThresholdBroken": false,        // 当玩家超过设置的治疗阈值时是否踢出服务器
        "SuppressPermissionFailureNotices": false,      // 禁止显示权限失败通知
        "DisableModifiedZenith": false,                 // 禁用修改顶点
        "DisableCustomDeathMessages": true,             // 禁用自定义死亡消息
        "CommandSpecifier": "/",                        // 指令标志，在聊天框里首位输入该符号视为指令
        "CommandSilentSpecifier": ".",                  // 指定哪个字符串开头会以静音的方式处理指令
        "DisableSpewLogs": true,                        // 禁止将服务器日志展示给玩家
        "DisableSecondUpdateLogs": false,               // 防止服务器更新检查写入日志档案
        "SuperAdminChatRGB": [255, 255, 255],           // 超级管理员聊天字体颜色
        "SuperAdminChatPrefix": "(Super Admin) ",       // 超级管理员发言前缀（位于名字之前）
        "SuperAdminChatSuffix": "",                     // 超级管理员发言后缀（位于名字之后）
        "EnableGeoIP": false,                           // 显示玩家IP的所在地【有可能侵犯他人隐私，建议不要开启】
        "DisplayIPToAdmins": false,                     // 是否将玩家的IP地址展示给管理员
        "ChatFormat": "{1}{2}{3}: {4}",                 // 聊天格式【{1}为前缀，{2}为玩家名称，{3}为后缀，{4}为聊天内容】
        "ChatAboveHeadsFormat": "{2}",                  // 在玩家头顶显示的内容
        "EnableChatAboveHeads": false,                  // 是否在玩家头上显示聊天信息
        "BroadcastRGB": [127,255,212],                  // 广播的字体颜色
        "StorageType": "sqlite",                        // 数据库类型
        "SqliteDBPath": "tshock.sqlite",                // 数据库的文件名字
        "MySqlHost": "localhost:3306",                  // 数据库连接地址
        "MySqlDbName": "",                              // 数据库的名字
        "MySqlUsername": "",                            // 登录数据库的账号
        "MySqlPassword": "",                            // 登录数据库的密码
        "UseSqlLogs": false,                            // 数据库的日志是否打印，建议不要开，不然数据库文件会变的很大
        "RevertToTextLogsOnSqlFailures": 10,            // SQL日志必须在回复到文本日志之前无法插入日志的次数
        "RestApiEnabled": false,                        // 是否启用RestAPI接口
        "RestApiPort": 7878,                            // RestAPI接口的端口
        "LogRest": false,                               // 是否打印Rest日志
        "EnableTokenEndpointAuthentication": false,     // 是否通过权限认证才能使用rest接口
        "RESTMaximumRequestsPerInterval": 5,            // 拒绝请求前连线池中最大的rest请求数
        "RESTRequestBucketDecreaseIntervalMinutes": 1,  // rest请求连线池以分钟为单位所减少1单位数量的频率（最小为1分钟）
        "ApplicationRestTokens": {                      // 设置rest接口的密钥，提示名和权限
        }
    }
}
```

# 九、服务器权限与指令

## 1、用户组权限

1. 下表等级从上到下依次递增，更高级的组拥有较低等级组的所有权限

| 组名 | 中文名 | 拥有的权限(代表性的) |
| ---- | ---- | ---- |
| guest | 游客​ | 注册、登陆、发送服务器消息， 在TShock4.5.5 以上的版本中不可被删除 |
| default | 玩家​ | 进行受限制的正常游戏(平民玩家) |
| vip |  | 预留服务器位，重命 名NPC，召唤 boss/入侵，虫洞 |
| newadmin | 新手管理员​ | k ick玩家，查看玩家 Index，设置重生点，调时间 |
| admin | 管理员​ | ban 玩家，管理传送点，生成 boss/怪物，tp |
| trustedadmin | 受信任管理员​ | 刷/给予物品(`/i` 和 `/g`)，无视各种限制，上传本地存档作为 SSC 存档 |
| owner | 服主 | tshock.su(使用指令绕过权限，基本等同于 superadmin) |
| superadmin | 超级管理员 | 具有所有权限，**注意，这个组是只读的，无法为这个用户组手动配置权限** |

2. owner 为 TShock4.4.0 以上版本添加的默认用户组，适用于服主希望参加游戏进程的情况​
3. owner 组具有权限 `tshock.su`，自身并不像 superadmin 一样具有所有权限​
4. 相反地，owner 组的用户可以通过 `/su` 指令临时获得超级管理员权限，或是通过 `/sudo` 指令绕过权限检测​
5. 这允许在 owner 组用户正常进行游戏（指 SSC 模式下不会因 `tshock.ignore.bypassssc` 权限忽略背包）时管理服务器
6. superadmin 现在更多用于 Rest/后台/插件中的操作，建议不要在参与游戏流程时使用 superadmin组

## 2、指令说明

1. 在服务器控制面板输入指令可以不打 `/`
2. 在游戏内输入需要在指令面前打 `/`，如 `:/help` 
3. `/` 可以在配置文件修改
4. `【】`内内容选填

## 3、设定管理员

1. 指令：`user group 玩家名字 用户组`
2. 描述：更改某一玩家的用户组
3. 指令示例：`/user group 玩家1 superadmin`
4. 示例效果：将玩家1 的用户组改成 superadmin（把玩家1 设为超管）

## 4、所有玩家可用

| 指令                      | 描述                                                              |
| ------------------------- | ----------------------------------------------------------------- |
| register 密码             | 注册账户(角色名字为账号,简幻欢默认的服务器广播设置的提示是错的) |
| register 用户名 密码      | 使用自己设置的用户名和密码注册(可以自定义用户名，方便记忆)      |
| login                     | 直接登录(需要先注册)                                            |
| login 密码                | 使用游戏角色名称和密码登录                                      |
| login 用户名 密码         | 用用户名和密码登录                                            |
| party 聊天内容            | 队内聊天                                                        |
| p 聊天内容                | 同上一条相同效果                                                |
| whisper 玩家名字 私聊内容 | 私聊指定玩家                                                    |
| playing                   | 显示当前服务器所有在线玩家。                                    |

## 5、仅管理员可用

### ①、封禁玩家相关

| 指令 | 描述 |
| ---- | ---- |
| ban add 玩家1 【理由】 | 永久封禁一个玩家 |
| ban list | 查看所有被封禁的用户的名称，角色 UUID，玩家设备 IP |
| ban del [ban ID] | 解封玩家的名称，或角色 UUID 或玩家设备 IP |

### ②、用户组相关

| 指令                          | 描述                                                                                                                                                                                                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| roup list 【页码】            | 显示所有已设置的用户组(常用的就三个)                                                                                                                                                                                                              |
| group prefix 用户组 前缀      | 设置指定用户组聊天前缀                                                                                                                                                                                                                            |
| group suffix 用户组 后缀      | 设置指定用户组聊天后缀                                                                                                                                                                                                                            |
| group addperm 用户组 权限     | 给指定用户组指定权限，这里的权限比较特殊<br>即使你输了一个根本不存在的权限，你输入的内容也会被加入到对应用户组的权限列表里，<br>当你要安装插件时，可以提前给用户组相应权限，例如 `:/group addperm LV0 tshock.npc.startdd2`，<br>效果：LV0 用户组可以召唤撒旦军团 |
| group delperm 用户组名称 权限 | 删除指定用户组的指定权限                                                                                                                                                                                                                          |

### ③、禁用物品相关

| 指令                                         | 描述                                   |
| -------------------------------------------- | -------------------------------------- |
| itemban add 物品英文名称或物品ID             | 封禁掉指定物品                       |
| itemban allow 物品英文名称或物品IP 用户组    | 允许指定用户组使用该被封禁的物品     |
| itemban del 物品英文名称或物品ID             | 将指定物品解除封禁                   |
| itemban disallow 物品英文名称或物品ID 用户组 | 取消某一用户组对该封禁物品的使用权限 |
| itemban list 【页码】                        | 列出所有被封禁掉的物品               |

### ④、领地相关

| 指令                              | 描述                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| region set 1                      | 输入之后拿镐子敲击一个方块，设置领地的一个角<br>输入指令后，镐子不会挖掉方块，所以不用换成镐力小的镐子 |
| region set 2                      | 用镐子敲击，设置领地的另一个角。                                                                     |
| region define 名称                | 将刚才设置的两个角连成矩形，并将其变成私有领地。                                                     |
| region delete 名称                | 删除某一个私有领地                                                                                   |
| region list 【页码】              | 显示当前所有领地                                                                                     |
| region allow 玩家名称 领地名称    | 将某一领地分享给另一位玩家                                                                           |
| region remove 玩家名称 领地名称   | 取消将某一领地分享给某位玩家                                                                         |
| region allowg 用户组名称 领地名称 | 将某一领地分享给某一个用户组                                                                         |
|region removeg 用户组名称 领地名称|将某一领地的分享权限取消至某个用户组 |

### ⑤、禁言相关

| 指令                 | 描述                 |
| -------------------- | -------------------- |
| mute 用户名 【理由】 | 禁言某位玩家       |
| unmute 用户名        | 解除某位玩家的禁言 |

### ⑥、给予物品相关

| 指令                                                        | 描述                                                                             |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------- |
| give 物品英文名称或物品 ID 玩家名称 【数量】【前缀英文或 ID】 | 给指定玩家指定物品<br>ID 可以去 Wiki 上查找<br>或者使用 `TL ID` 不填数量则默认最大堆叠数 |
| item 物品英文名称或物品 ID【数量】【前缀英文或 ID】           | 给自己指定物品                                                                 |
| i 物品英文名称或物品 ID【数量】【前缀英文或 ID】              | 与上条指令相同效果                                                             |

### ⑦、传送相关

| 指令              | 描述                           |
| ----------------- | ------------------------------ |
| home              | 回到自己设置的出生点【床】。 |
| spawn             | 回到地图【服务器】的出生点。 |
| tp 玩家名称       | 传送到指定玩家身边。         |
| pos               | 获取当前位置的坐标           |
| tppos x坐标 y坐标 | 传送到特定的一个坐标         |
| tphere 玩家名称   | 将指定玩家传送到你的身边     |

### ⑧、世界设置相关

| 指令 | 描述 |
| ---- | ---- |
| hardmode | 如当前地图处于简单模式【肉山前】，使用该指令立刻转至困难模式【肉山后】，反亦之。 |
| worldmode 难度 | 设置世界难度，难度有：journey(旅途)、normal(普通)、expert(专家)、master(大师) |
| setspawn | 将你脚下踩得这块方块设置为地图的出生点 |
| time 24时间 | 设置地图的时间<br>例如：`/time 12:00`，效果：将游戏时间调到 `12:00` |
|  |  |

### ⑨、玩家模式相关

| 指令             | 描述                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| godmode          | 将自己设置为伪上帝模式                                                                          |
| godmode 玩家名字 | 将指定玩家设置为上帝模式<br>如果你的 Tshock 版本低，那么如果该伤害超过了你的血量上限，你仍然会死亡。 |

### ⑩、传送点相关

| 指令                          | 描述                                         |
| ----------------------------- | -------------------------------------------- |
| warp 传送点名称               | 传送到该传送点(已注册玩家可用)             |
| warp add 传送点名称           | 在当前脚下设置一个传送点并命名             |
| warp del 传送点名称           | 删除某一传送点。                           |
| warp list 【页数】            | 显示当前服务器开的地图所设置的所有传送点。 |
| warp send 玩家名称 传送点名称 | 将某一用户立即强制传送到某一传送点‍‍‍‍。   |

### ⑪、掉落物相关

| 指令                             | 描述                                                                                                                                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clear item/npc/projectile [半径] | 清理掉以你角色为半径的item(掉落物)/npc(NPC,包括城镇NPC和敌怪)/projectile(发出去的弹药),<br>半径可以不写，默认为50<br>使用 clear npc 清理掉的 NPC 会直接消失,不会掉落物品 |

### ⑫、清理NPC

| 指令 | 描述 |
| ---- | ---- |
| butcher | 杀死全图的敌怪(不包括城镇NPC)，有掉落物，可以直接杀死有护盾的柱子 |
| butcher ID | 杀死全图指定的NPC或者敌怪 |

