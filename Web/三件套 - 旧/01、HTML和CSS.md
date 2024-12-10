# 一、B/S 软件的结构

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F001、BS软件的结构.png)

# 二、前端的开发流程

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F002、前端的开发流程.png)

# 三、网页的组成部分

1. 页面由三部分内容组成：分别是内容（结构）、表现、行为。
2. 内容（结构），是我们在页面中可以看到的数据。我们称之为内容。一般内容 我们使用html 技术来展示。
3. 表现，指的是这些内容在页面上的展示形式。比如说。布局，颜色，大小等等。一般使用CSS 技术实现

# 四、HTML 简介

1. Hyper Text Markup Language （超文本标记语言），简写：HTML
2. HTML 通过标签来标记要显示的网页中的各个部分。网页文件本身是一种文本文件，通过在文本文件中添加标记符，可以告诉浏览器如何显示其中的内容（如：文字如何处理，画面如何安排，图片如何显示等）

# 五、创建 HTML 文件

1. 创建一个 web 工程（静态的 web 工程）

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F003、创建一个web工程（静态的web工程）.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F004、创建一个web工程（静态的web工程）2.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F005、创建一个web工程（静态的web工程）3.png)

2. 在工程下创建 html 页面

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F006、在工程下创建html页面.png)

3. 选择浏览器执行页面

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F007、选择浏览器执行页面.png)

4. 第一个 html 示例：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F008、第一个html示例.png)

5. 注：<font color="red">Java 文件是需要先编译，再由 java 虚拟机跑起来。但 HTML 文件它不需要编译，直接由浏览器进行解析执行。</font>

# 六、HTML 文件的书写规

```html
<!-- 这是 html 注释，可以在页面右键查看源代码中看到 -->
<!-- 约束、声明 -->
<!DOCTYPE html>

	<!-- html标签表示html的开始，lang="zh_CN"表示中文， -->
	<!-- html标签中一般分为两部分，分别是：head、body -->
	<html lang="zh_CN">         

	<!-- 表示头部信息，一般包含三部分内容，title标签、css样式、js代码 -->
	<head>

		<!-- 表示当前页面使用UTF-8字符集 -->
		<meta charset="UTF-8">

		<!-- 表示本html页面显示的标题 -->
		<title>标题</title>

	</head>

	<!-- body标签：网页的主体内容 -->
	<body>
		hello
	</body>

<!-- 表示整个 html 页面的结束 -->
</html>
```

# 七、HTML 标签介绍

## 1、标签的格式

1. 标签名大小写不敏感

```html
<标签名>封装的数据</标签名>
<p>月海</p>
```

## 2、标签拥有自己的属性

1. 分为基本属性：可以修改简单的样式效果

```java
bgcolor="red"
```
   
2. 事件属性： 可以直接设置事件响应后的代码。

```html
onclick="alert('你好！');"
```

## 3、标签又分为，单标签和双标签

1. 单标签格式： `br`：换行、`hr`：水平线

```html
<标签名 />
<br/>
```
   
2. 双标签格式：

```html
<标签名> ...封装的数据...</标签名>
<p>月海</p>
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F009、HTML标签介绍.png)

## 4、标签的语法

1. 标签不能交叉嵌套

```html
<!-- 正确： -->
<div><span>早安，尚硅谷</span></div>

<!-- 错误： -->
<div><span>早安，尚硅谷</div></span>
```

2. 标签必须正确关闭
3. 有文本内容的标签

```html
<!-- 正确： -->
<div>早安，尚硅谷</div>

<!-- 错误： -->
<div>早安，尚硅谷
```

4. 没有文本内容的标签

```html
<!-- 正确： -->
<br />

<!-- 错误： -->
<br>
```

5. 属性必须有值，属性值必须加引号

```html
<!-- 正确： -->
<font color="blue">早安，尚硅谷</font>

<!-- 错误： -->
<font color=blue>早安，尚硅谷</font>

<!-- 错误： -->
<font color>早安，尚硅谷</font>
```

6. 注释不能嵌套

```html
<!-- 正确： -->
<!-- 注释内容 --> <br/>

<!-- 错误： -->
<!-- <!-- 这是错误的 html注释 --> -->
```

7. <font color="red">注意事项：</font>html 代码不是很严谨。有时候标签不闭合，也不会报错。

# 八、常用标签介绍

## 1、font 字体标签

```html
<!-- 字体标签
	需求 1：在网页上显示 我是字体标签 ，并修改字体为 宋体，颜色为红色。

	font标签是字体标签,它可以用来修改文本的字体，颜色，大小(尺寸)
		color 属性修改颜色
		face 属性修改字体
		size 属性修改文本大
 -->
<font color="red" face="宋体" size="8">月海</font>
```

## 2、特殊字符

```html
<!-- 特殊字符
	需求 1：把 <br> 换行标签 变成文本 转换成字符显示在页面上

	常用的特殊字符:
		< ： &lt;
> ： &gt;
		空格 ： &nbsp;
-->
我是&lt;br&gt;标&nbsp;&nbsp;&nbsp;&nbsp;签<br/>
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F010、常用特殊字符表.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F011、其他特殊字符表.png)

## 3、标题标签

```html
<!-- 标题标签
	需求 1：演示标题 1 到 标题 6 的

	h1 - h6 都是标题标签
	h1 最大
	h6 最小

	align 属性是对齐属性
		left 左对齐(默认)
		center 剧中
		right 右对齐
-->
<h1 align="left">标题 1</h1>
<h2 align="center">标题 2</h2>
<h3 align="right">标题 3</h3>
<h4>标题 4</h4>
<h5>标题 5</h5>
<h6>标题 6</h6>
<!-- 无效果 -->
<h7>标题 7</h7>
```

## 4、超链接

- 在网页中所有点击之后可以跳转的内容都是超连接

```html
<!-- a 标签是 超链接
	href 属性设置连接的地址
	target 属性设置哪个目标进行跳转
		_self 表示当前页面(默认值)
		_blank 表示打开新页面来进行跳转
-->
<a href="http://localhost:8080">百度</a><br/>
<a href="http://localhost:8080" target="_self">百度_self</a><br/>
<a href="http://localhost:8080" target="_blank">百度_blank</a><br/>
```

## 5、列表标签

```html
<!--列表标签：无序列表 、 有序列表
	需求 1：使用无序，列表方式，把东北 F4，赵四，刘能，小沈阳，宋小宝，展示出来

	ul 是无序列表
		type 属性可以修改列表项前面的符号
	ol 是有序列表（不常用）

	li 是列表项
-->
<ul type="none">
	<li>赵四</li>
	<li>刘能</li>
	<li>小沈阳</li>
	<li>宋小宝</li>
</ul>

<ol>
	<ol>
	
	</ol>
</ol>
```

## 6、img 标签

```html
<!--img 标签
	需求 1：使用 img 标签显示一张美女的照片。并修改宽高，和边框属性

	img 标签是图片标签,用来显示图片
		src 属性可以设置图片的路径
		width 属性设置图片的宽度
		height 属性设置图片的高度
		border 属性设置图片边框大小
		alt 属性设置当指定路径找不到图片时,用来代替显示的文本内容

	在 JavaSE 中路径也分为相对路径和绝对路径
		相对路径：从工程名开始算
		绝对路径：盘符:/目录/文件名

	在 web 中路径分为相对路径和绝对路径两种
	相对路径:
		.       表示当前文件所在的目录
		..      表示当前文件所在的上一级目录
		文件名  表示当前文件所在目录的文件,相当于 ./文件名 ./ 可以省略
	绝对路径:
		正确格式是: http://ip:port/工程名/资源路径
		错误格式是: 盘符:/目录/文件名
-->
<img src="1.jpg" width="200" height="260" border="1" alt="美女找不到"/>
<img src="../2.jpg" width="200" height="260" />
<img src="../imgs/3.jpg" width="200" height="260" />
<img src="../imgs/4.jpg" width="200" height="260" />
<img src="../imgs/5.jpg" width="200" height="260" />
<img src="../imgs/6.jpg" width="200" height="260" />
```

## 7、表格标签

```html
<!--表格标签
	需求 1：做一个 带表头的 ，三行，三列的表格，并显示边框
	需求 2：修改表格的宽度，高度，表格的对齐方式，单元格间距。
	
	table 标签是表格标签
		border 设置表格标签
		width 设置表格宽度
		height 设置表格高度
		align 设置表格相对于页面的对齐方式
		cellspacing 设置单元格间距
	
	tr 是行标签            表示一行
		th 是表头标签      大多数浏览器会把表头显示为粗体居中的文本
		td 是单元格标签    普通数据单元格的内容
		align 设置单元格文本对齐方式
	
	b 是加粗标签
-->
<table align="center" border="1" width="300" height="300" cellspacing="0">
	<tr>
		<th>1.1</th>
		<th>1.2</th>
		<th>1.3</th>
	</tr>
	<tr>
		<td><b>2.1</b></td>
		<td>2.2</td>
		<td>2.3</td>
	</tr>
	<tr>
		<td>3.1</td>
		<td>3.2</td>
		<td>3.3</td>
	</tr>
</table>
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F012、表格标签.png)

## 8、跨行跨列表格

```html
<!-- 跨行跨列表格
	需求 1：新建一个五行，五列的表格，
			第一行，第一列的单元格要跨两列，
			第二行第一列的单元格跨两行，
			第四行第四列的单元格跨两行两列。

	colspan 属性设置跨列
	rowspan 属性设置跨行
-->
<table width="500" height="500" cellspacing="0" border="1">
	<tr>
		<!-- 这个单元格占同一行，横着的两个格子 -->
		<!-- 既，以原先格子为起点，向右扩展一格 -->
		<td colspan="2">1.1</td>
		<td>1.3</td>
		<td>1.4</td>
		<td>1.5</td>
	</tr>
	<tr>
		<!-- 这个单元格占同一列，竖着的两个格子 -->
		<!-- 既，以原先格子为起点，向下扩展一格 -->
		<td rowspan="2">2.1</td>
		<td>2.2</td>
		<td>2.3</td>
		<td>2.4</td>
		<td>2.5</td>
	</tr>
	<tr>
		<td>3.2</td>
		<td>3.3</td>
		<td>3.4</td>
		<td>3.5</td>
	</tr>
	<tr>
		<td>4.1</td>
		<td>4.2</td>
		<td>4.3</td>
		<!-- 这个单元格占同一行和同一列，横着和竖着的两四格子 -->
		<!-- 既，以原先格子为起点，向右、下扩展各一格，其包裹的面积 -->
		<td colspan="2" rowspan="2">4.4</td>
	</tr>
	<tr>
		<td>5.1</td>
		<td>5.2</td>
		<td>5.3</td>
	</tr>
</table>
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F013、跨行跨列表格.png)

## 9、了解 iframe 框架标签 (内嵌窗口)

```html
<!--ifarme 标签可以在页面上开辟一个小区域，显示一个单独的页面
	ifarme 和 a 标签组合使用的步骤:
		1 在 iframe 标签中使用 name 属性定义一个名称
		2 在 a 标签的 target 属性上设置 iframe 的 name 的属性值
-->
<iframe src="3.标题标签.html" width="500" height="400" name="abc"></iframe>

<br/>

<ul>
	<li><a href="0-标签语法.html" target="abc">0-标签语法.html</a></li>
	<li><a href="1.font 标签.html" target="abc">1.font 标签.html</a></li>
	<li><a href="2.特殊字符.html" target="abc">2.特殊字符.html</a></li>
</ul>
```

## 10、表单标签

1. 什么是表单：表单就是 html 页面中，用来收集用户信息的所有元素集合.然后把这些信息发送给服务器

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F014、表单标签.png)

2. 表单的显示：

```html
<!--表单标签
	需求 1:创建一个个人信息注册的表单界面。包含用户名，密码，确认密码。性别（单选），兴趣爱好（多选），国籍（下拉列表）。
	隐藏域，自我评价（多行文本域）。重置，提交。
-->
<!--
	form 标签就是表单
		input type=text     是文件输入框 value 设置默认显示内容
		input type=password 是密码输入框 value 设置默认显示内容
		input type=radio    是单选框 name 属性可以对其进行分组 checked="checked"表示默认选中
		input type=checkbox 是复选框 checked="checked"表示默认选中

		input type=reset    是重置按钮 value 属性修改按钮上的文本
		input type=submit   是提交按钮 value 属性修改按钮上的文本
		input type=button   是按钮 value 属性修改按钮上的文本

		input type=file     是文件上传域
		input type=hidden   是隐藏域 当我们要发送某些信息，而这些信息，不需要用户参与，就可以使用隐藏域（提交的时候同时发送给服务器）

		select 标签是下拉列表框
			option 标签是下拉列表框中的选项 selected="selected"设置默认选中

		textarea 表示多行文本输入框 （起始标签和结束标签中的内容是默认值）
			rows 属性设置可以显示几行的高度
			cols 属性设置每行可以显示几个字符宽度
-->
<form>
	<!-- input type=text     是文件输入框 value 设置默认显示内容 -->
	用户名称：<input type="text" value="默认值"/><br/>
	<!-- input type=password 是密码输入框 value 设置默认显示内容 -->
	用户密码：<input type="password" value="abc"/><br/>
	确认密码：<input type="password" value="abc"/><br/>
	性别：
		<!-- input type=radio    是单选框，后面接选项-->
		<!-- 通过 name 属性可以对其进行分组，这样单选框就只能选中其中的一个 -->
		<!-- checked="checked"表示默认选中 -->
		<input type="radio" name="sex"/>男
		<input type="radio" name="sex" checked="checked" />女
		<br/>
	兴趣爱好：
		<!-- input type=checkbox 是复选框 checked="checked"表示默认选中 -->
		<!-- 通过 name 属性可以对其进行分组，这样单选框就只能选中其中的一个 -->
		<!-- checked="checked"表示默认选中 -->
		<input type="checkbox" checked="checked" />Java
		<input type="checkbox" />JavaScript
		<input type="checkbox" />C++
		<br/>
	国籍：
	<!-- select 标签是下拉列表框 -->
	<select>
		<!-- option 标签是下拉列表框中的选项 -->
		<!-- selected="selected"设置默认选中 -->
		<option>--请选择国籍--</option>
		<option selected="selected">中国</option>
		<option>美国</option>
		<option>小日本</option>
	</select><br/>
	自我评价：
		<!-- textarea 表示多行文本输入框 （起始标签和结束标签中的内容是默认值） -->
		<!-- rows 属性设置可以显示几行的高度
			 cols 属性设置每行可以显示几个字符宽度 -->
		<textarea rows="10" cols="20">我才是默认值</textarea><br/>

		<!-- input type=file     是文件上传域 -->
		<input type="file" >

		<!-- input type=reset    是重置按钮，value属性是按钮显示的名称 -->
		<input type="reset" value="abc" />
		<!-- input type=submit   是提交按钮，value属性是按钮显示的名称 -->
		<input type="submit"/>
</form>
```

3. 表单格式化：

```html
<form>
	<h1 align="center">用户注册</h1>
	<table align="center">
		<tr>
			<td> 用户名称：</td>
			<td>
				<input type="text" value="默认值"/>
			</td>
		</tr>
		<tr>
			<td> 用户密码：</td>
			<td><input type="password" value="abc"/></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" value="abc"/></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				<input type="radio" name="sex"/>男
				<input type="radio" name="sex" checked="checked" />女
			</td>
		</tr>
		<tr>
			<td> 兴趣爱好：</td>
			<td>
				<input type="checkbox" checked="checked" />Java
				<input type="checkbox" />JavaScript
				<input type="checkbox" />C++
			</td>
		</tr>
		<tr>
			<td>国籍：</td>
			<td>
				<select>
					<option>--请选择国籍--</option>
					<option selected="selected">中国</option>
					<option>美国</option>
					<option>小日本</option>
				</select>
			</td>
		</tr>
		<tr>
			<td>自我评价：</td>
			<td><textarea rows="10" cols="20">我才是默认值</textarea></td>
		</tr>
		<tr>
			<td><input type="reset" /></td>
			<td align="center"><input type="submit"/></td>
		</tr>
	</table>
</form>
```

4. **表单提交细节：**

```html
<!--
	form 标签是表单标签
		action 属性设置提交的服务器地址
		method 属性设置提交的方式 GET(默认值)或 POST

	表单提交的时候，数据没有发送给服务器的三种情况：
		1、表单项没有 name 属性值，想要将数据发送给服务器，必须加上name属性值
		2、单选、复选（下拉列表中的 option 标签）都需要添加 value 属性，以便发送给服务器
		3、表单项不在提交的 form 标签中

	GET 请求的特点是：
		1、浏览器地址栏中的地址是：action 属性[+?+请求参数]
		请求参数的格式是：name=value&name=value
		2、不安全（明文链接，所有参数信息都在连接中显示出来了）
		3、它有数据长度的限制

	POST 请求的特点是：
		1、浏览器地址栏中只有 action 属性值
		2、相对于 GET 请求要安全
		3、理论上没有数据长度的限制
-->

<!-- action 属性设置提交的服务器地址 -->
<!-- method 属性设置提交的方式 GET(默认值)或 POST -->
<form action="http://localhost:8080" method="post">
	<!-- input type=hidden   是隐藏域，当我们要发送某些信息，而这些信息，不需要用户参与，就可以使用隐藏域（提交的时候同时发送给服务器）-->
	<input type="hidden" name="action" value="login" />
	<h1 align="center">用户注册</h1>
	<table align="center">
		<tr>
			<td> 用户名称：</td>
			<td>
				<input type="text" name="username" value="默认值"/>
			</td>
		</tr>
		<tr>
			<td> 用户密码：</td>
			<td><input type="password" name="password" value="abc"/></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				<!-- 单选、复选（下拉列表中的 option 标签）都需要添加 value 属性，以便发送给服务器 -->
				<input type="radio" name="sex" value="boy"/>男
				<input type="radio" name="sex" checked="checked" value="girl" />女
			</td>
		</tr>
		<tr>
			<td> 兴趣爱好：</td>
			<td>
				<input name="hobby" type="checkbox" checked="checked" value="java"/>Java
				<input name="hobby" type="checkbox" value="js"/>JavaScript
				<input name="hobby" type="checkbox" value="cpp"/>C++
			</td>
		</tr>
		<tr>
			<td>国籍：</td>
			<td>
				<select name="country">
					<option value="none">--请选择国籍--</option>
					<option value="cn" selected="selected">中国</option>
					<option value="usa">美国</option>
					<option value="jp">小日本</option>
				</select>
			</td>
		</tr>
		<tr>
			<td>自我评价：</td>
			<td><textarea name="desc" rows="10" cols="20">我才是默认值</textarea></td>
		</tr>
		<tr>
			<td><input type="reset" /></td>
			<td align="center"><input type="submit"/></td>
		</tr>
	</table>
</form>
```

## 11、其他标签

```html
    <!--其他标签
        需求 1：div、span、p 标签的演示

        div 标签 默认独占一行
        span 标签 它的长度是封装数据的长度
        p 段落标签 默认会在段落的上方或下方各空出一行来（如果已有就不再空）
    -->
    <div>div 标签 1</div>
    <div>div 标签 2</div>
    <span>span 标签 1</span>
    <span>span 标签 2</span>
    <p>p 段落标签 1</p>
    <p>p 段落标签 2</p>
```

# 九、CSS 技术

## 1、CSS 技术介绍

- CSS 是「层叠样式表单」。是用于(增强)控制网页样式并允许将样式信息与网页内容分离的一种标记性语言。

## 2、CSS 语法规则

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%20-%20%E6%97%A7%2Fattachments%2F015、CSS语法规则.png)

1. <font color="red">选择器：</font>浏览器根据“选择器”决定受 CSS 样式影响的 HTML 元素（标签）。
2. <font color="red">属性 (property) </font>是你要改变的样式名，并且每个属性都有一个值。属性和值被冒号分开，并由花括号包围，这样就组成了一个完整的样式声明（declaration），例如：p {color: blue}
3. <font color="red">多个声明：</font>如果要定义不止一个声明，则需要用分号将每个声明分开。虽然最后一条声明的最后可以不加分号(但尽量在每条声明的末尾都加上分号)

```css
/* CSS 注释：/*注释内容*/
/* 注：一般每行只描述一个属性 */
p{
	color:red;
	font-size:30px;
}
```

## 3、CSS 和 HTML 的结合方式

### ①、第一种：在标签的 style 属性上设置 `key:value`，修改标签样式。

- 这种方式的缺点：
1. 如果标签多了。样式多了。代码量非常庞大。
2. 可读性非常差。
3. Css 代码没什么复用性可方言

```html
<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
	</head>
	<body>
		<!--需求 1：分别定义两个 div、span 标签，分别修改每个 div 标签的样式为：边框 1 个像素，实线，红色。px：像素单位-->
		<div style="border: 1px solid red;">div 标签 1</div>
		<div style="border: 1px solid red;">div 标签 2</div>
		<span style="border: 1px solid red;">span 标签 1</span>
		<span style="border: 1px solid red;">span 标签 2</span>
	</body>
</html>
```

### ②、第二种：在 head 标签中，使用 style 标签来定义各种自己需要的 css 样式。

1. 格式

```css
    xxx {
        Key : value value;
    }
```

- 这种方式的缺点。
1. 只能在同一页面内复用代码，不能在多个页面中复用 css 代码。
2. 维护起来不方便，实际的项目中会有成千上万的页面，要到每个页面中去修改。工作量太大了。

```html
<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<!--style 标签专门用来定义 css 样式代码-->
		<style type="text/css">
			/* 需求 1：分别定义两个 div、span 标签，分别修改每个 div 标签的样式为：边框 1 个像素，实线，红色。*/
			div{
				border: 1px solid red;
			}
			span{
				border: 1px solid red;
			}
		</style>
	</head>
	<body>
		<div>div 标签 1</div>
		<div>div 标签 2</div>
		<span>span 标签 1</span>
		<span>span 标签 2</span>
	</body>
</html>
```

### ③、 第三种：把 css 样式写成一个单独的 css 文件，再通过 link 标签引入即可复用。

1. css 文件内容

```css
 div{
	 border: 1px solid yellow;
 }
 span{
	 border: 1px solid red;
 }
```

2. html 文件代码

```html
 <!DOCTYPE html>
	 <html lang="en">
	 <head>
		 <meta charset="UTF-8">
		 <title>Title</title>
		 <!--link 标签专门用来引入 css 样式代码-->
		 <link rel="stylesheet" type="text/css" href="1.css"/>
	 </head>
	 <body>
		 <div>div 标签 1</div>
		 <div>div 标签 2</div>
		 <span>span 标签 1</span>
		 <span>span 标签 2</span>
	 </body>
 </html>
```

## 4、CSS 选择器

### ①、标签名选择器

- 可以决定哪些标签被动的使用这个样式。
1. 格式

```css
标签名{
	属性：值;
}
```

2. 示例代码

```html
 <!DOCTYPE html>
 <html>
	 <head>
		 <meta charset="UTF-8">
		 <title>CSS 选择器</title>
		 <style type="text/css">
			 div{
				border: 1px solid yellow;
				color: blue;
				font-size: 30px;
			 }
			 span{
				border: 5px dashed blue;
				color: yellow;
				font-size: 20px;
			 }
		 </style>
	 </head>
	 <body>
		 <!-- 需求 1：在所有 div 标签上修改字体颜色为蓝色，字体大小 30 个像素。边框为 1 像素黄色实线。
		 并且修改所有 span 标签的字体颜色为黄色，字体大小 20 个像素。边框为 5 像素蓝色虚线。
		 -->
		 <div>div 标签 1</div>
		 <div>div 标签 2</div>
		 <span>span 标签 1</span>
		 <span>span 标签 2</span>
	 </body>
 </html>
```

### ②、id 选择器

- 可以让我们通过 id 属性选择性的去使用这个样式。
- id是唯一标识一个元素的，在一个文件中只能出现一次并且能够非常精准的找到特定的元素
- 在一个HTML文档中，ID选择器只能使用一次，而且仅一次，id与类选择器一起使用时，优先使用id选择器

1. 格式

```css
#id 属性值{
	属性：值;
}
```

2. 示例代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>ID 选择器</title>
		<style type="text/css">
			#id001{
				color: blue;
				font-size: 30px;
				border: 1px yellow solid;
			}
			#id002{
				color: red;
				font-size: 20px;
				border: 5px blue dotted ;
		}
		</style>
	</head>
	<body>
		<!-- 需求 1：分别定义两个 div 标签，
		第一个 div 标签定义 id 为 id001 ，然后根据 id 属性定义 css 样式修改字体颜色为蓝色，
		字体大小 30 个像素。边框为 1 像素黄色实线。
		第二个 div 标签定义 id 为 id002 ，然后根据 id 属性定义 css 样式 修改的字体颜色为红色，字体大小 20 个像素。
		边框为 5 像素蓝色点线。
		-->
		<div id="id002">div 标签 1</div>
		<div id="id001">div 标签 2</div>
	</body>
</html>
```

### ③、class 选择器（类选择器）

- 可以通过 class 属性有效的选择性地去使用这个样式
- 类选择器可以使用多次

1. 格式

```css
.class 属性值{
	属性：值;
}
```

2. 示例代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>class 类型选择器</title>
		<style type="text/css">
			.class01{
				color: blue;
				font-size: 30px;
				border: 1px solid yellow;
			}
			.class02{
				color: grey;
				font-size: 26px;
				border: 1px solid red;
			}
		</style>
	</head>
	<body>
		<!--需求 1：修改 class 属性值为 class01 的 span 或 div 标签，字体颜色为蓝色，字体大小 30 个像素。边框为 1 像素黄色实线。
		需求 2：修改 class 属性值为 class02 的 div 标签，字体颜色为灰色，字体大小 26 个像素。边框为 1 像素红色实线。
		-->
		<div class="class02">div 标签 class01</div>
		<div class="class02">div 标签</div>
		<span class="class02">span 标签 class01</span>
		<span>span 标签 2</span>
	</body>
</html>
```


### ④、组合选择器

- 组合选择器可以让多个选择器共用同一个 css 样式代码。

1. 格式

```css
选择器 1，选择器 2，选择器 n{
	属性：值;
}
```

2. 示例代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>class 类型选择器</title>
		<style type="text/css">
			.class01 , #id01{
				color: blue;
				font-size: 20px;
				border: 1px yellow solid;
			}
		</style>
	</head>
	<body>
		<!-- 需求 1：修改 class="class01" 的 div 标签 和 id="id01" 所有的 span 标签，
		字体颜色为蓝色，字体大小 20 个像素。边框为 1 像素黄色实线。
		-->
		<div id="id01">div 标签 class01</div> <br />
		<span >span 标签</span> <br />
		<div>div 标签</div> <br />
		<div>div 标签 id01</div> <br />
	</body>
</html>
```

## 5、常用样式

1. 字体颜色
	1. 颜色可以写颜色名如：black, blue, red, green 等
	2. 颜色也可以写 rgb 值和十六进制表示值：如 rgb(255,0,0)，#00F6DE，如果写十六进制值必须加 `#`

```css
color:red；
```

2. 宽度
   1. 宽度可以写像素值：19px；
   2. 也可以写百分比值：20%；

```css
width:19px;
```

3. 高度
   1. 高度可以写像素值：19px；
   2. 也可以写百分比值：20%；

```css
height:20px;
```

4. 背景颜色

```css
background-color:#0F2D4C
```

5. 字体样式：

```css
color：#FF0000；字体颜色红色
font-size：20px; 字体大小
```

6.  红色 1 像素实线边框

```css
border：1px solid red;
```

7.  DIV 居中：div 块相对于整个页面居中

```css
margin-left: auto;
margin-right: auto;
```
   
8.  文本居中

```css
text-align: center;
```

9.  超连接去下划线

```css
text-decoration: none;
```

10. 表格细线

```css
table {
	border: 1px solid black; /*设置边框*/
	border-collapse: collapse; /*将边框合并*/
}
td,th {
	border: 1px solid black; /*设置边框*/
}
```

11. 列表去除修饰

```css
ul {
	list-style: none;
}
```

12. 示例代码：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>06-css 常用样式.html</title>
		<style type="text/css">
			div{
				color: red;
				border: 1px yellow solid;
				width: 300px;
				height: 300px;
				background-color: green;
				font-size: 30px;
				margin-left: auto;
				margin-right: auto;
				text-align: center;
			}
			table{
				border: 1px red solid;
				border-collapse: collapse;
			}
			td{
				border: 1px red solid;
			}
			a{
				text-decoration: none;
			}
			ul{
				list-style: none;
			}
		</style>
	</head>
	<body>
		<ul>
			<li>11111111111</li>
			<li>11111111111</li>
			<li>11111111111</li>
			<li>11111111111</li>
			<li>11111111111</li>
		</ul>
		<table>
			<tr>
				<td>1.1</td>
				<td>1.2</td>
			</tr>
		</table>
		<a href="http://www.baidu.com">百度</a>
		<div>我是 div 标签</div>
	</body>
</html>
```
