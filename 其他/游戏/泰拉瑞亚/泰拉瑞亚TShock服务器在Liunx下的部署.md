# 一、购买服务器
1. 推荐阿里云学生机，网址：https://developer.aliyun.com/plan/grow-up
2. 选择轻量型服务器，1核2G就可以，2核2G更好
    - 地域：随意
    - 镜像类型：系统镜像
    - 系统镜像：CentOS 7.3（或CentOS的其他版本）
3. 付款

# 二、设置服务器
1. 防火墙设置：
    - 点击<font color="#dd0000">服务器列表</font>，然后点击服务器进入设置
      - 点击<font color="#dd0000">3服务器安全设置</font>
        - 点击点击<font color="#dd0000">已设置2条</font>
          - 点击点击<font color="#dd0000">添加规则</font>
            - 端口范围设置为点击<font color="#dd0000">7777</font>，点击确定
2. 打开服务器终端

# 三、设置SWAP分区
- 由于ECS云服务器镜像安装好是没有给系统分配软件交换分区Swap的，所以这里我们需要手动分配一下，以免我们的泰拉瑞亚在挂机在服务器途中突然关闭。如果足够1GB则跳过这一步直接开始搭建游戏！
- 这里提一下vi编辑器的基本用法：
进入文本后按键盘上的insert按钮开始编辑，按esc退出编辑，上下左右移动光标，输入:wq保存并退出。
1. 查看SWAP设置了多少
    ```Apache
    free –m
    ```
2. 删除原来的Swap分区
    ```
    swapoff –a
    ```
3. 新增SWAP分区
    ```Apache
    dd if=/dev/zero of=/root/swapfile bs=1M count=4096
    ```
4. 格式化交换分区文件
    ```Apache
    mkswap /root/swapfile
    ```
5. 启用swap分区文件
    ```Apache
    swapon /root/swapfile
    ```
6. 添加开机启动，打开fstab
    ```Apache
    vi /etc/fstab
    ```
7. 在众多的文本最后添加一行
    ```Apache
    /root/swapfile swap swap defaults 0 0
    ```
8. 退出编辑，按一下<font color="#dd0000">Esc</font>，然后退出
    ```Apache
    :wq
    ```
9. 重启下是否生效
    ```Apache
    reboot
    ```
10. 重启后输入指令查看下SWAP是否增加
    ```Apache
    free -m
    ```

# 四、下载软件
1. 安装下载工具
    ```Apache
    yum install -y wget
    ```
2. 安装解压工具
   - 安装zip的过程中会出现IS this ok 询问的一句话，这里输入一个y代表同意并继续即可。
    ```Apache
    yum install unzip
    ```
3. 安装远程管理工具screen 
    ```Apache
    yum install -y screen
    ```
4. 安装mono
	```
	yum install mono-complete
    ```
    - mono的蓝奏云链接：https://wwa.lanzous.com/iNJuto3bbla

# 五、创建用户，授予权限，下载服务器
1. 创建用户yan：
   ```
   useradd yan
   ```
2. 设置用户yan的密码，在出现的提示后输入密码
   ```
   passwd yan
   ```
3. 修改用户权限，root帐号执行：
    ```
    chown -R :yan /home/yan/
    chmod -R 777 /home/yan/
    ```
4. 登录普通用户yan
   ```
   su yan
   ```
6. 进入普通用户yan，并进入根目录
    ```
    su yan
    ```
    ```
    cd ~
    ```
6. 在根目录下创建opt与GAME文件夹，在GAME下创建Terraria文件夹，在Terraria下创建TShock
    ```Apache
    mkdir -p opt GAME/Terraria/TShock
    ```
7. 进入opt文件夹
    ```Apache
    cd opt
    ```
8. 下载最新版本1.4.2.1的TShock
    ```Apache
    wget https://github.com/Pryaxis/TShock/releases/download/v4.5.0/TShock4.5.0_Terraria1.4.2.1.zip
    ```
   - TShock的github链接：https://github.com/Pryaxis/TShock/releases
   - TShock的蓝奏云链接：https://wwa.lanzous.com/iB3djo3b5eh
9. 将下载好的压缩包解压到TShock文件夹
    ```Apache
    unzip TShock4.5.0_Terraria1.4.2.1.zip -d ../GAME/Terraria/TShock/TShock4.5.0_Terraria1.4.2.1
    ```

# 六、配置泰拉瑞亚服务器
1.  启动服务器
    ```Apache
    cd ~
    ```
    ```Apache 
    cd GAME/Terraria/TShock/TShock4.5.0_Terraria1.4.2.1
    ```
    ```
    mono TerrariaServer.exe
    ```
2. 输入 n 创建新地图，回车确认，d为删除地图
    ```
    Error Logging Enabled.
    TerrariaAPI Version: 2.1.0.0 (Protocol v1.4.1.2 (234), OTAPI 1.4.1.2)
    TShock 4.4.0.0 (Go to sleep Patrikkk, Icy, Chris, Death, Axeel, Zaicon, hakusaro, Zack, and Yoraiz0r <3) now running.
    AutoSave Enabled
    Backups Disabled
    Welcome to TShock for Terraria!
    TShock comes with no warranty & is free software.
    You can modify & distribute it under the terms of the GNU GPLv3.
    [Server API] Info Plugin TShock v4.4.0.0 (by The TShock Team) initiated.
    Terraria Server v1.4.1.2

    n		New World
    d <number>	Delete World

    Choose World: 
    ```
3. 选择地图大小，大地图耗费的服务器资源也就更多，请根据自己服务器配置来选择，回车确认,1、2、3依次增大
    ```
    Terraria Server v1.4.1.2

    1	Small
    2	Medium
    3	Large

    Choose size: 
    ```
4. 选择难度，1：经典，2：专家，3：大师，4：旅程，回车确认
    ```
    Terraria Server v1.4.1.2

    1	Classic
    2	Expert
    3	Master
    4	Journey

    Choose difficulty: 
    ```
5. 选择世界类型，1：随机，2：腐化，3：猩红，回车确认
    ```
    Terraria Server v1.4.1.2

    1	Random
    2	Corrupt
    3	Crimson

    Choose world evil: 
    ```
6. 给世界取名，回车确认
    ```
    Terraria Server v1.4.1.2

    Enter world name: 
    ```
7. 输入种子，默认为随机，回车确认
    ```
    Terraria Server v1.4.1.2

    Enter Seed (Leave Blank For Random):
    ```
8. <font color="#dd0000">等待</font>
9. 输入我们刚创建的新世界前面的序号，回车确认
    ```
    Terraria Server v1.4.1.2

    1		1
    n		New World
    d <number>	Delete World

    Choose World: 
    ```
10. 选择最大人数，默认16，回车确认
    ```
    Terraria Server v1.4.1.2

    Max players (press enter for 16): 
    ```
11. 服务器端口号，默认7777，与前面设置的要相同，最好不要改，回车确认
    ```
    Terraria Server v1.4.1.2

    Server port (press enter for 7777): 
    ```
12. 是否自动转发端口，默认是，输入y，也可直接回车
    ```
    Terraria Server v1.4.1.2

    Automatically forward port? (y/n): 
    ```
13. 设置服务器密码，也可不设置直接回车
    ```
    Terraria Server v1.4.1.2

    Server password (press enter for none): 
    ```
14. <font color="#dd0000">等待</font>
15. 如果出现出现这些表示服务器启动成功
	```
    Terraria Server v1.4.1.2

    Listening on port 7777
    Type 'help' for a list of commands.

    To setup the server, join the game and type /setup 1935277
    This token will display until disabled by verification. (/setup)
    : Server started
    ```
    - 记下黄字中的：/setup 1935277
16. 不要关闭终端，打开游戏输入ip进入服务器
17. 玩家注册与登录，中间都要有空格
    注册：`/register 密码`
    登录：`/login 密码`
18. 成为临时超管
	- 进入游戏后输入回车打开聊天栏，输入
	```
    /setup 1935277
    ```
19. 注册管理员账号，在liunx服务器终端输入：
	```
    user add 账号 密码 superadmin
    ```
20. 登录管理员账号，在游戏输入刚才注册的管理员账号密码
	```
    /login 账号 密码
    ```
    - 已登录过普通账户的用户不可登录管理员账号
21. 保存并退出服务器，在服务器端输入：
    ```
    exit
    ```

# 七、更改服务器配置文件与指令权限
1. 强制开荒与初始背包等（sscconfig.json文件）配置
   网页链接：[TSHOCK从零开始的使用教学](https://www.bbstr.net/t/tshock.381/)
   文件位置：GAME/Terraria/TShock/TShock4.5.0_Terraria1.4.2.1/tshock/$\color{red}{sscconfig.json}$
   ```
   {
        "Settings": {
            "Enabled": false,                   //强制开荒，false为禁用，true为启用
            "ServerSideCharacterSave": 5,       //服务端角色存档数据的保存间隔时间，以分钟为单位
            "LogonDiscardThreshold": 250,       //开启强制开荒后，检测到玩家背包里有违规物品时将提示
            "StartingHealth": 100,              //初始生命值
            "StartingMana": 20,                 //初始魔法值
            "StartingInventory": [              //初始背包
            {
                "netID": -15,                   //物品ID
                "prefix": 0,                    //前缀
                "stack": 1                      //物品数量
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
            ]
        }
    }
   ```
   - 用户组权限
   ```
    guest​              注册、登陆、发送服务器消息
    default​            进行受限制的正常游戏(平民玩家)
    vip​                预留服务器位，重命名NPC，召唤boss/入侵，虫洞
    newadmin​           kick玩家，查看玩家Index，设置重生点，调时间
    admin​              ban玩家，管理传送点，生成boss/怪物，tp
    trustedadmin​       刷/给予物品(/i和/g)，无视各种限制，上传本地存档作为ssc存档
    superadmin​         具有所有权限
   ```
2. 游戏服务器内各种参数详细设置
   网页链接：[TSHOCK所有指令详细讲解](https://tieba.baidu.com/p/3770859135?see_lz=1)
   文件位置：GAME/Terraria/TShock/TShock4.5.0_Terraria1.4.2.1/tshock/$\color{red}{config.json}$
   ```
   {
        "Settings": {                               //设置
            "ServerPassword": "",                   //服务器的密码，不设置表示无密码
            "ServerPort": 7777,                     //服务器端口【默认7777】
            "MaxSlots": 8,                          //服务器人数上限
            "ReservedSlots": 20,                    //预留给管理员的通道数量
            "ServerName": "",                       //服务器名称
            "UseServerName": false,                 //是否使用服务器名称
            "LogPath": "tshock",                    //日志文件存放路径
            "DebugLogs": true,
            "DisableLoginBeforeJoin": false,        //踢出登录失败的玩家
            "IgnoreChestStacksOnLoad": false,       //加载地图的时候是否检测箱子里物品堆叠上线
            "AutoSave": true,                       //是否自动保存地图，强烈建议开启
            "AnnounceSave": true,                   //自动保存的时候是否进行提示
            "ShowBackupAutosaveMessages": true,     //是否显示服务器备份信息
            "BackupInterval": 0,                    //地图备份时间间隔/分钟
            "BackupKeepFor": 60,                    //备份的地图保留时间
            "SaveWorldOnCrash": true,               //服务器崩溃时是否及时保存地图
            "SaveWorldOnLastPlayerExit": true,
            "InvasionMultiplier": 1,                //入侵规模，计算公式：入侵怪物数量=100+（X*HP＞200的玩家）
            "DefaultMaximumSpawns": 5,              //怪物刷新最大数值（设置越高怪物越多）
            "DefaultSpawnRate": 600,                //刷新怪物时间间隔，数值越大刷新越慢
            "InfiniteInvasion": false,              //是否无限制怪物入侵【开启后使用命令召唤的怪物入侵将达到200万只左右】
            "PvPMode": "normal",                    //PVP模式【normal表示可以正常使用PVP，always表示强制PVP，disabled表示强制PVE】
            "SpawnProtection": false,               //是否保护出生点【强烈建议设置】
            "SpawnProtectionRadius": 10,            //出生点保护范围【一格一个】
            "RangeChecks": true,
            "HardcoreOnly": false,                  //仅允许困难模式的玩家进入服务器
            "MediumcoreOnly": false,                //仅允许中等模式的玩家进入服务器
            "DisableBuild": false,                  //是否禁止建筑【开启后将无法破坏地图里任何东西】
            "DisableHardmode": false,               //禁止让世界进入困难模式（即肉山后）
            "DisableDungeonGuardian": false,        //禁止攻打地牢守护者，与old man对话将会被立即传送到出生点
            "DisableClownBombs": false,             禁止小丑往出生点扔炸弹【大概】
            "DisableSnowBalls": false,              //禁止使用雪球
            "DisableTombstones": true,              //是否移除墓碑
            "ForceTime": "normal",                  //THE WORLD！【normal表示昼夜正常交替，day表示出现极昼现象，night表示出现极夜现象】
            "DisableInvisPvP": false,               //PVP状态下是否使隐身药水失效
            "MaxRangeForDisabled": 10,              //被冻结后最大移动距离
            "RegionProtectChests": false,           //领地内的箱子是否受到保护，PVE服务器强烈建议设置成true
            "RegionProtectGemLocks": true,
            "IgnoreProjUpdate": false,
            "IgnoreProjKill": false,
            "AllowCutTilesAndBreakables": false,
            "AllowIce": false,                      //是否禁止冰的扩散【这啥？】
            "AllowCrimsonCreep": false,              //是否允许血腥之地扩散，PVE强烈建议设置成false，下同
            "AllowCorruptionCreep": false,           //是否允许腐化之地扩散
            "AllowHallowCreep": false,               //是否允许神圣之地扩散
            "StatueSpawn200": 3,
            "StatueSpawn600": 6,
            "StatueSpawnWorld": 100,                //雕像召唤物品的最高上限
            "PreventBannedItemSpawn": false,        //是否禁止用item指令和give指令获得被封禁（ban）掉的物品
            "PreventDeadModification": true,
            "PreventInvalidPlaceStyle": true,
            "ForceXmas": false,                     //是否开启圣诞节
            "ForceHalloween": false,                //是否开启万圣节
            "AllowAllowedGroupsToSpawnBannedItems": false,
                                                    //是否允许有权限使用被封禁（ban）物品的用户组使用被封禁（ban）的物品
            "RespawnSeconds": 5,                    //玩家死亡后复活时间/秒
            "RespawnBossSeconds": 10,               //BOSS战时玩家死亡后复活时间/秒
            "AnonymousBossInvasions": true,
            "MaxHP": 500,                           //最大生命值
            "MaxMP": 200,                           //最大魔法值
            "BombExplosionRadius": 5,
            "DefaultRegistrationGroupName": "newadmin​",//注册用户的默认用户组【如不了解组的规划请暂时不要改动】
            "DefaultGuestGroupName": "guest",       //未注册用户的默认用户组
            "RememberLeavePos": false,              //记录离开位置，再次登录服务器将传送到上一次离开服务器的位置
            "MaximumLoginAttempts": 9,              //登录次数尝试最大限制，尝试次数过多将被移除（kick）服务器
            "KickOnMediumcoreDeath": false,         //移除（kick）死亡的中等难度的玩家
            "MediumcoreKickReason": "Death results in a kick",//中等难度的玩家被移除（kick）时的理由
            "BanOnMediumcoreDeath": false,          //封禁（ban）死亡的中等难度的玩家
            "MediumcoreBanReason": "Death results in a ban",//中等难度的玩家被封禁（ban）时的理由
            "EnableWhitelist": false,               //是否开启白名单
            "WhitelistKickReason": "You are not on the whitelist.",//因不在白名单而被拒绝进入服务器的提示
            "ServerFullReason": "Server is full",   //因服务器人满而被拒绝进入服务器的提示
            "ServerFullNoReservedReason": "Server is full. No reserved slots open.",
            "KickOnHardcoreDeath": false,
            "HardcoreKickReason": "Death results in a kick",
            "BanOnHardcoreDeath": false,
            "HardcoreBanReason": "Death results in a ban",
            "KickProxyUsers": true,
            "RequireLogin": false,
            "AllowLoginAnyUsername": true,
            "AllowRegisterAnyUsername": false,
            "MinimumPasswordLength": 4,
            "HashAlgorithm": "sha512",
            "BCryptWorkFactor": 7,
            "DisableUUIDLogin": false,
            "KickEmptyUUID": false,
            "TilePaintThreshold": 15,
            "KickOnTilePaintThresholdBroken": false,
            "MaxDamage": 1175,
            "MaxProjDamage": 1175,
            "KickOnDamageThresholdBroken": false,
            "TileKillThreshold": 60,
            "KickOnTileKillThresholdBroken": false,
            "TilePlaceThreshold": 32,
            "KickOnTilePlaceThresholdBroken": false,
            "TileLiquidThreshold": 50,
            "KickOnTileLiquidThresholdBroken": false,
            "ProjIgnoreShrapnel": true,
            "ProjectileThreshold": 50,
            "KickOnProjectileThresholdBroken": false,
            "HealOtherThreshold": 50,
            "KickOnHealOtherThresholdBroken": false,
            "TileRectangleSizeThreshold": 50,
            "KickOnTileRectangleSizeThresholdBroken": false,
            "CommandSpecifier": "/",
            "CommandSilentSpecifier": ".",
            "DisableSpewLogs": true,
            "DisableSecondUpdateLogs": false,
            "SuperAdminChatRGB": [
            255,
            255,
            255
            ],
            "SuperAdminChatPrefix": "(Super Admin) ",
            "SuperAdminChatSuffix": "",
            "EnableGeoIP": false,
            "DisplayIPToAdmins": false,
            "ChatFormat": "{1}{2}{3}: {4}",
            "ChatAboveHeadsFormat": "{2}",
            "EnableChatAboveHeads": false,
            "BroadcastRGB": [
            127,
            255,
            212
            ],
            "StorageType": "sqlite",
            "SqliteDBPath": "tshock.sqlite",
            "MySqlHost": "localhost:3306",
            "MySqlDbName": "",
            "MySqlUsername": "",
            "MySqlPassword": "",
            "UseSqlLogs": false,
            "RevertToTextLogsOnSqlFailures": 10,
            "RestApiEnabled": false,
            "RestApiPort": 7878,
            "LogRest": false,
            "EnableTokenEndpointAuthentication": false,
            "RESTMaximumRequestsPerInterval": 5,
            "RESTRequestBucketDecreaseIntervalMinutes": 1,
            "ApplicationRestTokens": {}
        }
    }
   ```
3. Tshock内置指令详解
   >指令：itemban
        介绍：封禁掉某一物品。
        >>子命令：
            itemban add 物品英文名称或物品ID--封禁掉某一物品
            itemban allow 物品英文名称或物品IP 用户组名称--允许某一用户组使用该被封禁的物品
            itemban del 物品英文名称或物品ID--将某一物品解除封禁
            itemban disallow 物品英文名称或物品ID 用户组名称--取消某一用户组对该封禁物品的使  用  权限
            itemban list 【页码】--列出所有被封禁掉的物品
            备注：没有权限使用该物品的用户组会被冻结。

    >指令：region
        介绍：设置领地，极为重要！
        >>子命令：
            region set 1/2 --设置临时边界点。
            region clear --清除设置的临时边界点
            region define 名字 --给刚才设置的临时边界起名，将其变成私有领地。
            region delete 领地名称 --删除某一个私有领地
            region name -显示当前位置的领地名称
            region list 【页码】 --显示当前所有领地
            region resize 领地名称 --重新设置领地大小
            region allow 玩家名称 领地名称 --将某一领地分享给另一位玩家
            region remove 玩家名称 领地名称 --取消将某一领地分享给某位玩家
            region allowg 用户组名称 领地名称 --将某一领地分享给某一个用户组
            region removeg 用户组名称 领地名称 --将某一领地的分享权限取消至某个用户组
            region info 领地名称 --显示领地信息
            region protect 领地名称 true/false --是否开启保护某个领地
            region z 领地名称 优先等级 --设置领地的优先权
            >>>备注：如何设置领地？
                先输入region set 1，之后敲击你需要设置区域的左上角
                下一步同理，输入region set 2之后再敲击设置区域的右下角！
                输入region define 名称 设置成自己的私有领地吧！
                私有领地不可被除领主之外的人破坏或建筑，除非共享给某个玩家。

    >指令：kick
        介绍：将玩家移除服务器，克熊孩子专用【其实ban更好...】。
        kick 玩家名称 【理由】
    
    >指令：projban
        介绍：在服务器里封禁某种弹药使用权限。
        >>子命令：
        projban add 弹药ID --封禁某种弹药
        projban allow 弹药ID 用户组名称 --允许某一用户组使用该被封禁的弹药
        projban del 弹药ID --恢复某一个弹药的使用权限
        projban disallow 弹药ID 用户组名称 --解除某一用户组使用某个弹药的权限
        projban list --列出所有被封禁的弹药

    >指令：mute
        介绍：禁言某玩家，刷屏的你们惨咯~
        mute 用户名 【理由】--禁言某位玩家
        unmute 用户名 --解除某位玩家的禁言

    >指令：savessc
        介绍：手动保存服务器的玩家存档。

    >指令：tempgroup
        介绍：‘设置临时用户组，不明意义。

    >指令：userinfo
        介绍：查询某一用户信息。
        usernfo 玩家姓名
        相关命令：
        ui 玩家姓名 --ui就是userinfo的简写

    >指令：annoy
        介绍：骚扰【shenmegui】一个玩家。
        annoy 玩家名称 骚扰时间
        备注：怎么骚扰的，可以亲自试验一下，23333

    >指令：confuse
        介绍：让某个玩家不再受控制。【即，方向箭无法正确的控制角色移动】【这命令真NB】
        confuse 玩家名称
        备注：对同一个玩家输入两次该命令将解除不受控制状态。


    >指令：rocket
        介绍：在某位玩家旁边发射一个火箭。
        rocket 玩家名称


    >指令：firework
        介绍：在某位玩家身边发射烟花。
        firework 玩家名称 【red/green/blue/yellow】


    >指令：checkupdates
        介绍：检查服务器【tshock】的更新状况。

    >指令：off
        介绍：关闭服务器并且保存服务器数据。
        相关命令：
        exit --同上
        指令：off-nosave
        介绍：关闭服务器但不保存服务器数据。服务器被熊炸了之后立即使用该命令，不要犹豫。
        相关命令：
        exit-nosave --真是没事闲着==

    >指令：reload
        介绍：重新载入config文件，不必重新启动服务器去加载config文件了，但是部分配置还必须重启服务器才能生效。

    >指令：restart
        介绍：重启服务器。

    >指令：serverpassword
        介绍：修改服务器的密码。

    >指令：version
        介绍：显示当前tshock版本信息。

    >指令：whitelist
        介绍：管理服务器白名单【需在config配置文件里把白名单打开】

    >指令：give
        介绍：给予玩家一个物品。
        give 物品英文名称或物品ID 玩家名称（可以是自己） 【数量】【英文前缀（武器用）】
        相关命令：
        g 物品英文名称或物品ID 玩家名称（可以是自己） 【数量】【英文前缀（武器用）】 --即give的简写

    >指令：item
    介绍：给予自己一个物品。
        item 物品英文名称或物品ID【数量】【英文前缀（武器用）】
        相关命令：
        i 物品英文名称或物品ID【数量】【英文前缀（武器用）】--不解释

    >指令：butcher
        介绍：杀死当前服务器里的怪物或可爱的npc。
        butcher 怪物id/npc
        备注：不写ID将表示杀死所有除了玩家的生物。

    >指令：invade
        介绍：开启军团入侵指令！
    invade 入侵军团
    备注：入侵军团的类型有：goblin【哥布林】，snowman【雪人军团】，pirate【海盗】。
    另外，南瓜月，血月，霜月有其他指令。

    >指令：maxspawn
        介绍：设置怪物最大刷新量，但只是临时的。
        备注：关闭服务器后失效，永久修改最大怪物刷新量请去修改config配置文件。

    >指令：bloodmoon
        介绍：开启血月！

    >指令：grow
        介绍：在你的旁边生长一颗植株，可以达到无限资源的目的。【本来就可以无线资源吧..】
        grow tree/epictree/mushroom/cactus/herb
        备注：这几个英文单词指得分别是：树，棕桐树，蘑菇，仙人掌，草药。

    >指令：dropmeteor
        介绍：使用该指令将会随机生成一个陨石！！！请在主城周围使用该命令否则后果自负。

    >指令：eclipse
        介绍：开启日食，配合config配置修改成极昼模式可以达到永久日食的目的。

    >指令：forcexmas
        介绍：是否开启圣诞模式，注意，有是否选项！
        forcexmas true/false

    >指令：fullmoon
        介绍：使用该指令开启满月！

    >指令：hardmode
        介绍：如当前地图处于简单模式【肉山前】，使用该指令立刻转至困难模式【肉山后】，反亦之。

    >指令：protectspawn
        介绍；开启临时保护出生点模式，范围在config配置文件里修改，不过也只是临时性的。

    >指令：rain
        介绍：是否开启或停止下雨。
        rain stop/start --前者停止正在下的雨，后者则开始下雨

    >指令：setspawn
        介绍：将你脚下踩得这块方块设置为地图的出生点，这个是永久的！但是仍然可以输入该指令改变地图出生点。

    >指令：settle
        介绍：立刻强制所有液体平衡。

    >指令：wind
        介绍：改变风速？
        wind 数值

    >指令：time
        介绍：设置地图的时间
        time day/night/dusk/noon/midnight
        备注：day代表白天，游戏时间为4:00整，这个时间点表示刚刚天亮。night表示傍晚，时间未知。dusk代表黄昏，表示刚刚步入夜晚。noon表示正午，太阳当空照~一天中最亮的时候。midnight代表午夜。

    >指令：world
        介绍：显示当前地图信息 。

    >指令：buff
        介绍：给予自己一种buff，可以自定义时间哦！
        buff buff序号或者英文名称 【持续的时间】
        备注：时间选项不添加默认为60秒。


    >指令：clear
        介绍：清理以你为O点的半径中的怪物/物品/弹幕。
        clear item/npc/projectile 【半径】
        备注：半径不填写大概默认为全部。npc代表怪物，第三者代表弹幕，item代表掉落物品。
        并且在minecraft里，clear指令是清空玩家背包的指令。

    >指令：gbuff
        介绍：给予某个玩家一种buff。
        gbuff 玩家名称 buff名称或buffID 【时间】
        相关指令：
        buffplayer 玩家名称 buff名称或buffID 【时间】
        备注：时间一栏不填写默认为60秒。


    >指令：godmode
        介绍：这将会给一个人上帝的权限！！！
        godmode --给予自己上帝的权利！
        godmode 用户名 --给予一个玩家上帝的权利！
        上帝的权利：当你收到任何伤害【这种伤害会减少你的体力】的时候，你马上恢复你血量上限的血量【比如你有200点血量上限，你收到伤害时，会立刻回满200点血。】。可是如果该伤害是致命的，仍然会死亡。【比如地牢守护者】


    >指令：heal
        介绍：治疗一个玩家【包括hp和mp】
        heal --治疗自己
        heal 玩家名称 --治疗某一个玩家


    >指令：kill
        介绍：干死某位玩家233。
        kill 玩家名称 --杀掉玩家

    >指令：stats
        介绍：显示当前服务器的信息。

    >指令：warp
        介绍：管理当前服务器所开的地图的传送点，不同的地图有不同的传送点管理。
        子命令：
        warp 传送点 --传送到该传送点，服务器的注册用户默认拥有该指令。
        warp add 传送点名称 --在当前脚下设置一个传送点并命名，所有传送点都是公共的。
        warp del 传送点名称 --删除某一传送点。
        warp list 【页数】 --显示当前服务器开的地图所设置的所有传送点。
        warp send 玩家名称 传送点名称 --将某一用户立即强制传送到某一传送点。
        warp hide 传送点名称 ture/false --设置传送点是否显示，ture为是，反之。
        备注：warp可以在任意一个地方建立传送点，也可以用来设置服务器活动传送点，所以如无特殊情况，请不要授予注册玩家管理传送点的权限。

    >指令：whisper
        介绍：发送一种私聊信息给予某位玩家。
        whisper 聊天内容 --私聊某位玩家。
        相关命令：
        tell 聊天内容 --还是私聊某位玩家。
        w 聊天内容 --whisper的简写。

    >指令：aliases
        介绍：查询某一命令的相同命令【比如上一条指令的whisper，就有两个相同命令，即tell和w】。

    >指令：help
        介绍：查询当前用户组可供使用的命令。

    >指令：motd
        介绍：显示服务器设置的欢迎信息。

    >指令：playing
        介绍：显示当前服务器所有在线玩家。
        相关命令：
        online
        who

    >指令：rule
        介绍：显示服务器设置的规则！新手最好先看服规，否则后果自负。

4. Tshock内置权限详解






# 八、使用screen后台运行泰拉瑞亚服务器
1. 输入命令创建终端，tr为终端名称，可任意更改，输入完毕后会进入一个新的页面
    ```Apache
    screen -S tr
    ```
2. 启动游戏
    ```
    cd ~
    ```
    ```Apache
    cd GAME/Terraria/TShock/TShock4.4.0_Pre15_Terraria1.4.1.2
    ```
    ```
    mono TerrariaServer.exe
    ```
3. 按Ctrl+a+d可退出终端

# 九、泰拉瑞亚服务器查看关闭等
1. 获取screen列表，会有一个<font color="#dd0000">XXX.tr</font>的进程
    ```Apache
    screen -ls
    ```
2. 输入进程名字即可进入终端
    ```Apache
    screen -r XXX.tr
    ```
3. 结束进程
    ```Apache
    screen -S XXX.tr -X quit
    ```
    
# 泰拉瑞亚服务器配置至此结束
