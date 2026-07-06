# 一、开发工具

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

## 2、


# 二、系统工具

## 1、使用 NUT 配置 UPS 不间断电源

> 参考：https://www.wangchucheng.com/zh/posts/setting-up-ups-with-nut-on-linux/#%E5%AE%9A%E6%97%B6%E5%85%B3%E6%9C%BA

1. 此处我使用的 UPS 设备是：山特 TG-BOX850
2. 首先需要将 UPS 接入电源并将电脑接入 UPS 插座，还需要将 UPS 的数据线与电脑的 USB 口相连接
3. 系统是：Ubuntu 22.04.3 LTS

### ①、安装 NUT

1. NUT（Network UPS Tools）是一套开源工具，用于监控 UPS（不间断电源）以及与 UPS 相关的电源设备，并在电源出现问题时自动执行操作（如关机）
2. NUT 在各类 Linux 系统中均可以使用默认的包管理工具进行安装。我使用的是 Ubuntu 22.04.3 LTS，安装指令如下所示：

```shell
# 更新软件源
sudo apt update

# 安装 nut
apt install nut
```

### ②、配置 UPS

#### Ⅰ、配置 UPS 驱动

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

3. 修改 `/etc/nut/ups.conf` 文件，在其中添加如下内容：

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

4. 设置 NUT 运行模式，找到 `/etc/nut/ups.conf` 文件中的 `MODE` 属性，将其配置为 `standalone` 模式

```shell
# 将其配置为 standalone 模式
MODE=standalone
```

5. 重新加载并应用最新的 USB 设备权限规则

```shell
sudo udevadm control --reload-rules
sudo udevadm trigger
```

6. 接下来可以通过以下命令启动 UPS：

```shell
sudo systemctl start nut-server
```

7. 停止 UPS：

```shell
sudo systemctl stop nut-server nut-client nut-monitor
```

#### Ⅱ、查看 UPS 的相关信息

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

### ③、配置 NUT 服务

> 此处将设置操作 UPS 的用户信息

#### Ⅰ、新建用户

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

#### Ⅱ、配置权限

1. 需要注意的是我们不应使该文件对所有用户均可读，因为它包含密码等敏感信息。我们可以使用如下命令设置相关权限：

```shell
# 确保只有 root 用户和 nut 组的成员可以读取和修改 /etc/nut/upsd.conf 和 /etc/nut/upsd.users 文件
chown root:nut /etc/nut/upsd.conf /etc/nut/upsd.users
chmod 0640 /etc/nut/upsd.conf /etc/nut/upsd.users
```

#### Ⅲ、启动服务

1. 启动服务：

```shell
sudo systemctl start nut-server
```

2. 重启服务：

```shell
sudo systemctl restart nut-server
```

3. 查看帮助

```shell
/sbin/upsd --help
```


#### Ⅳ、设置电池低电量自动关机

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
sudo systemctl start nut-monitor
```

### ④、自定义事件

#### Ⅰ、介绍

1. 除了默认的低电量关机功能，可能我们有时还需其他自定义的功能。例如停电一分钟后关机或者邮件通知等。NUT 通过 upssched 提供了该功能。
2. 该功能的实现为通过在 upsmon 中设置触发条件通知 upssched，并由 upssched 完成后续工作。

#### Ⅱ、修改 upsmon 设置

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

#### Ⅲ、配置 upssched

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
sudo systemctl start nut-monitor
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

#### Ⅳ、编写脚本

1. 上面定义的执行脚本是：`/usr/local/bin/upssched`，所以我们要创建该脚本，同时注意该脚本所属的用户，避免权限上的出错

```shell
nano /usr/local/bin/upssched
```

2. 在脚本中写入以下内容；类似的，还可以通过编写脚本的方式进行其他操作：

```shell
#! /bin/sh

# 定日志文件路径，用于记录 UPS 电源状态变化
path_log="/var/log/nut/SANTAK-TGBOX-850-NUT.log"

# 定义方法，用于记录日志
sava_log() {
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】 - $1" >> $path_log
}
# 定义方法，用于发送邮件通知
send_mail() {
    echo "【$(date '+%Y-%m-%d %H:%M:%S')】 - $1" | mail -s "$2" -r yan@yuehai.fun 770717410@qq.com
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

3. 给予脚本文件权限：

```shell
sudo chmod +x /usr/local/bin/upssched; sudo chown root:nut /usr/local/bin/upssched
```

4. 创建日志目录并给权限：

```shell
sudo mkdir -p /var/log/nut; sudo chown nut:nut /var/log/nut
```

5. 创建日志文件并设置日志文件的权限，允许所有人进行读写

```shell
touch /var/log/nut/SANTAK-TGBOX-850-NUT.log; chmod 666 /var/log/nut/SANTAK-TGBOX-850-NUT.log
```

6. 将日志文件软连接到其他地方，以便于查看：

```shell
# 登录 yan 用户
su yan

# 将文件 /var/log/nut/SANTAK-TGBOX-850-NUT.log 软连接到 目录 /mnt/data/app_data/system/SystemEnhancement/nut/ 下
ln -s /var/log/nut/SANTAK-TGBOX-850-NUT.log /mnt/data/app_data/system/SystemEnhancement/nut/
```

### ⑤、文件的简单解释

#### Ⅰ、upsmon.conf

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

#### Ⅱ、upssched.conf

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
	4. 启动一个名为 `<timername>` 的定时器，在 `<interval>` 秒后触发，并将 `<timername>` 作为第一个参数传递给 `CMDSCRIPT`。
	5. 示例：当任意 UPS（`*`）的通信断开超过 10 秒时执行：

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


## 2、cockpit 网页系统控制台

### ①、说明

1. Cockpit 是一个现代、轻量且开源的 Linux 服务器管理面板。它通过网页浏览器，为用户提供了一个直观的图形化界面，以执行和监控系统底层的管理任务，核心特点：
2. 轻量无侵入：Cockpit 自身资源占用极低（仅在访问时激活），且所有操作都是通过标准的、底层的 Linux API（如 systemd, DBus）完成。在界面上做的任何修改，都能在命令行中立刻反映出来，反之亦然，二者永远同步
3. 即用即装 (Out-of-the-Box)：被包含在大多数主流 Linux 发行版（如 Debian, Ubuntu, CentOS）的官方仓库中，安装简单，使用服务器的本地账户即可登录
4. 功能全面 (Comprehensive)：覆盖了系统监控、日志查看、存储管理 (RAID/LVM/ZFS)、网络配置、服务启停、用户账户管理等核心运维功能
5. 高度可扩展 (Extensible)：支持通过安装插件来增强功能，例如集成虚拟机管理 (cockpit-machines)、容器管理 (cockpit-podman) 和更高级的存储方案 (cockpit-zfs-manager)
6. 内置终端 (Built-in Terminal)：无缝内嵌了一个功能完整的 SSH 终端，允许用户在图形化操作和命令行之间自由切换
7. 一句话总结：Cockpit 是为系统管理员和高级用户设计的，一个将强大的 Linux 命令行后台，用直观且标准的方式呈现在浏览器前端的瑞士军刀

### ②、安装

1. 更新软件源

```shell
sudo apt update
```

2. 安装 cockpit 本体、虚拟机管理器

```shell
sudo apt install cockpit cockpit-machines -y
```

3. cockpit 依赖于 python3，如果没安装 python3 需要手动安装：

```shell
sudo apt install python3-venv -y
```

### ③、访问

1. 访问：[http://127.0.0.1:9090](http://127.0.0.1:9090)
2. 进入登录页面后，输入机器的用户名密码即可进入

### ④、nginx 代理

#### Ⅰ、创建 cockpit 配置文件

1. 编辑或创建配置文件：

```shell
sudo vi /etc/cockpit/cockpit.conf
```

2. 写入针对您域名的专有配置：

```shell
[WebService]
# 带上完整域名端口，否则安全校验依然无法通过
Origins = https://cockpit.yuehai.fun:63 http://127.0.0.1:9090 https://127.0.0.1:9090 http://192.168.1.5:9090 https://192.168.1.5:9090
ProtocolHeader = X-Forwarded-Proto
# 可通过 http 访问，转到 http 放行
AllowUnencrypted = true
```

3. 重新加载配置文件

```shell
systemctl daemon-reload
```

4. 重启 Cockpit 服务让新规则生效：

```shell
sudo systemctl restart cockpit.socket
sudo systemctl restart cockpit
```

#### Ⅱ、nginx 添加内网通信规则

1. 仅允许内网 `192.168.0.0/16` 访问

![|500](attachments/Pasted%20image%2020260331105459.png)

![](attachments/Pasted%20image%2020260331105505.png)

![](attachments/Pasted%20image%2020260331105511.png)

#### Ⅲ、代理服务，应用内网通信规则

![](attachments/Pasted%20image%2020260331105604.png)


## 3、kvm 虚拟机

### ①、安装 KVM 底层 + virt-manager 桌面版

1. 检查 CPU 是否支持虚拟化，只要输出的数字大于 0 就没问题：

```shell
egrep -c '(vmx|svm)' /proc/cpuinfo
```

2. 安装 KVM 核心组件和图形化管理器

```shell
# 更新软件源
sudo apt update

# 安装 KVM 核心组件和图形化管理器
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager -y
```

3. 将 yan 账户加入权限组

```shell
sudo adduser yan libvirt
sudo adduser yan kvm
```

4. 重启机器或者注销并重新登录

### ②、设置数据盘

1. KVM 虚拟机默认会把所有创建的虚拟硬盘文件 `.qcow2` 放在 `/var/lib/libvirt/images/` 目录下。也就是说，如果不改配置，虚拟机都会存在系统盘
2. 创建目录 `/mnt/data/VMs`：

```shell
mkdir -p /mnt/data/VMs
```

3. 在 **虚拟系统管理器** 中修改默认路径：
4. 打开虚拟系统管理器，点击顶部菜单栏的 编辑 (Edit) -> 连接详情 (Connection Details)

![](attachments/Pasted%20image%2020260401090443.png)

5. 切换到 **存储** (Storage) 选项卡，点击左下角的 `+` 号添加一个新的存储池。名字可以叫 `Data_VMs`，类型选 `dir: 文件系统目录`，目标路径选择自己想要指定的目录，比如 `/mnt/data/VMs`

![](attachments/Pasted%20image%2020260401090709.png)

6. 点击完成即可

### ③、下载 virtio-win 驱动

1. `virtio-win` 是虚拟化环境中 ‌Windows 虚拟机高性能运行的基石‌，尤其适用于对磁盘和网络性能敏感的场景
2. `virtio-win` 是一个专为 ‌Windows 虚拟机‌ 设计的 ‌半虚拟化驱动集合‌，主要用于在基于 KVM/QEMU 的虚拟化环境（如 Proxmox VE、OpenStack 等）中提升 Windows 客户机（Guest OS）的性能和功能支持
3. 包含 磁盘控制器（viostor/vioscsi）、网卡（netkvm）、内存气球（balloon）、串口（vioserial）‌ 等驱动，使 Windows 虚拟机能够识别和使用 KVM/QEMU 提供的 VirtIO 设备
4. 相比传统模拟设备（如 IDE 磁盘或 E1000 网卡），VirtIO 驱动可显著降低 I/O 延迟，提升吞吐量
5. 官方最新稳定版 virtio-win.iso 下载：https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso

### ④、创建虚拟机

1. 第一步，选择 本地安装介质(ISO映像或者光驱)(L)

![](attachments/Pasted%20image%2020260401091812.png)

2. 第二步，选择想要安装的 iso 镜像文件

![](attachments/Pasted%20image%2020260401091925.png)

3. 第三步，设置内存和 cpu 数，虚拟机运行时，并不会全部占用设置的数量

![](attachments/Pasted%20image%2020260401092103.png)

4. 第四步，操作 1，选择或创建自定义存储(S)，然后点击管理

![](attachments/Pasted%20image%2020260401092305.png)

5. 第四步，操作 2，确保左侧选中了 Data_VMs，然后点击中间带有绿色加号 `+` 的按钮

![](attachments/Pasted%20image%2020260401103607.png)

6. 第四步，操作 3，创建存储卷
	1. 名称：随便起，比如 `windows_server_2016`
	2. 格式：建议保持默认的 `qcow2`。这是 KVM 的原生格式，支持极速快照，而且是 **动态扩容** 的，即如果分配了 100G，但里面只装了 20G 的文件，它在物理硬盘上实际上只占用 20G 的空间
	3. 容量：想要给这台虚拟机分配的最大硬盘大小
	4. 点击完成

![](attachments/Pasted%20image%2020260401103648.png)

7. 第四步，操作 4，选择刚才创建的储存卷，然后点击 Choose Volume

![](attachments/Pasted%20image%2020260401103724.png)

8. 第四步，操作 5，自定义存储创建完成，点击下一步

![](attachments/Pasted%20image%2020260401104029.png)

9. 第五步，创建信息确认
	1. 名称：随便起，比如 `windows_server_2016`
	2. 一定要勾选 <font color="#ff0000">安装前自定义配置</font>
	3. 点击完成

![](attachments/Pasted%20image%2020260401104124.png)

### ⑤、虚拟机安装前自定义配置

1. 上面勾选安装前自定义配置点击完成后，系统不会立刻开机进入安装界面，而是会弹出一个极其详细的虚拟硬件编辑窗口。在这里，要对 Windows 虚拟机进行三项必须的微调，否则鼠标会卡顿，甚至可能无法识别虚拟硬盘
2. 第一步：改 BIOS 为 UEFI
	1. 点击左侧列表最上面的 **概况** (Overview)
	2. 在右侧找到 **固件** (Firmware) 选项
	3. 从默认的 BIOS 改为 UEFI

![|700](attachments/Pasted%20image%2020260401105206.png)

3. 第二步：修改磁盘总线类型
	1. 点击左侧的 **SATA 磁盘 1**
	2. 把 **磁盘总线** (Disk bus) 改为 `VirtIO`，VirtIO 是 KVM 的半虚拟化直通技术，硬盘跑满速全靠它
	3. 此时应用后，左侧的 **SATA 磁盘 1** 会变成 **Virtlo 磁盘 1**

![|700](attachments/Pasted%20image%2020260401105236.png)

4. 第三步：修改网卡类型
	1. 如果没改桥接的话，这里的 **网络源** 应该是 **虚拟网络'default'：NAT**，我是已经修改为桥接了，没有桥接选择虚拟网络即可
	2. 点击左侧的 **NIC : xx:xx:xx**（网卡）
	3. 把右侧的 **设备型号** (Device model) 改为 `virtio`
	4. 点击应用

![|700](attachments/Pasted%20image%2020260401105441.png)

### ⑥、添加 virtio-win 驱动光盘

1. 点击添加硬件

![|700](attachments/Pasted%20image%2020260401105640.png)

2. 设备类型选择 **CDROM 设备**，总线类型选择 **SATA**，勾选 **选择或创建自定义存储**，点击 **管理**

![|700](attachments/Pasted%20image%2020260401110309.png)

3. 找到刚才下载的 `virtio-win.iso` 并选中，点击完成

![](attachments/Pasted%20image%2020260401110421.png)

![|700](attachments/Pasted%20image%2020260401110450.png)

4. 现在左侧列表里应该有两个 CDROM 设备了

![|700](attachments/Pasted%20image%2020260401110528.png)

### ⑦、安装系统

1. 上面的配置完成后，点击最上方的开始安装
2. 显示出来虚拟机的画面后，立刻用鼠标在黑色的画面里点一下，然后只要屏幕上一出现 `Press any key to boot from CD or DVD...` 这行字，立刻狂按空格键或回车键，如果错过了就强制重启然后重复这个步骤
3. Windows 安装光盘加载成功，点击 **下一步**，然后点击 **现在安装**

![|700](attachments/Pasted%20image%2020260401112232.png)

4. 选择要安装的系统，建议选择第二个：Windows Server 2016 Standard (桌面体验)
	1. 带不带 **桌面体验** 的区别：第一、三项没有任何括号的选项是 Server Core（服务器核心版），装完之后没有图形界面，只有纯命令提示符窗口
	2. Standard（标准版） 和 Datacenter（数据中心版）：这两者的图形界面和基础功能一模一样。Datacenter 主要是给大型数据中心做无限制嵌套虚拟化和软件定义网络用的，日常使用来说 Standard 标准版完全足够了

![|700](attachments/Pasted%20image%2020260401112510.png)

5. 选择 自定义：仅安装 Windows (高级)

![|700](attachments/Pasted%20image%2020260401112735.png)

6. 加载 virtio-win 驱动
	1. 点击左下角的 加载驱动程序
	2. 点击 浏览
	3. 找到叫 virtio-win 的光驱盘符，依次展开进入：viostor -> 2k16 (因为是 Server 2016 系统) -> amd64 文件夹
	4. 点击确定，列表里会出现 Red Hat VirtIO SCSI controller，选中它点下一步

![|700](attachments/Pasted%20image%2020260401112913.png)

![|700](attachments/Pasted%20image%2020260401112925.png)

![|700](attachments/Pasted%20image%2020260401112943.png)

![|700](attachments/Pasted%20image%2020260401123936.png)

![|700](attachments/Pasted%20image%2020260401124241.png)

7. 进度条跑完后，128G 的虚拟硬盘就会出现在列表里了，选中那块 128G 的未分配空间，点击下一步，Windows 就会开始复制文件、正式进入安装流程了

![|700](attachments/Pasted%20image%2020260401124427.png)

8. 系统安装完成，设置密码

![|700](attachments/Pasted%20image%2020260401124840.png)

9. 安卓完毕，进入桌面

![|700](attachments/Pasted%20image%2020260401124947.png)


### ⑧、安装 VirtIO 全套驱动

1. 不论底层网络是 NAT 还是桥接，这台虚拟机的 **物理网卡** 已经被设置成了 virtio 模式
2. Windows 原生根本就不认识这种网卡设备，所以它现在是断网状态。只有打上驱动，它才能认出网卡

![|700](attachments/Pasted%20image%2020260401125543.png)

3. 在虚拟机里打开 **此电脑** (文件资源管理器)，找到那个挂载了 virtio-win 驱动的光驱，双击打开它

![|700](attachments/Pasted%20image%2020260401130959.png)

4. 在光盘根目录里，一直往下滚动，找到一个名为 `virtio-win-guest-tools.exe` 的程序

![|700](attachments/Pasted%20image%2020260401131037.png)

5. 双击运行它，一路无脑点击 **下一步**，同意许可协议，然后点击 **Install** (安装)

![|700](attachments/Pasted%20image%2020260401131057.png)

6. 安装过程中可能会弹出几次 **是否信任来自 Red Hat 的软件** 的确认框，全部勾选信任并点击 **安装**

![|700](attachments/Pasted%20image%2020260401131128.png)

7. 安装进度条跑完后，就会：
	1. 右下角那个带红叉的网络图标会自动变成连接状态，通过 NAT 连上了外网
	2. 如果打开 **设备管理器**，里面所有带黄色感叹号的未知设备（PCI 设备、以太网控制器等）都会全部消失，被完美识别
8. 打完驱动后，可以试着打开虚拟机里的浏览器，随便上个网测试一下。如果网络畅通，就可以把它正常关机，然后去 Ubuntu 底层把桥接（Bridge）给做出来了

![|700](attachments/Pasted%20image%2020260401131152.png)


### ⑨、ubuntu 修改底层网络为桥接（Bridge）

1. 将虚拟机关机
2. 获取当前的真实网络信息：

```shell
# 查看网卡名称和 IP
ip a

# 查看目前的网络配置文件
cat /etc/netplan/*.yaml
```

```shell
user@my-nas-server:~$ ip a

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever

# 物理网卡，连接到局域网
2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    # MAC 地址
    link/ether 00:1a:2b:3c:4d:5e brd ff:ff:ff:ff:ff:ff
    # IP 地址
    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0
       valid_lft 86400sec preferred_lft 86400sec
    # 本地链路 IPv6 地址
    inet6 fe80::21a:2bff:fe3c:4d5e/64 scope link 
       valid_lft forever preferred_lft forever

# KVM/libvirt创建的默认虚拟网桥，用于NAT模式的虚拟机。
3: virbr0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    # MAC地址
    link/ether 52:54:00:ab:cd:ef brd ff:ff:ff:ff:ff:ff
    # 这是虚拟网络的网关地址
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever

# 连接到virbr0网桥上的一台虚拟机的虚拟网卡接口。
5: vnet1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master virbr0 state UNKNOWN group default qlen 1000
    # MAC 地址
    link/ether fe:54:00:11:22:33 brd ff:ff:ff:ff:ff:ff
    # 本地链路 IPv6 地址
    inet6 fe80::fc54:ff:fe11:2233/64 scope link 
       valid_lft forever preferred_lft forever
```

```shell
yan@yuehai-nas:~$ sudo cat /etc/netplan/*.yaml
[sudo] yan 的密码： 

# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
network:
  version: 2
  ethernets:
    enp4s0:
      dhcp4: true
yan@yuehai-nas:~$ 
```

3. 通过上面的命令，拿到了最核心的三个数据
	1. 物理网卡名称： `enp4s0`
	2. 当前 IP 地址： `192.168.1.100`
	3. 网卡 MAC 地址： `00:1a:2b:3c:4d:5e`，使用时请修改为自己的
4. 先备份网络配置

```shell
sudo cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
```

5. 使用 nano 打开配置文件

```shell
sudo nano /etc/netplan/50-cloud-init.yaml
```

6. 删掉里面的所有内容，替换为以下代码，然后保存

```shell
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp4s0:
      dhcp4: false
  bridges:
    br0:
      interfaces:
        - enp4s0
      dhcp4: true
      macaddress: 00:1a:2b:3c:4d:5e
```

7. 把配置文件的权限收紧：

```shell
sudo chmod 600 /etc/netplan/*.yaml
```

8. 安全应用配置，敲下回车后，会发生以下两种情况之一：
	1. 情况 A（极其顺利）： 远程桌面画面卡顿了 1-3 秒，然后马上恢复了，或者短暂断开然后很快又可以连上了。终端里提示你是否要保留配置并进入倒计时。此时只需要 按下回车键 (Enter)，配置就永久生效了！
	2. 情况 B（有惊无险）： 远程桌面断开，并且暂时连接不上了，120 秒后才能连接上。120 秒后，Ubuntu 会自动撤销刚才的配置，远程桌面就可以重新连上了。如果遇到这种情况，说明代码复制时缩进乱了，需要排查后重新应用

```shell
sudo netplan try
```

9. 成功时的提示，此时此时只需要 按下回车键 即可

```shell
yan@yuehai-nas:~$ sudo netplan try

Do you want to keep these settings?

Press ENTER before the timeout to accept the new configuration

Changes will revert in  39 seconds
Configuration accepted.
```


### ⑩、修改虚拟机网络为桥接

1. 打开虚拟机的虚拟硬件详情
2. 在左侧列表找到并点击 **NIC :xx:xx:xx (网卡)**
3. 在右侧的配置中：
	1. 网络源 (Network source)：在下拉菜单里选择 **桥接设备** (Bridge device)
	2. 设备名称 (Device name)：手动输入 `br0`
	3. 设备型号 (Device model)：保持 `virtio` 不变
4. 点击右下角的 应用 (Apply)
5. 修改完毕，此时在开启虚拟机即可

![|700](attachments/Pasted%20image%2020260401134530.png)

### ⑪、使用 qcow2 恢复虚拟机

1. 点击新建虚拟机

![|560](attachments/Pasted%20image%2020260401102555.png)

2. 选择：导入现有磁盘映像(E)

![](attachments/Pasted%20image%2020260401102610.png)

3. 选择想要恢复的虚拟机 qcow2 文件后，再选择对应的具体系统

![](attachments/Pasted%20image%2020260401102738.png)

4. 设置内存和 cpu 数，虚拟机运行时，并不会全部占用设置的数量

![](attachments/Pasted%20image%2020260401102801.png)

5. 创建信息确认
	1. 名称：随便起，比如 `windows_server_2016
	2. 一定要勾选 <font color="#ff0000">安装前自定义配置</font>
	3. 网络可以直接选择桥接模式，前提是宿主机已经修改为桥接
	4. 点击完成

![](attachments/Pasted%20image%2020260401102850.png)

6. 进入虚拟机安装前自定义配置后，同样是修改那三个地方：
7. 第一步：改 BIOS 为 UEFI
	1. 点击左侧列表最上面的 **概况** (Overview)
	2. 在右侧找到 **固件** (Firmware) 选项
	3. 从默认的 BIOS 改为 UEFI

![|700](attachments/Pasted%20image%2020260401102908.png)

8. 第二步：修改磁盘总线类型
	1. 点击左侧的 **SATA 磁盘 1**
	2. 把 **磁盘总线** (Disk bus) 改为 `VirtIO`，VirtIO 是 KVM 的半虚拟化直通技术，硬盘跑满速全靠它
	3. 此时应用后，左侧的 **SATA 磁盘 1** 会变成 **Virtlo 磁盘 1**

![|700](attachments/Pasted%20image%2020260401102928.png)

9. 第三步：修改网卡类型
	1. ，我是已经修改为桥接了没有桥接选择虚拟网络即可
	2. 点击左侧的 **NIC : xx:xx:xx**（网卡）
	3. 右侧 **网络源** 确定为是 **桥接设备**
	4. **设备型号** (Device model) 改为 `virtio`
	5. 点击应用

![|700](attachments/Pasted%20image%2020260401102955.png)

10. 修改完毕后，点击开始安装即可

## 4、使用 xrdp 开启远程桌面

### ①、安装 xrdp

#### Ⅰ、Ubuntu 中安装 xrdp

1. 更新软件源

```shell
sudo apt update
```

2. 在 Ubuntu 系统中安装远程桌面协议(Remote Desktop Protocol，RDP) 服务器程序 xrdp：

```shell
sudo apt install xrdp
```

3. 将 xrdp 用户加入 ssl-cert 用户组

```shell
adduser xrdp ssl-cert
```

4. 安装完成后启动 xrdp 程序：

```shell
sudo systemctl enable --now xrdp
```

5. 再执行下面的命令打开防火墙端口 3389

```shell
sudo ufw allow from any to any port 3389 proto tcp
```


### ②、连接 xrdp

#### Ⅰ、Windows 系统远程桌面连接

1. 在 Windows 系统中，首先点击搜索框，然后输入关键字 `remote`，再在搜索结果中点击“远程桌面连接”应用。

![|700](attachments/Pasted%20image%2020231225153003.png)

2. 在弹出的远程桌面连接的窗口中，先输入 Ubuntu 服务器的 IP 地址，然后点击“连接”按钮去连接服务器

![|700](attachments/Pasted%20image%2020231225153047.png)

3. 在随后弹出的登录界面中，需要先填入 Ubuntu 服务器的用户名和密码，然后再点击“OK”按钮

![|700](attachments/Pasted%20image%2020231225153111.png)

4. 没有问题的话，这样就可以登录进去了

### ③、问题记录

#### Ⅰ、Windows 远程连接后没有声音

> 1. pulseaudio-module-xrdp：xrdp 音频重定向模块，https://github.com/neutrinolabs/pulseaudio-module-xrdp/wiki/README
> 	1. v0.7 下载：[pulseaudio-module-xrdp-0.7.zip](attachments/pulseaudio-module-xrdp-0.7.zip)
> 2. pulseaudio-module-xrdp 依赖 pulseaudio：https://www.freedesktop.org/wiki/Software/PulseAudio/Download/
> 	2. 17.0 下载：[pulseaudio-17.0.tar.gz](attachments/pulseaudio-17.0.tar.gz)
> 3. 上面两个安装过程中会出现很多依赖的问题，善用 gpt 排查

##### （1）、pulseaudio 编译安装

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

##### （2）、pulseaudio-module-xrdp 编译安装

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

##### （3）、启动

1. 重新启动 PulseAudio：

```shell
# 关闭 PulseAudio
pulseaudio --kill

# 启动 PulseAudio
pulseaudio --start
```

2. 手动启动加载脚本：`/home/yan/apply/tools/pulseaudio-module-xrdp-0.7/instfiles/load_pa_modules.sh`
3. 此时在 设置 -> 声音 中，输入和输出设备应该都显示 `xrdp`

![](attachments/Pasted%20image%2020240326144331.png)

##### （4）、创建桌面文件 pulseaudio-xrdp.desktop

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

##### （5）、解决 pulseaudio 警告

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

#### Ⅱ、远程登录后弹出需要验证的窗口

1. 有时候登录后还弹出一个如下图所示的认证窗口，那么还需要再输入一次密码来认证，这样显得有点麻烦。

![|700](attachments/Pasted%20image%2020231225153514.png)

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

#### Ⅲ、画面卡顿

##### （1）、调整 Xrdp 配置参数

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

##### （2）、调整系统参数

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

#### Ⅳ、无法复制

1. 重启 xrdp 或是注销用户后重新登录可恢复功能

#### Ⅴ、远程登录后是黑屏状态

1. 如果远程登录后并没有出现 Ubuntu 桌面而是黑屏状态，那么可能是已经有用户登录进去了
2. 需要先把之前的用户退出来（Log Out），如果更直接一点就是重启 Ubuntu 系统

![|700](attachments/Pasted%20image%2020231225153222.png)


## 5、使用 `lastb` 查看登录失败尝试记录

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

## 6、使用 `fail2ban` 屏蔽 SSH 爆破

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
		4. `Currently banned`：当前没有任何 IP 被封禁。
		5. `Total banned`：至今没有 IP 被封禁。
		6. `Banned IP list`：显示已封禁的 IP 地址列表，此处为空。

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


## 7、`screen` 多重视窗管理程序

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
	4. 使用 `-S` 创建和直接输入 `screen` 创建的虚拟终端，不会检录之前创建的 `screen`，也就是会创建同名的 `screen`
	5. 使用 `-R` 创建，如果之前有创建唯一一个同名的 `screen`，则直接进入之前创建的 `screen`
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

## 8、

# 三、网络通信

## 1、使用 V2Ray 搭建 vpn

### ①、ubuntu 搭建 V2Ray 服务端

> 使用的野草云：https://my.yecaoyun.com/

1. 开放 `10010` 端口

![|388](attachments/Pasted%20image%2020241121100626.png)

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

### ②、使用 docker 部署 V2Ray 服务端
 
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

### ③、使用 docker 部署 V2Ray 客户端

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


### ④、手机端使用 V2Ray

> 软件下载：[v2rayNG_1.8.25.apk](attachments/v2rayNG_1.8.25.apk)

1. 打开软件，点击右上角 + 号

![|254](attachments/Pasted%20image%2020240627153200.png)

2. 选择：`手动输入[Vmess]`

![|229](attachments/Pasted%20image%2020240627153220.png)

3. 依照下面的图片填入内容：
	1. 地址：服务器的 ip 
	2. 端口：V2Ray 服务端的端口
	3. 用户 ID：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `settings.clients.id`
	4. 额外 ID：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `settings.clients.alterId`
	5. 传入协议：选择 `ws`，即 `WebSocket ` 协议
	6. path：之前配置文件 `/usr/local/etc/v2ray/config.json` 的 `streamSettings.wsSettings.path`

![|258](attachments/Pasted%20image%2020241121125059.png)

4. 点击右上角 `√` 号保存
5. 选择刚才创建的配置，点击连接即可

![|229](attachments/Pasted%20image%2020240627153020.png)

### ⑤、windows 端使用 V2Ray

> 软件下载：https://github.com/2dust/v2rayN/releases

1. 打开软件，点击左上角 `服务器` 按钮

![|625](attachments/Pasted%20image%2020240627153707.png)

2. 选择：`添加[Vmess]服务器`

![|625](attachments/Pasted%20image%2020240627153728.png)

3. 填入参数，内容与上面的手机端相同

![|625](attachments/Pasted%20image%2020240627153807.png)

4. 点击确定，即可使用，软件会自动连接

## 2、使用 mailutils 发送邮件

### ①、安装 mailutils

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

### ②、发送邮件

1. 使用 `mail` 命令发送邮件：

```shell
echo "测试邮件正文" | mail -s "测试邮件主题" -r yan@yuehai.fun 770717410@qq.com
```

2. `"测试邮件正文"`：邮件正文
3. `mail`：用于发送邮件
4. `-s "测试邮件主题"`：指定邮件的主题（标题）为：测试邮件主题
5. `-r yan@yuehai.fun`：指定邮件的发件人地址为 `yan@yuehai.fun`
6. `770717410@qq.com`：指定邮件的收件人地址为 `770717410@qq.com`

## 3、

# 四、论坛博客

# 五、文件相关

## 1、Syncthing 文件同步的使用

### ①、介绍

1. Syncthing 是跨平台的应用，可在 windows、linux、macOS、ios、android 等平台下载安装，可在不同设备之间同步文件
2. 因为在开发之际确实超前地考虑到全平台的通用性，因此采用了浏览器/服务器（B/S）架构以适应绝大多数操作系统和体系结构
3. Syncthing 的缺点是只能在不同设备之间同步文件，而不能在同一个设备的不同目录（硬盘）之间同步文件
4. 若想要在同一个设备的不同目录（硬盘）之间同步文件，可以使用下面的 FreeFileSync

### ②、基本使用

> 下载地址：https://syncthing.net/downloads/

1. 下载对应版本后解压
2. 进入解压目录，启动应用：`./syncthing`
3. 启动成功后，进入网址即可：`http://localhost:8384`

![|700](attachments/Pasted%20image%2020240624160538.png)

4. 先点击添加远程设备，设备 ID 点击右上角操作 -> 显示设备 ID 获取；设备之间要互相绑定才可以
5. 再点击添加文件夹，<font color="#ff0000">文件夹 ID</font> 必须唯一，不同设备间根据 <font color="#ff0000">文件夹 ID</font> 进行同步
6. 添加完文件夹后，需点击共享，选择想要同步该文件夹的设备，点击保存即可开始同步

![|700](attachments/Pasted%20image%2020240624161051.png)

### ③、设置开机自启

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

### ④、关闭开机自启

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

### ⑤、使用 HTTPS 连接到 GUI

#### Ⅰ、开启使用 HTTPS 连接到 GUI

1. 点击：操作 -> 设置 -> GUI，勾选使用 HTTPS 连接到 GUI，点击保存

![|675](attachments/Pasted%20image%2020241101104348.png)

2. 然后重启服务，重启完成后，重新访问主页
3. 但是此时会显示：您的连接不是私密连接
4. 点击高级然后选择：继续前往127.0.0.1（不安全），可以进入主页

![|450](attachments/Pasted%20image%2020241101104647.png)

5. 但是每次都这样选择太麻烦了，我们可以将 syncthing 自签的证书换成我们自己的，这样就不会有这个提示了

#### Ⅱ、替换证书

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

3. 将 `/etc/letsencrypt/archive/www.yuehai.fun/` 下的证书文件复制到当前目录，来替换 `https-cert.pem` 和 `https-key.pem`

```shell
sudo cp /etc/letsencrypt/archive/www.yuehai.fun/cert1.pem ./https-cert.pem
sudo cp /etc/letsencrypt/archive/www.yuehai.fun/privkey1.pem ./https-key.pem
```

4. 修改生成的文件的用户组：

```shell
# 修改用户组：
sudo chown yan:yan https-cert.pem https-key.pem
```

5. 重启服务，再次进入就不会有提示了

### ⑥、配置目录单向备份（仅新增）

#### Ⅰ、仅新增说明

1. 有 A、B 两个设备，A 设备产生新数据，B 设备用于数据备份
2. 我想要 A 设备指定目录中的所有数据都同步到 B 设备中，而且同步完之后，当 A 设备中删除数据后，B 设备中仍然保留，不会删除
3. 即仅新增 B 设备中没有的文件

#### Ⅱ、设置仅新增

> 官方对这个选项的解释：[IgnoreDelete](https://docs.syncthing.net/advanced/folder-ignoredelete.html#ignoredelete)

1. 点击操作 -> 高级

![|700](attachments/Pasted%20image%2020241120185037.png)

2. 在弹窗中选择文件夹 -> 想要设置为仅新增的文件夹

![|700](attachments/Pasted%20image%2020241120185309.png)

3. 在打开的选项中，勾选 `Ignore Delete`；需要注意的是，这个选项只是忽略了删除命令，当文件被覆盖时，可能会引起旧文件的丢失。所以建议与版本控制一同使用，以防万一。

![|700](attachments/Pasted%20image%2020241120185558.png)

4. 在最下方点击保存：

![|700](attachments/Pasted%20image%2020241120185612.png)

5. 设置完毕

## 2、FreeFileSync 文件同步的使用

### ①、介绍

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

### ②、下载解压

1. 官网：https://freefilesync.org/download.php

![|675](attachments/Pasted%20image%2020240718092505.png)

2. 下载完成后，使用 tar 命令提取：

```shell
tar -xvf FreeFileSync_13.7_Linux.tar.gz
```

3. 会生成 `FreeFileSync_13.7_Install.run` 文件

### ③、安装

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

![](attachments/Pasted%20image%2020240718093931.png)

7. 绿色的 `FreeFileSync` 是 FreeFileSync 主程序
8. 红色的 `RealTimeSync` 是自动同步程序，启动后，若指定目录中的文件发生变化，则会执行对应脚本

### ④、使用 FreeFileSync 同步文件

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

![|700](attachments/Pasted%20image%2020240718124000.png)

3. 打开过滤器，在排除项中加入以下内容：
	1. 因为是将 FreeFileSync 和 Syncthing 结合使用，所以同步的目录中有 Syncthing 创建的目录
	2. 这里是将 Syncthing 创建的目录排除掉

```shell
*/.stfolder*
*/.stfolder/*
*/.stversions/*
```

![|700](attachments/Pasted%20image%2020241119162520.png)

4. 点击同步设置，改为镜像模式：
	1. 因为多端文件的同步使用的是 Syncthing，FreeFileSync 只是作为文件备份工具来使用，所以使用镜像模式
	2. 四种模式的区别请参照第一节

![|700](attachments/Pasted%20image%2020240718130803.png)

5. 关于上面的使用数据库文件来检测变化的作用：
	1. 当启用使用数据库文件的选项时，FreeFileSync 会创建一个数据库来记录文件和文件夹的状态信息。这些信息包括文件的大小、修改时间和其他元数据。通过这种方式，每次同步时 FreeFileSync 只需要比较当前文件状态与数据库中记录的状态，从而确定哪些文件发生了变化。这种方法的优势包括：
		1. 效率更高：比较过程只需对比数据库中的记录与当前状态，不需要对整个文件内容进行扫描，从而提高同步的效率。
		2. 减少资源消耗：减少了对磁盘的读写操作，尤其是在文件数量庞大的情况下。
		3. 改进的变化检测：能够更精确地识别出哪些文件确实发生了变化，即使文件修改时间没有更新。
	2. 如果不使用数据库文件，FreeFileSync 将直接比较源和目标文件夹中的文件。这通常涉及到比较文件的大小、修改时间等属性。这种方法的特点包括：
		4. 简单直接：不需要额外创建和维护数据库文件，操作更为直接。
		5. 可能的性能开销：在没有数据库辅助的情况下，每次同步可能需要更多的时间和计算资源，特别是文件数量多或文件大小大的情况下。
		6. 适用性：对于较小的或不经常变化的文件集，这种方法可能更加高效。
	3. 总的来说，选择使用数据库文件还是不使用，取决于具体需求、文件数量以及同步频率。使用数据库可以显著提高大规模文件同步的效率和准确性，但如果同步任务不频繁或文件数量较少，直接比较也是一个有效的选择。
6. 点击浏览可以选择同步的目录：
	4. 左边的目录是原始目录，右边的目录是目标目录
	5. 当左边的目录中的内容发生变化时，会将变化同步至右边的目录中
	6. 具体的同步细节再上面的同步设置中
	7. 可以选择多个目录，也可以一对多

![|700](attachments/Pasted%20image%2020240718131152.png)

7. 此时点击同步按钮即可开始同步

![|700](attachments/Pasted%20image%2020240718131527.png)

8. 点击保存可以将本次的设置保存下来，以便下次使用

![|700](attachments/Pasted%20image%2020240718131619.png)

### ⑤、使用 RealTimeSync 自动同步文件

1. 点击绿色的 `FreeFileSync` 打开软件
2. 先选择刚才保存的配置，然后点击上方的另存为批处理作业

![|700](attachments/Pasted%20image%2020240718131908.png)

3. 可以选择以最小化运行以及忽略错误，点击另存为保存

![|700](attachments/Pasted%20image%2020240718132037.png)

4. 点击红色的 `RealTimeSync` 打开软件
5. 首先选择要监视变化的目录，一般和上面选择同步的原始目录相同
6. 然后填入检测到变化后要执行的命令行，此处填入 FreeFileSync 安装路径及程序，后面以刚才保存的批处理作业的路径为参数

```shell
/home/yan/apply/file/FreeFileSync/FreeFileSync /home/yan/apply/file/FreeFileSync/sava/SyncSettings.ffs_batch
```

![|700](attachments/Pasted%20image%2020240718132846.png)

7. 最后的选项运行命令之前最小的空闲时间（以秒计），表示如果监测到了目录中的内容发生了变化，延迟执行命令的时间
8. 点击开始，即可启动后台任务，当程序监测到了目录中的内容发生了变化，就会执行同步操作

### ⑥、关闭 RealTimeSync 自动同步任务

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

### ⑦、同步日志记录脚本

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

![|700](attachments/Pasted%20image%2020241119165725.png)

### ⑧、定时执行同步任务

#### Ⅰ、说明

1. 使用定时执行同步任务，而不是上面使用 RealTimeSync 检测到文件变动就自动同步的原因是：如果 Syncthing 和 FreeFileSync 配合使用，当 RealTimeSync 检测到文件变动时会锁住文件，这时 Syncthing 就不能对文件进行操作了，只能生成很多副本，要手动删除，很麻烦，而且有时会导致同步混乱，数据出问题
2. 所以现在的解决方案是，先使用 Syncthing 将文件同步到路径 A，然后选择一个基本不会对文件进行修改的时间（比如凌晨 2 点），调用 FreeFileSync 进行同步
3. 这样时间错开，也就不会出现文件被锁住，同步出问题的情况了

#### Ⅱ、为什么要使用 XVFB 模拟 X 环境

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

#### Ⅲ、安装 XVFB 模拟 X 环境

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
 
#### Ⅳ、编写脚本，将 XVFB 与 FreeFileSync 一同运行

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

3. 将 XVFB 与 FreeFileSync 整合到脚本，在启动 XVFB 后自动运行 FreeFileSync：

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

#### Ⅴ、设置定时任务运行脚本

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

### ⑨、以管理员权限启动 FreeFileSync

1. 如果在本地机器上运行，确保当前用户有权访问 X 服务器。这可以通过 xhost 工具管理。可以临时允许所有用户访问 X 服务器（注意这有安全风险）

```shell
xhost +
```

2. 如果在图形界面环境中直接运行命令且遇到权限问题，可以尝试使用 gksudo 或 pkexec 而不是 sudo 来运行图形界面应用，因为 sudo 可能不会传递必要的环境变量；要使用应用的全路径：

```shell
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY /home/yan/apply/file/FreeFileSync/FreeFileSync
```

3. 执行后，会提示输入密码，输入当前用户的密码即可

### ⑩、FreeFileSync 备份 docker 应用时备份失败的应用记录

#### Ⅰ、报错

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

#### Ⅱ、原因

1. 有的应该是尝试访问的对象是不支持操作的类型，如 socket 文件
	1. `qbittorrent/config/qBittorrent/ipc-socket`
2. 有的应该是容器在运行，被容器占用，所以直接复制不行
	2. 比如以 `tmp` 结尾的文件
3. 还有的是目录带有特殊符号，无法直接创建目录、复制目录
	1. `/nextcloud/data/appdata_ocuun68rg8dx/appstore/app-discover-cache/"675fbad9-77d"`
	2. `/homeassistant/config/.storage/xiaomi_miot/urn:miot-spec-v2:device:air-conditioner:0000A004:lumi-mcn02:1.json`

#### Ⅲ、报错应用记录

> 有的报错应该是容器在运行，所以直接复制不行

1. Home Assistant 智能家居平台：
	1. `/homeassistant/config/`
2. mysql 数据库：
	2. `/mysql/data/`
3. nextcloud 自托管云存储和协作平台：
	1. `/nextcloud/data/`
4. nginx-proxy-manager-zh 基于 Nginx 的反向代理管理工具
	2. `/nginx-proxy-manager/data/`
5. qbittorrent BitTorrent 客户端
	1. `/qbittorrent/config/`
6. qinglong 青龙定时任务管理
	2. `/qinglong/data/`
7. xunlei 迅雷群晖提取版
	1. `/xunlei/data/`

#### Ⅳ、备份 docker 应用时的排除

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


## 3、smartmontools 硬盘检测

> 1. smartmontools 是一组工具，用于监控和管理硬盘驱动器和固态硬盘的健康状况，主要包含两个工具：smartctl 和 smartd
> 2. 它们帮助用户通过 SMART（Self-Monitoring, Analysis, and Reporting Technology）获取硬盘信息，检测潜在问题，防止数据丢失

### ①、smartmontools 的主要功能

1. 硬盘健康状况监控：获取硬盘的健康状态、SMART 属性、错误日志等。
2. 执行自检测试：运行短期或长期自检来评估硬盘是否存在潜在故障。
3. 错误日志查看：检查硬盘的错误历史记录，查看是否有错误发生。
4. 自动监控服务：使用 smartd 作为后台服务，定期监控硬盘健康状况并发送通知。
5. 温度监控：查看和监控硬盘温度，预防温度过高造成的硬盘损坏。
6. 支持多种接口：支持 IDE/ATA、SATA、SCSI、NVMe、USB、RAID 等不同接口的存储设备。

### ②、smartctl 命令

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

### ③、smartd 命令

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

### ④、smartmontools 其他常用命令

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

### ⑤、提示未知 USB 桥接器 Unknown USB bridge

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

### ⑥、开启 SMART 功能

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

## 4、samba 目录共享

1. 更新软件源：

```shell
sudo apt update
```

2. 安装 samba 服务

```shell
sudo apt install samba -y
```

3. 创建一个专门用于共享的文件夹：

```shell
sudo mkdir -p /mnt/public_share
sudo chmod 777 /mnt/public_share
```

4. 打开 samba 配置文件：

```shell
sudo nano /etc/samba/smb.conf
```

5. 用方向键一直拉到文件的最底部，新起一行，把下面这段粘贴进去：

```ini
[NAS-Share]
   comment = nas share
   path = /mnt/public_share
   browseable = yes
   read only = no
   guest ok = yes
   create mask = 0777
   directory mask = 0777
```

6. 重启服务强制生效：

```shell
sudo systemctl restart smbd
```

7. 在 Windows 电脑中，打开文件管理器，在顶部的路径地址栏输入 `\\192.168.1.5` 然后回车，就会看到一个名为 `nas_share` 的文件夹

### ①、Windows 电脑无法连接

#### Ⅰ、报错现象

1. 其他设备可以连接
2. Windows 电脑无法连接

#### Ⅱ、原因

1. 在 `smb.conf` 配置中，写了 `guest ok = yes`（允许匿名访客直接读写）
2. 但微软为了防范勒索病毒，在较新版本的 Windows 10/11 中，默认封杀了所有的 SMB 匿名共享访问（Insecure Guest Logons）
3. 也就是说，哪怕服务器允许你不输密码直接进，Windows 也会认为这太危险而强行掐断连接，从而报出 Windows 无法访问 的错误

#### Ⅲ、解决

1. 按键盘上的 Win + R，输入 `gpedit.msc` 并回车，打开 本地组策略编辑器
2. 依次在左侧展开寻找路径：
3. 计算机配置 -> 管理模板 -> 网络 -> Lanman 工作站 (Lanman Workstation)
4. 在右侧找到策略：启用不安全的来宾登录 (Enable insecure guest logons)
5. 双击它，将其改为 已启用 (Enabled)，然后点确定
6. 再次在资源管理器里输入 `\\192.168.1.5` 即可

![](attachments/Pasted%20image%2020260617105939.png)

### ②、Debian XFCE 桌面无法连接

#### Ⅰ、报错现象

1. 其他设备可以连接
2. Debian XFCE 桌面无法连接无法连接

![|700](attachments/Pasted%20image%2020260617123257.png)

![|700](attachments/Pasted%20image%2020260617123555.png)

#### Ⅱ、原因

1. 当在地址栏只敲 `smb://192.168.1.5/` 时，Linux 的文件管理器试图以匿名身份向服务器请求：请告诉我你都有哪些共享文件夹（拉取列表）
2. 但较新的 Samba 服务端出于安全策略，拒绝匿名读取目录列表，于是 Linux 文件管理器直接罢工，甩出了无效的参数报错
3. 既然已经知道文件夹的确切名字了，解决办法很简单：不要让它去猜，直接把车开进车库

#### Ⅲ、解决

1. 在 Thunar 文件管理器的地址栏（按 Ctrl + L 唤出），不要只输入 IP，直接将最终的文件夹名称拼在后面，输入：

```shell
smb://192.168.1.5/nas_share
```

2. 直接回车后，如果它依然弹出 需要认证 的框，请按如下方式改写：
	1. 用户名(U)： 填 `anonymous`
	2. 域(D)： 保持 `WORKGROUP`
	3. 密码(P)： 绝对留空
	4. 点击连接

## 5、使用 sftp 命令从 linux 服务器下载文件

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

## 6、解压与压缩 zip 文件

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


## 7、

## 8、

# 六、自动脚本

# 十、媒体娱乐

# 十一、生活消费

# 十二、生产力工具

# 二十、docker

## 1、docker 安装配置

### ①、安装 docker

1. 如果之前可能装过其他来源的 Docker，先运行此命令进行一次彻底的清理：

```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

2. 安装依赖，确保 apt 可以通过 HTTPS 使用软件源：

```shell
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common lsb-release -y
```

3. 添加 Docker 官方的 GPG 密钥（数字签名）：

```shell
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

4. 添加 Docker 的软件源地址：

```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. 更新软件源：

```shell
sudo apt update
```

6. 安装 docker 标准最小化三件套：
	1. `containerd.io`：真正运行和管理容器的底层核心组件，负责所有基础工作
	2. `docker-ce`：作为后台服务运行，提供了完整的 Docker API，并指挥 `containerd.io`
	3. `docker-ce-cli`：输入的 docker 命令本身，用来向 `docker-ce` 下达指令

```shell
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

7. 将当前用户添加到 docker 用户组：

```shell
sudo usermod -aG docker $USER
```

### ②、配置 docker 数据目录

1. 在想要存放数据的硬盘里建一个专门的文件夹：

```shell
sudo mkdir -p /mnt/data/docker/root
```

2. 新建 Docker 的核心配置文件：

```shell
sudo nano /etc/docker/daemon.json
```

3. 编写配置

```json
{
  "data-root": "/mnt/data/docker/root",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "20m",
    "max-file": "3"
  }
}
```

4. 重启 Docker 服务让新路径生效：

```shell
sudo systemctl restart docker
```


### ③、配置自定义网络的网段

> 1. 为什么要配置网段：Docker 默认使用 `172.17.0.0/16` 及后续网段，极易与公司内网、VPN 或云服务器的 VPC 网段发生重叠
> 2. 这会导致 路由黑洞，例如 SSH 突然断开或无法直连宿主机
> 3. 需要将其全局限制在一个安全的、未被占用的可用网段池中，例如 `172.31.0.0/16`

1. 编辑 Docker 的核心配置文件：

```shell
sudo nano /etc/docker/daemon.json
```

2. 加入网段配置：
	1. `bip`：强制指定 Docker 默认 `docker0` 网桥的 IP 地址与子网掩码
	2. `default-address-pools`：限制后续使用 `docker compose` 或 `docker network create` 创建自定义网络时，只能从该安全池子里按 `/24` 切分网段

```json
{
  "bip": "172.31.0.1/24",
  "default-address-pools": [
    {
      "base": "172.31.0.0/16",
      "size": 24
    }
  ]
}

```

3. 重新加载 systemd 守护进程配置：

```shell
sudo systemctl daemon-reload
```

4. 重启 Docker 服务让网段新规生效：

```shell
sudo systemctl restart docker
```

5. 如果是在已经运行了一段时间的机器上补齐此配置，重启 Docker 后还需清理历史遗留的冲突网络：

```shell
# 清理前需确保冲突网络上的容器已停止或已移除
sudo docker network prune -f
```

### ④、

### ⑤、

## 2、

# 二十一、自部署服务

# 三十、安卓工具

# 九十九、其他软件

