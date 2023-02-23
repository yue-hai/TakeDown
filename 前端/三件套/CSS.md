> [https://developer.aliyun.com/course/1895](https://developer.aliyun.com/course/1895) ，不太好
> [css.jpg](https://www.yuque.com/attachments/yuque/0/2023/jpeg/29280567/1673925617013-a6c69e4c-0d7a-4eb9-a554-70f579f8128e.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fjpeg%2F29280567%2F1673925617013-a6c69e4c-0d7a-4eb9-a554-70f579f8128e.jpeg%22%2C%22name%22%3A%22css.jpg%22%2C%22size%22%3A207431%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u709511c8-f505-434e-a234-f7f6fdf207d%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u91df2ffd%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)

## 一、CSS简介
### ![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655700359348-485d1899-da36-4874-a7be-b91efb0d1d8c.png#clientId=u15f33af2-7971-4&from=paste&height=291&id=uab9629eb&name=image.png&originHeight=291&originWidth=729&originalType=binary&ratio=1&rotation=0&showTitle=false&size=119003&status=done&style=stroke&taskId=uab061f41-90fd-461d-9058-12d34a51c15&title=&width=729)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655700631711-423191c2-d180-4e12-967d-93f70c09169c.png#clientId=u15f33af2-7971-4&from=paste&height=544&id=uf7daa567&name=image.png&originHeight=544&originWidth=765&originalType=binary&ratio=1&rotation=0&showTitle=false&size=220400&status=done&style=stroke&taskId=ufc0ef6fa-8227-4fb6-ab35-ee8cd254ede&title=&width=765)
## 二、css 代码的书写方式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655701130322-a76aac42-2f6f-44a3-bd19-6fe28809332a.png#clientId=u15f33af2-7971-4&from=paste&height=65&id=uf86c61a9&name=image.png&originHeight=65&originWidth=394&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29617&status=done&style=stroke&taskId=u199205ed-f4ed-4706-abb8-8972c7e7491&title=&width=394)
### 1、嵌入式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655701193837-b3d5773c-7ec6-4df1-8292-c469f5875f9c.png#clientId=u15f33af2-7971-4&from=paste&height=246&id=ubf95ec1e&name=image.png&originHeight=246&originWidth=732&originalType=binary&ratio=1&rotation=0&showTitle=false&size=110341&status=done&style=stroke&taskId=ub812776f-2494-4a6d-bcf9-5baeb07f5db&title=&width=732)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655701496136-3acb5716-f097-4646-942f-2ff1e65d2bc3.png#clientId=u15f33af2-7971-4&from=paste&height=643&id=u2d5d08ec&name=image.png&originHeight=643&originWidth=1200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=375923&status=done&style=stroke&taskId=uc1f6e508-9159-448b-be9a-c3df6ba8443&title=&width=1200)
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655701713254-1250e5bb-6c73-46a8-a4e3-1646769a9a71.png#clientId=u15f33af2-7971-4&from=paste&height=133&id=u462ab181&name=image.png&originHeight=133&originWidth=725&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74939&status=done&style=stroke&taskId=u4be10b29-e7e0-436f-ba9a-b29c1a21e2b&title=&width=725)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655701665969-7b89a0e3-5080-4a0e-a9d3-27b0c24e32b8.png#clientId=u15f33af2-7971-4&from=paste&height=197&id=u264a0a34&name=image.png&originHeight=197&originWidth=613&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67795&status=done&style=stroke&taskId=u75408460-5746-4396-b2c7-86570dcf07c&title=&width=613)
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702217566-12977163-5d64-4922-8bdb-378637c47bf1.png#clientId=u15f33af2-7971-4&from=paste&height=343&id=u44fd9cde&name=image.png&originHeight=343&originWidth=1918&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49775&status=done&style=stroke&taskId=ua5176e9d-0b56-4fb3-ac3f-014b1d8fe66&title=&width=1918)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702405648-597a3b1f-340e-4add-989c-ba03c3b50c20.png#clientId=u15f33af2-7971-4&from=paste&height=245&id=u75768826&name=image.png&originHeight=245&originWidth=740&originalType=binary&ratio=1&rotation=0&showTitle=false&size=195110&status=done&style=stroke&taskId=uc44b471d-6217-4236-bb56-fb2f0c6177b&title=&width=740)
### 3、行内式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702718471-ba91b7fa-9191-44cf-a332-e729e6b3ffe9.png#clientId=u15f33af2-7971-4&from=paste&height=154&id=u32bff4b5&name=image.png&originHeight=154&originWidth=540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85721&status=done&style=stroke&taskId=u6d5a0140-c9ca-414d-9df0-9ebb46ead5e&title=&width=540)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702698836-8dec672c-fc3f-44b1-b926-ba3e121d4d0e.png#clientId=u15f33af2-7971-4&from=paste&height=646&id=u32dcec56&name=image.png&originHeight=646&originWidth=1114&originalType=binary&ratio=1&rotation=0&showTitle=false&size=316776&status=done&style=stroke&taskId=ua720fcec-f649-4433-a8f7-b571c303249&title=&width=1114)
### 4、总结
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702848499-741aa134-ebc5-4ae1-82a0-f4940492fb31.png#clientId=u15f33af2-7971-4&from=paste&height=65&id=uba65911e&name=image.png&originHeight=65&originWidth=593&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57777&status=done&style=stroke&taskId=u84fe403a-0b2f-4720-9c8b-5495aba7b15&title=&width=593)
## 三、注释
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655702890586-ce66b026-9725-4c50-9e4f-cd7ac236b191.png#clientId=u15f33af2-7971-4&from=paste&height=67&id=u4288e64b&name=image.png&originHeight=67&originWidth=178&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12455&status=done&style=stroke&taskId=ucf4e1550-679a-401e-8aec-6536a4787a6&title=&width=178)
## 四、基本选择器
### 1、什么是选择器
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655703134968-6d45b8d4-cf87-479d-9f9b-0dcdfd1a04f9.png#clientId=u15f33af2-7971-4&from=paste&height=98&id=u9554f46c&name=image.png&originHeight=98&originWidth=776&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90652&status=done&style=stroke&taskId=ue013b7ea-7465-45d4-afee-0dfbbd932c7&title=&width=776)
### 2、基本选择器
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655703374348-ed928122-d5f7-4169-a3bb-0e329f975fef.png#clientId=u15f33af2-7971-4&from=paste&height=388&id=uf40cf87e&name=image.png&originHeight=388&originWidth=799&originalType=binary&ratio=1&rotation=0&showTitle=false&size=341961&status=done&style=stroke&taskId=ueb98053d-413b-4289-b9a9-b701704fadb&title=&width=799)
### 3、一个标签内可以携带多个类名
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655713770847-164cb9ac-ea73-4def-9487-d4feb70a105c.png#clientId=u1b4cd33d-ffab-4&from=paste&height=328&id=ub0027bdd&name=image.png&originHeight=328&originWidth=780&originalType=binary&ratio=1&rotation=0&showTitle=false&size=161179&status=done&style=stroke&taskId=u4d5bba65-a3b6-4db8-800d-cc004955e24&title=&width=780)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655713715706-04a82bd6-22a1-4b1b-b47e-e8bbde54fd0e.png#clientId=u1b4cd33d-ffab-4&from=paste&height=527&id=u82e8de99&name=image.png&originHeight=527&originWidth=840&originalType=binary&ratio=1&rotation=0&showTitle=false&size=264284&status=done&style=stroke&taskId=u41557616-7781-4e61-83e4-772d52a496c&title=&width=840)
## 五、属性
### 1、尺寸样式属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655703872863-f0652136-ab4b-4dca-97d1-64f9b3b7f8d5.png#clientId=u15f33af2-7971-4&from=paste&height=195&id=u10b7e008&name=image.png&originHeight=195&originWidth=804&originalType=binary&ratio=1&rotation=0&showTitle=false&size=79558&status=done&style=stroke&taskId=u7334cc9b-e2f2-46e3-8b4c-8a6ed06f869&title=&width=804)
### 2、文本属性

- 一般用 span 标签将问题引起来

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655704109042-4d49d399-032b-4992-94fd-00ba9445ccec.png#clientId=u15f33af2-7971-4&from=paste&height=369&id=ueacd3096&name=image.png&originHeight=369&originWidth=797&originalType=binary&ratio=1&rotation=0&showTitle=false&size=228498&status=done&style=stroke&taskId=ud3a0ac78-66ac-4695-8f1d-58afe11b9b6&title=&width=797)
### 3、字体属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655705176476-d707506c-d9c8-441c-aeee-9a4bf60a57bf.png#clientId=u15f33af2-7971-4&from=paste&height=273&id=u970e5a9f&name=image.png&originHeight=274&originWidth=797&originalType=binary&ratio=1&rotation=0&showTitle=false&size=176648&status=done&style=stroke&taskId=u9ed21107-7225-414c-99a4-6a045ab610c&title=&width=793)
## 六、复合元素选择器
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655705484506-26a95c8a-3eb2-4fc5-98f9-5634866e30ae.png#clientId=u15f33af2-7971-4&from=paste&height=298&id=ufa9bcf42&name=image.png&originHeight=299&originWidth=805&originalType=binary&ratio=1&rotation=0&showTitle=false&size=214709&status=done&style=stroke&taskId=u59cea632-a66f-4a12-bca0-2ac373b1177&title=&width=801)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655706129505-07f67ed5-de08-4294-be2d-e8e26d6051e4.png#clientId=u15f33af2-7971-4&from=paste&height=244&id=u04aecf0f&name=image.png&originHeight=244&originWidth=796&originalType=binary&ratio=1&rotation=0&showTitle=false&size=138473&status=done&style=stroke&taskId=ue5cf8803-60df-42e3-a920-b6e0aac12af&title=&width=796)
## 七、列表样式属性

- 这里的列表指的是：无序列表和有序列表

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655706269871-f891b02e-2159-4cce-b9b5-d8adddefe59b.png#clientId=u15f33af2-7971-4&from=paste&height=220&id=ucb88b201&name=image.png&originHeight=220&originWidth=775&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159782&status=done&style=stroke&taskId=ua27083d5-2f58-49d8-94c8-e87eaff43b3&title=&width=775)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655707136644-a671c8a3-ff12-4650-8ebd-7d7291875063.png#clientId=u15f33af2-7971-4&from=paste&height=573&id=ucd1556b2&name=image.png&originHeight=573&originWidth=887&originalType=binary&ratio=1&rotation=0&showTitle=false&size=348416&status=done&style=stroke&taskId=u80161298-11a1-43f1-a706-2528172810e&title=&width=887)
## 八、伪类选择器
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655707542291-44fba508-eeeb-4361-8821-061361576f0d.png#clientId=u1b4cd33d-ffab-4&from=paste&height=456&id=u037d3641&name=image.png&originHeight=456&originWidth=843&originalType=binary&ratio=1&rotation=0&showTitle=false&size=267394&status=done&style=stroke&taskId=u2e9e6605-2d8e-4eb7-92dc-fc1cf02f984&title=&width=843)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655708242080-5d6899dc-ae97-4bb3-93c8-476545f62220.png#clientId=u1b4cd33d-ffab-4&from=paste&height=84&id=u40f168ae&name=image.png&originHeight=84&originWidth=714&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67238&status=done&style=stroke&taskId=uadd37570-4227-4f24-a1d5-ff561c149de&title=&width=714)

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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655708828339-48ffd586-dafb-45f4-aee4-90d7c1d6332f.png#clientId=u1b4cd33d-ffab-4&from=paste&height=520&id=u0bf49f62&name=image.png&originHeight=520&originWidth=807&originalType=binary&ratio=1&rotation=0&showTitle=false&size=355959&status=done&style=stroke&taskId=u5edd6d76-1982-4931-b379-ca60ebe61f7&title=&width=807)
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

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655711488305-a034b825-dd85-480a-8082-04fb073a07e6.png#clientId=u1b4cd33d-ffab-4&from=paste&height=93&id=u61cf86d9&name=image.png&originHeight=93&originWidth=782&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73388&status=done&style=stroke&taskId=u41ed4a6d-d4f7-40e6-8cd2-53ecdd13b0e&title=&width=782)
### 2、优先级
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655712101424-e11cf28a-15d8-43bf-acc2-b6ee06002869.png#clientId=u1b4cd33d-ffab-4&from=paste&height=375&id=ubcb8fe61&name=image.png&originHeight=375&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=228668&status=done&style=stroke&taskId=u3595ff18-b7f0-41fd-ac5a-ccfd0a5c286&title=&width=786)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655712140640-1584d13f-7e18-474c-937e-5249b2d96e43.png#clientId=u1b4cd33d-ffab-4&from=paste&height=269&id=u3eb5c54c&name=image.png&originHeight=269&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78512&status=done&style=stroke&taskId=u4df26a93-e902-4b41-8c83-5583f0cfa05&title=&width=408)
### 3、!important属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655712203937-9d08c91e-3c30-4889-a307-567f82612112.png#clientId=u1b4cd33d-ffab-4&from=paste&height=246&id=K6tRf&name=image.png&originHeight=246&originWidth=518&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77506&status=done&style=stroke&taskId=ua9a9ce5d-3ebc-444b-a271-f52568f39ba&title=&width=518)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655712258429-9082cee4-d8e0-4a2d-8c70-bd960ec125a1.png#clientId=u1b4cd33d-ffab-4&from=paste&height=110&id=Uk5Ka&name=image.png&originHeight=110&originWidth=201&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21266&status=done&style=stroke&taskId=ud5881e95-08d1-406a-ad76-1cede76d461&title=&width=201)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655712582533-6b973845-58f8-42a6-b0a5-fc5bc30b5104.png#clientId=u1b4cd33d-ffab-4&from=paste&height=512&id=R1icO&name=image.png&originHeight=512&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159664&status=done&style=stroke&taskId=ud6b0acba-77d1-4da1-b422-785c361b46b&title=&width=784)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655713105093-2afbd102-d47e-4a93-b169-a59ef4d5797d.png#clientId=u1b4cd33d-ffab-4&from=paste&height=944&id=gtmOj&name=image.png&originHeight=944&originWidth=1064&originalType=binary&ratio=1&rotation=0&showTitle=false&size=446599&status=done&style=stroke&taskId=u700e111d-b784-409a-97fb-21383ce61db&title=&width=1064)
## 十一、背景样式属性
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655713829304-207550b8-d3b5-42ba-8cf0-c6234d5eeb77.png#clientId=u1b4cd33d-ffab-4&from=paste&height=281&id=u5fc4dbde&name=image.png&originHeight=281&originWidth=799&originalType=binary&ratio=1&rotation=0&showTitle=false&size=198354&status=done&style=stroke&taskId=uad707a81-5e81-4173-b243-433f6938b95&title=&width=799)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655715442671-dd43012e-6c06-4ccc-8afa-12651e32b1cf.png#clientId=u1b4cd33d-ffab-4&from=paste&height=663&id=u9c888ec9&name=image.png&originHeight=663&originWidth=789&originalType=binary&ratio=1&rotation=0&showTitle=false&size=526317&status=done&style=stroke&taskId=ua643c8fb-86b8-46c4-87da-03ab2231cac&title=&width=789)
## 十二、标准文档流
### 1、什么是标准文档流
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655715535550-2e81e5a5-9c2a-4619-b9f1-bbf305417d6d.png#clientId=u1b4cd33d-ffab-4&from=paste&height=86&id=u22736c04&name=image.png&originHeight=86&originWidth=647&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89846&status=done&style=stroke&taskId=u6ec3e8b5-1e66-465c-9974-905007989ec&title=&width=647)
### 2、标准文档流要注意的事项
#### ①、空白折叠现象

- 如何解决这个问题：放在同一行

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655772059441-4b1b2594-092c-4171-a843-d08b010474bc.png#clientId=ue8a850a2-0457-4&from=paste&height=763&id=u1a3162be&name=image.png&originHeight=763&originWidth=1273&originalType=binary&ratio=1&rotation=0&showTitle=false&size=917303&status=done&style=stroke&taskId=ue871c3c2-8792-4845-9300-56e1acdc0d5&title=&width=1273)
#### ②高矮不齐，底部对齐
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655772374974-44a09da8-ad56-43de-a254-d99010930b5f.png#clientId=ue8a850a2-0457-4&from=paste&height=498&id=ub0cf1963&name=image.png&originHeight=498&originWidth=741&originalType=binary&ratio=1&rotation=0&showTitle=false&size=252034&status=done&style=stroke&taskId=u66a7bb8c-6cca-479f-9185-23f7910b867&title=&width=741)

## 十三、浮动
### 1、浮动
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655774093147-31c426e0-ac55-4211-9ab9-ca6ce6a028ec.png#clientId=ue8a850a2-0457-4&from=paste&height=583&id=u4b4a7c1b&name=image.png&originHeight=583&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=483548&status=done&style=stroke&taskId=u1360599f-6bb8-41f1-b3b0-495708a29b6&title=&width=778)
### 2、清除浮动
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655777646024-fc017d22-6abc-43b4-bf9e-7624ed484028.png#clientId=ue8a850a2-0457-4&from=paste&height=349&id=u2351f869&name=image.png&originHeight=349&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=224588&status=done&style=stroke&taskId=u682709d7-d04d-42d7-9418-1d1d5b9c779&title=&width=778)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655778471018-e0ade540-eb62-4813-9250-931bcefafa55.png#clientId=ue8a850a2-0457-4&from=paste&height=641&id=ud1c1ea6a&name=image.png&originHeight=641&originWidth=746&originalType=binary&ratio=1&rotation=0&showTitle=false&size=309238&status=done&style=stroke&taskId=u94862f74-7738-40f4-9ec6-906ed1af598&title=&width=746)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655777654501-9228bef2-2218-44c0-aae3-1e52fa01dee8.png#clientId=ue8a850a2-0457-4&from=paste&height=166&id=u382b4f1a&name=image.png&originHeight=166&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=182249&status=done&style=stroke&taskId=ufdb81816-8b72-4250-b517-2752ab9384e&title=&width=857)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655777673461-e0c6e693-9bb6-483e-8af1-76bed94d20d7.png#clientId=ue8a850a2-0457-4&from=paste&height=632&id=ub549034b&name=image.png&originHeight=632&originWidth=762&originalType=binary&ratio=1&rotation=0&showTitle=false&size=298425&status=done&style=stroke&taskId=ube4b5dec-591a-42be-8c2f-c48bed920b9&title=&width=762)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655778425190-57464558-5215-4309-adb5-a77d74ad1973.png#clientId=ue8a850a2-0457-4&from=paste&height=91&id=ub582d5ba&name=image.png&originHeight=91&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94289&status=done&style=stroke&taskId=u4f4ef64d-79cd-47b1-a410-50e98936a1b&title=&width=761)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655778374452-cd6dcdea-1773-4bd5-b35e-9fa423793245.png#clientId=ue8a850a2-0457-4&from=paste&height=572&id=udfd68d7f&name=image.png&originHeight=572&originWidth=975&originalType=binary&ratio=1&rotation=0&showTitle=false&size=327312&status=done&style=stroke&taskId=u7eb9a24c-4fa5-43a6-b911-bed74aa5660&title=&width=975)
## 十四、 盒子模型
### 1、什么是盒子
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655778584558-9600a9fc-d62b-4092-a732-88baf0c91ea2.png#clientId=ue8a850a2-0457-4&from=paste&height=238&id=u9b18f1cd&name=image.png&originHeight=238&originWidth=789&originalType=binary&ratio=1&rotation=0&showTitle=false&size=154305&status=done&style=stroke&taskId=ud6580bda-7608-4322-b06c-630e1757d16&title=&width=789)
### 2、盒子的大小
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655779160493-89a3bff7-b7c4-4085-b6aa-c5edda5fe3ee.png#clientId=ue8a850a2-0457-4&from=paste&height=745&id=u72b825a8&name=image.png&originHeight=745&originWidth=879&originalType=binary&ratio=1&rotation=0&showTitle=false&size=405067&status=done&style=stroke&taskId=u86cb39e1-1415-4f43-a874-ef475e1c0cd&title=&width=879)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655779216504-c5841e84-8e7f-46fb-9c56-3561c8bca051.png#clientId=ue8a850a2-0457-4&from=paste&height=114&id=u93dffe40&name=image.png&originHeight=114&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=114051&status=done&style=stroke&taskId=u24fa6a8b-ce00-4c25-96b1-08dd2cca3c0&title=&width=784)
## 十五、盒子属性
### 1、pasdding - 内填充
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655780098236-51b041be-a2a1-4649-8f73-f208a1687af6.png#clientId=ue8a850a2-0457-4&from=paste&height=530&id=ud1b6b0d9&name=image.png&originHeight=530&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=326074&status=done&style=stroke&taskId=u605b0f1b-75e9-42d0-b565-8a72237c828&title=&width=786)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655780106394-1f6e6d9d-f9f1-4ad7-8023-67df71ec2e6f.png#clientId=ue8a850a2-0457-4&from=paste&height=484&id=u6b4654a3&name=image.png&originHeight=484&originWidth=1043&originalType=binary&ratio=1&rotation=0&showTitle=false&size=352895&status=done&style=stroke&taskId=u156182ff-dbe1-4700-83f5-39ea426c6c1&title=&width=1043)
### 2、margin - 外边距
#### ①、margin 介绍
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655780208785-d6aabe26-d6b1-4d6d-9535-e1e2b25ab45e.png#clientId=ue8a850a2-0457-4&from=paste&height=352&id=u843ee74a&name=image.png&originHeight=352&originWidth=782&originalType=binary&ratio=1&rotation=0&showTitle=false&size=198354&status=done&style=stroke&taskId=u07394c26-0bff-41f1-9ef4-e4b4edfb43b&title=&width=782)
#### ②、margin 塌陷现象
**什么是 margin 塌陷现象：**

1. 在标准的文档流中，竖直方向的 margin 值不会叠加，他会取较大的值

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655781371110-6ccb2473-ad2b-4483-aae3-19a377194c68.png#clientId=ue8a850a2-0457-4&from=paste&height=649&id=ua7223052&name=image.png&originHeight=649&originWidth=924&originalType=binary&ratio=1&rotation=0&showTitle=false&size=402169&status=done&style=stroke&taskId=u3148d290-8b1a-4370-87ec-7302559b243&title=&width=924)

2. 横着方向是没有 margin 塌陷现象的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655781035848-b8bab201-538c-46ae-97f2-df1ffcad9a1b.png#clientId=ue8a850a2-0457-4&from=paste&height=621&id=u082a0187&name=image.png&originHeight=621&originWidth=750&originalType=binary&ratio=1&rotation=0&showTitle=false&size=353550&status=done&style=stroke&taskId=u2f9edef7-cf06-48bf-8b55-1ad503a1ffb&title=&width=750)

3. 浮动元素他也是没有 margin 塌陷现象的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655781668627-f0927759-d989-43be-93ec-659611c29be7.png#clientId=ue8a850a2-0457-4&from=paste&height=664&id=ube81307a&name=image.png&originHeight=664&originWidth=739&originalType=binary&ratio=1&rotation=0&showTitle=false&size=411707&status=done&style=stroke&taskId=uf52b0b7f-7a52-4c66-8c3c-2fda9f99527&title=&width=739)
#### ③、margin 居中
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655782242205-d0ad73da-6a0c-4b15-a2f4-93acb4408967.png#clientId=ue8a850a2-0457-4&from=paste&height=243&id=uec7bc865&name=image.png&originHeight=243&originWidth=806&originalType=binary&ratio=1&rotation=0&showTitle=false&size=177739&status=done&style=stroke&taskId=uf47b00e6-6e29-4865-aeb8-1415571db4e&title=&width=806)
           ![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655786475849-c3cb5daa-d855-47d1-9b90-34e64d7ea995.png#clientId=ue8a850a2-0457-4&from=paste&height=56&id=uf0df5929&name=image.png&originHeight=56&originWidth=751&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52346&status=done&style=stroke&taskId=u77c8d540-6656-4efe-9520-3a6e40edf28&title=&width=751)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655786216740-c24105a6-1a09-499d-9378-60ffedda50df.png#clientId=ue8a850a2-0457-4&from=paste&height=581&id=u883bee6f&name=image.png&originHeight=581&originWidth=709&originalType=binary&ratio=1&rotation=0&showTitle=false&size=290268&status=done&style=stroke&taskId=u0df37030-bf46-47a8-b8de-99197339116&title=&width=709)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655786372592-a8fe08e9-e19f-4049-86c6-c9a7de19eeb4.png#clientId=ue8a850a2-0457-4&from=paste&height=608&id=u349ad693&name=image.png&originHeight=608&originWidth=1116&originalType=binary&ratio=1&rotation=0&showTitle=false&size=396143&status=done&style=stroke&taskId=u97893594-8eb8-4e9f-b727-f1845aa1f4d&title=&width=1116)
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655787311936-74db3e17-7392-42af-beb0-c2fee200e5a6.png#clientId=ue8a850a2-0457-4&from=paste&height=707&id=u3a18da40&name=image.png&originHeight=707&originWidth=1147&originalType=binary&ratio=1&rotation=0&showTitle=false&size=627753&status=done&style=stroke&taskId=uf6ce6ffd-126a-4948-ab4b-8e365f12404&title=&width=1147)

- 要解决这个问题，有两个方法可以解决：
   - 1、给其父元素设置一个边框线（不常用）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655787571579-1e945c40-2598-49ee-a004-f677c04d4cc9.png#clientId=ue8a850a2-0457-4&from=paste&height=698&id=u65120160&name=image.png&originHeight=698&originWidth=1151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=665373&status=done&style=stroke&taskId=ua66d3996-6b71-47fd-bf75-8835b9ec088&title=&width=1151)

   - 2、不要使用子元素的 margin 二十使用其父元素的 padding

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655787715011-4b2441fe-2103-4670-8fbc-903bb1eaaaa3.png#clientId=ue8a850a2-0457-4&from=paste&height=638&id=u692e6289&name=image.png&originHeight=638&originWidth=1218&originalType=binary&ratio=1&rotation=0&showTitle=false&size=536722&status=done&style=stroke&taskId=ufca3f109-5087-4b99-bd73-f1622acad57&title=&width=1218)

- 说明：margin 这个属性他本意是用于描述兄弟与兄弟之间的关系，不是用于描述父子元素之间的关系的。如果是父子元素的关系，就最好给其父元素使用 padding 属性
### 3、border - 边框
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655787964292-a0fadb7d-d7f9-4052-ba44-ef7c742e445a.png#clientId=ue8a850a2-0457-4&from=paste&height=123&id=u7576e561&name=image.png&originHeight=123&originWidth=324&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46891&status=done&style=stroke&taskId=ua06f8697-13ba-4fd8-9cf2-0690aef20e9&title=&width=324)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655788050342-002f6a88-5a30-44d5-aac3-890c6d6a5420.png#clientId=ue8a850a2-0457-4&from=paste&id=u99878066&name=image.png&originHeight=674&originWidth=636&originalType=binary&ratio=1&rotation=0&showTitle=false&size=264141&status=done&style=stroke&taskId=uf9146adf-4d23-4e4d-83f2-c8cf226fd34&title=)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655788515229-e5ec953f-3a88-4b9d-8b94-ce743101b859.png#clientId=ue8a850a2-0457-4&from=paste&height=521&id=ue50baa94&name=image.png&originHeight=521&originWidth=694&originalType=binary&ratio=1&rotation=0&showTitle=false&size=153131&status=done&style=stroke&taskId=uc1fc6468-fb96-48a4-9aa7-16dffe07bd1&title=&width=694)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655788868971-873a5853-f956-410f-98c4-ae04e40d9e01.png#clientId=ue8a850a2-0457-4&from=paste&height=546&id=u90275741&name=image.png&originHeight=546&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=227799&status=done&style=stroke&taskId=u625bf698-b7c7-40dd-adba-8e38238d93c&title=&width=545)
### 4、display - 显示
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789248691-f3af0f61-9385-493b-95c5-c907a437d3d1.png#clientId=ue8a850a2-0457-4&from=paste&height=172&id=u6e06cee1&name=image.png&originHeight=172&originWidth=782&originalType=binary&ratio=1&rotation=0&showTitle=false&size=126507&status=done&style=stroke&taskId=u918e377e-d12d-42cf-9560-fc3107452de&title=&width=782)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789293365-f1cc5e5a-1300-4f37-a4d4-0dcaa78fd2ad.png#clientId=ue8a850a2-0457-4&from=paste&height=592&id=u5e2a6b09&name=image.png&originHeight=592&originWidth=1001&originalType=binary&ratio=1&rotation=0&showTitle=false&size=369877&status=done&style=stroke&taskId=u72378c70-08c9-4ec6-8cde-38a64b2a98f&title=&width=1001)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789473620-eeef30ad-e197-4db8-b7d9-7cf4d606ab5a.png#clientId=ue8a850a2-0457-4&from=paste&height=60&id=ua7e419b1&name=image.png&originHeight=60&originWidth=771&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44925&status=done&style=stroke&taskId=u79d314cc-cd30-41ad-9446-11c53b38563&title=&width=771)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789476923-0899c240-6bfd-44ad-a791-371f0ecef33f.png#clientId=ue8a850a2-0457-4&from=paste&height=671&id=ufdaa6215&name=image.png&originHeight=671&originWidth=672&originalType=binary&ratio=1&rotation=0&showTitle=false&size=321218&status=done&style=stroke&taskId=u17d8d384-d41f-406c-93c7-93ce55db6a8&title=&width=672)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789546882-f0857598-f759-4ae9-814f-dad4fe0cd4e3.png#clientId=ue8a850a2-0457-4&from=paste&height=93&id=ue6fde0cb&name=image.png&originHeight=93&originWidth=766&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71987&status=done&style=stroke&taskId=u0b5fb268-8947-4369-bc39-2d0a118b7b3&title=&width=766)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655789674477-426893c7-fab9-48d0-9131-ac88ee11b20d.png#clientId=ue8a850a2-0457-4&from=paste&height=99&id=ua443d797&name=image.png&originHeight=99&originWidth=757&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76570&status=done&style=stroke&taskId=u35506aef-6afa-4543-8b7b-eaaeb78b672&title=&width=757)
### 5、position - 定位
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655790227695-76c19c3a-8099-45d5-8142-f757e72bfa27.png#clientId=ue8a850a2-0457-4&from=paste&height=325&id=u76c0c80d&name=image.png&originHeight=325&originWidth=635&originalType=binary&ratio=1&rotation=0&showTitle=false&size=162542&status=done&style=stroke&taskId=uc10e81d1-cbed-4384-bee6-8cec1665d54&title=&width=635)
#### ①、fixed - 固定定位
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655790510917-cf699a95-c953-4ea3-8deb-7ba34e3c4e8a.png#clientId=ue8a850a2-0457-4&from=paste&height=292&id=ub4a5cf87&name=image.png&originHeight=292&originWidth=780&originalType=binary&ratio=1&rotation=0&showTitle=false&size=164273&status=done&style=stroke&taskId=u2683a7f7-7814-447b-9e54-5c086ada602&title=&width=780)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655790831198-054c5812-32f5-45e3-b7fb-6dca2a77bc04.png#clientId=ue8a850a2-0457-4&from=paste&height=457&id=u6183037e&name=image.png&originHeight=457&originWidth=513&originalType=binary&ratio=1&rotation=0&showTitle=false&size=224310&status=done&style=stroke&taskId=u84b72850-3430-42d1-bc6a-ec8e76d6548&title=&width=513)
#### ②、relatvie - 相对定位
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655792029021-c7a48690-0f03-48eb-a487-37adeb760bf2.png#clientId=ue8a850a2-0457-4&from=paste&height=386&id=uea8ab894&name=image.png&originHeight=386&originWidth=779&originalType=binary&ratio=1&rotation=0&showTitle=false&size=220177&status=done&style=stroke&taskId=ub0c0824c-8364-4a30-9cd0-fe2b33bfe3d&title=&width=779)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655792025509-a44529d1-57b5-4407-9592-dcab4f418f38.png#clientId=ue8a850a2-0457-4&from=paste&height=431&id=u35f86cf4&name=image.png&originHeight=431&originWidth=901&originalType=binary&ratio=1&rotation=0&showTitle=false&size=197843&status=done&style=stroke&taskId=u86915bd7-d2d6-4e93-834c-aa7a15099d4&title=&width=901)
#### ③、absolute - 绝对定位
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655792851449-bbe98210-21bf-4107-9470-3db209ef0fe9.png#clientId=ue8a850a2-0457-4&from=paste&height=429&id=u80e8614c&name=image.png&originHeight=429&originWidth=781&originalType=binary&ratio=1&rotation=0&showTitle=false&size=287535&status=done&style=stroke&taskId=u2838ab4b-31d8-4ade-84cd-501a2597474&title=&width=781)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793509501-7376247a-aa04-46a2-a9f3-9c716e5dceff.png#clientId=ue8a850a2-0457-4&from=paste&height=233&id=u56792d29&name=image.png&originHeight=233&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=164047&status=done&style=stroke&taskId=u5f913ae3-e510-43ba-a948-7730cd63087&title=&width=786)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655792855268-1d3b7dcf-3a68-46da-8cc7-3b74d64690bd.png#clientId=ue8a850a2-0457-4&from=paste&height=576&id=u8157c6dc&name=image.png&originHeight=576&originWidth=951&originalType=binary&ratio=1&rotation=0&showTitle=false&size=347237&status=done&style=stroke&taskId=u4d6f0eaa-f388-4aba-b351-c7d5337f121&title=&width=951)

- 在父元素中设置一个相对定位

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793060359-9766122f-9f6e-42dd-ae24-d8c59134088d.png#clientId=ue8a850a2-0457-4&from=paste&height=254&id=u83bc38a6&name=image.png&originHeight=254&originWidth=675&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5385&status=done&style=stroke&taskId=ueaba9c30-40df-4110-9781-9aee89193b3&title=&width=675)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655792995695-8fbd11bc-4692-45a0-ba78-5e9d19c59de0.png#clientId=ue8a850a2-0457-4&from=paste&height=612&id=u251a931b&name=image.png&originHeight=612&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=375349&status=done&style=stroke&taskId=ubf89600c-5c6b-4d90-b762-fe21fc28908&title=&width=830)

- 在父元素的父元素中设置一个相对定位

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793212609-aba54cd7-1b27-40ed-96c7-f79399d3ed7a.png#clientId=ue8a850a2-0457-4&from=paste&height=472&id=u55868da8&name=image.png&originHeight=472&originWidth=894&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9121&status=done&style=stroke&taskId=u4bbd499e-c5a7-43fd-b5e5-e16769df06b&title=&width=894)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793240419-b496b233-0316-4a6a-833c-2cc500f0ddf5.png#clientId=ue8a850a2-0457-4&from=paste&height=548&id=uc0dc606b&name=image.png&originHeight=548&originWidth=764&originalType=binary&ratio=1&rotation=0&showTitle=false&size=366892&status=done&style=stroke&taskId=u0c16c97b-e113-497c-bd38-1288c4837ef&title=&width=764)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793408467-938b9157-f4ed-4038-bc69-67556db19dfd.png#clientId=ue8a850a2-0457-4&from=paste&height=153&id=u7c121083&name=image.png&originHeight=153&originWidth=780&originalType=binary&ratio=1&rotation=0&showTitle=false&size=123835&status=done&style=stroke&taskId=u666bda22-6c95-4fbc-9ed2-a97ed9210b3&title=&width=780)

- 案例

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655793930835-0855d80b-48d8-4682-a60e-62adf38563b7.png#clientId=ue8a850a2-0457-4&from=paste&height=586&id=uc7697bb2&name=image.png&originHeight=586&originWidth=882&originalType=binary&ratio=1&rotation=0&showTitle=false&size=372499&status=done&style=stroke&taskId=u51917eca-f11f-4b29-b2f7-7319b1f6a5d&title=&width=882)
### 8、z-index - 竖轴
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655794314419-2d4dee6e-3bf3-471b-9f5b-266acdac96c5.png#clientId=ue8a850a2-0457-4&from=paste&height=179&id=u4cbf8020&name=image.png&originHeight=179&originWidth=785&originalType=binary&ratio=1&rotation=0&showTitle=false&size=152989&status=done&style=stroke&taskId=u4d6a1d0a-c892-4065-877d-bea623e2cf4&title=&width=785)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655794311746-b66417fe-e1eb-4917-93d3-2786ea6b6e8b.png#clientId=ue8a850a2-0457-4&from=paste&height=559&id=u26efeed0&name=image.png&originHeight=559&originWidth=956&originalType=binary&ratio=1&rotation=0&showTitle=false&size=332605&status=done&style=stroke&taskId=u048ed6a8-196d-4269-a7b1-33e67f95ca2&title=&width=956)

- 都设置 z-index 属性

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655794495416-b101b1d2-a7d8-4235-a864-d9ac4bdf128a.png#clientId=ue8a850a2-0457-4&from=paste&height=516&id=ubafb61ca&name=image.png&originHeight=516&originWidth=917&originalType=binary&ratio=1&rotation=0&showTitle=false&size=293266&status=done&style=stroke&taskId=u3e3a5ae1-5e8c-4864-ab8e-d4e7ee227f5&title=&width=917)
## CSS 3

- css 3 和 css 2 的区别
   - css 3 = css 2 + 新语法 + 新属性
   - 就是对 css 2 进行扩充、删减、优化
### 1、结构伪类
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655795103124-339e8463-2318-4c24-80cf-e10c4b86fd78.png#clientId=ue8a850a2-0457-4&from=paste&height=265&id=u663b6e5c&name=image.png&originHeight=265&originWidth=706&originalType=binary&ratio=1&rotation=0&showTitle=false&size=132244&status=done&style=stroke&taskId=u13dc9e4f-ef67-4c30-b940-b4e95291a99&title=&width=706)
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

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655796648605-6673a5b9-df0f-49ed-8a26-a11b01f78a4c.png#clientId=ue8a850a2-0457-4&from=paste&height=726&id=ub980af11&name=image.png&originHeight=726&originWidth=658&originalType=binary&ratio=1&rotation=0&showTitle=false&size=288931&status=done&style=stroke&taskId=u8f201722-cb36-41a8-92c3-aaeb31f5f43&title=&width=658)
### 3、伪元素
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655797000914-7e5d3dfc-089d-40d9-bc57-fc27af7f3910.png#clientId=ue8a850a2-0457-4&from=paste&height=148&id=uc4f34f28&name=image.png&originHeight=148&originWidth=747&originalType=binary&ratio=1&rotation=0&showTitle=false&size=87644&status=done&style=stroke&taskId=u33d82357-ead9-40a1-975d-56d24d7a28e&title=&width=747)
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798026008-3d1ab7c5-5893-4cd3-8a0d-4c9d6c6c1971.png#clientId=ue8a850a2-0457-4&from=paste&height=371&id=u1e9bfbd0&name=image.png&originHeight=371&originWidth=776&originalType=binary&ratio=1&rotation=0&showTitle=false&size=207306&status=done&style=stroke&taskId=u85dfe7c4-5310-443a-b83c-99842f97efa&title=&width=776)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798086792-e205239c-3250-44e5-87b1-95d0035911bf.png#clientId=ue8a850a2-0457-4&from=paste&height=57&id=u02312a31&name=image.png&originHeight=57&originWidth=217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18185&status=done&style=stroke&taskId=u56f213e8-5a25-4be6-90f8-8b19ac9c0e8&title=&width=217)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798073217-8080a775-0719-4ae1-abe3-a92b2ee34ccc.png#clientId=ue8a850a2-0457-4&from=paste&height=602&id=u864664b9&name=image.png&originHeight=602&originWidth=893&originalType=binary&ratio=1&rotation=0&showTitle=false&size=242736&status=done&style=stroke&taskId=ue626a5e9-c460-43e1-bda5-1154e39c106&title=&width=893)

- 设置多组阴影
- ![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798380924-53fb726e-d922-4621-b18d-a4f6f470321b.png#clientId=ue8a850a2-0457-4&from=paste&height=51&id=ufad0ec42&name=image.png&originHeight=51&originWidth=230&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20226&status=done&style=stroke&taskId=u5ae1592e-8ae4-450f-977f-c017c252a55&title=&width=230)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798402536-91e22b8c-81aa-4835-bc38-ba9ccaeb6673.png#clientId=ue8a850a2-0457-4&from=paste&height=258&id=ueddb274a&name=image.png&originHeight=258&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135432&status=done&style=stroke&taskId=u8022c215-4cdf-48cf-b93f-b895ba782c8&title=&width=831)
### 5、盒子阴影
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655799225589-900e740e-7869-437a-87af-5ef7a39fd871.png#clientId=ue8a850a2-0457-4&from=paste&height=503&id=ucf89b32c&name=image.png&originHeight=503&originWidth=754&originalType=binary&ratio=1&rotation=0&showTitle=false&size=288637&status=done&style=stroke&taskId=u376e0d0b-9ffe-48a6-ac45-690d9cee4b0&title=&width=754)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655799003939-9cbf7d6e-6597-4d18-9eca-876451af73e4.png#clientId=ue8a850a2-0457-4&from=paste&height=130&id=ufb25aac8&name=image.png&originHeight=130&originWidth=132&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2815&status=done&style=stroke&taskId=u1ce58e53-cb69-4d35-b735-cf9374751c1&title=&width=132)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655798976894-97c070e0-be1e-409e-b1a7-5cfa7045a671.png#clientId=ue8a850a2-0457-4&from=paste&height=407&id=u4704cd6e&name=image.png&originHeight=407&originWidth=877&originalType=binary&ratio=1&rotation=0&showTitle=false&size=207233&status=done&style=stroke&taskId=u03130a9c-65f5-4bb4-8ff3-1f7f44cd928&title=&width=877)

- 给图片设置阴影

![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655799292516-b7022377-fec5-48d2-8a36-21ad090570ee.png#clientId=ue8a850a2-0457-4&from=paste&height=234&id=uddfe8c95&name=image.png&originHeight=234&originWidth=159&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46455&status=done&style=stroke&taskId=u55d62c68-4a62-4d69-8dbc-a2818c063ec&title=&width=159)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655799305603-2998dd7f-07d2-45db-a382-a6592cf85288.png#clientId=ue8a850a2-0457-4&from=paste&height=438&id=u1c4eb88f&name=image.png&originHeight=438&originWidth=681&originalType=binary&ratio=1&rotation=0&showTitle=false&size=178639&status=done&style=stroke&taskId=u3bd20148-2a55-49e2-977c-ad34732909f&title=&width=681)
### 6、圆角矩形

-  border-radius:  左上 右上 右下 左下
- 如果四个值都是一样的话，只需要写一个参数就可以了
#### 1、圆角矩形
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655800084695-c6a59629-2da8-4e96-a612-4cad8f629040.png#clientId=ue8a850a2-0457-4&from=paste&height=133&id=u86e621c4&name=image.png&originHeight=133&originWidth=261&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3226&status=done&style=stroke&taskId=u8476768a-a02d-4521-b3a2-3026fc5a001&title=&width=261)
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655800704299-ff1b25ea-cdbb-47c7-8add-39b4e0aac419.png#clientId=ue8a850a2-0457-4&from=paste&height=70&id=ue5846d35&name=image.png&originHeight=70&originWidth=137&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5634&status=done&style=stroke&taskId=u35f17747-866c-4894-b737-20c82204f2a&title=&width=137)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655800714860-c16dae89-0c36-4e92-a178-b2243761b874.png#clientId=ue8a850a2-0457-4&from=paste&height=319&id=u8f55c430&name=image.png&originHeight=319&originWidth=615&originalType=binary&ratio=1&rotation=0&showTitle=false&size=167804&status=done&style=stroke&taskId=u75d0671b-519e-42a6-8332-d9acb81e657&title=&width=615)
### 7、透明度
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655857071116-7c3db4d1-0832-4088-b101-5a5e43376401.png#clientId=u047cf215-32f6-4&from=paste&height=262&id=uffb8cdc7&name=image.png&originHeight=262&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=134249&status=done&style=stroke&taskId=u666a4920-e5c1-42d2-aea0-2de62cd201b&title=&width=678)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/29280567/1655857068158-0dffd9ee-4d42-449f-9a3b-57bf5d430c54.png#clientId=u047cf215-32f6-4&from=paste&height=512&id=ud7f8fb2e&name=image.png&originHeight=512&originWidth=662&originalType=binary&ratio=1&rotation=0&showTitle=false&size=255990&status=done&style=stroke&taskId=uad985659-e6e3-417d-bf30-4693bf9e1a2&title=&width=662)






### 
