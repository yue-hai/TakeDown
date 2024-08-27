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

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093536.png)

2. 点击实例 ID 后，会进入实例详情，点击重置密码

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093423.png)

3. 输入想要设置的密码，点击确定

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093648.png)

## 2、在云服务器网站中进行防火墙设置

1. 在实例详情中，点击安全组。然后点击管理规则

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124093923.png)

2. 进入后点击手动添加，下方会出现设置
	1. 授权策略：`允许`
	2. 优先级：`1`；1 为最高优先级
	3. 协议类型：`自定义 TCP`，或者全部；若是选择了全部则代表开放了所有的端口，那么下面的端口范围无法选择
	4. 端口范围：若是选择了全部则不需输入；若是选择的自定义 TCP，<font color="#ff0000">则输入游戏的端口号</font> `7777`
	5. 授权对象：`0.0.0.0/0`
	6. 描述：随意
	7. 操作：上面的都设置好后，点击保存

![|600](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094029.png)

5. 在云服务器网站中进行防火墙设置完成

## 3、在命令行中进行防火墙设置

1. 在概览中点击远程连接

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092751.png)

2. 在弹出来的窗口中点击通过 Workbench 远程连接

![|675](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124092854.png)

3. 可以选择密码认证，然后输入刚才设置的密码；也可以选择进士 SSH 密钥认证；点击确定进行连接

![|700](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020240124094251.png)

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

4. 下载 dotnet 6.0.0，1.4 的联机依赖 dotnet
	1. 建议 Windows 下载后上传到 linux，因为 linux 下载太慢了：https://dotnet.microsoft.com/en-us/download/dotnet/6.0
	2. 愿意等待的话，启动 tModLoader 服务器时会自动下载

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230517084849.png)

5. dotnet 6.0.418 压缩包下载：[dotnet-sdk-6.0.418-linux-x64.tar.gz](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2Fdotnet-sdk-6.0.418-linux-x64.tar.gz)

# 五、创建用户，下载游戏服务器

1. 创建用户 steam，根据提示设置密码：

```shell
adduser steam
```

2. 登录普通用户 steam，根据提示输入密码，然后进入用户根目录

```shell
su steam & cd ~
```

3. 在根目录下创建 `game/tModLoader` 目录，仅是为了方便管理

```shell
mkdir -p game/tModLoader
```

4. 进入 `game/tModLoader` 文件夹

```shell
cd game/tModLoader
```

5. 下载 tModLoader，Github 地址：https://github.com/tModLoader/tModLoader/releases

```shell
wget https://github.com/tModLoader/tModLoader/releases/download/v2023.12.2.5/tModLoader.zip
```

6. 也可以本地下载后上传到 linux：
	1. <font color="#ff0000">若是版本更新了，请注意并修改版本号</font>
	2. tModLoaderv2023.12.2.5 版本下载：[tModLoader-v2023.12.2.5.zip](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FtModLoader-v2023.12.2.5.zip)
7. 创建与 tModLoader 版本对应的目录，仅是为了方便管理

```shell
mkdir -p v2023.12.2.5
```

8. 将下载好的压缩包解压到 `v2023.12.2.5` 目录

```shell
unzip tModLoader.zip -d /home/steam/game/tModLoader/v2023.12.2.5
```

9. 创建 dotnet 目录并进入，然后将之前下载的 dotnet 6.0.0 上传到此目录；若是愿意等待的话，启动 tModLoader 服务器时会自动下载，8、9 步不用执行

```shell
mkdir -p /home/steam/game/tModLoader/v2023.12.2.5/dotnet/6.0.0/
```

```shell
cd /home/steam/game/tModLoader/v2023.12.2.5/dotnet/6.0.0/
```

10. 解压 dotnet

```shell
tar -zxvf dotnet-sdk-6.0.418-linux-x64.tar.gz
```

# 六、启动游戏服务器，创建 MOD 及地图目录

1. 进入 `v2023.12.2.5` 目录

```shell
cd /home/steam/game/tModLoader/v2023.12.2.5
```

2. 将启动脚本设置为可执行

```shell
chmod 755 start-tModLoaderServer.sh
```

2. 执行服务器启动脚本；若有提示输入 `n` ：不使用 steam 服务

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

4. MOD 及地图目录已自动创建，关闭服务器，按 `Ctrl + z`

# 七、使用 screen 后台运行服务器

1. 输入命令创建终端，ttr为终端名称，可任意更改，输入完毕后会进入一个新的页面

```shell
screen -S ttr
```

2. 启动服务器；若有提示输入 `n` ：不使用 steam 服务

```shell
/home/steam/game/tModLoader/v2023.12.2.5/start-tModLoaderServer.sh
```

3. 输入 `m` 管理 MOD，`n` 为创建新世界，`d + 世界ID` 为删除世界，回车确认

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

13. 服务器端口号，默认7777，与前面开放端口设置的要相同，最好不要改，回车确认

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

# 八、服务器查看关闭等

1. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.ttr</font> 的进程

```shell
screen -ls
```

2. 输入进程名字即可进入终端

```shell
screen -r XXX.ttr
```

3. 结束进程

```shell
screen -S XXX.ttr -X quit
```

# 九、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

### ②、重要路径

1. MOD 目录：`~/.local/share/Terraria/tModLoader/Mods/`，将 mod 文件上传到此目录即可
2. 地图目录：`~/.local/share/Terraria/tModLoader/Worlds/`，将地图文件上传到此目录即可，上传的地图文件需授予读写权限：

```shell
chmod 755 /home/steam/.local/share/Terraria/tModLoader/Worlds/*
```

## 2、参数说明