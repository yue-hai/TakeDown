> 官网：[http://git-scm.com/](http://git-scm.com/)
> 
> 高速下载地址：[https://registry.npmmirror.com/binary.html?path=git-for-windows/](https://registry.npmmirror.com/binary.html?path=git-for-windows/)
> 
> 尚硅谷技术课程系列之Git V2.0.pdf：[尚硅谷技术课程系列之Git%20V2.0.pdf](attachments/尚硅谷技术课程系列之Git%20V2.0.pdf)

# 一、Git 概述

1. Git 是一个免费的、开源的分布式版本控制系统，可以快速高效地处理从小型到大型的各种项目
2. Git 易于学习，占地面积小，性能极快。 
3. 它具有廉价的本地库，方便的暂存区域和多个工作流分支等特性。其性能优于 Subversion、CVS、Perforce 和 ClearCase 等版本控制工具。

## 1、何为版本控制

1. 版本控制是一种记录文件内容变化，以便将来查阅特定版本修订情况的系统。
2. 版本控制其实最重要的是可以记录文件修改历史记录，从而让用户能够查看历史版本，方便版本切换。

![](attachments/Pasted%20image%2020230724105234.png)

## 2、为什么需要版本控制

- 个人开发过渡到团队协作

![](attachments/Pasted%20image%2020230724105251.png)

## 3、版本控制工具

### ①、集中式版本控制工具

1. CVS、SVN(Subversion)、VSS……
2. 集中化的版本控制系统诸如 CVS、SVN 等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。多年以来，这已成为版本控制系统的标准做法。
3. 这种做法带来了许多好处，每个人都可以在一定程度上看到项目中的其他人正在做些什么。而管理员也可以轻松掌控每个开发者的权限，并且管理一个集中化的版本控制系统，要远比在各个客户端上维护本地数据库来得轻松容易。
4. 事分两面，有好有坏。这么做显而易见的缺点是中央服务器的单点故障。如果服务器宕机一小时，那么在这一小时内，谁都无法提交更新，也就无法协同工作

![](attachments/Pasted%20image%2020230724105353.png)

### ②、分布式版本控制工具

1. Git、Mercurial、Bazaar、Darcs……
2. 像 Git 这种分布式版本控制工具，客户端提取的不是最新版本的文件快照，而是把代码仓库完整地镜像下来（本地库）。这样任何一处协同工作用的文件发生故障，事后都可以用其他客户端的本地仓库进行恢复。因为每个客户端的每一次文件提取操作，实际上都是一次对整个文件仓库的完整备份。
3. 分布式的版本控制系统出现之后，解决了集中式版本控制系统的缺陷：
   1. 服务器断网的情况下也可以进行开发（因为版本控制是在本地进行的）
   2. 每个客户端保存的也都是整个完整的项目（包含历史记录，更加安全）

![](attachments/Pasted%20image%2020230724105418.png)

## 4、Git 简史

![](attachments/Pasted%20image%2020230724105447.png)

## 5、Git 工作机制

![](attachments/Pasted%20image%2020230724105510.png)

## 6、 Git 和代码托管中心

代码托管中心是基于网络服务器的远程代码仓库，一般我们简单称为远程库

### ①、局域网

- GitLab

### ②、互联网

1. GitHub（外网）
2. Gitee 码云（国内网站）

# 二、Git 安装
## 1、下载
> 官网：[http://git-scm.com/](http://git-scm.com/)
> 高速下载地址：[https://registry.npmmirror.com/binary.html?path=git-for-windows/](https://registry.npmmirror.com/binary.html?path=git-for-windows/)

## 2、安装

1. 查看 GNU 协议，可以直接点击下一步

![](attachments/Pasted%20image%2020230724105545.png)

2. 选择 Git 安装位置，要求是非中文并且没有空格的目录，然后下一步

![](attachments/Pasted%20image%2020230724105558.png)

3. Git 选项配置，推荐默认设置，然后下一步

![](attachments/Pasted%20image%2020230724105611.png)

4. Git 安装目录名，不用修改，直接点击下一步

![](attachments/Pasted%20image%2020230724105624.png)

5. Git 的默认编辑器，建议使用默认的 Vim 编辑器，然后点击下一步

![](attachments/Pasted%20image%2020230724105637.png)

6. 默认分支名设置，选择让 Git 决定，分支名默认为 master，下一步

![](attachments/Pasted%20image%2020230724105652.png)

7.  修改 Git 的环境变量，选第一个，不修改环境变量，只在 Git Bash 里使用 Git  

![](attachments/Pasted%20image%2020230724105718.png)

8. 选择后台客户端连接协议，选默认值 OpenSSL，然后下一步

![](attachments/Pasted%20image%2020230724105741.png)

9. 配置 Git 文件的行末换行符，Windows 使用 CRLF，Linux 使用 LF，选择第一个自动转换，然后继续下一步

![](attachments/Pasted%20image%2020230724105813.png)

10. 选择 Git 终端类型，选择默认的 Git Bash 终端，然后继续下一步

![](attachments/Pasted%20image%2020230724105826.png)

11.  选择 Git pull 合并的模式，选择默认，然后下一步

![](attachments/Pasted%20image%2020230724105841.png)

12. 选择 Git 的凭据管理器，选择默认的跨平台的凭据管理器，然后下一步

![](attachments/Pasted%20image%2020230724105856.png)

13. 其他配置，选择默认设置，然后下一步

![](attachments/Pasted%20image%2020230724105909.png)

14. 实验室功能，技术还不成熟，有已知的 bug，不要勾选，然后点击右下角的 Install 按钮，开始安装 Git

![](attachments/Pasted%20image%2020230724105926.png)

15. 点击 Finsh 按钮，Git 安装成功

![](attachments/Pasted%20image%2020230724105938.png)

16. 右键任意位置，在右键菜单里选择 Git Bash Here 即可打开 Git Bash 命令行终端

![](attachments/Pasted%20image%2020230724105951.png)

17. 在 Git Bash 终端里输入 git --version 查看 git 版本，如图所示，说明 Git 安装成功

```shell
git --version
```

![](attachments/Pasted%20image%2020230724110003.png)

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
4. `git config --global user.name 用户名`
5. `git config --global user.email 邮箱`

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

- `git init`：让 git 获取这个项目的管理权

1. 进行需要使用 git 管理的项目

![](attachments/Pasted%20image%2020230724110225.png)

2. 右键鼠标，选择 Git Bash Here

![](attachments/Pasted%20image%2020230724110237.png)

3. 输入命令：`git init`

![](attachments/Pasted%20image%2020230724110255.png)

4. 完成后会在该目录生成 `.git` 目录，此时初始化完成

![](attachments/Pasted%20image%2020230724110309.png)

## 3、查看本地库状态：`git status`

- `git status`

### ①、首次查看（工作区没有任何文件）

![](attachments/Pasted%20image%2020230724110354.png)

![](attachments/Pasted%20image%2020230724110406.png)

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

![](attachments/Pasted%20image%2020230724110426.png)

2. 提示 hello.txt 只存在于工作区，并没有被追踪

![](attachments/Pasted%20image%2020230724110440.png)

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

- `git add 文件名`

### ①、将工作区的文件添加到暂存区

![](attachments/Pasted%20image%2020230724110531.png)

```shell
git add hello.txt
```

### ②、再次查看本地库状态（检测到暂存区有新文件）

![](attachments/Pasted%20image%2020230724110545.png)

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

- `git rm --cached 文件名`

1. 这只是删除了暂存区的文件，并没有删除本地文件

![](attachments/Pasted%20image%2020230724110602.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git rm --cached hello.txt
rm 'hello.txt'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$
```

2. 删除后再查看本地库状态

![](attachments/Pasted%20image%2020230724110616.png)

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

- `git commit -m "日志信息" 文件名`
- 不添加 `-m` 参数的话，也会弹出来弹窗让输入信息

### ①、将暂存区的文件提交到本地库

![](attachments/Pasted%20image%2020230724110804.png)

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

![](attachments/Pasted%20image%2020230724110818.png)

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

![](attachments/Pasted%20image%2020230724110831.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git reflog
da7a36f (HEAD -> master) HEAD@{0}: commit (initial): yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

### ②、查看本地库日志

`git log`

![](attachments/Pasted%20image%2020230724110846.png)

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

![](attachments/Pasted%20image%2020230724110902.png)

### ②、查看状态（检测到工作区有文件被修改）

`git status`

![](attachments/Pasted%20image%2020230724110920.png)

### ③、将修改的文件再次添加暂存区

`git add hello.txt`

![](attachments/Pasted%20image%2020230724110933.png)

### ④、查看状态（工作区的修改添加到了暂存区）

`git status`

![](attachments/Pasted%20image%2020230724110945.png)

## 8、历史版本切换

- 每提交一次本地库会生成一个新版本

### ①、查看历史版本

![](attachments/Pasted%20image%2020230724110959.png)

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

- `git reset --hard 版本号`

![](attachments/Pasted%20image%2020230724111048.png)

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

![](attachments/Pasted%20image%2020230724111108.png)

### ③、查看是否成功回溯版本

- 在工作目录下的 `.git\refs\heads\master` 文件中会显示当前版本的完整版本号

### ④、Git 切换版本，底层其实是移动的 HEAD 指针

![](attachments/Pasted%20image%2020230724111133.png)

# 四、Git 分支操作

![](attachments/Pasted%20image%2020230724111147.png)

## 1、什么是分支

1. 在版本控制过程中，同时推进多个任务，为每个任务，我们就可以创建每个任务的单独分支。
2. 使用分支意味着程序员可以把自己的工作从开发主线上分离开来，开发自己分支的时候，不会影响主线分支的运行。
3. 对于初学者而言，分支可以简单理解为副本，一个分支就是一个单独的副本。（分支底层其实也是指针的引用）

![](attachments/Pasted%20image%2020230724111224.png)

## 2、分支的好处

1. 同时并行推进多个功能开发，提高开发效率。
2. 各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的分支删除重新开始即可。

## 3、分支的操作

| 命令名称            | 作用                         |
| ------------------- | ---------------------------- |
| git branch 分支名   | 创建分支                     |
| git branch -v       | 查看分支                     |
| git checkout 分支名 | 切换分支                     |
| git merge 分支名    | 把指定的分支合并到当前分支上 |

### ①、查看分支

- `git branch 分支名`
- `*` 代表当前所在的分区

![](attachments/Pasted%20image%2020230724111418.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

### ②、创建分支

- `git branch 分支名`

![](attachments/Pasted%20image%2020230724111442.png)

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

![](attachments/Pasted%20image%2020230724111506.png)

2. 提交到暂存区，然后提交到本地库

![](attachments/Pasted%20image%2020230724111522.png)

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

![](attachments/Pasted%20image%2020230724111537.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   5500b6e yuehai02
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

### ④、切换分支

- `git checkout 分支名`

1. 查看分支

![](attachments/Pasted%20image%2020230724111559.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git branch -v
* master   5500b6e yuehai02
  yuehai01 da7a36f yuehai01

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$

```

2. 切换分支

![](attachments/Pasted%20image%2020230724111642.png)

```shell
10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (master)
$ git checkout yuehai01
Switched to branch 'yuehai01'

10222148@EQDP-10222148 MINGW64 /d/Idea/save/java/gitTest (yuehai01)
$

```

3. 切换后发现文件被改变

![](attachments/Pasted%20image%2020230724111658.png)

### ⑤、合并分支

- 将指定的分支合并到当前分支上

- `git merge 分支名`

![](attachments/Pasted%20image%2020230724111735.png)

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

![](attachments/Pasted%20image%2020230724111754.png)

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

![](attachments/Pasted%20image%2020230724111811.png)

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

![](attachments/Pasted%20image%2020230724111909.png)

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

![](attachments/Pasted%20image%2020230724111922.png)

5. 查看本地库状态

![](attachments/Pasted%20image%2020230724111938.png)

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

1. 打开有冲突的文件：特殊符号：<<<<<<< HEAD 当前分支的代码 ======= 合并过来的代码 >>>>>>> yuehai01

![](attachments/Pasted%20image%2020230724112021.png)

2. 手动选择要保留的内容；选择保留 master 分支的内容

![](attachments/Pasted%20image%2020230724112037.png)

3. 修改完文件后，将其提交到本地库，注意此时不要指定文件名

![](attachments/Pasted%20image%2020230724112051.png)

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

![](attachments/Pasted%20image%2020230724112209.png)

# 五、Git 团队协作机制

## 1、团队内协作

![](attachments/Pasted%20image%2020230724112228.png)

## 2、跨团队协作

![](attachments/Pasted%20image%2020230724112244.png)

# 六、GitHub 操作

> [https://www.bilibili.com/video/BV1vy4y1s7k6?p=20&vd_source=b55e15966ca689b32671d4aa387cab01](https://www.bilibili.com/video/BV1vy4y1s7k6?p=20&vd_source=b55e15966ca689b32671d4aa387cab01)

# 七、IDEA 集成 Git

## 1、配置 Git 忽略文件

### ①、Eclipse 特定文件

![](attachments/Pasted%20image%2020230724112320.png)

### ②、IDEA 特定文件

![](attachments/Pasted%20image%2020230724112335.png)

### ③、Maven 工程的 target 目录

![](attachments/Pasted%20image%2020230724112350.png)

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

![](attachments/Pasted%20image%2020230724112426.png)

## 3、初始化本地库

![](attachments/Pasted%20image%2020230724112440.png)

![](attachments/Pasted%20image%2020230724112454.png)

![](attachments/Pasted%20image%2020230724112516.png)

## 4、添加到暂存区

### ①、手动添加到暂存区

1. 刚初始化本地库后 pom 文件是红色的

![](attachments/Pasted%20image%2020230724112535.png)

2. 右键项目，git --> add，将整个项目添加到暂存区，pom 文件就会变为绿色

![](attachments/Pasted%20image%2020230724112550.png)

3. 添加完成

![](attachments/Pasted%20image%2020230724112605.png)

### ②、自动添加到暂存区

1. 创建文件后，idea 会询问是否自动添加到暂存区，可以选择确定

![](attachments/Pasted%20image%2020230724112622.png)

## 5、提交到本地库

![](attachments/Pasted%20image%2020230724112635.png)

## 6、切换版本

1. 修改一下代码

![](attachments/Pasted%20image%2020230724112700.png)

2. 再次提交

![](attachments/Pasted%20image%2020230724112718.png)

3. 查看版本

![](attachments/Pasted%20image%2020230724112752.png)

4. 切换版本；右键要切换的版本，选择 Checkout Revision

![](attachments/Pasted%20image%2020230724112818.png)

5. 切换到了之前的版本

![](attachments/Pasted%20image%2020230724112845.png)

6. 切换会 master 版本

![](attachments/Pasted%20image%2020230724112913.png)

## 7、创建分支

1. 点击 `git --> log --> 选择版本 --> 右键 --> 新分支`

![](attachments/Pasted%20image%2020230724112938.png)

2. 输入分支名称

![](attachments/Pasted%20image%2020230724113005.png)

3. 创建完后会自动切换到该分支

![](attachments/Pasted%20image%2020230724113021.png)

## 8、切换分支

1. 在 `git --> log` 中选择要切换的分支，右键选择检出即可切换

![](attachments/Pasted%20image%2020230724123323.png)

2. 也可以左键点击右下角的分支名，在弹出来的弹窗中选择分支进行切换

![](attachments/Pasted%20image%2020230724123340.png)

![](attachments/Pasted%20image%2020230724123359.png)

3. 切换完毕后的样子

![](attachments/Pasted%20image%2020230724123413.png)

## 9、合并分支

1. 修改 yuehai 分支的代码，提交到本地库

![](attachments/Pasted%20image%2020230724123430.png)

2. 切换到 master 分支

![](attachments/Pasted%20image%2020230724123446.png)

3. 右键选择要合并的分支，选择合并到当前分支

![](attachments/Pasted%20image%2020230724123501.png)

4. 合并后的结果

![](attachments/Pasted%20image%2020230724123515.png)

## 10、解决冲突

1. 切换到 yuehai 分支，修改一下代码，提交到本地库

![](attachments/Pasted%20image%2020230724123533.png)

2. 切换到 master 分支，修改一下代码，提交到本地库

![](attachments/Pasted%20image%2020230724123545.png)

3. 右键要合并的分支，选择合并到当前分支

![](attachments/Pasted%20image%2020230724123559.png)

4. 提示代码有冲突

![](attachments/Pasted%20image%2020230724123612.png)

5. 点击合并，可以看到冲突的代码

![](attachments/Pasted%20image%2020230724123627.png)

6. 也可以不点击合并，直接选择使用哪个分支的代码

![](attachments/Pasted%20image%2020230724123645.png)

# 八、IDEA 集成 GitHub

# 九、码云（gitee） - 国内代码托管中心

## 1、简介

1. 众所周知，GitHub 服务器在国外，使用 GitHub 作为项目托管网站，如果网速不好的话，严重影响使用体验，甚至会出现登录不上的情况。针对这个情况，大家也可以使用国内的项目托管网站-码云
2. 码云是开源中国推出的基于 Git 的代码托管服务中心，网址是 [https://gitee.com/](https://gitee.com/) ，使用方式跟 GitHub 一样，而且它还是一个中文网站，如果你英文不是很好它是最好的选择

## 2、码云帐号注册和登录

1. 进入码云官网地址：[https://gitee.com/](https://gitee.com/)，点击注册 Gitee

![](attachments/Pasted%20image%2020230724123710.png)

2. 输入个人信息，进行注册即可

![](attachments/Pasted%20image%2020230724123724.png)

3. 帐号注册成功以后，直接登录

![](attachments/Pasted%20image%2020230724123737.png)

4. 登录以后，就可以看到码云官网首页了

![](attachments/Pasted%20image%2020230724123749.png)

## 3、码云创建远程库

1. 点击首页右上角的加号，选择下面的新建仓库

![](attachments/Pasted%20image%2020230724123806.png)

2. 填写仓库名称，路径，创建时只能选择私有库，如需创建公开仓库，请在创建仓库后通过「仓库设置」修改为公开；点击创建按钮

![](attachments/Pasted%20image%2020230724123821.png)

3. 远程库创建好以后，就可以看到 HTTPS 和 SSH 的链接

- `git@gitee.com:yuehaiyan/git-test.git`

![](attachments/Pasted%20image%2020230724123840.png)

![](attachments/Pasted%20image%2020230724123857.png)

# 十、IDEA 集成码云

## 1、IDEA 安装码云插件

1. Idea 默认不带码云插件，我们第一步要安装 Gitee 插件。
2. 点击设置

![](attachments/Pasted%20image%2020230724123914.png)

3. 点击插件，在 Idea 插件商店搜索 Gitee，然后点击右侧的 Install 按钮

![](attachments/Pasted%20image%2020230724123928.png)

## 2、IDEA 安装码云插件 - 官网

1. idea 中有可能不能搜索，可能是网络问题，可以在官网下载
2. idea官网下载离线安装：[http://plugins.jetbrains.com/](http://plugins.jetbrains.com/)
3. gitee 插件：[https://plugins.jetbrains.com/plugin/11491-gitee](https://plugins.jetbrains.com/plugin/11491-gitee)
4. 点击安装

![](attachments/Pasted%20image%2020230724123944.png)

5. idea 中会弹出弹窗，点击确定

![](attachments/Pasted%20image%2020230724123958.png)

6. 当然也可能下载失败

![](attachments/Pasted%20image%2020230724124011.png)

## 3、IDEA 安装码云插件 - 离线下载

1. gitee 插件：[https://plugins.jetbrains.com/plugin/11491-gitee](https://plugins.jetbrains.com/plugin/11491-gitee)
2. 点击 Versions

![](attachments/Pasted%20image%2020230724124032.png)

3. 根据 idea 的版本号下载安装包

![](attachments/Pasted%20image%2020230724124054.png)

4. 下载完成后，在 idea 中点击设置 --> 插件 --> 设置 --> 从磁盘安装插件

![](attachments/Pasted%20image%2020230724124106.png)

5. 选择下载的安装包即可

![](attachments/Pasted%20image%2020230724124119.png)

## 4、码云登录

1. 先在 gitee 中绑定一个邮箱

![](attachments/Pasted%20image%2020230724124420.png)

2. 在 idea 中使用该邮箱登录

![](attachments/Pasted%20image%2020230724124431.png)

3. 登录成功

![](attachments/Pasted%20image%2020230724124445.png)

## 5、分享工程到码云

1. 工具栏 VCS  --> 导入到版本控制  --> Share Project on Gitee

![](attachments/Pasted%20image%2020230724124500.png)

2. 在弹出来的弹窗中填入信息

![](attachments/Pasted%20image%2020230724124551.png)

3. 成功的话会在右下角弹出来一个弹窗

![](attachments/Pasted%20image%2020230724124604.png)

4. 在 gitee 中也会出现这个库

![](attachments/Pasted%20image%2020230724124640.png)

## 6、push 推送本地库到远程库

> 注意：push 是将本地库代码推送到远程库，如果本地库代码跟远程库代码版本不一致， push 的操作是会被拒绝的。也就是说，要想 push 成功，一定要保证本地库的版本要比远程 库的版本高！
> 
> 因此一个成熟的程序员在动手改本地代码之前，一定会先检查下远程库跟本地代码的区别！如果本地的代码版本已经落后，切记要先 pull 拉取一下远程库的代码，将本地代码更新到最新以后，然后再修改，提交，推送！  

1. 更换分支

![](attachments/Pasted%20image%2020230724124811.png)

2. 右键点击项目，可以将当前分支的内容 push 到 GitHub 的远程仓库中

![](attachments/Pasted%20image%2020230724124827.png)

3. 点击推送

![](attachments/Pasted%20image%2020230724124839.png)

4. 推送成功

![](attachments/Pasted%20image%2020230724124852.png)

5. git 上的项目就更新了

![](attachments/Pasted%20image%2020230724124905.png)

## 7、pull 拉取远程库到本地库

- 注意：pull 是拉取远端仓库代码到本地，如果远程库代码和本地库代码不一致，会自动合并，如果自动合并失败，还会涉及到手动解决冲突的问题

1. 右键点击项目，可以将远程仓库的内容 pull 到本地仓库

![](attachments/Pasted%20image%2020230724124957.png)

2. 选择分支，点击拉取

![](attachments/Pasted%20image%2020230724125010.png)

## 8、clone 克隆远程库到本地

1. 工具栏 VCS --> Git --> Clone 

![](attachments/Pasted%20image%2020230724125521.png)

2. 输入远程仓库的地址，点击克隆

![](attachments/Pasted%20image%2020230724125543.png)

3. 克隆完成

![](attachments/Pasted%20image%2020230724125621.png)

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

![](attachments/Pasted%20image%2020230724125724.png)

## 2、设置 GitLab 插件

![](attachments/Pasted%20image%2020230724125746.png)

## 3、GitLab 拉取项目

1. VCS -> 从版本控制中获取

![](attachments/Pasted%20image%2020230724125821.png)

2. 弹出一个弹窗

![](attachments/Pasted%20image%2020230724125834.png)

3. 在 gitlab 中复制项目连接

![](attachments/Pasted%20image%2020230724125851.png)

4. 在 idea 中弹出来的弹窗中输入复制的网址

![](attachments/Pasted%20image%2020230724125903.png)

5. 点击克隆
6. 输入 gitlab 的账号密码

## 4、push 本地代码到 GitLab 远程库

1. 注意：gitlab 网页上复制过来的连接是：[http://gitlab.example.com/root/git-test.git](http://gitlab.example.com/root/git-test.git)，需要手动修改为：[http://gitlab-server/root/git-test.git](http://gitlab-server/root/git-test.git)
2. 选择 gitlab 远程连接，进行 push
3. 推送、拉取、克隆等与 gitee 相同

# 十三、问题总结

## 1、无法推送

### ①、idea 提示：

![](attachments/Pasted%20image%2020230724130829.png)

### ②、原因

git 设置的用户名和邮箱与 gitlab 上的不同

### ③、解决

1. 查看设置的用户名和邮箱：`git config --global --list | grep user`

![](attachments/Pasted%20image%2020230724130953.png)

2. 清空所有用户名和密码（cmd 以管理员身份运行）：git config --system --unset credential.helper
3. 修改用户名：`git config --global user.name "用户名"`
4. 修改邮箱：`git config --global user.email "邮箱"`

![](attachments/Pasted%20image%2020230724131005.png)

### ④、使用 TortoiseGit 解决

1. 首先下载 TortoiseGit：https://tortoisegit.org/
2. 安装
3. 打开设置

![|700](attachments/Pasted%20image%2020240117085304.png)

4. 点击 git，修改 Email 即可

![|700](attachments/Pasted%20image%2020240117085415.png)

## 2、本地自建仓库推送到新建 git

1. 提交

![](attachments/Pasted%20image%2020230329101938.png)

2. 推送，此时推送应该是被拒

![](attachments/Pasted%20image%2020230329103017.png)

3. 日志中多了远程选项，选中远程，点击提取所有远程

![](attachments/Pasted%20image%2020230329102203.png)

4. 右键远程分支，新建分支

![](attachments/Pasted%20image%2020230329102252.png)

![](attachments/Pasted%20image%2020230329102327.png)

5. 签出到 master 分支，右键新建的分支，选择将 master 变基到新分支

![](attachments/Pasted%20image%2020230329103321.png)

6. 完成，可以推送 master 分支，此时可删除新建的分支
7. <font color="#ff0000">直接将远程 master 合并到本地 master 应该也可以</font>

## 3、本地回滚（撤销）提交

### ①、撤销提交但是保留工作区和暂存区的状态

1. `git reset --soft HEAD~1`：可以撤销最后一次的提交，而且会保留工作区和暂存区的状态。这意味着代码的更改还在，只是撤销了提交的动作。
2. 这个命令非常适合在提交信息写错或者忘记添加某些文件时使用。
3. `--soft` 参数告诉 Git 保留工作目录的更改，并将这些更改放回暂存区。
4. `HEAD~1` 表示当前分支的上一个提交，也可以设置为修订号

### ②、撤销提交和暂存区、但是保留工作区的状态

1. `git reset HEAD~1` 或者 `git reset --mixed HEAD~1` 会撤销最后一次的提交，并且撤销暂存区的状态，但是保留工作区的状态。这意味着代码更改还在工作目录中，但是不再处于暂存状态，需要重新添加它们到暂存区以准备下一次的提交。
2. 这个命令适用于想要修改最近的提交（例如，添加遗漏的文件或更改提交信息）。
3. `--mixed` 是 Git reset 的默认模式，所以即使不指定 `--mixed`，效果也是一样的。
4. `HEAD~1` 表示当前分支的上一个提交，也可以设置为修订号

### ③、撤销提交、暂存区和工作区

1. `git reset --hard HEAD~1` 命令会撤销最后一次的提交，并且撤销暂存区和工作区的状态。这意味着代码更改将会被完全丢弃，回到上一次提交的状态。
2. 这是一个<font color="#ff0000">非常危险</font>的操作，因为可能会丢失工作进度。在执行这个命令前，请确保确实想要这样做。
3. `--hard` 参数告诉 Git 完全回到上一个提交的状态，放弃所有在此之后的更改。
4. `HEAD~1` 表示当前分支的上一个提交，也可以设置为修订号
5. 截图示例：
6. 右键点击想要回滚到的提交，复制其修订号

![](attachments/Pasted%20image%2020240117090128.png)

7. 打开 git bash，输入：`git reset --hard 修订号`，回车

```shell
10222148@EQDN-10222148-1 MINGW64 /d/新建文件夹/笔记/【笔记】 (master)
$ git reset --hard 1f205e82454e25184f7b23bdc574bb7714c41447
HEAD is now at 1f205e8 Merge remote-tracking branch 'origin/master'
```

8. 本地回滚完成，再看 idea

![|700](attachments/Pasted%20image%2020240117090803.png)

## 4、远程回滚（撤销）提交

> 如果不仅本地提交了，还推送到远程了该怎么办？

1. 执行上面的 `3、本地回滚提交`
2. 在 git bash 中执行：
	1.  `<提交哈希>` 是想要回滚到的提交记录，具体请看下图
	2. `<分支名>` 即想要回滚的分支，如 `master`

```shell
git push --force origin <提交哈希>:<分支名>
```

3. 查看 github 提交历史，远程回滚完成

![|700](attachments/Pasted%20image%2020240117091249.png)

4. 请注意，强制推送会重写远程仓库的历史，并且对于其他协作者来说可能会造成问题。在进行强制推送之前，请确保：
	1. 已经和团队中的其他成员沟通了这个操作的影响。
	2. 没有其他人正在基于这些将要被重写的提交工作。
	3. 确信这是撤销推送的唯一或最好的方法。
5. 在某些情况下，更好的做法可能是创建一个新的提交来撤销之前提交的更改，然后正常推送这个新的提交。这样做不会重写历史，但会保留原始提交并添加一个新的“撤销”提交。

## 5、开了 vpn，idea 推送到 github 还是失败

### ①、问题

1. 浏览器可以访问 `github.com`，但是 idea 或者 gitbash 推送失败

### ②、原因

1. 并不是所有软件或工具的网络请求都会走系统代理，有些应用的网络请求可能绕过代理，直接与网络通信。

### ③、解决

1. 我们要设置 gitbash 的代理：

```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

2. 这样设置完就可以使用 gitbash 提交了
3. 上面的端口为 vpn 所使用的端口，如我使用的软件 Clash 的端口为 7890

![|700](attachments/Pasted%20image%2020231009092901.png)

## 6、idea 提交时不想看到指定的目录或文件

1. 在提交中右键目录或文件
2. 选择：`添加到 .gitignore`
3. 然后选择：`.git/info/exclude` 即可，点击后会打开 `.git/info/exclude` 文件，同时会添加刚才选择的目录或文件到文件中
4. 若是想指定某目录下的文件全部都不显示，可以在 `.git/info/exclude` 文件中加入通配符：`/目录名/*`

![](attachments/Pasted%20image%2020240614133946.png)

## 7、同时推送到 GitHub 和 gitee 上

1. 首先在 GitHub 和 gitee 上分别创建两个仓库

![|700](attachments/Pasted%20image%2020240819084416.png)

![|700](attachments/Pasted%20image%2020240819084359.png)

2. 从 GitHub 或者 gitee 上将 test 仓库拉取到本地(这里选择克隆 GitHub 的 test 仓库)
3. 查看仓库：

```shell
git remote -v
```

```shell
PS D:\Idea\save\TakeDown\.idea> git remote -v
origin https://github.com/yue-hai/TakeDown.git (fetch)
origin https://github.com/yue-hai/TakeDown.git (push)

PS D:\Idea\save\TakeDown\.idea>
```

4. 通过上面的输出结果，发现 github 仓库的名称是 origin，我们先删除这个名称：

```shell
git remote rm origin
```

```shell
PS D:\Idea\save\TakeDown\.idea> git remote rm origin
PS D:\Idea\save\TakeDown\.idea> git remote -v

PS D:\Idea\save\TakeDown\.idea>
```

5. 添加远程仓库 github：

```shell
git remote add github https://github.com/yue-hai/TakeDown.git
```

6. 添加远程仓库 gitee：

```shell
git remote add gitee https://gitee.com/yuehaiyan/take-down.git
```

7. 再次查看仓库：

```shell
git remote -v
```

```shell
PS D:\Idea\save\TakeDown\.idea> git remote -v
gitee   https://gitee.com/yuehaiyan/take-down.git (fetch)
gitee   https://gitee.com/yuehaiyan/take-down.git (push)
github  https://github.com/yue-hai/TakeDown.git (fetch)
github  https://github.com/yue-hai/TakeDown.git (push)

PS D:\Idea\save\TakeDown\.idea>
```

8. 进入 idea 查看：

![](attachments/Pasted%20image%2020240819085100.png)

9. 此时推送时就可以选择推送到哪里：

![](attachments/Pasted%20image%2020240819085124.png)

## 8、将文件或目录加入忽略列表

1. `.git\info\exclude` 文件是一个本地的忽略文件，不会被提交到远程仓库，所以可以将一些不想提交的文件或目录加入到这个文件中
2. `.gitignore` 文件是一个全局的忽略文件，会被提交到远程仓库，所以可以将一些不想提交的文件或目录加入到这个文件中
3. 两个文件的格式是一样的，都是一行一个文件或目录，可以使用通配符
4. 比如：

```shell
# 忽略所有 .class 文件
*.class

# 忽略所有 .log 文件
*.log

# 忽略所有 target 目录
target

# 忽略所有 /公司/ 目录下的文件
/公司/*
```

## 9、变基无法终止，也无法继续

### ①、问题

1. 无法继续变基，提示：

```shell
You must edit all merge conflicts and then mark them as resolved using git add
```

2. 无法终止变基，提示：

```shell
warning: could not read '.git/rebase-merge/head-name': No such file or directory
```

3. `git status` 提示：

```shell
PS D:\OneDrive\文档资料\TakeDown> git status
On branch master
Your branch is ahead of 'github/master' by 9 commits.
  (use "git push" to publish your local commits)

You are currently rebasing.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .idea/.gitignore
        new file:   .idea/TakeDown.iml
        new file:   .idea/misc.xml
        new file:   .idea/modules.xml
        new file:   .idea/shelf/___.xml
        new file:   ".idea/shelf/\345\234\250\345\217\230\345\237\272\344\271\213\345\211\215\346\234\252\346\217\220\344\272\244\347\232\204\346\233\264\346\224\271_[\346\233\264\346\224\271]/shelved.patch"
        new file:   .idea/vcs.xml
        new file:   .idea/workspace.xml

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    .idea/TakeDown.iml
        deleted:    .idea/misc.xml
        deleted:    .idea/modules.xml
        deleted:    .idea/shelf/___.xml
        deleted:    ".idea/shelf/\345\234\250\345\217\230\345\237\272\344\271\213\345\211\215\346\234\252\346\217\220\344\272\244\347\232\204\346\233\264\346\224\271_[\346\233\264\346\224\271]/shelved.patch"
        deleted:    .idea/workspace.xml

PS D:\OneDrive\文档资料\TakeDown>
```

### ②、解决办法

1. 删除变基的临时目录，清除当前变基状态：删除 `.git/rebase-merge` 目录
2. 将分支重置到当前的最后一次提交状态：

```shell
git reset --hard HEAD
```

## 11、

## 12、

## 13、

## 14、

## 15、




