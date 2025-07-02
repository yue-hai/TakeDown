> [B 站尚硅谷视频](https://www.bilibili.com/video/BV1uK411H7on/?p=68&spm_id_from=pageDriver&vd_source=b55e15966ca689b32671d4aa387cab01)
> 
> [尚硅谷前端_ES6.pdf](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/尚硅谷前端_ES6.pdf)

# 一、ECMASript 相关介绍

## 1、什么是 ECMA

 ECMA（European Computer Manufacturers Association）中文名称为欧洲计算机制 造商协会，这个组织的目标是评估、开发和认可电信和计算机标准。1994 年后该 组织改名为 Ecma 国际。  

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-16-861--7dWDchtM-93w_Q.png)

## 2、什么是 ECMAScript

ECMAScript 是由 Ecma 国际通过 ECMA-262 标准化的脚本程序设计语言

## 3、什么是 ECMA-262

 Ecma 国际制定了许多标准，而 ECMA-262 只是其中的一个，所有标准列表查看：
 
> http://www.ecma-international.org/publications/standards/Standard.htm

## 4、ECMA-262 历史

 ECMA-262（ECMAScript）历史版本查看网址:
 
> http://www.ecma-international.org/publications/standards/Ecma-262-arch.htm
> 
>  注：从 ES6 开始，每年发布一个版本，版本号比年份最后一位大 1  

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-17-514--1f8ENp9t60O5MQ.png)

## 5、谁在维护 ECMA-262

TC39（Technical Committee 39）是推进 ECMAScript 发展的委员会。其会员都是公司（其中主要是浏览器厂商，有苹果、谷歌、微软、因特尔等）。TC39 定期召开会议，会议由会员公司的代表与特邀专家出席

## 6、为什么要学习 ES6

1. ES6 的版本变动内容最多，具有里程碑意义
2. ES6 加入许多新的语法特性，编程实现更简单、高效
3. ES6 是前端发展趋势，就业必备技能

# 二、ECMASript 6 新特性

## 1、let 关键字

let 关键字用来声明变量，使用 let 声明的变量有几个特点：

1. 不允许重复声明
2. 块儿级作用域
3. 不存在变量提升：不允许在变量声明之前调用变量
4. 不影响作用域链
5. 应用场景：以后声明变量使用 let 就对了

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
    <h2>let</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 声明变量
        let a;
        let b, c, d;
        let e = 100;
        let f = 200, g = "月海", h = [1, 2, 3];

        console.log(a,b,c,d,e,f,g,h);

        // 1、不允许重复声明
        // let a = 111;
        // console.log(a);

        // 2、块儿级作用域：function、if、while、for 等
        // {
        //     let i = 1;
        //     console.log(i);
        // }
        // console.log(i);

        // 3、不存在变量提升：不允许在变量声明之前调用变量
        
        // 4、不影响作用域链
        {
            let g = 1;
            function fun(){
                console.log(g);
            }
            fun()
        }

    })
    
</script>

</html>
```

## 2、const 关键字

const 关键字用来声明常量，const 声明有以下特点

1. 声明必须赋初始值
2. 标识符一般为大写
3. 不允许重复声明
4. 值不允许修改
5. 对数组和对象的元素进行修改，不算对常量的修改
6. 块儿级作用域
7. 注意: 对象属性修改和数组元素变化不会出发 const 错误
8. 应用场景：声明对象类型使用 const，非对象类型声明选择 let

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
    <h2>const</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 1、声明必须赋初始值
        // 2、标识符一般为大写（习惯）
        const A = 1;

        console.log(A);

        // 3、不允许重复声明
        // const a = 111;
        // console.log(a);

        // 4、值不允许修改
        // A = 2;

        // 5、对数组和对象的元素进行修改，不算对常量的修改
        const YUEHAI = {
            name:"月海",
            age:16
        }
        console.log(YUEHAI);

        YUEHAI.age = 14
        console.log(YUEHAI);

        // 6、块儿级作用域：function、if、while、for 等
        {
            const i = 1;
            console.log(i);
        }
        console.log(i);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-17-531--rzV4U1Oq1W_02g.png)

## 3、变量的解构赋值

1. ES6 允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构赋值
2.  注意：频繁使用对象方法、数组元素，就可以使用解构赋值形式 

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
    <h2>变量的解构赋值</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 1、数组的解构
        // 1.1、创建数组
        const nanGong = ["月海", "言", "羽"]
        // 1.2、解构赋值
        let [yuehai, yan, yu] = nanGong
        console.log(nanGong);
        console.log(yuehai);
        console.log(yan);
        console.log(yu);

        // 2、对象的解构
        // 2.1、创建对象
        const nanGong2 = {
            yuehai2:"月海", 
            yan2:"言", 
            yu2:"羽",
            fun2: function(){
                console.log("南宫");
            }
        }
        // 2.2、解构赋值
        let {yuehai2, yan2, yu2, fun2} = nanGong2
        console.log(nanGong2);
        console.log(yuehai2);
        console.log(yan2);
        console.log(yu2);
        fun2();
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-17-648--qHPrIi-vmbkEYg.png)

## 4、模板字符串

 模板字符串（template string）是增强版的字符串，用反引号 ``` 标识，特点：

1. 字符串中可以出现换行符
2. 可以使用 `${xxx}` 形式输出变量 
3. 注意：当遇到字符串与变量拼接的情况使用模板字符串

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
    <h2>模板字符串</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 1、声明
        let str = `月海`;
        console.log(str);

        // 2、字符串中可以出现换行符
        let str2 = `<ul>
                        <li>月海</li>
                        <li>言</li>
                        <li>羽</li>
                    </ul>`;
        console.log(str2);

        // 3、变量拼接
        let str3 = 14;
        let yuehai = `${str}-${str3}`
        console.log(yuehai);
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-17-778--AhtjEBH8oyiHeA.png)

## 5、简化对象写法

ES6 允许在大括号里面，直接写入变量和函数，作为对象的属性和方法。这样的书写更加简洁

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
    <h2>简化对象写法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 1、原先的写法，直接声明变量
        const yuehai = {
            name:"月海", 
            age:16
        }
        console.log(yuehai);

        // 2、简化对象写法
        // 2.1、先声明对象
        let name2 = "言";
        let age2 = 14;
        // 2.2、在对象中写入已经声明的对象
        const yan = {
            name2, 
            age2
        }
        console.log(yan);

        // 3、简化方法的写法
        const yu = {
            name:"羽", 
            age:18,
            play(){
                console.log("玩");
            }
        }
        console.log(yu);
        yu.play();
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-17-941--ytNcc3Wxbee06g.png)

## 6、箭头函数

 ES6 允许使用「箭头」（=>）定义函数 ， 箭头函数的注意点 ：

1.  如果形参只有一个，则小括号可以省略
2. 函数体如果只有一条语句，则花括号可以省略，函数的返回值为该条语句的 执行结果
3. this 是静态的，箭头函数 this 始终指向声明时所在作用域下 this 的值
4. 箭头函数不能作为构造函数实例化
5. 不能使用 arguments  
6. 注意：箭头函数不会更改 this 指向，用来指定回调函数会非常合适

---

1. 箭头函数适合与 this 无关的回调，定时器、数组的方法回调
2. 箭头函数不适合与 this 有关的回调，事件回调、对象的方法

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
    <h2>简化对象写法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // 1、原先的写法
        let fun = function(){
            console.log("1、原先的写法");
        }
        fun();

        // 2、箭头函数
        let fun2 = () => {
            console.log("2、箭头函数");
        }
        fun2();

        // 3、传递参数
        let fun3 = (a, b) => {
            console.log(`3、传递参数：${a}、${b}`);
        }
        fun3(1, 2);

        // 4、如果形参只有一个，则小括号可以省略
        let fun4 = a => {
            console.log(`4、如果形参只有一个，则小括号可以省略：${a}`);
        }
        fun4(1);

        // 5、函数体如果只有一条语句，则花括号可以省略，函数的返回值为该条语句的 执行结果
        let fun5 = (a, b) => console.log(`5、函数体如果只有一条语句，则花括号可以省略，函数的返回值为该条语句的 执行结果：${a}、${b}`);
        fun5(1, 2);

        // 6、this 是静态的，箭头函数 this 始终指向声明时所在作用域下 this 的值
        function fun6_1(){
            console.log(this.name);
        }
        let fun6_2 = () => {
            console.log(this.name);
        }
        window.name = "月海";
        const yuehai = {
            name: "yuehai"
        }
        fun6_1();
        fun6_2();

        // 7、箭头函数不能作为构造函数实例化
        // let fun7 = (name,age) => {
        //     this.name = name;
        //     this.age = age;
        // }
        // let fun7_2 = new fun7();

        // 8、不能使用 arguments  
        let fun8 = () => {
            console.log(arguments);
        }
        fun8(1);
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-021--Z4iNKsXB8A3SPg.png)

## 7、函数参数默认值

1. 可以给参数设置默认值
2. 具有默认值的参数，一般放在最后面
3. 可以与结构赋值结合使用

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
    <h2>rest 参数</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // ES6 引入 rest 参数，用于获取函数的实参，用来代替 arguments
        function add(a,b,c=10){
            console.log(a+b+c);
        }
        add(1,2);
        add(1,2,20);

        // 可以与结构赋值结合使用
        // 之前的方式
        function yuehai(yuehai){
            console.log(yuehai.name);
            console.log(yuehai.age);
        }
        // 调用函数，传递对象
        yuehai({
            name:"月海",
            age:16
        })

        // 现在的方式，与结构赋值结合使用
        function yan({name, age}){
            console.log(name);
            console.log(age);
        }
        // 调用函数，传递对象
        yan({
            name:"言",
            age:14
        })

        // 现在的方式，与结构赋值结合使用，赋初始值
        function yu({name, age=18, sex}){
            console.log(name);
            console.log(age);
            console.log(sex);
        }
        // 调用函数，传递对象
        yu({
            name:"羽",
            sex:1
        }) 
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-177--7UEmPLZSRwFZKQ.png)

## 8、 rest 参数

1. ES6 引入 rest 参数，用于获取函数的实参，用来代替 arguments；
2. rest 参数必须放到参数的最后
3.  注意：rest 参数非常适合不定个数参数函数的场景

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
    <h2>rest 参数</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        // ES6 引入 rest 参数，用于获取函数的实参，用来代替 arguments
        // 以前使用 arguments
        function data(){
            console.log(arguments, typeof arguments);
        }
        data(1, 2, 3)

        // 现在使用 rest 参数
        function data2(...args){
            // 打印
            console.log(args, typeof args);
            for (let i = 0; i < args.length; i++) {
                console.log(args[i], typeof args[i]);
            }
        }
        data2(4, 5, 6)
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-274--OYNyDGcfQj9KXg.png)

## 9、spread 扩展运算符

1. 扩展运算符（spread）也是三个点 `...`
2. 它好比 rest 参数的逆运算，将一个数组转为用逗号分隔的参数序列，对数组进行解包

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
    <h2>spread 扩展运算符</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个数组
        const arr = ["月海","言","羽"];
        // 声明一个函数
        function name(...args){
            console.log(args);
        }

        // 以前的方式调用函数，传递的是一整个数组
        // 相当于：name(["月海","言","羽"])
        name(arr)

        // 使用 spread 扩展运算符，是将组分割开来分别传入
        // 相当于：name("月海","言","羽")
        name(...arr)
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-369--WsFx8E658KqAlA.png)

## 10、Symbol

> [https://es6.ruanyifeng.com/#docs/symbol](https://es6.ruanyifeng.com/#docs/symbol)

### ①、Symbol 基本使用

ES6 引入了一种新的原始数据类型 Symbol，表示独一无二的值。它是 JavaScript 语言的第七种数据类型，是一种类似于字符串的数据类型；感觉类似 java 中的常量

Symbol 特点：

1. Symbol 的值是唯一的，用来解决命名冲突的问题
2. Symbol 值不能与其他数据进行运算
3. Symbol 定义的对象属性不能使用 for…in 循环遍历，但是可以使用Reflect.ownKeys 来获取对象的所有键名
4. 注: 遇到唯一性的场景时要想到 Symbol

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
    <h2>spread 扩展运算符</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 方式一：对象方式创建
        let s = Symbol();
        let s2 = Symbol("月海");
        let s3 = Symbol("月海");
        // 数据类型为 Symbol
        console.log(s, typeof s);
        console.log(s2, typeof s2);
        console.log(s3, typeof s3);
        // 这种方式创建的 Symbol 不相等
        console.log(s2 === s3);

        // 方式二：函数对象创建
        let s4 = Symbol.for("月海");
        let s5 = Symbol.for("月海");
        console.log(s4, typeof s4);
        console.log(s5, typeof s5);
        // 这种方式创建的 Symbol 相等
        console.log(s4 === s5);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-528--GSi9wk_2iMw5Qw.png)

### ②、对象添加 Symbol 类型的属性

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
    <h2>对象添加 Symbol 类型的属性</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 创建对象，向对象中添加方法 up down
        // 需求：向其中添加方法
        let game = {
            name:'俄罗斯方块',
            up: function(){},
            down: function(){}
        };
        // 创建第二个对象，也向对象中添加方法 up、down、yuehai
        // 防止对象 game 中没有这三个方法
        let methods = {
            up: Symbol(),
            down: Symbol(),
            yuehai: Symbol()
        };
        // 向 game 中添加方法
        game[methods.up] = function(){
            console.log("我可以改变形状");
        }
        game[methods.down] = function(){
            console.log("我可以快速下降!!");
        }
        game[methods.yuehai] = function(){
            console.log("月海");
        }
        console.log(game);

        // 另一种方式创建对象方法
        let youxi = {
            name:"狼人杀",
            [Symbol('say')]: function(){
                console.log("我可以发言")
            },
            [Symbol('zibao')]: function(){
                console.log('我可以自爆');
            }
        }
        console.log(youxi)
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-823--TQvU2oq7RNohrg.png)

### ③、Symbol 内置值

除了定义自己使用的 Symbol 值以外，ES6 还提供了 11 个内置的 Symbol 值，指向语言内部使用的方法。可以称这些方法为魔术方法，因为它们会在特定的场景下自动执行

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-18-999--s-P1-W9WrNPuqQ.png)

## 11、迭代器

### ①、迭代器的使用

遍历器（Iterator）就是一种机制。它是一种接口，为各种不同的数据结构提供统一的访问机制。任何数据结构只要部署 Iterator 接口（对象里的一个属性：Symbol.iterator），就可以完成遍历操作。

1. ES6 创造了一种新的遍历命令 for...of 循环，Iterator 接口主要供 for...of 消费
2. 原生具备 iterator 接口的数据(可用 for of 遍历)
   1. Array
   2. Arguments
   3. Set
   4. Map
   5. String
   6. TypedArray
   7. NodeList
3. 工作原理
   1. 创建一个指针对象，指向当前数据结构的起始位置
   2. 第一次调用对象的 next 方法，指针自动指向数据结构的第一个成员
   3. 接下来不断调用 next 方法，指针一直往后移动，直到指向最后一个成员
   4. 每调用 next 方法返回一个包含 value 和 done 属性的对象

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
    <h2>迭代器</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个数组
        const yuehai = ["月海",16,168,50];

        // for 循环遍历
        for (let i = 0; i < yuehai.length; i++) {
            console.log(yuehai[i]);
        }
        // for of 循环遍历
        for (const iterator of yuehai) {
            console.log(iterator);
        }
        // 打印数组
        console.log(yuehai);

        // 获取数组 yuehai 的 Symbol.iterator 属性
        let iterator = yuehai[Symbol.iterator]();
        // 工作原理：
        console.log(iterator.next());
        console.log(iterator.next());
        console.log(iterator.next());
        console.log(iterator.next());
        console.log(iterator.next());
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-234--a_7JSDHSxdRAuw.png)

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-358--Jh_IufeLGYV6Ug.png)

### ②、自己实现迭代器

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
    <h2>自己实现迭代器</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个对象，再对象中声明一个数组
        const yuehai = {
            name: "月海",
            property: [
                "yuehai", 16, 168, 50
            ],
            // 自己实现迭代器
            [Symbol.iterator](){
                // 索引变量
                let index = 0;
                // 将 yuehai 这个对象赋值给 _this
                let _this = this
                return {
                    next: function(){
                        // 判断数组长度
                        if(index < _this.property.length){
                            const result = {
                                // 返回的值
                                value: _this.property[index],
                                // 返回的状态
                                done: false
                            }
                            // 索引自增
                            index++;
                            // 返回 result
                            return result;
                        }else{
                            return {
                                // 返回的值
                                value: undefined,
                                // 返回的状态
                                done: true
                            }
                        }
                    }
                }
            }
        };

        // for 循环遍历对象中的数组
        for (let i = 0; i < yuehai.property.length; i++) {
            console.log(yuehai.property[i]);
        }

        // 使用 for of 迭代器遍历
        for (const iterator of yuehai.property) {
            console.log(iterator);
        }

        // 使用 for of 自己实现的迭代器遍历
        for (const iterator of yuehai) {
            console.log(iterator);
        }

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-449--GLG7qUS6pufVaA.png)

## 12、生成器

### ①、生成器的使用

生成器函数是 ES6 提供的一种异步编程解决方案，语法行为与传统函数完全不同

1. `*` 的位置没有限制
2. 生成器函数返回的结果是迭代器对象，调用迭代器对象的 `next` 方法可以得到 `yield` 语句后的值
3. `yield` 相当于函数的暂停标记，也可以认为是函数的分隔符，每调用一次 `next` 方法，执行一段代码
4. `next` 方法可以传递实参，作为 `yield` 语句的返回值

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
    <h2>生成器</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 生成器其实就是一个特殊的函数
        // 异步编程纯回调函数 node fs ajax mongodb
        // yield 相当于函数的暂停标记，也可以认为是函数的分隔符，每调用一次 next 方法，执行一段代码
        function * yuehai(){
            console.log(1);
            yield "第 1 段代码"

            console.log(2);
            yield "第 2 段代码"

            console.log(3);
            yield "第 3 段代码"

            console.log(4);
            yield "第 4 段代码"
        }

        let iterator = yuehai();
        // 调用一次，输出：1
        iterator.next()
        // 调用二次，输出：2
        iterator.next()
        // 调用三次，输出：3
        iterator.next()
        // 调用四次，输出：4
        iterator.next()
        // 调用五次，没有输出
        iterator.next()

        // 遍历
        for (const iterator of yuehai()) {
            // 既返回每一段代码，也返回 yield 的值
            console.log(iterator);
        }

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-536--vIQ4ukqx00HyMg.png)

### ②、生成器参数的传递

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
    <h2>生成器</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 生成器其实就是一个特殊的函数
        // 异步编程纯回调函数 node fs ajax mongodb
        // yield 相当于函数的暂停标记，也可以认为是函数的分隔符，每调用一次 next 方法，执行一段代码
        function * yuehai(arg){

            console.log(arg);
            console.log(1);
            let one = yield "第 1 段代码"

            console.log(one);
            console.log(2);
            let two = yield "第 2 段代码"

            console.log(two);
            console.log(3);
            yield "第 3 段代码"

            console.log(4);
            yield "第 4 段代码"
        }

        // 调用函数时传递参数，会在第一次调用 next() 方法时输出传递的参数
        let iterator = yuehai("zero");
        // 调用一次，输出：10000、1；本次传递的参数不会被输出
        iterator.next(11111);
        // 调用二次，输出：22222、2；作为第一个 yield 语句的值输出
        iterator.next(22222);
        // // 调用三次，输出：33333、3；作为第二个 yield 语句的值输出
        iterator.next(33333);
        // // 调用四次，输出：4
        // iterator.next();
        // // 调用五次，没有输出
        // iterator.next();

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-624--aZ_wf6XR_u5RwA.png)

### ③、生成器案例解决回调地狱

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
    <h2>生成器案例</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 异步编程  文件操作 网络操作(ajax, request) 数据库操作
        // 1s 后控制台输出 111  2s后输出 222  3s后输出 333 
        // 回调地狱，以前的写法
        // setTimeout(() => {
        //     console.log(111);
        //     setTimeout(() => {
        //         console.log(222);
        //         setTimeout(() => {
        //             console.log(333);
        //         }, 3000);
        //     }, 2000);
        // }, 1000);

        function one(){
            setTimeout(()=>{
                console.log(111);
                // 调用迭代器，让代码自动向下运行
                iterator.next();
            },1000)
        }
        function two(){
            setTimeout(()=>{
                console.log(222);
                // 调用迭代器，让代码自动向下运行
                iterator.next();
            },2000)
        }
        function three(){
            setTimeout(()=>{
                console.log(333);
                // 调用迭代器，让代码自动向下运行
                iterator.next();
            },3000)
        }
        // 创建生成器函数，放入之前定义的函数
        function * gen(){
            yield one();
            yield two();
            yield three();
        }

        //调用生成器函数
        let iterator = gen();
        iterator.next();

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-769--gBHvOb2_rNtLGw.png)

### ④、依照顺序调用指定函数获得数据

1. 不可以直接调用的原因是这些数据再实际中是包含关系，需依次获得
2. 先得到用户数据，基于用户数据获得订单数据，再基于订单数据获得商品数据

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
    <h2>生成器案例2</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        //模拟获取  用户数据  订单数据  商品数据 
        function getUsers(){
            setTimeout(()=>{
                let data = '用户数据';
                // 调用 next 方法, 并且将数据传入
                iterator.next(data);
            }, 1000);
        }

        function getOrders(){
            setTimeout(()=>{
                let data = '订单数据';
                iterator.next(data);
            }, 1000)
        }

        function getGoods(){
            setTimeout(()=>{
                let data = '商品数据';
                iterator.next(data);
            }, 1000)
        }

        function * gen(){
            let users = yield getUsers();
            // 打印传递过来的参数：用户数据
            console.log(users);

            let orders = yield getOrders();
            // 打印传递过来的参数：订单数据
            console.log(orders);

            let goods = yield getGoods();
            // 打印传递过来的参数：商品数据
            console.log(goods);

        }

        // 调用生成器函数
        let iterator = gen();
        iterator.next();
        

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-19-872--zEVygpAtHaivvg.png)

## 13、Promise

Promise 是 ES6 引入的异步编程的新解决方案。语法上 Promise 是一个构造函数，用来封装异步操作并可以获取其成功或失败的结果。

1. Promise 构造函数:：`Promise (excutor) {}`
2. `Promise.prototype.then` 方法
3. `Promise.prototype.catch` 方法

---

- 状态返回值：
   - pending：进行中；在到达 fulfilled、rejected 状态前 promise 都处在 pending 状态
   - fulfilled：已完成
   - rejected：已失败
   - resolved：可当作 fulfilled 状态；表示 Promise 对象处于 settled 状态，或者 Promise 对象被锁定在了调用链中

> resolved 的具体解析可以看这里： [https://blog.csdn.net/weixin_45697314/article/details/107057094](https://blog.csdn.net/weixin_45697314/article/details/107057094)

Promise有三种状态：

1. 如果用Promise()构造器创建一个Promise对象，当被创建时，它的状态是pending
2. 如果一个Promise对象的resolve方法被调用，它的状态会变成fulfilled
3. 而如果一个Promise对象的reject方法被调用，它的状态会变成rejected
4. 此外，还有两种初始化Promise对象的方法，分别是Promise.resolve方法和Promise.reject方法，前者会直接返回一个状态为fulfilled的Promise对象而后者会直接返回一个状态为rejected的Promise对象。

1. 在一个Promise链中，如果一个Promise状态变成了fulfilled，它会自动在Promise链中向下寻找，直到发现一个then方法，并执行其中的第一个参数函数
2. 而如果一个Promise的状态变成了rejected，它会在Promise链中向下寻找，直到发现一个带有两个参数的then方法并执行它的第二个参数函数或发现一个catch方法并执行它的参数函数

### ①、Promise 使用

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
    <h2>Promise</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        //生成随机数
        function rand(m,n){
            return Math.ceil(Math.random() * (n-m+1)) + m-1;
        }
        
        // 实例化 Promise 对象
        // resolve：解决，函数类型的数据，异步任务成功调用他
        // reject： 拒绝，函数类型的数据，异步任务失败调用他
        const promise = new Promise(function(resolve, reject){
            // 生成 1-100 的随机数
            let n = rand(1, 100);
            // 判断
            if(n <= 30){
                // 将 promise 的状态设置为成功
                resolve();
            }else{
                // 将 promise 的状态设置为失败
                reject();
            }
        })

        // 调用 then 方法
        // 需要两个参数，都是函数
        // 参数1：promise 成功时执行的函数
        // 参数2：promise 失败时执行的函数
        promise.then(function(value){
            console.log("中奖");
        }, function(reason){
            console.log("未中奖");
        })

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-039--Azm8kJzLeUwf9Q.png)

### ②、Promise 封装读取文件

#### Ⅰ、调用方法读取文件

```javascript
// 1、引入 fs 模块
const fs = require("fs");

// 2、调用方法读取文件
fs.readFile("13、Promise.html", (err, data) => {
    // 如果失败，则抛出错误
    if(err) throw err;

    // 如果没有出错，则输出内容
    console.log(data.toString());
})
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-181--asPZGfnh7tpalw.png)

#### Ⅱ、使用 Promise 封装

##### （1）、成功

```javascript
// 1、引入 fs 模块
const fs = require("fs");

// 2、使用 Promise 封装
// resolve：解决，函数类型的数据，异步任务成功调用他
// reject： 拒绝，函数类型的数据，异步任务失败调用他
const promise = new Promise(function(resolve, reject){
    fs.readFile("13、Promise.html", (err, data) => {
        // 如果失败，则抛出错误
        if(err) reject(err);
    
        // 如果没有出错，则输出内容
        resolve(data)
    })
})

// 调用 then 方法
// 需要两个参数，都是函数
// 参数1：promise 成功时执行的函数
// 参数2：promise 失败时执行的函数
promise.then(function(value){
    console.log(value.toString());
}, function(reason){
    console.log("读取失败");
})


```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-343--WibTZe-ilkD2nA.png)

##### （2）、失败

```javascript
// 1、引入 fs 模块
const fs = require("fs");

// 2、使用 Promise 封装
// resolve：解决，函数类型的数据，异步任务成功调用他
// reject： 拒绝，函数类型的数据，异步任务失败调用他
const promise = new Promise(function(resolve, reject){
    fs.readFile("13、Promise.htmlllllllllll", (err, data) => {
        // 如果失败，则抛出错误
        if(err) reject(err);
    
        // 如果没有出错，则输出内容
        resolve(data)
    })
})

// 调用 then 方法
// 需要两个参数，都是函数
// 参数1：promise 成功时执行的函数
// 参数2：promise 失败时执行的函数
promise.then(function(value){
    console.log(value.toString());
}, function(reason){
    console.log("读取失败");
})


```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-445--GS_lNY6l6j73Rg.png)

### ③、Promise 封装 AJAX

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
    <h2>Promise封装AJAX</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 接口地址: https://api.apiopen.top/api/sentences
        const p = new Promise((resolve, reject) => {
            // 1. 创建对象
            const xhr = new XMLHttpRequest();

            // 2. 初始化
            xhr.open("GET", "https://api.apiopen.top/api/sentences");

            // 3. 发送
            xhr.send();

            // 4. 绑定事件, 处理响应结果
            xhr.onreadystatechange = function () {
                // 判断
                if (xhr.readyState === 4) {
                    // 判断响应状态码 200-299
                    if (xhr.status >= 200 && xhr.status < 300) {
                        // 表示成功
                        resolve(xhr.response);
                    } else {
                        // 如果失败
                        reject(xhr.status);
                    }
                }
            }
        })
        
        //指定回调
        p.then(function(value){
            // 输出字符串
            console.log(value);

            // 将字符串转为对象
            let json = JSON.parse(value);
            console.log(json);

            console.log(`名句：${json.result.name}`);
            console.log(`作者：${json.result.from}`);
        }, function(reason){
            console.error(reason);
        });

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-598--0WEx208v22wVaQ.png)

### ④、`Promise.prototype.then` 方法

#### Ⅰ、回调处理

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
    <h2>Promise.prototype.then方法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建 promise 对象
        // resolve：解决，函数类型的数据，异步任务成功调用他
        // reject： 拒绝，函数类型的数据，异步任务失败调用他
        const promise = new Promise((resolve, reject)=>{
            resolve('成功');
            // reject('失败');
        });

        // 调用 then 方法
        // 需要两个参数，都是函数
        // 参数1：promise 成功时执行的函数
        // 参数2：promise 失败时执行的函数
        promise.then(function(value){
            console.log("成功");
        }, function(reason){
            console.log("失败");
        })

    })
    
</script>

</html>
```

#### Ⅱ、返回结果

1. then 方法的返回结果是 Promise 对象, 对象状态由回调函数的执行结果决定

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-20-768--aOmU5-ZJu1sbMA.png)

2. 如果回调函数中返回的结果是 非 promise 类型的属性, 状态为成功, 返回值为对象的成功的值

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-21-996--E_y7rAEzYILkkg.png)

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
    <h2>Promise.prototype.then方法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建 promise 对象
        const promise = new Promise((resolve, reject)=>{
            resolve('成功');
            // reject('失败');
        });

        // 调用 then 方法
        // then 方法的返回结果是 Promise 对象, 对象状态由回调函数的执行结果决定
        // 如果回调函数中返回的结果是 非 promise 类型的属性, 状态为成功, 返回值为对象的成功的值
        const result = promise.then(function(value){
            console.log("成功");
            return "成功"
        }, function(reason){
            console.log("失败");
        })

        console.log(result);

    })
    
</script>

</html>
```

#### Ⅲ、链式调用

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
    <h2>Promise.prototype.then方法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建 promise 对象
        const promise = new Promise((resolve, reject)=>{
            resolve('成功');
            // reject('失败');
        });

        // 链式调用；避免回调地狱
        promise.then(value => {

        }, reject => {

        }).then(value => {

        }, reject => {

        })
    })
    
</script>

</html>
```

### ⑤、Promise 读取多个文件内容

#### Ⅰ、回调方式

```javascript
// 引入 fs 模块
const fs = require("fs");

// 回调方式
// 按顺序引入，一次性全部输出
fs.readFile("./resources/为学.md", (err, data) => {
    fs.readFile("./resources/插秧诗.md", (err, data2) => {
        fs.readFile("./resources/观书有感.md", (err, data3) => {
            let result = data + '\r\n' + data2 + '\r\n' + data3;
            console.log(result)
        })
    })
})
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-22-331--NSIDgCKfniPcFw.png)

#### Ⅱ、Promise

```javascript
// 引入 fs 模块
const fs = require("fs");

// 定义读取文件的函数
function chaYangShi(val){
    // 创建匿名 Promise 对象
    return new Promise((resolve, reject) => {
        fs.readFile("./resources/插秧诗.md", (err, data) => {
            resolve([val, data])
        })
    })
}
function guanShuYouGan(val){
    return new Promise((resolve, reject) => {
        fs.readFile("./resources/观书有感.md", (err, data) => {
            // 将本次读取的文件数据压入传递过来的数组中
            val.push(data);
            resolve(val);
        })
    })
}

// Promise
// 按顺序引入，一次性全部输出，首先读取第一个文件
const promise = new Promise((resolve, reject) => {
    fs.readFile("./resources/为学.md", (err, data) => {
        // 放回成功
        resolve(data)
    })
})

promise.then((val) => {
    // 调用第二个文件，将上面传过来的数据传递给函数
    return chaYangShi(val);
}).then((val) => {
    // 调用第三个文件，将上面传过来的数据传递给函数
    return guanShuYouGan(val);
}).then((val) => {
    // 输出
    console.log(val.join('\r\n'));
})
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-22-485--mJtTtNmxpBkxjQ.png)

### ⑥、`Promise.prototype.catch` 方法

- `catch` 方法相当于只指定失败的 `then` 方法

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
    <h2>Promise.prototype.catch方法</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建 promise 对象
        const promise = new Promise((resolve, reject)=>{
            // resolve('成功');
            reject('失败');
        });

        // 调用 then 方法
        // const result = promise.then(function(value){
        //     console.log("成功");
        // }, function(reason){
        //     console.log("失败");
        // })

        // 调用 catch 方法
        promise.catch((reason) => {
            console.log("失败");
        })

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-22-630--A9s4PhAeCGhZVg.png)

## 14、Set（集合）

ES6 提供了新的数据结构 Set（集合）。它类似于数组，但成员的值都是唯一的，集合实现了 iterator 接口，所以可以使用『扩展运算符』和『for…of…』进行遍历，集合的属性和方法：

1. `size`：返回集合的元素个数
2. `add`：增加一个新元素，返回当前集合
3. `delete`：删除元素，返回 boolean 值
4. `has`：检测集合中是否包含某个元素，返回 boolean 值
5. `clear`：清空集合，返回 undefined

### ①、使用方法

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
    <h2>Set（集合）</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建一个 set 集合
        let s = new Set();
        // 查看类型
        console.log(s, typeof s);

        // set 集合的值都是唯一的
        let s2 = new Set(["月海","言","月海","羽"]);
        // 查看类型
        console.log(s2, typeof s2);

        // size：返回集合的元素个数
        console.log(s2.size);

        // add：增加一个新元素，返回当前集合
        s2.add("烟花烬头")
        console.log(s2);

        // delete：删除元素，返回 boolean 值
        s2.delete("言");
        console.log(s2);

        // has：检测集合中是否包含某个元素，返回 boolean 值
        console.log(s2.has("月海"));
        console.log(s2.has("言"));

        // clear：清空集合，返回 undefined
        s2.clear();
        console.log(s2);

        // 使用 for…of… 进行遍历
        let s3 = new Set(["月海","言","月海","羽"]);
        for (const iterator of s3) {
            console.log(iterator);
        }
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-22-721--Zpkfnqn-oEKx7w.png)

### ②、案例：去重、交集、并集、差集

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
    <h2>Set（集合）</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 数组
        let arr = [1,2,3,4,5,4,3,2,1]
        let arr2 = [4,5,6,5,6,7];
        
        // 去重
        let s1 = [...new Set(arr)]
        console.log(s1);

        // 交集
        // let arr2_2 = new Set(arr2);
        // // filter：它创建一个新数组，新数组中的元素是通过检查指定数组中符合条件的所有元素
        // let s2 = [...new Set(arr)].filter(item => {
        //     if(arr2_2.has(item)){
        //         return true;
        //     }else{
        //         return false;
        //     }
        // })
        // console.log(s2);
        // 简化上面的代码：
        let s2 = [...new Set(arr)].filter(item => new Set(arr2).has(item) )
        console.log(s2);

        // 并集
        let s3 = [...new Set([...arr, ...arr2])]
        console.log(s3);

        // 差集；数组 arr 相对于 数组 arr2 的差集
        // 与交集类似，条件判断取反
        let s4 = [...new Set(arr)].filter(item => !(new Set(arr2).has(item)) )
        console.log(s4);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-014--diboPBlszkZgaw.png)

## 15、Map（键值对的集合）

ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合。但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。Map 也实现了 iterator 接口，所以可以使用『扩展运算符』和『for…of…』进行遍历。Map 的属性和方法：

1. set 增加一个新元素，返回当前 Map
2. size 返回 Map 的元素个数
3. get 返回键名对象的键值
4. has 检测 Map 中是否包含某个元素，返回 boolean 值
5. clear 清空集合，返回 undefined

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
    <h2>Map（键值对的集合）</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 创建一个 set 集合
        let map = new Map();
        // 查看类型
        console.log(map, typeof map);

        // set：增加一个新元素；前面是键，后面是值
        map.set("言","羽");
        map.set(1,["月海","言","羽"]);
        map.set("月海",{
            name: "月海",
            age: 16
        });
        // 键不可重复
        map.set("言","月海");
        console.log(map);

        // size：返回集合的元素个数
        console.log(map.size);

        // get 返回键名对象的键值
        console.log(map.get("言"));
        console.log(map.get(1));

        // has 检测 Map 中是否包含某个元素，返回 boolean 值
        console.log(map.has(1));
        console.log(map.has(2));

        // 使用 for…of… 进行遍历
        console.log("----遍历开始----");
        for (const iterator of map) {
            console.log(iterator);
        }
        console.log("----遍历结束----");

        // clear 清空集合，返回 undefined
        // map.clear();
        // console.log(map);
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-176--F3dM_AQiTlV3gA.png)

## 16、class 类

ES6 提供了更接近传统语言的写法，引入了 Class（类）这个概念，作为对象的模板。通过 class 关键字，可以定义类。基本上，ES6 的 class 可以看作只是一个语法糖，它的绝大部分功能，ES5 都可以做到，新的 class 写法只是让对象原型的写法更加清晰、更像面向对象编程的语法而已。知识点：

1. class 声明类
2. constructor 定义构造函数初始化
3. extends 继承父类
4. super 调用父级构造方法
5. static 定义静态方法和属性
6. 父类方法可以重写

### ①、以前的方式

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
    <h2>class 类-以前的方式</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 定义函数
        function Person(name, age) {
            this.name = name;
            this.age = age;
        }

        // 添加方法
        Person.prototype.property = function(name){
            console.log(this.name + "的属性：");
        }

        // 实例化对象
        let yuehai = new Person("月海", 16);
        // 调用添加的方法
        yuehai.property();
        // 调用属性
        console.log(yuehai);
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-291--8MN33Co1yVfCQw.png)

### ②、class 类方式

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
    <h2>class 类方式</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 定义类
        class Person{
            // constructor：构造方法，名字不能改变，必须这么写
            constructor(name, age) {
                this.name = name;
                this.age = age;
            }

            // 添加方法；方法必须使用该语法，不能使用ES5的对象完整形式
            property(name){
                console.log(this.name + "的属性：");
            }
        }

        // 实例化对象
        let yuehai = new Person("月海", 16);
        // 调用方法
        yuehai.property();
        // 调用属性
        console.log(`姓名：${yuehai.name}，年龄${yuehai.age}`);
        console.log(yuehai);
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-393--2xKpTE_psLgvxQ.png)

### ③、static 定义静态方法和属性

#### Ⅰ、函数对象

- 实例对象和函数对象是不相通的

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
    <h2>class 类的静态成员-函数对象</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 声明函数对象
        function Person() { }
      
        // 给函数对象添加属性；给函数对象添加属性；称为静态成员
        Person.name = "月海";
        Person.age = 16;
        Person.property = function(name) {
            console.log(`${this.name}的属性：`);
        }
      
        // 调用函数对象的原型
        Person.property("月海")
        console.log(`姓名：${Person.name}，年龄${Person.age}`);

        // 实例化函数对象；实例对象和函数对象是不相通的
        let yuehai = new Person();
        // 调用实例化对象，会返回 undefined
        console.log(yuehai.name);

        // 使用 prototype 方法才可以添加属性和方法；给实例对象添加属性
        Person.prototype.height = 168;
        console.log(yuehai.height);
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-545--fbfvVtBeDPDHIA.png)

#### Ⅱ、class 类

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
    <h2>class 类的静态成员-class类</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 定义类
        class Person{
            // 定义静态属性
            static album = "烟花烬头"
            // 定义静态方法
            static singer(){
                console.log("河图");
            }

            // constructor：构造方法，名字不能改变，必须这么写
            constructor(name, age) {
                // 定义普通属性
                this.name = name;
                this.age = age;
            }

            // 添加方法；方法必须使用该语法，不能使用ES5的对象完整形式
            property(name){
                console.log(this.name + "的属性：");
            }
        }

        // 实例化对象
        let yuehai = new Person("月海", 16);
        // 调用普通方法
        yuehai.property();
        // 调用普通属性
        console.log(`姓名：${yuehai.name}，年龄${yuehai.age}`);
        console.log(yuehai);

        // 使用实例对象无法调用静态属性和方法 undefined
        console.log(yuehai.album);

        // 调用静态属性和方法只能使用类名调用
        console.log(Person.album);
        Person.singer
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-666--cWNRf8YpGuEPfg.png)

### ④、extends 继承父类

#### Ⅰ、函数对象

#### Ⅱ、class 类

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
    <h2>class 类继承</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 定义类
        class Person{
            // constructor：构造方法，名字不能改变，必须这么写
            constructor(name, age) {
                // 定义普通属性
                this.name = name;
                this.age = age;
            }

            // 添加方法；方法必须使用该语法，不能使用ES5的对象完整形式
            property(name){
                console.log(this.name + "的属性：");
            }

            play(){
                console.log("玩");
            }
        }

        // 实例化父类对象
        const yuehai = new Person("月海", 16);
        // 调用方法
        yuehai.property();
        // 调用属性
        console.log(`姓名：${yuehai.name}，年龄${yuehai.age}`);
        console.log(yuehai);


        // 继承
        class yan extends Person {
            // constructor：构造方法，名字不能改变，必须这么写
            constructor(name, age, sex, size) {
                // 调用父类的构造方法
                super(name, age);
                // 定义子类独有的普通属性
                this.sex = sex;
                this.size = size;
            }

            // 重写父类方法
            play(){
                console.log(`玩${this.name}`);
            }

            // 定义子类独有的方法
            playyan(){
                console.log(`再玩${this.name}`);
            }
        }

        // 实例化
        const yan1 = new yan("言",14,0,150);
        // 调用继承的父类属性
        console.log(yan1.name);
        console.log(yan1.age);
        // 调用子类独有的属性
        console.log(yan1.sex);
        console.log(yan1.size);

        // 调用继承的父类的方法
        yan1.property();
        // 调用子类重写的父类的方法
        yan1.play();
        // 调用子类独有的方法
        yan1.playyan();


    })
    
</script>

</html>
```

### ⑤、class 类中的 `getter()、setter()` 方法

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
    <h2>class 类继承</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 定义类
        class Person{
            // 类中可以不写构造方法
            get age(){
                console.log("获取年龄");
                // 输出 _age
                return this._age
            }

            set age(age) {
                console.log("年龄被修改了");
                // 将赋值的 age 的值赋值给 _age
                this._age = age;
            }

        }

        // 实例化父类对象
        const yueha = new Person();
        // 调用 get 属性，会执行其中的语句
        yueha.age;
        // 调用 get 属性，会有返回值
        console.log(yueha.age);

        // 调用 get 属性，会执行其中的语句
        yueha.age = 14;
        // // 调用 get 属性，会有返回值
        console.log(yueha.age);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-759--6whuF4ZQYRE60Q.png)

## 17、数值扩展

### ①、`Number.EPSILON`：JavaScript 最小精度

1. `Number.EPSILON` 是 JavaScript 表示的最小精度
2. `EPSILON` 属性的值接近于 2.2204460492503138808472633361816E-16
3. 一般用法：两个数的差值小于 `Number.EPSILON` ，则认为这两个数是相等的

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
    <h2>class 类继承</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        console.log(0.1 + 0.2);
        console.log(0.1 + 0.2 === 0.3);


        // 创建一个比较函数
        function equal(a, b){
            if(Math.abs(a - b) < Number.EPSILON ){
                return true;
            }else{
                return false;
            }
        }

        console.log(equal(0.1 + 0.2, 0.3));


    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-898--NZWG6Yofng93TA.png)

### ②、二进制和八进制

1. ES6 提供了二进制和八进制数值的新的写法，分别用前缀 0b 和 0o 表示
2. 二进制：0b101010
3. 八进制：0o8546

### ③、Number.isFinite() 与 Number.isNaN()：检查一个数值是否为有限、检查一个值是否为 NaN

1. `Number.isFinite()`：用来检查一个数值是否为有限
2. `Number.isNaN()`：用来检查一个值是否为 NaN；是则为 true，不是则为 false
- NaN 属性是代表非数字值的特殊值，该属性用于指示某个值不是数字

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
    <h2>17、数值扩展3-Number.isFinite() 与 Number.isNaN().html</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // Number.isFinite() 用来检查一个数值是否为有限
        console.log(Number.isFinite(100/10));
        console.log(Number.isFinite(100/0));

        console.log("-----------------------");

        // Number.isNaN() 用来检查一个值是否为 NaN；是则为 true，不是则为 false
        // NaN 属性是代表非数字值的特殊值，该属性用于指示某个值不是数字
        console.log(Number.isNaN(111));

        let aa = Number("aa")
        console.log(aa);
        console.log(Number.isNaN(aa));

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-23-973--eNkZkgiaVi5WjA.png)

### ④、Number.parseInt() 与 Number.parseFloat()：字符串转整数、字符串转小数

类似截取字符串，若字符串在数字前面，则不能转换；数字只能在最前面

1. `Number.parseInt()`：字符串转整数
2. `Number.parseFloat()`：字符串转小数

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
    <h2>17、Number.parseInt() 与 Number.parseFloat()</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // Number.parseInt()：字符串转整数
        console.log(Number.parseInt("月海16"));
        console.log(Number.parseInt("16月海"));
        
        // Number.parseFloat()：字符串转小数
        console.log(Number.parseFloat("言14.5"));
        console.log(Number.parseFloat("14.5言"));

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-093--x5YlC2Lc0iCdbg.png)

### ⑤、Math.trunc()：去除一个数的小数部分

- `Math.trunc()`：去除一个数的小数部分，返回整数部分

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-160--EDyBeZTkUp5O7Q.png)

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
    <h2>17、数值扩展5-Number.isInteger</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // Math.trunc：去除一个数的小数部分，返回整数部分
        console.log(Math.trunc(3.2));
        console.log(Math.trunc(10/7));

    })
    
</script>

</html>
```

### ⑥、Math.sign() 与 Number.isInteger()：判断一个数是正数还是负数还是0、判断一个数值是否为整数

1. Math.sign()：判断一个数是正数、负数、0
   1. 正数：返回 1
   2. 负数：返回 -1
   3. 0   ：返回 0
2. Number.isInteger ()：判断一个数值是否为整数

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
    <h2>17、数值扩展6-Math.sign() 与 Number.isInteger</h2>
    <button id="btn">点击</button>
    
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 判断一个数是正数、负数、0
        // 正数：返回 1
        // 负数：返回 -1
        // 0   ：返回 0
        console.log(Math.sign(5));
        console.log(Math.sign(10/7));

        console.log(Math.sign(0));
        console.log(Math.sign(1 - 1));

        console.log(Math.sign(1 - 10));
        console.log(Math.sign(-6));


        console.log("-----------------------");


        // 判断一个数值是否为整数
        console.log(Number.isInteger(7));
        console.log(Number.isInteger(7.0));
        console.log(Number.isInteger(10/2));

        console.log(Number.isInteger(1.1));
        console.log(Number.isInteger(1.0));
        console.log(Number.isInteger(10/7));

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-325--h4QDEsZtdWvYtA.png)

## 19、模块化

模块化是指将一个大的程序文件，拆分成许多小的文件，然后将小文件组合起来

### ①、模块化的优势

1. 防止命名冲突
2. 代码复用
3. 高维护性

### ②、模块化规范产品

ES6 之前的模块化规范有：

1. CommonJS => NodeJS、Browserify
2. AMD => requireJS
3. CMD => seaJS

### ③、ES6 模块化语法

模块功能主要由两个命令构成：export 和 import。

1. export 命令用于规定模块的对外接口
2. import 命令用于输入其他模块提供的功能

### ④、暴露数据语法汇总

#### Ⅰ、分别暴露

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
    <h2>18、模块化01</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 引入 js 模块中的内容
    import * as m01 from "./18、模块化js/18、模块化01.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        console.log(m01);
        // 调用引入的模块的属性
        console.log(m01.name);
        // 调用引入的模块的方法
        m01.play();

    })
    
</script>

</html>
```
```javascript
// export：模块对外暴露的接口；分别暴露
export let name = '月海';

export function play(){
    console.log(`${name}玩`);
}
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-475--1fo8x8YDu3WPXA.png)

#### Ⅱ、统一暴露

```javascript
let name = '月海';

function play(){
    console.log(`${name}玩`);
}

// export：模块对外暴露的接口；统一暴露
export{
    name,
    play
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
</head>
<body>
    <h2>18、模块化02-统一暴露</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 引入 js 模块中的内容
    import * as m02 from "./18、模块化js/18、模块化02-统一暴露.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        console.log(m02);
        // 调用引入的模块的属性
        console.log(m02.name);
        // 调用引入的模块的方法
        m02.play();

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-564--mqDY8RaNyS14RA.png)

#### Ⅲ、默认暴露

```javascript
// 默认暴露
export default{
    name:'默认暴露',
    change(){
        console.log('默认暴露');
    }
}

let name = '月海';

function play(){
    console.log(`${name}玩`);
}

// export：模块对外暴露的接口；统一暴露
export{
    name,
    play
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
</head>
<body>
    <h2>18、模块化03-默认暴露</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 引入 js 模块中的内容
    import * as m03 from "./18、模块化js/18、模块化03-默认暴露.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        console.log(m03);
        // 调用引入的模块的默认暴露属性
        console.log(m03.default.name);
        // 调用引入的模块的默认暴露方法
        m03.default.change();

        // 调用引入的模块的统一暴露属性
        console.log(m03.name);
        // 调用引入的模块的统一暴露方法
        m03.play();

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-665--j3M_emhHuKmSFA.png)

### ⑤、引入数据语法汇总

```javascript
let name = '月海';

function play(){
    console.log(`${name}玩`);
}

// export：模块对外暴露的接口；统一暴露
export{
    name,
    play
}
```

#### Ⅰ、通用引入方式

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
    <h2>18、模块化04-引入方式</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 1、引入 js 模块中的内容；通用引入
    import * as m02 from "./18、模块化js/18、模块化02-统一暴露.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 调用引入的模块的统一暴露属性
        console.log(m02.name);
        // 调用引入的模块的统一暴露方法
        m02.play();

    })
    
</script>

</html>
```

#### Ⅱ、结构赋值引入方式

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
    <h2>18、模块化04-引入方式</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 2、结构赋值引入方式
    import {name,play} from "./18、模块化js/18、模块化02-统一暴露.js"
    // as：起别名，防止重名
    import {name as name2,play as play2} from "./18、模块化js/18、模块化02-统一暴露.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 调用引入的模块的统一暴露属性
        console.log(name);
        // 调用引入的模块的统一暴露方法
        play();

        // 调用引入的模块的统一暴露属性
        console.log(name2);
        // 调用引入的模块的统一暴露方法
        play2();

    })
    
</script>

</html>
```

#### Ⅲ、简便引入形式（只能针对默认暴露）

```javascript
// 默认暴露
export default{
    name:'默认暴露',
    change(){
        console.log('默认暴露');
    }
}

let name = '月海';

function play(){
    console.log(`${name}玩`);
}

// export：模块对外暴露的接口；统一暴露
export{
    name,
    play
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
</head>
<body>
    <h2>18、模块化04-引入方式</h2>
    <button id="btn">点击</button>
    
</body>

<script type="module">

    // 3、简便引入形式（只能针对默认暴露）
    import m03 from "./18、模块化js/18、模块化03-默认暴露.js"

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){

        // 调用引入的模块的统一暴露属性
        console.log(m03.name);
        // 调用引入的模块的统一暴露方法
        m03.change();

    })
    
</script>

</html>
```

### ⑥、入口文件

```javascript
// 入口文件

// 模块引入
import * as m01 from "./18、模块化01.js"
import * as m02 from "./18、模块化02-统一暴露.js"
import * as m03 from "./18、模块化03-默认暴露.js"

console.log(m01.name);
console.log(m02.name);
console.log(m03.name);
```
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
    <h2>18、模块化05-入口文件</h2>
    <button id="btn">点击</button>
    
</body>

<script src="./18、模块化js/18、模块化05-入口文件.js" type="module"></script>

</html>
```

### ⑦、babel 对 ES6代码进行转化

> [https://www.bilibili.com/video/BV1uK411H7on/?p=46&spm_id_from=pageDriver&vd_source=b55e15966ca689b32671d4aa387cab01](https://www.bilibili.com/video/BV1uK411H7on/?p=46&spm_id_from=pageDriver&vd_source=b55e15966ca689b32671d4aa387cab01)

### ⑧、ES6 模块化引入 NPM 包

> [https://www.bilibili.com/video/BV1uK411H7on/?p=47&spm_id_from=pageDriver&vd_source=b55e15966ca689b32671d4aa387cab01](https://www.bilibili.com/video/BV1uK411H7on/?p=47&spm_id_from=pageDriver&vd_source=b55e15966ca689b32671d4aa387cab01)

# 三、ECMASript 7 新特性

## 1、.Array.prototype.includes

- Includes 方法用来检测数组中是否包含某个元素，返回布尔类型值

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
    <h2>01、Array.prototype.includes</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // Includes 方法用来检测数组中是否包含某个元素，返回布尔类型值
        let arr = [0,1,2,3,45,6];

        console.log(arr.includes(0));
        console.log(arr.includes(1));
        console.log(arr.includes(0,1));
        console.log(arr.includes('0'));

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-758--O3vbJ7v5JqvdBw.png)

## 2、指数操作符

- 在 ES7 中引入指数运算符 `**`，用来实现幂运算，功能与 `Math.pow` 结果相同

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
    <h2>02、指数操作符</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 指数操作符
        console.log(2 ** 10);
        console.log(Math.pow(2, 10));

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-24-971--MGk9H-oQstIBug.png)

# 四、ECMASript 8 新特性

## 1、`async` 和 `await`

async 和 await 两种语法结合可以让异步代码像同步代码一样

### ①、`async` 函数

1. `async` 函数的返回值为 promise 对象
2. promise 对象的结果由 `async` 函数执行的返回值决定
3. promise 成功的语法糖

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
    <h2>01、async 和 await</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义一个 async 函数
        async function fn(){
            // 只要 async 函数的返回值不是 promise 对象，那么他就会返回一个成功的 promise 对象
            return '月海'
        }
        // async 函数的返回值为 promise 对象
        // promise 对象的结果由 async 函数执行的返回值决定
        console.log(fn());


        async function fn2(){
            // 返回一个失败的 promise 对象
            throw new Error('出错')
        }
        console.log(fn2());


        async function fn3(){
            // 返回一个成功的 promise 对象
            return new Promise((resolve, reject) => {
                resolve('成功')
            })
        }
        console.log(fn3());

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-070--52WTYbnoTVNnog.png)

### ②、`await` 表达式

1. `await` 必须写在 `async` 函数中
2. `await` 右侧的表达式一般为 promise 对象
3. `await` 返回的是 promise 成功的值
4. `await` 的 promise 失败了, 就会抛出异常, 需要通过 try...catch 捕获处理

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
    <h2>01、async 和 await</h2>
    <button id="btn">点击</button>
</body>

<script>
    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 创建 Promise 对象
        const p = new Promise((resolve, reject) => {
            // resolve('成功');
            reject('失败');
        })

        async function fn(){
            
            // 捕获异常
            try {
                // await 必须写在 async 函数中；返回的是 promise 成功的值
                let result = await p;
                // 成功的返回值
                console.log(result);
            }catch (e) {
                // 失败的返回值
                console.log(e);
            }
        }

        fn()

    })
    
</script>

</html>
```

### ③、`async` 和 `await` 结合去读文件内容

```javascript
// 引入 fs 模块
const fs = require("fs");

// 读取文件
function readYuehai(){
    return new Promise((resolve, reject) => {
        fs.readFile("./文件/月海.txt", (err, data) => {
            // 如果失败
            if (err) {
                reject(err);
            }

            // 如果成功
            resolve(data);
        })
    })
}

// 声明一个 async 函数
async function main(){
    // 调用方法
    let yuehai = await readYuehai();

    console.log(yuehai);
}

// 调用方法
main();
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-173--LvXUDRFMzu2a0g.png)

### ④、`async` 和 `await` 结合发送AJAX请求

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
    <h2>01、async 和 await04 结合发送AJAX请求</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 定义 AJAX 方法
    function sendAjax(url){
        return new Promise((resolve, reject) => {
            // 1、创建对象
            const ajax = new XMLHttpRequest();
            
            // 2、初始化
            ajax.open('GET', url);

            // 3、发送请求
            ajax.send();

            // 4、事件绑定
            ajax.onreadystatechange = () => {
                if (!ajax){
                    // 成功
                    resolve(ajax.response)
                }else {
                    // 失败
                    reject(ajax.status)
                }
            }
        })
    }

    // async 和 await 测试
    async function main(){
        // 发送 AJAX 请求
        await sendAjax('https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=月海');
    }

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 调用 main 方法
        main();
        
    })
    
</script>

</html>
```

## 2、对象方法扩展

1. `Object.keys`：获取对象所有的键

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-330--HI2A3eaknE1V_Q.png)

2. `Object.values`：获取对象所有的值

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-437--z8L4UXzuK__hWA.png)

3. `Object.entries`：返回对象自身可遍历属性 `[key,value]` 的数组

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-543--jurLHnfJczqPdg.png)

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-635--AVQzVGI0Aw-JUw.png)

4. `Object.getOwnPropertyDescriptors`：返回对象属性的描述对象

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-730--LfNHPqheQyGmaw.png)

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
    <h2>02、对象方法扩展01-Object.values</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义对象
        const person = {
            name:'人',
            yan:['言',14],
            yuehai:['月海',16]
        }

        // 1、Object.keys：获取对象所有的键
        console.log(Object.keys(person));

        // 2、Object.values：获取对象所有的值
        console.log(Object.values(person));

        // 3、Object.entries：返回对象自身可遍历属性 [key,value] 的数组
        console.log(Object.entries(person));

        // 3.2、将 Object.entries 返回的值赋值给 map 集合
        let map = new Map(Object.entries(person));
        console.log(map);

        // 4、Object.getOwnPropertyDescriptors：返回对象属性的描述对象
        console.log(Object.getOwnPropertyDescriptors(person));

    })
    
</script>

</html>
```
# 五、ECMASript 9 新特性

Rest 参数与 spread 扩展运算符在 ES6 中已经引入，不过 ES6 中只针对于数组
在 ES9 中为对象提供了像数组一样的 rest 参数和扩展运算符  

## 1、rest 参数

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
    <h2>01、rest 参数</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义函数；使用解构赋值，rest 参数
        function user({ name, age, ...args }) {
            console.log(name);
            console.log(age);
            console.log(ages);
        }

        // 调用函数
        user({
            name : '月海',
            age : 16,
            sex : 0,
            play : '羽'
        })

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-896--mYseDczHiZkTWA.png)

## 2、spread 扩展运算符

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
    <h2>02、spread 扩展运算符</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义 3 个对象
        const yan = { yanName: '言' }
        const yu =  { yuName: '羽' }
        const yuehai = { yuehaiName: '月海' }

        // 定义另外的对象，使用 spread 扩展运算符赋值；合并对象
        const user = {...yan, ...yu, ...yuehai}
        console.log(user);


    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-25-973--ONdNYjVf0vHqiQ.png)

## 3、正则表达式扩展

### ①、命名捕获组

 ES9 允许命名捕获组使用符号：`?<name>`,这样获取捕获结果可读性更强 

1. 没有分组时的情况

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
    <h2>03、正则表达式扩展01-命名捕获组</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = '<a href = "https://www.bilibili.com/">批哩批哩</a>';

        // 提取 url 和 标签文本；(.*)：需要提取的文本；*：通配符
        const reg = /<a href = "(.*)">(.*)<\/a>/;

        // 执行
        const result = reg.exec(str);

        // 执行结果是一个数组
        console.log(result);
        // 第一个元素是原始字符串
        console.log(result[0]);
        // 第二个元素是提取的第一个文本
        console.log(result[1]);
        // 第三个元素是提取的第二个文本
        console.log(result[2]);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-091--XqgX9wVuCHD6Bg.png)

2. 有分组时的情况

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
    <h2>03、正则表达式扩展01-命名捕获组</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = '<a href = "https://www.bilibili.com/">批哩批哩</a>';

        // 提取 url 和 标签文本；(.*)：需要提取的文本；*：通配符
        const reg = /<a href = "(?<url>.*)">(?<text>.*)<\/a>/;

        // 执行
        const result = reg.exec(str);

        // 执行结果依然是一个数组
        console.log(result);
        // 提取指定的属性 url
        console.log(result.groups.url);
        // 提取指定的属性 test
        console.log(result.groups.text);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-188--bBbRCnUYpsPyrQ.png)

### ②、断言

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
    <h2>03、正则表达式扩展01-命名捕获组</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = 'JS5211314你知道么555啦啦啦';

        // 正向断言；\d：匹配一个数字字符，等价于 [0-9]；判断数字后面是不是 啦
        const justReg = /\d+(?=啦)/;
        const result01 = justReg.exec(str);
        console.log(result01);

        // 反向断言；\d：匹配一个数字字符，等价于 [0-9]；判断数字前面是不是 么
        const backReg = /(?<=么)\d+/;
        const result02 = backReg.exec(str);
        console.log(result02);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-258--eS9cy5tup98GXw.png)

### ③、dotAll 模式

1. 正则表达式中点 `.` 匹配除回车外的任何单字符；`\s` 匹配回车

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
    <h2>03、正则表达式扩展03-dotAll 模式</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = `
        <ul>
            <li>
                <a>肖生克的救赎</a>
                <p>上映日期: 1994-09-10</p>
            </li>
            <li>
                <a>阿甘正传</a>
                <p>上映日期: 1994-07-06</p>
            </li>
        </ul>`;

        // 声明正则
        const reg = /<li>\s+<a>(?<name>.*?)<\/a>\s+<p>(?<time>.*?)<\/p>/;
        const result = reg.exec(str);
        console.log(result);
        console.log(result.groups.name);
        console.log(result.groups.time);
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-379--2NuCWnk7bR-BxQ.png)


2. dotAll 模式里的标记 `s`  改变了这种行为  ，使得 `.` 不止匹配任何单字符，还匹配回车，允许了行终止符出现

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
    <h2>03、正则表达式扩展03-dotAll 模式</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = `
        <ul>
            <li>
                <a>肖生克的救赎</a>
                <p>上映日期: 1994-09-10</p>
            </li>
            <li>
                <a>阿甘正传</a>
                <p>上映日期: 1994-07-06</p>
            </li>
        </ul>`;

        // 声明正则
        const reg = /<li>.*?<a>(?<name>.*?)<\/a>.*?<p>(?<time>.*?)<\/p>/s;
        const result = reg.exec(str);
        console.log(result);
        console.log(result.groups.name);
        console.log(result.groups.time);
        
    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-486--tRMyx9Y4COqY8w.png)

# 六、ECMASript 10 新特性

## 1、对象方法扩展

- `Object.fromEntries`：数组或集合变对象

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
    <h2>01、对象方法扩展</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // Object.fromEntries：数组或集合变对象
        // 定义一个二维数组
        const resultArr = Object.fromEntries([
            ['yan','言'],
            ['yuehai','月海']
        ]);
        console.log(resultArr);

        // 定义一个 map 集合
        const map = new Map();
        map.set("yuehai","月海");
        map.set("yu","羽");
        const resultMap = Object.fromEntries(map);
        console.log(resultMap);


        // es8 中的 Object.entries：对象变数组
        const arr = Object.entries({
            yuehai : '月海',
            yan : '言'
        });
        console.log(arr);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-614--TOO7LmvKouTjMw.png)

## 2、数组方法扩展

1. `arr.flat(`)：可将数组降维；二维变一维，三维变二维
2. `arr.map()`：该数组中的每个元素都调用一个提供的回调函数，返回一个新数组
3. `arr.flatMap()`：`arr.flat()` 和 `arr.map()` 的结合；即数组中的每个元素都调用一个提供的回调函数的同时，还可以将数组降维

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
    <h2>03、字符串方法扩展</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // arr.flat()：可将数组降维；二维变一维，三维变二维
        // 也可传递参数，代表数组深度；一维深度为0，二维深度为1
        // 定义一个二维数组
        let arr2 = [1,2,3,[5,6]];
        // 将二维数组降为一维
        console.log(arr2.flat());

        // 定义一个三维数组
        let arr3 = [1,2,3,[5,6,[8,9]]];
        // 将三维数组降为二维
        console.log(arr3.flat());
        // 将三维数组降为一维
        console.log(arr3.flat(2));


        // arr.map()：该数组中的每个元素都调用一个提供的回调函数，返回一个新数组
        let arrMap = [1,2,3,4];
        // 使数组 arr 中的每个元素都 * 10
        let resultMap = arrMap.map( i => i * 10 );
        console.log(resultMap);


        // arr.flatMap()：arr.flat() 和 arr.map() 的结合；即数组中的每个元素都调用一个提供的回调函数的同时，还可以将数组降维
        let arrFaltMap = [4,5,6,7]
        // 使数组 arr 中的每个元素都 * 10；并使返回值都为数组
        let resultFaltMap1 = arrFaltMap.map( i => [i * 10] );
        console.log(resultFaltMap1);

        // 使数组 arr 中的每个元素都 * 10；并使返回值都为数组，然后将数组降维
        let resultFaltMap2 = arrFaltMap.flatMap( i => [i * 10] );
        console.log(resultFaltMap2);

    })
    
</script>

</html>
```

## 3、字符串方法扩展

1. `str.trim()`：去除左右两边的空格
2. `str.trimStart()`：去除前边的空格
3. `str.trimEnd()`：去除后边的空格
4. `str.trimLeft()`：去除左前边的空格
5. `str.trimRight()`：去除右边的空格

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
    <h2>03、字符串方法扩展</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义一个字符串
        let str = '    月 海    ';

        console.log(str);
        // str.trim()：去除左右两边的空格
        console.log(str.trim());
        // str.trimStart()：去除前边的空格
        console.log(str.trimStart());
        // str.trimEnd()：去除后边的空格
        console.log(str.trimEnd());
        // str.trimLeft()：去除左前边的空格
        console.log(str.trimLeft());
        // str.trimRight()：去除右边的空格
        console.log(str.trimRight());

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-781--2ZG2HoG3Q6b4yQ.png)

## 4、Symbol 扩展

- `Symbol.description` 获取 Symbol 的描述字符串（值）

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
    <h2>04、Symbol方法扩展</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义一个 Symbol
        let s = Symbol("月海");

        // 打印 Symbol
        console.log(s);
        // 获取 Symbol 的描述字符串（值）
        console.log(s.description);
        

    })
    
</script>

</html>
```

# 七、ECMASript 11 新特性

---

## 1、类的私有属性

1. 私有属性定义：变量前加 `#`
2. 私有属性只能在类里面调用，实例化后在外部不可调用

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
    <h2>01、类的私有属性</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义一个 class 
        class Person{
            // 定义公有属性
            name;
            // 定义私有属性：#
            #age;
            #sex;

            // 使用构造方法初始化；构造方法参数中的私有属性不能加 #
            constructor(name, age, sex) {
                this.name = name;
                this.#age = age;
                this.#sex = sex;
            }

            // 创建方法
            intro(){
                // 方法内调用公有属性
                console.log(this.name);
                // 方法内调用私有属性
                console.log(this.#age);
                console.log(this.#sex);
            }
        }


        // 实例化 class 类
        const yuehai = new Person("月海", 16, 0);
        console.log(yuehai);
        // 调用公有属性
        console.log(yuehai.name);
        // 调用私有属性
        console.log(yuehai.age);
        console.log(yuehai.sex);
        // 调用方法
        yuehai.intro();

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-879--VwjSDgoQapp64Q.png)

## 2、Promise 方法扩展

1. `Promise.all()`：有一个 Promise 对象错误，就会返回错误
2. `Promise.allSettled()`：返回的值始终是成功的，且包含每个 Promise 的结果和状态

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
    <h2>02、Promise.allSettled</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明两个 promise 对象
        const p1 = new Promise( (resolve, reject) => {
            resolve("成功 1");
            // reject("失败 1")
        } )
        const p2 = new Promise( (resolve, reject) => {
            // resolve("成功 2");
            reject("失败 2")
        } )

        // 调用 Promise.all() 方法；
        // Promise.all() 方法是要有一个 Promise 对象错误，就会返回错误
        const result01 = Promise.all([p1, p2]);
        console.log(result01);

        // 调用 Promise.allSettled() 方法；
        // Promise.allSettled() 方法返回的值始终是成功的，且包含每个 Promise 的结果和状态
        const result02 = Promise.allSettled([p1, p2]);
        console.log(result02);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-26-979--AtgN9MAEEEWu0A.png)

## 3、字符串方法扩展 matchAll

- `str.match()`：得到正则表达式批量匹配的结果，返回一个可迭代对象，可通过 for-of 遍历

1. 通过 for-of 遍历

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
    <h2>03、字符串方法扩展 matchAll</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = `
        <ul>
            <li>
                <a>肖生克的救赎</a>
                <p>上映日期: 1994-09-10</p>
            </li>
            <li>
                <a>阿甘正传</a>
                <p>上映日期: 1994-07-06</p>
            </li>
        </ul>`;

        // 声明正则
        const reg = /<a>(?<name>.*?)<\/a>.*?<p>(?<time>.*?)<\/p>/sg;

        // str.match()：得到正则表达式批量匹配的结果，返回一个可迭代对象，可通过 for-of 遍历
        const result = str.matchAll(reg);
        console.log(result);

        // 遍历结果
        for (const v of result) {
            console.log(v);
            console.log(v.groups.name);
            console.log(v.groups.time);
        }

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-110--ILCQwnGJEcsASQ.png)

2. 使用扩展运算符对其进行展开

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
    <h2>03、字符串方法扩展 matchAll02</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 声明一个字符串
        let str = `
        <ul>
            <li>
                <a>肖生克的救赎</a>
                <p>上映日期: 1994-09-10</p>
            </li>
            <li>
                <a>阿甘正传</a>
                <p>上映日期: 1994-07-06</p>
            </li>
        </ul>`;

        // 声明正则
        const reg = /<a>(?<name>.*?)<\/a>.*?<p>(?<time>.*?)<\/p>/sg;

        // str.match()：得到正则表达式批量匹配的结果，返回一个可迭代对象，可通过 for-of 遍历
        const result = str.matchAll(reg);
        console.log(result);

        // 使用扩展运算符对其进行展开
        let arr = [...result];
        console.log(arr);

        console.log(arr[0]);
        console.log(arr[1]);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-204--Q5IoW5shhW7MiA.png)

## 4、可选链操作符

- `?`：相当于判断前面的参数存不存在，这样即使传递的参数不对也不会报错

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
    <h2>04、可选链操作符</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义方法
        function fn(config) {
            // 原先的方式获取参数，链式调用；若是参数传递的不对则会报错
            console.log(config.db.host);

            // 可选链操作符：?
            // ? 相当于判断前面的参数存不存在，这样即使传递的参数不对也不会报错
            console.log(config?.db?.host);
        }

        // 定义参数
        const config = {
            db: {
                host: '192.168.1.100',
                username: 'root'
            },
            cache: {
                host: '192.168.1.200',
                username: 'admin'
            }
        }

        // 调用方法
        fn(config)

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-350--RkdC3Co1gwoghg.png)

## 5、动态 import 导入

- 按需加载（懒加载）

```javascript
// 定义并暴露一个函数
export function hello(){
    console.log('hello');
}
```
```javascript
// 之前的方式，静态引入
// import * as hello from './05、动态 import 导入.js';

// 获取元素对象
const btn = document.querySelector("#btn")
// 绑定单击事件
btn.addEventListener("click",function(){
    // 调用静态引入 js 中的方法
    // hello.hello();

    // 动态引入；返回的是一个 Promise 对象
    import("./05、动态 import 导入.js").then(module => {
        // 调用动态引入 js 中的方法
        module.hello();
    })

})
```
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
    <h2>05、动态 import 导入</h2>
    <button id="btn">点击</button>
</body>

<script src="./05、动态 import 导入入口文件.js" type="module"></script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-424--Z_hKCYzNFr3LcQ.png)

## 6、大整数 `BigInt`

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
    <h2>06、大整数 BigInt</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        // 定义一个大整数
        let numN = 456n;
        // 类型是 bigint
        console.log(numN, typeof(numN));

        // 大整数的运算
        console.log("大整数的运算：" + numN + BigInt(1));

        // 将普通整形转换为大整数
        let num = 456;
        console.log("将普通整形转换为大整数：" + BigInt(num));
        // 普通整形与大整数的运算：
        console.log(BigInt(num) + numN);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-558--tIV6QR3CUBusNg.png)

## 7、绝对全局对象 `globalThis`

- 无论执行环境是什么，始终指向全局环境
- 浏览器指向 Window，nodejs 指向 nodejs 等

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
    <h2>06、大整数 BigInt</h2>
    <button id="btn">点击</button>
</body>

<script>

    // 获取元素对象
    const btn = document.querySelector("#btn")
    // 绑定单击事件
    btn.addEventListener("click",function(){
        
        console.log(globalThis);

    })
    
</script>

</html>
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/%E4%B8%89%E4%BB%B6%E5%A5%97/attachments/2023-07-25-13--09-27-702--nvhH8YJ1ZIbYsg.png)

