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
    dd if=/dev/zero of=/root/swapfile bs=1M count=2048
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
5. 进入普通用户yan，并进入根目录
    ```
    su yan
    ```
    ```
    cd ~
    ```
6. 在根目录下创建opt与GAME文件夹，在GAME下创建Terraria文件夹，在Terraria下创建tModLoader
    ```Apache
    mkdir -p opt GAME/Terraria/tModLoader
    ```
7. 进入opt文件夹
    ```Apache
    cd opt
    ```
8. 下载tModLoader
    ```
    wget https://github.com/tModLoader/tModLoader/releases/download/v0.11.8.3/tModLoader.Linux.v0.11.8.3.zip
    ```
    - Github地址：https://github.com/tModLoader/tModLoader/releases
9. 将下载好的压缩包解压到tModLoader文件夹
    ```Apache
    unzip tModLoader.Linux.v0.11.8.3.zip -d ../GAME/Terraria/tModLoader/tModLoader.Linux.v0.11.8.3.zip
    ```

# 六、启动服务器，创建MOD及地图目录
1. 将相关文件（tModLoaderServer、tModLoaderServer.bin.x86_64等）设置为可执行
    ```
    chmod u+x /home/yan/GAME/Terraria/tModLoader/tModLoader.Linux.v0.11.8.3.zip/tModLoaderServer*
    ```
2. 执行服务器启动脚本。
    ```
    /home/yan/GAME/Terraria/tModLoader/tModLoader.Linux.v0.11.8.3.zip/tModLoaderServer
    ```
3. MOD及地图目录已自动创建，关闭服务器，按Ctrl+z

# 七、上传mod或地图
1. 游戏MOD文件相关目录，将.tmod和.1.locpack文件复制到此处即可
    ```
    /home/yan/.local/share/Terraria/ModLoader/Mods
    ```
2. 游戏MOD文件相关目录：
    ```
    /home/yan/.local/share/Terraria/ModLoader/Worlds
    ```

# 八、使用screen后台运行泰拉瑞亚服务器
1. 输入命令创建终端，ttr为终端名称，可任意更改，输入完毕后会进入一个新的页面
    ```Apache
    screen -S ttr
    ```
2. 启动游戏
    ```
    cd ~
    ```
    ```
    /home/yan/GAME/Terraria/tModLoader/tModLoader.Linux.v0.11.8.3.zip/tModLoaderServer
    ```
3. 输入m管理MOD，n为创建新世界，d+世界ID为删除世界，b为MOD浏览器，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    n       New World
    d <number>Delete World
    m               Mods Menu
    b               Mod Browser

    Choose World: 
    ```
4. 输入ID开启MOD，数字ID后为MOD名称，MOD后（disabled）为未启用，（enabled）为已启用，
   e为全部启用，d为全部禁用，r为重新加载并返回世界菜单，
   <font color="#dd0000">启用并重新加载后MOD才被启用</font>
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    1               Localizer (disabled)
    e               Enable All
    d               Disable All
    r               Reload and return to world menu
    Type a number to switch between enabled/disabled

    Type a command: 
    ```
5. 输入 n 创建新地图，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    n       New World
    d <number>Delete World
    m               Mods Menu
    b               Mod Browser

    Choose World: 
    ```
6. 选择地图大小，大地图耗费的服务器资源也就更多，请根据自己服务器配置来选择，回车确认,1、2、3依次增大
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    1       Small
    2       Medium
    3       Large

    Choose size: 
    ```
7. 选择难度，1：经典，2：专家，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    1       Normal
    2       Expert

    Choose difficulty: 
    ```
8. 给世界取名，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Enter world name: 

    ```
9. <font color="#dd0000">等待</font>
10. 输入我们刚创建的新世界前面的序号，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    1               1
    n       New World
    d <number>Delete World
    m               Mods Menu
    b               Mod Browser

    Choose World: 
    ```
11. 选择最大人数，默认8，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Max players (press enter for 8): 
    ```
12. 服务器端口号，默认7777，与前面设置的要相同，最好不要改，回车确认
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Server port (press enter for 7777): 
    ```
13. 是否自动转发端口，默认是，输入y，也可直接回车
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Automatically forward port? (y/n): 
    ```
14. 设置服务器密码，也可不设置直接回车
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Server password (press enter for none): 
    ```
15. <font color="#dd0000">等待</font>
16. 如果出现出现这些表示服务器启动成功
    ```
    Terraria Server v1.3.5.3 - tModLoader v0.11.8.3

    Listening on port 7777
    Type 'help' for a list of commands.

    : 
    ```
17. 按Ctrl+a+d可退出终端

# 九、泰拉瑞亚服务器查看关闭等
1. 获取screen列表，会有一个<font color="#dd0000">XXX.ttr</font>的进程
    ```Apache
    screen -ls
    ```
2. 输入进程名字即可进入终端
    ```Apache
    screen -r XXX.ttr
    ```
3. 结束进程
    ```Apache
    screen -S XXX.ttr -X quit
    ```
    
# 泰拉瑞亚服务器配置至此结束






































