# 一、Java入门环境搭建

## 1、Java 的特性和优势

1. 简单性
2. 面向对象
3. 可移植性
4. 高性能
5. 分布式
6. 动态性（反射）
7. 多线程
8. 安全性
9. 健壮性

## 2、Java 的三大版本

1. JavaSE：标准版（桌面程序，控制台开发等）
2. JavaME：嵌入式开发（手机，小家电等，不过现在几乎没人用了）
3. JavaEE：企业级开发（web端，服务器开发等）

## 3、JDK、JRE、JVM

1. JDK：Java Development Kit（Java开发者工具，开发Java所需，并包含了jre）
2. JRE：Java Runtime Environment（Java运行环境，运行Java程序所需）
3. JVM：JAVA Virtual Machine（Java虚拟机，跨平台等所需）

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、JDK、JRE、JVM.png)

## 4、Java开发环境

### ①、安装 jdk

1. 在D盘（或其他）的跟目录创建Java文件夹
2. 在Java文件夹中创建Java-8u271-windows-x64文件夹
3. 在Java-8u271-windows-x64文件夹中创建jdk、jre文件夹

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、创建安装Java的目录.png)

4. 下载电脑对应版本的jdk-8u271-windows-x64，双击打开
5. 点击下一步，在安装位置后选择更改，选择刚才创建的jdk文件夹
6. 安装完成后会添跳出jre的安装，选择刚才创建的jre文件夹
7. 完成
8. 右键我的电脑，选择属性，点击高级系统，点击环境变量
9.  在系统变量中点击新建，输入变量名：JAVA_HOME，变量值：D:\Java\jdk-8u271-windows-x64\jdk
10. 在系统变量中选择Path，点击编辑
11. 点击新建，输入：%JAVA_HOME%\bin，再次点击新建，输入：%JAVA_HOME%\jre\bin

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、Java环境变量的设置.png)

12. 完成
13. 打开控制台，输入 `javac` 与 `java -version` 测试是否成功

### ②、卸载 jdk

1. 删除 D 盘的 Java 目录
2. 删除 `JAVA_HOME`
3. 删除 path 下的 `%JAVA_HOME%\bin` 与 `%JAVA_HOME%\jre\bin`

## 5、Hello World

1. 新建一个 `HelloWorld.Java` 文件
2. 打开文件，编写以下代码

```java
public class HelloWorld{
    public static void main(String[] args){
        System.out.print("Hello World");
    }
}
```

3. 编译 Java 文件：打开 `HelloWorld.Java` 文件所在的文件夹，在路径前输入：`cmd+空格`

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F04、打开控制台.png)

1. 在控制台输入：`javac HelloWorld.Java`，回车

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F05、编译Java文件.png)

4. 会生成 `HelloWorld.class` 文件，接着在控制台输入：`java HelloWorld`

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F06、运行Java文件，输出语句.png)

## 6、需要注意的问题

1. 每个单词的大小写不能出现问题，Java 是大小写敏感的
2. 尽量使用英文
3. 文件名和类名必须保持一致，并且首字母大写
4. 符号必须是英文的

## 7、Java 运行机制

1. 编译型：对系统要求较低，一般是开发操作系统等
2. 解释型：对速度要求低，一般是开发网页、服务器脚本等
3. Java 运行机制：源程序（.Java文件）-> 字节码（.class文件）-> 类装载器 -> 字节码效验器 -> 解释器 -> 操作系统平台

# 二、Java 基础

## 1、注释、标识符、关键字

### ①、注释

   - 注释并不会被执行，是给书写代码的人看的注解
   - 单行注释、多行注释、文档注释

1. 单行注释：只注释一行

```java
//注释文字
```

2. 多行注释：可注释多行

```java
/*
注释文字
第二行注释

*/
```

3. 这是文档注释（JavaDoc）：可多行注释，可添加一些参数

```java
/**
* 这是文档注释，JavaDoc
* @Description HelloWorld
* 可以添加一些参数
* */
```

### ②、标识符

   - Java中所有的组成部分都需要名字。类名、变量名以及方法名都被称为标识符

1. 所有的标识符都应该以字母`A-`Z 或者 `a-z`、美元符号`$`、或者下划线 `_` 开始
2. 首字符之后可以是字母 `A-Z` 或者 `a-z`、美元符号 `$`、或者下划线 `_` 或数字的任何字符组合
3. 不能使用关键字作为变量名或方法名
4. <font color="red">标识符是大小写敏感的</font>
5. 可以使用中文命名，但是一般不建议这样使用，也不建议使用拼音


### ③、关键字

- Java中大部分的关键字：

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、标识符、关键字.png)

## 2、数据类型

1. 强类型语言：要求变量的使用要严格符合规定，所有变量都必须先定义后才能使用（安全性高，但是速度比较慢）（Java、c 等）
2. 弱类型语言：变量的使用没有严格的规定（JavaScript 等）
3. Java 的数据类型分为两大类：
	1. 基本类型（primitive type）
	2. 引用类型（reference type）

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、数据类型.png)

|数据类型|名称|说明|最小值|最大值|默认值|补充|
|--|--|--|--|--|--|--|
|<font color="red">byte</font>|<font color="red">整数</font>|8位、有符号的，以二进制补码表示|-128（-2^7）|127（2^7-1）|0|byte 类型用在大型数组中节约空间，主要代替整数，<br/>因为 byte 变量占用的空间只有 int 类型的四分之一|
|<font color="red">short</font>|<font color="red">整数</font>|16 位、有符号的以二进制补码表示|-32768（-2^15）|32767（2^15 - 1）|0|Short 数据类型也可以像 byte 那样节省空间。<br/>一个short变量是int型变量所占空间的二分之一|
|<font color="red">int</font>|<font color="red">整数</font>|32位、有符号的以二进制补码表示|-2,147,483,648（-2^31）|2,147,483,647（2^31 - 1）|0|一般地整型变量默认为 int 类型|
|<font color="red">long</font>|<font color="red">整数</font>| 64 位、有符号的以二进制补码表示|-9,223,372,036,854,775,808（-2^63）|9,223,372,036,854,775,807（2^63 -1）|0L|这种类型主要使用在需要比较大整数的系统上|
|<font color="red">float</font>|<font color="red">浮点数</font>|单精度、32位、符合IEEE 754标准的| / | / |0.0f|float 在储存大型浮点数组的时候可节省内存空间，<br/>浮点数不能用来表示精确的值，如货币|
|<font color="red">double</font>|<font color="red">浮点数</font>|双精度、64 位、符合 IEEE 754 标准| / | / |0.0d|浮点数的默认类型为 double 类型，<br/>double类型同样不能表示精确的值，如货币|
|<font color="red">boolean</font>|<font color="red">布尔型</font>|表示一位的信息，只有两个取值：true 和 false| / | / |false|这种类型只作为一种标志来记录 true/false 情况|
|<font color="red">char</font>|<font color="red">字符型</font>|单一的 16 位 Unicode 字符|\u0000（十进制等效值为 0）|\uffff（即为 65535）| / |char 数据类型可以储存任何字符|

## 3、类型转换

### ①、类型转换

1. 由于 Java 是强类型语言，所以要进行有些运算的时候，需要用到类型转换
2. 运算中，不同类型的数据先转化为同一类型，然后进行运算
3. 强制转换：`(类型)变量名`，高-->低
4. 自动转换：低-->高

```java
低 ------------------------------------------------> 高
byte , short , char -> int -> long -> float -> double
```
   
5. 强制转换及内存溢出例子

```java
int i = 128;             // 定义 int 类型的 i
byte b = (byte) i;       // 将 int 类型的i强制转换为 byte 类型，并赋值给 byte 类型的 b
System.out.println(i);   // 结果：128，输出int类型的i=128
System.out.println(b);   // 结果：-128，输出 byte 类型的 b=128，但是储存的数值范围为 -128~127，最大只能为 127，所以内存溢出，变为 -128
```

### ②、强制转换注意点

1. 不能对布尔值进行转换
2. 不能把对象类型转换为不相干的类型
3. 在把高容量转换到低容量的时候，强制转换
4. 转换的时候可能存在精度问题

```java
System.out.println((int)23.7);       //结果：23
System.out.println((int)-45.89f);    //结果：-45
```

5. 转换的时候可能存在内存溢出问题

```java
//JDK7开始，数字之间可以用下划线分割，原素据不变
int money = 10_0000_0000;           //定义int类型的money，并赋值10_0000_0000
int years = 20;                     //定义int类型的years，并赋值20

int total1 = money*years;           //定义int类型的total1，并赋值money*years
long total2 = money*years;          //定义long类型的total2，并赋值money*years
long total3 = (long)money*years;    //定义long类型的total3，先把一个数强转为long，并赋值(long)money*years

System.out.println(total1);         //结果：-1474836480，内存溢出，结果超出了int类型的最大值
System.out.println(total2);         //结果：-1474836480，内存溢出，相乘的两个数是int类型，所以结果超出了int类型的最大值
System.out.println(total3);         //结果：20000000000，money在相乘之前转换为long类型，无内存溢出
```

## 4、引号、字节、进制

### ①、java 中单引号和双引号区别

1. java 中的单引号表示字符，java 中的双引号是字符串。
2. 单引号引的数据一般是 char 类型的；双引号引的数据是 String 类型的。
3. java 中单引号里面只能放一个字母或数字或符号；java 中的双引号里面是 0 到多个字符构成。所以字符可以直接转换成字符串。字符串需要使用`charAt(n)` 来获取第几个字符。
4. char 定义时用单引号，只能有一个字母、数字：`char c='c';`
5. 而 String 用双引号，可以是一个，也可能是多个字母，汉字等。就是所谓的字符串。`String s="adsaf"`;
6. char 只是一个基本类型，而 String 可以是一个类，可以直接引用。比如 `char c='c';` 不能直接对 c 调用方法。`String s="abc"`; 这时可以调用`s.charAt(0);`等方法；因为 String 是类，这是就是对象的调用了。

### ②、什么是字节

1. 位（bit）：是计算机内部数据储存的最小单位，11001100 是一个八位二进制数
2. 字节（byte）：是计算机中数据处理的基本单位，习惯上用大写B来表示
   - 1bit 表示 1 位
   - 1Byte 表示一个字节，1B = 8b
   - 1024B = 1KB
   - 1024KB = 1M
   - 1024M = 1G
3. 字符是指计算机中中使用的字母、数字、字和符号

### ③、进制

1. 二进制：逢二进一，0，1
2. 十进制：逢十进一，0，1，2，3，4，5，6，7，8，9

```java
int i = 10;
```
   
3. 八进制：逢八进一，0，1，2，3，4，5，6，7

```java
int i = 010;
```

4. 十六进制：逢十六进一，0，1，2，3，4，5，6，7，8，9，A，B，C，D，E，F

```java
int i = 0x10;
```

5. 浮点数：float，double

```java
float f = 0.1f;              //0.1
double d = 1.0/10;           //0.1
System.out.println(f==d);    //结果应该是true，但运行后却是false
```
   
   - 浮点数的位数是有限且离散（结果有区别，因为会有舍入误差）的，故
   - <font color="red">最好完全避免使用浮点数进行比较</font>

6. 强制类型转换

```java
char c1 = 'a';
char c2 = '中';

System.out.println(c1);          //结果：a
System.out.println(c2);          //结果：中

System.out.println((int)c1);     //结果：97
System.out.println((int)c2);     //结果：20013
```
   
   - 故，<font color="red">所有字符的本质还是数字</font>
   - char类型涉及到Unicode编码的问题，可以处理各种语言的文字，占两字节，最多可以表示65536个字符

7. 转义字符
   - \t：制表符
   - \n：换行符

## 5、变量、常量、作用域

### ①、变量

1. 变量就是可以变化的量，它定义了一个空间，空间地址不变，但是储存的内容（值）可以变
2. Java 是一种强类型语言，每个变量都必须声明其类型
3. Java 变量是程序中最基本的存储单元，其要素包括变量名，变量值和作用域

```java
// 数据类型 变量名 = 变量值
type varName = 10;
int id = 10;
String name = "言";
```

4. 注意事项：
	1. 每个变量都有类型，类型可以是基本类型，也可以是引用类型
	2. 变量名必须是合法的标识符
	3. 变量名是一条完整的语句，因此每一个声明都必须以分号结束

### ②、变量作用域

1. 局部变量：定义在方法中，必须进行初始化值
2. 实例变量（全局变量）：从属于对象，定义在类中，调用时必须实例化对象
	1. 可以不进行初始化，如果不初始化那么它的值是这个类型的默认值，基本类型一般是 `0`，`0.0` 等
	2. 布尔值默认是 `false`，除了基本类型，其余的默认值都是 `null`
3. 类变量：使用 static 修饰，定义在类中，可直接调用
	1. 可以不进行初始化，如果不初始化那么它的值是这个类型的默认值，基本类型一般是 `0`，`0.0` 等
	2. 布尔值默认是 `false`，除了基本类型，其余的默认值都是 `null`

```java
public class Demo01 {
  //类变量
  static double salary = 2500;
  static int j;

  //实例变量（全局变量）：从属于对象，定义在类中
  //可以不进行初始化，如果不初始化那么它的值是这个类型的默认值，基本类型一般是0，0.0等
  //布尔值默认是false，除了基本类型，其余的默认值都是null
  String name;
  int age;

  //main方法
  public static void main(String[] args) {
	 //局部变量：定义在方法中，必须进行初始化值
	 String passwoed = "ccj000123";
	 int i = 10;

	 System.out.println(i);              //10

	 System.out.println(salary);         //2500.0
	 System.out.println(j);              //0

	 Demo01 demo01 = new Demo01();       //调用实例变量必须实例化对象
	 System.out.println(demo01.name);    //null
	 System.out.println(demo01.age);     //0

  }
}
```

### ③、变量的命名规则


1. 所有的变量、方法、类名：见名知意
2. 类名：首字母大写和驼峰原则：`Man`，`GoodMan`
3. 方法名：首字母小写和驼峰原则：`run()`，`runRun()`，除了第一个单词以外，后面的单词首字母大写
4. 类成员变量：首字母小写和驼峰原则：`monthSalary`
5. 局部变量：首字母小写和驼峰原则（同3、4）
6. 常量：大写字母和下划线：`MAX_VALUE`

### ④、常量

1. 使用 final 修饰
2. 定义之后值不可变
```java
public class Demo02 {
  //全局常量，使用final修饰
  static final int i = 1;

  public static void main(String[] args) {
	 //局部常量，同样使用final修饰
	 final int j = 2;
	 
	 System.out.println(i);
	 System.out.println(j);
  }
}
```

## 6、运算符

1. Java 语言支持如下运算符：
	1. 算数运算符：`+(加)、-(减)、*(乘)、/(除)、%(模，求余)、++(自增)、--(自减)`
	2. 关系运算符：`>(大于)、<(小于)、>=(大于等于)、<==(小于)、==(等于)、!=(不等于)、instanceof`
	3. 逻辑运算符：`&&(与)、||(或)、!(非)`
	4. 赋值运算符：`=(把后面的赋值给前面的)`
	5. 扩展赋值运算符：`+=、-=、*=、/=`
	6. 条件运算符：`?、:`
	7. 位运算符：`&(按位与)、|(按位或)、^(按位或)、~(取反)、>>(左移)、<<(右移)、>>>（无符号右移)`
2. 自增自减运算符（一元运算符）：
	1. 一元运算符在变量后（`b = a++`）：先赋值后自增自减
	2. 一元运算符在变量前（`b = ++a`）：先自增自减后赋值
```java
//++ -- ，自增自减运算符（一元运算符）
int a = 3;
int b = a++;
int c = ++a;

System.out.println(a);  //结果：5
System.out.println(b);  //结果：3
System.out.println(c);  //结果：5
```

3. 数学工具类（Math）：很多运算会使用工具类进行操作，此处了解，以后深挖

```java
//幂运算，2^3，2*2*2
double pow = Math.pow(2,3);
System.out.println(pow);

//求最大值，在一些数中选择一个最大值
double max = Math.max(2,3);
System.out.println(max);
```

4. 逻辑运算符：&&（与，and）、||（或，or）、!（非，取反）
	1. 逻辑与运算：所有变量都为真，结果才为真（true），只要有一个为假，结果就为假（false）
		1. 逻辑与有短路的一种情况，如：(a&&b)，若a为假，则不会判断b值的真假，此称之为短路
	2. 逻辑或运算：有一个变量为真，结果就为真（true），所有变量都为假，结果才为假（false）
	3. 逻辑非运算：如果是真，则变为假；如果是假，则变为真

```java
boolean a =  true;                           //a为真
boolean b = false;                           //b为假

System.out.println("a && b："+(a&&b));       //结果：false，a和b中b为假，则a和b为假
System.out.println("a || b："+(a||b));       //结果：true， a或b中a为真，则a或b为真
System.out.println("!(a && b)："+!(a&&b));   //结果：true， a和b中b为假，则a和b为假，则非a和b为真
System.out.println("!(a || b)："+!(a||b));   //结果：false，a或b中a为真，则a或b为真，则非a或b为假
```

5. 位运算符：两个二进制数每一位分别进行比较，因为是直接与二进制打交道，故<font color="red">效率极高</font>

```java
A = 0011 1100
B = 0000 1101

A&B = 0000 1100   //按位与：对比的值都为1结果才为1，否则为0，有一个0就为0
A|B = 0011 1101   //按位或：对比的值都为0结果才为0，否则为1，有一个1就为1
A^B = 0011 0001   //按位异或：对比的值相同结果为0，不同结果为1
~A  = 1100 0011   //取反：1变为0，0变为1
~B  = 1111 0010   //取反：1变为0，0变为1
-----------------------------------------------------------------------
0000 0000      0
0000 0001      1
0000 0010      2
0000 0011      3
0000 0100      4
0000 1000      8
0001 0000      16          //1每向前移一位，数变大一倍（*2）

<<：前移，相当于*2
>>：后移，相当于/2

2 *8 = 16，可分解为：2*2*2*2

System.out.println(2<<3);  //结果：16.相当于2的三次方
```

6. 扩展赋值运算符：

```java
int a = 10;
int b = 20;

a += b;     //结果：30  ，a = a + b
a -= b;     //结果：-10 , a = a - b
a *= b;     //结果：200 , a = a * b
a /= b;     //结果：0   , a = a / b
```

7. 条件运算符（三元运算符）：`x ? y : z`  ，如果 `x == true`，则结果为 y，否则结果为 z

```java
int score = 80;                                 //设一个分数为80
String type = score <60 ? "不及格" : "及格";    //分数小于60则输出不及格，大于或等于60则输出及格
System.out.println(type);                       //结果：及格
```

8. 字符串连接符：`+`，String 类型；若 `+` 在 String 类型字符串前面，则可以执行计算，若是在字符串后面，则只能进行字符串的拼接

```java
int a = 10;
int b = 20;

System.out.println(a+b+"字符串");   // 结果：30 字符串
System.out.println("字符串"+a+b);   // 结果：字符串 1020
```

## 7、包机制（文件夹）

1. 为了更好的组织类，Java 提供了包机制，用于区别类名的命名空间
2. 包语句的语法格式为：

```java
package pkg1[. pkg2[. pkg3...]];
```

3. <font color="red">一般利用公司域名倒置作为包名</font>，如：`com.baidu.www`
4. 为了能够使用某一个包的成员，我们需要在 Java 程序中明确导入该包，使用 `import` 语句

```java
import package1[. pkg2...].(classname|*);
```

## 8、Java Doc

1. JavaDoc 命令是用来生成自己 API 文档的

```java
@author     //作者名
@version    //版本号
@since      //指明需要最早使用的jdk版本
@param      //参数名
@return     //返回值情况
@throws     //异常抛出情况
```

2. 例子，加在类上面就是类的注释，加在方法上面就是方法的注释

```java
/**
* @author 言
* @version 1.0
* @since 1.8
*/
public class Doc {
	String name;
	
	/**
	* 
	* @param name
	* @return
	* @throws Exception
	*/
	public String test(String name) throws Exception{
		return name;
	}
}
```

## 9、IDEADebug
 
1. 在需要 Debug 的代码最面前单击，建立 Debug 点，可以设置多个

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、Debug01.png)

2. 选择方法名右键并右键，点击 Debug

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F04、Debug02.png)

3. Debug 界面按钮

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F05、Debug03.png)

# 三、Java 流程控制

## 1、用户交互 Scanner

1. Java 提供了一个工具类，可以获取用户的输入，`java.util.Scanner` 是 Java5 的新特征
2. 通过 Scanner 类的 `next()` 与 `nextLine()` 方法获取输入的字符串，在读取前我们一般需要使用 `hasNext()` 与 `hasNextLine()` 判断是否还有输入的数据。
3. 基本语法：

```java
Scanner s = new Scanner(System.in);
```
   
4. `scanner.next()` 语法：
	1. 一定要读取到有效字符才可以结束输入
	2. 对输入有效字符之前遇到的空白，`next()` 方法会自动将其去掉
	3. 只有输入有效字符后才将其后面的空白作为分隔符或者结束符
	4. 故，<font color="red">next() 不能得到带有空格的字符串，此方法使用也较少</font>

```java
import java.util.Scanner;

public class Demo01 {

	public static void main(String[] args) {
		//创建一个扫描器对象，用于接收键盘数据
		//System.in：in为接收数据
		Scanner scanner = new Scanner(System.in);     

		System.out.println("使用next方式接收：");

		//判断用户有没有输入字符串，有输入则执行
		if (scanner.hasNext()){
			//使用next方式接收，程序会等待用户输入
			String str = scanner.next();
			System.out.println("输入的内容为："+str);
		}
		//凡是输入IO流的类如果不关闭会一直占用资源，要养成好习惯用完就关掉
		scanner.close();
	}
}
```

```shell
请输入：
Hello world
输入的内容为：Hello

Process finished with exit code 0
```

5.  `scanner.nextLien()` 语法
	1. 以 Enter 为结束符，也就是说 `nextLien()` 方法返回的是输入回车之前的所有字符
	2. 可以得到带有空格的字符串
	3. <font color="red">一般使用此方法</font>

	```java
import java.util.Scanner;

public class Demo02 {

	public static void main(String[] args) {
		//创建一个扫描器对象，用于接收键盘数据
		//System.in：in为接收数据
		Scanner scanner = new Scanner(System.in);

		System.out.println("使用nextLine方式接收：");

		//判断用户有没有输入字符串
		if (scanner.hasNextLine()){
			//使用nextLine方式接收，程序会等待用户输入
			String str = scanner.nextLine();
			System.out.println("输入的内容为："+str);
		}
		//凡是输入IO流的类如果不关闭会一直占用资源，要养成好习惯用完就关掉
		scanner.close();
	}
}
	```

6. 输入整数与小数

```java
import java.util.Scanner;

public class Demo03 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		//从键盘接收数据
		int i = 0;
		float f = 0.0f;

		System.out.println("请输入整数：");
		//判断输入的是不是整数
		if (scanner.hasNextInt()){
			//将输入的整数类型数据赋值给i
			i = scanner.nextInt();
			System.out.println("整数数据："+i);
		}else{
			System.out.println("输入的不是整数数据！");
		}

		System.out.println("请输入小数：");
		//判断输入的是不是小数
		if (scanner.hasNextFloat()){
			//将输入的小数类型数据赋值给f
			f = scanner.nextFloat();
			System.out.println("小数数据："+f);
		}else{
			System.out.println("输入的不是小数数据！");
		}
		scanner.close();
	}
}
```

```shell
----结果1-------------------------------------------------
请输入整数：
1
整数数据：1
请输入小数：
2
小数数据：2.0

Process finished with exit code 0

----结果2-------------------------------------------------
请输入整数：
1.1
输入的不是整数数据！
请输入小数：
小数数据：1.1

Process finished with exit code 0
```

7. 输入多个数字
	1. 可以输入多个数字，并求其总和与平均数
	2. 每输入一个数字用回车来确定，通过输入非数字来结束输入并输出结果

```java
import java.util.Scanner;

public class Demo04 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		//总和
		double sum = 0;
		//循环次数
		int m = 0;

		//如果输入的double类型的字符，则进行循环
		while (scanner.hasNextDouble()){
			//将输入的double类型的数字赋值给double类型的变量x
			double x = scanner.nextDouble();
			//记录循环次数，每循环一次就加一
			m = m + 1;
			//输入的数字的总和，每输入一个数字就相加
			sum = sum + x;

			//输出循环的次数与当前的总和
			System.out.println("当前输入的"+m+"数据的个和为："+sum);
		}
		//输出总的循环的次数与总和
		System.out.println("总共输入的"+m+"数据的个和为："+sum);

		//关闭资源
		scanner.close();
	}
}
```

```shell
----结果-------------------------------------------------
1
当前输入的1数据的个和为：1.0
2
当前输入的2数据的个和为：3.0
3
当前输入的3数据的个和为：6.0
1.1
当前输入的4数据的个和为：7.1
56.3
当前输入的5数据的个和为：63.4
z
总共输入的5数据的个和为：63.4

Process finished with exit code 0
```

## 2、顺序结构

1. Java 的基本结构就是顺序结构，除非特别指明，否则就按照顺序一句一句执行
2. 顺序结构是最简单的算法结构
3. 语句与语句之间，框与框之间是按从上到下的顺序进行的，它是由若干个依次执行的处理组成的
4. <font color="red">他是任何一个算法都离不开的一种基本算法结构</font>

## 3、选择结构

1. `if` 单选择结构：我们很多时候需要去判断一个东西是否可行，然后我们才去执行，这样一个过程在程序中用 `if` 语句来表示

```java
if(布尔表达式){
	// 如果布尔表达式的值为 true 则将要执行的语句
}
```
   
2. `if` 双选择结构：
	1. 现在有一个需求，公司要收购一个软件，成功了，给人支付 100 万；失败了，自己找人开发。
	2. 这样的需求用一个 `if` 就搞不定了，我们需要有两个判断，需要一个双选择结构，所以就有了 `if-else` 结构

```java
if(布尔表达式){
	//如果布尔表达式的值为true则将要执行的语句
}else{
	//如果布尔表达式的值为false则将要执行的语句
}
   ```
   
3. `if` 多选择结构：实际情况中选择可能不仅仅是两个，还存在区间多级判断，所以需要一个多选择结构来处理这类问题
```java
if(布尔表达式 1 ){
	//如果布尔表达式 1 的值为true则将要执行的语句
}else if(布尔表达式 2 ){
	//如果布尔表达式 2 的值为true则将要执行的语句
}else if(布尔表达式 3 ){
	//如果布尔表达式 3 的值为true则将要执行的语句
}else{
	//如果以上布尔表达式都不为true则执行此语句
}
```

4. 嵌套的 `if` 结构：
	1. 使用嵌套的 `if...else` 语句是合法的
	2. 也就是说可以在另一个 `if` 或者 `else if` 语句中使用个 `if` 或者 `else if` 语句，你可以像 `if` 语句一样嵌套 `else if...else` 语句
	3. 无限套娃

```java
if(布尔表达式 1 ){
	//如果布尔表达式 1 的值为true则将要执行的语句
	if(布尔表达式 2 ){
		//如果布尔表达式 2 的值为true则将要执行的语句
		if(布尔表达式 3 ){
			//如果布尔表达式 3 的值为true则将要执行的语句
		}
	}
}
```
   
5. switch 多选择结构:
	1. 多选择结构还有一个实现方式就是 `switch case` 语句
	2. `switch case` 语句判断一个变量与一系列值中的某个值是否相等，每个值成为一个分支
6. `switch` 语句中的变量类型可以是：
	1. `byte`、`short`、`int`、或者 `char`
	2. 从 Java SE 7 开始，`switch` 支持 `String` 类型了
	3. 同时 `case` 标签必须为字符串常量或字面量

```java
switch(expression){ //判断表达式
	case value 1 :
		//语句
		break;      //可选，没有此语句程序会继续输出下面的语句，不管满不满足条件，直到判断结束或遇到break语句
	case value 2 :
		//语句
		break;
	case value 3 :
		//语句
		break;

	//你可以有任意数量的case语句

	default :       //可选，若上方的判断没有匹配的，则执行此语句
		//语句
}
```

7. 另，流程控制的源码，代码文件与反编译文件的对比，<font color="red">字符的本质还是数字</font>

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、switch多选择结构，源码.png)

## 4、循环结构

1. `while` 循环，`while` 是最基本的循环，他的结构为：
	1.  只要布尔表达式为 true，循环就会一直执行下去
	2. 我们大多数情况是会让循环停止下来的，我们需要一个让表达式失效的方式来结束循环
	3. 少部分情况需要循环一直执行，比如服务器的请求相应监听等
	4. 循环条件一直为true就会造成无限循环【死循环】，我们正常的业务变成中应该尽量避免死循环，会影响程序性能或者造成程序卡死崩溃

   ```java
    while(布尔表达式){
        //循环内容
    }
   ```
   
2. `do...while` 循环：
	1.  对于 `while` 语句而言，如果不满足条件，则不能进入循环，但有时候我们需要即使不满足条件，也至少执行一次
	2. `do...while` 循环和 `while` 循环相似，不同的是，`do...while` 循环至少会执行一次
	3. `while` 先判断后执行，`do...while` 先执行后判断
	4. <font color="red">语句开始时会先执行do后面的语句，然后再进行while中的表达式判断，若为true，则继续执行do后面的语句；若为false，则结束循环</font>

```java
do{
	//代码语句
}while(布尔表达式){
	//可选，循环结束时执行
};
```
   

3. `for` 循环
	1.  虽然所有的循环结构都可以用 `while` 或者 `do...while` 表示，但 Java 提供了另一种语句： `for` 循环，使一些循环结构变得更加简单
	2. `for` 循环语句是支持迭代的一种通用结构，是最有效、最灵活的循环结构
	3. `for` 循环执行的次数是在执行前就确定的，
	4. <font color="red">嵌套的 for 循环会从外侧依次执行一次，然后执行完最里面的一层；再第二次依次从外侧执行</font>
	5. 关于 `for` 循环有以下几点说明：
		1. 最先执行初始化步骤，可以声明一种类型，但可以初始化一个或多个循环控制变量，也可以是空语句。
		2. 然后，检测布尔表达式的值，如果为 `true`，循环体被执行。如果为 `false`，循环终止，开始执行循环体后面的语句
		3. 执行一次训话后，更新循环控制变量（迭代银子控制循环变量的增减）
		4. 再次检测布尔表达式，循环执行上面的过程。

```java
for(初始化；布尔表达式；更新){
	//代码语句
}

----例子 1 ----

//分别算出100以内的偶数和与奇数和
public class Demo02 {
	public static void main(String[] args) {
		//奇数和
		int oddSun = 0;
		//偶数和
		int evenSun = 0;

		for (int i = 0; i < 100; i++) {
			if (i%2!=0){
				oddSun = oddSun + i;
			}else{
				evenSun = evenSun + i;
			}
		}
		System.out.println("奇数和："+oddSun);
		System.out.println("偶数和："+evenSun);
	}
}

----例子 2 ----

//输出1~1000之间能被5整除的数，并且每行输出3个
public class Demo03 {
	public static void main(String[] args) {

		for (int i = 0; i <= 1000; i++) {
			//i除5求余，如果等于0则进行循环
			if (i%5==0){
				//输出i与一个空格
				System.out.print(i+"\t");
			}
			//i除15（3个5）求余，如果等于0则进行循环
			if (i%(5*3)==0){
				//输出一个换行
				System.out.println();
			}
		}
	}
}

----例子 3 ----

//打印九九乘法表
public class Demo04 {
	public static void main(String[] args) {
		//第一层for循环，设定行数
		for (int i=1;i<=9;i++){
			//第二层for循环，设定列数，然后通过i来规定j的最大值
			for (int j=1;j<=i;j++){
				System.out.print(i+"+"+j+"="+(i*j)+"\t");
			}
			System.out.println();
		}
	}
}

```

4. 增强型 for 循环（在 Java5 中引入）

```java
for(声明语句 : 表达式){
	//代码句子
}

----例子 1 ----

public class Demo05 {
	public static void main(String[] args) {
		int[] numbers = {10,20,30,40,50};

		//遍历数组的元素
		for (int i : numbers){
			System.out.println(i);
		}
	}
}
```

   5. 此处了解，学习数组之后在重点使用，增强型 `for` 循环主要是用来遍历数组

## 5、循环跳出 break & continue

1. `break`：`break` 在任何循环语句的主体部分，均可用 `break` 控制循环的流程；`break` 用于<font color="red">强行退出循环</font>，不执行循环中剩余的语句，`break` 语句也在 `switch` 语句中使用
2. `continue`：`continue` 语句用在循环语句体中，用于终止某次循环过程，即跳过循环体中尚未执行的语句，接着进行下一次是否执行循环的判定

## 6、练习，打印三角形

```java
//打印三角形
public class Demo06 {
    public static void main(String[] args) {
        //第一层循环，定义行数，
        for (int i=1;i<=5;i++){
            //第2.1层循环，打印三角形前面的空白
            //j初始化为5，条件为j>=i，每次循环j减1，故第一次循环5次
            //第一行（第一次循环）打印5个空格，第二行打印4个空格等
            for (int j=5;j>=i;j--){
                System.out.print(" ");
            }
            //第2.2层循环，在2.1层循环结束之后开始，打印三角形的中线及左侧
            //j初始化为1，条件为j<=i，每次循环j加1，故第一次循环1次
            //第一行（第一次循环）打印1个*，第二行打印2个*等
            for (int j=1;j<=i;j++){
                System.out.print("*");
            }
            //第2.3层循环，在2.2层循环结束之后开始，打印三角形的右侧
            //j初始化为1，条件为j<i，每次循环j加1，故第一次循环0次
            //第一行（第一次循环）不打印，第二行打印1个*等
            for (int j=1;j<i;j++){
                System.out.print("*");
            }
            //每次第2层循环结束后打印一个换行
            System.out.println();
        }
    }
}
```

# 四、Java 方法

## 1、什么是方法

1. `System.out.println()` 是什么？
	1. `System` 是类
	2. `out` 是对象
	3. `println()` 就是方法
	4. 总：调用系统类 `System` 里面的标准输出对象 `out` 中的 `println()` 方法
2. Java 方法是语句的集合，他们在一起执行一个功能
	1. 方法是解决一类问题的步骤的有序组合
	2. 方法包含于类或对象中
	3. 方法在程序中被创建，在其他地方被引用
3. 设计方法的原则：方法的本意是功能模块，就是某个功能的语句块的集合，我们设计方法的时候，最好保持方法的原子性：<font color="red">一个方法只完成一个功能，这样有利于我们后期的扩展</font>
4. 方法的命名规则：首字母小写和驼峰原则：`run()`，`runRun()`，除了第一个单词以外，后面的单词首字母大写

```java
public class Demo01 {
	// main方法
	public static void main(String[] args) {
		// 调用 add 方法，并传入 a=1,b=2
		int sum = add(1,2);                     // 1 和 2 为实参
		System.out.println(sum);
	}
}

// 加法方法
// public static：修饰符
// int：返回值类型，对应return a+b中a+b的类型
// add(int a,int b)，方法名，以及需要传入的参数
public static int add(int a,int b){         // a 和 b 为形参
	//返回值
	return a+b;
}
```

## 2、方法的定义及调用

### ①、方法的定义

1. Java 的方法类似于其他语言的函数，是一段<font color="red">用来完成特定功能的代码片段</font>
2. <font color="red">方法包含一个方法头和一个方法体</font>，下面是一个方法的所有部分：
	1. <font color="red">修饰符</font>：修饰符，这是可选的，告诉编辑器如何调用该方法，定义了该方法的访问类型
	2. <font color="red">返回值类型</font>：方法可能会有返回值，returnValueType是方法返回值的数据类型。有些方法执行所需的操作，但没有返回值，在这种情况下，returnValueType是关键字void
	3. <font color="red">方法名</font>：是方法名的实际名称，方法名和参数表示共同构成方法签名
	4. <font color="red">参数类型</font>：参数像是一个占位符，当方法被调用时，传递值给参数，这个值被称为实参或变量。参数列表是指方法的参数类型、顺序和参数的个数。参数是可选的，方法可以不包含任何参数
		1. 形式参数（形参）：在方法被调用时用于接收外界输入的数据，定义方法时方法名后面定义的参数
		2. 实际参数（实参）：调用方法时实际传递给方法的数据
	5. <font color="red">方法体</font>：方法体包含具体的语句，定义该方法的功能

```java
修饰符 返回值类型 方法名(参数类型 参数名){
   ...
   方法体
   ...
}
```

### ②、方法的调用

1. 调用方法：对象名.方法名(实参列表)
2. Java 支持两种调用方法的方式，根据方法是否返回值来选择
3. 当方法返回一个值的时候，方法调用通常被当做一个值，例如：

```java
int larger = max(30,40);
```
 
4. 如果方法返回值是 void，方法调用一定是一条语句，例如：

```java
System.out.println("Hello,kuangshen");
```

5. 例子

```java
public class Demo02 {
	public static void main(String[] args) {
		int larger = max(30,40);
		System.out.println(larger);
	}

	//比大小
	public static int max(int num1,int num2){
		int result = 0;

		if (num1>num2){
			result = num1;
		}else{
			result = num2;
		}

		if (num1 == num2){
			System.out.println("num1 == num2");
			//终止方法
			return 0;
		}

		return result;
	}
}
```

### ③、值传递和引用传递

1. Java 都是值传递
2. 值传递：只要是基本类型传递，都是值传递
3. 引用传递：针对于基本类型进行封装，对封装进行传递，是引用传递

### ④、方法的重载

1. 重载就是在一个类中，有相同的函数名称，但形参不同的函数
2. 方法重载的规则：
	1. <font color="red">方法名称必须相同</font>
	2. <font color="red">参数列表必须不同</font>（个数不同、类型不同、或参数排列顺序不同等）
	3. 方法返回类型可以相同也可以不同
	4. 仅仅返回类型不同不足以成为方法的重载
3. 实现理论：方法名相同时，编译器会根据调用方法的参数个数，参数类型等去逐个匹配，以选择对应的方法，如果匹配失败，则编译器报错

```java
//方法的重载
public class Demo02 {
	public static void main(String[] args) {
		//调用第一个max方法，传入int类型的参数
		int larger = max(30,40);
		//调用第二个max方法，传入double类型的参数
		double larger2 = max(30.2,40.2);

		System.out.println(larger);
		System.out.println(larger2);
	}

	//比大小，接收int类型的参数
	public static int max(int num1,int num2){
		int result = 0;

		if (num1>num2){
			result = num1;
		}else{
			result = num2;
		}

		if (num1 == num2){
			System.out.println("num1 == num2");
			//终止方法
			return 0;
		}

		return result;
	}

	//比大小，接收double类型的参数
	public static double max(double num1,double num2){
		double result = 0;

		if (num1>num2){
			result = num1;
		}else{
			result = num2;
		}

		if (num1 == num2){
			System.out.println("num1 == num2");
			//终止方法
			return 0;
		}

		return result;
	}
}
```
## 3、命令行传参

1. 有时候希望运行一个程序的时候再传递给他消息，这要靠传递命令行参数给 `main()` 函数实现

```java
public class CommandLine {
	public static void main(String[] args) {
		for(int i=0;i<args.length;i++>){
			System.out.println("args["+i+"]:"+args[i]);
		}
	}
}
```

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、命令行传参.png)

## 4、可变参数

1. JDK1.5 开始，Java 支持传递同类型的可变参数给一个方法
2. 在方法声明中，在指定参数类型后加一个省略号 `...`
3. 一个方法中只能指定一个可变参数，他必须是方法的最后一个参数，任何普通的参数必须在他之前声明

```java
public class Demo03 {
	public static void main(String[] args) {
		Demo03 demo03 = new Demo03();
		demo03.test(1,1,2,3,4,5);
	}

	//可变参数，本本质是数组
	//a为普通参数，接收正常数据的传入
	//j为可变参数，接收数组的传入
	public void test(int a,int... j){
		//打印普通参数
		System.out.println("普通参数："+a);
		//设置循环，最大小于可变参数j的长度
		for (int i = 0; i < j.length; i++) {
			//打印传入的参数
			System.out.print("可变参数："+j[i]+",");
		}
	}
}
```

## 5、递归

> 一种思想的学习，但是对电脑性能有影响，能不用就不用

1. A 方法调用 B 方法，我们很容易理解
2. 递归就是：A 方法调用 A 方法，就是自己调用自己
3. 递归结构包括两个部分：
	1. 递归头：什么时候不调用自身方法，如果没有头，将陷入死循环
	2. 递归体：什么时候需要调用自身方法
4. 利用递归可以用简单的程序来解决一些复杂的问题。它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大减少了程序的代码量。递归的能力在于用有限的语句来定义对象的无限集合
```java
//递归
public class Demo04 {
	public static void main(String[] args) {
		System.out.println(f(5));
	}

	//阶乘：x!，如：
	//2的阶乘：2! = 2*1
	//3的阶乘：3! = 3*2*1
	//4的阶乘：4! = 4*3*2*1
	public static int f(int n){
		//如果判断输入的是1，则返回1并结束语句
		if (n==1){
			return 1;
		//如果判断输入的不是1，则执行下面的语句
		}else{
			//1，f(5)中，输入的是5，则执行5*f(4)
			//2，f(4)中，输入的是4，则执行4*f(3)
			//3，f(3)中，输入的是3，则执行3*f(2)
			//4，f(2)中，输入的是2，则执行2*f(1)
			//5，f(1)中，输入的是1，则返回1并结束语句
			//6，故，f(5)=5*f(4)，f(4)=4*f(3)，f(3)=3*f(2)，f(2)=2*f(1)，f(1)=1
			//7，故，f(5)=5*4*3*2*1
			return n*f(n-1);
		}
	}
}
```

![|675](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、递归.png)

## 6、作业，计算器

1. 写 4 个方法，加减乘除
2. 利用循环 + `switch` 进行交互
3. 传递需要操作的两个数
4. 输出结果 `x`
```java
public class Demo05 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		double s1 = 0;
		double s2 = 0;
		double s3 = 0;
		String s = "";
		String yn = "";

		do {
			System.out.println("----------------------------------------");
			System.out.print("请输入第一个数字：");
			if (scanner.hasNextDouble()){
				s1 = scanner.nextDouble();
			}else{
				System.out.println("输入错误，请重新输入");
				continue;
			}

			System.out.print("请输入第二个数字：");
			if (scanner.hasNextDouble()){
				s2 = scanner.nextDouble();
			}else{
				System.out.println("输入错误，请重新输入");
				continue;
			}

			System.out.print("请输入加减乘除中的一种运算符：");
			if (scanner.hasNext()){
				s = scanner.next();
			}else{
				System.out.println("输入错误，请重新输入");
				continue;
			}


			switch (s){
				case "+":
					s3 = s1 + s2;
					System.out.println("结果为："+s1+s+s2+"="+s3);
					break;
				case "-":
					s3 = s1 - s2;
					System.out.println("结果为："+s1+s+s2+"="+s3);
					break;
				case "*":
					s3 = s1 * s2;
					System.out.println("结果为："+s1+s+s2+"="+s3);
					break;
				case "/":
					s3 = s1 / s2;
					System.out.println("结果为："+s1+s+s2+"="+s3);
					break;
			}

			System.out.print("是否继续(y/n)：");
			if (scanner.hasNext()){
				yn = scanner.next();
			}



		}while (yn.equals("y"));

		System.out.println("计算器结束");

		scanner.close();

	}
}
```

# 五、Java 数组

## 1、数组概述，数组的定义

1. 数组是相同类型数据的有序集合
2. 数组描述的是相同类型的若干个数据，按照一定的先后次序排列组合而成
3. 其中，每一个数据称作一个数组元素，每个数组元素可以通过一个下标来访问他们

## 2、数组声明创建

### ①、数组声明创建

1. 首先，必须声明数组变量，才能在程序中使用数组，下面是声明数组变量的语法

```java
int[] arr;   //创建（声明）一个 int 类型的数组 arr，推荐使用

int arr2[];   //创建（声明）一个 int 类型的数组 arr2，但不推荐使用
```

2. Java 语言使用 new 操作符来创建数组，语法如下

```java
int[] arr = new int[10];    //创建（声明）一个 int 类型的数组 arr，并规定其数组空间为 10

//给数组中的元素赋值
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
arr[3] = 4;
arr[4] = 5;
```

3. 数组的元素是通过索引访问的，数组索引从 0 开始
4. 获取数组的长度：

```java
//数组名称.length
arr.length;
```

5. 计算数组元素的总和

```java
public class Demo01 {
	public static void main(String[] args) {

		//创建int类型的数组arr，并规定空间为10
		int[] arr = new int[10];

		//循环给数组元素赋值
		for(int i = 0 ; i <10 ; i++){
			arr[i] = i + 1;
		}

		int sum = 0;
		//计算数组元素的总和，最大循环次数小于数组的长度
		for (int i = 0 ; i < arr.length ; i++) {
			sum = sum + arr[i];
		}
		System.out.println(sum);
	}
}
```

### ②、内存分析



1. 堆：
	1. 存放 new 的对象和数组
	2. 可以被所有的线程共享，不会存放别的对象引用
2. 栈
	1. 存放基本变量类型（会包含这个基本类型的具体数值）
	2. 引用对象的变量（会存放这个引用在堆里里面的具体地址）
3. 方法区
	1. 可以被所有的线程共享
	2. 包含了所有的 `class` 和 `static` 变量
4. 声明数组时，会在栈里压入数组(arr)
   
```java
int[] arr;
```

5. 创建数组时，会在堆里开辟一个空间（此处为10）

```java
arr = new int[10];
```

6. 给数组赋值时，则堆中的空间被赋值

```java
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
arr[3] = 4;
arr[4] = 5;
```

![|625](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、内存分析.png)

### ③、三种初始化

1. 静态初始化

```java
// 静态初始化，int[0]=1,int[1]=2 等，创建一开始就赋值
int[] arr = {1,2,3,4,5,6,7,8};
```

2. 动态初始化

```java
// 动态初始化，包含默认初始化
int[] arr = new int[10];

// 创建一开始不赋值，使用时再赋值
arr[0] = 1;
arr[1] = 2;
```

3. 默认初始化：
	1. 数组时引用类型，他的元素相当于类的实例变量，因此数组一经分配空间，其中的每个元素也被按照实例变量同样的方式被隐式初始化
	2. 故，只要声明并创建了数组（分配的空间），即使并没有给数组中的元素赋值，也是有默认值的

### ④、数组的四个基本特点

1. 其长度是确定的，数组一旦被创建，他的长度就是不可以改变的
2. 其元素必须是相同的类型，不允许出现混合类型
3. 数组中的元素可以是任何数据类型，包括基本类型和引用类型
4. 数组变量属于引用类型，数组也可以看成是对象，数组中的每个元素相当于该对象的成员变量。数组本身就是对象，Java 中对象是在堆中的，因此数组无论保存原始类型还是其他对象类型，<font color="red">数组对象本身是在堆中的</font>

### ⑤、数组越界

1. 具体来说就是遍历的数组下标大于数组分配的空间长度，导致无法遍历此元素，故称越界
2. 若越界，则报：`ArrayIndexOutofBounds`

```java
// 声明创建数组，并赋值
// arr[0]=1，arr[1]=2
int[] arr = {1,2};

// 打印数组元素arr[2]，但创建的数组只有arr[0]和arr[1]，故会数组越界
System.out.println(arr[2]);
```

## 3、数组使用

1. `For-Each` 循环

```java
public class Demo03 {
  public static void main(String[] args) {
	 //声明创建并给数组赋值
	 int[] arr = {1,2,3,4,5};

	 //For-Each循环，JDK1.5加入，但是没有下标
	 //循环条件(int i : arr)中：arr为数组名称，i为数组元素
	 for (int i : arr) {
		   //打印数组元素
		   System.out.println(i);
	 }
  }
}
```

2. 数组做方法入参

```java
public class Demo04 {
  public static void main(String[] args) {
	 //声明创建并给数组赋值
	 int[] arr = {1,2,3,4,5};

	 //调用prinArray方法，传入arr数组
	 prinArray(arr);
  }

  //数组做方法入参
  //循环遍历arr数组，规定传入的参数为数组arr
  public static void prinArray(int[] arr){
	 for (int i = 0 ; i < arr.length ; i++){
		   System.out.println(arr[i]);
	 }
  }
}
```

3. 数组做返回值

```java
public class Demo05 {
  public static void main(String[] args) {
	 //声明创建并给数组赋值
	 int[] arr = {1,2,3,4,5};

	 //调用reverse方法并传入arr数组（reverse(arr)）
	 //并将reverse方法返回的数组赋值给刚创建的reverse数组
	 int[] reverse = reverse(arr);

	 //调用prinArray方法，传入reverse数组，遍历reverse数组
	 prinArray(reverse);
  }

  //反转数组，将传入的数组反向输出
  //规定返回值为int类型的数组，传入的参数为int类型的数组
  public static int[] reverse(int[] arr){
	 //声明创建数组，使用传入的arr数组的长度为result数组开辟空间
	 int[] result = new int[arr.length];

	 for (int i = 0; i < arr.length; i++) {
		   //将arr数组的最高位赋值给result数组的最低位，反向输出
		   result[i] = arr[arr.length-1-i];
	 }
	 //返回result数组
	 return result;
  }

  //数组做方法入参
  //循环遍历arr数组，规定传入的参数为int类型的数组
  public static void prinArray(int[] arr){
	 for (int i = 0;i<arr.length;i++){
		   System.out.println(arr[i]);
	 }
  }
}
```

## 4、多维数组


1. 多维数组可以看成是数组的数组，比如二维数组就是一个特殊的一维数组，其中每一个元素都是一个一维数组
2. 二维数组：该二维数组可以看成一个两行五列的数组

```java
int arr[][] = new int[2][5]
```

3. 多维数组：数组套数组。以上面的二维数组来说，就是在栈里开辟了 2 个空间，然后分别又在这两个空间里各开辟了 5 个空间

```java
public class Demo06 {
  public static void main(String[] args) {

	 //动态初始化
	 //声明数组
	 int [][] arr;
	 //创建数组
	 arr = new int[2][5];
	 //给数组赋值
	 arr[0][0] = 1;
	 arr[0][1] = 2;
	 arr[0][2] = 3;
	 arr[0][3] = 4;
	 arr[0][4] = 5;

	 arr[1][0] = 6;
	 arr[1][1] = 7;
	 arr[1][2] = 8;
	 arr[1][3] = 9;
	 arr[1][4] = 10;

	 //静态初始化，声明创建数组，并给数组赋值
	 int [][] arr2 = {{1,2,3,4,5},{6,7,8,9,10}};
  }
}
```

![|400](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、多维数组.png)

4. 打印二维数组

```java
public class Demo07 {
  public static void main(String[] args) {

	 // 二维数组
	 // 静态初始化，声明创建数组，并给数组赋值
	 // 数组空间同：int arr[][] = new int[2][5]
	 int [][] arr = {{1,2,3,4,5},{6,7,8,9,10}};

	 // 第一层 for 循环，起始为0，最大长度小于arr数组第一层的长度（第一层花括号的数量）
	 for (int i = 0; i <arr.length ; i++) {
		   // 第二层for循环，起始为0，最大长度小于arr数组第二层的长度（第一层花括号中的，第二层花括号的数量）
		   for (int j = 0; j <arr[0].length ; j++) {
			  System.out.println(arr[i][j]);
		   }
	 }

  }
}
```

5. 三维四维数组或其他更高维的数组与与二维相同，都是数组套数组，一般不会使用三维及更高维的数组

```java
public class Demo08 {
  public static void main(String[] args) {

	 // 三维数组
	 // 静态初始化，声明创建数组，并给数组赋值
	 // 数组空间同：int arr[][][] = new int[3][2][3]
	 int [][][] arr = { { {1,2,3} , {4,5,6} } , { {7,8,9} , {10,11,12} } , { {13,14,15} , {16,17,18} } };

	 // 第一层for循环，起始为0，最大长度小于arr数组第一层的长度（第一层花括号的数量）
	 for (int i = 0; i <arr.length ; i++) {
		   // 第二层for循环，起始为0，最大长度小于arr数组第二层的长度（第一层花括号中的，第二层花括号的数量）
		   for (int j = 0; j <arr[0].length ; j++) {
			  // 第三层for循环，起始为0，最大长度小于arr数组第三层的长度（第一层花括号中的，第二层花括号的中的，第三层花括号的数量）
			  for (int z = 0; z <arr[0][0].length ; z++) {
				 // 反斜杠t为每打印完一个元素打印一个空格
				 System.out.print(arr[i][j][z]+"\t");
			  }
			  // 此处为每每循环完一次第三层打印一个回车
			  System.out.println();
		   }
	 }

  }
}
```

## 5、Arrays 类

1. 数组的工具类：`java.util.Arrays`
2. 由于数组对象本身并没有什么方法可以供我们调用，但 API 中提供了一个工具类 `Arrays` 供我们使用，从而可以对数据对象进行一些基本的操作
3. <font color="red">查看JDK帮助文档</font>
4. `Array` 类中的方法都是 `static` 修饰的静态方法，在使用的时候可以直接使用类名进行调用，而“不用”使用对象来调用（注意是“不用”，而不是“不能”）
5. `Array` 具有以下常用功能：
	1. 给数组赋值：通过 `fill` 方法
	2. 对数组排序：通过 `sort` 方法，按升序
	3. 比较数组  ：通过 `equals` 方法比较数组中元素是否相等
	4. 查找数组元素：通过 `binarySearch` 方法能对排序好的数组进行二分查找法操作

## 6、冒泡排序

1. 比较数组中两个相邻的元素，如果第一个数比第二个数大，我们就交换他们的位置
2. 每一次比较中，都会产生出一个最大，或者最小的数字
3. 下一轮则可以少一次排序
4. 一次循环，直到结束

```java
public class Demo10 {
  public static void main(String[] args) {
	 //声明创建并给数组赋值
	 int[] arr = {1,2,3,22,12,65,25,8,43,98,11};

	 //调用sort方法并传入arr数组，并将排序后返回的arr数组赋值给刚创建的arr2数组
	 int[] arr2 = sort(arr);
	 //调用Arrays类的toString()方法打印出arr2数组
	 System.out.println(Arrays.toString(arr2));
  }

  //冒泡排序
  public static int[] sort(int[] arr){
	 //临时（中间）变量
	 int temp = 0;

	 //第一层循环，判断要循环多少次，比数组长度少一，因为是两两比较
	 for (int i = 0; i <arr.length-1 ; i++) {
		   //第二层循环，最大循环次数为比数组长度少一，每循环一次最大循环次数减一
		   for (int j = 0; j <arr.length-1-i ; j++) {
			  //两两比较，如果第一个数比第二个数大，则交换位置
			  if (arr[j] > arr[j+1]){
				 //将第一个数的值赋给临时变量
				 temp = arr[j];
				 //将第二个数的值赋给第一个数
				 arr[j] = arr[j+1];
				 //将临时变量（第一个数）的值赋值给第二个数
				 arr[j+1] = temp;
			  }
		   }
	 }
	 //返回排序后的arr数组
	 return arr;
  }
  
}
```

## 7、稀疏数组

1. 当一个数组中大部分元素为 0，或者为同一值的数组时，可以使用稀疏数组来保存该数组
2. 稀疏数组的处理方式是：
	1. 记录数组一共有几行几列，有多少个不同值
	2. 把具有不同值的元素和行列及值记录在一个小规模的数组中，从而缩小程序的规模
3. 如下图，左边是原始数组，右边是稀疏数组

![|625](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、稀疏数组.png)

```java
   //稀疏数组实例
   public class Demo11 {
      public static void main(String[] args) {
         //声明并创建一个二维数组， 11*11 ，0：没有棋子，1：黑棋，2：白棋
         int[][] arr = new int[11][11];

         //给黑棋与白棋的位置赋值
         arr[1][2] = 1;
         arr[2][3] = 2;

         //循环打印数组
         for(int i = 0; i <arr.length ; i++){
               for(int j = 0; j <arr[0].length ; j++){
                  System.out.print(arr[i][j]+"\t");
               }
               System.out.println();
         }

         //分割线
         System.out.println("------------------------------------------------");

         //转换为稀疏数组保存
         //获取有效值的个数
         int sum = 0;
         //循环遍历数组
         for (int i = 0; i <arr.length ; i++) {
               for (int j = 0; j <arr[0].length ; j++) {
                  //比较每一个数组的元素，每遇到一个不等于0的数sum+1
                  if (arr[i][j] !=0 ){
                     sum++;
                  }
               }
         }
         System.out.println("有效值的个数："+sum);

         //声明并创建一个稀疏数组的二维数组，行数为有效值个数+1（第一行记录总行数与总列数），列数固定为3
         int[][] sparseArray = new int[sum+1][3];

         //给稀疏数组的第一行赋值
         //第一行第一个元素为arr数组的总行数
         sparseArray[0][0] = arr.length;
         //第一行第二个元素为arr数组的总列数
         sparseArray[0][1] = arr[0].length;
         //第一行第三个元素为arr数组的总有效值个数
         sparseArray[0][2] = sum;


         //遍历二维数组，将非零的值存放在稀疏数组中
         //定义一个临时数并赋值为1，表示稀疏数组的行数，因为第一行（arr[0][0]）已被赋值，故从1开始（arr[1][0]）
         int count = 1;
         //循环遍历数组
         for (int i = 0; i <arr.length ; i++) {
               for (int j = 0; j <arr[0].length ; j++) {
                  //比较每一个数组的元素，每遇到一个不等于0的数执行语句
                  if (arr[i][j] != 0){
                     //给第count行第一个元素赋值为i，为该元素在arr数组中的行数
                     sparseArray[count][0] = i;
                     //给第count行第二个元素赋值为j，为该元素在arr数组中的列数
                     sparseArray[count][1] = j;
                     //给第count行第三个元素赋值为arr[i][j]，为该元素在arr数组中的值
                     sparseArray[count][2] = arr[i][j];
                     //使count+1，为下一行赋值
                     count++;
                  }
               }
         }

         //打印稀疏数组
         System.out.println("稀疏数组：");

         System.out.println("行数|列数|总有效值个数");
         //打印稀疏数组的第一行
         System.out.println(sparseArray[0][0]+"\t"+sparseArray[0][1]+"\t"+sparseArray[0][2]);

         //循环遍历稀疏数组
         //行数从1开始，因为上面已经打印完第一行了
         for (int i = 1; i <sparseArray.length ; i++) {
               for (int j = 0; j <sparseArray[0].length ; j++) {
                  System.out.print(sparseArray[i][j]+"\t");
               }
               System.out.println();
         }

         //分割线
         System.out.println("------------------------------------------------");

         //还原稀疏数组
         ////声明并创建一个二维数组，行数为稀疏数组第一行的第一个元素（总行数），列数为稀疏数组第一行的第二个元素（总列数）
         int[][] arr2 = new int[sparseArray[0][0]][sparseArray[0][1]];

         //循环给arr2数组赋值，从1开始，因为sparseArray的第一行为总行数与总列数等
         for (int i = 1; i <sparseArray.length ; i++) {
               //sparseArray[1][0]为稀疏数组第二行的第一个元素，为第一个有效值的行数
               //sparseArray[1][1]为稀疏数组第二行的第二个元素，为第一个有效值的列数
               //sparseArray[1][2]为稀疏数组第二行的第三个元素，为第一个有效值的值
               arr2[sparseArray[i][0]][sparseArray[i][1]] = sparseArray[i][2];
         }

         //打印还原后的数组
         for (int i = 0; i <arr2.length ; i++) {
               for (int j = 0; j <arr2[0].length ; j++) {
                  System.out.print(arr2[i][j]+"\t");
               }
               System.out.println();
         }

      }
   }
```

# 六、面向对象

## 1、初识面向对象（OOP）

### ①、面向过程和面向对象

1. 面向过程思想：
	1. 步骤清晰简单，第一步做什么，第二步做什么
	2. 面向过程适合处理一些较为简单的问题
2. 面向对象思想：
	1. 物以类聚，分类的思想模式，思考问题首先会解决问题需要哪些分类，然后对这些分类进行单独思考。最后，才对某个分类下的细节进行面向过程的思索
	2. 面向对象适合处理复杂的问题，适合处理需要多人协作的问题
3. <font color="red">对于描述复杂的事务，为了从宏观上把握，从整体上合理分析，我们需要使用面向对象的思路来分析整个系统。但是，具体到围观操作，仍然需要面向过程的思路去处理</font>
4. 面向对象编程的英文是：Objet-Oriented Programming，简称 OOp
5. 面向对象编程的本质就是：<font color="red">以类的方式组织代码，以对象的形式组织（封装）数据</font>

### ②、<font color="red">核心思想：抽象</font>

1. 介绍：在面向对象的概念中，我们知道所有的对象都是通过类来描绘的，但是并不是所有的类都是用来描绘对象的，如果一个类中没有包含足够的信息来描绘一个具体的对象，这样的类就是抽象类。抽象类往往用来表征我们在对问题领域进行分析、 设计中得出的抽象概念，是对一系列看上去不同，但是本质上相同的具体概念的抽象，我们不能把它们实例化（拿不出一个具体的东西）所以称之为抽象。
2. 比如：我们要描述“水果”，它就是一个抽象，它有质量、体积等一些共性（水果有质量），但又缺乏特性（苹果、橘子都是水果，它们有自己的特性），我们拿不出唯一一种能代表水果的东西（因为苹果、橘子都不能代表水果），可用抽象类来描述它，所以抽象类是不能够实例化的。当我们用某个类来具体描述“苹果”时，这个类就可以继承描述“水果”的抽象类，我们都知道“苹果”是一种“水果”。
3. 抽象方法：被 `abstract` 修饰的方法是抽象方法，抽象方法没有方法体。`修饰符 abstract 返回值类型 函数名();` 抽象方法的修饰符只能用 `public` 、 `protected` 或者没有修饰，不能被 `final`，`static`，`private` 修饰。
	1. 类即使不包含抽象方法，也可以定义成抽象类。
	2. 类中含有抽象方法的类一定要定义成抽象类。
	3. 抽象类中字段的定义和子类的访问与一般类没有变化。
	4. 扩展抽象类有两种方法，第一种是在子类中定义部分抽象方法或者抽象方法不定义，这样子类也必须定义成抽象类，第二种是定义全部的抽象方法，这样子类就可以不定义成抽象的了
	5. 抽象类不能被实例化，但是可以定义一个抽象类的对象变量，这个变量可以引用非抽象子类的对象
	6. 抽象类中包含有构造方法，也可以显式书写构造方法，构造方法在实例化子类的对象中调用
4. 接口与抽象类的区别：
	1. 不同点：
		1. 接口可以多实现，而抽象类只能单继承
		2. 抽象类可以有非抽象的方法和构造方法、变量，但是接口只能有抽象方法，静态常量
		3. 抽象类和子类具有父子关系，子类能拥有父类中一些属性。接口虽然某个类实现一个接口，但是由于接口中的变量都为静态常量，不存在继承关系
	2. 相同点：
	3. 无论接口还是抽象类，都无法直接实例化，其自身实例化需要靠实现类或子类来实现
	4. 接口和抽象类都必须实现其中的所有方法

### ③、<font color="red">三大特性：封装、继承、多态</font>

#### Ⅰ、封装

1. 定义：隐藏对象的属性和实现细节，仅对外公开接口，控制在程序中属性的读和修改的访问级别
2. 目的：增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员
3. 封装的基本要求：把所有的属性私有化，对每个属性提供 `getter` 和 `setter` 方法，如果有一个带参的构造函数的话，那一定要写一个不带参的构造函数。在开发的时候经常要对已经编写的类进行测试，所以在有的时候还有重写toString方法，但这不是必须的

#### Ⅱ、继承

1. 定义：子类可以继承父类所有的属性和方法，也可以增加新的属性和方法
2. 目的：实现代码的复用
3. 介绍：
	1. 当两个类具有相同的特征（属性）和行为（方法）时，可以将相同的部分抽取出来放到一个类中作为父类，其它两个类继承这个父类。
	2. 继承后子类自动拥有了父类的属性和方法，但特别注意的是，父类的私有属性和构造方法并不能被继承。
	3. 另外子类可以写自己特有的属性和方法，目的是实现功能的扩展，子类也可以复写父类的方法即方法的重写。
	4. 子类不能继承父类中访问权限为 `private` 的成员变量和方法。
	5. 子类可以重写父类的方法，及命名与父类同名的成员变量。
	6. 有时候我们需要这样的需求：我们需要将某些事物尽可能地对这个世界隐藏，但是仍然允许子类的成员来访问它们。这个时候就需要使用到 `protected`

#### Ⅲ、多态

1. 概念：相同的事物，调用其相同的方法，参数也相同时，但表现的行为却不同
	1. Java 实现多态有三个必要条件：继承、重写、向上转型
	2. 继承：在多态中必须存在有继承关系的子类和父类
	3. 重写：子类对父类中某些方法进行重新定义，在调用这些方法时就会调用子类的方法
	4. 向上转型：在多态中需要将子类的引用赋给父类对象，只有这样该引用才能够具备技能调用父类的方法和子类的方法
	5. 只有满足了上述三个条件，我们才能够在同一个继承结构中使用统一的逻辑实现代码处理不同的对象，从而达到执行不同的行为
2. 多态的实现方式：
	1. 基于继承实现的多态：基于继承的实现机制主要表现在父类和继承该父类的一个或多个子类对某些方法的重写，多个子类对同一方法的重写可以表现出不同的行为
	2. 基于接口实现的多态：继承是通过重写父类的同一方法的几个不同子类来体现的，那么就可就是通过实现接口并覆盖接口中同一方法的几不同的类体现的。在接口的多态中，指向接口的引用必须是指定这实现了该接口的一个类的实例程序，在运行时，根据对象引用的实际类型来执行对应的方法。继承都是单继承，只能为一组相关的类提供一致的服务接口。但是接口可以是多继承多实现，它能够利用一组相关或者不相关的接口进行组合与扩充，能够对外提供一致的服务接口。所以它相对于继承来说有更好的灵活性
3. 多态性主要表现在如下两个方面：
	1. 方法重载：通常指在同一个类中，相同的方法名对应着不同的方法实现，但是方法的参数不同
	2. 成员覆盖：通常指在不同类(父类和子类)中，允许有相同的变量名，但是数据类型不同；也允许有相同的方法名，但是对应的方法实现不同
4. 多态的好处：程序的可扩展性及可维护性增强

### ④、类成员访问修饰符与访问能力之间的关系

![|675](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、类成员访问修饰符与访问能力之间的关系.png)

### ⑤、总结

1. 从认识论角度考虑是先有对象后有类。对象是具体的事物；类是抽象的，是对对象的抽象
2. 从代码运行角度考虑是先有类后有对象，类是对象的模板

## 2、方法回顾和加深

### ①、方法的定义

1. 返回类型：`break` 和 `return` 的区别：break 跳出 switch，结束循环；return：结束方法并传递参数（有返回值的方法）
2. 方法名：见名知意，首字母小写+驼峰命名法

```java
// 返回类型为 String，返回值为："Hello"
public String sayHello(){
	return "Hello";
}
```
    
3. 参数列表

```java
// 参数列表为：int a,int b
public String plus(int a,int b){
	return "Hello";
}
```
    
4. 异常抛出

```java
//在方法上声明异常：throws Exception
public void readFile(String file) throws Exception {

}
```

### ②、方法的调用

1. 静态方法：加 `static`，可直接通过 `类名.方法名` 调用
2. 非静态方法：不加 `static`，要实例化类(new)之后才可通过 `类名.方法名` 调用

```java
//静态方法
public static String sayHello(){
	return "Hello";
}

//非静态方法
public String say2Hello(){
	return "Hello";
}
```

3. 形参和实参

```java
public class Demo01 {

	public static void main(String[] args) {
		//调用Demo01类中的add方法传入参数并把结果赋值给sum
		//(1,2)中1与2为实参
		int sum = Demo01.add(1,2);
		//打印sum
		System.out.println(sum);
	}

	//定义了一个add方法
	//(int a,int b)中a与b为形参
	public static int add(int a,int b){
		return a+b;
	}

}
```

### ③、值传递和引用传递

1. 值传递：

```java
// 值传递
public class Demo02 {
	public static void main(String[] args) {
		// 定义了一个int类型的属性a，并赋值1
		int a = 1;
		// 打印a
		// 结果是1，因为初始化就是1
		System.out.println(a);
	
		// 调用change方法，并传入参数a
		Demo02.change(a);
		// 打印调用change方法后的a
		// 结果还是1，因为虽然调用了change方法，a也变为了10，但是并没有返回a=10
		System.out.println(a);
		
	}
	// 定义了一个没有返回值的change方法，将10赋值给传入的参数
	public static void change(int a){
		a = 10;
	}

}

```

```shell
1
1

Process finished with exit code 0
```

2. 引用传递：

```java
// 引用传递，对象，本质本质还是值传递
public class Demo03 {
  public static void main(String[] args) {
	  //创建对象person
	  Person person = new Person();
	  //打印person对象中的name属性，因未赋值所以是null
	  System.out.println(person.name);

	  //调用change方法，并传入对象person
	  Demo03.change(person);
	  //打印调用change方法后的，person对象中的name属性
	  //虽然与上面相似，但是却打印出来了：月海
	  //调用change方法修改Person类中的name属性，故可以打印出person.name="月海"
	  System.out.println(person.name);
  }

  //定义个一个没有返回值的change方法，传入参数为Person类
  public static void change(Person person){
	  //将字符串"月海"赋值给person类中的属性name
	  //此处指向的是Person类，修改的是Person类中的name属性的值
	  person.name = "月海";
  }

}

//新创建了一个类，和Demo03等相同
class Person{
  //定义String类型的属性name，未赋值，所以现在是null
  String name;
}

```

```shell
null
月海

Process finished with exit code 0
```

## 3、类与对象的创建和分析

### ①、类与对象的关系

1. 类是一种抽象的数据类型，他是对某一种事物整体的描述/定义，但是并不能代表某一个具体的事物
	1. 动物、植物、手机、电脑
	2. Person类、Pet类、Car类等，这些都是用来描述/定义某一类具体事物应该具备的特点和行为
2. 对象是抽象概念的具体实例
	1. 张三就是人的一个人的具体实例，张三家里的旺财就是狗的一个具体实例
	2. 能够体现出特点，展现出功能的是具体的实例，而不是一个抽象的概念
3. 需先定义类(class)，然后通过类来创建(new)对象

### ②、创建与初始化对象

1. 使用 `new` 关键字创建对象
2. 使用 `new` 关键字创建的时候，除了分配内存空间之外，还会给创建好的对象进行默认的初始化以及对类中构造器的调用
3. 类中的构造器也称之为构造方法，是在进行创建对象的时候必须要调用的，并且构造器有以下两个特点：
	1. 必须和类的名字相同
	2. 必须没有返回类型，也不能写 `void`
4. <font color="red">构造器必须要掌握</font>
5. 类与对象的创建与使用：

```java
// 定义一个学生类，类中只会有属性和方法
public class StudentTest {

  //类中的属性应该是空的，不应该被写死，因为是抽象类，被实例化之前不该有具体的代指
  //定义一个属性：字段，名字
  String name;
  //年龄
  int age;

  //定义一个方法
  public void study(){
	  //this：指当前这个类
	  System.out.println(this.name+"在学习");
  }

}
```

```java
// 一个项目应该只存在一个 main 方法
public class Application {

  public static void main(String[] args) {

	  // 类是抽象的，需要实例化，实例化后会返回一个自己的对象
	  // Student()：类，student：对象（对象名可以随便写，不同的对象名指向不同的对象）
	  Student student = new Student();

	  //创建对象：xiaoming
	  Student xiaoming = new Student();
	  //创建对象：xiaohong
	  Student xiaohong = new Student();

	  //给对象xiaoming的属性赋值
	  xiaoming.name = "小明";
	  xiaoming.age = 20;

	  //给对象xiaohong的属性赋值
	  xiaohong.name = "小红";
	  xiaohong.age = 18;

	  //打印对象xiaoming的属性
	  System.out.println(xiaoming.name);
	  System.out.println(xiaoming.age);

	  //打印对象xiaohong的属性
	  System.out.println(xiaohong.name);
	  System.out.println(xiaohong.age);

	  //调用对象xiaoming中的方法study()
	  //因前面已给xiaoming.name赋值，故可以打印出名字
	  xiaoming.study();

  }

}
```

```shell
小明
20
小红
18
小明在学习

Process finished with exit code 0
```

6. 使用默认无参构造器：

```java
//定义人类
public class Person {

  //定义属性
  String name;

  // 一个类即使什么都不写，他也会存在一个方法（构造器），默认构造器
  // 显示的自己定义的无参构造器：
  public Person(){
	  //核心作用1：使用new关键字实例化对象，本质是在调用构造器

	  //核心作用2：实例化初始值，对象创建后被调用的值为此处初始化的值（不为null）
	  //this：指当前这个类；this.name：指当前这个类中的name属性
	  this.name = "月海";
  }

}
```

```java
public class PersonTest {

public static void main(String[] args) {
	// 实例化对象
	Person person = new Person();

	// 实例化对象后不赋值直接打印person.name，不为null而是构造器中初始化的值
	System.out.println(person.name);
}
}
```

```shell
月海

Process finished with exit code 0
```

7. 自定义构造器，当自定义构造器时，一定要显式指定无参构造器

```java
//定义人类
public class Person {

  //定义属性
  String name;

  //一个类即使什么都不写，他也会存在一个方法（构造器），默认构造器
  //显示的自己定义的无参构造器：
  public Person(){
	  //核心作用1：使用new关键字实例化对象，本质是在调用构造器

	  //核心作用2：实例化初始值，对象创建后被调用的值为此处初始化的值（不为null）
	  //this：指当前这个类；this.name：指当前这个类中的name属性
	  //this.name = "月海";
  }

  //有参构造器：一旦定义了有参构造器，无参构造器就必须也定义出来，并且最好不写参数，重载构造器
  //传入的参数为String类型
  public Person(String name){
	  //将传入的参数赋值给当前这个类的name属性
	  this.name = name;
  }

}
```

```java
public class PersonTest {
	public static void main(String[] args) {
		//实例化对象，使用有参构造器传入参数
		Person person = new Person("月海2");
	
		//实例化对象后不赋值直接打印person.name，不为null而是有参构造器中传入的值
		System.out.println(person.name);
	}
}
```

```shell
月海2

Process finished with exit code 0
```

### ③、创建对象的内存分析

```java
public class Pet {
	public String name;
	public int age;
	
	public void shout(){
		System.out.println("叫了一声");
	}
}
```

```java
public class Application {
	public static void main(String[] args) {
		Pet dog = new Pet();
	
		dog.name = "旺财";
		dog.age = 3;
		dog.shout();
	
		System.out.println(dog.name);
		System.out.println(dog.age);
	
		Pet cat = new Pet();
	}
}
```

```shell
叫了一声
旺财
3

Process finished with exit code 0
```

1. 在堆中的方法区里，加载类 `Application`，主函数 `main()`，常量池：旺财，同时加载静态方法区
2. 在栈中执行 `main` 方法，加载 `Pet` 类、创建 `dog` 方法，加载属性：`name`、`age`，加载方法：`shout()`
3. `main` 方法创建了 `dog` 引用变量名，其中保存了指向堆中的 `Pet` 对象的地址
4. 堆中的 `Pet` 对象调用堆中方法区中的 `Pet` 方法，此时 `Pet` 方法数值为初始化还没被赋值
5. 将方法区中 `Application` 的 `dog` 属性赋值给堆中的 `Pet` 对象
6. 在栈中执行 `main` 方法，加载 `Pet` 类、创建 `cat` 方法，加载属性：`name`、`age`，加载方法：`shout()`
7. `main` 方法创建了 `cat` 引用变量名，其中保存了指向堆中的 `Pet` 对象的地址（与之前 `dog` 指向的不同）
8. 堆中的 `Pet` 对象调用堆中方法区中的 `Pet` 方法，此时 `Pet` 方法数值为初始化还没被赋值
9. 将方法区中 `Application` 的 `cat` 属性赋值给堆中的 `Pet` 对象

![|675](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、创建对象的内存分析.png)

## 4、面向对象的三大特性

### ①、封装

1. 该露的露，该藏的藏
	1. 我们程序设计要追求“高内聚，低耦合”
	2. 高内聚：类的内部数据操作细节自己完成，不允许外部干涉
	3. 低耦合：仅暴露少量的方法给外部使用
2. 数据的隐藏：通常，应禁止直接访问一个对象数据的实际表示，而应通过操作接口来访问，这称之为信息隐藏
3. <font color="red">属性私有（private），get/set</font>，作用：
	1. 提高程序的安全性，保护数据
	2. 隐藏代码的实现细节
	3. 统一接口
	4. 增加系统的可维护性

```java
public class Student {

	//属性私有
	private String name;
	private int id;
	private char sex;
	
	//提供一些可以操作这个属性的方法
	//提供一些public的get、set方法
	
	//get 可以获得这个数据，可加入逻辑判断
	public String getName() {
		return name;
	}
	//set 可以给这个数据设置值
	public void setName(String name) {
		this.name = name;
	}
}
```

```java
public class Application {
	public static void main(String[] args) {
		//创建对象
		Student s1 = new Student();
	
		//使用set方法给被封装的属性设置值
		s1.setName("月海");
		//使用get方法获取被封装的属性的值
		System.out.println(s1.getName());
	
	}
}
```

### ②、继承

1. 继承的本质是对某一批类的抽象，从而实现堆像是世界更好的建模
2. `extands` 的意思是“扩展”。子类是父类的扩展
3. JAVA 中类只有单继承，没有多继承（子类只能继承一个父类）
4. 继承是类和类之间的一种关系。除此之外，类和类之间的关系还有依赖、组合、聚合等
5. 继承关系的两个类，一个为子类（派生类），一个为父类（基类）。子类继承父类，使用关键字 `extands` 来表示
6. 子类和父类之间，从意义上讲应该具有 “is a” 的关系

```java
// 父类
public class Person {
	private int money = 10_0000_0000;
	
	public void say(){
		System.out.println("说了一句话");
	}
	
	public int getMoney() {
		return money;
	}
	
	public void setMoney(int money) {
		this.money = money;
	}
}
```

```java
// 子类
public class Student extends Person {

}
```

```java
// 实现类
public class Application {
	public static void main(String[] args) {
		//创建对象
		Student s1 = new Student();
	
		s1.say();
		System.out.println(s1.getMoney());
	
	
	}
}
```

7. `object` 类：所有类的父类
8. `super`：代表父类，与 `this` 相似
	1. 调用父类的构造方法，必须在构造方法的第一个
	2. 必须只能出现在子类的方法或者构造方法中
	3. `super` 和 `this` 不能同时调用构造方法！
9. `super` 和 `this` 的区别
	1. 代表的对象不同：
		1. `this`：本身调用者的这个对象
		2. `super`：代表父类对象的应用
	2. 前提：
		1. `this`：没有继承也可以使用
		2. `super`：只能在继承条件下才可以使用
	3. 构造方法：
		1. `this()`：本类的构造
		2. `super()`：父类的构造

```java
//父类
public class Person {
  protected String name = "父类属性";

  //----------------------------------------------

  public void print(){
	  System.out.println("父类方法");
  }

  //----------------------------------------------

  public Person(){
	  System.out.println("父类无参构造器");
  }
}
```

```java
//子类
public class Student extends Person {
	private String name = "子类属性";
	
	public void test(String name){
		//此方法传递进来的name
		System.out.println(name);
		//这个类定义的name
		System.out.println(this.name);
		//父类定义的name
		System.out.println(super.name);
	}
	
	public void print(){
		System.out.println("子类方法");
	}
	
	public void test1(){
		//子类的print()方法
		print();
		//子类的print()方法
		this.print();
		//父类的print()方法
		super.print();
	}
	
	public Student(){
		//有隐藏代码，默认调用了父类的无参构造：super();
		super();//调用父类的构造器，必须要在子类构造器的第一行
		System.out.println("子类无参构造器");
	}
}
```

```java
// 实现类
public class Application {
	public static void main(String[] args) {
		//创建对象
		Student s1 = new Student();
	
		s1.test("输入属性");
	
		System.out.println("----------------");
	
		s1.test1();
	}
}
```

```shell
父类无参构造器
子类无参构造器
输入属性
子类属性
父类属性
----------------
子类方法
子类方法
父类方法

Process finished with exit code 0
```

10. 方法重写：需要有继承关系，子类重写父类的方法。重写是方法的重写，与属性无关
    1. 方法名必须相同
    2. 参数列表必须相同
    3. 方法体必须不同
    4. 修饰符：范围可以扩大，但不能缩小：public（大） > Protected > Default > Private
    5. 抛出的异常可以缩小，但不能扩大：Exception（大） > ClassNotFoundException
11. 为什么需要重写：父类的功能子类不一定需要，或者不一定满足
  
```java
// 父类
public class A {
	public void test(){
		System.out.println("父类A");
	}
}
```

```java
// 子类
public class B extends A{
	//方法的重写
	//子类方法中，方法名、参数列表相同，方法体不同
	public void test(){
		System.out.println("子类B");
	}
}
```

### ③、多态

1. 可以实现动态编译，增强可扩展性
2. 同一个方法可以根据发送对象的不同而采用多种不同的行为方式
3. 一个对象的实际类型是确定的，但可以指向对象的引用的类型很多
4. 多态的存在条件：
	1. 有继承关系
	2. 子类重写父类方法
	3. 父类引用指向子类对象
5. 多态的注意事项：多态是方法的多态，属性没有多态
   
```java
//父类
public class Person {
	public void test(){
		System.out.println("父类方法");
	}
}
```

```java
// 子类
public class Student extends Person {
	public void test(){
		System.out.println("子类方法");
	}
	public void test1(){
		System.out.println("子类方法1");
	}
}
```

```java
// 实现类
public class Application {
	public static void main(String[] args) {
	
		//多态：可以指向的引用类型就不确定了，父类的引用指向子类
	
		//Student，子类型，能调用的方法都是自己的或者继承父类的
		Student s1 = new Student();
		//Person，父类型，可以指向子类，但是不能调用子类独有的方法
		Person s2 = new Student();
		//Object，所有类的父类
		Object s3 = new Student();
	
		s1.test();
		s2.test();
	
		//此处是父类调用子类独有的方法
		//需强制类型转换，将Person（父类）转换为Student（子类）
		((Student) s2).test1();
	}
}
```

6. 类型转换：（目标类型）需要转换的对象，方便方法的调用，减少重复的代码；存在条件：
	1. 父类的引用指向子类的对象
	2. 向上转型：把子类转换为父类，可自动转型，可能会丢失自己的一些方法
	3. 向下转型：把父类转换为子类，需强制转换

### ④、`static` 关键字详解

1. 静态变量：加载时与类一同加载

  ```java
public class Student {
	private static int age; //静态变量
	private double score;   //非静态变量
	
	public static void main(String[] args) {
	
		Student.age = 1;    //静态变量可以直接使用类名调用，当然是能在同一个类中
		
		Student s1 = new Student();
		s1.score = 1;       //非静态变量只能通过对象调用
	}
}
  ```
  
2. 静态方法

```java
public class Student {
	// 第二个执行
	// 匿名代码块：也是一个方法，但是没有名字
	{
		System.out.println("匿名代码块");
	}
	
	// 第一个执行
	// 静态方法：与类一同加载，只执行一次
	// 可以用来赋初始值等
	static {
		System.out.println("静态代码块");
	}
	
	// 第三个执行
	// 构造方法
	Student(){
		System.out.println("构造方法");
	}
	
	public static void main(String[] args) {
	Student s1 = new Student();
	System.out.println("----分割线-----------------");
	Student s2 = new Student();
	}
}
```
  
```shell
静态代码块
匿名代码块
构造方法
----分割线-----------------
匿名代码块
构造方法

Process finished with exit code 0
```

3. final关键字：被此关键字修饰的类不能被继承

```java
public final class Student {

}
```

## 5、抽象类和接口

### ①、抽象类

1. `abstract` 修饰符可以用来修饰方法也可以用来修饰类，如果修饰方法，那么该方法就是抽象方法。如果修饰类，那么该类就是抽象类
2. 抽象类中可以没有抽象方法，但是有抽象方法的类一定要声明为抽象类
3. 抽象类：不能使用 `new` 关键字来创建对象，他是用来让子类继承的，是一个约束
4. 抽象方法：只有方法的声明，没有方法的实现，他是用来让子类实现的，也是一个约束
5. 抽象方法必须在抽象类中，但是抽象类中可以写普通的方法
6. 子类继承抽象类，那么必须要实现抽象类没有实现的方法，否则该子类也会声明为抽象类

```java
// abstract：抽象类
// extends：继承，但是只能单继承，接口可以多继承
public abstract class Person {
	// abstract：抽象方法，只有方法的名字，没有方法的实现
	// 只是一种约束，有人帮我们实现
	public abstract void run();
}
```

```java
//实现类
public class YueHai extends Person {
	public void run() {
	
	}
}
```

### ②、接口

1. 普通类：只有具体的实现
2. 抽象类：具体实现和规范（抽象方法）都有
3. 接口：只有规范！自己无法写方法，是专业的约束，约束和实现分离
4. 接口就是规范，定义的是一组规则，体现了现实世界中，“如果你是。。。则必须你能。。。”的思想，比如：如果你是天使，则你必须能飞。如果你是汽车，则你必须能跑。
5. <font color="red">接口的本质是契约</font>，就像我们人间的法律一样，指定好之后大家都遵守
6. java 的精髓，是对对象的抽象，最能体现这一点的就是接口。为什么我们讨论设计模式都只针对具备了抽象能力的语言（比如 c++、java、c# 等），就是因为设计模式所研究的，实际上就是如何合理的去抽象
7. 接口中的所有定义其实都是抽象的，默认：`pubilc abstract`
8. 声明类的关键字是 `class`，声明接口的关键字是 `interface`
9. 接口可以多继承

```java
// 接口1
// 接口，接口中的所有定义都是抽象的
public interface UserService {
	// 在接口中定义的属性都是静态的常量
	// 同：public static final int age = 99;
	// 一般不会定义属性
	int age = 99;
	
	//增
	void add();
	//删
	void delete();
	//改
	void update();
	//查
	void query();
}
```

```java
// 接口2
public interface TimeService {
	// 计时
	void time();
}
```

```java
// 实现类
// 类可以实现接口，实现了接口中的类，就需要重写接口中的方法
// 利用接口可以实现多继承
public class UserServiceImpl implements UserService,TimeService {
	@Override
	public void add() {
	
	}
	
	@Override
	public void delete() {
	
	}
	
	@Override
	public void update() {
	
	}
	
	@Override
	public void query() {
	
	}
	
	@Override
	public void time() {
	
	}
}
```

10. 接口的作用：
	1. 约束
	2. 定义一些方法，让不同的人实现
	3. 默认方法：pubilc abstract
	4. 默认常量：public static final
	5. 接口不能被实例化，接口中没有接口没有构造方法
	6. 通过implements可以实现多个接口
	7. 必须要重写接口中的方法

## 6、内部类

1. 内部类就是在一个类的内部定义一个类；比如，在 A 类中定义一个 B 类，那么 B 类相对 A 类来说就称为内部类，而 A 类相对 B 类来说就是外部类了。
2. 成员内部类：成员内部类是定义在另一个类中的非静态类。它可以直接访问外部类的所有成员（属性和方法），并且可以通过外部类的实例进行实例化。

```java
// 外部类
public class A {
	// 外部类的属性
	private int id;
	// 外部类的方法
	public void out(){
		System.out.println("这是外部类的方法");
	}
	
	// 内部类
	public class Inner{
		// 内部类的方法
		public void in(){
		System.out.println("这是内部类的方法");
	}
	// 获得外部类的私有属性
	public void getID(){
		System.out.println(id);
	}
	// 获得外部类的方法
	public void getOut(){
		A a = new A();
		a.out();
	}
	
	}
}
```

```java
// 实现类
public class Application {
	public static void main(String[] args) {
	// 实例化A类
	A a = new A();
	// 通过实例化的A类来实例化A类的内部类Inner
	A.Inner inner = a.new Inner();
	
	// 外部类的方法
	a.out();
	// 内部类的方法
	inner.in();
	
	// 通过内部类获得外部类的私有属性
	inner.getID();
	// 通过内部类获得外部类的方法
	inner.getOut();
	}
}
```

```shell
这是外部类的方法
这是内部类的方法
0
这是外部类的方法

Process finished with exit code 0
```

3. 静态内部类：静态内部类是使用 static 关键字修饰的内部类。静态内部类不能直接访问外部类的非静态成员（属性和方法），只能访问静态成员。它可以通过外部类的类名直接实例化，而不需要外部类的实例。

```java
// 外部类
public class A {
	// 外部类的属性
	private int id;
	
	// 静态内部类：static
	// 因为是静态类，所以在最开始加载，所以不能获取id等在其之后加载的属性及方法等
	public static class Inner{
		// 获得外部类的私有属性
		public void getID(){
			System.out.println(id);
		}
	}
}
```

```java
// 实现类
public class Application {
    public static void main(String[] args) {
        // 通过外部类的类名直接实例化静态内部类
        A.Inner inner = new A.Inner();

        // 调用静态内部类的方法
        inner.getID();
    }
}
```

```shell
20
```

4. 局部内部类：局部内部类是定义在方法内部的类。它的作用域仅限于该方法内部，不推荐广泛使用。局部内部类可以访问外部类的成员，以及方法的 final 变量。

```java
// 外部类
public class B {
	// 外部类的方法
	public void method(){
		// 局部内部类，写在外部类的方法中
		// 不推荐
		class Inner{
		
		}
	}
}
```

```java
// 实现类
public class Application {
    public static void main(String[] args) {
        // 实例化外部类
        B b = new B();

        // 调用外部类的方法，其中包含局部内部类的定义和使用
        b.method();
    }
}
```

```shell
这是局部内部类的方法
```

5. 匿名内部类：匿名内部类是没有名字的类，通常用于创建一次性对象。匿名内部类常用于接口的实现或抽象类的实例化。

```java
// 接口
interface Greeting {
    void sayHello();
}

// 实现类
public class Application {
    public static void main(String[] args) {
        // 匿名内部类，实现接口
        Greeting greeting = new Greeting() {
            @Override
            public void sayHello() {
                System.out.println("Hello, this is an anonymous inner class!");
            }
        };

        // 调用匿名内部类的方法
        greeting.sayHello();
    }
}
```

```shell
Hello, this is an anonymous inner class!
```

## 7、异常机制

### ①、什么是异常

1. 实际工作中，遇到的情况不可能是非常完美的。
2. 比如：你写的某个模块，用户输入不一定符合你的要求、你的程序要打开某个文件，这个文件可能不存在或者文件格式不对，你要读取数据库的数据，数据可能是空的等，我们的程序在跑着，内存或硬盘可能满了，等等
3. 软件程序在运行过程中，非常可能遇到刚刚提到的这些异常问题，我们叫异常，英文是：Exception，意思是例外。这些例外情况，或者叫异常，怎么让我们写的程序做出合理的处理，而不至于程序崩溃。
4. 异常指程序运行中出现的不期而至的各种状况，如：文件找不到、网络链接失败、非法参数等。
5. 异常发生在程序运行期间，它影响的正常的程序执行流程

### ②、异常的简单分类

1. 检查性异常：最具代表的检查性异常是用户错误或问题引起的异常，这是程序员无法预见的；例如：要打开一个不存在的文件时，一个异常就发生了，这些异常在编译时不能被简单的忽略
2. 运行时异常：运行时异常时可能被程序员避免的异常。与检查性异常相反，运行时异常可以在编译时被忽略
3. 错误 ERROR：错误不是异常，而是脱离程序员控制的问题。错误在代码中通常被忽略；例如：当栈溢出时，一个错误就发生了，他们在编译时也检查不到的

### ③、异常体系结构

1. Java 把异常当作对象来处理，并定义一个基类 `java.lang.Throwable` 作为所有异常的超类
2. 在 Java API 中已经定义了许多异常类，这些异常分为两大类，错误 `Error` 和异常 `Exception`
   
![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、异常体系结构.png)

### ④、Error 异常

1. Error 类对象由 Java 虚拟机生成并抛出，大多数错误与代码编写者所执行的操作无关
2. Java 虚拟机运行错误（Virtual MachineError），当 JVM 不再有继续执行操作所需的内存资源时，将出现 OutOfMemoryError。这些异常发生时， Java 虚拟机（JVM）一般会选择线程终止
3. 还有发生在虚拟机试图执行应用时，如类定义错误（NoClassDefFoundError）、链接错误（LinKageError）。这些错误是不可查的，因为他们在应用程序的控制和处理能力之外，而且绝大多数是程序运行时不允许出现的状况

### ⑤、Exception

1. 在 Exception 分支中有一个重要的子类：`RuntimeException`（运行时异常）
	1. `ArraylndexOutOfBoundsException`（数组下标越界）
	2. `NullPointerException`（空指针异常）
	3. `ArithmeticException`（算术异常）
	4. `MissingResourceException`（丢失资源）
	5. `ClassNotFoundException`（找不到类）等异常，这些异常是不检查异常，程序中可以选择捕获处理，也可以不处理
2. 这些异常一般是由程序逻辑错误引起的，程序应该从逻辑角度尽可能避免这类异常的发生
3. `Error` 和 `Exception` 的区别：
	1. `Error` 通常是灾难性的致命的错误，是程序无法控制和处理的，当出现这些异常时，Java 虚拟机（JVN）一般会选择终止线程；
	2. `Exception` 通常情况下是可以被程序处理的，并且在程序中应该尽可能的去处理这些异常

### ⑥、Java 异常处理机制

1. 捕获异常

```java
int a = 1;
int b = 0;

// 异常的捕获，异常被捕获之后程序不会停止运行
// 快捷键：Ctrl + Shift + T
try {                                   //try：监控区域
	System.out.println(a/b);
}catch (Error e){                   //catch：捕获Error异常，可以写多个，
	System.out.println("程序出现错误");
}catch (Exception e){               //catch：捕获Exception异常
	e.printStackTrace();            //打印错误信息
	System.out.println("程序出现异常");
}finally {                          //finally：处理善后工作，可以不要
	System.out.println("finally");
}
```
  
2. 抛出异常

  ```java
public class Test {
	public static void main(String[] args) {
		new Test().test(1,0);
	}
	
	// 假设这个方法中处理不了这个异常，方法上抛出异常
	// throws：抛出异常
	public void test(int a,int b) throws ArithmeticException{
		if (b==0){
		// 本来应该不报错，现在这里主动抛了一个异常
		// throw：主动抛出异常，一般在方法中使用
		throw new ArithmeticException();
		}
	}
}
  ```

### ⑦、自定义异常

1. 使用 Java 内置的异常类可以描述在编程时出现的大部分异常情况。除此之外，用户还可以自定义异常，用户自定义异常，只需继承 `Exception` 类即可。
   1. 在程序中使用自定义异常类，大体可分为以下几个步骤：
	   1. 创建自定义异常类
	   2. 在方法中通过 `throw` 关键字抛出异常对象
	   3. 如果在当前抛出异常的方法中处理异常，可以使用 `try-catch` 语句捕获并处理；否则在方法的声明处通过 `throws` 关键字指明要抛出给方法调用者的异常，继续进行下一步操作
	   4. 在出现异常方法的调用者中捕获并处理异常

```java
// 自定义的异常类
public class MyException extends Exception {
	private int detail;
	
	public MyException(int a){
	this.detail = a;
}

// toString：异常的打印信息
@Override
public String toString() {
	return "MyException{" + "detail=" + "自定义异常" + '}';
	}
}
```

```java
public class MyExceptionTest {
	// 可能会存在异常的方法
	public void test(int a) throws MyException {
		// a 大于10就抛出此异常
		if(a > 10){
			throw new MyException(a);
		}
		System.out.println("OK");
	}
}
```

```java
public class MyExceptionTest1 {
	// 测试方法
	public static void main(String[] args) {
		// 捕获异常
		try {
			// 调用test()方法
			new MyExceptionTest().test(11);
		} catch (MyException e) {
			// 打印错误信息
			e.printStackTrace();
			// 在错误信息后面打印信息
			System.out.println("MyException=>"+e);
		}
	}
}
```

### ⑧、总结

1. 处理运行时异常时，采用逻辑去合理规避同时辅助 `try-catch` 处理
2. 在多重 `catch` 块后面，可以加一个 `catch`（Exception）来处理可能会被遗漏的异常
3. 对于不确定的代码，也可以加上 `try-catch`，增加一些处理异常的代码块
4. 尽量去处理异常，切记只是简单的调用 `printStackTrace()` 去打印输出
5. 具体如何处理异常，要根据不同的业务和异常类型去决定
6. 尽量添加 `finally` 语句块去释放占用的资源

## 8、设计模式

> 设计模式是在大量的实践中总结和理论化之后优选的代码结构、编程风格、以及解决问题的思考方式。
> 
> 设计模免去我们自己再思考和摸索。就像是经典的棋谱，不同的棋局，我们用不同的棋谱。”套路”
> 
> 这里只简单举例单例模式

### ①、单例模式

1. 所谓类的单例设计模式，就是采取一定的方法保证在整个的软件系统中，对某个类只能存在一个对象实例，并且该类只提供一个取得其对象实例的方法。
2. 如果我们要让类在一个虚拟机中只能产生一个对象，我们首先必须将类的构造器的访问权限设置为 `private`，这样，就不能用 `new` 操作符在类的外部产生类的对象了，但在类内部仍可以产生该类的对象。
3. 因为在类的外部开始还无法得到类的对象，只能调用该类的某个静态方法以返回类内部创建的对象，静态方法只能访问类中的静态成员变量，所以，指向类内部产生的该类对象的变量也必须定义成静态的。
4. 饿汉式单例模式

```java
// 饿汉式单例模式的创建
public class MySingleton {
	// 1、私有化类的构造器
	private MySingleton(){
	
	}

	// 2、内部创建类的对象
	// 4、要求此对象也必须声明为静态的
	private static MySingleton mySingleton = new MySingleton();
	
	// 3、提供公用的静态方法，返回类的对象
	public static MySingleton getMySingleton(){
		return mySingleton;
	}
}
```

```java
// 测试类
public class Test {
	public static void main(String[] args) {
		// 单例模式无法在类的外面创建对象
		// MySingleton mySingleton = new MySingleton();
	
		// 但是可以调用创建对象的方法来创建对象
		MySingleton mySingleton = MySingleton.getMySingleton();
	}
}
```

5. 懒汉式单例模式

```java
// 懒汉式单例模式的创建
public class MySingleton02 {
	// 1、私有化类的构造器
	private MySingleton02(){
	
	}
	
	// 2、声明当前类对象，没有初始化
	// 4、要求此对象也必须声明为静态的
	private static MySingleton02 mySingleton02 = null;
	
	// 3、声明public、static的返回当前类的方法
	public static MySingleton02 getMySingleton02(){
		// 判断是否创建过对象，若是没有创建过则创建新对象
		if (mySingleton02 == null){
			mySingleton02 = new MySingleton02();
		}
		// 若是创建过对象，则返回之前创建的对象
		return mySingleton02;
	}
}
```

```java
// 测试类
public class Test {
	public static void main(String[] args) {
		// 单例模式无法在类的外面创建对象
		// MySingleton mySingleton = new MySingleton();
	
		// 但是可以调用创建对象的方法来创建对象
		MySingleton02 mySingleton02 = MySingleton02.getMySingleton02();
	}
}
```

6. 区分饿汉式和懒汉式
	1. 饿汉式：
		1. 好处：线程是安全的
		2. 坏处：一开始就创建了对象，对象加载时间过长。
	2. 懒汉式：
		1. 好处：延迟对象的创建，
		2. 坏处：线程不安全  --> 此处是不安全的，到线程时在做修改
7. 应用场景
	1. 网站的计数器，一般也是单例模式实现，否则难以同步。
	2. 应用程序的日志应用，一般都使用单例模式实现，这一般是由于共享的日志文件一直处于打开状态，因为只能有一个实例去操作，否则内容不好追加。
	3. 数据库连接池的设计一般也是采用单例模式，因为数据库连接是一种数据库资源。
	4. 项目中，读取配置文件的类，一般也只有一个对象。没有必要每次使用配置文件数据，都生成一个对象去读取。
	5. `Application` 也是单例的典型应用
	6. Windows 的 Task Manager (任务管理器)就是很典型的单例模式
	7. Windows 的 Recycle Bin (回收站)也是典型的单例应用。在整个系统运行过程中，回收站一直维护着仅有的一个实例。

# 七、多线程

## 1、基本概念：程序、进程、线程

1. 程序（program）：是为完成特定任务、用某种语言编写的一组指令的集合。即指<font color="red">一段静态的代码</font>，静态对象
2. 进程（process）：是程序的一次执行过程，或是正在运行的一个程序。是一个动态的过程：有它自身的产生、存在和消亡的过程。——生命周期
	1. 如：运行中的QQ，运行中的MP3播放器
	2. 程序是静态的，进程是动态的
	3. <font color="red">进程作为资源分配的单位</font>，系统在运行时会为每个进程分配不同的内存区域
3. 线程(thread)，进程可进一步细化为线程，是一个程序内部的一条执行路径。
	1. 若一个进程同一时间并行执行多个线程，就是支持多线程的
	2. 线程作为调度和执行的单位，每个线程拥有独立的运行栈和程序计数器(pc)，线程切换的开销小
	3. 一个进程中的多个线程共享相同的内存单元/内存地址空间它们从同一堆中分配对象，可以访问相同的变量和对象.这就使得线程间通信更简便、高效。但多个线程操作共享的系统资源可能就会带来安全的隐患
4. 单核 CPU 和多核 CPU 的理解
	1. 单核CPU，其实是一种假的多线程，因为在一个时间单元内，也只能执行一个线程的任务。例如：虽然有多车道，但是收费站只有一个工作人员在收费，只有收了费才能通过，那么 CPU 就好比收费人员。如果有某个人不想交钱，那么收费人员可以把他“挂起”（晾着他，等他想通了，准备好了钱，再去收费）。但是因为 CPU 时间单元特别短，因此感觉不出来。
	2. 如果是多核的话，才能更好的发挥多线程的效率。（现在的服务器都是多核的）
	3. 一个 Java 应用程序 java.exe，其实至少有三个线程：`main()` 主线程，`gc()` 垃圾回收线程，`异常处理线程`。当然如果发生异常，会影响主线程。
5. 并行与并发
	1. 并行：多个 CPU 同时执行多个任务。比如：多个人同时做不同的事。
	2. 并发：一个 CPU(采用时间片)同时（看似是同时）执行多个任务。比如：秒杀、多个人做同一件事。
6. 使用多线程的优点
	1. 提高应用程序的响应。对图形化界面更有意义，可增强用户体验。
	2. 提高计算机系统CPU的利用率
	3. 改善程序结构。将既长又复杂的进程分为多个线程，独立运行，利于理解和修改
7. 何时需要多线程
	1. 程序需要同时执行两个或多个任务。
	2. 程序需要实现一些需要等待的任务时，如用户输入、文件读写操作、网络操作、搜索等。
	3. 需要一些后台运行的程序时。
8. 线程的分类：Java 中的线程分为两类：一种是守护线程，一种是用户线程。
	1. 它们在几乎每个方面都是相同的，唯一的区别是判断 JVM 何时离开。
	2. 守护线程是用来服务用户线程的，通过在 `start()` 方法前调用 `thread.setDaemon(true)` 可以把一个用户线程变成一个守护线程。
	3. Java 垃圾回收就是一个典型的守护线程。
	4. 若 JVM 中都是守护线程，当前 JVM 将退出。
	5. 形象理解：兔死狗烹，鸟尽弓藏

## 2、<font color="red">线程的创建和使用</font>

### ①、简介

1. Java 语言的 JVM 允许程序运行多个线程，它通过 `java.lang.Thread` 类来体现。
2. Thread 类的特性
	1. 每个线程都是通过某个特定 Thread 对象的 `run()` 方法来完成操作的，经常把 `run()` 方法的主体称为线程体
	2. 通过该 Thread 对象的 `start()` 方法来启动这个线程，而非直接调用 `run()`
3. Thread 类
	1. `Thread()`：创建新的Thread对象
	2. `Thread(String threadname)`：创建线程并指定线程实例名
	3. `Thread(Runnable target)`：指定创建线程的目标对象，它实现了 Runnable 接口中的 run 方法
	4. `Thread(Runnable target, String name)`：创建新的 Thread 对象

### ②、API中创建线程的两种方式（JDK5之前）

#### Ⅰ、继承 Thread 类的方式

1. 创建一个继承于 Thread 类的子类
2. 重写 Thread 类的 `run()` 的子类：将此线程执行的操作声明在 `run()` 中
3. 创建 Thread 类的子类的对象
4. 通过此对象调用 `start()`
5. 注意点：
	1. 如果自己手动调用 `run()` 方法，那么就只是普通方法，没有启动多线程模式。
	2. `run()` 方法由 JVM 调用，什么时候调用，执行的过程控制都有操作系统的 CPU 调度决定。
	3. 想要启动多线程，必须调用 `start` 方法。
	4. 一个线程对象只能调用一次 `start()` 方法启动，如果重复调用了，则将抛出以上的异常 `IllegalThreadStateException` 。若想调用，只能重新调用对象。

```java
// 子线程1
// 1、创建一个继承于Thread类的子类
public class MyThread extends Thread {
	// 2、重写Thread类的run()的子类
	@Override
	public void run() {
		for (int i = 0; i < 100; i++) {
			if (i % 2 == 0){
				// Thread.currentThread().getName()：打印此线程的名称
				System.out.println(Thread.currentThread().getName() + "：" + i);
			}
		}
	}
}
```

```java
// 子线程2
public class MyThread2 extends Thread {
	@Override
	public void run() {
		for (int i = 0; i < 100; i++) {
			if ( i % 2 != 0 ){
				System.out.println(Thread.currentThread().getName() + "：" + i);
			}
		}
	}
}
```

```java
public class ThreadTest {
	public static void main(String[] args) {
		// 3、创建Thread类的子类的对象
		MyThread myThread = new MyThread();
		MyThread2 myThread2 = new MyThread2();
		
		// 4、通过此对象调用start()
		myThread.start();   // -->子线程1：MyThread
		myThread2.start();  // -->子线程2：MyThread2
		
		System.out.println("主线程");// -->主线程
	}
}
```

#### Ⅱ、实现 Runnable 接口的方式

1. 定义子类，实现 `Runnable` 接口。
2. 子类中重写 `Runnable` 接口中的 `run` 方法。
3. 通过 `Thread` 类含参构造器创建线程对象。
4. 将 `Runnable` 接口的子类对象作为实际参数传递给 `Thread` 类的构造器中。
5. 调用 `Thread` 类的 `start` 方法：开启线程，调用 `Runnable` 子类接口的 `run` 方法。

```java
// 1. 定义子类，实现Runnable接口。
public class MyRunnable  implements Runnable  {
  // 2. 子类中重写Runnable接口中的run方法。
  @Override
  public void run() {
	 for (int i = 0; i < 100; i++) {
		   if (i % 2 == 0){
			  // 此处获取线程名只能用Thread.currentThread().getName()
			  // 无法使用this.getName()
			  System.out.println(Thread.currentThread().getName() + "：" +i);
		   }
	 }
  }
}
```

```java
public class RunnableTest {
  public static void main(String[] args) {
	 // 3. 通过Thread类含参构造器创建线程对象。
	 MyRunnable myRunnable = new MyRunnable();
	 // 4. 将Runnable接口的子类对象作为实际参数传递给Thread类的构造器中。
	 Thread thread = new Thread(myRunnable);
	 // 设置对象thread的线程名为：线程1
	 thread.setName("线程1");
	 // 5. 调用Thread类的start方法：开启线程，调用Runnable子类接口的run方法。
	 thread.start();

	 // 再启动一个线程，同样是遍历100以内的偶数
	 // 创建一个新的对象来启动新的线程
	 Thread thread2 = new Thread(myRunnable);
	 thread2.setName("线程2");
	 thread2.start();

  }
}
```

### ③、Thread 类的有关方法

1. `void start()`：启动线程，并执行对象的 `run()` 方法

```java
对象名.start();
```

2. `run()`：线程在被调度时执行的操作，通常需要重写 Thread 类中的此方法，将创建的线程要执行的操作声明在此方法中

```java
public void run() {
  方法体
}
```

3. `currentThread()`：静态方法，返回执行当前代码的线程，方便进行线程名的获取与设置等

```java
Thread.currentThread();
```

4. `String getName()`：获取当前线程的名称

```java
Thread.currentThread().getName();   --> 子线程中
对象名.getName()  --> 主线程中
```

5. `void setName(String name)`：设置当前线程的名称

```java
Thread.currentThread().setName("线程名");   --> 子线程中
对象名.setName("线程名")  --> 主线程中
```

6. `static void yield()`：线程让步，释放当前 cup 的执行权
	1. 暂停当前正在执行的线程，把执行机会让给优先级相同或更高的线程
	2. 若队列中没有同优先级的线程，忽略此方法

```java
yield();
```
   
1. `join()`：当某个程序执行流中调用其他线程的 `join()` 方法时，调用线程将被阻塞，直到 `join()` 方法加入的 `join` 线程执行完为止，低优先级的线程也可以获得执行

```java
Thread.currentThread().join();   --> 子线程中
对象名.join();  --> 主线程中
```

8. `static void sleep(long millis)`：(指定时间：毫秒)，进程休眠，使其在一段时间内处于非活动状态
	1. 令当前活动线程在指定时间段内放弃对 CPU 控制，使其他线程有机会被执行，时间到后重排队
	2. 抛出 `InterruptedException` 异常

```java
sleep(1000);  -->  休眠1000毫秒，也就是1秒
```
   
1.  `stop()`: 强制线程生命期结束，不推荐使用

```java
对象名.stop();
```

10. `boolean isAlive()`：返回 boolean，判断线程是否还活着

```java
对象名.isAlive();
```

### ④、线程的调度及优先级

1. 调度策略
	1. 时间片：将进程分为多段大小相同的时间片，依次执行
	2. 抢占式：高优先级的线程抢占 CPU
2. Java的调度方法
	1. 同优先级线程组成先进先出队列（先到先服务），使用时间片策略
	2. 对高优先级，使用优先调度的抢占式策略
3. 线程的优先级等级
	1. `MAX_PRIORITY`：10
	2. `MIN_PRIORITY`：1
	3. `NORM_PRIORITY`：5（默认）
4. 涉及的方法：
5. `getPriority()`：获取线程优先值

```java
Thread.currentThread().getPriority();   --> 子线程中
对像名.getPriority();   --> 主线程中
```

6. `setPriority(int newPriority)`：设置线程的优先级，最好在启动线程 `start()` 之前执行

```java
Thread.currentThread().setPriority(6)   --> 子线程中
对像名.setPriority(6)   --> 主线程中

Thread.currentThread().setPriority(Thread.MAX_PRIORITY);   -->  优先级设置为10
Thread.currentThread().setPriority(Thread.MIN_PRIORITY);   -->  优先级设置为1
Thread.currentThread().setPriority(Thread.NORM_PRIORITY);  -->  优先级设置为5
```

7. 说明：
   1. 线程创建时继承父线程的优先级
   2. 低优先级只是获得调度的概率低，并非一定是在高优先级线程之后才被调用

### ⑤、两种创建线程方式的比较

1. 开发中，<font color="red">建议优先选择实现 Runnable 接口的方式</font>
2. 原因 1：实现 Runnable 接口的方式的方式没有类的单继承的局限性
3. 原因 2：实现 Runnable 接口的方式更适合来处理多个线程有共享数据的情况
4. 联系：Thread 类本身也是实现了 Runnable 接口
5. 相同点：两种方式都需要重写 `run()`，将线程要执行的逻辑声明在 `run()` 中

## 3、线程的生命周期

1. JDK 中用 `Thread.State` 类定义了线程的几种状态，要想实现多线程，必须在主线程中创建新的线程对象。Java 语言使用 Thread 类及其子类的对象来表示线程，在它的一个完整的生命周期中通常要经历如下的五种状态：
2. <font color="red">新建</font>： 当一个 Thread 类或其子类的对象被声明并创建时，新生的线程对象处于新建状态
3. <font color="red">就绪</font>：处于新建状态的线程被 `start()` 后，将进入线程队列等待 CPU 时间片，此时它已具备了运行的条件，只是没分配到 CPU 资源
4. <font color="red">运行</font>：当就绪的线程被调度并获得 CPU 资源时,便进入运行状态， `run()` 方法定义了线程的操作和功能
5. <font color="red">阻塞</font>：在某种特殊情况下，被人为挂起或执行输入输出操作时，让出 CPU 并临时中止自己的执行，进入阻塞状态
6. <font color="red">死亡</font>：线程完成了它的全部工作或线程被提前强制性地中止或出现异常导致结束

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、线程的生命周期.png)

## 4、<font color="red">线程的同步</font>

### ①、问题说明

1. 问题的提出：
	1. 多个线程执行的不确定性引起执行结果的不稳定
	2. 多个线程对账本的共享，会造成操作的不完整性，会破坏数据。
2. 问题描述：假如有三个进程进来，但是只剩 1 张票，进程 1 过来判断剩余的车票大于一于是执行，执行过程中被阻塞的时候进程 2、3 也进来了，此时进程 1 还没有来得及打印车票，总票数也还没有减少，于是进程 2、3 也执行，所以左后会有 0 票以及 -1 票的出现
3. 问题原因：当多条语句在操作同一个线程共享数据时，一个线程对多条语句只执行了一部分，还没有执行完，另一个线程参与进来执行。导致共享数据的错误。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、线程的同步.png)

4. 解决：对多条操作共享数据的语句，只能让一个线程都执行完，在执行过程中，其他线程不可以参与执行。

### ②、通过同步机制，来解决线程的安全问题，<font color="red">synchronized</font>

#### Ⅰ、方式一：同步代码块

```java
synchronized(同步监视器){
	// 需要同步的代码，不能包多了也不能包少了
}
```

1. 操作共享数据的代码，即为需要同步的代码
2. 共享数据：多个线程共同操作的变量，比如：车票就是共享数据
3. 同步监视器，俗称：锁。任何一个类的对象都可以充当锁，但是多个线程必须要公用同一把锁
4. <font color="red">注意：若是使用继承 Thread 类的方法处理数据共享问题，synchronized 方法的加锁对象要设置成静态的，如此才可以保证对象是唯一的，如：</font>

```java
private static Object object = new Object();
```

5. <font color="red">但是，可以下成下面的样子，代表这个类，因为 Java 中的类也是对象，而且也只加载一次，当然实现 Runnable 接口的线程也可以这样写，而且推荐这样写</font>

```java
类名.class
// 本质来说，这个类相当于这样：
Class class = 类名.class
```

6. 实现 Runnable 接口的方式例子：

```java
// 方式一：同步代码块
// 子线程
public class MyThread implements Runnable {
  // 车票
  private int ticket = 100;
  // 为了锁创建的对象
  // 因为多个线程必须要公用同一把锁，所以此对象不能在run()方法里创建
  // 但是，为了方便，在实现Runnable接口的线程中，synchronized的同步监视器（锁）可以使用this
  // 也就是不必创建此对象，但是继承Thread的线程则要慎用这种方法，要看这个对象是不是唯一的
  Object object = new Object();

  @Override
  public void run() {
	 // 循环体
	 while (true){
		   // 同步锁，也可以写：synchronized (this)
		   synchronized (object){

			  if (ticket > 0){
				 try {
					   // 线程休眠100毫秒
					   Thread.sleep(100);
				 } catch (InterruptedException e) {
					   e.printStackTrace();
				 }

				 System.out.println(Thread.currentThread().getName() + "卖票：票号为：" + ticket);
				 // 每循环一次车票数减一
				 ticket--;
			  // 车票数小于1时跳出循环
			  }else{
				 break;
			  }
		   }
	 }
  }
}
```

```java
// 主线程
public class ThreadTest {
  public static void main(String[] args) {
	 // 通过Thread类含参构造器创建线程对象。
	 MyThread myThread = new MyThread();

	 // 将Runnable接口的子类对象作为实际参数传递给Thread类的构造器中。
	 Thread t1 = new Thread(myThread);
	 Thread t2 = new Thread(myThread);
	 Thread t3 = new Thread(myThread);

	 // 设置线程名
	 t1.setName("线程一：");
	 t2.setName("线程二：");
	 t3.setName("线程三：");

	 // 调用start方法：开启线程
	 t1.start();
	 t2.start();
	 t3.start();
  }
}
```

#### Ⅱ、方式二：同步方法

1. 如果操作共享数据的代码完整的声明在一个方法中，我们不妨将此方声明为同步的，表示整个方法为同步方法。

```java
public synchronized void show (String name){
	...
}
```

2. 同步方法仍然涉及到同步监视器，只是不需要我们显式的声明。
3. 非静态的同步方法，同步监视器是：`this`
4. 静态的同步方法，同步监视器是：当前类本身：`类名.class`
5. <font color="red">注意：若是使用继承 Thread 类的方法处理数据共享问题，synchronized 方法的加锁对象要设置成静态的，如此才可以保证对象是唯一的，同时方法里面的方法也要是静态的，如：</font>

```java
private static synchronized void show(){
	// Thread.currentThread()
	System.out.println(Thread.currentThread().getName() + "卖票：票号为：" + ticket);
}
```

4. 实现 Runnable 接口的方式例子：

```java
// 子线程
public class MyThread implements Runnable {

  // 定义总票数
  private int ticket = 100;

  // 重写的run()方法
  @Override
  public void run() {
	 // 循环调用show()同步方法
	 while (true){
		   show();
	 }
  }

  // 同步方法，此时同步监视器是：MyThread.class
  private synchronized void show(){
	 if (ticket > 0){
		   try {
			  // 线程休眠100毫秒
			  Thread.sleep(100);
		   } catch (InterruptedException e) {
			  e.printStackTrace();
		   }

		   System.out.println(Thread.currentThread().getName() + "卖票：票号为：" + ticket);
		   // 每循环一次车票数减一
		   ticket--;
		   // 车票数小于1时跳出循环
	 }
  }
}
```

```java
// 主线程
public class Test {
  public static void main(String[] args) {
	 // 通过Thread类含参构造器创建线程对象。
	 MyThread myThread = new MyThread();

	 // 将Runnable接口的子类对象作为实际参数传递给Thread类的构造器中。
	 Thread t1 = new Thread(myThread);
	 Thread t2 = new Thread(myThread);
	 Thread t3 = new Thread(myThread);

	 // 设置线程名
	 t1.setName("线程一：");
	 t2.setName("线程二：");
	 t3.setName("线程三：");

	 // 调用start方法：开启线程
	 t1.start();
	 t2.start();
	 t3.start();
  }
}
```

#### Ⅲ、同步的方式的优缺点

1. 好处：同步的方式，解决了线程的安全问题。
2. 局限性：操作同步代码时，只能有一个线程参与，其他线程等待，相当于是一个单线程的过程，效率低。
3. 同步原理分析：所有线程运行到锁前面时开始抢夺锁，谁枪到谁运行锁里的方法块，当此线程处理完锁中的代码块后释放锁，其他等待的线程才再次开始抢夺锁。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、线程的同步原理.png)

#### Ⅳ、同步的范围

1. <font color="red">如何找问题，即代码是否存在线程安全？（非常重要）</font>
	1. 明确哪些代码是多线程运行的代码
	2. 明确多个线程是否有共享数据
	3. 明确多线程运行代码中是否有多条语句操作共享数据
2. <font color="red">如何解决呢？（非常重要）</font>
	1. 对多条操作共享数据的语句，只能让一个线程都执行完，在执行过程中，其他线程不可以参与执行。
	2. 即所有操作共享数据的这些语句都要放在同步范围中
3. 切记：
	1. 范围太小：没锁住所有有安全问题的代码
	2. 范围太大：没发挥多线程的功能。

#### Ⅴ、释放锁的操作

1. 当前线程的同步方法、同步代码块执行结束。
2. 当前线程在同步代码块、同步方法中遇到 break、return 终止了该代码块、该方法的继续执行。
3. 当前线程在同步代码块、同步方法中出现了未处理的 Error 或 Exception，导致异常结束。、
4. 当前线程在同步代码块、同步方法中执行了线程对象的 `wait()` 方法，当前线程暂停，并释放锁。

#### Ⅵ、不会释放锁的操作

1. 线程执行同步代码块或同步方法时，程序调用 `Thread.sleep()`、`Thread.yield()` 方法暂停当前线程的执行
2. 线程执行同步代码块时，其他线程调用了该线程的 `suspend()` 方法将该线程挂起，该线程不会释放锁（同步监视器）。
3. 应尽量避免使用 `suspend()` 和 `resume()` 来控制线程

#### Ⅶ、懒汉式单例模式

```java
public class MySingleton {
	private MySingleton(){};
	
	private static MySingleton mySingleton = null;
	
	public static MySingleton getMySingleton(){
		// 同步线程，方式一：效率稍差
		//        synchronized (MySingleton.class) {
		//            if (mySingleton == null){
		//                mySingleton = new MySingleton();
		//            }
		//            return mySingleton;
		//        }
		// 同步线程，方式二：效率更高
		synchronized (MySingleton.class) {
			if (mySingleton == null){
				mySingleton = new MySingleton();
			}
		}
		return mySingleton;
	}
}
```

#### Ⅷ、线程的死锁问题

1. 死锁
	1. 不同的线程分别占用对方需要的同步资源不放弃，都在等待对方放弃自己需要的同步资源，就形成了线程的死锁
	2. 出现死锁后，不会出现异常，不会出现提示，只是所有的线程都处于阻塞状态，无法继续
	3. 我们使用同步时，要避免死锁的问题
2. 解决方法
	1. 专门的算法、原则
	2. 尽量减少同步资源的定义
	3. 尽量避免嵌套同步

#### Ⅸ、Lock（锁）

1. 从 JDK 5.0 开始，Java 提供了更强大的线程同步机制：通过显式定义同步锁对象来实现同步。同步锁使用 Lock 对象充当。
2. `java.util.concurrent.locks.Lock` 接口是控制多个线程对共享资源进行访问的工具。锁提供了对共享资源的独占访问，每次只能有一个线程对 `Lock` 对象加锁，线程开始访问共享资源之前应先获得 `Lock` 对象。
3. `ReentrantLock` 类实现了 `Lock` ，它拥有与 `synchronized` 相同的并发性和内存语义，在实现线程安全的控制中，比较常用的是 `ReentrantLock`，可以显式加锁、释放锁。
```java
public class MyLock implements Runnable {
  private int ticket = 100;
  // 1、实例化ReentrantLock
  private ReentrantLock lock = new ReentrantLock();

  @Override
  public void run() {
	 while (true){
		   try {
			  //2、调用锁定方法：lock()
			  lock.lock();

			  if (ticket > 0){
				 try {
					   Thread.sleep(100);
				 } catch (InterruptedException e) {
					   e.printStackTrace();
				 }

				 System.out.println(Thread.currentThread().getName() + "：售票，票号为：" + ticket);
				 ticket--;
			  }else {
				 break;
			  }
		   }finally {
			  // 3、调用解锁方法：unlock()
			  lock.unlock();
		   }
	 }
  }
}
```

```java
public class Test {
  public static void main(String[] args) {
	 MyLock myLock = new MyLock();

	 Thread t1 = new Thread(myLock);
	 Thread t2 = new Thread(myLock);
	 Thread t3 = new Thread(myLock);

	 t1.start();
	 t2.start();
	 t3.start();

  }
}
```

4. `synchronized` 与 `lock` 的异同：
	1. 相同：二者都可以解决线程安全的问题
	2. Lock 是显式锁（手动开启和关闭锁，别忘记关闭锁），synchronized 是隐式锁，出了作用域自动释放
	3. Lock 只有代码块锁，synchronized 有代码块锁和方法锁
	4. 使用 Lock 锁，JVM 将花费较少的时间来调度线程，性能更好。并且具有更好的扩展性（提供更多的子类）
5. <font color="red">优先使用顺序</font>：Lock -> 同步代码块（已经进入了方法体，分配了相应资源） -> 同步方法（在方法体之外）

## 5、线程的通信

### ①、例题：使用两个线程打印 1-100。线程 1, 线程 2 交替打印

1. `wait()`：令当前线程挂起并放弃 CPU、同步资源并等待，使别的线程可访问并修改共享资源，而当前线程排队等候其他线程调用 `notify()` 或 `notifyAll()` 方法唤醒，唤醒后等待重新获得对监视器的所有权后才能继续执行。
2. `notify()`：唤醒正在排队等待同步资源的线程中优先级最高者结束等待
3. `notifyAll()`：唤醒正在排队等待资源的所有线程结束等待.
4. 这三个方法只有在 `synchronized` 方法或 `synchronized` 代码块中才能使用，否则会报 `java.lang.IllegalMonitorStateException` 异常。
5. 因为这三个方法必须有锁对象调用，而任意对象都可以作为 `synchronized` 的同步锁，因此这三个方法只能在 Object 类中声明（定义在 Object 类中），即调用者必须是同步代码快或同步方法中的同步监视器

```java
public class Communication implements Runnable {
  // 初始化
  private int i = 1;

  @Override
  public void run() {
	 for (; i <= 100; i++) {
		synchronized (this) {
		   // 唤醒被阻塞的优先级最高的进程，同：this.notify();
		   // 上面第5点，也即：同步监视器.notify();
		   notify();

		   try {
			  Thread.sleep(10);
		   } catch (InterruptedException e) {
			  e.printStackTrace();
		   }

		   System.out.println(Thread.currentThread().getName() + "：" + i);

		   // 此处判断的作用为，循环到最后一次时，不调用wait()方法
		   // 故使得线程不会被阻塞，正常的结束程序
		   if (i < 100) {
			  try {
					// 使得调用如下wait()方法的线程进入阻塞状态
					wait();
			  } catch (InterruptedException e) {
					e.printStackTrace();
			  }
		   }
		}
	 }
  }
}
```

6. `sleep()` 和 `wait()` 的异同
	1. 相同：一旦执行方法，都可以使得当前的线程进入阻塞状态
	2. 两个方法声明的位置不同：Thread 类中声明 `sleep()`，`Object()` 类中声明 `wait()`
	3. 调用的要求不同：`sleep()` 可以在任何需要的场景下调用，`wait()` 必须使用在同步代码块或同步方法中
	4. 关于是否释放同步监视器，如果两个方法都使用在同步代码块或同步方法中，`sleep()` 不会释放锁，`wait()` 会释放锁

### ②、例题：生产者/消费者问题

1. 生产者(Productor)将产品交给店员(Clerk)，而消费者(Customer)从店员处取走产品，店员一次只能持有固定数量的产品(比如:20），如果生产者试图生产更多的产品，店员会叫生产者停一下，如果店中有空位放产品了再通知生产者继续生产；如果店中没有产品了，店员会告诉消费者等一下，如果店中有产品了再通知消费者来取走产品。
2. 这里可能出现两个问题：
	1. 生产者比消费者快时，消费者会漏掉一些数据没有取到。
	2. 消费者比生产者快时，消费者会取相同的数据。
3. 分析：
	1. 是否是多线程问题？         是，生产者线程，消费者线程
	2. 是否有共享数据？           是，店员（或产品）
	3. 如何解决线程的安全问题？   同步机制，有三种方法
	4. 是否涉及到线程的通信？     是

```java
   
```

## 6、JDK5 新增线程创建方式

### ①、一、实现 Callable 接口


1. 与使用 `Runnable` 相比， `Callable` 功能更强大些
	1. 相比 `run()` 方法，可以有返回值
	2. 方法可以抛出异常
	3. 支持泛型的返回值
	4. 需要借助 `FutureTask` 类，比如获取返回结果
2. Future接口
	1. 可以对具体 `Runnable`、`Callable` 任务的执行结果进行取消、查询是否完成、获取结果等。
	2. `FutrueTask` 是 `Futrue` 接口的唯一的实现类
	3. `FutureTask` 同时实现了 `Runnable`, `Future` 接口。它既可以作为 `Runnable` 被线程执行，又可以作为 `Future` 得到 `Callable` 的返回值

```java
// 1、创建一个实现Callable接口的实现类
public class MyCallable implements Callable {
	// 2、实现call()方法，将此线程需要执行的操作声明在call()中
	@Override
	public Object call() throws Exception {
		int sum = 0;
		for (int i = 0; i < 100; i++) {
			if (i % 2 == 0){
				System.out.println(i);
				sum = sum + i;
			}
		}
		// 返回值
		return sum;
	}
}
```
   
```java
// 测试类
public class Test {
	public static void main(String[] args) {
		// 3、创建Callable接口实现的对象
		MyCallable myCallable = new MyCallable();
		// 4、将此Callable接口实现的对象作为参数传递到FutureTask构造器中，创建FutureTask的对象
		FutureTask futureTask = new FutureTask(myCallable);
		// 5、将FutureTask的对象作为参数传递到Thread类的构造器中，创建Thread对象
		Thread thread = new Thread(futureTask);
		// 6、使用thread对象调用start()方法启动线程
		thread.start();
		
		// 7、获取Callable中call()方法的返回值，需抛出异常
		try {
			// 将获取的返回值赋值给sum，其类型只能为Object
			Object sum = futureTask.get();
			// 打印sum
			System.out.println("总和为：" + sum);
		} catch (InterruptedException e) {
			e.printStackTrace();
		} catch (ExecutionException e) {
			e.printStackTrace();
		}
	}
}
```
   
3. 如何理解实现 `Callable` 接口的方式创建多线程比实现 `Runnable` 接口创建线程的方式强大
	1. `call()` 可以有返回值
	2. `call()` 可以抛出异常，被外面的操作捕获，获取异常的信息
	3. `Callable` 是支持泛型的

### ②、使用线程池

1. 背景：经常创建和销毁、使用量特别大的资源，比如并发情况下的线程，对性能影响很大。
2. 思路：提前创建好多个线程，放入线程池中，使用时直接获取，使用完放回池中。可以避免频繁创建销毁、实现重复利用。类似生活中的公共交通工具。
3. 好处：
	1. 提高响应速度（减少了创建新线程的时间）
	2. 降低资源消耗（重复利用线程池中线程，不需要每次都创建）
	3. 便于线程管理
		1. `corePoolSize`：核心池的大小
		2. `maximumPoolSize`：最大线程数
		3. `keepAliveTime`：线程没有任务时最多保持多长时间后会终止
		4. 等等
4. 线程池相关API
	1. JDK 5.0 起提供了线程池相关API：`ExecutorService` 和 `Executors`
	2. `ExecutorService`：真正的线程池接口。常见子类 `ThreadPoolExecutor`
		1. `void execute(Runnable command)` ：执行任务/命令，没有返回值，一般用来执行 `Runnable`
		2. `<T> Future<T> submit(Callable<T> task)`：执行任务，有返回值，一般又来执行 `Callable`
		3. `void shutdown()` ：关闭连接池
	3. `Executors`：工具类、线程池的工厂类，用于创建并返回不同类型的线程池
		1. `Executors.newCachedThreadPool()`：创建一个可根据需要创建新线程的线程池
		2. `Executors.newFixedThreadPool(n)`; 创建一个可重用固定线程数的线程池
		3. `Executors.newSingleThreadExecutor()` ：创建一个只有一个线程的线程池
		4. `Executors.newScheduledThreadPool(n)`：创建一个线程池，它可安排在给定延迟后运行命令或者定期地执行。
5. 实现 Runnable 接口的线程池的方法

```java
public class MyThreadPool implements Runnable {
  @Override
  public void run() {
	 for (int i = 0; i < 100; i++) {
		   if (i % 2 == 0){
			  System.out.println(Thread.currentThread().getName() + "：" + i);
		   }
	 }
  }
}
```

```java
public class Test {
  public static void main(String[] args) {
	 // 1、提供指定线程数量的线程池
	 ExecutorService executorService = Executors.newFixedThreadPool(10);
	 // 2、创建实现Runnable接口实现类的对象
	 MyThreadPool myThreadPool = new MyThreadPool();

	 // 3、启动线程，执行指定的线程的操作，需要提供实现Runnable接口实现类的对象
	 // 适合用于Runnable
	 executorService.execute(myThreadPool);

	 // 4、关闭线程
	 executorService.shutdown();
  }
}
```
``
6. 实现 Callable 接口的线程池的方法

```java
public class MyThreadPool02 implements Callable {
  @Override
  public Object call() throws Exception {
	 int sum = 0;
	 for (int i = 0; i < 100; i++) {
		   if (i % 2 == 0){
			  System.out.println(Thread.currentThread().getName() + "：" + i);
			  sum = sum + i;
		   }
	 }
	 return sum;
  }
}
```

```java
public class Test02 {
  public static void main(String[] args) {
	 // 1、提供指定线程数量的线程池
	 ExecutorService executorService = Executors.newFixedThreadPool(10);
	 // 2、创建实现Callable接口实现类的对象
	 MyThreadPool02 myThreadPool02 = new MyThreadPool02();
	 // 3、将此Callable接口实现的对象作为参数传递到FutureTask构造器中，
	 // 创建FutureTask的对象，以便获取返回值
	 FutureTask futureTask = new FutureTask(myThreadPool02);
	 // 4、启动线程，执行指定的线程的操作，需要提供实现Runnable接口实现类的对象
	 // 适合适用于Callable
	 executorService.submit(myThreadPool02);

	 // 5、获取返回值，但是程序运行到这里被阻塞了
	 try {
		   futureTask.get();
	 } catch (InterruptedException e) {
		   e.printStackTrace();
	 } catch (ExecutionException e) {
		   e.printStackTrace();
	 }

	 // 6、关闭线程
	 executorService.shutdown();
  }
}
```

# 八、常用类

## 1、String 类及常用方法

### ①、String 类简介及内存分析

1. <font color="red">String 类（是类，而不是数据类型）：代表字符串。</font>Java 程序中的所有字符串字面值（如 `abc` ）都作为此类的实例实现。
2. `String` 是一个 `final` 类，代表<font color="red">不可变的字符序列</font>。
3. 字符串是常量，用双引号引起来表示。它们的值在创建之后不能更改。
4. `String` 对象的字符内容是存储在一个字符数组 `value[]` 中的。

```java
public final class String
	implements java.io.Serializable, Comparable<String>, CharSequence {
	/** The value is used for character storage. */
	private final char value[];
	/** Cache the hash code for the string */
	private int hash; // Default to 0
```

5. 理解 String 的不可变型

```java
public class StringTest {
	public static void main(String[] args) {
		/**
		* String：字符串，使用一对""引起来表示
		* 1、String声明为final的，不可被继承
		* 2、实现了Serializable接口：表示字符串是支持序列化的（io流）
		* 3、实现了Comparable接口：表示String字符串可以比较大小
		* 4、String内部定义了final char[] value用于存储字符串数据
		* 5、String代表不可变的字符串序列。简称：不可变型
		*    体现：1、当对字符串重新赋值时，需要重写指定内存区域赋值，不能使用原有的value进行赋值
		*         2、对现有的字符串进行链接操作时，也需要重新指定内存区域赋值，不能使用原有的value进行赋值
		*         3、当调用String的replace()方法修改指定字符或自古出时，也需要重新指定内存区域赋值，不能使用原有的value进行赋值
		* 6、通过字面量的方式（区别于new）给一个字符串赋值，此时的字符串值声明在字符串常量池中
		* 7、字符串常量池中是不会存储相同内容的字符串的。
		*/
		String s1 = "abc";  //字面量的定义方式 --> 直接赋值
		String s2 = "abc";  //
		String s3 = "abc";
		String s4 = "abc";
		System.out.println(s1 == s2 && s2 == s3);   //true

		s1 = "hello";
		System.out.println(s1); //hello
		System.out.println(s2); //abc

		s3 = s3 + "def";
		System.out.println(s3); //abcdef
		System.out.println(s2); //abc

		//s4中的a变成m,然后赋值给s5
		String s5 = s4.replace('a','m');
		System.out.println(s4); //abc
		System.out.println(s5); //mbc
	}
}
```

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F04、String方法内存区解释.jpg)

6. String 对象的创建

```java
// 字符串常量存储在字符串常量池，目的是共享
String str = "hello";

// 字符串非常量对象存储在堆中。
// 本质上this.value = new char[0];
String s1 = new String(); 

// this.value = original.value;
String s2 = new String(String original); 

// this.value = Arrays.copyOf(value, value.length);
String s3 = new String(char[] a); 

String s4 = new String(char[] a,int startIndex,int count);
```

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F05、创建字符串方式的区别.png)

7. 字符串对象是如何存储的

```java
public class demo02 {
	public static void main(String[] args) {
		// 通过字面量定义的方式，此时的s1和s2的数据“JavaEE”声明在方法区中的字符串常量池中
		// jdk7，字符串常量池被移到了堆中，jdk8以后有移到常量池中了
		String s1 = "javaEE";
		String s2 = "javaEE";

		// 通过new + 构造器的方式，此时的s3和s4保存的地址值，是数据在堆空间开辟空间以后对应的地址值
		// 虽然堆中也是指向常量池，但是s3与s4指向的是堆，所以是float
		String s3 = new String("javaEE");
		String s4 = new String("javaEE");

		System.out.println(s1 == s2);   //true
		System.out.println(s1 == s3);   //float
		System.out.println(s1 == s4);   //float
		System.out.println(s3 == s4);   //float
	}
}
```

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F06、字符串对象是如何存储的.png)

8. 字符串对象是如何存储的2

```java
class Person{
	String name;

	public Person() {}
	public Person(String name) {this.name = name;}
}

public class deno03 {
	public static void main(String[] args) {
		// Person p1 = new Person("aaa");
		Person p1 = new Person();
		p1.name = "aaa";

		Person p2 = new Person();
		p2.name = "aaa";

		// 1、equals()比较字符串中所包含的内容是否相同。
		System.out.println(p1.name.equals(p2.name));    //true
		// 2、“==”比较两个变量本身的值，即两个对象在内存中的首地址。
		System.out.println(p1.name == p2.name);    //true
		// 3、两者指向的常量池中的地址相同
		System.out.println(p1.name == "aaa");    //true
	}
}
```

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F07、字符串对象是如何存储的2.png)

9. 面试题：`String s = new String("abc");` 方式创建对象，在内存中创建了几个对象？
	1.  两个
	2.  一个是堆空间中 new 结构
	3.  另一个是 `char[]` 对应的常量池中的数据：abc
	4.  <font color="red">若是常量池中原先已有"abc"，则不会创建新的对象，而是沿用之前的</font>
10. 字符串的特性：
	1. 常量与常量的拼接结果在常量池。且常量池中不会存在相同内容的常量。
	2. 只要其中有一个是变量，结果就在堆中

	```java
public class demo01 {
	public static void main(String[] args) {
		String s1 = "javaEE";
		String s2 = "hadoop";

		String s3 = "javaEEhadoop";
		String s4 = "javaEE" + "hadoop";
		String s5 = s1 + "hadoop";
		String s6 = "javaEE" + s2;
		String s7 = s1 + s2;

		// s3与s4这种字符串拼接的，是直接在常量池中寻找相同的
		System.out.println(s3 == s4);   //true
		System.out.println(s3 == s5);   //false
		System.out.println(s3 == s6);   //false
		System.out.println(s3 == s7);   //false
		// s5、s6、s7是在堆中重新开辟地址空间
		System.out.println(s5 == s6);   //false
		System.out.println(s5 == s7);   //false
		System.out.println(s6 == s7);   //false

		// intern()方法：获取此字符串的常量池中的地址
		// 也可以这么写：String s8 = "javaEEhadoop".intern();
		String s8 = s5.intern();
		System.out.println(s3 == s8);   //true
	}
}
	```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F08、字符串的特性.jpg)

### ②、String 类常用方法

```java
public class demo02 {
	public static void main(String[] args) {
		String s1 = "Hello World";
		String s2 = "hello world";
		String s3 = "  Hello world  ";
		String s4 = "abc123def456";

		// 1、int length()：返回字符串的长度： return value.length
		System.out.println(s1.length());
		// 2、char charAt(int index)： 返回某索引处的字符return value[index]
		System.out.println(s1.charAt(0));
		System.out.println(s1.charAt(2));
		// 3、boolean isEmpty()：判断是否是空字符串：return value.length == 0
		// 空字符串返回true，非空字符串返回false
		System.out.println(s1.isEmpty());
		// 4、String toLowerCase()：使用默认语言环境，将 String 中的所有字符转换为小写
		System.out.println(s1.toLowerCase());
		// 5、String toUpperCase()：使用默认语言环境，将 String 中的所有字符转换为大写
		System.out.println(s1.toUpperCase());
		// 6、String trim()：返回字符串的副本，忽略前导空白和尾部空白
		// 只会删掉最前面和最后面的空白，被字符(中英文数字等所有符号)包裹起来的空格不会被删掉
		System.out.println(s3.trim());
		// 7、boolean equals(Object obj)：比较字符串的内容是否相同
		// 相比较的字符串相同返回true，不同返回false
		System.out.println(s1.equals(s2));
		// 8、boolean equalsIgnoreCase(String anotherString)：与equals方法类似，忽略大小写
		System.out.println(s1.equalsIgnoreCase(s2));
		// 9、String concat(String str)：将指定字符串连接到此字符串的结尾。 等价于用“+”
		System.out.println(s1.concat(s2));
		// 10、int compareTo(String anotherString)：比较两个字符串的大小
		// 比较时化为ASCII码比较，涉及到字符串排序
		// 结果为负则前面的小，结果为正则前面的大，结果为0则相同
		System.out.println(s1.compareTo(s2));
		// 11、String substring(int beginIndex)：返回一个新的字符串，它是此字符串的从beginIndex开始(包含，从0开始)截取到最后的一个子字符串。
		System.out.println(s1.substring(3));
		// 12、String substring(int beginIndex, int endIndex) ：返回一个新字符串，它是此字符串从beginIndex开始(包含，从0开始)截取到endIndex(不包含)的一个子字符串。
		// 左闭右开
		System.out.println(s1.substring(3,7));
		// 13、boolean endsWith(String suffix)：测试此字符串是否以指定的后缀结束
		System.out.println(s1.endsWith("ld"));
		// 14、boolean startsWith(String prefix)：测试此字符串是否以指定的前缀开始
		System.out.println(s1.startsWith("  H"));
		// 15、boolean startsWith(String prefix, int toffset)：测试此字符串从指定索引开始的子字符串是否以指定前缀开始
		System.out.println(s1.startsWith("ll",2));
		// 16、boolean contains(CharSequence s)：当且仅当此字符串包含指定的 char 值序列时，返回 true
		System.out.println(s1.contains("llo"));
		// 17、int indexOf(String str)：返回指定子字符串在此字符串中第一次出现处的索引
		// 返回第一次出现的位置的数字
		System.out.println(s1.indexOf("ll"));
		// 18、int indexOf(String str, int fromIndex)：返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引开始
		System.out.println(s1.indexOf("ll",6));
		// 19、int lastIndexOf(String str)：返回指定子字符串在此字符串中最右边出现处的索引
		// 但是返回的数字依然是从前往后数的，因为返回的是数组的角标
		System.out.println(s1.lastIndexOf("ll"));
		// 20、int lastIndexOf(String str, int fromIndex)：返回指定子字符串在此字符串中最后一次出现处的索引，从指定的索引开始反向搜索
		// 但是返回的数字依然是从前往后数的，因为返回的是数组的角标
		// 问：什么情况下indexOf(str)和lastIndexOf(str)返回值相同
		//      1、只存在唯一一个str。       2、不存在str
		// 注：indexOf和lastIndexOf方法如果未找到都是返回-1
		System.out.println(s1.lastIndexOf("ll",6));
		// 21、String replace(char oldChar, char newChar)：返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。
		// 替换一个字符，替换所有的匹配的
		System.out.println(s1.replace("l","llll"));
		// 22、String replace(CharSequence target, CharSequence replacement)：使用指定的字面值替换序列替换此字符串所有匹配字面值目标序列的子字符串。
		// 替换一个字符串，替换所有的匹配的
		System.out.println(s1.replace("World","hell"));
		// 23、String replaceAll(String regex, String replacement)：使用给定的replacement替换此字符串所有匹配给定的正则表达式的子字符串。
		// 正则表达式：\d+：匹配数字串，替换所有的匹配的
		System.out.println(s4.replaceAll("\\d+","被替换"));
		// 24、String replaceFirst(String regex, String replacement)：使用给定的replacement替换此字符串匹配给定的正则表达式的第一个子字符串。
		// 只替换一次
		System.out.println(s4.replaceFirst("\\d+","被替换"));
		// 25、boolean matches(String regex)：告知此字符串是否匹配给定的正则表达式。
		String str25 = "12345";
		//判断str字符串中是否全部有数字组成，即有1-n个数字组成
		System.out.println(str25.matches("\\d+"));
		// 26、String[] split(String regex)：根据给定正则表达式的匹配拆分此字符串。
		String str26 = "hello|world|java";
		String[] strs = str26.split("\\|");
		for (int i = 0; i < strs.length; i++) {
			System.out.println(strs[i]);
		}
		// 27、String[] split(String regex, int limit)：根据匹配给定的正则表达式来拆分此字符串，最多不超过limit个，如果超过了，剩下的全部都放到最后一个元素中。
		String str27 = "hello.world.java";
		String[] strs2 = str27.split("\\.",2);
		for (int i = 0; i < strs2.length; i++) {
			System.out.println(strs2[i]);
		}
	}
}
```

### ③、String 与其他数据类型的转换

#### Ⅰ、String 与基本数据类型、包装类的转换

1. `String` -> 基本数据类型、包装类：调用包装类的静态方法：`parseInt()`

```java
String str1 = "123";
int num = Integer.parseInt(str1);
```
    
2. 基本数据类型、包装类 -> `String`：调用 String 重载的 `valueOf()` 方法

```java
int i = 123;
String str2 = String.valueOf(i);
// 当然也可以直接这样
str2 = i + ""; 
```

#### Ⅱ、String 与字符数组 `char[]` 的转换

1. `String` -> `char[]`：调用 `String` 的 `toCharArray()` 方法

```java
public class demo05 {
	public static void main(String[] args) {
		String str = "abc123";
		
		char[] arr = str.toCharArray();

		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}
}
```
    
1. `char[]` --> `String`：调用 `String` 的构造器

```java
char[] arr2 = {'h','e','l','l','o'};
String str2 = new String(arr2);
```
   
#### Ⅲ、String 与字节数组 `byte[]` 的转换

```java
public class demo06 {
	public static void main(String[] args) throws UnsupportedEncodingException {
		String str1 = "abc123月海";

		// 1、String --> byte[]：调用String的getBytes()方法
		// 使用默认的字符集进行编码
		byte[] bytes1 = str1.getBytes();
		// Arrays.toString()：将数组转换成String类型输出
		// 因数组是bytes类型的，所以打印出来是ACSII码
		System.out.println(Arrays.toString(bytes1));

		// 使用GBK字符集进行编码
		byte[] bytes2 = str1.getBytes("GBK");
		System.out.println(Arrays.toString(bytes2));

		System.out.println("------------------------------------");

		// 2、byte[] --> String：调用String的构造器
		// 使用默认的字符集进行解码
		String str2 = new String(bytes1);
		System.out.println(str2);

		// 使用默认的字符集（UTF-8）对使用GBK编码的数据进行解码，会出现乱码
		// 故，编码字符集和解码字符集要相同，否则会出现乱码
		String str3 = new String(bytes2);
		System.out.println(str3);

		// 使用GBK字符集进行解码
		String str4 = new String(bytes2, "GBK");
		System.out.println(str4);
	}
}
```

```shell
[97, 98, 99, 49, 50, 51, -26, -100, -120, -26, -75, -73]
[97, 98, 99, 49, 50, 51, -44, -62, -70, -93]
------------------------------------
abc123月海
abc123�º�
abc123月海

Process finished with exit code 0
```

### ④、常见算法题目


1. 模拟一个 `trim` 方法，去除字符串两端的空格。

```java
public class demo07 {
	public static void main(String[] args) {
		// 定义需要处理的字符串
		String str = "  hello world  ";

		// 创建TrimTest对象
		TrimTest trimTest = new TrimTest();
		// 调用TrimTest对象的trimTest方法，并输出
		System.out.println(trimTest.trimTest(str));
	}
}

class TrimTest{
	public char[] trimTest(String str){
		// 将传输过来的str字符串转换为char型数组arr
		char[] arr = str.toCharArray();
		// 定义前面的空格
		int frontSpace = 0;
		// 定义后面的空格
		int behindSpace = 0;

		// 计算前面的空格
		for (int i = 0; i < arr.length; i++) {
			// 通过循环，依次将arr数组分别赋值给str01字符串
			String str01 = new String(String.valueOf(arr[i]));
			// 通过循环，依次比较str01这个字符串是否是空格，直到遇到不是空格的就跳出循环
			if(str01.equals(" ")){
				// 记录从前面开始有几个连续的空格
				frontSpace++;
			}else{
				break;
			}
		}

		// 计算后面的空格
		for (int i = 0; i < arr.length; i++) {
			// 通过循环，依次将arr数组分别赋值给str01字符串，不过这次是从最后面开始
			String str01 = new String(String.valueOf(arr[arr.length - i - 1]));
			// 通过循环，依次比较str01这个字符串是否是空格，直到遇到不是空格的就跳出循环
			if(str01.equals(" ")){
				// 记录从后面开始有几个连续的空格
				behindSpace++;
			}else{
				break;
			}
		}

		// 定义一个接收数组数据的数组arrTest，长度为输入的数组减去两端的空格
		char[] arrTest = new char[arr.length - frontSpace - behindSpace];

		// 循环长度为arrTest数组的长度
		for (int i = 0; i < arrTest.length; i++) {
			// 从输入数组的不是空格的第一位开始，赋值给arrTest数组
			arrTest[i] = arr[i + frontSpace];
		}

		// 返回arrTest数组
		return arrTest;
	}
}
```

2. 将一个字符串进行反转。将字符串中指定部分进行反转。比如 `abcdefg` 反转为 `abfedcg` 
3. 获取一个字符串在另一个字符串中出现的次数。比如：获取 `ab` 在 `abkkcadkabkebfkabkskab` 中出现的次数
4. 获取两个字符串中最大相同子串。比如：`str1 = "abcwerthelloyuiodef"; str2 = "cvhellobnm"`。提示：将短的那个串进行长度依次递减的子串与较长的串比较。
5. 对字符串中字符进行自然顺序排序。
	1. 提示：字符串变成字符数组。
	2. 对数组排序，选择，冒泡，`Arrays.sort()`;
	3. 将排序后的数组变成字符串。

### ⑤、`StringBuffer`、`StringBuilder` 类及常用方法

#### Ⅰ、简介

1. `java.lang.StringBuffer` 代表<font color="red">可变的字符序列</font>，JDK1.0 中声明，可以对字符串内容进行<font color="red">增删</font>，此时不会产生新的对象。
2. <font color="red">很多方法与 String 相同。</font>
3. 作为参数传递时，方法内部可以改变值。
4. `String`、`StringBuffer`、`StringBuilder` 三者的异同
	1. `String`：不可变的字符序列
	2. `StringBuffer`：可变的字符序列，线程是安全的，但是效率偏低
	3. `StringBuilder`：可变的字符序列，线程是不安全的，效率高，jdk5.0 新增
	4. 三者底层都使用 `char[]` 数组存储，jdk1.9 之后都改为 `byte[]`

#### Ⅱ、`StringBuffer`、`StringBuilder` 源码分析

```java
// 源码分析
public class demo08 {
	public static void main(String[] args) {
		// char[] value = new char[0];
		String str01 = new String();
		// char[] value = new char[]{'a','b','c'};
		String str02 = new String("abc");

		// char[] value = new char[16]; --> 底层创建了一个长度是16的数组
		StringBuffer sb01 = new StringBuffer();
		// value[0] = 'a'; --> 所以StringBuffer字符串改变的本质是value数组增加了元素
		sb01.append('a');
		// value[1] = 'b';
		sb01.append('b');
		// char[] value = new char["abc".length() + 16]; --> 所以不论字符串有多长，value都会比他长16
		StringBuffer sb02 = new StringBuffer("abc");

		/**
		* 问题1：此时输出sb02的长度是多少 --> 3，输出的是有效长度，只与定义了多少有关
		* 问题2：扩容问题：如果要添加的数据底层数组盛不下了，怎么扩容？
		*        默认情况下，扩容为原来的2倍+2，同时将原有数组中的元素赋值到新的数组中
		* 指导意义：开发中建议使用：StringBuffer(int capacity) 或 StringBuilder(int capacity)
		*           来指定字符串的长度，以减少不必要的性能消耗
		* */
	}
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F08、StringBuilder方法链.png)

#### Ⅲ、`StringBuffer`、`StringBuilder` 常用方法

```java
public class demo09 {
	public static void main(String[] args) {
		StringBuilder s1 = new StringBuilder("abc123");

		// 1、StringBuffer append(xxx)：提供了很多的append()方法，用于进行字符串拼接，在最后面添加
		// int、char、char[]、float、double、long、boolean、String等
		System.out.println(s1.append("qwe"));
		// 2、StringBuffer delete(int start,int end)：删除指定位置的内容，删除两数直接的元素，左闭右开
		System.out.println(s1.delete(3, 6));
		// 3、StringBuffer insert(int offset, xxx)：在指定位置插入xxx
		System.out.println(s1.insert(3,"123"));
		// 4、StringBuffer replace(int start, int end, String str)：把[start,end)位置替换为str
		System.out.println(s1.replace(3,6,"456"));
		// 5、StringBuffer reverse() ：把当前字符序列逆转
		System.out.println(s1.reverse());

		// public int indexOf(String str)，返回指定子字符串在此字符串中第一次出现处的索引
		// 与String相同
		System.out.println(s1.indexOf("a"));
		// public String substring(int start,int end)，左闭右开
		// 返回一个新字符串，它是此字符串从beginIndex开始(包含，从0开始)截取到endIndex(不包含)的一个子字符串。
		System.out.println(s1.substring(0, 3));
		// public int length()，返回字符串的长度
		System.out.println(s1.length());
		// public char charAt(int n )，返回某索引处的字符return value[index]
		System.out.println(s1.charAt(6));
		// public void setCharAt(int n ,char ch)，在指定位置插入
		s1.setCharAt(0,'x');
		System.out.println(s1);
	}
}
```

1. 当 `append` 和 `insert` 时，如果原来 `value` 数组长度不够，可扩容。
2. 如上（1~5）这些方法支持方法链操作，原理：

```java
// 原理：因为返回的还是原本的字符串，所以可以再次调用
@Override
public StringBuilder append(String str) {
	super.append(str);
	return this;
}
```

```java
// 比如：
StringBuilder s2 = new StringBuilder();
s1.append("123456789").delete(0,3).insert(0,"abc");
```

3. 总结：
	1. 增：`append(xxx)`
	2. 删：`delete(int start,int end)`
	3. 改：`replace(int start, int end, String str)、setCharAt(int n ,char ch)`
	4. 查：`charAt(int n )`
	5. 插：`insert(int offset, xxx)`
	6. 长度：`length()`
	7. 遍历：`for() + charAt(int n )`

#### Ⅳ、String、StringBuffer、StringBuilder 效率对比

1. 效率从高到低排列：`StringBuilder` > `StringBuffer` > `String`
2. String 的效率远远低于另外两个

## 2、JDK 8 之前的日期时间 API

### ①、System 静态方法

1. System 类提供的 `public static long currentTimeMillis()` 用来返回当前时间与 1970 年 1 月 1 日 0 时 0 分 0 秒之间<font color="red">以毫秒为单位的时间差</font>。时间戳
2. 此方法适于计算时间差。
3. 计算世界时间的主要标准有：
	1. UTC(Coordinated Universal Time)
	2. GMT(Greenwich Mean Time)
	3. CST(Central Standard Time)
```java
long time = System.currentTimeMillis();
System.out.println(time);
```

### ②、Date 类

#### Ⅰ、`java.util.Date` 类

1. `java.util.Date` 类，表示特定的瞬间，精确到毫秒
2. 构造器：
	1. `Date()`：使用无参构造器创建的对象可以获取本地当前时间。
	2. `Date(long date)`
3. 常用方法
	1. `getTime()`：返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 `Date` 对象表示的毫秒数，与 `System.currentTimeMillis()` 方法相同
	2. `toString()`：
		1. 显示当前的年、月、日、时、分、秒
		2. 把此 `Date` 对象转换为以下形式的 String： `dow mon ddhh:mm:ss zzz yyyy`；其中： dow 是一周中的某一天 (Sun, Mon, Tue, Wed, Thu, Fri, Sat)，zzz 是时间标准。

```java
import java.util.Date;

public class demo01 {
	public static void main(String[] args) {
		// 构造器一：Date()：创建了一个对应当前时间的Date对象
		Date date01 = new Date();
		// toString()：显示当前的年、月、日、时、分、秒
		System.out.println(date01.toString());
		// getTime()：返回当前时间与1970年1月1日00:00:00之间以毫秒为单位的时间差
		// 与System.currentTimeMillis()方法相同
		System.out.println(date01.getTime());

		// 构造器二、创建一个指定毫秒数的Date对象
		// 毫秒数时long型的数据，所以最后面要加：L
		Date date02 = new Date(1636294443690000L);
		System.out.println(date02.toString());
	}
}
```

```shell
Sun Nov 07 22:31:46 CST 2021
1636295506997
Sat Feb 09 10:21:30 CST 53822

Process finished with exit code 0
```

#### Ⅱ、`java.sql.Date` 类

1. `java.sql.Date` 类，是 `java.util.Date` 类的子类，对应着数据库中的日期类型的变量
2. 构造器：只有 `Date(long date)` 构造器
3. 常用方法：同样有 `getTime()` 与 `toString()` 方法
4. 创建 `java.sql.Date` 对象

```java
import java.sql.Date;

public class demo02 {
	public static void main(String[] args) {
		// 创建java.sql.Date对象
		Date date01 = new Date(16362944436900L);
		System.out.println(date01);
	}
}
```

6. 如何将 `java.util.Date` 对象转换为 `java.sql.Date` 对象

```java
// 如何将 java.util.Date 对象转换为 java.sql.Date 对象
public class demo03 {
	public static void main(String[] args) {

		// 构造器一：Date()：创建了一个对应当前时间的Date对象
		Date date01 = new Date();
		// toString()：显示当前的年、月、日、时、分、秒
		System.out.println(date01.toString());

		// 如何将 java.util.Date对象转换为java.sql.Date对象
		// 情况一：使用向下转型，不建议使用
		java.sql.Date date02 = (java.sql.Date) date01;

		// 情况二：新创建一个java.sql.Date对象，然后将java.util.Date的对象作为参数传入
		// 因为java.sql.Date只有者一个构造器可以用，共同的只有时间戳
		java.sql.Date date03 = new java.sql.Date(date01.getTime());
	}
}
```

#### Ⅲ、SimpleDateFormat 类

1. `java.text.SimpleDateFormat` 类
2. Date 类的 API 不易于国际化，大部分被废弃了，`java.text.SimpleDateFormat` 类是一个不与语言环境有关的方式来格式化和解析日期的具体类。
3. 它允许进行<font color="red">格式化：日期 -> 文本</font>、<font color="red">解析：文本 -> 日期</font>
4. 格式化：
   1.  `SimpleDateFormat()`：默认的模式和语言环境创建对象
   2.  `public SimpleDateFormat(String pattern)`：该构造方法可以用参数 `pattern` 指定的格式创建一个对象，该对象调用：`public String format(Date date)`：方法格式化时间对象 date
5. 解析：`public Date parse(String source)`：从给定字符串的开始解析文本，以生成一个日期。格式化的逆过程
6. 默认构造器：

```java
public class demo04 {
	public static void main(String[] args) throws ParseException {
		// 实例化SimpleDateFormat
		SimpleDateFormat sdf = new SimpleDateFormat();

		// 格式化日期，format()方法：Date日期 --> 字符串
		Date date = new Date();             // 通过Date获取当前日期
		System.out.println(date);           // 打印未格式化的日期
		String format = sdf.format(date);   // 格式化日期
		System.out.println(format);         // 打印格式化后的日期

		// 解析日期，parse()方法：字符串 --> Date日期
		String str = "1996-09-20 下午9:46"; // 创建被格式化后的日期字符串
		Date date02 = sdf.parse(str);       // 解析日期，并赋值给Date对象
		System.out.println(date02);         // 打印解析后的日期
	}
}
```

7. 有参构造器：

```java
public class demo05 {
	public static void main(String[] args) {
		// 实例化SimpleDateFormat
		// 日常开发中常使用如下字符：
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

		// 通过Date获取当前日期
		Date date = new Date();
		// 调用SimpleDateFormatd的format(方法)格式化日期
		String str = sdf.format(date);
		// 打印格式化后的日期
		System.out.println(str);
	}
}
```

8. SimpleDateFormat中的符号说明：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F09、SimpleDateFormat中的符号.png)

#### Ⅳ、Calendar（日历）类


1. `Calendar` 是一个抽象基类，主要用于完成日期字段之间相互操作的功能。 
2. 获取 `Calendar` 实例的方法：
	1. 使用 `Calendar.getInstance()` 方法
	2. 调用它的子类 `GregorianCalendar` 的构造器。
3. 一个 `Calendar` 的实例是系统时间的抽象表示，通过 `get(int field)` 方法来取得想要的时间信息。比如 YEAR、MONTH、DAY_OF_WEEK、HOUR_OF_DAY 、MINUTE、SECOND
	1. `public void get(int field,int value)`
	2. `public void set(int field,int value)`
	3. `public void add(int field,int amount)`
	4. `public final Date getTime()`
	5. `public final void setTime(Date date)`
4. <font color="red">注意</font>：
	1. 获取月份时：一月是 0，二月是 1，以此类推，12 月是 11
	2. 获取星期时：周日是 1，周二是 2 ， 。。。。周六是 7
\
```java
public class demo06 {
	public static void main(String[] args) {
		// 一、实例化
		// 方式一、创建其子类（GregorianCalendar）的对象
		GregorianCalendar gregorianCalendar = new GregorianCalendar();

		// 方式二、调用其静态方法：getInstance()
		// 两种方式都一样，都是调用的GregorianCalendar
		Calendar calendar = Calendar.getInstance();

		// 二、常用方法
		// 1、get()，获取
		// 获取今天是这个周的第几天
		System.out.println(calendar.get(Calendar.DAY_OF_WEEK));
		// 获取今天是这个月的第几天
		System.out.println(calendar.get(Calendar.DAY_OF_MONTH));
		// 获取今天是今年的第几天
		System.out.println(calendar.get(Calendar.DAY_OF_YEAR));

		// 2、set()，修改
		// 将今天改为是今年的第200天
		calendar.set(Calendar.DAY_OF_YEAR,200);
		// 获取今天是今年的第几天，原来的数值发生了改变
		System.out.println(calendar.get(Calendar.DAY_OF_YEAR));

		// 3、add()，增加
		// 在今天的基础上增加3天
		calendar.add(Calendar.DAY_OF_YEAR,3);
		System.out.println(calendar.get(Calendar.DAY_OF_YEAR));
		// 在今天的基础上减去3天
		calendar.add(Calendar.DAY_OF_YEAR,-3);
		System.out.println(calendar.get(Calendar.DAY_OF_YEAR));

		// 4、getTime()，通过日历类得到了一个Date的数据
		Date date01 = new Date();
		date01 = calendar.getTime();
		System.out.println(date01);

		// 5、setTime()，将Date数据变为日历类
		// 与SimpleDateFormat类的parse()类似
		Date date02 = new Date();
		calendar.setTime(date02);
		System.out.println(calendar.get(Calendar.DAY_OF_YEAR));
	}
}
```

## 3、JDK 8 中新日期时间 API

### ①、背景

1. 如果我们可以跟别人说：“我们在 1502643933071 见面，别晚了！” 那么就再简单不过了。但是我们希望时间与昼夜和四季有关，于是事情就变复杂了。JDK 1.0 中包含了一个 `java.util.Date` 类，但是它的大多数方法已经在 JDK 1.1 引入 `Calendar` 类之后被弃用了。而 `Calendar` 并不比 `Date` 好多少。它们面临的问题是：
2. <font color="red">可变性</font>：像日期和时间这样的类应该是不可变的。
3. <font color="red">偏移性</font>：Date 中的年份是从 1900 开始的，而月份都从 0 开始。
4. <font color="red">格式化</font>：格式化只对 Date 有用，Calendar 则不行。
5. 此外，它们也不是线程安全的；不能处理闰秒等。
6. <font color="red">总结：对日期和时间的操作一直是J ava 程序员最痛苦的地方之一。</font>
7. 第三次引入的 API 是成功的，并且 Java 8 中引入的 <font color="red">java.time</font> API 已经纠正了过去的缺陷，将来很长一段时间内它都会为我们服务。
8. Java 8 吸收了 Joda-Time 的精华，以一个新的开始为 Java 创建优秀的 API。新的 `java.time` 中包含了所有关于<font color="red">本地日期（LocalDate）、本地时间（LocalTime）、本地日期时间（LocalDateTime）、时区（ZonedDateTime）和持续时间（Duration）的类。</font>历史悠久的 Date 类新增了 `toInstant()` 方法，用于把 Date 转换成新的表示形式。这些新增的本地化时间日期 API 大大简化了日期时间和本地化的管理。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F10、JDK%208中新日期时间API.png)

### ②、LocalDate、LocalTime、LocalDateTime


1. `LocalDate`、`LocalTime`、`LocalDateTime` 类是其中较重要的几个类，它们的实例是不可变的对象，分别表示使用 ISO-8601日历系统的日期、时间、日期和时间。它们提供了简单的本地日期或时间，并不包含当前的时间信息，也不包含与时区相关的信息。
2. <font color="red">LocalDate</font> 代表 IOS 格式（yyyy-MM-dd）的日期，可以存储 生日、纪念日等日期。
3. <font color="red">LocalTime</font> 表示一个时间，而不是日期。
4. <font color="red">LocalDateTime</font> 是用来表示日期和时间的，<font color="red">这是一个最常用的类之一</font>。
5. 注：ISO-8601 日历系统是国际标准化组织制定的现代公民的日期和时间的表示法，也就是公历。
6. <font color="red">具体方法：三个类都可以用</font>

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F11、JDK%208中新日期时间API的方法.png)

```java
public class demo07 {
	public static void main(String[] args) {
		// 一、now()：静态方法，根据当前时间创建对象/指定时区的对象
		LocalDate localDate = LocalDate.now();  // 获取本地日期
		LocalTime localTime = LocalTime.now();  // 获取本地时间
		LocalDateTime localDateTime = LocalDateTime.now();// 获取本地日期和时间

		System.out.println(localDate);
		System.out.println(localTime);
		System.out.println(localDateTime);

		// 二、of()：设置指定的时间与日期
		LocalDate.of(1996,9,20);    // 设置日期
		LocalTime.of(20,00,00); // 设置时间
		LocalDateTime.of(2021,11,9,21,19,01);// 设置日期和时间
		// 打印指定的时间与日期
		System.out.println(LocalDateTime.of(2021,11,9,21,19,01));

		// 三、get()：获取
		// 1、获取今天是本周的第几天
		System.out.println(localDateTime.getDayOfWeek());
		// 2、获取今天是本月的第几天
		System.out.println(localDateTime.getDayOfMonth());
		// 3、获取今天是今年的第几天
		System.out.println(localDateTime.getDayOfYear());
		// 4、获取现在是多少年
		System.out.println(localDateTime.getYear());
		// 5、获取现在是几月，英文
		System.out.println(localDateTime.getMonth());
		// 6、获取现在是几月，数字
		System.out.println(localDateTime.getMonthValue());
		// 7、获取现在是多少小时
		System.out.println(localDateTime.getHour());
		// 8、获取现在是多少分钟
		System.out.println(localDateTime.getMinute());
		// 9、获取现在是多少秒
		System.out.println(localDateTime.getSecond());
		// 10、获取现在是多少纳秒
		System.out.println(localDateTime.getNano());
		// 11、获取使用的是什么年表
		System.out.println(localDateTime.getChronology());

		// 四、with()：修改，原数据不变，不可变性
		// 1. 修改今天是这个月的第几天，他会返回一个修改后的对象
		System.out.println(localDateTime.withDayOfMonth(7));
		//      原时间并没有被修改
		System.out.println(localDateTime);
		// 2、修改今天是今年的第几天
		System.out.println(localDateTime.withDayOfYear(1));
		// 3、修改现在是第多少年
		System.out.println(localDateTime.withYear(1));
		// 4、修改现在是几月
		System.out.println(localDateTime.withMonth(7));
		// 5、修改现在是几点
		System.out.println(localDateTime.withHour(1));
		// 6、修改现在是多少分钟
		System.out.println(localDateTime.withMinute(1));
		// 7、修改现在是多少秒
		System.out.println(localDateTime.withSecond(1));
		// 8、修改现在是多少纳秒
		System.out.println(localDateTime.withNano(1));

		// 五、plus()：增加时间和日期
		// 1、使年份增加一年
		System.out.println(localDateTime.plusYears(1));
		// 2、使小时增加一小时
		System.out.println(localDateTime.plusHours(1));
		// 3、使年份减少一年，加负的当然就是减少了
		System.out.println(localDateTime.plusYears(-1));

		// 六、minus()：减少时间和日期
		// 1、使年份减少一年
		System.out.println(localDateTime.minusYears(1));
		// 2、使年份增加一年，减负的当然就是增加了
		System.out.println(localDateTime.minusYears(-1));
	}
}
```

### ③、Instant 瞬时

1. Instant：时间线上的一个瞬时点。 这可能被用来记录应用程序中的事件时间戳。
2. 在处理时间和日期的时候，我们通常会想到年、月、日、时、分、秒。然而，这只是时间的一个模型，是面向人类的。第二种通用模型是面向机器的，或者说是连续的。在此模型中，时间线中的一个点表示为一个很大的数，这有利于计算机处理。<font color="red">在 UNIX 中，这个数从 1970 年开始，以秒为的单位；同样的，在 Java 中，也是从 1970 年开始，但以毫秒为单位。</font>
3. `java.time` 包通过值类型 `Instant` 提供机器视图，不提供处理人类意义上的时间单位。`Instant` 表示时间线上的一点，而不需要任何上下文信息，例如，时区。概念上讲，它只是简单的表示自 1970 年 1 月 1 日 0 时 0 分 0 秒（UTC）开始的秒数。因为 `java.time` 包是基于纳秒计算的，所以 `Instant` 的精度可以达到纳秒级。
4. 1 秒 = 1000 毫秒 =10^6 微秒=10^9 纳秒，(1 ns = 10-9 s)
5. 时间戳是指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数。
6. `Instant` 中的方法：类似于 `java.util.Date` 类

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F12、Instant中的方法.png)

```java
public class demo08 {
	public static void main(String[] args) {
		// now()，静态方法，实例化：Instant
		// 获取基于本初子午线对应的标准时间
		Instant instant = Instant.now();
		System.out.println(instant);

		// ofEpochMilli(long epochMilli)，静态方法，实例化：ofEpochMilli
		// 返回在1970-01-01 00:00:00基础上加上指定毫秒数之后的Instant类的对象
		Instant ofEpochMilli = Instant.ofEpochMilli(99999999999999L);
		System.out.println(ofEpochMilli);

		// 结合即时的时间的偏移量来创建一个 OffsetDateTime
		// 2021-11-10T21:20:52.759+08:00
		OffsetDateTime atOffset = instant.atOffset(ZoneOffset.ofHours(8));
		System.out.println(atOffset);

		// 返回1970-01-01 00:00:00到当前时间的毫秒数，即为时间戳
		long toEpochMilli = instant.toEpochMilli();
		System.out.println(toEpochMilli);
	}
}
```

### ④、DateTimeFormatter

1. 格式化或解析日期、时间
2. <font color="red">java.time.format.DateTimeFormatter</font> 类：该类提供了三种格式化方法：
3. 预定义的标准格式。如：ISO_LOCAL_DATE_TIME、ISO_LOCAL_DATE、ISO_LOCAL_TIME
4. 本地化相关的格式。如：`ofLocalizedDateTime(FormatStyle.LONG)`
5. <font color="red">自定义的格式。如：ofPattern(“yyyy-MM-dd hh:mm:ss”)</font>
6. 具体方法：类似于 `SimpleDateFormat`

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F13、DateTimeFormatter方法.png)

```java
public class demo09 {
	public static void main(String[] args) {
		// 方式一、预定义的标准格式。
		// 如：ISO_LOCAL_DATE_TIME;ISO_LOCAL_DATE;ISO_LOCAL_TIME
		DateTimeFormatter formatterTIME = DateTimeFormatter.ISO_LOCAL_TIME;
		DateTimeFormatter formatterDate = DateTimeFormatter.ISO_LOCAL_DATE;
		DateTimeFormatter formatterTimeDate = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
		// 获取本地日期和时间，创建localDateformatterTime对象
		LocalDateTime localDateTime = LocalDateTime.now();
		System.out.println(localDateTime);
		// 将localDateTime作为参数传入DateTimeFormatter的format()方法
		// 将localDateTime格式化：Date日期 --> 字符串
		String format = formatterTimeDate.format(localDateTime);
		System.out.println(format);
		// 解析，字符串 --> Date日期
		System.out.println(formatterTimeDate.parse("2021-11-10T22:13:24.031"));

		// 方式二、本地化相关的格式。如：ofLocalizedDateTime()
		// FormatStyle.LONG / FormatStyle.MEDIUM / FormatStyle.SHORT
		DateTimeFormatter formatter01 = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.LONG);
		// 格式化：Date日期 --> 字符串
		System.out.println(formatter01.format(localDateTime));
		// 解析，字符串 --> Date日期
		System.out.println(formatter01.parse("2021年11月10日 下午10时31分32秒"));

		// 方式三、自定义的格式。如：ofPattern("yyyy-MM-dd hh:mm:ss")，重点
		DateTimeFormatter formatter02 = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
		// 格式化：Date日期 --> 字符串
		System.out.println(formatter02.format(localDateTime));
		// 解析，字符串 --> Date日期
		System.out.println(formatter02.parse("2021-11-10 22:41:15"));
	}
}
```

### ⑤、其它类

1. `ZoneId`：该类中包含了所有的时区信息，一个时区的 ID，如 `Europe/Paris`
2. `ZonedDateTime`：一个在 ISO-8601 日历系统时区的日期时间，如 `2007-12-03T10:15:30+01:00 Europe/Paris`。其中每个时区都对应着 ID，地区 ID都为 `{区域}/{城市}` 的格式，例如：`Asia/Shanghai` 等
3. `Clock`：使用时区提供对当前即时、日期和时间的访问的时钟。
4. `TemporalAdjuster` : 时间校正器。有时我们可能需要获取例如：将日期调整到“下一个工作日”等操作。
5. `TemporalAdjusters` : 该类通过静态方法 `firstDayOfXxx()/lastDayOfXxx()/nextXxx()` 提供了大量的常用 `TemporalAdjuster` 的实现。
6. 持续时间：`Duration`，用于计算两个“时间”间隔
7. 日期间隔：`Period`，用于计算两个“日期”间隔

```java
// ZoneId:类中包含了所有的时区信息
// ZoneId的getAvailableZoneIds():获取所有的ZoneId
Set<String> zoneIds = ZoneId.getAvailableZoneIds();
for (String s : zoneIds) {
System.out.println(s);
}
// ZoneId的of():获取指定时区的时间
LocalDateTime localDateTime = LocalDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(localDateTime);
// ZonedDateTime:带时区的日期时间
// ZonedDateTime的now():获取本时区的ZonedDateTime对象
ZonedDateTime zonedDateTime = ZonedDateTime.now();
System.out.println(zonedDateTime);
// ZonedDateTime的now(ZoneId id):获取指定时区的ZonedDateTime对象
ZonedDateTime zonedDateTime1 = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(zonedDateTime1);

// Duration:用于计算两个“时间”间隔，以秒和纳秒为基准
LocalTime localTime = LocalTime.now();
LocalTime localTime1 = LocalTime.of(15, 23, 32);
// between():静态方法，返回Duration对象，表示两个时间的间隔
Duration duration = Duration.between(localTime1, localTime);
System.out.println(duration);
System.out.println(duration.getSeconds());
System.out.println(duration.getNano());
LocalDateTime localDateTime = LocalDateTime.of(2016, 6, 12, 15, 23, 32);
LocalDateTime localDateTime1 = LocalDateTime.of(2017, 6, 12, 15, 23, 32);
Duration duration1 = Duration.between(localDateTime1, localDateTime);
System.out.println(duration1.toDays());

// Period:用于计算两个“日期”间隔，以年、月、日衡量
LocalDate localDate = LocalDate.now();
LocalDate localDate1 = LocalDate.of(2028, 3, 18);
Period period = Period.between(localDate, localDate1);
System.out.println(period);
System.out.println(period.getYears());
System.out.println(period.getMonths());
System.out.println(period.getDays());
Period period1 = period.withYears(2);
System.out.println(period1);

// TemporalAdjuster:时间校正器
// 获取当前日期的下一个周日是哪天？
TemporalAdjuster temporalAdjuster = TemporalAdjusters.next(DayOfWeek.SUNDAY);
LocalDateTime localDateTime = LocalDateTime.now().with(temporalAdjuster);
System.out.println(localDateTime);
// 获取下一个工作日是哪天？
LocalDate localDate = LocalDate.now().with(new TemporalAdjuster() {
	@Override
	public Temporal adjustInto(Temporal temporal) {
		LocalDate date = (LocalDate) temporal;
		if (date.getDayOfWeek().equals(DayOfWeek.FRIDAY)) {
			return date.plusDays(3);
		} else if (date.getDayOfWeek().equals(DayOfWeek.SATURDAY)) {
			return date.plusDays(2);
		} else {
			return date.plusDays(1);
		}
	}
});
System.out.println("下一个工作日是：" + localDate);
```

### ⑥、与传统日期处理的转换

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F14、与传统日期处理的转换.png)

## 4、Java 比较器

### ①、介绍

1. 在 Java 中经常会涉及到对象数组的排序问题，那么就涉及到对象之间的比较问题。
2. Java 实现对象排序的方式有两种：
3. 自然排序：`java.lang.Comparable`
4. 定制排序：`java.util.Comparator`

### ②、Comparable 接口

1. `Comparable` 接口强行对实现它的每个类的对象进行整体排序。这种排序被称为类的自然排序。
2. 实现 `Comparable` 的类必须实现 `compareTo(Object obj)` 方法，两个对象即通过 `compareTo(Object obj)` 方法的返回值来比较大小。<font color="red">如果当前对象 this 大于形参对象 obj，则返回正整数，如果当前对象 this 小于形参对象 obj，则返回负整数，如果当前对象 this 等于形参对象 obj，则返回零。</font>
3. 实现 Comparable 接口的对象列表（和数组）可以通过 `Collections.sort` 或 `Arrays.sort` 进行自动排序。实现此接口的对象可以用作有序映射中的键或有序集合中的元素，无需指定比较器。
4. 对于类 C 的每一个 e1 和 e2 来说，当且仅当 `e1.compareTo(e2) == 0 与e1.equals(e2)` 具有相同的 `boolean` 值时，类 C 的自然排序才叫做与 equals 一致。建议（虽然不是必需的）最好使自然排序与 equals 一致。
5. Comparable 的典型实现：(<font color="red">默认都是从小到大排列的</font>)
	1. `String`：按照字符串中字符的Unicode值进行比较
	2. `Character`：按照字符的Unicode值来进行比较
	3. 数值类型对应的包装类以及BigInteger、BigDecimal：按照它们对应的数值大小进行比较
	4. `Boolean`：true 对应的包装类实例大于 false 对应的包装类实例
	5. `Date`、`Time` 等：后面的日期时间比前面的日期时间大

```java
/**
* 一、说明，Java中的对象，正常情况下只能比较： == 或 != ，不能使用 > 或 < 但是在开发场景中，我们需要对多个对象进行排序，言外之意就需要比较对象的大小
*     如何实现？使用两个接口中的任何一个：Comparable或Comparator
* 二、Comparable接口的使用，自然排序
*     1、像String、包装类等实现了Comparable接口，重写了compareTo()方法，给出了比较两个对象大小的方式
*     2、像String、包装类重写compareTo()方法以后进行了从大到小的排列
*     3、重写compareTo()方法的规则：如果当前对象this大于形参对象obj，则返回正整数，如果当前对象this小于形参对象obj，则返回负整数，如果当前对象this等于形参对象obj，则返回零。
*     4、对于自定义类来说，如果需要排序，我们可以让自定义类实现Comparable接口重写compareTo()方法，在compareTo(obj)方法中指明如何进行排序
*/
public class demo01 {
	public static void main(String[] args) {
		// 一、Comparable接口的使用举例

		// 1、字符串等排序
		// 创建一个字符串
		String[] arr = new String[]{"AA","CC","KK","MM","GG","JJ","DD"};
		// 使用Arrays.sort()方法进行排序，Arrays.sort()方法实现了Comparable接口
		Arrays.sort(arr);
		// 打印排序后的结果
		System.out.println(Arrays.toString(arr));

		// 2、类的排序
		// 根据类创建数组
		Goode[] goode = new Goode[5];
		// 给数组赋值
		goode[0] = new Goode("联想",33);
		goode[1] = new Goode("戴尔",44);
		goode[2] = new Goode("小米",11);
		goode[3] = new Goode("华为",66);
		goode[4] = new Goode("微软",66);
		// 使用Arrays.sort()方法进行排序
		Arrays.sort(goode);
		// 打印排序后的结果
		System.out.println(Arrays.toString(goode));

	}
}

// 商品类
// 实现Comparable接口
class Goode implements Comparable {
	private String name;    // 名称
	private double price;   // 价格

	public Goode() { }
	public Goode(String name, double price) { this.name = name;this.price = price; }

	public String getName() { return name; }
	public void setName(String name) { this.name = name; }

	public double getPrice() { return price; }
	public void setPrice(double price) { this.price = price; }

	@Override
	public String toString() {
		return "Goode{" + "name='" + name + '\'' + ", price=" + price + '}';
	}

	// 重写compareTo(Object o)方法，指明商品比较大小的方式，按照价格从低到高排序
	@Override
	public int compareTo(Object o) {
		// 判断o是不是Goode
		if(o instanceof Goode){
			// 对o进行类型的强制转换
			Goode goode = (Goode) o;
			// 方式一：自己重写
			// 判断当前的价格与传入的goode的价格的大小
			if(this.price > goode.price){
				// 当前的价格大，返回值大于0
				return 1;
			}else if(this.price < goode.price){
				// 当前的价格小，返回值小于0
				return -1;
			}else{
				// 价格相等，返回值等于0
				// return 0;
				// 若是价格相等，则比较名称
				return this.name.compareTo(goode.name);
			}
			// 方式二：调用提供的方法
			// return Double.compare(this.price,goode.price);
		}
		// return 0;也可
		throw new RuntimeException("传入的数据类型不一致！");
	}
}
```

```shell
[AA, CC, DD, GG, JJ, KK, MM]
[Goode{name='小米', price=11.0}, Goode{name='联想', price=33.0}, Goode{name='戴尔', price=44.0}, Goode{name='华为', price=66.0}, Goode{name='微软', price=66.0}]

Process finished with exit code 0
```

### ③、Comparator 接口

1. <font color="red">当元素的类型没有实现 java.lang.Comparable 接口而又不方便修改代码，或者实现了 java.lang.Comparable 接口的排序规则不适合当前的操作，那么可以考虑使用 Comparator 的对象来排序</font>，强行对多个对象进行整体排序的比较。
2. 重写 `compare(Object o1,Object o2)` 方法，比较 o1 和 o2 的大小：<font color="red">如果方法返回正整数，则表示 o1 大于 o2；如果返回 0，表示相等；返回负整数，表示 o1 小于 o2。</font>
3. 可以将 `Comparator` 传递给 `sort` 方法（如 `Collections.sort` 或 `Arrays.sort`），从而允许在排序顺序上实现精确控制。
4. 还可以使用 Comparator 来控制某些数据结构（如有序 set或有序映射）的顺序，或者为那些没有自然顺序的对象 collection 提供排序。

```java
/**
* 三、Comparator接口的使用，定制排序
*     1、背景：当元素的类型没有实现java.lang.Comparable接口而又不方便修改代码，或者实现了java.lang.Comparable接口的排序规则不适合当前的操作，那么可以考虑使用 Comparator 的对象来排序
*     2、重写compare(Object o1,Object o2)方法，比较o1和o2的大小：
*        如果方法返回正整数，则表示o1大于o2；如果返回0，表示相等；返回负整数，表示o1小于o2。
*/
public class demo02 {
	public static void main(String[] args) {
		// 一、Comparator接口的使用举例

		// 1、字符串等排序
		// 创建一个字符串
		String[] arr = new String[]{"AA","CC","KK","MM","GG","JJ","DD"};
		// 使用Arrays.sort()方法进行排序，并传入对象Comparator(){}
		// 因为对象Comparator(){}只使用一次，所以创建为匿名对象
		Arrays.sort(arr, new Comparator() {
			@Override
			public int compare(Object o1, Object o2) {
				// 判断o1与o2是不是字符串（String）
				if(o1 instanceof String && o2 instanceof String){
					// 强制类型转换
					String s1 = (String) o1;
					String s2 = (String) o2;
					// 返回从大到小的排序
					// 也可以这样：return s2.compareTo(s1);
					return -s1.compareTo(s2);
				}
				throw new RuntimeException("输入的数据类型不一致！");
			}
		});
		// 打印排序后的结果
		System.out.println(Arrays.toString(arr));

		// 2、类的排序
		// 根据类创建数组
		Goode02[] goode02 = new Goode02[6];
		// 给数组赋值
		goode02[0] = new Goode02("联想",33);
		goode02[1] = new Goode02("戴尔",44);
		goode02[2] = new Goode02("小米",11);
		goode02[3] = new Goode02("华为",66);
		goode02[4] = new Goode02("微软",66);
		goode02[5] = new Goode02("微软",99);
		// 使用Arrays.sort()方法进行排序并传入对象Comparator(){}
		// 因为对象Comparator(){}只使用一次，所以创建为匿名对象
		Arrays.sort(goode02, new Comparator() {
			// 指明商品比较大小的方式，先按照名称从高到低排序，再按照价格从低到高排序
			@Override
			public int compare(Object o1, Object o2) {
				// 判断o1与o2是不是商品（Goode02）
				if(o1 instanceof Goode02 && o2 instanceof Goode02){
					// 强制类型转换
					Goode02 g1 = (Goode02) o1;
					Goode02 g2 = (Goode02) o2;
					// 判断g1与g2的名称是否相等
					if(g1.getName().equals(g2.getName())){
						// 若是相等，则返回价格从小到大的排序
						return Double.compare(g1.getPrice(),g2.getPrice());
					}else {
						// 若是不等，则返回名称从大到小（-）的排序
						return -g1.getName().compareTo(g2.getName());
					}
				}
				throw new RuntimeException("输入的数据类型不一致！");
			}
		});
		// 打印排序后的结果
		System.out.println(Arrays.toString(goode02));
	}
}

// 商品类
// 实现Comparable接口
class Goode02{
	private String name;    // 名称
	private double price;   // 价格

	public Goode02() { }
	public Goode02(String name, double price) { this.name = name;this.price = price; }

	public String getName() { return name; }
	public void setName(String name) { this.name = name; }

	public double getPrice() { return price; }
	public void setPrice(double price) { this.price = price; }

	@Override
	public String toString() {
		return "Goode{" + "name='" + name + '\'' + ", price=" + price + '}';
	}
}
```

```shell
[MM, KK, JJ, GG, DD, CC, AA]
[Goode{name='联想', price=33.0}, Goode{name='戴尔', price=44.0}, Goode{name='微软', price=66.0}, Goode{name='微软', price=99.0}, Goode{name='小米', price=11.0}, Goode{name='华为', price=66.0}]

Process finished with exit code 0
```

### ④、两种方式的对比

1. `Comparable` 接口的方式一旦确定，保证 `Comparable` 接口实现类的对象在任何位置都可以比较大小
2. `Comparator` 接口属于临时性的比较

## 5、System 类

### ①、介绍

1. `System` 类代表系统，系统级的很多属性和控制方法都放置在该类的内部。该类位于 `java.lang` 包。
2. 由于该类的构造器是 `private` 的，所以无法创建该类的对象，也就是无法实例化该类。其内部的成员变量和成员方法都是 `static` 的，所以也可以很方便的进行调用。
3. 成员变量：`System` 类内部包含 `in`、`out` 和 `err` 三个成员变量，分别代表标准输入流(键盘输入)、标准输出流(显示器)和标准错误输出流(显示器)。

### ②、成员方法

1. `native long currentTimeMillis()`：该方法的作用是返回当前的计算机时间，时间的表达格式为当前计算机时间和 GMT 时间(格林威治时间) 1970 年 1 月 1 号 0 时 0 分 0 秒所差的毫秒数。
2. `void exit(int status)`：该方法的作用是退出程序。其中 status 的值为 0 代表正常退出，非零代表异常退出。使用该方法可以在图形界面编程中实现程序的退出功能等。
3. `void gc()`：该方法的作用是请求系统进行垃圾回收。至于系统是否立刻回收，则取决于系统中垃圾回收算法的实现以及系统执行时的情况。
4. `String getProperty(String key)`：该方法的作用是获得系统中属性名为 key 的属性对应的值。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F15、系统中常见方法.png)

```java
public class demo03 {
	public static void main(String[] args) {
		// System类
		// 1、java版本
		String javaVersion = System.getProperty("java.version");
		System.out.println("java的version:" + javaVersion);
		// 2、java的安装路径
		String javaHome = System.getProperty("java.home");
		System.out.println("java的home:" + javaHome);
		// 3、系统的版本名称
		String osName = System.getProperty("os.name");
		System.out.println("os的name:" + osName);
		// 4、系统的版本号
		String osVersion = System.getProperty("os.version");
		System.out.println("os的version:" + osVersion);
		// 5、系统的用户名
		String userName = System.getProperty("user.name");
		System.out.println("user的name:" + userName);
		// 6、系统的用户文件夹路径
		String userHome = System.getProperty("user.home");
		System.out.println("user的home:" + userHome);
		// 7、本项目的路径
		String userDir = System.getProperty("user.dir");
		System.out.println("user的dir:" + userDir);
	}
}
```

## 6、Math 类

1. `java.lang.Math` 提供了一系列静态方法用于科学计算。
2. 其方法的参数和返回值类型一般为 `double` 型。

|方法|作用|
|--|--|
|abs|绝对值|
|acos,asin,atan,cos,sin,tan|三角函数|
|sqrt|平方根|
|pow(double a,doble b)|a的b次幂|
|log|自然对数|
|exp|e为底指数|
|max(double a,double b)|求两个数的最大值|
|min(double a,double b)|求两个数的最小值|
|random()|返回0.0到1.0的随机数|
|long round(double a)|double型数据a转换为long型（四舍五入）|
|toDegrees(double angrad)|弧度—>角度|
|toRadians(double angdeg)|角度—>弧度|

```java
public class demo04 {
	public static void main(String[] args) {
		// 定义变量
		int a = 1;
		int b = 2;
		double c = 3.3d;
		float d = -4.4f;

		// Math一些方法的使用
		// 绝对值
		System.out.println(Math.abs(d));
		// 最大值
		System.out.println(Math.max(a,d));
		// 返回0.0到1.0的随机数
		System.out.println(Math.random());
		// 返回0.0到1.0的随机数，然后乘10
		System.out.println(Math.random() *10 );
	}
}
```

## 7、BigInteger 与 BigDecimal

### ①、BigInteger

1. `Integer` 类作为 `int` 的包装类，能存储的最大整型值为 $2^{31}-1$，Long 类也是有限的，最大为 $2^{63}-1$。如果要表示再大的整数，不管是基本数据类型还是他们的包装类都无能为力，更不用说进行运算了。
2. <font color="red">java.math 包的 BigInteger 可以表示不可变的任意精度的整数（想多长就多长）</font>。BigInteger 提供所有 Java 的基本整数操作符的对应物，并提供 `java.lang.Math` 的所有相关方法。另外，`BigInteger` 还提供以下运算：模算术、GCD 计算、质数测试、素数生成、位操作以及一些其他操作。
3. 构造器：`BigInteger(String val)`：根据字符串构建 BigInteger 对象
4. BigInteger 类常用方法：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F16、BigInteger类常见方法.png)

```java
public class demo05 {
	public static void main(String[] args) {
		// 定义BigInteger类型的变量
		BigInteger b1 = new BigInteger("11111111111111111111111111111111111111");

		// 打印
		System.out.println(b1);
	}
}
----------------结果----------------
11111111111111111111111111111111111111

Process finished with exit code 0
```

### ②、BigDecimal

1. 一般的 Float 类和 Double 类可以用来做科学计算或工程计算，<font color="red">但在商业计算中，要求数字精度比较高，故用到 java.math.BigDecimal 类。</font>
2. `BigDecimal` 类支持不可变的、任意精度的有符号十进制定点数。
3. 构造器
   1. `public BigDecimal(double val)`
   2. `public BigDecimal(String val)`
4. BigDecimal 类常用方法：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F17、BigDecimal类常见方法.png)

```java
public class demo06 {
	public static void main(String[] args) {
		// 定义BigDecimal类型的变量
		BigDecimal b1 = new BigDecimal("22222222222222222222.1111111111");
		BigDecimal b2 = new BigDecimal("11");

		// 打印b1
		System.out.println(b1);
		// 打印b1除b2，(15,BigDecimal.ROUND_UP)为四舍五入至15位
		// 也可以不写，但是如果不能除尽就会报错
		System.out.println(b1.divide(b2,15,BigDecimal.ROUND_UP));
	}
}
```

# 九、枚举类与注解

## 1、枚举类的使用

### ①、如何自定义枚举类

1. 类的对象只有有限个，确定的，称作枚举类。举例如下：
	1. 星期：Monday(星期一)、......、Sunday(星期天)
	2. 性别：Man(男)、Woman(女)
	3. 季节：Spring(春节)......Winter(冬天)
	4. 支付方式：Cash（现金）、WeChatPay（微信）、Alipay(支付宝)、BankCard(银行卡)、CreditCard(信用卡)
	5. 就职状态：Busy、Free、Vocation、Dimission
	6. 订单状态：Nonpayment（未付款）、Paid（已付款）、Delivered（已发货）、Return（退货）、Checked（已确认）Fulfilled（已配货）、
	7. 线程状态：创建、就绪、运行、阻塞、死亡
2. <font color="red">当需要定义一组常量时，强烈建议使用枚举类</font>
3. 枚举类的实现
   1. JDK 1.5 之前需要自定义枚举类
   2. JDK 1.5  新增的<font color="red"> enum 关键字</font>用于定义枚举类
4. 若枚举只有一个对象, 则可以作为一种单例模式的实现方式。
5. 枚举类的属性
   1. 枚举类对象的属性不应允许被改动，所以应该使用 `private final` 修饰
   2. 枚举类的使用 `private final` 修饰的属性应该在构造器中为其赋值
   3. 若枚举类显式的定义了带参数的构造器, 则在列出枚举值时也必须对应的传入参数

```java
/**
* 一、枚举类的使用
*     1、枚举类的理解：类的对象只有有限个，确定的，我们称作枚举类
*     2、当需要定义一组常量时，强烈建议使用枚举类
*     3、如果枚举类中只有一个对象，则可以作为单例模式的实现方式
* 二、如何定义枚举类
*     方式一：jdk5.0之前，自定义枚举类
*     方式二：jdk5，可以使用enum关键字定义枚举类
*/
public class demo01 {
	public static void main(String[] args) {
		// 调用Season类的SPRING对象，并赋值给spring对象
		Season spring = Season.SPRING;
		// 打印spring
		System.out.println(spring);
	}
}

// 自定义枚举类
class Season{
	// 声明Season对象的属性：使用 private final 来修饰
	// 因为类时常量，那么属性也尽量定义成常量
	private final String seasonName;    // 名字
	private final String seasonDesc;    // 描述

	// 1、私有化类的构造器，并给对象的属性赋值
	private Season(String seasonName,String seasonDesc) {
		this.seasonName = seasonName;
		this.seasonDesc = seasonDesc;
	}

	// 3、提供当前枚举类的多个对象：使用 public static final 修饰
	public static final Season SPRING = new Season("春天","春春春春");
	public static final Season SUMMER = new Season("夏天","夏夏夏夏");
	public static final Season AUTUMN = new Season("秋天","秋秋秋秋");
	public static final Season WINTER = new Season("冬天","冬冬冬冬");

	// 4、提供get方法，获取枚举类对象的属性
	public String getSeasonName() { return seasonName; }
	public String getSeasonDesc() { return seasonDesc; }

	// 5、提供toString()方法
	@Override
	public String toString() {
		return "Season{" +
				"seasonName='" + seasonName + '\'' +
				", seasonDesc='" + seasonDesc + '\'' +
				'}';
	}
}
```

### ②、如何使用关键字 enum 定义枚举类

1. 使用 enum 定义的枚举类<font color="red">默认继承</font>了 `java.lang.Enum` 类，因此不能再继承其他类
2. 枚举类的构造器只能使用 `private` 权限修饰符
3. 枚举类的所有实例必须在枚举类中显式列出<font color="red">(, 分隔 ; 结尾)</font>。列出的实例系统会<font color="red">自动添加 public static final 修饰</font>
4. <font color="red">必须在枚举类的第一行声明枚举类对象</font>
5. <font color="red">JDK 1.5 中可以在 switch 表达式中使用Enum定义的枚举类的对象作为表达式, case 子句可以直接使用枚举值的名字, 无需添加枚举类作为限定。</font>

```java
public class demo02 {
	public static void main(String[] args) {
		Season02 spring = Season02.SPRING;
		System.out.println(spring);
	}
}

// 方式二：使用enum关键字定义枚举类
enum Season02{
	// 1、提供当前枚举类的多个对象，多个对象之间用","隔开，末尾";"结束
	SPRING("春天","春春春春"),
	SUMMER("夏天","夏夏夏夏"),
	AUTUMN("秋天","秋秋秋秋"),
	WINTER("冬天","冬冬冬冬");

	// 2、声明Season对象的属性
	private final String seasonName;    // 名字
	private final String seasonDesc;    // 描述

	// 3、私有化类的构造器，并给对象的属性赋值
	private Season02(String seasonName,String seasonDesc) {
		this.seasonName = seasonName;
		this.seasonDesc = seasonDesc;
	}

	// 4、提供get方法，获取枚举类对象的属性
	public String getSeasonName() { return seasonName; }
	public String getSeasonDesc() { return seasonDesc; }

	// 5、enum中一般情况下不在重写toString方法
}
```

### ③、Enum 类的主要方法


1. `values()` 方法：返回枚举类型的对象数组。该方法可以很方便地遍历所有的枚举值。
2. `valueOf(String str)`：可以把一个字符串转为对应的枚举类对象。要求字符串必须是枚举类对象的“名字”。如不是，会有运行时异常：`IllegalArgumentException`。
3. `toString()`：返回当前枚举类对象常量的名称
4. 其他的主要方法：

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F18、Enum类的主要方法.png)

```java
public class demo02 {
	public static void main(String[] args) {
		// 1、values()方法：返回枚举类型的对象数组。
		//    该方法可以很方便地遍历所有的枚举值。
		Season02[] values = Season02.values();
		for (int i = 0; i < values.length; i++) {
			System.out.println(values[i]);
		}

		// 2、valueOf(String str)：返回枚举类中对象名是str的对象
		Season02 winter = Season02.valueOf("WINTER");
		System.out.println(winter);

		// 3、toString()：返回当前枚举类对象常量的名称
		//    默认调用toString()方法
		Season02 spring = Season02.SPRING;
		System.out.println(spring);
	}
}

// 方式二：使用enum关键字定义枚举类
enum Season02{
	// 1、提供当前枚举类的多个对象，多个对象之间用","隔开，末尾";"结束
	SPRING("春天","春春春春"),
	SUMMER("夏天","夏夏夏夏"),
	AUTUMN("秋天","秋秋秋秋"),
	WINTER("冬天","冬冬冬冬");

	// 2、声明Season对象的属性
	private final String seasonName;    // 名字
	private final String seasonDesc;    // 描述

	// 3、私有化类的构造器，并给对象的属性赋值
	private Season02(String seasonName,String seasonDesc) {
		this.seasonName = seasonName;
		this.seasonDesc = seasonDesc;
	}

	// 4、提供get方法，获取枚举类对象的属性
	public String getSeasonName() { return seasonName; }
	public String getSeasonDesc() { return seasonDesc; }

	// 5、enum中一般情况下不在重写toString方法，有需要再写
}
```

### ④、实现接口的枚举类

1. 和普通 Java 类一样，枚举类可以实现一个或多个接口
2. 若每个枚举值在调用实现的接口方法呈现相同的行为方式，则只要统一实现该方法即可。
3. 若需要每个枚举值在调用实现的接口方法呈现出不同的行为方式, 则可以让每个枚举值分别来实现该方法
4. 情况一：实现接口，在 enum 类中实现抽象方法

```java
// 情况一：实现接口，在enum类中实现抽象方法
public class demo02 {
	public static void main(String[] args) {
		// 调用Season02类的SPRING对象，并赋值给spring对象
		Season02 spring = Season02.SPRING;
		// 调用show()方法
		spring.show();
	}
}

// 接口类
interface info{
	public void show();
}

// 使用enum关键字定义枚举类，并实现info接口
enum Season02 implements info{
	// 1、提供当前枚举类的多个对象，多个对象之间用","隔开，末尾";"结束
	SPRING("春天","春春春春"),
	SUMMER("夏天","夏夏夏夏"),
	AUTUMN("秋天","秋秋秋秋"),
	WINTER("冬天","冬冬冬冬");

	// 2、声明Season对象的属性
	private final String seasonName;    // 名字
	private final String seasonDesc;    // 描述

	// 3、私有化类的构造器，并给对象的属性赋值
	private Season02(String seasonName,String seasonDesc) {
		this.seasonName = seasonName;
		this.seasonDesc = seasonDesc;
	}

	// 4、提供get方法，获取枚举类对象的属性
	public String getSeasonName() { return seasonName; }
	public String getSeasonDesc() { return seasonDesc; }

	// 5、enum中一般情况下不在重写toString方法，有需要再写

	// 实现接口的方法
	@Override
	public void show() {
		System.out.println("这是一个季节");
	}
}
```

5. 情况二：让枚举类的对象分别实现接口中的抽象方法

```java
// 情况二：让枚举类的对象分别实现接口中的抽象方法
public class demo03 {
	public static void main(String[] args) {
		// values()方法：返回枚举类型的对象数组。
		//    该方法可以很方便地遍历所有的枚举值。
		Season03[] values = Season03.values();
		for (int i = 0; i < values.length; i++) {
			System.out.println(values[i]);
			values[i].show();
		}
	}
}

// 接口类
interface info{
	public void show();
}

// 使用enum关键字定义枚举类，并实现info接口
enum Season03 implements info{
	// 1、提供当前枚举类的多个对象，多个对象之间用","隔开，末尾";"结束
	//    在每个对象中分别实现接口中的方法
	SPRING("春天","春春春春"){
		@Override
		public void show() {
			System.out.println("春春天");
		}
	},
	SUMMER("夏天","夏夏夏夏"){
		@Override
		public void show() {
			System.out.println("夏夏天");
		}
	},
	AUTUMN("秋天","秋秋秋秋"){
		@Override
		public void show() {
			System.out.println("秋秋天");
		}
	},
	WINTER("冬天","冬冬冬冬"){
		@Override
		public void show() {
			System.out.println("冬冬天");
		}
	};

	// 2、声明Season对象的属性
	private final String seasonName;    // 名字
	private final String seasonDesc;    // 描述

	// 3、私有化类的构造器，并给对象的属性赋值
	private Season03(String seasonName,String seasonDesc) {
		this.seasonName = seasonName;
		this.seasonDesc = seasonDesc;
	}

	// 4、提供get方法，获取枚举类对象的属性
	public String getSeasonName() { return seasonName; }
	public String getSeasonDesc() { return seasonDesc; }

	// 5、enum中一般情况下不在重写toString方法，有需要再写
}
```

## 2、注解的使用

### ①、注解（Annotation）概述

1. 从 JDK 5.0 开始，Java 增加了对元数据(MetaData) 的支持，也就是 <font color="red">Annotation(注解)</font>
2. Annotation 其实就是代码里的<font color="red">特殊标记</font>，这些标记可以在编译、类加载、运行时被读取，并执行相应的处理。通过使用 Annotation, 程序员可以在不改变原有逻辑的情况下, 在源文件中嵌入一些补充信息。代码分析工具、开发工具和部署工具可以通过这些补充信息进行验证或者进行部署。
3. Annotation 可以像修饰符一样被使用，可用于<font color="red">修饰包,类, 构造器, 方法, 成员变量, 参数, 局部变量的声明</font>，这些信息被保存在 Annotation 的 `name=value` 对中。
4. 在 JavaSE 中，注解的使用目的比较简单，例如标记过时的功能，忽略警告等。在 JavaEE/Android 中注解占据了更重要的角色，例如用来配置应用程序的任何切面，代替 JavaEE 旧版中所遗留的繁冗代码和 XML 配置等。
5. 未来的开发模式都是基于注解的，JPA 是基于注解的，Spring2.5 以上都是基于注解的，Hibernate3.x 以后也是基于注解的，现在的 Struts2 有一部分也是基于注解的了，注解是一种趋势，一定程度上可以说：<font color="red">框架 = 注解 + 反射 + 设计模式</font>。

### ②、常见的 Annotation 示例

1. 使用 Annotation 时要在其前面增加 `@` 符号, 并把该 Annotation 当成一个修饰符使用。用于修饰它支持的程序元素
2. 示例一：生成文档相关的注解

|注解|作用|
|--|--|
|@author|标明开发该类模块的作者，多个作者之间使用","分割|
|@version|标明该类模块的版本|
|@see|参考转向，也就是相关主题|
|@since|从哪个版本开始增加的|
|@param|对方法中某参数的说明，如果没有参数就不能写|
|@return|对方法返回值的说明，如果方法的返回值类型是void就不能写|
|@exception|对方法可能抛出的异常进行说明 ，如果方法没有用throws显式抛出的异常就不能写其中|
|注解|<font color="red">格式要求</font>|
|@param @return 和 @exception|这三个标记都是只用于方法的。|
|@param的格式要求|@param 形参名 形参类型 形参说明|
|@return 的格式要求|@return 返回值类型 返回值说明|
|@exception的格式要求|@exception 异常类型 异常说明|
|@param和@exception|可以并列多个|

```java
package com.annotation.javadoc;
/**
* @author shkstart
* @version 1.0
* @see Math.java
*/
public class JavadocTest {
	/**
	* 程序的主方法，程序的入口
	* @param args String[] 命令行参数
	*/
	public static void main(String[] args) {

	}
	/**
	* 求圆面积的方法
	* @param radius double 半径值
	* @return double 圆的面积
	*/
	public static double getArea(double radius){
		return Math.PI * radius * radius;
	}
}
```

3. 示例二：在编译时进行格式检查(JDK内置的三个基本注解)

|注解|作用|
|--|--|
|@Override|限定重写父类方法, 该注解只能用于方法|
|@Deprecated|用于表示所修饰的元素(类, 方法等)已过时。通常是因为所修饰的结构危险或存在更好的选择|
|@SuppressWarnings|抑制编译器警告|

```java
package com.annotation.javadoc;

public class AnnotationTest{
	public static void main(String[] args) {
		@SuppressWarnings("unused")
		int a = 10;
	}

	@Deprecated
	public void print(){
		System.out.println("过时的方法");
	}

	@Override
	public String toString() {
		return "重写的toString方法()";
	}
}
```

4. 示例三：跟踪代码依赖性，实现替代配置文件功能：

- Servlet3.0提供了注解(annotation),使得不再需要在web.xml文件中进行Servlet的部署。

```java
@WebServlet("/login")
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	} 
}
```
```java
<servlet>
	<servlet-name>LoginServlet</servlet-name>
	<servlet-class>com.servlet.LoginServlet</servlet-class>
</servlet>

<servlet-mapping>
	<servlet-name>LoginServlet</servlet-name>
	<url-pattern>/login</url-pattern>
</servlet-mapping>
```

- spring框架中关于“事务”的管理

```java
@Transactional(propagation=Propagation.REQUIRES_NEW,isolation=Isolation.READ_COMMITTED,readOnly=false,timeout=3)
public void buyBook(String username, String isbn) {
	//1.查询书的单价
	int price = bookShopDao.findBookPriceByIsbn(isbn);
	//2. 更新库存
	bookShopDao.updateBookStock(isbn);
	//3. 更新用户的余额
	bookShopDao.updateUserAccount(username, price);
}
```
```java
<!-- 配置事务属性 -->
<tx:advice transaction-manager="dataSourceTransactionManager" id="txAdvice">
	<tx:attributes>
		<!-- 配置每个方法使用的事务属性 -->
		<tx:method name="buyBook" propagation="REQUIRES_NEW" isolation="READ_COMMITTED" read-only="false" timeout="3" />
	</tx:attributes>
</tx:advice>
```

### ③、自定义 Annotation

1. 定义新的 Annotation 类型使用 <font color="red">@interface</font> 关键字
2. 自定义注解自动继承了<font color="red">java.lang.annotation.Annotation接口</font>
3. Annotation 的成员变量在 Annotation 定义中以无参数方法的形式来声明。其方法名和返回值定义了该成员的名字和类型。我们称为配置参数。类型只能是。<font color="red">八种基本数据类型、String 类型、Class 类型、enum 类型、Annotation 类型、及以上所有类型的数组</font>
4. 可以在定义 Annotation 的成员变量时为其指定初始值, 指定成员变量的初始值可使用 <font color="red">default 关键字</font>
5. 如果只有一个参数成员，建议使用<font color="red">参数名为 value</font>
6. 如果定义的注解含有配置参数，那么使用时必须指定参数值，除非它有默认值。格式是 `参数名 = 参数值`，如果只有一个参数成员，且名称为value，可以省略 `value=`
7. 没有成员定义的 Annotation 称为<font color="red">标记</font>；包含成员变量的 Annotation 称为元数据 Annotation
8. 注意：<font color="red">自定义注解必须配上注解的信息处理流程才有意义。</font>

```java
/**
* 自定义注解
*    1、注解声明为：@interface
*    2、内部定义成员，通常使用value表示、
*    3、可以指定成员的默认值，使用default定义
*    4、如果自定义的注解没有成员，表明是一个标识作用
* 如果注解有成员，在使用主机时，需要指明成员的值
* 注意：自定义注解必须配上注解的信息处理流程才有意义。
*      自定义注解通常都会指明两个元注解：Retention、Target
*/

// 实现类
// 使用注解
@MyAnnotation(value = "hell")
public class demo01{
	@MyAnnotation
	public static void main(String[] args) {

	}
}

// 自定义注解
// 声明为RUNTIME生命周期
@Retention(RetentionPolicy.SOURCE)
@interface MyAnnotation {
	String value() default "hello" ;
}
```

### ④、JDK 提供的 4 中的元注解

#### Ⅰ、介绍

1. JDK 的元 Annotation 用于修饰其他 Annotation 定义，修饰注解的注解
2. 元注解的理解：对现有的注解进行解释说明的注解
3. 元数据的理解：对现有的数据进行解释说明的数据
4. JDK5.0 提供了 4 个标准的 `meta-annotation` 类型，分别是：

|元注解|作用|
|--|--|
|Retention|指定所修饰的 Annotation 的生命周期：<br/>SOURCE\CLASS（默认行为）\RUNTIME<br/>只有声明为RUNTIME生命周期的注解，才能通过反射获取
|Target|用于指定被修饰的 Annotation 能用于修饰哪些元素
|Documented|表示所修饰的注解再被Javadoc解析时，保留下来
|Inherited|被它修饰的 Annotation 将具有继承性

#### Ⅱ、@Retention

1. <font color="red">@Retention</font>: 只能用于修饰一个 Annotation 定义, 用于指定该 Annotation 的生命周期，@Rentention 包含一个 <font color="red">RetentionPolicy</font> 类型的成员变量, 使用@Rentention 时必须为该 value 成员变量指定值:
2. <font color="red">RetentionPolicy.SOURCE</font>:在源文件中有效（即源文件保留），编译器直接丢弃这种策略的注释
3. <font color="red">RetentionPolicy.CLASS</font>:在class文件中有效（即class保留），当运行 Java 程序时, JVM 不会保留注解。 这是默认值
4. <font color="red">RetentionPolicy.RUNTIME</font>:在运行时有效（即运行时保留），当运行 Java 程序时, JVM 会保留注释。<font color="red">程序可以通过反射获取该注释</font>。

```java
@Retention(RetentionPolicy.SOURCE)
@interface MyAnnotation1{ }
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation2{ }
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F19、JDK%20中的元注解@Retention.png)

#### Ⅲ、@Target

1. `@Target`: 用于修饰 Annotation 定义, 用于指定被修饰的 Annotation 能用于修饰哪些程序元素。 
2. `@Target` 也包含一个名为 value 的成员变量。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F20、JDK%20中的元注解@Target.png)

#### Ⅳ、@Documented

1. `@Documented`：用于指定被该元 Annotation 修饰的 Annotation 类将被javadoc 工具提取成文档。默认情况下，javadoc 是不包括注解的。
2. 定义为 Documented 的注解必须设置 Retention 值为 RUNTIME。

#### Ⅴ、@Inherited

1. `@Inherited`: 被它修饰的 Annotation 将具有继承性。如果某个类使用了被 `@Inherited` 修饰的 Annotation，则其子类将自动具有该注解。
2. 比如：如果把标有 `@Inherited` 注解的自定义的注解标注在类级别上，子类则可以继承父类类级别的注解
3. 实际应用中，使用较少

### ⑤、利用反射获取注解信息（在反射部分涉及）

1. JDK 5.0 在 `java.lang.reflect` 包下新增了 AnnotatedElement 接口，该接口代表程序中可以接受注解的程序元素
2. 当一个 Annotation 类型被定义为运行时 Annotation 后，该注解才是运行时可见，当 class 文件被载入时保存在 class 文件中的 Annotation 才会被虚拟机读取
3. 程序可以调用 AnnotatedElement 对象的如下方法来访问 Annotation 信息

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F21、利用反射获取注解信息.png)

### ⑥、JDK 8 中注解的新特性

1. Java 8 对注解处理提供了两点改进：<font color="red">可重复的注解及可用于类型的注解</font>。此外，反射也得到了加强，在 Java8 中能够得到方法参数的名称。这会简化标注在方法参数上的注解。
2. **可重复注解：**
	1. 在 MyAnnotation 上声明 `@Repeatable`，成员值为 `MyAnnotation.class`
	2. MyAnnotation 的 Target 和 Retention 和 MyAnnotation 相同
3. 可重复注解示例：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F22、可重复注解示例.png)

4. **类型注解：** JDK1.8 之后，关于元注解 `@Target` 的参数类型 ElementType 枚举值多了两个：TYPE_PARAMETER和TYPE_USE。
5. 在 Java 8 之前，注解只能是在声明的地方所使用，Java8 开始，注解可以应用在任何地方。
6. 新加的元注解 `@Target` 的参数类型 ElementType 的枚举值：

| 参数                         | 作用                         |
| -------------------------- | -------------------------- |
| ElementType.TYPE_PARAMETER | 表示该注解能写在类型变量的声明语句中（如：泛型声明） |
| ElementType.TYPE_USE       | 表示该注解能写在使用类型的任何语句中         |

# 十、集合

## 1、Java 集合框架概述

1. 一方面， 面向对象语言对事物的体现都是以对象的形式，为了方便对多个对象的操作，就要对对象进行存储。
2. 另一方面，使用 Array 存储对象方面具有<font color="red">一些弊端</font>，而 Java 集合就像一种容器，可以<font color="red">动态</font>地把多个对象的引用放入容器中。
3. **数组在内存存储方面的特点：**
	1. 数组初始化以后，长度就确定了。
	2. 数组声明的类型，就决定了进行元素初始化时的类型
4. **数组在存储数据方面的弊端：**
	1. 数组初始化以后，长度就不可变了，不便于扩展
	2. 数组中提供的属性和方法少，不便于进行添加、删除、插入等操作，且效率不高。
	3. 无法直接获取存储元素的个数，没有现成的属性或方法可用
	4. 数组存储的数据是有序的、可以重复的。也可以说是：---->存储数据的特点单一
5. Java 集合类可以用于存储数量不等的多个<font color="red">对象</font>，还可用于保存具有映射关系的关联数组。
6. 集合、数组都是对多个数据进行储存操作的结构，简称java容器：此时的储存，主要指的是内存层面的存储，不涉及到持久化的存储（.txt、.jpg、avi、数据库等）
7. 集合的使用场景

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F23、集合的使用场景.png)

7. Java 集合可分为 **Collection** 和 **Map** 两种体系
8.  **Collection接口**：单列数据，定义了存取一组对象的方法的集合
	1. List：储存有序、可重复的集合 --> “动态”数组；**实现类：ArryList、LinkedList、Vector**
	1. Set： 储存无序、不可重复的集合 --> 类似高中数学的“集合”；**实现类：HashSet、LinkedHashSet、TreeSet**
9.  Collection 接口继承树

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F25、Collection接口继承树.png)

10. **Map接口**：双列数据，保存具有映射关系“key-value对”的集合 --> 高中函数：y = f(x)
	1. 类似高中函数：y = f(x)，有一对一、一对多的关系；**实现类：HashMap、LinkedHashMap、TreeMap、Hashtable、Properties**
11. Map 接口继承树

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F26、Map接口继承树.png)

## 2、Collection 接口方法

### ①、Collection 接口概述

1. Collection 接口是 List、Set 和 Queue 接口的父接口，该接口里定义的方法既可用于操作 Set 集合，也可用于操作 List 和 Queue 集合。
2. JDK 不提供此接口的任何直接实现，而是提供更具体的子接口（如：Set 和 List）实现。
3. 在 Java5 之前，Java 集合会丢失容器中所有对象的数据类型，把所有对象都当成 Object 类型处理；从 JDK 5.0 增加了泛型以后，Java 集合可以记住容器中对象的数据类型。
4. 向 Collection 接口的实现类的对象中添加数据 ob 时，要求 obj 所在类要重写 equals() 方法
5. Collection 接口方法：

|序号|方法|作用|
|--|--|--|
|1|add(Object obj)<br/>addAll(Collection coll)|添加|
|2|int size()|获取集合中有效元素的个数|
|3|void clear()|清空集合|
|4|boolean isEmpty()|判断集合是否是空集合|
|5|boolean retainAll(Collection c)|取两个集合的交集，把交集的结果存在当前集合中，不影响c|
|6|boolean equals(Object obj)|集合是否相等|
|7|Object[] toArray()|转成对象数组|
|8|hashCode()|获取集合对象的哈希值|
|9||**判断当前集合是否包含某个元素**|
||boolean contains(Object obj)|通过调用obj对象所在类的equals()方法来判断是否是同一个对象|
||boolean containsAll(Collection c)|也是调用元素的equals方法来比较的。拿两个集合的元素挨个比较。|
|10||**删除**|
||boolean remove(Object obj)|通过元素的equals方法判断是否是要删除的那个元素。只会删除找到的第一个元素|
||boolean removeAll(Collection coll)|取当前集合的差集|
|11|iterator()|遍历，返回迭代器对象，用于集合遍历|

```java
// 实现类
public class demo01 {
  public static void main(String[] args) {
	 // 通过Collection创建ArrayList()的对象，多态，向上转型
	 Collection coll = new ArrayList();

	 // 1.1、add(Object obj)，将元素添加到集合coll中
	 coll.add(123);// 自动装箱
	 coll.add("AA");
	 coll.add(new String("BB"));
	 coll.add(true);
	 coll.add(false);
	 coll.add(new Date());
	 coll.add(new Person("月海",16));
	 Person p = new Person("言",18);
	 coll.add(p);
	 // 打印集合中的元素
	 System.out.println(coll);

	 // 1.2、addAll(Collection coll)
	 //    将coll集合中的元素添加到当前的集合中
	 Collection coll02 = new ArrayList();
	 coll02.add("CC");
	 coll02.add(456);
	 coll02.addAll(coll);
	 // 打印集合中的元素
	 System.out.println(coll02);

	 // 2、int size()，获取添加的元素的个数
	 System.out.println(coll.size());  // 8
	 System.out.println(coll02.size());// 10

	 // 3、void clear()，清空集合
	 coll02.clear();

	 // 4、boolean isEmpty()，判断集合是否是空集合
	 //    判断集合中是否有元素
	 System.out.println(coll02.isEmpty());// true

	 // 5、boolean retainAll(Collection c)
	 // 取两个集合的交集，获取当前集合和c集合的交集，并返回给当前集合
	 // 把交集的结果存在当前集合中，不影响，保留一样的，删除不一样的
	 Collection c03 = Arrays.asList(new Person("言",18),"AA",true,123456,"PP");
	 coll.retainAll(c03);
	 System.out.println(coll);

	 // 6、boolean equals(Object obj)，比较集合是否相等
	 //    两个集合完全一样才会返回true
	 // 注意：因为ArrayList是有序的，所以就算元素相同，如果顺序不同也会返回flast
	 System.out.println(coll.equals(c03));

	 // 7、Object[] toArray()，将集合转成对象数组
	 Object[] array = coll.toArray();
	 for (int i = 0; i < array.length; i++) {
		   System.out.println(array[i]);
	 }

	 // 8、hashCode()，获取集合对象的哈希值
	 System.out.println(coll.hashCode());

	 // 9.1、boolean contains(Object obj)：
	 //    判断当前集合是否包含obj
	 //    通过调用obj对象所在类的equals方法来判断是否是同一个对象
	 System.out.println(coll.contains(123));// true
	 System.out.println(coll.contains("AA"));// true
	 System.out.println(coll.contains(new String("BB")));// true
	 System.out.println(coll.contains(new Person("月海",16)));// true
	 System.out.println(coll.contains(new Person("言",18)));// true

	 // 9.2、boolean containsAll(Collection c)
	 //    判断形参c中的所有元素是否都存在于当前集合中
	 //    也是调用元素的equals方法来比较的。拿两个集合的元素挨个比较。
	 Collection c = Arrays.asList("月海",16,123);
	 System.out.println(coll.containsAll(coll));// true

	 // 10.1、boolean remove(Object obj)
	 //     通过元素的equals方法判断是否是要删除的那个元素。
	 //     只会删除找到的第一个元素
	 coll.remove(123);
	 System.out.println(coll);

	 // 10.2、boolean removeAll(Collection coll)，取当前集合的差集
	 //      从当前集合中移除coll中所有的元素
	 Collection c02 = Arrays.asList(new Person("月海",16),123456);
	 coll.removeAll(c02);
	 System.out.println(coll);

	 // 11、iterator()返回迭代器对象，用于集合遍历
	 //     返回迭代器terator接口的实例，用于遍历集合元素
	 //     在三、Iterator迭代器接口中详细说明

	 // 拓展：将数组转成集合：调用Arrays类的静态方法asList()

	 System.out.println("----------------------");

	 String[] arr = new String[]{"AA","BB","CC"};
	 List<String> list = Arrays.asList(arr);
	 System.out.println(list);

	 int[] arr01 = new int[] {1,2,3,4,11,67,890};
	 // 这种写法程序认为是一个元素，打印出来是地址值
	 List list01 = Arrays.asList(arr01);
	 System.out.println(list01);
	 // 这种写法程序可以分辩出来字符串
	 List list02 = Arrays.asList(1,2,3,4,11,67,890);
	 System.out.println(list02);
	 // 这种写法程序可以分辩出来数组，包装类的对象
	 Integer[] arr02 = new Integer[]{33,44,66,123456};
	 List list03 = Arrays.asList(arr02);
	 System.out.println(list03);
  }
}

// po类
class Person{
  private String name;
  private int age;

  public Person() { }
  public Person(String name, int age) { this.name = name;this.age = age; }

  public String getName() { return name; }
  public void setName(String name) { this.name = name; }

  public int getAge() { return age; }
  public void setAge(int age) { this.age = age; }

  @Override
  public String toString() {
	 return "Person{" +
			  "name='" + name + '\'' +
			  ", age=" + age +
			  '}';
  }

  // 重写的equals方法，可以使得集合的contains方法比较时比较其内容
  @Override
  public boolean equals(Object o) {
	 if (this == o) return true;
	 if (o == null || getClass() != o.getClass()) return false;
	 Person person = (Person) o;
	 return age == person.age &&
			  Objects.equals(name, person.name);
  }

//    @Override
//    public int hashCode() {
//        return Objects.hash(name, age);
//    }
}
```

### ②、Iterator 迭代器接口

1. Iterator 对象称为迭代器(设计模式的一种)，主要用于遍历 Collection 集合中的元素。
2. <font color="red">GOF 给迭代器模式的定义为：提供一种方法访问一个容器(container)对象中各个元素，而又不需暴露该对象的内部细节。迭代器模式，就是为容器而生。</font>类似于“公交车上的售票员”、“火车上的乘务员”、“空姐”。
3. Collection 接口继承了 `java.lang.Iterable` 接口，该接口有一个 `iterator()` 方法，那么所有实现了 Collection 接口的集合类都有一个 `iterator()` 方法，用以返回一个实现了 Iterator 接口的对象。
4. Iterator 仅用于遍历集合，Iterator 本身并不提供承装对象的能力。如果需要创建 Iterator 对象，则必须有一个被迭代的集合。
5. 集合对象每次调用 `iterator()` 方法都得到一个全新的迭代器对象，默认游标都在集合的第一个元素之前。
#### Ⅰ、Iterator 接口的 hasNext() 和 next() 方法

1. Iterator 接口的方法

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F27、Iterator接口的方法.png)

```java
/**
* 集合元素的遍历操作，使用迭代Iterator接口
* 内部的方法：hasNext() 和 next()
* 每调用一次iterator.next()方法指针下移一次
*/
public class demo02 {
  public static void main(String[] args) {
	 // 通过Collection创建ArrayList()的对象，多态，向上转型
	 Collection coll = new ArrayList();

	 // 添加元素
	 coll.add(123);
	 coll.add(456);
	 coll.add("AA");
	 coll.add("BB");
	 coll.add(new Date());

	 // 通过集合的iterator()方法创建迭代器对象
	 Iterator iterator = coll.iterator();

	 // 方式一：不推荐
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());

	 // 方式二：不推荐
//        for (int i = 0; i < coll.size(); i++) {
//            System.out.println(iterator.next());
//        }

	 // 方式三：推荐
	 // 判断是否还有下一个元素
	 // 每调用一次iterator.next()方法指针下移一次
	 while (iterator.hasNext()){
		//next():①指针下移 ②将下移以后集合位置上的元素返回
		System.out.println(iterator.next());
	 }
  }
}
```

```java
// 错误方式一：会跳着输出，因为判断时调用了一次iterator.Next()方法之后
//            指针下移了一次，到输出时输出的是第二个元素
Iterator iterator = coll.iterator();
while (iterator.Next() != NULL){
  System.out.println(iterator.next());
}

// 错误方式二：会一直输出第一个元素。因为每次循环时都会重新创建对象
while (coll.iterator().hasNext()){
  System.out.println(iterator.next());
}
```

2. 迭代器的执行原理

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F28、迭代器的执行原理.png)

#### Ⅱ、Iterator 接口 emove() 方法

1. 可以在遍历的时候，删除集合中的元素，此方法不同于集合中直接调用 `remove()`
2. **注意：**
	1.  Iterator 可以删除集合的元素，但是是遍历过程中通过迭代器对象的 remove 方法，不是集合对象的 remove 方法。
	2.  <font color="red">如果还未调用 next() 或在上一次调用 next 方法之后已经调用了 remove 方法，再调用 remove 都会报IllegalStateException。</font>
```java
public class demo03 {
 public static void main(String[] args) {
	Collection coll = new ArrayList();

	// 添加元素
	coll.add(123);
	coll.add(456);
	coll.add("AA");
	coll.add("BB");
	coll.add(new Date());

	// 通过集合的iterator()方法创建迭代器对象
	Iterator iterator = coll.iterator();

	// 遍历迭代器
	while (iterator.hasNext()){
		  // 将迭代器元素赋值给next对象
		  Object next = iterator.next();
		  // 判断next元素是否与123相等，相等就删掉
		  if(next.equals(123)){
			 iterator.remove();
		  }
	}

	// 重新获取iterator对象，将指针移到最上面
	iterator = coll.iterator();
	// 遍历迭代器
	while (iterator.hasNext()){
		  System.out.println(iterator.next());
	}
 }
}
```

#### Ⅲ、使用 foreach 循环遍历集合元素

1. Java 5.0 提供了 foreach 循环迭代访问 Collection 和数组。
2. 遍历操作不需获取 Collection 或数组的长度，无需使用索引访问元素。
3. 遍历集合的底层调用 Iterator 完成操作。
4. foreach 还可以用来遍历数组。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F29、使用foreach循环遍历集合元素.png)

```java
public class demo04 {
  public static void main(String[] args) {
	 Collection coll = new ArrayList();
	 // 添加元素
	 coll.add(123);
	 coll.add(456);
	 coll.add("AA");
	 coll.add("BB");
	 coll.add(new Date());

	 // 遍历集合
	 // for( 集合元素的类型 局部自定义变量 ： 集合对象 )
	 for(Object obj : coll){
		   System.out.println(obj);
	 }

	 // 遍历数组
	 int[] arr = new int[]{1,2,3,4,5};
	 for (int i : arr){
		   System.out.println(i);
	 }
  }
}
```

### ③、Collection 子接口一：List

#### Ⅰ、List 接口概述

1. 鉴于 Java 中数组用来存储数据的局限性，我们通常使用 List 替代数组
2. List 集合类中<font color="red">元素有序、且可重复</font>，集合中的每个元素都有其对应的顺序索引。
3. List 容器中的元素都对应一个整数型的序号记载其在容器中的位置，可以根据序号存取容器中的元素。
4. JDK API 中 List 接口的实现类常用的有：<font color="red">ArrayList、LinkedList 和 Vector。</font>

#### Ⅱ、List 实现类之一：ArrayList

##### （1）、ArrayList 说明

1. <font color="red">对于频繁查询元素的操作，建议使用 ArrayList 类，效率较高，因为是顺序表（数组）的存储方式</font>
2. ArrayList 是 List 接口的典型实现类、主要实现类，<font color="red">线程不安全，效率高</font>
3. 本质上，ArrayList是对象引用的一个“变长”数组，底层使用Object[] elementData 存储
4. `Arrays.asList(…)` 方法返回的 List 集合，既不是 ArrayList 实例，也不是 Vector 实例。 `Arrays.asList(…)` 返回值是一个固定长度的 List 集合

##### （2）、ArrayList 的 JDK1.8 之前与之后的实现区别？

1. JDK1.7：
	1. ArrayList 像饿汉式，直接创建一个初始容量为 10 的 `Object[] elementData` 数组。
	2. 添加数据时，如果此次的添加导致底层 elementData 数组的容量不够，则扩容。默认情况下，扩容为原来容量的 1.5 倍，同时需要将原有数组中的数据复制到新的数组中
	3. 结论：建议开发中使用带参的构造器：`ArrayList list = new ArrayList(int capacity)` 来规定数组初始长度，尽量避免自动扩容
2. JDK1.8：
	1. ArrayList 像懒汉式，一开始创建一个长度为 0 的 `Object[] elementData` 数组，初始化为：`{}`
	2. 当添加第一个元素时再创建一个始容量为 10 的数组，即第一次调用 `list.add()` 方法时
	3. 后续的添加和扩容与 jdk7 一致

#### Ⅲ、List 实现类之二：LinkedList

1. <font color="red">对于频繁的插入或删除元素的操作，建议使用 LinkedList 类，效率较高，因为是双向链表的存储方式</font>
2. 底层使用双向链表存储，内部没有声明数组，而是定义了 Node 类型的 first 和 last，用于记录首末元素。同时，定义内部类 Node，作为 LinkedList 中保存数据的基本结构。Node 除了保存数据，还定义了两个变量：
   1. `prev` 变量记录前一个元素的位置
   2. `next` 变量记录下一个元素的位置

```java
private static class Node<E> {
	E item;
	Node<E> next;
	Node<E> prev;
	
	Node(Node<E> prev, E element, Node<E> next) {
		this.item = element;
		this.next = next;
		this.prev = prev;
	}
}
```

#### Ⅳ、List 实现类之三：Vector

1. `Vector` 是一个古老的集合，JDK1.0 就有了。大多数操作与 ArrayList 相同，<font color="red">区别之处在于 Vector 是线程安全的，所以效率低。</font>
2. 在各种 list 中，最好把 `ArrayList` 作为缺省选择。当插入、删除频繁时，使用 `LinkedList`；`Vector` 总是比 `ArrayList` 慢，所以尽量<font color="red">避免使用</font>。
3. 本质上也是对象引用的一个“变长”数组，底层使用 `Object[] elementData` 存储
4. 通过 `Vector()` 构造器创建对象时，底层都创建了长度为 10 数组；在扩容方面，默认扩容为原来的数组长度的 2 倍

#### Ⅴ、三种实现方式的异同

1. 相同点：三个类都是实现了 List 接口，存储数据的特点相同：存储有序的、可重复的数据
2. **ArrayList 和 LinkedList 的异同**
	1. 二者都线程不安全，相对线程安全的 Vector，执行效率高。
	2. 此外，`ArrayList` 是实现了基于动态数组的数据结构，`LinkedList` 基于链表的数据结构。对于随机访问 `get` 和 `set`，`ArrayList` 觉得优于 `LinkedList`，因为 `LinkedList` 要移动指针。
	3. 对于新增和删除操作 `add` (特指插入) 和 `remove`，`LinkedList` 比较占优势，因为ArrayList要移动数据。
3. **ArrayList 和 Vector 的区别**
	1. `Vector` 和 `ArrayList` 几乎是完全相同的，唯一的区别在于 `Vector` 是同步类(synchronized)，属于强同步类。因此开销就比 `ArrayList` 要大，访问要慢。
	2. 正常情况下，大多数的 Java 程序员使用 `ArrayList` 而不是 `Vector`，因为同步完全可以由程序员自己来控制。`Vector` 每次扩容请求其大小的 2 倍空间，而 `ArrayList` 是 1.5 倍。`Vector` 还有一个子类 `Stack

#### Ⅵ、List 接口方法

1. List 除了从 Collection 集合<font color="red">继承的方法外</font>，List 集合里添加了一些根据索引来操作集合元素的方法。

| 方法                                         | 作用                             |
| ------------------------------------------ | ------------------------------ |
| void add(int index, Object ele)            | 在 index 位置插入 ele 元素            |
| boolean addAll(int index, Collection eles) | 从 index 位置开始将 eles 中的所有元素添加进来  |
| Object get(int index)                      | 获取指定 index 位置的元素               |
| int indexOf(Object obj)                    | 返回 obj 在集合中首次出现的位置             |
| int lastIndexOf(Object obj)                | 返回 obj 在当前集合中末次出现的位置           |
| Object remove(int index)                   | 移除指定 index 位置的元素，并返回此元素        |
| Object set(int index, Object ele)          | 设置指定 index 位置的元素为 ele          |
| List subList(int fromIndex, int toIndex)   | 返回从 fromIndex 到 toIndex 位置的子集合 |

2. 总结：常用方法
	1. 增：add(Object ele)
	2. 删：remove(int index)、remove(Object 0)
	3. 改：set(int index, Object ele)
	4. 查：get(int index)
	5. 插：add(int index, Object ele)
	6. 长度：size()
	7. 遍历：
		1. Iterator迭代器
		2. 增强for循环
		3. 普通的循环

```java
public class demo01 {
	public static void main(String[] args) {
		ArrayList list = new ArrayList();
		
		list.add(123);
		list.add(456);
		list.add("AA");
		list.add("BB");
		System.out.println(list);
		
		// 1、void add(int index, Object ele):在index位置插入ele元素
		//    元素从0开始
		list.add(2,"DD");
		System.out.println(list);
		
		// 2、boolean addAll(int index, Collection eles)
		//    从index位置开始将eles中的所有元素添加进来
		List<Integer> asList = Arrays.asList(99, 999);
		list.addAll(2,asList);
		System.out.println(list);
		
		// 3、Object get(int index):获取指定index位置的元素
		System.out.println(list.get(2));
		
		// 4、int indexOf(Object obj):返回obj在集合中首次出现的位置
		//    如果不存在返回-1
		System.out.println(list.indexOf(999));
		
		// 5、int lastIndexOf(Object obj):返回obj在当前集合中末次出现的位置
		//    从后往前查，但是返回的数是从前往后的顺序，如果不存在返回-1
		System.out.println(list.lastIndexOf(999));
		
		// 6、Object remove(int index):移除指定index位置的元素，并返回此元素
		System.out.println(list.remove(2));
		System.out.println(list);
		// 6.2、Object remove(Object o):移除指定的元素，并返回true或false
		System.out.println(list.remove("AA"));
		System.out.println(list);
		// 6.3、如果集合中2的位置有元素，而又要移除数字2，
		//      直接list.remove(2)的话移除的是位置2上的元素
		//  故，可以这样写
		list.remove(new Integer(2));
		
		// 7、Object set(int index, Object ele):设置指定index位置的元素为ele
		//    返回被修改的元素
		System.out.println(list.set(1, 789));
		System.out.println(list);
		
		// 8、List subList(int fromIndex, int toIndex)
		// 返回从fromIndex到toIndex位置的子集合，左闭右开
		System.out.println(list.subList(2, 5));
		
		// 9、遍历
		System.out.println("----------------------------------");
		// 9.1、Iterator迭代器
		Iterator iterator = list.iterator();
		while (iterator.hasNext()){
			System.out.println(iterator.next());
		}
		
		System.out.println("----------------------------------");
		
		// 9.2、增强for循环
		for(Object obj : list){
			System.out.println(obj);
		}
		
		System.out.println("----------------------------------");
		
		// 9.3、普通的循环
		for (int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i));
		}
	}
}
```

### ④、Collection 子接口二：Set

#### Ⅰ、Set 接口概述

1. `Set` 接口是 `Collection` 的子接口，set 接口没有提供额外的方法
2. `Set` 集合不允许包含相同的元素，如果试把两个相同的元素加入同一个 Set 集合中，则添加操作失败。
3. `Set` 判断两个对象是否相同不是使用 `==` 运算符，而是根据 `equals()` 方法
4. 对于存放在 Set 容器中的对象，<font color="red">对应的类一定要重写 equals() 和 hashCode(Object obj) 方法，以实现对象相等规则。</font>
5. <font color="red">重写的 equals() 和 hashCode(Object obj) 方法要尽可能保持一致性：相等的对象必须具有相等的散列码</font>
6. 每创建一个 Set 集合就时创建了一个 Map 集合，向 Set 中添加的元素就是添加到了 Map 的 key 中

#### Ⅱ、Set 实现类之一：HashSet

##### （1）、介绍

1. `HashSet` 是 `Set` 接口的<font color="red">典型实现，大多数时候使用 Set 集合时都使用这个实现类</font>。底层是：数组+链表
2. `HashSet` 按 `Hash` 算法来存储集合中的元素，因此具有很好的存取、查找、删除性能。
3. <font color="red">HashSet 具有以下特点：</font>
	1. 无序性：不等于随机性，存储的数据在底层数组中并非按照数组索引的顺序添加，而是根据数据的哈希值（不能保证元素的排列顺序）
	2. 不可重复性：保证添加的元素按照 `equals()` 判断时，不能返回 true，即相同的元素只能添加一个
	3. HashSet 不是线程安全的
	4. 集合元素可以是 null
4. <font color="red">HashSet 集合判断两个元素相等的标准：</font>两个对象通过 hashCode() 方法比较相等，并且两个对象的 equals() 方法返回值也相等。
5. **向HashSet中添加元素的过程：**
	1. 当向 HashSet 集合中存入一个元素a时，HashSet 会调用该元素a所在类的 hashCode() 方法来得到元素a的 hashCode 值，然后根据 hashCode 值，通过某种散列函数决定该元素a在 HashSet <font color="red">底层数组中</font>的存储位置（即：索引位置）。（这个散列函数会与底层数组的长度相计算得到在数组中的下标，并且这种散列函数计算还尽可能保证能均匀存储元素，越是散列分布，该散列函数设计的越好）
	2. **此时判断数组此位置上是否已经有其他元素：**
	3. 如果此位置上没有其他元素，则元素a添加成功 --> **情况1**
	4. 如果此位置上有其他元素b（或以链表形式存在的多个元素），则比较元素a与元素b的 hashCode 值：
		1. 如果 hashCode 值不相同，则元素a添加成功 --> **情况2**
		2. 如果 hashCode 值相同，进而需要调用equals()方法：
			1. 如果 equals() 方法返回 true，说明 a 与 b 相同，则添加失败
			2. 如果 equals() 方法返回 false，说明 a 与 b 不相同，则元素 a 添加成功 --> **情况3**
	5. 对于添加成功的情况2和情况3而言：元素a与已经存在指定索引位置上的数据以链表的方式存储
		1. jdk 7 ：元素a放到数组中，指向原来的元素
		2. jdk 8 ：原来的元素依然在数组中，指向元素a（7头插法，8尾插法，七上八下）
6. 如果两个元素的 equals() 方法返回 true，但它们的 hashCode() 返回值不相等，hashSet 将会把它们存储在不同的位置，但依然可以添加成功。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F30、Set实现类之一：HashSet底层也是数组.png)

##### （2）、重写 hashCode() 方法的基本原则

1. 在程序运行时，同一个对象多次调用 hashCode() 方法应该返回相同的值。
2. 当两个对象的 equals() 方法比较返回 true 时，这两个对象的 hashCode() 方法的返回值也应相等。
3. 对象中用作 equals() 方法比较的 Field，都应该用来计算 hashCode 值。

##### （3）、重写 equals() 方法的基本原则

1. 以自定义的 Customer 类为例，何时需要重写 equals()？
2. 当一个类有自己特有的“逻辑相等”概念,当改写 equals() 的时候，总是要改写 hashCode()，根据一个类的 equals 方法（改写后），两个截然不同的实例有可能在逻辑上是相等的，但是，根据 Object.hashCode() 方法，它们仅仅是两个对象。
3. 因此，违反了“<font color="red">相等的对象必须具有相等的散列码</font>”。
4. <font color="red">结论：复写equals方法的时候一般都需要同时复写hashCode方法。通常参与计算hashCode的对象的属性也应该参与到equals()中进行计算。</font>

##### （4）、Eclipse/IDEA 工具里 hashCode() 的重写

1. 以 Eclipse/IDEA 为例，在自定义类中可以调用工具自动重写 equals 和 hashCode。问题：<font color="red">为什么用 Eclipse/IDEA 复写 hashCode 方法，有 31 这个数字？</font>
2. 选择系数的时候要选择尽量大的系数。因为如果计算出来的 hash 地址越大，所谓的“冲突”就越少，查找起来效率也会提高。（减少冲突）
3. 并且 31 只占用 5bits，相乘造成数据溢出的概率较小。
4. 31 可以 由i*31== (i<<5)-1来表示,现在很多虚拟机里面都有做相关优化。（提高算法效率）
5. 31 是一个素数，素数作用就是如果我用一个数字来乘以这个素数，那么最终出来的结果只能被素数本身和被乘数还有 1 来整除！(减少冲突)

#### Ⅲ、Set 实现类之二：LinkedHashSet

1. LinkedHashSet 是 HashSet 的子类
2. LinkedHashSet 根据元素的 hashCode 值来决定元素的存储位置，但它同时使用双向链表维护元素的次序，这使得元素看起来是以<font color="red">插入顺序保存</font>的。遍历其内部数据时，可以按照添加到顺序遍历
3. <font color="red">LinkedHashSet插入性能略低于 HashSet</font>，但在迭代遍历访问 Set 里的全部元素时有很好的性能。
4. LinkedHashSet 不允许集合元素重复

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F31、Set实现类之二：LinkedHashSet.png)

#### Ⅳ、Set 实现类之三：TreeSet

##### （1）、介绍

1. TreeSet 是 SortedSet 接口的实现类，TreeSet 可以确保集合元素处于排序状态，按照添加对象的<font color="red">属性</font>进行排序
2. 所以，向 TreeSet 中添加的数据，要求是<font color="red">相同类</font>的对象
3. TreeSet 底层使用<font color="red">红黑树</font>结构存储数据，所以不能放相同的数
4. 新增的方法如下： (了解)
	1. Comparator comparator()
	2. Object first()
	3. Object last()
	4. Object lower(Object e)
	5. Object higher(Object e)
	6. SortedSet subSet(fromElement, toElement)
	7. SortedSet headSet(toElement)
	8. SortedSet tailSet(fromElement)
5. TreeSet 两种排序方法：<font color="red">自然排序</font>和<font color="red">定制排序</font>。默认情况下，TreeSet 采用自然排序。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F32、Set实现类之三：TreeSet.png)

##### （2）、排序：自然排序

1. 自然排序：TreeSet 会调用集合元素的 `compareTo(Object obj)` 方法来比较元素之间的大小关系，然后将集合元素按升序(默认情况)排列
2. <font color="red">如果试图把一个对象添加到 TreeSet 时，则该对象的类必须实现 Comparable 接口。</font>实现 Comparable 的类必须实现 `compareTo(Object obj)` 方法，两个对象即通过 `compareTo(Object obj)` 方法的返回值来比较大小。
3. Comparable 的典型实现：
	1. BigDecimal、BigInteger 以及所有的数值型对应的包装类：按它们对应的数值大小进行比较
	2. Character：按字符的 unicode值来进行比较
	3. Boolean：true 对应的包装类实例大于 false 对应的包装类实例
	4. String：按字符串中字符的 unicode 值进行比较
	5. Date、Time：后边的时间、日期比前面的时间、日期大
4. 向 TreeSet 中添加元素时，只有第一个元素无须比较 compareTo() 方法，后面添加的所有元素都会调用 compareTo() 方法进行比较。
5. <font color="red">因为只有相同类的两个实例才会比较大小，所以向 TreeSet 中添加的应该是同一个类的对象。</font>
6. 对于 TreeSet 集合而言，它<font color="red">判断两个对象是否相等的唯一标准是：两个对象通过 compareTo(Object obj) 方法比较返回值，而不是equals()方法</font>
7. 当需要把一个对象放入 TreeSet 中，重写该对象对应的 equals() 方法时，应保证该方法与 compareTo(Object obj) 方法有一致的结果：如果两个对象通过 equals() 方法比较返回 true，则通过 compareTo(Object obj) 方法比较应返回 0。否则，让人难以理解。

```java
public class demo02 {
  public static void main(String[] args) {
	 TreeSet treeSet = new TreeSet();

	 // 举例一：基本类型
//        treeSet.add(11);
//        treeSet.add(22);
//        treeSet.add(-11);
//        treeSet.add(33);
//        treeSet.add(-100);

	 // 举例二：字符串
//        treeSet.add("AA");
//        treeSet.add("123");
//        treeSet.add("DD");
//        treeSet.add("月海");
//        treeSet.add("BB");
//        treeSet.add("言");

	 // 举例三：
	 treeSet.add(new Person("言",16));
	 treeSet.add(new Person("月海",18));
	 treeSet.add(new Person("羽",20));
	 treeSet.add(new Person("烟花烬头",22));
	 treeSet.add(new Person("烟花烬头",30));

	 // 遍历
	 Iterator iterator = treeSet.iterator();
	 while (iterator.hasNext()){
		   System.out.println(iterator.next());
	 }
  }
}

// 实现自然排序：必须实现Comparable接口
class Person implements Comparable{
  private String name;
  private int age;

  public Person() { }
  public Person(String name, int age) { this.name = name;this.age = age; }

  public String getName() { return name; }
  public void setName(String name) { this.name = name; }

  public int getAge() { return age; }
  public void setAge(int age) { this.age = age; }

  @Override
  public String toString() {
	 return "Person{" +
			  "name='" + name + '\'' +
			  ", age=" + age +
			  '}';
  }

  // 重写的Comparable接口的compareTo(Object o)方法
  // 按照姓名从小到大排列，姓名相同则按年龄从小到大
  @Override
  public int compareTo(Object o) {
	 // 比较传进来的数组与Object o是否是同一个对象
	 if(o instanceof Person){
		   // 强制转型，将Object o强转为Person类型
		   Person person = (Person) o;
		   // 判断两个name的比较结果不是0
		   if(this.name.compareTo(person.name) != 0){
			  // 输出按照姓名从小到大排列
			  return this.name.compareTo(person.name);
			  // 判断两个name的比较结果是0
		   }else{
			  // 按年龄从小到大排列输出
			  return Integer.compare(this.age,person.age);
		   }
		   // 比较传进来的数组与Object o是否是同一个对象
	 }else{
		   throw new RuntimeException("输入的类型不匹配！");
	 }
  }
}
```

##### （3）、排序：定制排序

1. TreeSet 的自然排序要求元素所属的类实现 Comparable 接口，如果元素所属的类没有实现 Comparable 接口，或不希望按照升序(默认情况)的方式排列元素或希望按照其它属性大小进行排序，则考虑使用定制排序。
2. 定制排序，通过 Comparator 接口来实现。需要重写 compare(T o1,T o2) 方法。
3. 利用 int compare(T o1,T o2) 方法，比较 o1 和 o2 的大小：如果方法返回正整数，则表示 o1 大于 o2；如果返回 0，表示相等；返回负整数，表示 o1 小于 o2。
4. 要实现定制排序，需要将实现 Comparator 接口的实例作为形参传递给 TreeSet 的构造器。
5. 此时，<font color="red">仍然只能向TreeSet中添加类型相同的对象</font>。否则发生 ClassCastException 异常。
6. 使用定制排序<font color="red">判断两个元素相等的标准</font>是：通过 Comparator 比较两个元素返回了 0。

```java
public class demo03 {
  public static void main(String[] args) {
	 // 使用Comparator接口的对象来排序
	 Comparator comparator = new Comparator() {
		   // 小按年龄从小到大排列，再按照名称从小到大排序
		   @Override
		   public int compare(Object o1, Object o2) {
			  // 判断o1与o2是不是Person03
			  if(o1 instanceof Person03 && o2 instanceof Person03){
				 // 强制类型转换
				 Person03 p1 = (Person03)o1;
				 Person03 p2 = (Person03)o2;
				 // 判断p1与p2的年龄是否相等
				 if(p1.getAge() != p2.getAge()){
					   // 若是相等，则返回年龄从小到大的排序
					   return Integer.compare(p1.getAge(),p2.getAge());
				 }else{
					   // 若是不等，则返回名称从小到大的排序
					   return p1.getName().compareTo(p2.getName());
				 }
			  } else {
				 throw new RuntimeException("输入的类型不匹配！");
			  }
		   }
	 };

	 // 将Comparator接口返回的对象作为形参传递给TreeSet的构造器
	 TreeSet treeSet = new TreeSet(comparator);

	 // 添加数据
	 treeSet.add(new Person03("言",20));
	 treeSet.add(new Person03("月海",16));
	 treeSet.add(new Person03("羽",16));
	 treeSet.add(new Person03("烟花烬头",30));
	 treeSet.add(new Person03("烟花烬头",22));

	 // 遍历集合
	 Iterator iterator = treeSet.iterator();
	 while (iterator.hasNext()){
		   System.out.println(iterator.next());
	 }
  }
}

// 定制排序
class Person03{
  private String name;
  private int age;

  public Person03() { }
  public Person03(String name, int age) { this.name = name;this.age = age; }

  public String getName() { return name; }
  public void setName(String name) { this.name = name; }

  public int getAge() { return age; }
  public void setAge(int age) { this.age = age; }

  @Override
  public String toString() {
	 return "Person03{" +
			  "name='" + name + '\'' +
			  ", age=" + age +
			  '}';
  }
}
```

### ⑤、Collection 接口练习题

#### Ⅰ、在 List 内去除重复数字值，要求尽量简单


```java   
public static void main(String[] args) {
  // 创建ArrayList集合list
  List list = new ArrayList();
  // 添加5条数据
  list.add(new Integer(1));
  list.add(new Integer(2));
  list.add(new Integer(2));
  list.add(new Integer(4));
  list.add(new Integer(4));
  // 调用duplicateList()方法，将数组作为参数传递过去，并返回集合：list2
  List list2 = duplicateList(list);
  // 遍历集合list2
  for (Object integer : list2) {
  System.out.println(integer);
  }
}

// 方法类
public static List duplicateList(List list) {
  // 创建HashSet()集合set
  HashSet set = new HashSet();
  // 将传递过来的list集合添加到set集合中
  // 因为HashSet()不允许重复的数据，所以添加到集合set中之后就把重复的数据去掉了
  set.addAll(list);
  // 创建ArrayList集合并将集合set添加进去，并返回
  return new ArrayList(set);
}
```

## 3、Map 接口

### ①、Map 接口概述

1. Map 与 Collection 并列存在。用于保存具有<font color="red">映射关系</font>的<font color="red">双列数据</font>：key-value（键值对）-> 类似于高中的函数
2. Map 中的 key 和 value 都可以是<font color="red">任何引用类型</font>的数据
3. Map 中的<font color="red"> key 用 Set 来存放，不允许重复</font>，即同一个 Map 对象所对应的类，须重写 hashCode() 和 equals() 方法
4. 常用 String 类作为 Map 的“键”
5. key 和 value 之间存在单向一对一关系，即通过指定的 key 总能找到唯一的、确定的 value
6. **Map接口的常用实现类：**
	1. <font color="red">HashMap</font>：作为 Map 的<font color="red">主要实现类</font>：线程是不安全的，<font color="red">效率高</font>，可以储存 null 的 key 和 value
	2. LinkedHashMap：保证在遍历 Map 元素时，可以按照添加的顺序实现遍历。原因：在原有的 HashMap 的底层结构上，添加了一对指针，指向前一个和后一个元素（双向链表）。
	3. TreeMap：保证可以按照添加的 key-value（键值对）进行排序，实现排序遍历，此时考虑使用 key 的自然排序或定制排序。<font color="red">底层使用红黑树</font>
	4. Hashtable：作为古老的实现类：线程是安全的，效率低，不能储存 null 的 key 和 value
	5. Properties：常用来处理配置文件，key 和 value 都是 String 类型
7. 其中，<font color="red">HashMap 是 Map 接口使用频率最高的实现类</font>
8. Map 接口继承树

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F33、Map接口继承树.png)

9. **Map结构的理解：**
	1.  Map 中的 key：无序的、不可重复的，使用 Set 存储所有的 key；key 所在的类要重写 equals() 和 hashCode() 方法（以 HashMap 为例） 
	2.  Map 中的 value：无序的、可重复的，使用 Callection 存储所有的 value；value 所在类要重写 equals() 方法
	3.  一个键值对：一个 key 和一个 value 构成了一个 Entry 对象
	4.  Map 中的 Entry：无序的、不可重复的，使用 Set 存储所有的 Entry

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F34、Map接口的理解.png)

### ②、Map 接口的常用方法

#### Ⅰ、添加、删除、修改操作

| 方法                                  | 作用                           |
| ----------------------------------- | ---------------------------- |
| Object put(Object key,Object value) | 将指定key-value添加到(或修改)当前map对象中 |
| void putAll(Map m)                  | 将m中的所有key-value对存放到当前map中    |
| Object remove(Object key)           | 移除指定key的key-value对，并返回value  |
| void clear()                        | 清空当前map中的所有数据                |

#### Ⅱ、元素查询的操作

| 方法                                  | 作用                  |
| ----------------------------------- | ------------------- |
| Object get(Object key)              | 获取指定key对应的value     |
| boolean containsKey(Object key)     | 是否包含指定的key          |
| boolean containsValue(Object value) | 是否包含指定的value        |
| int size()                          | 返回map中key-value对的个数 |
| boolean isEmpty()                   | 判断当前map是否为空         |
| boolean equals(Object obj)          | 判断当前map和参数对象obj是否相等 |

#### Ⅲ、元视图操作的方法

| 方法                  | 作用                       |
| ------------------- | ------------------------ |
| Set keySet()        | 返回所有key构成的Set集合          |
| Collection values() | 返回所有value构成的Collection集合 |
| Set entrySet()      | 返回所有key-value对构成的Set集合   |

#### Ⅳ、总结

1. 添加：`Object put(Object key,Object value)`
2. 删除：`Object remove(Object key)`
3. 修改：`Object put(Object key,Object value)`
4. 查询：`Object get(Object key)`
5. 长度：`size()`
6. 遍历：`Set keySet()`、`Collection values()`、`Set entrySet()`

```java
public class demo01 {
  public static void main(String[] args) {
	 HashMap map = new HashMap();

	 // 1、Object put(Object key,Object value)：
	 // 将指定key-value添加到(或修改)当前map对象中
	 // key与value不限数据类型，key不可重复，value可重复
	 map.put("A",123);// --> 添加
	 map.put("A","AA");// --> 修改
	 map.put(12,"AA");// --> 添加
	 System.out.println(map);// --> {A=AA, 12=AA}

	 // 2、void putAll(Map m):将m中的所有key-value对存放到当前map中
	 HashMap m = new HashMap();
	 m.put(1,"111");
	 m.put(2,"BB");
	 map.putAll(m);
	 System.out.println(map);

	 // 3、Object remove(Object key)：
	 // 移除指定key的key-value对，并返回value
	 System.out.println(map.remove(1));
	 System.out.println(map);

	 // 4、void clear()：清空当前map中的所有数据
	 //map.clear();// 与 map == null 不同
	 System.out.println(map);

	 // 5、bject get(Object key)：获取指定key对应的value
	 System.out.println(map.get(2));

	 // 6、boolean containsKey(Object key)：是否包含指定的key
	 System.out.println(map.containsKey("A"));

	 // 7、boolean containsValue(Object value)：是否包含指定的value
	 System.out.println(map.containsValue("AA"));

	 // 8、int size()：返回map中key-value对的个数
	 System.out.println(map.size());

	 // 9、boolean isEmpty()：判断当前map是否为空
	 System.out.println(map.isEmpty());

	 // 10、boolean equals(Object obj)：判断当前map和参数对象obj是否相等
	 System.out.println(map.equals(map));// --> 集合map和集合map
	 System.out.println(map.equals(m));// --> 集合map和集合m
	 System.out.println(map.equals("AA"));// --> 集合map和字符串"AA"
  }
}
```

```java
public class demo02 {
  public static void main(String[] args) {
	 Map map = new HashMap();

	 map.put("AA","月海");
	 map.put("BB",111);
	 map.put(1,"言");
	 map.put(2,222);

	 // 1、Set keySet()：返回所有key构成的Set集合
	 Set set = map.keySet();
	 // 调用set集合的iterator()方法返回迭代器对象，用于集合遍历
	 Iterator iterator = set.iterator();
	 while (iterator.hasNext()){
		   System.out.println(iterator.next());
	 }

	 // 2、Collection values()：返回所有value构成的Collection集合
	 Collection collection = map.values();
	 for (Object obj : collection){
		   System.out.println(obj);
	 }

	 //3、Set entrySet()：返回所有key-value对构成的Set集合
	 Set entrySet = map.entrySet();
	 // 3.1、直接遍历
	 Iterator iterator02 = entrySet.iterator();
	 while (iterator02.hasNext()){
		   System.out.println(iterator02.next());
	 }

	 Iterator iterator03 = entrySet.iterator();
	 // 3.2、使用Entry[]数组遍历，单独拿到key和value
	 while (iterator03.hasNext()){
		   Object obj = iterator03.next();
		   Map.Entry entry = (Map.Entry) obj;
		   System.out.println("Key：" + entry.getKey() + " --> value：" + entry.getValue());
	 }
  }
}
```

### ③、Map实现类之一：HashMap

#### Ⅰ、介绍

1. <font color="red">HashMap 是 Map 接口使用频率最高的实现类。</font>
2. 允许使用 null 键和 null 值，与 HashSet 一样，不保证映射的顺序。
3. 所有的 key 构成的集合是 Set，无序的、不可重复的。所以，key 所在的类要重写：equals() 和 hashCode()
4. 所有的 value 构成的集合是 Collection：无序的、可以重复的。所以，value 所在的类要重写：equals()
5. 一个 ey-value 构成一个 entry
6. 所有的 entry 构成的集合是 Set，无序的、不可重复的
7. HashMap<font color="red"> 判断两个 key 相等的标准</font>是：两个 key 通过 equals() 方法返回 true，hashCode 值也相等。
8. HashMap<font color="red"> 判断两个 value 相等的标准</font>是：两个 value 通过 equals() 方法返回 true。

#### Ⅱ、HashMap 的底层实现原理

##### （1）、jdk 7 

1. 在实例化以后，底层创建了长度是 16 的一堆数组 `Entry[] table`

```java
HashMap map = new HashMap();
```

2. 可能已经执行过多次 put，添加过一些数据

```java
map.put(key1,value1);
```

3. 首先，调用 key1 所在类的 hashCode() 计算 key1 的哈希值，此哈希值经过某种算法计算以后，得到在 Entry 数组中的存放位置
4. 如果此位置上的数据为空，此时的 key1-value1（Entry 数组）添加成功 --> **情况1**
5. 如果此位置上的数据不为空，意味着此位置上存在一个或多个数据（多个数据以链表形式存在），则比较 key1 和已经存在的一个或多个数据的哈希值：
	1. 如果 key1 的哈希值与已经存在的数据的哈希值不相同，此时 key1-value1（Entry数组）添加成功 --> **情况2**
	2. 如果 key1 的哈希值与已经存在的某一个数据 key2-value2 的哈希值相同，则继续比较：调用 key1 所在类的 equals(key2) 方法
		1. 如果 equals() 返回 false：此时 ey1-value1（Entry数组）添加成功 --> **情况3**
		2. 如果 equals() 返回 true：那么使用 value1 替换 value2（相当于修改）
6. 补充：对于添加成功的情况 2 和情况 3 而言，此时 key1-value1（Entry数组）和原来的数据以链表的方式存储
7. 在不断的添加过程中，会涉及到扩容问题，当超出临界值（且要存放的位置非空）时，扩容。默认的扩容方式：扩容为原来容量的 2 倍，并将原有的数据复制过来。

##### （2）、jdk 8 相较于 jdk 7 的不同

1. 实例化以后，底层没有创建一个长度为 16 的数组

```java
   HashMap map = new HashMap();
```

2. jdk 8 底层的数组是：`Node[]`，而非 `Entry[]`
3. 首次调用 `put()` 方法时，底层才创建长度为 16 的数组
4. jdk 7 的结构只有：数组 + 链表
5. Jdk 8 中底层结构：数组 + 链表 + 红黑树 --> 当数组中的某一个索引位置上的元素以链表形式存在的数据个数 > 8 且当前数组的长度 > 64 时，此时此索引位置上的所有数据改为使用红黑树存储

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F35、HashMap的存储结构.png)

### ④、Map 实现类之二：LinkedHashMap

#### Ⅰ、介绍

1. LinkedHashMap 是 HashMap 的子类
2. 在 HashMap 存储结构的基础上，使用了一对双向链表来记录添加元素的顺序
3. 与 LinkedHashSet 类似，LinkedHashMap 可以维护 Map 的迭代顺序：迭代顺序与 Key-Value 对的插入顺序一致

#### Ⅱ、LinkedHashMap的底层实现原理

1. LinkedHashMap 中继承并重写了 HashMap中 的 Node 数组，为 Entry
2. 增加了两个变量：`Entry<K,V> before, after;`，指向前一个和后一个元素
3. 使其能够记录添加的元素的先后顺序

```java
// HashMap中的内部类：Node
static class Node<K,V> implements Map.Entry<K,V> {
  final int hash;
  final K key;
  V value;
  Node<K,V> next;
}

// LinkedHashMap中的内部类：Entry
static class Entry<K,V> extends HashMap.Node<K,V> {
  Entry<K,V> before, after;
  Entry(int hash, K key, V value, Node<K,V> next) {
	 super(hash, key, value, next);
  }
}
```

### ⑤、Map 实现类之三：TreeMap

1. TreeMap 存储 Key-Value 对时，需要根据 key-value 对进行排序。TreeMap 可以保证所有的 Key-Value 对处于<font color="red">有序</font>状态。
2. TreeSet 底层使用<font color="red">红黑树</font>结构存储数据
3. TreeMap 的 Key 的排序：
	1. <font color="red">自然排序</font>：TreeMap 的所有的 Key 必须实现 Comparable 接口，而且所有的 Key 应该是同一个类的对象，否则将会抛出 ClasssCastException
	2. <font color="red">定制排</font>序：创建 TreeMap 时，传入一个 Comparator 对象，该对象负责对TreeMap 中的所有 key 进行排序。此时不需要 Map 的 Key 实现Comparable 接口
4. TreeMap 判断<font color="red">两个 key 相等的标准</font>：两个 key 通过 compareTo() 方法或者 compare() 方法返回 0。

```java
// 自然排序
public class demo03 {
  public static void main(String[] args) {
	 TreeMap map = new TreeMap();

	 Person p1 = new  Person("月海",16);
	 Person p2 = new  Person("烟花烬头",14);
	 Person p3 = new  Person("言",18);
	 Person p4 = new  Person("羽",20);

	 map.put(p1,80);
	 map.put(p2,60);
	 map.put(p3,71);
	 map.put(p4,100);

	 Set set = map.entrySet();
	 Iterator iterator = set.iterator();
	 while (iterator.hasNext()){
		   System.out.println(iterator.next());
	 }

  }
}

class Person implements Comparable{
  public String name ;
  public int age;

  public Person() { }
  public Person(String name, int age) {
	 this.name = name;
	 this.age = age;
  }

  @Override
  public String toString() {
	 return "Person{" +
			  "name='" + name + '\'' +
			  ", age=" + age +
			  '}';
  }

  @Override
  public boolean equals(Object o) {
	 if (this == o) return true;
	 if (o == null || getClass() != o.getClass()) return false;
	 Person person = (Person) o;
	 return age == person.age &&
			  Objects.equals(name, person.name);
  }

  @Override
  public int hashCode() {
	 return Objects.hash(name, age);
  }

  // 重写的Comparable接口的compareTo(Object o)方法
  // 按照年龄从小到大排列，年龄相同则按姓名从小到大
  @Override
  public int compareTo(Object o) {
	 // 比较传进来的数组与Object o是否是同一个对象
	 if(o instanceof Person){
		   // 强制转型，将Object o强转为Person类型
		   Person person = (Person) o;
		   // 判断两个age的比较结果不是0
		   if(this.age != person.age){
			  // 按年龄从小到大排列输出
			  return Integer.compare(this.age,person.age);
			  // 判断两个name的比较结果是0
		   }else{
			  // 输出按照姓名从小到大排列
			  return this.name.compareTo(person.name);
		   }
		   // 比较传进来的数组与Object o是否是同一个对象
	 }else{
		   throw new RuntimeException("输入的类型不匹配！");
	 }
  }
}
```

```java
// 定制排序
public class demo04 {
  public static void main(String[] args) {
	 TreeMap map = new TreeMap(new Comparator() {
		   // 重写的Comparator接口的compare方法
		   // 按照年龄从小到大排列，年龄相同则按姓名从小到大
		   @Override
		   public int compare(Object o1, Object o2) {
			  // 比较传进来的数组与Object o是否是同一个对象
			  if(o1 instanceof Person04 && o2 instanceof Person04){
				 // 强制转型，将Object o强转为Person类型
				 Person04 p1 = (Person04) o1;
				 Person04 p2 = (Person04) o2;
				 // 判断两个age的比较结果不是0
				 if(p1.age != p2.age){
					   // 按年龄从小到大排列输出
					   return Integer.compare(p1.age,p2.age);
					   // 判断两个name的比较结果是0
				 }else{
					   // 输出按照姓名从小到大排列
					   return p1.name.compareTo(p2.name);
				 }
				 // 比较传进来的数组与Object o是否是同一个对象
			  }else{
				 throw new RuntimeException("输入的类型不匹配！");
			  }
		   }
	 });

	 Person04 p1 = new  Person04("月海",16);
	 Person04 p2 = new  Person04("烟花烬头",14);
	 Person04 p3 = new  Person04("言",18);
	 Person04 p4 = new  Person04("羽",20);

	 map.put(p1,80);
	 map.put(p2,60);
	 map.put(p3,71);
	 map.put(p4,100);

	 Set set = map.entrySet();
	 Iterator iterator = set.iterator();
	 while (iterator.hasNext()){
		   System.out.println(iterator.next());
	 }
  }
}

class Person04{
  public String name ;
  public int age;

  public Person04() { }
  public Person04(String name, int age) {
	 this.name = name;
	 this.age = age;
  }

  @Override
  public String toString() {
	 return "Person04{" +
			  "name='" + name + '\'' +
			  ", age=" + age +
			  '}';
  }

  @Override
  public boolean equals(Object o) {
	 if (this == o) return true;
	 if (o == null || getClass() != o.getClass()) return false;
	 Person04 person04 = (Person04) o;
	 return age == person04.age &&
			  Objects.equals(name, person04.name);
  }

  @Override
  public int hashCode() {
	 return Objects.hash(name, age);
  }
}
```

### ⑥、Map 实现类之四：Hashtable

1. Hashtable 是个古老的 Map 实现类，JDK1.0 就提供了。不同于 HashMap，Hashtable 是线程安全的。
2. Hashtable 实现原理和 HashMap 相同，功能相同。底层都使用哈希表结构，查询速度快，很多情况下可以互用。
3. 与 HashMap 不同，Hashtable 不允许使用 null 作为 key 和 value
4. 与 HashMap 一样，Hashtable 也不能保证其中 Key-Value 对的顺序
5. Hashtable 判断两个 key 相等、两个 value 相等的标准，与 HashMap 一致。

### ⑦、Map 实现类之五：Properties

1. Properties 类是 Hashtable 的子类，该对象用于处理属性文件
2. 由于属性文件里的 key、value 都是字符串类型，所以 Properties 里的 key 和 value 都是字符串类型
3. 存取数据时，建议使用 `setProperty(String key,String value)` 方法和 `getProperty(String key)` 方法

```java
public class demo05 {
  public static void main(String[] args) throws IOException {
	 // Properties()常用来处理配置文件，key和value都是String类型
	 Properties properties = new Properties();
	 // 文件路径，需抛出异常
	 FileInputStream fis = new FileInputStream("D:\\Idea\\save\\Test\\4、集合\\src\\com\\yuehai\\day03\\demo05.properties");
	 // 加载流对应的文件，需抛出异常
	 properties.load(fis);

	 // 获取key对应的value
	 String name = properties.getProperty("name");
	 String password = properties.getProperty("password");

	 // 打印
	 System.out.println("name：" + name + "，password：" + password);
	 // 关闭，需抛出异常
	 fis.close();
  }
}
```

## 4、Collections 工具类

### ①、介绍

1. Collections 是一个操作<font color="red"> Set、List 和 Map </font>等集合的工具类
2. Collections 中提供了一系列静态的方法对集合元素进行排序、查询和修改等操作，还提供了对集合对象设置不可变、对集合对象实现同步控制等方法

### ②、Collections 常用方法


1. 排序操作：（均为 static 方法）

|方法|作用|
|--|--|
|reverse(List)|反转 List 中元素的顺序|
|shuffle(List)|对 List 集合元素进行随机排序|
|sort(List)|根据元素的自然顺序对指定 List 集合元素按升序排序|
|sort(List，Comparator)|根据指定的 Comparator 产生的顺序对 List 集合元素进行排序|
|swap(List，int， int)|将指定 list 集合中的 i 处元素和 j 处元素进行交换|

2. 查找、替换：

|方法|作用|
|--|--|
|Object max(Collection)|根据元素的自然顺序，返回给定集合中的最大元素|
|Object max(Collection，Comparator)|根据 Comparator 指定的顺序，返回给定集合中的最小元素|
|Object min(Collection)|根据元素的自然顺序，返回给定集合中的最大元素|
|Object min(Collection，Comparator)|根据 Comparator 指定的顺序，返回给定集合中的最小元素|
|int frequency(Collection，Object)|返回指定集合中指定元素的出现次数|
|void copy(List dest,List src)|将src中的内容复制到dest中|
|boolean replaceAll(List list，Object oldVal，Object newVal)|使用新值替换List 对象的所有旧值|

```java
public class demo01 {
  public static void main(String[] args) {
	 List list = new ArrayList();

	 list.add(123);
	 list.add(-99);
	 list.add(0);
	 list.add(123);
	 // 打印
	 System.out.println(list);

	 // 1、reverse(List)：反转 List 中元素的顺序
	 Collections.reverse(list);
	 System.out.println(list);

	 // 2、shuffle(List)：对 List 集合元素进行随机排序
	 Collections.shuffle(list);
	 System.out.println(list);

	 // 3、sort(List)：根据元素的自然顺序对指定 List 集合元素按升序排序
	 //    只能排序数字
	 Collections.sort(list);
	 System.out.println(list);

	 // 4、swap(List，int， int)：将指定 list 集合中的 i 处元素和 j 处元素进行交换
	 Collections.swap(list,0,1);
	 System.out.println(list);

	 // 5、Object max(Collection)：根据元素的自然顺序，返回给定集合中的最大元素
	 System.out.println(Collections.max(list));
	 // 6、Object max(Collection，Comparator)：根据 Comparator 指定的顺序，返回给定集合中的最大元素
	 // 7、Object min(Collection)：根据元素的自然顺序，返回给定集合中的最大元素
	 // 8、Object min(Collection，Comparator)：根据 Comparator 指定的顺序，返回给定集合中的最小元素

	 // 9、int frequency(Collection，Object)：返回指定集合中指定元素的出现次数
	 System.out.println(Collections.frequency(list, 123));

	 // 10、void copy(List dest,List src)：将src中的内容复制到dest中
	 // --> 错误的写法，会报异常：List de = new ArrayList();
	 // --> 错误的写法，会报异常：Collections.copy(de,list);
	 List de = Arrays.asList(new Object[list.size()]);//创建时给予长度
	 Collections.copy(de,list);
	 System.out.println(de);
	 // 11、boolean replaceAll(List list，Object oldVal，Object newVal)：使用新值替换List 对象的所有旧值
  }
}
```

3. 同步控制：Collections 类中提供了多个 `synchronizedXxx()` 方法，该方法可使将指定集合包装成线程同步的集合，从而可以解决多线程并发访问集合时的线程安全问题

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F36、Collections常用方法：同步控制.png)

```java
public class demo02 {
  public static void main(String[] args) {
	 List list = new ArrayList();
	 // 返回的list1即为线程安全的list
	 List list1 = Collections.synchronizedList(list);
  }
}
```

4. Enumeration 接口是 Iterator 迭代器的 “古老版本”

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F37、Enumeration.png)

# 十一、泛型

## 1、为什么要有泛型


1. 泛型：标签
2. 举例：
	1. 中药店，每个抽屉外面贴着标签
	2. 超市购物架上很多瓶子，每个瓶子装的是什么，有标签
3. 泛型的设计背景：集合容器类在设计阶段/声明阶段不能确定这个容器到底实际存的是什么类型的对象，所以<font color="red">在 JDK1.5 之前只能把元素类型设计为 Object，JDK1.5 之后使用泛型来解决。</font>因为这个时候除了元素的类型不确定，其他的部分是确定的，例如关于这个元素如何保存，如何管理等是确定的，因此此时<font color="red">把元素的类型设计成一个参数，这个类型参数叫做泛型</font>。`Collection<E>`，`List<E>`，`ArrayList<E>` 这个 `<E>` 就是类型参数，即泛型。
4. **泛型的概念**：
	1. <font color="red">所谓泛型，就是允许在定义类、接口时通过一个标识表示类中某个属性的类型或者是某个方法的返回值及参数类型。这个类型参数将在使用时（例如，继承或实现这个接口，用这个类型声明变量、创建对象时）确定（即传入实际的类型参数，也称为类型实参）。</font>
	2. 从 JDK1.5 以后，Java 引入了“参数化类型（Parameterized type）”的概念，允许我们在创建集合时再指定集合元素的类型，正如：`List<String>`，这表明该 List 只能保存字符串类型的对象。
	3. JDK1.5 改写了集合框架中的全部接口和类，为这些接口、类增加了泛型支持，从而可以在声明集合变量、创建集合对象时传入类型实参。
5. 那么为什么要有泛型呢，直接 Object 不是也可以存储数据吗？
	1. 解决元素存储的安全性问题，好比商品、药品标签，不会弄错。
	2. 解决获取数据元素时，需要类型强制转换的问题，好比不用每回拿商品、药品都要辨别。
6. Java 泛型可以保证如果程序在编译时没有发出警告，运行时就不会产生 ClassCastException 异常。同时，代码更加简洁、健壮。
7. **在集合中没有泛型时：**

```java
public class demo01 {
	public static void main(String[] args) {
		ArrayList list = new ArrayList();
		// 需求：存放学生的成绩
		list.add(123);
		list.add(0);
		list.add(-1);
		// 问题一：类型不安全
		list.add("月海");

		// 遍历
		for (Object obj : list){
			//  问题二：强转时，可能出现ClassCastException
			int score = (int) obj;
			System.out.println(score);
		}
	}
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F38、在集合中没有泛型时.png)

8. **在集合中有泛型时：**

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F39、在集合中有泛型时.png)

## 2、在集合中使用泛型

1. 集合接口或集合类在 5.0 时都修改为带泛型的结构
2. 在实例化集合类时，可以指明具体的泛型类型
3. 指明完泛型以后，在集合类或接口中凡是定义类或接口时，内部结构（比如：方法、构造器、属性等）使用到类的泛型的位置都指明为实例化的泛型类型
   1. 比如：`add(E e)` --> 实例化以后：`add(Integer e)`
4. 注意点：泛型的类型必须是类，不能是基本数据类型，需要用到基本数据类型的位置，拿包装类替换
5. 如果实例化时，没有指明泛型的类型，默认为 `java.lang.Object` 类型

```java
// Collection接口的ArryList举例
public class demo02 {
	public static void main(String[] args) {
		// 创建集合，并规定泛型为Integer
		// 注意泛型不能是基本数据类型，要是他的包装类
		// ArrayList<Integer> list = new ArrayList<Integer>();
		// jdk 7 新特性：类型推断，后面不用写泛型
		ArrayList<Integer> list = new ArrayList<>();

		list.add(111);
		list.add(-23);
		list.add(0);

		Iterator<Integer> iterator = list.iterator();
		while (iterator.hasNext()){
			int score = iterator.next();
			System.out.println(score);
		}
	}
}
```

```java
// Map接口的HashMap举例
public class demo03 {
	public static void main(String[] args) {
		// 创建map集合，并规定泛型，key为String类型，value为Integer类型
		// Map<String,Integer> map = new HashMap<String,Integer>();
		// jdk 7 新特性：类型推断，后面不用写泛型
		Map<String,Integer> map = new HashMap<>();

		map.put("言",14);
		map.put("月海",16);
		map.put("羽",18);

		// 泛型的嵌套
		Set<Map.Entry<String, Integer>> entries = map.entrySet();

		Iterator<Map.Entry<String, Integer>> iterator = entries.iterator();
		while (iterator.hasNext()){
			Map.Entry<String, Integer> next = iterator.next();
			String key = next.getKey();
			Integer value = next.getValue();
			System.out.println("Key：" + key + "，value：" + value);
		}
	}
}
```

6. 排序中的泛型

```java
// 自然排序
public class demo04 {
	public static void main(String[] args) {
		TreeMap<Person,Integer> map = new TreeMap<>();

		Person p1 = new  Person("月海",16);
		Person p2 = new  Person("烟花烬头",14);
		Person p3 = new  Person("言",18);
		Person p4 = new  Person("羽",20);

		map.put(p1,80);
		map.put(p2,60);
		map.put(p3,71);
		map.put(p4,100);

		Set<Map.Entry<Person, Integer>> entries = map.entrySet();
		Iterator<Map.Entry<Person, Integer>> iterator = entries.iterator();
		while (iterator.hasNext()){
			Map.Entry<Person, Integer> next = iterator.next();
			System.out.println(next);
		}

	}
}

// 相比较谁就写谁的泛型，也可以直接写类名
class Person implements Comparable<Person>{
	public String name ;
	public int age;

	public Person() { }
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	@Override
	public String toString() {
		return "Person{" +
				"name='" + name + '\'' +
				", age=" + age +
				'}';
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		Person person = (Person) o;
		return age == person.age &&
				Objects.equals(name, person.name);
	}

	@Override
	public int hashCode() {
		return Objects.hash(name, age);
	}

	// 没有指明泛型时的写法：
	// 重写的Comparable接口的compareTo(Object o)方法
	// 按照年龄从小到大排列，年龄相同则按姓名从小到大
//    @Override
//    public int compareTo(Object o) {
//        // 比较传进来的数组与Object o是否是同一个对象
//        if(o instanceof Person){
//            // 强制转型，将Object o强转为Person类型
//            Person person = (Person) o;
//            // 判断两个age的比较结果不是0
//            if(this.age != person.age){
//                // 按年龄从小到大排列输出
//                return Integer.compare(this.age,person.age);
//            // 判断两个name的比较结果是0
//            }else{
//                // 输出按照姓名从小到大排列
//                return this.name.compareTo(person.name);
//            }
//            // 比较传进来的数组与Object o是否是同一个对象
//        }else{
//            throw new RuntimeException("输入的类型不匹配！");
//        }
//    }

	// 指明泛型时的写法：
	// 按照年龄从小到大排列，年龄相同则按姓名从小到大
	@Override
	public int compareTo(Person o) {
		// 判断两个age的比较结果不是0
		if(this.age != o.age){
			// 按年龄从小到大排列输出
			return Integer.compare(this.age,o.age);
		// 判断两个name的比较结果是0
		}else{
			// 输出按照姓名从小到大排列
			return this.name.compareTo(o.name);
		}
	}
}
```

## 3、自定义泛型结构

### ①、介绍

1. 泛型的声明
	1. `interface List< T > 和 class GenTest< K , V >` 
	2. 其中，T,K,V 不代表值，而是表示类型。这里使用任意字母都可以。常用T表示，是 Type 的缩写。
2. 泛型的实例化：
	1. 一定要在类名后面指定类型参数的值（类型）。如：
	2. `List< String > strList = new ArrayList< String >();`
	3. `Iterator< Customer > iterator = customers.iterator();`
	4. T 只能是类，不能用基本数据类型填充。但可以使用包装类填充
	5. 把一个集合中的内容限制为一个特定的数据类型，这就是 generics 背后的核心思想

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F40、自定义泛型结构.png)

### ②、自定义泛型类、泛型接口

1. 泛型类可能有多个参数，此时应将多个参数一起放在尖括号内。比如：`<E1, E2, E3>`
2. 泛型类的构造器如下：`public GenericClass(){}`；而这个是错误的：`public GenericClass< E >(){}`
3. 实例化后，操作原来泛型位置的结构必须与指定的泛型类型一致。
4. <font color="red">泛型不同的引用不能相互赋值</font>；尽管在编译时 `ArrayList<String>`和 `ArrayList<Integer>` 是两种类型，但是，在运行时只有一个 ArrayList 被加载到 JVM 中。
5. 泛型如果不指定，将被擦除，泛型对应的类型均按照 Object 处理，但不等价于 Object。<font color="red">经验：泛型要使用一路都用。要不用，一路都不要用。</font>
6. 如果泛型结构是一个接口或抽象类，则不可创建泛型类的对象。
7. jdk1.7，泛型的简化操作：`ArrayList< Fruit > flist = new ArrayList<>();`
8. 泛型的指定中不能使用基本数据类型，可以使用包装类替换。
9.  在类/接口上声明的泛型，在本类或本接口中即代表某种类型，可以作为非静态属性的类型、非静态方法的参数类型、非静态方法的返回值类型。但<font color="red">在静态方法中不能使用类的泛型</font>。
10. 异常类不能是泛型的
11. 不能使用 `new E[]` 创建数组。
	1.  但是可以：`E[] elements = (E[])new Object[capacity];`
	2.  参考：`ArrayList` 源码中声明：`Object[] elementData`，而非泛型参数类型数组。
12. 父类有泛型，子类可以选择保留泛型也可以选择指定泛型类型：
	1.  子类不保留父类的泛型：按需实现
		1.  没有类型 擦除
		2.  具体类型
	2.  子类保留父类的泛型：泛型子类
		1.  全部保留
		2.  部分保留

	```java
class Father<T1, T2> {
}

// 子类不保留父类的泛型
// 1)没有类型 擦除
// 等价于class Son extends Father<Object,Object>{
class Son1 extends Father {
}

// 2)具体类型
class Son2 extends Father<Integer, String> {
}

// 子类保留父类的泛型
// 1)全部保留
class Son3<T1, T2> extends Father<T1, T2> {
}

// 2)部分保留
class Son4<T2> extends Father<Integer, T2> {
}
	```

```java
class Father<T1, T2> {
}

// 子类不保留父类的泛型
// 1)没有类型 擦除
// 等价于class Son extends Father<Object,Object>{
class Son<A, B> extends Father{
}

// 2)具体类型
class Son2<A, B> extends Father<Integer, String> {
}

// 子类保留父类的泛型
// 1)全部保留
class Son3<T1, T2, A, B> extends Father<T1, T2> {
}

// 2)部分保留
class Son4<T2, A, B> extends Father<Integer, T2> {
}
```

13.  结论：子类必须是“富二代”，子类除了指定或保留父类的泛型，还可以增加自己的泛型
14.  定义了泛型结构：

```java
public class demo05 {
	public static void main(String[] args) {
		// 如果定义了泛型类，实例化没有指明类的泛型，则认为此泛型类型为Object类型
		// 要求：如果大家定义了类时带泛型的，建议在实例化时要指明类的泛型
		Order order = new Order();
		order.setOrderT(123);
		order.setOrderT("ABC");

		// 建议：实例化时指明类的泛型
		Order<String> order02 = new Order("yan",16,"泛型");
	}
}

// 定义的泛型类
class Order<T>{
	String orderName;
	int orderId;
	// 类的内部结构就可以使用类的泛型
	private T orderT;

	// 构造器
	public Order() { }
	public Order(String orderName, int orderId, T orderT) {
		this.orderName = orderName;
		this.orderId = orderId;
		this.orderT = orderT;
	}

	// 此处的get、set、toString都不是泛型方法
	public T getOrderT() { return orderT; }
	public void setOrderT(T orderT) { this.orderT = orderT; }

	@Override
	public String toString() {
		return "Order{" +
				"orderName='" + orderName + '\'' +
				", orderId=" + orderId +
				", orderT=" + orderT +
				'}';
	}

	// static的方法中不能声明泛型
	//public static void show(T t) {
	//
	//}
	
	// 不能在try-catch中使用泛型定义
	//public void test() {
	//try {
	//
	//} catch (MyException<T> ex) {
	//
	//}
	//}
}

// 泛型类的子类
// 不再是泛型类
class Order02 extends Order<Integer>{
	// 此时的orderT属性的类型就是Integer
}

// 仍然是泛型类
class Order03<T> extends Order<T>{
	// 此时的orderT属性的类型任然不确定
}
```

### ③、自定义泛型方法

1. 方法，也可以被泛型化，不管此时定义在其中的类是不是泛型类。
2. 在泛型方法中可以定义泛型参数，此时，参数的类型就是传入数据的类型。
3. 泛型方法的格式：

```java
[访问权限] <泛型> 返回类型<泛型> 方法名(泛型标识 参数名称) 抛出的异常
```

4. 泛型方法声明泛型时也可以指定上限

```java
public class DAO {
	public <E> E get(int id, E e) {
		E result = null;
		return result;
	}
}
```

5. 在方法中出现了泛型的结构，泛型参数与类的泛型参数没有任何关系。换句话说，泛型方法所属的类是不是泛型类都没关系
6. 泛型方法是可以声明为静态的

```java
public class demo01 {
	public static void main(String[] args) {
		Person p1 = new Person();
		// 泛型方法在调用时，指明泛型参数的类型
		Integer[] arr = new Integer[]{1,2,3};
		// 泛型方法在调用时才指明参数的类型
		List<Integer> list = p1.listTest(arr);
		System.out.println(list);

		Person02<String> p2 = new Person02();
		// 泛型方法的泛型与类的泛型没有任何关系
		Integer[] arr02 = new Integer[]{1,2,3};
		// 泛型方法在调用时才指明参数的类型
		List<Integer> list02 = p2.listTest(arr02);
		System.out.println(list02);
	}
}

// 普通类中的泛型方法
class Person{
	// 泛型方法创建时要在返回类型前声明泛型
	// 泛型方法是可以声明为静态的
	//   原因：泛型参数是在调用方法时确定的，并非在实例化时确定
	public static <E> List<E> listTest(E[] arr){
		ArrayList<E> list = new ArrayList();

		for(E e : arr){
			list.add(e);
		}
		return list;
	}
}

// 泛型类中的泛型方法
class Person02<E>{
	// 泛型方法创建时要在返回类型前声明泛型
	public <E> List<E> listTest(E[] arr){
		ArrayList<E> list = new ArrayList();

		for(E e : arr){
			list.add(e);
		}
		return list;
	}
}
```

## 4、泛型在继承上的体现

1. 如果 B 是 A 的一个子类型（子类或者子接口），而 G 是具有泛型声明的类或接口，`G<B>`并不是 `G<A>` 的子类型！
2. 比如：`String` 是 `Object` 的子类，但是 `List<String>` 并不是 `List<Object>` 的子类。

```java
public void testGenericAndSubClass() {
	Person[] persons = null;
	Man[] mans = null;
	// 而 Person[] 是 Man[] 的父类.
	persons = mans;
	
	Person p = mans[0];
	
	// 在泛型的集合上
	List<Person> personList = null;
	List<Man> manList = null;
	// personList = manList;(报错)
}
```

## 5、通配符的使用

### ①、一般通配符的使用

1. 使用类型<font color="red">通配符：？</font>
	1. 比如：`List<?>` ，`Map<?, ?>`
	2. `List<?>` 是 `List<String>`、`List<Object>` 等各种泛型 List 的父类。
2. <font color="red">读取</font> `List<?>` 的对象 list 中的元素时，永远是安全的，因为不管 `list` 的真实类型是什么，它包含的都是 `Object`。
3. <font color="red">写入</font> `list` 中的元素时，不行。因为我们不知道 c 的元素类型，我们不能向其中添加对象；唯一的例外是 null，它是所有类型的成员。
4. <font color="red">将任意元素加入到其中不是类型安全的：</font>
	1. `Collection<?> c = new ArrayList< String >();`
	2. `c.add(new Object());` // 编译时错误
	3. 因为我们不知道 c 的元素类型，我们不能向其中添加对象。add 方法有类型参数E作为集合的元素类型。我们传给 add 的任何参数都必须是一个未知类型的子类。因为我们不知道那是什么类型，所以我们无法传任何东西进去。
5. <font color="red">唯一的例外的是 null，它是所有类型的成员。</font>
6. <font color="red">另一方面，我们可以调用 get() 方法并使用其返回值。返回值是一个未知的类型，但是我们知道，它总是一个 Object。</font>

```java
public class Demo03 {
	public static void main(String[] args) {
		List<Object> list = new ArrayList<Object>();
		list.add(123);
		list.add("AA");

		List<String> list02 = new ArrayList<String>();
		list02.add("SS");

		List<?> list03 = new ArrayList();
		// 通配符不能向其内部添加（写入）数据 --> 因为不确定该添加什么类型
		// list03.add();
		//   除了添加null之外
		list03.add(null);// --> 其实也是啥也没加

		// 通配符可以被其他泛型赋值，相当于他们的父类
		list03 = list;
		//list03 = list02;

		Person03 p1 = new Person03();
		Person03 p2 = new Person03();
		Person03 p3 = new Person03();

		p1.listTest(list);
		p2.listTest(list02);
		p3.listTest(list03);

		// 通配符也可以正常读取数据
		Object o = list03.get(0);
		System.out.println(o);
	}
}

class Person03{
	public void listTest(List<?> list){
		Iterator<?> iterator = list.iterator();
		while (iterator.hasNext()){
			Object next = iterator.next();
			System.out.print(next + "-->");
		}
		System.out.println();
	}
}
```

```java
// //注意点1：编译错误：不能用在泛型方法声明上，返回值类型前面<>不能使用?
public static <?> void test(ArrayList<?> list){

}
```

```java
//注意点2：编译错误：不能用在泛型类的声明上
class GenericTypeClass<?>{

}
```

```java
//注意点3：编译错误：不能用在创建对象上，右边属于创建集合对象
ArrayList<?> list2 = new ArrayList<?>();
```

### ②、有限制的通配符


1. `<?>`：允许所有泛型的引用调用
2. 通配符指定上限：上限 extends：使用时指定的类型必须是继承某个类，或者实现某个接口，即 <=
3. 通配符指定下限：下限 super：使用时指定的类型不能小于操作的类，即 >=
4. 举例：

```java
// 只允许泛型为Number及Number子类的引用调用
<? extends Number> (无穷小 , Number]

// 只允许泛型为Number及Number父类的引用调用
<? super Number> [Number , 无穷大)

// 只允许泛型为实现Comparable接口的实现类的引用调用
<? extends Comparable>
```

```java
public class Demo04 {
	public static void main(String[] args) {
		// 通配符指定上限：(无穷小，Person04]
		// 上限extends：使用时指定的类型必须是继承某个类，或者实现某个接口，即<=
		List<? extends Person04> list01 = new ArrayList<>();
		// 通配符指定下限：[Person04，无穷大)
		// 下限super：使用时指定的类型不能小于操作的类，即>=
		List<? super Person04> list02 = new ArrayList<>();

		List<Person04> list03 = new ArrayList<>();
		List<Student04> list04 = new ArrayList<>();
		List<Object> list05 = new ArrayList<>();

		list01 = list03;
		list01 = list04;
//        list01 = list05;

		list02 = list03;
//        list02 = list04;
		list02 = list05;

		// 读取数据 --> 写上限
		list01 = list04;
		Person04 p = list01.get(0);
//        Student04 p2 = list01.get(0);// 编译不通过

		list02 = list03;
//        Person04 p3 = list02.get(0);// 编译不通过
		Object p4 = list02.get(0);

		// 写入数据 --> 写下限
//        list01.add(new Student04());// 编译不通过

		list02.add(new Person04());
		list02.add(new Student04());

	}
}

class Person04{

}

class Student04 extends Person04{

}
```

# 十二、IO 流

## 1、File 类的使用

### ①、介绍

1. `java.io.File` 类：<font color="red">文件和文件目录路径</font>的抽象表示形式，与平台无关
2. File 能新建、删除、重命名文件和目录，但 File 不能访问文件内容本身。如果需要访问文件内容本身，则需要使用 <font color="red">IO流（输入/输出流）</font>。
3. <font color="red">想要在 Java 程序中表示一个真实存在的文件或目录，那么必须有一个 File 对象，但是 Java 程序中的一个 File 对象，可能没有一个真实存在的文件或目录。</font>
4. File 对象可以作为参数传递给流的构造器

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F41、File相对文件路径.png)

### ②、常用构造器

1. <font color="red">public File(String pathname)</font>：以 pathname 为路径创建 File 对象，可以是<font color="red">绝对路径或者相对路径</font>，如果 pathname 是相对路径，则默认的当前路径在系统属性 `user.dir` 中存储。
	1. 绝对路径：是一个固定的路径,从盘符开始
	2. 相对路径：是相对于某个位置开始
2. <font color="red">public File(String parent,String child)</font>：以 parent 为父路径，child 为子路径创建 File 对象。
3. <font color="red">public File(File parent,String child)</font>：根据一个父 File 对象和子文件路径创建 File 对象
4. 一般 Java 文件的相对路径在主 Project 目录下：相对路径：hello.txt

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F41、File相对文件路径%201.png)

```java
// 此时创建的file仅仅只是内存中的对象而已，与磁盘中的文件没有任何关系
public class Demo01 {
	public static void main(String[] args) {
		// 一、构造器1：public File(String pathname)
		// 以pathname为路径创建File对象，可以是绝对路径或者相对路径，
		// 如果pathname是相对路径，则默认的当前路径在系统属性user.dir中存储。
		//     相对路径
		File file01 = new File("hello.txt");
		//     绝对路径
		File file02 = new File("D:\\Idea\\save\\Test\\6、IO流\\save\\hello.txt");

		System.out.println(file01);
		System.out.println(file02);

		// 二、构造器2：public File(String parent,String child)
		// 以parent为父路径，child为子路径创建File对象。
		File file03 = new File("D:\\Idea\\save\\Test\\6、IO流","save");
		System.out.println(file03);

		// 三、构造器3：public File(File parent,String child)
		// 根据一个父File对象和子文件路径创建File对象
		File file04 = new File(file03,"hello.txt");
		System.out.println(file04);
	}
}
```

### ③、路径分隔符

1. 路径中的每级目录之间用一个路径分隔符隔开。
2. 路径分隔符和系统有关：
	1. windows 和 DOS 系统默认使用 `\` 来表示
	2. UNIX 和 UR L使用 `/` 来表示
3. Java 程序支持跨平台运行，因此路径分隔符要慎用。
4. 为了解决这个隐患，File类提供了一个常量：`public static final String separator`。根据操作系统，动态的提供分隔符。
5. 举例：

```java
// d:\atguigu\info.txt
// Windows和DOS系统
File file1 = new File("d:\\atguigu\\info.txt");
// UNIX和URL
File file3 = new File("d:/atguigu");
// public static final String separator。根据操作系统，动态的提供分隔符。
File file2 = new File("d:" + File.separator + "atguigu" + File.separator + "info.txt");
```

### ④、常用方法

#### Ⅰ、File 类的获取功能

|方法|作用|
|--|--|
|public String getAbsolutePath()|获取绝对路径|
|public String getPath() |获取路径|
|public String getName() |获取名称|
|public String getParent()|获取上层文件目录路径。若无，返回null|
|public long length() |获取文件长度（即：字节数）。不能获取目录的长度|
|public long lastModified() |获取最后一次的修改时间，毫秒值|
|public String[] list() |获取指定目录下的所有文件或者文件目录的名称数组|
|public File[] listFiles() |获取指定目录下的所有文件或者文件目录的File数组|

```java
public class Demo02 {
	public static void main(String[] args) {
		File file01 = new File("hello.txt");
		File file02 = new File("D:\\Idea\\save\\Markdown\\2、Java高级编程\\6、IO流.md");
		File file03 = new File("D:\\Idea\\save\\Markdown\\2、Java高级编程\\img");
		// 一、File类的获取功能
		// 1、public String getAbsolutePath()：获取绝对路径
		System.out.println(file01.getAbsolutePath());
		System.out.println(file02.getAbsolutePath());

		// 2、public String getPath() ：获取路径
		System.out.println(file01.getPath());
		System.out.println(file02.getPath());

		// 3、public String getName() ：获取名称
		System.out.println(file01.getName());
		System.out.println(file02.getName());

		// 4、public String getParent()：获取上层文件目录路径。若无，返回null
		System.out.println(file01.getParent());
		System.out.println(file02.getParent());

		// 5、public long length() ：获取文件长度（即：字节数）。不能获取目录的长度。
		System.out.println(file01.length());
		System.out.println(file02.length());

		// 6、public long lastModified() ：获取最后一次的修改时间，毫秒值
		System.out.println(file01.lastModified());
		// 将返回的毫秒值作为参数添加到Date中，输出Date数据
		System.out.println(new Date(file02.lastModified()));

		// 以下两个方法适用于文件目录
		// 7、public String[] list() ：获取指定目录下的所有文件或者文件目录的名称数组
		// 要求目录存在，不然会报错，只输出文件名称
		String[] list01 = file03.list();
		for(String s : list01){
			System.out.println(s);
		}

		// 8、public File[] listFiles() ：获取指定目录下的所有文件或者文件目录的File数组
		// 输出文件的完整路径
		File[] list02 = file03.listFiles();
		for(File f : list02){
			System.out.println(f);
		}
	}
}
```

#### Ⅱ、File类的重命名功能 --> 剪切与重命名

|方法|作用|
|--|--|
|public boolean renameTo(File dest)|把文件重命名为指定的文件路径|

```java
public class Demo03 {
	public static void main(String[] args) {
		// 二、File类的重命名功能 --> 剪切与重命名
		// 1、public boolean renameTo(File dest):把文件重命名为指定的文件路径与名称
		// 要想保证返回true，需要file01在硬盘中是存在的，且file02不能在硬盘中存在
		File file01 = new File("hello.txt");
		File file02 = new File("D:\\新建文件夹\\hi.txt");

		boolean renameTo = file01.renameTo(file02);
		System.out.println(renameTo);
	}
}
```

#### Ⅲ、File 类的判断功能

|方法|作用|
|--|--|
|public boolean isDirectory()|判断是否是文件目录|
|public boolean isFile() |判断是否是文件|
|public boolean exists() |判断是否存在|
|public boolean canRead() |判断是否可读|
|public boolean canWrite() |判断是否可写|
|public boolean isHidden() |判断是否隐藏|

```java
public class Demo04 {
	public static void main(String[] args) {
		File file01 = new File("hello.txt");
		File file02 = new File("6、IO流");
		// 三、File类的判断功能
		// 1、public boolean isDirectory()：判断是否是文件目录
		System.out.println(file02.isDirectory());

		// 2、public boolean isFile() ：判断是否是文件
		System.out.println(file01.isFile());

		// 3、public boolean exists() ：判断是否存在
		System.out.println(file01.exists());
		System.out.println(file02.exists());

		// 4、public boolean canRead() ：判断是否可读
		System.out.println(file01.canRead());
		System.out.println(file02.canRead());

		// 5、public boolean canWrite() ：判断是否可写
		System.out.println(file01.canWrite());
		System.out.println(file02.canWrite());

		// 6、public boolean isHidden() ：判断是否隐藏
		System.out.println(file01.isHidden());
		System.out.println(file02.isHidden());
	}
}
```

#### Ⅳ、File 类的创建功能

- <font color="red">注意事项：如果你创建文件或者文件目录没有写盘符路径，那么，默认在项目路径下。</font>

|方法|作用|
|--|--|
|public boolean createNewFile() |创建文件。若文件存在，则不创建，返回false|
|public boolean mkdir() |创建文件目录。如果此文件目录存在，就不创建了。<br/>如果此文件目录的上层目录不存在，也不创建。|
|public boolean mkdirs() |创建文件目录。如果上层文件目录不存在，一并创建|

```java
public class Demo05 {
	public static void main(String[] args) throws IOException {
		File file01 = new File("hello.txt");
		File file02 = new File("月海/言");

				// 四、File类的创建功能
		// 1、public boolean createNewFile() ：创建文件。若文件存在，则不创建，返回false
		System.out.println(file01.createNewFile());

		// 2、public boolean mkdir() ：创建文件目录。如果此文件目录存在，就不创建了。
		//    如果此文件目录的上层目录不存在，也不创建。
		System.out.println(file02.mkdir());

		// 3、public boolean mkdirs() ：创建文件目录。如果上层文件目录不存在，一并创建
		System.out.println(file02.mkdirs());
	}
}
```

#### Ⅴ、File 类的删除功能

- 删除注意事项：Java 中的删除不走回收站。
- 要删除一个文件目录，请注意该文件目录内不能包含文件或者文件目录

|方法|作用|
|--|--|
|public boolean delete()|删除文件或者文件夹|

```java
    public class Demo06 {
        public static void main(String[] args) {
            File file = new File("月海/言");
            // 五、File类的删除功能
            // 1、public boolean delete()：删除文件或者文件夹
            // 要删除一个文件目录，请注意该文件目录内不能包含文件或者文件目录
            System.out.println(file.delete());
        }
    }
```

## 2、IO 流原理及流的分类

### ①、Java IO 原理 

1. I/O 是 Input/Output 的缩写， I/O 技术是非常实用的技术，用于<font color="red">处理设备之间的数据传输</font>。如读/写文件，网络通讯等。
2. Java 程序中，对于数据的输入/输出操作以<font color="red">“流(stream)” </font>的方式进行。
3. `java.io` 包下提供了各种“流”类和接口，用以获取不同种类的数据，并通过<font color="red">标准的方法</font>输入或输出数据。
4. Java IO 原理：
   1. <font color="red">输入 input</font>：读取外部数据（磁盘、光盘等存储设备的数据）到程序（内存）中。
   2. <font color="red">输出 output</font>：将程序（内存）数据输出到磁盘、光盘等存储设备中。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F43、IO流原理.png)

### ②、流的分类

1. 按数据流的<font color="red">流向</font>不同分为：**输入流，输出流**
2. 按操作<font color="red">数据单位</font>不同分为：
	1. **字节流(8 bit)：**适合处理图片、视频等
	2. **字符流(16 bit)：**适合处理文本等
3. 按流的<font color="red">角色</font>的不同分为：
	1. **节点流：**直接从数据源或目的地读写数据
	2. **处理流：**不直接连接到数据源或目的地，而是“连接”在已存在的流（节点流或处理流）之上，通过对数据的处理为程序提供更为强大的读写功能。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F46、节点流.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F47、处理流.png)

![|625](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F44、流的分类.png)

1. Java 的 IO 流共涉及 40 多个类，实际上非常规则，都是从如下 4 个<font color="red">抽象基类</font>派生的。
2. 由这四个类派生出来的子类名称都是以其父类名作为子类名后缀。

|(抽象基类)|字节流|字符流|
|--|--|--|
|输入流|<font color="red">InputStream</font>|<font color="red">Reader</font>|
|输出流|<font color="red">OutputStream</font>|<font color="red">Writer</font>|

6. IO 流体系

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F45、IO流体系.png)

### ③、抽象基类的具体分类

#### Ⅰ、输入流（InputStream & Reader）

##### （1）、输入流介绍

1. 1、`InputStream` 和 Reader 是所有输入流的基类。
2. `InputStream`（典型实现：<font color="red">FileInputStream</font>）
	1. `int read()`
	2. `int read(byte[] b)`
	3. `int read(byte[] b, int off, int len)`
3. Reader（典型实现：<font color="red">FileReader</font>）
   1. `int read()`
   2. `int read(char [] c)`
   3. `int read(char [] c, int off, int len)`
4. 程序中打开的文件 IO 资源不属于内存里的资源，垃圾回收机制无法回收该资源，所以应该<font color="red">显式关闭文件 IO 资源</font>。
5. `FileInputStream` 从文件系统中的某个文件中获得输入字节。`FileInputStream` 用于读取非文本数据之类的原始字节流。要读取字符流，需要使用 `FileReader`

##### （2）、InputStream

1. <font color="red">int read()：</font>从输入流中读取数据的下一个字节。返回 0 到 255 范围内的 int 字节值。如果因为已经到达流末尾而没有可用的字节，则返回值 -1。
2. <font color="red">int read(byte[] b)：</font>从此输入流中将最多 b.length 个字节的数据读入一个 byte 数组中。如果因为已经到达流末尾而没有可用的字节，则返回值 -1。否则以整数形式返回实际读取的字节数。
3. <font color="red">int read(byte[] b, int off,int len)：</font>将输入流中最多 len 个数据字节读入 byte 数组。尝试读取 len 个字节，但读取的字节也可能小于该值。以整数形式返回实际读取的字节数。如果因为流位于文件末尾而没有可用的字节，则返回值 -1。
4. <font color="red">public void close() throws IOException：</font>关闭此输入流并释放与该流关联的所有系统资源。

##### （3）、Reader

1. <font color="red">int read()：</font>读取单个字符。作为整数读取的字符，范围在 0 到 65535 之间 (0x00-0xffff)（2个字节的Unicode码），如果已到达流的末尾，则返回 -1
2. <font color="red">int read(char[] cbuf)：</font>将字符读入数组。如果已到达流的末尾，则返回 -1。否则返回本次读取的字符数。
3. <font color="red">int read(char[] cbuf,int off,int len)：</font>将字符读入数组的某一部分。存到数组cbuf中，从off处开始存储，最多读len个字符。如果已到达流的末尾，则返回 -1。否则返回本次读取的字符数。
4. <font color="red">public void close() throws IOException：</font>关闭此输入流并释放与该流关联的所有系统资源。

#### Ⅱ、输出流（OutputStream & Writer）

##### （1）、输出流介绍

1. OutputStream 和 Writer 也非常相似：
   1. <font color="red">void write(<font color="green">int b</font>/<font color="blued">int c</font>);</font>
   2. <font color="red">void write(<font color="green">byte[] b</font>/<font color="blued">char[] cbuf</font>);</font>
   3. <font color="red">void write(<font color="green">byte[] b</font>/<font color="blued">char[] buff, </font>int off, int len);</font>
   4. <font color="red">void flush();</font>
   5. <font color="red">void close()</font>：需要先刷新，再关闭此流
2. 因为字符流直接以字符作为操作单位，所以 Writer 可以用字符串来替换字符数组，即以 String 对象作为参数
   1. <font color="red">void write(String str);</font>
   2. <font color="red">void write(String str, int off, int len);</font>
3. FileOutputStream 从文件系统中的某个文件中获得输出字节。FileOutputStream 用于写出非文本数据之类的原始字节流。要写出字符流，需要使用 FileWriter

##### （2）、OutputStream

1. <font color="red">void write(int b)：</font>将指定的字节写入此输出流。write 的常规协定是：向输出流写入一个字节。要写入的字节是参数 b 的八个低位。b 的 24 个高位将被忽略。 即写入0~255范围的。
2. <font color="red">void write(byte[] b)：</font>将 b.length 个字节从指定的 byte 数组写入此输出流。write(b) 的常规协定是：应该与调用 write(b, 0, b.length) 的效果完全相同。
3. <font color="red">void write(byte[] b,int off,int len)：</font>将指定 byte 数组中从偏移量 off 开始的 len 个字节写入此输流。
4. <font color="red">public void flush()throws IOException：</font>刷新此输出流并强制写出所有缓冲的输出字节，调用此方法指示应将这些字节立即写入它们预期的目标。
5. <font color="red">public void close() throws IOException：</font>关闭此输出流并释放与该流关联的所有系统资源。

##### （3）、Writer

1. <font color="red">void write(int c)：</font>写入单个字符。要写入的字符包含在给定整数值的 16 个低位中，16 高位被忽略。 即写入0 到 65535 之间的Unicode码。
2. <font color="red">void write(char[] cbuf)：</font>写入字符数组。
3. <font color="red">void write(char[] cbuf,int off,int len)：</font>写入字符数组的某一部分。从off开始，写入len个字符
4. <font color="red">void write(String str)：</font>写入字符串。
5. <font color="red">void write(String str,int off,int len)：</font>写入字符串的某一部分。
6. <font color="red">void flush()：</font>刷新该流的缓冲，则立即将它们写入预期目标。
7. <font color="red">public void close() throws IOException：</font>关闭此输出流并释放与该流关联的所有系统资源。

## 3、节点流(或文件流)

### ①、介绍

1. 字节流操作字节，比如：.mp3，.avi，.rmvb，mp4，.jpg，.doc，.ppt
2. 字符流操作字符，只能操作普通文本文件。最常见的文本文件：.txt，.java，.c，.cpp 等语言的源代码。尤其注意 .doc,excel,ppt 这些不是文本文件。
3. 单纯只是复制而不是读取的话，文本文件可以使用字符流和字节流，只是字节流效率低点
4. <font color="red">但是非文本文件不可以使用字符流</font>
5. 定义文件路径时，注意：可以用 `/` 或者 `\`。
6. 在<font color="red">写入</font>一个文件时，如果使用构造器 `FileOutputStream(file)`，则<font color="red">目录下有同名文件将被覆盖。</font>
7. 如果使用构造器 `FileOutputStream(file,true)`，则目录下的同名文件不会被覆盖，<font color="red">在文件内容末尾追加内容。</font>
8. 在<font color="red">读取</font>文件时，必须保证该文件已存在，否则报异常。
9. 节点流分类：
   1.  字节输入流（FileInputStream）：`read(byte[] buffer)`
   2.  字节输出流（FileOutputStream）：`write(byte[] buffer, 0, len)`
   3.  字符输入流（FileReader）：`read(char[] buffer)`
   4.  字符输出流（FileWriter）：`write(char[] buffer, 0, len)`

### ②、节点流 FileReader（字符输入流）

1. 从磁盘（文件）中读取文件到内存
2. `read()`：返回读入的一个字符，如果达到文件末尾，返回-1
3. 读入的文件一定要存在，不然会报 `java.io.FileNotFoundException` 异常
4. 异常处理：throws IOException，<font color="red">不能这么抛出，可能导致流无法关闭</font>

```java
public class Demo01 {
	public static void main(String[] args) throws IOException {
		// 1、实例化File类的对象，指明要操作的文件
		File file = new File("hello.txt");
		// 2、提供具体的流（FileReader：字符输入流），需抛出异常
		FileReader fr = new FileReader(file);

		// 3、数据的读入，需抛出异常
		// read()：返回读入的一个字符，如果达到文件末尾，返回-1

		// 方式一：
		// 将读取的数据赋值给data，read()自带迭代
//        int data = fr.read();
//        while (data != -1) {
//            // 将data数据强转为char型字符，并输出
//            System.out.print((char) data);
//            // 因read()自带迭代，所以再次赋值并循环
//            data = fr.read();
//        }

		// 方式二：针对方式一语法上的修改，和效率无关
		int data;
		// 将读取的数据赋值给data，read()自带迭代，并判断
		while ( (data = fr.read()) != -1) {
			// 将data数据强转为char型字符，并输出
			System.out.print((char)data);
		}

		// 4、流的关闭操作
		fr.close();
	}
}
```

5. 异常处理：`try-catch-finally`。<font color="red">为了保证资源一定可以执行关闭操作，需要使用 try-catch-finally 处理</font>

```java
// 使用try-catch-finally处理异常
public class Demo01 {
	public static void main(String[] args) {
		// 1、实例化File类的对象，指明要操作的文件
		File file = new File("hello.txt");
		// 创建FileReader类型的fr，留给具体的流和close()使用
		FileReader fr = null;

		try {
			// 2、提供具体的流（FileReader：字符输入流），需抛出异常
			fr = new FileReader(file);

			// 3、数据的读入，需抛出异常
			// read()：返回读入的一个字符，如果达到文件末尾，返回-1
			int data;
			// 将读取的数据赋值给data，read()自带迭代，并判断
			while ( (data = fr.read()) != -1) {
				// 将data数据强转为char型字符，并输出
				System.out.print((char)data);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {

			// 4、流的关闭操作
			try {
				// 判断fr对像是不是空的，若是空则不调用close()方法
				// 因为fr = new FileReader(file);时可能会出现异常，若是此时异常则fr对像为空，若是调用close()会报空指针异常
				if(fr != null){
					fr.close();
				}
			} catch (IOException e) {
				e.printStackTrace();
			}

		}

	}
}
```

6. `read()` 操作升级：使用 `read()` 的重载方法

```java
// read()操作升级：使用read()的重载方法
public class Demo02 {
	public static void main(String[] args) {
		// 1、File类的实例化
		File file = new File("hello.txt");
		// 2、FileReader（字符输入流）流的实例化
		FileReader fr = null;

		try {
			// 2、FileReader（字符输入流）流的实例化
			fr = new FileReader(file);

			// 3、读入的具体操作
			// read(char[] cbuffer)：返回每次读入cbuffer数组中的字符的个数，如果达到文件末尾，返回-1
			// char[5]：每次装入5个字符到数组中
			char[] cbuffer = new char[5];
			int len;
			while ( ( len = fr.read(cbuffer) ) != -1 ){
				// 方式一：
				// 循环判断使用len，即每次循环的次数为装入cbuffer数组的字符的个数
//                for (int i = 0; i < len; i++) {
//                    System.out.print(cbuffer[i]);
//                }

				// 方式二：
				// 读取cbuffer字符数组中的元素，从第0个开始读取，到第len个
				String str = new String(cbuffer,0,len);
				System.out.print(str);
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if ( fr != null ){
				// 4、流资源的关闭
				try {
					fr.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ③、节点流 FileWriter（字符输出流）


1. 从内存中写出数据到磁盘（文件）
2. 输出操作，对应的 File 可以不存在。
	1. 如果不存在，在输出的过程中，会自动创建此文件，并不会报异常
	2. 如果存在，则根据 `FileWriter` 的第二个参数判断是进行覆盖还是添加
	3. <font color="red">第二个参数为空时，默认覆盖原文件</font>

```java
// 如果存在此文件，则覆盖此文件
FileWriter fW01 = new FileWriter(file,false);
// 如果存在此文件，则在源文件后面进行追加
FileWriter fW02 = new FileWriter(file,true);
```

3. `FileWriter` 写出数据

```java
public class Demo03 {
	public static void main(String[] args) {
		// 2、创建FileWriter的对象，用于数据的写出
		FileWriter fW = null;
		
		try {
			// 1、创建File类的对象，指明写出到的文件
			File file = new File("hello.txt");

			// 2、创建FileWriter的对象，用于数据的写出
			fW = new FileWriter(file,true);

			// 3、写出的操作
			fW.write("月海\n");
			fW.write("yue hai\n");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (fW != null){
				// 4、流资源的关闭
				try {
					fW.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
}
```

4. `FileReader` 和 `FileWriter` 实现文本的复制

```java
public class Demo04 {
	public static void main(String[] args) {
		// 2、创建FileReader和FileWriter的对象，用于数据的读入和写出
		FileReader fR = null;
		FileWriter fW = null;

		try {
			// 1、创建File类的对象，指明读入和写出到的文件
			File srcFile = new File("hello.txt");
			File destFile = new File("hello2.txt");

			// 2、创建FileReader和FileWriter的对象，用于数据的读入和写出
			fR = new FileReader(srcFile);
			fW = new FileWriter(destFile,true);

			// 3、读入和写出的操作
			char[] cbuffer = new char[5];
			// 记录每次读入到cbuffer数组中的字符的个数
			int len;
			// 循环读取与复制到cbuffer中，并判断是否达到文件末尾
			while ((len = fR.read(cbuffer)) != -1){
				// 输出cbuffer，从第一个开始输出，输出len个
				fW.write(cbuffer,0,len);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、流资源的关闭
			if(fW != null){
				try {
					fW.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(fR != null){
				try {
					fR.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ④、节点流 FileInputStream（字节输入流）与 FileOutputStream（字节输出流）

1. 使用字节流 FileInputStream 处理文本文件，可能出现乱码
2. 复制图片测试

```java
public class Demo06 {
	public static void main(String[] args)  {
		// 创建FileInputStream类型的fIS，留给具体的流和close()使用
		// 创建FileOutputStream类型的fOS，留给具体的流和close()使用
		FileInputStream fIS = null;
		FileOutputStream fOS = null;

		try {
			// 1、创建File类的对象，指明读入与写出的文件
			File file01 = new File("壁纸.jpg");
			File file02 = new File("壁纸2.jpg");

			// 2、调用FileInputStream和FileOutputStream的构造器且传入参数
			fIS = new FileInputStream(file01);
			fOS = new FileOutputStream(file02);

			// 3、读入与写出的操作
			byte[] buffer = new byte[5];
			int len;
			while ( (len = fIS.read(buffer)) != -1 ){
				fOS.write(buffer);
			}
			System.out.println("复制成功");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、流资源的关闭
			if(fOS != null){
				try {
					fOS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(fIS != null){
				try {
					fIS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

	}
}
```

3. 创建复制图片的方法的测试

```java
// 测试类
public class Demo07 {
	public static void main(String[] args) {
		// 记录复制操作开始的时间
		long start = System.currentTimeMillis();

		// 创建Copy类的对象
		Copy copy = new Copy();

		// 创建并设置起始文件与目标文件的参数
		String srcPath = "壁纸.jpg";
		String destPath = "壁纸2.jpg";

		// 调用复制方法并传递参数
		copy.copyFile(srcPath,destPath);

		// 记录复制操作结束的时间
		long end = System.currentTimeMillis();
		System.out.println("复制花费的时间为：" + (end - start));
	}
}

// Copy类
class Copy{
	// 复制方法
	public void copyFile(String srcPath,String destPath){
		// 创建FileInputStream类型的fIS，留给具体的流和close()使用
		// 创建FileOutputStream类型的fOS，留给具体的流和close()使用
		FileInputStream fIS = null;
		FileOutputStream fOS = null;

		try {
			// 1、创建File类的对象，指明读入与写出的文件
			File file01 = new File(srcPath);
			File file02 = new File(destPath);

			// 2、调用FileInputStream和FileOutputStream的构造器且传入参数
			fIS = new FileInputStream(file01);
			fOS = new FileOutputStream(file02);

			// 3、读入与写出的操作
			byte[] buffer = new byte[5];
			int len;
			while ( (len = fIS.read(buffer)) != -1 ){
				fOS.write(buffer);
			}
			System.out.println("复制成功");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、流资源的关闭
			if(fOS != null){
				try {
					fOS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(fIS != null){
				try {
					fIS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}

}
```

## 4、缓冲流（处理流之一）

### ①、介绍

1. <font color="red">为了提高数据读写的速度</font>，Java API 提供了带缓冲功能的流类，在使用这些流类时，会创建一个内部缓冲区数组，缺省使用 <font color="red">8192 个字节(8Kb)的缓冲区</font>。
2. 缓冲流要“套接”在相应的节点流之上，根据数据操作单位可以把缓冲流分为：
	1. 字节输入流（BufferedInputStream）：`read(byte[] buffer)`
	2. 字节输出流（BufferedOutputStream）：`write(byte[] buffer, 0, len)` / `flush()`
	3. 字符输入流（BufferedReader）：`read(char[] buffer)` / `readLine()`
	4. 字符输出流（BufferedWriter）：`write(char[] buffer, 0, len)` / `flush()`

### ②、缓冲流处理流程

1. 当读取数据时，数据按块读入缓冲区，其后的读操作则直接访问缓冲区
2. 当使用 BufferedInputStream 读取字节文件时，BufferedInputStream 会一次性从文件中读取 8192 个(8Kb)字节数组，存在缓冲区中，直到缓冲区装满了，才重新从文件中读取下一个 8192 个字节数组。
3. 向流中写入字节时，不会直接写到文件，先写到缓冲区中直到缓冲区写满，BufferedOutputStream 才会把缓冲区中的数据一次性写到文件里。<font color="red">使用方法flush()可以强制将缓冲区的内容全部写入输出流</font>
4. 关闭流的顺序和打开流的顺序相反。只要关闭最外层流即可，关闭最外层流也会相应关闭内层节点流
5. `flush()` 方法的使用：手动将 buffer 中内容写入文件
6. 如果是带缓冲区的流对象的 `close()` 方法，不但会关闭流，还会在关闭流之前刷新缓冲区，关闭后不能再写出

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F48、缓冲流.png)

### ③、缓冲流（字节输入输出流）

```java
// 实现非文本文件的复制
public class Demo01 {
	public static void main(String[] args) {
		BufferedInputStream bIS = null;
		BufferedOutputStream bOS = null;
		try {
			// 1、造文件
			File file01 = new File("壁纸.jpg");
			File file02 = new File("壁纸2.jpg");

			// 2、造流
			//    2.1、造节点流
			FileInputStream fIS = new FileInputStream(file01);
			FileOutputStream fOS = new FileOutputStream(file02);
			//    2.2、造缓冲流 --> 需与节点流，字节或者字符
			bIS = new BufferedInputStream(fIS);
			bOS = new BufferedOutputStream(fOS);

			// 3、复制的细节
			byte[] buffer = new byte[10];
			int len;
			while ( (len = bIS.read(buffer)) != -1 ){
				bOS.write(buffer,0,len);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、关闭
			//    要求：先关闭外层的流，再关闭内层的流
			if(bOS != null){
				try {
					bOS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(bIS != null){
				try {
					bIS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			//    说明：关闭外层的流的同时，内层流也会自动的进行关闭，所以内层流的关闭，我们可以省略
			// fOS.close();
			// fIS.close();
		}

	}
}
```

### ④、缓冲流（字符输入输出流）


```java
public class Demo02 {
	public static void main(String[] args) {
		BufferedReader bR = null;
		BufferedWriter bW = null;
		try {
			// 2.2缓冲流（2.1节点流（1文件对象））
			// bR = new BufferedReader(new FileReader(new File("hello.txt")));
			// bW = new BufferedWriter(new FileWriter(new File("hello2.txt")));

			// 更简单的写法：
			// 2.2缓冲流（2.1节点流（文件路径））
			bR = new BufferedReader(new FileReader("hello.txt"));
			bW = new BufferedWriter(new FileWriter("hello2.txt"));

			// 3、复制的细节
			// 方式一：使用char[]数组
//            char[] buffer = new char[10];
//            int len;
//            while ( (len = bR.read(buffer)) != -1 ){
//                bW.write(buffer,0,len);
//            }

			// 方式二：使用String
			String data;
			while ( (data = bR.readLine()) != null ){
				// 方法一：data中不包含换行符
				// bW.write(data);

				// 方法二：
				bW.write(data);
				// 提供换行的操作
				bW.newLine();
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、关闭
			//    要求：先关闭外层的流，再关闭内层的流
			if(bR != null){
				try {
					bR.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(bW != null){
				try {
					bW.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ⑤、加密解密


```java
// 加密
public class Demo03 {
	public static void main(String[] args) throws IOException {

		FileInputStream fIS = null;
		FileOutputStream fOS = null;

		try {
			fIS = new FileInputStream("壁纸.jpg");
			fOS = new FileOutputStream("壁纸 - 加密.jpg");

			byte[] buffer = new byte[20];
			int len;
			while ( (len = fIS.read(buffer)) != -1 ){
				// 对字节数组进行修改
				for (int i = 0; i < len; i++) {
					// ^：异或
					buffer[i] = (byte) (buffer[i] ^ 5);
				}
				fOS.write(buffer,0,len);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 关闭
			if(fOS != null){
				fOS.close();
			}
			if(fIS != null){
				fIS.close();
			}
		}

	}
}
```

```java
// 解密
public class Demo04 {
	public static void main(String[] args) throws IOException {

		FileInputStream fIS = null;
		FileOutputStream fOS = null;

		try {
			fIS = new FileInputStream("壁纸 - 加密.jpg");
			fOS = new FileOutputStream("壁纸 - 解密.jpg");

			byte[] buffer = new byte[20];
			int len;
			while ( (len = fIS.read(buffer)) != -1 ){
				// 对字节数组进行修改
				for (int i = 0; i < len; i++) {
					// ^：异或的异或等于他本身
					buffer[i] = (byte) (buffer[i] ^ 5);
				}
				fOS.write(buffer,0,len);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 关闭
			if(fOS != null){
				fOS.close();
			}
			if(fIS != null){
				fIS.close();
			}
		}

	}
}
```

## 5、转换流（处理流之二，属于字符流）

### ①、介绍

1. 转换流提供了在字节流和字符流之间的转换
2. 字节流中的数据都是字符时，转成字符流操作更高效。
3. 很多时候我们使用转换流来处理文件乱码问题。实现编码和解码的功能。
4. Java API提供了两个转换流：
   1. <font color="red">InputStreamReader：将InputStream（字节输入流）转换为Reader（字符输入流）</font>
   2. <font color="red">OutputStreamWriter：将Writer（字符输出流）转换为OutputStream（字节输出流）</font>

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F50、转换流.png)

### ②、InputStreamReader（字符输入流）

1. <font color="red">实现将字节的输入流按指定字符集转换为字符的输入流。</font>
2. 需要和 InputStream “套接”。
3. 构造器：

```java
public InputStreamReader(InputStream in)
```

```java
public InputSreamReader(InputStream in,String charsetName)
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F49、转换流：InputStreamReader.png)

4. 文件的转码读取

```java
public class Demo01 {
	public static void main(String[] args) {
		InputStreamReader iSR = null;
		try {
			// 创建节点流对象，并设定文件的位置
			FileInputStream fIS = new FileInputStream("hello.txt");
			// 转换流：不写参数则使用系统默认的字符集 --> UTF-8
			// InputStreamReader iSR = new InputStreamReader(fIS);
			// 转换流：参数2指明了字符集：具体使用哪个字符集取决于文件保存时使用的字符集
			iSR = new InputStreamReader(fIS,"UTF-8");

			// 具体的处理
			char[] cbuffer = new char[20];
			int len;
			while ( (len = iSR.read(cbuffer)) != -1 ){
				String str = new String(cbuffer,0,len);
				System.out.print(str);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 关闭
			if(iSR != null){
				try {
					iSR.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ③、OutputStreamWriter（字符输出流）

1. <font color="red">实现将字符的输出流按指定字符集转换为字节的输出流。</font>
2. 需要和 OutputStream“套接”。
3. 构造器：

```java
public OutputStreamWriter(OutputStream out)
```

```java
public OutputSreamWriter(OutputStream out,String charsetName)
```

4. 文件的复制

```java
public class Demo02 {
	public static void main(String[] args) {

		InputStreamReader iSR = null;
		OutputStreamWriter oSW = null;

		try {
			// 1、造文件，造节点流流
			FileInputStream fIS = new FileInputStream("hello.txt");
			FileOutputStream fOS = new FileOutputStream("hello - GBK.txt");

			// 2、造转换流
			iSR = new InputStreamReader(fIS,"utf-8");
			oSW = new OutputStreamWriter(fOS,"gbk");

			// 3、具体的读写过程
			char[] cbuffer = new char[20];
			int len;
			while ( (len = iSR.read(cbuffer)) != -1 ){
				oSW.write(cbuffer,0,len);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 4、关闭
			if(oSW != null){
				try {
					oSW.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if(iSR != null){
				try {
					iSR.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

	}
}
```

### ④、补充：字符编码

1. 编码：<font color="red">字符串 --> 字节数组</font>
2. 解码：<font color="red">字节数组 --> 字符串</font>
3. 转换流的编码应用
	1. 可以将字符按指定编码格式存储
	2. 可以对文本数据按指定编码格式来解读
	3. 指定编码表的动作由构造器完成
4. 编码表的由来：计算机只能识别二进制数据，早期由来是电信号。为了方便应用计算机，让它可以识别各个国家的文字。就将各个国家的文字用数字来表示，并一一对应，形成一张表。这就是编码表。
5. 常见的编码表:

|编码表|解释|字节长度|
|--|--|--|
|ASCII|美国标准信息交换码|用一个字节的7位可以表示|
|ISO8859-1|拉丁码表。欧洲码表|用一个字节的8位表示|
|GB2312|中国的中文编码表|最多两个字节编码所有字符|
|GBK|中国的中文编码表升级<br/>融合了更多的中文文字符号|最多两个字节编码|
|Unicode|国际标准码，融合了目前人类使用的所有字符<br/>为每个字符分配唯一的字符码|所有的文字都用两个字节来表示|
|UTF-8|变长的编码方式|可用1-4个字节来表示一个字符|

6. <font color="red">在 Unicode 出现之前，所有的字符集都是和具体编码方案绑定在一起的（即字符集 ≈ 编码方式）</font>，都是直接将字符和最终字节流绑定死了。
7. 在标准 UTF-8 编码中，超出基本多语言范围（BMP-Basic Multilingual Plane）的字符被编码为 4 字节格式，但是在修正的 UTF-8 编码中，他们由代理编码对（surrogatepairs）表示，然后这些代理编码对在序列中分别重新编码，结果标准 UTF-8 编码中需要 4 个字节的字符，在修正的 UTF-8 编码中将需要 6 个字节
8. GBK 等双字节编码方式，用最高位是 1 或 0 表示两个字节和一个字节。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F51、在Unicode出现之前的编码.png)

9. Unicode 不完美，这里就有三个问题:
	1. 一个是，我们已经知道，英文字母只用一个字节表示就够了
	2. 第二个问题是如何才能区别 Unicode 和 ASCII？计算机怎么知道两个字节表示一个符号，而不是分别表示两个符号呢？
	3. 第三个，如果和 GBK 等双字节编码方式一样，用最高位是 1 或 0 表示两个字节和一个字节，就少了很多值无法用于表示字符，不够表示所有字符。Unicode 在很长一段时间内无法推广，直到互联网的出现。
10. 面向传输的众多 UTF（UCS Transfer Format）标准出现了，顾名思义，<font color="red">UTF-8 就是每次 8 个位传输数据，UTF-16 就是每次 16 个位。</font>这是为传输而设计的编码，并使编码无国界，这样就可以显示全世界上所有文化的字符了。
11. <font color="red">Unicode 只是定义了一个庞大的、全球通用的字符集，并为每个字符规定了唯一确定的编号，具体存储成什么样的字节流，取决于字符编码方案。</font>推荐的 Unicode 编码是 UTF-8 和 UTF-16。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F52、字符编码：Unicode与UTF-8编码方式.png)

12. ANSI 编码，通常指的是平台的默认编码，例如英文操作系统中是 ISO-8859-1，中文系统是 GBK
13. Unicode 字符集只是定义了字符的集合和唯一编号，Unicode 编码，则是对 UTF-8、UCS-2/UTF-16 等具体编码方案的统称而已，并不是具体的编码方案。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F53、字符编码：ANSI编码.png)

## 6、标准输入、输出流（处理流之三）

1. <font color="red">System.in</font>：系统标准的输入流，默认从键盘输入
2. <font color="red">System.out</font>系统标准的输出流，默认从控制台输出
3. `System.in` 的类型是 `InputStream`
4. `System.out` 的类型是 `PrintStream`，其是 `OutputStream` 的子类 `FilterOutputStream` 的子类
5. `System` 类的 `setIn(InputStream is)` / `setOut(PrintStream ps)` 方法重新指定输入和输出的流
6. 重定向：通过 `System` 类的 `setIn`，`setOut` 方法对默认设备进行改变。
	1. `public static void setIn(InputStream in)`
	2. `public static void setOut(PrintStream out)`
7. 练习：从键盘输入字符串，要求将读取到的整行字符串转成大写输出。然后继续进行输入操作，直至当输入 `e` 或者 `exit` 时，退出程序。

```java
// 使用System.in
// System.in --> 转换至：BufferedReader的readLine
public class Demo01 {
	public static void main(String[] args) {
		BufferedReader bR = null;
		try {
			// 把“标准”输入流(键盘输入)这个字节流包装成字符流
			InputStreamReader iSR = new InputStreamReader(System.in);
			// 再包装成缓冲流
			bR = new BufferedReader(iSR);

			// 具体的处理内容
			String data = null;
			// 一直循环，直到用户输入e或者exit
			while (true){
				System.out.print("请输入字符串（退出输入e或者exit）：");
				// 将缓冲流获取的字符串复制给data
				data = bR.readLine();
				// 判断书否结束
				if("e".equalsIgnoreCase(data) || "exit".equalsIgnoreCase(data)){
					System.out.println("程序结束");
					break;
				}
				// 调用String的toUpperCase()方法将字符串小写字符转换为大写
				String upperCase = data.toUpperCase();
				System.out.println(upperCase);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// 关闭流
			if(bR != null){
				try {
					bR.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
}
```

## 7、打印流（处理流之四）

1. 实现将<font color="red">基本数据类型</font>的数据格式转化为<font color="red">字符串</font>输出
2. 打印流：<font color="red">PrintStream</font> 和 <font color="red">PrintWriter</font>
   1. 提供了一系列重载的 `print()` 和 `println()` 方法，用于多种数据类型的输出
   2. `PrintStream` 和 `PrintWriter` 的输出不会抛出 `IOxception` 异常
   3. `PrintStream` 和 `PrintWriter` 有自动 `flush` 功能
   4. `PrintStream` 打印的所有字符都使用平台的默认字符编码转换为字节。在需要写入字符而不是写入字节的情况下，应该使用 `PrintWriter` 类。
   5. `System.out` 返回的是 `PrintStream` 的实例

```java
// 将从控制台输出改为从文件输出
public class Demo02 {
	public static void main(String[] args) {

		PrintStream ps = null;
		try {
			// // 造文件，造节点流流
			FileOutputStream fos = new FileOutputStream(new File("text.txt"));
			// 创建打印输出流，设置为自动刷新模式(写入换行符或字节 '\n' 时都会刷新输出缓冲区)
			ps = new PrintStream(fos, true);
			// 把标准输出流从控制台输出改成文件输出
			if (ps != null) {
				System.setOut(ps);
			}

			// 循环输出ASCII字符
			for (int i = 0; i <= 255; i++) {
				// 将字节转换为字符串，即输出各ASCII代表的字符
				System.out.print((char) i);
				// 每50个数据一行
				if (i % 50 == 0) {
					// 换行
					System.out.println();
				}
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			// 关闭流
			if (ps != null) {
				ps.close();
			}
		}

	}
}
```

## 8、数据流（处理流之五）

1. 为了方便地操作 Java 语言的基本数据类型和 String 的数据，可以使用数据流。
2. 数据流有两个类：(用于读取和写出基本数据类型、String 类的数据）
	1. <font color="red">DataInputStream 和 DataOutputStream</font>
	2. <font color="red">分别“套接”在 InputStream 和 OutputStream 子类的流上</font>
3. DataInputStream 中的方法

|方法|类型|说明|
|--|--|--|
|<font color="red">byte readByte()</font>|<font color="red">整数</font>|8位、有符号的，以二进制补码表示的整数|
|<font color="red">short readShort()</font>|<font color="red">整数</font>|16 位、有符号的以二进制补码表示的整数|
|<font color="red">int readInt()</font>|<font color="red">整数</font>|32位、有符号的以二进制补码表示的整数|
|<font color="red">long readLong()</font>|<font color="red">整数</font>| 64 位、有符号的以二进制补码表示的整数|
|<font color="red">float readFloat()</font>|<font color="red">浮点数</font>|单精度、32位、符合IEEE 754标准的浮点数|
|<font color="red">double readDouble()</font>|<font color="red">浮点数</font>|双精度、64 位、符合 IEEE 754 标准的浮点数|
|<font color="red">boolean readBoolean()</font>|<font color="red">布尔型</font>|只有两个取值：true 和 false|
|<font color="red">char readChar()</font>|<font color="red">字符型</font>|单一的 16 位 Unicode 字符，可以储存任何字符|
|<font color="red">void readFully(byte[] b)</font>|<font color="red">字符型数组</font>|char的数组，可以储存任何字符|
|<font color="red">String readUTF()</font>|<font color="red">字符串</font>|字符串|

4. DataOutputStream 中的方法：<font color="red">将上述的方法的 read 改为相应的 write 即可。</font>
5. 将内存中的字符串、基本数据类型的变量写出到文件中

```java
// 将内存中的字符串、基本数据类型的变量写出到文件中
// 存入后可能乱码，需要使用数据流读取才可
public class Demo03 {
	public static void main(String[] args) {

		DataOutputStream dOS = null;

		try {
			// 造文件（追加）、造流
			dOS = new DataOutputStream(new FileOutputStream("月海.txt",true));

			// 具体的处理
			dOS.writeUTF("月海");
			// 刷新内存，将内存中的数据全部存入文件
			dOS.flush();
			dOS.writeInt(16);
			dOS.flush();
			dOS.writeBoolean(true);
			dOS.flush();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(dOS != null){
				// 关闭流
				try {
					dOS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

	}
}
```

6. 将文件中储存的基本数据类型变量和字符串读取但内存中，保存在变量中

```java
// 将文件中储存的基本数据类型变量和字符串读取但内存中，保存在变量中
public class Demo04 {
	public static void main(String[] args) throws IOException {

		DataInputStream dIS = null;

		try {
			// 造文件、造流
			dIS = new DataInputStream(new FileInputStream("月海.txt"));

			// 具体的方法
			// 读取的不同类型的数据的顺序要和存入的顺序一致
			String name = dIS.readUTF();
			int age = dIS.readInt();
			Boolean sex = dIS.readBoolean();

			System.out.println("姓名：" + name + "\n年龄：" + age + "\n性别：" + sex);

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(dIS != null){
				// 关闭
				dIS.close();
			}
		}

	}
}
```

## 9、对象流（处理流之六）

### ①、介绍

1. <font color="red">ObjectInputStream</font> 和 <font color="red">OjbectOutputSteam</font>
2. 用于存储和读取<font color="red">基本数据类型数据</font>或<font color="red">对象</font>的处理流。它的强大之处就是可以把Java中的对象写入到数据源中，也能把对象从数据源中还原回来。
3. 序列化：用 `ObjectOutputStream` 类<font color="red">保存</font>基本类型数据或对象的机制
4. 反序列化：用 `ObjectInputStream` 类<font color="red">读取</font>基本类型数据或对象的机制
5. `ObjectOutputStream` 和 `ObjectInputStream` 不能序列化 <font color="red">static</font> 和 <font color="red">transient</font> 修饰的成员变量

### ②、对象的序列化

1. **<font color="red">对象序列化机制</font>允许把内存中的 Java 对象转换成平台无关的二进制流，从而允许把这种二进制流持久地保存在磁盘上，或通过网络将这种二进制流传输到另一个网络节点。当其它程序获取了这种二进制流，就可以恢复成原来的 Java 对象**
2. 序列化的好处在于可将任何实现了 Serializable 接口的对象转化为<font color="red">字节数据</font>，使其在保存和传输时可被还原
3. 序列化是 RMI（Remote Method Invoke – 远程方法调用）过程的参数和返回值都必须实现的机制，而 RMI 是 JavaEE 的基础。因此序列化机制是JavaEE 平台的基础
4. 如果需要让某个对象支持序列化机制，则必须让对象所属的类及其属性是可序列化的，为了让某个类是可序列化的，该类必须实现如下两个接口之一。否则，会抛出 NotSerializableException 异常
	1. <font color="red">Serializable</font>
	2. Externalizable
5. 凡是实现 Serializable 接口的类都有一个表示序列化版本标识符的静态变量：
	1. <font color="red">private static final long serialVersionUID;</font>
	2. serialVersionUID 用来表明类的不同版本间的兼容性。简言之，其目的是以序列化对象进行版本控制，有关各版本反序列化时是否兼容。
	3. 如果类没有显示定义这个静态常量，它的值是Java运行时环境根据类的内部细节自动生成的。<font color="red">若类的实例变量做了修改，serialVersionUID 可能发生变化</font>。故建议，显式声明。
6. 简单来说，Java 的序列化机制是通过在运行时判断类的 serialVersionUID 来验证版本一致性的。在进行反序列化时，JVM 会把传来的字节流中的 serialVersionUID 与本地相应实体类的 serialVersionUID 进行比较，如果相同就认为是一致的，可以进行反序列化，否则就会出现序列化版本不一致的异常。(InvalidCastException)

### ③、使用对象流序列化对象

1. 若某个类实现了 Serializable 接口，该类的对象就是可序列化的：
	1. <font color="red">创建一个 ObjectOutputStream</font>
	2. <font color="red">调用 ObjectOutputStream 对象的 writeObject(对象) 方法输出可序列化对象</font>
	3. <font color="red">注意写出一次，操作flush()一次</font>
2. 反序列化
	1. <font color="red">创建一个 ObjectInputStream</font>
	2. <font color="red">调用 readObject() 方法读取流中的对象</font>
3. 强调：如果某个类的属性不是基本数据类型或 String 类型，而是另一个引用类型，那么这个引用类型必须是可序列化的，否则拥有该类型的Field 的类也不能序列化

### ④、序列化与反序列化 String 对象

1. 序列化

```java
// 序列化过程：将内存中的java对象保存到磁盘中或通过网络传输出去
// 使用OjbectOutputSteam实现
public class Demo01 {
	public static void main(String[] args) {

		ObjectOutputStream oOS = null;

		try {
			// 1、2、造流、造文件
			oOS = new ObjectOutputStream(new FileOutputStream("hello.txt"));

			// 3、写入对象
			oOS.writeObject(new String("月海"));
			// 刷新操作，把内存中的缓存写入磁盘
			oOS.flush();

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(oOS != null){
				// 4、关闭
				try {
					oOS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}

			}
		}

	}
}
```

2. 反序列化

```java
// 反序列化过程：将磁盘文件中的对象还原为内存中的一个java对象
// 使用ObjectInputStream实现
public class Demo02 {
	public static void main(String[] args)  {

		ObjectInputStream oIS = null;

		try {
			// 1、2、造流、造文件
			oIS = new ObjectInputStream(new FileInputStream("hello.txt"));

			// 3、读取对象
			Object obj =  oIS.readObject();
			String str = (String) obj;
			System.out.println(str);

		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} finally {
			if(oIS != null){
				//4、关闭
				try {
					oIS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ⑤、序列化与反序列化自定义对象


1. 要想一个 Java 对象时可序列化的，需要满足相应的要求
	1. 实现 Serializable 接口（没有抽象方法：标识接口）
	2. 当前类需要提供一个全局常量：serialVersionUID
	3. 除了当前 Person 类需要实现 Serializable 接口以外，还必须保证其内部类所有属性也必须是可序列化的（默认情况下，基本数据类型可序列化）
2. 自定义类

```java
// 自定义Person类
// 要想一个Java对象时可序列化的，需要满足相应的要求:
//     1、实现Serializable接口（没有抽象方法：标识接口）
//     2、当前类需要提供一个全局常量：serialVersionUID
//     3、除了当前Person类需要实现Serializable接口以外，还必须保证其内部类所有属性也必须是可序列化的（默认情况下，基本数据类型可序列化）
public class Person implements Serializable {
	// 实现可序列化需要提供的全局常量，值随意，需要long类型
	public static final long serialVersionUID = 546789876543567L;

	private String name;
	private int age;

	public Person() { }
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public String getName() { return name; }
	public void setName(String name) { this.name = name; }

	public int getAge() { return age; }
	public void setAge(int age) { this.age = age; }

	@Override
	public String toString() {
		return "Person{" +
				"name='" + name + '\'' +
				", age=" + age +
				'}';
	}
}
```

3. 序列化

```java
public class Demo03 {
	public static void main(String[] args) {

		ObjectOutputStream oOs = null;

		try {
			// 1、2、造文件、造流
			oOs = new ObjectOutputStream(new FileOutputStream("hello.txt"));

			// 3、写入对象
			//    写入String对象
			oOs.writeObject(new String("月海"));
			//    刷新操作，把内存中的缓存写入磁盘
			oOs.flush();
			//    写入Person对象
			oOs.writeObject(new Person("言",14));
			oOs.flush();
			oOs.writeObject(new Person("月海",16));
			oOs.flush();

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(oOs != null){
				// 4、关闭
				try {
					oOs.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

4. 反序列化

```java
public class Demo04 {
	public static void main(String[] args) {

		ObjectInputStream oIS = null;

		try {
			// 1、2、造文件、造流
			oIS = new ObjectInputStream(new FileInputStream("hello.txt"));

			// 3、读取对象
			//    读取时的顺序依然要和保存的顺序相同
			String str = (String) oIS.readObject();
			Person p1 = (Person) oIS.readObject();
			Person p2 = (Person) oIS.readObject();

			System.out.println(str);
			System.out.println(p1);
			System.out.println(p2);

		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} finally {
			if(oIS != null){
				// 4、关闭
				try {
					oIS.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ⑥、谈谈对 `java.io.Serializable` 接口的理解，我们知道它用于序列化，是空方法接口，还有其它认识吗？

1. 实现了 Serializable 接口的对象，可将它们转换成一系列字节，并可在以后完全恢复回原来的样子。<font color="red">这一过程亦可通过网络进行。这意味着序列化机制能自动补偿操作系统间的差异。</font>换句话说，可以先在Windows机器上创建一个对象，对其序列化，然后通过网络发给一台 Unix 机器，然后在那里准确无误地重新“装配”。不必关心数据在不同机器上如何表示，也不必关心字节的顺序或者其他任何细节。
2. 由于大部分作为参数的类如 String、Integer 等都实现了 `java.io.Serializable` 的接口，也可以利用多态的性质，作为参数使接口更灵活。

## 10、随机存取文件流（RandomAccessFile 类）

### ①、介绍

1. `RandomAccessFile` 声明在 `java.io` 包下，但直接继承于 `java.lang.Object` 类。并且它实现了 `DataInput`、`DataOutput` 这两个接口，也就意味着这个类<font color="red">既可以读也可以写</font>。
2. `RandomAccessFile` 类支持 “随机访问” 的方式，程序可以直接跳到文件的任意地方来读、写文件
	1. 支持只访问文件的部分内容
	2. 可以向已存在的文件后追加内容
3. `RandomAccessFile` 对象包含一个记录指针，用以标示当前读写处的位置
4. `RandomAccessFile` 类对象可以自由移动记录指针：
   1. <font color="red">long getFilePointer()</font>：获取文件记录指针的当前位置
   2. <font color="red">void seek(long pos)</font>：将文件记录指针定位到 pos 位置
5. 构造器：

```java
public RandomAccessFile(File file, String mode) 
```

```java
public RandomAccessFile(String name, String mode)
```

6. 创建 `RandomAccessFile` 类实例需要指定一个 `mode` 参数，该参数指定 `RandomAccessFile` 的访问模式：
	1. <font color="red">r: 以只读方式打开</font>
	2. <font color="red">rw：打开以便读取和写入</font>
	3. <font color="red">rwd:打开以便读取和写入；同步文件内容的更新</font>
	4. <font color="red">rws:打开以便读取和写入；同步文件内容和元数据的更新</font>
7. 如果模式为只读r。则不会创建文件，而是会去读取一个已经存在的文件，如果读取的文件不存在则会出现异常。 如果模式为 rw 读写。如果文件不存在则会去创建文件，如果存在则不会创建。
8. 如果 `RandomAccessFile` 类作为输出流时，写出到的文件如果不存在，则在执行过程中自动创建。如果写出到的文件存在，则会对原有文件内容进行覆盖（默认情况下，从头开始一个个字符的进行覆盖）
9. `RandomAccessFile` 类：我们可以用 `RandomAccessFile` 这个类，来实现一个<font color="red">多线程断点下载</font>的功能，用过下载工具的朋友们都知道，下载前都会建立<font color="red">两个临时文件</font>，一个是与被下载文件大小相同的空文件，另一个是记录文件指针的位置文件，每次暂停的时候，都会保存上一次的指针，然后断点下载的时候，会继续从上一次的地方下载，从而实现断点下载或上传的功能，有兴趣的朋友们可以自己实现下。

### ②、RandomAccessFile 实现文件的复制

```java
public class Demo01 {
	public static void main(String[] args) {

		RandomAccessFile rAF01 = null;
		RandomAccessFile rAF02 = null;

		try {
			// 1、造文件
			// 2、造流
			//    使用rAF01读取文件，使用rAF02储存文件
			/**
			* r:  以只读方式打开
			* rw：打开以便读取和写入
			* rwd:打开以便读取和写入；同步文件内容的更新
			* rws:打开以便读取和写入；同步文件内容和元数据的更新
			*/
			rAF01 = new RandomAccessFile(new File("壁纸.jpg"),"r");
			rAF02 = new RandomAccessFile(new File("壁纸2.jpg"),"rw");

			// 3、复制的具体操作
			byte[] buffer = new byte[1024];
			int len;
			while ( (len = rAF01.read(buffer)) != -1 ){
				rAF02.write(buffer,0,len);
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(rAF02 != null){
				// 4、关闭
				try {
					rAF02.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			if(rAF01 != null){
				try {
					rAF01.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

### ③、RandomAccessFile 实现数据的插入

1. 一般来说对文件的操作都是追加，插入操作效率低

```java
// 使用RandomAccessFile实现数据的插入效果
public class Demo02 {
	public static void main(String[] args) {

		RandomAccessFile rAF = null;

		try {
			// 1、2、造文件、造流
			rAF = new RandomAccessFile(new File("hello.txt"),"rw");

			// 3、具体的方法
			// 将指针调到角标为3的位置
			rAF.seek(3);
			// 保存指针3后面的所有数据到StringBuilder中
			StringBuilder builder = new StringBuilder((int) new File("hello.txt").length());
			byte[] buffer = new byte[20];
			int len;
			while ( (len = rAF.read(buffer)) != -1 ){
				builder.append(new String(buffer,0,len));
			}
			// 因为上面已经将指针3后面的所有数据到StringBuilder中了、
			// 所以指针已经移动到最后了，为了在指针3后面插入数据
			// 故将指针再次调到角标为3的位置
			rAF.seek(3);
			// 在指针后面覆盖数据
			rAF.write("123".getBytes());

			// 将StringBuilder中的数据写如到文件中
			rAF.write(builder.toString().getBytes());

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (rAF != null){
				// 4、关闭
				try {
					rAF.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}
}
```

## 11、流的基本应用小节

1. 流是用来处理数据的。
2. 处理数据时，一定要先明确数据源，与数据目的地
	1. 数据源可以是文件，可以是键盘。
	2. 数据目的地可以是文件、显示器或者其他设备。
3. 而流只是在帮助数据进行传输,并对传输的数据进行处理，比如过滤处理、转换处理等。

## 12、NIO.2 中 Path、Paths、Files 类的使用

### ①、Java NIO 概述

1. Java NIO (New IO，Non-Blocking IO)是从 Java 1.4 版本开始引入的一套新的 IO API，可以替代标准的 Java IO API。NIO 与原来的 IO 有同样的作用和目的，但是使用的方式完全不同，NIO 支持面向缓冲区的(IO 是面向流的)、基于通道的 IO 操作。<font color="red">NIO 将以更加高效的方式进行文件的读写操作。</font>
2. Java API 中提供了两套 NIO，<font color="red">一套是针对标准输入输出 NIO</font>，<font color="blued">另一套就是网络编程 NIO</font>。
3. `java.nio.channels.Channel`
	1. <font color="blued">FileChannel：处理本地文件</font>
	2. <font color="red">SocketChannel：TCP网络编程的客户端的Channel</font>
	3. <font color="red">ServerSocketChannel:TCP网络编程的服务器端的Channel</font>
	4. <font color="red">DatagramChannel：UDP网络编程中发送端和接收端的Channel</font>
4. <font color="red">NIO. 2：</font>随着 JDK 7 的发布，Java 对 NIO 进行了极大的扩展，增强了对文件处理和文件系统特性的支持，以至于我们称他们为 NIO.2。因为 NIO 提供的一些功能，NIO 已经成为文件处理中越来越重要的部分。

### ②、Path、Paths 和 Files 核心 API

1. 早期的 Java 只提供了一个 File 类来访问文件系统，但 File 类的功能比较有限，所提供的方法性能也不高。而且，<font color="red">大多数方法在出错时仅返回失败，并不会提供异常信息</font>。
2. NIO. 2 为了弥补这种不足，引入了 Path 接口，代表一个平台无关的平台路径，描述了目录结构中文件的位置。<font color="red">Path 可以看成是 File 类的升级版本，实际引用的资源也可以不存在</font>。
3. 在以前 IO 操作都是这样写的:

```java
import java.io.File;

File file = new File("index.html");
```

4. 但在 Java7 中，我们可以这样写：

```java
import java.nio.file.Path; 
import java.nio.file.Paths; 

Path path = Paths.get("index.html");
```

5. 同时，NIO.2 在 java.nio.file 包下还提供了 Files、Paths 工具类，Files 包含了大量静态的工具方法来操作文件；Paths 则包含了两个返回 Path 的静态工厂方法。
6. **Paths 类提供的静态 get() 方法用来<font color="red">获取 Path 对象</font>：**
	1. `static Path get(String first, String … more)` : 用于将多个字符串串连成路径
	2. `static Path get(URI uri)`: 返回指定 uri 对应的 Path 路径

### ③、Path 接口


1. Path 常用方法：

| 方法                              | 介绍                                |
| ------------------------------- | --------------------------------- |
| String toString()               | 返回调用 Path 对象的字符串表示形式              |
| boolean startsWith(String path) | 判断是否以 path 路径开始                   |
| boolean endsWith(String path)   | 判断是否以 path 路径结束                   |
| boolean isAbsolute()            | 判断是否是绝对路径                         |
| Path getParent()                | 返回Path对象包含整个路径，不包含 Path 对象指定的文件路径 |
| Path getRoot()                  | 返回调用 Path 对象的根路径                  |
| Path getFileName()              | 返回与调用 Path 对象关联的文件名               |
| int getNameCount()              | 返回Path 根目录后面元素的数量                 |
| Path getName(int idx)           | 返回指定索引位置 idx 的路径名称                |
| Path toAbsolutePath()           | 作为绝对路径返回调用 Path 对象                |
| Path resolve(Path p)            | 合并两个路径，返回合并后的路径对应的Path对象          |
| File toFile()                   | 将Path转化为File类的对象                  |

### ④、Files 类

1. `java.nio.file.Files` 用于操作文件或目录的工具类。
2. Files 常用方法：

|方法|介绍|
|--|--|
|Path copy(Path src, Path dest, CopyOption … how)|文件的复制|
|Path createDirectory(Path path, FileAttribute<?> … attr)|创建一个目录|
|Path createFile(Path path, FileAttribute<?> … arr)|创建一个文件|
|void delete(Path path)|删除一个文件/目录，如果不存在，执行报错|
|void deleteIfExists(Path path)|Path对应的文件/目录如果存在，执行删除|
|Path move(Path src, Path dest, CopyOption…how)|将 src 移动到 dest 位置|
|long size(Path path)|返回 path 指定文件的大小|

3. Files常用方法：用于判断

|方法|介绍|
|--|--|
|boolean exists(Path path, LinkOption … opts)|判断文件是否存在|
|boolean isDirectory(Path path, LinkOption … opts)|判断是否是目录|
|boolean isRegularFile(Path path, LinkOption … opts)|判断是否是文件|
|boolean isHidden(Path path)|判断是否是隐藏文件|
|boolean isReadable(Path path)|判断文件是否可读|
|boolean isWritable(Path path)|判断文件是否可写|
|boolean notExists(Path path, LinkOption … opts)|判断文件是否不存在|

4. Files常用方法：用于操作内容

| 方法                                                            | 介绍                     |
| ------------------------------------------------------------- | ---------------------- |
| SeekableByteChannel newByteChannel(Path path, OpenOption…how) | 获取与指定文件的连接，how 指定打开方式。 |
| DirectoryStream< Path > newDirectoryStream(Path path)         | 打开 path 指定的目录          |
| InputStream newInputStream(Path path, OpenOption…how)         | 获取 InputStream 对象      |
| OutputStream newOutputStream(Path path, OpenOption…how)       | 获取 OutputStream 对象     |

# 十三、网络编程

## 1、网络编程概述

1. Java 是 Internet 上的语言，它从语言级上提供了对网络应用程序的支持，程序员能够很容易开发常见的网络应用程序。
2. Java 提供的网络类库，可以实现无痛的网络连接，联网的底层细节被隐藏在 Java 的本机安装系统里，由 JVM 进行控制。并且 Java 实现了一个跨平台的网络库，<font color="red">程序员面对的是一个统一的网络编程环境。</font>
3. **计算机网络：**把分布在不同地理区域的计算机与专门的外部设备用通信线路互连成一个规模大、功能强的网络系统，从而使众多的计算机可以方便地互相传递信息、共享硬件、软件、数据信息等资源。
4. **网络编程的目的：**<font color="red">直接或间接地通过网络协议与其它计算机实现数据交换，进行通讯。</font>
5. **网络编程中有两个主要的问题：**
	1. 如何准确地定位网络上一台或多台主机；定位主机上的特定的应用：IP与端口号
	2. 找到主机后如何可靠高效地进行数据传输：网络通信协议

## 2、网络通信要素概述

### ①、如何实现网络中的主机互相通信

1. **通信双方地址：**
	1. <font color="red">IP</font>
	2. <font color="red">端口号</font>
2. **一定的规则（即：网络通信协议。有两套参考模型）**
	1. <font color="red">OSI参考模型</font>：模型过于理想化，未能在因特网上进行广泛推广
	2. <font color="red">TCP/IP参考模型(或TCP/IP协议)</font>：事实上的国际标准。

### ②、网络通信协议

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F58、网络通信协议.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F59、网络通信协议2.png)

## 3、通信要素 1：IP 和端口号

### ①、IP 地址：InetAddress

1. 唯一的标识 Internet 上的计算机（通信实体）
2. 本地回环地址(hostAddress)：`127.0.0.1`，主机名(hostName)：`localhost`
3. IP 地址分类方式1：<font color="red">IPV4</font> 和 <font color="red">IPV6</font>
	1. IPV4：4 个字节组成，4 个 0-255。大概 42 亿，30 亿都在北美，亚洲 4 亿。2011 年初已经用尽。以点分十进制表示，如 `192.168.0.1`
	2. IPV6：128 位（16 个字节），写成 8 个无符号整数，每个整数用四个十六进制位表示，数之间用冒号 `:` 分开，如：`3ffe:3201:1401:1280:c8ff:fe4d:db39:1984`
4. IP 地址分类方式 2：<font color="red">公网地址(万维网使用)</font>和<font color="red">私有地址(局域网使用)</font>。`192.168.` 开头的就是私有址址，范围即为 `192.168.0.0--192.168.255.255`，专门为组织机构内部使用
5. 特点：不易记忆

### ②、端口号

1. 标识正在计算机上运行的**进程（程序）**
2. 不同的进程要有不同的端口号
3. 被规定为一个 16 位的整数 0~65535。
4. 端口分类：
	1. <font color="red">公认端口：</font>0~1023。被预先定义的服务通信占用（如：HTTP占用端口80，FTP占用端口21，Telnet占用端口23）
	2. <font color="red">注册端口：</font>1024~49151。分配给用户进程或应用程序。（如：Tomcat占用端口8080，MySQL占用端口3306，Oracle占用端口1521等）。
	3. <font color="red">动态/私有端口：</font>49152~65535。
5. 端口号与 IP 地址的组合得出一个网络套接字：Socket

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F60、IP和端口号.png)

### ③、InetAddress 类

1. **在 Java 中使用 InetAddress 类代表 IP**
2. Internet 上的主机有两种方式表示地址：
	1. <font color="red">域名(hostName)：</font>www.atguigu.com
	2. <font color="red">IP 地址(hostAddress)：</font>202.108.35.210
3. InetAddress 类主要表示 IP 地址，两个子类：**Inet4Address**、**Inet6Address**。
4. InetAddress 类对象含有一个 Internet 主机地址的域名和 IP 地址：www.atguigu.com 和 202.108.35.210。
5. 域名容易记忆，当在连接网络时输入一个主机的域名后，域名服务器(DNS)负责将域名转化成IP地址，这样才能和主机建立连接：域名解析
6. InetAddress 类没有提供公共的构造器，而是提供了如下几个静态方法来获取InetAddress实例

```java
// 在给定主机名的情况下确定主机的IP地址，如果参数为null,获得的是本机的IP地址
// 如输入：www.baidu.com，返回：www.baidu.com/110.242.68.3
public static InetAddress getByName(String host)

// 获取本机Ip地址
public static InetAddress getLocalHost()
```

6. InetAddress 提供了如下几个常用的方法

```java
public String getHostName()：获取此 IP 地址的（域名）
public String getHostAddress()：返回 IP 地址字符串（以文本表现形式）。

public boolean isReachable(int timeout)：测试是否可以达到该地址
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F61、域名如何转化为IP地址.png)

```java
public class Demo01 {
  public static void main(String[] args) throws UnknownHostException {
	 // 在给定主机名的情况下确定主机的IP地址，如果参数为null,获得的是本机的IP地址
	 // 如输入：www.baidu.com，返回：www.baidu.com/110.242.68.3
	 InetAddress inet01 = InetAddress.getByName("www.baidu.com");
	 System.out.println(inet01);

	 // 获取本机Ip地址
	 InetAddress localHost = InetAddress.getLocalHost();
	 System.out.println(localHost);

	 // 获取www.baidu.com的域名
	 System.out.println(inet01.getHostName());
	 // 获取www.baidu.com的IP地址
	 System.out.println(inet01.getHostAddress());
  }
}
```

## 4、通信要素 2：网络协议

### ①、介绍

1. 网络通信协议：计算机网络中实现通信必须有一些约定，即通信协议，<font color="red">对速率、传输代码、代码结构、传输控制步骤、出错控制等制定标准。</font>
2. 问题：网络协议太复杂：计算机网络通信涉及内容很多，比如指定源地址和目标地址，加密解密，压缩解压缩，差错控制，流量控制，路由控制，如何实现如此复杂的网络协议呢？
3. 通信协议分层的思想：在制定协议时，把复杂成份分解成一些简单的成份，再将它们复合起来。最常用的复合方式是层次方式，即<font color="red">同层间可以通信、上一层可以调用下一层，而与再下一层不发生关系。</font>各层互不影响，利于系统的开发和扩展。

### ②、TCP/IP 协议簇

1. 传输层协议中有两个非常重要的协议：
	1. 传输控制协议：<font color="red">TCP</font>(Transmission Control Protocol)
	2. 用户数据报协议：<font color="red">UDP</font>(User Datagram Protocol)。
2. <font color="red">TCP/IP 以其两个主要协议：传输控制协议(TCP)和网络互联协议(IP)</font>而得名，实际上是一组协议，包括多个具有不同功能且互为关联的协议。
3. IP(Internet Protocol) 协议是网络层的主要协议，支持网间互连的数据通信。
4. TCP/IP 协议模型从更实用的角度出发，形成了高效的四层体系结构，即<font color="red">物理链路层、IP层、传输层和应用层。</font>

### ③、TCP 和 UDP

1. <font color="red">TCP 协议：</font>打电话
	1. 使用 TCP 协议前，须先建立 TCP 连接，形成传输数据通道
	2. 传输前，采用“三次握手”方式，点对点通信，<font color="red">是可靠的</font>
	3. TCP 协议进行通信的两个应用进程：客户端、服务端。
	4. 在连接中可<font color="red">进行大数据量的传输</font>
	5. 传输完毕，需<font color="red">释放已建立的连接，效率低</font>
2. <font color="red">UDP 协议：</font>发短信
	1. 将数据、源、目的封装成数据包，<font color="red">不需要建立连接</font>
	2. 每个数据报的大小限制在64K内
	3. 发送不管对方是否准备好，接收方收到也不确认，故是不可靠的
	4. 可以广播发送
	5. 发送数据结束时<font color="red">无需释放资源，开销小，速度快</font>
3. TCP 三次握手

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F62、TCP三次握手.png)

4. TCP 四次挥手

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F63、TCP四次挥手.png)

### ④、Socket

1. 利用套接字(Socket)开发网络应用程序早已被广泛的采用，以至于成为事实上的标准。
2. <font color="red">网络上具有唯一标识的 IP 地址和端口号组合在一起才能构成唯一能识别的标识符套接字。</font>
3. 通信的两端都要有 Socket，是两台机器间通信的端点。
4. 网络通信其实就是 Socket 间的通信。
5. Socket 允许程序把网络连接当成一个流，数据在两个 Socket 间通过 IO 传输。
6. 一般主动发起通信的应用程序属<font color="red">客户端</font>，等待通信请求的为<font color="red">服务端</font>。
7. Socket分类：
	1. <font color="red">流套接字（stream socket）：使用TCP提供可依赖的字节流服务</font>
	2. <font color="red">数据报套接字（datagram socket）：使用UDP提供“尽力而为”的数据报服务</font>
8. Socket 类的常用构造器：

```java
// 创建一个流套接字并将其连接到指定 IP 地址的指定端口号。
public Socket(InetAddress address,int port)
// 创建一个流套接字并将其连接到指定主机上的指定端口号。
public Socket(String host,int port)
```

9.  Socket 类的常用方法：

| 方法                                         | 介绍                                                                                                                                                   |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| public InputStream <br/>getInputStream()   | 返回此套接字的输入流。可以用于接收网络消息                                                                                                                                |
| public OutputStream <br/>getOutputStream() | 返回此套接字的输出流。可以用于发送网络消息                                                                                                                                |
| public InetAddress <br/>getInetAddress()   | 此套接字连接到的远程 IP 地址；<br/>如果套接字是未连接的，则返回 null。                                                                                                           |
| public InetAddress <br/>getLocalAddress()  | 获取套接字绑定的本地地址。 即本端的IP地址                                                                                                                               |
| public int <br/>getPort()                  | 此套接字连接到的远程端口号；<br/>如果尚未连接套接字，则返回 0。                                                                                                                  |
| public int <br/>getLocalPort()             | 返回此套接字绑定到的本地端口。<br/>如果尚未绑定套接字，则返回 -1。即本端的端口号。                                                                                                        |
| public void <br/>close()                   | 关闭此套接字。<br/>套接字被关闭后，便不可在以后的网络连接中使用（即无法重新连接或重新绑定）。<br/>需要创建新的套接字对象。<br/>关闭此套接字也将会关闭该套接字的 InputStream 和OutputStream。                                   |
| public void <br/>shutdownInput()           | 如果在套接字上调用 shutdownInput() 后从套接字输入流读取内容，则流将返回 EOF（文件结束符）。<br/>即不能在从此套接字的输入流中接收任何数据。                                                                   |
| public void <br/>shutdownOutput()          | 禁用此套接字的输出流。<br/>对于 TCP 套接字，任何以前写入的数据都将被发送，并且后跟 TCP 的正常连接终止序列。<br/>如果在套接字上调用 shutdownOutput() 后写入套接字输出流，则该流将抛出 IOException。 <br/>即不能通过此套接字的输出流发送任何数据。 |

## 5、TCP 网络编程

### ①、基于 Socket 的 TCP 编程

- Java 语言的基于套接字编程分为服务端编程和客户端编程，其通信模型如图所示：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F64、基于TCP的Socket通信.png)

### ②、客户端 Socket 的工作过程

#### Ⅰ、四个基本的步骤

1. <font color="red">创建 Socket：</font>根据指定服务端的 IP 地址或端口号构造 Socket 类对象。若服务器端响应，则建立客户端到服务器的通信线路。若连接失败，会出现异常。
2. <font color="red">打开连接到 Socket 的输入/出流：</font>使用 `getInputStream()` 方法获得输入流，使用 `getOutputStream()` 方法获得输出流，进行数据传输
3. <font color="red">按照一定的协议对 Socket 进行读/写操作：</font>通过输入流读取服务器放入线路的信息（但不能读取自己放入线路的信息），通过输出流将信息写入线程。
4. <font color="red">关闭 Socket：</font>断开客户端到服务器的连接，释放线路

#### Ⅱ、客户端创建 Socket 对象

1. 客户端程序可以使用 Socket 类创建对象，<font color="red">创建的同时会自动向服务器方发起连接。Socket 的构造器是：</font>

```java
// 向服务器(域名是host。端口号为port)发起TCP连接，
// 若成功，则创建Socket对象，否则抛出异常。
Socket(String host,int port)throws UnknownHostException,IOException

// 根据InetAddress对象所表示的IP地址以及端口号port发起连接。
Socket(InetAddress address,int port)throws IOException
```

2. 客户端建立 socketAtClient 对象的过程就是向服务器发出套接字连接请求

### ③、服务器 Socket 的工作过程

#### Ⅰ、四个基本的步骤

1. <font color="red">调用 ServerSocket(int port) ：</font>创建一个服务器端套接字，并绑定到指定端口上。用于监听客户端的请求。
2. <font color="red">调用 accept()：</font>监听连接请求，如果客户端请求连接，则接受连接，返回通信套接字对象。
3. <font color="red">调用该 Socket 类对象的 getOutputStream() 和 getInputStream()：</font>获取输出流和输入流，开始网络数据的发送和接收。
4. <font color="red">关闭 ServerSocket 和 Socket 对象：</font>客户端访问结束，关闭通信套接字。

#### Ⅱ、服务器建立 ServerSocket 对象

1. ServerSocket 对象负责等待客户端请求建立套接字连接，类似邮局某个窗口中的业务员。也就是说，<font color="red">服务器必须事先建立一个等待客户请求建立套接字连接的ServerSocket对象。</font>
2. 所谓“接收”客户的套接字请求，就是 `accept()` 方法会返回一个 Socket 对象

### ④、例题

#### Ⅰ、客户端发送内容给服务端，服务端将内容打印到控制台上

```java
public class Demo02 {

  // 客户端
  @Test
  public void client() {

	 Socket socket = null;
	 OutputStream oS = null;

	 try {
		   // IP
		   InetAddress inet = InetAddress.getByName("127.0.0.1");

		   // 1、创建 Socket，
		   // 根据指定服务端的 IP 地址或端口号构造 Socket 类对象
		   // 若服务器端响应，则建立客户端到服务器的通信线路。若连接失败，会出现异常。
		   socket = new Socket(inet,8899);

		   // 2、打开连接到 Socket 的输入/出流
		   // 使用 getInputStream()方法获得输入流，
		   // 使用getOutputStream()方法获得输出流，进行数据传输
		   oS = socket.getOutputStream();

		   // 3、按照一定的协议对 Socket 进行读/写操作
		   oS.write("你好，我是客户端".getBytes());

	 } catch (IOException e) {
		   e.printStackTrace();
	 } finally {
		   if(oS != null){
			  // 4、关闭 Socket
			  // 断开客户端到服务器的连接，释放线路
			  try {
				 oS.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }

		   if(socket != null){
			  try {
				 socket.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }
	 }

  }

  // 服务器
  @Test
  public void server() {

	 ServerSocket serverSocket = null;
	 Socket socket = null;
	 InputStream iS = null;
	 ByteArrayOutputStream bAOS = null;

	 try {
		   // 1、调用 ServerSocket(int port)，指定自己的端口号
		   // 创建一个服务器端套接字，并绑定到指定端口上。用于监听客户端的请求。
		   serverSocket = new ServerSocket(8899);

		   // 2、调用 accept()：
		   // 监听连接请求，如果客户端请求连接，则接受连接，返回通信套接字对象。
		   socket = serverSocket.accept();

		   // 3、调用该Socket类对象的 getOutputStream() 和 getInputStream ()：
		   // 获取输出流和输入流，开始网络数据的发送和接收。
		   iS = socket.getInputStream();

		   // 不建议这样写，可能会有乱码
//        byte[] buffer = new byte[20];
//        int len;
//        while ( (len = iS.read(buffer)) != -1 ){
//            String str = new String(buffer,0,len);
//            System.out.println(str);
//        }

		   // 4、读取客户端发送过来的数据
		   bAOS = new ByteArrayOutputStream();
		   byte[] buffer = new byte[20];
		   int len;
		   while ( (len = iS.read(buffer)) != -1 ){
			  bAOS.write(buffer,0,len);
		   }
		   // 4.1、打印客户端发送的数据
		   System.out.println(bAOS.toString());
		   // 打印获取的IP地址
		   System.out.println("收到了来自于：" + socket.getInetAddress().getHostAddress() + "的数据");

	 } catch (IOException e) {
		   e.printStackTrace();
	 } finally {

		   if(bAOS != null){
			  // 5、关闭ServerSocket和Socket对象
			  // 客户端访问结束，关闭通信套接字。
			  try {
				 bAOS.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }

		   if(iS != null){
			  try {
				 iS.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }

		   if(socket != null){
			  try {
				 socket.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }

		   if(serverSocket != null){
			  try {
				 serverSocket.close();
			  } catch (IOException e) {
				 e.printStackTrace();
			  }
		   }

	 }

  }

}
```

#### Ⅱ、客户端发送文件给服务端，服务端将文件保存在本地。

- **<font color="red">注意：</font>此处涉及到的异常，应该使用try-catch-finally处理

```java
public class Demo03 {

  // 客户端
  @Test
  public void client() throws IOException {
	 // 1、创建 Socket
	 Socket socket = new Socket(InetAddress.getByName("127.0.0.1"),9090);

	 // 2、打开连接到 Socket 的输入/出流
	 //    2.1、字节输入流
	 FileInputStream fIS = new FileInputStream(new File("../壁纸.jpg"));
	 //    2.2、字节输出流
	 OutputStream oS = socket.getOutputStream();

	 // 3、按照一定的协议对 Socket 进行读/写操作
	 byte[] buffer = new byte[1024];
	 int len;
	 while ( (len = fIS.read(buffer)) != -1 ){
		   // 把数据传出去
		   oS.write(buffer,0,len);
	 }

	 // 4、关闭 Socket
	 oS.close();
	 fIS.close();
	 socket.close();

  }

  // 服务器
  @Test
  public void server() throws IOException {

	 // 1、调用 ServerSocket(int port)，指定自己的端口号
	 ServerSocket serverSocket = new ServerSocket(9090);

	 // 2、调用 accept()：监听连接请求
	 Socket socket = serverSocket.accept();

	 // 3、调用该Socket类对象的 getOutputStream() 和 getInputStream ()
	 //    3.1、字节输入流
	 InputStream iS = socket.getInputStream();
	 //    3.2、字节输出流
	 FileOutputStream fOS = new FileOutputStream(new File("../壁纸2.jpg"));

	 // 4、读取客户端发送过来的数据
	 byte[] buffer = new byte[1024];
	 int len;
	 while ( (len = iS.read(buffer)) != -1 ){
		   fOS.write(buffer,0,len);
	 }

	 // 5、关闭ServerSocket和Socket对象
	 fOS.close();
	 iS.close();
	 socket.close();
	 serverSocket.close();
  }

}
```

#### Ⅲ、从客户端发送文件给服务端，服务端保存到本地。并返回“发送成功”给客户端。并关闭相应的连接。

- **<font color="red">注意：</font>此处涉及到的异常，应该使用try-catch-finally处理

```java
public class Demo04 {

  // 客户端
  @Test
  public void client() throws IOException {
	 // 1、创建 Socket
	 Socket socket = new Socket(InetAddress.getByName("127.0.0.1"),9090);

	 // 2、打开连接到 Socket 的输入/出流
	 //    2.1、字节输入流
	 FileInputStream fIS = new FileInputStream(new File("../壁纸.jpg"));
	 //    2.2、字节输出流
	 OutputStream oS = socket.getOutputStream();

	 // 3、按照一定的协议对 Socket 进行读/写操作
	 byte[] buffer = new byte[1024];
	 int len;
	 while ( (len = fIS.read(buffer)) != -1 ){
		   // 把数据传出去
		   oS.write(buffer,0,len);
	 }

	 // 3.1、关闭客户端的输出流
	 // 因为下面还有要传输或接收的数据，若是不关闭，则会无限循环
	 socket.shutdownOutput();

	 // 4、接受来自于服务器的反馈，并显示到控制台上
	 InputStream socketInputStream = socket.getInputStream();
	 ByteArrayOutputStream bAOS = new ByteArrayOutputStream();
	 byte[] buffer02 = new byte[20];
	 int len02;
	 while ( (len02 = socketInputStream.read(buffer02)) != -1 ){
		   bAOS.write(buffer02,0,len02);
	 }
	 System.out.println(bAOS.toString());

	 // 5、关闭 Socket
	 bAOS.close();
	 socketInputStream.close();
	 oS.close();
	 fIS.close();
	 socket.close();

  }

  // 服务器
  @Test
  public void server() throws IOException {

	 // 1、调用 ServerSocket(int port)，指定自己的端口号
	 ServerSocket serverSocket = new ServerSocket(9090);

	 // 2、调用 accept()：监听连接请求
	 Socket socket = serverSocket.accept();

	 // 3、调用该Socket类对象的 getOutputStream() 和 getInputStream ()
	 //    3.1、字节输入流
	 InputStream iS = socket.getInputStream();
	 //    3.2、字节输出流
	 FileOutputStream fOS = new FileOutputStream(new File("../壁纸2.jpg"));

	 // 4、读取客户端发送过来的数据
	 byte[] buffer = new byte[1024];
	 int len;
	 while ( (len = iS.read(buffer)) != -1 ){
		   fOS.write(buffer,0,len);
	 }
	 System.out.println("图片接收完成");

	 // 5、服务器端给予客户端反馈
	 OutputStream socketOutputStream = socket.getOutputStream();
	 socketOutputStream.write("图片已收到".getBytes());

	 // 6、关闭ServerSocket和Socket对象
	 socketOutputStream.close();
	 fOS.close();
	 iS.close();
	 socket.close();
	 serverSocket.close();
  }

}
```

### ⑤、TCP 网络编程总结

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F65、TCP网络编程.png)

## 6、UDP 网络编程

### ①、介绍

1. 类 `DatagramSocket` 和 `DatagramPacket` 实现了基于 UDP 协议网络程序。
2. UDP 数据报通过数据报套接字 `DatagramSocket` 发送和接收，系统不保证 UDP 数据报一定能够安全送到目的地，也不能确定什么时候可以抵达。
3. `DatagramPacket` 对象封装了 UDP 数据报，在数据报中包含了发送端的 IP 地址和端口号以及接收端的 IP 地址和端口号。
4. UDP 协议中每个数据报都给出了完整的地址信息，因此无须建立发送方和接收方的连接。如同发快递包裹一样。

### ②、常用方法

1. DatagramSocket 类的常用方法：

|方法|详情|
|--|--|
|public DatagramSocket(int port)|创建数据报套接字并将其绑定到本地主机上的指定端口。<br/>套接字将被绑定到通配符地址，IP 地址由内核来选择。|
|public DatagramSocket(int port,InetAddress laddr)|创建数据报套接字，将其绑定到指定的本地地址。<br/>本地端口必须在 0 到 65535 之间（包括两者）。<br/>如果 IP 地址为 0.0.0.0，套接字将被绑定到通配符地址，IP 地址由内核选择。|
|public void close()|关闭此数据报套接字。|
|public void send(DatagramPacket p)|从此套接字发送数据报包。<br/>DatagramPacket 包含的信息指示：将要发送的数据、其长度、远程主机的 IP 地址和远程主机的端口号。|
|public void receive(DatagramPacket p)|从此套接字接收数据报包。<br/>当此方法返回时，DatagramPacket的缓冲区填充了接收的数据。<br/>数据报包也包含发送方的 IP 地址和发送方机器上的端口号。<br/>此方法在接收到数据报前一直阻塞。<br/>数据报包对象的 length 字段包含所接收信息的长度。<br/>如果信息比包的长度长，该信息将被截短。|
|public InetAddress getLocalAddress()|获取套接字绑定的本地地址。|
|public int getLocalPort()|返回此套接字绑定的本地主机上的端口号。|
|public InetAddress getInetAddress()|返回此套接字连接的地址。<br/>如果套接字未连接，则返回 null。|
|public int getPort()|返回此套接字的端口。如果套接字未连接，则返回 -1。|

2. DatagramPacket 类的常用方法：

|方法|详情|
|--|--|
|public DatagramPacket(byte[] buf,int length)|构造 DatagramPacket，用来接收长度为 length 的数据包。<br/>length 参数必须小于等于 buf.length。|
|public DatagramPacket(byte[] buf,int length,InetAddress address,int port)|构造数据报包，用来将长度为 length 的包发送到指定主机上的指定端口号。<br/>length参数必须小于等于 buf.length。|
|public InetAddress getAddress()|返回某台机器的 IP 地址，此数据报将要发往该机器或者是从该机器接收到的。|
|public int getPort()|返回某台远程主机的端口号，此数据报将要发往该主机或者是从该主机接收到的。|
|public byte[] getData()|返回数据缓冲区。<br/>接收到的或将要发送的数据从缓冲区中的偏移量 offset 处开始，持续 length 长度。|
|public int getLength()|返回将要发送或接收到的数据的长度。|

3. 流 程：
	1. DatagramSocket 与 DatagramPacket
	2. 建立发送端，接收端
	3. 建立数据包
	4. 调用 Socket 的发送、接收方法
	5. 关闭 Socket
4. 发送端与接收端是两个独立的运行程序
5. 例题

```java
public class Demo01 {

  // 发送端
  @Test
  public void send() throws IOException {

	 // UDP数据报通过数据报套接字 DatagramSocket 发送和接收，
	 // 系统不保证UDP数据报一定能够安全送到目的地，也不能确定什么时候可以抵达。
	 DatagramSocket socket = new DatagramSocket();

	 String str = "我是以UDP方式发送的导弹";
	 byte[] bytes = str.getBytes();
	 // 发送端的IP地址
	 InetAddress inet = InetAddress.getLocalHost();
	 // DatagramPacket 对象封装了UDP数据报，
	 // 在数据报中包含了发送端的IP地址和端口号以及接收端的IP地址和端口号
	 DatagramPacket packet = new DatagramPacket(bytes,0,bytes.length,inet,9090);

	 // 发送
	 socket.send(packet);

	 // 关闭
	 socket.close();

  }

  // 接收端
  @Test
  public void receive() throws IOException {

	 // UDP数据报通过数据报套接字 DatagramSocket 发送和接收，
	 // 系统不保证UDP数据报一定能够安全送到目的地，也不能确定什么时候可以抵达。
	 // 指定端口号
	 DatagramSocket socket = new DatagramSocket(9090);

	 byte[] buffer = new byte[100];
	 // DatagramPacket 对象封装了UDP数据报，
	 // 在数据报中包含了发送端的IP地址和端口号以及接收端的IP地址和端口号
	 DatagramPacket packet = new DatagramPacket(buffer,0,buffer.length);

	 // 接收
	 socket.receive(packet);

	 // 输出接收的文件
	 String str = new String(buffer,0,buffer.length);
	 System.out.println(str);
	 
	 // 关闭
	 socket.close();

  }

}
```

## 7、URL 编程

### ①、介绍

1. <font color="red">URL (Uniform Resource Locator)：</font>统一资源定位符，它表示 Internet 上<font color="red">某一资源</font>的地址。
2. 它是一种具体的 URI，即 URL 可以用来标识一个资源，而且还指明了如何 locate 这个资源。
3. 通过 URL 我们可以访问 Internet 上的各种网络资源，比如最常见的 `www`，`ftp` 站点。浏览器通过解析给定的 URL 可以在网络上查找相应的文件或其他资源。
4. URL 的基本结构由5部分组成：
	1. **<font color="red">传输协议</font>://<font color="orange">主机名</font>:<font color="green">端口号</font>/<font color="Cyan">文件名</font>#<font color="#8db3e2">片段名</font>?<font color="purple">参数列表</font>**，列如：
	2. <font color="red">http</font>://<font color="orange">192.168.1.100</font>:<font color="green">8080</font>/<font color="Cyan">helloworld/index.jsp</font>#<font color="#8db3e2">a</font>?<font color="purple">username=shkstart&password=123</font>
	3. <font color="#8db3e2">#片段名：</font>即锚点，例如看小说，直接定位到章节
	4. <font color="purple">参数列表格式：</font>参数名=参数值&参数名=参数值....

### ②、URL 类构造器

1. 为了表示 URL，`java.net` 中实现了类 URL。我们可以通过下面的构造器来初始化一个 URL 对象：

```java
// 通过一个表示URL地址的字符串可以构造一个URL对象。
// 例如：URL url = new URL ("http://www.atguigu.com/"); 
public URL (String spec)

// 通过基 URL 和相对 URL 构造一个 URL 对象。
// 例如：URL downloadUrl = new URL(url, “download.html")
public URL(URL context, String spec)：

// 例如：new URL("http", "www.atguigu.com", “download. html");
public URL(String protocol, String host, String file); 

// 例如: URL gamelan = new URL("http", "www.atguigu.com", 80, “download.html");
public URL(String protocol, String host, int port, String file); 
```

2. URL 类的构造器都声明抛出非运行时异常，必须要对这一异常进行处理，通常是用 `try-catch` 语句进行捕获。

![|700](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F66、URL类构造器.png)

### ③、URL 类常用方法

- 一个 URL 对象生成后，其属性是不能被改变的，但可以通过它给定的方法来获取这些属性：

|方法|详情|
|--|--|
|public String getProtocol( )|获取该URL的协议名|
|public String getHost( )|获取该URL的主机名|
|public String getPort( )|获取该URL的端口号|
|public String getPath( )|获取该URL的文件路径|
|public String getFile( )|获取该URL的文件名|
|public String getQuery( )|获取该URL的查询名|

```java
URL url = new URL("http://localhost:8080/examples/myTest.txt");
System.out.println("getProtocol() :"+url.getProtocol());
System.out.println("getHost() :"+url.getHost());
System.out.println("getPort() :"+url.getPort());
System.out.println("getPath() :"+url.getPath());
System.out.println("getFile() :"+url.getFile());
System.out.println("getQuery() :"+url.getQuery());
```

### ④、针对 HTTP 协议的 URLConnection 类

1. <font color="red">URL 的方法 openStream()：能从网络上读取数据</font>
2. 若希望输出数据，例如向服务器端的 CGI （公共网关接口-Common Gateway Interface-的简称，是用户浏览器和服务器端的应用程序进行连接的接口）程序发送一些数据，则必须先与 URL 建立连接，然后才能对其进行读写，此时需要使用 URLConnection 。
3. URLConnection：表示到URL所引用的远程对象的连接。当与一个 URL 建立连接时，首先要在一个 URL 对象上通过方法 <font color="red">openConnection()</font> 生成对应的 URLConnection对象。如果连接过程失败，将产生IOException. 
	1. `URL netchinaren = new URL ("http://www.atguigu.com/index.shtml");` 
	2. `URLConnectonn u = netchinaren.openConnection( );` 
4. 通过 URLConnection 对象获取的输入流和输出流，即可以与现有的 CGI 程序进行交互。

```java
public Object getContent( ) throws IOException
public int getContentLength( )
public String getContentType( )
public long getDate( )
public long getLastModified( )
public InputStream getInputStream( )throws IOException
public OutputSteram getOutputStream( )throws IOException
```

### ⑤、URI、URL 和 URN 的区别

1. <font color="red">URI，是 uniform resource identifier，统一资源标识符，</font>用来唯一的标识一个资源。
2. <font color="red">URL 是uniform resource locator，统一资源定位符，</font>它是一种具体的 URI，即 URL 可以用来标识一个资源，而且还指明了如何 locate 这个资源。
3. URN，uniform resource name，统一资源命名，是通过名字来标识资源，比如 `mailto:java-net@java.sun.com`。
4. 也就是说，URI 是以一种抽象的，高层次概念定义统一资源标识，而 URL 和 URN 则是具体的资源标识的方式。URL 和 URN 都是一种 URI。
5. 在 Java 的 URI 中，一个 URI 实例可以代表绝对的，也可以是相对的，只要它符合 URI 的语法规则。而 URL 类则不仅符合语义，还包含了定位该资源的信息，因此它不能是相对的。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F67、URI、URL和URN的区别.png)

### ⑥、小结

1. 位于网络中的计算机具有唯一的IP地址，这样不同的主机可以互相区分。
2. <font color="red">客户端－服务器</font>是一种最常见的网络应用程序模型。服务器是一个为其客户端提供某种特定服务的硬件或软件。客户机是一个用户应用程序，用于访问某台服务器提供的服务。<font color="red">端口号</font>是对一个服务的访问场所，它用于区分同一物理计算机上的多个服务。<font color="red">套接字</font>用于连接客户端和服务器，客户端和服务器之间的每个通信会话使用一个不同的套接字。TCP 协议用于实现面向连接的会话。
3. Java 中有关网络方面的功能都定义在 `java.net` 程序包中。Java 用 InetAddress 对象表示 <font color="red">IP 地址</font>，该对象里有两个字段：主机名(String) 和 IP 地址(int)。
4. 类 Socket 和 ServerSocket 实现了基于TCP协议的客户端－服务器程序。Socket 是客户端和服务器之间的一个连接，连接创建的细节被隐藏了。这个连接提供了一个安全的数据传输通道，这是因为 TCP 协议可以解决数据在传送过程中的丢失、损坏、重复、乱序以及网络拥挤等问题，它保证数据可靠的传送。
5. 类 URL 和 URLConnection 提供了最高级网络应用。URL 的网络资源的位置来同一表示 Internet 上各种网络资源。通过 URL 对象可以创建当前应用程序和 URL 表示的网络资源之间的连接，这样当前程序就可以读取网络资源数据，或者把自己的数据传送到网络上去

# 十四、反射

## 1、Java 反射机制概述

### ①、Java Reflection 反射

1. Reflection（反射）是被视为<font color="red">动态语言</font>的关键，反射机制允许程序在执行期借助于 Reflection API 取得任何类的内部信息，并能直接操作任意对象的内部属性及方法。
2. 加载完类之后，在堆内存的方法区中就产生了一个 Class 类型的对象（一个类只有一个 Class 对象），这个对象就包含了完整的类的结构信息。我们可以通过这个对象看到类的结构。<font color="red">这个对象就像一面镜子，透过这个镜子看到类的结构，所以，我们形象的称之为：反射。</font>

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F68、反射.png)

### ②、动态语言 vs 静态语言

1. 动态语言：
	1. 是一类在运行时可以改变其结构的语言：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。通俗点说就是：<font color="red">在运行时代码可以根据某些条件改变自身结构。</font>
	2. 主要动态语言：Object-C、C#、JavaScript、PHP、Python、Erlang
2. 静态语言：与动态语言相对应的，运行时结构不可变的语言就是静态语言。如 Java、C、C++。
3. Java 不是动态语言，但 Java 可以称之为“<font color="red">准动态语言</font>”。即 Java 有一定的动态性，我们可以利用反射机制、字节码操作获得类似动态语言的特性。Java 的动态性让编程的时候更加灵活！

### ③、Java 反射机制研究及应用

1. 在运行时判断任意一个对象所属的类
2. 在运行时构造任意一个类的对象
3. 在运行时判断任意一个类所具有的成员变量和方法
4. 在运行时获取泛型信息
5. 在运行时调用任意一个对象的成员变量和方法
6. 在运行时处理注解
7. 生成动态代理

### ④、反射相关的主要 API

1. `java.lang.Class`：代表一个类
2. `java.lang.reflect.Method`：代表类的方法
3. `java.lang.reflect.Field`：代表类的成员变量
4. `java.lang.reflect.Constructor`：代表类的构造器
5. ......

### ⑤、例子

```java
// Person 类
public class Person {
	// 属性
	private String name;
	public int age;
	// 构造器
	public Person() { }
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	// 私有构造器
	private Person(String name) { this.name = name; }

	// get/set方法
	public String getName() { return name; }
	public void setName(String name) { this.name = name; }

	// 方法
	public void show(){
		System.out.println("你好，我是好人");
	}

	private String showNation(String nation){
		System.out.println("我的国籍是：" + nation);
		return nation;
	}

	@Override
	public String toString() {
		return "Person{" +
				"name='" + name + '\'' +
				", age=" + age +
				'}';
	}
}
```

```java
// 学反射之前，对于Person的操作
public class Demo01 {
	public static void main(String[] args) {

		// 1、创建Person类的对象（实例化）
		Person p1 = new Person("月海",16);
		System.out.println(p1.toString());

		// 2、通过对象，调用其内部的属性、方法
		p1.setName("言");
		p1.age = 14;
		System.out.println(p1.toString());

		p1.show();

	}
}   
```

```java
// 学反射之后，对于Person的操作
public class Demo02 {
	public static void main(String[] args) throws Exception {

		// 1、通过反射，创建Person类的对象（实例化）
		Class<Person> personClass = Person.class;
		Constructor<Person> constructor = personClass.getConstructor(String.class, int.class);
		//    1.3、调用构造器，创建Person的对象p1
		Person p1 = constructor.newInstance("月海", 16);
		System.out.println(p1.toString());

		// 2、通过反射，调用对象指定的属性、方法（公有）
		//    2.1、获取属性：age
		Field age = personClass.getDeclaredField("age");
		//    2.2、修改
		age.set(p1,14);
		System.out.println(p1.toString());

		//    2.3、获取方法：show
		Method show = personClass.getDeclaredMethod("show");
		//    2.4、调用方法
		show.invoke(p1);

		// 3、通过反射，调用对象指定的属性、方法（私有）
		//    3.1、调用私有的构造器
		Constructor<Person> constructor02 = personClass.getDeclaredConstructor(String.class);
		constructor02.setAccessible(true);
		//    3.2、调用私有构造器，创建Person的对象p2
		Person p2 = constructor02.newInstance("言");
		System.out.println(p2);

		//    3.3、调用私有的属性
		Field name = personClass.getDeclaredField("name");
		name.setAccessible(true);
		//    3.4、修改
		name.set(p2,"月海");
		System.out.println(p2);

		//    3.5、获取方法：
		Method showNation = personClass.getDeclaredMethod("showNation", String.class);
		showNation.setAccessible(true);
		//    3.6、调用方法
		//         相当于：showNation("中国");
		//         将返回值赋值给invoke
		Object invoke = showNation.invoke(p2, "中国");
		//         打印返回值
		System.out.println(invoke);

	}
}
```

### ⑥、注意事项

1. 疑问 1：通过直接 new 的方式或反射的方式都可以调用公共的结构，开发中到底用哪个？
	1. <font color="red">建议通过直接 new 的方式</font>
	2. 什么时候会使用反射的方式：编译时不知道该造什么对象（反射的特性：动态性）
2. 疑问 2：反射机制与面向对象中的封装性是不是矛盾的？如何看待两个技术？
	1. 当然是不矛盾的，矛盾还得了
	2. 封装的<font color="red">具体概念是隐藏对象的属性和实现细节</font>，在此处主要是<font color="red">告诉</font>程序员这个属性或方法等是被封装的，最好是不要调用，因为这个属性或方法等可能是其内部使用或是有更好的实现方式。但是，非要调用，那也没办法（防君子不防小人）

## 2、理解 Class 类并获取 Class 实例

### ①、Class 类


1. 在 Object 类中定义了以下的方法，此方法将被所有子类继承：

```java
public final Class getClass()
```

2. 以上的方法返回值的类型是一个 Class 类，此类是 <font color="red">Java 反射的源头</font>，实际上所谓反射从程序的运行结果来看也很好理解，即：可以通过对象反射求出类的名称。
3. 类的加载过程：
	1. 程序经过 `javac.exe` 命令以后，会生成一个或多个字节码文件（`.class` 结尾）
	2. 接着我们使用 `java.exe` 命令对某个字节码文件进行解释运行，相当于将某个字节码文件加载到内存中，此过程就称为类的加载
	3. 加载到内存中的类，我们就称为**运行时类**，此运行时类，就作为 Class 的一个实例
	4. **换句话说，Class 类的实例就对应着一个运行时类**
	5. 加载到内存中的运行时类，会缓存一定的时间。在此时间之内，我们可以通过不同的方式来获取此运行时类。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F69、反射的理解.png)

3. 对象照镜子后可以得到的信息：某个类的属性、方法和构造器、某个类到底实现了哪些接口。对于每个类而言，JRE 都为其保留一个不变的 Class 类型的对象。一个 Class 对象包含了特定某个结构（`class/interface/enum/annotation/primitive type/void/[]`）的有关信息。
	1. Class 本身也是一个类
	2. Class 对象只能由系统建立对象
	3. 一个加载的类在 JVM 中只会有一个 Class 实例
	4. 一个 Class 对象对应的是一个加载到 JVM 中的一个 `.class` 文件
	5. 每个类的实例都会记得自己是由哪个 Class 实例所生成
	6. 通过 Class 可以完整地得到一个类中的所有被加载的结构
	7. Class 类是 Reflection 的根源，针对任何你想动态加载、运行的类，唯有先获得相应的 Class 对象
4. <font color="red">对 Class 类的理解：Class 实例对应着加载到内存中的一个运行时类</font>
5. <font color="red">运行时类：只需将其理解为具有该对象类型的所有元数据的对象</font>
	1. 在该对象中，可以找到在类、字段、类型层次结构等中声明的方法. 该信息通常由使用反射的代码使用，以使用它们来检查对象/类型或运行方法，而无需在对其本身进行编码时定义和编译类.
	2. 运行时可能会被强调，因为类定义可能会随着时间而改变，或者对象可能被声明为超类型，而该对象实际上是所声明的子类型的实例.加载某个类时，就是该实例期间加载的信息，将由 `getClass()` 方法返回
	3. 简而言之，当运行代码时，VM 将以与在 `.java` 文件中键入的”源形式不同的方式对类进行定义。当然，这些信息将在编译后加载，并且所有元数据（如上所述）将构成它们所谓的运行时类“、这是一种奇妙的说法，即一个对象，其中包含程序运行时加载的有关类的所有元数据 

### ②、Class 类的常用方法

| 方法                                               | 功能                                     |
| ------------------------------------------------ | -------------------------------------- |
| static Class forName(String name)                | 返回指定类名 name 的 Class 对象                 |
| Object newInstance()                             | 调用缺省构造函数，返回该Class对象的一个实例               |
| getName()                                        | 返回此Class对象所表示的实体（类、接口、数组类、基本类型或void）名称 |
| Class getSuperClass()                            | 返回当前Class对象的父类的Class对象                 |
| Class [] getInterfaces()                         | 获取当前Class对象的接口                         |
| ClassLoader getClassLoader()                     | 返回该类的类加载器                              |
| Class getSuperclass()                            | 返回表示此Class所表示的实体的超类的Class              |
| Constructor[] getConstructors()                  | 返回一个包含某些Constructor对象的数组               |
| Field[] getDeclaredFields()                      | 返回Field对象的一个数组                         |
| Method getMethod(String name,Class … paramTypes) | 返回一个Method对象，此对象的形参类型为paramType        |

### ③、获取 Class 类实例的四种方法


1. **前提：** 若已知具体的类，通过类的 class 属性获取，该方法最为安全可靠，程序性能最高

```java
Class clazz = String.class
```

2. **前提：** 已知某个类的实例，调用该实例的 getClass() 方法获取 Class 对象

```java
Class clazz = “www.atguigu.com”.getClass()
```

3. **前提：** 已知一个类的全类名，且该类在类路径下，可通过 Class 类的静态方法 `forName()` 获取，可能抛出 ClassNotFoundException
	- <font color="red">最能体现反射的动态性的方法</font>

```java
Class clazz = Class.forName(“java.lang.String”)
```

4. 其他方式(不做要求)

```java
ClassLoader cl = this.getClass().getClassLoader();
Class clazz4 = cl.loadClass(“类的全类名”)
```

```java
// 获取Class实例的方式（前三种方式需要掌握）
public class Demo04 {
	public static void main(String[] args) throws ClassNotFoundException {

		// 方式一：调用运行时类的属性：.class
		Class<Person> p1Class = Person.class;
		System.out.println(p1Class);

		// 方式二：通过运行时类的对象，调用getClass()
		Person p2 = new Person();
		Class<? extends Person> p2Class = p2.getClass();
		System.out.println(p2Class);

		// 方式三：调用Class的静态方法：forName(String classPath)
		Class<?> p3Class = Class.forName("com.yuehai.day01.Person");
		System.out.println(p3Class);
		// 可以选择所有的类
		Class<?> SClass = Class.forName("java.lang.String");
		System.out.println(SClass);

		// 方式四：使用类的加载器：ClassLoader
		ClassLoader classLoader = Demo04.class.getClassLoader();
		Class p4Class = classLoader.loadClass("com.yuehai.day01.Person");
		System.out.println(p4Class);

		// 这四种方法得到的对象指向的内存地址时相同的
		System.out.println(p1Class == p2Class);// true
		System.out.println(p1Class == p3Class);// true
		System.out.println(p1Class == p4Class);// true

	}
}
```

### ④、哪些类型可以有 Class 对象？


1. `class`：外部类，成员(成员内部类，静态内部类)，局部内部类，匿名内部类
2. `interface`：接口
3. `[]`：数组
4. `enum`：枚举
5. `annotation`：注解 @interface
6. `primitive type`：基本数据类型
7. `void`
- 理解 Class 类并获取 Class 的实例

```java
Class c1 = Object.class;
Class c2 = Comparable.class;
Class c3 = String[].class;
Class c4 = int[][].class;
Class c5 = ElementType.class;
Class c6 = Override.class;
Class c7 = int.class;
Class c8 = void.class;
Class c9 = Class.class;

int[] a = new int[10];
int[] b = new int[100];
Class c10 = a.getClass();
Class c11 = b.getClass();
// 只要元素类型与维度一样（比如上面的都是int），就是同一个Class
System.out.println(c10 == c11);
```

## 3、类的加载与 ClassLoader 的理解

### ①、了解：类的加载过程

- 类的加载过程：当程序主动使用某个类时，如果该类还未被加载到内存中，则系统会通过如下三个步骤来对该类进行初始化。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F70、类的加载过程.png)

### ②、类的加载与 ClassLoader 的理解


1. 加载：将 class 文件字节码内容加载到内存中，并将这些静态数据转换成方法区的运行时数据结构，然后生成一个代表这个类的 `java.lang.Class` 对象，作为方法区中类数据的访问入口（即引用地址）。所有需要访问和使用类数据只能通过这个 Class 对象。这个加载的过程需要类加载器参与。
2. 链接：将 Java 类的二进制代码合并到 JVM 的运行状态之中的过程。
	1. 验证：确保加载的类信息符合 JVM 规范，例如：以 cafe 开头，没有安全方面的问题
	2. 准备：正式为类变量（static）分配内存并**设置类变量默认初始值**的阶段，这些内存都将在方法区中进行分配。
	3. 解析：虚拟机常量池内的符号引用（常量名）替换为直接引用（地址）的过程。
3. 初始化：
	1. 执行类构造器 `<clinit>()` 方法的过程。类构造器 `<clinit>()` 方法是由编译期自动收集类中所有类变量的赋值动作和静态代码块中的语句合并产生的。（类构造器是构造类信息的，不是构造该类对象的构造器）。
	2. 当初始化一个类的时候，如果发现其父类还没有进行初始化，则需要先触发其父类的初始化。
	3. 虚拟机会保证一个类的 `<clinit>()` 方法在多线程环境中被正确加锁和同步。

```java
public class ClassLoadingTest {
	public static void main(String[] args) {
		System.out.println(A.m);
	}
}
	
class A {
	static {
		m = 300;
	}
	static int m = 100;
}
//第二步：链接结束后m=0
//第三步：初始化后，m的值由<clinit>()方法执行决定
// 这个A的类构造器<clinit>()方法由类变量的赋值和静态代码块中的语句按照顺序合并产生，类似于
//      <clinit>(){
//          m = 300;
//          m = 100;
//      }                        
```

### ③、了解：什么时候会发生类初始化？

1. **类的主动引用（一定会发生类的初始化）**
	1. 当虚拟机启动，先初始化 main 方法所在的类
	2. new 一个类的对象
	3. 调用类的静态成员（除了 final 常量）和静态方法
	4. 使用 `java.lang.reflect` 包的方法对类进行反射调用
	5. 当初始化一个类，如果其父类没有被初始化，则先会初始化它的父类
2. **类的被动引用（不会发生类的初始化）**
	1. 当访问一个静态域时，只有真正声明这个域的类才会被初始化
	2. 当通过子类引用父类的静态变量，不会导致子类初始化
	3. 通过数组定义类引用，不会触发此类的初始化
	4. 引用常量不会触发此类的初始化（常量在链接阶段就存入调用类的常量池中了）
3. **类加载器的作用：**
	1. **类加载的作用：** 将 class 文件字节码内容加载到内存中，并将这些静态数据<font color="red">转换成方法区的运行时数据结构</font>，然后在堆中生成一个代表这个类的 `java.lang.Class` 对象，作为方法区中类数据的访问入口。
	2. **类缓存：** 标准的 JavaSE 类加载器可以按要求查找类，但一旦某个类被加载到类加载器中，它将维持加载（缓存）一段时间。不过 JVM 垃圾回收机制可以回收这些 Class 对象。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F71、类加载器的作用.png)

### ④、了解：ClassLoader

1. 类加载器作用是用来把类（class）装载进内存的。
2. JVM 规范定义了如下类型的类的加载器。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F72、类加载器.png)

```java
 //1.获取一个系统类加载器
 ClassLoader classloader = ClassLoader.getSystemClassLoader();
 System.out.println(classloader);

 //2.获取系统类加载器的父类加载器，即扩展类加载器
 classloader = classloader.getParent();
 System.out.println(classloader);

 //3.获取扩展类加载器的父类加载器，即引导类加载器
 classloader = classloader.getParent();
 System.out.println(classloader);

 //4.测试当前类由哪个类加载器进行加载
 classloader = Class.forName("exer2.ClassloaderDemo").getClassLoader();
 System.out.println(classloader);

 //5.测试JDK提供的Object类由哪个类加载器加载
 classloader = Class.forName("java.lang.Object").getClassLoader();
 System.out.println(classloader);

 //*6.关于类加载器的一个主要方法：getResourceAsStream(String str):获取类路径下的指定文件的输入流
 InputStream in = null;
 in = this.getClass().getClassLoader().getResourceAsStream("exer2\\test.properties");
 System.out.println(in);
```

### ⑤、使用 ClassLoader 加载配置文件

1. 方式一：io 流

```java
public class Demo05 {
	public static void main(String[] args) throws IOException {
		// 此时的文件默认在主工程下
		// 加载文件
		FileInputStream fIS = new FileInputStream("jdbc.properties");
		// 创建Properties对象
		Properties pros = new Properties();
		// 调用Properties对象的load方法，读取文件
		pros.load(fIS);

		// 读取key是user的内容
		String user = pros.getProperty("user");
		// 读取key是password的内容
		String password = pros.getProperty("password");

		System.out.println("user：" +user + "，password：" +password);

	}
}
```

2. 方式二：使用 ClassLoader

```java
public class Demo06 {
	public static void main(String[] args) throws IOException {

		// 创建Properties对象
		Properties pros = new Properties();

		// 配置文件默认识别为：当前module的src目录下
		ClassLoader classLoader = Demo06.class.getClassLoader();
		InputStream iS = classLoader.getResourceAsStream("jdbc1.properties");

		// 调用Properties对象的load方法，读取文件
		pros.load(iS);

		// 读取key是user的内容
		String user = pros.getProperty("user");
		// 读取key是password的内容
		String password = pros.getProperty("password");

		System.out.println("user：" +user + "，password：" +password);

	}
}
```

## 4、创建运行时类的对象，理解反射的动态性

### ①、有了 Class 对象，能做什么？

1. **创建类的对象**：调用 Class 对象的 `newInstance()` 方法，要求：
	1.  类必须有一个无参数的构造器。
	2.  类的构造器的访问权限需要足够。
2. <font color="red">难道没有无参的构造器就不能创建对象了吗？</font>
3. 不是！只要在操作的时候明确的调用类中的构造器，并将参数传递进去之后，才可以实例化操作。步骤如下：
	1. 通过 Class 类的 `getDeclaredConstructor(Class … parameterTypes)` 取得本类的指定形参类型的构造器
	2. 向构造器的形参中传递一个对象数组进去，里面包含了构造器中所需的各个参数。
	3. 通过 Constructor 实例化对象。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F73、创建运行时类的对象.png)

4. 以上是反射机制应用最多的地方。

### ②、创建类的对象的方式：

1. 方式一：new + 构造器

```java
Person p = new Person();
```

2. 方式二：要创建Xxx类的对象，可以考虑：Xxx、Xxxs、XxxFactory、XxxBuilder、类中查看是否有静态方法的存在，可以调用其静态方法（会自动创建创建Xxx对象）

```java
Xxx.静态方法;
```

3. 方式三：通过反射，上面写的三种方法

### ③、理解反射的动态性

```java
// 理解反射的动态性
public class Demo08 {
	public static void main(String[] args) {

		// 循环100遍，创建100个对象
		for (int i = 0; i < 100; i++) {
			// 生成一个随机的int值，该值介于[0,n)的区间，
			// 也就是0到n之间的随机int值，包含0而不包含n
			int num = new Random().nextInt(3);
			// 创建String类型的classPath字符串
			String classPath = "";

			// switch判断，根据num的值来选择classPath的参数
			switch (num){
				case 0:
					classPath = "java.util.Date";
					break;
				case 1:
					classPath = "java.lang.Object";
					break;
				case 2:
					classPath = "com.yuehai.day01.Person";
			}

			try {
				// 调用getInstance()方法，将classPath作为参数传递过去
				// 返回的对象赋值给obj
				Object obj = getInstance(classPath);
				// 打印obj，由此实现的动态的创建对象
				System.out.println(obj);
			} catch (Exception e) {
				e.printStackTrace();
			}

		}

	}

	// getInstance()方法
	// 接收调用者传输过来的String类型的classPath
	public static Object getInstance(String classPath) throws Exception {
		// 调用Class的forName方法
		// 返回指定类名classPath的 Class 对象
		Class aClass = Class.forName(classPath);
		// 调用newInstance()方法，实例化classPath对象
		// 并返回
		return aClass.newInstance();
	}
}
```

## 5、获取运行时类的完整<font color="red">结构</font>

### ①、使用反射可以取得

1. 实现的全部接口

```java
// 确定此对象所表示的类或接口实现的接口。
public Class<?>[] getInterfaces()
```

2. 所继承的父类

```java
// 返回表示此 Class 所表示的实体（类、接口、基本类型）的父类的Class。
public Class<? Super T> getSuperclass()
```

3. 全部的构造器

```java
// 返回此 Class 对象所表示的类的所有public构造方法。
public Constructor<T>[] getConstructors()
// 返回此 Class 对象表示的类声明的所有构造方法。
public Constructor<T>[] getDeclaredConstructors()

// Constructor类中：
// 取得修饰符:
public int getModifiers();
// 取得方法名称: 
public String getName();
// 取得参数的类型：
public Class<?>[] getParameterTypes();
```

4. 全部的方法

```java
// 返回此Class对象所表示的类或接口的全部方法
public Method[] getDeclaredMethods()
// 返回此Class对象所表示的类或接口的public的方法
public Method[] getMethods() 

// Method类中：
// 取得全部的返回值
public Class<?> getReturnType()
// 取得全部的参数
public Class<?>[] getParameterTypes()
// 取得修饰符
public int getModifiers()
// 取得异常信息
public Class<?>[] getExceptionTypes()
```

5. 全部的 Field

```java
// 返回此Class对象所表示的类或接口的public的Field。
public Field[] getFields() 
// 返回此Class对象所表示的类或接口的全部Field。
public Field[] getDeclaredFields() 

// Field方法中：
// 以整数形式返回此Field的修饰符
public int getModifiers() 
// 得到Field的属性类型
public Class<?> getType() 
// 返回Field的名称。
public String getName() 
```

6. Annotation 相关

```java
get Annotation(Class<T> annotationClass)
getDeclaredAnnotations() 
```

7. 泛型相关

```java
// 获取父类泛型类型：
Type getGenericSuperclass()
// 泛型类型：
ParameterizedType
// 获取实际的泛型类型参数数组：
getActualTypeArguments()
```

8. 类所在的包：`Package getPackage()`
9. 小结：
	1.  在实际的操作中，取得类的信息的操作代码，并不会经常开发。
	2.  一定要熟悉 `java.lang.reflect` 包的作用，反射机制。
	3.  如何取得属性、方法、构造器的名称，修饰符等。

### ②、例子

1. 自定义注解

```java
// 自定义注解
@Target({TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE})
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
	String value() default "hello";
}
```

2. 父类

```java
// 父类
public class Creature<T> implements Serializable {
	// 性别
	private char gender;
	// 体重
	public double weight;

	// 呼吸
	private void breath(){
		System.out.println("生物呼吸");
	}
	// 吃
	public void eat(){
		System.out.println("生物吃东西");
	}

}
```

3. 接口类

```java
// 接口类
public interface MyInterface {
	// 信息接口
	void info();
}
```

4. 子类、接口实现类

```java
// 子类
// 接口实现类
@MyAnnotation(value = "hi")
public class Person extends Creature<String> implements Comparable<String>,MyInterface {
	// 属性
	private String name;
	int age;
	public int id;

	// 构造器
	public Person() { }
	private Person(String name) { this.name = name; }
	Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	// 子类自定义方法
	@MyAnnotation
	private String show(String nation){
		System.out.println("我的国籍是：" + nation);
		return nation;
	}
	// 子类自定义方法
	@MyAnnotation(value = "月海")
	public String display(String interests,int age) throws NullPointerException,ClassCastException{
		return interests + age;
	}

	// 实现的MyInterface接口的方法
	@Override
	public void info() {
		System.out.println("我是一个人");
	}
	// 实现的Comparable接口的方法
	@Override
	public int compareTo(String o) {
		return 0;
	}

	// 子类自定义的静态方法
	private static void showDesc(){
		System.out.println("静态方法");
	}
}
```

5. 获取运行时类的属性结构

```java
// 获取当前运行时类的属性结构
public class FieldStructureTest {

	@Test
	public void test1(){

		Class<Person> pClass = Person.class;

		// 获取属性结构
		// getFields()：获取当前运行时类及其父类中声明为public访问权限的属性
		Field[] fields = pClass.getFields();
		for (Field f : fields){
			System.out.println(f);
		}
		System.out.println();

		// getDeclaredFields()：获取当前运行时类中声明的所有属性（不包含父类中声明的属性）
		Field[] declaredFields = pClass.getDeclaredFields();
		for (Field f : declaredFields){
			System.out.println(f);
		}
		System.out.println();

	}

	// 权限修饰符   数据类型   变量名
	@Test
	public void test2(){

		Class<Person> pClass = Person.class;

		// getDeclaredFields()：获取当前运行时类中声明的所有属性（不包含父类中声明的属性）
		Field[] declaredFields = pClass.getDeclaredFields();

		for (Field f : declaredFields){
			// 1、权限修饰符
			// 默认为int型
			int modifiers = f.getModifiers();
			System.out.print(modifiers + "\t");
			// 使用Modifier类的toString()方法可以将int型翻译为字符串
			String ftoString = Modifier.toString(modifiers);
			System.out.print(ftoString + "\t");

			// 2、数据类型
			Class<?> type = f.getType();
			System.out.print(type + "\t");

			// 3、变量名
			String fName = f.getName();
			System.out.println(fName);
		}

	}

}
```

6. 获取运行时类的方法结构

```java
// 获取运行时类的方法结构
public class MethodStructureTest {

	@Test
	public void test1(){

		Class<Person> pClass = Person.class;

		// getMethods()：获取当前运行时类及其所有父类中声明为public权限的方法
		Method[] methods = pClass.getMethods();
		for (Method m : methods){
			System.out.println(m);
		}
		System.out.println();

		// getDeclaredMethods()：获取当前运行时类中声明的所有方法（不包含父类中声明的方法）
		Method[] declaredMethods = pClass.getDeclaredMethods();
		for (Method m : declaredMethods){
			System.out.println(m);
		}
		System.out.println();

	}
	
	// @某某注解
	// 权限修饰符 返回值类型 方法名（参数类型1 形参名, ... ）throws 某某异常
	@Test
	public void test2(){

		Class<Person> pClass = Person.class;
		Method[] declaredMethods = pClass.getDeclaredMethods();

		for (Method m : declaredMethods){

			// 1、获取方法声明的注解
			Annotation[] annotations = m.getAnnotations();
			for(Annotation a : annotations){
				System.out.println(a + "\t");
			}

			// 2、权限修饰符
			System.out.print(Modifier.toString(m.getModifiers()) + " ");

			// 3、返回值类型
			System.out.print(m.getReturnType().getName() + " ");

			// 4、方法名
			System.out.print(m.getName());
			// 方法名后的前括号
			System.out.print("(");

			// 5、形参列表
			Class<?>[] parameterTypes = m.getParameterTypes();
			// 如是有形参的话：
			if( !(parameterTypes == null || parameterTypes.length == 0) ){
				for(int i = 0;i < parameterTypes.length;i++){
					// 判断这个形参是不是最后一个，如果是后面就不加逗号了
					// 然后结束循环
					if(i == parameterTypes.length-1){
						System.out.print(parameterTypes[i].getName() + " args_" + i);
						break;
					}
					// 不是最后一个就加逗号
					System.out.print(parameterTypes[i].getName() + " args_" + i + ",");
				}
			}
			// 方法名后的后括号
			System.out.print(")");
			// 6、抛出的异常
			Class<?>[] exceptionTypes = m.getExceptionTypes();
			// 如是没有异常的话：
			if( exceptionTypes == null || exceptionTypes.length == 0){
				System.out.println();
			// 如是有异常的话：
			}else {
				System.out.print(" throws ");
				for(int i = 0;i < exceptionTypes.length;i++){
					// 判断这个异常是不是最后一个，如果是后面就不加逗号了
					// 然后结束循环
					if(i == exceptionTypes.length-1){
						System.out.println(exceptionTypes[i].getName());
						break;
					}
					// 不是最后一个就加逗号
					System.out.println(exceptionTypes[i].getName() + ",");
				}
			}

		}

	}

}
```

7. 获取运行时类的构造器结构

```java
// 获取运行时类的构造器结构
public class OtherTest {
	public static void main(String[] args) {
		
		Class<Person> pClass = Person.class;

		// getConstructors()：获取当前运行时类中声明为public的构造器
		Constructor<?>[] constructors = pClass.getConstructors();
		for (Constructor c : constructors){
			System.out.println(c);
		}
		System.out.println();

		// getDeclaredConstructors()：获取当前运行时类中声明的所有的构造器
		Constructor<?>[] declaredConstructors = pClass.getDeclaredConstructors();
		for (Constructor c : declaredConstructors){
			System.out.println(c);
		}
		System.out.println();
		
	}
}
```

8. <font color="red">获取运行时类的父类及其父类的泛型</font>

```java
// 获取运行时类的父类及其父类的泛型
public class SuperTest {
	public static void main(String[] args) {

		Class<Person> pClass = Person.class;

		// 1、getSuperclass()：获取运行时类的父类
		Class<? super Person> superclass = pClass.getSuperclass();
		System.out.println(superclass);

		// 2、获取运行时类的带泛型的父类
		Type genericSuperclass = pClass.getGenericSuperclass();
		System.out.println(genericSuperclass);

		// 3、获取运行时类的父类的泛型类型
		//    将上面获取的genericSuperclass强转为ParameterizedType类型
		ParameterizedType parameterizedType = (ParameterizedType) genericSuperclass;
		//    然后调用getActualTypeArguments()方法，返回一个Typ数组
		Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();
		//    遍历
		for(Type a : actualTypeArguments){
			System.out.println(a);
		}

		// 4、去掉3中类型前面的class
		for(Type a : actualTypeArguments){
			// 1、调用getTypeName()方法
			System.out.println(a.getTypeName());
			// 2、因为actualTypeArguments是数组所一没有getName()方法
			//    将其强转为Class类型就可以了（本来也是Class类型）
			System.out.println( ( (Class)a).getName() );
		}
		
	}
}
```

9.  <font color="red">获取运行时类的接口、所在包、注解等</font>

```java
// 获取运行时类的接口、所在包、注解等
public class InterfaceTest {
	public static void main(String[] args) {

		Class<Person> pClass = Person.class;

		// 1、获取运行时类实现的接口
		Class<?>[] interfaces = pClass.getInterfaces();
		for(Class c : interfaces){
			System.out.println(c);
		}
		System.out.println();

		// 2、获取运行时类的父类实现的接口
		Class<?>[] interfaces1 = pClass.getSuperclass().getInterfaces();
		for(Class c : interfaces1){
			System.out.println(c);
		}
		System.out.println();

		// 3、获取运行时类的所在包
		Package pack = pClass.getPackage();
		System.out.println(pack);

		// 4、获取运行时类的注解等
		Annotation[] annotations = pClass.getAnnotations();
		for(Annotation c : annotations){
			System.out.println(c);
		}
		System.out.println();
		
	}
}
```

## 6、调用运行时类的指定结构

### ①、调用指定方法


- 通过反射，调用类中的方法，通过 Method 类完成。步骤：

1. 通过 Class 类的 `getMethod(String name,Class…parameterTypes)` 方法取得一个 `Method` 对象，并设置此方法操作时所需要的参数类型。
2. 之后使用 `Object invoke(Object obj, Object[] args)` 进行调用，并向方法中传递要设置的obj对象的参数信息。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F74、调用运行时类的指定结构.png)

3. `Object invoke(Object obj, Object … args)`：
	1. `.Object` 对应原方法的返回值，若原方法无返回值，此时返回 null
	2. 若原方法若为静态方法，此时形参 Object obj 可为 null
	3. 若原方法形参列表为空，则 `Object[] args` 为 null
	4. 若原方法声明为 private，则需要在调用此 `invoke()` 方法前，显式调用方法对象的 `setAccessible(true)` 方法，将可访问 private 的方法。
4. 例子：

```java
// 调用指定方法
public class MethodTest {

	@Test
	public void test1() throws NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException {

		Class<Person> pClass = Person.class;

		// 创建运行时类的对象
		Person p = pClass.newInstance();

		// 1、获取指定的某个方法：getDeclaredMethod();
		// 参数1：指明获取的方法的名称。
		// 参数2：指明获取的方法的形参列表
		Method show = pClass.getDeclaredMethod("show", String.class);

		// 2、保证当前属性是可访问的
		// 除了public，其他权限只有使用此方法设置为true才可以访问
		show.setAccessible(true);

		// 3、调用方法：invoke();
		// 参数1：方法的调用者。参数2：给方法的形参赋值的参数
		// invoke()方法的返回值即为 调用的对应类中方法的返回值
		Object invoke = show.invoke(p, "中国");
		System.out.println(invoke);

	}

	// 如何调用静态方法
	@Test
	public void test2() throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {

		Class<Person> pClass = Person.class;

		// 创建运行时类的对象
		Person p = pClass.newInstance();

		// 1、获取指定的某个方法：getDeclaredMethod();
		Method showDesc = pClass.getDeclaredMethod("showDesc");

		// 2、保证当前属性是可访问的
		showDesc.setAccessible(true);

		// 3、调用方法：invoke();
		// 如果调用的运行时类中的方法没有返回值，则此invoke()返回null
		Object invoke = showDesc.invoke(p);
		System.out.println(invoke);

	}

}
```

### ②、调用指定属性


1. 在反射机制中，可以直接通过Field类操作类中的属性，通过 Field 类提供的 `set()` 和 `get()` 方法就可以完成设置和取得属性内容的操作。

```java
// 返回此Class对象表示的类或接口的指定的public的Field。
public Field getField(String name) 
// 返回此Class对象表示的类或接口的指定的Field。
public Field getDeclaredField(String name)
```

2. 在Field中：

```java
// 取得指定对象obj上此Field的属性内容
public Object get(Object obj) 
// 设置指定对象obj上此Field的属性内容
public void set(Object obj,Object value) 
```

3. 例子

```java
// 调用指定属性
public class ReflectionTest {

	// 通常不采用此方式
	@Test
	public void test1() throws IllegalAccessException, InstantiationException, NoSuchFieldException {

		Class<Person> pClass = Person.class;

		// 创建运行时类的对象
		Person p = pClass.newInstance();
		// 获取指定的属性：要求运行时类中属性声明为public
		// 通常不采用此方式
		Field id = pClass.getField("id");

		// 设置当前属性的值：set()：
		// 参数1：指明设置哪个对象的属性值，参数2：将此属性值设置为多少
		id.set(p,1001);

		// 获取当前属性的值：get()：
		// 参数1：指明获取哪个对象的属性值
		int pId = (int) id.get(p);
		System.out.println(pId);

	}

	@Test
	public void test2() throws IllegalAccessException, InstantiationException, NoSuchFieldException {

		Class<Person> pClass = Person.class;

		// 创建运行时类的对象
		Person p = pClass.newInstance();

		// 1、getDeclaredField(String fieldName)：
		// 获取运行时类中指定变量名的属性
		Field name = pClass.getDeclaredField("name");

		// 2、保证当前属性是可访问的
		// 除了public，其他权限只有使用此方法设置为true才可以访问
		name.setAccessible(true);

		// 3、设置当前属性的值：set()：
		// 参数1：指明设置哪个对象的属性值，参数2：将此属性值设置为多少
		name.set(p,"月海");

		// 4、获取并赋值
		String pName = (String) name.get(p);

		System.out.println(pName);

	}

}
```

### ③、调用运行时类中的指定的构造器

```java
// 调用运行时类中的指定的构造器
public class ConstructorTest {
	public static void main(String[] args) throws NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {

		Class<Person> pClass = Person.class;

		// 1、获取指定的构造器：getDeclaredConstructor();
		// 参数：指明构造器的参数列表
		Constructor<Person> constructor = pClass.getDeclaredConstructor(String.class);

		// 2、保证此构造器是可访问的
		constructor.setAccessible(true);

		// 3、调用此构造器创建运行时类的对象
		// 参数：给构造器所需的参数赋值
		Person person = constructor.newInstance("月海");

		System.out.println(person);

	}
}
```

### ④、关于 setAccessible 方法的使用

1. `Method` 和 `Field`、`Constructor` 对象都有 `setAccessible()` 方法。
2. `setAccessible` 启动和禁用访问安全检查的开关。
3. 参数值为 `true` 则指示反射的对象在使用时应该取消 Java 语言访问检查。
	1. 提高反射的效率。如果代码中必须用反射，而该句代码需要频繁的被调用，那么请设置为 `true`。
	2. 使得原本无法访问的私有成员也可以访问
4. 参数值为 `false` 则指示反射的对象应该实施 Java 语言访问检查。

## 7、反射的应用：动态代理

### ①、代理设计模式的原理

1. 使用一个代理将对象包装起来, 然后用该代理对象取代原始对象。任何对原始对象的调用都要通过代理。<font color="red">代理对象决定是否以及何时将方法调用转到原始对象上。</font>
2. 之前为大家讲解过代理机制的操作，属于静态代理，特征是代理类和目标对象的类都是在编译期间确定下来，不利于程序的扩展。同时，每一个代理类只能为一个接口服务，这样一来程序开发中必然产生过多的代理。<font color="red">最好可以通过一个代理类完成全部的代理功能。</font>
3. 动态代理是指客户通过代理类来调用其它对象的方法，并且是在程序运行时根据需要动态创建目标类的代理对象。
4. 动态代理使用场合：
	1. 调试
	2. 远程方法调用
5. **动态代理相比于静态代理的优点：** 抽象角色（接口）中声明的所有方法都被转移到调用处理器一个集中的法中处理，这样，我们可以更加灵活和统一的处理众多的方法。
6. <font color="red">静态代理类举例</font>
   - 特点：代理类和被代理类在编译期间就确定下来了

```java
// 接口类
interface ClothFactory{
	void produceCloth();
}

// 代理类
class ProxyClothFactory implements ClothFactory{
	// 用被代理类对象进行实例化
	private ClothFactory factory;

	public ProxyClothFactory(ClothFactory factory){
		this.factory = factory;
	}

	@Override
	public void produceCloth() {
		System.out.println("代理工厂做的一些准备工作");
		// 调用被代理类的produceCloth()方法
		factory.produceCloth();

		System.out.println("代理工厂做的一些收尾工作");
	}
}

// 被代理类
class YueHai implements ClothFactory{

	@Override
	public void produceCloth() {
		System.out.println("月海可爱");
	}
}

// 测试实现类
public class Demo01 {
	public static void main(String[] args) {
		// 1、创建被代理类的对象
		YueHai yueHai = new YueHai();

		// 2、创建代理类的对象
		// 代理类处理接口，实际传入的参数是被代理类
		ClothFactory prox = new ProxyClothFactory(yueHai);

		// 3、调用代理类的produceCloth()方法
		// 在代理类的produceCloth()方法中，
		// 又调用了被代理类的produceCloth()方法
		prox.produceCloth();
	}
}
```

### ②、Java 动态代理相关 API

1. `Proxy`：专门完成代理的操作类，是所有动态代理类的父类。通过此类为一个或多个接口动态地生成实现类。
2. 提供用于创建动态代理类和动态代理对象的静态方法

```java
// 创建一个动态代理类所对应的Class对象
static Class<?> getProxyClass(ClassLoader loader, Class<?>... interfaces) 
```

```java
// 直接创建一个动态代理对象
static Object newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler h) 
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F75、Java动态代理相关API.png)

### ③、动态代理步骤

1. 创建一个实现接口 `InvocationHandler` 的类，它必须实现 invoke 方法，以完成代理的具体操作。

```java
public Object invoke(Object theProxy, Method method, Object[] params) throws Throwable{

	try{
		Object retval = method.invoke(targetObj, params);
		// Print out the result
		System.out.println(retval);
		return retval;
	}catch (Exception exc){
		
	}

}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F76、动态代理步骤1.png)

2. 创建被代理的类以及接口

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F77、动态代理步骤2.png)

3. 通过 Proxy 的静态方法：`newProxyInstance(ClassLoader loader, Class[]interfaces,InvocationHandler h)` 创建一个Subject接口代理

```java
RealSubject target = new RealSubject();
// Create a proxy to wrap the original implementation
DebugProxy proxy = new DebugProxy(target);
// Get a reference to the proxy through the Subject interface
Subject sub = (Subject) Proxy.newProxyInstance(
Subject.class.getClassLoader(),new Class[] { Subject.class }, proxy);
```

4. 通过 Subject 代理调用 RealSubject 实现类的方法

```java
String info = sub.say("Peter", 24);
System.out.println(info);
```

5. 动态代理类举例：

```java
// 接口类
// 人
interface Human{
	// 信仰
	String getBelief();
	// 吃
	void eat(String food);
}

// 被代理类
// 超人
class SuperMan implements Human{

	// 信仰
	@Override
	public String getBelief() {
		return "I believe I can fly!";
	}

	// 吃
	@Override
	public void eat(String food) {
		System.out.println("我喜欢吃" + food);
	}
}

/*
想要实现动态代理，需要解决的问题？
问题一：如何根据加载到内存中的被代理类，动态的创建一个代理类及其对象
问题二：当通过代理类的对象调用方法时，如何动态的去调用被代理类中的同名方法
*/
// 代理类
class ProxyFactory{
	// 调用此方法，返回一个代理类的对象，解决了问题一
	// obj：被代理类的对象
	public static Object getProxyFactory(Object obj){
		// 创建handler对象
		MyInvocationHandler handler = new MyInvocationHandler();
		// 调用handler对象的构造器，给被代理类的对象实例化
		handler.MyInvocationHandler(obj);

		// 直接创建一个动态代理对象
		// obj.getClass().getClassLoader()：用哪个类加载器去加载代理对象
		// obj.getClass().getInterfaces()：动态代理类需要实现的接口
		// handler：动态代理方法在执行时，会调用handler里面的invoke方法去执行
		return Proxy.newProxyInstance(obj.getClass().getClassLoader(),obj.getClass().getInterfaces(),handler);
	}

}

// 动态代理必须实现的接口，是proxy代理实例的调用处理程序实现的一个接口，每一个proxy代理实例都有一个关联的调用处理程序
// 在代理实例调用方法时，方法调用被编码分派到调用处理程序的invoke方法。
class MyInvocationHandler implements InvocationHandler{
	// 需要使用被代理类的对象赋值
	private Object obj;

	// 通过构造器给被代理类的对象实例化
	public void MyInvocationHandler(Object obj){
		this.obj = obj;
	}

	// 当我们通过代理类的对象，调用方法a时，就会自动的调用如下的方法：invoke()
	// 将被代理类要执行的方法a的功能声明在invoke()中
	@Override
	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
		// method：即为代理类对象调用的方，此方法也就作为了被代理类对象要调用的方法
		// 解决了问题二
		// obj：被代理类的对象
		Object invoke = method.invoke(obj, args);
		// 上述方法的返回值就作为当前类中的invoke()方法的返回值
		return invoke;
	}
}

// 测试实现类
public class Demo02 {
	public static void main(String[] args) {
		// 创建superMan对象
		SuperMan superMan = new SuperMan();
		// factory：代理类的对象
		Human factory = (Human) ProxyFactory.getProxyFactory(superMan);

		// 当通过代理类对象调用方法时，会自动的调用被代理类中同名的方法
		System.out.println(factory.getBelief());
		factory.eat("火锅");

	}
}
```

### ④、动态代理与 AOP（Aspect Orient Programming)

1. AOP：在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。
2. 前面介绍的 `Proxy` 和 `InvocationHandler`，很难看出这种动态代理的优势，下面介绍一种更实用的动态代理机制

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F78、动态代理与AOP1.png)

3. 改进后的说明：代码段 1、代码段 2、代码段3和深色代码段分离开了，但代码段 1、2、3 又和一个特定的方法 A 耦合了！最理想的效果是：代码块 1、2、3 既可以执行方法 A，又无须在程序中以硬编码的方式直接调用深色代码的方法

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F79、动态代理与AOP2.png)

### ⑤、总结

1. 使用 Proxy 生成一个动态代理时，往往并不会凭空产生一个动态代理，这样没有太大的意义。通常都是为指定的目标对象生成动态代理
2. 这种动态代理在 AOP 中被称为 AOP 代理，AOP 代理可代替目标对象，AOP 代理包含了目标对象的全部方法。但 AOP 代理中的方法与目标对象的方法存在差异：<font color="red">AOP 代理里的方法可以在执行目标方法之前、之后插入一些通用处理</font>

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F80、动态代理与AOP总结.png)

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十一、JDK 8 新特性

## 0、Java 8 新特性简介

1. Java 8 (又称为 jdk 1.8) 是 Java 语言开发的一个主要版本。
2. Java 8 是 oracle 公司于 2014 年 3 月发布，可以看成是自 Java 5 以来最具革命性的版本。
3. Java 8 为 Java 语言、编译器、类库、开发工具与 JVM 带来了大量新特性：
   1.  速度更快
   2. 代码更少(增加了新的语法：Lambda 表达式)
   3. 强大的 Stream API
   4. 便于并行
   5. 最大化减少空指针异常：Optional
   6. Nashorn 引擎，允许在 JVM上 运行 JS 应用
4. 并行流与串行流：
   1. 并行流就是把一个内容分成多个数据块，并用不同的线程分别处理每个数据块的流。
   2. 相比较串行的流，并行的流可以很大程度上提高程序的执行效率。
   3. Java 8 中将并行进行了优化，我们可以很容易的对数据进行并行操作。Stream API 可以声明性地通过 parallel() 与 sequential() 在并行流与顺序流之间进行切换

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092210.png)

## 1、Lambda 表达式

### ①、为什么使用 Lambda 表达式

1. Lambda 是一个匿名函数，我们可以把 Lambda 表达式理解为是一段可以传递的代码（将代码像数据一样进行传递）。使用它可以写出更简洁、更灵活的代码。
2. 作为一种更紧凑的代码风格，使 Java 的语言表达能力得到了提升

### ②、语法

1. Lambda 表达式：在 Java 8 语言中引入的一种新的语法元素和操作符。这个操作符为 `->`，该操作符被称为 Lambda 操作符或箭头操作符。它将 Lambda 分为两个部分：
2. 左侧：指定了 Lambda 表达式需要的参数列表
3. 右侧：指定了 Lambda 体，是抽象方法的实现逻辑，也即Lambda 表达式要执行的功能。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092303.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092326.png)

### ③、类型推断

1. 上述 Lambda 表达式中的参数类型都是由编译器推断得出的。
2. Lambda 表达式中无需指定类型，程序依然可以编译，这是因为 javac 根据程序的上下文，在后台推断出了参数的类型。
3. Lambda 表达式的类型依赖于上下文环境，是由编译器推断出来的。这就是所谓的“类型推断”。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092355.png)

### ④、例子

1. 语法格式一：无参，无返回值

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092408.png)

```java
/**
 * 语法格式一：无参，无返回值
 */
@Test
public void test01(){
    /*
      传统写法
     */
    Runnable r1 = new Runnable() {
        @Override
        public void run() {
            System.out.println("月海");
        }
    };
    r1.run();

    /*
      lambda 表达式
     */
    Runnable r2 = () -> System.out.println("言");
    r2.run();
}
```

2. 语法格式二：Lambda 需要一个参数，但是没有返回值。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092422.png)

3. 语法格式三：数据类型可以省略，因为可由编译器推断得出，称为“类型推断”（由 2 更加简化而来）

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092436.png)

```java
/**
 * 语法格式二：Lambda 需要一个参数，但是没有返回值。
 * 语法格式三：数据类型可以省略，因为可由编译器推断得出，称为“类型推断”
 */
@Test
public void test02(){
    /*
      传统写法
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return Integer.compare(o1, o2);
        }
    };
    System.out.println(c1.compare(1, 2));

    /*
      lambda 表达式
     */
    Comparator<Integer> c2 = (o1, o2) -> Integer.compare(o1, o2);
    System.out.println(c2.compare(2, 1));

    /*
      方法引用
     */
    Comparator<Integer> c3 = Integer::compare;
    System.out.println(c3.compare(1, 1));
}
```

4. 语法格式四：Lambda 若只需要一个参数时，参数的小括号可以省略

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092455.png)

```java
/**
 * 语法格式四：Lambda 若只需要一个参数时，参数的小括号可以省略
 */
@Test
public void test04(){
    /*
      传统写法
     */
    Consumer<String> c1 = new Consumer<String>() {
        @Override
        public void accept(String s) {
            System.out.println(s);
        }
    };
    c1.accept("月海");

    /*
      lambda 表达式
     */
    Consumer<String> c2 = s -> System.out.println(s);
    c2.accept("言");

    /*
      方法引用
     */
    Consumer<String> c3 = System.out::println;
    c3.accept("羽");
}
```

5. 语法格式五：Lambda 需要两个或以上的参数，多条执行语句，并且可以有返回值

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092509.png)

```java
/**
 * 语法格式五：Lambda 需要两个或以上的参数，多条执行语句，并且可以有返回值
 */
@Test
public void test05(){
    /*
      传统写法
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            System.out.println("月海");
            return Integer.compare(o1, o2);
        }
    };
    System.out.println(c1.compare(1, 2));

    /*
      lambda 表达式
     */
    Comparator<Integer> c2 = (o1, o2) -> {
        System.out.println("言");
        return Integer.compare(o1, o2);
    };
    System.out.println(c2.compare(2, 1));
}
```

6. 语法格式六：当Lambda 体只有一条语句时，return 与大括号若有，都可以省略（可由 3 更加简化而来）

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092523.png)

```java
/**
     * 语法格式六：当 Lambda 体只有一条语句时，return 与大括号若有，都可以省略
     */
    @Test
    public void test06(){
        /*
          传统写法
         */
        Comparator<Integer> c1 = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return Integer.compare(o1, o2);
            }
        };
        System.out.println(c1.compare(1, 2));

        /*
          lambda 表达式
         */
        Comparator<Integer> c2 = (o1, o2) -> Integer.compare(o1, o2);
        System.out.println(c2.compare(2, 1));

        /*
          方法引用
         */
        Comparator<Integer> c3 = Integer::compare;
        System.out.println(c3.compare(1, 1));
    }
```

## 2、函数式(Functional)接口

### ①、什么是函数式接口

1. 只包含一个抽象方法的接口，称为函数式接口。
2. 你可以通过 Lambda 表达式来创建该接口的对象。（若 Lambda 表达式抛出一个受检异常（即：非运行时异常），那么该异常需要在目标接口的抽象方法上进行声明）。
3. 我们可以在一个接口上使用 `@FunctionalInterface` 注解，这样做可以检查它是否是一个函数式接口。同时 javadoc 也会包含一条声明，说明这个接口是一个函数式接口。
4. 在 `java.util.function` 包下定义了 Java 8 的丰富的函数式接口

### ②、如何理解函数式接口

1. Java 从诞生日起就是一直倡导“一切皆对象”，在 Java 里面面向对象(OOP)编程是一切。但是随着 python、scala 等语言的兴起和新技术的挑战，Java 不得不做出调整以便支持更加广泛的技术要求，也即 java 不但可以支持 OOP 还可以支持 OOF（面向函数编程）
2. 在函数式编程语言当中，函数被当做一等公民对待。在将函数作为一等公民的编程语言中，Lambda 表达式的类型是函数。但是在 Java8 中，有所不同。在 Java8 中，Lambda 表达式是对象，而不是函数，它们必须依附于一类特别的对象类型——函数式接口。
3. 简单的说，在 Java8 中，Lambda 表达式就是一个函数式接口的实例。这就是 Lambda 表达式和函数式接口的关系。也就是说，只要一个对象是函数式接口的实例，那么该对象就可以用 Lambda 表达式来表示。
4. 所以以前用匿名实现类表示的现在都可以用 Lambda 表达式来写。

### ③、函数式接口举例

```java
package java.lang;

/**
 * Represents an operation that does not return a result.
 *
 * <p> This is a {@linkplain java.util.function functional interface}
 * whose functional method is {@link #run()}.
 *
 * @author  Arthur van Hoff
 * @see     java.util.concurrent.Callable
 * @since   1.0
 */
@FunctionalInterface
public interface Runnable {
    /**
     * Runs this operation.
     */
    void run();
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092549.png)

### ④、自定义函数式接口

#### Ⅰ、`Consumer<T>`  消费型接口

```java
/**
 * 定义一个函数式接口
 * Consumer<T>  消费型接口       void accept(T t)
 * 对类型为 T 的对象应用操作
 */
public void happyTime(double money, Consumer<Double> com){
    com.accept(money);
}

@Test
public void test01(){
    /**
     * 调用接口：以前的方式
     */
    happyTime(500, new Consumer<Double>() {
        @Override
        public void accept(Double aDouble) {
            System.out.println("月海 = " + aDouble);
        }
    });

    /**
     * 调用接口：lambda 表达式的方式
     */
    happyTime(500, aDouble -> System.out.println("月海 = " + aDouble));
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092606.png)

#### Ⅱ、`Predicate<T>` 断定型接口

```java
/**
 * 定义一个函数式接口
 * Predicate<T> 断定型接口       boolean test(T t)
 * 确定类型为 T 的对象是否满足某约束，并返回boolean 值
 *
 * 根据给定的规则，过滤集合中的字符串，此规则由 Predicate 的方法决定（调用时设置）
 */
public List<String> filterString(List<String> list, Predicate<String> predicate){
    // 保存过滤后的字符串
    ArrayList<String> filterList = new ArrayList<>();

    for (String s : list) {
        if (predicate.test(s)){
            filterList.add(s);
        }
    }

    return filterList;
}

@Test
public void test02(){
    /**
     * 调用接口：以前的方式
     * 判断本次处理的字符串是不是中文，是则返回 true；返回是中文的字符串
     */
    List<String> filterString = filterString(Arrays.asList("yuehai", "月", "海", "言"), new Predicate<String>() {
        @Override
        public boolean test(String s) {
            // 判断本次处理的字符串是不是中文，是则返回 true
            return String.valueOf(s).matches("[\\u4e00-\\u9fa5]");
        }
    });
    System.out.println(filterString);

    /**
     * 调用接口：lambda 表达式的方式
     * 判断本次处理的字符串是不是中文，不是则返回 true；返回不是中文的字符串
     */
    List<String> filterString2 = filterString(Arrays.asList("yuehai", "月", "海", "言"), s -> !String.valueOf(s).matches("[\\u4e00-\\u9fa5]"));
    System.out.println(filterString2);
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092641.png)

### ⑤、作为参数传递 Lambda 表达式

作为参数传递 Lambda 表达式：为了将 Lambda 表达式作为参数传递，接收Lambda 表达式的参数类型必须是与该 Lambda 表达式兼容的函数式接口的类型

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092720.png)

### ⑥、Java 内置四大核心函数式接口

| 函数式接口 | 参数类型 | 返回类型 | 用途 |
| --- | --- | --- | --- |
| `Consumer<T>` 消费型接口 | `T` | `void` | 对类型为 `T` 的对象应用操作，包含方法：`void accept(T t)` |
| `Supplier<T>` 供给型接口 | 无 | `T` | 返回类型为 `T` 的对象，包含方法：`T get()` |
| `Function<T, R>` 函数型接口 | `T` | `R` | 对类型为 `T` 的对象应用操作，并返回结果。结果是R类型的对象。包含方法：`R apply(T t)` |
| `Predicate<T>` 断定型接口 | `T` | `boolean` | 确定类型为 `T` 的对象是否满足某约束，并返回boolean 值。包含方法：`boolean test(T t)` |

### ⑦、其他接口

| 函数式接口 | 参数类型 | 返回类型 | 用途 |
| --- | --- | --- | --- |
| `BiFunction<T, U, R>` | `T, U` | `R` | 对类型为 T, U 参数应用操作，返回 R 类型的结果。包含方法为：`R apply(T t, U u);` |
| `UnaryOperator<T>` Function子接口 | `T` | `T` | 对类型为T的对象进行一元运算，并返回T类型的结果。包含方法为：`T apply(T t);` |
| `BinaryOperator<T>` BiFunction 子接口 | `T, T` | `T` | 对类型为T的对象进行二元运算，并返回T类型的结果。包含方法为：`T apply(T t1, T t2);` |
| `BiConsumer<T, U>` | `T, U` | `void` | 对类型为T, U 参数应用操作。包含方法为： `void accept(T t, U u)` |
| `BiPredicate<T, U>`  | `T,U ` | `boolean ` | 包含方法为： `boolean test(T t,U u)` |
| `ToIntFunction`、`ToLongFunction`、`ToDoubleFunction` | `T` | `int`、`long`、`double` | 分别计算int、long、double值的函数 |
| `IntFunction`、`LongFunction`、`DoubleFunction` | `int`、`long`、`double` | `R` | 参数分别为int、long、double 类型的函数 |

## 3、方法引用与构造器引用

### ①、方法引用是什么

1. 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用！
2. 方法引用可以看做是 Lambda 表达式深层次的表达。换句话说，方法引用就是 Lambda 表达式，也就是函数式接口的一个实例，通过方法的名字来指向一个方法，可以认为是 Lambda 表达式的一个语法糖。
3. 要求：实现接口的抽象方法的参数列表和返回值类型，必须与方法引用的方法的参数列表和返回值类型保持一致！
4. 格式：使用操作符 `::` 将类(或对象) 与 方法名分隔开来。
   1. 如下三种主要使用情况：
      1. `对象::实例方法名（非静态方法）`
      2. `类::静态方法名`
      3. `类::实例方法名（非静态方法）`

### ②、方法引用案例

1. 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用

```java
/**
 * 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用！
 */
@Test
public void test01(){
    List<String> list = Arrays.asList("月海", "言", "羽");

    /**
     * 传统写法
     */
    for (String s : list) {
        System.out.print(s + ", ");
    }
    System.out.println();
    /**
     * lambda 表达式
     */
    list.forEach((s) -> System.out.print(s + ", "));
    System.out.println();
    /**
     * 方法引用
     */
    list.forEach(System.out::print);
}
```

2. 先定义一个函数式接口

```java
/**
 * 定义一个函数式接口
 * Consumer<T>  消费型接口       void accept(T t)
 * 对类型为 T 的对象应用操作
 */
public void happyTime(double money, Consumer<Double> com){
    com.accept(money);
}
```

3. 对象::实例方法名（非静态方法）

```java
/**
 * 方法引用可以看做是 Lambda 表达式深层次的表达。
 * 换句话说，方法引用就是 Lambda 表达式，也就是函数式接口的一个实例，通过方法的名字来指向一个方法，可以认为是 Lambda 表达式的一个语法糖。
 * 所以方法引用也是函数式接口的一个实例
 *   1. 对象::实例方法名（非静态方法）
 *   2. 类::静态方法名
 *   3. 类::实例方法名（非静态方法）
 */

/**
 * 1. 对象::实例方法名（非静态方法）
 * Consumer 中的 void accept(T t)
 * PrintStream 中的 void println(T t)
 */
@Test
public void test02(){
    /**
     * 调用接口：以前的方式
     */
    Consumer<String> con1 = new Consumer<String>() {
        @Override
        public void accept(String s) {
            System.out.println("月海 = " + s);
        }
    };
    con1.accept("yuehai");
    /**
     * 调用接口：lambda 表达式的方式
     */
    Consumer<String> con2 = s -> System.out.println("言 = " + s);
    con2.accept("yan");
    /**
     * 方法引用
     */
    Consumer<String> con3 = System.out::println;
    con3.accept("羽");

    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */

    User user = new User("月海", 16);
    /**
     * 调用接口：以前的方式
     */
    Supplier<String> s1 = new Supplier<String>() {
        @Override
        public String get() {
            return user.getName();
        }
    };
    System.out.println(s1.get());
    /**
     * 调用接口：lambda 表达式的方式
     */
    Supplier<String> s2 = () -> user.getName();
    System.out.println(s2.get());
    /**
     * 方法引用
     */
    Supplier<String> s3 = user::getName;
    System.out.println(s3.get());
}
```

4. 类::静态方法名

```java
/**
 * 2. 类::静态方法名
 * Comparator 中的 int compare(T t1,T t2)
 * Integer 中的 int compare(T t1,T t2)
 */
@Test
public void test03(){
    /**
     * 调用接口：以前的方式
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o1.compareTo(o2);
        }
    };
    System.out.println(c1.compare(10, 20));

    /**
     * 调用接口：lambda 表达式的方式
     */
    Comparator<Integer> c2 = (o1, o2) -> o1.compareTo(o2);
    System.out.println(c2.compare(10, 10));

    /**
     * 方法引用
     */
    Comparator<Integer> c3 = Integer::compareTo;
    System.out.println(c3.compare(10, 10));

    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */

    /**
     * Function 中的 R apply(T t)
     * Math 中的 Long round(Double d)
     */
    /**
     * 调用接口：以前的方式
     */
    Function<Double, Long> f1 = new Function<Double, Long>() {
        @Override
        public Long apply(Double aDouble) {
            return Math.round(aDouble);
        }
    };
    System.out.println(f1.apply(11.22));

    /**
     * 调用接口：lambda 表达式的方式
     */
    Function<Double, Long> f2 = d -> Math.round(d);
    System.out.println(f2.apply(22.11));

    /**
     * 方法引用
     */
    Function<Double, Long> f3 = Math::round;
    System.out.println(f3.apply(5.541));
}
```

5. 类::实例方法名（非静态方法）

```java
/**
 * 3. 类::实例方法名（非静态方法）
 * Comparator 中的 int comapre(T t1,T t2)
 * String 中的 int t1.compareTo(t2)
 */
@Test
public void test04() {
    /**
     * 调用接口：以前的方式
     */
    Comparator<String> c1 = new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            return o1.compareTo(o2);
        }
    };
    System.out.println(c1.compare("月海", "言"));
    /**
     * 调用接口：lambda 表达式的方式
     */
    Comparator<String> c2 = (o1, o2) -> o1.compareTo(o2);
    System.out.println(c2.compare("言", "羽"));
    /**
     * 方法引用
     */
    Comparator<String> c3 = String::compareTo;
    System.out.println(c3.compare("月海", "yuehai"));


    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */


    /**
     * BiPredicate 中的 boolean test(T t1, T t2);
     * String 中的 boolean t1.equals(t2)
     */
    /**
     * 调用接口：以前的方式
     */
    BiPredicate<String, String> b1 = new BiPredicate<String, String>() {
        @Override
        public boolean test(String s, String s2) {
            return s.equals(s2);
        }
    };
    System.out.println(b1.test("月海", "月海"));
    /**
     * 调用接口：lambda 表达式的方式
     */
    BiPredicate<String, String> b2 = (s, s2) -> s.equals(s2);
    System.out.println(b2.test("月海", "yuehai"));
    /**
     * 方法引用
     */
    BiPredicate<String, String> b3 = String::equals;
    System.out.println(b3.test("月海", "言"));


    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */


    /**
     * Function中的R apply(T t)
     * Employee中的String getName();
     */
    User user = new User("言", 14);
    /**
     * 调用接口：以前的方式
     */
    Function<User, String> f1 = new Function<User, String>() {
        @Override
        public String apply(User user) {
            return user.getName();
        }
    };
    System.out.println(f1.apply(user));
    /**
     * 调用接口：lambda 表达式的方式
     */
    Function<User, String> f2 = user1 -> user1.getName();
    System.out.println(f2.apply(user));
    /**
     * 方法引用
     */
    Function<User, String> f3 = User::getName;
    System.out.println(f3.apply(user));
}
```

### ③、构造器引用

1. 和方法引用类似，函数式接口的抽象方法的形参列表和构造器的形参列表一致
2. 抽象方法的返回值类型即为构造器所属的类的类型
3. 格式：`ClassName::new`
4. 与函数式接口相结合，自动与函数式接口中方法兼容。
5. 可以把构造器引用赋值给定义的方法，要求构造器参数列表要与接口中抽象方法的参数列表一致！且方法的返回值即为构造器对应类的对象。
6. 案例：

```java
package org.yuehai._03_MethodReferences;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Supplier;

/**
 * @author 月海
 * @create 2023/2/17 8:55
 */
public class ConstructorReferences_01 {

    /**
     * 案例 1
     * Supplier中的T get()
     * User 的空参构造器：User()
     */
    @Test
    public void test01(){
        /**
         * 传统写法
         */
        Supplier<User> s1 = new Supplier<User>() {
            @Override
            public User get() {
                return new User();
            }
        };
        System.out.println(s1.get());
        /**
         * lambda 表达式
         */
        Supplier<User> s2 = () -> new User();
        System.out.println(s2.get());
        /**
         * 构造器（方法）引用
         */
        Supplier<User> s3 = User::new;
        System.out.println(s3.get());
    }

    /**
     * 案例 2
     * Function中的R apply(T t)
     * User 的带参构造器：User()：实体类中要有对应的构造器
     */
    @Test
    public void test02(){
        /**
         * 传统写法
         */
        Function<Integer, User> f1 = new Function<Integer, User>() {
            @Override
            public User apply(Integer integer) {
                return new User(integer);
            }
        };
        System.out.println(f1.apply(14));
        /**
         * lambda 表达式
         */
        Function<Integer, User> f2 = age -> new User(age);
        System.out.println(f2.apply(16));
        /**
         * 构造器（方法）引用
         */
        Function<Integer, User> f3 = User::new;
        System.out.println(f3.apply(18));
    }

    /**
     * 案例 3
     * BiFunction中的R apply(T t,U u)
     * User 的带参构造器：User()：实体类中要有对应的构造器
     */
    @Test
    public void test03(){
        /**
         * 传统写法
         */
        BiFunction<String, Integer, User> b1 = new BiFunction<String, Integer, User>() {
            @Override
            public User apply(String s, Integer integer) {
                return new User(s, integer);
            }
        };
        System.out.println(b1.apply("月海", 16));
        /**
         * lambda 表达式
         */
        BiFunction<String, Integer, User> b2 = (name, age) -> new User(name, age);
        System.out.println(b2.apply("言", 14));
        /**
         * 构造器（方法）引用
         */
        BiFunction<String, Integer, User> b3 = User::new;
        System.out.println(b3.apply("羽", 18));
    }

}
```

### ④、数组引用

1. 可以把数组看做是一个特殊的类，则写法与构造器引用一致
2. 格式： `ClassName::new`
3. 案例：

```java
package org.yuehai._03_MethodReferences;

import org.junit.Test;

import java.util.Arrays;
import java.util.function.Function;

/**
 * @author 月海
 * @create 2023/2/17 9:22
 */
public class ArrayReference_01 {
    /**
     * 数组引用
     * Function中的R apply(T t)
     */
    @Test
    public void test03(){
        /**
         * 传统写法
         */
        Function<Integer, String[]> f1 = new Function<Integer, String[]>() {
            @Override
            public String[] apply(Integer integer) {
                return new String[integer];
            }
        };
        System.out.println(Arrays.toString(f1.apply(2)));
        /**
         * lambda 表达式
         */
        Function<Integer, String[]> f2 = length -> new String[length];
        System.out.println(Arrays.toString(f2.apply(4)));
        /**
         * 构造器（方法）引用
         */
        Function<Integer, String[]> f3 = String[]::new;
        System.out.println(Arrays.toString(f3.apply(6)));
    }
}

```

## 4、强大的 Stream API

### ①、Stream API 说明

1. Java8 中有两大最为重要的改变。第一个是 Lambda 表达式；另外一个则是 Stream API。
2. Stream API ( java.util.stream) 把真正的函数式编程风格引入到 Java 中。这是目前为止对 Java 类库最好的补充，因为 Stream API 可以极大提供 Java 程序员的生产力，让程序员写出高效率、干净、简洁的代码。
3. Stream 是 Java8 中处理集合的关键抽象概念，它可以指定你希望对集合进行的操作，可以执行非常复杂的查找、过滤和映射数据等操作。 使用Stream API 对集合数据进行操作，就类似于使用 SQL 执行的数据库查询。
4. 也可以使用 Stream API 来并行执行操作。简言之，Stream API 提供了一种高效且易于使用的处理数据的方式

### ②、为什么要使用 Stream API

1. 实际开发中，项目中多数数据源都来自于 Mysql，Oracle 等。但现在数据源可以更多了，有 MongDB，Redis 等，而这些 NoSQL 的数据就需要 Java 层面去处理。
2. Stream 和 Collection 集合的区别：Collection 是一种静态的内存数据结构，而 Stream 是有关计算的。
3. 前者是主要面向内存，存储在内存中，后者主要是面向 CPU，通过 CPU 实现计算

### ③、什么是 Stream

1. Stream到底是什么呢？是数据渠道，用于操作数据源（集合、数组等）所生成的元素序列。
2. 集合讲的是数据，Stream讲的是计算！
3. 注意：
   1. Stream 自己不会存储元素。
   2. Stream 不会改变源对象。相反，他们会返回一个持有结果的新Stream。
   3. Stream 操作是延迟执行的。这意味着他们会等到需要结果的时候才执行。

### ④、Stream 的操作三个步骤

1. 创建 Stream：一个数据源（如：集合、数组），获取一个流
2. 中间操作：一个中间操作链，对数据源的数据进行处理
3. 终止操作(终端操作)：一旦执行终止操作，就执行中间操作链，并产生结果。之后，不会再被使用

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726093332.png)

### ⑤、创建 Stream

#### Ⅰ、 通过集合  

1. Java8 中的 Collection 接口被扩展，提供了两个获取流的方法：
2. `default Stream<E> stream()` : 返回一个顺序流
3. `default Stream<E> parallelStream()` : 返回一个并行流

```java
/**
 * 创建 Stream 1 ：通过集合
 */
@Test
public void test01(){
    // 创建一个集合
    List<User> list = Arrays.asList(new User("月海", 16), new User("言", 14), new User("羽", 18));

    // 1、default Stream<E> stream() : 返回一个顺序流
    Stream<User> stream = list.stream();

    // 2、default Stream<E> parallelStream() : 返回一个并行流
    Stream<User> parallelStream = list.parallelStream();
}
```

#### Ⅱ、通过数组

1. Java8 中的 Arrays 的静态方法 stream() 可以获取数组流：`static <T> Stream<T> stream(T[] array)`：返回一个流
2. 重载形式，能够处理对应基本类型的数组：
   1. `public static IntStream stream(int[] array)`
   2. `public static LongStream stream(long[] array)`
   3. `public static DoubleStream stream(double[] array)`

```java
/**
 * 创建 Stream 2 ：通过数组
 */
@Test
public void test02(){
    // 创建一个数组
    int[] arr = new int[]{1, 2, 4 ,7};

    // 调用 Arrays 类的 static <T> Stream<T> stream(T[] array): 返回一个流
    IntStream stream = Arrays.stream(arr);
}
```

#### Ⅲ、通过Stream的of()

1. 可以调用 Stream 类静态方法 of()，通过显示值创建一个流。它可以接收任意数量的参数。
2. `public static<T> Stream<T> of(T... values)`：返回一个流

```java
/**
 * 创建 Stream 3 ：通过 Stream 的 of()
 */
@Test
public void test03(){
    // static<T> Stream<T> of(T... values) : 返回一个流
    Stream<Integer> stream = Stream.of(1, 2, 4, 7);
}
```

#### Ⅳ、创建无限流

1. 自己创建一些数据
2. 可以使用静态方法 `Stream.iterate()` 和 `Stream.generate(`)，创建无限流。
3. 迭代：`public static<T> Stream<T> iterate(final T seed, final UnaryOperator<T> f)`
4. 生成：`public static<T> Stream<T> generate(Supplier<T> s)`

```java
/**
 * 创建 Stream 4 ：创建无限流
 */
@Test
public void test04(){
    /**
     * 迭代
     * public static<T> Stream<T> iterate(final T seed, final UnaryOperator<T> f)
     * 遍历前十个偶数
     * Stream.iterate(0, t -> t + 2)：参数 1：初始值；参数 2：lambda 表达式；该语句会一直反复执行（迭代）
     * limit(10)：只要前十个结果，十个之后就结束
     */
    Stream.iterate(0, t -> t + 2).limit(10).forEach(System.out::println);

    /**
     * 生成
     * public static<T> Stream<T> generate(Supplier<T> s)
     * 取十个随机数
     * Stream.generate(Math::random)：参数 1：lambda 表达式；该语句会一直反复执行（迭代）
     * limit(10)：只要前十个结果，十个之后就结束
     */
    Stream.generate(Math::random).limit(10).forEach(System.out::println);
}
```

### ⑥、Stream 中间操作

1. 多个中间操作可以连接起来形成一个流水线，除非流水线上触发终止操作，否则中间操作不会执行任何的处理！
2. 而在终止操作时一次性全部处理，称为“惰性求值”。

#### Ⅰ、筛选与切片

| 方 法 | 描 述 |
| --- | --- |
| `filter(Predicate p)` | 接收 Lambda ， 从流中排除某些元素 |
| `distinct()` | 筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素 |
| `limit(long maxSize)` | 截断流，使其元素不超过给定数量 |
| `skip(long n)` | 跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 11:00
 */
public class _02_OperationStream_01 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * filter(Predicate p)	接收 Lambda ， 从流中排除某些元素
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：筛选出年龄大于 14；filter(Predicate p)	接收 Lambda ， 从流中排除某些元素
        stream.filter(l -> l.getAge() > 14).forEach(System.out::println);
    }

    /**
     * distinct()	筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：去重；distinct()	筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素
        stream.distinct().forEach(System.out::println);
    }

    /**
     * limit(long maxSize)	截断流，使其元素不超过给定数量
     */
    @Test
    public void test03(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：年龄大于 14，只要前一个；limit(long maxSize)	截断流，使其元素不超过给定数量
        stream.filter(l -> l.getAge() > 14).limit(1).forEach(System.out::println);
    }

    /**
     * skip(long n)	跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补
     */
    @Test
    public void test04(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：年龄大于 14，跳过第一个，只要前一个；skip(long n)	跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补
        stream.filter(l -> l.getAge() > 14).skip(1).limit(1).forEach(System.out::println);
    }
}
```

#### Ⅱ、映射

| 方 法 | 描 述 |
| --- | --- |
| `map(Function f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。 |
| `mapToInt(ToIntFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。 |
| `mapToDouble(ToDoubleFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。 |
| `mapToLong(ToLongFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream. |
| `flatMap(Function f)` | 接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 11:29
 */
public class _02_OperationStream_02 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * map(Function f)	接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：给姓名加前缀
        // map(Function f)	接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
        stream.map( l -> "name：" + l.getName() ).forEach(System.out::println);
    }

    /**
     * mapToInt(ToIntFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 10
        // mapToInt(ToIntFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。
        IntStream intStream = stream.mapToInt(l -> l.getAge() + 10);
        intStream.forEach(System.out::println);
    }

    /**
     * mapToDouble(ToDoubleFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。
     */
    @Test
    public void test03(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 10.1
        // mapToDouble(ToDoubleFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。
        DoubleStream doubleStream = stream.mapToDouble(l -> l.getAge() + 10.1);
        doubleStream.forEach(System.out::println);
    }

    /**
     * mapToLong(ToLongFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream.
     */
    @Test
    public void test04(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 1564864165341365417L
        // mapToLong(ToLongFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream.
        stream.mapToLong(l -> l.getAge() + 1564864165341365417L ).forEach(System.out::println);
    }


    
    
    /**
     * 定义一个方法，将字符串中的多个字符构成的集合转换为对应的 Stream 的实例
     */
    public static Stream<Character> fromStringToStream(String str){
        ArrayList<Character> list = new ArrayList<>();
        for(Character c : str.toCharArray()){
            list.add(c);
        }
        return list.stream();
    }
    /**
     * flatMap(Function f)	接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流
     */
    @Test
    public void test05(){
        // 定义一个集合
        List<String> list5 = Arrays.asList("月海", "言", "羽", "yuehai");

        /**
         * 上面的 map 方法，类似于 list 的 add 方法，作为一个流来进行处理
         * 此处的 flatMap 方法，类似于 list 的 addAll 方法，将其中的元素取出来，每一个元素都作为一个流来进行处理
         */

        // 1、使用 map；类似集合里套集合
        Stream<Stream<Character>> streamStream = list5.stream().map(_02_OperationStream_02::fromStringToStream);
        streamStream.forEach( l -> l.forEach(System.out::println) );

        System.out.println("--------------------------------------");

        // 2、使用 flatMap；不会被嵌套
        Stream<Character> characterStream = list5.stream().flatMap(_02_OperationStream_02::fromStringToStream);
        characterStream.forEach(System.out::println);
    }
}
```

#### Ⅲ、排序

| 方 法 | 描 述 |
| --- | --- |
| `sorted()` | 产生一个新流，其中按自然顺序排序 |
| `sorted(Comparator com)` | 产生一个新流，其中按比较器顺序排序 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 13:22
 */
public class _02_OperationStream_03 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海0", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * sorted()	产生一个新流，其中按自然顺序排序
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：取出年龄创建一个新的流，然后按这个年龄排序
        // sorted()	产生一个新流，其中按自然顺序排序
        stream.mapToInt(User::getAge).sorted().forEach(System.out::println);
    }

    /**
     * sorted()	产生一个新流，其中按比较器顺序排序
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：使用比较器按年龄大小排序
        // sorted()	产生一个新流，其中按比较器顺序排序
        stream.sorted((u1, u2) -> {
            int compareAge = Integer.compare(u1.getAge(), u2.getAge());
            if (compareAge != 0){
                return compareAge;
            }else {
                return u1.getName().compareTo(u2.getName());
            }
        }).forEach(System.out::println);
    }

}
```

### ⑦、Stream 的终止操作

#### Ⅰ、匹配与查找

- 终端操作会从流的流水线生成结果。其结果可以是任何不是流的值，例如：List、Integer，甚至是 void 。
- 流进行了终止操作后，不能再次使用。

| 方 法 | 描 述 |
| --- | --- |
| `allMatch(Predicate p)` | 检查是否匹配所有元素 |
| `anyMatch(Predicate p)` | 检查是否至少匹配一个元素 |
| `noneMatch(Predicate p)` | 检查是否没有匹配所有元素 |
| `findFirst()` | 返回第一个元素 |
| `findAny()` | 返回当前流中的任意元素 |
| `count()` | 返回流中元素总数 |
| `max(Comparator c)` | 返回流中最大值 |
| `min(Comparator c)` | 返回流中最小值 |
| `forEach(Consumer c)` | 内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了) |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 13:53
 */
public class  _03_EndStream {
    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海0", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * allMatch(Predicate p)	检查是否匹配所有元素
     * anyMatch(Predicate p)	检查是否至少匹配一个元素
     * noneMatch(Predicate p)	检查是否没有匹配所有元素
     * findFirst()	返回第一个元素
     * findAny()	返回当前流中的任意元素
     * count()	返回流中元素总数
     * max(Comparator c)	返回流中最大值
     * min(Comparator c)	返回流中最小值
     * forEach(Consumer c)	内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了)
     */
    @Test
    public void test01(){
        /**
         * 3.1、结束操作：检查是否所有人的年龄都大于 14
         * allMatch(Predicate p)	检查是否匹配所有元素
         */
        // System.out.println(list.stream().allMatch(l -> l.getAge() > 14));

        /**
         * 3.2、结束操作：检查是否有人的年龄大于 14
         * anyMatch(Predicate p)	检查是否至少匹配一个元素
         */
        // System.out.println(list.stream().anyMatch(l -> l.getAge() > 14));

        /**
         * 3.3、结束操作：检查是否没有人的年龄大于 14（是否全部小于 14）
         * noneMatch(Predicate p)	检查是否没有匹配所有元素
         */
        // System.out.println(list.stream().noneMatch(l -> l.getAge() > 14));

        /**
         * 3.4、结束操作：
         * findFirst()	返回第一个元素
         */
        // System.out.println(list.stream().findFirst());

        /**
         * 3.5、结束操作：
         * findAny()	返回当前流中的任意元素
         */
        // System.out.println(list.parallelStream().findAny());

        /**
         * 3.6、结束操作：
         * count()	返回流中元素总数
        */
        // System.out.println(list.stream().count());

        /**
         * 3.7、结束操作：
         * max(Comparator c)	返回流中最大值
         */
        // System.out.println(list.stream().mapToInt(User::getAge).max());

        /**
         * 3.8、结束操作：
         * min(Comparator c)	返回流中最小值
         */
        // System.out.println(list.stream().mapToInt(User::getAge).min());

        /**
         * 3.9、结束操作：
         * forEach(Consumer c)	内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了)
         */
        // 内部迭代
        list.stream().forEach(System.out::println);

        System.out.println("------------------------------");

        // 外部迭代
        list.forEach(System.out::println);
    }

}

```

#### Ⅱ、归约

| 方 法 | 描 述 |
| --- | --- |
| `reduce(T iden, BinaryOperator b)` | 可以将流中元素反复结合起来，得到一个值。返回 T |
| `reduce(BinaryOperator b)` | 可以将流中元素反复结合起来，得到一个值。返回 Optional |

```java
/**
 * reduce(T iden, BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 T
 * reduce(BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 Optional
 */
@Test
public void test02(){
    /**
     * 3.1、结束操作：取出集合中所有的年龄，产生一个新流，然后将新流中的年龄求和
     * reduce(T iden, BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 T
     */
    int reduceInt = list.stream().mapToInt(User::getAge).reduce(0, Integer::sum);
    System.out.println(reduceInt);

    /**
     * 3.2、结束操作：取出集合中所有的年龄，产生一个新流，然后将新流中的年龄求和
     * reduce(BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 Optional
     */
    OptionalInt reduceOptionalInt = list.stream().mapToInt(User::getAge).reduce(Integer::sum);
    System.out.println(reduceOptionalInt);
}
```

#### Ⅲ、收集

| 方 法 | 描 述 |
| --- | --- |
| `collect(Collector c)` | 将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法 |

1. Collector 接口中方法的实现决定了如何对流执行收集的操作(如收集到 List、Set、Map)。
2. 另外， Collectors 实用类提供了很多静态方法，可以方便地创建常见收集器实例，具体方法与实例如下表：

| 方法 | 返回类型 | 作用 | 举例 |
| --- | --- | --- | --- |
| `toList` | List | 把流中元素收集到List | List emps= list.stream().collect(Collectors.toList()); |
| `toSet` | Set | 把流中元素收集到Set | Set emps= list.stream().collect(Collectors.toSet()); |
| `toCollection` | Collection | 把流中元素收集到创建的集合 | Collection emps =list.stream().collect(Collectors.toCollection(ArrayList::new)); |
| `counting` | Long | 计算流中元素的个数 | long count = list.stream().collect(Collectors.counting()); |
| `summingInt` | Integer | 对流中元素的整数属性求和 | int total=list.stream().collect(Collectors.summingInt(Employee::getSalary)); |
| `averagingInt` | Double | 计算流中元素Integer属性的平均值 | double avg = ist.stream().collect(Collectors.averagingInt(Employee::getSalary)); |
| `summarizingInt` | IntSummaryStatistics | 收集流中Integer属性的统计值。如：平均值 | int SummaryStatisticsiss=ist.stream().collect(Collectors.summarizingInt(Employee::getSalary)); |
| `joining` | String | 连接流中每个字符串 | String str= list.stream().map(Employee::getName).collect(Collectors.joining()); |
| `maxBy` | Optional | 根据比较器选择最大值 | Optionalmax= list.stream().collect(Collectors.maxBy(comparingInt(Employee::getSalary))); |
| `minBy` | Optional | 根据比较器选择最小值 | Optional min = list.stream().collect(Collectors.minBy(comparingInt(Employee::getSalary))); |
| `reducing` | 归约产生的类型 | 从一个作为累加器的初始值开始，利用BinaryOperator与流中元素逐个结合，从而归约成单个值 | int total=list.stream().collect(Collectors.reducing(0, Employee::getSalar, Integer::sum)); |
| `collectingAndThen` | 转换函数返回的类型 | 包裹另一个收集器，对其结果转换函数 | int how= list.stream().collect(Collectors.collectingAndThen(Collectors.toList(), List::size)); |
| `groupingBy` | Map<K, List> | 根据某属性值对流分组，属性为K，结果为V | Map<Emp.Status, List> map= list.stream().collect(Collectors.groupingBy(Employee::getStatus)); |
| `partitioningBy` | Map<Boolean, List> | 根据true或false进行分区 | Map<Boolean,List> vd = list.stream().collect(Collectors.partitioningBy(Employee::getManage)); |

```java
/**
 * collect(Collector c)	将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法
 */
@Test
public void test03(){
    /**
     * 3、结束操作：
     * collect(Collector c)	将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法
     */

    /**
     * toList	List	把流中元素收集到List
     */
    List<User> collect = list.stream().collect(Collectors.toList());
    collect.forEach(System.out::println);

    /**
     * joining	String	连接流中每个字符串
     */
    String collect1 = list.stream().map(User::getName).collect(Collectors.joining());
    System.out.println(collect1);
}
```

## 5、Optional 类

### ①、介绍

1. 到目前为止，臭名昭著的空指针异常是导致 Java 应用程序失败的最常见原因。
2. 以前，为了解决空指针异常，Google 公司著名的 Guava 项目引入了 Optional 类，Guava 通过使用检查空值的方式来防止代码污染，它鼓励程序员写更干净的代码。受到 Google Guava 的启发，Optional 类已经成为 Java 8 类库的一部分。
3. `Optional<T>` 类(java.util.Optional) 是一个容器类，它可以保存类型 T 的值，代表这个值存在。或者仅仅保存 null，表示这个值不存在。原来用 null 表示一个值不存在，现在 Optional 可以更好的表达这个概念。并且可以避免空指针异常。
4. Optional 类的 Javadoc 描述如下：这是一个可以为 null 的容器对象。如果值存在则 `isPresent()` 方法会返回 true，调用 get() 方法会返回该对象

### ②、方法案例

- Optional提供很多有用的方法，这样我们就不用显式进行空值检测：
1. 创建 Optional 类对象的方法：
   1. `Optional.of(T t)` : 创建一个 Optional 实例，t必须非空；
   2. `Optional.empty()`: 创建一个空的 Optional 实例
   3. `Optional.ofNullable(T t)`：t 可以为 null

```java
/**
 * 创建 Optional 类对象的方法：
 *      Optional.of(T t) : 创建一个 Optional 实例，t必须非空；
 *      Optional.empty(): 创建一个空的 Optional 实例
 *      Optional.ofNullable(T t)：t 可以为 null
 */
@Test
public void test01(){
    User user = new User();

    /**
     * Optional.of(T t) : 创建一个 Optional 实例，t必须非空；
     */
    Optional<User> optional = Optional.of(user);
    System.out.println(optional);

    /**
     * Optional.ofNullable(T t)：t 可以为 null
     */
    user = null;
    Optional<User> optional2 = Optional.ofNullable(user);
    System.out.println(optional2);

    /**
     * Optional.empty(): 创建一个空的 Optional 实例
     */
    Optional<User> optional3 = Optional.empty();
    System.out.println(optional3);
}
```

2. 判断 Optional 容器中是否包含对象：

   1. `boolean isPresent()` : 判断是否包含对象
   2. `void ifPresent(Consumer<? super T> consumer)`：如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。

```java
/**
 * 判断 Optional 容器中是否包含对象：
 *      boolean isPresent() : 判断是否包含对象
 *      void ifPresent(Consumer<? super T> consumer)：如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。
 */
@Test
public void test02(){
    // 创建 Optional 对象
    Optional<User> optional = Optional.of(new User());
    Optional<User> optional2 = Optional.empty();

    /**
     * boolean isPresent() : 判断是否包含对象
     */
    System.out.println(optional.isPresent());
    System.out.println(optional2.isPresent());

    /**
     * void ifPresent(Consumer<? super T> consumer)：
     * 如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。
     * 如果没有值，则不进行任何操作
     */
    optional.ifPresent(System.out::println);
    optional2.ifPresent(System.out::println);
}
```

3. 获取 Optional 容器的对象：

   1. `T get()`: 如果调用对象包含值，返回该值，否则抛异常
   2. `T orElse(T other)`：如果有值则将其返回，否则返回指定的 other 对象。
   3. `T orElseGet(Supplier<? extends T> other)` ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
   4. `T orElseThrow(Supplier<? extends X> exceptionSupplier)`：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。

```java
/**
 * 获取 Optional 容器的对象：
 *      T get(): 如果调用对象包含值，返回该值，否则抛异常
 *      T orElse(T other)：如果有值则将其返回，否则返回指定的 other 对象。
 *      T orElseGet(Supplier<? extends T> other) ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
 *      T orElseThrow(Supplier<? extends X> exceptionSupplier)：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。
 */
@Test
public void test03() throws Exception {
    // 创建 Optional 对象
    Optional<User> optional = Optional.of(new User("月海", 16));
    Optional<User> optional2 = Optional.empty();

    /**
     * T get(): 如果调用对象包含值，返回该值，否则抛异常
     */
    System.out.println(optional.get());
    System.out.println(optional2.get());

    /**
     * T orElse(T other)：如果有值则将其返回，否则返回指定的 other 对象。
     */
    System.out.println(optional.orElse(new User()));
    System.out.println(optional2.orElse(new User()));

    /**
     * T orElseGet(Supplier<? extends T> other) ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
     */
    System.out.println(optional.orElseGet(() -> new User("言", 14)));
    System.out.println(optional2.orElseGet(() -> new User("言", 14)));

    /**
     * T orElseThrow(Supplier<? extends X> exceptionSupplier)：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。
     */
    System.out.println(optional.orElseThrow(Exception::new));
    System.out.println(optional2.orElseThrow(Exception::new));
}
```

## 6、新的日期时间 API

### ①、出现背景

1. 如果我们可以跟别人说：“我们在1502643933071见面，别晚了！”那么就再简单不过了。但是我们希望时间与昼夜和四季有关，于是事情就变复杂了。
2. JDK 1.0 中包含了一个 java.util.Date 类，但是它的大多数方法已经在 JDK 1.1 引入 Calendar 类之后被弃用了。而 Calendar 并不比 Date 好多少。
3. 它们面临的问题是：
   1. 可变性：像日期和时间这样的类应该是不可变的。
   2. 偏移性：Date 中的年份是从 1900 开始的，而月份都从 0 开始。
   3. 格式化：格式化只对 Date 有用，Calendar 则不行。
   4. 此外，它们也不是线程安全的；不能处理闰秒等。
4. 总结：对日期和时间的操作一直是Java程序员最痛苦的地方之一。

### ②、新时间日期 API

1. 第三次引入的 API 是成功的，并且 Java 8 中引入的 java.time API 已经纠正了过去的缺陷，将来很长一段时间内它都会为我们服务。
2. Java 8 吸收了 Joda-Time 的精华，以一个新的开始为 Java 创建优秀的 API。
3. 新的 java.time 中包含了所有关于本地日期（LocalDate）、本地时间（LocalTime）、本地日期时间（LocalDateTime）、时区（ZonedDateTime）和持续时间（Duration）的类。
4. 历史悠久的 Date 类新增了 toInstant() 方法，用于把 Date 转换成新的表示形式。这些新增的本地化时间日期 API 大大简化了日期时间和本地化的管理。
5. 具体的包：
   1. `java.time` – 包含值对象的基础包
   2. `java.time.chrono` – 提供对不同的日历系统的访问
   3. `java.time.format` – 格式化和解析时间和日期
   4. `java.time.temporal` – 包括底层框架和扩展特性
   5. `java.time.zone` – 包含时区支持的类
6. 说明：大多数开发者只会用到基础包和 format 包，也可能会用到 temporal 包。因此，尽管有 68 个新的公开类型，大多数开发者，大概将只会用到其中的三分之一。

### ③、`LocalDate`、`LocalTime`、`LocalDateTime`

1.  LocalDate、LocalTime、LocalDateTime 类是其中较重要的几个类，它们的实例是不可变的对象，分别表示使用 ISO-8601日历系统的日期、时间、日期和时间。
2. 它们提供了简单的本地日期或时间，并不包含当前的时间信息，也不包含与时区相关的信息。
3. LocalDate 代表IOS格式（yyyy-MM-dd）的日期，可以存储生日、纪念日等日期。
4. LocalTime 表示一个时间，而不是日期。
5. LocalDateTime 是用来表示日期和时间的，这是一个最常用的类之一。
6. 注：ISO-8601日历系统是国际标准化组织制定的现代公民的日期和时间的表示法，也就是公历。

| 方法 | 描述 |
| --- | --- |
| `now()` / `* now(ZoneId zone)` | 实例化方式 1：静态方法，根据当前时间创建对象/指定时区的对象 |
| `of()` | 实例化方式2：静态方法，根据指定日期/时间创建对象 |
| `getDayOfMonth()`/`getDayOfYear()` | 获得月份天数(1-31) /获得年份天数(1-366) |
| `getDayOfWeek()` | 获得星期几(返回一个 DayOfWeek 枚举值，英文) |
| `getMonth()` | 获得月份，返回一个 Month 枚举值（英文） |
| `getMonthValue()` / `getYear()` | 获得月份(1-12) /获得年份（数字） |
| `getHour()`/`getMinute()`/`getSecond()` | 获得当前对象对应的小时、分钟、秒 |
| `withDayOfMonth()`/`withDayOfYear()`/`withMonth()`/`withYear()` | 将月份天数、年份天数、月份、年份修改为指定的值并返回新的对象 |
| `plusDays()`/`plusWeeks()`/`plusMonths()`/`plusYears()`/`plusHours()` | 向当前对象添加几天、几周、几个月、几年、几小时 |
| `minusMonths()` / `minusWeeks()`/`minusDays()`/`minusYears()`/`minusHours()` | 从当前对象减去几月/几周、几天、几年、几小时 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

/**
 * @author 月海
 * @create 2023/2/17 16:52
 */
public class _01_DateTime {

    /**
     * LocalDate 代表IOS格式（yyyy-MM-dd）的日期，可以存储生日、纪念日等日期。
     * LocalTime 表示一个时间，而不是日期。
     * LocalDateTime 是用来表示日期和时间的，这是一个最常用的类之一。
     */
    @Test
    public void test01(){
        // 实例化方式 1 ：now() / * now(ZoneId zone)	静态方法，根据当前时间创建对象/指定时区的对象
        LocalDate localDateNow = LocalDate.now();
        System.out.println(localDateNow);

        LocalTime localTimeNow = LocalTime.now();
        System.out.println(localTimeNow);

        LocalDateTime localDateTimeNow = LocalDateTime.now();
        System.out.println(localDateTimeNow);

        // 实例化方式 2 ：of()	静态方法，根据指定日期/时间创建对象
        LocalDateTime localDateTimeOf = LocalDateTime.of(2020, 11, 21, 13, 23, 43);
        System.out.println(localDateTimeOf);


        // getDayOfMonth()/getDayOfYear()	获得月份天数(1-31) /获得年份天数(1-366)
        System.out.println("当月的第几天：" + localDateTimeNow.getDayOfMonth());
        System.out.println("今年的第几天：" + localDateTimeNow.getDayOfYear());

        // getDayOfWeek()	获得星期几(返回一个 DayOfWeek 枚举值)
        System.out.println("星期几（英文）：" + localDateTimeNow.getDayOfWeek());

        // getMonth()	获得月份, 返回一个 Month 枚举值
        System.out.println("几月（英文）：" + localDateTimeNow.getMonth());

        // getMonthValue() / getYear()	获得月份(1-12) /获得年份
        System.out.println("月份（数字）：" + localDateTimeNow.getMonthValue());
        System.out.println("年份（数字）：" + localDateTimeNow.getYear());

        // getHour()/getMinute()/getSecond()	获得当前对象对应的小时、分钟、秒

        // withDayOfMonth()/withDayOfYear()/withMonth()/withYear()	将月份天数、年份天数、月份、年份修改为指定的值并返回新的对象

        // plusDays()/plusWeeks()/plusMonths()/plusYears()/plusHours()	向当前对象添加几天、几周、几个月、几年、几小时
        System.out.println("今年加上 2 年之后：" + localDateTimeNow.plusYears(2));

        // minusMonths() / minusWeeks()/minusDays()/minusYears()/minusHours()	从当前对象减去几月/几周、几天、几年、几小时

    }
    
}
```

### ④、瞬时 `Instant`

1. Instant：时间线上的一个瞬时点。 这可能被用来记录应用程序中的事件时间戳。
2. 在处理时间和日期的时候，我们通常会想到年、月、日、时、分、秒。然而，这只是时间的一个模型，是面向人类的。第二种通用模型是面向机器的，或者说是连续的。在此模型中，时间线中的一个点表示为一个很大的数，这有利于计算机处理。
3. 在 UNIX 中，这个数从 1970 年开始，以秒为的单位；同样的，在 Java 中，也是从 1970 年开始，但以毫秒为单位。
4. java.time 包通过值类型 Instant 提供机器视图，不提供处理人类意义上的时间单位。Instant 表示时间线上的一点，而不需要任何上下文信息，例如，时区。
5. 概念上讲，它只是简单的表示自 1970 年 1 月 1 日 0 时 0 分 0 秒（UTC）开始的秒数。因为 java.time 包是基于纳秒计算的，所以 Instant 的精度可以达到纳秒级。
6. (1 ns = 10-9 s) 1秒 = 1000毫秒 =10^6微秒=10^9纳秒

| 方法 | 描述 |
| --- | --- |
| `now()` | 实例化方式 1：静态方法，返回默认 UTC 时区的 Instant 类的对象 |
| `ofEpochMilli(long epochMilli) ` | 实例化方式 2：静态方法，返回在 1970-01-01 00:00:00 基础上加上指定毫秒数之后的 Instant 类的对象 |
| `atOffset(ZoneOffset offset)` | 结合即时的偏移来创建一个 OffsetDateTime |
| `toEpochMilli()` | 返回 1970-01-01 00:00:00 到当前时间的毫秒数，即为时间戳 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * @author 月海
 * @create 2023/2/20 8:43
 */
public class _02_Instant {

    @Test
    public void test(){
        // 实例化方式 1： now()	静态方法，返回默认 UTC 时区的 Instant 类的对象；中时区（本初子午线）
        Instant instant = Instant.now();
        System.out.println("英国时间：" + instant);

        // 实例化方式 2：atOffset(ZoneOffset offset)	结合即时的偏移来创建一个 OffsetDateTime（中国为东 8 区）
        OffsetDateTime offsetDateTime = instant.atOffset(ZoneOffset.ofHours(8));
        System.out.println("中国时间" + offsetDateTime);

        // ofEpochMilli(long epochMilli) 	静态方法，返回在 1970-01-01 00:00:00 基础上加上指定毫秒数之后的 Instant 类的对象
        System.out.println(Instant.ofEpochMilli(154635412415L));

        // toEpochMilli()	返回 1970-01-01 00:00:00 到当前时间的毫秒数，即为时间戳
        System.out.println(instant.toEpochMilli());
    }

}
```

- 时间戳是指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726093207.png)

### ⑤、格式化与解析日期或时间 `DateTimeFormatter`

1. java.time.format.DateTimeFormatter 类提供了三种格式化方法：
2. 预定义的标准格式。如：
   1. `ISO_LOCAL_DATE_TIME`
   2. `ISO_LOCAL_DATE`
   3. `ISO_LOCAL_TIME`
3. 本地化相关的格式。如：`ofLocalizedDateTime(FormatStyle.LONG)`
4. 自定义的格式。如：`ofPattern("yyyy-MM-dd hh:mm:ss")`

| 方法 | 描述 |
| --- | --- |
| `ofPattern(String pattern)` | 静态方法，返回一个指定字符串格式的 DateTimeFormatter |
| `format(TemporalAccessor t) ` | 格式化一个日期、时间，返回字符串 |
| `parse(CharSequence text)` | 将指定格式的字符序列解析为一个日期、时间 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.time.temporal.TemporalAccessor;

/**
 * @author 月海
 * @create 2023/2/20 9:02
 */
public class _03_DateTimeFormatter {

    /**
     * 1. 预定义的标准格式。如：
     *   a. ISO_LOCAL_DATE_TIME
     *   b. ISO_LOCAL_DATE
     *   c. ISO_LOCAL_TIME
     * 2. 本地化相关的格式。如：ofLocalizedDateTime(FormatStyle.LONG)
     * 3. 自定义的格式。如：ofPattern("yyyy-MM-dd hh:mm:ss")
     */

    /**
     * 1. 预定义的标准格式。如：
     *      a. ISO_LOCAL_DATE_TIME
     *      b. ISO_LOCAL_DATE
     *      c. ISO_LOCAL_TIME
     */
    @Test
    public void test01(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        DateTimeFormatter isoLocalDate = DateTimeFormatter.ISO_LOCAL_DATE;
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = isoLocalDate.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = isoLocalDate.parse(format);

        // 不格式化：2023-02-20T09:07:06.374653300
        System.out.println(localDateTime);
        // 格式化：2023-02-20；
        System.out.println(format);
        // 解析：{},ISO resolved to 2023-02-20
        System.out.println(parse);
    }

    /**
     * 2. 本地化相关的格式。如：ofLocalizedDateTime(FormatStyle.LONG)
     */
    @Test
    public void test02(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        // java.time.ZoneId.systemDefault()：获取系统默认时区
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.LONG).withZone(ZoneId.systemDefault());
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = dateTimeFormatter.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = dateTimeFormatter.parse(format);

        // 不格式化：2023-02-20T09:25:20.183983500
        System.out.println(localDateTime);
        // 格式化：2023年2月20日 CST 09:25:20
        System.out.println(format);
        // 解析：{InstantSeconds=1676906720},ISO,America/Chicago,0 resolved to 2023-02-20T09:25:20
        System.out.println(parse);
    }

    /**
     * 3. 自定义的格式。如：ofPattern("yyyy-MM-dd hh:mm:ss")
     */
    @Test
    public void test03(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss");
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = dateTimeFormatter.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = dateTimeFormatter.parse(format);

        // 不格式化：2023-02-20T09:31:02.432417900
        System.out.println(localDateTime);
        // 格式化：2023-02-20 09:31:02
        System.out.println(format);
        // 解析：{SecondOfMinute=2, MicroOfSecond=0, MinuteOfHour=31, NanoOfSecond=0, HourOfAmPm=9, MilliOfSecond=0},ISO resolved to 2023-02-20
        System.out.println(parse);
    }

}
```

### ⑥、其它 API

| 方法 | 描述 |
| --- | --- |
| `ZoneId` | 该类中包含了所有的时区信息，一个时区的 ID，如 Europe/Paris；systemDefault() 为系统默认时区 |
| `ZonedDateTime` | 一个在 ISO-8601 日历系统时区的日期时间，如 2007-12-03T10:15:30+01:00 Europe/Paris<br/>其中每个时区都对应着 ID，地区 ID 都为“{区域}/{城市}”的格式，例如：Asia/Shanghai 等 |
| `Clock` | 使用时区提供对当前即时、日期和时间的访问的时钟。 |
| 持续时间 `Duration` | 用于计算两个“时间”间隔 |
| 日期间隔 `Period` | 用于计算两个“日期:间隔 |
| `TemporalAdjuster` | 时间校正器。有时我们可能需要获取例如：将日期调整到“下一个工作日”等操作。 |
| `TemporalAdjusters` | 该类通过静态方法(`firstDayOfXxx()`/`lastDayOfXxx()`/`nextXxx()`)提供了大量的常用 `TemporalAdjuster` 的实现. |

```java
//ZoneId:类中包含了所有的时区信息
// ZoneId的getAvailableZoneIds():获取所有的ZoneId
Set<String> zoneIds = ZoneId.getAvailableZoneIds();
for (String s : zoneIds) {
    System.out.println(s);
}
// ZoneId的of():获取指定时区的时间
LocalDateTime localDateTime = LocalDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(localDateTime);
//ZonedDateTime:带时区的日期时间
// ZonedDateTime的now():获取本时区的ZonedDateTime对象
ZonedDateTime zonedDateTime = ZonedDateTime.now();
System.out.println(zonedDateTime);
// ZonedDateTime的now(ZoneId id):获取指定时区的ZonedDateTime对象
ZonedDateTime zonedDateTime1 = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(zonedDateTime1);

//Duration:用于计算两个“时间”间隔，以秒和纳秒为基准
LocalTime localTime = LocalTime.now();
LocalTime localTime1 = LocalTime.of(15, 23, 32);
//between():静态方法，返回Duration对象，表示两个时间的间隔
Duration duration = Duration.between(localTime1, localTime);
System.out.println(duration);
System.out.println(duration.getSeconds());
System.out.println(duration.getNano());
LocalDateTime localDateTime = LocalDateTime.of(2016, 6, 12, 15, 23, 32);
LocalDateTime localDateTime1 = LocalDateTime.of(2017, 6, 12, 15, 23, 32);
Duration duration1 = Duration.between(localDateTime1, localDateTime);
System.out.println(duration1.toDays());

//Period:用于计算两个“日期”间隔，以年、月、日衡量
LocalDate localDate = LocalDate.now();
LocalDate localDate1 = LocalDate.of(2028, 3, 18);
Period period = Period.between(localDate, localDate1);
System.out.println(period);
System.out.println(period.getYears());
System.out.println(period.getMonths());
System.out.println(period.getDays());
Period period1 = period.withYears(2);
System.out.println(period1);

// TemporalAdjuster:时间校正器
// 获取当前日期的下一个周日是哪天？
TemporalAdjuster temporalAdjuster = TemporalAdjusters.next(DayOfWeek.SUNDAY);
LocalDateTime localDateTime = LocalDateTime.now().with(temporalAdjuster);
System.out.println(localDateTime);
// 获取下一个工作日是哪天？
LocalDate localDate = LocalDate.now().with(new TemporalAdjuster() {
    @Override
    public Temporal adjustInto(Temporal temporal) {
        LocalDate date = (LocalDate) temporal;
        if (date.getDayOfWeek().equals(DayOfWeek.FRIDAY)) {
            return date.plusDays(3);
        } else if (date.getDayOfWeek().equals(DayOfWeek.SATURDAY)) {
            return date.plusDays(2);
        } else {
            return date.plusDays(1);
        }
    }
});
System.out.println("下一个工作日是：" + localDate);
```

### ⑦、与传统日期处理的转换

| 类 | To 遗留类 | To 遗留类 |
| --- | --- | --- |
| `java.time.Instant`与`java.util.Date` | Date.from(instant) | date.toInstant() |
| `java.time.Instant`与`java.sql.Timestamp` | Timestamp.from(instant) | timestamp.toInstant() |
| `java.time.ZonedDateTime`与`java.util.GregorianCalendar` | GregorianCalendar.from(zonedDateTime) | cal.toZonedDateTime() |
| `java.time.LocalDate`与`java.sql.Time` | Date.valueOf(localDate) | date.toLocalDate() |
| `java.time.LocalTime`与`java.sql.Time` | Date.valueOf(localDate) | date.toLocalTime() |
| `java.time.LocalDateTime`与`java.sql.Timestamp` | Timestamp.valueOf(localDateTime) | timestamp.toLocalDateTime() |
| `java.time.ZoneId`与`java.util.TimeZone` | Timezone.getTimeZone(id) | timeZone.toZoneId() |
| `java.time.format.DateTimeFormatter`与`java.text.DateFormat` | formatter.toFormat() | 无 |

## 7、接口的默认方法和静态方法

## 8、Nashorn、JavaScript 引擎

## 9、Base64

# 二十二、

# 二十三、

# 二十四、

# 二十五、

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

