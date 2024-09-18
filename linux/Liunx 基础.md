> 菜鸟教程：[https://www.runoob.com/linux/linux-tutorial.html](https://www.runoob.com/linux/linux-tutorial.html)

# 零、其他命令

## 1、输出字符串：`echo`

### ①、命令格式

```shell
echo string
```

### ②、普通字符串

```shell
echo "It is a test"
```

### ③、普通字符串可省略双引号

```shell
echo It is a test
```

### ④、显示转义字符

```shell
echo "\"It is a test\""
```

结果：

```shell
"It is a test"
```

同样，双引号也可以省略

### ⑤、显示变量

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量

```shell
#!/bin/sh
read name 
echo "$name It is a test"

# 以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:
[root@www ~]# sh test.sh
OK                     #标准输入
OK It is a test        #输出
```

### ⑥、显示换行

```shell
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
```

输出结果：

```shell
OK! 
It is a test
```

### ⑦、显示不换行

```shell
#!/bin/sh 
echo -e "OK! \c" # -e 开启转义 \c 不换行 
`echo "It is a test"
```

输出结果：

```shell
OK! It is a test
```

### ⑧、显示结果保存至文件

#### Ⅰ、覆盖

```shell
echo "It is a test" > myfile
```

#### Ⅱ、在源文件最后追加

```shell
echo "It is a test" >> myfile
```

### ⑨、原样输出字符串，不进行转义或取变量(用单引号)

```shell
echo '$name\"'
```

输出结果：

```shell
$name\"
```

### ⑩、显示命令执行结果

- 注意： 这里使用的是反引号 \`, 而不是单引号 `'` 

```shell
echo `date`
```

结果将显示当前日期

```shell
Thu Jul 24 10:08:46 CST 2014
```

## 2、管道：`|`

### ①、`-` 代表传过来的数据

1. 不写 `-` 默认传过来的数据是在最后
2. 写 `-` 代表传过来的数据在 `-` 的地方： `sort -k1,3 data | head -n5 -`（虽然这个例子并不能看出来，不过 join 命令的时候会用到）

## 3、Ubuntu 下创建新用户

### ①、`adduer`

- 对应着删除用户的命令：`deluser`

1. `sudo adduser newUer`
2. 会自动为创建的用户指定主目录、系统 shell 版本，会在创建时输入用户密码
3. 认情况下：
   1. `adduser` 在创建用户时会主动调用 `/etc/adduser.conf`
   2. 在创建用户主目录时默认在 `/home` 下，而且创建为 `/home/用户名`
   3. 如果主目录已经存在，就不再创建，但是此主目录虽然作为新用户的主目录，而且默认登录时会进入这个目录下，但是这个目录并不是属于新用户，当使用 `userdel` 删除新用户时，并不会删除这个主目录，因为这个主目录在创建前已经存在且并不属于这个用户。
   4. 为用户指定 shell 版本为：`/bin/bash`
4. 常用参数选项为：
   1. `–home`： 指定创建主目录的路径，默认是在 /home 目录下创建用户名同名的目录，这里可以指定；如果主目录同名目录存在，则不再创建，仅在登录时进入主目录。
   2. `–quiet`： 即只打印警告和错误信息，忽略其他信息。
   3. `–debug`： 定位错误信息。
   4. `–conf`： 在创建用户时使用指定的configuration文件。
   5. `–force-badname`： 默认在创建用户时会进行/etc/adduser.conf中的正则表达式检查用户名是否合法，如果想使用弱检查，则使用这个选项，如果不想检查，可以将/etc/adduser.conf中相关选项屏蔽。如：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2FPasted%20image%2020230725150747.png)

### ②、`useradd`

- 对应着删除用户的命令：`userdel`
1. 使用任何参数选项创建用户：`sudo useradd newUer`
2. 为用户指定登录密码：`sudo passwd newUer`
3. 需要使用参数选项指定基本设置，如果不使用任何参数，则创建的用户无密码、无主目录、没有指定 shell 版本
4. 为用户指定命令解释程序(通常为/bin/bash)：`sudo usermod -s /bin/bash tt`
5. 为用户指定用户主目录：`sudo usermod -d /home/tt tt`
6. 常用为用户指定参数的useradd命令：
   1. `-d`： 指定用户的主目录
   2. `-m`： 如果存在不再创建，但是此目录并不属于新创建用户；如果主目录不存在，则强制创建； -m和-d一块使用。
   3. `-s`： 指定用户登录时的shell版本
   4. `-M`： 不创建主目录

# 一、**文件管理**

## 1、显示文件内容：`cat、more、less`

### ①、cat：一次性在终端中显示文件的所有内容

#### Ⅰ、语法格式

`cat 参数 文件`

#### Ⅱ、参数说明

| -n 或 --number | 由 1 开始对所有输出的行数编号 |
| --- | --- |
| -b 或 --number-nonblank | 和 -n 相似，只不过对于空白行不编号 |
| -s 或 --squeeze-blank | 当遇到有连续两行以上的空白行，就代换为一行的空白行 |
| -v 或 --show-nonprinting | 使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外 |
| -E 或 --show-ends | 在每行结束处显示 $ |
| -T 或 --show-tabs | 将 TAB 字符显示为 ^I |

#### Ⅲ、实例

1. 把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里：`cat -n textfile1 > textfile2`
2. 把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：`cat -b textfile1 textfile2 >> textfile3`
3. 清空 /etc/test.txt 文档内容：`cat /dev/null > /etc/test.txt`

### ②、more：分页显示

#### Ⅰ、语法格式

`more 参数 文件`

#### Ⅱ、参数说明

| -num | 一次显示的行数 |
| --- | --- |
| -d | 提示使用者，在画面下方显示 [Press space to continue, 'q' to quit.] ，如果使用者按错键，则会显示 [Press 'h' for instructions.] 而不是 '哔' 声 |
| -l | 取消遇见特殊字元 ^L（送纸字元）时会暂停的功能 |
| -f | 计算行数时，以实际上的行数，而非自动换行过后的行数（有些单行字数太长的会被扩展为两行或两行以上） |
| -p | 不以卷动的方式显示每一页，而是先清除萤幕后再显示内容 |
| -c | 跟 -p 相似，不同的是先显示内容再清除其他旧资料 |
| -s | 当遇到有连续两行以上的空白行，就代换为一行的空白行 |
| -u | 不显示下引号 （根据环境变数 TERM 指定的 terminal 而有所不同） |
| +/pattern | 在每个文档显示前搜寻该字串（pattern），然后从该字串之后开始显示 |
| +num | 从第 num 行开始显示 |

#### Ⅲ、常用操作命令

1. Enter 向下n行，需要定义。默认为1行
2. Ctrl+F 向下滚动一屏
3. 空格键 向下滚动一屏
4. Ctrl+B 返回上一屏
5. = 输出当前行的行号
6. ：f 输出文件名和当前行的行号
7. V 调用vi编辑器
8. !命令 调用Shell，并执行命令
9. q 退出more

### ③、less：分页显示

与 more 类似

## 2、显示文件开头内容：`head`

head 命令可用于查看文件的开头部分的内容，有一个常用的参数 -n 用于显示行数，默认为 10，即显示 10 行的内容

### ①、语法

`head 参数 文件`

### ②、参数

1. -q 隐藏文件名
2. -v 显示文件名
3. -c<数目> 显示的字节数。
4. -n<行数> 显示的行数。

## 3、显示文件结尾内容：`tail`

tail 命令可用于查看文件的结尾部分的内容，有一个常用的参数 -n 用于显示行数，默认为 10，即显示 10 行的内容

### ①、语法

`tail 参数 文件`

### ②、参数

1. -f 循环读取
2. -q 不显示处理信息
3. -v 显示详细的处理信息
4. -c<数目> 显示的字节数
5. -n<行数> 显示文件的尾部 n 行内容
6. --pid=PID 与-f合用,表示在进程ID,PID死掉之后结束
7. -q, --quiet, --silent 从不输出给出文件名的首部
8. -s, --sleep-interval=S 与-f合用,表示在每次反复的间隔休眠S秒

## 4、创建文件：`touch`

`Linux touch` 命令用于修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不存在，系统会建立一个新的文件。
`ls -l` 可以显示档案的时间记录

### ①、语法

`touch 文件名`

### ②、参数

![image.png](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2F2023-07-25-13--14-19-774--HCn3-mVRxk9Yhg.png)

## 5、移动文件/更改文件名：`mv`

### ①、语法

- 假如一个文件名为：yuehai，对其进行操作

#### Ⅰ、移动文件

`mv 原目录/yuehai 新目录/yuehai`

#### Ⅱ、改名

`mv yuehai yuehai123`

#### Ⅲ、移动文件并改名

`mv 原目录/yuehai 新目录/yuehai123`

### ②、参数

1. -b: 当目标文件或目录存在时，在执行覆盖前，会为其创建一个备份。
2. -i: 如果指定移动的源目录或文件与目标的目录或文件同名，则会先询问是否覆盖旧文件，输入 y 表示直接覆盖，输入 n 表示取消该操作。
3. -f: 如果指定移动的源目录或文件与目标的目录或文件同名，不会询问，直接覆盖旧文件。
4. -n: 不要覆盖任何已存在的文件或目录。
5. -u：当源文件比目标文件新或者目标文件不存在时，才执行移动操作。

## 6、复制文件或目录：`cp`

### ①、语法

`cp 原目录/文件 新目录/文件`

### ②、参数

1. -a：此选项通常在复制目录时使用，它保留链接、文件属性，并复制目录下的所有内容。其作用等于dpR参数组合。
2. -d：复制时保留链接。这里所说的链接相当于 Windows 系统中的快捷方式。
3. -f：覆盖已经存在的目标文件而不给出提示。
4. -i：与 **-f** 选项相反，在覆盖目标文件之前给出提示，要求用户确认是否覆盖，回答 **y** 时目标文件将被覆盖。
5. -p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
6. -r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。
7. -l：不复制文件，只是生成链接文件。

## 7、删除文件或目录：`rm`

### ①、语法

`rm 目录（或文件）`

### ②、参数

1. -i 删除前逐一询问确认。
2. -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
3. -r 将目录及以下之档案亦逐一删除。

## 8、更改权限：`chmod`

### ①、简介

1. Linux chmod（英文全拼：change mode）命令是控制用户对文件的权限的命令
2. Linux/Unix 的文件调用权限分为三级 : 文件所有者（Owner）、用户组（Group）、其它用户（Other Users）

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2FPasted%20image%2020230725151003.png)

### ②、语法

`chmod 参数 权限设置 文件（或目录）`

- mode : 权限设定字串，格式如下
- `[ugoa...][[+-=][rwxX]...][,...]`
- u 表示该文件的拥有者，g 表示与该文件的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。
- + 表示增加权限、- 表示取消权限、= 表示唯一设定权限。
- r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行。

### ③、语法模式

只有文件所有者和超级用户可以修改文件或目录的权限。可以使用**绝对模式**（八进制数字模式），**符号模式**指定文件的权限

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2FPasted%20image%2020230726092132.png)

### ④、绝对模式（八进制数字模式）

1. chmod命令可以使用八进制数来指定权限
2. 文件或目录的权限位是由9个权限位来控制，每三位为一组，它们分别是：
   1. 文件所有者（User）的读、写、执行
   2. 用户组（Group）的读、写、执行
   3. 其它用户（Other）的读、写、执行

| # | 权限 | rwx | 二进制 |
| --- | --- | --- | --- |
| 7 | 读 + 写 + 执行 | rwx | 111 |
| 6 | 读 + 写 | rw- | 110 |
| 5 | 读 + 执行 | r-x | 101 |
| 4 | 只读 | r-- | 100 |
| 3 | 写 + 执行 | -wx | 011 |
| 2 | 只写 | -w- | 010 |
| 1 | 只执行 | --x | 001 |
| 0 | 无 | --- | 000 |

3. 例如， 765 将这样解释：
   1. 所有者的权限用数字表达：属主的那三个权限位的数字加起来的总和。如 rwx ，也就是 4+2+1 ，应该是 7。
   2. 用户组的权限用数字表达：属组的那个权限位数字的相加的总和。如 rw- ，也就是 4+2+0 ，应该是 6。
   3. 其它用户的权限数字表达：其它用户权限位的数字相加的总和。如 r-x ，也就是 4+0+1 ，应该是 5。
4. 如：`chmod 777 file`：
   1. 语法为：`chmod abc file`，和  `chmod a=rwx file` 效果相同
   2. 其中 a,b,c 各为一个数字，分别表示User、Group、及Other的权限。
   3. r=4，w=2，x=1
   4. 若要 rwx 属性则 4+2+1=7；
   5. 若要 rw- 属性则 4+2=6；
   6. 若要 r-x 属性则 4+1=5
5. `chmod 771 file` 和 `chmod ug=rwx,o=x file` 效果相同
6. 若用 `chmod 4755 filename` 可使此程序具有 root 的权限

## 9、远程文件复制：`scp`

Linux scp 命令用于 Linux 之间复制文件和目录。
scp 是 secure copy 的缩写, scp 是 linux 系统下基于 ssh 登陆进行安全的远程文件拷贝命令。
scp 是加密的，rcp 是不加密的，scp 是 rcp 的加强版

### ①、语法

#### Ⅰ、本地复制到远程

`scp 参数 本地文件 远程用户名@IP地址:文件`

#### Ⅱ、远程复制到本地

`scp 参数 远程用户名@IP地址:文件 本地文件`

### ②、参数

1. -1： 强制scp命令使用协议ssh1
2. -2： 强制scp命令使用协议ssh2
3. -4： 强制scp命令只使用IPv4寻址
4. -6： 强制scp命令只使用IPv6寻址
5. -B： 使用批处理模式（传输过程中不询问传输口令或短语）
6. -C： 允许压缩。（将-C标志传递给ssh，从而打开压缩功能）
7. -p：保留原文件的修改时间，访问时间和访问权限。
8. -q： 不显示传输进度条。
9. -r： 递归复制整个目录。
10. -v：详细方式显示输出。scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题。
11. -c cipher： 以cipher将数据传输进行加密，这个选项将直接传递给ssh。
12. -F ssh_config： 指定一个替代的ssh配置文件，此参数直接传递给ssh。
13. -i identity_file： 从指定文件中读取传输时使用的密钥文件，此参数直接传递给ssh。
14. -l limit： 限定用户所能使用的带宽，以Kbit/s为单位。
15. -o ssh_option： 如果习惯于使用ssh_config(5)中的参数传递方式，
16. -P port：注意是大写的P, port是指定数据传输用到的端口号
17. -S program： 指定加密传输时所使用的程序。此程序必须能够理解ssh(1)的选项。

## 10、备份文件：`tar`

### ①、语法

`tar [-ABcdgGhiklmMoOpPrRsStuUvwWxzZ][-b <区块数目>][-C <目的目录>][-f <备份文件>][-F <Script文件>][-K <文件>][-L <媒体容量>][-N <日期时间>]`
`[-T <范本文件>][-V <卷册名称>][-X <范本文件>][-<设备编号><存储密度>][--after-date=<日期时间>][--atime-preserve][--backuup=<备份方式>][--checkpoint]`
`[--concatenate][--confirmation][--delete][--exclude=<范本样式>][--force-local][--group=<群组名称>][--help][--ignore-failed-read]`
`[--new-volume-script=<Script文件>][--newer-mtime][--no-recursion][--null][--numeric-owner][--owner=<用户名称>][--posix][--erve][--preserve-order]`
`[--preserve-permissions][--record-size=<区块数目>][--recursive-unlink][--remove-files][--rsh-command=<执行指令>][--same-owner]`
`[--suffix=<备份字尾字符串>][--totals][--use-compress-program=<执行指令>][--version][--volno-file=<编号文件>][文件或目录...]`

### ②、参数

1. -A或--catenate 新增文件到已存在的备份文件。
2. -b<区块数目>或--blocking-factor=<区块数目> 设置每笔记录的区块数目，每个区块大小为12Bytes。
3. -B或--read-full-records 读取数据时重设区块大小。
4. -c或--create 建立新的备份文件。
5. -C<目的目录>或--directory=<目的目录> 切换到指定的目录。
6. -d或--diff或--compare 对比备份文件内和文件系统上的文件的差异。
7. -f<备份文件>或--file=<备份文件> 指定备份文件。
8. -F<Script文件>或--info-script=<Script文件> 每次更换磁带时，就执行指定的Script文件。
9. -g或--listed-incremental 处理GNU格式的大量备份。
10. -G或--incremental 处理旧的GNU格式的大量备份。
11. -h或--dereference 不建立符号连接，直接复制该连接所指向的原始文件。
12. -i或--ignore-zeros 忽略备份文件中的0 Byte区块，也就是EOF。
13. -k或--keep-old-files 解开备份文件时，不覆盖已有的文件。
14. -K<文件>或--starting-file=<文件> 从指定的文件开始还原。
15. -l或--one-file-system 复制的文件或目录存放的文件系统，必须与tar指令执行时所处的文件系统相同，否则不予复制。
16. -L<媒体容量>或-tape-length=<媒体容量> 设置存放每体的容量，单位以1024 Bytes计算。
17. -m或--modification-time 还原文件时，不变更文件的更改时间。
18. -M或--multi-volume 在建立，还原备份文件或列出其中的内容时，采用多卷册模式。
19. -N<日期格式>或--newer=<日期时间> 只将较指定日期更新的文件保存到备份文件里。
20. -o或--old-archive或--portability 将资料写入备份文件时使用V7格式。
21. -O或--stdout 把从备份文件里还原的文件输出到标准输出设备。
22. -p或--same-permissions 用原来的文件权限还原文件。
23. -P或--absolute-names 文件名使用绝对名称，不移除文件名称前的"/"号。
24. -r或--append 新增文件到已存在的备份文件的结尾部分。
25. -R或--block-number 列出每个信息在备份文件中的区块编号。
26. -s或--same-order 还原文件的顺序和备份文件内的存放顺序相同。
27. -S或--sparse 倘若一个文件内含大量的连续0字节，则将此文件存成稀疏文件。
28. -t或--list 列出备份文件的内容。
29. -T<范本文件>或--files-from=<范本文件> 指定范本文件，其内含有一个或多个范本样式，让tar解开或建立符合设置条件的文件。
30. -u或--update 仅置换较备份文件内的文件更新的文件。
31. -U或--unlink-first 解开压缩文件还原文件之前，先解除文件的连接。
32. -v或--verbose 显示指令执行过程。
33. -V<卷册名称>或--label=<卷册名称> 建立使用指定的卷册名称的备份文件。
34. -w或--interactive 遭遇问题时先询问用户。
35. -W或--verify 写入备份文件后，确认文件正确无误。
36. -x或--extract或--get 从备份文件中还原文件。
37. -X<范本文件>或--exclude-from=<范本文件> 指定范本文件，其内含有一个或多个范本样式，让ar排除符合设置条件的文件。
38. -z或--gzip或--ungzip 通过gzip指令处理备份文件。
39. -Z或--compress或--uncompress 通过compress指令处理备份文件。
40. -<设备编号><存储密度> 设置备份用的外围设备编号及存放数据的密度。
41. --after-date=<日期时间> 此参数的效果和指定"-N"参数相同。
42. --atime-preserve 不变更文件的存取时间。
43. --backup=<备份方式>或--backup 移除文件前先进行备份。
44. --checkpoint 读取备份文件时列出目录名称。
45. --concatenate 此参数的效果和指定"-A"参数相同。
46. --confirmation 此参数的效果和指定"-w"参数相同。
47. --delete 从备份文件中删除指定的文件。
48. --exclude=<范本样式> 排除符合范本样式的文件。
49. --group=<群组名称> 把加入设备文件中的文件的所属群组设成指定的群组。
50. --help 在线帮助。
51. --ignore-failed-read 忽略数据读取错误，不中断程序的执行。
52. --new-volume-script=<Script文件> 此参数的效果和指定"-F"参数相同。
53. --newer-mtime 只保存更改过的文件。
54. --no-recursion 不做递归处理，也就是指定目录下的所有文件及子目录不予处理。
55. --null 从null设备读取文件名称。
56. --numeric-owner 以用户识别码及群组识别码取代用户名称和群组名称。
57. --owner=<用户名称> 把加入备份文件中的文件的拥有者设成指定的用户。
58. --posix 将数据写入备份文件时使用POSIX格式。
59. --preserve 此参数的效果和指定"-ps"参数相同。
60. --preserve-order 此参数的效果和指定"-A"参数相同。
61. --preserve-permissions 此参数的效果和指定"-p"参数相同。
62. --record-size=<区块数目> 此参数的效果和指定"-b"参数相同。
63. --recursive-unlink 解开压缩文件还原目录之前，先解除整个目录下所有文件的连接。
64. --remove-files 文件加入备份文件后，就将其删除。
65. --rsh-command=<执行指令> 设置要在远端主机上执行的指令，以取代rsh指令。
66. --same-owner 尝试以相同的文件拥有者还原文件。
67. --suffix=<备份字尾字符串> 移除文件前先行备份。
68. --totals 备份文件建立后，列出文件大小。
69. --use-compress-program=<执行指令> 通过指定的指令处理备份文件。
70. --version 显示版本信息。
71. --volno-file=<编号文件> 使用指定文件内的编号取代预设的卷册编号。

### ③、说明

### ④、案例

1. 压缩文件 非打包

```shell
# touch a.c       
# tar -czvf test.tar.gz a.c   //压缩 a.c文件为test.tar.gz
a.c
```

2. 列出压缩文件内容

```shell
# tar -tzvf test.tar.gz 
-rw-r--r-- root/root     0 2010-05-24 16:51:59 a.c
```

3. 解压文件

```shell
# tar -xzvf test.tar.gz 
a.c
```

## 11、

## 12、

# 二、**文档编辑**

## 0、vim

### ①、什么是 vim

> Vim 是从 vi 发展出来的一个文本编辑器。代码补全、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。
> 简单的来说， vi 是老式的字处理器，不过功能已经很齐全了，但是还是有可以进步的地方。 vim 则可以说是程序开发者的一项很好用的工具。
> 连 vim 的官方网站 ([https://www.vim.org/)](https://www.vim.org/)) 自己也说 vim 是一个程序开发工具而不是文字处理软件

### ②、vim 键盘图

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2FPasted%20image%2020230726092146.png)

### ③、vi/vim 的使用

- 基本上 vi/vim 共分为三种模式，分别是**命令模式**（Command mode），**输入模式**（Insert mode）和**底线命令模式**（Last line mode）

#### Ⅰ、命令模式

1. 用户刚刚启动 vi/vim，便进入了命令模式
2. 此状态下敲击键盘动作会被 Vim 识别为命令，而非输入字符。比如我们此时按下 i，并不会输入一个字符，i 被当作了一个命令
3. 以下是常用的几个命令：
   1. i：切换到输入模式，以输入字符。
   2. x：删除当前光标所在处的字符。
   3. :  ：切换到底线命令模式，以在最底一行输入命令。
4. 若想要编辑文本：启动Vim，进入了命令模式，按下i，切换到输入模式
5. 命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令

#### Ⅱ、输入模式

1. 在命令模式下按下i就进入了输入模式
2. 在输入模式中，可以使用以下按键
   1. 字符按键以及 Shift 组合，输入字符
   2. ENTER，回车键，换行
   3. BACK SPACE，退格键，删除光标前一个字符
   4. DEL，删除键，删除光标后一个字符
   5. 方向键，在文本中移动光标
   6. HOME/END，移动光标到行首/行尾
   7. Page Up/Page Down，上/下翻页
   8. Insert，切换光标为输入/替换模式，光标将变成竖线/下划线
   9. ESC，退出输入模式，切换到命令模式

#### Ⅲ、底线命令模式

1. 在命令模式下按下:（英文冒号）就进入了底线命令模式
2. 底线命令模式可以输入单个或多个字符的命令，可用的命令非常多
3. 在底线命令模式中，基本的命令有（已经省略了冒号）
   1. q：退出程序
   2. w：保存文件
   3. wq：保存并退出
4. 按 ESC 键可随时退出底线命令模式

### ④、vi/vim 工作模式

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2FPasted%20image%2020230725151303.png)

### ⑤、按键：复制粘贴、搜索替换等

| **一般模式可用的命令** |  |
| --- | --- |
| `[Ctrl] + [f]` | 屏幕『向下』移动一页，相当于 `[Page Down`] 按键 (常用) |
| `[Ctrl] + [b]` | 屏幕『向上』移动一页，相当于 `[Page Up]` 按键 (常用) |
| `0` 或功能键 `[Home]` | 这是数字『 0 』：移动到这一行的最前面字符处 (常用) |
| `$` 或功能键 `[End]` | 移动到这一行的最后面字符处(常用) |
| `H` | 光标移动到这个屏幕的最上方那一行的第一个字符 |
| `M` | 光标移动到这个屏幕的中央那一行的第一个字符 |
| `L` | 光标移动到这个屏幕的最下方那一行的第一个字符 |
| `G` | 移动到这个档案的最后一行(常用) |
| `nG` | n 为数字。移动到这个档案的第 n 行。例如 20G 则会移动到这个档案的第 20 行(可配合 :`set nu`) |
| `gg` | 移动到这个档案的第一行，相当于 1G  (常用) |
| `n<Enter>` | n 为数字。光标向下移动 n 行(常用) |
| `/word` | 向光标之下寻找一个名称为 word 的字符串。例如要在档案内搜寻 vbird 这个字符串，就输入 `/vbird` 即可！ (常用) |
| `?word` | 向光标之上寻找一个字符串名称为 word 的字符串。 |
| `n` | 这个 n 是英文按键。代表重复前一个搜寻的动作。举例来说， 如果刚刚我们执行 /vbird 去向下搜寻 vbird 这个字符串，则按下 n 后，会向下继续搜寻下一个名称为 vbird 的字符串。如果是执行 ?vbird 的话，那么按下 n 则会向上继续搜寻名称为 vbird 的字符串！ |
| `N` | 这个 N 是英文按键。与 n 刚好相反，为『反向』进行前一个搜寻动作。 例如 /vbird 后，按下 N 则表示『向上』搜寻 vbird  |
| `dd` | 剪切游标所在的那一整行(常用)，用 p/P 可以粘贴。 |
| `ndd` | n 为数字。剪切光标所在的向下 n 行，例如 20dd 则是剪切 20 行(常用)，用 p/P 可以粘贴。 |
| `d1G` | 删除光标所在到第一行的所有数据 |
| `dG` | 删除光标所在到最后一行的所有数据 |
| `d$` | 删除游标所在处，到该行的最后一个字符 |
| `d0` | 那个是数字的 0 ，删除游标所在处，到该行的最前面一个字符 |
| `yy` | 复制游标所在的那一行(常用) |
| `nyy` | n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行(常用) |
| `y1G` | 复制游标所在行到第一行的所有数据 |
| `yG` | 复制游标所在行到最后一行的所有数据 |
| `y0` | 复制光标所在的那个字符到该行行首的所有数据 |
| `y`$ | 复制光标所在的那个字符到该行行尾的所有数据 |
| `p`, P | p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！ 举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？ 那么原本的第 20 行会被推到变成 30 行。 (常用) |
| `J` | 将光标所在行与下一行的数据结合成同一行 |
| `c` | 重复删除多个数据，例如向下删除 10 行，`[ 10cj ]` |
| `u` | 复原前一个动作。(常用) |
| `[Ctrl]+r` | 重做上一个动作。(常用) |
| `.` | 不要怀疑！这就是小数点！意思是重复前一个动作的意思。 如果你想要重复删除、重复贴上等等动作，按下小数点『.』就好了！ (常用) |
| **命令模式可用的命令** |  |
| `:w` | 将编辑的数据写入硬盘档案中(常用) |
| `:w!` | 若文件属性为『只读』时，强制写入该档案。不过，到底能不能写入， 还是跟你对该档案的档案权限有关啊！ |
| `:q` | 离开 vi (常用) |
| `:q!` | 若曾修改过档案，又不想储存，使用 ! 为强制离开不储存档案。 |
| `:wq` | 储存后离开，若为 :wq! 则为强制储存后离开 (常用) |

## 1、文件内容排序：`sort`

sort 可针对文本文件的内容，以行为单位来排序

### ①、语法

`sort 参数 文件`

### ②、参数

1. -b 忽略每行前面开始出的空格字符。
2. -c 检查文件是否已经按照顺序排序。
3. -d 排序时，处理英文字母、数字及空格字符外，忽略其他的字符。
4. -f 排序时，将小写字母视为大写字母。
5. -i 排序时，除了040至176之间的ASCII字符外，忽略其他的字符。
6. -m 将几个排序好的文件进行合并。
7. -M 将前面3个字母依照月份的缩写进行排序。
8. -n 依照数值的大小排序。
9. -u 意味着是唯一的(unique)，输出的结果是去完重了的。
10. -o<输出文件> 将排序后的结果存入指定的文件。
11. -r 以相反的顺序来排序（倒序）
12. -t<分隔字符> 指定排序时所用的栏位分隔字符。
13. +<起始栏位>-<结束栏位> 以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位
14. [-k 开始排序的列,结束排序的列] 按指定的列进行排序。
   1. `sort -k3,3 -k8,8 tencd`：第3行开始排序，至第3行结束；第8行开始排序，至第8行结束
   2. `sort -k3 tencd`：第3行开始排序，一直到最后

## 2、删除文件中重复的行：`uniq`

Linux uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用

### ①、语法

`uniq 参数 文件`

### ②、参数

1. -c或--count 在每列旁边显示该行重复出现的次数。
2. -d或--repeated 仅显示重复出现的行列。
3. -f<栏位>或--skip-fields=<栏位> 忽略比较指定的栏位。
4. -s<字符位置>或--skip-chars=<字符位置> 忽略比较指定的字符。
5. -u或--unique 仅显示出一次的行列。
6. -w<字符位置>或--check-chars=<字符位置> 指定要比较的字符。
7. --help 显示帮助。
8. --version 显示版本信息。
9. [输入文件] 指定已排序好的文本文件。如果不指定此项，则从标准读取数据；
10. [输出文件] 指定输出的文件。如果不指定此选项，则将内容显示到标准输出设备（显示终端）。

## 3、查找文件中的字符串：`grep`

grep 指令用于查找内容包含指定的范本样式的文件，如果发现某文件的内容符合所指定的范本样式，预设 grep 指令会把含有范本样式的那一列显示出来。若不指定任何文件名称，或是所给予的文件名为 -，则 grep 指令会从标准输入设备读取数据

### ①、语法

`grep 查找的字符串 文件`

1. 若是指定文件，则会在当前文件中查找指定的字符串，当某一行中有指定的字符串时，会将这一行输出出来

```shell
[trial@localhost data]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost data]$ grep '1' data
3 2 1
1 2 3
1 3 3
1 1 1
1 4 6
3 2 1
2 1 4
2 1 3
```

2. 查找以指定字符串结尾的行：`^abc`

```shell
[trial@localhost topic5]$ cat grep_file 
Linux
LINUX
123456

12
12456
abcdefghlig
ac
abc
abbc
abbbc
abbbbc
a1c
abbbbbbc

ab2c
abcabcabcdefdef
113-1234
 113-1234
  113-1234
   113-1234
a.b
1a
ab|11 
a
121234
12121234
abc||
abcd123456789
123abc
cab
cccc
adef
abc123abc
123+
[trial@localhost topic5]$ grep '^abc' grep_file 
abcdefghlig
abc
abcabcabcdefdef
abc||
abcd123456789
abc123abc
```

3. 查找以指定字符串结尾的行：`abc$`

```shell
[trial@localhost topic5]$ cat grep_file 
Linux
LINUX
123456

12
12456
abcdefghlig
ac
abc
abbc
abbbc
abbbbc
a1c
abbbbbbc

ab2c
abcabcabcdefdef
113-1234
 113-1234
  113-1234
   113-1234
a.b
1a
ab|11 
a
121234
12121234
abc||
abcd123456789
123abc
cab
cccc
adef
abc123abc
123+
[trial@localhost topic5]$ grep 'abc$' grep_file 
abc
123abc
abc123abc
```

4. 匹配区间：`[a-z]`：
   1. 小写字母：`[a-z]`

```shell
[trial@localhost topic5]$ grep '[a-z]' grep_file 
Linux
abcdefghlig
ac
abc
abbc
abbbc
abbbbc
a1c
abbbbbbc
ab2c
abcabcabcdefdef
a.b
1a
ab|11 
a
abc||
abcd123456789
123abc
cab
cccc
adef
abc123abc
```

   2. 大写字母：`[A-Z]`

```shell
[trial@localhost topic5]$ grep '[A-Z]' grep_file 
Linux
LINUX
```

   3. 含有数字：`[0-9]`

```shell
[trial@localhost topic5]$ grep '[0-9]' grep_file 
123456
12
12456
a1c
ab2c
113-1234
 113-1234
  113-1234
   113-1234
1a
ab|11 
121234
12121234
abcd123456789
123abc
abc123abc
123+
```

   4. 匹配除换行符 \n 之外的任何单字符：`.`

```shell
[trial@localhost topic5]$ grep 'a.c' grep_file 
abcdefghlig
abc
a1c
abcabcabcdefdef
abc||
abcd123456789
123abc
abc123abc
```

   5. 含有区间：`[a-z]`

```shell
[trial@localhost topic5]$ grep 'a[a-g]c' grep_file
abcdefghlig
abc
abcabcabcdefdef
abc||
abcd123456789
123abc
abc123abc
```

   6. 排除区间：`[^a-z]`
```shell
[trial@localhost topic5]$ grep 'a[^a-g]c' grep_file
a1c
```

5. 正则表达式：需使用参数 `-E` 
   1. 

### ②、参数

1. -a 或 --text : 不要忽略二进制的数据。
2. -A<显示行数> 或 --after-context=<显示行数> : 除了显示符合范本样式的那一列之外，并显示该行之后的内容。
3. -b 或 --byte-offset : 在显示符合样式的那一行之前，标示出该行第一个字符的编号。
4. -B<显示行数> 或 --before-context=<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前的内容。
5. -c 或 --count : 计算符合样式的列数。
6. -C<显示行数> 或 --context=<显示行数>或-<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前后的内容。
7. -d <动作> 或 --directories=<动作> : 当指定要查找的是目录而非文件时，必须使用这项参数，否则grep指令将回报信息并停止动作。
8. -e<范本样式> 或 --regexp=<范本样式> : 指定字符串做为查找文件内容的样式。
9. -E 或 --extended-regexp : 将样式为延伸的正则表达式来使用。
10. -f<规则文件> 或 --file=<规则文件> : 指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式。
11. -F 或 --fixed-regexp : 将样式视为固定字符串的列表。
12. -G 或 --basic-regexp : 将样式视为普通的表示法来使用。
13. -h 或 --no-filename : 在显示符合样式的那一行之前，不标示该行所属的文件名称。
14. -H 或 --with-filename : 在显示符合样式的那一行之前，表示该行所属的文件名称。
15. -i 或 --ignore-case : 忽略字符大小写的差别。
16. -l 或 --file-with-matches : 列出文件内容符合指定的样式的文件名称。
17. -L 或 --files-without-match : 列出文件内容不符合指定的样式的文件名称。
18. -n 或 --line-number : 在显示符合样式的那一行之前，标示出该行的列数编号。
19. -o 或 --only-matching : 只显示匹配PATTERN 部分。
20. -q 或 --quiet或--silent : 不显示任何信息。
21. -r 或 --recursive : 此参数的效果和指定"-d recurse"参数相同。
22. -s 或 --no-messages : 不显示错误信息。
23. -v 或 --invert-match : 显示不包含匹配文本的所有行。
24. -V 或 --version : 显示版本信息。
25. -w 或 --word-regexp : 只显示全字符合的列。
26. -x --line-regexp : 只显示全列符合的列。
27. -y : 此参数的效果和指定"-i"参数相同。

## 4、计算字数：`wc`

Linux wc 命令用于计算字数。
利用 wc 指令我们可以计算文件的 Byte 数、字数、或是列数，若不指定文件名称、或是所给予的文件名为"-"，则 wc 指令会从标准输入设备读取数据

### ①、语法

`wc [-clw][--help][--version][文件...]`
`wc 参数 文件名`
不加参数时，结果会显示：行数、字数、字节数、文件名

### ②、参数

1. -c或--bytes或--chars 只显示 Bytes 数
2. -l或--lines 显示行数
3. -w或--words 只显示字数

## 5、用脚本来处理文本文件：`sed`

1. Linux sed 命令是利用脚本来处理文本文件
2. sed 可依照脚本的指令来处理、编辑文本文件
3. sed 主要用来自动编辑一个或多个文件、简化对文件的反复操作、编写转换程序等
4. 注意要使用单引号：`''`

### ①、语法

`sed [-hnV][-e<script>][-f<script文件>][文本文件]
`
### ②、参数

1. -e：`<script>` 或 `--expression=<script>` 以选项中指定的script来处理输入的文本文件。
2. -f：`<script文件>` 或 `--file=<script文件>` 以选项中指定的script文件来处理输入的文本文件。
3. -n：或 --quiet或--silent 仅显示script处理后的结果。
4. -h：或 --help 显示帮助。
5. -V：或 --version 显示版本信息。

### ③、动作说明

1. a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)
2. c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行
3. d ：删除，因为是删除啊，所以 d 后面通常不接任何东西
4. i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)
5. p ：打印，亦即将某个 选择的数据印出。通常 p 会与参数 sed -n 一起运行
6. s ：取代，通常这个 s 的动作可以搭配正则表达式！例如 1,20s/old/new/g

### ④、例子

#### Ⅰ、增：`a`

1. 在第二行后添加一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2a 4 5 yurhai' data
3 2 1
2 2 2
4 5 yurhai
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

2. 在第二行到第六行后添加一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2,6a 4 5 yurhai' data
3 2 1
2 2 2
4 5 yurhai
1 2 3
4 5 yurhai
1 3 3
4 5 yurhai
1 1 1
4 5 yurhai
2 2 2
4 5 yurhai
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

3. 在第二行到最后一行后添加一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2,$a 4 5 yurhai' data
3 2 1
2 2 2
4 5 yurhai
1 2 3
4 5 yurhai
1 3 3
4 5 yurhai
1 1 1
4 5 yurhai
2 2 2
4 5 yurhai
3 3 3
4 5 yurhai
2 4 6
4 5 yurhai
1 4 6
4 5 yurhai
3 2 1
4 5 yurhai
2 1 4
4 5 yurhai
3 3 3
4 5 yurhai
2 1 3
4 5 yurhai
```

#### Ⅱ、删:`d`

1. 删除第二行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2d' data
3 2 1
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

2. 删除第二行到最后一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2,$d' data
3 2 1
```

3. 删除存在 1 的行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed '/1/d' data
2 2 2
2 2 2
3 3 3
2 4 6
3 3 3
```

4. 删除空行

```shell
[trial@localhost cuichangjian]$ sed '/^$/d' data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

#### Ⅲ、改:`c、s`

1. 修改第二行：`c`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2c 02 02 02 yuehai' data
3 2 1
02 02 02 yuehai
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

2. 修改第二行到最后一行：`c`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2,$c 02 02 02 yuehai' data
3 2 1
02 02 02 yuehai
```

3. 根据正则表达式，替换特定的字符；替换第一行：`s`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed '1s/1/01/g' data
3 2 01
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

4. 根据正则表达式，替换特定的字符；替换第三行到八行：`s`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed '3,8s/1/01/g' data
3 2 1
2 2 2
01 2 3
01 3 3
01 01 01
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

5. 根据正则表达式，替换特定的字符；替换全文：`s`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed "s/1/01/g" data
3 2 01
2 2 2
01 2 3
01 3 3
01 01 01
2 2 2
3 3 3
2 4 6
01 4 6
3 2 01
2 01 4
3 3 3
2 01 3
```

#### Ⅳ、插入:`i`

1. 在第二行前添加一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2i 02 02 02 yuehai' data
3 2 1
02 02 02 yuehai
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
```

2. 在第二行到最后一行前添加一行

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ sed -e '2,$i 02 02 02 yuehai' data
3 2 1
02 02 02 yuehai
2 2 2
02 02 02 yuehai
1 2 3
02 02 02 yuehai
1 3 3
02 02 02 yuehai
1 1 1
02 02 02 yuehai
2 2 2
02 02 02 yuehai
3 3 3
02 02 02 yuehai
2 4 6
02 02 02 yuehai
1 4 6
02 02 02 yuehai
3 2 1
02 02 02 yuehai
2 1 4
02 02 02 yuehai
3 3 3
02 02 02 yuehai
2 1 3
```

#### Ⅴ、查

1. 查询出字符 US 和 UK 之间的行数据（有多个相同的数据，会显示最前和最后的两个之间的数据）

```shell
[trial@localhost topic5]$ cat sed_file 
1 JP is japan JP is japan JP is japan JP is japan JP is japan
2 JP is japan
3 JP is japan
4 JP is japan
5 JP is japan
5 JP is japan
6 JP is japan
11 JP is japan JP is japan JP is japan JP is japan JP is japan
21 JP is japan JP is japan JP is japan JP is japan JP is japan
31 JP is japan JP is japan JP is japan JP is japan JP is japan
41 JP is japan JP is japan JP is japan JP is japan JP is japan
USa ,JP is japan
<td>111<</td>
<td>222></td>
<td>333<></td>
<td>444</td>
<td>555</td>
11 JaP is japan JP is japan JP is japan JP is japan JP is japan
21 JaP is japan JP is japan JP is japan JP is japan JP is japan
31 JaP is japan JP is japan JP is japan JP is japan JP is japan
41 JaP is japan JP is japan JP is japan JP is japan JP is japan
UK ,JP is japan

[trial@localhost topic5]$ sed -n ' /US/,/UK/p ' sed_file 
USa ,JP is japan
<td>111<</td>
<td>222></td>
<td>333<></td>
<td>444</td>
<td>555</td>
11 JaP is japan JP is japan JP is japan JP is japan JP is japan
21 JaP is japan JP is japan JP is japan JP is japan JP is japan
31 JaP is japan JP is japan JP is japan JP is japan JP is japan
41 JaP is japan JP is japan JP is japan JP is japan JP is japan
UK ,JP is japan
```

## 6、复杂格式文本处理工具：`awk`

AWK 是一种处理文本文件的语言，是一个强大的文本分析工具

> [https://www.runoob.com/linux/linux-comm-awk.html](https://www.runoob.com/linux/linux-comm-awk.html)

### ①、语法

`awk [选项参数] 'script' var=value file(s) `

 或
 
`awk [选项参数] -f scriptfile var=value file(s)`

---

`awk [选项参数] '要处理的数据{处理方式}' 文件 `

### ②、参数

1. -F fs or --field-separator fs：指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:。
2. -v var=value or --asign var=value：赋值一个用户定义变量。
3. -f scripfile or --file scriptfile：从脚本文件中读取awk命令。
4. -mf nnn and -mr nnn：对nnn值设置内在限制，-mf选项限制分配给nnn的最大块数目；-mr选项限制记录的最大数目。这两个功能是Bell实验室版awk的扩展功能，在标准awk中不适用。
5. -W compact or --compat, -W traditional or --traditional：在兼容模式下运行awk。所以gawk的行为和标准的awk完全一样，所有的awk扩展都被忽略。
6. -W copyleft or --copyleft, -W copyright or --copyright：打印简短的版权信息。
7. -W help or --help, -W usage or --usage：打印全部awk选项和每个选项的简短说明。
8. -W lint or --lint：打印不能向传统unix平台移植的结构的警告。
9. -W lint-old or --lint-old：打印关于不能向传统unix平台移植的结构的警告。
10. -W posix：打开兼容模式。但有以下限制，不识别：/x、函数关键字、func、换码序列以及当fs是一个空格时，将新行作为一个域分隔符；操作符**和**=不能代替^和^=；fflush无效。
11. -W re-interval or --re-interval：允许间隔正则表达式的使用，参考(grep中的Posix字符类)，如括号表达式[[:alpha:]]。
12. -W source program-text or --source program-text：使用program-text作为源代码，可与-f命令混用。
13. -W version or --version：打印bug报告信息的版本。

### ③、运算符

| 运算符 | 描述 |
| --- | --- |
| `= += -= *= /= %= ^= **=` | 赋值 |
| ?: | C条件表达式 |
| &#124;&#124; | 逻辑或 |
| && | 逻辑与 |
| ~ 和 !~ | 匹配正则表达式和不匹配正则表达式 |
| < <= > >= != == | 关系运算符 |
| 空格 | 连接 |
| + - | 加，减 |
| * / % | 乘，除与求余 |
| + - ! | 一元加，减和逻辑非 |
| ^ *** | 求幂 |
| ++ -- | 增加或减少，作为前缀或后缀 |
| $ | 字段引用 |
| in | 数组成员 |

### ④、内建变量

| 变量 | 描述 | 描述2 |
| --- | --- | --- |
| $n | 当前记录的第n个字段，字段间由FS分隔 |  |
| $0 | 完整的输入记录 |  |
| ARGC | 命令行参数的数目 | |
| ARGIND | 命令行中当前文件的位置(从0开始算) | |
| ARGV | 包含命令行参数的数组 | |
| CONVFMT | 数字转换格式(默认值为%.6g)ENVIRON环境变量关联数组 | |
| ERRNO | 最后一个系统错误的描述 | |
| FIELDWIDTHS | 字段宽度列表(用空格键分隔) | |
| FILENAME | 当前文件名 | |
| FNR | 各文件分别计数的行号 | 每个文件不同的行号 |
| FS | 字段分隔符(默认是任何空格) | |
| IGNORECASE | 如果为真，则进行忽略大小写的匹配 | |
| NF | 一条记录的字段的数目 | 列数 |
| NR | 已经读出的记录数，就是行号，从1开始 | 行号 |
| OFMT | 数字的输出格式(默认值是%.6g) | |
| OFS | 输出字段分隔符，默认值与输入字段分隔符一致。 | |
| ORS | 输出记录分隔符(默认值是一个换行符) | |
| RLENGTH | 由match函数所匹配的字符串的长度 | |
| RS | 记录分隔符(默认是一个换行符) | |
| RSTART | 由match函数所匹配的字符串的第一个位置 | |
| SUBSEP | 数组下标分隔符(默认值是/034) | |

### ⑤、例子

1. 匹配第 2 列等于 2 的行；打印全部

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk '$2=="2" {print}' data
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
```

2. 匹配第 2 列等于 2 的行；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk '$2=="2" {print $1,$2,$3,"----",FNR}' data
3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
```

3. 匹配第 3 行；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk 'NR=="3" {print $1,$2,$3,"----",FNR}' data
1 2 3 ---- 3
```

4. 匹配第 3 行；打印出：第 1 列 + 10、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk 'NR==3 {print $1+10,$2,$3,"----",FNR}' data
11 2 3 ---- 3
```

5. 匹配第 3 行；先给第 1 列赋值 100；然后再打印出：第 1 列 + 10、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk 'NR==3 {$1=100; print $1+10,$2,$3,"----",FNR}' data
110 2 3 ---- 3
```

6. 正则表达式：匹配存在 1 的行；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ awk '/[1]/ {print $1,$2,$3,"----",FNR}' data
3 2 1 ---- 1
1 2 3 ---- 3
1 3 3 ---- 4
1 1 1 ---- 5
1 4 6 ---- 9
3 2 1 ---- 10
2 1 4 ---- 11
2 1 3 ---- 13
[trial@smartedu data]$ 
```

7. 正则表达式：匹配第 1 列的数中，范围在 1-2 的数；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk '$1 ~/[1-2]/ {print $1,$2,$3,"----",FNR}' data
2 2 2 ---- 2
1 2 3 ---- 3
1 3 3 ---- 4
1 1 1 ---- 5
2 2 2 ---- 6
2 4 6 ---- 8
1 4 6 ---- 9
2 1 4 ---- 11
2 1 3 ---- 13
```

8. 拓展正则表达式：需添加参数 `--re-interva` ，匹配第一列中有连续两个 1 的数据

```shell
[trial@localhost data]$ cat test_date 
20160110 20160111 20160112 1111
20160113 20160114 20160115 1111
20160116 20160117 20160118 1111
20160119 20160120 20160121 1111
20160122 20160123 20160124 1111
20160125 20160126 20160127 1111
20160128 20160129 20160130 1111
20160131 20160201 20160202 1111
20160203 20160204 20160205 1111
20160206 20160207 20160208 1111
20160209 20160210 20160211 1111
20160212 20160213 20160214 1111
20160215 20160216 20160217 1111
20160218 20160219 20160220 1111
20160221 20160222 20160223 1111
20160224 20160225 20160226 1111
20160227 20160228 20160229 1111
20160301 20160302 20160303 1111
[trial@localhost data]$ awk --re-interval '$1~/[1]{2}/ {print }' test_date 
20160110 20160111 20160112 1111
20160113 20160114 20160115 1111
20160116 20160117 20160118 1111
20160119 20160120 20160121 1111
```

9. 拓展正则表达式：需添加参数 `--re-interva` ，匹配第二列中有连续两个 1 、且第四列中有连续四个 1 的数据

```shell
[trial@localhost data]$ cat test_date 
20160110 20160111 20160112 1111
20160113 20160114 20160115 1111
20160116 20160117 20160118 1111
20160119 20160120 20160121 1111
20160122 20160123 20160124 1111
20160125 20160126 20160127 1111
20160128 20160129 20160130 1111
20160131 20160201 20160202 1111
20160203 20160204 20160205 1111
20160206 20160207 20160208 1111
20160209 20160210 20160211 1111
20160212 20160213 20160214 1111
20160215 20160216 20160217 1111
20160218 20160219 20160220 1111
20160221 20160222 20160223 1111
20160224 20160225 20160226 1111
20160227 20160228 20160229 1111
20160301 20160302 20160303 1111
[trial@localhost data]$ awk --re-interval '$1~/[2]{2}/ && $4~/[1]{4}/ {print }' test_date  
20160122 20160123 20160124 1111
20160221 20160222 20160223 1111
20160224 20160225 20160226 1111
20160227 20160228 20160229 1111
```

10. 筛选指定行区间的数据；筛选出第10行和第20行的所有列的数据

```shell
[trial@localhost topic5]$ cat awk_file 
0003 0010 0008 0007 00000004906137067700 0 1 0 119
0003 0010 0011 0004 00000004907556209214 0 1 0 379
0003 0010 0012 0001 00000004522646681284 0 6 0 948
0003 0010 0012 0001 00000004562126583592 0 1 0 295
0003 0010 0012 0004 00000004522646671209 0 3 0 192
0003 0010 0012 0004 00000004522646672121 0 3 0 297
0003 0010 0012 0004 00000004522646672138 0 2 0 198
0003 0010 0012 0005 00000004522646671216 0 2 0 128
0003 0010 0012 0006 00000004903320567184 0 1 0 1098
0003 0010 0012 0007 00000004580107092666 0 1 0 129
0003 0010 0012 0008 00000004589937277090 0 1 0 299
0003 0010 0012 0008 00000004589937277106 0 1 0 399
0003 0010 0012 0010 00000004903320575981 0 1 0 279
0003 0010 0017 0010 00000004560416660695 0 1 0 99
0003 0010 0017 0010 00000004903206052674 0 1 0 249
0003 0010 0017 0018 00000004987115800014 0 3 0 597
0003 0010 0017 0020 00000004955671310117 0 3 0 687
0003 0010 0017 0020 00000004955671310124 0 1 0 189
0003 0010 0018 0008 00000004580107090815 0 4 0 392
0003 0010 0018 0008 00000004901065846151 0 1 0 199
[trial@localhost topic5]$ awk ' NR>=10 && NR <=20 {print } ' awk_file 
0003 0010 0012 0007 00000004580107092666 0 1 0 129
0003 0010 0012 0008 00000004589937277090 0 1 0 299
0003 0010 0012 0008 00000004589937277106 0 1 0 399
0003 0010 0012 0010 00000004903320575981 0 1 0 279
0003 0010 0017 0010 00000004560416660695 0 1 0 99
0003 0010 0017 0010 00000004903206052674 0 1 0 249
0003 0010 0017 0018 00000004987115800014 0 3 0 597
0003 0010 0017 0020 00000004955671310117 0 3 0 687
0003 0010 0017 0020 00000004955671310124 0 1 0 189
0003 0010 0018 0008 00000004580107090815 0 4 0 392
0003 0010 0018 0008 00000004901065846151 0 1 0 199
```

9. 在最后增加一列；求第 9 列 大于 400 的列，并将 6、7、8、9 列的数据求和放到每列的最后

```shell
[trial@localhost topic5]$ cat awk_file 
0003 0010 0008 0007 00000004906137067700 0 1 0 119
0003 0010 0011 0004 00000004907556209214 0 1 0 379
0003 0010 0012 0001 00000004522646681284 0 6 0 948
0003 0010 0012 0001 00000004562126583592 0 1 0 295
0003 0010 0012 0004 00000004522646671209 0 3 0 192
0003 0010 0012 0004 00000004522646672121 0 3 0 297
0003 0010 0012 0004 00000004522646672138 0 2 0 198
0003 0010 0012 0005 00000004522646671216 0 2 0 128
0003 0010 0012 0006 00000004903320567184 0 1 0 1098
0003 0010 0012 0007 00000004580107092666 0 1 0 129
0003 0010 0012 0008 00000004589937277090 0 1 0 299
0003 0010 0012 0008 00000004589937277106 0 1 0 399
0003 0010 0012 0010 00000004903320575981 0 1 0 279
0003 0010 0017 0010 00000004560416660695 0 1 0 99
0003 0010 0017 0010 00000004903206052674 0 1 0 249
0003 0010 0017 0018 00000004987115800014 0 3 0 597
0003 0010 0017 0020 00000004955671310117 0 3 0 687
0003 0010 0017 0020 00000004955671310124 0 1 0 189
0003 0010 0018 0008 00000004580107090815 0 4 0 392
0003 0010 0018 0008 00000004901065846151 0 1 0 199
[trial@localhost topic5]$ awk '$9>400 {$10 = $6 + $7 + $8 + $9;print } ' awk_file 
0003 0010 0012 0001 00000004522646681284 0 6 0 948 954
0003 0010 0012 0006 00000004903320567184 0 1 0 1098 1099
0003 0010 0017 0018 00000004987115800014 0 3 0 597 600
0003 0010 0017 0020 00000004955671310117 0 3 0 687 690
```

### ⑥、awk 脚本关键词：`BEGIN`、`END`

关于 awk 脚本，我们需要注意两个关键词 BEGIN 和 END

1. BEGIN{ 这里面放的是执行前的语句 }
2. {这里面放的是处理每一行时要执行的语句}
3. END {这里面放的是处理完所有的行后要执行的语句 }

---

1. 例子
   1. 打印：开始运行
   2. 匹配第 2 列等于 2 的行；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号
   3. 打印：运行结束

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk 'BEGIN{print "开始运行"} $2=="2" {print $1,$2,$3,"----",FNR} END{print "运行结束"}' dataa
开始运行
3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
运行结束
```

2. 计算总行数

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk 'BEGIN{num=0} {num=num+1;print $1,$2,$3,"----",FNR,num} END{print "总行数="num}' data
3 2 1 ---- 1 1
2 2 2 ---- 2 2
1 2 3 ---- 3 3
1 3 3 ---- 4 4
1 1 1 ---- 5 5
2 2 2 ---- 6 6
3 3 3 ---- 7 7
2 4 6 ---- 8 8
1 4 6 ---- 9 9
3 2 1 ---- 10 10
2 1 4 ---- 11 11
3 3 3 ---- 12 12
2 1 3 ---- 13 13
总行数=13
```

### ⑦、操作类型

#### Ⅰ、打印输出：`print`、`printf`

##### （1）、print

- 会自动换行

1. 匹配第 2 列等于 2 的行；打印全部

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk '$2=="2" {print}' data
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
```

2. 匹配第 2 列等于 2 的行；打印出：第 1 列、第 2 列、第 3 列、----、各文件分别计数的行号

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk '$2=="2" {print $1,$2,$3,"----",FNR}' data
3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
```

3. 会自动换行

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk 'BEGIN{print "开始运行";print "开始运行"} $2=="2" {print $1,$2,$3,"----",FNR} END{print "运行结束"}' data
开始运行
开始运行
3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
运行结束
```

---

##### （2）、`printf`

![image.png](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2Fattachments%2F2023-07-25-13--14-20-483--AQvHkjA-3psrAw.png)


- 10 进制的整数
   - %5d：长度为 5 （多的不会被删掉），右对齐
   - %-5d：长度为 5（多的不会被删掉），左对齐
   - %05d：长度为 5（多的不会被删掉），不足 5 位 前面用 0 填充

```shell
[trial@localhost cuichangjian]$ selcol -c4 data2
1.15
53.54
3623.13
6.431
40.1312
0.042
1.0242
233.03
3.445
53.21
4.5

[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%5d\n",$1)}'
    1
   53
 3623
    6
   40
    0
    1
  233
    3
   53
    4
		
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%-5d\n",$1)}'
1    
53   
3623 
6    
40   
0    
1    
233  
3    
53   
4    

[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%05d\n",$1)}'
00001
00053
03623
00006
00040
00000
00001
00233
00003
00053
00004
```

   - 同时操作多行；第 1 行补全 10 位 0，第 2 行左对齐

```shell
[trial@localhost cuichangjian]$ selcol -c1 -c4 data2
3 1.15
2 53.54
1 3623.13
1 6.431
1 40.1312
2 0.042
3 1.0242
2 233.03
1 3.445
3 53.21
2 4.5
[trial@localhost cuichangjian]$ selcol -c1 -c4 data2 | awk '{printf("%010d %-5d\n",$1,$2)}'
0000000003 1    
0000000002 53   
0000000001 3623 
0000000001 6    
0000000001 40   
0000000002 0    
0000000003 1    
0000000002 233  
0000000001 3    
0000000003 53   
0000000002 4    
```

- 浮点数（小数）
   - %.2f：小数点后保留 2 位（四舍五入）
   - %6.2f：包括整数位、小数点、小数位在内，总长度为 6（多的不会被删掉），小数点后保留 2 位，小数点对齐
   - %-6.2f：包括整数位、小数点、小数位在内，总长度为 6（多的不会被删掉），小数点后保留 2 位，左对齐
   - %06.2f：包括整数位、小数点、小数位在内，总长度为 6（多的不会被删掉），小数点后保留 2 位，不足 6 位 前面用 0 填充

```shell
[trial@localhost cuichangjian]$ selcol -c4 data2
1.15
53.54
3623.13
6.431
40.1312
0.042
1.0242
233.03
3.445
53.21
4.5
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%.2f\n",$1)}'
1.15
53.54
3623.13
6.43
40.13
0.04
1.02
233.03
3.44
53.21
4.50
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%6.2f\n",$1)}'
  1.15
 53.54
3623.13
  6.43
 40.13
  0.04
  1.02
233.03
  3.44
 53.21
  4.50
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%-6.2f\n",$1)}'
1.15  
53.54 
3623.13
6.43  
40.13 
0.04  
1.02  
233.03
3.44  
53.21 
4.50  
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%06.2f\n",$1)}'
001.15
053.54
3623.13
006.43
040.13
000.04
001.02
233.03
003.44
053.21
004.50
```

- 文字（字符串）
   - %10s：显示 10 个字符（不足 10 个会从最前面补空格，超过 10 个不会变），右对齐
   - %-10s：显示 10 个字符（不足 10 个会从最后面补空格，超过 10 个不会变），左对齐
   - %10.4s：显示 10 个字符（不足 10 个会从最前面补空格），从获取的字符串中截取 4 个显示，右对齐
   - %-10.4s：显示 10 个字符（不足 10 个会从最后面补空格），从获取的字符串中截取 4 个显示，左对齐

```shell
[trial@localhost cuichangjian]$ selcol -c4 data2
1.15
53.54
3623.13
6.431
40.1312
0.042
1.0242
233.03
3.445
53.21
4.5
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%10s\n",$1)}'
      1.15
     53.54
   3623.13
     6.431
   40.1312
     0.042
    1.0242
    233.03
     3.445
     53.21
       4.5
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%-10s\n",$1)}'
1.15      
53.54     
3623.13   
6.431     
40.1312   
0.042     
1.0242    
233.03    
3.445     
53.21     
4.5       
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%10.4s\n",$1)}'
      1.15
      53.5
      3623
      6.43
      40.1
      0.04
      1.02
      233.
      3.44
      53.2
       4.5
[trial@localhost cuichangjian]$ selcol -c4 data2 | awk '{printf("%-10.4s\n",$1)}'
1.15      
53.5      
3623      
6.43      
40.1      
0.04      
1.02      
233.      
3.44      
53.2      
4.5       
```

---

1. 不会自动换行

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk 'BEGIN{printf "开始运行";printf "开始运行"} $2=="2" {print $1,$2,$3,"----",FNR} END{print "运行结束"}' data
开始运行开始运行3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
运行结束
```

2. 手动换行：`\n`

```shell
[trial@localhost cuichangjian]$ ssort -k2 data
1 1 1
2 1 4
2 1 3
3 2 1
2 2 2
1 2 3
2 2 2
3 2 1
1 3 3
3 3 3
3 3 3
2 4 6
1 4 6
[trial@localhost cuichangjian]$ awk 'BEGIN{printf "开始运行\n";printf "开始运行\n"} $2=="2" {print $1,$2,$3,"----",FNR} END{print "运行结束"}' data
开始运行
开始运行
3 2 1 ---- 1
2 2 2 ---- 2
1 2 3 ---- 3
2 2 2 ---- 6
3 2 1 ---- 10
运行结束
```

#### Ⅱ、变量：`变量名=值`

- 计算总行数

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk 'BEGIN{num=0} {num=num+1;print $1,$2,$3,"----",FNR,num} END{print "总行数="num}' data
3 2 1 ---- 1 1
2 2 2 ---- 2 2
1 2 3 ---- 3 3
1 3 3 ---- 4 4
1 1 1 ---- 5 5
2 2 2 ---- 6 6
3 3 3 ---- 7 7
2 4 6 ---- 8 8
1 4 6 ---- 9 9
3 2 1 ---- 10 10
2 1 4 ---- 11 11
3 3 3 ---- 12 12
2 1 3 ---- 13 13
总行数=13
```

#### Ⅲ、判断：`if`

- 以行为单位运行，每行运行一次

1. 判断第 1 列是否等于 2 ，等于就多打印：月海

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk '{ if($1==2){print $1,$2,$3,"----",FNR,"月海"} else{print $1,$2,$3,"----",FNR} }' data
3 2 1 ---- 1
2 2 2 ---- 2 月海
1 2 3 ---- 3
1 3 3 ---- 4
1 1 1 ---- 5
2 2 2 ---- 6 月海
3 3 3 ---- 7
2 4 6 ---- 8 月海
1 4 6 ---- 9
3 2 1 ---- 10
2 1 4 ---- 11 月海
3 3 3 ---- 12
2 1 3 ---- 13 月海
```

2. 判断第 1 列是否等于 1 ，等于就多打印：言；判断第 1 列是否等于 2 ，等于就多打印：羽；否则只打印：月海

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk '{ if($1==1){print $1,$2,$3,"----",FNR,"言"} else if($1==2){print $1,$2,$3,"----",FNR,"羽"} else{print "月海"} }' data
月海
2 2 2 ---- 2 羽
1 2 3 ---- 3 言
1 3 3 ---- 4 言
1 1 1 ---- 5 言
2 2 2 ---- 6 羽
月海
2 4 6 ---- 8 羽
1 4 6 ---- 9 言
月海
2 1 4 ---- 11 羽
月海
2 1 3 ---- 13 羽
```

#### Ⅳ、循环：`for`

- 以行为单位运行，每行运行一次

- 输出列表是：第一列数据,i,列数    第二列数据,i,列数    第三列数据,i,列数    月海

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3

[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf $i","i","NF" "} printf "月海\n"}' data
3,1,3 2,2,3 1,3,3 月海
2,1,3 2,2,3 2,3,3 月海
1,1,3 2,2,3 3,3,3 月海
1,1,3 3,2,3 3,3,3 月海
1,1,3 1,2,3 1,3,3 月海
2,1,3 2,2,3 2,3,3 月海
3,1,3 3,2,3 3,3,3 月海
2,1,3 4,2,3 6,3,3 月海
1,1,3 4,2,3 6,3,3 月海
3,1,3 2,2,3 1,3,3 月海
2,1,3 1,2,3 4,3,3 月海
3,1,3 3,2,3 3,3,3 月海
2,1,3 1,2,3 3,3,3 月海
```

### ⑧、函数

#### Ⅰ、int(f)

语法：`int(f)`

将给定字符串 f 的小数点以下舍去，使其变为为整数

```shell
[trial@localhost cuichangjian]$ cat data2
3 2 1 1.15
2 2 2 53.54
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
2 2 2 0.042
3 3 3 1.0242
2 4 6 233.03
1 4 6 3.445
3 2 1 53.21
2 1 4 4.5
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf $i","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1.15,4,4 月海
2,1,4 2,2,4 2,3,4 53.54,4,4 月海
1,1,4 2,2,4 3,3,4 3623.13,4,4 月海
1,1,4 3,2,4 3,3,4 6.431,4,4 月海
1,1,4 1,2,4 1,3,4 40.1312,4,4 月海
2,1,4 2,2,4 2,3,4 0.042,4,4 月海
3,1,4 3,2,4 3,3,4 1.0242,4,4 月海
2,1,4 4,2,4 6,3,4 233.03,4,4 月海
1,1,4 4,2,4 6,3,4 3.445,4,4 月海
3,1,4 2,2,4 1,3,4 53.21,4,4 月海
2,1,4 1,2,4 4,3,4 4.5,4,4 月海
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf int($i)","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1,4,4 月海
2,1,4 2,2,4 2,3,4 53,4,4 月海
1,1,4 2,2,4 3,3,4 3623,4,4 月海
1,1,4 3,2,4 3,3,4 6,4,4 月海
1,1,4 1,2,4 1,3,4 40,4,4 月海
2,1,4 2,2,4 2,3,4 0,4,4 月海
3,1,4 3,2,4 3,3,4 1,4,4 月海
2,1,4 4,2,4 6,3,4 233,4,4 月海
1,1,4 4,2,4 6,3,4 3,4,4 月海
3,1,4 2,2,4 1,3,4 53,4,4 月海
2,1,4 1,2,4 4,3,4 4,4,4 月海
```

#### Ⅱ、sprintf("format", v1, v2,...)

语法：`sprintf("format", v1, v2,...)`

返回与 printf 函数进行了相同格式转换的字符串

```shell
[trial@localhost cuichangjian]$ cat data2
3 2 1 1.15
2 2 2 53.54
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
2 2 2 0.042
3 3 3 1.0242
2 4 6 233.03
1 4 6 3.445
3 2 1 53.21
2 1 4 4.5
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf $i","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1.15,4,4 月海
2,1,4 2,2,4 2,3,4 53.54,4,4 月海
1,1,4 2,2,4 3,3,4 3623.13,4,4 月海
1,1,4 3,2,4 3,3,4 6.431,4,4 月海
1,1,4 1,2,4 1,3,4 40.1312,4,4 月海
2,1,4 2,2,4 2,3,4 0.042,4,4 月海
3,1,4 3,2,4 3,3,4 1.0242,4,4 月海
2,1,4 4,2,4 6,3,4 233.03,4,4 月海
1,1,4 4,2,4 6,3,4 3.445,4,4 月海
3,1,4 2,2,4 1,3,4 53.21,4,4 月海
2,1,4 1,2,4 4,3,4 4.5,4,4 月海
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf sprintf("%010d",$i)","i","NF" "} printf "月海\n"}' data2
0000000003,1,4 0000000002,2,4 0000000001,3,4 0000000001,4,4 月海
0000000002,1,4 0000000002,2,4 0000000002,3,4 0000000053,4,4 月海
0000000001,1,4 0000000002,2,4 0000000003,3,4 0000003623,4,4 月海
0000000001,1,4 0000000003,2,4 0000000003,3,4 0000000006,4,4 月海
0000000001,1,4 0000000001,2,4 0000000001,3,4 0000000040,4,4 月海
0000000002,1,4 0000000002,2,4 0000000002,3,4 0000000000,4,4 月海
0000000003,1,4 0000000003,2,4 0000000003,3,4 0000000001,4,4 月海
0000000002,1,4 0000000004,2,4 0000000006,3,4 0000000233,4,4 月海
0000000001,1,4 0000000004,2,4 0000000006,3,4 0000000003,4,4 月海
0000000003,1,4 0000000002,2,4 0000000001,3,4 0000000053,4,4 月海
0000000002,1,4 0000000001,2,4 0000000004,3,4 0000000004,4,4 月海
```

#### Ⅲ、substr(s, p, n)

语法：`substr(s, p, n)`

从字符串 s 中的第 p 个字符开始，截取并返回 n 个字符串

```shell
[trial@localhost cuichangjian]$ cat data2
3 2 1 1.15
2 2 2 53.54
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
2 2 2 0.042
3 3 3 1.0242
2 4 6 233.03
1 4 6 3.445
3 2 1 53.21
2 1 4 4.5
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf $i","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1.15,4,4 月海
2,1,4 2,2,4 2,3,4 53.54,4,4 月海
1,1,4 2,2,4 3,3,4 3623.13,4,4 月海
1,1,4 3,2,4 3,3,4 6.431,4,4 月海
1,1,4 1,2,4 1,3,4 40.1312,4,4 月海
2,1,4 2,2,4 2,3,4 0.042,4,4 月海
3,1,4 3,2,4 3,3,4 1.0242,4,4 月海
2,1,4 4,2,4 6,3,4 233.03,4,4 月海
1,1,4 4,2,4 6,3,4 3.445,4,4 月海
3,1,4 2,2,4 1,3,4 53.21,4,4 月海
2,1,4 1,2,4 4,3,4 4.5,4,4 月海
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf substr($i,0,4)","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1.15,4,4 月海
2,1,4 2,2,4 2,3,4 53.5,4,4 月海
1,1,4 2,2,4 3,3,4 3623,4,4 月海
1,1,4 3,2,4 3,3,4 6.43,4,4 月海
1,1,4 1,2,4 1,3,4 40.1,4,4 月海
2,1,4 2,2,4 2,3,4 0.04,4,4 月海
3,1,4 3,2,4 3,3,4 1.02,4,4 月海
2,1,4 4,2,4 6,3,4 233.,4,4 月海
1,1,4 4,2,4 6,3,4 3.44,4,4 月海
3,1,4 2,2,4 1,3,4 53.2,4,4 月海
2,1,4 1,2,4 4,3,4 4.5,4,4 月海
```

#### Ⅳ、length(s)

语法：`length(s)`

返回字符串 s 的长度（字节数）

```shell
[trial@localhost cuichangjian]$ cat data2
3 2 1 1.15
2 2 2 53.54
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
2 2 2 0.042
3 3 3 1.0242
2 4 6 233.03
1 4 6 3.445
3 2 1 53.21
2 1 4 4.5
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf $i","i","NF" "} printf "月海\n"}' data2
3,1,4 2,2,4 1,3,4 1.15,4,4 月海
2,1,4 2,2,4 2,3,4 53.54,4,4 月海
1,1,4 2,2,4 3,3,4 3623.13,4,4 月海
1,1,4 3,2,4 3,3,4 6.431,4,4 月海
1,1,4 1,2,4 1,3,4 40.1312,4,4 月海
2,1,4 2,2,4 2,3,4 0.042,4,4 月海
3,1,4 3,2,4 3,3,4 1.0242,4,4 月海
2,1,4 4,2,4 6,3,4 233.03,4,4 月海
1,1,4 4,2,4 6,3,4 3.445,4,4 月海
3,1,4 2,2,4 1,3,4 53.21,4,4 月海
2,1,4 1,2,4 4,3,4 4.5,4,4 月海
[trial@localhost cuichangjian]$ awk '{for(i=1;i<=NF;i++){ printf length($i)","i","NF" "} printf "月海\n"}' data2
1,1,4 1,2,4 1,3,4 4,4,4 月海
1,1,4 1,2,4 1,3,4 5,4,4 月海
1,1,4 1,2,4 1,3,4 7,4,4 月海
1,1,4 1,2,4 1,3,4 5,4,4 月海
1,1,4 1,2,4 1,3,4 7,4,4 月海
1,1,4 1,2,4 1,3,4 5,4,4 月海
1,1,4 1,2,4 1,3,4 6,4,4 月海
1,1,4 1,2,4 1,3,4 6,4,4 月海
1,1,4 1,2,4 1,3,4 5,4,4 月海
1,1,4 1,2,4 1,3,4 5,4,4 月海
1,1,4 1,2,4 1,3,4 3,4,4 月海
```

### ⑨、三元运算符

- 以行为单位运行，每行运行一次

语法：`条件 ? 条件为真时执行的语句 : 条件为假时执行的语句`

```shell
[trial@localhost cuichangjian]$ cat data
3 2 1
2 2 2
1 2 3
1 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@localhost cuichangjian]$ awk '{ print $1==1 ?  "月海1111" : "yuehai" }' data
yuehai
yuehai
月海1111
月海1111
月海1111
yuehai
yuehai
yuehai
月海1111
yuehai
yuehai
yuehai
yuehai
```

## 7、

# 三、**文件传输**

# 四、**磁盘管理**

## 1、创建文件夹：`mkdir`

### ①、语法

`mkdir 文件夹`

### ②、参数

-p 确保目录名称存在，不存在的就建一个

## 2、显示目录内容：`ls`

### ①、语法

`ls 目录（默认本目录）`

### ②、参数

1. -a 显示所有文件及目录 (. 开头的隐藏文件也会列出)
2. -l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出
3. -r 将文件以相反次序显示(原定依英文字母次序)
4. -t 将文件依建立时间之先后次序列出
5. -A 同 -a ，但不列出 "." (目前目录) 及 ".." (父目录)
6. -F 在列出的文件名称后加一符号；例如可执行档则加 "*", 目录则加 "/"
7. -R 若目录下有文件，则以下之文件亦皆依序列出

## 3、显示目前所在的工作目录的绝对路径：`pwd`

语法：`pwd`

## 4、切换当前工作目录：`cd`

1. 指定目录：`cd 路径`
2. 用户目录：`cd ~`
3. 上一层目录：`cd ../`

## 5、删除空的目录：`rmdir`

### ①、语法

`rmdir 目录`

### ②、参数

-p 当子目录被删除后使它也成为空目录的话，则顺便一并删除。

# 五、磁盘维护

# 六、网络通讯

## 1、确认远端主机网络连接状况：`ping`

Linux ping 命令用于检测主机。

执行 ping 指令会使用 ICMP 传输协议，发出要求回应的信息，若远端主机的网络功能没有问题，就会回应该信息，因而得知该主机运作正常

### ①、语法

`ping 参数 ip地址`

### ②、参数

1. -d 使用Socket的SO_DEBUG功能。
2. -c <完成次数> 设置完成要求回应的次数。
3. -f 极限检测。
4. -i<间隔秒数> 指定收发信息的间隔时间。
5. -I<网络界面> 使用指定的网络接口送出数据包。
6. -l<前置载入> 设置在送出要求信息之前，先行发出的数据包。
7. -n 只输出数值。
8. -p<范本样式> 设置填满数据包的范本样式。
9. -q 不显示指令执行过程，开头和结尾的相关信息除外。
10. -r 忽略普通的Routing Table，直接将数据包送到远端主机上。
11. -R 记录路由过程。
12. -s<数据包大小> 设置数据包的大小。
13. -t<存活数值> 设置存活数值TTL的大小。
14. -v 详细显示指令的执行过程。
15. `-w <deadline>` 在 deadline 秒后退出。
16. `-W <timeout>` 在等待 timeout 秒后开始执行。

## 2、连接远程主机：`ssh`

语法：`ssh 用户名@IP地址`

## 3、

# 七、系统管理

## 1、时间：`date`

### ①、显示当前时间

`date`

### ②、指定时间的显示形式

`date +"%Y-%m-%d"`

### ③、可选参数

| `-d`, --date=STRING | 通过字符串显示时间格式，字符串不能是'now' |
| --- | --- |
| `-f`, --file=DATEFILE | 类似于--date; 一次从DATEFILE处理一行 |
| `-I`[FMT], --iso-8601[=FMT] | 按照 ISO 8601 格式输出时间，FMT 可以为'date'(默认)，'hours'，'minutes'，'seconds'，'ns'。 可用于设置日期和时间的精度，例如：2006-08-14T02:34:56-0600 |
| `-R`, --rfc-2822 | 按照 RFC 5322 格式输出时间和日期，例如: Mon, 14 Aug 2006 02:34:56 -0600 |
| --rfc-3339=FMT | 按照 RFC 3339 格式输出，FMT 可以为'date', 'seconds','ns'中的一个，可用于设置日期和时间的精度， 例如：2006-08-14 02:34:56-06:00 |
| `-r`, --reference=FILE | 显示文件的上次修改时间 |
| `-s`, --set=STRING | 根据字符串设置系统时间 |
| `-u`, --utc, --universal | 显示或设置协调世界时(UTC) |
| --help | 显示帮助信息 |
| --version | 输出版本信息 |

## 2、显示服务器负荷：`top`

Linux top命令用于实时显示 process 的动态

### ①、语法

`top 参数`

### ②、参数

1. d : 改变显示的更新速度，或是在交谈式指令列( interactive command)按 s
2. q : 没有任何延迟的显示速度，如果使用者是有 superuser 的权限，则 top 将会以最高的优先序执行
3. c : 切换显示模式，共有两种模式，一是只显示执行档的名称，另一种是显示完整的路径与名称
4. S : 累积模式，会将己完成或消失的子进程 ( dead child process ) 的 CPU time 累积起来
5. s : 安全模式，将交谈式指令取消, 避免潜在的危机
6. i : 不显示任何闲置 (idle) 或无用 (zombie) 的进程
7. n : 更新的次数，完成后将会退出 top
8. b : 批次档模式，搭配 "n" 参数一起使用，可以用来将 top 的结果输出到档案内

## 3、显示当前进程的状态：`ps`

Linux ps （英文全拼：process status）命令用于显示当前进程的状态，类似于 windows 的任务管理器

### ①、语法

`ps 参数`

### ②、参数

- ps 的参数非常多, 在此仅列出几个常用的参数并大略介绍含义

- -A 列出所有的进程
- -w 显示加宽可以显示较多的资讯
- -au 显示较详细的资讯
- -aux 显示所有包含其他使用者的进程
- au(x) 输出格式 :USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
   - USER: 行程拥有者
   - PID: pid
   - %CPU: 占用的 CPU 使用率
   - %MEM: 占用的记忆体使用率
   - VSZ: 占用的虚拟记忆体大小
   - RSS: 占用的记忆体大小
   - TTY: 终端的次要装置号码 (minor device number of tty)
   - STAT: 该行程的状态:
      - D: 无法中断的休眠状态 (通常 IO 的进程)
      - R: 正在执行中
      - S: 静止状态
      - T: 暂停执行
      - Z: 不存在但暂时无法消除
      - W: 没有足够的记忆体分页可分配
      - <: 高优先序的行程
      - N: 低优先序的行程
      - L: 有记忆体分页分配并锁在记忆体内 (实时系统或捱A I/O)
   - START: 行程开始时间
   - TIME: 执行的时间
   - COMMAND:所执行的指令

## 4、强制结束正在执行的进程：`kill`

Linux kill 命令用于删除执行中的程序或工作。
kill 可将指定的信息送至程序。预设的信息为 SIGTERM(15)，可将指定程序终止。若仍无法终止该程序，可使用 SIGKILL(9) 信息尝试强制删除程序。程序或工作的编号可利用 ps 指令或 jobs 指令查看

### ①、语法

`kill 参数 程序编号`

### ②、参数

1. 1 (HUP)：重新加载进程。
2. 9 (KILL)：杀死一个进程。
3. 15 (TERM)：正常停止一个进程

## 5、

# 八、系统设置

# 九、备份压缩

# 十、设备管理
