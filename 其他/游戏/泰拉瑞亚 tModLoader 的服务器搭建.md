# 一、购买服务器

1. 推荐阿里云学生机，网址：https://developer.aliyun.com/plan/grow-up
2. 选择轻量型服务器，1 核 2G 就可以，2 核 2G 更好
    - 地域：随意
    - 镜像类型：系统镜像
    - 系统镜像：CentOS 7.3（或 CentOS 的其他版本）
3. 付款

# 二、设置服务器

1. 防火墙设置：
    - 点击<font color="#dd0000">服务器列表</font>，然后点击服务器进入设置
      - 点击<font color="#dd0000">3服务器安全设置</font>
        - 点击点击<font color="#dd0000">已设置2条</font>
          - 点击点击<font color="#dd0000">添加规则</font>
            - 端口范围设置为点击<font color="#dd0000">7777</font>，点击确定
2. 打开服务器终端

# 三、设置 SWAP 分区

- 由于 ECS 云服务器镜像安装好像是没有给系统分配软件交换分区 Swap 的，所以这里我们需要手动分配一下，以免我们的游戏在挂机在服务器途中突然关闭。
- 这里提一下 vi 编辑器的基本用法：进入文本后按键盘上的 `i` 键开始编辑，按 `esc` 退出编辑，上下左右移动光标，输入 `:wq` 保存并退出。

1. 查看 SWAP 设置了多少（有的话就不用进行下面的操作了，直接看第四节）

```bash
free –m
```
    
2. 删除原来的 Swap 分区

```bash
swapoff –a
```
    
3. 新增 SWAP 分区（一般是物理内存的 2 倍）

```bash
dd if=/dev/zero of=/root/swapfile bs=1M count=8192
```

4. 格式化交换分区文件

```bash
mkswap /root/swapfile
```

5. 启用 swap 分区文件

```bash
swapon /root/swapfile
```

6. 添加开机启动，打开 fstab

```bash
vi /etc/fstab
```

7. 在众多的文本最后添加一行

```bash
/root/swapfile swap swap defaults 0 0
```

8. 退出编辑，按一下 <font color="#dd0000">Esc</font>，然后退出

```bash
:wq
```

9. 重启下是否生效

```bash
reboot
```

10. 重启后输入指令查看下SWAP是否增加
    
```bash
free -m
```

# 四、下载软件

1. 安装下载工具

```bash
yum install -y wget
```

2. 安装解压工具；安装 zip 的过程中会出现 `IS this ok` 询问的一句话，这里输入一个 `y` 代表同意并继续即可。

```bash
yum install unzip
```

3. 安装远程管理工具screen 

```bash
yum install -y screen
```

4. ~~安装 mono：mono 的蓝奏云链接：https://wwa.lanzous.com/iNJuto3bbla~~，1.4 的联机不再依赖 mono，而是要使用 dotnet

```bash
yum install mono-complete
```

5. 下载 dotnet 6.0.0：https://dotnet.microsoft.com/en-us/download/dotnet/6.0；建议 Windows 下载后上传到 linux，因为 linux 下载太慢了

![](attachments/Pasted%20image%2020230517084849.png)

# 五、创建用户，授予权限，下载服务器，上传 dotnet

1. 创建用户 tmodloader，根据提示设置密码：

```bash
adduser tmodloader
```

2. 登录普通用户 tmodloader，根据输入密码，然后进入根目录

```
su tmodloader
```

```bash
cd ~
```

3. 在根目录下创建 download 目录

```bash
mkdir -p download
```

4. 进入 download 文件夹

```bash
cd download
```

5. 下载 tModLoader；也可以本地下载后上传到 linux：Github 地址：https://github.com/tModLoader/tModLoader/releases

```bash
wget https://github.com/tModLoader/tModLoader/releases/download/v2022.09.47.49/tModLoader.zip
```

6. 创建与 tModLoader 版本对应的目录，仅是为了方便

```bash
mkdir -p /home/tmodloader/v2022.09.47.49
```

6. 将下载好的压缩包解压到 v2022.09.47.49 目录

```bash
unzip tModLoader.zip -d /home/tmodloader/v2022.09.47.49
```

7. 创建 dotnet 目录并进入，然后将之前下载的 dotnet 6.0.0 上传到此目录

```bash
mkdir -p /home/tmodloader/v2022.09.47.49/dotnet/6.0.0/
```

```bash
cd /home/tmodloader/v2022.09.47.49/dotnet/6.0.0/
```

8. 解压 dotnet

```bash
tar -zxvf dotnet-sdk-6.0.408-linux-x64.tar.gz
```

# 六、启动服务器，创建 MOD 及地图目录

1. 进入 v2022.09.47.49 目录

```bash
cd /home/tmodloader/v2022.09.47.49
```

2. 将相关文件设置为可执行

```bash
chmod u+x start-tModLoaderServer.sh
```

2. 执行服务器启动脚本；若有提示输入 `y` ：不使用 steam 服务

```bash
./start-tModLoaderServer.sh
```

3. MOD 及地图目录已自动创建，关闭服务器，按 `Ctrl+z`

# 七、上传 mod 或地图

1. 游戏 MOD 文件相关目录，将 .tmod 文件上传到此处即可：

```bash
/home/tmodloader/.local/share/Terraria/tModLoader/Mods/
```

2. 游戏地图文件相关目录：

```bash
/home/tmodloader/.local/share/Terraria/tModLoader/Worlds/
```

3. 上传的地图文件需授予读写权限

```bash
chmod 755 /home/tmodloader/.local/share/Terraria/tModLoader/Worlds/*
```

# 八、使用 screen 后台运行泰拉瑞亚服务器

1. 输入命令创建终端，ttr为终端名称，可任意更改，输入完毕后会进入一个新的页面

```bash
screen -S ttr
```

2. 启动服务器；若有提示输入 `y` ：不使用 steam 服务

```bash
/home/tmodloader/v2022.09.47.49/start-tModLoaderServer.sh
```

3. 输入 `m` 管理 MOD，`n` 为创建新世界，`d + 世界ID` 为删除世界，b 为 MOD 浏览器，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

n       New World
d <number>Delete World
m               Mods Menu
b               Mod Browser

Choose World: 
```

4. 输入 ID 开启 MOD，数字 ID 后为 MOD 名称，MOD后（disabled）为未启用，（enabled）为已启用，
   e 为全部启用，d 为全部禁用，r 为重新加载并返回世界菜单，<font color="#dd0000">启用并重新加载后 MOD 才被启用</font>

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

1               Localizer (disabled)
e               Enable All
d               Disable All
r               Reload and return to world menu
Type a number to switch between enabled/disabled

Type a command: 
```

5. 输入 `n` 创建新地图，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

n       New World
d <number>Delete World
m               Mods Menu
b               Mod Browser

Choose World: 
```

6. 选择地图大小，大地图耗费的服务器资源也就更多，请根据自己服务器配置来选择，回车确认，1、2、3 依次增大

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

1       Small
2       Medium
3       Large

Choose size: 
```

7. 选择难度，1：经典，2：专家，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

1       Normal
2       Expert

Choose difficulty: 
```

8. 给世界取名，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Enter world name: 

```

9. <font color="#dd0000">等待</font>
10. 输入我们刚创建的新世界前面的序号，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

1               1
n       New World
d <number>Delete World
m               Mods Menu
b               Mod Browser

Choose World: 
```

11. 选择最大人数，默认 8，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Max players (press enter for 8): 
```

12. 服务器端口号，默认7777，与前面设置的要相同，最好不要改，回车确认

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Server port (press enter for 7777): 
```

13. 是否自动转发端口，默认是，输入y，也可直接回车

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Automatically forward port? (y/n): 
```

14. 设置服务器密码，也可不设置直接回车

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Server password (press enter for none): 
```

15. <font color="#dd0000">等待</font>
16. 如果出现出现这些表示服务器启动成功

```bash
Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

Listening on port 7777
Type 'help' for a list of commands.

: 
```

17. 按 `Ctrl+a+d` 可退出终端

# 九、泰拉瑞亚服务器查看关闭等

1. 获取 screen 列表，会有一个 <font color="#dd0000">XXX.ttr</font> 的进程

```bash
screen -ls
```

2. 输入进程名字即可进入终端

```bash
screen -r XXX.ttr
```

3. 结束进程

```bash
screen -S XXX.ttr -X quit
```







































