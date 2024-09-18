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
	4. 端口范围：若是选择了全部则不需输入；若是选择的自定义 TCP，则添加两个，<font color="#ff0000">分别输入饥荒的端口号</font> `10998`、`10999`
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
sudo ufw allow from any to any port 10998 proto tcp

sudo ufw allow from any to any port 10999 proto tcp
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

# 五、创建用户，下载游戏服务器

1. 创建用户 steam，设置密码

```shell
adduser steam
```
   
2. 登录普通用户 steam，创建 `steamcmd` 文件夹，再进入 `steamcmd` 目录

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
	1. 若是想自定义下载目录，需在登陆前设置：`force_install_dir /home/steam/game/dstserver`

```shell
login anonymous
```

7. 下载饥荒联机版，更新游戏时同样使用此命令
 
```shell
app_update 343050 validate
```

8. 等待下载完后输入 quit 或者 （ctrl + c） 退出 SteamCMD，至此服务器已经下载好了，接下来就是配置服务器

# 六、启动服务器

1. ~~首先解决最重要的问题，linux 下饥荒的服务器似乎需要的组件跟现在的组件产生了名字上的差错，导致启动服务器会显示缺少关键的组件libcurl-gnutls.so.4，因此需要执行下面的命令来解决~~；
	1. 现在支持 64 位了，不用下载这个了
  
```shell
ln -s /usr/lib/libcurl.so.4 /home/steam/dstserver/bin/lib32/libcurl-gnutls.so.4
```

2. 进入饥荒联机版 bin64 目录；为什么会有这么奇怪的目录名称啊

```shell
cd "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/"
```

3. 启动地表层（主世界）服务器；因为服务器虽然启动但还未配置所以显示未正常启动，之后等待一两分钟后按下 `Ctrl + C` 关闭服务器
   
```shell
./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Master
```

4. 启动洞穴层服务器；因为服务器虽然启动但还未配置所以显示未正常启动，之后等待一两分钟后按下 `Ctrl + C` 关闭服务器
 
```shell
./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Caves
```

5. 经过上述服务器初次启动，在 ```/home/steam/.klei/DoNotStarveTogether/Cluster_1/``` 文件夹下就会自动生成默认的配置文件，这个配置文件就是我们饥荒服务器的配置文件了
6. 接下来有两种方式：
	1. 一种是自己修改配置，这种要求比较高
	2. 另一种就是现在自己电脑上创建一个服务器，然后将配置文件复制到 Linux 服务器上
	3. 推荐使用第二种，简单，准确，这里也只描述第二种

# 七、导入配置、地图、mod 等文件

## 1、导入配置、地图

1. 使用 windows 电脑的饥荒联机版，创建一个新的服务器，并设置好房间名、密码、游戏模式、地上与洞穴的配置、服务器 mod 等
2. 然后点击创建，等房间创建好到选人界面，就可以退出了
3. 打开文件资源管理器，进入：文档 -> Klei -> DoNotStarveTogetger -> （一串数字） -> Cluster_1（后面的数字表示是第几个服务器）
4. 进入 Cluster_1，所有文件复制到服务器的 `/home/steam/.klei/DoNotStarveTogether/Cluster_1/` 目录中

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230502172147.png)

## 2、服务器 token

- 在服务器的 `/home/steam/.klei/DoNotStarveTogether/Cluster_1/` 目录中新建一个文件：`cluster_token.txt`，然后在 windows 电脑的饥荒联机版主界面中：
1. 点击左下角的账号按钮
2. 点击弹窗上方的游戏按钮
3. 点击《饥荒：联机版》的游戏服务器按钮
4. 点击添加新服务器按钮
5. 复制出现的令牌码 ```pds-g^KU_......```，粘贴入 `cluster_token.txt` 文件中

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230502173321.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230502173401.png)

## 3、设置管理员

- 在服务器的 `/home/steam/.klei/DoNotStarveTogether/Cluster_1/` 目录中新建一个文件：`adminlist.txt`，然后在 windows 电脑的饥荒联机版主界面中：
1. 点击左下角的账号
2. 复制 KLEI 用户 ID 到此文件中，可添加多个管理员，每个一行

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230502173424.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2F%E6%B8%B8%E6%88%8F%2Fattachments%2FPasted%20image%2020230502173345.png)

## 4、mod

1. windows 电脑进入 Master 或者 Caves 文件夹，打开 `modoverrides.lua` 文件
2. linux 服务器进入 `cd "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/mods"` 文件夹，打开 `dedicated_server_mods_setup.lua` 文件
3. 将 windows 电脑 `modoverrides.lua` 文件中方括号内 ```workshop-``` 后的数字填入linux 服务器的 `dedicated_server_mods_setup.lua` 文件中，格式为：

```shell
ServerModSetup("序号1")
ServerModSetup("序号2")

ServerModCollectionSetup("序号1")
ServerModCollectionSetup("序号2")
```

4. 再次启动服务器就会自动下载 mod

# 八、使用 screen 后台运行服务器

### ①、启动服务器

1. 进入服务器脚本目录

```shell
cd "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/"
```

2. 启动地表层服务器；按 `Ctrl + a + d` 可退出终端

```shell
screen -S dstserver_master

./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Master
```

3. 启动洞穴层服务器；按 `Ctrl + a + d` 可退出终端
 
```shell
screen -S dstserver_caves

./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Caves
```

4. 获取 screen 列表，会有一个 `XXX.dstserver_master` 和 `XXX.dstserver_caves` 的进程
 
```shell
screen -ls
```

5. 输入进程名字即可进入终端

```shell
# 进入 地表层服务器
screen -r dstserver_master

# 进入 洞穴层服务器
screen -r dstserver_caves
```

6. 结束进程
 
```shell
# 关闭地表层服务器
screen -S dstserver_master -X quit

# 关闭洞穴层服务器
screen -S dstserver_caves -X quit
```

### ②、自动关服脚本

1. 进入游戏服务器目录：
   
```shell
cd "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/"
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch dstserver_server_close.sh

# 创建日志文件：
touch dstserver_server.log
```

3. 编写自动关服脚本代码：`nano dstserver_server_close.sh`

```shell
#!/bin/bash

# 主世界 screen 会话名称，每个会话中可能有多个窗口
screen_name_master="dstserver_master"
# 洞穴 screen 会话名称，每个会话中可能有多个窗口
screen_name_caves="dstserver_caves"
# 脚本所在路径
path="/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64"

# 定义发送命令并可选地休眠的函数
# $1 是要发送的命令
# $2 是可选的休眠时间
# $3 是可选的 screen 会话名称
send_command() {

    # 判断是否提供了 screen 会话名称
    if [ ! -z "$3" ]; then
        screen_name=$3
    else
        screen_name=$screen_name_master
    fi
    
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

# 主世界启动：发送指令，保存并关闭服务器，并模拟按下回车键；等待 30 秒
send_command "c_shutdown(true)\r" 30
# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 20

# 向日志文件中追加内容
echo "$(date)：饥荒 主世界 服务器已关闭" >> "$path/dstserver_server.log"

# 洞穴启动：发送指令，保存并关闭服务器，并模拟按下回车键；等待 30 秒
send_command "c_shutdown(true)\r" 30 $screen_name_caves
# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20 $screen_name_caves
send_command $'\x03' 20 $screen_name_caves

# 向日志文件中追加内容
echo "$(date)：饥荒 洞穴 服务器已关闭" >> "$path/dstserver_server.log"
echo "" >> "$path/dstserver_server.log"
```

4. 设置脚本权限：

```shell
chmod 755 dstserver_server_close.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 饥荒 服务器关闭，每天 20 点
0 20 * * * "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/dstserver_server_close.sh"
```

8. 在 cron 表达式中，参数用于指定定时任务的执行时间。一个标准的 cron 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
9. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置

### ③、自动开服脚本

1. 进入游戏服务器目录：
   
```shell
cd "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/"
```

2. 在其中创建文件：

```shell
# 创建脚本文件：
touch dstserver_server_start.sh

# 创建日志文件：
touch dstserver_server.log
```

3. 编写自动开服脚本代码：`nano dstserver_server_start.sh`

```shell
#!/bin/bash

# 主世界 screen 会话名称，每个会话中可能有多个窗口
screen_name_master="dstserver_master"
# 洞穴 screen 会话名称，每个会话中可能有多个窗口
screen_name_caves="dstserver_caves"
# 脚本所在路径
path="/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64"

# 定义发送命令并可选地休眠的函数
# $1 是要发送的命令
# $2 是可选的休眠时间
# $3 是可选的 screen 会话名称
send_command() {

    # 判断是否提供了 screen 会话名称
    if [ ! -z "$3" ]; then
        screen_name=$3
    else
        screen_name=$screen_name_master
    fi
    
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

# 主世界启动：发送指令，保存并关闭服务器，并模拟按下回车键；等待 30 秒
send_command "c_shutdown(true)\r" 30
# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20
send_command $'\x03' 5
# 进入游戏服务器目录
send_command "cd \"$path\"\r" 5
# 发送启动命令，并模拟按下回车键；等待 20 秒，确保 PalServer 启动完成
send_command "./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Master\r" 20

# 向日志文件中追加内容
echo "$(date)：饥荒 主世界 服务器已启动" >> "$path/dstserver_server.log"

# 洞穴启动：发送指令，保存并关闭服务器，并模拟按下回车键；等待 30 秒
send_command "c_shutdown(true)\r" 30 $screen_name_caves
# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒；执行两次
send_command $'\x03' 20 $screen_name_caves
send_command $'\x03' 5 $screen_name_caves
# 进入游戏服务器目录
send_command "cd \"$path\"\r" 5 $screen_name_caves
# 发送启动命令，并模拟按下回车键；等待 20 秒，确保 PalServer 启动完成
send_command "./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Caves\r" 20 $screen_name_caves

# 向日志文件中追加内容
echo "$(date)：饥荒 洞穴 服务器已启动" >> "$path/dstserver_server.log"
```

4. 设置脚本权限：

```shell
chmod 755 dstserver_server_start.sh
```

5. 设置定时执行：
6. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
7. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 饥荒服务器开启，每天 17 点
0 17 * * * "/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/dstserver_server_start.sh"
```

# 十、文件和参数说明

## 1、重要路径和文件

### ①、重要文件

1. 服务器主配置文件 `/home/steam/.klei/DoNotStarveTogether/Cluster_1/cluster.ini`
2. 服务器 token 配置文件：`/home/steam/.klei/DoNotStarveTogether/Cluster_1/cluster_token.txt`
3. 管理员配置文件：`/home/steam/.klei/DoNotStarveTogether/Cluster_1/adminlist.txt`
4. mod 配置文件：`/home/steam/Steam/steamapps/common/Don't Starve Together Dedicated Server/mods/dedicated_server_mods_setup.lua`

### ②、重要路径

1. 地图存档和配置主目录：`/home/steam/.klei/DoNotStarveTogether/Cluster_1/`
2. 地表存档和配置目录：`/home/steam/.klei/DoNotStarveTogether/Cluster_1/Master/`
3. 洞穴存档和配置目录：`/home/steam/.klei/DoNotStarveTogether/Cluster_1/Caves`

## 2、服务器主配置文件 `cluster.ini` 参数说明

```shell
  [GAMEPLAY]
  game_mode = endless                 # 游戏模式：无尽
  max_players = 6                     # 最大游戏人数：6
  pvp = false                         # 是否开启pvp
  pause_when_empty = true             # 没人时服务器是否暂停
  vote_kick_enabled = false           # 投票踢人

  [NETWORK]
  lan_only_cluster = false            # 是否是局域网游戏
  cluster_intention = cooperative     # 游戏偏好，随便设置
  cluster_password = 000123           # 游戏密码，不设置表示无密码
  cluster_description = 月海的服务器   # 游戏房间描述
  cluster_name = 月海                 # 游戏房间名称
  offline_cluster = false             # 是否是离线服务器
  cluster_language = zh               # 游戏语言

  [MISC]
  max_snapshots = 6                   # 最大快照数，决定了可回滚的天数
  console_enabled = true              # 是否开启控制台

  [SHARD]
  shard_enabled = true                # 服务器共享，要开启洞穴服务器的必须启用
  bind_ip = 127.0.0.1                 # 服务器监听的地址
  master_ip = 127.0.0.1               # master 服务器的 IP
  master_port = 10888                 # 监听 master 服务器的 UDP 端口，所有连接至 master 服务器的非 master 服务器必须相同
  cluster_key = defaultPass           # 连接密码，每台服务器必须相同，会被 server.ini 覆盖

  [STEAM]
  steam_group_only = false            # 只允许某 Steam 组的成员加入
  steam_group_id = 0                  # 指定某个 Steam 组，填写组 ID
  steam_group_admins = false          # 开启后，Steam 组的管理员拥有服务器的管理权限

```

# 十一、问题、报错

## 1、`Shard server mode disabled: missing is_master setting`

1. 洞穴服务器无法启动，报错

```shell
[00:00:10]: [Shard] Shard server mode disabled: missing is_master setting.
[00:00:10]: [Shard] Missing 'is_master' config field.
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-2287303119
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-374550642
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-2119742489
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-2505341606
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-2283028733
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-378160973
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-569043634
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-1878212389
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-1207269058
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-1185229307
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-623749604
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-362175979
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-856487758
[00:00:10]: Could not load mod_config_data/modconfiguration_workshop-375859599
Unknown bind__() error -1.
Unknown bind__() error -1.
[00:00:11]: [Error] Server failed to start!
[00:00:11]: Unhandled exception during server startup: RakNet UDP startup failed: SOCKET_PORT_ALREADY_IN_USE (5)
[00:00:11]: PushNetworkDisconnectEvent With Reason: "ID_DST_INITIALIZATION_FAILED", reset: false
[00:00:11]: Details: SOCKET_PORT_ALREADY_IN_USE
      
```

2. 原因：应该是没有说明是否是主服务器
3. 解决：在 `Cluster_1/Caves/` 目录下的 `server.ini` 文件中添加配置：`is_master = false`

```shell
[ACCOUNT]
server_port = 11000
is_master = false
encode_user_path = true
```

## 2、
## 3、

## 4、