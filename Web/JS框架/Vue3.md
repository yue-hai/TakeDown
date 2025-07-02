> github上的tags地址：[https://github.com/vuejs/vue-next/releases/tag/v3.0.0](https://github.com/vuejs/vue-next/releases/tag/v3.0.0)
> 
> [B 站尚硅谷 vue3 视频](https://www.bilibili.com/video/BV1Zy4y1K7SH)
> 
> [vue3快速上手.md](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/vue3快速上手.md)

# 一、Vue3 简介

## 1、Vue3 简介

- 2020年9月18日，Vue.js发布3.0版本，代号：One Piece（海贼王）
- 耗时2年多、2600+次提交、30+个RFC、600+次PR、99位贡献者
- github上的tags地址：[https://github.com/vuejs/vue-next/releases/tag/v3.0.0](https://github.com/vuejs/vue-next/releases/tag/v3.0.0)

## 2、Vue3 带来了什么

1. 性能的提升
   1. 打包大小减少41%
   2. 初次渲染快55%, 更新渲染快133%
   3. 内存减少54%......
2. 源码的升级
   1. 使用Proxy代替defineProperty实现响应式
   2. 重写虚拟DOM的实现和Tree-Shaking......
3. 拥抱TypeScript
4. 新的特性
5. Composition API（组合API）
   1. setup配置
   2. ref与reactive
   3. watch与watchEffect
   4. provide与inject
   5. ......
6. 新的内置组件
   1. Fragment
   2. Teleport
   3. Suspense
7. 其他改变
   1. 新的生命周期钩子
   2. data 选项应始终被声明为一个函数
   3. 移除keyCode支持作为 v-on 的修饰符
   4. ......

# 二、创建 Vue3.0 工程

## 1、使用 vue-cli 创建

### ①、创建工程

官方文档：[https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create](https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create)

```bash
## 查看@vue/cli版本，确保@vue/cli版本在4.5.0以上
vue --version
## 安装或者升级你的@vue/cli
npm install -g @vue/cli
## 创建
vue create vue_test
## 启动
cd vue_test
npm run serve
```

### ②、分析工程结构

1. `main.js` 简化

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// createApp(App).mount('#app')
// 创建应用实例对象：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
const app = createApp(App)
// 挂载
app.mount('#app')
```

2. 组件中可以没有根标签

```javascript
<template>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
    name: 'App',
    components: {
        HelloWorld
    }
}
</script>
```

3. 工程结构

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230725125500.png)

## 2、使用 vite 创建

1. 官方文档：[https://v3.cn.vuejs.org/guide/installation.html#vite](https://v3.cn.vuejs.org/guide/installation.html#vite)
2. vite官网：[https://vitejs.cn](https://vitejs.cn)
3. 什么是vite？—— 新一代前端构建工具。
4. 优势如下： 
   1. 开发环境中，无需打包操作，可快速的冷启动。
   2. 轻量快速的热重载（HMR）。
   3. 真正的按需编译，不再等待整个应用编译完成。
5. 传统构建 与 vite构建对比图

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230725124852.png)

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230725124900.png)

```bash
## 创建工程
npm create vite@latest vue3-vite --template vue

## 输入 y 确定，并选择 Vue
Need to install the following packages:
  create-vite@latest
Ok to proceed? (y) y
? Select a framework: » - Use arrow-keys. Return to submit.
    Vanilla                                                
>   Vue                                                    
    React                                                  
    Preact                                                 
    Lit                                                    
    Svelte                                                 
    Others  

## 选择 JavaScript
√ Select a framework: » Vue                              
? Select a variant: » - Use arrow-keys. Return to submit.
>   JavaScript                                           
    TypeScript                                           
    Customize with create-vue ↗                          
    Nuxt ↗ 

## 进入工程目录
cd vue3-vite

## 安装依赖
npm install

## 运行
npm run dev
```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-149--QzNcMeyS2cO3Ig.png)

# 三、常用组合式 Composition API

## 1、拉开序幕的 setup

1. 理解：Vue3.0 中一个新的配置项，值为一个函数。
2. setup 是所有 Composition API（组合API）“ 表演的舞台 ”。
3. 组件中所用到的：数据、方法等等，均要配置在 setup 中。
4. setup 函数的两种返回值：
   1. 若返回一个对象，则对象中的属性、方法，在模板中均可以直接使用。（重点关注！）
   2. 若返回一个渲染函数：则可以自定义渲染内容。（了解）
5. 注意点：
   1. 尽量不要与 Vue2.x 配置混用
      1. Vue2.x 配置（data、methos、computed...）中可以访问到 setup 中的属性、方法。
      2. 但在 setup 中不能访问到 Vue2.x 配置（data、methos、computed...）。
      3. 如果有重名，setup 优先。
   2. setup 不能是一个 async 函数，因为返回值不再是 return 的对象，而是 promise，模板看不到 return 对象中的属性。（后期也可以返回一个Promise 实例，但需要 Suspense 和异步组件的配合）

---

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// createApp(App).mount('#app')
// 创建应用实例对象：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
const app = createApp(App)
// 挂载
app.mount('#app')
```

```vue
<template>
    <HelloWorld />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
    name: 'App',
    components: { HelloWorld }
}
</script>
```

```vue
<template>
    <h1>姓名：{{name}}</h1>
    <button @click="hello">介绍</button>
</template>

<script>
// 引入渲染函数 h
// import { h } from 'vue'

export default {
    name: 'HelloWorld',
    setup(){
        // 数据
        let name = "月海";
        let age = 16;

        // 方法
        function hello(){
            alert(`姓名：${name}，年龄：${age}`)
        }

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { name, hello }

        // 返回一个渲染函数：则可以自定义渲染内容；需要引入渲染函数 h
        // return ()=> h( 'name', '1111111111111111111')
    }
}
</script>
```

## 2、ref 函数

1. 作用：定义一个响应式的数据
2. 语法：`const xxx = ref(initValue)`
   1. 创建一个包含响应式数据的引用对象（reference对象，简称ref对象）。
   2. JS中操作数据：` xxx.value`
   3. 模板中读取数据：不需要.value，直接：`<div>{{xxx}}</div>`
3. 备注：
   1. 接收的数据可以是：基本类型、也可以是对象类型。
   2. 基本类型的数据：响应式依然是靠 `Object.defineProperty()` 的 `get` 与 `set` 完成的。
   3. 对象类型的数据：内部 “ 求助 ” 了 Vue3.0 中的一个新函数：`reactive` 函数。

```vue
<template>
    <h1>姓名：{{name}}</h1>
    <h4>工作：{{job.type}}</h4>
    <h4>工资：{{job.salary}}</h4>
    <button @click="hello">介绍</button>
    <button @click="update">修改</button>
</template>

<script>
    // 引入 vue 函数
    import { ref } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 数据
            let name = ref("月海");
            let age = ref(16);
            let job = ref({
                type: "java",
                salary: 6000
            })

            // 方法
            function hello(){
                alert(`姓名：${name.value}，年龄：${age.value}`)
            }
            function update(){
                name.value = "言";
                age.value = 14;
                job.value.type = 'vue';
                job.value.salary = 5000;
            }

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { name, job, hello, update }
        }
    }
</script>

```

## 3、reactive 函数

1. 作用：定义一个对象类型的响应式数据（基本类型不要用它，要用 `ref` 函数）
2. 语法：`const 代理对象 = reactive(源对象)` 接收一个对象（或数组），返回一个代理对象（Proxy 的实例对象，简称 proxy 对象）
3. reactive 定义的响应式数据是“深层次的”。
4. 内部基于 ES6 的 Proxy 实现，通过代理对象操作源对象内部数据进行操作。

```vue
<template>
    <h1>姓名：{{person.name}}</h1>
    <h4>工作：{{person.job.type}}</h4>
    <h4>工资：{{person.job.salary}}</h4>
    <ul>
        <li v-for="(hobby, index) in person.hobbys" :key="hobby">
            {{hobby}}
            <button @click="update2(index)">* 10</button>
        </li>
    </ul>
    <button @click="hello">介绍</button>
    <button @click="update">修改</button>
</template>

<script>
// 引入 vue 函数
import { reactive } from 'vue'

export default {
    name: 'HelloWorld',
    setup(){
        const data = reactive({
            person: {
                name: "月海",
                age: 16,
                job: {
                    type: "java",
                    salary: 6000
                },
                hobbys: [ 1,2,3,4,5 ]
            }
        })

        // 方法
        function hello(){
            alert(`姓名：${data.person.name}，年龄：${data.person.age}`)
        }
        function update(){
            data.person.name = "言";
            data.person.age = 14;
            // 使用 reactive 不用再 .value
            data.person.job.type = 'vue';
            data.person.job.salary = 5000;
            data.person.hobbys[0] = 22;
        }
        function update2(index){
            data.person.hobbys[index] = data.person.hobbys[index] * 10;
        }

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { ...data, hello, update, update2 }
    }
}
</script>

```

## 4、Vue3.0 中的响应式原理

### ①、vue2.x 的响应式

1. 实现原理：
   1. 对象类型：通过 `Object.defineProperty()` 对属性的读取、修改进行拦截（数据劫持）。
   2. 数组类型：通过重写更新数组的一系列方法来实现拦截。（对数组的变更方法进行了包裹）。

```vue
Object.defineProperty(data, 'count', {
    get () {}, 
    set () {}
})
```

2. 存在问题：
   1. 新增属性、删除属性，界面不会更新。
   2. 直接通过下标修改数组，界面不会自动更新

### ②、Vue3.0 的响应式

> [https://www.bilibili.com/video/BV1Zy4y1K7SH/?p=146](https://www.bilibili.com/video/BV1Zy4y1K7SH/?p=146)

- 实现原理：
1. 通过 `Proxy`（代理）：拦截对象中任意属性的变化, 包括：属性值的读写、属性的添加、属性的删除等。
2. 通过 `Reflect`（反射）：对源对象的属性进行操作。
3. MDN 文档中描述的 `Proxy` 与 `Reflect`：
   - Proxy：[https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
   - Reflect：[https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

```vue
new Proxy(data, {
    /** 
    *	拦截读取属性值
    *	target：原数据，就是 data
    *	prop：读取的数据
    */
    get (target, prop) {
        return Reflect.get(target, prop)
    },
    /** 
    *	拦截设置属性值或添加新属性
    *	target：原数据，就是 data
    *	prop：读取的数据
    *	value：修改或添加的新值
    */
    set (target, prop, value) {
        return Reflect.set(target, prop, value)
    },
    // 拦截删除属性
    deleteProperty (target, prop) {
        return Reflect.deleteProperty(target, prop)
    }
})

proxy.name = 'tom'   
```

## 5、reactive 对比 ref

1. 从定义数据角度对比：
   1. `ref` 用来定义：基本类型数据。
   2. `reactive` 用来定义：对象（或数组）类型数据。
   3. 备注：`ref` 也可以用来定义对象（或数组）类型数据，它内部会自动通过 `reactive` 转为代理对象。
2. 从原理角度对比：
   1. `ref` 通过 `Object.defineProperty()` 的 `get` 与 `set` 来实现响应式（数据劫持）。
   2. `reactive` 通过使用 `Proxy` 来实现响应式（数据劫持），并通过 `Reflect` 操作源对象内部的数据。
3. 从使用角度对比：
   1. `ref` 定义的数据：操作数据需要 `.value`，读取数据时模板中直接读取`不需要` `.value`。
   2. `reactive` 定义的数据：操作数据与读取数据：均不需要 `.value`。

## 6、setup 的两个注意点

1. `setup` 执行的时机
   - 在 `beforeCreate` 之前执行一次，`this` 是 `undefined`。
2. `setup` 的参数
   1. `props`：值为对象，包含：组件外部传递过来，且组件内部声明接收了的属性。
   2. `context`：上下文对象
      1. `attrs`：值为对象，包含：组件外部传递过来，但没有在 props 配置中声明的属性，相当于 `this.$attrs`。

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-617--mV2cK_8I0AedBQ.png)

      2. `emit`：分发自定义事件的函数，相当于 `this.$emit`。

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-631--2f2t6MlpcZtoUg.png)

      3. `slots`：收到的插槽内容，相当于 `this.$slots`。

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-642--_5dIAMrOsRKu3A.png)

---

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 创建应用实例对象并挂载：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).mount('#app')
```
```vue
<template>
    <!-- @HelloWorldHello="AppHello"：给子组件绑定 HelloWorldHello 事件，被触发时调用父组件的 AppHello 函数 -->
    <HelloWorld @HelloWorldHello="AppHello" attrsTest1="attrs1" attrsTest2="attrs2">
        <!-- 插槽 -->
        <template v-slot:slotTest>
            <p>yuehai</p>
        </template>

    </HelloWorld>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
    name: 'App',
    components: { HelloWorld },
    setup(){
        function AppHello(value){
            console.log(`AppHello 事件被触发，收到的参数为：${value}`)
        }

        return { AppHello }
    }
}
</script>

```

```vue
<template>
    <h1>{{person.name}}</h1>
    <button @click="test">触发 HelloWorldHello 事件</button>
    <slot name="slotTest"></slot>
</template>

<script>
// 引入 vue 函数
import { reactive } from 'vue'

export default {
    name: 'HelloWorld',
    // props：声明接收父组件传过来的参数
    props: [ 'attrsTest1' ],
    // emits：声明接收父组件绑定的事件，不过触发还是需要通过 context.emit，所以这个属性配不配置没有影响
    emits: [ 'HelloWorldHello' ],
    // setup 执行的时机，在 beforeCreate 之前执行一次，this 是 undefined
    setup(props, context){
        const data = reactive({
            person: {
                name: "月海"
            }
        })

        // props：值为对象，包含：组件外部传递过来，且组件内部声明接收了的属性
        console.log(props.attrsTest1)
        // 1、attrs：值为对象，包含：组件外部传递过来，但没有在 props 配置中声明的属性，相当于 this.$attrs
        console.log(context.attrs.attrsTest1)
        console.log(context.attrs.attrsTest2)
        console.log("----------------")

        // 2、emit：分发自定义事件的函数，相当于 this.$emit
        function test(){
            // 触发绑定给此组件的 HelloWorldHello 事件，传递参数 666
            context.emit("HelloWorldHello", 666)
        }

        // 3、slots：收到的插槽内容，相当于 this.$slots
        console.log(context.slots)

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { ...data, test }
    }
}
</script>
```

## 7、计算属性与监视属性

### ①、计算属性 `computed` 函数

1. 与 Vue2.x 中 `computed` 配置功能一致
2. 写法

```vue
<template>
    姓：<input type="text" v-model="person.firstName"><br>
    名：<input type="text" v-model="person.lastName"><br>
    <h1>全名：{{person.fullName}}</h1>
    <h1>全名：<input type="text" v-model="person.fullName2"></h1>
</template>

<script>
// 引入 vue 函数
import { reactive, computed } from 'vue'

export default {
    name: 'HelloWorld',
    setup(){
        const data = reactive({
            person: {
                firstName: '月海',
                lastName: 'yuehai'
            }
        })

        // 使用计算属性：简写形式，没有考虑计算属性被修改的情况
        data.person.fullName = computed(()=>{
            return `${data.person.firstName}-${data.person.lastName}`
        })

        // 使用计算属性：完整形式，考虑读写
        data.person.fullName2 = computed({
            get(){
                return `${data.person.firstName}-${data.person.lastName}`
            },
            set(value){
                const arr = value.split('-');
                data.person.firstName = arr[0];
                data.person.lastName = arr[1];
            }
        })

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { ...data }
    }
}
</script>

```

### ②、监视属性`watch` 函数

- 与 Vue2.x 中 `watch` 配置功能一致
- 监视使用 `ref` 定义的基本属性时不用 `.value`
- 两个小“坑”：
   - 监视 `reactive` 定义的响应式数据时：`oldValue` 无法正确获取、强制开启了深度监视（deep 配置失效）。
   - 监视 `reactive` 定义的响应式数据中某个属性时：deep 配置有效。

```vue
<template>
    <h2>当前求和为：{{sum}}</h2>
    <button @click="sum++">点击+1</button><hr>

    <h2>当前求和 2 为：{{sum2}}</h2>
    <h2>当前信息为：{{msg}}</h2>
    <button @click="sum2++">点击+1</button>
    <button @click="msg = msg + '！'">点击显示信息</button><hr>

    <h2>姓名：{{person.name}}</h2>
    <h2>年龄：{{person.age}}</h2>
    <h2>java：{{person.job.java}}</h2>
    <button @click="person.name = person.name + '~'">修改姓名</button>
    <button @click="person.age ++">修改年龄</button>
    <button @click="person.job.java = person.job.java + 500">修改薪资</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { ref, reactive, watch} from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let sum = ref(0);
            let sum2 = ref(0);
            let msg = ref('你好啊');
            const person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 情况一：监视 ref 所定义的一个响应式数据
            // 参数 1：监视的属性是谁
            // 参数 2：监视的回调
            // 参数 3：配置项：
            //      配置项：立即执行 immediate
            //      配置项：深度监视 deep
            watch(sum, (newValue, oldValue)=>{
                console.log('sum 发生了改变', newValue, oldValue)
            }, {immediate: true, deep: true})

            // 情况二：监视 ref 所定义的多个响应式数据，将所要监视的属性放入数组传递，此时 newValue 和 oldValue 的值也是数组
            watch([sum2, msg], (newValue, oldValue)=>{
                console.log('sum 或 msg 发生了改变', newValue, oldValue)
            })

            // 情况三：监视 reactive 定义的响应式数据，无法正确获得 oldValue，且强制开启了深度监视（deep：true）不可关闭
            // watch(person, (newValue, oldValue)=>{
            //     console.log('person 发生了改变', newValue, oldValue)
            // })

            // 情况四：监视 reactive 定义的响应式数据中的某个属性，需传入一个函数，监视其返回值，此方法的 oldValue 可以正确获得
            watch(()=>person.age, (newValue, oldValue)=>{
                console.log('person 发生了改变', newValue, oldValue)
            })

            // 情况五：监视 reactive 定义的响应式数据中的某些属性，将所要监视的属性放入数组传递，此时 newValue 和 oldValue 的值也是数组
            watch([()=>person.name, ()=>person.age], (newValue, oldValue)=>{
                console.log('person 发生了改变', newValue, oldValue)
            })

            // 特殊情况：监视 reactive 定义的响应式数据中对象，若其中还有嵌套的对象，则要开启深度监视，但依然无法正确获得 oldValue
            watch(()=>person.job, (newValue, oldValue)=>{
                console.log('person.job 发生了改变', newValue, oldValue)
            }, {deep: true})

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { sum, sum2, msg, person }
        }
    }
</script>

```

### ③、监视属性`watchEffect` 函数

1. `watch` 的套路是：既要指明监视的属性，也要指明监视的回调。
2. `watchEffect` 的套路是：不用指明监视哪个属性，监视的回调中用到哪个属性，那就监视哪个属性。
3. `watchEffect` 有点像 `computed`：
   1. 但 `computed` 注重的计算出来的值（回调函数的返回值），所以必须要写返回值。
   2. 而 `watchEffect` 更注重的是过程（回调函数的函数体），所以不用写返回值。

```vue
<template>
    <h2>当前求和为：{{sum}}</h2>
    <button @click="sum++">点击+1</button><hr>

    <h2>姓名：{{person.name}}</h2>
    <h2>年龄：{{person.age}}</h2>
    <h2>java：{{person.job.java}}</h2>
    <button @click="person.name = person.name + '~'">修改姓名</button>
    <button @click="person.age ++">修改年龄</button>
    <button @click="person.job.java = person.job.java + 500">修改薪资</button><hr>
</template>

<script>
import {reactive, ref, watchEffect} from 'vue'

export default {
    name: "watchEffectTest",
    setup(){
        // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
        let sum = ref(0);
        const person = reactive({
            name: '月海',
            age: 18,
            job: {
                java: 1000
            }
        })

        watchEffect(()=>{
            let java = person.job.java
            console.log(`当前求和为${sum.value}，当前薪资为${java}`)
        })

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { sum, person }
    }
}
</script>

<style scoped>

</style>
```

## 8、生命周期

### ①、vue2.x 的生命周期

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230726143217.png)

### ②、vue3.0 的生命周期

1. vue3.0 中可以继续使用 Vue2.x 中的生命周期钩子，但有有两个被更名：
   1. `beforeDestroy` 改名为 `beforeUnmount`
   2. `destroyed` 改名为 `unmounted`

```vue
<template>
    <button @click="isShow = !isShow">切换隐藏/显示</button>
    <HelloWorld v-if="isShow" />
</template>

<script>
    // 引入 vue 函数
    import { ref } from 'vue'

    // 引入组件
    import HelloWorld from './components/HelloWorld.vue'

export default {
    name: 'App',
    components: { HelloWorld },
    setup(){
        let isShow = ref(true)

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { isShow }
    }
}
</script>

```

```vue
<template>
    <h2>当前求和为：{{sum}}</h2>
    <button @click="sum++">点击+1</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { ref } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let sum = ref(0);

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { sum }
        },
        // 通过配置项 的形式使用生命周期钩子
        beforeCreate() {
            console.log('----初始化之前：beforeCreate----')
        },
        created() {
            console.log('----初始化完成：created----')
        },
        beforeMount() {
            console.log('----挂载之前：beforeMount----')
        },
        mounted() {
            console.log('----挂载完成：mounted----')
        },
        beforeUpdate() {
            console.log('----更新之前：beforeUpdate----')
        },
        updated() {
            console.log('----更新完成：updated----')
        },
        beforeUnmount() {
            console.log('----卸载之前：beforeUnmount----')
        },
        unmounted() {
            console.log('----卸载完成：unmounted----')
        }
    }
</script>

```

2. Vue3.0 也提供了 `Composition API` 形式的生命周期钩子，与 Vue2.x 中钩子对应关系如下：
   1. 初始化之前：`beforeCreate`===>`setup()`
   2. 初始化完成：`created`=======>`setup()`
   3. 挂载之前：`beforeMount`====>`onBeforeMount`
   4. 挂载完成：`mounted`=======>`onMounted`
   5. 更新之前：`beforeUpdate`===>`onBeforeUpdate`
   6. 更新完成：`updated`=======>`onUpdated`
   7. 卸载之前：`beforeUnmount`==>`onBeforeUnmount`
   8. 卸载完成：`unmounted`=====>`onUnmounted`

```vue
<template>
    <h2>当前求和为：{{sum}}</h2>
    <button @click="sum++">点击+1</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { ref, onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted } from 'vue'

    export default {
        name: 'HelloWorld2',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let sum = ref(0);

            console.log('----初始化之前：beforeCreate----')
            console.log('----初始化完成：created----')
            // 通过组合式 api 的形式使用生命周期钩子
            onBeforeMount(()=>{
                console.log('----挂载之前：beforeMount----')
            })
            onMounted(()=>{
                console.log('----挂载完成：mounted----')
            })
            onBeforeUpdate(()=>{
                console.log('----更新之前：beforeUpdate----')
            })
            onUpdated(()=>{
                console.log('----更新完成：updated----')
            })
            onBeforeUnmount(()=>{
                console.log('----卸载之前：beforeUnmount----')
            })
            onUnmounted(()=>{
                console.log('----卸载完成：unmounted----')
            })

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { sum }
        },

    }
</script>

```

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230726143534.png)

## 9、自定义 `hook` 函数

1. 什么是 `hook`：本质是一个函数，把 `setup` 函数中使用的 Composition API 进行了封装。 
2. 类似于 vue2.x 中的 `mixin`。 
3. 自定义 `hook` 的优势：复用代码，让 `setup` 中的逻辑更清楚易懂。 

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 创建应用实例对象并挂载：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).mount('#app')
```

- 在 src 目录下创建 hooks 目录，在其中创建 usePoint.js 文件

```javascript
import {onBeforeUnmount, onMounted, reactive} from 'vue'

// 显示鼠标点击的坐标，将逻辑写在一个函数里
function savePoint(){
    // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
    const point = reactive({
        x: 0,
        y: 0
    })

    // 给坐标赋值
    function savePoint(event){
        point.x = event.pageX;
        point.y = event.pageY;
        console.log(event.pageX, event.pageY)
    }

    // 挂载完成，绑定点击事件
    onMounted(()=> {
        window.addEventListener('click', savePoint)
    })

    // 卸载之前，删除绑定事件
    onBeforeUnmount(()=>{
        window.removeEventListener('click', savePoint)
    })

    // 最后需要返回数据
    return point;
}

// 暴露
export default { savePoint }
```
```vue
<template>
    <h2>当前鼠标点击的坐标为：<br>X：{{point.x}}，Y：{{point.y}}</h2>
</template>

<script>
    // 引入 vue 函数
    import {  } from 'vue'
    // 引入 hook 函数
    import UsePoint from '@/hooks/usePoint'

    export default {
        name: 'HelloWorld',
        setup(){
            // 调用 UsePoint 中的 savePoint() 函数，得到其返回值
            let point = UsePoint.savePoint()

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { point }
        }
    }
</script>

```

```vue
<template>
    <button @click="isShow = !isShow">切换隐藏/显示</button>
    <HelloWorld v-if="isShow" />
</template>

<script>
    // 引入组件
    import HelloWorld from './components/HelloWorld.vue'
    import {ref} from 'vue'

    export default {
        name: 'App',
        components: { HelloWorld },
        setup(){
            let isShow = ref(true)

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { isShow }
        }
    }
</script>

```

## 10、`toRef`

1. 作用：创建一个 `ref` 对象，其 `value` 值指向另一个对象中的某个属性。
2. 语法：`const name = toRef(person,'name')`
3. 应用：要将响应式对象中的某个属性单独提供给外部使用时。

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{person.age}}</h2>
    <h2>java：{{javaToRef}}</h2>
    <button @click="name = name + '~'">修改姓名</button>
    <button @click="person.age ++">修改年龄</button>
    <button @click="javaToRef = javaToRef + 500">修改薪资</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { reactive, toRef } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            const person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return {
                // 返回 person，模板中可通过 person.xxx 使用
                person,

                // 使用 toRef 返回 person 中的 name 属性，模板中可通过 name 使用
                name: toRef(person, 'name'),
                // 使用 toRef 返回 person.job 中的 java 属性，模板中可通过 javaToRef 使用
                javaToRef: toRef(person.job, 'java'),
            }
        }
    }
</script>

```

4. 扩展：`toRefs` 与 `toRef` 功能一致，但可以批量创建多个 `ref` 对象，语法：`toRefs(person)`

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <h2>java：{{job.java}}</h2>
    <button @click="name = name + '~'">修改姓名</button>
    <button @click="age ++">修改年龄</button>
    <button @click="job.java = job.java + 500">修改薪资</button><hr>
</template>

<script>
// 引入 vue 函数
import { reactive, toRefs } from 'vue'

export default {
    name: 'ToRefsTest',
    setup(){
        // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
        const person = reactive({
            name: '月海',
            age: 18,
            job: {
                java: 1000
            }
        })

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return {
            // 使用 toRefs
            ...toRefs(person)
        }
    }
}
</script>

```

# 四、其它组合式 Composition API

## 1、`shallowReactive` 与 `shallowRef`

1. `shallowReactive`：只处理对象最外层属性的响应式（浅响应式）。
2. `shallowRef`：只处理基本数据类型的响应式，不进行对象的响应式处理。
3. 什么时候使用?
   1. 如果有一个对象数据，结构比较深，但变化时只是外层属性变化：`shallowReactive`。
   2. 如果有一个对象数据，后续功能不会修改该对象中的属性，而是生新的对象来替换：`shallowRef`。

## 2、`readonly` 与 `shallowReadonly`

1. `readonly`：让一个响应式数据变为只读的（深只读），所有数据都不可更改
2. `shallowReadonly`：让一个响应式数据变为只读的（浅只读），只有第一层不可修改，嵌套的对象可以修改
3. 应用场景：不希望数据被修改时。

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <h2>java：{{job.java}}</h2>
    <button @click="name = name + '~'">修改姓名</button>
    <button @click="age ++">修改年龄</button>
    <button @click="job.java = job.java + 500">修改薪资</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { reactive, toRefs, readonly, shallowReadonly } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 1. readonly：让一个响应式数据变为只读的（深只读），所有数据都不可更改
            // person = readonly(person);

            // 2. shallowReadonly：让一个响应式数据变为只读的（浅只读），只有第一层不可修改，嵌套的对象可以修改
            person = shallowReadonly(person);

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { ...toRefs(person) }
        }
    }
</script>

```

## 3、`toRaw` 与 `markRaw`

1. `toRaw`：
   1. 作用：将一个由 `reactive` 生成的响应式对象转为普通对象。
   2. 使用场景：用于读取响应式对象对应的普通对象，对这个普通对象的所有操作，不会引起页面更新。
2. `markRaw`：
   1. 作用：标记一个对象，使其永远不会再成为响应式对象。
   2. 应用场景:
      1. 有些值不应被设置为响应式的，例如复杂的第三方类库等。
      2. 当渲染具有不可变数据源的大列表时，跳过响应式转换可以提高性能。

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <h2>java：{{job.java}}</h2>
    <button @click="name = name + '~'">修改姓名</button>
    <button @click="age ++">修改年龄</button>
    <button @click="job.java = job.java + 500">修改薪资</button><hr>

    <button @click="showRawPerson">输入最原始的 person 对象</button><hr>

    <h2>性别：{{person.sex}}</h2>
    <button @click="addSex">给对象添加性别属性</button>
    <button @click="person.sex = 1">修改性别</button>
</template>

<script>
    // 引入 vue 函数
    import { reactive, toRefs, toRaw, markRaw } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 将一个由 reactive 生成的响应式对象转为普通对象
            function showRawPerson(){
                const p = toRaw(person);
                console.log(p)
            }

            // 添加属性，添加的自动就为响应式数据
            function addSex(){
                let sex = {sex: 0}
                person.sex = markRaw(sex);
            }

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { ...toRefs(person), showRawPerson, addSex, person }
        }
    }
</script>

```

## 4、`customRef`

1. 作用：创建一个自定义的 `ref`，并对其依赖项跟踪和更新触发进行显式控制。
2. 本质就是一个函数
3. 实现防抖效果：

```vue
<template>
    <input type="text" v-model="keyword">
    <h3>{{ keyword }}</h3>
</template>

<script>
    import { ref, customRef } from 'vue'

    export default {
        name: 'HelloWorld',
        setup() {
            // 使用 Vue 准备好的内置 ref
            // let keyword = ref('hello')

            /**
             * 自定义一个 myRef
             * 参数 1：传进来的值，显示的数据
             * 参数 2：传进来的值，设置的抖动参数
             */
            function myRef(value, delay) {
                // 设置一个值，来判断定时器是否开启
                let timer

                // 通过customRef去实现自定义
                return customRef((track, trigger) => {
                    return {
                        get() {
                            // 告诉 Vue 这个 value 值是需要被“追踪”的
                            track()
                            // 返回传进来的值
                            return value
                        },
                        
                        // 参数：修改的值
                        set(newValue) {
                            // 关闭定时器 timer
                            clearTimeout(timer)
                            // 开启定时器，并将其赋值给 timer
                            timer = setTimeout(() => {
                                // 将值变为修改后的值
                                value = newValue
                                // 告诉 Vue 去更新界面
                                trigger()
                            }, delay)
                        }
                    }
                })
            }

            // 使用程序员自定义的 ref
            let keyword = myRef('hello', 1000)

            return { keyword }
        }
    }
</script>
```

## 5、`provide` 与 `inject`

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020230726143721.png)

1. 作用：实现祖与后代组件间通信
2. 套路：父组件有一个 `provide` 选项来提供数据，后代组件有一个 `inject` 选项来开始使用这些数据
3. 具体写法：
   1. 祖组件中：

```vue
setup(){
    ......
    let car = reactive({name:'奔驰',price:'40万'})
    provide('car',car)
    ......
}
```

   2. 后代组件中：

```vue
setup(props,context){
    ......
    const car = inject('car')
    return {car}
    ......
}
```

---

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 创建应用实例对象并挂载：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).mount('#app')

```

```vue
<template>
    <div class="app">
        <h2>app 组件，姓名：{{name}}</h2>
        <Child />
    </div>
</template>

<script>
    // 引入 vue 函数
    import { reactive, toRefs, provide } from 'vue'

    // 引入组件
    import Child from '@/components/Child.vue'

    export default {
        name: 'App',
        components: { Child },
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            const person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 给自己的后代组件传递数据
            provide('person', person)

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { ...toRefs(person) }
        }
    }
</script>

<style>
    .app{
        background-color: skyblue;
        padding: 10px;
    }
    .child{
        background-color: coral;
        padding: 10px;
    }
    .son{
        background-color: lightpink;
        padding: 10px;
    }
</style>

```

```vue
<template>
    <div class="child">
        <h2>Child 组件，年龄：{{age}}</h2>
        <Son/>
    </div>
</template>

<script>
    // 引入 vue 函数
    import { toRefs, inject } from 'vue'
    import Son from '@/components/Son.vue'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Child",
        components: { Son },
        setup(){
            // 获取祖组件传递的数据
            const person = inject('person')

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { ...toRefs(person) }
        }
    }
</script>
```

```vue
<template>
    <div class="son">
        <h2>Son 组件，薪资：{{job.java}}</h2>
    </div>
</template>

<script>
// 引入 vue 函数
import { toRefs, inject } from 'vue'

export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Son",
    setup(){
        // 获取祖组件传递的数据
        const person = inject('person')

        // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
        return { ...toRefs(person) }
    }
}
</script>
```

## 6、响应式数据的判断

1. `isRef`：检查一个值是否为一个 `ref` 对象
2. `isReactive`：检查一个对象是否是由 `reactive` 创建的响应式代理
3. `isReadonly`：检查一个对象是否是由 `readonly` 创建的只读代理
4. `isProxy`：检查一个对象是否是由 `reactive` 或者 `readonly` 方法创建的代理

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <h2>java：{{job.java}}</h2>
    <button @click="name = name + '~'">修改姓名</button>
    <button @click="age ++">修改年龄</button>
    <button @click="job.java = job.java + 500">修改薪资</button><hr>
</template>

<script>
    // 引入 vue 函数
    import { reactive, toRefs, isRef, isReactive, isReadonly, isProxy } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            // 基本类型要使用 ref，若是使用 reactive，必须为对象或数组
            let person = reactive({
                name: '月海',
                age: 18,
                job: {
                    java: 1000
                }
            })

            // 1. isRef：检查一个值是否为一个 ref 对象
            console.log(isRef(person))

            // 2. isReactive：检查一个对象是否是由 reactive 创建的响应式代理
            console.log(isReactive(person))

            // 3. isReadonly：检查一个对象是否是由 readonly 创建的只读代理
            console.log(isReadonly(person))

            // 4. isProxy：检查一个对象是否是由 reactive 或者 readonly 方法创建的代理
            console.log(isProxy(person))

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { ...toRefs(person) }
        }
    }
</script>

```

# 五、组合式 Composition API 的优势

## 1、Options API 存在的问题

使用传统 OptionsAPI 中，新增或者修改一个需求，就需要分别在 `data`、`methods`、`computed` 里修改 。

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/f84e4e2c02424d9a99862ade0a2e4114~tplv-k3u1fbpfcp-watermark.gif)

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/e5ac7e20d1784887a826f6360768a368~tplv-k3u1fbpfcp-watermark.gif)

## 2、Composition API 的优势

我们可以更加优雅的组织我们的代码，函数。让相关功能的代码更加有序的组织在一起。

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/bc0be8211fc54b6c941c036791ba4efe~tplv-k3u1fbpfcp-watermark.gif)

![](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/6cc55165c0e34069a75fe36f8712eb80~tplv-k3u1fbpfcp-watermark.gif)

# 六、新的组件

## 1、Fragment

1. 在 Vue2 中：组件必须有一个根标签
2. 在 Vue3 中：组件可以没有根标签，内部会将多个标签包含在一个 Fragment 虚拟元素中
3. 好处：减少标签层级，减小内存占用

## 2、Teleport

1. 什么是 `Teleport`：`Teleport` 是一种能够将我们的组件 `html` 结构移动到指定位置的技术。 
2. 可以使元素的定位更加方便

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 创建应用实例对象并挂载：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).mount('#app')

```
```vue
<template>
    <div class="app">
        <h2>app 组件</h2>
        <Child />
    </div>
</template>

<script>
    // 引入组件
    import Child from '@/components/Child.vue'

    export default {
        name: 'App',
        components: { Child }
    }
</script>

<style>
    .app{
        background-color: skyblue;
        padding: 10px;
    }
    .child{
        background-color: coral;
        padding: 10px;
    }
    .son{
        background-color: lightpink;
        padding: 10px;
    }
</style>

```

```vue
<template>
    <div class="child">
        <h2>Child 组件</h2>
        <Son/>
    </div>
</template>

<script>
    // 引入组件
    import Son from '@/components/Son.vue'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Child",
        components: { Son }
    }
</script>
```

```vue
<template>
    <div class="son">
        <h2>Son 组件</h2>
        <DiaLog/>
    </div>
</template>

<script>
    // 引入组件
    import DiaLog from '@/components/DiaLog.vue'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Son",
        components: { DiaLog }
    }
</script>
```

```vue
<template>
    <div>
        <button @click="isShow = true">点我弹窗</button>
        <!-- 将组件 html 结构移动到指定位置，body 下 -->
        <Teleport to="body">
            <!-- 遮罩层 -->
            <div class="mask"  v-if="isShow">
                <!-- 弹窗 -->
                <div class="dialog">
                    <h3>我是一个弹窗</h3>
                    <h4>月海</h4>
                    <h4>月海</h4>
                    <h4>月海</h4>
                    <button @click="isShow =false">关闭弹窗</button>
                </div>
            </div>
        </Teleport>
    </div>
</template>

<script>
    // 引入 vue 函数
    import { ref } from 'vue'

    export default {
        name: "DiaLog",
        setup(){
            let isShow = ref(false)

            return { isShow }
        }
    }
</script>

<style scoped>
    .mask{
        position: absolute;
        top: 0; bottom: 0; left: 0; right: 0;
        background-color: rgba(0, 0, 0, 0.5);
    }
    .dialog{
        background-color: olivedrab;
        padding: 10px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 300px;
        height: 300px;
    }
</style>
```

## 3、Suspense

1. 等待异步组件时渲染一些额外内容，让应用有更好的用户体验
2. 使用步骤：
   1. 异步引入组件

```vue
import {defineAsyncComponent} from 'vue'
const Child = defineAsyncComponent(()=>import('./components/Child.vue'))
```

   2. 使用 `Suspense` 包裹组件，并配置好 `default` 与 `fallback`

```vue
<template>
    <div class="app">
        <h3>我是App组件</h3>
        <Suspense>
            <template v-slot:default>
                <Child/>
            </template>
            <template v-slot:fallback>
                <h3>加载中.....</h3>
            </template>
        </Suspense>
    </div>
</template>
```

---

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 创建应用实例对象并挂载：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).mount('#app')

```

```vue
<template>
    <div class="app">
        <h2>app 组件</h2>
        <!-- Suspense：等待异步组件时渲染一些额外内容 -->
        <Suspense>
            <!-- v-slot:default：需要加载的组件 -->
            <template v-slot:default>
                <Child />
            </template>
            <!-- v-slot:fallback：等待组件加载时显示的内容 -->
            <template v-slot:fallback>
                加载中。。。请稍后
            </template>
        </Suspense>
    </div>
</template>

<script>
    // 引入 vue 函数，defineAsyncComponent：异步引入
    import { defineAsyncComponent } from 'vue'
    const Child = defineAsyncComponent(()=>import('@/components/Child.vue'))
    // 引入组件，静态引入
    // import Child from '@/components/Child.vue'

    export default {
        name: 'App',
        components: { Child }
    }
</script>

<style>
    .app{
        background-color: skyblue;
        padding: 10px;
    }
    .child{
        background-color: coral;
        padding: 10px;
    }
</style>

```

```vue
<template>
    <div class="child">
        <h2>Child 组件</h2>
    </div>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Child"
    }
</script>
```

# 七、其他改变

## 1、全局 API 的转移

1. Vue 2.x 有许多全局 API 和配置。
- 例如：注册全局组件、注册全局指令等。

```vue
// 注册全局组件
Vue.component('MyButton', {
  data: () => ({
    count: 0
  }),
  template: '<button @click="count++">Clicked {{ count }} times.</button>'
})

// 注册全局指令
Vue.directive('focus', {
  inserted: el => el.focus()
}
```

2. Vue3.0 中对这些 API 做出了调整

- 将全局的 API，即：`Vue.xxx` 调整到应用实例（`app`）上

| 2.x 全局 API（Vue） | 3.x 实例 API (app) |
| --- | --- |
| Vue.config.xxxx | app.config.xxxx |
| Vue.config.productionTip | **移除** |
| Vue.component | app.component |
| Vue.directive | app.directive |
| Vue.mixin | app.mixin |
| Vue.use | app.use |
| Vue.prototype | app.config.globalProperties |

## 2、其他改变

1. `data` 选项应始终被声明为一个函数。
2. 过度类名的更改：
   1. Vue2.x 写法

```vue
.v-enter,
.v-leave-to {
  opacity: 0;
}
.v-leave,
.v-enter-to {
  opacity: 1;
}
```

   2. Vue3x 写法

```vue
.v-enter,
.v-leave-to {
  opacity: 0;
}
.v-leave,
.v-enter-to {
  opacity: 1;
}
```

3. 移除 `keyCode` 作为 `v-on` 的修饰符，同时也不再支持 `config.keyCodes`
4. 移除 `v-on.native` 修饰符
   1. 父组件中绑定事件

```vue
<my-component
  v-on:close="handleComponentEvent"
  v-on:click="handleNativeClickEvent"
/>
```

   2. 子组件中声明自定义事件

```vue
<script>
  export default {
    emits: ['close']
  }
</script>
```

5. 移除过滤器（`filter`）

> 过滤器虽然这看起来很方便，但它需要一个自定义语法，打破大括号内表达式是 “只是 JavaScript” 的假设，这不仅有学习成本，而且有实现成本！建议用方法调用或计算属性去替换过滤器。

6. ......

# 八、追加

## 1、使用 svg

> 阿里巴巴矢量图标库：[https://www.iconfont.cn/](https://www.iconfont.cn/)

1. 进入网站，选择矢量图
2. 点击下载，可下载 SVG 文件或者 SVG 代码

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-657--91ZQUe9R8oEEzg.png)

### ①、直接使用

1. 复制 SVG 代码
2. 粘贴到 vue 组件中
3. 将 `<style></style>` 标签中的样式移动到 vue 的 `<style></style>` 标签中
4. 删除 `<defs></defs>` 标签，即可使用

```vue
<template>
    <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" id="b52015b4-2459-46df-970a-a6cd264bdde9">
        <title>党建1024px尺寸</title>
        <rect height="1024" width="1024" class="bd557e99-0b60-410e-9190-ab39419af894"></rect>
        <path d="M892.19,468.81a6.4,6.4,0,0,1-2.87-12.48c1.71-.39,30.78-6.8,57.52,3.93,10-19.51,15.95-41.22,13.34-68.57C937.69,155.37,715.46,279.07,512.3,101.94c-102.19-89.1-203.12-67.57-268.64-3.67,12.66,18.83,31.68,36.7,42.36,45.3a6.4,6.4,0,0,1-8,10A270.16,270.16,0,0,1,242.43,118q-4.32-5.28-7.87-10.34c-70.65,77.13-93.35,205-17.69,283.08,21.76,22.47,31.31,44.24,33.46,65.51,25.26-.61,49.85,4.24,64.92,21a6.4,6.4,0,1,1-9.52,8.56c-12.19-13.54-33-17.5-55-16.89C247.4,586.07,45.29,689.44,470,816.65c213.73,64,320.93,33.34,364.64-46,43.41-78.83,18.26-98.79,32.05-169.25,11.26-57.6,49.61-90.25,73.73-129.75C917.6,463.19,892.55,468.73,892.19,468.81Z"
              class="a54ce527-3476-4590-b6a3-daf0baba896f"></path>
        <path d="M445.95,222.22h36.11a0,0,0,0,1,0,0v55.21a0,0,0,0,1,0,0H445.95A24.41,24.41,0,0,1,421.53,253v-6.38a24.41,24.41,0,0,1,24.41-24.41Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M482.06,279.56H445.22a25.85,25.85,0,0,1-25.82-25.82v-7.83a25.85,25.85,0,0,1,25.82-25.82h36.84a2.13,2.13,0,0,1,2.13,2.13v55.21A2.13,2.13,0,0,1,482.06,279.56Zm-36.84-55.21a21.58,21.58,0,0,0-21.55,21.56v7.83a21.58,21.58,0,0,0,21.55,21.55h34.71V224.35Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M437.16,246.55s17.11-3.73,22.44,7.16" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M459.6,255.85a2.12,2.12,0,0,1-1.91-1.2c-4.55-9.28-19.92-6.05-20.07-6a2.13,2.13,0,1,1-.91-4.16c.76-.17,18.81-3.95,24.81,8.3a2.14,2.14,0,0,1-1,2.86A2.09,2.09,0,0,1,459.6,255.85Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M332.29,593.16S311,678.51,317.59,720.67s51,22.29,51,22.29L395.9,613.49l-67.83-19.67"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M346.64,749.79a33,33,0,0,1-15.85-3.66c-8.26-4.49-13.42-13-15.31-25.13-5.84-37.56,9.77-107.47,13.83-124.6l-1.83-.54a2.13,2.13,0,1,1,1.19-4.09l1.69.49a2.13,2.13,0,0,1,4.05,1.17l62.09,18a2.13,2.13,0,0,1,1.49,2.49L370.64,743.41a2.13,2.13,0,0,1-1.22,1.5A62.14,62.14,0,0,1,346.64,749.79Zm-13.22-152.2c-4,17.19-19.35,86.6-13.73,122.75,1.68,10.8,6.1,18.21,13.12,22,12.38,6.75,29.62.73,33.89-1L393.41,615Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M439.67,436s-56.4,7.71-93.12,81.48c-13.84,27.81-23.65,58.87-32.77,77.8a22.12,22.12,0,0,0,11.62,30.09l52.89,21.52a22.15,22.15,0,0,0,28.63-11.63l34.64-79.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M644.74,404.62a245.08,245.08,0,0,0-58.61-5.74H555.21c-43.81-.85-87.52,18-126.43,42.89a41.54,41.54,0,0,0-18.87,29.16c-6,41.91-18.12,158.8-12.63,391,0,0,258.89,12.8,361.29-25.6L719.21,587.27,750,448.09c-23.87-17.07-72.12-36-105.3-43.47"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M493.66,866.07c-55,0-95.47-1.93-96.49-2a2.14,2.14,0,0,1-2-2.08c-5.53-234.23,7-351.73,12.66-391.38A43.73,43.73,0,0,1,427.63,440c46.08-29.44,89.08-44,127.63-43.22h30.85a249.59,249.59,0,0,1,59.1,5.78c31.37,7,80.84,25.78,106.07,43.83a2.11,2.11,0,0,1,.84,2.19L721.38,587.33,760.68,836a2.13,2.13,0,0,1-1.36,2.33C697.66,861.48,578.45,866.07,493.66,866.07Zm-94.3-6.15C423.46,861,659,870.3,756.19,835L717.1,587.6a2.1,2.1,0,0,1,0-.79L747.65,449c-25.13-17.49-72.88-35.5-103.37-42.32a245.11,245.11,0,0,0-58-5.69h-31c-38-.76-79.94,13.58-125.28,42.56A39.45,39.45,0,0,0,412,471.23C406.41,510.66,394,627.35,399.36,859.92Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M850.47,591.22l-74.11,66.25a16.69,16.69,0,0,1-24.53-2.53l-45-60.84c-22.81-30.83-33.63-69.25-28.57-107.26,3.4-25.54,13.95-47.5,39.51-52,64-11.41,117.41,99.55,136.45,136.28A16.7,16.7,0,0,1,850.47,591.22Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <polygon
                points="785.54 635.83 841.01 576.09 823.94 537.69 785.54 537.69 759.94 567.56 759.94 593.16 785.54 635.83"
                class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></polygon>
        <path d="M438.57,174.74s14.21,37.9,9.48,47.38c0,0,4.73-4.74,14.21,0V189Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M533.27,359.24s3.15,27.63-7.78,44.71c-5,7.8-1,18.22,7.75,21.32,18.55,6.58,48,11,81.29-6.7a10,10,0,0,0,3.23-15c-7-8.95-15.26-26.54-12.13-58.23Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M566.33,433.17a101.24,101.24,0,0,1-33.8-5.89,17,17,0,0,1-10.46-10.56,16,16,0,0,1,1.62-13.92c10.39-16.23,7.5-43.05,7.46-43.32a2.15,2.15,0,0,1,1.72-2.34l72.36-13.93a2.1,2.1,0,0,1,1.84.52,2.16,2.16,0,0,1,.69,1.78c-3,30.64,4.68,47.75,11.68,56.7a12.19,12.19,0,0,1-3.91,18.25C597.71,429.89,581,433.17,566.33,433.17ZM535.57,361c.51,6.76,1.34,29.1-8.29,44.13a11.78,11.78,0,0,0-1.17,10.23,12.78,12.78,0,0,0,7.84,7.93c18.35,6.51,47.06,10.64,79.59-6.58a7.91,7.91,0,0,0,2.54-11.84c-7.26-9.28-15.25-26.63-12.83-56.91Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path transform="translate(1301.48 499.65) rotate(180)"
              d="M642.37,222.22H681a0,0,0,0,1,0,0v55.21a0,0,0,0,1,0,0H646a25.55,25.55,0,0,1-25.55-25.55v-7.77a21.89,21.89,0,0,1,21.89-21.89Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M657.31,279.56H620.48a2.13,2.13,0,0,1-2.14-2.13V222.22a2.13,2.13,0,0,1,2.14-2.13h36.83a25.85,25.85,0,0,1,25.83,25.82v7.83A25.85,25.85,0,0,1,657.31,279.56Zm-34.7-4.27h34.7a21.58,21.58,0,0,0,21.56-21.55v-7.83a21.58,21.58,0,0,0-21.56-21.56h-34.7Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M525.86,130.65h44.46a72.62,72.62,0,0,1,72.62,72.62v70.87A94.85,94.85,0,0,1,548.09,369h0a94.85,94.85,0,0,1-94.85-94.85V203.27A72.62,72.62,0,0,1,525.86,130.65Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M548.09,371.12a97.08,97.08,0,0,1-97-97V130.65a2.13,2.13,0,0,1,2.13-2.13h189.7a2.13,2.13,0,0,1,2.13,2.13V274.14A97.09,97.09,0,0,1,548.09,371.12ZM455.37,132.79V274.14a92.72,92.72,0,1,0,185.44,0V132.79Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M676.45,102.77c.11-.85.21-1.71.25-2.59.72-16.45-12.91-30.41-30.45-31.19a33.66,33.66,0,0,0-12.36,1.77c-9.24-9.8-23.44-16.41-39.63-17.12-16.68-.73-31.8,5-41.86,14.41A47.16,47.16,0,0,0,521,54.43c-18.78-.82-35.36,9.11-43,24a34.49,34.49,0,0,0-13.45-3.38c-17.92-.79-33.35,12.26-37,30.1-13.1,5.23-22.43,16.57-23,30.12-.69,15.6,10.38,29.32,26.26,34.51a39.26,39.26,0,0,0,69.4,10.43,44.06,44.06,0,0,0,23.21,7.88,44.52,44.52,0,0,0,31.35-11.16c7.8,12.32,20.67,20.67,35.6,21.33a43.68,43.68,0,0,0,31.31-11.58,55.76,55.76,0,0,0,27.7,8.73c29.29,1.29,54-19.74,55.2-47C705.39,128.9,693.85,111.52,676.45,102.77Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M464.17,272.26h-.11L441.53,271a2.13,2.13,0,0,1-2-2.24,2.06,2.06,0,0,1,2.24-2L464.29,268a2.13,2.13,0,0,1-.12,4.26Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M587.91,275.29a2.13,2.13,0,0,1-.12-4.26l22.52-1.23a2,2,0,0,1,2.25,2,2.13,2.13,0,0,1-2,2.24L588,275.29Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M482.17,271A32.93,32.93,0,1,1,515.1,238.1,33,33,0,0,1,482.17,271Zm0-61.6a28.67,28.67,0,1,0,28.66,28.67A28.69,28.69,0,0,0,482.17,209.43Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M571.77,271A32.93,32.93,0,1,1,604.7,238.1,33,33,0,0,1,571.77,271Zm0-61.6a28.67,28.67,0,1,0,28.66,28.67A28.69,28.69,0,0,0,571.77,209.43Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M540.16,236.89a2.16,2.16,0,0,1-1.42-.54c-9.2-8.25-21.66-.16-22.19.19a2.14,2.14,0,0,1-2.36-3.56c5.39-3.59,18-8.18,27.4.19a2.13,2.13,0,0,1-1.43,3.72Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M488.08,139.94c-11.06,0-18.9-2.77-23.37-8.27-6.55-8.07-3.16-18.74-3-19.19a2.14,2.14,0,0,1,4.06,1.33c0,.09-2.81,9,2.28,15.19,4.57,5.6,14.47,7.74,28.62,6.16a2.1,2.1,0,0,1,2.35,1.89,2.13,2.13,0,0,1-1.88,2.35A81.76,81.76,0,0,1,488.08,139.94Z"
              class="bf745ff3-d487-4892-9840-f9bc03550fe1"></path>
        <path d="M535.18,144.42c-6.19,0-9.87-.26-10-.27a2.14,2.14,0,0,1,.32-4.26c.61.05,61.48,4.35,107.71-23.39a2.14,2.14,0,1,1,2.2,3.66C599.35,141.78,554.77,144.42,535.18,144.42Z"
              class="bf745ff3-d487-4892-9840-f9bc03550fe1"></path>
        <path d="M528.76,290.1c-12.07,0-19.06-6.79-19.16-6.9a2.13,2.13,0,0,1,3-3c.56.55,13.45,12.8,35.3-.32a2.13,2.13,0,1,1,2.19,3.66C541.9,288.44,534.71,290.1,528.76,290.1Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M464.2,195.4a2.12,2.12,0,0,1-1.77-3.31c.1-.16,10.56-15.52,26.13-10.32a2.13,2.13,0,1,1-1.35,4c-12.52-4.18-21.15,8.5-21.23,8.63A2.14,2.14,0,0,1,464.2,195.4Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M607.33,198.49a2.13,2.13,0,0,1-2.07-1.61c0-.07-1.86-7-7.41-9.58-3.56-1.63-8-1.13-13.26,1.49a2.13,2.13,0,1,1-1.9-3.82c6.46-3.23,12.18-3.74,17-1.54,7.41,3.41,9.65,12,9.74,12.41a2.13,2.13,0,0,1-1.55,2.58A1.91,1.91,0,0,1,607.33,198.49Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M274.39,258a27.07,27.07,0,0,1-12.7-3.16c-8.21-4.25-12.65-9.51-14.57-14.57-20.07-3.76-29.48-24-29.58-24.28a2.13,2.13,0,0,1,3.88-1.76c.39.85,8.12,17.39,24.62,21.46a15.93,15.93,0,0,1,.45-5.7c2-7.56,9.28-12.59,17.7-12.19,4.94.22,9.46,5.06,9.67,10.35.09,2.45-.75,10.59-15.54,12.42a36.76,36.76,0,0,1-6.23.26c1.95,3.53,5.59,7.13,11.56,10.23,22,11.41,44.91-18.36,45.14-18.67a2.13,2.13,0,0,1,3.4,2.58C311.34,236.08,294.47,258,274.39,258Zm-23.93-21.55a33.63,33.63,0,0,0,7.34-.12c7.66-.95,12-3.87,11.79-8-.12-3.09-2.84-6.13-5.6-6.26-6.42-.32-11.88,3.43-13.38,9A11.93,11.93,0,0,0,250.46,236.44Z"
              class="a635c0bf-c78a-49dd-bca9-cad7ca5aedca"></path>
        <circle r="18.44" cy="395.68" cx="829.65" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></circle>
        <path d="M829.65,416.26a20.58,20.58,0,1,1,20.57-20.58A20.6,20.6,0,0,1,829.65,416.26Zm0-36.89A16.31,16.31,0,1,0,846,395.68,16.33,16.33,0,0,0,829.65,379.37Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <circle r="6.23" cy="245.25" cx="470.74" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></circle>
        <circle r="6.23" cy="245.25" cx="556.08" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></circle>
        <path d="M357.84,367.36s-46.93-67.49-68.26-41.89c-14,16.79,6.81,18.61,17.05,20a113.51,113.51,0,0,1,18.15,4C334.86,352.7,348.34,358.29,357.84,367.36Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M357.84,369.49a2.13,2.13,0,0,1-1.47-.59c-9.3-8.88-22.66-14.33-32.23-17.33a109.87,109.87,0,0,0-17.8-3.94l-1.61-.22c-7.93-1.07-18.79-2.54-21.42-9.3-1.51-3.88,0-8.46,4.63-14a17,17,0,0,1,14.35-6.55c24,1.05,55.95,46.64,57.3,48.58a2.13,2.13,0,0,1-1.75,3.35Zm-56.4-47.68a12.76,12.76,0,0,0-10.23,5c-2.39,2.88-5,6.9-3.92,9.72,1.71,4.42,11.91,5.8,18,6.63l1.63.22a113.68,113.68,0,0,1,18.49,4.09,108.49,108.49,0,0,1,21.7,9.34c-11.09-13.64-30.3-34.37-45-35Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <ellipse transform="translate(-50.29 47.73) rotate(-7.73)" ry="6.4" rx="21.33" cy="395.87" cx="327.98"
                 class="ec866187-f413-49ef-aca1-b2c926a96c4c"></ellipse>
        <path d="M320.05,405a44.74,44.74,0,0,1-6.74-.47c-5.32-.84-8.21-2.68-8.58-5.47h0c-.79-5.81,10.9-10.09,22.1-11.61a57.37,57.37,0,0,1,15.82-.17c5.32.84,8.21,2.68,8.58,5.47.79,5.81-10.9,10.09-22.1,11.61A67.75,67.75,0,0,1,320.05,405ZM309,398.46c.59,1.13,7.33,3.3,19.59,1.64s18.29-5.63,18.45-6.84c-.47-1.07-7.21-3.3-19.59-1.61S309.22,397.2,309,398.46Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M664.7,179.29s-12.8,34.14-8.53,42.67c0,0-4.27-4.27-12.8,0V192.09Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M897.37,302.36c-4.78,0-9.17-3.36-13.07-10-3.09-5.24-6.25-8-9.14-8.08h-.06c-3.64,0-6.74,4.3-7.9,6.16a29.27,29.27,0,0,1-6.45,7.6c-7.45,5.85-15.35,4.85-21.69-2.76-3.14-3.77-6.14-5.68-8.91-5.68s-4.94,1.91-6.27,3.52c-3,3.58-5.89,5.9-8.89,7.09-4.29,1.7-10.74,2.36-17-4.22-2.5-2.61-5-3.84-7.56-3.58-4.92.44-8.62,6-8.66,6a2.13,2.13,0,0,1-3.57-2.34c.19-.3,4.85-7.3,11.81-7.94,3.9-.36,7.62,1.28,11.06,4.88,3.74,3.91,7.92,5,12.39,3.2,2.32-.92,4.68-2.83,7.19-5.85,1.92-2.31,5.13-5.06,9.54-5.06h0c4.1,0,8.2,2.43,12.19,7.22,4.92,5.91,10.08,6.61,15.78,2.13a25,25,0,0,0,5.47-6.51c1.93-3.08,6.15-8.14,11.64-8.15,4.52.06,8.81,3.49,12.74,10.18,3.08,5.23,6.24,7.89,9.41,7.89h.06c4.56,0,8.75-5.74,10-7.93a2.13,2.13,0,0,1,3.73,2.07c-.23.42-5.68,10-13.65,10.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M897.37,327.67c-4.78,0-9.17-3.36-13.07-10-3.09-5.25-6.25-8-9.14-8.08h-.06c-3.64,0-6.74,4.3-7.9,6.15a29.27,29.27,0,0,1-6.45,7.6c-7.45,5.86-15.35,4.85-21.69-2.76-3.14-3.77-6.14-5.68-8.91-5.68s-4.94,1.92-6.27,3.52c-3,3.58-5.89,5.9-8.89,7.09-4.29,1.7-10.74,2.37-17-4.22-2.5-2.6-5-3.82-7.56-3.58-4.92.44-8.62,6-8.66,6a2.13,2.13,0,0,1-3.57-2.33c.19-.3,4.85-7.3,11.81-7.95,3.9-.36,7.62,1.29,11.06,4.88,3.74,3.91,7.92,5,12.39,3.21,2.32-.92,4.68-2.84,7.19-5.86,1.92-2.3,5.13-5.05,9.54-5.05h0c4.1,0,8.2,2.42,12.19,7.21,4.92,5.91,10.08,6.62,15.78,2.14a25.19,25.19,0,0,0,5.47-6.52c1.93-3.07,6.15-8.25,11.64-8.15,4.52.07,8.81,3.49,12.74,10.19,3.08,5.23,6.24,7.88,9.41,7.88h.06c4.56,0,8.75-5.74,10-7.93a2.14,2.14,0,0,1,3.73,2.08c-.23.41-5.68,10-13.65,10.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M643.37,254a2.27,2.27,0,0,1-.62-.09,2.14,2.14,0,0,1-1.42-2.67c0-.13,4.34-13.44,23.83-9.2a2.13,2.13,0,1,1-.91,4.17c-15.68-3.44-18.81,6.18-18.84,6.28A2.13,2.13,0,0,1,643.37,254Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M572.84,418.61c-26.78,1.08-41.24-6.35-48.94-17.45-4.26,0-17.2,1.18-17.06,4.27.68,15.16,33.43,31.08,66,29.78s58.4-17.31,57.72-32.48c-.09-2-6.08-2.06-9.9-2.92a5.12,5.12,0,0,0-5.17,1.78C608,411.08,596.26,417.68,572.84,418.61Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <rect transform="translate(-88.61 79.51) rotate(-6.78)" rx="8.78" height="217.6" width="755.2" y="678.39"
              x="248.8" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></rect>
        <path d="M273.3,652.83a20.79,20.79,0,0,1,33,14.36l16.54,145.56L339.39,958.3a20.78,20.78,0,0,1-28.94,21.41L176.13,921.26,41.8,862.81A20.78,20.78,0,0,1,37.74,827l117.78-87.11Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path transform="translate(-83.26 77.63) rotate(-6.78)"
              d="M244.37,632.3H982a8.78,8.78,0,0,1,8.78,8.78V807.91a42,42,0,0,1-42,42H244.37a8.78,8.78,0,0,1-8.78-8.78v-200a8.78,8.78,0,0,1,8.78-8.78Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M283.84,891.71a39.66,39.66,0,0,1-39.3-34.93L227.69,715.14a39.59,39.59,0,0,1,34.65-44l675.48-80.36a39.67,39.67,0,0,1,44,34.66l16.85,141.64a39.61,39.61,0,0,1-34.66,44L288.55,891.43A39.53,39.53,0,0,1,283.84,891.71Zm658.68-297a35.29,35.29,0,0,0-4.2.25L262.84,675.36a35.35,35.35,0,0,0-30.92,39.27l16.85,141.64A35.37,35.37,0,0,0,288,887.2l675.48-80.37a35.34,35.34,0,0,0,30.93-39.27L977.6,625.92A35.41,35.41,0,0,0,942.52,594.75Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M260.08,606.74a20.79,20.79,0,0,1,33,14.36l16.55,145.56,16.54,145.55a20.78,20.78,0,0,1-28.94,21.41L162.91,875.17,28.58,816.72A20.79,20.79,0,0,1,24.52,781L142.3,693.84Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M305.59,937.51a22.93,22.93,0,0,1-9.2-1.94L27.74,818.67a22.92,22.92,0,0,1-4.49-39.44L258.82,605a22.91,22.91,0,0,1,36.39,15.84L328.3,912a23,23,0,0,1-22.71,25.54ZM272.4,604.77a18.56,18.56,0,0,0-11,3.68L25.79,782.66a18.65,18.65,0,0,0,3.65,32.1l268.65,116.9a18.65,18.65,0,0,0,26-19.21L291,621.35a18.75,18.75,0,0,0-18.57-16.58Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M845.06,839.08c8.53,4.27,5.33,7.21-5.42,31.41,0,.07,0,4.27,0,12.8,0,14.41-11.42,24-25.19,28.2l-.41.13c-42.67,12.8-67.12-21.34-67.12-21.34S725.59,869,725.59,856.15s17.07,0,17.07,0c-4.27-21.33,12.8-8.53,12.8-8.53-4.27-21.34,17.06-4.27,17.06-4.27-4.26-17.07,8.54-12.8,17.07,0,7,10.46,25.6,17.07,25.6,17.07S834.26,833.69,845.06,839.08Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M795.37,916.6c-31.79,0-50-24.78-50.18-25.08-.67-.62-21.73-21.84-21.73-35.37,0-4.47,1.89-6.36,3.48-7.15,3.7-1.85,9.16.54,12.95,2.77-.3-4.64.73-7.66,3.12-9.17,2.93-1.84,6.83-.62,9.77.86-.16-3.91.86-6.49,3.07-7.83,3.77-2.3,9.66.47,13.74,3-.33-5.23,1.59-7.37,3.52-8.22,5.3-2.34,13.19,4.13,18.25,11.73,5.4,8.09,18.64,13.9,23.07,15.67,4.45-6,20.58-26.16,31.58-20.67,9.1,4.55,7,9.22-.12,24.69-1.21,2.64-2.59,5.66-4.13,9.11v12.32c0,13.83-10,25.14-26.7,30.24l-.41.13A67.13,67.13,0,0,1,795.37,916.6Zm-65.33-64a2.72,2.72,0,0,0-1.19.23c-.93.47-1.13,2.07-1.13,3.34,0,9.77,14.95,26.86,20.71,32.62,1.19,1.61,24.33,33,65,20.8l.43-.13c14.79-4.51,23.65-14.29,23.65-26.15v-8.51c0-4.69,0-4.69.19-5.14,1.62-3.65,3.06-6.81,4.32-9.56,7.5-16.38,7.2-16.54,2.09-19.09h0c-6.65-3.34-20.21,10.91-27.17,20.67a2.14,2.14,0,0,1-2.45.77c-.79-.28-19.38-7-26.67-17.9-5.07-7.62-11-11.08-13-10.19-.8.35-1.74,2.53-.25,8.49a2.14,2.14,0,0,1-3.4,2.19c-4.08-3.27-10.93-7.1-13.13-5.75-.44.27-1.77,1.63-.51,7.93a2.13,2.13,0,0,1-3.37,2.12c-2.65-2-7.21-4.16-8.89-3.11-.51.32-2,2-.54,9.52a2.14,2.14,0,0,1-3.37,2.13C738.23,855.5,733,852.58,730,852.58Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M772.52,843.35s4.27,17.07,25.6,25.6" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M798.12,871.08a2.21,2.21,0,0,1-.79-.15c-22.09-8.84-26.69-26.32-26.88-27.06a2.15,2.15,0,0,1,1.55-2.59,2.11,2.11,0,0,1,2.59,1.55c.17.65,4.35,16.15,24.32,24.14a2.13,2.13,0,0,1-.79,4.11Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M755.46,847.62S764,869,785.32,877.48" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M785.32,879.62a2,2,0,0,1-.79-.16c-21.93-8.77-30.69-30.15-31-31.05a2.13,2.13,0,0,1,4-1.59c.08.21,8.48,20.6,28.67,28.68a2.14,2.14,0,0,1-.79,4.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M742.66,856.15s8.53,21.33,25.6,29.87" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M768.26,888.15a2.09,2.09,0,0,1-1-.23c-17.59-8.79-26.26-30.08-26.62-31a2.13,2.13,0,1,1,4-1.58c.08.2,8.45,20.69,24.57,28.75a2.13,2.13,0,0,1-1,4Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M337.39,936.38s-18.13-75.41,0-75.41c10.05,0,10.05,45.25,10.05,45.25S342.42,856,357.5,861c4.77,1.59,10.05,45.25,10.05,45.25S366.37,861,377.61,861c10.05,0,5,45.25,5,45.25s12.16-38.11,20.11-30.16c5,5-2.7,29.35-2.8,35-.31,17.31-2.23,35.34-27.36,40.37C362.51,953.47,342.42,951.46,337.39,936.38Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M365.45,954.23c-10.84,0-25.6-3.73-30.09-17.18a1.54,1.54,0,0,0-.05-.17c-1.51-6.29-14.47-61.84-4.16-74.92a7.74,7.74,0,0,1,6.24-3.12c1.71,0,5.72,1.22,8.67,11.54,1-4.61,2.59-8.39,5-10.32a7.23,7.23,0,0,1,7.1-1.11c3.14,1,5.89,11.21,8.12,23.71.94-8.95,2.82-17.86,6.5-21.64,2.65-2.71,6.52-3,9-.21,4.23,4.72,4.58,19.13,4.11,30.57,3.57-8.32,8.43-17.22,13.26-18.4a5.29,5.29,0,0,1,5.11,1.57c4,4,2.19,14.57-.64,27.93a68,68,0,0,0-1.54,8.65c-.32,18.59-2.83,37.17-29.08,42.42A39.41,39.41,0,0,1,365.45,954.23Zm-26-18.44c4.78,14.1,24.46,15.22,32.72,13.58,23.15-4.63,25.34-20.76,25.64-38.31a65.75,65.75,0,0,1,1.64-9.46c1.57-7.45,4.5-21.33,1.79-24-.56-.55-.88-.49-1.09-.43-4.48,1.09-11.75,18-15.48,29.74a2.13,2.13,0,0,1-4.15-.89c1.54-13.82,2.37-37.53-1.92-42.33a1.25,1.25,0,0,0-1-.54,2.37,2.37,0,0,0-1.77.89c-5.8,6-6.41,32.45-6.15,42.16a2.13,2.13,0,0,1-4.25.31c-2.33-19.24-6.39-41.39-8.89-43.61a2.87,2.87,0,0,0-2.82.53c-3.43,2.74-4.75,12.6-4.94,23.07.5,5.45.79,12,.79,19.76a2.14,2.14,0,0,1-4.26.21,187.33,187.33,0,0,1-.84-18.84c-1.24-13.63-3.79-24.48-7.09-24.48a3.49,3.49,0,0,0-2.89,1.49C326.86,874.29,335.46,919.18,339.44,935.79Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M402.17,810.73l1-57.07-7.15.87.28-13.19,29.52-3.6L424.91,788l6.26-2.64-.32,13.87Zm18-96,5.3,16-20.78,2.53-5.3-16Zm37.38,12.51v-3.35l-23.69,2.88.12-10.09,23.82-2.9,0-.94-5.36-4.32,28.46-3.47-.22,5.94,23.95-2.92-.11,10.09-24,2.92-.12,3.37,19.85-2.42-.23,10.24-19.72,2.4-.13,3.38,25.94-3.17-.22,10.24-75.58,9.21.23-10.24,26.6-3.24.13-3.37-20.91,2.55.23-10.24Zm18.34,74.47,5.07-8,.05-7.26-26.33,3.21-.23,14.67L432.74,807l1-50.49L503.46,748l-.84,41.6a13.37,13.37,0,0,1-1.61,6.58,6.45,6.45,0,0,1-5.13,3.11Zm-21-21.09,26.34-3.21.06-3.9L455,776.77Zm.17-12.92,26.34-3.21.1-3.63-26.34,3.2Z"></path>
        <path d="M535.82,707.15l-3.77-3.44,26.34-3.21-3.28,10.61,13.1-1.6.25-10.1-5-4.5,30.18-3.67-.3,15.21,32.69-4-.19,12.78-32.82,4-.28,15.35L630.61,730l-.32,12.8-15.08,1.84-.4,24.36,12.58-1.53,5.07-5.72-.36,20.19L598.35,786a7.82,7.82,0,0,1-6.39-1.77,7.27,7.27,0,0,1-2.36-6.16l.46-30.42-23.43,2.86L549.12,792,524,795.09l17.52-41.49-16.81,2,.31-12.8,42.62-5.19L568,722.3,551,724.38,547.68,735l-21.31,2.6Z"></path>
        <path d="M646.4,779.1l5.22-13.39.84-46.05-5,.62.19-12.78,27.66-3.37-.89,53.3,18.79,3.21,61.55-7.49-.19,12.78-70.42,8.58-13.43-2.26-1.65,4.1Zm21.8-94.53L675.46,699l-20.11,2.45L648.08,687Zm35.21-4.29L701,693.34l9.67-1.18.23-10.23-5-4.5L731,674.37l-.28,15.34,17.61-2.14L748.13,699l-17.6,2.15-.17,12.91,20.11-2.45-.21,11.45-12.57,1.53-.24,10.23,10.06-1.22,5.21-5.74-.46,20.47-35.2,4.29.5-25.58-7.67.93L702,754.47l-20.11,2.45,7.92-26.49-9.93,1.22.22-11.45,30.18-3.67.17-12.92L698.89,705l-1.08,6.58-17.6,2.14L685,687,680.77,683Z"></path>
        <path d="M774.31,719.87l.44-22.89-8.61,1,.32-12.8,8.61-1.05.22-11.45-3.65-3.45,24.35-3-.28,15.34,6.36-.77-.32,12.8-6.22.76-.34,17.1,6.28-2.51-.16,14.12-6.41,2.53-.54,28.67a10.33,10.33,0,0,1-2.74,6.71,10,10,0,0,1-6.38,3.27l-20.39,2.48,8.88-13.17.41-19.79-8.73,3.35.31-14ZM827.89,733l.05-6.18-21.84,2.66.3-11.86,21.71-2.65.16-5.25,21.18-2.58-.16,5.26L871,709.7l-.3,11.86-21.57,2.63-.06,6.18,23.43-2.85-.28,12-23.43,2.85-.18,14-21.17,2.58.17-14-26.07,3.18.28-12Zm44.28-73.09,0,1.75-.37,16.84-19.51,13,23.9,10.93-25.54,3.11-11.29-5.61-15.67,10.37-19.06,2.33.17-5.26L826,693.16l-20.75-10.5L827.47,680l10.69,5L854.8,673.8l-49.5,6,.3-11.86Z"></path>
        <path d="M102.56,780.5a7.51,7.51,0,0,1-3.6-14l72.91-41.21A2.13,2.13,0,1,1,174,729l-72.91,41.21A3.09,3.09,0,0,0,99.6,774a3.06,3.06,0,0,0,3.54,2.15L275,750.59a2.16,2.16,0,0,1,2.42,1.8,2.12,2.12,0,0,1-1.79,2.42l-171.88,25.6A8.18,8.18,0,0,1,102.56,780.5Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M104.65,810.3a2.13,2.13,0,0,1-.3-4.24l174.93-25.6a2.13,2.13,0,1,1,.62,4.22L105,810.28A1.56,1.56,0,0,1,104.65,810.3Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="162.85" x2="833.46" y1="155.86" x1="768.85" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M833.47,165h-.23l-64.62-7a2.14,2.14,0,0,1-1.89-2.35,2.18,2.18,0,0,1,2.35-1.89l64.61,7a2.13,2.13,0,0,1-.22,4.25Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="123.55" x2="772.35" y1="106.37" x1="811.4" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M772.35,125.69a2.13,2.13,0,0,1-.86-4.09l39-17.19a2.14,2.14,0,0,1,1.72,3.91l-39,17.19A2.18,2.18,0,0,1,772.35,125.69Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="103.56" x2="754.22" y1="61.5" x1="792.58" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M754.22,105.7a2.14,2.14,0,0,1-1.57-3.58L791,60.07a2.13,2.13,0,0,1,3.15,2.87L755.8,105A2.14,2.14,0,0,1,754.22,105.7Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M600.62,230a2.13,2.13,0,0,1-.56-4.19L647,213.05a2.13,2.13,0,1,1,1.13,4.11L601.19,230A2.24,2.24,0,0,1,600.62,230Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
    </svg>


</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'svg1'
    }
</script>

<style>
    .bd557e99-0b60-410e-9190-ab39419af894 {
        fill: none;
    }

    .a54ce527-3476-4590-b6a3-daf0baba896f {
        fill: #e61f19;
        opacity: 0.2;
    }

    .ec866187-f413-49ef-aca1-b2c926a96c4c {
        fill: #fff;
    }

    .e1c3efd2-ec07-48e8-9f5a-049331813ab8 {
        fill: #040000;
    }

    .bf745ff3-d487-4892-9840-f9bc03550fe1 {
        fill: #fffdfd;
    }

    .a635c0bf-c78a-49dd-bca9-cad7ca5aedca {
        fill: #231815;
    }

    .a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d {
        fill: #060001;
    }
</style>

```

5. 在 App 组件中引入 svg1.vue 组件

```vue
<template>
    <!-- 引入 svg1 组件 -->
    <svg1 /><hr>
</template>

<script>
    import svg1 from './components/svg1.vue'

    export default {
        name: 'App',
        components: { svg1 }
    }
</script>

```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-684--OVWnWW2tEZ3agg.png)

---

1. 可在 `<svg></svg>` 内使用 `width、height` 属性修改矢量图尺寸

```vue
<template>
    <svg width="200px" height="200px" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" id="b52015b4-2459-46df-970a-a6cd264bdde9">
        <title>党建1024px尺寸</title>
        <rect height="1024" width="1024" class="bd557e99-0b60-410e-9190-ab39419af894"></rect>
        <path d="M892.19,468.81a6.4,6.4,0,0,1-2.87-12.48c1.71-.39,30.78-6.8,57.52,3.93,10-19.51,15.95-41.22,13.34-68.57C937.69,155.37,715.46,279.07,512.3,101.94c-102.19-89.1-203.12-67.57-268.64-3.67,12.66,18.83,31.68,36.7,42.36,45.3a6.4,6.4,0,0,1-8,10A270.16,270.16,0,0,1,242.43,118q-4.32-5.28-7.87-10.34c-70.65,77.13-93.35,205-17.69,283.08,21.76,22.47,31.31,44.24,33.46,65.51,25.26-.61,49.85,4.24,64.92,21a6.4,6.4,0,1,1-9.52,8.56c-12.19-13.54-33-17.5-55-16.89C247.4,586.07,45.29,689.44,470,816.65c213.73,64,320.93,33.34,364.64-46,43.41-78.83,18.26-98.79,32.05-169.25,11.26-57.6,49.61-90.25,73.73-129.75C917.6,463.19,892.55,468.73,892.19,468.81Z"
              class="a54ce527-3476-4590-b6a3-daf0baba896f"></path>
        <path d="M445.95,222.22h36.11a0,0,0,0,1,0,0v55.21a0,0,0,0,1,0,0H445.95A24.41,24.41,0,0,1,421.53,253v-6.38a24.41,24.41,0,0,1,24.41-24.41Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M482.06,279.56H445.22a25.85,25.85,0,0,1-25.82-25.82v-7.83a25.85,25.85,0,0,1,25.82-25.82h36.84a2.13,2.13,0,0,1,2.13,2.13v55.21A2.13,2.13,0,0,1,482.06,279.56Zm-36.84-55.21a21.58,21.58,0,0,0-21.55,21.56v7.83a21.58,21.58,0,0,0,21.55,21.55h34.71V224.35Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M437.16,246.55s17.11-3.73,22.44,7.16" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M459.6,255.85a2.12,2.12,0,0,1-1.91-1.2c-4.55-9.28-19.92-6.05-20.07-6a2.13,2.13,0,1,1-.91-4.16c.76-.17,18.81-3.95,24.81,8.3a2.14,2.14,0,0,1-1,2.86A2.09,2.09,0,0,1,459.6,255.85Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M332.29,593.16S311,678.51,317.59,720.67s51,22.29,51,22.29L395.9,613.49l-67.83-19.67"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M346.64,749.79a33,33,0,0,1-15.85-3.66c-8.26-4.49-13.42-13-15.31-25.13-5.84-37.56,9.77-107.47,13.83-124.6l-1.83-.54a2.13,2.13,0,1,1,1.19-4.09l1.69.49a2.13,2.13,0,0,1,4.05,1.17l62.09,18a2.13,2.13,0,0,1,1.49,2.49L370.64,743.41a2.13,2.13,0,0,1-1.22,1.5A62.14,62.14,0,0,1,346.64,749.79Zm-13.22-152.2c-4,17.19-19.35,86.6-13.73,122.75,1.68,10.8,6.1,18.21,13.12,22,12.38,6.75,29.62.73,33.89-1L393.41,615Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M439.67,436s-56.4,7.71-93.12,81.48c-13.84,27.81-23.65,58.87-32.77,77.8a22.12,22.12,0,0,0,11.62,30.09l52.89,21.52a22.15,22.15,0,0,0,28.63-11.63l34.64-79.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M644.74,404.62a245.08,245.08,0,0,0-58.61-5.74H555.21c-43.81-.85-87.52,18-126.43,42.89a41.54,41.54,0,0,0-18.87,29.16c-6,41.91-18.12,158.8-12.63,391,0,0,258.89,12.8,361.29-25.6L719.21,587.27,750,448.09c-23.87-17.07-72.12-36-105.3-43.47"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M493.66,866.07c-55,0-95.47-1.93-96.49-2a2.14,2.14,0,0,1-2-2.08c-5.53-234.23,7-351.73,12.66-391.38A43.73,43.73,0,0,1,427.63,440c46.08-29.44,89.08-44,127.63-43.22h30.85a249.59,249.59,0,0,1,59.1,5.78c31.37,7,80.84,25.78,106.07,43.83a2.11,2.11,0,0,1,.84,2.19L721.38,587.33,760.68,836a2.13,2.13,0,0,1-1.36,2.33C697.66,861.48,578.45,866.07,493.66,866.07Zm-94.3-6.15C423.46,861,659,870.3,756.19,835L717.1,587.6a2.1,2.1,0,0,1,0-.79L747.65,449c-25.13-17.49-72.88-35.5-103.37-42.32a245.11,245.11,0,0,0-58-5.69h-31c-38-.76-79.94,13.58-125.28,42.56A39.45,39.45,0,0,0,412,471.23C406.41,510.66,394,627.35,399.36,859.92Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M850.47,591.22l-74.11,66.25a16.69,16.69,0,0,1-24.53-2.53l-45-60.84c-22.81-30.83-33.63-69.25-28.57-107.26,3.4-25.54,13.95-47.5,39.51-52,64-11.41,117.41,99.55,136.45,136.28A16.7,16.7,0,0,1,850.47,591.22Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <polygon
                points="785.54 635.83 841.01 576.09 823.94 537.69 785.54 537.69 759.94 567.56 759.94 593.16 785.54 635.83"
                class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></polygon>
        <path d="M438.57,174.74s14.21,37.9,9.48,47.38c0,0,4.73-4.74,14.21,0V189Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M533.27,359.24s3.15,27.63-7.78,44.71c-5,7.8-1,18.22,7.75,21.32,18.55,6.58,48,11,81.29-6.7a10,10,0,0,0,3.23-15c-7-8.95-15.26-26.54-12.13-58.23Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M566.33,433.17a101.24,101.24,0,0,1-33.8-5.89,17,17,0,0,1-10.46-10.56,16,16,0,0,1,1.62-13.92c10.39-16.23,7.5-43.05,7.46-43.32a2.15,2.15,0,0,1,1.72-2.34l72.36-13.93a2.1,2.1,0,0,1,1.84.52,2.16,2.16,0,0,1,.69,1.78c-3,30.64,4.68,47.75,11.68,56.7a12.19,12.19,0,0,1-3.91,18.25C597.71,429.89,581,433.17,566.33,433.17ZM535.57,361c.51,6.76,1.34,29.1-8.29,44.13a11.78,11.78,0,0,0-1.17,10.23,12.78,12.78,0,0,0,7.84,7.93c18.35,6.51,47.06,10.64,79.59-6.58a7.91,7.91,0,0,0,2.54-11.84c-7.26-9.28-15.25-26.63-12.83-56.91Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path transform="translate(1301.48 499.65) rotate(180)"
              d="M642.37,222.22H681a0,0,0,0,1,0,0v55.21a0,0,0,0,1,0,0H646a25.55,25.55,0,0,1-25.55-25.55v-7.77a21.89,21.89,0,0,1,21.89-21.89Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M657.31,279.56H620.48a2.13,2.13,0,0,1-2.14-2.13V222.22a2.13,2.13,0,0,1,2.14-2.13h36.83a25.85,25.85,0,0,1,25.83,25.82v7.83A25.85,25.85,0,0,1,657.31,279.56Zm-34.7-4.27h34.7a21.58,21.58,0,0,0,21.56-21.55v-7.83a21.58,21.58,0,0,0-21.56-21.56h-34.7Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M525.86,130.65h44.46a72.62,72.62,0,0,1,72.62,72.62v70.87A94.85,94.85,0,0,1,548.09,369h0a94.85,94.85,0,0,1-94.85-94.85V203.27A72.62,72.62,0,0,1,525.86,130.65Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M548.09,371.12a97.08,97.08,0,0,1-97-97V130.65a2.13,2.13,0,0,1,2.13-2.13h189.7a2.13,2.13,0,0,1,2.13,2.13V274.14A97.09,97.09,0,0,1,548.09,371.12ZM455.37,132.79V274.14a92.72,92.72,0,1,0,185.44,0V132.79Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M676.45,102.77c.11-.85.21-1.71.25-2.59.72-16.45-12.91-30.41-30.45-31.19a33.66,33.66,0,0,0-12.36,1.77c-9.24-9.8-23.44-16.41-39.63-17.12-16.68-.73-31.8,5-41.86,14.41A47.16,47.16,0,0,0,521,54.43c-18.78-.82-35.36,9.11-43,24a34.49,34.49,0,0,0-13.45-3.38c-17.92-.79-33.35,12.26-37,30.1-13.1,5.23-22.43,16.57-23,30.12-.69,15.6,10.38,29.32,26.26,34.51a39.26,39.26,0,0,0,69.4,10.43,44.06,44.06,0,0,0,23.21,7.88,44.52,44.52,0,0,0,31.35-11.16c7.8,12.32,20.67,20.67,35.6,21.33a43.68,43.68,0,0,0,31.31-11.58,55.76,55.76,0,0,0,27.7,8.73c29.29,1.29,54-19.74,55.2-47C705.39,128.9,693.85,111.52,676.45,102.77Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M464.17,272.26h-.11L441.53,271a2.13,2.13,0,0,1-2-2.24,2.06,2.06,0,0,1,2.24-2L464.29,268a2.13,2.13,0,0,1-.12,4.26Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M587.91,275.29a2.13,2.13,0,0,1-.12-4.26l22.52-1.23a2,2,0,0,1,2.25,2,2.13,2.13,0,0,1-2,2.24L588,275.29Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M482.17,271A32.93,32.93,0,1,1,515.1,238.1,33,33,0,0,1,482.17,271Zm0-61.6a28.67,28.67,0,1,0,28.66,28.67A28.69,28.69,0,0,0,482.17,209.43Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M571.77,271A32.93,32.93,0,1,1,604.7,238.1,33,33,0,0,1,571.77,271Zm0-61.6a28.67,28.67,0,1,0,28.66,28.67A28.69,28.69,0,0,0,571.77,209.43Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M540.16,236.89a2.16,2.16,0,0,1-1.42-.54c-9.2-8.25-21.66-.16-22.19.19a2.14,2.14,0,0,1-2.36-3.56c5.39-3.59,18-8.18,27.4.19a2.13,2.13,0,0,1-1.43,3.72Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M488.08,139.94c-11.06,0-18.9-2.77-23.37-8.27-6.55-8.07-3.16-18.74-3-19.19a2.14,2.14,0,0,1,4.06,1.33c0,.09-2.81,9,2.28,15.19,4.57,5.6,14.47,7.74,28.62,6.16a2.1,2.1,0,0,1,2.35,1.89,2.13,2.13,0,0,1-1.88,2.35A81.76,81.76,0,0,1,488.08,139.94Z"
              class="bf745ff3-d487-4892-9840-f9bc03550fe1"></path>
        <path d="M535.18,144.42c-6.19,0-9.87-.26-10-.27a2.14,2.14,0,0,1,.32-4.26c.61.05,61.48,4.35,107.71-23.39a2.14,2.14,0,1,1,2.2,3.66C599.35,141.78,554.77,144.42,535.18,144.42Z"
              class="bf745ff3-d487-4892-9840-f9bc03550fe1"></path>
        <path d="M528.76,290.1c-12.07,0-19.06-6.79-19.16-6.9a2.13,2.13,0,0,1,3-3c.56.55,13.45,12.8,35.3-.32a2.13,2.13,0,1,1,2.19,3.66C541.9,288.44,534.71,290.1,528.76,290.1Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M464.2,195.4a2.12,2.12,0,0,1-1.77-3.31c.1-.16,10.56-15.52,26.13-10.32a2.13,2.13,0,1,1-1.35,4c-12.52-4.18-21.15,8.5-21.23,8.63A2.14,2.14,0,0,1,464.2,195.4Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M607.33,198.49a2.13,2.13,0,0,1-2.07-1.61c0-.07-1.86-7-7.41-9.58-3.56-1.63-8-1.13-13.26,1.49a2.13,2.13,0,1,1-1.9-3.82c6.46-3.23,12.18-3.74,17-1.54,7.41,3.41,9.65,12,9.74,12.41a2.13,2.13,0,0,1-1.55,2.58A1.91,1.91,0,0,1,607.33,198.49Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M274.39,258a27.07,27.07,0,0,1-12.7-3.16c-8.21-4.25-12.65-9.51-14.57-14.57-20.07-3.76-29.48-24-29.58-24.28a2.13,2.13,0,0,1,3.88-1.76c.39.85,8.12,17.39,24.62,21.46a15.93,15.93,0,0,1,.45-5.7c2-7.56,9.28-12.59,17.7-12.19,4.94.22,9.46,5.06,9.67,10.35.09,2.45-.75,10.59-15.54,12.42a36.76,36.76,0,0,1-6.23.26c1.95,3.53,5.59,7.13,11.56,10.23,22,11.41,44.91-18.36,45.14-18.67a2.13,2.13,0,0,1,3.4,2.58C311.34,236.08,294.47,258,274.39,258Zm-23.93-21.55a33.63,33.63,0,0,0,7.34-.12c7.66-.95,12-3.87,11.79-8-.12-3.09-2.84-6.13-5.6-6.26-6.42-.32-11.88,3.43-13.38,9A11.93,11.93,0,0,0,250.46,236.44Z"
              class="a635c0bf-c78a-49dd-bca9-cad7ca5aedca"></path>
        <circle r="18.44" cy="395.68" cx="829.65" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></circle>
        <path d="M829.65,416.26a20.58,20.58,0,1,1,20.57-20.58A20.6,20.6,0,0,1,829.65,416.26Zm0-36.89A16.31,16.31,0,1,0,846,395.68,16.33,16.33,0,0,0,829.65,379.37Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <circle r="6.23" cy="245.25" cx="470.74" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></circle>
        <circle r="6.23" cy="245.25" cx="556.08" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></circle>
        <path d="M357.84,367.36s-46.93-67.49-68.26-41.89c-14,16.79,6.81,18.61,17.05,20a113.51,113.51,0,0,1,18.15,4C334.86,352.7,348.34,358.29,357.84,367.36Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M357.84,369.49a2.13,2.13,0,0,1-1.47-.59c-9.3-8.88-22.66-14.33-32.23-17.33a109.87,109.87,0,0,0-17.8-3.94l-1.61-.22c-7.93-1.07-18.79-2.54-21.42-9.3-1.51-3.88,0-8.46,4.63-14a17,17,0,0,1,14.35-6.55c24,1.05,55.95,46.64,57.3,48.58a2.13,2.13,0,0,1-1.75,3.35Zm-56.4-47.68a12.76,12.76,0,0,0-10.23,5c-2.39,2.88-5,6.9-3.92,9.72,1.71,4.42,11.91,5.8,18,6.63l1.63.22a113.68,113.68,0,0,1,18.49,4.09,108.49,108.49,0,0,1,21.7,9.34c-11.09-13.64-30.3-34.37-45-35Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <ellipse transform="translate(-50.29 47.73) rotate(-7.73)" ry="6.4" rx="21.33" cy="395.87" cx="327.98"
                 class="ec866187-f413-49ef-aca1-b2c926a96c4c"></ellipse>
        <path d="M320.05,405a44.74,44.74,0,0,1-6.74-.47c-5.32-.84-8.21-2.68-8.58-5.47h0c-.79-5.81,10.9-10.09,22.1-11.61a57.37,57.37,0,0,1,15.82-.17c5.32.84,8.21,2.68,8.58,5.47.79,5.81-10.9,10.09-22.1,11.61A67.75,67.75,0,0,1,320.05,405ZM309,398.46c.59,1.13,7.33,3.3,19.59,1.64s18.29-5.63,18.45-6.84c-.47-1.07-7.21-3.3-19.59-1.61S309.22,397.2,309,398.46Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M664.7,179.29s-12.8,34.14-8.53,42.67c0,0-4.27-4.27-12.8,0V192.09Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M897.37,302.36c-4.78,0-9.17-3.36-13.07-10-3.09-5.24-6.25-8-9.14-8.08h-.06c-3.64,0-6.74,4.3-7.9,6.16a29.27,29.27,0,0,1-6.45,7.6c-7.45,5.85-15.35,4.85-21.69-2.76-3.14-3.77-6.14-5.68-8.91-5.68s-4.94,1.91-6.27,3.52c-3,3.58-5.89,5.9-8.89,7.09-4.29,1.7-10.74,2.36-17-4.22-2.5-2.61-5-3.84-7.56-3.58-4.92.44-8.62,6-8.66,6a2.13,2.13,0,0,1-3.57-2.34c.19-.3,4.85-7.3,11.81-7.94,3.9-.36,7.62,1.28,11.06,4.88,3.74,3.91,7.92,5,12.39,3.2,2.32-.92,4.68-2.83,7.19-5.85,1.92-2.31,5.13-5.06,9.54-5.06h0c4.1,0,8.2,2.43,12.19,7.22,4.92,5.91,10.08,6.61,15.78,2.13a25,25,0,0,0,5.47-6.51c1.93-3.08,6.15-8.14,11.64-8.15,4.52.06,8.81,3.49,12.74,10.18,3.08,5.23,6.24,7.89,9.41,7.89h.06c4.56,0,8.75-5.74,10-7.93a2.13,2.13,0,0,1,3.73,2.07c-.23.42-5.68,10-13.65,10.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M897.37,327.67c-4.78,0-9.17-3.36-13.07-10-3.09-5.25-6.25-8-9.14-8.08h-.06c-3.64,0-6.74,4.3-7.9,6.15a29.27,29.27,0,0,1-6.45,7.6c-7.45,5.86-15.35,4.85-21.69-2.76-3.14-3.77-6.14-5.68-8.91-5.68s-4.94,1.92-6.27,3.52c-3,3.58-5.89,5.9-8.89,7.09-4.29,1.7-10.74,2.37-17-4.22-2.5-2.6-5-3.82-7.56-3.58-4.92.44-8.62,6-8.66,6a2.13,2.13,0,0,1-3.57-2.33c.19-.3,4.85-7.3,11.81-7.95,3.9-.36,7.62,1.29,11.06,4.88,3.74,3.91,7.92,5,12.39,3.21,2.32-.92,4.68-2.84,7.19-5.86,1.92-2.3,5.13-5.05,9.54-5.05h0c4.1,0,8.2,2.42,12.19,7.21,4.92,5.91,10.08,6.62,15.78,2.14a25.19,25.19,0,0,0,5.47-6.52c1.93-3.07,6.15-8.25,11.64-8.15,4.52.07,8.81,3.49,12.74,10.19,3.08,5.23,6.24,7.88,9.41,7.88h.06c4.56,0,8.75-5.74,10-7.93a2.14,2.14,0,0,1,3.73,2.08c-.23.41-5.68,10-13.65,10.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M643.37,254a2.27,2.27,0,0,1-.62-.09,2.14,2.14,0,0,1-1.42-2.67c0-.13,4.34-13.44,23.83-9.2a2.13,2.13,0,1,1-.91,4.17c-15.68-3.44-18.81,6.18-18.84,6.28A2.13,2.13,0,0,1,643.37,254Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M572.84,418.61c-26.78,1.08-41.24-6.35-48.94-17.45-4.26,0-17.2,1.18-17.06,4.27.68,15.16,33.43,31.08,66,29.78s58.4-17.31,57.72-32.48c-.09-2-6.08-2.06-9.9-2.92a5.12,5.12,0,0,0-5.17,1.78C608,411.08,596.26,417.68,572.84,418.61Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <rect transform="translate(-88.61 79.51) rotate(-6.78)" rx="8.78" height="217.6" width="755.2" y="678.39"
              x="248.8" class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></rect>
        <path d="M273.3,652.83a20.79,20.79,0,0,1,33,14.36l16.54,145.56L339.39,958.3a20.78,20.78,0,0,1-28.94,21.41L176.13,921.26,41.8,862.81A20.78,20.78,0,0,1,37.74,827l117.78-87.11Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path transform="translate(-83.26 77.63) rotate(-6.78)"
              d="M244.37,632.3H982a8.78,8.78,0,0,1,8.78,8.78V807.91a42,42,0,0,1-42,42H244.37a8.78,8.78,0,0,1-8.78-8.78v-200a8.78,8.78,0,0,1,8.78-8.78Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M283.84,891.71a39.66,39.66,0,0,1-39.3-34.93L227.69,715.14a39.59,39.59,0,0,1,34.65-44l675.48-80.36a39.67,39.67,0,0,1,44,34.66l16.85,141.64a39.61,39.61,0,0,1-34.66,44L288.55,891.43A39.53,39.53,0,0,1,283.84,891.71Zm658.68-297a35.29,35.29,0,0,0-4.2.25L262.84,675.36a35.35,35.35,0,0,0-30.92,39.27l16.85,141.64A35.37,35.37,0,0,0,288,887.2l675.48-80.37a35.34,35.34,0,0,0,30.93-39.27L977.6,625.92A35.41,35.41,0,0,0,942.52,594.75Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M260.08,606.74a20.79,20.79,0,0,1,33,14.36l16.55,145.56,16.54,145.55a20.78,20.78,0,0,1-28.94,21.41L162.91,875.17,28.58,816.72A20.79,20.79,0,0,1,24.52,781L142.3,693.84Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M305.59,937.51a22.93,22.93,0,0,1-9.2-1.94L27.74,818.67a22.92,22.92,0,0,1-4.49-39.44L258.82,605a22.91,22.91,0,0,1,36.39,15.84L328.3,912a23,23,0,0,1-22.71,25.54ZM272.4,604.77a18.56,18.56,0,0,0-11,3.68L25.79,782.66a18.65,18.65,0,0,0,3.65,32.1l268.65,116.9a18.65,18.65,0,0,0,26-19.21L291,621.35a18.75,18.75,0,0,0-18.57-16.58Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M845.06,839.08c8.53,4.27,5.33,7.21-5.42,31.41,0,.07,0,4.27,0,12.8,0,14.41-11.42,24-25.19,28.2l-.41.13c-42.67,12.8-67.12-21.34-67.12-21.34S725.59,869,725.59,856.15s17.07,0,17.07,0c-4.27-21.33,12.8-8.53,12.8-8.53-4.27-21.34,17.06-4.27,17.06-4.27-4.26-17.07,8.54-12.8,17.07,0,7,10.46,25.6,17.07,25.6,17.07S834.26,833.69,845.06,839.08Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M795.37,916.6c-31.79,0-50-24.78-50.18-25.08-.67-.62-21.73-21.84-21.73-35.37,0-4.47,1.89-6.36,3.48-7.15,3.7-1.85,9.16.54,12.95,2.77-.3-4.64.73-7.66,3.12-9.17,2.93-1.84,6.83-.62,9.77.86-.16-3.91.86-6.49,3.07-7.83,3.77-2.3,9.66.47,13.74,3-.33-5.23,1.59-7.37,3.52-8.22,5.3-2.34,13.19,4.13,18.25,11.73,5.4,8.09,18.64,13.9,23.07,15.67,4.45-6,20.58-26.16,31.58-20.67,9.1,4.55,7,9.22-.12,24.69-1.21,2.64-2.59,5.66-4.13,9.11v12.32c0,13.83-10,25.14-26.7,30.24l-.41.13A67.13,67.13,0,0,1,795.37,916.6Zm-65.33-64a2.72,2.72,0,0,0-1.19.23c-.93.47-1.13,2.07-1.13,3.34,0,9.77,14.95,26.86,20.71,32.62,1.19,1.61,24.33,33,65,20.8l.43-.13c14.79-4.51,23.65-14.29,23.65-26.15v-8.51c0-4.69,0-4.69.19-5.14,1.62-3.65,3.06-6.81,4.32-9.56,7.5-16.38,7.2-16.54,2.09-19.09h0c-6.65-3.34-20.21,10.91-27.17,20.67a2.14,2.14,0,0,1-2.45.77c-.79-.28-19.38-7-26.67-17.9-5.07-7.62-11-11.08-13-10.19-.8.35-1.74,2.53-.25,8.49a2.14,2.14,0,0,1-3.4,2.19c-4.08-3.27-10.93-7.1-13.13-5.75-.44.27-1.77,1.63-.51,7.93a2.13,2.13,0,0,1-3.37,2.12c-2.65-2-7.21-4.16-8.89-3.11-.51.32-2,2-.54,9.52a2.14,2.14,0,0,1-3.37,2.13C738.23,855.5,733,852.58,730,852.58Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M772.52,843.35s4.27,17.07,25.6,25.6" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M798.12,871.08a2.21,2.21,0,0,1-.79-.15c-22.09-8.84-26.69-26.32-26.88-27.06a2.15,2.15,0,0,1,1.55-2.59,2.11,2.11,0,0,1,2.59,1.55c.17.65,4.35,16.15,24.32,24.14a2.13,2.13,0,0,1-.79,4.11Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M755.46,847.62S764,869,785.32,877.48" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M785.32,879.62a2,2,0,0,1-.79-.16c-21.93-8.77-30.69-30.15-31-31.05a2.13,2.13,0,0,1,4-1.59c.08.21,8.48,20.6,28.67,28.68a2.14,2.14,0,0,1-.79,4.12Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M742.66,856.15s8.53,21.33,25.6,29.87" class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M768.26,888.15a2.09,2.09,0,0,1-1-.23c-17.59-8.79-26.26-30.08-26.62-31a2.13,2.13,0,1,1,4-1.58c.08.2,8.45,20.69,24.57,28.75a2.13,2.13,0,0,1-1,4Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M337.39,936.38s-18.13-75.41,0-75.41c10.05,0,10.05,45.25,10.05,45.25S342.42,856,357.5,861c4.77,1.59,10.05,45.25,10.05,45.25S366.37,861,377.61,861c10.05,0,5,45.25,5,45.25s12.16-38.11,20.11-30.16c5,5-2.7,29.35-2.8,35-.31,17.31-2.23,35.34-27.36,40.37C362.51,953.47,342.42,951.46,337.39,936.38Z"
              class="ec866187-f413-49ef-aca1-b2c926a96c4c"></path>
        <path d="M365.45,954.23c-10.84,0-25.6-3.73-30.09-17.18a1.54,1.54,0,0,0-.05-.17c-1.51-6.29-14.47-61.84-4.16-74.92a7.74,7.74,0,0,1,6.24-3.12c1.71,0,5.72,1.22,8.67,11.54,1-4.61,2.59-8.39,5-10.32a7.23,7.23,0,0,1,7.1-1.11c3.14,1,5.89,11.21,8.12,23.71.94-8.95,2.82-17.86,6.5-21.64,2.65-2.71,6.52-3,9-.21,4.23,4.72,4.58,19.13,4.11,30.57,3.57-8.32,8.43-17.22,13.26-18.4a5.29,5.29,0,0,1,5.11,1.57c4,4,2.19,14.57-.64,27.93a68,68,0,0,0-1.54,8.65c-.32,18.59-2.83,37.17-29.08,42.42A39.41,39.41,0,0,1,365.45,954.23Zm-26-18.44c4.78,14.1,24.46,15.22,32.72,13.58,23.15-4.63,25.34-20.76,25.64-38.31a65.75,65.75,0,0,1,1.64-9.46c1.57-7.45,4.5-21.33,1.79-24-.56-.55-.88-.49-1.09-.43-4.48,1.09-11.75,18-15.48,29.74a2.13,2.13,0,0,1-4.15-.89c1.54-13.82,2.37-37.53-1.92-42.33a1.25,1.25,0,0,0-1-.54,2.37,2.37,0,0,0-1.77.89c-5.8,6-6.41,32.45-6.15,42.16a2.13,2.13,0,0,1-4.25.31c-2.33-19.24-6.39-41.39-8.89-43.61a2.87,2.87,0,0,0-2.82.53c-3.43,2.74-4.75,12.6-4.94,23.07.5,5.45.79,12,.79,19.76a2.14,2.14,0,0,1-4.26.21,187.33,187.33,0,0,1-.84-18.84c-1.24-13.63-3.79-24.48-7.09-24.48a3.49,3.49,0,0,0-2.89,1.49C326.86,874.29,335.46,919.18,339.44,935.79Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M402.17,810.73l1-57.07-7.15.87.28-13.19,29.52-3.6L424.91,788l6.26-2.64-.32,13.87Zm18-96,5.3,16-20.78,2.53-5.3-16Zm37.38,12.51v-3.35l-23.69,2.88.12-10.09,23.82-2.9,0-.94-5.36-4.32,28.46-3.47-.22,5.94,23.95-2.92-.11,10.09-24,2.92-.12,3.37,19.85-2.42-.23,10.24-19.72,2.4-.13,3.38,25.94-3.17-.22,10.24-75.58,9.21.23-10.24,26.6-3.24.13-3.37-20.91,2.55.23-10.24Zm18.34,74.47,5.07-8,.05-7.26-26.33,3.21-.23,14.67L432.74,807l1-50.49L503.46,748l-.84,41.6a13.37,13.37,0,0,1-1.61,6.58,6.45,6.45,0,0,1-5.13,3.11Zm-21-21.09,26.34-3.21.06-3.9L455,776.77Zm.17-12.92,26.34-3.21.1-3.63-26.34,3.2Z"></path>
        <path d="M535.82,707.15l-3.77-3.44,26.34-3.21-3.28,10.61,13.1-1.6.25-10.1-5-4.5,30.18-3.67-.3,15.21,32.69-4-.19,12.78-32.82,4-.28,15.35L630.61,730l-.32,12.8-15.08,1.84-.4,24.36,12.58-1.53,5.07-5.72-.36,20.19L598.35,786a7.82,7.82,0,0,1-6.39-1.77,7.27,7.27,0,0,1-2.36-6.16l.46-30.42-23.43,2.86L549.12,792,524,795.09l17.52-41.49-16.81,2,.31-12.8,42.62-5.19L568,722.3,551,724.38,547.68,735l-21.31,2.6Z"></path>
        <path d="M646.4,779.1l5.22-13.39.84-46.05-5,.62.19-12.78,27.66-3.37-.89,53.3,18.79,3.21,61.55-7.49-.19,12.78-70.42,8.58-13.43-2.26-1.65,4.1Zm21.8-94.53L675.46,699l-20.11,2.45L648.08,687Zm35.21-4.29L701,693.34l9.67-1.18.23-10.23-5-4.5L731,674.37l-.28,15.34,17.61-2.14L748.13,699l-17.6,2.15-.17,12.91,20.11-2.45-.21,11.45-12.57,1.53-.24,10.23,10.06-1.22,5.21-5.74-.46,20.47-35.2,4.29.5-25.58-7.67.93L702,754.47l-20.11,2.45,7.92-26.49-9.93,1.22.22-11.45,30.18-3.67.17-12.92L698.89,705l-1.08,6.58-17.6,2.14L685,687,680.77,683Z"></path>
        <path d="M774.31,719.87l.44-22.89-8.61,1,.32-12.8,8.61-1.05.22-11.45-3.65-3.45,24.35-3-.28,15.34,6.36-.77-.32,12.8-6.22.76-.34,17.1,6.28-2.51-.16,14.12-6.41,2.53-.54,28.67a10.33,10.33,0,0,1-2.74,6.71,10,10,0,0,1-6.38,3.27l-20.39,2.48,8.88-13.17.41-19.79-8.73,3.35.31-14ZM827.89,733l.05-6.18-21.84,2.66.3-11.86,21.71-2.65.16-5.25,21.18-2.58-.16,5.26L871,709.7l-.3,11.86-21.57,2.63-.06,6.18,23.43-2.85-.28,12-23.43,2.85-.18,14-21.17,2.58.17-14-26.07,3.18.28-12Zm44.28-73.09,0,1.75-.37,16.84-19.51,13,23.9,10.93-25.54,3.11-11.29-5.61-15.67,10.37-19.06,2.33.17-5.26L826,693.16l-20.75-10.5L827.47,680l10.69,5L854.8,673.8l-49.5,6,.3-11.86Z"></path>
        <path d="M102.56,780.5a7.51,7.51,0,0,1-3.6-14l72.91-41.21A2.13,2.13,0,1,1,174,729l-72.91,41.21A3.09,3.09,0,0,0,99.6,774a3.06,3.06,0,0,0,3.54,2.15L275,750.59a2.16,2.16,0,0,1,2.42,1.8,2.12,2.12,0,0,1-1.79,2.42l-171.88,25.6A8.18,8.18,0,0,1,102.56,780.5Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M104.65,810.3a2.13,2.13,0,0,1-.3-4.24l174.93-25.6a2.13,2.13,0,1,1,.62,4.22L105,810.28A1.56,1.56,0,0,1,104.65,810.3Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="162.85" x2="833.46" y1="155.86" x1="768.85" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M833.47,165h-.23l-64.62-7a2.14,2.14,0,0,1-1.89-2.35,2.18,2.18,0,0,1,2.35-1.89l64.61,7a2.13,2.13,0,0,1-.22,4.25Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="123.55" x2="772.35" y1="106.37" x1="811.4" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M772.35,125.69a2.13,2.13,0,0,1-.86-4.09l39-17.19a2.14,2.14,0,0,1,1.72,3.91l-39,17.19A2.18,2.18,0,0,1,772.35,125.69Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <line y2="103.56" x2="754.22" y1="61.5" x1="792.58" class="a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d"></line>
        <path d="M754.22,105.7a2.14,2.14,0,0,1-1.57-3.58L791,60.07a2.13,2.13,0,0,1,3.15,2.87L755.8,105A2.14,2.14,0,0,1,754.22,105.7Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
        <path d="M600.62,230a2.13,2.13,0,0,1-.56-4.19L647,213.05a2.13,2.13,0,1,1,1.13,4.11L601.19,230A2.24,2.24,0,0,1,600.62,230Z"
              class="e1c3efd2-ec07-48e8-9f5a-049331813ab8"></path>
    </svg>


</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: 'svg1'
    }
</script>

<style>
    .bd557e99-0b60-410e-9190-ab39419af894 {
        fill: none;
    }

    .a54ce527-3476-4590-b6a3-daf0baba896f {
        fill: #e61f19;
        opacity: 0.2;
    }

    .ec866187-f413-49ef-aca1-b2c926a96c4c {
        fill: #fff;
    }

    .e1c3efd2-ec07-48e8-9f5a-049331813ab8 {
        fill: #040000;
    }

    .bf745ff3-d487-4892-9840-f9bc03550fe1 {
        fill: #fffdfd;
    }

    .a635c0bf-c78a-49dd-bca9-cad7ca5aedca {
        fill: #231815;
    }

    .a226ff1a-3cb1-4ecf-84f6-4ccc6cc0a18d {
        fill: #060001;
    }
</style>

```

### ②、使用 SVG 文件

> <font color="#ff0000">现在可以直接使用 `img` 标签引入 `svg` 文件</font>

1. 安装依赖：`npm install svg-sprite-loader -D`
2. 创建目录：src/icons/svg ，将下载的 svg 文件放入其中
3. 修改文件 vue.config.js 

```javascript
const {defineConfig} = require('@vue/cli-service')
const path = require('path')
function resolve(dir) {
    return path.join(__dirname, '.', dir)
}
module.exports = defineConfig({
    transpileDependencies: true,
    // 关闭语法检查
    lintOnSave: false,

    chainWebpack: config => {
        // 重点：删除默认配置中处理 svg
        config.module.rules.delete("svg");
        config.module
            .rule('svg-sprite-loader')
            .test(/\.svg$/)
            .include
            // 处理 svg 目录，svg 文件存放的目录
            .add(resolve('src/icons/svg'))
            .end()
            .use('svg-sprite-loader')
            .loader('svg-sprite-loader')
            .options({
                symbolId: 'icon-[name]'
            })
    },
})

```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-702--2oHxwv9uw-5Mtg.png)

4. 修改文件 main.js

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'

// 导入 SvgIcon 组件
import SvgIcon from '@/components/SvgIcon/baseSvgIcon.vue'
const req = require.context('@/icons/svg', false, /\.svg$/)
req.keys().map(req)

// 创建应用实例对象：app(类似于之前 Vue2 中的 vm，但 app 比 vm 更“轻”)
createApp(App).component('svg-icon', SvgIcon).mount('#app')


```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-742--vsgChq3cI8Qqiw.png)

5. 在目录 components 中创建目录 SvgIcon ，在其中创建组件 baseSvgIcon.vue

```vue
<template>
    <!-- 只需要给一个 dom 存放 svg 即可 -->
    <svg :class="className" aria-hidden="true">
        <!-- 这边是做一个联动，根据传入的 iconName 来展示相关的 svg -->
        <use :xlink:href="iconName"></use>
    </svg>
</template>

<script>
    import { computed } from "@vue/reactivity";

    export default {
        name: "baseSvgIcon",
        // 因为是被调用，所以要传入 props
        props: {
            // 调用时传入的要使用的 svg 文件
            name: { type: String },
            // 调用时传入的要使用的 样式
            class: { type: String },
        },
        setup(props) {
            // 对传入的 name 进行处理，返回要使用的 svg 文件名
            const iconName = computed(() => {
                return props.name ? `#icon-${props.name}` : "#icon-趣味插画缺省页";
            });
            // 对传入的 class 进行处理，返回要使用的 样式名
            const className = computed(() => {
                return props.class ? `svg-icon${props.class}` : "svg-icon";
            });
            return { iconName, className };
        },
    };
</script>

<style scoped>
    /* 默认样式 */
    .svg-icon {
        width: 200px;
        height: 200px;
    }
</style>
```

6. 在 App 组件中引入 SvgIcon 组件，传入适当的参数即可使用

```vue
<template>
    <!-- 引入 svg1 组件 -->
    <svg1 /><hr>

    <!-- 引入 SvgIcon 组件，传递组件名 -->
    <SvgIcon name="请先选择" />
    <!-- 引入 SvgIcon 组件，传递组件名和样式名 -->
    <SvgIcon name="无网络" class="big" />
    <hr>
    <!-- 引入 SvgIcon 组件，不传递组件名和样式名，使用默认 svg 和 样式 -->
    <SvgIcon />
</template>

<script>
    import svg1 from './components/svg1.vue'
    import SvgIcon from '@/components/SvgIcon/baseSvgIcon.vue'

    export default {
        name: 'App',
        components: { svg1, SvgIcon }
    }
</script>

```

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-776--Ui2g4H5cufv-EA.png)

## 2、使用 axios

1. 安装 axios ：`npm i axios`
2. 修改 `main.js` 文件，引入并使用 `provide` 派发 axios

```javascript
// 引入的不再是 Vue 构造函数了，而是一个名为 createApp 的工厂函数
import { createApp } from 'vue'
// 引入 app 组件，他是所有组件的父组件
import App from './App.vue'
// 引入 axios
import axios from 'axios'

// 创建应用实例对象并挂载；使用 provide 派发 axios
createApp(App).provide("$axios", axios).mount('#app')

```

3. 修改（或创建） `vue.config.js` 文件，配置代理服务器

```javascript
const {defineConfig} = require('@vue/cli-service')
const path = require('path')
function resolve(dir) {
    return path.join(__dirname, '.', dir)
}
module.exports = defineConfig({
    transpileDependencies: true,

    // 配置代理服务器
    devServer: {
        proxy: {
            // /Boot1：请求前缀
            '/Boot1': {
                // 需要代理到的服务器
                target: 'http://43.138.106.181:9000',
                // 正则匹配，将请求路径中的 /Boot1 替换为空；若不加则路径是：http://localhost:8080/Boot1/Test/get
                pathRewrite: { '^/Boot1' : '' },
                // 用于支持 websocket
                ws: true,
                // 是否将请求伪装为服务器端口（默认为 true）
                changeOrigin: true
            },
        }
    }
})

```

4. 在组件中使用 `inject` 接受 `provide` 派发的 axios，然后即可使用 `axios` 发送请求

```javascript
<template>
    <button @click="getData">请求</button>
    <ul>
        <li v-for="person in persons" :key="person.id">ID：{{person.id}}，NAME：{{person.name}}</li>
    </ul>
</template>

<script>
    // 引入 vue 函数
    import { ref, inject } from 'vue'

    export default {
        name: 'HelloWorld',
        setup(){
            /**
             * 基本类型要使用 ref，若是使用 reactive，必须为对象
             * 数组若是使用 reactive，arr = nwArr 会使其失去响应式，必须要进行额外的梳理，比如改为使用 push
             */
            let persons = ref([])

            // 使用 inject 接受 provide 派发的 axios
            const $axios = inject("$axios");

            const getData = () => {
                $axios.get('/Boot1/Test/get').then((data)=>{
                    console.log("成功", data.data.data)
                    persons.value = data.data.data
                }).catch((data)=>{
                    console.log("失败", data)
                })
            }

            // 返回一个对象，则对象中的属性、方法，在模板中均可以直接使用
            return { persons, getData }
        }
    }
</script>

```

5. 结果

![image.png](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/2023-07-25-12--51-14-811--tCvWd6v948M0Jg.png)

## 3、vue3 vite 使用 pinia

> [https://pinia.vuejs.org/zh/introduction.html](https://pinia.vuejs.org/zh/introduction.html)
> 
> Vuex 最新版 = Vuex 5

1. 安装：`npm install pinia`
2. 在 main.js 中引入并挂载

```java
import { createApp } from 'vue'
import App from './App.vue'

// 引入 Pinia
import {createPinia} from 'pinia'

createApp(App).use(createPinia()).mount('#app');
```

3. 在 src 文件下创建一个 store 文件夹，并添加 index.js

```java
// 引入 Pinia
import { defineStore } from 'pinia'

/**
 * 1. 定义容器、导出容器
 * 参数1：容器的ID，必须是唯一的，后面Pinia会把所有的容器挂载到根容器
 * 参数2：一些选项对象，也就是state、getter和action
 * 返回值：一个函数，调用即可得到容器实例
 */
export const useCounterStore = defineStore('counter', {
    /**
     * 类似于 Vue2 组件中的 data，用于存储全局状态数据，但有两个要求
     * 1. 必须是函数，目的是为了在服务端渲染的时候避免交叉请求导致的数据状态污染
     * 2. 必须是箭头函数，这样是为了更好的 TS 类型推导
     */
    state: () => {
        return {
            count: 0
        }
    },
    actions: {},
})

/**
 * 2. 使用容器中的 state
 * 3. 通过 getter 修改 state
 * 4. 使用容器中的 action 同步和异步请求
 */
```

4. 在组件中使用

```java
<template>
    111
</template>

<script setup>
    import { useCounterStore } from "../store/index.js";

    const pinia = useCounterStore();

    console.log(pinia.count)
</script>
```

## 4、vue3 vite 使用 路由

### ①、使用

1. 安装路由：`npm install vue-router@4`
2. 在 src 目录下新建目录叫 router，新建一个 js 文件叫 index.js，文件内容如下：

```javascript
// 引入 路由 vue-router
import {createRouter, createWebHistory} from 'vue-router'
// 导入路由页面的配置
import routes from './routes'

// 路由参数配置，默认暴露
export default createRouter({
    // 使用hash(createWebHashHistory)模式，(createWebHistory是HTML5历史模式，支持SEO)
    history: createWebHistory(),
    routes: routes,
})

```

3. 接着新建一个 js 文件叫 routes.js，内容如下(可以自己继续添加其他页面)：

```javascript
// 路径配置
export default [
    {
        path: '/PanoramaOfTheScene',
        name: 'PanoramaOfTheScene',
        component: () => import('../pages/PanoramaOfTheScene.vue')
    }
]
```

4. 在 main.js 中使用路由

```javascript
import { createApp } from 'vue'
import App from './App.vue'

// 引入 路由 router
import router from './router'

createApp(App).use(router)
    .mount('#app');
```

5. 使用

### ②、路由嵌套

- routes.js 中，添加`children` 属性，在其中添加子路由

```javascript
// 路径配置
export default [
    {
        // 登录页
        path: '/',
        name: 'Login',
        component: () => import('../components/Login.vue')
    },{
        // 主页
        path: '/Home',
        name: 'Home',
        props: true,
        component: () => import('../components/Home.vue'),
        children: [
            {
                // 次级目录选项
                path: 'Titles',
                name: 'Titles',
                props: true,
                component: () => import('../pages/Home/Titles.vue')
            },{
                // 侧边栏
                path: 'Sider',
                name: 'Sider',
                props: true,
                component: () => import('../pages/Home/Sider.vue'),
                children: [
                    {
                        // 现场全景
                        path: 'PanoramaOfTheScene',
                        name: 'PanoramaOfTheScene',
                        props: true,
                        component: () => import('../pages/PanoramaOfTheScene/PanoramaOfTheScene.vue')
                    },{
                        // 火灾详情
                        path: 'FireDetails',
                        name: 'FireDetails',
                        component: () => import('../pages/FireDetails/FireDetails.vue')
                    },{
                        // 专家连线
                        path: 'ExpertConnection',
                        name: 'ExpertConnection',
                        component: () => import('../pages/ExpertConnection/ExpertConnection.vue')
                    },{
                        // 大屏
                        path: 'LargeScreen',
                        name: 'LargeScreen',
                        component: () => import('../pages/LargeScreen/LargeScreen.vue')
                    },{
                        // 用户管理
                        path: 'userManagement',
                        name: 'userManagement',
                        component: () => import('../pages/userManagement/userManagement.vue')
                    },{
                        // 部门管理
                        path: 'DepartmentManagement',
                        name: 'DepartmentManagement',
                        component: () => import('../pages/DepartmentManagement/DepartmentManagement.vue')
                    },{
                        // 角色管理
                        path: 'RoleManagement',
                        name: 'RoleManagement',
                        component: () => import('../pages/RoleManagement/RoleManagement.vue')
                    },{
                        // 通知管理
                        path: 'NotificationManagement',
                        name: 'NotificationManagement',
                        component: () => import('../pages/NotificationManagement/NotificationManagement.vue')
                    },{
                        // 系统设置
                        path: 'SystemSettings',
                        name: 'SystemSettings',
                        component: () => import('../pages/SystemSettings/SystemSettings.vue')
                    },{
                        // 知识库
                        path: 'knowledgeBase',
                        name: 'knowledgeBase',
                        component: () => import('../pages/knowledgeBase/knowledgeBase.vue')
                    },{
                        // 视频推流
                        path: 'VideoStreaming',
                        name: 'VideoStreaming',
                        component: () => import('../pages/VideoStreaming/VideoStreaming.vue')
                    },{
                        // 授权管理
                        path: 'AuthorizationManagement',
                        name: 'AuthorizationManagement',
                        component: () => import('../pages/AuthorizationManagement/AuthorizationManagement.vue')
                    }
                ]
            }
        ]
    }
]
```

### ③、路由传参

#### Ⅰ、发送

1. 首先在需要跳转的页面引入API：`useRouter`

```javascript
import { useRouter } from 'vue-router'
```

2. 在跳转页面定义 `router` 变量

```javascript
// 首先在 setup 中定义
 const router = useRouter()
```

3. 用 `router.push` 跳转页面

```javascript
// 字符串
router.push('home')
 
// 对象
router.push({ path: 'home' })
 
// 命名的路由
router.push({ name: 'user', params: { userId: '123' }})
 
// 带查询参数，变成 /register?userId=123
router.push({ path: 'register', query: { userId: '123' }}
```

4. 若是使用 `router-link` 的 `to` 属性传参：
```vue
<router-link @click="NavigationTabAdd(title)" :to="{ path: `/Home/Sider/${title.router}`, query: { siders: title.siders } }">
    <div>
        <border-outlined class="icon"/>
        <p>{{title.name}}</p>
    </div>
</router-link>
```

#### Ⅱ、接收

1. 在接收页面引入API：`useRoute`

```vue
import { useRoute } from 'vue-router'
```

2. 在接收页面定义变量 route，获取传过来的变量

```javascript
//首先在setup中定义
const route = useRoute()
//query
let userId=route.query.userId;
 
//params
let userId=route.params.userId;
```

### ④、创建多个路由文件

1. 在 router 目录下创建 `index.js` 文件

```js
// 引入 路由 vue-router
import {createRouter, createWebHistory} from 'vue-router'
// 导入路由页面的配置
import gather from './gather'

// 路由参数配置，默认暴露
export default createRouter({
    // 使用hash(createWebHashHistory)模式，(createWebHistory是HTML5历史模式，支持SEO)
    history: createWebHistory(),
    routes: gather
})
```

2. 在 router 目录下创建 `gather.js` 路由汇总文件

```js
// 路由汇总文件，引入其他路由文件
import home from "@/router/home.js";
import music from "@/router/music"

export default [
    ...home,
    ...music
]
```

3. 在 router 目录下创建 `home.js` ，代表主页的路由文件

```js
// 路径配置
export default [
    {
        // 登录页
        path: '/',
        name: 'Login',
        component: () => import('@/pages/home/Login.vue')
    },{
        // 主页
        path: '/Home',
        name: 'Home',
        component: () => import('@/pages/home/Home.vue')
    }
]
```

4. 在 router 目录下创建 `music.js` ，代表音乐的路由文件

```js
// 路径配置
export default [

]
```

### ⑤、设置子路由时的 /

1. 设置子路由时的 `/` 代表根路径
2. 比如父路由是 `/home`，其中设置的子路由 `file` 和 `/file` 的区别是：
3.  `file`：访问路径为：`/home/file`
4. `/file`：访问路径为：`/file`

## 5、vite 创建的 vue3 中使用 `@` 作为根路径

- 在 `vite.config.js` 中配置

```js
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from "path"

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    // 配置根路径
    resolve: {
        // 配置根路径别名
        alias: {
            "@": resolve(__dirname, "./src")
        }
    }
})

```

## 6、vue3 中使用 setup 语法糖时使用 props 接收参数

1. 父组件传递参数

```vue
<template>
    <div v-for="card in data" :key="card.id">
        <HomeCards :card="card"></HomeCards>
    </div>
</template>

<script setup>
    // 引入组件
    import HomeCards from "@/pages/home/HomeCards.vue";
    
    const data = [
        { id: 1, imgPath: "src/assets/svg/月亮.svg", introduce: "月海" },
        { id: 2, imgPath: "src/assets/svg/海浪.svg", introduce: "月海" },
        { id: 3, imgPath: "src/assets/svg/唱歌.svg", introduce: "音乐" },
        { id: 4, imgPath: "src/assets/svg/让电脑开口说话.svg", introduce: "论坛" },
    ]
</script>

<style scoped>

</style>
```

2. 子组件接收参数

```vue
<template>
    <div class="book">
        <p>{{props.card.introduce}}</p>
        <div class="cover">
            <img :src="props.card.imgPath" alt="">
        </div>
    </div>
</template>

<script setup>
    // 接收父组件传递的参数
    const props = defineProps(["card"])

</script>
```

## 7、npm 整理

### ①、阿里镜像的安装

> 阿里镜像通知网站：https://developer.aliyun.com/mirror/NPM

#### Ⅰ、方法一（建议使用方法二）

1. 使用阿里定制的 cnpm 命令行工具代替默认的 npm，输入以下代码

```shell
npm install -g cnpm --registry=http://registry.npmmirror.com
```

2. 检查是否安装成功：

```shell
cnpm -v
```

3. 安装成功之后，以后安装依赖包的方式和 npm 的是一样的，只是 npm 的命令换成是 cnpm 就可以了。

#### Ⅱ、方法二

1. 单次使用：

```shell
npm install --registry=http://registry.npmmirror.com
```

2. 永久替换：
3. 在开发 react-native 的时候，不要使用 cnpm，cnpm 安装的模块路径比较奇怪，packager 不能正常识别
4. 所以，为了方便开发，我们最好是直接永久使用淘宝的镜像源
5. 直接命令行的设置：

```shell
npm config set registry http://registry.npmmirror.com
```

6. 手动修改设置：

```shell
 1.打开 .npmrc 文件（C:\Program Files\nodejs\node_modules\npm\npmrc，没有的话可以使用 git 命令行建一个( touch .npmrc)，用 cmd 命令建会报错）
 2.增加 registry=http://registry.npmmirror.com  即可。
```

7. 如果需要恢复成原来的官方地址只需要执行如下命令:

```shell
npm config set registry https://registry.npmjs.org
```

8. 检测是否安装成功：

```shell
npm config get registry
```

### ②、

### ③、

### ④、

## 8、常见的 Vue 项目目录结构示例

### ①、使用 vue-cli 创建的项目

```shell
├── public/
│   ├── index.html          # 主 HTML 文件
│   ├── favicon.ico         # 网站图标
│   └── ...                 # 其他静态资源
├── src/
│   ├── assets/             # 静态资源（图片、字体、样式等）
│   │   ├── images/         # 图片资源
│   │   ├── styles/         # 全局样式文件
│   │   └── ...             # 其他资源文件
│   ├── components/         # 全局组件
│   │   ├── Header.vue      # 头部组件
│   │   ├── Footer.vue      # 底部组件
│   │   └── ...             # 其他组件
│   ├── views/              # 页面级组件（对应路由）
│   │   ├── Home.vue        # 主页
│   │   ├── About.vue       # 关于页面
│   │   └── ...             # 其他页面
│   ├── router/             # 路由配置文件
│   │   └── index.js        # 路由入口文件
│   ├── store/              # Vuex 状态管理（如有使用 Vuex）
│   │   └── index.js        # 状态管理入口文件
│   ├── App.vue             # 根组件
│   ├── main.js             # 入口 JS 文件
│   └── ...                 # 其他配置和工具文件
├── tests/                  # 测试文件
│   ├── unit/               # 单元测试
│   ├── e2e/                # 端到端测试
│   └── ...                 # 其他测试相关文件
├── dist/                   # 构建输出目录（生产环境）
├── node_modules/           # 依赖包目录
├── .gitignore              # Git 忽略文件配置
├── package.json            # 项目元数据和依赖
├── README.md               # 项目说明文档
└── vue.config.js           # Vue CLI 配置文件
```

1. `public/`：存放公共文件，这些文件不会被 Webpack 处理，直接被复制到构建输出目录下。`index.html` 是项目的主 HTML 文件，`favicon.ico` 是浏览器标签上的图标。
2. `src/`：源代码目录，存放所有与业务逻辑相关的代码。
	1. `assets/`：存放静态资源，如图片、字体、全局样式等。可以在项目中通过相对路径引用这些资源。
	2. `components/`：存放 Vue 组件，这些组件通常是可复用的小块 UI 元素，可以在不同的页面或其他组件中引入和使用。
	3. `views/`：存放页面级的组件，这些组件通常与路由相对应，每个 Vue 组件代表应用中的一个页面。
	4. `router/`：存放路由相关的代码，index.js 是路由的入口文件，负责配置应用的路由规则。
	5. `store/`：存放 Vuex 状态管理相关的文件（如果使用 Vuex），用于集中管理应用的全局状态。
	6. `App.vue`：根组件，整个应用的结构通常都在这里定义。
	7. `main.js`：应用的入口文件，在这里初始化 Vue 实例，并将其挂载到 DOM 中。
3. `tests/`：测试目录，用于存放单元测试和端到端测试文件。
4. `dist/`：构建输出目录，生产环境下编译后的文件会输出到这里。
5. `node_modules/`：存放所有通过 npm 安装的项目依赖包。
6. `.gitignore`：Git 忽略文件配置，用于指定不需要纳入版本控制的文件和目录。
7. `package.json`：项目的元数据文件，记录项目名称、版本、依赖关系、脚本等信息。
8. `README.md`：项目的说明文档，通常用来描述项目的功能、安装步骤、使用方法等。
9. `vue.config.js`：Vue CLI 的配置文件，用于自定义 Webpack 配置、开发服务器设置等。
10. 这种目录结构清晰且模块化，有助于开发和维护 Vue 项目。如果项目需求较为复杂，可以根据实际情况进一步细化目录结构。例如，添加 `services/` 目录来存放与 API 交互的代码，或创建 `mixins/` 目录来存放可复用的 Vue mixins。

### ②、使用 vite 创建的项目

```shell
├── public/
│   ├── favicon.ico         # 网站图标
│   └── ...                 # 其他静态资源，如robots.txt等
├── src/
│   ├── assets/             # 静态资源（图片、字体、样式等）
│   │   ├── images/         # 图片资源
│   │   ├── styles/         # 全局样式文件（如main.css）
│   │   └── ...             # 其他资源文件
│   ├── components/         # 全局复用组件
│   │   ├── HeaderComponent.vue # 头部组件
│   │   ├── FooterComponent.vue # 底部组件
│   │   └── ...             # 其他组件
│   ├── views/              # 页面级组件，通常对应路由
│   │   ├── HomeView.vue    # 主页组件
│   │   ├── AboutView.vue   # 关于页面组件
│   │   └── ...             # 其他页面
│   ├── router/             # 路由配置
│   │   └── index.js        # 路由定义，使用Vue Router
│   ├── store/              # 状态管理（如使用Vuex或Pinia）
│   │   └── index.js        # 状态管理定义
│   ├── App.vue             # 应用根组件
│   ├── main.js             # 应用入口文件
│   └── ...                 # 其他配置和工具脚本
├── tests/                  # 测试文件夹
│   ├── unit/               # 单元测试
│   ├── e2e/                # 端到端测试
│   └── ...                 # 其他测试文件
├── index.html              # 主 HTML 文件（Vite 通常将此文件放在根目录）
├── vite.config.js          # Vite 配置文件
├── package.json            # 项目依赖和脚本
├── README.md               # 项目文档
└── .gitignore              # Git 忽略文件配置
```

1. **静态资源**：位于 `public` 文件夹中的资源将会被直接复制到最终的构建目录中而不会经过 Vite 处理，适合放置 `favicon.ico` 和一些不需要处理的静态文件。而 `src/assets/` 目录则用于放置需要经过 Vite 处理的资源如 LESS、SASS 文件或 JavaScript 中引用的图片
2. **碎片页面/组件**：通常放在 `src/views/` 目录下，每个文件代表一个路由的视图
3. **导航代码**：放在 `src/router/` 目录中，这里存放 Vue Router 的路由配置
4. **全局样式**：可以放在 `src/assets/styles/` 目录下，通过在 `main.js` 或单独的组件中引入使用
5. **配置文件**：`vite.config.js` 是 Vite 的配置文件，位于项目根目录，用于配置插件、优化等
6. 这样的结构有利于维护一个清晰、模块化的项目架构，适应现代 web 开发的需要
7. 使用 Vite 创建的 Vue 项目结构通常会与 Vue CLI 创建的项目结构类似，但有一些细微的差异，主要是因为 Vite 是一个更现代化的开发工具，更倾向于使用原生 ES 模块，并且在配置和构建方面更为轻量

## 9、vue 的部署

### ①、直接部署生产环境（非打包）

1. 将生产代码复制到服务器，即除了 `.git`、`.idea`、`node_modules` 等非代码目录外
2. 在服务器项目的根目录，执行命令，安装依赖

```shell
npm install
```

3. 启动开发服务器：

```shell
npm run build
```

4. 直接访问即可

### ②、打包后部署到服务器

1. 在项目根目录执行打包命令，执行完毕后，项目根目录会生成 `dist` 目录

```shell
npm run build
```

2. 将 `dist` 目录中的所有文件上传到服务器
3. 然后使用后台服务端（比如 java 服务端）或者 nginx  来返回 `index.html` 文件和其他资源

### ③、vue 打包部署后页面空白，也没有报错

#### Ⅰ、原因

- 路由的 history 模式为 html5 模式： `createWebHistory("/")` 导致的

#### Ⅱ、解决办法 1

- 路由的 history 模式改为 `createWebHashHistory()`

```shell
// 创建并导出一个新的路由实例
export default createRouter({
    // 使用 hash 模式的路由历史；hash 模式使用 URL 中的 hash 部分（#）来作为路由地址
    history: createWebHashHistory(),
    // 定义路由规则；通过展开运算符 ... 将导入的路由合并到当前的路由配置中
    routes: []
})
```

#### Ⅲ、解决办法 2

> vue 官网的说明：https://router.vuejs.org/zh/guide/essentials/history-mode.html

1. 配置 `vue.config.js` 中的 publicPath

```js
module.exports = {
  // 根目录
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
};
```

2. 配置 vue-router

```js
const router = createRouter({
  //根目录
  history: createWebHistory("/"),
  routes
})
```

3. 配置 nginx 的 server

```nginx
location / {
    root   /opt/app/fontend;
    index index.html index.htm;
    try_files  $uri $uri/ /index.html;
}
```

4. 把打包后生成的 css、js、html 等文件放入服务器中的 /opt/app/fontend 目录下，访问对应 ip:端口 即可看到页面。

### ④、打包后图片等资源文件没有被打包

#### Ⅰ、原因

1. vite 官方默认的配置，如果资源文件在 assets 文件夹打包后会把图片名加上 hash值，但是直接通过 `:src="imgSrc"` 方式引入并不会在打包的时候解析，导致开发环境可以正常引入，打包后却不能显示的问题
2. 这里我们先看看vite官方文档的解释：https://vitejs.bootcss.com/guide/assets.html
3. 我们看到实际上我们不希望资源文件被 wbpack 编译可以把图片放到 public 目录会更省事，不管是开发环境还是生产环境，可以始终以根目录保持图片路径的一致，这点跟 webpack 是一致的

![|675](https://openlist.yuehai.fun:63/d/TakeDown/Web/JS%E6%A1%86%E6%9E%B6/attachments/Pasted%20image%2020240905131130.png)

4. 看到这里，也许问题就解决了，如果在 vite 确实需要将静态文件放在 assets，我们再往下看：
5. 这里我们先假设：
	1. 静态文件目录：`src/assets/images/`
	2. 我们的目标静态文件在 `src/assets/images/home/home_icon.png`
6. 尝试过 require 动态引入， 发现报错：require is not defind，这是因为 require 是属于 Webpack 的方法

```vue
<img :src="require('@/assets/images/home/home_icon.png')" />
```

#### Ⅱ、第一种方式（适用于处理单个链接的资源文件）

1. 先将图片使用 `import` 引入，在通过 `:src` 使用

```vue
import homeIcon from '@/assets/images/home/home_icon.png'

<img :src="homeIcon" />
```

2. 若是文件很多，一个个的引入太麻烦

#### Ⅲ、第二种方式（适用于处理多个链接的资源文件）

> 推荐，这种方式传入的变量可以动态传入文件路径！！

1. 工具文件目录： `src/utils/resourceReader.js`

```js
/**
 * 获取图片资源
 * @param path 图片路径
 * @returns {string} 图片资源路径
 */
export const readImage = (path) => {
    /**
     * new URL() 方法用于创建一个新的 URL 对象，该对象表示指定的绝对或相对 URL
     * import.meta.url 属性返回当前模块的绝对 URL，模块是指当前文件
     * href 属性返回完整的 URL，包括主机名、端口号、路径等
     * 通过 new URL() 方法将图片路径转换为绝对路径，然后返回
     */
    return new URL(`../assets/images/${path}`, import.meta.url).href;
};
```

2. 使用方式：

```vue
<template>
    <!-- 使用返回的图片资源路径，显示图片 -->
    <img :src="imgPath" alt="">
</template>

<script setup>
    /**
     * 此处代码块用于获取由路由传递的导航标签数据，展示主页导航卡片
     * 引入资源读取工具
     */
    import { readImage } from '@/utils/resourceReader.js';
    // 图片文件的路径
    const path = "home/月球.svg"
    // 调用方法，返回图片资源路径
    const imgPath = readImage(path);
</script>
```

### ⑤、

### ⑥、

## 10、安装卸载库

1. 安装库：`npm install 库名`

```shell
npm install vue-router@4
```

2. 卸载库：`npm uninstall 库名`

```shell
npm uninstall vue-router@4
```

## 11、

## 12、

## 13、
## 14、
## 15、




