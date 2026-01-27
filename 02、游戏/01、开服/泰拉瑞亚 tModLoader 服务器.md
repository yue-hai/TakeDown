# 一、游戏服务器信息

1. 端口号：`7777`
2. 不需要通过 SteamCmd 进行下载
3. 首先进行：[服务器设置](游戏服务器购买和设置.md)

# 二、下载游戏服务器

1. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

2. 在根目录下创建 `game/tModLoader` 目录，仅是为了方便管理

```shell
mkdir -p game/tModLoader
```

3. 进入 `game/tModLoader` 文件夹

```shell
cd game/tModLoader
```

4. 下载 v2023.12.2.5 版本的 tModLoader，Github 地址：https://github.com/tModLoader/tModLoader/releases

```shell
wget https://github.com/tModLoader/tModLoader/releases/download/v2023.12.2.5/tModLoader.zip
```

5. 也可以本地下载后上传到 linux：
	1. <font color="#ff0000">若是版本更新了，请注意并修改版本号</font>
	2. tModLoader v2023.12.2.5 版本下载：[tModLoader-v2023.12.2.5.zip](attachments/tModLoader-v2023.12.2.5.zip)
6. 创建与 tModLoader 版本对应的目录，仅是为了方便管理

```shell
mkdir -p v2023.12.2.5
```

7. 将下载好的压缩包解压到 `v2023.12.2.5` 目录

```shell
unzip tModLoader.zip -d /home/steam/game/tModLoader/v2023.12.2.5
```

# 三、启动游戏服务器，创建 MOD 及地图目录

1. 进入 `v2023.12.2.5` 目录

```shell
cd /home/steam/game/tModLoader/v2023.12.2.5
```

2. 将启动脚本设置为可执行

```shell
chmod 755 start-tModLoaderServer.sh
```

2. 执行服务器启动脚本；若有提示输入 `n` ：即不使用 steam 服务

```shell
./start-tModLoaderServer.sh
```

3. 显示如下内容则代表启动成功：

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

n               New World
d <number>      Delete World
m               Mods Menu

Choose World: 
```

4. MOD 及地图目录已自动创建，关闭服务器：按 `Ctrl + z`

# 四、使用 screen 后台运行服务器

1. 输入命令创建终端，tmodloader 为终端名称，可任意更改，输入完毕后会进入一个新的页面

```shell
screen -S tmodloader
```

2. 启动服务器；若有提示输入 `n` ：不使用 steam 服务

```shell
/home/steam/game/tModLoader/v2023.12.2.5/start-tModLoaderServer.sh
```

3. `n` 为创建新世界，`d + 世界ID` 为删除世界， `m` 为管理 MOD，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

n               New World
d <number>      Delete World
m               Mods Menu

Choose World: 
```

4. 输入 `m` 进入管理 MOD 页面：
	1. 最前方数字为 mod ID ，输入 mod ID 并按下回车启用该 mod
	2. 数字 ID 后为 mod 名称，可能与 mod 文件的命名不同，请注意区分
	3. mod 名称后（disabled）为未启用，（enabled）为已启用
	4. 输入 e 并按下回车为全部启用
	5. 输入 d 并按下回车为全部禁用
	6. 输入 r 并按下回车为重新加载并返回世界菜单，<font color="#dd0000">启用并重新加载后 MOD 才被启用</font>
	7. mod 目录看第六节文件和参数说明，将 mod 上传到目录 `~/.local/share/Terraria/tModLoader/Mods/ 中即可

```shell
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

1               Localizer (disabled)
e               Enable All
d               Disable All
r               Reload and return to world menu
Type a number to switch between enabled/disabled

Type a command: 
```

5. 输入 `n` 创建新地图，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

n               New World
d <number>      Delete World
m               Mods Menu

Choose World: 
```

6. 选择地图大小，大地图耗费的服务器资源也就更多，请根据自己服务器配置来选择，回车确认
	1. 1：小型
	2. 2：中型
	3. 3：大型

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

1       Small
2       Medium
3       Large

Choose size: 
```

7. 选择难度，回车确认
	1. 1：经典
	2. 2：专家
	3. 3：大师
	4. 4：旅途

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

1       I'm Too Young to Mine
2       Bone Me Plenty
3       I Am Cthulhu Incarnate
4       Journey

Choose difficulty: 
```

8. 选择腐化形式，回车确认
	1. 1：随机
	2. 2：腐化
	3. 3：猩红

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

1       Random
2       Corrupt
3       Crimson

Choose world evil: 
```

9. 给世界取名，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Enter world name: 
```

10. 输入种子，一般不输入；继续回车则开始创建世界，创建成功后会返回主页

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Enter Seed (Leave Blank For Random):
```

11. 世界创建成功后，输入我们刚创建的新世界前面的序号，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

1               LvRen
n               New World
d <number>      Delete World
m               Mods Menu

Choose World: 
```

12. 选择最大人数，默认 16，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Max players (press enter for 16): 
```

13. 服务器端口号，默认7777，与前面开放端口设置的要相同，不要修改，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Server port (press enter for 7777): 
```

14. 是否自动转发端口，默认是，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Automatically forward port? (y/n): 
```

15. 设置服务器密码，输入密码后，回车确认

```shell
Terraria Server v1.4.4.9 - tModLoader v2023.12.2.5 Preview 0c8af328, built 2024/1/8 06:27

Server password (press enter for none): 
```

16. 如果出现出现这些表示服务器启动成功

```shell
Running one update...
Terraria Server v1.4.4.9

Listening on port 7777
Type 'help' for a list of commands.

```

17. 按 `Ctrl + a + d` 可退出终端

# 五、服务器查看关闭等

1. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.tmodloader</font> 的进程

```shell
screen -ls
```

2. 输入进程名字即可进入终端

```shell
screen -r XXX.tmodloader
```

3. 结束进程

```shell
screen -S XXX.tmodloader -X quit
```

# 六、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

### ②、重要路径

1. MOD 目录：`~/.local/share/Terraria/tModLoader/Mods/`，将 mod 文件上传到此目录即可
2. 地图目录：`~/.local/share/Terraria/tModLoader/Worlds/`，将地图文件上传到此目录即可，上传的地图文件需授予读写权限：

```shell
chmod 755 /home/steam/.local/share/Terraria/tModLoader/Worlds/*
```
