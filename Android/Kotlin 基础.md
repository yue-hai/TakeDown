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

6. 上面的版本不重要，重要的是项目中使用的版本：`gradle/wrapper/gradle-wrapper.properties`

```properties
#Wed May 10 09:51:26 CST 2023
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
# 后面的 gradle-8.1-bin.zip ，表示项目使用的 gradle 版本号
distributionUrl=https\://services.gradle.org/distributions/gradle-8.1-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

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
3. 指定类型：`val 变量名:类型名`
4. 指定变量可为空：`val 变量名:类型名?`

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
package com.yuehai.kotlin._02_BasicGrammar

/**
@author 月海
@create 2023/4/14 9:16
 */
fun main() {
	// 区间默认由小到大，输出 1234
	println("---- 区间默认由小到大 ----")
	for (i in 1..4) print("$i， ")
	// 区间默认由小到大，由大到小则会什么都不输出
	println("---- 区间默认由小到大，由大到小则会什么都不输出 ----")
	for (i in 4..1) print("$i， ")
	
	// until，半包区间，包左不包右
	println("---- until，半包区间，包左不包右 ----")
	for (i in 1 until  4) print("$i， ")
	
	// downTo ，倒序，由大到小的区间
	println("---- downTo ，倒序，由大到小的区间 ----")
	for (i in 4 downTo 1) print("$i， ")
	
	// step 跳步，跳过只当步长
	println("---- step 跳步，跳过只当步长 ----")
	for (i in 1 .. 4 step 2) print("$i， ")
	
	// 判断是否在区间内；等同于 1 <= num && num <= 10
	println("---- 判断是否在区间内；等同于 1 <= num && num <= 10 ----")
	val num = 8
	if (num in 1..10) {
		println(num)
	}

}
```

```Kotlin
---- 区间默认由小到大 ----
1， 2， 3， 4， ---- 区间默认由小到大，由大到小则会什么都不输出 ----
---- until，半包区间，包左不包右 ----
1， 2， 3， ---- downTo ，倒序，由大到小的区间 ----
4， 3， 2， 1， ---- step 跳步，跳过只当步长 ----
1， 3， ---- 判断是否在区间内；等同于 1 <= num && num <= 10 ----
8

进程已结束,退出代码0
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
fun main() {
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
	println("---- 更简单的 lambda 表达式 ----------------")
	list.forEach { println(it) }
	
	// 5、传递函数
	println("---- 传递函数 ----------------")
	list.forEach {
		val a = it * 10;
		println(a * 10)
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
---- 更简单的 lambda 表达式 ----------------
5
1
4
7
8
2
---- 传递函数 ----------------
500
100
400
700
800
200

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

## 9、单例

1. 使用关键字 `object` 即可创建
2. 在编译成的 java 代码里会编译成构造器私有化

```Kotlin
object a{

}
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
| `none(): Boolean`                          | 如果集合中没有任何元素，则返回true，否则返回false                                                     |
| `none(predicate: (T) -> Boolean): Boolean` | 如果集合中没有符合匹配条件的元素，返回true，否则返回false                                             |
| `count(): Int`                             | 返回集合元素个数                                                                                      |
| `count(predicate: (T) -> Boolean): Int`    | 返回符合匹配条件的元素的个数                                                                          |
| `max, min`                                 | 查询最大，最小元素，空集返回null                                                                      |
| `find(predicate: (T) -> Boolean): T?` | 查找符合给定条件的第一个元素，并返回该元素（或者返回 null）                                                                                                      |

6. 过滤操作函数

| 方法                                         | 描述                                      |
| -------------------------------------------- | ----------------------------------------- |
| `take(n: Int): List`                         | 根据传入的参数挑出该集合前n个元素的子集合 |
| `filter(predicate: (T) -> Boolean): List<T>` | 过滤集合中满足给定条件的元素，并返回一个新的集合                                          |

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

# 五、`Kotlin` 函数

## 1、函数定义

1. 函数定义使用关键字 fun，参数格式为：参数 : 类型
2. 因为是函数式的语言，所以必须要有返回值：
	1. `Unit`：无返回值，类似 java 中的 `void`
	2. `Any`：全部类型，类似 java 中的 `Object`
	3. `Nothing`：这个方法就是无法正常返回的
	4. 这三个的具体定义在第二章，第 3 节
3. 在函数中可指定变量不可为空：`变量名!!`

```Kotlin
package com.yuehai.kotlin._05_fun

/**
@author 月海
@create 2023/4/13 11:11
 */
fun main() {
	// 1、函数定义使用关键字 fun，参数格式为：参数 : 类型
	fun sum(a:Int, b:Int): Int {
		// a!!：指定 a 不可为空，若为空则会报错
		return a!! + b;
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

# 六、`Kotlin` 类和对象

## 1、类定义

### ①、属性和方法

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 10:09
 */

/**
 * 定义类，类名为：Person
 *
 * Kotlin 中的类可以有一个 主构造器，以及一个或多个次构造器
 * 主构造器是类头部的一部分，位于类名称之后，使用 constructor 关键词定义，不能包含任何代码
 * 如果主构造器没有任何注解，也没有任何可见度修饰符，那么constructor关键字可以省略
 */
class Person (name:String?, age:Int?) {
	
	// 成员变量，默认 public
	var name = name
		/**
		 * 属性的 get set 方法；此处的 field 就代表 get set 所在的这个变量
		 * 设置了 get set 方法，则调用时就会自动走 get set 方法
		 * 不设置也是默认拥有的
		 */
		get() = "name：$field"
		set(value){
			field = " name 修改：$value"
		}
	
	var age = age
		// 属性的 get set 方法；此处的 field 就代表 get set 所在的这个变量
		get() = field?.minus(1)
		set(value){
			if (value != null) {
				field = value - 2
			}
		}
	
	// 也可以定义为私有方法 private
	// lateinit 关键字可以延迟初始化，但数据类型不可以是基本类型
	private lateinit var sex:String;
	
	
	// 成员函数
	fun play(){
		println("name：$name，age：$age")
	}
	
}

// 也可以定义一个空类
class Empty

fun main() {
	// 实例化类
	val person = Person("月海", 16)
	
	// 设置了 get set 方法，则调用时就会自动走 get set 方法
	println(person.name)
	println(person.age)
	// println(person.sex)
	
	person.name = "言"
	person.age = 14
	
	// 调用方法
	person.play()
}
```

```Kotlin
name：月海
15
name：name： name 修改：言，age：11

进程已结束,退出代码0
```

### ②、构造器

1. Kotlin 中的类可以有一个 主构造器，以及一个或多个次构造器
2. 主构造器是类头部的一部分，位于类名称之后，使用 constructor 关键词定义
3. 如果主构造器没有任何注解，也没有任何可见度修饰符，那么constructor关键字可以省略
4. 主构造器中不能包含任何代码，初始化代码可以放在初始化代码段中，初始化代码段使用 init 关键字作为前缀
5. 从最后一个次构造函数依次向前代理

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 10:56
 */
/**
 * 定义类，类名为：Person
 *
 * Kotlin 中的类可以有一个 主构造器，以及一个或多个次构造器
 * 主构造器是类头部的一部分，位于类名称之后，使用 constructor 关键词定义
 * 如果主构造器没有任何注解，也没有任何可见度修饰符，那么constructor关键字可以省略
 * 主构造器中不能包含任何代码，初始化代码可以放在初始化代码段中，初始化代码段使用 init 关键字作为前缀
 */
class Person2 (name:String) {
	
	// 成员变量，默认 public
	var name: String? = null
	var age:Int? = null
	// lateinit 关键字可以延迟初始化，但数据类型不可以是基本类型
	private lateinit var sex:String;
	
	// 成员函数
	fun play(){
		println("name：$name，age：$age，sex：$sex")
	}
	
	// 主构造器初始化代码块
	init {
		println("---- 主构造器初始化代码块 ----")
		// 可以在此对变量进行初始化（定义时初始化好像更方便）
		this.name = name
	}
	
	// 次构造函数 1，必须使用 this 代理主构造函数
	constructor(name:String, age:Int) : this(name){
		println("---- 次构造函数 1 ----")
		// 可以在此对变量进行初始化（定义时初始化好像更方便）
		this.age = age
	}
	// 次构造函数 2，必须使用 this 代理主构造函数
	constructor(name:String, age:Int, sex:String) : this(name, age){
		println("---- 次构造函数 2 ----")
		// 也可以对常量或 lateinit 关键字定义函数进行初始化
		this.sex = sex
	}
	
	
}

fun main() {
	// 实例化对象，因为变量定义时并没有赋初始值，所以 person2 和 person3 调用没有传递值的属性时会报错
	val person = Person2("月海", 16, "0")
	val person2 = Person2("月海", 16 )
	val person3 = Person2("月海")

	// 调用方法
	person.play()
	// person2.play()
}
```

```Kotlin
---- 主构造器初始化代码块 ----
---- 次构造函数 1 ----
---- 次构造函数 2 ----
---- 主构造器初始化代码块 ----
---- 次构造函数 1 ----
---- 主构造器初始化代码块 ----
name：月海，age：16，sex：0

进程已结束,退出代码0
```

6. 更简便的属性定义

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 10:56
 */
/**
 * 定义类，类名为：Person
 *
 * 可以在构造器中直接定义成员属性，实例化时可直接被赋值
 */
class Person2b (
	var name: String,
	var age: Int,
	private var sex: String
) {
	
	// 成员函数
	fun play(){
		println("name：$name，age：$age，sex：$sex")
	}
	
}

fun main() {
	// 实例化对象，因为变量定义时并没有赋初始值，所以 person2 和 person3 调用没有传递值的属性时会报错
	val person = Person2b("月海", 16, "0")

	// 调用方法
	person.play()
	
	// 设置属性
	person.name = "言"
	// 获取属性
	println(person.name)
}
```

```Kotlin
name：月海，age：16，sex：0
言

进程已结束,退出代码0
```

### ③、权限修饰符

1. 类修饰符，标示类本身特性：
	1. `final`：类不可继承，默认修饰符
	2. `open`：类可继承，类默认是 `final` 的
	3. `abstract`：抽象类
	4. `enum`：枚举类
	5. `annotation`：注解类
2. 属性方法修饰符：
	1. `public`，公共的，所有调用的地方都可见；默认权限修饰符
	2. `private`，私有的，仅在同一个文件中可见
	3. `protected`，受保护的，同一个文件中或子类可见
	4. `internal`，内部的，同一个模块中可见（与 java 不能混用）；使用场景：你定义了一个方法，自己的其他方法要用到它，但是你又不希望别人实例化了这个类之后用对象来调用这个方法

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 12:56
 */

/**
 * 类的修饰符，标示类本身特性：
 * final		：类不可继承，默认修饰符
 * open			：类可继承，类默认是 final 的
 * abstract		：抽象类
 * enum			：枚举类
 * annotation	：注解类
 */
open class Person3(
	// public，公共的，所有调用的地方都可见；默认权限修饰符
	public var name:String,
	// private，私有的，仅在同一个文件中可见
	private var sex:Char,
	// protected，受保护的，同一个文件中或子类可见
	protected var age:Int,
	
) {
	
	// internal，内部的，同一个模块中可见（与 java 不能混用）
	// 使用场景：你定义了一个方法，自己的其他方法要用到它，但是你又不希望别人实例化了这个类之后用对象来调用这个方法
	internal fun fun1(){
		println("只能我自己用！")
	}
	
}
```

### ④、嵌套类、内部类和匿名内部类

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 13:20
 */
class Person4(
	var name:String,
	var age:Int,
	private var sex:Char,
	) {
	
	// 我们可以把类嵌套在其他类中
	class yueHai{
		fun play(){
			println("月海")
		}
	}
	
	// 内部类定义：使用 inner 关键字
	// 内部类会带有一个对外部类的对象的引用，所以内部类可以访问外部类成员属性和成员函数
	inner class yan{
		// 获取外部类的成员变量：
		val yanName = name;
		// 为了消除歧义，要访问来自外部作用域的 this，我们使用 this@label，其中 @label 是一个 代指 this 来源的标签
		val yanAge = this@Person4.age
		
		fun play(){
			println("${yanName}，$yanAge")
		}
	}
	
	/**
	 * 匿名内部类，使用对象表达式来创建匿名内部类，要使用接口
	 *
	 * 1、定义一个接口，并在其中定义一个抽象方法
	 * 2、定义一个方法，传入定义的接口
	 * 3、在方法中调用接口中的抽象方法
	 * 4、调用匿名内部类，使用对象表达式来创建匿名内部类，实现其方法
	 */
	// 2、定义一个方法，传入定义的接口
	fun game(play: Play){
		// 3、在方法中调用接口中的抽象方法
		play.game()
	}
	
	
}

// 1、定义一个接口
interface Play{
	// 1.2、在接口中定义一个抽象方法
	fun game()
}

fun main() {
	// 调用嵌套类
	Person4.yueHai().play()
	
	// 调用内部类
	Person4("月海", 16, '0').yan().play()
	
	// 4、调用匿名内部类，使用对象表达式来创建匿名内部类，实现其方法
	Person4("月海", 16, '0').game(object : Play{
		override fun game() {
			println("调用匿名内部类，使用对象表达式来创建匿名内部类，实现其方法")
		}
	})
	
}
```

```Kotlin
月海
月海，16
调用匿名内部类，使用对象表达式来创建匿名内部类，实现其方法

进程已结束,退出代码0
```

## 2、继承

### ①、父类

1. Kotlin 中所有类都继承该 Any 类，它是所有类的超类，对于没有超类型声明的类是默认超类：从 Any 隐式继承：`class Example`
2. Any 默认提供了三个函数：`equals()、hashCode()、toString()`，因此，所有 Kotlin 类都定义了这些方法；注意：`Any` 不是 `java.lang.Object`
3. 如果一个类要被继承，可以使用 `open` 关键字进行修饰
4. 与 java 相同，子类无法多继承，但是可以实现多个接口

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 14:05
 */

// 定义基类
open class Play1(
	val name:String
) {
}

// 子类继承父类
class Game(name:String):Play1(name){

}
```

### ②、构造函数

1. 如果子类有主构造函数， 则基类必须在主构造函数中立即初始化
2. 如果子类没有主构造函数，则必须在每一个二级构造函数中用 super 关键字初始化基类，或者在代理另一个构造函数。初始化基类时，可以调用基类的不同构造方法

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 14:24
 */
// 定义基类
open class Play2(
	val name:String
) {
	fun play(){
		println("玩$name")
	}
}

// 如果子类有主构造函数， 则基类必须在主构造函数中立即初始化
class Game2(name:String):Play2(name){

}

//  如果子类没有主构造函数，则必须在每一个二级构造函数中用 super 关键字初始化基类，或者在代理另一个构造函数。初始化基类时，可以调用基类的不同构造方法
class Game2b:Play2{
	constructor(name:String): super(name){
	
	}
}

fun main() {
	// 调用类中的方法
	Game2("月海").play()
	Game2b("月海").play()

}
```

### ③、重写

1. 在基类中，使用 `fun` 声明函数时，此函数默认为 `final` 修饰，不能被子类重写。如果允许子类重写该函数，那么就要手动添加 `open` 修饰它，子类重写方法使用 `override` 关键词
2. 属性重写使用 `override` 关键字，属性必须具有兼容类型，每一个声明的属性都可以通过初始化程序或者 `getter` 方法被重写
3. 可以用一个 `var` 属性重写一个 `val` 属性，但是反过来不行。因为 `val` 属性本身定义了 `getter` 方法，重写为 `var` 属性会在衍生类中额外声明一个 `setter` 方法
4. 子类继承父类时，不能有跟父类同名的变量，除非父类中该变量为 `private`，或者父类中该变量为 `open` 并且子类用 `override` 关键字重写
5. 派生类初始化顺序：
	1. 在构造派生类的新实例的过程中，第一步完成其基类的初始化（在之前只有对基类构造函数参数的求值），因此发生在派生类的初始化逻辑运行之前
	2. 这意味着，基类构造函数执行时，派生类中声明或覆盖的属性都还没有初始化。
	3. 如果在基类初始化逻辑中（直接或通过另一个覆盖的 open 成员的实现间接）使用了任何一个这种属性，那么都可能导致不正确的行为或运行时故障。
	4. 设计一个基类时，应该避免在构造函数、属性初始化器以及 init 块中使用 open 成员
6. 可以使用 `super` 关键字调用其父类的函数与属性
7. 在一个内部类中访问外部类的超类，可以通过由外部类名限定的 `super` 关键字来实现

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 14:50
 */
// 定义基类
open class Play3(
	// 属性重写使用 override 关键字，属性必须具有兼容类型，每一个声明的属性都可以通过初始化程序或者getter方法被重写
	val name:String = "yuehai",
	val age:Int = 16
) {
	// 在基类中，使用 fun 声明函数时，此函数默认为 final 修饰，不能被子类重写。如果允许子类重写该函数，那么就要手动添加 open 修饰它
	open fun play(){
		println("玩$name")
	}
}

// 如果子类有主构造函数， 则基类必须在主构造函数中立即初始化
class Game3(name:String):Play3(name){
	
	// 子类重写方法使用 override 关键词
	override fun play(){
		// 可以使用 super 关键字调用其父类的函数与属性
		println("玩${name}的游戏，${super.age}")
	}
}

fun main() {
	// 调用类中的方法
	Game3("月海").play()
	
}
```

```Kotlin
玩月海的游戏，16

进程已结束,退出代码0
```

### ④、抽象类

1. 抽象类：存在抽象方法的类，使用 abstract 关键字定义

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 15:21
 */
// 抽象类：存在抽象方法的类，使用 abstract 关键字定义
abstract class Play4(
	val name:String = "yuehai",
	val age:Int = 16
) {
	// 抽象方法
	abstract fun play()
}

// 如果子类有主构造函数， 则基类必须在主构造函数中立即初始化
class Game4(name:String):Play4(name){
	// 子类中要实现父类的抽象方法，不然子类也必须定义为抽象类
	override fun play() {
		println("玩${name}的游戏，${super.age}")
	}
}

fun main() {
	// 调用类中的方法
	Game4("月海").play()
	
}
```

```Kotlin
玩月海的游戏，16

进程已结束,退出代码0
```

## 3、接口

1. Kotlin 接口与 Java 8 类似，使用 `interface` 关键字定义接口，允许方法有默认实现
2. 必须要实现接口中的所有抽象属性和方法
3. 可以多实现

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 15:27
 */

// 使用 interface 关键字定义接口，允许方法有默认实现
interface PlayInterface1{
	
	// 接口中的属性只能是抽象的，不允许初始化值，接口不会保存属性值，实现接口时，必须重写属性
	var name:String
	
	// 定义抽象方法 play
	fun play()
	// 定义抽象方法 sleep
	fun sleep()
	
	// 定义默认已实现的方法
	fun game(){
		println("玩${name}的游戏")
	}
	
}

// 实现接口，可多实现
class GameInterface1(
	// 必须要实现接口中的所有抽象属性和方法
	override var name: String
):PlayInterface1{
	
	override fun play() {
		println("玩${name}")
	}
	
	override fun sleep() {
		println("睡${name}")
	}
}

fun main() {
	// 实例化类
	val gameInterface1 = GameInterface1("月海")
	
	// 调用方法
	gameInterface1.game()
	gameInterface1.play()
	gameInterface1.sleep()
}
```

```Kotlin
玩月海的游戏
玩月海
睡月海

进程已结束,退出代码0
```

## 4、数据类

1. 数据类和普通类并没有什么不同，只有多了一些东西
2. Kotlin 可以创建一个只包含数据的类，关键字为 `data`
3. 编译器会自动的从主构造函数中根据所有声明的属性提取以下函数：

```Kotlin
equals()
hashCode()
// 格式如 "User(name=John, age=42)"
toString() 
// functions 对应于属性，按声明顺序排列
componentN() 
// 复制函数
copy() 
```

3. 如果这些函数在类中已经被明确定义了，或者从超类中继承而来，就不再会生成。为了保证生成代码的一致性以及有意义，数据类需要满足以下条件：
	1. 主构造函数至少包含一个参数。
	2. 所有的主构造函数的参数必须标识为val 或者 var ;
	3. 数据类不可以声明为 `abstract`、`open`、`sealed` 或者 `inner`;
	4. 数据类不能继承其他类 (但是可以实现接口)

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/14 16:24
 */

// 定义数据类
data class User(
	val name:String,
	val age:Int,
)

fun main() {
	// 实例化数据类
	val user = User("月海", 16)
	println(user.toString())
	
	// 使用 copy 函数复制对象并修改部分属性
	val copy = user.copy(name = "言")
	println(copy)
}
```

```Kotlin
User(name=月海, age=16)
User(name=言, age=16)

进程已结束,退出代码0
```

## 5、伴生类（伴生对象）

1. 伴生对象从功能上的另外一个描述：它是工厂方法和静态成员的地盘。
2. 与 Java 做一个比较，Kotlin 本身是不支持 `static` 关键字的，即 `static` 关键字并不是Kotlin语言的一部分。
3. 作为替代方案，Kotlin 提供了包级别函数（可以在大多数情况下替代Java的静态方法）和对象声明（大多数情况下替代Java的静态方法及静态成员），多数情况下，还是推荐使用顶层函数
4. 如何声明：在类中定义一个用特殊关键字标记的对象：`companion`。`companion` 修饰的对象，使得外部可以直接通过 `companion` 容器类来访问这个对象（companion object）的属性和方法，就像 Java 中对静态方法和静态成员的访问形式，不需要再通过具体实例来访问
5. 伴生对象内定义的属性，类似静态属性：
	1. 若是定义常量 `val`，需要加关键字 `const`
	2. 若是定义变量 `var`，需要加注解 `@JvmField`
	3. 如果想被 java 调用时被当作静态属性，需添加注解 `@JvmStatic`，此注解只对 java 有用

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/15 13:41
 */

class Person5(
    // 定义普通成员变量
    var name:String,
    var age:Int,
    private var sex:Char,
) {

    // 定义普通成员函数
    fun play(){
        println("name：$name，age：$age，sex：$sex")
    }

    // 伴生对象；如果想被 java 调用时被当作静态属性，需添加注解 @JvmStatic，此注解只对 java 有用
    companion object {
        // 伴生对象内定义的属性，类似静态属性，若是定义常量 val，需要加关键字 const
        const val comName:String = "言"
        // 伴生对象内定义的属性，类似静态属性，若是定义变量 var，需要加注解 @JvmField
        @JvmField
        var comAge:Int = 14
        @JvmField
        val arr:Array<Int> = arrayOf(5,1,4,6)
        // 伴生对象内定义的方法，类似静态方法
        fun comOlay(){
            println("伴生对象方法")
        }
    }

}


fun main() {
    // 实例化类
    val person = Person5("月海", 16, '0')

    // 调用普通成员变量
    println(person.name)
    // 调用伴生对象成员函数
    person.play()


    // 设置伴生对象成员变量
    Person5.comAge = 15
    Person5.arr[0] = 1000
    // 调用伴生对象成员变量
    println(Person5.comAge)
    println(Person5.comName)
    Person5.arr.forEach { print("$it， ") }
    println()

    // 调用伴生对象成员函数
    Person5.comOlay()

}
```

```Kotlin
月海
name：月海，age：16，sex：0
15
言
1000， 1， 4， 6， 
伴生对象方法

进程已结束,退出代码0
```

## 6、枚举类

1. 枚举类最基本的用法是实现一个类型安全的枚举。
2. 枚举常量用逗号分隔 `,` 每个枚举常量都是一个对象。
3. 枚举初始化，每一个枚举都是枚举类的实例，它们可以被初始化；在主构造函数中定义的变量就相当于在每个枚举内定义的变量；可以认为每一个枚举项就是继承了枚举类的子类
4. Kotlin 中的枚举类可以实现接口，每个枚举项都需要实现

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/15 14:55
 */
// 枚举常量用逗号分隔，每个枚举常量都是一个对象
enum class Color {
    RED,
    BLACK,
    BLUE,
    GREEN,
    WHITE
}

// 枚举初始化，每一个枚举都是枚举类的实例，它们可以被初始化
// 在主构造函数中定义的变量就相当于在每个枚举内定义的变量
// 可以认为每一个枚举项就是继承了枚举类的子类
enum class Color2(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF)
}

// 使用 interface 关键字定义接口，允许方法有默认实现
interface PlayInterface2{
    // 定义抽象方法 play
    fun play()
}
// Kotlin 中的枚举类可以实现接口，每个枚举项都需要实现
enum class Color3(val rgb: Int):PlayInterface2 {
    RED(0xFF0000) {
        override fun play() {
            TODO("Not yet implemented")
        }
    },
    GREEN(0x00FF00) {
        override fun play() {
            TODO("Not yet implemented")
        }
    }
}

fun main() {
    println(Color.RED.name)
    println(Color2.RED.rgb)

    // 可以使用字符串匹配枚举名，与 . 的方式相同，若未匹配成功，会抛出IllegalArgumentException
    val valueOf = Color2.valueOf("RED")
    println("枚举名：${valueOf.name}，枚举值：${valueOf.rgb}")

    // 以数组的形式，返回枚举项
    val values = Color2.values()
    values.forEach { println("枚举名：${it.name}，枚举值：${it.rgb}") }
}
```

```Kotlin
RED
16711680
枚举名：RED，枚举值：16711680
枚举名：RED，枚举值：16711680
枚举名：GREEN，枚举值：65280
枚举名：BLUE，枚举值：255

进程已结束,退出代码0
```

## 7、密封类

1. 密封类用来表示受限的类继承结构：当一个值为有限几种的类型，而不能有任何其他类型时。
2. 在某种意义上，他们是枚举类的扩展：枚举类型的值集合也是受限的，但每个枚举常量只存在一个实例，而密封类的一个子类可以有可包含状态的多个实例。
3. 要声明一个密封类，可以在类名之前加上 `sealed` 修饰符。一个密封类可以有子类，但是所有子类都必须在同一个文件中声明，作为密封类的本身。（kotlin 1.1 之前，规则甚至更严格：类必须嵌套在密封类的声明中）
4. `sealed` 不能修饰 `interface`、`abstract class`(会报 `warning`，但是不会出现编译错误)

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/15 15:49
 */

// 定义一个密封类：武器类
sealed class Weapon {
    // 定义属于密封类的属性
    open val name:String? = null

    // 在密封类中定义数据类，需继承密封类，在原本密封类的基础上可以扩展
    data class Gun(override val name:String, val bullet:Double): Weapon()
    data class Knife(override val name:String, val size:String): Weapon()
}

fun main() {
    // 实例化密封类中的数据类
    val gun = Weapon.Gun("KAR98K", 7.92)
    val knife = Weapon.Knife("砍刀", "很大的砍刀")

    println("name：${gun.name}，bullet：${gun.bullet}")
    println("name：${knife.name}，size：${knife.size}")
}
```

```Kotlin
name：KAR98K，bullet：7.92
name：砍刀，size：很大的砍刀

进程已结束,退出代码0
```

## 8、对象表达式

1. Kotlin 中的对象表达式是一种创建匿名内部类的方式，类似于 Java 中的匿名内部类。
2. 对象表达式通过 `object` 关键字实现，能够实现对当前类进行轻微修改的类对象，且不需要声明一个新的子类。
3. 对象表达式和对象声明都可以用来创建单例对象，但是对象表达式可以在任何地方定义，而不需要在类的顶层定义。
4. Kotlin 中的对象声明是一种创建单例类的方式，通过 `object` 关键字实现。对象声明是在定义它的地方立即创建并初始化的

```Kotlin
fun main() {
	// 使用对象表达式来创建一个匿名内部类，该类只使用一次。
	// 创建了一个对象 site，该对象包含两个属性：name 和 url。
	// 我们可以通过 site.name 和 site.url 访问这些属性。
    val site = object {
        var name: String = "Kotlin Tutorial"
        var url: String = "www.runoob.com"
    }
    println(site.name)
    println(site.url)
}
```

## 9、委托

1. Kotlin 的类委托是一种设计模式，基本理念是：操作对象自己不会去处理某段逻辑，而是会把工作委托给另外一个辅助对象去处理。
2. Kotlin 也支持委托功能，分为类委托和属性委托。
3. 属性委托是通过将一个属性的 `get()` 和 `set()` 方法委托给另一个对象来实现的。这个对象可以是任何实现了 `getValue()` 和 `setValue()` 方法的类。Kotlin 标准库提供了一些有用的委托，例如：延迟属性、可观察属性、映射属性等等。

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

import kotlin.reflect.KProperty

/**
@author 月海
@create 2023/4/15 20:26
 */

class Example {
    // 将这个属性的 get() 和 set() 方法委托给了 Delegate 类。
    // Delegate 类实现了 getValue() 和 setValue() 方法，这两个方法分别在属性获取和赋值时被调用。
    var p: String by Delegate()
}

class Delegate {
    // Delegate 类实现了 getValue() 和 setValue() 方法，这两个方法分别在属性获取和赋值时被调用。
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return "$thisRef, 这里委托了 ${property.name} 属性"
    }

    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: String) {
        println("$thisRef 的 ${property.name} 属性赋值为 $value")
    }
}

fun main() {
    // 创建了一个 Example 对象 e，并打印了它的属性 p，然后将 e 的属性 p 赋值为 NEW
    // 在这个过程中，Delegate 的 setValue() 方法被调用，并打印出了赋值的信息
    val e = Example()
    println(e.p)
    e.p = "NEW"
}
```

4. 类委托即一个类中定义的方法实际是调用另一个类的对象的方法来实现的，可以通过将其所有公有成员都委托给指定对象来实现一个接口

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/15 20:42
 */

// 1、定义了一个接口 Base，其中包含一个 print() 方法
interface Base {
    fun print()
}

// 2、定义了一个类 BaseImpl，它实现了 Base 接口，并包含一个整型属性 x
class BaseImpl(val x: Int) : Base {
    override fun print() { print(x) }
}

// 3、定义了一个类 Derived，它通过 by 关键字将自己的 print() 方法委托给了另一个实现了 Base 接口的对象 b。
// 这样就可以实例化 Derived 之后，通过实例化的 Derived 对象调用 Base 中的方法
class Derived(b: Base) : Base by b

fun main() {
    // 4、在 main() 函数中，创建一个 BaseImpl 对象 b
    val b = BaseImpl(10)
    // 5、调用 Derived 对象的 print() 方法。在这个过程中，BaseImpl 的 print() 方法被调用，并打印出了整型属性 x 的值
    Derived(b).print()
}
```

## 10、扩展

1. Kotlin 扩展是一种静态行为，可以对一个类的属性和方法进行扩展，且不需要继承或使用 Decorator 模式。
2. 扩展使我们可以在不修改类 / 不继承类的情况下，向一个类添加新函数或者新属性。
3. 这样可以避免因为继承而带来的复杂性，同时也可以让代码更加简洁易懂。
4. 扩展函数是静态解析的，并不是接收者类型的虚拟成员，在调用扩展函数时，具体被调用的的是哪一个函数，是由调用函数的的对象表达式来决定的，而不是动态的类型决定的
5. 可以为一个不能修改的、来自第三方库中的类编写一个新的函数。 这个新增的函数就像那个原始类本来就有的函数一样，可以用普通的方法调用。 这种机制称为 扩展函数 。
6. 也有扩展属性， 允许为一个已经存在的类添加新的属性；扩展属性允许定义在类或者 kotlin 文件中，不允许定义在函数中。初始化属性因为属性没有后端字段（backing field），所以不允许被初始化，只能由显式提供的 `getter/setter` 定义

```Kotlin
package com.yuehai.kotlin._06_ClassesAndObjects

/**
@author 月海
@create 2023/4/15 21:10
 */

// 定义一个类，在其中定义一个方法
class Play5(var name:String){
    fun game(){
        println("玩${name}游戏")
    }
}

// 给类 Play5 添加一个 sleep 方法
fun Play5.sleep(){
    // 这个 this 关键字在扩展函数内部对应到接收者对象，即类 Play5
    println("睡${this.name}")
}

// 扩展属性；初始化属性因为属性没有后端字段（backing field），所以不允许被初始化，只能由显式提供的 getter/setter 定义
// val Foo.bar = 1 这种直接复制是不可以的，扩展属性不能有初始化器
var Play5.age:Int
    get() = 14
    set(value) {
        // 好像不能修改扩展属性的值
        this.name = "言"
        println("想要修改 age：${value}")
    }

fun main() {
    // 实例化 Play 类
    val play5 = Play5("月海")
    // 调用 game方法
    play5.game()
    // 调用 sleep
    play5.sleep()
    // 调用 age 属性
    println(play5.age)

    // 设置 age 属性
    play5.age = 14
    // 调用 age 属性
    println(play5.age)
    println(play5.name)
}
```

```Kotlin
玩月海游戏
睡月海
14
想要修改 age：14
14
言

进程已结束,退出代码0
```

# 七、`Kotlin` 泛型

## 1、泛型的使用

1. 泛型，即 "参数化类型"，将类型参数化，可以用在类，接口，方法上。
2. 与 Java 一样，Kotlin 也提供泛型，为类型安全提供保证，消除类型强转的烦恼。
3. Kotlin 的泛型与 Java 一样，都是一种语法糖，即只在源代码中有泛型定义，到了class级别就被擦除了。 
4. 泛型（Generics）其实就是把类型参数化，真正的名字叫做类型参数，它的引入给强类型编程语言加入了更强的灵活性

```Kotlin
package com.yuehai.kotlin._07_Genericity

/**
@author 月海
@create 2023/4/15 16:18
 */


// 泛型接口：定义泛型类型，是在类型名之后、主构造函数之前用尖括号括起的大写字母类型参数指定
interface Drinks<T> {
    fun taste(): T
    fun price(t: T)
}

// 泛型类
// 定义泛型类型字段，可以完整地写明类型参数，如果编译器可以自动推定类型参数，也可以省略类型参数
abstract class Color<T>(var t: T/*泛型字段*/) {
    abstract fun printColor()
}
class Blue {
    val color = "blue"
}
class BlueColor(t: Blue) : Color<Blue>(t) {
    override fun printColor() {
        println("color:${t.color}")
    }

}

// 泛型方法：Kotlin 泛型方法的声明与 Java 相同，类型参数要放在方法名的前面
fun <T> fromJson(json: String, tClass: Class<T>): T? {
    /*获取T的实例*/
    val t: T? = tClass.newInstance()
    return t
}
```

## 2、泛型约束

1. 我们可以使用泛型约束来设定一个给定参数允许使用的类型。
2. Kotlin 中使用 `:` 对泛型的类型上限进行约束。默认的上界是 `Any?`

```Kotlin
package com.yuehai.kotlin._07_Genericity

/**
@author 月海
@create 2023/4/15 16:39
 */

// 最常见的约束是上界(upper bound)：
fun <T : Comparable<T>> sort(list: List<T>) {
    println("排完序了")
}

// 对于多个上界约束条件，可以用 where 子句：
fun <T> copyWhenGreater(list: List<T>, threshold: T):
    List<String>
    // CharSequence： char 值的可读序列
    where T : CharSequence,
          T : Comparable<T> {
    return list.filter { it > threshold }.map { it.toString() }
}

fun main() {
    // Comparable 的子类型可以替代 T。 例如:
    // OK。Int 是 Comparable<Int> 的子类型
    sort(listOf(1, 2, 3))
    // 错误：HashMap<Int, String> 不是 Comparable<HashMap<Int, String>> 的子类型
    // sort(listOf(HashMap<Int, String>()))
}
```

# 八、`Kotlin` 协程

## 1、Kotlin 协程

1. Kotlin 协程提供了一种全新处理并发的方式，你可以在 Android 平台上使用它来简化异步执行的代码。
2. 协程从 Kotlin 1.3 版本开始引入，但这一概念在编程世界诞生的黎明之际就有了，最早使用协程的编程语言可以追溯到 1967 年的 Simula 语言。
3. 在过去几年间，协程这个概念发展势头迅猛，现已经被诸多主流编程语言采用，比如 Javascript、C#、Python、Ruby 以及 Go 等。
4. Kotlin 协程是基于来自其他语言的既定概念
5. Google 官方推荐将 Kotlin 协程作为在 Android 上进行异步编程的解决方案，值得关注的功能点包括：
	1. 轻量：可以在单个线程上运行多个协程，因为协程支持挂起，不会使正在运行协程的线程阻塞。挂起比阻塞节省内存，且支持多个并行操作
	2. 内存泄露更少：使用结构化并发机制在一个作用域内执行多个操作
	3. 内置取消支持：取消功能会自动通过正在运行的协程层次结构传播
	4. Jetpack 集成：许多 Jetpack 库都包含提供全面协程支持的扩展。某些库还提供自己的协程作用域，可供你用于结构化并发
6. 如果是用于 Android 平台的话，可以只引用以下的 `coroutines-android`，当中已经包含了 `coroutines-core`

```Kotlin
implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.2'
implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2'
```

7. 引入依赖，打开 app 目录下的 `build.gradle` 文件，在 中添加依赖：

![](attachments/Pasted%20image%2020230416140807.png)

```Kotlin
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    namespace 'com.yuehai.kotlin'
    compileSdk 32

    defaultConfig {
        applicationId "com.yuehai.kotlin"
        minSdk 28
        targetSdk 32
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = '1.8'
    }
}

dependencies {

    implementation 'androidx.core:core-ktx:1.7.0'
    implementation 'androidx.appcompat:appcompat:1.4.1'
    implementation 'com.google.android.material:material:1.5.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.3'
    implementation 'junit:junit:4.13.1'
    testImplementation 'junit:junit:4.13.2'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
    // 协程
    implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.2'
    implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2'
}
```

## 2、第一个协程

1. 协程可以称为 轻量级线程。Kotlin 协程在 CoroutineScope 的上下文中通过 launch、async 等 协程构造器（CoroutineBuilder）来声明并启动
2. 在下面的例子中，通过 `GlobalScope`（全局作用域）启动了一个协程，在延迟一秒后输出一行日志。从输出结果可以看出来，启动的协程是运行在协程内部的线程池中。虽然从表现结果上来看，启动一个协程类似于我们直接使用 `Thread` 来执行耗时任务，但实际上协程和线程有着本质上的区别。通过使用协程，可以极大的提高线程的并发效率，避免以往的嵌套回调地狱，极大提高了代码的可读性
3. 代码涉及到了协程的四个基础概念：
	1. `suspend function`：即挂起函数，`delay()` 就是协程库提供的一个用于实现非阻塞式延时的挂起函数
	2. `CoroutineScope`：即协程作用域，`GlobalScope` 是 `CoroutineScope` 的一个实现类，用于指定协程的作用范围，可用于管理多个协程的生命周期，所有协程都需要通过 `CoroutineScope` 来启动
	3. `CoroutineContext`：即协程上下文，包含多种类型的配置参数。`Dispatchers.IO` 就是 `CoroutineContext` 这个抽象概念的一种实现，用于指定协程的运行载体，即用于指定协程要运行在哪类线程上
	4. `CoroutineBuilder`：即协程构建器，协程在 `CoroutineScope` 的上下文中通过 `launch`、`async` 等协程构建器来进行声明并启动。`launch`、`async` 均被声明为 `CoroutineScope` 的扩展方法

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 13:55
 */

@OptIn(DelicateCoroutinesApi::class)
fun main() {
    GlobalScope.launch(context = Dispatchers.IO) {
        // 延时一秒
        delay(1000)
        log("launch")
    }
    // 主动休眠两秒，防止 JVM 过快退出
    Thread.sleep(2000)
    log("end")
}

private fun log(msg: Any?) = println("[${Thread.currentThread().name}] $msg")
```

## 3、`suspend`

1. 如果上述例子试图直接在 `GlobalScope` 外调用 `delay()` 函数的话，IDE 就会提示一个错误：`Suspend function 'delay' should be called only from a coroutine or another suspend function`。意思是：`delay()` 函数是一个挂起函数，只能由协程或者由其它挂起函数来调用
2. `delay()` 函数就使用了 `suspend` 进行修饰，用 `suspend` 修饰的函数就是挂起函数：源码

```Kotlin
/**
 * Delays coroutine for a given time without blocking a thread and resumes it after a specified time.
 *
 * This suspending function is cancellable.
 * If the [Job] of the current coroutine is cancelled or completed while this suspending function is waiting, this function
 * immediately resumes with [CancellationException].
 * There is a **prompt cancellation guarantee**. If the job was cancelled while this function was
 * suspended, it will not resume successfully. See [suspendCancellableCoroutine] documentation for low-level details.
 *
 * If you want to delay forever (until cancellation), consider using [awaitCancellation] instead.
 *
 * Note that delay can be used in [select] invocation with [onTimeout][SelectBuilder.onTimeout] clause.
 *
 * Implementation note: how exactly time is tracked is an implementation detail of [CoroutineDispatcher] in the context.
 * @param timeMillis time in milliseconds.
 */
public suspend fun delay(timeMillis: Long) {
    if (timeMillis <= 0) return // don't delay
    return suspendCancellableCoroutine sc@ { cont: CancellableContinuation<Unit> ->
        // if timeMillis == Long.MAX_VALUE then just wait forever like awaitCancellation, don't schedule.
        if (timeMillis < Long.MAX_VALUE) {
            cont.context.delay.scheduleResumeAfterDelay(timeMillis, cont)
        }
    }
}
```

3. 在网上看关于协程的文章的时候，应该经常会看到这么一句话：**挂起函数不会阻塞其所在线程，而是会将协程挂起，在特定的时候才再恢复执行**
4. 对于这句话我的理解是：`delay()` 函数类似于 Java 中的 `Thread.sleep()`，而之所以说 `delay()` 函数是非阻塞的，是因为它和单纯的线程休眠有着本质的区别。
5. 例如，当在 `ThreadA` 上运行的 `CoroutineA` 调用了 `delay(1000L)` 函数指定延迟一秒后再运行，`ThreadA` 会转而去执行 `CoroutineB`，等到一秒后再来继续执行 `CoroutineA`。所以，`ThreadA` 并不会因为 `CoroutineA` 的延时而阻塞，而是能继续去执行其它任务，所以挂起函数并不会阻塞其所在线程，这样就极大地提高了线程的并发灵活度，最大化了线程的利用效率。
6. 而如果是使用 `Thread.sleep()` 的话，线程就只能干等着而不能去执行其它任务，降低了线程的利用效率
7. 协程是运行于线程上的，一个线程可以运行多个（几千上万个）协程。
8. 线程的调度行为是由操作系统来管理的，而协程的调度行为是可以由开发者来指定并由编译器来实现的，协程能够细粒度地控制多个任务的执行时机和执行线程，当线程所执行的当前协程被 `suspend` 后，该线程也可以腾出资源去处理其他任务

## 4、`suspend` 挂起与恢复

1. 协程在常规函数的基础上添加了两项操作用于处理长时间运行的任务，在 `invoke`（或 `call`）和 `return` 之外，协程添加了 `suspend` 和 `resume`：
	1. `suspend`：用于暂停执行当前协程，并保存所有局部变量
	2. `resume`：用于让已暂停的协程从暂停处继续执行
2. `suspend` 函数只能由其它 `suspend` 函数调用，或者是由协程来调用
3. 以下示例展示了一项任务（假设 get 方法是一个网络请求任务）的简单协程实现：

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import android.app.ProgressDialog.show
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 14:28
 */


suspend fun fetchDocs() {
    // 调用 get 方法，会在启动网络请求之前暂停协程
    // 当网络请求完成后，get() 会恢复已暂停的协程，使得主线程协程可以直接拿到网络请求结果而不用使用回调来通知主线程。Retrofit 就是以这种方式来实现对协程的支持
    val result = get("https://developer.android.com")
    println(result)
}

// get() 主体内通过调用 withContext(Dispatchers.IO) 创建了一个在 IO 线程池中运行的代码块，在该块内的任何代码都始终通过 IO 调度器执行
suspend fun get(url: String) = withContext(Dispatchers.IO) {
    println("进行请求")
    return@withContext "返回数据"
}

suspend fun main() {
    fetchDocs()
}
```

4. 在上面的示例中，`get()` 仍在主线程上被调用，但它会在启动网络请求之前暂停协程。`get()` 主体内通过调用 `withContext(Dispatchers.IO)` 创建了一个在 IO 线程池中运行的代码块，在该块内的任何代码都始终通过 IO 调度器执行。
5. 当网络请求完成后，`get()` 会恢复已暂停的协程，使得主线程协程可以直接拿到网络请求结果而不用使用回调来通知主线程。`Retrofit` 就是以这种方式来实现对协程的支持
6. Kotlin 使用**堆栈帧**来管理要运行哪个函数以及所有局部变量。暂停协程时，系统会复制并保存当前的堆栈帧以供稍后使用。恢复时，会将堆栈帧从其保存的位置复制回来，然后函数再次开始运行。虽然代码可能看起来像普通的顺序阻塞请求，协程也能确保网络请求不会阻塞主线程
7. 在主线程进行的**暂停协程**和**恢复协程**的两个操作，既实现了将耗时任务交由后台线程完成，保障了主线程安全，又以同步代码的方式完成了实际上的多线程异步调用。可以说，在 Android 平台上协程主要就用来解决两个问题：
	1. 处理耗时任务 (Long running tasks)，这种任务常常会阻塞主线程
	2. 保证主线程安全 (Main-safety)，即确保安全地从主线程调用任何 suspend 函数

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 14:28
 */

suspend fun fetchDocs() {
    // 调用 get 方法，会在启动网络请求之前暂停协程
    // 当网络请求完成后，get() 会恢复已暂停的协程，使得主线程协程可以直接拿到网络请求结果而不用使用回调来通知主线程。Retrofit 就是以这种方式来实现对协程的支持
    val result = get("https://developer.android.com")
    println(result)
}

// get() 主体内通过调用 withContext(Dispatchers.IO) 创建了一个在 IO 线程池中运行的代码块，在该块内的任何代码都始终通过 IO 调度器执行
suspend fun get(url: String) = withContext(Dispatchers.IO) {}

```

## 5、`CoroutineScope`

### ①、简介

1. `CoroutineScope` 即**协程作用域**，用于对协程进行追踪。
2. 如果我们启动了多个协程但是没有一个可以对其进行统一管理的途径的话，就会导致我们的代码臃肿杂乱，甚至发生内存泄露或者任务泄露。
3. 为了确保所有的协程都会被追踪，Kotlin 不允许在没有 `CoroutineScope` 的情况下启动协程。`CoroutineScope` 可被看作是一个具有超能力的 `ExecutorService` 的轻量级版本。它能启动协程，同时这个协程还具备上文所说的 `suspend` 和 `resume` 的优势
4. 所有的协程都需要通过 `CoroutineScope` 来启动，它会跟踪通过 `launch` 或 `async` 创建的所有协程，你可以随时调用 `scope.cancel()` 取消正在运行的协程。`CoroutineScope` 本身并不运行协程，它只是确保你不会失去对协程的追踪，即使协程被挂起也是如此。
5. 在 Android 中，某些 ktx 库为某些生命周期类提供了自己的 `CoroutineScope`，例如，`ViewModel` 有 `viewModelScope`，`Lifecycle` 有 `lifecycleScope`
6. CoroutineScope 大体上可以分为三种：
	1. `GlobalScope`：即全局协程作用域，在这个范围内启动的协程可以一直运行直到应用停止运行。`GlobalScope` 本身不会阻塞当前线程，且启动的协程相当于守护线程，不会阻止 JVM 结束运行
	2. `runBlocking`：一个顶层函数，和 `GlobalScope` 不一样，它会阻塞当前线程直到其内部所有相同作用域的协程执行结束
	3. 自定义 `CoroutineScope`：可用于实现主动控制协程的生命周期范围，对于 Android 开发来说最大意义之一就是可以在 `Activity`、`Fragment`、`ViewModel` 等具有生命周期的对象中按需取消所有协程任务，从而确保生命周期安全，避免内存泄露

### ②、`GlobalScope`

1. GlobalScope 属于**全局作用域**，这意味着通过 `GlobalScope` 启动的协程的生命周期只受整个应用程序的生命周期的限制，只要整个应用程序还在运行且协程的任务还未结束，协程就可以一直运行
2. `GlobalScope` 不会阻塞其所在线程，所以以下代码中主线程的日志会早于 `GlobalScope` 内部输出日志。
3. 此外，`GlobalScope` 启动的协程相当于守护线程，不会阻止 `JVM` 结束运行，所以如果将主线程的休眠时间改为三百毫秒的话，就不会看到 `launch A` 输出日志
4. `GlobalScope.launch` 会创建一个顶级协程，尽管它很轻量级，但在运行时还是会消耗一些内存资源，且可以一直运行直到整个应用程序停止（只要任务还未结束），这可能会导致内存泄露，所以在日常开发中应该谨慎使用 `GlobalScope`

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

/**
@author 月海
@create 2023/4/16 15:07
 */
fun main() {
    log("start")

    // 创建协程 1
    GlobalScope.launch {

        // 创建协程 1 中的协程 1.1
        launch {
            delay(400)
            log("launch A")
        }

        // 创建协程 1 中的协程 1.2
        launch {
            delay(300)
            log("launch B")
        }

        // 协程 1 中非创建协程代码
        log("GlobalScope")
    }

    log("end")
    Thread.sleep(500)
}
```

```Kotlin
[main] start
[main] end
[DefaultDispatcher-worker-2] GlobalScope

进程已结束,退出代码0
```

### ③、`runBlocking`

1. 也可以使用 `runBlocking` 这个顶层函数来启动协程，`runBlocking` 函数的第二个参数即协程的执行体，该参数被声明为 `CoroutineScope` 的扩展函数，因此执行体就包含了一个隐式的 `CoroutineScope`，所以在 `runBlocking` 内部可以来直接启动协程

```Kotlin
/**
 * Runs a new coroutine and **blocks** the current thread _interruptibly_ until its completion.
 * This function should not be used from a coroutine. It is designed to bridge regular blocking code
 * to libraries that are written in suspending style, to be used in `main` functions and in tests.
 *
 * The default [CoroutineDispatcher] for this builder is an internal implementation of event loop that processes continuations
 * in this blocked thread until the completion of this coroutine.
 * See [CoroutineDispatcher] for the other implementations that are provided by `kotlinx.coroutines`.
 *
 * When [CoroutineDispatcher] is explicitly specified in the [context], then the new coroutine runs in the context of
 * the specified dispatcher while the current thread is blocked. If the specified dispatcher is an event loop of another `runBlocking`,
 * then this invocation uses the outer event loop.
 *
 * If this blocked thread is interrupted (see [Thread.interrupt]), then the coroutine job is cancelled and
 * this `runBlocking` invocation throws [InterruptedException].
 *
 * See [newCoroutineContext][CoroutineScope.newCoroutineContext] for a description of debugging facilities that are available
 * for a newly created coroutine.
 *
 * @param context the context of the coroutine. The default value is an event loop on the current thread.
 * @param block the coroutine code.
 */
@Throws(InterruptedException::class)
public fun <T> runBlocking(context: CoroutineContext = EmptyCoroutineContext, block: suspend CoroutineScope.() -> T): T {
    contract {
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    }
    val currentThread = Thread.currentThread()
    val contextInterceptor = context[ContinuationInterceptor]
    val eventLoop: EventLoop?
    val newContext: CoroutineContext
    if (contextInterceptor == null) {
        // create or use private event loop if no dispatcher is specified
        eventLoop = ThreadLocalEventLoop.eventLoop
        newContext = GlobalScope.newCoroutineContext(context + eventLoop)
    } else {
        // See if context's interceptor is an event loop that we shall use (to support TestContext)
        // or take an existing thread-local event loop if present to avoid blocking it (but don't create one)
        eventLoop = (contextInterceptor as? EventLoop)?.takeIf { it.shouldBeProcessedFromContext() }
            ?: ThreadLocalEventLoop.currentOrNull()
        newContext = GlobalScope.newCoroutineContext(context)
    }
    val coroutine = BlockingCoroutine<T>(newContext, currentThread, eventLoop)
    coroutine.start(CoroutineStart.DEFAULT, coroutine, block)
    return coroutine.joinBlocking()
}
```

2. runBlocking 的一个方便之处就是：只有当内部相同作用域的所有协程都运行结束后，声明在 `runBlocking` 之后的代码才能执行，<font color="#ff0000">即 `runBlocking` 会阻塞其所在线程</font>
3. 看以下代码。`runBlocking` 内部启动的两个协程会各自做耗时操作，从输出结果可以看出来两个协程还是在交叉并发执行，且 `runBlocking` 会等到两个协程都执行结束后才会退出，外部的日志输出结果有明确的先后顺序。
4. 即 `runBlocking` 内部启动的协程是非阻塞式的，但 `runBlocking` 阻塞了其所在线程。
5. 此外，`runBlocking` 只会等待相同作用域的协程完成才会退出，而不会等待 `GlobalScope` 等其它作用域启动的协程

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

/**
@author 月海
@create 2023/4/16 15:19
 */
fun main() {
    log("start")

    // 创建 runBlocking 协程 1
    runBlocking {
        // 创建 runBlocking 协程 1 中的 runBlocking 协程 1.1
        launch {
            repeat(3) {
                delay(100)
                log("launchA - $it")
            }
        }

        // 创建 runBlocking 协程 1 中的 runBlocking 协程 1.2
        launch {
            repeat(3) {
                delay(100)
                log("launchB - $it")
            }
        }

        // 创建 runBlocking 协程 1 中的 GlobalScope 协程 1.3
        GlobalScope.launch {

            repeat(3) {
                delay(90)
                log("GlobalScope - $it")
            }
        }
    }

    log("end")
}
```

```Kotlin
[main] start
[DefaultDispatcher-worker-1] GlobalScope - 0
[main] launchA - 0
[main] launchB - 0
[DefaultDispatcher-worker-1] GlobalScope - 1
[main] launchA - 1
[main] launchB - 1
[DefaultDispatcher-worker-1] GlobalScope - 2
[main] launchA - 2
[main] launchB - 2
[main] end

进程已结束,退出代码0
```

6. 所以说，`runBlocking` 本身带有阻塞线程的意味，但其内部运行的协程又是非阻塞的，需要明白这两者的区别
7. 基于是否会阻塞线程的区别，以下代码中 `runBlocking` 会早于 `GlobalScope` 输出日志

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 15:32
 */
fun main() {
    // 创建 runBlocking 协程 1
    runBlocking {
        delay(1000)
        log("runBlocking -- 01")
    }

    // 创建 GlobalScope 协程 2
    GlobalScope.launch(Dispatchers.IO) {
        delay(600)
        log("GlobalScope")
    }

    // 创建 runBlocking 协程 3
    runBlocking {
        delay(500)
        log("runBlocking -- 02")
    }

    //主动休眠两百毫秒，使得和 runBlocking 加起来的延迟时间多于一千毫秒
    Thread.sleep(200)
    log("after sleep")
}
```

```Kotlin
[main] runBlocking -- 01
[main] runBlocking -- 02
[DefaultDispatcher-worker-1] GlobalScope
[main] after sleep

进程已结束,退出代码0
```

### ④、`coroutineScope`

1. `coroutineScope` 函数用于创建一个独立的协程作用域，直到所有启动的协程都完成后才结束自身。
2. `runBlocking` 和 `coroutineScope` 看起来很像，因为它们都需要等待其内部所有相同作用域的协程结束后才会结束自己。
3. 两者的主要区别在于 `runBlocking` 方法会阻塞当前线程，而 `coroutineScope` 不会，而是会挂起并释放底层线程以供其它协程使用。
4. 基于这个差别，`runBlocking` 是一个普通函数，而 `coroutineScope` 是一个挂起函数

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

/**
@author 月海
@create 2023/4/16 15:40
 */
fun main(){

    runBlocking {

        launch {
            delay(100)
            log("Task from runBlocking")
        }

        coroutineScope {
            launch {
                delay(500)
                log("Task from nested launch")
            }

            delay(50)
            log("Task from coroutine scope")
        }

        log("Coroutine scope is over")
    }

}
```

```Kotlin
[main] Task from coroutine scope
[main] Task from runBlocking
[main] Task from nested launch
[main] Coroutine scope is over

进程已结束,退出代码0
```

### ⑤、`supervisorScope`

1. `supervisorScope` 函数用于创建一个使用了 `SupervisorJob` 的 `coroutineScope`，该作用域的特点就是抛出的异常不会连锁取消同级协程和父协程

```
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.*
/**
@author 月海
@create 2023/4/16 15:47
 */
fun main() = runBlocking {

    launch {
        delay(100)
        log("Task from runBlocking")
    }

    supervisorScope {

        launch {
            delay(500)
            log("Task throw Exception")
            throw Exception("failed")
        }

        launch {
            delay(600)
            log("Task from nested launch")
        }
    }

    log("Coroutine scope is over")
}
```

```Kotlin
[main] Task from runBlocking
[main] Task throw Exception
Exception in thread "main" java.lang.Exception: failed
	at com.yuehai.kotlin._08_Coroutines._05_04_supervisorScopeKt$main$1$2$1.invokeSuspend(_05_04_supervisorScope.kt:20)
	at kotlin.coroutines.jvm.internal.BaseContinuationImpl.resumeWith(ContinuationImpl.kt:33)
	at kotlinx.coroutines.DispatchedTaskKt.resume(DispatchedTask.kt:234)
	at kotlinx.coroutines.DispatchedTaskKt.dispatch(DispatchedTask.kt:166)
	at kotlinx.coroutines.CancellableContinuationImpl.dispatchResume(CancellableContinuationImpl.kt:397)
	at kotlinx.coroutines.CancellableContinuationImpl.resumeImpl(CancellableContinuationImpl.kt:431)
	at kotlinx.coroutines.CancellableContinuationImpl.resumeImpl$default(CancellableContinuationImpl.kt:420)
	at kotlinx.coroutines.CancellableContinuationImpl.resumeUndispatched(CancellableContinuationImpl.kt:518)
	at kotlinx.coroutines.EventLoopImplBase$DelayedResumeTask.run(EventLoop.common.kt:489)
	at kotlinx.coroutines.EventLoopImplBase.processNextEvent(EventLoop.common.kt:274)
	at kotlinx.coroutines.BlockingCoroutine.joinBlocking(Builders.kt:85)
	at kotlinx.coroutines.BuildersKt__BuildersKt.runBlocking(Builders.kt:59)
	at kotlinx.coroutines.BuildersKt.runBlocking(Unknown Source)
	at kotlinx.coroutines.BuildersKt__BuildersKt.runBlocking$default(Builders.kt:38)
	at kotlinx.coroutines.BuildersKt.runBlocking$default(Unknown Source)
	at com.yuehai.kotlin._08_Coroutines._05_04_supervisorScopeKt.main(_05_04_supervisorScope.kt:8)
	at com.yuehai.kotlin._08_Coroutines._05_04_supervisorScopeKt.main(_05_04_supervisorScope.kt)
[main] Task from nested launch
[main] Coroutine scope is over

进程已结束,退出代码0
```

### ⑥、自定义 CoroutineScope

1. 假设我们在 `Activity` 中先后启动了多个协程用于执行异步耗时操作，那么当 `Activity` 退出时，必须取消所有协程以避免内存泄漏。
2. 我们可以通过保留每一个 `Job` 引用然后在 `onDestroy` 方法里来手动取消，但这种方式相对来说会比较繁琐和低效。`kotlinx.coroutines` 提供了 `CoroutineScope` 来管理多个协程的生命周期
3. 我们可以通过创建与 `Activity` 生命周期相关联的协程作用域来管理协程的生命周期。`CoroutineScope` 的实例可以通过 `CoroutineScope()` 或 `MainScope()` 的工厂函数来构建。
4. 前者创建通用作用域，后者创建 `UI` 应用程序的作用域并使用 `Dispatchers.Main` 作为默认的调度器

```Kotlin
class Activity {

    private val mainScope = MainScope()

    fun onCreate() {
        mainScope.launch {
            repeat(5) {
                delay(1000L * it)
            }
        }
    }

    fun onDestroy() {
        mainScope.cancel()
    }

}
```

5. 或者，我们可以通过委托模式来让 `Activity` 实现 `CoroutineScope` 接口，从而可以在 `Activity` 内直接启动协程而不必显示地指定它们的上下文，并且在 `onDestroy()` 中自动取消所有协程

```Kotlin
package com.yuehai.kotlin._08_Coroutines

import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 15:50
 */
class Activity : CoroutineScope by CoroutineScope(Dispatchers.Default) {

    fun onCreate() {
        launch {
            repeat(5) {
                delay(200L * it)
                log(it)
            }
        }
        log("Activity Created")
    }

    fun onDestroy() {
        cancel()
        log("Activity Destroyed")
    }

}

fun main() = runBlocking {
    val activity = Activity()
    activity.onCreate()
    delay(1000)
    activity.onDestroy()
    delay(1000)
}
```

6. 从输出结果可以看出，当回调了`onDestroy()` 方法后协程就不会再输出日志了

```Kotlin
[main] Activity Created
[DefaultDispatcher-worker-2] 0
[DefaultDispatcher-worker-2] 1
[DefaultDispatcher-worker-2] 2
[main] Activity Destroyed

进程已结束,退出代码0
```

7. 已取消的作用域无法再创建协程。因此，仅当控制其生命周期的类被销毁时，才应调用 `scope.cancel()`。例如，使用 `viewModelScope` 时， `ViewModel` 会在自身的 `onCleared()` 方法中自动取消作用域

## 6、`CoroutineBuilder`

### ①、`launch`

1. 看下 `launch` 函数的方法签名。`launch` 是一个作用于 `CoroutineScope` 的扩展函数，用于在不阻塞当前线程的情况下启动一个协程，并返回对该协程任务的引用，即 `Job` 对象

```Kotlin
/**
 * Launches a new coroutine without blocking the current thread and returns a reference to the coroutine as a [Job].
 * The coroutine is cancelled when the resulting job is [cancelled][Job.cancel].
 *
 * The coroutine context is inherited from a [CoroutineScope]. Additional context elements can be specified with [context] argument.
 * If the context does not have any dispatcher nor any other [ContinuationInterceptor], then [Dispatchers.Default] is used.
 * The parent job is inherited from a [CoroutineScope] as well, but it can also be overridden
 * with a corresponding [context] element.
 *
 * By default, the coroutine is immediately scheduled for execution.
 * Other start options can be specified via `start` parameter. See [CoroutineStart] for details.
 * An optional [start] parameter can be set to [CoroutineStart.LAZY] to start coroutine _lazily_. In this case,
 * the coroutine [Job] is created in _new_ state. It can be explicitly started with [start][Job.start] function
 * and will be started implicitly on the first invocation of [join][Job.join].
 *
 * Uncaught exceptions in this coroutine cancel the parent job in the context by default
 * (unless [CoroutineExceptionHandler] is explicitly specified), which means that when `launch` is used with
 * the context of another coroutine, then any uncaught exception leads to the cancellation of the parent coroutine.
 *
 * See [newCoroutineContext] for a description of debugging facilities that are available for a newly created coroutine.
 *
 * @param context additional to [CoroutineScope.coroutineContext] context of the coroutine.
 * @param start coroutine start option. The default value is [CoroutineStart.DEFAULT].
 * @param block the coroutine code which will be invoked in the context of the provided scope.
 **/
public fun CoroutineScope.launch(
    context: CoroutineContext = EmptyCoroutineContext,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope.() -> Unit
): Job {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy)
        LazyStandaloneCoroutine(newContext, block) else
        StandaloneCoroutine(newContext, active = true)
    coroutine.start(start, coroutine, block)
    return coroutine
}
```

2. `launch` 函数共包含三个参数：
	1. `context`：用于指定协程的上下文
	2. `start`：用于指定协程的启动方式，默认值为 `CoroutineStart.DEFAULT`，即协程会在声明的同时就立即进入等待调度的状态，即可以立即执行的状态。可以通过将其设置为 `CoroutineStart.LAZY` 来实现延迟启动，即懒加载
	3. `block`：用于传递协程的执行体，即希望交由协程执行的任务
3. 可以看到 launchA 和 launchB 是并行交叉执行的

```Kotlin
package com.yuehai.kotlin._08_Coroutines._06_CoroutineBuilder

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 16:04
 */
fun main() = runBlocking {
    val launchA = launch {
        repeat(3) {
            delay(100)
            log("launchA - $it")
        }
    }
    val launchB = launch {
        repeat(3) {
            delay(100)
            log("launchB - $it")
        }
    }
}
```

```Kotlin
[main] launchA - 0
[main] launchB - 0
[main] launchA - 1
[main] launchB - 1
[main] launchA - 2
[main] launchB - 2

进程已结束,退出代码0
```

### ②、`Job`

1. `Job` 是协程的句柄。
2. 使用 `launch` 或 `async` 创建的每个协程都会返回一个 `Job` 实例，该实例唯一标识协程并管理其生命周期。
3. `Job` 是一个接口类型，这里列举 `Job` 几个比较有用的属性和函数

```Kotlin
//当 Job 处于活动状态时为 true
//如果 Job 未被取消或没有失败，则均处于 active 状态
public val isActive: Boolean

//当 Job 正常结束或者由于异常结束，均返回 true
public val isCompleted: Boolean

//当 Job 被主动取消或者由于异常结束，均返回 true
public val isCancelled: Boolean

//启动 Job
//如果此调用的确启动了 Job，则返回 true
//如果 Job 调用前就已处于 started 或者是 completed 状态，则返回 false 
public fun start(): Boolean

//用于取消 Job，可同时通过传入 Exception 来标明取消原因
public fun cancel(cause: CancellationException? = null)

//阻塞等待直到此 Job 结束运行
public suspend fun join()

//当 Job 结束运行时（不管由于什么原因）回调此方法，可用于接收可能存在的运行异常
public fun invokeOnCompletion(handler: CompletionHandler): DisposableHandle
```

4. `Job` 具有以下几种状态值，每种状态对应的属性值各不相同

| State                          | isActive | isCompleted | isCancelled |
| ------------------------------ | -------- | ----------- | ----------- |
| New (optional initial state)   | false    | false       | false       |
| Active (default initial state) | true     | false       | false       |
| Completing (transient state)   | true     | false       | false       |
| Cancelling (transient state)   | false    | false       | true        |
|Cancelled (final state)|false|true|true|
|Completed (final state)|false|true|false|


```Kotlin
package com.yuehai.kotlin._08_Coroutines._06_CoroutineBuilder

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 16:12
 */
fun main() {
    // 将协程设置为延迟启动
    val job = GlobalScope.launch(start = CoroutineStart.LAZY) {
        for (i in 0..100) {
            // 每循环一次均延迟一百毫秒
            delay(100)
        }
    }
    
    job.invokeOnCompletion {
        log("invokeOnCompletion：$it")
    }
    log("1. job.isActive：${job.isActive}")
    log("1. job.isCancelled：${job.isCancelled}")
    log("1. job.isCompleted：${job.isCompleted}")

    job.start()

    log("2. job.isActive：${job.isActive}")
    log("2. job.isCancelled：${job.isCancelled}")
    log("2. job.isCompleted：${job.isCompleted}")

    // 休眠四百毫秒后再主动取消协程
    Thread.sleep(400)
    job.cancel(CancellationException("test"))

    //休眠四百毫秒防止JVM过快停止导致 invokeOnCompletion 来不及回调
    Thread.sleep(400)

    log("3. job.isActive：${job.isActive}")
    log("3. job.isCancelled：${job.isCancelled}")
    log("3. job.isCompleted：${job.isCompleted}")
}
```

```Kotlin
[main] 1. job.isActive：false
[main] 1. job.isCancelled：false
[main] 1. job.isCompleted：false
[main] 2. job.isActive：true
[main] 2. job.isCancelled：false
[main] 2. job.isCompleted：false
[DefaultDispatcher-worker-1] invokeOnCompletion：java.util.concurrent.CancellationException: test
[main] 3. job.isActive：false
[main] 3. job.isCancelled：true
[main] 3. job.isCompleted：true

进程已结束,退出代码0
```

### ③、`async`

1. 看下 `async` 函数的方法签名。`async` 也是一个作用于 `CoroutineScope` 的扩展函数，和 `launch` 的区别主要就在于：`async` 可以返回协程的执行结果，而 `launch` 不行
2. 通过 `await(`) 方法可以拿到 `async` 协程的执行结果，可以看到两个协程的总耗时是远少于七秒的，总耗时基本等于耗时最长的协程
3. 由于 `launch` 和 `async` 仅能够在 `CouroutineScope` 中使用，所以任何创建的协程都会被该 `scope` 追踪。`Kotlin` 禁止创建不能够被追踪的协程，从而避免协程泄漏

```Kotlin
package com.yuehai.kotlin._08_Coroutines._06_CoroutineBuilder

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis

/**
@author 月海
@create 2023/4/16 16:17
 */
fun main() {
    val time = measureTimeMillis {

        runBlocking {

            val asyncA = async {
                delay(3000)
                1
            }

            val asyncB = async {
                delay(4000)
                2
            }

            log(asyncA.await() + asyncB.await())
        }
    }

    log(time)
}
```

```Kotlin
[main] 3
[main] 4110

进程已结束,退出代码0
```

### ④、`async` 错误用法

1. 修改上述代码，可以发现两个协程的总耗时就会变为七秒左右

```Kotlin
package com.yuehai.kotlin._08_Coroutines._06_CoroutineBuilder

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis

/**
@author 月海
@create 2023/4/16 16:19
 */
fun main() {
    val time = measureTimeMillis {

        runBlocking {

            val asyncA = async(start = CoroutineStart.LAZY) {
                delay(3000)
                1
            }

            val asyncB = async(start = CoroutineStart.LAZY) {
                delay(4000)
                2
            }

            log(asyncA.await() + asyncB.await())
        }
    }

    log(time)
}
```

```Kotlin
[main] 3
[main] 7118

进程已结束,退出代码0
```

2. 会造成这不同区别是因为 `CoroutineStart.LAZY` 不会主动启动协程，而是直到调用 `async.await()` 或者`async.satrt()` 后才会启动（即懒加载模式），所以 `asyncA.await() + asyncB.await()` 会导致两个协程其实是在顺序执行。
3. 而默认值 `CoroutineStart.DEFAULT` 参数会使得协程在声明的同时就被启动了（实际上还需要等待被调度执行，但可以看做是立即就执行了），所以此时调用第一个 `async.await()` 时两个协程其实都是处于运行状态，所以总耗时就是四秒左右
4. 此时可以通过先调用 `start()` 再调用 `await()` 来实现第一个例子的效果

```Kotlin
asyncA.start()
asyncB.start()
log(asyncA.await() + asyncB.await())
```

### ⑤、`async` 并行分解

1. 由 `suspend` 函数启动的所有协程都必须在该函数返回结果时停止，因此你可能需要保证这些协程在返回结果之前完成。
2. 借助 Kotlin 中的结构化并发机制，你可以定义用于启动一个或多个协程的 `coroutineScope`。然后，你可以使用 `await()`（针对单个协程）或 `awaitAll()`（针对多个协程）保证这些协程在从函数返回结果之前完成
3. 假设我们定义一个用于异步获取两个文档的 `coroutineScope`，通过对每个延迟引用调用 `await()`，我们可以保证这两项 `async` 操作在返回值之前完成：

```Kotlin
suspend fun fetchTwoDocs() = coroutineScope {
    val deferredOne = async { fetchDoc(1) }
    val deferredTwo = async { fetchDoc(2) }
    deferredOne.await()
    deferredTwo.await()
}
```

4. 还可以对集合使用 `awaitAll()` 来达到相同效果。虽然 `fetchTwoDocs()` 使用 `async` 启动新协程，但该函数使用 `awaitAll()` 等待启动的协程完成后才会返回结果。
5. 不过，即使我们没有调用 `awaitAll()`，`coroutineScope` 构建器也会等到所有内部协程都完成后才会恢复名为 `fetchTwoDocs` 的协程。
6. 此外，`coroutineScope` 会捕获协程抛出的所有异常，并将其传送给调用方

```Kotlin
suspend fun fetchTwoDocs() = coroutineScope {
    val deferreds = listOf(
        async { fetchDoc(1) },
        async { fetchDoc(2) }
    )
    deferreds.awaitAll()
}
```

### ⑥、`Deferred`

1. `async` 函数的返回值是一个 `Deferred` 对象。
2. `Deferred` 是一个接口类型，继承于 `Job` 接口，所以 `Job` 包含的属性和方法 `Deferred` 都有，其主要是在 `Job` 的基础上扩展了 `await()` 方法

## 7、`CoroutineContext`

- `CoroutineContext` 使用以下元素集定义协程的行为：

1. `Job`：控制协程的生命周期
2. `CoroutineDispatcher`：将任务指派给适当的线程
3. `CoroutineName`：协程的名称，可用于调试
4. `CoroutineExceptionHandler`：处理未捕获的异常

### ①、`Job`

1. 协程中的 `Job` 是其上下文 `CoroutineContext` 中的一部分，可以通过 `coroutineContext[Job]` 表达式从上下文中获取到，我们可以通过控制 `Job` 来控制 `CoroutineScope` 的生命周期

```Kotlin
package com.yuehai.kotlin._08_Coroutines._07_CoroutineContext

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 16:31
 */
val job = Job()

val scope = CoroutineScope(job + Dispatchers.IO)

fun main(): Unit = runBlocking {

    log("job is $job")

    val job = scope.launch {
        try {
            delay(3000)
        } catch (e: CancellationException) {
            log("job is cancelled")
            throw e
        }

        log("end")
    }

    delay(1000)
    log("scope job is ${scope.coroutineContext[Job]}")
    scope.coroutineContext[Job]?.cancel()
}
```

```Kotlin
[main] job is JobImpl{Active}@2b9627bc
[main] scope job is JobImpl{Active}@2b9627bc
[DefaultDispatcher-worker-1] job is cancelled

进程已结束,退出代码0
```

2. 实际上 `CoroutineScope` 的 `isActive` 这个扩展属性只是 `coroutineContext[Job]?.isActive ?: true` 的一种简便写法

```Kotlin
public val CoroutineScope.isActive: Boolean
    get() = coroutineContext[Job]?.isActive ?: true
```

### ②、`CoroutineDispatcher`

1. `CoroutineContext` 包含一个 `CoroutineDispatcher`（协程调度器）用于指定执行协程的目标载体，即 运行于哪个线程。
2. `CoroutineDispatcher` 可以将协程的执行操作限制在特定线程上，也可以将其分派到线程池中，或者让它无限制地运行。所有的协程构造器（如 `launch` 和 `async`）都接受一个可选参数，即 `CoroutineContext` ，该参数可用于显式指定要创建的协程和其它上下文元素所要使用的 `CoroutineDispatcher`
3. 要在主线程之外运行代码，可以指定 Kotlin 协程在 `Default` 或 `IO` 调度程序上执行工作。
4. 在 Kotlin 中，所有协程都必须在 `CoroutineDispatcher` 中运行，即使它们在主线程上运行也是如此。协程可以自行暂停，而 `CoroutineDispatcher` 负责将其恢复
5. Kotlin 协程库提供了四个 `Dispatcher` 用于指定在哪一类线程中执行协程：
	1. `Dispatchers.Default`：默认调度器，适合用于执行占用大量 CPU 资源的任务。例如：对列表排序和解析 JSON
	2. `Dispatchers.IO`：适合用于执行磁盘或网络 I/O 的任务。例如：使用 Room 组件、读写磁盘文件，执行网络请求
	3. `Dispatchers.Unconfined`：对执行协程的线程不做限制，可以直接在当前调度器所在线程上执行
	4. `Dispatchers.Main`：使用此调度程序可用于在 Android 主线程上运行协程，只能用于与界面交互和执行快速工作，例如：更新 UI、调用 `LiveData.setValue`

```Kotlin
package com.yuehai.kotlin._08_Coroutines._07_CoroutineContext

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 16:40
 */
fun main() = runBlocking<Unit> {

    launch {
        log("main runBlocking")
    }

    launch(Dispatchers.Default) {
        log("Default")

        launch(Dispatchers.Unconfined) {
            log("Unconfined 1")
        }
    }

    launch(Dispatchers.IO) {
        log("IO")

        launch(Dispatchers.Unconfined) {
            log("Unconfined 2")
        }
    }

    launch(newSingleThreadContext("MyOwnThread")) {
        log("newSingleThreadContext")

        launch(Dispatchers.Unconfined) {
            log("Unconfined 4")
        }
    }

    launch(Dispatchers.Unconfined) {
        log("Unconfined 3")
    }

    GlobalScope.launch {
        log("GlobalScope")
    }
}
```

```Kotlin
[DefaultDispatcher-worker-1] Default
[DefaultDispatcher-worker-2] IO
[DefaultDispatcher-worker-1] Unconfined 1
[DefaultDispatcher-worker-2] Unconfined 2
[main] Unconfined 3
[DefaultDispatcher-worker-2] GlobalScope
[main] main runBlocking
[MyOwnThread] newSingleThreadContext
[MyOwnThread] Unconfined 4

进程已结束,退出代码0
```

6. `launch` 在不执行 `Dispatchers` 的情况下使用时，它从外部的协程作用域继承上下文和调度器，即和 `runBlocking` 保持一致，均在 `main` 线程执行
7. `IO` 和 `Default` 均依靠后台线程池来执行
8. `Unconfined` 则不限定具体的线程类型，当前调度器在哪个线程，就在该线程上进行执行，因此上述例子中每个 `Unconfined` 协程所在线程均不一样
9. `GlobalScope` 启动协程时默认使用的调度器是 `Dispatchers.Default`，因此也是在后台线程池中执行
10. `newSingleThreadContext` 用于为协程专门创建一个新的线程，专用线程是一种成本非常昂贵的资源，在实际开发时必须当不再需要时释放掉线程资源，或者存储在顶级变量中以便在整个应用程序中进行复用

### ③、`withContext`

1. 对于以下代码，`get()` 方法内使用 `withContext(Dispatchers.IO)` 创建了一个指定在 IO 线程池中运行的代码块，该区间内的任何代码都始终通过 IO 线程来执行。由于 `withContext` 方法本身就是一个挂起函数，因此 `get()` 方法也必须定义为挂起函数

```Kotlin
package com.yuehai.kotlin._08_Coroutines._07_CoroutineContext

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

/**
@author 月海
@create 2023/4/16 16:51
 */
suspend fun fetchDocs() {                      // Dispatchers.Main
    val result = get("developer.android.com")  // Dispatchers.Main
    log(result)                                // Dispatchers.Main
}

suspend fun get(url: String) =                 // Dispatchers.Main
    withContext(Dispatchers.IO) {// Dispatchers.IO (main-safety block)
        /* perform network IO here */          // Dispatchers.IO (main-safety block)
        return@withContext "get"
    }                                          // Dispatchers.Main

suspend fun main() {
    fetchDocs()
}
```

```Kotlin
[DefaultDispatcher-worker-1] get

进程已结束,退出代码0
```

2. 借助协程，你可以细粒度地来调度线程。由于 `withContext()` 支持在不引入回调的情况下控制任何代码的执行线程池，因此你可以将其应用于非常小的函数，例如从数据库中读取数据或执行网络请求。一种不错的做法是使用 `withContext()` 来确保每个函数都是主线程安全的，这意味着，你可以从主线程调用每个函数。这样，调用方就从不需要考虑应该使用哪个线程来执行函数了
3. 在前面的示例中，`fetchDocs()` 方法在主线程上执行，不过它可以安全地调用 `get()` 方法，因为 `get()` 方法已确保网络请求会在子线程中执行。由于协程支持 `suspend` 和 `resume` 操作，因此 `withContext` 块完成后，主线程上的协程会立即根据 `get()` 结果恢复
4. 与基于回调的等效实现相比，`withContext()` 不会增加额外的开销。
5. 此外，在某些情况下，还可以优化 `withContext()` 调用，使其超越基于回调的等效实现。
6. 例如，如果某个函数需要先后调用十次网络请求，你可以在最外层调用 `withContext()` 让协程只切换一次线程，这样即使每个网络请求内部均会使用 `withContext()`，它也会留在同一调度程序上，从而避免频率切换线程。此外，协程还优化了 `Dispatchers.Default` 与 `Dispatchers.IO` 之间的切换，以尽可能避免线程切换
7. 使用线程池的调度器（例如 `Dispatchers.IO` 或 `Dispatchers.Default`）不能保证代码块一直在同一线程上从上到下执行，在某些情况下，协程在 `suspend` 和 `resume` 后可能会将任务移交给另一个线程来执行。这意味着，对于整个 `withContext()` 块，由于多线程并发之间的原子性和可见性等原因，先后读取到的线程局部变量可能并非是同个值

### ④、`CoroutineName`

1. `CoroutineName` 用于为协程指定一个名字，方便调试和定位问题

```Kotlin
package com.yuehai.kotlin._08_Coroutines._07_CoroutineContext

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 18:46
 */
fun main() = runBlocking<Unit>(CoroutineName("RunBlocking")) {

    log("start")

    launch(CoroutineName("MainCoroutine")) {

        launch(CoroutineName("Coroutine#A")) {
            delay(400)
            log("launch A")
        }

        launch(CoroutineName("Coroutine#B")) {
            delay(300)
            log("launch B")
        }
    }
}
```

### ⑤、`CoroutineExceptionHandler`

1. 在下文的异常处理会讲到

### ⑥、组合上下文元素

1. 有时我们需要为协程上下文定义多个元素，此时就可以用 `+` 运算符。例如，我们可以同时为协程指定 `Dispatcher` 和 `CoroutineName`
2. 而由于 `CoroutineContext` 是由一组元素组成的，所以加号右侧的元素会覆盖加号左侧的元素，从而组成新的 `CoroutineContext`。比如，`(Dispatchers.Main, "name") + (Dispatchers.IO)` 的运行结果是：`(Dispatchers.IO, "name")`

```Kotlin
package com.yuehai.kotlin._08_Coroutines._07_CoroutineContext

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.CoroutineName
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

/**
@author 月海
@create 2023/4/16 18:55
 */
fun main() = runBlocking<Unit> {
    launch(Dispatchers.Default + CoroutineName("test")) {
        log("Hello World")
    }
}
```

```Kotlin
[DefaultDispatcher-worker-1] Hello World

进程已结束,退出代码0
```

## 8、取消协程

### ①、介绍

1. 如果用户退出启动了协程的 `Activity` / `Fragment`，那正常情况下就应该取消所有协程
2. `job.cancel()` 就用于取消协程，`job.join()` 用于阻塞等待协程运行结束。
3. 因为 `cancel()` 函数调用后会马上返回而不是等待协程结束后再返回，所以此时协程不一定就是已经停止运行了。
4. 如果需要确保协程结束运行后再执行后续代码，就需要调用 `join()` 方法来阻塞等待。也可以通过调用 `Job` 的扩展函数 `cancelAndJoin()` 来完成相同操作，它结合了 `cancel` 和 `join` 两个操作

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

/**
@author 月海
@create 2023/4/16 19:07
 */
fun main() = runBlocking {
    val job = launch {
        repeat(1000) { i ->
            log("job: I'm sleeping $i ...")
            delay(500L)
        }
    }

    delay(1300L)
    log("main: I'm tired of waiting!")

    job.cancel()

    job.join()
    log("main: Now I can quit.")
}
```

```Kotlin
[main] job: I'm sleeping 0 ...
[main] job: I'm sleeping 1 ...
[main] job: I'm sleeping 2 ...
[main] main: I'm tired of waiting!
[main] main: Now I can quit.

进程已结束,退出代码0
```

### ②、协程可能无法取消

1. 并不是所有协程都可以响应取消操作，协程的取消操作是需要协作 (`cooperative`) 完成的，协程必须协作才能被取消。
2. 协程库中的所有挂起函数都是可取消的，它们在运行前检查协程是否被取消了，并在取消时抛出 `CancellationException` 从而结束整个任务。
3. 而如果协程在执行计算任务前没有判断自身是否已被取消的话，此时就无法取消协程
4. 所以即使以下代码主动取消了协程，协程也只会在完成既定循环后才结束运行，因为协程没有在每次循环前先进行检查，导致任务不受取消操作的影响

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:13
 */
fun main() = runBlocking {
    val startTime = System.currentTimeMillis()

    val job = launch(Dispatchers.Default) {
        var nextPrintTime = startTime
        var i = 0
        while (i < 5) {
            if (System.currentTimeMillis() >= nextPrintTime) {
                log("job: I'm sleeping ${i++} ...")
                nextPrintTime += 500L
            }
        }
    }

    delay(1300L)
    log("main: I'm tired of waiting!")

    job.cancelAndJoin()
    log("main: Now I can quit.")
}
```

```Kotlin
[DefaultDispatcher-worker-1] job: I'm sleeping 0 ...
[DefaultDispatcher-worker-1] job: I'm sleeping 1 ...
[DefaultDispatcher-worker-1] job: I'm sleeping 2 ...
[main] main: I'm tired of waiting!
[DefaultDispatcher-worker-1] job: I'm sleeping 3 ...
[DefaultDispatcher-worker-1] job: I'm sleeping 4 ...
[main] main: Now I can quit.

进程已结束,退出代码0
```

5. 为了实现取消协程的目的，就需要为上述代码加上判断协程是否还处于可运行状态的逻辑，当不可运行时就主动退出协程。`isActive` 是 `CoroutineScope` 的扩展属性，就用于判断协程是否还处于可运行状态

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:19
 */
fun main() = runBlocking {
    val startTime = System.currentTimeMillis()

    val job = launch(Dispatchers.Default) {
        var nextPrintTime = startTime
        var i = 0

        while (i < 5) {
            if (isActive) {
                if (System.currentTimeMillis() >= nextPrintTime) {
                    log("job: I'm sleeping ${i++} ...")
                    nextPrintTime += 500L
                }
            } else {
                return@launch
            }
        }
    }

    delay(1300L)
    log("main: I'm tired of waiting!")

    job.cancelAndJoin()
    log("main: Now I can quit.")
}
```

```Kotlin
[DefaultDispatcher-worker-1] job: I'm sleeping 0 ...
[DefaultDispatcher-worker-1] job: I'm sleeping 1 ...
[DefaultDispatcher-worker-1] job: I'm sleeping 2 ...
[main] main: I'm tired of waiting!
[main] main: Now I can quit.

进程已结束,退出代码0
```

6. 取消协程这个操作类似于在 Java 中调用 `Thread.interrupt()` 方法来向线程发起中断请求，这两个操作都不会强制停止协程和线程，外部只是相当于发起一个停止运行的请求，需要依靠协程和线程响应请求后主动停止运行
7. Java 和 Kotlin 之所以均没有提供一个可以直接强制停止线程或协程的方法，是因为这个操作可能会带来各种意想不到的情况。例如，在停止线程或协程的时候，它们可能还持有着某些排他性资源（例如：锁，数据库链接），如果强制性地停止，它们持有的锁就会一直无法得到释放，导致其它线程或协程一直无法得到目标资源，最终就可能导致线程死锁。
8. 所以 `Thread.stop()` 方法目前也是处于废弃状态，Java 官方并没有提供一个可靠的停止线程的方法

### ③、用 `finally` 释放资源

1. 可取消的挂起函数在取消时会抛出 `CancellationException`，可以依靠 `try {...} finally {...}` 或者 Kotlin 的 use 函数在取消协程后释放持有的资源

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:23
 */
fun main() = runBlocking {

    val job = launch {
        try {
            repeat(1000) { i ->
                log("job: I'm sleeping $i ...")
                delay(500L)
            }
        } catch (e: Throwable) {
            log(e.message)
        } finally {
            log("job: I'm running finally")
        }
    }

    delay(1300L)
    log("main: I'm tired of waiting!")
    
    job.cancelAndJoin()
    log("main: Now I can quit.")
}
```

```Kotlin
[main] job: I'm sleeping 0 ...
[main] job: I'm sleeping 1 ...
[main] job: I'm sleeping 2 ...
[main] main: I'm tired of waiting!
[main] StandaloneCoroutine was cancelled
[main] job: I'm running finally
[main] main: Now I can quit.

进程已结束,退出代码0
```

### ④、`NonCancellable`

1. 如果在上一个例子中的 `finally` 块中再调用挂起函数的话，将会导致抛出 `CancellationException`，因为此时协程已经被取消了。
2. 通常我们并不会遇到这种情况，因为常见的资源释放操作都是非阻塞的，且不涉及任何挂起函数。
3. 但在极少数情况下我们需要在取消的协程中再调用挂起函数，此时可以使用 `withContext` 函数和 `NonCancellable` 上下文将相应的代码包装在 `withContext(NonCancellable) {...}` 代码块中，`NonCancellable` 就用于创建一个无法取消的协程作用域

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:25
 */
fun main() = runBlocking {

    log("start")

    val launchA = launch {
        try {
            repeat(5) {
                delay(50)
                log("launchA-$it")
            }
        } finally {
            delay(50)
            log("launchA isCompleted")
        }
    }

    val launchB = launch {
        try {
            repeat(5) {
                delay(50)
                log("launchB-$it")
            }
        } finally {
            withContext(NonCancellable) {
                delay(50)
                log("launchB isCompleted")
            }
        }
    }

    // 延时一百毫秒，保证两个协程都已经被启动了
    delay(200)

    launchA.cancel()
    launchB.cancel()

    log("end")
}
```

```Kotlin
[main] start
[main] launchA-0
[main] launchB-0
[main] launchA-1
[main] launchB-1
[main] launchA-2
[main] launchB-2
[main] end
[main] launchB isCompleted

进程已结束,退出代码0
```

### ⑤、父协程和子协程

1. 当一个协程在另外一个协程的协程作用域中启动时，它将通过 `CoroutineScope.coroutineContext` 继承其上下文，新启动的协程就被称为子协程，子协程的 `Job` 将成为父协程 `Job` 的子 `Job`。父协程总是会等待其所有子协程都完成后才结束自身，所以父协程不必显式跟踪它启动的所有子协程，也不必使用 `Job.join` 在末尾等待子协程完成
2. 所以虽然 `parentJob` 启动的三个子协程的延时时间各不相同，但它们最终都会打印出日志

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:29
 */
fun main() = runBlocking {

    val parentJob = launch {
        repeat(3) { i ->
            launch {
                delay((i + 1) * 200L)
                log("Coroutine $i is done")
            }
        }

        log("request: I'm done and I don't explicitly join my children that are still active")
    }
}
```

```Kotlin
[main] request: I'm done and I don't explicitly join my children that are still active
[main] Coroutine 0 is done
[main] Coroutine 1 is done
[main] Coroutine 2 is done

进程已结束,退出代码0
```

### ⑥、传播取消操作

1. 一般情况下，协程的取消操作会通过协程的层次结构来进行传播：
	1. 如果取消父协程或者父协程抛出异常，那么子协程都会被取消；
	2. 而如果子协程被取消，则不会影响同级协程和父协程，但如果子协程抛出异常则也会导致同级协程和父协程被取消
2. 对于以下代码，子协程 `jon1` 被取消并不影响子协程 `jon2` 和父协程继续运行，但父协程被取消后子协程都会被递归取消

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:31
 */
fun main() = runBlocking {

    val request = launch {

        val job1 = launch {
            repeat(10) {
                delay(300)
                log("job1: $it")
                if (it == 2) {
                    log("job1 canceled")
                    cancel()
                }
            }
        }
        
        val job2 = launch {
            repeat(10) {
                delay(300)
                log("job2: $it")
            }
        }
    }

    delay(1600)
    log("parent job canceled")

    request.cancel()
    delay(1000)
}
```

```Kotlin
[main] job1: 0
[main] job2: 0
[main] job1: 1
[main] job2: 1
[main] job1: 2
[main] job1 canceled
[main] job2: 2
[main] job2: 3
[main] job2: 4
[main] parent job canceled

进程已结束,退出代码0
```

### ⑦、`withTimeout`

1. `withTimeout` 函数用于指定协程的运行超时时间，如果超时则会抛出 `TimeoutCancellationException`，从而令协程结束运行
2. `withTimeout` 方法抛出的 `TimeoutCancellationException` 是 `CancellationException` 的子类，之前我们并未在输出日志上看到关于 `CancellationException` 这类异常的堆栈信息，这是因为对于一个已取消的协程来说，`CancellationException` 被认为是触发协程结束的正常原因。
3. 但对于 `withTimeout` 方法来说，抛出异常是其上报超时情况的一种手段，所以该异常不会被协程内部消化掉
4. 如果不希望因为异常导致协程结束，可以改用 `withTimeoutOrNull` 方法，如果超时就会返回 `null`

```Kotlin
package com.yuehai.kotlin._08_Coroutines._08_Cancel

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:32
 */
fun main() = runBlocking {
    log("start")

    val result = withTimeout(300) {
        repeat(5) {
            delay(100)
        }
        200
    }

    log(result)

    log("end")
}
```

```Kotlin
[main] start
Exception in thread "main" kotlinx.coroutines.TimeoutCancellationException: Timed out waiting for 300 ms
	at kotlinx.coroutines.TimeoutKt.TimeoutCancellationException(Timeout.kt:186)
	at kotlinx.coroutines.TimeoutCoroutine.run(Timeout.kt:156)
	at kotlinx.coroutines.EventLoopImplBase$DelayedRunnableTask.run(EventLoop.common.kt:497)
	at kotlinx.coroutines.EventLoopImplBase.processNextEvent(EventLoop.common.kt:274)
	at kotlinx.coroutines.DefaultExecutor.run(DefaultExecutor.kt:69)
	at java.base/java.lang.Thread.run(Thread.java:834)

进程已结束,退出代码1
```

## 9、异常处理

### ①、介绍

1. 当一个协程由于异常而运行失败时，它会传播这个异常并传递给它的父协程。接下来，父协程会进行下面几步操作：
	1. 取消它自己的子级
	2. 取消它自己
	3. 将异常传播并传递给它的父级
2. 异常会到达层级的根部，且当前 `CoroutineScope` 所启动的所有协程都会被取消，但协程并非都是一发现异常就执行以上流程，`launch` 和 `async` 在处理异常方面有着一些差异
3. `launch` 将异常视为未捕获异常，类似于 Java 的 `Thread.uncaughtExceptionHandler`，当发现异常时就会马上抛出。`async` 期望最终通过调用 `await` 来获取结果 (或者异常)，所以默认情况下它不会抛出异常，这意味着如果使用 `async` 启动新的协程，它会静默地将异常丢弃，直到调用 `async.await()` 才会得到目标值或者抛出存在的异常
4. 例如，以下的 `fetchDocs()` 方法由于并没有调用 `Deferred.await()`，因此异常并不会被抛给调用方，而如果使用的是 `launch` 而非 `async` 的话，异常就会马上被抛出

```Kotlin
package com.yuehai.kotlin._08_Coroutines._09_Exception

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:40
 */
private val ioScope = CoroutineScope(Dispatchers.IO)

private fun fetchDocs() {
    ioScope.async {
        delay(500)
        log("taskA throw AssertionError")
        throw AssertionError()
    }
}

private suspend fun fetchDocs2() {
    var a = ioScope.async {
        delay(500)
        log("taskA throw AssertionError")
        throw AssertionError()

    }.await()

}

suspend fun main() {
    log("--------")
    fetchDocs()
    
    log("--------")
    fetchDocs2()
}
```

```Kotlin
[main] --------
[main] --------
[DefaultDispatcher-worker-3] taskA throw AssertionError
[DefaultDispatcher-worker-1] taskA throw AssertionError
Exception in thread "main" java.lang.AssertionError
	at com.yuehai.kotlin._08_Coroutines._09_Exception._00_ExceptionKt$fetchDocs2$a$1.invokeSuspend(_00_Exception.kt:24)
	at kotlin.coroutines.jvm.internal.BaseContinuationImpl.resumeWith(ContinuationImpl.kt:33)
	at kotlinx.coroutines.DispatchedTask.run(DispatchedTask.kt:106)
	at kotlinx.coroutines.scheduling.CoroutineScheduler.runSafely(CoroutineScheduler.kt:571)
	at kotlinx.coroutines.scheduling.CoroutineScheduler$Worker.executeTask(CoroutineScheduler.kt:750)
	at kotlinx.coroutines.scheduling.CoroutineScheduler$Worker.runWorker(CoroutineScheduler.kt:678)
	at kotlinx.coroutines.scheduling.CoroutineScheduler$Worker.run(CoroutineScheduler.kt:665)

```

### ②、`CoroutineExceptionHandler`

1. 如果想主动捕获异常信息，可以使用 `CoroutineExceptionHandler` 作为协程的上下文元素之一，在这里进行自定义日志记录或异常处理，它类似于对线程使用 `Thread.uncaughtExceptionHandler`。
2. 但是，`CoroutineExceptionHandler` 只会在预计不会由用户处理的异常上调用，因此在 `async` 中使用它没有任何效果，当 `async` 内部发生了异常且没有捕获时，那么调用 `async.await()` 依然会导致应用崩溃
3. 以下代码只会捕获到 `launch` 抛出的异常

```Kotlin
package com.yuehai.kotlin._08_Coroutines._09_Exception

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:46
 */
fun main() = runBlocking {

    val handler = CoroutineExceptionHandler { _, exception ->
        log("Caught $exception")
    }

    val job = GlobalScope.launch(handler) {
        throw AssertionError()
    }

    val deferred = GlobalScope.async(handler) {
        throw ArithmeticException()
    }

    joinAll(job, deferred)
}
```

```Kotlin
[DefaultDispatcher-worker-1] Caught java.lang.AssertionError

进程已结束,退出代码0
```

### ③、`SupervisorJob`

1. 由于异常导致的取消在协程中是一种双向关系，会在整个协程层次结构中传播，那如果我们需要的是单向取消该怎么实现呢？
2. 例如，假设在 `Activity` 中启动了多个协程，如果单个协程所代表的子任务失败了，此时并不一定需要连锁终止整个 `Activity` 内部的所有其它协程任务，即此时希望子协程的异常不会传播给同级协程和父协程。而当 `Activity` 退出后，父协程的异常（即 `CancellationException`）又应该连锁传播给所有子协程，终止所有子协程
3. 可以使用 `SupervisorJob` 来实现上述效果，取消操作只会向下传播，一个子协程的运行失败不会影响到同级协程和父协程
4. 例如，以下示例中 `firstChild` 抛出的异常不会导致 `secondChild` 被取消，但当 `supervisor` 被取消时 `secondChild` 也被同时取消了

```Kotlin
package com.yuehai.kotlin._08_Coroutines._09_Exception

import com.yuehai.kotlin._08_Coroutines.log
import kotlinx.coroutines.*

/**
@author 月海
@create 2023/4/16 19:48
 */
fun main() = runBlocking {

    val supervisor = SupervisorJob()

    with(CoroutineScope(coroutineContext + supervisor)) {

        val firstChild = launch(CoroutineExceptionHandler { _, _ -> }) {
            log("First child is failing")
            throw AssertionError("First child is cancelled")
        }

        val secondChild = launch {
            firstChild.join()
            log("First child is cancelled: ${firstChild.isCancelled}, but second one is still active")
            try {
                delay(Long.MAX_VALUE)
            } finally {
                log("Second child is cancelled because supervisor is cancelled")
            }
        }

        firstChild.join()
        log("Cancelling supervisor")

        // 取消所有协程
        supervisor.cancel()
        secondChild.join()
    }
}
```

```Kotlin
[main] First child is failing
[main] First child is cancelled: true, but second one is still active
[main] Cancelling supervisor
[main] Second child is cancelled because supervisor is cancelled

进程已结束,退出代码0
```

5. 但是，如果异常没有被处理且 `CoroutineContext` 没有包含一个 `CoroutineExceptionHandler` 的话，异常会到达默认线程的 `ExceptionHandler`。
6. 在 JVM 中，异常会被打印在控制台；
7. 而在 Android 中，无论异常在那个 `Dispatcher` 中发生，都会直接导致应用崩溃。所以如果上述例子中移除了 `firstChild` 包含的 `CoroutineExceptionHandler` 的话，就会导致 Android 应用崩溃

## 10、`Android ktx`

1. `Android ktx` 是包含在 `Android Jetpack` 及其他 Android 库中的一组 Kotlin 扩展程序。
2. `ktx` 扩展程序可以为 `Jetpack`、`Android` 平台及其他 API 提供简洁的惯用 Kotlin 代码，这些扩展程序利用了多种 Kotlin 语言功能，其中就包括了对 Kotlin 协程的支持

### ①、`Lifecycle ktx`

1. `Lifecycle ktx` 为每个 `Lifecycle` 对象（`Activity`、`Fragment`、`Process` 等）定义了一个 `LifecycleScope`，该作用域具有生命周期安全的保障，在此范围内启动的协程会在 `Lifecycle` 被销毁时同时取消，可以使用 `lifecycle.coroutineScope` 或 `lifecycleOwner.lifecycleScope` 属性来拿到该 `CoroutineScope`
2. 引入依赖：

```
dependencies {
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.4.0"
}
```

3. 使用示例

```Kotlin
package com.yuehai.kotlin._10_AndroidKtx

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.coroutineScope
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch

/**
@author 月海
@create 2023/4/16 19:56
 */
class MyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        
        super.onCreate(savedInstanceState)
        
        lifecycleScope.launch {
            //Do Something
        }
        
        lifecycle.coroutineScope.launch {
            //Do Something
        }
    }

}
```

4. `lifecycleScope` 和 `lifecycle.coroutineScope` 两者是等价的，`lifecycleScope` 只是 `ktx` 库提供的一种简便写法。
5. 从源码也可以看到，`lifecycleScope` 是存储在抽象类 `Lifecycle` 的 `mInternalScopeRef` 字段中，且使用的是 `SupervisorJob` 和 `Dispatchers.Main.immediate`，因此我们不必担心任意子协程的异常情况会影响到全局的协程任务，且其默认就是在主线程运行协程

```Kotlin
public val LifecycleOwner.lifecycleScope: LifecycleCoroutineScope
    get() = lifecycle.coroutineScope

public val Lifecycle.coroutineScope: LifecycleCoroutineScope
    get() {
        while (true) {
            val existing = mInternalScopeRef.get() as LifecycleCoroutineScopeImpl?
            if (existing != null) {
                return existing
            }
            val newScope = LifecycleCoroutineScopeImpl(
                this,
                SupervisorJob() + Dispatchers.Main.immediate
            )
            if (mInternalScopeRef.compareAndSet(null, newScope)) {
                newScope.register()
                return newScope
            }
        }
    }
```

### ②、`ViewModel ktx`

1. `ViewModel ktx` 库提供了一个 `viewModelScope`，用于在 `ViewModel` 中启动协程，该作用域的生命周期和 `ViewModel` 相等，当 `ViewModel` 回调了 `onCleared()` 方法时会自动取消该作用域
2. 引入依赖

```Kotlin
dependencies {
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.4.0"
}
```

3. 例如，以下 `fetchDocs()` 方法内就依靠 `viewModelScope` 启动了一个协程，用于在后台线程发起网络请求

```Kotlin
class MyViewModel : ViewModel() {
    
    fun fetchDocs() {
        viewModelScope.launch {
            val result = get("https://developer.android.com")
            show(result)
        }
    }

    suspend fun get(url: String) = withContext(Dispatchers.IO) { /* ... */ }

}
```

4. 从源码可以看到其大体实现思路和 `lifecycleScope` 类似，存储在 `ViewModel` 类的 `mBagOfTags` 这个 `Map` 中，且使用的也是 `SupervisorJob` 和 `Dispatchers.Main.immediate`

```Kotlin
public val ViewModel.viewModelScope: CoroutineScope
    get() {
        val scope: CoroutineScope? = this.getTag(JOB_KEY)
        if (scope != null) {
            return scope
        }
        return setTagIfAbsent(
            JOB_KEY,
            CloseableCoroutineScope(SupervisorJob() + Dispatchers.Main.immediate)
        )
    }

internal class CloseableCoroutineScope(context: CoroutineContext) : Closeable, CoroutineScope {
    override val coroutineContext: CoroutineContext = context

    override fun close() {
        coroutineContext.cancel()
    }
}
```

### ③、`LiveData ktx`

1. 在某些情况下，我们需要先完成特定的异步计算任务，根据计算结果来向 `LiveData` 回调值，此时就可以使用 `LiveData ktx` 提供的 `liveData` 构建器函数来执行 `suspend` 函数所代表的异步计算任务（耗时任务），并将结果赋值给 `LiveData`
2. 引入依赖：

```Kotlin
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.4.0"
}
```

3. 在以下示例中，`loadUser()` 是在其它地方声明的 `suspend` 函数，你可以使用 `liveData` 构建器函数异步调用 `loadUser()`，然后使用 `emit()` 来发出结果：

```Kotlin
val user: LiveData<User> = liveData {
    val data = database.loadUser()
    emit(data)
}
```

4. 从源码可以看到，我们所传入的 `suspend` 任务体 `block` 最终是会被 `CoroutineLiveData` 包装为一个 `BlockRunner` 对象，而 `CoroutineLiveData` 会在自身开始有 `Observer` 监听时执行 `blockRunner`，并在所有 `Observer` 均被移除时自动 `Cancel` 掉 `blockRunner`

```Kotlin
public fun <T> liveData(
    context: CoroutineContext = EmptyCoroutineContext,
    timeoutInMs: Long = DEFAULT_TIMEOUT,
    @BuilderInference block: suspend LiveDataScope<T>.() -> Unit
): LiveData<T> = CoroutineLiveData(context, timeoutInMs, block)

internal class CoroutineLiveData<T>(
    context: CoroutineContext = EmptyCoroutineContext,
    timeoutInMs: Long = DEFAULT_TIMEOUT,
    block: Block<T>
) : MediatorLiveData<T>() {
    private var blockRunner: BlockRunner<T>?
    private var emittedSource: EmittedSource? = null

    init {
        val supervisorJob = SupervisorJob(context[Job])
        val scope = CoroutineScope(Dispatchers.Main.immediate + context + supervisorJob)
        blockRunner = BlockRunner(
            liveData = this,
            block = block,
            timeoutInMs = timeoutInMs,
            scope = scope
        ) {
            blockRunner = null
        }
    }

    override fun onActive() {
        super.onActive()
        blockRunner?.maybeRun()
    }

    override fun onInactive() {
        super.onInactive()
        blockRunner?.cancel()
    }
}

internal class BlockRunner<T>(
    private val liveData: CoroutineLiveData<T>,
    private val block: Block<T>,
    private val timeoutInMs: Long,
    private val scope: CoroutineScope,
    private val onDone: () -> Unit
) {
    // currently running block job.
    private var runningJob: Job? = null

    // cancelation job created in cancel.
    private var cancellationJob: Job? = null

    @MainThread
    fun maybeRun() {
        cancellationJob?.cancel()
        cancellationJob = null
        if (runningJob != null) {
            return
        }
        runningJob = scope.launch {
            val liveDataScope = LiveDataScopeImpl(liveData, coroutineContext)
            block(liveDataScope)
            onDone()
        }
    }

    @MainThread
    fun cancel() {
        if (cancellationJob != null) {
            error("Cancel call cannot happen without a maybeRun")
        }
        cancellationJob = scope.launch(Dispatchers.Main.immediate) {
            delay(timeoutInMs)
            if (!liveData.hasActiveObservers()) {
                runningJob?.cancel()
                runningJob = null
            }
        }
    }
}
```

# 九、Kotlin 与 Java 的调用

1. Kotlin 在设计之初，就考虑了与 Java 的互操作性。因此 Java 和 Kotlin 是可以很方便的进行互相调用的。
2. 虽然 Kotlin 完全兼容 Java，但不代表 Kotlin 就是 Java，它们在相互调用但时候，还是有一些需要注意的细节。

## 1、Kotlin 调 Java

### ①、Kotlin 调 Java

1. 首先，几乎所有的 Java 代码，都可以在 Kotlin 中调用而没有任何问题。如在 Kotlin 中使用集合类：

```Kotlin
import java.util.*

fun demo(source: List<Int>) {
    val list = ArrayList<Int>()
    // “for”-循环用于 Java 集合：
    for (item in source) {
        list.add(item)
    }
    // 操作符约定同样有效：
    for (i in 0..source.size - 1) {
        list[i] = source[i] // 调用 get 和 set
    }
}
```

2. 只是在创建对象和使用对象方法的时候，可以有更简洁的方式去使用。
3. 下面针对一些细节做详细介绍：

### ②、访问普通属性和方法

1. 如果要访问一个 `Java` 对象的私有属性，`Java` 对象都会提供 `Getter` 和 `Setter` 方法，通过相关的 `Getter` 和 `Setter` 方法，就可以拿到属性的值。
2. 而如果一个 `Java` 类为成员属性提供了 `Getter` 和 `Setter` 方法，则在 Kotlin 中使用该属性的时候，就可以直接通过属性名去访问，而不用调对应的 `Getter` 和 `Setter` 方法，如

```java
package com.yuehai.kotlin._09_KotlinCallJava;

/**
 * @author 月海
 * @create 2023/4/17 9:39
 */
public class JavaTest {
    private String name;
    private Integer age;

    public JavaTest() {
    }
    public JavaTest(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }

    public void play(){
        System.out.println("玩" + this.name);
    }
}

```

```Kotlin
package com.yuehai.kotlin._09_KotlinCallJava

/**
@author 月海
@create 2023/4/17 9:41
 */
fun main() {
	// Kotlin 实例化 Java 类
	val java = JavaTest("月海", 16)
	
	// 调用对象属性
	println(java.name)
	// 调用对象方法
	java.play()
}
```

```Kotlin
月海
玩月海

进程已结束,退出代码0
```

# 十、其他

## 1、Kotlin 中的引用和对象操作的详细解释和总结

### ①、基本概念

1. **对象**：存储在内存中的数据结构，可以包含多个属性和方法。
2. **引用**：指向内存中对象的变量。改变引用所指向的对象的属性会影响所有指向该对象的引用。

### ②、引用操作示例

#### Ⅰ、**修改对象属性**

   1. 当通过一个引用修改其指向的对象的属性时，所有指向这个对象的引用都将**看到**这些更改。

```kotlin
// 定义一个简单的数据类
data class Person(var name: String, var age: Int)

// 创建一个 Person 对象并赋值给 p1 引用
val p1 = Person("Alice", 30)
// p2 也指向同一个 Person 对象
val p2 = p1

// 通过 p1 修改对象的属性
p1.name = "Bob"

// p2 也会看到这个更改
println(p2.name) // 输出 "Bob"
```

   2. 在这个例子中，`p1` 和 `p2` 都指向同一个 `Person` 对象。通过 `p1` 修改 `name` 属性后，通过 `p2` 访问同一个对象的 `name` 属性也显示了更新后的值。

#### Ⅱ、**改变引用**


   1. 当改变一个引用本身（使其指向另一个对象或设置为 `null`）时，这个改变只影响该引用。

   ```kotlin
   // 继续使用 Person 类
   var p3 = Person("Charlie", 25)
   var p4 = p3

   // p3 现在指向一个新的 Person 对象
   p3 = Person("Diana", 28)

   // p4 仍然指向原来的对象
   println(p4.name) // 输出 "Charlie"
   println(p3.name) // 输出 "Diana"
   ```

   2. 这里，`p3` 被重新赋值，指向一个新的 `Person` 对象。而 `p4` 依然指向原来的对象。这表明重新赋值操作只影响 `p3`，而不影响 `p4`。

### ③、Kotlin 中的集合和对象引用

1. 当操作集合中的对象时，对集合中的对象引用的修改同样遵循上述规则。

```kotlin
// 创建一个 Person 对象列表
val people = mutableListOf(Person("Eva", 22))

// a 指向列表中第一个元素的引用
var a = people[0]

// 修改 a 引用的对象的属性
a.age = 23

// 通过列表访问该对象，可以看到更改
println(people[0].age) // 输出 23
```

2. 在这个例子中，`a` 指向 `people` 列表中第一个元素的引用。修改 `a` 引用的对象的 `age` 属性后，这个更改通过列表也是可见的。

### ④、结论

1. 修改对象的属性会影响所有引用该对象的变量
2. 而更改引用本身只影响该特定的引用变量

## 2、

## 3、

## 4、
