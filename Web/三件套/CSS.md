> [https://developer.aliyun.com/course/1895](https://developer.aliyun.com/course/1895) ，不太好

## 一、CSS简介

## 1、什么是 CSS

css (Cascading Style Sheets 的缩写)，翻译为“层叠样式表”或者“级联样式表”，简称样式表。

## 2、CSS 的主要作用

1. 它主要是用来给 HTML 网页来设置外观或者样式
2. HTML 网页中的文字的大小、颜色、字体，网页的背景颜色、背景图片

## 3、书写 CSS 的语法规则

![](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2FPasted%20image%2020230728130239.png)

1. CSS 代码是由选择器和一对括号组成
2. 大括号里面是由一条一条的声明语句组成
3. 每一条语句都要使用英文状态下面的分号
4. 每一条语句是由“属性:值”组成
5. css 中的属性值一般不加引号,
6. 在 CSS 中如果属性值为数值型数据的时候一般情况下需要加单位惇单位一般都是 px(像素)
7. 在CSS中不能出现 HTML 标签·

## 二、css 代码的书写方式

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-533--QBnsXiZftgLhNQ.png)

### 1、嵌入式

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-564--Pe6_SmXJno_S2w.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-578--efGHRJ2zibyaxQ.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- 嵌入式 -->
    <style>
        p{
            /* 字体颜色 */
            color: red;
            /* 字体大小 */
            font-size: 100px;
        }
    </style>

</head>
<body>
    
    <p>月海</p>
    
</body>
</html>
```

### 2、外链式

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-617--Z5KipvSI2dBOqA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-628--P6wOto620npXSA.png)

```css
p{
    /* 字体颜色 */
    color: red;
    /* 字体大小 */
    font-size: 100px;
}
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- 外链式 -->
    <link rel="stylesheet" href="./css/index.css" />

</head>
<body>
    
    <p>月海</p>
    
</body>
</html>
```

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-769--D5ww1344N8sBRg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-22-869--YJ1xyNcyz2rdng.png)

### 3、行内式

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-023--Jafik_FT7cVWow.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-121--fEYAYb1sjLbSNg.png)

### 4、总结

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-280--I6HfsoFvYmdIqw.png)

## 三、注释

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-487--TP5Sk_HFO-A4mg.png)

## 四、基本选择器

### 1、什么是选择器

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-613---F0T39vucXVFYw.png)

### 2、基本选择器

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-779--6sjtEcTPVWtoYw.png)

### 3、一个标签内可以携带多个类名

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-23-926--9mR1fiwblp5uzQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-063--ToLbSoUWuSNi7w.png)

## 五、属性
### 1、尺寸样式属性

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-218--6uUZrItyZR-eWw.png)

### 2、文本属性

- 一般用 span 标签将问题引起来

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-344--IlvQyBhgRqnIeA.png)

### 3、字体属性

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-564--elhtsDwrxl6Fgw.png)

## 六、复合元素选择器

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-699--IJqABvlRaTMvhA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-24-830--rGMmjdqMBhgAYQ.png)

## 七、列表样式属性

- 这里的列表指的是：无序列表和有序列表

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-005--PU_PAVBBoXQ80A.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-176--WmoyhmIIVwMZRw.png)

## 八、伪类选择器

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-445--iTv-9hlsnKIAkg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-632--_h2XY8FcS9ALlA.png)

- 顺序为：link -> visited -> hover-> active

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        /* 未被访问 */
        a:link{
            color: #f00;
        }
        /* 访问过后 */
        a:visited{
            color: #000;
        }
        /* 鼠标放上 */
        a:hover{
            color: gold;
        }
        /* 鼠标按下 */
        a:active{
            color: #0f0;
        }
    </style>

</head>
<body>
    
    <a href="https://www.baidu.com/">百度</a>
    <a href="https://www.133.com/">133</a>
    <a href="https://www.134.com/">134</a>

</body>
</html>
```

## 九、属性选择器

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-778--337ZbymmmhunXg.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>属性选择器</title>

    <style>
        /* 通过属性选择器来匹配元素 */

        /* 1、[属性名] ，根据是否有此属性来匹配元素 */
        /* [align]{
            color: red;
        } */

        /* 1.2、标签名[属性名] ，先匹配标签，额案后根据匹配到的标签内是否有此属性来匹配元素 */
        /* p[align]{
            color: red;
        } */

        /* 2、[属性名=值]，根据是否有此属性，以及值是否一致来匹配元素；同样可以在起那面添加标签 */
        /* [align="center"]{
            color: blueviolet;
        } */

        /* 3、[属性名^=值]，根据是否有此属性，以及值的开头是否一致来匹配元素；同样可以在起那面添加标签 */
        [align^="cen"]{
            color: blue;
        }
      
         /* 其他的都类似 */

    </style>

</head>
<body>
    
    <h2 align="center">月海</h2>
    <p align="center">yuehai</p>
    <p>yuehai</p>

</body>
</html>
```

## 十、继承性和优先级

### 1、继承性

1. html 标签中，外层元素的样式会被内层元素所继承。
2. html 标签中，如果内层元素与外层元素的样式相同时，外层元素的样式会被内层元素所覆盖。
3. 并不是所有的样式都能被继承；只有文本与字体样式样式属性能够被继承，其他的样式属性都不可以。

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-25-993--t8OcuWexfGqkNw.png)

### 2、优先级

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-125--ApcIoaUxjm4u7Q.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-319--rlQzu3SMQ-gu1w.png)

### 3、!important属性

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-433--6oKYvvkmb1QRAw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-544--cRnefTZhu_WdgA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-649--JZhi1tcinDvGxg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-26-853--cZ0RMKECPRDDGA.png)

## 十一、背景样式属性

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-27-060--Y9UActCZWaEYog.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-27-224--wZzL-rVrBbPyYg.png)

## 十二、标准文档流

### 1、什么是标准文档流

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-27-411--N7lqSm3UYjG6MQ.png)

### 2、标准文档流要注意的事项

#### ①、空白折叠现象

- 如何解决这个问题：放在同一行

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-27-543--2rLzOg4_hiOS9w.png)

#### ②、高矮不齐，底部对齐

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-27-894--W7zrNQbEv5pW_Q.png)

## 十三、浮动

### 1、浮动

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-28-102--i4ygrxyoklJT_A.png)

### 2、清除浮动

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-28-335--wo3WwX_AwL_ThA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-28-485--I350cG0AEB-kdg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-28-657--ELYyuXTKpbUDJw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-28-817--H-4W1KEX3dh6Vg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-031--Q113cCzQkCT-xA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-137--2EjBtNTAfJ7J-w.png)

## 十四、 盒子模型
### 1、什么是盒子

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-302--HFXGFwQRIh2gnA.png)

### 2、盒子的大小

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-576--CG--3ZdJB_IJtA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-747--VXBFPPqNw_PtzQ.png)

## 十五、盒子属性
### 1、pasdding - 内填充

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-29-915--oo_F9M8Zm5nOgw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-30-130--KZ5EVorc8BQCbw.png)

### 2、margin - 外边距

#### ①、margin 介绍

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-30-311--YKEIp9OicHAMlQ.png)

#### ②、margin 塌陷现象

**什么是 margin 塌陷现象：**

1. 在标准的文档流中，竖直方向的 margin 值不会叠加，他会取较大的值

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-30-579--Sx9dWZs26OBnaw.png)

2. 横着方向是没有 margin 塌陷现象的

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-30-750--49JlGV6iSkeGGw.png)

3. 浮动元素他也是没有 margin 塌陷现象的

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-30-937--QgRnX1A0Zec7CA.png)

#### ③、margin 居中

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-113--k0LM_QW1ptedSQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-237--a2hV8AFILi3_fw.png)


![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-371--k7LAgETXuXAj6w.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-601--Qt677ibZefqCsA.png)

### 3、善于使用父元素的 padding 而不使用子元素的 margin

#### 0、使元素紧贴浏览器边框

```html
/* 通用选择器来去除 HTML 中所有标签的默认内填充与外边距 */
*{
  margin: 0px;
  padding: 0px;
}
```

#### 1、问题：单独设置嵌套的里面盒子的外边距，会使其父元素生效

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-804--oemrbQwLfBn2xw.png)

- 要解决这个问题，有两个方法可以解决：
   - 1、给其父元素设置一个边框线（不常用）

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-31-979--7dhcHHigxwhWCA.png)

   - 2、不要使用子元素的 margin 二十使用其父元素的 padding

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-32-186--cYUrWcTFWM91YA.png)

- 说明：margin 这个属性他本意是用于描述兄弟与兄弟之间的关系，不是用于描述父子元素之间的关系的。如果是父子元素的关系，就最好给其父元素使用 padding 属性

### 3、border - 边框

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-32-507--gqV3CFS6HgWNNg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-32-594--qXZ1FV782ZUymw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-32-794--iPRqVEHy7oidXA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-32-990--7YxCFzLygKQYcg.png)

### 4、display - 显示

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-220--I7L5SDxk-2eeoQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-390--cETeSIXEN7JDuA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-546--G_v6EdVIfbNu-g.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-648--Lg8Q3Yib2OwM1Q.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-826--Utppgh1VTdS8Sg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-33-983--6qtPIW9y1Ta3lw.png)

### 5、position - 定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-34-161--aLKasYcI8lWntg.png)

#### ①、fixed - 固定定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-34-316--uBUjsH0VuZ38eA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-34-485--52RVphIeJC862g.png)

#### ②、relatvie - 相对定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-34-660--yMADjhagD5uNIQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-34-805--6UNMQ3ie7G9k2g.png)

#### ③、absolute - 绝对定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-020--BYBjz2TLMqMSfQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-201--EFUt-ZJr6OF3nQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-368--SKo1dl5S5ar7lg.png)

- 在父元素中设置一个相对定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-613--RejV83u37Rt9Aw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-728--uSPycXjFCNEnRg.png)

- 在父元素的父元素中设置一个相对定位

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-35-918--hWojrSyyoxvQbw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-007--hdEK7-Mf8SsNzw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-171--63L9Ov38JR6iNQ.png)

- 案例

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-310--UEqef9RDjoIS6Q.png)

### 8、z-index - 竖轴

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-481--AIZ6niTSwbWZ3g.png)


![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-743--mykxRfPrtSgOhg.png)

- 都设置 z-index 属性

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-36-921--SCWeGoDJ2oGSKg.png)

## CSS 3

- css 3 和 css 2 的区别
   - css 3 = css 2 + 新语法 + 新属性
   - 就是对 css 2 进行扩充、删减、优化

### 1、结构伪类

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-37-191--TPIFYl0D6BMM7A.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        /* 使用 css 3 中的结构伪类选择器来匹配元素 */

        /* 匹配第一个孩子 */
        .box ul li:first-child{
            width: 100px;
            height: 100px;
            color: red;
            line-height: 30px;
            border: 1px solid red;
        }
        /* 匹配最后一个孩子 */
        .box ul li:last-child{
            width: 100px;
            height: 100px;
            color: blueviolet;
            line-height: 30px;
            border: 1px solid blueviolet;
        }
        /* 匹配第 n 个孩子 */
        .box ul li:nth-child(2){
            width: 100px;
            height: 100px;
            color: blue;
            line-height: 30px;
            border: 1px solid blue;
        }
        /* 匹配偶数的孩子，如2、4、6 */
        /* 匹配奇数的孩子，如1、3、5 */
        /* 匹配有且只有一个孩子 */
    </style>

</head>
<body>
    
    <div class="box">
        <ul>
            <li>月海000123</li>
            <li>月海000123</li>
            <li>月海000123</li>
            <li>月海000123</li>
        </ul>
    </div>

</body>
</html>
```

### 2、border-collapse - 表格边框

- border-collapse 属性设置表格的边框是否被合并为一个单一的边框，还是象在标准的 HTML 中那样分开显示

| separate | 默认值。边框会被分开。不会忽略 border-spacing 和 empty-cells 属性。 |
| --- | --- |
| collapse | 如果可能，边框会合并为一个单一的边框。会忽略 border-spacing 和 empty-cells 属性。 |
| inherit | 规定应该从父元素继承 border-collapse 属性的值。 |

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-37-326--g0qs-XXrK35OnQ.png)

### 3、伪元素

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-37-458--TvnKBPsOFz6RXg.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .box{
            width: 40%;
            /* 让当前元素水平居中 */
            margin: 100px auto;
            font-size: 14px;
            border: 1px solid #444;
            color: #333;
        }
        /* 操作当前元素中的第一个字 */
        .box::first-letter{
            color: red;
            font-size: 40px;
            padding: 20px;
        }
        /* 操作当前元素中的第一行的字 */
        .box::first-line{
            color: aquamarine;
        }
        /* 在当前元素的最前面插入（依然在盒子内） */
        .box::before{
            /* 要在当前元素的最前面插入文字，必须将文字放在 content 中 */
            content: "月海";
        }
        /* 在当前元素的最后面插入（依然在盒子内） */
        .box::after{
            /* 要在当前元素的最前面插入文字，必须将文字放在 content 中 */
            content: "月海";
        }
    </style>

</head>
<body>

    <div class="box">
        愚者途径，准支柱级旧日。源堡第三位苏醒者（1349年6月28日凌晨）。原身在被封印物“安提哥努斯家族笔记”杀害后，又被做了“转运仪式”的周明瑞附体重生。周明瑞为了返回地球再次举行了“转运仪式”，却意外进入了一个神秘的灰雾空间，期间不经意将奥黛丽.霍尔和阿尔杰.威尔逊的意识拉进灰雾空间；为了掌握谈话的主导权伪装成复苏中的隐秘存在，自称“愚者先生”，并建立一周聚会一次的“塔罗会”，此后视情况不断拉入新成员。“世界”是其为了方便交易、换取情报以及保持高位格而通过灰雾创造出来的小号。 
        曾化名夏洛克.莫里亚蒂、格尔曼.斯帕罗、辛巴.德沃伦特、道恩.唐泰斯、梅林.赫尔墨斯等，并具有海神“卡维图瓦”的马甲。
        克莱恩在消化完序列1‘诡秘侍者’魔药后，做好充足准备后，前往霍纳奇斯山脉试图容纳序列0‘愚者’的唯一性，期间受到阿蒙、第二代造物主、原初魔女和隐匿贤者的阻拦，但借助“黑夜女神”、“风暴之主”、“知识与智慧之神”、“永恒烈阳”、“大地母神”和“蒸汽与机械之神”的帮助，将容纳唯一性的仪式改为完整的成神仪式，成功晋升为真神。
        最后在“源堡”内与阿蒙的本体决斗，成功击败阿蒙后收回“门”途径和“错误”途径的唯一性和序列一非凡特性，成为半个诡秘之主。之后为了对抗体内前代诡秘之主不断复苏的意识，陷入了长久的沉睡。十年之后，精神逐渐平稳，初步苏醒，并回应了妹妹与侄女的祈祷。
        愚者尊名：“不属于这个时代的愚者；灰雾之上的神秘主宰；执掌好运的黄黑之王”
        序列三尊名：“灵界和源堡的眷者；源自古代的诡秘；漫长历史的见证；贝克兰德魔术和戏剧表演的保护者（后改为：贝克兰德所有贫困孩子的保护者）；伟大的格尔曼.斯帕罗”
    </div>

</body>
</html>
```

### 4、文本阴影

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-37-669--PqSHu15lvTuHTA.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-37-908--AFj-haMSZRvVYw.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-017--MOfEvV9XZIthUw.png)


- 设置多组阴影

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-144--NGJg4rh3-JFPTQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-243--M2vF1u8jj73NDQ.png)

### 5、盒子阴影

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-389--y1y6RzLQlUoKaQ.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-572--Co3qgWEwQgBNQg.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-647--Rw_-_duBxCxv-w.png)

- 给图片设置阴影

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-38-917--e7UQN9vYrU_7_g.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-021--QLtjo_RZmnBj0g.png)

### 6、圆角矩形

-  border-radius:  左上 右上 右下 左下
- 如果四个值都是一样的话，只需要写一个参数就可以了

#### 1、圆角矩形

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-225--Uoh0XKi2GKwzmg.png)

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
            width: 100px;
            height: 100px;
            border: 1px solid red;
            float: left;
            margin: 10px;
        }
        
        .box1{
            /* 圆角矩形：左上 右上 右下 左下 */
            border-radius: 10px 20px 30px 40px;
        }
        .box2{
            /* 圆角矩形：如果四个值都是一样的话，只需要写一个参数就可以了 */
            border-radius: 30px;
        }
    </style>

</head>
<body>
    
    <div class="box1"></div>
    <div class="box2"></div>

</body>
</html>
```

#### 2、圆形

1. div设置为正方形
2. border-radius 的值设置为正方形边长的一半

#### 3、椭圆形

1. div设置为长方形
2. border-radius 的值设置为长方形其中一对相对边（一般是短边）边长的一半

#### 4、实心的上半部分是圆

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-332--ZhzuvIbnUsme0A.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-438--wYBNG-VIQVXG3g.png)

### 7、透明度

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-553--sOy8jE1Ge9-y6Q.png)

![image.png](http://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2F%E4%B8%89%E4%BB%B6%E5%A5%97%2Fattachments%2F2023-07-25-13--07-39-653--JQKCWxOzwbhzUw.png)

