> [https://developer.aliyun.com/learning/course/595](https://developer.aliyun.com/learning/course/595)，视频不太好
> 代码：[Ajax.jpg](https://www.yuque.com/attachments/yuque/0/2023/jpeg/29280567/1673925268858-9deaf0aa-f10a-48b3-8624-d3ff268bbaea.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fjpeg%2F29280567%2F1673925268858-9deaf0aa-f10a-48b3-8624-d3ff268bbaea.jpeg%22%2C%22name%22%3A%22Ajax.jpg%22%2C%22size%22%3A119994%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22type%22%3A%22image%2Fjpeg%22%2C%22taskId%22%3A%22u85cc8a32-3a29-424e-a0b1-4ab7298d343%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22mode%22%3A%22title%22%2C%22id%22%3A%22u8852449d%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

## 一、Ajax 概念
### 1、Ajax 是什么

1. AJAX：Asynchronous JavaScript and XML
2. AJAX 是一种用于创建快速动态网页的技术。
3. AJAX 通过在后台与服务器进行少量数据交换，使网页实现异步更新。这意味着可以在不重载整个页面的情况下，对网页的某些部分进行更新。
4. 传统的网页（不使用 AJAX）如果需要更新内容，必须重载整个页面。
5. 有很多使用 AJAX 的应用程序案例：Google Maps、Gmail、Youtube 和 Facebook
### 2、Ajax 的作用

- 获取服务器的数据
### 3、Ajax 的效果

- 在不刷新整个网页的情况下，通过一个 url 地址获取服务器的数据，然后进行页面的局部刷新
### 4、Ajax 如何工作
![](https://cdn.nlark.com/yuque/0/2022/gif/29280567/1657175088151-a195babc-50c3-4dd0-a383-df3ec0c3f58f.gif#clientId=uaa1c8773-3935-4&from=paste&id=Wx9Iy&originHeight=308&originWidth=576&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=stroke&taskId=udd4f7dfc-b28e-46d1-a8d4-5796a48e2df&title=)
### 5、AJax 基于因特网标准
AJAX 基于因特网标准，并使用以下技术组合：

1. XMLHttpRequest 对象（与服务器异步交互数据）
2. JavaScript/DOM（显示/取回信息）
3. CSS（设置数据的样式）
4. XML（常用作数据传输的格式）

💡lamp AJAX 应用程序与浏览器和平台无关的！
### 6、小结
:::info
局部、异步刷新
:::
Ajax 的全称：Asynchronous JavaScript and XML，就是使用 JS 代码获取服务器数据
## 二、基础知识铺垫 - 网络与服务器
### 1、服务器与客户端的概念
:::info
服务器和客户端其实都是电脑，下面从几个方面来介绍一下他们二者之间的差异
:::
#### ①、概念层面上的差异

1. 服务器：能够提供某种服务的电脑
2. 客户端：想使用服务器所提供服务的电脑
#### ②、硬件层面上的差异

1. 服务器：由于要给千千万万个客户端提供服务，因此一 般来说，服务器的硬件配置要高一些
2. 客户端：个人电脑、手机、平板等都可以称作为客户端
#### ③、服务器图例
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657176250143-b09c1ab0-64e2-425c-853c-f7c2078ba74b.png#clientId=uaa1c8773-3935-4&from=paste&height=443&id=u6d7f48b7&name=image.png&originHeight=443&originWidth=651&originalType=binary&ratio=1&rotation=0&showTitle=false&size=524819&status=done&style=stroke&taskId=ue00cc4d9-b43f-4cb2-89f5-6fe95ef36bf&title=&width=651)
#### ④、客户端图例
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657176315018-d1994d08-1112-446e-b9fc-0aa623c32d8d.png#clientId=uaa1c8773-3935-4&from=paste&height=200&id=u8bb8f078&name=image.png&originHeight=200&originWidth=562&originalType=binary&ratio=1&rotation=0&showTitle=false&size=117523&status=done&style=stroke&taskId=ua9413a26-c7f7-48c9-86bd-5e0a33d8ef6&title=&width=562)

- 服务器与客户端在硬件上并没有明显的划分，配置很差的个人电脑依然可以当作服务器使用，只不过这台服务器的速度慢一些而已
#### ⑤、服务器能提供什么服务？
些我们日常生活中常使用的功能，其实都是服务器所提供的服务。比如网页服务、邮箱服务、文件上传下载服务、聊天服务等等
#### ⑥、服务器软件

1. 既然服务器也是一台电脑，那这台电脑就必须要安装操作系统，否则就是一台裸机，啥事情都做不了，更不用说提供服务了
2. 一般来说，服务器更多会选择 Linux 操作系统，而个人电脑更多会选择安装 Windows 操作系统
3. 服务器能提供服务是由于在服务器操作系统上安装了很多软件，由这些软件对外提供服务，比如：
   1. HTTP网页服务：Apache、Tomcat、 IIS 等。
   2. 文件上传下载服务：VsFtp 等。
   3. 邮箱服务：SendMail 等。
   4. 数据存储服务：MySq|、Oracle 等
#### ⑦、小结：服务器就是提供服务的，客户端就是使用服务器所提供的服务
### 2、网络相关的概念
#### ①、IP 地址

1. 地址是为了标注某个地点，方便查找
2. 互联网上就那么多公司，每家公司都有自己的服务器提供服务。通过 ip 地址就找到特定的服务器，使用这台服务器提供的服务
3. 比如百度服务器的ip地址为：123.125.114.144
#### ②、域名

1. 由于 IP 地址是一串数字，人很难记忆。就好像经度纬度一样， 人们能记忆下来是地名。而域名就相当于是地名一样，方便人们查找到服务器
2. 比如：www.baidu.com、www.qq.come
3. 查看本机的 IP： ipconfig

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657177545441-28bebc15-0c3f-4c78-88cd-1485eae44803.png#clientId=u548c7152-2476-4&from=paste&height=480&id=u5dbe1275&name=image.png&originHeight=480&originWidth=551&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13194&status=done&style=stroke&taskId=uf73b1dd8-3715-4c6e-aec2-021410d4cc1&title=&width=551)
#### ③、DNS 域名解析服务器

1. DNS 叫做域名解析服务器，提供域名与 ip 地址的映射关系
2. 访问服务器的流程：本机 hosts 文件 --> DNS 服务器 --> 服务器
3. 本机 host 文件的路径为：C:\Windows\System32\drivers\etc\HOSTS

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657178172422-8e445731-b041-437d-838f-1219720a7d05.png#clientId=u548c7152-2476-4&from=paste&height=493&id=u885beea3&name=image.png&originHeight=493&originWidth=1156&originalType=binary&ratio=1&rotation=0&showTitle=false&size=143004&status=done&style=stroke&taskId=uf49ffb6b-9dbb-4846-93ec-800bb30c170&title=&width=1156)
#### ④、端口

1. 前面我们说过，服务器就是提供服务的。ip 地址是用来查找某一台服务器的，域名是方便人们记忆的，DNS 维护着域名和 ip 地址的映射关系，所以通过域名是可以找到某一台服务器的
2. 我们确实是可以通过域名来找到一台服务器，但是一台服务器可能提供多种服务，我们找到这台服务器的时候，究竟是想使用这台服务器的什么服务呢？这就使用端口号来进行区分
3. 其实我们每次访问网页，最完整的写法应该是 htp://www.baidu.com:80，80 这个端口比较特殊，可以省略不写
4. 再比如我们在设置邮箱客户端的时候，也需要指定端口号
### 3、通信协议的概念
:::info
通信协议就是事先规定好的规则
:::

1. 想一想人和人的交流是怎么进行的：说同一门语言才能交流无障碍。那机器与机器之间的交流也需要满足实现规定的规则
2. 客户端访问服务器，通过 IP 地址和端口已经找到了这台服务器了，这时候就认为是两台计算机在交流，协议可以简单的认为是两台计算机交流时候说的话
3. 常见的协议：
   1. HTTP、HTTPS 超文本传输协议
   2. FTP 文件传输协议
   3. SMTP 简单邮件传输协议
4. 在HTTP协议中，需要大致了解的是：请求头、响应头、请求体、响应体
5. 计算机世界中充满着各种各样的协议，任何一种协议都是约定一些规范。对于协议本身，里面的内容相当复杂，我们没有必要深究
6. 小结：通信协议就是计算机交流时事先约定的规则
### 4、Wamp 的安装和配置 
#### ①、为什么要安装 Wampe
将我们写的 html 界面以服务的方式分享给别人看，否则别人的电脑是无法看到我们所写的界面
#### ②、Wamp 是什么
Wamp指的是：windows、apache、mysql、php几个服务器软件的缩写
类似的还有Lamp：linux、apache、 mysq|、 phpe
我们安装 wamp 可以认为把我们自己的电脑变成了一台服务器，服务器是干嘛的，提供服务的。Wamp 可以让我们的电脑提供网页服务。其他电脑只需要通过 ip 地址或者域名
就能够访问到对应的 HTML 界面
#### ③、Wamp 的安装
> [Wamp 官网地址](http://www.wampserver.com/en)

选择合适你操作系统的安装包，双击安装之后一路 next 即可完成安装。安装完成后，运行服务，当右下角的图标变为绿色，即代表服务安装成功。接下来将我们需要
以服务方式分享给别人看的 html 文件放到 C:\wamp\www 目录下即可
#### ④、Wamp 的简单配置

1. 配置访问权限： 默认情况下，apache 提供的网页服务只允许 localhost 和 127.0.0.1 进行访问，我们需要对配置文件进行修改。配置文件位于：C:\wamp\bin\apache\Apache2.4.4\conf\httpd.conf ，将 268 行的 Deny from all 改为 Allow from alle

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657180914186-086f7c6a-a3c8-4745-98ac-bf2037cfba91.png#clientId=u548c7152-2476-4&from=paste&height=151&id=ube255041&name=image.png&originHeight=151&originWidth=474&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88871&status=done&style=stroke&taskId=ucfe1aae5-f8a6-434e-a933-99f94a0fda1&title=&width=474)

2. 网站根路径的配置，默认情况下，网站的根路径为 C:\wamp\www， 在此目录下的文件才可以以服务的方式提供给别人看，如果你不想使用这个目录，也可以进行修改。修改C:\wamp\bin\apache\Apache2.4.4\confhttpd.conf 文件，将 DocumentRoot 进行修改，如下图：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657180954183-9992c302-22ef-4176-a928-59d9d1657bf6.png#clientId=u548c7152-2476-4&from=paste&height=54&id=u7b528c33&name=image.png&originHeight=54&originWidth=345&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37066&status=done&style=stroke&taskId=u6e9a0ca1-147a-4d3c-892b-f6394c8bb65&title=&width=345)
### 5、虚拟主机的配置
## 三、基础知识铺垫 - PHP基础语法
### 1、网站的分类：静态网站和动态网站

1. 静态网站

全部由 HTML 代码格式页面组成的网站，没有数据库的支持，在网站制作和维护方面工作量较大。

2. 动态网站

动态网站并不是指具有动画功能的网站，而是指网站内容可根据不同情况动态变更的网站。一般情况下动态网站通过数据库进行架构
动态网站体现在网页一般是以 asp、jsp、php、aspx 等结尾，动态网页以数据库技术为基础，可以大大降低网站维护的工作量，维护方便
### 2、PHP 语法的基本结构

1. 所有的 PHP 代码都要写到 `<?php .. ?>` 里面
2. PHP 文件可以和 HTML 相互结合进行使用
3. PHP 文件的默认文件扩展名是 `.php`
4. PHP 代码必须在服务器上执行
### 3、echo 的使用

1. `echo`的作用就是向页面当中输入字符串
2. `print_r`输出复杂类型
3. `var_ dump`输出复杂类型
```php
<?php
	// 输出字符串
	echo "<h1>月海</h1>";
?>
```
### 4、变量的声明和变量的使用
无论是变量的声明还是变量的使用都需要用`$`符号
```php
<?php
	// 定义变量
	$str = "言";
	// 使用变量
	echo $str;
?>
```
### 5、字符串的拼接
字符串的拼接使用`.`进行连接
```php
<?php
	// 定义变量
	$str1 = "言";
	$str2 = "yan";
	
	// 字符串拼接
	echo $str1 . $str2;
?>
```
### 6、PHP的执行原理
浏览器是不能识别 PHP 代码的，PHP 代码必须在服务器中执行，双击打开 php 文件是达不到效果的
### 7、数组
#### ①、数组的定义和使用
```php
<?php
    // 定义数组，并添加参数
    $arr = array("月海","yuehai");
    // 用下标向数组中添加数据
    $arr[2] = "言";

    // 打印数组（复杂类型）
    print_r($arr);
    // 也是打印数组（复杂类型）
    var_dump($arr);
		// 将数组转化为 json 格式的字符串
    echo json_encode($arr);
?>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657245920957-f06962e2-a7e8-4bb3-8dba-106bb10d82e1.png#clientId=u98a8b497-4da5-4&from=paste&height=177&id=u7b2e99d3&name=image.png&originHeight=177&originWidth=360&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6843&status=done&style=stroke&taskId=u176461b6-a17a-48cc-9065-32ec8c1ae56&title=&width=360)
#### ②、数组的下标索引自定义
```php
<?php
    // 定义数组，并添加参数；将 月海 的索引改为 yuehai
    $arr = array("yuehai"=>"月海","言");

    // 打印数组（复杂类型）
    var_dump($arr["yuehai"]);
    var_dump($arr[0]);
    var_dump($arr);
?>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657247518667-255eec78-7497-4a13-92b2-a808f77cfa21.png#clientId=u98a8b497-4da5-4&from=paste&height=144&id=u35e2417d&name=image.png&originHeight=144&originWidth=366&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3650&status=done&style=stroke&taskId=u92970839-28ff-4d86-910e-764831ee0e7&title=&width=366)
#### ③、二维数组
##### Ⅰ、二维数组
```php
<?php
    // 定义数组
    $arr = array();

    // 二维数组
    $arr["yuehai"] = array("age"=>16,"height"=>168,"weight"=>50);
    $arr["yan"] = array("age"=>14,"height"=>160,"weight"=>40);

    // 打印数组（复杂类型）
    var_dump($arr);
?>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657248079113-8a8d92ca-aed1-4ad2-a725-aef2fe7e44a5.png#clientId=u98a8b497-4da5-4&from=paste&height=215&id=u2fe24ad2&name=image.png&originHeight=215&originWidth=258&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3473&status=done&style=stroke&taskId=uec8b1689-fc1f-4d35-a5c8-e72304215f0&title=&width=258)
##### Ⅱ、二维数组转 JSON
```php
<?php
    // 定义数组
    $arr = array();

    // 二维数组
    $arr["yuehai"] = array("age"=>16,"height"=>168,"weight"=>50);
    $arr["yan"] = array("age"=>14,"height"=>160,"weight"=>40);

    // 将数组转化为 json 格式的字符串
    echo json_encode($arr);
?>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657248105064-0849ac8f-d4ad-4f2e-9b16-6b5ab90f16de.png#clientId=u98a8b497-4da5-4&from=paste&height=253&id=u43a6b396&name=image.png&originHeight=253&originWidth=212&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14311&status=done&style=stroke&taskId=u13e29b51-cab4-42eb-af66-10ca217fc5f&title=&width=212)
#### ④、数组遍历
##### Ⅰ、普通 for 循环
```php
<?php
    // 定义数组
    $arr = array("月海","yuehai");

    // 普通遍历；依据数组下标进行，只能遍历默认数字下标的数组
    for ($i=0; $i < count($arr); $i++) { 
        echo $arr[$i] . "<br/>";
    }
?>
```
##### Ⅱ、foreach（常用）
```php
<?php
    // 定义数组
    $arr = array("yuehai"=>"月海","言");

    // foreach 遍历；遍历时，将数组 $arr 的 下标赋值给 $key，值赋值给 $value$value
    foreach ($arr as $key => $value) {
        echo $key . "=" . $value . "<br/>";
    }
?>

```
### 8、函数
#### ①、系统函数

1. json_ encode：php中将数组转化为 json 格式的字符串
2. var_dump：输出复杂的数据类型
3. print_r：输出复杂的数据类型
4. count：得到数组的长度
#### ②、自定义函数
和 js 类似，以 function 进行声明
### 9、预定义变量
#### ①、请求类型
请求有时候是需要携带参数的，用来标识特定的要求，根据参数携带位置的不同可以简单的把请求分为 Get 请求和 Post 请求

1. Get 请求：参数在 URL 后面，多个参数用 & 进行连接
2. Post 请求：参数在请求体中
#### ②、获取请求参数的值

1. GET：`$_GET[]`
2. POST：`$_POST[]`
##### Ⅰ、GET

- GET 访问：[http://localhost/Ajax/15.php?username=yuehai&password=000123](http://localhost/Ajax/15.php?username=yuehai&password=000123)
```php
<?php
    // 获取请求参数中 username 的值
    $username = $_GET["username"];
    // 获取请求参数中 password 的值
    $password = $_GET["password"];

    // 判断
    if($username == "yuehai" && $password == "000123"){
        echo "输入正确";
    }else{
        echo "输入错误";
    }
?>
```
##### Ⅱ、POST
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
    
    <h1>测试 POST</h1>
    <form action="16.2.php" method="post">
        用户名：<input type="text" name="username">

        密码：<input type="password" name="password">

        <input type="submit" value="提交">
    </form>

</body>
</html>
```
```php
<?php
    // 获取请求体中 username 的值
    $username = $_POST["username"];
    // 获取请求体中 password 的值
    $password = $_POST["password"];

    // 判断
    if($username == "yuehai" && $password == "000123"){
        echo "输入正确";
    }else{
        echo "输入错误";
    }
?>
```
#### ③、预定义变量
:::info
预定义变量又叫超全局变量
php中，自定义的变量的作用域分两种：全局变量（函数外）、局部作用域（函数内）
预定义变量的作用域称为“超全局作用域”，即：全局作用域 + 局部作用域的总和（函数内外全都可用）
:::
| 变量 | 介绍 |
| --- | --- |
| $GLOBALS | 全局作用域中的全部可用变量，并不包含函数中的局部变量和静态变量 |
| $_REQUEST | 包含了 $_GET，$_POST 和 $_COOKIE 的所有信息 |
| $_GET | 通过 GET 方法提交的数据 |
| $_POST | 通过 POST 方法提交的数据 |
| $_COOKIE | 通过 HTTP Cookies 方式传递给当前脚本的变量所组成的数组 |
| $_FILES | 通过 POST 方式上传到服务器的文件数据 |
| $_SESSION | 当前脚本可用 SESSION 变量组成的数组 |
| $_ENV | 通过环境方式传递给当前脚本的变量组成的数组 |
| $_SERVER | 服务器和执行环境的信息 |

- 由于 $_SERVER 中包含的信息众多，这里只截取了部分结果，部分变量的含义如下表所示
| 变量的名称 | 说明 |
| --- | --- |
| $_SERVER['SERVER_ADDR'] | 当前程序所在的服务器的 IP 地址 |
| $_SERVER['SERVER_NAME'] | 当前程序所在的服务器的主机名。如果程序运行在虚拟主机上，则该名称由虚拟主机所设置的值决定 |
| $_SERVER['REQUERT_METHOD'] | 访问页面使用的请求方法。如 GET、HEAD、POST、PUT 等 |
| $_SERVER['REMOTE_ADDR'] | 浏览当前页面的用户的 IP 地址 |
| $_SERVER['REMOTE_HOST'] | 浏览当前页面的用户的主机名，反向域名解析基于该用户的 REMOTE_ADDR |
| $_SERVER['REMOTE_PORT'] | 用户机器上连接到 Web 服务器所使用的端口号 |
| $_SERVER['SCRIPT_FILENAME'] | 当前程序的绝对路径 |
| $_SERVER['SERVER_PORT'] | 当前运行脚本所在的服务器的端口号，默认是 80，如果使用 SSL 安全连接，则这个值是用户设置的 HTTP 端口 |
| $_SERVER['SERVER_SIGNATURE'] | 包含了服务器版本和虚拟主机名的字符串 |
| $_SERVER['DOCUMENT_ROOT'] | 当前运行脚本所在的文档根目录 |

## 四、Ajax的使用
### 1、使用的基本场景和步骤
:::info
Ajax 简单的来说，就是一个异步的 javascript 请求，用来获取后台服务端的数据，而并不是整个界面进行跳转
:::
在元素 JS 中来实现 Ajax 主要的类就是 XMLHttpRequest，它的使用一般有四个步骤：

1. 创建XMLHttpRequest对象
2. 准备发送网络请求
3. 开始发送网络请求
4. 指定回调函数
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    
</head>
<body>
    
    <h1>模拟注册</h1>
    <form action="18.2.php" method="post">
        用户名：<input id="username" type="text" name="username">
        <input id="btn" type="button" value="校验用户名">
        <!-- 提示语显示处 -->
        <span id="result"></span>
        

        密码：<input type="password" name="password">

        <input type="submit" value="提交">
    </form>

</body>

<script>
    $(function(){
        // 给 id 为 btn 的标签绑定单击事件
        $("#btn").click(function(){
            // 获取 id 为 username 的标签的文本内容
            var username = $("#username").val();

            // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
            // 1. 创建XMLHttpRequest对象
            var xhr = new XMLHttpRequest();

            // 2. 准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
						// 还有第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
            xhr.open("get","18.2.php?username=" + username);

            // 3. 开始发送网络请求；因为请求方式为 get，故此处参数为 null
            xhr.send(null);

            // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
            xhr.onreadystatechange = function(){
                // 获取本次请求的返回值
                var result = xhr.responseText;

                // 在 span 标签内显示提示语
                $("#result").html(result);
            }
        });
    })
</script>
</html>
```
```php
<?php
    // 获取请求体中 username 的值
    $username = $_GET["username"];

    // 模拟注册时的用户名校验
    if($username == "yuehai"){
        echo "用户名已存在";
    }else{
        echo "用户名可注册";
    }
?>
```
### 2、4 个步骤的讲解
```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    
</head>
<body>
    
    <h1>模拟注册</h1>
    <form action="18.2.php" method="post">
        用户名：<input id="username" type="text" name="username">
        <input id="btn" type="button" value="校验用户名">
        <!-- 提示语显示处 -->
        <span id="result"></span>
        

        密码：<input type="password" name="password">

        <input type="submit" value="提交">
    </form>

</body>

<script>
    $(function(){
        // 给 id 为 btn 的标签绑定单击事件
        $("#btn").click(function(){
            // 获取 id 为 username 的标签的文本内容
            var username = $("#username").val();
            console.log(username);

            // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
            // 1. 创建XMLHttpRequest对象；有的浏览器没有这个对象（比如IE6），所以需要做兼容处理
            var xhr = null;
            // 判断浏览器没有这个对象
            if(window.XMLHttpRequest){
                xhr = new XMLHttpRequest();
            }else{
                // IE6浏览器
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
            
            // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
            // 还有第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
            // xhr.open("get","18.2.php?username=" + username,true);

            // 2.2. POST：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径；
            // 还有第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
            xhr.open("post","18.3.php");

            // 3.1. GET：开始发送网络请求；因为请求方式为 get，故此处参数为 null
            // xhr.send(null);

            // 3.2. POST：开始发送网络请求；因为请求方式为 POST，故此处需传递参数
            var param = "username=" + username;
            // 设置请求头信息，写法固定
            xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xhr.send(param);

            // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
            xhr.onreadystatechange = function(){
                // 判断返回状态
                if(xhr.readyState == 4){
                    // 判断服务器是否响应正常
                    if(xhr.status == 200){
                        // 获取本次请求的返回值
                        var result = xhr.responseText;

                        // 在 span 标签内显示提示语
                        $("#result").html(result);
                    }
                }
            }
        });
    })
</script>
</html>
```
```php
<?php
    // 获取请求体中 username 的值
    $username = $_POST["username"];

    // 模拟注册时的用户名校验
    if($username == "yuehai"){
        echo "用户名已存在";
    }else{
        echo "用户名可注册";
    }
?>
```
### 3、同步请求

1. 界面会卡顿，卡顿多长时间，取决于网络速度
2. xhr.onreadystatechange 的回调将不会被执行，需要修改代码后才能获取到数据，将回调去除即可
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    
</head>
<body>
    
    <h1>模拟注册</h1>
    <form action="18.2.php" method="post">
        用户名：<input id="username" type="text" name="username">
        <input id="btn" type="button" value="校验用户名">
        <!-- 提示语显示处 -->
        <span id="result"></span>
        

        密码：<input type="password" name="password">

        <input type="submit" value="提交">
    </form>

</body>

<script>
    $(function(){
        // 给 id 为 btn 的标签绑定单击事件
        $("#btn").click(function(){
            // 获取 id 为 username 的标签的文本内容
            var username = $("#username").val();

            // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
            var xhr = new XMLHttpRequest();
            
            // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
            // 第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
            xhr.open("get","18.2.php?username=" + username,false);

            // 3.1. GET：开始发送网络请求；因为请求方式为 get，故此处参数为 null
            xhr.send(null);

            // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
            // 若是改为同步，则 xhr.onreadystatechange 中的回调函数不会执行
            
            // 直接将回调函数中的代码拿出来
            // 判断服务器是否响应正常
            if(xhr.status == 200){
                // 获取本次请求的返回值
                var result = xhr.responseText;

                // 在 span 标签内显示提示语
                $("#result").html(result);
            }
        });
    })
</script>
</html>
```
```php
<?php
    // 休眠 5 秒；php 中单位为秒
    sleep(5);

    // 获取请求体中 username 的值
    $username = $_GET["username"];

    // 模拟注册时的用户名校验
    if($username == "yuehai"){
        echo "用户名已存在";
    }else{
        echo "用户名可注册";
    }
?>
```
### 4、同步异步的原理
js 中的异步的实现的原理是单线程加事件队列，js 的代码执行是单线程的，所谓的单线程的含义是 js 的代码是从上往下按顺序依次执行的，一定是上一行代码执行完再执行下一行代码
事件队列可以认为是一个容器，这个容器中存储一些回调函数。这些回调函数只有在 js 代码全部执行完成之后，才有可能会去调用，因为 js 是单线程的，一次只能做一件事情
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657269314415-fc6c697b-6bbc-45dc-b8b3-9160b8b9fe36.png#clientId=u3557a9e8-d252-4&from=paste&height=499&id=ZbpvU&name=image.png&originHeight=499&originWidth=1210&originalType=binary&ratio=1&rotation=0&showTitle=false&size=163330&status=done&style=stroke&taskId=u65770bcb-55c4-44d7-8397-3cdb421b3ae&title=&width=1210)

- xhr.onreadystatechange 图解

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657269933638-4a29c05c-4e22-4f5d-a23d-fd8d05b3a9e4.png#clientId=ubc2866f4-11b6-4&from=paste&height=386&id=doygE&name=image.png&originHeight=386&originWidth=1016&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57080&status=done&style=stroke&taskId=udc24b541-3ab8-4b90-ae9e-5c437396b7f&title=&width=1016)
### 5、数据格式的讲解
#### ①、什么是数据格式
:::info
将数据通过一定的规范组织起来，叫做数据格式
:::

- 如：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657270245711-424cb962-31b5-4778-9a5d-939fdd4f278e.png#clientId=ubc2866f4-11b6-4&from=paste&height=34&id=uf9f19add&name=image.png&originHeight=34&originWidth=585&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29404&status=done&style=stroke&taskId=u92531dce-8490-4e60-8f8b-fe7c4f25386&title=&width=585)
#### ②、XML 数据格式

- 缺点：体积太大，传输慢，元数据太多，解析不方便，目前使用的很少

Xml 数据格式是将数据以标签的方式进行组装，必须以 `<?xml version="1.0"encoding="utf-8" ?>` 开头，标签必须成对出现，也就是有开始标签就一定要有结束标签。
Xml 是一个通用的标准，任何人都知道该如何解析它。例如：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657270624832-21dd9e1f-31c4-4054-a6fb-8cc0fc8738d3.png#clientId=ubc2866f4-11b6-4&from=paste&height=441&id=u5544e561&name=image.png&originHeight=441&originWidth=376&originalType=binary&ratio=1&rotation=0&showTitle=false&size=123337&status=done&style=stroke&taskId=u77ada5a0-18f4-4467-9a2d-bf2aa1887cd&title=&width=376)
#### ③、JSON 格式

- 优点：体积小，传输快，解析方便

Json 数据格式类似于 js 中的对象方式，通过 key-value 的形式组装，是一个通用的标准，任何人都知道如何解析它
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657270833105-ea3ee874-ccd6-484a-9fee-dd50fca97f9e.png#clientId=ubc2866f4-11b6-4&from=paste&height=468&id=u0668722b&name=image.png&originHeight=468&originWidth=337&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77837&status=done&style=stroke&taskId=u6a74f951-52e1-4769-ae2e-b8425ae87e7&title=&width=337)
### 6、解析 xml 数据格式
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <div>
        <table border="1">
            <tr>
                <th>书名</th>
                <th>作者</th>
                <th>描述</th>
            </tr>
            <tr>
                <td>三国演义</td>
                <td>罗贯中</td>
                <td>一个沙发纷争的年代</td>
            </tr>
        </table>
    </div>
</body>

<script>
    $(function(){
        // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
        var xhr = new XMLHttpRequest();
        
        // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
        // 第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
        xhr.open("get","26.2.php");

        // 3.1. GET：开始发送网络请求；因为请求方式为 get，故此处参数为 null
        xhr.send(null);

        // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
        xhr.onreadystatechange = function(){
            // 判断返回状态
            if(xhr.readyState == 4){
                // 判断服务器是否响应正常
                if(xhr.status == 200){
                    // 获取本次请求的返回值（XML 格式）
                    var result = xhr.responseXML;

                    console.log(result.getElementsByTagName("booklist")[0]);
                    console.log(result);
                }
            }
        }
    })
</script>

</html>
```
```php
<?php
    header("Content-Type:text/xml;");//这里设置响应头信息，保证浏览器可以把相应内容识别为xml文件类型
    $arr = array();
    $arr[0] = array("name"=>"三国演义","author"=>"罗贯中","desc"=>"一个杀伐纷争的年代");
    $arr[1] = array("name"=>"水浒传","author"=>"施耐庵","desc"=>"108条好汉的故事");
    $arr[2] = array("name"=>"西游记","author"=>"吴承恩","desc"=>"佛教与道教斗争");
    $arr[3] = array("name"=>"红楼梦","author"=>"曹雪芹","desc"=>"一个封建王朝的缩影");
?>

<?xml version="1.0" encoding="utf-8" ?>
<booklist>
    <?php
        foreach ($arr as $key => $value) {
    ?>
    
    <book>
        <name><?php echo $value['name'] ?></name>
        <author><?php echo $value['author'] ?></author>
        <desc><?php echo $value['desc'] ?></desc>
    </book>
    
    <?php
        }
    ?>

</bookkist>
```
### 7、解析 json 数据格式
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <div>
        <table border="1">
            <tr>
                <th>书名</th>
                <th>作者</th>
                <th>描述</th>
            </tr>
            <tr>
                <td>三国演义</td>
                <td>罗贯中</td>
                <td>一个沙发纷争的年代</td>
            </tr>
        </table>
    </div>
</body>

<script>
    $(function(){
        // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
        var xhr = new XMLHttpRequest();
        
        // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
        // 第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
        xhr.open("get","27.2.php");

        // 3.1. GET：开始发送网络请求；因为请求方式为 get，故此处参数为 null
        xhr.send(null);

        // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
        xhr.onreadystatechange = function(){
            // 判断返回状态
            if(xhr.readyState == 4){
                // 判断服务器是否响应正常
                if(xhr.status == 200){
                    // 获取本次请求的返回值（JSON 格式）
                    var result = xhr.responseText;
                    // 将 JSON 字符串转化为对象
                    result = JSON.parse(result);

                    // 插入网页的总字符串
                    var newHtml = "";
                    // 遍历对象，对其进行操作
                    for (var i = 0; i < result.length; i++) {
                        // 获取当我遍历的对象
                        var item = result[i];
                        // 获取对象中的属性
                        var name = item.name;
                        var author = item.author;
                        var desc = item.desc;
                        
                        // 向网页中插入的数据
                        var tempHtml = "<tr><td>" + name + "</td><td>" + author + "</td><td>" + desc + "</td></tr>";
                        newHtml = newHtml + tempHtml;
                    }

                    // 在所选内容的最后插入 HTML 内容
                    $(newHtml).appendTo("table");
                }
            }
        }
    })
</script>

</html>
```
```php
<?php
    $arr = array();
    $arr[0] = array("name"=>"三国演义","author"=>"罗贯中","desc"=>"一个杀伐纷争的年代");
    $arr[1] = array("name"=>"水浒传","author"=>"施耐庵","desc"=>"108条好汉的故事");
    $arr[2] = array("name"=>"西游记","author"=>"吴承恩","desc"=>"佛教与道教斗争");
    $arr[3] = array("name"=>"红楼梦","author"=>"曹雪芹","desc"=>"一个封建王朝的缩影");

    // 将数组转化为 json 格式的字符串
    echo json_encode($arr);
?>

```
## 五、Ajax的封装
:::info
在之前的案例中，我们已经获取了好几次服务器的数据，每当我们需要获取数据的时候，都要写1234四个步骤，略显麻烦，接下来我们需要做的就是将 Ajax 的几个步骤进行封装，封装到一个方法中
:::
### 1、初步封装
对于封装方法，我们主要要考虑几个方面：

1. 哪些东西是变的
2. 哪些东西是不变的
3. 如何将结果通知调用者
4. 如何调用方便

---

1. 根据之前案例的经验，我们知道，不同场景的 ajax 调用，调用方法 get 还是 post 这个是有可能发生改变的，调用 url 地址也是会变的，请求参数也是会变的，返回数据的类型也是会变的。对于发生改变的东西可以通过参数传递的方式实现。
2. 基础代码例如创建 XMLHtpReguest 对象，准备发送、执行发送，响应回调中有些代码也是固定不变的。
3. 将结果通知调用者也可以通过在调用时传入一个方法就可实现。
4. 综上所述，代码可以封装成以下形式：
```javascript
		/**
     * type：请求类型，get 或者 post
     * url：请求地址
     * params：请求参数
     * dataType：服务器返回的数据的类型，json 或者 xml
     * callback：函数，获取数据之后进行的操作
    */
    function myAjax(type,url,params,dataType,callback){
        // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
        // 1. 创建XMLHttpRequest对象；有的浏览器没有这个对象（比如IE6），所以需要做兼容处理
        var xhr = null;
        // 判断浏览器没有这个对象
        if(window.XMLHttpRequest){
            xhr = new XMLHttpRequest();
        }else{
            // IE6 浏览器
            xhr = new ActiveXObject("Microsoft.XMLHTTP");
        }
        
        // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
        // 第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
        // 判断请求是不是 get
        if(type == "get"){
            // 是 get；拼接 url
            url = url + "?" + params;
        }
        xhr.open(type,url);
        
        // 3.1. GET：开始发送网络请求
        // 判断请求是不是 get
        if(type == "get"){
            // 是 get
            xhr.send(null);
        }else if(type == "post"){
            // 是 post；设置请求头信息
            xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xhr.send(params);
        }

        // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
        xhr.onreadystatechange = function(){
            // 判断返回状态
            if(xhr.readyState == 4){
                // 判断服务器是否响应正常
                if(xhr.status == 200){

                    var result = null;
                    // 判断得到的参数是 JSON 还是 XML
                    if(dataType == "json"){
                        // 获取本次请求的返回值（JSON 格式）
                        result = xhr.responseText;
                        // 将 JSON 字符串转化为对象
                        result = JSON.parse(result);
                    }else if(dataType == "xml"){
                        // 获取本次请求的返回值（XML 格式）
                        result = xhr.responseXML;
                    }else{
                        // 都不是
                        result = xhr.responseText;
                    }
                    
                    // 将结果传递出去
                    callback(result);
                }
            }
        }
    }
```
### 2、封装测试
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>

    <div>
        <table border="1">
            <tr>
                <th>书名</th>
                <th>作者</th>
                <th>描述</th>
            </tr>
        </table>
    </div>

</body>

<script>
    // 自己封装的 Ajax 方法

    /**
     * type：请求类型，get 或者 post
     * url：请求地址
     * params：请求参数
     * dataType：服务器返回的数据的类型，json 或者 xml
     * callback：函数，获取数据之后进行的操作
    */
    function myAjax(type,url,params,dataType,callback){
        // 使用 Ajax，此处使用的是 JS 原生的 Ajax，并不是经过 JQuery 封装的
        // 1. 创建XMLHttpRequest对象；有的浏览器没有这个对象（比如IE6），所以需要做兼容处理
        var xhr = null;
        // 判断浏览器没有这个对象
        if(window.XMLHttpRequest){
            xhr = new XMLHttpRequest();
        }else{
            // IE6 浏览器
            xhr = new ActiveXObject("Microsoft.XMLHTTP");
        }
        
        // 2.1. GET：准备发送网络请求；参数 1 为请求方式，参数 2 为请求路径与传递的参数；
        // 第三个参数，同步或异步，true 异步、false 同步（不写默认为异步）
        // 判断请求是不是 get
        if(type == "get"){
            // 是 get；拼接 url
            url = url + "?" + params;
        }
        xhr.open(type,url);
        
        // 3.1. GET：开始发送网络请求
        // 判断请求是不是 get
        if(type == "get"){
            // 是 get
            xhr.send(null);
        }else if(type == "post"){
            // 是 post；设置请求头信息
            xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xhr.send(params);
        }

        // 4. 指定回调函数；即 Ajax 请求成功后执行的函数
        xhr.onreadystatechange = function(){
            // 判断返回状态
            if(xhr.readyState == 4){
                // 判断服务器是否响应正常
                if(xhr.status == 200){

                    var result = null;
                    // 判断得到的参数是 JSON 还是 XML
                    if(dataType == "json"){
                        // 获取本次请求的返回值（JSON 格式）
                        result = xhr.responseText;
                        // 将 JSON 字符串转化为对象
                        result = JSON.parse(result);
                    }else if(dataType == "xml"){
                        // 获取本次请求的返回值（XML 格式）
                        result = xhr.responseXML;
                    }else{
                        // 都不是
                        result = xhr.responseText;
                    }
                    
                    // 将结果传递出去
                    callback(result);
                }
            }
        }
    }

    $(function(){
        // 自己封装的 Ajax 方法所需的参数
        var type = "get";
        var url = "27.2.php";
        var params = null;
        var dataType = "json";
        // 调用自己封装的 Ajax 方法
        myAjax(type,url,params,dataType,function(result){
            // 插入网页的总字符串
            var newHtml = "";
            // 遍历对象，对其进行操作
            for (var i = 0; i < result.length; i++) {
                // 获取当我遍历的对象
                var item = result[i];
                // 获取对象中的属性
                var name = item.name;
                var author = item.author;
                var desc = item.desc;
                
                // 向网页中插入的数据
                var tempHtml = "<tr><td>" + name + "</td><td>" + author + "</td><td>" + desc + "</td></tr>";
                newHtml = newHtml + tempHtml;
            }

            // 在所选内容的最后插入 HTML 内容
            $(newHtml).appendTo("table");
        });
    })
        
</script>

</html>
```
```php
<?php
    $arr = array();
    $arr[0] = array("name"=>"三国演义","author"=>"罗贯中","desc"=>"一个杀伐纷争的年代");
    $arr[1] = array("name"=>"水浒传","author"=>"施耐庵","desc"=>"108条好汉的故事");
    $arr[2] = array("name"=>"西游记","author"=>"吴承恩","desc"=>"佛教与道教斗争");
    $arr[3] = array("name"=>"红楼梦","author"=>"曹雪芹","desc"=>"一个封建王朝的缩影");

    // 将数组转化为 json 格式的字符串
    echo json_encode($arr);
?>

```
### 3、细节完善

- [课程，第 30、31、32、33 课时](https://developer.aliyun.com/lesson_1747_14621#_14621)
## 六、JQuery 中 Ajax 的使用
> 菜鸟教程：[JQuery AJAX 方法 ](https://www.runoob.com/jquery/ajax-ajax.html)

对于 jQuery 中关于 ajax 的封装，它提供了很多方法供开发者进行调用。不过这些封装都是基于一个方法的基础上进行的修改。这个方法就是 `s.ajax()`
在这部分的学习中，我们主要关注 3 个方法：

1. `$.ajax()`
2. `$.get()`
3. `$.post()`
### 1、`$.ajax()`
$.ajax() 的使用是传入一个对象，有些参数不传递的话，也具有默认值
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <div>
        <table border="1">
            <tr>
                <th>书名</th>
                <th>作者</th>
                <th>描述</th>
            </tr>
        </table>
    </div>
</body>

<script>
    $(function(){
        $.ajax({
            // 请求类型（GET 或 POST）
            type:"get",
            // 请求地址
            url:"27.2.php",
            // 请求参数
            // data:{
                // name:"",
                // password:""
            // },
            // 表示请求是否异步处理。默认是 true
            // async:"true",
            // 预期的服务器响应的数据类型
            dateType:"json",
            success:function(result){
                // 将 JSON 字符串转化为对象
                result = JSON.parse(result);

                // 插入网页的总字符串
                var newHtml = "";
                // 遍历对象，对其进行操作
                for (var i = 0; i < result.length; i++) {
                    // 获取当我遍历的对象
                    var item = result[i];
                    // 获取对象中的属性
                    var name = item.name;
                    var author = item.author;
                    var desc = item.desc;
                    
                    // 向网页中插入的数据
                    var tempHtml = "<tr><td>" + name + "</td><td>" + author + "</td><td>" + desc + "</td></tr>";
                    newHtml = newHtml + tempHtml;
                }

                // 在所选内容的最后插入 HTML 内容
                $(newHtml).appendTo("table");
            }
        });
    })
</script>

</html>
```
```php
<?php
    $arr = array();
    $arr[0] = array("name"=>"三国演义","author"=>"罗贯中","desc"=>"一个杀伐纷争的年代");
    $arr[1] = array("name"=>"水浒传","author"=>"施耐庵","desc"=>"108条好汉的故事");
    $arr[2] = array("name"=>"西游记","author"=>"吴承恩","desc"=>"佛教与道教斗争");
    $arr[3] = array("name"=>"红楼梦","author"=>"曹雪芹","desc"=>"一个封建王朝的缩影");

    // 将数组转化为 json 格式的字符串
    echo json_encode($arr);
?>
```
### 2、`$.get()` 和 `$.post()`
jQuery.中对于网络请求，还有其他一些方法，但是本质.上都是对 XMLHttpRequest 的封装，如：`$.get()` 和 `$.post()`
看这两个方法很容易就知道 `$.get` 是针对 get 请求的，`$.post ` 针对的是 post 请求，调用方法如下：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657516864078-c12867ca-02ff-4799-8ba4-6d38c8e87df1.png#averageHue=%2335352b&clientId=uf1ed69ad-fdb9-4&from=paste&height=121&id=u232c10d1&name=image.png&originHeight=121&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&size=70815&status=done&style=stroke&taskId=ubb4a688b-0335-4b58-aaac-fd81a3840e4&title=&width=422)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657516475951-58761ce9-2f9c-4858-a2a5-54f415a32de5.png#averageHue=%232c2c26&clientId=uf1ed69ad-fdb9-4&from=paste&height=87&id=u0f4e2b32&name=image.png&originHeight=87&originWidth=435&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36347&status=done&style=stroke&taskId=uccd5fa51-3492-4c50-8f20-6b5bde3dc13&title=&width=435)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657516698874-0c046bff-6798-4de7-aab6-72ea28a098c0.png#averageHue=%232c2c27&clientId=uf1ed69ad-fdb9-4&from=paste&height=81&id=u32880bc0&name=image.png&originHeight=81&originWidth=468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38532&status=done&style=stroke&taskId=uf33ef634-24e5-4cba-b624-c5a68bbfeba&title=&width=468)
## 七、跨域
### 1、跨域的概念
跨域源于一个叫做同源策略的东西
同源策略是浏览器上为安全性考虑实施的非常重要的安全机制。Ajax 默认是能获取到同源的数据，对于非同源的数据，ajax 默认是获取不到的。
下面举一个例子，来看看什么叫做同源：
比如有一个页面，它的地址为 [http://www.example.com/dir/page.html](http://www.example.com/dir/page.html) 这个网址，在这个网址中，要去获取服务器的数据，获职数据的地址如下所示，在下面的地址中，有的是同源，有的是非同源。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657517050847-d326c10c-b7d5-4669-8123-07ac34be6e76.png#clientId=uf1ed69ad-fdb9-4&from=paste&height=265&id=u9221db5a&name=image.png&originHeight=265&originWidth=681&originalType=binary&ratio=1&rotation=0&showTitle=false&size=127997&status=done&style=stroke&taskId=ucc78cc91-18ba-4fcf-8772-f25f34070e8&title=&width=681)
所谓的同源就是协议、端口、域名三者都完全一样，如果我们使用 ajax 来请求非同源路径下的数据，那么将会报如下错误：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657517452867-70b0474b-3d2c-4fe8-8759-4fc2fc3276f3.png#clientId=uf1ed69ad-fdb9-4&from=paste&height=52&id=u0712d914&name=image.png&originHeight=52&originWidth=665&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47129&status=done&style=stroke&taskId=u4c583c59-97c6-426f-9316-339e1d579f0&title=&width=665)

---

那我们需要处理获取非同源数据获取的情况吗？答案是肯定的。因为前端界面访问非同源的服务器的这种需求是非常常见的，比如在前端界面中获取天气数据，天气数据肯定是存在于别人的服务器上的，我们如果不能使用 ajax 进行访问的话，那么该怎么办呢？这里就需要使用到跨域了。
所以，先把概念理解清楚。不管是 ajax 还是跨域，都是为了访问服务器数据。简单来说：Ajax 是为了访问自己服务器的数据，跨域是为了访问别人服务器的数据。
### 2、跨域的实现
XMLHttpRequest 对象默认情况下是无法获取到非同源服务器下的数据。那么怎么获取别人服务器的数据呢？使用 XMHttpRequest 是达不到的，我们只能另辟蹊径
我们可以通过 script 标签，用 script 标签的 src 属性引入一个外部文件，这个外部文件是不涉及到同源策略的影响的
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

    <!-- 在引入 37.js 文件之前定义 foo() 函数 -->
    <script>
        function foo(data){
            console.log(data);
        }
    </script>
    <!-- 37.js 文件 -->
    <script src="37.js"></script>
</head>
<body>
    
</body>

<script>
    // 调用 37.js 文件中的函数 text()
    test();
</script>

</html>
```
```javascript
var str = "yuehai";
function test(){
    console.log(str);
}

// 调用未定义的函数
foo("123");
```
### 3、动态创建 script 标签
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

    <!-- 在引入 39.js 文件之前定义 foo() 函数 -->
    <script>
        function foo(data){
            console.log(data);
        }
    </script>
    
</head>
<body>
    
    <h1>天气信息查询</h1>
    <input type="text" id="city" placeholder="请输入城市名称">
    <input type="button" id="btn" value="查询">

</body>

<script>
    $(function(){
        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var city = $("#city").val();

            // 动态创建 script 标签，动态指定 src 属性的值
            $("<script src='39.php?city=" + city + " '/>").appendTo("head");
        });
    })
</script>

</html>
```
```php
<?php
    $city = $_GET["city"];
    
    if($city == "北京"){
        echo "foo('北京的天气晴')";
    }else{
        echo "foo('没有查询到天气信息')";
    }
?>
```
### 4、动态指定回调函数
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

    <!-- 在引入 39.js 文件之前定义 foo() 函数 -->
    <!-- <script>
        function foo(data){
            console.log(data);
        }
    </script> -->
    
</head>
<body>
    
    <h1>天气信息查询</h1>
    <input type="text" id="city" placeholder="请输入城市名称">
    <input type="button" id="btn" value="查询">

</body>

<script>
    $(function(){
        // 与之前上面定义 foo 函数的作用相同
        window["foo"] = function(data){
            console.log(data);
        };

        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var city = $("#city").val();

            // 动态创建 script 标签，动态指定 src 属性的值
            // callback=foo：指定调用的函数的名称
            $("<script src='39.php?city=" + city + "&callback=foo '/>").appendTo("head");
        });
    })
</script>

</html>
```
```php
<?php
    // 获取地址信息
    $city = $_GET["city"];
    // 获取函数名
    $callback = $_GET["callback"];
    
    // 判断
    if($city == "北京"){
        echo $callback . "('北京的天气晴')";
    }else{
        echo $callback . "('没有查询到天气信息')";
    }
?>
```
### 5、淘宝提示词案例
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <input type="text" id="keyWord" placeholder="请输入相关的关键字">
    <input type="button" id="btn" value="查询">

    <ul>
    </ul>
</body>

<!-- 淘宝搜索提示地址：https://suggest.taobao.com/sug -->
<!-- 请求类型：get、关键字：q、回调函数：callback -->
<script>
    $(function(){
        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var keyWord = $("#keyWord").val();

            // 动态创建 script 标签，动态指定 src 属性的值
            // callback=data：指定调用的函数的名称
            $("<script src='https://suggest.taobao.com/sug?q=" + keyWord + "&callback=data '/>").appendTo("head");

            // 创建回调函数
            window["data"] = function(data){
                // 遍历返回的对象
                for (let i = 0; i < data.result.length; i++) {
                    var temp = data.result[i];
                    var name = temp[0];

                    动态创建元素
                    $("<li>" + name + "</li>").appendTo("ul");
                    
                }
            };

        });
    })
</script>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657526750224-c3867327-4d9a-4bed-b915-fc899e126260.png#averageHue=%23fdfcfb&clientId=uf6c29a48-a041-4&from=paste&height=310&id=u9094efd4&name=image.png&originHeight=310&originWidth=385&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25366&status=done&style=stroke&taskId=u3a28d89e-b006-48a9-871a-cf57d1e7086&title=&width=385)
### 6、百度提示词案例
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <input type="text" id="keyWord" placeholder="请输入相关的关键字">
    <input type="button" id="btn" value="查询">

    <ul>
    </ul>
</body>

<!-- 百度搜索提示地址：https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su -->
<!-- 请求类型：get、关键字：wd、回调函数：cb -->
<script>
    $(function(){
        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var keyWord = $("#keyWord").val();

            // 动态创建 script 标签，动态指定 src 属性的值
            // callback=data：指定调用的函数的名称
            $("<script src='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=" + keyWord + "&cb=data '/>").appendTo("head");

            // 创建回调函数
            window["data"] = function(data){
                // 遍历返回的对象
                for (let i = 0; i < data.s.length; i++) {
                    var name = data.s[i];

                    // 动态创建元素
                    $("<li>" + name + "</li>").appendTo("ul");
                    
                }
                console.log(data);
            };

        });
    })
</script>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657527242140-a1ba5198-d67d-4864-9848-a431ef94b2bc.png#averageHue=%23fefdfc&clientId=uf6c29a48-a041-4&from=paste&height=278&id=u0679dd96&name=image.png&originHeight=278&originWidth=264&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11856&status=done&style=stroke&taskId=u376986ad-03b3-401a-aba4-1d3623122ef&title=&width=264)
### 7、使用 JQuery 获取跨域数据
使用 JQuery 获取跨域数据：`dataType:"jsonp"`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

</head>
<body>
    <input type="text" id="keyWord" placeholder="请输入相关的关键字">
    <input type="button" id="btn" value="查询">

    <ul>
    </ul>
</body>

<!-- 百度搜索提示地址：https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su -->
<!-- 请求类型：get、关键字：wd、回调函数：cb -->
<script>
    $(function(){
        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var keyWord = $("#keyWord").val();

            // 使用 JQuery 获取跨域数据
            $.ajax({
                // 请求方式
                type:"get",
                // 请求地址
                url:"https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su",
                // 请求参数
                data:{wd:keyWord},
                // 想要获取跨域数据，dataType 一定要是 jsonp
                dataType:"jsonp",
                // 修改回调函数的 key 值
                jsonp:"cb",
                // 修改回调函数的 value 值（一般不用改）
                // jsonpCallback:"data",
                // 回调函数
                success:function(data){
                    // 遍历返回的对象
                    for (let i = 0; i < data.s.length; i++) {
                        var name = data.s[i];

                        // 动态创建元素
                        $("<li>" + name + "</li>").appendTo("ul");
                        
                    }
                    console.log(data);
                }
            });

        });
    })
</script>

</html>
```
## 八、模板引擎的使用
### 1、artTemplate 的简单使用
> Github 下载：[https://aui.github.io/art-template/zh-cn/docs/installation.html](https://aui.github.io/art-template/zh-cn/docs/installation.html)
> 或者点击此图种下载：[art-template-web.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/29280567/1657591636749-952fe160-ea19-4997-a97b-633d4d090378.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F29280567%2F1657591636749-952fe160-ea19-4997-a97b-633d4d090378.jpeg%22%2C%22name%22%3A%22art-template-web.jpg%22%2C%22size%22%3A98616%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22type%22%3A%22image%2Fjpeg%22%2C%22mode%22%3A%22title%22%2C%22taskId%22%3A%22u9125b968-ef7e-40d1-83d0-65c774673f7%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22ucd795465%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <script src="./pack/template-web.js"></script>
    <!-- 
        1、模板的 type="text/html"
        2、给模板配一个 id ：resultTemplate
        3、在其中编写代码
        4、根据 id 使用 ajax 将代码加入到页面中
    -->
    <script type="text/html" id="resultTemplate" >
            <!-- resultTemplate 的循环语法 -->
            {{each s as value i}}
                <li>
                    {{value}}
                </li>
            {{/each}}
    </script>

</head>
<body>
    <input type="text" id="keyWord" placeholder="请输入相关的关键字">
    <input type="button" id="btn" value="查询">

    <ul></ul>

</body>

<!-- 百度搜索提示地址：https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su -->
<!-- 请求类型：get、关键字：wd、回调函数：cb -->
<script>
    $(function(){
        // 绑定点击事件
        $("#btn").click(function(){
            // 获取内容
            var keyWord = $("#keyWord").val();

            // 使用 JQuery 获取跨域数据
            $.ajax({
                // 请求方式
                type:"get",
                // 请求地址
                url:"https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su",
                // 请求参数
                data:{wd:keyWord},
                // 想要获取跨域数据，dataType 一定要是 jsonp
                dataType:"jsonp",
                // 修改回调函数的 key 值
                jsonp:"cb",
                // 修改回调函数的 value 值（一般不用改）
                // jsonpCallback:"data",
                // 回调函数
                success:function(data){
                    // 4、使用 ajax 将代码加入到页面中
                    // template 方法的含义就是将数据和模板结合起来，生成 html 片段
                    var html = template("resultTemplate",data);

                    // 动态创建元素
                    $(html).appendTo("ul");
                }
            });

        });
    })
</script>

</html>
```
### 2、artTemplate 的常用语法
> 教程：[https://www.e-learn.cn/tag/arttemplateyufa](https://www.e-learn.cn/tag/arttemplateyufa)























