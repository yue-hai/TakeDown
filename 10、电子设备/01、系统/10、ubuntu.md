# 一、系统安装

1. 桌面版镜像下载：https://cn.ubuntu.com/download/desktop
2. 可使用 rufus 创建启动盘：https://rufus.ie/zh/
3. 在 bios 中选择从启动盘打开，但是有的 bios 需要关闭安全启动；一般是 boot 选项下的 `Secure Boot` 选项，修改为 `Disabled` 禁用
4. 在 bios 选择从启动盘打开后，选择第一项：`Try or Install Ubuntu`，然后按回车

![|655](attachments/Pasted%20image%2020231225150729.png)

5. 在下一个屏幕中，单击 `Install Ubuntu`

![|655](attachments/Pasted%20image%2020231225150824.png)

6. 选择喜欢的键盘布局，然后单击下一步

![|655](attachments/Pasted%20image%2020231225150914.png)

7. 在这一步中，我们必须选择安装类型。有两个选项，普通安装和最小安装，然后单击下一步
	1. 在普通安装中，将安装所有 GUI 相关的应用程序，
	2. 在最小安装中只会安装基本的应用程序。

![|655](attachments/Pasted%20image%2020231225151000.png)

8. 在这一步中，将提示我们选择安装类型。这里的安装类型指的是分区方案。以下是两种安装类型
	1. `Erase Disk and Install Ubuntu`：它将删除整个磁盘，并将自动创建分区。
	2. `Something else`：创建自定义分区方案。如果是 Ubuntu Linux 的新手，那么建议选择第一个选项

![|655](attachments/Pasted%20image%2020231225151211.png)

9. 根据当前的地区选择位置，它将相应地配置时区。

![|655](attachments/Pasted%20image%2020231225151259.png)

10. 创建用户并设置主机名；在此步骤中，指定本地用户名及其密码，指定系统的主机名。我们会在安装系统后使用该用户。

![|655](attachments/Pasted%20image%2020231225151331.png)

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

![](attachments/Pasted%20image%2020230725150747.png)

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
sudo nano /etc/ssh/sshd_config
```

```shell
# 将：
#PermitRootLogin prohibit-password
# 改成
PermitRootLogin yes

# 将：
#PasswordAuthentication yes
# 改成
PasswordAuthentication yes
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

![|700](attachments/Pasted%20image%2020231226102848.png)

## 4、


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

## 6、按需启动桌面环境

### ①、设置默认启动状态为纯命令行

1. 将 Ubuntu 的默认启动状态设置为纯命令行，但保留所有图形界面（GNOME）和 XRDP 的组件

```shell
# 设置开机默认不启动桌面
sudo systemctl set-default multi-user.target
```

2. 之后直接连接显示器时，显示器上不会显示桌面画面，而是终端，要输入下面这个命令才会唤醒桌面环境：

```shell
sudo systemctl isolate graphical.target
```


3. 拔掉显示器后，再输入这个命令，关闭图形界面回到纯命令行

```shell
sudo systemctl isolate multi-user.target
```

4. 远程桌面 (XRDP) 的按需唤醒：
	1. xrdp 本身是一个非常轻量级的后台服务，驻留在后台几乎不占资源
	2. 它的工作原理是：当通过 Windows 远程桌面连接时，xrdp 会临时生成（唤醒）一个桌面会话
	3. 核心注意点：当通过 RDP 使用完之后，绝对不能只点击右上角的 X 直接关闭窗口！ 这样只是断开了连接，GNOME 桌面依然在服务器后台运行，继续消耗资源
	4. 必须在 Ubuntu 桌面的右上角选择 <font color="#ff0000">注销</font> (Log Out)。注销后，本次生成的桌面会话就会被彻底销毁，系统再次回到低负载状态

### ②、问题记录

#### Ⅰ、远程桌面连接后黑屏

##### （1）、报错现象

1. 使用远程桌面可以连接，但是一直显示黑屏，也不会报错断开

![|700](attachments/Pasted%20image%2020260402084836.png)

##### （2）、原因

1. 这是典型的 **图形会话冲突**
2. 在 Ubuntu 宿主机上启动了 GNOME 图形界面，可能是通过 `startx` 或 `systemctl isolate graphical.target` 命令，也可能是将默认启动改了回去
3. 此时，物理显卡/虚拟显卡资源已经被宿主机的 GNOME 桌面环境给霸占了
4. 当通过 Windows 远程桌面连接时，xrdp 启动一个新的、专供远程使用的图形会话
5. 但是，由于显卡资源已经被宿主机的桌面占用了，xrdp 创建的新会话无法正常渲染画面，于是就只看到了一个连接成功但内容全黑的窗口

##### （3）、解决

1. 确保默认启动模式是纯命令行：

```shell
sudo systemctl set-default multi-user.target
```

2. 找出所有与桌面环境相关的进程：

```shell
ps -U yan -f | grep 'gnome-shell\|Xorg\|gdm'
```

3. 强制终止这些进程

```shell
sudo kill -9 1234
```

##### （4）、根除问题

1. 问题原因：XRDP 在用户注销时，没有能够干净、彻底地终结掉整个图形会话（Xorg 服务和 GNOME Shell），导致这些进程变成了 **孤儿** 在后台残留；当下一次再次连接时，XRDP 发现已经有一个属于您的桌面会话在运行（虽然它已经卡死了），于是尝试去 **重用** (reconnect) 这个会话，结果就直接连上了一个黑屏
2. 为什么 XRDP 会留下 **残局**：出现这种现象，通常和 `/etc/xrdp/sesman.ini` 这个配置文件中的会话管理策略有关。默认情况下，XRDP 可能会被配置成一种 **断开后保留会话** 的模式，以便用户下次能快速重连。但这种模式在和现代桌面环境（如 GNOME）配合时，非常容易出问题，导致注销不彻底
3. 解决：修改 `sesman.ini` 文件，强制要求 XRDP 在用户断开连接或注销时，无条件地终结整个会话，而不是让它继续保留。这样每次远程登录都是一次全新的、干净的会话
4. 用 nano 编辑器打开配置文件：

```shell
sudo nano /etc/xrdp/sesman.ini
```

5. 找到 `[SessionVariables]` 配置段，修改两个关键参数，如果没有就自己添加，确保它们的值是 `true`：
	1. `KillDisconnected=true`：
		1. 含义：当用户的 RDP 客户端意外断开（比如网络中断，或者直接点了窗口的 "X"）时，立即终结这个会话
		2. 效果： 防止因为非正常退出而导致会话残留
	2. `KillOnExit=true`：
		1. 含义：当用户在会话内部正常注销 (Log Out) 时，确保整个会话（包括 Xorg 服务）被彻底终止
		2. 效果：这是解决您当前“手动注销依然残留”问题的核心武器

```shell
[SessionVariables]
...
...
# 将下面这两行的值修改为 true
KillDisconnected=true
KillOnExit=true
...
```

6. 重启 XRDP 服务使配置生效：

```shell
sudo systemctl restart xrdp
```

#### Ⅱ、

#### Ⅲ、


## 7、开机自动挂载硬盘到指定目录

1. 查看所有磁盘列表：

```shell
lsblk
```

```shell
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0     7:0    0     4K  1 loop /snap/bare/5
loop1     7:1    0    74M  1 loop /snap/core22/2292
loop2     7:2    0 251.7M  1 loop /snap/firefox/7766
loop3     7:3    0  66.8M  1 loop /snap/core24/1587
loop4     7:4    0 531.4M  1 loop /snap/gnome-42-2204/247
loop5     7:5    0  10.8M  1 loop /snap/snap-store/1270
loop6     7:6    0  91.7M  1 loop /snap/gtk-common-themes/1535
loop7     7:7    0  48.1M  1 loop /snap/snapd/25935
loop8     7:8    0   576K  1 loop /snap/snapd-desktop-integration/343
loop9     7:9    0  48.4M  1 loop /snap/snapd/26382
loop10    7:10   0 254.9M  1 loop /snap/firefox/7967
loop11    7:11   0  66.8M  1 loop /snap/core24/1499
loop12    7:12   0  15.5M  1 loop /snap/snap-store/1310
loop13    7:13   0    74M  1 loop /snap/core22/2411
loop14    7:14   0   395M  1 loop /snap/mesa-2404/1165
loop15    7:15   0 606.1M  1 loop /snap/gnome-46-2404/153
loop16    7:16   0  18.5M  1 loop /snap/firmware-updater/212
loop17    7:17   0  16.4M  1 loop /snap/firmware-updater/223
sda       8:0    0 465.8G  0 disk 
├─sda1    8:1    0     1G  0 part /boot/efi
├─sda2    8:2    0     2G  0 part 
├─sda3    8:3    0     8G  0 part [SWAP]
└─sda4    8:4    0 454.7G  0 part 
nvme0n1 259:0    0   1.8T  0 disk /mnt/data
yan@yuehai-nas:~$ 
```

2. 通过硬盘的大小来判断目标硬盘的代号，比如我当前需要处理的硬盘是 2t 的，那么就是 `nvme0n1`
3. 卸载当前的临时挂载：

```shell
sudo umount /dev/nvme0n1
```

4. 在系统根目录创建数据文件夹：

```shell
sudo mkdir -p /mnt/data
```

5. 获取硬盘的唯一身份证 UUID：

```shell
sudo blkid /dev/nvme0n1
```

```shell
/dev/nvme0n1: LABEL="970_EVO_Plus" UUID="f05320df-gd4k-4da9-bc5a-7e3a151b623f" BLOCK_SIZE="4096" TYPE="ext4"
```

6. 备份配置文件：

```shell
# 备份文件
sudo cp /etc/fstab /etc/fstab.bak
```

7. 使用 nano 编辑器打开配置文件，然后在文件的最末尾，另起一行，添加配置：
	1. `defaults`：使用默认的读写权限；
	2. `0`：不让系统自带的 dump 备份它
	3. `2`：开机时在系统盘之后检查它的磁盘错误

```shell
# 使用 nano 编辑器打开
sudo nano /etc/fstab
```

```shell
UUID=上面获取的UUID /mnt/data ext4 defaults 0 2
```

8. 执行自动挂载测试，如果敲完回车后什么提示都没有（没有报错），那么配置正确：

```shell
sudo mount -a
```

```shell
# 出现这个提示是正常的
mount: (hint) your fstab has been modified, but systemd still uses

       the old version; use 'systemctl daemon-reload' to reload.
```

9. 配置权限，把这个 2TB 硬盘的所有权交给自己：

```shell
sudo chown -R yan:yan /mnt/data
```

10. 刷新 systemd 的配置缓存：

```shell
systemctl daemon-reload
```

11. 再次执行全盘挂载：

```shell
mount -a
```

12. 配置完毕，测试可以输入 `df -h` 检查一下，列表的最下方已经稳稳地出现了挂载在 `/mnt/data` 上的 2TB 硬盘。以后无论怎么断电重启，它都会死死地钉在这个目录下


## 8、

## 9、


# 六、命令使用

## 1、实时进程监控工具 top

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

## 2、套接字信息检索工具 `ss`

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

## 3、处理压缩文件和目录常用的命令

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

## 4、查看 Ubuntu 系统和内核的版本

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

## 5、软连接（符号链接）ln

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

## 6、复制 cp、rsync

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

## 7、移动 mv

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


## 8、使用 dos2unix 转换换行符格式

1. 报错信息：

```shell
-bash: ./run_jar.sh: /bin/bash^M: bad interpreter: No such file or directory
```

1. 原因：错误信息中的 `^M` 表示的是 Windows 风格的换行符（Carriage Return + Line Feed），而在 Unix/Linux 系统中使用的是 Line Feed。这种不同的换行符格式可能导致解释器无法正确识别脚本文件。
2. 解决：使用 `dos2unix` 命令将脚本文件的换行符格式转换为 Unix 格式。在终端中执行以下命令：

```shell
# run_jar.sh 替换为需要转换的文件
dos2unix run_jar.sh
```

1. 若是提示以下内容，则需要安装 dos2unix

```shell
Command 'dos2unix' not found, but can be installed with:
apt install dos2unix
Please ask your administrator.
```

1. 更新软件源

```shell
sudo apt update
```

1. 执行以下命令安装 dos2unix

```dart
apt install dos2unix
```

## 9、使用 sed 转换换行符格式

1. 上面是使用 dos2unix 转换的，也可以直接使用 `sed` 命令进行替换：

```shell
sed -i 's/\r$//' run_jar.sh
```

## 10、查看指定目录中所有文件和子目录的总大小

1. 基本命令：
	1.  `-s`：表示汇总指定目录的总大小
	2. `-h`：使输出以易于阅读的格式（如 KB、MB 或 GB）显示。

```shell
du -sh /path/to/directory
```

1. 如果想看到每个子目录的大小而不仅仅是总大小，可以省略 `-s` 选项。这会列出所有子目录及其大小：

```shell
du -h /path/to/directory
```

1. 查看特定深度的目录大小：
	1. `--max-depth=1`：表示只显示直接子目录的大小。
	2. 可以将 1 替换为其他数字来指定不同的深度。

```shell
du -h --max-depth=1 /path/to/directory
```



# 七、配置脚本

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

## 2、定时挂载和卸载硬盘的脚本

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


# 八、


# 九、问题记录

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

1. 输出结果：

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

1. 最末尾 `/dev/sdb2` 就是出问题的硬盘
2. 修复挂载错误的相应的分区，如提示中的 `/dev/sdb2`，输入：

```shell
sudo ntfsfix /dev/sdb2
```

1. 再次插入移动硬盘即可正常使用

## 6、


# 十、硬件驱动

# 十一、

# 十二、

# 十三、

# 十四

# 十五、云服务器

## 1、DMIT 服务器

### ①、设置 ssh 密钥登录

1. 打开命令提示符 (CMD) 或 PowerShell，复制并粘贴以下命令，然后按回车：
	1. `-t ed25519`：指定生成一种高安全性的密钥类型
	2. `-C "dmit-key"`：给这个密钥一个备注，方便识别
	3. `-f ~/.ssh/dmit_key`：将生成的私钥命名为 dmit_key，并保存在 .ssh 文件夹下

```shell
ssh-keygen -t ed25519 -C "dmit-key" -f C:/Users/10222148/.ssh/dmit_key
```

2. 按三次回车，执行命令后，它会问三次问题：
	1. Enter file in which to save the key...：保存密钥到哪里？ 直接按回车，使用默认位置
	2. Enter passphrase...：是否给密钥文件本身再加一个密码？ 直接按回车，表示不需要
	3. Enter same passphrase again...：再次输入密码。 直接按回车
	4. 完成后，它会提示密钥已经生成，并显示一个图案
3. 进入目录 `C:/Users/10222148/.ssh`，打开新生成的文件 `dmit_key.pub`，这里的完整内容就是公钥，一会会用到
4. 进入 dmit 控制台，点击更改密钥

![|700](attachments/Pasted%20image%2020260119133620.png)

5. 点击添加密钥，将刚才生成的 `dmit_key.pub` 文件中的全部内容都复制到公钥中，然后随意设定一个名字，点击添加 SSH Key 即可

![|700](attachments/Pasted%20image%2020260119133850.png)

6. 最后返回 dmit 控制台，点击更改密钥，然后选择刚才添加的 SSH Key 即可

![|700](attachments/Pasted%20image%2020260119134057.png)

7. dmit 服务器设置完毕后，在 ssh 终端中，选择生成的私钥文件 `C:/Users/10222148/.ssh/dmit_key` 即可进行登录

![|640](attachments/Pasted%20image%2020260119134337.png)


### ②、使用账号密码登录

1. 修改主配置文件 `/etc/ssh/sshd_config`

```shell
# 打开主配置文件
nano /etc/ssh/sshd_config

# 找到 PermitRootLogin prohibit-password 这一行
PermitRootLogin yes
```

2. 修改 Cloud-init 的 SSH 配置文件 `/etc/ssh/sshd_config.d/50-cloud-init.conf`，确保 Cloud-init 在下次启动时，不会把设置再改回去

```shell
# 打开 Cloud-init 的 SSH 配置文件
nano /etc/ssh/sshd_config.d/50-cloud-init.conf

# 修改或者添加配置：
PasswordAuthentication yes
```

3. 修改完毕，之后就可以直接使用账号密码密码登录

### ③、安装 UFW 防火墙

1. 安装 UFW 防火墙

```shell
# 更新软件源
sudo apt update

# 安装 UFW
sudo apt install ufw
```

2. 设置默认规则

```shell
# 拒绝所有进入服务器的网络连接
sudo ufw default deny incoming
# 允许所有从服务器出去的网络连接
sudo ufw default allow outgoing
# 许所有通过SSH服务（22号端口）的连接进入
sudo ufw allow ssh
```

3. 开启 http、https 端口

```shell
# 开启 http 80 端口
sudo ufw allow 80
# 开启 https 443 端口
sudo ufw allow 443
```

4. 启动 UFW 防火墙

```
sudo ufw enable
```

5. 列出防火墙状态，以及设置的所有规则列表

```shell
sudo ufw status verbose
```

## 2、

## 3、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、

