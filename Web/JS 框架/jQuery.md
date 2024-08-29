> [https://developer.aliyun.com/course/25](https://developer.aliyun.com/course/25) ，这个视频讲的很差

## 一、JQuery 简介

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-39-680--BdNMHxNrq_LlKw.png)

## 二、下载引入

### 1、本地文件

1. 官网：[https://jquery.com/](https://jquery.com/)
2. 下载相应的版本引入即可

### 2、网络库引入

1. 选择 JQuery 官方或其他网络库
2. 使用标签引入即可

```javascript
<!-- 以链接的方式引入 JQuery 库 -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
```

## 三、基础语法

jQuery 语法是通过选取 HTML 元素，并对选取的元素执行某些操作
基础语法： $(selector).action()

1. 美元符号定义 jQuery
2. 选择符（selector）"查询"和"查找" HTML 元素
3. jQuery 的 action() 执行对元素的操作

- 实例

```javascript
$(this).hide() - 隐藏当前元素

$("p").hide() - 隐藏所有 <p> 元素

$("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素

$("#test").hide() - 隐藏 id="test" 的元素
```
```javascript
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
    <p>月海</p>
</body>

<script>

    $(Document).ready(function(){
        alert("文档加载完毕");
    })

</script>

</html>
```

## 四、选择器

jQuery 选择器允许对 HTML 元素组或单个元素进行操作

> 菜鸟教程：[jQuery 选择器](https://www.runoob.com/jquery/jquery-ref-selectors.html)

### 1、基础选择器

#### ①、选择所有元素 - (*)

- 描述：选择所有元素
- 语法：`$("*")`
- 注意，由于是选择所有元素，有些浏览器将会比较缓慢，这个选择器要谨慎使用

```javascript
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
    <p>月海</p>
    <div>
        <p>月海111</p>
        <a>月海222</a>
    </div>
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择所有元素；.html()：设置或返回所选元素的内容（包括 HTML 标记）
        // $("*").html("言");
        // 选择 div 标签下的所有元素
        $("div *").html("言");
    })
    
</script>

</html>
```

#### ②、类选择器 - (".class")

- 描述：选择给定的类名的所有元素
- 语法：`$(".class")`

```javascript
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
    <p class="yuehai">月海</p>
    <div>
        <p>月海111</p>
        <a class="yuehai">月海222</a>
    </div>
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择所有 class 属性中带有 yuehai 的元素
        $(".yuehai").html("言");
    })
    
</script>

</html>
```

#### ③、id 选择器 - ("#id")

- 描述：选择一个具有给定 id 属性的元素
- 语法：`$("#id")`

```javascript
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
    <p class="yuehai">月海</p>
    <div>
        <p id="111">月海111</p>
        <a class="yuehai">月海222</a>
    </div>
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择 id 为 111 的元素
        $("#111").html("言");
    })
    
</script>

</html>
```

#### ④、标签（元素）选择器 - ("标签名")

- 描述：选择给定标签名的所有元素
- 语法：`$("标签名")`

```javascript
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
    <p class="yuehai">月海</p>
    <div>
        <p>月海111</p>
        <a class="yuehai">月海222</a>
    </div>
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择标签名为 p 的所有元素
        $("p").html("言");
    })
    
</script>

</html>
```

#### ⑤、组合选择器 - ("#a,.b,c,...")

- 描述：选择多种元素，可将上面的选择器组合使用；只要满足其中一个就会被选择
- 语法：`$("选择器1,选择器2,选择器3,...")`

```javascript
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
    <p class="yuehai">月海</p>
    <div>
        <p id="111">月海111</p>
        <a class="yuehai">月海222</a>
    </div>
    <ul>
        <li>月海000123</li>
        <li>月海000123</li>
        <li>月海000123</li>
        <li>月海000123</li>
    </ul>
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择 id 为 111、class 为 yuehai、标签名为 li 的元素
        $("#111,.yuehai,li").html("言");
    })
    
</script>

</html>
```

### 2、属性选择器

属性值的引号是可选的
若是一个单词则可以不带引号
若是中间带空格则需要带引号

#### ①、指定值

```javascript
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
    <a class="yuehai" href="#" hreflang="zh">月海</a>
    

    <a class="yuehai" href="http://www.baidu.com" hreflang="en">百度</a>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 hreflang 的值为 en 的元素
        $("[hreflang=en]").css("color","red");
    })

</script>

</html>
```

#### ②、包含某字符串的值

```javascript
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
    <a class="yuehai" href="#" hreflang="zh" yuehai="yuehaui">月海</a>
    

    <a class="yuehai" href="http://www.baidu.com" hreflang="en" yuehai="yuehaui">百度</a>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 yuehai 的值包含 y 的元素
        $("[yuehai*=y]").css("color","red");
    })

</script>

</html>
```

#### ③、用空格分隔的值中的某个值

```javascript
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
    <p yuehai="yue hai">月海</p>
    <p yuehai="yu e hai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 yuehai 的值中用空格分隔的值中包含 yue 的元素
        $("[yuehai~=yue]").css("color","red");
    })

</script>

</html>
```

#### ④、指定值或以指定值为前缀（用 - 分隔）

```javascript
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
    <p yuehai="yueh-ai">月海</p>
    <p yuehai="yue-hai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 yuehai 的值为 yue 或 以 yue 为前缀（用 - 分隔）的元素
        $("[yuehai|=yue]").css("color","red");
    })

</script>

</html>
```

#### ⑤、不存在给定值的值

- 描述：整个网页的所有标签元素中，只要没有这个属性和值都会被选择

```javascript
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
    <p yuehai="yan">月海</p>
    <p yuehai="yuehai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 整个网页的所有标签元素中，只要没有 yuehai=yan 这个属性的都会被选择
        $("[yuehai!=yan]").css("color","red");
    })

</script>

</html>
```

#### ⑥、以给定值结尾的值

- 描述：区分大小写

```javascript
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
    <p yuehai="yuehaiyan">月海</p>
    <p yuehai="yuehai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 yuehai 的值中以 yan 结尾的元素
        $("[yuehai$=yan]").css("color","red");
    })

</script>

</html>
```

#### ⑦、以给定值开头的值

- 描述：区分大小写

```javascript
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
    <p yuehai="yuehai yan">月海</p>
    <p yuehai="yuehai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择属性 yuehai 的值中以 yan 开头的元素
        $("[yuehai^=y]").css("color","red");
    })

</script>

</html>
```

#### ⑧、选择属性

- 描述：只要有该属性就选择，不管值是什么

```javascript
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
    <p yuehai="yuehai yan" yan="yu">月海</p>
    <p yuehai="yuehai">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择存在 yan 这个属性的元素
        $("[yan]").css("color","red");
    })

</script>

</html>
```

#### ⑨、组合属性选择器

- 描述：选择多种元素，可将上面的选择器组合使用；要满足全部的条件才行

```javascript
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
    <p yuehai="yuehai yan" yan="yu">月海</p>
    <p yuehai="yuehai">百度</p>
    <p yuehai="yue">百度</p>
    <p yuehai="hai">百度</p>
    <p yuehai="yan">百度</p>
    <p yu="yu">百度</p>
    <p aaa="bbb">百度</p>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择 属性 yuehai 的值中以 i 结尾、以 y 开头、包含 u 的元素
        $("[yuehai$=i][yuehai^=y][yuehai*=u]").css("color","red");
    })

</script>

</html>
```

### 3、基础过滤

#### ①、选择所有正在执行动画效果的元素（:animated）

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

    <style>
        div{
            width: 100px;
            height: 100px;
            background-color: yellow;
            float: left;
            border: 1px solid black;
            margin: 0 5px;
        }
        .colored{
            background-color: green;
        }
    </style>
</head>
<body>
    
    <button id="run">run</button>
    <div></div>
    <div id="mover"></div>
    <div></div>

</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // 选择 id 为 run 的元素，为其绑定单击事件
        $("#run").click(function(){
            // 选择 div 元素中，正在执行动画效果的元素，添加或移除 colored 类
            $("div:animated").toggleClass("colored");
        })

        // 定义一个函数
        function animatedIt(){
            // 选择 id 为 mover 的元素，执行 slideToggle 方法
            // 如果被选元素是可见的，则隐藏这些元素，如果被选元素是隐藏的，则显示这些元素；通过使用滑动效果（高度变化）来切换元素的可见状态
            // $(selector).slideToggle(speed,callback)：
            //      speed：可选。规定元素从隐藏到可见的速度（或者相反）。默认为 "normal"。值：毫秒 （比如 1500）、"slow"、"normal"、"fast"
            //      callback：可选。toggle 函数执行完之后，要执行的函数；除非设置了 speed 参数，否则不能设置该参数
            $("#mover").slideToggle("slow",animatedIt);
        }

        // 调用 animatedIt 函数
        animatedIt();

    })
</script>

</html>
```

#### ②、选择给定索引值的元素（:eq(index)）

- 可以是负值，这样的话就是从后往前数，但是 -0 还是整数第一个， -1 才是倒数第一个

```javascript
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
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择 li 标签中的 第2个 标签
        $("li:eq(1)").css("color","red");
        // 选择 li 标签中的 倒数第2个 标签（如果是 -0 的话就是选择正数第一个）
        $("li:eq(-2)").css("color","red");
    })

</script>

</html>
```

#### ③、选择大于给定索引值的元素（:gt(index)）

- 可以是负值，这样的话就是从后往前数，但是 -0 还是整数第一个， -1 才是倒数第一个

```javascript
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
    <h1>111</h1>
    <h2>222</h2>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择大于 li 标签中的 第5个 标签的元素
        $("li:gt(4)").css("color","red");
        // 选择选择大于 li 标签中的 倒数第4个 标签的元素的元素（如果是 -0 的话就是选择正数第一个）
        $("li:gt(-4)").css("color","red");

    })

</script>

</html>
```

#### ④、选择小于给定索引值的元素（:lt(-index)）

- 可以是负值，这样的话就是从后往前数，但是 -0 还是整数第一个， -1 才是倒数第一个

```javascript
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
    <h1>111</h1>
    <h2>222</h2>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择小于 li 标签中的 第5个 标签的元素
        $("li:lt(4)").css("color","red");
        // 选择选择小于 li 标签中的 倒数第4个 标签的元素的元素（如果是 -0 的话就是选择正数第一个）
        $("li:lt(-4)").css("color","red");

    })

</script>

</html>
```

#### ⑤、选择索引值为偶数的元素（:even）

- 因为索引值是从 0 开始，索引选择的元素是第 1、3、5、7 ... 个

```javascript
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
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择索引值为偶数的元素
        $("li:even").css("color","red");
    })

</script>

</html>
```

#### ⑥、选择索引值为奇数的元素（:odd）

- 因为索引值是从 0 开始，索引选择的元素是第 2、4、6、8 ... 个

```javascript
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
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择索引值为奇数的元素
        $("li:odd").css("color","red");
    })

</script>

</html>
```

#### ⑦、选择第一个匹配的元素（:first）

```javascript
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
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择第一个匹配的元素
        $("li:first").css("color","red");
    })

</script>

</html>
```

#### ⑧、选择最后一个匹配的元素（:last）

```javascript
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
    <h1>111</h1>
    <h2>222</h2>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择最后一个匹配的元素
        $("li:last").css("color","red");
    })

</script>

</html>
```

#### ⑨、选择当前获取焦点的元素（:focus）

```javascript
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
    <input class="colored" type="text" value="1">
    <input type="text" value="2">
    <input type="text" value="3">
    <input type="text" value="4">
    <input type="text" value="5">
</body>

<script>
    // 网页加载完毕立即执行
    $(function(){
        // input 标签的焦点改变时触发此函数
        $("input").focus(function(){
            // 获取当前焦点的 value ，并赋值给 value 属性
            var value = $(":focus").val();
            // 打印
            console.log(value);
        })
    })

</script>

</html>
```

#### ⑩、选择所有标题元素（:header）

- 像 h1、h2 等

```javascript
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
    <h1>111</h1>
    <h2>222</h2>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择所有标题元素，像 h1、h2 等
        $(":header").css("color","red");
    })

</script>

</html>
```

### 4、子元素过滤
#### ①、选择所有属于其父元素的第 n 个子元素

- `:nth-child(index)`
- 选择同级元素中的第 n 个是给定标签的元素，不是给定标签的元素不会选择

```javascript
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
    <p>pppp</p>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <ul>
        <p>pppp</p>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 判断所有 li 标签同级的第 2 个标签，是 li 标签的话就选择（第 2 个就是第 2 个，不是从 0）
        $("li:nth-child(2)").css("color","red");
    })

</script>

</html>
```

#### ②、选择所有属于其父元素的第一个子元素

- `:first-child`
- 选择同级元素中的第一个是给定标签的元素，不是给定标签的元素不会选择

```javascript
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
    <p>pppp</p>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <ul>
        <p>pppp</p>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 判断所有 li 标签同级的第一个标签，是 li 标签的话就选择
        $("li:first-child").css("color","red");
    })

</script>

</html>
```

#### ③、选择所有属于其父元素的最后一个子元素

- `:last-child`
- 选择同级元素中的最后一个是给定标签的元素，不是给定标签的元素不会选择

```javascript
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
    <p>pppp</p>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <ul>
        <p>pppp</p>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 判断所有 li 标签同级的最后一个标签，是 li 标签的话就选择
        $("li:last-child").css("color","red");
    })

</script>

</html>
```

#### ④、选择所有相同的元素名称的第一个兄弟元素

- `:first-of-type`
- 选择同级元素中的第一个是给定标签的元素

```javascript
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
    <p>pppp</p>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <ul>
        <p>pppp</p>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择所有 li 标签同级的的第一个兄弟元素
        $("li:first-of-type").css("color","red");
    })

</script>

</html>
```

#### ⑤、选择所有相同的元素名称的最后一个兄弟元素

- `:last-of-type`
- 选择同级元素中的最后一个是给定标签的元素

```javascript
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
    <p>pppp</p>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <ul>
        <p>pppp</p>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
        <li>7</li>
    </ul>
</body>

<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择所有 li 标签同级的的最后一个兄弟元素
        $("li:last-of-type").css("color","red");
    })

</script>

</html>
```

### 5、内容过滤
#### ①、选择所有包含指定文本的元素

- `:contains(text)`
- text：用来查找的一个字符串，区分大小写
- 匹配的文本可以直接出现在所选元素中，或在该元素的任何后代中，或两者兼有

```javascript
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
        <p>月海</p>
        <p>言</p>
    </div>

    <div>
        <p>yuehai</p>
        <p>言</p>
    </div>
</body>
<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 判断 div 标签中是否包含字符串：月海
        $("div:contains(月海)").css("color","red");
    })

</script>
</html>
```

#### ②、根据指定的选择器选取包含一个或多个元素的元素

- `:has(selector)`
- 只要包含其指定的元素就可，即使被子元素包含

```javascript
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
        <span>yuehai</span>
        <p>月海</p>
        <p>言</p>
    </div>

    <div>
        <p>yuehai</p>
        <p>言</p>
        <p></p>
    </div>
</body>
<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 判断 div 标签中是否包含 span 标签
        $("div:has(span)").css("color","red");
    })

</script>
</html>
```

#### ③、选择所有不包含子元素或文本的元素

- `:empty`
- 只会选择指定的标签，不会选择更下一层的标签（除非不指定，*选择所有）

```javascript
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
    <table border="1">
        <tr>
            <td>11</td>
            <td>12</td>
        </tr>
        <tr>
            <td>21</td>
            <td></td>
        </tr>
        <tr>
            <td>31</td>
            <td>32</td>
        </tr>
    </table>
</body>
<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择 td 标签中的不包含子元素或文本的元素
        $("td:empty").css("background-color","yellow");
    })

</script>
</html>
```

#### ④、选择所有包含子元素或文本的元素

- `:parent`
- 与 `:empty` 相反

```javascript
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
    <table border="1">
        <tr>
            <td>11</td>
            <td>12</td>
        </tr>
        <tr>
            <td>21</td>
            <td></td>
        </tr>
        <tr>
            <td>31</td>
            <td>32</td>
        </tr>
    </table>
</body>
<script>

    // 网页加载完毕立即执行
    // .css()：设置元素的 css 样式
    $(function(){
        // 选择 td 标签中的包含子元素或文本的元素
        $("td:parent").css("background-color","yellow");
    })

</script>
</html>
```

### 6、表单
#### ①、选择所有类型为按钮的元素

- `:button`

```javascript
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
    <form action="">
        <input type="text" value="文本框">
        <button value="按钮1">按钮1</button>
        <button value="按钮2">按钮2</button>
    </form>
</body>

<script>

    $(function(){

        $(":button").css("background-color","red");

    })

</script>

</html>
```

#### ②、选择所有类型为复选框的元素

- `:checkbox`

#### ③、选择所有类型为密码的元素

- `:password`

#### ④、选择所有类型为图像的元素

- `:image`

#### ⑤、选择所有类型为文件的元素

- `:file`

#### ⑥、选择所有类型为 input 的元素

- `:input`
- 同样会选择 textarea、select、button 元素

#### ⑦、选择所有勾选的元素

- `:checked`

#### ⑧、选择所有被禁用的元素

- `:disabled`

#### ⑨、选择所有可用（未被禁用）的元素

- `:enabled`

#### ⑩、选择所有当前获取焦点的元素

- `:focus`
- 和之前的一样

### 7、层级

#### ①、子元素选择器

- `parent > child`
- parent：任何有效的选择器
- child：用来筛选子元素的选择器
- 选择所有指定 parent 元素中的直接子元素 child 
- 只能选择直接子元素

#### ②、后代元素选择器

- `parent descendant`
- parent：任何有效的选择器
- child：用来筛选后代元素的选择器
- 选择所有指定 parent 元素中的后代元素 child 

#### ③、紧邻下一个元素选择器

- `element + next`
- 紧邻 element 元素的下一个 next 元素

#### ④、兄弟元素选择器

- `element ~ siblings`
- 和 element 元素同级的所有 siblings 元素

### 8、可见性过滤

#### ①、选择所有隐藏的元素

- `:hidden`
- 元素可以被认为是隐藏的几个情况
   - 他们的 CSS display 的值是 none
   - 他们是 type="hidden" 的表单元素
   - 他们的宽度和高度都设置为 0
   - 一个祖先元素是隐藏的，因此该元素是不会在页面上显示的

#### ②、选择所有可见的元素

- `:visible`
- 如果元素占据文档中一定的空间，元素被认为是可见的。可见元素的宽度或高度，是大于零。
- 所以:元素的 visibility:hidden 或 opacity:0 被认为是可见的，因为他们仍然占用空间布局。
- 不在文档中的元素是被认为隐藏的，jQuery 没有办法知道他们是否是可见的，因为元素可见性依赖于适用的样式。
- 隐藏元素上做动画，元素被认为是可见的，直到动画结束。显示元素上做动画，在动画的开始处该元素被认为是可见的。

### 9、JQuery 扩展

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-40-150--uO-tuvVVwCJvZA.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-40-382--ILpGUH_sz1ErbQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-40-576--VuVW3URDnXRoxA.png)

### 10、【总结】

#### ①、基本选择器

| 选择器 | 介绍 |
| --- | --- |
| $("#id")  | ID选择器 |
| $("div")  | 元素选择器 |
| $(".classname") | 类选择器 |
| $(".classname,.classname1,#id1") | 组合选择器 |

#### ②、层次选择器

| 选择器 | 介绍 |
| --- | --- |
| $("#id>.classname ") | 子元素选择器 |
| $("#id .classname ") | 后代元素选择器 |
| $("#id + .classname ") | 紧邻下一个元素选择器 |
| $("#id ~ .classname ") | 兄弟元素选择器 |

#### ③、过滤选择器(重点)

| 选择器 | 介绍 |
| --- | --- |
| $("li:first") | 第一个li |
| $("li:last") | 最后一个li |
| $("li:even") | 挑选下标为偶数的li |
| $("li:odd") | 挑选下标为奇数的li |
| $("li:eq(4)") | 下标等于 4 的li(第五个 li 元素) |
| $("li:gt(2)") | 下标大于 2 的li |
| $("li:lt(2)") | 下标小于 2 的li |
| $("li:not(#runoob)") | 挑选除 id="runoob" 以外的所有li |

#### ④、内容过滤选择器

| 选择器 | 介绍 |
| --- | --- |
| $("div:contains('Runob')") | 包含 Runob文本的元素 |
| $("td:empty") | 不包含子元素或者文本的空元素 |
| $("div:has(selector)") | 含有选择器所匹配的元素 |
| $("td:parent") | 含有子元素或者文本的元素 |

#### ⑤、可见性过滤选择器

| 选择器 | 介绍 |
| --- | --- |
| $("li:hidden") | 匹配所有不可见元素，或type为hidden的元素 |
| $("li:visible") | 匹配所有可见元素 |

#### ⑥、属性过滤选择器

| 选择器 | 介绍 |
| --- | --- |
| $("div[id]") | 所有含有 id 属性的 div 元素  |
| $("div[id='123']") | id属性值为123的div 元素 |
| $("div[id!='123']") |  id属性值不等于123的div 元素 |
| $("div[id^='qq']") | id属性值以qq开头的div 元素 |
| $("div[id$='zz']")  | id属性值以zz结尾的div 元素 |
| $("div[id*='bb']") | id属性值包含bb的div 元素 |
| $("input[id][name$='man']") | 多属性选过滤，同时满足两个属性的条件的元素 |

#### ⑦、状态过滤选择器

| 选择器 | 介绍 |
| --- | --- |
| $("input:enabled") | 匹配可用的 input  |
| $("input:disabled") | 匹配不可用的 input  |
| $("input:checked") | 匹配选中的 input  |
| $("option:selected") | 匹配选中的 option |

#### ⑧、表单选择器

| 选择器 | 介绍 |
| --- | --- |
| $(":input") | 匹配所有 input, textarea, select 和 button 元素  |
| `$(":text")` | 所有的单行文本框，`$(":text")` 等价于`$("[type=text]")`，推荐使用`$("input:text")`效率更高，下同 |
| $(":password") | 所有密码框  |
| $(":radio") | 所有单选按钮  |
| $(":checkbox") | 所有复选框  |
| $(":submit") | 所有提交按钮  |
| $(":reset") | 所有重置按钮  |
| $(":button") | 所有button按钮  |
| $(":file") | 所有文件域 |

## 五、事件

> 菜鸟教程：[jQuery 事件方法](https://www.runoob.com/jquery/jquery-ref-events.html)

### 1、鼠标事件

| 鼠标事件 | 说明 |
| --- | --- |
| [click](https://www.runoob.com/jquery/event-click.html) | 点击事件 |
| [dblclick](https://www.runoob.com/jquery/event-dblclick.html) | 双击事件 |
| [hover](https://www.runoob.com/jquery/event-hover.html) | 鼠标悬停和离开 |
| [mouseenter](https://www.runoob.com/jquery/event-mouseenter.html) | 鼠标进入元素 |
| [mouseleave](https://www.runoob.com/jquery/event-mouseleave.html) | 鼠标离开元素 |
| mousedown() | 当鼠标指针移动到元素上方，并按下鼠标按键时（还没抬起来） |
| mouseup() | 当在元素上松开鼠标按钮时 |
| mousemove() | 鼠标在元素内移动 |
| mouseover() | 鼠标进入元素（支持事件冒泡） |
| mouseout() | 鼠标离开元素（支持事件冒泡） |

- 事件冒泡：当子元素（事件源）事件触发，事件会沿着包含关系，依次往上级传递，每一级都可以感知到事件，直到触发根元素（根源)

### 2、键盘事件

| 键盘事件 | 说明 |
| --- | --- |
| [keydown](https://www.runoob.com/jquery/event-keydown.html) | 键按下的过程 |
| [keyup](https://www.runoob.com/jquery/event-keyup.html) | 键被松开 |
| [keypress](https://www.runoob.com/jquery/event-keypress.html) | 键被按下；keypress 事件不会触发所有的键（比如 ALT、CTRL、SHIFT、ESC），请使用 keydown() 方法来检查这些键 |

- 常用键盘按键对应的代码：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-40-791--TnnohSPX9R9O4Q.png)

### 3、浏览器事件

| 窗口事件 | 说明 |
| --- | --- |
| [scroll](https://www.runoob.com/jquery/event-scroll.html) | 当用户滚动指定的元素时，会发生 scroll 事件 |
| [resize](https://www.runoob.com/jquery/event-resize.html) | 当调整浏览器窗口大小时，发生 resize 事件 |

### 4、文档加载事件

| 文档加载事件 | 说明 |
| --- | --- |
| ready | 当 DOM（document object model 文档对象模型）加载完毕且页面完全加载（包括图像）时发生 ready 事件 |
| load | load() 方法在 jQuery 版本 1.8 中[已废弃](https://www.runoob.com/jquery/NewWindow('deprecated.htm')) |

```javascript
		// ready 的写法
    // 1、正经写法
    $(document).ready(function(){

    })

    // 2、简写1
    $().ready(function(){

    })

    // 3、简写2（常用）
    $(function(){
        
    })
```

**文档加载过程：**

1. 解析 HTML 结构
2. 加载外部脚本和样式表文件
3. 解析并执行脚本代码
4. 构造 HTML DOM 模型
5. 加载图片等外部文件
6. 页面加载完成

### 5、绑定事件处理器

| 方法 | 描述 |
| --- | --- |
| [bind()](https://www.runoob.com/jquery/event-bind.html) | 向元素添加事件处理程序 |
| [delegate()](https://www.runoob.com/jquery/event-delegate.html) | 向匹配元素的当前或未来的子元素添加处理程序 |
| [off()](https://www.runoob.com/jquery/event-off.html) | 移除通过 on() 方法添加的事件处理程序 |
| [on()](https://www.runoob.com/jquery/event-on.html) | 向元素添加事件处理程序 |
| [one()](https://www.runoob.com/jquery/event-one.html) | 向被选元素添加一个或多个事件处理程序。该处理程序只能被每个元素触发一次 |
| [unbind()](https://www.runoob.com/jquery/event-unbind.html) | 从被选元素上移除添加的事件处理程序 |
| [undelegate()](https://www.runoob.com/jquery/event-undelegate.html) | 从现在或未来的被选元素上移除事件处理程序 |

- 对于由 jQuery 动态生成的元素，如用 jQuery 给元素添加 class，或者直接添加一对 p 标签，不能直接绑定常用的事件，如 click。因为这些元素属于动态生成，除非采用 noclick 内联的形式。那么解决办法是使用 live 和 on 事件方法。注意，jquery 1.7.2 之后的版本不建议使用 live
- 例如：

```javascript
$(".box ").click(function(){});

// 类名为 box 的元素是由 jquery 动态生成，以上写法将会无效，那么可以改为如下：
$(".box ").live('click', function(){});

// 或者：
$(".box ").on('click', function(){});

// 另外 click, blur, keyup, change等方法，都可以这样解决。
```

### 6、事件对象

| 方法 | 描述 |
| --- | --- |
| [event.currentTarget](https://www.runoob.com/jquery/jq-event-currenttarget.html) | 在事件冒泡阶段内的当前 DOM 元素 |
| [event.data](https://www.runoob.com/jquery/event-data.html) | 包含当前执行的处理程序被绑定时传递到事件方法的可选数据 |
| [event.delegateTarget](https://www.runoob.com/jquery/event-delegatetarget.html) | 返回当前调用的 jQuery 事件处理程序所添加的元素 |
| [event.isDefaultPrevented()](https://www.runoob.com/jquery/event-isdefaultprevented.html) | 返回指定的 event 对象上是否调用了 event.preventDefault() |
| [event.isImmediatePropagationStopped()](https://www.runoob.com/jquery/event-isimmediatepropagationstopped.html) | 返回指定的 event 对象上是否调用了 event.stopImmediatePropagation() |
| [event.isPropagationStopped()](https://www.runoob.com/jquery/event-ispropagationstopped.html) | 返回指定的 event 对象上是否调用了 event.stopPropagation() |
| [event.namespace](https://www.runoob.com/jquery/event-namespace.html) | 返回当事件被触发时指定的命名空间 |
| [event.pageX](https://www.runoob.com/jquery/event-pagex.html) | 返回相对于文档左边缘的鼠标位置 |
| [event.pageY](https://www.runoob.com/jquery/event-pagey.html) | 返回相对于文档上边缘的鼠标位置 |
| [event.preventDefault()](https://www.runoob.com/jquery/event-preventdefault.html) | 阻止事件的默认行为 |
| [event.relatedTarget](https://www.runoob.com/jquery/jq-event-relatedtarget.html) | 返回当鼠标移动时哪个元素进入或退出 |
| [event.result](https://www.runoob.com/jquery/event-result.html) | 包含由被指定事件触发的事件处理程序返回的最后一个值 |
| [event.stopImmediatePropagation()](https://www.runoob.com/jquery/event-stopimmediatepropagation.html) | 阻止其他事件处理程序被调用 |
| [event.stopPropagation()](https://www.runoob.com/jquery/event-stoppropagation.html) | 阻止事件向上冒泡到 DOM 树，阻止任何父处理程序被事件通知 |
| [event.target](https://www.runoob.com/jquery/jq-event-target.html) | 返回哪个 DOM 元素触发事件 |
| [event.timeStamp](https://www.runoob.com/jquery/jq-event-timestamp.html) | 返回从 1970 年 1 月 1 日到事件被触发时的毫秒数 |
| [event.type](https://www.runoob.com/jquery/jq-event-type.html) | 返回哪种事件类型被触发 |
| [event.which](https://www.runoob.com/jquery/event-which.html) | 返回指定事件上哪个键盘键或鼠标按钮被按下 |
| [event.metaKey](https://www.runoob.com/jquery/event_metakey.html) | 事件触发时 META 键是否被按下 |

```javascript
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
    <a href="https://www.baidu.com/">百度</a>
</body>

<script>
    $(function(){
        // 给 a 标签添加点击事件，并传入参数 e
        $("a").click(function(e){
            // 调用事件对象：阻止事件的默认行为
            e.preventDefault();
            
            // 点击后触发的事件
            alert("阻止超链接跳转的默认事件");
        });
    })
</script>

</html>
```

### 7、表单事件

| 方法 | 描述 |
| --- | --- |
| [focus()](https://www.runoob.com/jquery/event-focus.html) | 添加/触发获得焦点事件；当元素获得焦点时，发生 focus 事件 |
| [blur()](https://www.runoob.com/jquery/event-blur.html) | 添加/触发失去焦点事件；当元素失去焦点时，发生 blur 事件 |
| [change()](https://www.runoob.com/jquery/event-change.html) | 添加/触发 change 事件；当元素的值发生改变时，会发生 change 事件 |
| [select()](https://www.runoob.com/jquery/event-select.html) | 添加/触发 select 事件；当 textarea 或文本类型的 input 元素中的文本被选择时，会发生 select 事件 |
| [submit()](https://www.runoob.com/jquery/event-submit.html) | 添加/触发 submit 事件；当提交表单时，会发生 submit 事件 |

```javascript
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
    <form action="">
        <input id="1" type="text" value="1">
        <input id="2" type="text" value="2">
        <input id="btn" type="button" value="按钮">
    </form>
</body>

<script>
    $(function(){
        // 给 id 为 btn 的标签添加点击事件
        $("#btn").click(function(){
            // 给 id 为 1 的标签添加 失去焦点事件
            $("#1").blur(function(){
                // 失去焦点后触发的事件
                alert("失去焦点事件")
            })
        });
    })
</script>

</html>
```

### 8、DOM 属性

- HTML / CSS 方法

| 方法 | 描述 |
| --- | --- |
| [attr()](https://www.runoob.com/jquery/html-attr.html) | 设置或返回被选元素的属性/值 |
| [addClass()](https://www.runoob.com/jquery/html-addclass.html) | 向被选元素添加一个或多个类名 |
| [prop()](https://www.runoob.com/jquery/html-prop.html) | 设置或返回被选元素的属性/值 |
| [hasClass()](https://www.runoob.com/jquery/html-hasclass.html) | 检查被选元素是否包含指定的 class 名称 |
| [removeAttr()](https://www.runoob.com/jquery/html-removeattr.html) | 从被选元素移除一个或多个属性 |
| [removeClass()](https://www.runoob.com/jquery/html-removeclass.html) | 从被选元素移除一个或多个类 |
| [removeProp()](https://www.runoob.com/jquery/html-removeprop.html) | 移除通过 prop() 方法设置的属性 |
| [toggleClass()](https://www.runoob.com/jquery/html-toggleclass.html) | 在被选元素中添加/移除一个或多个类之间切换 |
| [val()](https://www.runoob.com/jquery/html-val.html) | 设置或返回被选元素的属性值（针对表单元素） |

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 以链接的方式引入 JQuery 库 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <style>
        .a{
            color: red;
        }
    </style>
</head>
<body>
    <p>123</p>
</body>

<script>
    $(function(){
        // 在每个 p 标签上添加类名 a
        $("p").addClass("a");
        // 在每个 p 标签后插入内容
        $("p").after("在每个 p 标签后插入内容");
    })
</script>

</html>
```

### 9、DOM 操作 - 插入并包裹现有内容

| 方法 | 描述 |
| --- | --- |
| [wrap()](https://www.runoob.com/jquery/html-wrap.html) | 在每个被选元素的周围用 HTML 元素包裹起来 |
| [wrapAll()](https://www.runoob.com/jquery/html-wrapall.html) | 在所有被选元素的周围用 HTML 元素包裹起来 |
| [wrapInner()](https://www.runoob.com/jquery/html-wrapinner.html) | 在每个被选元素的内容周围用 HTML 元素包裹起来 |

### 10、DOM 属性 - 插入到现有元素内

| 方法 | 描述 |
| --- | --- |
| [append()](https://www.runoob.com/jquery/html-append.html) | 在被选元素的结尾插入内容 |
| [appendTo()](https://www.runoob.com/jquery/html-appendto.html) | 在被选元素的结尾插入 HTML 元素 |
| [prepend()](https://www.runoob.com/jquery/html-prepend.html) | 在被选元素的开头插入内容 |
| [prependTo()](https://www.runoob.com/jquery/html-prependto.html) | 在被选元素的开头插入 HTML 元素 |
| [html()](https://www.runoob.com/jquery/html-html.html) | 设置或返回被选元素的内容 |
| [text()](https://www.runoob.com/jquery/html-text.html) | 设置或返回被选元素的文本内容 |

```javascript
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
    <p>111</p>
    <p>222</p>
</body>

<script>
    $(function(){
        // 在每个 p 标签的结尾插入内容
        $("p").append("结尾插入的内容");
        // 在每个 p 标签的结尾添加 <h1>111</h1>
        $("<h1>111</h1>").appendTo("p");
			
				// 返回 p 标签的内容
        console.log($("p").html());
        // 设置 p 标签的内容
        console.log($("p").html(333));
    })
</script>

</html>
```

### 11、DOM 属性 - 插入到现有元素外

| 方法 | 描述 |
| --- | --- |
| [after()](https://www.runoob.com/jquery/html-after.html) | 在被选元素后插入内容 |
| [before()](https://www.runoob.com/jquery/html-before.html) | 在被选元素前插入内容 |
| [insertAfter()](https://www.runoob.com/jquery/html-insertafter.html) | 在被选元素后插入 HTML 元素 |
| [insertBefore()](https://www.runoob.com/jquery/html-insertbefore.html) | 在被选元素前插入 HTML 元素 |

### 12、DOM 移除、替换

| 方法 | 描述 |
| --- | --- |
| [detach()](https://www.runoob.com/jquery/html-detach.html) | 移除被选元素（保留数据和事件） |
| [empty()](https://www.runoob.com/jquery/html-empty.html) | 从被选元素移除所有子节点和内容 |
| [remove()](https://www.runoob.com/jquery/html-remove.html) | 移除被选元素（包含数据和事件） |
| [unwrap()](https://www.runoob.com/jquery/html-unwrap.html) | 移除被选元素的父元素 |
| [replaceAll()](https://www.runoob.com/jquery/html-replaceall.html) | 把被选元素替换为新的 HTML 元素 |
| [replaceWith()](https://www.runoob.com/jquery/html-replacewith.html) | 把被选元素替换为新的内容 |

### 13、DOM 复制元素

| 方法 | 描述 |
| --- | --- |
| [clone()](https://www.runoob.com/jquery/html-clone.html) | 生成被选元素的副本 |

### 14、CSS 属性

| 方法 | 描述 |
| --- | --- |
| [css()](https://www.runoob.com/jquery/css-css.html) | 为被选元素设置或返回一个或多个样式属性 |
| [height()](https://www.runoob.com/jquery/css-height.html) | 设置或返回被选元素的高度 |
| [width()](https://www.runoob.com/jquery/css-width.html) | 设置或返回被选元素的宽度 |
| [innerHeight()](https://www.runoob.com/jquery/html-innerheight.html) | 返回元素的高度（包含 padding，不包含 border） |
| [innerWidth()](https://www.runoob.com/jquery/html-innerwidth.html) | 返回元素的宽度（包含 padding，不包含 border） |
| [outerHeight()](https://www.runoob.com/jquery/html-outerheight.html) | 返回元素的高度（包含 padding 和 border） |
| [outerWidth()](https://www.runoob.com/jquery/html-outerwidth.html) | 返回元素的宽度（包含 padding 和 border） |
| [scrollTop()](https://www.runoob.com/jquery/css-scrolltop.html) | 设置或返回被选元素的垂直滚动条位置 |
| [scrollLeft()](https://www.runoob.com/jquery/css-scrollleft.html) | 设置或返回被选元素的水平滚动条位置 |
| [offset()](https://www.runoob.com/jquery/css-offset.html) | 设置或返回被选元素的偏移坐标（相对于文档） |
| [position()](https://www.runoob.com/jquery/css-position.html) | 返回元素的位置（相对于父元素） |
| [offsetParent()](https://www.runoob.com/jquery/css-offsetparent.html) | 返回第一个定位的祖先元素 |
| [$.escapeSelector()](https://www.runoob.com/jquery/html-escapeSelector.html) | 转义CSS选择器中有特殊意义的字符或字符串 |
| [$.cssHooks](https://www.runoob.com/jquery/html-csshooks.html) | 提供了一种方法通过定义函数来获取和设置特定的CSS值 |

## 六、遍历

> 菜鸟教程：[JQuery 遍历](https://www.runoob.com/jquery/jquery-traversing.html)
> 菜鸟教程：[JQuery 遍历方法](https://www.runoob.com/jquery/jquery-ref-traversing.html)

1. jQuery 遍历，意为"移动"，用于根据其相对于其他元素的关系来"查找"（或选取）HTML 元素。以某项选择开始，并沿着这个选择移动，直到抵达您期望的元素为止。
2. 下图展示了一个家族树。通过 jQuery 遍历，您能够从被选（当前的）元素开始，轻松地在家族树中向上移动（祖先），向下移动（子孙），水平移动（同胞）。这种移动被称为对 DOM 进行遍历

![image.png](https://www.yue-hai.top:10300/file/downloadFile?basePathType=takeDown&subPath=%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-40-921--i8xU8-faarwjwQ.png)

> - `<div>` 元素是 `<ul>` 的父元素，同时是其中所有内容的祖先。
> - `<ul>` 元素是 `<li>` 元素的父元素，同时是 `<div>` 的子元素
> - 左边的 `<li>` 元素是 `<span>` 的父元素，`<ul>` 的子元素，同时是 `<div>` 的后代。
> - `<span>` 元素是 `<li>` 的子元素，同时是 `<ul>` 和 `<div>` 的后代。
> - 两个 `<li>` 元素是同胞（拥有相同的父元素）。
> - 右边的 `<li>` 元素是 `<b>` 的父元素，`<ul>` 的子元素，同时是 `<div>` 的后代。
> - `<b>` 元素是右边的 `<li>` 的子元素，同时是 `<ul>` 和 `<div>` 的后代。

### 1、过滤

| 方法 | 描述 |
| --- | --- |
| [eq()](https://www.runoob.com/jquery/traversing-eq.html) | 返回带有被选元素的指定索引号的元素 |
| [first()](https://www.runoob.com/jquery/traversing-first.html) | 返回被选元素的第一个元素 |
| [last()](https://www.runoob.com/jquery/traversing-last.html) | 返回被选元素的最后一个元素 |
| [filter()](https://www.runoob.com/jquery/traversing-filter.html) | 把匹配元素集合缩减为匹配选择器或匹配函数返回值的新元素 |
| [has()](https://www.runoob.com/jquery/traversing-has.html) | 返回拥有一个或多个元素在其内的所有元素 |
| [is()](https://www.runoob.com/jquery/traversing-is.html) | 根据选择器/元素/jQuery 对象检查匹配元素集合，如果存在至少一个匹配元素，则返回 true |
| [not()](https://www.runoob.com/jquery/traversing-not.html) | 从匹配元素集合中移除元素 |
| map() | 把当前匹配集合中的每个元素传递给函数，产生包含返回值的新 jQuery 对象 |
| [slice()](https://www.runoob.com/jquery/traversing-slice.html) | 把匹配元素集合缩减为指定范围的子集 |

### 2、树遍历

- 祖先、兄弟、后代等
  
| 方法 | 描述 |
| --- | --- |
| addBack() | 把之前的元素集添加到当前集合中 |
| [parents()](https://www.runoob.com/jquery/traversing-parents.html) | 返回被选元素的所有祖先元素 |
| [closest()](https://www.runoob.com/jquery/traversing-closest.html) | 返回被选元素的第一个祖先元素 |
| [siblings()](https://www.runoob.com/jquery/traversing-siblings.html) | 返回被选元素的所有同级元素 |
| [prevAll()](https://www.runoob.com/jquery/traversing-prevall.html) | 返回被选元素之前的所有同级元素 |
| [nextAll()](https://www.runoob.com/jquery/traversing-nextall.html) | 返回被选元素之后的所有同级元素 |
| [prev()](https://www.runoob.com/jquery/traversing-prev.html) | 返回被选元素的前一个同级元素 |
| [next()](https://www.runoob.com/jquery/traversing-next.html) | 返回被选元素的后一个同级元素 |
| [parent()](https://www.runoob.com/jquery/traversing-parent.html) | 返回被选元素的直接父元素 |
| [children()](https://www.runoob.com/jquery/traversing-children.html) | 返回被选元素的所有直接子元素 |
| [find()](https://www.runoob.com/jquery/traversing-find.html) | 返回被选元素的后代元素 |
| [offsetParent()](https://www.runoob.com/jquery/traversing-offsetparent.html) | 返回第一个定位的父元素 |
| [parentsUntil()](https://www.runoob.com/jquery/traversing-parentsuntil.html) | 返回介于两个给定参数之间的所有祖先元素 |
| [prevUntil()](https://www.runoob.com/jquery/traversing-prevuntil.html) | 返回介于两个给定参数之间的每个元素之前的所有同级元素 |
| [nextUntil()](https://www.runoob.com/jquery/traversing-nextuntil.html) | 返回介于两个给定参数之间的每个元素之后的所有同级元素 |
| [each()](https://www.runoob.com/jquery/traversing-each.html) | 为每个匹配元素执行函数 |

### 3、其他遍历

| 方法 | 描述 |
| --- | --- |
| [add()](https://www.runoob.com/jquery/traversing-add.html) | 把元素添加到匹配元素的集合中 |
| [contents()](https://www.runoob.com/jquery/traversing-contents.html) | 返回被选元素的所有直接子元素（包含文本和注释节点） |
| end() | 结束当前链中最近的一次筛选操作，并把匹配元素集合返回到前一次的状态 |

## 七、特效（效果）

> 菜鸟教程：[jQuery 效果方法](https://www.runoob.com/jquery/jquery-ref-effects.html)

### 1、隐藏与显示

| 方法 | 描述 |
| --- | --- |
| [hide()](https://www.runoob.com/jquery/eff-hide.html) | 隐藏被选元素 |
| [show()](https://www.runoob.com/jquery/eff-show.html) | 显示被选元素 |
| [toggle()](https://www.runoob.com/jquery/eff-toggle.html) | hide() 和 show() 方法之间的切换 |

### 2、淡入与淡出

| 方法 | 描述 |
| --- | --- |
| [fadeIn()](https://www.runoob.com/jquery/eff-fadein.html) | 逐渐改变被选元素的不透明度，从隐藏到可见 |
| [fadeOut()](https://www.runoob.com/jquery/eff-fadeout.html) | 逐渐改变被选元素的不透明度，从可见到隐藏 |
| [fadeToggle()](https://www.runoob.com/jquery/eff-fadetoggle.html) | 在 fadeIn() 和 fadeOut() 方法之间进行切换 |
| [fadeTo()](https://www.runoob.com/jquery/eff-fadeto.html) | 把被选元素逐渐改变至给定的不透明度 |

### 3、滑动

| 方法 | 描述 |
| --- | --- |
| [slideUp()](https://www.runoob.com/jquery/eff-slideup.html) | 通过调整高度来滑动隐藏被选元素 |
| [slideDown()](https://www.runoob.com/jquery/eff-slidedown.html) | 通过调整高度来滑动显示被选元素 |
| [slideToggle()](https://www.runoob.com/jquery/eff-slidetoggle.html) | slideUp() 和 slideDown() 方法之间的切换 |

### 4、回调（链）

> 通过 jQuery，可以把动作/方法链接在一起。
> Chaining 允许我们在一条语句中运行多个 jQuery 方法（在相同的元素上）

- 下面的例子把 css()、slideUp() 和 slideDown() 链接在一起。"p1" 元素首先会变为红色，然后向上滑动，再然后向下滑动

```javascript
$("#p1").css("color","red").slideUp(2000).slideDown(2000);
```

### 5、自定义效果

| 方法 | 描述 |
| --- | --- |
| [animate()](https://www.runoob.com/jquery/eff-animate.html) | 对被选元素应用"自定义"的动画 |
| [delay()](https://www.runoob.com/jquery/eff-delay.html) | 对被选元素的所有排队函数（仍未运行）设置延迟 |
| [stop()](https://www.runoob.com/jquery/eff-stop.html) | 停止被选元素上当前正在运行的动画 |
| [finish()](https://www.runoob.com/jquery/eff-finish.html) | 对被选元素停止、移除并完成所有排队动画 |
| [dequeue()](https://www.runoob.com/jquery/eff-dequeue.html) | 移除下一个排队函数，然后执行函数 |
| [clearQueue()](https://www.runoob.com/jquery/eff-clearqueue.html) | 对被选元素移除所有排队函数（仍未运行的） |
| [queue()](https://www.runoob.com/jquery/eff-queue.html) | 显示被选元素的排队函数 |

