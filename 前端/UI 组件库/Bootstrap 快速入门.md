> [https://developer.aliyun.com/course/23](https://developer.aliyun.com/course/23) ，很差
> [Bootstrap.jpg](https://www.yuque.com/attachments/yuque/0/2023/jpeg/29280567/1673925876960-345b03c8-5759-4821-a96f-602f9c502c11.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fjpeg%2F29280567%2F1673925876960-345b03c8-5759-4821-a96f-602f9c502c11.jpeg%22%2C%22name%22%3A%22Bootstrap.jpg%22%2C%22size%22%3A92783%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u3ac819bb-6bfa-4f26-9f19-23927da3fd8%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22uca2b7a35%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

# 一、Bootstrap 简介
## 1、Bootstrap 介绍

1. 官网：[getbootstrap.com](https://getbootstrap.com)
2. 中文网址：[www.bootcss.com](https://www.bootcss.com)
## 2、Bootstrap 下载
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657614548824-a12bcf99-05a5-4a31-942b-31c3b09a74ab.png#clientId=u0af9bfdb-89f4-4&from=paste&height=335&id=ufadc78b1&name=image.png&originHeight=335&originWidth=885&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60451&status=done&style=stroke&taskId=ue7eb940a-f6f0-49c7-bf26-7c207404755&title=&width=885)

- 或者通过网络引入：
```html
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
```
## 3、Bootstrap 基本模板
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>

</head>
<body>
    <h1>你好，世界！</h1>
</body>
</html>
```
# 二、Bootstrap 全局 css 样式
> [https://v3.bootcss.com/css/](https://v3.bootcss.com/css/)

## 1、排版与链接
Bootstrap 排版、链接样式设置了基本的全局样式。分别是：

1. 为 body 元素设置 `background-color: #fff`
2. 使用 `@font-family-base`、`@font-size-base` 和 `@line-height-base` 变量作为排版的基本参数
3. 为所有链接设置了基本颜色 `@link-color`，并且当链接处于 `:hover` 状态时才添加下划线
## 2、布局容器
Bootstrap 需要为页面内容和栅格系统包裹一个 .container 容器。我们提供了两个作此用处的类。注意，由于 padding 等属性的原因，这两种 容器类不能互相嵌套。
`.container` 类用于固定宽度并支持响应式布局的容器
```html
<div class="container">
  ...
</div>
```
`.container-fluid` 类用于 100% 宽度，占据全部视口（viewport）的容器。
```html
<div class="container-fluid">
  ...
</div>
```
## 3、更改样式

- Bootstrap 中可通过这种方式来更改样式

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657616314364-19a14c08-af90-4b63-acfe-7999818325b7.png#clientId=u16004791-dc8f-4&from=paste&height=448&id=u6cf76ffd&name=image.png&originHeight=448&originWidth=478&originalType=binary&ratio=1&rotation=0&showTitle=false&size=125205&status=done&style=stroke&taskId=u8d4ae8f2-a7d9-4735-ad05-e86f0f90d56&title=&width=478)
## 4、栅格系统
### ①、简介
栅格系统用于通过一系列的行（row）与列（column）的组合来创建页面布局，你的内容就可以放入这些创建好的布局中。下面就介绍一下 Bootstrap 栅格系统的工作原理：

- “行（row）”必须包含在 .container （固定宽度）或 .container-fluid （100% 宽度）中，以便为其赋予合适的排列（aligment）和内补（padding）。
- 通过“行（row）”在水平方向创建一组“列（column）”。
- 你的内容应当放置于“列（column）”内，并且，只有“列（column）”可以作为行（row）”的直接子元素。
- 类似 .row 和 .col-xs-4 这种预定义的类，可以用来快速创建栅格布局。Bootstrap 源码中定义的 mixin 也可以用来创建语义化的布局。
- 通过为“列（column）”设置 padding 属性，从而创建列与列之间的间隔（gutter）。通过为 .row 元素设置负值 margin 从而抵消掉为 .container 元素设置的 padding，也就间接为“行（row）”所包含的“列（column）”抵消掉了padding。
- 负值的 margin就是下面的示例为什么是向外突出的原因。在栅格列中的内容排成一行。
- 栅格系统中的列是通过指定1到12的值来表示其跨越的范围。例如，三个等宽的列可以使用三个 .col-xs-4 来创建。
- 如果一“行（row）”中包含了的“列（column）”大于 12，多余的“列（column）”所在的元素将被作为一个整体另起一行排列。
- 栅格类适用于与屏幕宽度大于或等于分界点大小的设备 ， 并且针对小屏幕设备覆盖栅格类。 因此，在元素上应用任何 .col-md-* 栅格类适用于与屏幕宽度大于或等于分界点大小的设备 ， 并且针对小屏幕设备覆盖栅格类。 因此，在元素上应用任何 .col-lg-* 不存在， 也影响大屏幕设备。

通过研究后面的实例，可以将这些原理应用到你的代码中。
### ②、栅格参数
最大 12 列， .col-lg- 后加的数字即为站几列
通过下表可以详细查看 Bootstrap 的栅格系统是如何在多种屏幕设备上工作的

|  | 超小屏幕 手机 (<768px) | 小屏幕 平板 (≥768px) | 中等屏幕 桌面显示器 (≥992px) | 大屏幕 大桌面显示器 (≥1200px) |
| --- | --- | --- | --- | --- |
| 栅格系统行为 | 总是水平排列 | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列C |  |  |
| .container 最大宽度 | None （自动） | 750px | 970px | 1170px |
| 类前缀 | .col-xs- | .col-sm- | .col-md- | .col-lg- |
| 列（column）数 | 12 |  |  |  |
| 最大列（column）宽 | 自动 | ~62px | ~81px | ~97px |
| 槽（gutter）宽 | 30px （每列左右均有 15px） |  |  |  |
| 可嵌套 | 是 |  |  |  |
| 偏移（Offsets） | 是 |  |  |  |
| 列排序 | 是 |  |  |  |

### ③、移动设备和桌面屏幕
是否不希望在小屏幕设备上所有列都堆叠在一起？那就使用针对超小屏幕和中等屏幕设备所定义的类吧，即 .col-xs-* 和 .col-md-*
```html
<!-- Stack the columns on mobile by making one full-width and the other half-width -->
<div class="row">
  <div class="col-xs-12 col-md-8">.col-xs-12 .col-md-8</div>
  <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
</div>

<!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
<div class="row">
  <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
  <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
  <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
</div>

<!-- Columns are always 50% wide, on mobile and desktop -->
<div class="row">
  <div class="col-xs-6">.col-xs-6</div>
  <div class="col-xs-6">.col-xs-6</div>
</div>
```
### ④、列偏移
使用 .col-md-offset-* 类可以将列向右侧偏移。这些类实际是通过使用 * 选择器为当前元素增加了左侧的边距（margin）。例如，.col-md-offset-4 类将 .col-md-4 元素向右侧偏移了4个列（column）的宽度
```html
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>
</div>
<div class="row">
  <div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
  <div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
</div>
<div class="row">
  <div class="col-md-6 col-md-offset-3">.col-md-6 .col-md-offset-3</div>
</div>
```
### ⑤、嵌套列
为了使用内置的栅格系统将内容再次嵌套，可以通过添加一个新的 .row 元素和一系列 .col-sm-* 元素到已经存在的 .col-sm-* 元素内。被嵌套的行（row）所包含的列（column）的个数不能超过12（其实，没有要求你必须占满12列）。
```html
<div class="row">
  <div class="col-sm-9">
    Level 1: .col-sm-9
    <div class="row">
      <div class="col-xs-8 col-sm-6">
        Level 2: .col-xs-8 .col-sm-6
      </div>
      <div class="col-xs-4 col-sm-6">
        Level 2: .col-xs-4 .col-sm-6
      </div>
    </div>
  </div>
</div>
```
### ⑥、列排序
```html
<div class="row">
  <div class="col-md-9 col-md-push-3">.col-md-9 .col-md-push-3</div>
  <div class="col-md-3 col-md-pull-9">.col-md-3 .col-md-pull-9</div>
</div>
```
## 5、排版
### ①、标题
HTML 中的所有标题标签，<h1> 到 <h6> 均可使用。另外，还提供了 .h1 到 .h6 类，为的是给内联（inline）属性的文本赋予标题的样式。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672010724-9106f205-52a7-42c6-8e86-d39cc5063461.png#clientId=u5fc7af02-33a9-4&from=paste&height=418&id=u42159fb0&name=image.png&originHeight=418&originWidth=859&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32499&status=done&style=stroke&taskId=u4f389290-feba-4c81-9968-135efede995&title=&width=859)
```html
<h1>h1. Bootstrap heading</h1>
<h2>h2. Bootstrap heading</h2>
<h3>h3. Bootstrap heading</h3>
<h4>h4. Bootstrap heading</h4>
<h5>h5. Bootstrap heading</h5>
<h6>h6. Bootstrap heading</h6>
```

---

在标题内还可以包含 <small> 标签或赋予 .small 类的元素，可以用来标记副标题。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672030793-a42b3d56-40f7-4fa5-a957-788119a6e04b.png#clientId=u5fc7af02-33a9-4&from=paste&height=406&id=u411ecab8&name=image.png&originHeight=406&originWidth=859&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36734&status=done&style=stroke&taskId=u57af8ae0-3994-4a7c-b8ce-69c2869d27c&title=&width=859)
```html
<h1>h1. Bootstrap heading <small>Secondary text</small></h1>
<h2>h2. Bootstrap heading <small>Secondary text</small></h2>
<h3>h3. Bootstrap heading <small>Secondary text</small></h3>
<h4>h4. Bootstrap heading <small>Secondary text</small></h4>
<h5>h5. Bootstrap heading <small>Secondary text</small></h5>
<h6>h6. Bootstrap heading <small>Secondary text</small></h6>
```
### ②、页面主体
#### Ⅰ、页面主体
Bootstrap 将全局 font-size 设置为 **14px**，line-height 设置为 **1.428**。这些属性直接赋予 <body> 元素和所有段落元素。另外，<p> （段落）元素还被设置了等于 1/2 行高（即 10px）的底部外边距（margin）。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672127221-cc67213f-e87f-4bb7-90f8-4cd6a178a3e5.png#clientId=u5fc7af02-33a9-4&from=paste&height=272&id=ud9d22d9b&name=image.png&originHeight=272&originWidth=855&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23873&status=done&style=stroke&taskId=u0825eb07-b752-460e-8fec-478ee729548&title=&width=855)
#### Ⅱ、中心内容
通过添加 .lead 类可以让段落突出显示。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672159756-28f555b3-841e-4dcb-9bf1-46ded3f2798b.png#clientId=u5fc7af02-33a9-4&from=paste&height=170&id=ue75608dd&name=image.png&originHeight=170&originWidth=861&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16256&status=done&style=stroke&taskId=ub1c9157f-7a8c-4728-bf40-517828884f3&title=&width=861)
#### Ⅲ、使用 Less 工具构建
**variables.less** 文件中定义的两个 Less 变量决定了排版尺寸：@font-size-base 和 @line-height-base。第一个变量定义了全局 font-size 基准，第二个变量是 line-height 基准。我们使用这些变量和一些简单的公式计算出其它所有页面元素的 margin、 padding 和 line-height。自定义这些变量即可改变 Bootstrap 的默认样式
### ③、内联文本元素
#### Ⅰ、标记的文本
由于文本在另一个上下文中的相关性，要突出显示一系列文本，请使用标记 <mark>
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672315025-282df35c-7a34-42d9-a336-f64c4a6fecde.png#clientId=u5fc7af02-33a9-4&from=paste&height=135&id=udab48dc6&name=image.png&originHeight=135&originWidth=863&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7785&status=done&style=stroke&taskId=u2263ca13-cbc1-4df4-baa6-9e0e3f407d0&title=&width=863)
```html
You can use the mark tag to <mark>highlight</mark> text.
```
#### Ⅱ、被删除的文本
对于被删除的文本使用 <del> 标签
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672359189-463bb143-479c-4f50-8c1f-07452c0d3d1b.png#clientId=u5fc7af02-33a9-4&from=paste&height=131&id=u421c5b56&name=image.png&originHeight=131&originWidth=861&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7670&status=done&style=stroke&taskId=ue115f6b6-93c0-469c-aa57-c556a46bbb4&title=&width=861)
```html
<del>This line of text is meant to be treated as deleted text.</del>
```
#### Ⅲ、无用文本
对于没用的文本使用 <s> 标签
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672409215-015e3d4e-1c15-4a78-9669-826eb94d6401.png#clientId=u5fc7af02-33a9-4&from=paste&height=130&id=u850e6211&name=image.png&originHeight=130&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7558&status=done&style=stroke&taskId=u78e22ff8-0340-4b89-bcf2-4c7567d9099&title=&width=857)
```html
<s>This line of text is meant to be treated as no longer accurate.</s>
```
#### Ⅳ、插入文本
额外插入的文本使用 <ins> 标签。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672466021-f57d2c0e-247f-4bee-9bb0-7d0097e5a492.png#clientId=u5fc7af02-33a9-4&from=paste&height=132&id=u3af66cb5&name=image.png&originHeight=132&originWidth=856&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8165&status=done&style=stroke&taskId=ubbddcc24-798b-4644-8bb0-e3c6ed14efa&title=&width=856)
```html
<ins>This line of text is meant to be treated as an addition to the document.</ins>
```
#### Ⅴ、带下划线的文本
为文本添加下划线，使用 <u> 标签
利用 HTML 自带的表示强调意味的标签来为文本增添少量样式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672515498-8a05867e-79d6-4558-b7c9-7daa4ac9bb3b.png#clientId=u5fc7af02-33a9-4&from=paste&height=134&id=u0c3b43f2&name=image.png&originHeight=134&originWidth=858&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6618&status=done&style=stroke&taskId=u34d381cc-a0d7-4dc4-bcee-dbcaf0d8a91&title=&width=858)
```html
<u>This line of text will render as underlined</u>
```
#### Ⅵ、小号文本
对于不需要强调的inline或block类型的文本，使用 <small> 标签包裹，其内的文本将被设置为父容器字体大小的 85%。标题元素中嵌套的 <small> 元素被设置不同的 font-size 。
你还可以为行内元素赋予 .small 类以代替任何 <small> 元素
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672575753-e6376af4-b593-439f-b3f6-f77921b70dda.png#clientId=u5fc7af02-33a9-4&from=paste&height=128&id=ud6671b1d&name=image.png&originHeight=128&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7403&status=done&style=stroke&taskId=ub14ecd05-7384-485e-9913-4bb45c5ff5e&title=&width=857)
```html
<small>This line of text is meant to be treated as fine print.</small>
```
#### Ⅶ、着重
通过增加 font-weight 值强调一段文本
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672656931-97f1efbc-e779-43bc-8e79-7659661c927e.png#clientId=u5fc7af02-33a9-4&from=paste&height=132&id=u058b6718&name=image.png&originHeight=132&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7516&status=done&style=stroke&taskId=ua32804eb-fee0-4506-b1a3-4372e65f195&title=&width=860)
```html
<strong>rendered as bold text</strong>
```
#### Ⅷ、斜体
用斜体强调一段文本
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672692650-9e5ca7c9-8e8c-478d-a37e-9307c5a519fa.png#clientId=u5fc7af02-33a9-4&from=paste&height=133&id=ue3dc062a&name=image.png&originHeight=133&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7606&status=done&style=stroke&taskId=uaf096e5c-933d-48a8-8e92-bbb32f76441&title=&width=857)
```html
<em>rendered as italicized text</em>
```
#### Ⅸ、注意
在 HTML5 中可以放心使用 <b> 和 <i> 标签。<b> 用于高亮单词或短语，不带有任何着重的意味；而 <i> 标签主要用于发言、技术词汇等
### ④、对齐
通过文本对齐类，可以简单方便的将文字重新对齐
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672778060-b49501ea-6fdf-4fed-9b7e-221bc26ce5e1.png#clientId=u5fc7af02-33a9-4&from=paste&height=203&id=u1ca0aa49&name=image.png&originHeight=206&originWidth=849&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7416&status=done&style=stroke&taskId=u4fb58b9d-ac66-43f5-83fc-2bccadc73c3&title=&width=836)
```html
<p class="text-left">Left aligned text.</p>
<p class="text-center">Center aligned text.</p>
<p class="text-right">Right aligned text.</p>
<p class="text-justify">Justified text.</p>
<p class="text-nowrap">No wrap text.</p>
```
### ⑤、改变大小写
通过这几个类可以改变文本的大小写
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672844543-83438779-93c9-4ed0-96bf-7413a916514a.png#clientId=u5fc7af02-33a9-4&from=paste&height=96&id=u15b2a294&name=image.png&originHeight=96&originWidth=157&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3049&status=done&style=stroke&taskId=u0d492b80-e688-45a8-a82f-2cd8e431d48&title=&width=157)
```html
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">Capitalized text.</p>
```
### ⑥、缩略语
当鼠标悬停在缩写和缩写词上时就会显示完整内容，Bootstrap 实现了对 HTML 的 <abbr> 元素的增强样式。缩略语元素带有 title 属性，外观表现为带有较浅的虚线框，鼠标移至上面时会变成带有“问号”的指针。如想看完整的内容可把鼠标悬停在缩略语上（对使用辅助技术的用户也可见）, 但需要包含 title 属性
#### Ⅰ、基本缩略语
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672912286-8e1ad0da-d325-4650-aec1-963fefd5fdf3.png#clientId=u5fc7af02-33a9-4&from=paste&height=35&id=u7036285b&name=image.png&originHeight=35&originWidth=274&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2149&status=done&style=stroke&taskId=u165beee4-acc9-4a11-9a03-f57a78dd289&title=&width=274)
```html
<abbr title="attribute">attr</abbr>
```
#### Ⅱ、首字母缩略语
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672931226-121f090e-7a34-4a6d-bef2-6f29c18fe71f.png#clientId=u5fc7af02-33a9-4&from=paste&height=34&id=u022f0f8e&name=image.png&originHeight=34&originWidth=271&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1857&status=done&style=stroke&taskId=u622c95e3-bd77-49ed-b582-f8b42a65817&title=&width=271)
```html
<abbr title="HyperText Markup Language" class="initialism">HTML</abbr>
```
### ⑦、地址
让联系信息以最接近日常使用的格式呈现。在每行结尾添加 <br> 可以保留需要的样式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657672978794-d7a4acd7-c886-4a82-885b-0a21030d87fe.png#clientId=u5fc7af02-33a9-4&from=paste&height=159&id=ua85711bf&name=image.png&originHeight=159&originWidth=207&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6829&status=done&style=stroke&taskId=ua717a99d-a66e-42a3-9659-b6bc2c39a11&title=&width=207)
```html
<address>
  <strong>Twitter, Inc.</strong><br>
  1355 Market Street, Suite 900<br>
  San Francisco, CA 94103<br>
  <abbr title="Phone">P:</abbr> (123) 456-7890
</address>

<address>
  <strong>Full Name</strong><br>
  <a href="mailto:#">first.last@example.com</a>
</address>
```
### ⑧、引用
在你的文档中引用其他来源的内容
#### Ⅰ、默认样式的引用
将任何 HTML 元素包裹在 <blockquote> 中即可表现为引用样式。对于直接引用，我们建议用 <p> 标签
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673064231-f7de8f45-5e06-4d75-8b5b-d9eeba1fe805.png#clientId=u5fc7af02-33a9-4&from=paste&height=63&id=ua6b251db&name=image.png&originHeight=63&originWidth=682&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6774&status=done&style=stroke&taskId=uebd6e7cf-d21e-442b-8b65-e75e2bfffab&title=&width=682)
```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
</blockquote>
```
#### Ⅱ、多种引用样式
对于标准样式的 <blockquote>，可以通过几个简单的变体就能改变风格和内容
##### （1）、命名来源
添加 <footer> 用于标明引用来源。来源的名称可以包裹进 <cite>标签中
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673155799-6f283248-96ba-495b-8bf3-dc217a8ee007.png#clientId=u5fc7af02-33a9-4&from=paste&height=91&id=uf00b8755&name=image.png&originHeight=91&originWidth=687&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8977&status=done&style=stroke&taskId=u98731bb0-eec3-46fd-97be-1e1cc524a73&title=&width=687)
```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
```
##### （2）、另一种展示风格
通过赋予 .blockquote-reverse 类可以让引用呈现内容右对齐的效果
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673201137-59578485-c380-4811-bd7b-c0f00bf9c69c.png#clientId=u5fc7af02-33a9-4&from=paste&height=92&id=u78825e9a&name=image.png&originHeight=92&originWidth=694&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9343&status=done&style=stroke&taskId=ubf70e52e-b8a7-409f-b72b-4a97858ea63&title=&width=694)
```html
<blockquote class="blockquote-reverse">
  ...
</blockquote>
```
### ⑨、列表
#### Ⅰ、无序列表
排列顺序_无关紧要_的一列元素
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673281791-e5621df0-353e-4d3c-a8bd-1e7c73a4c54a.png#clientId=u5fc7af02-33a9-4&from=paste&height=279&id=u7e398927&name=image.png&originHeight=279&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13697&status=done&style=stroke&taskId=uad18ebe0-5ec7-492f-ab25-1065f9a0a71&title=&width=300)
```html
<ul>
  <li>...</li>
</ul>
```
#### Ⅱ、有序列表
顺序_至关重要_的一组元素
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673316759-7c0d6d2e-c41d-4a29-9132-66e715cb2da9.png#clientId=u5fc7af02-33a9-4&from=paste&height=202&id=uc7639ab1&name=image.png&originHeight=202&originWidth=278&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10051&status=done&style=stroke&taskId=u0c8f047f-5da5-4c8b-b9da-5e85cf0ca94&title=&width=278)
```html
<ol>
  <li>...</li>
</ol>
```
#### Ⅲ、无样式列表
移除了默认的 list-style 样式和左侧外边距的一组元素（只针对直接子元素）。**这是针对直接子元素的**，也就是说，你需要对所有嵌套的列表都添加这个类才能具有同样的样式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673352087-4e92fb76-97ab-4155-9639-18372a88a5d1.png#clientId=u5fc7af02-33a9-4&from=paste&height=279&id=u5ccdef63&name=image.png&originHeight=279&originWidth=305&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13526&status=done&style=stroke&taskId=ubfd9f352-0f60-46d5-8008-5492ae84700&title=&width=305)
```html
<ul class="list-unstyled">
  <li>...</li>
</ul>
```
#### Ⅳ、内联列表
通过设置 display: inline-block; 并添加少量的内补（padding），将所有元素放置于同一行
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673384988-4f9fe9c5-255d-4e9c-bbf5-5b498f72f568.png#clientId=u5fc7af02-33a9-4&from=paste&height=30&id=u314f7497&name=image.png&originHeight=30&originWidth=320&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2095&status=done&style=stroke&taskId=u822041c5-ebbb-4987-876a-239bf9d82b8&title=&width=320)
```html
<ul class="list-inline">
  <li>...</li>
</ul>
```
#### Ⅴ、描述
带有描述的短语列表
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673416587-1f98df41-7a92-4526-8ec7-d52fd7515e6c.png#clientId=u5fc7af02-33a9-4&from=paste&height=184&id=u5b957b04&name=image.png&originHeight=184&originWidth=509&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12295&status=done&style=stroke&taskId=u077f6501-1361-4b33-85d5-247b6fb8301&title=&width=509)
```html
<dl>
  <dt>...</dt>
  <dd>...</dd>
</dl>
```
#### Ⅵ、水平排列的描述
.dl-horizontal 可以让 <dl> 内的短语及其描述排在一行。开始是像 <dl> 的默认样式堆叠在一起，随着导航条逐渐展开而排列在一行
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673452110-556b7670-d38e-4a4e-a0eb-bd6e33092ed2.png#clientId=u5fc7af02-33a9-4&from=paste&height=165&id=ua9e417a7&name=image.png&originHeight=165&originWidth=827&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16612&status=done&style=stroke&taskId=ubaae7fb7-fb54-484d-ab6d-fe5b7dc8a14&title=&width=827)
```html
<dl class="dl-horizontal">
  <dt>...</dt>
  <dd>...</dd>
</dl>
```
#### Ⅶ、自动截断
通过 text-overflow 属性，水平排列的描述列表将会截断左侧太长的短语。在较窄的视口（viewport）内，列表将变为默认堆叠排列的布局方式
## 6、代码
### ①、内联代码
通过 <code> 标签包裹内联样式的代码片段
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673666384-51246cd7-da1d-4893-81fb-f837ba8bebfd.png#clientId=u5fc7af02-33a9-4&from=paste&height=36&id=u0948b142&name=image.png&originHeight=36&originWidth=355&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2864&status=done&style=stroke&taskId=uc0850f62-0c87-47da-9966-3418753d508&title=&width=355)
```html
For example, <code>&lt;section&gt;</code> should be wrapped as inline.
```
### ②、用户输入
通过 <kbd> 标签标记用户通过键盘输入的内容
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673701341-032fbf2e-c5f0-4ec3-9fdb-7dc30d787252.png#clientId=u5fc7af02-33a9-4&from=paste&height=56&id=u7ec6baef&name=image.png&originHeight=56&originWidth=436&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4891&status=done&style=stroke&taskId=ue9896f7b-9123-491f-8057-aab1605bbfc&title=&width=436)
```html
To switch directories, type <kbd>cd</kbd> followed by the name of the directory.<br>
To edit settings, press <kbd><kbd>ctrl</kbd> + <kbd>,</kbd></kbd>
```
### ③、代码块
多行代码可以使用 <pre> 标签。为了正确的展示代码，注意将尖括号做转义处理
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673734681-b8b0a68e-a8fb-486f-9a27-fdf1b32fa43a.png#clientId=u5fc7af02-33a9-4&from=paste&height=87&id=u9fb87186&name=image.png&originHeight=87&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2991&status=done&style=stroke&taskId=ue872d3dd-2f3b-4b95-a237-98c494ce519&title=&width=831)
```html
<pre>&lt;p&gt;Sample text here...&lt;/p&gt;</pre>
```
### ④、变量
通过 <var> 标签标记变量
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673772203-3da779ed-94f1-44f5-810f-c0c9ea2fd188.png#clientId=u5fc7af02-33a9-4&from=paste&height=37&id=uba919424&name=image.png&originHeight=37&originWidth=96&originalType=binary&ratio=1&rotation=0&showTitle=false&size=880&status=done&style=stroke&taskId=u30cfb139-c523-4715-b1f3-b6a891289a3&title=&width=96)
```html
<var>y</var> = <var>m</var><var>x</var> + <var>b</var>
```
### ⑤、程序输出
通过 <samp> 标签来标记程序输出的内容
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673810356-c15c6cdb-ba84-4aab-bea7-fb1a9d4c7323.png#clientId=u5fc7af02-33a9-4&from=paste&height=35&id=ud0515733&name=image.png&originHeight=35&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2772&status=done&style=stroke&taskId=ue09ac63c-7fbc-4613-9d42-78b4c8471ae&title=&width=581)
```html
<samp>This text is meant to be treated as sample output from a computer program.</samp>
```
## 7、表格
### ①、基本实例
为任意 <table> 标签添加 .table 类可以为其赋予基本的样式 — 少量的内补（padding）和水平方向的分隔线。这种方式看起来很多余！？但是我们觉得，表格元素使用的很广泛，如果我们为其赋予默认样式可能会影响例如日历和日期选择之类的插件，所以我们选择将此样式独立出来
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673931945-9418cf2e-8dd9-4b6a-8773-d7043f673712.png#clientId=u5fc7af02-33a9-4&from=paste&height=154&id=u3914e033&name=image.png&originHeight=154&originWidth=829&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6924&status=done&style=stroke&taskId=u81e19bb4-c1e5-4e22-89d8-37912086c3e&title=&width=829)
```html
<table class="table">
  ...
</table>
```
### ②、条纹状表格
通过 .table-striped 类可以给 <tbody> 之内的每一行增加斑马条纹样式
跨浏览器兼容性：条纹状表格是依赖 :nth-child CSS 选择器实现的，而这一功能不被 Internet Explorer 8 支持
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657673988476-f5efa7b7-e410-479a-8a5b-818931508d46.png#clientId=u5fc7af02-33a9-4&from=paste&height=156&id=ua4f126a9&name=image.png&originHeight=156&originWidth=823&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7245&status=done&style=stroke&taskId=u6ea79fd3-d405-400f-9566-47302b8dbeb&title=&width=823)
```html
<table class="table table-striped">
  ...
</table>
```
### ③、带边框的表格
添加 .table-bordered 类为表格和其中的每个单元格增加边框
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674042605-b473cb60-0ad1-4ee0-a0ab-4fb5e4f16885.png#clientId=u5fc7af02-33a9-4&from=paste&height=162&id=u833e1305&name=image.png&originHeight=162&originWidth=825&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7234&status=done&style=stroke&taskId=uf452364e-5d1f-40f3-adee-e6269a5fecf&title=&width=825)
```html
<table class="table table-bordered">
  ...
</table>
```
### ④、鼠标悬停
通过添加 .table-hover 类可以让 <tbody> 中的每一行对鼠标悬停状态作出响应
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674117818-b1ffb8cd-c1fa-4a9d-b7cf-517fef9c76cb.png#clientId=u5fc7af02-33a9-4&from=paste&height=170&id=u90d38c1a&name=image.png&originHeight=170&originWidth=824&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7358&status=done&style=stroke&taskId=u27739512-62e8-4308-a2a6-850d2232cc5&title=&width=824)
```html
<table class="table table-hover">
  ...
</table>
```
### ⑤、紧缩表格
通过添加 .table-condensed 类可以让表格更加紧凑，单元格中的内补（padding）均会减半
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674155019-ed97c78b-924e-4c49-af70-07f5d4c7ac81.png#clientId=u5fc7af02-33a9-4&from=paste&height=127&id=ufddcccfa&name=image.png&originHeight=127&originWidth=824&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6472&status=done&style=stroke&taskId=u4de28202-5be6-491f-a06d-37038492beb&title=&width=824)
```html
<table class="table table-condensed">
  ...
</table>
```
### ⑥、状态类
通过这些状态类可以为行或单元格设置颜色
向使用辅助技术的用户传达用意：通过为表格中的一行或一个单元格添加颜色而赋予不同的意义只是提供了一种视觉上的表现，并不能为使用辅助技术 -- 例如屏幕阅读器 -- 浏览网页的用户提供更多信息。因此，请确保通过颜色而赋予的不同意义可以通过内容本身来表达（即在相应行或单元格中的可见的文本内容）；或者通过包含额外的方式 -- 例如应用了 .sr-only 类而隐藏的文本 -- 来表达出来

| Class | 描述 |
| --- | --- |
| .active | 鼠标悬停在行或单元格上时所设置的颜色 |
| .success | 标识成功或积极的动作 |
| .info | 标识普通的提示信息或动作 |
| .warning | 标识警告或需要用户注意 |
| .danger | 标识危险或潜在的带来负面影响的动作 |

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674238733-c966b61b-4ed3-4c1a-8436-0bda24ba59fe.png#clientId=u5fc7af02-33a9-4&from=paste&height=373&id=ude808511&name=image.png&originHeight=373&originWidth=826&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24090&status=done&style=stroke&taskId=u2301c51c-bd0a-45d1-b66a-a33d2c95c81&title=&width=826)
```html
<!-- On rows -->
<tr class="active">...</tr>
<tr class="success">...</tr>
<tr class="warning">...</tr>
<tr class="danger">...</tr>
<tr class="info">...</tr>

<!-- On cells (`td` or `th`) -->
<tr>
  <td class="active">...</td>
  <td class="success">...</td>
  <td class="warning">...</td>
  <td class="danger">...</td>
  <td class="info">...</td>
</tr>
```
### ⑦、响应式表格
将任何 .table 元素包裹在 .table-responsive 元素内，即可创建响应式表格，其会在小屏幕设备上（小于768px）水平滚动。当屏幕大于 768px 宽度时，水平滚动条消失
垂直方向的内容截断：响应式表格使用了 overflow-y: hidden 属性，这样就能将超出表格底部和顶部的内容截断。特别是，也可以截断下拉菜单和其他第三方组件
Firefox 和 fieldset 元素：Firefox 浏览器对 fieldset 元素设置了一些影响 width 属性的样式，导致响应式表格出现问题。可以使用下面提供的针对 Firefox 的 hack 代码解决，但是以下代码并未集成在 Bootstrap 中：@-moz-document url-prefix() {   fieldset { display: table-cell; } }

- 小于 768px 宽度

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674355602-e9528f47-e09c-41c3-965c-e6128b5dc71d.png#clientId=u5fc7af02-33a9-4&from=paste&height=182&id=u7efc9261&name=image.png&originHeight=182&originWidth=468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6681&status=done&style=stroke&taskId=u9258ec96-3064-4554-b486-1cc91a22448&title=&width=468)

- 大于 768px 宽度

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674457551-4123036b-7c2f-44d2-8c0d-b7453be19dc2.png#clientId=u5fc7af02-33a9-4&from=paste&height=170&id=u2088faae&name=image.png&originHeight=170&originWidth=832&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10302&status=done&style=stroke&taskId=u392cfe9b-834a-4da3-9163-d2131c5ea2e&title=&width=832)
```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>
```
## 8、表单
### ①、基本实例
单独的表单控件会被自动赋予一些全局样式。所有设置了 .form-control 类的 <input>、<textarea> 和 <select> 元素都将被默认设置宽度属性为 width: 100%;。 将 label 元素和前面提到的控件包裹在 .form-group 中可以获得最好的排列
不要将表单组和输入框组混合使用：不要将表单组直接和[输入框组](https://v3.bootcss.com/components/#input-groups)混合使用。建议将输入框组嵌套到表单组中使用
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674536099-d0a18e05-c76e-43a2-bb1d-872a53cac729.png#clientId=u5fc7af02-33a9-4&from=paste&height=316&id=u1691c896&name=image.png&originHeight=316&originWidth=832&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12067&status=done&style=stroke&taskId=u0fe2fbc5-1ba5-411f-83ab-a43db485a22&title=&width=832)
```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
```
### ②、内联表单
为 <form> 元素添加 .form-inline 类可使其内容左对齐并且表现为 inline-block 级别的控件。**只适用于视口（viewport）至少在 768px 宽度时（视口宽度再小的话就会使表单折叠）**
> 可能需要手动设置宽度：在 Bootstrap 中，输入框和单选/多选框控件默认被设置为 width: 100%; 宽度。在内联表单，我们将这些元素的宽度设置为 width: auto;，因此，多个控件可以排列在同一行。根据你的布局需求，可能需要一些额外的定制化组件.

> 一定要添加 label 标签：如果你没有为每个输入控件设置 label 标签，屏幕阅读器将无法正确识别。对于这些内联表单，你可以通过为 label 设置 .sr-only 类将其隐藏。还有一些辅助技术提供label标签的替代方案，比如 aria-label、aria-labelledby 或 title 属性。如果这些都不存在，屏幕阅读器可能会采取使用 placeholder 属性，如果存在的话，使用占位符来替代其他的标记，但要注意，这种方法是不妥当的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674689915-cc4f214b-899a-4001-b339-8a1ed9c04f8e.png#clientId=u5fc7af02-33a9-4&from=paste&height=52&id=u75495a1a&name=image.png&originHeight=52&originWidth=622&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4531&status=done&style=stroke&taskId=ube23b37e-6ee9-429e-8443-a7612b8cd67&title=&width=622)
```html
<form class="form-inline">
  <div class="form-group">
    <label for="exampleInputName2">Name</label>
    <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">Email</label>
    <input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
  </div>
  <button type="submit" class="btn btn-default">Send invitation</button>
</form>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674702914-0ac31f1c-c6b5-496c-a66f-dab4710e0ba3.png#clientId=u5fc7af02-33a9-4&from=paste&height=47&id=u7645b346&name=image.png&originHeight=47&originWidth=613&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3480&status=done&style=stroke&taskId=u0a4d6875-d8fa-4bc4-9fe8-10b5ee2fae2&title=&width=613)
```html
<form class="form-inline">
  <div class="form-group">
    <label class="sr-only" for="exampleInputEmail3">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail3" placeholder="Email">
  </div>
  <div class="form-group">
    <label class="sr-only" for="exampleInputPassword3">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword3" placeholder="Password">
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Remember me
    </label>
  </div>
  <button type="submit" class="btn btn-default">Sign in</button>
</form>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674713148-47c3bf06-1d98-4963-9b89-5f4b5821a0ed.png#clientId=u5fc7af02-33a9-4&from=paste&height=51&id=u7dca3bbe&name=image.png&originHeight=51&originWidth=407&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2773&status=done&style=stroke&taskId=u902f5a9d-a548-4dc9-b1fa-fac1665621c&title=&width=407)
```html
<form class="form-inline">
  <div class="form-group">
    <label class="sr-only" for="exampleInputAmount">Amount (in dollars)</label>
    <div class="input-group">
      <div class="input-group-addon">$</div>
      <input type="text" class="form-control" id="exampleInputAmount" placeholder="Amount">
      <div class="input-group-addon">.00</div>
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Transfer cash</button>
</form>
```
### ③、水平排列的表单
通过为表单添加 .form-horizontal 类，并联合使用 Bootstrap 预置的栅格类，可以将 label 标签和控件组水平并排布局。这样做将改变 .form-group 的行为，使其表现为栅格系统中的行（row），因此就无需再额外添加 .row 了
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674811363-52d8f735-9c62-4afd-b4a3-e19aeab499db.png#clientId=u5fc7af02-33a9-4&from=paste&height=201&id=uc34dee81&name=image.png&originHeight=201&originWidth=807&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6087&status=done&style=stroke&taskId=u530e3e63-cf12-474a-8dac-460827bea22&title=&width=807)
```html
<form class="form-horizontal">
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <div class="checkbox">
        <label>
          <input type="checkbox"> Remember me
        </label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-default">Sign in</button>
    </div>
  </div>
</form>
```
### ④、被支持的控件
表单布局实例中展示了其所支持的标准表单控件
#### Ⅰ、输入框
包括大部分表单控件、文本输入域控件，还支持所有 HTML5 类型的输入控件： text、password、datetime、datetime-local、date、month、time、week、number、email、url、search、tel 和 color
> 必须添加类型声明：只有正确设置了 type 属性的输入控件才能被赋予正确的样式

> 输入控件组：如需在文本输入域 <input> 前面或后面添加文本内容或按钮控件，请参考[输入控件组](https://v3.bootcss.com/components/#input-groups)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657674923656-053c8391-61cc-436f-8ae2-73acdd6be4ab.png#clientId=u5fc7af02-33a9-4&from=paste&height=55&id=u1c48b27e&name=image.png&originHeight=55&originWidth=832&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1464&status=done&style=stroke&taskId=u355bc280-a0d1-443c-90e7-f3eb0697ac6&title=&width=832)
```html
<input type="text" class="form-control" placeholder="Text input">
```
#### Ⅱ、文本域
支持多行文本的表单控件。可根据需要改变 rows 属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675047481-1a0ea96f-1c4f-4810-8cd2-f216f5bf0c8c.png#clientId=u5fc7af02-33a9-4&from=paste&height=94&id=ua4bdd26d&name=image.png&originHeight=94&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1718&status=done&style=stroke&taskId=ud9b240e5-e3dc-4e74-9ce5-fcfcf6bd16e&title=&width=830)
```html
<textarea class="form-control" rows="3"></textarea>
```
#### Ⅲ、多选和单选框
多选框（checkbox）用于选择列表中的一个或多个选项，而单选框（radio）用于从多个选项中只选择一个。
Disabled checkboxes and radios are supported, but to provide a "not-allowed" cursor on hover of the parent <label>, you'll need to add the .disabled class to the parent .radio, .radio-inline, .checkbox, or .checkbox-inline
##### （1）、默认外观（堆叠在一起）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675178405-01b6d4c1-2287-4c3a-9645-a1d2fe19fe69.png#clientId=u5fc7af02-33a9-4&from=paste&height=178&id=u8d80acd8&name=image.png&originHeight=178&originWidth=498&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12233&status=done&style=stroke&taskId=u44e9cee9-28d7-4824-a381-6f8406eab92&title=&width=498)
```html
<div class="checkbox">
  <label>
    <input type="checkbox" value="">
    Option one is this and that&mdash;be sure to include why it's great
  </label>
</div>
<div class="checkbox disabled">
  <label>
    <input type="checkbox" value="" disabled>
    Option two is disabled
  </label>
</div>

<div class="radio">
  <label>
    <input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>
    Option one is this and that&mdash;be sure to include why it's great
  </label>
</div>
<div class="radio">
  <label>
    <input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
    Option two can be something else and selecting it will deselect option one
  </label>
</div>
<div class="radio disabled">
  <label>
    <input type="radio" name="optionsRadios" id="optionsRadios3" value="option3" disabled>
    Option three is disabled
  </label>
</div>
```
##### （2）、内联单选和多选框
通过将 .checkbox-inline 或 .radio-inline 类应用到一系列的多选框（checkbox）或单选框（radio）控件上，可以使这些控件排列在一行
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675208876-0a14d8ff-2682-4168-8a82-254c6a05dfc7.png#clientId=u5fc7af02-33a9-4&from=paste&height=74&id=u8c213c5d&name=image.png&originHeight=74&originWidth=149&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1364&status=done&style=stroke&taskId=u028541db-58ba-4277-85bf-b8e772c3e23&title=&width=149)
```html
<label class="checkbox-inline">
  <input type="checkbox" id="inlineCheckbox1" value="option1"> 1
</label>
<label class="checkbox-inline">
  <input type="checkbox" id="inlineCheckbox2" value="option2"> 2
</label>
<label class="checkbox-inline">
  <input type="checkbox" id="inlineCheckbox3" value="option3"> 3
</label>

<label class="radio-inline">
  <input type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1"> 1
</label>
<label class="radio-inline">
  <input type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2"> 2
</label>
<label class="radio-inline">
  <input type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3"> 3
</label>
```
##### （3）、不带 label 文本的 Checkbox 和 radio
如果需要 <label> 内没有文字，输入框（input）正是你所期望的。 **目前只适用于非内联的 checkbox 和 radio。** 请记住，仍然需要为使用辅助技术的用户提供某种形式的 label（例如，使用 aria-label）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675237661-fbecd9d5-a45e-4d38-9d9b-ca6ade14ba42.png#clientId=u5fc7af02-33a9-4&from=paste&height=74&id=ud7265216&name=image.png&originHeight=74&originWidth=54&originalType=binary&ratio=1&rotation=0&showTitle=false&size=529&status=done&style=stroke&taskId=u237dea43-e27e-4156-8653-6a762539478&title=&width=54)
```html
<div class="checkbox">
  <label>
    <input type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
  </label>
</div>
<div class="radio">
  <label>
    <input type="radio" name="blankRadio" id="blankRadio1" value="option1" aria-label="...">
  </label>
</div>
```
#### Ⅳ、下拉列表（select）
注意，很多原生选择菜单 - 即在 Safari 和 Chrome 中 - 的圆角是无法通过修改 border-radius 属性来改变的
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675317450-7f8d6881-fbdc-4efc-88c4-75f895814f5e.png#clientId=u5fc7af02-33a9-4&from=paste&height=162&id=u2c164f60&name=image.png&originHeight=162&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6249&status=done&style=stroke&taskId=u2a64db64-d839-4580-aaab-f37fcf670cb&title=&width=830)
```html
<select class="form-control">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
  <option>5</option>
</select>
```

---

对于标记了 multiple 属性的 <select> 控件来说，默认显示多选项
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675341518-a1c7bae2-55cd-4e0e-b3a7-c8d1483f2a90.png#clientId=u5fc7af02-33a9-4&from=paste&height=101&id=uf07eed97&name=image.png&originHeight=101&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1694&status=done&style=stroke&taskId=ua803232f-8d84-489f-9832-8986d403cec&title=&width=830)
```html
<select multiple class="form-control">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
  <option>5</option>
</select>
```
### ⑤、静态控件
如果需要在表单中将一行纯文本和 label 元素放置于同一行，为 <p> 元素添加 .form-control-static 类即可
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675412259-804f2340-b004-4a57-bf6b-6d30754c903b.png#clientId=u5fc7af02-33a9-4&from=paste&height=108&id=ufb73021c&name=image.png&originHeight=108&originWidth=790&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4335&status=done&style=stroke&taskId=ud8e89021-8bff-435e-a480-26011aa2048&title=&width=790)
```html
<form class="form-horizontal">
  <div class="form-group">
    <label class="col-sm-2 control-label">Email</label>
    <div class="col-sm-10">
      <p class="form-control-static">email@example.com</p>
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword" class="col-sm-2 control-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword" placeholder="Password">
    </div>
  </div>
</form>
```

---

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675426925-6b231267-4573-4ee4-b041-a388f3a62761.png#clientId=u5fc7af02-33a9-4&from=paste&height=51&id=u1e67fc45&name=image.png&originHeight=51&originWidth=479&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3701&status=done&style=stroke&taskId=ude5ab873-5b86-4034-b5ad-3d39463882a&title=&width=479)
```html
<form class="form-inline">
  <div class="form-group">
    <label class="sr-only">Email</label>
    <p class="form-control-static">email@example.com</p>
  </div>
  <div class="form-group">
    <label for="inputPassword2" class="sr-only">Password</label>
    <input type="password" class="form-control" id="inputPassword2" placeholder="Password">
  </div>
  <button type="submit" class="btn btn-default">Confirm identity</button>
</form>
```
### ⑥、焦点状态
我们将某些表单控件的默认 outline 样式移除，然后对 :focus 状态赋予 box-shadow 属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675730008-f12ad40f-a25b-474d-b553-eec834b6cea3.png#clientId=u5fc7af02-33a9-4&from=paste&height=56&id=ub698383e&name=image.png&originHeight=56&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3338&status=done&style=stroke&taskId=ud3de907d-0197-4a42-9507-ed64217a558&title=&width=831)
> 演示:focus 状态：在本文档中，我们为上面实例中的输入框赋予了自定义的样式，用于演示 .form-control 元素的 :focus 状态

### ⑦、禁用状态
为输入框设置 disabled 属性可以禁止其与用户有任何交互（焦点、输入等）。被禁用的输入框颜色更浅，并且还添加了 not-allowed 鼠标状态
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675768903-c8418499-081a-4b94-985c-219857c3460f.png#clientId=u5fc7af02-33a9-4&from=paste&height=54&id=uebe8db22&name=image.png&originHeight=54&originWidth=832&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1977&status=done&style=stroke&taskId=u68b40f2e-96b0-4008-b781-b5f86f7c0c0&title=&width=832)
```html
<input class="form-control" id="disabledInput" type="text" placeholder="Disabled input here..." disabled>
```
### ⑧、被禁用的 fieldset
为<fieldset> 设置 disabled 属性,可以禁用 <fieldset> 中包含的所有控件
> <a> 标签的链接功能不受影响：默认情况下，浏览器会将 <fieldset disabled> 内所有的原生的表单控件（<input>、<select> 和 <button> 元素）设置为禁用状态，防止键盘和鼠标与他们交互。然而，如果表单中还包含 <a ... class="btn btn-*"> 元素，这些元素将只被赋予 pointer-events: none 属性。正如在关于 [禁用状态的按钮](https://v3.bootcss.com/css/#buttons-disabled) 章节中（尤其是关于锚点元素的子章节中）所描述的那样，该 CSS 属性尚不规范，并且在 Opera 18 及更低版本的浏览器或 Internet Explorer 11 总没有得到全面支持，并且不会阻止键盘用户能够获取焦点或激活这些链接。所以为了安全起见，建议使用自定义 JavaScript 来禁用这些链接

> 跨浏览器兼容性：虽然 Bootstrap 会将这些样式应用到所有浏览器上，Internet Explorer 11 及以下浏览器中的 <fieldset> 元素并不完全支持 disabled 属性。因此建议在这些浏览器上通过 JavaScript 代码来禁用 <fieldset>

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675824431-c9b994e5-fc06-4794-9d59-fe017b039e40.png#clientId=u5fc7af02-33a9-4&from=paste&height=228&id=u832b9011&name=image.png&originHeight=228&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8708&status=done&style=stroke&taskId=ub197c034-0ec4-47f8-ab4a-fd51b9e4c92&title=&width=831)
```html
<form>
  <fieldset disabled>
    <div class="form-group">
      <label for="disabledTextInput">Disabled input</label>
      <input type="text" id="disabledTextInput" class="form-control" placeholder="Disabled input">
    </div>
    <div class="form-group">
      <label for="disabledSelect">Disabled select menu</label>
      <select id="disabledSelect" class="form-control">
        <option>Disabled select</option>
      </select>
    </div>
    <div class="checkbox">
      <label>
        <input type="checkbox"> Can't check this
      </label>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>
```
### ⑨、只读状态
为输入框设置 readonly 属性可以禁止用户修改输入框中的内容。处于只读状态的输入框颜色更浅（就像被禁用的输入框一样），但是仍然保留标准的鼠标状态
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657675893777-4f97bb23-810f-4ab3-b63c-ca1614ac7c56.png#clientId=u5fc7af02-33a9-4&from=paste&height=46&id=u44878490&name=image.png&originHeight=46&originWidth=828&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1900&status=done&style=stroke&taskId=u3fb661d4-5c33-4033-8468-257e35ece82&title=&width=828)
```html
<input class="form-control" type="text" placeholder="Readonly input here…" readonly>
```
### ⑩、帮助文本
表单控件的块级帮助文本。
> 将帮助文本与表单控件关联：帮助文本应该使用 aria describedby 属性与表单控件显式关联。这将确保辅助技术（如屏幕阅读器）在用户聚焦或进入控件时会宣布此帮助文本

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676092313-538a793d-d043-40b0-af8a-e6a93d2bc342.png#clientId=u5fc7af02-33a9-4&from=paste&height=110&id=u02c0e6b7&name=image.png&originHeight=110&originWidth=824&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5467&status=done&style=stroke&taskId=u4c7ae96c-476c-4373-9053-352d28fc688&title=&width=824)
```html
<label for="inputHelpBlock">Input with help text</label>
<input type="text" id="inputHelpBlock" class="form-control" aria-describedby="helpBlock">
...
<span id="helpBlock" class="help-block">A block of help text that breaks onto a new line and may extend beyond one line.</span>
```
### ⑪、校验状态
Bootstrap 对表单控件的校验状态，如 error、warning 和 success 状态，都定义了样式。使用时，添加 .has-warning、.has-error 或 .has-success 类到这些控件的父元素即可。任何包含在此元素之内的 .control-label、.form-control 和 .help-block 元素都将接受这些校验状态的样式
> 向辅助设备和色盲用户传达验证状态：使用这些校验样式只是为表单控件提供一个可视的、基于色彩的提示，但是并不能将这种提示信息传达给使用辅助设备的用户 - 例如屏幕阅读器 - 或者色盲用户。
> 为了确保所有用户都能获取正确信息，Bootstrap 还提供了另一种提示方式。例如，你可以在表单控件的 <label> 标签上以文本的形式显示提示信息（就像下面代码中所展示的）；包含一个 [Glyphicon 字体图标](https://v3.bootcss.com/components/#glyphicons) （还有赋予 .sr-only 类的文本信息 - 参考[Glyphicon 字体图标实例](https://v3.bootcss.com/components/#glyphicons-examples)）；或者提供一个额外的 [辅助信息](https://v3.bootcss.com/css/#forms-help-text) 块。另外，对于使用辅助设备的用户，无效的表单控件还可以赋予一个 aria-invalid="true" 属性

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676148397-942f3ba7-827c-48d4-a37d-ab6275fce058.png#clientId=u5fc7af02-33a9-4&from=paste&height=337&id=u68247e37&name=image.png&originHeight=337&originWidth=833&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15097&status=done&style=stroke&taskId=u4249dac0-2940-4ab8-a688-21f4720a33e&title=&width=833)
```html
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">Input with success</label>
  <input type="text" class="form-control" id="inputSuccess1" aria-describedby="helpBlock2">
  <span id="helpBlock2" class="help-block">A block of help text that breaks onto a new line and may extend beyond one line.</span>
</div>
<div class="form-group has-warning">
  <label class="control-label" for="inputWarning1">Input with warning</label>
  <input type="text" class="form-control" id="inputWarning1">
</div>
<div class="form-group has-error">
  <label class="control-label" for="inputError1">Input with error</label>
  <input type="text" class="form-control" id="inputError1">
</div>
<div class="has-success">
  <div class="checkbox">
    <label>
      <input type="checkbox" id="checkboxSuccess" value="option1">
      Checkbox with success
    </label>
  </div>
</div>
<div class="has-warning">
  <div class="checkbox">
    <label>
      <input type="checkbox" id="checkboxWarning" value="option1">
      Checkbox with warning
    </label>
  </div>
</div>
<div class="has-error">
  <div class="checkbox">
    <label>
      <input type="checkbox" id="checkboxError" value="option1">
      Checkbox with error
    </label>
  </div>
</div>
```
#### Ⅰ、添加额外的图标
你还可以针对校验状态为输入框添加额外的图标。只需设置相应的 .has-feedback 类并添加正确的图标即可。
**反馈图标（feedback icon）只能使用在文本输入框 <input class="form-control"> 元素上**
> 图标、label 和输入控件组：对于不带有 label 标签的输入框以及右侧带有附加组件的[输入框组](https://v3.bootcss.com/components/#input-groups)，需要手动为其放置反馈图标。为了让所有用户都能访问你的网站，我们强烈建议为所有输入框添加 label 标签。如果你不希望将 label 标签展示出来，可以通过添加 .sr-only 类将其隐藏。如果的确不能添加 label 标签，请调整反馈图标的 top 值。对于输入框组，请根据附加组件的实际情况调整 right 值

> 向辅助技术设备传递图标的含义：为了确保辅助技术- 如屏幕阅读器 - 正确传达一个图标的含义，额外的隐藏的文本应包含在 .sr-only 类中，并明确关联使用了 aria-describedby 的表单控件。或者，以某些其他形式（例如，文本输入字段有一个特定的警告信息）传达含义，例如改变与表单控件实际相关联的 <label> 的文本。
> 虽然下面的例子已经提到各自表单控件本身的 <label> 文本的验证状态，上述技术（使用 .sr-only 文本 和 aria-describedby) ）已经包括了需要说明的目的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676266599-554192bd-9f16-4f87-a237-7e359b2ded39.png#clientId=u5fc7af02-33a9-4&from=paste&height=299&id=u3a658b8f&name=image.png&originHeight=299&originWidth=827&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9753&status=done&style=stroke&taskId=ud0661ac9-ca61-4818-ac5a-d8661d8d586&title=&width=827)
```html
<div class="form-group has-success has-feedback">
  <label class="control-label" for="inputSuccess2">Input with success</label>
  <input type="text" class="form-control" id="inputSuccess2" aria-describedby="inputSuccess2Status">
  <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
  <span id="inputSuccess2Status" class="sr-only">(success)</span>
</div>
<div class="form-group has-warning has-feedback">
  <label class="control-label" for="inputWarning2">Input with warning</label>
  <input type="text" class="form-control" id="inputWarning2" aria-describedby="inputWarning2Status">
  <span class="glyphicon glyphicon-warning-sign form-control-feedback" aria-hidden="true"></span>
  <span id="inputWarning2Status" class="sr-only">(warning)</span>
</div>
<div class="form-group has-error has-feedback">
  <label class="control-label" for="inputError2">Input with error</label>
  <input type="text" class="form-control" id="inputError2" aria-describedby="inputError2Status">
  <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span>
  <span id="inputError2Status" class="sr-only">(error)</span>
</div>
<div class="form-group has-success has-feedback">
  <label class="control-label" for="inputGroupSuccess1">Input group with success</label>
  <div class="input-group">
    <span class="input-group-addon">@</span>
    <input type="text" class="form-control" id="inputGroupSuccess1" aria-describedby="inputGroupSuccess1Status">
  </div>
  <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
  <span id="inputGroupSuccess1Status" class="sr-only">(success)</span>
</div>
```
#### Ⅱ、为水平排列的表单和内联表单设置可选的图标
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676335261-4e469907-0f85-4873-914c-2d129b2bf87a.png#clientId=u5fc7af02-33a9-4&from=paste&height=104&id=u45317298&name=image.png&originHeight=104&originWidth=816&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4988&status=done&style=stroke&taskId=ue178d5d7-46ce-41c9-ad57-e75174f4cb9&title=&width=816)
```html
<form class="form-horizontal">
  <div class="form-group has-success has-feedback">
    <label class="control-label col-sm-3" for="inputSuccess3">Input with success</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="inputSuccess3" aria-describedby="inputSuccess3Status">
      <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
      <span id="inputSuccess3Status" class="sr-only">(success)</span>
    </div>
  </div>
  <div class="form-group has-success has-feedback">
    <label class="control-label col-sm-3" for="inputGroupSuccess2">Input group with success</label>
    <div class="col-sm-9">
      <div class="input-group">
        <span class="input-group-addon">@</span>
        <input type="text" class="form-control" id="inputGroupSuccess2" aria-describedby="inputGroupSuccess2Status">
      </div>
      <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
      <span id="inputGroupSuccess2Status" class="sr-only">(success)</span>
    </div>
  </div>
</form>
```

---

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676366252-6f4d3ab7-f49a-4a0e-8858-4fbd6504c701.png#clientId=u5fc7af02-33a9-4&from=paste&height=102&id=ue5aeef27&name=image.png&originHeight=102&originWidth=459&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4686&status=done&style=stroke&taskId=u7c040321-1b23-4b0e-a383-83ac79bc9a9&title=&width=459)
```html
<form class="form-inline">
  <div class="form-group has-success has-feedback">
    <label class="control-label" for="inputSuccess4">Input with success</label>
    <input type="text" class="form-control" id="inputSuccess4" aria-describedby="inputSuccess4Status">
    <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
    <span id="inputSuccess4Status" class="sr-only">(success)</span>
  </div>
</form>
<form class="form-inline">
  <div class="form-group has-success has-feedback">
    <label class="control-label" for="inputGroupSuccess3">Input group with success</label>
    <div class="input-group">
      <span class="input-group-addon">@</span>
      <input type="text" class="form-control" id="inputGroupSuccess3" aria-describedby="inputGroupSuccess3Status">
    </div>
    <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
    <span id="inputGroupSuccess3Status" class="sr-only">(success)</span>
  </div>
</form>
```
#### Ⅲ、可选的图标与设置 .sr-only 类的 label
如果你使用 .sr-only 类来隐藏表单控件的 <label> （而不是使用其它标签选项，如 aria-label 属性）， 一旦它被添加，Bootstrap 会自动调整图标的位置
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676401999-77e9ae82-5134-4614-8d92-200413db10c2.png#clientId=u5fc7af02-33a9-4&from=paste&height=111&id=u8dc0fb13&name=image.png&originHeight=111&originWidth=832&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2269&status=done&style=stroke&taskId=uff279888-0747-479f-ae9f-ea078339855&title=&width=832)
```html
<div class="form-group has-success has-feedback">
  <label class="control-label sr-only" for="inputSuccess5">Hidden label</label>
  <input type="text" class="form-control" id="inputSuccess5" aria-describedby="inputSuccess5Status">
  <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
  <span id="inputSuccess5Status" class="sr-only">(success)</span>
</div>
<div class="form-group has-success has-feedback">
  <label class="control-label sr-only" for="inputGroupSuccess4">Input group with success</label>
  <div class="input-group">
    <span class="input-group-addon">@</span>
    <input type="text" class="form-control" id="inputGroupSuccess4" aria-describedby="inputGroupSuccess4Status">
  </div>
  <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
  <span id="inputGroupSuccess4Status" class="sr-only">(success)</span>
</div>
```
### ⑫、控件尺寸
通过 .input-lg 类似的类可以为控件设置高度，通过 .col-lg-* 类似的类可以为控件设置宽度
#### Ⅰ、高度尺寸
创建大一些或小一些的表单控件以匹配按钮尺寸
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676482262-60d561b7-72ef-4afb-901b-1196a8edcffa.png#clientId=u5fc7af02-33a9-4&from=paste&height=292&id=uf4ddd9bb&name=image.png&originHeight=292&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9290&status=done&style=stroke&taskId=ub5be8a12-f2c8-4ede-99d6-6a6fb10d042&title=&width=830)
```html
<input class="form-control input-lg" type="text" placeholder=".input-lg">
<input class="form-control" type="text" placeholder="Default input">
<input class="form-control input-sm" type="text" placeholder=".input-sm">

<select class="form-control input-lg">...</select>
<select class="form-control">...</select>
<select class="form-control input-sm">...</select>
```
#### Ⅱ、水平排列的表单组的尺寸
通过添加 .form-group-lg 或 .form-group-sm 类，为 .form-horizontal 包裹的 label 元素和表单控件快速设置尺寸
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676521971-cb5d5473-c34f-4c21-a641-0dc989a9b80c.png#clientId=u5fc7af02-33a9-4&from=paste&height=116&id=u7b30ab31&name=image.png&originHeight=116&originWidth=814&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5493&status=done&style=stroke&taskId=u4367b1d2-4dcc-4b2c-b7f3-9d2105cc79d&title=&width=814)
```html
<form class="form-horizontal">
  <div class="form-group form-group-lg">
    <label class="col-sm-2 control-label" for="formGroupInputLarge">Large label</label>
    <div class="col-sm-10">
      <input class="form-control" type="text" id="formGroupInputLarge" placeholder="Large input">
    </div>
  </div>
  <div class="form-group form-group-sm">
    <label class="col-sm-2 control-label" for="formGroupInputSmall">Small label</label>
    <div class="col-sm-10">
      <input class="form-control" type="text" id="formGroupInputSmall" placeholder="Small input">
    </div>
  </div>
</form>
```
#### Ⅲ、调整列（column）尺寸
用栅格系统中的列（column）包裹输入框或其任何父元素，都可很容易的为其设置宽度
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657676559992-83c48d3d-d968-494b-b3ad-3b3b3e20f2dd.png#clientId=u5fc7af02-33a9-4&from=paste&height=56&id=u79b3c26f&name=image.png&originHeight=56&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2371&status=done&style=stroke&taskId=ufc2fa4b0-9d46-4caa-a51e-051f2cfd781&title=&width=624)
```html
<div class="row">
  <div class="col-xs-2">
    <input type="text" class="form-control" placeholder=".col-xs-2">
  </div>
  <div class="col-xs-3">
    <input type="text" class="form-control" placeholder=".col-xs-3">
  </div>
  <div class="col-xs-4">
    <input type="text" class="form-control" placeholder=".col-xs-4">
  </div>
</div>
```
## 9、按钮
### ①、可作为按钮使用的标签或元素
为 <a>、<button> 或 <input> 元素添加按钮类（button class）即可使用 Bootstrap 提供的样式
> 针对组件的注意事项：虽然按钮类可以应用到 <a> 和 <button> 元素上，但是，导航和导航条组件只支持 <button> 元素

> 链接被作为按钮使用时的注意事项：如果 <a> 元素被作为按钮使用 -- 并用于在当前页面触发某些功能 -- 而不是用于链接其他页面或链接当前页面中的其他部分，那么，务必为其设置 role="button" 属性

> 跨浏览器展现：我们总结的最佳实践是：**强烈建议尽可能使用 <button> 元素**来获得在各个浏览器上获得相匹配的绘制效果。
> 另外，我们还发现了 [Firefox <30 版本的浏览器上出现的一个 bug](https://bugzilla.mozilla.org/show_bug.cgi?id=697451)，其表现是：阻止我们为基于 <input> 元素所创建的按钮设置 line-height 属性，这就导致在 Firefox 浏览器上不能完全和其他按钮保持一致的高度

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677480506-aa8d423a-1d1e-4b79-b714-f52ff70cd941.png#clientId=u5fc7af02-33a9-4&from=paste&height=56&id=u55c10736&name=image.png&originHeight=56&originWidth=281&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1918&status=done&style=stroke&taskId=uf8db4f33-360f-497a-937d-bfe67b9131f&title=&width=281)
```html
<a class="btn btn-default" href="#" role="button">Link</a>
<button class="btn btn-default" type="submit">Button</button>
<input class="btn btn-default" type="button" value="Input">
<input class="btn btn-default" type="submit" value="Submit">
```
### ②、预定义样式
使用下面列出的类可以快速创建一个带有预定义样式的按钮
> 向辅助技术传达意义：为按钮添加不同的颜色只是一种视觉上的信息表达方式，但是，对于使用辅助技术 -- 例如屏幕阅读器 -- 的用户来说，颜色是不可见的。建议，确保通过颜色表达的信息或者通过内容自身表达出来（按钮上的文字），或者通过其他方式 -- 例如通过 .sr-only 类隐藏的额外文本 -- 表达出来

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677553660-f0f23f5f-7620-4915-bbaa-1a229eb4b271.png#clientId=u5fc7af02-33a9-4&from=paste&height=99&id=u518f7ffb&name=image.png&originHeight=99&originWidth=748&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11166&status=done&style=stroke&taskId=uf77b0d3f-2b2d-4a99-950d-06c237f9018&title=&width=748)
```html
<!-- Standard button -->
<button type="button" class="btn btn-default">（默认样式）Default</button>

<!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
<button type="button" class="btn btn-primary">（首选项）Primary</button>

<!-- Indicates a successful or positive action -->
<button type="button" class="btn btn-success">（成功）Success</button>

<!-- Contextual button for informational alert messages -->
<button type="button" class="btn btn-info">（一般信息）Info</button>

<!-- Indicates caution should be taken with this action -->
<button type="button" class="btn btn-warning">（警告）Warning</button>

<!-- Indicates a dangerous or potentially negative action -->
<button type="button" class="btn btn-danger">（危险）Danger</button>

<!-- Deemphasize a button by making it look like a link while maintaining button behavior -->
<button type="button" class="btn btn-link">（链接）Link</button>
```
### ③、尺寸
需要让按钮具有不同尺寸吗？使用 .btn-lg、.btn-sm 或 .btn-xs 就可以获得不同尺寸的按钮
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677646741-0a091c2f-8d35-4ed1-9901-276cf8630854.png#clientId=u5fc7af02-33a9-4&from=paste&height=181&id=ufe509507&name=image.png&originHeight=181&originWidth=471&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17604&status=done&style=stroke&taskId=uca679b3f-2cc8-4fce-91dd-f176f97baf2&title=&width=471)
```html
<p>
  <button type="button" class="btn btn-primary btn-lg">（大按钮）Large button</button>
  <button type="button" class="btn btn-default btn-lg">（大按钮）Large button</button>
</p>
<p>
  <button type="button" class="btn btn-primary">（默认尺寸）Default button</button>
  <button type="button" class="btn btn-default">（默认尺寸）Default button</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-sm">（小按钮）Small button</button>
  <button type="button" class="btn btn-default btn-sm">（小按钮）Small button</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-xs">（超小尺寸）Extra small button</button>
  <button type="button" class="btn btn-default btn-xs">（超小尺寸）Extra small button</button>
</p>
```

---

通过给按钮添加 .btn-block 类可以将其拉伸至父元素100%的宽度，而且按钮也变为了块级（block）元素
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677664048-4013dc1c-40b3-44cb-a6e5-8f3f0e0dd148.png#clientId=u5fc7af02-33a9-4&from=paste&height=161&id=u989e8e68&name=image.png&originHeight=161&originWidth=433&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8644&status=done&style=stroke&taskId=u26abe5a5-0121-484a-8934-f51523a1f06&title=&width=433)
```html
<button type="button" class="btn btn-primary btn-lg btn-block">（块级元素）Block level button</button>
<button type="button" class="btn btn-default btn-lg btn-block">（块级元素）Block level button</button>
```
### ④、激活状态
当按钮处于激活状态时，其表现为被按压下去（底色更深、边框夜色更深、向内投射阴影）。对于 <button> 元素，是通过 :active 状态实现的。对于 <a> 元素，是通过 .active 类实现的。然而，你还可以将 .active 应用到 <button> 上（包含 aria-pressed="true" 属性)），并通过编程的方式使其处于激活状态
#### Ⅰ、button 元素
由于 :active 是伪状态，因此无需额外添加，但是在需要让其表现出同样外观的时候可以添加 .active 类
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677729082-cdb2bc1f-8f2c-4800-8905-5cd40d0957c8.png#clientId=u5fc7af02-33a9-4&from=paste&height=76&id=ubabb92de&name=image.png&originHeight=76&originWidth=257&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4100&status=done&style=stroke&taskId=u2c13ad57-144f-4043-ac08-340da1fa106&title=&width=257)
```html
<button type="button" class="btn btn-primary btn-lg active">Primary button</button>
<button type="button" class="btn btn-default btn-lg active">Button</button>
```
#### Ⅱ、链接（<a>）元素
可以为基于 <a> 元素创建的按钮添加 .active 类
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677765278-0e369952-f6f0-4044-9dba-271c4b738a91.png#clientId=u5fc7af02-33a9-4&from=paste&height=67&id=uba873562&name=image.png&originHeight=67&originWidth=215&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3090&status=done&style=stroke&taskId=ub4beeb5a-49c9-4116-a78a-164a010c58e&title=&width=215)
```html
<a href="#" class="btn btn-primary btn-lg active" role="button">Primary link</a>
<a href="#" class="btn btn-default btn-lg active" role="button">Link</a>
```
### ⑤、禁用状态
通过为按钮的背景设置 opacity 属性就可以呈现出无法点击的效果
#### Ⅰ、button 元素
为 <button> 元素添加 disabled 属性，使其表现出禁用状态
> 跨浏览器兼容性：如果为 <button> 元素添加 disabled 属性，Internet Explorer 9 及更低版本的浏览器将会把按钮中的文本绘制为灰色，并带有恶心的阴影，目前我们还没有解决办法

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677831823-5943b9f0-6a8e-48a2-9167-98f14ec17390.png#clientId=u5fc7af02-33a9-4&from=paste&height=70&id=u28fdb297&name=image.png&originHeight=70&originWidth=256&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3714&status=done&style=stroke&taskId=u97b6d3d8-835a-4618-87fe-aebca5c9aba&title=&width=256)
```html
<button type="button" class="btn btn-lg btn-primary" disabled="disabled">Primary button</button>
<button type="button" class="btn btn-default btn-lg" disabled="disabled">Button</button>
```
#### Ⅱ、链接（<a>）元素
为基于 <a> 元素创建的按钮添加 .disabled 类
我们把 .disabled 作为工具类使用，就像 .active 类一样，因此不需要增加前缀
> 链接的原始功能不受影响：上面提到的类只是通过设置 pointer-events: none 来禁止 <a> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。此外，即使在支持指针事件的浏览器中：无，键盘导航仍然不受影响，这意味着有视力的键盘用户和辅助技术用户仍然能够激活这些链接。 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657677909843-e3f6b7db-344f-4d25-b4ef-6de49cfcf396.png#clientId=u5fc7af02-33a9-4&from=paste&height=68&id=uab8d0fb5&name=image.png&originHeight=68&originWidth=217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2720&status=done&style=stroke&taskId=u570b9b9c-2f02-4089-8f01-da0aea3e29d&title=&width=217)
```html
<a href="#" class="btn btn-primary btn-lg disabled" role="button">Primary link</a>
<a href="#" class="btn btn-default btn-lg disabled" role="button">Link</a>
```
## 10、图片
## ①、响应式图片
在 Bootstrap 版本 3 中，通过为图片添加 .img-responsive 类可以让图片支持响应式布局。其实质是为图片设置了 max-width: 100%;、 height: auto; 和 display: block; 属性，从而让图片在其父元素中更好的缩放。
如果需要让使用了 .img-responsive 类的图片水平居中，请使用 .center-block 类，不要用 .text-center。 [请参考助手类章节](https://v3.bootcss.com/css/#helper-classes-center) 了解更多关于 .center-block 的用法
> SVG 图像和 IE 8-10：在 Internet Explorer 8-10 中，设置为 .img-responsive 的 SVG 图像显示出的尺寸不匀称。为了解决这个问题，在出问题的地方添加 width: 100% \9; 即可。Bootstrap 并没有自动为所有图像元素设置这一属性，因为这会导致其他图像格式出现错乱

```html
<img src="..." class="img-responsive" alt="Responsive image">
```
## ②、图片形状
通过为 <img> 元素添加以下相应的类，可以让图片呈现不同的形状
> 跨浏览器兼容性：请时刻牢记：Internet Explorer 8 不支持 CSS3 中的圆角属性

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1657678111731-807295e2-95df-4d22-b851-0ea42f0e7d49.png#clientId=u5fc7af02-33a9-4&from=paste&height=167&id=u5f801f1f&name=image.png&originHeight=167&originWidth=468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4255&status=done&style=stroke&taskId=u46a504f1-4568-4045-8e54-17223bb7222&title=&width=468)
```html
<img src="..." alt="..." class="img-rounded">
<img src="..." alt="..." class="img-circle">
<img src="..." alt="..." class="img-thumbnail">
```
## 11、辅助类
> [https://v3.bootcss.com/css/#helper-classes](https://v3.bootcss.com/css/#helper-classes)

## 12、响应式工具
> [https://v3.bootcss.com/css/#helper-classes](https://v3.bootcss.com/css/#helper-classes)

为了加快对移动设备友好的页面开发工作，利用媒体查询功能并使用这些工具类可以方便的针对不同设备展示或隐藏页面内容。另外还包含了针对打印机显示或隐藏内容的工具类。
有针对性的使用这类工具类，从而避免为同一个网站创建完全不同的版本。相反，通过使用这些工具类可以在不同设备上提供不同的展现形式。
## 13、使用 Less
> [https://v3.bootcss.com/css/#helper-classes](https://v3.bootcss.com/css/#helper-classes)

Bootstrap 的 CSS 文件是通过 Less 源码编译而来的。Less 是一门预处理语言，支持变量、mixin、函数等额外功能。对于希望使用 Less 源码而非编译而来的 CSS 文件的用户，Bootstrap 框架中包含的大量变量、mixin 将非常有价值。
针对栅格系统的变量和 mixin 包含在[栅格系统](https://v3.bootcss.com/css/#grid-less)章节
## 14、使用 Sass
虽然 Bootstrap 是基于 Less 构建的，我们还提供了一套[官方支持的 Sass 移植版](https://github.com/twbs/bootstrap-sass)代码。我们将这个版本放在单独的 GitHub 仓库中进行维护，并通过脚本处理源码更新
由于 Sass 移植版存放于单独的仓库，并针对不同的使用群体，这个项目中的内容与 Bootstrap 主项目有很大不同。这也是为了保证 Sass 移植版与更多基于 Sass 的系统相兼容

| 路径 | 描述 |
| --- | --- |
| lib/ | Ruby gem code (Sass configuration, Rails and Compass integrations) |
| tasks/ | Converter scripts (turning upstream Less to Sass) |
| test/ | Compilation tests |
| templates/ | Compass package manifest |
| vendor/assets/ | Sass, JavaScript, and font files |
| Rakefile | Internal tasks, such as rake and convert |

请访问 [Sass 移植版在 GitHub 上的仓库](https://github.com/twbs/bootstrap-sass) 来了解这些文件
# 三、
# 四、
# 五、
# 六、
# 七、
# 八、
# 九、
# 十、
# 十一、
# 十二、
# 十三、
# 十四、
# 十五、
# 十六、
# 十七、
# 十八、
# 十九、
# 二十、
