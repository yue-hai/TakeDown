> https://www.bilibili.com/video/BV1Db4y1m7Ho，尚硅谷，感觉不是太好，还行吧

# 一、Python 环境的安装
## 1、下载
> 官网：https://www.python.org/

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303105734.png)

## 2、安装
1. 双击下载好的 Python 安装包
2. 勾选左下角 `Add Python 3.7 to PATH` 选项，然后选择 `Install now` 立刻安装 Python
3. 默认安装

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303105855.png)

4. 自定义安装

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303105912.png)

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303105926.png)

5. 安装完成

## 3、测试是否安装成功
1. 点击电脑左下角开始按钮，输入 cmd 进入到 windows 的命令行模式。在命令行中输入 Python，正确显示 Python 版本，即表示 Python 安装成功
2. 如果在命令行中输入 python 出现如下错误

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110044.png)

3. 可能是因为在安装 Python 的过程中没有勾选 `Add Python 3.7 to PATH` 选项，此时需要手动对 Python 进行配置

## 4、手动配置 Python
> 注意：如果在安装过程中，已经勾选了 `Add Python 3.7 to PATH` 选项，并且在 cmd 命令模式下输入 python 指令不报错，就不需要再手动的配置Python
1. 右键 此电脑 --> 选择 属性

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110430.png)

2. 选择 高级系统设置 --> 环境变量 --> 找到并且双击 Path

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110446.png)

3. 双击 Path ,在弹框里点击新建，找到Python的安装目录，把路径添加进去

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110504.png)

4. 这里新添加的路径 `E:\python` 是 Python 安装好以后， Python.exe 这个可执行文件所在的目录

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110529.png)

# 二、pip 的使用
> pip 是一个现代的，通用的 Python 包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能，便于我们对 Python 的资源包进行管理。

## 1、安装

在安装 Python 时，会自动下载并且安装 pip

## 2、配置
1. 在 windows 命令行里，输入 `pip -V` 可以查看 pip 的版本。
2. 如果在命令行里，运行 `pip -V` 出现如下提示：

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110044.png)

3. 可能是因为在安装 python 的过程中未勾选 `Add Python 3.7 to PATH` 选项，需要手动的配置 pip 的环境变量。
4. 右键 此电脑 --> 环境变量 --> 找到并且双击 Path --> 在弹窗里点击新建 --> 找到 pip 的安装目录，把路径添加进去。

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110847.png)

5. 这里新添加的路径 `E:\python\Scripts` 是 Python 安装好以后， pip.exe 这个可执行文件所在的目录。

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303110920.png)

## 3、使用 pip 管理 Python 包

1. `pip install <包名>`：安装指定的包
2. `pip uninstall <包名>`：删除指定的包
3. `pip list`：显示已经安装的包
4. `pip freeze`：显示已经安装的包，并且以指定的格式显示

## 4、 修改 pip 下载源

1. 运行 `pip install` 命令会从网站上下载指定的 python 包，默认是从 https://files.pythonhosted.org/ 网站上下载。这是个国外的网站，遇到网络情况不好的时候，可能会下载失败，我们可以通过命令，修改pip现在软件时的源。
2. 格式：`pip install 包名 -i 国内源地址`
3. 示例：`pip install ipython -i https://pypi.mirrors.ustc.edu.cn/simple/` 就是从中国科技大学(ustc)的服务器上下载 requests(基于python的第三方 web 框架)
4. 国内常用的pip下载源列表：
	1. 阿里云 http://mirrors.aliyun.com/pypi/simple/
	2. 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	3. 豆瓣(douban) http://pypi.douban.com/simple/
	4. 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
	5. 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

# 三、运行 Python 程序

## 1、终端运行代码

## 2、运行 python 文件

使用 python 指令运行后缀为 .py 的 python 文件

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303111400.png)

## 3、Pycharm

下载地址：http://www.jetbrains.com/pycharm/download

1. 创建工程

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303112528.png)

2. 创建完成：

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303125141.png)

3. 创建 python 代码文件

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303125258.png)

4. 编写代码

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303125724.png)

# 四、Python 基础

## 0、注释
1. 单行注释：以 `#` 开头，`#` 右边的所有东西当做说明，而不是真正要执行的程序，起辅助说明作用
2. 多行注释：以 `'''` 开始，并以 `'''` 结束，我们称之为多行注释；
3. 可以使用三个单引号，也可以使用三个双引号

```python
# @Time     : 2023/3/3 13:13
# @Author   : 月海
# @File     : 01_test.py
# @Project  : 01_python

# 单行注释

"""
    多行注释
"""

'''
    多行注释
'''
print("月海")
```

## 1、变量
1. 单个定义变量：`变量名 = 变量值`
2. 多个变量赋值：`变量名1 = 变量名2 = 变量名3 = 变量值`
3. 为多个变量指定多个值：`变量名1,变量名2,变量名3 = 变量值1,变量值2,变量值3`
4. 可以使用 `del` 语句删除一些对象的引用

```python
# @Time     : 2023/3/3 13:33
# @Author   : 月海
# @File     : 02_变量
# @Project  : 01_python

# 1. 单个定义变量：`变量名 = 变量值`
name = "月海"

# 2. 多个变量赋值：`变量名1 = 变量名2 = 变量名3 = 变量值`
salary = putAside = 0

# 3. 为多个变量指定多个值：`变量名1,变量名2,变量名3 = 变量值1,变量值2,变量值3`
age, sex = 16, 0

# 打印
print(name)

# 删除变量（删除对象的引用）
del name

# 再次打印
print(name)
```

5. 变量命名规范：
	1. 标识符由字母、下划线和数字组成，且数字不能开头。
	2. 严格区分大小写。
	3. 不能使用关键字
6. 关键字：
	1. 关键字的概念：一些具有特殊功能的标识符，这就是所谓的关键字。
	2. 关键字，已经被 python 官方使用了，所以不允许开发者自己定义和关键字相同名字的标识符。

<table>
	<tr>
		<td>False</td>
		<td>None</td>
		<td>True</td>
		<td>and</td>
		<td>as</td>
		<td>assert</td>
		<td>break</td>
		<td>class</td>
	</tr>
	<tr>
		<td>continue</td>
		<td>def</td>
		<td>del</td>
		<td>elif</td>
		<td>else</td>
		<td>except</td>
		<td>finally</td>
		<td>for</td>
	</tr>
		<tr>
		<td>from</td>
		<td>global</td>
		<td>if</td>
		<td>import</td>
		<td>in</td>
		<td>is</td>
		<td>lambda</td>
		<td>nonlocal</td>
	</tr>
		<tr>
		<td>not</td>
		<td>or</td>
		<td>pass</td>
		<td>raise</td>
		<td>return</td>
		<td>try</td>
		<td>while</td>
		<td>with</td>
	</tr>
		<tr>
		<td>yield</td>
	</tr>
</table>

## 2、数据类型
1. 程序中：在 Python 里为了应对不同的业务需求，也把数据分为不同的类型。 如下图所示：

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303134507.png)

2. 在 python 中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，不需要咱们开发者主动的去说明它的类型，<font color="#c00000">系统会自动辨别</font>。也就是说在使用的时候：<font color="#c00000">变量没有类型，数据才有类型</font>。
3. 比如下面的示例里，a 的类型可以根据数据来确认，但是我们没法预测变量 b 的类型

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303134728.png)

4. 如果临时想要查看一个变量存储的数据类型，可以使用 `type(变量的名字)`，来查看变量存储的数据类型

```python
# @Time     : 2023/3/3 13:49
# @Author   : 月海
# @File     : 02_数据类型
# @Project  : 01_python

# 定义变量
name = "月海"
# 打印
print(type(name))

# 重新赋值
name = 123
# 打印
print(type(name))
```

## 3、运算符

> https://www.runoob.com/python3/python3-basic-operators.html

### ①、 算数运算符
1. 混合运算时，优先级顺序为： `**` 高于 `*`、 `/` `%` `//` 高于 `+` `-` ，为了避免歧义，建议使用 `()` 来处理运算符优先级。 并且，不同类型的数字在进行混合运算时，整数将会转换成浮点数进行运算
2. 如果是两个字符串做加法运算，会直接把这两个字符串拼接成一个字符串
3. 如果是数字和字符串做加法运算，会直接报错
4. 如果是数字和字符串做乘法运算，会将这个字符串重复多次

| 运算符|描述|实例|
|--|--|--|
| + |加|两个对象相加 a + b 输出结果 30                                |
| - |减|得到负数或是一个数减去另一个数 a - b 输出结果 -10             |
| * |乘|两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200 |
| / |除|b / a 输出结果 2                                              |
| // |取整除|返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0 |
| %|取余|返回除法的余数 b % a 输出结果 0                             |
| `**`|指数|`a**b` 为 10 的 20 次方|
| `()` | 小括号 | 提高运算优先级，比如：`(1+2) * 3` |

### ②、 赋值运算符

| 运算符 | 描述       | 实例 |
| ------ | ---------- | ---- |
| `=`    | 赋值运算符 | 把 `=` 号右边的结果 赋给 左边的变量，如 `num = 1 + 2 * 3`，结果 num 的值为7     |

### ③、复合赋值运算符

| 运算符 | 描述                                                                 | 实例                          |
| ------ | -------------------------------------------------------------------- | ----------------------------- |
| `+=`   | 加法赋值运算符                                                       | `c += a` 等效于 `c = c + a`   |
| `-=`   | 减法赋值运算符                                                       | `c -= a` 等效于 `c = c - a`   |
| `*=`   | 乘法赋值运算符                                                       | `c *= a` 等效于 `c = c * a`   |
| `/=`   | 除法赋值运算符                                                       | `c /= a` 等效于 `c = c / a`   |
| `//=`  | 取整除赋值运算符                                                     | `c //= a` 等效于 `c = c // a` |
| `%=`   | 取模赋值运算符                                                       | `c %= a` 等效于 `c = c % a`   |
| `**=`  | 幂赋值运算符                                                         | `c **= a` 等效于 `c = c ** a` |
| `:=`   | 海象运算符，可在表达式内部为变量赋值。<br>Python3.8 版本新增运算符。 | 在这个示例中，赋值表达式可以避免调用 len() 两次：<br>`if (n := len(a)) > 10: print(f"List is too long ({n} elements, expected <= 10)")`                              |


### ④、 比较运算符
> 以下假设变量 a 为 10，变量 b 为 20
> 
> 所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价

| 运算符|描述|实例|
|--|--|--|
|`==`|等于：比较对象是否相等|`(a == b)` 返回False|
|`!=`|不等于：比较两个对象是否不相等|`(a != b)` 返回true|
|`>` |大于：返回 x 是否大于 y|`(a > b)` 返回False|
|`>=`|大于等于：返回 x 是否大于等于 y|`(a >= b)` 返回False|
| `<` |小于：返回 x 是否小于 y|`(a < b)` 返回true|
|`<=`|小于等于：返回x是否小于等于y|`(a <= b)` 返回true|


### ⑤、逻辑运算符

| 运算符 | 描述                            |
| ------ | ------------------------------- |
| and    | 与；只有全部为 true 才为 true   |
| or     | 或；只有全部为 false 才为 false |
| not    | 非；取反                      |

### ⑥、位运算符

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230310094140.png)

## 4、输入输出

### ①、输出

1. 普通输出：`print('月海：16')`
2. 格式化输出：
	1. 类似 c 语言中的格式化输出，和 C 语言的区别在于，Python 中格式控制符和转换说明符用 `%` 分隔，C 语言中用逗号
	2. %字符：标记转换说明符的开始，% 前是格式字符，% 后是变量或具体的字符
	3. 最小字段宽度和精度
		1. 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*（星号），则宽度会从值元组中读出。
		2. 点 `.` 后跟精度值：如果需要输出实数，精度值表示出现在小数点后的位数。如果需要输出字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
	4. 转换标志：`-` 表示左对齐；`+` 表示在数值前要加上正负号；` `(空白字符)表示正数之前保留空格()；0 表示转换值若位数不够则用 0 填充
3. `format()` 函数
4. <font color="#ff0000">模板字符串</font>

```python
# @Time     : 2023/3/3 16:19
# @Author   : 月海
# @File     : 07_输出
# @Project  : 01_python

# 格式化输出
name = '月海'
age = 16

# 普通输出
print(name + '的年龄是：' + str(age) + '岁')

# 格式化输出；%字符：标记转换说明符的开始，% 前是格式字符，% 后是变量或具体的字符
print('%s的年龄是：%d岁' % (name, age))
print('%s的年龄是：%d岁' % ('言', 14))

# 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*（星号），则宽度会从值元组中读出。
# 点 `.` 后跟精度值：如果需要输出实数，精度值表示出现在小数点后的位数。如果需要输出字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
# 第一个值：字段宽 10，精度 1；字段宽 10 所以会显示 10 个字符（补的空格），精度 1 所以只显示了一个应该显示的值
# 第二个值：字段宽 10，精度 3；字段宽 10 所以会显示 10 个字符（补的空格），精度 3 所以只显示了 3 个小数
print('%10.1s的年龄是：%10.3f岁' % (name, 12.54687))

# 转换标志：`-` 表示左对齐；`+` 表示在数值前要加上正负号；` `(空白字符)表示正数之前保留空格()；0 表示转换值若位数不够则用 0 填充
print('%-f' % 54.2168465)
print('%+f' % 54.2168465, '%+f' % -54.2168465)
print('% f' % 54.2168465, '% f' % -54.2168465)
print('%012.3f' % 54.2168465, '% f' % -54.2168465)

# format() 函数
# 索引
print('{0}的年龄是：{1}'.format('月海', 16))
# 关键字
print('{y}的年龄是：{age}'.format(y='月海', age=16))

# 模板字符串
print(f'{name}的年龄是：{age}')
```

3. 格式字符归纳

|格式字符|说明|
|--|--|
|%s|字符串采用str()的显示|
|%r|字符串(repr())的显示| 
|%c|单个字符|
|%b|二进制整数|
|%d|十进制整数|
|%i|十进制整数|
|%o|八进制整数|
|%x|十六进制整数|
|%e|指数（基底写e）|
|%E|指数（基底写E）|
|%f、%F|浮点数|
|%g|指数(e)或浮点数(根据显示长度)|
|%G|指数(E)或浮点数(根据显示长度)|
|`%%`|字符%|

### ②、输入（获取键盘输入）

1. `input()` 的小括号中放入的是提示信息，用来在获取数据之前给用户的一个简单提示
2. `input()` 在从键盘获取了数据以后，会存放到等号右边的变量中
3. `input()` 会把用户输入的任何值都作为字符串来对待
4. `raw_input()` 是 Python2.X 版本中的函数，在 Python3.X 中已经无法使用。`raw_input()` 用于获取用户（控制台）输入，且 `raw_input()` 将所有输入都当成字符串看待。在 Python3.X 中 <font color="#ff0000">`input()`</font> 代替了 raw_input()

```python
# @Time     : 2023/3/3 16:53
# @Author   : 月海
# @File     : 08_输入
# @Project  : 01_python

# input() 的小括号中放入的是提示信息，用来在获取数据之前给用户的一个简单提示
# input() 在从键盘获取了数据以后，会存放到等号右边的变量中
# input() 会把用户输入的任何值都作为字符串来对待
name = input('请输入姓名：')
print('输入的姓名为：%s' % name)
```

```python
请输入姓名：月海
输入的姓名为：月海

进程已结束,退出代码0
```

# 五 、流程控制语句
## 1、`if` 判断

- 和 java 中一样

```python
# @Time     : 2023/3/6 8:50
# @Author   : 月海
# @File     : 01_if
# @Project  : 01_python

name = '月海'

# if
if name == '月海':
    print('可爱')

# if-else
if name == '月海':
    print('可爱')
else:
    print('？')

# if-elif
if name == '月海':
    print('可爱')
elif name == '言':
    print('也可爱')
```

```python
可爱
可爱
可爱

进程已结束,退出代码0
```

## 2、`for in` 循环

- 循环控制语句
| 控制语句                                | 描述                                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------------- |
| break 语句                              | 在语句块执行过程中终止循环，并且<font color="#ff0000">跳出整个循环</font>                   |
| continue 语句                           | 在语句块执行过程中终止当前循环，<font color="#ff0000">跳出该次循环</font>，执行下一次循环。 |
| pass 语句                               | pass是空语句，是为了保持程序结构的完整性。                                                  |
| <font color="#ff0000">for...else</font> | 当循环执行完毕（即遍历完 iterable 中的所有元素）后，会执行 else 子句中的代码<br>如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句                                                                                            |

- 和 java 中一样

```python
# @Time     : 2023/3/6 8:50
# @Author   : 月海
# @File     : 02_for
# @Project  : 01_python

# 定义字符串
name = 'yuehai月海'
# 定义列表
list = ['月海', 16, 0, ['yuehai', 'yan']]

# 遍历字符串
for s in name:
    print(s)

print('------------------------------')

# 遍历集合
for l in list:
    print(l)
```

```python
y
u
e
h
a
i
月
海
------------------------------
月海
16
0
['yuehai', 'yan']

进程已结束,退出代码0
```

## 3、`While` 循环

- 循环控制语句
| 控制语句      | 描述                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------- |
| break 语句    | 在语句块执行过程中终止循环，并且<font color="#ff0000">跳出整个循环</font>                   |
| continue 语句 | 在语句块执行过程中终止当前循环，<font color="#ff0000">跳出该次循环</font>，执行下一次循环。 |
| pass 语句     | pass是空语句，是为了保持程序结构的完整性。                                                  |
| <font color="#ff0000">for...else</font> | 如果 while 后面的条件语句为 false 时，则执行 else 的语句块<br>如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句                                                                                            |

- 和 java 中一样；没有 `do-while`

```python
# @Time     : 2023/3/6 8:50
# @Author   : 月海
# @File     : 03_While
# @Project  : 01_python

# 定义数字
num = 0
while num < 10:
    print(num)
    num = num + 1

print('-------------------------')

# 定义列表
num = 0
list = ['月海', 16, 0, ['yuehai', 'yan']]
while num < len(list):
    print(list[num])
    num = num + 1
```

```python
0
1
2
3
4
5
6
7
8
9
-------------------------
月海
16
0
['yuehai', 'yan']

进程已结束,退出代码0
```

## 4、`pass` 语句
1. Python pass 是空语句，是为了保持程序结构的完整性。
2. `pass` 不做任何事情，一般用做占位语句。
3. 在 Python 中有时候会看到一个 `def` 函数：该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行

```python
def sample(n_samples):
    pass
```

4. 空函数在 Python2.x 版本中 `pass` 是必须的；在 Python3.x 的时候 `pass` 可以写或不写

```python
# @Time     : 2023/3/6 8:51
# @Author   : 月海
# @File     : 04_pass
# @Project  : 01_python

# Python pass 是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。

# 定义集合
list = ['月海', 16, 0, ['yuehai', 'yan']]

# 遍历集合
for l in list:
    pass
    print(l)

```

## 5、`match` 分支（switch）

1. Python 3.10 增加了 `match...case` 的条件判断，不需要再使用一连串的 i`f-else` 来判断了。
2. `match` 后的对象会依次与 `case` 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，`_` 可以匹配一切

```python
# @Time     : 2023/3/7 9:52
# @Author   : 月海
# @File     : 05_match
# @Project  : 01_python

name = '月海'

match name:
    case 'yuehai':
        print('yuehai')
    case 'yan':
        print('yan')
    case '月海':
        print('月海')
    case _:
        print('都不是')
```

# 六、数据类型
## 1、`Numbers` 数字

> https://www.runoob.com/python3/python3-number.html

1. 数字数据类型用于存储数值。
2. 他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
3. 当你指定一个值时，Number 对象就会被创建
4. Python 支持四种不同的数字类型：
	1. int（有符号整型）
	2. long（长整型，也可以代表八进制和十六进制），3.0 之后尾部不需要加  L，python 会自动识别
	3. float（浮点型）
	4. complex（复数）；复数由实部（real）和虚部（imag）构成，在 Python 中，复数的虚部以 j 或者 J 作为后缀

```python
# @Time     : 2023/3/3 15:03
# @Author   : 月海
# @File     : 01_数字
# @Project  : 01_python

# 1. int（有符号整型）
myInt = 1
print(type(myInt), myInt)

# 2. long（长整型，也可以代表八进制和十六进制），3.0 之后尾部不需要加  L，python 会自动识别
myLong = 1548564152341586415634153213215341564156415416341564156341634186416341563418641541635
print(type(myLong), myLong)

# 3. float（浮点型）
myFloat = 101.21536416541
print(type(myFloat), myFloat)

# 4. complex（复数）；复数由实部（real）和虚部（imag）构成，在 Python 中，复数的虚部以 j 或者 J 作为后缀
# 实部可以进行计算操作；虚部类似后缀，跟在实部后面
c1 = 10 + 2j
print(type(c1), c1)
print(type(c1 + 10), c1 + 10)
```

```python
<class 'int'> 1
<class 'int'> 1548564152341586415634153213215341564156415416341564156341634186416341563418641541635
<class 'float'> 101.21536416541
<class 'complex'> (10+2j)
<class 'complex'> (20+2j)

进程已结束,退出代码0
```

## 2、`bool` 布尔
1. 只有两个值：`true`、`false`
2. 其中：`true`  也可以写为 `1`、`false`  也可以写为 `0`
## 3、`String` 字符串
> https://www.runoob.com/python3/python3-string.html

### ①、初识
1. 字符串或串(String)是由数字、字母、下划线组成的一串字符；它是编程语言中表示文本的数据类型。
2. python 的字串列表有 2 种取值顺序:
	1. 从左到右索引默认 0 开始的，最大范围是字符串长度少 1
	2. 从右到左索引默认 -1 开始的，最大范围是字符串开头

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303151801.png)

3. 如果你要实现从字符串中获取一段子字符串的话，可以使用 `[头下标:尾下标]` 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。`[头下标:尾下标]` 获取的子字符串<font color="#c00000">包含头下标的字符</font>，但<font color="#c00000">不包含尾下标的字符</font>；不论正序还是倒序，但是从左到右

```python
# @Time     : 2023/3/3 15:20
# @Author   : 月海
# @File     : 02_字符串_01
# @Project  : 01_python

name = "yuehai月海"

# 正序截取字符串
print(name[2:5])

# 倒序截取字符串；不论正序还是倒序，但是从左到右
print(name[-4:-2])

# 既正又负
print(name[2:-2])

# 指定位置及其后面全部
print(name[2:])
```

```python
eha
ai
ehai
ehai月海

进程已结束,退出代码0
```

4. 加号 `+` 是字符串连接运算符，星号 `*` 是重复操作

```python
# @Time     : 2023/3/3 15:28
# @Author   : 月海
# @File     : 02_字符串_02
# @Project  : 01_python

name = "yuehai月海"

# 加号 `+` 是字符串连接运算符
print(name + "可爱")

# 星号 `*` 是重复操作
print(name*2)

```

```python
yuehai月海可爱
yuehai月海yuehai月海

进程已结束,退出代码0
```

5. Python 列表截取可以接收第三个参数，参数作用是截取的步长（取当前位置后面的第几个字符），以下实例在索引 1 到索引10的位置并设置为步长为 2（间隔一个位置）来截取字符串

```python
# @Time     : 2023/3/3 15:34
# @Author   : 月海
# @File     : 02_字符串_03
# @Project  : 01_python

name = "yuehai月海"

print((name * 2)[1:10:2])
```

```python
uhi海u

进程已结束,退出代码0
```

### ②、转义字符

在需要在字符中使用特殊字符时，python 用反斜杠 `\` 转义字符。如下表：

| 转义字符    | 描述                                                     |
| ----------- | -------------------------------------------------------- |
| `\`(在行尾时) | 续行符                                                   |
| `\\`          | 反斜杠符号                                               |
| `\'`          | 单引号                                                   |
| `\"`          | 双引号                                                   |
| `\a`          | 响铃                                                     |
| `\b`          | 退格(Backspace)                                          |
| `\e`          | 转义                                                     |
| `\000`        | 空                                                       |
| `\n`          | 换行                                                     |
| `\v`          | 纵向制表符                                               |
| `\t`          | 横向制表符                                               |
| `\r`          | 回车                                                     |
| `\f`          | 换页                                                     |
| `\oy`y        | 八进制数，y 代表 0~7 的字符，例如：`\012` 代表换行。       |
| `\xyy`        | 十六进制数，以 `\x` 开头，yy 代表的字符，例如：`\x0a` 代表换行 |
| `\other`      | 其它的字符以普通格式输出                                 |

### ③、字符串运算符

下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

| 操作符 | 描述                                                                                                                                                                                                         | 实例                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| `+`      | 字符串连接                                                                                                                                                                                                   | `>>>a + b` -> `'HelloPython'` |
| `*`      | 重复输出字符串                                                                                                                                                                                               | `>>>a * 2` -> `'HelloHello'`   |
| `[]`     | 通过索引获取字符串中字符                                                                                                                                                                                     | `>>>a[1]` -> `'e'`            |
| `[ : ]`  | 截取字符串中的一部分                                                                                                                                                                                         | `>>>a[1:4]` -> `'ell'`        |
| `in`     | 成员运算符 - 如果字符串中包含给定的字符返回 True                                                                                                                                                             | `>>>"H" in a` -> `True`       |
| `not in` | 成员运算符 - 如果字符串中不包含给定的字符返回 True                                                                                                                                                           | `>>>"M" not in a` -> `True`   |
| `r/R`    | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 <br/>原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | `>>>print r'\n'`<br>`\n`<br>`>>> print R'\n'`<br>`\n` |

### ④、字符串格式化

1. Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 `%s` 的字符串中。
2. 在 Python 中，字符串格式化使用与 C 中 `sprintf` 函数一样的语法
3. python 字符串格式化符号：

| 符号 | 描述                                 |
| ---- | ------------------------------------ |
| `%c` | 格式化字符及其ASCII码                |
| `%s` | 格式化字符串                         |
| `%d` | 格式化整数                           |
| `%u` | 格式化无符号整型                     |
| `%o` | 格式化无符号八进制数                 |
| `%x` | 格式化无符号十六进制数               |
| `%X` | 格式化无符号十六进制数（大写）       |
| `%f` | 格式化浮点数字，可指定小数点后的精度 |
| `%e` | 用科学计数法格式化浮点数             |
| `%E` | 作用同`%e`，用科学计数法格式化浮点数   |
| `%g` | `%f`和`%e`的简写                         |
| `%G` | `%F` 和 `%E` 的简写                      |
| `%p` | 用十六进制数格式化变量的地址         |

4. 格式化操作符辅助指令：

| 符号    | 功能                                                                              |
| ------- | --------------------------------------------------------------------------------- |
| `*`     | 定义宽度或者小数点精度                                                            |
| `-`     | 用做左对齐                                                                        |
| `+`     | 在正数前面显示加号 `+`                                                           |
| `<sp>`  | 在正数前面显示空格                                                                |
| `#`     | 在八进制数前面显示零 `0`，在十六进制前面显示 `0x` 或者 `0X` (取决于用的是 `x` 还是 `X`) |
| `0`     | 显示的数字前面填充 `0` 而不是默认的空格                                             |
| `%`     | `%%` 输出一个单一的 `%`                                                             |
| `(var)` | 映射变量(字典参数)                                                                |
| `m.n.`    | m 是显示的最小总宽度，n 是小数点后的位数(如果可用的话)                             |

### ⑤、三引号（跨行赋值）

1. Python 中三引号可以将复杂的字符串进行赋值。
2. Python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
3. 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。

```python
 errHTML = '''
	<HTML><HEAD><TITLE>
	Friends CGI Demo</TITLE></HEAD>
	<BODY><H3>ERROR</H3>
	<B>%s</B><P>
	<FORM><INPUT TYPE=button VALUE=Back
	ONCLICK="window.history.back()"></FORM>
	</BODY></HTML>
'''
cursor.execute('''
	CREATE TABLE users (  
	login VARCHAR(8), 
	uid INTEGER,
	prid INTEGER)
	''')
```

### ⑥、Unicode 字符串

1. Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：

```python
>>> u'Hello World !'
u'Hello World !'
```

2. 引号前小写的 `u` 表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：

```python
>>> u'Hello\u0020World !'
u'Hello World !'
```

### ⑦、内置函数与方法

常用
| 函数                | 描述                                                                                                            |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| len                 | 获取字符串的长度。                                                                                   |
| find                | 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1. |
| startswith/endswith | 判断字符串是不是以指定字符开头/结尾                                                                               |
| count               | 返回字符串在 start 和 end 之间，在整个字符串里面出现的次数                                                                 |
| replace             | 替换字符串中指定的内容，如果指定次数 count，则替换不会超过 count 次。                                              |
| split               | 通过参数的内容切割字符串为数组                                                                                        |
| upper,lower         | 将字符串中的大小写互换                                                                                          |
| strip               | 去两边空格                                                                                                          |
| join                | 将序列中的元素以指定的字符连接生成一个新的字符串；先输出后面的一个字符，然后全部输出前面的字符、然后再次输出后面的第二个字符，然后全部输出前面的字符、以此类推                                                                                                      |

```python
# @Time     : 2023/3/6 9:41
# @Author   : 月海
# @File     : 01_内置函数
# @Project  : 01_python

name = 'YueHai-月海'

# len	获取字符串的长度。
print(len(name))

# find	查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1.
print(name.find('月海'))

# startswith,endswith	判断字符串是不是以指定字符开头/结尾
print(name.startswith('Y'), name.endswith('Y'))

# count	返回字符串在 start 和 end 之间，在整个字符串里面出现的次数
print(name.count('Y', 0, ))

# replace	替换字符串中指定的内容，如果指定次数 count，则替换不会超过 count 次。
print(name.replace('月海', '言'))

# split	通过参数的内容切割字符串为数组
print(name.split('-'))

# upper,lower	将字符串中的大小写互换
print(name.upper(), name.lower())

# strip	去两边空格
name2 = ' 月 海 '
print(name2.strip())

# join	将序列中的元素以指定的字符连接生成一个新的字符串；先输出后面的一个字符，然后全部输出前面的字符、然后再次输出后面的第二个字符，然后全部输出前面的字符、以此类推
print(name.join('+-*/'))
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\03_数据类型2\01_字符串\01_内置函数.py 
9
7
True False
1
YueHai-言
['YueHai', '月海']
YUEHAI-月海 yuehai-月海
月 海
+YueHai-月海-YueHai-月海*YueHai-月海/

进程已结束,退出代码0
```

### ⑧、模板字符串

1. 在字符串前加：`f`
2. 例子：`print(f'一起玩{self.name}')`

## 4、`List` 列表（集合）

> https://www.runoob.com/python3/python3-list.html

### ①、初识

1. List（列表） 是 Python 中使用最频繁的数据类型。
2. 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
3. <font color="#c00000">列表用 `[ ]` 标识，是 python 最通用的复合数据类型。</font>
4. 列表中值的切割也可以用到变量 `[头下标:尾下标]` ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230303154545.png)

5. 加号 `+` 是列表连接运算符，星号 `*` 是重复操作

```python
# @Time     : 2023/3/3 15:49
# @Author   : 月海
# @File     : 03_列表
# @Project  : 01_python

# 定义列表
list1 = ['月海', 16, 0, ['yuehai', 'yan']]
list2 = ['言', 14, 0, ['yan', 'yu']]

# 截取
print(list1[0:3])

# 加号 `+` 是列表连接运算符
print(list1 + list2)

# 星号 `*` 是重复操作
print(list1 * 2)

# 修改列表
list1[0] = "yuehai"
print(list1)
```

```python
['月海', 16, 0]
['月海', 16, 0, ['yuehai', 'yan'], '言', 14, 0, ['yan', 'yu']]
['月海', 16, 0, ['yuehai', 'yan'], '月海', 16, 0, ['yuehai', 'yan']]
['yuehai', 16, 0, ['yuehai', 'yan']]

进程已结束,退出代码0
```

### ②、列表脚本操作符
列表对 `+` 和 `*` 的操作符与字符串相似。`+` 号用于组合列表，`*` 号用于重复列表。

| Python 表达式                | 结果                         | 描述                 |
| ---------------------------- | ---------------------------- | -------------------- |
| len([1, 2, 3])               | 3                            | 长度                 |
| [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | 组合                 |
| ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
| 3 in [1, 2, 3]               | True                         | 元素是否存在于列表中 |
| for x in [1, 2, 3]: print x, | 1 2 3                        | 迭代                 |

### ③、列表截取

| Python 表达式 | 结果                 | 描述                     |
| ------------- | -------------------- | ------------------------ |
| L[2]          | 'Taobao'             | 读取列表中第三个元素     |
| L[-2]         | 'Runoob'             | 读取列表中倒数第二个元素 |
| L[1:]         | ['Runoob', 'Taobao'] | 从第二个元素开始截取列表 |

```python
>>>L = ['Google', 'Runoob', 'Taobao']
>>> L[2]
'Taobao'
>>> L[-2]
'Runoob'
>>> L[1:]
['Runoob', 'Taobao']
>>>
```

### ④、列表增删改查
1. 增：
	1. `append()`： 在末尾添加元素
	2. `insert()`： 在指定位置插入元素
	3. `extend()`： 合并两个列表
2. 删：
	1. `del`：根据下标进行删除
	2. `pop()`：删除最后一个元素
	3. `remove()`：根据元素的值进行删除
3. 改：使用下标修改即可
4. 查：
	1. `in`（存在）：如果存在那么结果为 true，否则为 false
	2. `not in`（不存在）：如果不存在那么结果为 true，否则 false
	3. `count()`：统计某个元素在列表中出现的次数
	4. `index()`：从列表中找出某个值第一个匹配项的索引位置
	5. `reverse()`：反向列表中元素
5. 排序：sort(cmp=None, key=None, reverse=False)：对原列表进行排序
	1. cmp：如果指定了该参数会使用该参数的方法进行排序。
	2. key：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
	3. reverse：排序规则，`reverse = True` 降序， `reverse = False` 升序（默认）。
	4. 排序的集合中不能出现类型不同的元素

```python
# @Time     : 2023/3/6 11:09
# @Author   : 月海
# @File     : 03_列表_02
# @Project  : 01_python

# 定义集合
list = ['月海', 16, 0, ['yuehai', 'yan']]

# 1. 增：
#   1.1. `append`： 在末尾添加元素
list.append('言')
print(list)
#   1.2. `insert`： 在指定位置插入元素
list.insert(2, '----')
print(list)
#   1.3. `extend`： 合并两个列表
list.extend(['言', 'yan'])
print(list)

# 2. 删：
#   2.1. `del`：根据下标进行删除
del list[-1]
print(list)
#   2.2. `pop`：删除最后一个元素
list.pop()
print(list)
#   2.3. `remove`：根据元素的值进行删除
list.remove('----')
print(list)

# 3. 改：使用下标修改即可
list[0] = '月-海'
print(list)

# 4. 查：
#   4.1. in（存在）：如果存在那么结果为 true，否则为 false
print('月-海' in list)
#   4.2. not in（不存在）：如果不存在那么结果为 true，否则 false
print('月-海' not in list)
#   4.3. count()：统计某个元素在列表中出现的次数
print(list.count(16))
# 4.4. `index()`：从列表中找出某个值第一个匹配项的索引位置
print(list.index(0))
# 4.5. `reverse()`：反向列表中元素
list.reverse()
print(list)

# 5. sort(cmp=None, key=None, reverse=False)：对原列表进行排序
#   5.1. cmp：如果指定了该参数会使用该参数的方法进行排序。
#   5.2. key：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#   5.3. reverse：排序规则，`reverse = True` 降序， `reverse = False` 升序（默认）。
list2 = [463, 5, 41, 653, 41]
list2.sort()
print(list2)

# 指定 key
list3 = [[5, 4], [7, 5], [10, 1], [4, 4, 13]]
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 指定第二个元素排序
list3.sort(key=takeSecond)
print(list3)
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\01_数据类型\03_列表_02.py 
['月海', 16, 0, ['yuehai', 'yan'], '言']
['月海', 16, '----', 0, ['yuehai', 'yan'], '言']
['月海', 16, '----', 0, ['yuehai', 'yan'], '言', '言', 'yan']
['月海', 16, '----', 0, ['yuehai', 'yan'], '言', '言']
['月海', 16, '----', 0, ['yuehai', 'yan'], '言']
['月海', 16, 0, ['yuehai', 'yan'], '言']
['月-海', 16, 0, ['yuehai', 'yan'], '言']
True
False
1
2
['言', ['yuehai', 'yan'], 0, 16, '月-海']
[5, 41, 41, 463, 653]
[[10, 1], [5, 4], [4, 4, 13], [7, 5]]

进程已结束,退出代码0
```

### ⑤、其他函数

1. `len(list)`：列表元素个数
2. `max(list)`：返回列表元素最大值
3. `min(list)`：返回列表元素最小值
4. `list(seq`)：将元组转换为列表

```python
# @Time     : 2023/3/6 13:40
# @Author   : 月海
# @File     : 03_列表_03
# @Project  : 01_python

list1 = [463, 5, 41, 653, 41]

# 1. `len(list)`：列表元素个数
print(len(list1))

# 2. `max(list)`：返回列表元素最大值
print(max(list1))

# 3. `min(list)`：返回列表元素最小值
print(min(list1))

# 4. `list(seq`)：将元组转换为列表
arr = ("月海", 16, 0, ("yuehai", "yan"))
listArr = list(arr)
print(listArr)

```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\01_数据类型\03_列表_03.py 
5
653
5
['月海', 16, 0, ('yuehai', 'yan')]

进程已结束,退出代码0
```

## 5、`Tuple` 元组（只读集合）

> https://www.runoob.com/python3/python3-tuple.html

1. 元组是另一个数据类型，类似于 List（列表）
2. 元组用 `()` 标识。内部元素用逗号隔开。但是<font color="#c00000">元组不能二次赋值，相当于只读列表</font>。
3. 因为不可修改，所以执行效率很高

```python
# @Time     : 2023/3/3 15:55
# @Author   : 月海
# @File     : 05_元组
# @Project  : 01_python

# 定义
arr = ("月海", 16, 0, ("yuehai", "yan"))

# 截取
print(arr[2:4])

# 加号 `+` 是列表连接运算符
print(arr + arr)

# 星号 `*` 是重复操作
print(arr * 2)

# 重新赋值，会报错
arr[0] = "言"
```

```python
(0, ('yuehai', 'yan'))
('月海', 16, 0, ('yuehai', 'yan'), '月海', 16, 0, ('yuehai', 'yan'))
('月海', 16, 0, ('yuehai', 'yan'), '月海', 16, 0, ('yuehai', 'yan'))
Traceback (most recent call last):
  File "D:\Idea\save\python\0_study\01_python\01_数据类型\05_元组.py", line 19, in <module>
    arr[0] = "言"
    ~~~^^^
TypeError: 'tuple' object does not support item assignment

进程已结束,退出代码1
```

3. 元组内置函数：
	1. len(tuple)：计算元组元素个数。
	2. max(tuple)：返回元组中元素最大值。
	3. min(tuple)：返回元组中元素最小值。
	4. tuple(seq)：将列表转换为元组。

```python
# @Time     : 2023/3/6 14:08
# @Author   : 月海
# @File     : 05_元组_02
# @Project  : 01_python

arr = (463, 5, 41, 653, 41)

# 1. len(tuple)：计算元组元素个数。
print(len(arr))

# 2. max(tuple)：返回元组中元素最大值。
print(max(arr))

# 3. min(tuple)：返回元组中元素最小值。
print(min(arr))

# 4. tuple(seq)：将列表转换为元组。
list1 = ['月海', 16, 0, ['yuehai', 'yan']]
print(tuple(list1))
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\01_数据类型\05_元组_02.py 
5
653
5
('月海', 16, 0, ['yuehai', 'yan'])

进程已结束,退出代码0
```

## 6、`Dictionary` 字典（map）

> https://www.runoob.com/python3/python3-dictionary.html

### ①、初识
1. 字典(dictionary)是除列表以外 python 之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
2. 两者之间的区别在于：<font color="#c00000">字典当中的元素是通过键来存取的，而不是通过偏移存取</font>。
3. 字典用 `{ }` 标识。字典由索引 `key` 和它对应的值 `value` 组成。

```python
# @Time     : 2023/3/3 16:05
# @Author   : 月海
# @File     : 06_字典
# @Project  : 01_python

# 定义
map = {'name': '月海', 'age': 16, 'sex': 0}

# 打印
print(map)

# 读取
print(map['name'])

# 修改
map['age'] = 17
print(map)
```

```python
{'name': '月海', 'age': 16, 'sex': 0}
月海
{'name': '月海', 'age': 17, 'sex': 0}

进程已结束,退出代码0
```
### ②、字典增删改查

1. 增：如果在使用 `变量名['键'] = 数据` 时，这个“键”在字典中不存在，那么就会新增这个元素
2. 删：
	1. `del 变量名['键']`：删除字典中指定的键
	2. `pop(key[,default])`：删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
	3. `popitem()`：返回并删除字典中的最后一对键和值。
	4. `del 变量名`：删除整个字典
	5. `clear()`：清空字典
3. 改：如果在使用 `变量名['键'] = 数据` 时，这个“键”在字典中存在，那么就会修改这个元素为本次指定的值
4. 查：
	1. `变量名['键']`、`get(key, default=None)`：返回指定键的值，如果值不在字典中返回 default 值
	2. ``setdefault(key, default=None)` 和 `get()` 类似, 但如果键不存在于字典中，将会添加键并将值设为 default`

```python
# @Time     : 2023/3/6 14:25
# @Author   : 月海
# @File     : 06_字典_02
# @Project  : 01_python

map = {'name': '月海', 'age': 16, 'sex': 0}

# 1. 增：如果在使用 `变量名['键'] = 数据` 时，这个“键”在字典中不存在，那么就会新增这个元素
map['teacher'] = '羽'
print(map)

# 3. 改：如果在使用 `变量名['键'] = 数据` 时，这个“键”在字典中存在，那么就会修改这个元素为本次指定的值
map['age'] = 17
print(map)

# 4. 查：
#   4.1. `变量名['键']`、get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
print(map['name'], map.get('age'))
#   4.2. `setdefault(key, default=None)` 和 `get()` 类似, 但如果键不存在于字典中，将会添加键并将值设为 default
map.setdefault('teacher2', '羽2')
print(map)

# 2. 删：
#   2.1. `del 变量名['键']`：删除字典中指定的键
del map['teacher']
print(map)
#   2.2. `pop(key[,default])`：删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
print(map.pop('teacher2'))
print(map)
#   2.3. `popitem()`：返回并删除字典中的最后一对键和值。
print(map.popitem())
print(map)
#   2.2. `del 变量名`：删除整个字典
del map
print(map)
#   2.3. `clear()`：清空字典
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\01_数据类型\06_字典_02.py 
{'name': '月海', 'age': 16, 'sex': 0, 'teacher': '羽'}
{'name': '月海', 'age': 17, 'sex': 0, 'teacher': '羽'}
月海 17
{'name': '月海', 'age': 17, 'sex': 0, 'teacher': '羽', 'teacher2': '羽2'}
{'name': '月海', 'age': 17, 'sex': 0, 'teacher2': '羽2'}
羽2
{'name': '月海', 'age': 17, 'sex': 0}
('sex', 0)
{'name': '月海', 'age': 17}
<class 'map'>

进程已结束,退出代码0
```

### ③、内置函数与方法

| 函数           | 描述                                               |
| -------------- | -------------------------------------------------- |
| `len(dict)`      | 计算字典元素个数，即键的总数。                     |
| `str(dict`)      | 输出字典可打印的字符串表示。                       |
| `type(variable)` | 返回输入的变量类型，如果变量是字典就返回字典类型。 |
|`dict.copy()`|返回一个字典的浅复制|
|`dict.fromkeys(seq[, val])`|创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值|
|`dict.has_key(key)`|如果键在字典 dict 里返回 true，否则返回 false|
|<font color="#ff0000">`dict.items()`</font>|以列表返回可遍历的 (键, 值) 元组数组|
|d`ict.keys()`|以列表返回一个字典所有的键|
|`dict.update(dict2)`|把字典 dict2 的键/值对更新到 dict 里|
|`dict.values()`|以列表返回字典中的所有值|

## 7、`Set` 集合

> https://www.runoob.com/python3/python3-set.html

1. 集合 `set` 是一个<font color="#ff0000">无序的不重复</font>元素序列。
2. 可以使用大括号 `{ }` 或者 `set()` 函数创建集合
3. 注意：创建一个空集合必须用 `set()` 而不是 `{ }`，因为 `{ }` 是用来创建一个空字典

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/10 8:25
# @Author   : 月海
# @File     : _09_set
# @Project  : 01_python

# 创建 set
my_set1 = {'月海', '言', '月海', 'yuehai'}
my_set2 = {'羽', '言', '月海', 'yuehai'}
print(my_set1, my_set2)

# a - b：集合a中包含而集合b中不包含的元素
# a | b：集合a或b中包含的所有元素
# a & b：集合a和b中都包含了的元素
# a ^ b：不同时包含于a和b的元素
print(my_set1 | my_set2)

# 添加元素
my_set1.add('yan')
print(my_set1)

# 移除元素
my_set1.remove('yuehai')
print(my_set1)
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe D:\Idea\save\python\0_study\01_python\01_数据类型\_09_set.py 
{'月海', 'yuehai', '言'} {'月海', 'yuehai', '言', '羽'}
{'月海', 'yuehai', '言', '羽'}
{'月海', 'yuehai', '言', 'yan'}
{'月海', '言', 'yan'}

进程已结束,退出代码0
```

## 8、类型转换

1. 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
2. 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

|函数|说明|
|--|--|
|int(x [,base])|将x转换为一个整数|
|long(x [,base] )|将x转换为一个长整数|
|float(x)|将x转换到一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象 x 转换为字符串|
|repr(x)|将对象 x 转换为表达式字符串|
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象|
|tuple(s)|将序列 s 转换为一个元组|
|list(s)|将序列 s 转换为一个列表|
|set(s)|转换为可变集合|
|dict(d)|创建一个字典。d 必须是一个序列 (key,value)元组。|
|frozenset(s)|转换为不可变集合|
|chr(x)|将一个整数转换为一个字符|
|unichr(x)|将一个整数转换为Unicode字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

# 七、函数（方法）

1. 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
2. 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

## 1、定义函数与调用函数

1. 定义函数：
	1. 函数代码块以 `def` 关键词开头，后接<font color="#ff0000">函数名</font>和圆括号 <font color="#ff0000">`()`</font>。
	2. 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
	3. 函数的第一行语句可以选择性地使用文档字符串：用于存放函数说明。
	4. 函数内容以冒号 `:` 起始，并且缩进。
	5. `return [表达式]` 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。
2. 调用函数：直接使用函数名称调用

```python
# @Time     : 2023/3/6 15:00
# @Author   : 月海
# @File     : 01_定义函数与调用函数
# @Project  : 01_python

# 定义函数
def fun(name):
    print('名字是：' + name)


# 调用函数
fun('月海')
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\03_函数\01_定义函数与调用函数.py 
名字是：月海

进程已结束,退出代码0
```

## 2、函数参数

### ①、可更改(mutable)与不可更改(immutable)对象

1. 在 python 中，类型属于对象，变量是没有类型的；下面代码中，`[1,2,3]` 是 List 类型，`Runoob` 是 String 类型，而变量 a 是没有类型，它仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象

```python
a=[1,2,3]
 
a="Runoob"
```

2. 可更改(mutable)与不可更改(immutable)对象
3. 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list、dict 等则是可以修改的对象
	1. 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
	2. 可变类型：变量赋值 `la=[1,2,3,4]` 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了
4. python 函数的参数传递
	1. 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
	2. 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），<font color="#ff0000">则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响</font>
5. python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
6. python 传不可变对象实例：实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print b # 结果是 2
```

7. 传可变对象实例：实例中传入函数的和在末尾添加新内容的对象用的是同一个引用，故输出结果如下

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print "函数外取值: ", mylist
```

```python
函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
```



### ②、必备参数

1. 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print str
   return
 
#调用printme函数
printme()
```

2. 调用 `printme()` 函数，你必须传入一个参数，不然会出现语法错误：

```python
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    printme()
TypeError: printme() takes exactly 1 argument (0 given)
```

### ③、关键字参数

1. 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
2. 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )
```

```python
Name:  miki
Age  50
```

### ④、默认参数

调用函数时，默认参数的值如果没有传入，则被认为是默认值。下例会打印默认的 age，如果 age 没有被传入：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )
```

```python
Name:  miki
Age  50
Name:  miki
Age  35
```

### ⑤、不定长参数
1. 你可能需要一个函数能处理比当初声明时更多的参数。
2. 这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名；加了星号 `*` 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
3. 如果单独出现星号 `*`，则星号 `*` 后的参数必须用关键字传入

```python
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
```

```python
输出: 
70
(60, 50)
```

3. 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
4. 还有一种就是参数带两个星号 `**`，加了两个星号 `**` 的参数会以字典的形式导入

```python
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
```

```python
输出: 
1
{'a': 2, 'b': 3}
```

### ⑥、匿名函数

1. python 使用 lambda 来创建匿名函数。
2. lambda 只是一个表达式，函数体比 def 简单很多。
3. lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
4. lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
5. 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
6. 语法：`lambda [arg1 [,arg2,.....argn]]:expression`；`lambda 参数1， 参数2 : 逻辑表达式`

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
```

```python
相加后的值为 :  30
相加后的值为 :  40
```

## 3、return 语句
1. `return [表达式]` ：退出函数，选择性地向调用方返回一个表达式。
2. 不带参数值的 return 语句返回 None

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print "函数内 : ", total
   return total
 
# 调用sum函数
total = sum( 10, 20 )
```

```python
函数内 :  30
```

## 4、变量作用域
1. 一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
2. 变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
	1. 全局变量
	2. 局部变量
3. <font color="#ff0000">定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域</font>。
4. 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
5. 调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total
 
#调用sum函数
sum( 10, 20 )
print "函数外是全局变量 : ", total
```

```python
函数内是局部变量 :  30
函数外是全局变量 :  0
```

## 5、模块

1. Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
2. 模块让你能够有逻辑地组织你的 Python 代码段。
3. 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
4. 模块能定义函数，类和变量，模块里也能包含可执行的代码

---
### ①、本地自定义包

1. 模块结构

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230306162442.png)

2. 创建 module 包，在其中创建 testModule.py 文件

```python
# @Time     : 2023/3/6 16:09
# @Author   : 月海
# @File     : testModule
# @Project  : 01_python

# 定义函数
def fun():
    print('module -> testModule')

```

3. 创建 module2 包，在其中创建 testModule1.py、testModule2.py 文件

```python
# @Time     : 2023/3/6 16:13
# @Author   : 月海
# @File     : testModule1
# @Project  : 01_python

# 定义函数
def fun():
    print('module2 -> testModule1')
```

```python
# @Time     : 2023/3/6 16:13
# @Author   : 月海
# @File     : testModule2
# @Project  : 01_python

# 定义函数
def fun():
    print('module2 -> testModule1')
```

4. 创建 02_模块.py文件，调用模块

```python
# @Time     : 2023/3/6 15:55
# @Author   : 月海
# @File     : 02_模块
# @Project  : 01_python

# 使用 import 导入指定包中的指定模块
import module.testModule as test
test.fun()

# 使用 from 导入指定包，再使用 import 导入其中的指定模块
# from module2 import testModule1

# 使用 from 导入指定包中的所有模块
from module2.testModule1 import *
fun()
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\03_函数\02_模块.py 
module -> testModule
module2 -> testModule1

进程已结束,退出代码0
```

### ②、导入第三方包

1. 在 PyCharm中，点击右下角 python，然后点击解释器设置

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307105308.png)

2. 在弹出来的页面中点击软件包上方的 +

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307105451.png)

3. 在弹出来的页面中输入包名，点击安装即可

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307105717.png)

## 6、一些内置函数

# 八、文件 File
## 1、文件的打开与读写 `open()`

1. Python `open()` 方法用于打开一个文件，并返回文件对象。
2. 在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
3. 注意：使用 `open()` 方法一定要保证关闭文件对象，即调用 `close()` 方法。
4. `open()` 函数常用形式是接收两个参数：文件名 `file` 和模式 `mode`：`open(file, mode='r')`
5. 完整的语法格式为：`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
	1. `file`：必需，文件路径（相对或者绝对路径）。
	2. `mode`：可选，文件打开模式
	3. `buffering`：设置缓冲
	4. `encoding`：一般使用 utf8
	5. `errors`：报错级别
	6. `newline`：区分换行符
	7. `closefd`：传入的 file 参数类型
	8. `opener`：设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
6. `mode` 默认为文本模式，如果要以二进制模式打开，加上 b，参数有：

|模式| 描述                                                                                                                                                               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| t    | 文本模式 (默认)。                                                                                                                                                  |
| <font color="#ff0000">x</font>    | <font color="#ff0000">写模式，新建一个文件，如果该文件已存在则会报错</font>。                                                                                                                   |
| b    | 二进制模式。                                                                                                                                                       |
| +    | 打开一个文件进行更新(可读可写)。                                                                                                                                   |
| U    | 通用换行模式（Python 3 不支持）。                                                                                                                                  |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。                                                                                                   |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。                                                           |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。                                                                                                                 |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。                                                                         |
| <font color="#ff0000">w</font>    | <font color="#ff0000">打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。</font>                                           |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。   |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                                             |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。     |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。             |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。                                 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。                                             |

7. file 对象使用 open() 函数来创建，下表列出了 file 对象常用的函数

| 函数                        | 描述                                                                                                                                                     |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file.close()`                | 关闭文件。关闭后文件不能再进行读写操作。                                                                                                                 |
| `file.flush()`                | 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。                                                                   |
| `file.fileno()`               | 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如 os 模块的 read 方法等一些底层操作上。                                                          |
| `file.isatty()`               | 如果文件连接到一个终端设备返回 True，否则返回 False。                                                                                                    |
| `file.read([size]`)           | 从文件读取指定的字节数，如果未给定或为负则读取所有。                                                                                                     |
| `file.readline([size]`)       | 读取整行，包括 `\n` 字符。                                                                                                                               |
| `file.readlines([sizeint])`   | 读取所有行并返回列表，若给定 sizeint>0，返回总和大约为 sizeint 字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。                                |
| `file.seek(offset[, whence])` | 移动文件读取指针到指定位置                                                                                                                               |
| `file.tell()`                 | 返回文件当前位置。                                                                                                                                       |
| `file.truncate([size])`       | 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。 |
| `file.write(str)`             | 将字符串写入文件，返回的是写入的字符长度。                                                                                                               |
| `file.writelines(sequence)`   | 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符                                                                                       |

```python
# @Time     : 2023/3/7 8:35
# @Author   : 月海
# @File     : 01_文件打开关闭
# @Project  : 01_python

# 打开文件
file = open('./file/《一阙晴空》BY莫天天.txt', encoding='utf-8')

# readlines(1024)：读取所有行并返回列表，若给定 sizeint>0，返回总和大约为 sizeint 字节的行
for line in file.readlines(1024):
    if line != '\n':
        # strip()：用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        print(line.strip('\n'))

# 关闭流
file.close()
```

## 2、文件的创建
创建文件也是使用 `open` 函数，不过需指定不同的 `mode`

```python
# @Time     : 2023/3/7 8:49
# @Author   : 月海
# @File     : 02_创建文件
# @Project  : 01_python

# w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
file = open('./file/月海.txt', 'w')
# 写入数据
file.write('yuehai月海')
# 关闭流
file.close()
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307093501.png)

## 3、文件的序列化

1. 通过文件操作，我们可以将字符串写入到一个本地文件。但是，如果是一个对象(例如列表、字典、元组等)，就无法直接写入到一个文件里，需要对这个对象进行序列化，然后才能写入到文件里。
2. 设计一套协议，按照某种规则，把内存中的数据转换为字节序列，保存到文件，这就是序列化，反之，从文件的字节序列恢复到内存中，就是反序列化。
	1. 对象 -> 字节序列：序列化
	2. 字节序列 -> 对象：反序列化
3. Python 中提供了 JSON 这个模块用来实现数据的序列化和反序列化
4. JSON 提供了 `dump` 和 `dumps` 方法，将一个对象进行序列化。`dumps` 方法的作用是把对象转换成为字符串，它本身不具备将数据写入到文件的功能

```python
# @Time     : 2023/3/7 10:13
# @Author   : 月海
# @File     : 03_序列化
# @Project  : 01_python

# 引入 json 模块
import json

# 定义集合
myList = ['月海', 16, 0, ['yuehai', 'yan']]

# 创建文件，序列化
file = open('./file/json 序列化', 'w')
# 序列化集合
result = json.dumps(myList)
# 打印序列化后的集合
print("序列化后：" + result)
# 将序列化后的集合写入文件
file.write(result)
# 关闭文件流
file.close()

# 读取文件，反序列化
file2 = open('./file/json 序列化')
# 调用 load 方法，将文件里的内容加载成为一个 Python 对象
result2 = json.load(file2)
# 打印反序列化后的集合
print("反序列化后：")
print(result2)
# 关闭文件流
file2.close()
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\04_文件File\03_序列化.py 
序列化后：["\u6708\u6d77", 16, 0, ["yuehai", "yan"]]
反序列化后：
['月海', 16, 0, ['yuehai', 'yan']]

进程已结束,退出代码0
```

## 4、OS 文件/目录方法

> os 模块提供了非常丰富的方法用来处理文件和目录
> 
> https://www.runoob.com/python3/python3-os-file-methods.html

# 九、对象

## 1、定义与实例化类

1. 创建类

```python
# @Time     : 2023/3/7 11:21
# @Author   : 月海
# @File     : 01_成员方法_01_class
# @Project  : 01_python

# 定义类
class YueHai:
    # 定义属性（可以省略）
    # name = None
    # age = None

    """
        self 关键字是成员方法定义的时候，必须填写的。它用来表示类对象自身的意思
        当我们使用类对象调用方法的是，self 会自动被 python 传入；在方法内部，想要访问类的成员变量，必须使用 self
        不过 self 关键字尽管在参数列表中，但是传参的时候可以忽略它
        感觉类似 this
    """

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义方法
    def play(self):
        print(f'玩{self.name}')
```

2. 使用类

```python
# @Time     : 2023/3/7 11:20
# @Author   : 月海
# @File     : 01_成员方法_01
# @Project  : 01_python

# 引入类
from YueHai import YueHai

# 实例化类
yuehai = YueHai('月海', 16)

# 调用类属性
print(yuehai.name)
print(yuehai.age)

# 修改类属性
yuehai.age = 17
print(yuehai.age)

# 调用类方法
yuehai.play()
```

## 2、其他内置方法
1. 上文学习的 `__init__` 构造方法，是 Python 类内置的方法之一。
2. 这些内置的类方法，各自有各自特殊的功能，这些内置方法我们称之为：魔术方法，类似 java 的某些重载方法
3. 魔术方法非常多，我们学习几个常见的即可：
	1. `__str__` 字符串方法
	2. `__lt__` 小于比较
	3. `__gt__` 大于比较
	4. `__le__` 小于等于比较
	5. `__ge__` 大于等于比较
	6. `__eq__` 等于比较

```python
# @Time     : 2023/3/7 11:21
# @Author   : 月海
# @File     : 01_成员方法_01_class
# @Project  : 01_python

# 定义类
class YueHai:
    # 定义属性（可以省略）
    # name = None
    # age = None

    """
        self 关键字是成员方法定义的时候，必须填写的。它用来表示类对象自身的意思
        当我们使用类对象调用方法的是，self 会自动被 python 传入；在方法内部，想要访问类的成员变量，必须使用 self
        不过 self 关键字尽管在参数列表中，但是传参的时候可以忽略它
        感觉类似 this
    """

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义方法
    def play(self):
        print(f'玩{self.name}')

    # __str__ 字符串方法，类似 toString
    def __str__(self):
        return f'YueHai: name={self.name}, age={self.age}'

    # __lt__ 小于符号比较
    # __gt__ 大于比较
    def __lt__(self, other):
        # < ：即 对象1 < 对象2 会返回 true
        return self.age < other.age

    # __le__ 小于等于比较
    # __ge__ 大于等于比较
    def __le__(self, other):
        # <= ：即 对象1 <= 对象2 会返回 true
        return self.age <= other.age

    # __eq__ 等于比较
    def __eq__(self, other):
        # == ：即 对象1 == 对象2 会返回 true
        return self.name == other.name
```

```python
# @Time     : 2023/3/7 13:11
# @Author   : 月海
# @File     : 02_魔术方法
# @Project  : 01_python

# 引入类
from YueHai import YueHai

# 实例化类
yuehai = YueHai('月海', 16)
yan = YueHai('言', 16)

print(yuehai < yan)
print(yuehai <= yan)
print(yuehai == yan)
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\06_对象\02_魔术方法.py 
False
True
False

进程已结束,退出代码0
```

## 3、封装

1. 定义私有成员的方式非常简单：
	1. 私有成员变量：变量名以 `__` 开头（2个下划线）
	2. 私有成员方法：方法名以 `__` 开头（2个下划线）
2. 私有方法无法直接被类对象使用，私有变量无法赋值，也无法获取值
3. 私有成员无法被类对象使用，但是可以被其它的成员使用

```python
# @Time     : 2023/3/7 13:37
# @Author   : 月海
# @File     : _03_YueHai
# @Project  : 01_python

# 定义类
class _03_YueHai:
    # 构造方法
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 定义方法
    def play(self):
        print(f'玩{self.__name}')

    # __str__ 字符串方法，类似 toString
    def __str__(self):
        return f'YueHai: name={self.__name}, age={self.__age}'

    # 既然封装了，就会有 get、set 方法
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

```

```python
# @Time     : 2023/3/7 13:38
# @Author   : 月海
# @File     : 02_封装
# @Project  : 01_python

# 引入类
from _03_YueHai import _03_YueHai

# 实例化类
yuehai = _03_YueHai('月海', 16)
print(yuehai)

# 直接调用私有属性，报错
# yuehai.__name

# 调用 get 方法
print(yuehai.getName())

# 调用 set 方法
yuehai.setName('言')
print(yuehai.getName())
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\06_对象\03_封装.py 
YueHai: name=月海, age=16
月海
言

进程已结束,退出代码0
```

## 4、继承

1. 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
2. 通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
3. 在python中继承中的一些特点：
	1. 如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看： python 子类继承父类构造函数说明。
	2. 在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
	3. Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
4. 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
5. 多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右）为优先级。即：<font color="#ff0000">先继承的保留，后继承的被覆盖</font>
6. 调用父类方法与属性：`父类名.属性/方法`

```python
# @Time     : 2023/3/7 11:21
# @Author   : 月海
# @File     : 01_成员方法_01_class
# @Project  : 01_python

# 定义类
class YueHai:
    # 定义属性（可以省略）
    # name = None
    # age = 0

    """
        self 关键字是成员方法定义的时候，必须填写的。它用来表示类对象自身的意思
        当我们使用类对象调用方法的是，self 会自动被 python 传入；在方法内部，想要访问类的成员变量，必须使用 self
        不过 self 关键字尽管在参数列表中，但是传参的时候可以忽略它
        感觉类似 this
    """

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义方法
    def play(self):
        print(f'玩{self.name}')

    # __str__ 字符串方法，类似 toString
    def __str__(self):
        return f'YueHai: name={self.name}, age={self.age}'
```

```python
# @Time     : 2023/3/7 13:59
# @Author   : 月海
# @File     : _04_yuehai
# @Project  : 01_python

# 引入类
from YueHai import YueHai


# 继承 YueHai，单继承
class _04_yuehai(YueHai):

    # 自定义方法
    def ageAdd(self):
        self.age += 1

    # 重写父类方法
    def play(self):
        print(f'一起玩{self.name}')
```

```python
# @Time     : 2023/3/7 13:58
# @Author   : 月海
# @File     : _04_继承
# @Project  : 01_python

# 引入类
from _04_yuehai import _04_yuehai

# 实例化类
yuehai = _04_yuehai('月海', 16)
print(yuehai)

# 调用自定义方法
yuehai.ageAdd()
print(yuehai)

# 调用重写方法
yuehai.play()
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\06_对象\_04_继承.py 
YueHai: name=月海, age=16
YueHai: name=月海, age=17
一起玩月海

进程已结束,退出代码0
```

## 5、多态

1. 多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。
2. 多态常作用在继承关系上，比如：
	1. 函数(方法)形参声明接收父类对象
	2. 实际传入父类的子类对象进行工作
	3. 即：以父类做定义声明、以子类做实际工作，用以获得同一行为，不同状态

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307144725.png)

3. 下面父类 Animal 的 speak 方法，是空实现，这种设计的含义是：
	1. 父类用来确定有哪些方法
	2. 具体的方法实现，由子类自行决定
4. 这种写法，就叫做抽象类（也可以称之为接口）
5. 抽象类：含有抽象方法的类称之为抽象类
6. 抽象方法：方法体是空实现的（pass）称之为抽象方法

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307144912.png)

7. 抽象类就好比定义一个标准，包含了一些抽象的方法，要求子类必须实现

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307145132.png)

8. 配合多态，完成：抽象的父类设计（设计标准）、具体的子类实现（实现标准）

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307145138.png)

## 6、类型注解

1. Python 在 3.5 版本的时候引入了类型注解，以方便静态类型检查工具，IDE 等第三方工具。
2. 类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）。
3. 主要功能：
	1. 帮助第三方 IDE 工具（如 PyCharm）对代码进行类型推断，协助做代码提示
	2. 帮助开发者自身对变量进行类型注释
4. 支持：
	1. 变量的类型注解
	2. 函数（方法）形参列表和返回值的类型注解
5. 语法：`形参变量: 类型`

```python
# @Time     : 2023/3/7 14:22
# @Author   : 月海
# @File     : _06_类型注解
# @Project  : 01_python

# 引入类
from YueHai import YueHai


# 定义方法，注解：字符串、数字、布尔、集合、自定义类、元组、字典
def play(name: str, age: int, sex: bool, like: list, attribute: YueHai, fate: tuple, other: dict[str, str]):
    print(f'玩{name}')


play('月海')

```

## 7、动态添加删除属性、方法

### ①、动态添加删除属性

```python
# @Time     : 2023/3/7 16:46
# @Author   : 月海
# @File     : _07_01_动态添加删除属性
# @Project  : 01_python

# 引入类
from YueHai import YueHai

# 实例化类
print('--------实例化类--------')
yuehai = YueHai('月海', 16)
print(yuehai)


# 动态给对象添加属性
print('--------动态给对象添加属性--------')
yuehai.sex = 0
print(yuehai)
print(yuehai.sex)


# 动态给类添加属性
print('--------动态给类添加属性--------')
yuehai2 = YueHai('言', 14)
# 类似与在类中初始化
YueHai.sex = 0
print(yuehai2)
print(yuehai2.sex)
# 重新赋值
yuehai2.sex = 1
print(yuehai2)
print(yuehai2.sex)


# 动态删除对像属性，在整个程序中删除，前面的代码想要访问这个属性也会变为空（或默认值）
# Python 的类属性的删除有两种方法，即：使用 del 语句和使用 delattr 函数
# del 语句和 delattr 函数不仅可以删除类属性还可以删除动态添加的类属性。

# 动态删除对像属性
print('--------动态删除对像属性--------')
del yuehai.name
print(yuehai)

delattr(yuehai, 'age')
print(yuehai)
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\06_对象\_07_01_动态添加删除属性.py 
--------实例化类--------
YueHai: name=月海, age=16
--------动态给对象添加属性--------
YueHai: name=月海, age=16
0
--------动态给类添加属性--------
YueHai: name=言, age=14
0
YueHai: name=言, age=14
1
--------动态删除对像属性--------
YueHai: name=None, age=16
YueHai: name=None, age=0

进程已结束,退出代码0

```

### ②、动态添加方法

```python
# @Time     : 2023/3/8 8:45
# @Author   : 月海
# @File     : _07_02_动态添加删除方法
# @Project  : 01_python


# 引入类
from YueHai import YueHai
# 动态添加方法需要导入 types 模块
import types

# 实例化类
print('--------实例化类--------')
yuehai = YueHai('月海', 16)
yuehai.play()


# 定义需要添加的方法
def study(self):
    print(f'学{self.name}')


# 动态给对象添加方法
print('--------动态给对象添加方法--------')
yuehai.study = types.MethodType(study, yuehai)
yuehai.study()


# 动态给类添加方法
print('--------动态给类添加方法--------')
# 添加方法
YueHai.study = study
# 实例化
yan = YueHai('言', 14)
# 调用动态添加的方法
yan.study()


# Python 的类方法的删除有两种方法，即：使用 del 语句和使用 delattr 函数
# 不能从类的实例中删除类方法，只能删除类中的方法
delattr(YueHai, 'play')
yuehai2 = YueHai('yuehai', 15)
print(yuehai2.name)
yuehai2.play()
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe D:\Idea\save\python\0_study\01_python\06_对象\_07_02_动态添加删除方法.py 
--------实例化类--------
玩月海
--------动态给对象添加方法--------
学月海
--------动态给类添加方法--------
学言
yuehai
Traceback (most recent call last):
  File "D:\Idea\save\python\0_study\01_python\06_对象\_07_02_动态添加删除方法.py", line 44, in <module>
    yuehai2.play()
    ^^^^^^^^^^^^
AttributeError: 'YueHai' object has no attribute 'play'

进程已结束,退出代码1
```


## 8、装饰器

> https://www.cnblogs.com/tobyqin/p/python-decorator.html

1. 装饰器是给现有的模块增添新的小功能，可以对原函数进行功能扩展，而且还不需要修改原函数的内容，也不需要修改原函数的调用。
2. 装饰器的使用符合了面向对象编程的开放封闭原则
3. 使用装饰器之前，我们要知道，其实python里是万物皆对象，也就是万物都可传参。函数也可以作为函数的参数进行传递的

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/10 16:11
# @Author   : 月海
# @File     : _03_装饰器
# @Project  : 01_python

# 之前
def yue_hai():
    print('月海')
    yan()


def yan():
    print('言')


# yue_hai()


# 装饰器
# 装饰器函数，在原函数基础上扩展的函数
def yan2(fun):
    def wrapper(name):
        print('言')
        return fun(name)

    return wrapper


# 原函数，需要增加功能
@yan2
def yue_hai2(name):
    print(f'月海 + {name}')


yue_hai2('言')
```

# 十、Spark 大数据处理

1. PySpark 的数据计算，都是基于 RDD 对象来进行的，那么如何进行呢？
2. 自然是依赖，RDD 对象内置丰富的：成员方法（算子）
3. Transformation：转换算子（数据计算）：
	1. 值类型 valueType：
		1. map：将传入的函数作用到数据集的每一个元素上，生成一个新的 RDD 返回
		2. flatMap：先执行 map 的操作，再将所有对象合并为一个集合
		3. filter：选出所有传入的函数返回值为 true 的元素，生成一个新的 RDD 返回
		4. distinct：去重
	2. 双值类型 DoubleValueType：
		1. Union：对两个 RDD 求并集
		2. Intersection：对两个 RDD 求交集
	3. key-Value （二元元组）值类型：
		1. groupByKey：以元组中的第 0 个元素作为 key，进行分组，返回一个新的 RDD
		2. reduceByKey：将 key 相同的键值对，按照传入的函数进行计算
		3. sortByKey：根据 key 进行排序
4. Action：动作（行动）算子（数据输出）：
	1. collect：返回一个 list，list 中包含 RDD 中的所有元素；只有当数据量较小的时候使用Collect 因为所有的结果都会加载到内存中
	2. reduce：reduce 将 RDD 中元素两两传递给输入函数，同时产生一个新的值，新产生的值与 RDD 中下一个元素再被传递给输入函数直到最后只有一个值为止
	3. first：返回 RDD 的第一个元素
	4. take：返回 RDD 的前 N 个元素，`take`(*num*)
	5. Top：排序取前几个从大到小
	6. Count：返回 RDD 中元素的个数
	7. foreach：仅返回满足 foreach 内函数条件元素

## 1、Spark 和 PySpark 是什么

### ①、Spark

1. 定义：Apache Spark 是用于大规模数据（large-scala data）处理的统一（unified）分析引擎。
2. 简单来说，Spark 是一款分布式的计算框架，用于调度成百上千的服务器集群，计算 TB、PB 乃至 EB 级别的海量数据
3. Spark 作为全球顶级的分布式计算框架，支持众多的编程语言进行开发。而 Python 语言，则是 Spark 重点支持的方向。

### ②、PySpark

1. Spark 对 Python 语言的支持，重点体现在，Python 第三方库：PySpark 之上。
2. PySpark 是由 Spark 官方开发的 Python 语言第三方库。
3. Python 开发者可以使用 pip 程序快速的安装 PySpark 并像其它三方库那样直接使用。

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307152212.png)

4. Python 应用场景和就业方向是十分丰富的，其中，最为亮点的方向为：大数据开发和人工智能

## 2、PySpark 库简单使用

1. 安装 PySpark 库

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307153211.png)

2. 构建 PySpark 执行环境入口对象：想要使用 PySpark 库完成数据处理，首先需要构建一个执行环境入口对象。PySpark 的执行环境入口对象是：类 SparkContext 的类对象

```python
# @Time     : 2023/3/7 15:36
# @Author   : 月海
# @File     : _01_PySpark 库简单使用
# @Project  : 01_python

# 导包
from pyspark import SparkConf, SparkContext

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')

# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 打印 pyspark 版本
print(sc.version)

# 停止 pyspark
sc.stop()
```

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe "D:\Idea\save\python\0_study\01_python\08_PySpark\_01_PySpark 库简单使用.py" 
23/03/07 15:44:00 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/03/07 15:44:00 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
3.3.2

进程已结束,退出代码0
```

3. SparkContext 类对象，是 PySpark 编程中一切功能的入口。PySpark 的编程，主要分为如下三大步骤：

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307155028.png)

4. 通过 SparkContext 对象，完成数据输入
5. 输入数据后得到 RDD 对象，对 RDD 对象进行迭代计算
6. 最终通过 RDD 对象的成员方法，完成数据输出工作

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307155129.png)

## 3、数据输入

### ①、理解 RDD 对象

1. PySpark 支持多种数据的输入，在输入完成后，都会得到一个：RDD 类的对象
2. RDD 全称为：弹性分布式数据集（Resilient Distributed Datasets），PySpark 针对数据的处理，都是以 RDD 对象作为载体，即：
	1. 数据存储在 RDD 内
	2. 各类数据的计算方法，也都是 RDD 的成员方法
	3. RDD 的数据计算方法，返回值依旧是 RDD 对象
3. PySpark的编程模型（下图）可以归纳为：
	1. 准备数据到 RDD -> RDD 迭代计算 -> RDD 导出为 list、文本文件等
	2. 即：源数据 -> RDD -> 结果数据

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307160304.png)

### ②、掌握 PySpark 数据输入的 2 种方法

1. PySpark 支持通过 SparkContext 对象的 parallelize 成员方法，将：`list、tuple、set、dict、str` 转换为 PySpark 的 RDD 对象
2. 注意：字符串会被拆分出 1 个个的字符，存入 RDD 对象，字典仅有 key 会被存入 RDD 对象
3. PySpark 也支持通过 SparkContext 入口对象，来读取文件，来构建出 RDD 对象。

```python
# @Time     : 2023/3/7 16:08
# @Author   : 月海
# @File     : _03_01_理解 RDD 对象
# @Project  : 01_python

# 导包
from pyspark import SparkConf, SparkContext

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 定义集合
list = ['月海', 16, 0, ['yuehai', 'yan']]
# 将 python 对象转换为 PySpark 的 RDD 对象
rdd = sc.parallelize(list)
print(rdd.collect())

# 通过 SparkContext 入口对象，来读取文件，来构建出 RDD 对象。
myFileRdd = sc.textFile('../04_文件File/file/《一阙晴空》BY莫天天.txt')
print(myFileRdd.collect())

# 停止 pyspark
sc.stop()
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307163123.png)


## 4、数据计算
> 报错换 3.10 版本的 python 试试，反正我换了就好了

### ①、map 方法

```python
# @Time     : 2023/3/8 9:33
# @Author   : 月海
# @File     : _04_01_map 方法
# @Project  : 01_python

# 导包
from pyspark import SparkConf, SparkContext
import os

# 设置 python 解释器的位置，不然 Spark 找不到
os.environ['PYSPARK_PYTHON'] = 'D:/java/Python/python3.10.10/python.exe'

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 将 python 对象转换为 PySpark 的 RDD 对象
rdd = sc.parallelize([5, 6, 1, 3, 2, 8])

# map：将传入的函数作用到数据集的每一个元素上，生成一个新的 RDD 返回
# 通过 map 方法将全部数据都 * 10 再 全部 + 5；传入函数
print(rdd.map(lambda data: data * 10).map(lambda data: data + 5).collect())

# 停止 pyspark
sc.stop()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\08_PySpark\_04_01_map 方法.py" 
23/03/08 10:28:07 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/03/08 10:28:07 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[55, 65, 15, 35, 25, 85]

进程已结束,退出代码0
```

### ②、filter 方法

```python
# @Time     : 2023/3/8 10:49
# @Author   : 月海
# @File     : _04_02_filter 方法
# @Project  : 01_python


# 导包
from pyspark import SparkConf, SparkContext
import os

# 设置 python 解释器的位置，不然 Spark 找不到
os.environ['PYSPARK_PYTHON'] = 'D:/java/Python/python3.10.10/python.exe'

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 将 python 对象转换为 PySpark 的 RDD 对象
rdd = sc.parallelize([5, 6, 1, 3, 2, 8])

# 保留偶数
print(rdd.filter(lambda i: i % 2 == 0).collect())

# 停止 pyspark
sc.stop()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\08_PySpark\_04_02_filter 方法.py" 
23/03/08 11:28:29 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/03/08 11:28:30 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[6, 2, 8]

进程已结束,退出代码0
```

### ③、reduceByKey 方法

```python
# @Time     : 2023/3/8 10:56
# @Author   : 月海
# @File     : _04_03_reduceByKey 方法
# @Project  : 01_python

# 导包
from pyspark import SparkConf, SparkContext
import os

# 设置 python 解释器的位置，不然 Spark 找不到
os.environ['PYSPARK_PYTHON'] = 'D:/java/Python/python3.10.10/python.exe'

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 将 python 对象（集合中的二元元组）转换为 PySpark 的 RDD 对象
rdd = sc.parallelize([('男', 80), ('女', 70), ('男', 90), ('女', 95), ('男', 70)])

# reduceByKey：将 key 相同的键值对，按照传入的函数进行计算
# 分别求男、女成绩的和
print(rdd.reduceByKey(lambda a, b: a + b).collect())

# 停止 pyspark
sc.stop()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\08_PySpark\_04_03_reduceByKey 方法.py" 
23/03/08 11:06:23 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/03/08 11:06:23 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
D:\Idea\save\python\0_study\01_python\venv\Lib\site-packages\pyspark\python\lib\pyspark.zip\pyspark\shuffle.py:65: UserWarning: Please install psutil to have better support with spilling
[('男', 240), ('女', 165)]

进程已结束,退出代码0
```

## 5、数据输出

### ①、输出为 Python 对象


```python
# @Time     : 2023/3/8 12:37
# @Author   : 月海
# @File     : _05_01_输出为 Python 对象
# @Project  : 01_python

# 导包
from pyspark import SparkConf, SparkContext
import os

# 设置 python 解释器的位置，不然 Spark 找不到
os.environ['PYSPARK_PYTHON'] = 'D:/java/Python/python3.10.10/python.exe'

# 创建 SparkContext 类对象
# setAppName('test_spark_app')：设置当前任务名称
conf = SparkConf().setMaster('local[*]').setAppName('test_spark_app')
# 基于 SparkConf 类对象创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# 将 python 对象（集合中的二元元组）转换为 PySpark 的 RDD 对象
rdd = sc.parallelize([5, 6, 1, 3, 2, 8, 5])

"""
    1. collect：返回一个 list，list 中包含 RDD 中的所有元素；只有当数据量较小的时候使用Collect 因为所有的结果都会加载到内存中
    2. reduce：reduce 将 RDD 中元素两两传递给输入函数，同时产生一个新的值，新产生的值与 RDD 中下一个元素再被传递给输入函数直到最后只有一个值为止
    3. first：返回 RDD 的第一个元素
    4. take：返回 RDD 的前 N 个元素，`take`(*num*)
    5. Top：排序取前几个从大到小
    6. Count：返回 RDD 中元素的个数
    7. foreach：仅返回满足 foreach 内函数条件元素
"""
print(rdd.collect())
print(rdd.reduce(lambda a, b: a + b))
print(rdd.top(rdd.count()))

# 停止 pyspark
sc.stop()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\08_PySpark\_05_01_输出为 Python 对象.py" 
23/03/08 12:51:14 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/03/08 12:51:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[5, 6, 1, 3, 2, 8, 5]
30
23/03/08 12:51:31 WARN ProcfsMetricsGetter: Exception when trying to compute pagesize, as a result reporting of ProcessTree metrics is stopped
[8, 6, 5, 5, 3, 2, 1]

进程已结束,退出代码0
```

### ②、输出到文件中

1. 使用 `saveAsTestFile()` 算子可将数据写入到文本文件中，但是需要配置 Hadoop 依赖
2. 下载Hadoop安装包：http://archive.apache.org/dist/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz
3. 解压到电脑任意位置
4. 在 Python 代码中使用 os 模块配置 `os.environ['HADOOP_HOME'] = 'HADOOP解压文件夹路径'`
5. 下载 winutils.exe，并放入 Hadoop 解压文件夹的 bin 目录内：https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/winutils.exe
6. 下载 hadoop.dll，并放入 `:C:/Windows/System32` 文件夹内：https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/hadoop.dll

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308125646.png)

# 十一、网络爬虫

## 1、爬虫简介

### ①、什么是互联网爬虫？

1. 如果我们把互联网比作一张大的蜘蛛网，那一台计算机上的数据便是蜘蛛网上的一个猎物，而爬虫程序就是一只小蜘蛛，沿着蜘蛛网抓取自己想要的数据
2. 解释1：通过一个程序，根据 Url(http://www.taobao.com) 进行爬取网页，获取有用信息
3. 解释2：使用程序模拟浏览器，去向服务器发送请求，获取响应信息

### ②、爬虫核心？

1. 爬取网页：爬取整个网页 包含了网页中所有得内容
2. 解析数据：将网页中你得到的数据进行解析
3. 难点：爬虫和反爬虫之间的博弈

### ③、爬虫的用途？

1. 数据分析/人工数据集
2. 社交软件冷启动
3. 舆情监控
4. 竞争对手监控

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308131014.png)

### ④、爬虫分类？

1. 通用爬虫：
	1. 实例：百度、360、google、sougou 等搜索引擎‐‐‐伯乐在线
	2. 功能：访问网页‐>抓取数据‐>数据存储‐>数据处理‐>提供检索服务
	3. robots协议：一个约定俗成的协议，添加 robots.txt 文件，来说明本网站哪些内容不可以被抓取，起不到限制作用自己写的爬虫无需遵守
	4. 网站排名(SEO)：
		1. 根据 pagerank 算法值进行排名（参考个网站流量、点击率等指标）
		2. 百度竞价排名
	5. 缺点：
		1. 抓取的数据大多是无用的
		2. 不能根据用户的需求来精准获取数据
2. <font color="#ff0000">聚焦爬虫</font>：
	1. 功能：根据需求，实现爬虫程序，抓取需要的数据
	2. 设计思路：确定要爬取的url：如何获取Url
	3. 模拟浏览器通过 http 协议访问 url，获取服务器返回的 html 代码：如何访问
	4. 解析 html 字符串（根据一定规则提取需要的数据）：如何解析

### ⑤、反爬手段？

1. User‐Agent：User Agent 中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。
2. 代理 IP
	1. 西次代理
	2. 快代理
	3. 什么是高匿名、匿名和透明代理？它们有什么区别？
		1. 使用透明代理，对方服务器可以知道你使用了代理，并且也知道你的真实IP。
		2. 使用匿名代理，对方服务器可以知道你使用了代理，但不知道你的真实IP。
		3. 使用高匿名代理，对方服务器不知道你使用了代理，更不知道你的真实IP。
3. 验证码访问
	1. 打码平台
	2. 云打码平台
	3. 超级🦅
4. 动态加载网页 网站返回的是js数据 并不是网页的真实数据：selenium驱动真实的浏览器发送请求
5. 数据加密：分析 js 代码

## 2、Urllib

### ①、获取百度首页的源码

```python
# @Time     : 2023/3/8 13:45
# @Author   : 月海
# @File     : _01_Urllib
# @Project  : 01_python

# 使用 Urllib 获取百度首页的源码

# 导包
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'http://www.baidu.com/'

# 2、模拟浏览器向服务器发送请求；urlopen：访问 url 获取数据
response = urllib.request.urlopen(url)

# 3、获取响应中的页面的源码
# read()：字节形式读取二进制；扩展：rede(5)返回前几个字节
# decode('utf-8')：解码；字节 ‐‐> 字符串
# encode()：编码；字符串 ‐‐> 字节
content = response.read().decode('utf-8')

# 打印
print(content)
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308140157.png)

### ②、HTTPResponse 类型的 6 个方法

1. `read()`：字节形式读取二进制；扩展：`rede(5)` 返回前几个字节
2. `readline()`：读取一行
3. `readlines()`：一行一行读取 直至结束
4. `getcode()`：获取状态码
5. `geturl()`：获取 url
6. `getheaders()`：获取 headers

```python
# @Time     : 2023/3/8 14:02
# @Author   : 月海
# @File     : _02_HTTPResponse 类型的 6 个方法
# @Project  : 01_python

# 导包
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'http://www.baidu.com/'

# 2、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 1. `read()`：字节形式,一个字节一个字节的读取二进制；扩展：`rede(5)` 返回前几个字节
print(response.read())

# 2. `readline()`：读取一行
print(response.readline())

# 3. `readlines()`：一行一行读取 直至结束
for readline in response.readlines():
    print(readline)

# 4. `getcode()`：获取状态码
print(response.getcode())

# 5. `geturl()`：获取 url
print(response.geturl())

# 6. `getheaders()`：获取 headers 响应头
print(response.getheaders())
```

### ③、HTTPRequest 下载

> 注意并不能自动创建文件夹

```python
# @Time     : 2023/3/8 14:23
# @Author   : 月海
# @File     : _03_HTTPRequest 下载
# @Project  : 01_python

# 导包
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'http://www.baidu.com/'

# urlretrieve：将远程数据下载到本地
# 下载网页
urllib.request.urlretrieve(url, './save/百度首页.html')

# 下载图片
urllib.request.urlretrieve('https://tse2-mm.cn.bing.net/th/id/OIP-C.xVSeWqBAc8GCsGXyxe_KaAHaEI?w=301&h=180&c=7&r=0&o=5&pid=1.7', './save/月海.jpg')

# 下载视频
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308151937.png)

### ④、请求对象的定制

1. url 的组成

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308153503.png)

2. UA 介绍：User Agent 中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本。浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等

```python
# @Time     : 2023/3/8 15:43
# @Author   : 月海
# @File     : _04_请求对象的定制
# @Project  : 01_python

# 导包
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'https://www.baidu.com/'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 4、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 5、打印
print(response.read().decode('utf8'))
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230308155403.png)

### ⑤、编解码

#### Ⅰ、get 请求方式：urllib.parse.quote()

```python
# @Time     : 2023/3/8 16:17
# @Author   : 月海
# @File     : _05_编解码_01_urllib.parse.quote()
# @Project  : 01_python

# 导包
import urllib.parse
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'https://www.baidu.com/s?wd='

# 1.2、转码：https://www.baidu.com/s?wd=%E6%9C%88%E6%B5%B7
url = url + urllib.parse.quote('月海')
print(url)

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 4、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 5、打印
print(response.read().decode('utf8'))
```

#### Ⅱ、2.get 请求方式：urllib.parse.urlencode()

```python
# @Time     : 2023/3/8 16:17
# @Author   : 月海
# @File     : _05_编解码_02_urllib.parse.urlencode()
# @Project  : 01_python

# 导包
import urllib.parse
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'https://www.baidu.com/s?'

# 1.2 定义参数
data = {
    'name': '月海',
    'age': 16,
    'sex': 0
}

# 1.3、转码：https://www.baidu.com/s?name=%E6%9C%88%E6%B5%B7&age=16&sex=0
url = url + urllib.parse.urlencode(data)

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 4、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 5、打印
print(response.read().decode('utf8'))
```

#### Ⅲ、post 请求方式

```python
# @Time     : 2023/3/8 16:18
# @Author   : 月海
# @File     : _05_编解码_03_post
# @Project  : 01_python

# 导包
import urllib.parse
import urllib.request
import json

# 1、定义一个 url，就是要访问的地址
url = 'https://fanyi.baidu.com/v2transapi?'

# 2、定制请求头
headers = {
    'Cookie': 'BIDUPSID=B27BD7138FB7CAA682BF840DAB0B20EC; PSTM=1653874920; BAIDUID=B27BD7138FB7CAA62272FAA2DC08326F:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=xJV2xMclhVRXpwNn5xOHNBNlQyeXlEQ0V-cHBDNWxIRGJRSjJyR2JXelg1ZzVqRVFBQUFBJCQAAAAAAAAAAAEAAADNDSI02K3A5NPq2LzSuQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANdZ52LXWediQW; BDUSS_BFESS=xJV2xMclhVRXpwNn5xOHNBNlQyeXlEQ0V-cHBDNWxIRGJRSjJyR2JXelg1ZzVqRVFBQUFBJCQAAAAAAAAAAAEAAADNDSI02K3A5NPq2LzSuQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANdZ52LXWediQW; MCITY=-236:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=B27BD7138FB7CAA62272FAA2DC08326F:FG=1; BA_HECTOR=8h800k2185agag8g2l8l2kd21i0ghr81n; ZFY=:BLVchZLDUNSo:AvGXc2wCLQbApmv:B6Ghigr7hZjY:AUyo:C; __bid_n=186a641461b89e4eeb4207; FPTOKEN=rzAjUmY8MF56PzeV247Ci3OlqdHstcdwz+wmMZ6yt+KbATlNsNnaRTpoSD6TosA1hY87Vymhxzolf7ci/J2eMJldwxzL1MQ4UWe6efcRcILah8Iq5yGdyqFuUqsCBqIBST4kvFFwgFdhwty3kvVb3MKRSJMBGVAZXN0VqquT81e9x+F1psnbQ/68Bjw42iqwAdHIxrBehBPJhSgVcgF2yi9rWpeFscdyAytWL4OqY7e6FTFiLBDdgiqlAYV9pAtp23oCXT3Plt97Ryb0PCwfEha5dnX2nlK3nTHQy0INN+OWcgqbslxsO8ir0NkXmIqPVs0mlTHcuzamZeDf2H+HrkVgtHmaZnhqi6CWHtdYt6go90tQi+6oTVHHJsedddHDSukJMzXtfD51GzX0d9Yl6g==|krkDgR+Pd4bnTgOUZTS8RSLBFyP905Rf2t73MFWlyHk=|10|c230b72e0d8b2f0e1578bb69d87a9fbb; RT="z=1&dm=baidu.com&si=fa43121f-86a5-4ada-8848-f4aa025e9462&ss=lezf5ovz&sl=2&tt=22q&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=jxs&ul=uc9&hd=ufw"; BCLID=10868960166335744046; BCLID_BFESS=10868960166335744046; BDSFRCVID=3nkOJeC62mr-OuOfWeCMrIckrhfGywnTH6_n0NtKNbqucCSYx9tLEG0Pnf8g0KuMss8qogKKymOTHrAF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=3nkOJeC62mr-OuOfWeCMrIckrhfGywnTH6_n0NtKNbqucCSYx9tLEG0Pnf8g0KuMss8qogKKymOTHrAF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbAO_C--JIP3DPJNhCTaMtCs2hoXetJyaR0eWJvvWJ5TMCozKCcc5f4E3UomWRjAKK3HBnQTM43_ShPCBPI2XR0UXx5D-4JmLa5OV4b13l02VbrIe-t2ynLIKp-Ob4RMW238Wl7mWPoNsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjj6jK4JKjH0tqToP; H_BDCLCKID_SF_BFESS=tbAO_C--JIP3DPJNhCTaMtCs2hoXetJyaR0eWJvvWJ5TMCozKCcc5f4E3UomWRjAKK3HBnQTM43_ShPCBPI2XR0UXx5D-4JmLa5OV4b13l02VbrIe-t2ynLIKp-Ob4RMW238Wl7mWPoNsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjj6jK4JKjH0tqToP; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1678067229,1678155746,1678233820,1678320434; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1678320434; ab_sr=1.0.1_NzdhZDk3MGU3MTJiOGI2OGM1NmIxYzJmY2U3YTUxYTI2ZGY4NWI4YzNlNTYwZGM1NjQyNTc4MmY4ODQyZDhiMDc0YzA5MDEzNjAyMjkwNTA0ZDAzZWQyZGY1MTVmZTFjZmNjZmM1ZjE3OTA0YjNhZjBhYzc1NzM3OGU2NWY2NDdmZjZmYzg4ODY1NTcxNTdlZjJlYjdjZDMwZjAxZDQ5ZDU4ZTdiNmExYjdhNDYwYWFmMzM0N2ZiMmUwZmZhNzcw'
}

# 3、输入翻译内容
keyword = input('请输入：')

# 4、定义参数
data = {
    'from': 'zh',
    'to': 'en',
    'query': keyword,
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '955925.685348',
    'token': '77736d50141670864149c056d1acf226',
    'domain': 'common'
}

# 5、转码：from=zh&to=en&query=%E6%9C%88%E6%B5%B7&transtype=translang&simple_means_flag=3&sign=955925.685348&token=77736d50141670864149c056d1acf226&domain=common
data = urllib.parse.urlencode(data).encode('utf-8')

# 6、定制请求对象
request = urllib.request.Request(url=url, headers=headers, data=data)

# 7、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 8、获取请求返回的结果
content = response.read().decode('utf8')

# 9、将返回的 json 字符串转为 json 对象（字典）
# {'trans_result': {'data': [{'dst': 'lunar mare', 'src': '月海'}], 'from': 'zh', 'to': 'en', 'status': 0, 'type': 2}, 'dict_result': {'from': 'CEDict', 'synthesize_means': {'symbols': [{'cys': [{'means': [{'mean_id': '76722', 'cy_id': '67109', 'part_id': None, 'word_mean': 'lunar mare'}]}], 'symbol_id': '69733', 'xg': '', 'parts': [], 'word_symbol': 'yuè hǎi', 'word_id': '69116'}], 'word_name': '月海', 'word_id': '69116'}, 'simple_means': {'symbols': [{'word_symbol': 'yuè hǎi', 'parts': [{'part_name': '', 'means': [{'text': 'lunar mare', 'word_mean': 'lunar mare'}]}]}], 'word_name': '月海', 'from': 'CEDict', 'word_means': ['lunar mare']}, 'common': {'text': 'lunar mare'}}, 'liju_result': {'double': '[[[["\\u672c\\u6587","w_0","w_0",0],["\\u5229\\u7528","w_1","w_1,w_27,w_28",0],["\\u4eea\\u5668","w_2","w_2,w_30",0],["\\u548c","w_3","w_3,w_31",0],["\\u653e\\u5c04","w_4","w_4,w_5,w_32",0],["\\u5316\\u5b66","w_5","w_4,w_5,w_32",0],["\\u7ec4","w_6","w_6",0],["\\u5206\\u79bb","w_7","w_7",0],["\\u7684","w_8","w_8,w_29",0],["\\u65b9\\u6cd5","w_9","w_9,w_33",0],["\\uff0c","w_10","w_10,w_34",0],["\\u5728","w_11","w_11,w_39",0],["62.10mg","w_12","w_12",0," "],["Apollo-17","w_13","w_13,w_41",0],["\\u6708\\u6d77","w_14","w_14,w_42,w_43",1],["\\u7384\\u6b66\\u5ca9","w_15","w_15,w_44",0],["\\u6837\\u54c1","w_16","w_16,w_45",0],["\\u4e2d","w_17","w_17",0],["\\uff0c","w_18","w_18,w_46",0],["\\u6d4b\\u5b9a","w_19","w_19,w_38",0],["\\u4e86","w_20","w_20",0],["36","w_21","w_21,w_35",0],["\\u79cd","w_22","w_22",0],["\\u5143\\u7d20","w_23","w_23,w_36",0],["\\u7684","w_24","w_24,w_49",0],["\\u542b\\u91cf","w_25","w_25,w_48",0],["\\u3002","w_26","w_26,w_56",0]],[["By","w_27","w_1,w_27,w_28",0," "],["means","w_28","w_1,w_27,w_28",0," "],["of","w_29","w_8,w_29",0," "],["instrumental","w_30","w_2,w_30",0," "],["and","w_31","w_3,w_31",0," "],["radiochemical","w_32","w_4,w_5,w_32",0," "],["methods","w_33","w_9,w_33",0],[",","w_34","w_10,w_34",0," "],["36","w_35","w_21,w_35",0," "],["elements","w_36","w_23,w_36",0," "],["are","w_37","",0," "],["determined","w_38","w_19,w_38",0," "],["in","w_39","w_11,w_39",0," "],["an","w_40","",0," "],["Apollo-17","w_41","w_13,w_41",0," "],["lunar","w_42","w_14,w_42,w_43",0," "],["mare","w_43","w_14,w_42,w_43",0," "],["basalt","w_44","w_15,w_44",0," "],["sample","w_45","w_16,w_45",0],[".","w_46","w_18,w_46",0," "],["Total","w_47","",0," "],["amount","w_48","w_25,w_48",0," "],["of","w_49","w_24,w_49",0," "],["the","w_50","",0," "],["sample","w_51","",0," "],["is","w_52","",0," "],["only","w_53","",0," "],["62.10","w_54","",0," "],["mg","w_55","",0],[".","w_56","w_26,w_56",0]],"http:\\/\\/dict.cnki.net\\/h_588546000.html","0"],[[["\\u7ed3\\u679c","w_57","w_57,w_83,w_84",0],["\\uff0c","w_58","w_58,w_85",0],["\\u6708\\u7403","w_59","w_59,w_90",0],["\\u8fd1","w_60","w_60,w_92",0],["\\u5730\\u9762","w_61","w_61",0],["\\u719f\\u6089","w_62","w_62,w_86",0],["\\u7684","w_63","w_63",0],["\\u56fe\\u6848","w_64","w_64,w_87",0],["\\u5f88","w_65","w_65,w_93",0],["\\u5bb9\\u6613","w_66","w_66,w_94",0],["\\u5c31\\u80fd","w_67","w_67,w_95",0],["\\u770b","w_68","w_68,w_96",0],["\\u51fa\\u6765","w_69","w_69,w_97",0],["\\uff0c","w_70","w_70,w_98",0],["\\u5305\\u62ec","w_71","w_71,w_99",0],["\\u5e73\\u6ed1","w_72","w_72,w_101",0],["\\u7684","w_73","w_73",0],["\\u6708\\u6d77","w_74","w_74,w_102,w_103",1],["\\u548c","w_75","w_75,w_104",0],["\\u5de8\\u5927","w_76","w_76,w_77,w_106",0],["\\u7684","w_77","w_76,w_77,w_106",0],["\\u7b2c\\u8c37","w_78","w_78,w_109",0],["\\u73af\\u5f62","w_79","w_79,w_80,w_108",0],["\\u5c71","w_80","w_79,w_80,w_108",0],["\\u3002","w_81","w_81,w_110",0]],[["As","w_82","",0," "],["a","w_83","w_57,w_83,w_84",0," "],["result","w_84","w_57,w_83,w_84",0],[",","w_85","w_58,w_85",0," "],["familiar","w_86","w_62,w_86",0," "],["details","w_87","w_64,w_87",0," "],["of","w_88","",0," "],["the","w_89","",0," "],["Moon","w_90","w_59,w_90",0],["\'s","w_91","",0," "],["nearside","w_92","w_60,w_92",0," "],["are","w_93","w_65,w_93",0," "],["easy","w_94","w_66,w_94",0," "],["to","w_95","w_67,w_95",0," "],["pick","w_96","w_68,w_96",0," "],["out","w_97","w_69,w_97",0],[",","w_98","w_70,w_98",0," "],["including","w_99","w_71,w_99",0," "],["the","w_100","",0," "],["smooth","w_101","w_72,w_101",0," "],["lunar","w_102","w_74,w_102,w_103",0," "],["mare","w_103","w_74,w_102,w_103",0," "],["and","w_104","w_75,w_104",0," "],["the","w_105","",0," "],["large","w_106","w_76,w_77,w_106",0," "],["ray","w_107","",0," "],["crater","w_108","w_79,w_80,w_108",0," "],["Tycho","w_109","w_78,w_109",0],[".","w_110","w_81,w_110",0]],"http:\\/\\/www.chazidian.com\\/dict\\/crater\\/","1"],[[["\\u5e94\\u7528","w_111","w_111",0],["\\u6a21\\u5f0f","w_112","w_112,w_138",0],["\\u8f93\\u51fa","w_113","w_113,w_139",0],["\\u7edf\\u8ba1","w_114","w_114,w_140",0],["\\u7684","w_115","w_115",0],["\\u9010\\u6b65","w_116","w_116,w_148",0],["\\u5224\\u522b","w_117","w_117",0],["\\u65b9\\u6cd5","w_118","w_118,w_144",0],["\\uff0c","w_119","w_119,w_145",0],["\\u5bf9","w_120","w_120,w_163",0],["\\u5c71\\u4e1c","w_121","w_121,w_169",0],["\\u5357","w_122","w_122,w_123,w_165",0],["\\u90e8","w_123","w_122,w_123,w_165",0],["\\u6cbf\\u6d77","w_124","w_124,w_166",0],["4","w_125","w_125,w_171",0],["\\uff5e","w_126","w_126,w_172",0],["7","w_127","w_127,w_128,w_173",0],["\\u6708\\u6d77","w_128","w_127,w_128,w_173",1],["\\u96fe","w_129","w_129,w_159",0],["\\u51fa\\u73b0","w_130","w_130,w_160",0],["\\u4f5c","w_131","w_131,w_155",0],["24h","w_132","w_132,w_162",0],["\\u7684","w_133","w_133,w_161",0],["\\u5224\\u522b","w_134","w_134",0],["\\u9884\\u62a5","w_135","w_135,w_157",0],["\\u3002","w_136","w_136,w_174",0]],[["A","w_137","",0," "],["model","w_138","w_112,w_138",0," "],["output","w_139","w_113,w_139",0," "],["statistics","w_140","w_114,w_140",0," "],["(","w_141","",0," "],["MOS","w_142","",0],[")","w_143","",0," "],["scheme","w_144","w_118,w_144",0],[",","w_145","w_119,w_145",0," "],["using","w_146","",0," "],["a","w_147","",0," "],["stepwise","w_148","w_116,w_148",0," "],["selection","w_149","",0," "],["discriminant","w_150","",0," "],["analysis","w_151","",0," "],["approach","w_152","",0],[",","w_153","",0," "],["is","w_154","",0," "],["used","w_155","w_131,w_155",0," "],["to","w_156","",0," "],["estimate","w_157","w_135,w_157",0," "],["marine","w_158","",0," "],["fog","w_159","w_129,w_159",0," "],["occurrence","w_160","w_130,w_160",0," "],["in","w_161","w_133,w_161",0," "],["24h","w_162","w_132,w_162",0," "],["for","w_163","w_120,w_163",0," "],["the","w_164","",0," "],["south","w_165","w_122,w_123,w_165",0," "],["coastal","w_166","w_124,w_166",0," "],["region","w_167","",0," "],["of","w_168","",0," "],["Shangdong","w_169","w_121,w_169",0," "],["during","w_170","",0," "],["April","w_171","w_125,w_171",0," "],["to","w_172","w_126,w_172",0," "],["July","w_173","w_127,w_128,w_173",0],[".","w_174","w_136,w_174",0]],"http:\\/\\/dict.cnki.net\\/h_53608153000.html","2"],[[["\\u5982\\u4f55","w_175","w_175,w_182",0],["\\u89e3\\u51b3","w_176","w_176,w_185",0],["\\u6708\\u6d77","w_177","w_177,w_189",1],["\\u8fd9\\u6837","w_178","w_178,w_179,w_188",0],["\\u7684","w_179","w_178,w_179,w_188",0],["\\u95ee\\u9898","w_180","w_180,w_187",0],["\\uff1f","w_181","w_181,w_190",0]],[["How","w_182","w_175,w_182",0," "],["do","w_183","",0," "],["you","w_184","",0," "],["solve","w_185","w_176,w_185",0," "],["a","w_186","",0," "],["problem","w_187","w_180,w_187",0," "],["like","w_188","w_178,w_179,w_188",0," "],["maria","w_189","w_177,w_189",0],["?","w_190","w_181,w_190",0]],"www.keke.com","3"],[[["\\u6708\\u6d77","w_191","w_191,w_210",1],["\\u662f","w_192","w_192,w_211",0],["\\u5706\\u5f62","w_193","w_193,w_212",0],["\\u6d3c\\u5730","w_194","w_194,w_213",0],["\\uff0c","w_195","w_195",0],["\\u8986\\u76d6","w_196","w_196,w_214",0],["\\u7740","w_197","w_197,w_215",0],["\\u6697\\u8272","w_198","w_198,w_216",0],["\\u7684","w_199","w_199",0],["\\u677e\\u6563","w_200","w_200,w_219",0],["\\u7269\\u8d28","w_201","w_201,w_202,w_220",0],["\\uff0c","w_202","w_201,w_202,w_220",0],["\\u800c","w_203","w_203",0],["\\u4e0d\\u662f","w_204","w_204",0],["\\u575a\\u786c","w_205","w_205,w_221",0],["\\u7684","w_206","w_206",0],["\\u5ca9\\u77f3","w_207","w_207,w_222",0],["\\u3002","w_208","w_208,w_223",0]],[["The","w_209","",0," "],["maria","w_210","w_191,w_210",0," "],["are","w_211","w_192,w_211",0," "],["circular","w_212","w_193,w_212",0," "],["depressions","w_213","w_194,w_213",0," "],["covered","w_214","w_196,w_214",0," "],["with","w_215","w_197,w_215",0," "],["dark","w_216","w_198,w_216",0],[",","w_217","",0," "],["loosely","w_218","",0," "],["packed","w_219","w_200,w_219",0," "],["material-not","w_220","w_201,w_202,w_220",0," "],["solid","w_221","w_205,w_221",0," "],["rock","w_222","w_207,w_222",0],[".","w_223","w_208,w_223",0]],"http:\\/\\/www.dictall.com\\/st\\/56\\/83\\/568398572E6.htm","4"],[[["\\u4f5c\\u4e3a","w_224","w_224,w_254",0],["\\u6708\\u8868","w_225","w_225,w_256",0],["\\u7684","w_226","w_226",0],["\\u4e3b\\u8981","w_227","w_227",0],["\\u7ebf\\u6027","w_228","w_228,w_229,w_258",0],["\\u6784\\u9020","w_229","w_228,w_229,w_258",0],["\\uff0c","w_230","w_230",0],["\\u6708\\u6d77","w_231","w_231,w_245,w_246",1],["\\u6d77\\u5cad","w_232","w_232,w_247,w_248",0],["\\u548c","w_233","w_233",0],["\\u5c71\\u8109","w_234","w_234",0],["\\u662f\\u5426","w_235","w_235,w_243",0],["\\u4e3a","w_236","w_236",0],["\\u6f6e\\u6c50","w_237","w_237,w_238,w_252,w_253",0],["\\u529b","w_238","w_237,w_238,w_252,w_253",0],["\\u4f5c\\u7528","w_239","w_239",0],["\\u7684","w_240","w_240,w_251",0],["\\u7ed3\\u679c","w_241","w_241,w_250",0],["\\uff1f","w_242","w_242,w_259",0]],[["Is","w_243","w_235,w_243",0," "],["the","w_244","",0," "],["May","w_245","w_231,w_245,w_246",0," "],["Sea","w_246","w_231,w_245,w_246",0," "],["Ridge","w_247","w_232,w_247,w_248",0," "],["Mountains","w_248","w_232,w_247,w_248",0," "],["the","w_249","",0," "],["result","w_250","w_241,w_250",0," "],["of","w_251","w_240,w_251",0," "],["tidal","w_252","w_237,w_238,w_252,w_253",0," "],["forces","w_253","w_237,w_238,w_252,w_253",0," "],["as","w_254","w_224,w_254",0," "],["the","w_255","",0," "],["lunar","w_256","w_225,w_256",0," "],["surface","w_257","",0," "],["lineament","w_258","w_228,w_229,w_258",0],["?","w_259","w_242,w_259",0]],"http:\\/\\/www.fabiao.net\\/content-68-559733-1.html","5"],[[["\\u6708","w_260","w_260,w_276",0],["\\u5cad","w_261","w_261,w_277",0],["\\u662f","w_262","w_262,w_278",0],["\\u6708\\u7403","w_263","w_263",0],["\\u8868\\u9762","w_264","w_264,w_293",0],["\\u6708\\u6d77","w_265","w_265,w_290",1],["\\u4e2d","w_266","w_266,w_288",0],["\\u5206\\u5e03","w_267","w_267,w_285",0],["\\u6700","w_268","w_268,w_286",0],["\\u5e7f","w_269","w_269,w_287",0],["\\u7684","w_270","w_270",0],["\\u4e00","w_271","w_271,w_279",0],["\\u79cd","w_272","w_272,w_280",0],["\\u7ebf\\u6027","w_273","w_273,w_282",0],["\\u6784\\u9020","w_274","w_274,w_283",0],["\\u3002","w_275","w_275,w_294",0]],[["Mare","w_276","w_260,w_276",0," "],["ridge","w_277","w_261,w_277",0," "],["is","w_278","w_262,w_278",0," "],["a","w_279","w_271,w_279",0," "],["kind","w_280","w_272,w_280",0," "],["of","w_281","",0," "],["linear","w_282","w_273,w_282",0," "],["structure","w_283","w_274,w_283",0," "],["which","w_284","",0," "],["distributed","w_285","w_267,w_285",0," "],["most","w_286","w_268,w_286",0," "],["widely","w_287","w_269,w_287",0," "],["in","w_288","w_266,w_288",0," "],["the","w_289","",0," "],["mare","w_290","w_265,w_290",0," "],["onthe","w_291","",0," "],["moon","w_292","",0," "],["surface","w_293","w_264,w_293",0],[".","w_294","w_275,w_294",0]],"http:\\/\\/www.fabiao.net\\/content-69-797480-1.html","6"],[[["\\u8fd9","w_295","w_295,w_314",0],["\\u9762\\u7684","w_296","w_296",0],["\\u6708\\u7403","w_297","w_297",0],["\\u4e0a","w_298","w_298,w_321",0],["\\u6df1\\u8272","w_299","w_299,w_324",0],["\\u7684","w_300","w_300",0],["\\u5730\\u533a","w_301","w_301,w_325",0],["\\uff0c","w_302","w_302,w_316",0],["\\u79f0","w_303","w_303,w_304,w_326",0],["\\u4e3a","w_304","w_303,w_304,w_326",0],["\\u6708\\u6d77","w_305","w_305,w_327",1],["\\uff0c","w_306","w_306,w_322",0],["\\u5b9e\\u9645\\u4e0a","w_307","w_307,w_329,w_330",0],["\\u662f","w_308","w_308,w_331",0],["\\u8f83\\u4e3a","w_309","w_309",0],["\\u5e73\\u5766","w_310","w_310,w_332",0],["\\u7684","w_311","w_311",0],["\\u533a\\u57df","w_312","w_312,w_333",0],["\\u3002","w_313","w_313,w_334",0]],[["This","w_314","w_295,w_314",0," "],["face","w_315","",0],[",","w_316","w_302,w_316",0," "],["known","w_317","",0," "],["as","w_318","",0," "],["the","w_319","",0," "],["near","w_320","",0," "],["side","w_321","w_298,w_321",0],[",","w_322","w_306,w_322",0," "],["has","w_323","",0," "],["darker","w_324","w_299,w_324",0," "],["regions","w_325","w_301,w_325",0," "],["called","w_326","w_303,w_304,w_326",0," "],["mares","w_327","w_305,w_327",0," "],["which","w_328","",0," "],["in","w_329","w_307,w_329,w_330",0," "],["fact","w_330","w_307,w_329,w_330",0," "],["are","w_331","w_308,w_331",0," "],["flatter","w_332","w_310,w_332",0," "],["regions","w_333","w_312,w_333",0],[".","w_334","w_313,w_334",0]],"provided by jukuu","7"],[[["\\u84dd\\u5929","w_335","w_335,w_354,w_355",0],["\\u6708\\u7403","w_336","w_336,w_356",0],["\\uff1a","w_337","w_337,w_357",0],["\\u9ed1\\u8272","w_338","w_338,w_359",0],["\\u7684","w_339","w_339",0],["\\u533a\\u57df","w_340","w_340,w_360",0],["\\u53eb\\u505a","w_341","w_341,w_362,w_363",0],["\\u6708\\u6d77","w_342","w_342,w_364,w_365",1],["\\uff0c","w_343","w_343",0],["\\u56e0\\u4e3a","w_344","w_344,w_366",0],["\\u4eba\\u4eec","w_345","w_345,w_367",0],["\\u66fe\\u7ecf","w_346","w_346,w_369",0],["\\u4ee5\\u4e3a","w_347","w_347,w_370",0],["\\u90a3","w_348","w_348",0],["\\u91cc\\u9762","w_349","w_349,w_373,w_374",0],["\\u5168","w_350","w_350",0],["\\u662f","w_351","w_351,w_372",0],["\\u6c34","w_352","w_352,w_375",0],["\\u3002","w_353","w_353,w_376",0]],[["Blue","w_354","w_335,w_354,w_355",0," "],["Sky","w_355","w_335,w_354,w_355",0," "],["Moon","w_356","w_336,w_356",0],[":","w_357","w_337,w_357",0," "],["The","w_358","",0," "],["dark","w_359","w_338,w_359",0," "],["areas","w_360","w_340,w_360",0," "],["are","w_361","",0," "],["known","w_362","w_341,w_362,w_363",0," "],["as","w_363","w_341,w_362,w_363",0," "],["lunar","w_364","w_342,w_364,w_365",0," "],["seas","w_365","w_342,w_364,w_365",0," "],["because","w_366","w_344,w_366",0," "],["they","w_367","w_345,w_367",0," "],["were","w_368","",0," "],["once","w_369","w_346,w_369",0," "],["believed","w_370","w_347,w_370",0," "],["to","w_371","",0," "],["be","w_372","w_351,w_372",0," "],["filled","w_373","w_349,w_373,w_374",0," "],["with","w_374","w_349,w_373,w_374",0," "],["water","w_375","w_352,w_375",0],[".","w_376","w_353,w_376",0]],"http:\\/\\/gb.cri.cn\\/29564\\/2009\\/09\\/16\\/4266s2622896_7.htm","8"],[[["\\u6708\\u6d77","w_377","w_377,w_406",1],["\\u51b2","w_378","w_378",0],["\\u76f8\\u4f4d","w_379","w_379,w_407",0],["\\u4f1a","w_380","w_380,w_409",0],["\\u6709","w_381","w_381,w_411",0],["\\u5982\\u4e0b","w_382","w_382",0],["\\u7684","w_383","w_383",0],["\\u60c5\\u5f62","w_384","w_384",0],["\\uff0c","w_385","w_385,w_426",0],["\\u4e5f\\u8bb8","w_386","w_386,w_427",0],["\\uff0c","w_387","w_387",0],["\\u4e00","w_388","w_388,w_414",0],["\\u65b9","w_389","w_389,w_416",0],["\\u6700\\u521d","w_390","w_390",0],["\\u7684","w_391","w_391",0],["\\u611f\\u89c9","w_392","w_392,w_412",0],["\\u53ef\\u80fd","w_393","w_393",0],["\\u4f1a","w_394","w_394",0],["\\u8ba4\\u4e3a","w_395","w_395",0],["\\u53e6","w_396","w_396",0],["\\u4e00\\u534a","w_397","w_397",0],["\\u662f","w_398","w_398,w_417",0],["\\u4e16\\u754c","w_399","w_399",0],["\\u4e0a","w_400","w_400",0],["\\u6700","w_401","w_401,w_419",0],["\\u652f\\u6301","w_402","w_402,w_420",0],["\\u81ea\\u5df1","w_403","w_403",0],["\\u7684","w_404","w_404",0],["\\u3002","w_405","w_405,w_429",0]],[["Moon","w_406","w_377,w_406",0," "],["opposite","w_407","w_379,w_407",0," "],["Neptune","w_408","",0," "],["can","w_409","w_380,w_409",0," "],["generate","w_410","",0," "],["include","w_411","w_381,w_411",0," "],["feeling","w_412","w_392,w_412",0," "],["like","w_413","",0," "],["one","w_414","w_388,w_414",0],["\'s","w_415","",0," "],["partner","w_416","w_389,w_416",0," "],["is","w_417","w_398,w_417",0," "],["the","w_418","",0," "],["most","w_419","w_401,w_419",0," "],["supportive","w_420","w_402,w_420",0," "],["person","w_421","",0," "],["one","w_422","",0," "],["has","w_423","",0," "],["ever","w_424","",0," "],["met","w_425","",0],[",","w_426","w_385,w_426",0," "],["for","w_427","w_386,w_427",0," "],["example","w_428","",0],[".","w_429","w_405,w_429",0]],"http:\\/\\/blog.sina.com.cn\\/s\\/blog_49f0c8b00100dex1.html","9"],[[["\\u76f4\\u5f84","w_430","w_430,w_463",0],["\\u8fbe","w_431","w_431,w_461",0],["900","w_432","w_432,w_433,w_462",0],["\\u516c\\u91cc","w_433","w_432,w_433,w_462",0],["\\uff0c","w_434","w_434,w_464",0],["\\u5468\\u56f4","w_435","w_435",0],["\\u73af\\u7ed5","w_436","w_436,w_465",0],["\\u7740","w_437","w_437,w_466",0],["\\u6210","w_438","w_438",0],["\\u540c\\u5fc3","w_439","w_439,w_467",0],["\\u5706","w_440","w_440",0],["\\u7684","w_441","w_441,w_469",0],["\\u6708\\u8868","w_442","w_442,w_470",0],["\\u5c71\\u8109","w_443","w_443,w_471",0],["\\uff0c","w_444","w_444,w_472",0],["\\u8be5","w_445","w_445,w_473",0],["\\u6708\\u6d77","w_446","w_446",1],["\\u88ab","w_447","w_447,w_474",0],["\\u8ba4\\u4e3a","w_448","w_448,w_475",0],["\\u662f","w_449","w_449,w_477",0],["\\u6708\\u4eae","w_450","w_450,w_487",0],["\\u5386\\u53f2","w_451","w_451,w_488",0],["\\u4e0a","w_452","w_452,w_486",0],["\\u6700\\u8fd1","w_453","w_453,w_483",0],["\\u4e00","w_454","w_454,w_481",0],["\\u6b21","w_455","w_455",0],["\\u5927\\u89c4\\u6a21","w_456","w_456,w_484",0],["\\u649e\\u51fb","w_457","w_457,w_485",0],["\\u7684","w_458","w_458,w_480",0],["\\u4ea7\\u7269","w_459","w_459,w_479",0],["\\u3002","w_460","w_460,w_489",0]],[["At","w_461","w_431,w_461",0," "],["900km","w_462","w_432,w_433,w_462",0," "],["across","w_463","w_430,w_463",0],[",","w_464","w_434,w_464",0," "],["ringed","w_465","w_436,w_465",0," "],["with","w_466","w_437,w_466",0," "],["concentric","w_467","w_439,w_467",0," "],["ranges","w_468","",0," "],["of","w_469","w_441,w_469",0," "],["moon","w_470","w_442,w_470",0," "],["mountains","w_471","w_443,w_471",0],[",","w_472","w_444,w_472",0," "],["it","w_473","w_445,w_473",0," "],["is","w_474","w_447,w_474",0," "],["believed","w_475","w_448,w_475",0," "],["to","w_476","",0," "],["be","w_477","w_449,w_477",0," "],["the","w_478","",0," "],["result","w_479","w_459,w_479",0," "],["of","w_480","w_458,w_480",0," "],["the","w_481","w_454,w_481",0," "],["most","w_482","",0," "],["recent","w_483","w_453,w_483",0," "],["giant","w_484","w_456,w_484",0," "],["impact","w_485","w_457,w_485",0," "],["in","w_486","w_452,w_486",0," "],["lunar","w_487","w_450,w_487",0," "],["history","w_488","w_451,w_488",0],[".","w_489","w_460,w_489",0]],"http:\\/\\/www.ecocn.org\\/thread-83351-1-11.html","10"],[[["\\u6708\\u6d77","w_490","w_490,w_527",1],["\\u76c6\\u5730","w_491","w_491,w_528",0],["\\u56e0","w_492","w_492",0],["\\u5176","w_493","w_493",0],["\\u4e0e","w_494","w_494,w_534",0],["\\u6708\\u8868","w_495","w_495,w_536",0],["\\u5927\\u90e8\\u5206","w_496","w_496,w_535",0],["\\u7ebf\\u72b6","w_497","w_497,w_537",0],["\\u6784\\u9020","w_498","w_498,w_538",0],["\\u6709","w_499","w_499,w_500,w_529",0],["\\u7740","w_500","w_499,w_500,w_529",0],["\\u660e\\u663e","w_501","w_501,w_531",0],["\\u7684","w_502","w_502",0],["\\u5171\\u751f","w_503","w_503,w_532",0],["\\u5173\\u7cfb","w_504","w_504,w_533",0],["\\uff0c","w_505","w_505,w_539",0],["\\u5206\\u6790","w_506","w_506,w_541",0],["\\u5176","w_507","w_507,w_548",0],["\\u7384\\u6b66\\u5ca9","w_508","w_508",0],["\\u55b7\\u53d1","w_509","w_509,w_543",0],["\\u5386\\u53f2","w_510","w_510,w_544",0],["\\u548c","w_511","w_511,w_545",0],["\\u6784\\u9020","w_512","w_512,w_546",0],["\\u4f5c\\u7528","w_513","w_513",0],["\\uff0c","w_514","w_514",0],["\\u5bf9\\u4e8e","w_515","w_515,w_554",0],["\\u4e86\\u89e3","w_516","w_516,w_555",0],["\\u6708\\u7403","w_517","w_517,w_557",0],["\\u6f14\\u5316","w_518","w_518,w_558",0],["\\u6709","w_519","w_519,w_520,w_549",0],["\\u7740","w_520","w_519,w_520,w_549",0],["\\u91cd\\u8981","w_521","w_521,w_551",0],["\\u7684","w_522","w_522",0],["\\u610f\\u4e49","w_523","w_523,w_553",0],["\\u3002","w_524","w_524,w_559",0]],[["Also","w_525","",0],[",","w_526","",0," "],["mare","w_527","w_490,w_527",0," "],["basins","w_528","w_491,w_528",0," "],["have","w_529","w_499,w_500,w_529",0," "],["a","w_530","",0," "],["obvious","w_531","w_501,w_531",0," "],["symbiotic","w_532","w_503,w_532",0," "],["relationship","w_533","w_504,w_533",0," "],["with","w_534","w_494,w_534",0," "],["most","w_535","w_496,w_535",0," "],["lunar","w_536","w_495,w_536",0," "],["linear","w_537","w_497,w_537",0," "],["structure","w_538","w_498,w_538",0],[",","w_539","w_505,w_539",0," "],["the","w_540","",0," "],["analysis","w_541","w_506,w_541",0," "],["of","w_542","",0," "],["eruption","w_543","w_509,w_543",0," "],["history","w_544","w_510,w_544",0," "],["and","w_545","w_511,w_545",0," "],["tectonism","w_546","w_512,w_546",0," "],["of","w_547","",0," "],["them","w_548","w_507,w_548",0," "],["has","w_549","w_519,w_520,w_549",0," "],["very","w_550","",0," "],["important","w_551","w_521,w_551",0," "],["geological","w_552","",0," "],["significance","w_553","w_523,w_553",0," "],["in","w_554","w_515,w_554",0," "],["understanding","w_555","w_516,w_555",0," "],["the","w_556","",0," "],["lunar","w_557","w_517,w_557",0," "],["evolution","w_558","w_518,w_558",0],[".","w_559","w_524,w_559",0]],"http:\\/\\/www.fabiao.net\\/content-43-23631-1.html","11"],[[["\\u5176","w_560","w_560,w_607",0],["\\u8868\\u9762","w_561","w_561,w_608",0],["\\u7684","w_562","w_562,w_606",0],["\\u4e00\\u534a","w_563","w_563,w_604,w_605",0],["\\u7531\\u4e8e","w_564","w_564,w_613,w_614",0],["\\u8f68\\u9053","w_565","w_565,w_618",0],["\\u529b\\u5b66","w_566","w_566,w_619",0],["\\u7684","w_567","w_567,w_617",0],["\\u53d8\\u5e7b\\u83ab\\u6d4b","w_568","w_568,w_616",0],["\\uff0c","w_569","w_569,w_620",0],["\\u8fd9","w_570","w_570,w_609",0],["\\u4e00\\u534a","w_571","w_571,w_610",0],["\\u603b\\u662f","w_572","w_572,w_621",0],["\\u9762\\u5bf9","w_573","w_573,w_622",0],["\\u5730\\u7403","w_574","w_574,w_623",0],["\\u4e00\\u76f4","w_575","w_575",0],["\\u5904\\u4e8e","w_576","w_576,w_624,w_625",0],["\\u9ed1\\u6697","w_577","w_577,w_627",0],["\\u4e4b\\u4e2d","w_578","w_578",0],["\\uff0c","w_579","w_579,w_628",0],["\\u8fd9","w_580","w_580",0],["\\u7247","w_581","w_581",0],["\\u9ed1\\u6697","w_582","w_582",0],["\\u7684","w_583","w_583",0],["\\u5730\\u65b9","w_584","w_584",0],["\\u88ab","w_585","w_585",0],["\\u79f0","w_586","w_586,w_587,w_636,w_637",0],["\\u4e3a","w_587","w_586,w_587,w_636,w_637",0],["\\u6708\\u6d77","w_588","w_588,w_638",1],["\\uff0c","w_589","w_589",0],["\\u4e0d\\u4ec5","w_590","w_590",0],["\\u5e73\\u5766","w_591","w_591,w_592,w_629",0],["\\u5e7f\\u9614","w_592","w_591,w_592,w_629",0],["\\uff0c","w_593","w_593",0],["\\u800c\\u4e14","w_594","w_594",0],["\\u7531","w_595","w_595,w_626",0],["\\u53e4\\u8001","w_596","w_596,w_632",0],["\\u800c","w_597","w_597,w_633",0],["\\u51bb\\u7ed3","w_598","w_598,w_634",0],["\\u7684","w_599","w_599",0],["\\u706b\\u5c71","w_600","w_600,w_601,w_635",0],["\\u5ca9","w_601","w_600,w_601,w_635",0],["\\u5f62\\u6210","w_602","w_602,w_630",0],["\\u3002","w_603","w_603,w_639",0]],[["One","w_604","w_563,w_604,w_605",0," "],["half","w_605","w_563,w_604,w_605",0," "],["of","w_606","w_562,w_606",0," "],["its","w_607","w_560,w_607",0," "],["surface","w_608","w_561,w_608",0," "],["the","w_609","w_570,w_609",0," "],["half","w_610","w_571,w_610",0," "],["which","w_611","",0],[",","w_612","",0," "],["thanks","w_613","w_564,w_613,w_614",0," "],["to","w_614","w_564,w_613,w_614",0," "],["the","w_615","",0," "],["vagaries","w_616","w_568,w_616",0," "],["of","w_617","w_567,w_617",0," "],["orbital","w_618","w_565,w_618",0," "],["mechanics","w_619","w_566,w_619",0],[",","w_620","w_569,w_620",0," "],["always","w_621","w_572,w_621",0," "],["faces","w_622","w_573,w_622",0," "],["Earth","w_623","w_574,w_623",0," "],["is","w_624","w_576,w_624,w_625",0," "],["dominated","w_625","w_576,w_624,w_625",0," "],["by","w_626","w_595,w_626",0," "],["dark","w_627","w_577,w_627",0],[",","w_628","w_579,w_628",0," "],["smooth","w_629","w_591,w_592,w_629",0," "],["expanses","w_630","w_602,w_630",0," "],["of","w_631","",0," "],["ancient","w_632","w_596,w_632",0],[",","w_633","w_597,w_633",0," "],["frozen","w_634","w_598,w_634",0," "],["lava","w_635","w_600,w_601,w_635",0," "],["known","w_636","w_586,w_587,w_636,w_637",0," "],["as","w_637","w_586,w_587,w_636,w_637",0," "],["maria","w_638","w_588,w_638",0],[".","w_639","w_603,w_639",0]],"http:\\/\\/www.remword.cn\\/article-361-1.html","12"],[[["\\u6b64\\u5916","w_640","w_640,w_679",0],["\\uff0c","w_641","w_641,w_680",0],["\\u5728","w_642","w_642,w_685",0],["\\u6708\\u7403","w_643","w_643",0],["\\u8f83","w_644","w_644",0],["\\u8fdc","w_645","w_645,w_687",0],["\\u90a3","w_646","w_646,w_686",0],["\\u4fa7","w_647","w_647,w_688",0],["\\u5982\\u6b64","w_648","w_648,w_681",0],["\\u5de8\\u5927","w_649","w_649,w_683",0],["\\u7684","w_650","w_650",0],["\\u4e00","w_651","w_651,w_682",0],["\\u6b21","w_652","w_652",0],["\\u78b0\\u649e","w_653","w_653,w_684",0],["\\u5e94\\u8be5","w_654","w_654,w_689",0],["\\u8fc5\\u901f","w_655","w_655",0],["\\u79fb\\u52a8","w_656","w_656,w_691",0],["\\u5f88\\u591a","w_657","w_657,w_692",0],["\\u5ca9\\u6d46","w_658","w_658,w_695",0],["\\u6d0b","w_659","w_659,w_696",0],["\\uff0c","w_660","w_660,w_697",0],["\\u7136\\u540e","w_661","w_661,w_698",0],["\\u5728","w_662","w_662",0],["\\u6708\\u7403","w_663","w_663,w_701",0],["\\u8868\\u9762","w_664","w_664,w_703",0],["\\u4e00\\u76f4","w_665","w_665",0],["\\u94fa","w_666","w_666,w_699",0],["\\u5230","w_667","w_667,w_704",0],["\\u8fd1\\u5730","w_668","w_668,w_706",0],["\\u4fa7","w_669","w_669,w_707",0],["\\uff0c","w_670","w_670,w_708",0],["\\u8fd9","w_671","w_671,w_709",0],["\\u5c31","w_672","w_672",0],["\\u5bfc\\u81f4","w_673","w_673,w_710",0],["\\u4e86","w_674","w_674",0],["\\u6708\\u6d77","w_675","w_675,w_716",1],["\\u7684","w_676","w_676,w_714",0],["\\u5f62\\u6210","w_677","w_677,w_713",0],["\\u3002","w_678","w_678,w_717",0]],[["Moreover","w_679","w_640,w_679",0],[",","w_680","w_641,w_680",0," "],["such","w_681","w_648,w_681",0," "],["a","w_682","w_651,w_682",0," "],["huge","w_683","w_649,w_683",0," "],["collision","w_684","w_653,w_684",0," "],["on","w_685","w_642,w_685",0," "],["the","w_686","w_646,w_686",0," "],["far","w_687","w_645,w_687",0," "],["side","w_688","w_647,w_688",0," "],["would","w_689","w_654,w_689",0," "],["have","w_690","",0," "],["shifted","w_691","w_656,w_691",0," "],["much","w_692","w_657,w_692",0," "],["of","w_693","",0," "],["the","w_694","",0," "],["magma","w_695","w_658,w_695",0," "],["ocean","w_696","w_659,w_696",0," "],["that","w_697","w_660,w_697",0," "],["then","w_698","w_661,w_698",0," "],["underlay","w_699","w_666,w_699",0," "],["the","w_700","",0," "],["moon","w_701","w_663,w_701",0],["\'s","w_702","",0," "],["surface","w_703","w_664,w_703",0," "],["to","w_704","w_667,w_704",0," "],["the","w_705","",0," "],["near","w_706","w_668,w_706",0," "],["side","w_707","w_669,w_707",0],[",","w_708","w_670,w_708",0," "],["which","w_709","w_671,w_709",0," "],["led","w_710","w_673,w_710",0," "],["to","w_711","",0," "],["the","w_712","",0," "],["formation","w_713","w_677,w_713",0," "],["of","w_714","w_676,w_714",0," "],["the","w_715","",0," "],["maria","w_716","w_675,w_716",0],[".","w_717","w_678,w_717",0]],"http:\\/\\/xiaozu.renren.com\\/xiaozu\\/228064\\/thread\\/334490112","13"],[[["\\u7ea6","w_718","w_718,w_765",0],["\\u5728","w_719","w_719,w_764",0],["31","w_720","w_720,w_766,w_767",0],["\\u00d7","w_721","w_721,w_768",0],["109a","w_722","w_722,w_770",0],["\\u81f3","w_723","w_723,w_772",0],["30","w_724","w_724,w_773,w_774",0],["\\u00d7","w_725","w_725,w_775",0],["109a","w_726","w_726,w_776,w_777",0],["\\u524d","w_727","w_727,w_779",0],["\\uff0c","w_728","w_728",0],["\\u5730","w_729","w_729,w_730,w_755",0],["\\u6708","w_730","w_729,w_730,w_755",0],["\\u8ddd\\u79bb","w_731","w_731,w_753",0],["\\u7a81\\u7136","w_732","w_732,w_759",0],["\\u66b4\\u80c0","w_733","w_733,w_760",0],["\\u4e86","w_734","w_734",0],["10","w_735","w_735,w_762",0],["\\u591a\\u500d","w_736","w_736,w_761",0],["\\uff0c","w_737","w_737,w_780",0],["\\u5bfc\\u81f4","w_738","w_738,w_781",0],["\\u592a","w_739","w_739,w_740,w_787",0],["\\u53e4\\u4ee3","w_740","w_739,w_740,w_787",0],["\\u5730\\u58f3","w_741","w_741",0],["\\u6784\\u9020","w_742","w_742,w_788",0],["\\u6d3b\\u52a8","w_743","w_743,w_785",0],["\\u548c","w_744","w_744,w_789",0],["\\u6708\\u6d77","w_745","w_745,w_794",1],["\\u7384\\u6b66\\u5ca9","w_746","w_746,w_795",0],["\\u55b7\\u53d1","w_747","w_747,w_791",0],["\\u8fc5\\u901f","w_748","w_748",0],["\\u7ec8\\u6b62","w_749","w_749,w_782",0],["\\uff1b","w_750","w_750,w_799",0]],[["Then","w_751","",0," "],["the","w_752","",0," "],["distance","w_753","w_731,w_753",0," "],["from","w_754","",0," "],["Earth","w_755","w_729,w_730,w_755",0," "],["to","w_756","",0," "],["Moon","w_757","",0," "],["had","w_758","",0," "],["suddenly","w_759","w_732,w_759",0," "],["inflated","w_760","w_733,w_760",0," "],["over","w_761","w_736,w_761",0," "],["10","w_762","w_735,w_762",0," "],["times","w_763","",0," "],["between","w_764","w_719,w_764",0," "],["about","w_765","w_718,w_765",0," "],["3","w_766","w_720,w_766,w_767",0," "],["1","w_767","w_720,w_766,w_767",0," "],["\\u00d7","w_768","w_721,w_768",0," "],["10","w_769","",0," "],["9","w_770","w_722,w_770",0," "],["a","w_771","",0," "],["and","w_772","w_723,w_772",0," "],["3","w_773","w_724,w_773,w_774",0," "],["0","w_774","w_724,w_773,w_774",0," "],["\\u00d7","w_775","w_725,w_775",0," "],["10","w_776","w_726,w_776,w_777",0," "],["9","w_777","w_726,w_776,w_777",0," "],["a","w_778","",0," "],["ago","w_779","w_727,w_779",0],[",","w_780","w_737,w_780",0," "],["which","w_781","w_738,w_781",0," "],["stopped","w_782","w_749,w_782",0," "],["the","w_783","",0," "],["mobile","w_784","",0," "],["period","w_785","w_743,w_785",0," "],["of","w_786","",0," "],["Archean","w_787","w_739,w_740,w_787",0," "],["tectonics","w_788","w_742,w_788",0," "],["and","w_789","w_744,w_789",0," "],["the","w_790","",0," "],["eruption","w_791","w_747,w_791",0," "],["of","w_792","",0," "],["the","w_793","",0," "],["Mare","w_794","w_745,w_794",0," "],["basalt","w_795","w_746,w_795",0," "],["in","w_796","",0," "],["short","w_797","",0," "],["order","w_798","",0],[".","w_799","w_750,w_799",0]],"http:\\/\\/dict.cnki.net\\/h_52022361000.html","14"],[[["\\u6839\\u636e","w_800","w_800,w_856,w_857",0],["\\u89c2\\u5bdf","w_801","w_801,w_802,w_862",0],["\\u8005","w_802","w_801,w_802,w_862",0],["\\u4e0d\\u540c","w_803","w_803",0],["\\u7684","w_804","w_804",0],["\\u6587\\u5316","w_805","w_805,w_859",0],["\\uff0c","w_806","w_806",0],["\\u6708\\u6d77","w_807","w_807,w_842",1],["\\u7684","w_808","w_808,w_840",0],["\\u9ed1\\u6697","w_809","w_809,w_839",0],["\\u548c","w_810","w_810,w_843",0],["\\u5468\\u56f4","w_811","w_811,w_848",0],["\\u7fa4\\u5c71","w_812","w_812,w_849",0],["\\u7684","w_813","w_813,w_846",0],["\\u660e\\u4eae","w_814","w_814,w_845",0],["\\u5bf9\\u6bd4","w_815","w_815,w_836",0],["\\u5f62\\u6210","w_816","w_816,w_850",0],["\\u4e86","w_817","w_817",0],["\\u4e00","w_818","w_818,w_851",0],["\\u79cd","w_819","w_819",0],["\\u4f17\\u6240\\u5468\\u77e5","w_820","w_820,w_853,w_854",0],["\\u7684","w_821","w_821",0],["\\u6a21\\u5f0f","w_822","w_822,w_852",0],["\\uff0c","w_823","w_823,w_863",0],["\\u6bd4\\u5982","w_824","w_824,w_864",0],["\\u5ae6\\u5a25","w_825","w_825",0],["\\uff0c","w_826","w_826,w_870",0],["\\u6708\\u5154","w_827","w_827,w_872",0],["\\u6216","w_828","w_828,w_876",0],["\\u8bb8\\u591a","w_829","w_829,w_879",0],["\\u5176\\u5b83","w_830","w_830,w_880",0],["\\u89c6","w_831","w_831,w_881",0],["\\u9519\\u89c9","w_832","w_832,w_882",0],["\\u4e4b\\u4e00","w_833","w_833,w_877,w_878",0],["\\u3002","w_834","w_834,w_883",0]],[["The","w_835","",0," "],["contrast","w_836","w_815,w_836",0," "],["between","w_837","",0," "],["the","w_838","",0," "],["darkness","w_839","w_809,w_839",0," "],["of","w_840","w_808,w_840",0," "],["the","w_841","",0," "],["maria","w_842","w_807,w_842",0," "],["and","w_843","w_810,w_843",0," "],["the","w_844","",0," "],["brightness","w_845","w_814,w_845",0," "],["of","w_846","w_813,w_846",0," "],["the","w_847","",0," "],["surrounding","w_848","w_811,w_848",0," "],["highlands","w_849","w_812,w_849",0," "],["forms","w_850","w_816,w_850",0," "],["a","w_851","w_818,w_851",0," "],["pattern","w_852","w_822,w_852",0," "],["popularly","w_853","w_820,w_853,w_854",0," "],["known","w_854","w_820,w_853,w_854",0],[",","w_855","",0," "],["depending","w_856","w_800,w_856,w_857",0," "],["on","w_857","w_800,w_856,w_857",0," "],["the","w_858","",0," "],["culture","w_859","w_805,w_859",0," "],["of","w_860","",0," "],["the","w_861","",0," "],["observer","w_862","w_801,w_802,w_862",0],[",","w_863","w_823,w_863",0," "],["as","w_864","w_824,w_864",0," "],["the","w_865","",0," "],["man","w_866","",0," "],["in","w_867","",0," "],["the","w_868","",0," "],["moon","w_869","",0],[",","w_870","w_826,w_870",0," "],["the","w_871","",0," "],["rabbit","w_872","w_827,w_872",0," "],["on","w_873","",0," "],["the","w_874","",0," "],["moon","w_875","",0," "],["or","w_876","w_828,w_876",0," "],["one","w_877","w_833,w_877,w_878",0," "],["of","w_878","w_833,w_877,w_878",0," "],["many","w_879","w_829,w_879",0," "],["other","w_880","w_830,w_880",0," "],["optical","w_881","w_831,w_881",0," "],["illusions","w_882","w_832,w_882",0],[".","w_883","w_834,w_883",0]],"www.keke.com","15"]]', 'tag': [], 'single': ''}, 'logid': 1994991060}
pythonObj = json.loads(content)

# 10、获得想要获取的数据
print(pythonObj['dict_result']['common']['text'])
```

### ⑥、ajax 的 get 请求（可变 url）

1. 工具类

```python
# @Time     : 2023/3/9 9:33
# @Author   : 月海
# @File     : utils
# @Project  : 01_python

# 导包
import urllib.parse
import urllib.request
import json


# 定制 get 请求请求头
def get_request(url, data):
    # 1、转码，拼接字符串
    url = url + urllib.parse.urlencode(data)

    # 2、定制请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }

    # 3、定制请求对象
    request = urllib.request.Request(url=url, headers=headers)

    # 4、模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)

    # 5、获取请求返回的结果
    content = response.read().decode('utf-8')

    # 6、将返回的 json 字符串转为 json 对象（集合）
    return json.loads(content)
```

2. 实现类

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 9:15
# @Author   : 月海
# @File     : _06_ajax 的 get 请求
# @Project  : 01_python

# 爬取豆瓣电影第一页数据；每页 20 条
# https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20

# 导包
from utils import get_request

# 1、定义一个 url，就是要访问的地址
url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&'

# 2、定义一个集合以存放数据
dataList = []

# 循环查询
start = 0
limit = 20
while start <= 200:
    # 3、参数
    data = {
        'start': start,
        'limit': limit
    }

    # 4、调用封装的方法，得到 json 对象（集合）
    pythonObj = get_request(url, data)

    # 5、对得到的数据进行处理
    for content in pythonObj:
        data = [
            '排名：' + str(content['rank']),
            '名字：' + str(content['title']),
            '评分：' + str(content['score']),
            '产地：' + str(content['regions']),
            '类型：' + str(content['types']),
            '发布日期：' + str(content['release_date']),
            '链接地址：' + str(content['url']),
        ]

        dataList.append(data)

    # 6、 start
    start += 20

# 7、遍历生成的数据
for data in dataList:
    print(data)
```

3. 结果；好像只有 142 条数据

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\11_爬虫\_01_Urllib\_06_ajax 的 get 请求.py" 
['排名：1', '名字：千与千寻', '评分：9.4', "产地：['日本']", "类型：['剧情', '动画', '奇幻']", '发布日期：2019-06-21', '链接地址：https://movie.douban.com/subject/1291561/']
['排名：2', '名字：大闹天宫', '评分：9.4', "产地：['中国大陆']", "类型：['剧情', '动画', '奇幻', '古装']", '发布日期：1961', '链接地址：https://movie.douban.com/subject/1418019/']
['排名：3', '名字：机器人总动员', '评分：9.3', "产地：['美国']", "类型：['科幻', '动画', '冒险']", '发布日期：2008-06-27', '链接地址：https://movie.douban.com/subject/2131459/']
['排名：4', '名字：疯狂动物城', '评分：9.2', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2016-03-04', '链接地址：https://movie.douban.com/subject/25662329/']
['排名：5', '名字：龙猫', '评分：9.2', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：2018-12-14', '链接地址：https://movie.douban.com/subject/1291560/']
['排名：6', '名字：天空之城', '评分：9.2', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：1992-05-01', '链接地址：https://movie.douban.com/subject/1291583/']
['排名：7', '名字：天书奇谭', '评分：9.2', "产地：['中国大陆']", "类型：['动画', '奇幻']", '发布日期：2021-11-05', '链接地址：https://movie.douban.com/subject/1428581/']
['排名：8', '名字：哪吒闹海', '评分：9.2', "产地：['中国大陆']", "类型：['冒险', '动画', '奇幻']", '发布日期：1979-05-19', '链接地址：https://movie.douban.com/subject/1307315/']
['排名：9', '名字：寻梦环游记', '评分：9.1', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '音乐']", '发布日期：2017-11-24', '链接地址：https://movie.douban.com/subject/20495023/']
['排名：10', '名字：飞屋环游记', '评分：9.1', "产地：['美国']", "类型：['剧情', '喜剧', '动画', '冒险']", '发布日期：2009-08-04', '链接地址：https://movie.douban.com/subject/2129039/']
['排名：11', '名字：哈尔的移动城堡', '评分：9.1', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：2004-09-05', '链接地址：https://movie.douban.com/subject/1308807/']
['排名：12', '名字：狮子王', '评分：9.1', "产地：['美国']", "类型：['动画', '冒险', '歌舞']", '发布日期：1995-07-15', '链接地址：https://movie.douban.com/subject/1301753/']
['排名：13', '名字：红辣椒', '评分：9.1', "产地：['日本']", "类型：['动画', '悬疑', '科幻', '惊悚']", '发布日期：2006-09-02', '链接地址：https://movie.douban.com/subject/1865703/']
['排名：14', '名字：未麻的部屋', '评分：9.1', "产地：['日本']", "类型：['动画', '奇幻', '惊悚']", '发布日期：1997-08-05', '链接地址：https://movie.douban.com/subject/1395091/']
['排名：15', '名字：攻壳机动队', '评分：9.1', "产地：['日本']", "类型：['动作', '科幻', '动画']", '发布日期：1995-11-18', '链接地址：https://movie.douban.com/subject/1291936/']
['排名：16', '名字：东京教父', '评分：9.0', "产地：['日本']", "类型：['剧情', '喜剧', '动画']", '发布日期：2003-11-08', '链接地址：https://movie.douban.com/subject/1310177/']
['排名：17', '名字：借东西的小人阿莉埃蒂', '评分：8.9', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：2010-07-17', '链接地址：https://movie.douban.com/subject/4202302/']
['排名：18', '名字：萤火之森', '评分：8.9', "产地：['日本']", "类型：['剧情', '爱情', '动画', '奇幻']", '发布日期：2011-09-17', '链接地址：https://movie.douban.com/subject/5989818/']
['排名：19', '名字：幽灵公主', '评分：8.9', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：1997-07-12', '链接地址：https://movie.douban.com/subject/1297359/']
['排名：20', '名字：玩具总动员3', '评分：8.9', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：2010-06-16', '链接地址：https://movie.douban.com/subject/1858711/']
['排名：21', '名字：侧耳倾听', '评分：8.9', "产地：['日本']", "类型：['剧情', '爱情', '动画']", '发布日期：1995-07-15', '链接地址：https://movie.douban.com/subject/1297052/']
['排名：22', '名字：玛丽和马克思', '评分：8.9', "产地：['澳大利亚', '美国']", "类型：['剧情', '喜剧', '动画']", '发布日期：2009-01-15', '链接地址：https://movie.douban.com/subject/3072124/']
['排名：23', '名字：风之谷', '评分：8.9', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：1984-03-11', '链接地址：https://movie.douban.com/subject/1291585/']
['排名：24', '名字：攻壳机动队2：无罪', '评分：9.2', "产地：['日本']", "类型：['剧情', '科幻', '动画']", '发布日期：2004-03-06', '链接地址：https://movie.douban.com/subject/1291566/']
['排名：25', '名字：你看起来好像很好吃', '评分：8.9', "产地：['日本']", "类型：['剧情', '动画', '儿童']", '发布日期：2010-10-16', '链接地址：https://movie.douban.com/subject/4848115/']
['排名：26', '名字：驯龙高手', '评分：8.8', "产地：['美国']", "类型：['动画', '奇幻', '冒险']", '发布日期：2010-05-14', '链接地址：https://movie.douban.com/subject/2353023/']
['排名：27', '名字：怪兽电力公司', '评分：8.8', "产地：['美国']", "类型：['儿童', '喜剧', '动画', '奇幻', '冒险']", '发布日期：2001-11-02', '链接地址：https://movie.douban.com/subject/1291579/']
['排名：28', '名字：头脑特工队', '评分：8.8', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2015-10-06', '链接地址：https://movie.douban.com/subject/10533913/']
['排名：29', '名字：千年女优', '评分：8.8', "产地：['日本']", "类型：['动画', '剧情', '爱情']", '发布日期：2001-07-28', '链接地址：https://movie.douban.com/subject/1307394/']
['排名：30', '名字：超能陆战队', '评分：8.7', "产地：['美国']", "类型：['喜剧', '动作', '科幻', '动画', '冒险']", '发布日期：2015-02-28', '链接地址：https://movie.douban.com/subject/11026735/']
['排名：31', '名字：心灵奇旅', '评分：8.7', "产地：['美国']", "类型：['动画', '奇幻', '音乐']", '发布日期：2020-12-25', '链接地址：https://movie.douban.com/subject/24733428/']
['排名：32', '名字：神偷奶爸', '评分：8.7', "产地：['美国', '法国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2010-06-20', '链接地址：https://movie.douban.com/subject/3287562/']
['排名：33', '名字：疯狂原始人', '评分：8.7', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2013-04-20', '链接地址：https://movie.douban.com/subject/1907966/']
['排名：34', '名字：海洋之歌', '评分：8.8', "产地：['爱尔兰', '丹麦', '比利时', '卢森堡', '法国']", "类型：['动画', '奇幻', '冒险']", '发布日期：2016-08-12', '链接地址：https://movie.douban.com/subject/11584019/']
['排名：35', '名字：无敌破坏王', '评分：8.7', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：2012-11-06', '链接地址：https://movie.douban.com/subject/6534248/']
['排名：36', '名字：同级生', '评分：9.1', "产地：['日本']", "类型：['爱情', '动画', '同性']", '发布日期：2016-02-20', '链接地址：https://movie.douban.com/subject/26344688/']
['排名：37', '名字：魔女宅急便', '评分：8.7', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：1989-07-29', '链接地址：https://movie.douban.com/subject/1307811/']
['排名：38', '名字：萤火虫之墓', '评分：8.7', "产地：['日本']", "类型：['动画', '剧情', '战争']", '发布日期：1988-04-16', '链接地址：https://movie.douban.com/subject/1293318/']
['排名：39', '名字：进击的巨人 最终季 完结篇 前篇', '评分：9.7', "产地：['日本']", "类型：['动作', '动画', '奇幻']", '发布日期：2023-03-03', '链接地址：https://movie.douban.com/subject/35853587/']
['排名：40', '名字：伦敦一家人', '评分：8.9', "产地：['英国']", "类型：['剧情', '动画', '家庭']", '发布日期：2016-10-15', '链接地址：https://movie.douban.com/subject/5327189/']
['排名：41', '名字：冰川时代', '评分：8.6', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2002-03-15', '链接地址：https://movie.douban.com/subject/1291578/']
['排名：42', '名字：蜘蛛侠：平行宇宙', '评分：8.6', "产地：['美国']", "类型：['动作', '科幻', '动画', '冒险']", '发布日期：2018-12-21', '链接地址：https://movie.douban.com/subject/26374197/']
['排名：43', '名字：崖上的波妞', '评分：8.6', "产地：['日本']", "类型：['动画', '奇幻', '冒险']", '发布日期：2020-12-31', '链接地址：https://movie.douban.com/subject/1959877/']
['排名：44', '名字：穿越时空的少女', '评分：8.6', "产地：['日本']", "类型：['剧情', '爱情', '科幻', '动画']", '发布日期：2006-07-15', '链接地址：https://movie.douban.com/subject/1937946/']
['排名：45', '名字：葫芦兄弟', '评分：8.8', "产地：['中国大陆']", "类型：['动画']", '发布日期：2008-05-27', '链接地址：https://movie.douban.com/subject/3062897/']
['排名：46', '名字：玩具总动员', '评分：8.6', "产地：['美国']", "类型：['喜剧', '动画', '家庭']", '发布日期：1995-11-22', '链接地址：https://movie.douban.com/subject/1291575/']
['排名：47', '名字：麦兜故事', '评分：8.6', "产地：['中国香港']", "类型：['剧情', '喜剧', '动画']", '发布日期：2001-12-15', '链接地址：https://movie.douban.com/subject/1302476/']
['排名：48', '名字：艾特熊和赛娜鼠', '评分：9.0', "产地：['法国']", "类型：['动画']", '发布日期：2012-05-23', '链接地址：https://movie.douban.com/subject/6518638/']
['排名：49', '名字：狼的孩子雨和雪', '评分：8.7', "产地：['日本']", "类型：['剧情', '动画', '奇幻', '家庭']", '发布日期：2012-07-21', '链接地址：https://movie.douban.com/subject/7064681/']
['排名：50', '名字：我在伊朗长大', '评分：8.7', "产地：['法国', '美国']", "类型：['剧情', '传记', '动画']", '发布日期：2007-05-23', '链接地址：https://movie.douban.com/subject/1962116/']
['排名：51', '名字：回忆三部曲', '评分：8.9', "产地：['日本']", "类型：['动画', '奇幻', '科幻', '惊悚']", '发布日期：1995-12-23', '链接地址：https://movie.douban.com/subject/1307897/']
['排名：52', '名字：红猪', '评分：8.6', "产地：['日本']", "类型：['喜剧', '动画', '冒险']", '发布日期：1992-07-18', '链接地址：https://movie.douban.com/subject/1291838/']
['排名：53', '名字：你的名字。', '评分：8.5', "产地：['日本']", "类型：['剧情', '爱情', '动画']", '发布日期：2016-12-02', '链接地址：https://movie.douban.com/subject/26683290/']
['排名：54', '名字：了不起的狐狸爸爸', '评分：8.6', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2009-10-14', '链接地址：https://movie.douban.com/subject/1759386/']
['排名：55', '名字：海底总动员', '评分：8.5', "产地：['美国', '澳大利亚']", "类型：['喜剧', '动画', '冒险']", '发布日期：2003-07-30', '链接地址：https://movie.douban.com/subject/1291586/']
['排名：56', '名字：美食总动员', '评分：8.5', "产地：['美国']", "类型：['喜剧', '动画', '奇幻']", '发布日期：2007-10-19', '链接地址：https://movie.douban.com/subject/1793491/']
['排名：57', '名字：疯狂约会美丽都', '评分：8.7', "产地：['法国', '比利时', '加拿大', '英国', '拉脱维亚']", "类型：['喜剧', '动画']", '发布日期：2003-06-11', '链接地址：https://movie.douban.com/subject/1291565/']
['排名：58', '名字：岁月的童话', '评分：8.6', "产地：['日本']", "类型：['剧情', '爱情', '动画']", '发布日期：1991-07-20', '链接地址：https://movie.douban.com/subject/1291588/']
['排名：59', '名字：宝莲灯', '评分：8.5', "产地：['中国大陆']", "类型：['动画', '奇幻', '冒险']", '发布日期：1999-07-30', '链接地址：https://movie.douban.com/subject/1299643/']
['排名：60', '名字：麦兜·我和我妈妈', '评分：8.6', "产地：['中国香港', '中国大陆']", "类型：['喜剧', '动画', '家庭']", '发布日期：2014-10-01', '链接地址：https://movie.douban.com/subject/25884416/']
['排名：61', '名字：玩具总动员4', '评分：8.5', "产地：['美国']", "类型：['喜剧', '动画', '奇幻']", '发布日期：2019-06-21', '链接地址：https://movie.douban.com/subject/6850547/']
['排名：62', '名字：魔术师', '评分：8.7', "产地：['法国', '英国']", "类型：['剧情', '动画']", '发布日期：2010-06-16', '链接地址：https://movie.douban.com/subject/1921583/']
['排名：63', '名字：河童之夏', '评分：8.7', "产地：['日本']", "类型：['喜剧', '动画', '奇幻']", '发布日期：2007-07-28', '链接地址：https://movie.douban.com/subject/2982823/']
['排名：64', '名字：狐妖小红娘剧场版：月红篇', '评分：9.3', "产地：['中国大陆']", "类型：['爱情', '动画', '奇幻']", '发布日期：2016-06-24', '链接地址：https://movie.douban.com/subject/26972694/']
['排名：65', '名字：玩具总动员2', '评分：8.5', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：1999-11-24', '链接地址：https://movie.douban.com/subject/1291574/']
['排名：66', '名字：狐妖小红娘剧场版：王权富贵', '评分：9.3', "产地：['中国大陆']", "类型：['剧情', '喜剧', '爱情', '动画']", '发布日期：2016-05-20', '链接地址：https://movie.douban.com/subject/26946612/']
['排名：67', '名字：至爱梵高·星空之谜', '评分：8.5', "产地：['英国', '波兰']", "类型：['剧情', '传记', '动画']", '发布日期：2017-12-08', '链接地址：https://movie.douban.com/subject/25837262/']
['排名：68', '名字：哪吒之魔童降世', '评分：8.4', "产地：['中国大陆']", "类型：['剧情', '喜剧', '动画', '奇幻']", '发布日期：2019-07-26', '链接地址：https://movie.douban.com/subject/26794435/']
['排名：69', '名字：麦兜·当当伴我心', '评分：8.5', "产地：['中国大陆', '中国香港']", "类型：['喜剧', '动画']", '发布日期：2012-07-10', '链接地址：https://movie.douban.com/subject/10772258/']
['排名：70', '名字：我的邻居山田君', '评分：8.8', "产地：['日本']", "类型：['动画', '喜剧', '家庭']", '发布日期：1999-07-17', '链接地址：https://movie.douban.com/subject/1417728/']
['排名：71', '名字：美女与野兽', '评分：8.5', "产地：['美国']", "类型：['喜剧', '爱情', '动画', '歌舞', '奇幻']", '发布日期：1991-09-29', '链接地址：https://movie.douban.com/subject/1297995/']
['排名：72', '名字：魁拔Ⅲ战神崛起', '评分：8.6', "产地：['中国大陆']", "类型：['动作', '动画', '奇幻', '冒险']", '发布日期：2014-10-01', '链接地址：https://movie.douban.com/subject/24723061/']
['排名：73', '名字：冰雪奇缘', '评分：8.4', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '歌舞']", '发布日期：2014-02-05', '链接地址：https://movie.douban.com/subject/4202982/']
['排名：74', '名字：百变狸猫', '评分：8.6', "产地：['日本']", "类型：['动画', '喜剧', '剧情', '奇幻']", '发布日期：1994-07-16', '链接地址：https://movie.douban.com/subject/1303907/']
['排名：75', '名字：迷墙', '评分：8.8', "产地：['英国']", "类型：['剧情', '动画', '奇幻']", '发布日期：1982-05-22', '链接地址：https://movie.douban.com/subject/1296157/']
['排名：76', '名字：黑客帝国动画版', '评分：8.8', "产地：['美国', '日本']", "类型：['动作', '剧情', '动画', '科幻']", '发布日期：2003-06-03', '链接地址：https://movie.douban.com/subject/1292347/']
['排名：77', '名字：心理游戏', '评分：8.9', "产地：['日本']", "类型：['动画', '冒险', '喜剧', '悬疑']", '发布日期：2004-08-07', '链接地址：https://movie.douban.com/subject/1477916/']
['排名：78', '名字：克劳斯：圣诞节的秘密', '评分：8.7', "产地：['西班牙', '英国', '美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2019-11-08', '链接地址：https://movie.douban.com/subject/26858510/']
['排名：79', '名字：西游记之大圣归来', '评分：8.3', "产地：['中国大陆']", "类型：['剧情', '动画', '奇幻']", '发布日期：2015-07-10', '链接地址：https://movie.douban.com/subject/26277313/']
['排名：80', '名字：雄狮少年', '评分：8.3', "产地：['中国大陆']", "类型：['剧情', '喜剧', '动画']", '发布日期：2021-12-17', '链接地址：https://movie.douban.com/subject/35144311/']
['排名：81', '名字：神兵小将', '评分：8.8', "产地：['中国大陆']", "类型：['动画', '奇幻']", '发布日期：2009-10-01', '链接地址：https://movie.douban.com/subject/3012377/']
['排名：82', '名字：秒速5厘米', '评分：8.3', "产地：['日本']", "类型：['动画', '剧情', '爱情']", '发布日期：2007-03-03', '链接地址：https://movie.douban.com/subject/2043546/']
['排名：83', '名字：辉夜姬物语', '评分：8.5', "产地：['日本']", "类型：['动画', '奇幻', '古装']", '发布日期：2013-11-23', '链接地址：https://movie.douban.com/subject/4099231/']
['排名：84', '名字：阿基拉', '评分：8.5', "产地：['日本']", "类型：['动作', '科幻', '动画']", '发布日期：1988-07-16', '链接地址：https://movie.douban.com/subject/1302770/']
['排名：85', '名字：僵尸新娘', '评分：8.3', "产地：['美国', '英国']", "类型：['剧情', '动画', '奇幻']", '发布日期：2005-09-07', '链接地址：https://movie.douban.com/subject/1309060/']
['排名：86', '名字：怪兽大学', '评分：8.3', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2013-08-23', '链接地址：https://movie.douban.com/subject/3789848/']
['排名：87', '名字：小王子', '评分：8.3', "产地：['法国']", "类型：['动画', '奇幻']", '发布日期：2015-10-16', '链接地址：https://movie.douban.com/subject/20645098/']
['排名：88', '名字：言叶之庭', '评分：8.3', "产地：['日本']", "类型：['爱情', '动画']", '发布日期：2013-05-31', '链接地址：https://movie.douban.com/subject/20470074/']
['排名：89', '名字：里约大冒险', '评分：8.3', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2011-04-08', '链接地址：https://movie.douban.com/subject/3731581/']
['排名：90', '名字：反叛的童谣', '评分：8.7', "产地：['英国']", "类型：['动画']", '发布日期：2016-12-26', '链接地址：https://movie.douban.com/subject/27073245/']
['排名：91', '名字：熊出没之过年', '评分：8.6', "产地：['中国大陆']", "类型：['剧情', '儿童', '喜剧', '动画', '冒险', '家庭']", '发布日期：2013-02-08', '链接地址：https://movie.douban.com/subject/21359690/']
['排名：92', '名字：白雪公主和七个小矮人', '评分：8.4', "产地：['美国']", "类型：['爱情', '动画', '奇幻', '歌舞']", '发布日期：1937-12-21', '链接地址：https://movie.douban.com/subject/1297756/']
['排名：93', '名字：魔发奇缘', '评分：8.3', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2010-11-24', '链接地址：https://movie.douban.com/subject/1863766/']
['排名：94', '名字：金猴降妖', '评分：9.2', "产地：['中国大陆']", "类型：['剧情', '动画', '奇幻']", '发布日期：1985', '链接地址：https://movie.douban.com/subject/1780256/']
['排名：95', '名字：冰川时代3', '评分：8.3', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2009-07-08', '链接地址：https://movie.douban.com/subject/2357162/']
['排名：96', '名字：邋遢大王奇遇记', '评分：8.6', "产地：['中国大陆']", "类型：['动画', '儿童']", '发布日期：2012-08-17', '链接地址：https://movie.douban.com/subject/11502154/']
['排名：97', '名字：小羊肖恩', '评分：8.4', "产地：['英国', '法国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2015-07-17', '链接地址：https://movie.douban.com/subject/24397586/']
['排名：98', '名字：鬼妈妈', '评分：8.3', "产地：['美国']", "类型：['动画', '奇幻', '冒险']", '发布日期：2009-02-06', '链接地址：https://movie.douban.com/subject/1919245/']
['排名：99', '名字：星际宝贝', '评分：8.5', "产地：['美国']", "类型：['喜剧', '科幻', '动画', '冒险', '家庭']", '发布日期：2002-06-16', '链接地址：https://movie.douban.com/subject/1307547/']
['排名：100', '名字：恶童', '评分：8.5', "产地：['日本']", "类型：['动画', '动作', '冒险', '犯罪']", '发布日期：2006-12-23', '链接地址：https://movie.douban.com/subject/1848925/']
['排名：101', '名字：小美人鱼', '评分：8.4', "产地：['美国']", "类型：['爱情', '动画', '奇幻', '歌舞']", '发布日期：1989-11-17', '链接地址：https://movie.douban.com/subject/1293120/']
['排名：102', '名字：蝙蝠侠：黑暗骑士归来(下)', '评分：8.9', "产地：['美国']", "类型：['动作', '动画']", '发布日期：2013-01-29', '链接地址：https://movie.douban.com/subject/11443810/']
['排名：103', '名字：功夫熊猫', '评分：8.2', "产地：['美国']", "类型：['喜剧', '动作', '动画', '冒险']", '发布日期：2008-06-20', '链接地址：https://movie.douban.com/subject/1783457/']
['排名：104', '名字：凯尔经的秘密', '评分：8.5', "产地：['爱尔兰', '法国', '比利时']", "类型：['动画', '奇幻', '冒险']", '发布日期：2009-02-08', '链接地址：https://movie.douban.com/subject/3212221/']
['排名：105', '名字：101忠狗', '评分：8.5', "产地：['美国']", "类型：['喜剧', '动画', '冒险', '家庭']", '发布日期：1961-01-25', '链接地址：https://movie.douban.com/subject/1298204/']
['排名：106', '名字：辛普森一家', '评分：8.4', "产地：['美国']", "类型：['动画', '冒险', '喜剧']", '发布日期：2007-07-27', '链接地址：https://movie.douban.com/subject/1851906/']
['排名：107', '名字：养家之人', '评分：8.3', "产地：['爱尔兰', '加拿大', '卢森堡', '美国', '英国', '法国']", "类型：['剧情', '动画', '家庭']", '发布日期：2019-01-11', '链接地址：https://movie.douban.com/subject/26346327/']
['排名：108', '名字：青春变形记', '评分：8.2', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：2022-03-11', '链接地址：https://movie.douban.com/subject/35284253/']
['排名：109', '名字：超人总动员', '评分：8.2', "产地：['美国']", "类型：['喜剧', '动作', '动画', '冒险']", '发布日期：2005-01-28', '链接地址：https://movie.douban.com/subject/1291577/']
['排名：110', '名字：起风了', '评分：8.2', "产地：['日本']", "类型：['剧情', '爱情', '动画']", '发布日期：2013-07-20', '链接地址：https://movie.douban.com/subject/6791750/']
['排名：111', '名字：冰川时代2：融冰之灾', '评分：8.2', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2006-06-09', '链接地址：https://movie.douban.com/subject/1437342/']
['排名：112', '名字：犬之岛', '评分：8.2', "产地：['德国', '日本', '美国', '英国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2018-04-20', '链接地址：https://movie.douban.com/subject/26640371/']
['排名：113', '名字：猫的报恩', '评分：8.2', "产地：['日本']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：2002-07-19', '链接地址：https://movie.douban.com/subject/1304970/']
['排名：114', '名字：仙履奇缘', '评分：8.4', "产地：['美国']", "类型：['爱情', '动画', '奇幻', '歌舞']", '发布日期：1950-03-04', '链接地址：https://movie.douban.com/subject/1294461/']
['排名：115', '名字：马达加斯加3', '评分：8.2', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2012-06-08', '链接地址：https://movie.douban.com/subject/3178770/']
['排名：116', '名字：大坏狐狸的故事', '评分：8.3', "产地：['法国', '比利时', '美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2018-03-16', '链接地址：https://movie.douban.com/subject/27042405/']
['排名：117', '名字：神偷奶爸2', '评分：8.1', "产地：['美国', '法国', '日本']", "类型：['喜剧', '动画', '冒险']", '发布日期：2014-01-10', '链接地址：https://movie.douban.com/subject/4915857/']
['排名：118', '名字：魁拔之十万火急', '评分：8.2', "产地：['中国大陆']", "类型：['儿童', '动画', '奇幻', '冒险']", '发布日期：2011-07-08', '链接地址：https://movie.douban.com/subject/4812830/']
['排名：119', '名字：海绵宝宝历险记', '评分：8.5', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2004-11-19', '链接地址：https://movie.douban.com/subject/1309156/']
['排名：120', '名字：驯龙高手2', '评分：8.1', "产地：['美国']", "类型：['动画', '奇幻', '冒险']", '发布日期：2014-08-14', '链接地址：https://movie.douban.com/subject/4824512/']
['排名：121', '名字：阿拉丁', '评分：8.3', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：1992-11-25', '链接地址：https://movie.douban.com/subject/1299513/']
['排名：122', '名字：欢乐好声音', '评分：8.1', "产地：['美国']", "类型：['喜剧', '动画', '歌舞']", '发布日期：2017-02-17', '链接地址：https://movie.douban.com/subject/26354572/']
['排名：123', '名字：哆啦A梦：伴我同行', '评分：8.1', "产地：['日本']", "类型：['剧情', '动画']", '发布日期：2015-05-28', '链接地址：https://movie.douban.com/subject/25769362/']
['排名：124', '名字：精灵旅社', '评分：8.1', "产地：['美国']", "类型：['喜剧', '动画', '奇幻']", '发布日期：2013-11-01', '链接地址：https://movie.douban.com/subject/3269068/']
['排名：125', '名字：小鹿斑比', '评分：8.6', "产地：['美国']", "类型：['剧情', '动画']", '发布日期：1942-08-21', '链接地址：https://movie.douban.com/subject/1295148/']
['排名：126', '名字：她的回忆', '评分：8.8', "产地：['日本']", "类型：['动画', '冒险', '科幻']", '发布日期：1995-12-23', '链接地址：https://movie.douban.com/subject/5162334/']
['排名：127', '名字：给桃子的信', '评分：8.3', "产地：['日本']", "类型：['剧情', '动画']", '发布日期：2011-09-10', '链接地址：https://movie.douban.com/subject/6010171/']
['排名：128', '名字：圣诞夜惊魂', '评分：8.2', "产地：['美国']", "类型：['动画', '奇幻', '音乐']", '发布日期：1993-10-29', '链接地址：https://movie.douban.com/subject/1297131/']
['排名：129', '名字：冰川时代4', '评分：8.1', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2012-07-27', '链接地址：https://movie.douban.com/subject/4914468/']
['排名：130', '名字：木偶奇遇记', '评分：8.4', "产地：['美国']", "类型：['剧情', '动画', '奇幻', '音乐']", '发布日期：1940-02-07', '链接地址：https://movie.douban.com/subject/1292757/']
['排名：131', '名字：赛车总动员', '评分：8.1', "产地：['美国']", "类型：['喜剧', '动画', '冒险']", '发布日期：2006-08-22', '链接地址：https://movie.douban.com/subject/1428878/']
['排名：132', '名字：守护者联盟', '评分：8.2', "产地：['美国']", "类型：['动画', '家庭', '奇幻', '冒险']", '发布日期：2012-11-16', '链接地址：https://movie.douban.com/subject/3769423/']
['排名：133', '名字：罗小黑战记', '评分：8.0', "产地：['中国大陆']", "类型：['动作', '动画', '奇幻']", '发布日期：2019-09-07', '链接地址：https://movie.douban.com/subject/26709258/']
['排名：134', '名字：正义联盟：闪点悖论', '评分：8.7', "产地：['美国']", "类型：['动作', '科幻', '动画', '奇幻', '冒险']", '发布日期：2013-07-30', '链接地址：https://movie.douban.com/subject/24718965/']
['排名：135', '名字：昆虫总动员', '评分：8.4', "产地：['法国', '比利时']", "类型：['动画', '冒险']", '发布日期：2014-08-22', '链接地址：https://movie.douban.com/subject/23048775/']
['排名：136', '名字：听到涛声', '评分：8.2', "产地：['日本']", "类型：['剧情', '爱情', '动画']", '发布日期：1993-05-05', '链接地址：https://movie.douban.com/subject/1418640/']
['排名：137', '名字：功夫熊猫2', '评分：8.0', "产地：['美国']", "类型：['喜剧', '动作', '动画', '冒险']", '发布日期：2011-05-28', '链接地址：https://movie.douban.com/subject/3233635/']
['排名：138', '名字：最终幻想7：圣子降临', '评分：8.3', "产地：['日本']", "类型：['动画', '动作', '科幻', '惊悚']", '发布日期：2005-08-31', '链接地址：https://movie.douban.com/subject/1422063/']
['排名：139', '名字：爱丽丝梦游仙境', '评分：8.7', "产地：['美国']", "类型：['动画', '奇幻', '冒险', '歌舞']", '发布日期：1951-07-26', '链接地址：https://movie.douban.com/subject/1310178/']
['排名：140', '名字：无敌破坏王2：大闹互联网', '评分：8.0', "产地：['美国']", "类型：['喜剧', '动画', '奇幻', '冒险']", '发布日期：2018-11-23', '链接地址：https://movie.douban.com/subject/20438964/']
['排名：141', '名字：熊出没之雪岭熊风', '评分：8.2', "产地：['中国大陆']", "类型：['喜剧', '动画', '冒险', '家庭']", '发布日期：2015-01-30', '链接地址：https://movie.douban.com/subject/26220731/']
['排名：142', '名字：原始星球', '评分：8.8', "产地：['法国', '捷克斯洛伐克']", "类型：['动画', '科幻']", '发布日期：1973-12-06', '链接地址：https://movie.douban.com/subject/1291989/']

进程已结束,退出代码0
```

### ⑦、异常 `URLError`、`HTTPError`

1. `HTTPError` 类是 `URLError` 类的子类
2. 导入的包 `urllib.error.HTTPError`、`urllib.error.URLError`
3. http 错误：http 错误是针对浏览器无法连接到服务器而增加出来的错误提示。引导并告诉浏览者该页是哪里出了问题。
4. 通过 urllib 发送请求的时候，有可能会发送失败，这个时候如果想让你的代码更加的健壮，可以通过 `try‐except` 进行捕获异常

### ⑧、cookie 登录

1. 适用的场景：数据采集的时候，需要绕过登陆，然后进入到某个页面
2. 什么情况下访问不成功：因为请求头的信息不够，所以访问不成功
3. cookie 中携带着你的登陆信息，如果有登陆之后的 cookie，那么我们就可以携带着 cookie 进入到任何页面

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 12:42
# @Author   : 月海
# @File     : _08_cookie 登录
# @Project  : 01_python

# 导包
import urllib.parse
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'https://user.qzone.qq.com/770717410'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'cookie': 'RK=vJ3RrlEBbZ; ptcz=1bd4831c599282d7f8b93f2f084124440536b2636221c5adbe2fc18c28c86790; pgv_pvid=7331529375; pac_uid=1_770717410; iip=0; ptui_loginuin=2274064464; o_cookie=770717410; uin=o0770717410; skey=@3RjUIrFdM; p_uin=o0770717410; pt4_token=Xz54Z*Y5sbuOw5jbN575pjBosd8MegEl23iMi4htVCM_; p_skey=6adfiyPffSaSnhNV16YVgti0xkn99cL0LRcNbzBzGDw_; Loading=Yes; qz_screen=1920x1080; pgv_info=ssid=s8835443925; QZ_FE_WEBP_SUPPORT=1; _qpsvr_localtk=0.41779585995479396; __Q_w_s__QZN_TodoMsgCnt=1; cpu_performance_v8=42'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 4、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 5、打印
print(response.read().decode('utf8'))
```

### ⑨、Handler 处理器

1. `urllib.request.urlopen(url)`：不能定制请求头
2. `urllib.request.Request(url,headers,data)`：可以定制请求头
3. `Handler`：定制更高级的请求头；随着业务逻辑的复杂，请求对象的定制已经满足不了我们的需求（动态 cookie 和代理不能使用请求对象的定制

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 13:31
# @Author   : 月海
# @File     : _09_Handler 处理器
# @Project  : 01_python

# 导包
import urllib.request

# 定义一个 url，就是要访问的地址
url = 'https://www.baidu.com/s?wd=%E6%9C%88%E6%B5%B7'
# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}
# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 1、获取 handler 对象
handler = urllib.request.HTTPHandler()
# 2、获取 opener 对象
opener = urllib.request.build_opener(handler)
# 3、调用 open 方法；模拟浏览器向服务器发送请求
response = opener.open(request)

# 打印
print(response.read().decode('utf8'))
```

### ⑩、代理服务器

> 快代理的免费代理：https://www.kuaidaili.com/free/

1. 代理的常用功能：
	1. 突破自身IP访问限制，访问国外站点。
	2. 访问一些单位或团体内部资源；扩展：某大学 FTP(前提是该代理地址在该资源的允许访问范围之内)，使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类 FTP 下载上传，以及各类资料查询共享等服务。
	3. 提高访问速度；扩展：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时， 则直接由缓冲区中取出信息，传给用户，以提高访问速度。
	4. 隐藏真实 IP；扩展：上网者也可以通过这种方法隐藏自己的IP，免受攻击。
2. 代码配置代理：
	1. 创建 `Reuqest` 对象
	2. 创建 `ProxyHandler` 对象
	3. 用 `handler` 对象创建 `opener` 对象
	4. 使用 `opener.open` 函数发送请求

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 14:10
# @Author   : 月海
# @File     : _10_02_代理服务器
# @Project  : 01_python

# 导包
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'http://www.baidu.com/s?wd=ip'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 2、设置代理服务器
proxies = {'http': '47.92.113.71:80'}
# 4、获取 handler 对象；设置代理服务器
handler = urllib.request.ProxyHandler(proxies)
# 5、获取 opener 对象
opener = urllib.request.build_opener(handler)
# 6、调用 open 方法；模拟浏览器向服务器发送请求
response = opener.open(request)

# 7、获取请求返回的结果
content = response.read().decode('utf-8')
print(content)

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
```

### ⑪、代理池

> 就是一个集合里放了很多 ip，然后通过随机函数随机取一个出来用

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 14:26
# @Author   : 月海
# @File     : _11_代理池
# @Project  : 01_python

# 导包
import urllib.request
import random

# 1、定义一个 url，就是要访问的地址
url = 'http://www.baidu.com/s?wd=ip'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 3、定制请求对象
request = urllib.request.Request(url=url, headers=headers)

# 2、设置代理服务器
proxies = [
    {'http': '47.92.113.71:80'},
    {'http': '47.92.113.71:81'},
    {'http': '47.92.113.71:82'},
]
# 4、获取 handler 对象；设置代理服务器
handler = urllib.request.ProxyHandler(random.choice(proxies))
# 5、获取 opener 对象
opener = urllib.request.build_opener(handler)
# 6、调用 open 方法；模拟浏览器向服务器发送请求
response = opener.open(request)

# 7、获取请求返回的结果
content = response.read().decode('utf-8')
print(content)

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
```

## 3、解析

> 定向获取网页中的数据

### ①、xpath

> XPath，全称 XML Path Language，即 XML 路径语言，它是一门在 XML 文档中查找信息的语言。最初是用来搜寻 XML 文档的，但同样适用于 HTML 文档的搜索。所以在做爬虫时完全可以使用 XPath 做相应的信息抽取
>  
> XPath 的选择功能十分强大，它提供了非常简洁明了的路径选择表达式。另外，它还提供了超过 100 个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理等，几乎所有想要定位的节点都可以用 XPath 来选择。
>  
  官方文档：https://www.w3.org/TR/xpath/
>
> 感觉用处不是很大，因为浏览器呈现得页面是各种 js 和 ajax 处理之后的，但是 xpath 获得的是原始数据，少了很多东西

1. 安装 `lxml` 库

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230309150649.png)

2. 导入 lxml.etree：`from lxml import etree`
3. `etree.parse()` 解析本地文件：`html_tree = etree.parse('XX.html')`
4. `etree.HTML()` 服务器响应文件：`html_tree = etree.HTML(response.read().decode('utf‐8')`
5. `html_tree.xpath(xpath路径)`：处理数据
6. xpath 基本语法：https://www.runoob.com/xpath/xpath-syntax.html
7. https://www.jianshu.com/p/85a3004b5c06

#### Ⅰ、爬取文本

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/9 15:24
# @Author   : 月海
# @File     : _01_基本使用
# @Project  : 01_python

# 导包
from lxml import etree
import urllib.request

# 1、定义一个 url，就是要访问的地址
url = 'https://isaac.huijiwiki.com/wiki/%E4%BB%A5%E6%92%92%E7%9A%84%E7%BB%93%E5%90%88%EF%BC%9A%E5%BF%8F%E6%82%94'

# 2、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3、解析服务器响应文件
tree = etree.HTML(response.read().decode('utf8'))

# 4、操作数据；结果是集合 list
resultList: list = tree.xpath('//table[contains(@class, "wikitable")]//td//text()')

# 5、处理获取的数据
data = []
dataList = []
i = -1
while i < len(resultList) - 1:

    i += 1

    if resultList[i].find('。') > 0:
        data.append(resultList[i])
        dataList.append(data)
        data = []
        continue

    data.append(resultList[i])

# 6、遍历
for data in dataList: print(data)
```

#### Ⅱ、爬取图片

> 和爬图片并没有什么区别

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/10 14:03
# @Author   : 月海
# @File     : _02_下载图片
# @Project  : 01_python

# 导包
from lxml import etree
import urllib.request
import urllib.parse
import uuid

# 必应图片搜索

# 1、获取搜索词
search = input('请输入搜索内容：')

# 2、定义一个 url，就是要访问的地址
url = 'https://cn.bing.com/images/search?'

# 3 定义参数
data = {
    'q': search
}

# 4、转码：https://cn.bing.com/images/search?q=%E6%9C%88%E6%B5%B7
url = url + urllib.parse.urlencode(data)

# 下载网页（和浏览器显示的并不一样，要从这里获取数据）
# urllib.request.urlretrieve(url, './save/百度首页.html')
# 5、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 6、解析服务器响应文件
tree = etree.HTML(response.read().decode('utf8'))

# 7、操作数据；得到图片链接地址，结果是集合 list
resultList = tree.xpath('//ul[contains(@class, "dgControl_list ")]//img/@src')

# 8、下载图片
for result in resultList:
    urllib.request.urlretrieve(result, f'./save/{uuid.uuid4()}.jpg')
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230310152552.png)

### ②、JsonPath

### ③、BeautifulSoup

## 4、Selenium

### ①、简介

1. 什么是 selenium？
	1. Selenium 是一个用于 Web 应用程序测试的工具。
	2. Selenium 测试直接运行在浏览器中，就像真正的用户在操作一样。
	3. 支持通过各种 driver（FirfoxDriver，IternetExplorerDriver，OperaDriver，ChromeDriver）驱动真实浏览器完成测试。
	4. selenium 也是支持无界面浏览器操作的。
2. 为什么使用selenium？模拟浏览器功能，自动执行网页中的 js 代码，实现动态加载
3. 如何安装selenium？
	1. 操作谷歌浏览器驱动下载地址：http://chromedriver.storage.googleapis.com/index.html
	2. Egde 浏览器驱动下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
	3. 将会下载的驱动解压缩，然后移动到项目中
	4. 谷歌驱动和谷歌浏览器版本之间的映射表：http://blog.csdn.net/huilan_same/article/details/51896672
	5. 查看谷歌浏览器版本：谷歌浏览器右上角‐‐>帮助‐‐>关于
	6. pip install selenium

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2Fedgedriver_win64.zip)

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230313083559.png)

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230313084414.png)

4. selenium 的使用步骤？
	1. 导入：from selenium import webdriver
	2. 创建谷歌浏览器操作对象：
		1. path = 谷歌浏览器驱动文件路径
		2. browser = webdriver.Chrome(path)
	3. 访问网址：
		1. url = 要访问的网址
		2. browser.get(url)

### ②、selenium 的基本使用

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 8:52
# @Author   : 月海
# @File     : _01_基本使用
# @Project  : 01_python

# 1、导入
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 2、防止打开的浏览器自动关闭
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

# 3、创建浏览器操作对象
service = Service(executable_path='./edgedriver/msedgedriver.exe')
browser = webdriver.ChromiumEdge(service=service, options=option)

# 4、输入要访问的网址进行访问
browser.get('https://www.bilibili.com/')

# 5、获取网页数据
content = browser.page_source
print(content)
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230313092210.png)

### ③、元素定位

> https://micheng.blog.csdn.net/article/details/117136214
> 
> https://blog.csdn.net/qq_18298049/article/details/117194464

1. 选择器

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230313100305.png)

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230313100315.png)

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 9:28
# @Author   : 月海
# @File     : _02_元素定位
# @Project  : 01_python

# 1、导入
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 2、防止打开的浏览器自动关闭
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

# 3、创建浏览器操作对象
service = Service(executable_path='./edgedriver/msedgedriver.exe')
browser = webdriver.ChromiumEdge(service=service, options=option)

# 4、输入要访问的网址进行访问
browser.get('https://www.baidu.com/')

# 5.1、根据 id 获取对象
# content = browser.find_element(By.ID, 'su')
# print(content.get_attribute('value'))

# 5.2、根据 name 属性 获取对象
# content = browser.find_element(By.NAME, 'ie')
# print(content.get_attribute('value'))

# 5.3、通过 class name 定位；获取百度首页搜索框
# 需要注意的是，使用class name进行元素定位时，不能使用复合class name，要使用calss name定位此元素，只能使用其中的一个属性值进行定位而不是全部
# content = browser.find_element(By.CLASS_NAME, 's_ipt')
# print(content.get_attribute('id'))

# 5.4、通过 tag name 定位；所谓tag name，即元素标签名称，如input、p、a、button、span等
contentList = browser.find_elements(By.TAG_NAME, 'input')
for content in contentList:
    print(content.get_attribute('name'))

# 5.5、通过 link text 定位；
# 此定位方式使用完整匹配可见元素进行匹配，仅适用于链接元素定位，即<a href="www.xxx.com“>xxx这样的标签元素，其他元素不能使用，如百度首页的新闻、贴吧等链接元素可使用此方式进行定位

# 5.6、通过 partial link text 定位
# 此定位方式于link text一样，都只能作用于链接元素，也使用可见文本进行匹配，不同之处在于，link text表示可见文本必须于指定的文本完全一致，才能匹配成功，
# 而partial link text只要可见文本中包含指定的文本，则匹配成功，如上一个示例中的贴吧元素，也可以使用以下代码进行定位

# 5.7、通过 css selector 定位
# 当我们无法使用ID、name、class name等方式准确定位到元素时，
# css selector定位器有自己的语法，相比之前的定位方式使用上更加灵活也更加复杂，也更容易定位到一些之前的定位方式无法定位的元素

# 5.8、通过 xpath 定位
# Xpath 定位与 css 定位方式类似，不过官方更推荐使用 CSS 的方式进行定位，说 xpath 语法复制不利于调试，虽然灵活但是速度慢
```

2. 层级定位

```python
element = driver.find_element(By.ID, "wd")   # 先定位id为wd的元素
cheddar = element.find_element(By.ID, "brie")  # 在圈定的范围内定位元素
```

3. 相对定位
	1. above()：返回指定元素上方的元素
	2. below()：返回指定元素下方的元素
	3. toLeftOf()：返回指定元素左侧的元素
	4. toRightOf()：返回指定元素右侧的元素
	5. near()：返回指定元素附件的一个元素，要求该元素离指定元素不超过50px

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name

# above()：返回指定元素上方的元素
driver = webdriver.Edge()
password = driver.find_element(By.ID, "password")  # 通过id定位 密码输入框
emailAddress = driver.find_element(with_tag_name("input").above(password))   # 通过相对定位定位邮箱地址输入框

#  below()：返回指定元素下方的元素
driver = webdriver.Edge()
emailAddress = driver.find_element(By.ID, "email")
password = driver.find_element(with_tag_name("input").below(emailAddress))

# toLeftOf()：返回指定元素左侧的元素
driver = webdriver.Edge()
submitButton = driver.find_element(By.ID, "submit")
cancelButton = driver.find_element(with_tag_name("button").to_left_of(submitButton))

# toRightOf()：返回指定元素右侧的元素
driver = webdriver.Edge()
submitButton = driver.find_element(By.ID, "submit")
cancelButton = driver.find_element(with_tag_name("button").to_left_of(submitButton))

# near()：返回指定元素附件的一个元素，要求该元素离指定元素不超过50px
driver = webdriver.Edge()
submitButton = driver.find_element(By.ID, "submit")
cancelButton = driver.find_element(with_tag_name("button").to_left_of(submitButton))
```

### ④、元素信息

1. 获取元素属性：`get_attribute('属性名')`
2. 获取元素文本：`text`
3. 获取标签名：`tag_name`
4. 判断元素是否启用编辑状态：`is_enabled()`；如果元素是可编辑的，则返回true，如果元素不可编辑，则返回false，不可编辑的元素进行输入内容或选择内容将不成功
5. 判断元素是否显示在页面上：`is_displayed()`；有些元素在DOM中能够找到，但不一定显示在页面上，所谓显示在页面上，即可见，有宽度的，如果元素可见，返回true，如果不可见，返回false，如果使用click()操作不可见元素时，将抛出异常
6. 判断单选框或复选框的状态是否被选中：`isSelected()`；如果选中返回true，否则返回false

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 10:09
# @Author   : 月海
# @File     : _03_元素信息
# @Project  : 01_python

# 1、导入
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 2、防止打开的浏览器自动关闭
# option = webdriver.EdgeOptions()
# option.add_experimental_option("detach", True)

# 3、创建浏览器操作对象
service = Service(executable_path='./edgedriver/msedgedriver.exe')
browser = webdriver.ChromiumEdge(service=service)

# 4、输入要访问的网址进行访问
browser.get('https://www.baidu.com/')

# 5、根据 id 获取对象
content = browser.find_element(By.ID, 'su')

# 6.1、获取元素属性：get_attribute('属性名')
print(content.get_attribute('value'))

# 6.2、获取元素文本：text
print(content.text)

# 6.3、获取标签名：tag_name
print(content.tag_name)
```

### ⑤、交互

1. 打开指定的网页地址：`driver.get('https://www.baidu.com/')`
2. 获取当前页面 url：我们在测试过程中，有时需要获取当前页面的url以判断是否跳转到指定页面：`driver.current_url`
3. 返回按钮：`driver.back()`
4. 前进按钮：`driver.forward()`
5. 刷新页面：`driver.refresh()`
6. 获取当前页面title：`driver.title`
7. 窗口大小操作：
	1. 设置窗口大小：`driver.set_window_size(1920, 1080)`
	2. 最大化窗口：`driver.maximize_window()`
	3. 最小化窗口：`driver.minimize_window()`；最小化窗口是selenium4的新功能，selenium3不能使用此方法
	4. 全屏窗口，相当于大多数浏览器中按下F11：`driver.fullscreen_window()`
8. 退出：`driver.quit()`
9. 点击：`click()`
10. 输入：`send_keys()`
11. 清空输入框中的内容：`clear()`
12. 提交一些没有按钮可点击的输入框：`submit()`；比如我们在进行一些搜索时，输入文字后没有点击搜索的按钮，而是直接敲击enter键完成搜索，则可以使用 `submit()` 方法模拟此操作
13. 模拟 JS 滚动：

```python
js='document.documentElement.scrollTop=100000'
# 执行js代码
browser.execute_script(js) 
```

13. 获取网页代码：`page_source`
14. 显式等待、隐式等待与强制等待：https://micheng.blog.csdn.net/article/details/117264022
15. 切换窗口与iframe：https://micheng.blog.csdn.net/article/details/117303257

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 11:10
# @Author   : 月海
# @File     : _04_交互
# @Project  : 01_python

# 1、导入
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# 2、防止打开的浏览器自动关闭
# option = webdriver.EdgeOptions()
# option.add_experimental_option("detach", True)

# 3、创建浏览器操作对象
service = Service(executable_path='./edgedriver/msedgedriver.exe')
browser = webdriver.ChromiumEdge(service=service)

# 4、输入要访问的网址进行访问
browser.get('https://www.baidu.com/')

# 5、根据 id 获取对象：输入框，输入内容
browser.find_element(By.ID, 'kw').send_keys('月海')

# 6、点击搜索按钮 百度一下
browser.find_element(By.ID, 'su').click()

# 7、睡 2 秒
time.sleep(2)

# 8、获取搜索结果
contentList = browser.find_elements(By.XPATH, '//div[@id="content_left"]/div/div/div/h3/a')
for content in contentList:
    # print(content.get_attribute('href'))
    print('搜索结果：' + content.text)
    print('链接地址：' + content.get_attribute('href'))
    print()

# 9、关闭
browser.close()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe D:\Idea\save\python\0_study\01_python\11_爬虫\_03_selenium\_04_交互.py 
搜索结果：月海(月球月面上比较低洼的平原) - 百度百科
链接地址：http://www.baidu.com/link?url=aGzOMm36rSCGvs25y_LXdP8EGFDcevIBxkW4ZtihMEirHvNCZ0tYdTkxIGHFIFR2wNbIoOyxBPjxEnxkOkKWyer1R9JWt13DEALtEqVO6Nm

搜索结果：静海(月海) - 百度百科
链接地址：http://www.baidu.com/link?url=YLny4bT1Mbi-7JQ51XFSoG6Ogh4IZy7_rc1TWqOk9wZKW8Jf081Om-LWFUZzPVRi1uWicdGgKGnvccE3g0AtTzd6jHfSComCT7tVBOCC04q

搜索结果：月海 - 歌曲
链接地址：http://music.163.com/song?id=2013118207&market=baiduqk

搜索结果：太阳系 - 月海是什么?如何形成的?
链接地址：http://www.baidu.com/link?url=pRJMNXm9LZ5x22i6s1lzi90idq3JMkkgkO9QRbbsPx7EepP9pvYcmGWWyg3vPobEoQLzTyeA8q6j2rkQ2BQrkZ7uoC3DOVZ05rxn0BmNEm2CHOrfshsvAsKViNtYrPBM

搜索结果：月亮上的海是什么海?
链接地址：http://www.baidu.com/link?url=Nmxh_aixztczBn5IJ3EIFh_vycVoYQDWOdWpUP2yk_m2yXvdD6ZdhlGbE-yjYAjsNYXgAlEkO0qvx-8ZizoT928YDN6pdv4-q34CJEz8IFK

搜索结果：月球上的“月海”是什么? - 量子探索
链接地址：http://www.baidu.com/link?url=_vIf7Y8AwXQcxTd7ajY_Zkv4YbrkBchaonoZ1-S3VJr7bzjL0G45RX-9Z8l5v-HeJhFp25bE8GbjuEfeJ7GGUUuY5zHreTTGERXEyDI6ZGW

搜索结果：月海- QQ音乐-千万正版音乐海量无损曲库新歌热歌天天畅听...
链接地址：http://www.baidu.com/link?url=YLny4bT1Mbi-7JQ51XFSo475F_6SxEJN4MWovQDa9yeczvgEyCqNHjhQHfeUDdLBpzKmxEPEELmc0iaUVgd2Sq

搜索结果：月海_阿萨Aza_单曲在线试听_酷我音乐
链接地址：http://www.baidu.com/link?url=a-ZaN-S1ELWlPPmCVSRHqrVg2qCSCl-oWqQwrldeWb8D0-lWGedmTIZ_iKwWN-g3N7pbaK2y4GamPsGvgIxUGK


进程已结束,退出代码0
```

### ⑥、Phantomjs

1. Phantomjs 是一个无界面的浏览器
2. 支持页面元素查找，js 的执行等
3. 由于不进行 css 和 gui 渲染，运行效率要比真实的浏览器要快很多
4. 不过 Phantomjs 基本被淘汰了，现在一般使用 Chrome handless

### ⑦、Chrome handless

1. Chrome-headless 模式， Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致
2. 系统要求：
	1. Chrome：
		1. `Unix\Linux` 系统需要 chrome >= 59
		2. Windows 系统需要 chrome >= 60
	2. Python3.6
	3. `Selenium==3.4.*`
	4. `ChromeDriver==2.31`
3. 我这里用的还是 Egde

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 13:06
# @Author   : 月海
# @File     : _05_Chrome handless
# @Project  : 01_python

# 1、导入
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# 2、定义一个option对象，实现无可视化界面的操作
options = webdriver.EdgeOptions()
options.add_argument("headless")
options.add_argument('‐‐disable‐gpu')

# 3、创建浏览器操作对象，依然还是使用 msedgedriver；
# 若是使用谷歌浏览器的话，有自带的 headless 模式
service = Service(executable_path='./edgedriver/msedgedriver.exe')
browser = webdriver.Edge(service=service, options=options)

# 4、输入要访问的网址进行访问
browser.get('https://www.baidu.com/')

# 5、根据 id 获取对象：输入框，输入内容
browser.find_element(By.ID, 'kw').send_keys('月海')

# 6、点击搜索按钮 百度一下
browser.find_element(By.ID, 'su').click()

# 7、睡 2 秒
time.sleep(2)

# 8、获取搜索结果
contentList = browser.find_elements(By.XPATH, '//div[@id="content_left"]/div/div/div/h3/a')
for content in contentList:
    # print(content.get_attribute('href'))
    print('搜索结果：' + content.text)
    print('链接地址：' + content.get_attribute('href'))
    print()

# 9、保存快照
browser.save_screenshot('./save/save.png')

# 10、关闭
browser.close()
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\11_爬虫\_03_selenium\_05_Chrome handless.py" 
搜索结果：月海(月球月面上比较低洼的平原) - 百度百科
链接地址：http://www.baidu.com/link?url=DbJqNhSpggbOBUedS-S-TpFOSdkjL0xjons-_NxWlyrzpmQdEXgF4QaGxGhjA70HIZTSHKTmMTGas_GugQWIIjpgRR69b4KrTs5fJHRMT3S

搜索结果：静海(月海) - 百度百科
链接地址：http://www.baidu.com/link?url=HVIgxie1yny2myEnyxcTh0mqc8uuINrm3jX0Lu1HuE-9V0Nu1W-heWlwOL-UEIofhUZ7xNIBsJQglJQcmpQCq0FzNrkdV9WnJF1-V9928qW

搜索结果：月海 - 歌曲
链接地址：http://music.163.com/song?id=2013118207&market=baiduqk

搜索结果：太阳系 - 月海是什么?如何形成的?
链接地址：http://www.baidu.com/link?url=fIXbIYsH-G_mYmL9GIuVN4AS0QTKVqWPzFPTtYHwEZIaw7SE4sePFPUxBYdbViht5BQzO4sD0bKptQBIbojCz9ZUNnCQQQlGYUyyBMvHzc1KBFc8jfZUdu33YiEjSTZr

搜索结果：月亮上的海是什么海?
链接地址：http://www.baidu.com/link?url=pkSi6An40TqjICBbkTcb4chr5IBYHLhZ-JNMnwjwZHRgWXZhGwFL30hECBEQLW4ENVcfxsOAld9yVlMdBYWlJ65xk9DlnOAimH8Rnt6ejd3

搜索结果：月球上的“月海”是什么? - 量子探索
链接地址：http://www.baidu.com/link?url=thAaa_bwcbA_JN34hjE5jEUzeJoMe8vIVpgNsiuTnlVm9z9TizHGdDXnS22ifMENDEqZgu7X18bSYvCI6YDJHQcPI1W4L0qrXN4AGCyEAny

搜索结果：月海- QQ音乐-千万正版音乐海量无损曲库新歌热歌天天畅听...
链接地址：http://www.baidu.com/link?url=HVIgxie1yny2myEnyxcThIn8CuTZYAricWPoA2XxSFRzf-7NBudC8jg8ttfGHqEsCUnql-B1CFqAuBiQXg4YOq

搜索结果：月海_阿萨Aza_单曲在线试听_酷我音乐
链接地址：http://www.baidu.com/link?url=xj9FHRO_saLMhwcRtEifyq8KDw3f9p20c3fsUvi7XL9swpaDjSAPiLEKLuZAdhq05Lk8zGhF3gjMcbGsA5GMPK


进程已结束,退出代码0
```

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2Fsave.png)

## 5、requests

### ①、基本使用
> 官方文档：http://cn.python‐requests.org/zh_CN/latest/
> 
> 快速上手：http://cn.python‐requests.org/zh_CN/latest/user/quickstart.html

1. 安装：`pip install requests`
2. response 的属性以及类型
	1. 类型 ：`models.Response`
	2. `r.text` : 获取网站源码
	3. `r.encoding` ：访问或定制编码方式
	4. `r.url` ：获取请求的url
	5. `r.conten`t ：响应的字节类型
	6. `r.status_code` ：响应的状态码
	7. `r.headers` ：响应的头信息

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 13:49
# @Author   : 月海
# @File     : _01_基本使用
# @Project  : 01_python

# 导包
import requests

# 1、定义 url，创建 requests 对象
url = 'https://www.baidu.com/'
requests = requests.get(url)

# 2、response的属性以及类型
# 类型 ：<class 'requests.models.Response'>
print(type(requests))

# r.encoding ：访问或定制编码方式
requests.encoding = 'utf-8'

# r.text : 获取网站源码
print(requests.text)

# r.url ：获取请求的url
print(requests.url)

# r.content ：响应的字节类型，返回二进制数据
print(requests.content)

# r.status_code ：响应的状态码
print(requests.status_code)

# r.headers ：响应的头信息
print(requests.headers)
```

### ②、get 请求

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 14:06
# @Author   : 月海
# @File     : _02_get 请求
# @Project  : 01_python

# 导包
import requests

# 1、定义 url，创建 requests 对象
url = 'http://127.0.0.1:9000/Test/get'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
}

# 3、参数
data = {
    'wd': '月海'
}

# 4、发送 get 请求
requests = requests.get(url=url, params=data, headers=headers)

# 5、设置编码
requests.encoding = 'utf-8'

# 6、获取网站源码
print(requests.text)
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\11_爬虫\_04_requests\_02_get 请求.py" 
{"msg":"ok","data":[{"id":"001","name":"月海"},{"id":"002","name":"言"},{"id":"003","name":"羽"}],"code":0}

进程已结束,退出代码0
```

### ③、post 请求

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 14:28
# @Author   : 月海
# @File     : _03_post 请求
# @Project  : 01_python

# 导包
import requests

# 1、定义 url，创建 requests 对象
url = 'http://127.0.0.1:9000/Test/post'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
}

# 3、参数
data = {
    'name': '月海'
}

# 4、发送 post 请求
requests = requests.post(url=url, data=data, headers=headers)

# 5、设置编码
requests.encoding = 'utf-8'

# 6、获取网站源码
print(requests.text)
```

```python
D:\Idea\save\python\0_study\01_python\venv\Scripts\python.exe "D:\Idea\save\python\0_study\01_python\11_爬虫\_04_requests\_03_post 请求.py" 
{"msg":"ok","data":"name：月海","code":0}

进程已结束,退出代码0
```

### ④、代理

```python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/13 14:46
# @Author   : 月海
# @File     : _04_代理
# @Project  : 01_python

# 导包
import requests

# 1、定义 url，创建 requests 对象
url = 'http://127.0.0.1:9000/Test/post'

# 2、定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
}

# 3、参数
data = {
    'name': '月海'
}

# 设置代理服务器
proxy = {
    'http': '218.7.171.91:3128'
}

# 4、发送 post 请求
requests = requests.post(url=url, data=data, headers=headers, proxies=proxy)

# 5、设置编码
requests.encoding = 'utf-8'

# 6、获取网站源码
print(requests.text)
```

### ⑤、cookie 定制

> https://www.bilibili.com/video/BV1Db4y1m7Ho/?p=88

## 6、scrapy

> Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2F05.scrapy.pdf)

# 十二、

# 十三、

# 十四

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、第三方包
## 1、数据可视化 pyecharts
> Echarts 是个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可. 而 Python 是门富有表达力的语言，很适合用于数据处理，当数据分析遇上数据可视化时 pyecharts 诞生了
> 
> 需安装包：pyecharts

### ①、折线图

1. 编写代码并执行

```python
# @Time     : 2023/3/7 11:04
# @Author   : 月海
# @File     : 01_折线图
# @Project  : 01_python

# 导包
from pyecharts.charts import Line

# 得到折线图对象
line = Line()

# 添加 x 轴数据
line.add_xaxis(['中国', '美国', '英国'])
# 添加 y 轴数据
line.add_yaxis('GDP', [30, 20, 10])

# 生成图表
line.render()
```

2. 执行后会生成一个 html 文件

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307111043.png)

3. 在浏览器中打开：

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2Fpython%2Fattachments%2FPasted%20image%2020230307111123.png)

### ②、地图

### ③、动态展示柱状图

## 2、Python 操作 MySql

1. 安装库：pymysql
2. 使用 python 操作数据库

```python
# @Time     : 2023/3/7 14:58
# @Author   : 月海
# @File     : _01_连接使用 mysql
# @Project  : 01_python

# 引入包
from pymysql import Connection

# 获取到 mysql 数据库的连接对象
conn = Connection(
    host='43.138.106.181',
    port=3306,
    user='root',
    password='000123'
)

# 选择数据库
conn.select_db('nacos-config')
# 获取游标对象
curses = conn.cursor()
# 执行 sql 语句
curses.execute('select * from config_info')

# 获取查询结果
# 游标对象使用 fetchall() 方法，得到的是全部的查询结果，是一个元组这个元组内部嵌套了元组，嵌套的元组就是一行查询结果
for result in curses.fetchall():
    print(result)

# 关闭数据库连接
conn.close()
```

3. 结果

```python
C:\Users\10222148\AppData\Local\Programs\Python\Python311\python.exe "D:\Idea\save\python\0_study\01_python\07_MySql\_01_连接使用 mysql.py" 
(1, 'test.yml', 'DEFAULT_GROUP', 'name: yuehai', 'cbdac6284f640be3c9425318d7954653', datetime.datetime(2023, 3, 2, 5, 45, 32), datetime.datetime(2023, 3, 2, 5, 45, 32), None, '218.58.71.195', '', '', '测试', None, None, 'yaml', None)
(4, 'nacos-config-client-info.yaml', 'DEFAULT_GROUP', 'name: yuehai-nginx-nacos', 'a33ad50b50db2c5c0fb58ad090bb70d1', datetime.datetime(2023, 3, 3, 2, 27, 17), datetime.datetime(2023, 3, 3, 2, 27, 17), None, '43.138.106.181', '', '', None, None, None, 'yaml', None)

进程已结束,退出代码0
```

## 3、

## 4、




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

### ⑪、⑫、⑬、⑭、⑮、⑯、⑰、⑱、⑲、⑳

### ㉑、㉒、㉓、㉔、㉕、㉖、㉗、㉘、㉙、㉚

### ㉛、㉜、㉝、㉞、㉟、㊱、㊲、㊳、㊴、㊵

### ㊶、㊷、㊸、㊹、㊺、㊻、㊼、㊽、㊾、㊿

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