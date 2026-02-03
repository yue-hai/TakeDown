# 一、安装系统

## 1、官方 Radxa OS (Debian)

### ①、默认账号密码

1. 账号：`radxa
2. 密码：`radxa`


### ②、

### ③、

### ④、

## 2、

# 二、安装 xrdp

## 1、安装 xrdp

1. 更新软件列表

```shell
sudo apt update
```

2. 安装 xrdp 和 xfce4，中间如果弹出框询问选 gdm3 还是 lightdm，直接回车选默认的 gdm3 即可

```shell
sudo apt install xrdp xfce4 xfce4-goodies -y
```

3. 解决 Debian/Radxa OS 特有的权限 BUG
	1. 在 Debian 系系统中，xrdp 默认没有权限读取 SSL 证书文件，这会导致连接瞬间闪退
	2. 将 xrdp 用户加入到 ssl-cert 组中即可

```shell
sudo adduser xrdp ssl-cert
```

4. 修改 xrdp 的启动脚本，防止它读取本地用户的环境变量，这是导致黑屏闪退的元凶

```shell
# 打开配置文件
sudo nano /etc/xrdp/startwm.sh
```

```shell
#!/bin/sh

# 在最前面，添加两行代码
unset DBUS_SESSION_BUS_ADDRESS
unset XDG_RUNTIME_DIR
# 添加结束

# ...后面原本的内容不要动...
if [ -r /etc/default/locale ]; then
  . /etc/default/locale
export LANG LANGUAGE
fi
# ...
```

5. 重启 xrdp 服务

```shell
sudo systemctl restart xrdp
```

## 2、安装 xrdp 问题记录

### ①、Failed to execute child process "dbus-launch" (No such file or directory)

#### Ⅰ、报错现象

1. 无法连接，报错：

![|700](attachments/Pasted%20image%2020260203142633.png)

#### Ⅱ、原因

1. 系统里少了一个叫 dbus-x11 的关键组件
2. 没有它，XFCE 桌面无法启动它的**消息总线**，所以就弹窗报错了
3. 这是 Debian 系精简版系统常见的一个问题

#### Ⅲ、解决

1. 补装缺失的组件，这个包包含了报错里提到的 dbus-launch 工具

```shell
sudo apt install dbus-x11 -y
```

2. 重启服务

```shell
sudo systemctl restart xrdp
```

### ②、

### ③、

### ④、

## 3、

## 4、

## 5、

## 6、


# 三、系统设置

## 1、添加中文

1. 安装中文字体，Linux 默认只有英文字体，如果不装中文字体包，切换语言后显示不出来汉字。这里只装谷歌出品的 Noto CJK 字体

```shell
# 更新软件列表
sudo apt update

# 安装中文字体 Noto CJK
sudo apt install fonts-noto-cjk -y
```

2. 运行配置命令

```shell
sudo dpkg-reconfigure locales
```

3. 运行配置命令后，在出来的界面中操作（键盘流）：
	1. 按 向下箭头 键一直往下翻，大概在列表的末尾部分
	2. 找到 `zh_CN.UTF-8 UTF-8` 这一行
	3. 按 空格键 选中它，此时方括号里会出现一个 * 号
	4. 按 Tab 键，光标会跳到 `<Ok>` 上，按 回车
4. 选择默认语言：
	1. 系统会跳到下一个界面，问你 default locale（默认语言）用哪个
	2. 按 向下箭头 选中 `zh_CN.UTF-8`
	3. 按 Tab 键跳到 `<Ok>`，按 回车
	4. 等待终端跑完，显示 Generation complete 即可
5. 重启机器，为了让所有服务和界面都应用中文，最彻底的方法是重启一

```shell
sudo reboot
```


## 2、禁用系统休眠

1. 禁止 睡眠/挂起

```shell
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

2. 防止锁屏掉线 XFCE 设置：虽然上面的命令禁止了硬件休眠，但桌面环境可能会自己黑屏锁屏。如果不想每次连接都要输密码解锁，可以运行这条命令（针对当前用户）：

```shell
xset s off 
xset -dpms
```

3. 重启机器

```shell
sudo reboot
```

## 3、

## 4、


# 四、

# 五、

# 六、

# 七、

# 八、

# 九、

# 十、

# 十一、

# 十二、

# 十三、

# 十四

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、



