# 一、强制缩进为 4 格
1. 在设置中搜索 `Tab Size`，都改为 4

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657775107031-1efaa747-ff62-4c62-9cf0-4d7308d9edd3.png#clientId=u2bb42ce1-a8aa-4&from=paste&height=525&id=u8c6686a4&name=image.png&originHeight=525&originWidth=1167&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41641&status=done&style=none&taskId=u0d148278-9553-42e5-ad1d-991a4d23427&title=&width=1167)

2. 搜索 `detectindentation`，取掉勾选

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657775184916-aadb8e4d-ac7d-4b40-adf3-4559b969eba4.png#clientId=u2bb42ce1-a8aa-4&from=paste&height=376&id=uf1e70560&name=image.png&originHeight=376&originWidth=1164&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40506&status=done&style=none&taskId=uc84670ff-da97-4475-833f-0015018c423&title=&width=1164)

3. 之后格式化文档，代码就都是 4格缩进了
# 二、VScode 同步配置
## 1、上传

1. 安装 code settings sync 插件
2. gistId：`m6ldkic3y4woebju780ph46`
3. 码云私人令牌：`4369d7da5ea39e2e73ed497c17c36b44`
4. 在 settings.json 文件中输入：
```shell
// @code settings sync 插件 ==> 用于同步 vscode 插件与 settings.json 文件
// gist字符串，是 gitee 的代码片段生成的
"gitee.gist":"m6ldkic3y4woebju780ph46", 
// gitee的私人令牌
"gitee.access_token":"4369d7da5ea39e2e73ed497c17c36b44",
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662531253401-df826a09-9121-4c15-b53b-c0047c269263.png#clientId=ua334135b-0334-4&from=paste&height=768&id=njU3f&name=image.png&originHeight=768&originWidth=1024&originalType=binary&ratio=1&rotation=0&showTitle=false&size=108232&status=done&style=none&taskId=u194fb34f-0de3-4bde-9830-25b0e765dcf&title=&width=1024)

5. 用快捷键【Ctrl+Shift+P】在 VsCode 的上方召唤出命令行
6. 输入 `upload setting`，进行 vscode 的配置同步，有如下提示表示成功

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662531356959-ae0290ec-8f6a-4585-9f32-f1fbf63c86f2.png#clientId=ua334135b-0334-4&from=paste&height=768&id=uTAI6&name=image.png&originHeight=768&originWidth=1024&originalType=binary&ratio=1&rotation=0&showTitle=false&size=103195&status=done&style=none&taskId=ua0eb63b5-f918-489c-9d5f-731b8f1145a&title=&width=1024)
## 2、下载

1. 新电脑上的 vscode，先去安装插件【code settings sync】
2. 在 settings.json 文件中，把 gistID、私人密钥复制进去
3. 使用快捷键 【Ctrl+Shift+P】在 vscode 的上面唤出命令行，输入 download setting
# 三、根据之前补全过的建议的前缀来优先提示

1. 打开设置，搜索：Suggest Selection
2. 选择：recentlyUsedByPrefix

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662692942923-02ed88a4-0c4b-4514-ba98-e06323ae70a7.png#clientId=ue464b2f3-1fe7-4&from=paste&height=1027&id=ud5c1835f&name=image.png&originHeight=1027&originWidth=829&originalType=binary&ratio=1&rotation=0&showTitle=false&size=92487&status=done&style=none&taskId=u3888d3de-c099-4372-8d98-2cfdd62e398&title=&width=829)
# 四、
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
