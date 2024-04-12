# 一、项目整理

## 1、项目结构

```shell
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

## 4、一些登录卡整理

### ①、用户卡

| 卡号          | 密码 | 描述                              |
| ------------- | ---- | --------------------------------- |
| 2960000000012 | 1111 |                                   |
| 2960000000029 | 2222 |                                   |
| 2960000000036 | 3333 |                                   |
| 2960000000043 | 4444 |                                   |
| 2960000000050 | 5555 |                       |
| 2960000000051 | 5555 | point 可以用                      |
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
| 2000100764206 |  |
|  |  |

## 5、一些商品整理

1. 输入商品：`adb shell input text xxx`
2. 回车确认：`adb shell input keyevent 66`

| 商品类型 | 名称 | id | Non-barcode |
| ---- | ---- | ---- | ---- |
| 2 倍 | トライアルブレッド（６） | 4902410140962 |  |
| 10 倍 | ｸｰﾙ･ﾌﾞｰｽﾄﾌﾚｯｼｭ8･ﾎﾞｯｸｽ | 02721523 |  |
| 5 P | アイムス　7歳以上用チキン | 19014617005 |  |
| non-plu | ケンコウゾウリ・リン | 4906943047620 |  |
|  | 産直野菜 | 2230001003009 |  |
| 防范 | しゃもじホルダー付き粒名 | 20081058 |  |
|  | とうもろこし１本 | 2532295000000 |  |
|  | おーいお茶緑茶 | 4901085003800 |  |
|  | しゃもじホルダー付き粒名 | 20081058 |  |
|  | パン粉　無地１ｋｇ | 0401410600031 |  |
|  | ﾗｰｸ･ｽｰﾊﾟｰ･MKSB | 45099724 |  |
|  | うまみ丸ごと野菜　国産豚 | 4903285702118 |  |
|  | オオバ　オオイタサン | 49306767 |  |
|  | メーカーズマーク | 085246500576 |  |
|  | １９６ストロングゼロレモ | 4901777192782 |  |
| 生鮮食品お惣菜： | 十勝おはぎ（つぶあん） | 2530921000998 |  |
|  | 生椎茸　（サンマッシュ） | 4560282120019 |  |
| 調味料・加工食品・菓子 | ブラックサンダー | 4903032001594 | ![\|225](attachments/Pasted%20image%2020240204090420.png) |
|  | コアラのマーチ＜チョコ＞ | 4903333066254 |  |
| 飲料 | 烏龍茶 | 4522646293166 | ![\|225](attachments/Pasted%20image%2020240202151314.png) |
|  | バヤリース　アップル　Ｐ | 4514603328318 |  |
| 冷蔵・冷凍 | 雪見　ベリーレアチーズ | 45127366 |  |
|  | イカ・ネギ焼き | 4952951326394 |  |
| 生活消耗品 | ＣＪ除菌ウェットティッシ | 4962035612466 |  |
|  | `ｷｭｷｭｯﾄ_CLEAR泡ｽﾌﾟﾚｰGF_本` | 4901301321961 |  |
| 生活雑貨 | 小皿 | 4905660022491<br> |  |
|  | ダイヤモンドシャープナー | 4972940601189 |  |
| 衣料品・靴 | 長袖東レ綿100%シャツ | 4512754964546 |  |
|  | セーター | 2103006792004 |  |
|  | ロング　シャツ | 4518564299618 |  |
| スポーツ・ペット・レジャー | 雑　記　帳 | 4972822109192 |  |
|  | ビーズストラップ（アソー | 1360017103 |  |
|  | キャンドル　アイスクリー | 4542804011623 |  |
| 不可达成分类的商品 | レジ袋 | 4522646330991 |  |
|  | 時計 | 4937996565380 |  |
|  | 万上芳醇本みりん１．１Ｌ | 4901515519611 |  |
|  | 家电 | 4983771856624 |  |
|  |  |  | ![\|225](attachments/Pasted%20image%2020240204133443.png) |

## 6、github review 模板

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

9. LGTM：Looks Good To Me. 朕知道了 代码已经过 review，可以合并

## 7、购物车硬件相关

1. 购物车屏幕大小：1280 * 800

## 8、签名打 staging 包

1. 进入项目根目录
2. 执行命令打包：`gradlew.bat clean assembleStaging`

![|725](attachments/Pasted%20image%2020230926165200.png)

3. 成功后 `..\app\build\outputs\apk\staging` 目录下有 app-staging.apk

![|683](attachments/Pasted%20image%2020230926165255.png)

4. 然后将以下文件解压后拷贝到 `..\app\build\outputs\apk\staging` 目录下：<a href="attachments/签名.zip" alt="文档">签名.zip</a>

![|700](attachments/Pasted%20image%2020230926165606.png)

5. 再执行：`Java -jar signapk.jar platform.x509.pem platform.pk8 app-staging.apk app-staging-signed.apk`
6. 完成后会有 staging 包：app-staging-signed.apk

## 9、
## 10、

# 二、一些问题

## 1、关于构建和 gradle 版本

1. 截至 3.10，该项目使用的 gradle 版本为 6.7.1
2. 设置 -> 构建工具 -> gradle

![](attachments/Pasted%20image%2020230427110736.png)

3. 项目结构 -> Project

![](attachments/Pasted%20image%2020230427110805.png)

## 2、melopan 配置导入

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

## 3、日志获取 （以 1041 车为例）

> 1. staging 或者 release 的那种包，oplog 必须得第二天在服务器上取 log，本地的没有权限取到
> 2. 凌晨 1点~5点 之间随机时间点进行上传。关机则不会进行上传；
> 3. 访问 [ダッシュボード | Retail AI, inc (raicart.io)](https://sandbox-console.raicart.io/ja/admin/dashboard) 进行下载

### ①、在购物车本地获取

#### Ⅰ、debug log

1. 连接设备后在本地查看 debug 日志，路径：`/sdcard/DebugLog/xxx.log`
2. 但是 3.9 之后的版本本地 debug 是加密的，若是想拿到不加密的可以让设备进入 stanby 页面，会自动上传 debug，等待上传后在 melopan 或 firebase 上获取
3. 若是在 melopan 或 firebase 上无法获取，可使用下面的脚本来解密：

```python
import os.path
import base64
import json
import subprocess

from Crypto.Cipher import AES

from Crypto.Util.Padding import unpad

"""
关于 Crypto 包报错的解决方法：

可能是由于 Python 包管理器 pip 在下载和安装包时默认将大小写敏感的文件名保持一致，
因此在安装 Crypto 库时，会将文件名保持为"crypto"，而 Python 的模块导入是大小写敏感的，
因此需要手动将文件名改为大写的"Crypto"才能正常运行。
"""


""" 对SSC的【全部是密文的日志文件】或者【含有明文和密文的日志文件(可能由于版本更新导致)】进行解码

1. 按行读取
2. 使用 Base64 对行文本进行解密，得到 json 文本
3. 解析 json 文本，拿到 iv 字段的值并进行 Base64 解密得到16位的字符串
4. 对 aeskey 进行 Base64 解码，得到明文
5. 从 json 字符串中拿到 value 字段，将 value 字段的最后两位 \u003d 转换成 =（代码中会自动处理）
6. 使用 aes-256-cbc 算法、aeskey 的明文，iv 的明文，对 value 的字符串进行解码，即可得到原文。
   
上述是在 melonpan 中进行的一个处理，由于我们已经知道了本番的 aes_key 和 iv_key 的明文，所以代码中直接使用了，没有解码的过程。

解码完成后会自动打开结果目录。
"""

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


def open_explorer(target_path):
    path = os.path.normpath(target_path)
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


keys = {
    "staging": {
        "aes_key": "************************************",
        "iv_key": "************************************",
        "aes_key_clear_bytes": b"************************************",
        "iv_key_clear_bytes": b"************************************",
        "start_text": "************************************"
    },
    "release": {
        "aes_key": "************************************",
        "iv_key": "************************************",
        "aes_key_clear_bytes": b"************************************",
        "iv_key_clear_bytes": b"************************************",
        "start_text": "************************************"
    }
}


class DecodingLogs:

    def __init__(self, is_staging=True) -> None:
        key = "staging" if is_staging else "release"
        self.AES_KEY = keys.get(key).get("aes_key")
        self.IV_KEY = keys.get(key).get("iv_key")

        self.AES_KEY_CLEAR_BYTES = keys.get(key).get("aes_key_clear_bytes")
        self.IV_KEY_CLEAR_BYTES = keys.get(key).get("iv_key_clear_bytes")

        self.START_TEXT = keys.get(key).get("start_text")

    def decoding_dir(self, src_dir, dst_dir):
        """解码路径中的所有日志文件

        Args:
            src_dir (str): 源文件目录
            dst_dir (str): 解码后放置文件的目录
        """
        filenames = os.listdir(src_dir)
        if len(filenames) <= 0:
            print("该目录下无任何文件")
            return

        os.makedirs(dst_dir, exist_ok=True)

        for filename in filenames:
            file = os.path.join(src_dir, filename)
            dst_filename = "{0}-{1}".format("output", filename)
            dst_file = os.path.join(dst_dir, dst_filename)
            self.decoding_log(file, dst_file)

        open_explorer(dst_dir)

    def decoding_log(self, src_file, dst_file):
        """解码日志

        Args:
            src_file (str): 源文件
            dst_file (str): 解码后生成的文件
            is_staging (bool, optional): 是否为测试环境，默认为测试环境. Defaults to True.
        """
        if not os.path.exists(src_file):
            print("文件不存在。")
            return

        if os.path.exists(dst_file):
            os.remove(dst_file)

        with open(dst_file, "a", encoding="utf8") as writer:

            with open(src_file, "r", encoding="utf8") as reader:
                # 读取行
                lines = reader.readlines()
                for line in lines:
                    line = line.strip()

                    text = self.decoding_line(line)
                    writer.write(text)

        open_explorer(dst_file)

    def decoding_line(self, line):
        """解码单行文本

        Args:
            line (str): 当行文本

        Returns:
            str: 解码后的文本
        """
        aes = AES.new(self.AES_KEY_CLEAR_BYTES, mode=AES.MODE_CBC, iv=self.IV_KEY_CLEAR_BYTES)

        if not line.startswith(self.START_TEXT):
            return line

        if line.endswith(','):
            line = line[:-1]

        line += ("=" * (4 - len(line) % 4))
        line_json_text = base64.b64decode(line).decode("utf-8")
        line_json_data = json.loads("{0}".format(line_json_text))
        real_value = line_json_data["value"].strip()

        data = base64.b64decode(real_value)
        res = aes.decrypt(data)
        res = unpad(res, 16)
        clear_text = res.decode("utf8")

        return clear_text.replace("\r\n", "\n")


if __name__ == "__main__":
    # 使用方式
    src_file = r""
    dst_file = r""
    # 本番环境日志 解码文件
    release_decoding = DecodingLogs(False)
    release_decoding.decoding_log(src_file, dst_file)

    src_dir = r""
    dst_dir = r""
    # 测试环境日志 解码目录
    staging_decoding = DecodingLogs()
    staging_decoding.decoding_dir(src_dir, dst_dir)

```

#### Ⅱ、op log

1. 连接设备后在本地获取 sqLite 数据库，路径：`/data/data/jp.retailai.raicart/databases/cart_database`
2. 获取 `cart_database` 数据库文件后，将其拖入 Idea 或其他数据库管理软件中
3. 其中的 `OperationLog` 表即为 oplog 表

### ②、在 melopan 上获取

#### Ⅰ、debug log

1. 访问 [ダッシュボード | Retail AI, inc (raicart.io)](https://sandbox-console.raicart.io/ja/admin/dashboard)
2. 点击：小売企業 -> 企業

![](attachments/Pasted%20image%2020240403132610.png)

3. 选择最后一项：Trial Holdings, Inc

![|700](attachments/Pasted%20image%2020240403132823.png)

4. 点击：子会社

![|700](attachments/Pasted%20image%2020240403132909.png)

5. 选择：Trial Company, Inc

![|700](attachments/Pasted%20image%2020240403132944.png)

6. 选择：SSC

![|700](attachments/Pasted%20image%2020240403133033.png)

7. 进入后，选择 `0027 - 新宮テスト環境` 环境、`Android` 系统，输入车号，点击搜索

![](attachments/Pasted%20image%2020240403133129.png)

8. 搜索到结果后，点击：タウンロード

![|700](attachments/Pasted%20image%2020240403133622.png)

9. 选择日期，然后选择 `デバッグ` ，点击下载即可操作ログ

![|700](attachments/Pasted%20image%2020240403133811.png)

#### Ⅱ、op log

1. 在上面的第 9 步中， 选择日期，然后选择 `操作ログ` ，点击下载即可

### ③、在 firebase 中获取

#### Ⅰ、debug log

1. 进入 firebase 上的购物车项目：https://console.firebase.google.com/u/1/project/ssc-raicart-android-develop
2. 点击右侧 storage

![|700](attachments/Pasted%20image%2020240403112344.png)

3. 然后依次选择：`debugLogs/ -> 1 -> 1 -> 3 -> 1041`
4. 下载指定日期的日志即可

#### Ⅱ、op log

1. 进入 firebase 上的购物车项目：https://console.firebase.google.com/u/1/project/ssc-raicart-android-develop
2. 点击右侧 storage
3. 然后依次选择：`operationLogs/ -> 1 -> 1 -> 3 -> 1041`
4. 下载指定日期的日志即可

## 4、开启设备 adb 

> 确认设备安装的 app 版本高于等于 3.9

1. 进入 melopan 的 SSC 中：https://sandbox-console.raicart.io/

![|800](attachments/Pasted%20image%2020230911160354.png)

2. 点击对应购物车的 `Enable ADB` 按钮

![|675](attachments/Pasted%20image%2020230911160507.png)

3. 修改弹窗中的 `Duration`，值为开启 `ADB` 功能的时间

![|700](attachments/Pasted%20image%2020230911162443.png)

4. 点击弹出的弹窗中的 `Enable` 按钮

![|700](attachments/Pasted%20image%2020230911160548.png)

5. 等待完成，变为 `disable ADB` 即为完成

![|725](attachments/Pasted%20image%2020230911160658.png)

## 5、sct 无法进入的解决办法

1. 卸载 `MicrosoftEdgeWebView2RuntimeInstallerX64` 然后重新安装
2. 若是无法卸载，则进入远程桌面：
3. 连接地址：`172.20.3.11:33896`，`administrator`、`admin1234`
4. 连接地址：`172.20.3.11:33892`，`administrator`、`admin1234`

## 6、1041 melopan 自动升级配置

1. 进入 melopan 的 SSC 中：https://sandbox-console.raicart.io/
2. 点击：デプロイ（部署）

![|700](attachments/Pasted%20image%2020240403134755.png)

3. 点击：新規作成

![|700](attachments/Pasted%20image%2020240403135030.png)

4. 进入页面后：
	1. 选择环境：0027 - 新宮テスト環境
	2. 选择系统：Android
	3. 选择要安装的版本
	4. 选中 `デプロイ中` 立即部署
	5. 选择要安装的车号
	6. 点击 `新規作成` 实行部署，会返回部署列表

![](attachments/Pasted%20image%2020240403135137.png)

## 7、postman 调用后端接口

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

## 8、

## 9、

## 10、

# 三、项目代码


## 1、LED 灯条


```kotlin
// 开启绿灯
CartDeviceManager.get().setLight(LightStatus.ONLY_GREEN_OPEN)
// 开启黄灯
CartDeviceManager.get().setLightYellow()

// 关灯
CartDeviceManager.get().closeLight()
```

## 2、全屏 dialog 弹窗

1. 代码中加入以下代码：

```kotlin
override fun onStart() {
	super.onStart()
	super.getDialog()?.window?.let { win ->
		val attr = win.attributes
		setPadding()
		win.decorView.setPadding(paddingLeft, paddingTop, paddingRight, paddingBottom)
		attr.width = WindowManager.LayoutParams.MATCH_PARENT
		attr.height = WindowManager.LayoutParams.MATCH_PARENT
		attr.gravity = Gravity.BOTTOM
		win.attributes = attr
	}
}
```

2. `xml` 布局中使用 `RelativeLayout` 作为根布局

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <androidx.constraintlayout.widget.ConstraintLayout
        android:id="@+id/dialog_confirm_bundle_purchase"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="@dimen/dp_632"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            android:background="@color/white"
            android:orientation="horizontal">
            
            <ImageView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginStart="@dimen/dp_170"
                android:layout_marginEnd="@dimen/dp_80"
                android:layout_marginTop="@dimen/dp_133"
                android:src="@drawable/ic_bundle_poc"/>
            
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:gravity="top|start"
                android:orientation="vertical">
                
                <LinearLayout
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="@dimen/dp_70"
                    android:orientation="horizontal">
                    <ImageView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:paddingTop="@dimen/dp_10"
                        android:src="@drawable/img_blue_warm"/>
                    
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginStart="@dimen/dp_20"
                        android:gravity="start"
                        android:text="パック商品の\nお買い上げですか？"
                        android:textSize="@dimen/sp_42"
                        android:textStyle="bold" />
                </LinearLayout>
                
                <jp.retailai.raicart.view.ShadowButton
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="@dimen/dp_160"
                    app:button_shadow_distance="6dp">
                    <TextView
                        android:id="@+id/button_buy_bundle"
                        android:layout_width="491dp"
                        android:layout_height="@dimen/dp_80"
                        android:gravity="center"
                        android:text="@string/common_yes"
                        android:textSize="@dimen/sp_30"
                        android:textColor="@color/white"
                        android:textStyle="bold"
                        android:background="@drawable/bg_button_blue_radius_40"/>
                </jp.retailai.raicart.view.ShadowButton>
                
                <jp.retailai.raicart.view.ShadowButton
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="@dimen/dp_32"
                    app:button_shadow_distance="6dp">
                    <TextView
                        android:id="@+id/button_buy_single"
                        android:layout_width="491dp"
                        android:layout_height="@dimen/dp_80"
                        android:gravity="center"
                        android:text="@string/common_no"
                        android:textSize="@dimen/sp_30"
                        android:textColor="@color/white"
                        android:textStyle="bold"
                        android:background="@drawable/bg_red_dark_blue_corner_40"/>
                </jp.retailai.raicart.view.ShadowButton>
            </LinearLayout>
        </LinearLayout>
    </androidx.constraintlayout.widget.ConstraintLayout>
    
    <androidx.constraintlayout.widget.ConstraintLayout
        android:id="@+id/dialog_scan_bundle_barcode"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone">
        
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="@dimen/dp_632"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            android:background="@color/white"
            android:orientation="vertical">
            
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="@dimen/dp_45"
                android:gravity="center"
                android:orientation="horizontal">
                
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="パックのバーコードをスキャンしてください"
                    android:textSize="@dimen/sp_42"
                    android:textStyle="bold"
                    app:drawableStartCompat="@drawable/img_blue_warm"
                    android:drawablePadding="@dimen/dp_10"/>
            </LinearLayout>
            
            <ImageView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="@dimen/dp_20"
                android:layout_gravity="center"
                android:src="@drawable/ic_scan_bundle_poc"/>
        </LinearLayout>
        
        <TextView
            android:id="@+id/button_return_from_barcode_scan_to_confirm"
            android:layout_width="@dimen/dp_128"
            android:layout_height="@dimen/dp_70"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            android:layout_marginStart="@dimen/dp_44"
            android:layout_marginTop="684dp"
            android:paddingStart="@dimen/dp_21"
            android:gravity="center_vertical"
            android:text="@string/common_back"
            android:textColor="@color/white"
            android:textSize="@dimen/sp_30"
            android:textStyle="bold"
            app:drawableLeftCompat="@drawable/ic_arrow_dropleft"
            android:drawablePadding="@dimen/dp_6"
            android:background="@drawable/bg_button_blue_corner_35" />
    </androidx.constraintlayout.widget.ConstraintLayout>
    
</RelativeLayout>
```

## 3、

## 4、

## 5、

# 四、poc 笔记

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

## 2、2043 新 coupon 页

![](attachments/Pasted%20image%2020231212084307.png)

## 3、2082 积分活动 v2

1. 声音播放
	1. 【倍率增加】时，必然是【新的分类达成】了
	2. 所以【倍率增加】时播放 ooudodon
	3. 【新的分类达成】时判断是否【倍率增加】了，
		1. 【倍率增加】没增加，播放 dodon
		2. 【倍率增加】增加了，播放 ooudodon
2. 声音冲突
	1. 扫描商品
	2. 购买无条形码商品
	3. 扫描商品后弹出 coupon
	4. 
3. 【倍率增加】弹窗冲突
	1. 扫描商品弹窗：会覆盖住动画
	2. 购买无条形码商品弹窗：会覆盖住动画
	3. 扫描商品后弹出 coupon 弹窗：会覆盖住动画
4. 倍率改变动画：
	1. 声音有点提前，或者说声音有点短
	2. 鼓点的声音没有压在数字变化的点上
	3. 不知道是使动画的数字变化提前，还是让声音延后一点播放

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
















