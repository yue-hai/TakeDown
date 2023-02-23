> 官网：[http://git-scm.com/](http://git-scm.com/)
> 高速下载地址：[https://registry.npmmirror.com/binary.html?path=git-for-windows/](https://registry.npmmirror.com/binary.html?path=git-for-windows/)
> [尚硅谷技术课程系列之Git V2.0.pdf](https://www.yuque.com/attachments/yuque/0/2022/pdf/29280567/1662532713147-4f4cabb5-041a-423e-a368-e65594da5199.pdf?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpdf%2F29280567%2F1662532713147-4f4cabb5-041a-423e-a368-e65594da5199.pdf%22%2C%22name%22%3A%22%E5%B0%9A%E7%A1%85%E8%B0%B7%E6%8A%80%E6%9C%AF%E8%AF%BE%E7%A8%8B%E7%B3%BB%E5%88%97%E4%B9%8BGit%20V2.0.pdf%22%2C%22size%22%3A5951277%2C%22type%22%3A%22application%2Fpdf%22%2C%22ext%22%3A%22pdf%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u0d358d34-625e-42b2-9fff-4bcd1a60d54%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u2946eaa7%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

# 一、Git 概述

1. Git 是一个免费的、开源的分布式版本控制系统，可以快速高效地处理从小型到大型的各种项目
2. Git 易于学习，占地面积小，性能极快。 
3. 它具有廉价的本地库，方便的暂存区域和多个工作流分支等特性。其性能优于 Subversion、CVS、Perforce 和 ClearCase 等版本控制工具。
## 1、何为版本控制

1. 版本控制是一种记录文件内容变化，以便将来查阅特定版本修订情况的系统。
2. 版本控制其实最重要的是可以记录文件修改历史记录，从而让用户能够查看历史版本，方便版本切换。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662015208639-d70bf5e3-aabf-4042-8b9d-8afc969a163b.png#clientId=u64789983-8ab7-4&from=paste&height=328&id=u2cde65e5&name=image.png&originHeight=328&originWidth=448&originalType=binary&ratio=1&rotation=0&showTitle=false&size=105419&status=done&style=stroke&taskId=ua60c23f5-aed0-4a7d-bd90-c1272189495&title=&width=448)
## 2、为什么需要版本控制

- 个人开发过渡到团队协作

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662015249351-7938fbd3-d0b1-49f3-bb86-ab6aaa61b6c7.png#clientId=u64789983-8ab7-4&from=paste&height=279&id=u1f13c319&name=image.png&originHeight=279&originWidth=555&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25626&status=done&style=stroke&taskId=u380e9e5f-b89e-4cfb-8187-8039d25d72d&title=&width=555)
## 3、版本控制工具
### ①、集中式版本控制工具

1. CVS、SVN(Subversion)、VSS……
2. 集中化的版本控制系统诸如 CVS、SVN 等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。多年以来，这已成为版本控制系统的标准做法。
3. 这种做法带来了许多好处，每个人都可以在一定程度上看到项目中的其他人正在做些什么。而管理员也可以轻松掌控每个开发者的权限，并且管理一个集中化的版本控制系统，要远比在各个客户端上维护本地数据库来得轻松容易。
4. 事分两面，有好有坏。这么做显而易见的缺点是中央服务器的单点故障。如果服务器宕机一小时，那么在这一小时内，谁都无法提交更新，也就无法协同工作

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662015740572-33f10476-2b76-458d-a87f-f9ffc40a9339.png#clientId=u64789983-8ab7-4&from=paste&height=341&id=udc3b7fdc&name=image.png&originHeight=342&originWidth=480&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71658&status=done&style=stroke&taskId=u6cc8750a-0ec6-4175-b6e1-bb8abef6318&title=&width=478)
### ②、分布式版本控制工具

1. Git、Mercurial、Bazaar、Darcs……
2. 像 Git 这种分布式版本控制工具，客户端提取的不是最新版本的文件快照，而是把代码仓库完整地镜像下来（本地库）。这样任何一处协同工作用的文件发生故障，事后都可以用其他客户端的本地仓库进行恢复。因为每个客户端的每一次文件提取操作，实际上都是一次对整个文件仓库的完整备份。
3. 分布式的版本控制系统出现之后，解决了集中式版本控制系统的缺陷：
   1. 服务器断网的情况下也可以进行开发（因为版本控制是在本地进行的）
   2. 每个客户端保存的也都是整个完整的项目（包含历史记录，更加安全）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662015894419-44e3863f-dbc5-4df1-b57d-67068878e7f8.png#clientId=u64789983-8ab7-4&from=paste&height=389&id=u37ba335d&name=image.png&originHeight=389&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84019&status=done&style=stroke&taskId=u7e95eacf-5568-42d4-a851-6e862d67d30&title=&width=454)
## 4、Git 简史
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662015977212-7f1111e7-8302-41ad-9c56-bdb1aac7ff05.png#clientId=u64789983-8ab7-4&from=paste&height=551&id=ue4e99083&name=image.png&originHeight=551&originWidth=1145&originalType=binary&ratio=1&rotation=0&showTitle=false&size=172606&status=done&style=stroke&taskId=u48e868c5-3afb-4690-b97d-46f75f9ac05&title=&width=1145)
## 5、Git 工作机制
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016085682-2175df04-67c5-4b2f-b3c5-16be44085011.png#clientId=u64789983-8ab7-4&from=paste&height=529&id=u8a57dd7c&name=image.png&originHeight=529&originWidth=538&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36330&status=done&style=stroke&taskId=uf76e0c06-b65d-48c8-a4d7-9ab9d71a08f&title=&width=538)
## 6、 Git 和代码托管中心
代码托管中心是基于网络服务器的远程代码仓库，一般我们简单称为远程库
### ①、局域网

1. GitLab
### ②、互联网

1. GitHub（外网）
2. Gitee 码云（国内网站）
# 二、Git 安装
## 1、下载
> 官网：[http://git-scm.com/](http://git-scm.com/)
> 高速下载地址：[https://registry.npmmirror.com/binary.html?path=git-for-windows/](https://registry.npmmirror.com/binary.html?path=git-for-windows/)

## 2、安装

1. 查看 GNU 协议，可以直接点击下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016522560-1335187d-1bf3-4775-878a-918d8124e3bb.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=uad9509d4&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21312&status=done&style=stroke&taskId=u581f3cdc-765a-4377-8bcf-ec8e6986069&title=&width=499)

2. 选择 Git 安装位置，要求是非中文并且没有空格的目录，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016746825-618cf3b9-d294-4bbe-b979-305931da0398.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=uf9f545f1&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15451&status=done&style=stroke&taskId=u884cbb24-3ffb-4438-bafc-0c9698402a8&title=&width=499)

3. Git 选项配置，推荐默认设置，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016801647-c9c612eb-a286-419d-ac37-3692c6d262e7.png#clientId=u64789983-8ab7-4&from=paste&height=422&id=u790c5e35&name=image.png&originHeight=422&originWidth=507&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89436&status=done&style=stroke&taskId=u1f934514-f84e-49fb-990a-d814c6bfc71&title=&width=507)

4. Git 安装目录名，不用修改，直接点击下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016864462-ea954438-f3a6-43c0-9b4e-bdf91468d1a6.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=u444fe5ca&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15036&status=done&style=stroke&taskId=u3868a9d8-05d6-4d50-b611-964b0cf73ff&title=&width=499)

5. Git 的默认编辑器，建议使用默认的 Vim 编辑器，然后点击下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662016895102-63b3e726-d957-4214-b5bb-ad3b7ba3abe1.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=ud22c1c52&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20997&status=done&style=stroke&taskId=u6a4c119f-d65c-4442-9a9d-f1c61828ebd&title=&width=499)

6. 默认分支名设置，选择让 Git 决定，分支名默认为 master，下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018152363-1dee1634-32f8-4c83-a54a-5441818149ad.png#clientId=u64789983-8ab7-4&from=paste&height=419&id=ue69d7cbd&name=image.png&originHeight=419&originWidth=506&originalType=binary&ratio=1&rotation=0&showTitle=false&size=86536&status=done&style=stroke&taskId=ue41cf674-36e2-4390-9924-d314d4ca155&title=&width=506)

7.  修改 Git 的环境变量，选第一个，不修改环境变量，只在 Git Bash 里使用 Git  

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018168506-b2ea8df7-1900-4809-b046-4cb26d7d55d9.png#clientId=u64789983-8ab7-4&from=paste&height=413&id=u40e371e0&name=image.png&originHeight=413&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106228&status=done&style=stroke&taskId=ua316b7a1-41a8-4cfb-8fe5-5ab951511ac&title=&width=500)

8. 选择后台客户端连接协议，选默认值 OpenSSL，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018182815-aca0d8e5-a182-466b-b724-421027dfeca0.png#clientId=u64789983-8ab7-4&from=paste&height=412&id=ud985f46c&name=image.png&originHeight=412&originWidth=495&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69949&status=done&style=stroke&taskId=ube5c1d94-cf34-4503-8a20-89f357732b5&title=&width=495)

9. 配置 Git 文件的行末换行符，Windows 使用 CRLF，Linux 使用 LF，选择第一个自动转换，然后继续下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018197889-df0435d0-28a8-4a35-b7bc-68fa2c06ba1e.png#clientId=u64789983-8ab7-4&from=paste&height=421&id=ud2ff423b&name=image.png&originHeight=421&originWidth=507&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109711&status=done&style=stroke&taskId=u040d4834-0576-4d07-8b40-c2e323f00a8&title=&width=507)

10. 选择 Git 终端类型，选择默认的 Git Bash 终端，然后继续下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018214726-b8b89069-0a0d-45c5-a8b2-4562055746a7.png#clientId=u64789983-8ab7-4&from=paste&height=428&id=u653c0edf&name=image.png&originHeight=428&originWidth=512&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112272&status=done&style=stroke&taskId=u786db0a7-fce0-474c-8457-3167eab5d39&title=&width=512)

11.  选择 Git pull 合并的模式，选择默认，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017104884-aee0db15-8794-4ca5-b155-ad7b8db6464c.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=u8d1459fe&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19202&status=done&style=stroke&taskId=uca27753b-bb3a-4b16-b85e-9068f54ee95&title=&width=499)

12. 选择 Git 的凭据管理器，选择默认的跨平台的凭据管理器，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017191125-fe1ff1ce-6697-4142-a97f-5ac55b793c7e.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=u722c0553&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15472&status=done&style=stroke&taskId=u9c8c2693-d5b5-4d57-a4fd-c324109c377&title=&width=499)

13. 其他配置，选择默认设置，然后下一步

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662018248286-5b2b0451-9294-4cb0-805b-06996bf29c01.png#clientId=u64789983-8ab7-4&from=paste&height=411&id=u4d952901&name=image.png&originHeight=411&originWidth=493&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60521&status=done&style=stroke&taskId=ub585fac6-cde0-4455-9fd3-273eb2f0fd1&title=&width=493)

14. 实验室功能，技术还不成熟，有已知的 bug，不要勾选，然后点击右下角的 Install 按钮，开始安装 Git

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017257612-90bb60c2-ebb6-42c9-99b1-e2ed03ee82af.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=u6476de13&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20234&status=done&style=stroke&taskId=u5bf8e5bb-8edd-4794-bb3f-41c60e4ac32&title=&width=499)

15. 点击 Finsh 按钮，Git 安装成功

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017381047-e65f297d-9858-4468-b004-52669a6ac4c1.png#clientId=u64789983-8ab7-4&from=paste&height=392&id=u2f793dda&name=image.png&originHeight=392&originWidth=499&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13907&status=done&style=stroke&taskId=u7668dd78-e1b0-4ddc-be1b-840ef13eac9&title=&width=499)

16. 右键任意位置，在右键菜单里选择 Git Bash Here 即可打开 Git Bash 命令行终端

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017400151-6886daa3-7d5b-401e-bb6d-8a8a05f4794f.png#clientId=u64789983-8ab7-4&from=paste&height=354&id=u37c368d2&name=image.png&originHeight=354&originWidth=265&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19619&status=done&style=stroke&taskId=u879ded6b-1f87-4e83-8ba5-3211914f569&title=&width=265)

17. 在 Git Bash 终端里输入 git --version 查看 git 版本，如图所示，说明 Git 安装成功
```shell
git --version
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662017458388-67019f75-2ae8-41e9-be3a-d5cbf18e1d52.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=uf0738710&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11973&status=done&style=stroke&taskId=u33aab550-03a9-4f87-84c6-16c620a46cc&title=&width=581)
# 三、Git 常用命令
| 命令名称 | 作用 |
| --- | --- |
| git config --global user.name 用户名 | 设置用户签名 |
| git config --global user.email 邮箱 | 设置用户签名 |
| git init | 初始化本地库 |
| git status | 查看本地库状态 |
| git add 文件名 | 添加到暂存区 |
| git commit -m "日志信息" 文件名 | 提交到本地库 |
| git reflog | 查看历史记录 |
|  git reset --hard 版本号 | 版本穿梭 |

## 1、设置用户签名：`git config --global user.name 用户名`

1. 签名的作用是区分不同操作者身份。用户的签名信息在每一个版本的提交信息中能够看到，以此确认本次提交是谁做的。
2. Git 首次安装必须设置一下用户签名，否则无法提交代码。
3. 注意：这里设置用户签名和将来登录 GitHub（或其他代码托管中心）的账号没有任何关系。

`git config --global user.name 用户名`
`git config --global user.email 邮箱`
### ①、设置用户签名

1. 设置用户签名
```shell
git config --global user.name yuehai
```

2. 查看是否设置成功，在电脑 C 盘：`C:\Users\用户\当前用户` 的目录下，打开 `.gitconfig` 文件即可看到设置的用户签名
```shell
[user]
	name = yuehai
```
### ②、设置用户邮箱

1. 设置用户邮箱
```shell
git config --global user.email yuehai.com
```

2. 查看是否设置成功，在电脑 C 盘：C:\Users\用户\当前用户 的目录下，打开 .gitconfig 文件即可看到设置的用户邮箱
```shell
[user]
	name = yuehai
	email = yuehai.com
```
## 2、初始化本地库：`git init`
`git init`
:::info
让 git 获取这个项目的管理权
:::

1. 进行需要使用 git 管理的项目

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662019479506-3cea7251-fd9b-46cf-b7b7-0bfe0d9b9624.png#clientId=u64789983-8ab7-4&from=paste&height=629&id=u9dc6ba1e&name=image.png&originHeight=629&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38503&status=done&style=stroke&taskId=ufd760084-5fa6-4bcc-91a3-9fcacc2f928&title=&width=894)

2. 右键鼠标，选择 Git Bash Here

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662019463851-aa226a37-370c-437d-81c0-328405417c48.png#clientId=u64789983-8ab7-4&from=paste&height=630&id=uf952433a&name=image.png&originHeight=630&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56100&status=done&style=stroke&taskId=u9338af3e-e6a6-47e9-9dd5-e13a31e0793&title=&width=894)

3. 输入命令：`git init`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662019673916-02a3a575-fded-432d-9335-47fe5c181ce8.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=uda549d5c&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12619&status=done&style=stroke&taskId=u7c75afcd-c808-44d5-9561-c93bf92ffd4&title=&width=581)

4. 完成后会在该目录生成 `.git` 目录，此时初始化完成

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662019746008-b1f18975-d8c4-48e7-a5f7-32abc4c24b7f.png#clientId=u64789983-8ab7-4&from=paste&height=626&id=u4d2febba&name=image.png&originHeight=626&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39094&status=done&style=stroke&taskId=ub4f61104-ca93-45cb-9f21-e861475260d&title=&width=894)
## 3、查看本地库状态：`git status`
`git status`
### ①、首次查看（工作区没有任何文件）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662020708473-8bec6be0-f60a-4193-a849-b00f619cba2f.png#clientId=u64789983-8ab7-4&from=paste&height=630&id=u135bb222&name=image.png&originHeight=630&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36784&status=done&style=stroke&taskId=u308bc4ed-a112-4eb4-a002-c9f027591e9&title=&width=894)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662020675866-ed2e79bc-d188-42d6-8aee-5ed205ad52f7.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=u7efb451a&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19407&status=done&style=stroke&taskId=u52b62a4e-02f1-4f51-aa69-2a020fb269b&title=&width=581)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ②、新增文件（hello.txt）、再次查看（检测到未追踪的文件）

1. 创建文件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662020743006-3c39de3f-76e4-4810-88e8-289cdcc9052c.png#clientId=u64789983-8ab7-4&from=paste&height=630&id=uc3d362a4&name=image.png&originHeight=630&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39206&status=done&style=stroke&taskId=u20ec6cf2-ffba-4c7b-a7af-2ff0a6f87ff&title=&width=894)

2. 提示 hello.txt 只存在于工作区，并没有被追踪

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662020827504-2ac74d52-3b96-4197-9118-bfef194526aa.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=ue19b7909&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26117&status=done&style=stroke&taskId=u2dce35b2-1359-4605-9a65-bc9dc9d546c&title=&width=581)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present (use "git add" to track)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
## 4、添加暂存区：`git add 文件名`
`git add 文件名`
### ①、将工作区的文件添加到暂存区
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662021163300-c2240c87-21b3-44d9-b8fd-68305fd9b438.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=u1541b94b&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27457&status=done&style=stroke&taskId=u0724766f-25ab-4486-8827-d3bcb67d532&title=&width=581)
```shell
git add hello.txt
```
### ②、再次查看本地库状态（检测到暂存区有新文件）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662021229407-6b851df3-b8c5-40fc-b319-f0f9a99f7019.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=ud5f1b242&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25518&status=done&style=stroke&taskId=u706138c1-cd27-4836-83c1-49b10fb36f5&title=&width=581)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.txt


10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ③、删除暂存区的文件
`git rm --cached 文件名`

1. 这只是删除了暂存区的文件，并没有删除本地文件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662021423065-e6cfd672-90a6-4d4b-9cd5-2c1756003acf.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=u13d548fb&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23952&status=done&style=stroke&taskId=u3997c84c-d147-4e99-afbd-b27ff244f91&title=&width=581)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git rm --cached hello.txt
rm 'hello.txt'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$
```

2. 删除后再查看本地库状态

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662021508550-a10ec378-e88c-4bfd-b5d1-06573b2b12d4.png#clientId=u64789983-8ab7-4&from=paste&height=370&id=u7d43cc5e&name=image.png&originHeight=370&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24540&status=done&style=stroke&taskId=u69c820fe-09b3-4ff8-b2e9-7040a634ec5&title=&width=581)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present (use "git add" to track)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

3. 再加回去
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git add hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
## 5、提交本地库：`git commit -m "日志信息" 文件名`
`git commit -m "日志信息" 文件名`

- 不添加 `-m` 参数的话，也会弹出来弹窗让输入信息
### ①、将暂存区的文件提交到本地库
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022051686-d4da01d5-1080-4ff9-ba83-0fe5a8afa95d.png#clientId=u64789983-8ab7-4&from=paste&height=610&id=u8b8ac690&name=image.png&originHeight=610&originWidth=773&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56821&status=done&style=stroke&taskId=u62575d3f-bfd8-4592-8476-1b2410bec6e&title=&width=773)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git commit -m "yuehai01"  hello.txt
[master (root-commit) da7a36f] yuehai01
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ②、查看状态（没有文件需要提交）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662021949737-8d3eaaef-b9c7-48cb-9c73-7a2553f30d1d.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=u695a48ce&name=image.png&originHeight=612&originWidth=777&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53315&status=done&style=stroke&taskId=u9d6d69a6-a285-45e9-9768-c3b9cf99f64&title=&width=777)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master
nothing to commit, working tree clean

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
## 6、查看本地库日志：`git reflog、git log`
### ①、查看本地库版本号
`git reflog`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022129318-a30199f3-b60c-4609-afd3-a2639dbd75e9.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=D2VhJ&name=image.png&originHeight=612&originWidth=777&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55582&status=done&style=stroke&taskId=u6c45cd63-8581-4add-a466-03c240f8a7e&title=&width=777)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git reflog
da7a36f (HEAD -> master) HEAD@{0}: commit (initial): yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ②、查看本地库日志
`git log`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022447475-be8f4cc9-c5fc-4e20-8622-3c4844d46ddf.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=u9ab76031&name=image.png&originHeight=612&originWidth=1074&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73951&status=done&style=stroke&taskId=ufb2aa6cb-d0b9-4aa9-8214-83545db4eb4&title=&width=1074)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git log
commit da7a36fb146a9982e8c7af401d4d171d8a6ab040 (HEAD -> master)
Author: yuehai <yuehai.com>
Date:   Thu Sep 1 16:42:59 2022 +0800

    yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
## 7、修改文件、将其再次添加到暂存区
### ①、修改文件（hello.txt）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022649037-8980679f-2cf0-41eb-8034-4cbf443b6a1b.png#clientId=u64789983-8ab7-4&from=paste&height=648&id=u18fef9cb&name=image.png&originHeight=648&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24525&status=done&style=stroke&taskId=uf300ef44-1d36-4233-be1b-0f5e6efc629&title=&width=655)
### ②、查看状态（检测到工作区有文件被修改）
`git status`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022689484-4efec70c-87ae-479e-a4cc-d69d230213ec.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=u02cef143&name=image.png&originHeight=612&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59950&status=done&style=stroke&taskId=ud4b208e0-b442-4aac-aee0-8e748d19a9f&title=&width=768)
### ③、将修改的文件再次添加暂存区
`git add hello.txt`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022724386-3932b25b-42a2-4c13-a597-702a38d744bb.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=u907caf35&name=image.png&originHeight=612&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60058&status=done&style=stroke&taskId=u8a2dcb8a-0dbd-46f3-bca7-5eab1f5a6a2&title=&width=768)
### ④、查看状态（工作区的修改添加到了暂存区）
`git status`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662022754967-9eeeefa4-6915-48a6-80f0-60c0e1338f49.png#clientId=u64789983-8ab7-4&from=paste&height=612&id=u406d5726&name=image.png&originHeight=612&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56976&status=done&style=stroke&taskId=u9441b573-acf5-4fd2-b5c4-ee7cf52c381&title=&width=768)
## 8、历史版本切换
:::info
每提交一次本地库会生成一个新版本
:::
### ①、查看历史版本
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662079049246-f3122b99-4641-4de7-9009-50d2d4563fc7.png#clientId=u90a0343c-dd16-4&from=paste&height=706&id=ua52ed639&name=image.png&originHeight=706&originWidth=847&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76965&status=done&style=stroke&taskId=u5662d031-ee74-489c-8cac-23f66b4a654&title=&width=847)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git reflog
03a9c58 (HEAD -> master) HEAD@{0}: commit: yuehai02
da7a36f HEAD@{1}: commit (initial): yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git log
commit 03a9c58da9b174b5fd761d1589ee8a706a7e8584 (HEAD -> master)
Author: yuehai <yuehai.com>
Date:   Fri Sep 2 08:30:51 2022 +0800

    yuehai02

commit da7a36fb146a9982e8c7af401d4d171d8a6ab040
Author: yuehai <yuehai.com>
Date:   Thu Sep 1 16:42:59 2022 +0800

    yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ②、版本穿梭
`git reset --hard 版本号`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662079502899-d94674ca-8487-4f08-92dc-f2b04c12ea8f.png#clientId=u90a0343c-dd16-4&from=paste&height=307&id=u324e2c33&name=image.png&originHeight=307&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47155&status=done&style=stroke&taskId=u11d0650f-ee26-4bb1-9d8a-c5ac3edefa9&title=&width=828)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git reset --hard da7a36f
HEAD is now at da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git reflog
da7a36f (HEAD -> master) HEAD@{0}: reset: moving to da7a36f
03a9c58 HEAD@{1}: commit: yuehai02
da7a36f (HEAD -> master) HEAD@{2}: commit (initial): yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

- 本地的文件变了

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662079628334-1284c5dd-0ba1-4f7a-81d2-3d5f327b7bd3.png#clientId=u90a0343c-dd16-4&from=paste&height=648&id=u1a4b2bc6&name=image.png&originHeight=648&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23765&status=done&style=stroke&taskId=u939452cd-d105-4d63-adb6-b8f9a1fb072&title=&width=655)
### ③、查看是否成功回溯版本

- 在工作目录下的 `.git\refs\heads\master` 文件中会显示当前版本的完整版本号
### ④、Git 切换版本，底层其实是移动的 HEAD 指针
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662079853619-46272502-ad82-4c12-b545-305611c5b8b3.png#clientId=u90a0343c-dd16-4&from=paste&height=403&id=ubb5f483f&name=image.png&originHeight=403&originWidth=992&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13528&status=done&style=stroke&taskId=ud6afc8ae-4e82-4f01-af9a-05f770c426e&title=&width=992)
# 四、Git 分支操作
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662080181095-ab51ef38-7f33-45d8-b780-8ef7b95593c9.png#clientId=u90a0343c-dd16-4&from=paste&height=416&id=u3efc084d&name=image.png&originHeight=416&originWidth=1093&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76867&status=done&style=stroke&taskId=ude5fb102-b610-44b0-81ea-95a756ce937&title=&width=1093)
## 1、什么是分支
**在版本控制过程中，同时推进多个任务，为每个任务，我们就可以创建每个任务的单独分支。使用分支意味着程序员可以把自己的工作从开发主线上分离开来，开发自己分支的时候，不会影响主线分支的运行。对于初学者而言，分支可以简单理解为副本，一个分支就是一个单独的副本。（分支底层其实也是指针的引用）**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662080265148-7bad4d44-1d1c-4819-85ef-1daea29849eb.png#clientId=u90a0343c-dd16-4&from=paste&height=435&id=u1186945f&name=image.png&originHeight=435&originWidth=1057&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67014&status=done&style=stroke&taskId=u2bd2aed8-955b-4916-8e30-21071e4fc9a&title=&width=1057)
## 2、分支的好处

1. 同时并行推进多个功能开发，提高开发效率。
2. 各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的分支删除重新开始即可。
## 3、分支的操作
| 命令名称 | 作用 |
| --- | --- |
| git branch 分支名  | 创建分支 |
| git branch -v | 查看分支 |
| git checkout 分支名 | 切换分支 |
| git merge 分支名  | 把指定的分支合并到当前分支上 |

### ①、查看分支
`git branch 分支名`
`*****`**代表当前所在的分区**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662080925281-835cea1e-b288-41dd-b1dc-051b5d2d687b.png#clientId=u90a0343c-dd16-4&from=paste&height=122&id=u6c52905d&name=image.png&originHeight=122&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12521&status=done&style=stroke&taskId=uaf240582-be1b-4688-bd0d-ae96e7d0818&title=&width=624)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ②、创建分支
`git branch 分支名`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662081467887-3fb149df-6803-4d8a-9b7f-58e3cabe4e33.png#clientId=u90a0343c-dd16-4&from=paste&height=256&id=u6ec38bec&name=image.png&originHeight=256&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33837&status=done&style=stroke&taskId=ub483a269-4b76-4d5e-96ee-6ac2e56c4fd&title=&width=828)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   da7a36f yuehai01
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ③、修改分支

1. 修改文件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082041180-76dc0ff8-321a-4c04-9706-343482063d04.png#clientId=u90a0343c-dd16-4&from=paste&height=648&id=u4ea0aaca&name=image.png&originHeight=648&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26535&status=done&style=stroke&taskId=u9d910973-7c92-417b-9b37-c0ef8646f48&title=&width=655)

2. 提交到暂存区，然后提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082117934-7159b698-ad29-433a-8fbe-8a206d9157e3.png#clientId=u90a0343c-dd16-4&from=paste&height=363&id=u6e177cff&name=image.png&originHeight=363&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37760&status=done&style=stroke&taskId=u820edc9d-33c8-4ce1-81ae-e985cdbcdb4&title=&width=828)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.txt

no changes added to commit (use "git add" and/or "git commit -a")

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git add hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git commit -m "yuehai02"
[master 5500b6e] yuehai02
 1 file changed, 3 insertions(+), 1 deletion(-)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

3. 再次查看状态

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082167355-5dab44a4-3a21-4704-a865-00dc27fd60d4.png#clientId=u90a0343c-dd16-4&from=paste&height=138&id=u3ab8efc0&name=image.png&originHeight=138&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14321&status=done&style=stroke&taskId=ube9444cd-f5ef-4456-b513-ac7069efab9&title=&width=828)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   5500b6e yuehai02
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ④、切换分支
`git checkout 分支名`

1. 查看分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082373146-afa3cd71-1739-4790-81da-83a5c5c19dcf.png#clientId=u90a0343c-dd16-4&from=paste&height=139&id=u7e23dffc&name=image.png&originHeight=139&originWidth=619&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13924&status=done&style=stroke&taskId=u3237d935-908c-4b3b-a3ca-dd1906c0229&title=&width=619)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   5500b6e yuehai02
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

2. 切换分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082505525-9b3dea49-d855-4ae9-8d6b-753d12637cef.png#clientId=u90a0343c-dd16-4&from=paste&height=121&id=ue8eac7bc&name=image.png&originHeight=121&originWidth=763&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18558&status=done&style=stroke&taskId=ue0b98166-0c13-4699-8b56-42405dde6e8&title=&width=763)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git checkout yuehai01
Switched to branch 'yuehai01'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$

```

3. 切换后发现文件被改变

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662082546510-99177432-7782-4105-8c20-fab8d409f6ea.png#clientId=u90a0343c-dd16-4&from=paste&height=648&id=u45b2af72&name=image.png&originHeight=648&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24099&status=done&style=stroke&taskId=ued7b4846-bd78-4166-937d-acd94e64718&title=&width=655)
### ⑤、合并分支

- 将指定的分支合并到当前分支上

`git merge 分支名`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662095335722-7e3269c2-6335-4355-8213-155494034e85.png#clientId=u08557644-209a-4&from=paste&height=279&id=u63d656f9&name=image.png&originHeight=279&originWidth=629&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29355&status=done&style=stroke&taskId=u901b7cb3-a2de-4f7e-8e26-15cc6ed668b&title=&width=629)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$ git branch -v
  master   5500b6e yuehai02
* yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$ git checkout master
Switched to branch 'master'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git merge yuehai01
Already up to date.

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
### ⑥、产生冲突

1. 冲突产生的原因：合并分支时，两个分支在同一个文件的同一个位置有两套完全不同的修改。Git 无法替我们决定使用哪一个。必须人为决定新代码内容
2. 冲突产生的表现：后面状态为 MERGING

---

1. 修改 master 的文件，并提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096156350-ad06bb58-77fb-4600-96a8-201c99266445.png#clientId=u08557644-209a-4&from=paste&height=636&id=u8b386788&name=image.png&originHeight=636&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28460&status=done&style=stroke&taskId=ub9253862-9081-40e0-9405-2d33d5310d6&title=&width=655)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   5500b6e yuehai02
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git checkout master
Already on 'master'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git add hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git commit -m "yuehai02"
[master 5500b6e] yuehai02
 1 file changed, 3 insertions(+), 1 deletion(-)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$
```

2. 修改 yuehai01 的文件，并提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096352652-3552911c-5b82-4f66-8db8-81216d4d8a2c.png#clientId=u08557644-209a-4&from=paste&height=636&id=u3e50f01f&name=image.png&originHeight=636&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24458&status=done&style=stroke&taskId=u725c8617-6096-4369-b281-b2a291c40d3&title=&width=655)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git checkout yuehai01
Switched to branch 'yuehai01'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$ git add  hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$ git commit -m "yuehai-01"
[yuehai01 42f5dd1] yuehai-01
 1 file changed, 2 insertions(+), 1 deletion(-)

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$
```

3. 切换到 master 分支，然后合并 yuehai01 分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096564663-843c8568-fdfa-411e-80b5-4c2e25618764.png#clientId=u08557644-209a-4&from=paste&height=221&id=u1c4e7077&name=image.png&originHeight=221&originWidth=672&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24373&status=done&style=stroke&taskId=u801f4fd8-0a7b-43a6-b8ff-34db80f2180&title=&width=672)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$ git checkout master
Switched to branch 'master'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git merge yuehai01
Auto-merging hello.txt
CONFLICT (content): Merge conflict in hello.txt
Automatic merge failed; fix conflicts and then commit the result.

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master|MERGING)
$

```

4. 此时的 hello.txt 文件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096790942-92393cd8-ca94-483c-bf16-a072a50861fb.png#clientId=u08557644-209a-4&from=paste&height=636&id=udff5a69a&name=image.png&originHeight=636&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41109&status=done&style=stroke&taskId=u292f911f-42c9-4849-acae-268e3a6670b&title=&width=655)

5. 查看本地库状态

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096678416-9b03ee51-f259-4115-8175-b46bccca1a46.png#clientId=u08557644-209a-4&from=paste&height=273&id=u3f97aadf&name=image.png&originHeight=273&originWidth=677&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24039&status=done&style=stroke&taskId=u773fd6ca-ae74-4705-8fed-cbabf3720e3&title=&width=677)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   hello.txt

no changes added to commit (use "git add" and/or "git commit -a")

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master|MERGING)
$

```
### ⑦、解决冲突

1. 打开有冲突的文件
:::info
特殊符号：<<<<<<< HEAD 当前分支的代码 ======= 合并过来的代码 >>>>>>> yuehai01
:::
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662096790942-92393cd8-ca94-483c-bf16-a072a50861fb.png#clientId=u08557644-209a-4&from=paste&height=636&id=LWPYc&name=image.png&originHeight=636&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41109&status=done&style=stroke&taskId=u292f911f-42c9-4849-acae-268e3a6670b&title=&width=655)

2. 手动选择要保留的内容；选择保留 master 分支的内容

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662097236578-6f063fd3-e0c8-46dd-aa0c-e2ca3f19f9ed.png#clientId=u08557644-209a-4&from=paste&height=636&id=u7b60fa38&name=image.png&originHeight=636&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27745&status=done&style=stroke&taskId=u66d8dd44-bb55-4971-8b0e-5dfdb7993c0&title=&width=655)

3. 修改完文件后，将其提交到本地库，注意此时不要指定文件名

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662097425998-165c56cc-90a8-4762-9606-3fe310cad3fc.png#clientId=u08557644-209a-4&from=paste&height=173&id=ua6747856&name=image.png&originHeight=173&originWidth=673&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19050&status=done&style=stroke&taskId=u55cc0c22-6f01-48d4-9de2-6ba0be9b751&title=&width=673)
```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master|MERGING)
$ git add hello.txt

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master|MERGING)
$ git commit -m "master-02"
[master e6069a2] master-02

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```
## 4、创建分支和切换分支图解

1. master、yuehai01（ hot-fix  ） 其实都是指向具体版本记录的指针。当前所在的分支，其实是由 HEAD 决定的。所以创建分支的本质就是多创建一个指针。
2. HEAD 如果指向 master，那么我们现在就在 master 分支上。
3. HEAD 如果执行 yuehai01（ hot-fix  ），那么我们现在就在 yuehai01（ hot-fix  ） 分支上。
4. 所以切换分支的本质就是移动 HEAD 指针。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662097570918-b0cebab5-5321-4e3d-9b78-dd7a163c6a07.png#clientId=u08557644-209a-4&from=paste&height=707&id=ubff08e4f&name=image.png&originHeight=707&originWidth=1436&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97427&status=done&style=stroke&taskId=ub46c92cf-19f7-41e2-99a1-c4daa82a485&title=&width=1436)
# 五、Git 团队协作机制
## 1、团队内协作
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662098736671-69bc9806-411a-47b0-a117-742a244b1e89.png#clientId=u08557644-209a-4&from=paste&height=568&id=udb63debc&name=image.png&originHeight=568&originWidth=961&originalType=binary&ratio=1&rotation=0&showTitle=false&size=155948&status=done&style=stroke&taskId=u0de7f2f1-45d6-42fa-8f50-5502273fa72&title=&width=961)
## 2、跨团队协作
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662098754716-6339b77a-90f3-46d1-a43b-9dcc0cdc265e.png#clientId=u08557644-209a-4&from=paste&height=564&id=ue7e4b3f8&name=image.png&originHeight=564&originWidth=1136&originalType=binary&ratio=1&rotation=0&showTitle=false&size=239496&status=done&style=stroke&taskId=u9a19ef30-9c15-4b54-beb3-424f688f576&title=&width=1136)
# 六、GitHub 操作
> [https://www.bilibili.com/video/BV1vy4y1s7k6?p=20&vd_source=b55e15966ca689b32671d4aa387cab01](https://www.bilibili.com/video/BV1vy4y1s7k6?p=20&vd_source=b55e15966ca689b32671d4aa387cab01)

# 七、IDEA 集成 Git
## 1、配置 Git 忽略文件
### ①、Eclipse 特定文件
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662340727857-2fcac31c-e572-4fce-8074-baf71c13e953.png#clientId=ub791c6f4-bf99-4&from=paste&height=367&id=uf601f7b9&name=image.png&originHeight=367&originWidth=339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=64546&status=done&style=stroke&taskId=ue5f3d57c-3308-4a17-bf5f-f8c31db5f5b&title=&width=339)
### ②、IDEA 特定文件
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662340751172-228e61d2-099a-4645-a10b-a559becafaf7.png#clientId=ub791c6f4-bf99-4&from=paste&height=237&id=u57b58ddf&name=image.png&originHeight=237&originWidth=309&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23295&status=done&style=stroke&taskId=uf75cb20e-043a-4b39-b3a8-bb83aa93d71&title=&width=309)
### ③、Maven 工程的 target 目录
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662340776375-96d43010-fe86-4eec-89d2-d4873a23250a.png#clientId=ub791c6f4-bf99-4&from=paste&height=318&id=ua39fdc3b&name=image.png&originHeight=318&originWidth=252&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23933&status=done&style=stroke&taskId=u1c961e95-68b2-4050-9045-ed4ec0f6a3e&title=&width=252)
### ④、为什么要忽略他们？
与项目的实际功能无关，不参与服务器上部署运行。把它们忽略掉能够屏蔽 IDE 工具之间的差异
### ⑤、怎么忽略？

1. 创建忽略规则文件 xxxx.ignore（前缀名随便起，建议是 git.ignore）
2. 这个文件的存放位置原则上在哪里都可以，为了便于让~/.gitconfig 文件引用，建议也放在用户家目录下
3. git.ignore 文件模版内容如下：
```shell
# Compiled class file
*.class
# Log file
*.log
# BlueJ files
*.ctxt
# Mobile Tools for Java (J2ME)
.mtj.tmp/
# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar
# virtual machine crash logs, see 
http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
.classpath
.project
.settings
target
.idea
*.iml

```

4. 在.gitconfig 文件中引用忽略配置文件（此文件在 Windows 的家目录中）
```shell
[user]
name = Layne
email = Layne@atguigu.com
[core]
excludesfile = C:/Users/asus/git.ignore

注意：这里要使用“正斜线（/）”，不要使用“反斜线（\）”
```
## 2、定位 Git 程序
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662341459357-932914f4-db59-430b-be51-c6fdbff6c2b0.png#clientId=ub791c6f4-bf99-4&from=paste&height=700&id=uea6b5ad8&name=image.png&originHeight=700&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74771&status=done&style=stroke&taskId=ua829b2a9-ecd5-454c-9648-2e8dabe20b4&title=&width=982)
## 3、初始化本地库
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662341806100-a4ff3625-50c7-4938-8db0-1eae101d6a35.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ub72020f6&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71687&status=done&style=stroke&taskId=u17cf13e3-9fc8-4b3d-ac04-d881c42db81&title=&width=846)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662341870826-5837f177-eec4-422c-8327-858fe7f8573b.png#clientId=ub791c6f4-bf99-4&from=paste&height=510&id=u480ba549&name=image.png&originHeight=510&originWidth=424&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33243&status=done&style=stroke&taskId=u67482018-271f-45d4-a011-e1c6de9228f&title=&width=424)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662341932193-5b53ef03-793c-47e1-89ba-00d773fe14a2.png#clientId=ub791c6f4-bf99-4&from=paste&height=607&id=ud8a661d1&name=image.png&originHeight=607&originWidth=793&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41525&status=done&style=stroke&taskId=u1abc79aa-cb7b-40f8-895f-06a552e3239&title=&width=793)
## 4、添加到暂存区
### ①、手动添加到暂存区

1. 刚初始化本地库后 pom 文件是红色的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662342262077-8b297830-4caa-4e39-9652-4bdea169182e.png#clientId=ub791c6f4-bf99-4&from=paste&height=256&id=JqeOd&name=image.png&originHeight=256&originWidth=287&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10875&status=done&style=stroke&taskId=u634b99f4-2f29-4b7f-80a1-383c6e36064&title=&width=287)

2. 右键项目，git --> add，将整个项目添加到暂存区，pom 文件就会变为绿色

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662342337028-e618ea02-46e9-42e5-a101-0db226809c97.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=FTeSa&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=114764&status=done&style=stroke&taskId=u9ea9c73c-ff02-4d5d-a862-021536835e6&title=&width=846)

3. 添加完成

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662342365965-d87c0670-cbd9-4d32-b798-3383e0f0d5a5.png#clientId=ub791c6f4-bf99-4&from=paste&height=253&id=sQ4dK&name=image.png&originHeight=253&originWidth=287&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10810&status=done&style=stroke&taskId=u99f9d35d-43a0-453e-9943-27d5ed5c435&title=&width=287)
### ②、自动添加到暂存区

1. 创建文件后，idea 会询问是否自动添加到暂存区，可以选择确定

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662342776290-23a7041c-3369-41d5-9220-adef29b12702.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ub982aced&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73449&status=done&style=stroke&taskId=ua71f7c32-2df0-4617-bcb7-60c25f77464&title=&width=846)
## 5、提交到本地库
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662356615720-4724fd9a-4167-450b-97fb-b206ca09f24d.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u26b36ac7&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77148&status=done&style=stroke&taskId=u2498e3aa-207d-491d-8dd8-77b3aad94ea&title=&width=846)
## 6、切换版本

1. 修改一下代码

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662356900282-6cdeea1d-68c3-45f6-ad3b-afefc1ecb34c.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u8ffd432a&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85360&status=done&style=stroke&taskId=ufbf6341c-8304-426d-9344-3c917751591&title=&width=846)

2. 再次提交

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662356944654-bb8eb863-b0d5-4397-9242-f08e886d4b37.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u6f360b6a&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82308&status=done&style=stroke&taskId=ue4ece98a-cfee-43d6-afe4-902fb9e2340&title=&width=846)

3. 查看版本

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662357257730-67bf0fd1-3b56-4e4b-a042-8c0ee3f127b5.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u16d22941&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=96635&status=done&style=stroke&taskId=ucd6bd196-67d7-4ba8-9672-5fac170886e&title=&width=846)

4. 切换版本；右键要切换的版本，选择 Checkout Revision

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662357603161-627bacb2-3fdb-40eb-911b-ecf1d85ea228.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u4a172edb&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104585&status=done&style=stroke&taskId=ub06d8152-9481-4b19-ae17-fe661cb9408&title=&width=846)

5. 切换到了之前的版本

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662357696470-3e0285a4-b68d-4c19-8cbc-6d0e53568d16.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u6422ccaf&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=87788&status=done&style=stroke&taskId=ue417af4c-4387-49bf-95d1-fedc6f2f4db&title=&width=846)

6. 切换会 master 版本

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662357754614-415aa1ff-9039-4d56-b0cc-2edf323812ae.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u672c073e&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=100954&status=done&style=stroke&taskId=u0b4b4be6-41e5-48fc-a3a5-6c852f6b6f5&title=&width=846)
## 7、创建分支

1. 点击 `git --> log --> 选择版本 --> 右键 --> 新分支`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358002006-820dd3c9-4176-4263-be93-e55931292964.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u97eb2047&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=99946&status=done&style=stroke&taskId=ucceb2f38-0606-4ef8-8ee2-c1a7a4f25bf&title=&width=846)

2. 输入分支名称

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358034083-21e3d0b2-52cb-4020-8498-866357212765.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ue93c9083&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104787&status=done&style=stroke&taskId=ube2a72c9-1879-42b3-9b40-b92afe573c3&title=&width=846)

3. 创建完后会自动切换到该分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358280008-92dc4983-3fba-4de6-8a56-e6807699eea4.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u68b225ca&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109152&status=done&style=stroke&taskId=u0dab69a4-b978-4d10-8b42-e3f691d7a50&title=&width=846)
## 8、切换分支

1. 在 `git --> log` 中选择要切换的分支，右键选择检出即可切换

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358433914-e9c478dd-6c8c-4153-afaa-728fd51349eb.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ue0060e79&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=105851&status=done&style=stroke&taskId=ub7939866-8b2f-4b91-87cc-19f9f2bfe3e&title=&width=846)

2. 也可以左键点击右下角的分支名，在弹出来的弹窗中选择分支进行切换

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358559409-f940135e-b4e9-4c5b-b4a2-7ea807836db7.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ufd837d0b&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=98770&status=done&style=stroke&taskId=u3a48b6c9-dd60-42ca-a527-1b4d70d94e0&title=&width=846)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358606726-e511541c-b040-476d-a89d-a784b01e50ad.png#clientId=ub791c6f4-bf99-4&from=paste&height=1033&id=u806ab1be&name=image.png&originHeight=1033&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106612&status=done&style=stroke&taskId=u5075009d-eee6-414f-96be-ada3ef51100&title=&width=846)

3. 切换完毕后的样子

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358647150-4e136b6d-227e-4650-a94d-291d282bcb5b.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ud99b99cc&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=95260&status=done&style=stroke&taskId=ufcf061d7-5986-4bff-86bb-882599f5098&title=&width=846)
## 9、合并分支

1. 修改 yuehai 分支的代码，提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662358921024-24dd1a2a-f04a-48af-a56f-b509649cda86.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u49d7192f&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102392&status=done&style=stroke&taskId=u028970eb-e819-4f21-88fa-65026fd875c&title=&width=846)

2. 切换到 master 分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662359074619-7196d853-c7e7-4387-9c76-dde34832f3d6.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=udac6dc66&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=93027&status=done&style=stroke&taskId=u52580236-d974-4719-800a-fb95e876467&title=&width=846)

3. 右键选择要合并的分支，选择合并到当前分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662359158510-fa33b282-56af-4515-b88d-ff621ec13943.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u975b63d2&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102866&status=done&style=stroke&taskId=u7d56e589-0979-4f6e-a5fd-3992c21121a&title=&width=846)

4. 合并后的结果

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662359497165-dfc525bf-96ae-4c38-a802-9ad8b3a506d4.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=uc1c4e201&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94657&status=done&style=stroke&taskId=u6cbfa0ed-5ede-4085-961a-98b4eeb79e1&title=&width=846)
## 10、解决冲突

1. 切换到 yuehai 分支，修改一下代码，提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662359931654-88f8e308-ce6e-45e9-8491-45eb8d063e27.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=uf0d3ebd5&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=100074&status=done&style=stroke&taskId=ud6bc8826-1438-411f-ba28-9c900e85f83&title=&width=846)

2. 切换到 master 分支，修改一下代码，提交到本地库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662360072700-0bea4a18-071d-49e3-be0a-9230dddb281c.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=u6cfb2fb0&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102840&status=done&style=stroke&taskId=u3e1ceea2-06f7-463f-8089-2ce85279b60&title=&width=846)

3. 右键要合并的分支，选择合并到当前分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662360186624-50cba400-8234-4931-adef-4ff76ee53060.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ua8d1cc85&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=108467&status=done&style=stroke&taskId=u10fc1acd-da29-40da-aa2a-0bbf87de874&title=&width=846)

4. 提示代码有冲突

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662360279673-e4d43d08-5c4a-4c35-921c-5cc3ab43ed9c.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ucb4bc7fd&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104377&status=done&style=stroke&taskId=u51b699c3-49b5-4961-87fe-210b52d51ff&title=&width=846)

5. 点击合并，可以看到冲突的代码

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662360570544-e3556a4c-27ee-4fe4-8d2a-0cb370f0b04f.png#clientId=ub791c6f4-bf99-4&from=paste&height=860&id=u5f689925&name=image.png&originHeight=860&originWidth=1536&originalType=binary&ratio=1&rotation=0&showTitle=false&size=70464&status=done&style=stroke&taskId=u2c57f624-b692-4b13-84ae-67e96d54d2a&title=&width=1536)

6. 也可以不点击合并，直接选择使用哪个分支的代码

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662360805705-81d72dc5-963c-41ac-bb86-349108fa7171.png#clientId=ub791c6f4-bf99-4&from=paste&height=1032&id=ubbe7ed4d&name=image.png&originHeight=1032&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=110776&status=done&style=stroke&taskId=u1730cb77-7468-457c-b556-93defb526a0&title=&width=846)
# 八、IDEA 集成 GitHub
# 九、码云（gitee） - 国内代码托管中心
## 1、简介

1. 众所周知，GitHub 服务器在国外，使用 GitHub 作为项目托管网站，如果网速不好的话，严重影响使用体验，甚至会出现登录不上的情况。针对这个情况，大家也可以使用国内的项目托管网站-码云
2. 码云是开源中国推出的基于 Git 的代码托管服务中心，网址是 [https://gitee.com/](https://gitee.com/) ，使用方式跟 GitHub 一样，而且它还是一个中文网站，如果你英文不是很好它是最好的选择
## 2、码云帐号注册和登录

1. 进入码云官网地址：[https://gitee.com/](https://gitee.com/)，点击注册 Gitee

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662511524866-4e01290b-bff1-427d-a70d-d336b5f29fe8.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u6ac11df3&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=179075&status=done&style=stroke&taskId=u2049012b-3b75-4fa1-b31f-7051f178dd8&title=&width=923)

2. 输入个人信息，进行注册即可

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662511618743-5ec530c1-447b-438a-ba7f-f2db73b5121c.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u1bbf8dae&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=242898&status=done&style=stroke&taskId=u261e7242-63fc-43d5-b755-1da77612d91&title=&width=923)

3. 帐号注册成功以后，直接登录

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662511640525-48edd748-70ab-477a-89e4-4dde7f1ce614.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u5c222154&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=236092&status=done&style=stroke&taskId=ubdb4582d-c5ab-4414-a026-11184dddeb5&title=&width=923)

4. 登录以后，就可以看到码云官网首页了

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662511686594-b54cf024-8aa1-4bd1-bcdb-80bb5b415882.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u643c12ab&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=158509&status=done&style=stroke&taskId=u0ed6aa79-ed43-48ca-a076-efdd054938f&title=&width=923)
## 3、码云创建远程库

1. 点击首页右上角的加号，选择下面的新建仓库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662511758917-6a8efb63-9705-43f2-9186-d2a7addba146.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u17e12109&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=149939&status=done&style=stroke&taskId=ud075f238-71b5-4840-a9d9-48eb7d99a41&title=&width=923)

2. 填写仓库名称，路径，创建时只能选择私有库，如需创建公开仓库，请在创建仓库后通过「仓库设置」修改为公开；点击创建按钮

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662518913428-d845313b-2a4b-4cac-bd12-b2bece1d5d25.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u8df6638e&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=101594&status=done&style=stroke&taskId=ufa208eb8-60e1-4d9d-9e1f-ff76f7b0273&title=&width=923)

3. 远程库创建好以后，就可以看到 HTTPS 和 SSH 的链接

`git@gitee.com:yuehaiyan/git-test.git`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662519032881-f6d25545-b438-4632-ac58-3e6bed611803.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=ue27ef09a&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136628&status=done&style=stroke&taskId=uc87c8831-c6c8-432e-b29c-ee07cb7cbbe&title=&width=923)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662519056884-9c7b7848-d3e3-4845-bc52-52153cc0461b.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=ub2880d3e&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=152430&status=done&style=stroke&taskId=u3044500d-1128-4a83-bd5f-54d028e58d7&title=&width=923)
# 十、IDEA 集成码云
## 1、IDEA 安装码云插件

1. Idea 默认不带码云插件，我们第一步要安装 Gitee 插件。
2. 点击设置

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662525248936-7cd0cd31-e4da-49a2-9db0-483b95bce5f3.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u522921c1&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=103516&status=done&style=stroke&taskId=u2abd7d09-9871-400a-9ea6-bf335f64db5&title=&width=923)

3. 点击插件，在 Idea 插件商店搜索 Gitee，然后点击右侧的 Install 按钮

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662525503859-2a4ef19e-170b-4b2a-b5a7-d3f2bb27ff2e.png#clientId=uf3fadae7-4ab9-4&from=paste&height=778&id=u3f7a1885&name=image.png&originHeight=778&originWidth=1082&originalType=binary&ratio=1&rotation=0&showTitle=false&size=188086&status=done&style=stroke&taskId=u6160ec7b-871c-4fee-829e-ddc6f2a7604&title=&width=1082)
## 2、IDEA 安装码云插件 - 官网

1. idea 中有可能不能搜索，可能是网络问题，可以在官网下载
2. idea官网下载离线安装：[http://plugins.jetbrains.com/](http://plugins.jetbrains.com/)
3. gitee 插件：[https://plugins.jetbrains.com/plugin/11491-gitee](https://plugins.jetbrains.com/plugin/11491-gitee)
4. 点击安装

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662525718662-0bf9c53e-c596-4a44-a599-87b920201abc.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1024&id=ud6cc50b6&name=image.png&originHeight=1024&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=83919&status=done&style=stroke&taskId=uab9d9c0c-caaa-4ac5-a9a3-3d3f05193f4&title=&width=990)

5. idea 中会弹出弹窗，点击确定

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662525777047-bc141c7b-0457-4dd5-ae6b-f5e3ab9848fe.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u0f1ed643&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104329&status=done&style=stroke&taskId=u280a5fae-0f57-42cf-99bf-1dc2fe72adc&title=&width=923)

6. 当然也可能下载失败

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662525850652-455c4982-c071-482e-a669-ec83af45540f.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u3cafcdac&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109329&status=done&style=stroke&taskId=uf63e78fb-bccd-45ff-87a6-34f82aca2c6&title=&width=923)
## 3、IDEA 安装码云插件 - 离线下载

1. gitee 插件：[https://plugins.jetbrains.com/plugin/11491-gitee](https://plugins.jetbrains.com/plugin/11491-gitee)
2. 点击 Versions

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662526267512-52fc737c-6ca3-4d52-bb60-4d85d760db66.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1002&id=u965c6f09&name=image.png&originHeight=1002&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82695&status=done&style=stroke&taskId=u1c922fd5-db1c-46e3-ae14-0fc94ec4396&title=&width=990)

3. 根据 idea 的版本号下载安装包

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662526353109-45b2cf01-f5f5-4eca-b067-01d9825f8c1b.png#clientId=uf3fadae7-4ab9-4&from=paste&height=996&id=uab1d92a4&name=image.png&originHeight=996&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82245&status=done&style=stroke&taskId=u18588964-7ac3-4315-966f-f6bf91be0f6&title=&width=990)

4. 下载完成后，在 idea 中点击设置 --> 插件 --> 设置 --> 从磁盘安装插件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662526479360-9b8b1565-f9c7-4272-b2f7-2e9888e386a1.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=uf593b21e&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=133625&status=done&style=stroke&taskId=uef584029-857d-40aa-90f7-42cf2768b44&title=&width=923)

5. 选择下载的安装包即可

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662526529537-386a3731-0327-4503-93ff-3a0d8959a773.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=uf1cfcd7f&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=132982&status=done&style=stroke&taskId=ud8e80626-e6b6-4a3d-b9d7-085597f6274&title=&width=923)
## 4、码云登录

1. 先在 gitee 中绑定一个邮箱

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662527115233-470c98dc-93e0-4339-960b-c75e423b0638.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1040&id=u8ef57920&name=image.png&originHeight=1040&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=163416&status=done&style=stroke&taskId=u502195d4-1dcf-4095-9513-b00830ebc89&title=&width=1920)

2. 在 idea 中使用该邮箱登录

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662526780449-3b6cdf8a-44ec-4c4a-a148-7d87e4de251e.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u35fdee90&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89343&status=done&style=stroke&taskId=u66630af3-ccd7-4c6a-b39d-68f4b8b2501&title=&width=923)

3. 登录成功

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662527196844-4a1e561d-d5d2-421b-bebe-3180556f767a.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=ub8cd798c&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78310&status=done&style=stroke&taskId=u3cf1e4d0-b99b-457e-b3a0-d9c25a4d98a&title=&width=923)
## 5、分享工程到码云

1. 工具栏 VCS  --> 导入到版本控制  --> Share Project on Gitee

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662527889468-c0e95500-2b92-4b9d-a6ad-ab4171e7a86e.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u0adc9e24&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=111596&status=done&style=stroke&taskId=u24cfaa32-4496-49a6-96a8-4a4beae3f97&title=&width=923)

2. 在弹出来的弹窗中填入信息

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528110263-58a83e3a-3c43-4958-9bdb-6b38874aa74a.png#clientId=uf3fadae7-4ab9-4&from=paste&height=193&id=u65bffdc1&name=image.png&originHeight=193&originWidth=303&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16161&status=done&style=stroke&taskId=u9fd915dd-eaec-46b0-a780-f28ee7b823f&title=&width=303)

3. 成功的话会在右下角弹出来一个弹窗

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528317039-094d0973-41a6-4fbd-b1eb-a875889419c0.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u42f5bf8e&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102894&status=done&style=stroke&taskId=u0e3f21be-1d2c-4cca-9d57-ea9e1580291&title=&width=923)

4. 在 gitee 中也会出现这个库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528375485-b85ead01-3607-4dc0-b7e9-9247e74b3e23.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1023&id=u968b001c&name=image.png&originHeight=1023&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112851&status=done&style=stroke&taskId=u5c5face5-b0f7-42c5-b3c5-3c6f7518259&title=&width=990)
## 6、push 推送本地库到远程库
:::info
注意：push 是将本地库代码推送到远程库，如果本地库代码跟远程库代码版本不一致， push 的操作是会被拒绝的。也就是说，要想 push 成功，一定要保证本地库的版本要比远程 库的版本高！
因此一个成熟的程序员在动手改本地代码之前，一定会先检查下远程库跟本地代码的区别！如果本地的代码版本已经落后，切记要先 pull 拉取一下远程库的代码，将本地代码更新到最新以后，然后再修改，提交，推送！  
:::

1. 更换分支

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528751680-00fd9d22-ac99-410e-99da-7508dfec7472.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=ueeb81613&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104510&status=done&style=stroke&taskId=u9f815e59-59fc-4261-8c0c-e0e01554584&title=&width=923)

2. 右键点击项目，可以将当前分支的内容 push 到 GitHub 的远程仓库中

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528776805-316e9e88-ce6d-47d6-a461-d6519a67b070.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u2afc7ea9&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=137875&status=done&style=stroke&taskId=udeb8f235-603b-495f-b2c0-7fb70b8baff&title=&width=923)

3. 点击推送

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528813180-54d735e9-973d-4ce5-acfa-6e124736f1a2.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u0ab24634&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=87281&status=done&style=stroke&taskId=u57740adf-25d8-43ac-bb47-38f07c09803&title=&width=923)

4. 推送成功

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528841844-de1a7c45-fa88-474a-af6f-3c2624918010.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=uc5358e2e&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109948&status=done&style=stroke&taskId=ud1cdafc2-c236-456a-8c95-04eaf917291&title=&width=923)

5. git 上的项目就更新了

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662528891764-b47d3c12-ff1d-4d7c-a319-691c5b6c859a.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1015&id=u57cbe75a&name=image.png&originHeight=1015&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102169&status=done&style=stroke&taskId=u03405829-07da-497e-afa3-48937e202aa&title=&width=990)
## 7、pull 拉取远程库到本地库
:::info
注意：pull 是拉取远端仓库代码到本地，如果远程库代码和本地库代码不一致，会自动合并，如果自动合并失败，还会涉及到手动解决冲突的问题
:::

1. 右键点击项目，可以将远程仓库的内容 pull 到本地仓库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662529108430-2d0aa521-f3cd-4ab1-aa91-b6612a2cf78e.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u80a4b575&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=140609&status=done&style=stroke&taskId=u4e503ff2-99d5-46ef-bfdd-9005e6d9273&title=&width=923)

2. 选择分支，点击拉取

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662529231860-14dfaa92-274b-4d44-930b-5bba89773f35.png#clientId=uf3fadae7-4ab9-4&from=paste&height=423&id=uebb1197d&name=image.png&originHeight=423&originWidth=534&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23429&status=done&style=stroke&taskId=u333df2b5-c59f-4e56-9284-ae5fd4ad321&title=&width=534)
## 8、clone 克隆远程库到本地

1. 工具栏 VCS --> Git --> Clone 

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662529426817-a26237bb-def0-4905-999a-e848d5b1ef9b.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u60bf5347&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135400&status=done&style=stroke&taskId=ufcfcb82f-19bf-49e2-a5e1-0616ba6301c&title=&width=923)

2. 输入远程仓库的地址，点击克隆

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662529621107-a614e647-044a-4fa0-8f7a-5589c273c93c.png#clientId=uf3fadae7-4ab9-4&from=paste&height=460&id=uf122990b&name=image.png&originHeight=460&originWidth=777&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25455&status=done&style=stroke&taskId=u947dffa3-c54f-478a-a591-9c8a0b54972&title=&width=777)

3. 克隆完成

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662529695786-16ddc7a2-3d6d-419a-bfbe-4c54daad655a.png#clientId=uf3fadae7-4ab9-4&from=paste&height=1032&id=u5c8f4942&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69152&status=done&style=stroke&taskId=u3945bda5-5788-466a-9a54-a79f3f4b930&title=&width=923)
# 十一、自建代码托管平台-GitLab
## 1、GitLab 简介

1. GitLab 是由 GitLabInc.开发，使用 MIT 许可证的基于网络的 Git 仓库管理工具，且具有 wiki 和 issue 跟踪功能。使用 Git 作为代码管理工具，并在此基础上搭建起来的 web 服务。
2. GitLab 由乌克兰程序员 DmitriyZaporozhets 和 ValerySizov 开发，它使用 Ruby 语言写成。后来，一些部分用 Go 语言重写。截止 2018 年 5 月，该公司约有 290 名团队成员，以及 2000 多名开源贡献者。GitLab 被 IBM，Sony，JülichResearchCenter，NASA，Alibaba，Invincea，O’ReillyMedia，Leibniz-Rechenzentrum(LRZ)，CERN，SpaceX 等组织使用
## 2、GitLab 官网地址

1. 官网地址：[https://about.gitlab.com/](https://about.gitlab.com/)
2. 安装说明：[https://about.gitlab.com/installation/](https://about.gitlab.com/installation/)
## 3、GitLab 安装
### ①、服务器准备
### ②、安装包准备
### ③、编写安装脚本
### ④、初始化 GitLab 服务
### ⑤、启动 GitLab 服务
### ⑥、使用浏览器访问 GitLab
### ⑦、GitLab 创建远程库
# 十二、IDEA 集成 GitLab
## 1、安装 GitLab 插件
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662533949511-873d4785-5237-4316-8335-1d9878a6ec30.png#clientId=u5d19dc8b-e409-4&from=paste&height=703&id=u95dc5280&name=image.png&originHeight=703&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94401&status=done&style=stroke&taskId=ua7552bcd-4fc8-4f05-be60-d403f08ae6d&title=&width=982)
## 2、设置 GitLab 插件
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1662534105599-e28b3b53-99e4-47fd-9fcc-21ff40f5c359.png#clientId=u5d19dc8b-e409-4&from=paste&height=1032&id=ucfbde992&name=image.png&originHeight=1032&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=93988&status=done&style=stroke&taskId=u9a224724-3dc5-48e7-a608-3e5f1a641c0&title=&width=923)
## 3、GitLab 拉取项目

1. VCS -> 从版本控制中获取

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663656782294-1f6cf63c-69f4-4dc1-b0e0-a52438b887b9.png#clientId=u7173aa62-aa79-4&from=paste&height=1040&id=u0721b769&name=image.png&originHeight=1040&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=99628&status=done&style=stroke&taskId=u696a6657-3ed8-42ba-9ab8-0aa540984b9&title=&width=1920)

2. 弹出一个弹窗

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663656842266-17d3d264-c298-473e-a3f5-db3f557caae0.png#clientId=u7173aa62-aa79-4&from=paste&height=1040&id=uf8f1d049&name=image.png&originHeight=1040&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84938&status=done&style=stroke&taskId=u8217f351-37a1-40ce-a555-fb9415885cb&title=&width=1920)

3. 在 gitlab 中复制项目连接

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663656881745-9bfb9011-3f62-4864-aff2-777b8dd09080.png#clientId=u7173aa62-aa79-4&from=paste&height=1080&id=uec76799b&name=image.png&originHeight=1080&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=219701&status=done&style=stroke&taskId=u9ed67823-1202-4e75-9f2e-0d9a2d1b2a0&title=&width=1920)

4. 在 idea 中弹出来的弹窗中输入复制的网址

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663656968941-ae5c27db-0b7b-4fae-a144-6c9e8912774b.png#clientId=u7173aa62-aa79-4&from=paste&height=1040&id=ub4eeb8d4&name=image.png&originHeight=1040&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88033&status=done&style=stroke&taskId=u3ed7c307-7fc9-4f6c-ab31-b276f07db22&title=&width=1920)

5. 点击克隆
6. 输入 gitlab 的账号密码
## 4、push 本地代码到 GitLab 远程库
:::info
注意：gitlab 网页上复制过来的连接是：[http://gitlab.example.com/root/git-test.git](http://gitlab.example.com/root/git-test.git)，需要手动修改为：[http://gitlab-server/root/git-test.git](http://gitlab-server/root/git-test.git)
选择 gitlab 远程连接，进行 push
:::
推送、拉取、克隆等与 gitee 相同
## 5、问题总结
### ①、无法推送
idea 提示：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663657158445-2f351f4b-f70a-42ef-836a-932fc954a42a.png#clientId=u7173aa62-aa79-4&from=paste&id=ub17621a7&name=image.png&originHeight=94&originWidth=344&originalType=url&ratio=1&rotation=0&showTitle=false&size=5006&status=done&style=stroke&taskId=ud2f9a43b-e481-451d-9410-8a6fe566c2a&title=)
:::info
原因：git 设置的用户名和邮箱与 gitlab 上的不同
:::
解决：

1. 查看设置的用户名和邮箱：`git config --global --list | grep user`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663657447117-8d248a82-3e1b-429b-858a-01d84952e0f4.png#clientId=u7173aa62-aa79-4&from=paste&height=510&id=u85da5c89&name=image.png&originHeight=510&originWidth=756&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13298&status=done&style=stroke&taskId=u036c16e6-af16-4b65-8d18-b6e4ab82391&title=&width=756)

2. 清空所有用户名和密码（cmd 以管理员身份运行）：git config --system --unset credential.helper
3. 修改用户名：`git config --global user.name "用户名"`
4. 修改邮箱：`git config --global user.email "邮箱"`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1663657518489-50497a21-63d7-44dd-8870-ee2828ff362b.png#clientId=u7173aa62-aa79-4&from=paste&height=552&id=u5579bfce&name=image.png&originHeight=552&originWidth=875&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20054&status=done&style=stroke&taskId=u9d999db3-d7be-41a6-9314-8e2a7a708b4&title=&width=875)
### ②、
### ③、
### ④、
