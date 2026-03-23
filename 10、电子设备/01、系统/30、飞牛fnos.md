# 一、虚拟机配置

## 1、android-x86_64-9.0

### ①、镜像下载

1. Android-x86 是一个开源项目，可以从其官方网站和指定的托管平台免费下载 ISO 镜像文件
2. 官方项目主页： https://www.android-x86.org
3. 进入后点击 Download，选择对应的版本目录，然后选择对应的镜像进行下载即可

![|700](attachments/Pasted%20image%2020250807130021.png)

### ②、创建虚拟机

1. 正常创建即可，没有选择硬件直通

![|530](attachments/Pasted%20image%2020250807130200.png)

![|530](attachments/Pasted%20image%2020250807130229.png)

![|530](attachments/Pasted%20image%2020250807130242.png)

![|530](attachments/Pasted%20image%2020250807130249.png)

### ③、安装系统镜像

1. 启动创建的虚拟机，使用 vnc 连接
2. 安装选项：选择第三个选项
	1. Live CD - Run Android-x86 without installation：直接从这个 ISO 镜像文件运行安卓系统，而不进行任何安装。可以把它看作一个免安装体验版，但是在系统中做的更改（如安装应用、修改设置）都会在虚拟机重启后消失
	2. Live CD - Debug mode：上一个选项类似，也是一个免安装的体验模式，但它会输出大量的调试信息
	3. Installation - Install Android-x86 to harddisk： 安装模式，这会将安卓系统永久性地安装到为虚拟机分配的虚拟硬盘上
	4. Advanced options...：高级选项。里面通常包含一些特殊的启动模式，比如无图形界面启动、指定显卡驱动（VESA）启动等，主要用于解决兼容性问题

![](attachments/Pasted%20image%2020250807130431.png)

3. 磁盘分区：选择第一个选项 Create/Modify partitions 并按回车后，按照以下步骤操作：
	1. 选择分区表类型： 提示：Do you want to use GPT? (您想使用 GPT 分区表吗？)。对于 Android-x86 来说，选择 No (不使用) 通常兼容性更好，它会使用传统的 MBR 分区方案
	2. 进入分区工具 (cfdisk)： 会看到一个代表虚拟硬盘的条目（例如 vda 或 sda）
	3. 创建新分区：
		1. 用方向键选择 `[ New ]` (新建)，然后按回车
		2. 它会询问分区类型，选择 `[ Primary ]` (主分区)，按回车
		3. 它会询问分区大小，直接按回车会默认使用全部硬盘空间
		4. 确保新创建的分区是 `[ Bootable ]` (可引导) 的。如果 Boot 标志没有出现在分区信息上，用方向键选中该分区，然后选择屏幕下方的 `[ Bootable ]` 选项并按回车，给它添加上启动标记
	4. 写入并退出：选择 `[ Write ]` (写入)，按回车，它会请求确认，输入 yes 然后按回车
	5. 最后，选择 `[ Quit ]` (退出)，按回车
	6. 完成以上操作后，就会返回到这个 Choose Partition 界面
	7. 这时，刚才创建的那个分区（例如 vda1 或 sda1）就会出现在列表中了。只需选中新出现的那个分区，然后选择 `< OK >`，就可以继续下一步的文件系统格式化和安装过程了

![](attachments/Pasted%20image%2020250807130720.png)

4. 格式化磁盘分区：选择 ext4

![](attachments/Pasted%20image%2020250807131208.png)

5. 是否启动引导程序：必须选择 `< Yes >`

![](attachments/Pasted%20image%2020250807131242.png)

6. 决定安卓的 `/system` 分区（系统核心文件所在的区域）在安装后是否可以被修改：推荐选择 `< Yes >`，然后选择直接进入系统或者重启

![](attachments/Pasted%20image%2020250807131346.png)

7. GRUB 启动引导加载器：这表示系统安装成功，选择第一个选项然后按回车，即可进入系统

![](attachments/Pasted%20image%2020250807131533.png)

### ④、修改分辨率

1. 重启虚拟机，进入 GRUB 启动引导加载器页面时，按 `e`

![](attachments/Pasted%20image%2020250807131533.png)

2. 此时会进入 GRUB 的编辑模式，选中第一项，再次按 `e`

![](attachments/Pasted%20image%2020250807131810.png)

3. 进入编辑命令行后，在最后加一个空格，然后输入想要的分辨率，如：`video=1920x1080`，然后按回车确认，再按 `b` 启动系统即可

![](attachments/Pasted%20image%2020250807131855.png)

### ⑤、开启 adb 远程连接

1. 在 Android-x86 虚拟机中，打开 终端模拟器 (Terminal) 应用
2. 首先输入 su 命令，获取管理员权限

```shell
su
```

3. 授予管理员权限后，再输入以下命令，让 ADB 开始在 5555 端口上监听网络连接

```shell
setprop service.adb.tcp.port 5555
stop adbd
start adbd
```

### ⑥、开机自动开启 adb 远程连接

1. 在 Android-x86 虚拟机中，打开 终端模拟器 (Terminal) 应用
2. 首先输入 su 命令，获取管理员权限

```shell
su
```

3. 挂载 `/system` 分区为可读写：为了能修改系统文件，需要确保 `/system` 分区是可写的。虽然在安装时已经选择了可读写，但有时系统启动后会以只读方式挂载以保证安全。执行以下命令可以确保它是可写的：

```shell
mount -o rw,remount /system
```

4. 编辑启动脚本 `init.sh`：

```shell
vi /system/etc/init.sh
```

5. 在脚本末尾 `return 0` 前面添加命令：
	1. 按下键盘上的 i 键，进入 vi 的插入(Insert)模式
	2. 使用 ↓ 方向键将光标移动到文件的最末尾
	3. 在末尾 `return 0` 之前添加以下两行内容：

```shell
# Set ADB to listen on TCP/IP port 5555 on boot
setprop service.adb.tcp.port 5555
```

6. 保存并退出 vi 编辑器：
	1. 按下 Esc 键，退出插入模式
	2. 然后输入 `:wq`，再按回车
7. 修改完毕，之后重启虚拟机就会自动开启 adb 远程连接了

## 2、windows_10_22H2 与硬件直通

### ①、硬件与结果说明

1. 结果：想要直通 5600g 的核显，直通失败
2. 硬件：
	1. 主板：华硕 TUF GAMING B450M-PRO S B450M 重炮手
	2. cpu：AMD Ryzen 5 5600G

### ②、主板 bios 设置

1. 重启电脑，在开机自检画面（出现ROG或TUF LOGO时）反复按 Del 或 F2 键，直到进入 BIOS 设置界面，然后进入并切换到高级模式
2. 开启 SVM（CPU 虚拟化）：
	1. 进入 Advanced (高级) 选项卡
	2. 选择 CPU Configuration (CPU 设置)
	3. 找到 SVM Mode，确保它被设置为 Enabled (开启)

![](attachments/Pasted%20image%2020250807134201.png)

3. 开启 IOMMU：
	1. 进入 Advanced (高级) 选项卡
	2. 找到并进入 AMD CBS (AMD Common BIOS Settings)
	3. 进入 NBIO Common Options (北桥通用选项)
	4. 找到 IOMMU，确保它被设置为 Enabled (开启)

![](attachments/Pasted%20image%2020250807134157.png)

4. 启用 Above 4G Decoding（最重要）：
	1. 进入 Advanced (高级) 选项卡
	2. 选择 PCI Subsystem Settings (PCI 子系统设置)
	3. 找到 Above 4G Decoding，将它设置为 Enabled (开启)
	4. 通常启用了 Above 4G Decoding 之后，在同一个 PCI Subsystem Settings 菜单下，会出现 Re-Size BAR Support 的选项，保持其为 Disabled (关闭)

![](attachments/Pasted%20image%2020250807134510.png)

5. 禁用 CSM（如果前三步都无效）
	1. 进入 Boot (启动) 选项卡
	2. 选择 CSM (Compatibility Support Module)
	3. 找到 Launch CSM，将其设置为 Disabled (关闭)
	4. 注意：禁用 CSM 可能会影响系统的引导。如果 fnos 之前是在 Legacy 模式下安装的，这可能会导致无法开机。但对于 UEFI 系统来说，这是推荐的设置。如果禁用后无法开机，需改回 Enabled
6. 说明：
	1. 在进行 4、5 的修改之前，虚拟机中直通的显卡提示：该设备找不到足够资源可以使用。(代码12) 如果要使用该设备，你需要禁用该系统上的另一个设备。
	2. 在进行 4、5 的修改之后，虚拟机中直通的显卡提示：由于该设备有问题，Windows 已将其停止。 (代码 43)；直到最后，这个问题也没有解决


### ③、创建虚拟机前的准备

1. 开启 ssh，使用命令查看遍历系统中所有的 IOMMU 分组，并列出每个组里包含的 PCI 设备信息：

```shell
#!/bin/bash
shopt -s nullglob
for d in /sys/kernel/iommu_groups/*/devices/*; do
    n=${d#*/iommu_groups/*}; n=${n%%/*}
    printf 'IOMMU Group %-2s ' "$n"
    lspci -nns "${d##*/}"
done | sort -V
```

```shell
yan@yuehai:~$ #!/bin/bash

shopt -s nullglob

for d in /sys/kernel/iommu_groups/*/devices/*; do

    n=${d#*/iommu_groups/*}; n=${n%%/*}

    printf 'IOMMU Group %-2s ' "$n"

    lspci -nns "${d##*/}"

done | sort -V

IOMMU Group 0  00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]

IOMMU Group 1  00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]

IOMMU Group 2  00:02.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]

IOMMU Group 3  00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]

IOMMU Group 4  00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]

IOMMU Group 5  00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]

IOMMU Group 6  00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]

IOMMU Group 7  00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 51)

IOMMU Group 7  00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)

IOMMU Group 8  00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 0 [1022:166a]

IOMMU Group 8  00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 1 [1022:166b]

IOMMU Group 8  00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 2 [1022:166c]

IOMMU Group 8  00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 3 [1022:166d]

IOMMU Group 8  00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 4 [1022:166e]

IOMMU Group 8  00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 5 [1022:166f]

IOMMU Group 8  00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 6 [1022:1670]

IOMMU Group 8  00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 7 [1022:1671]

IOMMU Group 9  01:00.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset USB 3.1 xHCI Compliant Host Controller [1022:43d5] (rev 01)

IOMMU Group 9  01:00.1 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset SATA Controller [1022:43c8] (rev 01)

IOMMU Group 9  01:00.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset PCIe Bridge [1022:43c6] (rev 01)

IOMMU Group 9  02:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset PCIe Port [1022:43c7] (rev 01)

IOMMU Group 9  02:01.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset PCIe Port [1022:43c7] (rev 01)

IOMMU Group 9  02:04.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] 400 Series Chipset PCIe Port [1022:43c7] (rev 01)

IOMMU Group 9  04:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller [10ec:8125] (rev 05)

IOMMU Group 9  05:00.0 SATA controller [0106]: ASMedia Technology Inc. ASM1166 Serial ATA Controller [1b21:1166] (rev 02)

IOMMU Group 10 06:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]

IOMMU Group 11 07:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series] [1002:1638] (rev c9)

IOMMU Group 12 07:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller [1002:1637]

IOMMU Group 13 07:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]

IOMMU Group 14 07:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]

IOMMU Group 15 07:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]

IOMMU Group 16 08:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 81)

yan@yuehai:~$ 
```

2. 从输出中可以看到：
	1. IOMMU Group 11: 仅包含 5600G 核显 (VGA compatible controller `[1002:1638]`)
	2. IOMMU Group 12: 仅包含该核显的音频设备 (Audio device `[1002:1637]`)
3. 这两个关键设备都被完美地独立到了各自的组中，没有任何其他设备干扰。这意味着可以非常干净利落地将它们一起直通给虚拟机，让虚拟机同时获得图形和通过 HDMI/DP 接口的声音输出
4. 检查显卡核心 (07:00.0) 的分配：`lspci -k -s 07:00.0`

```shell
yan@yuehai:~$ lspci -k -s 07:00.0
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series] (rev c9)
        Subsystem: ASUSTeK Computer Inc. Cezanne [Radeon Vega Series / Radeon Vega Mobile Series]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
```

5. 检查音频核心 (07:00.1) 的分配：`lspci -k -s 07:00.1`

```shell
yan@yuehai:~$ lspci -k -s 07:00.1
07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
        Subsystem: ASUSTeK Computer Inc. Renoir Radeon High Definition Audio Controller
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
```

6. `amdgpu` 和 `snd_hda_intel` 表示系统默认驱动，出现这个输出表示当前设备没有被虚拟机接管，由宿主机在使用
7. 如果变为了 `vfio-pci`，表示当前设备已经被虚拟机接管，直通成功

### ④、创建虚拟机

1. 设置虚拟机名称和系统

![|680](attachments/Pasted%20image%2020250807135444.png)

2. 设置虚拟机主要参数

![](attachments/Pasted%20image%2020250807135613.png)

3. 添加存储空间

![](attachments/Pasted%20image%2020250807135704.png)

4. 添加网卡

![](attachments/Pasted%20image%2020250807135715.png)

5. 设置硬件直通：此处我选择了 5600g 集成的 核显和声卡，由上面的命令得到的结果

![](attachments/Pasted%20image%2020250807135756.png)

### ⑤、安装系统镜像

1. 此处安装时，<font color="#c00000">一定要保证虚拟机无法连接外网</font>；将虚拟网卡删了也好，将路由器网线罢拔了也好
2. 因为如果连着外网，系统监测到了 amd 显卡就会自动安装驱动，而此时我们还没有来得及修改配置文件伪装虚拟化，amd 驱动会检测到他在一个虚拟环境中，安装就会报错，提示：由于该设备有问题，Windows 已将其停止。 (代码 43)
3. 启动虚拟机，虚拟机启动后可以再次使用 `lspci -k -s 07:00.0` 和 `lspci -k -s 07:00.1` 命令查询设备分配，此时应该都变为了 `Kernel driver in use: vfio-pci`
4. 系统正常安装即可，版本尽量选择专业版
5. 系统安装完毕后，开启远程桌面，然后用局域网中另一台电脑的远程桌面进行连接，可以连接再进行下一步
6. 重启虚拟机，然后再次尝试使用远程桌面进行连接，如果依然成功，关闭虚拟机

### ⑥、修改虚拟机配置文件

1. 确保虚拟机关闭
2. 查看虚拟机名称：`sudo virsh list --all`

```shell
yan@yuehai:~$ sudo virsh list --all
[sudo] password for yan: 
 Id   Name       State
---------------------------
 50   njzxkdn4   shut off

yan@yuehai:~$ 
```

3. 查看配置文件：`sudo virsh dumpxml njzxkdn4`，没有改动过应该是这样的：

```xml
yan@yuehai:~$ sudo virsh dumpxml pase10ba
<domain type='kvm'>
  <name>njzxkdn4</name>
  <uuid>91f3f656-61d6-4403-874e-7e9b8123fcb9</uuid>
  <title>windows_10_22H2</title>
  <metadata>
    <customMeta xmlns="customMeta">
      <osType xmlns="osType">windows</osType>
      <osVersion xmlns="osVersion">10</osVersion>
      <autostart xmlns="autostart">false</autostart>
      <createdTime xmlns="createdTime">1754548291</createdTime>
    </customMeta>
  </metadata>
  <memory unit='KiB'>33554432</memory>
  <currentMemory unit='KiB'>33554432</currentMemory>
  <vcpu placement='static'>12</vcpu>
  <os>
    <type arch='x86_64' machine='pc-q35-7.2'>hvm</type>
    <bootmenu enable='yes' timeout='5000'/>
  </os>
  <features>
    <acpi/>
    <hyperv mode='custom'>
      <relaxed state='on'/>
      <vapic state='on'/>
      <vpindex state='on'/>
      <synic state='on'/>
      <stimer state='on'/>
    </hyperv>
  </features>
  <cpu mode='host-passthrough' check='none' migratable='on'>
    <topology sockets='1' dies='1' cores='12' threads='1'/>
  </cpu>
  <clock offset='localtime'>
    <timer name='rtc' tickpolicy='catchup'/>
    <timer name='pit' tickpolicy='delay'/>
    <timer name='hpet' present='no'/>
    <timer name='hypervclock' present='yes'/>
  </clock>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <pm>
    <suspend-to-mem enabled='no'/>
    <suspend-to-disk enabled='no'/>
  </pm>
  <devices>
    <emulator>/usr/bin/qemu-system-x86_64</emulator>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='/vol1/1000/app_data/tool/virtual_machines/drive/virtio-win-0.1.262.iso'/>
      <target dev='sda' bus='sata'/>
      <readonly/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='/vol1/1000/app_data/tool/virtual_machines/windows/win10/22H2/zh-cn_windows_10_business_editions_version_22h2_updated_nov_2023_x64_dvd.iso'/>
      <target dev='sdb' bus='sata'/>
      <readonly/>
      <boot order='20'/>
      <address type='drive' controller='0' bus='0' target='0' unit='1'/>
    </disk>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/vol1/vm/pool/91f3f656-61d6-4403-874e-7e9b8123fcb9-23a2.qcow2'/>
      <target dev='vda' bus='virtio'/>
      <boot order='2'/>
      <alias name='ua-order--2'/>
      <address type='pci' domain='0x0000' bus='0x07' slot='0x00' function='0x0'/>
    </disk>
    <controller type='pci' index='0' model='pcie-root'/>
    <controller type='pci' index='1' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='1' port='0x1'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x0' multifunction='on'/>
    </controller>
    <controller type='pci' index='2' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='2' port='0x9'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
    </controller>
    <controller type='pci' index='3' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='3' port='0xa'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
    </controller>
    <controller type='pci' index='4' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='4' port='0xb'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x3'/>
    </controller>
    <controller type='pci' index='5' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='5' port='0xc'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x4'/>
    </controller>
    <controller type='pci' index='6' model='pcie-to-pci-bridge'>
      <model name='pcie-pci-bridge'/>
      <address type='pci' domain='0x0000' bus='0x05' slot='0x00' function='0x0'/>
    </controller>
    <controller type='sata' index='0'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x1f' function='0x2'/>
    </controller>
    <controller type='usb' index='0' model='qemu-xhci'>
      <address type='pci' domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
    </controller>
    <controller type='scsi' index='0' model='virtio-scsi'>
      <address type='pci' domain='0x0000' bus='0x03' slot='0x00' function='0x0'/>
    </controller>
    <controller type='virtio-serial' index='0'>
      <address type='pci' domain='0x0000' bus='0x04' slot='0x00' function='0x0'/>
    </controller>
    <controller type='pci' index='7' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='7' port='0xd'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x5'/>
    </controller>
    <controller type='pci' index='8' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='8' port='0xe'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x6'/>
    </controller>
    <controller type='pci' index='9' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='9' port='0xf'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x7'/>
    </controller>
    <interface type='bridge'>
      <mac address='ec:51:02:74:a3:60'/>
      <source bridge='enp4s0-ovs'/>
      <virtualport type='openvswitch'>
        <parameters interfaceid='84138fd9-6cb7-44aa-907c-72ee31558fa6'/>
      </virtualport>
      <model type='e1000'/>
      <address type='pci' domain='0x0000' bus='0x06' slot='0x01' function='0x0'/>
    </interface>
    <channel type='qemu-vdagent'>
      <source>
        <clipboard copypaste='yes'/>
      </source>
      <target type='virtio' name='com.redhat.spice.0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>
    <input type='tablet' bus='usb'>
      <address type='usb' bus='0' port='1'/>
    </input>
    <input type='mouse' bus='ps2'/>
    <input type='keyboard' bus='ps2'/>
    <graphics type='vnc' socket='/var/run/vms/pase10ba.vnc.sock' powerControl='yes'>
      <listen type='socket' socket='/var/run/vms/pase10ba.vnc.sock'/>
    </graphics>
    <sound model='ich6'>
      <address type='pci' domain='0x0000' bus='0x06' slot='0x02' function='0x0'/>
    </sound>
    <audio id='1' type='none'/>
    <video>
      <model type='vga' vram='16384' heads='1' primary='yes'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </video>
    <hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x07' slot='0x00' function='0x0'/>
      </source>
      <address type='pci' domain='0x0000' bus='0x08' slot='0x00' function='0x0'/>
    </hostdev>
    <hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x07' slot='0x00' function='0x1'/>
      </source>
      <address type='pci' domain='0x0000' bus='0x09' slot='0x00' function='0x0'/>
    </hostdev>
    <memballoon model='virtio'>
      <stats period='5'/>
      <address type='pci' domain='0x0000' bus='0x02' slot='0x00' function='0x0'/>
    </memballoon>
  </devices>
  <seclabel type='none' model='apparmor'/>
</domain>

yan@yuehai:~$ 
```

4. 修改配置文件：`sudo virsh edit njzxkdn4`：
5. 通常在底部，删除虚拟显卡 `<video>`、虚拟声卡 `<sound>` 和 `<audio>`、图形设备 `<graphics>` 标签和其中的内容
	1. 注意此处删除了这些设备之后，虚拟机就不可以通过 vnc 连接了，只能通过远程桌面进行连接
	2. 所以一定要保证远程桌面连接没问题
	3. 修改完毕后，保存退出，然后再进行下面的修改

```xml
    <graphics type='vnc' socket='/var/run/vms/pase10ba.vnc.sock' powerControl='yes'>
      <listen type='socket' socket='/var/run/vms/pase10ba.vnc.sock'/>
    </graphics>
    <sound model='ich6'>
      <address type='pci' domain='0x0000' bus='0x06' slot='0x02' function='0x0'/>
    </sound>
    <audio id='1' type='none'/>
    <video>
      <model type='vga' vram='16384' heads='1' primary='yes'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </video>
```

6. 通常在顶部，隐藏 KVM 虚拟机身份：
	1. 在 `<hyperv>` 块的内部，加入一行 `<vendor_id state='on' value='ASUS'/>`；这行代码的作用，是告诉 Hyper-V 虚拟机不要暴露默认的供应商 ID，那会暴露虚拟机的身份，假装供应商是 ASUS。这里的 ASUS 可以换成任何不超过 12 个字符的、看起来像主板厂商的名字，比如 MSI、Gigabyte 等等，不过 ASUS 就很好
	2. 在 `<hyperv>...</hyperv>` 块的下面，加入一个新的 `<kvm>` 块；这行代码的作用，是向虚拟机内的操作系统（Guest OS）隐藏它正在一个KVM虚拟环境中运行的事实

```xml
<features>
    <acpi/>
    <hyperv mode='custom'>
      <relaxed state='on'/>
      <vapic state='on'/>
      <vpindex state='on'/>
      <synic state='on'/>
      <stimer state='on'/>
      <vendor_id state='on' value='ASUS'/>
    </hyperv>
    <kvm>
      <hidden state='on'/>
    </kvm>
  </features>
```

7. 修改完毕后，保存退出

### ⑦、安装驱动

1. 启动虚拟机，将下载好的 amd 显卡驱动通过远程桌面复制到虚拟机中，然后尝试安装
2. 安装完毕后，如果设备管理器中显卡有黄色三角，并提示：该设备找不到足够资源可以使用。(代码12) 如果要使用该设备，你需要禁用该系统上的另一个设备。
	1. 那表示上面的配置文件修改失败，需要重复上面的步骤，或者看一下 bios 项是否设置的不对
3. 如果提示：由于该设备有问题，Windows 已将其停止。 (代码 43)
	1. 那可能安装时联网了，导致系统自动安装了驱动，此时需要重新创建虚拟机（卸载驱动太麻烦了，还很难卸载干净）
	2. 也可能配置文件修应该失败，导致驱动检测到了自己处于虚拟环境
	3. 我尝试了 `Adrenalin 25.5.1 (WHQL Recommended)` 和 `Adrenalin 22.3.2 Optional` 版本的驱动，安装完毕后都是提示 代码 43，没有解决这个问题，可能是硬件限制吧

# 二、

# 三、

# 四、

# 五、
