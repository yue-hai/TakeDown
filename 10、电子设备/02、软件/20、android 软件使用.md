# 一、开发工具

# 二、系统工具

## 1、Thanox

### ①、权限管理

#### Ⅰ、中文权限说明

#### Ⅱ、英文权限说明

1. `Read phone number` (读取电话号码)
	1. 对应权限：`android.permission.READ_PHONE_NUMBERS` (Android 8.0+)
	2. 作用：这是一个专门用于读取设备本机电话号码的权限。在 Android 8.0 之前，应用必须申请涵盖范围更广的 READ_PHONE_STATE 才能获取号码，为了隐私保护，Google将其分离出来
	3. 应用场景：
		1. 社交/通讯软件（如WhatsApp、Telegram）：在首次注册或登录时，自动读取并填入本机的手机号码，省去用户手动输入的麻烦
		2. 银行/支付应用：用于 SIM 卡绑定验证，确保操作是在绑定手机号的设备上进行的
2. `安装应用` / `请求安装应用`
	4. 对应权限：`android.permission.REQUEST_INSTALL_PACKAGES`
	5. 作用：允许应用程序安装其他的 APK 文件。这是一个高风险权限，应用不能直接获取，必须跳转到系统设置页面，由用户手动开启“允许来自此来源的应用”开关
	6. 应用场景：
		1. 第三方应用商店（如酷安、TapTap、豌豆荚）：下载完成后自动发起安装请求
		2. 浏览器（如 Chrome、Edge）：用户下载 APK 文件后点击打开进行安装
		3. 文件管理器：用户手动点击存储中的 APK 文件进行安装
3. `Picture in picture` (画中画)
	1. 对应操作：`AppOpsManager.OP_PICTURE_IN_PICTURE`
	2. 作用：允许应用在用户按下 Home 键回到桌面时，自动缩小成一个悬浮的小窗口继续播放视频，而不会中断
	3. 应用场景：
		1. 视频播放器（如Bilibili、YouTube、Netflix）：看视频时切出去回微信，视频窗口悬浮在角落继续播放
		2. 地图导航（如高德、Google Maps）：导航过程中切换到其他应用，导航路线以小窗形式显示
		3. 视频通话（如微信视频、Zoom）：通话时切换应用，对方的画面保持在小窗中
4. `Instant app start foreground` (即时应用启动前台服务)
	4. 对应操作：`AppOpsManager.OP_INSTANT_APP_START_FOREGROUND`
	5. 作用：这是一个针对 Instant Apps (Google Play 免安装应用) 的特殊权限。它允许那些用户没有真正安装、只是点击试用的“免安装应用”启动前台服务（即在通知栏显示常驻通知并运行任务）
	6. 应用场景：
		4. 试玩版游戏：用户未下载游戏，点击“试玩”时，游戏在后台下载资源的同时保持运行
		5. 临时工具：如停车缴费、临时租借充电宝的轻应用，在未完全安装的情况下保持连接状态
5. `Answer incoming phone calls` (接听来电)
	1. 对应权限：`android.permission.ANSWER_PHONE_CALLS` (Android 8.0+)
	2. 作用：允许应用通过代码编程的方式自动接听电话，而无需用户在屏幕上滑动接听
	3. 应用场景
		1. 智能穿戴配套应用：用户点击手表或手环上的“接听”按钮，手机自动接通电话
		2. 车载系统/蓝牙助手：驾驶模式下，通过语音指令“接听电话”，APP 自动执行接听操作
		3. 盲人辅助工具：特定的辅助功能应用帮助视障人士通过物理按键或手势快速接听
6. `在后台运行任务`
	4. 对应操作：`AppOpsManager.OP_RUN_IN_BACKGROUND` 或 `OP_RUN_ANY_IN_BACKGROUND`
	5. 作用：这是一个非常核心的底层控制项，通常被称为 “后台运行权限”。如果禁止此项，应用在切入后台（不可见）一段时间后，其所有的后台服务、定时任务和同步机制都会被系统强制停止
	6. 应用场景：
		4. 即时通讯（IM）（微信、QQ）：必须允许，否则切到后台或锁屏后无法接收新消息
		5. 下载工具（迅雷）：需要此权限在后台继续下载大文件
		6. 毒瘤/广告应用：建议拒绝，防止它们在后台偷偷耗电、跑流量或弹窗
7. `更改 Wifi 连接状态`
	1. 对应权限：`android.permission.CHANGE_WIFI_STATE`
	2. 作用：允许应用开启或关闭 Wi-Fi、连接到指定的 Wi-Fi 热点、或者断开当前连接。请注意，这不同于“获取位置”权限，它主要侧重于对开关和连接的控制
	3. 应用场景：
		1. 智能家居配网（如米家、涂鸦智能）：在添加新设备时，APP 需要自动切换连接到设备的临时热点进行配置
		2. 文件快传（如快牙、茄子快传）：自动建立并连接热点以进行点对点传输
		3. 系统工具：一键开关 Wi-Fi 的小部件
8. `Request package deletion through package installer`(请求通过软件包安装程序删除软件包)
	4. 对应权限：`android.permission.REQUEST_DELETE_PACKAGES`
	5. 作用：允许应用程序请求卸载设备上的其他应用。调用此权限后，系统会弹出标准的卸载确认对话框，需要用户手动确认后才能完成卸载
	6. 应用场景：
		4. 应用商店：用户在商店内点击“卸载”某个已安装应用
		5. 清理类工具：扫描出长期不用的 App 后，提供一键卸载功能（实际还是会逐个弹窗确认）
		6. 桌面启动器：长按桌面图标，选择“卸载”
9. `Bind an accessibility service` (绑定无障碍服务)
	1. 对应权限：`android.permission.BIND_ACCESSIBILITY_SERVICE`
	2. 作用：这是授予“无障碍服务”（辅助功能）的权限。拥有此权限的应用可以读取屏幕上的所有内容、模拟用户的点击、滑动等操作。它主要用于帮助有障碍的用户使用手机，但也常被一些自动化工具或增强功能应用（如密码管理器、自动化脚本）使用。这是一个非常强大的权限，需要用户在系统设置中手动开启
	3. 应用场景：
		1. 跳过广告工具（如李跳跳）：识别屏幕上的“跳过”字样并自动点击
		2. 密码管理器（如Bitwarden）：识别输入框并自动填充账号密码
		3. 自动化工具（如Tasker）：执行复杂的自动化脚本
		4. 视障辅助（如TalkBack）：朗读屏幕内容
10. `Any app start foreground service` (任何应用启动前台服务)
	4. 对应权限：`android.permission.FOREGROUND_SERVICE`
	5. 作用：允许应用创建“前台服务”。前台服务会在系统通知栏显示一个持续的通知，用于执行用户明确知道正在进行的操作（如音乐播放、导航、文件下载）。即使用户切换到其他应用，该服务也会继续运行，不容易被系统杀死
	6. 应用场景：
		1. 音乐/播客应用：后台播放时，通知栏显示播放控制条
		2. 运动健康（如Keep）：记录跑步轨迹时，锁屏后继续记录 GPS 位置
		3. 文件传输：后台上传或下载文件时显示进度条
11. `Blue tooth scan` (蓝牙扫描)
	1. 对应权限：`android.permission.BLUETOOTH_SCAN` (Android 12+)
	2. 作用：专门用于扫描附近的蓝牙设备。在旧版本安卓中，蓝牙扫描需要位置权限，为了加强隐私保护，新版本将其分离为独立权限
	3. 应用场景：
		1. 寻找丢失设备：扫描附近的蓝牙防丢器（如AirTag、Tile）
		2. 智能家居列表：打开App时扫描周围可用的智能灯泡或插座
		3. 室内定位：商场 App 通过扫描蓝牙信标（Beacon）进行室内导航
12. `Use BiometricPrompt` (使用生物识别)
	4. 对应权限：`android.permission.USE_BIOMETRIC`
	5. 作用：允许应用使用设备的生物识别硬件（如指纹、面部识别）来验证用户身份。常用于应用登录、支付确认等安全场景
	6. 应用场景：
		4. 金融/银行 App：登录账户或转账时验证指纹
		5. 应用锁：打开加密相册或笔记时需要指纹解锁
		6. 购物 App：免密支付确认
13. `Physical activity recognition` (身体活动识别)
	1. 对应权限：`android.permission.ACTIVITY_RECOGNITION`
	2. 作用：允许应用检测用户的身体活动状态，例如走路、跑步、骑行或驾车。这通常被健康、运动或地图类应用用来追踪用户活动
	3. 应用场景：
		1. 计步器（如微信运动）：不开启 GPS 也能计算步数
		2. 健身 App：自动识别用户开始跑步并开始记录
		3. 地图导航：判断用户是在步行还是驾车，以切换导航模式
14. `Financial app sms read` (读取短信)
	4. 对应权限：`android.permission.READ_SMS`
	5. 作用：允许应用读取设备上的所有短信内容。虽然这里标注为“金融类”，但实际权限是读取所有短信。谷歌对短信和通话记录权限有严格的政策，通常只有默认短信应用或特定类型的金融应用（如记账）才被允许使用
	6. 应用场景：
		4. 验证码自动填充：旧版本 App 常用，现在多用专用 API，但部分 App 仍用此权限读取验证码
		5. 记账软件：读取银行扣款短信，自动生成账单记录
		6. 垃圾短信拦截：安全软件读取短信内容以识别诈骗或骚扰信息
15. `Read/Write` `media of audio/video/image type` (读/写 音频/视频/图片 类型的媒体)
	1. 对应权限：`READ_MEDIA_AUDIO`、`READ_MEDIA_VIDEO`、`READ_MEDIA_IMAGES` (Android 13+)
	2. 作用：这是谷歌推出的“分区存储”策略下的细分媒体权限。应用不再需要请求宽泛的存储权限，而是可以根据需要分别请求对音频、视频或图片文件的访问权限，从而更好地保护用户隐私。写入媒体文件通常不需要特定权限，应用可以通过 MediaStore API 将自己的媒体文件保存到公共集合中
	3. 应用场景：
		1. 社交软件：发朋友圈时选择照片（请求图片权限）
		2. 视频剪辑软件：导入本地视频素材（请求视频权限）
		3. 音乐播放器：扫描本地歌曲文件（请求音频权限）
16. `使用辅助功能`
	4. 应用场景: 同第 9 条。常见于自动化点击、抢红包插件、自动安装器等
17. `读取设备信息 (IMEI / MEID, IMSI, SIM / Build serial)`
	1. 对应权限：`android.permission.READ_PHONE_STATE`
	2. 作用：允许应用访问设备的电话状态，包括设备ID（如IMEI）、SIM卡信息、网络信息以及通话状态。由于这些信息是持久且唯一的设备标识符，此权限被认为是敏感的
	3. 应用场景：
		1. 风控与安全：银行或游戏 App 判断是否是同一台设备登录，防止盗号或作弊
		2. 来电显示：检测是否有电话呼入，以便暂停音乐播放
		3. 运营商 App：读取 SIM 卡信息以免密登录
18. `Access media location` (访问媒体位置信息)
	4. 对应权限：`android.permission.ACCESS_MEDIA_LOCATION`
	5. 作用：允许应用读取存储在图片或视频文件中的地理位置信息（EXIF 数据）。即使应用有了读取图片的权限，也需要这个独立的权限才能获取照片的拍摄地点
	6. 应用场景：
		4. 相册 App：在“地图相册”功能中，将照片展示在地图对应的拍摄位置上
		5. 社交分享：上传原图时，App 读取照片拍摄地并建议“打卡”地点
19. `Query all packages` (查询所有软件包)
	1. 对应权限：`android.permission.QUERY_ALL_PACKAGES` (Android 11+)
	2. 作用：允许应用获取设备上安装的所有应用的列表。出于隐私考虑，此权限的使用受到 Google Play 政策的严格限制，只有少数类型的应用（如启动器、文件管理器、杀毒软件）才有资格申请
	3. 应用场景：
		1. 应用管理/杀毒软件：扫描手机里的病毒或垃圾应用
		2. 换机助手：读取应用列表以便同步到新手机
		3. 第三方启动器（Launcher）：需要列出所有应用图标供用户点击
20. `Access all external storage` (访问所有外部存储文件)
	4. 对应权限：`android.permission.MANAGE_EXTERNAL_STORAGE` (Android 11+)
	5. 作用：授予应用对外部共享存储（包括所有文件和文件夹）的完整读写访问权限。这是一个非常强大的权限，同样受到 Google Play 政策的严格限制，主要用于文件管理器、备份和恢复类应用
	6. 应用场景：
		4. 文件管理器（如ES文件浏览器）：管理、复制、删除任意文件
		5. 备份工具（如钛备份）：备份应用数据和文件
		6. 解压缩工具：解压文件到任意目录
21. `Loader usage stats` (应用使用情况统计)
	1. 对应权限：`android.permission.PACKAGE_USAGE_STATS`
	2. 作用：允许应用收集其他应用的使用情况数据，例如应用打开次数、使用时长等。这需要用户在系统设置中为应用单独授权
	3. 应用场景：
		1. 屏幕时间管理（如Digital Wellbeing）：统计你每天刷了多久抖音
		2. 省电/清理软件（如Greenify）：判断某个应用很久没用了，建议休眠或卸载
		3. 智能调度：根据用户习惯预加载常用应用
22. `MANAGE_ONGOING_CALLS` (管理正在进行的通话)
	4. 对应权限：`android.permission.MANAGE_ONGOING_CALLS`
	5. 作用：允许应用管理电话通话，例如查看通话信息或挂断电话。通常由默认电话应用或 VoIP 应用使用
	6. 应用场景：
		4. 智能手环 App：在手环上显示来电号码，并提供挂断按钮
		5. 驾驶模式 App：监控通话状态，驾驶时自动拒接或回复短信
23. `MANAGE_CREDENTIALS`、`USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER`、`RECORD_AUDIO_OUTPUT`、`MANAGE_MEDIA`
	1. 这些都是非常特殊或非公开的系统级权限，普通第三方应用通常无法获取或使用。它们分别用于凭据管理、运营商身份验证、系统音频录制和媒体管理中心等底层功能
	2. 应用场景：
		1. 系统设置：管理信任的证书、连接 VPN
		2. 运营商服务：SIM卡鉴权
		3. 录屏软件：RECORD_AUDIO_OUTPUT 用于内录系统声音（Android 10+）
24. `SCHEDULE_EXACT_ALARM` (设置精确闹钟)
	1. 对应权限：`android.permission.SCHEDULE_EXACT_ALARM` (Android 12+)
	2. 作用：允许应用设置需要在精确时间触发的闹钟或提醒。由于精确闹钟会消耗更多电量并可能被滥用，系统对其进行了限制，需要用户单独授权
	3. 应用场景：
		1. 闹钟 App：确保早上 7:00 准时响铃，而不是 7:05
		2. 日历/提醒事项：会议开始前的准时提醒
		3. 抢购脚本：需要在特定秒数触发操作
25. `BLUETOOTH_CONNECT` (蓝牙连接)
	1. 对应权限：`android.permission.BLUETOOTH_CONNECT` (Android 12+)
	2. 作用：允许应用连接到已配对的蓝牙设备，例如连接蓝牙耳机或音箱
	3. 应用场景：
		1. 蓝牙耳机 App：调节耳机的降噪模式或查看电量
		2. 智能手表同步：传输步数数据或推送通知到手表
26. `BLUETOOTH_ADVERTISE` (蓝牙广播)
	4. 对应权限：`android.permission.BLUETOOTH_ADVERTISE` (Android 12+)
	5. 作用：允许应用向附近的蓝牙设备进行广播，让其他设备可以发现自己
	6. 应用场景：
		1. 接触者追踪（特定时期）：手机不断广播随机 ID 以记录接触历史
		2. 近距离文件分享：让周围设备能搜到你以便发送文件
		3. 充当外设：用手机模拟蓝牙键盘或鼠标控制电脑
27. `RECORD_INCOMING_PHONE_AUDIO` (录制来电音频)
	1. 对应权限：这不是一个标准的公开 Android SDK 权限。它可能是特定设备制造商（OEM）定制的系统级权限，或者是在某些特殊场景下使用的内部权限。对于普通第三方应用来说，无法直接请求此权限来录制通话音频
28. `NEARBY_WIFI_DEVICES` (附近的 WLAN 设备)
	2. 对应权限：`android.permission.NEARBY_WIFI_DEVICES` (Android 12+)
	3. 作用：允许应用通过 Wi-Fi 发现并连接到附近的设备，而无需获取位置权限。这对于物联网(IoT)设备配网、文件快传等场景非常有用
	4. 应用场景：
		1. 打印机 App：搜索局域网内的打印机
		2. 投屏软件：搜索附近的电视或投影仪进行投屏
		3. 智能家居：通过 Wi-Fi Direct 配置新设备
29. `ACCESS_RESTRICTED_SETTINGS` (访问受限制的设置)
	1. 对应权限：`android.permission.ACCESS_RESTRICTED_SETTINGS`
	2. 作用：一个非常敏感的系统级权限。它允许应用更改一些被系统保护的、用户无法轻易修改的设置项，以防止关键功能被禁用。通常只有系统应用或设备管理类应用才能获得此权限
	3. 应用场景：
		1. 辅助功能服务开启：Android 13+ 对侧载（手动安装）的应用限制开启辅助功能，需要此权限“解除限制”
		2. 企业设备管理：公司配发的手机，禁止员工修改锁屏时间或密码设置


## 2、


# 三、网络通信


## 1、钉钉

### ①、获取组织 id：corpId

#### Ⅰ、获取原因

1. 绕过多租户 UI 阻塞：当账号挂载了多个企业主体（如总公司、分公司）时，通过常规的 Deep Link 唤起考勤 H5 容器，网关拦截器因缺少上下文会抛出 UI 阻塞，强制要求手动选择下拉列表
2. 通过显式携带 corpId 参数，可以直接绕过该弹窗，直达打卡指纹页面，这也是无感自动化的先决条件

#### Ⅱ、前置工具要求

1. 拥有 Root 管理权限（Magisk / KernelSU）。
2. 终端模拟器（推荐 Termux），用于执行底层 Logcat 嗅探

#### Ⅲ、获取步骤

1. 打开 Termux，进入 Root 模式并刷新掉庞大的历史系统日志池，避免读取时的噪音干扰

```shell
su
logcat -c
```

1. 在 Termux 中执行以下命令，开启正则过滤并监听 V8 引擎创建 JS Context 时的日志路由记录：

```shell
logcat | grep -iE "corpid=ding[a-zA-Z0-9]+"
```

1. 将 Termux 保持后台运行，返回桌面并打开钉钉
2. 走一遍完整的手动打卡流程：主界面 -> 工作台 -> 考勤打卡 -> 弹窗中选择要打卡的特定公司 -> 页面完全加载完毕
3. 切回 Termux，终止日志监听（Ctrl + C，或者直接看屏幕输出），终端内应该已捕获到类似如下的日志：

```shell
url: https://XXX.com/index.html#pages/home/index?XXX&corpId=dingda973a41gneodk22r6qfd3l5ga4s3dy6
```


1. 其中 `corpId=` 后面的 `dingda973a41gneodk22r6qfd3l5ga4s3dy6` 就是 组织 id


### ②、


## 2、


# 四、论坛博客

# 五、文件相关

# 六、自动脚本

## 1、Tasker

### ①、钉钉自动打卡（打开打卡页面）

#### Ⅰ、创建任务：上下班打卡

##### （1）、点亮屏幕

1. 添加动作 -> 代码 -> 运行 shell 脚本
2. 命令：

```shell
input keyevent 224
```

3. 勾选：使用 root

![|184](attachments/Pasted%20image%2020260702123451.png)

##### （2）、判断是否是工作日

1. 添加动作 -> 网络 -> `HTTP Request`
	1. 方法：`GET`
	2. URL：`https://timor.tech/api/holiday/info/`
	3. 返回值说明：
		1. 工作日（上班）：0
		2. 周末：1
		3. 节日：2
		4. 调休（上班）：3
	4. 接口的返回值会保存在全局变量中，比如：`%http_response_code`：响应代码，`%http_data`：响应体数据

```json
{
    "code": 0,
    "type": {
        "type": 0,
        "name": "周五",
        "week": 5
    },
    "holiday": null
}
```

2. 添加动作 -> 任务 -> 停止 -> 添加 if 条件：
	1. `%http_data[type.type]` = 1
	2. `%http_data[type.type]` = 2
	3. 表示 返回的 `type.type` 字段的值如果是 1 周末、2节日 则直接停止任务，不再打开蓝牙、定位、钉钉打卡页面

![|325](attachments/Pasted%20image%2020260529162308.png)

##### （3）、开启蓝牙、定位

1. 添加动作 -> 网络 -> 蓝牙 -> 设置：开
2. 添加动作 -> 位置 -> 定位模式 -> 模式：省电

![|325](attachments/Pasted%20image%2020260529150742.png)

##### ~~（4）、打开钉钉打卡页面（发送意图）~~

> 弃用此方式，有时会无法启动钉钉，更换为下面的 shell 脚本的方式

1. 添加动作 -> 系统 -> 发送意图
2. 操作：`android.intent.action.VIEW`
3. 数据：使用提取到的 corpId 拼凑以下链接：

```shell
dingtalk://dingtalkclient/page/link?url=https://attend.dingtalk.com/attend/index.html?corpId=dingda973a41gneodk22r6qfd3l5ga4s3dy6

# 若失败可以尝试替换为转义符：%3F 替换 ?，%3D 替换 =
dingtalk://dingtalkclient/page/link%3Furl=https://attend.dingtalk.com/attend/index.html%3FcorpId%3Ddingda973a41gneodk22r6qfd3l5ga4s3dy6
```

4. 目标：`Activity`

![|177](attachments/Pasted%20image%2020260529151917.png)

##### （4）、打开钉钉打卡页面（shell 脚本）

1. 添加动作 -> 代码 -> 运行 shell 脚本
2. 命令：

```shell
# 1. 使用包名动态寻址启动钉钉官方主页
am start $(cmd package resolve-activity --brief -c android.intent.category.LAUNCHER com.alibaba.android.rimet | tail -n 1)

# 2. 等待钉钉 5 秒完成冷启动初始化
sleep 5

# 3. 通过 Deep Link 打开考勤指纹页
am start -a android.intent.action.VIEW -d 'dingtalk://dingtalkclient/page/link?url=https://attend.dingtalk.com/attend/index.html%3FcorpId%3Ddingda973a41gneodk22r6qfd3l5ga4s3dy6'
```

3. 勾选：使用 root

![|234](attachments/Pasted%20image%2020260702124548.png)

##### （5）、全部任务列表：

![|184](attachments/Pasted%20image%2020260529162506.png)

#### Ⅱ、创建配置文件：上班打卡、下班打卡

1. 创建配置 -> 时间 -> 上班前2几分钟 至 上班
2. 创建配置 -> 状态 -> 电话 -> 周边基站 -> 在公司点击扫描 录入附近基站

![|450](attachments/Pasted%20image%2020260529163225.png)

![|209](attachments/Pasted%20image%2020260529163316.png)

### ②、


# 十、媒体娱乐

# 十一、生活消费

# 十二、生产力工具

# 二十、软件商店

# 二十一、自部署服务

# 90、谷歌商店软件

# 九十九、其他软件
