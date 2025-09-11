# 一、系统安装

1. 桌面版镜像下载：https://cn.ubuntu.com/download/desktop
2. 可使用 rufus 创建启动盘：https://rufus.ie/zh/
3. 在 bios 中选择从启动盘打开，但是有的 bios 需要关闭安全启动；一般是 boot 选项下的 `Secure Boot` 选项，修改为 `Disabled` 禁用
4. 在 bios 选择从启动盘打开后，选择第一项：`Try or Install Ubuntu`，然后按回车

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225150729.png)

5. 在下一个屏幕中，单击 `Install Ubuntu`

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225150824.png)

6. 选择喜欢的键盘布局，然后单击下一步

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225150914.png)

7. 在这一步中，我们必须选择安装类型。有两个选项，普通安装和最小安装，然后单击下一步
	1. 在普通安装中，将安装所有 GUI 相关的应用程序，
	2. 在最小安装中只会安装基本的应用程序。

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225151000.png)

8. 在这一步中，将提示我们选择安装类型。这里的安装类型指的是分区方案。以下是两种安装类型
	1. `Erase Disk and Install Ubuntu`：它将删除整个磁盘，并将自动创建分区。
	2. `Something else`：创建自定义分区方案。如果是 Ubuntu Linux 的新手，那么建议选择第一个选项

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225151211.png)

9. 根据当前的地区选择位置，它将相应地配置时区。

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225151259.png)

10. 创建用户并设置主机名；在此步骤中，指定本地用户名及其密码，指定系统的主机名。我们会在安装系统后使用该用户。

![|655](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225151331.png)

11. 接下来根据提示重启即登录即可

# 二、用户和密码

## 1、新安装的系统修改 root 密码

1. ubuntu 默认的 root 用户是没有固定密码的，它的密码是随机产生并且动态改变的，即每次开机都有一个新的 root 密码，如果想查看 root 密码，那么直接设置的 root 密码即可。
2. 使用安装时候的用户登录进入终端，在终端输入命令：`sudo passwd root`
3.  会显示以下内容，根据内容输入

```shell
[sudo] password for kerwin: # 输入当前用户密码
New password: # 输入root 新密码
Retype new password: # 再次输入 root 密码
passwd: password updated successfully # 密码更新成功
```

4. root 密码设置完成了，输入：`su root`
5. 切换到 root 用户，能切换到证明修改成功

## 2、Ubuntu 下创建新用户

### ①、`adduer`

- 对应着删除用户的命令：`deluser`

1. 会自动为创建的用户指定主目录、系统 shell 版本，会在创建时输入用户密码，使用：

```shell
sudo adduser 新用户名
```

2. 默认情况下：
   1. `adduser` 在创建用户时会主动调用 `/etc/adduser.conf`
   2. 在创建用户主目录时默认在 `/home` 下，而且创建为 `/home/用户名`
   3. 如果主目录已经存在，就不再创建，但是此主目录虽然作为新用户的主目录，而且默认登录时会进入这个目录下，但是这个目录并不是属于新用户，当使用 `userdel` 删除新用户时，并不会删除这个主目录，因为这个主目录在创建前已经存在且并不属于这个用户。
   4. 为用户指定 shell 版本为：`/bin/bash`
4. 常用参数选项为：
   1. `–home`： 指定创建主目录的路径，默认是在 /home 目录下创建用户名同名的目录，这里可以指定；如果主目录同名目录存在，则不再创建，仅在登录时进入主目录。
   2. `–quiet`： 即只打印警告和错误信息，忽略其他信息。
   3. `–debug`： 定位错误信息。
   4. `–conf`： 在创建用户时使用指定的configuration文件。
   5. `–force-badname`： 默认在创建用户时会进行/etc/adduser.conf中的正则表达式检查用户名是否合法，如果想使用弱检查，则使用这个选项，如果不想检查，可以将/etc/adduser.conf中相关选项屏蔽。如：

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020230725150747.png)

### ②、`useradd`

- 对应着删除用户的命令：`userdel`

1. 需要使用参数选项指定基本设置，如果不使用任何参数，则创建的用户无密码、无主目录、没有指定 shell 版本，使用：

```shell
sudo useradd 新用户名
```

2. 为用户指定登录密码：

```shell
sudo passwd 上面新建的用户名
```

4. 为用户指定命令解释程序(通常为/bin/bash)：

```shell
sudo usermod -s /bin/bash 上面新建的用户名
```

5. 为用户指定用户主目录：

```shell
sudo usermod -d /home/tt 上面新建的用户名
```

6. 常用为用户指定参数的 useradd 命令：
   1. `-d`： 指定用户的主目录
   2. `-m`： 如果存在不再创建，但是此目录并不属于新创建用户；如果主目录不存在，则强制创建； -m和-d一块使用。
   3. `-s`： 指定用户登录时的shell版本
   4. `-M`： 不创建主目录

## 3、给予普通用户 `sudo` 权限

- 使用 root 用户或者拥有 `sudo` 权限的用户执行下面的命令

```shell
sudo usermod -aG sudo 普通用户的用户名
```

## 4、修改用户密码

### ①、修改当前用户的密码

1. 打开终端，然后输入以下命令：

```shell
passwd
```

2. 系统会提示输入当前的密码（如果有的话），然后输入新密码并进行确认。

### ②、修改其他用户的密码

1. 如果是管理员或有 sudo 权限，可以为其他用户设置密码。打开终端，然后使用以下命令：

```shell
sudo passwd 用户名
```

2. 将“用户名”替换为想要修改密码的用户名。系统将提示输入新的密码。

### ③、在无法登录的情况下重置密码（恢复模式）

1. 如果无法登录，可以通过 Ubuntu 的恢复模式重置密码：
2. 重新启动的电脑。
3. 在启动时，按住 Shift 键（在一些系统上可能是 Esc 或其他键），以便进入 GRUB 菜单。
4. 选择 “高级选项” 并进入“恢复模式”。
5. 选择 “root” 以进入根终端。
6. 如果文件系统是只读的，运行 `mount -o remount,rw /` 来使其可写。
7. 使用 passwd 用户名 命令来设置新密码。
8. 重启系统。

## 5、更改文件所有者

1. 查看文件列表，发现此时 `privkey1.pem` 的所有者是 root

```shell
yan@yuehai:~/apply/yuehai-tool/https_certificate$ ll
total 24
drwxr-xr-x 2 yan  yan  4096 Aug 30 13:41 ./
drwxr-xr-x 4 yan  yan  4096 Aug 30 13:40 ../
-rw-r--r-- 1 yan  yan  1773 Aug 30 13:39 cert1.pem
-rw-r--r-- 1 yan  yan  1801 Aug 30 13:39 chain1.pem
-rw-r--r-- 1 yan  yan  3574 Aug 30 13:39 fullchain1.pem
-rw------- 1 root root 1704 Aug 30 13:41 privkey1.pem
yan@yuehai:~/apply/yuehai-tool/https_certificate$
```

2. 使用 `chown` 命令更改文件所有者为 yan

```shell
sudo chown yan:yan privkey1.pem
```

3. 再次查看文件列表，发现文件只有执行权限

```shell
yan@yuehai:~/apply/yuehai-tool/https_certificate$ ll
total 28
drwxr-xr-x 2 yan yan 4096 Aug 30 13:46 ./
drwxr-xr-x 4 yan yan 4096 Aug 30 13:40 ../
-rw-r--r-- 1 yan yan 1773 Aug 30 13:39 cert1.pem
-rw-r--r-- 1 yan yan 1801 Aug 30 13:39 chain1.pem
-rw-r--r-- 1 yan yan  124 Aug 30 13:43 config.json
-rw-r--r-- 1 yan yan 3574 Aug 30 13:39 fullchain1.pem
-rw------- 1 yan yan 1704 Aug 30 13:41 privkey1.pem
yan@yuehai:~/apply/yuehai-tool/https_certificate$ 
```

4. 修改权限为 `644`：

```shell
chmod 644 privkey1.pem
```

5. 再次查看文件列表

```shell
yan@yuehai:~/apply/yuehai-tool/https_certificate$ ll
total 28
drwxr-xr-x 2 yan yan 4096 Aug 30 13:46 ./
drwxr-xr-x 4 yan yan 4096 Aug 30 13:40 ../
-rw-r--r-- 1 yan yan 1773 Aug 30 13:39 cert1.pem
-rw-r--r-- 1 yan yan 1801 Aug 30 13:39 chain1.pem
-rw-r--r-- 1 yan yan  124 Aug 30 13:43 config.json
-rw-r--r-- 1 yan yan 3574 Aug 30 13:39 fullchain1.pem
-rw-r--r-- 1 yan yan 1704 Aug 30 13:41 privkey1.pem
yan@yuehai:~/apply/yuehai-tool/https_certificate$ 
```

## 6、使普通用户执行 sudo 命令不用输入密码

1. 使用 root 用户打开 sudoers 文件进行编辑：

```shell
sudo visudo
```

2. 在 sudoers 文件中添加如下行：
	1. `yan`：指定的用户名，表示该规则仅适用于用户 `yan`。只有 `yan` 用户在使用 `sudo` 时，该规则才会被考虑
	2. `ALL=(ALL)`：
		1. 第一个 ALL 指定该规则适用于所有的主机。这在使用网络或多机环境中配置 `sudo` 时特别有用，可以限定规则只在特定的主机上有效。在大多数单机配置中，这里通常使用 ALL
		2. `(ALL)` 指定用户 `yan` 可以以任何用户和用户组的身份执行该命令。这包括超级用户权限，意味着 `yan` 可以以系统上任何用户的权限执行此命令
	3. `NOPASSWD:`：这是一个标记，指示在执行后面指定的命令时，不需要 `yan` 用户输入密码。通常，`sudo` 需要用户输入自己的密码来验证，这个标记取消了该需求
	4. `/home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh`：这是具体的命令路径，指定了 `yan` 用户可以通过 `sudo` 执行哪个命令。这里是一个脚本的完整路径，表明只有这个脚本可以无密码执行
	5. `*`：这是一个通配符，代表 `yan` 可以在命令 `/home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh` 后带上任何参数来执行它，而不仅限于某些特定的参数。这提供了很高的灵活性，但也需要脚本本身有良好的安全检查，以防止潜在的安全风险

```shell
yan ALL=(ALL) NOPASSWD: /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh *
```

3. 修改完毕后保存退出即可
4. 这种配置方式适用于那些需要频繁自动执行某些管理任务而不希望每次都输入密码的场景。但使用时要注意，允许无密码执行特定命令会增加安全风险，因此需要确保该命令的执行不会对系统安全构成威胁

## 7、


# 三、用户登录

## 1、启用 SSH

1. 更新软件源

```shell
sudo apt update
```

2. 安装 `openssh-server` 软件包：

```shell
sudo apt install openssh-server
```

3. 当被提示时，输入密码并且按 Enter，继续安装。
4. 一旦安装完成之后，SSH 服务将会被自动启动。可以验证 SSH 是否正在运行，输入：

```shell
sudo systemctl status ssh
```

5. 如果输出内容和下文一样，则表示服务正在运行，并且启用开机启动。

```shell
yan@yan:~/桌面/clash$ sudo systemctl status ssh
[sudo] yan 的密码： 
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: e>
     Active: active (running) since Mon 2023-12-25 20:23:59 CST; 13h ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 724 (sshd)
      Tasks: 1 (limit: 35682)
     Memory: 3.4M
        CPU: 198ms
     CGroup: /system.slice/ssh.service
             └─724 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

12月 25 20:23:59 yan sshd[724]: Server listening on :: port 22.
12月 25 20:23:59 yan systemd[1]: Started OpenBSD Secure Shell server.
12月 25 20:27:58 yan sshd[2644]: Accepted password for yan from 192.168.31.1 po>
12月 25 20:27:58 yan sshd[2644]: pam_unix(sshd:session): session opened for use>
12月 25 20:32:55 yan sshd[3831]: Accepted password for yan from 192.168.31.1 po>
12月 25 20:32:55 yan sshd[3831]: pam_unix(sshd:session): session opened for use>
12月 25 20:34:43 yan sshd[3881]: Accepted password for yan from 192.168.31.1 po>
12月 25 20:34:43 yan sshd[3881]: pam_unix(sshd:session): session opened for use>
12月 26 01:43:59 yan sshd[6097]: Connection closed by 207.90.244.6 port 58230 [>
12月 26 01:44:01 yan sshd[6099]: Connection closed by 207.90.244.6 port 58238 [>
lines 1-22/22 (END)
```

## 2、开启 ssh 可以使用 root 用户登录

1. 已经安装了 `openssh-server` 软件包，启用了 SSH
2. 修改配置文件 `/etc/ssh/sshd_config`：

```shell
# 编辑或创建文件
sudo nano /etc/ssh/sshd_config

# 将：
# PermitRootLogin prohibit-password

# 改成
PermitRootLogin yes
```

3. 重启服务：`sudo systemctl restart ssh`

## 3、开启桌面可以使用 root 用户登录

1. 在设置完 root 用户的密码之后
2. 注释这两个文件的对应代码 `/etc/pam.d/gdm-autologin`、`/etc/pam.d/gdm-password`：

```shell
# 需要注释掉的代码
auth required pam_succeed_if.so user != root quiet_success

# 编辑或创建文件
# 此文件负责配置 GDM 无密码自动登录的认证过程。
# 它定义了在用户尝试通过 GDM 自动登录（无需输入密码）时所应用的 PAM 认证规则和模块。
# 配置可能包括一系列的 PAM 模块，用于检查用户的登录权限、记录登录尝试、设置用户环境等。
# 修改此文件可以改变自动登录的行为，比如添加额外的安全检查或者限制哪些用户可以自动登录。
sudo nano /etc/pam.d/gdm-autologin

# 编辑或创建文件
# 与 /etc/pam.d/gdm-autologin 相对，这个文件配置的是通过 GDM 使用密码登录时的认证过程。
# 它指定了用户在 GDM 登录界面输入密码尝试登录时所需遵循的 PAM 规则和使用的模块。
# 这些规则和模块可能涉及密码验证、账户和密码的有效期检查、用户登录限制等。
# 修改此文件可以用于增强登录过程的安全性，例如通过增加双因素认证、限制登录尝试次数等方式。
sudo nano /etc/pam.d/gdm-password
```

3. 修改 `/root/.profile` 文件：``

```shell
# 该配置文件专门用于 root 用户的 shell 环境设置。
# 当 root 用户登录到系统或启动一个新的 shell 会话时，这个文件被自动读取和执行。
sudo nano /root/.profile

# 注释掉或者删除行
mesg n 2＞ /dev/null || true

# 插入新行
tty -s && mesg n || true
```

4. 测试：注销当前用户后在登录界面选择“未列出”，然后输入用户名和密码登录，如下图所示：

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231226102848.png)

## 4、通过 Windows 远程桌面连接 Ubuntu 桌面

### ①、Ubuntu 中安装 xrdp

1. 更新软件源

```shell
sudo apt update
```

2. 在 Ubuntu 系统中安装远程桌面协议(Remote Desktop Protocol，RDP) 服务器程序 xrdp：

```shell
sudo apt install xrdp
```

3. 安装完成后启动 xrdp 程序：

```shell
sudo systemctl enable --now xrdp
```

4. 再执行下面的命令打开防火墙端口 3389

```shell
sudo ufw allow from any to any port 3389 proto tcp
```

5. 以上就是 Ubuntu 系统中的所有操作。

### ②、Windows 系统远程桌面连接

1. 在 Windows 系统中，首先点击搜索框，然后输入关键字 `remote`，再在搜索结果中点击“远程桌面连接”应用。

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225153003.png)

2. 在弹出的远程桌面连接的窗口中，先输入 Ubuntu 服务器的 IP 地址，然后点击“连接”按钮去连接服务器

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225153047.png)

3. 在随后弹出的登录界面中，需要先填入 Ubuntu 服务器的用户名和密码，然后再点击“OK”按钮

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225153111.png)

4. 没有问题的话，这样就可以登录进去了

## 5、通过 Windows 远程桌面连接 Ubuntu 桌面问题记录

### ①、Windows 远程连接后没有声音

> 1. pulseaudio-module-xrdp：xrdp 音频重定向模块，https://github.com/neutrinolabs/pulseaudio-module-xrdp/wiki/README
> 	1. v0.7 下载：[pulseaudio-module-xrdp-0.7.zip](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/pulseaudio-module-xrdp-0.7.zip)
> 2. pulseaudio-module-xrdp 依赖 pulseaudio：https://www.freedesktop.org/wiki/Software/PulseAudio/Download/
> 	1. 17.0 下载：[pulseaudio-17.0.tar.gz](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/pulseaudio-17.0.tar.gz)
> 3. 上面两个安装过程中会出现很多依赖的问题，善用 gpt 排查

#### Ⅰ、pulseaudio 编译安装

1. 查看原有的 `pulseaudio` 版本：

```shell
pulseaudio --version
```

2. 若是有输出则表示已经有安装，则执行下面的卸载；若是找不到命令，则表示没有安装，直接往下执行安装的步骤即可

```shell
sudo apt-get remove pulseaudio

sudo apt-get autoremove  # 移除未使用的依赖
```

3. 下载上面的 `pulseaudio-17.0.tar.gz` ，并解压到目录：`/home/yan/apply/tools/pulseaudio/`；或者使用 git：

```shell
# 进入 pulseaudio 应该存放的目录
cd /home/yan/apply/tools/

# git 协议
git clone git://anongit.freedesktop.org/pulseaudio/pulseaudio
# 如果在连接时遇到问题（由于防火墙等原因），请尝试使用较慢的 HTTP 协议
git clone http://anongit.freedesktop.org/git/pulseaudio/pulseaudio.git
```

4. 安装 PulseAudio 编译的依赖项；可能不完整，需根据提示安装缺失的包：

```shell
sudo apt-get update
sudo apt-get install -y build-essential libtool autoconf automake pkg-config libasound2-dev libpulse-dev libaudio-dev libjack-jackd2-dev libsndfile1-dev libudev-dev libavahi-client-dev libjson-c-dev libspeex-dev libspeexdsp-dev libglib2.0-dev libwebrtc-audio-processing-dev libsoxr-dev meson

# 安装 Linux capabilities 依赖，否则会有警告
sudo apt-get install libcap-dev
```

5. 安装 Meson 项目构建系统

```shell
sudo apt-get update

sudo apt-get install meson
```

6. 配置构建系统，创建一个构建目录（Meson 建议构建在源代码之外的目录进行），然后在该目录内配置构建环境：

```shell
# 进入 pulseaudio 所在目录
cd /home/yan/apply/tools/pulseaudio/
# 创建 build 目录
mkdir build && cd build

# 配置构建环境
meson setup ..
```

7. 编译 PulseAudio；执行该命令时可能会因为缺少依赖报错，善用 gpt 排查

```shell
meson compile
```

8. 安装 PulseAudio

```shell
sudo meson install
```

9. 查看的 `pulseaudio` 版本：

```shell
steam@yan:~$ pulseaudio --version
W: [pulseaudio] caps.c: Normally all extra capabilities would be dropped now, but that's impossible because PulseAudio was built without capabilities support.
pulseaudio 17.0-6-g84f5
steam@yan:~$ 
```

10. 有输出即为安装成功，本次的版本为：`17.0-6-g84f5`；关于警告的解释：
	1. W: 【pulseaudio】 caps.c: Normally all extra capabilities would be dropped now, but that's impossible because PulseAudio was built without capabilities support.
	2. 这条警告信息意味着 PulseAudio 想要放弃某些 Linux capabilities 来提高系统的安全性，但由于在编译 PulseAudio 时没有启用相应的支持，所以无法执行这个操作。在 Linux 中，capabilities 允许给予进程一些超出标准用户权限的特殊能力，而不是给予它们完全的 root 权限，这有助于降低系统的安全风险。
	3. 之后会解决这个问题，也可以放着不管
	4. 出现警告是因为没有 `libcap-dev` 依赖，现在上面已经加上这个依赖了，所以应该不会有这个警告了
11. 若是找不到命令，则可能是系统变量未更新的原因
12. 确认 PulseAudio 的安装位置：PulseAudio 应该安装在 `/usr/local/bin`，可以通过执行以下命令来确认这一点。如果该命令返回了 PulseAudio 的执行文件路径，则说明 PulseAudio 已经正确安装在该位置

```shell
ls /usr/local/bin/pulseaudio
```

13. 更新 PATH 环境变量，编辑用户环境变量配置文件；此操作只是给当前用户增加环境变量：

```shell
# 编辑用户变量配置文件
nano ~/.bashrc

# 在最底部增加以下内容：
export PATH=$PATH:/usr/local/bin
```

14. 运行指令刷新环境变量：

```shell
source ~/.bashrc
```

15. 再次查看的 `pulseaudio` 版本：

```shell
pulseaudio --version
```

#### Ⅱ、pulseaudio-module-xrdp 编译安装

1. 下载上面的 `pulseaudio-module-xrdp-0.7.zip` 并解压到目录：`/home/yan/apply/tools/pulseaudio-module-xrdp-0.7/`，
2. 安装 PulseAudio 编译的依赖项，可能不完整，需根据提示安装缺失的包：

```shell
sudo apt-get update

sudo apt-get install build-essential git automake libtool libpulse-dev
```

3. 运行 bootstrap 脚本：

```shell
./bootstrap
```

4. 配置项目，指定 `pulseaudio` 的编译目录；

```shell
# 指定 pulseaudio 的编译目录
PULSE_DIR=/home/yan/apply/tools/pulseaudio/

# 根据设定的参数，配置项目
./configure
```

5. 编译项目：

```shell
make
```

6. 安装 `pulseaudio-module-xrdp`：

```shell
sudo make install
```

7. 手动启动加载脚本：`/home/yan/apply/tools/pulseaudio-module-xrdp-0.7/instfiles/load_pa_modules.sh`
8. 安装完成后，您可以通过以下命令确认模块是否正确安装，有以下输出即为安装成功：

```shell
ls $(pkg-config --variable=modlibexecdir libpulse) | grep xrdp
module-xrdp-sink.la
module-xrdp-sink.so
module-xrdp-source.la
module-xrdp-source.so
yan@yan:~/apply/tools/pulseaudio$ 
```

#### Ⅲ、启动

1. 重新启动 PulseAudio：

```shell
# 关闭 PulseAudio
pulseaudio --kill

# 启动 PulseAudio
pulseaudio --start
```

2. 手动启动加载脚本：`/home/yan/apply/tools/pulseaudio-module-xrdp-0.7/instfiles/load_pa_modules.sh`
3. 此时在 设置 -> 声音 中，输入和输出设备应该都显示 `xrdp`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240326144331.png)

#### Ⅳ、创建桌面文件 pulseaudio-xrdp.desktop

> 1. 桌面文件 `pulseaudio-xrdp.desktop` 在 xrdp 环境中起着自动启动 PulseAudio 模块的作用。
> 2. 这个文件遵循 XDG Autostart 规范，它允许在用户登录并启动桌面环境时自动执行特定的脚本或应用程序。
> 3. 具体到 `pulseaudio-xrdp.desktop` 文件，它的目的是在 xrdp 会话开始时自动调用 `load_pa_modules.sh` 脚本，从而加载必要的 PulseAudio 模块以支持音频重定向。
> 4. 通过将此文件放置在 `/etc/xdg/autostart/` 目录下，当用户登录并启动桌面环境时，桌面环境的启动过程会自动检查该目录下的 `.desktop` 文件，并执行它们定义的命令。
> 5. 这意味着，对于支持 XDG Autostart 规范的桌面环境（大多数现代桌面环境都支持），`pulseaudio-xrdp.desktop` 会自动执行，从而无需用户手动干预就可以加载 xrdp 需要的 PulseAudio 模块。
> 6. 这个机制确保了在通过 xrdp 连接到远程桌面时，音频输入和输出可以正常工作，为用户提供流畅的音频体验。

1. 进入目录 `/etc/xdg/autostart/`

```shell
cd /etc/xdg/autostart/
```

2. 创建或打开 `pulseaudio-xrdp.desktop`

```shell
sudo nano pulseaudio-xrdp.desktop
```

3. 写入以下内容：

```shell
[Desktop Entry]
# 定义了这个文件遵循的桌面入口标准版本，确保兼容性
Version=1.0
# 指定这个桌面入口的显示名称，用户可以在菜单中看到这个名称
Name=PulseAudio xrdp modules
# 提供关于这个桌面入口的功能或用途的额外信息，帮助用户理解它的作用
Comment=Load PulseAudio Modules for xrdp
# 指定当这个桌面入口被激活时要执行的命令，这里是加载 PulseAudio 模块的脚本路径
Exec=/home/yan/apply/tools/pulseaudio-module-xrdp-0.7/instfiles/load_pa_modules.sh
# 控制是否在执行命令时打开终端窗口。这里设置为 false，意味着不打开终端窗口
Terminal=false
# 指定这个文件的类型。对于启动应用程序或脚本，这个值应该是 Application
Type=Application
# 定义这个入口所属的类别，有助于在应用菜单中适当地分类和显示。这里归类为系统工具
Categories=System;Utility;
# 提供一个通用名称，描述这个桌面入口的功能，有助于在不同语言环境下提供更清晰的说明
GenericName=PulseAudio XRDP Module Loader
```

4. 按 `ctrl + s` 保存，再按 `ctrl + x` 退出 nano 即可
5. 之后连接 `xrdp` 桌面时即会自动启动 xrdp pulseaudio 音频重定向

#### Ⅴ、解决 pulseaudio 警告

> W: 【pulseaudio】 caps.c: Normally all extra capabilities would be dropped now, but that's impossible because PulseAudio was built without capabilities support.
> 
> 关于警告的解释：这条警告信息意味着 PulseAudio 想要放弃某些 Linux capabilities 来提高系统的安全性，但由于在编译 PulseAudio 时没有启用相应的支持，所以无法执行这个操作。在 Linux 中，capabilities 允许给予进程一些超出标准用户权限的特殊能力，而不是给予它们完全的 root 权限，这有助于降低系统的安全风险。
> 所以安装 Linux capabilities 后再编译就可以了

1. 安装 libcap 开发包：

```shell
sudo apt-get install libcap-dev
```

2. 进入 PulseAudio 的源代码目录，并清理上次的构建结果（如果有的话）：

```shell
# 进入 PulseAudio 的源代码目录
cd /home/yan/apply/tools/pulseaudio/

# 或使用适当的清理命令
meson setup build --reconfigure
```

3. 进入 PulseAudio 的源代码目录中的 build 目录，删除其中的全部内容：

```shell
# 进入 PulseAudio 的源代码目录中的 build 目录
cd /home/yan/apply/tools/pulseaudio/build/

# 删除其中的全部内容；小心使用
rm -rf /home/yan/apply/tools/pulseaudio/build/
```

4. 卸载之前手动编译安装的 pulseaudio，需要在编译目录中执行该命令

```shell
sudo ninja uninstall
```

5. 配置构建系统：

```shell
meson setup ..
```

6. 编译 PulseAudio：

```shell
meson compile
```

7. 安装 PulseAudio

```shell
sudo meson install
```

8. 查看的 `pulseaudio` 版本：

```shell
yan@yan:~/apply/tools/pulseaudio/build$ pulseaudio --version
pulseaudio 17.0-6-g84f5
yan@yan:~/apply/tools/pulseaudio/build$ 
```

### ②、远程登录后弹出需要验证的窗口

1. 有时候登录后还弹出一个如下图所示的认证窗口，那么还需要再输入一次密码来认证，这样显得有点麻烦。

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225153514.png)

2. 如果不想弹出这个认证窗口，可以在 Ubuntu 中执行下面的命令：

```shell
sudo nano /etc/polkit-1/localauthority/50-local.d/45-allow-colord.pkla
```

3. 然后将下面的内容粘贴到文件里面：

```shell
[Allow Colord all Users]
Identity=unix-user:*
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile
ResultAny=no
ResultInactive=no
ResultActive=yes
```

4. 重启 Ubuntu 系统后，再远程登录就不会弹出这个窗口了

### ③、画面卡顿

#### Ⅰ、调整 Xrdp 配置参数

1. 首先查看两个值：输入以下两个命令，三个值分别是：最小值、默认值、最大值

```shell
yan@yan:~/桌面/clash$ cat /proc/sys/net/ipv4/tcp_wmem 
4096	16384	4194304
yan@yan:~/桌面/clash$ cat /proc/sys/net/ipv4/tcp_rmem 
4096	131072	6291456
yan@yan:~/桌面/clash$ 
```

2. 编辑 `/etc/xrdp/xrdp.ini` 文件：`sudo nano /etc/xrdp/xrdp.ini`
3. 其中 `tcp_send_buffer_bytes`、`tcp_recv_buffer_bytes` 两个参数默认被注释了，取消注释，根据上面查询的值来设置

```shell
tcp_send_buffer_bytes=4194304
tcp_recv_buffer_bytes=6291456
```

#### Ⅱ、调整系统参数

1. 调整系统参数，临时生效

```shell
sudo sysctl -w net.core.rmem_max=12582912
sudo sysctl -w net.core.wmem_max=8388608
```

2. 重启后保留，将以下内容写入配置文件 `/etc/sysctl.conf`
3. 编辑配置文件：`sudo nano /etc/sysctl.conf`

```shell
net.core.rmem_max = 12582912
net.core.wmem_max = 8388608
```

4. 然后执行：`sudo sysctl -p`
5. 重启 xrdp 服务使其生效：`sudo systemctl restart xrdp`

### ④、无法复制

1. 重启 xrdp 或是注销用户后重新登录可恢复功能

### ⑤、远程登录后是黑屏状态

1. 如果远程登录后并没有出现 Ubuntu 桌面而是黑屏状态，那么可能是已经有用户登录进去了
2. 需要先把之前的用户退出来（Log Out），如果更直接一点就是重启 Ubuntu 系统

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231225153222.png)

## 6、使用 `lastb` 查看登录失败尝试记录

### ①、`lastb` 的介绍

1. `lastb` 是 Linux 系统中用于查看登录失败尝试记录的命令。它从 `/var/log/btmp` 文件中读取信息，并以易读的格式显示。`lastb` 对应于 `last`，但专注于显示失败的登录尝试记录
2. `lastb` 是分析暴力破解和异常登录行为的重要工具，可用来追踪恶意登录尝试的来源。结合其他安全工具（如 `fail2ban`），能够有效提升服务器的安全性
3. 用途：显示所有用户的失败登录尝试。
4. 日志来源：`/var/log/btmp` 文件，记录所有失败的登录事件。

### ②、`lastb` 的基本用法

1. 显示失败登录记录：
	1. 用户名（`root` 或 `dell`）
	2. 登录终端（如 `ssh:notty`）
	3. 登录来源 IP（如 `81.161.238.51`）
	4. 登录时间和持续时间。

```shell
sudo lastb
```

```shell
root     ssh:notty    81.161.238.51    Wed Nov 13 20:44 - 20:44  (00:00)
dell     ssh:notty    81.161.238.51    Wed Nov 13 20:44 - 20:44  (00:00)
dell     ssh:notty    81.161.238.51    Wed Nov 13 20:44 - 20:44  (00:00)
guest    ssh:notty    81.161.238.51    Wed Nov 13 20:44 - 20:44  (00:00)
ubuntu   ssh:notty    81.161.238.51    Wed Nov 13 20:44 - 20:44  (00:00)
```

2. 限制显示条数，仅显示最近的 5 条记录：

```bash
sudo lastb -n 5
```

3. 结合 `grep` 筛选特定日期或时间的记录：

```bash
sudo lastb | grep "Nov 20"
```

4. 如果日志文件过大，可以清空：

```bash
sudo truncate -s 0 /var/log/btmp
```

### ③、相关日志文件

1. `/var/log/btmp`：存储失败登录尝试的二进制日志文件。
2. `/var/log/auth.log` 或 `/var/log/secure`：记录认证相关的所有日志（成功和失败）
3. 通过 `lastb`，管理员可以快速审查系统的登录安全状况。

## 7、使用 `fail2ban` 屏蔽 SSH 爆破

### ①、`fail2ban` 的介绍

1. `Fail2Ban` 是一个开源的入侵防护工具，主要用于保护 Linux 系统免受暴力破解和其他恶意登录行为的威胁。它通过监控日志文件（如 SSH、HTTP、FTP 等服务的日志），检测登录失败尝试，并根据预定义规则自动阻止可疑的 IP 地址
2. 主要功能：
3. **日志监控**：`Fail2Ban` 通过分析系统日志文件（如 `/var/log/auth.log` 或 `/var/log/secure`），检测失败登录尝试，并采取相应的防护措施。
4. **自动阻止 IP**：当特定 IP 地址的失败尝试次数超过配置的阈值后，Fail2Ban 会通过防火墙（如 iptables）自动封禁该 IP。
5. **自定义规则**：用户可以针对不同服务（如 SSH、Apache、Postfix 等）定义独立的规则，包括检测模式、封禁时长等。
6. **多服务保护**：支持多种协议和服务的保护，例如：
	1. SSH
	2. HTTP/HTTPS（防止恶意爬虫和攻击）
	3. FTP
	4. 邮件服务

### ②、核心配置文件

1. 主配置文件：
	1. `/etc/fail2ban/jail.conf` 或 `/etc/fail2ban/jail.local`
	2. 定义全局默认配置和各个服务的规则。
2. 日志文件：
	1. `/var/log/fail2ban.log`：记录 Fail2Ban 的运行日志。
	2. `/var/log/auth.log` 或 `/var/log/secure`：被监控的日志文件。

### ③、常用命令

1. 查看 `fail2ban` 状态：

```bash
sudo fail2ban-client status
```

2. 查看特定服务的状态：

```bash
sudo fail2ban-client status sshd
```

3. 手动封禁 IP：

```bash
sudo fail2ban-client set sshd banip <IP地址>
```

4. 手动解封 IP：

```bash
sudo fail2ban-client set sshd unbanip <IP地址>
```

5. 启用 `fail2ban` 服务开机自动启动

```shell
sudo systemctl enable fail2ban
```

6. 禁用 `fail2ban` 服务开机自动启动

```shell
sudo systemctl disable fail2ban
```

7. 启动服务：

```shell
sudo systemctl start fail2ban
```

8. 停止服务：

```shell
sudo systemctl stop fail2ban
```

9. 重启 `fail2ban` 服务：

```shell
sudo systemctl restart fail2ban
```

### ④、简单使用

1. 更新软件源

```shell
sudo apt update
```

2. 安装 `fail2ban`

```shell
sudo apt install fail2ban
```

3. 新建一个配置文件 `/etc/fail2ban/jail.local`：

```shell
sudo nano /etc/fail2ban/jail.local
```

4. 在配置文件中输入以下内容：

```shell
[DEFAULT]
# 时间以秒为单位。3600=1小时，86400=24小时（1天）          
# 30 分钟内计算失败尝试                                        
findtime    = 1800
# 封禁 12 小时
bantime     = 43200
# 允许失败尝试 5 次
maxretry    = 5
# 忽略的 ip，失败不会被封禁；本地和私网 IP
# 127.0.0.1：本地回环地址，表示本地机器自身
# 127.0.0.0/8：包含所有本地回环地址，127.x.x.x 的 IP 范围
# 192.168.0.0/16：常见的家庭或小型企业路由器使用的私有网络范围，192.168.x.x 的 IP 范围
ignoreip    = 127.0.0.1 127.0.0.0/8 192.168.0.0/16

[sshd]
# 启用对 SSH 的监控
enabled = true
```

5. 启用 `fail2ban` 服务开机自动启动

```shell
sudo systemctl enable fail2ban
```

6. 重启 `fail2ban` 服务：

```shell
sudo systemctl restart fail2ban
```

7. 查看 `fail2ban` 服务的总体状态，显示当前启用的所有监控规则（jails）的数量及列表：
	1. `Number of jail`：当前启用了 1 个监控规则（jail）。
	2. `Jail list`：列出了启用的规则名称，此处只有 `sshd`，表示它正在监控 SSH 登录。

```shell
sudo fail2ban-client status
```

```shell
yan@yan:~$ sudo fail2ban-client status
Status
|- Number of jail:      1
`- Jail list:   sshd
yan@yan:~$ 
```

8. 查看特定 `jail`（此处为 `sshd`）的详细状态，包括过滤和封禁的统计信息：
	1. Filter 部分：
		1. `Currently failed`：当前有 1 次失败的登录尝试。
		2. `Total failed`：总共记录了 2 次失败的尝试。
		3. `File list`：Fail2Ban 正在监控 `/var/log/auth.log` 文件中的登录尝试记录。
	2. Actions 部分：
		1. `Currently banned`：当前没有任何 IP 被封禁。
		2. `Total banned`：至今没有 IP 被封禁。
		3. `Banned IP list`：显示已封禁的 IP 地址列表，此处为空。

```shell
sudo fail2ban-client status sshd
```

```shell
yan@yan:~$ sudo fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed: 1
|  |- Total failed:     2
|  `- File list:        /var/log/auth.log
`- Actions
   |- Currently banned: 0
   |- Total banned:     0
   `- Banned IP list:
yan@yan:~$ 
```

## 8、


# 四、端口设置

## 1、查看已经开启的端口：

```shell
sudo ufw status numbered
```

## 2、Ubuntu 开启或关闭指定端口

### ①、开启指定端口

1. 比如要开启 3389 `tcp` 和 `udp` 端口：

```shell
sudo ufw allow from any to any port 3389
```

2. 开启 3389 tcp 端口

```shell
sudo ufw allow from any to any port 3389 proto tcp
```

3. 开启 3389 udp 端口

```shell
sudo ufw allow from any to any port 3389 proto udp
```

### ②、关闭指定端口

1. 查看当前 UFW 的规则列表：

```shell
sudo ufw status numbered
```

2. 若是提示：`状态：不活动`，表示防火墙未开启，需开启防火墙：

```shell
sudo ufw enable
```

3. 若是防火墙已开启，则找到想删除的规则编号：
	1. `3389/tcp`：表示该编号代表是 3389 `tcp` 端口
	2. `8000`：表示该编号代表是 8000 `tcp` 和 `udp` 端口
	3. `3389/tcp (v6)`：表示该编号代表是 3389 `tcp` 的 `ipv6` 端口
	4. `8000 (v6)`：表示该编号代表是 8000 `tcp` 和 `udp` 的 `ipv6` 端口

```shell
root@yan:~# sudo ufw status numbered
状态： 激活

     至                          动作          来自
     -                          --          --
[ 1] 3389/tcp                   ALLOW IN    Anywhere                  
[ 2] 8000                       ALLOW IN    Anywhere  
[ 3] 3389/tcp (v6)              ALLOW IN    Anywhere (v6)   
[ 4] 8000 (v6)                  ALLOW IN    Anywhere (v6)    

root@yan:~# 
```

4. 根据具体端口号来关闭指定端口：

```shell
# 关闭 3389 tcp 和 udp 端口：
sudo ufw delete allow from any to any port 3389

# 分别关闭 3389 TCP 和 UDP 端口：
sudo ufw delete allow from any to any port 3389 proto tcp
sudo ufw delete allow from any to any port 3389 proto udp
```

5. 根据编号来关闭指定端口：

```shell
sudo ufw delete [规则编号]
```

## 3、Ubuntu 开启所有端口

1. 允许所有传入和传出的连接：使用 iptables 命令来允许所有传入和传出的连接。执行以下命令来清除所有已有的规则，并允许所有连接：

```shell
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables-save
```

2. 允许所有传入和传出的连接（IPv6）：如果你使用的是IPv6，执行以下命令来允许所有传入和传出的IPv6连接：

```shell
sudo ip6tables -F
sudo ip6tables -P INPUT ACCEPT
sudo ip6tables -P FORWARD ACCEPT
sudo ip6tables -P OUTPUT ACCEPT
sudo iptables-save
```

2. 这样可以开放所有端口（如需开启指定端口，可以使用 `iptables -I INPUT -p tcp --dport 8080 -j ACCEPT` ），
3. 但是如果服务器重启，不会保存。为了使更改在系统重启后仍然生效，需要将它们保存到防火墙规则配置文件中。
4. 在 Ubuntu 中，iptables 的规则通常在 `/etc/iptables/rules.v4` 文件中，而 IPv6 规则在 `/etc/iptables/rules.v6` 文件中。
5. 以下是保存 `iptables` 规则的步骤：
6. 保存 IPv4 规则：

```shell
sudo sh -c 'iptables-save > /etc/iptables/rules.v4'
```

7. 保存 IPv6 规则：

```dart
sudo sh -c 'ip6tables-save > /etc/iptables/rules.v6'
```

8. 这样，在系统重启后，防火墙规则将会从这些文件加载，使更改保持生效。

## 4、使用 nc（netcat）工具测试网络连通性

> 服务端：测试的机器，本次测试就是为了测试此机器的网络连通性
> 
> 客户端：帮助测试的机器，用于测试服务端的端口是否可以联通

### ①、测试 TCP 连接

1. 在服务器端，打开一个端口监听，例如监听 9001 端口：

```shell
nc -l 9001
```

2. 在客户端，尝试连接到服务器的 9001 端口：

```shell
nc [服务器IP地址] 9001
```

3. 如果连接成功，可以在客户端输入文本，然后在服务器端看到相同的文本，这表明 TCP 连接是成功的。

### ②、测试 UDP 连接

1. 在服务器端，使用 -u 选项监听一个 UDP 端口，例如监听 9001 端口：

```shell
nc -ul 9001
```

2. 在客户端，同样使用 -u 选项尝试连接到服务器的 9001 端口：

```shell
nc -u [服务器IP地址] 9001
```

3. 客户端和服务器端可以相互发送和接收消息，验证 UDP 连接。

## 5、


# 五、系统设置

## 1、配置环境变量

### ①、单用户使用

1. 下载对应环境的二进制文件并解压到指定位置，如：`/home/yan/IDE/Java/JDK/jdk-21.0.2/`

```shell
sudo tar -xvzf openjdk-21.0.2_linux-x64_bin.tar.gz -C /home/yan/IDE/Java/JDK
```

2. 打开 `~/.bashrc` 文件进行编辑

```shell
nano ~/.bashrc
```

3. 在文件末尾，添加环境变量配置：

```shell
# 环境变量：jdk 21
export JAVA_HOME=/home/yan/IDE/Java/JDK/jdk-21.0.2
export PATH=$JAVA_HOME/bin:$PATH
```

4. 保存并关闭文件后，执行以下命令使变更生效

```shell
source ~/.bashrc
```

5. 查看配置是否生效：

```shell
java -version
```

### ②、多用户使用

1. 创建 `/usr/lib/jvm` 目录

```shell
sudo mkdir -p /usr/lib/jvm
```

2. 下载对应环境的二进制文件并解压到指定位置，如：`/usr/lib/jvm/jdk-21.0.2`

```shell
sudo tar -xvzf openjdk-21.0.2_linux-x64_bin.tar.gz -C /usr/lib/jvm
```

3. 要确保环境变量被设置在一个所有用户都能访问的地方，比如全局环境配置文件 `/etc/profile` 中：

```shell
sudo nano /etc/profile
```

4. 在文件末尾，添加环境变量配置：

```shell
# 环境变量：jdk 21
export JAVA_HOME=/usr/lib/jvm/jdk-21.0.2
export PATH=$JAVA_HOME/bin:$PATH
```

5. 保存并关闭文件后，执行以下命令使变更生效

```shell
source /etc/profile
```

6. 确保普通用户有权限访问 JDK 安装的目录，可以检查 `/usr/lib/jvm/jdk-21.0.2` 目录的权限，确保普通用户至少有读取和执行权限

```shell
sudo chmod -R +r /usr/lib/jvm/jdk-21.0.2
sudo chmod +x /usr/lib/jvm/jdk-21.0.2/bin/*
```

7. 查看配置是否生效：

```shell
java -version
```

## 2、将应用软件加入启动器和桌面快捷方式

> ubuntu下桌面配置文件 `*.desktop` 存放路径为 `/usr/share/applications` 
> 
> 该文件夹下存在的软件自然可以直接复制到桌面和加入启动器，但有些自己安装的软件（如解压缩包的软件）没有自动生成桌面配置文件，自然不能直接获得桌面快捷方式或加入启动器。

1. 命令行进入 `/usr/share/applications`：

```shell
cd /usr/share/applications
```

2. 该目录下添加桌面配置文件 `idea.desktop`

```shell
sudo nano idea.desktop
```

3. 在文件中加入以下配置内容，根据情况修改参数：

```shell
[Desktop Entry]
# 指定文件的编码格式
Encoding=UTF-8
# 应用程序的显示名称
Name=Idea
# 应用程序的描述
Comment=Idea
# 指定要执行的可执行文件的路径和名称。可以使用多种类型的命令或脚本作为 Exec 的参数，包括：
# 可执行文件的路径：可以直接指定可执行文件的完整路径，例如 /usr/bin/firefox。
# 脚本文件的路径：可以指定一个可执行的脚本文件的路径，例如 /path/to/your/script.sh。
# 命令行命令：可以指定一个命令行命令，例如 firefox 或 gnome-terminal。在这种情况下，系统会在 PATH 环境变量中查找该命令并执行它。
Exec=/home/yan/Idea/IntelliJ-ideaIU-2023.2.5/bin/idea
# 指定应用程序的图标文件的路径和名称；支持 PNG、SVG、ICO、XPM 格式
Icon=/home/yan/Idea/IntelliJ-ideaIU-2023.2.5/bin/idea.svg
# 指定是否在打开应用程序时启动终端
Terminal=false
# 指定是否在应用程序启动时显示通知
StartupNotify=true
# 指定应用程序的类型。通常为 Application，表示这是一个普通的应用程序
# Application：应用程序类型，用于表示一个可执行的应用程序。
# Link：链接类型，用于表示一个指向其他文件或网页的链接。
# Directory：目录类型，用于表示一个文件夹。
# File：文件类型，用于表示一个单独的文件。
# Service：服务类型，用于表示一个系统服务。
# MimeType：MIME 类型，用于表示一个特定的文件类型。
# Link：链接类型，用于表示一个指向其他文件或网页的链接。
# FSDevice：文件系统设备类型，用于表示一个文件系统设备。
Type=Application
# 指定应用程序所属的类别
Categories=Application;Development;
```

4. 快捷键 `ctrl + s` 保存，快捷键 `ctrl + x` 退出

## 3、启动默认开启小键盘

1. 打开终端，运行以下命令来编辑 `/etc/X11/xinit/xinitrc` 文件：

```shell
sudo nano /etc/X11/xinit/xinitrc
```

3. 在文件最后添加：

```shell
/usr/bin/numlockx on
```

4. 保存并关闭文件（使用 `Ctrl + O` 保存，`Ctrl + X` 退出）。
5. 重新启动系统。

## 4、设置系统时区

1. 查看当前时区：`timedatectl`
	1. 下面的这个输出表示系统当前设置的时区是 `Etc/UTC`。
	2. 这表示系统时区被设置为协调世界时（UTC），并且没有任何时差偏移，即 +0000。
	3. 所以，这个系统时间与世界标准时间是一致的。

```shell
yan@yuehai:~$ timedatectl
               Local time: Mon 2024-07-15 07:40:30 UTC
           Universal time: Mon 2024-07-15 07:40:30 UTC
                 RTC time: Mon 2024-07-15 07:40:31    
                Time zone: Etc/UTC (UTC, +0000)       
System clock synchronized: yes                        
              NTP service: active                     
          RTC in local TZ: no                         
yan@yuehai:~$ 
```

2. 查看可用的时区列表，特别是中国的时区：

```shell
timedatectl list-timezones | grep Asia/Shanghai
```

3. 设置时区为中国上海（UTC+8）：

```shell
sudo timedatectl set-timezone Asia/Shanghai
```

4. 验证时区设置是否成功：`timedatectl`

```shell
yan@yuehai:~/apply/n2n-edge-query-check$ timedatectl
               Local time: Tue 2024-07-16 08:35:49 CST
           Universal time: Tue 2024-07-16 00:35:49 UTC
                 RTC time: Tue 2024-07-16 00:35:50    
                Time zone: Asia/Shanghai (CST, +0800) 
System clock synchronized: yes                        
              NTP service: active                     
          RTC in local TZ: no                         
yan@yuehai:~/apply/n2n-edge-query-check$ 
```

## 5、定时任务

1. 首先编写需要定时执行的脚本 `nano /home/yan/apply/crontab_test.sh`：

```shell
#!/bin/bash

# 向 pal_server.log 文件中追加日志
echo "【$(date)】：定时任务运行日志" >> $path/pal_server.log
```

2. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
3. 在 `crontab` 文件中添加一行，指定时间和要执行的命令。比如要在每天凌晨 1 点执行命令：

```shell
0 1 * * * /home/yan/apply/crontab_test.sh
```

4. 在每月、每周、每天、每个小时、每分钟都执行一次脚本：

```shell
* * * * * /home/yan/apply/crontab_test.sh
```

5. 在 `cron` 表达式中，参数用于指定定时任务的执行时间。一个标准的 `cron` 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
6. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置
7. 若是在更改系统时区后，定时任务不在预期时间运行的原因可能与 cron 守护进程的时区设置有关。cron 通常在系统启动时加载，并使用那时的系统时区设置。如果在系统运行期间更改时区，cron 进程可能不会自动更新为新的时区设置。
8. 重新加载并使用当前的系统时区。你可以通过以下命令来重启 cron 服务：

```shell
sudo service cron restart
```

9. 或者使用：

```shell
sudo systemctl restart cron
```

## 6、

# 六、问题记录

## 1、使用 dos2unix 转换换行符格式

1. 报错信息：

```shell
-bash: ./run_jar.sh: /bin/bash^M: bad interpreter: No such file or directory
```

2. 原因：错误信息中的 `^M` 表示的是 Windows 风格的换行符（Carriage Return + Line Feed），而在 Unix/Linux 系统中使用的是 Line Feed。这种不同的换行符格式可能导致解释器无法正确识别脚本文件。
3. 解决：使用 `dos2unix` 命令将脚本文件的换行符格式转换为 Unix 格式。在终端中执行以下命令：

```shell
# run_jar.sh 替换为需要转换的文件
dos2unix run_jar.sh
```

4. 若是提示以下内容，则需要安装 dos2unix

```shell
Command 'dos2unix' not found, but can be installed with:
apt install dos2unix
Please ask your administrator.
```

5. 更新软件源

```shell
sudo apt update
```

6. 执行以下命令安装 dos2unix

```dart
apt install dos2unix
```

## 2、使用 sed 转换换行符格式

1. 上面是使用 dos2unix 转换的，也可以直接使用 `sed` 命令进行替换：

```shell
sed -i 's/\r$//' run_jar.sh
```

## 3、查看一个目录以及其中所有文件和子目录的总大小

1. 基本命令：
	1.  `-s`：表示汇总指定目录的总大小
	2. `-h`：使输出以易于阅读的格式（如 KB、MB 或 GB）显示。

```shell
du -sh /path/to/directory
```

2. 如果想看到每个子目录的大小而不仅仅是总大小，可以省略 `-s` 选项。这会列出所有子目录及其大小：

```shell
du -h /path/to/directory
```

3. 查看特定深度的目录大小：
	1. `--max-depth=1`：表示只显示直接子目录的大小。
	2. 可以将 1 替换为其他数字来指定不同的深度。

```shell
du -h --max-depth=1 /path/to/directory
```

## 4、解决 Ubuntu 不能挂载移动硬盘问题

### ①、问题

1. 挂载硬盘时无法挂载
2. 并报错：

```shell
Error mounting /dev/sda1 at /media/XXXX: Command-line `mount -t "ntfs" -o
```

### ②、解决

1. 在终端输入如下命令，查看分区挂载情况

```shell
sudo fdisk -l
```

2. 输出结果：

```shell
yan@yan:~$ sudo fdisk -l 
[sudo] yan 的密码： 
Disk /dev/loop0：4 KiB，4096 字节，8 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop1：55.66 MiB，58363904 字节，113992 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop2：55.36 MiB，58052608 字节，113384 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop3：63.95 MiB，67051520 字节，130960 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop4：63.97 MiB，67080192 字节，131016 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop5：74.27 MiB，77881344 字节，152112 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop6：74.25 MiB，77852672 字节，152056 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop7：271.38 MiB，284557312 字节，555776 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/nvme0n1：1.82 TiB，2000398934016 字节，3907029168 个扇区
Disk model: CT2000P5PSSD8                           
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：gpt
磁盘标识符：62471CC2-1DE9-4310-B954-9F0B16A9D973

设备              起点       末尾       扇区  大小 类型
/dev/nvme0n1p1    2048    1050623    1048576  512M EFI 系统
/dev/nvme0n1p2 1050624 3907028991 3905978368  1.8T Linux 文件系统


Disk /dev/loop8：271.63 MiB，284827648 字节，556304 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop9：349.7 MiB，366682112 字节，716176 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop10：504.15 MiB，528642048 字节，1032504 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop11：505.09 MiB，529625088 字节，1034424 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop12：91.69 MiB，96141312 字节，187776 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop13：12.93 MiB，13553664 字节，26472 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop14：12.2 MiB，12791808 字节，24984 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop15：38.73 MiB，40615936 字节，79328 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop16：38.83 MiB，40714240 字节，79520 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop17：564 KiB，577536 字节，1128 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop18：568 KiB，581632 字节，1136 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop19：321.08 MiB，336678912 字节，657576 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/loop20：321.1 MiB，336699392 字节，657616 个扇区
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


Disk /dev/sda：9.1 TiB，10000831348736 字节，19532873728 个扇区
Disk model: 721010ALE6L4    
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 4096 字节
I/O 大小(最小/最佳)：4096 字节 / 4096 字节
磁盘标签类型：gpt
磁盘标识符：B7260998-6105-471D-9C57-302D39909B45

设备        起点        末尾        扇区  大小 类型
/dev/sda1     34       32767       32734   16M Microsoft 保留
/dev/sda2  32768 19532869631 19532836864  9.1T Microsoft 基本数据

分区 1 未起始于物理扇区边界。


Disk /dev/sdb：3.64 TiB，4000787027968 字节，7814037164 个扇区
Disk model: External USB 3.0
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 4096 字节
I/O 大小(最小/最佳)：4096 字节 / 4096 字节
磁盘标签类型：gpt
磁盘标识符：656F765D-A491-4C1E-B03D-4ECAA0CE7EE7

设备         起点       末尾       扇区  大小 类型
/dev/sdb1      34     262177     262144  128M Microsoft 保留
/dev/sdb2  264192 7814035455 7813771264  3.6T Microsoft 基本数据

分区 1 未起始于物理扇区边界。
yan@yan:~$
```

3. 最末尾 `/dev/sdb2` 就是出问题的硬盘
4. 修复挂载错误的相应的分区，如提示中的 `/dev/sdb2`，输入：

```shell
sudo ntfsfix /dev/sdb2
```
\
5. 再次插入移动硬盘即可正常使用

## 5、定时挂载和卸载硬盘的脚本

1. 在目录 `/home/yan/apply/file/YottaMaster/` 中创建日志文件：`mount-unmount-disks.log`

```shell
touch mount-unmount-disks.log
```

2. 在目录 `/home/yan/apply/file/YottaMaster/` 中创建脚本：`mount-unmount-disks.sh`，编写以下内容

```shell
touch mount-unmount-disks.sh
```

```shell
#!/bin/bash

# 检查是否传入了参数：mount 或 unmount，否则提示用法并退出
if [ $# -ne 1 ]; then
    echo "用法: $0 <mount|unmount>"
    exit 1
fi

# 根据参数设定操作类型
operation=$1

# 硬盘设备标识列表，以空格分隔
devices=("/dev/sda2" "/dev/sdb2")
# 硬盘设备名称列表，以空格分隔；这是 Bash 4.0 新增的关联数组语法
declare -A DISK_NAME
# 为每个设备设置名称，用于日志记录
DISK_NAME["/dev/sda2"]="东芝V10-4t"
DISK_NAME["/dev/sdb2"]="hc330-10t"

# 日志文件路径
log_file="/home/yan/apply/file/YottaMaster/mount-unmount-disks.log"

# 函数：记录日志
log_action() {
    echo "【$(date "+%Y-%m-%d %H:%M:%S")】$1" >> "$log_file"
}

# 函数：检查并处理忙碌的设备
handle_busy_device() {
    local device=$1
    echo "检查设备 $device 是否忙碌..."

    # 使用 lsof 检查设备，获取占用设备的进程列表
    local busy_procs=$(lsof $device 2>/dev/null | awk '{print $2}' | tail -n +2 | uniq)

    if [ -n "$busy_procs" ]; then
        # 输出被占用信息到日志
        log_action "设备 $device 被以下进程占用：$busy_procs"

        # 这里可以选择杀掉这些进程或者给出警告让用户手动处理，例如，杀掉进程:
        for pid in $busy_procs; do
            kill -9 $pid
        done

        # 输出杀死进程信息到日志
        log_action "已尝试杀死占用 $device 的进程"
    fi
}

# 函数：挂载设备
mount_device() {
    # 参数 $1 代表设备标识
    local device=$1

    # 因为挂载命令需要输入密码，所以使用 expect 脚本自动化交互式命令
    # 1、mount_output=$(expect -c " ... ") 代表执行 expect 命令，并将输出保存到变量 mount_output
    # 2、set timeout 300 代表设置超时时间为 300 秒，超时后自动退出
    # 3、spawn /usr/bin/udisksctl mount -b $1 代表执行挂载命令，$1 代表传入的设备标识
    # 4、expect "Password:" 代表等待输出中出现 "Password:" 字符串
    # 5、send "000123\r" 代表发送密码 "000123" 并回车
    # 6、expect eof 代表等待输出结束
    local mount_output=$(expect -c "
        set timeout 300
        spawn /usr/bin/udisksctl mount -b $device
        expect \"Password:\"
        send \"000123\r\"
        expect eof
    ")

    if echo "$mount_output" | grep -q 'Mounted'; then
        log_action "挂载设备 $device at ${DISK_NAME["$device"]} 成功"
    else
        log_action "挂载设备 $device at ${DISK_NAME["$device"]} 失败：$mount_output"
    fi
}

# 函数：卸载设备
unmount_device() {
    # 参数 $1 代表设备标识
    local device=$1
    # 默认重试次数为 3 次；${2:-3} 代表如果传入了第二个参数，则使用传入的值，否则使用默认值 3
    local attempts=${2:-3}

    # 直接使用 udisksctl 命令卸载设备，不需要输入密码
    local unmount_output=$(/usr/bin/udisksctl unmount -b $device 2>&1)

    # 检查输出是否包含 'Unmounted'，判断卸载是否成功，并记录到日志文件
    if echo "$unmount_output" | grep -q 'Unmounted'; then
        log_action "卸载设备 $device from ${DISK_NAME["$device"]} 成功"
        return 0
    else
        # 卸载失败，记录到日志文件
        log_action "尝试卸载设备 $device from ${DISK_NAME["$device"]} 失败: $unmount_output"
        # 如果重试次数大于 1，则处理设备忙碌情况，等待 3 秒后递归调用自身，次数减一；否则记录最终失败信息
        if (( attempts > 1 )); then
            # 处理设备忙碌的情况
            handle_busy_device "$device"
            # 等待 3 秒
            sleep 3
            # 递归调用自身，次数减一
            unmount_device "$device" $((attempts - 1))
        else
            log_action "卸载设备 $device from ${DISK_NAME["$device"]} 最终失败"
            return 1
        fi
    fi
}

# 主循环：根据操作类型遍历设备列表，挂载或卸载
for device in "${devices[@]}"; do
    mount_info=$(mount | grep "$device")

    # 判断是否执行挂载操作
    if [ "$operation" == "mount" ]; then
        # 判断设备是否已经挂载，如果已经挂载则跳过，否则执行挂载操作
        if [ -n "$mount_info" ]; then
            log_action "设备 $device on ${DISK_NAME["$device"]} 已经挂载，跳过..."
        else
            mount_device "$device"
        fi
    # 判断是否执行卸载操作
    elif [ "$operation" == "unmount" ]; then
        # 判断设备是否已经挂载，如果已经挂载则执行卸载操作，否则跳过
        if [ -n "$mount_info" ]; then
            unmount_device "$device"
        else
            log_action "设备 $device on ${DISK_NAME["$device"]} 未挂载，跳过..."
        fi
    # 未知操作类型，提示用法并退出
    else
        echo "未知操作: $operation" >> "$log_file"
        echo "用法: $0 <mount|unmount>"
        exit 2
    fi
done

echo "挂载/卸载设备完成" >> "$log_file"
echo "----------------------------------------------------------------" >> "$log_file"
echo "" >> "$log_file"
```

3. 设置脚本权限：

```shell
chmod 755 mount-unmount-disks.sh
```

4. 设置定时执行：
5. 在终端中输入 `crontab -e`，这将打开个人 `crontab` 文件进行编辑
6. 在 `crontab` 文件中添加一行，指定时间和要执行的命令：

```shell
# 挂载硬盘：每周五 18:30
30 18 * * 5 /home/yan/apply/file/YottaMaster/mount-unmount-disks.sh mount
# 卸载硬盘：每周末 18:00
00 18 * * 7 /home/yan/apply/file/YottaMaster/mount-unmount-disks.sh unmount
```

7. 在 cron 表达式中，参数用于指定定时任务的执行时间。一个标准的 cron 表达式由五个或六个字段组成，每个字段代表不同的时间单位：
	1. 分钟（Minute）：0 ~ 59，代表一小时中的哪一分钟执行任务。
	2. 小时（Hour）：0 ~ 23，代表一天中的哪一个小时执行任务。0 代表午夜，23 代表晚上 11 点。
	3. 日（Day of the Month）：范围：1 ~ 31，代表一个月中的哪一天执行任务。
	4. 月（Month）：1 ~ 12 或使用月份名称的缩写（例如，1代表一月，2代表二月，等等），代表一年中的哪一个月份执行任务。
	5. 星期几（Day of the Week）：0 ~ 7 或使用星期名称的缩写（0和7都代表星期日，1代表星期一，等等）代表一周中的哪一天执行任务。
8. 在编辑完 `crontab` 后，保存并退出编辑器，`crontab` 会自动安装新的计划任务。可以通过 `crontab -l` 命令查看当前的 `crontab` 任务列表，以确认任务已正确设置

## 6、


# 七、软件使用

### ②、使用 V2Ray 搭建 vpn

#### Ⅰ、ubuntu 搭建 V2Ray 服务端

> 使用的野草云：https://my.yecaoyun.com/

1. 开放 `10010` 端口

![|388](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241121100626.png)

2. 通过官方脚本来安装 V2Ray，这个脚本会自动配置好 V2Ray

```shell
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh)"
```

3. 安装完成后，需要配置 V2Ray 来使用 VMess+WebSocket
	1. `port`：V2Ray 使用的端口号
	2. `protocol`：V2Ray 使用的协议
	3. `settings.clients.id`：每个客户端一个唯一的 UUID，可以通过许多在线工具生成
	4. `settings.clients.alterId`：额外的 ID，推荐设置为 64
	5. `streamSettings.network`：传输协议，此处为 `WebSocket ` 协议
	6. `streamSettings.wsSettings.path`：`WebSocket ` 的连接协议

```shell
sudo nano /usr/local/etc/v2ray/config.json
```

```shell
{
    "inbounds": [
        {
            "port": 10010,
            "protocol": "vmess",
            "settings": {
                "clients": [
                    {
                        "id": "A675E71B-87BA-CB0E-71D8-4B932F241E6F",
                        "alterId": 0
                    },
                    {
                        "id": "9053C302-6BB9-D9EC-5C0B-6D5B661618DB",
                        "alterId": 0
                    },
                    {
                        "id": "3A789917-A9B1-F9FA-2163-93439B28C607",
                        "alterId": 0
                    },
                    {
                        "id": "A68CEFB1-10F1-BFC3-97EA-A9AB068DFCF5",
                        "alterId": 0
                    },
                    {
                        "id": "FCA42E4D-A0BB-3E8A-8536-CE31ED434CBB",
                        "alterId": 0
                    },
                    {
                        "id": "1F67FB4C-BF09-8FE4-3002-96D2E4A940D7",
                        "alterId": 0
                    },
                    {
                        "id": "4369C60B-3B4C-EC85-DA88-66AE9783904D",
                        "alterId": 0
                    },
                    {
                        "id": "2851648A-9BE0-909F-E3AA-A8C7450E5F55",
                        "alterId": 0
                    },
                    {
                        "id": "2F862300-E39E-AB59-5F56-E0DA67FD75CF",
                        "alterId": 0
                    },
                    {
                        "id": "923EA6F0-150D-BD9D-6EA2-BDF7258D9D39",
                        "alterId": 0
                    }
                ]
            },
            "streamSettings": {
                "network": "ws",
                "wsSettings": {
                    "path": "/yuehai"
                }
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom",
            "settings": {}
        }
    ]
}
```

4. 配置完成后，重启 V2Ray 服务以应用新的配置：

```shell
sudo systemctl restart v2ray
```

5. 要启动 V2Ray 服务：

```shell
sudo systemctl start v2ray
```

6. 停止 V2Ray 服务：

```shell
sudo systemctl stop v2ray
```

7. 查看 V2Ray 服务状态：

```shell
sudo systemctl status v2ray
```

#### Ⅱ、使用 docker 部署 V2Ray 服务端
 
1. 在目录 `~/docker/volumes/V2Ray/config/` 中创建配置文件，并输入以下内容：
	1. `port`：V2Ray 使用的端口号
	2. `protocol`：V2Ray 使用的协议
	3. `settings.clients.id`：每个客户端一个唯一的 UUID，可以通过许多在线工具生成
	4. `settings.clients.alterId`：额外的 ID，推荐设置为 64
	5. `streamSettings.network`：传输协议，此处为 `WebSocket ` 协议
	6. `streamSettings.wsSettings.path`：`WebSocket ` 的连接协议

```shell
nano ~/docker/volumes/V2Ray/config/config.json
```

```shell
{
	"log": {
		"access": "/var/log/v2ray/access.log",
		"error": "/var/log/v2ray/error.log",
		"loglevel": "warning"
	  },
    "inbounds": [
        {
            "port": 10010,
            "protocol": "vmess",
            "settings": {
                "clients": [
                    {
                        "id": "A675E71B-87BA-CB0E-71D8-4B932F241E6F",
                        "alterId": 0
                    },
                    {
                        "id": "9053C302-6BB9-D9EC-5C0B-6D5B661618DB",
                        "alterId": 0
                    },
                    {
                        "id": "3A789917-A9B1-F9FA-2163-93439B28C607",
                        "alterId": 0
                    },
                    {
                        "id": "A68CEFB1-10F1-BFC3-97EA-A9AB068DFCF5",
                        "alterId": 0
                    },
                    {
                        "id": "FCA42E4D-A0BB-3E8A-8536-CE31ED434CBB",
                        "alterId": 0
                    },
                    {
                        "id": "1F67FB4C-BF09-8FE4-3002-96D2E4A940D7",
                        "alterId": 0
                    },
                    {
                        "id": "4369C60B-3B4C-EC85-DA88-66AE9783904D",
                        "alterId": 0
                    },
                    {
                        "id": "2851648A-9BE0-909F-E3AA-A8C7450E5F55",
                        "alterId": 0
                    },
                    {
                        "id": "2F862300-E39E-AB59-5F56-E0DA67FD75CF",
                        "alterId": 0
                    },
                    {
                        "id": "923EA6F0-150D-BD9D-6EA2-BDF7258D9D39",
                        "alterId": 0
                    }
                ]
            },
            "streamSettings": {
                "network": "ws",
                "wsSettings": {
                    "path": "/yuehai"
                }
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom",
            "settings": {}
        }
    ]
}
```

2. 在目录 `~/docker/volumes/V2Ray/log/` 中创建日志文件：

```shell
touch access.log error.log
```

3. 启动容器：
	1. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 10010:10010 \
-v ~/docker/volumes/V2Ray/config/config.json:/etc/v2ray/config.json \
-v ~/docker/volumes/V2Ray/log/:/var/log/v2ray/ \
--restart=unless-stopped \
--name v2ray-server \
teddysun/v2ray:latest
```

#### Ⅲ、使用 docker 部署 V2Ray 客户端

1. 启动容器：
	1. `-p 10010:2017`：将 Web 管理页面的默认端口 2017 映射到主机的 10010 端口
	2. `-p 10011:10808`：将默认代理端口映射到主机，供本地客户端使用。
	3. `--cap-add NET_ADMIN`：授予网络管理权限，用于调整路由规则。
	4. `--restart=unless-stopped`：指定容器的重启策略。除非显式停止，否则总是在宿主机重启或容器退出时重启容器。

```shell
docker run -d \
-p 10010:2017 \
-p 10011:10808 \
--cap-add NET_ADMIN \
--restart=unless-stopped \
--name v2raya-client \
mzz2017/v2raya
```

2. 访问：http://ip:10010/

#### Ⅳ、手机端使用 V2Ray

> 软件下载：[v2rayNG_1.8.25.apk](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/v2rayNG_1.8.25.apk)

1. 打开软件，点击右上角 + 号

![|254](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153200.png)

2. 选择：`手动输入[Vmess]`

![|229](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153220.png)

3. 依照下面的图片填入内容：
	1. 地址：服务器的 ip 
	2. 端口：V2Ray 服务端的端口
	3. 用户 ID：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `settings.clients.id`
	4. 额外 ID：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `settings.clients.alterId`
	5. 传入协议：选择 `ws`，即 `WebSocket ` 协议
	6. path：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `streamSettings.wsSettings.path`

![|258](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241121125059.png)

4. 点击右上角 `√` 号保存
5. 选择刚才创建的配置，点击连接即可

![|229](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153020.png)

#### Ⅴ、windows 端使用 V2Ray

> 软件下载：https://github.com/2dust/v2rayN/releases

1. 打开软件，点击左上角 `服务器` 按钮

![|625](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153707.png)

2. 选择：`添加[Vmess]服务器`

![|625](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153728.png)

3. 填入参数，内容与上面的手机端相同

![|625](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240627153807.png)

4. 点击确定，即可使用，软件会自动连接

### ③、Syncthing 文件同步的使用

#### Ⅰ、介绍

1. Syncthing 是跨平台的应用，可在 windows、linux、macOS、ios、android 等平台下载安装，可在不同设备之间同步文件
2. 因为在开发之际确实超前地考虑到全平台的通用性，因此采用了浏览器/服务器（B/S）架构以适应绝大多数操作系统和体系结构
3. Syncthing 的缺点是只能在不同设备之间同步文件，而不能在同一个设备的不同目录（硬盘）之间同步文件
4. 若想要在同一个设备的不同目录（硬盘）之间同步文件，可以使用下面的 FreeFileSync

#### Ⅱ、基本使用

> 下载地址：https://syncthing.net/downloads/

1. 下载对应版本后解压
2. 进入解压目录，启动应用：`./syncthing`
3. 启动成功后，进入网址即可：`http://localhost:8384`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240624160538.png)

4. 先点击添加远程设备，设备 ID 点击右上角操作 -> 显示设备 ID 获取；设备之间要互相绑定才可以
5. 再点击添加文件夹，<font color="#ff0000">文件夹 ID</font> 必须唯一，不同设备间根据 <font color="#ff0000">文件夹 ID</font> 进行同步
6. 添加完文件夹后，需点击共享，选择想要同步该文件夹的设备，点击保存即可开始同步

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240624161051.png)

#### Ⅲ、设置开机自启

1. 在某个录下创建一个名为 `syncthing.service` 的文件，内容如下：
	1. 需确保 `ExecStart` 参数的<font color="#ff0000">路径正确</font>

```shell
[Unit]
# 服务的描述，说明这个服务是做什么的。
Description=Syncthing - Open Source Continuous File Synchronization
# 提供了关于服务的文档的链接或路径，这里指向了 Syncthing 的手册页。
Documentation=man:syncthing(1)
# 指定了这个服务应该在网络服务完全启动后再启动，确保在启动时网络已可用。
After=network.target

[Service]
# 指定服务的启动类型。simple 是最常用的启动类型，表示由 ExecStart 指定的命令为主服务，服务启动即为该命令启动。
Type=simple
# 指定服务运行的用户，这里是 yan。这意味着 Syncthing 将以 yan 用户的权限运行。
User=yan
# 指定服务启动时执行的命令，这里是 Syncthing 的可执行文件的完整路径。
ExecStart=/home/yan/apply/file/syncthing-linux-amd64-v1.27.8/syncthing
# 服务失败时的重启策略。这里设置为 on-failure，意味着只有在服务异常退出时（如进程退出状态码非零）才会尝试重启。
Restart=on-failure
# 重启服务前等待的时间（秒）。这里设置为 10 秒，意味着服务崩溃后将等待 10 秒再进行重启。
RestartSec=10

[Install]
# 指定服务安装的目标。default.target 是多用户目标的一种通用别名，使服务能够在系统启动时启动。
WantedBy=default.target
```

2. 将服务文件移动到 `systemd` 目录

```shell
sudo mv syncthing.service /etc/systemd/system/
```

3. 重新加载 `systemd` 管理器配置

```shell
sudo systemctl daemon-reload
```

4. 启用服务

```shell
sudo systemctl enable syncthing.service
```

5. 启动服务

```shell
sudo systemctl start syncthing.service
```

6. 检查状态

```shell
sudo systemctl status syncthing.service
```

7. 关闭运行中的 Syncthing，可以在终端中查找其进程并杀掉它：

```shell
# 查找 Syncthing 进程
ps aux | grep syncthing

# 使用 kill 命令终止进程，其中 pid 是从上一步获得的进程 ID
kill [pid]
```

8. 重启服务：

```shell
sudo systemctl restart syncthing.service
```

#### Ⅳ、关闭开机自启

1. 停止服务：

```shell
sudo systemctl stop syncthing.service
```

2. 禁用服务：

```shell
sudo systemctl disable syncthing.service
```

3. 上面这两个命令会停止当前运行的 Syncthing 服务并从系统启动序列中移除它，这样在未来的系统启动时，Syncthing 将不会自动启动。
4. 如果确定不再需要这个服务，还可以删除服务文件：

```shell
sudo rm /etc/systemd/system/syncthing.service
```

5. 然后重新加载 systemd 配置以应用更改：

```shell
sudo systemctl daemon-reload
```

#### Ⅴ、使用 HTTPS 连接到 GUI

##### （1）、开启使用 HTTPS 连接到 GUI

1. 点击：操作 -> 设置 -> GUI，勾选使用 HTTPS 连接到 GUI，点击保存

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241101104348.png)

2. 然后重启服务，重启完成后，重新访问主页
3. 但是此时会显示：您的连接不是私密连接
4. 点击高级然后选择：继续前往127.0.0.1（不安全），可以进入主页

![|450](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241101104647.png)

5. 但是每次都这样选择太麻烦了，我们可以将 syncthing 自签的证书换成我们自己的，这样就不会有这个提示了

##### （2）、替换证书

> 1. 获取证书的方式：[使用 Let's Encrypt 免费获取证书](../编程相关/网络相关.md#1-1)
> 2. `cert.pem` 和 `key.pem` 是同步文件时使用的证书，不能替换，会导致证书验证出错无法同步文件
> 3. `https-cert.pem` 和 `https-key.pem` 是 GUI 客户端使用的证书，可以替换

1. 进入 syncthing 证书所在的目录
	1. windows 端的目录：`C:\Users\用户名\AppData\Local\Syncthing`
	2. linux 端的目录：`~/.local/state/syncthing/`

```shell
cd ~/.local/state/syncthing/
```

2. 将当前目录中原先存在的证书文件删除；只删除 `https-` 开头的两个

```shell
rm https-cert.pem https-key.pem
```

3. 将 `/etc/letsencrypt/archive/www.yue-hai.top/` 下的证书文件复制到当前目录，来替换 `https-cert.pem` 和 `https-key.pem`

```shell
sudo cp /etc/letsencrypt/archive/www.yue-hai.top/cert1.pem ./https-cert.pem
sudo cp /etc/letsencrypt/archive/www.yue-hai.top/privkey1.pem ./https-key.pem
```

4. 修改生成的文件的用户组：

```shell
# 修改用户组：
sudo chown yan:yan https-cert.pem https-key.pem
```

5. 重启服务，再次进入就不会有提示了

#### Ⅵ、配置目录单向备份（仅新增）

##### （1）、仅新增说明

1. 有 A、B 两个设备，A 设备产生新数据，B 设备用于数据备份
2. 我想要 A 设备指定目录中的所有数据都同步到 B 设备中，而且同步完之后，当 A 设备中删除数据后，B 设备中仍然保留，不会删除
3. 即仅新增 B 设备中没有的文件

##### （2）、设置仅新增

> 官方对这个选项的解释：[IgnoreDelete](https://docs.syncthing.net/advanced/folder-ignoredelete.html#ignoredelete)

1. 点击操作 -> 高级

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241120185037.png)

2. 在弹窗中选择文件夹 -> 想要设置为仅新增的文件夹

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241120185309.png)

3. 在打开的选项中，勾选 `Ignore Delete`；需要注意的是，这个选项只是忽略了删除命令，当文件被覆盖时，可能会引起旧文件的丢失。所以建议与版本控制一同使用，以防万一。

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241120185558.png)

4. 在最下方点击保存：

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241120185612.png)

5. 设置完毕

#### Ⅶ、

#### Ⅷ、

### ④、FreeFileSync 文件同步的使用

#### Ⅰ、介绍

1. FreeFileSync 是一款开源的文件同步软件，广泛用于备份和同步文件和文件夹。它支持多种操作系统，包括 Windows、macOS 和 Linux
2. 主要功能：
	1. 实时同步：通过 RealTimeSync 组件，用户可以实现文件的实时同步，这意味着任何文件的更改都会即时同步到目标位置。
	2. 批处理模式：用户可以创建 .ffs_batch 文件，这些文件包含同步任务的所有必要设置，可以通过命令行自动执行。
	3. 灵活的同步选项：支持镜像、更新和自定义同步，用户可以根据需要配置文件的复制和删除行为。
	4. 图形用户界面：提供直观的用户界面，使得文件同步的设置和执行变得简单易操作。
	5. 日志记录和错误报告：详细的日志帮助用户追踪同步任务的执行情况，及时发现和解决问题。
3. 使用场景：
	1. 数据备份：定期或实时备份重要数据到多个存储设备或云存储。
	2. 数据同步：在多个设备或位置之间同步数据，确保文件的一致性和可访问性。
	3. 自动化任务：通过批处理和命令行工具自动化常规的同步任务，节省时间和减少人为错误。
	4. FreeFileSync 是一个功能强大且灵活的工具，适用于个人用户和企业用户，帮助他们有效地管理文件同步和备份需求。
4. FreeFileSync 有四种同步模式：
	1. **双向模式**：源文件夹和目标文件夹内文件修改同步，修改任意文件夹内文件都影响到对方；
	2. **镜像模式**：源文件夹的文件修改会影响目标文件夹，目标文件夹的文件修改不会被保留且始终保持和源文件夹一致；
	3. **更新模式**：源文件夹的文件只会增量修改到目标文件夹，目标文件夹的修改可以保留且不影响源文件夹；
	4. **自定义模式**：自定义文件同步规则；
5. 使用的原因是 Syncthing 并不能实现同一个设备的不同目录（硬盘）之间同步文件，所以将 FreeFileSync 和 Syncthing 结合使用

#### Ⅱ、下载解压

1. 官网：https://freefilesync.org/download.php

![|675](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718092505.png)

2. 下载完成后，使用 tar 命令提取：

```shell
tar -xvf FreeFileSync_13.7_Linux.tar.gz
```

3. 会生成 `FreeFileSync_13.7_Install.run` 文件

#### Ⅲ、安装

1. 运行安装文件：

```shell
./FreeFileSync_13.7_Install.run
```

2. 输入 y 并按 ENTER 接受许可条款：

```shell
Accept the FreeFtlesync license terns? [y]es, [n]o, or [s]how: [y/n/s] y 
```

3. 设置项：
	1. 是否给所有用户安装
	2. 安装目录
	3. 是否创建快捷方式

```shell
FreeFilesync 13.7 Setup

1. Install for all users:    NO (current user only) 
2. Installation directory:   /home/yan/FreeFileSync 
3. Create desktop shortcuts: YES

Press a number [1-3] to change settings, 
ENTER to begin installation:
```

4. 设置项修改结果：

```shell
FreeFilesync 13. 7 Setup

1. Install for all users:    NO (current user only)
2. Installation directory:   /home/yan/apply/file/FreeFilesync 
3. Create desktop shortcuts: YES

Press a number [1-3] to change settings, 
ENTER to begin installation:
```

5. 按 ENTER 键继续安装：

```shell
-> Installing to: /home/yan/apply/file/FreeFileSync
-> New console command: freefilesync
-> Registering file extensions: *.ffs_gui, *.ffs_batch, *.ffs_real

All done!
           __     __
          /  \~~~/  \ 
    ,----(     ^^    )
   /      \__     __/
  /|         (\  |(
 ^ \   /___\  /\ |
    |__|   |__| "

Get the Donation Edition with bonus features and help keep FreeFileSync ad-free.
https://freefilesync.org/donate

yan@yan:~/apply/file/FreeFileSync$ 
```

6. 安装完成后，桌面上会多出来两个图标：

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718093931.png)

7. 绿色的 `FreeFileSync` 是 FreeFileSync 主程序
8. 红色的 `RealTimeSync` 是自动同步程序，启动后，若指定目录中的文件发生变化，则会执行对应脚本

#### Ⅳ、使用 FreeFileSync 同步文件

1. 点击绿色的 `FreeFileSync` 打开软件
2. FreeFileSync 的用户界面：
	1. 1：保存 / 加载配置
	2. 比较内容缩略图
	3. 比较文件差异按钮
	4. 文件比较设置
	5. 过滤器设置
	6. 文件同步设置
	7. 文件同步按钮
	8. 添加文件目录组
	9. 源文件目录
	10. 两侧互换按钮
	11. 目标文件目录
	12. 源文件目录与目标目录不同的文件列表
	13. 同步动作预览区域
	14. 目标文件与源文件不同的列表
	15. 同步动作统计

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718124000.png)

3. 打开过滤器，在排除项中加入以下内容：
	1. 因为是将 FreeFileSync 和 Syncthing 结合使用，所以同步的目录中有 Syncthing 创建的目录
	2. 这里是将 Syncthing 创建的目录排除掉

```shell
*/.stfolder*
*/.stfolder/*
*/.stversions/*
```

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241119162520.png)

4. 点击同步设置，改为镜像模式：
	1. 因为多端文件的同步使用的是 Syncthing，FreeFileSync 只是作为文件备份工具来使用，所以使用镜像模式
	2. 四种模式的区别请参照第一节

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718130803.png)

5. 关于上面的使用数据库文件来检测变化的作用：
	1. 当启用使用数据库文件的选项时，FreeFileSync 会创建一个数据库来记录文件和文件夹的状态信息。这些信息包括文件的大小、修改时间和其他元数据。通过这种方式，每次同步时 FreeFileSync 只需要比较当前文件状态与数据库中记录的状态，从而确定哪些文件发生了变化。这种方法的优势包括：
		1. 效率更高：比较过程只需对比数据库中的记录与当前状态，不需要对整个文件内容进行扫描，从而提高同步的效率。
		2. 减少资源消耗：减少了对磁盘的读写操作，尤其是在文件数量庞大的情况下。
		3. 改进的变化检测：能够更精确地识别出哪些文件确实发生了变化，即使文件修改时间没有更新。
	2. 如果不使用数据库文件，FreeFileSync 将直接比较源和目标文件夹中的文件。这通常涉及到比较文件的大小、修改时间等属性。这种方法的特点包括：
		1. 简单直接：不需要额外创建和维护数据库文件，操作更为直接。
		2. 可能的性能开销：在没有数据库辅助的情况下，每次同步可能需要更多的时间和计算资源，特别是文件数量多或文件大小大的情况下。
		3. 适用性：对于较小的或不经常变化的文件集，这种方法可能更加高效。
	3. 总的来说，选择使用数据库文件还是不使用，取决于具体需求、文件数量以及同步频率。使用数据库可以显著提高大规模文件同步的效率和准确性，但如果同步任务不频繁或文件数量较少，直接比较也是一个有效的选择。
6. 点击浏览可以选择同步的目录：
	1. 左边的目录是原始目录，右边的目录是目标目录
	2. 当左边的目录中的内容发生变化时，会将变化同步至右边的目录中
	3. 具体的同步细节再上面的同步设置中
	4. 可以选择多个目录，也可以一对多

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718131152.png)

7. 此时点击同步按钮即可开始同步

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718131527.png)

8. 点击保存可以将本次的设置保存下来，以便下次使用

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718131619.png)

#### Ⅴ、使用 RealTimeSync 自动同步文件

1. 点击绿色的 `FreeFileSync` 打开软件
2. 先选择刚才保存的配置，然后点击上方的另存为批处理作业

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718131908.png)

3. 可以选择以最小化运行以及忽略错误，点击另存为保存

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718132037.png)

4. 点击红色的 `RealTimeSync` 打开软件
5. 首先选择要监视变化的目录，一般和上面选择同步的原始目录相同
6. 然后填入检测到变化后要执行的命令行，此处填入 FreeFileSync 安装路径及程序，后面以刚才保存的批处理作业的路径为参数

```shell
/home/yan/apply/file/FreeFileSync/FreeFileSync /home/yan/apply/file/FreeFileSync/sava/SyncSettings.ffs_batch
```

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240718132846.png)

7. 最后的选项运行命令之前最小的空闲时间（以秒计），表示如果监测到了目录中的内容发生了变化，延迟执行命令的时间
8. 点击开始，即可启动后台任务，当程序监测到了目录中的内容发生了变化，就会执行同步操作

#### Ⅵ、关闭 RealTimeSync 自动同步任务

1. 在命令行输入 `ps -ef | grep FreeFileSync` 命令查看 FreeFileSync 是否在后台运行：

```shell
ps -ef | grep FreeFileSync
```

```shell
yan@yan:~$ ps -ef|grep FreeFileSync
yan      2601322 2598642  0 13:22 ?        00:00:00 /home/yan/apply/file/FreeFileSync/RealTimeSync
yan      2601327 2601322  0 13:22 ?        00:00:00 /home/yan/apply/file/FreeFileSync/Bin/RealTimeSync_x86_64
yan      2601781 2591203  0 13:32 pts/4    00:00:00 grep --color=auto FreeFileSync

yan@yan:~$ 
```

2. 从输出来看确实是在后台运行
3. 根据进程号关闭进程

```shell
kill 2601322 2601327
```

4. 如果想要确保进程被强制终止，可以使用 kill -9 命令：

```shell
kill -9 2601322 2601327
```

#### Ⅶ、同步日志记录脚本

1. 进入 `/home/yan/apply/file/FreeFileSync/sava/` 目录：

```shell
cd /home/yan/apply/file/FreeFileSync/sava/
```

2. 创建脚本文件 `record_logs.sh`：

```shell
touch record_logs.sh
```

3. 编辑脚本，输入以下内容：

```shell
#!/bin/bash

# 检查参数个数，如果不等于2，则提示错误
if [ "$#" -ne 2 ]; then
    echo "错误: 未提供源目录和目标目录"
    echo "使用: $0 <源目录路径> <目标目录路径>"
    echo "例如: $0 /home/yan/桌面/内存/文档资料/ /media/yan/hc330-10t-A/内存/文档资料/"
    exit 1
fi

# 日志所在路径
path="/home/yan/apply/file/FreeFileSync/sava"
# 源目录路径
source_path="$1"
# 目标目录路径
target_path="$2"
# 获取当前时间
current_time=$(date "+%Y-%m-%d %H:%M:%S")

# 向文件中追加成功日志
echo "【${current_time}】同步已完成" >> "$path/synchronize_logs.log"
# 向文件中追加源目录路径、目标目录路径
echo "同步目录为：$source_path -> $target_path" >> "$path/synchronize_logs.log"
# 向文件中追加分隔符
echo "--------------------------------" >> "$path/synchronize_logs.log"
# 向文件中追加空行
echo "" >> "$path/synchronize_logs.log"
```

4. 打开软件 FreeFileSync，选中配置，点击设置，再选中同步标签，再执行一个命令处选择：在完成时，然后再后面填上脚本路径和参数：
 
```shell
bash /home/yan/apply/file/FreeFileSync/sava/record_logs.sh /home/yan/桌面/内存/文档资料/ /media/yan/hc330-10t-A/内存/文档资料/
```

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241119165725.png)

#### Ⅷ、定时执行同步任务

##### （1）、说明

1. 使用定时执行同步任务，而不是上面使用 RealTimeSync 检测到文件变动就自动同步的原因是：如果 Syncthing 和 FreeFileSync 配合使用，当 RealTimeSync 检测到文件变动时会锁住文件，这时 Syncthing 就不能对文件进行操作了，只能生成很多副本，要手动删除，很麻烦，而且有时会导致同步混乱，数据出问题
2. 所以现在的解决方案是，先使用 Syncthing 将文件同步到路径 A，然后选择一个基本不会对文件进行修改的时间（比如凌晨 2 点），调用 FreeFileSync 进行同步
3. 这样时间错开，也就不会出现文件被锁住，同步出问题的情况了

##### （2）、为什么要使用 XVFB 模拟 X 环境

1. 由于 FreeFileSync 是图形化程序，需要图形界面支持。而如果没有桌面环境（GUI 环境），FreeFileSync 将无法启动，会报错。
2. 直接在 ssh 远程命令行中执行的报错：
 
```shell
yan@yan:~/apply/file/FreeFileSync/sava$ /home/yan/apply/file/FreeFileSync/FreeFileSync /home/yan/apply/file/FreeFileSync/sava/batch/document-um773-hc330.ffs_batch
Authorization required, but no authorization protocol specified
12:54:10: Error: Unable to initialize GTK+, is DISPLAY set properly?

yan@yan:~/apply/file/FreeFileSync/sava$
```

3. 为了在服务器或无桌面环境的系统上正常运行 FreeFileSync，我们可以安装并使用 X Virtual Framebuffer (XVFB)
4. 它可以模拟一个 X11 图形界面环境，使得 FreeFileSync 可以在没有物理显示器的情况下正常工作。

##### （3）、安装 XVFB 模拟 X 环境

1. 更新软件源：

```shell
sudo apt update
```

2. 安装 Xvfb：

```shell
sudo apt install xvfb
```

3. 可以通过启动 XVFB 来验证是否安装成功，使用以下命令启动一个 XVFB 会话：
	1. `:1` 指定了显示编号，可以根据需要设置为其他值
	2. `&` 在后台启动 XVFB，会生成一个虚拟显示环境。

```shell
Xvfb :1 &
```

4. XVFB 启动后，需要通过设置 DISPLAY 环境变量来告知 FreeFileSync 使用这个虚拟显示环境。例如，可以在执行 FreeFileSync 命令前添加以下内容：

```shell
export DISPLAY=:1
```

5. 这样，FreeFileSync 将会在 XVFB 提供的虚拟显示环境中运行，不会受到物理显示器的限制；此时再执行将不会报错：

```shell
/home/yan/apply/file/FreeFileSync/FreeFileSync /home/yan/apply/file/FreeFileSync/sava/batch/document/document-um773-hc330A.ffs_batch
```
 
##### （4）、编写脚本，将 XVFB 与 FreeFileSync 一同运行

> 1. FreeFileSync `_batch` 脚本保存位置：
> 	1. 文档 document：`/home/yan/apply/file/FreeFileSync/sava/batch/document`
> 	2. 内存 memory：`/home/yan/apply/file/FreeFileSync/sava/batch/memory`
> 	3. 备份 backup：`/home/yan/apply/file/FreeFileSync/sava/batch/backup`
> 2. 整合脚本保存位置：`/home/yan/apply/file/FreeFileSync/sava/batch/`

1. 进入目录：

```shell
cd /home/yan/apply/file/FreeFileSync/sava/batch/
```

2. 创建整合脚本 `start_backup_task.sh`

```shell
touch start_backup_task.sh
```

2. 将 XVFB 与 FreeFileSync 整合到脚本，在启动 XVFB 后自动运行 FreeFileSync：

```shell
#!/bin/bash

# 检查是否提供了参数
if [ -z "$1" ]; then
    echo "错误: 未提供配置文件路径！"
    echo "使用: $0 <配置文件路径>"
    echo "例如: $0 /document/document-um773-hc330.ffs_batch"
    exit 1
fi

# 定义基础路径
BASE_PATH="/home/yan/apply/file/FreeFileSync"
# 定义程序路径
PROGRAM_PATH="$BASE_PATH/FreeFileSync"
# 接收传入的参数，指定调用的配置文件
CONFIG_FILE="$BASE_PATH/sava/batch$1"

# 检查指定的配置文件是否存在
if [ ! -f "$CONFIG_FILE" ]; then
    echo "错误: 配置文件 $CONFIG_FILE 不存在！"
    exit 1
fi

# 设置 DISPLAY 环境变量，指定 X 显示编号为 :1
# 这样 FreeFileSync 可以在虚拟显示环境中运行
export DISPLAY=:1
# 设置 DBUS_SESSION_BUS_ADDRESS 环境变量，指定 D-Bus 会话总线地址
# D-Bus 用于在应用程序之间传递信息，该变量指定了会话总线的路径
# 替换为实际的路径（可以通过 echo $DBUS_SESSION_BUS_ADDRESS 获取）
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

# 启动虚拟显示环境 XVFB，指定显示编号为 :1
# XVFB (X Virtual Framebuffer) 是 X11 的虚拟显示服务器，用于在没有物理显示器的环境下运行图形化应用程序
/usr/bin/Xvfb :1 &
# 保存 Xvfb 进程的 PID，方便在后续终止
XVFB_PID=$!
# 使用 trap 命令，当脚本退出时（无论是正常退出还是因错误中断）自动执行 kill 命令终止 Xvfb 进程
trap "kill $XVFB_PID" EXIT

# 等待 2 秒，确保 XVFB 已经完全启动，避免后续的程序执行时找不到显示环境
sleep 2

# 根据指定的配置文件执行 FreeFileSync 进行同步任务
/home/yan/apply/file/FreeFileSync/FreeFileSync "$CONFIG_FILE"
```

##### （5）、设置定时任务运行脚本

1. 在命令行输入命令进入任务编辑器：

```shell
crontab -e
```

2. 设置定时运行：

```shell
# 下载阿里云的 docker 数据：每天凌晨 0 点；阿里云:/home/docker/docker/volumes/ -> /home/yan/桌面/dockerData/
00 00 * * 1-5 /home/yan/apply/file/CloudServerFileCopy/aliyun/aliyun_file_copy.sh
# 同步 docker 数据：周一至周五，每天凌晨 1 点；/home/yan/桌面/dockerData/ -> /media/yan/hc330-10t-A/dockerData/
00 01 * * 1-5 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /docker/docker-aliyun-hc330A.ffs_batch
# 同步 docker 数据：周一至周五，每天凌晨 2 点；/home/docker/docker/volumes/ -> /media/yan/hc330-10t-A/dockerData/
00 02 * * 1-5 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /docker/docker-um773-hc330A.ffs_batch
# 同步文档资料：周一至周五，每天凌晨 4 点；/home/yan/桌面/内存/文档资料/ -> /media/yan/hc330-10t/内存/文档资料/
00 04 * * 1-5 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /document/document-um773-hc330A.ffs_batch

# 同步【内存】：周六凌晨 2 点；/media/yan/hc330-10t-A/内存/ -> /media/yan/东芝V10-4t/内存/
00 02 * * 6 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /memory/memory-hc330A-V10.ffs_batch
# 同步【内存】：周六凌晨 4 点；/media/yan/hc330-10t-A/内存/ -> /media/yan/hc550-16t-A/内存/
00 04 * * 6 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /memory/memory-hc330A-hc550A.ffs_batch

# 同步【备份】：周日凌晨 2 点；/media/yan/hc330-10t-A/备份/ -> /media/yan/hc550-16t-A/备份/
00 02 * * 7 /home/yan/apply/file/FreeFileSync/sava/batch/start_backup_task.sh /backup/backup-hc330A-hc550A.ffs_batch
```

#### Ⅸ、以管理员权限启动 FreeFileSync

1. 如果在本地机器上运行，确保当前用户有权访问 X 服务器。这可以通过 xhost 工具管理。可以临时允许所有用户访问 X 服务器（注意这有安全风险）

```shell
xhost +
```

2. 如果在图形界面环境中直接运行命令且遇到权限问题，可以尝试使用 gksudo 或 pkexec 而不是 sudo 来运行图形界面应用，因为 sudo 可能不会传递必要的环境变量；要使用应用的全路径：

```shell
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY /home/yan/apply/file/FreeFileSync/FreeFileSync
```

3. 执行后，会提示输入密码，输入当前用户的密码即可

#### Ⅹ、FreeFileSync 备份 docker 应用时备份失败的应用记录

##### （1）、报错

```shell
15时21分26秒	错误	无法打开文件 "/home/docker/docker/volumes/qbittorrent/config/qBittorrent/ipc-socket".
		不支持的项目类型. [socket, 0140000]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-mcn02:1-6cfa.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:light:0000A001:lemesh-wy02:1-2a54.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:light:0000A001:yeelink-lamp21:1:0000C802-65c1.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:outlet:0000A002:cuco-v3:2-f91c.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:printer:0000A060:xiaomi-label:1-dc58.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:router:0000A036:xiaomi-ra74:1-f51c.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:scale:0000A07D:hmpace-mibfs:1-4adb.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:temperature-humidity-sensor:0000A00A:miaomiaoce-t9:1-6be5.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-mcn02:1-8812.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:light:0000A001:lemesh-wy02:1-73e3.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:light:0000A001:yeelink-lamp21:1:0000C802-8777.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:outlet:0000A002:cuco-v3:2-b2f7.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:printer:0000A060:xiaomi-label:1-fc74.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:router:0000A036:xiaomi-ra74:1-ee50.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:scale:0000A07D:hmpace-mibfs:1-b5c9.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法写入文件 "/media/yan/hc330-10t-A/dockerData/homeassistant/config/.storage/xiaomi_miot/spec-langs/urn:miot-spec-v2:device:temperature-humidity-sensor:0000A00A:miaomiaoce-t9:1-e59d.ffs_tmp".
		EINVAL: 无效的参数 [open]
15时21分29秒	错误	无法创建目录 "/media/yan/hc330-10t-A/dockerData/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"675136d5-77d"".
		EINVAL: 无效的参数 [mkdir]
15时21分29秒	错误	无法创建目录 "/media/yan/hc330-10t-A/dockerData/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"67514869-77d"".
		EINVAL: 无效的参数 [mkdir]
15时21分29秒	错误	无法创建目录 "/media/yan/hc330-10t-A/dockerData/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"67517299-77d"".
		EINVAL: 无效的参数 [mkdir]
15时21分29秒	错误	无法创建目录 "/media/yan/hc330-10t-A/dockerData/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"6757a7a9-77d"".
		EINVAL: 无效的参数 [mkdir]
15时21分29秒	错误	无法创建目录 "/media/yan/hc330-10t-A/dockerData/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"675fbad9-77d"".
		EINVAL: 无效的参数 [mkdir]
```

##### （2）、原因

1. 有的应该是尝试访问的对象是不支持操作的类型，如 socket 文件
	1. `qbittorrent/config/qBittorrent/ipc-socket`
2. 有的应该是容器在运行，被容器占用，所以直接复制不行
	1. 比如以 `tmp` 结尾的文件
3. 还有的是目录带有特殊符号，无法直接创建目录、复制目录
	1. `/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"675fbad9-77d"`
	2. `/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-mcn02:1.json`

##### （3）、报错应用记录

> 有的报错应该是容器在运行，所以直接复制不行

1. Home Assistant 智能家居平台：
	1. `/homeassistant/config/`
2. mysql 数据库：
	1. `/mysql/data/`
3. nextcloud 自托管云存储和协作平台：
	1. `/nextcloud/data/`
4. nginx-proxy-manager-zh 基于 Nginx 的反向代理管理工具
	1. `/nginx-proxy-manager/data/`
5. qbittorrent BitTorrent 客户端
	1. `/qbittorrent/config/`
6. qinglong 青龙定时任务管理
	1. `/qinglong/data/`
7. xunlei 迅雷群晖提取版
	1. `/xunlei/data/`

##### （4）、备份 docker 应用时的排除

```shell
*/.Trash-*/
*/.recycle/
*/.stfolder*
*/.stfolder/*
*/.stversions/*
/homeassistant/config/.storage/xiaomi_miot/urn*
/homeassistant/config/.storage/xiaomi_miot/spec-langs/*
/homeassistant/config/.storage/xiaomi_home/miot_specs/urn*
/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/
/qbittorrent/config/qBittorrent/ipc-socket
/xunlei/downloads/
```

### ⑤、使用 mailutils 发送邮件

#### Ⅰ、安装 mailutils

1. 查询是否已经安装：

```shell
mail --version
```

2. 更新软件源：

```shell
sudo apt update
```

3. 安装 mailutils

```shell
sudo apt install mailutils
```

4. 再次查询是否已经安装：

```shell
mail --version
```

```shell
yan@yan:~$ mail --version
mail (GNU Mailutils) 3.14
Copyright (C) 2007-2022 Free Software Foundation, inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

yan@yan:~$ 
```

#### Ⅱ、发送邮件

1. 使用 `mail` 命令发送邮件：

```shell
echo "测试邮件正文" | mail -s "测试邮件主题" -r yan@yue-hai.top 770717410@qq.com
```

2. `"测试邮件正文"`：邮件正文
3. `mail`：用于发送邮件
4. `-s "测试邮件主题"`：指定邮件的主题（标题）为：测试邮件主题
5. `-r yan@yue-hai.top`：指定邮件的发件人地址为 `yan@yue-hai.top`
6. `770717410@qq.com`：指定邮件的收件人地址为 `770717410@qq.com`

### ⑥、使用 NUT 配置 UPS 不间断电源

> 参考：https://www.wangchucheng.com/zh/posts/setting-up-ups-with-nut-on-linux/#%E5%AE%9A%E6%97%B6%E5%85%B3%E6%9C%BA

1. 此处我使用的 UPS 设备是：山特 TG-BOX850
2. 首先需要将 UPS 接入电源并将电脑接入 UPS 插座，还需要将 UPS 的数据线与电脑的 USB 口相连接
3. 系统是：Ubuntu 22.04.3 LTS

#### Ⅰ、安装 NUT

1. NUT（Network UPS Tools）是一套开源工具，用于监控 UPS（不间断电源）以及与 UPS 相关的电源设备，并在电源出现问题时自动执行操作（如关机）
2. NUT 在各类 Linux 系统中均可以使用默认的包管理工具进行安装。我使用的是 Ubuntu 22.04.3 LTS，安装指令如下所示：

```shell
# 更新软件源
sudo apt update

# 安装 nut
apt install nut
```

#### Ⅱ、配置 UPS

##### （1）、配置 UPS 驱动

1. 使用以下查看设备是否被正常接入：

```shell
lsusb
```

2. 若是被正常识别则会包含类似于如下的内容：`Bus 001 Device 002: ID 0463:ffff MGE UPS Systems UPS`

```shell
root@yan:/usr/local/bin# lsusb
Bus 009 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 010 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 007 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 003: ID 125f:a578 A-DATA Technology Co., Ltd. ORICO USB Device
Bus 004 Device 002: ID 0480:0820 Toshiba America Inc Canvio Advance Disk
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 002: ID 0e8d:0608 MediaTek Inc. Wireless_Device
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 002: ID 0463:ffff MGE UPS Systems UPS
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
root@yan:/usr/local/bin# 
```

2. 修改 `/etc/nut/ups.conf` 文件，在其中添加如下内容：

```shell
nano /etc/nut/ups.conf
```

```shell
# tg-box-850：自己定义的设备名
# driver = usbhid-ups：驱动名，不可修改
# port = auto：端口号，自动
# desc = "SANTAK TGBOX-850"：描述信息，可随意修改
[tg-box-850]
  driver = usbhid-ups
  port = auto
  desc = "SANTAK TGBOX-850"
```

3. 接下来可以通过以下命令启动 UPS：

```shell
/sbin/upsdrvctl start
```

4. 停止 UPS：

```shell
/sbin/upsdrvctl stop
```

##### （2）、查看 UPS 的相关信息

1. 查看 UPS 的相关信息：

```shell
# 使用上面配置的设备名 tg-box-850 查看 UPS 的相关信息
/bin/upsc tg-box-850@localhost

# 也可以选取特定类别的信息进行查看：
/bin/upsc tg-box-850@localhost ups.status
```

2. 属性说明：

```shell
root@yan:~# /bin/upsc tg-box-850@localhost
Init SSL without certificate database
# 电池相关属性
battery.charge: 100                  // 电池当前的电量百分比，显示为 100%，意味着电池已完全充满
battery.charge.low: 20               // 电池低电量的阈值，当电池电量降到 20% 时，系统可能会触发低电量警报或采取相应措施
battery.runtime: 3216                // 当前负载条件下电池的剩余运行时间，单位为秒，3216 秒约为 53 分钟
battery.type: PbAcid                 // 电池类型，PbAcid 表示铅酸电池
# 设备相关属性
device.mfr: EATON                    // 设备的制造商为 EATON，这是一家电源管理公司，生产 UPS 设备
device.model: SANTAK TG-BOX 850      // 设备型号为 SANTAK TG-BOX 850，表明这是 EATON 旗下 SANTAK 品牌的一款 850VA 的 UPS
device.serial: Blank                 // 设备的序列号为空，可能是因为 UPS 设备没有序列号
device.type: ups                     // 设备类型为UPS（Uninterruptible Power Supply，不间断电源）
# 驱动相关属性
driver.name: usbhid-ups              // 当前使用的 UPS 驱动名称为 usbhid-ups，这是 NUT（Network UPS Tools）系统中的一个常用 USB HID 类 UPS 驱动
driver.parameter.pollfreq: 30        // 轮询频率，表示每 30 秒查询一次设备状态
driver.parameter.pollinterval: 2     // 轮询间隔，表示每 2 秒对 UPS 状态进行一次查询
driver.parameter.port: auto          // 通信端口，auto 表示自动选择端口
driver.parameter.synchronous: no     // 是否同步通信，no 表示不是以同步方式与设备通信
driver.version: 2.7.4                // 驱动版本为 2.7.4
driver.version.data: MGE HID 1.40    // 驱动数据版本为 MGE HID 1.40
driver.version.internal: 0.41        // 驱动内部版本为 0.41
# 输入/输出相关属性
input.transfer.high: 264             // 输入电压的高阈值，当输入电压超过 264V 时，系统可能会触发高电压警报或采取相应措施
input.transfer.low: 184              // 输入电压的低阈值，当输入电压低于 184V 时，系统可能会触发低电压警报或采取相应措施
output.frequency.nominal: 50         // 输出电压的标称频率为 50Hz
output.voltage: 230.0                // 输出电压为 230V
output.voltage.nominal: 220          // 输出电压的标称值为 220V
# 电源输出插座相关属性
outlet.1.desc: PowerShare Outlet 1   // 描述了 outlet.1 的用途，PowerShare Outlet 1 表示这是一个 PowerShare 电源输出插座
outlet.1.id: 1                       // outlet.1 的 ID 为 1，表示这是第一个电源输出插座
outlet.1.status: on                  // outlet.1 的状态为 on，表示这个电源输出插座当前处于开启状态
outlet.1.switchable: no              // outlet.1 不可切换，表示这个电源输出插座不支持远程开关
outlet.desc: Main Outlet             // 描述了 outlet 的用途，Main Outlet 表示这是一个主要的电源输出插座
outlet.id: 0                         // outlet 的 ID 为 0，表示这是主要的电源输出插座
outlet.switchable: yes               // outlet 可切换，表示这个电源输出插座支持远程开关
# UPS状态及其他属性
ups.beeper.status: enabled           // UPS 蜂鸣器状态为 enabled，表示 UPS 蜂鸣器当前处于开启状态
ups.delay.shutdown: 20               // UPS 从收到关机命令到实际执行关机的延迟时间为 20 秒
ups.delay.start: 30                  // UPS 从电源恢复到开始供电的延迟时间为 30 秒
ups.firmware: 02.08.0010             // UPS 固件版本为 02.08.0010
ups.load: 6                          // UPS 当前的负载为 6.0%，表示连接到 UPS 的设备功耗占 UPS 最大输出功率的 6.0%
ups.mfr: EATON                       // UPS 制造商为 EATON
ups.model: SANTAK TG-BOX 850         // UPS 型号为 SANTAK TG-BOX 850
ups.power.nominal: 850               // UPS 的标称功率为 850VA
ups.productid: ffff                  // UPS 产品 ID 为 ffff
ups.serial: Blank                    // UPS 序列号为空
ups.status: OL                       // UPS 状态为 OL，表示 UPS 处于在线状态
ups.timer.shutdown: 0                // UPS 距离关机的时间为 0 秒，表示没有设置定时关机
ups.timer.start: 0                   // UPS 距离开始供电的时间为 0 秒，表示没有设置定时开机
ups.type: offline / line interactive // UPS 为线交互型，表示在市电异常时会切换到电池供电
ups.vendorid: 0463                   // UPS 供应商 ID 为 0463
```

#### Ⅲ、配置 NUT 服务

- 此处将设置操作 UPS 的用户信息

##### （1）、新建用户

1. 配置用户信息，编辑 `/etc/nut/upsd.users` 文件，添加以下内容：

```shell
nano /etc/nut/upsd.users
```

```shell
# tgbox-850：用户名
# password = 000123：密码
# upsmon master：运行模式；如果该设备为主节点则为该值，从节点则为 upsmon slave
[tgbox-850]
  password = 000123
  upsmon master
```

##### （2）、配置权限

1. 需要注意的是我们不应使该文件对所有用户均可读，因为它包含密码等敏感信息。我们可以使用如下命令设置相关权限：

```shell
# 确保只有 root 用户和 nut 组的成员可以读取和修改 /etc/nut/upsd.conf 和 /etc/nut/upsd.users 文件
chown root:nut /etc/nut/upsd.conf /etc/nut/upsd.users
chmod 0640 /etc/nut/upsd.conf /etc/nut/upsd.users
```

##### （3）、启动服务

1. 启动服务：

```shell
/sbin/upsd
```

2. 重启服务：

```shell
/sbin/upsd -c reload
```

3. 查看帮助

```shell
/sbin/upsd --help
```

4. 如果在启动服务时产生报错，可先设置 NUT 运行模式。使用编辑 `/etc/nut/nut.conf` 文件并选择模式，将其配置为 `standalone` 模式

```shell
nano /etc/nut/nut.conf
```

```shell
# 将其配置为 standalone 模式
MODE=standalone
```

##### （4）、设置电池低电量自动关机

1. NUT 默认会在 UPS 发送 LOWBATT （电池电量低）时通知机器关机，需配置 `/etc/nut/upsmon.conf` 文件

```sehll
nano /etc/nut/upsmon.conf
```

2. 搜索 `MONITOR`，若原有配置项则替换，没有则直接添加：定义要监控的 UPS 设备

```shell
# 参数为：
# tg-box-850@localhost：UPS 驱动配置的设备名
# 1：NUT 守护进程监控 UPS 的优先级，数值越低，优先级越高。1 表示这是最高优先级
# tgbox-850：NUT 服务配置的用户名
# 000123：NUT 服务配置的用户密码
# master：NUT 服务配置的运行模式
MONITOR tg-box-850@localhost 1 tgbox-850 000123 master
```

3. 搜索 `SHUTDOWNCMD`，若原有配置项则替换，没有则直接添加：定义当系统需要关闭时执行的命令：

```shell
# 一分钟后关机
SHUTDOWNCMD "/sbin/shutdown -h +1"
```

4. 搜索 `POWERDOWNFLAG`，若和此处相同则不需要修改，没有则直接添加；
	1. 路径设置：`POWERDOWNFLAG /etc/killpower` 表示标志文件将被创建在 `/etc/killpower` 这个路径下。
	2. 触发条件：当 UPS 在电池供电状态下，并且电池电量低到一个临界点（即将耗尽），upsmon 会创建这个文件。
	3. 这通常是在 `FINALDELAY` 设置的最后等待时间之后，系统执行关机命令之前的一个步骤。
	4. 系统关机脚本使用：在系统的关机脚本中，应该检查这个文件是否存在。如果存在，这意味着应该执行一个安全关机，通常是通过执行 `upsdrvctl shutdown` 命令来确保 UPS 设备也被正确关闭，避免硬件损坏。

```shell
POWERDOWNFLAG /etc/killpower
```

5. 由于该文件同样包含敏感信息，因此需要为其设置权限：

```shell
chown root:nut /etc/nut/upsmon.conf
chmod 0640 /etc/nut/upsmon.conf
```

6. 最后只需启动服务即可：

```shell
/sbin/upsmon
```

#### Ⅳ、自定义事件

##### （1）、介绍

1. 除了默认的低电量关机功能，可能我们有时还需其他自定义的功能。例如停电一分钟后关机或者邮件通知等。NUT 通过 upssched 提供了该功能。
2. 该功能的实现为通过在 upsmon 中设置触发条件通知 upssched，并由 upssched 完成后续工作。

##### （2）、修改 upsmon 设置

1. 编辑 `/etc/nut/upsmon.conf` 文件：

```shell
nano /etc/nut/upsmon.conf
```

2. 添加如下内容，这可以使我们在发生事件时运行 upssched 服务：

```shell
# 当触发特定 UPS 事件时，NUT 会调用 upssched 程序来处理这些事件
# upssched 是一个调度程序，可以通过设定延迟或条件来处理自定义事件；比如停电后一分钟执行某个脚本或发送邮件通知
NOTIFYCMD /sbin/upssched
# 在特定 UPS 事件触发时的通知方式。在这里设置的具体含义如下：
# ONBATT：这是事件类型，表示当 UPS 转为电池供电（即市电断电）时触发。
# SYSLOG：指定当 ONBATT 事件发生时，将消息写入系统日志中。这可以帮助管理员查看系统日志时获取 UPS 的事件信息。
# WALL：指定当 ONBATT 事件发生时，向所有登录用户发出通知。这在多用户系统中非常有用，可以及时提醒所有人 UPS 进入电池供电状态。
# EXEC：指定当 ONBATT 事件发生时，执行前面配置的 NOTIFYCMD 中的命令（在这里是 /sbin/upssched）;
#       这意味着在UPS转为电池供电时，将会自动调用 upssched 程序，从而根据 upssched 的配置文件进一步处理事件
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
# ONLINE：UPS 恢复使用在线电力时触发
NOTIFYFLAG ONLINE SYSLOG+WALL+EXEC
# LOWBATT：UPS 电池电量低时触发
NOTIFYFLAG LOWBATT SYSLOG+WALL+EXEC
# FSD：由主控触发的强制关机时触发
NOTIFYFLAG FSD SYSLOG+WALL+EXEC
# COMMOK：与 UPS 的通信已建立时触发
NOTIFYFLAG COMMOK SYSLOG+WALL+EXEC
# COMMBAD：与 UPS 的通信已丢失时触发
NOTIFYFLAG COMMBAD SYSLOG+WALL+EXEC
# SHUTDOWN：系统正在关机时触发
NOTIFYFLAG SHUTDOWN SYSLOG+WALL+EXEC
# REPLBATT：UPS 电池需要更换时触发
NOTIFYFLAG REPLBATT SYSLOG+WALL+EXEC
# NOCOMM：无法联系到 UPS 进行监控时触发
NOTIFYFLAG NOCOMM SYSLOG+WALL+EXEC
# NOPARENT：负责关机的进程已死亡，关机无法执行时触发
NOTIFYFLAG NOPARENT SYSLOG+WALL+EXEC
```

3. 在此设置的是当 UPS 状态改变时写入日志并运行之前定义的 upssched 服务。

##### （3）、配置 upssched

1. 在 `/etc/nut/upssched.conf` 文件中设置具体的实现逻辑：

```shell
nano /etc/nut/upssched.conf
```

2. 将 `CMDSCRIPT /bin/upssched-cmd` 这一行注释掉，然后在下面写入如下内容：

```shell
# 在事件发生时，upssched 将要执行脚本 /usr/local/bin/upssched
CMDSCRIPT /usr/local/bin/upssched
# 指定了 upssched 使用的管道文件的路径。在 NUT 系统中，upssched 通过管道与其他进程通信，传递事件和指令。
# 这里设置了管道文件的位置为 /var/run/nut/upssched/upssched.pipe，通常用于传递事件信息。
PIPEFN /var/run/nut/upssched/upssched.pipe
# 指定了锁文件的位置。锁文件用于确保同时只有一个 upssched 实例在处理事件，防止多次执行相同的事件。
# 这里的锁文件路径为 /var/run/nut/upssched/upssched.lock
LOCKFN /var/run/nut/upssched/upssched.lock

# 定义了当 UPS 切换到电池供电（ONBATT）时的行为：
# ONBATT *：当任何（*）UPS 设备进入电池供电模式时触发
# EXECUTE power-off：立即将 power-off 作为参数传递给 CMDSCRIPT 指定的脚本
AT ONBATT * EXECUTE power-off
# 定义了在 UPS 恢复市电时的操作
AT ONLINE * EXECUTE power-on

# 定义了 UPS 电池电量低时触发
AT LOWBATT * EXECUTE LOWBATT
# 定义了 UPS 电池需要更换时触发
AT REPLBATT * EXECUTE REPLBATT

# 定义了与 UPS 的通信已建立时触发
AT COMMOK * EXECUTE COMMOK
# 定义了与 UPS 的通信已丢失时触发
AT COMMBAD * EXECUTE COMMBAD

# 定义了由主控触发的强制关机时触发
AT FSD * EXECUTE FSD
# 定义了系统正在关机时触发
AT SHUTDOWN * EXECUTE SHUTDOWN
# 定义了无法联系到 UPS 进行监控时触发
AT NOCOMM * EXECUTE NOCOMM
# 定义了负责关机的进程已死亡，关机无法执行时触发
AT NOPARENT * EXECUTE NOPARENT
```

3. 需要注意的是 `AT` 语句应处于前三项以后，且 PIPEFN 及 LOCKFN 中的文件 NUT 应有读取写入及操作的权限。
4. 如果语句顺序错误则会产生如下报错：

```shell
PIPEFN must be set before any ATs in the config file!
```

5. 如果 PIPEFN 及 LOCKFN 文件的权限不正确则会产生如下报错：

```shell
Failed to connect to parent and failed to create parent: No such file or directory
```

6. 启动服务：

```shell
/sbin/upsmon
```

7. 如果报错，看看上面【设置电池低电量自动关机】有没有配置
8. 同时配置允许 `nut` 用户可以在无密码的情况下执行 `/sbin/shutdown` 命令：
9. 使用 `visudo` 命令编辑 `/etc/sudoers` 文件，以避免语法错误

```shell
visudo
```

10. 添加一行配置，允许特定用户 `nut` 无密码运行 `shutdown` 关机命令

```shell
# 允许 nut 用户执行关机命令时无需输入密码
nut ALL=(ALL) NOPASSWD: /sbin/shutdown
```

##### （4）、编写脚本

1. 上面定义的执行脚本是：`/usr/local/bin/upssched`，所以我们要创建该脚本，同时注意该脚本所属的用户，避免权限上的出错

```shell
nano /usr/local/bin/upssched
```

2. 在脚本中写入以下内容；类似的，还可以通过编写脚本的方式进行其他操作：

```shell
#! /bin/sh

# 定日志文件路径，用于记录 UPS 电源状态变化
path_log="/usr/local/bin/SANTAK-TGBOX-850-NUT.log"

# 定义方法，用于记录日志
sava_log() {
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】 - $1" >> $path_log
}
# 定义方法，用于发送邮件通知
send_mail() {
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】 - $1" | mail -s "$2" -r yan@yue-hai.top 770717410@qq.com
}


# 当 UPS 电源状态发生变化时，upssched 脚本会被调用
case $1 in
    # 当接收到 on-battery 参数时，表示电源已变为 ONBATT 状态，此时 UPS 转为电池供电
    # 此时服务器将记录日志并发送邮件通知
    power-off)
        # 记录日志
        sava_log "ups 供电已中断，5 分钟后若还没有恢复，则关机"
        # 发送邮件通知
        send_mail "ups 供电已中断，5 分钟后若还没有恢复，则关机" "ups 供电已中断"
        # 延迟 5 分钟后关机；也就是说在断电后 5 分钟内 UPS 未恢复供电，服务器将关机
        sudo /sbin/shutdown -h +5 "由于 UPS 断电，系统将在 5 分钟内关闭"
    ;;
    # 当接收到 power-on 参数时，表示电源已变为 ONLINE 状态，此时 UPS 转为市电供电
    # 服务器将记录日志并发送邮件通知
    power-on)
        # 记录日志
        sava_log "ups 供电已恢复"
        # 发送邮件通知
        send_mail "ups 供电已恢复" "ups 供电已恢复"
        # 电源恢复后，取消关机计划；也就是说只要 UPS 在断电后 5 分钟内恢复供电，服务器将取消关机计划
        sudo /sbin/shutdown -c
    ;;
    # 表示 UPS 电池电量低时触发的事件
    LOWBATT)
        # 记录日志
        sava_log "ups 电池电量低于 20%，立即关机"
        # 发送邮件通知
        send_mail "ups 电池电量低于 20%，立即关机" "ups 电池电量低"
        # 立即关机
        sudo /sbin/shutdown -h now "由于 UPS 电池电量低，系统将立即关闭"
    ;;
    # 表示 UPS 电池需要更换时触发
    REPLBATT)
        # 记录日志
        sava_log "ups 电池需要更换"
        # 发送邮件通知
        send_mail "ups 电池需要更换" "ups 电池需要更换"
    ;;

    # 表示与 UPS 的通信已建立时触发
    COMMOK)
        # 记录日志
        sava_log "ups 通信已建立"
        # 发送邮件通知
        send_mail "ups 通信已建立" "ups 通信已建立"
    ;;
    # 表示与 UPS 的通信已丢失时触发
    COMMBAD)
        # 记录日志
        sava_log "ups 通信已丢失"
        # 发送邮件通知
        send_mail "ups 通信已丢失" "ups 通信已丢失"
    ;;

    # 表示由主控触发的强制关机时触发
    FSD)
        # 记录日志
        sava_log "ups 主控触发强制关机"
    ;;
    # 表示系统正在关机时触发
    SHUTDOWN)
        # 记录日志
        sava_log "ups 正在关机"
    ;;
    # 表示无法联系到 UPS 进行监控时触发
    NOCOMM)
        # 记录日志
        sava_log "无法联系到 ups 进行监控"
    ;;
    # 表示负责关机的进程已死亡，关机无法执行时触发
    NOPARENT)
        # 记录日志
        sava_log "关机进程已死亡"
    ;;

    # 当接收到未知参数时，记录日志
    *)
        sava_log "未知参数：$1"
    ;;
esac

# 在日志文件中写入换行符，用于分隔不同时间点的记录
echo "" >> $path_log
```

3. 创建日志文件

```shell
touch /usr/local/bin/SANTAK-TGBOX-850-NUT.log
```

4. 设置日志文件的权限，允许所有人进行读写

```shell
chmod 666 /usr/local/bin/SANTAK-TGBOX-850-NUT.log
```

5. 将日志文件软连接到其他地方，以便于查看：

```shell
# 登录 yan 用户
su yan

# 将文件 /usr/local/bin/SANTAK-TGBOX-850-NUT.log 软连接到 目录 ~/apply/tools/SANTAK-TGBOX-850/ 下
ln -s /usr/local/bin/SANTAK-TGBOX-850-NUT.log ~/apply/tools/SANTAK-TGBOX-850/
```

#### Ⅴ、文件的简单解释

##### （1）、upsmon.conf

> 这是 Network UPS Tools (NUT) 的 upsmon.conf 配置文件示例，路径：/etc/nut/upsmon.conf
> 
> 用于设置如何监控不间断电源系统（UPS）以及在不同电源状态下如何响应。
> 
> 配置文件中包含了用户和密码的信息，因此需要保证其安全。

- 主要配置项：

| 配置项           | 介绍                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| RUN_AS_USER   | 指定 upsmon 运行的非特权用户，通常在编译时通过 `--with-user=...` 设置，默认可以用 `-u <user>` 进行覆盖。<br>这个用户应该没有写权限到 `upsmon.conf` 以防止潜在的攻击。                           |
| MONITOR       | 定义要监控的 UPS 系统<br>格式为 `<upsname>@<hostname>[:<port>]`，例如 `tg-box-850@localhost` 或 `su700@mybox`<br>`<powervalue>` 是一个整数，表示 UPS 给该系统供电的电源数量。 |
| MINSUPPLIES   | 设置系统运行所需接收电力的最小电源数量                                                                                                                        |
| SHUTDOWNCMD   | `upsmon` 使用此命令在系统需要关闭时执行                                                                                                                   |
| NOTIFYCMD     | 用于在发生特定事件时发送通知的命令                                                                                                                          |
| POLLFREQ      | 正常情况的轮询频率                                                                                                                                  |
| POLLFREQALERT | UPS 使用电池供电时的轮询频率                                                                                                                           |
| HOSTSYNC      | 等待从属 `upsmon` 断开连接的时间                                                                                                                      |
| DEADTIME      | 在声明 UPS "死亡"前等待的时间                                                                                                                         |
| POWERDOWNFLAG | 在主系统上为强制 UPS 关机设置的标志文件                                                                                                                     |
| NOTIFYFLAG    | 定义发生特定 NOTIFY 事件时 `upsmon` 的行为。<br>例如，`ONBATT` 事件指 UPS 使用电池供电时触发，可以设置为 `SYSLOG+WALL+EXEC` 以记录日志，通知所有用户并执行 `NOTIFYCMD`。                     |

- 全部的状态：

| 状态名      | 介绍                |
| -------- | ----------------- |
| ONLINE   | UPS 恢复使用在线电力      |
| ONBATT   | UPS 正在使用电池供电      |
| LOWBATT  | UPS 电池电量低         |
| FSD      | 由主控触发的强制关机        |
| COMMOK   | 与 UPS 的通信已建立      |
| COMMBAD  | 与 UPS 的通信已丢失      |
| SHUTDOWN | 系统正在关机            |
| REPLBATT | UPS 电池需要更换        |
| NOCOMM   | 无法联系到 UPS 进行监控    |
| NOPARENT | 负责关机的进程已死亡，关机无法执行 |

##### （2）、upssched.conf

> 这是关于 Network UPS Tools (NUT) 的 upssched.conf 配置文件的示例，路径：/etc/nut/upssched.conf
> 
> 用于定义 UPS（不间断电源）调度器在不同 UPS 事件发生时如何执行特定的命令或操作。
> 
> 文件的主要内容包括脚本命令、通信文件、锁文件和事件处理等配置。

1. `CMDSCRIPT <scriptname>`
	1. 这个脚本会在定时器触发时被调用。
	2. 脚本会接收一个参数 `<timername>`，即在 `AT ... START-TIMER` 中定义的定时器名称。
	3. 必须在第一个 `AT` 语句之前定义，否则程序会报错并退出。
	4. 建议使用一个包含 `case..esac` 结构的 shell 脚本来处理不同的定时器事件。
	5. 示例定义：

```shell
CMDSCRIPT /bin/upssched-cmd
```

2. `PIPEFN <filename>`
	1. 定义一个 FIFO（先进先出队列）的文件名，该文件用于在不同进程之间传递信息，以启动和停止定时器。
	2. 文件应放置在普通用户无法创建的路径下，以防止符号链接攻击和其他恶意行为。
	3. 如果使用类似 Solaris 的操作系统，文件权限可能不足以确保安全，必须将此文件放在受保护的目录中。
	4. 默认情况下，upsmon 会以配置文件 `upsmon.conf` 中 `RUN_AS_USER` 定义的用户运行 upssched，确保该用户有权限创建和写入 PIPEFN 和 LOCKFN 指定的文件。
	5. 建议为 upssched 创建一个专用目录，由 upsmon 用户拥有，并用于 PIPEFN 和 LOCKFN 文件。
	6. 该文件将在首次接收到事件时将自动创建
	7. 示例定义（默认被注释掉）：

```shell
PIPEFN /run/nut/upssched/upssched.pipe
```

3. `LOCKFN <filename>`
	1. 必需项，用于避免同时处理两个事件时产生的竞争条件。这个文件将会短暂存在，必须不能被其他进程创建。
	2. 建议将 LOCKFN 文件放在与 PIPEFN 相同的目录中。
	3. 该文件将在首次接收到事件时将自动创建
	4. 示例定义：

```shell
LOCKFN /run/nut/upssched/upssched.lock
```

4. `AT <notifytype> <upsname> <command>`
	1. 定义特定事件 `<notifytype>` 发生在 UPS `<upsname>` 上时的处理方式。
	2. `<upsname>` 可以使用 * 通配符，表示应用于所有 UPS。
	3. 当事件发生时，通过 `CMDSCRIPT` 执行命令 <command>。
5. 可能的 AT 命令：
6. `START-TIMER <timername> <interval>`
	1. 启动一个名为 `<timername>` 的定时器，在 `<interval>` 秒后触发，并将 `<timername>` 作为第一个参数传递给 `CMDSCRIPT`。
	2. 示例：当任意 UPS（`*`）的通信断开超过 10 秒时执行：

```shell
AT COMMBAD * START-TIMER upsgone 10
```

7. `CANCEL-TIMER <timername> [cmd]`
	1. 取消名为 `<timername>` 的运行定时器，如果可能的话。
	2. 如果定时器已经触发，则将可选的 `<cmd>` 参数传递给 `CMDSCRIPT`。
	3. 示例：如果特定的 UPS（myups@localhost）重新上线，则在定时器触发前停止它：

```shell
AT COMMOK myups@localhost CANCEL-TIMER upsgone
```

8. `EXECUTE <command>`
	1. 立即将 `<command>` 作为参数传递给 `CMDSCRIPT`。
	2. 示例：如果任意 UPS 恢复到市电电源，则通过 CMDSCRIPT 执行 ups-back-on-line：

```shell
AT ONLINE * EXECUTE ups-back-on-line
```

### ⑦、smartmontools 硬盘检测

> 1. smartmontools 是一组工具，用于监控和管理硬盘驱动器和固态硬盘的健康状况，主要包含两个工具：smartctl 和 smartd
> 2. 它们帮助用户通过 SMART（Self-Monitoring, Analysis, and Reporting Technology）获取硬盘信息，检测潜在问题，防止数据丢失

##### （1）、smartmontools 的主要功能

1. 硬盘健康状况监控：获取硬盘的健康状态、SMART 属性、错误日志等。
2. 执行自检测试：运行短期或长期自检来评估硬盘是否存在潜在故障。
3. 错误日志查看：检查硬盘的错误历史记录，查看是否有错误发生。
4. 自动监控服务：使用 smartd 作为后台服务，定期监控硬盘健康状况并发送通知。
5. 温度监控：查看和监控硬盘温度，预防温度过高造成的硬盘损坏。
6. 支持多种接口：支持 IDE/ATA、SATA、SCSI、NVMe、USB、RAID 等不同接口的存储设备。

##### （2）、smartctl 命令

> smartctl 是用于与硬盘交互的命令行工具，常用来获取和显示硬盘的 SMART 信息。

1. 查看设备列表：会以树状结构显示所有块设备（包括硬盘和分区）的信息：

```shell
lsblk
```

2. 查看设备信息，显示设备的基本信息（如型号、序列号、容量等）：

```shell
sudo smartctl -i /dev/sdX
```

3. 查看 SMART 健康状态，检查硬盘的健康状态，返回 PASSED 或 FAILED：

```shell
sudo smartctl -H /dev/sdX
```

4. 显示详细 SMART 信息，显示完整的 SMART 信息，包括属性、错误日志、自检状态等：

```shell
sudo smartctl -a /dev/sdX
```

5. 运行短测试，启动短测试，检查基本健康状况：

```shell
sudo smartctl -t short /dev/sdX
```

6. 运行长测试，运行详细的自检，检查整个硬盘是否存在问题：

```shell
sudo smartctl -t long /dev/sdX
```

7. 查看自检日志，显示所有已完成的自检测试结果：

```shell
sudo smartctl -l selftest /dev/sdX
```

8. 查看错误日志，查看硬盘的错误历史记录。：

```shell
sudo smartctl -l error /dev/sdX
```

9. 启用或禁用 SMART：

```shell
# 启用 SMART 功能
sudo smartctl -s on /dev/sdX

# 禁用 SMART 功能
sudo smartctl -s off /dev/sdX
```

10. 取消正在进行的自检：

```shell
sudo smartctl -X /dev/sdX
```

##### （3）、smartd 命令

> smartd 是 smartmontools 的守护进程，用于定期检查硬盘的健康状况，并根据需要发出警报或执行其他动作。

1. 启动 smartd：smartd 会通过配置文件自动监控指定硬盘。默认配置文件路径是 `/etc/smartd.conf`
2. 配置文件示例：在 `/etc/smartd.conf` 中，可以指定要监控的设备及其参数，例如：

```shell
# 这条指令表示对 /dev/sda 启用 SMART，开启自动保存和自检，并每天定时运行测试。
/dev/sda -a -o on -S on -s (S/../.././02|L/../../6/03)
```

3. 常用 smartd 配置选项：
	1. `-a`：显示所有 SMART 信息
	2. `-o on/off`：启用或禁用自动离线数据收集
	3. `-s`：指定定时自检计划
	4. `-m EMAIL`：当发现问题时发送电子邮件通知

##### （4）、smartmontools 其他常用命令

1. 查看设备是否支持 SMART，显示设备的 SMART 功能支持情况：

```shell
sudo smartctl -c /dev/sdX
```

2. 查看硬盘的温度和其他重要属性：

```shell
sudo smartctl -A /dev/sdX
```

3. 测试配置文件，检查 smartd 的配置文件是否正确：

```shell
sudo smartd -q onecheck
```

##### （5）、提示未知 USB 桥接器 Unknown USB bridge

> 1. 我使用的硬盘柜是 Yottamaster 尤达大师的五盘位硬盘柜，只有硬盘柜的功能，没有  raid
> 2. 使用 `-d sat` 参数可以正常识别

1. 如果硬盘不是直连的电脑，而是通过硬盘柜等设备连接的硬盘，可能会出现此提示

```shell
yan@yan:~/apply/file/FreeFileSync/sava$ sudo smartctl -a /dev/sda
smartctl 7.2 2020-12-30 r5155 [x86_64-linux-6.2.0-26-generic] (local build)
Copyright (C) 2002-20, Bruce Allen, Christian Franke, www.smartmontools.org

/dev/sda: Unknown USB bridge [0x125f:0xa578 (0x1324)]
Please specify device type with the -d option.

Use smartctl -h to get a usage summary

yan@yan:~/apply/file/FreeFileSync/sava$ 
```

2. 原因：因为许多硬盘柜使用的 USB-SATA 桥接芯片并不完全支持 SMART 协议，这可能导致 smartctl 无法直接检测硬盘的 SMART 状态
3. 解决方法：当通过 USB 硬盘柜连接时，可以尝试使用 -d 参数指定设备类型，这有助于 smartctl 识别桥接芯片并访问硬盘的 SMART 信息。
4. 以下是几种常见的 -d 选项，可以逐一尝试：
5. 许多 USB 硬盘柜支持 `sat` 设备类型：

```shell
sudo smartctl -d sat -a /dev/sda
```

6. 如果硬盘柜使用的是 JMicron 的桥接芯片（常见于一些 USB-SATA 转换器），可以使用 `usbjmicron` 类型：

```shell
sudo smartctl -d usbjmicron -a /dev/sda
```

7. 如果硬盘柜是基于 Sunplus 的桥接芯片，可以使用 usbsunplus 类型：

```shell
sudo smartctl -d usbsunplus -a /dev/sda
```

8. 尝试自动检测，`auto` 选项让 smartctl 自动识别设备类型，可能会解决桥接识别问题：

```shell
sudo smartctl -d auto -a /dev/sda
```

##### （6）、开启 SMART 功能

> 1. 机械硬盘的 SMART（Self-Monitoring, Analysis, and Reporting Technology）功能是一种自我监控和报告技术，用于检测和报告硬盘的健康状态
> 2. SMART 旨在通过监控硬盘内部的多个关键参数，帮助用户及系统预测和预防潜在的硬盘故障，从而减少数据丢失的风险。
> 3. 某些磁盘类型（如 SCSI、SAS 磁盘）或者某些 RAID 阵列可能不完全支持 smartctl 的 SMART 命令，特别是在企业级硬盘上。
> 4. 例如，SCSI 驱动器的 SMART 功能可能需要特殊的支持，而常见的 smartctl 工具并不总能完全兼容。
> 5. 除此之外，有的企业级硬盘（或者硬盘柜）默认是没有开启 SMART 功能的，这里尝试开启

1. 开启 SMART 功能：

```shell
sudo smartctl -s on /dev/sda
```

2. 如果提示未知 USB 桥接器 Unknown USB bridge，请看上一节

```shell
# 指定设备类型，使用 -d 参数
sudo smartctl -d sat -s on /dev/sda

# 使用 -scsi 参数等
sudo smartctl -d scsi -s on /dev/sda
```

3. 有时候，虽然设备不完全兼容，但 `smartctl` 可以在 **宽容模式** 下执行部分 SMART 命令。添加 `-T permissive` 选项可以忽略非关键的错误并继续操

```shell
sudo smartctl -T permissive -s on /dev/sda
```

4. 如果以上方法仍然不起作用，可能表明该硬盘不支持 smartctl 或需要专用的厂商工具。
5. HGST 硬盘通常可以使用 Western Digital 的诊断工具进行检测，可以尝试从 HGST 或 Western Digital 官方网站下载相应的工

### ⑧、

### ⑨、

# 八、命令使用

## 1、nano 和 vim

1. 在新安装的 Ubuntu 桌面中，`nano` 是自带的简单易用的文本编辑器，和 `vim` 类似
2. 它提供了基本的编辑功能和快捷键，如复制、粘贴、查找和替换等。可以通过以下命令来打开文件并使用 `nano` 编辑器：

```shell
nano 文件名
```

3. 在`nano`中，底部会显示一些常用的命令提示，例如，使用 `Ctrl + O` 保存文件，使用 `Ctrl + X` 退出编辑器。
4. 以下是 `nano` 文本编辑器中常用的一些快捷键：

| 快捷键   | 介绍                                                                        |
| -------- | --------------------------------------------------------------------------- |
| Ctrl + G | 显示帮助菜单，其中包含所有可用的快捷键和命令。                              |
| Ctrl + O | 保存文件并退出，按下后会提示你输入文件名，按下Enter确认保存。               |
| Ctrl + S | 保存文件。                                                                  |
| Ctrl + X | 退出编辑器，如果有未保存的更改，会提示你是否保存。                          |
| Ctrl + K | 剪切当前行。                                                                |
| Ctrl + U | 粘贴剪切的内容到当前位置。                                                  |
| Ctrl + W | 查找关键词，按下后会提示你输入要查找的关键词，按下Enter开始查找。           |
| Ctrl + \ | 替换关键词，按下后会提示你输入要替换的关键词和替换内容，按下Enter开始替换。 |
| Ctrl + C | 显示光标所在位置的行号和列号。                                              |
| Ctrl + J | 将光标移动到当前行的结尾。                                                  |
| Ctrl + A | 将光标移动到当前行的开头。                                                  |
| Ctrl + E | 将光标向下移动一行。                                                        |
| Ctrl + Y | 将光标向上移动一行。                                                        |
| Ctrl + V | 向下滚动一屏。                                                              |
| Ctrl + Y | 向上滚动一屏。                                                              |

## 2、`screen` 多重视窗管理程序

### ①、介绍

1. `GNU Screen` 简称 `Screen` 或 `screen`，源自 GNU 计划，其官网：[GNU Screen](https://www.gnu.org/software/screen/)。
2. 初始版本早在1987年就发布，目前的最新稳定版本是：4.8.0（2020年2月5日）。所以，你现在使用的 screen 命令，其实三十年前就有人在使用了。
3. screen的功能大体有三个：
4. 会话恢复：只要 `screen` 本身没有终止，在其内部运行的会话都可以恢复。
	1. 这一点对于远程登录的用户特别有用：即使网络连接中断，用户也不会失去对已经打开的命令行会话的控制。只要再次登录到主机上执行 `screen -r `就可以恢复会话的运行。
	2. 同样在暂时离开的时候，也可以执行分离命令 `detach`，在保证里面的程序正常运行的情况下让 `screen` 挂起（切换到后台）。
5. 多窗口：在 `screen` 环境下，所有的会话都独立的运行，并拥有各自的编号、输入、输出和窗口缓存。用户可以通过快捷键在不同的窗口下切换，并可以自由的重定向各个窗口的输入和输出。
6. 会话共享：`screen` 可以让一个或多个用户从不同终端多次登录一个会话，并共享会话的所有特性（比如可以看到完全相同的输出）。它同时提供了窗口访问权限的机制，可以对窗口进行密码保护。

### ②、安装 `screen`

1. 更新软件源

```shell
sudo apt update
```

2. 安装 screen

```shell
# CentOS
yum install screen

# Debian/Ubuntu
apt install screen
```

### ③、状态介绍

1. 通常情况下，screen 创建的虚拟终端，有两个工作模式：
	1. `Attached`：表示当前 `screen` 正在作为主终端使用，为活跃状态。
	2. `Detached`：表示当前 `screen` 正在后台使用，为非激发状态。

```shell
steam@yan:~$ screen -ls
There are screens on:
        58311.PalWorld-2        (2024年01月29日 19时46分37秒)   (Attached)
        41007.PalWorld  (2024年01月25日 19时07分23秒)   (Attached)
        30419.tmodloader        (2024年01月21日 15时36分14秒)   (Detached)
        16466.7DaysServer       (2024年01月19日 21时37分45秒)   (Detached)
4 Sockets in /run/screen/S-steam.
steam@yan:~$ 
```

2. 通常情况下，不需要关注上面的状态。

### ④、基础命令

#### Ⅰ、帮助查询

1. screen 的帮助文档实在是过于详细，以至于查个命令，可能要查几分钟
2. 但是你可以直接使用帮助命令，查询自己需要的命令:

```shell
# 查询 screen 提示
screen -help
```

3. 通过这个命令，可以查询到大部常用命令。

```shell
steam@yan:~$ screen -help
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]

Options:
-4            Resolve hostnames only to IPv4 addresses.
-6            Resolve hostnames only to IPv6 addresses.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-l            Login mode on (update /var/run/utmp), -ln = off.
-ls [match]   or
-list         Do nothing, just list our SockDir [on possible matches].
-L            Turn on output logging.
-Logfile file Set logfile name.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-Q            Commands will send the response to the stdout of the querying process.
-r [session]  Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 4.09.00 (GNU) 30-Jan-22".
-wipe [match] Do nothing, just clean up SockDir [on possible matches].
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
steam@yan:~$ 
```

#### Ⅱ、终端列表

1. 怎么查看已经存在的 screen 终端呢？很简单，使用命令：

```shell
screen -ls
```

2. 即可查看已经创建（在后台运行的终端）：

```shell
steam@yan:~$ screen -ls
There are screens on:
        58311.PalWorld-2        (2024年01月29日 19时46分37秒)   (Detached)
        41007.PalWorld  (2024年01月25日 19时07分23秒)   (Detached)
        30419.tmodloader        (2024年01月21日 15时36分14秒)   (Detached)
        16466.7DaysServer       (2024年01月19日 21时37分45秒)   (Detached)
4 Sockets in /run/screen/S-steam.
steam@yan:~$
```

3. 如果你之前没有创建，那么是为空的：

```shell
yan@yan:~$ screen -ls
No Sockets found in /run/screen/S-yan.

yan@yan:~$ 
```

#### Ⅲ、新建终端

1. 新建终端有三种方式：
	1. 输入 `screen` 回车，即可新建一个虚拟终端，但是这样的名称太乱
	2. 使用参数 `-S` 创建：`screen -S Hello`
	3. 使用参数 `-R` 创建：`screen -R Hello`
2. 三种创建方法比较：
	1. 使用 `-S` 创建和直接输入 `screen` 创建的虚拟终端，不会检录之前创建的 `screen`，也就是会创建同名的 `screen`
	2. 使用 `-R` 创建，如果之前有创建唯一一个同名的 `screen`，则直接进入之前创建的 `screen`
3. 创建好虚拟终端后，会新建一个空白的 Terminal，这个就是新的虚拟终端了
4. 运行你的程序，按 `Ctril + a`，再按 `d`，即可保持这个 `screen` 到后台并回到主终端

#### Ⅳ、回到 `screen` 终端

1. 在主终端使用 `-R` 或者 `-r` 命令即可：

```shell
# 使用 screen -r 命令
screen -r [pid/name]
```

2. 其中：`pid/name`：为虚拟终端 PID 或 Name，可使用 `screen -ls` 查看；下面 `58311.PalWorld-2` 即为 `pid.name`

```shell
steam@yan:~$ screen -ls
There are screens on:
        58311.PalWorld-2        (2024年01月29日 19时46分37秒)   (Detached)
        41007.PalWorld  (2024年01月25日 19时07分23秒)   (Detached)
        30419.tmodloader        (2024年01月21日 15时36分14秒)   (Detached)
        16466.7DaysServer       (2024年01月19日 21时37分45秒)   (Detached)
4 Sockets in /run/screen/S-steam.
steam@yan:~$
```

3. 如果使用大写 的 `-R`，和 `-r` 类似，但是没有对应名称的 PID 或者 Name 时，会自动创建新的虚拟终端。

#### Ⅴ、清除终端

1. 有时候，我们的进程已经“守护”完毕，不需要这个虚拟终端了，也就是需要释放资源，如何操作呢？
2. 比较推荐的方法，是进入对应虚拟终端，然后输入：

```shell
# 退出终端
exit
```

3. 之后，就会回到主终端
4. 当然，如果确定 screen 中的程序已经停止运行了，也可以在主终端内，使用命令释放：

```shell
# 使用-R/-r/-S均可
screen -S [pid/Name] -X quit
```

#### Ⅵ、不进入 `screen` 终端的情况下执行命令

1. 使用 `stuff` 指令向指定 `screen` 终端发送字符：

```shell
#!/bin/bash

# screen 会话名称，每个会话中可能有多个窗口
screen_name="PalWorld-2"
# 脚本所在路径
path="/home/steam/game/PalServer"

# 模拟按下 Ctrl + C 组合键，防止服务器正在运行；等待 10 秒
# -x：附加到指定的会话。
# -S $screen_name：指定要操作的会话名称。
# -p 0：选择会话中的窗口编号，这里是选择窗口编号为 0 的窗口。
# -X stuff：在选定的窗口中发送字符。
screen -x -S $screen_name -p 0 -X stuff $'\x03'
sleep 10
screen -x -S $screen_name -p 0 -X stuff $'\x03'
sleep 5

# 发送启动 PalServer 命令，包括运行参数，将命令发送到会话中，并模拟按下回车键。同时等待 20 秒，确保 PalServer 启动完成
screen -x -S $screen_name -p 0 -X stuff "$path/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDSD\r"
sleep 20

# 分离会话，模拟按下 Ctrl + C + D 组合键；等待 2 秒
screen -x -S $screen_name -p 0 -X stuff $'\x01'
screen -x -S $screen_name -p 0 -X stuff "D"
sleep 2

# 向 yuehai_server.log 文件中追加日志
echo "$(date)：帕鲁服务器 1 已启动" >> $path/yuehai_server.log
```

2. 具体参数的含义如下：
	1. `-x`：附加到指定的会话。
	2. `-S $screen_name`：指定要操作的会话名称。
	3. `-p 0`：选择会话中的窗口编号，这里是选择窗口编号为 0 的窗口；可以不加，默认选择会话的第一个窗口
	4. `-X stuff`：在选定的窗口中发送字符。

## 3、使用 sftp 命令从 linux 服务器下载文件

### ①、sftp 介绍

1. SFTP（SSH File Transfer Protocol）是一种安全的文件传输协议，它在 SSH 协议的基础上提供文件访问、文件传输和文件管理功能
2. 与 FTP 相比，SFTP 提供了加密的网络通信，保证数据在传输过程中的安全性

### ②、启动一个 SFTP 会话

```shell
sftp -oPort=端口号 username@hostname
```

1. `username` 是远程服务器上的用户名
2. `hostname` 是服务器的地址
3. 默认使用 ssh 的端口号，即 `22`；如果服务器使用了非标凈端口，可以使用 `-oPort=端口号` 来指定
4. 回车后会要求输入密码
5. 退出 SFTP 会话：`exit` 或 `quit`

```shell
exit
```

### ③、常用指令

#### Ⅰ、控制远程文件指令

1. `pwd`：查看当前所在的远程目录路径

```shell
sftp> pwd
Remote working directory: /home/yan/桌面

sftp> 
```

2. `ls` 或 `dir`：列出远程目录的内容。

```shell
sftp> ls
 \214Wk\250U                               100%   24MB  21.6KB/s   19:09    
IDE                      Idea                     aiXcoder                 
apply                    authlib-injector.log     output.pcap              
snap                     下载                   公共的                
图片                   文档                   桌面                   
模板                   视频                   音乐                   
sftp>
```

3. `cd`：改变远程目录。

```shell
sftp> cd 桌面
\300\306Wk\250U                              0%    0   -101.-1KB/s   -4:-5 E

sftp> pwd
Remote working directory: /home/yan/桌面

sftp> 
```

4. `mkdir`：在远程服务器上创建目录。

```shell
mkdir directory_name
```

5. `rmdir`：删除远程服务器上的目录。

```shell
rmdir directory_name
```

6. `rm`：删除远程服务器上的文件。

```shell
rm file_name
```

7. `chmod`：改变远程文件或目录的权限。

```shell
chmod 0755 file_name
```

#### Ⅱ、控制本地文件指令

1. `lpwd`：查看当前所在的本地目录路径

```shell
sftp> lpwd
Local working directory: /home/yan/apply

sftp> 
```

2. `lls`：列出本地目录的内容。

```shell
sftp> lls
n2n  n2n-edge-query  n2n-edge-query-check  v2ray
sftp> 
```

3. `lcd`：改变本地目录；下载时默认下载的目录

```shell
sftp> lcd ~/download

sftp> lpwd
Local working directory: /home/yan/download

sftp> 
```

#### Ⅲ、下载上传文件指令

1. `get`：下载文件：从远程机器到本地机器
	1. 如果未指定本地文件名，文件将以远程文件同名保存到当前本地目录
	2. 若是下载的文件路径中含有空格，需用引号包裹起来

```shell
get "/home/yan/桌面/音乐/【纯音乐】/墨明棋妙 - 皓水莫负.flac" [local-file]
```

2. `put`：上传文件：从本地机器到远程机器
	1. 如果未指定远程文件名，文件将以本地文件同名保存到当前远程目录。
	2. 若是上传的文件路径中含有空格，需用引号包裹起来

```shell
put "墨明棋妙 - 皓水莫负.flac" [remote-file]
```

3. `mget`：下载多个文件。

```shell
# 下载当前目录下的所有 flac 文件
mget *.flac

# 下载指定目录下的所有文件
mget /home/yan/桌面/音乐/【纯音乐】/*
```

4. `mput`：上传多个文件。

```shell
# 上传当前目录下的所有文件
mput *

# 上传指定目录下的所有 flac 文件
mput /home/yan/桌面/音乐/【纯音乐】/*.flac
```

## 4、实时进程监控工具 top

### ①、启动 `top`

1. 只需在终端中输入 `top`，按 Enter 键即可启动

### ②、输出信息介绍

#### Ⅰ、例子

```shell
yan@yan:~/apply/tools/yuehai-tool$ top
top - 08:40:54 up 14:54,  2 users,  load average: 0.01, 0.04, 0.04
任务: 377 total,   1 running, 376 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  4.5/29811.0  [|||                                                                           ]
MiB Swap:  0.0/2048.0   [                                                                              ]

 进程号 USER      PR  NI    VIRT    RES    SHR    %CPU  %MEM     TIME+ COMMAND                           
    851 root      20   0 2170060  44432  31232 S   0.7   0.1   2:22.64 containerd                        
  11658 yan       20   0   22076   4352   3328 R   0.3   0.0   0:01.29 top                               
      1 root      20   0  166956  11644   8188 S   0.0   0.0   0:31.43 systemd                           
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.03 kthreadd                          
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                            
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                        
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 slub_flushwq                      
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns                             
      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-events_highpri       
     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq                      
     11 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_kthread                 
     12 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_rude_kthread            
     13 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_trace_kthread           
     14 root      20   0       0      0      0 S   0.0   0.0   0:00.47 ksoftirqd/0                       
     15 root      20   0       0      0      0 I   0.0   0.0   0:15.45 rcu_preempt                       
     16 root      rt   0       0      0      0 S   0.0   0.0   0:00.30 migration/0                       
     17 root     -51   0       0      0      0 S   0.0   0.0   0:00.00 idle_inject/0                     
     19 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/0                           
     20 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/1                           
     21 root     -51   0       0      0      0 S   0.0   0.0   0:00.00 idle_inject/1                     
     22 root      rt   0       0      0      0 S   0.0   0.0   0:00.55 migration/1                       
     23 root      20   0       0      0      0 S   0.0   0.0   0:00.07 ksoftirqd/1                       
     25 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/1:0H-events_highpri       
     26 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/2                           
     27 root     -51   0       0      0      0 S   0.0   0.0   0:00.00 idle_inject/2                     
     28 root      rt   0       0      0      0 S   0.0   0.0   0:00.50 migration/2                       
     29 root      20   0       0      0      0 S   0.0   0.0   0:01.15 ksoftirqd/2                       
     31 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/2:0H-events_highpri       
     32 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/3                           
```

#### Ⅱ、top 命令的输出头部

```shell
top - 08:40:54 up 14:54,  2 users,  load average: 0.01, 0.04, 0.04
```

1. `08:40:54 up 14:54`：这表示系统在 08:40:54 运行了 top 命令，且系统已运行了 14 小时 54 分钟
2. `2 users`：系统上有 2 个用户登录
3. `load average: 0.01, 0.04, 0.04`：这些数字分别代表过去 1 分钟、5 分钟和 15 分钟的平均负载。负载平均值越低，表明系统越空闲

#### Ⅲ、任务（任务）

```shell
任务: 377 total,   1 running, 376 sleeping,   0 stopped,   0 zombie
```

1. `377 total`：系统总共有 377 个进程
2. `1 running`：有 1 个进程正在运行
3. `376 sleeping`：有 376 个进程处于休眠状态
4. `0 stopped`：没有进程被停止
5. `0 zombie`：没有僵尸进程

#### Ⅳ、CPU 使用情况（%Cpu(s)）

```shell
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
```

1. `0.0 us`：用户空间占用的 CPU 百分比
2. `0.0 sy`：内核空间占用的 CPU 百分比
3. `0.0 ni`：改变过优先级的进程占用的 CPU 百分比
4. `99.9 id`：空闲的 CPU 百分比
5. `0.0 wa`：等待输入输出的 CPU 百分比
6. `0.0 hi`：处理硬件中断的 CPU 百分比
7. `0.0 si`：处理软件中断的 CPU 百分比
8. `0.0 st`：被偷走的时间（在虚拟环境中被用于服务其他虚拟机的时间）

#### Ⅴ、内存使用情况

```shell
MiB Mem :  4.5/29811.0  [|||                                                                           ]
MiB Swap:  0.0/2048.0   [                                                                              ]
```

1. `MiB Mem : 4.5/29811.0`：从总共 29811 MiB 内存中，有 4.5 MiB 正在使用
2. `MiB Swap: 0.0/2048.0`：从总共 2048 MiB 交换空间中，有 0.0 MiB 正在使用

#### Ⅵ、进程列表

```shell
 进程号 USER      PR  NI    VIRT    RES    SHR    %CPU  %MEM     TIME+ COMMAND                           
    851 root      20   0 2170060  44432  31232 S   0.7   0.1   2:22.64 containerd                        
  11658 yan       20   0   22076   4352   3328 R   0.3   0.0   0:01.29 top                               
      1 root      20   0  166956  11644   8188 S   0.0   0.0   0:31.43 systemd                           
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.03 kthreadd   
```

1. `进程号`：进程的唯一标识符
2. `USER`：运行该进程的用户
3. `PR`：进程优先级
4. `NI`：进程的 nice 值，影响进程的优先级
5. `VIRT`：进程使用的虚拟内存总量
6. `RES`：进程使用的、未被换出的物理内存大小
7. `SHR`：共享内存大小
8. `%CPU`：进程占用的 CPU 百分比
9. `%MEM`：进程占用的内存百分比
10. `TIME+`：进程使用 CPU 的总时间
11. `COMMAND`：正在执行的命令名称
12. 示例进程：
	1. containerd 容器运行时，使用了 0.7% 的 CPU 和 0.1% 的内存
	2. top: top 命令本身，占用 0.3% 的 CPU

### ③、排序进程

1. 在 `top` 界面中，可以按特定的列进行排序，如 CPU 使用率或内存使用：
2. 按 `%CPU` 排序：按 `P`，即 `Ctrl + p`
3. 按内存使用排序：按 `M`，即 `Ctrl + m`

### ④、杀死进程

1. 如果需要结束某个进程，可以在 `top` 中直接操作：
2. 按 `k`，然后输入想要结束的进程的 PID（进程ID），并确认。

### ⑤、搜索进程

1. 可以通过进程名搜索特定进程：
2. 按 `o`（小写字母 O），然后输入 `COMMAND=<进程名>`，如 `COMMAND=bash`

### ⑥、改变更新间隔

1. 默认情况下，`top` 每几秒更新一次数据，可以调整这个间隔：
2. 在运行 `top` 时，可以按 `d`，然后输入想要的更新频率（秒数）。

### ⑦、显示或隐藏特定列

1. `top` 可以定制显示或隐藏的信息：
2. 按 `f` 进入字段管理界面，使用方向键选择要显示或隐藏的字段，按 `d` 或 `s` 来选择。

### ⑧、切换显示模式

1. 可以在不同的显示模式之间切换，以便更好地查看信息：
2. 按 `1` 可以查看每个 CPU 的详细利用率。
3. 按 `V` （即 `Ctrl + v`）可以按树状结构显示进程。

### ⑨、退出 `top`

1. 简单地按 `q`（退出键）即可退出 `top` 界面。

## 5、套接字信息检索工具 `ss`

> ss (socket statistics) 命令是一个非常强大的工具，用于检索有关 Linux 中的套接字的信息。
> 
> 它可以显示类似于 netstat 的信息，但比 netstat 更快，因为它直接从内核空间获取数据，而不需要读取和解析 /proc 目录

### ①、基本选项

1. - `-t`：显示 TCP 套接字
2. `-u`：显示 UDP 套接字
3. `-l`：显示处于监听状态的套接字
4. `-a`：显示所有套接字（默认只显示已建立的连接）
5. `-n`：以数字形式显示地址和端口号，不尝试解析域名、服务等
6. `-p`：显示使用套接字的进程 ID 和程序名称
7. `-s`：输出套接字使用概况统计。

### ②、高级选项

1. `-e`：显示扩展信息，这包括时间戳、内存、selinux 等
2. `-m`：显示套接字的内存使用情况
3. `-o`：显示计时器信息
4. `-4`：仅显示 IPv4 的套接字
5. `-6`：仅显示 IPv6 的套接字
6. `-d`：仅显示处于断开状态的套接字

### ③、过滤和查询

> `ss` 命令也支持使用过滤表达式来查询特定的连接或套接字。例如：

1. 显示所有到达或从指定 IP 发出的 TCP 连接：

```bash
ss state all dport = :http
```

2. 显示所有监听端口和对应进程：

```bash
ss -ltup
```

3. 显示所有与特定远程地址和端口建立的连接：
```bash
ss dst 192.168.1.1:ssh
```

### ④、使用实例

1. 列出所有活动的 TCP 连接：

```bash
ss -t -a
```

2. 查找使用特定端口的应用：

```bash
ss -ltnp | grep ':80'
```

3. 显示特定网络接口的统计数据：

```bash
ss -i src 192.168.1.5
```

4. 列出所有监听的套接字以及它们的进程名：

```bash
ss -ltup
```

5. 筛选出所有与端口 10000 相关的 TCP 连接，并显示相关信息，如使用该端口的进程和连接的 IP 地址

```shell
ss -ntp | grep 10000
```

## 6、处理压缩文件和目录常用的命令

### ①、tar 命令

1. tar（tape archive）命令是用于创建、维护、修改以及提取文件的工具，它可以处理 `.tar` 文件（归档），并且可以与 gzip 或 bzip2 等压缩程序结合使用来创建 `.tar.gz` 或 `.tar.bz2` 文件。
2. 常用参数：
	1. `-c`：创建一个新的归档文件。
	2. `-x`：从归档文件中提取文件。
	3. `-v`：显示操作过程（verbose模式）。
	4. `-f`：指定归档文件的名称。
	5. `-z`：使用 gzip 压缩或解压。
	6. `-j`：使用 bzip2 压缩或解压。
	7. `-t`：列出归档内容而不解压。
	8. `-C`：在解压时切换到指定目录。
3. 示例：
4. 创建归档文件：

```shell
tar -cvf 归档文件名.tar 想要打包的目录或文件名/
```

5. 创建并 gzip 压缩：

```shell
tar -czvf 归档文件名.tar.gz 想要打包的目录或文件名/
```

6. 解压 tar 文件：

```shell
tar -xvf 归档文件名.tar 想要提取的目录或文件名/
```

7. 解压并 gzip 解压：

```shell
tar -xzvf 归档文件名.tar.gz 想要提取的目录或文件名/
```

### ②、gzip 和 gunzip 命令

1. gzip 用于压缩文件，而 gunzip 用于解压文件。
2. 常用参数：
	1. `-d`：gzip 使用此参数可以解压文件，等同于gunzip。
	2. `-k`：保留原文件。
	3. `-l`：列出压缩文件的信息。
	4. `-r`：递归处理所有文件。
3. 示例：
4. 压缩文件：

```shell
gzip filename
```

5. 解压文件：

```shell
gunzip filename.gz

# 或
gzip -d filename.gz
```

6. gzip 命令本身并不支持直接压缩目录，因为它只能压缩单个文件。如果想压缩一个目录，通常的做法是先使用 tar 命令将目录打包成一个单一的文件，然后使用 gzip 来压缩这个文件

```shell
# 打包并压缩
tar -czvf 归档文件名.tar 想要打包的目录或文件名/
```

### ③、zip 和 unzip 命令

1. zip 是另一种常用的压缩工具，用于创建 `.zip` 文件。unzip 用于解压这些文件。
2. 常用参数：
	1. `-r`：递归地将目录及其内容添加到 zip 文件中。
	2. `-l`：列出 zip 归档的内容。
	3. `-u`：更新现有的 zip 归档。
	4. `-d`：指定解压目录。
3. 示例：
4. 压缩目录：

```shell
zip -r 归档文件名.zip 想要打包的目录或文件名/
```

5. 解压文件：

```shell
unzip 归档文件名.zip -d 想要解压到的目录/
```

## 7、查看 Ubuntu 系统和内核的版本

1. 查看系统版本方式一：

```shell
lsb_release -a
```

```shell
yan@yan:~$ lsb_release -a
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
yan@yan:~$ 
```

2. 查看系统版本方式二：

```shell
cat /proc/version
```

```shell
yan@yan:~$ cat /proc/version
Linux version 6.2.0-26-generic (buildd@bos03-amd64-042) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #26~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jul 13 16:27:29 UTC 2
yan@yan:~$ 
```

3. 查看内核版本：

```shell
uname -a
```

```shell
yan@yan:~$ uname -a
Linux yan 6.2.0-26-generic #26~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jul 13 16:27:29 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
yan@yan:~$ 
```

## 8、软连接（符号链接）ln

1. 在 Linux 中，软连接（也称为符号链接或 symlink）是一种特殊的文件，它指向系统中的另一个文件或目录。
2. 软连接类似于 Windows 系统中的快捷方式。通过软连接，可以快速访问目标文件或目录，而无需关心其物理位置。
3. 为文件创建软连接；假设有一个文件 `/home/user/documents/file.txt`，并希望在桌面上创建一个软连接：
	1. 这样，桌面上会有一个 `file_symlink.txt` 文件，它实际上指向 `/home/user/documents/file.txt`

```shell
ln -s /home/user/documents/file.txt ~/Desktop/file_symlink.txt
```

4. 为目录创建软连接；假设有一个文件目录 `/home/user/documents`，并希望在桌面上创建一个软连接：
	1. 这样，桌面上会有一个 `documents_symlink` 目录，它实际上指向 `/home/user/documents`

```shell
ln -s /home/user/documents ~/Desktop/documents_symlink
```

5. 要删除软连接，可以使用 rm 命令。注意，删除软连接时不会删除目标文件或目录，只会删除链接本身

```shell
# 删除文件的软连接：
rm ~/Desktop/file_symlink.txt

#删除目录的软连接：
rm -r ~/Desktop/documents_symlink
```

6. 软连接的特点：
	1. 指向性：软连接只是指向另一个文件或目录的路径，它本身并不包含实际的数据。当你访问软连接时，系统会自动重定向到目标文件或目录。
	2. 跨文件系统：软连接可以跨文件系统工作，这意味着你可以在不同的磁盘分区或设备上创建指向文件的软连接。
	3. 权限：软连接的权限通常不会影响目标文件的权限。访问软连接时，系统会根据目标文件的权限进行判断。
7. 符号链接和硬链接的区别：
	1. 符号链接（软连接）：指向文件的路径，可以指向不同文件系统上的文件或目录。如果原始文件被删除，软连接会失效（变为“断链”）。
	2. 硬链接：直接指向文件的 inode，只能用于同一文件系统上的文件。即使原始文件被删除，硬链接仍然可以访问数据。
8. 实际应用场景
	1. 快速访问常用文件或目录：通过在桌面或常用目录中创建软连接，你可以快速访问深层目录结构中的文件或目录。
	2. 软件配置：在配置某些软件时，可能需要为配置文件创建软连接，以便在不同版本或环境中复用相同的配置。
	3. 开发环境：在开发过程中，可能会使用软连接来管理不同项目中的共享资源或库文件。

## 9、解压与压缩 zip 文件

### ①、zip 压缩

1. 更新软件源：

```shell
apt-get update
```

2. 安装 zip：

```shell
apt-get install zip
```

3. 压缩文件：

```shell
zip 压缩文件名.zip 要压缩的文件名1 要压缩的文件名2 ...

# 指定压缩文件名时可以省略后缀 .zip：
zip 压缩文件名 要压缩的文件名1 要压缩的文件名2 ...
```

4. 压缩目录：

```shell
zip -r 压缩文件名.zip 要压缩的目录名1/ 要压缩的目录名2/ ...

# 指定压缩文件名时可以省略后缀 .zip：
zip -r 压缩文件名 要压缩的目录名1/ 要压缩的目录名2/ ...
```

5. 压缩时可以指定多个文件或目录，指定目录时需要使用相对路径，不然压缩文件将保留绝对路径
6. 压缩时使用参数 `-P` 指定密码：

```shell
zip -P 000123 压缩文件名 要压缩的文件名1 要压缩的文件名2 ...
```

### ②、unzip 解压

1. 更新软件源：

```shell
apt-get update
```

2. 安装 unzip：

```shell
apt-get install unzip
```

3. 默认解压在当前路径：

```shell
unzip 压缩文件名
```

4. 使用参数 `-d` 指定解压路径：

```shell
unzip 压缩文件名 -d ~/指定的解压路径/
```

5. 使用参数 `-l` 列举压缩文件的内容：

```shell
unzip -l 压缩文件名
```

6. 有的压缩文件是在 Windows 下压缩的，直接在 Linux 下解压会有乱码， 这时需要指定 GBK 编码：

```shell
unzip -O GBK 压缩文件名
```

7. 直接解压加密后的压缩文件时：会提示输入密码

```shell
$ unzip Test_2.zip
Archive:  Test_2.zip
[Test_2.zip] Test.txt password: 
 extracting: Test.txt
```

8. 当然也可以在命令行指定密码：

```shell
unzip -P 000123 压缩文件名
```

## 10、复制 cp、rsync

### ①、cp

1. `cp` 命令用于复制文件或目录，基本语法如下：
	1. `-r` 或 `--recursive`：递归复制整个目录
	2. `-i` 或 `--interactive`：在覆盖文件之前提示用户确认
	3. `-u` 或 `--update`：只复制源文件比目标文件新，或者目标文件不存在的时候
	4. `-v` 或 `--verbose`：显示详细的复制过程

```shell
cp [options] 源文件或目录 目标文件或目录
```

2. 示例：
3. 复制单个文件到另一个目录：

```shell
cp file.txt /path/to/destination/
```

4. 递归复制目录到另一个位置：

```shell
cp -r /path/to/source/ /path/to/destination/
```

### ②、rsync

1. 如果还没有安装 `rsync`，可以通过以下命令安装：

```shell
sudo apt-get update

sudo apt-get install rsync
```

2. rsync 是一个强大的工具，广泛用于在 Linux 系统（包括 Ubuntu）中复制和同步文件和目录。它不仅能在本地复制数据，还能跨网络同步，同时提供了大量的选项来控制其行为。下面是 rsync 的一些基本用法和常用选项：
	1. `-a` 或 `--archive`：归档模式，等同于 `-rlptgoD`，它包括了递归复制、保持文件权限、保持符号链接等
	2. `-v` 或 `--verbose`：详细模式，显示正在传输的文件
	3. `-r` 或 `--recursive`：递归地复制文件夹
	4. `--delete`：删除目标目录中源目录没有的文件
	5. `-z` 或 `--compress`：在传输时压缩数据
	6. `--exclude`：排除匹配的文件或目录，排除路径应该相对于源目录
	7. `--include`：包含匹配的文件或目录，包含路径应该相对于源目录
	8. `-n` 或 `--dry-run`：模拟运行，显示将要执行的操作但不实际执行
	9. `--progress`：在传输时显示进度信息
	10. `-e` 或 `--rsh=COMMAND`：指定使用的远程 shell 程序，默认使用 ssh

```shell
rsync [options] 源文件或目录的路径 目标文件或目录的路径
```

3. 指定源文件或目录的路径时，如果源目录的路径后面带有斜杠 `/`，`rsync` 会复制目录内容到目标目录，而不是复制目录本身
4. 示例：
5. 本地复制文件：

```shell
rsync -av /path/to/source /path/to/destination/
```

6. 网络同步文件：

```shell
rsync -avz /path/to/source username@remote_host:/path/to/destination/
```

7. 排除特定文件或目录：

```shell
rsync -av --exclude 'pattern_to_exclude' /path/to/source /path/to/destination/
```

8. 仅同步特定文件或目录：

```shell
rsync -av --include 'pattern_to_include' --exclude '*' /path/to/source /path/to/destination/
```

9. 删除目标中不存在于源中的文件：

```shell
rsync -av --delete /path/to/source /path/to/destination/
```

10. 查看将要执行的操作（模拟运行）：

```shell
rsync -av --dry-run /path/to/source /path/to/destination/
```

## 11、移动 mv

### ①、基本语法

1. `mv` 命令用于移动文件或目录，或重命名文件或目录，基本语法如下：
	1. `-i` 或 `--interactive`：在覆盖文件之前提示用户确认
	2. `-u` 或 `--update`：只移动源文件比目标文件新，或者目标文件不存在的时候
	3. `-v` 或 `--verbose`：显示详细的移动过程

```shell
mv [options] 源文件或目录 目标文件或目录
```

2. 示例：
3. 移动文件到另一个目录：

```shell
mv file.txt /path/to/destination/
```

3. 重命名文件：

```shell
mv oldname.txt newname.txt
```

### ②、

## 12、

# 九、一些脚本

## 1、复制云服务器的文件到本地

1. 自动输入密码
2. `--delete`：全同步，删除本地目录中相比远程目录多余的文件，即保持本地目录和远程目录一致

```shell
#!/bin/bash

# 定义变量
# 阿里云 ip
SERVER_IP="127.0.0.1"
# 阿里云 用户
SERVER_USER="yan"
# 阿里云 密码
SERVER_PASSWORD="123456"
# 阿里云 路径
SERVER_PATH="/home/docker/docker/volumes/"

# 阿里云 来源，作为 rsync 命令的来源参数
SERVER_SOURCE="$SERVER_USER@$SERVER_IP:$SERVER_PATH"
# 本地 目的地，作为 rsync 命令的目的地参数
DESTINATION="/home/yan/桌面/dockerData/"

# 使用 expect 实现自动输入密码
expect <<EOF
spawn rsync -avz --delete $SERVER_SOURCE $DESTINATION
expect {
    "$SERVER_USER@$SERVER_IP's password:" {
        send "$SERVER_PASSWORD\r"
        exp_continue
    }
}
EOF
```

## 2、


# 十、
