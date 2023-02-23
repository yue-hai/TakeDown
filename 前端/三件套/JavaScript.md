> [https://developer.aliyun.com/course/1724](https://developer.aliyun.com/course/1724)，这个视频讲的很差
> [JavaScript.jpg](https://www.yuque.com/attachments/yuque/0/2023/jpeg/29280567/1673925551184-ff76a5e4-fb3d-43ba-a897-2677415f7f07.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fjpeg%2F29280567%2F1673925551184-ff76a5e4-fb3d-43ba-a897-2677415f7f07.jpeg%22%2C%22name%22%3A%22JavaScript.jpg%22%2C%22size%22%3A100196%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22uc104194c-175e-456e-b8eb-04da2d9d14d%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u5d721911%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

## 一、JavaScript 简介
### 1、javaScript 编程语言
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655858632160-4a2351d5-5ec6-426a-8508-6b61b336ba1e.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=550&id=u339a1335&name=image.png&originHeight=550&originWidth=821&originalType=binary&ratio=1&rotation=0&showTitle=false&size=274650&status=done&style=stroke&taskId=u91d44bcc-19c9-4cd6-96b6-2840ee2573d&title=&width=821)
### 2、发展历史及学习概要 
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655859594530-7f9d33dd-5c4c-4455-a090-fa8b01a1894a.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=565&id=u4f9bac74&name=image.png&originHeight=836&originWidth=1238&originalType=binary&ratio=1&rotation=270&showTitle=false&size=1039997&status=done&style=stroke&taskId=uee625f18-d9ca-497e-a37d-f9ba73eda93&title=&width=836)
### 3、ECMAScript 与 JavaScript
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655860039733-d3561cc5-8ef8-4872-8aec-3e7253b6696b.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=83&id=u67d513b8&name=image.png&originHeight=83&originWidth=821&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71422&status=done&style=stroke&taskId=u5a024945-0a41-4cd1-a4d5-03b852f6495&title=&width=821)
### 4、JavaScript 和 HTML、CSS
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655860074158-0a34f738-debc-4085-bec2-42d16f85d97b.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=101&id=ua153d241&name=image.png&originHeight=101&originWidth=462&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53168&status=done&style=stroke&taskId=u2a903bf9-7c3f-42b6-a48d-60da0946322&title=&width=462)
### 5、JS 学习概括
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655860294509-dbb50bfd-9f28-4f03-9d53-410817dbe3a3.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=713&id=u9550a784&name=image.png&originHeight=713&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=322740&status=done&style=stroke&taskId=ub5f69fb5-332b-4359-a7b8-2416cfcc31a&title=&width=828)
## 二、JavaScript 入门
### 1、怎么写 js 代码

1. 写在行内
2. 写在 script 标签中
3. 引入外部 js 文件
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <!-- 将 js 代码写在行内 -->
    <input type="button" value="按钮" onclick="alert(123)">

    <!-- 将 js 代码写在 script 标签中 -->
    <script>
        alert(456);
    </script>

    <!-- 在 HTML 中引入外部 js 文件 -->
    <!-- 注意：若使用外部引入的方式，那么这个 script 标签中就不要再写其他的 js 代码了，有也不会被运行 -->
    <script src="./js/5.js"></script>

</body>
</html>
```
```javascript
alert(789);
```
### 2、变量
#### ①、什么是变量
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655862784550-730f211a-72db-4163-8294-fc661bd4d59c.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=171&id=u2cde0893&name=image.png&originHeight=171&originWidth=661&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81104&status=done&style=stroke&taskId=udf9a43af-e532-4959-ac43-614bcd426cb&title=&width=661) 
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655863110377-1b2553a0-a69d-4d4c-ba8e-e5defea5d83c.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=427&id=u6fe52804&name=image.png&originHeight=427&originWidth=367&originalType=binary&ratio=1&rotation=0&showTitle=false&size=93635&status=done&style=stroke&taskId=u9b53e2c0-c72c-44da-b586-f886b6dd0f6&title=&width=367)
#### ②、变量命名规则

1. 变量的名字必须是：数字、字母、下划线_、和 $ 组成（一种或几种）。
2. 变量的名字不能以数字开头。
3. 变量的名字不能是关键字。
4. 在 js 中变量名是区分大小写的。
5. 建议变量名一定要有意义（见名知意）。
6. 变量命名尽可能使用驼峰命名法。
## 三、JavaScript 数据类型
### 1、数值、字符串
#### ①、数值型（number）

1. 直接定义的数字即数值型。
2. 在 js 中整形与浮点型都可以直接定义
```javascript
var a = 1;
var b = 1.1;
```
#### ②、字符串（String）

1. 定义字符串需用双引号或单引号引起来。
2. 如果在字符串中使用引号，需使用转义字符：\" 。
```javascript
var str1 = "月海";
var str2 = "\"月海\"";
```
#### ③、JS 中的 + 号

1. + 既可以作为数学运算符使用，也可以作为字符串拼接使用
2. 从前往后进行运算，如果两个变量都是数值型，那么 + 作为数学运算符
3. 直到遇到一个字符串，此后所有的 + 都是字符串拼接
#### ④、转义字符
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655864685890-69e985fa-0992-42ff-8257-0cdff3013b5c.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=359&id=uc2424e0f&name=image.png&originHeight=359&originWidth=884&originalType=binary&ratio=1&rotation=0&showTitle=false&size=117710&status=done&style=stroke&taskId=uc8ee0142-5da9-420c-8701-2d75c0b027e&title=&width=884)
### 2、其他数据类型
#### ①、布尔型（Boolen）

1. Boolen 字面量：true 和 false，区分大小写
2. 计算机内部存储：true 为 1，false 为 0
#### ②、undefined

- undefined 表示一个声明了没有赋值的变量，变量只声明的时候值默认是 undefined
#### ③、null

- null 表示一个空，变量的值如果想为 null，必须手动设置
#### ④、对象（Object）

- 复杂数据类型，后面详解
### 3、检测数据类型
#### ①、在控制台检测

- 在控制台打印语句中使用 typeof 检测
```javascript
var i = "5";

console.log(typeof i);
```

- 这样打印时就会显示变量的数据类型

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655867464357-f39d8d2b-9ae2-485b-a52d-9171b4511dc8.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=116&id=u06bb78a9&name=image.png&originHeight=116&originWidth=291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6058&status=done&style=stroke&taskId=uccf33468-6b51-48bc-873e-d7f968b1eae&title=&width=291)
#### ②、在谷歌浏览器中快速查看数据类型
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655866617863-85c55e7a-6472-4cba-b76d-0207b438ef3c.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=191&id=Wmlc0&name=image.png&originHeight=191&originWidth=901&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63423&status=done&style=stroke&taskId=u7a1e662d-8da4-4a5c-ba8b-114d836f5e0&title=&width=901)
```javascript
/* 控制台打印数据类型 */
console.log("月海",22,null,undefined,true)
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655866842795-05f92b4a-6bfe-40ba-ab48-2e413a7533be.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=118&id=G0Sd6&name=image.png&originHeight=118&originWidth=327&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7593&status=done&style=stroke&taskId=u7597ff72-e23a-4eb2-ba25-fc1f605e9bd&title=&width=327)
### 4、注释
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655867062063-4a2760f3-f1b4-4e89-a70e-7d4f602db9ad.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=436&id=u5664af1d&name=image.png&originHeight=436&originWidth=413&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89872&status=done&style=stroke&taskId=u1036c055-9294-428a-98bc-bea28be4d0e&title=&width=413)
### 5、其他类型转为字符串
#### ①、toString() 方法
```javascript
var i = 5;
var s = i.toString();

console.log(typeof s);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655867464357-f39d8d2b-9ae2-485b-a52d-9171b4511dc8.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=116&id=KWaiZ&name=image.png&originHeight=116&originWidth=291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6058&status=done&style=stroke&taskId=uccf33468-6b51-48bc-873e-d7f968b1eae&title=&width=291)
#### ②、String()
```javascript
var i = 5;

console.log(typeof String(i));
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655867464357-f39d8d2b-9ae2-485b-a52d-9171b4511dc8.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=116&id=EOGCG&name=image.png&originHeight=116&originWidth=291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6058&status=done&style=stroke&taskId=uccf33468-6b51-48bc-873e-d7f968b1eae&title=&width=291)
#### ③、字符串拼接
```javascript
var i = 5;
var str = i + "";

console.log(typeof str);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655867464357-f39d8d2b-9ae2-485b-a52d-9171b4511dc8.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=116&id=U4qfh&name=image.png&originHeight=116&originWidth=291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6058&status=done&style=stroke&taskId=uccf33468-6b51-48bc-873e-d7f968b1eae&title=&width=291)
### 6、数值类型转换
#### ①、Number()
```javascript
var str1 = Number("str");
var str2 = Number("123");
var str3 = Number("123.1");
var bool = Number(true);
var nu = Number(null);
var undef = Number(undefined);

console.log(str1,str2,str3,bool,nu,undef);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655872653616-5943184d-493b-46a1-a4ae-004fd84e4466.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=122&id=uaa379b4e&name=image.png&originHeight=122&originWidth=291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6716&status=done&style=stroke&taskId=u368e151c-9f4d-484f-8b53-3ae3fc0c01e&title=&width=291)
#### ②、parseInt()
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655872790195-df0d3c05-2a80-409a-8f64-5f58c43581cd.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=268&id=u89a0f95f&name=image.png&originHeight=268&originWidth=311&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76648&status=done&style=stroke&taskId=u3116436f-41ef-40f4-be0b-655a8b8263d&title=&width=311)
#### ③、parseFloat()
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655872721882-0630161d-29c5-4cb0-962f-a0933c5559bb.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=315&id=u8e2bec48&name=image.png&originHeight=315&originWidth=359&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106301&status=done&style=stroke&taskId=ua2cc1120-1b77-47ed-a3bc-ef7ad721c61&title=&width=359)
### 7、布尔类型转换

1. 数值型：0 为 false ，其他都为 true
2. 字符串：空（""）为 false ，有内容就为 true
3. null：false
4. undefined：false
```javascript
var a = Boolean(0);
var b = Boolean(1);
var c = Boolean(2);
var d = Boolean("");
var e = Boolean(" ");
var f = Boolean("0");
var g = Boolean("1");
var h = Boolean("2");
var i = Boolean("true");
var j = Boolean("false");
var k = Boolean(null);
var l = Boolean(undefined);

console.log(a,b,c);
console.log(d,e,f,g,h);
console.log(i,j);
console.log(k,l);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655873465084-dc2ad733-23cf-4fb7-9d9e-6e3d7b5dc49e.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=185&id=u0088ac52&name=image.png&originHeight=185&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6554&status=done&style=stroke&taskId=u0dc886b9-04e8-47f6-acce-162db183428&title=&width=235)
## 四、操作符

1. 表达式：值和操作符，运算会有一个结果
2. 同时，表达式中的每个数值及部分表达式，又称为：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655873787520-ab5e285a-8548-4fd2-ac29-2ed616026a04.png#clientId=u7d2a2de4-9ea9-4&from=paste&height=187&id=ub689326d&name=image.png&originHeight=187&originWidth=481&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47458&status=done&style=stroke&taskId=ue2b34087-f241-4161-93d2-4db47b4d888&title=&width=481)
### 1、算数操作符
:::info
 +    -    *    /    %
:::

1. +：加号，加法运算（3+3）
2. - ：减号， 减法运算 (3–1) 负 (–1)
3. * ：星号，乘法运算 (3*3)
4. / ：正斜线， 除法运算 (3/3)
5. %：百分号，求余运算（10%3=1 （10/3=3·······1））
### 2、一元运算符
:::info
符合两边只有一个操作数的符号就是一元运算符；主要有两种：“++”“--”
:::

1. ++：运算符，他是一种自增运算符
```javascript
var a = 1;

a++;
// 结果：2
console.log(a);
```

2.  --  ：运算符，他是一种自减运算符
```javascript
var a = 1;

a--;
// 结果：0
console.log(a);
```

3. 运算符后置(a++)，当不出现赋值时，执行自增(自减)运算；但是出现赋值时，先赋值，后运算
```javascript
var a = 1;

var b = a++;
// 结果：2
console.log(a);
// 结果：1
console.log(b);
```

4. 运算符前置(++a)，当不出现赋值时，执行自增(自减)顺序，但出现赋值时，先运算，后赋值
```javascript
var a = 1;

var b = ++a;
// 结果：2
console.log(a);
// 结果：2
console.log(b);
```
### 3、逻辑运算符

1. &&：与，两个语句同时为 true，结果才为 true，否则为 false
2. ||     ：或，两个语句有一个为 true，结果就为 true，否则为 false
3. !      ：取反，true 变 false，false 变 true
4. 若 && 和 || 同时出现，则会先运算 && 再运算 ||  
### 4、比较（关系）运算符
:::info
 <    >    <=    >=    ==    !=    ===    !==
:::

- 因为 JS 是弱类型语言，所以变量的数据类型会自动转换
```javascript
var a = "2";
var b = 2;
// 此时 a 就被转换为了数值型
console.log(a == b);
```

1. <    ：小于
2. >    ：大于
3. <= ：小于等于
4. >= ：大于等于
5. == ：等于
6. !=   ：不等于
7. ===：全等于，类型和数值都相同才返回 true
8. !== ：不全等于，类型和数值都不相同才返回 false
### 5、赋值运算符
:::info
=    +=    -=    *=    /=    %=
:::
| 赋值运算符 | 说明 | 示例 | 等效于 |
| --- | --- | --- | --- |
| = | 赋值 | a = b | a = b |
| += | 加法运算或连接操作并赋值 | a += b | a = a + b |
| -= | 减法运算并赋值 | a -= b | a= a - b |
| *= | 乘法运算并赋值 | a *= b | a = a * b |
| /= | 除法运算并赋值 | a /= b | a = a / b |
| %= | 取模运算并赋值 | a %= b | a = a % b |

### 6、运算符的优先级
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655876742725-8e77b89c-d456-4047-802f-d159e2922e15.png#clientId=u329c99eb-bcc2-4&from=paste&height=193&id=ucece04fb&name=image.png&originHeight=193&originWidth=336&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56462&status=done&style=stroke&taskId=uc17398ab-9f5c-4881-ab07-18207000b82&title=&width=336)
## 五、流程控制
**程序的三种基本结构：**

1. 顺序结构：从上到下执行的代码就是顺序结构，程序默认是以由上到下的顺序执行的
2. 分支结构：根据不同的情况及判断，执行对应的代码，从而得到不同的结果
3. 循环结构：重复执行一段代码
### 1、分支结构
#### ①、if 判断

- **执行流程**：如果 if 里面的条件为真则执行大括号里面的语句，反之执行后面的语句，不执行大括号里面的语句
```javascript
if (条件表达式){
    执行语句;
}
```
#### ②、if else (双分支语句)

- **执行流程**：如果 if 里面的条件为真则执行大括号里面的语句，反之执行后面的语句，不执行大括号里面的语句
```javascript
if (条件表达式){
    执行语句1;
} else {
    执行语句2;
}
```
#### ③、if else if (多分支语句)

- **执行流程**：如果 if 里面的条件为真则执行大括号里面的语句，反之执行后面的语句，不执行大括号里面的语句
- 多分支语句还是多选 1 ，最后只能有一个语句执行
- else if 中间是有空格的，理论上可以有任意多个条件
```javascript
if (条件表达式1){
    语句1;
} else if (条件表达式2){
    语句2;
} else if (条件表达式3){
    语句3;
} else if (...){
    ...;       
} else{
    最后执行语句;
}
```
#### ④、switch-case 

- **执行流程**：条件表达式的值与下面语句的值进行匹配，匹配成功则执行匹配到的那个值底下相应的语句，如果都没匹配上就执行 default 内的语句
- break：如果 case 里面没有break，则不会退出 switch 是执行下面的一个 case
- 可以实现多选1的效果
```javascript
switch(条件表达式){
    case value1:
        执行语句1;
        break;
    case value2:
        执行语句2;
        break;
    ...
    
    default:
    	执行最后的语句;
}
```
#### ⑤、三元表达式

- **执行流程**：如果条件表达式结果为真则返回表达式 1 的值，如果条件表达式为假则返回表达式 2 的值
- 和 if-else语句一样的作用
```javascript
条件表达式 ? 表达式1:表达式2;
```
#### ⑥、switch 语句和 if else if 语句的区别

1. 一般情况下，它们两个的语句可以相互替换
2. switch...case 语句通常处理 case 为比较确定值得情况，而 if....else... 语句更加灵活，常用于范围判断（大于、等于某个范围）
3. switch 语句进行条件判断后直接执行到程序得条件语句，效率更高。而 if....else 语句有几种条件，就得判断多少次
4. 当分支较少时， if...else 语句的执行效率比 switch 语句要高
5. 当分支较多时，switch 语句的执行效率比较高，而且结构更清晰
### 2、循环结构
在 JS 语言中，循环语句有三种，while、do...while、for
#### ①、while

- **执行流程**：判断循环的条件，如果条件为真，则执行循环体；再判断循环条件，执行循环体；直到条件为假，则结束循环操作
```javascript
while(条件){
    // 循环体  代码块
    break;//终止当前循环 提前推出循环
    continue;//终止本次迭代，继续下一轮
}
```
#### ②、do...while

- **执行流程**：do…while 循环在做条件判断之前会先进行输出。即不管判断条件是否为真，都会先执行循环体一次
```javascript
do{
    // 循环体
}while(条件);
```
#### ③、for
```javascript
// for(循环变量的声明; 循环条件; 循环变量的改变){
for(表达式1; 表达式2; 表达式3){
    // 循环体
}

// 例子
// 定义属性 i = 0；判断条件 i < 10；i++（每进行一次判断，i自增1）
for(var i = 0; i < 10; i++){
	console.log("hello world");
}
```
:::info

1. 表达式 1 在循环开始之前执行。
2. 表达式 2 定义运行循环的条件。
3. 表达式 3 会在循环每次被执行后执行。
:::
> 在for循环中我们也会有特殊的写法：三个表达式都可以省略，前提条件是：
> 1. 省略声明表达式，在循环开始之前对循环变量定义
> 2. 省略条件判断表达式，在循环体中做跳出循环的操作
> 3. 省略循环变量的改变，在循环体中对循环变量进行改变

#### ④、嵌套循环

- 以上三种循环结构可以自由组合（嵌套循环）
1. while：没有固定的循环次数，一般的需求都是到什么为止 并且满足条件才循环
2. do…while：没有固定的循环次数，一般的需求都是到什么为止 无论是否满足循环条件都会执行一次
3. for：有固定的循环次数的场合用，使用较多
### 3、break 和 continue 

1. break ：立即跳出整个循环，即循环结束，开始执行循环后面的内容
2. continue ：立即跳出当前循环，继续下一次循环
## 六、数组
### 1、数组的基本概念
#### ①、什么是数组

1. 数组是一种特殊的变量，它能够一次存放一个以上的值
2. 数组可以用一个单一的名称存放很多值，并且还可以通过引用索引号来访问这些值
#### ②、创建数组

1. 构造函数方式
```javascript
// 创建空数组
var myCars=new Array();
// 给数组赋值
myCars[0]="Saab";      
myCars[1]="Volvo";
myCars[2]="BMW";

// 创建时赋值
var myCars=new Array("Saab","Volvo","BMW");
```

2. 字面量方式
```javascript
// 创建空数组
var myCars=[];
// 创建时赋值
var myCars=["Saab","Volvo","BMW"];
```
#### ③、多维数组
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655885327399-7b367216-ec67-4ffa-986a-139fe7732609.png#clientId=u52d9acef-070f-4&from=paste&height=258&id=ubb8141c6&name=image.png&originHeight=258&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89644&status=done&style=stroke&taskId=uc8049f58-0f89-42a0-8b73-139ffc1b9f6&title=&width=454)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655885332036-dd2a7c78-1c67-421f-a647-b245a2f41830.png#clientId=u52d9acef-070f-4&from=paste&height=309&id=u56377567&name=image.png&originHeight=309&originWidth=251&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40209&status=done&style=stroke&taskId=u89187146-e590-4dfc-890f-4ba7463d02a&title=&width=251)
### 2、获取数组元素
#### ①、获取数组长度
```javascript
var myCars=["Saab","Volvo","BMW"];
// 获取数组长度
var length = myCars.length;
console.log(length);
```
#### ②、根据下标获取数组元素

- 下标时从 0 开始的，所以第一个元素的下标是 0，第二个元素的下标是 1，
```javascript
    var myCars=["Saab","Volvo","BMW"];

    // 获取第一个元素
    console.log(myCars[0]);
    // 获取第二个元素
    console.log(myCars[1]);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655886169824-38d89536-898c-419d-b81f-558591a9f9f0.png#clientId=u52d9acef-070f-4&from=paste&height=135&id=ub7fb455f&name=image.png&originHeight=135&originWidth=290&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6392&status=done&style=stroke&taskId=ud67c4220-9ac5-4929-beab-59b540d4e99&title=&width=290)
### 3、遍历数组元素
#### ①、使用 for 循环进行遍历（常用）
```javascript
	var arr = [1,2,3,4,5,6,7,8];

    for (var i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
```
#### ②、使用 while 循环进行遍历
```javascript
    var arr = [1,2,3,4,5,6,7,8];

    var i = 0;
    while (i < arr.length) {
        console.log(arr[i]);
        i++
    }
```
## 七、函数
### 1、函数的声明
#### ①、函数声明（常用）

- 函数声明后不会立即执行，只是在初始化的时候会将函数声明提升，会在我们需要的时候调用到
```javascript
function functionName(parameters) {
	执行的代码
}
```
#### ②、函数表达式（匿名函数）（常用）

- 此函数实际上是一个 匿名函数 (函数没有名称)。函数存储在变量中，不需要函数名称，通常通过变量名来调用
```javascript
var x = function (a, b) {
	执行的代码
};
var z = x(4, 3);
```
#### ③、Function() 构造函数

- 通过内置的 JavaScript 函数构造器（Function()）定义
```javascript
var myFunction = new Function("a", "b", "return a * b");
var x = myFunction(4, 3);
```

- 如果函数调用前使用了 new 关键字, 则是调用了构造函数。这看起来就像创建了新的函数，但实际上 JavaScript 函数是重新创建的对象
- 构造函数的调用会创建一个新的对象。新对象会继承构造函数的属性和方法。构造函数中 this 关键字没有任何的值。 this 的值在函数调用实例化对象(new object)时创建
```javascript
// 构造函数:
function myFunction(arg1, arg2) {
    this.firstName = arg1;
    this.lastName  = arg2;
}
 
// This    creates a new object
var x = new myFunction("John","Doe");
x.firstName;                             // 返回 "John"
```
#### ④、自调用函数

- 函数表达式可以 "自调用"。自调用表达式会自动调用。
- 如果表达式后面紧跟 () ，则会自动调用。
- 不能自调用声明的函数。
```javascript
// 为一个匿名自调用函数
// 通过添加括号，来说明它是一个函数表达式：
(function () {
    var x = "Hello!!";
	// 我将调用自己
})();
```
#### ⑤、箭头函数

- ES6 新增了箭头函数。箭头函数表达式的语法比普通函数表达式更简洁。
:::info

1. 语法：
- 相当于：(参数1, 参数2, …, 参数N) =>{ return 表达式; }

(参数1, 参数2, …, 参数N) => { 函数声明 }
(参数1, 参数2, …, 参数N) => 表达式(单一)

2. 当只有一个参数时，圆括号是可选的：

(单一参数) => {函数声明}
单一参数 => {函数声明}

3. 没有参数的函数应该写成一对圆括号:

() => {函数声明}
:::
```javascript
// ES5
var x = function(x, y) {
     return x * y;
}
 
// ES6
const x = (x, y) => x * y;
```

1. 有的箭头函数都没有自己的 this。 不适合顶一个 对象的方法。
2. 当我们使用箭头函数的时候，箭头函数会默认帮我们绑定外层 this 的值，所以在箭头函数中 this 的值和外层的 this 是一样的。
3. 箭头函数是不能提升的，所以需要在使用之前定义。
4. 使用 const 比使用 var 更安全，因为函数表达式始终是一个常量。
5. 如果函数部分只是一个语句，则可以省略 return 关键字和大括号 {}，这样做是一个比较好的习惯:
#### ⑥、使用函数注意点
##### Ⅰ、函数提升

1. 提升（Hoisting）是 JavaScript 默认将当前作用域提升到前面去的的行为。
2. 提升（Hoisting）应用在变量的声明与函数的声明。
3. 因此，函数可以在声明之前调用：
4. 注意：使用表达式定义函数时无法提升
```javascript
myFunction(5);

function myFunction(y) {
    return y * y;
}
```
##### Ⅱ、函数式对象

1. 在 JavaScript 中使用 typeof 操作符判断函数类型将返回 "function" 。
2. 但是JavaScript 函数描述为一个对象更加准确。
3. JavaScript 函数有 属性 和 方法。
4. arguments.length 属性返回函数调用过程接收到的参数个数
```javascript
function myFunction(a, b) {    //2
    return arguments.length;
}
```

- toString() 方法将函数作为一个字符串返回：
```javascript
function myFunction(a, b) {
    return a * b;
}

var txt = myFunction.toString();     //function myFunction(a, b) { return a * b; }
```
### 2、函数的调用
#### ①、无参函数
```javascript
// 声明的函数 
function functionName() {
	执行的代码
}

// 调用函数：函数名();
functionName();
```
#### ②、有参函数
```javascript
// 声明的函数 
function functionName(parameters) {
	执行的代码
}

// 调用函数：函数名(参数);
functionName(参数);
```
### 3、形参和实参
> JavaScript函数是参数化的：函数的定义会包括一个称为形参（parameter）的标识符列表，这些参数在函数体中像局部变量一样工作。函数调用会为形参提供实参的值。函数使用它们实参的值来计算返回值，成为该函数调用表达式的值。

形参相当于函数中定义的变量，实参是在运行时的函数调用时传入的参数
```javascript
// 声明的函数时，parameters 只是一个变量，没有固定的值，即为形参
function functionName(parameters) {
	执行的代码
}

// 调用函数时，传入的参数是一个确定值，此时就为实参
functionName(参数);
```
### 4、函数的返回值

1. 正常有返回值的返回
```javascript
function f1(a,b){
	return a + b;
}
var i =  f1(1,2);
// 控制台打印：3
console.log(i);
```

2. 没有返回值的返回
```javascript
function f1(a,b){
	// return a + b;
}
var i =  f1(1,2);
// 控制台打印：undefined
console.log(i);
```

- 如果函数中没有 return ，那么函数调用之后接到的返回值就是 undefined
- 如果函数中有 return ，但 return 后面没有值，那么函数调用之后接到的返回值就是 undefined
- 函数中 return 之后，不管后面有什么代码，均不执行；return 之后函数调用结束
### 5、函数当作参数
#### ①、函数也是一种数据类型（函数）
```javascript
    function f1(){

    }
    // 控制台打印：function
    console.log(typeof f1);
```
#### ②、将函数当作值传递
```javascript
function f1(a,b){
	return a * b;
}

function f2(a,b){
	return a + b;
}

// 调用函数 f1 ，将函数 f2 的返回值作为参数传递给 f1
var sum = f1(f2(1,2),3)
// 结果：9
console.log(sum);
```
#### ③、直接传递函数
```javascript
function f1(a){
	// 已知传进来的是函数，调用此函数
	a();
}

function f2(){
	// 控制塔寺打印
	console.log(123);
}

// 调用函数 f1 ，将函数 f2 作为参数传递给 f1
// 结果：123
f1(f2);
```
#### ④、将函数作为返回值
```javascript
function f1(a,b){
	var sum =  a + b;

	// 在函数 f1 里定义 f2
	function f2(sum){
		alert(sum);
	}
	// 在函数 f1 里调用 f2 ，并返回
	return f2(sum);
}

// 调用函数 f1
var sum = f1(1,2)
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655948667641-a3fd5f26-aace-46e9-b3bb-8ae9b534286e.png#clientId=u433d991a-7cd6-4&from=paste&height=241&id=u7379d33e&name=image.png&originHeight=241&originWidth=564&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9613&status=done&style=stroke&taskId=u7ce29696-4aff-40a2-b5f4-f2bec4051e4&title=&width=564)
## 八、作用域与 JS 代码的运行
:::info
**作用域：变量可以其作用的范围和区域**
函数里面就是局部作用域，函数外面就是全局作用域
全局作用域的变量在哪里都可以使用
局部作用域只能在其定义的函数、或者其更下层的函数中才能使用
:::
### 1、全局变量和局部变量
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655948980078-d72b00f9-5498-41ee-a4f0-281fe24b5eeb.png#clientId=u433d991a-7cd6-4&from=paste&height=249&id=u79973721&name=image.png&originHeight=249&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=145147&status=done&style=stroke&taskId=u78ce6d6d-d8e2-4f74-b4d8-3123fb6e450&title=&width=850)
### 2、变量提升及代码执行阶段
**JS 代码的运行分为两个阶段：**

1. 解析（编译）阶段：此阶段进行语法检查、变量及函数的声明
2. 运行阶段：此阶段进行变量的赋值、代码流程的执行
- 变量提升
```javascript
// undefined
console.log(a);
var a = 0;
// 0
console.log(a);

// 根据 JS 代码运行阶段的说明，上面的代码可以拆解为以下四行：

// 1、解析（编译）阶段，对变量 a 进行声明
var a;
// 此时变量 a 只进行了声明，未进行赋值，故为 undefined
console.log(a);
// 2、运行阶段：对变量 a 进行赋值
a = 0;
// 因已进行了赋值，故为 0
console.log(a);

// 这就是变量提升
```
### 3、作用域链
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655950839246-b242bb42-e1f0-42ef-b72e-0af7280c1b62.png#clientId=u433d991a-7cd6-4&from=paste&height=120&id=u90ad469e&name=image.png&originHeight=122&originWidth=845&originalType=binary&ratio=1&rotation=0&showTitle=false&size=120005&status=done&style=stroke&taskId=u83b9a474-3fc2-4c88-94a0-37b773b9e7f&title=&width=834)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655950914600-c509e736-a021-4019-87b2-b782da3e3048.png#clientId=u433d991a-7cd6-4&from=paste&height=272&id=uf5a8808d&name=image.png&originHeight=272&originWidth=277&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42049&status=done&style=stroke&taskId=ub0d18d9c-e62f-4139-9189-9c091deb5b9&title=&width=277)
## 九、对象（Object）
### 1、什么是对象

- 万物皆对象

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655952283287-51160f9e-4527-4976-9c40-d14b43b4b9ed.png#clientId=u433d991a-7cd6-4&from=paste&height=126&id=u437db5be&name=image.png&originHeight=126&originWidth=592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63462&status=done&style=stroke&taskId=u5b350c2a-26f6-40e9-b0b0-edb0177fef8&title=&width=592)
### 2、JavaScript 中的对象

- **事务的特性在对象中用属性来表示**
- **事务的行为在对象中用方法来表示**

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655952314025-13a068ce-ff56-4e39-9365-e1a71aecac0d.png#clientId=u433d991a-7cd6-4&from=paste&height=200&id=uc145fa83&name=image.png&originHeight=200&originWidth=520&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97027&status=done&style=stroke&taskId=ue4a2ebc3-7182-4748-b02a-96413d9a20e&title=&width=520)
### 3、对象的声明
#### ①、字面量方式声明对象（常用）
```javascript
    // 1、字面量方式声明对象
    var obj = {};
    
    // 字面量方式声明对象并赋值
    // 对象中的数据都是成键值对存在的；通常来说，值是函数则称为方法，其他类型的值称为属性
    var obj1 = {
        id:1,
        name:"月海",
        age:16,
        // 在对象中定义的函数，称为方法（还是函数）
        work:function(){
            console.log("打卡上班");
            console.log("工作");
            console.log("打卡下班");
        }
    };
```
#### ②、实例化方式（内置构造函数）声明对象
```javascript
    // 2、实例化方式（内置构造函数）声明对象
    var obj2 = new Object();
```
#### ③、自定义构造函数方式声明对象
```javascript
    // 3、自定义构造函数方式声明对象
    // 创建函数
    function fun(){

    }
    // 使用自定义的构造函数声明对象
    var f = new fun();
```
### 4、对象的使用
:::info
获取对象的属性：对象名.属性名
获取对象的方法：对象名.方法名()
:::
```javascript
    var obj = {
        id:1,
        name:"月海",
        age:16,
        work:function(){
            console.log("打卡上班");
            console.log("工作");
            console.log("打卡下班");
        }
    };

    // 获取对象的属性或方法：对象名.属性名
    // 月海
    console.log(obj.name);
    // 打卡上班
    // 工作
    // 打卡下班
    obj.work();
```
### 5、this
:::info
**this 永远指向一个对象**
**this 的指向完全取决于函数调用的位置**

1. 在方法的调用中，因为运行环境在对象内，因此函数中的 this 指向这个对象
2. 而在全局作用域下 ，函数中的 this 就会指向全局作用域对象 window
:::

- 在方法中的 this 指的就是这个方法所在的对象
```javascript
    var obj = {
        id:1,
        name:"月海",
        age:16,
        work:function(){
            // 在方法中的 this 指的就是这个方法所在的对象
            console.log(this.name);
            console.log(this.name + "打卡上班");
            console.log("工作");
            console.log("打卡下班");
        }
    };

    // 月海
    // 月海打卡上班
    // 工作
    // 打卡下班
    obj.work();
```
### 6、对象的遍历及删除
#### ①、对象的遍历
:::info
for...in：for...in不仅可以遍历对象，还可以遍历数组
:::
```javascript
    var obj = {
        id:1,
        name:"月海",
        age:16,
        work:function(){
            console.log("打卡上班");
            console.log("工作");
            console.log("打卡下班");
        }
    };

    for(var k in obj){
        console.log(obj[k]);
    }
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655959943581-42110e0c-ecba-456b-80c7-c534de3c39b3.png#clientId=u433d991a-7cd6-4&from=paste&height=242&id=ue5acd2e4&name=image.png&originHeight=242&originWidth=337&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9975&status=done&style=stroke&taskId=u2c55351c-5086-41ef-b2ad-7743519c072&title=&width=337)
#### ②、对象的删除

- 使用 delete 关键字可以删除对象中的属性
```javascript
    var obj = {
        id:1,
        name:"月海",
        age:16,
        work:function(){
            console.log("打卡上班");
            console.log("工作");
            console.log("打卡下班");
        }
    };

    // for(var k in obj){
    //     console.log(obj[k]);
    // }

    console.log(obj);

    // 使用 delete 删除对象中的属性
    delete obj.id;

    console.log(obj);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655960093475-8210c7e8-0b81-4698-bb71-05f4b8d31353.png#clientId=u433d991a-7cd6-4&from=paste&height=151&id=u3a61a39a&name=image.png&originHeight=151&originWidth=335&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10253&status=done&style=stroke&taskId=ud5089f18-a473-4791-b398-2aa68ad9168&title=&width=335)
### 7、包装对象
> 在JavaScript中有七种数据类型
> 1. String（字符串）
> 2. Number（数值）
> 3. Boolean（布尔）
> 4. Null（空）
> 5. Undefined（未定义）
> 6. Symbol（标记）：es2015中添加的第七种数据类型,本篇不讨论。
> 7. Object（对象）
> 
这七种数据类型中，对象为“引用类型”，其他六种为“原始类型”（或叫“值类型”，或叫“基本类型”）。

:::info
原始类型的数据在一定条件下可以转化为对象，这就是包装对象
原始值可以自动当作对象来调用，可以调用各种属性及方法
如果包装对象使用完成，会立即自动销毁
:::
#### ①、原始类型有没有属性和方法

- 按原始类型与引用类型的定义来说，只有引用类型（对象）才有属性和方法，原始类型是没有自己的属性和方法的，但是我们也能经常看到有下面这样的写法。
```javascript
var num = 100;
var str = num.toString(); 
console.log(typeof str); //string
```

1. 我们使用toString方法将num这个数值型转换成了字符串型，这里面我们用原始类型num调用了toString方法，那是不是原始类型也能调用方法呢
2. 答案是否定的。仍然只有对象才能拥有自己的属性和方法。
3. 那为什么num就真的调用了toString却没有报错呢，这就需要我们接着讨论包装对象的概念了
#### ②、包装对象

1. 在JavaScript中有三种包装对象，他们对应的构造函数分别是String，Number，Boolean，这三个包装对象对应着三个原始类型：字符串、数值和布尔
2. 当我们使用原始类型调用toString方法的时候，原始类型会先通过其包装对象对应的构造函数转换成对象，然后用这个对象调用方法，调用方法之后，原始类型仍是原始类型，新创建的包装对象会被销毁
3. 如下面的代码所示，有包装对象的原始类型可以成功执行toString方法，没有包装对象的原始类型会报错
```javascript
//定义五个原始类型
var str = "hello"; //包装对象String
var num = 100; //包装对象Number
var bool = true; //包装对象Boolean
var und = undefined; //无包装对象
var nu = null; //无包装对象

//输出五个值，建议分别输出，查看那一条报错。
console.log(str.toString());
console.log(num.toString());
console.log(bool.toString());
console.log(und.toString()); //报错
console.log(nu.toString()); //报错
```

---

1. 再来看一个例子，通过包装对象，我们也能得到原始类型的某些属性，例如length属性
2. 通过length属性，可以获取到字符串的长度，这也是受益于包装对象
3. 但是undefined就不能输出length了（当然，我们也没这个必要输出undefined的长度，这里只是做一个示范）
```javascript
var str = "hello";
var un = undefined;
console.log(str.length); //5
console.log(un.length); //报错
```

---

1. 为str添加了name属性，这行代码成功执行，但是最后一行输出的却是undefined，这是为什么呢？
2. 上面已经说了，如果需要原始类型具有属性和方法，那包装对象就要登场，运行完之后，包装对象创建的对象就会被销毁
3. 在下面的例子中，第二行给name属性赋值的时候，包装对象会登场，创建一个str对应的对象，当然，这行执行完了这个对象就会被销毁。然后在第三行又会创建一个新的包装对象，这个对象当然是没有name属性的了，所以输出的是undefined
```javascript
var str = "hello";
str.name = "test";
console.log(str.name); //输出undefined
```
#### ③、总结
:::info
原始类型是没有属性和方法的，他们就是单纯的值，如果希望获取他们的属性或调用方法，那就需要包装对象来帮忙，但是帮完了，生成的对象马上就会被销毁
:::
### 8、数学（Math）对象
:::info
Math 对象用于执行数学任务。
Math 对象并不像 Date 和 String 那样是对象的类，因此没有构造函数 Math()
:::

- 语法
```javascript
var x = Math.PI; // 返回PI
var y = Math.sqrt(16); // 返回16的平方根
```
#### ①、Math 对象属性
| 属性 | 描述 |
| --- | --- |
| [E](https://www.runoob.com/jsref/jsref-e.html) | 返回算术常量 e，即自然对数的底数（约等于2.718）。 |
| [LN2](https://www.runoob.com/jsref/jsref-ln2.html) | 返回 2 的自然对数（约等于0.693）。 |
| [LN10](https://www.runoob.com/jsref/jsref-ln10.html) | 返回 10 的自然对数（约等于2.302）。 |
| [LOG2E](https://www.runoob.com/jsref/jsref-log2e.html) | 返回以 2 为底的 e 的对数（约等于 1.4426950408889634）。 |
| [LOG10E](https://www.runoob.com/jsref/jsref-log10e.html) | 返回以 10 为底的 e 的对数（约等于0.434）。 |
| [PI](https://www.runoob.com/jsref/jsref-pi.html) | 返回圆周率（约等于3.14159）。 |
| [SQRT1_2](https://www.runoob.com/jsref/jsref-sqrt1-2.html) | 返回 2 的平方根的倒数（约等于 0.707）。 |
| [SQRT2](https://www.runoob.com/jsref/jsref-sqrt2.html) | 返回 2 的平方根（约等于 1.414）。 |

#### ②、Math 对象方法
| 方法 | 描述 |
| --- | --- |
| [random()](https://www.runoob.com/jsref/jsref-random.html) | 返回 0 ~ 1 之间的随机数。 |
| [pow(x,y)](https://www.runoob.com/jsref/jsref-pow.html) | 返回 x 的 y 次幂（即 x 的 y 次方）。 |
| [sqrt(x)](https://www.runoob.com/jsref/jsref-sqrt.html) | 返回数的平方根。 |
| [max(x,y,z,...,n)](https://www.runoob.com/jsref/jsref-max.html) | 返回 x,y,z,...,n 中的最高值。 |
| [min(x,y,z,...,n)](https://www.runoob.com/jsref/jsref-min.html) | 返回 x,y,z,...,n中的最低值。 |
| [abs(x)](https://www.runoob.com/jsref/jsref-abs.html) | 返回 x 的绝对值。 |
| [round(x)](https://www.runoob.com/jsref/jsref-round.html) | 四舍五入。 |
| [ceil(x)](https://www.runoob.com/jsref/jsref-ceil.html) | 对 x 进行上舍入。 |
| [floor(x)](https://www.runoob.com/jsref/jsref-floor.html) | 对 x 进行下舍入。 |
| [sin(x)](https://www.runoob.com/jsref/jsref-sin.html) | 返回数的正弦。 |
| [cos(x)](https://www.runoob.com/jsref/jsref-cos.html) | 返回数的余弦。 |
| [tan(x)](https://www.runoob.com/jsref/jsref-tan.html) | 返回角的正切。 |
| [acos(x)](https://www.runoob.com/jsref/jsref-acos.html) | 返回 x 的反余弦值。 |
| [asin(x)](https://www.runoob.com/jsref/jsref-asin.html) | 返回 x 的反正弦值。 |
| [atan(x)](https://www.runoob.com/jsref/jsref-atan.html) | 以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。 |
| [atan2(y,x)](https://www.runoob.com/jsref/jsref-atan2.html) | 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。 |
| [exp(x)](https://www.runoob.com/jsref/jsref-exp.html) | 返回 Ex 的指数。 |
| [log(x)](https://www.runoob.com/jsref/jsref-log.html) | 返回数的自然对数（底为e）。 |

#### ③、取一个区间的数

- 比如：取 5-13 之间的任意一个数（包括 5-13）
```javascript
// 先取随机数，然后用随机数 * （最大的数 - 最小的数） + 最小的数
// 最后再将得到的数下舍入
var ran = Math.random() * (13-5) + 5;
console.log(Math.floor(ran));
```
### 9、日期（Date）对象
:::info
Date 对象用于处理日期与时间
JS 中获取的时间是计算机的本地时间，且月份是从 0 开始的
创建 Date 对象： new Date()
以下四种方法同样可以创建 Date 对象
:::
```javascript
var d = new Date();
// milliseconds：参数为毫秒；参数是一个 Unix 时间戳（Unix Time Stamp），它是一个整数值，表示自 1970 年 1 月 1 日 00:00:00 UTC（the Unix epoch）以来的毫秒数
var d = new Date(milliseconds);
// dateString：参数表示日期的字符串值
var d = new Date(dateString);
// year, month, day, hours, minutes, seconds, milliseconds：分别表示年、月、日、时、分、秒、毫秒
var d = new Date(year, month, day, hours, minutes, seconds, milliseconds);
```
#### ①、Date 对象属性
| 属性 | 描述 |
| --- | --- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-date.html) | 返回对创建此对象的 Date 函数的引用。 |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-date.html) | 使您有能力向对象添加属性和方法。 |

#### ②、Date 对象方法
| 方法 | 描述 |
| --- | --- |
| [getDate()](https://www.runoob.com/jsref/jsref-getdate.html) | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。 |
| [getDay()](https://www.runoob.com/jsref/jsref-getday.html) | 从 Date 对象返回一周中的某一天 (0 ~ 6)。 |
| [getFullYear()](https://www.runoob.com/jsref/jsref-getfullyear.html) | 从 Date 对象以四位数字返回年份。 |
| [getHours()](https://www.runoob.com/jsref/jsref-gethours.html) | 返回 Date 对象的小时 (0 ~ 23)。 |
| [getMilliseconds()](https://www.runoob.com/jsref/jsref-getmilliseconds.html) | 返回 Date 对象的毫秒(0 ~ 999)。 |
| [getMinutes()](https://www.runoob.com/jsref/jsref-getminutes.html) | 返回 Date 对象的分钟 (0 ~ 59)。 |
| [getMonth()](https://www.runoob.com/jsref/jsref-getmonth.html) | 从 Date 对象返回月份 (0 ~ 11)。 |
| [getSeconds()](https://www.runoob.com/jsref/jsref-getseconds.html) | 返回 Date 对象的秒数 (0 ~ 59)。 |
| [getTime()](https://www.runoob.com/jsref/jsref-gettime.html) | 返回 1970 年 1 月 1 日至今的毫秒数。 |
| [getTimezoneOffset()](https://www.runoob.com/jsref/jsref-gettimezoneoffset.html) | 返回本地时间与格林威治标准时间 (GMT) 的分钟差。 |
| [getUTCDate()](https://www.runoob.com/jsref/jsref-getutcdate.html) | 根据世界时从 Date 对象返回月中的一天 (1 ~ 31)。 |
| [getUTCDay()](https://www.runoob.com/jsref/jsref-getutcday.html) | 根据世界时从 Date 对象返回周中的一天 (0 ~ 6)。 |
| [getUTCFullYear()](https://www.runoob.com/jsref/jsref-getutcfullyear.html) | 根据世界时从 Date 对象返回四位数的年份。 |
| [getUTCHours()](https://www.runoob.com/jsref/jsref-getutchours.html) | 根据世界时返回 Date 对象的小时 (0 ~ 23)。 |
| [getUTCMilliseconds()](https://www.runoob.com/jsref/jsref-getutcmilliseconds.html) | 根据世界时返回 Date 对象的毫秒(0 ~ 999)。 |
| [getUTCMinutes()](https://www.runoob.com/jsref/jsref-getutcminutes.html) | 根据世界时返回 Date 对象的分钟 (0 ~ 59)。 |
| [getUTCMonth()](https://www.runoob.com/jsref/jsref-getutcmonth.html) | 根据世界时从 Date 对象返回月份 (0 ~ 11)。 |
| [getUTCSeconds()](https://www.runoob.com/jsref/jsref-getutcseconds.html) | 根据世界时返回 Date 对象的秒钟 (0 ~ 59)。 |
| getYear() | 已废弃。 请使用 getFullYear() 方法代替。 |
| [parse()](https://www.runoob.com/jsref/jsref-parse.html) | 返回1970年1月1日午夜到指定日期（字符串）的毫秒数。 |
| [setDate()](https://www.runoob.com/jsref/jsref-setdate.html) | 设置 Date 对象中月的某一天 (1 ~ 31)。 |
| [setFullYear()](https://www.runoob.com/jsref/jsref-setfullyear.html) | 设置 Date 对象中的年份（四位数字）。 |
| [setHours()](https://www.runoob.com/jsref/jsref-sethours.html) | 设置 Date 对象中的小时 (0 ~ 23)。 |
| [setMilliseconds()](https://www.runoob.com/jsref/jsref-setmilliseconds.html) | 设置 Date 对象中的毫秒 (0 ~ 999)。 |
| [setMinutes()](https://www.runoob.com/jsref/jsref-setminutes.html) | 设置 Date 对象中的分钟 (0 ~ 59)。 |
| [setMonth()](https://www.runoob.com/jsref/jsref-setmonth.html) | 设置 Date 对象中月份 (0 ~ 11)。 |
| [setSeconds()](https://www.runoob.com/jsref/jsref-setseconds.html) | 设置 Date 对象中的秒钟 (0 ~ 59)。 |
| [setTime()](https://www.runoob.com/jsref/jsref-settime.html) | setTime() 方法以毫秒设置 Date 对象。 |
| [setUTCDate()](https://www.runoob.com/jsref/jsref-setutcdate.html) | 根据世界时设置 Date 对象中月份的一天 (1 ~ 31)。 |
| [setUTCFullYear()](https://www.runoob.com/jsref/jsref-setutcfullyear.html) | 根据世界时设置 Date 对象中的年份（四位数字）。 |
| [setUTCHours()](https://www.runoob.com/jsref/jsref-setutchours.html) | 根据世界时设置 Date 对象中的小时 (0 ~ 23)。 |
| [setUTCMilliseconds()](https://www.runoob.com/jsref/jsref-setutcmilliseconds.html) | 根据世界时设置 Date 对象中的毫秒 (0 ~ 999)。 |
| [setUTCMinutes()](https://www.runoob.com/jsref/jsref-setutcminutes.html) | 根据世界时设置 Date 对象中的分钟 (0 ~ 59)。 |
| [setUTCMonth()](https://www.runoob.com/jsref/jsref-setutcmonth.html) | 根据世界时设置 Date 对象中的月份 (0 ~ 11)。 |
| [setUTCSeconds()](https://www.runoob.com/jsref/jsref-setutcseconds.html) | setUTCSeconds() 方法用于根据世界时 (UTC) 设置指定时间的秒字段。 |
| setYear() | 已废弃。请使用 setFullYear() 方法代替。 |
| [toDateString()](https://www.runoob.com/jsref/jsref-todatestring.html) | 把 Date 对象的日期部分转换为字符串。 |
| toGMTString() | 已废弃。请使用 toUTCString() 方法代替。 |
| [toISOString()](https://www.runoob.com/jsref/jsref-toisostring.html) | 使用 ISO 标准返回字符串的日期格式。 |
| [toJSON()](https://www.runoob.com/jsref/jsref-tojson.html) | 以 JSON 数据格式返回日期字符串。 |
| [toLocaleDateString()](https://www.runoob.com/jsref/jsref-tolocaledatestring.html) | 根据本地时间格式，把 Date 对象的日期部分转换为字符串。 |
| [toLocaleTimeString()](https://www.runoob.com/jsref/jsref-tolocaletimestring.html) | 根据本地时间格式，把 Date 对象的时间部分转换为字符串。 |
| [toLocaleString()](https://www.runoob.com/jsref/jsref-tolocalestring.html) | 根据本地时间格式，把 Date 对象转换为字符串。 |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-date.html) | 把 Date 对象转换为字符串。 |
| [toTimeString()](https://www.runoob.com/jsref/jsref-totimestring.html) | 把 Date 对象的时间部分转换为字符串。 |
| [toUTCString()](https://www.runoob.com/jsref/jsref-toutcstring.html) | ```javascript
var today = new Date(); 
var UTCstring = today.toUTCString();
```
 |
| [UTC()](https://www.runoob.com/jsref/jsref-utc.html) | 根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。 |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-date.html) | 返回 Date 对象的原始值。 |

### 10、数组（Array）对象
:::info
Array 对象用于在变量中存储多个值
第一个数组元素的索引值为 0，第二个索引值为 1，以此类推
:::
```javascript
var cars = ["Saab", "Volvo", "BMW"];
```
#### ①、数组属性
| 属性 | 描述 |
| --- | --- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-array.html) | 返回创建数组对象的原型函数。 |
| [length](https://www.runoob.com/jsref/jsref-length-array.html) | 设置或返回数组元素的个数。 |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-array.html) | 允许你向数组对象添加属性或方法。 |

#### ②、Array 对象方法
| 方法 | 描述 |
| --- | --- |
| [concat()](https://www.runoob.com/jsref/jsref-concat-array.html) | 连接两个或更多的数组，并返回结果。 |
| [copyWithin()](https://www.runoob.com/jsref/jsref-copywithin.html) | 从数组的指定位置拷贝元素到数组的另一个指定位置中。 |
| [entries()](https://www.runoob.com/jsref/jsref-entries.html) | 返回数组的可迭代对象。 |
| [every()](https://www.runoob.com/jsref/jsref-every.html) | 检测数值元素的每个元素是否都符合条件。 |
| [fill()](https://www.runoob.com/jsref/jsref-fill.html) | 使用一个固定值来填充数组。 |
| [filter()](https://www.runoob.com/jsref/jsref-filter.html) | 检测数值元素，并返回符合条件所有元素的数组。 |
| [find()](https://www.runoob.com/jsref/jsref-find.html) | 返回符合传入测试（函数）条件的数组元素。 |
| [findIndex()](https://www.runoob.com/jsref/jsref-findindex.html) | 返回符合传入测试（函数）条件的数组元素索引。 |
| [forEach()](https://www.runoob.com/jsref/jsref-foreach.html) | 数组每个元素都执行一次回调函数。 |
| [from()](https://www.runoob.com/jsref/jsref-from.html) | 通过给定的对象中创建一个数组。 |
| [includes()](https://www.runoob.com/jsref/jsref-includes.html) | 判断一个数组是否包含一个指定的值。 |
| [indexOf()](https://www.runoob.com/jsref/jsref-indexof-array.html) | 搜索数组中的元素，并返回它所在的位置。 |
| [isArray()](https://www.runoob.com/jsref/jsref-isarray.html) | 判断对象是否为数组。 |
| [join()](https://www.runoob.com/jsref/jsref-join.html) | 把数组的所有元素放入一个字符串。 |
| [keys()](https://www.runoob.com/jsref/jsref-keys.html) | 返回数组的可迭代对象，包含原始数组的键(key)。 |
| [lastIndexOf()](https://www.runoob.com/jsref/jsref-lastindexof-array.html) | 搜索数组中的元素，并返回它最后出现的位置。 |
| [map()](https://www.runoob.com/jsref/jsref-map.html) | 通过指定函数处理数组的每个元素，并返回处理后的数组。 |
| [pop()](https://www.runoob.com/jsref/jsref-pop.html) | 删除数组的最后一个元素并返回删除的元素。 |
| [push()](https://www.runoob.com/jsref/jsref-push.html) | 向数组的末尾添加一个或更多元素，并返回新的长度。 |
| [reduce()](https://www.runoob.com/jsref/jsref-reduce.html) | 将数组元素计算为一个值（从左到右）。 |
| [reduceRight()](https://www.runoob.com/jsref/jsref-reduceright.html) | 将数组元素计算为一个值（从右到左）。 |
| [reverse()](https://www.runoob.com/jsref/jsref-reverse.html) | 反转数组的元素顺序。 |
| [shift()](https://www.runoob.com/jsref/jsref-shift.html) | 删除并返回数组的第一个元素。 |
| [slice()](https://www.runoob.com/jsref/jsref-slice-array.html) | 选取数组的一部分，并返回一个新数组。 |
| [some()](https://www.runoob.com/jsref/jsref-some.html) | 检测数组元素中是否有元素符合指定条件。 |
| [sort()](https://www.runoob.com/jsref/jsref-sort.html) | 对数组的元素进行排序。 |
| [splice()](https://www.runoob.com/jsref/jsref-splice.html) | 从数组中添加或删除元素。 |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-array.html) | 把数组转换为字符串，并返回结果。 |
| [unshift()](https://www.runoob.com/jsref/jsref-unshift.html) | 向数组的开头添加一个或更多元素，并返回新的长度。 |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-array.html) | 返回数组对象的原始值。 |

### 11、字符串（String）对像
:::info
String 对象用于处理文本（字符串）
String 对象创建方法： new String()
:::
```javascript
var txt = new String("string");
或者更简单方式：

var txt = "string";
```
#### ①、String 对象属性
| 属性 | 描述 |
| --- | --- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-string.html) | 对创建该对象的函数的引用 |
| [length](https://www.runoob.com/jsref/jsref-length-string.html) | 字符串的长度 |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-string.html) | 允许您向对象添加属性和方法 |

#### ②、String 对象方法
| 方法 | 描述 |
| --- | --- |
| [charAt()](https://www.runoob.com/jsref/jsref-charat.html) | 返回在指定位置的字符。 |
| [charCodeAt()](https://www.runoob.com/jsref/jsref-charcodeat.html) | 返回在指定的位置的字符的 Unicode 编码。 |
| [concat()](https://www.runoob.com/jsref/jsref-concat-string.html) | 连接两个或更多字符串，并返回新的字符串。 |
| [endsWith()](https://www.runoob.com/jsref/jsref-endswith.html) | 判断当前字符串是否是以指定的子字符串结尾的（区分大小写）。 |
| [fromCharCode()](https://www.runoob.com/jsref/jsref-fromcharcode.html) | 将 Unicode 编码转为字符。 |
| [indexOf()](https://www.runoob.com/jsref/jsref-indexof.html) | 返回某个指定的字符串值在字符串中首次出现的位置。 |
| [includes()](https://www.runoob.com/jsref/jsref-string-includes.html) | 查找字符串中是否包含指定的子字符串。 |
| [lastIndexOf()](https://www.runoob.com/jsref/jsref-lastindexof.html) | 从后向前搜索字符串，并从起始位置（0）开始计算返回字符串最后出现的位置。 |
| [match()](https://www.runoob.com/jsref/jsref-match.html) | 查找找到一个或多个正则表达式的匹配。 |
| [repeat()](https://www.runoob.com/jsref/jsref-repeat.html) | 复制字符串指定次数，并将它们连接在一起返回。 |
| [replace()](https://www.runoob.com/jsref/jsref-replace.html) | 在字符串中查找匹配的子串，并替换与正则表达式匹配的子串。 |
| [replaceAll()](https://www.runoob.com/jsref/jsref-replaceall.html) | 在字符串中查找匹配的子串，并替换与正则表达式匹配的所有子串。 |
| [search()](https://www.runoob.com/jsref/jsref-search.html) | 查找与正则表达式相匹配的值。 |
| [slice()](https://www.runoob.com/jsref/jsref-slice-string.html) | 提取字符串的片断，并在新的字符串中返回被提取的部分。 |
| [split()](https://www.runoob.com/jsref/jsref-split.html) | 把字符串分割为字符串数组。 |
| [startsWith()](https://www.runoob.com/jsref/jsref-startswith.html) | 查看字符串是否以指定的子字符串开头。 |
| [substr()](https://www.runoob.com/jsref/jsref-substr.html) | 从起始索引号提取字符串中指定数目的字符。 |
| [substring()](https://www.runoob.com/jsref/jsref-substring.html) | 提取字符串中两个指定的索引号之间的字符。 |
| [toLowerCase()](https://www.runoob.com/jsref/jsref-tolowercase.html) | 把字符串转换为小写。 |
| [toUpperCase()](https://www.runoob.com/jsref/jsref-touppercase.html) | 把字符串转换为大写。 |
| [trim()](https://www.runoob.com/jsref/jsref-trim.html) | 去除字符串两边的空白。 |
| [toLocaleLowerCase()](https://www.runoob.com/jsref/jsref-tolocalelowercase.html) | 根据本地主机的语言环境把字符串转换为小写。 |
| [toLocaleUpperCase()](https://www.runoob.com/jsref/jsref-tolocaleuppercase.html) | 根据本地主机的语言环境把字符串转换为大写。 |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-string.html) | 返回某个字符串对象的原始值。 |
| [toString()](https://www.runoob.com/jsref/jsref-tostring.html) | 返回一个字符串。 |

#### ③、String HTML 包装方法

- HTML 返回包含在相对应的 HTML 标签中的内容。
- 以下方法并非标准方法，所以可能在某些浏览器下不支持
| 方法 | 描述 |
| --- | --- |
| [anchor()](https://www.runoob.com/jsref/jsref-anchor.html) | 创建 HTML 锚。 |
| [big()](https://www.runoob.com/jsref/jsref-big.html) | 用大号字体显示字符串。 |
| [blink()](https://www.runoob.com/jsref/jsref-blink.html) | 显示闪动字符串。 |
| [bold()](https://www.runoob.com/jsref/jsref-bold.html) | 使用粗体显示字符串。 |
| [fixed()](https://www.runoob.com/jsref/jsref-fixed.html) | 以打字机文本显示字符串。 |
| [fontcolor()](https://www.runoob.com/jsref/jsref-fontcolor.html) | 使用指定的颜色来显示字符串。 |
| [fontsize()](https://www.runoob.com/jsref/jsref-fontsize.html) | 使用指定的尺寸来显示字符串。 |
| [italics()](https://www.runoob.com/jsref/jsref-italics.html) | 使用斜体显示字符串。 |
| [link()](https://www.runoob.com/jsref/jsref-link.html) | 将字符串显示为链接。 |
| [small()](https://www.runoob.com/jsref/jsref-small.html) | 使用小字号来显示字符串。 |
| [strike()](https://www.runoob.com/jsref/jsref-strike.html) | 用于显示加删除线的字符串。 |
| [sub()](https://www.runoob.com/jsref/jsref-sub.html) | 把字符串显示为下标。 |
| [sup()](https://www.runoob.com/jsref/jsref-sup.html) | 把字符串显示为上标。 |

### 12、数值（Number）对象
:::info
Number 对象是原始数值的包装对象。
Number 创建方式 new Number()
**注意**：如果一个参数值不能转换为一个数字将返回 NaN (非数字值)
:::
```javascript
var num = new Number(value);
```
#### ①、Number 对象属性
| 属性 | 描述 |
| --- | --- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-number.html) | 返回对创建此对象的 Number 函数的引用。 |
| [MAX_VALUE](https://www.runoob.com/jsref/jsref-max-value.html) | 可表示的最大的数。 |
| [MIN_VALUE](https://www.runoob.com/jsref/jsref-min-value.html) | 可表示的最小的数。 |
| [NEGATIVE_INFINITY](https://www.runoob.com/jsref/jsref-negative-infinity.html) | 负无穷大，溢出时返回该值。 |
| [NaN](https://www.runoob.com/jsref/jsref-number-nan.html) | 非数字值。 |
| [POSITIVE_INFINITY](https://www.runoob.com/jsref/jsref-positive-infinity.html) | 正无穷大，溢出时返回该值。 |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-num.html) | 允许您可以向对象添加属性和方法。 |

#### ②、Number 对象方法
| 方法 | 描述 |
| --- | --- |
| [isFinite](https://www.runoob.com/jsref/jsref-isfinite-number.html) | 检测指定参数是否为无穷大。 |
| [isInteger](https://www.runoob.com/jsref/jsref-isinteger-number.html) | 检测指定参数是否为整数。 |
| [isNaN](https://www.runoob.com/jsref/jsref-isnan-number.html) | 检测指定参数是否为 NaN。 |
| [isSafeInteger](https://www.runoob.com/jsref/jsref-issafeInteger-number.html) | 检测指定参数是否为安全整数。 |
| [toExponential(x)](https://www.runoob.com/jsref/jsref-toexponential.html) | 把对象的值转换为指数计数法。 |
| [toFixed(x)](https://www.runoob.com/jsref/jsref-tofixed.html) | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| [toLocaleString(locales, options)](https://www.runoob.com/jsref/jsref-tolocalestring-number.html) | 返回数字在特定语言环境下的表示字符串。 |
| [toPrecision(x)](https://www.runoob.com/jsref/jsref-toprecision.html) | 把数字格式化为指定的长度。 |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-number.html) | 把数字转换为字符串，使用指定的基数。 |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-number.html) | 返回一个 Number 对象的基本数字值。 |

#### ③、ES6 新增 Number 属性
ES 6 增加了以下三个 Number 对象的属性：

| 属性 | 描述 |
| --- | --- |
| EPSILON | 表示 1 和比最接近 1 且大于 1 的最小 Number 之间的差别 |
| MIN_SAFE_INTEGER | 表示在 JavaScript中最小的安全的 integer 型数字 (-(253 - 1)) |
| MAX_SAFE_INTEGER | 表示在 JavaScript 中最大的安全整数（253 - 1） |

#### ④、ES6 新增 Number 方法
ES 6 增加了以下两个 Number 对象的方法：

| 方法 | 描述 |
| --- | --- |
| Number.isInteger() | 用来判断给定的参数是否为整数 |
| Number.isSafeInteger() | 判断传入的参数值是否是一个"安全整数" |

### 13、布尔（Boolean）对象
:::info
Boolean 对象用于转换一个不是 Boolean 类型的值转换为 Boolean 类型值 (true 或者false)
:::
#### ①、Boolean 对象属性
| 属性 | 描述 |
| --- | --- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-boolean.html) | 返回对创建此对象的 Boolean 函数的引用 |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-boolean.html) | 使您有能力向对象添加属性和方法。 |

#### ②、Boolean 对象方法
| 方法 | 描述 |
| --- | --- |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-boolean.html) | 把布尔值转换为字符串，并返回结果。 |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-boolean.html) | 返回 Boolean 对象的原始值。 |

### 14、JavaScript 全局属性
:::info
JavaScript 全局属性和方法可用于创建Javascript对象
:::
#### ①、JavaScript 全局属性
| 属性 | 描述 |
| --- | --- |
| [Infinity](https://www.runoob.com/jsref/jsref-infinity.html) | 代表正的无穷大的数值。 |
| [NaN](https://www.runoob.com/jsref/jsref-nan.html) | 指示某个值是不是数字值。 |
| [undefined](https://www.runoob.com/jsref/jsref-undefined.html) | 指示未定义的值。 |

#### ②、JavaScript 全局函数
| 函数 | 描述 |
| --- | --- |
| [decodeURI()](https://www.runoob.com/jsref/jsref-decodeuri.html) | 解码某个编码的 URI。 |
| [decodeURIComponent()](https://www.runoob.com/jsref/jsref-decodeuricomponent.html) | 解码一个编码的 URI 组件。 |
| [encodeURI()](https://www.runoob.com/jsref/jsref-encodeuri.html) | 把字符串编码为 URI。 |
| [encodeURIComponent()](https://www.runoob.com/jsref/jsref-encodeuricomponent.html) | 把字符串编码为 URI 组件。 |
| [escape()](https://www.runoob.com/jsref/jsref-escape.html) | 对字符串进行编码。 |
| [eval()](https://www.runoob.com/jsref/jsref-eval.html) | 计算 JavaScript 字符串，并把它作为脚本代码来执行。 |
| [isFinite()](https://www.runoob.com/jsref/jsref-isfinite.html) | 检查某个值是否为有穷大的数。 |
| [isNaN()](https://www.runoob.com/jsref/jsref-isnan.html) | 检查某个值是否是数字。 |
| [Number()](https://www.runoob.com/jsref/jsref-number.html) | 把对象的值转换为数字。 |
| [parseFloat()](https://www.runoob.com/jsref/jsref-parsefloat.html) | 解析一个字符串并返回一个浮点数。 |
| [parseInt()](https://www.runoob.com/jsref/jsref-parseint.html) | 解析一个字符串并返回一个整数。 |
| [String()](https://www.runoob.com/jsref/jsref-string.html) | 把对象的值转换为字符串。 |
| [unescape()](https://www.runoob.com/jsref/jsref-unescape.html) | 对由 escape() 编码的字符串进行解码。 |

# 十、其他
## 1、事件对象 `event`
> [https://blog.csdn.net/fuhanghang/article/details/124406113](https://blog.csdn.net/fuhanghang/article/details/124406113)

1. Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。
2. 什么时候会产生Event 对象呢？例如：当用户单击某个元素的时候，我们给这个元素注册的事件就会触发，该事件的本质就是一个函数，而该函数的形参接收一个event对象。
3. 事件通常与函数结合使用，函数不会在事件发生前被执行
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h2>event 对象</h2>
    <button id="btn">点击</button>

</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        console.log(event);

        console.log(event.target);
        console.log(event.target.innerHTML);

    })

</script>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1669773623900-160c0d3e-b9b6-4ac5-b786-f58fcf4f35d5.png#clientId=ub00c6c9a-0ed9-4&from=paste&height=226&id=u91bf4fd0&name=image.png&originHeight=226&originWidth=796&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24625&status=done&style=stroke&taskId=u4fc6eaed-205e-4f07-b122-076f645aa33&title=&width=796)
## 2、过滤方法 `filter`

1. 创建一个新数组，新数组中的元素是通过检查指定数组中符合条件的所有元素
2. 返回值为 true ，则通过检查，添加到新数组
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 引入 vue -->
    <script src="../js/vue.js"></script>
</head>
<body>

    <!-- 准备一个 vue 容器 -->
    <div id="root">

        <input type="text" placeholder="请输入姓名：" v-model="keyWord">
        <!-- for-of 循环；key：每次循环的唯一标识符 -->
        <ul v-for="(per, index) of personsFilter" :key="per.id">
            <li>{{per.id}}-{{per.name}}-{{per.age}}</li>
        </ul>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            keyWord: '',
            persons: [
                {id: 01, name: '月海', age: 16},
                {id: 02, name: '言', age: 14},
                {id: 03, name: '羽', age: 16},
            ],
            personsFilter: []
        },
        watch: {
            keyWord: {
                // 开启立即执行（网页被加载后），即网页加载后就为数组 personsFilter 赋值
                immediate: true,
                handler(newVal, oldVal){
                    // filter：创建一个新数组，新数组中的元素是通过检查指定数组中符合条件的所有元素
                    // 将过滤后创建的新数组，赋值给数组 
                    this.personsFilter = this.persons.filter((p) =>{
                        // 返回值为 true ，则通过检查，添加到新数组
                        return p.name.indexOf(newVal) !== -1;
                    })
                }
            }
        }
    });

</script>

</html>
```
## 3、排序方法 `sort`

1. `sort` 函数会改变原数组
2. `sort` 排序允许接受一个参数（函数），这个函数接受2个形参a,b,并且通过冒泡的方式比较
3. 当返回值为负数时，那么前面的数在前面，也就是不动；当返回值为正数时，那么后面的数在前
4. 即，p1 - p2：升序（小的在前面）；p2 - p1：降序（大的在前面）
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 引入 vue -->
    <script src="../js/vue.js"></script>
</head>
<body>

    <!-- 准备一个 vue 容器 -->
    <div id="root">

        <input type="text" placeholder="请输入姓名：" v-model="keyWord">
        <button @click="sortType = 1">升序</button>
        <button @click="sortType = 2">降序</button>
        <button @click="sortType = 0">原顺序</button>
        <!-- for-of 循环；key：每次循环的唯一标识符 -->
        <ul v-for="(per, index) of personsFilter" :key="per.id">
            <li>{{per.id}}-{{per.name}}-{{per.age}}</li>
        </ul>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            keyWord: '',
            persons: [
                {id: 01, name: '月海', age: 16},
                {id: 02, name: '言', age: 14},
                {id: 03, name: '羽', age: 16},
            ],
            // 因为计算属性是属性不是函数，不可以传递参数；所以这里定义一个变量，来代表点击的哪个按钮
            // 1升序 2降序 0原顺序
            sortType: 0
        },
        computed: {
            personsFilter(){
                let arr = this.persons.filter((p) => {
                    return p.name.indexOf(this.keyWord) !== -1
                })
                
                // 判断排序类型
                if( this.sortType === 1 ){
                    // sort 函数会改变原数组，p1 - p2 则为降序；p2 - p1 则为升序
                    arr.sort((p1, p2) =>{
                        return p2.age - p1.age;
                    })
                }else if( this.sortType === 2 ){
                    arr.sort((p1, p2) => {
                        return p1.age - p2.age;
                    })
                }
            }
        }
    });

</script>

</html>
```
## 4、`Object.defineProperty()` 方法
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 引入 vue -->
    <!-- <script src="../js/vue.js"></script> -->
</head>
<body>
    
    <h2>数据代理</h2>
    <button id="btn">点击</button>

</body>

<script>

    // 定义一个对象
    const yuehai = {
        name:"月海",
        age:16
    }
    console.log(yuehai);

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 调用 Object.defineProperty() 方法，给对象添加属性
        // 参数 1、要处理的对象
        // 参数 2、要添加的属性
        // 参数 3、配置项
        Object.defineProperty(yuehai, 'sex', {
            // 添加的属性的值（默认不可以被枚举，不参与遍历）
            value: 0,
            // 控制属性是否可以枚举，默认值是 false
            enumerable: true,
            // 控制属性是否可以修改，默认值是 false
            writable: true,
            // 控制属性是否可以删除，默认值是 false
            configurable: true,
        })

        Object.defineProperty(yuehai, 'play', {
            // 当有人读取 yuehai 的 play 属性时，get函数（getter）就会被调用，且返回值就是 play 的值 
            get(){
                console.log('有人读取 play 属性');
                return '玩月海'
            },
            // 当有人修改 yuehai 的 play 属性时，set函数（setter）就会被调用，且会收到修改的具体值
            set(value){
                console.log('要修改的值是：' , value);
            }
        })

        console.log(yuehai);
        // 遍历对象的属性名，变成数组（验证 Object.defineProperty() 是否可枚举）
        console.log(Object.keys(yuehai));

    })

</script>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1669768809894-e6e1e3cd-c86e-477d-b7ea-b7f27771591a.png#clientId=uae438773-a405-4&from=paste&height=626&id=u8cb7df2e&name=image.png&originHeight=626&originWidth=801&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74614&status=done&style=stroke&taskId=ub5300bd5-2565-4613-a04c-3501c9cc279&title=&width=801)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1669768883718-d375b603-3610-4d91-bbf1-5464eba81fb6.png#clientId=uae438773-a405-4&from=paste&height=389&id=u9b29dd84&name=image.png&originHeight=389&originWidth=779&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29943&status=done&style=stroke&taskId=u51dfac47-2834-42a2-bf76-6ca76438f81&title=&width=779)
## 5、
## 6、
## 7、
## 8、
## 9、






















