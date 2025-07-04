# 一、使用步骤

### ①、服务器列表

| 服务器地址                | 更新时间       | 备注                     |
| -------------------- | ---------- | ---------------------- |
| 101.200.86.248:10092 | 2024/12/17 | 可用，但是只有 3m 带宽，人多了可能会卡顿 |

### ②、使用方式

1. 下载 n2n 客户端，解压密码：`yuehai`：[n2n_client_windows_3.12-密码-yuehai.7z](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/n2n_client_windows_3.12-密码-yuehai.7z)
2. 或者在群里下载：

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/Pasted%20image%2020240819161741.png)

3. 解压，然后双击其中的 `n2n.exe` 运行；<font color="#ff0000">若是被杀毒软件误删，请加入白名单</font>

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/Pasted%20image%2020240819162113.png)

4. 复制上面的服务器地址到 n2n 服务器输入框中
5. `虚拟网IP` 后面的选项请勾选，防止虚拟 ip 和别人重复
	1. <font color="#ff0000">虚拟网 ip 前三位要保证和一起联机的朋友相同</font>
	2. 最后一位 1 ~ 255，随意选择；若是自动分配的前三位不同，请取消勾选自动分配，手动修改虚拟 ip
6. <font color="#ff0000">小组名称需要一摸一样</font>

![](attachments/Pasted%20image%2020250626153531.png)

7. 点击启动，有时等待时间会稍长一点，等待期间<font color="#ff0000">不要按重启按钮</font>，不然要再等 2 分钟左右才能连接上
8. 服务器 ip 后面显示绿色对号即为连接成功

![](attachments/Pasted%20image%2020250626153637.png)

# 二、连接不上的原因和解决方式

## 1、点击启动后没有马上显示成功

1. 连接时，从点击启动到连接成功有时等待时间会稍长一点，等待 10 秒左右看看
2. 当在连接成功的状态下，点击停止断开连接后马上再点击启动（或点击重启），并不会马上重连，需要等待 1 ~ 2 分钟，这是服务器机制问题，等待即可

## 2、NAT 类型问题

1. 点击测试工具 -> NAT 检测，点击开始检测

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/Pasted%20image%2020240819163053.png)

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
	1. 若是使用服务器地址 101.200.86.248 连接：[查询 n2n edge 节点列表](http://101.200.86.248:10093/static/n2n-edge-query.html)
	2. 其他的服务器地址，则修改下面连接中的 ip 进行访问：http://ip:10093/static/n2n-edge-query.html
2. ip 是唯一的，ip 相同时即使小组不同也会导致冲突，无法连接
3. 和朋友一起联机的话，ip 前三位需要相同，比如：`192.168.1`，最后一位可选 `1 ~ 254`
4. 挑一个没有被使用的就可以了

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/C8BDC8FFEE9C4793B8F32A08E6EBCBBC.png)

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

![|700](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%B6%E4%BB%96/n2n/attachments/C80DC490867A47FDBD0E43F4BD2153D3.png)

## 5、
