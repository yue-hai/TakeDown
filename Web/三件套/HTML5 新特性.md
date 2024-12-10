> [https://developer.aliyun.com/course/72](https://developer.aliyun.com/course/72) ，不好

# 一、音频
## 1、Audio(音频)

HTML.5 提供了播放音频文件的标准

## 2、control(控制器)

`control` 属性供添加播放、暂停和音量控件

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
    <audio src="./raw/Village People - YMCA.flac" controls="controls">123</audio>
</body>
</html>
```

![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--09-59-469--4CaFhR3jFC1caw.png)

## 3、标签

1. `<audio>`：定义声音
2. `<source>`：规定多媒体资源，可以是多个

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
    <audio controls="controls">
        <source src="./raw/Village People - YMCA.flac">
        <source src="./raw/Village People - YMCA.mp4">
        <source src="./raw/Village People - YMCA.ogg">
    </audio>
</body>
</html>
```

# 二、视频

## 1、Video(视频)

HTML .5 提供了展示视频的标准

## 2、control(控制器)

`control` 属性供添加播放、暂停和音量控件
## 3、标签:

1. `<video>`：定义声音
2. `<source>`：规定多媒体资源，可以是多个

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
    <video src="./raw/猫.mp4" controls="controls"></video>
</body>
</html>
```

## 4、属性:

1. `width`：宽
2. `height`：高

# 三、拖放

## 1、拖放：

拖放是一种常见的特性，即抓取对象以后拖到另一个位置。

## 2、浏览器支持：

Internet Explorer 9、Firefox、 Opera 12、Chrome 以及 Safari 5 支持拖放

## 3、设置元素为可拖放：

`draggable="true'`

## 4、拖动什么：

`ondragstart `和 `setData()`

## 5、放到何处：

`ondragover`

## 6、进行放置：

`ondrop`

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 300px;
            height: 300px;
        }
        #div1{
            border: 1px solid red;
        }
        #div2{
            border: 1px solid blue
        }
    </style>
    <script>
        // 阻止浏览器默认事件
        function allowDrop(ev){
            // 阻止冒泡事件
            ev.preventDefault();
        }
        // 放置
        function drag(ev){
            // 设置数据（根据 id）
            ev.dataTransfer.setData("Text",ev.target.id);
        }
        // 拖动
        function drop(ev){
            ev.preventDefault();
            // 获取数据
            var data = ev.dataTransfer.getData("Text");
            // 添加（放置）元素
            ev.target.appendChild(document.getElementById(data));
        }
    </script>
</head>
<body>
    <!-- ondrop：进行放置；ondragover：放到何处 -->
    <div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
    <!-- draggable：设置元素为可拖放；ondragstart：拖动什么 -->
    <audio id="drag" controls="controls"  draggable="true" ondragstart="drag(event)">
        <source src="./raw/Village People - YMCA.flac">
    </audio>

    <div id="div2" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
</body>
</html>
```

# 四、画布

画布是一个矩形区域，您可以控制其每一个像素
canvas 拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法

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
    <canvas id="canvas" width="400px" height="400px"></canvas>
</body>

<script>
    // 根据 id 获取元素
    var c = document.getElementById("canvas");
    // 绘制 2d 图形
    var cxt = c.getContext("2d");

    // // 设置颜色
    // cxt.fillStyle = "#ff0000";
    // // 绘制形状（正方形）
    // cxt.fillRect(0,0,100,100);

    // // 设置颜色
    // cxt.fillStyle = "#ff0000";
    // // 绘制形状（圆形）
    // // 开启路径（使用路径绘制的）
    // cxt.beginPath();
    // // 绘制图形
    // cxt.arc(70,18,15,0,Math.PI*2,true);
    // // 关闭路径
    // cxt.closePath();
    // // 渲染
    // cxt.fill();

    // 绘制图片
    var img = new Image();
    img.onload = function(){
        cxt.drawImage(img,0,0);
    }
    img.src = "./raw/1.jpg";

</script>

</html>
```
# 五、SVG

> SVG 用法 API：[https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element)

## 1、什么是SVG?

1. SVG 指可伸缩矢量图形(Scalable Vector Graphics)
2. SVG 用于定义用于网络的基于矢量的图形
3. SVG 使用 XML 格式定义图形
4. SVG 图像在放大或改变尺寸的情况下其图形质量不会有损失
5. SVG 是万维网联盟的标准

## 2、SVG的优势

与其他图像格式相比(比如 JPEG 和 GIF)，使用 SVG 的优势在于：

1. SVG 图像可通过文本编辑器来创建和修改
2. SVG 图像可被搜索、索引、脚本化或压缩.
3. SVG 是可伸缩的
4. SVG 图像可在任何的分辨率下被高质量地打印
5. SVG 可在图像质量不下降的情况下被放大

## 3、浏览器支持

Internet Explorer 9、Firefox、 Opera、 Chrome 以及 Safari 支持内联 SVG

---

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
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="100" viewBox="0 0 3 2">
        <rect width="1" height="2" x="0" fill="#008d46" />
        <rect width="1" height="2" x="1" fill="#ffffff" />
        <rect width="1" height="2" x="2" fill="#d2232c" />
    </svg>

    <!-- 引入 svg 文件 -->
    <iframe src="5.svg" frameborder="0"></iframe>
</body>
</html>
```
```html
<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
    <rect width="10" height="10">
        <animate attributeName="rx" values="0;5;0" dur="10s" repeatCount="indefinite" />
    </rect>
</svg>
```

# 六、地理定位

## 1、地理定位

HTML.5 Geplocation API 用于获得用户的地理位置

## 2、浏览器支持

Internet Explorer 9、Firefox、 Chrome、 Safari 以及 Opera 支持地理定位
注释：对于拥有 GPS 的设备，比如 iPhone，地理定位更加精确

---


![image.png](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--09-59-892--p4kvgWY4RYJYkA.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="http://maps.google.com/maps/api/js?sensor=false"></script>
    <script>
        // 获取当前地理位置
        function init() {
            navigator.geolocation.getCurrentPosition(function (position) {
                var coords = position.coords;
                //设定地图参数，将用户的当前地理的经纬度设为地图中心点
                var latlng = new google.maps.LatLng(coords.latitude, coords.longitude);
                var myOptions = {
                    zoom: 14,
                    center: latlng,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };
                //创建地图并"map"div中显示
                var map1;
                map1 = new google.maps.Map(document.getElementById("map"), myOptions);
                //地图上创建标记
                var marker = new google.maps.Marker({
                    position: latlng,
                    map: map1
                });
                //设定标准窗口,并指定该窗口的注释文字
                var infowindow = new google.maps .InfoWindow({
                    content:"当前位置"
                });
                infowindow.open(map1, marker);
            })
        }

    </script>
    <style>
        div {
            width: 400px;
            height: 400px;
        }
    </style>
</head>

<body onload="init()">
    <div>

    </div>
</body>

</html>
```

# 七、Web 存储

HTML.5 提供了两种在客户端存储数据的新方法：

1. `localStorage`：没有时间限制的数据存储，即使一年过去也不会被删除
2. `sessionStorage`：针对一个 session 的数据存储，当用户关闭当前浏览器窗口，数据会被删除

之前，这些都是由 cookie 完成的。但是 cookie 不适合大量数据的存储，因为它们由每个对服务器的请求来传递，这使得 cookie 速度很慢而且效率也不高

## 1、`localStorage`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        window.onload = function(){
            var text = document.getElementById("text");
            var btn = document.getElementById("btn");

            // 判断 localStorage 中有没有数据
            if(localStorage.text){
                // 有的话将 localStorage 中的数据取到文本框中
                text.value = localStorage.text;
            }

            // 绑定单击事件
            btn.onclick = function(){
                // 有的话将文本框中数据存到 localStorage 中
                localStorage.text = text.value;
            }
        }
    </script>
</head>
<body>
    <textarea id="text" style="width: 200px; height: 200px;"></textarea>
    <button id="btn">save</button>
</body>
</html>
```

## 2、`sessionStorage`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        var num = 0;

        window.onload = function(){
            var txt = document.getElementById("txt");
            var add = document.getElementById("add");

            // 判断 sessionStorage 中是否有 num
            if(sessionStorage.num){
                // 有，给 num 赋值
                num = sessionStorage.num;
            }else{
                // 没有，设置为 0
                num = 0;
            }

            // 绑定点击事件
            add.onclick = function(){
                // 自增
                num++;
                // 将 num 赋值给 sessionStorage 中的 num
                sessionStorage.num = num;
                // 调用函数
                showNum();
            }
        }

        function showNum(){
            // 更改标签的内容
            txt.innerHTML = num;
        }
    </script>
</head>
<body>
    <span id="txt">0</span>
    <button id="add">add</button>
</body>
</html>
```

# 八、CSS3 边框

## 1、CSS3边框

通过 CSS3，能够创建圆角边框，向矩形添加阴影，使用图片来绘制边框
并且不需使用设计软件，比如PhotoShop。

## 2、属性:

1. border-radius：圆角矩形
2. box-shadow：阴影
3. border-image：边框图像

## 3、浏览器支持:

Internet Explorer 9+ 支持 border-radius 和 box-shadow 属性
Firefox、Chrome 以及 Safari 支持所有新的边框属性。

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 400px;
            height: 200px;
        }
        .div1{
            border: 2px solid red;
            /* 圆角矩形 */
            border-radius: 30px;
        }
        .div2{
            background-color: aquamarine;
            /* 阴影
                参数1：右移距离（可为负数）
                参数2：下移距离（可为负数）
                参数3：模糊度
                参数4：阴影颜色
             */
            box-shadow: 10px 10px 5px black;
        }
        .div3{
						/* 边框 */
            border: 200px solid red;
						/* 边框图像 */
            border-image: url(./raw/1.jpg) 300 round;
        }
    </style>
</head>
<body>
    <div class="div1"></div><hr />
    <div class="div2"></div><hr />
    <div class="div3"></div><hr />
</body>
</html>
```

# 九、CSS3 背景

## 1、CSS3背景

CSS3 包含多个新的背景属性，它们提供了对背景更强大的控制。

## 2、属性:

1. `background-size`：修改背景图片大小

语法：background-size: length|percentage|cover|contain;

| 值 | 描述 |
| --- | --- |
| length | 设置背景图片高度和宽度。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为 **auto**(自动) |
| percentage | 将计算相对于背景定位区域的百分比。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为"auto(自动)" |
| cover | 此时会保持图像的纵横比并将图像缩放成将完全覆盖背景定位区域的最小大小。 |
| contain | 此时会保持图像的纵横比并将图像缩放成将适合背景定位区域的最大大小。 |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            /* 设置背景图片 */
            background: url("./raw/1.jpg");
            /* 不重复 */
            background-repeat: no-repeat;
            /* 设置顶部填充（空格） */
            padding-top: 400px;
            /* 修改背景图片大小
             */
            background-size: 100px;
        }
    </style>
</head>
<body>
    <p><img src="./raw/1.jpg" alt=""></p>
</body>
</html>
```

2. `background-origin`：内容框相对定位的背景图片

语法：background-origin: padding-box|border-box|content-box;

| 值 | 描述 |
| --- | --- |
| border-box | 背景图像边界框的相对位置 |
| content-box | 背景图像的相对位置的内容框 |
| padding-box | 背景图像填充框的相对位置 |

## 3、浏览器支持:

Internet Explorer 9+、Firefox、 Chrome、 Safari 以及 Opera 支持新的背景属性

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            /* 边框 */
            border: 1px solid cadetblue;
            /* 内边距 */
            padding: 35px;
            /* 设置背景图片 */
            background: url("./raw/1.jpg");
            /* 不重复 */
            background-repeat: no-repeat;
            /* 设置背景图像的起始位置 */
            background-position: left;
        }
        #div1{
            /* 背景图像边界框的相对位置 */
            background-origin: border-box;
        }
        #div2{
            /* 背景图像的相对位置的内容框 */
            background-origin: content-box;
        }
    </style>
</head>
<body>
    <p>border-box</p>
    <div id="div1">
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

    </div>

    <p>content-box</p>
    <div id="div2">
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

    </div>

    <p>原始的</p>
    <div>
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|

    </div>
</body>
</html>
```

# 十、文本效果

## 1、文本效果

CSS3 包含多个新的文本特性

## 2、属性

1. text-shadow：阴影

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{
            /* 阴影
                参数1：右移距离（可为负数）
                参数2：下移距离（可为负数）
                参数3：模糊度
                参数4：阴影颜色
             */
            text-shadow: 10px 10px 5px blue;
        }
    </style>
</head>
<body>
    <h1>月海</h1>
</body>
</html>
```

2. word-wrap：自动换行

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 200px;
            border: 1px solid red;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <div>
        |月海|月海|月海|月海|月海|月海|aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
    </div>
</body>
</html>
```

3. 加载服务器上的字体

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 加载服务器上的字体 */
        @font-face {
            /* 规定要加载的字体 */
            font-family: yuehai;
            /* 要加载字体的地址 */
            src: url("");
        }
        div{
            /* 设置从服务器上加载来的字体 */
            font-family: yuehai;
        }
    </style>
</head>
<body>
    <div>
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
    </div>
</body>
</html>
```

## 3、浏览器支持

Internet Explorer 10、Firefox、 Chrome、 Safari 以及 Opera 支持 text-shadow 属性

# 十一、2D 效果

## 1、2D效果:

通过 CSS3 转换，我们能够对元素进行移动、缩放、转动、拉长或拉伸。

## 2、浏览器支持:

1. Internet Explorer 10、Firefox 以及 Opera 支持 transform 属性
2. Chrome 和 Safari 需要前缀 -webkit-
3. Internet Explorer 9 需要前缀 -ms-

## 3、2D转换:

1. translate()：移动
2. rotate()：旋转
3. scale()：缩放
4. skew()：倾斜
5. matrix()：矩阵变换

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            margin: 30px;
            width: 200px;
            height: 100px;
            background-color: red;

            /* 旋转；顺时针旋转 30 度（可为负数） */
            /* transform: rotate(30deg); */

            /* 移动 */
            /* transform: translate(400px,400px); */

            /* 缩放，x 轴放大 2 倍，y 轴放大 4 倍 */
            /* transform: scale(2,4); */

            /* 倾斜；x 轴 30 度、y 轴 30 度 */
            /* transform: skew(30deg,30deg); */

            /* 矩阵变换 */
            transform: matrix(0.75, 0.8, -0.8, 1.2, 10, 20);
        }
    </style>
</head>
<body>
    <div>月海</div>
</body>
</html>
```

# 十二、3D 效果

## 1、3D效果:

CSS3 允许您使用 3D 转换来对元素进行格式化

## 2、浏览器支持:

Internet Explorer 10、Firefox 以及 Opera 支持 transform 属性
Chrome和Safari 需要前缀-webkit-
Internet Explorer 9需要前缀-ms-

## 3、属性:

rotateX()：沿 x 轴旋转，顶端向内旋转
rotateY()：沿 y 轴旋转，左端向内旋转

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            margin: 30px;
            width: 200px;
            height: 100px;
            background-color: red;

            /* 沿 x 轴旋转 120 度，顶端向内旋转  */
            /* transform: rotateX(120deg); */

            /* 沿 y 轴旋转 120 度，左端向内旋转  */
            transform: rotateY(120deg);
        }
    </style>
</head>
<body>
    <div>月海</div>
</body>
</html>
```

# 十三、过渡

## 1、过渡

通过 CSS3，我们可以在不使用 Flash 动画或 JavaScript 的情况下，当元素从一种样式变换为另一种样式时为元素添加效果

## 2、浏览器支持

Internet Explorer 10、Firefox、 Chrome 以及 Opera 支持 transition 属性
Safari 需要前缀 -webkit-

## 3、效果

CSS3 过渡是元素从一种样式逐渐改变为另一种的效果
要实现这一点，必须规定两项内容：

1. 规定希望把效果添加到哪个 CSS 属性上
2. 规定效果的时长

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            margin: 30px;
            width: 200px;
            height: 100px;
            background-color: red;

            /* 
                过度
                参数1：规定希望把效果添加到哪个 CSS 属性上
                参数2：规定效果的时长
             */
            transition: width 2s, height 2s, transform 3s;
        }
        /* 当鼠标移动到元素上时触发 */
        div:hover{
            width: 400px;
            height: 400px;
            /* 沿 y 轴旋转 120 度，左端向内旋转  */
            transform: rotateY(120deg);
        }
    </style>
</head>
<body>
    <div>月海</div>
</body>
</html>
```

# 十四、动画

## 1、动画

通过 CSS3，我们能够创建动画，这可以在许多网页中取代动画图片、Flash 动画以及 JavaScript

## 2、CSS3 @keyframes 规则

@keyframes 规则用于创建动画。在 @keyframes 中规定某项 CSS 样式，就能创建由当前样式逐渐改为新样式的动画效果

## 3、浏览器支持

Internet Explorer 10、Firefox  以及 Opera 支持 @keyframes 规则和 animation 属性
Chrome 和 Safari 需要前缀 -webkit-

## 4、规则

通过规定至少以下两项 CSS3 动画属性，即可将动画绑定到选择器：
规定动画的名称
规定动画的时长

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 200px;
            height: 100px;
            background-color: red;
            position: relative;
        }

        /* @keyframes 规则 */
        @keyframes color {
            from{
                background-color: red;
            }
            to{
                background-color: yellow;
            }
        }
        /* 当鼠标移动到元素上时触发 */
        #div1:hover{
            /* 根据动画的名称控制动画时间 */
            animation: color 3s;
        }

        /* @keyframes 规则；根据阶段控制 */
        @keyframes color2 {
            0%{
                background-color: red;
                left: 0px;
                top: 0px;
            }
            25%{
                background-color: yellow;
                left: 200px;
                top: 0px;
            }
            50%{
                background-color: blue;
                left: 200px;
                top: 200px;
            }
            75%{
                background-color: purple;
                left: 0px;
                top: 200px;
            }
            100%{
                background-color: red;
                left: 0px;
                top: 0px;
            }
        }
        /* 当鼠标移动到元素上时触发 */
        #div2:hover{
            /* 根据动画的名称控制动画时间 */
            animation: color2 5s;
        }
    </style>
</head>
<body>
    <div id="div1">月海</div><hr />
    <div id="div2">月海</div>
</body>
</html>
```

# 十五、多列

## 1、多列

通过 CSS3，您能够创建多个列来对文本进行布局，就像报纸那样!

## 2、浏览器支持

Internet Explorer 10 和 Opera 支持多列属性
Firefox 需要前缀 -moz-
Chrome和Safari 需要前缀 -webkit-

## 3、属性

column-count：列数
column-gap：列宽（列于列的间距）
column-rule：列间距中的线

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            /* 分为 3 列 */
            column-count: 3;
            /* 列宽（列于列的间距） */
            column-gap: 200px;
            /* 列间距中的线 */
            column-rule: 4px outset red;
        }
    </style>
</head>
<body>
    <div>
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
        |月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|月海|
    </div>
</body>
</html>
```









