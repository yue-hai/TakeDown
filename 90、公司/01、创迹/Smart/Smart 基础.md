# 零、进入练习服务器

## 1、使用 ttermpro 连接服务器

1. 打开 ttermpro
2. 输入 Ip：172.20.2.44
3. 端口号：22

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--16-59-623--bYBmgUXtLpM79w.png) 

## 2、输入账号密码进入

1. 账号：trial
2. 密码：trial1234

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-113--64rv0gJYsqWWPQ.png)

## 3、参数说明

- 此处说明的参数在 smart 中基本通用（也有与此处的说明不同的）

1. -c：指定第几列
2. -k：指定参考的主键
3. -s：指定不加处理的数据
4. -v：取反
5. -n：行数

# 一、数据输出处理

## 1、抽出指定列：`selcol`

**只会抽出并输出数据，不会改变原文件**

### ①、语法

`selcol –c COL1[,COL2]…[FILE]`

1. 抽取一列：`selcol -c 抽取第几列 文件名 `

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
[trial@localhost cuichangjian]$ selcol -c1 data
3
2
1
1
1
2
3
2
1
3
2
```

2. 抽取连续的几列：`selcol -c 抽取的开始列,抽取的结束列 文件名 `

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
[trial@localhost cuichangjian]$ selcol -c1,2 data
3 2
2 2
1 2
1 3
1 1
2 2
3 3
2 4
1 4
3 2
2 1
```

3. 抽取不连续的几列：`selcol -c 抽取的开始列,抽取的结束列 -c 抽取的开始列,抽取的结束列 文件名 `

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
[trial@localhost cuichangjian]$ selcol -c1 -c3 data
3 1
2 2
1 3
1 3
1 1
2 2
3 3
2 6
1 6
3 1
2 4
```

4. 从指定的列到最后一列，可以使用 `NF` 或 `9999`

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
[trial@localhost cuichangjian]$ selcol -c1 data
3
2
1
1
1
2
3
2
1
3
2
[trial@localhost cuichangjian]$ selcol -c1,NF data
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
[trial@localhost cuichangjian]$ selcol -c1,9999 data
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
```

### ②、参数

-c：指定抽取第几列

## 2、删除指定列：`delcol`

**只会抽出并输出数据，不会改变原文件**

### ①、语法

`delcol –c COL1[,COL2]…[FILE]`

1. 删除一列：`delcol -c 删除第几列 文件名 `

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
[trial@localhost cuichangjian]$ delcol -c 1 data
2 1
2 2
2 3
3 3
1 1
2 2
3 3
4 6
4 6
2 1
1 4
```

2. 删除连续的几列：`delcol -c 删除的开始列,删除的结束列 文件名 `

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
[trial@localhost cuichangjian]$ delcol -c1,2 data
1
2
3
3
1
2
3
6
6
1
4
```

3. 删除不连续的几列：`delcol -c 删除的开始列,删除的结束列 -c 删除的开始列,删除的结束列 文件名 `

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
[trial@localhost cuichangjian]$ delcol -c1 -c3 data
2
2
2
3
1
2
3
4
4
2
1
```

### ②、参数

-c：指定删除第几列

## 3、smart 版的排序：`ssort`

1. **按排序关键列对文件进行排序**
2. **多次指定排序关键列时，仅最后的指定有效。**
3. **排序关键列的比较以字节为单位进行大小比较，若想按数字大小排序，最好先补足位数**
4. **根据 UTF-8 的文字代码按依存顺序排序**
5. **只能排128列之前的列，更之后的列想要排要往前移**
6. **选择非连续列时，使用 @**
7. **比 liunx 原生的 sort 速度快**

### ①、语法

`ssort -kCOL1[,COL2] [FILE]`

1. `ssort -k 排序第几列 文件名`：仅对指定的列进行排序
2. `ssort -k 排序的开始列,排序的结束列 文件名`：依据指定的开始结束列进行排序，从前往后，先对第一列进行排序，当第一列大小相同时，再比较第二列，以此类推

```shell
[trial@localhost cuichangjian]$ cat data | ssort -k1
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1  
3 3 3
3 2 1
[trial@localhost cuichangjian]$ cat data | ssort -k1,1
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1  
3 3 3
3 2 1
[trial@localhost cuichangjian]$ cat data | ssort -k1,2
1 1 1
1 2 3
1 3 3
1 4 6
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1  
3 2 1
3 3 3
[trial@localhost cuichangjian]$ cat data | ssort -k1,3
1 1 1
1 2 3
1 3 3
1 4 6
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1  
3 2 1
3 3 3
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
[trial@localhost cuichangjian]$ 
```

3. `ssort -k 2,3@1,1 data`：先根据第 2、3 列进行排列，之后再根据第 1 列进行排列

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
[trial@localhost cuichangjian]$ ssort -k 2,3@1,1 data
1 1 1
2 1 4
3 2 1
3 2 1
2 2 2
2 2 2
1 2 3
1 3 3
3 3 3
1 4 6
2 4 6
```

### ②、参数

- -k ：指定排序关键列

## 4、smart 版的排序（弃用）：`ssort_base`

### ①、语法

`ssort_base -kCOL1[,COL2] [FILE]`

`ssort_base -k 指定开始的列,指定结束的列 文件`

### ②、参数

1. -k：指定排序的列

### ③、说明

1. 数据排序，与 `ssort` 区别是不能指定不连续的 `key` 进行排序
2. 基本不会用到

### ④、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort_base -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort_base -k1,2 data
1 1 1
1 2 3
1 3 3
1 4 6
2 1 4
2 1 3
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3
[trial@smartedu data]$ 
```

## 5、对排序完的数据再按其他列(小范围)排序：`groupsort`

### ①、语法

`roupsort [-r] -s<ソート済みキー> [-k<ソートキー>] [FILE]`
`roupsort [-r] -s指定已经排序的列 [-k指定要排序的列] 文件`

### ②、参数

1. -s：指定已经排序的列
2. -k：指定要排序的列；与 `-s` 指定的列不能相同；不可以使用 `@`
3. -r：根据 `-k` 指定的列进行倒序排序，`-k` 指定的列不会变化

### ③、说明

1. 必须已经排序并指定参数 `-s`
2. `-s` 与 `-k` 指定的列不能相同
3. 快

### ④、案例

1. 第一列已排序，本次排序第 2 列

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupsort -s1 -k2
1 1 1
1 2 3
1 3 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3
[trial@smartedu data]$ 
```

2. 第一列已排序，本次排序第 2、3 列

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupsort -s1 -k2,3
1 1 1
1 2 3
1 3 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3
[trial@smartedu data]$ 
```

3. 第一列已排序，本次排序第 2 列，倒序显示

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupsort -s1 -k2 -r
1 4 6
1 3 3
1 2 3
1 1 1
2 4 6
2 2 2
2 2 2
2 1 4
2 1 3
3 3 3
3 3 3
3 2 1
3 2 1
[trial@smartedu data]$ 
```

## 6、输出第一行：`fstrow`

1. 排序后才可使用此命令
2. 输出相同主键的第一行

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-124--iwXlrJOnuotTOA.png)

### ①、语法

`fstrow –kCOL1[,COL2] [FILE]`

`fstrow –k 开始的主键列,结束的主键列 [FILE]`

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
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | fstrow -k1
1 2 3
2 2 2
3 2 1
```

### ②、参数

-k：指定主键列

## 7、输出最后一行：`lstrow`

1. 排序后才可使用此命令
2. 输出相同主键的最后一行

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-257--WEkHMZ071miKzg.png)

### ①、语法

`lstrow –kCOL1[,COL2] [FILE]`

`lstrow –k 开始的主键列,结束的主键列 [FILE]`

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
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | lstrow -k1
1 4 6
2 1 4
3 2 1
```

### ②、参数

-k：指定主键列

## 8、输出最后一行数值：`lstval`

1. 排序后才可使用此命令
2. 相同主键的最后一行如果是数值，则输出；若是参数 `-N` 指定的字符，则判定为空，不输出，转而输出上一行
3. 与 `lstrow` 类似，不过可以指定输出数值

### ①、语法

`lstval –N<String> –k1[,COL2] [FILE]`

`lstval –N 指定判定为空的字符 –k 1,结束的主键列 [FILE]`

1. 默认判定符号 @ 为空

```shell
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4
1 2 20210301 11
1 2 20210302 12
1 2 20210303 13
1 2 20210304 @
1 3 20210301 11
1 3 20210302 12
1 3 20210303 13
1 3 20210304 _
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4|lstval -k1,2
1 2 20210304 13
1 3 20210304 _
```

2. 指定其他符号为空

```shell
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4
1 2 20210301 11
1 2 20210302 12
1 2 20210303 13
1 2 20210304 @
1 3 20210301 11
1 3 20210302 12
1 3 20210303 13
1 3 20210304 _
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4|lstval -N_ -k1,2
1 2 20210304 @
1 3 20210304 13
```

3. 指定多个

```shell
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4
1 2 20210301 11
1 2 20210302 12
1 2 20210303 13
1 2 20210304 @
1 3 20210301 11
1 3 20210302 12
1 3 20210303 13
1 3 20210304 _
[trial@localhost cuichangjian]$ echo 1 2 20210301 11 1 2 20210302 12 1 2 20210303 13 1 2 20210304 @ 1 3 20210301 11 1 3 20210302 12 1 3 20210303 13 1 3 20210304 _|tov -n4|lstval -N@ -N_ -k1,2
1 2 20210304 13
1 3 20210304 13
```

### ②、参数

1. -k：指定主键列
2. -N：指定判定为空的符号

## 9、输出最后一行指定列相同的数据：`lstblock`

1. 排序后才可使用此命令
2. 使用参数 `-k` 指定主键列，然后使用参数 `-r` 指定比较的列
3. 输出参数 `-r` 指定列的最后一行；与 `lstrow` 不同的是若最后几行的数据相同，则相同的这几行全都输出出来

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-386--RjxR7w_0CaoUHQ.png)

### ①、语法

`lstblock –kCOL1[,COL] –rCOL1[,COL2] [FILE]`
`lstblock –k 开始的主键列,结束的主键列 –r 开始的输出列,结束的输出列 [FILE]`

1. 以最后一行为主键列，比较第三列

```shell
[trial@localhost cuichangjian]$ ssort -k1,3 data
1 1 1
1 2 3
1 3 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3
[trial@localhost cuichangjian]$ ssort -k1,3 data | lstblock -k1 -r3
1 4 6
2 4 6
3 3 3
3 3 3
```

### ②、参数

1. -k：指定主键列
2. -r：指定比较的列

## 10、根据主键去重：`kuniq`

1. 不需要排序也可以使用，出来的数据是自动拍好序的
2. 只会输出指定的主键列

### ①、语法

`kuniq -kCOL1[,COL2] [@COL3] [FILE]`

`kuniq -k 开始的主键列,结束的主键列@不连续的其他主键列 [FILE]`

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
[trial@localhost data]$ kuniq -k1 data
1
2
3
```

### ②、参数

1. -k：指定去重的列

## 11、根据主键去重：`huniq`

#### Ⅰ、语法

`kuniq -kCOL1[,COL2] [@COL3 ] [FILE]`

`kuniq -k 指定开始的主键列,指定结束的主键列 [@指定不连续的主键列 ] 文件`

#### Ⅱ、参数

1. -k：去重的主键列

#### Ⅲ、说明

1. 虽然不需要排序也可以使用，但是不排序出来的数据也是没有排序的
2. 只会输出指定的主键列

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ cat data
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ kuniq -k1 data
1
2
3
5
[trial@smartedu data]$ huniq -k1 data
3
2
1
5
[trial@smartedu data]$ 
```

## 12、文件末尾指定行数删除：`stail`

在文件末尾删除指定的行数

### ①、语法

`stail -nNUM [FILE]`

`stail -n 指定删除的行数 [FILE]`

1. 删除文件最下面的一行、两行

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ stail -n1 master 
1 第一列 2
2 第二列 4
3 第三列 1
[trial@localhost cuichangjian]$ stail -n2 master 
1 第一列 2
2 第二列 4
```

### ②、参数

1. -n：指定删除的行数

## 13、筛选指定条件的列：`selrow`

### ①、语法

`selrow -e exp [FILE]
`
`selrow -e 筛选条件 文件`

### ②、参数

1. -e：筛选条件

### ③、说明

1. 功能和 `awk` 类似，但是功能单一，只能筛选符合条件的数据
2. `$1` 代表第一列；`$1>2`即为筛选第 1 列大于 2 的数
3. 可以是 `>、<、>=、<=、!=、==`
4. 快

### ④、案例

1. 输出第一列大于 2 的行

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ selrow -e '$1>2' data
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ 
```

2. 输出第一列大于等于 2 的行

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ selrow -e '$1>=2' data
3 2 1
2 2 2
2 2 2
3 3 3
2 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ 
```

## 14、截取列字符串：`substr`

指定列数，来截取列中指定长度的字符串
包括指定的开始的字符串，如 `substr -c 2.3.2`：截取第二列的数据，从第三个字符开始（包括第三个），截取两个字符

### ①、语法

`substr -c COL.START[.LENGTH]... [FILE]`

1. 截取一列：`selcol -c 第几列.从第几个字符开始.到第几个字符结束 文件名 `，不指定到第几个字符结束的话，就到本列的结尾

```shell
[trial@localhost data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ cat master | substr -c 2.1.2
1 第一 2
2 第二 4
3 第三 1
4 第四 5
[trial@localhost data]$ cat master | substr -c 2.1.1
1 第 2
2 第 4
3 第 1
4 第 5
```

2. 截取几列：`selcol -c 第几列.从第几个字符开始.到第几个字符结束 -c 第几列.从第几个字符开始.到第几个字符结束 文件名 `，不指定同样到每列的结尾

### ②、参数

-c：指定截取第几列

## 15、

## 16、

## 17、查找文件中的字符串：`grep`

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

## 18、分割文本文件：`fsplit`

1. 排序后才可使用此命令，且排序的主键列要和输出的主键列相同
2. 根据指定的主键列来分割文本文件，主键列中相同主键的数据会被放到一个文件中

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-586--Fxwan7i_6oOCtw.png)

### ①、语法

`fsplit [-a] NEWPATH.%c [FILE]`
`fsplit 追加到目标文件 生成的文件.%指定分割依据的列 [FILE]`

1. 使用 `%` 指定分割的主键列

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | fsplit ./new/newdata.%1
[trial@localhost cuichangjian]$ ll ./new
total 12
-rw-rw-r-- 1 trial trial 24 Aug  5 16:49 newdata.1
-rw-rw-r-- 1 trial trial 30 Aug  5 16:49 newdata.2
-rw-rw-r-- 1 trial trial 24 Aug  5 16:49 newdata.3
[trial@localhost cuichangjian]$ cat ./new/newdata.1
1 2 3
1 3 3
1 1 1
1 4 6
[trial@localhost cuichangjian]$ cat ./new/newdata.2
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
```

2. 去掉分割主键列并保存

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | fsplit -d ./new/newdata.%1
[trial@localhost cuichangjian]$ ll ./new
total 12
-rw-rw-r-- 1 trial trial 16 Aug  5 16:52 newdata.1
-rw-rw-r-- 1 trial trial 20 Aug  5 16:52 newdata.2
-rw-rw-r-- 1 trial trial 16 Aug  5 16:52 newdata.3
[trial@localhost cuichangjian]$ cat ./new/newdata.1
2 3
3 3
1 1
4 6
[trial@localhost cuichangjian]$ cat ./new/newdata.2
2 2
2 2
4 6
1 4
1 3
```

3. 压缩并保存

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | fsplit -z ./new/newdata.%1.gz
[trial@localhost cuichangjian]$ ll ./new
total 24
-rw-rw-r-- 1 trial trial 44 Aug  5 16:53 newdata.1
-rw-rw-r-- 1 trial trial 44 Aug  5 16:54 newdata.1.gz
-rw-rw-r-- 1 trial trial 44 Aug  5 16:53 newdata.2
-rw-rw-r-- 1 trial trial 44 Aug  5 16:54 newdata.2.gz
-rw-rw-r-- 1 trial trial 35 Aug  5 16:53 newdata.3
-rw-rw-r-- 1 trial trial 35 Aug  5 16:54 newdata.3.gz
[trial@localhost cuichangjian]$ zcat ./new/newdata.1.gz
1 2 3
1 3 3
1 1 1
1 4 6
[trial@localhost cuichangjian]$ zcat ./new/newdata.2.gz
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
```

4. 将分割后的数据追加到相应文件中

```shell
[trial@localhost cuichangjian]$ cat ./new/newdata.1
1 2 3
1 3 3
1 1 1
1 4 6
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | fsplit -a ./new/newdata.%1
[trial@localhost cuichangjian]$ ll ./new
total 24
-rw-rw-r-- 1 trial trial 48 Aug  5 16:58 newdata.1
-rw-rw-r-- 1 trial trial 44 Aug  5 16:54 newdata.1.gz
-rw-rw-r-- 1 trial trial 60 Aug  5 16:58 newdata.2
-rw-rw-r-- 1 trial trial 44 Aug  5 16:54 newdata.2.gz
-rw-rw-r-- 1 trial trial 48 Aug  5 16:58 newdata.3
-rw-rw-r-- 1 trial trial 35 Aug  5 16:54 newdata.3.gz
[trial@localhost cuichangjian]$ cat ./new/newdata.1
1 2 3
1 3 3
1 1 1
1 4 6
1 2 3
1 3 3
1 1 1
1 4 6
[trial@localhost cuichangjian]$ cat ./new/newdata.2
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
```

5. 指定多个主键列（都可以指定多个）
   1. 使用第一个主键列创建目录，第二个主键列创建文件

```shell
[trial@localhost cuichangjian]$ ssort -k1,3 data
1 1 1
1 2 3
1 3 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3

[trial@localhost cuichangjian]$ ssort -k1,3 data | fsplit -a ./new/%1/newdata.%2

[trial@localhost cuichangjian]$ ll ./new
total 12
drwxrwxr-x 2 trial trial 4096 Aug  9 14:13 1
drwxrwxr-x 2 trial trial 4096 Aug  9 14:13 2
drwxrwxr-x 2 trial trial 4096 Aug  9 14:13 3

[trial@localhost cuichangjian]$ ll ./new/1
total 16
-rw-rw-r-- 1 trial trial 6 Aug  9 14:13 newdata.1
-rw-rw-r-- 1 trial trial 6 Aug  9 14:13 newdata.2
-rw-rw-r-- 1 trial trial 6 Aug  9 14:13 newdata.3
-rw-rw-r-- 1 trial trial 6 Aug  9 14:13 newdata.4
[trial@localhost cuichangjian]$ cat ./new/1/newdata.1
1 1 1
[trial@localhost cuichangjian]$ cat ./new/1/newdata.2
1 2 3

[trial@localhost cuichangjian]$ ll ./new/2
total 12
-rw-rw-r-- 1 trial trial 12 Aug  9 14:13 newdata.1
-rw-rw-r-- 1 trial trial 12 Aug  9 14:13 newdata.2
-rw-rw-r-- 1 trial trial  6 Aug  9 14:13 newdata.4
[trial@localhost cuichangjian]$ cat ./new/2/newdata.2
2 2 2
2 2 2
```

   2. 使用主键列拼接文件名创建文件

```shell
[trial@localhost cuichangjian]$ ssort -k1,3 data
1 1 1
1 2 3
1 3 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3

[trial@localhost cuichangjian]$ ssort -k1,3 data | fsplit -a ./new/newdata.%1----%2

[trial@localhost cuichangjian]$ ll ./new
total 36
-rw-rw-r-- 1 trial trial  6 Aug  9 14:19 newdata.1----1
-rw-rw-r-- 1 trial trial  6 Aug  9 14:19 newdata.1----2
-rw-rw-r-- 1 trial trial  6 Aug  9 14:19 newdata.1----3
-rw-rw-r-- 1 trial trial  6 Aug  9 14:19 newdata.1----4
-rw-rw-r-- 1 trial trial 12 Aug  9 14:19 newdata.2----1
-rw-rw-r-- 1 trial trial 12 Aug  9 14:19 newdata.2----2
-rw-rw-r-- 1 trial trial  6 Aug  9 14:19 newdata.2----4
-rw-rw-r-- 1 trial trial 12 Aug  9 14:19 newdata.3----2
-rw-rw-r-- 1 trial trial 12 Aug  9 14:19 newdata.3----3
[trial@localhost cuichangjian]$ cat ./new/newdata.1----1
1 1 1
[trial@localhost cuichangjian]$ cat ./new/newdata.2----2
2 2 2
2 2 2
```

### ②、参数

1. -a：不加此参数为覆盖文件，添加此参数为追加到文件最后
2. -d：去掉分割的主键列
3. -z：生成压缩文件，但是生成的文件名的后缀 `.gz`要自己添加

## 19、比较：`head、tail、stail`

1. head：查看开头
   1. 默认查看开头 10 行

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
[trial@localhost cuichangjian]$ head data
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
```

   2. 指定行数：正数（或不加符号），则为从开头开始算，到指定的行数

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
[trial@localhost cuichangjian]$ head -n1 data
3 2 1
```

   3. 指定行数：负数，则为从结尾开始算，去掉指定的行数，显示剩余的数据

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
[trial@localhost cuichangjian]$ head -n-1 data
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
```

2. tail：查看结尾
   1. 默认查看结尾 10 行

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
[trial@localhost cuichangjian]$ tail data
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

   2. 指定行数：正数，则为从开头开始算，从指定的行数开始显示

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
[trial@localhost cuichangjian]$ tail -n+1 data
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
[trial@localhost cuichangjian]$ tail -n+5 data
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

   3. 指定行数：负数（或不加符号），则为从结尾开始算，到指定的行数

```shell
[trial@localhost cuichangjian]$ tail data
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
[trial@localhost cuichangjian]$ tail -n1 data
2 1 3
```

3. stail：删除结尾
   1. 默认不删除
   2. 指定的行数不能有符号，不论正负

```shell
[trial@localhost cuichangjian]$ stail data
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
[trial@localhost cuichangjian]$ stail -n1 data
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
[trial@localhost cuichangjian]$ stail -n+1 data
stail: 数値以外の文字(=+ : 2文字目)が入力されました。 input=+1
Try `stail --help' for more information.
[trial@localhost cuichangjian]$ stail -n-1 data
stail: 数値以外の文字(=- : 2文字目)が入力されました。 input=-1
Try `stail --help' for more information.
[trial@localhost cuichangjian]$ 
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-823--ufZ6BXZGoyBT0Q.png)

## 20、将文件转换为SMART文本：`cln`

有很多功能，如：转换CSV文件、自动去引号、去掉指定字符、去掉多余空格

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-00-919--xbydyyQ-R3fI8Q.png)

### ①、语法

`cln -d<c> [–csv] [*FILE]`

1. 自动去引号

```shell
[trial@tfs tmp]$ echo "10,20,30"|cln
10,20,30
```

2. 去掉指定字符（将字符变为空格）

```shell
[trial@tfs tmp]$ echo "10,20,30"|cln -d,
10 20 30
```

3. 去掉多个指定字符（将字符变为空格）

```shell
[trial@localhost cuichangjian]$ echo "10,20,30@01-5" | cln -d, | cln -d@ | cln -d- | tov
10
20
30
01
5
```

4. 自动去掉多余空格（将多个空格变为一个）

```shell
[trial@localhost data]$ echo "10       20      30" | cln
10 20 30
```

5. 转换 CSV 文件；CSV 文件以逗号 `,` 区分列，SMART 文本以空格 ` ` 区分列；所以本质应该是把逗号 `,` 变为空格 ` ` （不建议使用，建议使用 `csv_test`）

```shell
[trial@tfs tmp]$ echo "10,20,30"|cln --csv
10 20 30
```

### ②、参数

1. -d：指定去除的字符
2. --csv：转换CSV文件

# 二、数据运算

## 1、计算行数：`rowc`

计算文件中的总行数（横着的）
语法： `rowc [FILE]`

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
[trial@localhost data]$ rowc data
13
```

## 2、计算列数：`colc`

计算文件中的总列数（竖着的）
语法： `colc [FILE]`

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
[trial@localhost data]$ colc data
3
```

## 3、纵向求和：`sumup`

1. 排序后才可使用此命令
2. 根据指定的列数，来对每列的数据进行求和
3. 若是指定主键列，则会对主键列去重，然后根据主键列对其后指定的行数进行求和
4. 只会显示指定的主键列和求和的结果，不会显示原始数据
5. 若是指定最后一列求和，可以指定参数 -c 为 NF 或者 9999

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-052--mIdUkRwTnHPw1A.png)

### ①、语法 

`sumup [-n] [-kCOL1[,COL2]] -cCOL1[,COL2] [FILE]`

1. 单纯对一列进行求和：`ssort -k 排序第几列 data | sumup -c 求和第几列`
2. 对指定的连续的每一列进行求和：`ssort -k 排序第几列 data | sumup -c 求和开始的列数,求和结束的列数`

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | sumup -c1
21
[trial@localhost cuichangjian]$ ssort -k1 data | sumup -c1,3
21 26 32
```

3. 根据主键列来求和：`ssort -k 排序第几列 data | sumup -k 主键是第几列 -c 求和开始的列数,求和结束的列数`，结果第一列是去重的主键列，后面是主键列所对应的每列的行的和

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | sumup -k1 -c1,3
1 4 10 13
2 8 9 14
3 9 7 5
```

### ②、参数

1. -k：指定主键列，如果多次指定，则仅最后一个指定有效
2. -c：指定求和的列，如果多次指定，则仅最后一个指定有效
3. -n：将主键列的个数在主键列之后（第二列）打印出来

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-149--Q_w1fcRn1-eKLQ.png)

## 4、横向求和：`hsum`

1. 不排序也可以使用
2. 根据指定的列数，来对每行的数据进行求和，结果放在每行的最后

### ①、语法

`hsum –v -cCOL1[,COL2]... [FILE]`
`hsum 是否选择不求和的列 -c 求和开始列,求和结束列 ... [FILE]`

1. 对连续列求和：`hsum -c1,2 data`

```shell
[trial@localhost cuichangjian]$ hsum -c1,2 data
3 2 1 5
2 2 2 4
1 2 3 3
1 3 3 4
1 1 1 2
2 2 2 4
3 3 3 6
2 4 6 6
1 4 6 5
3 2 1 5
2 1 4 3
```

2. 对不连续列求和：`hsum -c1 -c3 data`

```shell
[trial@localhost cuichangjian]$ hsum -c1 -c3 data
3 2 1 4
2 2 2 4
1 2 3 4
1 3 3 4
1 1 1 2
2 2 2 4
3 3 3 6
2 4 6 8
1 4 6 7
3 2 1 4
2 1 4 6
```

### ②、参数

1. -c：指定求和的列
2. -v：取反；将 -c 选择的列变为不对其进行求和的列，并对其他接进行求和

## 5、总合计：`total`

1. 不排序也可以使用
2. 计算每一列的总和
3. 必须使用 -s 指定不进行合计的行

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-277--IulIsWEt5EuUJQ.png)

### ①、语法
`total -sCOL1[,COL2] -cCOL1[,COL2] [FILE]`
`subtotal -s 忽略开始列数,忽略结束列数 -c 合计开始列数,合计结束列数 文件`

```shell
[trial@localhost cuichangjian]$ total -s1 -c1,3 data
3 3 2 1
2 2 2 2
1 1 2 3
1 1 3 3
1 1 1 1
2 2 2 2
3 3 3 3
2 2 4 6
1 1 4 6
3 3 2 1
2 2 1 4
@ 21 26 32
```

### ②、参数

1. -s：指定忽略（不参与合计）的列
2. -c：指定参与合计的列

## 6、分组合计：`subtotal`

1. 排序后才可使用此命令，且排序的主键列要和求和的主键列相同
2. 必须使用 `-s` 指定不进行合计的行，可以不指定主键列
3. 根据指定的主键列，来对主键列相同的每行数据进行求和，在每个主键列的下面一行输出指定的每行的总和
4. 不被 `-k、-s、-c` 指定的列不会显示

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-433--FAGB4qQanNUfZw.png)

### ①、语法

`subtotal -kCOL1[,COL2] -sCOL1[,COL2] -cCOL1[,COL2] [FILE]`
`ssort -k 排序第几列 文件 | subtotal -k 主键开始列数,主键结束列数 -s 忽略开始列数,忽略结束列数 -c 合计开始列数,合计结束列数 文件`

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | subtotal -k1 -s1 -c2,3
1 1 2 3
1 1 3 3
1 1 1 1
1 1 4 6
1 @ 10 13
2 2 2 2
2 2 2 2
2 2 4 6
2 2 1 4
2 @ 9 14
3 3 2 1
3 3 3 3
3 3 2 1
3 @ 7 5
```

### ②、参数

1. -k：指定主键列（显示的主键列）
2. -s：指定忽略（不参与合计，带 @ 符号）的列
3. -c：指定参与合计的列

## 7、计算累积和：`addup`

1. 在指定列的后面添加一列，计算从本列的顶部到每一行的累积和
2. 若是指定主键列，则必须排序，且指定的主键列要和排序的主键列相同；此时的累积和则是每个主键列单独计算
3. 累积和会每一行相加、逐渐增大

### ①、语法

`addup [-kCOL1[,COL2]] -cCOL1[,COL2] [FILE]`
`addup [-k 主键列开始,主键列结束]] -c 计算列开始,计算列结束 [FILE]`

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
[trial@localhost cuichangjian]$ addup -c3 data
3 2 1 1
2 2 2 3
1 2 3 6
1 3 3 9
1 1 1 10
2 2 2 12
3 3 3 15
2 4 6 21
1 4 6 27
3 2 1 28
2 1 4 32
[trial@localhost cuichangjian]$ ssort -k1 data | addup -k1 -c3
1 2 3 3
1 3 3 6
1 1 1 7
1 4 6 13
2 2 2 2
2 2 2 4
2 4 6 10
2 1 4 14
3 2 1 1
3 3 3 4
3 2 1 5
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-592--Db95wTjgXimK4w.png)

### ②、参数

1. -c：指定计算累积和的列
2. -k：指定主键列

## 8、计算指定键的个数：`kcount`

1. 根据指定的列计算其个数
2. 排序后才可正常使用

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-01-749--wtFrQXamlE9RZA.png)

### ①、语法

`kcount -kCOL1[,COL2] [FILE]`
`kcount -k 开始的列数,结束的列数 [FILE]`

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
[trial@localhost cuichangjian]$ ssort -k1 data | kcount -k1
1 4
2 4
3 3
```

### ②、参数

-k：指定主键列

## 9、对小数四舍五入：`round`

可以使用参数 `-t` 对指定的列进行不同类型的四舍五入

1. `-tA` ： 正常的四舍五入
2. `-tB` ： 只要大于 0 ，就进位
3. `-tC` ： 不论是几，都不进位

### ①、语法

`round -tMODE -cCOL.PRECISION... [FILE]`
`round -t A或B或C -c 第几列.保留几位小数... [FILE]`

1. 正常的四舍五入

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
[trial@localhost cuichangjian]$ round -tA -c1.0 -c2.1 -c4.2 data2
3 2.0 1 1.15
2 2.0 2 53.54
1 2.0 3 3623.13
1 3.0 3 6.43
1 1.0 1 40.13
2 2.0 2 0.04
3 3.0 3 1.02
2 4.0 6 233.03
1 4.0 6 3.45
3 2.0 1 53.21
2 1.0 4 4.50
```

2. 只要大于 0 ，就进位

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
[trial@localhost cuichangjian]$ round -tB -c2.1 -c4.2 data2
3 2.0 1 1.15
2 2.0 2 53.54
1 2.0 3 3623.13
1 3.0 3 6.44
1 1.0 1 40.14
2 2.0 2 0.05
3 3.0 3 1.03
2 4.0 6 233.03
1 4.0 6 3.45
3 2.0 1 53.21
2 1.0 4 4.50
```

3. 不论是几，都不进位

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
[trial@localhost cuichangjian]$ round -tC -c2.1 -c4.2 data2
3 2.0 1 1.15
2 2.0 2 53.54
1 2.0 3 3623.13
1 3.0 3 6.43
1 1.0 1 40.13
2 2.0 2 0.04
3 3.0 3 1.02
2 4.0 6 233.03
1 4.0 6 3.44
3 2.0 1 53.21
2 1.0 4 4.50
```

### ②、参数

1. -c：指定四舍五入的列
   1. `-c1.0`：对第一列进行四舍五入，保留一位小数
   2. `-c2.3`：对第二列进行四舍五入，保留三位小数
2. -t：指定四舍五入的规则
   1. `-tA`：正常的四舍五入
   2. `-tB`：只要大于 0 ，就进位
   3. `-tC`：不论是几，都不进位

## 10、对小数四舍五入：`round_lm`

和上面的 `round` 一样

## 11、平均/最大/最小/总计：`groupby`

### ①、语法

`groupby [-n] [-kCOL1[,COL2]] -cCOL1[,COL2].XXX [FILE]`
`groupby [主键列的行数] [-k 指定开始的主键列,指定结束的主键列] -c 指定开始的列,指定结束的列.计算方法 文件`

### ②、参数

1. -k：指定主键列，必须已排序才可正常使用；指定主键列才会显示主键列
2. -c：指定进行处理的列；处理方式的命令必须大写
   1. SUM：总计
   2. MAX：最大值
   3. MIN：最小值
   4. AVG：平均（保留 4 位小数）
3. -n：是否在主键列后显示主键列的行数；不指定此参数默认不显示

### ③、说明

1. 必须排序才可正常使用
2. 非数字会被识别为 0
3. 一般使用命令 `groupby2` 而不使用此命令

### ④、案例

1. 求第 2 列总计、第 3 列平均值

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupby -n -k1 -c2.SUM -c3.AVG
1 4 10 3.2500
2 5 10 3.4000
3 4 10 2.0000
[trial@smartedu data]$ 
```

2. 求第 2 列最大值、第 3 列最小值

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupby -n -k1 -c2.MAX -c3.MIN
1 4 4 1
2 5 4 2
3 4 3 1
[trial@smartedu data]$ 
```

3. 求第 2 列总计，且不使用参数 `-n` 

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupby -k1 -c2.SUM
1 10
2 10
3 10
[trial@smartedu data]$ 
```

4. 求第 2 列总计，且不使用参数 `-n` 、不指定主键列

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupby -c2.SUM
30
[trial@smartedu data]$ 
```

## 12、平均/最大/最小/总计/个数/中间值：`groupby2
`
### ①、语法

`groupby2 [-n] [-k <キー開始列,[キー終了列]>] -c<開始列,[終了列]>.<計算方法> [FILE]`
`groupby2 [主键列的行数] [-k 指定开始的主键列,指定结束的主键列] -c<指定开始的列,指定结束的列.计算方法 文件`

### ②、参数

1. -k：指定主键列，必须已排序才可正常使用；指定主键列才会显示主键列
2. -c：指定进行处理的列；处理方式的命令必须大写
   1. SUM：总计
   2. MAX：最大值
   3. MIN：最小值
   4. AVG：平均（保留 4 位小数）
   5. MID：中间数
   6. UCT：指定列去重后的个数
3. -n：是否在主键列后显示主键列的行数；不指定此参数默认不显示

### ③、说明

1. `groupby2` 比 `groupby` 多了两个计算方法：`MID、UCT`，除此之外没有别的区别
2. 一般使用此命令

### ④、案例

1. 求第 2 列的中间数、求第 3 列重后的个数

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@smartedu data]$ ssort -k1 data | groupby2 -k1 -c2.MID -c3.UCT
1 2.5 3
2 2 4
3 2.5 2
[trial@smartedu data]$ 
```

## 13、将数字除以 1000 ：`divk`

1. 将指定列除以 1000
2. 默认对文件进行不保留小数的四舍五入；使用参数 `-s` 可保留小数

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-004--B9Fjh2JWrht9Sg.png)

### ①、语法

`divk -s -cCOL1[,COL2]… [FILE]`
`divk 保留小数 -c 开始的列,结束的列 … [FILE]`

1. 默认

```shell
[trial@localhost cuichangjian]$ cat data3
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
[trial@localhost cuichangjian]$ cat data3 | cln -d" "
321222
123133
111222
333246
146321
214333
213326
[trial@localhost cuichangjian]$ cat data3 | cln -d" " | divk -c1
321
123
111
333
146
214
213
```

2. 保留小数

```shell
[trial@localhost cuichangjian]$ cat data3
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
[trial@localhost cuichangjian]$ cat data3 | cln -d" "
321222
123133
111222
333246
146321
214333
213326
[trial@localhost cuichangjian]$ cat data3 | cln -d" " | divk -s -c1
321.222
123.133
111.222
333.246
146.321
214.333
213.326
```

### ②、参数

1. -c：指定除以 1000 的列
2. -s：保留小数

## 14、高精度计算：`scalc`

### ①、语法

`scalc <script> --divzero[=<string>] --overflow[=<string>] <files>...`
`scalc '计算方式' --divzero[=<除数为 0 （计算出错）时显示的字符>] --overflow[=<溢出时显示的字符>] 文件...`

### ②、参数

1. `--divzero=""`：除数为 0 （计算出错）时显示的字符
2. `--overflow=""`：溢出时显示的字符

### ③、说明

1. 计算上限为：整数 18 位 + 小数 18 位
2. 比 `awk` 快

### ④、案例

1. 使第 1 列数据乘 10

```shell
[trial@smartedu data]$ cat data
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
20 20
[trial@smartedu data]$ scalc '$1*10' data
30
20
10
10
10
20
30
20
10
30
20
30
20
[trial@smartedu data]$ 

```

2. 使第 1 列乘第 2 列 

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc '$1*$2' data
6
4
2
3
1
4
9
8
4
6
2
9
2
[trial@smartedu data]$ 
```

3. 第 1 列加第 2 列 ，第 2 列减第 3 列 

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc '$1 + $2,$2 - $3' data
5 1
4 0
3 -1
4 0
2 0
4 0
6 0
6 -2
5 -2
5 1
3 -3
6 0
3 -2
[trial@smartedu data]$ 
```

4. 第 1 列除以第 2 列 ，第 2 列除以 0； 被除数为0 时，不指定参数 `--divzero` 时默认显示 0

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc '$1 / $2,$2 / 0' data
1.500000000000000000 0
1 0
0.500000000000000000 0
0.333333333333333333 0
1 0
1 0
1 0
0.500000000000000000 0
0.250000000000000000 0
1.500000000000000000 0
2 0
1 0
2 0
[trial@smartedu data]$ 
```

5. 第 1 列除以第 2 列 ，第 2 列除以 0； 被除数为0 时，指定参数 `--divzero` 时显示指定的字符串

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc --divzero="**" '$1 / $2,$2 / 0' data
1.500000000000000000 ** **
1 ** **
0.500000000000000000 ** **
0.333333333333333333 ** **
1 ** **
1 ** **
1 ** **
0.500000000000000000 ** **
0.250000000000000000 ** **
1.500000000000000000 ** **
2 ** **
1 ** **
2 ** **
[trial@smartedu data]$ 
```

6. 第 1 列乘第 2 列 ，第 2 列乘 `9999999999999999999999`； 计算溢出时，不指定参数 `--divzero` 时会报错

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc '$1*2,$3 * 9999999999999999999999' data
6 Error[scalc] : オーバーフローが発生しました。
[trial@smartedu data]$ 
```

7. 第 3 列乘 `9999999999999999999999`；计算溢出时，指定参数 `--divzero` 时显示指定的字符串

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc --overflow="@@@" '$3 * 9999999999999999999999' data
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
@@@
[trial@smartedu data]$ 
```

8. 第 3 列乘 `9999999999999999999999`，第 1 列乘第 2 列；计算溢出时，指定参数 `--divzero` 时显示指定的字符串；只在计算列位置显示一列

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc --overflow="@@@" '$3 * 9999999999999999999999,$1*$2' data
@@@ 6
@@@ 4
@@@ 2
@@@ 3
@@@ 1
@@@ 4
@@@ 9
@@@ 8
@@@ 4
@@@ 6
@@@ 2
@@@ 9
@@@ 2
[trial@smartedu data]$ 
```

9. 第 1 列乘第 2 列，第 3 列乘 `9999999999999999999999`，第 1 列乘第 2 列；计算溢出时，指定参数 `--divzero` 时显示指定的字符串；会在计算列位置显示两列

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ scalc --overflow="@@@" '$1*$2,$3 * 9999999999999999999999,$1*$2' data
6 @@@ @@@ 6
4 @@@ @@@ 4
2 @@@ @@@ 2
3 @@@ @@@ 3
1 @@@ @@@ 1
4 @@@ @@@ 4
9 @@@ @@@ 9
8 @@@ @@@ 8
4 @@@ @@@ 4
6 @@@ @@@ 6
2 @@@ @@@ 2
9 @@@ @@@ 9
2 @@@ @@@ 2
[trial@smartedu data]$ 
```

## 15、查找文件中的字符串：`grep`

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
   1. 查找有一个 1 的行

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
[trial@localhost data]$ grep -E '1{1}' data
3 2 1
1 2 3
1 3 3
1 1 1
1 4 6
3 2 1
2 1 4
2 1 3
[trial@localhost data]$ 
```

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

## 16、用脚本来处理文本文件：`sed`

1. Linux sed 命令是利用脚本来处理文本文件
2. sed 可依照脚本的指令来处理、编辑文本文件
3. sed 主要用来自动编辑一个或多个文件、简化对文件的反复操作、编写转换程序等
4. 注意要使用单引号：`''`

### ①、语法

`sed [-hnV][-e<script>][-f<script文件>][文本文件]`

### ②、参数

1. -e：`<script>`或 `--expression=<script>` 以选项中指定的script来处理输入的文本文件。
2. -f：`<script文件>`或 `--file=<script文件>` 以选项中指定的script文件来处理输入的文本文件。
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

## 17、复杂格式文本处理工具：`awk`

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

| 运算符                  | 描述                             |
| ----------------------- | -------------------------------- |
| `= += -= *= /= %= ^= **=` | 赋值                             |
| ?:                      | C条件表达式                      |
| &#124;&#124;            | 逻辑或                           |
| &&                      | 逻辑与                           |
| ~ 和 !~                 | 匹配正则表达式和不匹配正则表达式 |
| < <= > >= != ==         | 关系运算符                       |
| 空格                    | 连接                             |
| + -                     | 加，减                           |
| * / %                   | 乘，除与求余                     |
| + - !                   | 一元加，减和逻辑非               |
| ^ ***                   | 求幂                             |
| ++ --                   | 增加或减少，作为前缀或后缀       |
| $                       | 字段引用                         |
| in | 数组成员 |

### ④、内建变量

| 变量 | 描述 | 描述2 |
| --- | --- | --- |
| $n | 当前记录的第n个字段，字段间由FS分隔 | |
| $0 | 完整的输入记录 | |
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

`print` 和 `printf` 不能一起使用

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

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-145--w-74L7ba3sFssA.png)

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

1. 返回与 printf 函数进行了相同格式转换的字符串

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

# 三、数据处理（行列转换）

## 1、将文本转为矩阵：`pivot`

1. 必须排序后才能正常使用
2. 若是数据只有 3 列，则以原数据的第一列为纵坐标，第二列为横坐标来建立表格
3. 若是数据有 4 列，则以原数据的第一列为纵表头，第二列为横表头，同时在矩阵的第二列增加一列以字母命名的表格头，在新行里写入原数据第四列的数据
4. 若是数据有 5 列，则在矩阵的第二列增加两列以字母命名的表格头；以此类推

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
[trial@localhost cuichangjian]$ ssort -k1,2 data | pivot -k1
* 1 2 3 4
1 1 3 3 6
2 3 2 0 6
3 0 1 3 0

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
[trial@localhost cuichangjian]$ ssort -k1,2 data2 | pivot -k1
* * 1 2 3 4
1 A 1 3 3 6
1 B 40.1312 3623.13 6.431 3.445
2 A 4 2 0 6
2 B 4.5 0.042 0 233.03
3 A 0 1 3 0
3 B 0 53.21 1.0242 0

[trial@localhost cuichangjian]$ cat data3
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
[trial@localhost cuichangjian]$ ssort -k1,2 data3 | pivot -k1
* * 1 2 3 4
1 A 1 3 0 6
1 B 2 1 0 3
1 C 2 3 0 2
1 D 2 3 0 1
2 A 3 0 0 0
2 B 3 0 0 0
2 C 2 0 0 0
2 D 6 0 0 0
3 A 0 1 3 0
3 B 0 2 2 0
3 C 0 2 4 0
3 D 0 2 6 0
[trial@localhost cuichangjian]$ 
```

5. 没有的数据会以 0 来补足

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-164--ou2z2pkzIbUnuw.png)

### ①、语法

`pivot -k1[,COL] [FILE]`
`pivot -k 开始的主键列,结束的主键列 [FILE]`

### ②、参数

1. -k：指定主键列

## 2、将矩阵转为文本：`unpivot`

1. `pivot` 的反向操作
2. 表格的纵坐标变为第一列，横坐标变为第二列
3. 因为将文本转为矩阵会用 0 补足空数据的原因，所以转变回来的数据可能会多一些

```shell
[trial@localhost cuichangjian]$ ssort -k1,2 data3
1 1 1 2 2 2
1 2 3 1 3 3
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6
[trial@localhost cuichangjian]$ ssort -k1,2 data3 | pivot -k1
* * 1 2 3 4
1 A 1 3 0 6
1 B 2 1 0 3
1 C 2 3 0 2
1 D 2 3 0 1
2 A 3 0 0 0
2 B 3 0 0 0
2 C 2 0 0 0
2 D 6 0 0 0
3 A 0 1 3 0
3 B 0 2 2 0
3 C 0 2 4 0
3 D 0 2 6 0
[trial@localhost cuichangjian]$ ssort -k1,2 data3 | pivot -k1 | unpivot -k1
1 1 1 2 2 2
1 2 3 1 3 3
1 3 0 0 0 0
1 4 6 3 2 1
2 1 3 3 2 6
2 2 0 0 0 0
2 3 0 0 0 0
2 4 0 0 0 0
3 1 0 0 0 0
3 2 1 2 2 2
3 3 3 2 4 6
3 4 0 0 0 0
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-321--pugfwPS5-xUaLA.png)

### ①、语法

`unpivot -kCOL[,COL] [FILE]`
`unpivot -k 开始的主键列,结束的主键列 [FILE]`

### ②、参数

1. -k：指定主键列

## 3、行转列：`tov`

1. 根据参数 `-n` 指定的数，将行截取为设定的列数，多余的移到下一行；不设定的话就是将数据变为一列
2. 若指定参数 `-k`，那么参数 `-n` 的计数会在参数 `-k` 指定的列之后开始
   1. 若参数 `-n` 小于原数据的列数，则多余的数据会下移到下一行，指定的主键列会补全在移到下一行的数据之前

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
[trial@localhost cuichangjian]$ ssort -k1 data | tov -k1 -n1
1 2
1 3
1 3
1 3
1 1
1 1
1 4
1 6
2 2
2 2
2 2
2 2
2 4
2 6
2 1
2 4
3 2
3 1
3 3
3 3
3 2
3 1
```

   2. 若参数 `-n` 大于原数据的列数，则不变

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
[trial@localhost cuichangjian]$ ssort -k1 data | tov -k1 -n4
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
```

3. 每一行数据最后都有一个回车，也就是说，如果原数据一行有 3 列，而指定参数 `-n2` ，且不指定参数 `-k` 那么结果是：

- 第一行 2 个数据
- 第二行 1 个数据（因为有回车）
- 第三行 1 个数据（和第 2  行的数据原本应该是在同一行，但是因为原数据每行最后的回车，就变为了第三行；而且原本的结果是和第二行的是同一行，这样第二行就是 2 个数据，所以第三行还是 1 个数据）
- 第四行 2 个数据（第 2 个数据后有回车）
- 第五行又与第一行相同

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ tov -n2 master 
1 第一列
2
2
第二列 4
3 第三列
1
4
第四列 5
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-517--cCPL6HNCAmHLjQ.png)

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-637--TbSAxP_RgWSPAQ.png)

### ①、语法

`tov -n <NUM> -kCOL1[,COL2]... [FILE]`
`tov -n 指定每行几列数据 -k 开始的主键列,结束的主键列 ... [FILE]`

1. 不指定参数 `-n` 和 `-k`；没有主键，每行一列数据

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ tov master 
1
第一列
2
2
第二列
4
3
第三列
1
4
第四列
5
```

2. 指定参数 `-k`；参数 `-n` 的计数会在参数 `-k` 指定的列之后开始，指定的主键列会补全在移到下一行的数据之前

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ tov -k1 master 
1 第一列
1 2
2 第二列
2 4
3 第三列
3 1
4 第四列
4 5
```

3. 都指定；若参数 `-n` 小于原数据的列数，则会下移到下一行；若参数 `-n` 大于原数据的列数，则不变

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ tov -k1 -n1 master 
1 第一列
1 2
2 第二列
2 4
3 第三列
3 1
4 第四列
4 5
[trial@localhost cuichangjian]$ tov -k1 -n3 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
```

### ②、参数

1. -n：指定每一行有多少列
2. -k：指定主键列

## 4、列转行：`toh`

1. 根据参数 `-n` 指定的数，将行截取为设定的列数，多余的移到下一行；不设定的话就是将数据变为一行

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
[trial@localhost cuichangjian]$ toh data
3 2 1 2 2 2 1 2 3 1 3 3 1 1 1 2 2 2 3 3 3 2 4 6 1 4 6 3 2 1 2 1 4
[trial@localhost cuichangjian]$ toh -n 20 data
3 2 1 2 2 2 1 2 3 1 3 3 1 1 1 2 2 2 3 3
3 2 4 6 1 4 6 3 2 1 2 1 4

```

2. 若指定参数 `-k`，那么参数 `-n` 的计数会在参数 `-k` 指定的列之后开始
   1. 若参数 `-n` 小于原数据的列数，则多余的数据会下移到下一行，指定的主键列会补全在移到下一行的数据之前

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
[trial@localhost cuichangjian]$ ssort -k1 data | toh -k1 -n5
1 2 3 3 3 1
1 1 4 6
2 2 2 2 2 4
2 6 1 4
3 2 1 3 3 2
3 1
```

   2. 若参数 `-n` 大于原数据的列数，则不变

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
[trial@localhost cuichangjian]$ ssort -k1 data | toh -k1 -n20
1 2 3 3 3 1 1 4 6
2 2 2 2 2 4 6 1 4
3 2 1 3 3 2 1
```

3. 回车的问题和上面一样

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-753--DB3xVCMQVAUdjg.png)

### ①、语法
`toh -n <NUM> -l <String> -kCOL1[,COL2]... [FILE]`
`toh -n 指定每行几列数据 -l 拼接符 -k 开始的主键列,结束的主键列... [FILE]`

1. 参数 `-l` 可以指定拼接符

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | toh -k1 -l-- -n5
1 2--3--3--3--1
1 1--4--6
2 2--2--2--2--4
2 6--1--4
3 2--1--3--3--2
3 1
```

### ②、参数

1. -n：指定每行几列数据
2. -k：指定主键列
3. -l：指定拼接符

## 5、行列转换：`row2col`

行变列，列变行
横着的变成竖着的，竖着的变成横着的

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-851--Y5wdMUkIJVMwCQ.png)

### ①、语法

`row2col [FILE]`

```shell
[trial@localhost cuichangjian]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ row2col master 
1 2 3 4
第一列 第二列 第三列 第四列
2 4 1 5
```

### ②、参数

无

## 6、将下一行的数据放到上一行：`shiftrow`

1. 此命令必须排序后才可正常使用，且排序指定的主键列要和该命令指定的主键列相同
2. 排序后，依据指定的主键列，将相同主键的最后一行删除，然后将删除的最后一行的数据放上后一行的末尾，以此类推
3. 如果指定的主键列只有一行，则主键列之后是空的

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-02-943--8nddgZWTIoEAuA.png)

### ①、语法

`shiftrow -k1[,COL] [FILE]`

`shiftrow -k 第一列,结束的主键列 文件`

1. 指定主键列为第 1 列：`ssort -k1 data | shiftrow -k1`

- 则以第一列为主键列，删除每个相同主键列的最后一行，将去掉主键的数据放到上一行

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | shiftrow -k1
1 2 3 3 3
1 3 3 1 1
1 1 1 4 6
2 2 2 2 2
2 2 2 4 6
2 4 6 1 4
3 2 1 3 3
3 3 3 2 1
```

2. 指定主键列为第 1、2 列：`ssort -k1 data | shiftrow -k1,2`

- 则以第 1、2列为主键列，删除每个相同主键列的最后一行，将去掉主键的数据放到上一行

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | shiftrow -k1,2
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2 2
2 4 6
2 1 4
3 2 1
3 3 3
3 2 1
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-03-115--BmXx1JpSZErisA.png)

### ②、参数

-k：指定主键列

## 7、将数据以 {x,y,z,...} 形式输出：`brace`

1. 不论数据有几行几列都将变为一行以 {x,y,z,...} 的形式输出
2. 不会自动换行，所以一般后面会加指令 `tov` 进行换行
3. 一般用来配合指令 `gzcat` 来使用

### ①、语法

`brace [FILE]`

`brace 文件`

1. 不论数据有几行几列都将变为一行以 {x,y,z,...} 的形式输出；不会自动换行

```shell
[trial@smartedu data]$ sdate -e $(sdate today) $(sdate today/+13) | tov -n7
20220822 20220823 20220824 20220825 20220826 20220827 20220828
20220829 20220830 20220831 20220901 20220902 20220903 20220904
[trial@smartedu data]$ sdate -e $(sdate today) $(sdate today/+13) | tov -n7 | brace
{20220822,20220823,20220824,20220825,20220826,20220827,20220828,20220829,20220830,20220831,20220901,20220902,20220903,20220904}[trial@smartedu data]$
```

2. 不会自动换行，所以一般后面会加指令 `tov` 进行换行

```shell
[trial@smartedu data]$ sdate -e $(sdate today) $(sdate today/+13) | tov -n7
20220822 20220823 20220824 20220825 20220826 20220827 20220828
20220829 20220830 20220831 20220901 20220902 20220903 20220904
[trial@smartedu data]$ sdate -e $(sdate today) $(sdate today/+13) | tov -n7 | brace | tov
{20220822,20220823,20220824,20220825,20220826,20220827,20220828,20220829,20220830,20220831,20220901,20220902,20220903,20220904}
[trial@smartedu data]$ 
```

### ②、参数

无

# 四、数据格式化

## 1、对数字补 0：`fmtfixed`

1. 数据的位数只会增加不会减少；前面是 0 也不会变
2. 比如一个数据有 4 位，设定参数`-w6` 时会在前面补 2 个 0，设定参数`-w2` 时数据还是 4 位，不会改变
3. 非数字会被变为 0 ，位数为参数`-w` 所设定的位数
4. 小数会被舍弃

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-03-344--pZIwcfjSylddWw.png)

### ①、语法

`fmtfixed –w<N> -cCOL1[,COL2]… [FILE]`

`fmtfixed –w 固定的位数 -c 开始补0的列,结束补0的列 … [FILE]`

```shell
[trial@localhost cuichangjian]$ cat orderdata | head
20160203 九州B 0049 0056 0153 0006 56016 00001 00020 00000000000045104947 95.00 129
20160203 九州B 0049 0056 0153 0005 56011 00003 00040 00000000000045142314 70.00 89
20160203 九州B 0049 0056 0153 0005 56011 00003 00030 00000000000045142321 70.00 89
20160203 九州B 0049 0060 0095 0003 _ _ _ 00000000000045149658 130.00 198
20160203 九州B 0049 0060 0095 0004 _ _ _ 00000000000045149672 195.00 298
20160203 九州B 0049 0056 0087 0002 56004 00001 00020 00000000000045161261 74.00 89
20160203 九州B 0049 0056 0153 0006 _ _ _ 00000000000045164200 63.00 79
20160203 九州B 0049 0056 0153 0006 _ _ _ 00000000000045164224 75.00 99
20160203 九州B 0049 0060 0095 0004 _ _ _ 00000000000045165443 195.00 299
20160203 九州B 0049 0056 0154 0010 56019 00001 00080 00000000000045176852 172.00 239
[trial@localhost cuichangjian]$ fmtfixed -w4 -c1,12 orderdata | head
20160203 0000 0049 0056 0153 0006 56016 00001 00020 00000000000045104947 0095 0129
20160203 0000 0049 0056 0153 0005 56011 00003 00040 00000000000045142314 0070 0089
20160203 0000 0049 0056 0153 0005 56011 00003 00030 00000000000045142321 0070 0089
20160203 0000 0049 0060 0095 0003 0000 0000 0000 00000000000045149658 0130 0198
20160203 0000 0049 0060 0095 0004 0000 0000 0000 00000000000045149672 0195 0298
20160203 0000 0049 0056 0087 0002 56004 00001 00020 00000000000045161261 0074 0089
20160203 0000 0049 0056 0153 0006 0000 0000 0000 00000000000045164200 0063 0079
20160203 0000 0049 0056 0153 0006 0000 0000 0000 00000000000045164224 0075 0099
20160203 0000 0049 0060 0095 0004 0000 0000 0000 00000000000045165443 0195 0299
20160203 0000 0049 0056 0154 0010 56019 00001 00080 00000000000045176852 0172 0239
[trial@localhost cuichangjian]$ fmtfixed -w8 -c1,12 orderdata | head
20160203 00000000 00000049 00000056 00000153 00000006 00056016 00000001 00000020 00000000000045104947 00000095 00000129
20160203 00000000 00000049 00000056 00000153 00000005 00056011 00000003 00000040 00000000000045142314 00000070 00000089
20160203 00000000 00000049 00000056 00000153 00000005 00056011 00000003 00000030 00000000000045142321 00000070 00000089
20160203 00000000 00000049 00000060 00000095 00000003 00000000 00000000 00000000 00000000000045149658 00000130 00000198
20160203 00000000 00000049 00000060 00000095 00000004 00000000 00000000 00000000 00000000000045149672 00000195 00000298
20160203 00000000 00000049 00000056 00000087 00000002 00056004 00000001 00000020 00000000000045161261 00000074 00000089
20160203 00000000 00000049 00000056 00000153 00000006 00000000 00000000 00000000 00000000000045164200 00000063 00000079
20160203 00000000 00000049 00000056 00000153 00000006 00000000 00000000 00000000 00000000000045164224 00000075 00000099
20160203 00000000 00000049 00000060 00000095 00000004 00000000 00000000 00000000 00000000000045165443 00000195 00000299
20160203 00000000 00000049 00000056 00000154 00000010 00056019 00000001 00000080 00000000000045176852 00000172 00000239
```

### ②、参数

1. -w：指定固定的位数
2. -c：指定固定位数的列

## 2、对字符串补 0：`fmtfixed_str`

1. 既可以对数字补 0，也可以对字符串补 0
2. 数据的位数只会增加不会减少
3. 一个字母占一位，一个汉字占三位

### ①、语法

`fmtfixed -w -cCOL1[,COL2]... [FILE]`
`fmtfixed 指定位数 -c 开始补0的列,结束补0的列 ... [FILE] `

1. 一般用法

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ fmtfixed_str -c2 -w1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ fmtfixed_str -c1,3 -w4 master 
0001 第一列 0002
0002 第二列 0004
0003 第三列 0001
0004 第四列 0005
[trial@smartedu data]$ fmtfixed_str -c1,3 -w10 master 
0000000001 0第一列 0000000002
0000000002 0第二列 0000000004
0000000003 0第三列 0000000001
0000000004 0第四列 0000000005
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master 
000000000001 000第一列 000000000002
000000000002 000第二列 000000000004
000000000003 000第三列 000000000001
000000000004 000第四列 000000000005
[trial@smartedu data]$ 
```

### ②、参数

1. -w：指定固定的位数
2. -c：指定固定位数的列

## 3、以千分位显示数字：`fmtcomma`

1. 以千分位显示数字，如：12,345,456
2. 注意：千分位处理后的列不能再进行运算。所以，千分位一般用于最后账票显示的格式化。切记！！切记！！

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-03-429--FuDtuGlWUde96Q.png)

### ①、语法

`fmtcomma –cCOL1[,COL2]… [FILE]`
`fmtcomma –c 开始的列,结束的列 … [FILE]`

1. 先将数据固定位数，再变为以千分位显示

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
[trial@localhost cuichangjian]$ fmtfixed -w9 -c1 data
000000003 2 1
000000002 2 2
000000001 2 3
000000001 3 3
000000001 1 1
000000002 2 2
000000003 3 3
000000002 4 6
000000001 4 6
000000003 2 1
000000002 1 4
000000003 3 3
000000002 1 3
[trial@localhost cuichangjian]$ fmtfixed -w9 -c1 data | fmtcomma -c1
000,000,003 2 1
000,000,002 2 2
000,000,001 2 3
000,000,001 3 3
000,000,001 1 1
000,000,002 2 2
000,000,003 3 3
000,000,002 4 6
000,000,001 4 6
000,000,003 2 1
000,000,002 1 4
000,000,003 3 3
000,000,002 1 3
```

### ②、参数

1. -c：指定以千分位显示的列

## 4、以十进制格式显示数字：`fmtfloat`

1. 将数字变为以十进制格式显示，如：01、1.0 变为 1
2. 非数字会被变为 0
3. 参数 `-r` 会将数字变为负数（负数变为正数）

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-03-562--DcF4BQOChiQz5w.png)

### ①、语法

`fmtfloat –r –cCOL1[,COL2]… [FILE]`
`fmtfloat 将数字变为负数 –c 开始的列,结束的列 … [FILE]`

1. 以十进制格式显示数字

```shell
[trial@localhost cuichangjian]$ echo 0001 1.1 0002 1300.0 0003 -003 | tov -n2
0001 1.1
0002 1300.0
0003 -003
[trial@localhost cuichangjian]$ echo 0001 1.1 0002 1300.0 0003 -003 | tov -n2 | fmtfloat -c2
0001 1.1
0002 1300
0003 -3
```

2. 将数字变为负数

```shell
[trial@localhost cuichangjian]$ echo 0001 1.1 0002 1300.0 0003 -003 | tov -n2
0001 1.1
0002 1300.0
0003 -003
[trial@localhost cuichangjian]$ echo 0001 1.1 0002 1300.0 0003 -003 | tov -n2 | fmtfloat -r -c2
0001 -1.1
0002 -1300
0003 3
```

3. 非数字会被变为 0

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
[trial@localhost cuichangjian]$ fmtfixed -w9 -c1 data | fmtcomma -c1
000,000,003 2 1
000,000,002 2 2
000,000,001 2 3
000,000,001 3 3
000,000,001 1 1
000,000,002 2 2
000,000,003 3 3
000,000,002 4 6
000,000,001 4 6
000,000,003 2 1
000,000,002 1 4
000,000,003 3 3
000,000,002 1 3
[trial@localhost cuichangjian]$ fmtfixed -w9 -c1 data | fmtcomma -c1 | fmtfloat  -c1
0 2 1
0 2 2
0 2 3
0 3 3
0 1 1
0 2 2
0 3 3
0 4 6
0 4 6
0 2 1
0 1 4
0 3 3
0 1 3
```

### ②、参数

1. -c：指定以十进制格式显示数字的列
2. -r：将正数变为负数，将负数变为正数

## 5、科学计数法转换到十进制：`fmtdecimal`

1. 将科学计数法转换到十进制

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/2023-07-25-13--17-03-775--pouDneS7_vc-MQ.png)

### ①、语法

`fmtdecimal -cCOL1[,COL2]… [FILE]`
`fmtdecimal -c 开始的列,结束的列 … [FILE]`

```shell
[trial@zaimu_pj ~]$ echo 1 2 1e-2 2 2 1.002 3 2 1e+2|tov -n3
1 2 1e-2
2 2 1.002
3 2 1e+2
[trial@zaimu_pj ~]$ echo 1 2 1e-2 2 2 1.002 3 2 1e+2|tov -n3|fmtdecimal -c3
1 2 0.01
2 2 1.002
3 2 100
```

### ②、参数

1. -c：指定以十进制格式显示数字的列

## 6、半角字符转换为全角字符：`fmtzen`

1. 将半角字符转换为全角字符
2. 注意全角字符的空格不能被识别为列的分隔符

### ①、语法

`fmtzen -cCOL1[,COL2]... [FILE]`
`fmtzen -c 开始的列,结束的列 ... [FILE]`

1. 全角字符的空格不能被识别为列的分隔符

```shell
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3
1 2 3
a b c
１　２　３　ａ　ｂ　ｃ
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3 | colc
3
1
```

2. 将半角字符转换为全角字符

```shell
[trial@localhost data]$ echo 1 2 3 a b c １　２　３ ａ　ｂ　ｃ 123| tov -n3
1 2 3
a b c
１　２　３ ａ　ｂ　ｃ 123
[trial@localhost data]$ echo 1 2 3 a b c １　２　３ ａ　ｂ　ｃ 123| tov -n3 | fmtzen -c1,3
１ ２ ３
ａ ｂ ｃ
１　２　３ ａ　ｂ　ｃ １２３
```

### ②、参数

1. -c：指定转换为全角字符的列

## 7、全角字符转换成半角字符：`fmthan`

1. 将全角字符转换为半角字符
2. 注意全角字符的空格不能被识别为列的分隔符
3. 全角空格会被转换为：`_`

### ①、语法

`fmthan -cCOL1[,COL2]... [FILE]`
`fmthan -c 开始的列,结束的列 ... [FILE]`

1. 全角字符的空格不能被识别为列的分隔符

```shell
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3
1 2 3
a b c
１　２　３　ａ　ｂ　ｃ
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3 | colc
3
1
```

2. 将全角字符转换为半角字符

```shell
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3
1 2 3
a b c
１　２　３　ａ　ｂ　ｃ
[trial@localhost data]$ echo 1 2 3 a b c １　２　３　ａ　ｂ　ｃ| tov -n3 | fmthan -c1
1 2 3
a b c
1_2_3_a_b_c
```

### ②、参数

1. -c：指定转换为全角字符的列

## 8、转换日期格式 `/`：`fmtdate`

1. 将 `YYYYMMDD` 格式的日期数据转换为 `YYYY/MM/DD` 格式的
2. 其他格式的数据不能转换

### ①、语法

`fmtcomma -cCOL1[,COL2]... [FILE]`
`fmtcomma -c 指定开始的列,指定结束的列 ... 文件`

1. 一般用法

```shell
[trial@smartedu data]$ cat test_date 
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
[trial@smartedu data]$ fmtdate -c1,3 test_date 
2016/01/10 2016/01/11 2016/01/12 1111
2016/01/13 2016/01/14 2016/01/15 1111
2016/01/16 2016/01/17 2016/01/18 1111
2016/01/19 2016/01/20 2016/01/21 1111
2016/01/22 2016/01/23 2016/01/24 1111
2016/01/25 2016/01/26 2016/01/27 1111
2016/01/28 2016/01/29 2016/01/30 1111
2016/01/31 2016/02/01 2016/02/02 1111
2016/02/03 2016/02/04 2016/02/05 1111
2016/02/06 2016/02/07 2016/02/08 1111
2016/02/09 2016/02/10 2016/02/11 1111
2016/02/12 2016/02/13 2016/02/14 1111
2016/02/15 2016/02/16 2016/02/17 1111
2016/02/18 2016/02/19 2016/02/20 1111
2016/02/21 2016/02/22 2016/02/23 1111
2016/02/24 2016/02/25 2016/02/26 1111
2016/02/27 2016/02/28 2016/02/29 1111
2016/03/01 2016/03/02 2016/03/03 1111
```

2. 选择不能转换的列不会报错，会原样输出

```shell
[trial@smartedu data]$ cat test_date 
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
[trial@smartedu data]$ fmtdate -c1,4 test_date 
2016/01/10 2016/01/11 2016/01/12 1111
2016/01/13 2016/01/14 2016/01/15 1111
2016/01/16 2016/01/17 2016/01/18 1111
2016/01/19 2016/01/20 2016/01/21 1111
2016/01/22 2016/01/23 2016/01/24 1111
2016/01/25 2016/01/26 2016/01/27 1111
2016/01/28 2016/01/29 2016/01/30 1111
2016/01/31 2016/02/01 2016/02/02 1111
2016/02/03 2016/02/04 2016/02/05 1111
2016/02/06 2016/02/07 2016/02/08 1111
2016/02/09 2016/02/10 2016/02/11 1111
2016/02/12 2016/02/13 2016/02/14 1111
2016/02/15 2016/02/16 2016/02/17 1111
2016/02/18 2016/02/19 2016/02/20 1111
2016/02/21 2016/02/22 2016/02/23 1111
2016/02/24 2016/02/25 2016/02/26 1111
2016/02/27 2016/02/28 2016/02/29 1111
2016/03/01 2016/03/02 2016/03/03 1111
[trial@smartedu data]$ 
```

### ②、参数

1. -c：指定进行格式转换的列

## 9、转换日期格式 `-`：`fmtisodate`

1. 将 `YYYYMMDD` 格式的日期数据转换为 `YYYY-MM-DD` 格式的
2. 其他格式的数据不能转换
3. 与 `fmtdate` 类似

### ①、语法

`fmtisodate -cCOL1[,COL2]... [FILE]`

`fmtisodate -c 指定开始的列,指定结束的列 ... 文件`

1. 一般用法

```shell
[trial@smartedu data]$ cat test_date 
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
[trial@smartedu data]$ fmtisodate -c1,2 test_date 
2016-01-10 2016-01-11 20160112 1111
2016-01-13 2016-01-14 20160115 1111
2016-01-16 2016-01-17 20160118 1111
2016-01-19 2016-01-20 20160121 1111
2016-01-22 2016-01-23 20160124 1111
2016-01-25 2016-01-26 20160127 1111
2016-01-28 2016-01-29 20160130 1111
2016-01-31 2016-02-01 20160202 1111
2016-02-03 2016-02-04 20160205 1111
2016-02-06 2016-02-07 20160208 1111
2016-02-09 2016-02-10 20160211 1111
2016-02-12 2016-02-13 20160214 1111
2016-02-15 2016-02-16 20160217 1111
2016-02-18 2016-02-19 20160220 1111
2016-02-21 2016-02-22 20160223 1111
2016-02-24 2016-02-25 20160226 1111
2016-02-27 2016-02-28 20160229 1111
2016-03-01 2016-03-02 20160303 1111
[trial@smartedu data]$
```

2. 选择不能转换的列不会报错，会原样输出

```shell
[trial@smartedu data]$ cat test_date 
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
[trial@smartedu data]$ fmtisodate -c1,4 test_date 
2016-01-10 2016-01-11 2016-01-12 1111
2016-01-13 2016-01-14 2016-01-15 1111
2016-01-16 2016-01-17 2016-01-18 1111
2016-01-19 2016-01-20 2016-01-21 1111
2016-01-22 2016-01-23 2016-01-24 1111
2016-01-25 2016-01-26 2016-01-27 1111
2016-01-28 2016-01-29 2016-01-30 1111
2016-01-31 2016-02-01 2016-02-02 1111
2016-02-03 2016-02-04 2016-02-05 1111
2016-02-06 2016-02-07 2016-02-08 1111
2016-02-09 2016-02-10 2016-02-11 1111
2016-02-12 2016-02-13 2016-02-14 1111
2016-02-15 2016-02-16 2016-02-17 1111
2016-02-18 2016-02-19 2016-02-20 1111
2016-02-21 2016-02-22 2016-02-23 1111
2016-02-24 2016-02-25 2016-02-26 1111
2016-02-27 2016-02-28 2016-02-29 1111
2016-03-01 2016-03-02 2016-03-03 1111
[trial@smartedu data]$ 
```

### ②、参数

1. -c：指定进行格式转换的列

## 10、转换空数据：`fmtnull`

1. smart 中的空数据默认为：`_`
2. `-i` 可将字符指定为空数据，`-s` 可指定将空数据替换成的字符
3. 不指定参数 `-i` 时，默认替换符号 `_`
4. 参数 `-i` 只能指定一种 字符为空数据

### ①、语法

`fmtnull -c<対象列> [-i<NULL代表する文字>] -s<置換文字>  [FILE]`

`fmtnull -c 指定开始的列,指定结束的列 [-i 指定为空数据的字符] -s 指定将空数据替换为的字符 [FILE]`

1. 一般用法；将空数据 `_` 替换为 `**`

```shell
[trial@smartedu ~]$ echo "1 _ 2 _" | tov -n2
1 _
2 _
[trial@smartedu ~]$ echo "1 _ 2 _" | tov -n2 | fmtnull -c2 -s**
1 **
2 **
[trial@smartedu ~]$ 
```

2. 指定作为空数据的字符

```shell
[trial@smartedu ~]$ echo "1 _ 2 _" | tov -n2
1 _
2 _
[trial@smartedu ~]$ echo "1 _ 2 _" | tov -n2 | fmtnull -i1 -c1,2 -s**
** _
2 _
[trial@smartedu ~]$ 
```

### ②、参数

1. -c：指定替换的列
2. -i：指定为空数据的字符
3. -s：指定将空数据替换成的字符

## 11、转换 GET、POST 接收的数据：`qsstr`

1. 将 GET、POST 接收的数据转换为 NAME 格式

### ①、语法

`qsstr -i <String> -l <String> [FILE]`

`qsstr -i 数据为空时的填充符号 -l 不止一列时列数据之间的连接符 [FILE]`

1. 默认

```shell
[trial@localhost cuichangjian]$ echo "name=月海 言 yuehai&age=16&sex=" | qsstr
name 月海 言 yuehai
age 16
sex _
```

2. 指定列数据之间的连接符

```shell
[trial@localhost cuichangjian]$ echo "name=月海 言 yuehai&age=16&sex=" | qsstr -l@@@@
name 月海@@@@言@@@@yuehai
age 16
sex _
```

3. 指定数据为空时的填充符号

```shell
[trial@localhost cuichangjian]$ echo "name=月海 言 yuehai&age=16&sex=" | qsstr -i----
name 月海 言 yuehai
age 16
sex ----
```

### ②、参数

1. -l：指定列数据之间的连接符
2. -i：指定数据为空时的填充符号

## 12、将数据变为 JSON 格式：`tojson`

### ①、语法

`tojson [-h] [-A] [-N] [-n<Name>] [-H<ヘッダ名>...] [-c<数字列>...] [FILE]`
`tojson [-h] [-A] [-N] [-n<Name>] [-H<ヘッダ名>...] [-c<数字列>...] [FILE]`

1. 不指定参数时，默认以数字 1、2、3、4 ... 作为键，每一行作为值的 json 串

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson master 
[
{"1":"1","2":"第一列","3":"2"},
{"1":"2","2":"第二列","3":"4"},
{"1":"3","2":"第三列","3":"1"},
{"1":"4","2":"第四列","3":"5"}
]
[trial@smartedu data]$ 
```

2. 参数 `-h`：以第一行作为键，其余行作为值的 json 串

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson -h master 
[
{"1":"2","第一列":"第二列","2":"4"},
{"1":"3","第一列":"第三列","2":"1"},
{"1":"4","第一列":"第四列","2":"5"}
]
[trial@smartedu data]$ 
```

3. 参数 `-H`：给一列数据添加键，数量必须与列数相同

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson -HAA -HBB -HCC master 
[
{"AA":"1","BB":"第一列","CC":"2"},
{"AA":"2","BB":"第二列","CC":"4"},
{"AA":"3","BB":"第三列","CC":"1"},
{"AA":"4","BB":"第四列","CC":"5"}
]
[trial@smartedu data]$ 
```

4. 参数 `-n`：给整个 json 加上一个整体的名字

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson -nAA master 
"AA":[
{"1":"1","2":"第一列","3":"2"},
{"1":"2","2":"第二列","3":"4"},
{"1":"3","2":"第三列","3":"1"},
{"1":"4","2":"第四列","3":"5"}
]
[trial@smartedu data]$ 
```

5. 参数 `-N`： 将单独的空数据 `_` 变为 `null`，中间的下划线不会变化（比如a_b不会变化）

```shell
[trial@smartedu data]$ echo 1 2 a_b 4 5 _ | tov -n3
1 2 a_b
4 5 _
[trial@smartedu data]$ echo 1 2 a_b 4 5 _ | tov -n3 | tojson -N
[
{"1":"1","2":"2","3":"a_b"},
{"1":"4","2":"5","3":null}
]
[trial@smartedu data]$ 
```

6. 参数 `-A`：会以数组的形式 `[]` 输出数据，而不是 json `{}`；该参数不能同时与参数 `-h` 一起使用

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson -A master 
[
["1","第一列","2"],
["2","第二列","4"],
["3","第三列","1"],
["4","第四列","5"]
]
[trial@smartedu data]$ 
```

7. 参数 `-c`：将数据当作数字输出（去掉值的双引号）

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ tojson master 
[
{"1":"1","2":"第一列","3":"2"},
{"1":"2","2":"第二列","3":"4"},
{"1":"3","2":"第三列","3":"1"},
{"1":"4","2":"第四列","3":"5"}
]
[trial@smartedu data]$ tojson -c1,2 master 
[
{"1":1,"2":第一列,"3":"2"},
{"1":2,"2":第二列,"3":"4"},
{"1":3,"2":第三列,"3":"1"},
{"1":4,"2":第四列,"3":"5"}
]
[trial@smartedu data]$ 
```

### ②、参数

1. -A：会以数组的形式 `[]` 输出数据，而不是 json `{}`；该参数不能同时与参数 `-h` 一起使用
2. -c：将数据当作数字输出（去掉值的双引号）
3. -h：以第一行作为键，其余行作为值的 json 串
4. -H：给一列数据添加键，数量必须与列数相同
5. -n：给整个 json 加上一个整体的名字
6. -N：将单独的空数据 `_` 变为 `null`，中间的下划线不会变化（比如a_b不会变化）

## 13、去掉数据前面的 0：`delzero`

1. 与 `fmtfloat` 类似
   1. 不同的是 `fmtfloat` 会将字符串变为 0，会去除前面、后面无用的 0
   2. 而 `delzero` 不会将字符串变为 0，会去除前面无用的 0，但不会去除后面的 0
2. `delzero` 不仅可以去除数字前面的 0，字符串前面的 0 也可以去除
3. 参数 `-r` 会在数据前面添加负号，若是有负号则会将负号去掉；字符串前面也会添加负号

### ①、语法

`delzero [-r] -cCOL1[,COL2]... [FILE]`
`delzero [取反] -c 指定开始的列,指定结束的列 ... [FILE]`

1. 一般用法；去掉前面的 0

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master 
000000000001 000第一列 000000000002
000000000002 000第二列 000000000004
000000000003 000第三列 000000000001
000000000004 000第四列 000000000005
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master | delzero -c1,3 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$
```

2. 使用参数 `-r` 取反

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master 
000000000001 000第一列 000000000002
000000000002 000第二列 000000000004
000000000003 000第三列 000000000001
000000000004 000第四列 000000000005
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master | delzero -c1,3 -r
-1 -第一列 -2
-2 -第二列 -4
-3 -第三列 -1
-4 -第四列 -5
[trial@smartedu data]$ fmtfixed_str -c1,3 -w12 master | delzero -c1,3 -r | delzero -c1,3 -r
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$
```

3. 也可以去掉负数前面的 0

```shell
[trial@smartedu data]$ echo "0000001234567 0000321 -000123 -567"|delzero -c1,3
1234567 321 -123 -567
[trial@smartedu data]$ 
```

### ②、参数

1. -c：指定列
2. -r：在前面加负号

## 14、将 CSV 文件转换为 SMART 文本：`csv_text`

1. 将CSV文件（UTF-8）转换为 SMART 文本
2. CSV 文件以逗号 `,` 区分列，SMART 文本以空格 ` ` 区分列
3. 与 `cln --csv` 类似；但是更强大，`cln --csv` 只是单纯的将逗号 `,` 变为空格 ` ` 
4. 在使用 `csv_text` 前大多使用 `nkf -wxLu` 转换格式，输出时使用 `nkf -Luwx` 转换格式
   1. `nkf -wxLu`：用于文件从 Windows 系统到 Liunx 系统传输时的格式转换
   2. `nkf -Luwx`：用于文件从 Liunx 系统到 Windows 系统传输时的格式转换

### ①、语法

`csv_text [FILENAME]`
`csv_text csv文件`

1. 从 Windows 系统到 Liunx 系统、从 Liunx 系统到 Windows 系统

```shell
[trial@smartedu data]$ echo "0001,0002,0003" | nkf -wxLu | csv_text
0001 0002 0003
[trial@smartedu data]$ echo "0001,0002,0003" | nkf -Luwx | csv_text
0001 0002 0003
[trial@smartedu data]$ 
```

2. 若是有空数据，则会将空数据变为下划线 `_`，下划线 `_` 在 SMART 中就代表空数据

```shell
[trial@smartedu data]$ echo 1,,2,23 | csv_text
1 _ 2 23
[trial@smartedu data]$ 
```

3. 只会转换作为分割列的逗号 `,`；双引号里面的数据，就算有逗号，也不会被分割

```shell
[trial@smartedu data]$ echo '1,"2,3",2,23'
1,"2,3",2,23
[trial@smartedu data]$ echo '1,"2,3",2,23' | csv_text
1 2,3 2 23
[trial@smartedu data]$ 
```

4. 空格会变成下划线，每列最前和最后的空格会被自动去除

```shell
[trial@smartedu data]$ echo '1,"2,3",2,23,2 2, 3 3 ,  4  4  '
1,"2,3",2,23,2 2, 3 3 ,  4  4  
[trial@smartedu data]$ echo '1,"2,3",2,23,2 2, 3 3 ,  4  4  ' | csv_text
1 2,3 2 23 2_2 3_3 4__4
[trial@smartedu data]$ 
```

### ②、参数

无

## 15、根据文件中的格式格式化数据：`render`

### ①、语法

`render [-l<LABEL>]  TEMPLATE [DATAFILE]`
`render [-l 依据的格式化文件中的方法名] 依据的格式化文件 文件`

### ②、参数

1. -l：依据的格式化文件中的方法名
2. -i：若指定该参数，则原数据中若是有空数据 `_`，则不会将其变为空格 ` `

### ③、说明

1. 依据的格式化文件中，以 `%1` 代表数据文件的第一列，若想在其后方加字符串，则只需：`%1字符串`；若想在其前方加字符串，则：`字符串%1`
2. 各列之间要加空格，不然会去掉所有的空格
3. 下面使用的文件：

```shell
[trial@smartedu data]$ cat rea 
<!--LIST-->
%1aaa %2sss%3ddd
<!--LIST-->
[trial@smartedu data]$ 
```

### ④、案例

1. 格式化文件

```shell
[trial@smartedu data]$ cat rea 
<!--LIST-->
%1aaa %2sss%3ddd
<!--LIST-->
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ render -lLIST rea data
3aaa 2sss1ddd
2aaa 2sss2ddd
1aaa 2sss3ddd
1aaa 3sss3ddd
1aaa 1sss1ddd
2aaa 2sss2ddd
3aaa 3sss3ddd
2aaa 4sss6ddd
1aaa 4sss6ddd
3aaa 2sss1ddd
2aaa 1sss4ddd
3aaa 3sss3ddd
2aaa 1sss3ddd
[trial@smartedu data]$ 
```

2. 不指定参数 `-i`，改变空数据

```shell
[trial@smartedu data]$ cat rea 
<!--LIST-->
%1aaa %2sss%3ddd
<!--LIST-->
[trial@smartedu data]$ echo 1 1 1 2 _ 2 3 3 3 | tov -n3
1 1 1
2 _ 2
3 3 3
[trial@smartedu data]$ render -lLIST rea <(echo 1 1 1 2 _ 2 3 3 3 | tov -n3)
1aaa 1sss1ddd
2aaa  sss2ddd
3aaa 3sss3ddd
[trial@smartedu data]$ 
```

3. 指定参数 `-i`，不改变空数据

```shell
[trial@smartedu data]$ cat rea 
<!--LIST-->
%1aaa %2sss%3ddd
<!--LIST-->
[trial@smartedu data]$ echo 1 1 1 2 _ 2 3 3 3 | tov -n3
1 1 1
2 _ 2
3 3 3
[trial@smartedu data]$ render -lLIST -i rea <(echo 1 1 1 2 _ 2 3 3 3 | tov -n3)
1aaa 1sss1ddd
2aaa _sss2ddd
3aaa 3sss3ddd
[trial@smartedu data]$ 
```

# 五、join 系（多表）

 master 表；必须是唯一的，类似主键，写在左边
 tran 表；写在右边
 
## 1、存在连接：`ejoin、hejoin`

1. 必须排序之后才可以正常使用此命令
2. 筛选
3. 参数 `-k` 指定的是 tran 表的主键列， master 表永远从第一列开始
4. 根据 master 表的主键列对 tran 表指定的主键列进行筛选，显示 tran 表中主键与 master 表主键相同的 tran 表中的数据
5. 只会显示 tran 表的数据

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725155815.png)

### ①、语法

`ejoin -v -kCOL1[,COL2] MASTER [FILE]`
`ejoin 反向选择（隐藏应该显示的数据，显示原先右表不显示的数据） -k 开始的主键列,结束的主键列 MASTER [FILE]`

1. ejoin 指定的主键列是 tran 表的，master 表永远是从第一列开始；若是指定多列，master 表也是从第一列开始算起

```shell
[trial@localhost data]$ ssort -k1 master
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ ejoin -k1 master <(ssort -k1 tran)
1 01 423
2 04 341
2 03 643
3 01 223
```

2. 若是想指定 master 表的其他列，可以使用 `selcol` 命令改变表顺序

```shell
[trial@localhost data]$ ssort -k3 master
3 第三列 1
1 第一列 2
2 第二列 4
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ ejoin -k1 <(selcol -c3 master | ssort -k1) <(ssort -k1 tran)
1 01 423
2 04 341
2 03 643
5 02 213
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725155920.png)

3. 参数 -a 可以显示 tran 表中所有数据；对应的显示在上面，不对应的显示在下面

```shell
[trial@localhost data]$ ssort -k1 master
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ ejoin -k1 master <(ssort -k1 tran)
1 01 423
2 04 341
2 03 643
3 01 223
[trial@localhost cuichangjian]$ ejoin -a -k1 master <(ssort -k1 tran)
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
```

### ②、参数

1. -k：指定主键列
2. -v：反向选择（隐藏应该显示的数据，显示原先右表不显示的数据）
3. -a：显示右表全部的数据

### ③、`hejoin`

当 master 表很小、 tran 表很大时使用，使用方式与 `ejoin` 相同
使用 `hejoin` 时左表（master）需要排序，右表（tran）无需排序

## 2、内连接：`ijoin、hijoin`

1. 必须排序之后才可以正常使用此命令
2. 筛选、连接
3. 参数 `-k` 指定的是 tran 表的主键列， master 表永远从第一列开始
4. 根据 master 表的主键列对 tran 表指定的主键列进行筛选，显示 tran 表中主键与 master 表中主键相同的 tran 表中的数据
5. 会显示两个表的数据，根据 tran 表指定的主键列， tran 表的主键列在前、 master 表数据（不包括主键列）在中间、 tran 表数据（不包括主键列）在最后
6. 与 `ejoin` 相比，只是增加了显示 master 表数据的功能

### ①、语法

`ijoin -kCOL1[,COL2] MASTER [FILE]`
`ijoin -k 开始的主键列,结束的主键列 MASTER [FILE]`

1. ijoin 指定的主键列也是 tran 表的， master 表永远是从第一列开始；若是指定多列，则 master 表也是从第一列开始算起

```shell
[trial@localhost data]$ ssort -k1 master
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ ijoin -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
```

2. 若是想指定 master 表的其他列，当然也可以使用 selcol 命令改变表顺序
3. 参数 -a 可以显示 tran 表中所有的数据；对应的显示在上面，不对应的显示在下面

```shell
[trial@localhost cuichangjian]$ ejoin -k1 master <(ssort -k1 tran)
1 01 423
2 04 341
2 03 643
3 01 223
[trial@localhost cuichangjian]$ ijoin -a -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
5 02 213
```

### ②、参数

1. -k：指定主键列
2. -a：显示右表全部的数据

### ③、`hijoin`

当 master 表很小、 tran 表很大时使用，使用方式与 `ejoin` 相同
使用 `hijoin` 时左表（master）需要排序，右表（tran）无需排序

## 3、右连接：`rjoin、hrjoin、hrjoinrepalce` 等

### ①、`rjoin`

1. 必须排序之后才可以正常使用此命令
2. 连接、显示
3. 参数 `-k` 指定的是 tran 表的主键列， master 表永远从第一列开始
4. 会显示 tran 表所有的数据，根据 tran 表的主键列对 master 表的数据进行筛选，显示 master 表中主键与 tran 表中主键相同的 master 表中的数据， master 表没有的主键默认以 `*` 填充
5. 会显示两个表的数据，根据 tran 表指定的主键列， tran 表的主键列在前、 master 表数据（不包括主键列）在中间、 tran 表数据（不包括主键列）在最后
6. 与内连接 `ijoin` 相比，会显示右表全部的数据（类似加了 -a 参数），右表存在而左表不存在的数据，则本该显示左表数据的地方会以 `*` 代替

#### Ⅰ、语法

`rjoin -kCOL1[,COL2] RIGHT [LEFT]`
`rjoin -k 开始的主键列,结束的主键列 master表 tran表`

1. rjoin 指定的主键列也是 tran 表的， master 表永远是从第一列开始；若是指定多列，则 master 表也是从第一列开始算起

```shell
[trial@localhost data]$ ssort -k1 master
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ rjoin -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
5 ****** * 02 213
```

2. 若是想指定 master 表的其他列，当然也可以使用 selcol 命令改变表顺序
3. 可以使用 `-i` 参数来更改填充符号

```shell
[trial@localhost data]$ ssort -k1 master
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost cuichangjian]$ rjoin -i---- -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
5 ---- ---- 02 213
```

#### Ⅱ、参数

1. -k：指定主键列
2. -i：将填充符号由 `*`指定为其他的符号

### ②、`rjoin_alignright`

#### Ⅰ、语法

`rjoin -kCOL1[,COL2] RIGHT [LEFT]`
`rjoin -k 指定开始的主键列,指定结束的主键列 master表 tran表`

#### Ⅱ、参数

1. -k：指定主键列

#### Ⅲ、说明

1. `rjoin_alignright` 是 `rjoin` 的功能的小扩展，区别只是 `rjoin_alignright` 会将 master 表的数据放到最右边
2. 是为了解决 master 表数据拼接后，总是需要调整列的问题 （因为rjoin连接 master 后，会破坏原来 tran 的数据列）
3. 现在推荐使用 `rjoin_default`

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ rjoin_alignright -k1 master <(ssort -k1 data)
1 2 3 第一列 2
1 1 1 第一列 2
1 4 6 第一列 2
2 2 2 第二列 4
2 2 2 第二列 4
2 4 6 第二列 4
2 1 4 第二列 4
2 1 3 第二列 4
3 2 1 第三列 1
3 3 3 第三列 1
3 2 1 第三列 1
3 3 3 第三列 1
5 3 3 ****** *
[trial@smartedu data]$ 
```

### ③、`rjoin_default
`
#### Ⅰ、语法

`rjoin_default -k<キー> -i<設定文字> -M<マスタ列数> [-p<L|R>] [-c<置換列> ...] <master> [tran]`

---

`rjoin_default -k 指定主键列 -i master表为空时填充的字符串 -M master表的列数 [-p<master表在最左边|master表在最右边>] `
`[-c<指定master表为空时使用tran表的哪列进行填充> ...] <master> [tran]`

#### Ⅱ、参数

1. -k：指定主键列
2. -i：master 表为空时填充的字符串
3. -M：master 表的列数，必须为正确的列数，不然会报错
4. -p：规定 master 表位置
   1. L：master 表在最左边
   2. R：master表在最右边
   3. 不指定该参数则 master 表在主键后面，tran 表前面
5. -c：指定 master 表为空时使用 tran 表的哪列（原数据）进行填充，指定一列就只会填充一列，可以指定多列，但不能超过 master 表去除主键列之后的列数

#### Ⅲ、说明

1. `rjoin_defalut` 是 `rjoin` 全面的扩展指令
2. master 如果是空数据时，不需要提前使用 `touchi` 命令替代列，只需指令执行时，通过 -M 指定 master 的列数即可
3. 连接的 master 数据的列，可以通过 `-p` 参数灵活指定 master 新加数据列的位置，可以居左，居右，居中
4. 参数 `-c` 可指定 master 表为空时使用 tran 表的哪列进行填充
5. 必须指定参数`-k、-i、-M`
6. 推荐使用`rjoin_default`

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ rjoin_default -k1 -i**** -M3 master <(ssort -k1 data)
1 第一列 2 2 3
1 第一列 2 1 1
1 第一列 2 4 6
2 第二列 4 2 2
2 第二列 4 2 2
2 第二列 4 4 6
2 第二列 4 1 4
2 第二列 4 1 3
3 第三列 1 2 1
3 第三列 1 3 3
3 第三列 1 2 1
3 第三列 1 3 3
5 **** **** 3 3
[trial@smartedu data]$ 
```

2. 指定 master 表居右

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ rjoin_default -k1 -i**** -M3 -pR master <(ssort -k1 data)
1 2 3 第一列 2
1 1 1 第一列 2
1 4 6 第一列 2
2 2 2 第二列 4
2 2 2 第二列 4
2 4 6 第二列 4
2 1 4 第二列 4
2 1 3 第二列 4
3 2 1 第三列 1
3 3 3 第三列 1
3 2 1 第三列 1
3 3 3 第三列 1
5 3 3 **** ****
[trial@smartedu data]$ 
```

3. 指定使用 tran 表的第 1 列填充 master 表的第 1 列空数据

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ rjoin_default -k1 -i**** -M3 -pR -c1 master <(ssort -k1 data)
1 2 3 第一列 2
1 1 1 第一列 2
1 4 6 第一列 2
2 2 2 第二列 4
2 2 2 第二列 4
2 4 6 第二列 4
2 1 4 第二列 4
2 1 3 第二列 4
3 2 1 第三列 1
3 3 3 第三列 1
3 2 1 第三列 1
3 3 3 第三列 1
5 3 3 5 ****
[trial@smartedu data]$ 
```

4. 指定使用 tran 表的第 2、3 列填充 master 表的第 1、2 列空数据

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ rjoin_default -k1 -i**** -M3 -pR -c2,3 master <(ssort -k1 data)
1 2 3 第一列 2
1 1 1 第一列 2
1 4 6 第一列 2
2 2 2 第二列 4
2 2 2 第二列 4
2 4 6 第二列 4
2 1 4 第二列 4
2 1 3 第二列 4
3 2 1 第三列 1
3 3 3 第三列 1
3 2 1 第三列 1
3 3 3 第三列 1
5 3 3 3 3
[trial@smartedu data]$ 
```

### ④、`hrjoin
`
当 master 表很小、 tran 表很大时使用，使用方式与 `ejoin` 相同
使用 `hrjoin` 时 master 表需要排序， tran 表无需排序

### ⑤、`hrjoinrepalce`

#### Ⅰ、语法

`hrjoinrepalc -kCOL1[,COL2] -s RIGHT [LEFT]`
`hrjoinrepalc -k 指定开始的主键列,指定结束的主键列 -s master表 tran表`

#### Ⅱ、参数

1. `hrjoin` 指令的扩展，主要是连接不上 master 的数据，需要补充的列内容时，可以用 tran 里的指定列（单列）来补充
2. 升级后的 `hrjoin_default` 也包含了这个指令，但是可以置换 2 列以上的连续列，功能更强大
3. 推荐使用 `hrjoin_default`

#### Ⅲ、说明

1. 相当于 `hrjoin_default` 命令使用的参数 `-c`
2. 不过 `hrjoinrepalce` 命令只能指定一列 tran 里列来替换 master 的数据

#### Ⅳ、案例
### ⑥、`hrjoin_default`

#### Ⅰ、语法

`hrjoin_default -k<キー> -i<設定文字> -M<マスタ列数> [-p<L|R>] [-c<置換列> ...] <master> [tran]`

---

`hrjoin_default -k 指定开始的主键列,指定结束的主键列 -i master表为空时填充的字符串 -M master表的列数`
`[-p<master表在最左边|master表在最右边>] [-c<指定master表为空时使用tran表的哪列进行填充> ...] <master> [tran]`

#### Ⅱ、参数

1. -k：指定主键列
2. -i：master 表为空时填充的字符串
3. -M：master 表的列数，必须为正确的列数，不然会报错
4. -p：规定 master 表位置
	1. L：master 表在最左边
	2. R：master表在最右边
	3. 不指定该参数则 master 表在主键后面，tran 表前面
5. -c：指定 master 表为空时使用 tran 表的哪列（原数据）进行填充，指定一列就只会填充一列，可以指定多列，但不能超过 master 表去除主键列之后的列数

#### Ⅲ、说明

1. 当 master 表很小、 tran 表很大时使用，使用方式与 `rjoin_default` 相同
2. 使用 `hrjoin_default` 时 master 需要排序， tran 无需排序
3. 使用方式与 `rjoin_default` 相同

#### Ⅳ、案例

## 4、完全（外）连接：`ojoin、ojoin_default`

### ①、ojoin

#### Ⅰ、语法

`ojoin –i<String> –k[,COL] FILE…`
`ojoin –i 指定填充符号 –k 第一列,结束的主键列 FILE…`

#### Ⅱ、参数

1. -k：指定主键列
2. -i：将填充符号由 `*`指定为其他的符

#### Ⅲ、说明

1. 必须排序之后才可以正常使用此命令
2. 根据指定的主键列显示所有表的数据，表中没有的主键列会以 `0` 来填充
3. 与右连接 `rjoin` 类似，会显示所有表的数据，根据指定的主键列，主键列在前、然后按写的顺序显示表的数据

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725160200.png)

#### Ⅳ、案例

1. 可以指定多个表，但是所有表只能指定相同的主键列

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost data]$ ojoin -k1 master <(ssort -k1 tran) <(ssort -k1 data2)
1 第一列 2 01 423 2 3 3623.13
1 0 0 0 0 3 3 6.431
1 0 0 0 0 1 1 40.1312
1 0 0 0 0 4 6 3.445
2 第二列 4 04 341 2 2 53.54
2 0 0 03 643 2 2 0.042
2 0 0 0 0 4 6 233.03
2 0 0 0 0 1 4 4.5
3 第三列 1 01 223 2 1 1.15
3 0 0 0 0 3 3 1.0242
3 0 0 0 0 2 1 53.21
4 第四列 5 0 0 0 0 0
5 0 0 02 213 0 0 0
```

2. 若是想指定表的其他列为主键列，当然也可以使用 selcol 命令改变表顺序
3. 可以使用 `-i` 参数来更改填充符号

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost data]$ ojoin -i** -k1 master <(ssort -k1 tran) <(ssort -k1 data2)
1 第一列 2 01 423 2 3 3623.13
1 ** ** ** ** 3 3 6.431
1 ** ** ** ** 1 1 40.1312
1 ** ** ** ** 4 6 3.445
2 第二列 4 04 341 2 2 53.54
2 ** ** 03 643 2 2 0.042
2 ** ** ** ** 4 6 233.03
2 ** ** ** ** 1 4 4.5
3 第三列 1 01 223 2 1 1.15
3 ** ** ** ** 3 3 1.0242
3 ** ** ** ** 2 1 53.21
4 第四列 5 ** ** ** ** **
5 ** ** 02 213 ** ** **
```

### ②、ojoin_default

#### Ⅰ、语法

`ojoin_default -k<キー> [-i<設定文字>] -M<マスタ列数>...  <master1> <master2> ...`
`ojoin_default -k 指定开始的主键列,指定结束的主键列 [-i 表为空时填充的字符串] -M 各个表的列数...  <master1> <master2> ...`

#### Ⅱ、参数

1. -k：指定主键列
2. -M：各个表的列数
3. -i：表为空时填充的字符串

#### Ⅲ、说明

1. `ojoin` 指令的升级指令
2. 用于多个数据的列的拼接，需要主键 keys 一致
3. 数据为空时，不用事先补充代替数据
4. 以后用 `ojoin_default` 代替 `ojoin` 的指令
5. 参数 `-k` 不能指定所有列，必须至少有一列为数据，否则会出错
6. 使用方式与 `rjoin_default` 类似；
7. 其区别是：
   1. `rjoin_default` 的 master 表可能会显示不全，因为会显示 tran 表的全部数据，而 master 表只会显示 master 表中主键与 tran 表中主键相同的数据
   2. `ojoin_default` 会显示所有表的所有数据

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@smartedu data]$ cat data
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ cat data2
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
[trial@smartedu data]$ ojoin_default -k1 -i* -M3 -M3 -M4 master <(ssort -k1 data) <(ssort -k1 data2)
1 第一列 2 2 3 2 3 3623.13
1 * * 1 1 3 3 6.431
1 * * 4 6 1 1 40.1312
1 * * * * 4 6 3.445
2 第二列 4 2 2 2 2 53.54
2 * * 2 2 2 2 0.042
2 * * 4 6 4 6 233.03
2 * * 1 4 1 4 4.5
2 * * 1 3 * * *
3 第三列 1 2 1 2 1 1.15
3 * * 3 3 3 3 1.0242
3 * * 2 1 2 1 53.21
3 * * 3 3 * * *
4 第四列 5 * * * * *
5 * * 3 3 * * *
[trial@smartedu data]$ 
```

## 5、交叉连接：`crossjoin`

1. 必须排序之后才可以正常使用此命令
2. 不指定主键列：tran 表的每一条数据都会和 master 表每一条数据所结合
3. 指定主键列：
   1. 根据指定的主键列，tran 表指定主键的数据会结合 master 表相同主键的每一条数据，即相同主键的数据会产生笛卡儿积
   2. 会显示 master 表和 tran 表主键相对应的数据，不对应的数据不会显示
4. 一般在数据需要进行补全时使用

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725160246.png)

### ①、语法

`crossjoin -kCOL1[,COL2] LEFT [RIGHT]`
`crossjoin -k 开始的主键列,结束的主键列 LEFT [RIGHT]`

1. crossjoin 指定的主键列也是 tran 表的， master 表永远是从第一列开始；若是指定多列，则 master 表也是从第一列开始算起

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ crossjoin -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
```

2. 若是想指定 master 表的其他列，当然也可以使用 selcol 命令改变表顺序
3. 可以不指定参数 `-k`，不指定主键列：tran 表的每一条数据都会和 master 表每一条数据所结合，即产生笛卡儿积

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ crossjoin master <(ssort -k1 tran)
1 第一列 2 1 01 423
1 第一列 2 2 04 341
1 第一列 2 2 03 643
1 第一列 2 3 01 223
1 第一列 2 5 02 213
2 第二列 4 1 01 423
2 第二列 4 2 04 341
2 第二列 4 2 03 643
2 第二列 4 3 01 223
2 第二列 4 5 02 213
3 第三列 1 1 01 423
3 第三列 1 2 04 341
3 第三列 1 2 03 643
3 第三列 1 3 01 223
3 第三列 1 5 02 213
4 第四列 5 1 01 423
4 第四列 5 2 04 341
4 第四列 5 2 03 643
4 第四列 5 3 01 223
4 第四列 5 5 02 213
```

4. 指定参数 `-k`，指定主键列：根据指定的主键列，tran 表指定主键的数据会结合 master 表相同主键的每一条数据，即相同主键的数据会产生笛卡儿积

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ crossjoin -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223

[trial@localhost data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost data]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost data]$ crossjoin <(ssort -k1 data) <(ssort -k1 data2)
1 2 3 1 2 3 3623.13
1 2 3 1 3 3 6.431
1 2 3 1 1 1 40.1312
1 2 3 1 4 6 3.445
1 2 3 2 2 2 53.54
1 2 3 2 2 2 0.042
1 2 3 2 4 6 233.03
1 2 3 2 1 4 4.5
1 2 3 3 2 1 1.15
1 2 3 3 3 3 1.0242
1 2 3 3 2 1 53.21
1 3 3 1 2 3 3623.13
1 3 3 1 3 3 6.431
1 3 3 1 1 1 40.1312
1 3 3 1 4 6 3.445
1 3 3 2 2 2 53.54
1 3 3 2 2 2 0.042
1 3 3 2 4 6 233.03
1 3 3 2 1 4 4.5
1 3 3 3 2 1 1.15
1 3 3 3 3 3 1.0242
1 3 3 3 2 1 53.21
1 1 1 1 2 3 3623.13
1 1 1 1 3 3 6.431
1 1 1 1 1 1 40.1312
1 1 1 1 4 6 3.445
1 1 1 2 2 2 53.54
1 1 1 2 2 2 0.042
1 1 1 2 4 6 233.03
1 1 1 2 1 4 4.5
1 1 1 3 2 1 1.15
1 1 1 3 3 3 1.0242
1 1 1 3 2 1 53.21
1 4 6 1 2 3 3623.13
1 4 6 1 3 3 6.431
1 4 6 1 1 1 40.1312
1 4 6 1 4 6 3.445
1 4 6 2 2 2 53.54
1 4 6 2 2 2 0.042
1 4 6 2 4 6 233.03
1 4 6 2 1 4 4.5
1 4 6 3 2 1 1.15
1 4 6 3 3 3 1.0242
1 4 6 3 2 1 53.21
2 2 2 1 2 3 3623.13
2 2 2 1 3 3 6.431
2 2 2 1 1 1 40.1312
2 2 2 1 4 6 3.445
2 2 2 2 2 2 53.54
2 2 2 2 2 2 0.042
2 2 2 2 4 6 233.03
2 2 2 2 1 4 4.5
2 2 2 3 2 1 1.15
2 2 2 3 3 3 1.0242
2 2 2 3 2 1 53.21
2 2 2 1 2 3 3623.13
2 2 2 1 3 3 6.431
2 2 2 1 1 1 40.1312
2 2 2 1 4 6 3.445
2 2 2 2 2 2 53.54
2 2 2 2 2 2 0.042
2 2 2 2 4 6 233.03
2 2 2 2 1 4 4.5
2 2 2 3 2 1 1.15
2 2 2 3 3 3 1.0242
2 2 2 3 2 1 53.21
2 4 6 1 2 3 3623.13
2 4 6 1 3 3 6.431
2 4 6 1 1 1 40.1312
2 4 6 1 4 6 3.445
2 4 6 2 2 2 53.54
2 4 6 2 2 2 0.042
2 4 6 2 4 6 233.03
2 4 6 2 1 4 4.5
2 4 6 3 2 1 1.15
2 4 6 3 3 3 1.0242
2 4 6 3 2 1 53.21
2 1 4 1 2 3 3623.13
2 1 4 1 3 3 6.431
2 1 4 1 1 1 40.1312
2 1 4 1 4 6 3.445
2 1 4 2 2 2 53.54
2 1 4 2 2 2 0.042
2 1 4 2 4 6 233.03
2 1 4 2 1 4 4.5
2 1 4 3 2 1 1.15
2 1 4 3 3 3 1.0242
2 1 4 3 2 1 53.21
2 1 3 1 2 3 3623.13
2 1 3 1 3 3 6.431
2 1 3 1 1 1 40.1312
2 1 3 1 4 6 3.445
2 1 3 2 2 2 53.54
2 1 3 2 2 2 0.042
2 1 3 2 4 6 233.03
2 1 3 2 1 4 4.5
2 1 3 3 2 1 1.15
2 1 3 3 3 3 1.0242
2 1 3 3 2 1 53.21
3 2 1 1 2 3 3623.13
3 2 1 1 3 3 6.431
3 2 1 1 1 1 40.1312
3 2 1 1 4 6 3.445
3 2 1 2 2 2 53.54
3 2 1 2 2 2 0.042
3 2 1 2 4 6 233.03
3 2 1 2 1 4 4.5
3 2 1 3 2 1 1.15
3 2 1 3 3 3 1.0242
3 2 1 3 2 1 53.21
3 3 3 1 2 3 3623.13
3 3 3 1 3 3 6.431
3 3 3 1 1 1 40.1312
3 3 3 1 4 6 3.445
3 3 3 2 2 2 53.54
3 3 3 2 2 2 0.042
3 3 3 2 4 6 233.03
3 3 3 2 1 4 4.5
3 3 3 3 2 1 1.15
3 3 3 3 3 3 1.0242
3 3 3 3 2 1 53.21
3 2 1 1 2 3 3623.13
3 2 1 1 3 3 6.431
3 2 1 1 1 1 40.1312
3 2 1 1 4 6 3.445
3 2 1 2 2 2 53.54
3 2 1 2 2 2 0.042
3 2 1 2 4 6 233.03
3 2 1 2 1 4 4.5
3 2 1 3 2 1 1.15
3 2 1 3 3 3 1.0242
3 2 1 3 2 1 53.21
3 3 3 1 2 3 3623.13
3 3 3 1 3 3 6.431
3 3 3 1 1 1 40.1312
3 3 3 1 4 6 3.445
3 3 3 2 2 2 53.54
3 3 3 2 2 2 0.042
3 3 3 2 4 6 233.03
3 3 3 2 1 4 4.5
3 3 3 3 2 1 1.15
3 3 3 3 3 3 1.0242
3 3 3 3 2 1 53.21
```

5. 参数 -a 可以显示 tran 表中所有的数据；对应的显示在上面，不对应的显示在下面

```shell
[trial@localhost data]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
[trial@localhost data]$ crossjoin -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
[trial@localhost data]$ crossjoin -a -k1 master <(ssort -k1 tran)
1 第一列 2 01 423
2 第二列 4 04 341
2 第二列 4 03 643
3 第三列 1 01 223
5 02 213
```

### ②、参数

1. -k：指定主键列
2. -a：显示右表全部的数据

## 6、全连接：`alljoin、alljoin_default`

### ①、`alljoin`

#### Ⅰ、语法

`alljoin -i <init> -kCOL1[,COL2] MASTER [TRAN]`
`alljoin -i master表为空时填充的字符串 -k 指定开始的主键列,指定结束的主键列 MASTER [TRAN]`

#### Ⅱ、参数

1. -k：指定键列
2. -i：master 表为空时填充的字符串

#### Ⅲ、说明

1. 必须排序之后才可以正常使用此命令
2. master 表的数据可以重复
3. 与交叉连接 `crossjoin` 类似，根据主键 tran 表每一条数据都会和 master 表相同主键的每一条数据相连接
4. 与交叉连接 `crossjoin` 不同的是 `alljoin` 会显示 tran 表的所有数据，master 表没有的数据会默认以 `*` 显示；可以使用参数 `-i` 指定

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ ssort -k1 tran
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
6 08 125
[trial@smartedu data]$ alljoin -k1 -i@ <(ssort -k1 data) <(ssort -k1 tran)
1 2 3 01 423
1 1 1 01 423
1 4 6 01 423
2 2 2 04 341
2 2 2 04 341
2 4 6 04 341
2 1 4 04 341
2 1 3 04 341
2 2 2 03 643
2 2 2 03 643
2 4 6 03 643
2 1 4 03 643
2 1 3 03 643
3 2 1 01 223
3 3 3 01 223
3 2 1 01 223
3 3 3 01 223
5 3 3 02 213
6 @ @ 08 125
[trial@smartedu data]$ 
```

### ②、`alljoin_default`

#### Ⅰ、语法

`alljoin_default -k<キー> -i<設定文字> -M<マスタ列数> [-p<L|R>] [-c<置換列> ...] <master> [tran]`

---

`alljoin_default -k 指定主键列 -i master表为空时填充的字符串 -M master表的列数 [-p<master表在最左边|master表在最右边>] `
`[-c<指定master表为空时使用tran表的哪列进行填充> ...] <master> [tran]`

#### Ⅱ、参数

1. -k：指定主键列
2. -i：master 表为空时填充的字符串
3. -M：master 表的列数，必须为正确的列数，不然会报错
4. -p：规定 master 表位置
   1. L：master 表在最左边
   2. R：master表在最右边
   3. 不指定该参数则 master 表在主键后面，tran 表前面
5. -c：指定 master 表为空时使用 tran 表的哪列（原数据）进行填充，指定一列就只会填充一列，可以指定多列，但不能超过 master 表去除主键列之后的列数

#### Ⅲ、说明

1. 与交叉连接 `crossjoin` 类似，根据主键 tran 表每一条数据都会和 master 表相同主键的每一条数据相连接
2. 与交叉连接 `crossjoin` 不同的是 `alljoin_default` 会显示 tran 表的所有数据（master 表中与  tran 表不对应的数据不会显示），master 表没有的数据会默认以 `*` 显示；可以使用参数 `-i` 指定
3. master 表的数据可以重复
4. 相当于 master 表可以为空的 `alljoin`
5. 参数 `-p` 可指定连接后 master 字段的放在左边还是右边
6. 参数 `-c` 参数 -c 可指定 master 表为空时使用 tran 表的哪列进行填充
7. 必须指定参数`-k、-i、-M`
8. 使用方式与 `rjoin_default` 类似

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
6 08 125
[trial@smartedu data]$ alljoin_default -k1 -i@ -M3 <(ssort -k1 data) <(ssort -k1 tran)
1 2 3 01 423
1 1 1 01 423
1 4 6 01 423
2 2 2 04 341
2 2 2 04 341
2 4 6 04 341
2 1 4 04 341
2 1 3 04 341
2 2 2 03 643
2 2 2 03 643
2 4 6 03 643
2 1 4 03 643
2 1 3 03 643
3 2 1 01 223
3 3 3 01 223
3 2 1 01 223
3 3 3 01 223
5 3 3 02 213
6 @ @ 08 125
[trial@smartedu data]$ 
```

2.  master 表数据放在最右边

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
6 08 125
[trial@smartedu data]$ alljoin_default -k1 -i@ -M3 -pR <(ssort -k1 data) <(ssort -k1 tran)
1 01 423 2 3
1 01 423 1 1
1 01 423 4 6
2 04 341 2 2
2 04 341 2 2
2 04 341 4 6
2 04 341 1 4
2 04 341 1 3
2 03 643 2 2
2 03 643 2 2
2 03 643 4 6
2 03 643 1 4
2 03 643 1 3
3 01 223 2 1
3 01 223 3 3
3 01 223 2 1
3 01 223 3 3
5 02 213 3 3
6 08 125 @ @
[trial@smartedu data]$ 
```

3.  使用 tran 表的第 1、2 列来替换 master 表中没有的数据

```shell
[trial@smartedu data]$ ssort -k1 data
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ ssort -k1 tran 
1 01 423
2 04 341
2 03 643
3 01 223
5 02 213
6 08 125
[trial@smartedu data]$ alljoin_default -k1 -i@ -M3 -c1,2 <(ssort -k1 data) <(ssort -k1 tran)
1 2 3 01 423
1 1 1 01 423
1 4 6 01 423
2 2 2 04 341
2 2 2 04 341
2 4 6 04 341
2 1 4 04 341
2 1 3 04 341
2 2 2 03 643
2 2 2 03 643
2 4 6 03 643
2 1 4 03 643
2 1 3 03 643
3 2 1 01 223
3 3 3 01 223
3 2 1 01 223
3 3 3 01 223
5 3 3 02 213
6 6 08 08 125
[trial@smartedu data]$ 
```

# 六、多文件读取

## 1、合并两个表：`append`

1. 必须排序后才可正常使用
2. 根据主键合并两个表

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725160410.png)

### ①、语法

`append –kCOL1[,COL2] MASTER [FILE]`
`append –k 开始的主键列,结束的主键列 MASTER [FILE]`

1. 两个表都指定第一列作为主键列来进行数据的合并

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost cuichangjian]$ append -k1 <(ssort -k1 data) <(ssort -k1 data2)
1 2 3
1 3 3
1 1 1
1 4 6
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1
3 3 3
3 2 1
3 3 3
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
```

### ②、参数

1. -k：指定主键列

## 2、合并两个表并根据主键输出最后一行：`lstd`

1. 必须排序后才可正常使用
2. 与`append`类似，不过只输出每个主键的最后一行

### ①、语法

`lstd –kCOL1[,COL2] MASTER [FILE]`
`lstd –k 开始的主键列,结束的主键列 MASTER [FILE]`

1. 两个表都指定第一列作为主键列来进行数据的合并

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost cuichangjian]$ append -k1 <(ssort -k1 data) <(ssort -k1 data2)
1 2 3
1 3 3
1 1 1
1 4 6
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1
3 3 3
3 2 1
3 3 3
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost cuichangjian]$ lstd -k1 <(ssort -k1 data) <(ssort -k1 data2)
1 4 6 3.445
2 1 4 4.5
3 2 1 53.21
```

### ②、参数

1. -k：指定主键列

## 3、合并多个表：`smerge`

1. 必须排序后才可正常使用
2. 根据主键合并多个表
3. 一般在进行大数据处理时使用

### ①、语法

`smerge –kCOL[,COL] FILE...`
`smerge –k 开始的主键列,结束的主键列 FILE...`

1. 所有表都指定第一列作为主键列来进行数据的合并

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data2
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@localhost cuichangjian]$ ssort -k1 data3
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6
[trial@localhost cuichangjian]$ ssort -k1 master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
[trial@localhost cuichangjian]$ smerge -k1 <(ssort -k1 data) <(ssort -k1 data2) <(ssort -k1 data3) <(ssort -k1 master)
1 2 3
1 3 3
1 1 1
1 4 6
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
1 第一列 2
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
2 1 4 3 3 3
2 1 3 3 2 6
2 第二列 4
3 2 1
3 3 3
3 2 1
3 3 3
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
3 2 1 2 2 2
3 3 3 2 4 6
3 第三列 1
4 第四列 5
```

### ②、参数

1. -k：指定主键列

## 4、输出多个 gz 文件：`zmerge`

#### Ⅰ、语法

`zmerge -k <MergeKey> [-g] [FileList]`
`zmerge -k <压缩时指定的排序的主键> [-g] 文件列表`

#### Ⅱ、参数

1. -k：压缩时指定的排序的主键
2. -g：

#### Ⅲ、说明

1. gz 压缩文件必须已事先排序
2. 所需参数是文件名称而不是数据

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort -k1 data | gzip -f >./zmerge/data.gz
[trial@smartedu data]$ ssort -k1 data2 | gzip -f >./zmerge/data2.gz
[trial@smartedu data]$ ssort -k1 data3 | gzip -f >./zmerge/data3.gz

[trial@smartedu data]$ cd ./zmerge/
[trial@smartedu zmerge]$ ll
total 12
-rw-rw-r--. 1 trial trial 61  8月 29 15:38 data.gz
-rw-rw-r--. 1 trial trial 94  8月 29 15:40 data2.gz
-rw-rw-r--. 1 trial trial 68  8月 29 15:40 data3.gz

[trial@smartedu zmerge]$ zcat data.gz 
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu zmerge]$ zcat data2.gz 
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@smartedu zmerge]$ zcat data3.gz 
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6
[trial@smartedu zmerge]$ zcat data.gz data2.gz data3.gz 
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6

[trial@smartedu zmerge]$ zmerge -k1 <(echo data.gz data2.gz data3.gz | tov)
1 2 3
1 1 1
1 4 6
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
3 2 1
3 3 3
3 2 1
3 3 3
3 2 1 2 2 2
3 3 3 2 4 6
5 3 3
[trial@smartedu zmerge]$ 
```

## 5、输出多个 sn 文件：`snmerge`

#### Ⅰ、语法

`snmerge -k <MergeKey> [-g] [FileList]`
`snmerge -k <压缩时指定的排序的主键> [-g] 文件列表`

#### Ⅱ、参数

1. -k：压缩时指定的排序的主键
2. -g：

#### Ⅲ、说明

1. sn 压缩文件必须已事先排序
2. 所需参数是文件名称而不是数据

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu data]$ ssort -k1 data | snzip >./snmerge/data.sn
[trial@smartedu data]$ ssort -k1 data2 | snzip >./snmerge/data2.sn
[trial@smartedu data]$ ssort -k1 data3 | snzip >./snmerge/data3.sn
[trial@smartedu data]$ cd snmerge/
[trial@smartedu snmerge]$ ll
total 12
-rw-rw-r--. 1 trial trial  72  8月 30 09:19 data.sn
-rw-rw-r--. 1 trial trial 139  8月 30 09:19 data2.sn
-rw-rw-r--. 1 trial trial  86  8月 30 09:19 data3.sn

[trial@smartedu snmerge]$ sncat data.sn 
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu snmerge]$ sncat data2.sn 
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@smartedu snmerge]$ sncat data3.sn 
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6

[trial@smartedu snmerge]$ snmerge -k1 <(echo data.sn data2.sn data3.sn | tov)
1 2 3
1 1 1
1 4 6
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
3 2 1
3 3 3
3 2 1
3 3 3
3 2 1 2 2 2
3 3 3 2 4 6
5 3 3
[trial@smartedu snmerge]$ 
```

## 6、读取多个文件：`jcat`

#### Ⅰ、语法

`jcat [FILE...]`
`jcat 文件1 文件2...`

#### Ⅱ、参数

无

#### Ⅲ、说明

1. 以文件名读取时与 `cat` 相同
2. `jcat` 与 `cat` 都可以读取 `{x,y,z,...}` 这种格式的文件列表
3. `jcat` 可以读取由 `brace` 格式化为 `{x,y,z,...}` 格式的文件列表；但是`cat` 不可以

#### Ⅳ、案例

1. 读取多个文件

```shell
[trial@smartedu data]$ cat master data
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ jcat master data
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ 
```

2. 读取 `{x,y,z,...}` 格式的文件列表

```shell
[trial@smartedu data]$ cat {master,data}
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ jcat {master,data}
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ 
```

3. 读取由 `brace` 格式化为 `{x,y,z,...}` 格式的文件列表

```shell
[trial@smartedu data]$ cat $(echo data data2 | brace)
cat: {data,data2}: No such file or directory
[trial@smartedu data]$ jcat $(echo data data2 | brace)
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
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
[trial@smartedu data]$ 
```

4. 读取不存在的文件，都会报错

```shell
[trial@smartedu data]$ cat master master2
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
cat: master2: No such file or directory
[trial@smartedu data]$ jcat master master2
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
cat: master2: No such file or directory
[trial@smartedu data]$ 
```

## 7、读取多个 gz 文件：`jzcat`

#### Ⅰ、语法

`jzcat [-p] FILE...`
`jzcat [出错时返回0] 文件1 文件2`

#### Ⅱ、参数

1. -p：指定此参数时，即使该命令报错，返回值也是 0

#### Ⅲ、说明

1. 与 `cat` 类似，`cat` 读取普通文件，`jzcat` 读取压缩文件
2. 与 `zmerge` 不同的是 `zmerge` 是按主键输出，`jzcat` 是完整的输出完一个文件再输出下一个文件

#### Ⅳ、案例

1. 一般使用

```shell
[trial@smartedu zmerge]$ ll
total 12
-rw-rw-r--. 1 trial trial 61  8月 29 15:38 data.gz
-rw-rw-r--. 1 trial trial 94  8月 29 15:40 data2.gz
-rw-rw-r--. 1 trial trial 68  8月 29 15:40 data3.gz

[trial@smartedu zmerge]$ cat data.gz 
�3T0R0�B i�`�e1���
                 P���($��m
�h;N

[trial@smartedu zmerge]$ jzcat data.gz
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu zmerge]$ jzcat data.gz data2.gz
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
[trial@smartedu zmerge]$ jzcat data.gz data2.gz data3.gz 
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
1 2 3 3623.13
1 3 3 6.431
1 1 1 40.1312
1 4 6 3.445
2 2 2 53.54
2 2 2 0.042
2 4 6 233.03
2 1 4 4.5
3 2 1 1.15
3 3 3 1.0242
3 2 1 53.21
1 2 3 1 3 3
1 1 1 2 2 2
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
3 2 1 2 2 2
3 3 3 2 4 6
[trial@smartedu zmerge]$ 
```

2. 参数 `-p`

```shell
[trial@smartedu zmerge]$ jzcat data.gz 111
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
gzip: 111.gz: No such file or directory
[trial@smartedu zmerge]$ echo $?
1
[trial@smartedu zmerge]$ jzcat -p data.gz 111
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
gzip: 111.gz: No such file or directory
[trial@smartedu zmerge]$ echo $?
0
[trial@smartedu zmerge]$ 
```

## 8、横向输出多个文件：`hcat`

1. `cat` 输出文件是纵向输出，`hcat` 是横向输出
2. 根据第一个文件行数不同，输出不同

### ①、语法

`hcat FILE...`

1. `cat`

```shell
[trial@localhost data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
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
[trial@localhost data]$ cat data2
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
[trial@localhost data]$ cat master data data2
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
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
```

2. `hcat` 根据第一个文件的行数显示

```shell
[trial@localhost data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
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
[trial@localhost data]$ cat data2
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
[trial@localhost data]$ hcat master data data2
1 第一列 2 3 2 1 3 2 1 1.15
2 第二列 4 2 2 2 2 2 2 53.54
3 第三列 1 1 2 3 1 2 3 3623.13
4 第四列 5 1 3 3 1 3 3 6.431
```

3. `hcat` 根据第一个文件行数不同，输出不同

```shell
[trial@localhost data]$ cat master 
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
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
[trial@localhost data]$ cat data2
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
[trial@localhost data]$ hcat data master data2
3 2 1 1 第一列 2 3 2 1 1.15
2 2 2 2 第二列 4 2 2 2 53.54
1 2 3 3 第三列 1 1 2 3 3623.13
1 3 3 4 第四列 5 1 3 3 6.431
1 1 1 1 1 1 40.1312
2 2 2 2 2 2 0.042
3 3 3 3 3 3 1.0242
2 4 6 2 4 6 233.03
1 4 6 1 4 6 3.445
3 2 1 3 2 1 53.21
2 1 4 2 1 4 4.5
3 3 3
2 1 3
```

### ②、参数

无

## 9、根据路径输出多个文件：`fcat`

1. 输出效果与 `cat` 相同，都是纵向显示
2. 可以输出指定路径下的所有文件

### ①、语法

`fcat -d <directory> [FILE]`

1. 读取命令中的文件名然后输出

```shell
[trial@localhost data]$ ls
data  data2  data3  master  tencd  test_date  tran
[trial@localhost data]$ ls | fcat
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
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
九州B 0049 0056 0153 0006 56016 00001 00020
九州A 0157 0056 0153 0006 56003 00001 00080
九州B 0158 0056 0153 0006 56004 00001 00080
九州B 0178 0056 0153 0006 56011 00001 00060
関東B 0250 0056 0153 0006 56013 00001 00070
九州B 0269 0056 0153 0006 56011 00001 00060
九州B 0282 0056 0153 0006 56014 00001 00020
九州A 0284 0056 0153 0006 56015 00001 00070
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州A 0315 0056 0153 0006 56013 00002 00060
関西 0333 0056 0153 0006 56010 00001 00060
九州B 0049 0056 0153 0005 56011 00003 00040
九州A 0157 0056 0153 0005 56007 00003 00060
九州B 0158 0056 0153 0005 56008 00003 00060
九州B 0178 0056 0153 0005 56008 00002 00050
関東B 0250 0056 0153 0005 56009 00003 00040
九州B 0269 0056 0153 0005 56007 00003 00040
九州B 0282 0056 0153 0005 56010 00003 00040
九州A 0284 0056 0153 0005 56010 00003 00050
関西 0299 0056 0153 0005 56007 00003 00040
九州B 0309 0056 0153 0005 56009 00003 00040
九州A 0315 0056 0153 0005 56009 00004 00030
関西 0333 0056 0153 0005 56007 00003 00060
九州B 0049 0056 0153 0005 56011 00003 00030
九州A 0157 0056 0153 0005 56007 00003 00070
九州B 0158 0056 0153 0005 56008 00003 00070
九州B 0178 0056 0153 0005 56008 00002 00040
関東B 0250 0056 0153 0005 56009 00003 00050
九州B 0269 0056 0153 0005 56007 00003 00030
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州a 0315 0056 0153 0006 56013 00002 00060
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
1 01 423
3 01 223
5 02 213
2 04 341
2 03 643
```

2. 读取文件中的文件名然后输出

```shell
[trial@localhost data]$ ls > lsName
[trial@localhost data]$ cat lsName 
data
data2
data3
lsName
master
tencd
test_date
tran
[trial@localhost data]$ fcat lsName 
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
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
data
data2
data3
lsName
master
tencd
test_date
tran
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
九州B 0049 0056 0153 0006 56016 00001 00020
九州A 0157 0056 0153 0006 56003 00001 00080
九州B 0158 0056 0153 0006 56004 00001 00080
九州B 0178 0056 0153 0006 56011 00001 00060
関東B 0250 0056 0153 0006 56013 00001 00070
九州B 0269 0056 0153 0006 56011 00001 00060
九州B 0282 0056 0153 0006 56014 00001 00020
九州A 0284 0056 0153 0006 56015 00001 00070
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州A 0315 0056 0153 0006 56013 00002 00060
関西 0333 0056 0153 0006 56010 00001 00060
九州B 0049 0056 0153 0005 56011 00003 00040
九州A 0157 0056 0153 0005 56007 00003 00060
九州B 0158 0056 0153 0005 56008 00003 00060
九州B 0178 0056 0153 0005 56008 00002 00050
関東B 0250 0056 0153 0005 56009 00003 00040
九州B 0269 0056 0153 0005 56007 00003 00040
九州B 0282 0056 0153 0005 56010 00003 00040
九州A 0284 0056 0153 0005 56010 00003 00050
関西 0299 0056 0153 0005 56007 00003 00040
九州B 0309 0056 0153 0005 56009 00003 00040
九州A 0315 0056 0153 0005 56009 00004 00030
関西 0333 0056 0153 0005 56007 00003 00060
九州B 0049 0056 0153 0005 56011 00003 00030
九州A 0157 0056 0153 0005 56007 00003 00070
九州B 0158 0056 0153 0005 56008 00003 00070
九州B 0178 0056 0153 0005 56008 00002 00040
関東B 0250 0056 0153 0005 56009 00003 00050
九州B 0269 0056 0153 0005 56007 00003 00030
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州a 0315 0056 0153 0006 56013 00002 00060
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
1 01 423
3 01 223
5 02 213
2 04 341
2 03 643
```

3. 添加参数 `-d`，添加路径

```shell
[trial@localhost data]$ pwd
/home/trial/work/cuichangjian/data
[trial@localhost data]$ cd /home/trial/work/cuichangjian
[trial@localhost cuichangjian]$ ls ./data
data  data2  data3  lsName  master  tencd  test_date  tran
[trial@localhost cuichangjian]$ ls ./data | fcat -d ./data/
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
3 2 1 2 2 2
1 2 3 1 3 3
1 1 1 2 2 2
3 3 3 2 4 6
1 4 6 3 2 1
2 1 4 3 3 3
2 1 3 3 2 6
data
data2
data3
lsName
master
tencd
test_date
tran
1111111111111111
1 第一列 2
2 第二列 4
3 第三列 1
4 第四列 5
九州B 0049 0056 0153 0006 56016 00001 00020
九州A 0157 0056 0153 0006 56003 00001 00080
九州B 0158 0056 0153 0006 56004 00001 00080
九州B 0178 0056 0153 0006 56011 00001 00060
関東B 0250 0056 0153 0006 56013 00001 00070
九州B 0269 0056 0153 0006 56011 00001 00060
九州B 0282 0056 0153 0006 56014 00001 00020
九州A 0284 0056 0153 0006 56015 00001 00070
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州A 0315 0056 0153 0006 56013 00002 00060
関西 0333 0056 0153 0006 56010 00001 00060
九州B 0049 0056 0153 0005 56011 00003 00040
九州A 0157 0056 0153 0005 56007 00003 00060
九州B 0158 0056 0153 0005 56008 00003 00060
九州B 0178 0056 0153 0005 56008 00002 00050
関東B 0250 0056 0153 0005 56009 00003 00040
九州B 0269 0056 0153 0005 56007 00003 00040
九州B 0282 0056 0153 0005 56010 00003 00040
九州A 0284 0056 0153 0005 56010 00003 00050
関西 0299 0056 0153 0005 56007 00003 00040
九州B 0309 0056 0153 0005 56009 00003 00040
九州A 0315 0056 0153 0005 56009 00004 00030
関西 0333 0056 0153 0005 56007 00003 00060
九州B 0049 0056 0153 0005 56011 00003 00030
九州A 0157 0056 0153 0005 56007 00003 00070
九州B 0158 0056 0153 0005 56008 00003 00070
九州B 0178 0056 0153 0005 56008 00002 00040
関東B 0250 0056 0153 0005 56009 00003 00050
九州B 0269 0056 0153 0005 56007 00003 00030
関西 0299 0056 0153 0006 56011 00001 00070
九州B 0309 0056 0153 0006 56020 00001 00010
九州a 0315 0056 0153 0006 56013 00002 00060
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
1 01 423
3 01 223
5 02 213
2 04 341
2 03 643
```

### ②、参数

1. -d：指定文件名所在的位置

# 七、日期处理

## 1、日期操作：`sdate`

### ①、语法

`sdate [option] 指定日期`
`sdate [参数] 指定日期`

### ②、参数

1. `-d`：输出日期列表
   1. `<yyyyww>w`：指定第几周，输出这个周所在的日期

```shell
[trial@localhost cuichangjian]$ sdate -d 202201w
20211227 20211228 20211229 20211230 20211231 20220101 20220102
```

   2. `<yyyymm>m`：指定月，输出日

```shell
[trial@localhost cuichangjian]$ sdate -d 202201m
20220101 20220102 20220103 20220104 20220105 20220106 20220107 20220108 20220109 20220110 20220111 20220112 20220113 20220114 20220115 20220116 20220117 20220118 20220119 20220120 20220121 20220122 20220123 20220124 20220125 20220126 20220127 20220128 20220129 20220130 20220131
```

   3. 对文件中的数据进行处理，`3w`：文件中的第三列，指定为周

```shell
[trial@localhost cuichangjian]$ cat test_date 
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
[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate -d 1w
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160111 20160112
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160114 20160115
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160117 20160118
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160120 20160121
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160123 20160124
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160126 20160127
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160129 20160130
201601 20151228 20151229 20151230 20151231 20160101 20160102 20160103 20160201 20160202
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160204 20160205
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160207 20160208
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160210 20160211
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160213 20160214
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160216 20160217
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160219 20160220
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160222 20160223
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160225 20160226
201602 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160228 20160229
201603 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate -d 1m
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160111 20160112
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160114 20160115
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160117 20160118
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160120 20160121
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160123 20160124
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160126 20160127
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160129 20160130
201601 20160101 20160102 20160103 20160104 20160105 20160106 20160107 20160108 20160109 20160110 20160111 20160112 20160113 20160114 20160115 20160116 20160117 20160118 20160119 20160120 20160121 20160122 20160123 20160124 20160125 20160126 20160127 20160128 20160129 20160130 20160131 20160201 20160202
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160204 20160205
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160207 20160208
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160210 20160211
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160213 20160214
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160216 20160217
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160219 20160220
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160222 20160223
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160225 20160226
201602 20160201 20160202 20160203 20160204 20160205 20160206 20160207 20160208 20160209 20160210 20160211 20160212 20160213 20160214 20160215 20160216 20160217 20160218 20160219 20160220 20160221 20160222 20160223 20160224 20160225 20160226 20160227 20160228 20160229 20160228 20160229
201603 20160301 20160302 20160303 20160304 20160305 20160306 20160307 20160308 20160309 20160310 20160311 20160312 20160313 20160314 20160315 20160316 20160317 20160318 20160319 20160320 20160321 20160322 20160323 20160324 20160325 20160326 20160327 20160328 20160329 20160330 20160331 20160302 20160303
```

2. `-w`：指定的日期是那一年的第几周，格式：202232，即 2022 年的第32 周；对文件中的数据进行处理，`3d`：文件中的第三列，指定为日

```shell
[trial@localhost cuichangjian]$ sdate -w today
202232

[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate -w 3d
20160110 20160111 20160112 201603
20160113 20160114 20160115 201603
20160116 20160117 20160118 201604
20160119 20160120 20160121 201604
20160122 20160123 20160124 201604
20160125 20160126 20160127 201605
20160128 20160129 20160130 201605
20160131 20160201 20160202 201606
20160203 20160204 20160205 201606
20160206 20160207 20160208 201607
20160209 20160210 20160211 201607
20160212 20160213 20160214 201607
20160215 20160216 20160217 201608
20160218 20160219 20160220 201608
20160221 20160222 20160223 201609
20160224 20160225 20160226 201609
20160227 20160228 20160229 201610
20160301 20160302 20160303 201610
```

3. `-y`：指定的日期是星期几；对文件中的数据进行处理，`3d`：文件中的第三列，指定为日

```shell
[trial@localhost cuichangjian]$ sdate -y today
5

[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate -y 3d
20160110 20160111 20160112 2
20160113 20160114 20160115 5
20160116 20160117 20160118 1
20160119 20160120 20160121 4
20160122 20160123 20160124 7
20160125 20160126 20160127 3
20160128 20160129 20160130 6
20160131 20160201 20160202 2
20160203 20160204 20160205 5
20160206 20160207 20160208 1
20160209 20160210 20160211 4
20160212 20160213 20160214 7
20160215 20160216 20160217 3
20160218 20160219 20160220 6
20160221 20160222 20160223 2
20160224 20160225 20160226 5
20160227 20160228 20160229 1
20160301 20160302 20160303 4
```

4. `-e`：输出指定日期范围的日期列表
   1. `<yyyymmdd>` 或 `<yyyymmdd>d`：输出天数

```shell
[trial@localhost cuichangjian]$ sdate -e 20110101d 20110201d
20110101 20110102 20110103 20110104 20110105 20110106 20110107 20110108 20110109 20110110 20110111 20110112 20110113 20110114 20110115 20110116 20110117 20110118 20110119 20110120 20110121 20110122 20110123 20110124 20110125 20110126 20110127 20110128 20110129 20110130 20110131 20110201
```

   2. `<yyyyww>w`：指定周
   3. `<yyyymm>m`：指定月
5. `-lwd`：指定日期的去年同周同星期几是哪一天；对文件中的数据进行处理，`3d`：文件中的第三列

```shell
[trial@localhost cuichangjian]$ sdate -lwd today
20210809
[trial@localhost cuichangjian]$ sdate -lwd 20220808
20210809

[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate -lwd 3d
20160110 20160111 20160112 20150113
20160113 20160114 20160115 20150116
20160116 20160117 20160118 20150119
20160119 20160120 20160121 20150122
20160122 20160123 20160124 20150125
20160125 20160126 20160127 20150128
20160128 20160129 20160130 20150131
20160131 20160201 20160202 20150203
20160203 20160204 20160205 20150206
20160206 20160207 20160208 20150209
20160209 20160210 20160211 20150212
20160212 20160213 20160214 20150215
20160215 20160216 20160217 20150218
20160218 20160219 20160220 20150221
20160221 20160222 20160223 20150224
20160224 20160225 20160226 20150227
20160227 20160228 20160229 20150302
20160301 20160302 20160303 20150305
```

6. `/±`：根据指定日期进行加减运算
   1. `<yyyymmdd>` 或 `<yyyymmdd>d`：计算日期

```shell
[trial@localhost cuichangjian]$ sdate 20220808/+2
20220810
[trial@localhost cuichangjian]$ sdate 20220808/-2
20220806
[trial@localhost cuichangjian]$ sdate 20220808d/+2
20220810
[trial@localhost cuichangjian]$ sdate 20220808d/-2
20220806
```

   2. `<yyyymm>m`：计算月

```shell
[trial@localhost cuichangjian]$ sdate 202208m/-2
202206
[trial@localhost cuichangjian]$ sdate 202208m/+2
202210
```

   3. `<yyyyww>w`：计算周

```shell
[trial@localhost cuichangjian]$ sdate 202220w/+2
202222
[trial@localhost cuichangjian]$ sdate 202220w/-2
202218
```

   4. 对文件中的数据进行处理，`3d/+2`：文件中的第三列，指定为日，每个数据都加两天

```shell
[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate 3d/+2
20160110 20160111 20160112 20160114
20160113 20160114 20160115 20160117
20160116 20160117 20160118 20160120
20160119 20160120 20160121 20160123
20160122 20160123 20160124 20160126
20160125 20160126 20160127 20160129
20160128 20160129 20160130 20160201
20160131 20160201 20160202 20160204
20160203 20160204 20160205 20160207
20160206 20160207 20160208 20160210
20160209 20160210 20160211 20160213
20160212 20160213 20160214 20160216
20160215 20160216 20160217 20160219
20160218 20160219 20160220 20160222
20160221 20160222 20160223 20160225
20160224 20160225 20160226 20160228
20160227 20160228 20160229 20160302
20160301 20160302 20160303 20160305
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate 3w/+2
20160110 20160111 201601 201603
20160113 20160114 201601 201603
20160116 20160117 201601 201603
20160119 20160120 201601 201603
20160122 20160123 201601 201603
20160125 20160126 201601 201603
20160128 20160129 201601 201603
20160131 20160201 201602 201604
20160203 20160204 201602 201604
20160206 20160207 201602 201604
20160209 20160210 201602 201604
20160212 20160213 201602 201604
20160215 20160216 201602 201604
20160218 20160219 201602 201604
20160221 20160222 201602 201604
20160224 20160225 201602 201604
20160227 20160228 201602 201604
20160301 20160302 201603 201605
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate 3m/+2
20160110 20160111 201601 201602
20160113 20160114 201601 201602
20160116 20160117 201601 201602
20160119 20160120 201601 201602
20160122 20160123 201601 201603
20160125 20160126 201601 201603
20160128 20160129 201601 201603
20160131 20160201 201602 201602
20160203 20160204 201602 201602
20160206 20160207 201602 201602
20160209 20160210 201602 201603
20160212 20160213 201602 201603
20160215 20160216 201602 201603
20160218 20160219 201602 201603
20160221 20160222 201602 201604
20160224 20160225 201602 201604
20160227 20160228 201602 201604
20160301 20160302 201603 201603
```

   5. 对文件中的数据进行处理，`3d +4`：文件中的第三列，指定为日，每个数据都加上第四列的数据

```shell
[trial@localhost cuichangjian]$ cat test_date 
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
[trial@localhost cuichangjian]$ sdate 3d +4 test_date 
20160110 20160111 20160112 1111 20190127
20160113 20160114 20160115 1111 20190130
20160116 20160117 20160118 1111 20190202
20160119 20160120 20160121 1111 20190205
20160122 20160123 20160124 1111 20190208
20160125 20160126 20160127 1111 20190211
20160128 20160129 20160130 1111 20190214
20160131 20160201 20160202 1111 20190217
20160203 20160204 20160205 1111 20190220
20160206 20160207 20160208 1111 20190223
20160209 20160210 20160211 1111 20190226
20160212 20160213 20160214 1111 20190301
20160215 20160216 20160217 1111 20190304
20160218 20160219 20160220 1111 20190307
20160221 20160222 20160223 1111 20190310
20160224 20160225 20160226 1111 20190313
20160227 20160228 20160229 1111 20190316
20160301 20160302 20160303 1111 20190319
```

7. 计算相差天数；
   1. 要前大后小，不然计算出来是负数

```shell
[trial@localhost cuichangjian]$ sdate 20110101 20110201
-31
[trial@localhost cuichangjian]$ sdate 20110101d 20110201d
-31
```

   2. 对文件中的数据进行处理，`2d 3d`：文件中的第二列、第三列

```shell
[trial@localhost cuichangjian]$ selcol -c1,3 test_date
20160110 20160111 20160112
20160113 20160114 20160115
20160116 20160117 20160118
20160119 20160120 20160121
20160122 20160123 20160124
20160125 20160126 20160127
20160128 20160129 20160130
20160131 20160201 20160202
20160203 20160204 20160205
20160206 20160207 20160208
20160209 20160210 20160211
20160212 20160213 20160214
20160215 20160216 20160217
20160218 20160219 20160220
20160221 20160222 20160223
20160224 20160225 20160226
20160227 20160228 20160229
20160301 20160302 20160303
[trial@localhost cuichangjian]$ selcol -c1,3 test_date | sdate 2d 3d
20160110 20160111 20160112 -1
20160113 20160114 20160115 -1
20160116 20160117 20160118 -1
20160119 20160120 20160121 -1
20160122 20160123 20160124 -1
20160125 20160126 20160127 -1
20160128 20160129 20160130 -1
20160131 20160201 20160202 -1
20160203 20160204 20160205 -1
20160206 20160207 20160208 -1
20160209 20160210 20160211 -1
20160212 20160213 20160214 -1
20160215 20160216 20160217 -1
20160218 20160219 20160220 -1
20160221 20160222 20160223 -1
20160224 20160225 20160226 -1
20160227 20160228 20160229 -1
20160301 20160302 20160303 -1
```

### ③、指定日期的命令

1. today：今天

```shell
[trial@localhost cuichangjian]$ sdate today
20220808
```

2. yesterday / yday：昨天（前一天）
3. tomorrow / nday：明天（后一天）
4. thisweek：今年的第几周，格式：202232，即 2022 年的第 32 周
5. thismonth：今年的第几月，格式：202208，即 2022 年的 8 月
6. thisyobi：今天是星期几

## 2、判断指定的字符串是否为日期：`isdate`

1. `echo $?`：查看命令执行成功与否
   1. 当一个进程执行完毕时，该进程会调用一个名为 _exit 的例程来通知内核它已经做好“消亡”的准备了。该进程会提供一个退出码（一个整数）表明它准备退出的原因
   2. 按照惯例，0 用来表示正常的或者说“成功”的终止；非0表示失败，具体是几由之前执行的进程决定
   3. 也就是说我们在执行 echo $? 时反回的值就是进程的退出码。而且，这个退出码是由刚刚执行完的进程提供给系统内核的
2. `isdate`：判断指定的字符串是否为日期

### ①、语法

`isdate <date>`
`isdate 字符串`

1. 使用 `isdate` 判断指定的字符串是否为日期，然后使用 `echo $?` 查看命令执行成功与否

```shell
[trial@localhost cuichangjian]$ isdate 20090101
[trial@localhost cuichangjian]$ echo $?
0
[trial@localhost cuichangjian]$ isdate 2009010
[trial@localhost cuichangjian]$ echo $?
1
```

### ②、参数

无

## 3、

# 八、数据压缩和解压缩

## 1、压缩成 SMART-ZIP：`szip`

1. 排序后才可使用此命令，且排序的主键列要和压缩指定的主键列相同
2. smart 自己的压缩方式，要使用 `scat` 读取

### ①、语法

`szip NEWPATH.%c [FILE]`
`szip 生成的文件.%指定分割依据的列 [FILE]`

1. 使用 % 指定分割的主键列

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | szip ./new/data.%1
[trial@localhost cuichangjian]$ ll ./new
total 24
-rw-rw-r-- 1 trial trial 27 Aug  5 17:25 data.1
-rw-rw-r-- 1 trial trial  7 Aug  5 17:25 data.1.IDX
-rw-rw-r-- 1 trial trial 28 Aug  5 17:25 data.2
-rw-rw-r-- 1 trial trial  7 Aug  5 17:25 data.2.IDX
-rw-rw-r-- 1 trial trial 21 Aug  5 17:25 data.3
-rw-rw-r-- 1 trial trial  7 Aug  5 17:25 data.3.IDX
[trial@localhost cuichangjian]$ cat ./new/data.1
x3T0R0�0��
[trial@localhost cuichangjian]$ scat ./new/data.1
1 2 3
1 3 3
1 1 1
1 4 6
```

### ②、参数

无

## 2、读取 SMART-ZIP：`scat`

读取 smart 自己的压缩文件

### ①、语法

`scat [FILE]`

### ②、参数

好像无

## 3、排序和压缩：`exchsort、exchcat`

### ①、语法

`exchsort -k<列番号[,列番号]> [FILE]`
`exchsort -k 指定开始的主键列,指定结束的主键列 > 文件名.exch`

---

`exchcat [FILE]`
`exchcat 文件名`

### ②、参数

1. exchsort -k：指定主键列

### ③、说明

1. `exchsort` 可将文件压缩，`-k` 指定的列会自动排序，生成的文件后缀名需为：`.exch`
2. `exchcat` 可读取被 `exchsort` 命令压缩的文件
3. 低内存也能执行
4. 需要配合 groupsort 执行，因为key不能超 1w

### ④、案例

1. 指定一列主键

```shell
[trial@smartedu data]$ mkdir exchsorttest
[trial@smartedu data]$ exchsort -k1 > exchsorttest/test.exch data
[trial@smartedu data]$ exchcat ./exchsorttest/test.exch 
1 2 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
5 3 3
[trial@smartedu data]$ 
```

2. 指定三列主键

```shell
[trial@smartedu data]$ exchsort -k1,3 > exchsorttest/test2.exch data
[trial@smartedu data]$ exchcat ./exchsorttest/test2.exch 
1 1 1
1 2 3
1 4 6
2 1 3
2 1 4
2 2 2
2 2 2
2 4 6
3 2 1
3 2 1
3 3 3
3 3 3
5 3 3
[trial@smartedu data]$ 
```

# 九、数据获取和传出

## 1、根据主键获取数据：`readvalue`

1. 不排序也可使用
2. 根据主键获取数据，输出的数据不显示主键，某些数据为空时默认以 `_` 填充，可使用参数 `-i` 指定填充符号

### ①、语法

`readvalue -i <String> -l <String> -u <Name> [FILE]`
`readvalue -i 数据为空时的填充符号 -l 不止一列时列数据之间的连接符 -u 主键名 [FILE]`

1. 根据主键获取数据

```shell
[trial@localhost data]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | readvalue -u1
2 3
3 3
1 1
4 6
```

2. 指定列数据之间的连接符

```shell
[trial@localhost cuichangjian]$ ssort -k1 data
1 2 3
1 3 3
1 1 1
1 4 6
2 2 2
2 2 2
2 4 6
2 1 4
2 1 3
3 2 1
3 3 3
3 2 1
3 3 3
[trial@localhost cuichangjian]$ ssort -k1 data | readvalue -l@ -u1
2@3
3@3
1@1
4@6
```

3. 指定数据为空时的填充符号

```shell
[trial@tfs tmp]$ cat master_yu
001 01 a
001 01 b
001 02 a
001 02 b
002 01 a
002 01 b
002 02 a
002 02 b
001
[trial@tfs tmp]$ cat master_yu|readvalue -u 001
01 a
01 b
02 a
02 b
_
[trial@tfs tmp]$ cat master_yu|readvalue -i@ -u 001
01 a
01 b
02 a
02 b
@
```

### ②、参数

1. -u：指定主键名称
2. -l：指定列数据之间的连接符
3. -i：指定数据为空时的填充符号

## 2、根据主键从多个文件中获取数据：`readvalues`

1. 该命令是从文件中获取数据，所以需要的参数是文件名，而不是数据
2. 所以要写成这种方式：`readvalues <(echo 主键) <(echo 文件1 文件2 | tov)`
3. 文件名参数要使用 `tov` 转成列，这样才会显示所有文件里的 value；否则只会显示最后一个文件里的 value
4. 与 `readvalue` 不同的是 `readvalue` 可以读取一个文件里相同 key 的所有 value，`readvalues` 只能读取每个数据文件里的指定 key 的最后一个 alue 值

### ①、语法

`readvalues FIELD_NAME_FILE FILE_LIST`
`readvalues 键 文件名`

1. 一般用法

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ cat data2
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
[trial@smartedu data]$ readvalues <(echo 1) <(echo data data2 | tov)
1
4 6
4 6 3.445
[trial@smartedu data]$ 
```

### ②、参数

无

## 3

# 十、进程，等待，重试

## 1、文件锁：`lock`

1. 一般是用来锁定脚本，在使用期间使其他人不能更改
2. 脚本调用完毕后要使用 `unlock` 来解除锁定

### ①、语法

`lock -f FILE -t TIMEOUT -i INVALIDTIME`
`lock -f 想要锁定的文件 -t TIMEOUT -i INVALIDTIME`

### ②、参数

1. -f：想要锁定的文件
2. -t：加锁等待的时间，超过时间等不到文件（被别的锁锁住了）会退出
3. -i：无效时间，锁的失效时间，超过会被别的锁覆盖，取消锁定（一般使用）

## 2、解除文件锁：`unlock`

1. 使被文件锁 `lock` 锁定的文件解锁
2. 被锁定的文件最后一定要使用 `unlock` 解锁

### ①、语法

`unlock -f FILE`
`unlock -f 想要解除锁定的文件`

### ②、参数

1. -f：想要解除锁定的文件

## 3、等待文件创建完成：`swait`

1. `-e` ：等不到文件就报错，时间由参数 `-T` 和 `-D` 设定
2. 不指定参数 `-e`，则参数 `-T` 和 `-D` 设定的时间过了会继续往下执行

### ①、语法

`swait -f FILE -e EXIT_FILE -T HHMM [-D YYYYMMDD]`
`swait -f 等待的文件 -e 抛出的错误 -T 等待的时间（年月日） [-D 等待的时间（时分秒）]`

### ②、参数

1. -f：等待的文件
2. -e：等待不到文件时抛出的错误，会使脚本停止
3. -T：等待的时间（年月日）
4. -D：等待的时间（时分秒）

## 4、报错：`errchk`

1. 检查管道执行结果，如果代码出现执行错误，会在 `errchk` 处报错
2. 可以当作 debug 使用

### ①、语法

`errchk v1 v2 ...`

### ②、参数

无

## 5、并行运行：`sparallel`

1. 可同时运行多个脚本

### ①、语法

`sparallel -n <Num> PROGRAM:%1%2...%9 [FILE]`
`sparallel -n 同时运行的脚本数量 执行的脚本名称:%1%2...%9 [参数1,参数2...参数9]`

### ②、参数

1. -n：同时运行的脚本数量
2. PROGRAM：执行的脚本名称
3. %1%2...%9：传递的参数的占位符，与后面的参数一致
4. FILE：传递的参数

## 6、

# 十一、ins插入新列

## 1、添加排名次：`insrank`

1. 排序后才可正常使用，若不指定主键列，则排序的主键列要和比较列相同
2. 不指定主键列：`ssort -k1 data | insrank -c1`
3. 
- 在最前面添加排名（编号），从高到低依次排列，排序主键列（排名比较列）相同的编号也相同（并列），但是编号依然会向下顺延一位，直到不同的排序主键列（排名比较列）出现时再赋予新编号

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insrank -c1
1 1 2 3
1 1 3 3
1 1 1 1
1 1 4 6
5 2 2 2
5 2 2 2
5 2 4 6
5 2 1 4
9 3 2 1
9 3 3 3
9 3 2 1
```

3. 指定主键列：`ssort -k1 data | insrank -k1 -c2`

- 根据指定的主键列在最前面添加排名（编号），从高到低依次排列，每个主键列单独编号，主键列变了就重新从 1 开始
- 比较列相同的编号也相同（并列），但是编号依然会向下顺延一位，直到不同的比较列出现时再赋予新编号

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insrank -k1 -c2
1 1 2 3
2 1 3 3
3 1 1 1
4 1 4 6
1 2 2 2
1 2 2 2
3 2 4 6
4 2 1 4
1 3 2 1
2 3 3 3
3 3 2 1
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725160903.png)

### ①、语法

`insrank [-kCOL1[,COL2]] -cCOL [FILE]`
`insrank [-k 开始的主键列,结束的主键列] -c 比较列 文件`

### ②、参数

1. -c：指定比较列，即排名是不是相同
2. -k：指定主键列，即会不会重新编号

## 2、添加行编号：`insseq`

根据主键添加排名，不同的主键列重新从 1 开始计数

1. 若不指定主键列的话，结果是在最前面添加从 1 开始的序号，不论排序与否

```shell
[trial@localhost cuichangjian]$ insseq data
1 3 2 1
2 2 2 2
3 1 2 3
4 1 3 3
5 1 1 1
6 2 2 2
7 3 3 3
8 2 4 6
9 1 4 6
10 3 2 1
11 2 1 4
[trial@localhost cuichangjian]$ ssort -k1 data | insseq
1 1 2 3
2 1 3 3
3 1 1 1
4 1 4 6
5 2 2 2
6 2 2 2
7 2 4 6
8 2 1 4
9 3 2 1
10 3 3 3
11 3 2 1
```

2. 若指定主键列且排序的话，要使排序的主键列和指定的主键列一致，结果是在最前面添加从 1 开始的序号，相同的主键列从高到低，不同的主键列重新从 1 开始计数

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insseq -k1
1 1 2 3
2 1 3 3
3 1 1 1
4 1 4 6
1 2 2 2
2 2 2 2
3 2 4 6
4 2 1 4
1 3 2 1
2 3 3 3
3 3 2 1
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725160938.png)

### ①、语法

`insseq [-kCOL1[,COL2]] [FILE]`
`insseq [-k 开始的主键列,结束的主键列] [FILE]`

### ②、参数

1. -k：指定主键列，即会不会根据主键重新编号

## 3、计算累计和：`inssum`

1. 排序后才可以正常使用
2. 根据指定的主键求指定列的和，将和放到指定列的后面
3. 不指定主键则是求这一列所有数据的和
4. 每一列的和会单独计算
5. 相同主键列的每一行的累计和相同

### ①、语法

`inssum [-sNUM] [-kCOL1[,COL2]] -cCOL1[,COL2] [FILE]`
`inssum [-s 指定小数位数] [-k 指定开始的主键列,指定结束的主键列] -c 指定开始求和的列,指定结束求和的列 文件`

1. 指定第一列为主键列，求第三列的和

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ ssort -k1 data | inssum -k1 -c3
1 2 3 13
1 3 3 13
1 1 1 13
1 4 6 13
2 2 2 17
2 2 2 17
2 4 6 17
2 1 4 17
2 1 3 17
3 2 1 8
3 3 3 8
3 2 1 8
3 3 3 8
[trial@smartedu data]$
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161049.png)

2. 指定第一列为主键列，求第二列和第三列的和

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ ssort -k1 data | inssum -k1 -c2,3
1 2 10 3 13
1 3 10 3 13
1 1 10 1 13
1 4 10 6 13
2 2 10 2 17
2 2 10 2 17
2 4 10 6 17
2 1 10 4 17
2 1 10 3 17
3 2 10 1 8
3 3 10 3 8
3 2 10 1 8
3 3 10 3 8
[trial@smartedu data]$ 
```

### ②、参数

1. -k：指定主键列
2. -c：指定求和的列

## 4、计算构成比：`insratio`

1. 构成比 = 某事物内部某一部分的数量 / 同一事物内部的整体数量 * %，即：这一列的每个数 / 这一列的总和 * %
2. 构成比反映的是事物静止状态内部构成成分占全体的比重，取值仅在0~1之间
3. 若是指定主键列，则最好排序后使用，且排序的主键列要和求构成比指定的主键列相同

### ①、语法

`insratio [-sNUM] [-kCOL1[,COL2]] -cCOL1[,COL2] [FILE]`
`insratio [-s 小数位数] [-k 开始的主键列,结束的主键列] -c 开始的计算列,结束的计算列 文件`

1. 不排序、不指定主键列求构成比：`insratio -c3 data`，是这一列的每个数 / 这一列的总数

```shell
[trial@localhost cuichangjian]$ insratio -c3 data
3 2 1 3.1
2 2 2 6.3
1 2 3 9.4
1 3 3 9.4
1 1 1 3.1
2 2 2 6.3
3 3 3 9.4
2 4 6 18.8
1 4 6 18.8
3 2 1 3.1
2 1 4 12.5
```

2. 排序、不指定主键列求构成比：`ssort -k1 data | insratio -c3`，是这一列的每个数 / 这一列的总数

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -c3
1 2 3 9.4
1 3 3 9.4
1 1 1 3.1
1 4 6 18.8
2 2 2 6.3
2 2 2 6.3
2 4 6 18.8
2 1 4 12.5
3 2 1 3.1
3 3 3 9.4
3 2 1 3.1
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -c1
1 4.8 2 3
1 4.8 3 3
1 4.8 1 1
1 4.8 4 6
2 9.5 2 2
2 9.5 2 2
2 9.5 4 6
2 9.5 1 4
3 14.3 2 1
3 14.3 3 3
3 14.3 2 1
```

3. 排序、不指定主键列、设置小数位数求构成比：`ssort -k1 data | insratio -s15 -c1`，是这一列的每个数 / 这一列的总数

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -s15 -c1
1 4.761904761904762 2 3
1 4.761904761904762 3 3
1 4.761904761904762 1 1
1 4.761904761904762 4 6
2 9.523809523809524 2 2
2 9.523809523809524 2 2
2 9.523809523809524 4 6
2 9.523809523809524 1 4
3 14.285714285714286 2 1
3 14.285714285714286 3 3
3 14.285714285714286 2 1
```

4. 排序、指定主键列、设置小数位数求多个构成比：`ssort -k1 data | insratio -s15 -k1 -c1,3`，是相同主键的每个数 / 相同主键相加的总数；每个主键单独计算

```shell
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -s15 -k1 -c1
1 25.000000000000000 2 3
1 25.000000000000000 3 3
1 25.000000000000000 1 1
1 25.000000000000000 4 6
2 25.000000000000000 2 2
2 25.000000000000000 2 2
2 25.000000000000000 4 6
2 25.000000000000000 1 4
3 33.333333333333333 2 1
3 33.333333333333333 3 3
3 33.333333333333333 2 1
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -s15 -k1 -c2
1 2 20.000000000000000 3
1 3 30.000000000000000 3
1 1 10.000000000000000 1
1 4 40.000000000000000 6
2 2 22.222222222222222 2
2 2 22.222222222222222 2
2 4 44.444444444444444 6
2 1 11.111111111111111 4
3 2 28.571428571428571 1
3 3 42.857142857142857 3
3 2 28.571428571428571 1
[trial@localhost cuichangjian]$ ssort -k1 data | insratio -s15 -k1 -c1,3
1 25.000000000000000 2 20.000000000000000 3 23.076923076923077
1 25.000000000000000 3 30.000000000000000 3 23.076923076923077
1 25.000000000000000 1 10.000000000000000 1 7.692307692307692
1 25.000000000000000 4 40.000000000000000 6 46.153846153846154
2 25.000000000000000 2 22.222222222222222 2 14.285714285714286
2 25.000000000000000 2 22.222222222222222 2 14.285714285714286
2 25.000000000000000 4 44.444444444444444 6 42.857142857142857
2 25.000000000000000 1 11.111111111111111 4 28.571428571428571
3 33.333333333333333 2 28.571428571428571 1 20.000000000000000
3 33.333333333333333 3 42.857142857142857 3 60.000000000000000
3 33.333333333333333 2 28.571428571428571 1 20.000000000000000
```

### ②、参数

1. -c：指定计算构成比的列
2. -k：指定主键列
3. -s：指定显示的小数位数，可以指定 0-15，不设置这个参数则是默认显示 1位小数

## 5、添加星期几：`insweek`

不加参数 -j 和 -e 则显示：1、2、3、4、5、6、7 这种星期几
数据的格式必须是正确的时间格式才可以使用此命令

- 8 位：YYYYMMDD
- 12 位：YYYYMMDDHHMM
- 14 位：YYYYMMDDHHMMSS

```shell
[trial@localhost cuichangjian]$ cat test_date 
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
```

### ①、语法

`insweek -j|e -cCOL1[,COL2]... [FILE]`
`insweek 日语|英语（显示哪种星期几） -c 开始的列数,结束的列数 ... 文件`

1. 默认显示数字格式

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
[trial@localhost data]$ insweek -c1 test_date 
20160110 7 20160111 20160112 1111
20160113 3 20160114 20160115 1111
20160116 6 20160117 20160118 1111
20160119 2 20160120 20160121 1111
20160122 5 20160123 20160124 1111
20160125 1 20160126 20160127 1111
20160128 4 20160129 20160130 1111
20160131 7 20160201 20160202 1111
20160203 3 20160204 20160205 1111
20160206 6 20160207 20160208 1111
20160209 2 20160210 20160211 1111
20160212 5 20160213 20160214 1111
20160215 1 20160216 20160217 1111
20160218 4 20160219 20160220 1111
20160221 7 20160222 20160223 1111
20160224 3 20160225 20160226 1111
20160227 6 20160228 20160229 1111
20160301 2 20160302 20160303 1111
```

2. `-j` 显示日语格式

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
[trial@localhost data]$ insweek -j -c1,3 test_date 
20160110 日 20160111 月 20160112 火 1111
20160113 水 20160114 木 20160115 金 1111
20160116 土 20160117 日 20160118 月 1111
20160119 火 20160120 水 20160121 木 1111
20160122 金 20160123 土 20160124 日 1111
20160125 月 20160126 火 20160127 水 1111
20160128 木 20160129 金 20160130 土 1111
20160131 日 20160201 月 20160202 火 1111
20160203 水 20160204 木 20160205 金 1111
20160206 土 20160207 日 20160208 月 1111
20160209 火 20160210 水 20160211 木 1111
20160212 金 20160213 土 20160214 日 1111
20160215 月 20160216 火 20160217 水 1111
20160218 木 20160219 金 20160220 土 1111
20160221 日 20160222 月 20160223 火 1111
20160224 水 20160225 木 20160226 金 1111
20160227 土 20160228 日 20160229 月 1111
20160301 火 20160302 水 20160303 木 1111
```

3. `-e` 显示英语格式

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
[trial@localhost data]$ insweek -e -c1 -c3 test_date 
20160110 Sun 20160111 20160112 Tue 1111
20160113 Wed 20160114 20160115 Fri 1111
20160116 Sat 20160117 20160118 Mon 1111
20160119 Tue 20160120 20160121 Thu 1111
20160122 Fri 20160123 20160124 Sun 1111
20160125 Mon 20160126 20160127 Wed 1111
20160128 Thu 20160129 20160130 Sat 1111
20160131 Sun 20160201 20160202 Tue 1111
20160203 Wed 20160204 20160205 Fri 1111
20160206 Sat 20160207 20160208 Mon 1111
20160209 Tue 20160210 20160211 Thu 1111
20160212 Fri 20160213 20160214 Sun 1111
20160215 Mon 20160216 20160217 Wed 1111
20160218 Thu 20160219 20160220 Sat 1111
20160221 Sun 20160222 20160223 Tue 1111
20160224 Wed 20160225 20160226 Fri 1111
20160227 Sat 20160228 20160229 Mon 1111
20160301 Tue 20160302 20160303 Thu 1111
```

### ②、参数

1. -c：指定使用哪几列的数据显示星期几（在第几列后添加）
2. -e：英语格式显示星期几
3. -j：日语的形式显示星期几

## 6、添加计算秒数：`insclock`

计算从 1970-01-01:00:00:00 开始到指定的日期所经过的秒数，在指定的列后输出出来
数据的格式必须是正确的时间格式才可以使用此命令

-  8  位：YYYYMMDD
- 12 位：YYYYMMDDHHMM
- 14 位：YYYYMMDDHHMMSS

```shell
[trial@localhost cuichangjian]$ cat test_date 
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
```

### ①、语法

`insclock -r -cCOL1[,COL2]... [FILE]`
`insclock 是否转换为日期 -c 开始计算的列,结束计算的列 ... [FILE]`

```shell
[trial@localhost cuichangjian]$ cat test_date 
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
[trial@localhost cuichangjian]$ insclock -c3 test_date 
20160110 20160111 20160112 1452524400 1111
20160113 20160114 20160115 1452783600 1111
20160116 20160117 20160118 1453042800 1111
20160119 20160120 20160121 1453302000 1111
20160122 20160123 20160124 1453561200 1111
20160125 20160126 20160127 1453820400 1111
20160128 20160129 20160130 1454079600 1111
20160131 20160201 20160202 1454338800 1111
20160203 20160204 20160205 1454598000 1111
20160206 20160207 20160208 1454857200 1111
20160209 20160210 20160211 1455116400 1111
20160212 20160213 20160214 1455375600 1111
20160215 20160216 20160217 1455634800 1111
20160218 20160219 20160220 1455894000 1111
20160221 20160222 20160223 1456153200 1111
20160224 20160225 20160226 1456412400 1111
20160227 20160228 20160229 1456671600 1111
20160301 20160302 20160303 1456930800 1111
[trial@localhost cuichangjian]$ insclock -r -c3 test_date 
20160110 20160111 20160112 19700822170152 1111
20160113 20160114 20160115 19700822170155 1111
20160116 20160117 20160118 19700822170158 1111
20160119 20160120 20160121 19700822170201 1111
20160122 20160123 20160124 19700822170204 1111
20160125 20160126 20160127 19700822170207 1111
20160128 20160129 20160130 19700822170210 1111
20160131 20160201 20160202 19700822170322 1111
20160203 20160204 20160205 19700822170325 1111
20160206 20160207 20160208 19700822170328 1111
20160209 20160210 20160211 19700822170331 1111
20160212 20160213 20160214 19700822170334 1111
20160215 20160216 20160217 19700822170337 1111
20160218 20160219 20160220 19700822170340 1111
20160221 20160222 20160223 19700822170343 1111
20160224 20160225 20160226 19700822170346 1111
20160227 20160228 20160229 19700822170349 1111
20160301 20160302 20160303 19700822170503 1111
```

### ②、参数

1. -c：指定使用哪几列的数据计算秒数（在第几列后添加）
2. 将描述转换为日期（即经过这些秒是多少年）

## 7、添加指定字符串：`insstr`

1. 使用参数 `-i` 指定要插入的字符串
2. 使用参数 `-c` 指定在哪一列后面插入，只能插入一列字符串；只有最后一个指定的参数 `-c` 会生效

### ①、语法

`insstr -i STR -cCOL1 [FILE]`
`insstr -i 要插入的字符串 -c 在哪一列后面插入 文件`

1. 在第一列后插入字符串

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ insstr -i_ -c1 data
3 _ 2 1
2 _ 2 2
1 _ 2 3
1 _ 3 3
1 _ 1 1
2 _ 2 2
3 _ 3 3
2 _ 4 6
1 _ 4 6
3 _ 2 1
2 _ 1 4
3 _ 3 3
2 _ 1 3
[trial@smartedu data]$
```

2. 在第三列后插入字符串

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ insstr -iyuehai -c3 data
3 2 1 yuehai
2 2 2 yuehai
1 2 3 yuehai
1 3 3 yuehai
1 1 1 yuehai
2 2 2 yuehai
3 3 3 yuehai
2 4 6 yuehai
1 4 6 yuehai
3 2 1 yuehai
2 1 4 yuehai
3 3 3 yuehai
2 1 3 yuehai
[trial@smartedu data]$ 
```

3. 只能插入一列字符串；只有最后一个指定的参数 `-c` 会生效

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ insstr -iyuehai -c1,3 data
3 yuehai 2 1
2 yuehai 2 2
1 yuehai 2 3
1 yuehai 3 3
1 yuehai 1 1
2 yuehai 2 2
3 yuehai 3 3
2 yuehai 4 6
1 yuehai 4 6
3 yuehai 2 1
2 yuehai 1 4
3 yuehai 3 3
2 yuehai 1 3
[trial@smartedu data]$ insstr -iyuehai -c1 -c2 data
3 2 yuehai 1
2 2 yuehai 2
1 2 yuehai 3
1 3 yuehai 3
1 1 yuehai 1
2 2 yuehai 2
3 3 yuehai 3
2 4 yuehai 6
1 4 yuehai 6
3 2 yuehai 1
2 1 yuehai 4
3 3 yuehai 3
2 1 yuehai 3
[trial@smartedu data]$ 
```

### ②、参数

1. -c：指定在哪一列后面插入，只能插入一列字符串；只有最后一个指定的参数 `-c` 会生效
2. -i：指定要插入的字符串

## 8、添加指定列数的数字 0：`inszero`

1. 参数 `-n` 可指定添加的列数，每列 1 个 0
2. 参数 `-c` 指定在哪一列后面添加 0
3. 参数 `-c` 只能指定一列；只有最后一个指定的参数 `-c` 会生效

### ①、语法

`inszero -n NUM -cCOL1 [FILE]`
`inszero -n 指定添加的列数 -c 指定在哪一列后面添加 文件`

1. 在第 1 列后面添加 3 列 0

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ inszero -n3 -c1 data
3 0 0 0 2 1
2 0 0 0 2 2
1 0 0 0 2 3
1 0 0 0 3 3
1 0 0 0 1 1
2 0 0 0 2 2
3 0 0 0 3 3
2 0 0 0 4 6
1 0 0 0 4 6
3 0 0 0 2 1
2 0 0 0 1 4
3 0 0 0 3 3
2 0 0 0 1 3
[trial@smartedu data]$ 
```

2. 在第 3 列后面添加 5 列 0

```shell
[trial@smartedu data]$ cat data
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
[trial@smartedu data]$ inszero -n5 -c3 data
3 2 1 0 0 0 0 0
2 2 2 0 0 0 0 0
1 2 3 0 0 0 0 0
1 3 3 0 0 0 0 0
1 1 1 0 0 0 0 0
2 2 2 0 0 0 0 0
3 3 3 0 0 0 0 0
2 4 6 0 0 0 0 0
1 4 6 0 0 0 0 0
3 2 1 0 0 0 0 0
2 1 4 0 0 0 0 0
3 3 3 0 0 0 0 0
2 1 3 0 0 0 0 0
[trial@smartedu data]$
```

### ②、参数

1. -c：指定在哪一列后面添加
2. -n：指定添加的列数

# 十二、excel 处理

## 1、读取表格：`rExcel`

## 2、生成表格：`wExcel`

### ①、语法

`wExcel -t<template> [-s<SheetNo> -n<SheetName> -x<1> -y<1>] -o<output> [-d<c>] [FILE]`

---

`wExcel -t<指定要将数据放入的表格模板文件> [-s<指定在第几页插入数据> -n<指定选择插入页的名称> `
`-x<指定在第几行开始插入（包含）> -y<指定在第几列开始插入（包含）>] -o<生成的文件名称> [-d<输入文件的类型为csv时，可以键入-d>] 文件`

### ②、参数

1. -t：指定要将数据放入的表格模板文件，必须是存在的文件
2. -o：数据插入完毕后，生成的文件名称，即做成的表格
3. -x：指定在第几行开始插入（包含指定的行）；`-x 1` 即为从第一行开始插入数据
4. -y：指定在第几列开始插入（包含指定的列）；`-y 1` 即为从第一列开始插入数据
5. -s：指定在第几页插入数据
6. -n：指定选择插入页的名称（这个参数好像有问题）
7. -d：字符拆分器；当输入文件的类型为 csv 时，可以使用该参数

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161318.png)

### ③、说明

1. 各个参数后跟的路径、数字或字符等要和参数空一个空格，不然会报错
2. 参数 `-t、-o、-x、-y` 必须指定；参数 `-s` 可以不指定，不指定默认写入第一页
3. 只能向 xls 格式的表格里写入数据，能向 xlsx 格式的模板里写东西（但是我试的时候用的就是 xlsx 格式的，正常使用😓）

### ④、案例

- 模板文件：上面的截图

#### Ⅰ、一般使用

1. 模板文件为：/home/trial/SYS/cuichangjian/excel/test.xlsx
2. 生成的文件为：/home/trial/SYS/cuichangjian/excel/1.xlsx
3. 在第 2 页的第 1 行、第 1 列插入数据

```shell
[trial@smartedu excel]$ echo a s d f g h | tov -n2 | wExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/1.xlsx -s 2 -x 1 -y 1
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161416.png)

#### Ⅱ、从第 4 行 第 5 列开始插入

1. 模板文件为：/home/trial/SYS/cuichangjian/excel/test.xlsx
2. 生成的文件为：/home/trial/SYS/cuichangjian/excel/2.xlsx
3. 在第 2 页的第 4 行、第 5 列插入数据
```shell
[trial@smartedu excel]$ echo a s d f g h | tov -n2 | wExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/2.xlsx -s 2 -x 4 -y 5
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161435.png)

## 3、复制表格格式：`copyStyle`

### ①、语法

`copyStyle -f<file> [-s<SheetNo> -x<1> -y<1>] [-R<range>]`
`copyStyle -f<指定要修改的表格> [-s<指定哪一页> -x<指定复制格式的横坐标> -y<指定复制格式的纵坐标>] [-R<指定复制到的坐标区间>]`

### ②、参数

1. -f：指定要修改的表格，复制格式只能从索要修改的表格里复制
2. -s：指定复制和修改的是哪一页
3. -x：指定复制格式的横坐标
4. -y：指定复制格式的纵坐标
5. -R：指定复制到的坐标区间

### ③、说明

1. 只能修改一个文件，不可以将格式从一个文件复制到另一个文件
2. 只能对指定的文件进行修改，不可以输出为一个新的文件

### ④、案例

#### Ⅰ、一般使用

##### （1）、原表格

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161507.png)

##### （2）、  命令及结果

1. 修改文件 /home/trial/SYS/cuichangjian/excel/2.xlsx 的格式
2. 选择其第 2 页的第 2 行、第 1 列的格式
3. 将其格式复制到 A10:B10 这个区间的表格中（包含）

```shell
[trial@smartedu excel]$ copyStyle -f /home/trial/SYS/cuichangjian/excel/2.xlsx -s 2 -x 2 -y 1 -R A10:B10
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161533.png)

## 4、隐藏某页表格：`hideSheet`

### ①、语法

`HideSheet -f<file> [-s<SheetNo> ...]`
`HideSheet -f<指定要进行操作的文件> [-s<指定要隐藏的页> ...]
`
### ②、参数

1. -f：指定要进行操作的文件
2. -s：指定要隐藏的页；可以指定多个 `-s` 参数

### ③、说明

1. 只能对指定的文件进行修改，不可以输出为一个新的文件

### ④、案例

#### Ⅰ、一般使用

##### （1）、原始表格

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161644.png)

##### （2）、命令及结果

1. 隐藏文件 /home/trial/SYS/cuichangjian/excel/2.xlsx 的页
2. 选择其第 2 页和第 3 页进行隐藏

```shell
[trial@smartedu excel]$ hideSheet -f /home/trial/SYS/cuichangjian/excel/2.xlsx -s 3 -s 4
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161712.png)

## 5、处理表格：`mkExcel`

### ①、语法

`mkExcel -t<template.xls> -o<output.xls> [-d<c>] -S<script>`
`mkExcel -t<template.xls> -o<output.xls> [-d<c>] -S<script>`

### ②、参数

1. -t：指定要将数据放入的表格模板文件，必须是存在的文件
2. -o：数据处理完毕后，生成的文件名称，即做成的表格
3. -d：字符拆分器；当输入文件的类型为 csv 时，可以使用该参数
4. -S：指定进行操作的方式
   1. FILLDATA：插入数据
   2. INSROW：在指定行的上面插入行
   3. DELROW：从指定行开始删除行
   4. SHEETNAME：设置指定页的名称
   5. HIDESHEET：隐藏指定页
   6. HIDECOL：隐藏列
   7. COPYSTYLE：复制格式
   8. VMERGECELL：合并单元格
5. 参数 `-S` 中设置左表的方式有两种
   1. 标记示例： `COPYSTYLE 2 A2 A10:C12`；将第 2 页的 A2 单元格的格式复制到 A10:C12 这个单元格区间中
   2. 矩阵示例： `COPYSTYLE 1 1,2 1,10:3,12`；将第 1 页的第 1 行、第 2 列单元格的格式复制到第 1 行、第 10 列至第 3 行、第 12 列这个单元格区间中

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161743.png)

### ③、说明

### ④、案例

- 模板文件：上面的截图

#### Ⅰ、FILLDATA：插入数据

##### （1）、一般使用

- 从 B3 开始插入数据

```shell
[trial@smartedu excel]$ echo 1 2 a s 3 4 g h | tov -n2 > data
[trial@smartedu excel]$ cat data 
1 2
a s
3 4
g h
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/01.xlsx -S <(echo FILLDATA 2 B3 data)
Row:1 do: FILLDATA 2 B3 data
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725161814.png)

#### Ⅱ、INSROW：在指定行的上面插入行

##### （1）、一般使用

- 在第 2 页的第 4 行上面插入 2 行

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/02.xlsx -S <(echo INSROW 2 4 2)
Row:1 do: INSROW 2 4 2
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162108.png)

#### Ⅲ、DELROW：从指定行开始删除行

##### （1）、一般使用

- 从第 2 页的第 4 行开始删除 2 行
- 使用的时候发现不包括指定的列，比如指定从第 2 页的第 4 行开始删除 2 行，他会删除第 5、6 行；和讲解的不同

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/03.xlsx -S <(echo DELROW 2 4 2)
Row:1 do: DELROW 2 4 2
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162149.png)

#### Ⅳ、SHEETNAME：设置指定页的名称
##### （1）、一般使用

- 设置第 1 页的名称为：yuehai
```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/04.xlsx -S <(echo SHEETNAME 1 yuehai)
Row:1 do: SHEETNAME 1 yuehai
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162230.png)

#### Ⅴ、HIDESHEET：隐藏指定页

##### （1）、一般使用

- 隐藏第 3 页

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/05.xlsx -S <(echo HIDESHEET 2)
Row:1 do: HIDESHEET 2
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162254.png)

#### Ⅵ、HIDECOL：隐藏列

##### （1）、一般使用

- 隐藏第 2 页的第 2 列

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/06.xlsx -S <(echo HIDECOL 2 2)
Row:1 do: HIDECOL 2 2
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162318.png)

#### Ⅶ、COPYSTYLE：复制格式

##### （1）、一般使用

- 选择第 2 页的第 2 行、第 2 列的格式， 将其格式复制到 A1 至 I1 这个区间的表格中（包含）

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/07.xlsx -S <(echo COPYSTYLE 2 B2 A1:I1)
Row:1 do: COPYSTYLE 2 B2 A1:I1
[trial@smartedu excel]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162340.png)

#### Ⅷ、VMERGECELL：合并单元格

##### （1）、一般使用

- 合并第 2 页 的 A2:A10 单元格
- 命令执行完并没有合并还是原先的格式，不知道为什么

```shell
[trial@smartedu excel]$ mkExcel -t /home/trial/SYS/cuichangjian/excel/test.xlsx -o /home/trial/SYS/cuichangjian/excel/08.xlsx -S <(echo VMERGECELL 2 A2:A10)
Row:1 do: VMERGECELL 2 A2:A10
[trial@smartedu excel]$ 
```

# 十三、文件处理

## 1、判断文件是否存在：`touchi`

### ①、语法

`touchi 'String' <File>`
`touchi '在创建的文件中添加的字符串' <File>`

### ②、参数

无

### ③、说明

1. 检查参数指定的文件是否存在，若是存在，则不进行任何操作
2. 若是不存在，则创建该文件，并将指定的字符串添加到该文件中

### ④、案例

1. 一般使用

```shell
[trial@smartedu data]$ ll
total 28
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ touchi "_" data
[trial@smartedu data]$ cat data
3 2 1
2 2 2
1 2 3
5 3 3
1 1 1
2 2 2
3 3 3
2 4 6
1 4 6
3 2 1
2 1 4
3 3 3
2 1 3
[trial@smartedu data]$ touchi "_" data5
[trial@smartedu data]$ ll
total 32
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ cat data5
_
[trial@smartedu data]$ 
```

## 2、判断 gz 文件是否存在：`touchg`

### ①、语法

`touchg <File>`
`touchg <File>`

### ②、参数

无

### ③、说明

1. 检查参数指定的 gz 文件是否存在，若是存在，则不进行任何操作
2. 若是不存在，则创建该 gz 文件，创建出来是空文件

### ④、案例

1. 一般使用

```shell
[trial@smartedu data]$ ll
total 32
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ touchg data6.gz
[trial@smartedu data]$ ll
total 36
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ zcat data6.gz 
[trial@smartedu data]$ -rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ cat data5
_
[trial@smartedu data]$ 
```

2. 注意创建的是压缩文件，并不能直接读取

```shell
[trial@smartedu data]$ ll
total 36
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ touchg data6
[trial@smartedu data]$ ll
total 40
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ cat data6
e�c[trial@smartedu data]$ 
```

![](https://openlist.yuehai.fun:63/d/TakeDown/%E5%85%AC%E5%8F%B8/%E5%88%9B%E8%BF%B9/Smart/attachments/Pasted%20image%2020230725162446.png)

## 3、判断文件是否存在：`default`

### ①、语法

`default -i<設定文字> -x<設定文字出力回数> [-i<設定文字> -x<設定文字出力回数> ...] [-f<指定ファイル>] [FILE]`

---

`default -i<在创建的文件中添加的字符串> -x<在创建的文件中添加的字符串的次数> `
`[-i<在创建的文件中添加的字符串> -x<在创建的文件中添加的字符串的次数> ...] [-f<指定文件>] [FILE]`

### ②、参数

1. -i：若指定的文件不存在，在创建的文件中添加的字符串
2. -x：前面的参数 `-i` 指定的字符串添加的次数，可指定 1-16 次；参数 `-i` 和 `-x` 必须同时使用且必须指定
3. -f：指定文件名，必须指定该参数

### ③、说明

1. 与 `touchi` 和 `touchg` 类似，会检查参数指定的文件是否存在，若是存在，则不进行任何操作
2. 若是不存在，则创建该文件，并将指定的字符串以指定的次数添加到该文件中

### ④、案例

1. 一般使用

```shell
[trial@smartedu data]$ ll
total 40
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   2  9月  8 16:11 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ default -i@ -x2 -f data5
[trial@smartedu data]$ cat data5
_ _
[trial@smartedu data]$ default -i@ -x2 -f data7
[trial@smartedu data]$ cat data7
@ @
[trial@smartedu data]$ 
```

2. 可以指定多个 `-i` 和 `-x` 参数

```shell
[trial@smartedu data]$ default -i@ -x2 -i__ -x3 -iaa11 -x4 -f data8
[trial@smartedu data]$ cat data8
@ @ __ __ __ aa11 aa11 aa11 aa11
[trial@smartedu data]$ 
```

## 4、判单多个文件是否存在：`chkexists`

### ①、语法

`chkexists [-1] [-d FILEPATH...] [-p]  [LISTファイル]`
`chkexists [-1] [-d FILEPATH...] [-p]  [LISTファイル]`

### ②、参数

1. -d：直接指定路径或文件时使用此参数
2. -p：指定该参数后，若是文件不存在也不会报错退出，会继续往下执行；不可与参数 `-1` 一起使用
3. -1：若是指定的文件中至少有一个存在，则正常退出；否则会报错退出

### ③、说明

1. 不指定参数时，该命令会读取指定的文件的数据，将其中的数据作为文件名来进行判断，若是文件不存在则默认退出
2. 指定参数 `-d`，表示后面指定的是文件，将会判断指定的文件存不存在，而不是读取文件的内容
3. 指定参数 `-p`，若是文件不存在也不会报错退出，会继续往下执行
4. 指定参数 `-1`，若是指定的文件中至少有一个存在，则正常退出；否则会报错退出，不再进行下面的命令
5. ng：文件不存在
6. ok：文件存在

### ④、案例

1. 不指定参数时，该命令会读取指定的文件的数据，将其中的数据作为文件名来进行判断，若是文件不存在则默认退出；此时不可指定多个文件

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists data
chkexists: 3 2 1 ng
[trial@smartedu data]$ 
```

2. 指定参数 `-d`时，可传递数据集合

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ ls | tov | chkexists 
chkexists: data ok
chkexists: data2 ok
chkexists: data3 ok
chkexists: data5 ok
chkexists: data6 ok
chkexists: data6.gz ok
chkexists: data7 ok
chkexists: data8 ok
chkexists: exchsorttest ok
chkexists: master ok
chkexists: rea ok
chkexists: snmerge ok
chkexists: test_date ok
chkexists: tran ok
chkexists: zmerge ok
[trial@smartedu data]$ 
```

3. 指定参数 `-d`，表示后面指定的是文件，将会判断指定的文件存不存在，而不是读取文件的内容

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists -d data
chkexists: data ok
[trial@smartedu data]$ 
```

4. 指定参数 `-d` 时，可指定多个文件

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists -d data data2
chkexists: data ok
chkexists: data2 ok
[trial@smartedu data]$ 
```

5. 不指定参数 `-p` 和 `-1` 时，当遇到有文件不存在就会报错并退出

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists -d data 1 data2
chkexists: data ok
chkexists: 1 ng
[trial@smartedu data]$ 
```

6. 指定参数 `-p`，若是文件不存在也不会报错退出，会继续往下执行

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists -d -p data 1 data2
data OK
1 NG
data2 OK
[trial@smartedu data]$ 
```

7. 指定参数 `-1`，若是指定的文件中至少有一个存在，则正常退出；否则会报错退出，不再进行下面的命令

```shell
[trial@smartedu data]$ ll
total 48
-rw-r--r--. 1 trial trial  78  8月 25 14:27 data
-rw-r--r--. 1 trial trial 135  8月  5 12:33 data2
-rw-r--r--. 1 trial trial  84  8月  5 15:53 data3
-rw-rw-r--. 1 trial trial   4  9月  8 16:23 data5
-rw-rw-r--. 1 trial trial  20  9月  8 16:19 data6
-rw-rw-r--. 1 trial trial  20  9月  8 16:16 data6.gz
-rw-rw-r--. 1 trial trial   4  9月  8 16:25 data7
-rw-rw-r--. 1 trial trial  33  9月  8 16:25 data8
drwxrwxr-x. 2 trial trial  41  8月 25 17:29 exchsorttest
-rw-r--r--. 1 trial trial  56  8月  4 16:34 master
-rw-rw-r--. 1 trial trial  41  8月 25 14:04 rea
drwxrwxr-x. 2 trial trial  53  8月 30 09:19 snmerge
-rw-r--r--. 1 trial trial 576  8月  4 11:42 test_date
-rw-r--r--. 1 trial trial  54  8月 25 15:44 tran
drwxrwxr-x. 2 trial trial  53  8月 29 15:40 zmerge
[trial@smartedu data]$ chkexists -d -1 data 1 data2
chkexists: data ok
chkexists: 1 ng
chkexists: data2 ok
[trial@smartedu data]$ echo $?
0
[trial@smartedu data]$ chkexists -d -1 1 2 3 aa
chkexists: 1 ng
chkexists: 2 ng
chkexists: 3 ng
chkexists: aa ng
[trial@smartedu data]$ echo $?
1
[trial@smartedu data]$ 
```

# 十四、缓存处理

## 1、读取文件的缓存大小：`chkcache`

### ①、语法

`chkcache [-r] [FILE...]`
`chkcache [计算文件夹中所有文件的页面缓存总数] [文件（路径）名...]`

### ②、参数

1. -r：若是要计算文件夹中所有文件的页面缓存总数，则使用此参数

### ③、说明

1. 可计算单个文件的缓存，也可计算多个文件的缓存
2. 还可以计算某路径下的缓存，此时要加参数 `-r`

### ④、案例

1. 一般使用

```shell
[trial@smartedu cuichangjian]$ pwd
/home/trial/SYS/cuichangjian
[trial@smartedu cuichangjian]$ chkcache -r /home/trial/SYS
/home/trial/SYS 1686257 1686257
[trial@smartedu cuichangjian]$ 
```

## 2、清除文件缓存：`freecache`

### ①、语法

`freecache [-r] [FILE...]`
`freecache [计算文件夹中所有文件的页面缓存总数] [文件（路径）名...]`

### ②、参数

1. -r：若是要计算文件夹中所有文件的页面缓存总数，则使用此参数

### ③、说明

1. 可清除单个文件的缓存，也可清除多个文件的缓存
2. 还可以清除某路径下的缓存，此时要加参数 `-r`

### ④、案例

1. 一般使用

```shell
[trial@smartedu cuichangjian]$ pwd
/home/trial/SYS/cuichangjian
[trial@smartedu cuichangjian]$ chkcache -r /home/trial/SYS
/home/trial/SYS 1686257 1686257
[trial@smartedu cuichangjian]$ freecache -r /home/trial/SYS
[trial@smartedu cuichangjian]$ chkcache -r /home/trial/SYS
/home/trial/SYS 1686257 0
[trial@smartedu cuichangjian]$ 
```

# 十五、

---

## 1、
## 2、
## 3、
## 4、
## 5、
## 6、
## 7、
## 8、
## 9、

---

### ①、
### ②、
### ③、
### ④、
### ⑤、
### ⑥、
### ⑦、
### ⑧、
### ⑨、
### ⑩、
#### Ⅰ、
#### Ⅱ、
#### Ⅲ、
#### Ⅳ、
#### Ⅴ、
#### Ⅵ、
#### Ⅶ、
#### Ⅷ、
#### Ⅸ、
#### Ⅹ、
