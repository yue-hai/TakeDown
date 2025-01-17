
# 一、`Android` 初识

## 1、App 的开发特点

### ①、App 的运行环境

1. Android App 必须在 Android 系统上运行，虽然 Android 系统基于 Linux 内核，但不等于 Linux 系统，故 App 应用无法在 Linux 系统上运行。
2. 要想观察 App 的运行效果，有下列两种办法：
	1. 在模拟器上运行 App 应用；
	2. 使用真实手机调试 App；

### ②、App 的开发语言

1. App 开发主要有两大技术路线，分别是原生开发和混合开发。
2. 原生开发指的是在移动平台上利用官方提供的编程语言、开发工具包、开发环境进行 App 开发；
3. 混合开发指的是结合原生与 H5 技术开发混合应用，也就是将部分 App 页面改成内嵌的网页。
4. Android 的官方编程语言包括 Java 和 Kotlin，此外还有界面布局需要的 XML。

### ③、App 连接的数据库

1. Android 内置了专门的数据库名叫 SQLite，它遵循关系数据库的设计理念，SQL 语法类似于 MySQL。
2. SQLite 无需单独安装，因为它内嵌到应用进程当中，所以 App 无需配置连接信息，即可直接对其增删改查。
3. 由于 SQLite 嵌入到应用程序，省去了配置数据库服务器的开销，因此它又被归类为嵌入式数据库。
4. 客户端与服务端分别操作的数据库

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515133844.png)

5. 客户端与服务端的多对一架构关系

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515133857.png)

## 2、App 的工程结构

### ①、App工程目录结构

1. App 工程分为两个层次，第一个层次是项目，另一个层次是模块。
2. 模块依附于项目，每个项目至少有一个模块，也能拥有多个模块。
3. 一般所言的“编译运行 App”，指的是运行某个模块，而非运行某个项目，因为模块才对应实际的 App。
4. App 项目下面有两个分类：app（代表 app 模块）、Gradle Scripts。
5. app 下面又有 3 个子目录，功能说明如下：
	1. manifests 子目录，存放 AndroidManifest.xml，它是 App 的运行配置文件。
	2. java 子目录，存放当前模块的 Java 源代码。
	3. res 子目录，存放当前模块的资源文件。
6. Gradle Scripts下面主要是工程的编译配置文件：
	1. build.gradle，该文件分为项目级与模块级两种，用于描述App工程的编译规则。
	2. proguard-rules.pro，该文件描述了 Java 代码的混淆规则。
	3. gradle.properties，该文件配置了编译工程的命令行参数，一般无须改动。
	4. settings.gradle，该文件配置了需要编译哪些模块，以及依赖库的仓库地址。
	5. local.properties，它是项目的本地配置文件。

![|486](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515134558.png)

### ②、编译配置文件 build.gradle

1. App 项目的 build.gradle 分为两个级别，一个是 Project 项目级别的 build.gradle，另一个是 Module 模块级别的 build.gradle。
2. 项目级别的 build.gradle 指定了当前项目的总体编译规则。（注意：从Android Studio Bumblebee 开始，仓库地址配到了 settings.gradle）
3. 模块级别的 build.gradle 对应于具体模块，每个模块都有自己的 build.gradle，它指定了当前模块的详细编译规则。
4. gradle 文件采用了 Gradle 工具完成编译构建操作，每个版本的 Android Studio 都有对应的 Gradle 版本。只有二者的版本正确对应，工程才能被正确的编译

![|227](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515135631.png)

5. app 模块的 build.gradle

```Kotlin
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    namespace 'com.yuehai.android'
    // 指定编译用的 SDK 版木号。比如 33 表示使用 Android 13.0 编译
    compileSdk 33

    defaultConfig {
        // 指定该模块的应用编号,也就是 App 的包名
        applicationId "com.yuehai.android"
        // 指定 app 适合运行的最小 SDK 版本号。比如 19 表示至少要在 Android 4.4 上运行
        minSdk 28
        // 指定目标设备的 SDK 版本号。表示 App 最希望在哪个版本的 Android 上运行
        targetSdk 33
        // 指定 App 的应用版本号
        versionCode 1
        // 指定 App 的应用版本名称
        versionName "1.0"

        // 单元测试
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"

    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = '1.8'
    }
    buildFeatures {
        viewBinding true
    }
}

// 依赖
dependencies {

    implementation 'androidx.core:core-ktx:1.8.0'
    implementation 'androidx.appcompat:appcompat:1.4.1'
    implementation 'com.google.android.material:material:1.5.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.3'
    implementation 'androidx.lifecycle:lifecycle-livedata-ktx:2.4.1'
    implementation 'androidx.lifecycle:lifecycle-viewmodel-ktx:2.4.1'
    implementation 'androidx.navigation:navigation-fragment-ktx:2.5.2'
    implementation 'androidx.navigation:navigation-ui-ktx:2.5.2'
    testImplementation 'junit:junit:4.13.2'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
}
```

6. settings.gradle 中配置仓库地址


```Kotlin
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
        // 以下四行添加阿里云的仓库地址，方便国内开发者下载相关插件
        maven { url 'https://maven.aliyun.com/repository/jcenter' }
        maven { url 'https://maven.aliyun.com/repository/google'}
        maven { url 'https://maven.aliyun.com/repository/gradle-plugin'}
        maven { url 'https://maven.aliyun.com/repository/public'}
        // 以下添加华为的仓库地址，引入HMS需要
        maven { url 'https://developer.huawei.com/repo/'}
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        // 以下四行添加阿里云的仓库地址，方便国内开发者下载相关插件
        maven { url 'https://maven.aliyun.com/repository/jcenter' }
        maven { url 'https://maven.aliyun.com/repository/google'}
        maven { url 'https://maven.aliyun.com/repository/gradle-plugin'}
        maven { url 'https://maven.aliyun.com/repository/public'}
        // 以下添加华为的仓库地址，引入HMS需要
        maven { url 'https://developer.huawei.com/repo/'}
    }
}
rootProject.name = "02_Android"
include ':app'
include ':01_simplecontrol'
include ':04_sharedpreferences'
include ':05_contentproviderserver'
include ':05_contentproviderclinet'
include ':06_broadcast'
include ':07_service'
include ':08_http'
include ':03_advancedcontrols'
```

### ③、运行配置清单文件 AndroidManifest.xml

1. AndroidManifest.xml 指定了 App 的运行配置信息，它的根节点为 `manifest`，package 属性指定了该 App 的包名。
2. manifest 下面有个 `application` 节点，它的各属性说明如下：
	1. android:allowBackup，是否允许应用备份。为 true 表示允许，为 false 表示不允许。
	2. android:icon，指定 App 在手机屏幕上显示的图标。
	3. android:label，指定 App 在手机屏幕上显示的名称。
	4. android:supportsRtl，是否支持从右往左的文字排列顺序。
	5. android:theme，指定 App 的显示风格。
3. `application` 节点下面还有个 `activity` 节点，他是活动页面的注册声明，只有在其中正确配置了 `activity` 节点，才能在运行时访问对应的活动页面。

![|296](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417125817.png)

```Kotlin
<?xml version="1.0" encoding="utf-8"?>
<!--
    xmlns:android：命名空间
    package：包名
    android:versionCode="1"：内部版本号
    android:versionName="1.0"：用户可见的版本号
-->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!--
        android:allowBackup，是否允许应用备份。
            允许用户备份系统应用和第三方应用的 apk 安装包和应用数据，以便在刷机或者数据丢失后恢复应用，用户即可通过 adb backup 和 adb restore 来进行对应用数据的备份和恢复。
            为 true 表示允许，为 false 则表示不允许
        android:icon，指定 App 在手机屏幕上显示的图标。
        android:label，指定 App 在手机屏幕上显示的名称。
        android:roundIcon，指定 App 的圆角图标。
        android:supportsRtl，是否支持 阿拉伯语/波斯语 这种从右往左的文字排列顺序。为 true 表示支持，为 false 则表示不支持。
        android:theme，指定 App 的显示风格。
     -->
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.02_Android"

        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        tools:targetApi="31">

        <!--
            1、Activity 是一个应用程序组件，提供一个屏幕（窗口），，它提供屏幕进行交互,用户可以用来交互为了完成某项任务。
            2、每个 Activity 都会获得一个用于绘制其用户界面的窗口，窗口可以充满哦屏幕也可以小于屏幕并浮动在其他窗口之上
            3、一个应用通常是由多个彼此松散联系的 Activity 组成，一般会指定应用中的某个 Activity 为主活动，也就是说首次启动应用时给用户呈现的 Activity。

            android:name=".MainActivity"：打开应用时首先看到的是哪个窗口
         -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

## 3、App 的设计规范

### ①、界面设计与代码逻辑

1. 页面布局与逻辑代码分离

![|684](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515141621.png)

2. 把 App 的界面设计与代码逻辑分开，不仅参考了网站的 WEB 前后端分离，还有下列几点好处。
	1. 使用 XML 文件描述 APP 界面，可以很方便地在 Android Studio 上预览界面效果。
	2. 一个界面布局可以被多处代码复用。
	3. 反过来，一个 Java 代码也可能适配多个界面布局。
3. `res/layout` 默认存放的是竖屏的布局文件
4. 若想增加横屏时的布局样式，需创建 `res/layout-land` 目录，在其中创建和 `res/layout` 中心相通文件名的文件
5. 利用 `XML` 标记描绘应用界面，使用 `JAVA（Kotlin）` 代码书写程序逻辑

![|386](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417130212.png)

### ②、利用 XML 标记描绘应用界面

1. 凡是 XML 标签都由标签头与标签尾组成，标签头以左右尖括号包括标签名称，形如 `<TextView>`；标签尾在左尖括号后面插入斜杆，以此同标签头区分开，形如 `</TextView>`。
2. 标签头允许在标签名称后面添加各种属性取值，而标签尾不允许添加任何属性

![|407](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417140616.png)


```Kotlin
<?xml version="1.0" encoding="utf-8"?>
<!--
    最外层；LinearLayout：线性布局
    xmlns:android="http://schemas.android.com/apk/res/android"：命名空间
    android:layout_width="match_parent"：宽，match_parent：填充父空间，即 100% 屏幕大小
    android:layout_height="match_parent"：高
    android:orientation="vertical"：线性布局（纵向）
    android:gravity="center"：居中
 -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center">

    <!--
        TextView：文本框
        android:id="@+id/yuehai_text"：设置 id，以便于调用
        android:layout_width="wrap_content"：宽，wrap_content：根据内容大小改变宽度
        android:layout_height="wrap_content"：高
        android:text="文本框"：文本框显示文字
     -->
    <TextView
        android:id="@+id/yuehai_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="文本框"
        />

</LinearLayout>
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417140651.png)

### ③、使用Java代码书写程序逻辑

1. XML 标签表达不了复杂的业务逻辑，只能由 App 后台的 Java 代码来处理。

```Kotlin
package com.yuehai.android

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 设置内容视图；当前的组件显示哪个视图（窗口）
        // R 就是 res 包
        setContentView(R.layout.activity_main)

        // 使用 id 修改属性；修改文本框显示文字
        // 传入的泛型为 xml 中的标签名，即组件类型
        val textView = findViewById<TextView>(R.id.yuehai_text)
        // 修改文本框显示文字
        textView.text = "修改文本框"
    }
}
```

## 4、App 的活动页面，`activity` 窗口的创建和跳转

### ①、创建新的 App 页面

1. 在 `layout` 下创建一个窗口文件 `yuehai.xml`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417143741.png)

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    最外层；LinearLayout：线性布局
    xmlns:android="http://schemas.android.com/apk/res/android"：命名空间
    android:layout_width="match_parent"：宽，match_parent：填充父空间，即 100% 屏幕大小
    android:layout_height="match_parent"：高
    android:orientation="vertical"：线性布局（纵向）
    android:gravity="center"：居中
 -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center">

    <!--
        TextView：文本框
        android:id="@+id/yuehai_text"：设置 id，以便于调用
        android:layout_width="wrap_content"：宽，wrap_content：根据内容大小改变宽度
        android:layout_height="wrap_content"：高
        android:text="@string/yuehai"：文本框显示文字
            @string/yuehai：引用 values 下的 strings.xml 中的 name 为 yuehai 的内容
     -->
    <TextView
        android:id="@+id/yuehai_text2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/yuehai"
        />

</LinearLayout>
```

2. 在 `res/values/strings.xml` 处定义的数据可在别处进行引用

![|331](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417164008.png)

```xml
<resources>
    <string name="app_name">02_Android</string>
    <string name="title_home">Home</string>
    <string name="title_dashboard">Dashboard</string>
    <string name="title_notifications">Notifications</string>
    <!-- 在此处定义的数据可在别处进行引用 -->
    <string name="yuehai">月海</string>
</resources>
```

3. 在 `AndroidManifest.xml` 清单文件中进行注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    xmlns:android：命名空间
    package：包名
    android:versionCode="1"：内部版本号
    android:versionName="1.0"：用户可见的版本号
-->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!--
        android:allowBackup，是否允许应用备份。
            允许用户备份系统应用和第三方应用的 apk 安装包和应用数据，以便在刷机或者数据丢失后恢复应用，用户即可通过 adb backup 和 adb restore 来进行对应用数据的备份和恢复。
            为 true 表示允许，为 false 则表示不允许
        android:icon，指定 App 在手机屏幕上显示的图标。
        android:label，指定 App 在手机屏幕上显示的名称。
        android:roundIcon，指定 App 的圆角图标。
        android:supportsRtl，是否支持 阿拉伯语/波斯语 这种从右往左的文字排列顺序。为 true 表示支持，为 false 则表示不支持。
        android:theme，指定 App 的显示风格。
     -->
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.02_Android"

        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        tools:targetApi="31">

        <!--
            1、Activity 是一个应用程序组件，提供一个屏幕（窗口），，它提供屏幕进行交互,用户可以用来交互为了完成某项任务。
            2、每个 Activity 都会获得一个用于绘制其用户界面的窗口，窗口可以充满哦屏幕也可以小于屏幕并浮动在其他窗口之上
            3、一个应用通常是由多个彼此松散联系的 Activity 组成，一般会指定应用中的某个 Activity 为主活动，也就是说首次启动应用时给用户呈现的 Activity。

            android:name=".MainActivity"：打开应用时首先看到的是哪个窗口
         -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <!-- 注册新窗口 -->
        <activity android:name=".Yuehai">
            <!-- 不是主窗口，所以不用配置 intent-filter -->
        </activity>
    </application>

</manifest>
```

4. 创建 `java/com/yuehai/android/Yuehai.kt` 文件，定义窗口的逻辑

```Kotlin
package com.yuehai.android

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

// 继承 AppCompatActivity()
class Yuehai : AppCompatActivity() {
    // 重写 onCreate(savedInstanceState: Bundle?) 方法
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.yuehai)
    }

}
```

### ②、跳到另一个页面

1. 出发页面为 `activity_main.xml`，到达页面为 `yuehai.xml`，那么跳转动作是从 `activity_main.xml` 跳转到 `yuehai.xml`，跳转代码便是下面这样的：

```Kotlin
// 活动页面跳转，从 activity_main.xml 跳到 yuehai.xml
startActivity(Intent(this, Yuehai().javaClass));
```

2. 因为跳转动作通常发生在当前页面，也就是从当前页面跳到其他页面，所以不产生歧义的话，可以使用 this 指代当前页面。
3. 为了可以在 `activity_main` 中跳转到这个窗口，需要在 `activity_main.xml` 窗口中增加一个按钮

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    最外层；LinearLayout：线性布局
    xmlns:android="http://schemas.android.com/apk/res/android"：命名空间
    android:layout_width="match_parent"：宽，match_parent：填充父空间，即 100% 屏幕大小
    android:layout_height="match_parent"：高
    android:orientation="vertical"：线性布局（纵向）
    android:gravity="center"：居中
 -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center">

    <!--
        TextView：文本框
        android:id="@+id/yuehai_text"：设置 id，以便于调用
        android:layout_width="wrap_content"：宽，wrap_content：根据内容大小改变宽度
        android:layout_height="wrap_content"：高
        android:text="文本框"：文本框显示文字
     -->
    <TextView
        android:id="@+id/yuehai_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="文本框"
        />
    
    <!--
        Button：按钮
        android:id="@+id/yuehai_btn"：设置 id，以便于调用
        android:layout_width="wrap_content"：宽，wrap_content：根据内容大小改变宽度
        android:layout_height="wrap_content"：高
        android:text="跳转到 月海"：按钮显示文字
     -->
    <Button
        android:id="@+id/yuehai_btn"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="跳转到 月海"/>

</LinearLayout>
```

4. 在 `activity_main.xml` 对应的 `MainActivity.kt` 中添加逻辑代码，给按钮添加点击事件

```Kotlin
package com.yuehai.android

import android.content.Intent
import android.os.Bundle
import android.os.PersistableBundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 设置内容视图；当前的组件显示哪个视图（窗口）
        // R 就是 res 包
        setContentView(R.layout.activity_main)

        // 使用 id 修改属性；修改文本框显示文字
        // 传入的泛型为 xml 中的标签名，即组件类型
        val textView = findViewById<TextView>(R.id.yuehai_text)
        // 修改文本框显示文字
        textView.text = "修改文本框"

        // 给按钮添加点击事件
        findViewById<Button>(R.id.yuehai_btn).setOnClickListener {
            // 获取 intent 对象
            val intent = Intent()
            // 跳转到该工程下的（同一个 Application 中的）activity 或者 service
            // 参数一为当前 Package 的 context，当前 Activity 的 context 就是 this，其他 Package 可能用到 createPackageContex()
            // 参数二为你要打开的 Activity 的类名
            intent.setClass(this, Yuehai().javaClass)
            
            // 启动窗口
            startActivity(intent)
        }
    }

}
```

5. 启动测试

# 二、`Android` 简单控件

1. 创建新模块：`01_simplecontrol`
2. 若是没有选默认样式，则可能 `res` 下没有 `layout` 等文件夹，可以自己创建
3. 与 `css` 类似
4. 属性设置方式基本都有两种：
	1. 在 XML 文件中通过属性设置
	2. 在代码中调用文本视图对象设置

## 1、文本显示

1. 设置文本：`android:text` 
	1. 引用字符串资源： `@string/xxx`
2. 设置文本大小：`android:textSize="50px"`
	        px:它是手机屏幕的最小显示单位，与设备的显示屏有关。
	        dp:它是与设备无关的显示单位，只与屏幕的尺寸有关。
	        sp:它专门用来设置字体大小，在系统设置中可以调整字体大小。
3. 设置文本颜色：`android:textColor="#F44336"`
4. 在 `layout` 下创建窗口文件 `layout.xml`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230417160550.png)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:gravity="center">
	
	<!--
	    1、android:text="@string/yuehai_text"：设置文本
	    2、android:textSize="50px"：设置文本大小
	        px:它是手机屏幕的最小显示单位，与设备的显示屏有关。
	        dp:它是与设备无关的显示单位，只与屏幕的尺寸有关。
	        sp:它专门用来设置字体大小，在系统设置中可以调整字体大小。
        3、android:textColor="#F44336"：设置文本颜色
	 -->
	<TextView
		android:id="@+id/yuehai_text"
		android:text="@string/yuehai_text"
		android:textSize="20sp"
		android:textColor="#F44336" />

</LinearLayout>
```

5. `res/values/strings.xml` 字符串常量

```xml
<resources>
	<string name="app_name">01_SimpleControl</string>
	<string name="yuehai_text">月海 —— 文本框</string>
</resources>
```

6. 在 `AndroidManifest.xml` 清单文件中进行注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!--
        android:allowBackup，是否允许应用备份。
            允许用户备份系统应用和第三方应用的 apk 安装包和应用数据，以便在刷机或者数据丢失后恢复应用，用户即可通过 adb backup 和 adb restore 来进行对应用数据的备份和恢复。
            为 true 表示允许，为 false 则表示不允许
        android:icon，指定 App 在手机屏幕上显示的图标。
        android:label，指定 App 在手机屏幕上显示的名称。
        android:roundIcon，指定 App 的圆角图标。
        android:supportsRtl，是否支持 阿拉伯语/波斯语 这种从右往左的文字排列顺序。为 true 表示支持，为 false 则表示不支持。
        android:theme，指定 App 的显示风格。
     -->
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!--
            android:name=".MainActivity"：当前注册的窗口是哪个
         -->
		<activity
			android:name=".Layout"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<action android:name="android.intent.action.MAIN" />
				
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>
</manifest>
```

7. 创建窗口文件对应的 `Layout.kt` 文件，定义窗口的逻辑

```Kotlin
package com.yuehai.simplecontrol

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class Layout: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.layout)
    }
}
```

8. 运行测试

## 2、视图基础

1. 设置视图宽高 `android:layout_width`、 `android:layout_height`；主要有下列三种:
	1. `match_parent`：表示与上级视图保持一致。
	2. `wrap_content`：表示与内容自适应。
	3. 以 dp 为单位的具体尺寸。
2. 设置视图的间距 `android:layout_margi`；有两种方式：
	1. 采用 `layout_margin` 属性，它指定了当前视图与周围平级视图之间的距离：包括 `layout_margin`、`layout_marginLeft`、`layout_marginTop`、`layout_marginRight`、`layout_marginBottom`
	2. 采用 `padding` 属性，它指定了当前视图与内部下级视图之间的距离：包括 `padding`、`paddingLeft`、 `paddingTop`、`paddingRight`、`paddingBottom`
3. 3、设置视图的对齐方式 `android:layout_gravity`；有两种途径:
	1. 采用 `layout_gravity` 属性，它指定了当前视图相对于上级视图的对齐方式。
	2. 采用 `gravity` 属性，它指定了下级视图相对于当前视图的对齐方式。
	3. `layout_gravity` 与 `gravity` 的取值包括: `left`、`top`、`right`、`bottom`，
	4. 还可以用竖线连接各取值，例如 `left|top` 表示即靠左又靠上，也就是朝左上角对齐。

```xml
<!--
		1、设置视图宽高 android:layout_width、 android:layout_height；主要有下列三种:
			match_parent:表示与上级视图保持一致。
			wrap_content:表示与内容自适应。
			以 dp 为单位的具体尺寸。
		2、设置视图的间距 android:layout_margi；有两种方式：
			采用 layout_margin 属性，它指定了当前视图与周围平级视图之间的距离：包括 layout_margin、layout_marginLeft、layout_marginTop、layout_marginRight、layout_marginBottom
			采用padding属性，它指定了当前视图与内部下级视图之间的距离：包括padding、paddingLeft、 paddingTop.paddingRight、 paddingBottom
		3、设置视图的对齐方式 android:layout_gravity；有两种途径:
			采用 layout_gravity 属性，它指定了当前视图相对于上级视图的对齐方式。
			采用 gravity 属性，它指定了下级视图相对于当前视图的对齐方式。
			layout_gravity 与 gravity 的取值包括: left、top、right、bottom，
			还可以用竖线连接各取值，例如 left|top 表示即靠左又靠上，也就是朝左上角对齐。

	 -->
	<TextView
		android:id="@+id/yuehai_text2"
		android:text="月海 —— 文本框2"
		android:textSize="20sp"
		
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_margin="20dp"
		android:layout_gravity="center" />
```

## 3、常用布局

- 各种布局可以随意嵌套

### ①、线性布局 LinearLayout

1. 线性布局内部的各视图有两种排列方式：
	1. `orientation` 属性值为 `horizontal` 时，内部视图在水平方向从左往右排列。
	2. `orientation` 属性值为 `vertical` 时，内部视图在垂直方向从上往下排列。
	3. 如果不指定 `orientation` 属性，则 `LinearLayout` 默认水平方向排列。
2. 特点：<font color="#ff0000">要不水平排列，要不竖直排列</font>，通过 `orintation` 进行设置（`horiztal` 为水平，`vertical` 为竖直）；
	1. 横向布局只能在一排中横向排列元素
	2. 纵向布局只能在一列中竖向排列元素
	3. 所以一个窗口中横向布局和纵向布局要结合使用
3. 权重属性：通过 `layout_weight` 来设置，在线性布局的直接下级进行设置，表示该下级布局占据的宽高比例。
4. `layout_width` 填 `0dp` 时，`layout_weight` 表示水平方向的宽度比例。
5. `layout_height` 填 `0dp` 时，`layout_weight` 表示垂直方向的高度比例。

### ②、相对布局 `RelativeLayout`

1. 相对布局的下级视图位置由其他视图决定。用于确定下级视图位置的参照物分两种：
	1. 与该视图自身平级的视图
	2. 该视图的上级视图(也就是它归属的 RelativeLayout)
2. 如果不设定下级视图的参照物，那么下级视图默认显示在 RelativeLayout 内部的左上角。
3. 相对位置的一些取值：

| 相对位置的属性取值       | 相对位置说明                     |
| ------------------------ | -------------------------------- |
| layout_toLeftOf          | 当前视图在指定视图的左边         |
| layout_toRightOf         | 当前视图在指定视图的右边         |
| layout_above             | 当前视图在指定视图的上方         |
| layout_below             | 当前视图在指定视图的下方         |
| layout_alignLeft         | 当前视图与指定视图的左侧对齐     |
| layout_alignRight        | 当前视图与指定视图的右侧对齐     |
| layout_alignTop          | 当前视图与指定视图的顶部对齐     |
| layout_alignBottom       | 当前视图与指定视图的底部对齐     |
| layout_centerlnParent    | 当前视图在上级视图中间           |
| layout_centerHorizontal  | 当前视图在上级视图的水平方向居中 |
| layout_centerVertical    | 当前视图在上级视图的垂直方向居中 |
| layout_alignParentLeft   | 当前视图与上级视图的左侧对齐     |
| layout_alignParentRight  | 当前视图与上级视图的右侧对齐     |
| layout_alignParentTop    | 当前视图与上级视图的顶部对齐     |
| layout_alignParentBottom | 当前视图与上级视图的底部对齐     |

### ③、网格布局 `GridLayout`

1. 网格布局支持多行多列的<font color="#ff0000">表格</font>排列。
2. 网格布局默认从左往右、从上到下排列，它新增了两个属性:
3. `columnCount` 属性，它指定了网格的列数，即每行能放多少个视图
4. `rowCount` 属性，它指定了网格的行数，即每列能放多少个视图;

### ④、滚动视图 `ScrollView`

1. 滚动视图有两种：
2. `ScrollView`，它是垂直方向的滚动视图；垂直方向滚动时，`layout_width` 属性值设置为 `match_parent`，`layout_height` 属性值设置为 `wrap_content`。
3. `HorizontalScrollView`，它是水平方向的滚动视图；水平方向滚动时，`layout_width` 属性值设置为 `wrap_content`，`ayout_height` 属性值设置为 `match_parent`。

### ⑤、新的相对布局 `ConstraintLayout`

## 4、按钮

1. `Button` 继承于 `TextView`，因此它们拥有的属性都是共通的。
2. 除此之外，`Button` 最重要的是点击事件。
	1. 点击监听器：通过 `setOnClickListener` 方法设置。按钮被按住少于 500 毫秒时，会触发点击事件。
	2. 长按监听器：通过 `setOnLongClickListener` 方法设置。按钮被按住超过 500 毫秒时，会触发长按事件；需要返回值， `true` 为成功，`false`  为失败
3. 有三种设置方式：
	1. 匿名内部类
	2. 实现 `OnClickListener` 接口
	3. `xml` 中配置（不推荐）
4. 在实际业务中，按钮通常拥有两种状态，即不可用状态与可用状态，它们在外观和功能上的区别如下：
	1. 不可用按钮：按钮不允许点击，即使点击也没反应，同时按钮文字为灰色
	2. 可用按钮：按钮允许点击，点击按钮会触发点击事件，同时按钮文字为正常的黑色
	3. 是否允许点击由 `enabled` 属性控制，属性值为 `true` 时表示允许点击，为 `false` 时表示不 允许
点击。
5. 按钮控件 `Button` 由 `TextView` 派生而来，它们之间的区别有：
	1. `Button` 拥有默认的按钮背景，而 `TextView` 默认无背景：
	2. `Button` 的内部文本默认居中对齐，而 `TextView` 的内部文本默认靠左对齐；
	3. `Button` 会默认将英文字母转为大写，而 `TextView` 保持原始的英文大小写;

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:gravity="center"
	android:orientation="vertical">
	
	<!--
	    1、android:text="@string/yuehai_text"：设置文本
	    2、android:textSize="50px"：设置文本大小
	        px:它是手机屏幕的最小显示单位，与设备的显示屏有关。
	        dp:它是与设备无关的显示单位，只与屏幕的尺寸有关。
	        sp:它专门用来设置字体大小，在系统设置中可以调整字体大小。
        3、android:textColor="#F44336"：设置文本颜色
    -->
	<TextView
		android:id="@+id/yuehai_text"
		android:layout_gravity="start"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		
		android:text="@string/yuehai_text"
		android:textSize="20sp"
		android:textColor="#F44336" />
	
	<!--
		1、设置视图宽高 android:layout_width、 android:layout_height；主要有下列三种:
			match_parent:表示与上级视图保持一致。
			wrap_content:表示与内容自适应。
			以 dp 为单位的具体尺寸。
		2、设置视图的间距 android:layout_margi；有两种方式：
			采用 layout_margin 属性，它指定了当前视图与周围平级视图之间的距离：包括 layout_margin、layout_marginLeft、layout_marginTop、layout_marginRight、layout_marginBottom
			采用padding属性，它指定了当前视图与内部下级视图之间的距离：包括padding、paddingLeft、 paddingTop.paddingRight、 paddingBottom
		3、设置视图的对齐方式 android:layout_gravity；有两种途径:
			采用 layout_gravity 属性，它指定了当前视图相对于上级视图的对齐方式。
			采用 gravity 属性，它指定了下级视图相对于当前视图的对齐方式。
			layout_gravity 与 gravity 的取值包括: left、top、right、bottom，
			还可以用竖线连接各取值，例如 left|top 表示即靠左又靠上，也就是朝左上角对齐。

	 -->
	<TextView
		android:id="@+id/yuehai_text2"
		android:text="月海 —— 文本框2"
		android:textSize="20sp"
		
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_margin="20dp"
		android:layout_gravity="center" />
	
	<Button
		android:id="@+id/yuehai_btn"
		android:text="月海 —— 按钮"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>
	

</LinearLayout>
```

```Kotlin
package com.yuehai.simplecontrol

import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Layout: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.layout)

        // 1、获取按钮 yuehai_btn 元素
        val button = findViewById<Button>(R.id.yuehai_btn)
        
        // 设置点击事件；
        // 2.1、方式一：匿名内部类；点击监听器
        button.setOnClickListener {
            println("匿名内部类；点击监听器")
        }
        // 2.2、方式一：匿名内部类；长按监听器
        button.setOnLongClickListener {
            println("匿名内部类；长按监听器")
            // 禁止点击事件
            button.isEnabled = false
            true
        }
        
        // 2、方式二：实现 OnClickListener 接口
        // button.setOnClickListener(MyOnClick())
        // button.setOnLongClickListener(MyOnLongClick())
    }
}

// 实现 OnClickListener 接口
class MyOnClick: View.OnClickListener {
    override fun onClick(p0: View?) {
        println("实现 OnClickListener 接口；点击监听器")
    }
}
// 实现 OnClickListener 接口
class MyOnLongClick: View.OnLongClickListener {
    override fun onLongClick(p0: View?): Boolean {
        println("实现 OnClickListener 接口；长按监听器")
        return true
    }
    
}
```

## 5、图像显示

1. 图片一般放在 `res/drawable` 目录下，设置图像显示一般有两种方法：
	1. 在 `XML` 文件中，通过属性 `android:src` 设置图片资源，属性值格式形如 `@drawable/不含扩展名` 的图片名称。
	2. 在 Java 代码中，调用 `setImageResource` 方法设置图片资源，方法参数格式形如 `R.drawable.不含扩展名` 的图片名称。

### ①、图像的缩放问题

1. `ImageView` 本身默认图片居中显示，若要改变图片的显示方式，可通过 `scaleType` 属性设定
2. 该属性的取值说明如下

| XML中的缩放类型 | ScaleType类中的缩放类型 | 说明                                                 |
| --------------- | ----------------------- | ---------------------------------------------------- |
| fitXY           | FIT XY                  | 拉伸图片使其正好填满视图(图片可能被拉伸变形)         |
| fitStart        | FIT START               | 保持宽高比例，拉伸图片使其位于视图上方或左侧         |
| fitCenter       | FIT_ CENTER             | 保持宽高比例，拉伸图片使其位于视图中间               |
| fitEnd          | FIT_ END                | 保持宽高比例，拉伸图片使其位于视图下方或右侧         |
| center          | CENTER                  | 保持图片原尺寸，并使其位于视图中间                   |
| centerCrop      | CENTER_ CROP            | 拉伸图片使其充满视图，并位于视图中间                 |
| centerlnside    | CENTER INSIDE           | 保持宽高比例，缩小图片使之位于视图中间(只缩小不放大) |

### ②、图像按钮 `ImageButton`

1. `ImageButton` 是显示图片的图像按钮，但它继承自 `ImageView`，而非继承 `Button`。
2. `ImageButton` 和 `Button` 之间的区别有：
	1. `Button` 既可显示文本也可显示图片，`ImageButton` 只能显示图片不能显示文本。
	2. `ImageButton` 上的图像可按比例缩放，而 `Button` 通过背景设置的图像会拉伸变形。
	3. `Button` 只能靠背景显示一张图片，而 `ImageButton` 可分别在前景和背景显示图片，从而实现两张图片叠加的效果。
3. 在某些场合，有的字符无法由输入法打出来，或者某些文字以特殊字体展示，就适合适合先切图再放到 `imageButton`。例如：开平方符号 `√`， 等等。
4. ImageButton 与 ImageView 之间的区别有：
	1. `ImageButton` 有默认的按钮背景，`ImageView` 默认无背景。
	2. `ImageButton` 默认的缩放类型为 `center`， 而 `ImageView` 默认的缩放类型为 `fitCenter`.

### ③、同时展示图片与按钮

1. 利用 LinearLayout 对 ImageView 和 TextView 组合布局。
2. 通过按钮控件 `Button` 的 `drawable ***` 属性设置文本周围的图标。
	1. drawableTop: 指定文字上方的图片。
	2. drawableBottom: 指定文字下方的图片。
	3. drawableLeft: 指定文字左边的图片。
	4. drawableRight: 指定文字右边的图片。
	5. drawablePadding: 指定图片与文字的间距。

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:gravity="center"
	android:orientation="vertical">

	<!--
	    1、android:text="@string/yuehai_text"：设置文本
	    2、android:textSize="50px"：设置文本大小
	        px:它是手机屏幕的最小显示单位，与设备的显示屏有关。
	        dp:它是与设备无关的显示单位，只与屏幕的尺寸有关。
	        sp:它专门用来设置字体大小，在系统设置中可以调整字体大小。
        3、android:textColor="#F44336"：设置文本颜色
    -->
	<TextView
		android:id="@+id/yuehai_text"
		android:layout_gravity="start"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"

		android:text="@string/yuehai_text"
		android:textSize="20sp"
		android:textColor="#F44336" />

	<!--
		1、设置视图宽高 android:layout_width、 android:layout_height；主要有下列三种:
			match_parent:表示与上级视图保持一致。
			wrap_content:表示与内容自适应。
			以 dp 为单位的具体尺寸。
		2、设置视图的间距 android:layout_margi；有两种方式：
			采用 layout_margin 属性，它指定了当前视图与周围平级视图之间的距离：包括 layout_margin、layout_marginLeft、layout_marginTop、layout_marginRight、layout_marginBottom
			采用padding属性，它指定了当前视图与内部下级视图之间的距离：包括padding、paddingLeft、 paddingTop.paddingRight、 paddingBottom
		3、设置视图的对齐方式 android:layout_gravity；有两种途径:
			采用 layout_gravity 属性，它指定了当前视图相对于上级视图的对齐方式。
			采用 gravity 属性，它指定了下级视图相对于当前视图的对齐方式。
			layout_gravity 与 gravity 的取值包括: left、top、right、bottom，
			还可以用竖线连接各取值，例如 left|top 表示即靠左又靠上，也就是朝左上角对齐。

	 -->
	<TextView
		android:id="@+id/yuehai_text2"
		android:text="月海 —— 文本框2"
		android:textSize="20sp"

		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_margin="20dp"
		android:layout_gravity="center" />

	<Button
		android:id="@+id/yuehai_btn"
		android:text="月海 —— 按钮"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

	<!-- 线性布局 -->
	<LinearLayout
		android:layout_width="match_parent"
		android:layout_height="match_parent"
		android:gravity="center"
		android:orientation="horizontal">
		
		<!--
			图片显示
			安卓的布局好像原生没有百分比设置，可以用某些依赖实现，比如：Android ConstraintLayout
		 -->
		<ImageView
				android:layout_width="100dp"
				android:layout_height="wrap_content"
				android:src="@drawable/qq"/>
		
		<!-- 图片按钮 -->
		<ImageButton
				android:id="@+id/yuehai_imageBtn"
				android:layout_width="100dp"
				android:layout_height="wrap_content"
				android:src="@drawable/wcat"
				android:scaleType="fitCenter"/>

		<!-- 按钮 文字 + 图片 -->
		<Button
				android:layout_width="100dp"
				android:layout_height="wrap_content"
				android:text="图片文字按钮"
		android:drawableTop="@drawable/wcat"/>
		
	</LinearLayout>
	
</LinearLayout>
```

```Kotlin
package com.yuehai.simplecontrol

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageButton
import androidx.appcompat.app.AppCompatActivity

class Layout: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.layout)

        // 1、获取按钮 yuehai_btn 元素
        val button = findViewById<Button>(R.id.yuehai_btn)
        
        // 设置点击事件；
        // 2.1、方式一：匿名内部类；点击监听器
        button.setOnClickListener {
            println("匿名内部类；点击监听器")
        }
        // 2.2、方式一：匿名内部类；长按监听器
        button.setOnLongClickListener {
            println("匿名内部类；长按监听器")
            // 禁止点击事件
            button.isEnabled = false
            true
        }

        // 2、方式二：实现 OnClickListener 接口
        // button.setOnClickListener(MyOnClick())
        // button.setOnLongClickListener(MyOnLongClick())

        // 图片按钮绑定点击事件
        findViewById<ImageButton>(R.id.yuehai_imageBtn).setOnClickListener {
            println("点击图片按钮")
        }
    }
}

// 实现 OnClickListener 接口
class MyOnClick: View.OnClickListener {
    override fun onClick(p0: View?) {
        println("实现 OnClickListener 接口；点击监听器")
    }
}
// 实现 OnClickListener 接口
class MyOnLongClick: View.OnLongClickListener {
    override fun onLongClick(p0: View?): Boolean {
        println("实现 OnClickListener 接口；长按监听器")
        return true
    }
    
}
```

# 三、`Activity` 

- `Activity` 是安卓开发四大组件之一，非常重要。
- 感觉类似 `vue` 的路由

## 1、`Activity` 的启动和结束

1. `Activity` 的启动这里指的是跳转，从一个页面跳转到一个新的页面，就相当于启动了一个新的页面。
2. 从当前页面跳到新页面，跳转代码：`startActivity(Intent(this, Activity01().javaClass))`
	1. `Intent` 翻译过来为 “意图”，它是一种运行时绑定（run-time binding）机制
	2. 可以应用于两个应用间的通讯交互，也能够应用于在同一个应用下不同组件的交互（activity、service、broadcast receiver
	3. 此处的参数 1：本窗口
	4. 此处的参数 2：要跳转到的窗口的 class 类
3. 从当前页面回到上一个页面，相当于关闭当前页面，返回代码如下：`finish()`
4. 新建 `activity_01.xml` 窗口

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent">
	
	<!-- 按钮 -->
	<Button
		android:id="@+id/yuehai_activity01_btn"
		android:text="activity01 -> 02"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

</LinearLayout>
```

5. 新建 `activity_01.xml` 窗口对应的代码文件

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Activity01:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_01)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity01_btn).setOnClickListener {
            /**
             * Intent 翻译过来为 “意图”，它是一种运行时绑定（run-time binding）机制
             * 可以应用于两个应用间的通讯交互，也能够应用于在同一个应用下不同组件的交互（activity、service、broadcast receiver
             * 此处的参数 1：本窗口
             * 此处的参数 2：要跳转到的窗口的 class 类
             */
            val intent = Intent(this, Activity02().javaClass)
            // 跳转到 Activity02 窗口，传递 intent 对象
            startActivity(intent)
        }
    }
}
```

6. 新建 `activity_02.xml` 窗口

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent">
	
	<!-- 按钮 -->
	<Button
		android:id="@+id/yuehai_activity02_btn"
		android:text="activity02 -> 01"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start|top"/>
	
	<!--
		返回按钮
		文字颜色：android:textColor="@color/black"
		背景颜色：android:backgroundTint="@color/teal_200"
	 -->
	<Button
		android:id="@+id/yuehai_activity02_back"
		android:text="返回"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/teal_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="end|top"/>

</LinearLayout>
```

7. 新建 `activity_02.xml` 窗口对应的代码文件

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Activity02:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_02)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity02_btn).setOnClickListener {
            /**
             * Intent 翻译过来为 “意图”，它是一种运行时绑定（run-time binding）机制
             * 可以应用于两个应用间的通讯交互，也能够应用于在同一个应用下不同组件的交互（activity、service、broadcast receiver
             * 此处的参数 1：本窗口
             * 此处的参数 2：要跳转到的窗口的 class 类
             */
            // 跳转到 Activity01 窗口，传递 intent 对象
            startActivity(Intent(this, Activity01().javaClass))
        }

        // 返回按钮；点击关闭当前页面，返回上个页面
        findViewById<Button>(R.id.yuehai_activity02_back).setOnClickListener {
            // 结束当前的活动页面
            finish()
        }
    }
}
```

8. 在 `AndroidManifest.xml` 清单文件中注册窗口

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!--
        android:allowBackup，是否允许应用备份。
            允许用户备份系统应用和第三方应用的 apk 安装包和应用数据，以便在刷机或者数据丢失后恢复应用，用户即可通过 adb backup 和 adb restore 来进行对应用数据的备份和恢复。
            为 true 表示允许，为 false 则表示不允许
        android:icon，指定 App 在手机屏幕上显示的图标。
        android:label，指定 App 在手机屏幕上显示的名称。
        android:roundIcon，指定 App 的圆角图标。
        android:supportsRtl，是否支持 阿拉伯语/波斯语 这种从右往左的文字排列顺序。为 true 表示支持，为 false 则表示不支持。
        android:theme，指定 App 的显示风格。
     -->
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- android:name=".MainActivity"：当前注册的窗口是哪个 -->
		<activity
			android:name=".Layout"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<activity
			android:name=".Activity01"
			android:exported="true"
			android:label="@string/app_name">
			<!-- 是主窗口，要配置 intent-filter -->
			<intent-filter>
				<action android:name="android.intent.action.MAIN" />
				
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
		<activity
			android:name=".Activity02"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
	</application>
</manifest>
```

## 2、`Activity` 的生命周期

### ①、生命周期

1. `onCreate`：创建活动。把页面布局加载进内存，进入了初始状态。
2. `onStart`：开始活动。把活动页面显示在屏幕上，进入了就绪状态。
3. `onResume`：恢复活动。活动页面进入活跃状态，能够与用户正常交互，例如允许响应用户的点击动作、允许用户输入文字等等。
4. `onPause`：暂停活动。页面进入暂停状态，无法与用户正常交互。
5. `onStop`：停止活动。页面将不在屏幕上显示。
6. `onDestroy`：销毁活动。回收活动占用的系统资源，把页面从内存中清除。
7. `onRestart`：重启活动。重新加载内存中的页面数据。
8. `onNewIntent`：重用已有的活动实例

![|631](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230419105744.png)

### ②、各状态之间的切换过程

1. 打开新页面的方法调用顺序为：`onCreate → onStart → onResume`
2. 关闭旧页面的方法调用顺序为：`onPause → onStop → onDestroy`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230419105858.png)

## 3、`Activity` 的启动模式

- Android 允许在创建 `Activity` 时设置启动模式，通过启动模式控制 `Activity` 的出入栈行为

### ①、简介

1. 某 App 先后打开两个活动，此时活动栈的变动情况如下图所示。

![|648](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230419110418.png)

2. 依次结束已打开的两个活动，此时活动栈的变动情况如下图所示

![|615](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230419110428.png)

### ②、静态设置

#### Ⅰ、设置方式

1. 打开 `AndroidManifest.xml` 清单文件，给 `activity` 添加属性 `android:launchMode`。如以下表示该 `activity` 使用 `standard` 标准模式，默认也是标准模式

```xml
<!--
			android:name=".MainActivity"：当前注册的窗口是哪个
			android:exported="true"：表示当前 Activity 是否可以被另一个 Application 的组件启动：true 允许被启动；false 不允许被启动
			android:label="@string/app_name"：标识当前窗口名
			android:launchMode="standard"：指定启动模式
		 -->
		<activity
			android:name=".Activity01"
			android:exported="true"
			android:label="@string/app_name"
			android:launchMode="standard">
			<!-- 是主窗口，要配置 intent-filter -->
			<intent-filter>
				<action android:name="android.intent.action.MAIN" />
				
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
```

2. `launchMode` 属性的取值说明：

| launchMode属性值  | 说明                                                                            |
| -------------- | ----------------------------------------------------------------------------- |
| standard       | 标准（默认）模式，无论何时启动哪个活动，都是重新创建该页面的实例并放入栈顶。<br/>如果不指定 `launchMode` 属性，则默认为标准模式     |
| singleTop      | 栈顶复用模式，启动新活动时，判断如果栈顶正好就是该活动的实例，则重用该实例<br/>否则创建新的实例并放入栈顶，也就是按照 `standard` 模式处理 |
| singleTask     | 栈内复用模式，启动新活动时，判断如果栈中存在该活动的实例，则重用该实例,并清除位于该实例上面的所有实例<br/>否则按照 `standard` 模式处理  |
| singlelnstance | 全局唯一模式，将该活动的实例放入一个新栈中，原栈的实例列表保持不变                                             |

### ③、动态设置

1. 通过 Intent 动态设置 Activity 启动模式：`intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP`
2. `intent.flags` 的取值有：

| lntent类的启动标志 | 说明 |
| ------------------ | ---- |
|Intent.FLAG_ACTIVITY_NEW_TASK|开辟一个新的任务栈<br />该值类似于 `launchMode="standard"`<br />不同之处在于，如果原来不存在活动栈，则会创建一个新栈|
|Intent.FLAG_ACTIVrTY_SINGLE_TOP|当栈顶为待跳转的活动实例之时，则重用栈顶的实例<br />该值等同于 `launchMode="singleTop"`|
|Intent.FLAG_ACTIVITY_CLEAR_TOP|当栈中存在待跳转的活动实例时，则重新创建一个新实例，并清除原实例上方的所有实例<br />该值与 `launchMode="singleTask"` 类似<br />但 `singleTask` 采取 `onNewIntent` 方法启用原任务﹐而 `FLAG_ACTIVrrY_CLEAR_TOP` 采取先调用 `onDestroy` 再调用 `onCreate` 来创建新任务|
|Intent.FLAG_ACTIVITY_NO_HISTORY|该标志与 `launchMode="standard"` 情况类似，但栈中不保存新启动的活动实例<br />这样下次无论以何种方式再启动该实例，也要走 `standard` 模式的完整流程|
|Intent.FLAG_ACTIVrrY_CLEAR_TASK|该标志非常暴力，跳转到新页面时，栈中的原有实例都被清空<br />注意该标志需要结合 F`LAG_ACTIVITY_NEW_TASK` 使用，即 `setFlags` 方法的参数为 `Intent.FLAG_ACTIVITY_CLEAR_TASK 丨 Intent.FLAG_ACTIVITY_NEW_TASK` |

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Activity01:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_01)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity01_btn).setOnClickListener {
            /**
             * Intent 翻译过来为 “意图”，它是一种运行时绑定（run-time binding）机制
             * 可以应用于两个应用间的通讯交互，也能够应用于在同一个应用下不同组件的交互（activity、service、broadcast receiver
             * 此处的参数 1：本窗口
             * 此处的参数 2：要跳转到的窗口的 class 类
             */
            val intent = Intent(this, Activity02().javaClass)

            // 通过 Intent 动态设置 Activity 启动模式
            intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP

            // 跳转到 Activity02 窗口，传递 intent 对象
            startActivity(intent)
        }
    }
}
```

## 4、`Activity` 之间传递信息

### ①、介绍

1. `Intent` 能够让 Android 各组件之间进行沟通。
2. `Intent` 可以完成 3 部分工作：
	1. 表明本次通信从哪里来，往哪里走，要怎么走。
	2. 发送方可以携带消息给接收方，接收方可以从收到的 `Intent` 解析数据。
	3. 发送方如果想要知道接收方的处理结果，接收方也可以通过 `Intent` 返回结果。
3. `Intent` 的一些组成元素：

| 元素名称      | 设置方法         | 说明与用途              |
| --------- | ------------ | ------------------ |
| Component | setComponent | 组件，它指定意图的来源与目标     |
| Action    | setAction    | 动作，它指定意图的动作行为      |
| Data      | setData      | 即Uri，它指定动作要操纵的数据路径 |
| category  | addCategory  | 类别，它指定意图的操作类别      |
| Type      | setType      | 数据类型，它指定消息的数据类型    |
| Extras    | putExtras    | 扩展信息，它指定装载的包裹信息    |
| Flags     | setFlags     | 标志位，它指定活动的启动标志     |

### ②、显式 `Intent`

1. 在 `Intent` 的构造函数中指定：

```Kotlin
val intent = Intent(this, Activity02().javaClass)
```

2. 调用 `setClass` 指定

```Kotlin
val intent = Intent()
intent.setClass(this, Activity02().javaClass)
```

3. 调用 `setComponent` 指定

```Kotlin
val intent = Intent()
val componentName = ComponentName(this, Activity02().javaClass)
intent.component = componentName
```

### ③、隐式 `Intent`

1. 没有明确指定所要跳转的页面，而是通过一些动作字符串来让系统自动匹配。
2. 通常是 App 不想向外暴露 `Activity` 的名称，只给出一些定义好的字符串。这些字符串可以自己定义，也有系统定义的。
3. 常见的系统动作如下：

| `lntent` 类的系统动作常量名 | 系统动作的常量值             | 说明            |
| ------------------------ | ---------------------------- | --------------- |
| ACTION_MAIN              | android.intent.action.MAIN   | App启动时的入口 |
| ACTION_VIEw              | android.intent.action.VIEW   | 向用户显示数据  |
| ACTION_SEND              | android.intent.action.SEND   | 分享内容        |
| ACTION_CALL              | android.intent.action.CALL   | 直接拨号        |
| ACITON_DIAL              | android.intent.action.DIAL   | 准备拨号        |
| ACTION_SENDTO            | android.intent.action.SENDTO | 发送短信        |
| ACTION_ANSWER            | android.intent.action.ANSWER | 接听电话        |

#### Ⅰ、下面以调用系统拨号页面举例

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity


class Activity01:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_01)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity01_btn).setOnClickListener {

            // 2.1、隐式 Intent 传递：
            val phone: String = "12345"
            val intent = Intent()
            // 这里表示设置意图动作为准备拨号
            intent.action = Intent.ACTION_DIAL
            intent.data = Uri.parse("tel:$phone")

            // 跳转到拨号窗口，传递 intent 对象；隐式指定了拨号窗口
            startActivity(intent)
        }
    }
}
```

#### Ⅱ、跳转到自己定义的 `activity`

1. 在 `AndroidManifest.xml` 清单找到该 `activity`，添加 `action` 和 `category` 标签，同时设置 `exported` 为 `true`，表示允许被其他 `activity` 调用。

```xml
<!--
			android:name=".MainActivity"：当前注册的窗口是哪个
			android:exported="true"：表示当前 Activity 是否可以被另一个 Application 的组件启动：true 允许被启动；false 不允许被启动
			android:label="@string/app_name"：标识当前窗口名
			android:launchMode="standard"：指定启动模式
		 -->
		<activity
			android:name=".Activity01"
			android:exported="true"
			android:label="@string/app_name"
			android:launchMode="standard">
			<!-- 是主窗口，要配置 intent-filter -->
			<intent-filter>
				<action android:name="android.intent.action.MAIN" />
				
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
		
		<activity
			android:name=".Activity02"
			android:exported="true"
			android:label="@string/app_name">
			
			<intent-filter>
				<!-- 设置隐式调用 intent 的名称 -->
				<action android:name="android.intent.action.Activity02" />
				<!-- 设置隐式调用 intent 的类型 -->
				<category android:name="android.intent.category.DEFAULT" />
			</intent-filter>
		</activity>
```

2. 调用过程和上面一样：

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity


class Activity01:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_01)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity01_btn).setOnClickListener {
            
            // 2.2、隐式 Intent 传递：跳转到自己定义的 activity
            val phone: String = "12345"
            val intent = Intent()
            // 设置值为 AndroidManifest.xml 中 action 标签的 android:name 值
            intent.action = "android.intent.action.Activity02"
            // 设置值为 AndroidManifest.xml 中 category 标签的 android:name 值
            intent.addCategory(Intent.CATEGORY_DEFAULT)

            // 跳转到跳转到自己定义的 activity，传递 intent 对象；隐式指定了拨号窗口
            startActivity(intent)
        }
    }
}
```

### ④、向下一个 `Activity` 发送消息

1. Intent 重载了很多 putExtra 方法用于传递各种类型的信息，包括整数类型，字符串等。
2. 但是显然通过调用 putExtra 方法会很不好管理，因为数据都是零碎传递。
3. 所以 Android 引入了 `Bundle`，其内部是一个 `Map`，使用起来也和 `Map` 一样
4. Bundle 对各类型数据的读写方法说明：

| 数据类型     | 读方法             | 写方法             |
| ------------ | ------------------ | ------------------ |
| 整型数       | getInt             | putInt             |
| 浮点数       | getFloat           | putFloat           |
| 双精度数     | getDouble          | putDouble          |
| 布尔值       | getBoolean         | putBoolean         |
| 字符串       | getString          | putString          |
| 字符串数组   | getStringArray     | putStringArray     |
| 字符串列表   | getStringArrayList | putStringArrayList |
| 可序列化结构 | getSerializable    | putSerializable    |

5. 向下一个 Activity 发送消息

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity


class Activity01:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_01)

        // 按钮；点击进行跳转
        findViewById<Button>(R.id.yuehai_activity01_btn).setOnClickListener {

            // 4、向下一个 Activity 发送消息
            // 4.1、显式 Intent 传递：在 Intent 的构造函数中指定：
            val intent = Intent(this, Activity02().javaClass)
            // 4.2、通过 bundle 包装数据
            val bundle = Bundle()
            bundle.putString("stringKey", "stringValue")
            // 4.3、将 bundle 放入 intent 对象中
            intent.putExtras(bundle);

            // 4.5、跳转到跳转到自己定义的 activity，传递 intent 对象；隐式指定了拨号窗口
            startActivity(intent)
        }
    }
}
```

6. 接收消息

```Kotlin
package com.yuehai.simplecontrol

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Activity02:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_02)

        // 4.6、跳转到的 Activity 就可以通过 intent 获取到所想要的数据了
        val bundle = intent.extras
        val stringValue = bundle!!.getString("stringKey")
        println("stringValue：$stringValue")
    }
}
```

### ⑤、向上一个 `Activity` 返回消息

1. 在需要返回数据的页面定义数据，关闭页面

```Kotlin
// 5、返回按钮；点击关闭当前页面，返回上个页面
findViewById<Button>(R.id.yuehai_activity02_back).setOnClickListener {

	// 5.1、通过 bundle 包装数据
	val bundle = Bundle()
	bundle.putString("stringResultKey", "stringResultValue")
	// 5.2、将 bundle 放入 intent 对象中
	intent.putExtras(bundle)
	// 5.3、返回数据给上一个页面
	setResult(Activity.RESULT_OK, intent)
	// 5.4、结束当前的活动页面
	finish()
}
```

2. 回调函数，重写 `onActivityResult()` 方法，接收上一个 Activity 中返回的消息

```Kotlin
// 5.5、回调函数，重写 onActivityResult() 方法，接收上一个 Activity 中返回的消息
private val someActivityResultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            // 5.6、获取到返回的数据
            val data = result.data
            Log.i("stringResultKey：", data.toString())
        }
    }
```

3. 调用回调函数 `someActivityResultLauncher` 启动另一个Activity

```Kotlin
// 5.7、按钮；点击进行跳转 activity01 -> 02 并获取其返回数据
findViewById<Button>(R.id.yuehai_activity01_Result).setOnClickListener {
	// 5.8、调用回调函数 someActivityResultLauncher 启动另一个Activity
	someActivityResultLauncher.launch(Intent(this, Activity02().javaClass))
}
```

## 5、`Activity` 获取一些附加信息

1. 获取资源信息

```Kotlin
package com.yuehai.simplecontrol

import android.content.pm.PackageManager
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

/**
@author 月海
@create 2023/4/23 16:12
 */
class Activity03: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.activity_03)

        // 按钮；点击进行跳转 yuehai_activity01_Result
        findViewById<Button>(R.id.yuehai_activity01_resources).setOnClickListener {
            // 获取资源信息
            Log.i("获取资源信息：", getString(R.string.yuehai_text))
            // 获取 color.xml 中的颜色资源
            Log.i("获取资源信息：", getColor(R.color.black).toString())

            // 获取包管理器
            val packageManager = packageManager
            // 获取当前的 Activity 信息
            val activityInfo = packageManager.getActivityInfo(componentName, PackageManager.GET_META_DATA)

            // 获取当前的 Activity 信息
            Log.i("获取当前 Activity 的 name：", activityInfo.name)
            Log.i("获取当前 Activity 的 name：", activityInfo.exported.toString())
            Log.i("获取当前 Activity 的 name：", activityInfo.labelRes.toString())
            Log.i("获取当前 Activity 的 name：", activityInfo.launchMode.toString())

            // 获取元数据
            val bundle = activityInfo.metaData
            Log.i("获取当前 Activity 的获取元数据 data1：", bundle.getString("data1")!!)
            Log.i("获取当前 Activity 的获取元数据 data2：", bundle.getInt("data2").toString())
            Log.i("获取当前 Activity 的获取元数据 data3：", bundle.getString("data3")!!)

        }
    }
}
```

2. 在 `AndroidManifest.xml` 清单文件中注册，并添加元数据

```xml
<!-- 注册窗口 -->
<activity
	android:name=".Activity03"
	android:exported="true"
	android:label="@string/app_name"
	android:launchMode="standard">
	<!-- 是主窗口，要配置 intent-filter -->
	<intent-filter>
		<action android:name="android.intent.action.MAIN" />
		<category android:name="android.intent.category.LAUNCHER" />
	</intent-filter>
	
	<!--
		<meta-data>：直译为“元数据”，
		该标签可为 <activity>、<activity-alias>、<application>、<provider>、<receiver>、<service> 等组件提供附加数据项。
		组件元素可以包含任意数量的 <meta-data> 子元素。系统将 meta-data 配置的数据存储于一个 Bundle 对象中，可以通过 PackageItemInfo.metaData 字段获取
	 -->
	<meta-data android:name="data1" android:value="appVersion" />
	<meta-data android:name="data2" android:value="10001" />
	<meta-data android:name="data3" android:value="@string/app_name" />
</activity>
```

# 四、`Android`  中级控件

## 1、图形定制

### ①、图形 Drawable

1. Drawable 类型表达了各种各样的图形，包括图片、色块、画板、背景等。
2. 包含图片在内的图形文件放在 `res` 目录的各个 `drawable` 目录下，其中 `drawable` 目录一般保存描述性的 XML 文件，而图片文件一般放在具体分辨率的 `drawable` 目录下。
3. 各视图的 `background` 属性、`ImageView` 和 `ImageButton` 的 `src` 属性、`TextView` 和 `Button` 四个方向的 `drawable***` 系列属性都可以引用图形文件。

### ②、形状图形

1. Shape 图形又称形状图形，它用来描述常见的几何形状，包括矩形、圆角矩形、圆形、椭圆等等。
2. 形状图形的定义文件是以 shape 标签为根节点的 XML 描述文件，它支持四种类型的形状：
	1. rectangle：矩形。默认值
	2. oval：椭圆。此时corners节点会失效
	3. line：直线。此时必须设置stroke节点，不然会报错
	4. ring：圆环
3. 除了根节点 shape 标签，形状图形还拥有下列规格标签：
	1. size（尺寸），它描述了形状图形的宽高尺寸。
	2. stroke（描边），它描述了形状图形的描边规格。
	3. corners（圆角），它描述了形状图形的圆角大小。
	4. solid（填充），它描述了形状图形的填充色彩。
	5. padding（间隔），它描述了形状图形与周围边界的间隔。
	6. gradient（渐变），它描述了形状图形的颜色渐变。
4. 创建：右键 drawable -> 新建 -> Drawable Resource File
5. 例子：

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
	<!-- 指定了形状内部的填充颜色 -->
	<solid android:color="#ffdd66" />
	<!-- 指定了形状轮廓的粗细与颜色 -->
	<stroke android:width="1dp" android:color="#aaaaaa" />
	<!-- 指定了形状四个圆角的半径 -->
	<corners android:radius="10dp" />
</shape>
```

![|292](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230515165103.png)

6. 指定某几个角为圆角

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/dark_blue" />
    <!-- 指定右上角和右下角为圆角 -->
    <corners
		android:radius="0dp"
		android:topLeftRadius="0dp"
		android:topRightRadius="@dimen/dp_23"
		android:bottomLeftRadius="0dp"
		android:bottomRightRadius="@dimen/dp_23" />
</shape>
```

### ③、九宫格图片

1. 将某张图片设置成视图背景时，如果图片尺寸太小，则系统会自动拉伸图片使之填满背景。
2. 可是一旦图片拉得过大，其画面容易变得模糊。
3. 点九图片的扩展名是 png，文件名后面常带有 `.9` 字样。因为该图片划分了 3×3 的九宫格区域，所以得名点九图片，也叫九宫格图片。
4. 在拉伸点九图片时，只拉伸内部区域，不拉伸边缘线条。
5. 在 Android Studio 中右击某张图片，并在右键菜单中选择 `Create 9-Patch files`，接着单击 OK 按钮即可自动生成点九图片。
6. 分为横向选中区域和纵向选中区域
	1. 当图片被横向拉伸时，只会拉伸纵向选中的区域，没有选中的区域不会被拉伸
	2. 当图片被纵向拉伸时，只会拉伸横向选中的区域，没有选中的区域不会被拉伸

![|330](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230516091542.png)

### ④、状态列表图形

1. 常见的图形文件一般为静态图形，但有时会用到动态图形，比如 Button 按钮的背景在正常情况下是凸起的，在按下时是凹陷的，从按下到弹起的过程，用户便能知道点击了这个按钮。
2. 根据不同的触摸情况变更不同的图形状态
3. 在项目中创建状态图形的 XML 文件，需右击 drawable 目录，然后在右键菜单中依次选择 New → Drawable resource file，即可自动生成一个空的 XML 文件。
4. 下面是一个状态列表图形的 drawable 文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- 按下时显示的图片 -->
    <item android:state_pressed="true" android:drawable="@drawable/qq" />
    <!-- 默认显示的图片 -->
    <item android:drawable="@drawable/shape_rounded_rectangle" />
</selector>
```

5. 状态类型的取值说明：

| 状态类型的属性名称 | 说明 | 适用的控件 |
| ------------------ | ---- | ---------- |
|state_pressed|是否按下|按钮Button|
|state_checked|是否勾选|复选框checkBox、单选按钮RadioButton|
|state_focused|是否获取焦点|文本编辑框EditText|
|state_selected|是否选中|各控件通用|

## 2、选择按钮

### ①、`CompoundButton` 类

1. `CompoundButton` 类是抽象的复合按钮，由它派生而来的子类包括：复选框 `CheckBox`、单选按钮 `RadioButton` 以及开关按钮 `Switch`。
2. 又因为 `CompoundButton` 类本身继承了 `Button` 类，故以上几种按钮同时具备 `Button` 的属性和方法
3. 下图描述了复合按钮的继承关系：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230516094727.png)

4. `CompoundButton` 在 XML 文件中主要使用下面两个属性。
	1. `checked`：指定按钮的勾选状态，true 表示勾选，false 表示未勾选。默认未勾选。
	2. `button`：指定左侧勾选图标的图形资源。如果不指定就使用系统的默认图标。
5. `CompoundButton` 在 Java 代码中主要使用下列4种方法。
	1. `setChecked`：设置按钮的勾选状态。
	2. `setButtonDrawable`：设置左侧勾选图标的图形资源。
	3. `setOnCheckedChangeListener`：设置勾选状态变化的监听器。
	4. `isChecked`：判断按钮是否勾选。

### ②、复选框 CheckBox

1. 创建布局文件 `select_button.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 复选框 -->
	<CheckBox
		android:id="@+id/select_button_CheckBox_1"
		android:text="复选框 1"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	<CheckBox
		android:id="@+id/select_button_CheckBox_2"
		android:text="复选框 2"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 复选框提示文字 -->
	<TextView
		android:id="@+id/select_button_text_CheckBox"
		android:text="复选框提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginBottom="20dp"/>

</LinearLayout>
```

2. 创建布局文件对应的代码文件 `SelectButtonActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import android.widget.CheckBox
import android.widget.CompoundButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class SelectButtonActivity: AppCompatActivity(), CompoundButton.OnCheckedChangeListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.select_button)
		
		// 给复选框 1 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_1).setOnCheckedChangeListener(this)
		
		// 给复选框 2 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_2).setOnCheckedChangeListener(this)

	}
	
	/**
	 * 实现 onCheckedChanged 方法，当复选框被选择和取消勾选时会被调用
	 *
	 * 参数 1：buttonView：被操作的复选框对象
	 * 参数 2：isChecked：被选中还是被取消勾选
	 */
	override fun onCheckedChanged(buttonView: CompoundButton?, isChecked: Boolean) {
		findViewById<TextView>(R.id.select_button_text_CheckBox).text = String.format("您%s了%s", if (isChecked) "勾选" else "取消勾选", buttonView?.text)
		
	}
}
```

3. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 选择按钮 SelectButtonActivity -->
		<activity
			android:name=".SelectButtonActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口 -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
	</application>

</manifest>
```

4. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101102.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101121.png)

### ③、开关按钮 Switch

1. `Switch` 是开关按钮，它在选中与取消选中时可展现的界面元素比复选框丰富。
2. `Switch` 控件新添加的 XML 属性说明如下。
	1. `textOn`：设置右侧开启时的文本。
	2. `textOff`：设置左侧关闭时的文本。
	3. `track`：设置开关轨道的背景。
	4. `thumb`：设置开关标识的图标。
3. 使用 `Switch` 标签时可能出现警告：
	1. 原文：`Use SwitchCompat from AppCompat or SwitchMaterial from Material library.`
	2. 翻译：使用 AppCompat 中的 SwitchCompat 或 Material 库中 SwitchMaterial
	3. 原因：因为 Switch 对于旧版本的 Android 有不同的外观。则使用 SwitchCompat 可以为所有 Android 版本提供一致的外观。
4. 修改布局文件 `select_button.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 复选框 -->
	<CheckBox
		android:id="@+id/select_button_CheckBox_1"
		android:text="复选框 1"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	<CheckBox
		android:id="@+id/select_button_CheckBox_2"
		android:text="复选框 2"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 复选框提示文字 -->
	<TextView
		android:id="@+id/select_button_text_CheckBox"
		android:text="复选框提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginBottom="20dp"/>
	
	<!-- 开关按钮 -->
	<!-- 因为 Switch 对于旧版本的 Android 有不同的外观。则使用 SwitchCompat 可以为所有 Android 版本提供一致的外观 -->
	<androidx.appcompat.widget.SwitchCompat
		android:id="@+id/select_button_Switch"
		android:text="开关按钮"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 开关按钮提示文字 -->
	<TextView
		android:id="@+id/select_button_text_SwitchCompat"
		android:text="开关按钮提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginBottom="20dp"/>

</LinearLayout>
```

5. 修改布局文件对应的代码文件 `SelectButtonActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import android.widget.CheckBox
import android.widget.CompoundButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SwitchCompat

class SelectButtonActivity: AppCompatActivity(), CompoundButton.OnCheckedChangeListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.select_button)
		
		// 给复选框 1 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_1).setOnCheckedChangeListener(this)
		
		// 给复选框 2 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_2).setOnCheckedChangeListener(this)
		
		// 给开关按钮设置监听器，一旦用户点击开关按钮，就触发监听器的 onCheckedChanged 方法
		findViewById<SwitchCompat>(R.id.select_button_Switch).setOnCheckedChangeListener(this)
	}
	
	/**
	 * 实现 onCheckedChanged 方法，当复选框被选择和取消勾选时会被调用
	 *
	 * 参数 1：buttonView：被操作的复选框对象
	 * 参数 2：isChecked：被选中还是被取消勾选
	 */
	override fun onCheckedChanged(buttonView: CompoundButton?, isChecked: Boolean) {
		// 根据 id 判断操作的是哪个按钮
		when(buttonView?.id){
			R.id.select_button_CheckBox_1, R.id.select_button_CheckBox_2 -> {
				findViewById<TextView>(R.id.select_button_text_CheckBox).text = String.format("您%s了%s", if (isChecked) "勾选" else "取消勾选", buttonView.text)
			}
			R.id.select_button_Switch -> {
				findViewById<TextView>(R.id.select_button_text_SwitchCompat).text = String.format("您%s了%s", if (isChecked) "开启" else "关闭", buttonView.text)
			}
		
		}
		
	}
}
```

6. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101230.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101243.png)

### ④、单选按钮 RadioButton

1. 单选按钮要在一组按钮中选择其中一项，并且不能多选，这要求有个容器确定这组按钮的范围，这个容器便是单选组 `RadioGroup`。
2. `RadioGroup` 实质上是个布局，同一组 `RadioButton` 都要放在同一个 `RadioGroup` 节点下。除了 `RadioButton`，也允许放置其他控件。
3. 单选组与线性布局相比，它们主要有以下两个区别：
	1. 单选组多了管理单选按钮的功能，而线性布局不具备该功能；
	2. 如果不指定 `orientation` 属性，那么单选组默认垂直排列，而线性布局默认水平排列；
4. 单选组的用法：
	1. 判断选中了哪个单选按钮，通常不是监听某个单选按钮，而是监听单选组的选中事件。
	2. 下面是 RadioGroup 常用的 3 个方法。
		1. `check`：选中指定资源编号的单选按钮。
		2. `getCheckedRadioButtonId`：获取选中状态单选按钮的资源编号。
		3. `setOnCheckedChangeListener`：设置单选按钮勾选变化的监听器。
5. 修改布局文件 `select_button.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 复选框 -->
	<CheckBox
		android:id="@+id/select_button_CheckBox_1"
		android:text="复选框 1"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	<CheckBox
		android:id="@+id/select_button_CheckBox_2"
		android:text="复选框 2"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 复选框提示文字 -->
	<TextView
		android:id="@+id/select_button_text_CheckBox"
		android:text="复选框提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginBottom="20dp"/>
	
	<!-- 开关按钮 -->
	<!-- 因为 Switch 对于旧版本的 Android 有不同的外观。则使用 SwitchCompat 可以为所有 Android 版本提供一致的外观 -->
	<androidx.appcompat.widget.SwitchCompat
		android:id="@+id/select_button_Switch"
		android:text="开关按钮"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 开关按钮提示文字 -->
	<TextView
		android:id="@+id/select_button_text_SwitchCompat"
		android:text="开关按钮提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginBottom="20dp"/>
	
	<!-- 单选组 -->
	<RadioGroup
		android:id="@+id/select_button_RadioGroup"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:orientation="horizontal">
		
		<RadioButton
			android:id="@+id/select_button_RadioGroup_male"
			android:text="男"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content" />
		
		<RadioButton
			android:id="@+id/select_button_RadioGroup_female"
			android:text="女"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content" />
	</RadioGroup>
	
	<!-- 单选组提示文字 -->
	<TextView
		android:id="@+id/select_button_RadioGroup_text"
		android:text="单选组提示文字"
		android:textSize="20dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

6. 修改布局文件对应的代码文件 `SelectButtonActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import android.widget.CheckBox
import android.widget.CompoundButton
import android.widget.RadioGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SwitchCompat

class SelectButtonActivity: AppCompatActivity(), CompoundButton.OnCheckedChangeListener,
	RadioGroup.OnCheckedChangeListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.select_button)
		
		// 给复选框 1 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_1).setOnCheckedChangeListener(this)
		
		// 给复选框 2 设置勾选监听器，一旦用户点击复选框，就触发监听器的 onCheckedChanged 方法
		findViewById<CheckBox>(R.id.select_button_CheckBox_2).setOnCheckedChangeListener(this)
		
		// 给开关按钮设置监听器，一旦用户点击开关按钮，就触发监听器的 onCheckedChanged 方法
		findViewById<SwitchCompat>(R.id.select_button_Switch).setOnCheckedChangeListener(this)
		
		// 给开关按钮设置监听器，一旦用户点击开关按钮，就触发监听器的 onCheckedChanged 方法
		findViewById<RadioGroup>(R.id.select_button_RadioGroup).setOnCheckedChangeListener(this)
	}
	
	/**
	 * 实现 onCheckedChanged 方法，当复选框被选择和取消勾选时会被调用
	 *
	 * 参数 1：buttonView：被操作的复选框对象
	 * 参数 2：isChecked：被选中还是被取消勾选
	 */
	override fun onCheckedChanged(buttonView: CompoundButton?, isChecked: Boolean) {
		// 根据 id 判断操作的是哪个按钮
		when(buttonView?.id){
			R.id.select_button_CheckBox_1, R.id.select_button_CheckBox_2 -> {
				findViewById<TextView>(R.id.select_button_text_CheckBox).text = String.format("您%s了%s", if (isChecked) "勾选" else "取消勾选", buttonView.text)
			}
			R.id.select_button_Switch -> {
				findViewById<TextView>(R.id.select_button_text_SwitchCompat).text = String.format("您%s了%s", if (isChecked) "开启" else "关闭", buttonView.text)
			}
		
		}
		
	}
	
	/**
	 * 实现 onCheckedChanged 方法，当单选框被选择和取消勾选时会被调用
	 *
	 * 参数 1：group：被操作的单选组
	 * 参数 2：checkedId：当前选中的单选按钮的 id
	 */
	override fun onCheckedChanged(group: RadioGroup?, checkedId: Int) {
		// 根据 id 判断操作的是哪个按钮
		when(checkedId){
			R.id.select_button_RadioGroup_male -> {
				findViewById<TextView>(R.id.select_button_RadioGroup_text).text = "当前选中的是男孩"
			}
			R.id.select_button_RadioGroup_female -> {
				findViewById<TextView>(R.id.select_button_RadioGroup_text).text = "当前选中的是女孩"
			}
		}
	}
	
}
```

7. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101402.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517101414.png)

## 3、文本输入

### ①、编辑框 EditText

1. EditText 是文本编辑框，用户可在此输入文本等信息。
2. EditText 的常用属性说明如下。
	1. inputType：指定输入的文本类型。若同时使用多种文本类型，则可使用竖线“|”把多种文本类型拼接起来。
	2. maxLength：指定文本允许输入的最大长度。
	3. hint：指定提示文本的内容。
	4. textColorHint：指定提示文本的颜色。
3. 输入类型 `inputType` 的取值说明：

| 输入类型           | 说明                             |
| -------------- | ------------------------------ |
| text           | 文本                             |
| textPassword   | 文本密码。显示时用圆点 `－` 代替             |
| number         | 整型数                            |
| numberSigned   | 带符号的数字。允许在开头带负号 `-`            |
| numberDecimal  | 带小数点的数字                        |
| numberPassword | 数字密码。显示时用圆点 `·` 代替             |
| datetime       | 时间日期格式。除了数字外，还允许输入横线、斜杆、空格、冒号  |
| date           | 日期格式。除了数字外，还允许输入横线 `-` 和斜杆 `/` |
| time           | 时间格式。除了数字外，还允许输入冒号 `:`         |

4. 创建状态列表 `edit_text_selector.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
	<!-- 正在输入（获得焦点）时显示的图片 -->
	<item android:state_focused="true" android:drawable="@drawable/qq" />
	<!-- 默认显示的图片 -->
	<item android:drawable="@drawable/shape_rounded_rectangle" />
</selector>
```

5. 创建布局文件 `edit_text.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 提示文字 -->
	<TextView
		android:text="文本输入框："
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<EditText
		android:inputType="text"
		android:hint="请输入用户名"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<EditText
		android:inputType="textPassword"
		android:hint="请输入密码"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- background：设置背景样式 -->
	<EditText
		android:inputType="text"
		android:hint="设置背景样式"
		android:textSize="20dp"
		android:background="@drawable/edit_text_selector"
		android:layout_width="match_parent"
		android:layout_height="50sp" />

</LinearLayout>
```

6. 创建布局文件对应的代码文件 `EdiTextActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class EdiTextActivity: AppCompatActivity() {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.edit_text)
	}
}
```

7. 修改 `AndroidManifest.xml` 清单文件

```xml
<!-- 注册 编辑框 EditText EdiTextActivity -->
<activity
	android:name=".EdiTextActivity"
	android:exported="true">
	<intent-filter>
		<!-- 配置为主窗口 -->
		<action android:name="android.intent.action.MAIN" />
		<category android:name="android.intent.category.LAUNCHER" />
	</intent-filter>
</activity>
```

8. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517100722.png)

### ②、焦点变更监听器

1. 编辑框点击两次后才会触发点击事件，因为第一次点击只触发焦点变更事件，第二次点击才触发点击事件。
2. 若要判断是否切换编辑框输入，应当监听焦点变更事件，而非监听点击事件。
3. 调用编辑框对象的 `setOnFocusChangeListener` 方法，即可在光标切换之时（获得光标和失去光标）触发焦点变更事件。
4. 修改布局文件 `edit_text.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 提示文字 -->
	<TextView
		android:id="@+id/edit_text_text"
		android:text="文本输入框："
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<EditText
		android:id="@+id/edit_text_name"
		android:inputType="text"
		android:hint="请输入用户名"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<EditText
		android:id="@+id/edit_text_password"
		android:inputType="textPassword"
		android:hint="请输入密码"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- background：设置背景样式 -->
	<EditText
		android:id="@+id/edit_text_background"
		android:inputType="text"
		android:hint="设置背景样式"
		android:textSize="20dp"
		android:background="@drawable/edit_text_selector"
		android:layout_width="match_parent"
		android:layout_height="50sp" />

</LinearLayout>
```

5. 创建布局文件对应的代码文件 `EdiTextActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class EdiTextActivity: AppCompatActivity(), View.OnFocusChangeListener, View.OnClickListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.edit_text)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_name).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_name).setOnClickListener(this)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_password).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_password).setOnClickListener(this)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_background).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_background).setOnClickListener(this)
	}
	
	/**
	 * 焦点变更事件的处理方法
	 *
	 * v：获得焦点的编辑框视图
	 * hasFocus：表示当前控件是否获得焦点
	 */
	override fun onFocusChange(v: View?, hasFocus: Boolean) {
		// 根据 id 判断操作的是哪个按钮
		when(v?.id){
			R.id.edit_text_name -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("用户名编辑框%s焦点", if (hasFocus) "获得" else "失去") }
			R.id.edit_text_password -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("密码编辑框%s焦点", if (hasFocus) "获得" else "失去") }
			R.id.edit_text_background -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("有背景的编辑框%s焦点", if (hasFocus) "获得" else "失去") }
		}
	}
	
	/**
	 * 编辑框比较特殊，要点击两次后才会触发点击事件，因为第一次点击只触发焦点变更事件，第二次点击才触发点击事件
	 *
	 * v：获得焦点的编辑框视图
	 */
	override fun onClick(v: View?) {
		// 根据 id 判断操作的是哪个按钮
		when(v?.id){
			R.id.edit_text_name -> { findViewById<TextView>(R.id.edit_text_text).text = "用户名编辑框被点击" }
			R.id.edit_text_password -> { findViewById<TextView>(R.id.edit_text_text).text = "密码编辑框被点击" }
			R.id.edit_text_background -> { findViewById<TextView>(R.id.edit_text_text).text = "有背景的编辑框被点击" }
		}
	}
}
```

6. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517100752.png)

### ③、文本变化监听器

1. 调用编辑框对象的 `addTextChangedListener` 方法即可注册文本监听器。
2. 文本监听器的接口名称为 `TextWatcher`，该接口提供了3个监控方法，具体说明如下。
	1. `beforeTextChanged`：在文本改变之前触发。
	2. `onTextChanged`：在文本改变过程中触发。
	3. `afterTextChanged`：在文本改变之后触发。
3. 修改布局文件 `edit_text.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<TextView
		android:id="@+id/edit_text_text_name"
		android:text="用户名输入框"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/edit_text_text_password"
		android:text="密码输入框"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/edit_text_text_background"
		android:text="有背景的输入框"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 提示文字 -->
	<TextView
		android:id="@+id/edit_text_text"
		android:text="文本输入框："
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<EditText
		android:id="@+id/edit_text_name"
		android:inputType="text"
		android:hint="请输入用户名"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<EditText
		android:id="@+id/edit_text_password"
		android:inputType="textPassword"
		android:hint="请输入密码"
		android:textSize="20dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- background：设置背景样式 -->
	<EditText
		android:id="@+id/edit_text_background"
		android:inputType="text"
		android:hint="设置背景样式"
		android:textSize="20dp"
		android:background="@drawable/edit_text_selector"
		android:layout_width="match_parent"
		android:layout_height="50sp" />

</LinearLayout>
```

4. 创建布局文件对应的代码文件 `EdiTextActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.widget.addTextChangedListener

class EdiTextActivity: AppCompatActivity(), View.OnFocusChangeListener, View.OnClickListener{
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.edit_text)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_name).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_name).setOnClickListener(this)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_password).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_password).setOnClickListener(this)
		
		// 给用户名编辑框注册一个焦点变化监听器，一旦焦点发生变化，就触发监听器的 onFocusChange 方法
		findViewById<EditText>(R.id.edit_text_background).onFocusChangeListener = this
		// 给用户名编辑框注册一个点击监听器，连续点击两次后，就触发监听器的 onClick 方法
		findViewById<EditText>(R.id.edit_text_background).setOnClickListener(this)
		
		
		// 给用户名编辑框注册一个文本变化监听器，一旦内容文本发生变化，就触发监听器的 beforeTextChanged、onTextChanged、afterTextChanged 方法
		// 这里使用的匿名内部类，因为这三个方法上并没有传递标识标签的属性，所以多个一起监听的话我不知道怎么判断了
		findViewById<EditText>(R.id.edit_text_name).addTextChangedListener(object: TextWatcher{
			/**
			 * 文本变化监听器，在文本改变之前触发
			 *
			 * s：修改之前的文字
			 * start：字符串中即将发生修改的位置
			 * count：字符串中即将被修改的文字的长度。如果是新增的话则为 0
			 * after：被修改的文字修改之后的长度。如果是删除的话则为 0
			 */
			override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
				/**
				 * 可以通过参数 s 来获取 EditText 的文本内容
				 * 如果有多个 EditText，可以通过判断 s 所属的 EditText 来判断是哪个 TextView 的文本发生了变化
				 */

			}
			
			/**
			 * 文本变化监听器，在文本改变过程中触发
			 *
			 * s：改变后的字符串
			 * start：有变动的字符串的序号
			 * before：被改变的字符串长度，如果是新增则为 0
			 * count：添加的字符串长度，如果是删除则为 0
			 */
			override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
			
			}
			
			/**
			 * 文本变化监听器，在文本改变之后触发
			 *
			 * s: 修改后的文字
			 */
			override fun afterTextChanged(s: Editable?) {
				findViewById<TextView>(R.id.edit_text_text_name).text = s.toString()
			}
		})
		// 使用 lambda 表达式简化
		findViewById<EditText>(R.id.edit_text_password).addTextChangedListener{
			findViewById<TextView>(R.id.edit_text_text_password).text = it.toString()
		}
		// 使用 lambda 表达式简化
		findViewById<EditText>(R.id.edit_text_background).addTextChangedListener{
			findViewById<TextView>(R.id.edit_text_text_background).text = it.toString()
		}
	}
	
	/**
	 * 焦点变更事件的处理方法
	 *
	 * v：获得焦点的编辑框视图
	 * hasFocus：表示当前控件是否获得焦点
	 */
	override fun onFocusChange(v: View?, hasFocus: Boolean) {
		// 根据 id 判断操作的是哪个按钮
		when(v?.id){
			R.id.edit_text_name -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("用户名编辑框%s焦点", if (hasFocus) "获得" else "失去") }
			R.id.edit_text_password -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("密码编辑框%s焦点", if (hasFocus) "获得" else "失去") }
			R.id.edit_text_background -> { findViewById<TextView>(R.id.edit_text_text).text = String.format("有背景的编辑框%s焦点", if (hasFocus) "获得" else "失去") }
		}
	}
	
	/**
	 * 编辑框比较特殊，要点击两次后才会触发点击事件，因为第一次点击只触发焦点变更事件，第二次点击才触发点击事件
	 *
	 * v：获得焦点的编辑框视图
	 */
	override fun onClick(v: View?) {
		// 根据 id 判断操作的是哪个按钮
		when(v?.id){
			R.id.edit_text_name -> { findViewById<TextView>(R.id.edit_text_text).text = "用户名编辑框被点击" }
			R.id.edit_text_password -> { findViewById<TextView>(R.id.edit_text_text).text = "密码编辑框被点击" }
			R.id.edit_text_background -> { findViewById<TextView>(R.id.edit_text_text).text = "有背景的编辑框被点击" }
		}
	}

	
}
```

5. 效果

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517100408.png)
![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517100434.png)

## 4、对话框

### ①、提醒对话框 AlertDialog

1. AlertDialog 可以完成常见的交互操作，例如提示、确认、选择等功能。
2. AlertDialog 借助建造器 `AlertDialog.Builder` 才能完成参数设置，AlertDialog.Builder 的常用方法说明如下。
	1. `setIcon`：设置对话框的标题图标。
	2. `setTitle`：设置对话框的标题文本。
	3. `setMessage`：设置对话框的内容文本。
	4. `setPositiveButton`：设置肯定按钮的信息，包括按钮文本和点击监听器。
	5. `setNegativeButton`：设置否定按钮的信息，包括按钮文本和点击监听器。
	6. `setNeutralButton`：设置中性按钮的信息，包括按钮文本和点击监听器。
3. 调用建造器的 `create` 方法生成对话框实例，再调用对话框实例的 `show` 方法，在页面上弹出提醒对话框。
4. 创建布局文件 `dialog_box.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/dialog_box_btn"
		android:text="点击弹出对话框"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text"
		android:text="提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

5. 创建布局文件对应的代码文件 `DialogBoxAlertDialogActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.app.AlertDialog
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class DialogBoxAlertDialogActivity: AppCompatActivity() {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.dialog_box)
		
		// 给按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn).setOnClickListener {
			// 创建提醒对话框的建造器
			val builder = AlertDialog.Builder(this)
			
			// 设置对话框的标题文本
			builder.setTitle("提醒对话框")
			// 设置对话框的内容文本
			builder.setMessage("提醒对话框的内容")
			
			/**
			 * 设置对话框的肯定按钮文本及其点击监听器
			 *
			 * dialog 是一个 AlertDialog.Builder 对象，它用于创建一个提醒对话框。
			 * which 是一个整数值，表示用户点击的按钮的索引。
			 *
			 * 在这里，我们设置了两个按钮：确定和取消。
			 * 当用户点击确定按钮时，which 的值为 DialogInterface.BUTTON_POSITIVE（-1），当
			 * 用户点击取消按钮时，which 的值为 DialogInterface.BUTTON_NEGATIVE（-2）
			 */
			builder.setPositiveButton("确定"){ dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了确定"
			}
			
			// 设置对话框的否定按钮文本及其点击监听器
			builder.setNegativeButton("取消"){dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了取消"
			}
			
			// 根据建造器构建提醒对话框对象
			val alertDialog = builder.create()
			
			// 显示提醒对话框
			alertDialog.show()
		}
		
		
	}
}
```

6. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 选择按钮 SelectButtonActivity -->
		<activity
			android:name=".SelectButtonActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 编辑框 EditText EdiTextActivity -->
		<activity
			android:name=".EdiTextActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 对话框 DialogBoxAlertDialogActivity -->
		<activity
			android:name=".DialogBoxAlertDialogActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口 -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
		
	</application>

</manifest>
```

7. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517095848.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517095926.png)

### ②、日期对话框 DatePickerDialog

1. 日期选择器 DatePicker 可以让用户选择具体的年月日。
2. 但 DatePicker 并非弹窗模式，而是在当前页面占据一块区域，并且不会自动关闭。
3. DatePickerDialog 相当于在 AlertDialog 上装载了 DatePicker，日期选择事件则由监听器 `OnDateSetListener` 负责响应，在该监听器的 `onDateSet` 方法中，开发者获取用户选择的具体日期，再做后续处理。
4. 需要注意的是 `onDateSet` 的月份参数，他的起始值不是 1 而是 0；也就是说一月份对应的参数值为 0，十二月份对应的参数值为 11
5. 修改布局文件 `dialog_box.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 提醒对话框弹出按钮 -->
	<Button
		android:id="@+id/dialog_box_btn"
		android:text="点击弹出对话框"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text"
		android:text="提醒对话框提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 日期对话框弹出按钮 -->
	<Button
		android:id="@+id/dialog_box_btn_DatePickerDialog"
		android:text="点击弹出对话框"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text_DatePickerDialog"
		android:text="日期对话框提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

6. 修改布局文件对应的代码文件 `DialogBoxAlertDialogActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.app.AlertDialog
import android.app.DatePickerDialog
import android.icu.util.Calendar
import android.os.Bundle
import android.widget.Button
import android.widget.DatePicker
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class DialogBoxAlertDialogActivity: AppCompatActivity(), DatePickerDialog.OnDateSetListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.dialog_box)
		
		// 给提醒对话框弹出按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn).setOnClickListener {
			// 创建提醒对话框的建造器
			val builder = AlertDialog.Builder(this)
			
			// 设置对话框的标题文本
			builder.setTitle("提醒对话框")
			// 设置对话框的内容文本
			builder.setMessage("提醒对话框的内容")
			
			/**
			 * 设置对话框的肯定按钮文本及其点击监听器
			 *
			 * dialog 是一个 AlertDialog.Builder 对象，它用于创建一个提醒对话框。
			 * which 是一个整数值，表示用户点击的按钮的索引。
			 *
			 * 在这里，我们设置了两个按钮：确定和取消。
			 * 当用户点击确定按钮时，which 的值为 DialogInterface.BUTTON_POSITIVE（-1），当
			 * 用户点击取消按钮时，which 的值为 DialogInterface.BUTTON_NEGATIVE（-2）
			 */
			builder.setPositiveButton("确定"){ dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了确定"
			}
			
			// 设置对话框的否定按钮文本及其点击监听器
			builder.setNegativeButton("取消"){dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了取消"
			}
			
			// 根据建造器构建提醒对话框对象
			val alertDialog = builder.create()
			
			// 显示提醒对话框
			alertDialog.show()
		}
		
		// 给日期对话框弹出按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn_DatePickerDialog).setOnClickListener {
			// 获取日历的一个实例，里面包含了当前的年月日
			val calendar = Calendar.getInstance()
			/**
			 * 构建一个日期对话框，该对话框已经集成了日期选择器。
			 *
			 * 参数 1：context，上下文对象，Activity
			 * 参数 2：日期监听器，需 Activity 实现 DatePickerDialog.OnDateSetListener 接口 的 onDateSet 方法
			 * 参数 3：年
			 * 参数 4：月
			 * 参数 5：日
			 */
			val dialog = DatePickerDialog(
				this, this,
				calendar[Calendar.YEAR],
				calendar[Calendar.MONTH],
				calendar[Calendar.DAY_OF_MONTH]
			)
			
			// 显示日期对话框
			dialog.show()
		}
		
	}
	
	/**
	 * 一旦点击日期对话框上的确定按钮，就会触发监听器的onDateSet方法
	 *
	 * view：由哪个日期对话框 DatePickerDialog 触发
	 * year：年
	 * month：月
	 * dayOfMonth：日
	 */
	override fun onDateSet(view: DatePicker?, year: Int, month: Int, dayOfMonth: Int) {
		val tip = "选择的日期是：$year 年 ${month + 1} 月 $dayOfMonth 日"
		findViewById<TextView>(R.id.dialog_box_text_DatePickerDialog).text = tip
	}
	
}
```

7. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517105509.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517105517.png)

### ③、时间对话框 TimePickerDialog

1. 时间选择器 TimePicker 可以让用户选择具体的小时和分钟
2. TimePickerDialog 的用法类似 DatePickerDialog，不同之处有两个：
	1. 构造方法传的是当前的小时与分钟，最后一个参数表示是否采取二十四小时制，一般传 true，表示小时的数值范围为 0～23；若为 false 则表示采取十二小时制。
	2. 时间选择监听器为 `OnTimeSetListener`，对应需要实现 `onTimeSet` 方法，在该方法中可获得用户选择的小时和分钟。
3. 修改布局文件 `dialog_box.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 提醒对话框弹出按钮 -->
	<Button
		android:id="@+id/dialog_box_btn"
		android:text="点击弹出提醒对话框"
		android:textSize="28dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text"
		android:text="提醒对话框提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 日期对话框弹出按钮 -->
	<Button
		android:id="@+id/dialog_box_btn_DatePickerDialog"
		android:text="点击弹出日期对话框"
		android:textSize="28dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text_DatePickerDialog"
		android:text="日期对话框提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<!-- 时间对话框弹出按钮 -->
	<Button
		android:id="@+id/dialog_box_btn_TimePickerDialog"
		android:text="点击弹出时间对话框"
		android:textSize="28dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<TextView
		android:id="@+id/dialog_box_text_TimePickerDialog"
		android:text="时间对话框提示文字"
		android:textSize="40dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

4. 修改布局文件对应的代码文件 `DialogBoxAlertDialogActivity`

```Kotlin
package com.yuehai.intermediatecontrols

import android.app.AlertDialog
import android.app.DatePickerDialog
import android.app.TimePickerDialog
import android.icu.util.Calendar
import android.os.Bundle
import android.widget.Button
import android.widget.DatePicker
import android.widget.TextView
import android.widget.TimePicker
import androidx.appcompat.app.AppCompatActivity

class DialogBoxAlertDialogActivity: AppCompatActivity(), DatePickerDialog.OnDateSetListener,
	TimePickerDialog.OnTimeSetListener {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.dialog_box)
		
		// 给提醒对话框弹出按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn).setOnClickListener {
			// 创建提醒对话框的建造器
			val builder = AlertDialog.Builder(this)
			
			// 设置对话框的标题文本
			builder.setTitle("提醒对话框")
			// 设置对话框的内容文本
			builder.setMessage("提醒对话框的内容")
			
			/**
			 * 设置对话框的肯定按钮文本及其点击监听器
			 *
			 * dialog 是一个 AlertDialog.Builder 对象，它用于创建一个提醒对话框。
			 * which 是一个整数值，表示用户点击的按钮的索引。
			 *
			 * 在这里，我们设置了两个按钮：确定和取消。
			 * 当用户点击确定按钮时，which 的值为 DialogInterface.BUTTON_POSITIVE（-1），当
			 * 用户点击取消按钮时，which 的值为 DialogInterface.BUTTON_NEGATIVE（-2）
			 */
			builder.setPositiveButton("确定"){ dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了确定"
			}
			
			// 设置对话框的否定按钮文本及其点击监听器
			builder.setNegativeButton("取消"){dialog, which ->
				findViewById<TextView>(R.id.dialog_box_text).text = "点击了取消"
			}
			
			// 根据建造器构建提醒对话框对象
			val alertDialog = builder.create()
			
			// 显示提醒对话框
			alertDialog.show()
		}
		
		// 给日期对话框弹出按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn_DatePickerDialog).setOnClickListener {
			// 获取日历的一个实例，里面包含了当前的年月日
			val calendar = Calendar.getInstance()
			/**
			 * 构建一个日期对话框，该对话框已经集成了日期选择器。
			 *
			 * 参数 1：context，上下文对象，Activity
			 * 参数 2：日期监听器，需 Activity 实现 DatePickerDialog.OnDateSetListener 接口 的 onDateSet 方法
			 * 参数 3：年
			 * 参数 4：月
			 * 参数 5：日
			 */
			val dialog = DatePickerDialog(
				this, this,
				calendar[Calendar.YEAR],
				calendar[Calendar.MONTH],
				calendar[Calendar.DAY_OF_MONTH]
			)
			
			// 显示日期对话框
			dialog.show()
		}
		
		// 给时间对话框弹出按钮设置点击事件
		findViewById<Button>(R.id.dialog_box_btn_TimePickerDialog).setOnClickListener {
			// 获取日历的一个实例，里面包含了当前的时分秒
			val calendar = Calendar.getInstance()
			/**
			 * 构建一个时间对话框，该对话框已经集成了时间选择器。
			 *
			 * 参数 1：context，上下文对象，Activity
			 * 参数 2：时间监听器，需 Activity 实现 TimePickerDialog.OnTimeSetListener 接口 的 onTimeSet 方法
			 * 参数 3：时
			 * 参数 4：分
			 * 参数 5：true，表示 24 小时制；false 表示采取 12 小时制
			 */
			val dialog = TimePickerDialog(
				this, this,
				calendar[Calendar.HOUR_OF_DAY],
				calendar[Calendar.MINUTE],
				true
			)
			
			// 显示时间对话框
			dialog.show()
		}
		
	}
	
	/**
	 * 一旦点击日期对话框上的确定按钮，就会触发监听器的 onDateSet 方法
	 *
	 * view：由哪个日期对话框 DatePickerDialog 触发
	 * year：年
	 * month：月
	 * dayOfMonth：日
	 */
	override fun onDateSet(view: DatePicker?, year: Int, month: Int, dayOfMonth: Int) {
		val tip = "选择的日期是：$year 年 ${month + 1} 月 $dayOfMonth 日"
		findViewById<TextView>(R.id.dialog_box_text_DatePickerDialog).text = tip
	}
	
	/**
	 * 一旦点击时间对话框上的确定按钮，就会触发监听器的 onTimeSet 方法
	 *
	 * view：由哪个时间对话框 TimePickerDialog 触发
	 * hourOfDay：时
	 * minute：分
	 */
	override fun onTimeSet(view: TimePicker?, hourOfDay: Int, minute: Int) {
		val tip = "选择的时间是：$hourOfDay 时 $minute 分"
		findViewById<TextView>(R.id.dialog_box_text_TimePickerDialog).text = tip
	}
	
}
```

5. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517111627.png)

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230517111634.png)

# 五、`Android` 高级控件

## 1、下拉列表

### ①、下拉框 Spinner

1. Spinner 是下拉框控件，它用于从一串列表中选择某项。
2. 下拉列表的展示方式有两种，
	1. `dropdown`：在当前下拉框的正下方弹出列表框，下拉菜单风格（默认）
	2. `dialog`：在页面中部弹出列表对话框，对话框风格
3. 分别对应 `SpinnerMode` 属性设置为 `dropdown` 或者 `dialog`

![|533](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230506084743.png)

4. Spinner 组件一共有两个，一个是本身的 `Spinner`，一个是 `android.support.v7.widget.AppCompatSpinner`
	1. 两者的区别在于 v7 内的 Spinner 是兼容低版本的
	2. Spinner 在高版本中才能使用的方法，换了 v7 下的 Spinner 后可以一直兼容到2.1 (v7 兼容到 api7)
	3. 除此之外两者的使用没有其他差别
5. 这里有用到适配器，下面会讲
6. 创建布局文件 `spinner_dropdown.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<TextView
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:text="下拉模式的列表框"
		android:textSize="20sp"/>

	<!--
		下拉列表
		android:spinnerMode：列表框的模式，有两个可选值
			dropdown 在当前下拉框的正下方弹出列表框，下拉菜单风格（默认）
			dialog 在页面中部弹出列表对话框，对话框风格
	 -->
	<Spinner
		android:id="@+id/spinner_dropdown"
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:spinnerMode="dropdown"/>

</LinearLayout>
```

7. 创建条目布局文件 `spinner_dropdown_item.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="200dp"
	android:layout_height="40dp"
	android:gravity="center"
	android:textSize="30sp"
	android:background="@color/purple_200"
	android:textColor="@color/teal_700"
	android:text="月海">
	
</TextView>
```

8. 创建布局文件对应的代码文件 Activity `SpinnerDropdownActivity`

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Spinner
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity


class SpinnerDropdownActivity: AppCompatActivity(), AdapterView.OnItemSelectedListener {

    // 定义下拉列表需要显示的文本数组
    private val starArray = arrayOf("水星", "金星", "地球", "火星", "木星", "土星")
    // 定义下拉列表对象，等待赋值
    private var spinnerDropdown: Spinner? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.spinner_dropdown)

        // 获取下拉列表对象，并赋值
        spinnerDropdown = findViewById<Spinner>(R.id.spinner_dropdown)
        /**
         * 声明一个数组适配器
         * 第一个参数：上下文环境
         * 第二个参数：当前列表项加载的布局文件
         * 第三个参数：数据源
         */
        val starAdapter: ArrayAdapter<String?> = ArrayAdapter<String?>(this, R.layout.spinner_dropdown_item, starArray)
        // 传入适配器实例
        spinnerDropdown!!.adapter = starAdapter

        // 设置默认为第一项
        spinnerDropdown!!.setSelection(0)
        // 设置监听器，一旦用户选择了某一项，则触发 onItemSelected 方法
        spinnerDropdown!!.onItemSelectedListener = this
    }

    // 选择后触发
    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.i("下拉列表", "选择后触发")
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "你选择的是" + starArray[position], Toast.LENGTH_SHORT).show();
    }

    // 当下拉列表中的选项被取消选择时，该方法将被调用。例如，当触摸被激活或适配器变为空时，选择可能会消失
    override fun onNothingSelected(parent: AdapterView<*>?) {
        Log.i("下拉列表", "当下拉列表中的选项被取消选择时触发")
    }
}
```

9. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

10. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508111847.png)

### ②、适配器 Adapte

1. `Adapter` 是用于连接后端数据和前端显示的适配器接口，是数据 data 和 UI（View）之间一个重要的纽带
2. 在常见的 View(ListView、GridView) 等地方都需要用到 Adapter
3. 适配器负责从数据集合中取出对应的数据显示到条目布局上
4. 如下图直观的表达了 Data、Adapter、View 三者的关系

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230504164626.png)

### ③、适配器 Adapte 继承结构

1. Adapter接口的组成中最常用的有以下几个：
2. `BaseAdapter` 是所有 Adapter 类的父类，所有的 Adapter 类的实现都是基于 BaseAdapter 的基础上的
3. `ArrayAdapter` 支持泛型操作，最为简单，但是只能展示一行字。
4. `SimpleAdapter` 虽然名称为 simple，但是用法功能还是很强大的，基本上我们在敲代码时都要与这个打交道

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230504164732.png)

### ③、复用 convertVie

1. 试想一个场景：若把所有数据集合的信息都加载到 ListView 上显示，ListView 要为每个数据都创建一个视图，那么会占用非常多的内存
2. 为了节省空间和时间，ListView 不会为每一个数据创建一个视图，而是采用了 Recycler 组件，用于回收和复用 View
3. 当屏幕需显示 x 个 Item 时，那么 ListView 会创建 x+1个视图；当第1个 Item 离开屏幕时，此 Item 的 View 被回收至缓存，入屏的 Item 的 View 会优先从该缓存中获取
4. 注：只有 Item 完全离开屏幕后才可复用，这也是为什么 ListView 要创建比屏幕需显示视图多 1 个的原因：缓冲显示视图
5. 即：第 1 个 Item 离开屏幕是有过程的，会有 1 个第 1 个 Item 的下半部分和第 8 个 Item 上半部分同时在屏幕中显示的状态，此时仍无法使用缓存的 View，只能继续用新创建的视图 View
6. 实例演示，设：屏幕只能显示 5 个 Item，那么 ListView 只会创建（5+1）个 Item 的视图；当第 1 个 Item 完全离开屏幕后才会回收至缓存从而复用（用于显示第 7 个 Item）

![|685](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230504165416.png)

### ④、数组适配器 ArrayAdapte

1. 最简单的适配器，用于绑定格式单一的数据，数据源可以是集合或者数组
2. 运用数组适配器分成下列步骤：
	1. 编写列表项的 XML 文件，内部布局只有一个 `TextView`、`ListView` 等标签
	2. 调用 `ArrayAdapter` 的构造方法
		1. 第一个参数：上下文环境
		2. 第二个参数：当前列表项加载的布局文件
		3. 第三个参数：数据源
	3. 调用下拉框控件的 setAdapter 方法，传入第二步得到的适配器实例

### ⑤、简单适配器 SimpleAdapter

#### Ⅰ、说明

1. 数组适配器简单但是只能用于文本列表，如果想要加上图标之类的，则需要用到简单适配器 `SimpleAdapter` 了
2. `SimpleAdapter` 类是用来处理 `ListView` 显示数据的，这个类可以将任何自定义的 xml 布局文件作为列表项来使用
3. SimpleAdapter构造方法的原型为：`public SimpleAdapter ( Context context,List<?extends Map<String,?>> data,int resource,String[] form,int[] to)`
	1. `context`：SimpleAdapter 关联的 View 的运行环境；上下文环境
	2. `data`：一个 Map 组成的 List。列表种的每个条目对应列表中的一行，每个 Map 中应该包含 from 参数中指定的键
	3. `resource`：定义列表项的布局文件的资源 id
	4. `from`：被添加到 Map 映射上的键名
	5. `to`：将绑定数据的视图的 Id 和 from 参数对应；from 与 to 一一对应，适配器绑定数据

#### Ⅱ、代码例子

1. 创建布局文件 `spinner_dropdown_simple_adapter.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<TextView
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:text="简单适配器 - 下拉模式的列表框"
		android:textSize="20sp"/>
	
	<!--
		下拉列表
		android:spinnerMode：列表框的模式，有两个可选值
			dropdown 在当前下拉框的正下方弹出列表框，下拉菜单风格（默认）
			dialog 在页面中部弹出列表对话框，对话框风格
	 -->
	<Spinner
		android:id="@+id/spinner_dropdown_simple_adapter"
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:spinnerMode="dropdown"/>

</LinearLayout>
```

2. 创建条目布局文件 `spinner_dropdown_simple_adapter_item.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:orientation="horizontal"
	android:gravity="center">
	
	<ImageView
		android:id="@+id/iv_icon"
		android:layout_width="50dp"
		android:layout_height="50dp"
		android:src="@drawable/qq"/>
	
	<TextView
		android:id="@+id/tv_name"
		android:layout_width="match_parent"
		android:layout_height="50dp"
		android:gravity="center"
		android:textColor="@color/white"
		android:background="@color/purple_700"
		android:textSize="20sp"
		android:text="地球" />

</LinearLayout>
```

3. 创建布局文件对应的代码文件 Activity `SpinnerDropdownSimpleAdapterActivity`

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.SimpleAdapter
import android.widget.Spinner
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity


class SpinnerDropdownSimpleAdapterActivity: AppCompatActivity(), AdapterView.OnItemSelectedListener {

    // 定义下拉列表需要显示的行星名称数组
    private val starArray = arrayOf("水星", "金星", "地球", "火星", "木星", "土星")
    // 定义下拉列表需要显示的行星图标数组
    private val iconArray = arrayOf(
        R.drawable.qq, R.drawable.qq, R.drawable.qq, R.drawable.qq,
        R.drawable.wcat, R.drawable.wcat
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.spinner_dropdown_simple_adapter)
5
        // 声明一个映射对象的列表，用于保存行星的图标与名称配对信息
        val list: MutableList<Map<String, Any?>> = ArrayList()
        // iconArray 是行星的图标数组，starArray 是行星的名称数组
        // 遍历名称，取出对应索引的名称和图标，配对以放入映射对象的列表
        for (index in starArray.indices){
            val item: MutableMap<String, Any?> = HashMap()
            item["icon"] = iconArray[index]
            item["name"] = starArray[index]
            list.add(item)
        }

        /**
         * 声明一个下拉列表的简单适配器，其中指定了图标与文本两组数据
         * SimpleAdapter(Context context, List<? extends Map<String, ?>> data, int resource, String[] from, int[] to)
         * 第一个参数 context：SimpleAdapter 关联的 View 的运行环境；上下文环境
         * 第二个参数 data：  一个 Map 组成的 List。列表种的每个条目对应列表中的一行，每个 Map 中应该包含 from 参数中指定的键
         * 第三个参数 resource：定义列表项的布局文件的资源 id
         * 第四个参数 from：  被添加到 Map 映射上的键名
         * 第五个参数 to：    将绑定数据的视图的 Id 和 from 参数对应；from 与 to 一一对应，适配器绑定数据
         */
        val startAdapter = SimpleAdapter(
            this,
            list,
            R.layout.spinner_dropdown_simple_adapter_item,
            arrayOf<String>("icon", "name"),
            intArrayOf(R.id.iv_icon, R.id.tv_name)
        )
        // 获取下拉列表对象
        val spIcon = findViewById<Spinner>(R.id.spinner_dropdown_simple_adapter)
        // 传入适配器实例
        spIcon.adapter = startAdapter
        // 设置默认为第一项
        spIcon.setSelection(0)
        // 设置监听器，一旦用户选择了某一项，则触发 onItemSelected 方法
        spIcon.onItemSelectedListener = this
    }

    // 选择后触发
    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.i("下拉列表", "选择后触发")
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "你选择的是" + starArray[position], Toast.LENGTH_SHORT).show();
    }

    // 当下拉列表中的选项被取消选择时，该方法将被调用。例如，当触摸被激活或适配器变为空时，选择可能会消失
    override fun onNothingSelected(parent: AdapterView<*>?) {
        Log.i("下拉列表", "当下拉列表中的选项被取消选择时触发")
    }
}
```

4. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

5. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508111742.png)

### ⑥、基本适配器 BaseAdapter

#### Ⅰ、说明

1. BaseAdapter 是一种适应性更强的基本适配器
2. 上面的 ArrayAdapter 和 SimpleAdapter 都是比较具体的实现类，想要有更多的扩展，必然是需要自定义适配器的
3. 我们可以通过继承 BaseAdapter，根据业务自定义数据适配器。

#### Ⅱ、代码例子

1. 创建布局文件 `spinner_dropdown_base_adapter.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<TextView
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:text="基本适配器 - 对话框风格的列表框"
		android:textSize="20sp"/>
	
	<!--
		下拉列表
		android:spinnerMode：列表框的模式，有两个可选值
			dropdown 在当前下拉框的正下方弹出列表框，下拉菜单风格（默认）
			dialog 在页面中部弹出列表对话框，对话框风格
	 -->
	<Spinner
		android:id="@+id/spinner_dialog_base_adapter"
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:spinnerMode="dialog"/>

</LinearLayout>
```

2. 创建条目布局文件 `spinner_dropdown_base_adapter_itme.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="horizontal">
	
	<!-- 这是显示行星图片的图像视图 -->
	<ImageView
		android:id="@+id/iv_icon"
		android:layout_width="0dp"
		android:layout_height="80dp"
		android:layout_weight="1"
		android:src="@drawable/qq" />
	
	<LinearLayout
		android:layout_width="0dp"
		android:layout_height="match_parent"
		android:layout_weight="3"
		android:orientation="vertical">
		
		<!-- 这是显示行星名称的文本视图 -->
		<TextView
			android:id="@+id/tv_name"
			android:layout_width="match_parent"
			android:layout_height="wrap_content"
			android:gravity="start|center"
			android:textColor="@color/white"
			android:background="@color/purple_700"
			android:textSize="20sp"
			android:text="地球" />
		
		<!-- 这是显示行星描述的文本视图 -->
		<TextView
			android:id="@+id/tv_desc"
			android:layout_width="match_parent"
			android:layout_height="wrap_content"
			android:gravity="start|center"
			android:textColor="@color/white"
			android:background="@color/purple_200"
			android:textSize="13sp"
			android:text="地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里" />
	</LinearLayout>

</LinearLayout>
```

3. 创建行星实体数据类 `Planet`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter.bean

/**
 * 行星实体数据类
 */
data class Planet(
    // 行星名称
    var name: String,
    // 行星图标
    var image: Int,
    // 行星描述
    var desc: String
)
```

4. 定义一个 ViewHolder，用来标记控件 `PlanetViewHolder`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter.bean.viewHolder

import android.widget.ImageView
import android.widget.TextView

/**
 * 定义一个 ViewHolder，用来标记控件
 */
class PlanetViewHolder {

    // 行星名称
    var name: TextView? = null
    // 行星图标
    var image: ImageView? = null
    // 行星描述
    var desc: TextView? = null

}
```

5. <font color="#ff0000">创建自定义适配器</font> `PlanetBaseAdapter`，<font color="#ff0000">实现基本适配器</font> `BaseAdapter`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import com.yuehai.advancedcontrols.R
import com.yuehai.advancedcontrols.bean.Planet
import com.yuehai.advancedcontrols.bean.viewHolder.PlanetViewHolder

/**
 * 行星的自定义适配器
 */
class PlanetBaseAdapter(
    // 上下文环境
    private var context: Context,
    // 所需数据
    private var data: MutableList<Planet>
): BaseAdapter() {

    /**
     * getCount : 要绑定的条目的数目，比如格子的数量
     * 该方法如果返回 0 的话就不调会下面 getView(.....)方法，如果大于 0 就会调用
     *
     * 可以简单的理解为，adapter 先从 getCount 里确定数量，然后循环执行 getView 方法将条目一个一个绘制出来
     * 所以必须重写的是 getCount 和 getView 方法
     * 而 getItem 和 getItemId 是调用某些函数才会触发的方法，如果不需要使用可以暂时不修改
     */
    override fun getCount(): Int {
        // 将 getCount 的返回值修改为数据源的长度，要显示几个条目，就传入多长的数据源就可以了
        return data.size
    }

    /**
     * getView : 获取该条目要显示的界面
     *
     * 参数 1：表示当前索引
     * 参数 2：缓存区
     *      这个 convertView 就是最关键的部分
     *      原理上讲，当 ListView 滑动的过程中，会有 item 被滑出屏幕，而不再被使用，
     *      这时候 Android 会回收这个条目的 view，这个 view 也就是这里的 convertView
     *      也就是为了不浪费内存重新调用第一个地址，就是被划上去的那个 View
     *      如果不使用 convertView，当 item1 被移除屏幕的时候，会重新 new 一个 View 给新显示的 item_new
     *      而如果使用了 convertView，我们可以复用它 这样就省去了 new View 的大量开销
     * 参数 3：每个 ItemView 里面的容器  返回的 View 直接添加到容器中来
     *
     * 返回值：就是每个 ItemView 要显示的内容
     */
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {

        // 定义视图对象，等待赋值
        val inflater = LayoutInflater.from(context)
        // convertView 不能重新赋值，创建一个局部变量来保存返回的 View
        val view: View
        // 实例化类 PlanetViewHolder，用来标记控件
        var holder = PlanetViewHolder()

        /**
         * 在 getView 方法中，Adapter 先从 xml 中用 inflate 方法创建 view 对象，然后在这个 view 找到每一个控件
         * 这里的 findViewById 操作是一个树查找过程，也是一个耗时的操作，所以这里也需要优化
         * 使用 viewHolder，把每一个控件都放在 Holder 中，当第一次创建 convertView 对象时，把这些控件找出来
         * 然后用 convertView 的 setTag 将 viewHolder 设置到 Tag 中，以便系统第二次绘制 ListView 时从 Tag 中取出
         * 当第二次重用 convertView 时，只需从 convertView 中 getTag 取出来就可以
         */
        if (convertView == null){
            // 根据布局文件 spinner_dialog_base_adapter_item.xml 生成转换视图对象
            view = inflater.inflate(R.layout.spinner_dialog_base_adapter_item, null)

            // 给对象 PlanetViewHolder 的属性赋值
            holder.name = view.findViewById(R.id.tv_name)
            holder.image = view.findViewById(R.id.iv_icon)
            holder.desc = view.findViewById(R.id.tv_desc)

            // 将视图持有者保存到转换视图当中，以便复用
            view.tag = holder
        } else {
            // convertView 不为空，进行复用
            holder = convertView.tag as PlanetViewHolder
            view = convertView
        }

        // 给视图设置数据
        holder.name?.text = data[position].name
        holder.image?.setImageResource(data[position].image)
        holder.desc?.text = data[position].desc

        // 返回 view 对象
        return view
    }

    /**
     * getItem : 根据一个索引（位置）获得该位置的对象
     */
    override fun getItem(position: Int): Any {
        return data[position]
    }

    /**
     * getItemId : 获取条目的id
     */
    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

}
```

6. 创建布局文件对应的代码文件 Activity `SpinnerDropdownSimpleAdapterActivity

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.Spinner
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.advancedcontrols.bean.Planet
import com.yuehai.advancedcontrols.ui.adapter.PlanetBaseAdapter

class SpinnerDropdownBaseAdapter: AppCompatActivity(), AdapterView.OnItemSelectedListener {

    // 定义下拉列表需要显示的行星数据集合
    private val planetList: MutableList<Planet> = mutableListOf(
        Planet("水星", R.drawable.qq, "水星是太阳系八大行星最内侧也是最小的一颗行星，也是离太阳最近的行星"),
        Planet("金星", R.drawable.wcat, "金星是太阳系八大行星之一，排行第二，距离太阳0.725天文单位"),
        Planet("地球", R.drawable.qq, "地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里"),
        Planet("火星", R.drawable.wcat, "火星是太阳系八大行星之一，排行第四，属于类地行星，直径约为地球的53%"),
        Planet("木星", R.drawable.qq, "木星是太阳系八大行星中体积最大、自转最快的行星，排行第五。它的质量为太阳的千分之一，但为太阳系中其它七大行星质量总和的2.5倍"),
        Planet("土星", R.drawable.wcat, "土星为太阳系八大行星之一，排行第六，体积仅次于木星"),
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.spinner_dialog_base_adapter)

        // 获取下拉列表对象
        val spAdapter = findViewById<Spinner>(R.id.spinner_dialog_base_adapter)
        // 构建一个行星列表的适配器
        val planetBaseAdapter = PlanetBaseAdapter(this, planetList)
        // 传入适配器实例
        spAdapter.adapter = planetBaseAdapter
        // 设置默认为第一项
        spAdapter.setSelection(0)
        // 设置监听器，一旦用户选择了某一项，则触发 onItemSelected 方法
        spAdapter.onItemSelectedListener = this
    }

    // 选择后触发
    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.i("下拉列表", "选择后触发")
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "你选择的是" + planetList[position].name, Toast.LENGTH_SHORT).show();
    }

    // 当下拉列表中的选项被取消选择时，该方法将被调用。例如，当触摸被激活或适配器变为空时，选择可能会消失
    override fun onNothingSelected(parent: AdapterView<*>?) {
        Log.i("下拉列表", "当下拉列表中的选项被取消选择时触发")
    }
}
```

7. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownBaseAdapter -->
		<activity
			android:name=".SpinnerDropdownBaseAdapter"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

8. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508111651.png)

## 2、列表类视图

### ①、列表视图 ListView

#### Ⅰ、说明

1. ListView 允许在页面上分行展示相似的数据列表，例如新闻列表、商品列表、图书列表等，方便用户浏览与操作。
2. 上面下拉列表都是点击选中之后就会消失，而如果想要实现像购物商城那样排列显示商品的效果，则可以用 ListView。
3. 对于上面的代码，数据适配器 `PlanetBaseAdapter`，条目布局 `item_list.xml`，都不需要修改。只需要创建新布局文件和修改主 `Activity` 即可

#### Ⅱ、代码例子

1. 创建布局文件 `list_view.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<LinearLayout
		android:layout_width="match_parent"
		android:layout_height="wrap_content">
		
		<CheckBox
			android:id="@+id/ck_divider"
			android:layout_width="0dp"
			android:layout_height="match_parent"
			android:layout_weight="1"
			android:gravity="start|center"
			android:text="显示分隔线"
			android:textSize="17sp"/>
		
		<CheckBox
			android:id="@+id/ck_selector"
			android:layout_width="0dp"
			android:layout_height="match_parent"
			android:layout_weight="1"
			android:gravity="start|center"
			android:text="显示按压背景"
			android:textSize="17sp"/>
	
	</LinearLayout>
	
	<!--只需要添加 ListView 即可-->
	<ListView
		android:id="@+id/list_view_planetList"
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:divider="@null"
		android:dividerHeight="0dp"
		android:listSelector="#00FFFFFF"/>

</LinearLayout>
```

2. 条目布局文件 `spinner_dropdown_base_adapter_itme.xml` 不用改动
3. 行星实体数据类 `Planet` 不用改动
4. ViewHolder，用来标记控件的 `PlanetViewHolder` 不用改动
5. 自定义适配器 `PlanetBaseAdapter` 不用改动
6. 创建 selector 文件 `drawable/list_selector.xml`，定义列表的状态效果

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
	<!-- 默认时的背景图片-->
	<!-- <item android:drawable="@drawable/qq" /> -->
	<!-- 没有焦点时的背景图片 -->
	<!-- <item android:state_window_focused="false" android:drawable="@drawable/wcat" /> -->
	<!-- 非触摸模式下获得焦点并单击时的背景图片 -->
	<!-- <item android:state_focused="true" android:state_pressed="true"   android:drawable= "@drawable/pic2" /> -->
	<!-- 触摸模式下单击时的背景图片-->
	<item android:state_focused="false" android:state_pressed="true" android:drawable="@drawable/qq" />
	<!-- 选中时的图片背景 -->
	<!-- <item android:state_selected="true"   android:drawable="@drawable/pic4" /> -->
	<!-- 获得焦点时的图片背景 -->
	<!-- <item android:state_focused="true"   android:drawable="@drawable/pic5" /> -->
</selector>
```

7. 创建布局文件对应的代码文件 Activity `ListViewActivity

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.CheckBox
import android.widget.CompoundButton
import android.widget.ListView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.res.ResourcesCompat
import com.yuehai.advancedcontrols.ui.adapter.PlanetBaseAdapter
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet


class ListViewActivity: AppCompatActivity(), CompoundButton.OnCheckedChangeListener, AdapterView.OnItemClickListener {

    // 定义下拉列表需要显示的行星数据集合
    private val planetList: MutableList<Planet> = mutableListOf(
        Planet("水星", R.drawable.qq, "水星是太阳系八大行星最内侧也是最小的一颗行星，也是离太阳最近的行星"),
        Planet("金星", R.drawable.wcat, "金星是太阳系八大行星之一，排行第二，距离太阳0.725天文单位"),
        Planet("地球", R.drawable.qq, "地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里"),
        Planet("火星", R.drawable.wcat, "火星是太阳系八大行星之一，排行第四，属于类地行星，直径约为地球的53%"),
        Planet("木星", R.drawable.qq, "木星是太阳系八大行星中体积最大、自转最快的行星，排行第五。它的质量为太阳的千分之一，但为太阳系中其它七大行星质量总和的2.5倍"),
        Planet("土星", R.drawable.wcat, "土星为太阳系八大行星之一，排行第六，体积仅次于木星"),
    )
    // 获取下拉列表对象，等待赋值
    var listView: ListView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.list_view)

        // 获取下拉列表对象
        listView = findViewById<ListView>(R.id.list_view_planetList)
        // 构建一个行星列表的适配器
        val planetBaseAdapter = PlanetBaseAdapter(this, planetList)
        // 传入适配器实例
        listView?.adapter = planetBaseAdapter

        // 设置监听器，一旦用户点击了某一项，则触发 onItemClick 方法
        listView?.onItemClickListener = this

        // 给 显示分隔线、显示按压背景 单选框绑定选中事件；onCheckedChanged 方法中以 id 区分
        findViewById<CheckBox>(R.id.ck_divider).setOnCheckedChangeListener(this)
        findViewById<CheckBox>(R.id.ck_selector).setOnCheckedChangeListener(this)
    }

    // 点击后触发
    override fun onItemClick(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.i("列表视图", "点击列表项后触发")
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "你选择的是" + planetList[position].name, Toast.LENGTH_SHORT).show();
    }

    override fun onCheckedChanged(buttonView: CompoundButton?, isChecked: Boolean) {
        Log.i("单选框", "单选框")

        // 判断当前选中的组件
        when(buttonView?.id){

            // 显示分隔线
            R.id.ck_divider -> {
                // 判断是否选中
                if (findViewById<CheckBox>(R.id.ck_divider).isChecked){
                    // 从资源文件获得图形对象
                    val drawable = ResourcesCompat.getDrawable(resources, R.color.black, null)
                    // 设置列表视图的分隔线颜色
                    listView?.divider = drawable
                    // 设置列表视图的分隔线高度
                    listView?.dividerHeight = 10
                }else{
                    listView?.divider = null
                    listView?.dividerHeight = 0
                }
            }

            // 显示按压背景
            R.id.ck_selector -> {
                if (findViewById<CheckBox>(R.id.ck_selector).isChecked){
                    // 从资源文件获得图形对象
                    val drawable = ResourcesCompat.getDrawable(resources, R.drawable.list_selector, null)
                    // 设置列表项的按压状态图形
                    listView?.selector = drawable
                }else{
                    listView?.selector = null
                }
            }

        }
    }


}
```

8. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownBaseAdapter -->
		<activity
			android:name=".SpinnerDropdownBaseAdapter"
			android:exported="true">
		</activity>
		
		<!-- 注册 ListViewActivity；列表视图 ListView -->
		<activity
			android:name=".ListViewActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

9. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508111558.png)

### ②、网格视图 GridView

#### Ⅰ、说明

1. 除了列表视图，网格视图 `GridView` 也是常见的列表类视图，它用于分行分列显示表格信息，比列表视图更适合展示物品清单。
2. 在 XML 文件中添加 GridView 需要指定列的数目，以及空隙的拉伸模式

| XML中的属性       | GridView类的设置方法 | 说明                                                                        |
| ----------------- | -------------------- | --------------------------------------------------------------------------- |
| horizontalSpacing | setHorizontalSpacing | 指定网格项在水平方向的间距                                                  |
| verticalSpacing   | setVerticalSpacing   | 指定网格项在垂直方向的间距                                                  |
| <font color="#ff0000">numColumns</font>        | setNumColumns        | 指定列的数目                                                                |
| <font color="#ff0000">stretchMode</font>       | setStretchMode       | 指定剩余空间的拉伸模式                                                      |
| columnWidth       | setColumnWidth       | 指定每列的宽度。拉伸模式为spacingWidth、spacingWidthUniform时，必须指定列宽 |

3. GridView 拉伸模式取值

| XML中的拉伸模式     | GridView类的拉伸模式    | 说明                                                 |
| ------------------- | ----------------------- | ---------------------------------------------------- |
| none                | NO_STRETCH              | 不拉伸                                               |
| columnWidth         | STRETCH_COLUMN_WIDTH    | 若有剩余空间，则拉伸列宽挤掉空隙                     |
| spacingWidth        | STRETCH_SPACING         | 若有剩余空间，则列宽不变，把空间分配到每列间的空隙   |
| spacingWidthUniform | STRETCH_SPACING_UNIFORM | 若有剩余空间，则列宽不变，把空间分配到每列左右的空隙 |

4. GridView 拉伸模式效果

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508103548.png)

#### Ⅱ、代码例子

1. 创建布局文件 `grid_view.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent">
	
	<!--
		网格视图 GridView
		numColumns="2"：列数
		stretchMode="columnWidth"：拉伸模式，若有剩余空间，则拉伸列宽挤掉空隙
		listSelector="@drawable/list_selector：定义列表的状态效果
	 -->
	<GridView
		android:id="@+id/grid_view_planetList"
		android:layout_width="match_parent"
		android:layout_height="match_parent"
		android:numColumns="2"
		android:stretchMode="columnWidth"
		android:listSelector="@drawable/list_selector"/>

</LinearLayout>
```

2. 条目布局文件 `spinner_dropdown_base_adapter_itme.xml` 不用改动
3. 行星实体数据类 `Planet` 不用改动
4. ViewHolder，用来标记控件的 `PlanetViewHolder` 不用改动
5. 自定义适配器 `PlanetBaseAdapter` 不用改动
6. 定义列表的状态效果 selector 文件 `drawable/list_selector.xml` 不用改动
7. 创建布局文件对应的代码文件 Activity `GridViewActivity

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.GridView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.advancedcontrols.ui.adapter.PlanetBaseAdapter
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet

class GridViewActivity: AppCompatActivity(), AdapterView.OnItemClickListener {

    // 定义下拉列表需要显示的行星数据集合
    private val planetList: MutableList<Planet> = mutableListOf(
        Planet("水星", R.drawable.qq, "水星是太阳系八大行星最内侧也是最小的一颗行星，也是离太阳最近的行星"),
        Planet("金星", R.drawable.wcat, "金星是太阳系八大行星之一，排行第二，距离太阳0.725天文单位"),
        Planet("地球", R.drawable.qq, "地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里"),
        Planet("火星", R.drawable.wcat, "火星是太阳系八大行星之一，排行第四，属于类地行星，直径约为地球的53%"),
        Planet("木星", R.drawable.qq, "木星是太阳系八大行星中体积最大、自转最快的行星，排行第五。它的质量为太阳的千分之一，但为太阳系中其它七大行星质量总和的2.5倍"),
        Planet("土星", R.drawable.wcat, "土星为太阳系八大行星之一，排行第六，体积仅次于木星"),
    )
    // 获取下拉列表对象，等待赋值
    var gridView: GridView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.grid_view)

        // 获取网格视图对象
        gridView = findViewById<GridView>(R.id.grid_view_planetList)
        // 构建一个行星列表的适配器
        val planetBaseAdapter = PlanetBaseAdapter(this, planetList)
        // 传入适配器实例
        gridView?.adapter = planetBaseAdapter

        // 设置监听器，一旦用户点击了某一项，则触发 onItemClick 方法
        gridView?.onItemClickListener = this
    }

    // 点击后触发
    override fun onItemClick(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.i("网格视图", "点击网格项后触发")
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "你选择的是" + planetList[position].name, Toast.LENGTH_SHORT).show();
    }
}
```

8. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownBaseAdapter -->
		<activity
			android:name=".SpinnerDropdownBaseAdapter"
			android:exported="true">
		</activity>
		
		<!-- 注册 ListViewActivity；列表视图 ListView -->
		<activity
			android:name=".ListViewActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 GridViewActivity；网格视图 GridView -->
		<activity
			android:name=".GridViewActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

9. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508111453.png)

## 3、翻页类视图

### ①、翻页视图 ViewPager

#### Ⅰ、说明

1. 翻页视图允许页面在水平方向左右滑动
2. 翻页视图的原理类似列表视图和网格视图，它们的用法也很类似。
3. 例如，列表视图和网格视图使用基本适配器 `BaseAdapter`，翻页视图则使用翻页适配器 `PagerAdapter`
4. 列表视图和网格视图使用列表项的点击监听器 `OnItemClickListener`，翻页视图则使用页面变更监听器 `OnPageChangeListener` 监听页面切换事件。
5. `viewpager2` 内部实现原理是使用 `recycleview` 加 `LinearLayoutManager` 实现竖直滚动，其实可以理解为对 `recyclerview` 的二次封装
6. `ViewPager` 与 `ViewPager2` 部分对比

| ViewPager                 | ViewPager 2                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| PagerAdapter              | RecyclerView.Adapter                                                         |
| FragmentStatePagerAdapter | FragmentStateAdapter                                                         |
| addPageChangeListener     | registerOnPageChangeCallback                                                 |
| 无                        | 从右到左(RTL)的布局支持                                                      |
| 无                        | 垂直方向支持                                                                 |
| 无                        | 停用用户输入的功能( setUserInputEnabled、isUserInputEnabled ）n.net/JMlW1407 |

#### Ⅱ、代码例子

1. 创建布局文件 `view_pager.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="horizontal">

	<!-- 翻页视图 ViewPage -->
	<androidx.viewpager.widget.ViewPager
		android:id="@+id/view_pager_planetList"
		android:layout_width="match_parent"
		android:layout_height="match_parent" />

</LinearLayout>
```

2. 条目布局文件 `spinner_dropdown_base_adapter_itme.xml` 不用改动
3. 行星实体数据类 `Planet` 不用改动
4. ViewHolder，用来标记控件的 `PlanetViewHolder` 不用改动
5. <font color="#ff0000">创建自定义适配器</font> `PlanetViewPagerAdapter`，<font color="#ff0000">实现基本适配器</font> `PagerAdapter`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.viewpager.widget.PagerAdapter
import com.yuehai.advancedcontrols.R
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet

/**
 * 行星的自定义适配器，翻页类视图
 */
class PlanetViewPagerAdapter(
    // 上下文环境
    private var context: Context,
    // 所需数据
    private var data: MutableList<Planet>
): PagerAdapter() {

    // 返回可以滑动的 VIew 的个数
    override fun getCount(): Int {
        return data.size
    }

    // 该函数用来判断 instantiateItem(ViewGroup, int) 函数所返回来的 Object 与当前页面视图是否是代表的同一个视图，官方建议直接返回 arg0 == arg1 即可。
    override fun isViewFromObject(view: View, arg1: Any): Boolean {
        return view == arg1
    }

    // 实例化指定位置的页面，将其添加到容器中，并返回当前 View 视图
    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        // 获取视图，根据传入的数据对其赋值
        val planetView = LayoutInflater.from(context).inflate(R.layout.spinner_dialog_base_adapter_item, null)
        planetView.findViewById<ImageView>(R.id.iv_icon).setImageResource(data[position].image)
        planetView.findViewById<TextView>(R.id.tv_name).text = data[position].name
        planetView.findViewById<TextView>(R.id.tv_desc).text = data[position].desc

        /**
         * 添加一个view到 container 中，而后返回一个跟这个 view 可以关联起来的对象，
         * 这个对象能够是 view 自身，也能够是其余对象，
         * 关键是在 isViewFromObject 可以将 view 和这个 object 关联起来
         */
        container.addView(planetView)
        return planetView
    }

    // 滑动切换的时候销毁当前的组件；从当前 container 中删除指定位置的 View
    override fun destroyItem(container: ViewGroup, position: Int, `object`: Any) {
        // 我尝试把创建视图提上去，会报错
        container.removeView(LayoutInflater.from(context).inflate(R.layout.spinner_dialog_base_adapter_item, null))
    }

}
```

6. 创建布局文件对应的代码文件 Activity `ViewPagerActivity

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager.widget.ViewPager
import com.yuehai.advancedcontrols.ui.adapter.PlanetViewPagerAdapter
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet

class ViewPagerActivity: AppCompatActivity() {

    // 定义翻页视图需要显示的行星数据集合
    private val planetList: MutableList<Planet> = mutableListOf(
        Planet("水星", R.drawable.qq, "水星是太阳系八大行星最内侧也是最小的一颗行星，也是离太阳最近的行星"),
        Planet("金星", R.drawable.wcat, "金星是太阳系八大行星之一，排行第二，距离太阳0.725天文单位"),
        Planet("地球", R.drawable.qq, "地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里"),
        Planet("火星", R.drawable.wcat, "火星是太阳系八大行星之一，排行第四，属于类地行星，直径约为地球的53%"),
        Planet("木星", R.drawable.qq, "木星是太阳系八大行星中体积最大、自转最快的行星，排行第五。它的质量为太阳的千分之一，但为太阳系中其它七大行星质量总和的2.5倍"),
        Planet("土星", R.drawable.wcat, "土星为太阳系八大行星之一，排行第六，体积仅次于木星"),
    )
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.view_pager)

        // 获取翻页视图对象
        val viewPager = findViewById<ViewPager>(R.id.view_pager_planetList)
        // 构建一个行星列表的适配器
        val planetViewPagerAdapter = PlanetViewPagerAdapter(this, planetList)
        // 传入适配器实例
        viewPager?.adapter = planetViewPagerAdapter
    }
}
```

7. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownBaseAdapter -->
		<activity
			android:name=".SpinnerDropdownBaseAdapter"
			android:exported="true">
		</activity>
		
		<!-- 注册 ListViewActivity；列表视图 ListView -->
		<activity
			android:name=".ListViewActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 GridViewActivity；网格视图 GridView -->
		<activity
			android:name=".GridViewActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 ViewPagerActivity；翻页视图 ViewPager -->
		<activity
			android:name=".ViewPagerActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

8. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508163515.png)

9. 翻页过程

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508163544.png)

### ②、翻页标签栏 PagerTabStrip

#### Ⅰ、说明

1. 翻页标签栏能够在翻页视图上方显示页面标题，点击页面标题即可切换到对应页面

#### Ⅱ、代码例子

1. 创建布局文件 `view_pager_tab_strip.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 
		翻页视图 ViewPager
		viewpager2 中不可以有子标签，所有写法会与此处不同
	 -->
	<androidx.viewpager.widget.ViewPager
		android:id="@+id/view_Pager_tab_planetList"
		android:layout_width="match_parent"
		android:layout_height="wrap_content">
		
		<!-- 翻页标签栏 PagerTabStrip 的节点名称 -->
		<androidx.viewpager.widget.PagerTabStrip
			android:id="@+id/view_Pager_tab_strip"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content" />
	</androidx.viewpager.widget.ViewPager>
	
</LinearLayout>
```

2. 条目布局文件 `spinner_dropdown_base_adapter_itme.xml` 不用改动
3. 行星实体数据类 `Planet` 不用改动
4. ViewHolder，用来标记控件的 `PlanetViewHolder` 不用改动
5. <font color="#ff0000">创建自定义适配器</font> `PlanetViewTapStripPagerAdapter`，<font color="#ff0000">实现基本适配器</font> `PagerAdapter`，<font color="#ff0000">新增了方法</font> `getPageTitle`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.viewpager.widget.PagerAdapter
import com.yuehai.advancedcontrols.R
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet

/**
 * 行星的自定义适配器，翻页类视图
 */
class PlanetViewTapStripPagerAdapter(
    // 上下文环境
    private var context: Context,
    // 所需数据
    private var data: MutableList<Planet>
): PagerAdapter() {

    // 返回可以滑动的 VIew 的个数
    override fun getCount(): Int {
        return data.size
    }

    // 该函数用来判断 instantiateItem(ViewGroup, int) 函数所返回来的 Object 与当前页面视图是否是代表的同一个视图，官方建议直接返回 arg0 == arg1 即可。
    override fun isViewFromObject(view: View, arg1: Any): Boolean {
        return view == arg1
    }

    // 实例化指定位置的页面，将其添加到容器中，并返回当前 View 视图
    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        // 获取视图，根据传入的数据对其赋值
        val planetView = LayoutInflater.from(context).inflate(R.layout.spinner_dialog_base_adapter_item, null)
        planetView.findViewById<ImageView>(R.id.iv_icon).setImageResource(data[position].image)
        planetView.findViewById<TextView>(R.id.tv_name).text = data[position].name
        planetView.findViewById<TextView>(R.id.tv_desc).text = data[position].desc

        /**
         * 添加一个view到 container 中，而后返回一个跟这个 view 可以关联起来的对象，
         * 这个对象能够是 view 自身，也能够是其余对象，
         * 关键是在 isViewFromObject 可以将 view 和这个 object 关联起来
         */
        container.addView(planetView)
        return planetView
    }

    // 滑动切换的时候销毁当前的组件；从当前 container 中删除指定位置的 View
    override fun destroyItem(container: ViewGroup, position: Int, `object`: Any) {
        // 我尝试把创建视图提上去，会报错
        container.removeView(LayoutInflater.from(context).inflate(R.layout.spinner_dialog_base_adapter_item, null))
    }

    // 该方法的返回值会作为翻页视图的标签栏的显示文字
    override fun getPageTitle(position: Int): CharSequence? {
        return data[position].name
    }
}
```

6. 创建布局文件对应的代码文件 Activity `ViewPagerTapStripActivity`

```Kotlin
package com.yuehai.advancedcontrols

import android.graphics.Color
import android.os.Bundle
import android.util.Log
import android.util.TypedValue
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager.widget.PagerTabStrip
import androidx.viewpager.widget.ViewPager
import com.yuehai.advancedcontrols.ui.adapter.PlanetViewTapStripPagerAdapter
import com.yuehai.advancedcontrols.ui.adapter.bean.Planet


class ViewPagerTapStripActivity: AppCompatActivity(), ViewPager.OnPageChangeListener {

    // 定义翻页视图需要显示的行星数据集合
    private val planetList: MutableList<Planet> = mutableListOf(
        Planet("水星", R.drawable.qq, "水星是太阳系八大行星最内侧也是最小的一颗行星，也是离太阳最近的行星"),
        Planet("金星", R.drawable.wcat, "金星是太阳系八大行星之一，排行第二，距离太阳0.725天文单位"),
        Planet("地球", R.drawable.qq, "地球是太阳系八大行星之一，排行第三，也是太阳系中直径、质量和密度最大的类地行星，距离太阳1.5亿公里"),
        Planet("火星", R.drawable.wcat, "火星是太阳系八大行星之一，排行第四，属于类地行星，直径约为地球的53%"),
        Planet("木星", R.drawable.qq, "木星是太阳系八大行星中体积最大、自转最快的行星，排行第五。它的质量为太阳的千分之一，但为太阳系中其它七大行星质量总和的2.5倍"),
        Planet("土星", R.drawable.wcat, "土星为太阳系八大行星之一，排行第六，体积仅次于木星"),
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.view_pager_tab_strip)

        // 获取翻页视图的标签栏对象
        val tabStrip = findViewById<PagerTabStrip>(R.id.view_Pager_tab_strip)
        // 设置翻页标签栏的文本大小
        tabStrip.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20f);
        // 设置翻页标签栏的标题颜色，这里需要带透明度的颜色值
        tabStrip.setTextColor(Color.BLACK);
        // 设置翻页标签栏的背景颜色
        tabStrip.setBackgroundColor(Color.RED);
        // 设置导航条下方指示器是否有完整下划线颜色；
        tabStrip.drawFullUnderline = true
        // 设置导航条下方指示器颜色，这里需要带透明度的颜色值
        tabStrip.tabIndicatorColor = Color.YELLOW;
        // 设置导航条文字的间隔。
        tabStrip.textSpacing = 1

        // 获取翻页视图对象
        val viewPager = findViewById<ViewPager>(R.id.view_Pager_tab_planetList)
        // 构建一个行星列表的适配器
        val planetViewTapStripPagerAdapter = PlanetViewTapStripPagerAdapter(this, planetList)
        // 传入适配器实例
        viewPager?.adapter = planetViewTapStripPagerAdapter
        // 给翻页视图添加页面变更监听器
        viewPager.addOnPageChangeListener(this)
        // 默认开始选中第几个视图
        viewPager.currentItem = 3

    }

    /**
     * 当页面在滑动的时候会调用此方法，在滑动被停止之前，此方法回一直得到调用。其中三个参数的含义分别为：
     * position :当前页面，即你点击滑动的页面（从A滑B，则是A页面的position。官方说明：Position index of the first page currently being displayed. Page position+1 will be visible if positionOffset is nonzero.）
     * positionOffset：当前页面偏移的百分比
     * positionOffsetPixels：当前页面偏移的像素位置
     */
    override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {
        Log.i("月海 翻页标签栏", "从【" + planetList[position].name + "】页离开")
    }

    /**
     * 此方法是页面跳转完后得到调用，position 是你当前选中的页面的 Position（位置编号）(从A滑动到B，就是B的position)
     */
    override fun onPageSelected(position: Int) {
        // 用户界面的文字弹窗提示
        Toast.makeText(this, "当前标签页是" + planetList[position].name, Toast.LENGTH_SHORT).show();
    }

    /**
     * 此方法是在状态改变的时候调用，其中 state 这个参数有三种状态：
     * SCROLL_STATE_DRAGGING（1）表示用户手指“按在屏幕上并且开始拖动”的状态（手指按下但是还没有拖动的时候还不是这个状态，只有按下并且手指开始拖动后log才打出。）
     * SCROLL_STATE_IDLE（0）滑动动画做完的状态。
     * SCROLL_STATE_SETTLING（2）在“手指离开屏幕”的状态。
     * 一个完整的滑动动作，三种状态的出发顺序为（1，2，0）
     */
    override fun onPageScrollStateChanged(state: Int) {
        when(state){
            1 -> { Toast.makeText(this, "手指按在屏幕上并且开始拖动", Toast.LENGTH_SHORT).show(); }
            2 -> { Toast.makeText(this, "手指离开屏幕", Toast.LENGTH_SHORT).show(); }
            0 -> { Toast.makeText(this, "滑动动画做完", Toast.LENGTH_SHORT).show(); }
        }
    }
}
```

7. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 SpinnerDropdownActivity -->
		<activity
			android:name=".SpinnerDropdownActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownSimpleAdapterActivity -->
		<activity
			android:name=".SpinnerDropdownSimpleAdapterActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 SpinnerDropdownBaseAdapter -->
		<activity
			android:name=".SpinnerDropdownBaseAdapter"
			android:exported="true">
		</activity>
		
		<!-- 注册 ListViewActivity；列表视图 ListView -->
		<activity
			android:name=".ListViewActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 GridViewActivity；网格视图 GridView -->
		<activity
			android:name=".GridViewActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 ViewPagerActivity；翻页视图 ViewPager -->
		<activity
			android:name=".ViewPagerActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册 ViewPagerTapStripActivity；翻页标签栏 PagerTabStrip -->
		<activity
			android:name=".ViewPagerTapStripActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

8. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230509100825.png)

9. 翻页过程

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230509100928.png)

## 4、Fragment

### ①、介绍

1. Fragment（碎片）是一种可以嵌入在 Activity 中的 UI 片段，与 Activity 非常相似，不仅包含布局，同时也具有自己的生命周期。
2. Fragment 表示应用界面中可重复使用的一部分。
3. Fragment 允许您将界面划分为离散的区块，从而将模块化和可重用性引入 Activity 的界面。
4. Fragment 的布局文件和代码使用起来和 Activity 基本无异。除了继承自 Fragment 与入口方法 onCreateView 两点，其他地方类似活动页面代码。
5. 传统的 Activity 并不能很好的处理大屏问题，所以急需一个碎片化的东西能够划区域的展示内容，且有属于自己的独立可操作空间，所以就出现了 Fragment

![|583](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230510101016.png)

6. Fragment 的注册方式有两种：
	1. 静态注册：在 xml 中引入
	2. 动态注册：通过 java 代码的方式引入
7. Fragment 的生命周期

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230510105618.png)

8. Fragment 与 Activity 生命周期的对比

![|340](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230510105736.png)

### ②、静态注册

> 静态注册：在 xml 中引入

1. 创建 Frament 布局文件 `fragment_test_static.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- fragment -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/fragment_test_btn"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:text="Fragment"
		android:textSize="40dp" />
	
</LinearLayout>
```

2. 创建 Frament 代码文件 `FragmentTestStatic`

```Kotlin
package com.yuehai.advancedcontrols.fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.yuehai.advancedcontrols.R

// 继承 Fragment
class FragmentTestStatic: Fragment() {
	
	/**
	 * onCreateView 是 Fragment 碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 * 使用：View view = inflater.inflate(R.layout.right_fragment, container, false);
	 *
	 * 三个参数的含义及作用：
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById() 用来寻找 xml 布局下的具体的控件（Button、TextView 等）
	 *      LayoutInflater inflater（）用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		/**
		 * LayoutInflater.inflate(resource: Int, root: ViewGroup?, attachToRoot: Boolean)：把 xml 布局转换为对应的 View 对象
		 * 参数 1 resource：指定要转换的 XML 布局文件的 ID
		 * 参数 2 root：指定要将该 View 对象添加到哪个 ViewGroup 中
		 * 参数 3 attachToRoot：指定是否将该 View 对象添加到 root ViewGroup 中；将该 View 对象添加到 root ViewGroup 中
		 *      可以使得该 View 对象的布局参数（LayoutParams）生效，即该 View 对象的大小、位置等属性可以被 root ViewGroup 所控制
		 *
		 * 当 root 传空时，会直接返回要加载的 layoutId，返回的 View 没有父布局且没有 LayoutParams；
		 * 当 root 不传空时，又分为 attachToRoot 为真或者为假：
		 *      attachToRoot = true 会为传入的 layoutId 直接设置参数，并将其添加到 root 中，然后将传入的 root返回
		 *      attachToRoot = false 会为传入的 layoutId 设置参数，但是不会添加到 root ，然后返回 layoutId对应的 View；
		 */
		return inflater.inflate(R.layout.fragment_test_static, container, false)
	}
}
```

3. 创建主 activity 布局文件 `fragment_activity_static.xml` ，在其中引入 Frament

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- activity，可引入 fragment -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	xmlns:tools="http://schemas.android.com/tools"
	android:orientation="vertical">
	
	<Button
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:text="本页面自己的内容"
		android:textSize="40dp" />
	
	<!--
		引入 fragment
		name：指定 fragment 的代码文件，其需要继承 Fragment
		tools:layout 仅仅是告诉编辑器，Fragment在程序预览的时候该显示成什么样，并不会对apk产生实际作用，是为开发者设计的
	 -->
	<fragment
		android:id="@+id/fragment_test"
		android:name="com.yuehai.advancedcontrols.fragment.FragmentTestStatic"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		tools:layout="@layout/fragment_test_static" />
	
	<Button
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:text="本页面自己的内容"
		android:textSize="40dp" />
	
</LinearLayout>
```

4. 创建主 activity 代码文件 `FragmentStaticActivity`

```Kotlin
package com.yuehai.advancedcontrols

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class FragmentStaticActivity: AppCompatActivity() {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.fragment_activity_static)
	}
}
```

5. 修改清单文件 `AndroidManifest.xml`

```xml
<!-- 注册 FragmentActivity -->
<activity
	android:name=".FragmentStaticActivity"
	android:exported="true">
	<intent-filter>
		<!-- 配置为主窗口 -->
		<action android:name="android.intent.action.MAIN" />
		<category android:name="android.intent.category.LAUNCHER" />
	</intent-filter>
</activity>
```

6. 效果

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230510124044.png)

### ③、动态注册

> 动态注册：通过 java 代码的方式引入

#### Ⅰ、Fragment 与 Activity 之间数据交互

1. Fragment 向 Activity 传递数据：Fragment 中定义一个内部回调接口，再让包含这个 Fragment 的 Activity 实现这个接口
2. Activity 向 Fragment 传递数据：使用Java语言描述的话，最关键的两个函数是 `setArguments` 和 `getArguments`；向fragment 中传递数据使用 Bundle，同时需要动态添加 fragment
3. 相比较于上面的传递数据的方式，<font color="#ff0000">EventBus</font> 就好用多了

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230510132520.png)

4. 在想<font color="#245bdb">接收数据</font>的类中注册为 `Subscriber(订阅者)`
5. <font color="#6425d0">发送数据</font>的类就不用注册了，直接只是用 `post()` 方法发送数据即可。
6. 然后在订阅者的类(<font color="#245bdb">接受数据</font>的类)中使用 `onEvent()` 接受数据即可
7. 需要先导入依赖：`implementation 'org.greenrobot:eventbus:3.2.0'`
8. ~~下面使用的就是 `EventBus`~~ 哪个都没用，若想在 `Fragment` 中使用 `EventBus`，记得要在 `Fragment` 暂停或销毁时执行 `EventBus` 注销方法，不然重复注册会报错

#### Ⅱ、代码

1. 创建 `Fragment` 布局文件 `fragment_test_dynamic.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- fragment -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/fragment_test_dynamic_btn"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:text="Fragment 1"
		android:textSize="40dp" />
	
</LinearLayout>
```

2. 创建 `Fragment` 布局文件对应的代码文件 `FragmentTestDynamic`

```Kotlin
package com.yuehai.advancedcontrols.fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import com.yuehai.advancedcontrols.R

// 继承 Fragment；参数是我自定义要接收的数据
class FragmentTestDynamic(
	private val data: Map<String, Any>
): Fragment() {
	
	/**
	 * onCreateView 是 Fragment 碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 * 使用：View view = inflater.inflate(R.layout.right_fragment, container, false);
	 *
	 * 三个参数的含义及作用：
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById() 用来寻找 xml 布局下的具体的控件（Button、TextView 等）
	 *      LayoutInflater inflater（）用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		
		/**
		 * LayoutInflater.inflate(resource: Int, root: ViewGroup?, attachToRoot: Boolean)：把 xml 布局转换为对应的 View 对象
		 * 参数 1 resource：指定要转换的 XML 布局文件的 ID
		 * 参数 2 root：指定要将该 View 对象添加到哪个 ViewGroup 中
		 * 参数 3 attachToRoot：指定是否将该 View 对象添加到 root ViewGroup 中；将该 View 对象添加到 root ViewGroup 中
		 *      可以使得该 View 对象的布局参数（LayoutParams）生效，即该 View 对象的大小、位置等属性可以被 root ViewGroup 所控制
		 *
		 * 当 root 传空时，会直接返回要加载的 layoutId，返回的 View 没有父布局且没有 LayoutParams；
		 * 当 root 不传空时，又分为 attachToRoot 为真或者为假：
		 *      attachToRoot = true 会为传入的 layoutId 直接设置参数，并将其添加到 root 中，然后将传入的 root返回
		 *      attachToRoot = false 会为传入的 layoutId 设置参数，但是不会添加到 root ，然后返回 layoutId对应的 View；
		 */
		val view = inflater.inflate(R.layout.fragment_test_dynamic, container, false)
		
		// 获取按钮组件对象，并赋值
		view.findViewById<Button>(R.id.fragment_test_dynamic_btn).text = data["btnText"].toString()
		
		return view
	}
	
}
```

3. <font color="#ff0000">创建自定义适配器</font> `FragmentTestDynamicAdapter`，<font color="#ff0000">实现适配器</font> `FragmentPagerAdapter`

```Kotlin
package com.yuehai.advancedcontrols.ui.adapter

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentPagerAdapter
import androidx.lifecycle.Lifecycle
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.yuehai.advancedcontrols.fragment.FragmentTestDynamic

/**
 * 自定义适配器，翻页类视图，使用 Fragment，翻页类视图需继承 FragmentPagerAdapter(fa: FragmentManager)
 *
 * FragmentPagerAdapter(fa: FragmentManager) 已被废弃，代替为：FragmentStateAdapter(fa FragmentManager, lifecycle Lifecycle)
 */
class FragmentTestDynamicAdapter(
	// FragmentManager 允许我们管理 Fragment；负责将 Fragment 添加到 Activity 中，并在需要时将其删除
	private var fa: FragmentManager,
	// 所需数据
	private var data: List<String>
): FragmentPagerAdapter(fa) {
	
	// 返回可以滑动的 VIew 的个数
	override fun getCount(): Int {
		return data.size
	}
	
	/**
	 * getItem() 方法主要是给 instantiateItem() 起到了辅助作用
	 * 在 instantiateItem() 方法中，首先会去容器中寻找是否已经添加了指定的 Fragment
	 * 如果为空，就会去调用 getItem() 去创建一个，所以在 getItem() 方法中，只要返回一个新的 Fragment 就可以了
	 * 这也是为什么 FragmentPagerAdapter 默认只让我们实现 getItem() 和 getCount() 这两个方法。
	 */
	override fun getItem(position: Int): Fragment {
		return FragmentTestDynamic(mutableMapOf("btnText" to data[position]))
	}
	
	// 该方法的返回值会作为翻页视图的标签栏的显示文字
	override fun getPageTitle(position: Int): CharSequence? {
		return data[position]
	}
	
}
```

4. 创建主布局文件 `fragment_activity_dynamic.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	xmlns:tools="http://schemas.android.com/tools"
	android:orientation="vertical">
	
	<!--
		翻页视图 ViewPager
	 -->
	<androidx.viewpager.widget.ViewPager
		android:id="@+id/fragment_test_dynamic_view_Pager_tab_planetList"
		android:layout_width="match_parent"
		android:layout_height="wrap_content">
		
		<!-- 翻页标签栏 PagerTabStrip 的节点名称 -->
		<androidx.viewpager.widget.PagerTabStrip
			android:id="@+id/fragment_test_dynamic_view_Pager_tab_strip"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content" />
		
	</androidx.viewpager.widget.ViewPager>

</LinearLayout>
```

5. 创建主布局文件对应的代码文件 `FragmentDynamicActivity`

```Kotlin
package com.yuehai.advancedcontrols

import android.graphics.Color
import android.os.Bundle
import android.util.Log
import android.util.TypedValue
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager.widget.PagerTabStrip
import androidx.viewpager.widget.ViewPager
import com.yuehai.advancedcontrols.ui.adapter.FragmentTestDynamicAdapter

class FragmentDynamicActivity: AppCompatActivity(), ViewPager.OnPageChangeListener {
	
	// 定义 Fragment 需要显示的数据
	private val fragmentData = listOf(
		"Fragment 1",
		"Fragment 2",
		"Fragment 3",
		"Fragment 4",
		"Fragment 5",
	)
	
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.fragment_activity_dynamic)
		
		// 获取翻页视图的标签栏对象
		val tabStrip = findViewById<PagerTabStrip>(R.id.fragment_test_dynamic_view_Pager_tab_strip)
		// 设置翻页标签栏的文本大小
		tabStrip.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20f);
		// 设置翻页标签栏的标题颜色，这里需要带透明度的颜色值
		tabStrip.setTextColor(Color.BLACK);
		// 设置翻页标签栏的背景颜色
		tabStrip.setBackgroundColor(Color.RED);
		// 设置导航条下方指示器是否有完整下划线颜色；
		tabStrip.drawFullUnderline = true
		// 设置导航条下方指示器颜色，这里需要带透明度的颜色值
		tabStrip.tabIndicatorColor = Color.YELLOW;
		// 设置导航条文字的间隔。
		tabStrip.textSpacing = 1
		
		// 获取翻页视图对象
		val viewPager = findViewById<ViewPager>(R.id.fragment_test_dynamic_view_Pager_tab_planetList)
		// 构建适配器
		val fragmentTestDynamicAdapter = FragmentTestDynamicAdapter(supportFragmentManager, fragmentData)
		// 传入适配器实例
		viewPager?.adapter = fragmentTestDynamicAdapter
		// 给翻页视图添加页面变更监听器
		viewPager.addOnPageChangeListener(this)
		// 默认开始选中第几个视图
		viewPager.currentItem = 0
	}
	
	/**
	 * 当页面在滑动的时候会调用此方法，在滑动被停止之前，此方法回一直得到调用。其中三个参数的含义分别为：
	 * position :当前页面，即你点击滑动的页面（从A滑B，则是A页面的position。官方说明：Position index of the first page currently being displayed. Page position+1 will be visible if positionOffset is nonzero.）
	 * positionOffset：当前页面偏移的百分比
	 * positionOffsetPixels：当前页面偏移的像素位置
	 */
	override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {
		Log.i("月海 翻页标签栏", "从【" + fragmentData[position] + "】页离开")
	}
	
	/**
	 * 此方法是页面跳转完后得到调用，position 是你当前选中的页面的 Position（位置编号）(从A滑动到B，就是B的position)
	 */
	override fun onPageSelected(position: Int) {
		// 用户界面的文字弹窗提示
		Toast.makeText(this, "当前标签页是" + fragmentData[position], Toast.LENGTH_SHORT).show();
	}
	
	/**
	 * 此方法是在状态改变的时候调用，其中 state 这个参数有三种状态：
	 * SCROLL_STATE_DRAGGING（1）表示用户手指“按在屏幕上并且开始拖动”的状态（手指按下但是还没有拖动的时候还不是这个状态，只有按下并且手指开始拖动后log才打出。）
	 * SCROLL_STATE_IDLE（0）滑动动画做完的状态。
	 * SCROLL_STATE_SETTLING（2）在“手指离开屏幕”的状态。
	 * 一个完整的滑动动作，三种状态的出发顺序为（1，2，0）
	 */
	override fun onPageScrollStateChanged(state: Int) {
		when(state){
			1 -> { Toast.makeText(this, "手指按在屏幕上并且开始拖动", Toast.LENGTH_SHORT).show(); }
			2 -> { Toast.makeText(this, "手指离开屏幕", Toast.LENGTH_SHORT).show(); }
			0 -> { Toast.makeText(this, "滑动动画做完", Toast.LENGTH_SHORT).show(); }
		}
	}
}
```

6. 修改 `AndroidManifest.xml` 清单文件

```xml
<!-- 注册 FragmentDynamicActivity -->
<activity
	android:name=".FragmentDynamicActivity"
	android:exported="true">
	<intent-filter>
		<!-- 配置为主窗口 -->
		<action android:name="android.intent.action.MAIN" />
		<category android:name="android.intent.category.LAUNCHER" />
	</intent-filter>
</activity>
```

7. 结果显示

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230511085838.png)

8. 翻页过程

![|435](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230511085935.png)

# 六、`Android` 数据存储 `SharedPreferences`

## 1、共享参数 `SharedPreferences`

1. `SharedPreferences` 是 `Android` 的一个轻量级存储工具，采用的存储结构是 `Key-Value` 的键值对方式。
2. 共享参数的存储介质是符合 XML 规范的配置文件。
3. 保存路径是：`/data/data/应用包名/shared_prefs/文件名.xml`
4. 共享参数主要适用于如下场合：
	1. 简单且孤立的数据。若是复杂且相互间有关的数据，则要保存在数据库中。
	2. 文本形式的数据。若是二进制数据，则要保存在文件中。
	3. 需要持久化存储的数据。在App退出后再次启动时，之前保存的数据仍然有效。
5. 实际开发中，共享参数经常存储的数据有 App 的个性化配置信息、用户使用 App 的行为信息、临时需要保存的片段信息等
6. `xml` 布局文件 `shared_preferences_01.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 按钮；共享参数 -->
	<Button
		android:id="@+id/yuehai_shared_preferences_01_btn"
		android:text="共享参数"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/purple_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

</LinearLayout>
```

6. `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!--
        android:allowBackup，是否允许应用备份。
            允许用户备份系统应用和第三方应用的 apk 安装包和应用数据，以便在刷机或者数据丢失后恢复应用，用户即可通过 adb backup 和 adb restore 来进行对应用数据的备份和恢复。
            为 true 表示允许，为 false 则表示不允许
        android:icon，指定 App 在手机屏幕上显示的图标。
        android:label，指定 App 在手机屏幕上显示的名称。
        android:roundIcon，指定 App 的圆角图标。
        android:supportsRtl，是否支持 阿拉伯语/波斯语 这种从右往左的文字排列顺序。为 true 表示支持，为 false 则表示不支持。
        android:theme，指定 App 的显示风格。
     -->
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!--
			android:name=".MainActivity"：当前注册的窗口是哪个
			android:exported="true"：表示当前 Activity 是否可以被另一个 Application 的组件启动：true 允许被启动；false 不允许被启动
			android:label="@string/app_name"：标识当前窗口名
			android:launchMode="standard"：指定启动模式
		 -->
		<activity
			android:name=".SharedPreferences01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

7. 代码文件 `SharedPreferences01.kt`

```Kotlin
package com.yuehai.sharedpreferences

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class SharedPreferences01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.shared_preferences_01)

        // 按钮；点击存储、读取 yuehai_activity01_btn
        findViewById<Button>(R.id.yuehai_shared_preferences_01_btn).setOnClickListener {
            println("")
            // sharedPreferences 对数据的存储和读取类似 Map，提供 put 和 set 方法。
            // 1、获取数据可以通过 SharedPreferences 对象存储和获取获取：第一个参数表示文件名，第二个参数表示私有模式
            val sharedPreferences = getSharedPreferences("fileName", MODE_PRIVATE)

            // 2、存储数据需要借助 Editor 类
            val edit = sharedPreferences.edit()
            // 放入数据
            edit.putInt("age", 16)
            edit.putString("name", "月海")
            // 保存数据
            edit.commit()

            // 3、读取数据；参数 1：要读取的数据的 key；参数 2：没有指定 key 时的默认值
            val name = sharedPreferences.getString("name", "name1")
            val age = sharedPreferences.getInt("age", 10)
            println("name：${name}；age：${age}")

        }

    }
}
```

## 2、数据库 `SQLite`

- SQLite 是安卓的一种小巧的嵌入式数据库，基本使用和思路和 Mysql 无异。

### ①、基本语法

1. 标准的 SQL 语句分为三类：数据定义、数据操纵和数据控制，但不同的数据库往往有自己的实现。
2. SQLite 是一种小巧的嵌入式数据库，由于它属于轻型数据库，不涉及复杂的数据控制操作，因此 App 开发只用到数据定义和数据操纵两类 SQL。
3. SQLite 的 SQL 语法与通用的 SQL 语法略有不同。

### ②、SQLite 的数据定义语言

1. 数据定义语言（DDL）描述了怎样变更数据实体的框架结构。
2. DDL语言主要包括三种操作：创建表、删除表、修改表结构。
	1. 创建表，格式为：`CREATE TABLE IF NOT EXISTS 表格名称`
	2. 删除表，格式为：`DROP TABLE IF EXISTS 表格名称`”
	3. 修改表结构，格式为“`ALTER TABLE 表格名称 修改操作`”
3. SQLite 只支持增加字段，不支持修改字段，也不支持删除字段

### ③、SQLite 的数据操纵语言

1. 数据操纵语言（DML）它描述了怎样处理数据实体的内部记录。
2. 表格记录的操作类型包括添加、删除、修改、查询四类：
	1. 添加记录，格式为：INSERT INTO 表格名称 (以逗号分隔的字段名列表) VALUES (以逗号分隔的字段值列表);”
	2. 删除记录，格式为：`DELETE FROM 表格名称 WHERE 查询条件`
	3. 修改记录，格式为：`UPDATE 表格名称 SET 字段名=字段值 WHERE 查询条件`
	4. 查询记录，格式为：`SELECT 以逗号分隔的字段名列表 FROM 表格名称 WHERE 查询条件`

### ④、数据库管理器 SQLiteDatabase

1.  SQLiteDatabase 是 SQLite 的数据库管理类，它提供了若干操作数据表的 API，常用的方法有 3 类：
2. 管理类，用于数据库层面的操作。
	1. `openDatabase`：打开指定路径的数据库。
	2. `isOpen`：判断数据库是否已打开。
	3. `close`：关闭数据库。
	4. `getVersion`：获取数据库的版本号。
	5. `setVersion`：设置数据库的版本号
3. 事务类，用于事务层面的操作。
	1. `beginTransaction`：开始事务。
	2. `setTransactionSuccessful`：设置事务的成功标志。
	3. `endTransaction`：结束事务；执行本方法时,系统会判断之前是否调用了 `setTransactionSuccessful` 方法，如果之前已调用该方法就提交事务，如果没有调用该方法就回滚事务。
4. 数据处理类，用于数据表层面的操作。
	1. `execSQL`：执行拼接好的SQL控制语句；般用于建表、删表、变更表结构。
	2. `delete`：删除符合条件的记录。
	3. `update`：更新符合条件的记录。
	4. `insert`：插入一条记录。
	5. `query`：执行查询操作，返回结果集的游标。
	6. `rawQuery`：执行拼接好的SQL查询语句，返回结果集的游标

### ⑤、数据库帮助器 SQLiteOpenHelper

1. 由于 SQLiteDatabase 存在局限性，一不小心就会重复打开数据库，处理数据库的升级也不方便；因此 Android 提供了数据库帮助器 SQLiteOpenHelper，帮助开发者合理使用 SQLite。
2. SQLiteOpenHelper 的具体使用步骤如下：
3. 步骤一，新建一个继承自 `SQLiteOpenHelper` 的数据库操作类，按提示重写 `onCreate` 和 `onUpgrade` 两个方法。
	1. 其中，`onCreate` 方法只在第一次打开数据库时执行，在此可以创建表结构；
	2. 而 `onUpgrade` 方法在数据库版本升高时执行，在此可以根据新旧版本号变更表结构。
4. 步骤二，为保证数据库安全使用，需要封装几个必要方法，包括获取单例对象、打开数据库连接、关闭数据库连接，说明如下：
	1. 获取单例对象：确保在 App 运行过程中数据库只会打开一次，避免重复打开引起错误。
	2. 打开数据库连接：SQLite 有锁机制，即读锁和写锁的处理；故而数据库连接也分两种，读连接可调用 `getReadableDatabase` 方法获得，写连接可调用 `getWritableDatabase` 获得。
	3. 关闭数据库连接：数据库操作完毕，调用数据库实例的 `close` 方法关闭连接。
5. 步骤三， 提供对表记录增加、删除、修改、查询的操作方法。
	1. 能被 SQLite 直接使用的数据结构是 `ContentValues` 类，它类似于映射 Map，也提供了 `put` 和 `get` 方法存取键值对。
	2. 区别之处在于：`ContentValues` 的键只能是字符串，不能是其他类型。`ContentValues` 主要用于增加记录和更新记录，对应数据库的 `insert` 和 `update` 方法。
	3. 记录的查询操作用到了游标类 `Cursor`，调用 `query` 和 `rawQuery` 方法返回的都是 `Cursor` 对象，若要获取全部的查询结果，则需根据游标的指示一条一条遍历结果集合。
6. `Cursor` 的常用方法可分为3类，说明如下：
7. 游标控制类方法，用于指定游标的状态
	1. `close`：关闭游标。
	2. `isClosed`：判断游标是否关闭。
	3. `isFirst`：判断游标是否在开头。
	4. `isLast`：判断游标是否在末尾。
8. 游标移动类方法，把游标移动到指定位置
	1. `moveToFirst`：移动游标到开头。
	2. `moveToLast`：移动游标到末尾。
	3. `moveToNext`：移动游标到下一条记录。
	4. `moveToPrevious`：移动游标到上一条记录。
	5. `move`：往后移动游标若干条记录。
	6. `moveToPosition`：移动游标到指定位置的记录。
9. 获取记录类方法，可获取记录的数量、类型以及取值
	1. `getCount`：获取结果记录的数量。
	2. `getInt`：获取指定字段的整型值。
	3. `getLong`：获取指定字段的长整型值。
	4. `getFloat`：获取指定字段的浮点数值。
	5. `getString`：获取指定字段的字符串值。
	6. `getType`：获取指定字段的字段类型。

### ⑥、例子

```Kotlin
package com.yuehai.contentproviderserver.contentProvider

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import com.yuehai.contentproviderserver.bean.UserInfo


/**
 * UserDBHelper 的参数 context：
 *      Context 是一个抽象类，它是 Android 应用程序的环境信息的接口。
 *      Context 提供了访问应用程序资源和类、调用 Activity、广播和接收 Intent 等功能。
 *      在 Android 中，Activity、Service、Application 等都是 Context 的子类，因此它们都可以使用 Context 提供的功能
 *      在 Kotlin 中，您可以使用 this 键字来引用当前上下文。例如，在 Activity 中，您可以使用 this 关键字来引用 Activity 的上下文
 * UserDBHelper 的参数：
 *      1. 上下文环境；第一个参数是必须的
 *      2. 数据库名字；第二个参数如果传入 null，则表示创建临时数据库，在应用退出之后，数据就会丢失
 *      3. 可选的游标工厂；第三个参数如果使用系统默认的游标工厂就传入 null，一般都填 null
 *      4. 代表你正在使用的数据库模型版本的整数；第四个参数用版本号来控制数据库的升级和降级，版本号从 1 开始
 */
class UserDBHelper(
    val context: Context,
    val tableName:String,
    val version:Int
): SQLiteOpenHelper(context, tableName, null, version) {

    // 数据库实例
    private var sdb: SQLiteDatabase? = null

    // 打开读连接
    fun openReadLink(): SQLiteDatabase? {
        if (sdb == null || !sdb!!.isOpen) {
            sdb = this.readableDatabase
        }
        return sdb
    }

    // 打开写连接
    fun openWriteLink(): SQLiteDatabase? {
        if (sdb == null || !sdb!!.isOpen) {
            sdb = this.writableDatabase
        }
        return sdb
    }

    // 关闭数据库连接
    fun closeLink() {
        if (sdb != null && sdb!!.isOpen) {
            sdb!!.close()
            sdb = null
        }
    }

    // onCreate() 方法在数据库第一次创建时执行，一般将创建表等初始化操作在该方法中执行
    override fun onCreate(db: SQLiteDatabase?) {
        // 先删除已存在表
        val dropSql = "drop table if exists $tableName;"
        db!!.execSQL(dropSql)

        // 创建表
        val createSql = (
                "CREATE TABLE IF NOT EXISTS $tableName" + " ("
                + "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                + "name VARCHAR NOT NULL,"
                + "age INTEGER NOT NULL);"
                )

        db.execSQL(createSql)
    }

    // onUpgrade() 方法在打开数据库时传入的版本号与当前的版本号不同时会调用该方法，一般将升级数据库等操作在该方法中执行
    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        // Android 的 ALTER 命令不支持一次添加多列，只能分多次添加
        var alterSql = "ALTER TABLE $tableName ADD COLUMN phone VARCHAR;"
        db!!.execSQL(alterSql)

        alterSql = "ALTER TABLE $tableName ADD COLUMN password VARCHAR;"
        db.execSQL(alterSql)

    }

    // 往表里添加一条记录
    fun insert(userinfo: UserInfo){
        // 获取 ContentValues 对象
        val contentValues = ContentValues()
        // 向 ContentValues 对象中添加数据
        contentValues.put("name", userinfo.name)
        contentValues.put("age", userinfo.age)

        // 保存数据
        sdb?.insert(tableName, "", contentValues)
    }

    // 往表里添加多条记录

    // 根据条件查询记录
    fun query(name:String): MutableList<UserInfo> {
        // 拼接语句
        val sql = "select id,name,age from $tableName where name=$name;"
        // 执行查询语句，该语句返回结果集的游标
        val rawQuery = sdb?.rawQuery(sql, null);

        // 定义可变集合；
        val userList:MutableList<UserInfo> = mutableListOf()
        // 遍历游标，取出数据
        if (rawQuery != null) {
            while (rawQuery.moveToNext()){
                userList.add(UserInfo(rawQuery.getString(1), rawQuery.getInt(2)))
            }

            rawQuery.close()
        }

        return userList
    }


}
```

```Kotlin
// 点击按钮
findViewById<Button>(R.id.yuehai_content_provider_server_01_btn).setOnClickListener {

	val userDBHelper = UserDBHelper(this, "yuehai", 1)

	// 创建表
	userDBHelper.onCreate(userDBHelper.writableDatabase)
	// 关闭数据库连接
	userDBHelper.close()

	// 插入数据
	userDBHelper.insert(userDBHelper.writableDatabase, UserInfo("name", 16))
	Log.i("插入数据", "")
	// 关闭数据库连接
	userDBHelper.close()

	// 读取数据
	val userInfos: MutableList<UserInfo> = userDBHelper.query(userDBHelper.readableDatabase, "name")
	userInfos.forEach {
		Log.i("读取数据 name", it.name)
		Log.i("读取数据 age", it.age.toString())
	}
	// 关闭数据库连接
	userDBHelper.close()

}
```

## 3、 存储卡

### ①、私有空间和公有空间

1. 为了更规范地管理手机存储空间，Android 从 7.0 开始将存储卡划分为私有存储和公共存储两大部分，也就是分区存储方式，系统给每个 App 都分配了默认的私有存储空间。
2. App 在私有空间上读写文件无须任何授权，但是若想在公共空间读写文件，则要在 `AndroidManifest.xml` 清单文件里面添加下述的权限配置
3. 但是即使 App 声明了完整的存储卡操作权限，系统仍然默认禁止该 App 访问公共空间。
4. 打开手机的系统设置界面，进入到具体应用的管理页面，会发现该应用的存储访问权限被禁止了。
5. 既然存储卡分为公共空间和私有空间两部分，它们的空间路径获取也就有所不同。
6. 若想获取公共空间的存储路径，调用的是 `Environment.getExternalStoragePublicDirectory` 方法；
7. 若想获取应用私有空间的存储路径，调用的是 `getExternalFilesDir` 方法
8. 在安卓6.0（API 23）及以上系统，考虑到安全，访问手机 SD 卡时，不但要加上上述权限，还需要在代码中动态申请权限

```xml
<!-- 按钮；存储卡 -->
	<Button
			android:id="@+id/yuehai_shared_preferences_01_SD"
			android:text="存储卡"
			android:textSize="30dp"
			android:textColor="@color/black"
			android:backgroundTint="@color/purple_200"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:layout_gravity="start"/>
```

```Kotlin
package com.yuehai.sharedpreferences

import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class SharedPreferences01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.shared_preferences_01)

        // 按钮；存储卡
        findViewById<Button>(R.id.yuehai_shared_preferences_01_SD).setOnClickListener {
            // 获取系统的公共存储路径
            val publicPath: String = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS).toString()

            // 获取系统的私有存储路径
            val privatePath = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS).toString()

            // Android10 的存储空间默认采用分区方式，这里是判断是使用传统方式还是分区方式
            // SDK 是否大于 29，即是否大于安卓 9
            var isLegacy = true
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {

                isLegacy = Environment.isExternalStorageLegacy()
            }

            Log.i("存储方式：", isLegacy.toString())
            // /storage/emulated/0/Download
            Log.i("系统的公共存储路径：", publicPath)
            // /storage/emulated/0/Android/data/com.yuehai.sharedpreferences/files/Download
            Log.i("系统的私有存储路径：", privatePath)

        }

    }
}
```

### ②、在存储卡上读写文件

1. 在 `AndroidManifest.xml` 清单文件中注册权限

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:tools="http://schemas.android.com/tools" xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 存储卡读写权限 -->
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
	<!--在sdcard中创建/删除文件的权限 -->
	<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" tools:ignore="ProtectedPermissions"/>
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!--
			android:name=".MainActivity"：当前注册的窗口是哪个
			android:exported="true"：表示当前 Activity 是否可以被另一个 Application 的组件启动：true 允许被启动；false 不允许被启动
			android:label="@string/app_name"：标识当前窗口名
			android:launchMode="standard"：指定启动模式
		 -->
		<activity
			android:name=".SharedPreferences01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

2. xml 窗口布局文件中定义按钮

```xml
<!-- 按钮；存储卡 -->
	<Button
			android:id="@+id/yuehai_shared_preferences_01_SD"
			android:text="存储卡"
			android:textSize="30dp"
			android:textColor="@color/black"
			android:backgroundTint="@color/purple_200"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:layout_gravity="start"/>
```

3. 窗口布局对应的代码文件

```Kotlin
// 按钮；存储卡
        findViewById<Button>(R.id.yuehai_shared_preferences_01_SD).setOnClickListener {
            // 获取系统的公共存储路径
            val publicPath: String = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS).toString()

            // 获取系统的私有存储路径
            val privatePath = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS).toString()

            // Android10 的存储空间默认采用分区方式，这里是判断是使用传统方式还是分区方式
            // SDK 是否大于 29，即是否大于安卓 9
            var isLegacy = true
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                isLegacy = Environment.isExternalStorageLegacy()
            }

            Log.i("存储方式：", isLegacy.toString())
            // /storage/emulated/0/Download
            Log.i("系统的公共存储路径：", publicPath)
            // /storage/emulated/0/Android/data/com.yuehai.sharedpreferences/files/Download
            Log.i("系统的私有存储路径：", privatePath)


            // 验证是否许可权限；Manifest 需要自行引入包：import android.Manifest
            if(ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED){
                // 不存在权限，进行申请
                ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE), 200)
            }


            // 创建文件
            val file = File("$privatePath/月海.txt")
            // 判断文件是否存在
            if (!file.exists()){
                // 不存在就创建
                file.createNewFile()
                Log.i("创建文件：", file.isFile.toString())
            }

            // 把字符串写入文件输出流
            file.writeText("月海11111111111111111111")
            Log.i("把字符串写入文件输出流：", file.isFile.toString())

            // 读取文件的文本内容
            val content = File("$privatePath/月海.txt").readText()
            Log.i("读取文件的文本内容：", content)

        }
```

### ③、在存储卡上读写 图片文件

#### Ⅰ、介绍

1. 文本文件可以转化为对字符串的读写，而图像的读写就需要借助专门的位图工具 Bitmap 处理。不同图像来源获取 Bitmap 的方式不同，有三种：
2. 方式一：从指定资源文件中获取：decodeResource，例如从资源文件 img.png 获取位图对象

```Kotlin
Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.img);
```

3. 方式二：从指定路径下获取：decodeFile，但是要注意从 Android10 开始，该方法只能获取私有空间下的图片，公共空间下获取不了

```Kotlin
Bitmap bitmap = BitmapFactory.decodeFile("C:\\Users\\OYMN\\Pictures\\onepunch.jpg");
```

4. 方式三：从指定的输入流中获取，比如使用 IO 流打开图片文件，然后作为参数传入 decodeStream

```Kotlin
public static Bitmap openImage(String path) {
    Bitmap bitmap = null; // 声明一个位图对象
    // 根据指定的文件路径构建文件输入流对象
    try (FileInputStream fis = new FileInputStream(path)) {
    	bitmap = BitmapFactory.decodeStream(fis); // 从文件输入流中解码位图数据
    } catch (Exception e) {
    	e.printStackTrace();
    }
    return bitmap; // 返回图片文件中的位图数据
}
```

5. 获取到图片之后就可以通过 ImageView 的 setImageBitmap 进行设置了
6. 有多种读取图片的方式，但是写图片只有一种方式。通过 Bitmap 的 compress 方法将位图数据压缩到文件输出流

```Kotlin
public static void saveImage(String path, Bitmap bitmap){
    //根据文件路径构建文件输出流
    try(FileOutputStream fos = new FileOutputStream()){
        //将位图数据压缩到文件输出流
        bitmap.compress(Bitmap.CompressFormat.JPEG, 80, fos);
    }catch(Exception e){
        e.printStackTrace();
    }
}
```

#### Ⅱ、代码

1. 创建布局文件 `picture.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/picture_btn_save"
		android:text="保存图片"
		android:textSize="30sp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<Button
		android:id="@+id/picture_btn_get"
		android:text="获取图片"
		android:textSize="30sp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
		
	<ImageView
		android:id="@+id/picture_imageView"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

2. 创建布局文件对应的代码文件 `PictureActivity`

```Kotlin
package com.yuehai.sharedpreferences

import android.Manifest
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import java.io.File
import java.io.FileOutputStream


class PictureActivity: AppCompatActivity() {
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.picture)
		
		// 给获取图片按钮绑定事件
		findViewById<Button>(R.id.picture_btn_get).setOnClickListener {
			
			// 在安卓 6.0（API 23）及以上系统，考虑到安全，访问手机 SD 卡时，不但要加权限，还需要在代码中动态申请权限
			// 判断是否有读取存储卡的权限
			if ( ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED ){
				// 没有权限，进行申请
				ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE), 200)
			}
			
			// 有权限，进行操作
			val bitmap = BitmapFactory.decodeFile("/sdcard/内存/图片/-10971e86458a4bdd.gif")
			findViewById<ImageView>(R.id.picture_imageView).setImageBitmap(bitmap)
		}
		
		// 给保存图片按钮绑定事件
		findViewById<Button>(R.id.picture_btn_save).setOnClickListener {
			
			// 在安卓 6.0（API 23）及以上系统，考虑到安全，访问手机 SD 卡时，不但要加权限，还需要在代码中动态申请权限
			// 判断是否有读取存储卡的权限
			if ( ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED ){
				// 没有权限，进行申请
				ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE), 200)
			}
			
			// 有权限，进行操作
			val bitmap = BitmapFactory.decodeFile("/sdcard/内存/图片/-10971e86458a4bdd.gif")
			
			// 创建输出流
			val fileOutputStream = FileOutputStream(File("/sdcard/内存/test.gif"))
			// 将图片数据压缩到文件输出流
			bitmap.compress(Bitmap.CompressFormat.PNG, 85, fileOutputStream)
			fileOutputStream.flush()
			fileOutputStream.close()
		}
		
		
	}
}
```

3. 修改清单文件 `AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:tools="http://schemas.android.com/tools" xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 存储卡读写权限 -->
	<!-- 在安卓 6.0（API 23）及以上系统，考虑到安全，访问手机 SD 卡时，不但要加权限，还需要在代码中动态申请权限 -->
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
	<!--在sdcard中创建/删除文件的权限 -->
	<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" tools:ignore="ProtectedPermissions"/>
	
	<!--
	    android:name=".MyApplication：注册应用组件 Application
	 -->
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android"
		android:name=".MyApplication"
		android:requestLegacyExternalStorage="true">
		
		<!-- 注册 PictureActivity -->
		<activity
			android:name=".PictureActivity"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口 -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

## 4、应用组件 `Application`

1. Application 是 Android 的一大组件，在 App 运行期间只有一个 Application 对象贯穿整个应用的生命周期。
2. 因此，Application 适合保存全局变量，主要是以下三类数据：
	1. 会频繁读取的信息：如用户名，手机号码等
	2. 不方便通过 intent 传递的数据，如位图对象，非字符串的集合对象等。
	3. 容易因频繁分配内存而导致内存泄漏的对象，如 Handler 处理器实例等。

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420104855.png)

3. 通过 Application 实现对全局内存的读写：
4. 写一个继承自 Application 的类 MyApplication。该类要采用单例模式

```Kotlin
package com.yuehai.sharedpreferences

import android.app.Application

// 继承 Application
object MyApplication : Application() {

    // Application 唯一实例
    private var myApplication: MyApplication = MyApplication
    //当作全局变量，用来存储数据
    var map: MutableMap<String, String> = mutableMapOf()

    override fun onCreate() {
        super.onCreate()
        myApplication = this
    }
}

```

5. 在 `AndroidManifest.xml` 清单文件中注册：`<application android:name=".MyApplication">`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:tools="http://schemas.android.com/tools" xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 存储卡读写权限 -->
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
	<!--在sdcard中创建/删除文件的权限 -->
	<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" tools:ignore="ProtectedPermissions"/>
	
	<!--
	    android:name=".MyApplication：注册应用组件 Application
	 -->
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android"
		android:name=".MyApplication">
		
		<!--
			android:name=".MainActivity"：当前注册的窗口是哪个
			android:exported="true"：表示当前 Activity 是否可以被另一个 Application 的组件启动：true 允许被启动；false 不允许被启动
			android:label="@string/app_name"：标识当前窗口名
			android:launchMode="standard"：指定启动模式
		 -->
		<activity
			android:name=".SharedPreferences01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
		<!-- 注册 -->
		<activity
			android:name=".SharedPreferences02"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
	</application>

</manifest>
```

6. 在 `Activity` 中调用 `MyApplication` 的 `instance()` 方法，获得 `MyApplication` 的一个静态对象，通过该对象访问 `MyApplication` 的公共变量和公共方法
7. 保存数据

```Kotlin
// Application 中保存数据
findViewById<Button>(R.id.yuehai_shared_preferences_01_Application).setOnClickListener {
	// 获取 MyApplication 实例
	val application = MyApplication.instance()
	val applicationData = application.map
	// 保存数据
	applicationData["applicationData"] = "111"
	Log.i("保存数据：", applicationData["applicationData"].toString())

	// 跳转到 SharedPreferences02 窗口，传递 intent 对象
	startActivity(Intent(this, SharedPreferences02().javaClass))
}
```

8. 获取数据

```Kotlin
package com.yuehai.sharedpreferences

import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class SharedPreferences02: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.shared_preferences_02)

        // Application 中获取数据
        findViewById<Button>(R.id.yuehai_shared_preferences_02_Application).setOnClickListener {
            // 获取 MyApplication 实例
            val application = MyApplication.instance()
            val applicationData = application.map
            // 获取数据
            Log.i("applicationData：", applicationData["applicationData"].toString())
        }
    }
}
```

# 七、`Android` 内容共享 `ContentProvider`

## 1、在应用之间共享数据

1. `ContentProvider` 是 Android 的四大组件之二，通过 ContentProvider 封装内部数据的外部访问接口，实现不同应用能够互相传输数据。
2. 和 `ContentProvider` 搭配使用的还有：`ContentResolver`（内容解析器），`ContentObserver`（内容观察器）
3. 上面提到的 SQLite 可以操作自身的数据库，而 `ContentProvider` 则是作为中间接口，通过 `SQLiteOpenHelper` 和 `SQLiteDatabase` 间接操控数据库，实现为其他应用提供数据的功能。
4. 场景：比如微信读取手机通讯录

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420132956.png)

## 2、使用举例

1. 创建一个 `UserInfoProvider`，用来提供用户信息给外界应用
2. 在弹出的右键菜单中依次选择 New→Other→Content Provider，此时会自动修改两处地方：
	1. 一是在 `AndroidManifest.xml` 中添加该 `Provider` 的配置信息
	2. 二是创建的这个 `Provider` 会继承 `ContentProvider`，并重写了一些方法

### ①、创建服务端模块 `05_contentproviderserver`

1. 新建 `xml` 窗口布局文件  `content_provider_server_01.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 按钮；共享参数 -->
	<Button
		android:id="@+id/yuehai_content_provider_server_01_btn"
		android:text="内容共享 - 服务端"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/purple_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>
	
	<TextView
		android:id="@+id/yuehai_content_provider_server_01_text"
		android:text="0"
		android:textSize="100sp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

2. 新建 `activity` 窗口布局对应的代码文件

```Kotlin
package com.yuehai.contentProviderServer

import android.content.ContentValues
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class ContentProviderServer01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.content_provider_server_01)

        // 点击按钮
        findViewById<Button>(R.id.yuehai_content_provider_server_01_btn).setOnClickListener {
            Log.i("点击服务端按钮：", "yuehai_content_provider_server_01_btn")

        }
    }
}
```

3. 在 `AndroidManifest.xml` 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">

		<!-- 注册窗口 -->
		<activity
			android:name="com.yuehai.contentProviderServer.ContentProviderServer01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
	</application>

</manifest>
```

### ②、创建客户端模块 `05_contentproviderclient`

1. 新建 `xml` 窗口布局文件  `activity`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	xmlns:tools="http://schemas.android.com/tools"
	android:orientation="vertical">
	
	<!-- 按钮；共享参数 -->
	<Button
		android:id="@+id/yuehai_content_provider_client_01_btn"
		android:text="内容共享 - 客户端"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/purple_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

	<!-- 列表视图 -->
	<ListView
		android:id="@+id/yuehai_content_provider_client_01_list"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		tools:layout="@layout/list_item"/>

</LinearLayout>
```

2. 新建条目布局文件 `list_item.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent">
	
	<TextView
		android:id="@+id/list_item_text"
		android:textSize="30sp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

3. 新建 `activity` 窗口布局对应的代码文件

```Kotlin
package com.yuehai.contentproviderclinet

import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class ContentProviderClinet01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.content_provider_clinet_01)

        // 点击按钮
        findViewById<Button>(R.id.yuehai_content_provider_client_01_btn).setOnClickListener {
            Log.i("点击客户端按钮：", "yuehai_content_provider_client_01_btn")

        }
    }
}
```

3. 在 `AndroidManifest.xml` 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册窗口 -->
		<activity
			android:name=".ContentProviderClinet01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ③、服务端模块使用 `ContentProvider`

1. 创建实体类 `UserInfo`

```Kotlin
package com.yuehai.contentProviderServer.bean

class UserInfo(
    var name: String,
    var age: Int
) {
}
```

2. 使用上面的 `SQLiteOpenHelper` 实现类 `UserDBHelper`

```Kotlin
package com.yuehai.contentProviderServer.contentProvider

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import com.yuehai.contentProviderServer.bean.UserInfo


/**
 * UserDBHelper 的参数 context：
 *      Context 是一个抽象类，它是 Android 应用程序的环境信息的接口。
 *      Context 提供了访问应用程序资源和类、调用 Activity、广播和接收 Intent 等功能。
 *      在 Android 中，Activity、Service、Application 等都是 Context 的子类，因此它们都可以使用 Context 提供的功能
 *      在 Kotlin 中，您可以使用 this 键字来引用当前上下文。例如，在 Activity 中，您可以使用 this 关键字来引用 Activity 的上下文
 * UserDBHelper 的参数：
 *      1. 上下文环境；第一个参数是必须的
 *      2. 数据库名字；第二个参数如果传入 null，则表示创建临时数据库，在应用退出之后，数据就会丢失
 *      3. 可选的游标工厂；第三个参数如果使用系统默认的游标工厂就传入 null，一般都填 null
 *      4. 代表你正在使用的数据库模型版本的整数；第四个参数用版本号来控制数据库的升级和降级，版本号从 1 开始
 */
class UserDBHelper(
    context: Context,
    val tableName:String,
    version:Int
): SQLiteOpenHelper(context, tableName, null, version) {

    // onCreate() 方法在数据库第一次创建时执行，一般将创建表等初始化操作在该方法中执行
    override fun onCreate(db: SQLiteDatabase?) {
        // 判断表是否存在；如果返回的数组计数等于1，则表示该表存在。否则，该表不存在
        val cursor = db?.rawQuery("SELECT name FROM sqlite_master WHERE type='table' AND name='$tableName'", null)

        if(cursor?.count!! != 1){
            // 创建表
            val createSql = (
                    "CREATE TABLE IF NOT EXISTS $tableName" + " ("
                            + "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                            + "name VARCHAR NOT NULL,"
                            + "age INTEGER NOT NULL);"
                    )

            db.execSQL(createSql)
        }

        cursor.close()
    }

    // onUpgrade() 方法在打开数据库时传入的版本号与当前的版本号不同时会调用该方法，一般将升级数据库等操作在该方法中执行
    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        // Android 的 ALTER 命令不支持一次添加多列，只能分多次添加
        var alterSql = "ALTER TABLE $tableName ADD COLUMN phone VARCHAR;"
        db!!.execSQL(alterSql)

        alterSql = "ALTER TABLE $tableName ADD COLUMN password VARCHAR;"
        db.execSQL(alterSql)

    }

    // 往表里添加一条记录
    fun insert(db: SQLiteDatabase?, userinfo: UserInfo){
        // 获取 ContentValues 对象
        val contentValues = ContentValues()
        // 向 ContentValues 对象中添加数据
        contentValues.put("name", userinfo.name)
        contentValues.put("age", userinfo.age)

        // 保存数据
        db?.insert(tableName, "", contentValues)
    }

    // 根据条件查询记录
    fun query(db: SQLiteDatabase?, name:String): MutableList<UserInfo> {
        // 拼接语句
        val sql = "select id,name,age from $tableName where name=$name;"
        // 执行查询语句，该语句返回结果集的游标
        val rawQuery = db?.rawQuery(sql, null);

        // 定义可变集合；
        val userList:MutableList<UserInfo> = mutableListOf()
        // 遍历游标，取出数据
        if (rawQuery != null) {
            while (rawQuery.moveToNext()){
                userList.add(UserInfo(rawQuery.getString(1), rawQuery.getInt(2)))
            }

            rawQuery.close()
        }

        return userList
    }


}
```

3. 创建 `UserInfoProvider` 继承 `ContentProvider`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420142041.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420142150.png)

```Kotlin
package com.yuehai.contentProviderServer.contentProvider

import android.content.ContentProvider
import android.content.ContentValues
import android.database.Cursor
import android.net.Uri

class UserInfoProvider : ContentProvider() {

    private var userDBHelper: UserDBHelper? = null

    /**
     * ContentProvider 只是服务端 App 存取数据的抽象类，我们需要在其基础上实现一个完整的内容提供器，并重写下列方法。
     *      onCreate：创建数据库并获得数据库连接
     *      insert：插入数据
     *      delete：删除数据
     *      update：更新数据
     *      query：查询数据，并返回结果集的游标
     *      getType：获取内容提供器支持的数据类型
     */

    // 创建数据库并获得数据库连接
    override fun onCreate(): Boolean {
        userDBHelper = UserDBHelper(context!!, "yuehai", 1)

        return true
    }

    // 插入数据
    override fun insert(uri: Uri, values: ContentValues?): Uri? {
        val database = userDBHelper?.writableDatabase
        database?.insert(userDBHelper?.tableName, null, values)

        return uri
    }

    // 删除数据
    override fun delete(uri: Uri, selection: String?, selectionArgs: Array<String>?): Int {
        TODO("Implement this to handle requests to delete one or more rows")
    }

    // 更新数据
    override fun update(
        uri: Uri, values: ContentValues?, selection: String?,
        selectionArgs: Array<String>?
    ): Int {
        TODO("Implement this to handle requests to update one or more rows.")
    }

    // 查询数据，并返回结果集的游标
    override fun query(
        uri: Uri, projection: Array<String>?, selection: String?,
        selectionArgs: Array<String>?, sortOrder: String?
    ): Cursor? {
        val database = userDBHelper?.readableDatabase
        return database?.query(userDBHelper?.tableName, projection, selection, selectionArgs, null, null, null)
    }

    // 获取内容提供器支持的数据类型
    override fun getType(uri: Uri): String? {
        TODO(
            "Implement this to handle requests for the MIME type of the data" +
                    "at the given URI"
        )
    }

}
```

4. 此时的 `AndroidManifest.xml` 清单文件，修改 `android:authorities` 属性

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">
		
		<!--
			内容共享 ContentProvider
			android:name：Provider 全类路径
			android:authorities：指定授权者(自定义字符串)
			android:enabled：是否可以被系统实例化，默认为 true 因为父标签 也有 enable 属性，所以必须两个都为默认值 true 的情况下服务才会被激活，否则不会激活
			android:exported：跨应用共享数据 设置为 true 默认为 false；表示该 provider 能够被其他应用程序组件调用
		 -->
		<provider
			android:name=".contentProvider.UserInfoProvider"
			android:authorities="com.yuehai.contentproviderserver.contentProvider.UserInfoProvider"
			android:enabled="true"
			android:exported="true" />
		
		<!-- 注册窗口 -->
		<activity
			android:name=".ContentProviderServer01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
	</application>

</manifest>
```

5. 编写 `ContentProviderServer01.kt` 代码文件，保存数据

```Kotlin
package com.yuehai.contentproviderserver

import android.content.ContentValues
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ContentProviderServer01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.content_provider_server_01)

        // 定义 uri
        val contentUri: Uri = Uri.parse("content://com.yuehai.contentproviderserver.contentProvider.UserInfoProvider/yuehai")

        // 点击按钮
        findViewById<Button>(R.id.yuehai_content_provider_server_01_btn).setOnClickListener {
            Log.i("点击服务端按钮：", "yuehai_content_provider_server_01_btn")
            
            // 获取文本框对象
            val textView = findViewById<TextView>(R.id.yuehai_content_provider_server_01_text)
            // 文本框内容 + 1，赋值给 age
            val age = textView.text.toString().toInt() + 1
            // 使文本框内容 + 1
            textView.text = age.toString()
            
            // 创建 ContentValues 对象
            val contentValues = ContentValues()
            contentValues.put("name", "言")
            contentValues.put("age", age)

            // 获取到 ContentResolver 之后调用插入方法进行插入
            contentResolver.insert(contentUri, contentValues)
        }
    }
}
```

### ④、客户端模块使用 `ContentProvider`

1. 出于安全考虑，Android11 需要事先声明需要访问的其他应用，在客户端 `AndroidManifest.xml` 清单文件中添加如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<queries>
		<!--服务端应用包名 -->
		<package android:name="com.yuehai.contentproviderserver"/>
		
		<!-- 或者直接指定 authorities -->
		<!-- <provider android:authorities="com.yuehai.contentproviderserver.contentProvider.UserInfoProvider"/> -->
	</queries>
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册窗口 -->
		<activity
			android:name=".ContentProviderClinet01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

2. 编写 `ContentProviderClinet01.kt` 代码文件，读取数据

```Kotlin
package com.yuehai.contentproviderclinet

import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.ListView
import android.widget.SimpleAdapter
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ContentProviderClinet01: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.content_provider_clinet_01)

        // 定义 uri
        val contentUri: Uri = Uri.parse("content://com.yuehai.contentproviderserver.contentProvider.UserInfoProvider/yuehai")

        // 点击按钮
        findViewById<Button>(R.id.yuehai_content_provider_client_01_btn).setOnClickListener {
            Log.i("点击客户端按钮：", "yuehai_content_provider_client_01_btn")
    
            // 声明一个集合，用于保存信息
            val list: MutableList<Map<String, Any?>> = ArrayList()
            // 查询
            val query = contentResolver.query(contentUri, null, null, null, null)
            // 遍历游标，取出数据
            if (query != null) {
                while (query.moveToNext()){
                    // 给集合赋值
                    val item: MutableMap<String, Any?> = HashMap()
                    item["data"] = "id：${query.getInt(0)}，name：${query.getString(1)}，age：${query.getInt(2)}"
                    list.add(item)
                }
            }
    
            /**
             * 声明一个下拉列表的简单适配器，其中指定了图标与文本两组数据
             * SimpleAdapter(Context context, List<? extends Map<String, ?>> data, int resource, String[] from, int[] to)
             * 第一个参数 context：SimpleAdapter 关联的 View 的运行环境；上下文环境
             * 第二个参数 data：  一个 Map 组成的 List。列表种的每个条目对应列表中的一行，每个 Map 中应该包含 from 参数中指定的键
             * 第三个参数 resource：定义列表项的布局文件的资源 id
             * 第四个参数 from：  被添加到 Map 映射上的键名
             * 第五个参数 to：    将绑定数据的视图的 Id 和 from 参数对应；from 与 to 一一对应，适配器绑定数据
             */
            val startAdapter = SimpleAdapter(
                this,
                list,
                R.layout.list_item,
                arrayOf<String>("data"),
                intArrayOf(R.id.list_item_text)
            )
    
            // 获取列表对象
            val clientList = findViewById<ListView>(R.id.yuehai_content_provider_client_01_list)
            // 传入适配器实例
            clientList.adapter = startAdapter
        }

    }
    
}
```

### ⑤、结果

1. 服务端

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230512123201.png)

2. 客户端

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230512123308.png)

## 3、运行时动态申请权限

1. 在上面讲公共存储空间与私有存储空间提到，App 若想访问存储卡的公共空间，就要在 `AndroidManifest.xml` 清单文件里面添加下述的权限配置

```xml
<!-- 存储卡读写权限 -->
<!-- 在安卓 6.0（API 23）及以上系统，考虑到安全，访问手机 SD 卡时，不但要加权限，还需要在代码中动态申请权限 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
```

2. 然而即使 App 声明了完整的存储卡操作权限，从 Android 7.0 开始，系统仍然默认禁止该 App 访问公共空间，必须到设置界面手动开启应用的存储卡权限才行。尽管此举是为用户隐私着想，可是人家咋知道要手工开权限呢？就算用户知道，去设置界面找到权限开关也颇费周折。为此 Android 支持在 Java 代码中处理权限，处理过程分为 3 个步骤：
	1. 检查 App 是否开启了指定权限：调用 `ContextCompat` 的 `checkSelfPermission` 方法
	2. 请求系统弹窗，以便用户选择是否开启权限：调用 `ActivityCompat` 的 `requestPermissions` 方法，即可命令系统自动弹出权限申请窗口。
	3. 判断用户的权限选择结果，是开启还是拒绝：重写活动页面的权限请求回调方法 `onRequestPermissionsResult`，在该方法内部处理用户的权限选择结果
3. 动态申请权限有两种方式：<font color="#ff0000">饿汉式</font>和<font color="#ff0000">懒汉式</font>。接下来通过获取通讯权限和短信权限来进行举例说明

### ①、懒汉式

> 懒汉式：当需要某种权限的时候再去申请

1. 创建工具类 `PermissionUtil`

```Kotlin
package com.yuehai.contentproviderclinet.util

import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.provider.Settings
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat


class PermissionUtil {
	
	/**
	 * 检查权限
	 * @param activity 当前 activity
	 * @param permissions 权限数组
	 * @param requestCode 权限申请识别码
	 * @return 返回 true 表示完全启用权限，返回 false 则表示未完全启用所有权限
	 */
	fun checkPermission(activity: Activity, permissions: Array<String>, requestCode: Int): Boolean{
		
		// 获取权限检查值
		var check = PackageManager.PERMISSION_GRANTED
		
		// 循环判断权限是否存在
		for (permission in permissions) {
			// 获取权限检查结果，给权限检查值赋值
			check = ContextCompat.checkSelfPermission(activity, permission)
			// 判断权限是否存在
			if (check != PackageManager.PERMISSION_GRANTED){
				// 数组中有一个权限不存在，就结束循环
				break
			}
		}
		
		/**
		 * 判断权限检查值，若有权限不存在，则请求系统弹窗，好让用户选择是否开启权限
		 *
		 * 为什么不在循环里请求权限的原因是：
		 *      判断权限是一个一个判断的
		 *      请求权限是可以一组一起获取的
		 */
		if (check != PackageManager.PERMISSION_GRANTED){
			// 请求权限
			ActivityCompat.requestPermissions(activity, permissions, requestCode)
			return false
		}
		
		// 所有权限都存在
		return true
	}
	
	/**
	 * 根据权限申请回调函数返回的权限申请结果数组，判断申请是否成功
	 *
	 * @param grantResults 权限申请结果数组
	 * @return 返回 true 表示都已经授权
	 */
	fun checkGrant(grantResults: IntArray): Boolean {
		// 遍历数组
		grantResults.forEach {
			// 判断结果，权限是否申请成功
			if (it != PackageManager.PERMISSION_GRANTED){
				// 权限申请失败
				return false
			}
		}
		
		// 权限申请成功
		return true
	}
	
	/**
	 * 跳转到设置界面
	 */
	fun jumpToSettings(activity: Activity, packageName: String){
		val intent = Intent()
		intent.action = Settings.ACTION_APPLICATION_DETAILS_SETTINGS
		intent.data = Uri.fromParts("package", packageName, null)
		intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
		activity.startActivity(intent)
	}
	
}
```

2. 创建布局文件 `permission_lazy.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/permission_lazy_contact"
		android:text="获取通讯录权限"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<Button
		android:id="@+id/permission_lazy_sms"
		android:text="获取短信权限"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

3. 创建布局文件对应的代码文件 `PermissionLazyActivity`

```Kotlin
package com.yuehai.contentproviderclinet

import android.Manifest
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.contentproviderclinet.util.PermissionUtil

class PermissionLazyActivity: AppCompatActivity() {
	
	// 通讯录的读写权限
	private val PERMISSION_CONTACT = arrayOf<String>(
		Manifest.permission.READ_CONTACTS,
		Manifest.permission.WRITE_CONTACTS
	)
	// 通讯录的读写权限申请识别码，作为回调识别参数
	private val PERMISSION_CONTACT_CODE = 1
	
	// 短信的读写权限
	private val PERMISSION_SMS = arrayOf<String>(
		Manifest.permission.SEND_SMS,
		Manifest.permission.RECEIVE_SMS
	)
	// 通讯录的读写权限申请识别码，作为回调识别参数
	private val PERMISSION_SMS_CODE = 2
	
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.permission_lazy)
		
		// 获取通讯录的读写权限
		findViewById<Button>(R.id.permission_lazy_contact).setOnClickListener {
			// 调用封装的方法，检查并获取权限
			PermissionUtil().checkPermission(this, PERMISSION_CONTACT, PERMISSION_CONTACT_CODE)
		}
		
		// 获取短信的读写权限
		findViewById<Button>(R.id.permission_lazy_sms).setOnClickListener {
			// 调用封装的方法，检查并获取权限
			PermissionUtil().checkPermission(this, PERMISSION_SMS, PERMISSION_SMS_CODE)
		}
	}
	
	/**
	 * 用户选择权限结果后会调用该回调方法
	 *
	 * 参数 1：权限申请识别码
	 * 参数 2：权限列表
	 * 参数 3：权限申请结果数组
	 */
	override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray ) {
		super.onRequestPermissionsResult(requestCode, permissions, grantResults)
		
		// 根据权限申请识别码判断是申请什么判断的回调
		when(requestCode){
			// 通讯录的读写权限回调
			PERMISSION_CONTACT_CODE -> {
				// 调用封装的方法，判断权限申请是否成功
				if (PermissionUtil().checkGrant(grantResults)){
					Log.d("月海", "通讯录获取成功")
				}else{
					Log.d("月海", "通讯录获取失败")
					// 跳转到设置界面
					PermissionUtil().jumpToSettings(this, packageName)
				}
			}
			// 短信的读写权限回调
			PERMISSION_SMS_CODE -> {
				// 调用封装的方法，判断权限申请是否成功
				if (PermissionUtil().checkGrant(grantResults)){
					Log.d("月海", "短信获取成功")
				}else{
					Log.d("月海", "短信获取失败")
					// 跳转到设置界面
					PermissionUtil().jumpToSettings(this, packageName)
				}
			}
		}
	}

}
```

4. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- uses-feature 用来声明应用中需要用的硬件和软件的功能 -->
	<!-- 该应用程序使用电话功能的移动设备，例如，电话与数据通信业务的无线电 -->
	<uses-feature android:name="android.hardware.telephony" android:required="false" />
	
	<!-- 开启通讯录权限-->
	<uses-permission android:name="android.permission.READ_CONTACTS"/>
	<uses-permission android:name="android.permission.WRITE_CONTACTS"/>
	
	<!-- 开启短信收发权限-->
	<uses-permission android:name="android.permission.SEND_SMS"/>
	<uses-permission android:name="android.permission.RECEIVE_SMS"/>
	
	<queries>
		<!--服务端应用包名 -->
		<package android:name="com.yuehai.contentproviderserver"/>
		
		<!-- 或者直接指定 authorities -->
		<!-- <provider android:authorities="com.yuehai.contentproviderserver.contentProvider.UserInfoProvider"/> -->
	</queries>
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册窗口 -->
		<activity
			android:name=".ContentProviderClinet01"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册窗口 -->
		<activity
			android:name=".PermissionLazyActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口 -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ②、饿汉式

> 懒汉式：在页面打开之后就一次性需要用户获取所有权限

1. 创建布局文件 `permission_lazy.xml`，和上面一样，就是改了个名

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<Button
		android:id="@+id/permission_lazy_contact"
		android:text="获取通讯录权限"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<Button
		android:id="@+id/permission_lazy_sms"
		android:text="获取短信权限"
		android:textSize="30dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

2. 创建布局文件对应的代码文件 `PermissionLazyActivity`

```Kotlin
package com.yuehai.contentproviderclinet

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.contentproviderclinet.util.PermissionUtil

class PermissionHungryActivity: AppCompatActivity() {
	
	// 所需全部读写权限
	private val PERMISSIONS = arrayOf(
		Manifest.permission.READ_CONTACTS,
		Manifest.permission.WRITE_CONTACTS,
		Manifest.permission.SEND_SMS,
		Manifest.permission.RECEIVE_SMS
	)
	// 权限申请识别码，作为回调识别参数
	private val REQUEST_CODE_ALL = 0
	
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.permission_hungry)
		
		// 检查是否拥有所有所需权限
		PermissionUtil().checkPermission(this, PERMISSIONS, REQUEST_CODE_ALL)
	}
	
	/**
	 * 用户选择权限结果后会调用该回调方法
	 *
	 * 参数 1：权限申请识别码
	 * 参数 2：权限列表
	 * 参数 3：权限申请结果数组
	 */
	override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray ) {
		super.onRequestPermissionsResult(requestCode, permissions, grantResults)
		
		// 根据权限申请识别码判断是申请什么判断的回调
		when(requestCode){
			// 通讯录的读写权限回调
			REQUEST_CODE_ALL -> {
				// 调用封装的方法，判断权限申请是否成功
				if (PermissionUtil().checkGrant(grantResults)){
					Log.d("月海", "所有权限获取成功")
				}else{
					
					// 部分权限获取失败，
					for ( (index, grantResult) in grantResults.withIndex() ) {
						
						// 判断本次循环返回的结果是申请失败
						if (grantResult != PackageManager.PERMISSION_GRANTED){
							// 判断是什么权限获取失败
							when(permissions[index]){
								// 通讯录权限
								Manifest.permission.READ_CONTACTS,
								Manifest.permission.WRITE_CONTACTS -> {
									Log.d("月海", "通讯录获取失败")
									// 跳转到设置界面
									PermissionUtil().jumpToSettings(this, packageName)
								}
								// 短信权限
								Manifest.permission.SEND_SMS,
								Manifest.permission.RECEIVE_SMS -> {
									Log.d("月海", "短信获取失败")
									// 跳转到设置界面
									PermissionUtil().jumpToSettings(this, packageName)
								}
							}
						}
						
					}
					
				}
			}

		}
	}
}
```

3. 修改 `AndroidManifest.xml` 清单文件

```xml
<!-- 注册窗口 -->
<activity
	android:name=".PermissionHungryActivity"
	android:exported="true">
	<intent-filter>
		<!-- 配置为主窗口 -->
		<action android:name="android.intent.action.MAIN" />
		<category android:name="android.intent.category.LAUNCHER" />
	</intent-filter>
</activity>
```

## 4、使用内容组件获取通讯信息

### ①、说明

1. 手机中通讯录的主要表结构有：
2. `raw_contacts` 表：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230512155543.png)

3. `data` 表：记录了用户的通讯录所有数据，包括手机号，显示名称等
	1. 里面的 `mimetype_id` 表示不同的数据类型，这与表 `mimetypes` 表中的 `id` 相对应
	2. `raw_contact_id` 与上面的 `raw_contacts` 表中的 id 相对应。

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230512155551.png)

4. `mimetypes` 表：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230512155605.png)

### ②、代码例子

## 5、在应用之间共享文件

### ①、通过系统相册获取图片和视频

1. 创建布局文件 `album_get_pictures.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical"
	android:layout_gravity="center">

	<Button
		android:id="@+id/album_get_pictures"
		android:text="从相册获取图片"
		android:textSize="20sp"
		android:layout_gravity="center"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<Button
		android:id="@+id/album_get_video"
		android:text="从相册获取视频"
		android:textSize="20sp"
		android:layout_gravity="center"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<Button
		android:id="@+id/album_get_all"
		android:text="从相册获取和图片和视频"
		android:textSize="20sp"
		android:layout_gravity="center"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
	<ImageView
		android:id="@+id/pictures_and_video"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />
	
</LinearLayout>
```

2. 创建布局文件对应的代码文件 `AlbumGetPicturesActivity`

```Kotlin
package com.yuehai.contentproviderclinet

import android.Manifest
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.contentproviderclinet.util.PermissionUtil

class AlbumGetPicturesActivity: AppCompatActivity() {
	
	// 存储卡读写权限
	private val PERMISSIONS_STORAGE = arrayOf(
		Manifest.permission.WRITE_EXTERNAL_STORAGE,
		Manifest.permission.READ_EXTERNAL_STORAGE,
	)
	// 权限申请识别码，作为回调识别参数
	private val REQUEST_CODE_ALL = 0
	
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.album_get_pictures)
		
		// 从相册获取图片按钮
		findViewById<Button>(R.id.album_get_pictures).setOnClickListener {
			// 调用封装的方法，检查并获取权限
			if (PermissionUtil().checkPermission(this, PERMISSIONS_STORAGE, REQUEST_CODE_ALL)){
				/**
				 * 获取图片资源；传入的参数就是你想要选择的资源类型
				 *
				 * launch("image/ *") 是一个 MIME 类型，它指定了要启动的 Activity 的类型。在这种情况下，它指定了要启动的 Activity 是一个图像选择器
				 * https://www.runoob.com/http/mime-types.html
				 */
				getPicturesOrVideoResultLauncher.launch("image/*")
			}
		}
		
		// 从相册获取视频按钮
		findViewById<Button>(R.id.album_get_video).setOnClickListener {
			// 调用封装的方法，检查并获取权限
			if (PermissionUtil().checkPermission(this, PERMISSIONS_STORAGE, REQUEST_CODE_ALL)){
				// 获取视频资源
				getPicturesOrVideoResultLauncher.launch("video/*")
			}
		}
		
		// 从相册获取和图片和视频按钮
		// 从相册获取视频按钮
		findViewById<Button>(R.id.album_get_all).setOnClickListener {
			// 调用封装的方法，检查并获取权限
			if (PermissionUtil().checkPermission(this, PERMISSIONS_STORAGE, REQUEST_CODE_ALL)){
				// 获取视频资源
				getPicturesAndVideoResultLauncher.launch(arrayOf("image/*", "video/*"))
			}
		}
	}
	
	/**
	 * 获取图片或视频
	 * 回调函数，重写 onActivityResult() 方法，接收上一个 Activity 中返回的消息
	 *
	 * registerForActivityResult() 是 Android 中的一个 API，用于在 Activity 或 Fragment 中注册结果回调。
	 * registerForActivityResult() 接受一个 ActivityResultContract 和一个 ActivityResultCallback，
	 * 并返回一个 ActivityResultLauncher，你将使用它来启动其他 Activity。
	 * 当你调用 registerForActivityResult() 时，它会返回一个 ActivityResultLauncher 实例，该实例负责启动其他 Activity 并发出请求以获取结果。
	 * 如果输入存在，则启动器会获取与 ActivityResultContract 类型匹配的输入
	 *
	 * 参数：
	 *      GetContent()：从相册中获取图片
	 *      StartActivityForResult()：启动另一个 Activity 并返回结果。
	 *      RequestPermission()：请求权限并返回结果。
	 *      TakePicturePreview()：拍摄照片并返回预览。
	 *      TakePicture()：拍摄照片并返回结果。
	 *      TakeVideo()：拍摄视频并返回结果
	 *      OpenDocument()：可以选择多个文件；和 GetContent() 的区别
	 *          GetContent() 只能选择一个文件，而 OpenDocument() 可以选择多个文件。
	 *          GetContent() 只能选择特定类型的文件（例如图片、视频等），而 OpenDocument() 可以选择任何类型的文件。
	 *          GetContent() 返回的 Uri 是指向文件的内容，而 OpenDocument() 返回的 Uri 是指向文档的元数据
 	 */
	private val getPicturesOrVideoResultLauncher = registerForActivityResult(ActivityResultContracts.GetContent()) { uri ->
			// 设置数据；uri 即是返回的选择的图片的 uri
			findViewById<ImageView>(R.id.pictures_and_video).setImageURI(uri)
	}
	
	// 获取图片和视频
	private val getPicturesAndVideoResultLauncher = registerForActivityResult(ActivityResultContracts.OpenDocument()) { uri ->
		// 设置数据；uri 即是返回的选择的图片的 uri
		findViewById<ImageView>(R.id.pictures_and_video).setImageURI(uri)
	}
}
```

3. 修改 `AndroidManifest.xml` 清单文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- uses-feature 用来声明应用中需要用的硬件和软件的功能 -->
	<!-- 该应用程序使用电话功能的移动设备，例如，电话与数据通信业务的无线电 -->
	<uses-feature android:name="android.hardware.telephony" android:required="false" />
	
	<!-- 开启通讯录权限-->
	<uses-permission android:name="android.permission.READ_CONTACTS"/>
	<uses-permission android:name="android.permission.WRITE_CONTACTS"/>
	
	<!-- 开启短信收发权限-->
	<uses-permission android:name="android.permission.SEND_SMS"/>
	<uses-permission android:name="android.permission.RECEIVE_SMS"/>
	
	<!-- 存储卡读写权限 -->
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
	
	<queries>
		<!--服务端应用包名 -->
		<package android:name="com.yuehai.contentproviderserver"/>
		
		<!-- 或者直接指定 authorities -->
		<!-- <provider android:authorities="com.yuehai.contentproviderserver.contentProvider.UserInfoProvider"/> -->
	</queries>
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册窗口；数据共享客户端模块 ContentProviderClinet01 -->
		<activity
			android:name=".ContentProviderClinet01"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册窗口；权限申请，懒汉式 -->
		<activity
			android:name=".PermissionLazyActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册窗口；权限申请，饿汉式 -->
		<activity
			android:name=".PermissionHungryActivity"
			android:exported="true">
		</activity>
		
		<!-- 注册窗口；从相册获取图片 -->
		<activity
			android:name=".AlbumGetPicturesActivity"
			android:exported="true">
			<intent-filter>
				<!-- 配置为主窗口 -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ②、借助 FileProvider 发送彩信

### ③、借助 FileProvider 安装应用

# 八、`Android` 广播组件 `Broadcast`

## 1、简介

1. 广播组件 Broadcast 是Android 四大组件之三。
2. 广播有以下特点：
	1. 活动只能一对一通信；而广播可以一对多，一人发送广播，多人接收处理。
	2. 对于发送方来说，广播不需要考虑接收方有没有在工作，接收方在工作就接收广播，不在工作就丢弃广播。
	3. 对于接收方来说，因为可能会收到各式各样的广播，所以接收方要自行过滤符合条件的广播，之后再解包处理
3. 与广播有关的方法主要有以下3个。
	1. `sendBroadcast`：发送广播。
	2. `registerReceiver`：注册广播的接收器，可在 `onStart` 或 `onResume` 方法中注册接收器。
	3. `unregisterReceiver`：注销广播的接收器，可在 `onStop` 或 `onPause` 方法中注销接收器。

## 2、收发应用广播

### ①、标准（无序）广播 `sendBroadcast`

1. 广播的收发过程分为三个步骤：
	1. 定义广播接收器
	2. 发送标准广播
	3. 开关广播接收器
2. 定义广播接收器，继承 `BroadcastReceiver`，实现 `onReceive` 方法

```Kotlin
package com.yuehai.broadcast.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

// 定义一个标准广播的接收器，继承 BroadcastReceiver，实现 onReceive 方法
class StandardReceiver: BroadcastReceiver() {

    // 定义常量，广播名，用以接收指定广播名的广播
    val STANDARD_ACTION:String = "com.yuehai.broadcast.standard"

    // 一旦接收到标准广播，马上触发接收器的 onReceive 方法
    override fun onReceive(context: Context?, intent: Intent?) {
        // 判断收到的 intent 不为空，且为指定广播名的广播
        if(intent != null && intent.action.equals(STANDARD_ACTION)){
            Log.d("月海", "收到一个标准广播");
        }
    }
}
```

3. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent">
	
	<!-- 发送标准广播 -->
	<Button
		android:id="@+id/yuehai_broadcast_01_btn"
		android:text="发送标准广播"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/purple_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

</LinearLayout>
```

3. 创建布局文件对应的代码文件，发送广播，开关广播接收器

```Kotlin
package com.yuehai.broadcast

import android.content.Intent
import android.content.IntentFilter
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.broadcast.receiver.StandardReceiver


class Broadcast01: AppCompatActivity() {

    // 实例化 StandardReceiver 类；接收 com.yuehai.broadcast.standard 广播
    private var standardReceiver = StandardReceiver()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.broadcast_01)

        // 点击按钮，发送标准广播
        findViewById<Button>(R.id.yuehai_broadcast_01_btn).setOnClickListener {
            // 定义发送的广播名
            val intent = Intent(standardReceiver.STANDARD_ACTION)
            // 发送标准广播
            sendBroadcast(intent)
        }

    }

    // 注册广播接收器
    override fun onStart() {
        super.onStart()

        // 创建一个意图过滤器，只处理 STANDARD_ACTION 的广播
        val filter = IntentFilter(standardReceiver.STANDARD_ACTION)
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(standardReceiver, filter)
    }

    // 注销广播接收器
    override fun onStop() {
        super.onStop()

        // 注销接收器，注销之后就不再接收广播
        unregisterReceiver(standardReceiver)
    }
}
```

4. 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 -->
		<activity
			android:name=".Broadcast01"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ②、有序广播 `sendOrderedBroadcast`

1. 由于广播没指定唯一的接收者，因此可能存在多个接收器，每个接收器都拥有自己的处理逻辑。
2. 这些接收器默认是都能够接受到指定广播并且是之间的顺序按照注册的先后顺序，也可以通过指定优先级来指定顺序。
3. 先收到广播的接收器 A，既可以让其他接收器继续收听广播，也可以中断广播不让其他接收器收听。

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230421094256.png)

4. 定义广播接收器，继承 `BroadcastReceiver`，实现 `onReceive` 方法；定义 `OrderAReceiver` 和 `OrderBReceiver` 两个广播接收器

```Kotlin
package com.yuehai.broadcast.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

// 定义一个有序广播的接收器，继承 BroadcastReceiver，实现 onReceive 方法
class OrderAReceiver: BroadcastReceiver() {

    // 定义常量，广播名，用以接收指定广播名的广播
    val ORDER_ACTION:String = "com.yuehai.broadcast.order"

    // 一旦接收到广播，马上触发接收器的 onReceive 方法
    override fun onReceive(context: Context?, intent: Intent?) {
        // 判断收到的 intent 不为空，且为指定广播名的广播
        if(intent != null && intent.action.equals(ORDER_ACTION)){
            Log.d("月海 OrderAReceiver", "收到一个有序广播");
        }
    }
}
```

```Kotlin
package com.yuehai.broadcast.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

// 定义一个有序广播的接收器，继承 BroadcastReceiver，实现 onReceive 方法
class OrderBReceiver: BroadcastReceiver() {

    // 定义常量，广播名，用以接收指定广播名的广播
    val ORDER_ACTION:String = "com.yuehai.broadcast.order"

    // 一旦接收到广播，马上触发接收器的 onReceive 方法
    override fun onReceive(context: Context?, intent: Intent?) {
        // 判断收到的 intent 不为空，且为指定广播名的广播
        if(intent != null && intent.action.equals(ORDER_ACTION)){
            Log.d("月海 OrderBReceiver", "收到一个有序广播");

            // 中断广播
            abortBroadcast()
        }
    }
}
```

5. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	<!-- 发送有序广播 -->
	<Button
		android:id="@+id/yuehai_broadcast_02_btn"
		android:text="发送有序广播"
		android:textSize="30dp"
		android:textColor="@color/black"
		android:backgroundTint="@color/purple_200"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

</LinearLayout>
```

6. 创建布局文件对应的代码文件，发送广播，开关广播接收器

```Kotlin
package com.yuehai.broadcast

import android.content.Intent
import android.content.IntentFilter
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.broadcast.receiver.OrderAReceiver
import com.yuehai.broadcast.receiver.OrderBReceiver


class Broadcast02: AppCompatActivity() {

    // 实例化 orderAReceiver 类；接收 com.yuehai.broadcast.order 广播
    private var orderAReceiver = OrderAReceiver()
    private var orderBReceiver = OrderBReceiver()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.broadcast_02)

        // 点击按钮，发送有序广播
        findViewById<Button>(R.id.yuehai_broadcast_02_btn).setOnClickListener {
            // 定义发送的广播名
            val intent = Intent(orderAReceiver.ORDER_ACTION)
            // 发送有序广播
            sendOrderedBroadcast(intent, null)
        }

    }

    // 注册广播接收器
    override fun onStart() {
        super.onStart()

        // 多个接收器处理有序广播的顺序规则为：
        // 1、优先级越大的接收器，越早收到有序广播；
        // 2、优先级相同的时候，越早注册的接收器越早收到有序广播

        // 创建一个意图过滤器 A，只处理 orderAReceiver 的广播，优先级为 8
        val filterA = IntentFilter(orderAReceiver.ORDER_ACTION)
        filterA.priority = 4
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(orderAReceiver, filterA)

        // 创建一个意图过滤器 B，只处理 orderBReceiver 的广播，优先级为 20
        val filterB = IntentFilter(orderBReceiver.ORDER_ACTION)
        filterB.priority = 8
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(orderBReceiver, filterB)
    }

    // 注销广播接收器
    override fun onStop() {
        super.onStop()

        // 注销接收器，注销之后就不再接收广播
        unregisterReceiver(orderAReceiver)
        unregisterReceiver(orderBReceiver)
    }
}
```

7. 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 -->
		<activity
			android:name=".Broadcast01"
			android:exported="true"
			android:label="@string/app_name">
			<!-- <intent-filter> -->
			<!-- 	&lt;!&ndash; 配置为主窗口， &ndash;&gt; -->
			<!-- 	<action android:name="android.intent.action.MAIN" /> -->
			<!-- 	<category android:name="android.intent.category.LAUNCHER" /> -->
			<!-- </intent-filter> -->
		</activity>
		
		<!-- 注册 -->
		<activity
			android:name=".Broadcast02"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ③、静态广播

1. 广播也可以通过静态代码的方式来进行注册。
2. 广播接收器也能在 `AndroidManifest.xml` 注册，并且注册时候的节点名为 receiver，一旦接收器在 `AndroidManifest.xml` 注册，就无须在代码中注册了。
3. 之所以罕见静态注册，是因为静态注册容易导致安全问题，故而 Android 8.0 之后废弃了大多数静态注册。
4. 静态广播的实现方式这里暂不介绍，可自行查阅资料。

## 3、监听系统广播

### ①、简介

1. 除了应用自身的广播，系统也会发出各式各样的广播
2. 通过监听这些系统广播，App 能够得知周围环境发生了什么变化，从而按照最新环境调整运行逻辑。‘
3. 接下来举几个系统广播的例子。

| 广播名           | 描述                    |
| ---------------- | ----------------------- |
| 接收分钟到达广播 | Intent.ACTION_TIME_TICK |
| 接收网络变更广播 | android.net.conn.CONNECTIVITY_CHANGE                        |

### ②、监听分钟到达广播（分钟变更）

1. 定义一个分钟广播的接收器，并重写接收器的 `onReceive` 方法，补充收到广播之后的处理逻辑。

```Kotlin
package com.yuehai.broadcast.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.icu.text.SimpleDateFormat
import android.icu.util.Calendar
import android.util.Log
import android.widget.TextView
import com.yuehai.broadcast.SystemMinuteActivity

// 定义一个分钟广播的接收器，继承 BroadcastReceiver，实现 onReceive 方法
class SystemMinuteReceiver: BroadcastReceiver() {

    // 定义常量，广播名，用以接收指定广播名的广播；每分钟变化
    val systemMinuteReceiverName:String = Intent.ACTION_TIME_TICK

    // 声明一个文本视图对象，等待 activity 传递
    var text:TextView? = null

    // 一旦接收到分钟变更的广播，马上触发接收器的 onReceive 方法
    override fun onReceive(context: Context?, intent: Intent?) {
        // 判断收到的 intent 不为空，且为指定广播名的广播
        if((intent != null) && intent.action.equals(systemMinuteReceiverName)){
            // 获取格式化后的系统时间
            val formatDate = SimpleDateFormat.getDateTimeInstance().format(Calendar.getInstance().time)

            // 给文本框赋值
            text?.text = "监听分钟到达广播：$formatDate"

            Log.i("分钟变化：", formatDate)
        }
    }
}
```

2. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 监听分钟到达广播 -->
	<TextView
		android:id="@+id/yuehai_system_minute_activity_text"
		android:text="监听分钟到达广播"
		android:textSize="30dp"
		android:textColor="#F44336"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>

</LinearLayout>
```

3. 创建布局文件对应的代码文件，
	1. 重写广播接收器的注册代码，注意要让接收器过滤分钟到达广播 `Intent.ACTION_TIME_TICK`
	2. 重写活动页面的 `onStop` 方法，添加广播接收器的注销代码。

```Kotlin
package com.yuehai.broadcast

import android.content.IntentFilter
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.broadcast.receiver.SystemMinuteReceiver

class SystemMinuteActivity: AppCompatActivity() {

    // 实例化 SystemMinuteReceiver 类；接收 Intent.ACTION_TIME_TICK 广播
    private val systemMinuteReceiver = SystemMinuteReceiver()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.system_minute_activity)

        // 给对象 systemMinuteReceiver 赋值，使其调用方法更改文本框显示
        systemMinuteReceiver.text = findViewById<TextView>(R.id.yuehai_system_minute_activity_text)
    }

    // 注册广播接收器
    override fun onStart() {
        super.onStart()

        // 创建一个意图过滤器，只处理 STANDARD_ACTION 的广播
        val filter = IntentFilter(systemMinuteReceiver.systemMinuteReceiverName)
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(systemMinuteReceiver, filter)
    }

    // 注销广播接收器
    override fun onStop() {
        super.onStop()

        // 注销接收器，注销之后就不再接收广播
        unregisterReceiver(systemMinuteReceiver)
    }
}
```

4. 清单文件中注册

```xml
<!-- 注册 -->
		<activity
			android:name=".SystemMinuteActivity"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
```

### ③、监听网络变更广播


1. 定义一个分钟广播的接收器，并重写接收器的 `onReceive` 方法，补充收到广播之后的处理逻辑。

```Kotlin
package com.yuehai.broadcast.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.net.NetworkInfo
import android.util.Log
import android.widget.TextView


// 定义一个网络变更广播的接收器，继承 BroadcastReceiver，实现 onReceive 方法
class NetworkReceiver: BroadcastReceiver() {

    // 定义常量，广播名，用以接收指定广播名的广播；每分钟变化
    val networkReceiverName:String = "android.net.conn.CONNECTIVITY_CHANGE"

    // 声明一个文本视图对象，等待 activity 传递
    var text: TextView? = null

    // 一旦接收到分钟变更的广播，马上触发接收器的 onReceive 方法
    override fun onReceive(context: Context?, intent: Intent?) {
        // 判断收到的 intent 不为空，且为指定广播名的广播
        if((intent != null) && intent.action.equals(networkReceiverName)){
            // networkInfo 在 android 10 后已被废弃
            val networkInfo: NetworkInfo? = intent.getParcelableExtra("networkInfo")
            // 网络大类为：
            val typeName = networkInfo!!.typeName
            // 网络小类为：
            val subtypeName = networkInfo.subtypeName
            // 网络状态为：
            val state = networkInfo.state

            // 给文本框赋值
            text?.text ="""
            网络大类为：$typeName
            网络小类为：$subtypeName
            网络状态为：$state
            """".trimIndent()

            Log.i("网络大类为：", typeName)
            Log.i("网络小类为：", subtypeName)
            Log.i("网络状态为：", state.toString())
        }
    }
}
```

2. 修改 xml 布局文件

```xml
<!-- 监听网络变更广播 -->
	<TextView
		android:id="@+id/yuehai_system_minute_activity_network_text"
		android:text="监听网络变更广播"
		android:textSize="30dp"
		android:textColor="#F44336"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_gravity="start"/>
```

3. 修改布局文件对应的代码文件，
	1. 重写广播接收器的注册代码，注意要让接收器过滤分钟到达广播 `Intent.ACTION_TIME_TICK`
	2. 重写活动页面的 `onStop` 方法，添加广播接收器的注销代码。

```Kotlin
package com.yuehai.broadcast

import android.content.IntentFilter
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.broadcast.receiver.NetworkReceiver
import com.yuehai.broadcast.receiver.SystemMinuteReceiver

class SystemMinuteActivity: AppCompatActivity() {

    // 监听分钟到达广播；实例化 SystemMinuteReceiver 类；接收 Intent.ACTION_TIME_TICK 广播
    private val systemMinuteReceiver = SystemMinuteReceiver()
    // 监听网络变更广播；实例化 NetworkReceiver 类；接收 android.net.conn.CONNECTIVITY_CHANGE 广播
    private val networkReceiver = NetworkReceiver()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.system_minute_activity)

        // 监听分钟到达广播；给对象 systemMinuteReceiver 赋值，使其调用方法更改文本框显示
        systemMinuteReceiver.text = findViewById<TextView>(R.id.yuehai_system_minute_activity_text)

        // 监听网络变更广播；给对象 systemMinuteReceiver 赋值，使其调用方法更改文本框显示
        networkReceiver.text = findViewById<TextView>(R.id.yuehai_system_minute_activity_network_text)
    }

    // 注册广播接收器
    override fun onStart() {
        super.onStart()

        // 创建一个意图过滤器，只处理分钟到达的广播
        val filter = IntentFilter(systemMinuteReceiver.systemMinuteReceiverName)
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(systemMinuteReceiver, filter)

        // 创建一个意图过滤器，只处理网络变更的广播
        val filter2 = IntentFilter(networkReceiver.networkReceiverName)
        // 注册接收器，注册之后才能正常接收广播
        registerReceiver(networkReceiver, filter2)
    }

    // 注销广播接收器
    override fun onStop() {
        super.onStop()

        // 注销接收器，注销之后就不再接收广播
        unregisterReceiver(systemMinuteReceiver)
        unregisterReceiver(networkReceiver)
    }
}
```

4. 清单文件中注册，上面注册完了

# 九、`Android` 服务组件 `Service`

## 1、介绍

1. 广播组件 Broadcast 是Android 四大组件之四。
2. 可在后台执行长时间运行操作而不提供界面的应用组件。如下载文件、播放音乐
3. Service 有两种方式：
	1. `startService` ：简单地启动，之后不能进行交互
	2. `bindService`：启动并绑定 Service 之后，可以进行交互
4. 它与生命周期有关的方法说明如下：
	1. `onCreate`：创建服务。
	2. `onStart`：开始服务，Android 2.0 以下版本使用，现已废弃。
	3. `onStartCommand`：开始服务，Android 2.0 及以上版本使用。返回的参数有以下四个：
		1. `START_STICKY`：如果 service 进程被 kill 掉，保留 service 的状态为开始状态，但不保留递送的 intent 对象。随后系统会尝试重新创建 service，由于服务状态为开始状态，所以创建服务后一定会调用`onStartCommand(Intent,int,int)` 方法。如果在此期间没有任何启动命令被传递到 service，那么参数 Intent 将为 null。
		2. `START_NOT_STICKY`：“非粘性的”。使用这个返回值时，如果在执行完 `onStartCommand` 后，服务被异常 kill 掉，系统不会自动重启该服务。
		3. `START_REDELIVER_INTENT`：重传 Intent。使用这个返回值时，如果在执行完 onStartCommand 后，服务被异常kill 掉，系统会自动重启该服务，并将 Intent 的值传入。
		4. `START_STICKY_COMPATIBILITY`： `START_STICKY` 的兼容版本，但不保证服务被 kill 后一定能重启。
	4. `onDestroy`：销毁服务。
	5. `onBind`：绑定服务。
	6. `onUnbind`：解除绑定。返回值为 true 表示允许再次绑定，之后再绑定服务时，不会调用onBind方法而是调用onRebind 方法；返回值为 false 表示只能绑定一次，不能再次绑定。
	7. onRebind：重新绑定。只有上次的onUnbind方法返回true时，再次绑定服务才会调用onRebind方法。
5. 下面通过一个音乐播放器实例来介绍这两种方式

## 2、`startService` 不能进行交互

1. 首先创建 `MusicHelper` 用来播放音频

```Kotlin
package com.yuehai.service.utils

import android.content.Context
import android.media.AudioManager
import android.media.MediaPlayer
import android.net.Uri
import android.util.Log
import com.yuehai.service.R
import java.io.IOException


class MusicHelper(private val context: Context) {

    private var mediaPlayer: MediaPlayer? = null
    // 获取音乐文件
    private val musics = intArrayOf(R.raw.li_zhi_chun, R.raw.bu_jian_chang_an)
    // 音乐文件的索引
    private var musicIndex = 0
    //
    private var prepared = false

    // 主构造器
    init {
        // 创建 MediaPlayer 对象
        createMediaPlayer()
    }

    // 创建 MediaPlayer 对象
    private fun createMediaPlayer() {
        mediaPlayer = MediaPlayer()
        mediaPlayer!!.setAudioStreamType(AudioManager.STREAM_MUSIC)
    }

    // 播放
    fun play() {
        // 判断是否正在播放，是则退出方法
        if (mediaPlayer!!.isPlaying) {
            return
        }

        if (prepared) {
            mediaPlayer!!.start()
            Log.d("月海", "播放音频 play")
            return
        }

        // 这里路径要注意：android.resource:// + 包名 + R.raw.XXXX
        mediaPlayer!!.setDataSource(context, Uri.parse("android.resource://" + context.packageName + "/" + musics[musicIndex]))
        mediaPlayer!!.prepareAsync()
        mediaPlayer!!.setOnPreparedListener { mp ->
            mp.start()
            Log.d("月海", "播放音频 play")
            prepared = true
        }

    }

    // 暂停
    fun pause() {
        if (!mediaPlayer!!.isPlaying) {
            return
        }
        mediaPlayer!!.pause()
    }

    // 上一首
    fun prev() {
        musicIndex = musicIndex - 1
        musicIndex = musicIndex % musics.size
        destroy()
        createMediaPlayer()
        play()
    }


    // 下一首
    operator fun next() {
        musicIndex = musicIndex + 1
        musicIndex = musicIndex % musics.size
        destroy()
        createMediaPlayer()
        play()
    }

    // 销毁
    fun destroy() {
        if (mediaPlayer == null) {
            return
        }
        mediaPlayer!!.stop()
        mediaPlayer!!.release()
        mediaPlayer = null
        prepared = false
    }
}
```

2. 创建 `Service` 的实现类 `MusicService`

```Kotlin
package com.yuehai.service.service

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log
import com.yuehai.service.utils.MusicHelper


class MusicService: Service() {

    private var musicHelper: MusicHelper? = null

    /**
     * 首次创建服务时，系统将调用此方法来执行一次性设置程序（在调用 onStartCommand() 或 onBind() 之前）。
     * 如果服务已在运行，则不会调用此方法，该方法只调用一次
     *
     * 在 onCreate 中创建 MusicHelper
     */
    override fun onCreate() {
        super.onCreate()

        musicHelper = MusicHelper(this)
    }

    /**
     * 当另一个组件（如 Activity）通过调用 startService() 请求启动服务时，系统将调用此方法。
     * 一旦执行此方法，服务即会启动并可在后台无限期运行。
     * 如果自己实现此方法，则需要在服务工作完成后，通过调用 stopSelf() 或 stopService() 来停止服务。
     * 在绑定状态下，无需实现此方法。
     *
     * 播放音频
     */
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        musicHelper?.play()
        Log.d("月海", "播放音频 onStartCommand");

        return super.onStartCommand(intent, flags, startId);
    }

    /**
     * 当服务不再使用且将被销毁时，系统将调用此方法。
     * 服务应该实现此方法来清理所有资源，如线程、注册的侦听器、接收器等，这是服务接收的最后一个调用。
     *
     * 在 onDestroy 中销毁 MusicHelper
     */
    override fun onDestroy() {
        super.onDestroy()

        musicHelper?.destroy()
        musicHelper = null
    }

    /**
     * 当另一个组件想通过调用 bindService() 与服务绑定（例如执行 RPC）时，系统将调用此方法。
     * 在此方法的实现中，必须返回 一个 IBinder 接口的实现类，供客户端用来与服务进行通信。
     * 无论是启动状态还是绑定状态，此方法必须重写，但在启动状态的情况下直接返回 null
     */
    override fun onBind(p0: Intent?): IBinder? {
        TODO("Not yet implemented")
    }
}
```

3. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 播放 -->
	<Button
		android:id="@+id/yuehai_start_service_activity_play"
		android:text="播放"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 停止 -->
	<Button
		android:id="@+id/yuehai_start_service_activity_stop"
		android:text="停止"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 暂停 -->
	<Button
		android:id="@+id/yuehai_start_service_activity_pause"
		android:text="暂停"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 上一首 -->
	<Button
		android:id="@+id/yuehai_start_service_activity_prev"
		android:text="上一首"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 下一首 -->
	<Button
		android:id="@+id/yuehai_start_service_activity_next"
		android:text="下一首"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />

</LinearLayout>
```

4. 创建布局文件对应的代码文件

```Kotlin
package com.yuehai.service

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.service.service.MusicService

class StartServiceActivity: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.start_service_activity)

        // 点击按钮，播放
        findViewById<Button>(R.id.yuehai_start_service_activity_play).setOnClickListener {
            Log.i("月海", "点击按钮，播放")

            // 创建 intent 对象
            val intent = Intent(this, MusicService().javaClass)
            // 这里会自动调用 Service 的 onStartCommand 方法
            startService(intent)
        }

        // 点击按钮，停止
        findViewById<Button>(R.id.yuehai_start_service_activity_stop).setOnClickListener {
            Log.i("月海", "点击按钮，停止")

            // 创建 intent 对象
            val intent = Intent(this, MusicService().javaClass)
            // 这里会直接调用 Service 的 onDestroy 方法，销毁 Service
            stopService(intent)
        }
    }
}
```

5. 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<application
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android" >
		
		<!-- 注册 service -->
		<service
			android:name=".service.MusicService"
			android:enabled="true"
			android:exported="true"/>
		
		<!-- 注册 -->
		<activity
			android:name=".StartServiceActivity"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
		
	</application>

</manifest>
```

6. `startService` 只能简单启动和销毁 `Service`，没办法进行交互，也就没办法进行暂停，下一首等功能

## 3、`bindService` 可以进行交互

1.  `MusicHelper` 不用变
2. 编辑 `Service` 的实现类 `MusicService` 
	1. 在其中创建内部类 `MyBinder` 并继承 `Binder()`
	2. <font color="#ff0000">重写 `onBind` 方法</font>

```Kotlin
package com.yuehai.service.service

import android.app.Service
import android.content.Intent
import android.os.Binder
import android.os.IBinder
import android.util.Log
import com.yuehai.service.utils.MusicHelper


class MusicService: Service() {

    private var musicHelper: MusicHelper? = null

    /**
     * 首次创建服务时，系统将调用此方法来执行一次性设置程序（在调用 onStartCommand() 或 onBind() 之前）。
     * 如果服务已在运行，则不会调用此方法，该方法只调用一次
     *
     * 在 onCreate 中创建 MusicHelper
     */
    override fun onCreate() {
        super.onCreate()

        musicHelper = MusicHelper(this)
    }

    /**
     * 当另一个组件（如 Activity）通过调用 startService() 请求启动服务时，系统将调用此方法。
     * 一旦执行此方法，服务即会启动并可在后台无限期运行。
     * 如果自己实现此方法，则需要在服务工作完成后，通过调用 stopSelf() 或 stopService() 来停止服务。
     * 在绑定状态下，无需实现此方法。
     *
     * 播放音频
     */
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        return super.onStartCommand(intent, flags, startId);
    }

    /**
     * 当服务不再使用且将被销毁时，系统将调用此方法。
     * 服务应该实现此方法来清理所有资源，如线程、注册的侦听器、接收器等，这是服务接收的最后一个调用。
     *
     * 在 onDestroy 中销毁 MusicHelper
     */
    override fun onDestroy() {
        super.onDestroy()

        // 销毁 service 的同时销毁 musicHelper
        musicHelper?.destroy()
    }

    /**
     * 新建内部类 MyBinder，继承自 Binder(Binder实现IBinder接口)
     * 在内部创建所需方法，以供外部调用
     * 需传入 MusicService 的实例，即本内部类的外部类
     */
    class MyBinder(private val musicService: MusicService): Binder() {

        // 播放
        fun play(){
            musicService.musicHelper?.play()
        }

        // 销毁
        fun destroy(){
            musicService.musicHelper?.destroy()
        }

        // 暂停
        fun pause(){
            musicService.musicHelper?.pause()
        }

        // 上一首
        fun prev(){
            musicService.musicHelper?.prev()
        }

        // 下一首
        fun next(){
            musicService.musicHelper?.next()
        }

    }

    /**
     * 当另一个组件想通过调用 bindService() 与服务绑定（例如执行 RPC）时，系统将调用此方法。
     * 在此方法的实现中，必须返回 一个 IBinder 接口的实现类，供客户端用来与服务进行通信。
     * 无论是启动状态还是绑定状态，此方法必须重写，但在启动状态的情况下直接返回 null
     *
     * bindService 需重写此方法，返回内部类 MyBinder 的实例
     */
    override fun onBind(p0: Intent?): IBinder? {
        return MyBinder(this)
    }
}
```

3. 创建 `MyConn` 类实现 `ServiceConnection` 接口，重写 `onServiceConnected` 方法，使其返回上面  `Service` 的实现类 `MusicService` 的内部类 `MyBinder`

```Kotlin
package com.yuehai.service.service

import android.content.ComponentName
import android.content.ServiceConnection
import android.os.IBinder

class MyConn: ServiceConnection {

    // 创建变量，保存 MusicService 的内部类 MyBinder 的实例
    var myBinder : MusicService.MyBinder? = null

    /**
     * 外部调用 bindService 方法时，会自动调用此方法

     */
    override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
        // 将传入的 IBinder 对象强转为 MusicService 的内部类 MyBinder 的类型，并赋值
        myBinder  = service as MusicService.MyBinder?
    }

    override fun onServiceDisconnected(name: ComponentName?) {

    }
}
```

4.  xml 布局文件和清单文件中注册不变
5. 修改布局文件对应的代码文件
	1. 调用 `bindService` 之后，客户端端连上 `Service`
	2. 触发 `MyConn` 类的 `onServiceConnected` 方法，获取 `Binder` 对象
	3. 之后可以 `Binder` 对象和 `Service` 交互（播放、暂停、下一首）

```Kotlin
package com.yuehai.service

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.yuehai.service.service.MusicService
import com.yuehai.service.service.MyConn

class StartServiceActivity: AppCompatActivity() {

    // 创建变量，保存 MyConn 的实例
    private var myConn:MyConn? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.start_service_activity)

        // 调用初始化服务
        initService();

        // 点击按钮，播放
        findViewById<Button>(R.id.yuehai_start_service_activity_play).setOnClickListener {
            Log.i("月海", "点击按钮，播放")

            myConn?.myBinder?.play()
        }

        // 点击按钮，停止
        findViewById<Button>(R.id.yuehai_start_service_activity_stop).setOnClickListener {
            Log.i("月海", "点击按钮，停止")

            myConn?.myBinder?.destroy()
        }

        // 点击按钮，暂停
        findViewById<Button>(R.id.yuehai_start_service_activity_pause).setOnClickListener {
            Log.i("月海", "点击按钮，暂停")
            myConn?.myBinder?.pause()
        }

        // 点击按钮，上一首
        findViewById<Button>(R.id.yuehai_start_service_activity_prev).setOnClickListener {
            Log.i("月海", "点击按钮，上一首")
            myConn?.myBinder?.prev()
        }

        // 点击按钮，下一首
        findViewById<Button>(R.id.yuehai_start_service_activity_next).setOnClickListener {
            Log.i("月海", "点击按钮，下一首")
            myConn?.myBinder?.next()
        }
    }

    // 初始化服务
    private fun initService(){
        // 开启服务
        val intent = Intent(this, MusicService().javaClass)
        // 这里会自动调用 Service 的 onStartCommand 方法
        startService(intent);

        // 绑定服务
        if(myConn == null){
            myConn = MyConn();
            // 这里会自动调用 MyConn 的 onServiceConnected 方法
            bindService(intent, myConn!!, 0);
        }
    }
}
```

# 十、`Android` 网络通信

## 1、`Handler` 消息机制

1. `Handler` 是一种异步回调机制，主要负责与子线程进行通信。
2. HTTP 请求需要一定时间才能完成，所以不能在主线程中执行； 一般采用创建一个新线程的方式来执行 HTTP，然后再将返回结果发送给主线程。
3. Android 提供了 Handler 来实现这一过程。
4. Handler 机制主要包括四个关键对象：
	1. `Message`：消息。
	2. `Handler`：处理者，主要负责 Message 的发送以及处理。
	3. `MessageQueue`：消息队列，主要用来存放 Handler 发送过来的消息。
	4. `Looper`：消息循环，不断的从 MessageQueue 中抽取 Message 并执行。

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230421192055.png)

5. 创建获取天气的线程 `WeatherThread`，继承 `: Thread` 类

```Kotlin
package com.example.http.thread

import android.os.Handler
import android.os.Message
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.URL
import javax.net.ssl.HttpsURLConnection

/**
@author 月海
@create 2023/4/21 19:40

获取天气的线程 WeatherThread
 */
class WeatherThread(private var handler: Handler): Thread() {

    // 天气接口
    private val path = "https://restapi.amap.com/v3/weather/weatherInfo?city=440300&key=f15437fa96e40903e41bcb0c0adc8d38";

    // 重写线程的 run 方法，调用 getWeather 方法
    override fun run() {
        // 调用 getWeather 方法获取天气信息
        val weather = getWeather()

        // Message 发送消息
        val message = Message()
        message.what = 0
        message.obj = weather

        // 调用 Handler 处理者，主要负责 Message 的发送以及处理。
        handler.sendMessage(message)
    }

    // 获取天气信息
    private fun getWeather(): String{

        // 获取 url 连接
        val connection = URL(path).openConnection() as HttpsURLConnection
        // 设置请求方式
        connection.requestMethod = "GET"
        // 设置超时时间
        connection.connectTimeout = 5000

        // 创建链接进行请求
        val reader = BufferedReader(InputStreamReader(connection.inputStream))
        // 得到请求结果并返回
        return reader.readLine()
    }

}
```

6. 异步消息接收者 `WeatherHandler`，继承 `: Handler` 类

```Kotlin
package com.example.http.handler

import android.os.Handler
import android.os.Message
import android.widget.TextView
import com.example.http.R
import com.example.http.YuehaiHandler

/**
@author 月海
@create 2023/4/21 20:20
 */
class WeatherHandler(private val yuehaiHandler: YuehaiHandler): Handler() {
    // 重写 handleMessage 方法
    override fun handleMessage(msg: Message) {
        super.handleMessage(msg)

        // 接受到消息则把天气结果设置到文本框
        if(msg.what == 0){
            yuehaiHandler.findViewById<TextView>(R.id.yuehai_bandler_text).text = msg.obj.toString()
        }
    }
}
```

7. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- 获取天气信息 -->
	<Button
		android:id="@+id/yuehai_bandler_btn"
		android:text="获取天气信息"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 显示文本框 -->
	<TextView
		android:id="@+id/yuehai_bandler_text"
		android:text="显示天气信息"
		android:textSize="25dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

8. 创建布局文件对应的代码文件

```Kotlin
package com.example.http

import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.http.handler.WeatherHandler
import com.example.http.thread.WeatherThread

/**
@author 月海
@create 2023/4/21 19:34
 */
class YuehaiHandler: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.yuehai_handler)

        // 点击按钮，开启新线程，发送 http 异步请求
        findViewById<Button>(R.id.yuehai_bandler_btn).setOnClickListener {
            // 实例化自定义的 WeatherHandler Handler 线程实现类
            val handler = WeatherHandler(this)
            // 实例化自定义的 WeatherThread Thread 线程实现类，调用 start() 方法，启动新线程
            WeatherThread(handler).start()
        }
    }
}
```

9. 清单文件中注册，需要申请网络联网权限：`<uses-permission android:name="android.permission.INTERNET" />`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 网络（联网）权限 -->
	<uses-permission android:name="android.permission.INTERNET" />
	
	<application
		android:allowBackup="true"
		android:label="@string/app_name"
		android:icon="@mipmap/ic_launcher"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">
		
		<!-- 注册 -->
		<activity
			android:name=".YuehaiHandler"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

## 2、`okhttp`

1. 上面用的 Java 中的 `HttpURLConnection` 是比较底层的接口，编写代码工作量大，容易出错。 
2. `okhttp` 是 android 平台使用最广泛的第三方网络框架，`okhttp` 做了很多网络优化，功能也很强大。
3. `okhttp` 有同步、异步两种接口
	1. 同步接口：阻塞方式
	2. 异步接口：自动创建线程进行网络请求
4. 引入依赖：`implementation 'com.squareup.okhttp3:okhttp:3.14.+'`

### ①、同步方式

1. 创建获取天气的线程 `WeatherThreadOkHttpSynchronous`，继承 `: Thread` 类

```Kotlin
package com.example.http.thread

import android.os.Handler
import android.os.Message
import okhttp3.OkHttpClient
import okhttp3.Request
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.URL
import javax.net.ssl.HttpsURLConnection

/**
@author 月海
@create 2023/4/21 19:40

获取天气的线程 WeatherThread
 */
class WeatherThreadOkHttpSynchronous(private var handler: Handler): Thread() {

    // 天气接口
    private val path = "https://restapi.amap.com/v3/weather/weatherInfo?city=440300&key=f15437fa96e40903e41bcb0c0adc8d38";

    // 重写线程的 run 方法，调用 getWeather 方法
    override fun run() {
        // 调用 getWeather 方法获取天气信息
        val weather = getWeather()

        // Message 发送消息
        val message = Message()
        message.what = 0
        message.obj = weather

        // 调用 Handler 处理者，主要负责 Message 的发送以及处理。
        handler.sendMessage(message)
    }

    // 获取天气信息
    private fun getWeather(): String{

        // 创建 OkHttpClient
        val okHttpClient = OkHttpClient()
        // 构建请求
        val request = Request.Builder().url(path).build()
        // 同步的方式发送请求
        val execute = okHttpClient.newCall(request).execute()

        // 返回响应体
        return execute.body()!!.string()
    }

}
```

2. 异步消息接收者 `WeatherHandlerOkHttpSynchronous`，继承 `: Handler` 类

```Kotlin
package com.example.http.handler

import android.os.Handler
import android.os.Message
import android.widget.TextView
import com.example.http.R
import com.example.http.YuehaiHandler
import com.example.http.YuehaiOkHttp

/**
@author 月海
@create 2023/4/21 20:20
 */
class WeatherHandlerOkHttpSynchronous(private val yuehaiOkHttp: YuehaiOkHttp): Handler() {
    // 重写 handleMessage 方法
    override fun handleMessage(msg: Message) {
        super.handleMessage(msg)

        // 接受到消息则把天气结果设置到文本框
        if(msg.what == 0){
            yuehaiOkHttp.findViewById<TextView>(R.id.yuehai_bandler_text).text = msg.obj.toString()
        }
    }
}
```

3. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- okhttp 同步方式 -->
	<Button
		android:id="@+id/yuehai_bandler_synchronous"
		android:text="okhttp 同步方式"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- okhttp 异步方式 -->
	<Button
		android:id="@+id/yuehai_bandler_asynchronous"
		android:text="okhttp 异步方式"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 显示文本框 -->
	<TextView
		android:id="@+id/yuehai_bandler_text"
		android:text="显示天气信息"
		android:textSize="25dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

4. 创建布局文件对应的代码文件

```Kotlin
package com.example.http

import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.http.handler.WeatherHandler
import com.example.http.handler.WeatherHandlerOkHttpSynchronous
import com.example.http.thread.WeatherThread
import com.example.http.thread.WeatherThreadOkHttpSynchronous

/**
@author 月海
@create 2023/4/21 19:34
 */
class YuehaiOkHttp: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.yuehai_okhttp)

        // okhttp 同步方式
        findViewById<Button>(R.id.yuehai_bandler_synchronous).setOnClickListener {
            // 实例化自定义的 WeatherHandlerOkHttpSynchronous Handler 线程实现类
            val handler = WeatherHandlerOkHttpSynchronous(this)
            // 实例化自定义的 WeatherThreadOkHttpSynchronous Thread 线程实现类，调用 start() 方法，启动新线程
            WeatherThreadOkHttpSynchronous(handler).start()
        }
        
    }
}
```

5. 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 网络（联网）权限 -->
	<uses-permission android:name="android.permission.INTERNET" />
	
	<application
		android:allowBackup="true"
		android:label="@string/app_name"
		android:icon="@mipmap/ic_launcher"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">
		
		<!-- 注册 -->
		<activity
			android:name=".YuehaiHandler"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册 -->
		<activity
			android:name=".YuehaiOkHttp"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

### ②、异步方式


1. 异步消息接收者 `WeatherHandlerOkHttpSynchronous`，继承 `: Handler` 类

```Kotlin
package com.example.http.handler

import android.os.Handler
import android.os.Message
import android.widget.TextView
import com.example.http.R
import com.example.http.YuehaiOkHttp

/**
@author 月海
@create 2023/4/21 20:20
 */
class WeatherHandlerOkHttpSynchronous(private val yuehaiOkHttp: YuehaiOkHttp): Handler() {
    // 重写 handleMessage 方法
    override fun handleMessage(msg: Message) {
        super.handleMessage(msg)

        // 接受到消息则把天气结果设置到文本框
        if(msg.what == 0){
            yuehaiOkHttp.findViewById<TextView>(R.id.yuehai_bandler_text).text = msg.obj.toString()
        }
    }
}
```

3. 创建 xml 布局文件（和上面一样没改）

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- okhttp 同步方式 -->
	<Button
		android:id="@+id/yuehai_bandler_synchronous"
		android:text="okhttp 同步方式"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- okhttp 异步方式 -->
	<Button
		android:id="@+id/yuehai_bandler_asynchronous"
		android:text="okhttp 异步方式"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 显示文本框 -->
	<TextView
		android:id="@+id/yuehai_bandler_text"
		android:text="显示天气信息"
		android:textSize="25dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

4. 创建布局文件对应的代码文件，异步方式就不需要人为开启子线程了

```Kotlin
package com.example.http

import android.os.Bundle
import android.os.Message
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.http.handler.WeatherHandler
import com.example.http.handler.WeatherHandlerOkHttpSynchronous
import com.example.http.thread.WeatherThread
import com.example.http.thread.WeatherThreadOkHttpSynchronous
import okhttp3.*
import java.io.IOException

/**
@author 月海
@create 2023/4/21 19:34
 */
class YuehaiOkHttp: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.yuehai_okhttp)

        // okhttp 同步方式
        findViewById<Button>(R.id.yuehai_bandler_synchronous).setOnClickListener {
            // 实例化自定义的 WeatherHandlerOkHttpSynchronous Handler 线程实现类
            val handler = WeatherHandlerOkHttpSynchronous(this)
            // 实例化自定义的 WeatherThread Thread 线程实现类，调用 start() 方法，启动新线程
            WeatherThreadOkHttpSynchronous(handler).start()
        }

        // okhttp 异步方式
        findViewById<Button>(R.id.yuehai_bandler_asynchronous).setOnClickListener {
            // 天气接口
            val path = "https://restapi.amap.com/v3/weather/weatherInfo?city=440300&key=f15437fa96e40903e41bcb0c0adc8d38";

            // 实例化自定义的 WeatherHandlerOkHttpSynchronous Handler 线程实现类
            val handler = WeatherHandlerOkHttpSynchronous(this)

            // 创建 OkHttpClient
            val okHttpClient = OkHttpClient()
            // 构建请求
            val request = Request.Builder().url(path).build()

            // 同步的方式发送请求；实现 Callback 接口中的两个方法 onFailure、onResponse
            okHttpClient.newCall(request).enqueue(object : Callback {
                // 请求失败，打印异常
                override fun onFailure(call: Call, e: IOException) {
                    println("Failed request api :( " + e.message)
                }

                // 响应
                override fun onResponse(call: Call, response: Response) {
                    val result = response.body()!!.string()

                    // 回调函数运行在子线程，不能直接操控 UI，通过 handler 把天气信息发送到主线程显示
                    val message = Message()
                    message.what = 0
                    message.obj = result

                    // 调用 Handler 处理者，主要负责 Message 的发送以及处理。
                    handler.sendMessage(message)
                }

            })

        }
    }
}
```

5. 清单文件中注册（和上面一样没改）
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 网络（联网）权限 -->
	<uses-permission android:name="android.permission.INTERNET" />
	
	<application
		android:allowBackup="true"
		android:label="@string/app_name"
		android:icon="@mipmap/ic_launcher"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">
		
		<!-- 注册 -->
		<activity
			android:name=".YuehaiHandler"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册 -->
		<activity
			android:name=".YuehaiOkHttp"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```


## 3、`retrofit`

1. 在 Android 开发中，`Retrofit` 是当下最热的一个网络请求库。
2. 底层默认使用 `okhttp` 封装的，准确来说，网络请求的工作本质上是 `okhttp` 完成，而 `Retrofit` 仅负责网络请求接口的封装。
3. 其作用主要是简化代码、提高可维护性。
4. 另外，最重要的是：`okhttp` 异步请求的回调运行在子线程，而 `retrofit` 的异步请求的回调默认运行在主线程。
5. 使用 `retrofit` 时，不再需要使用 `handler` 机制手工进行线程间通信。
6. 仍然使用天气的例子来介绍基本使用：
7. 引入依赖：

```xml
    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
    implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
```

8. 创建一个接口，指定 url（不包含域名和参数），GET 请求的参数通过 `@Query` 指定

```Kotlin
package com.example.http.retrofit

import com.google.gson.JsonObject
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Query

/**
@author 月海
@create 2023/4/23 13:45
 */

// 创建一个接口
interface WeatherService {

    // https://restapi.amap.com/v3/weather/weatherInfo?city=440300&key=f15437fa96e40903e41bcb0c0adc8d38
    /**
     * 指定 url（不包含域名和参数），GET 请求的参数通过 @Query 指定
     * @Path 和 @Query 都是 Retrofit 中的注解，用于指定请求参数的值。它们之间的区别在于：
     *      @Path 注解用于指定 URL 中的占位符
     *      @Query 注解用于指定查询参数的值
     */
    @GET("v3/weather/weatherInfo")
    // 这里返回值偷懒没有定义实体类，而是使用 JsonObject 代替
    fun fetchWeatherResult(@Query("city") city:String, @Query("key") key:String): Call<JsonObject?>

}
```

9. 创建 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="match_parent"
	android:layout_height="match_parent"
	android:orientation="vertical">
	
	<!-- retrofit -->
	<Button
		android:id="@+id/yuehai_bandler_retrofit"
		android:text="retrofit 获取天气信息"
		android:textSize="30dp"
		android:layout_width="match_parent"
		android:layout_height="wrap_content" />
	
	<!-- 显示文本框 -->
	<TextView
		android:id="@+id/yuehai_bandler_text"
		android:text="显示天气信息"
		android:textSize="25dp"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content" />

</LinearLayout>
```

10. 创建布局文件对应的代码文件

```Kotlin
package com.example.http

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.http.retrofit.WeatherService
import com.google.gson.JsonObject
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

/**
@author 月海
@create 2023/4/23 13:36
 */
class YuehaiRetrofit: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
        setContentView(R.layout.yuehai_retrofit)

        // 点击按钮，retrofit 请求获取天气信息
        findViewById<Button>(R.id.yuehai_bandler_retrofit).setOnClickListener {
            // 创建一个 Retrofit 实例
            val retrofit = Retrofit.Builder()
                .baseUrl("https://restapi.amap.com")
                .addConverterFactory(GsonConverterFactory.create())
                .build()

            // 使用 retrofit API 调用自定义的接口 WeatherService
            val service = retrofit.create(WeatherService::class.java)
            // 调用自定义 WeatherService 的方法，传入参数
            service.fetchWeatherResult("440300", "f15437fa96e40903e41bcb0c0adc8d38").enqueue(object: Callback<JsonObject?> {
                // 请求失败，打印异常
                override fun onFailure(call: Call<JsonObject?>, t: Throwable) {
                    t.printStackTrace()
                }

                // 响应
                override fun onResponse(call: Call<JsonObject?>, response: Response<JsonObject?>) {
                    // 获取天气结果
                    val body = response.body()

                    // 直接设置到 textView,不再需要使用 handler 手动进行线程间通信
                    findViewById<TextView>(R.id.yuehai_bandler_text).text = body.toString()
                }

            })
        }
    }
}
```

11. 清单文件中注册

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!-- 网络（联网）权限 -->
	<uses-permission android:name="android.permission.INTERNET" />
	
	<application
		android:allowBackup="true"
		android:label="@string/app_name"
		android:icon="@mipmap/ic_launcher"
		android:roundIcon="@mipmap/ic_launcher_round"
		android:supportsRtl="true"
		android:theme="@style/Theme.02_Android">
		
		<!-- 注册 Handler -->
		<activity
			android:name=".YuehaiHandler"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册 OkHttp -->
		<activity
			android:name=".YuehaiOkHttp"
			android:exported="true"
			android:label="@string/app_name">
		</activity>
		
		<!-- 注册 Retrofit -->
		<activity
			android:name=".YuehaiRetrofit"
			android:exported="true"
			android:label="@string/app_name">
			<intent-filter>
				<!-- 配置为主窗口， -->
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		
	</application>

</manifest>
```

# 十一、补充

## 1、架构

### ①、使用 MVVM 架构进行应用开发

#### Ⅰ、MVVM（Model-View-ViewModel）简介

1. MVVM 是一种基于数据绑定的架构模式，用于设计和组织应用程序的代码结构。它将应用程序分为三个主要部分：Model（模型）、View（视图）和ViewModel（视图模型）。
2. Model（模型）：负责处理数据和业务逻辑。它可以是从网络获取的数据、数据库中的数据或其他数据源。Model 层通常是独立于界面的，可以在多个界面之间共享。
3. View（视图）：负责展示数据和与用户进行交互。它可以是 Activity、Fragment、View 等。View 层主要负责 UI 的展示和用户输入的响应。
4. ViewModel（视图模型）：连接 View 和 Model，作为 View 和 Model 之间的桥梁。它负责从 Model 中获取数据，并将数据转换为 View 层可以直接使用的形式。ViewModel 还负责监听 Model 的数据变化，并通知 View 进行更新。ViewModel 通常是与View一一对应的，每个 View 都有一个对应的 ViewModel。

#### Ⅱ、MVVM 的特点和优势

1. 解耦合：MVVM 通过将 View 和 Model 解耦合，使得它们可以独立开发和测试。ViewModel 作为中间层，将数据从 Model 传递给 View，避免了直接在 View 中处理业务逻辑的情况。
2. 可维护性：MVVM 的分层结构使得代码更易于维护。View 只负责展示数据和用户交互，ViewModel 负责处理业务逻辑和数据转换，Model 负责数据的获取和存储。这种分离使得代码更加清晰和可读，也方便进行单元测试。
3. 数据驱动 UI：MVVM 采用数据绑定的方式，将 Model 的数据与 View 进行绑定。当 Model 的数据发生变化时，ViewModel 会自动更新 View 的显示，无需手动更新 UI。这种方式可以减少手动更新 UI 的代码量，提高开发效率。
4. 可测试性：由于 MVVM 的分层结构和数据驱动UI的特点，可以更容易地进行单元测试。ViewModel 中的业务逻辑可以独立于 View 进行测试，而不需要依赖于 Android 系统或 UI 组件。

#### Ⅲ、常见架构模式（MVC和MVP）区别

1. MVC（Model-View-Controller）：MVC 模式中，Controller 负责处理用户输入和业务逻辑，Model 负责数据和业务逻辑，View 负责展示数据。与 MVC 相比，MVVM 将 Controller 分离为 ViewModel，将数据绑定的方式集成进来，使得代码更加简洁和清晰。
2. MVP（Model-View-Presenter）：MVP 模式中，Presenter 负责处理用户输入和业务逻辑，Model 负责数据和业务逻辑，View 负责展示数据。与 MVP 相比，MVVM 将 Presenter 分离为 ViewModel

#### Ⅳ、MVVM 三个核心组件

1. 在 MVVM 模式中，有三个核心组件：Model（模型）、View（视图）和 ViewModel（视图模型）。
2. 它们各自具有不同的职责和作用，并通过数据绑定机制实现彼此之间的关系和交互。

##### （1）、Model（模型）

1. 职责：负责处理数据和业务逻辑。它可以是从网络获取的数据、数据库中的数据或其他数据源。Model层通常是独立于界面的，可以在多个界面之间共享
2. 作用：提供数据和处理数据的方法，封装业务逻辑。

##### （2）、View（视图）

1. 职责：负责展示数据和与用户进行交互。它可以是 Activity、Fragment、View 等。View 层主要负责 UI 的展示和用户输入的响应。 
2. 作用：将 ViewModel 中的数据展示给用户，并将用户的输入传递给 ViewModel。

##### （3）、ViewModel（视图模型）

1. 职责：连接 View 和 Model，作为 View 和 Model 之间的桥梁。它负责从 Model 中获取数据，并将数据转换为 View 层可以直接使用的形式。ViewModel 还负责监听 Model 的数据变化，并通知 View 进行更新。ViewModel 通常是与 View 一一对应的，每个 View 都有一个对应的 iewModel。 
2. 作用：处理 View 层的数据展示和用户交互，并与 Model 层进行交互。
3. ViewModel 通过数据绑定机制将 Model 的数据与 View 进行绑定，实现数据的自动更新。当 Model 的数据发生变化时，ViewModel 会自动通知 View 进行更新。这种数据绑定的方式减少了手动更新 UI 的代码量，提高了开发效率。
4. 下面是一个示意图，说明了 MVVM 模式中 Model、View 和 iewModel 之间的关系和交互方式：

```dart
        +-------------+
        |    Model    |
        +-------------+
              |
              |
              v        
	    +-------------+
        |  ViewModel  |
        +-------------+
              |
              |
              v
        +-------------+
        |     View    |
        +-------------+
```

5. 在这个示意图中，ViewModel 通过数据绑定机制将 Model 的数据绑定到 View上，当 Model 的数据发生变化时，ViewModel 会自动通知 View 进行更新，从而实现 UI 的自动刷新。用户的输入通过 View 传递给 ViewModel，ViewModel 再将数据传递给 Model 进行处理。
6. 通过 MVVM 模式，Model、View 和 ViewModel 之间的分离和解耦合，使得代码更易于维护和测试。
7. ViewModel 作为中间层，负责处理业务逻辑和数据转换，使得 View 层只关注 UI 的展示和用户交互，而不关心具体的业务逻辑和数据处理。这种分层结构和数据绑定的方式使得代码更加清晰、可读性更强，并提高了开发效率和代码质量。

#### Ⅴ、MVVM 数据绑定机制

1. 在 MVVM 模式中，数据绑定是实现 View 和 ViewModel 之间数据同步的关键机制。它允许将 View 中的 UI 元素（如 TextView、EditText）与 ViewModel 中的数据属性进行绑定，当数据发生变化时，自动更新 UI，同时用户的输入也会自动同步到 ViewModel 中。
2. 数据绑定的原理是通过观察者模式和反射机制实现的。当 ViewModel 中的数据发生变化时，会触发相应的通知，通知绑定的 View 进行更新。而当用户在 View 中输入数据时，数据绑定也会将输入的数据自动同步到 ViewModel 中。这种双向的数据同步机制，使得 View 和 ViewModel 之间实现了数据的实时同步。
3. 在 Android 中，可以使用数据绑定库（如Data Binding）来实现 MVVM 模式中的数据绑定。Data Binding 库提供了一组注解和工具类，可以简化数据绑定的实现过程。
4. 以下是在 Android 中使用 Data Binding 库实现 MVVM 模式中的数据绑定的步骤：
---
1. 配置 Data Binding 库：在项目的 `build.gradle` 文件中，添加 Data Binding 的插件和依赖项。

```gradle
    // ...
    dataBinding {
        enabled = true
    }
}
​
dependencies {
    // ...
    implementation 'androidx.databinding:databinding-runtime:7.0.2'
}
```

2. 创建布局文件：在布局文件中，使用标签包裹布局，并使用标签定义绑定的变量和表达式。

```xml
    <data>
        <variable name="user" type="com.example.mvvm.User" />
    </data>
    <LinearLayout android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{user.name}" />
        <TextView            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{String.valueOf(user.age)}" />
    </LinearLayout>
</layout>
```

3. 创建 ViewModel 类：创建一个与 View 对应的 ViewModel 类，并在其中定义与布局文件中绑定的变量。

```java
public class UserViewModel extends BaseObservable {
    private String name;
    private int age;
​
    // getter and setter methods
​
    @Bindable    
    public String getName() {
        return name;
    }
​
    public void setName(String name) {
        this.name = name;
        notifyPropertyChanged(BR.name);
    }
​
    @Bindable    
    public int getAge() {
        return age;
    }
​
    public void setAge(int age) {
        this.age = age;
        notifyPropertyChanged(BR.age);
    }
}
```

4. 绑定数据：在 Activity 或 Fragment 中，使用 DataBindingUtil 类将布局文件与 ViewModel 进行绑定，并设置 ViewModel 的数据

```dart
public class MainActivity extends AppCompatActivity {
    private UserViewModel userViewModel;
​
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
​
        // 创建ViewModel实例
        userViewModel = new UserViewModel();
        userViewModel.setName("John");
        userViewModel.setAge(25);
​
        // 绑定ViewModel和布局文件
	ActivityMainBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
    binding.setUser(userViewModel);
  }
}
```

5. 通过以上步骤，我们将布局文件和 ViewModel 进行了绑定，同时设置了 ViewModel 的数据。当 ViewModel 中的数据发生变化时，布局文件中相应的 UI 元素会自动更新。同时，当用户在 UI 元素中输入数据时，Data Binding 库也会自动将输入的数据同步到 ViewModel 中。
6. 使用数据绑定的好处是能够简化代码，减少手动更新UI的代码量，提高开发效率。它还能够降低代码的耦合性，使得 UI 和数据逻辑的修改更加灵活和独立。另外，数据绑定还能够提高代码的可读性和可维护性，使得代码更易于理解和调试。

#### Ⅵ、MVVM 架构模式发展趋势

1. MVVM 模式在 Android 开发中已经得到广泛应用，并且在未来仍然有着较大的发展潜力。以下是一些未来发展趋势：
2. Jetpack Compose：Jetpack Compose 是 Google 推出的一种全新的 UI 框架，它采用了声明式 UI 的方式，与 MVVM 模式非常契合。Jetpack Compose 能够简化 UI 开发流程，提供更加灵活和响应式的 UI 编程方式。
3. 数据驱动 UI：未来，数据驱动 UI 的概念将会更加普及和强调。MVVM 模式的数据绑定和观察者模式是实现数据驱动 UI 的重要手段，未来可能会有更多的框架和工具出现，进一步简化数据和 UI 的绑定过程。
4. 更强大的 ViewModel 组件：Android Jetpack 中的 ViewModel 组件已经为开发者提供了很多便利，但未来可能会有更多功能和特性被添加进来，以进一步提高ViewModel的灵活性和可扩展性。
5. 跨平台开发：MVVM 模式的解耦特性使得代码更具可移植性，未来可能会有更多的跨平台开发框架和工具出现，使得开发者能够更轻松地在不同平台上使用 MVVM 模式进行开发。

### ②、Navigation 导航框架的使用

> Navigation 是一套完整的导航框架，内置支持普通 Fragment、Activity 和 DialogFragment 组件的跳转，也就是所有 Dialog 或 PopupWindow 都建议使用 DialogFragment 实现，这样可以涵盖所有常用的跳转场景，统一返回栈的管理。另外，基于 Fragment 实现可以做到状态存储和恢复

#### Ⅰ、使用

1. 引入依赖：目前最新的稳定版本为 2.4.0，其他历史版本可查看 [Android Navigation Releate Note](https://developer.android.com/jetpack/androidx/releases/navigation)

```kotlin
// Android Navigation是一个用于管理应用程序导航的组件，它可以帮助你轻松地实现应用程序中的导航逻辑。
implementation "androidx.navigation:navigation-fragment-ktx:2.4.0"
implementation "androidx.navigation:navigation-ui-ktx:2.4.0"
```

2. 创建导航图：在 `res` 目录下新建 `navigation` 目录，然后右键 `navigation` 目录，点击新建，选择 `navigation` 资源文件，名称随意，一般为 `nav_graph.xml`

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230922101151.png)

3. 创建主 `Activity` 的布局文件 `main_activity.xml` 与代码文件 `MainActivity`，这是本项目唯一一个 `Activity`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
		xmlns:app="http://schemas.android.com/apk/res-auto"
		android:layout_width="match_parent"
		android:layout_height="match_parent" >

	<!--
		 defaultNavHost：true 表示此导航图将优先代理 系统返回键，
			用户通过手势或虚拟返回键返回时会优先弹出 Fragment 返回栈；
			若设置为 false，将会直接退出 Activity。
		navGraph：指定导航图
	 -->
	<androidx.fragment.app.FragmentContainerView
			android:id="@+id/nav_host_container"
			android:layout_width="match_parent"
			android:layout_height="match_parent"
			android:name="androidx.navigation.fragment.NavHostFragment"
			app:defaultNavHost="true"
			app:navGraph="@navigation/nav_graph"/>
	
</LinearLayout>
```

```kotlin
package com.yuehai.y_chat

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity: AppCompatActivity() {
	
	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.main_activity)
		
	}
}
```

4. 创建首页 `home` 的布局文件 `fragment_home.xml` 与代码文件 `HomeFragment`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
			  android:layout_width="match_parent"
			  android:layout_height="match_parent">

	<TextView
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:text="home"
			android:textSize="50sp"/>
	
	<Button
			android:id="@+id/button_home_to_settings"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:text="去设置"
			android:textSize="50sp" />
	
</LinearLayout>
```

```kotlin
package com.yuehai.y_chat.ui.home

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 8:59
 * 首页
 */
class HomeFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_home, container, false)

		return view
	}
	
}
```

5. 创建设置 `settings` 的布局文件 `fragment_settings.xml` 与代码文件 `SettingsFragment`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
			  android:layout_width="match_parent"
			  android:layout_height="match_parent">
	
	<TextView
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:text="settings"
			android:textSize="50sp"/>
	
	<Button
			android:id="@+id/button_settings_to_home"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:text="去首页"
			android:textSize="50sp" />

</LinearLayout>
```

```kotlin
package com.yuehai.y_chat.ui.settings

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 9:13
 */
class settingsFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_settings, container, false)

		return view
	}
	
}
```

6. 在导航图 `nav_graph.xml` 中
	1. 使用 `fragment` 标签引入 fragment
	2. 在根标签 `navigation` 中使用 `app:startDestination` 属性指定默认显示的 `fragment id`
	3. 在 `fragment` 标签中使用 `action` 标签，在其中使用 `destination` 属性指定要跳转到的 `fragment id`，可指定多个

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 导航图 -->
<!--
 startDestination：指定默认显示的 fragment id
 -->
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
			xmlns:app="http://schemas.android.com/apk/res-auto"
			xmlns:tools="http://schemas.android.com/tools"
			android:id="@+id/nav_graph"
			app:startDestination="@id/fragment_home">
	
	<!-- 首页 -->
	<fragment
			android:id="@+id/fragment_home"
			android:name="com.yuehai.y_chat.ui.home.HomeFragment"
			android:label="home"
			tools:layout="@layout/fragment_home">
		
		<!-- 首页 -> 设置 -->
		<action
				android:id="@+id/action_home_to_settings"
				app:destination="@id/fragment_settings"/>
	</fragment>
	
	<!-- 设置 -->
	<fragment
			android:id="@+id/fragment_settings"
			android:name="com.yuehai.y_chat.ui.settings.SettingsFragment"
			android:label="settings"
			tools:layout="@layout/fragment_settings">
		
		<!-- 设置 -> 首页 -->
		<action
				android:id="@+id/action_settings_to_home"
				app:destination="@id/fragment_home"/>
	</fragment>


</navigation>
```

7. 在 home Fragment 的代码文件 `HomeFragment` 中编写代码，点击按钮跳转至设置

```kotlin
package com.yuehai.y_chat.ui.home

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 8:59
 * 首页
 */
class HomeFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_home, container, false)
		
		view.findViewById<Button>(R.id.button_home_to_settings).setOnClickListener {
			/**
			 * 使用 Navigation 进行跳转
			 * 参数 1：导航图中定义的 action id
			 */
			findNavController().navigate(R.id.action_home_to_settings)
		}

		return view
	}
	
}
```

8. 在 settings Fragment 的代码文件 `SettingsFragment` 中编写代码，点击按钮跳转至首页

```kotlin
package com.yuehai.y_chat.ui.settings

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 9:13
 */
class SettingsFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_settings, container, false)
		
		view.findViewById<Button>(R.id.button_settings_to_home).setOnClickListener {
			/**
			 * 使用 Navigation 进行跳转
			 * 参数 1：导航图中定义的 action id
			 */
			findNavController().navigate(R.id.action_settings_to_home)
		}

		return view
	}
	
}
```

#### Ⅱ、传递参数

> 使用 `Bundle` 传递参数

1. 在 home Fragment 的代码文件 `HomeFragment` 中编写代码，点击按钮跳转至设置，并传递代码

```kotlin
package com.yuehai.y_chat.ui.home

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 8:59
 * 首页
 */
class HomeFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_home, container, false)
		
		view.findViewById<Button>(R.id.button_home_to_settings).setOnClickListener {
			// 使用 Bundle 设置值
			val bundle = Bundle()
			bundle.putString("月海", "button_home_to_settings")
			/**
			 * 使用 Navigation 进行跳转
			 * 参数 1：导航图中定义的 action id
			 * 参数 2：需要传递的参数，非必须
			 */
			findNavController().navigate(R.id.action_home_to_settings, bundle)
		}
		
		// 打印接收的消息
		Log.i("月海", "${arguments?.getString("月海")}")
		
		return view
	}
	
}
```

2. 在 settings Fragment 的代码文件 `SettingsFragment` 中编写代码，点击按钮跳转至首页，并传递代码

```kotlin
package com.yuehai.y_chat.ui.settings

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.yuehai.y_chat.R

/**
 * @author 月海
 * @create 2023/9/22 9:13
 */
class SettingsFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_settings, container, false)
		
		view.findViewById<Button>(R.id.button_settings_to_home).setOnClickListener {
			// 使用 Bundle 设置值
			val bundle = Bundle()
			bundle.putString("月海", "button_settings_to_home")
			/**
			 * 使用 Navigation 进行跳转
			 * 参数 1：导航图中定义的 action id
			 * 参数 2：需要传递的参数，非必须
			 */
			findNavController().navigate(R.id.action_settings_to_home, bundle)
		}
		
		// 打印接收的消息
		Log.i("月海", "${arguments?.getString("月海")}")
		
		return view
	}
	
}
```

#### Ⅲ、进入退出动画

1. 在 `anim` 中创建动画 `enter_left_slide.xml` 和 `exit_shrinks_centre.xml`，和上面 4 中一样
2. 再次在 `anim` 中创建动画 `enter_magnify_centre.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 向中心放大进入的动画 -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
	<!--
		fromXScale 和 fromYScale 设置动画的初始缩放比例，这里将视图缩小到 90%
		toXScale 和 toYScale 设置动画的最终缩放比例，这里将视图恢复到原始大小
		pivotX 和 pivotY 设置缩放动画的中心点位置，这里将中心点设置为视图的中心。
		duration 设置动画的持续时间，以毫秒为单位
	 -->
	<scale
			android:fromXScale="0.9"
			android:fromYScale="0.9"
			android:toXScale="1.0"
			android:toYScale="1.0"
			android:pivotX="50%"
			android:pivotY="50%"
			android:duration="300" />
</set>
```

3. 再次在 `anim` 中创建动画 `exit_left_slide.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 从左侧滑出的动画 -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
	<!--
		从左侧滑出
		android:fromXDelta：开始时 X 轴上的偏移量，这里设置为 0，表示在屏幕中心
		android:toXDelta：结束时 X 轴上的偏移量，这里设置为 -100%p 表示完全在屏幕左侧以外
		android:duration：动画持续时间，这里设置为 300 毫秒。
	 -->
	<translate
			android:fromXDelta="0"
			android:toXDelta="-100%p"
			android:duration="300" />
	
	<!--
		淡入
		android:fromAlpha：开始时的透明度，1.0 表示完全不透明。
		android:toAlpha：结束时的透明度，0.0 表示完全透明。
		android:duration：动画持续时间，这里设置为 300 毫秒。
	 -->
	<alpha
			android:fromAlpha="1.0"
			android:toAlpha="0.0"
			android:duration="300" />
</set>
```

4. 在 `nav_graph.xml` 导航图中使用，属性说明：
	1. android:id：该 action 的唯一标识符，跳转 fragment 时需要使用此 id
	2. app:destination：指定跳转到的 fragment
	3. app:enterAnim：进入（入栈）时的动画效果，这些动画会在导航到目标目的地时播放
	4. app:exitAnim：退出（出栈）时的动画效果，这些动画会在导航到目标目的地时播放
	5. app:popEnterAnim：返回（后退）时进入（入栈）时的动画效果。这些动画会在返回到前一个目的地时播放
	6. app:popExitAnim：返回（后退）时退出（出栈）时的动画效果。这些动画会在返回到前一个目的地时播放

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 导航图 -->
<!--
	startDestination：指定默认显示的 fragment id
 -->
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
			xmlns:app="http://schemas.android.com/apk/res-auto"
			xmlns:tools="http://schemas.android.com/tools"
			android:id="@+id/nav_graph"
			app:startDestination="@id/fragment_home">
	
	<!-- 首页 -->
	<fragment
			android:id="@+id/fragment_home"
			android:name="com.yuehai.y_chat.ui.home.homeFragment"
			android:label="home"
			tools:layout="@layout/fragment_home">

		<!--
			首页 -> 设置
			android:id：该 action 的唯一标识符，跳转 fragment 时需要使用此 id
			app:destination：指定跳转到的 fragment
			app:enterAnim：进入（入栈）时的动画效果，这些动画会在导航到目标目的地时播放
			app:exitAnim：退出（出栈）时的动画效果，这些动画会在导航到目标目的地时播放
			app:popEnterAnim：返回（后退）时进入（入栈）时的动画效果。这些动画会在返回到前一个目的地时播放
			app:popExitAnim：返回（后退）时退出（出栈）时的动画效果。这些动画会在返回到前一个目的地时播放
		 -->
		<action
				android:id="@+id/action_home_to_settings"
				app:destination="@id/fragment_settings"
				app:enterAnim="@anim/enter_left_slide"
				app:exitAnim="@anim/exit_shrinks_centre"
				app:popEnterAnim="@anim/enter_magnify_centre"
				app:popExitAnim="@anim/exit_left_slide"/>
	</fragment>
	
	<!-- 设置 -->
	<fragment
			android:id="@+id/fragment_settings"
			android:name="com.yuehai.y_chat.ui.settings.settingsFragment"
			android:label="settings"
			tools:layout="@layout/fragment_settings">

		<!-- 设置 -> 首页 -->
		<action
				android:id="@+id/action_settings_to_home"
				app:destination="@id/fragment_home"
				app:enterAnim="@anim/enter_left_slide"
				app:exitAnim="@anim/exit_shrinks_centre"
				app:popEnterAnim="@anim/enter_magnify_centre"
				app:popExitAnim="@anim/exit_left_slide"/>
	</fragment>


</navigation>
```

### ③、

### ④、

## 2、主题

### ①、隐藏软件标题栏

1. 修改文件 `res/values/themes.xml`
2. 标签 `style` 的属性 `parent` 一开始可能为： `Theme.MaterialComponents.DayNight.DarkActionBar`，即深色标题栏

![|310](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508083412.png)

4. 要使其隐藏可修改为：`Theme.MaterialComponents.DayNight.NoActionBar`

![|310](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230508083306.png)

### ②、`res/values/themes.xml` 内容介绍

- res/values-night/themes.xml 是深色模式的配置文件，与此基本相同

```xml
<resources xmlns:tools="http://schemas.android.com/tools">
	<!-- Base application theme. -->
	<style name="Theme.Y_pic" parent="Theme.MaterialComponents.DayNight.NoActionBar">
		
		<!-- 主题颜色设置 -->
		<!-- 应用的主要色调，actionBar 默认使用该颜色，Toolbar 导航栏的底色 -->
		<item name="colorPrimary">@color/yuehai_light_blue</item>
		<!-- 应用的主要暗色调，statusBarColor 默认使用该颜色 -->
		<item name="colorPrimaryDark">@color/black</item>
		<!-- 一般控件的选中效果默认采用该颜色，如 CheckBox，RadioButton，SwitchCompat，ProcessBar等 -->
		<item name="colorAccent">@color/purple_700</item>
		<item name="colorPrimaryVariant">@color/purple_700</item>
		<item name="colorOnPrimary">@color/white</item>
		<!-- 图片标题或者字幕、Medium、action bar subtitle等 -->
		<item name="colorSecondary">@color/teal_200</item>
		<item name="colorSecondaryVariant">@color/teal_700</item>
		<item name="colorOnSecondary">@color/black</item>
		
		<!-- 状态栏、顶部导航栏 相关 -->
		<!-- 状态栏颜色 -->
		<item name="android:statusBarColor">@color/yuehai_light_blue</item>
		<!-- activity 是否能在 status bar 底部绘制 -->
		<item name="android:windowOverscan">true</item>
		<!-- 让 status bar 透明，相当于 statusBarColor=transparent + windowOverscan=true -->
		<item name="android:windowTranslucentStatus">true</item>
		<!-- 改变status bar 文字颜色， true黑色， false白色，API23可用-->
		<!-- <item name="android:windowLightStatusBar">true</item> -->
		<!-- 全屏显示，隐藏状态栏、导航栏、底部导航栏 -->
		<item name="android:windowFullscreen">true</item>
		
		<!-- 隐藏标题栏 -->
		<item name="windowNoTitle">true</item>
		<!-- 底部虚拟导航栏颜色 -->
		<item name="android:navigationBarColor">#E91E63</item>
		<!-- 让底部导航栏变半透明灰色，覆盖在Activity之上（默认false，activity会居于底部导航栏顶部），如果设为true，navigationBarColor 失效 -->
		<item name="android:windowTranslucentNavigation">true</item>
		
		<!-- WindowBackground，可以设置@drawable，颜色引用（@color），不能设置颜色值（#fffffff），
		Window区域说明：Window涵盖整个屏幕显示区域，包括StatusBar的区域。当windowOverscan=false时，window的区域比Activity多出StatusBar，当windowOverscan=true时，window区域与Activity相同-->
		<item name="android:windowBackground">@drawable/ic_launcher_background</item>
		<!--<item name="android:windowBackground">@color/light_purple</item>-->
		
		<!-- 控件相关 -->
		<!-- button 文字是否全部大写（系统默认开）-->
		<item name="android:textAllCaps">false</item>
		
		<!-- 默认 Button,TextView的文字颜色 -->
		<item name="android:textColor">#B0C4DE</item>
		<!-- 默认 EditView 输入框字体的颜色 -->
		<item name="android:editTextColor">#E6E6FA</item>
		<!-- RadioButton checkbox等控件的文字 -->
		<item name="android:textColorPrimaryDisableOnly">#1C71A9</item>
		<!-- 应用的主要文字颜色,actionBar的标题文字默认使用该颜色 -->
		<item name="android:textColorPrimary">#FFFFFF</item>
		<!-- 辅助的文字颜色，一般比textColorPrimary的颜色弱一点，用于一些弱化的表示 -->
		<item name="android:textColorSecondary">#C1C1C1</item>
		<!-- 控件选中时的颜色,默认使用colorAccent -->
		<item name="android:colorControlActivated">#FF7F50</item>
		<!-- 控件按压时的色调-->
		<item name="android:colorControlHighlight">#FF00FF</item>
		<!-- CheckBox,RadioButton,SwitchCompat等默认状态的颜色 -->
		<item name="android:colorControlNormal">#FFD700</item>
		<!-- 默认按钮的背景颜色 -->
		<item name="android:colorButtonNormal">#1C71A9</item>
		
	</style>
</resources>
```


### ③、自定义字体

#### Ⅰ、使用 API 提供的默认字体

1. 以下几种：
	1. `noraml` ：普通字体,系统默认使用的字体
	2. `sans` ：非衬线字体
	3. `serif` ：衬线字体
	4. `monospace` ：等宽字体
2. xml 中 TextView 设置：

```xml
android:typeface="monospace"
```

3. java 代码 TextView 设置：

```kotlin
myText.setTypeface(Typeface.MONOSPACE);
```

#### Ⅱ、将字体文件放在 `assets` 目录中

1. 将字体文件放在 `assets` 目录中

![|682](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231227152014.png)

2. java 代码 TextView 设置：

```kotlin
Typeface typeface = Typeface.createFromAsset(getAssets(), "font/opposans.ttf");
myTextView.setTypeface(typeface);
```

#### Ⅲ、将字体文件放在 `res/font` 下

1. 安卓8.0后，在工程目录 `res` 下，创建一个 `font` 文件夹，把字体文件放入文件夹中，如图：

![|267](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231227152230.png)

2. xml 中 TextView 设置：

```xml
android:fontFamily="@font/opposans"
```

3. java 代码 TextView 设置：

```kotlin
if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
      Typeface typeface = getResources().getFont(R.font.opposans);
      myTextView.setTypeface(typeface);
}
```

4. 如果想整个 activity 界面都使用此字体，旧版 AS 工程在 `res/values/styles.xml` 中，新版 AS 工程在 `res/values/themes.xml` 中加入如下style

```xml
<style name="MyFont" parent="AppTheme">
   <item name="android:fontFamily">@font/opposans</item>
</style>
```

5. `manifest.xml` 中

```xml
<activity
		android:name=".MainActivity"
		android:theme="@style/MyFont" />
```

6. 如果想整个 APP 界面都使用此字体，在 `manifest.xml` 中

```xml
    <application
        android:theme="@style/AppTheme">
```

7. `styles.xml` 或者 `themes.xml` 中

```xml
<style name="AppTheme" parent="xxx">
   <item name="android:fontFamily">@font/opposans</item>
</style>
```

#### Ⅳ、

#### Ⅴ、


### ④、

## 3、动画

### ①、anim 动画

1. 在 `res` 目录下新建 `anim` 目录，然后右键 `anim` 目录，点击新建，选择 `Animation` 资源文件，名称随意，本次为 `enter_left_slide`

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230922112559.png)

2. 打开 `enter_left_slide.xml` 文件，编写动画代码

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 从左侧划入的动画 -->
<!--
	<set> 是一个动画集合，用于同时播放多个动画。在这里，我们将两种动画效果放在一起，使它们同时播放。
 -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
	<!--
		从左侧划入
		android:fromXDelta：开始时 X 轴上的偏移量，这里设置为 -100%p 表示完全在屏幕左侧以外
		android:toXDelta：结束时 X 轴上的偏移量，这里设置为 0，表示在屏幕中心
		android:duration：动画持续时间，这里设置为 300 毫秒。
	 -->
	<translate
			android:fromXDelta="-100%p"
			android:toXDelta="0"
			android:duration="300" />
	
	<!--
		淡入
		android:fromAlpha：开始时的透明度，0.0 表示完全透明。
		android:toAlpha：结束时的透明度，1.0 表示完全不透明。
		android:duration：动画持续时间，这里设置为 300 毫秒。
	 -->
	<alpha
			android:fromAlpha="0.0"
			android:toAlpha="1.0"
			android:duration="300" />
	
</set>
```

3. 再次新建一个文件 `exit_shrinks_centre.xml` ，编写动画代码

```xml
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">
	
	<!--
		fromXScale 和 fromYScale 设置动画的初始缩放比例，这里将视图缩小到 0
		toXScale 和 toYScale 设置动画的最终缩放比例，这里将视图恢复到原始大小
		pivotX 和 pivotY 设置缩放动画的中心点位置，这里将中心点设置为视图的中心。
		duration 设置动画的持续时间，以毫秒为单位
	 -->
	<scale
			android:fromXScale="1.0"
			android:fromYScale="1.0"
			android:toXScale="0.9"
			android:toYScale="0.9"
			android:pivotX="50%"
			android:pivotY="50%"
			android:duration="300" />

</set>
```

4. 在使用动画的 `Activity` 中使用动画：
	1. 设置进入动画：在 `onCreate`方法中，调用完 `setContentView` 方法之后，使用 `overridePendingTransition` 方法使用动画
	2. 设置退出动画：重写 `finish` 方法，调用完 `super.finish()` 方法之后，使用 `overridePendingTransition` 方法使用动画

```kotlin
package com.yuehai.pic.ui.activity

import com.yuehai.pic.R

/**
 * 图片详情页 Activity
 */
class ImageViewerActivity: AppCompatActivity() {

	override fun onCreate(savedInstanceState: Bundle?) {
		super.onCreate(savedInstanceState)
		// 设置内容视图；当前的组件显示哪个视图（窗口）；R 就是 res 包
		setContentView(R.layout.activity_image_viewer)
		
		/**
		 * 应用 activity 跳转动画
		 * 参数 1：要进入的的 activity 的进入动画，为 0 则为没有任何动画效果
		 * 参数 2：当前的 activity 的退出动画，为 0 则为没有任何动画效果
		 */
		overridePendingTransition(R.anim.image_details_enter, 0)
		
	}
	
	/**
	 * 当用户按下 back 键时，默认行为是关闭当前的 Activity，调用此方法
	 */
	override fun finish() {
		super.finish()
		/**
		 * 应用 activity 跳转动画
		 * 参数 1：要进入的的 activity 的进入动画，为 0 则为没有任何动画效果
		 * 参数 2：当前的 activity 的退出动画，为 0 则为没有任何动画效果
		 */
		overridePendingTransition(0, R.anim.image_details_exit)
	}
	
}
```

### ②、kotlin 代码中设置并执行动画

#### Ⅰ、介绍

1. 可使用 `public static ObjectAnimator ofFloat(Object target, String propertyName, float... values)` 方法来创建动画对象

```kotlin
// 动画的起始和结束位置
val startX = 1280f
val endX = 0f

// 设置积分倍率弹窗的初始状态
include_animator_test.translationX = startX
include_animator_test.visibility = View.VISIBLE

// 创建位移动画对象；屏幕左上角为 0,0
val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
// 设置动画的插值器；DecelerateInterpolator 是一个减速插值器。它会使动画在开始时较快，然后逐渐减速，给人一种减缓到达终点的效果
translateAnimator.interpolator = DecelerateInterpolator()
// 设置动画的持续时间
translateAnimator.duration = 300

// 启动动画
translateAnimator.start()
```

2. 可使用 `AnimatorSet()` 来创建动画集合，使多个动画按照指定的方式进行播放：

| 常用方法                                           | 介绍                                        |
| -------------------------------------------------- | ------------------------------------------- |
| play(Animator anim)                                | 将指定的动画添加到 AnimatorSet 中，配合 `before()` 方法可以指定顺序进行播放  |
| playTogether(Animator... animators)                | 将多个动画同时播放。                        |
| playSequentially(Animator... animators)            | 将多个动画按顺序播放。                      |
| setDuration(long duration)                         | 设置动画的持续时间。                        |
| setInterpolator(TimeInterpolator interpolator)     | 设置动画的插值器，用于控制动画的变化速率。  |
| setStartDelay(long startDelay)                     | 设置动画的延迟开始时间。                    |
| addListener(Animator.AnimatorListener listener)    | 添加动画监听器，用于监听动画的各个阶段。    |
| removeListener(Animator.AnimatorListener listener) | 移除动画监听器。                            |
| clone()                                            | 创建一个 AnimatorSet 的副本。               |
| getChildAnimations()                               | 获取 AnimatorSet 中包含的所有动画。         |
| getDuration()                                      | 获取动画的持续时间。                        |
| getStartDelay()                                    | 获取动画的延迟开始时间。                    |
| getInterpolator()                                  | 获取动画的插值器。                          |

4. `AnimatorSet()` 的使用看下方的实例


#### Ⅱ、实例

1. 积分增加 icon 图标 `ic_poc_points_up`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="632dp"
    android:height="138dp"
    android:viewportWidth="632"
    android:viewportHeight="138">
  <path
      android:pathData="M98.28,58.24C97.21,63.72 91.75,68.62 86.19,69.11C80.54,69.6 76.94,65.49 78.02,60.01C79.11,54.45 84.46,49.64 90.11,49.15C95.67,48.66 99.37,52.68 98.28,58.24ZM91.92,58.8C92.31,56.77 90.94,55.24 88.88,55.42C86.82,55.6 84.78,57.43 84.38,59.46C83.99,61.49 85.36,63.02 87.42,62.84C89.48,62.66 91.52,60.83 91.92,58.8ZM49.04,56.39L64.46,55.04L61.77,68.73L77.01,67.39C78.17,69.12 79.89,71.57 85.63,71.07C87.78,70.88 89.02,70.42 90.45,69.86L88.35,80.55L58.94,83.12L49.51,131.16L34.09,132.51L43.52,84.47L14.11,87.04L16.94,72.65L46.35,70.08L49.04,56.39ZM13.06,132.79L3.59,122.25C7.96,118.4 16.39,110.89 21.72,92.28L35.63,92.8C29.51,115.9 20.5,125.89 13.06,132.79ZM63.42,90.37L78.4,87.24C76.7,106.22 82.11,112.78 84.89,116.09L70.53,128.2C65.84,121.58 61.57,113.27 63.42,90.37ZM144.02,77.94L134.94,124.21L118.17,125.68L125.14,90.18C120.25,93.12 109.04,99.48 94.22,104.95L89,92.04C103.72,87.1 117.87,79.18 131.41,70.36C143.15,62.65 151.32,55.16 163.1,44.07L175.09,52.56C170.63,56.86 161.29,65.84 144.02,77.94ZM214.68,57.35L203.57,72.21C195.23,66.69 186.07,63.06 177.69,60.84L187.18,47.08C198.5,49.56 207.55,53.28 214.68,57.35ZM172.39,120.59L170.36,104.45C205.54,98.51 226.18,84.98 243.31,47.98L256.48,54.04C232.68,104.38 200.11,114.08 172.39,120.59ZM280.61,35.26L297.65,33.77L293.61,54.35C306.51,57.3 321.58,62.66 332.61,68.9L320.99,85.89C313.88,80.78 299.84,73.33 290.4,70.68L282.39,111.49L265.35,112.97L280.61,35.26ZM335.24,107.99L327.34,96.62C352.51,85.56 360.26,72.56 364.14,49.65L380.46,48.22C379.7,51.68 379,54.77 377.72,59.05C389.88,52.78 394.99,44.7 396.78,41.85L337.25,47.06L340.18,32.13L419.53,25.19C412.33,47.95 401.3,60.11 384.38,70.45L376.79,62C367.88,90.29 347.2,102.26 335.24,107.99ZM438.11,63.4L424.41,67.64C424.45,62.95 424.2,54.81 421.71,45.48L434.64,41.14C437.08,47.96 437.82,55.88 438.11,63.4ZM459.48,58.24L446.28,62.17C446.35,51.49 445.52,45.83 444.26,40.12L457.01,36.67C459.71,44.94 459.56,54.67 459.48,58.24ZM425.89,100.49L420.84,88.96C452.33,78.91 462.58,69.33 475.99,35.18L490.61,37.46C481.94,57.83 469.31,87.15 425.89,100.49ZM503.21,20.82L559.7,15.88C558.06,25.13 562.27,29.71 571.91,28.61C561.69,63.18 536.83,82.97 501.62,92.65L497.06,78.64C540.4,69.3 550.1,45.01 554.51,31.52L500.18,36.27L503.21,20.82ZM583.18,14.78C582.07,20.43 576.5,25.43 570.77,25.93C565.12,26.43 561.36,22.24 562.47,16.59C563.58,10.94 569.14,5.94 574.79,5.44C580.54,4.85 584.29,9.13 583.18,14.78ZM576.9,15.33C577.34,13.12 575.91,11.42 573.58,11.63C571.33,11.82 569.09,13.84 568.65,16.05C568.2,18.34 569.74,19.95 571.98,19.75C574.31,19.55 576.45,17.62 576.9,15.33ZM613.39,9.01L629.71,7.58L618,56.43L605.72,57.51L613.39,9.01ZM603.27,63.71L618.33,62.39L615.41,77.23L600.35,78.55L603.27,63.71Z"
      android:fillColor="#E60012"/>
</vector>
```

2. 向右箭头 icon 图标 `ic_poc_chevron_right`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="113dp"
    android:height="78dp"
    android:viewportWidth="113"
    android:viewportHeight="78">
  <path
      android:pathData="M85.26,31.01L8.18,31.01C6.01,31.01 3.93,31.87 2.4,33.41C0.86,34.94 -0,37.01 -0,39.18C-0,41.35 0.86,43.42 2.4,44.96C3.93,46.49 6.01,47.35 8.18,47.35L84.88,47.35L68.51,63.92C66.98,65.47 66.12,67.57 66.12,69.75C66.12,71.93 66.98,74.03 68.51,75.58C70.04,77.12 72.12,77.99 74.29,78C76.46,78.01 78.54,77.16 80.08,75.64L110.61,45.19C111.36,44.43 111.97,43.53 112.38,42.54C112.79,41.55 113,40.49 113,39.42C113,38.35 112.79,37.29 112.38,36.3C111.97,35.31 111.36,34.41 110.61,33.65L79.28,2.39C78.13,1.25 76.68,0.47 75.09,0.16C73.5,-0.16 71.86,0 70.36,0.62C68.87,1.24 67.59,2.29 66.69,3.63C65.79,4.97 65.32,6.55 65.31,8.17C65.32,9.21 65.53,10.24 65.94,11.19C66.35,12.14 66.95,13 67.71,13.72L85.26,31.01Z"
      android:fillColor="#ffffff"/>
</vector>

```

3. 外层盒子 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- 省略中间代码 -->

    <include
        android:id="@+id/include_animator_test"
        layout="@layout/poc_animator_test_content"
        android:layout_width="match_parent"
        android:layout_height="465dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        android:visibility="gone"
        tools:visibility="visible"/>
    
</androidx.constraintlayout.widget.ConstraintLayout>
```

4. 动画例子 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	xmlns:app="http://schemas.android.com/apk/res-auto"
	android:layout_width="match_parent"
	android:layout_height="465dp"
	android:gravity="center"
	android:background="#80000000"
	android:orientation="vertical">

	<ImageView
		android:id="@+id/content_points_up"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		app:layout_constraintTop_toTopOf="parent"
		app:layout_constraintBottom_toBottomOf="parent"
		app:layout_constraintStart_toStartOf="parent"
		app:layout_constraintEnd_toEndOf="parent"
		android:layout_marginTop="@dimen/dp_40"
		android:src="@drawable/ic_poc_points_up"/>
	
	<androidx.constraintlayout.widget.ConstraintLayout
		android:layout_width="match_parent"
		android:layout_height="match_parent"
		android:gravity="start|center"
		android:orientation="horizontal">
		
		<TextView
			android:id="@+id/content_multiple_front"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintEnd_toStartOf="@+id/content_times_front"
			android:text="1"
			android:textSize="240sp"
			android:textColor="@color/white"
			android:textStyle="bold"/>
		<TextView
			android:id="@+id/content_times_front"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintEnd_toStartOf="@+id/content_chevron_right"
			android:layout_marginEnd="@dimen/dp_50"
			android:text="倍"
			android:textSize="120sp"
			android:textColor="@color/white"
			android:textStyle="bold"/>
		
		<ImageView
			android:id="@+id/content_chevron_right"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintStart_toStartOf="parent"
	        app:layout_constraintEnd_toEndOf="parent"
			android:src="@drawable/ic_poc_chevron_right"/>
		
		<TextView
			android:id="@+id/content_point"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
			app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toEndOf="@+id/content_chevron_right"
			android:layout_marginStart="@dimen/dp_50"
			android:text="ポ\nイ\nン\nト"
			android:textSize="23sp"
			android:textColor="#FFF200"
			android:textStyle="bold"/>
		<TextView
			android:id="@+id/content_multiple_back"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintStart_toEndOf="@+id/content_point"
			app:layout_constraintEnd_toStartOf="@+id/content_times_back"
			android:text="2"
			android:textSize="120sp"
			android:textColor="#FFF200"
			android:textStyle="bold"/>
		<TextView
			android:id="@+id/content_times_back"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintStart_toEndOf="@+id/content_multiple_back"
			android:text="倍"
			android:textSize="60sp"
			android:textColor="#FFF200"
			android:textStyle="bold"
			android:textFontWeight="@integer/config_navAnimTime"/>
	</androidx.constraintlayout.widget.ConstraintLayout>
    
</LinearLayout>
```

5. kotlin 动画代码，省略上方代码，只保留了动画代码

```kotlin
// 启动动画
private fun animateBlackBox() {
	// 动画开始时，重置字号
	content_multiple_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, 240f)
	content_times_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	content_multiple_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	content_times_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, 60f)
	content_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, 23f)
	// 停止动画集合
	combinedAnimatorSet.cancel()
	combinedAnimatorSet.clone()
	
	
	// 进入动画弹回效果，按顺序播放
	val animateEnterBounce = AnimatorSet()
	animateEnterBounce.playSequentially(animateScoreMultiplierEnterBounceMoveRight(), animateScoreMultiplierkEnterBounceMoveLeft())
	
	// 字号变化动画 1，字号变化回弹的前半部分，同时播放
	val animateFontSizeChangeOne = AnimatorSet()
	animateFontSizeChangeOne.playTogether(animateTextShrinkFront(), animateTextEnlargeBack())
	// 字号变化动画 2，字号变化回弹的后半部分，同时播放
	val animateFontSizeChangeTwo = AnimatorSet()
	animateFontSizeChangeTwo.playTogether(animateTextEnlargeFront(), animateTextShrinkBack())
	// 字号变化动画 总，按顺序播放
	val animateFontSizeChange = AnimatorSet()
	animateFontSizeChange.startDelay = 500
	animateFontSizeChange.playSequentially(animateFontSizeChangeOne, animateFontSizeChangeTwo)
	
	// 滑出动画，按顺序播放
	val animateExit = AnimatorSet()
	animateExit.playSequentially(animateScoreMultiplierExit())
	animateExit.startDelay = 1000
	// 滑出动画弹回效果，按顺序播放
	val animateExitBounce = AnimatorSet()
	animateExitBounce.playSequentially(animateScoreMultiplierExitBounceMoveRight(), animateScoreMultiplierExitBounceMoveLeft())
	
	// 动画集合，按顺序播放
	combinedAnimatorSet.playSequentially(
		// 进入动画
		animateScoreMultiplierEnter(),
		// 进入动画弹回效果
		animateEnterBounce,
		// 字号变化动画 总，按顺序播放
		animateFontSizeChange,
		// 滑出动画
		animateExit,
		// 滑出动画弹回效果
		animateExitBounce
	)
	// 启动动画集合
	combinedAnimatorSet.start()
}

// 积分倍率弹窗进入动画
private fun animateScoreMultiplierEnter(): ObjectAnimator{
	// 动画的起始和结束位置
	val startX = 1280f
	val endX = 0f
	
	// 设置积分倍率弹窗的初始状态
	include_animator_test.translationX = startX
	include_animator_test.visibility = View.VISIBLE
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	// 设置动画的插值器
	translateAnimator.interpolator = DecelerateInterpolator()
	// 设置动画的持续时间
	translateAnimator.duration = 300
	
	return translateAnimator
}
// 积分倍率弹窗进入动画，弹回效果动画，右移
fun animateScoreMultiplierEnterBounceMoveRight(): ObjectAnimator{
	val startX = 0f
	val endX = 20f
	
	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	translateAnimator.interpolator = DecelerateInterpolator()
	translateAnimator.duration = 150

	return translateAnimator
}
// 积分倍率弹窗进入动画，弹回效果动画，左移
fun animateScoreMultiplierkEnterBounceMoveLeft(): ObjectAnimator{
	val startX = 20f
	val endX = 0f
	
	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	translateAnimator.interpolator = DecelerateInterpolator()
	translateAnimator.duration = 150

	return translateAnimator
}

// 积分倍率弹窗滑出动画
fun animateScoreMultiplierExit(): ObjectAnimator{
	val startX = 0f
	val endX = -1280f

	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	translateAnimator.interpolator = DecelerateInterpolator()
	translateAnimator.duration = 300

	return translateAnimator
}
// 积分倍率弹窗滑出动画，弹回效果动画，右移
fun animateScoreMultiplierExitBounceMoveRight(): ObjectAnimator{
	val startX = -1280f
	val endX = -1260f
	
	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	translateAnimator.interpolator = DecelerateInterpolator()
	translateAnimator.duration = 150
	
	return translateAnimator
}
// 积分倍率弹窗滑出动画，弹回效果动画，左移
fun animateScoreMultiplierExitBounceMoveLeft(): ObjectAnimator{
	val startX = -1260f
	val endX = -1280f
	
	val translateAnimator = ObjectAnimator.ofFloat(include_animator_test, "translationX", startX, endX)
	translateAnimator.interpolator = DecelerateInterpolator()
	translateAnimator.duration = 150
	
	return translateAnimator
}

// 前面的字变小动画，字号变化回弹的前半部分
fun animateTextShrinkFront(): AnimatorSet{
	val frontMultipleAnimator = ValueAnimator.ofFloat(240f, 100f)
		.apply {
			duration = animateFontSizeChangeOneTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_multiple_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val frontTimesAnimator = ValueAnimator.ofFloat(120f, 50f)
		.apply {
			duration = animateFontSizeChangeOneTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_times_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextShrinkFront = AnimatorSet()
	animateTextShrinkFront.playTogether(frontMultipleAnimator, frontTimesAnimator)
	
	return animateTextShrinkFront
}
// 后面的字变大动画，字号变化回弹的前半部分
fun animateTextEnlargeBack(): AnimatorSet{
	val backMultipleAnimator = ValueAnimator.ofFloat(120f, 250f)
		.apply {
			duration = animateFontSizeChangeOneTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_multiple_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val backTimesAnimator = ValueAnimator.ofFloat(60f, 130f)
		.apply {
			duration = animateFontSizeChangeOneTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_times_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val pointAnimator = ValueAnimator.ofFloat(23f, 50f)
		.apply {
			duration = animateFontSizeChangeOneTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextEnlargeBack = AnimatorSet()
	animateTextEnlargeBack.playTogether(backMultipleAnimator, backTimesAnimator, pointAnimator)
	
	return animateTextEnlargeBack
}

// 前面的字变大动画，字号变化回弹的后半部分
fun animateTextEnlargeFront(): AnimatorSet{
	val frontMultipleAnimator = ValueAnimator.ofFloat(100f, 120f)
		.apply {
			duration = animateFontSizeChangeTwoTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_multiple_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val frontTimesAnimator = ValueAnimator.ofFloat(50f, 60f)
		.apply {
			duration = animateFontSizeChangeTwoTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_times_front.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextShrinkFront = AnimatorSet()
	animateTextShrinkFront.playTogether(frontMultipleAnimator, frontTimesAnimator)
	
	return animateTextShrinkFront
}
// 后面的字变小动画，字号变化回弹的后半部分
fun animateTextShrinkBack(): AnimatorSet{
	val backMultipleAnimator = ValueAnimator.ofFloat(250f, 240f)
		.apply {
			duration = animateFontSizeChangeTwoTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_multiple_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val backTimesAnimator = ValueAnimator.ofFloat(130f, 120f)
		.apply {
			duration = animateFontSizeChangeTwoTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_times_back.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val pointAnimator = ValueAnimator.ofFloat(50f, 46f)
		.apply {
			duration = animateFontSizeChangeTwoTime
			addUpdateListener {
				val value = it.animatedValue as Float
				content_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextEnlargeBack = AnimatorSet()
	animateTextEnlargeBack.playTogether(backMultipleAnimator, backTimesAnimator, pointAnimator)
	
	return animateTextEnlargeBack
}
```

6. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画3.gif)

#### Ⅲ、上面动画的简化板

> 1. `ObjectAnimator.ofFloat()` 和 `ValueAnimator.ofFloat()` 都可以传递多个参数
> 2. 所以回弹效果不用分开写，向方法中传入多个参数即可
> 3. 动画效果略有修改
> 4. 字体文件：[NotoSansCJKjp-Black.ttf](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FNotoSansCJKjp-Black.ttf)

1. 积分增加 icon 图标 `ic_poc_points_up`，同上
2. 向右箭头 icon 图标 `ic_poc_chevron_right`，同上
3. 外层盒子 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- 省略中间代码 -->

    <include
        android:id="@+id/include_animator_points_up"
        layout="@layout/poc_animator_points_up"
        android:layout_width="match_parent"
        android:layout_height="465dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        android:visibility="visible"
        tools:visibility="visible"/>
    
    <include
        android:id="@+id/include_animator_multiple_change"
        layout="@layout/poc_animator_multiple_change"
        android:layout_width="match_parent"
        android:layout_height="465dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        android:visibility="visible"
        tools:visibility="visible"/>
    
</androidx.constraintlayout.widget.ConstraintLayout>
```

4. 蒙版及积分增加 icon 图标 `include_animator_points_up`  xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	xmlns:app="http://schemas.android.com/apk/res-auto"
	android:layout_width="match_parent"
	android:layout_height="465dp"
	android:gravity="center|top"
	android:background="#80000000"
	android:orientation="vertical">

	<ImageView
		android:id="@+id/content_points_up"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		app:layout_constraintTop_toTopOf="parent"
		app:layout_constraintBottom_toBottomOf="parent"
		app:layout_constraintStart_toStartOf="parent"
		app:layout_constraintEnd_toEndOf="parent"
		android:layout_marginTop="@dimen/dp_25"
		android:src="@drawable/ic_poc_points_up"/>
	
</LinearLayout>
```

5. 倍率变化文字 `include_animator_multiple_change` xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	xmlns:app="http://schemas.android.com/apk/res-auto"
	android:layout_width="match_parent"
	android:layout_height="465dp"
	android:paddingTop="@dimen/dp_158"
	android:gravity="start|center">

		<TextView
			android:id="@+id/multiple_change_front_number"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toStartOf="parent"
			android:layout_marginStart="@dimen/dp_340"
			android:text="1"
			android:textSize="240sp"
			android:textColor="@color/white"
			android:includeFontPadding="false"/>
		<TextView
			android:id="@+id/multiple_change_front_times"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintStart_toEndOf="@+id/multiple_change_front_number"
			android:layout_marginEnd="@dimen/dp_50"
			android:text="倍"
			android:textSize="120sp"
			android:textColor="@color/white"
			android:includeFontPadding="false"/>
		
		<ImageView
			android:id="@+id/multiple_change_chevron_right"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
	        app:layout_constraintBottom_toBottomOf="parent"
	        app:layout_constraintStart_toStartOf="parent"
			android:layout_marginStart="640dp"
			android:src="@drawable/ic_poc_chevron_right"/>
		
		<LinearLayout
			android:id="@+id/multiple_change_later"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
			app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toStartOf="parent"
			android:gravity="center"
			android:layout_marginStart="835dp">
			<TextView
				android:id="@+id/multiple_change_later_point"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="ポ\nイ\nン\nト"
				android:textSize="23sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
			<TextView
				android:id="@+id/multiple_change_later_number"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="2"
				android:textSize="120sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
			<TextView
				android:id="@+id/multiple_change_later_times"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="倍"
				android:textSize="60sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
		</LinearLayout>
	
</androidx.constraintlayout.widget.ConstraintLayout>
```

6. kotlin 动画代码，省略上方代码，只保留了动画代码

```kotlin
// 创建动画集合
private val combinedAnimatorSet = AnimatorSet()


// 页面初始化时，设置积分倍数动画
setPointsMultiplierAnimation()
// 页面初始化时，设置字体
val fromAsset = Typeface.createFromAsset(requireContext().assets, "fonts/NotoSansCJK-Black.otf")
multiple_change_front_number.typeface = fromAsset
multiple_change_front_times.typeface = fromAsset
multiple_change_later_point.typeface = fromAsset
multiple_change_later_number.typeface = fromAsset
multiple_change_later_times.typeface = fromAsset

// 在某个点击事件中，初始化属性并执行动画
var pocPointNum = multiple_change_front_number.text.toString().toInt() + 1
if (pocPointNum >= 6){
    pocPointNum = 1
}
initializeAndStartAnimation(pocPointNum.toString(), (pocPointNum + 1).toString())


// 设置积分倍率变化的动画
private fun setPointsMultiplierAnimation() {
	// 滑入动画，同时播放；积分变大蒙版弹窗进入动画、积分倍率数字弹窗进入动画
	val animateUpEnter = AnimatorSet()
	animateUpEnter.playTogether(animatePointsUpEnter(), animateScoreMultiplierEnter())
	
	// 字号变化动画 + 箭头和后面的字移动动画，同时播放
	val animateFontSizeChange = AnimatorSet()
	animateFontSizeChange.startDelay = 350
	animateFontSizeChange.playTogether(
		// 前面的字变小动画
		animateTextShrinkFront(),
		// 后面的字变大动画
		animateTextEnlargeLater(),
		// 箭头和后面的字移动动画
		animateChevronAndTextMove()
	)
	
	// 滑出动画，同时播放；积分变大蒙版弹窗滑出动画、积分倍率数字弹窗滑出动画
	val animateExit = AnimatorSet()
	animateExit.startDelay = 1350
	animateExit.playTogether(animatePointsUpExit(), animateScoreMultiplierExit())
	
	// 动画集合，按顺序播放：进入动画、字号变化动画、滑出动画
	combinedAnimatorSet.playSequentially(animateUpEnter, animateFontSizeChange, animateExit)
}

// 重置动画属性并启动动画
private fun initializeAndStartAnimation(startPoints: String, endPoints: String){
	// 停止动画集合
	combinedAnimatorSet.cancel()
	
	// 动画开始时，重置字号
	multiple_change_front_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 240f)
	multiple_change_front_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, 23f)
	multiple_change_later_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 60f)
	// 动画开始时，重置控件位置
	multiple_change_chevron_right.translationX = 0f
	multiple_change_later.translationX = 0f
	
	// 动画开始时，设置积分倍率数字
	multiple_change_front_number.text = startPoints
	multiple_change_later_number.text = endPoints
	
	// 启动动画集合
	combinedAnimatorSet.start()
}

// 积分变大蒙版弹窗进入动画
private fun animatePointsUpEnter(): ObjectAnimator{
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(
		View.TRANSLATION_X,
		Keyframe.ofFloat(0f, 1280f),
		Keyframe.ofFloat(0.39f, 0f),
		Keyframe.ofFloat(0.75f, 20f),
		Keyframe.ofFloat(1f, 0f),
	)
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(include_animator_points_up, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = DecelerateInterpolator()
	// 设置动画的持续时间
	translateAnimator.duration = 600
	
	return translateAnimator
}
// 积分倍率数字弹窗进入动画
private fun animateScoreMultiplierEnter(): ObjectAnimator{
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(
		View.TRANSLATION_X,
		Keyframe.ofFloat(0f, 1280f),
		Keyframe.ofFloat(0.39f, 0f),
		Keyframe.ofFloat(0.75f, 5f),
		Keyframe.ofFloat(1f, 0f),
	)
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(include_animator_multiple_change, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = DecelerateInterpolator()
	// 设置动画的持续时间
	translateAnimator.duration = 600
	
	return translateAnimator
}

// 积分变大蒙版弹窗滑出动画
private fun animatePointsUpExit(): ObjectAnimator{
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(
		View.TRANSLATION_X,
		Keyframe.ofFloat(0f, 0f),
		Keyframe.ofFloat(0.227f, -1260f),
		Keyframe.ofFloat(0.318f, -1150f),
		Keyframe.ofFloat(0.523f, -1280f),
		Keyframe.ofFloat(0.614f, -1265f),
		Keyframe.ofFloat(0.864f, -1280f),
		Keyframe.ofFloat(0.932f, -1278f),
		Keyframe.ofFloat(1f, -1280f),
	)
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(include_animator_points_up, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = DecelerateInterpolator()
	// 设置动画的持续时间
	translateAnimator.duration = 733
	
	return translateAnimator
}
// 积分变大蒙版弹窗滑出动画
private fun animateScoreMultiplierExit(): ObjectAnimator{
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(
		View.TRANSLATION_X,
		Keyframe.ofFloat(0f, 0f),
		Keyframe.ofFloat(1f, -1280f),
	)
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(include_animator_multiple_change, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = DecelerateInterpolator()
	// 设置动画的持续时间
	translateAnimator.duration = 166
	
	return translateAnimator
}

// 前面的字变小动画
private fun animateTextShrinkFront(): AnimatorSet{
	val frontNumberAnimator = ValueAnimator.ofFloat(240f, 105f, 120f)
		.apply {
			duration = 416
			addUpdateListener {
				val value = it.animatedValue as Float
				multiple_change_front_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val frontTimesAnimator = ValueAnimator.ofFloat(120f, 52.5f, 60f)
		.apply {
			duration = 416
			addUpdateListener {
				val value = it.animatedValue as Float
				multiple_change_front_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextShrinkFront = AnimatorSet()
	animateTextShrinkFront.playTogether(frontNumberAnimator, frontTimesAnimator)
	
	return animateTextShrinkFront
}
// 后面的字变大动画
private fun animateTextEnlargeLater(): AnimatorSet{
	val pointAnimator = ValueAnimator.ofFloat(23f, 49f, 46f)
		.apply {
			duration = 416
			addUpdateListener {
				val value = it.animatedValue as Float
				multiple_change_later_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val laterNumberAnimator = ValueAnimator.ofFloat(120f, 255f, 240f)
		.apply {
			duration = 416
			addUpdateListener {
				val value = it.animatedValue as Float
				multiple_change_later_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	val laterTimesAnimator = ValueAnimator.ofFloat(60f, 127.5f, 120f)
		.apply {
			duration = 416
			addUpdateListener {
				val value = it.animatedValue as Float
				multiple_change_later_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, value)
			}
		}
	
	// 字号变化动画
	val animateTextEnlargeLater = AnimatorSet()
	animateTextEnlargeLater.playTogether(pointAnimator, laterNumberAnimator, laterTimesAnimator)
	
	return animateTextEnlargeLater
}

// 箭头和后面的字左移动画
private fun animateChevronAndTextMove(): AnimatorSet{
	val chevronStartX = 0f
	val chevronEndX = -103f
	val chevronAnimator = ObjectAnimator.ofFloat(multiple_change_chevron_right, View.TRANSLATION_X, chevronStartX, chevronEndX - 10, chevronEndX)
	chevronAnimator.duration = 416
	
	val contentStartX = 0f
	val contentEndX = -152f
	val contentAnimator = ObjectAnimator.ofFloat(multiple_change_later, View.TRANSLATION_X, contentStartX, contentEndX - 10, contentEndX)
	contentAnimator.duration = 416
	
	// 箭头和后面的字左移动画
	val animateChevronAndTextMove = AnimatorSet()
	animateChevronAndTextMove.playTogether(chevronAnimator, contentAnimator)
	
	return animateChevronAndTextMove
}
```

7. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画9.gif)

#### Ⅳ、上面动画的更加简化板

> 1. 可以发现上面的方法都很相似
> 2. 所以我们可以把共通的部分抽取出来，做成一个方法
> 3. 字体文件：[NotoSansCJKjp-Black.ttf](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FNotoSansCJKjp-Black.ttf)

1. 积分增加 icon 图标 `ic_poc_points_up`，同上
2. 向右箭头 icon 图标 `ic_poc_chevron_right`，同上
3. 外层盒子 xml 布局文件，同上
4. 蒙版及积分增加 icon 图标 `include_animator_points_up`  xml 布局文件，同上
5. 倍率变化文字 `include_animator_multiple_change` xml 布局文件，同上
6. kotlin 动画代码，省略上方代码，只保留了动画代码

```kotlin
// 创建动画集合
private val combinedAnimatorSet = AnimatorSet()


// 页面初始化时，设置积分倍数动画
setPointsMultiplierAnimation()
// 页面初始化时，设置字体
val fromAsset = Typeface.createFromAsset(requireContext().assets, "fonts/NotoSansCJK-Black.otf")
multiple_change_front_number.typeface = fromAsset
multiple_change_front_times.typeface = fromAsset
multiple_change_later_point.typeface = fromAsset
multiple_change_later_number.typeface = fromAsset
multiple_change_later_times.typeface = fromAsset

// 在某个点击事件中，初始化属性并执行动画
var pocPointNum = multiple_change_front_number.text.toString().toInt() + 1
if (pocPointNum >= 6){
    pocPointNum = 1
}
initializeAndStartAnimation(pocPointNum.toString(), (pocPointNum + 1).toString())


// 设置积分倍率变化的动画
private fun setPointsMultiplierAnimation() {
	// 积分变大蒙版弹窗进入动画
	val animatePointsUpEnter = animatePointViewMove(include_animator_points_up, 600, mapOf(
		0f to 1280f,
		0.39f to 0f,
		0.75f to 20f,
		1f to 0f
	), DecelerateInterpolator())
	// 积分倍率数字弹窗进入动画
	val animateScoreMultiplierEnter = animatePointViewMove(include_animator_multiple_change, 600, mapOf(
		0f to 1280f,
		0.39f to 0f,
		0.75f to 5f,
		1f to 0f
	), DecelerateInterpolator())
	// 积分变大蒙版弹窗滑出动画
	val animatePointsUpExit = animatePointViewMove(include_animator_points_up, 733, mapOf(
		0f to 0f,
		0.227f to -1260f,
		0.318f to -1150f,
		0.523f to -1280f,
		0.614f to -1265f,
		0.864f to -1280f,
		0.932f to -1278f,
		1f to -1280f
	), DecelerateInterpolator())
	// 积分倍率数字弹窗滑出动画
	val animateScoreMultiplierExit = animatePointViewMove(include_animator_multiple_change, 166, mapOf(
		0f to 0f,
		1f to -1280f
	), DecelerateInterpolator())
	
	// 箭头，左移
	val animateChevronRightFrontMove = animatePointViewMove(multiple_change_chevron_right, 416, mapOf(
		0f to 0f,
		0.5f to -113f,
		1f to -103f
	))
	// 后面的积分倍率数字，左移
	val animateScoreMultiplierTextLaterMove = animatePointViewMove(multiple_change_later, 416, mapOf(
		0f to 0f,
		0.5f to -162f,
		1f to -152f
	))
	
	// 滑入动画，同时播放；积分变大蒙版弹窗进入动画、积分倍率数字弹窗进入动画
	val animateUpEnter = AnimatorSet()
	animateUpEnter.playTogether(animatePointsUpEnter, animateScoreMultiplierEnter)
	
	// 字号变化动画 + 箭头和后面的字移动动画，同时播放
	val animateFontSizeChange = AnimatorSet()
	animateFontSizeChange.startDelay = 350
	animateFontSizeChange.playTogether(
		// 前面的字变小动画
		animateTextSizeChange(multiple_change_front_number, 240f, 105f, 120f),
		animateTextSizeChange(multiple_change_front_times, 120f, 52.5f, 60f),
		// 后面的字变大动画
		animateTextSizeChange(multiple_change_later_point, 23f, 49f, 46f),
		animateTextSizeChange(multiple_change_later_number, 120f, 255f, 240f),
		animateTextSizeChange(multiple_change_later_times, 60f, 127.5f, 120f),
		// 箭头，左移
		animateChevronRightFrontMove,
		// 后面的积分倍率数字，左移
		animateScoreMultiplierTextLaterMove
	)
	
	// 滑出动画，同时播放；积分变大蒙版弹窗滑出动画、积分倍率数字弹窗滑出动画
	val animateExit = AnimatorSet()
	animateExit.startDelay = 1350
	animateExit.playTogether(animatePointsUpExit, animateScoreMultiplierExit)
	
	// 动画集合，按顺序播放：进入动画、字号变化动画、滑出动画
	combinedAnimatorSet.playSequentially(animateUpEnter, animateFontSizeChange, animateExit)
}

// 重置动画属性并启动动画
private fun initializeAndStartAnimation(startPoints: String, endPoints: String){
	// 停止动画集合
	combinedAnimatorSet.cancel()
	
	// 动画开始时，重置字号
	multiple_change_front_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 240f)
	multiple_change_front_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, 23f)
	multiple_change_later_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 60f)
	// 动画开始时，重置控件位置
	multiple_change_chevron_right.translationX = 0f
	multiple_change_later.translationX = 0f
	
	// 动画开始时，设置积分倍率数字
	multiple_change_front_number.text = startPoints
	multiple_change_later_number.text = endPoints
	
	// 启动动画集合
	combinedAnimatorSet.start()
}

// 控件移动动画
private fun animatePointViewMove(
	// 移动的视图对象
	view: View,
	// 动画持续时间，单位为毫秒
	duration: Long,
	// 关键帧和对应的位置
	keyframePositions: Map<Float, Float>,
	// 插值器，默认为加速减速插值器
	interpolator: TimeInterpolator = AccelerateDecelerateInterpolator()
): ObjectAnimator{
	// 创建一个关键帧的列表
	val keyframes = keyframePositions.map { (fraction, value) ->
		// 创建每个关键帧
		Keyframe.ofFloat(fraction, value)
	}
	
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(View.TRANSLATION_X, *keyframes.toTypedArray())
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(view, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = interpolator
	// 设置动画的持续时间
	translateAnimator.duration = duration
	
	return translateAnimator
}

// TextView 文字大小变化动画
private fun animateTextSizeChange(textView: TextView, vararg textSize: Float): ValueAnimator{
	// 创建文字大小变化的动画对象
	val frontMultipleAnimator = ValueAnimator.ofFloat(*textSize)
	// 设置动画持续时间，单位为毫秒
	frontMultipleAnimator.duration = 416
	// 添加动画更新监听器
	frontMultipleAnimator.addUpdateListener {
		// 在动画更新时设置 TextView 的文字大小
		textView.setTextSize(TypedValue.COMPLEX_UNIT_SP, it.animatedValue as Float)
	}
	
	return frontMultipleAnimator
}
```

7. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画9.gif)

### ③、自定义 ConstraintLayout 动态剪切控件

> 1. 需求更改：
> 2. 划入时倍率文字并不是和蒙版一起从右侧滑入
> 3. 而是倍率文字本来就在页面中，只不过不显示；蒙版滑入时，被蒙版覆盖的倍率文字才会显示出来，滑出时同理
> 4. 具体的样式请看下面的效果图
> 5. 字体文件：[NotoSansCJKjp-Black.ttf](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FNotoSansCJKjp-Black.ttf)

1. 积分增加 icon 图标 `ic_poc_points_up`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="632dp"
    android:height="138dp"
    android:viewportWidth="632"
    android:viewportHeight="138">
  <path
      android:pathData="M98.28,58.24C97.21,63.72 91.75,68.62 86.19,69.11C80.54,69.6 76.94,65.49 78.02,60.01C79.11,54.45 84.46,49.64 90.11,49.15C95.67,48.66 99.37,52.68 98.28,58.24ZM91.92,58.8C92.31,56.77 90.94,55.24 88.88,55.42C86.82,55.6 84.78,57.43 84.38,59.46C83.99,61.49 85.36,63.02 87.42,62.84C89.48,62.66 91.52,60.83 91.92,58.8ZM49.04,56.39L64.46,55.04L61.77,68.73L77.01,67.39C78.17,69.12 79.89,71.57 85.63,71.07C87.78,70.88 89.02,70.42 90.45,69.86L88.35,80.55L58.94,83.12L49.51,131.16L34.09,132.51L43.52,84.47L14.11,87.04L16.94,72.65L46.35,70.08L49.04,56.39ZM13.06,132.79L3.59,122.25C7.96,118.4 16.39,110.89 21.72,92.28L35.63,92.8C29.51,115.9 20.5,125.89 13.06,132.79ZM63.42,90.37L78.4,87.24C76.7,106.22 82.11,112.78 84.89,116.09L70.53,128.2C65.84,121.58 61.57,113.27 63.42,90.37ZM144.02,77.94L134.94,124.21L118.17,125.68L125.14,90.18C120.25,93.12 109.04,99.48 94.22,104.95L89,92.04C103.72,87.1 117.87,79.18 131.41,70.36C143.15,62.65 151.32,55.16 163.1,44.07L175.09,52.56C170.63,56.86 161.29,65.84 144.02,77.94ZM214.68,57.35L203.57,72.21C195.23,66.69 186.07,63.06 177.69,60.84L187.18,47.08C198.5,49.56 207.55,53.28 214.68,57.35ZM172.39,120.59L170.36,104.45C205.54,98.51 226.18,84.98 243.31,47.98L256.48,54.04C232.68,104.38 200.11,114.08 172.39,120.59ZM280.61,35.26L297.65,33.77L293.61,54.35C306.51,57.3 321.58,62.66 332.61,68.9L320.99,85.89C313.88,80.78 299.84,73.33 290.4,70.68L282.39,111.49L265.35,112.97L280.61,35.26ZM335.24,107.99L327.34,96.62C352.51,85.56 360.26,72.56 364.14,49.65L380.46,48.22C379.7,51.68 379,54.77 377.72,59.05C389.88,52.78 394.99,44.7 396.78,41.85L337.25,47.06L340.18,32.13L419.53,25.19C412.33,47.95 401.3,60.11 384.38,70.45L376.79,62C367.88,90.29 347.2,102.26 335.24,107.99ZM438.11,63.4L424.41,67.64C424.45,62.95 424.2,54.81 421.71,45.48L434.64,41.14C437.08,47.96 437.82,55.88 438.11,63.4ZM459.48,58.24L446.28,62.17C446.35,51.49 445.52,45.83 444.26,40.12L457.01,36.67C459.71,44.94 459.56,54.67 459.48,58.24ZM425.89,100.49L420.84,88.96C452.33,78.91 462.58,69.33 475.99,35.18L490.61,37.46C481.94,57.83 469.31,87.15 425.89,100.49ZM503.21,20.82L559.7,15.88C558.06,25.13 562.27,29.71 571.91,28.61C561.69,63.18 536.83,82.97 501.62,92.65L497.06,78.64C540.4,69.3 550.1,45.01 554.51,31.52L500.18,36.27L503.21,20.82ZM583.18,14.78C582.07,20.43 576.5,25.43 570.77,25.93C565.12,26.43 561.36,22.24 562.47,16.59C563.58,10.94 569.14,5.94 574.79,5.44C580.54,4.85 584.29,9.13 583.18,14.78ZM576.9,15.33C577.34,13.12 575.91,11.42 573.58,11.63C571.33,11.82 569.09,13.84 568.65,16.05C568.2,18.34 569.74,19.95 571.98,19.75C574.31,19.55 576.45,17.62 576.9,15.33ZM613.39,9.01L629.71,7.58L618,56.43L605.72,57.51L613.39,9.01ZM603.27,63.71L618.33,62.39L615.41,77.23L600.35,78.55L603.27,63.71Z"
      android:fillColor="#E60012"/>
</vector>
```

2. 向右箭头 icon 图标 `ic_poc_chevron_right`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="113dp"
    android:height="78dp"
    android:viewportWidth="113"
    android:viewportHeight="78">
  <path
      android:pathData="M85.26,31.01L8.18,31.01C6.01,31.01 3.93,31.87 2.4,33.41C0.86,34.94 -0,37.01 -0,39.18C-0,41.35 0.86,43.42 2.4,44.96C3.93,46.49 6.01,47.35 8.18,47.35L84.88,47.35L68.51,63.92C66.98,65.47 66.12,67.57 66.12,69.75C66.12,71.93 66.98,74.03 68.51,75.58C70.04,77.12 72.12,77.99 74.29,78C76.46,78.01 78.54,77.16 80.08,75.64L110.61,45.19C111.36,44.43 111.97,43.53 112.38,42.54C112.79,41.55 113,40.49 113,39.42C113,38.35 112.79,37.29 112.38,36.3C111.97,35.31 111.36,34.41 110.61,33.65L79.28,2.39C78.13,1.25 76.68,0.47 75.09,0.16C73.5,-0.16 71.86,0 70.36,0.62C68.87,1.24 67.59,2.29 66.69,3.63C65.79,4.97 65.32,6.55 65.31,8.17C65.32,9.21 65.53,10.24 65.94,11.19C66.35,12.14 66.95,13 67.71,13.72L85.26,31.01Z"
      android:fillColor="#ffffff"/>
</vector>

```

3. 外层盒子 xml 布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- 省略中间代码 -->

    <View
        android:id="@+id/poc_magnification_change_mask"
        android:layout_width="match_parent"
        android:layout_height="465dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toEndOf="parent"
        android:background="#B2000000"
        android:visibility="visible"
        tools:visibility="visible"/>
    
    <include
        android:id="@+id/poc_include_magnification_change_content"
        layout="@layout/poc_include_magnification_change_content"
        android:layout_width="match_parent"
        android:layout_height="465dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toEndOf="parent"
        android:visibility="visible"
        tools:visibility="visible"/>
    
</androidx.constraintlayout.widget.ConstraintLayout>
```

4. 自定义 `ClippedContentView` 类，实现 `ConstraintLayout` 类，实现 `onDraw` 方法

```kotlin
package jp.retailai.raicart.ui.shopping

import android.content.Context
import android.graphics.Canvas
import android.util.AttributeSet
import android.view.View
import androidx.constraintlayout.widget.ConstraintLayout

// ClippedContentView 类定义，它是 ConstraintLayout 的一个子类。
class ClippedContentView @JvmOverloads constructor(
	// 上下文
	context: Context,
	// 属性集，可用于从 XML 布局文件中获取属性
	attrs: AttributeSet? = null,
	// 默认样式属性
	defStyleAttr: Int = 0
) : ConstraintLayout(context, attrs, defStyleAttr) {
	// clipRectLeft 变量，用于存储裁剪区域的左边界位置，默认值为 1280f
	private var clipRectLeft: Float = 1280f
	// clipRectRight 变量，用于存储裁剪区域的右边界位置，默认值为 1280f
	private var clipRectRight: Float = 1280f
	
	// setClipLeft 方法，用于设置裁剪区域的左右边界，并刷新视图
	fun setClipLeft(left: Float, right: Float) {
		// 更新左边界
		clipRectLeft = left
		// 更新右边界
		clipRectRight = right
		// 刷新视图，导致 onDraw 方法被调用
		invalidate()
	}
	
	// onDraw 方法，用于绘制视图内容
	override fun onDraw(canvas: Canvas) {
		// 设置画布的裁剪区域，只有在这个矩形区域内的内容才会被绘制
		canvas.clipRect(clipRectLeft, 0f, clipRectRight, 465f)
		// 调用父类的 onDraw 方法，进行默认的绘制处理
		super.onDraw(canvas)
	}
}
```

5. 倍率变化文字 `poc_include_magnification_change_content` xml 布局文件，注意此处需要给 `ClippedContentView` 控件一个背景：`android:background="#00FFFFFF"`，不然没有那种剪切的效果，导致控件会一直显示

```xml
<?xml version="1.0" encoding="utf-8"?>
<jp.retailai.raicart.ui.shopping.ClippedContentView
	xmlns:android="http://schemas.android.com/apk/res/android"
	xmlns:app="http://schemas.android.com/apk/res-auto"
	android:layout_width="match_parent"
	android:layout_height="465dp"
	android:gravity="center"
	android:background="#00FFFFFF"
	android:orientation="vertical">
<LinearLayout
	android:layout_width="match_parent"
	android:layout_height="465dp"
	android:gravity="center"
	android:orientation="vertical">
	
	<ImageView
		android:id="@+id/content_points_up"
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:layout_marginTop="@dimen/dp_25"
		android:src="@drawable/poc_icon_points_up"/>
	
	<androidx.constraintlayout.widget.ConstraintLayout
		android:layout_width="match_parent"
		android:layout_height="match_parent">
		
		<LinearLayout
			android:id="@+id/multiple_change_front"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
			app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toStartOf="parent"
			android:layout_marginStart="@dimen/dp_211"
			android:gravity="center"
			android:orientation="horizontal">
			
			<TextView
				android:id="@+id/multiple_change_front_number"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="1"
				android:textSize="240sp"
				android:textColor="@color/white"
				android:includeFontPadding="false"/>
			<TextView
				android:id="@+id/multiple_change_front_times"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="倍"
				android:textSize="120sp"
				android:textColor="@color/white"
				android:includeFontPadding="false"/>
		</LinearLayout>
		
		<ImageView
			android:id="@+id/multiple_change_chevron_right"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
			app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toStartOf="parent"
			android:layout_marginStart="535dp"
			android:src="@drawable/poc_icon_chevron_right"/>
		
		<LinearLayout
			android:id="@+id/multiple_change_later"
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			app:layout_constraintTop_toTopOf="parent"
			app:layout_constraintBottom_toBottomOf="parent"
			app:layout_constraintStart_toStartOf="parent"
			android:gravity="center"
			android:layout_marginStart="732dp">
			<TextView
				android:id="@+id/multiple_change_later_point"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="ポ\nイ\nン\nト"
				android:textSize="23sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
			<TextView
				android:id="@+id/multiple_change_later_number"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="2"
				android:textSize="120sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
			<TextView
				android:id="@+id/multiple_change_later_times"
				android:layout_width="wrap_content"
				android:layout_height="wrap_content"
				android:text="倍"
				android:textSize="60sp"
				android:textColor="#FFF200"
				android:includeFontPadding="false"/>
		</LinearLayout>
	</androidx.constraintlayout.widget.ConstraintLayout>

</LinearLayout>
</jp.retailai.raicart.ui.shopping.ClippedContentView>
```

6. kotlin 动画代码，省略上方代码，只保留了动画代码

```kotlin
// 创建动画集合
private val combinedAnimatorSet = AnimatorSet()


// 页面初始化时，设置积分倍数动画
setPointsMultiplierAnimation()
// 页面初始化时，设置字体
val fromAsset = Typeface.createFromAsset(requireContext().assets, "fonts/ShinGoPro-Heavy.otf")
multiple_change_front_number.typeface = fromAsset
multiple_change_front_times.typeface = fromAsset
multiple_change_later_point.typeface = fromAsset
multiple_change_later_number.typeface = fromAsset
multiple_change_later_times.typeface = fromAsset

// 在某个点击事件中，初始化属性并执行动画
var pocPointNum = multiple_change_front_number.text.toString().toInt() + 1
if (pocPointNum >= 6){
    pocPointNum = 1
}
initializeAndStartAnimation(pocPointNum.toString(), (pocPointNum + 1).toString())


// 私有函数 setPointsMultiplierAnimation，用于设置积分倍率变化的动画效果
private fun setPointsMultiplierAnimation(){
	// 积分变大蒙版弹窗进入动画，设置 DecelerateInterpolator 减速插值器，使动画在开始时变化较快，结束时变化较慢
	val animatePointsUpEnter = animatePointViewMove(poc_magnification_change_mask, 350, mapOf(
		0f to 1280f,
		0.619f to 16f,
		0.81f to 195f,
		1f to 0f
	), DecelerateInterpolator())
	// 积分倍率数字弹窗进入动画
	val animateScoreMultiplierEnter = animatePointViewMove(poc_include_magnification_change_content, 350, mapOf(
		0f to 80f,
		0.619f to 0f,
		0.81f to 20f,
		1f to 0f
	), DecelerateInterpolator())
	
	// 积分变大蒙版弹窗滑出动画
	val animatePointsUpExit = animatePointViewMove(poc_magnification_change_mask, 333, mapOf(
		0f to 0f,
		0.6f to -1190f,
		0.9f to -1080f,
		1f to -1280f
	), DecelerateInterpolator())
	
	// 积分倍率数字，前面的，右移
	val animateScoreMultiplierTextFrontMove = animatePointViewMove(multiple_change_front, 267, mapOf(
		0f to 0f,
		1f to 62f
	))
	// 积分倍率数字，后面的，左移
	val animateScoreMultiplierTextLaterMove = animatePointViewMove(multiple_change_later, 267, mapOf(
		0f to 0f,
		1f to -62f
	))
	
	// 滑入动画，同时播放；积分变大蒙版弹窗进入动画、积分倍率数字弹窗进入动画
	val animateUpEnter = AnimatorSet()
	animateUpEnter.playTogether(animatePointsUpEnter, animateScoreMultiplierEnter)
	// 为积分变大蒙版进入动画添加一个 AnimatorUpdateListener，用于更新 ClippedContentView 的剪裁位置
	animatePointsUpEnter.addUpdateListener { animation ->
		// 获取当前动画的值，这个值应该是遮罩视图的 translationX 属性值
		val animatedValue = animation.animatedValue as Float
		// 获取 ClippedContentView 的实例
		val clippedView = poc_include_magnification_change_content as? ClippedContentView
		// 更新 ClippedContentView 的剪裁位置
		clippedView?.setClipLeft(animatedValue, 1280f)
	}
	
	// 字号变化动画 + 箭头和后面的字移动动画，同时播放
	val animateFontSizeChange = AnimatorSet()
	// 设置动画开始前的延迟时间，单位为毫秒
	animateFontSizeChange.startDelay = 783
	animateFontSizeChange.playTogether(
		// 前面的字变小动画
		animateTextSizeChange(multiple_change_front_number, 240f, 120f),
		animateTextSizeChange(multiple_change_front_times, 120f, 60f),
		// 后面的字变大动画
		animateTextSizeChange(multiple_change_later_point, 23f, 46f),
		animateTextSizeChange(multiple_change_later_number, 120f, 240f),
		animateTextSizeChange(multiple_change_later_times, 60f, 120f),
		// 积分倍率数字，前面的，右移
		animateScoreMultiplierTextFrontMove,
		// 积分倍率数字，后面的，左移
		animateScoreMultiplierTextLaterMove
	)
	
	// 设置动画开始前的延迟时间，单位为毫秒
	animatePointsUpExit.startDelay = 2150
	// 为积分变大蒙版滑出动画添加一个 AnimatorUpdateListener，用于更新 ClippedContentView 的剪裁位置
	animatePointsUpExit.addUpdateListener { animation ->
		// 获取当前动画的值，这个值应该是遮罩视图的 translationX 属性值
		val animatedValue = animation.animatedValue as Float
		// 获取 ClippedContentView 的实例
		val clippedView = poc_include_magnification_change_content as? ClippedContentView
		// 更新 ClippedContentView 的剪裁位置
		clippedView?.setClipLeft(0f, 1280f + animatedValue)
	}
	
	// 动画集合，按顺序播放：进入动画、字号变化动画、滑出动画
	combinedAnimatorSet.playSequentially(animateUpEnter, animateFontSizeChange, animatePointsUpExit)
}

// 重置动画属性
private fun initializeAndStartAnimation(startPoints: String, endPoints: String) {
	// 停止动画集合
	combinedAnimatorSet.cancel()
	
	// 动画开始时，重置字号
	multiple_change_front_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 240f)
	multiple_change_front_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_point.setTextSize(TypedValue.COMPLEX_UNIT_SP, 23f)
	multiple_change_later_number.setTextSize(TypedValue.COMPLEX_UNIT_SP, 120f)
	multiple_change_later_times.setTextSize(TypedValue.COMPLEX_UNIT_SP, 60f)
	// 动画开始时，重置控件位置
	poc_magnification_change_mask.translationX = 1280f
	multiple_change_front.translationX = 0f
	multiple_change_later.translationX = 0f
	
	// 动画开始时，设置积分倍率数字
	multiple_change_front_number.text = startPoints
	multiple_change_later_number.text = endPoints
	
	// 启动动画集合
	combinedAnimatorSet.start()
}

// 控件移动动画
private fun animatePointViewMove(
	// 移动的视图对象
	view: View,
	// 动画持续时间，单位为毫秒
	duration: Long,
	// 关键帧和对应的位置
	keyframePositions: Map<Float, Float>,
	// 插值器，默认为加速减速插值器
	interpolator: TimeInterpolator = AccelerateDecelerateInterpolator()
): ObjectAnimator{
	// 创建一个关键帧的列表
	val keyframes = keyframePositions.map { (fraction, value) ->
		// 创建每个关键帧
		Keyframe.ofFloat(fraction, value)
	}
	
	// 使用 PropertyValuesHolder.ofKeyframe 方法创建 PropertyValuesHolder
	val translateProperty = PropertyValuesHolder.ofKeyframe(View.TRANSLATION_X, *keyframes.toTypedArray())
	
	// 创建位移动画对象；屏幕左上角为 0,0
	val translateAnimator = ObjectAnimator.ofPropertyValuesHolder(view, translateProperty)
	// 设置动画的插值器
	translateAnimator.interpolator = interpolator
	// 设置动画的持续时间
	translateAnimator.duration = duration
	
	return translateAnimator
}

// TextView 文字大小变化动画
private fun animateTextSizeChange(textView: TextView, vararg textSize: Float): ValueAnimator {
	// 创建文字大小变化的动画对象
	val frontMultipleAnimator = ValueAnimator.ofFloat(*textSize)
	// 设置动画持续时间，单位为毫秒
	frontMultipleAnimator.duration = 267
	// 添加动画更新监听器
	frontMultipleAnimator.addUpdateListener {
		// 在动画更新时设置 TextView 的文字大小
		textView.setTextSize(TypedValue.COMPLEX_UNIT_SP, it.animatedValue as Float)
	}
	
	return frontMultipleAnimator
}
```

7. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画11.gif)

8. 滑入和滑出部分慢放效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画12.gif)

### ④、SpringAnimation 弹簧动画库

> 1. 可设置位置、阻尼、刚度，不可设置时间；
> 2. 效果为围绕结束位置进行幅度逐渐变小的震荡

#### Ⅰ、简介

1. 平常，我们使用最多的应该是用 ObjectAnimatior 来构建我们需要的动画对象，然后通过不断变化的值给相应的属性赋值实现动画效果，这种效果是相对比较呆板的。想象一下，一个球自由落体到地上，它的真实情况时怎么样的？又或者是拽住弹簧的一段，然后拉拽弹簧后松手，效果是怎么样的？效果应该是加速度正反不断的变化，速度也不断变化，最终会回归到初始稳定状态。如果我们用 ObjectAnimatior 怎么实现？
2. 可能的话，我们的动画应该是基于真实的物理系统去实现的，以至于动画看起来更加的真实自然。举个例子，当物体变化的时候，它应该是保持有动力的，并且会要很平滑的过渡到下一个变化。
3. 弹性动画，可以说，弹性动画得以实现，主要是依赖于 `SpringForce`，`SpringForce` 有两个很重要的属性，一个是 `damping`(阻尼) 和 `stiffness`(刚度)，通过改变这两个属性的值，弹性动画可以有不同的表现。

#### Ⅱ、使用 SpringAnimation

1. 添加 dynamicanimation 依赖

```gradle
dependencies {
	  implementation 'androidx.dynamicanimation:dynamicanimation:1.0.0
}
```

3. 创建 SpringForce 实现弹性效果，参数 0f 表示动画结束时的值

```kotlin
// 创建 SpringForce 实现弹性效果，参数 0f 表示动画结束时的值
val springForce = SpringForce(0f)
// 设置弹性效果的阻尼比，数值越小，弹性效果越明显，即回弹幅度越大
springForce.dampingRatio = SpringForce.DAMPING_RATIO_HIGH_BOUNCY
// 设置弹性效果的刚度，数值越大，弹性效果越明显，即回弹越快
springForce.stiffness = SpringForce.STIFFNESS_HIGH
```

4. 构建一个 SpringAnimation 实例，并给其设置 SpringForce

```kotlin
// 创建动画对象，设置弹性效果
val iconAnimation = SpringAnimation(include_animator_test, DynamicAnimation.TRANSLATION_X).setSpring(springForce)
// 设置动画的初始值
iconAnimation!!.setStartValue(1280f)
```

5. 启动动画，有两种方式可以 start 动画：
	1. `iconAnimation.start()`：若是 iconAnimation 的 springForce 对象设置了 finalPosition 参数（SpringForce(0f) 中的 0f 即 finalPosition 参数），直接调用这个方法启动即可
	2. `iconAnimation.animateToFinalPosition(value)`：若是 iconAnimation 的 springForce 对象没设置 finalPosition 参数，调用这个方法传入该参数启动

#### Ⅲ、参数介绍

1. `finalPosition`：结束时的位置
2. `dampingRatio`：设置弹性效果的阻尼比，数值越小，弹性效果越明显，即回弹幅度越大
	1. 阻尼是指振动系统在振动中，由于外界作用或系统本身固有的原因引起的振动幅度逐渐下降的特性。
	2. 通过阻尼，我们可以定义我们的动画振动衰减的一个频率
	3. 取值效果和内置常量：

| 取值 | 取值效果         | 内置常量                  | 内置常量值 |
| ---- | ---------------- | ------------------------- | ---------- |
|>1|迅速回到平衡位置|DAMPING_RATIO_HIGH_BOUNCY|0.2|
| =1    | 在较短的时间内回到平衡位置 | DAMPING_RATIO_MEDIUM_BOUNCY | 0.5        |
|<1|多次来回振动然后回到平衡位置|DAMPING_RATIO_LOW_BOUNCY|0.75|
|0|永远振动，回不到最终位置|DAMPING_RATIO_NO_BOUNCY|1|

3. `stiffness`：设置弹性效果的刚度，数值越大，弹性效果越明显，即回弹越快
	1. 刚度是指材料或结构在受力时抵抗弹性变形的能力。
	2. 想象有一根比较软的弹簧和一根比较硬的弹簧，同时拉拽两个弹簧到相同长度，哪个更费力些，当然是那根比较硬的弹簧。
	3. 系统也为我们内置了四个常量：

| 内置常量           | 内置常量值 |
| ------------------ | ---------- |
| STIFFNESS_HIGH     | 10000f     |
| STIFFNESS_MEDIUM   | 1500f      |
| STIFFNESS_LOW      | 200f       |
| STIFFNESS_VERY_LOW | 50f        |

#### Ⅳ、取值效果

1. 阻尼：0.2，刚度：10000f

```kotlin
private var iconAnimation: SpringAnimation? = null

// 取消之前的动画
iconAnimation?.cancel()

// 创建 SpringForce 实现弹性效果，参数 0f 表示动画结束时的值
val springForce = SpringForce(0f)
// 设置弹性效果的阻尼比，数值越小，弹性效果越明显，即回弹幅度越大
springForce.dampingRatio = SpringForce.DAMPING_RATIO_HIGH_BOUNCY
// 设置弹性效果的刚度，数值越大，弹性效果越明显，即回弹越快
springForce.stiffness = SpringForce.STIFFNESS_HIGH

// 创建动画对象，设置弹性效果
iconAnimation = SpringAnimation(include_animator_test, DynamicAnimation.TRANSLATION_X).setSpring(springForce)
// 设置动画的初始值
iconAnimation!!.setStartValue(1280f)

// 启动动画
iconAnimation!!.start()
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F1、020-10000.gif)

2. 阻尼：0.75，刚度：200f

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F2、075-200.gif)

3. 阻尼：0.5，刚度：200f

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F3、050-200.gif)

### ⑤、Interpolator 插值器

> 在上面的 ② 中，有使用 DecelerateInterpolator() 插值器

#### Ⅰ、介绍

1. `Interpolator` 被用于定义动画的变化速率。也可以说是加速度。系统自带了一些插值器如下：

| 插值器                          | 效果                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------ |
| AccelerateDecelerateInterolator | 先加速后减速                                                                   |
| AccelerateInterpolator          | 加速                                                                           |
| DecelerateInterpolator          | 减速                                                                           |
| AnticipateInterpolator          | 先向相反方向改变一段再加速播放                                                 |
| AnticipateOvershootInterpolator | 先向相反方向改变，再加速播放，会超出目标值然后缓慢移动至目标值，类似于弹簧回弹 |
| BounceInterpolator              | 快到目标值时值会跳跃                                                           |
| CycleIinterpolator              | 动画循环一定次数，值的改变为一正弦函数：`Math.sin(2 * mCycles * Math.PIinput)`            |
| LinearInterpolator              | 线性均匀改变                                                                   |
| OvershottInterpolator           | 最后超出目标值然后缓慢改变到目标值                                             |
| TimeInterpolator                | 一个允许自定义Interpolator的接口，以上都实现了该接口                           |

2. 都是通过：`valueAnimator.setInterpolator(new LinearInterpolator());` 设置即可。
3. 当没有为动画设置插值器时，系统默认会帮你设置加减速插值器 `AccelerateDecelerateInterpolator`
4. 来看下使用了插值器的效果是什么样的，此效果是设置了 `BounceInterpolator` 的样子，在临近消失时有弹跳效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F动画1.gif)

5. 来看下 `BounceInterpolator` 的源码：

```kotlin
/**
 * An interpolator where the change bounces at the end.
 */
public class BounceInterpolator extends BaseInterpolator implements NativeInterpolatorFactory {
    public BounceInterpolator() {
    }

    @SuppressWarnings({"UnusedDeclaration"})
    public BounceInterpolator(Context context, AttributeSet attrs) {
    }

    private static float bounce(float t) {
        return t * t * 8.0f;
    }

    public float getInterpolation(float t) {
        t *= 1.1226f;
        if (t < 0.3535f) return bounce(t);
        else if (t < 0.7408f) return bounce(t - 0.54719f) + 0.7f;
        else if (t < 0.9644f) return bounce(t - 0.8526f) + 0.9f;
        else return bounce(t - 1.0435f) + 0.95f;
    }

    /** @hide */
    @Override
    public long createNativeInterpolator() {
        return NativeInterpolatorFactoryHelper.createBounceInterpolator();
    }
}
```

6. 代码不是很多，很多都是写在 `getInterpolation` 方法里了。其实我们只关注 `getInterpolation(float input)` 这个方法，`getInterpolation()` 方法接收一个 input 参数，input 参数是系统根据设置的动画持续时间计算出来的，取值范围是 `[0,1]`，从 0 匀速增加到1 。再来看下 `LinearInterpolator`（线性插值器） 的源码：

```kotlin
/**
 * An interpolator where the rate of change is constant
 */
public class LinearInterpolator extends BaseInterpolator implements NativeInterpolatorFactory {

    public LinearInterpolator() {
    }

    public LinearInterpolator(Context context, AttributeSet attrs) {
    }

    public float getInterpolation(float input) {
        return input;
    }

    /** @hide */
    @Override
    public long createNativeInterpolator() {
        return NativeInterpolatorFactoryHelper.createLinearInterpolator();
    }
}
```

7. `LinearInterpolator` 的 `getInterpolation (float input)` 方法是直接把 `input` 参数作为返回值返回了！
8. 由于 input 参数是从 0 匀速增加到 1 的，所以自然就是线性插值器了。所以上面的 `BounceInterpolator` 插值器就是直接操作的 `getInterpolation()` 返回 `input` 实现的弹跳效果。

#### Ⅱ、自定义实现插值器

1. 系统自带了一些插值器无法传入参数，所以大部分情况下无法高度还原样式
2. 要自定义插值器需要实现  接口
3. 例子如下，此处实现的是控件划入后震动一次，幅度为 20dp，总时间为 400ms，前200ms 平滑移动，后200ms 震动：

```kotlin
package jp.retailai.raicart.ui.shopping

import android.view.animation.Interpolator
import kotlin.math.sin

/**
 * @author 月海
 * @date 2024/1/11 15:05
 * @description
 */
class MyBounceInterpolator: Interpolator {
	override fun getInterpolation(time: Float): Float {
		val smoothDuration = 120f
		val bounceDuration = 280f
		
		return when {
			time < smoothDuration / 400f -> {
				// 在前 200ms 内线性移动
				time / (smoothDuration / 400f)
			}
			time < (smoothDuration + bounceDuration) / 400f -> {
				// 在后 200ms 内应用弹簧震动效果
				val normalizedTime = (time - smoothDuration / 400f) / (bounceDuration / 400f)
				1 - sin(normalizedTime * Math.PI).toFloat() * 0.02f // 调整震动幅度
			}
			else -> {
				// 动画结束后保持最终状态
				1f
			}
		}
	}
}
```

4. 如果想将震动幅度从原来的 0.05f 减小到 0.02f，只需在相应的代码行进行修改：

```kotlin
1 - sin(normalizedTime * Math.PI).toFloat() * 0.02f // 调整震动幅度
```

### ⑥、

### ⑦、

### ⑧、

## 4、图片资源

### ①、drawable 下快速生成 icon 图片 vector

1. drawable 右击 new -> vector asset

![|650](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230518092027.png)

2. 选择 icon AS 中没有时需要导入 svg 或者 psd

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230518092055.png)

3. drawable 会生成对应 name 的图标文件 （可以点击左侧 line 7 颜色后选择颜色）

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230518092125.png)

4. 在对应的控件中引入就可以了：`android:src="@drawable/ic_up"`

### ②、`shape` 图形中分别设置四个角的圆角矩形


```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/dark_blue" />
    <!-- 分别设置 左上角、右上角、右下角、左下角的圆角半径 -->
    <corners
        android:topLeftRadius="@dimen/dp_5"
        android:topRightRadius="@dimen/dp_5"
        android:bottomLeftRadius="@dimen/dp_10"
        android:bottomRightRadius="@dimen/dp_10" />
</shape>
```


### ③、`shape` 图形中多个图形的叠加

1. 使用 `layer-list` 包裹多个 `item` 即可

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- layer-list 中的 item 会按照顺序叠加 -->
<layer-list xmlns:android="http://schemas.android.com/apk/res/android" >
    <!-- 第一个 item 是蓝色背景，作为边框，width 和 height 是整个 shape 的宽高 -->
    <item
        android:width="@dimen/dp_140"
        android:height="@dimen/dp_70">
        <!-- shape 是一个矩形，solid 是填充色，corners 是圆角 -->
        <shape>
            <solid android:color="@color/dark_blue" />
            <corners
                android:topLeftRadius="@dimen/dp_5"
                android:topRightRadius="@dimen/dp_5"/>
        </shape>
    </item>
    <!-- 第一个 item 是白色背景，作为内容，gravity 是居中方式 -->
    <item
        android:width="@dimen/dp_136"
        android:height="@dimen/dp_68"
        android:gravity="center_horizontal|bottom">
        <shape>
            <solid android:color="@color/white" />
            <corners
                android:topLeftRadius="@dimen/dp_5"
                android:topRightRadius="@dimen/dp_5"/>
        </shape>
    </item>
</layer-list>
```

2. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231208141804.png)

### ④、svg 转安卓 xml 形状图片

1. 有一个 svg 文件：[咖啡师.svg](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F咖啡师.svg)，我将其保存在了 D 盘根目录
2. 在安卓项目中，右键 `res/drawable` 目录，选择新建 -> Vectro Asset

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222090652.png)

3. 在弹出来的 Asset Studio 弹窗中
	1. 选择 Asset type 的第二项，Local file (SVG, PSD)
	2. 选择 Path 后方的浏览按钮，在弹出的弹窗中选择 SVG 文件
	3. 在 Nane 输入框中修改名称
	4. 在 Size 输入框中修改尺寸

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222091415.png)

4. 修改完后，点击下一步，在新页面中点击完成

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222091439.png)

5. 此时 xml 形状图片就被添加进来了

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222091532.png)

### ⑤、figma 导出图片对应的安卓资源文件夹

1. `mipmap-mdpi`：1x 图片
2. `mipmap-hdpi`：1.5x 图片
3. `mipmap-xhdpi`：2x 图片
4. `mipmap-xxhdpi`：3x 图片
5. `mipmap-xxxhdpi`：4x 图片

### ⑥、Camera1 API 与 YUV420、NV21

#### Ⅰ、YUV420 和 NV21 的说明

##### （1）、YUV420

1. YUV420 是一种颜色编码系统，广泛用于视频和图像处理。在 YUV420 格式中，图像被分为三个分量：Y（亮度），U 和 V（色度）。Y 分量代表图像的明暗信息，而 U 和 V 分量代表颜色信息
2. YUV420 的一个特点是色度分量的采样率是亮度的一半，这意味着对于每四个 Y 分量，只有一个 U 和一个 V 分量。这种格式有多种子类型，常见的包括 YUV420p（平面式）和 YUV420sp（半平面式，如 NV12 和 NV21）

##### （2）、NV21

1. NV21 是 YUV420sp（半平面）格式的一种，其中 Y 分量后跟交错的 V 和 U 分量。具体来说，所有的 Y 分量先连续存储，然后是所有的 VU 分量交错存储（首先是 V，然后是 U）。这种格式在 Android 设备上非常常见，因为它易于使用并可通过硬件加速进行处理

#### Ⅱ、Camera API 的说明

##### （1）、Camera1

1. Camera1 API，也称为原始的 Android 相机 API，是 Android 早期版本中用于相机应用开发的接口。这个 API 自 Android 1.0 起就存在，一直到 Android 5.0（Lollipop）推出 Camera2 API 后，Camera1 API 逐渐被视为过时。尽管 Camera1 API 已经不是开发新应用的首选，但它的简单性和广泛的兼容性使其在一些旧设备和简单应用中依然被使用
2. **支持的图像格式**：Camera1 API 主要支持 JPEG 和一些 YUV 格式，包括 NV21。NV21 由于其简单的内存布局和易于处理的特性，在 Camera1 API 中是默认的预览格式
3. **局限性**：Camera1 API 的主要局限性在于其对现代相机硬件功能的有限支持。例如，对高动态范围（HDR）拍摄、原始图像捕捉（RAW）等先进功能的支持非常有限
4. **过渡到 Camera2 和 CameraX**：鉴于 Camera1 的局限性，Google 推出了 Camera2 API，该 API 提供了对相机硬件更详细的控制，并支持更高级的图像处理功能。随后，为了简化 Camera2 的复杂性并改善开发者体验，Google 又引入了 CameraX 库，该库在保持 Camera2 强大功能的同时，简化了 API 的使用
5. 总的来说，Camera1 API 主要支持 JPEG 和 NV21 格式，尤其是在处理视频预览和简单图像捕获时。对于现代 Android 开发，推荐使用 CameraX 或至少是 Camera2 API，因为这些新 API 提供了更多的功能和更好的设备兼容性。如果需要在旧设备上维护或更新应用，仍然可能需要了解和使用Camera1 API

##### （2）、Camera2

1. Camera2 API 是 Android 5.0（Lollipop）引入的一套先进的相机控制 API，旨在提供比旧的 Camera1 API 更强大和灵活的相机操作功能。amera2 API 在设计上更加模块化和抽象，提供了对相机硬件的细粒度控制，包括每一帧的控制、详细的图像处理和更复杂的图像捕捉流程
2. **主要特性**：
	1. **控制和图像数据访问**：
		1. Camera2 允许应用程序对焦点、曝光、白平衡等进行精细控制。开发者可以手动设置这些参数，或者利用自动模式
		2. 提供对帧率、格式、分辨率等的详细控制，支持高速视频录制和高分辨率照片拍摄
	2. **会话和请求**：
		1. Camera2 API 使用会话（CameraCaptureSession）和请求（CaptureRequest）的概念来处理图像捕捉。每个请求可以细致地配置相机设置，而会话则管理一系列这样的请求
		2. 通过这种方式，Camera2 支持高级功能，如连拍（Burst capture）和YUV图像捕捉后的JPEG编码
	3. **管道和回调**：
		1. Camera2 API 构建在一个复杂的管道模型上，这个模型允许多个请求在相机管道中同时进行，提高了相机操作的效率和速度
		2. API 提供了强大的回调机制，如 CameraCaptureSession.CaptureCallback 和 CameraDevice.StateCallback，让开发者可以精确地知道相机状态和每个请求的处理情况
	4. **Android硬件抽象层（HAL）**：
		1. Camera2 的实现依赖于 Android 硬件抽象层（HAL），允许厂商根据硬件能力实现不同级别的功能支持
		2. 根据设备的能力，Camera2 API 分为三个级别：Legacy、Limited 和 Full。Full 级别提供了最全面的控制，Legacy 级别的设备则主要通过Camera1 API实现的功能来模拟Camera2的操作
	5. **支持的格式和帧控制**：
		1. Camera2 支持多种图像格式，包括 JPEG、DNG（RAW）、YUV_420_888 等，满足不同的图像处理需求
		2. 允许对捕获的每一帧进行细粒度的时间控制，支持创建复杂的图像捕捉序列和高动态范围（HDR）图像处理
3. **开发中的挑战**：
	1. API 复杂性：Camera2 提供了非常强大的功能，但相应的，它的 API 也相对复杂，学习曲线陡峭，尤其是对于初学者或只需简单相机功能的开发者
	2. 设备兼容性：虽然 Camera2 API 旨在统一相机访问接口，但不同设备制造商的实现可能有差异，这可能导致在不同设备上出现功能差异或兼容性问题
4. **CameraX 作为解决方案**：为了解决 Camera2 API 的复杂性和兼容性问题，Google 推出了 CameraX 库，它在保持 Camera2 强大功能的基础上，提供了更简单的 API 和更好的跨设备兼容性。CameraX 自动处理设备间的差异，并简化了相机应用的开发流程，使开发者能够更容易地实现高质量的相机功能
5. 总的来说，Camera2 API 是一套功能强大但使用复杂的相机控制接口，适合需要高度相机控制和复杂图像处理的应用。对于大多数开发者而言，使用 CameraX 可能是一个更简便且稳妥的选择

##### （3）、CameraX

1. CameraX 是 Android Jetpack 的一部分，它是一个简化相机应用开发的库，旨在克服 Camera2 API 使用中的复杂性和设备兼容性问题。CameraX 通过提供简洁的 API 和自动化的多数硬件级别的处理，帮助开发者更容易地实现高质量的相机功能，而不需要针对各种设备进行大量的测试和调整。
2. **CameraX 的主要特点**：
	1. **简化的 API**：
		1. CameraX 提供了一组简单的 API，允许开发者使用少量的代码实现常见的相机操作，如预览、拍照和图像分析。
		2. 这些API设计成与生命周期感知组件兼容，自动处理相机的打开和关闭，减少了开发者在管理相机生命周期时的工作量。
	2. **使用用例（Use Cases）架构**：
		1. CameraX 定义了几个基本的“用例”，包括 Preview、ImageCapture 和 ImageAnalysis。每个用例都对应一种常见的相机功能，开发者可以根据需要选择并配置这些用例。
		2. Preview（预览）：配置相机预览流到界面元素。
		3. ImageCapture（图像捕获）：用于捕获高质量的照片。
		4. ImageAnalysis（图像分析）：提供一种连续获取相机帧数据的方法，用于实时图像处理或机器学习。
	3. **兼容性和测试**：
		1. CameraX 通过内置的设备兼容性层，自动适配不同制造商的相机实现，确保在多种设备上表现一致。
		2. Google 提供了广泛的设备和系统版本的测试，保证了 CameraX 的稳定性和可靠性。
	4. **扩展性和灵活性**：
		1. 虽然 CameraX 旨在简化相机应用的开发，但它也提供了足够的扩展点和配置选项，以满足更高级的摄影需求。
		2. 开发者可以通过自定义配置来调整焦距、曝光、ISO 等参数，或使用附加的 CameraX Extensions 来增强功能，例如夜景模式、HDR 等。
	5. **与生命周期集成**：
		1. CameraX 使用 Android 生命周期，自动管理相机的打开和关闭，减少了内存泄漏和崩溃的风险。
		2. 这意味着当用户界面不可见时，CameraX 会自动释放相机资源，当用户界面重新可见时，再自动重新连接相机。
3. **开发示例**：
	1. 使用 CameraX 的开发流程通常包括以下几个步骤：
	2. 配置 Gradle：在项目的 build.gradle 文件中添加 CameraX 依赖。
	3. 设置相机的权限：在 AndroidManifest.xml 中请求必要的相机权限。
	4. 初始化和配置用例：创建和配置 Preview、ImageCapture 和/或 ImageAnalysis 用例。
	5. 绑定生命周期：将用例绑定到一个 LifecycleOwner，通常是一个 Activity 或 Fragment。
	6. 实现功能：根据需要实现拍照、预览显示或图像分析的逻辑。
4. 总结：CameraX 是面向所有 Android 开发者的相机库，它提供了一种高效、易用且可靠的方式来实现相机相关功能。通过简化应用的开发和测试工作，CameraX 让开发者可以集中精力于创造独特的用户体验和功能，而不必担心不同设备间的兼容性问题。

#### Ⅲ、将 YUV420 数据转为 NV21 数据


```kotlin
fun yuv420ToNv21(image: ImageProxy): ByteArray{
    val crop: Rect = image.getCropRect()
    val format: Int = image.getFormat()
    val width = crop.width()
    val height = crop.height()
    val planes: Array<ImageProxy.PlaneProxy> = image.getPlanes()
    val data = ByteArray(width * height * ImageFormat.getBitsPerPixel(format) / 8)
    val rowData = ByteArray(planes[0].getRowStride())
    var channelOffset = 0
    var outputStride = 1
    for (i in planes.indices) {
        when (i) {
            0 -> {
                channelOffset = 0
                outputStride = 1
            }
            1 -> {
                channelOffset = width * height + 1
                outputStride = 2
            }
            2 -> {
                channelOffset = width * height
                outputStride = 2
            }
        }
        val buffer: ByteBuffer = planes[i].getBuffer()
        val rowStride: Int = planes[i].getRowStride()
        val pixelStride: Int = planes[i].getPixelStride()
        val shift = if (i == 0) 0 else 1
        val w = width shr shift
        val h = height shr shift
        buffer.position(rowStride * (crop.top shr shift) + pixelStride * (crop.left shr shift))
        for (row in 0 until h) {
            var length: Int
            if (pixelStride == 1 && outputStride == 1) {
                length = w
                buffer[data, channelOffset, length]
                channelOffset += length
            } else {
                length = (w - 1) * pixelStride + 1
                buffer[rowData, 0, length]
                for (col in 0 until w) {
                    data[channelOffset] = rowData[col * pixelStride]
                    channelOffset += outputStride
                }
            }
            if (row < h - 1) {
                buffer.position(buffer.position() + rowStride - length)
            }
        }
    }
    return data
}
```

### ⑦、

### ⑧、

## 5、数据

### ①、使用 `Bundle()` 传递自定义对象

1. 自定义对象 `Contact` 联系人实体类

```kotlin
package com.yuehai.y_chat.bean.contact

import android.os.Parcel
import android.os.Parcelable

/**
 * @author 月海
 * @date 2023/10/8 9:34
 * @description 联系人实体类
 */
data class Contact(
	/**
	 * 联系人 id
	 */
	var contactId: String,
	
	/**
	 * 联系人昵称
	 */
	var contactNickName: String? = "联系人昵称"
) : Parcelable {
	
	/**
	 * 构造函数，用于从Parcel中读取数据以还原对象
	 * @param parcel 包含对象数据的 Parcel
	 */
	constructor(parcel: Parcel) : this(
		parcel.readString() ?: "",
		parcel.readString() ?: ""
	)
	
	/**
	 * 将对象数据写入 Parcel，以便进行序列化
	 * @param parcel 用于写入数据的 Parcel
	 * @param flags 附加标志（通常为0）
	 */
	override fun writeToParcel(parcel: Parcel, flags: Int) {
		parcel.writeString(contactId)
		parcel.writeString(contactNickName)
	}
	
	/**
	 * 描述对象内容的特殊标志，通常为 0
	 */
	override fun describeContents(): Int {
		return 0
	}
	
	companion object CREATOR : Parcelable.Creator<Contact> {
		/**
		 * 从 Parcel 创建对象的静态方法
		 * @param parcel 包含对象数据的 Parcel
		 * @return 从 Parcel 中创建的 Contact 对象
		 */
		override fun createFromParcel(parcel: Parcel): Contact {
			return Contact(parcel)
		}
		
		/**
		 * 创建指定大小的 Contact 对象数组
		 * @param size 数组大小
		 * @return Contact 对象数组
		 */
		override fun newArray(size: Int): Array<Contact?> {
			return arrayOfNulls(size)
		}
	}
}
```

2. 自定义对象 `MessagesReceive` 接收消息实体类，用于接收服务端发送的消息

```kotlin
package com.yuehai.y_chat.bean.message

import android.os.Parcel
import android.os.Parcelable

/**
 * @author 月海
 * @date 2023/12/25 16:50
 * @description 接收消息实体类，用于接收服务端发送的消息
 */
data class MessagesReceive (
	
	/**
	 * 发送者 id
	 */
	val senderId: String,
	
	/**
	 * 接收者 id
	 */
	val receiverId: String,
	
	/**
	 * 发送时间
	 */
	val sendTime: String,
	
	/**
	 * 消息内容
	 */
	val messageData: String,
	
	/**
	 * 消息类型
	 */
	val messageType: String,
	
	/**
	 * 消息是否成功发送
	 */
	val success: Boolean,
	
	/**
	 * 接收者是否在线
	 */
	val online: Boolean,
	
	/**
	 * 消息发送失败的原因
	 */
	val errorReason: String,
	
	/**
	 * 是否是回执消息
	 */
	val isReceipt: Boolean,
) : Parcelable {
	/**
	 * 构造函数，用于从Parcel中读取数据以还原对象
	 * @param parcel 包含对象数据的 Parcel
	 */
	constructor(parcel: Parcel) : this(
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readByte() != 0.toByte(),
		parcel.readByte() != 0.toByte(),
		parcel.readString() ?: "",
		parcel.readByte() != 0.toByte()
	)
	
	/**
	 * 将对象数据写入 Parcel，以便进行序列化
	 * @param parcel 用于写入数据的 Parcel
	 * @param flags 附加标志（通常为0）
	 */
	override fun writeToParcel(parcel: Parcel, flags: Int) {
		parcel.writeString(senderId)
		parcel.writeString(receiverId)
		parcel.writeString(sendTime)
		parcel.writeString(messageData)
		parcel.writeString(messageType)
		parcel.writeByte(if (success) 1 else 0)
		parcel.writeByte(if (online) 1 else 0)
		parcel.writeString(errorReason)
		parcel.writeByte(if (isReceipt) 1 else 0)
	}
	
	/**
	 * 描述对象内容的特殊标志，通常为 0
	 */
	override fun describeContents(): Int {
		return 0
	}
	
	companion object CREATOR : Parcelable.Creator<MessagesReceive> {
		/**
		 * 从 Parcel 创建对象的静态方法
		 * @param parcel 包含对象数据的 Parcel
		 * @return 从 Parcel 中创建的 MessagesReceive 对象
		 */
		override fun createFromParcel(parcel: Parcel): MessagesReceive {
			return MessagesReceive(parcel)
		}
		
		/**
		 * 创建指定大小的 MessagesReceive 对象数组
		 * @param size 数组大小
		 * @return MessagesReceive 对象数组
		 */
		override fun newArray(size: Int): Array<MessagesReceive?> {
			return arrayOfNulls(size)
		}
	}
}
```

3. 自定义对象 `MessageList` 消息列表项实体类

```kotlin
package com.yuehai.y_chat.bean.message

import android.os.Parcel
import android.os.Parcelable
import com.yuehai.y_chat.bean.contact.Contact

/**
 * @author 月海
 * @date 2023/9/26 9:12
 * @description 消息列表项实体类，实现 Parcelable 接口，使这个类可以被 Bundle 传递
 */
data class MessageList(
	/**
	 * 联系人信息
	 */
	var contact: Contact,
	/**
	 * 消息内容，包含发送者信息
	 */
	var messagesReceiveList: MutableList<MessagesReceive>,
	
): Parcelable {
	/**
	 * 构造函数，用于从Parcel中读取数据以还原对象
	 * @param parcel 包含对象数据的 Parcel
	 */
	@Suppress("DEPRECATION")
	constructor(parcel: Parcel) : this(
		parcel.readParcelable(Contact::class.java.classLoader) ?: Contact("", ""),
		mutableListOf<MessagesReceive>().apply {
			parcel.readArrayList(MessagesReceive::class.java.classLoader)
		}
	)
	
	/**
	 * 将对象数据写入 Parcel，以便进行序列化
	 * @param parcel 用于写入数据的 Parcel
	 * @param flags 附加标志（通常为0）
	 */
	override fun writeToParcel(parcel: Parcel, flags: Int) {
		parcel.writeParcelable(contact, flags)
		parcel.writeList(messagesReceiveList)
	}
	
	/**
	 * 描述对象内容的特殊标志，通常为 0
	 */
	override fun describeContents(): Int {
		return 0
	}
	
	companion object CREATOR : Parcelable.Creator<MessageList> {
		/**
		 * 从 Parcel 创建对象的静态方法
		 * @param parcel 包含对象数据的 Parcel
		 * @return 从 Parcel 中创建的 MessageList 对象
		 */
		override fun createFromParcel(parcel: Parcel): MessageList {
			return MessageList(parcel)
		}
		
		/**
		 * 创建指定大小的 MessageList 对象数组
		 * @param size 数组大小
		 * @return MessageList 对象数组
		 */
		override fun newArray(size: Int): Array<MessageList?> {
			return arrayOfNulls(size)
		}
	}
}
```

4. 发送消息：

```kotlin
// 创建 Bundle 对象并添加数据
val bundle = Bundle()
bundle.putParcelable("messagesReceiveList", messageListData.value!![position])
findNavController.navigate(R.id.action_chat_home_to_message_details, bundle)
```

5. 接收消息

```kotlin
val messagesReceiveList = arguments?.getParcelable<MessageList>("messagesReceiveList")
```

6. 1

### ②、

### ③、

### ④、

### ⑤、

## 6、网络请求

### ①、使用 logging-interceptor 追踪网络请求

1. 引入依赖

```gradle
implementation 'com.squareup.okhttp3:logging-interceptor:4.9.1'
```

2. 创建 Retrofit 实例时添加拦截器

```kotlin
package com.yuehai.chat.network.config

import com.yuehai.chat.network.config.GsonFactory.createGson
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

/**
 * Retrofit 客户端，用于创建 Retrofit 实例
 * @author 月海
 * @date 2024/4/29 16:52
 * @description Retrofit 客户端，用于创建 Retrofit 实例
 */
object RetrofitClient {
    
    /**
     * 通过传入的 URL 创建 Retrofit 实例
     * @param baseUrl 基础 URL
     * @param apiClass Api 接口类
     * @return Api 接口类的实例
     */
    fun <T> create(baseUrl: String, apiClass: Class<T>): T {
        // 创建日志拦截器实例，并设置日志级别
        val logging = HttpLoggingInterceptor().apply {
            level = HttpLoggingInterceptor.Level.BODY
        }

        // 创建 OkHttpClient 实例，并添加拦截器
        val client = OkHttpClient.Builder()
            .addInterceptor(logging)
            .build()

        // Retrofit.Builder() 用于创建 Retrofit 实例
        val retrofit = Retrofit.Builder()
            // 设置 URL
            .baseUrl(baseUrl)
            // 设置 OkHttpClient 实例，用于网络请求
            .client(client)
            // 添加 Gson 转换器
            .addConverterFactory(GsonConverterFactory.create(createGson()))
            // 创建 Retrofit 实例
            .build()
        
        // 创建并返回 Api 接口类的实例
        return retrofit.create(apiClass)
    }
    
}
```

3. 调用接口时使用上面的 `RetrofitClient` 调用即可

```kotlin
/**
 * 授权接口服务，用于处理授权相关的网络请求
 * @author 月海
 * @date 2024/4/29 16:35
 * @description 封装 AuthApi 的调用，确保所有网络请求在 IO 线程中执行
 */
object AuthApiService {
    
    /**
     * 使用 USER URL 创建的 AuthApi 实例
     */
    private val authApi = RetrofitClient.create(BaseApiServiceUrl.USER.url, AuthApi::class.java)
    
    /**
     * 用户注册，接收具体的用户信息，构造请求数据后调用 AuthApi 的注册接口，并返回响应对象
     * @param nickName 用户昵称
     * @param password 用户密码
     * @param email 用户邮箱
     * @param phoneNumber 用户手机号
     * @return 响应对象：用户 ID
     * <p></p>
     * withContext(Dispatchers.IO)：withContext 函数用于切换协程的上下文，将协程的执行环境切换到 IO 线程中
     * Dispatchers.IO 是一个预定义的调度器，专门用于执行 I/O 密集型任务，如文件操作、网络调用等。
     */
    suspend fun submitRegisterRequest(nickName: String, password: String, email: String, phoneNumber: String): Response<JsonResult<Int>> = withContext(Dispatchers.IO) {
        /**
         * 构造注册请求数据
         */
        val registrationData = mapOf(
            "nickName" to nickName,
            "password" to password,
            "email" to email,
            "phoneNumber" to phoneNumber
        )
        
        try {
            // 调用 AuthApi 的注册接口
            authApi.register(createGsonRequestBody(registrationData))
        } catch (e: Exception) {
            // 打印并处理异常
            e.printStackTrace()
            handleError(e, "发送注册请求失败")
        }
    }
}
```

### ②、

### ③、

### ④、

### ⑤、

## 7、控件

### ①、其他

#### Ⅰ、布局时使用负数参数

1. 可使用 `translationX` 和 `translationY` 来设置控件的位置
2. `translationX`：水平偏移
3. `translationY`：垂直偏移
4. 例子：

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/category_position_dialog"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/red_footer"
    android:orientation="vertical">
    
    <androidx.appcompat.widget.AppCompatImageView
            android:id="@+id/closeButton"
            android:layout_width="@dimen/dp_60"
            android:layout_height="@dimen/dp_60"
            android:src="@drawable/ic_close_button"
            android:translationX="@dimen/dp_m_30"
            android:translationY="@dimen/dp_30"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintEnd_toEndOf="parent"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```

![|668](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231026102417.png)

#### Ⅱ、在代码中动态修改控件的宽高

1. android 的 view 中有 `setPadding`，但是没有直接的 `setMargin` 方法，如果要在代码中设置 `Margin` 可以通过设置 view 里面的 `LayoutParams` 设置
2. 而这个 `LayoutParams` 是根据该 view 在不同的 `GroupView` 而不同的，具体取决于父布局的类型和需要修改的具体布局参数。
3. 如果父布局是 `ConstraintLayout`，并且需要修改的布局参数是 `ConstraintLayout.LayoutParams` 中定义的特定属性（例如 `topMargin`），那么可以使用 `fragmentContainerView.layoutParams as ConstraintLayout.LayoutParams`
4. 如果父布局是任何类型的 `ViewGroup` （`LinearLayout`、`RelativeLayout`、`FrameLayout` 和 `ConstraintLayout` 都属于 `ViewGroup`），并且只需要修改通用的布局参数（例如 `topMargin`、`leftMargin` 等），那么可以使用 `fragmentContainerView.layoutParams as ViewGroup.MarginLayoutParams`。
5. `MarginLayoutParams` 是 `ViewGroup` 的一个子类，它包含了常用的边距属性。
6. 所以，选择使用哪种写法取决于具体情况和需求。如果需要修改特定布局类型的特定属性，选择对应的布局参数类型；如果只需要修改通用属性，选择通用的 `MarginLayoutParams`
7. 使用流程
	1. 获取所要修改 `Margin` 的 view 对象的 `LayoutParams` 对象
	2. 给 `LayoutParams` 对象的 `topMargin`（或其他属性）属性赋值
	3. 将 `LayoutParams` 对象赋值给所要修改 `Margin` 的 view 对象的 `layoutParams` 属性
8. 代码示例，布局：

```dart

```

9. 代码示例，动态修改：
10. 1
11. 1
12. 1
13. 1

#### Ⅲ、

### ②、TextView 文本

#### Ⅰ、`TextView` 行间距设置

1. 可以使用 `android:lineSpacingExtra` 属性来设置行间距的额外空间；在下面的示例中，使用 `android:lineSpacingExtra` 属性来设置行间距的额外空间为 `8dp`。这样就会在每一行的底部增加 `8dp` 的额外空间，从而实现行间距的效果。也可以设置为负数

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello, World!"
    android:lineSpacingExtra="8dp" />
```

2. 也可以使用 `android:lineSpacingMultiplier` 属性来设置行间距的倍数。这个属性的值是一个浮点数，表示行间距相对于默认行间距的倍数；在下面的示例中，使用 `android:lineSpacingMultiplier` 属性将行间距设置为默认行间距的 `1.5` 倍。

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello, World!"
    android:lineSpacingMultiplier="1.5" />
```

#### Ⅱ、指定 `TextView` 行数

1. 可使用 `android:lines` 属性来设置占用行数，会占用指定的空间，超出的部分不再显示
2. 可使用 `android:maxLines` 属性来设置最大显示行数，超出的部分不再显示

```xml
<TextView
		android:layout_width="wrap_content"
		android:layout_height="wrap_content"
		android:text="testtesttesttesttesttesttesttest"
		android:textSize="20sp"
		android:lines="2"
		android:ellipsize="end"/>
```

2. `android:ellipsize="end"` 表示若内容超出，则在内容末尾 `end` 添加省略号（`...`）

#### Ⅲ、清除 `TextView` 字体周边空白

1. 在设置界面布局的时候，设计师会给一张标注了尺寸的 UI 设计图，如果在 UI 中包含了 `TextView` 空间的话，会发现即使完全按照标注的尺寸来做，最终的显示效果和设计图还是有差异。
2. 打开开发者模式中的布局边界，再观察 APP 的界面可以发现，在 `TextView` 中字体与 `TextView` 的边界是有一定的距离的，在 720px 的图中大概有 2px 的边界留白。就是这些默认的留白导致 UI 出现偏差。
3. 在 `TextView` 提供的属性设置里面，有这样一条属性：`android:includeFontPadding`，用来设置文本框是否包含顶部和底部留白（左右两侧默认没有留白），将其设置为 false，TextView 就会取消 2px 的留白。这样就避免了 TextView 导 UI 出现差异

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="25"
    android:textSize="46sp"
    android:textColor="@color/dark_blue"
    android:textStyle="bold"
    android:includeFontPadding="false"/>
```

#### Ⅳ、

#### Ⅴ、

### ③、recyclerView 列表

#### Ⅰ、`recyclerView` 滚动到指定位置时的动画

- `LinearLayoutManager` 是用于在 RecyclerView 中管理线性布局的布局管理器。它本身并没有提供滚动动画的功能。但可以通过结合使用 `RecyclerView` 的 `smoothScrollToPosition()` 方法和 `RecyclerView.ItemAnimator` 来实现滚动时的动画效果。

1. 首先，确保已经为 RecyclerView 设置了自定义的 ItemAnimator。例如：

```java
val recyclerView: RecyclerView = findViewById(R.id.recyclerView)
/**
 * RecyclerView.ItemAnimator 是用于处理 RecyclerView 中项目插入、移除、更改等操作时的动画效果的接口。
 * 它允许定义项目变化时的动画效果，例如淡入淡出、平移、缩放等。
 *
 * DefaultItemAnimator 是 Android 提供的默认 RecyclerView.ItemAnimator 实现之一。
 * DefaultItemAnimator 是 RecyclerView.ItemAnimator 接口的默认实现。它提供了一些默认的动画效果，例如渐变淡入淡出、默认的滑动动画等。
 * 当将 DefaultItemAnimator 分配给 RecyclerView 的 setItemAnimator() 方法时，它将处理 RecyclerView 中项目变化的动画效果。
 */
recyclerView.itemAnimator = DefaultItemAnimator()
```

2. 然后，可以使用 `smoothScrollToPosition()` 方法滚动到指定位置，并触发 ItemAnimator 中的动画效果。例如：

```java
var layoutManager = recyclerView.layoutManager as LinearLayoutManager
/**
 * 参数 1：RecyclerView：指定要进行滚动操作的 RecyclerView 实例。
 * 参数 2：RecyclerView.State：提供有关 RecyclerView 的状态信息，如焦点位置等。在大多数情况下，可以传递 null，以使用默认的状态。
 * 参数 3：int position：指定要滚动到的目标位置。
 */
layoutManager.smoothScrollToPosition(recyclerView, null, 0)
```

3. 这将滚动到列表中的第一个位置，并触发 ItemAnimator 中的动画效果（如果有定义的话）。
4. 注意，要使上述代码正常工作，确保在调用 `smoothScrollToPosition()` 方法之前已经设置了适当的布局管理器（例如 `LinearLayoutManager`）和适配器（例如 `RecyclerView.Adapter`）。
5. 另外，请注意，根据定制的需求，可能需要自定义 `ItemAnimator` 的实现，或者使用第三方库来实现更复杂的动画效果。

#### Ⅱ、添加分割线

##### （1）、添加默认分割线

```kotlin
//添加Android自带的分割线
recyclerView.addItemDecoration(DividerItemDecoration(this, DividerItemDecoration.VERTICAL));
```

##### （2）、添加自定义分割线

1. 创建 `Drawable` 形状图片

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">

    <gradient
        android:centerColor="#ff00ff00" //绿色
        android:endColor="#ff0000ff"    //蓝色
        android:startColor="#ffff0000"  //红色
        android:type="linear" />
    <size android:height="3dp" />

</shape>
```

2. 创建 `DividerItemDecoration` 对象，引用 `Drawable` 形状图片，并设置给 `RecyclerView`

```kotlin
// 定义适配器
private val couponAndItemAdapter by lazy { CouponAndItemAdapter() }
// 获取 RecyclerView 对象
val recyclerViewCouponAndItem = include_new_coupons.coupon_and_item

// 设置 布局管理器
recyclerViewCouponAndItem.layoutManager = LinearLayoutManager(context, LinearLayoutManager.HORIZONTAL, false)

// 创建 DividerItemDecoration 对象
val divider = DividerItemDecoration(context, DividerItemDecoration.HORIZONTAL)
// 引用 Drawable 形状图片
divider.setDrawable(ContextCompat.getDrawable(requireContext(), R.drawable.bg_button_blue_radius_5)!!)
// 设置给 RecyclerView
recyclerViewCouponAndItem.addItemDecoration(divider)

// 设置适配器
recyclerViewCouponAndItem.adapter = couponAndItemAdapter
```

#### Ⅲ、使用 DiffUtil 高效刷新 recyclerView 列表

1. 使实体类实现 `equals` 和 `hashCode` 方法，用于比较对象是否相同

```kotlin
package com.yuehai.y_chat.bean.contact

/**
 * @author 月海
 * @date 2023/10/8 9:34
 * @description 联系人实体类
 */
data class Contact(
	/**
	 * 联系人 id
	 */
	var contactId: String,
	
	/**
	 * 联系人昵称
	 */
	var contactNickName: String? = "联系人昵称"
) {
	override fun equals(other: Any?): Boolean {
		if (this === other) return true
		if (javaClass != other?.javaClass) return false
		
		other as Contact
		
		if (contactId != other.contactId) return false
		if (contactNickName != other.contactNickName) return false
		
		return true
	}
	
	override fun hashCode(): Int {
		var result = contactId.hashCode()
		result = 31 * result + (contactNickName?.hashCode() ?: 0)
		return result
	}
}
```

```kotlin
package com.yuehai.y_chat.bean.message

import android.os.Parcel
import android.os.Parcelable

/**
 * @author 月海
 * @date 2023/12/25 16:50
 * @description 接收消息实体类，用于接收服务端发送的消息
 * 实现 Parcelable 接口，用于在 Fragment 之间传递对象
 */
data class MessagesReceive (
	
	/**
	 * 发送者 id
	 */
	val senderId: String,
	
	/**
	 * 接收者 id
	 */
	val receiverId: String,
	
	/**
	 * 发送时间
	 */
	val sendTime: String,
	
	/**
	 * 消息内容
	 */
	val messageData: String,
	
	/**
	 * 消息类型
	 */
	val messageType: String,
	
	/**
	 * 消息是否成功发送
	 */
	val success: Boolean,
	
	/**
	 * 接收者是否在线
	 */
	val online: Boolean,
	
	/**
	 * 消息发送失败的原因
	 */
	val errorReason: String,
	
	/**
	 * 是否是回执消息
	 */
	val isReceipt: Boolean,
): Parcelable {
	override fun equals(other: Any?): Boolean {
		if (this === other) return true
		if (javaClass != other?.javaClass) return false
		
		other as MessagesReceive
		
		if (senderId != other.senderId) return false
		if (receiverId != other.receiverId) return false
		if (sendTime != other.sendTime) return false
		if (messageData != other.messageData) return false
		if (messageType != other.messageType) return false
		if (success != other.success) return false
		if (online != other.online) return false
		if (errorReason != other.errorReason) return false
		if (isReceipt != other.isReceipt) return false
		
		return true
	}
	
	override fun hashCode(): Int {
		var result = senderId.hashCode()
		result = 31 * result + receiverId.hashCode()
		result = 31 * result + sendTime.hashCode()
		result = 31 * result + messageData.hashCode()
		result = 31 * result + messageType.hashCode()
		result = 31 * result + success.hashCode()
		result = 31 * result + online.hashCode()
		result = 31 * result + errorReason.hashCode()
		result = 31 * result + isReceipt.hashCode()
		return result
	}
	
	/**
	 * 构造函数，用于从 Parcel 中读取数据以还原对象
	 * @param parcel 包含对象数据的 Parcel
	 */
	constructor(parcel: Parcel) : this(
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readString() ?: "",
		parcel.readByte() != 0.toByte(),
		parcel.readByte() != 0.toByte(),
		parcel.readString() ?: "",
		parcel.readByte() != 0.toByte()
	)
	
	/**
	 * 将对象数据写入 Parcel，以便进行序列化
	 * @param parcel 用于写入数据的 Parcel
	 * @param flags 附加标志（通常为0）
	 */
	override fun writeToParcel(parcel: Parcel, flags: Int) {
		parcel.writeString(senderId)
		parcel.writeString(receiverId)
		parcel.writeString(sendTime)
		parcel.writeString(messageData)
		parcel.writeString(messageType)
		parcel.writeByte(if (success) 1 else 0)
		parcel.writeByte(if (online) 1 else 0)
		parcel.writeString(errorReason)
		parcel.writeByte(if (isReceipt) 1 else 0)
	}
	
	/**
	 * 描述对象内容的特殊标志，通常为 0
	 */
	override fun describeContents(): Int {
		return 0
	}
	
	companion object CREATOR : Parcelable.Creator<MessagesReceive> {
		/**
		 * 从 Parcel 创建对象的静态方法
		 * @param parcel 包含对象数据的 Parcel
		 * @return 从 Parcel 中创建的 MessagesReceive 对象
		 */
		override fun createFromParcel(parcel: Parcel): MessagesReceive {
			return MessagesReceive(parcel)
		}
		
		/**
		 * 创建指定大小的 MessagesReceive 对象数组
		 * @param size 数组大小
		 * @return MessagesReceive 对象数组
		 */
		override fun newArray(size: Int): Array<MessagesReceive?> {
			return arrayOfNulls(size)
		}
	}
}
```

```kotlin
package com.yuehai.y_chat.bean.message

import androidx.recyclerview.widget.DiffUtil
import com.yuehai.y_chat.bean.contact.Contact

/**
 * @author 月海
 * @date 2023/9/26 9:12
 * @description 消息列表项实体类，实现 Parcelable 接口，使这个类可以被 Bundle 传递
 */
data class MessageList(
	/**
	 * 联系人信息
	 */
	var contact: Contact,
	/**
	 * 消息内容，包含发送者信息
	 */
	var messagesReceiveList: MutableList<MessagesReceive>,
	
) {

	override fun equals(other: Any?): Boolean {
		if (this === other) return true
		if (javaClass != other?.javaClass) return false
		
		other as MessageList
		
		if (contact != other.contact) return false
		if (messagesReceiveList != other.messagesReceiveList) return false
		
		return true
	}
	
	override fun hashCode(): Int {
		var result = contact.hashCode()
		result = 31 * result + messagesReceiveList.hashCode()
		return result
	}
}
```

2. 在最外面的实体类 `MessageList` 中<font color="#ff0000">创建伴生对象，用于 DiffUtil 的比较</font>

```kotlin
package com.yuehai.y_chat.bean.message

import androidx.recyclerview.widget.DiffUtil
import com.yuehai.y_chat.bean.contact.Contact

/**
 * @author 月海
 * @date 2023/9/26 9:12
 * @description 消息列表项实体类，实现 Parcelable 接口，使这个类可以被 Bundle 传递
 */
data class MessageList(
	/**
	 * 联系人信息
	 */
	var contact: Contact,
	/**
	 * 消息内容，包含发送者信息
	 */
	var messagesReceiveList: MutableList<MessagesReceive>,
	
) {
	/**
	 * 伴生对象；伴生对象是一个类的对象，可以访问类的私有属性和方法
	 * 伴生对象的成员类似于 Java 中的静态成员，其生命周期伴随类始终
	 * 此处用于 DiffUtil 的比较
	 */
	companion object {
		/**
		 * DiffUtil 的回调，用于计算新旧列表的差异。
		 * 主要用于 RecyclerView.Adapter 中的数据更新。
		 */
		val DIFF_CALLBACK: DiffUtil.ItemCallback<MessageList> = object : DiffUtil.ItemCallback<MessageList>() {
			/**
			 * 这个方法用于判断两个数据项是否代表同一个对象
			 * 通常，可以直接通过比较两个数据项是否相等来判断它们是否代表同一个对象
			 */
			override fun areItemsTheSame(oldItem: MessageList, newItem: MessageList): Boolean {
				// 比较两个 MessageList 是否代表同一个联系人（通过 contactId 判断）
				return oldItem.contact.contactId == newItem.contact.contactId
			}
			
			/**
			 * 这个方法用于判断两个数据项是否具有相同的内容
			 * 通常，可以直接通过比较两个数据项是否相等来判断它们是否具有相同的内容
			 */
			override fun areContentsTheSame(oldItem: MessageList, newItem: MessageList): Boolean {
				// 比较两个 MessageList 是否具有相同的内容
				return oldItem == newItem
			}
		}
	}
	
	override fun equals(other: Any?): Boolean {
		if (this === other) return true
		if (javaClass != other?.javaClass) return false
		
		other as MessageList
		
		if (contact != other.contact) return false
		if (messagesReceiveList != other.messagesReceiveList) return false
		
		return true
	}
	
	override fun hashCode(): Int {
		var result = contact.hashCode()
		result = 31 * result + messagesReceiveList.hashCode()
		return result
	}
}
```

3. `messageListData` 观察者对象的创建：

```kotlin
/**
 * 聊天消息列表，MessageList 页面所显示的有聊天记录的联系人列表
 * MutableLiveData：可变的 LiveData，可以通过 setValue(T) 和 postValue(T) 方法来更新 LiveData 实例的值
 */
val messageListData: MutableLiveData<MutableList<MessageList>> = MutableLiveData()
```

4. 更改 `messageListData` 观察者对象中的数据，并通知其观察者数据已改变

```kotlin
/**
 * 向消息列表中添加消息
 * @param messagesReceive 接收到的消息
 */
fun addMessageToMessageList(messagesReceive: MessagesReceive) {
	// 获取当前的数据列表
	val currentList = messageListData.value ?: mutableListOf()
	
	// 查找消息列表中是否已经存在该联系人
	val existingContact = currentList.find { it.contact.contactId == messagesReceive.senderId }
	
	// 如果消息列表中已经存在该联系人，则将消息添加到该联系人的消息列表中，否则创建一个新的消息列表项
	if (existingContact != null) {
		// 将消息添加到该联系人的消息列表中
		existingContact.messagesReceiveList.add(messagesReceive)
		
		// 从原来的位置删除
		currentList.remove(existingContact)
		// 添加到集合最后
		currentList.add(existingContact)
	} else {
		// 创建一个新的消息列表项，添加到集合最后
		currentList.add(
			MessageList(
				Contact(messagesReceive.senderId, "${messagesReceive.senderId} 昵称"),
				mutableListOf(messagesReceive)
			)
		)
	}
	// 通知观察者数据已更新
	messageListData.postValue(currentList)
}
```

5. `fragment_chat_home_message_list.xml` 聊天列表布局

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 消息列表 -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
		xmlns:tools="http://schemas.android.com/tools"
		android:layout_width="match_parent"
		android:layout_height="match_parent"
		android:orientation="vertical"
		style="@style/fragment_chat_home_message_list">
	
	<!-- 消息列表 -->
	<androidx.recyclerview.widget.RecyclerView
		android:id="@+id/home_message_list"
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		tools:listitem="@layout/fragment_chat_home_message_list_item"/>

</LinearLayout>
```

6. `MessageListFragment.kt` 聊天列表代码

```kotlin
package com.yuehai.y_chat.ui.chatHome.messageList

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.yuehai.y_chat.R
import com.yuehai.y_chat.bean.WebSocketConnect.messageListData
import com.yuehai.y_chat.utils.RecyclerViewUtil

/**
 * @author 月海
 * @date 2023/9/25 13:48
 * @description 消息列表
 */
class MessageListFragment: Fragment() {
	
	/**
	 * onCreateView 是碎片的生命周期中的一种状态，在为碎片创建视图（加载布局）时调用
	 *
	 * LayoutInflater inflater：作用类似于 findViewById()
	 *      findViewById（）用来寻找 xml 布局下的具体的控件（Button、TextView等）
	 *      LayoutInflater inflater() 用来找 res/layout/ 下的 xml 布局文件
	 * ViewGroup container：表示容器，View 放在里面
	 * Bundle savedInstanceState：保存当前的状态，在活动的生命周期中，只要离开了可见阶段，活动很可能就会被进程终止，这种机制能保存当时的状态
	 */
	override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
		// 加载 Fragment 布局
		val view = inflater.inflate(R.layout.fragment_chat_home_message_list , container, false)
		
		// 获取控件对象
		val messageList = view.findViewById<RecyclerView>(R.id.home_message_list)
		/**
		 * 创建线性布局管理器
		 *
		 * 第一个参数 context 表示上下文
		 * 第二个参数 LinearLayoutManager.VERTICAL 表示布局方向为垂直方向
		 * 第三个参数 false 表示是否反转布局
		 */
		val layoutManager = LinearLayoutManager(context, LinearLayoutManager.VERTICAL, false)
		// 设置反向显示布局，即索引大的在上面，索引小的在下面
		layoutManager.reverseLayout = true
		// 设置布局管理器
		messageList.layoutManager = layoutManager
		// 设置适配器
		messageList.adapter = MessageListItemAdapter(requireContext(), findNavController())
		// 观察 messageListData，当数据发生变化时，刷新显示区域
		messageListData.observe(viewLifecycleOwner) { RecyclerViewUtil.refreshDisplayArea(messageList) }
		
		return view
	}
	
}
```

7. `fragment_chat_home_message_list_item.xml`  聊天列表项适配器布局

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 消息列表项 -->
<androidx.constraintlayout.widget.ConstraintLayout
		android:id="@+id/home_message_list_item"
		xmlns:android="http://schemas.android.com/apk/res/android"
		xmlns:app="http://schemas.android.com/apk/res-auto"
		xmlns:tools="http://schemas.android.com/tools"
		android:layout_width="match_parent"
		android:layout_height="@dimen/dp_70"
		android:padding="@dimen/dp_10"
		android:clickable="true"
		android:focusable="true"
		style="@style/fragment_chat_home_message_list_item">
	
		<!-- 头像 -->
		<ImageView
				android:id="@+id/home_message_list_item_avatar"
				android:layout_width="@dimen/dp_50"
				android:layout_height="@dimen/dp_50"
				app:layout_constraintTop_toTopOf="parent"
				app:layout_constraintBottom_toBottomOf="parent"
				app:layout_constraintStart_toStartOf="parent"
				android:layout_marginEnd="@dimen/dp_10"
				android:src="@drawable/bg_rectangle_light_gray_2"
				android:contentDescription="@string/chat_home_message_list_item_avatar"/>
		
		<!-- 昵称、时间、消息内容 -->
		<LinearLayout
				android:layout_width="0dp"
				android:layout_height="wrap_content"
				app:layout_constraintTop_toTopOf="parent"
				app:layout_constraintBottom_toBottomOf="parent"
				app:layout_constraintStart_toEndOf="@+id/home_message_list_item_avatar"
				app:layout_constraintEnd_toEndOf="parent"
				android:layout_gravity="center"
				android:layout_marginStart="@dimen/dp_10"
				android:orientation="vertical">
			
			<!-- 昵称、时间 -->
			<androidx.constraintlayout.widget.ConstraintLayout
					android:layout_width="match_parent"
					android:layout_height="wrap_content">
				
				<!-- 昵称 -->
				<TextView
						android:id="@+id/home_message_list_item_nick_name"
						android:layout_width="0dp"
						android:layout_height="wrap_content"
						app:layout_constraintTop_toTopOf="parent"
						app:layout_constraintBottom_toBottomOf="parent"
						app:layout_constraintStart_toStartOf="parent"
						app:layout_constraintEnd_toStartOf="@+id/home_message_list_item_date"
						android:paddingEnd="@dimen/dp_10"
						android:textSize="@dimen/sp_20"
						android:lines="1"
						android:ellipsize="end"
						tools:ignore="RtlSymmetry"/>
				
				<!-- 时间 -->
				<TextView
						android:id="@+id/home_message_list_item_date"
						android:layout_width="wrap_content"
						android:layout_height="wrap_content"
						app:layout_constraintBottom_toBottomOf="parent"
						app:layout_constraintEnd_toEndOf="parent"
						android:textSize="@dimen/sp_15"/>
			</androidx.constraintlayout.widget.ConstraintLayout>
			
			<!-- 消息内容 -->
			<TextView
					android:id="@+id/home_message_list_item_message"
					android:layout_width="wrap_content"
					android:layout_height="wrap_content"
					android:textSize="@dimen/sp_15"
					android:lines="1"
					android:ellipsize="end"/>
			
		</LinearLayout>
	
</androidx.constraintlayout.widget.ConstraintLayout>
```

8. `MessageListItemAdapter.kt`  聊天列表项适配器代码，<font color="#ff0000">重点：实现</font> `: ListAdapter<MessageList, MessageListItemAdapterHolder>(MessageList.DIFF_CALLBACK)`

```kotlin
package com.yuehai.y_chat.ui.chatHome.messageList

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.navigation.NavController
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.yuehai.y_chat.R
import com.yuehai.y_chat.bean.WebSocketConnect.messageListData
import com.yuehai.y_chat.bean.message.MessageList


/**
 * @author 月海
 * @date 2023/9/26 8:46
 * @description 消息列表项适配器
 */
class MessageListItemAdapter(
	// 上下文环境
	private var context: Context,
	// NavController 导航对象
	private var findNavController: NavController
): ListAdapter<MessageList, MessageListItemAdapterHolder>(MessageList.DIFF_CALLBACK) {
	/**
	 * onCreateViewHolder() 用于创建新的 ViewHolder 对象，当 RecyclerView 需要新的 ViewHolder 时，会调用此方法。
	 * 该方法会创建并初始化 ViewHolder 及其关联的视图，但不会填充视图的内容，因为此时 ViewHolder 尚未绑定到具体数据。
	 * 该方法的返回值是一个 ViewHolder 对象。在该方法中，需要创建一个新的 View 对象，并将其包装在一个新的 ViewHolder 对象中。
	 */
	override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MessageListItemAdapterHolder {
		return MessageListItemAdapterHolder(LayoutInflater.from(context).inflate(R.layout.fragment_chat_home_message_list_item, parent, false))
	}
	
	/**
	 * getItemCount() 用于获取数据集中的元素数量。当 RecyclerView 需要知道列表中有多少项时，会调用此方法。
	 * 该方法的返回值是一个整数，表示数据集中的元素数量。
	 */
	override fun getItemCount(): Int {
		return messageListData.value?.size ?: 0
	}
	
	/**
	 * onBindViewHolder() 用于将数据与 ViewHolder 对象关联起来。当 RecyclerView 需要新的数据绑定到 ViewHolder 时，会调用此方法。
	 * 该方法会提取适当的数据，并使用该数据填充 ViewHolder 的布局。
	 * 该方法的第一个参数是一个 ViewHolder 对象，第二个参数是该 ViewHolder 在列表中的位置。在该方法中，您需要使用适当的数据填充视图。
	 */
	override fun onBindViewHolder(holder: MessageListItemAdapterHolder, position: Int) {
		// 获取 ViewHolder 对象
		
		// 获取消息内容列表中的最后一项所在的索引
		val lastMessageIndex = messageListData.value!![position].messagesReceiveList.size - 1
		
		// 头像
		holder.itemAvatar.setImageResource(R.drawable.software_icon)
		// 昵称
		holder.itemNickName.text = messageListData.value?.get(position)?.contact?.contactNickName
		// 时间
		holder.itemDate.text = messageListData.value?.get(position)?.messagesReceiveList?.get(lastMessageIndex)?.sendTime
		// 消息内容
		holder.itemMessage.text = messageListData.value?.get(position)?.messagesReceiveList?.get(lastMessageIndex)?.messageData
		
		// item 的单击事件，跳转至消息详情页面
		holder.item.setOnClickListener {
			// 创建 Bundle 对象并添加数据
			val bundle = Bundle()
			// 当前联系人所在消息列表的索引
			bundle.putInt("position", position)
			// 当前联系人的信息
			bundle.putString("contactId", messageListData.value?.get(position)?.contact?.contactId)
			findNavController.navigate(R.id.action_chat_home_to_message_details, bundle)
		}
	}

}

/**
 * ImageViewerAdapter 对应的 holder 对象
 */
class MessageListItemAdapterHolder(view: View) : RecyclerView.ViewHolder(view) {
	// 根布局
	var item: ConstraintLayout
	// 头像
	var itemAvatar: ImageView
	// 昵称
	var itemNickName: TextView
	// 时间
	var itemDate: TextView
	// 消息
	var itemMessage: TextView
	
	init {
		item = view.findViewById(R.id.home_message_list_item)
		itemAvatar = view.findViewById(R.id.home_message_list_item_avatar)
		itemNickName = view.findViewById(R.id.home_message_list_item_nick_name)
		itemDate = view.findViewById(R.id.home_message_list_item_date)
		itemMessage = view.findViewById(R.id.home_message_list_item_message)
	}
}
```

9. 此时更新 `messageListData` 即可刷新列表

#### Ⅳ、RecyclerView 刷新方法

```kotlin
// 刷新所有
public final void notifyDataSetChanged();

// position数据发生了改变，那调用这个方法，就会回调对应position的onBindViewHolder()方法了
public final void notifyItemChanged(int position);

// 刷新从positionStart开始itemCount数量的item了（这里的刷新指回调onBindViewHolder()方法）
public final void notifyItemRangeChanged(int positionStart, int itemCount);

// 在第position位置被插入了一条数据的时候可以使用这个方法刷新，注意这个方法调用后会有插入的动画，这个动画可以使用默认的，也可以自己定义
public final void notifyItemInserted(int position);

// 从fromPosition移动到toPosition为止的时候可以使用这个方法刷新
public final void notifyItemMoved(int fromPosition, int toPosition);

// 批量添加
public final void notifyItemRangeInserted(int positionStart, int itemCount);

// 第position个被删除的时候刷新，同样会有动画
public final void notifyItemRemoved(int position);

// 批量删除
public final void notifyItemRangeRemoved(int positionStart, int itemCount);
```

### ④、Button 按钮

#### Ⅰ、Button 按钮背景

1. 使用 Android Studio 4.1 之后的版本进行开发时，创建的项目默认的主题都是 `Theme.MaterialComponents.DayNight.DarkActionBar`。所有 Button 都是 Material 类型的 Button，默认使用主题色。即 `app/src/main/res/values/themes.xml` 中定义的颜色
2. 若是想自定义背景，可以使用 `android.widget.Button`

```shell
<android.widget.Button
        android:id="@+id/btn_1"
```

#### Ⅱ、

### ⑤、

### ⑥、

## 8、

# 十二、错误总结

## 1、module java.base does not "opens java.io"

```cmd
Unable to make field private final java.lang.String java.io.File.path accessible: module java.base does not "opens java.io" to unnamed module @28904302
```

1. 打开项目根目录下的 `gradle.properties` 文件
2. 加入以下代码：

```properties
org.gradle.jvmargs=-Xmx1536M \
--add-exports=java.base/sun.nio.ch=ALL-UNNAMED \
--add-opens=java.base/java.lang=ALL-UNNAMED \
--add-opens=java.base/java.lang.reflect=ALL-UNNAMED \
--add-opens=java.base/java.io=ALL-UNNAMED \
--add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED
```

## 2、编译报错：  `javax.annotation.processing.Generated`

1. 原因：`javax.annotation.processing.Generated` 类是 JDK 1.8 引入的注解，用于标识由注解处理器生成的代码。但是 jdk11及其以上移除了该包
2. 解决方法 1：下载 `javax.annotation-api`，手动引入
3. 解决方法 2：退回 jdk8
4. 解决方法 3：`build.gradle` 中添加依赖：`compile 'org.glassfish:javax.annotation:10.0-b28'`

## 3、

## 4、

## 5、

# 十三、其他补充记录

## 1、工具

### ①、开源投屏工具：`scrcpy`

1. 下载解压：https://github.com/Genymobile/scrcpy/releases
2. 鼠标键盘操作：`https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md`
3. 给安装目录设置环境变量；也可以不设置，每次进入解压目录执行命令也可

![|527](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230425162439.png)

4. 手机记得开启 usb 调试
5. 断开所有 wifi 连接设备：`adb disconnect`
6. 断开指定的 wifi 设备连接：`adb disconnect xxx.xxx.xxx.xxx`

#### Ⅰ、USB 连接

1. usb 连接手机
2. 打开 cmd，进入解压目录
3. 输入 `adb devices`，查看已连接设备
4. 若是已连接设备只有一个，则输入 `scrcpy` 直接进行连接

#### Ⅱ、网络连接设备

1. 打开 cmd，进入解压目录
2. 输入 `adb connect IP:端口号` 连接设备
3. 输入 `adb devices`，查看已连接设备
4. 若是已连接设备只有一个，则输入 `scrcpy` 直接进行连接

#### Ⅲ、连接多个设备

1. 输入 `adb devices`，查看已连接设备
2. 若是已连接设备不只有一个，则输入 `scrcpy -s [ip或者设备号]` 进行连接

#### Ⅳ、播放手机的声音

1. scrcpy 是无法实现该功能的，但可以通过 sndcpy 播放手机的声音
2. 首先，下载 sndcpy：https://github.com/rom1v/sndcpy#get-the-app
3. 和 scrcpy 相同，手机端需要开启开发者模式和 USB 调试，并且开启 USB 安装
4. PC 端安装 VLC播放器：https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe
5. 在 sndcpy 的文件夹下输入 cmd 进入命令行，然后输入 `sndcpy`
6. 此时手机端会提醒安装一个 app，同意就是了
7. 安装完成后命令行应该会显示这样：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230425164606.png)

8. 不要关闭此命令行窗口，再开启一个 scrcpy 的命令行窗口
9. 以上面的方式连接 scrcpy 即可
10. 该程序的原理是通过在手机端安装 sndcpyapp，拦截手机端的声音，再通过 adb 转发到 PC 端，再通过 VLC 播放器播放声音

#### Ⅴ、常用快捷键

- 在 Windows 中，MOD 一般代表 Alt 键

| 动作                                  | 快捷键                              |
| ------------------------------------- | ----------------------------------- |
| 将窗口大小调整为 1：1（像素完美）     | MOD + g                             |
| 调整窗口大小以删除黑色边框            | MOD + w丨双击左键                   |
| 返回主页                              | MOD + h丨中键点击                   |
| 返回按钮                              | MOD + b丨MOD + Backspace 丨右键单击 |
| 打开任务列表                          | MOD + s                             |
| 音量增加                              | MOD + ↑                             |
| 音量减少                              | MOD + ↓                             |
| 点击电源键（锁屏 & 解锁）             | MOD + p                             |
| 关闭设备屏幕（scrcpt 中依然显示镜像） | MOD + o                                    |
| 打开设备屏幕 | MOD + Shift + o                                    |
| 旋转设备屏幕 | MOD + r |
| 展开通知面板 | MOD + n |
| 复制到剪贴板 | MOD + c |
| 同步剪贴板和粘贴 | MOD + v |
| 注入计算机剪贴板文本 | MOD + Shift + v |
| 捏合缩放 | Ctrl + 左键点击移动 |
| 拖放APK文件 | 从计算机安装APK |
| 拖放非APK文件 | 将文件推送到设备 |

#### Ⅵ、几大类模拟器的地址和端口号

1. 网易mumu模拟器：adb connect 127.0.0.1:7555
2. 夜神模拟器：adb connect 127.0.0.1:62001
3. 蓝叠模拟器：adb connect 127.0.0.1:5555
4. 雷电模拟器：adb connect 127.0.0.1:5555

### ②、安卓手机当电脑摄像头 DroidCam

> 电脑软件下载网址：https://www.dev47apps.com/
> 
> 电脑软件：[DroidCam.Setup](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FDroidCam.Setup.6.5.2.exe)
> 
> 手机端软件：[DroidCam](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FDroidCam.apk)

1. 电脑与手机端分别安装软件
2. 手机端进入下方页面，记录端口号

![|250](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2F4A13FF6FFC900441630FD400F9D43B98.jpg)

3. 电脑端打开 DroidCamApp 软件，选择 USB 连接，选择自己的手机，填入端口号，点击 `Start` 进行连接

![|240](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420084259.png)

4. 连接成功后：

![|315](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020230420084501.png)

### ③、连接手机使其作为外放音响 1 SoundWire（不推荐）

> 电脑端：[SoundWire_Server_setup7-8-10.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FSoundWire_Server_setup7-8-10.zip)
> 
> 安卓端：[SoundWire_Free.apk](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FSoundWire_Free.apk)
> 
> 推荐使用下面的 SyncAudio

1. 电脑手机下载安装上面的软件
2. 电脑端打开软件，防火墙点击允许

![|418](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231023141708.png)

3. 在 Input Select 选择输出音频，选一个未使用的
4. 之后再到Windows音量中修改输出设备，选择你在软件中勾选的输出源

![|413](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231023141752.png)

5. 手机端在中间的方框中输入本地 IP，回车键即可连接

![|325](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231023141820.png)

### ④、连接手机使其作为外放音响 2 SyncAudio

> 电脑端下载：[SyncAudio(同步听) 1.0.3.7z](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FSyncAudio%28%E5%90%8C%E6%AD%A5%E5%90%AC%29%201.0.3.7z)

1. 电脑端下载上面的软件，解压，双击打开
2. 使用手机任意软件扫描二维码即可
3. 推荐使用微信等不会被经常杀掉后台的软件

### ⑤、

### ⑥、

## 2、模拟器

### ①、genymotion 模拟器

> 官网：https://www.genymotion.com/

#### Ⅰ、安装软件失败

> 官网解释：Genymotion 模拟器使用的是 x86 架构，在第三方市场上的应用有部分不采用 x86 这么一种架构，所以在编译的时候不通过，报 “APP not installed”
> 
> 可以下载 Genymotion 提供的 ARM 转换工具包，将应用市场中的 ARM 架构的 apk 转换成 Genymotion 可以编译的 x86 架构：Genymotion_ARM_Translation
> 
> https://github.com/m9rco/Genymotion_ARM_Translation
> 
> [Genymotion-ARM-Translation_for_4.3.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_4.3.zip)
> 
> [Genymotion-ARM-Translation_for_4.4.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_4.4.zip)
> 
> [Genymotion-ARM-Translation_for_5.1.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_5.1.zip)
> 
> [Genymotion-ARM-Translation_for_6.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_6.0.zip)
> 
> [Genymotion-ARM-Translation_for_7.X.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2Genymotion-ARM-Translation_for_7.X.zipp)
> 
> [Genymotion-ARM-Translation_for_8.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_8.0.zip)
> 
> [Genymotion-ARM-Translation_for_9.0.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FGenymotion-ARM-Translation_for_9.0.zip)

1. 下载 Genymotion_ARM_Translation
2. 解压 `Genymotion_ARM_Translation-master`，进入 `package` 目录，将对应安卓版本的压缩包拖到模拟器中（<font color="#ff0000">注意电脑中 Genymotion_ARM_Translation 保存的目录不可以是中文</font>）
3. 若是直接安装了，则直接重启模拟器即可；若是被复制到了 `Download` 目录，则继续下一步
4. 打开电脑 cmd ，执行：

```cmd
 adb shell
 cd /sdcard/Download/
 sh /system/bin/flash-archive.sh /sdcard/Download/Genymotion-ARM-Translation.zip
 adb reboot
```

5. 出现 `result ok` 代表成功，重启模拟器即可

```cmd
......
[install_file] Installing system/lib/arm/nb/libtcb.so
[install_arm_lib] Skipping system/lib/arm/nb/libui.so lib (x86 version exists)
[install_arm_lib] Skipping system/lib/arm/nb/libutils.so lib (x86 version exists)
[install_arm_lib] Skipping system/lib/arm/nb/libvulkan.so lib (x86 version exists)
[install_arm_lib] Skipping system/lib/arm/nb/libz.so lib (x86 version exists)
[install_file] Installing system/lib/arm/xstdata
[install_file] Installing system/lib/libhoudini.so
[flash_archive] Remount /system in ro
mount: '/dev/block/sda6'->'/system': Device or resource busy
[WARNING][remount_system_ro] cannot remount system in ro
[flash_archive] Delete tmp directory
rm: /data/local/tmp/sanitized.zip: No such file or directory
[flash_archive] Done successfully !
{Result:OK};
genymotion:/sdcard/Download #
```

6. 但是我试了安卓 8 和安卓 9 ，都不行，不知道为啥

#### Ⅱ、genymotion 无法启动虚拟设备

##### （1）、问题

- 无法启动，报错：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231019152707.png)

##### （2）、原因 1：虚拟网卡问题

2. 原因：Genymotion 运行虚拟机是依靠 VirtualBox，但是，启动 Genymotion 虚拟机后，VirtualBox 会创建一个网络连接，问题出现在这里：网络连接未启动
3. 解决方案：
4. 在 Windows 下打开控制面板，按照路径：控制面板 --> 网络和 Internet --> 网络和共享中心 --> 更改适配器选项

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231019152919.png)

5. 将被 `VirtualBox Host-Only Nerwork` 创建的所有连接关闭，然后打开最大的那个即可

![|675](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231019152956.png)

##### （3）、原因 2：未正常关闭

1. 打开软件 `Oracle VM VirtualBox`
2. 选择未正常关闭的设备
3. 点击清楚，清楚未正常关闭状态即可

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020240308181725.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020240308181742.png)

#### Ⅲ、genymotion 更改模拟器的存放路径

> 1. 当用一个电脑上的新用户想使用之前的虚拟机，或者自己移动了虚拟机的存放路径
> 2. 那么就要修改对应的用户目录中的配置文件
> 3. genymotion 的模拟器默认存放路径是 `C:/Users/用户名/AppData/Local/Genymobile/Genymotion/deployed/`
> 4. 修改默认存放路径：Genymotion -> Settings -> Hypervisor

1. 进入目录，打开文件：`C:\Users\用户名.VirtualBox\VirtualBox.xml` 
2. 查看该标签：

```xml
<MachineRegistry>
  <MachineEntry uuid="{f5a61440-cc21-45d3-9459-a9ce48cc6395}" src="D:\apply\game\Genymotion\saveData\Google Pixel 2\Google Pixel 2.vbox"/>
</MachineRegistry>
```

3. 将 `src=` 后的内容换成移动之后的文件路径即可
4. 若是新用户的配置文件中没有这个标签，那么直接复制过来即可

### ②、

### ③、

### ④、

## 3、adb 问题整理

### ①、adb 常用命令

1. 多设备时要在 adb 后加 -s 指定设备
2. 官网：
	1. https://android-doc.github.io/tools/help/adb.html
	2. https://android-doc.github.io/tools/help/shell.html#shellcommands
3. 关于ADB更多的用法可以参考：https://github.com/mzlogin/awesome-adb

| 命令                                                                                    | 描述                                |             |
| ------------------------------------------------------------------------------------- | --------------------------------- | ----------- |
| adb shell svc wifi disable/enable                                                     | 关闭wifi/开启wifi                     |             |
| adb devices                                                                           | 查看当前连接的设备                         |             |
| adb shell media volume --show --stream 3 --get                                        | 获取当前多媒体音量大小                       |             |
| adb disconnect xxx.xxx.xxx.xxx                                                        | 断开指定的wifi设备连接                     |             |
| adb shell media volume --show --stream 3 --set 1                                      | 设定当前多媒体音量大小                       |             |
| adb disconnect                                                                        | 断开所有wifi连接设备                      |             |
| adb shell setprop service.adb.tcp.port 5555                                           | 设置adb服务端口为5555， 打开adb网络调试功能       |             |
| adb connect device_ip_address[:5555]                                                  | 利用ip连接新的android设备，需要在同一网络环境下      |             |
| adb get-state                                                                         | 获取连接状态，有3种：device，offline，unknown |             |
| adb start-server                                                                      | 启动adb服务                           |             |
| adb kill-server                                                                       | 关闭adb服务                           |             |
| adb uninstall package                                                                 | 卸载程序，package是包名                   |             |
| adb install xxx.apk                                                                   | 安装程序                              |             |
| adb shell am start -n package/package.MainActivity                                    | 启动程序，package是包名                   |             |
| adb shell am force-stop package                                                       | 强制结束程序，package是包名                 |             |
| adb pull /sdcard/DebugLog/20220805.log C:\Users\10153702\Desktop                      | 将设备里的文件拉取到本地                      |             |
| adb push C:\Users\10153702\Desktop\20220805.log /sdcard/DebugLog/20220805.log         | 将本地文件上传到设备里                       |             |
| adb shell dumpsys package jp.retailai.raicart                                         | 查看应用相关信息                          |             |
| adb shell dumpsys meminfo jp.retailai.raicart                                         | 查看应用占用内存情况                        |             |
| adb shell dumpsys cpuinfo                                                             | findstr jp.retailai.raicart       | 查看应用cpu占用情况 |
| adb shell input keyevent 66                                                           | 模拟按回车键                            |             |
| adb shell input keyevent 3                                                            | 模拟按HOME键                          |             |
| adb shell input text 2960000000012                                                    | 输入字符串                             |             |
| adb shell input keyevent 26                                                           | 灭/亮屏                              |             |
| adb shell input keyevent 82                                                           | 解锁屏幕                              |             |
| adb shell input tap x y                                                               | 按照(x,y)位置模拟点击                     |             |
| adb shell input swipe x1 y1 x2 y2                                                     | 从(x1,y1)位置到(x2,y2)位置模拟滑动          |             |
| adb shell monkey -p jp.retailai.raicart 100>C:\Users\10153702\Desktop\\monkey_log.txt | 执行 monkey100 次随意点击测试，并记录日志到本地     |             |

### ②、手机开启无线调试功能

> 华为 mate20 pro 测试可用

1. 进入手机的开发者选项，勾选：USB 调试
2. 勾选：“仅充电”模式下允许 ADB 调试

![|261](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020240903083653.png)

3. 连接电脑，手机弹窗选择：传输文件
4. 使用 ADB 连接输入命令：

```shell
adb tcpip 5555
```

5. 如果出现以下输出，则表明开启端口成功

```shell
restarting in TCP mode port: 5555
```

6. 此时电脑端输入以下命令远程连接手机：

```shell
adb connect 手机ip:端口号
```

7. 出现以下输出，则表明连接成功

```shell
* daemon not running; starting now at tcp:5038
* daemon started successfully
connected to 172.20.5.148:5555
```

8. 查看当前连接的设备：

```shell
adb devices
```

9. 断开指定的wifi设备连接：

```shell
adb disconnect 手机ip:端口号
```

10. 不过这个方法有个问题，就是一旦设备重启，就要重头操作一遍。所以要尽量保持手机开机

### ③、

### ④、

## 4、idea 问题整理

### ①、关闭 Idea 时会自动关闭 ADB 进程的解决办法

1. idea 点击文件 -> 设置 -> 构建、执行、部署 -> 调试器，进入以下页面，拉到最下面

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222102826.png)

2. 选择：`Use existing manually managed server`，因为ADB 默认使用的端口号是 `5037`，所以设置为 `5037` 即可
3. 但是，这个选项不可以设置为 `5037` 即以下，只能设置为 `5038` 即以上（我不知道为什么会这样）
4. 所以此处将其设置为 `5038`，然后修改 ADB 的默认端口为 `5038` 即可
5. 打开电脑的高级系统设置，在系统变量中新建一个变量：`ANDROID_ADB_SERVER_PORT`，值设置为 `5038`
6. 重启电脑
7. 命令行窗口中，输入 `adb start-server`，显示 `daemon not running; starting now at tcp:5038` 即为配置完成

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020231222103427.png)

### ②、idea 打开安卓 xml 布局文件时会卡死

#### Ⅰ、问题

1. idea 打开安卓 xml 布局文件时会卡死，要很久才能自己回复
2. 此时 idea 页面冻结，什么也点不了，只能任务管理器关闭进程

#### Ⅱ、解决

1. 点击文件 -> 设置，搜索 Emmet
2. 取消勾选 `启用 XML/HTML Emmett (E)`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FAndroid%2Fattachments%2FPasted%20image%2020241023085809.png)


### ③、

### ④、

## 5、

## 6、



