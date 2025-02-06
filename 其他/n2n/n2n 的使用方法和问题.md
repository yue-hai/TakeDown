# 一、使用步骤

## 1、使用脚本启动

1. 下载群文件中的 `gnb_udp_over_tcp`

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240819161206.png)

2. 解压，进入 `\gnb_udp_over_tcp\bin\Window10_x86_64`，双击 `run_gnb_udp_over_tcp.bat` 运行脚本

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240819161555.png)

3. 双击 `run_gnb_udp_over_tcp.bat` 运行脚本后，会启动一个命令行窗口，请在使用 n2n 的过程中一直保持其开启，<font color="#ff0000">不要关闭</font>

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108140744.png)

4. 下载群文件中的 n2n 客户端：`n2n电脑客户端_client_windows_3.12_Pack_2.zip`

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240819161741.png)

5. 解压，然后双击其中的 `n2n.exe` 运行；<font color="#ff0000">若是被杀毒软件误删，请加入白名单</font>

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240819162113.png)

6. 服务器中输入：`127.0.0.1:10092`，一定要保证 2 中的 `run_gnb_udp_over_tcp.bat` 脚本在运行
7. `虚拟网IP` 后面的选项请勾选，防止虚拟 ip 和别人重复
8. <font color="#ff0000">虚拟网 ip 前三位要保证和一起联机的朋友相同</font>，最后一位 1 ~ 255，随意选择；若是自动分配的前三位不同，请取消勾选自动分配，手动修改虚拟 ip
9. <font color="#ff0000">小组名称需要一摸一样</font>

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108141133.png)

10. 点击启动，等待时间会稍长一点，大概 10 秒；等待期间<font color="#ff0000">不要按重启按钮</font>，不然要在等 2 分钟左右才能连接上
11. 服务器 ip 后面显示绿色对号即为连接成功

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108141259.png)

12. 如果经过了上面的步骤，但是一直无法连接成功，一直不显示绿色对号，那么继续看下面：

## 2、不用脚本，手动输入命令

> 经测试，上面的 `run_gnb_udp_over_tcp.bat` 运行脚本有一部分人可以使用，但是也有一部分人没有作用
> 
> 那么就不使用脚本，自己手动输入命令

1. 关闭上面因为启动脚本而弹出的命令行窗口：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108140744.png)

2. 依然是进入 `\gnb_udp_over_tcp\bin\Window10_x86_64` 目录

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241101135047.png)

3. 在目录中，按住键盘的 shift 键，然后点击鼠标右键，选择：在此处打开 Powershell 窗口

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240809134147.png)

4. 之后会弹出一个窗口，在其中输入以下内容并回车：
	1. `-u`：表示启用 UDP 模式，即将接收到的 TCP 数据转换为 UDP 数据。
	2. `-l 10092`：<font color="#ff0000">n2n 使用的端口</font>，`-l` 参数后跟的是监听的 UDP 端口号，这里设置为 10092，表示该服务将监听端口 10092 上的 UDP 数据。
	3. `83.229.120.176`：这是 TCP 源地址，即服务端的 IP 地址；<font color="#ff0000">请根据要连接的服务端自行修改这个参数</font>
	4. `10095`：这是服务端监听的 TCP 端口号。

```shell
.\gnb_udp_over_tcp.exe -u -l 10092 83.229.120.176 10095
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108140744.png)

5. 同样的，请在使用 n2n 的过程中一直保持其开启，<font color="#ff0000">不要关闭</font>
6. n2n 的设置与上面相同：
	1. 服务器中输入：`127.0.0.1:10092`，<font color="#ff0000">一定要保证上面的 Powershell 窗口中的程序一直在运行</font>
	2. `虚拟网IP` 后面的选项请勾选，防止虚拟 ip 和别人重复
	3. <font color="#ff0000">虚拟网 ip 前三位要保证和一起联机的朋友相同</font>，最后一位 1 ~ 255，随意选择；若是自动分配的前三位不同，请取消勾选自动分配，手动修改虚拟 ip
	4. <font color="#ff0000">小组名称需要一摸一样</font>

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108141133.png)

7. 服务器 ip 后面显示绿色对号即为连接成功

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241108141259.png)

## 3、其他的服务器地址

### ①、说明

1. 这里列举的服务器有的不太稳定带宽太低，有的只是暂时能用，有的可能过期了没有续费等，不保证一定能用
2. 只是作为后备使用，如果上面的脚本方式无法使用、连接，再尝试这些地址

### ②、服务器列表

| 服务器地址                | 更新时间       | 备注            |
| -------------------- | ---------- | ------------- |
| 101.200.86.248:10092 | 2024/12/17 | 可用，但是人多了可能会卡顿 |

### ③、使用方式

1. 如果上面开启了 `gnb_udp_over_tcp` 脚本，请关掉，这里的这些 ip 都不再需要使用这个脚本
2. 复制上面的服务器地址到 n2n 中，勾选虚拟网 ip 自动分配， 设置小组名称，点击启用即可

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241217162243.png)

3. 大概等待几秒钟，服务器 ip 后面显示绿色对号即为连接成功

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020241217162332.png)

4. 如果 1 分钟后还没有成功，请换一个服务器地址重新尝试

# 二、连接不上的原因和解决方式

## 1、点击启动后没有马上显示成功

1. 通过使用 `gnb_udp_over_tcp` 连接时，从点击启动到连接成功大概有 10 秒左右，等待 10 秒左右看看
2. 当在连接成功的状态下，点击停止断开连接后马上再点击启动（或点击重启），并不会马上重连，需要等待 1 ~ 2 分钟，这是服务器机制问题，等待即可

## 2、NAT 类型问题

1. 点击测试工具 -> NAT 检测，点击开始检测

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FPasted%20image%2020240819163053.png)

2. 若是显示检测失败或结果不是下面的四种，请点击切换服务器，然后多次测试
3. 若检测结果是 `Symmetric NAT`，说明当前机器是不可以使用 n2n 的，若想使用，请自行修改光猫，百度搜索：NAT 类型修改
	1. [家用路由器修改NAT1](https://www.bilibili.com/read/cv22212682/)
	2. [网络类型NAT3改NAT1 基于（联通）光猫桥接、路由器红米AX5、win10系统](https://blog.csdn.net/qq_46648437/article/details/113747066)
	3. [如何提升NAT类型，NAT提升至full_cone，设置光猫](https://blog.csdn.net/weixin_42168194/article/details/106037065)
4. 若不是 `Symmetric NAT`，而是其他三种，说明无法连接的原因不在这里
5. 几种常见的 NAT 类型：
	1. Full Cone
	2. Restricted Cone
	3. Port Restricted Cone
	4. Symmetric NAT

## 3、虚拟 ip 冲突

1. 进入下面的网址查看一下 ip 是不是已经被使用了：
	1. 若是选择的使用脚本的方式连接：[查询 n2n edge 节点列表](http://yan.yue-hai.top:10093/static/n2n-edge-query.html)
	2. 其他的服务器地址，则修改下面连接中的 ip 进行访问：http://ip:10093/static/n2n-edge-query.html
2. ip 是唯一的，ip 相同时即使小组不同也会导致冲突，无法连接
3. 和朋友一起联机的话，ip 前三位需要相同，比如：`192.168.1`，最后一位可选 `1 ~ 254`
4. 挑一个没有被使用的就可以了

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FC8BDC8FFEE9C4793B8F32A08E6EBCBBC.png)

## 4、windows 防火墙的问题

1. 右键开始菜单，选择以**管理员模式**打开 `powershell`，执行下面命令就可以开启 v4 和 v6 的入站规则
2. 开启 v4 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V4" protocol=icmpv4:any,any dir=in action=allow
```

3. 开启 v6 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V6" protocol=icmpv6:any,any dir=in action=allow
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2F%E5%85%B6%E4%BB%96%2Fn2n%2Fattachments%2FC80DC490867A47FDBD0E43F4BD2153D3.png)

## 5、
