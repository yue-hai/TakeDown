# 一、项目整理

1. 鼓励用户购买特定的产品。会议里提到了一种策略，用户购买一种产品，然后可以获得额外的商品，例如购买一个捆绑的啤酒，然后可以获得额外的一罐啤酒
2. 分析收集到的用户在购物过程中扫描的条形码、购买数量以及购物车的重量变化等数据
3. 还有改进弹出窗口策略、优化捆绑销售流程等措施来提高用户购物体验

## 1、项目结构

```
java/jp/retailai/raicart
├── base
├── bean
│	└── operationLog
│	└── scale
├── deployer
│	└── battery
│	└── camera
│	└── installation
│	└── logger
├── event
├── guide
├── network
├── room
├── ui
│	└── bag
│	└── base
│	└── cancel
│	└── common
│	└── couponlist
│	└── employee
│	└── end
│	└── login
│	└── management
│	└── nobarcode
│	└── payment
│	└── pin
│	└── pop
│	└── register
│	└── scanreminder
│	└── shopping
│	└── standby
├── utils
├── view
	
res
├── anim
├── drawable
├── drawable-v24
├── layout
├── mipmap-anydpi-v26
├── mipmap-hdpi
├── mipmap-mdpi
├── mipmap-xhdpi
├── mipmap-xxhdpi
├── mipmap-xxxhdpi
├── navigation
├── raw
├── values
├── values-en-rUS
```

## 2、可用的购物车

| 所在地 | 车号 | ip                  |
| ------ | ---- | ------------------- |
| 青岛   | 1041 | 不固定              |
| 烟台   |      | 172.18.7.22         |
|        |      | 172.20.5.155        |
|        | 1066 | 172.18.7.13         |
| 日本   |      | ~~~10.105.12.193~~~ |
|        | 1243 | 10.105.12.229       |
|        | 1250 | 10.105.12.172       |

## 3、流程

> 关掉 adb 进程：taskkill /F /IM adb.exe
> 
> 强制结束程序：adb shell am force-stop jp.retailai.raicart

1. 连接：`adb connect 172.20.5.192`
2. 查看已连接设备： `adb devices`
3. 远程显示：`scrcpy`
4. gitbash：
5. 唤醒，输入从业员号，模拟扫描从业员：`i-emp`
6. 设定购物车静音模式：
	1. `silent`
	2. `adb shell media volume --show --stream 3 --set 0`
7. 模拟用户登录：`i-user`，登录密码为 id 的倒数第二位，四个数都是
8. 模拟扫描商品：`i-jan`
9. 结账，输入从业员号，模拟扫描从业员：`i-emp`
10. 卸载应用：`adb uninstall jp.retailai.raicart`
11. 安装应用：
	1. `i-app`
	2. `adb install -r -d --user 0 /d/app-debug.apk`

## 4、adb 常用命令

1. 多设备时要在 adb 后加 -s 指定设备
2. 官网：
	1. https://android-doc.github.io/tools/help/adb.html
	2. https://android-doc.github.io/tools/help/shell.html#shellcommands
3. 关于ADB更多的用法可以参考：https://github.com/mzlogin/awesome-adb

| 命令 | 描述 |
| ---- | ---- |
|adb shell svc wifi disable/enable|关闭wifi/开启wifi|
|adb devices|查看当前连接的设备|
|adb shell media volume --show --stream 3 --get|获取当前多媒体音量大小|
|adb disconnect xxx.xxx.xxx.xxx|断开指定的wifi设备连接|
|adb shell media volume --show --stream 3 --set 1|设定当前多媒体音量大小|
|adb disconnect|断开所有wifi连接设备|
|adb shell setprop service.adb.tcp.port 5555|设置adb服务端口为5555， 打开adb网络调试功能|
|adb connect device_ip_address[:5555]|利用ip连接新的android设备，需要在同一网络环境下|
|adb get-state|获取连接状态，有3种：device，offline，unknown|
|adb start-server|启动adb服务|
|adb kill-server|关闭adb服务|
|adb uninstall package|卸载程序，package是包名|
|adb install xxx.apk|安装程序|
|adb shell am start -n package/package.MainActivity|启动程序，package是包名|
|adb shell am force-stop package|强制结束程序，package是包名|
|adb pull /sdcard/DebugLog/20220805.log C:\Users\10153702\Desktop|将设备里的文件拉取到本地|
|adb push C:\Users\10153702\Desktop\20220805.log /sdcard/DebugLog/20220805.log|将本地文件上传到设备里|
|adb shell dumpsys package jp.retailai.raicart|查看应用相关信息|
|adb shell dumpsys meminfo jp.retailai.raicart|查看应用占用内存情况|
|adb shell dumpsys cpuinfo | findstr jp.retailai.raicart|查看应用cpu占用情况|
|adb shell input keyevent 66|模拟按回车键|
|adb shell input keyevent 3|模拟按HOME键|
|adb shell input text 2960000000012|输入字符串|
|adb shell input keyevent 26|灭/亮屏|
|adb shell input keyevent 82|解锁屏幕|
|adb shell input tap x y|按照(x,y)位置模拟点击|
|adb shell input swipe x1 y1 x2 y2|从(x1,y1)位置到(x2,y2)位置模拟滑动|
|adb shell monkey -p jp.retailai.raicart 100>C:\Users\10153702\Desktop\\monkey_log.txt|执行 monkey100 次随意点击测试，并记录日志到本地|

## 5、一些登录卡整理

### ①、用户卡

| 卡号          | 密码 | 描述                              |
| ------------- | ---- | --------------------------------- |
| 2960000000012 | 1111 |                                   |
| 2960000000029 | 2222 |                                   |
| 2960000000036 | 3333 |                                   |
| 2960000000043 | 4444 |                                   |
| 2960000000050 | 5555 | point 可以用                      |
| 2960000000067 | 6666 |                                   |
| 2960000000074 | 7777 |                                   |
| 2960000000081 | 8888 |                                   |
| 2960000000098 | 9999 |                                   |
| 2999000000081 | 0081 | 为非会员卡 （仅限于【研修模式】） |
| 2960000001771 | 8001 | 为非会员卡                        |
| 2960000001770 | 9522 | 为非会员卡                        |

### ②、从业员卡

| 卡号 | 描述 |
| ---- | ---- |
| 2000100764206     |      |

### ③、supay 账号

| 卡号 | 描述 |
| ---- | ---- |
| 2979000006146     |      |

![|389](attachments/Pasted%20image%2020230928105710.png)

### ④、SCT 账号

| 卡号 | 描述 |
| ---- | ---- |
| 2000100764206     |      |

## 6、一些商品整理

1. 输入商品：`adb shell input text xxx`
2. 回车确认：`adb shell input keyevent 66`

| 商品类型 | id            | 名称 |
| -------- | ------------- | ---- |
| 2 倍      | 4902410140962 |      |
| 10 倍     | 02721523      |      |
| 5 P       | 19014617005   |      |
|        | 4560282120019   |      |
| 防范     | 4901422152208 |      |

## 7、github review 模板

1. <font color="#ff0000">新建分支</font>
2. 提交该分支应该提交的代码
3. 推送分支到<font color="#ff0000">新分支</font>
4. 新建拉取请求 Pull requests
5. 选中本次 poc 的<font color="#ff0000">基础分支</font>与刚才推送的<font color="#ff0000">新分支</font>

![](attachments/Pasted%20image%2020231031133836.png)

6. github review 模板

```

SSCPOC-1927 Build:thanks page

# Overview
https://retailai.atlassian.net/browse/SSCPOC-1927

# Feature & Changes
- Increase points earned from activities

# Notes
none

# Screenshots


分支已推送：poc/category-point-campaign-thanksPage
review 已提交：https://github.com/retail-ai-inc/raicart/pull/273

```

7. 选择审查人

![|188](attachments/Pasted%20image%2020231031111341.png)

8. review 时选择 Approve

![](attachments/Pasted%20image%2020231008123601.png)

## 8、购物车硬件相关

1. 购物车屏幕大小：1280 * 800

## 9、签名打 staging 包

1. 进入项目根目录
2. 执行命令打包：`gradlew.bat clean assembleStaging`

![|725](attachments/Pasted%20image%2020230926165200.png)

3. 成功后 `..\app\build\outputs\apk\staging` 目录下有 app-staging.apk

![|683](attachments/Pasted%20image%2020230926165255.png)

4. 然后将以下文件解压后拷贝到 `..\app\build\outputs\apk\staging` 目录下：<a href="attachments/签名.zip" alt="文档">签名.zip</a>

![|700](attachments/Pasted%20image%2020230926165606.png)

5. 再执行：`Java -jar signapk.jar platform.x509.pem platform.pk8 app-staging.apk app-staging-signed.apk`
6. 完成后会有 staging 包：app-staging-signed.apk

## 10、postman 调用后端接口

1. 首先访问这个接口获取 Token： (POST) `https://sandbox.raicart.io/v1/user/4u/c/signin`
2. 请求头参数：
	1. `Client-Id`：项目的 secret.gradle 文件中，`manju` 的 `clientId`
	2. `Client-Secret`：项目的 secret.gradle 文件中，`manju` 的 `clientSecret`
	3. `UUID`：购物车的 uuid，在 melopan 和购物车的管理页面上都可以获取到
3. 请求体参数
	1. 格式：`application/json`
	2. 参数：`userId` 为登录的用户卡号，`pincode` 为密码

```json
{
    "userId": "2960000000050",
    "pincode": "5555" 
}
```

4. 访问后得到的数据中，第一个参数是 `accessToken`，拿到他的值

![|775](attachments/Pasted%20image%2020231019101441.png)

5. 访问想要访问的接口，如： (GET) `https://sandbox-macaron.raicart.io/v2/user/r/coupon/recommendation/4910026530008`
6. 请求头参数：`Authorization`：`Bearer 刚刚拿到的accessToken`
7. 即可得到数据

![|775](attachments/Pasted%20image%2020231019101503.png)

# 二、一些问题

## 1、如何找到指定页面

1. 先看看项目结构
2. 进入 `res/navigation/nav_graph.xml` 导航碎片页面
3. 根据相应碎片名称可知其场景，各场景中有其使用的 `action`
4. `action` 的 `app:destination` 属性对应 `fragment` 的 `id`
5.  `fragment` 的 `android:name` 对应其本身的代码逻辑页面
6. 代码逻辑页面的 `layoutId` 方法对应了 `xml` 布局文件

```Kotlin
override fun layoutId(): Int {
	return R.layout.fragment_end
}
```

7. 若是 `res/navigation/nav_graph.xml` 导航碎片页面中没有，可根据页面出现的时机，和代码逻辑、项目结构，去指定的代码文件中查找
8. 比如新增商品弹窗应该是在 `java/jp/retailai/raicart/ui/shopping/ShoppingFragment.kt` 中定义的，根据代码逻辑可知是这个属性

```Kotlin
/**
 * 新增商品弹窗
 */
private var itemAddCartDialog: AddItemAnimationDialog? = null
```

9. 这样就从这里进入 `AddItemAnimationDialog` 类，然后根据 `getLayout` 方法进入 `fragment_dialog_success` 布局文件

## 2、关于构建和 gradle 版本

1. 截至 3.10，该项目使用的 gradle 版本为 6.7.1
2. 设置 -> 构建工具 -> gradle

![](attachments/Pasted%20image%2020230427110736.png)

3. 项目结构 -> Project

![](attachments/Pasted%20image%2020230427110805.png)


## 3、melopan 配置导入

1. 配置项在 melopan 上进行配置

![|700](attachments/Pasted%20image%2020230905132049.png)

2. 配置导入代码文件：`java/jp/retailai/raicart/MainViewModel.kt`
3. 其中方法：`getCartConfig`
4. 通过属性名，如 `add_item_popup_time` 进行属性的赋值

```Kotlin
/**
 * 通过远程获取数据，此处获取的的是新增物品的弹窗关闭时间
 * 这些时间是在别处配置的，启动时会通过网络获取这些时间并赋值给相应变量
 */
"add_item_popup_time" -> {
	Constant.add_item_popup_time = element.value
}
```


## 4、日志的查看

1. staging 或者 release 那种 signed 的包，必须得第二天在服务器上取 log，本地的没有权限取到
	1. 凌晨 1点~5点 之间随机时间点进行上传。关机则不会进行上传；
	2. 访问 [ダッシュボード | Retail AI, inc (raicart.io)](https://sandbox-console.raicart.io/ja/admin/dashboard) 进行下载
2. 连接设备后在本地查看 debug 日志，路径：`/sdcard/DebugLog/xxx.log`

![](attachments/Pasted%20image%2020230504150017.png)

## 5、adb 链接经常断开

> https://sandbox-console.raicart.io/

1. 进入 melopan 的 SSC 中

![|800](attachments/Pasted%20image%2020230911160354.png)

2. 点击对应购物车的 `Enable ADB` 按钮

![|675](attachments/Pasted%20image%2020230911160507.png)

3. 修改弹窗中的 `Duration`，值为开启 `ADB` 功能的时间

![|700](attachments/Pasted%20image%2020230911162443.png)

4. 点击弹出的弹窗中的 `Enable` 按钮

![|700](attachments/Pasted%20image%2020230911160548.png)

5. 等待完成，变为 `disable ADB` 即为完成

![|725](attachments/Pasted%20image%2020230911160658.png)

## 6、3.9 之后的版本 debug 日志乱码

> https://sandbox-console.raicart.io/

1. 当软件进入 standby 页面之后会自动上传  debug 日志
2. 所以稍等几分钟，从 melopan 上下载  debug 日志即可

## 7、sct 无法进入的解决办法

1. 卸载 `MicrosoftEdgeWebView2RuntimeInstallerX64` 然后重新安装
2. 若是无法卸载，则进入远程桌面：
3. 连接地址：`172.20.3.11:33896`，`administrator`、`admin1234`
4. 连接地址：`172.20.3.11:33892`，`administrator`、`admin1234`

# 三、poc 笔记

## 1、1979 推荐商品地图

1. ui
2. log 格式

We can record the IDs, categories, and click counts of the recommended products that customers click on in order to determine which products customers want to buy but don't know where to find.

Current oplog:
```json
{
    "amount": 0,
    "barcode": "",
    "cardNo": "2960000000012",
    "categoryId": "null",
    "categoryName": "null",
    "companyID": "1",
    "coupon": "null",
    "isNonBarcodeItem": false,
    "isSuccess": true,
    "operationName": "Recommender Details",
    "operationTime": "2023/09/04 14:48:18.21",
    "otherCartId": "null",
    "posNo": "1069",
    "productName": "",
    "recommend": "[{\"couponId\":\"\",\"displaySessionId\":\"\",\"image\":\"https://cdnstaging.raicart.io/images/retailer/item/867b8fb34b154032870a449e117a849e/ea8301508bc7467fa6b4759e2029ca42/10/P6/Vk/SkpmIivFeyh0OYqQRZRmPPUOeDg0rpfLefVkP610.webp\",\"isCoupon\":false,\"itemId\":\"\",\"itemMasterId\":\"\",\"itemName\":\"ワァン（ちゃんぽんスープ）\",\"price\":\"149\"}]",
    "storeID": "3",
    "subsidiaryId": "1",
    "systemView": "Shopping",
    "uploadState": 0,
    "weightValue": "null"
}
```

Here is a modified example I wrote:
```json
{
    "amount": 2,
    "barcode": "5f76aa653e648335380b74f2",
    "cardNo": "2960000000012",
    "categoryId": "null",
    "categoryName": "BUMON_CODE:27, MINI_BUMON_CODE:6",
    "companyID": "1",
    "coupon": "null",
    "isNonBarcodeItem": false,
    "isSuccess": true,
    "operationName": "Recommender Details",
    "operationTime": "2023/09/04 14:48:18.21",
    "otherCartId": "null",
    "posNo": "1069",
    "productName": "",
    "recommend": "[{\"couponId\":\"\",\"displaySessionId\":\"\",\"image\":\"https://cdnstaging.raicart.io/images/retailer/item/867b8fb34b154032870a449e117a849e/ea8301508bc7467fa6b4759e2029ca42/10/P6/Vk/SkpmIivFeyh0OYqQRZRmPPUOeDg0rpfLefVkP610.webp\",\"isCoupon\":false,\"itemId\":\"\",\"itemMasterId\":\"\",\"itemName\":\"ワァン（ちゃんぽんスープ）\",\"price\":\"149\"}]",
    "storeID": "3",
    "subsidiaryId": "1",
    "systemView": "Shopping",
    "uploadState": 0,
    "weightValue": "null"
}
```

or:
```json
{
    "amount": 2,
    "barcode": "5f76aa653e648335380b74f2",
    "cardNo": "2960000000012",
    "categoryId": "null",
    "categoryName": "{\"id\": \"5f76c3d13e6483353832f0d8\",\"level\": 4,\"categoryType\": \"BUMON_CODE\",\"remoteCategoryId\": 27},{\"id\": \"5f76c3d3b16d29f980ab6e59\",\"level\": 5,\"categoryType\": \"MINI_BUMON_CODE\",\"remoteCategoryId\": 6}",
    "companyID": "1",
    "coupon": "null",
    "isNonBarcodeItem": false,
    "isSuccess": true,
    "operationName": "Recommender Details",
    "operationTime": "2023/09/04 14:48:18.21",
    "otherCartId": "null",
    "posNo": "1069",
    "productName": "",
    "recommend": "[{\"couponId\":\"\",\"displaySessionId\":\"\",\"image\":\"https://cdnstaging.raicart.io/images/retailer/item/867b8fb34b154032870a449e117a849e/ea8301508bc7467fa6b4759e2029ca42/10/P6/Vk/SkpmIivFeyh0OYqQRZRmPPUOeDg0rpfLefVkP610.webp\",\"isCoupon\":false,\"itemId\":\"\",\"itemMasterId\":\"\",\"itemName\":\"ワァン（ちゃんぽんスープ）\",\"price\":\"149\"}]",
    "storeID": "3",
    "subsidiaryId": "1",
    "systemView": "Shopping",
    "uploadState": 0,
    "weightValue": "null"
}
```


## 2、

## 3、

## 4、

## 5、

# 四、

# 五、

## 1、

## 2、

## 3、

## 4、

## 5、

## 6、

## 7、

## 8、

## 9、

---

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

### ⑩、

### ⑪、⑫、⑬、⑭、⑮、⑯、⑰、⑱、⑲、⑳

### ㉑、㉒、㉓、㉔、㉕、㉖、㉗、㉘、㉙、㉚

### ㉛、㉜、㉝、㉞、㉟、㊱、㊲、㊳、㊴、㊵

### ㊶、㊷、㊸、㊹、㊺、㊻、㊼、㊽、㊾、㊿

#### Ⅰ、

#### Ⅱ、

#### Ⅲ、

#### Ⅳ、

#### Ⅴ、

#### Ⅵ、

#### Ⅶ、

#### Ⅷ、

#### Ⅸ、

#### Ⅹ、















