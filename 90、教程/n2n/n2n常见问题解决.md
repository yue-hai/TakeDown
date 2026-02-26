### ①、点击启动后没有马上显示成功

1. 连接时，从点击启动到连接成功有时等待时间会稍长一点，等待 10 秒左右看看
2. 当在连接成功的状态下，点击停止断开连接后马上再点击启动（或点击重启），并不会马上重连，需要等待 1 ~ 2 分钟，这是服务器机制问题，等待即可

### ②、NAT 类型问题

1. 点击测试工具 -> NAT 检测，点击开始检测

![](../../../Docker/attachments/Pasted%20image%2020251111143709.png)

1. 若是显示检测失败或结果不是下面的四种，请点击切换服务器，然后多次测试
2. 若检测结果是 `Symmetric NAT`，说明当前机器是不可以使用 n2n 的，若想使用，请自行修改光猫，百度搜索：NAT 类型修改
	1. [家用路由器修改NAT1](https://www.bilibili.com/read/cv22212682/)
	2. [网络类型NAT3改NAT1 基于（联通）光猫桥接、路由器红米AX5、win10系统](https://blog.csdn.net/qq_46648437/article/details/113747066)
	3. [如何提升NAT类型，NAT提升至full_cone，设置光猫](https://blog.csdn.net/weixin_42168194/article/details/106037065)
3. 若不是 `Symmetric NAT`，而是其他三种，说明无法连接的原因不在这里
4. 几种常见的 NAT 类型：
	4. Full Cone
	5. Restricted Cone
	6. Port Restricted Cone
	7. Symmetric NAT

### ③、虚拟 ip 冲突

1. 进入下面的网址查看一下 ip 是不是已经被使用了：
	1. 若是使用服务器地址 101.200.86.248 连接：[查询 n2n edge 节点列表](http://101.200.86.248:41900/static/n2n-edge-query.html)
	2. 其他的服务器地址，则修改下面连接中的 ip 进行访问：http://ip:41900/static/n2n-edge-query.html
2. ip 是唯一的，ip 相同时即使小组不同也会导致冲突，无法连接
3. 和朋友一起联机的话，ip 前三位需要相同，比如：`192.168.1`，最后一位可选 `1 ~ 254`
4. 挑一个没有被使用的就可以了

![](../../../Docker/attachments/Pasted%20image%2020251111144005.png)

### ④、windows 防火墙的问题

1. 右键开始菜单，选择以**管理员模式**打开 `powershell`，执行下面命令就可以开启 v4 和 v6 的入站规则
2. 开启 v4 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V4" protocol=icmpv4:any,any dir=in action=allow
```

1. 开启 v6 的入站规则

```shell
netsh advfirewall firewall add rule name= "All ICMP V6" protocol=icmpv6:any,any dir=in action=allow
```

![](../../../Docker/attachments/Pasted%20image%2020251111144121.png)

### ⑤、

### ⑥、
