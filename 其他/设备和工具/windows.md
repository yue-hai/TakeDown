# 一、系统安装

# 二、用户和密码

## 1、设置账号为空密码

1. 右键我的电脑，选择管理

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023091142.png)

2. 点击计算机管理 -> 系统工具 -> 本地用户和组 -> 用户

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023091703.png)

3. 选择想要设置的用户（比如 yan），右键选择设置密码，弹窗选择继续

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023091806.png)

4. 在弹出的弹窗中，不输入任何内容，直接点击确定

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023091917.png)

5. 完成

## 2、

# 三、用户登录

## 1、开启远程桌面及相应操作

### ①、开启远程桌面

1. 设置中搜索远程，点击远程桌面设置

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085625.png)

2. 进入后，点击启用远程桌面，在弹出的弹窗中点击确认

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085638.png)

3. 同一个页面中，点击下方的 选择可远程访问这台电脑的用户

![|675](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085737.png)

4. 点击添加

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085810.png)

5. 点击高级

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085830.png)

6. 点击立即查找，在下方出现的列表中选择想要使用远程桌面的用户，点击确定
	1. 之后进行远程桌面的使用时，账号和密码就是现在选择的这个用户的账号和密码

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806085857.png)

7. 再次点击确定即可

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806090103.png)

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250806090116.png)

### ②、远程桌面时打开远程设备的任务管理器

1. 方法 1：按 `Ctrl + Alt + End` 或 `Ctrl + Alt + Esc`
2. 方法 2：按 `Win + R`，然后输入 `taskmgr.exe`，最后按 `Enter` 键


## 2、允许使用空密码的账号进行远程登录

1. `win + r` ，弹出运行窗口，输入：`secpol.msc`，打开本地安全策略

![|394](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023092257.png)

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023092314.png)

2. 选择安全设置 -> 本地策略 -> 安全选项

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023092411.png)

3. 拉到最后，选中倒数第四个：帐户：使用空密码的本地帐户只允许进行控制台登录

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023092541.png)

4. 双击打开，选择已禁用，点击应用，然后点击确定即可

## 3、本地登录时提示：引用的帐户当前已锁定，且可能无法登录

### ①、管理员账户可登录

1. 登录管理员账户
2. 右键点击此电脑，然后点击管理

![|305](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912084203.png)

3. 选择：系统工具 -> 班底用户和组 -> 用户，选择被禁止登录的用户，双击打开

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912084600.png)

4. 将账户已锁定取消勾选，点击应用，然后点击确定即可；我这里显示点不了是因为使用的不是管理员账户，管理员账户没有这个问题

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912084632.png)

5. 重新登录该用户即可

### ②、管理员账户不可登录

1.  按住 Shift 键 ，点击右下角电源按钮，然后点击：重启，进入 Windows 高级启动选项界面

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912084936.png)

2. 选择：疑难解答

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085042.png)

3. 选择：高级选项

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085053.png)

4. 选择：命令提示符，进入命令提示符界面

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085102.png)

5. 输入 `net user` 列出当前计算机的所有账户，根据下面的图片可以看到有一个 `Administrator` 账户

```shell
net user
```

6.  然后输入 `net user Administrator /active:yes`激活 `Administrator` 账户
	1. 这条命令的作用是将 `Administrator` 账户设置为活动状态，使其可以登录到Windows系统。
	2. 通常，系统默认情况下，`Administrator` 账户是禁用的，以增加系统的安全性

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085240.png)

7. 命令执行完成后，关闭命令提示符界面
8. 点击：继续，正常启动计算机后，再次使用正确的密码就可以正常登录了

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085416.png)

## 4、更改登录尝试失败后的锁定持续时间

1. `Windows + R` 打开运行，输入 `secpol.msc` 后点击确定，打开本地安全策略窗口

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912085926.png)

2. 第一个选项：允许管理员帐户锁定，建议关闭，这样普通用户的账号被锁定后，可以登录管理员账号解锁；<font color="#ff0000">但是这样做最好设置管理员账号禁止远程登录</font>

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240912090217.png)

3. 第三个选项：账户锁定阈值，若是永远不想让账户被锁定，将其改为 0 即可
4. 第二、四个选项根据个人喜好设置

## 5、开启电脑网络唤醒

> 这里以华硕主板为例
> 
> wol 唤醒是通过网线将数据传输到主板从而进行唤起计算器，所以是一定要将一根网线连接到电脑，并且使用连接网线的这个网卡上网
> 
> 华硕官方教程：https://www.asus.com.cn/support/faq/1045950/
> 
> 其他的详细教程，整理了一些常见问题：https://post.smzdm.com/p/amx025p4/

### ①、查看主板是否支持网络唤醒

1. 网络唤醒是需要硬件支持的，需要满足以下两点（绝大多数现今的电脑都能满足，除非你的电脑真的很老旧）：
	1. 使用支持 ATX 2.01 标准的电源；
	2. 主板需要支持 PCIE 2.2 标准：
2. 在 PCIE 2.2 标准之前，那些旧的主板上会有一个用于网络唤醒的接口（ WAKEUP-LINK header ）需要使用一个特殊的电缆线连接到网卡上才能实现网络唤醒。但是在 PCIE 2.2 标准开始，那些支持此项标准的主板和网卡就不再需要前面所说的网络唤醒电缆线了，因为待机时的电源是通过 PCIE 总线转发的。（参考自 Wiki：[Wake-on-LAN](https://en.wikipedia.org/wiki/Wake-on-LAN#Hardware_requirements)）
3. 也就是说，如果你设置了网络唤醒，你的电脑在睡眠（S3）、休眠（S4）或关机（S5）时，你的网卡还是会处于待机状态，那么此时网卡待机时所需要的电源就是由 PCIE 总线转发的。
4. 不同的主板对网卡待机的电源策略不同，并不是所有主板都支持网卡在睡眠（S3）、休眠（S4）或关机（S5）时处于待机（Standby）状态。
5. 因此我们在 BIOS 中查找 WOL 有关的设置时，往往需要到电源的相关选项中去寻找关于 WOL 的选项，其中的关键词有（参考自[少数派文章](https://sspai.com/post/67003)）：
	1. ACPI 
	2. PCIE 设备开机
	3. Automatic Power On
	4. Wake on LAN/WLAN
	5. Power Management
	6. Power On by Onboard LAN
	7. Power On by PCI-E Devices
	8. ......
6. 关于具体的主板型号，请自行百度了解，或者询问卖家客服

### ②、主板 BIOS 设置

1. 开机按住 F2 或者 <font color="#ff0000">DEL</font> 进入 bios，这是针对华硕主板，其它主板可以自行百度。
2. 切换语言-简体中文，进入高级设置（Advanced），找到：高级电源管理设置（APM Configuration）

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918133750.png)

3. 将 PCI-E 设备唤醒（Power On By PCI-E），设置为启用：Enabled

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918133933.png)

4. 保存退出，操作完成后计算机会自动开机，等待 2 秒开机。

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918134001.png)

5. 至此主板 BIOS 设置完毕，继续进行下面的设置

### ③、网卡设置

1. 右键我的电脑，选择管理

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918134318.png)

2. 找到网络设配器，找到自己的网卡，网卡是和 cpu 关联，一般是在最上面的，切记别选中带有 wifi 字样的，wol 唤醒是通过网线将数据传输到主板从而进行唤起计算器，所以要找到有线网络的网卡

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918134452.png)

3. 双击网卡打开属性面板，进入高级设置，找到唤醒魔包，将其启用

![|461](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918134947.png)

4. 再选择电源管理设置，勾选：允许这个装置唤醒计算机

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918135036.png)

### ④、关闭快速启动功能

1. 鼠标右键点击 Windows 开始菜单 ，并选择：电源选项

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918135400.png)

2. 在弹出来的设置页面中选择：其他电源设置

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918135509.png)

3. 在弹出来的控制面板页面中选择：选择电源按钮的功能

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918135654.png)

4. 在新的控制面板页面中，先点击：更改当前不可用的设置，然后<font color="#ff0000">取消勾选：启用快速启动</font>

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918135801.png)

5. <font color="#ff0000">点击保存更改</font>

### ⑤、查看本机 mac 地址、ipv4 地址

1. 右键开始菜单，选择运行，输入：cmd，打开命令行工具

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918140126.png)

2. 输入：`ipconfig/all` 查看本机相关网络参数，记录下网卡对应的物理地址（mac 地址）和 ipv4 地址，<font color="#ff0000">端口默认为 9</font>

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240918140544.png)

### ⑥、网络唤醒

> 需要设置都在同一个局域网才可以进行网络唤醒

1. 输入 mac 地址、ip 地址、端口号即可，可以使用下面的工具
2. 使用网站：https://www.depicus.com/wake-on-lan/woli
3. 或者 app：[WakeOnLan.apk](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/WakeOnLan.apk)
4. 或者自己实现代码：

```java
package com.yuehai.tool.tool;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 * Wake-on-LAN 工具类
 *
 * @author 月海
 * @date 2024/3/15 13:28
 * @description 使用 Wake-on-LAN 唤醒局域网内的电脑
 */
public class WakeOnLan {
    
    /**
     * 启动 Wake-on-LAN
     *
     * @throws IOException 发送数据包时可能抛出的异常
     */
    public void startWakeOnLan(String mac, String ip, int port) throws IOException {
        // 尝试发送魔术包
        wakeup(mac, ip, port);
    }
    
    /**
     * 发送魔术包以唤醒指定的设备
     *
     * @param mac 目标设备的 MAC 地址
     * @param ip 广播地址
     * @param port 端口号
     */
    private void wakeup(String mac, String ip, int port) throws IOException {
        // 将 MAC 地址字符串转换为 byte 数组
        byte[] macBytes = getMacBytes(mac);
        // 创建 byte 数组用于存放魔术包数据，6 个字节的广播地址 + 16 倍的 MAC 地址
        byte[] bytes = new byte[6 + 16 * macBytes.length];
        // 填充魔术包前 6 个字节为 0xFF，这是 Wake-on-LAN 协议规定的格式
        for (int i = 0; i < 6; i++) {
            bytes[i] = (byte) 0xff;
        }
        // 将 MAC 地址重复 16 次添加到魔术包数据中
        for (int i = 6; i < bytes.length; i += macBytes.length) {
            System.arraycopy(macBytes, 0, bytes, i, macBytes.length);
        }
        
        // 根据提供的 IP 地址创建 InetAddress 对象，这里可能会将域名解析为 IP 地址
        InetAddress address = InetAddress.getByName(ip);
        /*
            创建 DatagramSocket 对象用于发送数据包，这里不指定端口表示由系统随机分配端口
            使用 try-with-resources 语法，确保 DatagramSocket 资源在使用后自动关闭
         */
        try (DatagramSocket socket = new DatagramSocket()) {
            // 创建 DatagramPacket 对象，包含要发送的数据、长度、目标地址和端口
            DatagramPacket packet = new DatagramPacket(bytes, bytes.length, address, port);
            // 通过 DatagramSocket 发送数据包
            socket.send(packet);
        }
    }
    
    /**
     * 将 MAC 地址字符串转换为 byte 数组
     *
     * @param macStr MAC 地址字符串
     * @return MAC 地址的 byte 数组形式
     */
    private byte[] getMacBytes(String macStr) throws IllegalArgumentException {
        // 创建一个长度为 6 的 byte 数组，用于存储 MAC 地址的二进制形式
        byte[] bytes = new byte[6];
        // 将 MAC 地址字符串按照冒号或短横线分割成字符串数组
        String[] hex = macStr.split("([:\\-])");
        // 如果分割后的数组长度不等于 6，说明 MAC 地址格式不正确，抛出异常
        if (hex.length != 6) {
            throw new IllegalArgumentException("无效的 MAC 地址");
        }
        // 循环将每个十六进制字符串转换为 byte 值，存储到 byte 数组中
        try {
            for (int i = 0; i < 6; i++) {
                bytes[i] = (byte) Integer.parseInt(hex[i], 16);
            }
        } catch (NumberFormatException e) {
            // 如果转换过程中出现异常，表示 MAC 地址中包含非十六进制字符，抛出异常
            throw new IllegalArgumentException("解析 MAC 地址出错", e);
        }
        
        // 返回转换后的 MAC 地址 byte 数组
        return bytes;
    }
}
```

### ⑦、问题总结

#### Ⅰ、每天或每周总有时候无法网络唤醒

1. 看看有没有设置路由器定时重启
2. 在电脑关机时，若是路由器重启了，那么直到电脑再次开机之前，时无法网络唤醒的
3. 解决办法：关闭路由器的定时重启，或者选一个不会被影响的时间

#### Ⅱ、

## 6、


# 四、端口设置

## 1、查看指定进程的端口号

1. 打开任务管理器，选择详细信息，这次查看 QQ 的端口号，可以看到 PID 为 `8020`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231222101725.png)

2. 根据这个 PID 来查询其信息：`netstat -ano | find "8028"`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231222102248.png)

3. 其中第二列就是 QQ 这个进程使用的所有的端口号

## 2、想要允许你的电脑被此网络上的其他电脑和设备发现吗？

1. 当新安装系统时，电脑通知中会出现这个选项

![|675](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Snipaste_2024-09-14_10-01-27.png)

2. 若是此时没有选择允许，之后想要手动开启，可进行如下操作：
3. 点击设置 -> 网络和 Internet -> 网络和共享中心

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241112131333.png)

4. 再选择更改高级共享设置

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241112131416.png)

5. 将启用网络发现打开，然后点击保存更改即可

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241112131503.png)

## 3、重新获取新的动态 IP 地址

```PowerShell
# 去除网卡的动态IP地址
ipconfig /release

# 为网卡重新动态分配 IP 地址
ipconfig /renew
```

## 4、


# 五、系统设置

## 1、开机时默认启开小键盘（数字键盘）

1. 首先按 `win+R` 启动打开 `运行` ，弹出运行窗口后输入 `regedit`  按 `确定` 
2. 之后会弹出注册表编辑器，在这里我们打开：`计算机\HKEY_USERS\.DEFAULT\Control Panel\Keyboard`
3. 打开它后双击打开 `InitialKeyboardIndicators`，默认数值是 `2147483648`
4. 弹出编辑字符串，在数值数据中输入 `2`，单击确定；在这里 2 的意思是“默认启开小键盘

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530124920.png)

5. 设置完成后重启电脑即可

## 2、设置软件开机自启

### ①、使用当前用户的启动目录

1. 按 Win+R 打开运行窗口，输入 `shell:startup`，然后按回车
2. 会打开当前用户的启动目录：`C:\Users\[用户名]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
3. 将软件的快捷方式放入此目录即可
4. 若是这样设置之后不能开机自启，继续尝试下面的操作

### ②、使用所有用户的启动目录

1. 按 Win+R 打开运行窗口，输入 `shell:common startup`，然后按回车
2. 会打开所有用户的启动目录：`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
3. 将软件的快捷方式放入此目录即可
4. 若是这样设置之后不能开机自启，继续尝试下面的操作

### ③、使用任务计划程序

1. 按 Win+R 打开运行窗口，输入 `taskschd.msc`，然后按回车
2. 会打开任务计划程序（Task Scheduler）
3. 创建基本任务
4. 设置名称为：CopyQ Autostart
5. 触发器选择：计算机启动时
6. 操作选择：启动程序
7. 程序或脚本：浏览选择 copyq.exe 的完整路径
8. 完成设置
9. 若是这样设置之后不能开机自启，继续尝试下面的操作

### ④、使用注册表

1. 按 Win+R 打开运行窗口，输入 `regedit`，然后按回车
2. 导航到：`计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
3. 右键 -> 新建 -> 字符串值
4. 名称设为 "CopyQ"
5. 数据设为 copyq.exe 的完整路径
6. 若是这样设置之后不能开机自启，继续尝试下面的操作

### ⑤、设置环境变量

1. 将 copyq.exe 所在文件夹添加到系统环境变量 PATH 中

## 3、语言设置已经是中文，但设置内仍是英文

1. 打开控制面板
2. 选择：`控制面板\时钟和区域`，点击：更改日期、时间或数字格式

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125212.png)

3. 在弹窗中点击管理，然后点击：更改系统区域设置

![|461](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125309.png)

4. 在当前系统区域设置中，选择：**中文(简体，中国)**

![|415](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125432.png)

5. 点击确定，重启即可

## 4、某些软件显示字符为乱码

1. 打开控制面板
2. 选择：`控制面板\时钟和区域`，点击：更改日期、时间或数字格式

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125212.png)

3. 在弹窗中点击管理，然后点击：更改系统区域设置

![|461](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125309.png)

4. 在当前系统区域设置中，选择：**中文(简体，中国)**

![|415](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125432.png)

5. 查看下方的 `Beta 版` 是否勾选，若是勾选则`取消勾选`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240530125558.png)

6. 点击确定，重启即可

## 5、双系统时修改启动加载器显示名称

1. 使用管理员打开 cmd

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250811085034.png)

2. 输入命令查看 Windows 启动加载器详情：`bcdedit`

```PowerShell
C:\Windows\system32>bcdedit

Windows 启动管理器
--------------------
标识符                  {bootmgr}
device                  partition=\Device\HarddiskVolume1
path                    \EFI\Microsoft\Boot\bootmgfw.efi
description             Windows Boot Manager
locale                  zh-CN
inherit                 {globalsettings}
default                 {current}
resumeobject            {7711a715-75da-11f0-b0e8-90f261811765}
displayorder            {current}
                        {428b9c43-7501-11f0-9541-d5809271f2b2}
toolsdisplayorder       {memdiag}
timeout                 5

Windows 启动加载器
-------------------
标识符                  {current}
device                  partition=C:
path                    \Windows\system32\winload.efi
description             主用系统 windows 10 ltsc 2021
locale                  zh-CN
inherit                 {bootloadersettings}
recoverysequence        {945bde32-75da-11f0-8f22-aa33128f1ccf}
displaymessageoverride  Recovery
recoveryenabled         Yes
isolatedcontext         Yes
allowedinmemorysettings 0x15000075
osdevice                partition=C:
systemroot              \Windows
resumeobject            {7711a715-75da-11f0-b0e8-90f261811765}
nx                      OptIn
bootmenupolicy          Standard

Windows 启动加载器
-------------------
标识符                  {428b9c43-7501-11f0-9541-d5809271f2b2}
device                  partition=F:
path                    \Windows\system32\winload.efi
description             国产游戏 windows 10 ltsc 2021
locale                  zh-CN
inherit                 {bootloadersettings}
recoverysequence        {5e342cb9-7501-11f0-a6b1-d3805224f578}
displaymessageoverride  Recovery
recoveryenabled         Yes
isolatedcontext         Yes
allowedinmemorysettings 0x15000075
osdevice                partition=F:
systemroot              \Windows
resumeobject            {428b9c42-7501-11f0-9541-d5809271f2b2}
nx                      OptIn
bootmenupolicy          Standard

C:\Windows\system32>
```

3. description 字段就是在开机选择界面看到的名字，输入命令进行修改：

```shell
bcdedit /set {current} description "主用系统 windows 10 ltsc 2021"
```

## 6、双系统时修改默认系统和等待时间

1. `Windows + R` 打开运行，输入 `msconfig` 后点击确定，打开 系统配置 窗口
2. 切换到 引导 (Boot) 选项卡
3. 单击选中希望作为默认系统的那个选项，点击 设为默认值 (Set as default) 按钮
4. 在右侧的 超时 (Timeout) 框里，可以设置选择界面的等待时间（单位是秒，例如 5 或 10 秒）
5. 点击 确定 即可

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250811090125.png)

## 7、删除右键菜单项

### ①、删除启用 BitLocker(B)

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250811095013.png)

1. `Windows + R` 打开运行，输入 `regedit` 后点击确定，打开 注册表编辑器 窗口
2. 在注册表编辑器中，导航到以下路径：

```shell
HKEY_CLASSES_ROOT\Drive\shell\encrypt-bde-elev
```

3. 在右侧找到 AppliesTo，右键点击选择修改，将其最后的 True 改为 False：

```shell
(System.Volume.BitLockerProtection:=System.Volume.BitLockerProtection#Off OR System.Volume.BitLockerProtection:=System.Volume.BitLockerProtection#OnPreProvisioned) AND System.Volume.BitLockerRequiresAdmin:=System.StructuredQueryType.Boolean#False
```

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

## 8、添加右键菜单项

### ①、为所有文件类型添加 Notepad3

1. 添加 reg 脚本：[Notepad3_Add_SubMenu.reg](attachments/Notepad3_Add_SubMenu.reg)，清理 reg 脚本：[Notepad3_Remove_Menu.reg](attachments/Notepad3_Remove_Menu.reg)
2. 如不想使用脚本，可手动修改注册表：
3. `Windows + R` 打开运行，输入 `regedit` 后点击确定，打开 注册表编辑器 窗口
4. 进入注册表路径：`HKEY_CLASSES_ROOT\*\shell`
5. 在左侧的树状目录中，右键点击 shell 项，选择 新建 -> 项(K)，将这个新建的项命名为您想在菜单上看到的文字，例如：用 Notepad3 编辑
6. 添加图标：
	1. 选中刚刚创建的 用 Notepad3 编辑 项，在右侧空白处，右键点击 -> 新建 -> 字符串值(S)，将这个字符串值命名为 Icon
	2. 双击 Icon，在 数值数据 中输入 Notepad3 程序 Notepad3.exe 的完整路径。例如：E:\apply\devTools\TextEditor\Notepad3\Notepad3.exe,这会让菜单项旁边显示程序的图标
7. 新建 command 项：
	1. 在左侧目录中，右键点击刚创建的 用 Notepad3 编辑 项，选择 新建 -> 项(K)，将这个新建的子项命名为 command
	2. 单击选中 command 项，在右侧窗口中，会有一个名为 (默认) 的值。双击它
	3. 在弹出的 编辑字符串 对话框的 数值数据 一栏中，输入 Notepad3 的完整路径，并在后面加上 "%1"（包含英文双引号）
	4. 例如："E:\apply\devTools\TextEditor\Notepad3\Notepad3.exe" "%1"
	5. 点击确定保存

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250812112346.png)

### ②、

## 9、设置开发环境变量脚本

1. 脚本下载：[setup_env.ps1](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/setup_env.ps1)
2. 如果无法运行，查看当前的执行策略：
3. 使用管理员打开 PowerShell，输入： `Get-ExecutionPolicy`
4. 如果是 `Restricted` 的话，将其更改为 `RemoteSigned`，在确认中输入 A 表示确定修改

```PowerShell
PS C:\Windows\system32> Get-ExecutionPolicy
Restricted
PS C:\Windows\system32> Set-ExecutionPolicy RemoteSigned

执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): A
PS C:\Windows\system32> Get-ExecutionPolicy
RemoteSigned
PS C:\Windows\system32>
```

4. 修改完毕后，重新执行脚本


## 10、

# 六、问题记录

## 1、Win10 系统下任务栏图标显示白色方块变成空白的解决方法

1. 按快捷键 `Win+R` 打开 cmd 命令行，输入 `%localappdata%`，回车，进入 `C:\Users\10222148\AppData\Local` 目录
2. 在打开的文件夹中，找到 `Iconcache.db`，将其删除。（如果找不到 `Iconcache.db` 文件，说明被系统隐藏了，在文件夹选项中，查看的选项卡，点击“显示隐藏的文件、文件夹和驱动器”即可）
3. 打开 `任务管理器`，在任务管理器中找到 `Windows资源管理器`，右击鼠标，选择 `重新启动` 即可重建图标缓存。

## 2、win10 企业版 LTSC 激活方法

1. win+R 输入 PowerShell 打开 PowerShell 管理员版本
2. 逐条输入以下代码：

```PowerShell
# 安装产品密钥
# 此命令使用 slmgr 脚本（Windows 软件许可管理工具）来安装指定的产品密钥
slmgr -ipk M7XTQ-FN8P6-TTKYV-9D4CC-J462D

# 设置密钥管理服务(KMS)服务器地址
# slmgr -skms 命令用于指定 KMS 服务的地址，用于激活 Windows
slmgr -skms kms.03k.org

# 激活 Windows
# slmgr -ato 命令触发操作系统使用先前安装的密钥和配置的 KMS 服务器进行在线激活
slmgr -ato

# 显示许可信息
# slmgr -dlv 命令用于显示详细的许可信息，包括激活状态和许可证类型
slmgr -dlv
```

## 3、延长 windows 系统暂停更新时间

1. 按下 `Win + R` 组合键，打开运行，然后输入 `regedit` 命令，再按回车，打开注册表编辑器

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090204.png)

2. 注册表编辑器窗口，依次展开到以下路径：`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings`

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090327.png)

3. 在 `Settings` 右侧空白处，点击右键，选择：新建 -> DWORD(32 位)值(D)

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090429.png)

4. 新建的 DWORD(32 位)值(D) 命名为 `FlightSettingsMaxPauseDays`

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090540.png)

5. 双击打开 `FlightSettingsMaxPauseDays` 编辑窗口，基数选择十进制，数值数据输入你想暂停更新的的天数，比如设置 3000 天，再点击确定

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090708.png)

6. `Win+I` 快捷键打开设置，选择：更新和安全 -> Windows 更新 -> 高级选项，设置暂停更新的截止日期

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240820090858.png)

## <span id="6-4">4、ltsc 安装 `.msixbundle` 或 `.msix` 应用包</span>

### ①、正常安装

1. 将安装包放到磁盘根目录，比如：`E:\ModernFlyouts_0.9.3.0_neutral.Msixbundle`
2. 使用管理员打开 PowerShell

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020250811083002.png)

3. 输入命令安装软件：

```PowerShell
Add-AppxPackage -Path "E:\ModernFlyouts_0.9.3.0_neutral.Msixbundle"
```

4. 如果提示：此程序包依赖于一个找不到的框架

```PowerShell
PS C:\Windows\system32> Add-AppxPackage -Path "E:\ModernFlyouts_0.9.3.0_neutral.Msixbundle"                             
Add-AppxPackage : 部署失败，原因是 HRESULT: 0x80073CF3, 包无法进行更新、相关性或冲突验证。                              
Windows 无法安装程序包 32669SamG.ModernFlyouts_0.9.3.0_x64__pcy8vm99wrpcg，因为此程序包依赖于一个找不到的框架。请随要安装的此程序包一起提供由“CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US”发布的框架“Microsoft.VCLibs.140.00.UWPDesktop”(具有中性或 x64 处理器体系结构，最低版本为 14.0.29231.0)。
当前已安装的名称为“Microsoft.VCLibs.140.00.UWPDesktop”的框架为: {}
注意: 有关其他信息，请在事件日志中查找 [ActivityId] 50b5dcb5-09db-0004-e135-ba50db09dc01，或使用命令行 Get-AppPackageLog -ActivityID 50b5dcb5-09db-0004-e135-ba50db09dc01

所在位置 行:1 字符: 1
+ Add-AppxPackage -Path "E:\ModernFlyouts_0.9.3.0_neutral.Msixbundle"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (E:\ModernFlyout...tral.Msixbundle:String) [Add-AppxPackage], IOException
    + FullyQualifiedErrorId : DeploymentError,Microsoft.Windows.Appx.PackageManager.Commands.AddAppxPackageCommand

PS C:\Windows\system32>
```

5. 原因是该系统缺少一个必要的 依赖项 或 公共组件，首先下载并安装缺失的 VCLibs 运行库：
	1. 网络下载 [Microsoft.VCLibs.x64.14.00.Desktop.appx](https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx)
	2. 本地下载 [Microsoft.VCLibs.x64.14.00.Desktop.appx](attachments/Microsoft.VCLibs.x64.14.00.Desktop.appx)
6. 将下载的运行库安装包也放入到磁盘根目录，比如：`E:\Microsoft.VCLibs.x64.14.00.Desktop.appx`
7. 输入命令安装运行库：

```PowerShell
Add-AppxPackage -Path "E:\Microsoft.VCLibs.x64.14.00.Desktop.appx"
```

8. 如果安装成功，再次输入命令安装软件：

```PowerShell
Add-AppxPackage -Path "E:\ModernFlyouts_0.9.3.0_neutral.Msixbundle"
```

### ②、其他报错

#### Ⅰ、查看卸载软件包和依赖

1. 根据名称查看已经安装的的应用包，这两个分别是 `Microsoft.VCLibs.140.00.UWPDesktop` 的 `x64` 和 `x86` 版本

```PowerShell
PS C:\Windows\system32> Get-AppxPackage -Name "Microsoft.VCLibs.140.00*"

Name              : Microsoft.VCLibs.140.00.UWPDesktop
Publisher         : CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Architecture      : X64
ResourceId        :
Version           : 14.0.33728.0
PackageFullName   : Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe
InstallLocation   : C:\Program Files\WindowsApps\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe
IsFramework       : True
PackageFamilyName : Microsoft.VCLibs.140.00.UWPDesktop_8wekyb3d8bbwe
PublisherId       : 8wekyb3d8bbwe
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : False
NonRemovable      : False
IsPartiallyStaged : False
SignatureKind     : Store
Status            : Ok

Name              : Microsoft.VCLibs.140.00.UWPDesktop
Publisher         : CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Architecture      : X86
ResourceId        :                                                                                                     
Version           : 14.0.33728.0                                                                                        PackageFullName   : Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x86__8wekyb3d8bbwe                                  InstallLocation   : C:\Program Files\WindowsApps\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x86__8wekyb3d8bbwe     
IsFramework       : True                                                                                                PackageFamilyName : Microsoft.VCLibs.140.00.UWPDesktop_8wekyb3d8bbwe                                                    
PublisherId       : 8wekyb3d8bbwe                                                                                       IsResourcePackage : False                                                                                               
IsBundle          : False                                                                                               IsDevelopmentMode : False                                                                                               
NonRemovable      : False                                                                                               IsPartiallyStaged : False                                                                                               
SignatureKind     : Store                                                                                               
Status            : Ok                                                                                                                                                                                            
PS C:\Windows\system32>
```

2. 使用 `Remove-AppxPackage` 卸载应用包，此处提示由两个应用包依赖于本应用，需要先卸载这两个应用包才可以

```PowerShell
PS C:\Windows\system32> Remove-AppxPackage -Package "Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe"
Remove-AppxPackage : 部署失败，原因是 HRESULT: 0x80073CF3, 包无法进行更新、相关性或冲突验证。
Windows 无法删除框架 Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe，因为程序包  32669SamG.ModernFl
youts Microsoft.Edge.GameAssist 当前依赖于该框架。如果删除所有依赖于该框架的程序包，则会自动删除该框架。
注意: 有关其他信息，请在事件日志中查找 [ActivityId] 24293e96-0bf0-000c-095f-2924f00bdc01，或使用命令行 Get-AppPackageLo
g -ActivityID 24293e96-0bf0-000c-095f-2924f00bdc01
所在位置 行:1 字符: 1
+ Remove-AppxPackage -Package "Microsoft.VCLibs.140.00.UWPDesktop_14.0. ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (Microsoft.VCLib...__8wekyb3d8bbwe:String) [Remove-AppxPackage], IOException
    + FullyQualifiedErrorId : DeploymentError,Microsoft.Windows.Appx.PackageManager.Commands.RemoveAppxPackageCommand

PS C:\Windows\system32>
```

3. 卸载这两个依赖的应用程序

```PowerShell
PS C:\Windows\system32> Get-AppxPackage *ModernFlyouts* | Remove-AppxPackage
PS C:\Windows\system32> Get-AppxPackage *Microsoft.Edge.GameAssist* | Remove-AppxPackage
```

4. 卸载这 `Microsoft.VCLibs.140.00.UWPDesktop`，包括 `x64` 和 `x86` 版本

```PowerShell
PS C:\Windows\system32> Get-AppxPackage -Name "Microsoft.VCLibs.140.00.UWPDesktop" | Remove-AppxPackage
```

#### Ⅱ、缺少 `Microsoft.UI.Xaml.2.8`

1. 网络下载 [Microsoft.UI.Xaml-2.8.6](https://www.nuget.org/api/v2/package/Microsoft.UI.Xaml/2.8.6)，此链接会下载一个 `.nupkg` 文件，需要将其后缀名改为 `.zip`，然后解压，在 `tools\AppX\x64\Release` 目录下找到 `Microsoft.UI.Xaml.2.8.appx` 文件
2. 本地下载 [Microsoft.UI.Xaml.2.8.appx](attachments/)
3. 下载后使用上面的命令进行安装

```PowerShell
PS C:\Windows\system32> Add-AppxPackage -Path "E:\bundle.msixbundle"                                                    
Add-AppxPackage : 部署失败，原因是 HRESULT: 0x80073CF3, 包无法进行更新、相关性或冲突验证。                              
Windows 无法安装程序包 28017CharlesMilette.TranslucentTB_2025.1.0.0_x64__v826wp6bftszj，因为此程序包依赖于一个找不到的框架。请随要安装的此程序包一起提供由“CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US”发布的框架“Microsoft.UI.Xaml.2.8”(具有中性或 x64 处理器体系结构，最低版本为 8.2310.30001.0)。
当前已安装的名称为“Microsoft.UI.Xaml.2.8”的框架为: {}
注意: 有关其他信息，请在事件日志中查找 [ActivityId] 24293e96-0bf0-0004-738f-2924f00bdc01，或使用命令行 Get-AppPackageLog -ActivityID 24293e96-0bf0-0004-738f-2924f00bdc01

所在位置 行:1 字符: 1
+ Add-AppxPackage -Path "E:\bundle.msixbundle"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (E:\bundle.msixbundle:String) [Add-AppxPackage], IOException
    + FullyQualifiedErrorId : DeploymentError,Microsoft.Windows.Appx.PackageManager.Commands.AddAppxPackageCommand

PS C:\Windows\system32>
```

## 5、

# 七、软件使用



## 3、使用 2fauth 保存 steam 手机令牌验证码

1. 如果 steam 已经绑定了手机令牌，那么首先解绑原先的手机令牌
2. 下载 `steamguard.exe`：
	1. 本地 v0.15.0 下载：[steamguard.exe](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/steamguard.exe)
	2. github 下载：https://github.com/dyc3/steamguard-cli
3. 将下载的 `steamguard.exe` 放到 D 盘根目录
4. 打开 PowerShell，输入命令，会要求输入账号、密码、邮箱验证码，根据提示输入即可

```PowerShell
# 进入 D 盘根目录
cd D:

# 启动 steamguard
./steamguard setup
```

5. 验证成功后会提示：Authenticator has not yet been linked. Before continuing with finalization, please take the time to write down your revocation code: R12345，记下 `R12345`，这是移除这个验证器的恢复密码
6. 按下回车确认，【速验通】会给绑定的手机发来一个验证码，输入验证码，此时添加验证令牌成功
7. 然后在 PowerShell 中输入命令打印二维码，尝试使用 2fauth 扫描该二维码，如果扫描失败，则进行下面的步骤

```PowerShell
./steamguard qr
```

8. 进入目录：`C:\Users\用户\AppData\Roaming\steamguard-cli\maFiles`，打开 `*.maFile` 文件，搜索 `uri` 字段，将 `uri` 字段的值复制下来

```shell
{
    ...
    "uri": "otpauth://totp/Steam:johndoe?secret=D5RTFGT8Z7SW4DYU6I9UH5F4RRE1DF4G&issuer=Steam",
    ...
}
```

9. 打开 2fauth，点击新建，选择导入，将上面 `uri` 字段的值复制到直接输入的框中，然后点击提交

![|575](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241226101009.png)

10. 点击提交后会进入一个新页面，点击导入即可

![|575](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020241226101054.png)

11. 整体流程：

```PowerShell
PS C:\Users\10222148> cd D:
PS D:\> ./steamguard setup
INFO reading manifest from C:\Users\10222148\AppData\Roaming\steamguard-cli/maFiles
Log in to the account that you want to link to steamguard-cli
Username: INFO Logging in to 770717410
Password:
Enter the 2fa code sent to your email: INFO Polling for tokens... -- If this takes a long time, try logging in again.
INFO Logged in successfully!
INFO Adding authenticator...
INFO Saving manifest and accounts...
Authenticator has not yet been linked. Before continuing with finalization, please take the time to write down your revocation code: R12345
Press enter to continue...A code has been sent to your phone number ending in 6394.
Enter SMS code: INFO Verifying authenticator status...
INFO Authenticator finalized.
INFO Saving manifest and accounts...
Authenticator has been finalized. Please actually write down your revocation code: R12345
PS D:\> ./steamguard qr
INFO reading manifest from C:\Users\10222148\AppData\Roaming\steamguard-cli/maFiles
INFO Generating QR codes for 1 accounts
INFO Printing QR code for 770717410
█████████████████████████████████████████████
█████████████████████████████████████████████
████ ▄▄▄▄▄ █▄▄▄█ ▀█ ▄▄ ▄▄ █ ▀ ████ ▄▄▄▄▄ ████
████ █   █ █▄▀██▄▀▀ █ ▀▄█▄▀ ▀ ▀  █ █   █ ████
████ █▄▄▄█ █▀ ▄█▀  ▄▀▀▀██▄▀▀▄▀▀▄▀█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄█▄▀▄█▄▀ ▀▄▀▄▀ ▀▄█▄▀ █▄▄▄▄▄▄▄████
████▀▀█▄█▄▄▄▀▀▀ ▀ ▀▄█▄██▀  █▀▄█  ▀▀▄▄▄▀█▄████
████▀▀▀▄▄ ▄▀▄ █▄ ▀▄ ▄█  ▀█▄█▄▀█ ▄▄ ▄███▀▄████
████▄▀  ▄ ▄  ▀▀▀▀▀█ █▄  █ ▀ ▀▄▀▄▄▄▄▄▀ ▄▄▀████
████▄█▄▀█▀▄█▄▄▄█   ▀ ▄▀█▀▄██▀▄▀ ▄▀▀  █ ▀ ████
█████  ▄ ▀▄ ▄▀ ▄   ▀█ █   ▄ ▄▀█▀▀▀ ███▄▀█████
████▀ █▄▀█▄▀▄▀▄▄██▀ ▀▀█▄▀ ▄▄▄ ▄▄  ▄▄ ▀▄ ▀████
████▄█▀ ▀█▄▀ ▄██ ▄▄▄█▄█▄█▀▀ ▄▄▀▄█ █  █▀▄▀████
████▄▄▀██▄▄█ ▄█▄▀█ ▄██▄██▄▀██▄ ▀ █▄ ▄█ ▀▄████
████ ▄▄▄▄▄ █▄ ▄▀██▄▄ ▄  █▄▀ ▄▄▄▀ █▄█ ▀▄██████
████ █   █ ██▄  █▀▄▄   ▄▀ ███▀    ▄▄ ▀▀ ▄████
████ █▄▄▄█ █▄▀█ ▄ ▄▀ █ █▀█▀█ ▄▀██ ▀█▄  ▄▄████
████▄▄▄▄▄▄▄█▄█████▄███▄████▄██▄▄██▄█▄█▄█▄████
█████████████████████████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
PS D:\>
```

## 4、图种制作

1. 将图片和种子（或其他文件）放在同一个目录中
2. 图片重命名为：`1.jpg`
3. 种子重命名为：`2.torrent`
4. 将种子文件压缩，如：`2.rar`
5. 在同目录下创建文本文档，然后在其中输入：`copy/b 1.jpg+2.rar 3.jpg`
6. 将文本文档的后缀名改为：`.bat`
7. 双击 bat 文件。生成的 3.jpg 即为图种
8. 要解压图种只需更改后缀名为 `.rar`，然后解压即可


### ③、

### ④、

## 7、

## 8、

# 八、命令使用

## 1、查看及导出目录结构

#### Ⅰ、查看目录结构

1. 目录窗口视图

![|675](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240511090819.png)

2. 查看目录结构（文件夹）：在当前要操作的文件夹目录下输入命令 `tree`，此时得到目录下树形的目录结构。默认情况下只显示“文件夹”而不显示文件。

```PowerShell
tree
```

![|474](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240511091131.png)

1. 查看目录结构（包括文件）：使用参数 `/f` 将以层次的结构显示所有文件夹及文件的名称。

```PowerShell
tree /f
```

![|481](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240511091256.png)

#### Ⅱ、导出目录结构

> 将当前文件夹树形结构写入 xxx.txt 中

1. 保存的树形结构，只含有文件夹

```PowerShell
tree /f > darknet.txt
```

2. 保存的树形结构，包含文件夹和文件

```PowerShell
tree /f > darknetf.txt
```

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020240511092214.png)


# 九、硬件驱动 AMD 

## 1、去除或恢复 AMD 显卡的右键菜单的方法

1. amd 显卡驱动安装完之后，在资源管理器右键会显示 amd 的菜单：

![|481](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023093010.png)

1. 去除方式：
2. `win + r` ，弹出运行窗口，输入：`regedit.exe`，打开注册表

![|750](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023093512.png)

1. 在地址栏输入：`计算机\HKEY_CLASSES_ROOT\Directory\background\shellex\ContextMenuHandlers\ACE`，点击进入 `ACE`

![|750](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023093748.png)

1. 删除 `ACE` 下的这个数值文件即可

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/%E8%AE%BE%E5%A4%87%E5%92%8C%E5%B7%A5%E5%85%B7/attachments/Pasted%20image%2020231023093902.png)


# 十、


