# 一、游戏服务器信息

1. 端口号：`29600`、`29602`，游戏端口说明：

| 端口        | 协议 | 说明                                           |
| ----------- | ---- | ---------------------------------------------- |
| 8080        | TCP  | Web 控制台                                     |
| 8081        | TCP  | Telnet 端口（这个建议不要放行）                |
| 8082        | TCP  | 如果安装了 Alloc 的 mods，这个端口可以展示地图 |
| 26900/26902 | UDP  | 客户端通讯                                               |

2. 需要通过 SteamCmd 进行下载
3. 首先进行：[服务器设置](游戏服务器购买和设置.md)

# 二、下载游戏服务器

1. 进入 steam 用户，再进入 `steamcmd` 目录

```shell
su steam && cd ~ && cd steamcmd
```

2. 启动 SteamCMD，以 `Steam>` 开头的就代表进入了 SteamCMD

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

3. 匿名登录 steam
	1. 若是想自定义下载目录，需在登陆前设置：`force_install_dir /home/steam/game/7DaysToDieServer`

```shell
login anonymous
```

4. 下载七日杀，更新游戏时同样使用此命令
 
```shell
app_update 294420 validate
```

5. 等待下载完后输入 quit 或者 （ctrl + c） 退出 SteamCMD，至此服务器已经下载好了，接下来就是配置服务器

# 三、使用 screen 后台运行服务器

1. 进入七日杀服务端根目录

```shell
cd "/home/steam/Steam/steamapps/common/7 Days to Die Dedicated Server/"
```

2. 启动服务器；按 `Ctrl + a + d` 可退出终端

```shell
screen -S 7DaysServer

./startserver.sh -configfile=serverconfig.xml
```

3. 获取 screen 列表，会有一个 `XXX.7DaysServer` 的进程
 
```shell
screen -ls
```

4. 输入进程名字即可进入终端

```shell
screen -r XXX
```

5. 结束进程
 
```shell
screen -S XXX -X quit
```

# 四、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

1. 服务器配置文件：`"~/Steam/steamapps/common/7 Days to Die Dedicated Server/serverconfig.xml"`
2. 管理员配置文件：`~/.local/share/7DaysToDie/Saves/serveradmin.xml` 

### ②、重要路径

1. 服务端主目录：`"~/Steam/steamapps/common/7 Days to Die Dedicated Server/"`
2. 服务端地图目录：`"~/Steam/steamapps/common/7 Days to Die Dedicated Server/Data/Worlds"`
3. 服务器日志输出目录：`"~/Steam/steamapps/common/7 Days to Die Dedicated Server/7DaysToDieServer_Data"`
4. Mods 目录：`"~/Steam/steamapps/common/7 Days to Die Dedicated Server/Mods"`
	1. 需要自己创建
	2. 将想要使用的 mod 上传至 Mods 目录即可，游戏会自动加载
	3. mod 目录的名字不要使用中文
5. 服务端存档目录：`~/.local/share/7DaysToDie/Saves`

## 2、服务器配置文件：`~/steam/7DaysToDieServer/serverconfig.xml` 参数说明

```xml
<?xml version="1.0"?>
<ServerSettings>
	<!-- GENERAL SERVER SETTINGS -->

	<!-- Server representation -->
	<!-- 服务器名称，请自行设置（默认是：My Game Host） -->
	<property name="ServerName"						value="月海 七日杀"/>
	<!-- 相当于服务器的简介 -->
	<property name="ServerDescription"				value="月海的服务器"/>
	<!-- 服务器的网站URL（默认无）可以把你的主页网站放到这里 -->
	<property name="ServerWebsiteURL"				value=""/>
	<!-- 进入服务器的密码（默认无） -->
	<property name="ServerPassword"					value="000123"/>
	<!-- 如果设置用户将在加入服务器的过程中看到该消息（玩家进入游戏时会看到的文字，默认没有） -->
	<property name="ServerLoginConfirmationText"	value="欢迎进入月海" />
	<!-- The region this server is in. Values: NorthAmericaEast, NorthAmericaWest, CentralAmerica, SouthAmerica, Europe, Russia, Asia, MiddleEast, Africa, Oceania -->
	<property name="Region"							value="NorthAmericaEast" />
	<!-- 游戏语言：英语：English；中文：zh-CN -->
	<property name="Language"						value="zh-CN" />

	<!-- Networking -->
	<!-- 服务器监听的端口. -->
	<property name="ServerPort"						value="26900"/>
	<!-- 服务器的可见性：2=公共，1=仅向朋友显示，0=未列出. -->
	<property name="ServerVisibility"				value="2"/>
	<!--【未知，请勿乱开】-->
	<!-- Networking protocols that should not be used. Separated by comma. Possible values: LiteNetLib, SteamNetworking. Dedicated servers should disable SteamNetworking if there is no NAT router in between your users and the server or when port-forwarding is set up correctly -->
	<property name="ServerDisabledNetworkProtocols"	value="SteamNetworking"/>
	<!-- 【上传带宽（ＫＢ/Ｓ）默认即可，读取地图或上传保存时的速度　】　Maximum (!) speed in kiB/s the world is transferred at to a client on first connect if it does not have the world yet. Maximum is about 1300 kiB/s, even if you set a higher value. -->
	<property name="ServerMaxWorldTransferSpeedKiBs" value="512"/>

	<!-- Slots -->
	<!--  最多多少人同时在线（越多越卡，根据你的服务器或PC主机来） -->
	<property name="ServerMaxPlayerCount"			value="8"/>
	<!-- 【服务器人满时，允许几个特权的人还可加入游戏】 -->
	<property name="ServerReservedSlots"			value="0"/>
	<!-- Required permission level to use reserved slots above -->
	<property name="ServerReservedSlotsPermission"	value="100"/>
	<!--【服务器人满时，允许几位管理员还可加入游戏】-->
	<property name="ServerAdminSlots"				value="0"/>
	<!-- Required permission level to use the admin slots above -->
	<property name="ServerAdminSlotsPermission"		value="0"/>

	<!-- Admin interfaces -->
	<!-- 启用/禁用Web控制面板 -->
	<property name="ControlPanelEnabled"			value="true"/>
	<!-- 控制面板网页的端口 -->
	<property name="ControlPanelPort"				value="8080"/>
	<!-- 进入控制面板的密码 -->
	<property name="ControlPanelPassword"			value="000123"/>
	
	<!-- 启用/禁用telnet -->
	<property name="TelnetEnabled"					value="true"/>
	<!-- 远程登录服务器的端口 -->
	<property name="TelnetPort"						value="8081"/>
	<!-- 进入telnet界面的密码 -->
	<property name="TelnetPassword"					value=""/>
	<!-- 在来自单个远程客户端的许多错误密码之后将被阻止连接到Telnet -->
	<property name="TelnetFailedLoginLimit"			value="10"/>
	<!-- 阻止将持续多长时间（以秒为单位 -->
	<property name="TelnetFailedLoginsBlocktime"	value="10"/>

	<!-- 显示用于日志输出/命令输入的终端窗口 -->
	<property name="TerminalWindowEnabled"			value="true"/>

	<!-- Folder and file locations -->
	<!-- 服务器配置文件名称 -->
	<property name="AdminFileName"					value="serveradmin.xml"/>
	
	<!--这里复制你保存的路径（默认保存到Ｃ盘）极大影响游戏性能！-->
	<!-- Use this to override where the server stores all generated data, including RWG generated worlds. Do not forget to uncomment the entry! -->
	<!-- <property name="UserDataFolder"				value="absolute path" /> -->
	
	<!-- 这里复制你保存的路径（默认保存到Ｃ盘）极大影响游戏性能 -->
	<!-- Use this to only override the save game path. Do not forget to uncomment the entry! -->
	<!-- <property name="SaveGameFolder"				value="absolute path" /> -->

	<!-- Other technical settings -->
	<!-- 启用或禁用ＥＡＣ反作弊　true＝启用　false＝禁用（一旦禁用玩家就可以修改文件作弊了） -->
	<property name="EACEnabled"						value="false"/>
	<!-- Hide logging of command execution. 0 = show everything, 1 = hide only from Telnet/ControlPanel, 2 = also hide from remote game clients, 3 = hide everything -->
	<property name="HideCommandExecutionLog"		value="0"/>
	<!-- Override how many chunks can be uncovered on the ingame map by each player. Resulting max map file size limit per player is (x * 512 Bytes), uncovered area is (x * 256 m²). Default 131072 means max 32 km² can be uncovered at any time -->
	<property name="MaxUncoveredMapChunksPerPlayer"	value="131072"/>
	<!-- If disabled a player can join with any selected profile. If true they will join with the last profile they joined with -->
	<property name="PersistentPlayerProfiles"		value="false" />



	<!-- 游戏设置 -->
	
	<!-- 游戏世界/地图设置 -->
	<!-- 使用的地图；改为 RWG 则会创建随机地图 -->
	<property name="GameWorld"						value="Siwoho Valley"/>
	<!-- 如果是RWG，则这是产生新世界的种子。 如果世界已经存在，其结果名称将已经存在 -->
	<property name="WorldGenSeed"					value="road"/>
	<!-- 生成的地图区块大小 -->
	<property name="WorldGenSize"					value="6144"/>
	<!-- 游戏名称 -->
	<property name="GameName"						value="My Game"/>
	<!-- 是否是单人模式: GameModeSurvival 多人 GameModeSurvivalSP 单人 -->	
	<property name="GameMode"						value="GameModeSurvival"/>

	<!-- 难度设置 -->
	<!-- 0-5，0 =最简单，5 =最困难 -->
	<property name="GameDifficulty"					value="3"/>
	<!-- -玩家对方块的伤害（整数百分比） -->
	<property name="BlockDamagePlayer"				value="200" />
	<!-- AI对积木造成的伤害（整数百分比） -->
	<property name="BlockDamageAI"					value="100" />
	<!-- 血月期间AI对块造成的损害（整数百分比） -->
	<property name="BlockDamageAIBM"				value="100" />
	<!-- XP增益乘数（整数百分比） -->
	<property name="XPMultiplier"					value="100" />
	<!-- 如果玩家小于或等于该级别，则在生成时会创建一个安全区域 -->
	<property name="PlayerSafeZoneLevel"			value="5" />
	<!-- 此安全区存在的世界时间 -->
	<property name="PlayerSafeZoneHours"			value="5" />

	<!--  -->
	<!-- 作弊模式打开/关闭 -->
	<property name="BuildCreate"					value="true" />
	<!-- 这里设置真实世界多少分钟=游戏中的24小时（默认为真实世界60分钟=游戏中24小时） -->
	<property name="DayNightLength"					value="60" />
	<!-- 在游戏时间内，白天时间为：游戏日中每天18小时的日照 -->
	<property name="DayLightLength"					value="18" />
	<!-- 玩家死亡时掉落 0 =无，1 =一切，2 =仅工具带，3 =仅背包，4 =全部删除 -->
	<property name="DropOnDeath"					value="0" />
	<!-- 玩家退出游戏时掉落 0 =无，1 =一切，2 =仅工具带，3 =仅背包 -->
	<property name="DropOnQuit"						value="0" />
	<!--在床多少范围内不产生僵尸Size-->
	<property name="BedrollDeadZoneSize"			value="30" />
	<!--离线玩家的床还可以保存多久-->
	<property name="BedrollExpiryTime"				value="45" />

	<!-- 性能设置 -->
	<!--整个地图能同时出现多少个僵尸（越多越卡）建议按玩家比例来调整，参考：１个玩家对4-8个左右差不多了-->
	<property name="MaxSpawnedZombies"				value="20" />
	<!--整个地图能同时出现多少个野生动物（越多越卡）,这个使用的性能比僵尸少，可以略多于僵尸-->
	<property name="MaxSpawnedAnimals"				value="20" />
	<!--玩家最多可以看多远（6-12）.数值越高越卡-->
	<property name="ServerMaxAllowedViewDistance"	value="10" />

	<!-- 僵尸设置 -->
	<!-- 启用/禁用敌人生成　true＝启用　false＝禁用 -->
	<property name="EnemySpawnMode"					value="true" />
	<!-- 僵尸的难度　0 =正常，1 =疯狂 -->
	<property name="EnemyDifficulty"				value="0" />
	<!-- 0-3 (Off, Day, Night, All) -->
	<property name="ZombieFeralSense"				value="0" />
	<!-- 僵尸白天速度　0-4（0＝步行，１＝慢跑，２＝奔跑，３＝冲刺，４＝噩梦） -->
	<property name="ZombieMove"						value="0" />
	<!-- 僵尸夜间速度0-4（0＝步行，１＝慢跑，２＝奔跑，３＝冲刺，４＝噩梦） -->
	<property name="ZombieMoveNight"				value="3" />
	<!-- 凶残丧尸速度0-4（0＝步行，１＝慢跑，２＝奔跑，３＝冲刺，４＝噩梦） -->
	<property name="ZombieFeralMove"				value="3" />
	<!-- 丧尸血月速度0-4（0＝步行，１＝慢跑，２＝奔跑，３＝冲刺，４＝噩梦） -->
	<property name="ZombieBMMove"					value="3" />
	<!-- 血月隔几天出现一次《七日杀》的名字由来啊！（以天为单位）,设置为“ 0”表示没有血月 -->
	<property name="BloodMoonFrequency"				value="7" />
	<!-- How many days can the actual blood moon day randomly deviate from the above setting. Setting this to 0 makes blood moons happen exactly each Nth day as specified in BloodMoonFrequency -->
	<property name="BloodMoonRange"					value="0" />
	<!--几点开始提示当日是血月（-1为不提示）-->
	<property name="BloodMoonWarning"				value="8" />
	<!--血月时，同时产生多少个僵尸，可能会受其他玩家影响-->
	<property name="BloodMoonEnemyCount"			value="24" />

	<!-- 战利品 -->
	<!-- 战利品掉落率：整数百分比 -->
	<property name="LootAbundance"					value="100" />
	<!-- 地块或者区域或者房间、物品多久刷新一次：整数天 -->
	<property name="LootRespawnDays"				value="7" />
	<!-- 空投在游戏时间发生的频率（应该为小时单位） -->
	<property name="AirDropFrequency"				value="72"/>
	<!-- 是否在标记空投位置（地图或指南针显示）true＝是，false＝不标记 -->
	<property name="AirDropMarker"					value="true"/>

	<!--多人游戏设置 -->
	<!-- 你需要在队友多少范围内拿到队友的共享经验值（比如说击杀僵尸、建基地、挖矿、交任务等） -->
	<property name="PartySharedKillRange"			value="100"/>
	<!-- 玩家杀戮设置（0 =无法杀死玩家，1 =仅杀死盟友，2 =仅杀死陌生人，3 =杀死所有人）玩家对战还是纯粹合作模式看你的选择了 -->
	<property name="PlayerKillingMode"				value="0" />

	<!-- 多人游戏－土地认证设置 -->
	<!-- 每个玩家可拥有几个领地. -->
	<property name="LandClaimCount"					value="1"/>
	<!-- 玩家领地范围 -->
	<property name="LandClaimSize"					value="41"/>
	<!-- 领地旁非好友能创建建筑范围 -->
	<property name="LandClaimDeadZone"				value="30"/>
	<!--领地有效天数-->
	<property name="LandClaimExpiryTime"			value="7"/>
	
	<!-- 领地范围衰减天数 0 =慢速 1 =快速 2 =全面保护，直到过期 -->
	<property name="LandClaimDecayMode"				value="0"/>		
	<!-- 玩家在线时，领地区域硬度增加倍数。 0表示无限（永远不会受到伤害）。 默认值为4x -->
	<property name="LandClaimOnlineDurabilityModifier"	value="4"/>
	<!-- 玩家离线时，领地区域硬度增加倍数。 0表示无限（永远不会受到伤害）。 默认值为4x -->
	<property name="LandClaimOfflineDurabilityModifier"	value="4"/>
	<!-- 玩家离线后领地保护改变时间(分钟) 默认为0-->
	<property name="LandClaimOfflineDelay"			value="0"/>

	
	<property name="DynamicMeshEnabled"				value="true"/>				<!-- Is Dynamic Mesh system enabled -->
	<property name="DynamicMeshLandClaimOnly"		value="true"/>				<!-- Is Dynamic Mesh system only active in player LCB areas -->
	<property name="DynamicMeshLandClaimBuffer"		value="3"/>					<!-- Dynamic Mesh LCB chunk radius -->
	<property name="DynamicMeshMaxItemCache"		value="3"/>					<!-- How many items can be processed concurrently, higher values use more RAM -->

	<property name="TwitchServerPermission"			value="90"/>				<!-- Required permission level to use twitch integration on the server -->
	<property name="TwitchBloodMoonAllowed"			value="false"/>				<!-- If the server allows twitch actions during a blood moon. This could cause server lag with extra zombies being spawned during blood moon. -->

	<!-- 有几种游戏设置在开始新游戏时无法更改。There are several game settings that you cannot change when starting a new game.
	您可以使用控制台命令来更改其中至少一些命令。You can use console commands to change at least some of them ingame.
	setgamepref BedrollDeadZoneSize 30 -->
</ServerSettings>
```

# 五、管理服务器

1. 在服务器中安装 telnet。（也可以用 Xshell 的远程 telnet 连接，这里不做赘述）

```bash
# RedHat/CentOS
rpm -qa telnet	# 检测 telnet 的 rpm 包是否安装 
yum install telnet	# 若未安装，则安装 telnet

# Ubuntu/Debian
netstat -a | grep telnet	# 检测 telnet 的 rpm 包是否安装 
sudo apt-get install xinetd telnetd	# 若未安装，则安装 telnet
```

2. 登录服务器 telnet

```bash
telnet localhost 8081
```

3. 管理员指令

| 指令                        | 描述                                                                |
| ------------------------- | ----------------------------------------------------------------- |
| admin add <玩家名> <权限级别>    | 给予玩家管理权限（最高级别为0）                                                  |
| admin remove <玩家名>        | 移除玩家的管理权限                                                         |
| admin update <玩家名> <权限等级> | 提高管理权限级别<br>建议先在 telnet 用上述指令给自己管理权限<br>然后就可以直接在游戏中，按 F1 使用下面的指令了 |
| dm                        | 打开或关闭debug模式                                                      |
| ban <玩家名> <时间>            | 禁止玩家登陆服务器一段时间(minutes, hours, days, weeks, months, years)         |
| kill <id/name>            | 杀死指定玩家                                                            |
| listplayers lp            | 获取在线玩家信息                                                          |
| give <id/name> <物品> <数量>  | 给玩家刷某样东西                                                          |
| shutdown                  | 关闭服务器                                                             |
| say <信息>                  | 以server的名义广播一条信息                                                  |

