# 一、强制缩进为 4 格

1. 在设置中搜索 `Tab Size`，都改为 4

![](attachments/Pasted%20image%2020230724103852.png)

2. 搜索 `detectindentation`，取掉勾选

![](attachments/Pasted%20image%2020230724103907.png)

3. 之后格式化文档，代码就都是 4格缩进了

# 二、根据之前补全过的建议的前缀来优先提示

1. 打开设置，搜索：Suggest Selection
2. 选择：recentlyUsedByPrefix

![](attachments/Pasted%20image%2020230724104016.png)

# 三、连接 linux 远程开发

1. 安装插件：`Remote - SSH`，安装时会自动安装另外两个插件：`Remote - SSH: Editing Configuration Files`、`Remote Explorer`

![](attachments/Pasted%20image%2020230525083915.png)

2. 安装完成后重启，左边侧边栏会多一个远程资源管理器的按钮，点击

![](attachments/Pasted%20image%2020230525084223.png)

3. 点击设置，打开 ssh 配置文件

![](attachments/Pasted%20image%2020230616150322.png)

4. 在配置文件中以下面的格式输入参数，尽量使用这个格式，其他格式或者有中文可能会报错

```ssh
Host 用户名@IP
    HostName IP
    Port 端口
    User 用户名
```

![](attachments/Pasted%20image%2020230525091005.png)

5. 保存配置文件后，点击刷新

![](attachments/Pasted%20image%2020230616150616.png)

6. 点击刷新后，新配置的连接就会显示出来

![](attachments/Pasted%20image%2020230525091210.png)

7. 点击后方按钮进行连接，第一个是在当前窗口进行连接，第二个是在新窗口进行连接

![](attachments/Pasted%20image%2020230525090043.png)

8. 选择连接的机器的系统类型

![](attachments/Pasted%20image%2020230525090240.png)

9. 询问是否继续，点击 `Continue` 继续

![](attachments/Pasted%20image%2020230525090435.png)

10. 输入密码，回车确认

![](attachments/Pasted%20image%2020230525090608.png)

11. 点击打开文件夹

![](attachments/Pasted%20image%2020230525091913.png)

12. 选择一个目录作为根目录，点击确定

![](attachments/Pasted%20image%2020230525091942.png)

13. 再次输入密码

![](attachments/Pasted%20image%2020230525092221.png)

14. 此时即可直接处理服务器上的文件

![](attachments/Pasted%20image%2020230525092032.png)

# 五、在上面的基础上，免除密码登录

1. 我使用的设备：本地 Windows，远程 ubuntu 服务器
2. 在本地打开 Windows PowerShell，输入：`ssh-keygen`，一直回车直到结束，若是已经生成过密钥，则可以跳过这一步
	1. `id_rsa`：私钥，本地机器使用
	2. `id_rsa.pub`：公钥，远程服务器使用

![](attachments/Pasted%20image%2020230616151933.png)

3. 在远程服务器的 ubuntu 用户根目录中，若没有 `.ssh` 目录，则创建，权限为 `700`
4. 将本地的文件 `C:\Users\10222148\.ssh\id_rsa.pub` 复制到 `.ssh` 目录中
5. 将 `id_rsa.pub` 追加到 `authorized_keys` 中：`cat id_rsa.pub >> authorized_keys`
6. 设置 `id_rsa.pub` 的权限为 `644`，设置 `authorized_keys` 的权限为 `600`
7. 重启SSH：`sudo service sshd restart
8. 若还是需要密码，执行命令：`sudo vim /etc/ssh/sshd_config`，查看下面的两项配置：

```vim
RSAAuthentication yes
PubkeyAuthentication yes
```

9. 主要是 `PubkeyAuthentication`，若是 `no` 则将其改为 `yes`，再次重启 SSH 尝试连接

# 六、

# 七、

# 八、

# 九、

# 十、

# 十一、

# 十二、

# 十三、

# 十四、

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、
