# 一、快速注释 ctrl+/，注释会在行首位置的问题

1. 文件 -> 设置 -> 代码样式 -> 代码生成 -> 注释代码 -> 取消行注释在第一列的勾选 -> 勾选在行注释开始处添加空格即可
2. Code Generation -> Comment Code -> 取消 Line Comment at first column的勾选 -> 将 Add a space at comment start

![](attachments/Pasted%20image%2020230724103223.png)

# 二、Toncat 在 IDEA 控制台中文乱码

## 1、乱码

![](attachments/Pasted%20image%2020230724103300.png)

## 2、解决

1. 设置 IDEA

![](attachments/Pasted%20image%2020230724103339.png)

2. 打开服务器配置，在虚拟机选项中输入：`-Dfile.encoding=UTF-8`

![](attachments/Pasted%20image%2020230724103518.png)

![](attachments/Pasted%20image%2020230724103541.png)

3. 点击帮助，编辑自定义 VM 选项，在最后加入：`-Dfile.encoding=UTF-8`

![](attachments/Pasted%20image%2020230724103417.png)

![](attachments/Pasted%20image%2020230724103614.png)

4. 进入 IDEA 安装目录，进入 bin 目录，打开下面两个文件，在最后加入：`-Dfile.encoding=UTF-8`

![](attachments/Pasted%20image%2020230724103646.png)

![](attachments/Pasted%20image%2020230724103710.png)

5. 进入 Tomcat 安装目录，进入 conf 目录，打开 logging.properties 文件，将 `java.util.logging.ConsoleHandler.encoding` 的值改为 `UTF-8`

![](attachments/Pasted%20image%2020230724103728.png)

# 三、设置忽略文件

1. 设置 -> 编辑器 -> 文件类型 -> 忽略的文件和文件夹
2. 点击添加

![](attachments/Pasted%20image%2020230724103826.png)

# 四、idea 启动时报错：Your JRE: 17.0.5+1-b653.14 amd64 (JetBrains s.r.o.) D:\\Idea\\IntelliJ IDEA 2022.3\\jbr

![](attachments/Pasted%20image%2020230330080650.png)

1. 管理员方式运行如下命令：`netsh winsock reset`
2. 运行完成之后重启电脑即可永久解决此问题

# 五、离线下载插件

1. gitee 插件：[https://plugins.jetbrains.com/plugin/11491-gitee](https://plugins.jetbrains.com/plugin/11491-gitee)
2. 点击 Versions

![](attachments/Pasted%20image%2020230724124032.png)

3. 根据 idea 的版本号下载安装包

![](attachments/Pasted%20image%2020230724124054.png)

4. 下载完成后，在 idea 中点击设置 --> 插件 --> 设置 --> 从磁盘安装插件

![](attachments/Pasted%20image%2020230724124106.png)

5. 选择下载的安装包即可

![](attachments/Pasted%20image%2020230724124119.png)

# 六、开了 vpn，idea 推送到 github 还是失败

- 问题：浏览器可以访问 `github.com`，但是 idea 或者 gitbash 推送失败
- 原因：并不是所有软件或工具的网络请求都会走系统代理，有些应用的网络请求可能绕过代理，直接与网络通信。
- 解决：
1. 根据原因，我们可以分别给 idea 等工具和 git 分别设置代理即可
2. 如我使用的软件 Clash 的端口为 7890

![|700](attachments/Pasted%20image%2020231009092901.png)

3. 那么我 idea 中设置代理，使其走本机的 7890 端口，这样 idea 就可以访问外网了

![|700](attachments/Pasted%20image%2020231009093028.png)

4. 但是这样操作之后，idea 提交 git 还是失败，是因为 idea 也还是调用 gitbash 进行提交，所以我们还要设置 gitbash 的代理：

```bash
git config --global http.proxy http://127.0.0.1:7890 
git config --global https.proxy http://127.0.0.1:7890
```

5. 这样设置完就可以使用 gitbash 提交了

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
