# 一、开发工具

# 二、系统工具

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
