# 一、系统安装

## 1、LineageOS

1. 应确认索贝已经解锁 Bootloader 
2. 确定 LineageOS 所需的原厂底层固件，比如 LineageOS 20261019 要求的是 Android 16 原厂底层固件

### ①、设备信息

| 项目           | 内容                                  |
| ------------ | ----------------------------------- |
| 手机           | 一加 Ace 3，国行 PJE110                  |
| LineageOS 代号 | `astonc`                            |
| 电脑           | Windows、PowerShell                  |
| 原厂恢复工具       | 欧加真 Fastboot 线刷工具 v7.3.1            |
| 原厂恢复包        | `PJE110_16.0.5.1002(CN01)-F.31.zip` |
| 目标系统         | LineageOS 24.0，Android 17           |
| 系统版本         | `20261019-NIGHTLY-astonc`           |
| Google 服务    | MindTheGapps 17.0.0，ARM64           |
| 最终结果         | 系统与 GApps 安装成功，正常进入系统               |

### ②、下载文件

1. LineageOS 官方下载页：https://download.lineageos.org/devices/astonc
2. 下载指定版本下提供的所有文件
3. GApps 下载页：https://github.com/MindTheGapps/17.0.0-arm64/releases/tag/MindTheGapps-17.0.0-arm64-20261022_132445
4. LineageOS 24 是 Android 17，因此 GApps 使用 17.0／ARM64 手机版本，不是 Android 16，也不是 ATV 电视版本

### ③、刷入启动与 Recovery 镜像

1. 原厂系统开启 USB 调试，授权电脑后进入 Bootloader Fastboot：

```shell
adb devices
adb -d reboot bootloader
fastboot devices
```

2. 刷入六个镜像：

```shell
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash init_boot init_boot.img
fastboot flash vbmeta vbmeta.img
fastboot flash vendor_boot vendor_boot.img
fastboot reboot bootloader
fastboot flash recovery recovery.img

fastboot wipe-super super_empty.img
```

2. 每条命令确认成功，没有 FAILED
3. 用手机 Bootloader 菜单进入 Recovery
4. 确认是 Lineage Recovery，本次版本为：`24.0 (20261019)`

### ④、安装 LineageOS

1. 手机选择：

```shell
Apply update
→ Apply from ADB
```

2. 电脑执行：

```shell
adb -d sideload "lineage-24.0-20261019-nightly-astonc-signed.zip"
```

3. 等待手机完成：

```shell
Step 1/2
Step 2/2
```

4. 以手机端最新的成功结果为准，电脑进度停在约 47% 不一定失败
5. 系统安装完成后，手机提示：

```shell
To install additional packages, you need to reboot recovery first.
Do you want to reboot to recovery now?
```

6. 为了接着安装 GApps，选择 `Yes` 
7. 如果不想安装 GApps，可以选择 `No`

### ⑤、安装 Google Play 与 Google 服务

1. 重新进入 Recovery 后，选择：

```shell
Apply update
→ Apply from ADB
```

2. 电脑执行：

```shell
adb -d sideload "MindTheGapps-17.0.0-arm64-20261022_132445.zip"
```

3. 若手机出现提示：

```shell
Signature verification failed
```

4. 并询问是否继续安装，确认使用的是上述官方来源、完整的安装包后，选择 `Yes`
    1. MindTheGapps 不是使用 LineageOS 官方密钥签名，因此附加包出现这个确认提示属于预期情况
    2. 这个 `Yes` 是允许继续安装，与前面重启 Recovery 的 Yes 是两回事。不要因此关闭全局验证，也不要对来源不明的包随意放行
5. 等待实际安装完成后，返回主菜单选择：

```shell
Reboot system now
```

6. 等待首次启动，完成初始化

### ⑥、问题记录

#### Ⅰ、LineageOS 安装 Error 7

##### （1）、报错现象

1. 系统安装在 Step 1/2 中止：

```shell
Error applying update: 7 (ErrorCode::kInstallDeviceOpenError)
Error in /sideload/package.zip (status 7)
Installation aborted.
```

2. 日志中的直接错误：

```shell
Attempting to create duplication partition with name: odm_b
Cannot add partition odm_b to group oneplus_dynamic_partitions_b
```

##### （2）、原因

1. 安装器准备 B 槽布局时发生 odm_b 重名冲突
2. 对本机导出的动态分区元数据检查发现：
    1. 校验和正常
    2. 多个原厂 A 槽分区归入 default 组
    3. 预期的 OnePlus 分区组没有对应成员
3. 这与安装器按分区组清理后仍出现重名的现象吻合
4. 没有证据证明闪存硬件损坏，也不能确定由线刷工具的哪条操作造成

##### （3）、解决

1. 在 fastbootd 使用匹配的官方空布局重建 super：

```shell
fastboot wipe-super super_empty.img
fastboot reboot recovery
```

2. 然后重新侧载 LineageOS，安装成功

### ⑦、


## 2、

## 3、

## 4、


# 二、用户和密码

# 三、用户登录

# 四、端口设置

# 五、系统设置

## 1、刷入面具修补镜像 init_boot

1. 在手机 Magisk 首页，点击 Magisk 卡片里的安装，选择：选择并修补一个文件
2. 选择手机系统的原始 `init_boot.img`，开始修补
3. 完成后会生成文件通常类似：`magisk_patched-xxxxx_xxxxx.img`，将该文件复制到电脑中
4. 手机连接电脑，进入 Bootloader Fastboot

```shell
adb -d reboot bootloader
fastboot devices
```

5. 刷入 init_boot：

```shell
fastboot flash init_boot "magisk_patched.img"
```

6. 确认输出成功、没有 FAILED 后重启手机：

```shell
fastboot reboot
```


## 2、

## 3、

## 4、

# 六、命令使用

## 1、修改 adb 端口号

1. 授予 root 权限

```shell
su
```

2. 强行打开 5555 端口并重启底层 ADB 守护进程

```shell
setprop service.adb.tcp.port 5555
stop adbd
start adbd
```


# 七、配置脚本

# 八、

# 九、问题记录


# 十、硬件驱动

# 十一、

# 十二、

# 十三、

# 十四

# 十五、类原生

## 1、无法设置铃声

### ①、问题

1. 该问题出现在 Android15+ 的系统上
2. 在提示音和震动中，比如手机铃声点击添加铃声
3. 在点击确定按钮之前，点击新添加的项目，播放的声音是正常的
4. 但是在点击确定之后，重新点击再听，就是一个默认的声音了
5. 并且这时有电话打入，声音也是这个默认的声音

### ②、原因

1. 权限问题
2. 简单来说，当通过 + 添加某个文件夹（比如下载文件夹）选择一个声音文件时，系统只是得到了一个**临时通行证**来播放它，所以在确定前试听是正常的
3. 但是，当点击**确定**后，由于安卓现代版本的隐私和权限管理（作用域存储），系统设置程序可能没有被授予永久读取那个文件夹的权限。当真正有通知或电话来时，系统再去寻找这个文件，却发现自己没有钥匙打不开那个文件夹的门，于是只能无奈地播放它自己能找到的默认铃声了

### ③、解决方法

1. 要彻底解决这个问题，需要把自定义的声音文件，放到系统专门用来存放铃声的公共目录里。这样做，系统就会给予它们最高的读取权限
2. 打开手机的文件管理器，在内部存储空间，即 `/storage/emulated/0` 中创建以下三个文件夹
	1. Alarms：用于存放闹钟铃声
	2. Notifications：用于存放通知提示音
	3. Ringtones：用于存放手机来电铃声
3. 创建完成后，将对应的铃声文件复制到对应的文件夹中，然后重启手机
4. 重启后，再次进入提示音和振动。这次，当点击**手机铃声**或**默认通知提示音**时，不要再点击 + 号，应该可以直接在系统提供的列表里，直接看到并选择刚才复制的声音了

### ④、解决方法 2：放入系统目录

> 使用 MiXplorer 文件管理器进行的操作，需要 root 权限

1. 确认已经给与 MiXplorer root 权限
2. 进入 MiXplorer，打开设置，点击高级，勾选  Root 权限

![|254](attachments/Pasted%20image%2020250827142434.png)

3. 进入根目录，确认当前模式是 RW，若不是，点击菜单进行修改

![|254](attachments/Pasted%20image%2020250827142545.png)

4. 进入媒体文件所在目录：
	1. `/system/product/media/audio/`：较新的系统
	2. `/system/media/audio/`：较旧的系统
5. 在这个目录下，应该会看到 `alarms`、`notifications`、`ringtones` 这三个文件夹，它们分别对应着系统自带的**闹钟**、**通知**和**来电铃声**
6. 将对应的铃声文件复制到对应的目录中，然后将复制文件的权限都改为 `644`
7. 完成所有操作后，为了系统安全，可以再通过文件管理器的挂载功能，将系统分区恢复为 **只读 (RO)** 状态
8. 重启手机

![|254](attachments/Pasted%20image%2020250827143136.png)

## 2、手机时间不准、网页显示证书日期无效

### ①、报错现象

1. 安卓类原生手机某次重启后时间不准、访问网页显示证书日期无效

![|219](attachments/Pasted%20image%2020260708153732.png)

### ②、原因

1. 为什么重启后时间不准？
	1. 原因：NTP 被墙
	2. 类原生的固有设定： 类原生系统在开机时，由于硬件实时时钟 RTC 可能存在微小硬件漂移或在彻底断电/重启时重置，系统需要立即通过网络进行对时
	3. 致命的默认服务器： 它们默认配置的网络时间协议 NTP 服务器通常是谷歌时间服务器 `time.android.com`
	4. 网络阻断： 在国内网络环境下，这个域名由于不可抗力阻断，导致手机开机后无法完成时间同步。系统只能回退到上一次关机时记录的时间，或者直接回滚到一个极早的基准时间，如 ROM 编译时间甚至 Unix 时间戳元年
2. 为什么访问网页显示证书日期无效？（信任链失效）
	4. 在建立 HTTPS 安全连接时，浏览器会对目标网站 SSL 证书进行时效性校验
	5. 证书中硬编码了两个时间指针：生效时间 NotBefore 和 失效时间 NotAfter
	6. 安全验证要求：`NotBefore ≤ 手机系统当前时间 ≤ NotAfter`
	7. 当手机系统时间因为无法对时而严重滞后，比如回退到了 2024 年或更早，而网站证书是在 2025/2026 年刚刚颁发的，浏览器会判断该证书尚未生效或已经过期，从而出于安全防范拦截连接，抛出 证书日期无效 ERR_CERT_DATE_INVALID 的警告

### ③、解决

1. 手机打开 USB 调试，连接电脑，打开电脑的 cmd，输入以下指令：

```shell
# 1. 验证设备是否在线（若显示设备序列号则说明连接成功）
adb devices

# 2. 查询当前系统配置的 NTP 服务器（通常会返回 time.android.com）
adb shell settings get global ntp_server

# 3. 将 NTP 服务器修改为国内极速响应的阿里云/腾讯云时间源
adb shell settings put global ntp_server ntp.aliyun.com

# 4. （可选）部分类原生 ROM 拥有备用 NTP 选项，一并将其修改
adb shell settings put global ntp_server_2 ntp.tencent.com

# 5. 触发系统立即进行时间同步测试
adb shell cmd network_time_update_service force_refresh
```


## 3、

## 4、


# 十六、

# 十七、

# 十八、

# 十九、

# 二十、




