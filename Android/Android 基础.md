> https://www.bilibili.com/video/BV19U4y1R7zV/
> 
> IDE：idea
> 
> JDK 11
> 
> Android Minimum SDK：API 28: Android 9.0(Pie)

# 一、开发环境搭建

## 1、安装 `java 11`

1. 查看版本：`java -version`
2. 不用安装了，这次是学的 `Kotlin`

## 2、安装 `gradle`

1. https://gradle.org/releases/ ，我使用的版本是 6.9.4，下载二进制压缩包
2. 解压到随意目录

![](attachments/Pasted%20image%2020230412081122.png)

3. 右键点击此电脑，点击属性 -> 高级系统配置 -> 环境变量 -> 新建变量名：`GRADLE_HOME`

![](attachments/Pasted%20image%2020230412081307.png)

4. 点击 path -> 编辑 -> 新建：`%GRADLE_HOME%\bin`
5. cmd 中 输入指令查看：`gradle -v`

![](attachments/Pasted%20image%2020230412081639.png)

## 3、创建工程，下载配置 Android SDK

> <font color="#ff0000">注意此处下载的是 Android 9.0</font>

1. 下载 Android SDK
2. 选择模板 -> Phone and Tablet -> Empty Activity

![](attachments/Pasted%20image%2020230411125712.png)

3. 填写项目信息，语言选择 Java

![](attachments/Pasted%20image%2020230411130003.png)

4. 安装组件，创建项目

![](attachments/Pasted%20image%2020230411130522.png)

5. 右键点击此电脑，点击属性 -> 高级系统配置 -> 环境变量 -> 新建变量名：`ANDROID_HOME`

![](attachments/Pasted%20image%2020230412083241.png)

6. 点击 path -> 编辑 -> 新建：
	1. `%ANDROID_HOME%\tools`
	2. `%ANDROID_HOME%\platform-tools`
	3. `%ANDROID_HOME%\build-tools\33.0.2`
7. cmd 中 输入指令查看：`android -h`

![](attachments/Pasted%20image%2020230412083652.png)

## 4、IDEA Android SDK 配置

1. idea 设置 -> 外观与行为 -> 系统设置 -> Android SDK，选择和之前下载的 SDK 对应的版本，点击应用进行下载

![](attachments/Pasted%20image%2020230412083946.png)

2. 没有报错即可，点击完成，然后点击应用确定

![](attachments/Pasted%20image%2020230412084212.png)

## 5、IDEA gradle 配置

1. idea 设置 -> 构建、执行、部署 -> 构建工具 -> Gradle

![](attachments/Pasted%20image%2020230412084422.png)

## 6、项目结构配置

1. 点击设置 -> 项目结构
2. 点击 SDK，将安卓 SDK 的 Build target 的版本改为 28，java 版本改为 11

![](attachments/Pasted%20image%2020230412084803.png)

3. 选择项目，选择刚才配置的 SDK

![](attachments/Pasted%20image%2020230412084903.png)

## 7、创建内置模拟器

1. 点击右侧 Device Manager

![](attachments/Pasted%20image%2020230411132603.png)

2. 点击 Create device

![](attachments/Pasted%20image%2020230411132803.png)

3. 选择安卓参数，点击右侧 Clone Device

![](attachments/Pasted%20image%2020230412090555.png)

4. 选择一个主题，点击完成，然后点击下一步

![](attachments/Pasted%20image%2020230412090708.png)

5. 下载镜像，选择安卓 9，下载完成后点击下一步，然后点击完成

![](attachments/Pasted%20image%2020230412090846.png)

6. 启动模拟器

![](attachments/Pasted%20image%2020230411134030.png)

7. 要是还不行，报错：

```
04/12 11:06:28: Launching 'app' on Pixel 2 (Edited) 9 API 28.
Installation did not succeed.
The application could not be installed.

List of apks:
[0] 'D:\Idea\save\android\00_Android\app\build\intermediates\apk\debug\app-debug.apk'
Installation failed due to: 'Connection refused: connect'
Retry
Failed to launch an application on all devices

```

8. 我怀疑是电脑问题，连我自己手机开发了

## 8、Android 开发涉及的语言

1. App 开发主要有两大技术路线，分别是原生开发和混合开发。
2. Android 的官方编程语言包括 `Java` 和 `Kotlin`。

![](attachments/Pasted%20image%2020230411134942.png)

3. 除此之外还有 `c++(NDK)` 和 `xml` 等

## 9、项目结构

> https://blog.csdn.net/xqy3177563/article/details/90142446

# 二、`Kotlin` 基础语法

## 1、包声明

1. 代码文件的开头一般为包的声明：

```Kotlin
// 包
package com.runoob.main

// 库
import java.util.*

// 方法
fun test() {}

// 
class Runoob {}
```

2. kotlin 源文件不需要相匹配的目录和包，源文件可以放在任何文件目录。
3. 以上例中 test() 的全名是 com.runoob.main.test、Runoob 的全名是 com.runoob.main.Runoob。
4. 如果没有指定包，默认为 default 包。

## 2、默认导入

1. 默认导入

```Kotlin
kotlin.*
kotlin.annotation.*
kotlin.collections.*
kotlin.comparisons.*
kotlin.io.*
kotlin.ranges.*
kotlin.sequences.*
kotlin.text.*
```

## 3、`Unit`、`Any` 和 `Nothing`

### ①、`Unit`

1. 首先 `Unit` 本身是一个用 `object` 表示的单例，所以可以理解为 Kotlin 有一个类，这个类只有一个单例对象，叫 `Unit` 。
2. 这个类型类似于 Java 中的 `Void` 。
3. 由于在 Kotlin 中，一切方法/函数都是表达式，表达式是总是有值的，所以每一个方法都必有一个返回值。如果没有用 `return` 明确的指定，那么一般来说就会用自动帮我们加上 `Unit`，等同于这样：

```Kotlin
fun returnUnit():Unit{
    return Unit
}
```

4. 返回值类型为 `Unit`，实际返回了 `Unit` 的单例对象 `Unit`

### ②、`Any`

1. 根据注释，`Any` 其实就跟 Java 里的 `Object` 是一样的，也就是说在 Kotlin 中 `Any` 取代了 Java 中的 `Object`，成为了 Kotlin 中所有类的父类。
2. 不过这个说法还不是很严谨，因为 Any 是不可为空的，而 Kotlin 中还有一个 `Any?`，是指可空的 Any 。
3. 显而易见， `Any?` 是 `Any` 的父类，那么严格来说， `Any?` 是所有类的父类， `Any` 只是所有不可为空的类（也就是没有?）的父类。

### ③、`Nothing`

1. `Nothing` 是最难理解的一个概念，不同于 `Unit` 至于 `Void` ，`Any` 之于 `Object` ， `Nothing` 在 Java 中并没有一个相似的概念。 `Nothing` 的定义如下：

```Kotlin
package kotlin

/**
 * Nothing has no instances. You can use Nothing to represent "a value that never exists": for example,
 * if a function has the return type of Nothing, it means that it never returns (always throws an exception).
 */
public class Nothing private constructor()
```

2. `Nothing` 是一个类，这个类构造器是私有的，也就是说我们从外面是无法构造一个 `Nothing` 对象的。前面说每一个方法都有返回值，且返回值至少也是一个 `Unit`，这是对正常方法来说的。
3. 如果一个方法的返回类型定义为 `Nothing` ，那么这个方法就是无法正常返回的。可以这么理解，Koltin 中一切方法都是表达式，也就是都有返回值，那么正常方法返回 `Unit` ，无法正常返回的方法就返回 `Nothing` 。举个例子，定义如下两个方法：

```Kotlin
fun test1():Nothing{
    while (true){}
}

fun test2():Nothing{
    while (false){}
}
```

4. `test1()` 方法是可以编译通过的，但是执行的时候程序会一直陷入循环中无法正常返回；
5. `test2()` 乍一看执行的时候可以正常返回，但是因为返回类型定义为了 `Nothing` ，这句矛盾了，都说好了不能正常返回（定义返回类型为 `Nothing` ），结果你方法内部逻辑没问题，给我返回了，那就有问题了，所以他其实是编译不通过的，其实也很好理解：我需要返回一个 `Nothing` 类的对象，但是因为 `Nothing` 类不是 `open` 的，且构造器为私有的，所以没法返回一个他的对象。
6. 怎么让他编译通过呢？可以抛一个异常：

```Kotlin
fun test2():Nothing{
    while (false){}
    throw Exception()
}
```

7. 好了，现在我因为抛了一个异常，所以还是没法正常返回，那么我声明返回类型为 `Nothing` 也就没问题了
8. 类似的用法，比如Kotlin中有一个方法 TODO ：

```Kotlin
fun test3(){
    TODO()
}

@kotlin.internal.InlineOnly
public inline fun TODO(): Nothing = throw NotImplementedError()
```

9. 因为要抛异常，注定无法正常返回，所以返回 Nothing 类型。而 test3() 方法返回值类型应该是默认的 Unit ，或者其他自己定义的返回类型，但实际上因为调用了 TODO() ，所以返回了一个 Nothing （并没有正常返回），这样编译是可以通过的，为什么呢？
10. 有一些文章是把 Nothing 当做其他所有类的子类来理解的，也就是说 Nothing 是其他类的子类，所以返回其他类的地方可以用一个返回 Nothing 来代替，这样理解也是没问题的。
11. 但是就有疑问了，Kotlin&Java 不是单继承的吗？如果 Nothing 是所有类的子类，那不就是多继承了？其实这里有一个概念，我也是最近在 《Kotlin 核心编程》中学到。其实“继承”和“子类化”是两个概念，我们说类A 继承了类 B，即 A extends B，是强调 B 中的一些实现，可以在 A 中复用；而说类 A 是类 B 的子类，是强调在需要类 B 的地方可以用类 A 代替。两者的角度不一样。
12. 单继承，指的是从继承的角度上，一切类的顶级父类都是 Any (Java中是 Object )，那么大家都可以复用父类的现有实现。
13. 而子类化，则是在所有需要用到父类的地方可以代替，比如一个方法我需要返回一个 Any，那么我实际上返回一个 Int 对象，也是没问题的。
14. 所以说，Nothing 可以代替原方法的返回类型，是从子类化的角度，因为可代替，所以 Nothing 是所有类的子类，这和单继承是没冲突的。参照这个说法，Kotlin中还有一个 emptyList :

```Kotlin
/**
 * Returns an empty read-only list.  The returned list is serializable (JVM).
 * @sample samples.collections.Collections.Lists.emptyReadOnlyList
 */
public fun <T> emptyList(): List<T> = EmptyList

internal object EmptyList : List<Nothing>...
```

15. 因为 `Nothing` 是其他类型的子类，所以按照泛型的协变，`emptyList` 就可以代替需要 `List<T>` 的地方了。

## 4、变量定义

1. 变量：`var`
2. 常量：`val`

```Kotlin
package com.yuehai.kotlin._01_variable

/**
@author 月海
@create 2023/4/12 16:16
 */
class _01_variable {
	
	// 变量：var
	var myInt:Int = 123;
	
	// 常量：val
	val myInt2:Int = 12345;
}
```

3. 可以使用 `is` 运算符检测一个表达式是否某类型的一个实例(类似于 Java 中的 `instanceof` 关键字)。

## 5、`NULL` 检查机制

1. Kotlin 的空安全设计对于声明可为空的参数，在使用时要进行空判断处理
2. 字段后加 `!!` 像 Java 一样抛出空异常
3. 另一种字段后加 `?` 可不做处理返回值为 `null` 
4. 配合 `?:` 做空判断处理

```Kotlin
// 类型后面加?表示可为空
var age: String? = "23" 

// 抛出空指针异常
val ages = age!!.toInt()

// 不做处理返回 null
val ages1 = age?.toInt()

// 做处理，age 为空返回-1
val ages2 = age?.toInt() ?: -1
```

3. 当一个引用可能为 `null` 值时，对应的类型声明必须明确地标记为可为 `null`。当 `str` 中的字符串内容不是一个整数时, 返回 null：

```Kotlin
fun parseInt(str: String): Int? {
  // ...
}
```

## 6、区间

1. 区间表达式由具有操作符形式 `..` 的 `rangeTo` 函数辅以 `in` 和 `!in` 形成。
	1. `in` ：存在
	2. `!in` 不存在
2. 区间是为任何可比较类型定义的，但对于整型原生类型，它有一个优化的实现。以下是使用区间的一些示例：

```Kotlin
for (i in 1..4) print(i) // 输出“1234”

for (i in 4..1) print(i) // 什么都不输出

if (i in 1..10) { // 等同于 1 <= i && i <= 10
    println(i)
}

// 使用 step 指定步长
for (i in 1..4 step 2) print(i) // 输出“13”

for (i in 4 downTo 1 step 2) print(i) // 输出“42”


// 使用 until 函数排除结束元素
for (i in 1 until 10) {   // i in [1, 10) 排除了 10
     println(i)
}
```

## 7、条件控制

### ①、`if`

1. 与 java 中类似

```Kotlin
package com.yuehai.kotlin._02_BasicGrammar

import org.junit.Test

/**
@author 月海
@create 2023/4/13 13:10
 */
class _07_01_if {
	@Test
	fun myFun(){
		val num:Int = 10
		
		// 1、单条件判断
		if (num === 10){
			println("单条件判断：num = 10")
		}
		
		// 2、多条件判断
		if (num > 10){
			println("多条件判断：num > 10")
		}else if (num < 10){
			println("多条件判断：num < 10")
		}else{
			println("多条件判断：num = 10")
		}
		
		// 3、作为表达式，把 IF 表达式的结果赋值给一个变量
		// 这也说明我也不需要像Java那种有一个三元操作符，因为我们可以使用它来简单实现
		val a:Int = 1
		val b:Int = 2
		val c = if (a > b){
			println("a 比较大")
			a
		}else if (a < b){
			println("b 比较大")
			b
		}else{
			println("一样大")
			0
		}
		println(c)
	
		// 4、使用 in 运算符来检测某个数字是否在指定区间内，区间格式为 x..y ：
		if (num in 1..100){
			println("变量 num 的值在 1 - 100 的区间内")
		}
	
	}
}
```

```Kotlin
单条件判断：num = 10
多条件判断：num = 10
b 比较大
2
变量 num 的值在 1 - 100 的区间内

进程已结束,退出代码0

```

### ②、`when`

1. when 将它的参数和所有的分支条件顺序比较，直到某个分支满足条件。
2. when 既可以被当做表达式使用也可以被当做语句使用。
3. 如果它被当做表达式，符合条件的分支的值就是整个表达式的值；如果当做语句使用， 则忽略个别分支的值。
4. when 类似其他语言的 switch 操作符

```Kotlin
package com.yuehai.kotlin._02_BasicGrammar

import org.junit.Test

/**
@author 月海
@create 2023/4/13 13:23
 */
class _07_02_when {
	@Test
	fun myFun(){
		val num:Int = 10
		
		// 1、when 类似其他语言的 switch 操作符。其最简单的形式如下：
		// 在 when 中，else 同 switch 的 default。如果其他分支都不满足条件将会求值 else 分支。
		when(num){
			1 -> println("变量 num 的值是 1")
			10 -> println("变量 num 的值是 10")
			100 -> {
				println("变量 num 的值是 100")
			}
			else -> {
				println("变量 num 的值不是 1、10、100")
			}
		}
		
		// 2、如果很多分支需要用相同的方式处理，则可以把多个分支条件放在一起，用逗号分隔
		when(num){
			1, 10, 100 -> {
				println("变量 num 的值是 $num")
			}
			else -> {
				println("变量 num 的值不是 1、10、100")
			}
		}
		
		// 3、我们也可以检测一个值在（in）或者不在（!in）一个区间或者集合中
		when(num){
			in 1..10 -> println("变量 num 的值在 1 - 10 的区间内")
			in 10..100 -> println("变量 num 的值在 10 - 100 的区间内")
			else -> println("变量 num 的值不在 1 - 100 的区间内")
		}
		
		// 4、另一种可能性是检测一个值是（is）或者不是（!is）一个特定类型的值。
		// 注意： 由于智能转换，你可以访问该类型的方法和属性而无需 任何额外的检测。
		fun isType(x: Any) = when(x) {
			is String -> println("传入的变量类型是字符串")
			is Int -> println("传入的变量类型是整形")
			else -> false
		}
		isType("月海")
		
	}
}
```

```Kotlin
变量 num 的值是 10
变量 num 的值是 10
变量 num 的值在 1 - 10 的区间内
传入的变量类型是字符串

进程已结束,退出代码0
```

## 8、循环控制

### ①、`return`、`Break` 和 `Continue` 标签

1. Kotlin 有三种结构化跳转表达式：
	1. `return`：默认从最直接包围它的函数或者匿名函数返回。
	2. `break`：终止最直接包围它的循环。
	3. `continue`：终止本次、继续下一次最直接包围它的循环。
2. 在 Kotlin 中任何表达式都可以用标签 `label` 来标记。 标签的格式为标识符后跟 `@` 符号，例如：`abc@`、`fooBar@` 都是有效的标签。 要为一个表达式加标签，我们只要在其前加标签即可：

```Kotlin
// 在表达式前使用标签标记
loop@ for (i in 1..100) {
    // ……
}

// 现在，我们可以用标签限制 break 或者continue 来跳出指定标签的语句
loop@ for (i in 1..100) {
    for (j in 1..100) {
        if (……) break@loop
    }
}
```

3. 标签限制的 `break` 跳转到刚好位于该标签指定的循环后面的执行点。 continue 继续标签指定的循环的下一次迭代。

### ②、`for`

1. `for` 循环可以对任何提供迭代器（`iterator`）的对象进行遍历

```Kotlin
package com.yuehai.kotlin._02_BasicGrammar

import org.junit.Test

/**
@author 月海
@create 2023/4/13 13:55
 */
class _08_02_for {
	@Test
	fun myFun(){
		// 创建一个集合
		val list:List<Int> = mutableListOf<Int>(5,1,4,7,8,2)
		
		// 1、for 循环可以对任何提供迭代器（`iterator`）的对象进行遍历
		println("---- 直接遍历 ----------------")
		for (i in list) {
			println(i)
		}
		
		// 2、通过索引进行遍历；这种"在区间上遍历"会编译成优化的实现而不会创建额外对象
		println("---- 通过索引进行遍历 ----------------")
		for (index in list.indices) {
			println(list[index])
		}
		
		// 3、使用库函数 withIndex，直接获得 值 和 索引
		println("---- 使用库函数 withIndex 遍历 ----------------")
		for ( (index, value) in list.withIndex()) {
			println("索引为：$index，值为：$value")
		}
		
		// 4、lambda 表达式
		println("---- lambda 表达式 ----------------")
		list.forEach { l -> println(l) }
	}
}
```

```Kotlin
---- 直接遍历 ----------------
5
1
4
7
8
2
---- 通过索引进行遍历 ----------------
5
1
4
7
8
2
---- 使用库函数 withIndex 遍历 ----------------
索引为：0，值为：5
索引为：1，值为：1
索引为：2，值为：4
索引为：3，值为：7
索引为：4，值为：8
索引为：5，值为：2
---- lambda 表达式 ----------------
5
1
4
7
8
2

进程已结束,退出代码0
```

### ③、`while` 与 `do...while` 循环

1. 对于 `while` 语句而言，如果不满足条件，则不能进入循环。
2. `do…while` 循环和 `while` 循环相似，不同的是，`do…while` 循环至少会执行一次

```Kotlin
package com.yuehai.kotlin._02_BasicGrammar

import org.junit.Test

/**
@author 月海
@create 2023/4/13 16:18
 */
class _08_03_while {
	@Test
	fun myFun(){
		// 创建一个集合
		val list:List<Int> = mutableListOf<Int>(5,1,4,7,8,2)
		// 创建集合的迭代器
		val iterator = list.iterator();
		
		// 1、对于 while 语句而言，如果不满足条件，则不能进入循环。
		// 迭代器
		println("---- 迭代器遍历 ----------------")
		while (iterator.hasNext()){
			println(iterator.next())
		}
		
		// 2、do…while 循环和 while 循环相似，不同的是，do…while 循环至少会执行一次
		// 普通遍历集合
		println("---- 普通遍历集合 ----------------")
		var i:Int = 0
		do {
			println(list[i])
			i ++;
		}while (i < list.size)
	
	}
}
```

```Kotlin
---- 迭代器遍历 ----------------
5
1
4
7
8
2
---- 普通遍历集合 ----------------
5
1
4
7
8
2

进程已结束,退出代码
```

# 三、`Kotlin` 基本数据类型

## 1、基本数据类型

1. Kotlin 的基本数值类型包括 `Byte`、`Short`、`Int`、`Long`、`Float`、`Double` 等。不同于 Java 的是，字符不属于数值类型，是一个独立的数据类型。

| 类型    | 名称   | 位宽度 | Java基本数据类型 | 说明                                                                                                                                                                                                                         |
| ------- | ------ | ------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean | 布尔型 |        | boolean          | 它有两个值：true 和 false                                                                                                                                                                                                    |
| Char    | 字符型 |        | byte             | 和 Java 不一样，Kotlin 中的 Char 不能直接和数字操作<br>Char 必需是单引号 `'` 包含起来的。比如普通字符 `'0'`，`'a'`；字符字面值用单引号括起来: '1'<br>特殊字符可以用反斜杠转义。 <br>支持这几个转义序列：`\t、 \b、\n、\r、\'、\"、\\ 和 \$`。 编码其他字符要用 Unicode 转义序列语法：`'\uFF00`'。 |
| Byte    | 字节型 | 8      | byte             | 最大 127，最小 -128                                                                                                                                                                                                          |
| Short   | 短整型 | 16     | short            | 最大 32767，最小 -32768                                                                                                                                                                                                      |
| Int     | 整型   | 32     | int              | 最小值是 -2,147,483,648（-2^31）；最大值是 2,147,483,647（2^31 - 1）                                                                                                                                                         |
| Long    | 长整型 | 64     | int              | 最小值是 -9,223,372,036,854,775,808（-2^63）；最大值是 9,223,372,036,854,775,807（2^63 -1）；                                                                                                                                |
| Float   | 长整型 | 32     | float            | 最多 6 位小数，超过的会四舍五入                                                                                                                                                                                              |
| Double  | 长整型 | 64     | float            | 最多 12 位小数，超过的会四舍五入                                                                                                                                                                                             |

```Kotlin
package com.yuehai.kotlin._02_DataType

import org.junit.Test

/**
@author 月海
@create 2023/4/12 15:43

基本数据类型
 */
class _01_BasicDataType {

    @Test
    fun basicDataType(){

        // Boolea
        val myBoolean:Boolean = true;
        println(myBoolean)
        
        // Char
        // Char 必需是单引号 ' 包含起来的。比如普通字符 '0'，'a'；字符字面值用单引号括起来: '1'。
        val myChar:Char = '0';
        // 特殊字符可以用反斜杠转义。 支持这几个转义序列：\t、 \b、\n、\r、\'、\"、\\ 和 \$。 编码其他字符要用 Unicode 转义序列语法：'\uFF00'。
        val myChar2 = '\$';
        println("$myChar，$myChar2")
        
        // Byte；最大 127，最小 -128
        val myByte:Byte = 127;
        println(myByte)
        
        // Short；最大 32767，最小 -32768
        val myShot:Short = 128;
        println(myShot)
        
        // Int；最小值是 -2,147,483,648（-2^31）；最大值是 2,147,483,647（2^31 - 1）
        val myInt:Int = 123456;
        println(myInt)
        
        // Long；最小值是 -9,223,372,036,854,775,808（-2^63）；最大值是 9,223,372,036,854,775,807（2^63 -1）；
        val myLong:Long = 12345678910
        println(myLong)
        
        // Float；最多 6 位小数，超过的会四舍五入
        val myFloat:Float = 553.1614F;
        println(myFloat)
        
        // Double；最多 12 位小数，超过的会四舍五入
        val myDouble:Double = 553.161413121;
        println(myDouble)
    }

}
```

## 2、比较两个数字

1. Kotlin 中没有基础数据类型，只有封装的数字类型，你每定义的一个变量，其实 Kotlin 帮你封装了一个对象，这样可以保证不会出现空指针。数字类型也一样，所以在比较两个数字的时候，就有比较数据大小和比较两个对象是否相同的区别了。
2. 在 Kotlin 中，三个等号 `===` 表示比较对象地址，两个 `==` 表示比较两个值大小。

## 3、类型转换

1. 由于不同的表示方式，较小类型并不是较大类型的子类型，较小的类型不能隐式转换为较大的类型。 
2. 这意味着在不进行显式转换的情况下我们不能把 Byte 型值赋给一个 Int 变量。
3. 每种数据类型都有下面的这些方法，可以转化为其它的类型：
	1. `toByte(): Byte`
	2. `toShort(): Short`
	3. `toInt(): Int`
	4. `toLong(): Long`
	5. `toFloat(): Float`
	6. `toDouble(): Double`
	7. `toChar(): Char`
4. 根据被转换的类型，有些类型没有对应方法
5. 而 `char` 类型是要先调用 `code` 方法，将其转换为 10 进制 `int` 类型的 `ASCII` 码，再进行其他类型的转换

```Kotlin
	package com.yuehai.kotlin._02_DataType
	
	import org.junit.Test
	
	/**
	@author 月海
	@create 2023/4/12 16:28
	 */
	class _02_BasicDataType {
		
		@Test
		fun basicDataType(){
			
			// 由于不同的表示方式，较小类型并不是较大类型的子类型，较小的类型不能隐式转换为较大的类型。
			// 这意味着在不进行显式转换的情况下我们不能把 Byte 型值赋给一个 Int 变量。
			val myBoolean:Boolean = true;
			println(myBoolean.toString())
	
			val myChar:Char = '\$';
			println(myChar.code.toFloat())
			
			val myByte:Byte = 127;
			println(myByte.toInt().toShort())
			
			val myInt:Int = 123456;
			println(myInt.toString())
			
		}
		
	}
```

6. 有些情况下也是可以使用自动类型转化的，前提是可以根据上下文环境推断出正确的数据类型而且数学操作符会做相应的重载。例如下面是正确的：

```Kotlin
// Long + Int => Long
val l = 1L + 3
```

## 4、位操作符

1. 对于 `Int` 和 `Long` 类型，还有一系列的位操作符可以使用，分别是：

| 操作符 | 名称 | 与 java 中对应 | 描述 |
| ------ | ---- | -------------- | ---- |
|shl(bits)|左移位|(Java’s <<)|每一位 * 2|
|shr(bits)|右移位|(Java’s >>)|每一位 / 2|
|ushr(bits)|无符号右移位|(Java’s >>>)|每一位 / 2|
|and(bits)|与|&|运算规则即(两个为真才为真)1&1=1 , 1&0=0 , 0&1=0 , 0&0=0|
|or(bits)|或|丨|运算规则(一个为真即为真)1丨0 = 1 , 1丨1 = 1 , 0丨0 = 0 , 0丨1 = 1|
|xor(bits)|异或|^|运算规则为1^0 = 1 , 1^1 = 0 , 0^1 = 1 , 0^0 = 0|
|inv()|反向|~|取反就是1为0,0为1,5的二进制位是0000 0101，取反后为1111 1010，值为-6|

```Kotlin
package com.yuehai.kotlin._01_BasicDataType

import org.junit.Test

/**
@author 月海
@create 2023/4/13 9:33

位操作符
 */
class _05_BitwiseOperators {
	@Test
	fun bitwiseOperators(){
		val myInt:Int = 123456
		
		// shl(bits) – 左移位 (Java’s <<) ，每一位 * 2
		println(myInt.shl(2))
		println("----------------")
		
		// shr(bits) – 右移位 (Java’s >>) ，每一位 / 2
		// 如果该数为正，则高位补0，若为负数，则高位补1；
		println(myInt.shr(1))
		println("----------------")
		
		// ushr(bits) – 无符号右移位 (Java’s >>>)，每一位 / 2
		// 无符号右移，也叫逻辑右移，即若该数为正，则高位补0，而若该数为负数，则右移后高位同样补0。
		println(myInt.ushr(1))
		println("----------------")
		
		// and(bits)，与 &；& 按位与的运算规则是将两边的数转换为二进制位，然后运算最终值
		// 运算规则即(两个为真才为真)1&1=1 , 1&0=0 , 0&1=0 , 0&0=0
		println( myInt and 12345 )
		println("----------------")
		
		// |or(bits)，或 |；| 按位或和 & 按位与计算方式都是转换二进制再计算
		// 不同的是运算规则(一个为真即为真)1|0 = 1 , 1|1 = 1 , 0|0 = 0 , 0|1 = 1
		println( myInt or 12345 )
		println("----------------")
		
		// |xor(bits)，异或 ^；^异或运算符顾名思义，异就是不同
		// 其运算规则为1^0 = 1 , 1^1 = 0 , 0^1 = 1 , 0^0 = 0
		println( myInt xor 123456 )
		println( myInt xor 12345 )
		println("----------------")
		
		// |inv()，反向 ~；取反就是1为0,0为1,5的二进制位是0000 0101，取反后为1111 1010，值为-6
		println( myInt xor 123456 )
		println( myInt xor 12345 )
		println("----------------")
	}
}

```

```Kotlin
493824
----------------
61728
----------------
61728
----------------
8192
----------------
127609
----------------
0
119417
----------------
0
119417
----------------

进程已结束,退出代码0
```

## 5、逻辑操作符

1. `||`：短路逻辑或
2. `&&`：短路逻辑与
3. `!`：逻辑非
# 四、`Kotlin` 其他数据类型

## 1、字符串

1. 和 Java 一样，String 是不可变的。方括号 `[]` 语法可以很方便的获取字符串中的某个字符，也可以通过 `for` 循环来遍历：
2. Kotlin 支持三个引号 """ 扩起来的字符串，支持多行字符串；注意前方的空格也算字符，可通过 trimIndent() 方法来删除多余的空白
3. Kotlin 支持模板字符串，`$` 表示值，`${}` 表示表达式

```Kotlin
package com.yuehai.kotlin._03_OtherDataType

import org.junit.Test

/**
@author 月海
@create 2023/4/13 10:44
 */
class _01_String {
	@Test
	fun myString(){
		val myString:String = "月海yuehai"
		
		// 和 Java 一样，String 是不可变的。方括号 [] 语法可以很方便的获取字符串中的某个字符，也可以通过 for 循环来遍历：
		println(myString[0])
		println(myString[2])
		for (s in myString){
			println(s)
		}
		
		// Kotlin 支持三个引号 """ 扩起来的字符串，支持多行字符串
		// 注意前方的空格也算字符，可通过 trimIndent() 方法来删除多余的空白
		val myString2:String = """
			月海
			yue
			hai
		"""
		val myString3:String = """
			月海
			yue
			hai
		""".trimIndent()
		println(myString2)
		println(myString3)
		
		// 模板字符串
		val myInt:Int = 123456
		// $ 表示值
		println("数字为：$myInt，字符串为：$myString")
		// ${} 表示表达式
		println("数字 + 1为：${myInt + 1}，字符串为：${myString.replace("月海", "言")}")
		
	}
}
```

```Kotlin
月
y
月
海
y
u
e
h
a
i

			月海
			yue
			hai
		
月海
yue
hai
数字为：123456，字符串为：月海yuehai
数字 + 1为：123457，字符串为：言yuehai

进程已结束,退出代码0
```

## 2、数组

1. 数组用类 Array 实现，并且还有一个 `size` 属性及 `get` 和 `set` 方法，由于使用 `[]` 重载了 `get` 和 `set` 方法，所以我们可以通过下标很方便的获取或者设置数组对应位置的值。
2. 数组的创建两种方式：一种是使用函数 `arrayOf()`；另外一种是使用工厂函数。如下所示，我们分别是两种方式创建了两个数组：

```Kotlin
package com.yuehai.kotlin._04_OtherDataType


/**
@author 月海
@create 2023/4/13 16:42
 */
fun main(){
	// 1、使用函数 arrayOf() 创建
	val arr:Array<Int> = arrayOf(5,1,4,6)
	// 使用工厂函数创建
	val arr2:Array<Int> = Array(4) { i: Int -> i * 2 }
	// 不使用泛型，使用对应类型的 arrayOf 方法创建数组
	val arr3 = intArrayOf(4,8,87,9,7)

	// 2、遍历数组
	arr.forEach { i: Int -> print("$i， ") }
	println()
	arr2.forEach { i: Int -> print("$i， ") }
	println()
	arr3.forEach { i: Int -> print("$i， ") }

	// 3、使用下标通过索引获取元素，get 也是通过索引获取
	println(arr3[2])
	println(arr3.get(2))

	// 4、获取数组大小
	println(arr3.size)

	// 5、使用下标通过索引设置元素，set 也是通过索引设置
	arr3[2] = 20000
	println(arr3[2])
	arr3.set(3, 30000)
	println(arr3.get(3))
}
```

```Kotlin
5， 1， 4， 6， 
0， 2， 4， 6， 
4， 8， 87， 9， 7， 87
87
5
20000
30000

进程已结束,退出代码0
```

## 3、集合 `List`

1. `List` 集合的最大特征就是集合元素都有对应的顺序索引。`List` 集合允许使用重复元素，可以通过索引来访问指定位置的集合元素
2. `list` 与 `java` 类似，分为不可变集合 `list` 和可变集合 `mutableList`

```Kotlin
package com.yuehai.kotlin._04_OtherDataType

/**
@author 月海
@create 2023/4/13 18:29
 */
fun main() {
    // 1、创建集合
    // listOf()：该函数返回不可变的List集合。该函数可接受0个或多个参数，这些参数将作为集合的元素。
    // listOfNotNull()：该函数返回不可变的List集合。该函数与前一个函数的唯一区别是,该函数会自动去掉传入的一系列参数中的null值。
    // mutableListOf()：该函数返回可变的MutableList集合。该函数可接受0个或多个参数，这些参数将作为集合的元素。
    // arrayListOf()：该函数返回可变的ArrayList集合。该函数可接受0个或多个参数，这些参数将作为集合的元素。
    // 定义不可变集合；只读的，不可变的、可序列化的
    val list:List<Int> = listOf(4,57,746)
    // 定义可变集合；
    // 在 MutableList 中，除了继承 List中 的那些函数外，另外新增了 add/addAll、remove/removeAll/removeAt、set、clear、retainAll 等更新修改的操作函数。
    val mutableList:MutableList<Int> = mutableListOf(5,4,7,78,56)
    // 如果已经有了一个不可变的List，想把他转换成可变的List，可直接调用转换函数toMutableList()
    val toMutableList = list.toMutableList();

    // 2、添加
    mutableList.add(1000)
    // 根据下标添加，会使后面的元素全部后移一位
    mutableList.add(0, 1000)

    // 3、遍历
    mutableList.forEach { l: Int -> print("$l， ") }
    println()

    // 4、判断是否为空
    toMutableList.clear()
    println(toMutableList.isEmpty())
}
```

```Kotlin
1000， 5， 4， 7， 78， 56， 1000， 
true

进程已结束,退出代码0
```

3. 常用方法：
4. 常见的 `List` 元素操作函数

| 方法                                                       | 描述                                                                                                                          |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `add`、`remove`、`set`、`clear`                                    | 这几个操作符与Java中的List一样                                                                                                |
| `toMutableList()`                                            | 将不可变集合变为可变集合                                                                                                      |
| `retainAll`                                                  | 取两个集合交集                                                                                                                |
| `contains(element: T): Boolean`                              | 判断集合中是否有指定元素，有就返回true，否则返回false                                                                         |
| `elementAt(index: Int): T`                                 | 查找下标对应的元素，如果下标越界会抛IndexOutOfBoundsException                                                                 |
| `elementAtOrElse(index: Int, defaultValue: (Int) -> T): T` | 查找下标对应元素，如果越界会根据方法返回默认值                                                                                |
| `elementAtOrNull(index: Int): T?`                          | 查找下标对应元素，如果越界就返回null                                                                                          |
| `first()`                                                  | 返回集合第1个元素，如果是空集，抛出异常java.util.NoSuchElementException: List is empty.                                       |
| `firstOrNull(): T?`                                        | 返回集合第1个元素，如果是空集, 对空指针异常处理的函数，如果集合为空，则返回null                                               |
| `first(predicate: (T) -> Boolean): T`                      | 返回符合条件的第一个元素，没有则抛异常NoSuchElementException                                                                  |
| `firstOrNull(predicate: (T) -> Boolean): T?`               | 返回符合条件的第一个元素，没有就返回null                                                                                      |
| `indexOf(element: T): Int`                                 | 返回指定元素的下标，没有就返回-1                                                                                              |
| `indexOfFirst(predicate: (T) -> Boolean): Int`             | 返回第一个符合条件的元素的下标，没有就返回-1                                                                                  |
| `indexOfLast(predicate: (T) -> Boolean): Int`              | 返回最后一个符合条件的元素下标，没有就返回-1                                                                                  |
| `last()`                                                   | 返回集合最后一个元素，空集则抛出异常NoSuchElementException                                                                    |
| `last(predicate: (T) -> Boolean): T`                       | 返回符合条件的最后一个元素，没有就抛NoSuchElementException                                                                    |
| `lastOrNull(predicate: (T) -> Boolean): T?`                | 返回符合条件的最后一个元素，没有就返回null                                                                                    |
| `lastIndexOf(element: T): Int`                             | 返回符合条件的最后一个元素的下标，没有就返回-1                                                                                |
| `single(): T`                                              | 该集合如果只有1个元素，则返回该元素。为空时会抛出NoSuchElementException 异常，存在多个元素时会抛 IllegalArgumentException异常 |
| `singleOrNull(): T?`                                       | 返回符合条件单个元素, 如果集合为空或者有多个元素，则返回null                                                                  |
| `single(predicate: (T) -> Boolean): T`                     | 返回符合条件的单个元素，如有没有符合的抛异常NoSuchElementException，或超过一个的抛异常IllegalArgumentException                |
| `singleOrNull(predicate: (T) -> Boolean): T?`              | 返回符合条件单个元素，如果未找到符合的元素或找到多个元素，则返回null                                                          |

5. `List` 集合运算的基本函数

| 方法                                       | 描述                                                                                                  |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `any(): Boolean`                           | 判断集合元素，如果集合为空，返回false, 集合中存有一个或多个元素时返回true                             |
| `any(predicate: (T) -> Boolean): Boolean`  | 判断集合元素，如果集合为空或者没有符号条件的元素返回false, 集合中存有一个或多个元素符合条件时返回true |
| `all(predicate: (T) -> Boolean): Boolean`  | 当且仅当该集合中所有元素都满足条件时，返回true；否则都返回false。                                     |
| `none(): Boolean`                          | 如果集合中没有元素，则返回true，否则返回false                                                         |
| `none(predicate: (T) -> Boolean): Boolean` | 如果集合中没有符合匹配条件的元素，返回true，否则返回false                                             |
| `count(): Int`                             | 返回集合元素个数                                                                                      |
|`count(predicate: (T) -> Boolean): Int`|返回符合匹配条件的元素的个数|
|`max, min`|查询最大，最小元素，空集返回null|

6. 过滤操作函数

| 方法                 | 描述                                      |
| -------------------- | ----------------------------------------- |
| `take(n: Int): List` | 根据传入的参数挑出该集合前n个元素的子集合 |

7. 映射操作符

| 方法                               | 描述                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `map(transform: (T) -> R): List`   | 将集合中的元素通过转换函数transform映射后的结果，存到一个集合中返回                                     |
| `mapNotNull(transform: (T) -> R?)` | 遍历集合每个元素，得到通过函数算子transform映射之后的值，剔除掉这些值中的null，返回一个无null元素的集合 |

8. 排序操作符

| 方法                       | 描述                                                               |
| -------------------------- | ------------------------------------------------------------------ |
| `reversed(): List`         | 倒序排列集合元素。如:[1, 2, 7, 6, 4, 5]排列后为:[5, 4, 6, 7, 2, 1] |
| `sorted(): List`           | 升序排序                                                           |
| `sortedDescending(): List` | 降序排序                                                           |
|`sortedBy和sortedByDescending`|可变集合MutableList的排序操作。根据函数映射的结果进行升序排序和降序排序|

9. 生产操作符

| 方法                             | 描述                                                |
| -------------------------------- | --------------------------------------------------- |
| `zip(other: Iterable): List`     | 合拢 转换是根据两个集合中具有相同位置的元素构建配对 |
| `plus(elements: Iterable): List` | 合并两个List                                        |

## 4、不可重复集合 `Set`

1. Kotlin 的 `Collection` 集合和 `Set` 集合的功能基本相同，`Set` 集合只是为 `Collection` 集合增加了额外的限制：集合元素不允许重复

```Kotlin
package com.yuehai.kotlin._04_OtherDataType

/**
@author 月海
@create 2023/4/13 19:29
 */
fun main() {
    // 1、创建不可变集合，返回值是Set，集合元素按添加顺序排列
    val set = setOf("Java", "Kotlin", "Go")
    // 创建可变集合，返回值是MutableSet，集合元素按添加顺序排列
    val mutableSet = mutableSetOf("Java", "Kotlin", "Go")
    // 创建 HashSet 集合，不保证元素的顺序
    val hashSet = hashSetOf("Java", "Kotlin", "Go")
    // 创建 LinkedHashSet 集合，集合元素按添加顺序排列
    val linkedHashSet = linkedSetOf("Java", "Kotlin", "Go")
    // 创建 TreeSet 集合，集合元素由小到大排列
    val treeSet = sortedSetOf("Java", "Kotlin", "Go")

    // 2、遍历
    hashSet.forEach { s -> print("$s， ") }

}
```

```Kotlin
Go， Java， Kotlin， 
进程已结束,退出代码0
```

## 5、键值对集合 `Map`

1. Kotlin的Map集合用于保存key-value对，其也被分为可变的和不可变的

```Kotlin
package com.yuehai.kotlin._04_OtherDataType

/**
@author 月海
@create 2023/4/13 19:44
 */
fun main() {
    // 1、创建不可变集合，返回值是 Map，按添加顺序排列
    val map = mapOf("Java" to 86, "Kotlin" to 92, "Go" to 78)
    // 创建可变集合，按添加顺序排列
    val mutableMap = mutableMapOf("Java" to 86, "Kotlin" to 92, "Go" to 78)
    // 创建 HashMap 集合，不保证排列顺序
    val hashMap = hashMapOf("Java" to 86, "Kotlin" to 92, "Go" to 78)
    // 创建 LinkedHashMap，按添加顺序排列
    val linkedHashMap = linkedMapOf("Java" to 86, "Kotlin" to 92, "Go" to 78)
    //创建 TreeMap 集合，按 key 由小到大排列
    val treeMap = sortedMapOf("Java" to 86, "Kotlin" to 92, "Go" to 78)

    // 2、增删改查
    hashMap["月海"] = 16
    hashMap.remove("Go")
    hashMap["Java"] = 100
    hashMap["Java"]


    // 3、遍历
    // 遍历 Map 的 key-value 对，entris 元素返回 key-value 对组成的 Set
    for (en in hashMap.entries) {
        print("${en.key}->${en.value}， ")
    }
    println()
    // 先遍历 Map 的 key，再通过 key 获取 value
    for (key in hashMap.keys) {
        print("${key}->${hashMap[key]}， ")
    }
    println()
    // 直接用 for-in 循环遍历 Map
    for ((key, value) in hashMap) {
        print("${key}->${value}， ")
    }
    println()
    // 用 Lambda 表达式遍历 Map
    hashMap.forEach { print("${it.key}->${it.value}， ") }
    println()


    // 对 Map 集合元素进行过滤：要求 key 包含 li
    println(hashMap.filter { "li" in it.key })

    // 将每个 key-value 对映射成新值，返回所有新值组成的 Map 集合
    println(hashMap.map { "${it.key}有${it.value}节课" })

    // 根据 key 获取最大值
    println(hashMap.maxBy { it.key })
    // 根据 value 获取最小值
    println(hashMap.minBy { it.value })

    val bMap= mapOf("Lua" to 67,"Erlang" to 73,"Kotlin" to 100)
    // 求并集
    println(hashMap + bMap)
    // 集合相减
    println(hashMap - bMap)
}
```

```Kotlin
Java->100， 月海->16， Kotlin->92， 
Java->100， 月海->16， Kotlin->92， 
Java->100， 月海->16， Kotlin->92， 
Java->100， 月海->16， Kotlin->92， 
{Kotlin=92}
[Java有100节课, 月海有16节课, Kotlin有92节课]
月海=16
月海=16
{Java=100, 月海=16, Kotlin=100, Lua=67, Erlang=73}
{Java=100, 月海=16, Kotlin=92}

进程已结束,退出代码0
```

# 五、函数

## 1、函数定义

1. 函数定义使用关键字 fun，参数格式为：参数 : 类型
2. 表达式作为函数体，返回类型自动推断：
3. 无返回值的函数(类似Java中的void)：

```Kotlin
package com.yuehai.kotlin._05_fun


/**
@author 月海
@create 2023/4/13 11:11
 */
fun main() {
	// 1、函数定义使用关键字 fun，参数格式为：参数 : 类型
	fun sum(a:Int, b:Int): Int {
		return a + b;
	}
	println(sum(1, 2))

	// 2、表达式作为函数体，返回类型自动推断：
	fun sum2(a:Int, b:Int) = a + b;
	// public 方法则必须明确写出返回类型
	// public fun sum2(a:Int, b:Int):Int= a + b;
	println(sum2(1, 2))

	// 3、无返回值的函数(类似Java中的void)：
	fun sum3() {
		println(1 + 2);
	}
	sum3();

	// 4、如果是返回 Unit （无返回值 void）类型，则可以省略(对于public方法也是这样)
	fun sum4():Unit {
		println(1 + 2);
	}
	sum3();
}
```

```Kotlin
3
3
3
3

进程已结束,退出代码0
```

## 2、可变长参数函数

1. 函数的变长参数可以用 `vararg` 关键字进行标识：

```Kotlin
package com.yuehai.kotlin._05_fun

/**
@author 月海
@create 2023/4/13 12:45
 */
fun main() {
	// 函数的变长参数可以用 vararg 关键字进行标识：
	fun fun1(a:Int, b:Int, vararg args:Int){
		println("a + b：${a + b}");
		for (arg in args) {
			println(arg)
		}
	}

	// 调用函数
	fun1(1,2,3,4,5,6,4,5,1000)
}
```

```Kotlin
a + b：3
3
4
5
6
4
5
1000

进程已结束,退出代码0
```

## 3、lambda（匿名函数）

```Kotlin
package com.yuehai.kotlin._05_fun

/**
@author 月海
@create 2023/4/13 12:50
 */
fun main() {
	// 定义普通函数
	fun fun1(a:Int, b:Int):Int{
		return a + b;
	}
	// 定义 lambda 表达式，有参数
	val fun2:(Int, Int) -> Int = { a, b -> a + b }
	// 定义 lambda 表达式，无参数
	val fun3: () -> Unit = { println("123") }

	println(fun1(1, 2))
	println(fun2(1, 2))
	fun3()
}
```

```Kotlin
3
3
123

进程已结束,退出代码0
```

## 4、将函数作为参数传递

```Kotlin
package com.yuehai.kotlin._05_fun

/**
@author 月海
@create 2023/4/13 20:30
 */
fun main() {
    // 接收函数作为参数
    fun fun4(a:Int, b:Int, c:(a:Int, b:Int)->Int):Int{
        val c1 = c(a, b)
        return c1 + 100
    }

    // 位置参数；调用函数，传递普通参数和函数参数
    println(fun4(10, 20, { a, b -> a * b }))

    // 命名参数；命名参数和位置参数是不能混在一起使用
    println(fun4(a=10, b=20, c={ a, b -> a * b }))

    // 将 Lambda 实参移出括号；如果函数是作为最后一个参数，才可以在以 lambda 表达式的方式在参数列表外传递
    println(fun4(10, 20) { a, b -> a * b })

    // 非 Lambda 函数
    println(fun4(10, 20) { a, b ->
        val c = a + b
        return@fun4 c * 10
    })

}
```

## 5、内联函数之 `with`

1. `with` 函数和前面的几个函数使用方式略有不同，因为它不是以扩展的形式存在的。
2. 它是将某对象作为函数的参数，在函数块内可以通过 `this` 指代该对象。返回值为函数块的最后一行或指定 `return` 表达式
3. `with` 函数的适用的场景：适用于调用同一个类的多个方法时，可以省去类名重复，直接调用类的方法即可，经常用于 `Android` 中 `RecyclerView` 中 `onBinderViewHolder` 中，数据 `model` 的属性映射到 `UI` 上

```Kotlin
package com.yuehai.kotlin._05_fun

/**
@author 月海
@create 2023/4/13 20:53
 */
fun main() {
    // 1、首先，我们定义一个数据类 Person
    data class Person(var name: String, var age: String)

    // 2、然后，实例化一个 Person
    val person = Person("张三", "23")

    // 3、不使用 with 的调用
    person.name = "月海"
    person.age = "16"
    println("name：${person.name}，age：${person.age}")

    // 4、使用 with 的调用
    with(person) {
        name = "言"
        age = "14"
    }
    println("name：${person.name}，age：${person.age}")

}
```

```Kotlin
name：月海，age：16
name：言，age：14

进程已结束,退出代码0
```

## 6、内联扩展函数之 `let`

1. `let` 扩展函数的实际上是一个作用域函数，当你需要去定义一个变量在一个特定的作用域范围内，`let` 函数的是一个不错的选择
2. `let` 函数另一个作用就是可以避免写一些判断 `null` 的操作
3. let函数适用的场景
	1. 场景一：最常用的场景就是使用 `let` 函数处理需要针对一个可 `null` 的对象统一做判空处理。
	2. 场景二：然后就是需要去明确一个变量所处特定的作用域范围内可以使用
4. `let` 函数使用前后的对比

```Kotlin
// 没有使用 let 函数的代码是这样的，看起来不够优雅
mVideoPlayer?.setVideoView(activity.course_video_view)
mVideoPlayer?.setControllerView(activity.course_video_controller_view)
mVideoPlayer?.setCurtainView(activity.course_video_curtain_view)

// 没有使用 let 函数的代码是这样的，看起来不够优雅
mVideoPlayer?.let {
    it.setVideoView(activity.course_video_view)
    it.setControllerView(activity.course_video_controller_view)
    it.setCurtainView(activity.course_video_curtain_view)
}
```

## 7、内联扩展函数之 `run`

1. `run` 函数实际上可以说是 `let` 和 `with` 两个函数的结合体，`run` 函数只接收一个 `lambda` 函数为参数，以闭包形式返回，返回值为最后一行的值或者指定的 return 的表达式
2. `run` 函数的适用场景：适用于 `let`、`with` 函数任何场景。因为 `run` 函数是 `let`、`with` 两个函数结合体，准确来说它弥补了 `let` 函数在函数体内必须使用 `it` 参数替代对象，在 `run` 函数中可以像 `with` 函数一样可以省略，直接访问实例的公有属性和方法，另一方面它弥补了 `with` 函数传入对象判空问题，在 `run` 函数中可以像 `let` 函数一样做判空处理

```Kotlin
// with 代码
override fun onBindViewHolder(holder: ViewHolder, position: Int){
  val item = getItem(position)?: return

  with(item){

   holder.tvNewsTitle.text = StringUtils.trimToEmpty(titleEn)
    holder.tvNewsSummary.text = StringUtils.trimToEmpty(summary)
    holder.tvExtraInf = "难度：$gradeInfo | 单词数：$length | 读后感: $numReviews"
    ...  
  }
}

//使用 run 函数后的优化
override fun onBindViewHolder(holder: ViewHolder, position: Int){

 getItem(position)?.run{
   holder.tvNewsTitle.text = StringUtils.trimToEmpty(titleEn)
    holder.tvNewsSummary.text = StringUtils.trimToEmpty(summary)
    holder.tvExtraInf = "难度：$gradeInfo | 单词数：$length | 读后感: $numReviews"
    ...  
  }
}
```

## 8、内联扩展函数之 `apply`

1. 整体作用功能和 run 函数很像，唯一不同点就是它返回的值是对象本身，而 run 函数是一个闭包形式返回，返回的是最后一行的值。正是基于这一点差异它的适用场景稍微与 run 函数有点不一样。
2. apply 一般用于一个对象实例初始化的时候，需要对对象中的属性进行赋值。或者动态 inflate 出一个 XML 的 View 的时候需要给 View 绑定数据也会用到，这种情景非常常见。特别是在我们开发中会有一些数据 model 向View model 转化实例化的过程中需要用到

```Kotlin
// 没有使用apply函数的代码是这样的，看起来不够优雅
mSheetDialogView = View.inflate(activity, R.layout.biz_exam_plan_layout_sheet_inner, null)
mSheetDialogView.course_comment_tv_label.paint.isFakeBoldText = true
mSheetDialogView.course_comment_tv_score.paint.isFakeBoldText = true
mSheetDialogView.course_comment_tv_cancel.paint.isFakeBoldText = true
mSheetDialogView.course_comment_tv_confirm.paint.isFakeBoldText = true
mSheetDialogView.course_comment_seek_bar.max = 10
mSheetDialogView.course_comment_seek_bar.progress = 0

// 使用apply函数后的代码是这样的
mSheetDialogView = View.inflate(activity, R.layout.biz_exam_plan_layout_sheet_inner, null).apply{
    course_comment_tv_label.paint.isFakeBoldText = true
    course_comment_tv_score.paint.isFakeBoldText = true
    course_comment_tv_cancel.paint.isFakeBoldText = true
    course_comment_tv_confirm.paint.isFakeBoldText = true
    course_comment_seek_bar.max = 10
    course_comment_seek_bar.progress = 0
}

// 多层级判空问题
if (mSectionMetaData == null || mSectionMetaData.questionnaire == null || mSectionMetaData.section == null) {
    return;
}
if (mSectionMetaData.questionnaire.userProject != null) {
    renderAnalysis();
    return;
}
if (mSectionMetaData.section != null && !mSectionMetaData.section.sectionArticles.isEmpty()) {
    fetchQuestionData();
    return;
}

// kotlin的apply函数优化
mSectionMetaData?.apply{
//mSectionMetaData不为空的时候操作mSectionMetaData
}?.questionnaire?.apply{
//questionnaire不为空的时候操作questionnaire
}?.section?.apply{
//section不为空的时候操作section
}?.sectionArticle?.apply{
//sectionArticle不为空的时候操作sectionArticle
}
```

## 9、内联扩展函数之 `also`

1. also 函数的结构实际上和 let 很像唯一的区别就是返回值的不一样，let 是以闭包的形式返回，返回函数体内最后一行的值，如果最后一行为空就返回一个 Unit 类型的默认值。而 also 函数返回的则是传入对象的本身
2. 适用于 let 函数的任何场景，also 函数和 let 很像，只是唯一的不同点就是 let 函数最后的返回值是最后一行的返回值而 also 函数的返回值是返回当前的这个对象。一般可用于多个扩展函数链式调用

## 10、`let`、`with`、`run`、`apply`、`also` 函数区别

![](attachments/Pasted%20image%2020230413211225.png)

![](attachments/Pasted%20image%2020230413211232.png)

# 六、类和对象

# 七、

# 八、

# 九、

# 十、

# 十一、

# 十二、

# 十三、

# 十四

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、

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















