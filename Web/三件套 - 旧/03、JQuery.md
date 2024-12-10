# 一、jQuery 介绍

1. 什么是 jQuery：jQuery，顾名思义，也就是 JavaScript 和查询（Query），它就是辅助 JavaScript 开发的 js 类库。
2. jQuery 核心思想：它的核心思想是 write less,do more(写得更少,做得更多)，所以它实现了很多浏览器的兼容问题。
3. jQuery 流行程度：jQuery 现在已经成为最流行的 JavaScript 库，在世界前 10000 个访问最多的网站中，有超过 55%在使用jQuery。
4. jQuery 好处：jQuery 是免费、开源的，jQuery 的语法设计可以使开发更加便捷，例如操作文档对象、选择 DOM 元素、制作动画效果、事件处理、使用 Ajax 以及其他功能

# 二、jQuery 的初体验

1. 常见问题：
2. 使用 jQuery 一定要引入 jQuery 库吗？
	1. 是，必须
3. jQuery 中的 `$` 到底是什么？
	1. 它是一个函数
4. 怎么为按钮添加点击响应函数的？
	1. 使用 jQuery 查询到标签对象
	2. 使用标签对象   .click( function(){} );

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Insert title here</title>
	<!-- 引入 jQuery 库= -->
	<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		// js原生的单击事件
		// window.onload = function () {
		//     var btnObj = document.getElementById("btnId");
		//     // alert(btnObj);//[object HTMLButtonElement] ====>>> dom 对象
		//     btnObj.onclick = function () {
		//         alert("js 原生的单击事件");
		//     }
		// }

		// jQuery 的单击事件
		$(function () { // 表示页面加载完成 之后，相当 window.onload = function () {}
			var $btnObj = $("#btnId"); // 表示按 id 查询标签对象
			$btnObj.click(function () { // 绑定单击事件
				alert("jQuery 的单击事件"); // 单击效果
			});
		});
	</script>
</head>

<body>
	<button id="btnId">SayHello</button>
</body>

</html>
```

# 三、jQuery 核心函数
-  <font color="red">$</font>
1. $ ： 是 jQuery 的核心函数，能完成 jQuery 的很多功能。`$()` 就是调用 $ 这个函数
2. 传入参数为 `[函数]` 时：表示页面加载完成之后。相当于 `window.onload = function(){}`
```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>测试</title>

	<script type="text/javascript" src="../save/script/jquery-1.7.2.js"></script>
	
	<script type="text/javascript">

		// 页面加载完成之后自动调用
		// function()就是函数
		$(function () {
			alert("页面加载完成之后自动调用");
		});

	</script>

</head>

<body>

</body>

</html>
```

3. 传入参数为 `[HTML 字符串]` 时：会对我们创建这个 html 标签对象

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>测试</title>

	<script type="text/javascript" src="../save/script/jquery-1.7.2.js"></script>

	<script type="text/javascript">

		// 页面加载完成之后自动调用
		// function()就是函数
		$(function () {

			// 创建这个 html 标签对象，在 body 标签中
			$(
				"<div>" +
					" <p>可爱</p> " +
				"</div>"
			).appendTo("body");

		});

	</script>

</head>

<body>

	<p>月海</p>

</body>

</html>
```

4. 传入参数为 `[选择器字符串]` 时：
	1. `$("#id 属性值")`：id 选择器，根据 id 查询标签对象
	2. `$("标签名")`：标签名选择器，根据指定的标签名查询标签对象
	3. `$(".class 属性值")`：类型选择器，可以根据 class 属性查询标签对象

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>测试</title>

	<script type="text/javascript" src="../save/script/jquery-1.7.2.js"></script>

	<script type="text/javascript">

		// 页面加载完成之后自动调用
		// function()就是函数
		$(function () {

			alert($("#01").value);
			alert($("button").length);
			alert($(".yan").length);

		});

	</script>

</head>

<body>

	<p >月海</p>
	<button id="#01">按钮1</button>
	<button>按钮2</button>
	<button class=".yan">按钮3</button>

</body>

</html>
```

5. 传入参数为 [ DOM 对象 ] 时：会把这个 dom 对象转换为 jQuery 对象

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>测试</title>

	<script type="text/javascript" src="../save/script/jquery-1.7.2.js"></script>

	<script type="text/javascript">

		var pObj = document.getElementById("#01");
		alert("pObj");

		alert( $("pObj") );

	</script>

</head>

<body>

	<p >月海</p>
	<button id="#01">按钮1</button>
	<button>按钮2</button>
	<button class=".yan">按钮3</button>

</body>

</html>
```

# 四、jQuery 对象和 dom 对象区分

## 1、什么是 jQuery 对象，什么是 dom 对象

1. Dom 对象
	1. 通过 getElementById()查询出来的标签对象是 Dom 对象
	2. 通过 getElementsByName()查询出来的标签对象是 Dom 对象
	3. 通过 getElementsByTagName()查询出来的标签对象是 Dom 对象
	4. 通过 createElement() 方法创建的对象，是 Dom 对象
	5. DOM 对象 Alert 出来的效果是：

```js
[object HTML 标签名 Element]
```

2. jQuery 对象
	1. 通过 JQuery 提供的 API 创建的对象，是 JQuery 对象
	2. 通过 JQuery 包装的 Dom 对象，也是 JQuery 对象
	3. 通过 JQuery 提供的 API 查询到的对象，是 JQuery 对像
	4. jQuery 对象 Alert 出来的效果是：

```js
[object Object]
```

## 2、问题：jQuery 对象的本质是什么？

- <font color="red">jQuery 对象是 dom 对象的数组 + jQuery 提供的一系列功能函数</font>

## 3、jQuery 对象和 Dom 对象使用区别

1. jQuery 对象不能使用 DOM 对象的属性和方法
2. DOM 对象也不能使用 jQuery 对象的属性和方法

## 4、Dom 对象和 jQuery 对象互转

1. <font color="red">dom 对象转化为 jQuery 对象（重点）</font>
	1. 先有 DOM 对象
	2. `$(DOM 对象)` 就可以转换成为 jQuery 对象
2. <font color="red">jQuery 对象转为 dom 对象（重点）</font>
	1. 先有 jQuery 对象
	2. jQuery 对象` [下标]` 取出相应的 DOM 对象

```html
<script type="text/javascript">
	// dom 对象转化为 jQuery 对象
	var docObj = document.getElementById("01");
	var $jqObj = $(docObj);
	// 或
	var $jqObj2 = $(document.getElementById("01"));

	// jQuery 对象转为 dom 对象
	var docObj2 = $jqObj[0];

</script>
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F017、Dom对象和jQuery对象互转.png)

# <font color="red">五、jQuery 选择器（重点）</font>

## <font color="red">1、基本选择器（重点）</font>

| 选择器                            | 介绍                     |
| ------------------------------ | ---------------------- |
| `#ID（id选择器）`                   | </font>根据 id 查找标签对象    |
| `.class`（类选择器）                 | </font>根据 class 查找标签对象 |
| `element`（标签选择器）               | </font>根据标签名查找标签对象     |
| `*`（通配符选择器）                    | </font>表示任意的，所有的元素     |
| `selector1`，`selector2`（组合选择器） | </font>合并选择器 1，选择器 2   |

```js
// 表示标签名必须是 p 标签，而且 class 类型还要是 myClass
p.myClass
```

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Untitled Document</title>
		<style type="text/css">
			div, span, p {
				width: 140px;
				height: 140px;
				margin: 5px;
				background: #aaa;
				border: #000 1px solid;
				float: left;
				font-size: 17px;
				font-family: Verdana;
			}
			
			div.mini {
				width: 55px;
				height: 55px;
				background-color: #aaa;
				font-size: 12px;
			}
			
			div.hide {
				display: none;
			}
		</style>
		<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
		<script type="text/javascript">
				// 网页全部加载完之后，会执行里面的操作
				$(function () {
					// 给 id 为 #btn1 的标签设定单击事件
					$("#btn1").click(function () {
						// css() 方法 可以设置和获取样式
						//1.选择 id 为 one 的元素 "background-color","#bbffaa"
						$("#one").css("background-color","#bbffaa");
					});

					// 给 id 为 #btn2 的标签设定单击事件
					$("#btn2").click(function () {
						//2.选择 class 为 mini 的所有元素
						$(".mini").css("background-color","#bbffaa");
					});

					// 给 id 为 #btn3 的标签设定单击事件
					$("#btn3").click(function () {
						//3.选择 元素名是 div 的所有元素
						$("div").css("background-color","#bbffaa");
					});

					// 给 id 为 #btn4 的标签设定单击事件
					$("#btn4").click(function () {
						//4.选择所有的元素
						$("*").css("background-color","#bbffaa");
					});

					// 给 id 为 #btn5 的标签设定单击事件
					$("#btn5").click(function () {
						//5.选择所有的 span 元素和id为two的元素
						$("span,#two").css("background-color","#bbffaa");
					});

				});

		</script>
	</head>
	<body>
		<!-- 	<div>
			<h1>基本选择器</h1>
		</div>	 -->
		<input type="button" value="选择 id 为 one 的元素" id="btn1" />
		<input type="button" value="选择 class 为 mini 的所有元素" id="btn2" />
		<input type="button" value="选择 元素名是 div 的所有元素" id="btn3" />
		<input type="button" value="选择 所有的元素" id="btn4" />
		<input type="button" value="选择 所有的 span 元素和id为two的元素" id="btn5" />

		<br>
		<div class="one" id="one">
			id 为 one,class 为 one 的div
			<div class="mini">class为mini</div>
		</div>
		<div class="one" id="two" title="test">
			id为two,class为one,title为test的div
			<div class="mini" title="other">class为mini,title为other</div>
			<div class="mini" title="test">class为mini,title为test</div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini"></div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini" title="tesst">class为mini,title为tesst</div>
		</div>
		<div style="display:none;" class="none">style的display为"none"的div</div>
		<div class="hide">class为"hide"的div</div>
		<div>
			包含input的type为"hidden"的div<input type="hidden" size="8">
		</div>
		<span class="one" id="span">^^span元素^^</span>
	</body>
</html>
```

## <font color="red">2、层级选择器（重点）</font>

| 选择器                          | 介绍                                        |
| ---------------------------- | ----------------------------------------- |
| `ancestor descendant`（后代选择器） | </font>在给定的祖先元素下匹配所有的后代元素                 |
| `parent > c`hild（子元素选择器）     | </font>在给定的父元素下只匹配所有的子元素，更下一层不再选择         |
| `prev + next`（相邻元素选择器）       | </font>匹配所有紧接在 prev 元素后的 next 元素，更下一层不再选择 |
| `prev ~ sibings`（之后的兄弟元素选择器） | </font>匹配 prev 元素之后的所有 siblings           |

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Untitled Document</title>
		<style type="text/css">
			div, span, p {
				width: 140px;
				height: 140px;
				margin: 5px;
				background: #aaa;
				border: #000 1px solid;
				float: left;
				font-size: 17px;
				font-family: Verdana;
			}
			
			div.mini {
				width: 55px;
				height: 55px;
				background-color: #aaa;
				font-size: 12px;
			}
			
			div.hide {
				display: none;
			}			
		</style>
		<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
		<script type="text/javascript">
			// 网页全部加载完之后，会执行里面的操作
			$(document).ready(function(){

				// 给 id 为 #btn1 的标签设定单击事件
				$("#btn1").click(function(){
					//1.选择 body 内的所有 div 元素
					$("body div").css("background", "#bbffaa");
				});

				// 给 id 为 #btn2 的标签设定单击事件
				$("#btn2").click(function(){
					//2.在 body 内, 只选择div子元素，更下一层不再选择
					$("body > div").css("background", "#bbffaa");
				});

				// 给 id 为 #btn3 的标签设定单击事件
				$("#btn3").click(function(){
					//3.选择 id 为 one 的下一个 div 元素，更下一层不再选择
					$("#one+div").css("background", "#bbffaa");
				});

				// 给 id 为 #btn4 的标签设定单击事件
				$("#btn4").click(function(){
					//4.选择 id 为 two 的元素后面的所有 div 兄弟元素
					// 不选择 id 为 two 的标签，选择其后面的所有 div 标签
					$("#two~div").css("background", "#bbffaa");
				});
			});
		</script>
	</head>
	<body>

		<!-- 	<div>
			<h1>层级选择器:根据元素的层级关系选择元素</h1>
			ancestor descendant    ：
			parent > child 		   ：
			prev + next 		   ：
			prev ~ siblings 	   ：
		</div>	 -->
		<input type="button" value="选择 body 内的所有 div 元素" id="btn1" />
		<input type="button" value="在 body 内, 选择div子元素" id="btn2" />
		<input type="button" value="选择 id 为 one 的下一个 div 元素" id="btn3" />
		<input type="button" value="选择 id 为 two 的元素后面的所有 div 兄弟元素" id="btn4" />
		<br><br>
		<div class="one" id="one">
			id 为 one,class 为 one 的div
			<div class="mini">class为mini</div>
		</div>
		<div class="one" id="two" title="test">
			id为two,class为one,title为test的div
			<div class="mini" title="other">class为mini,title为other</div>
			<div class="mini" title="test">class为mini,title为test</div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini"></div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini" title="tesst">class为mini,title为tesst</div>
		</div>
		<div style="display:none;" class="none">style的display为"none"的div</div>
		<div class="hide">class为"hide"的div</div>
		<div>
			包含input的type为"hidden"的div<input type="hidden" size="8">
		</div>
		<span id="span">^^span元素^^</span>
	</body>
</html>
```

## 3、过滤选择器

### 1、基本过滤器

| 过滤器                                 | 介绍                     |
| ----------------------------------- | ---------------------- |
| <font color="red">:first</font>     | 获取第一个元素                |
| <font color="red">:last</font>      | 获取最后个元素                |
| :not(selector)                      | 去除所有与给定选择器匹配的元素        |
| :even                               | 匹配所有索引值为偶数的元素，从 0 开始计数 |
| :odd                                | 匹配所有索引值为奇数的元素，从 0 开始计数 |
| <font color="red">:eq(index)</font> | 匹配一个给定索引值的元素           |
| :gt(index)                          | 匹配所有大于给定索引值的元素         |
| :lt(index)                          | 匹配所有小于给定索引值的元素         |
| :header                             | 匹配如 h1, h2, h3 之类的标题元素 |
| :animated                           | 匹配所有正在执行动画效果的元素        |

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Untitled Document</title>
		<style type="text/css">
			div, span, p {
				width: 140px;
				height: 140px;
				margin: 5px;
				background: #aaa;
				border: #000 1px solid;
				float: left;
				font-size: 17px;
				font-family: Verdana;
			}

			div.mini {
				width: 55px;
				height: 55px;
				background-color: #aaa;
				font-size: 12px;
			}

			div.hide {
				display: none;
			}
		</style>
		<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
		<script type="text/javascript">
			// 网页全部加载完之后，会执行里面的操作
			// 与 $(function () {});相同
			$(document).ready(function(){
				function anmateIt(){
					$("#mover").slideToggle("slow", anmateIt);
				}
				anmateIt();
			});

			$(document).ready(function(){
				// 给 id 为 #btn1 的标签设定单击事件
				//1.选择第一个 div 元素
				$("#btn1").click(function(){
					$("div:first").css("background", "#bbffaa");
				});

				//2.选择最后一个 div 元素
				$("#btn2").click(function(){
					$("div:last").css("background", "#bbffaa");
				});

				//3.选择class不为 one 的所有 div 元素
				$("#btn3").click(function(){
					$("div:not(.one)").css("background", "#bbffaa");
				});

				//4.选择索引值为偶数的 div 元素
				$("#btn4").click(function(){
					$("div:even").css("background", "#bbffaa");
				});

				//5.选择索引值为奇数的 div 元素
				$("#btn5").click(function(){
					$("div:odd").css("background", "#bbffaa");
				});

				//6.选择索引值为大于 3 的 div 元素
				$("#btn6").click(function(){
					$("div:gt(3)").css("background", "#bbffaa");
				});

				//7.选择索引值为等于 3 的 div 元素
				$("#btn7").click(function(){
					$("div:eq(3)").css("background", "#bbffaa");
				});

				//8.选择索引值为小于 3 的 div 元素
				$("#btn8").click(function(){
					$("div:lt(3)").css("background", "#bbffaa");
				});

				//9.选择所有的标题元素
				$("#btn9").click(function(){
					$(":header").css("background", "#bbffaa");
				});

				//10.选择当前正在执行动画的所有元素
				$("#btn10").click(function(){
					$(":animated").css("background", "#bbffaa");
				});
				//11.选择没有执行动画的最后一个div
				$("#btn11").click(function(){
					$("div:not(:animated):last").css("background", "#bbffaa");
				});
			});
		</script>
	</head>
	<body>
		<input type="button" value="选择第一个 div 元素" id="btn1" />
		<input type="button" value="选择最后一个 div 元素" id="btn2" />
		<input type="button" value="选择class不为 one 的所有 div 元素" id="btn3" />
		<input type="button" value="选择索引值为偶数的 div 元素" id="btn4" />
		<input type="button" value="选择索引值为奇数的 div 元素" id="btn5" />
		<input type="button" value="选择索引值为大于 3 的 div 元素" id="btn6" />
		<input type="button" value="选择索引值为等于 3 的 div 元素" id="btn7" />
		<input type="button" value="选择索引值为小于 3 的 div 元素" id="btn8" />
		<input type="button" value="选择所有的标题元素" id="btn9" />
		<input type="button" value="选择当前正在执行动画的所有元素" id="btn10" />
		<input type="button" value="选择没有执行动画的最后一个div" id="btn11" />


		<h3>基本选择器.</h3>
		<br><br>
		<div class="one" id="one">
			id 为 one,class 为 one 的div
			<div class="mini">class为mini</div>
		</div>
		<div class="one" id="two" title="test">
			id为two,class为one,title为test的div
			<div class="mini" title="other">class为mini,title为other</div>
			<div class="mini" title="test">class为mini,title为test</div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini"></div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini" title="tesst">class为mini,title为tesst</div>
		</div>
		<div style="display:none;" class="none">style的display为"none"的div</div>
		<div class="hide">class为"hide"的div</div>
		<div>
			包含input的type为"hidden"的div<input type="hidden" size="8">
		</div>
		<div id="mover">正在执行动画的div元素.</div>
	</body>
</html>
```

### 2、内容过滤器

|过滤器|介绍|
|--|--|
|:contains(text)|匹配包含给定文本的元素|
|:empty|匹配所有不包含子元素或者文本的空元素|
|:has(selector)|匹配含有选择器所匹配的元素的元素|
|:parent|匹配含有子元素或者文本的元素|

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Untitled Document</title>
		<style type="text/css">
			div, span, p {
				width: 140px;
				height: 140px;
				margin: 5px;
				background: #aaa;
				border: #000 1px solid;
				float: left;
				font-size: 17px;
				font-family: Verdana;
			}
			
			div.mini {
				width: 55px;
				height: 55px;
				background-color: #aaa;
				font-size: 12px;
			}
			
			div.hide {
				display: none;
			}			
		</style>
		<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
		<script type="text/javascript">
			$(document).ready(function(){
				function anmateIt(){
					$("#mover").slideToggle("slow", anmateIt);
				}
	
				anmateIt();				
			});
			
			/** 
			:contains(text)   
			:empty 			  
			:has(selector) 	
			:parent 			
			*/
		   // 网页全部加载完之后，会执行里面的操作
		   // 与 $(function () {});相同
			$(document).ready(function(){
				// 给 id 为 #btn1 的标签设定单击事件
				//1.选择 含有文本 'di' 的 div 元素
				$("#btn1").click(function(){
					$("div:contains('di')").css("background", "#bbffaa");
				});

				//2.选择不包含子元素(或者文本元素) 的 div 空元素
				$("#btn2").click(function(){
					$("div:empty").css("background", "#bbffaa");
				});

				//3.选择含有 class 为 mini 元素的 div 元素
				$("#btn3").click(function(){
					$("div:has(.mini)").css("background", "#bbffaa");
				});

				//4.选择含有子元素(或者文本元素)的div元素
				$("#btn4").click(function(){
					$("div:parent").css("background", "#bbffaa");
				});
			});
		</script>
	</head>
	<body>		
		<input type="button" value="选择 含有文本 'di' 的 div 元素" id="btn1" />
		<input type="button" value="选择不包含子元素(或者文本元素) 的 div 空元素" id="btn2" />
		<input type="button" value="选择含有 class 为 mini 元素的 div 元素" id="btn3" />
		<input type="button" value="选择含有子元素(或者文本元素)的div元素" id="btn4" />
		
		<br><br>
		<div class="one" id="one">
			id 为 one,class 为 one 的div
			<div class="mini">class为mini</div>
		</div>
		<div class="one" id="two" title="test">
			id为two,class为one,title为test的div
			<div class="mini" title="other">class为mini,title为other</div>
			<div class="mini" title="test">class为mini,title为test</div>
		</div>/
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini"></div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini" title="tesst">class为mini,title为tesst</div>
		</div>
		<div style="display:none;" class="none">style的display为"none"的div</div>
		<div class="hide">class为"hide"的div</div>
		<div>
			包含input的type为"hidden"的div<input type="hidden" size="8">
		</div>
		<div id="mover">正在执行动画的div元素.</div>
	</body>
</html>
```

### 3、属性过滤器

| 过滤器                              | 介绍                                        |
| -------------------------------- | ----------------------------------------- |
| `[attribute]`                    | <font color="red">匹配包含给定属性的元素。</font>     |
| `[attribute=value]`              | <font color="red">匹配给定的属性是某个特定值的元素</font> |
| `[attribute!=value]`             | 匹配所有不含有指定的属性，或者属性不等于特定值的元素。               |
| `[attribute^=value]`             | 匹配给定的属性是以某些值开始的元素                         |
| `[attribute$=value]`             | 匹配给定的属性是以某些值结尾的元素                         |
| `[attribute*=value]`             | 匹配给定的属性是以包含某些值的元素                         |
| `[attrSel1][attrSel2][attrSelN]` | 复合属性选择器，需要同时满足多个条件时使用。                    |

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Untitled Document</title>
<style type="text/css">
div,span,p {
	width: 140px;
	height: 140px;
	margin: 5px;
	background: #aaa;
	border: #000 1px solid;
	float: left;
	font-size: 17px;
	font-family: Verdana;
}

div.mini {
	width: 55px;
	height: 55px;
	background-color: #aaa;
	font-size: 12px;
}

div.hide {
	display: none;
}
</style>
<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
<script type="text/javascript">
	/**
	[attribute] 			
	[attribute=value] 		
	[attribute!=value] 		 
	[attribute^=value] 		
	[attribute$=value] 		
	[attribute*=value] 		
	[attrSel1][attrSel2][attrSelN]
	*/
   // 网页全部加载完之后，会执行里面的操作
	$(function() {
		// 给 id 为 #btn1 的标签设定单击事件
		//1.选取含有 属性title 的div元素
		$("#btn1").click(function() {
			$("div[title]").css("background", "#bbffaa");
		});
		//2.选取 属性title值等于'test'的div元素
		$("#btn2").click(function() {
			$("div[title='test']").css("background", "#bbffaa");
		});
		//3.选取 属性title值不等于'test'的div元素(*没有属性title的也将被选中)
		$("#btn3").click(function() {
			$("div[title!='test']").css("background", "#bbffaa");
		});
		//4.选取 属性title值 以'te'开始 的div元素
		$("#btn4").click(function() {
			$("div[title^='te']").css("background", "#bbffaa");
		});
		//5.选取 属性title值 以'est'结束 的div元素
		$("#btn5").click(function() {
			$("div[title$='est']").css("background", "#bbffaa");
		});
		//6.选取 属性title值 含有'es'的div元素
		$("#btn6").click(function() {
			$("div[title*='es']").css("background", "#bbffaa");
		});
		
		//7.首先选取有属性id的div元素，然后在结果中 选取属性title值 含有'es'的 div 元素
		$("#btn7").click(function() {
			$("div[id][title*='es']").css("background", "#bbffaa");
		});
		//8.选取 含有 title 属性值, 且title 属性值不等于 test 的 div 元素
		$("#btn8").click(function() {
			$("div[title][title!='test']").css("background", "#bbffaa");
		});
	});
</script>
</head>
<body>
	<input type="button" value="选取含有 属性title 的div元素." id="btn1" />
	<input type="button" value="选取 属性title值等于'test'的div元素." id="btn2" />
	<input type="button"
		value="选取 属性title值不等于'test'的div元素(没有属性title的也将被选中)." id="btn3" />
	<input type="button" value="选取 属性title值 以'te'开始 的div元素." id="btn4" />
	<input type="button" value="选取 属性title值 以'est'结束 的div元素." id="btn5" />
	<input type="button" value="选取 属性title值 含有'es'的div元素." id="btn6" />
	<input type="button"
		value="组合属性选择器,首先选取有属性id的div元素，然后在结果中 选取属性title值 含有'es'的 div 元素."
		id="btn7" />
	<input type="button"
		value="选取 含有 title 属性值, 且title 属性值不等于 test 的 div 元素." id="btn8" />

	<br>
	<br>
	<div class="one" id="one">
		id 为 one,class 为 one 的div
		<div class="mini">class为mini</div>
	</div>
	<div class="one" id="two" title="test">
		id为two,class为one,title为test的div
		<div class="mini" title="other">class为mini,title为other</div>
		<div class="mini" title="test">class为mini,title为test</div>
	</div>
	<div class="one">
		<div class="mini">class为mini</div>
		<div class="mini">class为mini</div>
		<div class="mini">class为mini</div>
		<div class="mini"></div>
	</div>
	<div class="one">
		<div class="mini">class为mini</div>
		<div class="mini">class为mini</div>
		<div class="mini">class为mini</div>
		<div class="mini" title="tesst">class为mini,title为tesst</div>
	</div>
	<div style="display: none;" class="none">style的display为"none"的div</div>
	<div class="hide">class为"hide"的div</div>
	<div>
		包含input的type为"hidden"的div<input type="hidden" value="123456789"
			size="8">
	</div>
	<div id="mover">正在执行动画的div元素.</div>
</body>
</html>
```

### 4、表单过滤器

|过滤器|介绍|
|--|--|
|:input|匹配所有 input, textarea, select 和 button 元素|
|<font color="red">:text</font>|匹配所有 文本输入框|
|<font color="red">:password</font>|匹配所有的密码输入框|
|<font color="red">:radio</font>|匹配所有的单选框|
|<font color="red">:checkbox</font>|匹配所有的复选框|
|:submit|匹配所有提交按钮|
|:image|匹配所有 img 标签|
|:reset|匹配所有重置按钮|
|:button|匹配所有 input type=button < button >按钮|
|:file|匹配所有 input type=file 文件上传|
|:hidden|匹配所有不可见元素 display:none 或 input type=hidden|
|:enabled|匹配所有可用元素|
|:disabled|匹配所有不可用元素|
|<font color="red">:checked</font>|<font color="red">匹配所有选中的单选，复选，和下拉列表中选中的 option 标签对象</font>|
|<font color="red">:selected</font>|<font color="red">匹配所有选中的 optio</font>|

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Untitled Document</title>
	<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		// 网页全部加载完之后，会执行里面的操作
		$(function () {
			/**
			:input 		
			:text 		
			:password 	
			:radio 		
			:checkbox 	
			:submit 	
			:image 		
			:reset 		
			:button 	
			:file 		
			:hidden 	
			
			表单对象的属性
			:enabled 		
			:disabled 		
			:checked 		
			:selected 		
			*/

			// 给 id 为 #btn1 的标签设定单击事件
			//1.对表单内 可用input 赋值操作
			$("#btn1").click(function () {
				// val()可以操作表单项的value属性值
				// 它可以设置和获取
				$(":text:enabled").val("我是万能的程序员");
			});

			//2.对表单内 不可用input 赋值操作
			$("#btn2").click(function () {
				$(":text:disabled").val("管你可用不可用，反正我是万能的程序员");
			});

			//3.获取多选框选中的个数  使用size()方法获取选取到的元素集合的元素个数
			$("#btn3").click(function () {
				alert($(":checkbox:checked").length);
			});

			//4.获取多选框，每个选中的value值
			$("#btn4").click(function () {
				// 获取全部选中的复选框标签对象
				var $checkboies = $(":checkbox:checked");
				// 老式遍历
				// for (var i = 0; i < $checkboies.length; i++){
				// 	alert( $checkboies[i].value );
				// }

				// each方法是jQuery对象提供用来遍历元素的方法
				// 在遍历的function函数中，有一个this对象，这个this对象，就是当前遍历到的dom对象
				$checkboies.each(function () {
					alert(this.value);
				});
			});

			//5.获取下拉框选中的内容  
			$("#btn5").click(function () {
				// 获取选中的option标签对象
				var $options = $("select option:selected");
				// 遍历，获取option标签中的文本内容
				$options.each(function () {
					// 在each遍历的function函数中，有一个this对象。这个this对象是当前正在遍历到的dom对象
					alert(this.innerHTML);
				});
			});
		})
	</script>
</head>

<body>
	<h3>表单对象属性过滤选择器</h3>
	<button id="btn1">对表单内 可用input 赋值操作.</button>
	<button id="btn2">对表单内 不可用input 赋值操作.</button><br /><br />
	<button id="btn3">获取多选框选中的个数.</button>
	<button id="btn4">获取多选框选中的内容.</button><br /><br />
	<button id="btn5">获取下拉框选中的内容.</button><br /><br />

	<form id="form1" action="#">
		可用元素: <input name="add" value="可用文本框1" /><br>
		不可用元素: <input name="email" disabled="disabled" value="不可用文本框" /><br>
		可用元素: <input name="che" value="可用文本框2" /><br>
		不可用元素: <input name="name" disabled="disabled" value="不可用文本框" /><br>
		<br>

		多选框: <br>
		<input type="checkbox" name="newsletter" checked="checked" value="test1" />test1
		<input type="checkbox" name="newsletter" value="test2" />test2
		<input type="checkbox" name="newsletter" value="test3" />test3
		<input type="checkbox" name="newsletter" checked="checked" value="test4" />test4
		<input type="checkbox" name="newsletter" value="test5" />test5

		<br><br>
		下拉列表1: <br>
		<!-- multiple="multiple"：可以多选，按住ctrl或shift选择 -->
		<select name="test" multiple="multiple" style="height: 100px" id="sele1">
			<option>浙江</option>
			<option selected="selected">辽宁</option>
			<option>北京</option>
			<option selected="selected">天津</option>
			<option>广州</option>
			<option>湖北</option>
		</select>

		<br><br>
		下拉列表2: <br>
		<select name="test2">
			<option>浙江</option>
			<option>辽宁</option>
			<option selected="selected">北京</option>
			<option>天津</option>
			<option>广州</option>
			<option>湖北</option>
		</select>
	</form>
</body>

</html>
```

# 六、jQuery 常用的元素筛选

|元素筛选|介绍|
|--|--|
|eq()|获取给定索引的元素 功能跟 :eq() 一样|
|first()|获取第一个元素 功能跟 :first 一样|
|last()|获取最后一个元素 功能跟 :last 一样|
|filter(exp)|留下匹配的元素|
|is(exp)|判断是否匹配给定的选择器，只要有一个匹配就返回，true|
|has(exp)|返回包含有匹配选择器的元素的元素 功能跟 :has 一样|
|not(exp)|删除匹配选择器的元素 功能跟 :not 一样|
|children(exp)|返回匹配给定选择器的子元素 功能跟 parent>child 一样|
|find(exp)|返回匹配给定选择器的后代元素 功能跟 ancestor descendant 一样|
|next()|返回当前元素的下一个兄弟元素 功能跟 prev + next 功能一样|
|nextAll()|返回当前元素后面所有的兄弟元素 功能跟 prev ~ siblings 功能一样|
|nextUntil()|返回当前元素到指定匹配的元素为止的后面元素|
|parent()|返回父元素|
|prev(exp)|返回当前元素的上一个兄弟元素|
|prevAll()|返回当前元素前面所有的兄弟元素|
|prevUnit(exp)|返回当前元素到指定匹配的元素为止的前面元素|
|siblings(exp)|返回所有兄弟元素|
|add()|把 add 匹配的选择器的元素添加到当前 jquery 对象|

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>DOM查询</title>
		<style type="text/css">
			div, span, p {
				width: 140px;
				height: 140px;
				margin: 5px;
				background: #aaa;
				border: #000 1px solid;
				float: left;
				font-size: 17px;
				font-family: Verdana;
			}
			
			div.mini {
				width: 55px;
				height: 55px;
				background-color: #aaa;
				font-size: 12px;
			}
			
			div.hide {
				display: none;
			}			
		</style>
		<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
		<script type="text/javascript">
			// 网页全部加载完之后，会执行里面的操作
			$(document).ready(function(){
				function anmateIt(){
					$("#mover").slideToggle("slow", anmateIt);
				}
				anmateIt();
				
				/**
								
				过滤
				eq(index|-index) 			
				first() 					
				last() 						
				hasClass(class) 			
				filter(expr|obj|ele|fn) 	
				is(expr|obj|ele|fn)1.6* 	
				has(expr|ele) 				
				not(expr|ele|fn) 			
				slice(start,[end]) 			
				
				查找
				children([expr]) 			
				closest(expr,[con]|obj|ele)1.6*   
				find(expr|obj|ele) 				
				next([expr]) 					
				nextall([expr]) 				
				nextUntil([exp|ele][,fil])1.6* 	
				parent([expr]) 					
				parents([expr]) 				
				parentsUntil([exp|ele][,fil])1.6*  
				prev([expr]) 					
				prevall([expr]) 				
				prevUntil([exp|ele][,fil])1.6* 	
				siblings([expr]) 				
				
				串联
				add(expr|ele|html|obj[,con])
				
				*/
				
				// 给 id 为 #btn1 的标签设定单击事件
				//(1)eq()  选择索引值为等于 3 的 div 元素
				$("#btn1").click(function(){
					$("div").eq(3).css("background-color","#bfa");
				});
				//(2)first()选择第一个 div 元素
				$("#btn2").click(function(){
					//first()   选取第一个元素
					$("div").first().css("background-color","#bfa");
				});
				//(3)last()选择最后一个 div 元素
				$("#btn3").click(function(){
					//last()  选取最后一个元素
					$("div").last().css("background-color","#bfa");
				});
				//(4)filter()在div中选择索引为偶数的
				$("#btn4").click(function(){
					//filter()  过滤   传入的是选择器字符串
					$("div").filter(":even").css("background-color","#bfa");
				});
				//(5)is()判断#one是否为:empty或:parent
				//is用来检测jq对象是否符合指定的选择器
				$("#btn5").click(function(){
					alert( $("#one").is(":empty") );
				});
				
				//(6)has()选择div中包含.mini的
				$("#btn6").click(function(){
					//has(selector)  选择器字符串    是否包含selector
					$("div").has(".mini").css("background-color","#bfa");
				});
				//(7)not()选择div中class不为one的
				$("#btn7").click(function(){
					//not(selector)  选择不是selector的元素
					$("div").not('.one').css("background-color","#bfa");
				});
				//(8)children()在body中选择所有class为one的div子元素
				$("#btn8").click(function(){
					//children()  选出所有的子元素
					$("body").children("div.one").css("background-color","#bfa");
				});
				
				//(9)find()在body中选择所有class为mini的div元素
				$("#btn9").click(function(){
					//find()  选出所有的后代元素
					$("body").find("div.mini").css("background-color","#bfa");
				});
				//(10)next() #one的下一个div
				$("#btn10").click(function(){
					//next()  选择下一个兄弟元素
					$("#one").next("div").css("background-color","#bfa");
				});
				//(11)nextAll() #one后面所有的span元素
				$("#btn11").click(function(){
					//nextAll()   选出后面所有的元素
					$("#one").nextAll("span").css("background-color","#bfa");
				});
				//(12)nextUntil() #one和span之间的元素
				$("#btn12").click(function(){
					//
					$("#one").nextUntil("span").css("background-color","#bfa")
				});
				//(13)parent() .mini的父元素
				$("#btn13").click(function(){
					$(".mini").parent().css("background-color","#bfa");
				});
				//(14)prev() #two的上一个div
				$("#btn14").click(function(){
					//prev()  
					$("#two").prev("div").css("background-color","#bfa")
				});
				//(15)prevAll() span前面所有的div
				$("#btn15").click(function(){
					//prevAll()   选出前面所有的元素
					$("span").prevAll("div").css("background-color","#bfa")
				});
				//(16)prevUntil() span向前直到#one的元素
				$("#btn16").click(function(){
					//prevUntil(exp)   找到之前所有的兄弟元素直到找到exp停止
					$("span").prevUntil("#one").css("background-color","#bfa")
				});
				//(17)siblings() #two的所有兄弟元素
				$("#btn17").click(function(){
					//siblings()    找到所有的兄弟元素，包括前面的和后面的
					$("#two").siblings().css("background-color","#bfa")
				});
				
				//(18)add()选择所有的 span 元素和id为two的元素
				$("#btn18").click(function(){
	
					//   $("span,#two,.mini,#one")
					$("span").add("#two").add("#one").css("background-color","#bfa");
					
				});
				


			});
			
		</script>
	</head>
	<body>		
		<input type="button" value="eq()选择索引值为等于 3 的 div 元素" id="btn1" />
		<input type="button" value="first()选择第一个 div 元素" id="btn2" />
		<input type="button" value="last()选择最后一个 div 元素" id="btn3" />
		<input type="button" value="filter()在div中选择索引为偶数的" id="btn4" />
		<input type="button" value="is()判断#one是否为:empty或:parent" id="btn5" />
		<input type="button" value="has()选择div中包含.mini的" id="btn6" />
		<input type="button" value="not()选择div中class不为one的" id="btn7" />
		<input type="button" value="children()在body中选择所有class为one的div子元素" id="btn8" />
		<input type="button" value="find()在body中选择所有class为mini的div后代元素" id="btn9" />
		<input type="button" value="next()#one的下一个div" id="btn10" />
		<input type="button" value="nextAll()#one后面所有的span元素" id="btn11" />
		<input type="button" value="nextUntil()#one和span之间的元素" id="btn12" />
		<input type="button" value="parent().mini的父元素" id="btn13" />
		<input type="button" value="prev()#two的上一个div" id="btn14" />
		<input type="button" value="prevAll()span前面所有的div" id="btn15" />
		<input type="button" value="prevUntil()span向前直到#one的元素" id="btn16" />
		<input type="button" value="siblings()#two的所有兄弟元素" id="btn17" />
		<input type="button" value="add()选择所有的 span 元素和id为two的元素" id="btn18" />

		
		<h3>基本选择器.</h3>
		<br /><br />
		文本框<input type="text" name="account" disabled="disabled" />
		<br><br>
		<div class="one" id="one">
			id 为 one,class 为 one 的div
			<div class="mini">class为mini</div>
		</div>
		<div class="one" id="two" title="test">
			id为two,class为one,title为test的div
			<div class="mini" title="other"><b>class为mini,title为other</b></div>
			<div class="mini" title="test">class为mini,title为test</div>
		</div>
		
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini"></div>
		</div>
		<div class="one">
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini">class为mini</div>
			<div class="mini" title="tesst">class为mini,title为tesst</div>
		</div>
		<div style="display:none;" class="none">style的display为"none"的div</div>
		<div class="hide">class为"hide"的div</div>
		<span id="span1">^^span元素 111^^</span>
		<div>
			包含input的type为"hidden"的div<input type="hidden" size="8">
		</div>
		<span id="span2">^^span元素 222^^</span>
		<div id="mover">正在执行动画的div元素.</div>
	</body>
</html>
```

# 七、jQuery 的属性操作

- 不传参数是获取，传递参数是设置
- 固有属性用prop，不是固有属性用attr

|jQuery属性|介绍|
|--|--|
|html()|它可以设置和获取起始标签和结束标签中的内容。 跟 dom 属性 innerHTML 一样|
|text()|它可以设置和获取起始标签和结束标签中的文本。 跟 dom 属性 innerText 一样|
|val()|它可以设置和获取<font color="red">表单项</font>的 value 属性值。 跟 dom 属性 value 一样|
|attr()|可以设置和获取属性的值，不推荐操作 checked、readOnly、selected、disabled 等等。attr 方法还可以操作非标准的属性。比如自定义属性：abc,bbj|
|prop()|可以设置和获取属性的值,只推荐操作 checked、readOnly、selected、disabled 等等|

```html 
<!DOCTYPE html>
<html lang="zh_CN">

<head>
	<meta charset="UTF-8">
	<title>Title</title>
	<script type="text/javascript" src="../script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		// 网页全部加载完之后，会执行里面的操作
		$(function () {

			$("#btn0").click(function(){
				// 不传参数是获取，传递参数是设置
				// 弹窗显示 id 为 username 的标签中的内容
				alert($("#username").val());
				// 将 id 为 username 的标签中的内容改为：
				$("#username").val("月海可爱")
			});

			$("#btn1").click(function(){
				// 不传参数是获取，传递参数是设置
				// 弹窗显示body标签中的内容
				alert($("body").html());
				// 将body标签中的内容改为：
				$("body").html("月海")
			});

			$("#btn2").click(function(){
				// 不传参数是获取，传递参数是设置
				// 弹窗显示 id 为 mul1 的标签中的内容
				alert($("#mul1").text());
				// 将 id 为 mul1 的标签中的内容改为：
				$("#mul1").text("月海")
			});

			// 固有属性用prop，不是固有属性用attr
			$("#btn3").click(function(){
				// 不传参数是获取，传递参数是设置
				// 弹窗显示 type 为 checkbox 的第一个元素(:first)的name属性的值
				alert($(":checkbox:first").attr("name"));
				// 将 type 为 checkbox 的第一个元素(:first)的name属性的值改为：
				$(":checkbox:first").attr("name","月海")
			});

			// 固有属性用prop，不是固有属性用attr
			$("#btn4").click(function(){
				// 不传参数是获取，传递参数是设置
				// 弹窗显示 type 为 checkbox 的value属性的值
				alert($(":checkbox").attr("value"));
				// 将 type 为 checkbox 的 value 属性的值改为：
				$(":checkbox").prop("value","月海")
				// 多选框全选
				$(":checkbox").prop("checked",true);
				// 多选框全不选
				$(":checkbox").prop("checked",false);
			});

			$("#btn5").click(function(){
				// 多选框全选
				$(":checkbox").prop("checked",true);
			});
			$("#btn6").click(function(){
				// 多选框全不选
				$(":checkbox").prop("checked",false);
			});

		});
	</script>
</head>

<body>

	<body>
		请输入：
		<input type="text" id="username" name="username" value="月海" />
		<button id="btn0" >显示输入文字</button>
		<br />
		单选：
		<input name="radio" type="radio" value="radio1" />radio1
		<input name="radio" type="radio" value="radio2" />radio2
		<br />
		多选：
		<input name="checkbox" type="checkbox" value="checkbox1" />checkbox1
		<input name="checkbox" type="checkbox" value="checkbox2" />checkbox2
		<input name="checkbox" type="checkbox" value="checkbox3" />checkbox3
		<br />
		下拉多选 ：
		<select id="multiple" multiple="multiple" size="4">
			<option value="mul1" id="mul1">mul1</option>
			<option value="mul2" name="mul2" >mul2</option>
			<option value="mul3">mul3</option>
			<option value="mul4">mul4</option>
		</select>
		<br />
		下拉单选 ：
		<select id="single">
			<option value="sin1">sin1</option>
			<option value="sin2">sin2</option>
			<option value="sin3">sin3</option>
		</select>
		<br />
		<button id="btn1" >按钮1</button>
		<button id="btn2" >按钮2</button>
		<button id="btn3" >按钮3</button>
		<button id="btn4" >按钮4</button>
		<button id="btn5" >多选框全选</button>
		<button id="btn6" >多选框全不选</button>
	</body>
</body>

</html>
```

# 八、DOM 的增删改

|方法|使用演示|介绍|
|--|--|--|
|<font color="red">**内部插入：**</font>|||
|appendTo()|a.appendTo(b)|把 a 插入到 b 子元素末尾，成为最后一个子元素|
|prependTo()|a.prependTo(b)|把 a 插到 b 所有子元素前面，成为第一个子元素|
|<font color="red">**外部插入：**</font>|||
|insertAfter()|a.insertAfter(b)|得到 ba|
|insertBefore()|a.insertBefore(b)|得到 ab|
|<font color="red">**替换:**</font>|||
|replaceWith()|a.replaceWith(b)|用 b 替换掉 a|
|replaceAll()|a.replaceAll(b)|用 a 替换掉所有 b|
|<font color="red">**删除：**</font>|||
|remove()|a.remove();|删除 a 标签|
|empty()|a.empty();|清空 a 标签里的内容|

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>测试</title>

	<style type="text/css">
		div, span, p {
			width: 200px;
			height: 200px;
			margin: 5px;
			background: #aaa;
			border: #000 1px solid;
			float: left;
			font-size: 17px;
			font-family: Verdana;
		}
	</style>

	<script type="text/javascript" src="../save/script/jquery-1.7.2.js"></script>

	<script type="text/javascript">
		// 网页全部加载完之后，会执行里面的操作
		$(function(){

			// 内部插入
			// 在每个 div 内部的最末尾插入：<h1>末尾插入</h1>
			$("<h1>末尾插入</h1>").appendTo("div");

			// 在每个 div 内部的最前面插入：<h1>前面插入</h1>
			$("<h2>前面插入</h2>").prependTo("div");

			// 外部插入
			// 在每个 div 外部后面插入：<h1>外部后面插入</h1>
			$("<h1>外部后面插入</h1>").insertAfter("div");

			// 在每个 div 外部前面插入：<h1>外部前面插入</h1>
			$("<h2>外部前面插入</h2>").insertBefore("div");

			// 替换
			// 将 每个 div 标签替换为：<h1>替换</h1>
			// $("div").replaceWith("<h1>替换</h1>");

			// 将 每个 div 标签替换为：<h1>替换</h1>
			// $("<h2>替换</h2>").replaceAll("div");

			// 删除
			// 删除 h1 标签
			$("h1").remove();
			// 删除 div 标签里的内容
			$("div").empty();

		});

	</script>

</head>

<body>

	<div>div1</div>
	<div>div2</div>

</body>

</html>
```

# 九、jQuery 练习

## 1、全选、反选、全部选

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="../../script/jquery-1.7.2.js"></script>
<script type="text/javascript">
	// 网页全部加载完之后，会执行里面的操作
	$(function(){
		// 给全选按钮绑定单击事件
		$("#checkedAllBtn").click(function(){
			// 将 type 为 checkbox 的多选框设置为已选择
			$(":checkbox").prop("checked",true);
		});

		// 给全不选按钮绑定单击事件
		$("#checkedNoBtn").click(function(){
			// 将 type 为 checkbox 的多选框设置为未选择
			$(":checkbox").prop("checked",false);
		});

		// 给反选按钮绑定单击事件
		$("#checkedRevBtn").click(function(){
			// 将 type 为 checkbox 且属性 name 的值为 items 的多选框设置为反选
			// each()：循环遍历
			// :checkbox[name='items']：过滤器，type 为 checkbox 且属性 name 的值为 items
			$(":checkbox[name='items']").each(function(){
				// this.checked：当前遍历到的checked属性的值
				this.checked = !this.checked;
			});

			// 检查是否全选，若是全选，则自动选定【全选/全不选】按钮
			// 获取全部的球类个数
			var allCount = $(":checkbox[name='items']").length;
			// 再获取选中的球类的个数
			// :checkbox[name='items']:checked
			//  type 为 checkbox 且属性 name 的值为 items 的 checked 的值
			var checkedCount = $(":checkbox[name='items']:checked").length;

			// 方式一：
			// if(allCount == checkedCount){
			// 	$("#checkedAllBox").prop("checked",true);
			// }else{
			// 	$("#checkedAllBox").prop("checked",false);
			// }

			// 方式二：
			$("#checkedAllBox").prop("checked",allCount == checkedCount);

		});

		// 给提交按钮绑定单击事件
		// 弹窗提示选定的内容
		$("#sendBtn").click(function(){
			// :checkbox[name='items']:checked
			//  type 为 checkbox 且属性 name 的值为 items 的 checked 的值
			// 故，是循环多选框中，已选定的值
			$(":checkbox[name='items']:checked").each(function(){
				alert(this.value);
			});
		});

		// 给【全选/全不选】绑定单击事件
		$("#checkedAllBox").click(function(){
			// :checkbox[name='items']
			//  type 为 checkbox 且属性 name 的值为 items 的 checked 都改为，checkedAllBox 的 checked 的值
			$(":checkbox[name='items']").prop("checked",this.checked);
		});

		// 检查是否全选，若是全选，则自动选定【全选/全不选】按钮，否则取消选定
		// 给全部球类绑定单击事件，同步给【全选/全不选】按钮
		$(":checkbox[name='items']").click(function(){
			// 获取全部的球类个数
			var allCount = $(":checkbox[name='items']").length;
			// 再获取选中的球类的个数
			// :checkbox[name='items']:checked
			//  type 为 checkbox 且属性 name 的值为 items 的 checked 的值
			var checkedCount = $(":checkbox[name='items']:checked").length;

			// 方式一：
			// if(allCount == checkedCount){
			// 	$("#checkedAllBox").prop("checked",true);
			// }else{
			// 	$("#checkedAllBox").prop("checked",false);
			// }

			// 方式二：
			$("#checkedAllBox").prop("checked",allCount == checkedCount);
		});

	});
	
</script>
</head>
<body>

	<form method="post" action="">
	
		你爱好的运动是？<input type="checkbox" id="checkedAllBox" />全选/全不选
		
		<br />
		<input type="checkbox" name="items" value="足球" />足球
		<input type="checkbox" name="items" value="篮球" />篮球
		<input type="checkbox" name="items" value="羽毛球" />羽毛球
		<!-- checked="true"：默认选中 -->
		<input type="checkbox" name="items" value="乒乓球" checked="true" />乒乓球
		<br />
		<input type="button" id="checkedAllBtn" value="全　选" />
		<input type="button" id="checkedNoBtn" value="全不选" />
		<input type="button" id="checkedRevBtn" value="反　选" />
		<input type="button" id="sendBtn" value="提　交" />
	</form>

</body>
</html>
```

## 2、从左到右、从右到左

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
	<style type="text/css">
		select {
			width: 100px;
			height: 140px;
		}
		
		div {
			width: 130px;
			float: left;
			text-align: center;
		}
	</style>
	<script type="text/javascript" src="script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		
		// 网页全部加载完之后，会执行里面的操作
		$(function(){

			// 给【选中添加到右边】按钮设置单击事件
			// button:eq(0)：第1个button
			$("button:eq(0)").click(function(){
				// 将第1个select标签中的option标签中选中的（selected）元素，插入到第2个select标签中
				$("select:eq(0) option:selected").appendTo($("select:eq(1)"));
			});

			// 给【全部添加到右边】按钮设置单击事件
			// button:eq(1)：第2个button
			$("button:eq(1)").click(function(){
				// 将第1个select标签中的option标签，插入到第2个select标签中
				$("select:eq(0) option").appendTo($("select:eq(1)"));
			});

			// 给【选中删除到左边】按钮设置单击事件
			// button:eq(2)：第3个button
			$("button:eq(2)").click(function(){
				// 将第2个select标签中的option标签中选中的（selected）元素，插入到第1个select标签中
				$("select:eq(1) option:selected").appendTo($("select:eq(0)"));
			});

			// 给【选中添加到右边】按钮设置单击事件
			// button:eq(3)：第4个button
			$("button:eq(3)").click(function(){
				// 将第2个select标签中的option标签，插入到第1个select标签中
				$("select:eq(1) option").appendTo($("select:eq(0)"));
			});


		});
	
	</script>
</head>
<body>

	<div id="left">
		<select multiple="multiple" name="sel01">
			<option value="opt01">选项1</option>
			<option value="opt02">选项2</option>
			<option value="opt03">选项3</option>
			<option value="opt04">选项4</option>
			<option value="opt05">选项5</option>
			<option value="opt06">选项6</option>
			<option value="opt07">选项7</option>
			<option value="opt08">选项8</option>
		</select>
		
		<button>选中添加到右边</button>
		<button>全部添加到右边</button>
	</div>
	<div id="rigth">
		<select multiple="multiple" name="sel02">
		</select>
		<button>选中删除到左边</button>
		<button>全部删除到左边</button>
	</div>

</body>
</html>
```

## 3、动态添加和删除行记录

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Untitled Document</title>
<link rel="stylesheet" type="text/css" href="styleB/css.css" />
<script type="text/javascript" src="../../script/jquery-1.7.2.js"></script>
<script type="text/javascript">

	// 网页全部加载完之后，会执行里面的操作
	$(function(){

		// 封装删除表格的方法
		function del(){
			// 在事件响应的 function 函数中，有一个 this 对象，这个 this 对象是当前正在响应事件的 dom 对象
			// 此处即这个 a 标签，取一次他的父标签为 <td>，再取一次为 <tr>
			var $trObj = $(this).parent().parent();

			// find：在给定的祖先元素下匹配所有的后代元素
			// :first：获取第一个元素
			// find("td:first")：选择 td 标签中的第一个元素
			// 即，选择这个对象（$trObj）中的，标签 <td> 中的第一个子标签（td:first）的起始标签和结束标签中的文本（text()）
			var name = $trObj.find("td:first").text();

			// confirm 是JavaScript语言提供的一个确认提示框函数，给他传什么，他就提示什么
			// 当用户点击了确定，他就返回true；当用户点击了取消，他就返回false，
			if( confirm("你确定要删除[" + name + "]吗？") ){
				$trObj.remove();
			}

			// return false：可以阻止元素的默认行为
			return false;
		}

		// 给【添加】按钮绑定单击事件
		$("#addEmpButton").click(function(){

			// 获取输入框中姓名、邮箱、工资的内容
			var name = $("#empName").val();
			var email = $("#email").val();
			var salary = $("#salary").val();

			// 创建一个行标签对象，添加到显示数据的表格中
			var $trObj = $(
				"<tr>" +
					"<td>" + name + "</td>" +
					"<td>" + email + "</td>" +
					"<td>" + salary + "</td>" +
					"<td><a href='deleteEmp'>Delete</a></td>" +
				"</tr>"
			);
			// 将行标签对象添加到显示数据的表格中
			$trObj.appendTo( $("#employeeTable") );

			// 给添加的行标签绑定上事件，调用自己封装的del函数
			$trObj.find("a").click( del );
		});

		// 给删除的 a 标签绑定单击事件，调用自己封装的del函数
		$("a").click( del );

	});

</script>
</head>
<body>

	<!-- 表格1 -->
	<table id="employeeTable">
		<tr>
			<th>姓名</th>
			<th>邮箱</th>
			<th>工资</th>
			<th>&nbsp;</th>
		</tr>
		<tr>
			<td>Tom</td>
			<td>tom@tom.com</td>
			<td>5000</td>
			<td><a href="deleteEmp?id=001">Delete</a></td>
		</tr>
		<tr>
			<td>Jerry</td>
			<td>jerry@sohu.com</td>
			<td>8000</td>
			<td><a href="deleteEmp?id=002">Delete</a></td>
		</tr>
		<tr>
			<td>Bob</td>
			<td>bob@tom.com</td>
			<td>10000</td>
			<td><a href="deleteEmp?id=003">Delete</a></td>
		</tr>
	</table>

	<div id="formDiv">
	
		<h4>添加新员工</h4>

		<!-- 表格2 -->
		<table>
			<tr>
				<td class="word">name: </td>
				<td class="inp">
					<input type="text" name="empName" id="empName" />
				</td>
			</tr>
			<tr>
				<td class="word">email: </td>
				<td class="inp">
					<input type="text" name="email" id="email" />
				</td>
			</tr>
			<tr>
				<td class="word">salary: </td>
				<td class="inp">
					<input type="text" name="salary" id="salary" />
				</td>
			</tr>
			<tr>
				<td colspan="2" align="center">
					<button id="addEmpButton" value="abc">
						添加
					</button>
				</td>
			</tr>
		</table>

	</div>

</body>
</html>
```

# 十、jQuery CSS 样式操作

|方法|介绍|
|--|--|
|addClass()|添加样式|
|removeClass()|删除样式|
|toggleClass()|有就删除，没有就添加样式。|
|offset()|获取和设置元素的坐标。|

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Insert title here</title>
	<style type="text/css">
		div {
			width: 100px;
			height: 260px;
		}

		div.border {
			border: 2px white solid;
		}

		div.redDiv {
			background-color: red;
		}

		div.blackDiv {
			border: 5px blue solid;
		}
	</style>

	<script type="text/javascript" src="script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		$(function () {
			/*
			CSS
			css(name|pro|[,val|fn])       读写匹配元素的样式属性。
											a.css('color')取出a元素的color
											a.css('color',"red")设置a元素的color为red

			CSS 类

			addClass(class|fn) 			为元素添加一个class值;<div class="mini big">
			removeClass([class|fn]) 	删除元素的class值；传递一个具体的class值，就会删除具体的某个class
										a.removeClass()：移除所有的class值
			**/

			var $divEle = $('div:first');

			$('#btn01').click(function () {
				//addClass() - 向被选元素添加一个或多个类
				$divEle.addClass("redDiv blackDiv");
			});

			$('#btn02').click(function () {
				//removeClass() - 从被选元素删除一个或多个类 
				$divEle.removeClass()
			});

			$('#btn03').click(function () {
				//toggleClass() - 对被选元素进行添加/删除类的切换操作 
				//切换就是如果具有该类那么删除，如果没有那么添加上
				$divEle.toggleClass("redDiv");
			});

			$('#btn04').click(function () {
				//offset() - 返回第一个匹配元素相对于文档的位置。
				var os = $divEle.offset();
				//注意通过offset获取到的是一个对象，这个对象有两个属性top表示顶边距，left表示左边距
				alert("顶边距：" + os.top + " 左边距：" + os.left);

				//调用offset设置元素位置时，也需要传递一个js对象，对象有两个属性top和left
				//offset({ top: 10, left: 30 });
				$divEle.offset({
					top: 50,
					left: 60
				});
			});

		})
	</script>
</head>

<body>

	<table align="center">
		<tr>
			<td>
				<div class="border">
				</div>
			</td>

			<td>
				<div class="btn">
					<input type="button" value="addClass()" id="btn01" />
					<input type="button" value="removeClass()" id="btn02" />
					<input type="button" value="toggleClass()" id="btn03" />
					<input type="button" value="offset()" id="btn04" />
				</div>
			</td>
		</tr>
	</table>

	<br /> <br />

	<br /> <br />

</body>

</html>
```

# 十一、jQuery 动画操作

- 动画方法都可以添加参数。
- 第一个参数是动画 执行的时长，以毫秒为单位
- 第二个参数是动画的回调函数 (动画完成后自动调用的函数)

|方法|介绍|
|--|--|
|<font color="red">**基本动画**</font>||
|show()|将隐藏的元素显示|
|hide()|将可见的元素隐藏。|
|toggle()|可见就隐藏，不可见就显示。|
|<font color="red">**淡入淡出动画**</font>||
|fadeIn()|淡入（慢慢可见）|
|fadeOut()|淡出（慢慢消失）|
|fadeToggle()|淡入/淡出 切换|
|fadeTo()|在指定时长内慢慢的将透明度修改到指定的值。<br />0 透明，1 完成可见，0.5 半透明|

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Untitled Document</title>
		<link href="css/style.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="script/jquery-1.7.2.js"></script>
	
<script type="text/javascript">
		/* 	
			基本
			show([speed,[easing],[fn]]) 
			hide([speed,[easing],[fn]]) 
			toggle([speed],[easing],[fn]) 
			滑动
			slideDown([spe],[eas],[fn]) 
			slideUp([speed,[easing],[fn]]) 
			slideToggle([speed],[easing],[fn]) 
			淡入淡出
			fadeIn([speed],[eas],[fn]) 
			fadeOut([speed],[eas],[fn]) 
			fadeTo([[spe],opa,[eas],[fn]]) 
			fadeToggle([speed,[eas],[fn]])
		*/
		$(function(){
			//显示   show()
			$("#btn1").click(function(){
				$("#div1").show(500,function(){
					$("div").css("background-color","red");
				});
			});
			//隐藏  hide()
			$("#btn2").click(function(){
				$("#div1").hide(500,function(){
					alert("已隐藏");
				});
			});	
			//切换   toggle()
			$("#btn3").click(function(){
				$("#div1").toggle(500);
			});	

			// 定义一个函数abc，里面有toggle方法，并且还调用abc方法
			// 即，递归调用
			// var abc = function(){
			// 	$("#div1").toggle(500,abc);
			// }
			// // 此处调用了abc方法，那么他就会一直调用toggle方法
			// abc();
			
			//淡入   fadeIn()
			$("#btn4").click(function(){
				$("#div1").fadeIn(500);
			});	
			//淡出  fadeOut()
			$("#btn5").click(function(){
				$("#div1").fadeOut(500);
			});
			//淡化切换  fadeToggle()
			$("#btn7").click(function(){
				$("#div1").fadeToggle("slow","linear");
			});
			//淡化到  fadeTo()
			$("#btn6").click(function(){
				// Math.random()：随机值
				$("#div1").fadeTo("slow",Math.random());
			});
		})
</script>
	
	</head>
	<body>
		<table style="float: left;">
			<tr>
				<td><button id="btn1">显示show()</button></td>
			</tr>
			<tr>
				<td><button id="btn2">隐藏hide()</button></td>
			</tr>
			<tr>
				<td><button id="btn3">显示/隐藏切换 toggle()</button></td>
			</tr>
			<tr>
				<td><button id="btn4">淡入fadeIn()</button></td>
			</tr>
			<tr>
				<td><button id="btn5">淡出fadeOut()</button></td>
			</tr>
			<tr>
				<td><button id="btn7">淡化切换fadeToggle()</button></td>
			</tr>
			<tr>
				<td><button id="btn6">淡化到fadeTo()</button></td>
			</tr>
		</table>
		
		<div id="div1" style="float:left;border: 1px solid;background-color: blue;width: 300px;height: 200px;">
			jquery动画定义了很多种动画效果，可以很方便的使用这些动画效果
		</div>
	</body>

</html>
```

# 十二、jQuery 事件操作

## 1、jQuery 与 原生 js 的区别

1. 两种方式的区别？

```js
$( function(){} );

window.onload = function(){}
```

2. 他们分别是在什么时候触发？
	1. jQuery 的页面加载完成之后、浏览器的内核解析完页面、标签创建好 DOM 对象之后，就会马上执行。
	2. 原生 js 的页面加载完成之后，除了要等浏览器内核解析完标签创建好 DOM 对象，还要等标签显示时需要的内容加载完成。
3. 他们触发的顺序？
	1. 页面加载完成之后先执行 jQuery
	2. 等原生 js 的页面加载完成之后，再执行原生 js
4. 他们执行的次数？
	1. 原生 js 的页面加载完成之后，只会执行最后一次的赋值函数。
	2. jQuery 的页面加载完成之后是全部把注册的 function 函数，依次顺序全部执行。

## 2、jQuery 中其他的事件处理方法：

|方法|介绍|
|--|--|
|click()|它可以绑定单击事件，以及触发单击事件|
|mouseover()|鼠标移入事件|
|mouseout()|鼠标移出事件|
|bind()|可以给元素一次性绑定一个或多个事件。|
|one()|使用上跟 bind 一样。但是 one 方法绑定的事件只会响应一次。|
|unbind()|跟 bind 方法相反的操作，解除事件的绑定|
|live()|也是用来绑定事件。它可以用来绑定选择器匹配的所有元素的事件。哪怕这个元素是后面动态创建出来的也有效|

```js
// 传入 function 函数是绑定事件
$('h5').click(function () {
	alert("事件");
});

$('#btn01').click(function () {
	// 不传入 function 函数是触发事件
	$("h5").click();
});
```

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Untitled Document</title>
	<link href="css/style.css" type="text/css" rel="stylesheet" />
	<script type="text/javascript" src="../../script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		$(function () {
			//*1.通常绑定事件的方式
			//给元素绑定事件
			//jquery对象.事件方法(回调函数(){ 触发事件执行的代码 }).事件方法(回调函数(){ 触发事件执行的代码 }).事件方法(回调函数(){ 触发事件执行的代码 })
			//绑定事件可以链式操作
			$(".head").click(function () {
				$(".content").toggle();
			}).mouseover(function () {
				$(".content").toggle();
			});

			//*2.jQuery提供的绑定方式：bind(type,[data],fn)函数把元素和事件绑定起来
			//type表示要绑定的事件   [data]表示传入的数据   fn表示事件的处理方法
			//bind(事件字符串,回调函数),后来添加的元素不会绑定事件
			//使用bind()绑定多个事件   type可以接受多个事件类型，使用空格分割多个事件
			/* $(".head").bind("click mouseover",function(){
				$(".content").toggle();
			}); */


			//3.one()只绑定一次,绑定的事件只会发生一次one(type,[data],fn)函数把元素和事件绑定起来
			//type表示要绑定的事件   [data]表示传入的数据   fn表示事件的处理方法
			/* 	$(".head").one("click mouseover",function(){
					$(".content").toggle();
				}); */

			//4.live方法会为现在及以后添加的元素都绑定上相应的事件
			/**	$(".head").live("click",function(){
					$(".content").toggle();
				});

				$("#panel").before("<h5 class='head'>什么是jQuery?</h5>");
			*/
		});
	</script>
</head>

<body>
	<div id="panel">
		<h5 class="head">什么是jQuery?</h5>
		<div class="content">
			jQuery是继Prototype之后又一个优秀的JavaScript库，它是一个由 John Resig
			创建于2006年1月的开源项目。jQuery凭借简洁的语法和跨平台的兼容性，极大地简化了JavaScript开发人员遍历HTML文档、操作DOM、处理事件、执行动画和开发Ajax。它独特而又优雅的代码风格改变了JavaScript程序员的设计思路和编写程序的方式。
		</div>
	</div>
</body>

</html>
```

## 3、事件的冒泡

1. 事件的冒泡是指，父子元素同时监听同一个事件。当触发子元素的事件的时候，同一个事件也被传递到了父元素的事件里去响应。
2. 那么如何阻止事件冒泡呢？在子元素事件函数体内，return false; 可以阻止事件的冒泡传递。

## 4、javaScript 事件对象

1. 事件对象，是封装有触发的事件信息的一个 javascript 对象。
2. 我们重点关心的是怎么拿到这个 javascript 的事件对象。以及使用。
3. 如何获取呢 javascript 事件对象呢？
	1. 在给元素绑定事件的时候，在事件的 function( event ) 参数列表中添加一个参数，这个参数名，我们习惯取名为 event。
	2. 这个 event 就是 javascript 传递参事件处理函数的事件对象
4. 举例：
5. 原生 javascript 获取 事件对像

```js
window.onload = function () {
	document.getElementById("areaDiv").onclick = function (event) {
		console.log(event);
	}
}
```

6. jQuery 代码获取 事件对像

```js
$(function () {
	$("#areaDiv").click(function (event) {
		console.log(event);
	});
});
```

7. 使用 bind 同时对多个事件绑定同一个函数。怎么获取当前操作是什么事件

```js
// mouseover mouseout：在鼠标进入或者离开作用元素或者其子元素时，都会触发
$("#areaDiv").bind("mouseover mouseout",function (event) {
	if (event.type == "mouseover") {
		console.log("鼠标移入");
	} else if (event.type == "mouseout") {
		console.log("鼠标移出");
	}
});
```

# 十三、图片跟随实现

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Insert title here</title>
	<style type="text/css">
		body {
			text-align: center;
		}

		#small {
			margin-top: 150px;
		}

		#showBig {
			position: absolute;
			display: none;
		}
	</style>
	<script type="text/javascript" src="script/jquery-1.7.2.js"></script>
	<script type="text/javascript">
		// 网页全部加载完之后，会执行里面的操作
		$(function () {
			// mouseover：鼠标进入触发
			// mouseout： 鼠标移出触发
			// mousemove：鼠标指针在指定的元素中移动时触发
			$("#small").bind("mouseover mouseout mousemove",function(event){

				// 判断鼠标是否移入其中
				if( event.type == "mouseover" ){
					// 显示隐藏的元素
					$("#showBig").show();
				// 判断鼠标是否移出
				}else if( event.type == "mouseout" ){
					// 隐藏可见的元素
					$("#showBig").hide();
				// 判断鼠标是否在指定的元素中移动
				}else if( event.type == "mousemove" ){
					$("#showBig").offset({
						// 把鼠标指针离开这个图片一些距离
						// 不然会判断鼠标在显示的大图片上，而不是在小图片里
						left:event.pageX + 10,
						top:event.pageY + 10
					});
				}

			});

		});
	</script>
</head>

<body>

	<img id="small" src="img/small.jpg" />

	<div id="showBig">
		<img src="img/big.jpg">
	</div>

</body>

</html>
```
