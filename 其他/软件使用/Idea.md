# 一、快速注释ctrl+/，注释会在行首位置的问题
:::info
文件->设置->代码样式->代码生成->注释代码->取消行注释在第一列的勾选->勾选在行注释开始处添加空格即可

Code Generation --> Comment Code --> 取消 Line Comment at first column的勾选 --> 将Add a space at comment start
:::
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1658825963390-b9c0e003-f811-40af-9e20-7576ab4fb4f3.png#clientId=uc1ee5bf9-2dcd-4&from=paste&height=703&id=u138d3e0e&name=image.png&originHeight=703&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66566&status=done&style=none&taskId=u80993b9e-6b45-4dd9-a0ac-a3e47dc58c9&title=&width=982)
# 二、Toncat 在IDEA 控制台中文乱码
## 1、乱码
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667436807533-c9a06578-65fa-4415-88ca-194a8a1addca.png#averageHue=%23342d2c&clientId=ud5029737-dcc9-4&from=paste&height=161&id=u6dbf6827&name=image.png&originHeight=161&originWidth=573&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12762&status=done&style=none&taskId=uad724bc4-6874-43c9-b2ec-82c6fe4cef6&title=&width=573)
## 2、解决

1. 设置 IDEA

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667439212056-9361c276-6395-40d3-afb1-07e557945f6d.png#averageHue=%233d4146&clientId=ud5029737-dcc9-4&from=paste&height=703&id=ub913bb77&name=image.png&originHeight=703&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61196&status=done&style=none&taskId=uf2ab215f-3ab1-4871-aaa2-6aa48554c2f&title=&width=982)

2. 打开服务器配置，在虚拟机选项中输入：`-Dfile.encoding=UTF-8`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667437031145-d061051e-1fe2-4cb9-8d14-bd374542b0e8.png#averageHue=%233e444a&clientId=ud5029737-dcc9-4&from=paste&height=173&id=u2fb5cce1&name=image.png&originHeight=173&originWidth=274&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12705&status=done&style=none&taskId=u82790660-5845-4327-8952-ebc5a0eed7d&title=&width=274)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667437047934-dcdc30be-aeae-4859-b36d-9229532f9c31.png#averageHue=%233d4143&clientId=ud5029737-dcc9-4&from=paste&height=682&id=uc79f37ad&name=image.png&originHeight=682&originWidth=1076&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59898&status=done&style=none&taskId=u6f62bc68-e19d-4272-acb5-91db18341ee&title=&width=1076)

3. 点击帮助，编辑自定义 VM 选项，在最后加入：`-Dfile.encoding=UTF-8`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667440186706-eafa4b05-5c0f-4e2a-9657-799bf34e18fd.png#averageHue=%237a947e&clientId=ud5029737-dcc9-4&from=paste&height=494&id=u81842f0c&name=image.png&originHeight=494&originWidth=350&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44214&status=done&style=none&taskId=u41f32a21-ea43-448c-9faa-2b39b974a4a&title=&width=350)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667440228922-16c63d5c-448e-42c8-8fa0-9eb745ba53fc.png#averageHue=%232d2c2c&clientId=ud5029737-dcc9-4&from=paste&height=494&id=u6423549c&name=image.png&originHeight=494&originWidth=985&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46749&status=done&style=none&taskId=u95f6bf3a-a121-4bdb-894b-cafd1b72daa&title=&width=985)

4. 进入 IDEA 安装目录，进入 bin 目录，打开下面两个文件，在最后加入：`-Dfile.encoding=UTF-8`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667440357453-25d7578e-40e7-414b-89f8-84e8b4bfe206.png#averageHue=%23f7f5f3&clientId=ud5029737-dcc9-4&from=paste&height=631&id=ua64242f8&name=image.png&originHeight=631&originWidth=793&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97374&status=done&style=none&taskId=u439fb3d7-5b36-4ec8-b975-3a5699cbb8a&title=&width=793)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667440373960-22c59b31-ebe9-43e6-bf58-0b8b149138d4.png#averageHue=%23f2f0ee&clientId=ud5029737-dcc9-4&from=paste&height=564&id=ude0fabe8&name=image.png&originHeight=564&originWidth=630&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82262&status=done&style=none&taskId=uf0df0473-82b8-4dfd-b698-749a70d2c51&title=&width=630)

5. 进入 Tomcat 安装目录，进入 conf 目录，打开 logging.properties 文件，将 `java.util.logging.ConsoleHandler.encoding` 的值改为 `UTF-8`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1667440491949-a730b7bd-66e9-40a9-a0ca-f7c7de493992.png#averageHue=%23faf9f6&clientId=ud5029737-dcc9-4&from=paste&height=783&id=ub915ab76&name=image.png&originHeight=783&originWidth=1234&originalType=binary&ratio=1&rotation=0&showTitle=false&size=182273&status=done&style=none&taskId=u25001897-de3f-443c-a465-6c546aa2b68&title=&width=1234)
# 三、设置忽略文件

1. 设置 -> 编辑器 -> 文件类型 -> 忽略的文件和文件夹
2. 点击添加

![image.png](https://cdn.nlark.com/yuque/0/2023/png/29280567/1673424256072-7bc61d76-b9a5-40d1-837f-cf05152a8667.png#averageHue=%233d4247&clientId=uae114e32-055b-4&from=paste&height=712&id=ue347dac7&name=image.png&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48557&status=done&style=none&taskId=u292ecccc-deb4-4517-a907-f04b7bce96e&title=&width=982)

# 四、idea 启动时报错：Your JRE: 17.0.5+1-b653.14 amd64 (JetBrains s.r.o.) D:\Idea\IntelliJ IDEA 2022.3\jbr

![](attachments/Pasted%20image%2020230330080650.png)

1. 管理员方式运行如下命令：`netsh winsock reset`
2. 运行完成之后重启电脑即可永久解决此问题

# 五、
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
