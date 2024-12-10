> 官方教程：https://flutter.cn/docs
> 
> 文档参考：https://book.flutterchina.club/
> 
> 文档参考 github：https://github.com/flutterchina/flutter_in_action_2nd

# 一、环境准备

## 1、配置环境变量

1. 进入官网，下载 SDK：https://flutter.cn/docs/get-started/install/windows

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926125318.png)

2. 将下载下来的文件解压，并将 `bin` 目录配置到系统变量中

![|550](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926125515.png)

3. 打开命令行窗口，执行：`flutter --version`、`dart --version`，出现如下信息则配置成功

![|775](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926130052.png)

4. 如是提示网络问题，则看下面的将下载源改为国内源

## 2、将下载源改为国内源

1. 打开环境变量，新建两条用户变量
	1. `PUB_HOSTED_URL`、`https://pub.flutter-io.cn`
	2. `FLUTTER_STORAGE_BASE_URL`、`https://storage.flutter-io.cn`

![|641](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926130339.png)

## 3、使用 idea 创建 flutter 项目

1. idea 安装两个插件 `Flutter`、`Dart`

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926131825.png)

2. 点击新建，创建一个 `flutter` 项目

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020230926131950.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016155909.png)

3. 项目创建完成，结构说明：

![|632](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016163227.png)

## 4、连接手机或模拟器安卓测试

1. 某个模拟器

![|925](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016160123.png)

2. idea 会自动连接到模拟器，点击运行安装软件

![|950](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016160239.png)

3. 安装完成

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016160354.png)

4. 进入软件

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016160410.png)

5. 热重载与开发者工具

![|571](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017095401.png)

## 5、使用命令启动并安装项目

1. 在连接到机器的情况下

![|1175](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016161205.png)

2. 进入终端，执行：
	1. `flutter run`，它将默认使用第一个设备进行安装和运行
	2. `flutter run -d all`：它会将应用程序安装在所有连接的设备上

![|1000](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016161500.png)

4. 安装完成：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016161534.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231016161543.png)

5. 在使用命令安装项目的情况下，在此终端窗口中，按下以下按键，将会执行不同操作：

  | 按键 | 功能                                                 |
  | ---- | ---------------------------------------------------- |
  | r | 热重载                   |
  | R（shift + r） | 热重启项目。                                         |
  | p | 显示网格，这个可以很好的掌握布局情况，工作中很有用。 |
  | o | 切换 android 和 ios 的预览模式                                 |

## 6、Dart SDK 在 Flutter SDK 中的存储路径

- `flutterSDK路径\bin\cache\dart-sdk`

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231127090935.png)

## 7、

## 8、

# 二、flutter 基础知识

## 1、数器应用示例

1. 用 Android Studio 和 VS Code 创建的 Flutter 应用模板默认是一个简单的计数器示例。
2. 本节先仔细讲解一下这个计数器 Demo 的源码，以对 Flutter 应用程序结构有个基本了解，然后在随后的小节中将会基于此示例，一步一步添加一些新的功能来介绍 Flutter 应用的其他概念与技术。

### ①、创建 Flutter 应用模板

1. 通过 Android Studio 或 VS Code 创建一个新的 Flutter 工程，创建好后，就会得到一个默认的计数器应用示例。
2. 注意，默认计数器示例可能随着编辑器 Flutter 插件的版本变化而变化，本例中会介绍计数器示例的全部代码，所以不会对本示例产生影响。
3. 我们先运行创建的工程，效果如图所示：

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231115131326.png)

4. 该计数器示例中，每点击一次右下角带 `+` 号的悬浮按钮，屏幕中央的数字就会加1。
5. 在这个示例中，主要 Dart 代码是在 `lib/main.dart` 文件中，下面是它的源码：

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('You have pushed the button this many times:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
```

### ②、模板代码分析

#### Ⅰ、导入包

```dart
import 'package:flutter/material.dart';
```

1. 此行代码作用是导入了 Material UI 组件库。Material 是一种标准的移动端和 web 端的视觉设计语言，
2. Flutter 默认提供了一套丰富的 Material 风格的UI组件

#### Ⅱ、应用入口

```dart
void main() => runApp(MyApp());
```

1. 与 C/C++、Java 类似，Flutter 应用中 main 函数为应用程序的入口。
2. main 函数中调用了 `runApp` 方法，它的功能是启动 Flutter 应用。
3. runApp 它接受一个 Widget 参数，在本示例中它是一个 MyApp 对象，`MyApp()` 是 Flutter 应用的根组件。
4. main函数使用了 `=>` 符号，这是 Dart 中单行函数或方法的简写

#### Ⅲ、应用结构

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      //应用名称  
      title: 'Flutter Demo', 
      theme: ThemeData(
        //蓝色主题  
        primarySwatch: Colors.blue,
      ),
      //应用首页路由  
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}
```

1. `MyApp` 类代表 Flutter 应用，它继承了 `StatelessWidget` 类，这也就意味着应用本身也是一个 widget。
2. 在 Flutter 中，大多数东西都是 widget（后同“组件”或“部件”），包括对齐（Align）、填充（Padding）、手势处理（GestureDetector）等，它们都是以 widget 的形式提供。
3. Flutter 在构建页面时，会调用组件的 `build` 方法，widget 的主要工作是提供一个 `build()` 方法来描述如何构建 UI 界面（通常是通过组合、拼装其他基础 widget ）。
4. `MaterialApp` 是 Material 库中提供的 Flutter APP 框架，通过它可以设置应用的名称、主题、语言、首页及路由列表等。`MaterialApp` 也是一个 widget。
5. `home` 为 Flutter 应用的首页，它也是一个 widget

### ③、初识 Widget

```dart
class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;
  
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
 ...
}
```

1. `MyHomePage` 是应用的首页，它继承自 `StatefulWidget` 类，表示它是一个有状态的组件（Stateful widget）。关于 Stateful widget 我们将在 “2.2Widget简介” 一节仔细介绍，现在我们只需简单认为有状态的组件（Stateful widget） 和无状态的组件（Stateless widget）有两点不同：
	1. Stateful widget 可以拥有状态，这些状态在 widget 生命周期中是可以变的，而 Stateless widget 是不可变的。
	2. Stateful widget 至少由两个类组成：
		1. 一个 `StatefulWidget` 类。
		2. 一个 `State` 类； `StatefulWidget` 类本身是不变的，但是State类中持有的状态在 widget 生命周期中可能会发生变化。
2. `_MyHomePageState` 类是 `MyHomePage` 类对应的状态类。看到这里，我们已经发现：和 `MyApp` 类不同， `MyHomePage` 类中并没有 `build` 方法，取而代之的是，`build` 方法被挪到了`_MyHomePageState` 方法中，至于为什么这么做，先留个疑问，在分析完完整代码后再来解答

### ④、State 类

1. 接下来，我们看看 `_MyHomePageState` 中都包含哪些东西：
2. 组件的状态：由于我们只需要维护一个点击次数计数器，所以定义一个 `_counter` 状态，`_counter` 为保存屏幕右下角带 `+` 号按钮点击次数的状态。

```dart
int _counter = 0; //用于记录按钮点击的总次数
```

3. 设置状态的自增函数：当按钮点击时，会调用此函数，该函数的作用是先自增 `_counter`，然后调用 `setState` 方法。`setState` 方法的作用是通知 Flutter 框架，有状态发生了改变，Flutter 框架收到通知后，会执行 `build` 方法来根据新的状态重新构建界面， `Flutter` 对此方法做了优化，使重新执行变的很快，所以你可以重新构建任何需要更新的东西，而无需分别去修改各个 widget

```dart
void _incrementCounter() {
  setState(() {
     _counter++;
  });
}
```

4. 构建 UI 界面的 build 方法：构建 UI 界面的逻辑在 `build` 方法中，当 `MyHomePage` 第一次创建时， `_MyHomePageState` 类会被创建，当初始化完成后，Flutter 框架会调用 widget 的 `build` 方法来构建 widget 树，最终将 widget 树渲染到设备屏幕上。所以，我们看看 `_MyHomePageState` 的 `build` 方法中都干了什么事：
	1. `Scaffold` 是 Material 库中提供的页面脚手架，它提供了默认的导航栏、标题和包含主屏幕 widget 树（后同“组件树”或“部件树”）的 `body` 属性，组件树可以很复杂。在后面示例中，路由默认都是通过 `Scaffold` 创建。
	2. `body` 的组件树中包含了一个 `Center` 组件，`Center` 可以将其子组件树对齐到屏幕中心。
	3. 此例中， `Center` 子组件是一个 `Column` 组件，`Column` 的作用是将其所有子组件沿屏幕垂直方向依次排列； 
	4. 此例中 `Column` 子组件是两个 `Text`，第一个 `Text` 显示固定文本 `You have pushed the button this many times:` ，第二个Text 显示 `_counter` 状态的数值。
	5. `floatingActionButton` 是页面右下角的带 `+` 的悬浮按钮，它的 `onPressed` 属性接受一个回调函数，代表它被点击后的处理器，本例中直接将 `_incrementCounter` 方法作为其处理函数。

```dart
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      title: Text(widget.title),
    ),
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text('You have pushed the button this many times:'),
          Text(
            '$_counter',
            style: Theme.of(context).textTheme.headline4,
          ),
        ],
      ),
    ),
    floatingActionButton: FloatingActionButton(
      onPressed: _incrementCounter,
      tooltip: 'Increment',
      child: Icon(Icons.add),
    ), 
  );
}
```

5. 现在，我们将整个计数器执行流程串起来：当右下角的 `floatingActionButton` 按钮被点击之后，会调用`_incrementCounter` 方法。在 `_incrementCounter` 方法中，首先会自增 `_counter` 计数器（状态），然后 `setState` 会通知 Flutter 框架状态发生变化，接着，Flutter 框架会调用 `build` 方法以新的状态重新构建 UI，最终显示在设备屏幕上

### ⑤、为什么要将 build 方法放在 State 中，而不是放在 StatefulWidget 中？

1. 现在，我们回答之前提出的问题，为什么 `build()` 方法放在 `State` 而不是 `StatefulWidget` 中 ？
2. 这主要是为了提高开发的灵活性。
3. 如果将 `build()` 方法放在 `StatefulWidget` 中则会有两个问题：

#### Ⅰ、状态访问不便

1. 试想一下，如果我们的 `StatefulWidget` 有很多状态，而每次状态改变都要调用 `build` 方法，由于状态是保存在  `State` 中的，如果 `build` 方法在 `StatefulWidget` 中，那么 `build` 方法和状态分别在两个类中，那么构建时读取状态将会很不方便！
2. 试想一下，如果真的将 `build` 方法放在 `StatefulWidget` 中的话，由于构建用户界面过程需要依赖 `State`，所以 `build` 方法将必须加一个 `State` 参数，大概是下面这样：

```dart
Widget build(BuildContext context, State state){
  //state.counter
  ...
}
```

3. 这样的话就只能将 `State` 的所有状态声明为公开的状态，这样才能在 `State` 类外部访问状态！但是，将状态设置为公开后，状态将不再具有私密性，这就会导致对状态的修改将会变的不可控。
4. 但如果将 `build()` 方法放在 `State` 中的话，构建过程不仅可以直接访问状态，而且也无需公开私有状态，这会非常方便。

#### Ⅱ、继承 `StatefulWidget` 不便

1. 例如，Flutter 中有一个动画 widget 的基类 `AnimatedWidget`，它继承自 `StatefulWidget` 类。
2. `AnimatedWidget` 中引入了一个抽象方法 `build(BuildContext context)`，继承自 `AnimatedWidget` 的动画 widget 都要实现这个 `build` 方法。现在设想一下，如果 `StatefulWidget` 类中已经有了一个 `build` 方法，正如上面所述，此时 `build` 方法需要接收一个 `State` 对象，这就意味着 `AnimatedWidget` 必须将自己的 `State` 对象(`记为_animatedWidgetState`) 提供给其子类，因为子类需要在其 `build` 方法中调用父类的 `build` 方法，代码可能如下：

```dart
class MyAnimationWidget extends AnimatedWidget{
    @override
    Widget build(BuildContext context, State state){
      //由于子类要用到AnimatedWidget的状态对象_animatedWidgetState，
      //所以AnimatedWidget必须通过某种方式将其状态对象_animatedWidgetState
      //暴露给其子类   
      super.build(context, _animatedWidgetState)
    }
}
```

3. 这样很显然是不合理的，因为：
	1. `AnimatedWidget` 的状态对象是 `AnimatedWidget` 内部实现细节，不应该暴露给外部。
	2. 如果要将父类状态暴露给子类，那么必须得有一种传递机制，而做这一套传递机制是无意义的，因为父子类之间状态的传递和子类本身逻辑是无关的。
4. 综上所述，可以发现，对于 `StatefulWidget`，将 `build` 方法放在 `State` 中，可以给开发带来很大的灵活性。

## 2、Widget 简介

### ①、Widget 概念

1. 在 Flutter 中几乎所有的对象都是一个 `widget` 。
2. 与原生开发中“控件”不同的是，Flutter 中的 `widget` 的概念更广泛，它不仅可以表示 UI 元素，也可以表示一些功能性的组件如：用于手势检测的 `GestureDetector` 、用于 APP 主题数据传递的 `Theme` 等等。而原生开发中的控件通常只是指 UI 元素。
3. 在后面的内容中，我们在描述 UI 元素时可能会用到“控件”、“组件”这样的概念，我们心里需要知道他们就是 <font color="#ff0000">widget</font> ，只是在不同场景的不同表述而已。
4. 由于 Flutter 主要就是用于构建用户界面的，所以，在大多数时候，可以认为 `widget` 就是一个控件，不必纠结于概念。
5. Flutter 中是通过 Widget 嵌套 Widget 的方式来构建 UI 和进行事件处理的，所以记住，<font color="#ff0000">Flutter 中万物皆为Widget。</font>

### ②、Widget 接口

1. 在 Flutter 中， `widget` 的功能是：描述一个 UI 元素的配置信息
2. 它就是说， `Widget` 其实并不是表示最终绘制在设备屏幕上的显示元素，所谓的配置信息就是 Widget 接收的参数，比如对于 `Text` 来讲，文本的内容、对齐方式、文本样式都是它的配置信息。
3. 下面我们先来看一下 `Widget` 类的声明：

```dart
@immutable // 不可变的
abstract class Widget extends DiagnosticableTree {
  const Widget({ this.key });

  final Key? key;

  @protected
  @factory
  Element createElement();

  @override
  String toStringShort() {
    final String type = objectRuntimeType(this, 'Widget');
    return key == null ? type : '$type-$key';
  }

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
    properties.defaultDiagnosticsTreeStyle = DiagnosticsTreeStyle.dense;
  }

  @override
  @nonVirtual
  bool operator ==(Object other) => super == other;

  @override
  @nonVirtual
  int get hashCode => super.hashCode;

  static bool canUpdate(Widget oldWidget, Widget newWidget) {
    return oldWidget.runtimeType == newWidget.runtimeType
        && oldWidget.key == newWidget.key;
  }
  ...
}
```

4. `@immutable`：代表 `Widget` 是不可变的，这会限制 `Widget` 中定义的属性（即配置信息）必须是不可变的（`final`），为什么不允许 `Widget` 中定义的属性变化呢？这是因为，Flutter 中如果属性发生变化则会重新构建 `Widget` 树，即重新创建新的 `Widget` 实例来替换旧的 `Widget` 实例，所以允许 `Widget` 的属性变化是没有意义的，因为一旦 `Widget` 自己的属性变了自己就会被替换。这也是为什么 `Widget` 中定义的属性必须是 final 的原因。
5. `DiagnosticableTree`：`widget` 类继承自 `DiagnosticableTree`，`DiagnosticableTree` 即“诊断树”，主要作用是提供调试信息。
6. `Key`：这个 key 属性类似于 `React/Vue` 中的 `key`，主要的作用是决定是否在下一次 `build` 时复用旧的 `widget` ，决定的条件在 `canUpdate()` 方法中。
7. `createElement()`：一个 `widget` 可以对应多个 Elemen；Flutter 框架在构建 UI 树时，会先调用此方法生成对应节点的 Element 对象。此方法是 Flutter 框架隐式调用的，在我们开发过程中基本不会调用到。
8. `debugFillProperties(...)`：复写父类的方法，主要是设置诊断树的一些特性。
9. `canUpdate(...)`：是一个静态方法，它主要用于在 `widget` 树重新 build 时复用旧的 `widget` ，其实具体来说，应该是：是否用新的 `widget` 对象去更新旧 UI 树上所对应的 Element 对象的配置；通过其源码我们可以看到，只要 `newWidget` 与 `oldWidget` 的 `runtimeType` 和 `key` 同时相等时就会用 `new widget` 去更新Element 对象的配置，否则就会创建新的 Element。
10. 有关 `Key` 和 `widget` 复用的细节将会在后面高级部分深入讨论，现在只需知道，为 `widget` 显式添加 `key` 的话可能（但不一定）会使 UI 在重新构建时变的高效，目前可以先忽略此参数，后面在用到时会详细解释 。
11. 另外 `Widget` 类本身是一个抽象类，其中最核心的就是定义了 `createElement()` 接口，在 Flutter 开发中，我们一般都不用直接继承 `Widget` 类来实现一个新组件，相反，我们通常会通过继承 `StatelessWidget` 或 `StatefulWidget` 来间接继承 `widget` 类来实现。
12. `StatelessWidget` 和 `StatefulWidget` 都是直接继承自 `Widget` 类，而这两个类也正是 Flutter 中非常重要的两个抽象类，它们引入了两种 widget 模型，接下来我们将重点介绍一下这两个类。

### ③、Flutter中的四棵树

1. 既然 `Widget` 只是描述一个 UI 元素的配置信息，那么真正的布局、绘制是由谁来完成的呢？Flutter 框架的处理流程是这样的：
	1. 根据 Widget 树生成一个 Element 树，Element 树中的节点都继承自 Element 类。
	2. 根据 Element 树生成 Render 树（渲染树），渲染树中的节点都继承自RenderObject 类。
	3. 根据渲染树生成 Layer 树，然后上屏显示，Layer 树中的节点都继承自 Layer 类。
2. 真正的布局和渲染逻辑在 Render 树中，Element 是 Widget 和 RenderObject 的粘合剂，可以理解为一个中间代理。我们通过一个例子来说明，假设有如下 Widget 树：

```dart
Container( // 一个容器 widget
  color: Colors.blue, // 设置容器背景色
  child: Row( // 可以将子widget沿水平方向排列
    children: [
      Image.network('https://www.example.com/1.png'), // 显示图片的 widget
      const Text('A'),
    ],
  ),
);
```

3. 注意，如果 Container 设置了背景色，Container 内部会创建一个新的 ColoredBox 来填充背景，相关逻辑如下

```dart
if (color != null)
  current = ColoredBox(color: color!, child: current);
```

4. 而 Image 内部会通过 RawImage 来渲染图片、Text 内部会通过 RichText 来渲染文本，所以最终的 Widget 树、Element 树、渲染树结构如图下所示：

![|850](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017092643.png)

5. 这里需要注意：
	1. 三棵树中，Widget 和 Element 是一一对应的，但并不和 RenderObject 一一对应。比如 `StatelessWidget` 和 `StatefulWidget` 都没有对应的 `RenderObject`。
	2. 渲染树在上屏前会生成一棵 Layer 树，这个我们将在后面原理篇介绍，在前面的章节中只需要记住以上三棵树就行。

### ④、StatelessWidget 无状态组件
#### Ⅰ、简介

1. `StatelessWidget` 相对比较简单，它继承自 `widget` 类，重写了 `createElement()` 方法

```dart
@override
StatelessElement createElement() => StatelessElement(this);
```

2. `StatelessElement` 间接继承自 `Element` 类，与 `StatelessWidget` 相对应（作为其配置数据）。
3. `StatelessWidget` 用于不需要维护状态的场景，它通常在 build 方法中通过嵌套其他 `widget` 来构建 UI，在构建过程中会递归的构建其嵌套的 `widget` 。我们看一个简单的例子：

```dart
class Echo extends StatelessWidget  {
  const Echo({
    Key? key,  
    required this.text,
    this.backgroundColor = Colors.grey, //默认为灰色
  }):super(key:key);
    
  final String text;
  final Color backgroundColor;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        color: backgroundColor,
        child: Text(text),
      ),
    );
  }
}
```

4. 上面的代码，实现了一个回显字符串的 Echo widget 。
	1. 按照惯例，`widget` 的构造函数参数应使用命名参数，命名参数中的必需要传的参数要添加 `required` 关键字，这样有利于静态代码分析器进行检查；
	2. 在继承 `widget` 时，第一个参数通常应该是 `Key`。另外，如果 `widget` 需要接收子 `widget` ，那么 `child` 或 `children` 参数通常应被放在参数列表的最后。
	3. 同样是按照惯例， `widget` 的属性应尽可能的被声明为 `final`，防止被意外改变。
5. 然后我们可以通过如下方式使用它

```dart
 Widget build(BuildContext context) {
  return Echo(text: "hello world");
}
```

6. 运行后效果：

![|300](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017093352.png)

#### Ⅱ、Context

1. `build` 方法有一个 `context` 参数，它是 `BuildContext` 类的一个实例，表示当前 `widget` 在 `widget` 树中的上下文，每一个 `widget` 都会对应一个 `context` 对象（因为每一个 `widget` 都是 `widget` 树上的一个节点）。
2. 实际上，`context` 是当前 `widget` 在 `widget` 树中位置中执行”相关操作“的一个句柄(handle)，比如它提供了从当前 `widget` 开始向上遍历 `widget` 树以及按照 `widget` 类型查找父级 `widget` 的方法。下面是在子树中获取父级 widget 的一个示例：

```dart
class ContextRoute extends StatelessWidget  {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Context测试"),
      ),
      /**
	   * body: 用于定义页面的主要内容区域
	   * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	   * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	   */
      body: Container(
        child: Builder(builder: (context) {
          // 在 widget 树中向上查找最近的父级`Scaffold`  widget 
          Scaffold scaffold = context.findAncestorWidgetOfExactType<Scaffold>();
          // 直接返回 AppBar的title， 此处实际上是Text("Context测试")
          return (scaffold.appBar as AppBar).title;
        }),
      ),
    );
  }
}
```

3. 运行后效果如图：

![|420](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017093716.png)

### ⑤、StatefulWidget 有状态组件

1. 和 `StatelessWidget` 一样，`StatefulWidget` 也是继承自 `widget` 类，并重写了 `createElement()` 方法，不同的是返回的 `Element` 对象并不相同；另外 `StatefulWidget类` 中添加了一个新的接口 `createState()`。
2. 下面我们看看StatefulWidget的类定义：

```dart
abstract class StatefulWidget extends Widget {
  const StatefulWidget({ Key key }) : super(key: key);
    
  @override
  StatefulElement createElement() => StatefulElement(this);
    
  @protected
  State createState();
}
```

3. `StatefulElement` 间接继承自 Element 类，与 `StatefulWidget` 相对应（作为其配置数据）。`StatefulElement` 中可能会多次调用 `createState()` 来创建状态（State）对象。
4. `createState()` 用于创建和 `StatefulWidget` 相关的状态，它在 `StatefulWidget` 的生命周期中可能会被多次调用。
5. 例如，当一个 `StatefulWidget` 同时插入到 `widget` 树的多个位置时，Flutter 框架就会调用该方法为每一个位置生成一个独立的 `State` 实例，其实，本质上就是一个 `StatefulElement` 对应一个 `State` 实例。
6. 而在 `StatefulWidget` 中，`State` 对象和 `StatefulElement` 具有一一对应的关系，所以在 Flutter 的 SDK 文档中，可以经常看到“从树中移除 `State` 对象”或“插入 `State` 对象到树中”这样的描述，此时的树指通过 widget 树生成的 Element 树。
7. Flutter 的 SDK 文档中经常会提到“树” ，我们可以根据语境来判断到底指的是哪棵树。其实，无论是哪棵树，最终的目标都是为了描述 UI 的结构和绘制信息，所以在 Flutter 中遇到“树”的概念时，若无特别说明，我们都可以理解为 “一棵构成用户界面的节点树”

### ⑥、State 状态

#### Ⅰ、简介

1. 一个 `StatefulWidget` 类会对应一个 `State` 类，`State` 表示与其对应的 `StatefulWidget` 要维护的状态，`State` 中的保存的状态信息可以：
	1. 在 `widget` 构建时可以被同步读取。
	2. 在 `widget` 生命周期中可以被改变，当 `State` 被改变时，可以手动调用其 `setState()` 方法通知 Flutter 框架状态发生改变，Flutter 框架在收到消息后，会重新调用其 build 方法重新构建 `widget` 树，从而达到更新 UI 的目的。
2. `State` 中有两个常用属性：
	1. `widget`，它表示与该 `State` 实例关联的 `widget` 实例，由 Flutter 框架动态设置。注意，这种关联并非永久的，因为在应用生命周期中，UI 树上的某一个节点的 widget 实例在重新构建时可能会变化，但 State 实例只会在第一次插入到树中时被创建，当在重新构建时，如果 widget 被修改了，Flutter 框架会动态设置 `State. widget` 为新的 `widget` 实例。
	2. `context`：`StatefulWidget` 对应的 `BuildContext`，作用同 `StatelessWidget` 的 `BuildContext`。

#### Ⅱ、State 生命周期

1. 理解 `State` 的生命周期对 flutter 开发非常重要，为了加深印象，本节通过一个实例来演示一下 `State` 的生命周期。在接下来的示例中，以计数器功能为例，实现一个计数器 CounterWidget 组件 ，点击它可以使计数器加 1，由于要保存计数器的数值状态，所以我们应继承 `StatefulWidget`，代码如下

```dart
class CounterWidget extends StatefulWidget {
  const CounterWidget({Key? key, this.initValue = 0});

  final int initValue;

  @override
  _CounterWidgetState createState() => _CounterWidgetState();
}
```

2. `CounterWidget` 接收一个 `initValue` 整型参数，它表示计数器的初始值。下面我们看一下 `State` 的代码：

```dart
class _CounterWidgetState extends State<CounterWidget> {
  int _counter = 0;

  @override
  void initState() {
    super.initState();
    //初始化状态
    _counter = widget.initValue;
    print("initState");
  }

  @override
  Widget build(BuildContext context) {
    print("build");
    return Scaffold(
      /**
	   * body: 用于定义页面的主要内容区域
	   * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	   * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	   */
      body: Center(
        child: TextButton(
          child: Text('$_counter'),
          //点击后计数器自增
          onPressed: () => setState(
            () => ++_counter,
          ),
        ),
      ),
    );
  }

  @override
  void didUpdateWidget(CounterWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    print("didUpdateWidget ");
  }

  @override
  void deactivate() {
    super.deactivate();
    print("deactivate");
  }

  @override
  void dispose() {
    super.dispose();
    print("dispose");
  }

  @override
  void reassemble() {
    super.reassemble();
    print("reassemble");
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    print("didChangeDependencies");
  }
}
```

3. 接下来，我们创建一个新路由，在新路由中，我们只显示一个 `CounterWidget`

```dart
class StateLifecycleTest extends StatelessWidget {
  const StateLifecycleTest({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CounterWidget();
  }
}
```

4. 我们运行应用并打开该路由页面，在新路由页打开后，屏幕中央就会出现一个数字 0，然后控制台日志输出：

```dart
I/flutter ( 5436): initState
I/flutter ( 5436): didChangeDependencies
I/flutter ( 5436): build
```

5. 可以看到，在 `StatefulWidget` 插入到 `widget` 树时首先 `initState` 方法会被调用。然后我们点击⚡️按钮热重载，控制台输出日志如下：

```dart
I/flutter ( 5436): reassemble
I/flutter ( 5436): didUpdateWidget 
I/flutter ( 5436): build
```

6. 可以看到此时 `initState` 和 `didChangeDependencies` 都没有被调用，而此时 `didUpdateWidget` 被调用。接下来，我们在 `widget` 树中移除 `CounterWidget`，将 `StateLifecycleTest` 的 build 方法改为：

```dart
 Widget build(BuildContext context) {
  //移除计数器 
  //return CounterWidget ();
  //随便返回一个Text()
  return Text("xxx");
}
```

7. 然后热重载，日志如下：

```dart
I/flutter ( 5436): reassemble
I/flutter ( 5436): deactive
I/flutter ( 5436): dispose
```

8. 我们可以看到，在 `CounterWidget` 从 `widget` 树中移除时，`deactive` 和 `dispose` 会依次被调用。
9. 下面我们来看看各个回调函数：
	1. `initState`：当 `widget` 第一次插入到 `widget` 树时会被调用，对于每一个 `State` 对象，Flutter 框架只会调用一次该回调，所以，通常在该回调中做一些一次性的操作，如状态初始化、订阅子树的事件通知等。不能在该回调中调用 `BuildContext.dependOnInheritedWidgetOfExactType`（该方法用于在 `widget` 树上获取离当前 `widget` 最近的一个父级 `InheritedWidget`，关于 `InheritedWidget` 我们将在后面章节介绍），原因是在初始化完成后，`widget` 树中的 `InheritFrom widget` 也可能会发生变化，所以正确的做法应该在在 `build()` 方法或 `didChangeDependencies()` 中调用它。
	2. `didChangeDependencies()`：当 `State` 对象的依赖发生变化时会被调用；例如：在之前 `build()` 中包含了一个 `InheritedWidget` ，然后在之后的 `build()` 中 `Inherited widget` 发生了变化，`那么此时InheritedWidget` 的子 `widget` 的 `didChangeDependencies()` 回调都会被调用。典型的场景是当系统语言 Locale 或应用主题改变时，Flutter 框架会通知 `widget` 调用此回调。需要注意，组件第一次被创建后挂载的时候（包括重创建）对应的 `didChangeDependencies` 也会被调用。
	3. `build()`：它主要是用于构建 `widget` 子树的，会在如下场景被调用：
		1. 在调用 `initState()` 之后。
		2. 在调用 `didUpdateWidget()` 之后。
		3. 在调用 `setState()` 之后。
		4. 在调用 `didChangeDependencies()` 之后。
		5. 在 `State` 对象从树中一个位置移除后（会调用 `deactivate`）又重新插入到树的其他位置之后。
	4. `reassemble()`：此回调是专门为了开发调试而提供的，在热重载(hot reload)时会被调用，此回调在 `Release` 模式下永远不会被调用。
	5. `didUpdateWidget()`：在 `widget` 重新构建时，Flutter 框架会调用 `widget.canUpdate` 来检测 `widget` 树中同一位置的新旧节点，然后决定是否需要更新，如果 `widget.canUpdate` 返回 true 则会调用此回调。正如之前所述，`widget.canUpdate` 会在新旧 `widget` 的 `key` 和 `runtimeType` 同时相等时会返回 `true`，也就是说在在新旧 `widget` 的 `key` 和 `runtimeType` 同时相等时 `didUpdateWidget()` 就会被调用。
	6. `deactivate()`：当 `State` 对象从树中被移除时，会调用此回调。在一些场景下，Flutter 框架会将 `State` 对象重新插到树中，如包含此 `State` 对象的子树在树的一个位置移动到另一个位置时（可以通过GlobalKey 来实现）。如果移除后没有重新插入到树中则紧接着会调用 `dispose()` 方法。
	7. `dispose()`：当 `State` 对象从树中被永久移除时调用；通常在此回调中释放资源。
10. `StatefulWidget` 生命周期如图所示：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017100448.png)

### ⑦、在 widget 树中获取State对象

1. 由于 `StatefulWidget` 的具体逻辑都在其 `State` 中，所以很多时候，我们需要获取 `StatefulWidget` 对应的 `State` 对象来调用一些方法，比如 `Scaffold` 组件对应的状态类 `ScaffoldState` 中就定义了打开 `SnackBar`（路由页底部提示条）的方法。
2. 我们有两种方法在子 `widget` 树中获取父级 `StatefulWidget` 的 `State` 对象

#### Ⅰ、通过 Context 获取

1. `context` 对象有一个 `findAncestorStateOfType()` 方法，该方法可以从当前节点沿着 `widget` 树向上查找指定类型的 `StatefulWidget` 对应的 `State` 对象。下面是实现打开 SnackBar 的示例：

```dart
class GetStateObjectRoute extends StatefulWidget {
  const GetStateObjectRoute({Key? key}) : super(key: key);

  @override
  State<GetStateObjectRoute> createState() => _GetStateObjectRouteState();
}

class _GetStateObjectRouteState extends State<GetStateObjectRoute> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("子树中获取State对象"),
      ),
      /**
	   * body: 用于定义页面的主要内容区域
	   * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	   * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	   */
      body: Center(
        child: Column(
          children: [
            Builder(builder: (context) {
              return ElevatedButton(
                onPressed: () {
                  // 查找父级最近的Scaffold对应的ScaffoldState对象
                  ScaffoldState _state = context.findAncestorStateOfType<ScaffoldState>()!;
                  // 打开抽屉菜单
                  _state.openDrawer();
                },
                child: Text('打开抽屉菜单1'),
              );
            }),
          ],
        ),
      ),
      drawer: Drawer(),
    );
  }
}
```

2. 一般来说，如果 `StatefulWidget` 的状态是私有的（不应该向外部暴露），那么我们代码中就不应该去直接获取其 `State` 对象；如果 `StatefulWidget` 的状态是希望暴露出的（通常还有一些组件的操作方法），我们则可以去直接获取其 `State` 对象。
3. 但是通过 `context.findAncestorStateOfType` 获取 `StatefulWidget` 的状态的方法是通用的，我们并不能在语法层面指定 `StatefulWidget` 的状态是否私有，所以在 Flutter 开发中便有了一个默认的约定：如果 `StatefulWidget` 的状态是希望暴露出的，应当在 `StatefulWidget` 中提供一个 `of` 静态方法来获取其 `State` 对象，开发者便可直接通过该方法来获取；
4. 如果 `State` 不希望暴露，则不提供 `of` 方法。这个约定在 Flutter SDK 里随处可见。
5. 所以，上面示例中的 `Scaffold` 也提供了一个 `of` 方法，我们其实是可以直接调用它的：

```dart
Builder(builder: (context) {
  return ElevatedButton(
    onPressed: () {
      // 直接通过of静态方法来获取ScaffoldState
      ScaffoldState _state=Scaffold.of(context);
      // 打开抽屉菜单
      _state.openDrawer();
    },
    child: Text('打开抽屉菜单2'),
  );
}),
```

6. 又比如我们想显示 snack bar 的话可以通过下面代码调用：

```dart
Builder(builder: (context) {
  return ElevatedButton(
    onPressed: () {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("我是SnackBar")),
      );
    },
    child: Text('显示SnackBar'),
  );
}),
```

7. 上面示例运行后，点击”显示SnackBar“，效果如图所示：

![|400](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017101253.png)

#### Ⅱ、通过 GlobalKey

Flutter 还有一种通用的获取 `State` 对象的方法：通过 `GlobalKey` 来获取；步骤分两步：

1. 给目标 `StatefulWidget` 添加 GlobalKey。

```dart
//定义一个globalKey, 由于GlobalKey要保持全局唯一性，我们使用静态变量存储
static GlobalKey<ScaffoldState> _globalKey= GlobalKey();
...
Scaffold(
    key: _globalKey , //设置key
    ...  
)
```

2. 通过 `GlobalKey` 来获取 `State` 对象

```dart
_globalKey.currentState.openDrawer()
```

3. `GlobalKey` 是 Flutter 提供的一种在整个 App 中引用 element 的机制。如果一个 `widget` 设置了 `GlobalKey`，那么我们便可以通过 `globalKey.currentWidget` 获得该 `widget` 对象、`globalKey.currentElement` 来获得 `widget` 对应的 `element` 对象，如果当前 `widget` 是 `StatefulWidget`，则可以通过 `globalKey.currentState` 来获得该 `widget` 对应的 `state` 对象。
4. 注意：使用 `GlobalKey` 开销较大，如果有其他可选方案，应尽量避免使用它。另外，同一个 `GlobalKey` 在整个 `widget` 树中必须是唯一的，不能重复。

### ⑧、通过 RenderObject 自定义 Widget

1. `StatelessWidget` 和 `StatefulWidget` 都是用于组合其他组件的，它们本身没有对应的 `RenderObject`。
2. Flutter 组件库中的很多基础组件都不是通过 `StatelessWidget` 和 `StatefulWidget` 来实现的，比如 `Text` 、`Column`、`Align` 等，就好比搭积木，`StatelessWidget` 和 `StatefulWidget` 可以将积木搭成不同的样子，但前提是得有积木，而这些积木都是通过自定义 `RenderObject` 来实现的。
3. 实际上 Flutter 最原始的定义组件的方式就是通过定义 `RenderObject` 来实现，而 `StatelessWidget` 和 `StatefulWidget` 只是提供的两个帮助类。
4. 下面我们简单演示一下通过 `RenderObject` 定义组件的方式：

```dart
class CustomWidget extends LeafRenderObjectWidget{
  @override
  RenderObject createRenderObject(BuildContext context) {
    // 创建 RenderObject
    return RenderCustomObject();
  }
  @override
  void updateRenderObject(BuildContext context, RenderCustomObject  renderObject) {
    // 更新 RenderObject
    super.updateRenderObject(context, renderObject);
  }
}

class RenderCustomObject extends RenderBox{

  @override
  void performLayout() {
    // 实现布局逻辑
  }

  @override
  void paint(PaintingContext context, Offset offset) {
    // 实现绘制
  }
}
```

5. 如果组件不会包含子组件，则我们可以直接继承自 `LeafRenderObjectWidget` ，它是 `RenderObjectWidget` 的子类，而 `RenderObjectWidget` 继承自 `Widget` ，我们可以看一下它的实现：

```dart
abstract class LeafRenderObjectWidget extends RenderObjectWidget {
  const LeafRenderObjectWidget({ Key? key }) : super(key: key);

  @override
  LeafRenderObjectElement createElement() => LeafRenderObjectElement(this);
}
```

6. 很简单，就是帮 `widget` 实现了 `createElement` 方法，它会为组件创建一个类型为 `LeafRenderObjectElement` 的 `Element` 对象。
7. 如果自定义的 `widget` 可以包含子组件，则可以根据子组件的数量来选择继承 `SingleChildRenderObjectWidget` 或 `MultiChildRenderObjectWidget`，它们也实现了 `createElement()` 方法，返回不同类型的 `Element` 对象。
8. 然后我们重写了 `createRenderObject` 方法，它是 `RenderObjectWidget` 中定义方法，该方法被组件对应的 `Element` 调用（构建渲染树时）用于生成渲染对象。我们的主要任务就是来实现 `createRenderObject` 返回的渲染对象类，本例中是 `RenderCustomObject` 。
9. `updateRenderObject` 方法是用于在组件树状态发生变化但不需要重新创建 `RenderObject` 时用于更新组件渲染对象的回调。
10. `RenderCustomObject` 类是继承自 `RenderBox`，而 `RenderBox` 继承自 `RenderObject`，我们需要在 `RenderCustomObject` 中实现布局、绘制、事件响应等逻辑，关于如何实现这些逻辑，涉及到的知识点会贯穿全文

### ⑨、Flutter SDK 内置组件库介绍

Flutter 提供了一套丰富、强大的基础组件，在基础组件库之上 Flutter 又提供了一套 Material 风格（ Android 默认的视觉风格）和一套 Cupertino 风格（iOS 视觉风格）的组件库。要使用基础组件库，需要先导入：

```dart
import 'package:flutter/widgets.dart';
```

#### Ⅰ、基础组件

1. `Text`：该组件可以创建一个带格式的文本。
2. `Row`、 `Column`： 
	1. 这些具有弹性空间的布局类 `widget` 可以在水平（Row）和垂直（Column）方向上创建灵活的布局。
	2. 其设计是基于 Web 开发中的 Flexbox 布局模型。
3. `Stack`： 
	1. 取代线性布局 (译者语：和 Android 中的 FrameLayout 相似)
	2. [Stack](https://docs.flutter.dev/flutter/ widgets/Stack-class.html) 允许子 `widget` 堆叠， 可以使用 `Positioned` 来定位他们相对于 `Stack` 的上下左右四条边的位置。
	3. `Stacks` 是基于 Web 开发中的绝对定位（absolute positioning )布局模型设计的。
4. `Container ： 
	1. 可以创建矩形视觉元素。
	2. `Container` 可以装饰一个 `BoxDecoration` ，如 `background`、一个边框、或者一个阴影。 
	3. `Container` 也可以具有边距（margins）、填充(padding) 和应用于其大小的约束(constraints)。
	4. 另外， `Container` 可以使用矩阵在三维空间中对其进行变换。

#### Ⅱ、Material 组件

1. Flutter 提供了一套丰富的 `Material` 组件，它可以帮助我们构建遵循 Material Design 设计规范的应用程序。
2. Material 应用程序以 MaterialApp 组件开始，该组件在应用程序的根部创建了一些必要的组件，比如 `Theme` 组件，它用于配置应用的主题。 
3. 是否使用 MaterialApp 完全是可选的，但是使用它是一个很好的做法。
4. 在之前的示例中，我们已经使用过多个 Material 组件了，如：`Scaffold`、`AppBar`、`TextButton` 等。
5. 要使用 Material 组件，需要先引入它：

```dart
import 'package:flutter/material.dart';
```

#### Ⅲ、Cupertino 组件

1. Flutter 也提供了一套丰富的 Cupertino 风格的组件，尽管目前还没有 Material 组件那么丰富，但是它仍在不断的完善中。
2. 值得一提的是在 Material 组件库中有一些组件可以根据实际运行平台来切换表现风格，比如 `MaterialPageRoute`
	1. 在路由切换时，如果是 Android 系统，它将会使用 Android 系统默认的页面切换动画(从底向上)；
	2. 如果是 iOS 系统，它会使用 iOS 系统默认的页面切换动画（从右向左）。
3. 由于在前面的示例中还没有 Cupertino 组件的示例，下面我们实现一个简单的 Cupertino 组件风格的页面：

```dart
//导入cupertino  widget 库
import 'package:flutter/cupertino.dart';

class CupertinoTestRoute extends StatelessWidget  {
  const CupertinoTestRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CupertinoPageScaffold(
      navigationBar: const CupertinoNavigationBar(
        middle: Text("Cupertino Demo"),
      ),
      child: Center(
        child: CupertinoButton(
            color: CupertinoColors.activeBlue,
            child: const Text("Press"),
            onPressed: () {}
        ),
      ),
    );
  }
}
```

4. 下面是在 iPhoneX 上页面效果截图：

![|400](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017104451.png)

### ⑩、总结

1. Flutter 的 `widget` 类型分为 `StatefulWidget` 和 `StatelessWidget` 两种，需要深入理解它们的区别，`widget` 将是我们构建 Flutter 应用的基石。
2. Flutter 提供了丰富的组件，在实际的开发中我们可以根据需要随意使用它们，而不必担心引入过多组件库会让你的应用安装包变大，这不是 web 开发，dart 在编译时只会编译你使用了的代码。
3. 由于 Material 和 Cupertino 都是在基础组件库之上的，所以如果我们的应用中引入了这两者之一，则不需要再引入 `flutter/widgets.dart` 了，因为它们内部已经引入过了。
4. 另外需要说明一点，本章后面章节的示例中会使用一些布局类组件，如 `Scaffold`、`Row`、`Column` 等，这些组件将在后面“布局类组件”一章中详细介绍，可以先不用关注。

## 3、状态管理

### ①、简介

1. 响应式的编程框架中都会有一个永恒的主题：状态(State)管理，无论是在 `React/Vue`（两者都是支持响应式编程的 Web 开发框架）还是 Flutter 中，他们讨论的问题和解决的思想都是一致的。
2. 言归正传，我们想一个问题，`StatefulWidget` 的状态应该被谁管理？Widget 本身？父 Widget ？都会？还是另一个对象？答案是取决于实际情况！以下是管理状态的最常见的方法：
	1. Widget 管理自己的状态。
	2. Widget 管理子 Widget 状态。
	3. 混合管理（父 Widget 和子 Widget 都管理状态）。
3. 如何决定使用哪种管理方法？下面是官方给出的一些原则可以帮助你做决定：
	1. 如果状态是有关界面外观效果的，例如颜色、动画，那么状态最好由 Widget 本身来管理。
	2. 如果状态是用户数据，如复选框的选中状态、滑块的位置，则该状态最好由父 Widget 管理。
	3. 如果某一个状态是不同 Widget 共享的则最好由它们共同的父 Widget 管理。
4. 在 Widget 内部管理状态封装性会好一些，而在父 Widget 中管理会比较灵活。有些时候，如果不确定到底该怎么管理状态，那么推荐的首选是在父 Widget 中管理（灵活会显得更重要一些）。
5. 接下来，我们将通过创建三个简单示例 TapboxA、TapboxB 和 TapboxC 来说明管理状态的不同方式。 
6. 这些例子功能是相似的：创建一个盒子，当点击它时，盒子背景会在绿色与灰色之间切换。状态 `_active` 确定颜色：绿色为 true ，灰色为 false，如图所示：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231115152243.png)

7. 下面的例子将使用 `GestureDetector` 来识别点击事件，关于该 `GestureDetector` 的详细内容我们将在后面“事件处理”一章中介绍

### ②、Widget 管理自身状态

1. 我们实现一个 `TapboxA`，在它对应的 `_TapboxAState` 类：
2. 管理 `TapboxA` 的状态。
3. 定义 `_active`：确定盒子的当前颜色的布尔值。
4. 定义 `_handleTap()` 函数，该函数在点击该盒子时更新 `_active`，并调用 `setState()` 更新 UI。
5. 实现 widget 的所有交互式行为。

```dart
import 'package:flutter/material.dart';

import '00_基础知识/02_状态管理/01_TapboxA.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: TapboxA(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TapboxA extends StatefulWidget {
  const TapboxA({super.key});

  @override
  _TapboxAState createState() => _TapboxAState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _TapboxAState extends State<TapboxA> {
  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击
  bool _active = false;

  @override
  Widget build(BuildContext context) {
    // GestureDetector 是一个用于手势识别的小部件
    return GestureDetector(
      // 当用户点击 Container 时，会调用 _handleTap() 方法
      onTap: _handleTap,
      // Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
      child: Center(
        // Container 是一个组合类小部件，它本身不对应具体的渲染器，它是 DecoratedBox、ConstrainedBox、Transform、Padding、Align 等小部件组合的一个多功能容器。
        child: Container(
          width: 200,
          height: 200,
          // 设置背景颜色，当 _active 为 true 时为绿色，为 false 时为灰色
          color: _active ? Colors.lightGreen[700] : Colors.grey[600],
          // 当 _active 为 true 时，显示 Active，为 false 时，显示 Inactive
          child: Center(child: Text(_active ? 'Active' : 'Inactive',))
        ),
      )
    );
  }

  // 定义一个私有方法，用于处理点击事件，点击时将 _active 取反，然后调用 setState() 方法更新 UI
  void _handleTap() {
    setState(() {
      _active = !_active;
    });
  }

}
```

6. 效果：

![|416](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画8.gif)

### ③、父 Widget 管理子 Widget 的状态

1. 对于父 Widget 来说，管理状态并告诉其子 Widget 何时更新通常是比较好的方式。 
2. 例如，`IconButton` 是一个图标按钮，但它是一个无状态的 Widget，因为我们认为父 Widget 需要知道该按钮是否被点击来采取相应的处理。
3. 在以下示例中，`TapboxB` 通过回调将其状态导出到其父组件，状态由父组件管理，因此它的父组件为 `StatefulWidget`。但是由于 `TapboxB` 不管理任何状态，所以 `TapboxB` 为 `StatelessWidget`。
4. `ParentBWidgetState` 类:
	1. 为 `TapboxB` 管理 `_active` 状态。
	2. 实现 `_handleTapboxChanged()`，当盒子被点击时调用的方法。
	3. 当状态改变时，调用 `setState()` 更新 UI。

```dart
import 'package:flutter/material.dart';

import '02_2_TapboxB.dart';

// 创建一个 StatefulWidget 类
class ParentBWidget extends StatefulWidget {
  const ParentBWidget({super.key});

  @override
  _ParentBWidgetState createState() => _ParentBWidgetState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _ParentBWidgetState extends State<ParentBWidget> {
  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击
  bool _active = false;

  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
    return Center(
      /**
       * TapboxB 是一个自定义的小部件，它继承自 StatefulWidget，实现了一个点击时会变色的按钮，它的状态由父组件管理
       * 两个参数 active 和 onChanged 由父组件管理，当点击时，会调用父组件的 _handleTapboxChanged() 方法，更新 _active 的值，从而更新 UI
       */
      child: TapboxB(
        active: _active,
        onChanged: _handleTapboxChanged,
      ),
    );
  }

  // 定义一个私有方法，用于处理点击事件，点击时将 _active 取反，然后调用 setState() 方法更新 UI
  void _handleTapboxChanged(bool newValue) {
    setState(() {
      _active = newValue;
    });
  }

}
```

5. TapboxB 类：
	1. 继承 `StatelessWidget` 类，因为所有状态都由其父组件处理。
	2. 当检测到点击时，它会通知父组件。

```dart
import 'package:flutter/material.dart';

// 创建一个 StatelessWidget 类
class TapboxB extends StatelessWidget {
  const TapboxB({super.key, required this.active, required this.onChanged});

  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击，由父组件传递
  final bool active;
  // 定义一个 ValueChanged<bool> 类型的变量，用于保存点击事件的回调，由父组件传递
  final ValueChanged<bool> onChanged;

  @override
  Widget build(BuildContext context) {
    // GestureDetector 是一个用于手势识别的小部件
    return GestureDetector(
      // 当用户点击 Container 时，会调用 _handleTap() 方法
      onTap: _handleTap,
      // Container 是一个组合类小部件，它本身不对应具体的渲染器，它是 DecoratedBox、ConstrainedBox、Transform、Padding、Align 等小部件组合的一个多功能容器。
      child: Container(
        width: 200,
        height: 200,
        // 设置背景颜色，当 _active 为 true 时为绿色，为 false 时为灰色
        color: active ? Colors.lightGreen[700] : Colors.grey[600],
        // 当 _active 为 true 时，显示 Active，为 false 时，显示 Inactive
        child: Center(child: Text(active ? 'Active 2' : 'Inactive 2',))
      ),
    );
  }

  // 调用 onChanged() 方法，将 _active 的值传递给父组件，从而更新 UI
  void _handleTap() {
    // 调用 onChanged() 方法，将 _active 的值传递给父组件，从而更新 UI
    onChanged(!active);
  }

}
```

6. `main` 入口方法

```dart
import 'package:flutter/material.dart';

import '00_基础知识/02_状态管理/02_1_ParentBWidget.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ParentBWidget(),
      )
    );
  }
}
```

7. 效果：

![|416](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画9.gif)

### ④、混合状态管理

1. 对于一些组件来说，混合管理的方式会非常有用。在这种情况下，组件自身管理一些内部状态，而父组件管理一些其他外部状态。
2. 在下面 `TapboxC` 示例中，手指按下时，盒子的周围会出现一个深绿色的边框，抬起时，边框消失。点击完成后，盒子的颜色改变。 `TapboxC` 将其 `_active` 状态导出到其父组件中，但在内部管理其 `_highlight` 状态。这个例子有两个状态对象 `_ParentCWidgetState` 和 `_TapboxCState`。
3. `_ParentCWidgetStateC`类：
	1. 管理 `_active` 状态。
	2. 实现 `_handleTapboxChanged()` ，当盒子被点击时调用。
	3. 当点击盒子并且 `_active` 状态改变时调用 `setState()` 更新 UI。

```dart
import 'package:flutter/material.dart';

import '03_2_TapboxC.dart';


// 创建一个 StatefulWidget 类
class ParentCWidget extends StatefulWidget {
  const ParentCWidget({super.key});

  @override
  _ParentCWidgetState createState() => _ParentCWidgetState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _ParentCWidgetState extends State<ParentCWidget> {
  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击
  bool _active = false;

  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
    return Center(
      /**
       * TapboxB 是一个自定义的小部件，它继承自 StatefulWidget，实现了一个点击时会变色的按钮，它的状态由父组件管理
       * 两个参数 active 和 onChanged 由父组件管理，当点击时，会调用父组件的 _handleTapboxChanged() 方法，更新 _active 的值，从而更新 UI
       */
      child: TapboxC(
        active: _active,
        onChanged: _handleTapboxChanged,
      ),
    );
  }

  // 定义一个私有方法，用于处理点击事件，点击时将 _active 取反，然后调用 setState() 方法更新 UI
  void _handleTapboxChanged(bool newValue) {
    setState(() {
      _active = newValue;
    });
  }

}
```

4. `_TapboxCState` 对象:
	1. 管理 `_highlight` 状态。
	2. `GestureDetector` 监听所有 `tap` 事件。当用户点下时，它添加高亮（深绿色边框）；当用户释放时，会移除高亮。
	3. 当按下、抬起、或者取消点击时更新  `_highlight` 状态，调用 `setState()`更新 UI。
	4. 当点击时，将状态的改变传递给父组件。

```dart
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TapboxC extends StatefulWidget {
  const TapboxC({super.key, required this.active, required this.onChanged});

  @override
  _TapboxCState createState() => _TapboxCState();

  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击，由父组件传递
  final bool active;
  // 定义一个 ValueChanged<bool> 类型的变量，用于保存点击事件的回调，由父组件传递
  final ValueChanged<bool> onChanged;
}

// 创建与上述 StatefulWidget 相关的状态类
class _TapboxCState extends State<TapboxC> {
  // 定义一个布尔类型的变量，用于保存当前按钮是否被点击
  bool _highlight = false;

  @override
  Widget build(BuildContext context) {
    // GestureDetector 是一个用于手势识别的小部件
    return GestureDetector(
      // 处理按下事件
      onTapDown: _handleTapDown,
      // 处理抬起事件
      onTapUp: _handleTapUp,
      // 处理点击事件，比如说，用户按下按钮，然后抬起手指，此时就会触发点击事件
      onTap: _handleTap,
      // 处理取消事件，比如说，用户按下按钮，但是没有抬起手指，而是移动了手指，此时就会触发取消事件
      onTapCancel: _handleTapCancel,
      // Container 是一个组合类小部件，它本身不对应具体的渲染器，它是 DecoratedBox、ConstrainedBox、Transform、Padding、Align 等小部件组合的一个多功能容器。
      child: Container(
        width: 200,
        height: 200,
        // BoxDecoration 是一个装饰类小部件，它可以在其子小部件之上绘制一个装饰，如背景、边框、渐变等。
        decoration: BoxDecoration(
          // 设置背景颜色，当 _active 为 true 时为绿色，为 false 时为灰色
          color: widget.active ? Colors.lightGreen[700] : Colors.grey[600],
          // 设置边框，当 _highlight 为 true 时，边框宽度为 10，颜色为深绿色，否则边框宽度为 0，颜色为透明
          border: _highlight ? Border.all(color: Colors.teal[700]!, width: 10.0) : null,
        ),
        // 当 _active 为 true 时，显示 Active，为 false 时，显示 Inactive
        child: Center(child: Text(widget.active ? 'Active 3' : 'Inactive 3',)),
      ),
    );
  }

  // 定义一个私有方法，用于处理按下事件，当按下时，将 _highlight 设置为 true，表示显示深绿色边框
  void _handleTapDown(TapDownDetails details) {
    setState(() {
      _highlight = true;
    });
  }

  // 定义一个私有方法，用于处理抬起事件，当抬起时，将 _highlight 设置为 false，表示隐藏深绿色边框
  void _handleTapUp(TapUpDetails details) {
    setState(() {
      _highlight = false;
    });
  }

  // 定义一个私有方法，用于处理取消事件，当取消时，将 _highlight 设置为 false，表示隐藏深绿色边框
  void _handleTapCancel() {
    setState(() {
      _highlight = false;
    });
  }

  /// 定义一个私有方法，用于处理点击事件，当点击时，调用 widget.onChanged() 方法
  /// 将盒子的状态取反，使其在点击时可以切换状态，使背景在灰色和绿色之间切换，内容文本在 Inactive 和 Active 之间切换
  void _handleTap() {
    widget.onChanged(!widget.active);
  }

}
```

5. `main` 入口方法

```dart
import 'package:flutter/material.dart';

import '00_基础知识/02_状态管理/03_1_ParentCWidget.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ParentCWidget(),
      )
    );
  }
}
```

6. 效果：

![|416](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画10.gif)

7. 另一种实现可能会将高亮状态导出到父组件，但同时保持 `_active` 状态为内部状态，但如果你要将该 `TapBox` 给其他人使用，可能没有什么意义。 开发人员只会关心该框是否处于 Active 状态，而不在乎高亮显示是如何管理的，所以应该让 TapBox 内部处理这些细节。

### ⑤、全局状态管理

1. 当应用中需要一些跨组件（包括跨路由）的状态需要同步时，上面介绍的方法便很难胜任了。
2. 比如，我们有一个设置页，里面可以设置应用的语言，我们为了让设置实时生效，我们期望在语言状态发生改变时，App 中依赖应用语言的组件能够重新 `build` 一下，但这些依赖应用语言的组件和设置页并不在一起，所以这种情况用上面的方法很难管理。
3. 这时，正确的做法是通过一个全局状态管理器来处理这种相距较远的组件之间的通信。目前主要有两种办法：
	1. 实现一个全局的事件总线，将语言状态改变对应为一个事件，然后在 APP 中依赖应用语言的组件的 `initState` 方法中订阅语言改变的事件。当用户在设置页切换语言后，我们发布语言改变事件，而订阅了此事件的组件就会收到通知，收到通知后调用 `setState(...)` 方法重新 build 一下自身即可。
	2. 使用一些专门用于状态管理的包，如 `Provider`、`Redux`，可以在 pub 上查看其详细信息。
4. 下面将在"功能型组件"一章中介绍 `Provider` 包的实现原理及用法，同时也将会在"事件处理与通知"一章中实现一个全局事件总线，有需要可以直接翻看。

## 4、路由管理 Route

1. 路由（Route）在移动开发中通常指页面（Page），这跟 Web 开发中单页应用的 Route 概念意义是相同的
2. Route 在 Android 中 通常指一个 Activity，在 iOS 中指一个 ViewController。
3. 所谓路由管理，就是管理页面之间如何跳转，通常也可被称为导航管理。
4. Flutter 中的路由管理和原生开发类似，无论是 Android 还是 iOS，导航管理都会维护一个路由栈，路由入栈（push）操作对应打开一个新页面，路由出栈（pop）操作对应页面关闭操作，而路由管理主要是指如何来管理路由栈

### ①、一个简单示例

1. main 主方法，配置路由

```dart
import 'package:flutter/material.dart';

import '00_基础知识/01_路由/HomeRoute.dart';
import '00_基础知识/01_路由/SettingRoute.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      // 设置应用的主页为 HomeRoute 小部件
      home: const HomeRoute(),
      // 路由设置
      routes: {
        // 定义名为 /setting 的路由，对应着 SettingRoute 小部件
        '/setting': (context) => const SettingRoute(),
      },
    );
  }
}
```

2. HomeRoute 页面

```dart
import 'package:flutter/material.dart';

class HomeRoute extends StatelessWidget {
  const HomeRoute({super.key});

  @override
  Widget build(BuildContext context) {

    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.amberAccent,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，跳转到 /setting 路由
            onPressed: (){
              // 使用 SettingRoute 类作为路由导航
              // Navigator.push(context, MaterialPageRoute(builder: (context) => const SettingRoute()),);
              // 使用路由名称作为导航，在 main.dart 的 routes 中进行的配置
              Navigator.pushNamed(context, '/setting');
            },
            child: const Text("点击进入设置", textDirection: TextDirection.ltr,),
          )
        ],
      ),
    );
  }
}
```

3. SettingRoute 页面

```dart
import 'package:flutter/material.dart';

class SettingRoute extends StatelessWidget {
  const SettingRoute({super.key});

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，返回上一个路由
            onPressed: (){
              // 返回上一个路由
              Navigator.pop(context);
            },
            child: const Text("点击返回主页", textDirection: TextDirection.ltr,),
          )
        ],
      )
    );
  }
}
```

4. `Navigator.push()` 和 `Navigator.pushNamed()` 都是用于在导航器中切换页面的方法，但它们有一些区别：
5. `Navigator.push()` 方法需要传递一个 `Route` 对象，该对象描述了要推送到导航器的新页面。通常使用 `MaterialPageRoute` 作为 `Route` 对象，它接受一个 `builder` 函数来构建新页面的小部件。
6. `Navigator.pushNamed()` 方法使用路由名称来推送新页面到导航器。在 `MaterialApp` 的 `routes` 属性中定义了一个路由名称与小部件的映射关系后，可以使用 `Navigator.pushNamed()` 方法来推送对应的小部件。
7.  `MaterialApp` 的 `routes` 属性是可选的。如果不需要使用命名路由，可以省略 `routes` 属性。在这种情况下，可以使用 `Navigator.push()` 方法来推送任何小部件到导航器，而不需要通过路由名称来引用它们。
8. 下面是使用 `Navigator.push()` 的代码：
9. main 主方法

```dart
import 'package:flutter/material.dart';

import '00_基础知识/01_路由/HomeRoute.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      // 设置应用的主页为 HomeRoute 小部件
      home: HomeRoute()
    );
  }
}
```

10. HomeRoute 页面

```dart
import 'package:flutter/material.dart';

import 'SettingRoute.dart';

class HomeRoute extends StatelessWidget {
  const HomeRoute({super.key});

  @override
  Widget build(BuildContext context) {

    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.amberAccent,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，跳转到 /setting 路由
            onPressed: (){
              // 使用 SettingRoute 类作为路由导航
              Navigator.push(context, MaterialPageRoute(builder: (context) => const SettingRoute()),);
            },
            child: const Text("点击进入设置", textDirection: TextDirection.ltr,),
          )
        ],
      ),
    );
  }
}

```

11. SettingRoute 页面

```dart
import 'package:flutter/material.dart';

class SettingRoute extends StatelessWidget {
  const SettingRoute({super.key});

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，返回上一个路由
            onPressed: (){
              // 返回上一个路由
              Navigator.pop(context);
            },
            child: const Text("点击返回主页", textDirection: TextDirection.ltr,),
          )
        ],
      )
    );
  }
}
```

12. 效果：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025105505.png)

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025105511.png)

### ②、MaterialPageRoute

1. `MaterialPageRoute` 继承自 `PageRoute` 类
2. `PageRoute` 类是一个抽象类，表示占有整个屏幕空间的一个模态路由页面，它还定义了路由构建及切换时过渡动画的相关接口及属性。
3. `MaterialPageRoute` 是 `Material` 组件库提供的组件，它可以针对不同平台，实现与平台页面切换动画风格一致的路由切换动画：
	1. 对于 Android，当打开新页面时，新的页面会从屏幕底部滑动到屏幕顶部；当关闭页面时，当前页面会从屏幕顶部滑动到屏幕底部后消失，同时上一个页面会显示到屏幕上。
	2. 对于 iOS，当打开页面时，新的页面会从屏幕右侧边缘一直滑动到屏幕左边，直到新页面全部显示到屏幕上，而上一个页面则会从当前屏幕滑动到屏幕左侧而消失；当关闭页面时，正好相反，当前页面会从屏幕右侧滑出，同时上一个页面会从屏幕左侧滑入。
4. 下面我们介绍一下 `MaterialPageRoute` 构造函数的各个参数的意义：

```dart
MaterialPageRoute({
  /**
   * builder 是一个 WidgetBuilder 类型的回调函数，它的作用是构建路由页面的具体内容，
   * 返回值是一个 widget。我们通常要实现此回调，返回新路由的实例
   */
  WidgetBuilder builder,
  /**
   * settings 包含路由的配置信息，如路由名称、是否初始路由（首页）
   */
  RouteSettings settings,
  /**
   * maintainState：默认情况下，当入栈一个新路由时，原来的路由仍然会被保存在内存中，
   * 如果想在路由没用的时候释放其所占用的所有资源，可以设置 maintainState 为 false
   */
  bool maintainState = true,
  /**
   * fullscreenDialog 表示新的路由页面是否是一个全屏的模态对话框，
   * 在 iOS 中，如果 fullscreenDialog 为 true，新页面将会从屏幕底部滑入（而不是水平方向）
   */
  bool fullscreenDialog = false,
})
```

5. 如果想自定义路由切换动画，可以自己继承 PageRoute 来实现

### ③、Navigator 路由管理

1. `Navigator` 是一个路由管理的组件，它提供了打开和退出路由页方法。
2. `Navigator` 通过一个栈来管理活动路由集合。通常当前屏幕显示的页面就是栈顶的路由。Navigator 提供了一系列方法来管理路由栈，在此我们只介绍其最常用的两个方法：
3. `Future push(BuildContext context, Route route)`：将给定的路由入栈（即打开新的页面），返回值是一个 Future 对象，用以接收新路由出栈（即关闭）时的返回数据。
4. `bool pop(BuildContext context, [ result ])`：将栈顶路由出栈，result 为页面关闭时返回给上一个页面的数据。
5. Navigator 还有很多其他方法，如 `Navigator.replace`、`Navigator.popUntil` 等，详情请参考API文档或SDK 源码注释，在此不再赘述。

### ④、路由传值

1. 使用路由进入新页面，或返回之前的页面时，都可以传递参数
2. mian 主方法

```dart
import 'package:flutter/material.dart';

import '00_基础知识/01_路由/HomeRoute.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      // 设置应用的主页为 HomeRoute 小部件
      home: HomeRoute()
    );
  }
}
```

3. HomeRoute 页面

```dart
import 'package:flutter/material.dart';

import 'SettingRoute.dart';

// 创建一个 StatefulWidget 类
class HomeRoute extends StatefulWidget {
  const HomeRoute({super.key});

  @override
  _HomeRouteState createState() => _HomeRouteState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _HomeRouteState extends State<HomeRoute> {
  // 用于接收路由传递的参数
  String text = "";

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.amberAccent,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            /**
             * 使用 Navigator 导航到 SettingRoute 页面，并等待返回结果
             * async：在 Dart 语言中，async 用于标记一个函数是异步函数，即该函数可能会执行耗时操作而不会阻塞其他代码的执行。
             * 异步函数可以使用 await 关键字来等待其他异步操作的完成
             */
            onPressed: () async {
              /**
               * await：await 关键字只能在异步函数中使用，用于等待一个异步操作的完成。
               * 当遇到 await 关键字时，函数会暂停执行，直到等待的异步操作完成并返回结果。
               * 在等待期间，函数会让出主线程，允许其他代码继续执行
               */
              final result = await Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SettingRoute(text: 'HomeRoute 传递的参数',)),
              );
              /**
               * setState：setState 是 Flutter 框架中的一个方法，用于更新小部件的状态并触发重建。
               * 当小部件的状态发生变化时，调用 setState 方法可以通知框架重新构建小部件，并在新的状态下重新渲染。
               * 通常，setState 方法会在异步操作完成后被调用，以更新 UI 并显示异步操作的结果
               */
              setState((){
                // 如果返回值为空，则将 text 设置为空字符串
                text = result ?? "";
              });
            },
            child: const Text("点击进入设置", textDirection: TextDirection.ltr,),
          ),
          // 显示从 SettingRoute 页面返回的参数
          Text("SettingRoute 返回的参数：$text", style: const TextStyle(color: Colors.white),)
        ],
      ),
    );
  }
}
```

4. SettingRoute 页面

```dart
import 'package:flutter/material.dart';

class SettingRoute extends StatelessWidget {
  const SettingRoute({super.key, required this.text});

  // 用于接收路由传递的参数
  final String text;

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，返回上一个路由
            onPressed: (){
              // 返回上一个路由，并返回消息
              Navigator.pop(context, "SettingRoute 的返回值");
            },
            child: const Text("点击返回主页", textDirection: TextDirection.ltr,),
          ),
          // 显示从 HomeRoute 页面传递的参数
          Text("HomeRoute 传递的参数：$text", style: const TextStyle(color: Colors.white),)
        ],
      )
    );
  }
}
```

5. 效果：刚打开 HomeRoute 主页面

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025133841.png)

6. 进入 SettingRoute 页面

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025133851.png)

7. 点击按钮返回 HomeRoute 页面

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025133900.png)

### ⑤、命名路由

1. 所谓“命名路由”（Named Route）即有名字的路由
2. 我们可以先给路由起一个名字，然后就可以通过路由名字直接打开新的路由了，这为路由管理带来了一种直观、简单的方式

#### Ⅰ、路由表

1. 要想使用命名路由，我们必须先提供并注册一个路由表（routing table），这样应用程序才知道哪个名字与哪个路由组件相对应。
2. 其实注册路由表就是给路由起名字，路由表的定义如下：

```dart
Map<String, WidgetBuilder> routes;
```

3. 它是一个 Map，`key` 为路由的名字，是个字符串；`value` 是个 `builder` 回调函数，用于生成相应的路由 `widget`。
4. 我们在通过路由名字打开新路由时，应用会根据路由名字在路由表中查找到对应的 `WidgetBuilder` 回调函数，然后调用该回调函数生成路由 `widget` 并返回

#### Ⅱ、注册路由表

1. 路由表的注册方式很简单，在 `MyApp` 类的 `build` 方法中找到 `MaterialApp`，添加 `routes` 属性，代码如下

```dart
import 'package:flutter/material.dart';

import '00_基础知识/01_路由/HomeRoute.dart';
import '00_基础知识/01_路由/SettingRoute.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      // 设置应用的主页为 HomeRoute 小部件
      home: const HomeRoute(),
      // 路由设置
      routes: {
        // 定义名为 /setting 的路由，对应着 SettingRoute 小部件
        '/setting': (context) => const SettingRoute(),
      },
    );
  }
}
```

2. 然后在页面中通过 `Navigator.pushNamed` 方法传入路由名，进行路由跳转

```dart
import 'package:flutter/material.dart';

import 'SettingRoute.dart';

// 创建一个 StatefulWidget 类
class HomeRoute extends StatefulWidget {
  const HomeRoute({super.key});

  @override
  _HomeRouteState createState() => _HomeRouteState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _HomeRouteState extends State<HomeRoute> {

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.amberAccent,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            onPressed: () { 
              // 跳转到名为 /setting 的路由
              Navigator.pushNamed(context, "/setting"); 
            },
            child: const Text("点击进入设置", textDirection: TextDirection.ltr,),
          )
        ],
      ),
    );
  }
}
```

3. 依然是通过 `Navigator.pop` 方法返回到上一个页面

```dart
import 'package:flutter/material.dart';

class SettingRoute extends StatelessWidget {
  const SettingRoute({super.key});

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，返回上一个路由
            onPressed: (){
              // 返回上一个路由
              Navigator.pop(context);
            },
            child: const Text("点击返回主页", textDirection: TextDirection.ltr,),
          ),
        ],
      )
    );
  }
}
```

#### Ⅲ、命名路由参数传递

1. 在 Flutter 最初的版本中，命名路由是不能传递参数的，后来才支持了参数；下面展示命名路由如何传递并获取路由参数：
2. 我们先注册一个路由：

```dart
import 'package:flutter/material.dart';

import '00_基础知识/01_路由/HomeRoute.dart';
import '00_基础知识/01_路由/SettingRoute.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      // 设置应用的主页为 HomeRoute 小部件
      home: const HomeRoute(),
      // 路由设置
      routes: {
        // 定义名为 /setting 的路由，对应着 SettingRoute 小部件
        '/setting': (context) => const SettingRoute(),
      },
    );
  }
}
```

3. 在打开路由时传递参数

```dart
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class HomeRoute extends StatefulWidget {
  const HomeRoute({super.key});

  @override
  _HomeRouteState createState() => _HomeRouteState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _HomeRouteState extends State<HomeRoute> {
  // 用于接收路由传递的参数
  String text = "";

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.amberAccent,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            /**
             * 使用 Navigator 导航到 SettingRoute 页面，并等待返回结果
             * async：在 Dart 语言中，async 用于标记一个函数是异步函数，即该函数可能会执行耗时操作而不会阻塞其他代码的执行。
             * 异步函数可以使用 await 关键字来等待其他异步操作的完成
             */
            onPressed: () async {
              /**
               * 跳转到名为 /setting 的路由，并传递参数 arguments
               * await：await 关键字只能在异步函数中使用，用于等待一个异步操作的完成。
               * 当遇到 await 关键字时，函数会暂停执行，直到等待的异步操作完成并返回结果。
               * 在等待期间，函数会让出主线程，允许其他代码继续执行
               */
              final result = await Navigator.pushNamed(context, "/setting", arguments: "HomeRoute 传递的参数");
              /**
               * setState：setState 是 Flutter 框架中的一个方法，用于更新小部件的状态并触发重建。
               * 当小部件的状态发生变化时，调用 setState 方法可以通知框架重新构建小部件，并在新的状态下重新渲染。
               * 通常，setState 方法会在异步操作完成后被调用，以更新 UI 并显示异步操作的结果
               */
              setState((){
                // 将返回值赋值被 text
                text = result.toString();
              });
            },
            child: const Text("点击进入设置", textDirection: TextDirection.ltr,),
          ),
          // 显示从 SettingRoute 页面返回的参数
          Text("SettingRoute 返回的参数：$text", style: const TextStyle(color: Colors.white),)
        ],
      ),
    );
  }
}
```

4. 在 SettingRoute 页面接收并返回参数

```dart
import 'package:flutter/material.dart';

class SettingRoute extends StatelessWidget {
  const SettingRoute({super.key});

  @override
  Widget build(BuildContext context) {
    // 获取传递过来的路由参数
    var args = ModalRoute.of(context)?.settings.arguments;

    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          const SizedBox(height: 50),
          ElevatedButton(
            // 当按钮被点击时，返回上一个路由
            onPressed: (){
              // 返回上一个路由，并返回消息
              Navigator.pop(context, "SettingRoute 的返回值");
            },
            child: const Text("点击返回主页", textDirection: TextDirection.ltr,),
          ),
          // 显示从 HomeRoute 页面传递的参数
          Text("HomeRoute 传递的参数：$args", style: const TextStyle(color: Colors.white),)
        ],
      )
    );
  }
}
```

5. 刚进入主页时

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025141120.png)

6. 进入 SettingRoute 页面

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025141131.png)

7. 返回 HomeRoute 页面

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025141141.png)

#### Ⅳ、路由生成钩子

1. 假设我们要开发一个电商 App，当用户没有登录时可以看店铺、商品等信息，但交易记录、购物车、用户个人信息等页面需要登录后才能看。
2. 为了实现上述功能，我们需要在打开每一个路由页前判断用户登录状态！如果每次打开路由前我们都需要去判断一下将会非常麻烦，那有什么更好的办法吗？
3. `MaterialApp` 有一个 `onGenerateRoute` 属性，它在打开命名路由时可能会被调用，之所以说可能，是因为当调用 `Navigator.pushNamed(...)` 打开命名路由时，如果指定的路由名在路由表中已注册，则会调用路由表中的 `builder` 函数来生成路由组件；如果路由表中没有注册，才会调用 `onGenerateRoute` 来生成路由。
4. `onGenerateRoute` 回调签名如下：

```dart
Route<dynamic> Function(RouteSettings settings)
```

5. 有了 `onGenerateRoute` 回调，要实现上面控制页面权限的功能就非常容易：
6. 我们放弃使用路由表，取而代之的是提供一个 `onGenerateRoute` 回调，然后在该回调中进行统一的权限控制，如：

```dart
MaterialApp(
  ... //省略无关代码
  onGenerateRoute:(RouteSettings settings){
	  return MaterialPageRoute(builder: (context){
		   String routeName = settings.name;
       // 如果访问的路由页需要登录，但当前未登录，则直接返回登录页路由，
       // 引导用户登录；其他情况则正常打开路由。
     }
   );
  }
);
```

7. 注意，`onGenerateRoute` 只会对命名路由生效

## 5、包管理

## 6、资源管理

1. Flutter APP 安装包中会包含代码和 assets（资源）两部分。
2. Assets 是会打包到程序安装包中的，可在运行时访问。
3. 常见类型的 assets 包括静态数据（例如JSON文件）、配置文件、图标和图片等

### ①、指定 assets

1. 和包管理一样，Flutter 也使用 `pubspec.yaml` 文件来管理应用程序所需的资源，举个例子:

```yaml
flutter:
  assets:
    - assets/my_icon.png
    - assets/background.png
```

2. `assets` 指定应包含在应用程序中的文件， 每个 `asset` 都通过相对于 `pubspec.yaml` 文件所在的文件系统路径来标识自身的路径。`asset` 的声明顺序是无关紧要的，asset 的实际目录可以是任意文件夹（在本示例中是assets 文件夹）。
3. 在构建期间，Flutter 将 asset 放置到称为 asset bundle 的特殊存档中，应用程序可以在运行时读取它们（但不能修改）

### ②、Asset 变体（variant）

1. 构建过程支持 asset 变体 的概念：不同版本的 asset 可能会显示在不同的上下文中。 
2. 在 `pubspec.yaml` 的 `assets` 部分中指定 asset 路径时，构建过程中，会在相邻子目录中查找具有相同名称的任何文件。这些文件随后会与指定的 asset 一起被包含在 asset bundle 中。
3. 例如，如果应用程序目录中有以下文件:

```dart
…/pubspec.yaml
…/graphics/my_icon.png
…/graphics/background.png
…/graphics/dark/background.png
….
```

4. 然后 `pubspec.yaml` 文件中只需包含:

```yaml
flutter:
  assets:
    - graphics/background.png
```

5. 那么这两个 `graphics/background.png` 和 `graphics/dark/background.png` 都将包含在 asset bundle 中。
6. 前者被认为是_main asset_ （主资源），后者被认为是一种变体（variant）。
7. 在选择匹配当前设备分辨率的图片时，Flutter 会使用到 asset 变体（见下文）

### ③、加载 assets

#### Ⅰ、加载文本 assets

1. 通过 `rootBundle` 对象加载：每个 Flutter 应用程序都有一个 `rootBundle` 对象， 通过它可以轻松访问主资源包，直接使用 `package:flutter/services.dart` 中全局静态的 `rootBundle` 对象来加载 asset 即可。
2. 通过 `DefaultAssetBundle` 加载：建议使用 `DefaultAssetBundle` 来获取当前 BuildContext 的 AssetBundle。 这种方法不是使用应用程序构建的默认 asset bundle，而是使父级 widget 在运行时动态替换的不同的 AssetBundle，这对于本地化或测试场景很有用。
3. 通常，可以使用 `DefaultAssetBundle.of()` 在应用运行时来间接加载 asset（例如 JSON 文件），而在 widget 上下文之外，或其他 AssetBundle 句柄不可用时，可以使用 rootBundle 直接加载这些 asset，例如：

```dart
import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;

Future<String> loadAsset() async {
  return await rootBundle.loadString('assets/config.json');
}
```

#### Ⅱ、加载图片

##### （1）、声明分辨率相关的图片 assets

1. `AssetImage` 可以将 asset 的请求逻辑映射到最接近当前设备像素比例（dpi）的 asset。为了使这种映射起作用，必须根据特定的目录结构来保存 asset：

```dart
…/image.png
…/Mx/image.png
…/Nx/image.png
…
```

2. 其中 M 和 N 是数字标识符，对应于其中包含的图像的分辨率，也就是说，它们指定不同设备像素比例的图片。
3. 主资源默认对应于 1.0 倍的分辨率图片。看一个例子：

```dart
…/my_icon.png
…/2.0x/my_icon.png
…/3.0x/my_icon.png
```

4. 在设备像素比率为 1.8 的设备上，`.../2.0x/my_icon.png` 将被选择。对于 2.7 的设备像素比率，`.../3.0x/my_icon.png` 将被选择。
5. 如果未在 Image widget 上指定渲染图像的宽度和高度，那么 Image widget 将占用与主资源相同的屏幕空间大小。 也就是说，如果 `.../my_icon.png` 是 72px 乘 72px，那么 `.../3.0x/my_icon.png` 应该是 216px 乘 216px; 但如果未指定宽度和高度，它们都将渲染为 72 像素 × 72 像素（以逻辑像素为单位）。
6. `pubspec.yaml` 中 asset 部分中的每一项都应与实际文件相对应，但主资源项除外。当主资源缺少某个资源时，会按分辨率从低到高的顺序去选择 ，也就是说 1x 中没有的话会在 2x 中找，2x 中还没有的话就在 3x 中找。

##### （2）、加载图片

1. 要加载图片，可以使用 `AssetImage` 类。例如，我们可以从上面的 asset 声明中加载背景图片：

```dart
Widget build(BuildContext context) {
  return DecoratedBox(
    decoration: BoxDecoration(
      image: DecorationImage(
        image: AssetImage('graphics/background.png'),
      ),
    ),
  );
}
```

2. 注意，`AssetImage` 并非是一个 widget， 它实际上是一个 `ImageProvider`，有些时候你可能期望直接得到一个显示图片的 widget，那么你可以使用 `Image.asset()` 方法，如：

```dart
Widget build(BuildContext context) {
  return Image.asset('graphics/background.png');
}
```

3. 使用默认的 asset bundle 加载资源时，内部会自动处理分辨率等，这些处理对开发者来说是无感知的。 (如果使用一些更低级别的类，如 `ImageStream` 或 `ImageCache` 时你会注意到有与缩放相关的参数)

##### （3）、依赖包中的资源图片

1. 加载依赖包中的图像，必须给 AssetImage 提供 package 参数。
2. 例如，假设您的应用程序依赖于一个名为 `my_icons` 的包，它具有如下目录结构：

```dart
…/pubspec.yaml
…/icons/heart.png
…/icons/1.5x/heart.png
…/icons/2.0x/heart.png
…
```

3. 然后加载图像，使用：

```dart
AssetImage('icons/heart.png', package: 'my_icons')

或

Image.asset('icons/heart.png', package: 'my_icons')
```

4. 注意：包在使用本身的资源时也应该加上 package 参数来获取。

##### （4）、打包包中的 assets

1. 如果在 `pubspec.yaml` 文件中声明了期望的资源，它将会打包到相应的 package 中。特别是，包本身使用的资源必须在 `pubspec.yaml` 中指定。
2. 包也可以选择在其 `lib/` 文件夹中包含未在其 `pubspec.yaml` 文件中声明的资源。在这种情况下，对于要打包的图片，应用程序必须在 `pubspec.yaml` 中指定包含哪些图像。 例如，一个名为 `fancy_backgrounds` 的包，可能包含以下文件：

```dart
…/lib/backgrounds/background1.png
…/lib/backgrounds/background2.png
…/lib/backgrounds/background3.png
```

3. 要包含第一张图像，必须在 `pubspec.yaml` 的 assets 部分中声明它：

```yaml
flutter:
  assets:
    - packages/fancy_backgrounds/backgrounds/background1.png
```

4. `lib/` 是隐含的，所以它不应该包含在资产路径中。

#### Ⅲ、特定平台 assets

1. 上面的资源都是 flutter 应用中的，这些资源只有在 Flutter 框架运行之后才能使用，如果要给我们的应用设置 APP 图标或者添加启动图，那我们必须使用特定平台的 assets

##### （1）、设置 Android APP 图标

1. 在 Flutter 项目的根目录中，导航到 `.../android/app/src/main/res` 目录，里面包含了各种资源文件夹
2. 如 `mipmap-hdpi` 已包含占位符图像 ic_launcher.png，见下图：

![|253](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231116101636.png)

3. 只需按照 Android 开发人员指南中的说明， 将其替换为所需的资源，并遵守每种屏幕密度（dpi）的建议图标大小标准。
4. 注意：如果重命名 `.png` 文件，则还必须在 `AndroidManifest.xml` 的 `<application>` 标签的 `android:icon` 属性中更新名称

##### （2）、设置 iOS APP 图标

1. 在 Flutter 项目的根目录中，导航到 `.../ios/Runner`。
2. 该目录中 `Assets.xcassets/AppIcon.appiconset` 已经包含占位符图片，见下图， 只需将它们替换为适当大小的图片，保留原始文件名称

![|280](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231116101932.png)

##### （3）、更新启动页

1. 在 Flutter 框架加载时，Flutter 会使用本地平台机制绘制启动页。
2. 此启动页将持续到 Flutter 渲染应用程序的第一帧时。
3. 注意：这意味着如果不在应用程序的 `main()` 方法中调用 `runApp` 函数 （或者更具体地说，如果不调用`window.render` 去响应 `window.onDrawFrame` ）的话， 启动屏幕将永远持续显示。

![|204](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231116102151.png)

##### （4）、Android 更新启动页

1. 要将启动屏幕（splash screen）添加到 Flutter 应用程序， 请导航至 `.../android/app/src/main`。
2. 在 `res/drawable/launch_background.xml`，通过自定义 drawable 来实现自定义启动界面
3. 也可以直接换一张图片

##### （5）、iOS 更新启动页

1. 要将图片添加到启动屏幕（splash screen）的中心，请导航至 `.../ios/Runner`。
2. 在 `Assets.xcassets/LaunchImage.imageset`， 拖入图片，并命名为 `LaunchImage.png`、`LaunchImage@2x.png`、`LaunchImage@3x.png`。
3. 如果使用不同的文件名，那还必须更新同一目录中的 `Contents.json` 文件，图片的具体尺寸可以查看苹果官方的标准。
4. 也可以通过打开 Xcode 完全自定义 storyboard。在 Project Navigator 中导航到 `Runner/Runner` 然后通过打开 Assets.xcassets 拖入图片，或者通过在 LaunchScreen.storyboard 中使用 Interface Builder 进行自定义，如下图所示。

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231116102613.png)

### ④、平台共享 assets

1. 如果我们采用的是 Flutter + 原生 的开发模式，那么可能会存 Flutter 和原生需要共享资源的情况
2. 比如 Flutter 项目中已经有了一张图片 A，如果原生代码中也要使用 A，我们可以将 A 拷贝一份到原生项目的特定目录，这样的话虽然功能可以实现，但是最终的应用程序包会变大，因为包含了重复的资源
3. 为了解决这个问题，Flutter 提供了一种 Flutter 和原生之间共享资源的方式
4. 由于实现上需要涉及平台相关的原生代码，这里不做展开，有需要可以自行查阅：[官方文档](https://flutter.cn/docs/development/ui/assets-and-images#sharing-assets-with-the-underlying-platform)

## 7、

## 8、

# 三、基本组件

## 0、Center 居中布局

1. Flutter 中的 Center 组件是一个用于在其子组件周围居中对齐它们的布局组件。
2. 它将其子组件放置在水平和垂直方向上的中心位置。
3. 这意味着无论子组件的大小如何，它们都将在屏幕的中央或父组件的中央对齐。

```dart
import 'package:flutter/material.dart';

// 入口方法
void main() {
  /**
   * const：定义常量，多个相同的实例会共享存储空间，且重新构建时不会重新构建该组件
   * 实例化 Center 类（布局组件），它将其子组件放置在水平和垂直方向上的中心位置
   */
  runApp(const Center(
    /**
     * 创建一个 Text 文本对象，指定其对象名为 child
     * 参数 1：显示文本
     */
    child: Text("月海"),
  ));
}
```

## 1、Text 文本组件

- 用于显示简单样式文本，它包含一些控制文本显示样式的一些属性

### ①、基础属性

```dart
import 'package:flutter/material.dart';

import '01_基本组件/01_Text文本组件/01_基础属性.dart';

// 入口方法
void main() {
  /**
   * const：定义常量，多个相同的实例会共享存储空间，且重新构建时不会重新构建该组件
   * 实例化 Center 类（布局组件），它将其子组件放置在水平和垂直方向上的中心位置
   */
  runApp(const Center(
    child: TextComponent(),
  ));
}
```

```dart
import 'package:flutter/material.dart';

class TextComponent extends StatelessWidget {
  const TextComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * 创建一个 Text 文本对象，指定其对象名为 child
     * 参数 1：显示文本；
     * textAlign：文本的对齐方式；可以选择左对齐、右对齐还是居中等
     * style：设置文本样式
     * textDirection：文本显示方向，默认从左向右排列
     *    TextDirection.ltr：从左向右排列
     *    TextDirection.rtl：从右向左排列
     */
    return const Text(
      "月海",
      textAlign: TextAlign.start,
      style: TextStyle(
        color: Colors.blue,
        fontSize: 30,
      ),
      textDirection: TextDirection.ltr,
    );
  }
}
```

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017112137.png)

| 属性 | 介绍 |
| ---- | ---- |
|data (String)|这是要显示的文本内容，通常是一个字符串。|
|style (TextStyle)|用于定义文本的样式，例如字体、字号、颜色等。|
|strutStyle (StrutStyle)|用于设置基线网格，可用于自定义文本的垂直布局。|
|textAlign (TextAlign)|用于指定文本的水平对齐方式，如左对齐、居中对齐或右对齐。|
|textDirection (TextDirection)|用于指定文本的文本方向，如从左到右（TextDirection.ltr）或从右到左（TextDirection.rtl）。|
|locale (Locale)|用于定义文本的语言环境，以支持本地化。|
|softWrap (bool)|一个布尔值，指示文本是否应在文本框之内自动换行。|
|overflow (TextOverflow)|当文本超出可用空间时，指定如何处理溢出文本，例如省略号（ellipsis）或截断（clip）。|
|textScaleFactor (double)|用于缩放文本的比例因子，可以改变文本的大小。|
|maxLines (int)|用于指定文本的最大行数，超过这个行数时将截断文本。|
|semanticsLabel (String)|用于设置文本的语义标签，以帮助可访问性工具理解文本的含义。|
|textWidthBasis (TextWidthBasis)|用于确定文本行的宽度，可以是 parent、longestLine 或 layout。|
|textHeightBehavior (TextHeightBehavior)|用于自定义文本行高的行为，包括最小行高、最大行高和领先（leading）。|
|selectionColor (Color)|用于指定文本的选择背景颜色，当用户选择文本时会用到。|

### ②、TextSpan 富文本

1. 在上面的例子中，Text 的所有文本内容只能按同一种样式，如果我们需要对一个 Text 内容的不同部分按照不同的样式显示，这时就可以使用 `TextSpan`，它代表文本的一个“片段”。
2. TextSpan 的定义中，`style` 和 `text` 属性代表该文本片段的样式和内容； `children` 是一个 `TextSpan` 的数组，也就是说 `TextSpan` 可以包括其他 `TextSpan`。而 `recognizer` 用于对该文本片段上用于手势进行识别处理：

```dart
const TextSpan({
  TextStyle style, 
  String text,
  List<TextSpan> children,
  GestureRecognizer recognizer,
});
```

2. 下面的代码中通过 `TextSpan` 实现了一个基础文本片段和一个链接片段，然后通过 `Text.rich` 方法将 `TextSpan` 添加到 `Text` 中，之所以可以这样做，是因为 `Text` 其实就是 `RichText` 的一个包装，而 `RichText` 是可以显示多种样式(富文本)的 `widget`。

```dart
import 'package:flutter/material.dart';

import '01_基本组件/01_Text文本组件/02_TextSpan富文本.dart';

// 入口方法
void main() {
  /**
   * const：定义常量，多个相同的实例会共享存储空间，且重新构建时不会重新构建该组件
   * 实例化 Center 类（布局组件），它将其子组件放置在水平和垂直方向上的中心位置
   */
  runApp(const Center(
    child: TextComponent(),
  ));
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

class TextComponent extends StatelessWidget {
  // 创建一个名为 TextComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const TextComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      /**
       * 通过 TextSpan 实现了一个基础文本片段和一个链接片段，
       * 然后通过 Text.rich 方法将 TextSpan 添加到 Text 中，
       * 之所以可以这样做，是因为 Text 其实就是 RichText 的一个包装，
       * 而 RichText 是可以显示多种样式(富文本)的 widget。
       */
      child: Text.rich(TextSpan(
        children: [
          // 第一个 TextSpan 显示白色文本
          TextSpan(
            text: "白色",
            style: TextStyle(color: Colors.white),
          ),
          // 第二个TextSpan显示蓝色文本
          TextSpan(
            text: "蓝色",
            style: TextStyle(color: Colors.blue)
          ),
        ],
      ))
    );
  }
}
```

![|725](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017112052.png)

### ③、DefaultTextStyle 默认样式

1. 在 `Widget` 树中，文本的样式默认是可以被继承的（子类文本类组件未指定具体样式时可以使用 Widget 树中父级设置的默认样式）
2. 因此，如果在 `Widget` 树的某一个节点处设置一个默认的文本样式，那么该节点的子树中所有文本都会默认使用这个样式
3. 而 `DefaultTextStyle` 正是用于设置默认文本样式的。

```dart
import 'package:flutter/material.dart';

import '01_基本组件/01_Text文本组件/03_DefaultTextStyle默认样式.dart';

// 入口方法
void main() {
  /**
   * const：定义常量，多个相同的实例会共享存储空间，且重新构建时不会重新构建该组件
   * 实例化 Center 类（布局组件），它将其子组件放置在水平和垂直方向上的中心位置
   */
  runApp(const Center(
    child: TextComponent(),
  ));
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

class TextComponent extends StatelessWidget {
  // 创建一个名为 TextComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const TextComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      // 指定文本方向为从左到右
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件：设置默认文本
      child: DefaultTextStyle(
        // 设置默认文本样式
        style: TextStyle(
            color: Colors.red,
            fontSize: 20
        ),
        // 设置子文本
        child: Column(
          children: [
            Text("月海"),
            Text("言"),
            Text("白色", style: TextStyle(color: Colors.white),),
            Text(
              "NotoSansCJKjp 正常字体",
              style: TextStyle(
                color: Colors.white,
                fontFamily: "NotoSansCJKjp"
              ),
            ),
            Text(
              "NotoSansCJKjp 加粗字体",
              style: TextStyle(
                color: Colors.white,
                fontFamily: "NotoSansCJKjp",
                fontWeight: FontWeight.bold
              ),
            ),
          ],
        )
      )
    );
  }
}
```

### ④、字体

#### Ⅰ、简介

1. 可以在 Flutter 应用程序中使用不同的字体。
2. 例如，我们可能会使用设计人员创建的自定义字体，或者其他第三方的字体，如 Google Fonts 中的字体。
3. 在 Flutter 中使用字体分三步完成。
	1. 首先将字体文件复制到项目根目录的 `asset/fonts` 目录下，没有目录可自己创建一个
	2. 然后在 `pubspec.yaml` 中声明它们，以确保它们会打包到应用程序中。
	3. 最后通过 `TextStyle` 属性使用字体。

#### Ⅱ、在 asset 中声明

1. 要将字体文件打包到应用中，和使用其他资源一样
2. 要先将字体文件复制到目录中，如：

![|373](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017152218.png)

3. 然后在 `pubspec.yaml` 中声明它：

```yaml
flutter:
  # 下面的行确保 Material Icons 字体
  # 包含在您的应用程序中，以便您可以在
  # material Icons 类中使用这些图标。
  uses-material-design: true

  # 字体配置
  fonts:
    # 这表示定义了一个名为 NotoSansCJKjp 的字体系列（font family）。这个系列包含了不同样式和权重的字体
    - family: NotoSansCJKjp
      # 指定了与 NotoSansCJKjp 字体系列相关的字体文件
      fonts:
        # 是 NotoSansCJKjp 字体系列的正常（Regular）字体。它的资源文件位于应用程序的 assets/fonts 目录下
        - asset: asset/fonts/NotoSansCJKjp-Regular.ttf
        # 是 NotoSansCJKjp 字体系列的粗体（Bold）字体。它的资源文件位于应用程序的 assets/fonts 目录下
        - asset: asset/fonts/NotoSansCJKjp-Bold.ttf
```

#### Ⅲ、使用字体

```dart
import 'package:flutter/material.dart';

import '01_基本组件/01_Text文本组件/03_DefaultTextStyle默认样式.dart';

// 入口方法
void main() {
  /**
   * const：定义常量，多个相同的实例会共享存储空间，且重新构建时不会重新构建该组件
   * 实例化 Center 类（布局组件），它将其子组件放置在水平和垂直方向上的中心位置
   */
  runApp(const Center(
    child: TextComponent(),
  ));
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

class TextComponent extends StatelessWidget {
  // 创建一个名为 TextComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const TextComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Directionality(
        // 指定文本方向为从左到右
        textDirection: TextDirection.ltr,
        // 设置默认文本
        child: DefaultTextStyle(
          // 设置默认文本样式
          style: TextStyle(
              color: Colors.red,
              fontSize: 20
          ),
          // 设置子文本
          child: Column(
            children: [
              Text("月海"),
              Text("言"),
              Text("白色", style: TextStyle(color: Colors.white),),
              Text(
                "NotoSansCJKjp 正常字体",
                style: TextStyle(
                  color: Colors.white,
                  fontFamily: "NotoSansCJKjp"
                ),
              ),
              Text(
                "NotoSansCJKjp 加粗字体",
                style: TextStyle(
                  color: Colors.white,
                  fontFamily: "NotoSansCJKjp",
                  fontWeight: FontWeight.bold
                ),
              ),
            ],
          )
        )
    );
  }
}
```

![|750](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017131341.png)

## 2、Button 按钮

1. Material 组件库中提供了多种按钮组件如 `ElevatedButton`、`TextButton`、`OutlinedButton` 等，它们都是直接或间接对 `RawMaterialButton` 组件的包装定制，所以他们大多数属性都和 `RawMaterialButton` 一样。
2. 在介绍各个按钮时我们先介绍其默认外观，而按钮的外观大都可以通过属性来自定义，我们在后面统一介绍这些属性。
3. 另外，所有 Material 库中的按钮都有如下相同点：
	1. 按下时都会有“水波动画”（又称“涟漪动画”，就是点击时按钮上会出现水波扩散的动画）。
	2. 有一个 `onPressed` 属性来设置点击回调，当按钮按下时会执行该回调，如果不提供该回调则按钮会处于禁用状态，禁用状态不响应用户点击

### ①、ElevatedButton 漂浮按钮

1. `ElevatedButton` 即"漂浮"按钮
2. 它默认带有阴影和灰色背景。按下后，阴影会变大


```dart
import 'package:flutter/material.dart';

import '01_基本组件/02_button按钮/01_ElevatedButton漂浮按钮.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // ElevatedButton 漂浮按钮
                ElevatedButtonComponent(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// ElevatedButton 漂浮按钮
class ElevatedButtonComponent extends StatelessWidget {
  // 创建一个名为 ButtonComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const ElevatedButtonComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: ElevatedButton(
        onPressed: () {
          print('点击 ElevatedButton 漂浮按钮');
        },
        child: const Text("ElevatedButton 漂浮按钮")
      )
    );
  }
}
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017135246.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017135256.png)

### ②、TextButton 文本按钮

- `TextButton` 即文本按钮，默认背景透明并不带阴影。按下后，会有背景色

```dart
import 'package:flutter/material.dart';

import '01_基本组件/02_button按钮/01_ElevatedButton漂浮按钮.dart';
import '01_基本组件/02_button按钮/02_TextButton文本按钮.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // ElevatedButton 漂浮按钮
                ElevatedButtonComponent(),
                // TextButton 文本按钮
                TextButtonComponent(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// TextButton 文本按钮
class TextButtonComponent extends StatelessWidget {
  // 创建一个名为 TextButtonComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const TextButtonComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: TextButton(
        onPressed: () {
          print('点击 TextButton 文本按钮');
        },
        child: const Text("TextButton 文本按钮")
      )
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017140640.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017140650.png)

### ③、OutlinedButton 轮廓按钮

1. `OutlinedButton` 默认有一个边框，不带阴影且背景透明。
2. 按下后，边框颜色会变亮、同时出现背景和阴影(较弱)

```dart
import 'package:flutter/material.dart';

import '01_基本组件/02_button按钮/01_ElevatedButton漂浮按钮.dart';
import '01_基本组件/02_button按钮/02_TextButton文本按钮.dart';
import '01_基本组件/02_button按钮/03_OutlinedButton轮廓按钮.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // ElevatedButton 漂浮按钮
                ElevatedButtonComponent(),
                // TextButton 文本按钮
                TextButtonComponent(),
                // OutlinedButton 轮廓按钮
                OutlinedButtonComponent()
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// OutlinedButton 轮廓按钮
class OutlinedButtonComponent extends StatelessWidget {
  // 创建一个名为 OutlinedButtonComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const OutlinedButtonComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: OutlinedButton(
        onPressed: () {
          print('点击 OutlinedButton 轮廓按钮');
        },
        child: const Text("OutlinedButton 轮廓按钮")
      )
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017141725.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017141738.png)

### ④、IconButton 图标按钮

1. `IconButton` 是一个可点击的 Icon 图标
2. 不包括文字，默认没有背景，点击后会出现背景

```dart
import 'package:flutter/material.dart';

import '01_基本组件/02_button按钮/01_ElevatedButton漂浮按钮.dart';
import '01_基本组件/02_button按钮/02_TextButton文本按钮.dart';
import '01_基本组件/02_button按钮/03_OutlinedButton轮廓按钮.dart';
import '01_基本组件/02_button按钮/04_IconButton图标按钮.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // ElevatedButton 漂浮按钮
                ElevatedButtonComponent(),
                // TextButton 文本按钮
                TextButtonComponent(),
                // OutlinedButton 轮廓按钮
                OutlinedButtonComponent(),
                // IconButton 图标按钮
                IconButtonComponent(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// IconButton 图标按钮
class IconButtonComponent extends StatelessWidget {
  // 创建一个名为 IconButtonComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const IconButtonComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: IconButton(
        onPressed: () {
          print('点击 OutlinedButton 轮廓按钮');
        },
        // 加载 flutter 自带图标
        icon: const Icon(Icons.add_a_photo_rounded),
      )
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017143844.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017143850.png)

### ⑤、带图标的按钮

- `ElevatedButton`、`TextButton`、`OutlinedButton` 都有一个 `icon` 构造函数，通过它可以轻松创建带图标的按钮

```dart
import 'package:flutter/material.dart';

import '01_基本组件/02_button按钮/01_ElevatedButton漂浮按钮.dart';
import '01_基本组件/02_button按钮/02_TextButton文本按钮.dart';
import '01_基本组件/02_button按钮/03_OutlinedButton轮廓按钮.dart';
import '01_基本组件/02_button按钮/04_IconButton图标按钮.dart';
import '01_基本组件/02_button按钮/05_带图标的按钮.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // ElevatedButton 漂浮按钮
                ElevatedButtonComponent(),
                // TextButton 文本按钮
                TextButtonComponent(),
                // OutlinedButton 轮廓按钮
                OutlinedButtonComponent(),
                // IconButton 图标按钮
                IconButtonComponent(),
                // ButtonWithIconComponent 带图标的按钮
                ButtonWithIconComponent()
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// ButtonWithIconComponent 带图标的按钮
class ButtonWithIconComponent extends StatelessWidget {
  // 创建一个名为 ButtonWithIconComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const ButtonWithIconComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: ElevatedButton.icon(
        onPressed: () {
          print('点击 ElevatedButton 漂浮按钮');
        },
        label: const Text("ElevatedButton 漂浮按钮 带图标"),
        icon: const Icon(Icons.account_balance_wallet_outlined),
      )
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017144522.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017144531.png)

## 3、图片及 ICON

### ①、图片

- Flutter 中，我们可以通过 Image 组件来加载并显示图片，Image 的数据源可以是 asset、文件、内存以及网络。

#### Ⅰ、ImageProvider

1. `ImageProvider` 是一个抽象类，主要定义了图片数据获取的接口 `load()`
2. 从不同的数据源获取图片需要实现不同的 `ImageProvider` 
3. 如 `AssetImage` 是实现了从 `Asset` 中加载图片的 `ImageProvider`，而 `NetworkImage` 实现了从网络加载图片的 `ImageProvider`

#### Ⅱ、Image

1. `Image widget` 有一个必选的 `image` 参数，它对应一个 `ImageProvider`。
2. 下面我们分别演示一下如何从 asset 和网络加载图片

##### （1）、从 asset 中加载图片

1. 将图片复制到目录中

![|379](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017151915.png)

2. 然后在 `pubspec.yaml` 中的 flutter 部分声明图片

```yaml
flutter:
  
  # 下面的行确保 Material Icons 字体
  # 包含在您的应用程序中，以便您可以在
  # material Icons 类中使用这些图标。
  uses-material-design: true

  # 图片配置
  assets:
    - asset/images/QQ图片20220920105928.jpg

  # 字体配置
  fonts:
    # 这表示定义了一个名为 NotoSansCJKjp 的字体系列（font family）。这个系列包含了不同样式和权重的字体
    - family: NotoSansCJKjp
      # 指定了与 NotoSansCJKjp 字体系列相关的字体文件
      fonts:
        # 是 NotoSansCJKjp 字体系列的正常（Regular）字体。它的资源文件位于应用程序的 assets/fonts 目录下
        - asset: asset/fonts/NotoSansCJKjp-Regular.ttf
        # 是 NotoSansCJKjp 字体系列的粗体（Bold）字体。它的资源文件位于应用程序的 assets/fonts 目录下
        - asset: asset/fonts/NotoSansCJKjp-Bold.ttf
```

3. 最后在代码中使用

```dart
import 'package:flutter/material.dart';

import '01_基本组件/03_图片及ICON/01_从asset中加载图片.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // 从 asset 中加载图片
                LoadImagesFromAssetComponent()
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// 从 asset 中加载图片
class LoadImagesFromAssetComponent extends StatelessWidget {
  // 创建一个名为 LoadImagesFromAssetComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const LoadImagesFromAssetComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return const Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: Image(
        image: AssetImage("asset/images/QQ图片20220920105928.jpg"),
        width: 100,
      ),
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017152700.png)

##### （2）、从网络加载图片

```dart
import 'package:flutter/material.dart';

import '01_基本组件/03_图片及ICON/01_从asset中加载图片.dart';
import '01_基本组件/03_图片及ICON/02_从网络加载图片.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // 从 asset 中加载图片
                LoadImagesFromAssetComponent(),
                // 从网络中加载图片
                LoadImagesFromNetworkComponent(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// 从网络中加载图片
class LoadImagesFromNetworkComponent extends StatelessWidget {
  // 创建一个名为 LoadImagesFromNetworkComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const LoadImagesFromNetworkComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return const Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: Image(
        image: NetworkImage("https://img1.baidu.com/it/u=69888158,2774794857&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500"),
        width: 100,
      ),
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017153437.png)

#### Ⅲ、参数

1. Image 在显示图片时定义了一系列参数，通过这些参数我们可以控制图片的显示外观、大小、混合效果等。我们看一下 Image 的主要参数：

```dart
const Image({
  ...
  this.width, //图片的宽
  this.height, //图片高度
  this.color, //图片的混合色值
  this.colorBlendMode, //混合模式
  this.fit,//缩放模式
  this.alignment = Alignment.center, //对齐方式
  this.repeat = ImageRepeat.noRepeat, //重复方式
  ...
})
```

2. `width`、`height`：用于设置图片的宽、高，当不指定宽高时，图片会根据当前父容器的限制，尽可能的显示其原始大小，如果只设置 `width`、`height` 的其中一个，那么另一个属性默认会按比例缩放，`但可以通过下面介绍的fit` 属性来指定适应规则。
3. `fit`：该属性用于在图片的显示空间和图片本身大小不同时指定图片的适应模式。适应模式是在 `BoxFit` 中定义，它是一个枚举类型，有如下值：
	1. `fill`：会拉伸填充满显示空间，图片本身长宽比会发生变化，图片会变形。
	2. `cover`：会按图片的长宽比放大后居中填满显示空间，图片不会变形，超出显示空间部分会被剪裁。
	3. `contain`：这是图片的默认适应规则，图片会在保证图片本身长宽比不变的情况下缩放以适应当前显示空间，图片不会变形。
	4. `fitWidth`：图片的宽度会缩放到显示空间的宽度，高度会按比例缩放，然后居中显示，图片不会变形，超出显示空间部分会被剪裁。
	5. `fitHeight`：图片的高度会缩放到显示空间的高度，宽度会按比例缩放，然后居中显示，图片不会变形，超出显示空间部分会被剪裁。
	6. `none`：图片没有适应策略，会在显示空间内显示图片，如果图片比显示空间大，则显示空间只会显示图片中间部分。
4. 对一个宽高相同的头像图片应用不同的 `fit` 值：

![|400](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017153745.png)

11. `color` 和 `colorBlendMode`：在图片绘制时可以对每一个像素进行颜色混合处理，`color` 指定混合色，而 `colorBlendMode` 指定混合模式，下面是一个简单的示例：

```dart
Image(
  image: AssetImage("images/avatar.png"),
  width: 100.0,
  color: Colors.blue,
  colorBlendMode: BlendMode.difference,
);
```

![|204](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017153935.png)

12. `repeat`：当图片本身大小小于显示空间时，指定图片的重复规则。简单示例如下

![|158](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017154004.png)

#### Ⅳ、Image 缓存

- Flutter 框架对加载过的图片是有缓存的（内存），关于 Image 的详细内容及原理我们将会在后面进阶部分深入介绍

### ②、ICON

#### Ⅰ、介绍

1. Flutter 中，可以像 Web 开发一样使用 `iconfont`，`iconfont` 即“字体图标”，它是将图标做成字体文件，然后通过指定不同的字符而显示不同的图片。
2. 在字体文件中，每一个字符都对应一个位码，而每一个位码对应一个显示字形，不同的字体就是指字形不同，即字符对应的字形是不同的。而在 `iconfont` 中，只是将位码对应的字形做成了图标，所以不同的字符最终就会渲染成不同的图标。
3. 在 Flutter 开发中，`iconfont` 和图片相比有如下优势：
	1. 体积小：可以减小安装包大小。
	2. 矢量的：`iconfont` 都是矢量图标，放大不会影响其清晰度。
	3. 可以应用文本样式：可以像文本一样改变字体图标的颜色、大小对齐等。
	4. 可以通过 `TextSpan` 和文本混用。

#### Ⅱ、使用 Material Design 字体图标

1. Flutter 默认包含了一套 Material Design 的字体图标，在 pubspec.yaml 文件中配置为 `true` 即可启用

```yaml
flutter:
  # 下面的行确保 Material Icons 字体
  # 包含在您的应用程序中，以便您可以在
  # material Icons 类中使用这些图标。
  uses-material-design: true
```

2. Material Design 所有图标可以在其官网查看：https://material.io/tools/icons/
3. 我们看一个简单的例子：

```dart
import 'package:flutter/material.dart';

import '01_基本组件/03_图片及ICON/01_从asset中加载图片.dart';
import '01_基本组件/03_图片及ICON/02_从网络加载图片.dart';
import '01_基本组件/03_图片及ICON/03_使用Material Design字体图标 1.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // 从 asset 中加载图片
                LoadImagesFromAssetComponent(),
                // 从网络中加载图片
                LoadImagesFromNetworkComponent(),
                // 使用 Material Design 字体图标 1
                MaterialDesignIconFont1Component(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// 使用 Material Design 字体图标
class MaterialDesignIconFont1Component extends StatelessWidget {
  // 创建一个名为 MaterialDesignIconFont1Component 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const MaterialDesignIconFont1Component({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return const Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项，即真正显示的组件
      child: Text(
        // 这里定义了三个字体图标
        "\uE03e \uE237 \uE287",
        style: TextStyle(
          fontFamily: "MaterialIcons",
          fontSize: 24.0,
          color: Colors.green,
        ),
      )
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017160214.png)

4. 通过这个示例可以看到，使用图标就像使用文本一样，但是这种方式需要我们提供每个图标的码点，这对开发者并不友好，所以，Flutter 封装了 IconData 和 Icon 来专门显示字体图标，上面的例子也可以用如下方式实现：
5. Icons 类中包含了所有 Material Design 图标的 IconData 静态变量定义

```dart
import 'package:flutter/material.dart';

import '01_基本组件/03_图片及ICON/01_从asset中加载图片.dart';
import '01_基本组件/03_图片及ICON/02_从网络加载图片.dart';
import '01_基本组件/03_图片及ICON/03_使用Material Design字体图标 1.dart';
import '01_基本组件/03_图片及ICON/03_使用Material Design字体图标 2.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // 从 asset 中加载图片
                LoadImagesFromAssetComponent(),
                // 从网络中加载图片
                LoadImagesFromNetworkComponent(),
                // 使用 Material Design 字体图标 1
                MaterialDesignIconFont1Component(),
                // 使用 Material Design 字体图标 2
                MaterialDesignIconFont2Component(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入Flutter的material包，包含Flutter应用程序的核心功能。
import 'package:flutter/material.dart';

// 使用 Material Design 字体图标 2
class MaterialDesignIconFont2Component extends StatelessWidget {
  // 创建一个名为 MaterialDesignIconFont2Component 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const MaterialDesignIconFont2Component({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Directionality：用于确定文本的显示方向。
    return const Directionality(
      // 设置文本方向为从左到右（Left To Right）
      textDirection: TextDirection.ltr,
      // 设置 Directionality 组件中的子项；Row 是 Flutter 中的一个小部件，用于在水平方向排列其子小部件
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        // 设置 Row 组件中的子项；即真正显示的组件
        children: <Widget>[
          Icon(Icons.accessible, color: Colors.green),
          Icon(Icons.error, color: Colors.green),
          Icon(Icons.fingerprint, color: Colors.green),
        ],
      ),
    );
  }
}
```

## 4、单选开关和复选框

### ①、简介

1. Material 组件库中提供了 Material 风格的单选开关 `Switch` 和复选框 `Checkbox`
2. 虽然它们都是继承自 `StatefulWidget`，但它们本身不会保存当前选中状态，选中状态都是由父组件来管理的。
3. 当 `Switch` 或 `Checkbox` 被点击时，会触发它们的 onChanged 回调，我们可以在此回调中处理选中状态改变逻辑。下面看一个简单的例子：



```dart
import 'package:flutter/material.dart';

import '01_基本组件/04_单选开关和复选框/SwitchAndCheckBoxTestRoute.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                SwitchAndCheckBoxTestRoute()
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类，用于显示开关按钮和复选框
class SwitchAndCheckBoxTestRoute extends StatefulWidget {
  const SwitchAndCheckBoxTestRoute({super.key});

  // 用于在 StatefulWidget 和其对应的 State 之间建立关联，以便管理界面的状态
  @override
  SwitchAndCheckBoxTestRouteState createState() => SwitchAndCheckBoxTestRouteState();
}

/*
  创建与上述 StatefulWidget 相关的状态类
  SwitchAndCheckBoxTestRoute 类是一个 StatefulWidget，它通常用于表示整个 Widget。在这种情况下，它表示包含开关按钮和复选框的整个部分。
  SwitchAndCheckBoxTestRoute 类的主要职责是创建 SwitchAndCheckBoxTestRouteState 类的实例，它通过 createState 方法与其状态关联。
  SwitchAndCheckBoxTestRouteState 类是 SwitchAndCheckBoxTestRoute 的状态类。
  它包含了应用程序的状态信息，例如开关按钮和复选框的状态，以及构建用户界面的逻辑。
  通过 createState 方法，SwitchAndCheckBoxTestRoute 在需要时创建了一个 SwitchAndCheckBoxTestRouteState 实例，这个状态类用于管理界面的状态和行为
  总之，SwitchAndCheckBoxTestRoute 是 SwitchAndCheckBoxTestRouteState 的父类，负责创建和管理状态类的实例，
  而 SwitchAndCheckBoxTestRouteState 则包含了实际的界面状态和构建逻辑。这是 Flutter 中使用 StatefulWidget 和其对应的 State 的常见模式。
 */
class SwitchAndCheckBoxTestRouteState extends State<SwitchAndCheckBoxTestRoute> {
  // 维护单选开关状态，默认关闭
  bool _switchSelected = false;
  // 维护复选框状态，默认不选中
  bool _checkboxSelected = false;

  @override
  Widget build(BuildContext context) {
    // 构建界面的主体部分，包括开关和复选框；Column：用于在垂直方向上排列子组件
    return Column(
      children: <Widget>[
        // 创建一个开关组件
        Switch(
          // 当前开关状态
          value: _switchSelected,
          // 状态改变回调
          onChanged:(value){
            print('点击开关组件，点击后状态为：$value');
            // 当用户改变开关状态时触发的回调函数，重新构建页面
            setState(() {
              // 更新开关状态
              _switchSelected = value;
            });
          },
        ),
        // 创建一个复选框组件
        Checkbox(
          // 当前复选框状态
          value: _checkboxSelected,
          //选中时的颜色
          activeColor: Colors.red,
          // 状态改变回调
          onChanged:(value){
            print('点击复选框组件，点击后状态为：$value');
            // 当用户改变复选框状态时触发的回调函数
            setState(() {
              // 更新复选框状态
              _checkboxSelected = value!;
            });
          } ,
        )
      ],
    );
  }
}
```

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017164807.png)

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231017164814.png)

### ②、属性及外观

1. `Switch` 和 `Checkbox` 属性比较简单，它们都有一个 `activeColor` 属性，用于设置激活态的颜色。
2. 至于大小，到目前为止，`Checkbox` 的大小是固定的，无法自定义
3. 而 `Switch` 只能定义宽度，高度也是固定的。
4. 值得一提的是 `Checkbox` 有一个属性 `tristate` ，表示是否为三态，
	1. 其默认值为 `false` ，这时 `Checkbox` 有两种状态即“选中”和“不选中”，对应的 value 值为 true 和 false
	2. 如果 `tristate` 值为 `true` 时，`value` 的值会增加一个状态 `null`

### ③、注意

1. 通过 `Switch` 和 `Checkbox` 我们可以看到，虽然它们本身是与状态（是否选中）关联的，但它们却不是自己来维护状态，而是需要父组件来管理状态，然后当用户点击时，再通过事件通知给父组件
2. 这样是合理的，因为 `Switch` 和 `Checkbox` 是否选中本就和用户数据关联，而这些用户数据也不可能是它们的私有状态。
3. 我们在自定义组件时也应该思考一下哪种状态的管理方式最为合理。

## 5、输入框及表单

### ①、TextField 文本输入

#### Ⅰ、主要属性介绍

```dart
const TextField({
  ...
  /**
   * 编辑框的控制器，通过它可以设置/获取编辑框的内容、选择编辑内容、监听编辑文本改变事件。
   * 大多数情况下我们都需要显式提供一个 controller 来与文本框交互。如果没有提供 controller，则 TextField 内部会自动创建一个
   */
  TextEditingController controller,
  // 用于控制 TextField 是否占有当前键盘的输入焦点。它是我们和键盘交互的一个句柄（handle）
  FocusNode focusNode,
  // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
  InputDecoration decoration = const InputDecoration(),
  /**
   * 用于设置该输入框默认的键盘输入类型，取值如下：
   *    text：文本输入键盘
   *    multiline：多行文本，需和maxLines配合使用(设为null或大于1)
   *    number：数字；会弹出数字键盘
   *    phone：优化后的电话号码输入键盘；会弹出数字键盘并显示 “* #”
   *    datetime：优化后的日期输入键盘；Android 上会显示 “: -”
   *    emailAddress：优化后的电子邮件地址；会显示 “@ .”
   *    url：优化后的 url 输入键盘； 会显示 “/ .”
   */
  TextInputType keyboardType,
  // 键盘动作按钮图标(即回车键位图标)，它是一个枚举值，有多个可选值
  TextInputAction textInputAction,
  // 正在编辑的文本样式
  TextStyle style,
  // 输入框内编辑文本在水平方向的对齐方式
  TextAlign textAlign = TextAlign.start,
  // 是否自动获取焦点
  bool autofocus = false,
  // 是否隐藏正在编辑的文本，如用于输入密码的场景等，文本内容会用“•”替换
  bool obscureText = false,
  // 输入框的最大行数，默认为1；如果为null，则无行数限制
  int maxLines = 1,
  // 代表输入框文本的最大长度，设置后输入框右下角会显示输入的文本计数
  int maxLength,
  // 决定当输入文本长度超过 maxLength 时如何处理，如截断、超出等
  this.maxLengthEnforcement,
  // 长按或鼠标右击时出现的菜单，包括 copy、cut、paste 以及 selectAll
  ToolbarOptions? toolbarOptions,
  // 输入框内容改变时的回调函数；注：内容改变事件也可以通过 controller 来监听
  ValueChanged<String> onChanged,
  /**
   * onEditingComplete 和 onSubmitted：这两个回调都是在输入框输入完成时触发
   * 比如按了键盘的完成键（对号图标）或搜索键（🔍图标）。不同的是两个回调签名不同
   * onSubmitted 回调是 ValueChanged<String> 类型，它接收当前输入内容做为参数
   * 而 onEditingComplete 不接收参数
   */
  VoidCallback onEditingComplete,
  ValueChanged<String> onSubmitted,
  // 用于指定输入格式；当用户输入内容改变时，会根据指定的格式来校验
  List<TextInputFormatter> inputFormatters,
  // 如果为 false，则输入框会被禁用，禁用状态不能响应输入和事件，同时显示禁用态样式（在其 decoration 中定义）
  bool enabled,
  // 自定义输入框光标宽度
  this.cursorWidth = 2.0,
  // 自定义输入框圆角
  this.cursorRadius,
  // 自定义输入框颜色
  this.cursorColor,
  this.onTap,
  ...
})
```

#### Ⅱ、登录输入框示例布局

```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                TextFieldComponent()
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class TextFieldComponent extends StatelessWidget {
  const TextFieldComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return const Column(
      children: <Widget>[
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person)
          ),
        ),
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: InputDecoration(
              labelText: "密码",
              hintText: "用户名登录密码",
              prefixIcon: Icon(Icons.person)
          ),
        ),
      ],
    );
  }
}
```

![|400](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231019153255.png)

#### Ⅲ、获取输入内容

1. 获取输入内容有两种方式：
	1. 定义两个变量，用于保存用户名和密码，然后在 onChange 触发时，各自保存一下输入内容。
	2. 通过 controller 直接获取。

```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入_获取输入内容.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 实例化 TextFieldComponent 类
    TextField1Component textField1Component = TextField1Component();

    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // TextFieldComponent 类实例化的对象
                textField1Component,
                // 按钮组件
                ElevatedButton(
                  // 点击事件
                  onPressed: (){
                    print('密码：${textFieldComponent.pwdController.text}');
                  },
                  child: const Text("点击打印密码")
                )
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class TextField1Component extends StatelessWidget {
  TextField1Component({Key? key}) : super(key: key);

  // 定义一个 controller
  final TextEditingController pwdController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    // 创建一个变量，用户名输入框每次变化时都对其赋值
    String userName = "";

    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return Column(
      children: <Widget>[
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person)
          ),
          // 输入框内容改变时的回调函数
          onChanged: (value){
            // 用户名输入框每次变化时都对 userName 赋值
            userName = value;
          },
        ),
        ElevatedButton(
            onPressed: (){
              print('用户名：$userName');
            },
            child: const Text("点击打印用户名")
        ),
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
              labelText: "密码",
              hintText: "用户名登录密码",
              prefixIcon: Icon(Icons.person)
          ),
          controller: pwdController
        ),
      ],
    );
  }
}
```

#### Ⅳ、监听文本变化

1. 监听文本变化也有两种方式：
	1. 设置 `onChange` 回调，上面用户名以展示，此处不再详写
	2. 通过 `controller` 监听
2. 两种方式相比，`onChanged` 是专门用于监听文本变化，而 `controller` 的功能却多一些，除了能监听文本变化外，它还可以设置默认值、选择文本等

```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入_获取输入内容.dart';
import '01_基本组件/05_输入框及表单/02_TextField 文本输入_监听文本变化.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // TextFieldComponent 类实例化的对象
                TextField2Component(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TextField2Component extends StatefulWidget {
  const TextField2Component({Key? key}) : super(key: key);

  @override
  TextFieldComponentState createState() => TextFieldComponentState();
}

/*
  创建与上述 StatefulWidget 相关的状态类
  SwitchAndCheckBoxTestRoute 类是一个 StatefulWidget，它通常用于表示整个 Widget。在这种情况下，它表示包含开关按钮和复选框的整个部分。
  SwitchAndCheckBoxTestRoute 类的主要职责是创建 SwitchAndCheckBoxTestRouteState 类的实例，它通过 createState 方法与其状态关联。
  SwitchAndCheckBoxTestRouteState 类是 SwitchAndCheckBoxTestRoute 的状态类。
  它包含了应用程序的状态信息，例如开关按钮和复选框的状态，以及构建用户界面的逻辑。
  通过 createState 方法，SwitchAndCheckBoxTestRoute 在需要时创建了一个 SwitchAndCheckBoxTestRouteState 实例，这个状态类用于管理界面的状态和行为
  总之，SwitchAndCheckBoxTestRoute 是 SwitchAndCheckBoxTestRouteState 的父类，负责创建和管理状态类的实例，
  而 SwitchAndCheckBoxTestRouteState 则包含了实际的界面状态和构建逻辑。这是 Flutter 中使用 StatefulWidget 和其对应的 State 的常见模式。
 */
class TextFieldComponentState extends State<TextField2Component> {
  // 定义一个 controller
  final TextEditingController pwdController = TextEditingController();

  @override
  void initState() {
    super.initState();
    // 设置默认值
    pwdController.text="hello world!";
    // 监听输入改变
    pwdController.addListener(() {
      print("密码改变了：${pwdController.text}");
    });
  }

  @override
  Widget build(BuildContext context) {
    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return Column(
      children: <Widget>[
        const TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: InputDecoration(
              labelText: "用户名",
              hintText: "用户名或邮箱",
              prefixIcon: Icon(Icons.person)
          ),
        ),
        TextField(
          // 是否自动获取焦点
            autofocus: false,
            // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
            decoration: const InputDecoration(
                labelText: "密码",
                hintText: "用户名登录密码",
                prefixIcon: Icon(Icons.person)
            ),
            controller: pwdController
        ),
      ],
    );
  }
}
```

#### Ⅴ、控制焦点

1. 焦点可以通过 `FocusNode` 和 `FocusScopeNode` 来控制
2. 默认情况下，焦点由 `FocusScope` 来管理，它代表焦点控制范围，可以在这个范围内可以通过 `FocusScopeNode` 在输入框之间移动焦点、设置默认焦点等。
3. 我们可以通过 `FocusScope.of(context)` 来获取 `Widget` 树中默认的 `FocusScopeNode`。
4. 下面看一个示例，在此示例中创建两个 `TextField`，第一个自动获取焦点，然后创建两个按钮：
	1. 点击第一个按钮可以将焦点从第一个 `TextField` 挪到第二个 `TextField`。
	2. 点击第二个按钮可以关闭键盘。

```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入_获取输入内容.dart';
import '01_基本组件/05_输入框及表单/02_TextField 文本输入_监听文本变化.dart';
import '01_基本组件/05_输入框及表单/03_TextField 文本输入_控制焦点.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // TextFieldComponent 类实例化的对象
                TextField3Component(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TextField3Component extends StatefulWidget {
  const TextField3Component({Key? key}) : super(key: key);

  @override
  TextFieldComponentState createState() => TextFieldComponentState();
}

/*
  创建与上述 StatefulWidget 相关的状态类
  SwitchAndCheckBoxTestRoute 类是一个 StatefulWidget，它通常用于表示整个 Widget。在这种情况下，它表示包含开关按钮和复选框的整个部分。
  SwitchAndCheckBoxTestRoute 类的主要职责是创建 SwitchAndCheckBoxTestRouteState 类的实例，它通过 createState 方法与其状态关联。
  SwitchAndCheckBoxTestRouteState 类是 SwitchAndCheckBoxTestRoute 的状态类。
  它包含了应用程序的状态信息，例如开关按钮和复选框的状态，以及构建用户界面的逻辑。
  通过 createState 方法，SwitchAndCheckBoxTestRoute 在需要时创建了一个 SwitchAndCheckBoxTestRouteState 实例，这个状态类用于管理界面的状态和行为
  总之，SwitchAndCheckBoxTestRoute 是 SwitchAndCheckBoxTestRouteState 的父类，负责创建和管理状态类的实例，
  而 SwitchAndCheckBoxTestRouteState 则包含了实际的界面状态和构建逻辑。这是 Flutter 中使用 StatefulWidget 和其对应的 State 的常见模式。
 */
class TextFieldComponentState extends State<TextField3Component> {
  FocusNode focusNode1 = FocusNode();
  FocusNode focusNode2 = FocusNode();
  FocusScopeNode? focusScopeNode;

  @override
  Widget build(BuildContext context) {
    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return Column(
      children: <Widget>[
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person),
          ),
          // 关联 focusNode1
          focusNode: focusNode1
        ),
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
            labelText: "密码",
            hintText: "用户名登录密码",
            prefixIcon: Icon(Icons.person)
          ),
          // 关联 focusNode2
          focusNode: focusNode2
        ),
        ElevatedButton(
          onPressed: (){
            // 如果 focusScopeNode 为空，则执行后面的逻辑；给 focusScopeNode 赋值
            focusScopeNode ??= FocusScope.of(context);
            // 如果 focusScopeNode 不为空，则执行后面的逻辑；使 focusNode2 获取焦点
            focusScopeNode?.requestFocus(focusNode2);
          },
          child: const Text("移动焦点")
        ),
        ElevatedButton(
          onPressed: (){
            // 当所有编辑框都失去焦点时键盘就会收起
            focusNode1.unfocus();
            focusNode2.unfocus();
          },
          child: const Text("隐藏键盘")
        )
      ],
    );
  }
}
```

#### Ⅵ、监听焦点状态改变事件

- `FocusNode` 继承自 `ChangeNotifier`，通过 `FocusNode` 可以监听焦点的改变事件

```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入_获取输入内容.dart';
import '01_基本组件/05_输入框及表单/02_TextField 文本输入_监听文本变化.dart';
import '01_基本组件/05_输入框及表单/03_TextField 文本输入_控制焦点.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // TextFieldComponent 类实例化的对象
                TextField3Component(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TextField3Component extends StatefulWidget {
  const TextField3Component({Key? key}) : super(key: key);

  @override
  TextFieldComponentState createState() => TextFieldComponentState();
}

/*
  创建与上述 StatefulWidget 相关的状态类
  SwitchAndCheckBoxTestRoute 类是一个 StatefulWidget，它通常用于表示整个 Widget。在这种情况下，它表示包含开关按钮和复选框的整个部分。
  SwitchAndCheckBoxTestRoute 类的主要职责是创建 SwitchAndCheckBoxTestRouteState 类的实例，它通过 createState 方法与其状态关联。
  SwitchAndCheckBoxTestRouteState 类是 SwitchAndCheckBoxTestRoute 的状态类。
  它包含了应用程序的状态信息，例如开关按钮和复选框的状态，以及构建用户界面的逻辑。
  通过 createState 方法，SwitchAndCheckBoxTestRoute 在需要时创建了一个 SwitchAndCheckBoxTestRouteState 实例，这个状态类用于管理界面的状态和行为
  总之，SwitchAndCheckBoxTestRoute 是 SwitchAndCheckBoxTestRouteState 的父类，负责创建和管理状态类的实例，
  而 SwitchAndCheckBoxTestRouteState 则包含了实际的界面状态和构建逻辑。这是 Flutter 中使用 StatefulWidget 和其对应的 State 的常见模式。
 */
class TextFieldComponentState extends State<TextField3Component> {
  FocusNode focusNode1 = FocusNode();
  FocusNode focusNode2 = FocusNode();
  FocusScopeNode? focusScopeNode;

  @override
  Widget build(BuildContext context) {
    focusNode1.addListener(() {
      print('用户名 输入框的焦点改变了');
    });
    
    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return Column(
      children: <Widget>[
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person),
          ),
          // 关联 focusNode1
          focusNode: focusNode1
        ),
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: const InputDecoration(
            labelText: "密码",
            hintText: "用户名登录密码",
            prefixIcon: Icon(Icons.person)
          ),
          // 关联 focusNode2
          focusNode: focusNode2
        ),
        ElevatedButton(
          onPressed: (){
            // 如果 focusScopeNode 为空，则执行后面的逻辑；给 focusScopeNode 赋值
            focusScopeNode ??= FocusScope.of(context);
            // 如果 focusScopeNode 不为空，则执行后面的逻辑；使 focusNode2 获取焦点
            focusScopeNode?.requestFocus(focusNode2);
          },
          child: const Text("移动焦点")
        ),
        ElevatedButton(
          onPressed: (){
            // 当所有编辑框都失去焦点时键盘就会收起
            focusNode1.unfocus();
            focusNode2.unfocus();
          },
          child: const Text("隐藏键盘")
        )
      ],
    );
  }
}
```

#### Ⅶ、自定义样式

- 一般来说，优先通过 `decoration` 来自定义样式，如果 `decoration` 实现不了，再用 `widget` 组合的方式


```dart
import 'package:flutter/material.dart';

import '01_基本组件/05_输入框及表单/01_TextField 文本输入_获取输入内容.dart';
import '01_基本组件/05_输入框及表单/02_TextField 文本输入_监听文本变化.dart';
import '01_基本组件/05_输入框及表单/03_TextField 文本输入_控制焦点.dart';
import '01_基本组件/05_输入框及表单/04_TextField 文本输入_自定义样式.dart';

// 入口方法
void main() => runApp(const WhiteBackgroundComponent());

// 定义白色背景
class WhiteBackgroundComponent extends StatelessWidget {
  // 创建一个名为 WhiteBackgroundComponent 的自定义小部件，继承自 StatelessWidget，接受一个可选的 Key 参数。
  const WhiteBackgroundComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建一个 MaterialApp 小部件，这是 Flutter 应用程序的根小部件。
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        // 设置顶部应用栏
        appBar: AppBar(
          // 设置顶部应用栏的标题文本
          title: const Text('White Background'),
        ),
        /**
	     * body: 用于定义页面的主要内容区域
	     * Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
	     * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
	     */
        body: const Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 控制子组件在主轴方向上的对齐方式。在 Column 中，主轴通常是垂直方向
            mainAxisAlignment: MainAxisAlignment.center,
              // 指定要放置在容器内的子组件列表
              children: [
                // TextFieldComponent 类实例化的对象
                TextFieldStyleComponent(),
              ]
          )
        ),
      ),
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class TextFieldStyleComponent extends StatefulWidget {
  const TextFieldStyleComponent({Key? key}) : super(key: key);

  @override
  TextFieldComponentState createState() => TextFieldComponentState();
}

/*
  创建与上述 StatefulWidget 相关的状态类
  SwitchAndCheckBoxTestRoute 类是一个 StatefulWidget，它通常用于表示整个 Widget。在这种情况下，它表示包含开关按钮和复选框的整个部分。
  SwitchAndCheckBoxTestRoute 类的主要职责是创建 SwitchAndCheckBoxTestRouteState 类的实例，它通过 createState 方法与其状态关联。
  SwitchAndCheckBoxTestRouteState 类是 SwitchAndCheckBoxTestRoute 的状态类。
  它包含了应用程序的状态信息，例如开关按钮和复选框的状态，以及构建用户界面的逻辑。
  通过 createState 方法，SwitchAndCheckBoxTestRoute 在需要时创建了一个 SwitchAndCheckBoxTestRouteState 实例，这个状态类用于管理界面的状态和行为
  总之，SwitchAndCheckBoxTestRoute 是 SwitchAndCheckBoxTestRouteState 的父类，负责创建和管理状态类的实例，
  而 SwitchAndCheckBoxTestRouteState 则包含了实际的界面状态和构建逻辑。这是 Flutter 中使用 StatefulWidget 和其对应的 State 的常见模式。
 */
class TextFieldComponentState extends State<TextFieldStyleComponent> {
  @override
  Widget build(BuildContext context) {
    // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
    return Column(
      children: <Widget>[
        const TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person),
            // 未获得焦点下划线设为红色
            enabledBorder: UnderlineInputBorder(
              borderSide: BorderSide(color: Colors.red)
            ),
            // 未获得焦点下划线设为黄色
            focusedBorder: UnderlineInputBorder(
                borderSide: BorderSide(color: Colors.amberAccent)
            ),
          ),
        ),
        TextField(
          // 是否自动获取焦点
          autofocus: false,
          // 用于控制 TextField 的外观显示，如提示文本、背景颜色、边框等。
          decoration: InputDecoration(
            labelText: "密码",
            hintText: "用户名登录密码",
            prefixIcon: const Icon(Icons.person),
            // 文本框的边框样式
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
            ),
            // 文本框在非焦点状态下的边框样式
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
              borderSide: BorderSide(color: Colors.grey),
            ),
            // 文本框在焦点状态下的边框样式
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
              borderSide: BorderSide(color: Colors.blue),
            ),
            // 文本框在有错误时的边框样式
            errorBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
              borderSide: BorderSide(color: Colors.red),
            ),
            // 文本框在焦点状态下有错误时的边框样式
            focusedErrorBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
              borderSide: BorderSide(color: Colors.red),
            ),
          )
        ),
      ],
    );
  }
}
```

### ②、Form 表单

#### Ⅰ、简介

1. 实际业务中，在正式向服务器提交数据前，都会对各个输入框数据进行合法性校验，但是对每一个 `TextField` 都分别进行校验将会是一件很麻烦的事。
2. 还有，如果用户想清除一组 `TextField` 的内容，除了一个一个清除有没有什么更好的办法呢？
3. 为此，`Flutter` 提供了一个 `Form` 组件，它可以对输入框进行分组，然后进行一些统一操作，如输入内容校验、输入框重置以及输入内容保存

#### Ⅱ、Form

1. Form 继承自StatefulWidget对象，它对应的状态类为 `FormState`。
2. `Form` 类的定义：

```dart
Form({
  required Widget child,
  /**
   * 是否自动校验输入内容；当为 true 时，每一个子 FormField 内容发生变化时都会自动校验合法性，并直接显示错误信息。
   * 否则，需要通过调用 FormState.validate()来手动校验
   */
  bool autovalidate = false,
  /**
   * 决定 Form 所在的路由是否可以直接返回（如点击返回按钮）
   * 该回调返回一个 Future 对象，如果 Future 的最终结果是 false，则当前路由不会返回；
   * 如果为 true，则会返回到上一个路由。此属性通常用于拦截返回按钮
   */
  WillPopCallback onWillPop,
  /**
   * Form 的任意一个子 FormField 内容发生变化时会触发此回调
   */
  VoidCallback onChanged,
})
```

#### Ⅲ、FormField

1. `Form` 的子孙元素必须是 `FormField` 类型，`FormField` 是一个抽象类，定义几个属性，`FormState` 内部通过它们来完成操作，`FormField` 部分定义如下：
2. 为了方便使用，`Flutter` 提供了一个 `TextFormField` 组件，它继承自 `FormField` 类，也是 `TextField` 的一个包装类，所以除了 `FormField` 定义的属性之外，它还包括 `TextField` 的属性

```dart
const FormField({
  ...
  FormFieldSetter<T> onSaved, // 保存回调
  FormFieldValidator<T>  validator, // 验证回调
  T initialValue, // 初始值
  bool autovalidate = false, // 是否自动校验。
})
```

#### Ⅳ、FormState

1. `FormState` 为 `Form` 的 `State` 类，可以通过 `Form.of()` 或 `GlobalKey` 获得。我们可以通过它来对 `Form` 的子孙 `FormField` 进行统一操作。我们看看其常用的三个方法：
2. `FormState.validate()`：调用此方法后，会调用 `Form` 子孙 `FormField` 的 `validate` 回调，如果有一个校验失败，则返回 `false`，所有校验失败项都会返回用户返回的错误提示。
3. `FormState.save()`：调用此方法后，会调用 `Form` 子孙 `FormField` 的 `save` 回调，用于保存表单内容
4. `FormState.reset()`：调用此方法后，会将子孙 `FormField` 的内容清空

## 6、进度指示器

### ①、简介

1. Material 组件库中提供了两种进度指示器：`LinearProgressIndicator` 和 `CircularProgressIndicator`，它们都可以同时用于精确的进度指示和模糊的进度指示。
2. 精确进度通常用于任务进度可以计算和预估的情况，比如文件下载；
3. 而模糊进度则用户任务进度无法准确获得的情况，如下拉刷新，数据提交等

### ②、LinearProgressIndicator 线性进度条

1. LinearProgressIndicator 是一个线性、条状的进度条，定义如下：

```dart
LinearProgressIndicator({
  /**
   * value 表示当前的进度，取值范围为 [0,1]；
   * 如果 value 为 null 时则指示器会执行一个循环动画（模糊进度）；
   * 当 value 不为 null 时，指示器为一个具体进度的进度条
   */
  double value,
  /**
   * 指示器的背景色
   */
  Color backgroundColor,
  /**
   * 指示器的进度条颜色；
   * 值得注意的是，该值类型是 Animation<Color>，这允许我们指定进度条的颜色和动画。
   * 换言之，我们想对进度条应用一种固定的颜色，此时我们可以通过 AlwaysStoppedAnimation 来指定
   */
  Animation<Color> valueColor,
  ...
})
```

2. 例子：

```dart
import 'package:flutter/material.dart';

import '01_基本组件/ 06_进度指示器/01_LinearProgressIndicator 线性进度条.dart';

// 入口方法
void main() => runApp(const LinearProgressIndicatorComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class LinearProgressIndicatorComponent extends StatefulWidget  {
  const LinearProgressIndicatorComponent({Key? key}) : super(key: key);

  @override
  State<LinearProgressIndicatorComponent> createState() => _LinearProgressIndicatorComponentState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _LinearProgressIndicatorComponentState extends State<LinearProgressIndicatorComponent>{
  // 表示进度条的当前进度
  double progress = 0.0;

  /// 这是一个重写的方法，它在小部件被插入到小部件树中时被调用。
  /// 在这个方法中，调用了父类的 initState 方法，并且调用了 startTimer 方法
  @override
  void initState() {
    super.initState();
    startTimer();
  }

  // 定时增加进度条进度
  void startTimer() {
    // 启动一个定时器，每秒触发一次
    Timer.periodic(const Duration(seconds: 1), (timer) {
      // 调用 setState 方法，告诉 Flutter 框架 progress 的值已经改变，需要重新构建界面
      setState(() {
        progress += 0.05;
        if (progress > 1.0) {
          progress = 0.0;
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
         * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
         */
        body: Center(
            // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
            child: Column(
              // 垂直居中
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                // 模糊进度条(会执行一个动画)
                LinearProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.blue),
                ),
                // 两个进度条之间的距离
                const SizedBox(height: 50.0),
                // 进度条显示50%
                LinearProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.blue),
                  value: progress,
                )
              ],
            )
        ),
      ),
    );
  }
}
```

![|394](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231020160120.png)

### ③、CircularProgressIndicator 圆形进度条

1. `CircularProgressIndicator` 是一个圆形进度条，定义如下

```dart
CircularProgressIndicator({
  /**
   * value 表示当前的进度，取值范围为 [0,1]；
   * 如果 value 为 null 时则指示器会执行一个循环动画（模糊进度）；
   * 当 value 不为 null 时，指示器为一个具体进度的进度条
   */
  double value,
  /**
   * 指示器的背景色
   */
  Color backgroundColor,
  /**
   * 指示器的进度条颜色；
   * 值得注意的是，该值类型是 Animation<Color>，这允许我们指定进度条的颜色和动画。
   * 换言之，我们想对进度条应用一种固定的颜色，此时我们可以通过 AlwaysStoppedAnimation 来指定
   */
  Animation<Color> valueColor,
  // strokeWidth 表示圆形进度条的粗细
  this.strokeWidth = 4.0,
  ...
})
```

2. 例子：

```dart
import 'package:flutter/material.dart';

import '01_基本组件/ 06_进度指示器/01_LinearProgressIndicator 线性进度条.dart';
import '01_基本组件/ 06_进度指示器/02_CircularProgressIndicator 圆形进度条.dart';

// 入口方法
void main() => runApp(const CircularProgressIndicatorComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class CircularProgressIndicatorComponent extends StatefulWidget  {
  const CircularProgressIndicatorComponent({Key? key}) : super(key: key);

  @override
  State<CircularProgressIndicatorComponent> createState() => _CircularProgressIndicatorComponentState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _CircularProgressIndicatorComponentState extends State<CircularProgressIndicatorComponent>{
  // 表示进度条的当前进度
  double progress = 0.0;

  /// 这是一个重写的方法，它在小部件被插入到小部件树中时被调用。
  /// 在这个方法中，调用了父类的 initState 方法，并且调用了 startTimer 方法
  @override
  void initState() {
    super.initState();
    startTimer();
  }

  // 定时增加进度条进度
  void startTimer() {
    // 启动一个定时器，每秒触发一次
    Timer.periodic(const Duration(seconds: 1), (timer) {
      // 调用 setState 方法，告诉 Flutter 框架 progress 的值已经改变，需要重新构建界面
      setState(() {
        progress += 0.05;
        if (progress > 1.0) {
          progress = 0.0;
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
         * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
         */
        body: Center(
            // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
            child: Column(
              // 垂直居中
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                // 模糊进度条(会执行一个动画)
                CircularProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.blue),
                  strokeWidth: 5,
                ),
                // 两个进度条之间的距离
                const SizedBox(height: 50.0),
                // 进度条显示50%
                CircularProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.green),
                  value: progress,
                  strokeWidth: 10,
                )
              ],
            )
        ),
      ),
    );
  }
}
```

![|394](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231020160041.png)

### ④、自定义尺寸

1. 我们可以发现 `LinearProgressIndicator` 和 `CircularProgressIndicator`，并没有提供设置圆形进度条尺寸的参数；如果我们希望 `LinearProgressIndicator` 的线细一些，或者希望 `CircularProgressIndicator` 的圆大一些该怎么做？
2. 其实 `LinearProgressIndicator` 和 `CircularProgressIndicator` 都是取父容器的尺寸作为绘制的边界的。知道了这点，我们便可以通过尺寸限制类 `Widget`，如 `ConstrainedBox`、`SizedBox`：

```dart
import 'package:flutter/material.dart';

import '01_基本组件/ 06_进度指示器/03_自定义尺寸.dart.dart';

// 入口方法
void main() => runApp(const ProgressIndicatorSizeComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

// 创建一个 StatefulWidget 类
class ProgressIndicatorSizeComponent extends StatefulWidget  {
  const ProgressIndicatorSizeComponent({Key? key}) : super(key: key);

  @override
  State<ProgressIndicatorSizeComponent> createState() => _ProgressIndicatorSizeComponentState();
}

// 创建与上述 StatefulWidget 相关的状态类
class _ProgressIndicatorSizeComponentState extends State<ProgressIndicatorSizeComponent>{
  // 表示进度条的当前进度
  double progress = 0.0;

  /// 这是一个重写的方法，它在小部件被插入到小部件树中时被调用。
  /// 在这个方法中，调用了父类的 initState 方法，并且调用了 startTimer 方法
  @override
  void initState() {
    super.initState();
    startTimer();
  }

  // 定时增加进度条进度
  void startTimer() {
    // 启动一个定时器，每秒触发一次
    Timer.periodic(const Duration(seconds: 1), (timer) {
      // 调用 setState 方法，告诉 Flutter 框架 progress 的值已经改变，需要重新构建界面
      setState(() {
        progress += 0.05;
        if (progress > 1.0) {
          progress = 0.0;
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
         * 它将其子小部件居中显示，并根据需要调整大小；此处 Center 小部件用于将 Column 小部件放置在屏幕的中心位置
         */
        body: Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 垂直居中
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              SizedBox(
                height: 20,
                // 线性模糊进度条(会执行一个动画)
                child: LinearProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.blue),
                ),
              ),
              // 两个进度条之间的距离
              const SizedBox(height: 50.0),
              SizedBox(
                width: 100,
                height: 100,
                // 圆形进度条
                child: CircularProgressIndicator(
                  backgroundColor: Colors.grey[200],
                  valueColor: const AlwaysStoppedAnimation(Colors.green),
                  value: progress,
                  strokeWidth: 10,
                )
              )
            ],
          )
        ),
      ),
    );
  }
}
```

![|394](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231020161209.png)

# 四、布局类组件

## 1、简介

1. 布局类组件都会包含一个或多个子组件，不同的布局类组件对子组件排列（layout）方式不同

| Widget                        | 说明             | 用途                                                                                   |
| ----------------------------- | ---------------- | -------------------------------------------------------------------------------------- |
| LeafRenderObjectWidget        | 非容器类组件基类 | Widget 树的叶子节点，用于没有子节点的 widget，通常基础组件都属于这一类，如 Image。        |
| SingleChildRenderObjectWidget | 单子组件基类     | 包含一个子 Widget，如：ConstrainedBox、DecoratedBox 等                                   |
| MultiChildRenderObjectWidget  | 多子组件基类     | 包含多个子 Widget，一般都有一个 children 参数，接受一个 Widget 数组。<br>如 Row、Column、Stack 等 |

2. 布局类组件就是指直接或间接继承(包含) `SingleChildRenderObjectWidget` 和 `MultiChildRenderObjectWidget` 的 `Widget`，它们一般都会有一个 `child` 或 `children` 属性用于接收子 `Widget`。
3. 我们看一下继承关系 `Widget > RenderObjectWidget > (Leaf/SingleChild/MultiChild)RenderObjectWidget` 。
4. `RenderObjectWidget` 类中定义了创建、更新 `RenderObject` 的方法，子类必须实现他们，关于 `RenderObject` 我们现在只需要知道它是最终布局、渲染 UI 界面的对象即可，也就是说，对于布局类组件来说，其布局算法都是通过对应的 `RenderObject` 对象来实现的
5. 所以如果对接下来介绍的某个布局类组件的原理感兴趣，可以查看其对应的 `RenderObject` 的实现，比如 `Stack` （层叠布局）对应的 `RenderObject` 对象就是 `RenderStack`，而层叠布局的实现就在 `RenderStack` 中

## 2、布局原理与约束（constraints）

- 尺寸限制类容器用于限制容器大小，`Flutter` 中提供了多种这样的容器，如 `ConstrainedBox`、`SizedBox`、`UnconstrainedBox`、`AspectRatio` 等，本节将介绍一些常用的

### ①、Flutter 布局模型

1. Flutter 中有两种布局模型：
	1. 基于 `RenderBox` 的盒模型布局。
	2. 基于 `Sliver` ( RenderSliver ) 按需加载列表布局。
2. 两种布局方式在细节上略有差异，但大体流程相同，布局流程如下：
	1. 上层组件向下层组件传递约束（constraints）条件。
	2. 下层组件确定自己的大小，然后告诉上层组件。注意下层组件的大小必须符合父组件的约束。
	3. 上层组件确定下层组件相对于自身的偏移和确定自身的大小（大多数情况下会根据子组件的大小来确定自身的大小）。
3. 比如，父组件传递给子组件的约束是“最大宽高不能超过 100，最小宽高为 0”，如果我们给子组件设置宽高都为200，则子组件最终的大小是 `100*100`，因为任何时候子组件都必须先遵守父组件的约束，在此基础上再应用子组件约束（相当于父组件的约束和自身的大小求一个交集）。
4. 本节我们主要看一下盒模型布局，然后会在可滚动组件一章中介绍 `Sliver` 布局模型。盒模型布局组件有两个特点：
5. 组件对应的渲染对象都继承自 `RenderBox` 类。在后面如果提到某个组件是 `RenderBox`，则指它是基于盒模型布局的，而不是说组件是 `RenderBox` 类的实例。
6. 在布局过程中父级传递给子级的约束信息由 BoxConstraints 描述

### ②、BoxConstraints 约束信息

1. `BoxConstraints` 是盒模型布局过程中父渲染对象传递给子渲染对象的约束信息，包含最大宽高信息，子组件大小需要在约束的范围内，`BoxConstraints` 默认的构造函数如下：

```dart
const BoxConstraints({
  this.minWidth = 0.0, //最小宽度
  this.maxWidth = double.infinity, //最大宽度
  this.minHeight = 0.0, //最小高度
  this.maxHeight = double.infinity //最大高度
})
```

2. 它包含 4 个属性，`BoxConstraints` 还定义了一些便捷的构造函数，`用于快速生成特定限制规则的BoxConstraints`，
	1. 如 `BoxConstraints.tight(Size size)`，它可以生成固定宽高的限制；
	2. `BoxConstraints.expand()` 可以生成一个尽可能大的用以填充另一个容器的 `BoxConstraints`。
	3. 除此之外还有一些其他的便捷函数，可以查看类定义。
	4. 另外我们会在后面深入介绍布局原理时还会讨论 `Constraints`，在这里，读者只需知道父级组件是通过 `BoxConstraints` 来描述对子组件可用的空间范围即可。
3. 约定：为了描述方便，如果我们说一个组件不约束其子组件或者取消对子组件约束时是指对子组件约束的最大宽高为无限大，而最小宽高为0，相当于子组件完全可以自己根据需要的空间来确定自己的大小。

### ③、`ConstrainedBox` 额外约束

1. `ConstrainedBox` 用于对子组件添加额外的约束。例如，如果你想让子组件的最小高度是 80 像素，你可以使用`const BoxConstraints(minHeight: 80.0)` 作为子组件的约束
2. 我们先定义一个 `redBox`，它是一个背景颜色为红色的盒子，不指定它的宽度和高度
3. 我们实现一个最小高度为 50，宽度尽可能大的红色容器

```dart
import 'package:flutter/material.dart';

import '02_布局类组件/01_布局原理与约束（constraints）/01_ConstrainedBox 额外约束.dart';

// 入口方法
void main() => runApp(const ConstrainedBoxComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

class ConstrainedBoxComponent extends StatelessWidget {
  const ConstrainedBoxComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    // 定义一个 DecoratedBox 的对象 redBox
    Widget redBox = const DecoratedBox(
      decoration: BoxDecoration(color: Colors.red),
    );

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body:用于定义页面的主要内容区域
         * ConstrainedBox：用于对子组件添加额外的约束
         */
        body: ConstrainedBox(
          constraints: const BoxConstraints(
            // 宽度尽可能大
            minWidth: double.infinity,
            // 最小高度为 50 像素
            minHeight: 50
          ),
          /**
           * Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等。
           * 它可以根据需要自动调整大小，并且可以根据子部件的大小自动调整自身大小。
           * 可以使用 Container 来包装其他小部件，并对其进行布局和装饰
           */
          child: Container(
            child: redBox,
          ),
        )
      )
    );
  }
}
```

![|438](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023144103.png)

### ④、SizedBox 给子元素指定固定的宽高

1. `SizedBox` 用于给子元素指定固定的宽高，如：

```dart
SizedBox(
  width: 80.0,
  height: 80.0,
  child: redBox
)
```

2. 实际上 `SizedBox` 只是 `ConstrainedBox` 的一个定制，上面代码等价于：

```dart
ConstrainedBox(
  constraints: BoxConstraints.tightFor(width: 80.0,height: 80.0),
  child: redBox, 
)
```

3. 而 `BoxConstraints.tightFor(width: 80.0,height: 80.0)` 等价于：

```dart
BoxConstraints(minHeight: 80.0,maxHeight: 80.0,minWidth: 80.0,maxWidth: 80.0)
```

4. 而实际上 `ConstrainedBox` 和 `SizedBox` 都是通过 `RenderConstrainedBox` 来渲染的，我们可以看到 `ConstrainedBox` 和 `SizedBox` 的 `createRenderObject()` 方法都返回的是一个 `RenderConstrainedBox` 对象：

```dart
@override
RenderConstrainedBox createRenderObject(BuildContext context) {
  return RenderConstrainedBox(
    additionalConstraints: ...,
  );
}
```

### ⑤、多重限制

1. 如果某一个组件有多个父级 `ConstrainedBox` 限制，那么最终会是哪个生效？我们看一个例子：

```dart
ConstrainedBox(
  constraints: BoxConstraints(minWidth: 60.0, minHeight: 60.0), //父
  child: ConstrainedBox(
    constraints: BoxConstraints(minWidth: 90.0, minHeight: 20.0),//子
    child: redBox,
  ),
)
```

2. 上面我们有父子两个 `ConstrainedBox`，他们的约束条件不同，运行后效果如图所示：

![|220](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023145029.png)

3. 最终显示效果是宽 90，高 60，也就是说是子 `ConstrainedBox` 的 `minWidth` 生效，而 `minHeight` 是父 `ConstrainedBox` 生效。单凭这个例子，我们还总结不出什么规律，我们将上例中父子约束条件换一下：

```dart
ConstrainedBox(
  constraints: BoxConstraints(minWidth: 90.0, minHeight: 20.0),
  child: ConstrainedBox(
    constraints: BoxConstraints(minWidth: 60.0, minHeight: 60.0),
    child: redBox,
  )
)
```

4. 运行效果如图所示：

![|220](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023145029.png)

5. 最终的显示效果仍然是 90，高 60，效果相同，但意义不同，因为此时 `minWidth` 生效的是父 `ConstrainedBox` ，而 `minHeight` 是子 `ConstrainedBox` 生效。
6. 通过上面示例，我们发现有多重限制时，对于 `minWidth` 和 `minHeight` 来说，是取父子中相应数值较大的。
7. 实际上，只有这样才能保证父限制与子限制不冲突

### ⑥、UnconstrainedBox 无约束

1. 虽然任何时候子组件都必须遵守其父组件的约束，但前提条件是它们必须是父子关系，假如有一个组件 A，它的子组件是 B，B 的子组件是 C，则 C 必须遵守 B 的约束，同时 B 必须遵守 A 的约束，但是 A 的约束不会直接约束到 C，除非B将A对它自己的约束透传给了C。 利用这个原理，就可以实现一个这样的 B 组件：
	1. B 组件中在布局 C 时不约束C（可以为无限大）。
	2. C 根据自身真实的空间占用来确定自身的大小。
	3. B 在遵守 A 的约束前提下结合子组件的大小确定自身大小。
2. 而这个 B 组件就是 `UnconstrainedBox` 组件，也就是说 `UnconstrainedBox` 的子组件将不再受到约束，大小完全取决于自己。一般情况下，我们会很少直接使用此组件，但在"去除"多重限制的时候也许会有帮助，我们看下下面的代码：

```dart
ConstrainedBox(
  constraints: BoxConstraints(minWidth: 60.0, minHeight: 100.0),  // 父
  child: UnconstrainedBox( // “去除”父级限制
    child: ConstrainedBox(
      constraints: BoxConstraints(minWidth: 90.0, minHeight: 20.0),// 子
      child: redBox,
    ),
  )
)
```

3. 上面代码中，如果没有中间的 `UnconstrainedBox`，那么根据上面所述的多重限制规则，那么最终将显示一个 90×100 的红色框。但是由于 `UnconstrainedBox` 去除了父 `ConstrainedBox` 的限制，则最终会按照子 `ConstrainedBox` 的限制来绘制 `redBox`，即 90×20，如图所示：

![|150](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023145917.png)

4. 但是，请注意 `UnconstrainedBox` 对父组件限制的“去除”并非是真正的去除：上面例子中虽然红色区域大小是 90×20，但上方仍然有 80 的空白空间。也就是说父限制的 `minHeight(100.0)` 仍然是生效的，只不过它不影响最终子元素 `redBox` 的大小，但仍然还是占有相应的空间，可以认为此时的父 `ConstrainedBox` 是作用于子 `UnconstrainedBox` 上，而 `redBox` 只受子 `ConstrainedBox` 限制，这一点请务必注意。
5. 那么有什么方法可以彻底去除父 `ConstrainedBox` 的限制吗？答案是否定的！请牢记，任何时候子组件都必须遵守其父组件的约束，所以在此提示，在定义一个通用的组件时，如果要对子组件指定约束，那么一定要注意，因为一旦指定约束条件，子组件自身就不能违反约束。
6. 在实际开发中，当我们发现已经使用 `SizedBox` 或 `ConstrainedBox` 给子元素指定了固定宽高，但是仍然没有效果时，几乎可以断定：已经有父组件指定了约束！
7. 举个例子，如 `Material` 组件库中的 `AppBar`（导航栏）的右侧菜单中，我们使用 `SizedBox` 指定了 `loading` 按钮的大小，代码如下：

```dart
 AppBar(
   title: Text(title),
   actions: <Widget>[
     SizedBox(
       width: 20, 
       height: 20,
       child: CircularProgressIndicator(
         strokeWidth: 3,
         valueColor: AlwaysStoppedAnimation(Colors.white70),
       ),
     )
   ],
)
```

8. 上面代码运行后，效果如图所示：

![|522](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023150056.png)

9. 我们会发现右侧 `loading` 按钮大小并没有发生变化！这正是因为 `AppBar` 中已经指定了 `actions` 按钮的约束条件，所以我们要自定义 `loading` 按钮大小，就必须通过 `UnconstrainedBox` 来 “去除” 父元素的限制，代码如下：

```dart
AppBar(
  title: Text(title),
  actions: <Widget>[
    UnconstrainedBox(
      child: SizedBox(
        width: 20,
        height: 20,
        child: CircularProgressIndicator(
          strokeWidth: 3,
          valueColor: AlwaysStoppedAnimation(Colors.white70),
        ),
      ),
    )
  ],
)
```

10. 运行后效果如图所示：

![|518](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023150341.png)

11. 生效了！实际上将 `UnconstrainedBox` 换成 `Center` 或者 `Align` 也是可以的，至于为什么，我们会在后面布局原理相关的章节中解释。
12. 另外，需要注意，`UnconstrainedBox` 虽然在其子组件布局时可以取消约束（子组件可以为无限大），但是 `UnconstrainedBox` 自身是受其父组件约束的，所以当 `UnconstrainedBox` 随着其子组件变大后，`如果UnconstrainedBox` 的大小超过它父组件约束时，也会导致溢出报错，比如：

```dart
Column(
  children: <Widget>[
    UnconstrainedBox(
      alignment: Alignment.topLeft,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(children: [Text('xx' * 30)]),
      ),
    ),
 ]
```

13. 文本已经超过屏幕宽度，溢出了

![|696](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023150430.png)

## 3、线性布局（Row和Column）

1. 所谓线性布局，即指沿水平或垂直方向排列子组件。
2. `Flutter` 中通过 `Row` 和 `Column` 来实现线性布局，类似于 Android 中的 `LinearLayout` 控件。
3. `Row` 和 `Column` 都继承自 `Flex`，我们将在弹性布局一节中详细介绍 `Flex`。

### ①、主轴和纵轴

1. 对于线性布局，有主轴和纵轴之分，如果布局是沿水平方向，那么主轴就是指水平方向，而纵轴即垂直方向；如果布局沿垂直方向，那么主轴就是指垂直方向，而纵轴就是水平方向。
2. 在线性布局中，有两个定义对齐方式的枚举类 `MainAxisAlignment` 和 `CrossAxisAlignment`，分别代表主轴对齐和纵轴对齐。

### ②、Row 水平线性布局

1. `Row` 可以沿水平方向排列其子 `widget`。定义如下

```dart
Row({
  ...
  /**
   * textDirection：表示水平方向子组件的布局顺序(是从左往右还是从右往左)
   * 默认为系统当前 Locale 环境的文本方向(如中文、英语都是从左往右，而阿拉伯语是从右往左)。
   */
  TextDirection textDirection,
  /**
   * mainAxisSize：表示 Row 在主轴(水平)方向占用的空间
   * 默认是 MainAxisSize.max，表示尽可能多的占用水平方向的空间，此时无论子 widgets 实际占用多少水平空间，Row 的宽度始终等于水平方向的最大宽度；
   * 而 MainAxisSize.min 表示尽可能少的占用水平空间，当子组件没有占满水平剩余空间，则 Row 的实际宽度等于所有子组件占用的水平空间；
   */
  MainAxisSize mainAxisSize = MainAxisSize.max,
  /**
   * mainAxisAlignment：表示子组件在 Row 所占用的水平空间内对齐方式，
   * 如果 mainAxisSize 值为 ainAxisSize.min，则此属性无意义，因为子组件的宽度等于Row的宽度。
   * 只有当 mainAxisSize 的值为 MainAxisSize.max 时，此属性才有意义，
   * MainAxisAlignment.start 表示沿 textDirection 的初始方向对齐，
   *    如 textDirection 取值为 TextDirection.ltr 时，则 MainAxisAlignment.start 表示左对齐，
   *    textDirection 取值为 TextDirection.rtl 时表示从右对齐。
   * 而 MainAxisAlignment.end 和 MainAxisAlignment.start 正好相反；
   * MainAxisAlignment.center 表示居中对齐。读者可以这么理解：textDirection 是 mainAxisAlignment 的参考系。
   */
  MainAxisAlignment mainAxisAlignment = MainAxisAlignment.start,
  /**
   * verticalDirection：表示 Row 纵轴（垂直）的对齐方向，默认是 VerticalDirection.down，表示从上到下。
   */
  VerticalDirection verticalDirection = VerticalDirection.down,
  /**
   * crossAxisAlignment：表示子组件在纵轴方向的对齐方式，Row 的高度等于子组件中最高的子元素高度，
   * 它的取值和 MainAxisAlignment 一样(包含 start、end、 center 三个值)，
   * 不同的是 crossAxisAlignment 的参考系是 verticalDirection，
   * 即 verticalDirection 值为 VerticalDirection.dow n时 crossAxisAlignment.start 指顶部对齐，
   * verticalDirection 值为 VerticalDirection.up 时，crossAxisAlignment.start 指底部对齐；
   * 而 crossAxisAlignment.end 和 crossAxisAlignment.start 正好相反；
   */
  CrossAxisAlignment crossAxisAlignment = CrossAxisAlignment.center,
  // children ：子组件数组。
  List<Widget> children = const <Widget>[],
})
```

2. 请阅读下面代码，先想象一下运行的结果：

```dart
Column(
  //测试Row对齐方式，排除Column默认居中对齐的干扰
  crossAxisAlignment: CrossAxisAlignment.start,
  children: <Widget>[
    Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(" hello world "),
        Text(" I am Jack "),
      ],
    ),
    Row(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(" hello world "),
        Text(" I am Jack "),
      ],
    ),
    Row(
      mainAxisAlignment: MainAxisAlignment.end,
      textDirection: TextDirection.rtl,
      children: <Widget>[
        Text(" hello world "),
        Text(" I am Jack "),
      ],
    ),
    Row(
      crossAxisAlignment: CrossAxisAlignment.start,  
      verticalDirection: VerticalDirection.up,
      children: <Widget>[
        Text(" hello world ", style: TextStyle(fontSize: 30.0),),
        Text(" I am Jack "),
      ],
    ),
  ],
);
```

3. 实际运行结果

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023153047.png)

4. 解释：
	1. 第一个 `Row` 很简单，默认为居中对齐；
	2. 第二个 `Row`，由于 `mainAxisSize` 值为 `MainAxisSize.min`，`Row` 的宽度等于两个 `Text` 的宽度和，所以对齐是无意义的，所以会从左往右显示；
	3. 第三个 `Row` 设置 `textDirection` 值为 `TextDirection.rtl`，所以子组件会从右向左的顺序排列，而此时 `MainAxisAlignment.end` 表示左对齐，所以最终显示结果就是图中第三行的样子；
	4. 第四个 `Row` 测试的是纵轴的对齐方式，由于两个子 `Text` 字体不一样，所以其高度也不同，`我们指定了verticalDirection` 值为 `VerticalDirection.up`，即从低向顶排列，而此时 `crossAxisAlignment` 值为 `CrossAxisAlignment.start` 表示底对齐

### ③、Column 垂直线性布局

1. `Column` 可以在垂直方向排列其子组件。
2. 参数和 `Row` 一样，不同的是布局方向为垂直，主轴纵轴正好相反，可类比 `Row` 来理解
3. 实际上，`Row` 和 `Column` 都只会在主轴方向占用尽可能大的空间，而纵轴的长度则取决于他们最大子元素的长度

## 4、弹性布局（Flex）

1. 弹性布局允许子组件按照一定比例来分配父容器空间。
2. 弹性布局的概念在其他 UI 系统中也都存在，如 H5 中的弹性盒子布局，Android 中 的 `FlexboxLayout` 等。
3. Flutter 中的弹性布局主要通过 `Flex` 和 `Expanded` 来配合实现

### ①、Flex

1. `Flex` 组件可以沿着水平或垂直方向排列子组件，如果你知道主轴方向，使用 `Row` 或 `Column` 会方便一些，因为 `Row` 和 `Column` 都继承自 `Flex`，参数基本相同，所以能使用 `Flex` 的地方基本上都可以使用 `Row` 或 `Column`。
2. `Flex` 本身功能是很强大的，它也可以和 `Expanded` 组件配合实现弹性布局。
3. 接下来我们只讨论 `Flex` 和弹性布局相关的属性(其他属性已经在介绍 `Row` 和 `Column` 时介绍过了)。

```dart
Flex({
  ...
  required this.direction, // 弹性布局的方向, Row 默认为水平方向，Column 默认为垂直方向
  List<Widget> children = const <Widget>[],
})
```

4. `Flex` 继承自 `MultiChildRenderObjectWidget`，对应的 `RenderObject` 为 `RenderFlex`，`RenderFlex` 中实现了其布局算法

### ②、Expanded

1. `Expanded` 只能作为 `Flex` 的孩子（否则会报错），它可以按比例“扩伸” `Flex` 子组件所占用的空间。因为 `Row` 和 `Column` 都继承自 `Flex`，所以 `Expanded` 也可以作为它们的孩子。

```dart
const Expanded({
  int flex = 1, 
  required Widget child,
})
```

2. `flex` 参数为弹性系数，如果为 0 或 null，则 child 是没有弹性的，即不会被扩伸占用的空间。如果大于 0，所有的 `Expanded` 按照其 flex 的比例来分割主轴的全部空闲空间。下面我们看一个例子

```dart
class FlexLayoutTestRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        //Flex的两个子widget按1：2来占据水平空间  
        Flex(
          direction: Axis.horizontal,
          children: <Widget>[
            Expanded(
              flex: 1,
              child: Container(
                height: 30.0,
                color: Colors.red,
              ),
            ),
            Expanded(
              flex: 2,
              child: Container(
                height: 30.0,
                color: Colors.green,
              ),
            ),
          ],
        ),
        Padding(
          padding: const EdgeInsets.only(top: 20.0),
          child: SizedBox(
            height: 100.0,
            //Flex的三个子widget，在垂直方向按2：1：1来占用100像素的空间  
            child: Flex(
              direction: Axis.vertical,
              children: <Widget>[
                Expanded(
                  flex: 2,
                  child: Container(
                    height: 30.0,
                    color: Colors.red,
                  ),
                ),
                Spacer(
                  flex: 1,
                ),
                Expanded(
                  flex: 1,
                  child: Container(
                    height: 30.0,
                    color: Colors.green,
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
```

3. 运行效果如图：

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023153900.png)

## 5、流式布局（Wrap、Flow）

1. 在介绍 `Row` 和 `Column` 时，如果子 `widget` 超出屏幕范围，则会报溢出错误，如

```dart
Row(
  children: <Widget>[
    Text("xxx"*100)
  ],
);
```

2. 运行效果如图所示

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023154138.png)

3. 可以看到，右边溢出部分报错。这是因为 `Row` 默认只有一行，如果超出屏幕不会折行。
4. 我们把超出屏幕显示范围会自动折行的布局称为流式布局。
5. Flutter 中通过 `Wrap` 和 `Flow` 来支持流式布局，将上例中的 `Row` 换成 `Wrap` 后溢出部分则会自动折行，下面我们分别介绍 `Wrap` 和 `Flow`

### ①、Wrap

1. 下面是Wrap的定义:

```dart
Wrap({
  ...
  this.direction = Axis.horizontal,
  this.alignment = WrapAlignment.start,
  // 主轴方向子 widget 的间距
  this.spacing = 0.0,
  // 纵轴方向的对齐方式
  this.runAlignment = WrapAlignment.start,
  // 纵轴方向的间距
  this.runSpacing = 0.0,
  this.crossAxisAlignment = WrapCrossAlignment.start,
  this.textDirection,
  this.verticalDirection = VerticalDirection.down,
  List<Widget> children = const <Widget>[],
})
```

2. 可以看到 `Wrap` 的很多属性在 `Row`（包括 `Flex` 和 `Column`）中也有，如 `direction`、`crossAxisAlignment`、`textDirection`、`verticalDirection` 等，这些参数意义是相同的，不再重复介绍
3. 可以认为 `Wrap` 和 `Flex`（包括 `Row` 和 `Column`）除了超出显示范围后 `Wrap` 会折行外，其他行为基本相同。
4. 下面看一个示例：

```dart
Wrap(
   spacing: 8.0, // 主轴(水平)方向间距
   runSpacing: 4.0, // 纵轴（垂直）方向间距
   alignment: WrapAlignment.center, //沿主轴方向居中
   children: <Widget>[
     Chip(
       avatar: CircleAvatar(backgroundColor: Colors.blue, child: Text('A')),
       label: Text('Hamilton'),
     ),
     Chip(
       avatar: CircleAvatar(backgroundColor: Colors.blue, child: Text('M')),
       label: Text('Lafayette'),
     ),
     Chip(
       avatar: CircleAvatar(backgroundColor: Colors.blue, child: Text('H')),
       label: Text('Mulligan'),
     ),
     Chip(
       avatar: CircleAvatar(backgroundColor: Colors.blue, child: Text('J')),
       label: Text('Laurens'),
     ),
   ],
)
```

5. 运行效果如图所示：

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023154846.png)

### ②、Flow

1. 我们一般很少会使用 `Flow`，因为其过于复杂，需要自己实现子 `widget` 的位置转换，在很多场景下首先要考虑的是 `Wrap` 是否满足需求。`Flow` 主要用于一些需要自定义布局策略或性能要求较高(如动画中)的场景。
2. `Flow` 有如下优点：
	1. 性能好：`Flow` 是一个对子组件尺寸以及位置调整非常高效的控件，`Flow` 用转换矩阵在对子组件进行位置调整的时候进行了优化：在 `Flow` 定位过后，如果子组件的尺寸或者位置发生了变化，在 `FlowDelegate` 中的`paintChildren()` 方法中调用 `context.paintChild` 进行重绘，而 `context.paintChild` 在重绘时使用了转换矩阵，并没有实际调整组件位置。
	2. 灵活：由于我们需要自己实现 `FlowDelegate` 的 `paintChildren()` 方法，所以我们需要自己计算每一个组件的位置，因此，可以自定义布局策略。
3. 缺点：
	1. 使用复杂。
	2. `Flow` 不能自适应子组件大小，必须通过指定父容器大小或实现 `TestFlowDelegate` 的 `getSize` 返回固定大小。
4. 我们对六个色块进行自定义流式布局：

```dart
Flow(
  delegate: TestFlowDelegate(margin: EdgeInsets.all(10.0)),
  children: <Widget>[
    Container(width: 80.0, height:80.0, color: Colors.red,),
    Container(width: 80.0, height:80.0, color: Colors.green,),
    Container(width: 80.0, height:80.0, color: Colors.blue,),
    Container(width: 80.0, height:80.0,  color: Colors.yellow,),
    Container(width: 80.0, height:80.0, color: Colors.brown,),
    Container(width: 80.0, height:80.0,  color: Colors.purple,),
  ],
)
```

5. 实现 `TestFlowDelegate`

```dart
class TestFlowDelegate extends FlowDelegate {
  EdgeInsets margin;

  TestFlowDelegate({this.margin = EdgeInsets.zero});

  double width = 0;
  double height = 0;

  @override
  void paintChildren(FlowPaintingContext context) {
    var x = margin.left;
    var y = margin.top;
    //计算每一个子widget的位置
    for (int i = 0; i < context.childCount; i++) {
      var w = context.getChildSize(i)!.width + x + margin.right;
      if (w < context.size.width) {
        context.paintChild(i, transform: Matrix4.translationValues(x, y, 0.0));
        x = w + margin.left;
      } else {
        x = margin.left;
        y += context.getChildSize(i)!.height + margin.top + margin.bottom;
        //绘制子widget(有优化)
        context.paintChild(i, transform: Matrix4.translationValues(x, y, 0.0));
        x += context.getChildSize(i)!.width + margin.left + margin.right;
      }
    }
  }

  @override
  Size getSize(BoxConstraints constraints) {
    // 指定Flow的大小，简单起见我们让宽度尽可能大，但高度指定为200，
    // 实际开发中我们需要根据子元素所占用的具体宽高来设置Flow大小
    return Size(double.infinity, 200.0);
  }

  @override
  bool shouldRepaint(FlowDelegate oldDelegate) {
    return oldDelegate != this;
  }
}
```

6. 运行效果

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023155408.png)

7. 可以看到我们主要的任务就是实现 `paintChildren`，它的主要任务是确定每个子 `widget` 位置。
8. 由于 `Flow` 不能自适应子 `widget` 的大小，我们通过在 `getSize` 返回一个固定大小来指定 `Flow` 的大小。
9. 注意，如果我们需要自定义布局策略，一般首选的方式是通过直接继承 `RenderObject`，然后通过重写 `performLayout` 的方式实现

## 6、层叠布局（Stack、Positioned）

1. 层叠布局和 Web 中的绝对定位、Android 中的 `Frame` 布局是相似的，子组件可以根据距父容器四个角的位置来确定自身的位置。
2. 层叠布局允许子组件按照代码中声明的顺序堆叠起来。
3. Flutter 中使用 `Stack` 和 `Positioned` 这两个组件来配合实现绝对定位。
4. `Stack` 允许子部件堆叠，可使用 `Positioned` 根据 `Stack` 的四个角来定位子部件。

### ①、Stack

1. `Stack` 是一个用于堆叠子组件的容器。它将子组件按照添加的顺序依次叠放在一起。默认情况下，子组件会居中对齐。可以使用 `alignment` 属性来调整子组件的对齐方式
2. `Stack` 组件定义如下：

```dart
Stack({
  /**
   * alignment：此参数决定如何去对齐没有定位（没有使用 Positioned）或部分定位的子组件。
   * 所谓部分定位，在这里特指没有在某一个轴上定位：left、right 为横轴，top、bottom 为纵轴，
   * 只要包含某个轴上的一个定位属性就算在该轴上有定位。
   */
  this.alignment = AlignmentDirectional.topStart,
  /**
   * textDirection：和 Row、Wrap 的 textDirection 功能一样，都用于确定 alignment 对齐的参考系，
   * 即：textDirection 的值为 TextDirection.ltr，则 alignment 的 start 代表左，end 代表右，即从左往右的顺序；
   * textDirection 的值为 TextDirection.rtl，则 alignment 的 start 代表右，end 代表左，即从右往左的顺序。
   */
  this.textDirection,
  /**
   * fit：此参数用于确定没有定位的子组件如何去适应 Stack 的大小。
   * StackFit.loose 表示使用子组件的大小，StackFit.expand 表示扩伸到 Stack 的大小。
   */
  this.fit = StackFit.loose,
  /**
   * clipBehavior：此属性决定对超出 Stack 显示空间的部分如何剪裁，
   * Clip 枚举类中定义了剪裁的方式，
   * Clip.hardEdge 表示直接剪裁，不应用抗锯齿
   */
  this.clipBehavior = Clip.hardEdge,
  List<Widget> children = const <Widget>[],
})
```

### ②、Positioned

1. `Positioned` 组件用于指定子组件在 `Stack` 中的位置和尺寸。通过 `top`、`right`、`bottom`、`left` 属性可以设置子组件的边距。`Positioned` 组件需要作为 `Stack` 的子组件使用
2. `Positioned` 组件定义如下：

```dart
const Positioned({
  Key? key,
  // 离 Stack 左 四边的距离
  this.left,
  // 离 Stack 上 边的距离
  this.top,
  // 离 Stack 右 边的距离
  this.right,
  // 离 Stack 底 四边的距离
  this.bottom,
  // 需要定位元素的宽度
  this.width,
  // 需要定位元素的高度
  this.height,
  required Widget child,
})
```

2. 注意，`Positioned` 的 `width`、`height` 和其他地方的意义稍微有点区别，此处用于配合 `left`、`top` 、`right`、 `bottom` 来定位组件
3. 举个例子，在水平方向时，只能指定 `left`、`right`、`width` 三个属性中的两个，如指定 `left` 和 `width` 后，`right` 会自动算出(`left+width`)，如果同时指定三个属性则会报错，垂直方向同理

### ③、示例

1. 示例代码：

```dart
import 'package:flutter/material.dart';

import '02_布局类组件/05_层叠布局（Stack、Positioned）/01_层叠布局（Stack、Positioned）.dart';

// 入口方法
void main() => runApp(const StackPositionedComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

class StackPositionedComponent extends StatelessWidget {
  const StackPositionedComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body:用于定义页面的主要内容区域
         * ConstrainedBox：用于对子组件添加额外的约束
         */
        body: ConstrainedBox(
          constraints: const BoxConstraints(
            // 宽度尽可能大
            minWidth: double.infinity,
            // 高度尽可能大
            minHeight: double.infinity,
          ),
          child: Stack(
            // 指定未定位或部分定位 widget 的对齐方式
            alignment:Alignment.center,
            children: [
              Container(
                color: Colors.red,
                child: const Text("Hello world",style: TextStyle(color: Colors.white)),
              ),
              const Positioned(
                left: 18.0,
                child: Text("左侧"),
              ),
              const Positioned(
                top: 18.0,
                child: Text("上方"),
              ),
              const Positioned(
                bottom: 18.0,
                right: 18.0,
                child: Text("右下"),
              )
            ],
          ),
        )
      )
    );
  }
}
```

2. 结果：

![|387](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231023165229.png)

## 7、对齐与相对定位（Align）

1. 在上一节中我们讲过通过 `Stack` 和 `Positioned`，我们可以指定一个或多个子元素相对于父元素各个边的精确偏移，并且可以重叠。
2. 但如果我们只想简单的调整一个子元素在父元素中的位置的话，使用 `Align` 组件会更简单一些

### ①、Align 对齐

1. Align 组件可以调整子组件的位置，定义如下：

```dart
Align({
  Key key,
  /**
   * alignment: 需要一个 AlignmentGeometry 类型的值，表示子组件在父组件中的起始位置。
   * AlignmentGeometry 是一个抽象类，它有两个常用的子类：Alignment和 FractionalOffset
   */
  this.alignment = Alignment.center,
  /**
   * widthFactor 和 heightFactor 是用于确定 Align 组件本身宽高的属性；
   * 它们是两个缩放因子，会分别乘以子元素的宽、高，最终的结果就是 Align 组件的宽高。
   * 如果值为 null，则组件的宽高将会占用尽可能多的空间。
   */
  this.widthFactor,
  this.heightFactor,
  Widget child,
})
```

2. 例子：


```dart
import 'package:flutter/material.dart';

import '02_布局类组件/06_对齐与相对定位（Align）/01_Align 对齐.dart';

// 入口方法
void main() => runApp(const AlignComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:async';

import 'package:flutter/material.dart';

class AlignComponent extends StatelessWidget {
  const AlignComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body:用于定义页面的主要内容区域
         * ConstrainedBox：用于对子组件添加额外的约束
         */
        body: ConstrainedBox(
          constraints: const BoxConstraints(
            // 宽度尽可能大
            minWidth: double.infinity,
            // 高度尽可能大
            minHeight: double.infinity,
          ),
          child: const Align(
            // 指定对齐方式，右上角
            alignment: Alignment.topRight,
            child: Text("月海", style: TextStyle(fontSize: 50),)
          ),
        )
      )
    );
  }
}
```

3. 效果：

![|375](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024110902.png)

4. 我们通过 `Alignment.topRight` 将控件定位在 `Container` 的右上角。那 `Alignment.topRight` 是什么呢？通过源码我们可以看到其定义如下

```dart
//右上角
static const Alignment topRight = Alignment(1.0, -1.0);
```

5. 可以看到它只是 `Alignment` 的一个实例，下面我们介绍一下 `Alignment`

### ②、Alignment

1. `Alignment` 继承自 `AlignmentGeometry`，表示矩形内的一个点，他有两个属性 `x、y`，分别表示在水平和垂直方向的偏移，`Alignment` 定义如下：

```dart
Alignment(this.x, this.y)
```

2. `Alignment Widget` 会以矩形的中心点作为坐标原点，即 `Alignment(0.0, 0.0)` 。`x、y` 的值从 `-1` 到 `1` 分别代表矩形左边到右边的距离和顶部到底边的距离
3. 因此 2 个水平（或垂直）单位则等于矩形的宽（或高），如 `Alignment(-1.0, -1.0)` 代表矩形的左侧顶点，而 `Alignment(1.0, 1.0)` 代表右侧底部终点，而 `Alignment(1.0, -1.0)` 则正是右侧顶点，即 `Alignment.topRight`。
4. 为了使用方便，矩形的原点、四个顶点，以及四条边的终点在 `Alignment` 类中都已经定义为了静态常量。
5. `Alignment` 可以通过其坐标转换公式将其坐标转为子元素的具体偏移坐标：

```dart
实际偏移 = (Alignment.x * (parentWidth - childWidth) / 2 + (parentWidth - childWidth) / 2,
        Alignment.y * (parentHeight - childHeight) / 2 + (parentHeight - childHeight) / 2)
```

6. 其中 `childWidth` 为子元素的宽度，`childHeight` 为子元素高度。
7. 现在我们再看看上面的示例，我们将 `Alignment(1.0, -1.0)` 带入上面公式，可得 FlutterLogo 的实际偏移坐标正是`（60，0）`。下面再看一个例子：

```dart
Align(
  widthFactor: 2,
  heightFactor: 2,
  alignment: Alignment(2,0.0),
  child: FlutterLogo(
    size: 60,
  ),
)
```

8. 我们可以先想象一下运行效果：将 `Alignment(2,0.0)` 带入上述坐标转换公式，可以得到 FlutterLogo 的实际偏移坐标为`（90，30）`。实际运行如图所示

![|218](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024111729.png)

### ③、FractionalOffset

1. `FractionalOffset` 继承自 `Alignment`，它和 `Alignment` 唯一的区别就是坐标原点不同！
2. `FractionalOffset` 的坐标原点为矩形的左侧顶点，这和布局系统的一致，所以理解起来会比较容易。
3. `FractionalOffset` 的坐标转换公式为：

```dart
实际偏移 = (FractionalOffse.x * (parentWidth - childWidth), FractionalOffse.y * (parentHeight - childHeight))
```

4. 下面看一个例子：

```dart
Container(
  height: 120.0,
  width: 120.0,
  color: Colors.blue[50],
  child: Align(
    alignment: FractionalOffset(0.2, 0.6),
    child: FlutterLogo(
      size: 60,
    ),
  ),
)
```

5. 实际运行效果如图所示：

![|178](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024112023.png)

6. 我们将 `FractionalOffset(0.2, 0.6)` 带入坐标转换公式得 FlutterLogo 实际偏移为`（12，36）`，和实际运行效果吻合。

### ④、Align 和 Stack 对比

1. 可以看到，`Align` 和 `Stack/Positioned` 都可以用于指定子元素相对于父元素的偏移，但它们还是有两个主要区别：
2. 定位参考系统不同；`Stack/Positioned` 定位的参考系可以是父容器矩形的四个顶点；而 `Align` 则需要先通过 `alignment` 参数来确定坐标原点，不同的 `alignment` 会对应不同原点，最终的偏移是需要通过 `alignment` 的转换公式来计算出。
3. `Stack` 可以有多个子元素，并且子元素可以堆叠，而 `Align` 只能有一个子元素，不存在堆叠

### ⑤、Center 组件

1. 们在前面的例子中已经使用过 `Center` 组件来居中子元素了，现在我们正式来介绍一下它。通过查找 SDK 源码，我们看到 `Center` 组件定义如下：

```dart
class Center extends Align {
  const Center({ Key? key, double widthFactor, double heightFactor, Widget? child })
    : super(key: key, widthFactor: widthFactor, heightFactor: heightFactor, child: child);
}
```

2. 可以看到 `Center` 继承自 `Align`，它比 `Align` 只少了一个 `alignment` 参数；由于 `Align` 的构造函数中 `alignment` 值为 `Alignment.center`，所以，我们可以认为 `Center` 组件其实是对齐方式确定 （`Alignment.center`）了的 `Align`。
3. 上面我们讲过当 `widthFactor` 或 `heightFactor` 为 `null` 时组件的宽高将会占用尽可能多的空间，这一点需要特别注意，我们通过一个示例说明：

```dart
...//省略无关代码
DecoratedBox(
  decoration: BoxDecoration(color: Colors.red),
  child: Center(
    child: Text("xxx"),
  ),
),
DecoratedBox(
  decoration: BoxDecoration(color: Colors.red),
  child: Center(
    widthFactor: 1,
    heightFactor: 1,
    child: Text("xxx"),
  ),
)
```

4. 运行效果如图所示：

![|516](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024123420.png)

## 8、LayoutBuilder

1. 通过 `LayoutBuilder`，我们可以在布局过程中拿到父组件传递的约束信息，然后我们可以根据约束信息动态的构建不同的布局。
2. 比如我们实现一个响应式的 `Column` 组件 `ResponsiveColumn`，它的功能是当当前可用的宽度小于 200 时，将子组件显示为一列，否则显示为两列。简单来实现一下
3. 示例：

```dart
import 'package:flutter/material.dart';

import '02_布局类组件/06_对齐与相对定位（Align）/02_LayoutBuilder.dart';

// 入口方法
void main() => runApp(const LayoutBuilderRoute());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class LayoutBuilderRoute extends StatelessWidget {
  const LayoutBuilderRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    var children = List.filled(6, const Text("A", style: TextStyle(fontSize: 50),));

    return Directionality(
      textDirection: TextDirection.ltr,
      // Column 在本示例中在水平方向的最大宽度为屏幕的宽度
      child: Column(
        children: [
          // 限制宽度为 190，小于 200
          SizedBox(width: 190, child: ResponsiveColumn(children: children)),
          ResponsiveColumn(children: children)
        ],
      )
    );
  }
}

class ResponsiveColumn extends StatelessWidget {
  const ResponsiveColumn({Key? key, required this.children}) : super(key: key);

  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    /**
     * 通过 LayoutBuilder，我们可以在布局过程中拿到父组件传递的约束信息
     * 然后我们可以根据约束信息动态的构建不同的布局
     */
    return LayoutBuilder(builder: (BuildContext context, BoxConstraints constraints){
      // 判断约束信息中的 最大宽度
      if (constraints.maxWidth < 200) {
        // 最大宽度小于 200，显示单列
        return Column(mainAxisSize: MainAxisSize.min, children: children);
      } else {
        // 大于 200，显示双列
        var children = <Widget>[];
        for (var i = 0; i < children.length; i += 2) {
          if (i + 1 < children.length) {
            children.add(Row(
              mainAxisSize: MainAxisSize.min,
              children: [children[i], children[i + 1]],
            ));
          } else {
            children.add(children[i]);
          }
        }
        return Column(mainAxisSize: MainAxisSize.min, children: children);
      }
    });
  }
}
```

4. 效果：

![|375](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024134927.png)

## 9、获取组件大小和坐标

### ①、获取组件大小和相对于屏幕的坐标

1. Flutter 是响应式 UI 框架，和命令式 UI 框架最大的不同就是：大多数情况下开发者只需要关注数据的变化，数据变化后框架会自动重新构建 UI 而不需要开发者手动去操作每一个组件，所以我们会发现 `Widget` 会被定义为不可变的（immutable），并且没有提供任何操作组件的 API，因此如果我们想在 Flutter 中获取某个组件的大小和位置就会很困难，当然大多数情况下不会有这个需求，但总有一些场景会需要，而在命令式 UI 框架中是不会存在这个问题的。
2. 我们知道，只有当布局完成时，每个组件的大小和位置才能确定，所以获取的时机肯定是布局完成后，那布局完成的时机如何获取呢？至少事件分发肯定是在布局完成之后的，比如

```dart
Builder(
  builder: (context) {
    return GestureDetector(
      child: Text('flutter@wendux'),
      onTap: () => print(context.size), //打印 text 的大小
    );
  },
),
```

3. `context.size` 可以获取当前上下文 `RenderObject` 的大小，对于 `Builder`、`StatelessWidget` 以及 `StatefulWidget` 这样没有对应 `RenderObject` 的组件（这些组件只是用于组合和代理组件，本身并没有布局和绘制逻辑），获取的是子代中第一个拥有 `RenderObject` 组件的 `RenderObject` 对象。

### ②、获取组件相对于某个父组件的坐标

1. `RenderAfterLayout` 类继承自 `RenderBox`，`RenderBox` 有一个 `localToGlobal` 方法，它可以将坐标转化为相对与指定的祖先节点的坐标，比如下面代码可以打印出 `Text('A')` 在 父 `Container` 中的坐标

```dart
Builder(builder: (context) {
  return Container(
    color: Colors.grey.shade200,
    alignment: Alignment.center,
    width: 100,
    height: 100,
    child: AfterLayout(
      callback: (RenderAfterLayout ral) {
        Offset offset = ral.localToGlobal(
          Offset.zero,
          // 传一个父级元素
          ancestor: context.findRenderObject(),
        );
        print('A 在 Container 中占用的空间范围为：${offset & ral.size}');
      },
      child: Text('A'),
    ),
  );
}),
```

# 五、容器类组件

1. 容器类 `Widget` 和布局类 `Widget` 都作用于其子 `Widget`，不同的是：
2. 布局类 `Widget` 一般都需要接收一个 `widget` 数组（`children`），他们直接或间接继承自（或包含） `MultiChildRenderObjectWidget` ；
3. 而容器类 `Widget` 一般只需要接收一个子 `Widget`（`child`），他们直接或间接继承自（或包含） `SingleChildRenderObjectWidget`。
4. 布局类 `Widget` 是按照一定的排列方式来对其子 `Widget` 进行排列；
5. 而容器类 `Widget` 一般只是包装其子 `Widget`，对其添加一些修饰（补白或背景色等）、变换(旋转或剪裁等)、或限制(大小等)。

## 1、填充（Padding）

### ①、Padding

1. `Padding` 可以给其子节点添加填充（留白），和边距效果类似。我们在前面很多示例中都已经使用过它了，现在来看看它的定义：

```dart
Padding({
  ...
  /**
   * EdgeInsetsGeometry 是一个抽象类，开发中，我们一般都使用 EdgeInsets 类
   * 它是EdgeInsetsGeometry的一个子类，定义了一些设置填充的便捷方法
   */
  EdgeInsetsGeometry padding,
  Widget child,
})
```

### ②、EdgeInsets

1. 我们看看 `EdgeInsets` 提供的便捷方法：
2. `fromLTRB(double left, double top, double right, double bottom)`：分别指定四个方向的填充。
3. `all(double value)` : 所有方向均使用相同数值的填充。
4. `only({left, top, right ,bottom })`：可以设置具体某个方向的填充(可以同时指定多个方向)。
5. `symmetric({ vertical, horizontal })`：用于设置对称方向的填充，`vertical` 指 `top` 和 `bottom`，`horizontal` 指 `left` 和 `right`

### ③、示例

1. 示例：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）/01_填充（Padding）.dart';

// 入口方法
void main() => runApp(const PaddingComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class PaddingComponent extends StatelessWidget {
  const PaddingComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body:用于定义页面的主要内容区域
         * Column：垂直线性布局
         */
        body: Column(
          mainAxisSize: MainAxisSize.max,
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            Container(
              constraints: const BoxConstraints.tightFor(width: 200, height: 200),
              color: Colors.red,
              child: const Padding(
                padding: EdgeInsets.only(left: 50),
                child: Text("月海", style: TextStyle(fontSize: 50),),
              ),
            ),

            const SizedBox(height: 10),

            Container(
              constraints: const BoxConstraints.tightFor(width: 200, height: 200),
              color: Colors.red,
              child: const Padding(
                  padding: EdgeInsets.symmetric(horizontal: 100),
                  child: Text("月海", style: TextStyle(fontSize: 50), textAlign: TextAlign.end,)),
            ),

            const SizedBox(height: 10),

            Container(
              constraints: const BoxConstraints.tightFor(width: 200, height: 200),
              color: Colors.red,
              child: const Padding(
                padding: EdgeInsets.all(50),
                child: Text("月海", style: TextStyle(fontSize: 50), textAlign: TextAlign.end,)),
            ),
          ],
        )
      )
    );
  }
}
```

2. 效果：

![|353](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024142938.png)

## 2、装饰容器（DecoratedBox）

### ①、DecoratedBox

1. `DecoratedBox` 可以在其子组件绘制前(或后)绘制一些装饰（`Decoration`），如背景、边框、渐变等。 `DecoratedBox` 定义如下：

```dart
const DecoratedBox({
  /**
   * decoration：代表将要绘制的装饰，它的类型为 Decoration。
   * Decoration 是一个抽象类，它定义了一个接口 createBoxPainter()，
   * 子类的主要职责是需要通过实现它来创建一个画笔，该画笔用于绘制装饰
   */
  Decoration decoration,
  /**
   * position：此属性决定在哪里绘制 Decoration，它接收 DecorationPosition 的枚举类型，该枚举类有两个值：
   * background：在子组件之后绘制，即背景装饰。
   * foreground：在子组件之上绘制，即前景
   */
  DecorationPosition position = DecorationPosition.background,
  Widget? child
})
```

### ②、BoxDecoration

1. 我们通常会直接使用 BoxDecoration 类，它是一个 Decoration 的子类，实现了常用的装饰元素的绘制

```dart
BoxDecoration({
  Color color, //颜色
  DecorationImage image,//图片
  BoxBorder border, //边框
  BorderRadiusGeometry borderRadius, //圆角
  List<BoxShadow> boxShadow, //阴影,可以指定多个
  Gradient gradient, //渐变
  BlendMode backgroundBlendMode, //背景混合模式
  BoxShape shape = BoxShape.rectangle, //形状
})
```

### ③、示例

1. 示例

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）.dart';
import '03_容器类组件/02_装饰容器（DecoratedBox）.dart';

// 入口方法
void main() => runApp(const DecoratedBoxComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class DecoratedBoxComponent extends StatelessWidget {
  const DecoratedBoxComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
       /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),

              DecoratedBox(
                decoration: BoxDecoration(
                  // 背景渐变
                  gradient: LinearGradient(colors:[Colors.red,Colors.orange.shade700]),
                  // 3像素圆角
                  borderRadius: BorderRadius.circular(3.0),
                  // 阴影
                  boxShadow: const [
                    BoxShadow(
                        color:Colors.black54,
                        offset: Offset(2.0,2.0),
                        blurRadius: 4.0
                    )
                  ]
                ),
                child: const Padding(
                  padding: EdgeInsets.symmetric(horizontal: 80.0, vertical: 18.0),
                  child: Text("Login", style: TextStyle(color: Colors.white),),
                )
              ),

              const SizedBox(height: 10),

            ],
          )
        )
    );
  }
}
```

2. 效果

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024143832.png)

## 3、变换（Transform）

### ①、简介

1. `Transform` 可以在其子组件绘制时对其应用一些矩阵变换来实现一些特效。
2. `Matrix4` 是一个 4D 矩阵，通过它我们可以实现各种矩阵操作，下面是一个例子：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）.dart';
import '03_容器类组件/02_装饰容器（DecoratedBox）.dart';
import '03_容器类组件/03_变换（Transform）.dart';

// 入口方法
void main() => runApp(const TransformComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class TransformComponent extends StatelessWidget {
  const TransformComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),

              Container(
                color: Colors.black,
                child: Transform(
                  alignment: Alignment.topRight, //相对于坐标系原点的对齐方式
                  transform: Matrix4.skewY(0.3), //沿Y轴倾斜0.3弧度
                  child: Container(
                    padding: const EdgeInsets.all(8.0),
                    color: Colors.deepOrange,
                    child: const Text('Apartment for rent!'),
                  ),
                ),
              )

            ],
          )
        )
    );
  }
}
```

3. 运行效果如图所示：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024144245.png)

4. 关于矩阵变换的相关内容属于线性代数范畴，此处不做讨论；由于矩阵变化时发生在绘制时，而无需重新布局和构建等过程，所以性能很好

### ②、平移

1. `Transform.translate` 接收一个 `offset` 参数，可以在绘制时沿 x、y 轴对子组件平移指定的距离

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）.dart';
import '03_容器类组件/02_装饰容器（DecoratedBox）.dart';
import '03_容器类组件/03_变换（Transform）.dart';

// 入口方法
void main() => runApp(const TransformComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class TransformComponent extends StatelessWidget {
  const TransformComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),

              Container(
                color: Colors.black,
                child: Transform(
                  alignment: Alignment.topRight, //相对于坐标系原点的对齐方式
                  transform: Matrix4.skewY(0.3), //沿Y轴倾斜0.3弧度
                  child: Container(
                    padding: const EdgeInsets.all(8.0),
                    color: Colors.deepOrange,
                    child: const Text('Apartment for rent!'),
                  ),
                ),
              ),

              const SizedBox(height: 50),

              DecoratedBox(
                decoration:const BoxDecoration(color: Colors.red),
                //默认原点为左上角，左移20像素，向上平移5像素
                child: Transform.translate(
                  offset: const Offset(-20.0, -5.0),
                  child: const Text("Hello world"),
                ),
              )

            ],
          )
        )
    );
  }
}
```

2. 效果：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024144728.png)

### ③、旋转

1. `Transform.rotate` 可以对子组件进行旋转变换，
2. 注意：要使用 `math.pi` 需先进行如下导包：

```dart
import 'dart:math' as math;
```

3. ，如：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）.dart';
import '03_容器类组件/02_装饰容器（DecoratedBox）.dart';
import '03_容器类组件/03_变换（Transform）.dart';

// 入口方法
void main() => runApp(const TransformComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';
import 'dart:math' as math;

class TransformComponent extends StatelessWidget {
  const TransformComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),
              Container(
                color: Colors.black,
                child: Transform(
                  alignment: Alignment.topRight, //相对于坐标系原点的对齐方式
                  transform: Matrix4.skewY(0.3), //沿Y轴倾斜0.3弧度
                  child: Container(
                    padding: const EdgeInsets.all(8.0),
                    color: Colors.deepOrange,
                    child: const Text('Apartment for rent!'),
                  ),
                ),
              ),

              const SizedBox(height: 50),
              // 平移
              DecoratedBox(
                decoration:const BoxDecoration(color: Colors.red),
                //默认原点为左上角，左移20像素，向上平移5像素
                child: Transform.translate(
                  offset: const Offset(-20.0, -5.0),
                  child: const Text("Hello world"),
                ),
              ),

              const SizedBox(height: 50),
              // 旋转
              DecoratedBox(
                decoration:BoxDecoration(color: Colors.red),
                child: Transform.rotate(
                  //旋转90度
                  angle:math.pi/2 ,
                  child: Text("Hello world"),
                ),
              ),

            ],
          )
        )
    );
  }
}
```

2. 效果：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024145256.png)

### ④、缩放

1. Transform.scale 可以对子组件进行缩小或放大，如：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/01_填充（Padding）.dart';
import '03_容器类组件/02_装饰容器（DecoratedBox）.dart';
import '03_容器类组件/03_变换（Transform）.dart';

// 入口方法
void main() => runApp(const TransformComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';
import 'dart:math' as math;

class TransformComponent extends StatelessWidget {
  const TransformComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),
              Container(
                color: Colors.black,
                child: Transform(
                  alignment: Alignment.topRight, //相对于坐标系原点的对齐方式
                  transform: Matrix4.skewY(0.3), //沿Y轴倾斜0.3弧度
                  child: Container(
                    padding: const EdgeInsets.all(8.0),
                    color: Colors.deepOrange,
                    child: const Text('Apartment for rent!'),
                  ),
                ),
              ),

              const SizedBox(height: 50),
              // 平移
              DecoratedBox(
                decoration:const BoxDecoration(color: Colors.red),
                //默认原点为左上角，左移20像素，向上平移5像素
                child: Transform.translate(
                  offset: const Offset(-20.0, -5.0),
                  child: const Text("Hello world"),
                ),
              ),

              const SizedBox(height: 50),
              // 旋转
              DecoratedBox(
                decoration:const BoxDecoration(color: Colors.red),
                child: Transform.rotate(
                  //旋转90度
                  angle:math.pi/2 ,
                  child: const Text("Hello world"),
                ),
              ),

              const SizedBox(height: 50),
              // 缩放
              DecoratedBox(
                  decoration:const BoxDecoration(color: Colors.red),
                  child: Transform.scale(
                      scale: 1.5, //放大到1.5倍
                      child: const Text("Hello world")
                  )
              )

            ],
          )
        )
    );
  }
}
```

2. 效果：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024145418.png)

### ⑤、Transform 注意事项

1. `Transform` 的变换是应用在绘制阶段，而并不是应用在布局(`layout`)阶段，所以无论对子组件应用何种变化，其占用空间的大小和在屏幕上的位置都是固定不变的，因为这些是在布局阶段就确定的。下面我们具体说明：


```dart
import 'package:flutter/material.dart';

import '03_容器类组件/04_变换（Transform）2.dart';

// 入口方法
void main() => runApp(const Transform2Component());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';
import 'dart:math' as math;

class Transform2Component extends StatelessWidget {
  const Transform2Component({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Column(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 50),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  DecoratedBox(
                      decoration:const BoxDecoration(color: Colors.red),
                      child: Transform.scale(scale: 1.5,
                          child: const Text("Hello world")
                      )
                  ),
                  const Text("你好", style: TextStyle(color: Colors.green, fontSize: 18.0),)
                ],
              )

            ],
          )
        )
    );
  }
}
```

2. 效果：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024145718.png)

3. 由于第一个 `Text` 应用变换(放大)后，其在绘制时会放大，但其占用的空间依然为红色部分，所以第二个 `Text` 会紧挨着红色部分，最终就会出现文字重合。
4. 由于矩阵变化只会作用在绘制阶段，所以在某些场景下，在 UI 需要变化时，可以直接通过矩阵变化来达到视觉上的 UI 改变，而不需要去重新触发 build 流程，这样会节省 layout 的开销，所以性能会比较好。
5. 如之前介绍的 Flow 组件，它内部就是用矩阵变换来更新 UI，除此之外，Flutter 的动画组件中也大量使用了 Transform 以提高性能

### ⑥、RotatedBox

1. `RotatedBox` 和 `Transform.rotate` 功能相似，它们都可以对子组件进行旋转变换，但是有一点不同：
2. `RotatedBox` 的变换是在 `layout` 阶段，会影响在子组件的位置和大小。
3. 我们将上面介绍 `Transform.rotate` 时的示例改一下：

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.center,
  children: <Widget>[
    DecoratedBox(
      decoration: BoxDecoration(color: Colors.red),
      //将Transform.rotate换成RotatedBox  
      child: RotatedBox(
        quarterTurns: 1, //旋转90度(1/4圈)
        child: Text("Hello world"),
      ),
    ),
    Text("你好", style: TextStyle(color: Colors.green, fontSize: 18.0),)
  ],
),
```

4. 效果如图所示：

![|314](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024145946.png)

5. 由于 `RotatedBox` 是作用于 `layout` 阶段，所以子组件会旋转 90 度（而不只是绘制的内容），`decoration` 会作用到子组件所占用的实际空间上，所以最终就是上图的效果，可以和前面 `Transform.rotat`e 示例对比理解

## 4、容器组件（Container）

### ①、Container

1. `Container` 是一个组合类容器，它本身不对应具体的 `RenderObject`，它是 `DecoratedBox`、`ConstrainedBox`、`Transform`、`Padding`、`Align` 等组件组合的一个多功能容器，所以我们只需通过一个 Container 组件可以实现同时需要装饰、变换、限制的场景。
2. 下面是 `Container` 的定义

```dart
Container({
  this.alignment,
  this.padding, //容器内补白，属于decoration的装饰范围
  Color color, // 背景色
  Decoration decoration, // 背景装饰
  Decoration foregroundDecoration, //前景装饰
  double width,//容器的宽度
  double height, //容器的高度
  BoxConstraints constraints, //容器大小的限制条件
  this.margin,//容器外补白，不属于decoration的装饰范围
  this.transform, //变换
  this.child,
  ...
})
```

3. 容器的大小可以通过 `width`、`height` 属性来指定，也可以通过 `constraints` 来指定；如果它们同时存在时，`width`、`height` 优先。
4. 实际上 `Container` 内部会根据 `width`、`height` 来生成一个 `constraints`。
5. `color` 和 `decoration` 是互斥的，如果同时设置它们则会报错！
6. 实际上，当指定 `color` 时，`Container` 内会自动创建一个 `decoration`

### ②、示例

1. 示例：


```dart
import 'package:flutter/material.dart';

import '03_容器类组件/05_容器组件（Container）.dart';

// 入口方法
void main() => runApp(const ContainerComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';
import 'dart:math' as math;

class ContainerComponent extends StatelessWidget {
  const ContainerComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Column：垂直线性布局
           */
          body: Container(
            width: 200,
            height: 150,
            margin: const EdgeInsets.only(top: 50.0, left: 120.0),
            // 卡片内文字居中
            alignment: Alignment.center,
            // 卡片倾斜变换
            transform: Matrix4.rotationZ(.2),
            // 背景装饰
            decoration: const BoxDecoration(
              // 背景径向渐变
              gradient: RadialGradient(
                colors: [Colors.red, Colors.orange],
                center: Alignment.topLeft,
                radius: .98,
              ),
              boxShadow: [
                // 卡片阴影
                BoxShadow(
                  color: Colors.black54,
                  offset: Offset(2.0, 2.0),
                  blurRadius: 4.0,
                )
              ],
            ),
            child: const Text(
              //卡片文字
              "5.20", style: TextStyle(color: Colors.white, fontSize: 40.0),
            ),
          )
        )
    );
  }
}
```

2. 效果：

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024150818.png)

3. 可以看到 `Container` 具备多种组件的功能，通过查看 `Container` 源码，我们会很容易发现它正是前面我们介绍过的多种组件组合而成。在 Flutter 中，Container 组件也正是组合优先于继承的实例

## 5、剪裁（Clip）

### ①、剪裁类组件

1. Flutter 中提供了一些剪裁组件，用于对组件进行剪裁

| 剪裁 Widget | 默认行为                                                 |
| ---------- | -------------------------------------------------------- |
| ClipOval   | 子组件为正方形时剪裁成内贴圆形；为矩形时，剪裁成内贴椭圆 |
| ClipRRect  | 将子组件剪裁为圆角矩形                                   |
| ClipRect   | 默认剪裁掉子组件布局空间之外的绘制内容（溢出部分剪裁）   |
| ClipPath   | 按照自定义的路径剪裁                                     |

2. 下面看一个例子：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/05_容器组件（Container）.dart';
import '03_容器类组件/06_剪裁（Clip）.dart';

// 入口方法
void main() => runApp(const ClipComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';
import 'dart:math' as math;

class ClipComponent extends StatelessWidget {
  const ClipComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    Widget redBox = Container(
      constraints: const BoxConstraints.tightFor(width: 100, height: 100),
      color: Colors.red
    );

    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body:用于定义页面的主要内容区域
           * Center：居中布局
           */
          body:Column(
            children: [
              const SizedBox(height: 50),

              // 原本的样子
              redBox,
              const SizedBox(height: 10),

              // 子组件为正方形时剪裁成内贴圆形；为矩形时，剪裁成内贴椭圆
              ClipOval(child: redBox,),
              const SizedBox(height: 10),

              // 圆角矩形
              ClipRRect(
                // 设置圆角弧度
                borderRadius: BorderRadius.circular(10),
                child: redBox,
              ),
              const SizedBox(height: 10),

              // 剪裁掉一半图形，被剪裁的会溢出
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // 剪裁掉一部分
                  Align(
                    alignment: Alignment.topLeft,
                    // 宽度设为原来宽度一半
                    widthFactor: .5,
                    child: redBox,
                  ),
                  const Text("剪裁掉一部分")
                ],
              ),
              const SizedBox(height: 10),

              // 剪裁掉一半图形，使用 ClipRect，被剪裁的不会溢出
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // 剪裁掉一部分
                  ClipRect(
                    child: Align(
                      alignment: Alignment.topLeft,
                      // 宽度设为原来宽度一半
                      widthFactor: .5,
                      child: redBox,
                    ),
                  ),
                  const Text("剪裁掉一部分")
                ],
              )

            ],
          )

      )
    );
  }
}
```

3. 运行效果如图所示

![|378](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024155529.png)

### ②、自定义裁剪（CustomClipper）

1. 如果我们想剪裁子组件的特定区域，比如，在上面示例的图片中，如果我们只想截取图片中部 40×30 像素的范围应该怎么做？这时我们可以使用 `CustomClipper` 来自定义剪裁区域，实现代码如下：
2. 首先，自定义一个 `CustomClipper`：

```dart
class MyClipper extends CustomClipper<Rect> {
  /**
   * getClip() 是用于获取剪裁区域的接口，由于图片大小是 60×60，
   * 我们返回剪裁区域为 Rect.fromLTWH(10.0, 15.0, 40.0, 30.0)，即图片中部 40×30 像素的范围
   */
  @override
  Rect getClip(Size size) => Rect.fromLTWH(10.0, 15.0, 40.0, 30.0);
  /**
   * houldReclip() 接口决定是否重新剪裁。
   * 如果在应用中，剪裁区域始终不会发生变化时应该返回 false，这样就不会触发重新剪裁，避免不必要的性能开销。
   * 如果剪裁区域会发生变化（比如在对剪裁区域执行一个动画），那么变化后应该返回 true 来重新执行剪裁
   */
  @override
  bool shouldReclip(CustomClipper<Rect> oldClipper) => false;
}
```

3. 然后，我们通过 `ClipRect` 来执行剪裁，为了看清图片实际所占用的位置，我们设置一个红色背景：

```dart
DecoratedBox(
  decoration: BoxDecoration(
    color: Colors.red
  ),
  child: ClipRect(
    clipper: MyClipper(), //使用自定义的clipper
    child: avatar
  ),
)
```

4. 运行效果如图所示：

![|186](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024155959.png)

5. 可以看到我们的剪裁成功了，但是图片所占用的空间大小仍然是 60×60（红色区域），这是因为组件大小是是在 layout 阶段确定的，而剪裁是在之后的绘制阶段进行的，所以不会影响组件的大小，这和 `Transform` 原理是相似的。
6. `ClipPath` 可以按照自定义的路径实现剪裁，它需要自定义一个 `CustomClipper<Path>` 类型的 `Clipper`，定义方式和 `MyClipper` 类似，只不过 `getClip` 需要返回一个 `Path`，不再赘述。

## 6、空间适配（FittedBox）

### ①、FittedBox

1. 子组件大小超出了父组件大小时，如果不经过处理的话 Flutter 中就会显示一个溢出警告并在控制台打印错误日志，比如下面代码会导致溢出

```dart
Padding(
  padding: const EdgeInsets.symmetric(vertical: 30.0),
  child: Row(children: [Text('xx'*30)]), //文本长度超出 Row 的最大宽度会溢出
)
```

2. 运行效果如图所示：

![|696](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024160237.png)

3. 可以看到右边溢出了 45 像素。
4. 上面只是一个例子，理论上我们经常会遇到子元素的大小超过他父容器的大小的情况，比如一张很大图片要在一个较小的空间显示，根据 Flutter 的布局协议，父组件会将自身的最大显示空间作为约束传递给子组件，子组件应该遵守父组件的约束，如果子组件原始大小超过了父组件的约束区域，则需要进行一些缩小、裁剪或其他处理，而不同的组件的处理方式是特定的，比如 `Text` 组件，如果它的父组件宽度固定，高度不限的话，则默认情况下 `Text` 会在文本到达父组件宽度的时候换行。
5. 那如果我们想让 Text 文本在超过父组件的宽度时不要换行而是字体缩小呢？
6. 还有一种情况，比如父组件的宽高固定，而 Text 文本较少，这时候我们想让文本放大以填充整个父组件空间该怎么做呢？
7. 实际上，上面这两个问题的本质就是：子组件如何适配父组件空间。而根据 Flutter 布局协议适配算法应该在容器或布局组件的 layout 中实现，为了方便开发者自定义适配规则，Flutter 提供了一个 `FittedBox` 组件，定义如下：

```dart
const FittedBox({
  Key? key,
  this.fit = BoxFit.contain, // 适配方式
  this.alignment = Alignment.center, //对齐方式
  this.clipBehavior = Clip.none, //是否剪裁
  Widget? child,
})
```

### ②、适配原理

1. `FittedBox` 在布局子组件时会忽略其父组件传递的约束，可以允许子组件无限大，即 `FittedBox` 传递给子组件的约束为：`0<=width<=double.infinity, 0<= height <=double.infinity`
2. `FittedBox` 对子组件布局结束后就可以获得子组件真实的大小。
3. `FittedBox` 知道子组件的真实大小也知道他父组件的约束，那么 `FittedBox` 就可以通过指定的适配方式（BoxFit 枚举中指定），让起子组件在 `FittedBox` 父组件的约束范围内按照指定的方式显示。
4. 我们通过一个简单的例子说明：

```dart
Widget build(BuildContext context) {
  return Center(
    child: Column(
      children: [
        wContainer(BoxFit.none),
        Text('Wendux'),
        wContainer(BoxFit.contain),
        Text('Flutter中国'),
      ],
    ),
  );
}

Widget wContainer(BoxFit boxFit) {
  return Container(
    width: 50,
    height: 50,
    color: Colors.red,
    child: FittedBox(
      fit: boxFit,
      // 子容器超过父容器大小
      child: Container(width: 60, height: 70, color: Colors.blue),
    ),
  );
```

5. 运行后效果如图所示：

![|202](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231024160802.png)

6. 因为父 `Container` 要比子 `Container` 小，所以当没有指定任何适配方式时，子组件会按照其真实大小进行绘制，所以第一个蓝色区域会超出父组件的空间，因而看不到红色区域。
7. 第二个我们指定了适配方式为 `BoxFit.contain`，含义是按照子组件的比例缩放，尽可能多的占据父组件空间，因为子组件的长宽并不相同，所以按照比例缩放适配父组件后，父组件能显示一部分。
8. 要注意一点，在未指定适配方式时，虽然 `FittedBox` 子组件的大小超过了 `FittedBox` 父 `Container` 的空间，但 `FittedBox` 自身还是要遵守其父组件传递的约束，所以最终 `FittedBox` 的本身的大小是 50×50，这也是为什么蓝色会和下面文本重叠的原因，因为在布局空间内，父 `Container` 只占 50×50 的大小，接下来文本会紧挨着 `Container` 进行布局，而此时 `Container` 中有子组件的大小超过了自己，所以最终的效果就是绘制范围超出了 `Container`，但布局位置是正常的，所以就重叠了。如果我们不想让蓝色超出父组件布局范围，那么可以可以使用 `ClipRect` 对超出的部分剪裁掉即可：

```dart
 ClipRect( // 将超出子组件布局范围的绘制内容剪裁掉
  child: Container(
    width: 50,
    height: 50,
    color: Colors.red,
    child: FittedBox(
      fit: boxFit,
      child: Container(width: 60, height: 70, color: Colors.blue),
    ),
  ),
);
```

8. 关于 `BoxFit` 的各种适配规则和 `Image` 的 `fix` 属性指定是一样的，可以查看我们在介绍 `Image` 组件时关于各种适配规则对应的效果

## 7、页面骨架（Scaffold）

1. `Material` 组件库提供了丰富多样的组件，本节介绍一下最常用的 `Scaffold` 组件，其余的可以自行查看文档或 Flutter Gallery 中 Material 组件部分的示例。
2. 注意：Flutter Gallery 是 Flutter 官方提供的 Flutter Demo，源码位于 flutter 源码中的 examples 目录下，强烈建议用户将 Flutter Gallery 示例跑起来，它是一个很全面的 Flutter 示例应用，是非常好的参考 Demo，也是学习 Flutter 的第一手资料

### ①、Scaffold

1. 一个完整的路由页可能会包含导航栏、抽屉菜单 (`Drawer`) 以及底部 `Tab` 导航菜单等。
2. 如果每个路由页面都需要开发者自己手动去实现这些，这会是一件非常麻烦且无聊的事。
3. 幸运的是，Flutter Material 组件库提供了一些现成的组件来减少我们的开发任务。
4. `Scaffold` 是一个路由页的骨架，我们使用它可以很容易地拼装出一个完整的页面。
5. 我们实现一个页面，它包含：
	1. 一个导航栏
	2. 导航栏右边有一个分享按钮
	3. 有一个抽屉菜单
	4. 有一个底部导航
	5. 右下角有一个悬浮的动作按钮
6. 实现代码如下：

```dart
import 'package:flutter/material.dart';

import '03_容器类组件/07_页面骨架（Scaffold）.dart';

// 入口方法
void main() => runApp(const ScaffoldComponent());
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'dart:developer';

import 'package:flutter/material.dart';

import '08_页面骨架（Scaffold）抽屉.dart';

class ScaffoldComponent extends StatelessWidget {
  const ScaffoldComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * 导航栏
           */
          appBar: AppBar(
            // 导航栏标题
            title: const Text("月海"),
            // 导航栏右侧按钮
            actions: <Widget>[
              IconButton(icon: const Icon(Icons.share), onPressed: () {}),
            ],
          ),
          /**
           * 侧边栏抽屉
           * FractionallySizedBox 是一个小部件，用于根据父级容器的尺寸调整其子部件的大小。
           * FractionallySizedBox 的 widthFactor 和 heightFactor 属性用于指定子部件相对于父级容器的宽度和高度比例。
           * 这两个属性接受一个 0.0 到 1.0 之间的值，其中 0.0 表示子部件的大小为 0%，1.0 表示子部件的大小为父级容器的 100%。
           */
          drawer: const FractionallySizedBox(
            // 宽度为父组件的 0.6
            widthFactor: 0.6,
            child: ScaffoldDrawerComponent(),
          ),
          /**
           * 底部导航栏
           */
          bottomNavigationBar: BottomNavigationBar(
            /**
             * items：一个包含 BottomNavigationBarItem 的列表，用于定义每个导航项的图标和标签。
             * 每个 BottomNavigationBarItem 都包含一个 icon 参数用于指定图标，以及一个 label 参数用于指定标签文本
             */
            items: const <BottomNavigationBarItem>[
              BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
              BottomNavigationBarItem(icon: Icon(Icons.business), label: 'Business'),
              BottomNavigationBarItem(icon: Icon(Icons.school), label: 'School'),
            ],
            // currentIndex：一个整数，用于指定当前选中的导航项的索引。默认为 0，表示第一个导航项
            currentIndex: 0,
            // fixedColor：一个颜色值，用于指定选中导航项的颜色。当用户点击导航项时，选中的导航项将使用此颜色进行高亮显示
            fixedColor: Colors.blue,
            // onTap：一个回调函数，用于处理用户点击导航项的事件。当用户点击导航项时，将调用此回调函数，并传递被点击项的索引作为参数。
            onTap: _onItemTapped,
          ),
          /**
           * 悬浮按钮
           */
          floatingActionButton: FloatingActionButton(
            // 悬浮按钮点击事件
            onPressed:_onAdd,
            child: const Icon(Icons.add)
          ),
        )
    );
  }

  void _onItemTapped(int index) {
    log("点击了第 $index 个导航按钮");
  }

  void _onAdd(){
    log("点击了悬浮按钮");
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class ScaffoldDrawerComponent extends StatelessWidget {
  const ScaffoldDrawerComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.red,
      // 垂直线性布局
      child: const Column(
        // Row 在主轴(垂直)方向占用的空间
        mainAxisSize: MainAxisSize.max,
        children: [
          Text("抽屉", style: TextStyle(color: Colors.white),)
        ],
      )
    );
  }
}
```

7. 最终效果所示：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025151616.png)

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025151626.png)

8. 上面代码中我们用到了如下组件：

| 组件名称             | 解释           |
| -------------------- | -------------- |
| AppBar               | 一个导航栏骨架 |
| MyDrawer             | 抽屉菜单       |
| BottomNavigationBar  | 底部导航栏     |
| FloatingActionButton | 漂浮按钮       |

### ②、AppBar 导航栏骨架

1. AppBar 是一个 Material 风格的导航栏，通过它可以设置导航栏标题、导航栏菜单、导航栏底部的 Tab 标题等。下面我们看看 AppBar 的定义：

```dart
AppBar({
  Key? key,
  this.leading, //导航栏最左侧 Widget，常见为抽屉菜单按钮或返回按钮。
  this.automaticallyImplyLeading = true, //如果 leading 为 null，是否自动实现默认的 leading 按钮
  this.title,// 页面标题
  this.actions, // 导航栏右侧菜单
  this.bottom, // 导航栏底部菜单，通常为 Tab 按钮组
  this.elevation = 4.0, // 导航栏阴影
  this.centerTitle, //标题是否居中 
  this.backgroundColor,
  ...   //其他属性见源码注释
})
```

2. 如果给 `Scaffold` 添加了抽屉菜单，默认情况下 `Scaffold` 会自动将 `AppBar` 的 `leading` 设置为菜单按钮，点击它便可打开抽屉菜单。如果我们想自定义菜单图标，可以手动来设置 `leading`，如：

```dart
Scaffold(
  appBar: AppBar(
    title: Text("App Name"),
    leading: Builder(builder: (context) {
      return IconButton(
        icon: Icon(Icons.dashboard, color: Colors.white), //自定义图标
        onPressed: () {
          // 打开抽屉菜单  
          Scaffold.of(context).openDrawer(); 
        },
      );
    }),
    ...  
  )  
```

3. 代码运行效果如图所示：

![|261](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025152040.png)

4. 代码中打开抽屉菜单的方法在 `ScaffoldState` 中，通过 `Scaffold.of(context)` 可以获取父级最近的 `Scaffold` 组件的 `State` 对象

### ③、Drawer 抽屉菜单

1. `Scaffold` 的 `drawer` 和 `endDrawer` 属性可以分别接受一个 `Widget` 来作为页面的左、右抽屉菜单。
2. 如果开发者提供了抽屉菜单，那么当用户手指从屏幕左（或右）侧向里滑动时便可打开抽屉菜单。
3. 抽屉菜单通常将 `Drawer` 组件作为根节点，它实现了 `Material` 风格的菜单面板，`MediaQuery.removePadding` 可以移除 `Drawer` 默认的一些留白（比如 `Drawer` 默认顶部会留和手机状态栏等高的留白）

### ④、底部 Tab 导航栏

1. 我们可以通过 `Scaffold` 的 `bottomNavigationBar` 属性来设置底部导航，如本节开始示例所示，我们通过 `Material` 组件库提供的 `BottomNavigationBar` 和 `BottomNavigationBarItem` 两种组件来实现 `Material` 风格的底部导航栏。
2. 可以看到上面的实现代码非常简单，所以不再赘述，但是如果我们想实现如下图所示效果的底部导航栏应该怎么做呢？

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025152615.png)

3. `Material` 组件库中提供了一个 `BottomAppBar` 组件，它可以和 `FloatingActionButton` 配合实现这种“打洞”效果，源码如下：

```dart
bottomNavigationBar: BottomAppBar(
  color: Colors.white,
  shape: CircularNotchedRectangle(), // 底部导航栏打一个圆形的洞
  child: Row(
    children: [
      IconButton(icon: Icon(Icons.home)),
      SizedBox(), //中间位置空出
      IconButton(icon: Icon(Icons.business)),
    ],
    mainAxisAlignment: MainAxisAlignment.spaceAround, //均分底部导航栏横向空间
  ),
)
```

4. 可以看到，上面代码中没有控制打洞位置的属性，实际上，打洞的位置取决于 `FloatingActionButton` 的位置，上面 `FloatingActionButton` 的位置为：

```dart
floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
```

5. 所以打洞位置在底部导航栏的正中间。
6. `BottomAppBar` 的 `shape` 属性决定洞的外形，`CircularNotchedRectangle` 实现了一个圆形的外形，我们也可以自定义外形，比如，Flutter Gallery 示例中就有一个“钻石”形状的示例，感兴趣可以自行查看

### ⑤、FloatingActionButton 漂浮按钮

1. `FloatingActionButton` 是 `Material` 设计规范中的一种特殊 `Button`，通常悬浮在页面的某一个位置作为某种常用动作的快捷入口
2. 我们可以通过 `Scaffold` 的 `floatingActionButton` 属性来设置一个 `FloatingActionButton`，同时通过 `floatingActionButtonLocation` 属性来指定其在页面中悬浮的位置，这个比较简单，不再赘述

### ⑥、页面 body

1. 最后就是页面的 `Body` 部分了
2. `Scaffold` 有一个 `body` 属性，接收一个 `Widget`，我们可以传任意的 `Widget` 
3. 在下一章中，我们会介绍 `TabBarView`，它是一个可以进行页面切换的组件，在多 Tab 的 App 中，一般都会将 `TabBarView` 作为 `Scaffold` 的 `Body`

# 六、可滚动组件

## 1、可滚动组件简介

### ①、`Sliver` 布局模型

1. 通常可滚动组件的子组件可能会非常多、占用的总高度也会非常大；如果要一次性将子组件全部构建出将会非常昂贵！
2. 为此，Flutter 中提出一个 `Sliver`（中文为“薄片”的意思）概念，`Sliver` 可以包含一个或多个子组件。
3. `Sliver` 的主要作用是配合：加载子组件并确定每一个子组件的布局和绘制信息，如果 `Sliver` 可以包含多个子组件时，通常会实现按需加载模型。
4. 只有当 `Sliver` 出现在视口中时才会去构建它，这种模型也称为“基于 `Sliver` 的列表按需加载模型”。
5. 可滚动组件中有很多都支持基于 `Sliver` 的按需加载模型，如 `ListView`、`GridView`，但是也有不支持该模型的，如 `SingleChildScrollView`。
6. 约定：后面如果我们说一个组件是 `Sliver` 则表示它是基于 `Sliver` 布局的组件；同理，说一个组件是 `RenderBox`，则代表它是基于盒模型布局的组件，并不是说它就是 `RenderBox` 类的实例。
7. Flutter 中的可滚动组件主要由三个角色组成：`Scrollable`、`Viewport` 和 `Sliver`：
	1. `Scrollable` ：用于处理滑动手势，确定滑动偏移，滑动偏移变化时构建 `Viewport` 。
	2. `Viewport`：显示的视窗，即列表的可视区域；
	3. `Sliver`：视窗里显示的元素。
8. 具体布局过程：
	1. `Scrollable` 监听到用户滑动行为后，根据最新的滑动偏移构建 `Viewport` 。
	2. `Viewport` 将当前视口信息和配置信息通过 `SliverConstraints` 传递给 `Sliver`。
	3. `Sliver` 中对子组件（`RenderBox`）按需进行构建和布局，然后确认自身的位置、绘制等信息，保存在 `geometry` 中（一个 `SliverGeometry` 类型的对象）。
9. 比如有一个 `ListView`，大小撑满屏幕，假设它有 100 个列表项（都是 `RenderBox`）且每个列表项高度相同，结构如图所示：

![|530](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025153857.png)

10. 图中白色区域为设备屏幕，也是 `Scrollable` 、 `Viewport` 和 `Sliver` 所占用的空间，三者所占用的空间重合
11. 父子关系为：`Sliver` 父组件为 `Viewport`，`Viewport` 的 父组件为 `Scrollable` 。
12. 注意 `ListView` 中只有一个 `Sliver`，在 `Sliver` 中实现了子组件（列表项）的按需加载和布局。
13. 其中顶部和底部灰色的区域为 `cacheExtent`，它表示预渲染的高度，需要注意这是在可视区域之外，如果 `RenderBox` 进入这个区域内，即使它还未显示在屏幕上，也是要先进行构建的，预渲染是为了后面进入 `Viewport` 的时候更丝滑。
14. `cacheExtent` 的默认值是 `250`，在构建可滚动列表时我们可以指定这个值，这个值最终会传给 `Viewport`。

### ②、Scrollable

1. `Scrollable` 用于处理滑动手势，确定滑动偏移，滑动偏移变化时构建 `Viewport`，我们看一下其关键的属性：

```dart
Scrollable({
  ...
  /**
   * axisDirection 滚动方向
   */
  this.axisDirection = AxisDirection.down,
  /**
   * controller：此属性接受一个 ScrollController 对象。
   * ScrollController 的主要作用是控制滚动位置和监听滚动事件。
   * 默认情况下，Widget 树中会有一个默认的 PrimaryScrollController，如果子树中的可滚动组件没有显式的指定controller，
   * 并且 primary 属性值为 true 时（默认就为 true），可滚动组件会使用这个默认的 PrimaryScrollController。
   * 这种机制带来的好处是父组件可以控制子树中可滚动组件的滚动行为，
   * 例如，Scaffold 正是使用这种机制在 iOS 中实现了点击导航栏回到顶部的功能
   */
  this.controller,
  /**
   * physics：此属性接受一个 ScrollPhysics 类型的对象，它决定可滚动组件如何响应用户操作，
   * 比如用户滑动完抬起手指后，继续执行动画；或者滑动到边界时，如何显示。
   * 默认情况下，Flutter 会根据具体平台分别使用不同的 ScrollPhysics 对象，应用不同的显示效果，
   * 如当滑动到边界时，继续拖动的话，在 iOS 上会出现弹性效果，而在 Android 上会出现微光效果。
   * 如果你想在所有平台下使用同一种效果，可以显式指定一个固定的 ScrollPhysics，
   * Flutter SDK 中包含了两个 ScrollPhysics 的子类，他们可以直接使用：
   *     ClampingScrollPhysics：列表滑动到边界时将不能继续滑动，通常在 Android 中 配合 GlowingOverscrollIndicator（实现微光效果的组件） 使用。
   *     BouncingScrollPhysics：iOS 下弹性效果。
   */
  this.physics,
  /**
   * viewportBuilder：构建 Viewport 的回调。
   * 当用户滑动时，Scrollable 会调用此回调构建新的 Viewport，同时传递一个 ViewportOffset 类型的 offset 参数，该参数描述 Viewport 应该显示哪一部分内容。
   * 注意重新构建 Viewport 并不是一个昂贵的操作，因为 Viewport 本身也是 Widget，只是配置信息，
   * Viewport 变化时对应的 RenderViewport 会更新信息，并不会随着 Widget 进行重新构建
   */
  required this.viewportBuilder,
})
```

2. 主轴和纵轴：在可滚动组件的坐标描述中，通常将滚动方向称为主轴，非滚动方向称为纵轴。由于可滚动组件的默认方向一般都是沿垂直方向，所以默认情况下主轴就是指垂直方向，水平方向同理

### ③、Viewport

1. `Viewport` 比较简单，用于渲染当前视口中需要显示 `Sliver`：

```dart
Viewport({
  Key? key,
  this.axisDirection = AxisDirection.down,
  this.crossAxisDirection,
  this.anchor = 0.0,
  required ViewportOffset offset, // 用户的滚动偏移
  // 类型为Key，表示从什么地方开始绘制，默认是第一个元素
  this.center,
  this.cacheExtent, // 预渲染区域
  //该参数用于配合解释cacheExtent的含义，也可以为主轴长度的乘数
  this.cacheExtentStyle = CacheExtentStyle.pixel, 
  this.clipBehavior = Clip.hardEdge,
  List<Widget> slivers = const <Widget>[], // 需要显示的 Sliver 列表
})
```

2. 需要注意的是：
3. `offset`：该参数为 `Scrollabel` 构建 `Viewport` 时传入，它描述了 `Viewport` 应该显示哪一部分内容。
4. `cacheExtent` 和 `cacheExtentStyle`：`CacheExtentStyle` 是一个枚举，有 `pixel` 和 `viewport` 两个取值。当 `cacheExtentStyle` 值为 `pixel` 时，`cacheExtent` 的值为预渲染区域的具体像素长度；当值为 `viewport` 时，`cacheExtent` 的值是一个乘数，表示有几个 `viewport` 的长度，最终的预渲染区域的像素长度为：`cacheExtent * viewport` 的积， 这在每一个列表项都占满整个 `Viewport` 时比较实用，这时 `cacheExtent` 的值就表示前后各缓存几个页面

### ④、Sliver

1. `Sliver` 主要作用是对子组件进行构建和布局，比如 `ListView` 的 `Sliver` 需要实现子组件（列表项）按需加载功能，只有当列表项进入预渲染区域时才会去对它进行构建和布局、渲染。
2. `Sliver` 对应的渲染对象类型是 `RenderSliver`，`RenderSliver` 和 `RenderBox` 的相同点是都继承自 `RenderObject` 类，不同点是在布局的时候约束信息不同。
3. `RenderBox` 在布局时父组件传递给它的约束信息对应的是 `BoxConstraints`，只包含最大宽高的约束；而 `RenderSliver` 在布局时父组件（列表）传递给它的约束是对应的是 `SliverConstraints`

### ⑤、可滚动组件的通用配置

1. 几乎所有的可滚动组件在构造时都能指定 `scrollDirection`（滑动的主轴）、`reverse`（滑动方向是否反向）、`controller`、`physics` 、`cacheExtent` ，这些属性最终会透传给对应的 `Scrollable` 和 `Viewport`，这些属性我们可以认为是可滚动组件的通用属性，后续再介绍具体的可滚动组件时将不再赘述。
2. `reverse` 表示是否按照阅读方向相反的方向滑动，如：`scrollDirection` 值为 `Axis.horizontal` 时，即滑动方向为水平，如果阅读方向是从左到右（取决于语言环境，阿拉伯语就是从右到左）。`reverse` 为 `true` 时，那么滑动方向就是从右往左。

### ⑥、ScrollController

1. 可滚动组件都有一个 `controller` 属性，通过该属性我们可以指定一个 `ScrollController` 来控制可滚动组件的滚动比如可以通过 `ScrollController` 来同步多个组件的滑动联动。
2. 由于 `ScrollController` 是需要结合可滚动组件一起工作，所以本章中，我们会在介绍完 `ListView` 后详细介绍 `ScrollController`

### ⑦、子节点缓存

1. 按需加载子组件在大多数场景中都能有正收益，但是有些时候也会有副作用。
2. 比如有一个页面，它由一个 `ListView` 组成，我们希望在页面顶部显示一块内容， 这部分内容的数据需要在每次页面打开时通过网络来获取，为此我们通一个 `Header` 组件来实现，它是一个 `StatefulWidget` ，会在 `initState` 中请求网络数据，然后将它作为 `ListView` 的第一个孩子。
3. 现在问题来了，因为 `ListView` 是按需加载子节点的，这意味着如果 `Header` 滑出 `Viewport` 的预渲染区域之外时就会被销毁，重新滑入后又会被重新构建，这样就会发起多次网络请求，不符合我们期望，我们预期是 `Header` 能够缓存不销毁。
4. 综上，为了方便控制子组件在滑出可视区域后是否缓存，可滚动组件提供了一种缓存子节点的通用解决方案，它允许开发者对特定的子界限进行缓存，这个我们将在后面小节中详细介绍

### ⑧、Scrollbar

1. `Scrollbar` 是一个 `Material` 风格的滚动指示器（滚动条），如果要给可滚动组件添加滚动条，只需将 `Scrollbar` 作为可滚动组件的任意一个父级组件即可，如

```dart
Scrollbar(
  child: SingleChildScrollView(
    ...
  ),
);
```

2. `Scrollbar` 和 `CupertinoScrollbar` 都是通过监听滚动通知来确定滚动条位置的。
3. 关于的滚动通知的详细内容我们将在本章最后一节中专门介绍

## 2、SingleChildScrollView 可滚动组件

### ①、简介

1. `SingleChildScrollView` 类似于 Android 中的 `ScrollView`，它只能接收一个子组件，定义如下：

```dart
SingleChildScrollView({
  this.scrollDirection = Axis.vertical, //滚动方向，默认是垂直方向
  this.reverse = false, 
  this.padding, 
  bool primary, 
  this.physics, 
  this.controller,
  this.child,
})
```

2. 除了上一节我们介绍过的可滚动组件的通用属性外，我们重点看 `primary` 属性：它表示是否使用 `widget` 树中默认的 `PrimaryScrollController`（`MaterialApp` 组件树中已经默认包含一个 `PrimaryScrollController` 了）
3. 当滑动方向为垂直方向（`scrollDirection` 值为 `Axis.vertical`）并且没有指定 `controller` 时，`primary` 默认为 `true`。
4. 需要注意的是，通常 `SingleChildScrollView` 只应在期望的内容不会超过屏幕太多时使用，这是因为 `SingleChildScrollView` 不支持基于 `Sliver` 的延迟加载模型，所以如果预计视口可能包含超出屏幕尺寸太多的内容时，那么使用 `SingleChildScrollView` 将会非常昂贵（性能差），此时应该使用一些支持 `Sliver` 延迟加载的可滚动组件，如 `ListView`。

### ②、实例

1. 下面是一个将大写字母 A-Z 沿垂直方向显示的例子，由于垂直方向空间会超过屏幕视口高度，所以我们使用 `SingleChildScrollView`

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/01_SingleChildScrollView.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: SingleChildScrollViewComponent(),
      )
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class SingleChildScrollViewComponent extends StatelessWidget {
  const SingleChildScrollViewComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    String str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Scrollbar：显示滚动条
    return Scrollbar(
      // SingleChildScrollView 可滚动组件
      child: SingleChildScrollView(
        // 内边距
        padding: const EdgeInsets.all(16.0),
        // Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
        child: Center(
          // Column：用于在垂直方向上排列子组件；它允许多个小部件垂直堆叠在一起，以构建垂直布局
          child: Column(
            // 将字符串 str 拆分成单个字符
            children: str.split("")
              /**
               * 对拆分后的每个字符执行映射操作。使用 map 方法将每个字符 c 转换为一个 Text 小部件。
               * textScaleFactor: 2.0 用于将字体大小设置为原来的两倍
               */
              .map((c) => Text(c, textScaleFactor: 2.0,))
              // 将映射操作后的结果转换为一个小部件列表
              .toList(),
          ),
        ),
      ),
    );
  }
}
```

2. 效果：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025162350.png)

## 3、ListView 列表组件

1. `ListView` 是最常用的可滚动组件之一，它可以沿一个方向线性排布所有子组件，
2. 并且它也支持列表项懒加载（在需要时才会创建）

### ①、默认构造函数

1. 我们看看 ListView 的默认构造函数定义：

```dart
ListView({
  ...  
  //可滚动 widget 公共参数
  Axis scrollDirection = Axis.vertical,
  bool reverse = false,
  ScrollController? controller,
  bool? primary,
  ScrollPhysics? physics,
  EdgeInsetsGeometry? padding,
  
  // ListView 各个构造函数的共同参数
  /**
   * temExtent：该参数如果不为 null，则会强制 children 的“长度”为 itemExtent 的值；
   * 这里的“长度”是指滚动方向上子组件的长度，也就是说如果滚动方向是垂直方向，则 itemExtent 代表子组件的高度；
   * 如果滚动方向为水平方向，则 itemExtent 就代表子组件的宽度。
   * 在 ListView 中，指定 itemExtent 比让子组件自己决定自身长度会有更好的性能，
   * 这是因为指定 itemExtent 后，滚动系统可以提前知道列表的长度，而无需每次构建子组件时都去再计算一下，
   * 尤其是在滚动位置频繁变化时（滚动系统需要频繁去计算列表高度）。
   */
  double? itemExtent,
  /**
   * prototypeItem：如果我们知道列表中的所有列表项长度都相同但不知道具体是多少，
   * 这时我们可以指定一个列表项，该列表项被称为 prototypeItem（列表项原型）。
   * 指定 prototypeItem 后，可滚动组件会在 layout 时计算一次它延主轴方向的长度，
   * 这样也就预先知道了所有列表项的延主轴方向的长度，所以和指定 itemExtent 一样，
   * 指定 prototypeItem 会有更好的性能。
   * 注意，itemExtent 和prototypeItem 互斥，不能同时指定它们
   */
  Widget? prototypeItem,
  /**
   * shrinkWrap：该属性表示是否根据子组件的总长度来设置 ListView 的长度，默认值为false 。
   * 默认情况下，ListView 会在滚动方向尽可能多的占用空间。
   * 当 ListView 在一个无边界(滚动方向上)的容器中时，shrinkWrap 必须为 true
   */
  bool shrinkWrap = false,
  /**
   * addAutomaticKeepAlives：该属性我们将在介绍 PageView 组件时详细解释
   */
  bool addAutomaticKeepAlives = true,
  /**
   * addRepaintBoundaries：该属性表示是否将列表项（子组件）包裹在 RepaintBoundary 组件中。
   * RepaintBoundary 可以先简单理解为它是一个“绘制边界”，将列表项包裹在 RepaintBoundary 中可以避免列表项不必要的重绘，
   * 但是当列表项重绘的开销非常小（如一个颜色块，或者一个较短的文本）时，
   * 不添加 RepaintBoundary反而会更高效（具体原因会在后面 Flutter 绘制原理相关章节中介绍）。
   * 如果列表项自身来维护是否需要添加绘制边界组件，则此参数应该指定为 false
   */
  bool addRepaintBoundaries = true,
  // 预渲染区域长度
  double? cacheExtent,
    
  //子 widget 列表
  List<Widget> children = const <Widget>[],
})
```

2. 上面参数分为两组：第一组是可滚动组件的公共参数，之前已经介绍过，不再赘述；第二组是 `ListView` 各个构造函数（`ListView` 有多个构造函数）的共同参数
3. 注意：上面这些参数并非 `ListView` 特有，在后面介绍的其他可滚动组件也可能会拥有这些参数，它们的含义是相同的。
4. 默认构造函数有一个 `children` 参数，它接受一个 `Widget` 列表（`List<Widget>`）。
5. 这种方式适合只有少量的子组件数量已知且比较少的情况，反之则应该使用 `ListView.builder` 按需动态构建列表项。
6. 注意：虽然这种方式将所有 `children` 一次性传递给 `ListView`，但子组件仍然是在需要时才会加载（build（如有）、布局、绘制），也就是说通过默认构造函数构建的 `ListView` 也是基于 `Sliver` 的列表懒加载模型
7. 下面是一个例子：

```dart
ListView(
  shrinkWrap: true, 
  padding: const EdgeInsets.all(20.0),
  children: <Widget>[
    const Text('I\'m dedicating every day to you'),
    const Text('Domestic life was never quite my style'),
    const Text('When you smile, you knock me out, I fall apart'),
    const Text('And I thought I was so smart'),
  ],
);
```

8. 可以看到，虽然使用默认构造函数创建的列表也是懒加载的，但我们还是需要提前将 `Widget` 创建好，等到真正需要加载的时候才会对 `Widget` 进行布局和绘制

### ②、ListView.builder 

1. `ListView.builder` 适合列表项比较多或者列表项不确定的情况，下面看一下 `ListView.builder` 的核心参数列表：

```dart
ListView.builder({
  // ListView公共参数已省略  
  ...
  /**
   * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
   * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
   */
  required IndexedWidgetBuilder itemBuilder,
  /**
   * itemCount：列表项的数量，如果为 null，则为无限列表
   */
  int itemCount,
  ...
})
```

2. 下面看一个例子：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/01_SingleChildScrollView/01_SingleChildScrollView.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ListViewBuilderComponent(),
      )
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class ListViewBuilderComponent extends StatelessWidget {
  const ListViewBuilderComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Scrollbar：显示滚动条
    return Scrollbar(
      // ListView 列表组件
      child: ListView.builder(
        // itemCount：列表项的数量，如果为 null，则为无限列表
        itemCount: 100,
        // 强制高度为 50.0
        itemExtent: 50.0,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index) {
          return ListTile(title: Text("$index"));
        }
      )
    );
  }
}
```

3. 运行效果如图所示：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025164241.png)

### ③、ListView.separated 分割组件

1. `ListView.separated` 可以在生成的列表项之间添加一个分割组件，它比 `ListView.builder` 多了一个 `separatorBuilder` 参数，该参数是一个分割组件生成器。
2. 下面我们看一个例子：奇数行添加一条蓝色下划线，偶数行添加一条红色下划线

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/01_SingleChildScrollView/01_SingleChildScrollView.dart';

// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ListViewBuilderComponent(),
      )
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class ListViewBuilderComponent extends StatelessWidget {
  const ListViewBuilderComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 创建下划线 widget 预定义以供复用。
    Widget dividerBlue = const Divider(color: Colors.blue,);
    Widget dividerRed = const Divider(color: Colors.red);

    // Scrollbar：显示滚动条
    return Scrollbar(
      // ListView 列表组件
      child: ListView.separated(
        // itemCount：列表项的数量，如果为 null，则为无限列表
        itemCount: 100,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index) {
          return ListTile(title: Text("$index"));
        },
        // 分割器构造器
        separatorBuilder: (BuildContext context, int index) {
          return index % 2 == 0 ? dividerBlue: dividerRed;
        },
      )
    );
  }
}
```

3. 运行效果如图所示：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231025164940.png)

### ④、ListView 原理

1. `ListView` 内部组合了 `Scrollable`、`Viewport` 和 `Sliver`，需要注意：
2. `ListView` 中的列表项组件都是 `RenderBox`，并不是 `Sliver`， 这个一定要注意。
3. 一个 `ListView` 中只有一个 `Sliver`，对列表项进行按需加载的逻辑是 `Sliver` 中实现的。
4. `ListView` 的 `Sliver` 默认是 `SliverList`，如果指定了 `itemExtent` ，则会使用 `SliverFixedExtentList`；
5. 如果 `prototypeItem` 属性不为空，则会使用 `SliverPrototypeExtentList`，无论是是哪个，都实现了子组件的按需加载模型。

### ⑤、固定高度列表

1. 前面说过，给列表指定 `itemExtent` 或 `prototypeItem` 会有更高的性能，所以当我们知道列表项的高度都相同时，强烈建议指定 `itemExtent` 或 `prototypeItem` 。下面看一个示例

```dart
class FixedExtentList extends StatelessWidget {
  const FixedExtentList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
   		prototypeItem: ListTile(title: Text("1")),
      //itemExtent: 56,
      itemBuilder: (context, index) {
        //LayoutLogPrint是一个自定义组件，在布局时可以打印当前上下文中父组件给子组件的约束信息
        return LayoutLogPrint(
          tag: index, 
          child: ListTile(title: Text("$index")),
        );
      },
    );
  }
}
```

2. 因为列表项都是一个 `ListTile`，高度相同，但是我们不知道 `ListTile` 的高度是多少，所以指定了 `prototypeItem` ，运行后，控制台打印：

```cmd
flutter: 0: BoxConstraints(w=428.0, h=56.0)
flutter: 1: BoxConstraints(w=428.0, h=56.0)
flutter: 2: BoxConstraints(w=428.0, h=56.0)
...
```

3. 可见 `ListTile` 的高度是 56 ，所以我们指定 `itemExtent` 为 56也是可以的。但是还是建议优先指定原型，这样的话在列表项布局修改后，仍然可以正常工作（前提是每个列表项的高度相同）。
4. 如果本例中不指定 `itemExtent` 或 `prototypeItem` ，我们看看控制台日志信息：

```cmd
flutter: 0: BoxConstraints(w=428.0, 0.0<=h<=Infinity)
flutter: 1: BoxConstraints(w=428.0, 0.0<=h<=Infinity)
flutter: 2: BoxConstraints(w=428.0, 0.0<=h<=Infinity)
...
```

5. 可以发现，列表不知道列表项的具体高度，高度约束变为 0.0 到 Infinity。

### ⑥、实例：无限加载列表

1. 假设我们要从数据源异步分批拉取一些数据，然后用 `ListView` 展示
2. 当我们滑动到列表的某一个位置（倒数第五个）时，去拉取数据，拉取成功后将数据插入列表，代码如下：

```dart
import 'package:flutter/material.dart';

class InfiniteListViewComponent extends StatefulWidget {
  const InfiniteListViewComponent({Key? key}) : super(key: key);

  @override
  _InfiniteListViewComponentState createState() => _InfiniteListViewComponentState();
}

class _InfiniteListViewComponentState extends State<InfiniteListViewComponent> {
  // 刷新次数
  int _num = 0;
  // 数据，用于显示 ListView 列表，初始值为 20 条数据，每次刷新增加 20 条数据
  final List<String> _data = List.generate(20, (index) => "第 0 次刷新、第 ${index + 1} 条数据");

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
    return Scrollbar(
      // ListView 列表组件
      child: ListView.separated(
        // itemCount：列表项的数量：_data 的长度
        itemCount: _data.length,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index) {
          // 如果到了末尾
          if(index == _data.length - 1 -5){
            // 刷新次数 + 1
            _num++;
            // 获取数据，添加到 _data 中，刷新列表
            _retrieveData();
          }
          return ListTile(title: Text(_data[index]));
        },
        // 分割器构造器
        separatorBuilder: (context, index) => const Divider(color: Colors.red),
      )
    );
  }

  void _retrieveData(){
    // 等待模拟的网络请求完成
    Future.delayed(const Duration(milliseconds: 5)).then((value) => {
      setState(() {
        _data.addAll(List.generate(20, (index) => "第 $_num 次刷新、第 ${index + 1 + _data.length} 条数据"));
      })
    });
  }

}
```

3. 运行后效果如图所示：

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231106100141.png)

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231106100150.png)

### ⑦、表头

1. ListView 并没有表头这个属性，但是可以使用其他方式来实现，如 `Column` 配合 `ListView` 等
2. 此处使用 Scaffold 和 CustomScrollView 实现

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/02_ListView/04_表头.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: HeaderListViewComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class HeaderListViewComponent extends StatefulWidget {
  const HeaderListViewComponent({Key? key}) : super(key: key);

  @override
  _HeaderListViewComponentState createState() => _HeaderListViewComponentState();
}

class _HeaderListViewComponentState extends State<HeaderListViewComponent> {
  // 刷新次数
  int _num = 0;
  // 数据，用于显示 ListView 列表，初始值为 20 条数据，每次刷新增加 20 条数据
  final List<String> _data = List.generate(20, (index) => "第 0 次刷新、第 ${index + 1} 条数据");

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Scaffold 是一个用于创建基本页面布局的小部件。
    return Scaffold(
      /**
       * body: 用于定义页面的主要内容区域
       * CustomScrollView 可以包含多个 Sliver 类型的小部件，如 SliverAppBar、SliverList、SliverGrid 等。
       * 每个 Sliver 类型的小部件都可以根据需要进行配置，以实现不同的滚动效果和布局。
       * 通过使用 CustomScrollView，可以创建具有复杂滚动行为的界面，如具有固定表头和可滚动内容的列表、具有多个不同类型滚动小部件的复合滚动效果等
       */
      body: CustomScrollView(
        /**
         * slivers 是一个 CustomScrollView 的参数，它是一个包含多个 Sliver 类型小部件的列表。Sliver 是一种特殊类型的小部件，用于创建可滚动的内容。
         * Sliver 类型的小部件与普通的小部件不同，它们是在可滚动视图中使用的，可以根据需要进行配置，以实现不同的滚动效果和布局。
         * Sliver 小部件通常用于构建具有特定滚动行为的界面，如固定表头、悬停效果、可扩展的列表项等。
         * 常见的 Sliver 类型小部件有：
         *    SliverAppBar：创建一个带有可折叠效果的应用栏，可以固定在顶部或底部。
         *    SliverList：创建一个垂直滚动的列表，可以包含多个列表项。
         *    SliverGrid：创建一个网格布局的列表，可以包含多个网格项。
         *    SliverToBoxAdapter：将一个普通的小部件包装为 Sliver 类型的小部件，用于在滚动视图中显示任意内容。
         */
        slivers: [
          // SliverAppBar：创建一个带有可折叠效果的应用栏，可以固定在顶部或底部
          const SliverAppBar(
            /**
             * pinned 是 SliverAppBar 的一个属性，用于控制应用栏是否固定在顶部。
             * 如果设置为 true，则应用栏将一直保持在顶部，不会随着滚动而消失。
             * 如果设置为 false，则应用栏会在滚动时自动隐藏，并在滚动到顶部时重新出现
             */
            pinned: true,
            title: Text('表头'),
          ),
          // SliverList：创建一个垂直滚动的列表，可以包含多个列表项
          SliverList(
            /**
             * delegate 是 SliverList 和 SliverGrid 的一个属性，用于指定子部件的构建方式。
             * 在 SliverChildBuilderDelegate 中，可以通过提供一个构建器函数来生成子部件。
             * SliverChildBuilderDelegate 的构造函数有两个参数：
             *    childCount：一个整数，指定子部件的数量。如果设置为 null，则表示子部件的数量不确定。
             *    builder：一个函数，用于构建每个子部件。它接收两个参数：上下文 BuildContext 和索引 int，并返回一个小部件。
             */
            delegate: SliverChildBuilderDelegate(
              childCount: _data.length,
              (BuildContext context, int index) {
                if (index == _data.length - 1 - 5) {
                  _num++;
                  _retrieveData();
                }
                return ListTile(title: Text(_data[index]));
              },
            ),
          ),
        ],
      ),
    );
  }

  void _retrieveData() {
    Future.delayed(const Duration(milliseconds: 5)).then((value) => {
      setState(() {
        _data.addAll(List.generate(20, (index) => "第 $_num 次刷新、第 ${index + 1 + _data.length} 条数据"));
      })
    });
  }
}

```

3. 效果：

![|361](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231106165957.png)

## 4、滚动监听及控制

### ①、ScrollController 滚动监听

1. `ScrollController` 构造函数如下：

```dart
ScrollController({
  double initialScrollOffset = 0.0, //初始滚动位置
  this.keepScrollOffset = true,//是否保存滚动位置
  ...
})
```

2. `ScrollController` 常用的属性和方法：
3. `offset`：可滚动组件当前的滚动位置。
4. `jumpTo(double offset)、animateTo(double offset,...)`：这两个方法用于跳转到指定的位置，它们不同之处在于，后者在跳转时会执行一个动画，而前者不会。
5. `ScrollController` 还有一些属性和方法，我们将在后面原理部分解释。

#### Ⅰ、滚动监听

- `ScrollController` 间接继承自 `Listenable`，我们可以根据 `ScrollController` 来监听滚动事件，如：

```dart
controller.addListener(()=>print(controller.offset))
```

#### Ⅱ、实例

1. 我们创建一个 ListView，当滚动位置发生变化时，我们先打印出当前滚动位置
2. 然后判断当前位置是否超过屏幕像素，如果超过则在屏幕右下角显示一个“返回顶部”的按钮，该按钮点击后可以使 ListView 恢复到初始位置；
3. 如果没有超过像素，则隐藏“返回顶部”按钮。代码如下：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/03_滚动监听及控制/01_ScrollController 滚动监听.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ScrollControllerComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class ScrollControllerComponent extends StatefulWidget {
  const ScrollControllerComponent({Key? key}) : super(key: key);

  @override
  _ScrollControllerComponentState createState() => _ScrollControllerComponentState();
}

class _ScrollControllerComponentState extends State<ScrollControllerComponent> {
  // ScrollController 是一个用于控制可滚动组件（如 ListView、GridView、SingleChildScrollView 等）的控制器。
  ScrollController _controller = ScrollController();

  // 刷新次数
  int _num = 0;
  // 数据，用于显示 ListView 列表，初始值为 20 条数据，每次刷新增加 20 条数据
  final List<String> _data = List.generate(20, (index) => "第 0 次刷新、第 ${index + 1} 条数据");
  // 是否显示 返回到顶部 按钮
  bool showToTopBtn = false;
  // 添加一个变量用于保存屏幕的纵向尺寸（纵向像素）
  double screenHeight = 0;

  @override
  void initState() {
    super.initState();
    // 监听滚动事件，打印滚动位置
    _controller.addListener(() {
      /**
       * 打印滚动位置
       * offset 的值表示可滚动组件内容顶部相对于可滚动区域顶部的偏移量。
       * 初始情况下，offset 的值通常为 0，表示内容顶部与可滚动区域顶部对齐，没有发生滚动。
       * 向下滚动列表时，offset 的值会逐渐增加；向上滚动列表时，offset 的值会逐渐减小
       */
      print("月海：${_controller.offset}");
      // 如果当前列表的偏移量小于屏幕的纵向尺寸，且 返回到顶部 按钮已经显示，则隐藏按钮
      if (_controller.offset < screenHeight && showToTopBtn) {
        setState(() {
          showToTopBtn = false;
        });
        // 如果当前列表的偏移量大于屏幕的纵向尺寸，且 返回到顶部 按钮没有显示，则显示按钮
      } else if (_controller.offset >= screenHeight && !showToTopBtn) {
        setState(() {
          showToTopBtn = true;
        });
      }
    });
  }

  /// dispose 方法是一个生命周期方法，它在 State 对象被永久地从内存中移除之前被调用。
  @override
  void dispose() {
    // 为了避免内存泄露，需要调用 _controller.dispose 释放资源
    _controller.dispose();
    super.dispose();
  }

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // 获取屏幕的尺寸
    Size screenSize = MediaQuery.of(context).size;
    // 获取屏幕的纵向尺寸（纵向像素）
    screenHeight = screenSize.height;

    /**
     * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
     * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
     */
    return Scaffold(
      /**
       * body: 用于定义页面的主要内容区域
       * Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
       */
      body: Scrollbar(
        // ListView 列表组件
        child: ListView.separated(
          // controller：控制器，用于控制 ListView 的滚动位置
          controller: _controller,
          // itemCount：列表项的数量：_data 的长度
          itemCount: _data.length,
          /**
           * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
           * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
           */
          itemBuilder: (BuildContext context, int index) {
          // 如果到了末尾
          if(index == _data.length - 1 - 5){
            // 刷新次数 + 1
            _num++;
            // 获取数据，添加到 _data 中，刷新列表
            _retrieveData();
          }
          return ListTile(title: Text(_data[index]));
        },
        // 分割器构造器
        separatorBuilder: (context, index) => const Divider(color: Colors.red),
        ),
      ),
      /**
       * 悬浮按钮
       * showToTopBtn 为 true 时显示，为 false 时隐藏
       */
      floatingActionButton: !showToTopBtn ? null : FloatingActionButton(
        // child 属性用于设置悬浮按钮的内容，通常是一个 Icon 小部件
        child: const Icon(Icons.arrow_upward),
        // onPressed 点击事件
        onPressed: () {
          /**
           * animateTo 方法可以滚动列表到指定的位置
           * 参数 1：指定滚动的偏移量，0 表示滚动到列表的起始位置
           * 参数 2：滚动动画执行的时间，这里设置为 200 毫秒
           * 参数 3：滚动动画曲线，这里设置为 Curves.ease，表示动画曲线为匀速曲线
           */
          _controller.animateTo(0, duration: const Duration(milliseconds: 200), curve: Curves.ease);
        },
      )
    );
  }

  void _retrieveData(){
    // 等待模拟的网络请求完成
    Future.delayed(const Duration(milliseconds: 5)).then((value) => {
      setState(() {
        _data.addAll(List.generate(20, (index) => "第 $_num 次刷新、第 ${index + 1 + _data.length} 条数据"));
      })
    });
  }

}
```

4. 结果

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231107124424.png)

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231107124432.png)

#### Ⅲ、滚动位置恢复

1. `PageStorage` 是一个用于保存页面(路由)相关数据的组件，它并不会影响子树的 UI 外观，其实，`PageStorage` 是一个功能型组件，它拥有一个存储桶（bucket），子树中的 `Widget` 可以通过指定不同的 `PageStorageKey` 来存储各自的数据或状态。
2. 每次滚动结束，可滚动组件都会将滚动位置 `offset` 存储到 `PageStorage` 中，当可滚动组件重新创建时再恢复。
3. 如果 `ScrollController.keepScrollOffset` 为 `false`，则滚动位置将不会被存储，可滚动组件重新创建时会使用 `ScrollController.initialScrollOffset`
4. `ScrollController.keepScrollOffset` 为 `true` 时，可滚动组件在第一次创建时，会滚动到 `initialScrollOffset` 处，因为这时还没有存储过滚动位置。在接下来的滚动中就会存储、恢复滚动位置，而 `initialScrollOffset` 会被忽略。
5. 当一个路由中包含多个可滚动组件时，如果你发现在进行一些跳转或切换操作后，滚动位置不能正确恢复，这时你可以通过显式指定 `PageStorageKey` 来分别跟踪不同的可滚动组件的位置，如：

```dart
ListView(key: PageStorageKey(1), ... );
...
ListView(key: PageStorageKey(2), ... );
```

6. 不同的 `PageStorageKey`，需要不同的值，这样才可以为不同可滚动组件保存其滚动位置
7. 注意：一个路由中包含多个可滚动组件时，如果要分别跟踪它们的滚动位置，并非一定就得给他们分别提供PageStorageKey。这是因为Scrollable本身是一个StatefulWidget，它的状态中也会保存当前滚动位置，所以，只要可滚动组件本身没有被从树上移除（detach），那么其State就不会销毁(dispose)，滚动位置就不会丢失。只有当Widget发生结构变化，导致可滚动组件的State销毁或重新构建时才会丢失状态，这种情况就需要显式指定PageStorageKey，通过PageStorage来存储滚动位置，一个典型的场景是在使用TabBarView时，在Tab发生切换时，Tab页中的可滚动组件的State就会销毁，这时如果想恢复滚动位置就需要指定PageStorageKey。

#### Ⅳ、ScrollPosition

1. `ScrollPosition` 是用来保存可滚动组件的滚动位置的。
2. 一个 `ScrollController` 对象可以同时被多个可滚动组件使用，`ScrollController` 会为每一个可滚动组件创建一个 `ScrollPosition` 对象，这些 `ScrollPosition` 保存在 `ScrollController` 的 `positions` 属性中`List<ScrollPosition>`。
3. `ScrollPosition` 是真正保存滑动位置信息的对象，`offset` 只是一个便捷属性：

```dart
double get offset => position.pixels;
```

4. 一个 `ScrollController` 虽然可以对应多个可滚动组件，但是有一些操作，如读取滚动位置 `offset`，则需要一对一！但是我们仍然可以在一对多的情况下，通过其他方法读取滚动位置，举个例子，假设一个 `ScrollController` 同时被两个可滚动组件使用，那么我们可以通过如下方式分别读取他们的滚动位置：

```dart
...
controller.positions.elementAt(0).pixels
controller.positions.elementAt(1).pixels
...    
```

5. 我们可以通过 `controller.positions.length` 来确定 `controller` 被几个可滚动组件使用
6. `ScrollPosition` 有两个常用方法：`animateTo()` 和 `jumpTo()`，它们是真正来控制跳转滚动位置的方法， `ScrollController` 的这两个同名方法，内部最终都会调用 `ScrollPositio` 的

#### Ⅴ、ScrollController 控制原理

1. 我们来介绍一下 ScrollController 的另外三个方法：

```dart
ScrollPosition createScrollPosition(
    ScrollPhysics physics,
    ScrollContext context,
    ScrollPosition oldPosition);
	void attach(ScrollPosition position) ;
	void detach(ScrollPosition position) ;
)
```

2. 当 `ScrollController` 和可滚动组件关联时，可滚动组件首先会调用 `ScrollController` 的 `createScrollPosition()` 方法创建一个 `ScrollPosition` 来存储滚动位置信息
3. 接着，可滚动组件会调用 `attach()` 方法，将创建的 `ScrollPosition` 添加到 `ScrollController` 的 `positions` 属性中，这一步称为“注册位置”，只有注册后 a`nimateTo()` 和 `jumpTo()` 才可以被调用。
4. 当可滚动组件销毁时，会调用 `ScrollController` 的 `detach()` 方法，将其 `ScrollPosition` 对象从 `ScrollController` 的 `positions` 属性中移除，这一步称为“注销位置”，注销后 `animateTo()` 和 `jumpTo()` 将不能再被调用。
5. 需要注意的是，`ScrollController` 的 `animateTo()` 和 `jumpTo()` 内部会调用所有 `ScrollPosition` 的 `animateTo()` 和  `jumpTo()`，以实现所有和该 `ScrollController` 关联的可滚动组件都滚动到指定的位置

### ②、滚动通知

#### Ⅰ、滚动通知

1. Flutter `Widget` 树中子 `Widget` 可以通过发送通知（`Notification`）与父(包括祖先) `Widget` 通信。
2. 父级组件可以通过 `NotificationListener` 组件来监听自己关注的通知，这种通信方式类似于 Web 开发中浏览器的事件冒泡，我们在 Flutter 中沿用“冒泡”这个术语，关于通知冒泡我们将在后面“事件处理与通知”一章中详细介绍。
3. 可滚动组件在滚动时会发送 `ScrollNotification` 类型的通知，`ScrollBar` 正是通过监听滚动通知来实现的。
4. 通过 `NotificationListener` 监听滚动事件和通过 `ScrollController` 有两个主要的不同：
	1. `NotificationListener` 可以在可滚动组件到 `widget` 树根之间任意位置监听。而 `ScrollController` 只能和具体的可滚动组件关联后才可以。
	2. 收到滚动事件后获得的信息不同；`NotificationListener` 在收到滚动事件时，通知中会携带当前滚动位置和 `ViewPort` 的一些信息，而 `ScrollController` 只能获取当前滚动位置

#### Ⅱ、实例

1. 下面，我们监听 ListView 的滚动通知，然后显示当前列表的参数：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/03_滚动监听及控制/02_滚动通知.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: ScrollNotificationComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class ScrollNotificationComponent extends StatefulWidget {
  const ScrollNotificationComponent({Key? key}) : super(key: key);

  @override
  _ScrollNotificationComponentState createState() => _ScrollNotificationComponentState();
}

class _ScrollNotificationComponentState extends State<ScrollNotificationComponent> {
  // ScrollController 是一个用于控制可滚动组件（如 ListView、GridView、SingleChildScrollView 等）的控制器。
  ScrollController _controller = ScrollController();

  // 刷新次数
  int _num = 0;
  // 数据，用于显示 ListView 列表，初始值为 20 条数据，每次刷新增加 20 条数据
  final List<String> _data = List.generate(20, (index) => "第 0 次刷新、第 ${index + 1} 条数据");
  // 是否显示 返回到顶部 按钮
  bool showToTopBtn = false;
  // 添加一个变量用于保存屏幕的纵向尺寸（纵向像素）
  double screenHeight = 0;
  // 保存当前所在位置（提示刷新次数）
  String _progress = """
    当前滚动位置：
    最大可滚动长度：
    滑出ViewPort顶部的长度：
    ViewPort内部长度：
    列表中未滑入ViewPort部分的长度：
    是否滑到了可滚动组件的边界：
  """.split("\n").map((line) => line.trimLeft()).join('\n');

  @override
  void initState() {
    super.initState();
    // 监听滚动事件，打印滚动位置
    _controller.addListener(() {
      /**
       * 打印滚动位置
       * offset 的值表示可滚动组件内容顶部相对于可滚动区域顶部的偏移量。
       * 初始情况下，offset 的值通常为 0，表示内容顶部与可滚动区域顶部对齐，没有发生滚动。
       * 向下滚动列表时，offset 的值会逐渐增加；向上滚动列表时，offset 的值会逐渐减小
       */
      print("月海：${_controller.offset}");
      // 如果当前列表的偏移量小于屏幕的纵向尺寸，且 返回到顶部 按钮已经显示，则隐藏按钮
      if (_controller.offset < screenHeight && showToTopBtn) {
        setState(() {
          showToTopBtn = false;
        });
        // 如果当前列表的偏移量大于屏幕的纵向尺寸，且 返回到顶部 按钮没有显示，则显示按钮
      } else if (_controller.offset >= screenHeight && !showToTopBtn) {
        setState(() {
          showToTopBtn = true;
        });
      }
    });
  }

  /// dispose 方法是一个生命周期方法，它在 State 对象被永久地从内存中移除之前被调用。
  @override
  void dispose() {
    // 为了避免内存泄露，需要调用 _controller.dispose 释放资源
    _controller.dispose();
    super.dispose();
  }

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // 获取屏幕的尺寸
    Size screenSize = MediaQuery.of(context).size;
    // 获取屏幕的纵向尺寸（纵向像素）
    screenHeight = screenSize.height;

    /**
     * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
     * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
     */
    return Scaffold(
      /**
       * body: 用于定义页面的主要内容区域
       * Stack 是一个小部件，它可以将子部件叠加排列。
       * Stack 允许子部件堆叠，可使用 Positioned 根据 Stack 的四个角来定位子部件。
       */
      body: Stack(
        // children是 Stack 的一个属性，用于设置 Stack 的子部件。
        children: [
          // Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
          Scrollbar(
            // ListView 列表组件
            child: NotificationListener(
              onNotification: (ScrollNotification notification){
                setState(() {
                  _progress = """
                    当前滚动位置：${notification.metrics.pixels}
                    最大可滚动长度：${notification.metrics.maxScrollExtent}
                    滑出ViewPort顶部的长度：${notification.metrics.extentBefore}
                    ViewPort内部长度：${notification.metrics.extentInside}
                    列表中未滑入ViewPort部分的长度：${notification.metrics.extentAfter}
                    是否滑到了可滚动组件的边界：${notification.metrics.atEdge}
                  """.split("\n").map((line) => line.trimLeft()).join('\n');
                });
                return false;
              },
              child: ListView.separated(
                // controller：控制器，用于控制 ListView 的滚动位置
                controller: _controller,
                // itemCount：列表项的数量：_data 的长度
                itemCount: _data.length,
                /**
                 * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
                 * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
                 */
                itemBuilder: (BuildContext context, int index) {
                  // 如果到了末尾
                  if(index == _data.length - 1 - 5){
                    // 刷新次数 + 1
                    _num++;
                    // 获取数据，添加到 _data 中，刷新列表
                    _retrieveData();
                  }
                  return ListTile(title: Text(_data[index]));
                },
                // 分割器构造器
                separatorBuilder: (context, index) => const Divider(color: Colors.red),
              ),
            )
          ),
          /**
           * Align 是相对（父布局）定位
           */
          Align(
            // 居中
            alignment: Alignment.center,
            // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
            child: Container(
              color: Colors.cyan,
              child: Text(_progress),
            ),
          )
        ]
      ),
      /**
       * 悬浮按钮
       * showToTopBtn 为 true 时显示，为 false 时隐藏
       */
      floatingActionButton: !showToTopBtn ? null : FloatingActionButton(
        // child 属性用于设置悬浮按钮的内容，通常是一个 Icon 小部件
        child: const Icon(Icons.arrow_upward),
        // onPressed 点击事件
        onPressed: () {
          /**
           * animateTo 方法可以滚动列表到指定的位置
           * 参数 1：指定滚动的偏移量，0 表示滚动到列表的起始位置
           * 参数 2：滚动动画执行的时间，这里设置为 200 毫秒
           * 参数 3：滚动动画曲线，这里设置为 Curves.ease，表示动画曲线为匀速曲线
           */
          _controller.animateTo(0, duration: const Duration(milliseconds: 200), curve: Curves.ease);
        },
      )
    );
  }

  void _retrieveData(){
    // 等待模拟的网络请求完成
    Future.delayed(const Duration(milliseconds: 5)).then((value) => {
      setState(() {
        _data.addAll(List.generate(20, (index) => "第 $_num 次刷新、第 ${index + 1 + _data.length} 条数据"));
      })
    });
  }

}
```

2. 效果：

![|369](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231108143721.png)

## 5、AnimatedList 动画列表组件

### ①、介绍

1. `AnimatedList` 和 `ListView` 的功能大体相似
2. 不同的是， `AnimatedList` 可以在列表中插入或删除节点时执行一个动画，在需要添加或删除列表项的场景中会提高用户体验。
3. `AnimatedList` 是一个 `StatefulWidget`，它对应的 `State` 类型为 `AnimatedListState`，添加和删除元素的方法位于 `AnimatedListState` 中：

```dart
void insertItem(int index, { Duration duration = _kDuration });

void removeItem(int index, AnimatedListRemovedItemBuilder builder, { Duration duration = _kDuration }) ;
```

### ②、例子

1. 初始的时候有5个列表项，点击 + 号按钮，会添加一个，添加过程执行渐显动画。
2. 点击列表项后面的删除按钮，会删除该项，删除的时候执行一个渐隐 + 收缩的合成动画。

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/04_AnimatedList 动画列表组件/01_AnimatedList 动画列表组件.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: AnimatedListComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class AnimatedListComponent extends StatefulWidget {
  const AnimatedListComponent({Key? key}) : super(key: key);

  @override
  _AnimatedListComponentState createState() => _AnimatedListComponentState();
}

class _AnimatedListComponentState extends State<AnimatedListComponent> {
  // 列表数据源，初始值为 0-4
  final List<int> _data = List.generate(5, (index) => index);
  /// globalKey 是一个 GlobalKey 对象，它是一个全局的唯一标识符，用于在 Flutter 中标识和操作特定的组件或部件状态
  /// 具体来说，globalKey 是一个 GlobalKey<AnimatedListState> 对象，
  /// 它可以通过 currentState 属性来获取 AnimatedList 的当前状态。
  /// 通过 currentState，我们可以调用 AnimatedListState 中定义的方法，比如 insertItem 和 removeItem，来操作列表项并且触发相应的动画效果
  final globalKey = GlobalKey<AnimatedListState>();

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Stack 允许子部件堆叠，可使用 Positioned 根据 Stack 的四个角来定位子部件。
    return Stack(
      children: [
        // AnimatedList 动画列表组件
        buildAnimatedList(),
        // Align 是相对（父布局）定位，alignment: Alignment.center：居中
        Align(alignment: Alignment.center, child: buildAddBtn())
      ],
    );
  }

  /// AnimatedList 动画列表组件
  Widget buildAnimatedList(){
    // Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
    return Scrollbar(
      // AnimatedList 动画列表组件
      child: AnimatedList(
        // 属性 key 的作用是为部件在整个应用程序中提供一个唯一的标识，以便在需要对其进行操作时能够准确定位到该部件
        key: globalKey,
        // initialItemCount：列表项的数量：_data 的长度
        initialItemCount: _data.length,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index, Animation<double> animation) {
          // 添加列表项时会执行渐显动画
          return FadeTransition(
            opacity: animation,
            // 调用 buildItem 方法构建列表项，并将其作为渐变动画的子部件
            child: buildItem(context, index),
          );
        },
      ),
    );
  }

  // 构建列表项
  Widget buildItem(context, index) {
    // ListTile 是一个 Material Design 风格的列表项，它是一个常用的列表项小部件
    return ListTile(
      // 为列表项添加一个 key，用于在删除列表项时定位到该列表项
      key: ValueKey(_data[index]),
      // 设置列表项的标题
      title: Text("第 ${_data[index] + 1} 条数据"),
      // trailing 是 ListTile 的一个属性，用于设置列表项的尾部内容
      trailing: IconButton(
        icon: const Icon(Icons.delete),
        // 点击时删除
        onPressed: () => { onDelete(context, index) },
      ),
    );
  }

  // 创建一个 + 按钮，点击后会向列表中插入一项
  Widget buildAddBtn() {
    // FloatingActionButton 是一个浮动按钮，它通常用于在页面上做一个快捷操作按钮
    return FloatingActionButton(
      child: const Icon(Icons.add),
      onPressed: () {
        // 如果列表为空，则向列表中添加一个 0，否则在最后一个列表项的值上加 1
        if(_data.isEmpty){
          _data.add(0);
        }else{
          _data.add(_data[_data.length - 1] + 1);
        }
        // 告诉列表项有新添加的列表项
        globalKey.currentState!.insertItem(_data.length - 1);
      },
    );
  }

  /// 处理删除列表项的操作
  onDelete(context, index) {
    // 使用 globalKey 获取当前 AnimatedList 的状态，并调用 removeItem 方法来移除列表中的项
    globalKey.currentState?.removeItem(
      // 要移除的列表项的索引
      index,
      // 动画时间为 200 ms
      duration: const Duration(milliseconds: 200),
      // 这是一个回调函数，它接收两个参数，context 表示当前上下文，animation 是用于执行删除动画的动画对象
      (context, animation){
        // 创建要删除的列表项的副本，以便在动画中使用
        var item = buildItem(context, index);
        // 从数据源 _data 中删除指定索引的项
        _data.removeAt(index);
        // 返回一个 FadeTransition，它包裹了一个 SizeTransition，实现了渐隐和收缩列表项的合成动画
        return FadeTransition(
          // 设置渐隐动画的曲线，让透明度变化更快一些
          opacity: CurvedAnimation(
            parent: animation,
            curve: const Interval(0.5, 1.0),
          ),
          // 实现列表项高度的缩小动画
          child: SizeTransition(
            sizeFactor: animation,
            axisAlignment: 0.0,
            child: item,
          ),
        );
      }
    );
  }

}
```

## 6、GridView 网格布局

### ①、默认构造函数

1. GridView可以构建一个二维网格列表，其默认构造函数定义如下：

```dart
GridView({
  Key? key,
  Axis scrollDirection = Axis.vertical,
  bool reverse = false,
  ScrollController? controller,
  bool? primary,
  ScrollPhysics? physics,
  bool shrinkWrap = false,
  EdgeInsetsGeometry? padding,
  /**
   * gridDelegate 参数，类型是 SliverGridDelegate，它的作用是控制 GridView 子组件如何排列(layout)
   * SliverGridDelegate 是一个抽象类，定义了 GridView Layout 相关接口，子类需要通过实现它们来实现具体的布局算法。
   * Flutter 中提供了两个 SliverGridDelegate 的子类
   *    SliverGridDelegateWithFixedCrossAxisCount：实现了一个横轴为固定数量子元素的 layout 算法
   *    SliverGridDelegateWithMaxCrossAxisExtent：实现了一个横轴子元素为固定最大长度的 layout 算法
   */
  required this.gridDelegate,  //下面解释
  bool addAutomaticKeepAlives = true,
  bool addRepaintBoundaries = true,
  double? cacheExtent,
  List<Widget> children = const <Widget>[],
  ...
})
```

2. `GridView` 和 `ListView` 的大多数参数都是相同的，它们的含义也都相同的，在此不再赘述。
3. 唯一需要关注的是 `gridDelegate` 参数，类型是 `SliverGridDelegate`，它的作用是控制 `GridView` 子组件如何排列(layout)。

### ②、SliverGridDelegateWithFixedCrossAxisCount

1. 该子类实现了一个横轴为固定数量子元素的layout算法，其构造函数为：

```dart
SliverGridDelegateWithFixedCrossAxisCount({
  /**
   * crossAxisCount：横轴子元素的数量。
   * 此属性值确定后子元素在横轴的长度就确定了，即 ViewPort 横轴长度除以 crossAxisCount 的商
   */
  @required double crossAxisCount,
  /**
   * mainAxisSpacing：主轴方向的间距。
   */
  double mainAxisSpacing = 0.0,
  /**
   * crossAxisSpacing：横轴方向子元素的间距。
   */
  double crossAxisSpacing = 0.0,
  /**
   * childAspectRatio：子元素在横轴长度和主轴长度的比例。
   * 由于 crossAxisCount 指定后，子元素横轴长度就确定了，然后通过此参数值就可以确定子元素在主轴的长度。
   */
  double childAspectRatio = 1.0,
})
```

2. 可以发现，子元素的大小是通过 `crossAxisCount` 和 `childAspectRatio` 两个参数共同决定的。
3. 注意，这里的子元素指的是子组件的最大显示空间，注意确保子组件的实际大小不要超出子元素的空间
4. 示例：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/05_GridView 网格布局/01_SliverGridDelegateWithFixedCrossAxis.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: SliverGridDelegateWithFixedCrossAxisCountComponent(),
      )
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class SliverGridDelegateWithFixedCrossAxisCountComponent extends StatelessWidget {
  const SliverGridDelegateWithFixedCrossAxisCountComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // GridView 是一个常用的网格列表小部件，它可以沿着两个方向排列子元素，类似于网格布局。
    return GridView(
      // SliverGridDelegateWithFixedCrossAxisCount 是 GridView 的一个构造方法，用于创建一个横轴固定数量子元素的网格列表。
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        // 横轴三个子 widget
        crossAxisCount: 3,
        // 宽高比为 1 时，子 widget 的宽度和高度相等；即子 widget 为正方形
        childAspectRatio: 1.0
      ),
      // 子 widget 列表
      children: const [
        Icon(Icons.ac_unit),
        Icon(Icons.airport_shuttle),
        Icon(Icons.all_inclusive),
        Icon(Icons.beach_access),
        Icon(Icons.cake),
        Icon(Icons.free_breakfast)
      ]
    );
  }
}
```
5. 效果：

![|363](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231113150724.png)

### ③、SliverGridDelegateWithMaxCrossAxisExtent

1. 该子类实现了一个横轴子元素为固定最大长度的 layout 算法，其构造函数为：

```dart
SliverGridDelegateWithMaxCrossAxisExtent({
  /**
   * maxCrossAxisExtent 为子元素在横轴上的最大长度，
   * 之所以是“最大”长度，是因为横轴方向每个子元素的长度仍然是等分的，
   * 举个例子，如果 ViewPort 的横轴长度是 450，那么当 maxCrossAxisExtent 的值在区间 [450/4，450/3) 内的话，
   * 子元素最终实际长度都为112.5，而 childAspectRatio 所指的子元素横轴和主轴的长度比为最终的长度比
   */
  double maxCrossAxisExtent,
  /**
   * mainAxisSpacing：主轴方向的间距。
   */
  double mainAxisSpacing = 0.0,
  /**
   * crossAxisSpacing：横轴方向子元素的间距。
   */
  double crossAxisSpacing = 0.0,
  /**
   * childAspectRatio：子元素在横轴长度和主轴长度的比例。
   * 由于 crossAxisCount 指定后，子元素横轴长度就确定了，然后通过此参数值就可以确定子元素在主轴的长度。
   */
  double childAspectRatio = 1.0,
})
```

2. 示例

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/05_GridView 网格布局/01_SliverGridDelegateWithFixedCrossAxis.dart';
import '04_可滚动组件/05_GridView 网格布局/02_SliverGridDelegateWithMaxCrossAxisExtent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: SliverGridDelegateWithMaxCrossAxisExtentComponent(),
      )
    );
  }
}
```

```dart
// 引入 Flutter 的 material 包，包含 Flutter 应用程序的核心功能。
import 'package:flutter/material.dart';

class SliverGridDelegateWithMaxCrossAxisExtentComponent extends StatelessWidget {
  const SliverGridDelegateWithMaxCrossAxisExtentComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // GridView 是一个常用的网格列表小部件，它可以沿着两个方向排列子元素，类似于网格布局。
    return GridView(
      // SliverGridDelegateWithFixedCrossAxisCount 是 GridView 的一个构造方法，用于创建一个横轴固定数量子元素的网格列表。
      gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
        // maxCrossAxisExtent 是一个横轴子元素的最大长度，
        maxCrossAxisExtent: 120.0,
        // 宽高比为 2 时，子 widget 的宽度是高度的两倍
        childAspectRatio: 2.0
      ),
      // 子 widget 列表
      children: const [
        Icon(Icons.ac_unit),
        Icon(Icons.airport_shuttle),
        Icon(Icons.all_inclusive),
        Icon(Icons.beach_access),
        Icon(Icons.cake),
        Icon(Icons.free_breakfast)
      ]
    );
  }
}
```

3. 效果

![|363](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231113152404.png)

### ④、GridView.count

1. `GridView.count` 构造函数内部使用了 `SliverGridDelegateWithFixedCrossAxisCount`，我们通过它可以快速的创建横轴固定数量子元素的 `GridView`，我们可以通过以下代码实现和上面例子相同的效果等：

```dart
GridView.count( 
  crossAxisCount: 3,
  childAspectRatio: 1.0,
  children: <Widget>[
    Icon(Icons.ac_unit),
    Icon(Icons.airport_shuttle),
    Icon(Icons.all_inclusive),
    Icon(Icons.beach_access),
    Icon(Icons.cake),
    Icon(Icons.free_breakfast),
  ],
);
```

### ⑤、GridView.extent

1. `GridView.extent` `构造函数内部使用了SliverGridDelegateWithMaxCrossAxisExtent`，我们通过它可以快速的创建横轴子元素为固定最大长度的 `GridView`，上面的示例代码等价于：

```dart
GridView.extent(
   maxCrossAxisExtent: 120.0,
   childAspectRatio: 2.0,
   children: <Widget>[
     Icon(Icons.ac_unit),
     Icon(Icons.airport_shuttle),
     Icon(Icons.all_inclusive),
     Icon(Icons.beach_access),
     Icon(Icons.cake),
     Icon(Icons.free_breakfast),
   ],
 );
```

### ⑥、GridView.builder

1. 上面我们介绍的 `GridView` 都需要一个 `widget` 数组作为其子元素，这些方式都会提前将所有子 `widget` 都构建好，所以只适用于子 `widget` 数量比较少时
2. 当子 `widget` 比较多时，我们可以通过 `GridView.builder` 来动态创建子 `widget`。
3. `GridView.builder` 必须指定的参数有两个：

```dart
GridView.builder(
 ...
 required SliverGridDelegate gridDelegate, 
 required IndexedWidgetBuilder itemBuilder,
)
```

4. 其中 `itemBuilder` 为子 `widget` 构建器
5. 假设我们需要从一个异步数据源（如网络）分批获取一些 `Icon`，然后用 `GridView` 来展示：


```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/05_GridView 网格布局/01_SliverGridDelegateWithFixedCrossAxis.dart';
import '04_可滚动组件/05_GridView 网格布局/02_SliverGridDelegateWithMaxCrossAxisExtent.dart';
import '04_可滚动组件/05_GridView 网格布局/03_GridViewBuilder.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: GridViewBuilderComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class GridViewBuilderComponent extends StatefulWidget {
  const GridViewBuilderComponent({Key? key}) : super(key: key);

  @override
  _GridViewBuilderComponentState createState() => _GridViewBuilderComponentState();
}

class _GridViewBuilderComponentState extends State<GridViewBuilderComponent> {
  // 数据
  final List<IconData> _data = [];

  // initState 方法是 StatefulWidget 的一个方法，当 StatefulWidget 第一次插入到 Widget 树时会被调用
  @override
  void initState() {
    super.initState();
    // 初始化数据
    _retrieveData();
  }

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
    return Scrollbar(
      // GridView.builder 是 GridView 的一个构造方法，用于创建一个横轴固定数量子元素的网格列表。
      child: GridView.builder(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          // 每行三列
          crossAxisCount: 3,
          // 宽高比为 1 时，子 widget 的宽度和高度相等；即子 widget 为正方形
          childAspectRatio: 1.0,
        ),
        // itemCount：列表项的数量：_data 的长度
        itemCount: _data.length,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index) {
          // 如果到了末尾
          if(index == _data.length - 1){
            // 获取数据，添加到 _data 中，刷新列表
            _retrieveData();
          }
          return Icon(_data[index]);
        },
      )
    );
  }

  void _retrieveData(){
    // 等待模拟的网络请求完成
    Future.delayed(const Duration(milliseconds: 5)).then((value) => {
      setState(() {
        _data.addAll([
          Icons.ac_unit,
          Icons.airport_shuttle,
          Icons.all_inclusive,
          Icons.beach_access,
          Icons.cake,
          Icons.free_breakfast,
        ]);
      })
    });
  }

}
```

6. 效果：

![|363](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231113160015.png)

## 7、PageView 与页面缓存

### ①、PageView 构造函数

1. 如果要实现页面切换和 `Tab` 布局，我们可以使用 `PageView` 组件。
2. 需要注意，`PageView` 是一个非常重要的组件，因为在移动端开发中很常用，比如大多数 App 都包含 Tab 换页效果、图片轮动以及抖音上下滑页切换视频功能等等，这些都可以通过 `PageView` 轻松实现。

```dart
PageView({
  Key? key,
  this.scrollDirection = Axis.horizontal, // 滑动方向
  this.reverse = false,
  PageController? controller,
  this.physics,
  List<Widget> children = const <Widget>[],
  this.onPageChanged,
  
  // 每次滑动是否强制切换整个页面，如果为false，则会根据实际的滑动距离显示页面
  this.pageSnapping = true,
  // 主要是配合辅助功能用的，后面解释
  this.allowImplicitScrolling = false,
  // 后面解释
  this.padEnds = true,
})
```

### ②、示例

1. 示例

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/06_PageView 与页面缓存/01_Page.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: PageView(
          children: const [
            PageComponent(text: "Page 1"),
            PageComponent(text: "Page 2"),
            PageComponent(text: "Page 3"),
            PageComponent(text: "Page 4"),
            PageComponent(text: "Page 5"),
            PageComponent(text: "Page 6"),
          ],
        ),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class PageComponent extends StatefulWidget {
  const PageComponent({Key? key, required this.text}) : super(key: key);

  final String text;

  @override
  _PageComponentState createState() => _PageComponentState();
}

class _PageComponentState extends State<PageComponent> {

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
	// 页面构建时打印数据
	print("build ${widget.text}");
    // Center 是一个小部件，用于将其子部件居中显示在屏幕上
    return Center(child: Text("${widget.text}", textScaleFactor: 5));
  }
  
}
```

2. 效果

![|362](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画.gif)

### ③、页面缓存

1. 我们在运行上面示例时，每当页面切换时都会触发新 `Page` 页的 `build`，比如我们从第一页滑到第二页，然后再滑回第一页时，控制台打印如下：

```dart
flutter: build 0
flutter: build 1
flutter: build 0
```

2. 可见 `PageView` 默认并没有缓存功能，一旦页面滑出屏幕它就会被销毁，这和我们前面讲过的 `ListView/GridView` 不一样，在创建 `ListView/GridView` 时我们可以手动指定 `ViewPort` 之外多大范围内的组件需要预渲染和缓存（通过 `cacheExtent` 指定），只有当组件滑出屏幕后又滑出预渲染区域，组件才会被销毁，但是不幸的是 `PageView`  并没有 `cacheExtent` 参数！
3. 但是在真实的业务场景中，对页面进行缓存是很常见的一个需求，比如一个新闻 App，下面有很多频道页，如果不支持页面缓存，则一旦滑到新的频道旧的频道页就会销毁，滑回去时又得重新请求数据和构建页面，这谁扛得住！
4. 按道理 `cacheExtent` 是 `Viewport` 的一个配置属性，且 `PageView` 也是要构建 `Viewport` 的，那么为什么就不能透传一下这个参数呢？于是看了一下 PageView 的源码，发现在 PageView 创建Viewport 的代码中是这样的：

```dart
child: Scrollable(
  ...
  viewportBuilder: (BuildContext context, ViewportOffset position) {
    return Viewport(
      // TODO(dnfield): we should provide a way to set cacheExtent
      // independent of implicit scrolling:
      // https://github.com/flutter/flutter/issues/45632
      cacheExtent: widget.allowImplicitScrolling ? 1.0 : 0.0,
      cacheExtentStyle: CacheExtentStyle.viewport,
      ...
    );
  },
)
```

5. 我们发现，虽然 `PageView` 没有透传 `cacheExtent`，但是却在 `allowImplicitScrolling` 为 `true` 时设置了预渲染区域；
6. 注意，此时的缓存类型为 `CacheExtentStyle.viewport`，则 `cacheExtent` 则表示缓存的长度是几个 `Viewport` 的宽度，`cacheExtent` 为 `1.0`，则代表前后各缓存一个页面宽度，即前后各一页。既然如此，那我们将 `PageView` 的 `allowImplicitScrolling` 置为 `true` 则不就可以缓存前后两页了？我们修改代码，然后运行示例，此时就可以缓存上下各一页了；
7. 能缓存前后各一页也貌似比不能缓存好一点，但还是不能彻底解决不了我们的问题。为什么明明就是顺手的事， flutter 就不让开发者指定缓存策略呢？然后我们翻译一下源码中的注释：

>    Todo：我们应该提供一种独立于隐式滚动（implicit scrolling）的设置 cacheExtent 的机制。

8. 放开 cacheExtent 透传是很简单的事情，为什么还要以后再做？是有什么难题么？要理解这个我们就需要看看 `allowImplicitScrolling` 到底是什么了，根据文档以及注释中 issue 的链接，发现 PageView 中设置  `cacheExtent` 会和 iOS 中 辅助功能有冲突（读者可以先不用关注），所以暂时还没有什么好的办法。
9. 看到这可能国内的很多开发者要说我们的 App 不用考虑辅助功能，既然如此，那问题很好解决，将 PageView 的源码拷贝一份，然后透传 cacheExtent 即可。
10. 拷源码的方式虽然很简单，但毕竟不是正统做法，那有没有更通用的方法吗？有！还记得我们在本章第一节中说过“可滚动组件提供了一种通用的缓存子项的解决方案” 吗，我们将在下一节重点介绍

## 8、AutomaticKeepAlive 可滚动组件子项缓存

### ①、简介

1. 本节将介绍可滚动组件中缓存指定子项的通用方案。
2. 在介绍 `ListView` 时，有一个 `addAutomaticKeepAlives` 属性我们并没有介绍，如果 `addAutomaticKeepAlives` 为 `true`，则 `ListView` 会为每一个列表项添加一个 `AutomaticKeepAlive` 父组件。
3. 虽然 `PageView` 的默认构造函数和 `PageView.builder` 构造函数中没有该参数，但它们最终都会生成一个 `SliverChildDelegate` 来负责列表项的按需加载，而在 `SliverChildDelegate` 中每当列表项构建完成后，`SliverChildDelegate` 都会为其添加一个 `AutomaticKeepAlive` 父组件。
4. `AutomaticKeepAlive` 的组件的主要作用是将列表项的根 `RenderObject` 的 `keepAlive` 按需自动标记 为 `true` 或 `false`。为了方便叙述，我们可以认为根 `RenderObject` 对应的组件就是列表项的根 `Widget`，代表整个列表项组件，同时我们将列表组件的 `Viewport 区域 + cacheExtent（预渲染区域）` 称为加载区域 ：
	1. 当 `keepAlive` 标记为 `false` 时，如果列表项滑出加载区域时，列表组件将会被销毁。
	2. 当 `keepAlive` 标记为 `true` 时，当列表项滑出加载区域后，`Viewport` 会将列表组件缓存起来；当列表项进入加载区域时，`Viewport` 从先从缓存中查找是否已经缓存，如果有则直接复用，如果没有则重新创建列表项。
5. 那么 `AutomaticKeepAlive` 什么时候会将列表项的 `keepAlive` 标记为 `true` 或 `false` 呢？答案是开发者说了算！
6. Flutter 中实现了一套类似 `C/S` 的机制，`AutomaticKeepAlive` 就类似一个 `Server`，它的子组件可以是 `Client`，这样子组件想改变是否需要缓存的状态时就向 `AutomaticKeepAlive` 发一个通知消息`（KeepAliveNotification）`，`AutomaticKeepAlive` 收到消息后会去更改 `keepAlive` 的状态，如果有必要同时做一些资源清理的工作（比如 `keepAlive` 从 `true` 变为 `false` 时，要释放缓存）。
7. 我们基于上一节 `PageView` 示例，实现页面缓存，根据上面的描述实现思路就很简单了：让 `Page` 页变成一个 `AutomaticKeepAlive Client` 即可。为了便于开发者实现，Flutter 提供了一个 `AutomaticKeepAliveClientMixin` ，我们只需要让 `PageState` 混入这个 mixin，且同时添加一些必要操作即可

### ②、实例

1. 让 `PageState` 混入 `AutomaticKeepAliveClientMixin`，在 `build` 中调用父类的 `build` 方法，并指定是否需要缓存

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/07_可滚动组件子项缓存/01_AutomaticKeepAlive.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: PageView(
          children: const [
            AutomaticKeepAliveComponent(text: "Page 1"),
            AutomaticKeepAliveComponent(text: "Page 2"),
            AutomaticKeepAliveComponent(text: "Page 3"),
            AutomaticKeepAliveComponent(text: "Page 4"),
            AutomaticKeepAliveComponent(text: "Page 5"),
            AutomaticKeepAliveComponent(text: "Page 6"),
          ],
        ),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class AutomaticKeepAliveComponent extends StatefulWidget {
  const AutomaticKeepAliveComponent({Key? key, required this.text}) : super(key: key);

  final String text;

  @override
  _AutomaticKeepAliveComponentState createState() => _AutomaticKeepAliveComponentState();
}

// 混入 AutomaticKeepAliveClientMixin，这是保持状态的关键
class _AutomaticKeepAliveComponentState extends State<AutomaticKeepAliveComponent> with AutomaticKeepAliveClientMixin {

  // wantKeepAlive 为 true 表示使用 AutomaticKeepAliveClientMixin 保持状态
  @override
  // 是否需要缓存，如果为 false，则不缓存，每次都会重新构建
  bool get wantKeepAlive => true;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // 必须调用父类的 build 方法
    super.build(context);
    // 页面构建时打印数据
    print("build ${widget.text}");
    // Center 是一个小部件，用于将其子部件居中显示在屏幕上
    return Center(child: Text("${widget.text}", textScaleFactor: 5));
  }

}
```

2. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画%201.gif)

3. 代码很简单，我们只需要提供一个 `wantKeepAlive`，它会表示 `AutomaticKeepAlive` 是否需要缓存当前列表项；另外我们必须在 `build` 方法中调用一下 `super.build(context)`，该方法实现在 `AutomaticKeepAliveClientMixin` 中，功能就是根据当前 `wantKeepAlive` 的值给 `AutomaticKeepAlive` 发送消息，`AutomaticKeepAlive` 收到消息后就会开始工作，如图所示：

![|600](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231114101153.png)

4. 需要注意，如果我们采用 `PageView.custom` 构建页面时没有给列表项包装 `AutomaticKeepAlive` 父组件，则上述方案不能正常工作，因为此时 `Client` 发出消息后，找不到 `Server`，404 了

## 9、TabBarView 标签栏

### ①、TabBarView

1. `TabBarView` 封装了 `PageView`，它的构造方法很简单

```dart
TabBarView({
  Key? key,
  required this.children, // tab 页
  this.controller, // TabController
  this.physics,
  this.dragStartBehavior = DragStartBehavior.start,
}) 
```

2. `TabController` 用于监听和控制 `TabBarView` 的页面切换，通常和 `TabBar` 联动。
3. 如果没有指定，则会在组件树中向上查找并使用最近的一个 `DefaultTabController` 。

### ②、TabBar

1. `TabBar` 为 `TabBarView` 的导航标题，如图所示：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231114102651.png)

2. `TabBar` 有很多配置参数，通过这些参数我们可以定义 `TabBar` 的样式，很多属性都是在配置 `indicator` 和 `label`，拿上图来举例，`Label` `是每个Tab` 的文本，`indicator` 指 “历史” 下面的白色下划线。

```dart
const TabBar({
  Key? key,
  required this.tabs, // 具体的 Tabs，需要我们创建
  this.controller,
  this.isScrollable = false, // 是否可以滑动
  this.padding,
  this.indicatorColor,// 指示器颜色，默认是高度为2的一条下划线
  this.automaticIndicatorColorAdjustment = true,
  this.indicatorWeight = 2.0,// 指示器高度
  this.indicatorPadding = EdgeInsets.zero, //指示器padding
  this.indicator, // 指示器
  this.indicatorSize, // 指示器长度，有两个可选值，一个tab的长度，一个是label长度
  this.labelColor, 
  this.labelStyle,
  this.labelPadding,
  this.unselectedLabelColor,
  this.unselectedLabelStyle,
  this.mouseCursor,
  this.onTap,
  ...
}) 
```

3. `TabBar` 通常位于 `AppBar` 的底部，它也可以接收一个 `TabController` ，如果需要和 `TabBarView` 联动， `TabBar` 和 `TabBarView` 使用同一个 `TabController` 即可
4. 注意，联动时 `TabBar` 和 `TabBarView` 的孩子数量需要一致。
5. 如果没有指定 `controller`，则会在组件树中向上查找并使用最近的一个 `DefaultTabController` 。
6. 另外我们需要创建需要的 `tab` 并通过 `tabs` 传给 `TabBar`， `tab` 可以是任何 `Widget`，不过 `Material` 组件库中已经实现了一个 `Tab` 组件，我们一般都会直接使用它：

```dart
const Tab({
  Key? key,
  this.text, //文本
  this.icon, // 图标
  this.iconMargin = const EdgeInsets.only(bottom: 10.0),
  this.height,
  this.child, // 自定义 widget
})
```

7. 注意，`text` 和 `child` 是互斥的，不能同时制定。

### ③、实例

1. 实例

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/08_TabBarView 标签栏/01_TabBarView.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: TabBarViewComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

import '../07_可滚动组件子项缓存/01_AutomaticKeepAlive.dart';

class TabBarViewComponent extends StatefulWidget {
  const TabBarViewComponent({Key? key}) : super(key: key);

  @override
  _TabBarViewComponentState createState() => _TabBarViewComponentState();
}

// 混入 AutomaticKeepAliveClientMixin，这是保持状态的关键
class _TabBarViewComponentState extends State<TabBarViewComponent> with SingleTickerProviderStateMixin {
  // late 关键字，表示这个变量会延迟初始化
  late TabController _tabController;
  List tabs = ["新闻", "历史", "图片"];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: tabs.length, vsync: this);
  }

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * Scaffold 是一个用于创建基本页面布局的小部件。
     * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
     * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
     */
    return Scaffold(
      // appBar 属性用于设置应用程序顶部的导航栏。
      appBar: AppBar(
        /**
         * toolbarHeight 属性用于设置 AppBar 的高度, 默认高度为 kToolbarHeight = 56.0
         * 如果设置为 0，则 AppBar 的高度将会变为 0，即不再给 title 留出空间
         */
        toolbarHeight: 0,
        /**
         * bottom 属性用于设置 AppBar 的底部区域，通常用于设置 TabBar
         * TabBar 是一个 Material Design 样式的选项卡，通常放置在 AppBar 的底部
         */
        bottom: TabBar(
          controller: _tabController,
          tabs: tabs.map((e) => Tab(text: e)).toList(),
        ),
      ),
      /**
       * body: 用于定义页面的主要内容区域
       * TabBarView 是一个用于在 TabBar 和 TabBarView 之间同步切换的小部件。
       */
      body: TabBarView(
        controller: _tabController,
        children: tabs.map((e) {
          // 创建一个 TabBarView，它包含了三个 Tab 页
          return AutomaticKeepAliveComponent(text: e,);
        }).toList(),
      ),
    );
  }
  
  @override
  void dispose() {
    // 释放资源
    _tabController.dispose();
    super.dispose();
  }

}
```

2. 效果

![|415](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画1.gif)

### ④、使用默认控制器

1. 上面的例子中，滑动页面时顶部的 Tab 也会跟着动，点击顶部 Tab 时页面也会跟着切换。
2. 为了实现 `TabBar` 和 `TabBarView` 的联动，我们显式创建了一个 `TabController`，由于 `TabController` 又需要一个 `TickerProvider` （vsync 参数）， 我们又混入了 `SingleTickerProviderStateMixin`；
3. 由于 `TabController` 中会执行动画，持有一些资源，所以我们在页面销毁时必须得释放资源（dispose）。
4. 综上，我们发现创建 `TabController` 的过程还是比较复杂，实战中，如果需要 TabBar 和 TabBarView 联动，通常会创建一个 `DefaultTabController` 作为它们共同的父级组件，这样它们在执行时就会从组件树向上查找，都会使用我们指定的这个 `DefaultTabController`。
5. 我们修改后的实现如下：

```dart
import 'package:flutter/material.dart';

import '../07_可滚动组件子项缓存/01_AutomaticKeepAlive.dart';

class TabBarViewComponent extends StatefulWidget {
  const TabBarViewComponent({Key? key}) : super(key: key);

  @override
  _TabBarViewComponentState createState() => _TabBarViewComponentState();
}

class _TabBarViewComponentState extends State<TabBarViewComponent>{
  List tabs = ["新闻", "历史", "图片"];

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * DefaultTabController 是默认的 TabController 实现，它接受一个 length 参数来指定 TabBar 中 Tab 页的个数，
     * 然后通过 Scaffold.of(context) 来获取父级最近的 Scaffold 组件，然后再调用 ScaffoldState 的方法来设置底部的 TabBar。
     */
    return DefaultTabController(
      // 设置 TabBar 中 Tab 页的个数
      length: tabs.length,
      /**
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      child: Scaffold(
        // appBar 属性用于设置应用程序顶部的导航栏。
        appBar: AppBar(
          /**
           * toolbarHeight 属性用于设置 AppBar 的高度, 默认高度为 kToolbarHeight = 56.0
           * 如果设置为 0，则 AppBar 的高度将会变为 0，即不再给 title 留出空间
           */
          toolbarHeight: 0,
          /**
           * bottom 属性用于设置 AppBar 的底部区域，通常用于设置 TabBar
           * TabBar 是一个 Material Design 样式的选项卡，通常放置在 AppBar 的底部
           */
          bottom: TabBar(
            tabs: tabs.map((e) => Tab(text: e)).toList(),
          ),
        ),
        /**
         * body: 用于定义页面的主要内容区域
         * TabBarView 是一个用于在 TabBar 和 TabBarView 之间同步切换的小部件。
         */
        body: TabBarView(
          children: tabs.map((e) {
            // 创建一个 TabBarView，它包含了三个 Tab 页
            return AutomaticKeepAliveComponent(text: e,);
          }).toList(),
        ),
      )
    );
  }

}
```

6. 可以看到我们无需去手动管理 `Controller` 的生命周期，也不需要提供 `SingleTickerProviderStateMixin`，同时也没有其他的状态需要管理，也就不需要用 `StatefulWidget` 了，这样简单很多。

## 10、CustomScrollView 和 Slivers

### ①、CustomScrollView

1. 前面介绍的 `ListView`、`GridView`、`PageView` 都是一个完整的可滚动组件，所谓完整是指它们都包括 `Scrollable` 、 `Viewport` 和 `Sliver`。
2. 假如我们想要在一个页面中，同时包含多个可滚动组件，且使它们的滑动效果能统一起来，比如：我们想将已有的两个沿垂直方向滚动的 `ListView` 拼接成一个 `ListView` ，这样在第一个 `ListView` 滑动到底部时能自动接上第二 `ListView`，如果尝试写一个 demo：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/09_CustomScrollView 和 Slivers/01_CustomScrollView_1.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: CustomScrollView1Component(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class CustomScrollView1Component extends StatefulWidget {
  const CustomScrollView1Component({Key? key}) : super(key: key);

  @override
  _CustomScrollView1ComponentState createState() => _CustomScrollView1ComponentState();
}

class _CustomScrollView1ComponentState extends State<CustomScrollView1Component>{

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // 创建 ListView，其中包含 20 个 ListTile，用于显示列表项
    var listView = ListView.builder(
      itemCount: 20,
      itemBuilder: (_, index) => ListTile(title: Text('$index')),
    );

    // Column 是一个将子 Widget 垂直排列的小部件，它的高度默认为子 Widget 的高度之和
    return Column(
      children: [
        // Expanded 是一个可以用来包裹子 Widget 的小部件，它会将子 Widget 沿着父部件的垂直方向拉伸并填充满父部件
        Expanded(child: listView),
        // Divider 是一个分割线小部件，它可以在任何两个 Widget 之间添加一个分割线
        const Divider(color: Colors.grey),
        Expanded(child: listView),
      ],
    );
  }

}
```

3. 运行效果如图所示：

![|415](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画2.gif)

4. 页面中有两个 `ListView`，各占可视区域一半高度，虽然能够显式出来，但每一个 `ListView` 只会响应自己可视区域中滑动，实现不了我们想要的效果。
5. 之所以会这样的原因是两个 `ListView` 都有自己独立的 `Scrollable` 、 `Viewport` 和 `Sliver`，既然如此，我们自己创建一个共用的 `Scrollable` 和 `Viewport` 对象，然后再将两个 `ListView` 对应的 `Sliver` 添加到这个共用的 `Viewport` 对象中就可以实现我们想要的效果了。
6. 如果这个工作让开发者自己来做无疑是比较麻烦的，因此 Flutter 提供了一个 `CustomScrollView` 组件来帮助我们创建一个公共的 `Scrollable` 和 `Viewport` ，然后它的 `slivers` 参数接受一个 `Sliver` 数组，这样我们就可以使用 `CustomScrollView` 方面的实现我们期望的功能了：

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/09_CustomScrollView 和 Slivers/02_CustomScrollView_2.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: CustomScrollView2Component(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class CustomScrollView2Component extends StatefulWidget {
  const CustomScrollView2Component({Key? key}) : super(key: key);

  @override
  _CustomScrollView2ComponentState createState() => _CustomScrollView2ComponentState();
}

class _CustomScrollView2ComponentState extends State<CustomScrollView2Component>{

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * SliverFixedExtentList 是一个 Sliver，它可以生成高度相同的列表项。
     * 再次提醒，如果列表项高度相同，我们应该优先使用SliverFixedExtentList 和 SliverPrototypeExtentList，
     * 如果不同，使用 SliverList.
     */
    var listView1 = SliverFixedExtentList(
      // 列表项高度固定
      itemExtent: 56,
      delegate: SliverChildBuilderDelegate(
        (_, index) => ListTile(title: Text('第一个列表 $index')),
        childCount: 20,
      ),
    );

    var listView2 = SliverFixedExtentList(
      // 列表项高度固定
      itemExtent: 56,
      delegate: SliverChildBuilderDelegate(
            (_, index) => ListTile(title: Text('第二个列表 ${index + 20}')),
        childCount: 20,
      ),
    );

    // CustomScrollView 是一个可以自定义滚动模型的组件，它可以包含多种滚动模型。
    return CustomScrollView(
      // slivers 是 CustomScrollView 的一个参数，它接受一个 SliverList 集合。
      slivers: [
        listView1,
        // 插入一个分割线
        SliverToBoxAdapter(
          child: Container(
            height: 1.0,
            color: Colors.grey,
          ),
        ),
        listView2,
      ],
    );
  }

}
```

7. 效果：

![|415](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画3.gif)

8. 综上，`CustomScrollView` 的主要功能是提供一个公共的 `Scrollable` 和 `Viewport`，来组合多个 `Sliver`，`CustomScrollView` 的结构如图所示：

![|600](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231114145921.png)

### ②、Flutter 中常用的 Sliver

1. 之前小节介绍过的可滚动组件都有对应的 `Sliver`：

| Sliver名称                | 功能                               | 对应的可滚动组件               |
| ------------------------- | ---------------------------------- | ------------------------------ |
| SliverList                | 列表                               | ListView                       |
| SliverFixedExtentList     | 高度固定的列表                     | ListView，指定itemExtent时     |
| SliverAnimatedList        | 添加/删除列表项可以执行动画        | AnimatedList                   |
| SliverGrid                | 网格                               | GridView                       |
| SliverPrototypeExtentList | 根据原型生成高度固定的列表         | ListView，指定prototypeItem 时 |
| SliverFillViewport        | 包含多个子组件，每个都可以填满屏幕 | PageView                       |

2. 除了和列表对应的 `Sliver` 之外还有一些用于对 `Sliver` 进行布局、装饰的组件，它们的子组件必须是 `Sliver`，我们列举几个常用的：

| Sliver名称                      | 对应 RenderBox      |
| ------------------------------- | ------------------- |
| SliverPadding                   | Padding             |
| SliverVisibility、SliverOpacity | Visibility、Opacity |
| SliverFadeTransition            | FadeTransition      |
| SliverLayoutBuilder             | LayoutBuilder       |

3. 还有一些其他常用的 `Sliver`：

| Sliver名称             | 说明                                                   |
| ---------------------- | ------------------------------------------------------ |
| SliverAppBar           | 对应 AppBar，主要是为了在 CustomScrollView 中使用。    |
| SliverToBoxAdapter     | 一个适配器，可以将 RenderBox 适配为 Sliver，后面介绍。 |
| SliverPersistentHeader | 滑动到顶部时可以固定住，后面介绍。                     |

4. `Sliver` 系列 `Widget` 比较多，我们不会一一介绍，只需记住它的特点，需要时再去查看文档即可。
5. 上面之所以说“大多数”Sliver都和可滚动组件对应，是由于还有一些如 `SliverPadding`、`SliverAppBar` 等是和可滚动组件无关的，它们主要是为了结合 `CustomScrollView` 一起使用，这是因为 `CustomScrollView` 的子组件必须都是 `Sliver`

### ③、Flutter 中常用的 Sliver 示例

1. 代码分为三部分：
2. 头部 `SliverAppBar`：`SliverAppBar` 对应 `AppBar`，两者不同之处在于 `SliverAppBar` 可以集成到 `CustomScrollView`。`SliverAppBar` 可以结合 `FlexibleSpaceBar` 实现 `Material Design` 中头部伸缩的模型，具体效果，可以运行该示例查看。
3. 中间的 `SliverGrid`：它用 `SliverPadding` 包裹以给 `SliverGrid` 添加补白。`SliverGrid` 是一个两列，宽高比为 4 的网格，它有 20 个子组件。
4. 底部 `SliverFixedExtentList`：它是一个所有子元素高度都为 50 像素的列表。

```dart
// 因为本路由没有使用 Scaffold，为了让子级Widget(如Text)使用
// Material Design 默认的样式风格,我们使用 Material 作为本路由的根。
Material(
  child: CustomScrollView(
    slivers: <Widget>[
      // AppBar，包含一个导航栏.
      SliverAppBar(
        pinned: true, // 滑动到顶端时会固定住
        expandedHeight: 250.0,
        flexibleSpace: FlexibleSpaceBar(
          title: const Text('Demo'),
          background: Image.asset(
            "./imgs/sea.png",
            fit: BoxFit.cover,
          ),
        ),
      ),
      SliverPadding(
        padding: const EdgeInsets.all(8.0),
        sliver: SliverGrid(
          //Grid
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2, //Grid按两列显示
            mainAxisSpacing: 10.0,
            crossAxisSpacing: 10.0,
            childAspectRatio: 4.0,
          ),
          delegate: SliverChildBuilderDelegate(
            (BuildContext context, int index) {
              //创建子widget
              return Container(
                alignment: Alignment.center,
                color: Colors.cyan[100 * (index % 9)],
                child: Text('grid item $index'),
              );
            },
            childCount: 20,
          ),
        ),
      ),
      SliverFixedExtentList(
        itemExtent: 50.0,
        delegate: SliverChildBuilderDelegate(
          (BuildContext context, int index) {
            //创建列表项
            return Container(
              alignment: Alignment.center,
              color: Colors.lightBlue[100 * (index % 9)],
              child: Text('list item $index'),
            );
          },
          childCount: 20,
        ),
      ),
    ],
  ),
);
```

5. 运行效果如图所示：

![|320](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231114150955.png)

![|320](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231114151004.png)

### ④、SliverToBoxAdapter

1. 在实际布局中，我们通常需要往 `CustomScrollView` 中添加一些自定义的组件，而这些组件并非都有 `Sliver` 版本，为此 Flutter 提供了一个 `SliverToBoxAdapter` 组件，它是一个适配器：可以将 `RenderBox` 适配为 `Sliver`。比如我们想在列表顶部添加一个可以横向滑动的 `PageView`，可以使用 `SliverToBoxAdapter` 来配置：

```dart
import 'package:flutter/material.dart';

class SliverToBoxAdapterComponent extends StatefulWidget {
  const SliverToBoxAdapterComponent({Key? key}) : super(key: key);

  @override
  _SliverToBoxAdapterComponentState createState() => _SliverToBoxAdapterComponentState();
}

class _SliverToBoxAdapterComponentState extends State<SliverToBoxAdapterComponent>{

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * SliverFixedExtentList 是一个 Sliver，它可以生成高度相同的列表项。
     * 再次提醒，如果列表项高度相同，我们应该优先使用SliverFixedExtentList 和 SliverPrototypeExtentList，
     * 如果不同，使用 SliverList.
     */
    var listView1 = SliverFixedExtentList(
      // 列表项高度固定
      itemExtent: 56,
      delegate: SliverChildBuilderDelegate(
        (_, index) => ListTile(title: Text('第一个列表 $index')),
        childCount: 20,
      ),
    );

    var listView2 = SliverFixedExtentList(
      // 列表项高度固定
      itemExtent: 56,
      delegate: SliverChildBuilderDelegate(
            (_, index) => ListTile(title: Text('第二个列表 ${index + 20}')),
        childCount: 20,
      ),
    );

    // CustomScrollView 是一个可以自定义滚动模型的组件，它可以包含多种滚动模型。
    return CustomScrollView(
      // slivers 是 CustomScrollView 的一个参数，它接受一个 SliverList 集合。
      slivers: [
        SliverToBoxAdapter(
          child: SizedBox(
            height: 300,
            child: PageView(
              children: const [Text("1", textScaleFactor: 20), Text("2", textScaleFactor: 20)],
            ),
          ),
        ),
        listView1,
        // 插入一个分割线
        SliverToBoxAdapter(
          child: Container(
            height: 1.0,
            color: Colors.grey,
          ),
        ),
        listView2,
      ],
    );
  }

}
```

2. 效果：

![|415](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画4.gif)

3. 注意，上面的代码是可以正常运行的，但是如果将 `PageView` 换成一个滑动方向和 `CustomScrollView` 一致的 `ListView` 则不会正常工作！
4. 原因是：`CustomScrollView` 组合 `Sliver` 的原理是为所有子 `Sliver` 提供一个共享的 `Scrollable`，然后统一处理指定滑动方向的滑动事件，如果 `Sliver` 中引入了其他的 `Scrollable`，则滑动事件便会冲突。
5. 上例中 `PageView` 之所以能正常工作，是因为 `PageView` 的 `Scrollable` 只处理水平方向的滑动，而 `CustomScrollView` 是处理垂直方向的，两者并未冲突，所以不会有问题，但是换一个也是垂直方向的 `ListView` 时则不能正常工作，最终的效果是，在 `ListView` 内滑动时只会对 `ListView` 起作用，原因是滑动事件被 `ListView` 的 `Scrollable` 优先消费，`CustomScrollView` 的 `Scrollable` 便接收不到滑动事件了。
6. Flutter 中手势的冲突时，默认的策略是子元素生效，这个我们将在后面事件处理相关章节介绍。
7. 所以我们可以得出一个结论：如果 `CustomScrollView` 有孩子也是一个完整的可滚动组件且它们的滑动方向一致，则 `CustomScrollView` 不能正常工作。要解决这个问题，可以使用 `NestedScrollView`，这个我们将在下一节介绍

### ⑤、SliverPersistentHeader

1. SliverPersistentHeader 的功能是当滑动到 CustomScrollView 的顶部时，可以将组件固定在顶部。
2. 需要注意， Flutter 中设计 `SliverPersistentHeader` 组件的初衷是为了实现 `SliverAppBar`，所以它的一些属性和回调在 `SliverAppBar` 中才会用到。
3. 因此，如果我们要直接使用 `SliverPersistentHeader`，看到它的一些配置和参数会感到疑惑，使用起来会感觉有心智成本，为此，会在下面介绍中指出哪些是需要我们重点关注的，哪些是可以忽略的
4. 我们先看看 `SliverPersistentHeader` 的定义：

```dart
const SliverPersistentHeader({
  Key? key,
  /**
   * delegate 是用于生成 header 的委托，类型为 SliverPersistentHeaderDelegate，它是一个抽象类，需要我们自己实现
   */
  required SliverPersistentHeaderDelegate delegate,
  /**
   * header 滑动到可视区域顶部时是否固定在顶部
   */
  this.pinned = false, 
  /**
   * floating 的作用是：pinned 为 false 时 ，则 header 可以滑出可视区域（CustomScrollView 的 Viewport）（不会固定到顶部），
   * 当用户再次向下滑动时，此时不管 header 已经被滑出了多远，它都会立即出现在可视区域顶部并固定住，
   * 直到继续下滑到 header 在列表中原来的位置时，header 才会重新回到原来的位置（不再固定在顶部）
   */
  this.floating = false,
})
```

5. delegate 的定义如下：

```dart
abstract class SliverPersistentHeaderDelegate {

  /**
   * header 最大高度；pined为 true 时，当 header 刚刚固定到顶部时高度为最大高度。
   */
  double get maxExtent;

  /**
   * header 的最小高度；pined 为 true 时，当 header 固定到顶部，用户继续往上滑动时，
   * header 的高度会随着用户继续上滑从 maxExtent 逐渐减小到 minExtent
   */
  double get minExtent;

  /**
   * 构建 header。
   * shrinkOffset 取值范围 [0,maxExtent]，当 header 刚刚到达顶部时，shrinkOffset 值为 0，
   * 如果用户继续向上滑动列表，shrinkOffset 的值会随着用户滑动的偏移减小，直到减到 0 时。
   * overlapsContent：一般不建议使用，在使用时一定要小心，后面会解释。
   */
  Widget build(BuildContext context, double shrinkOffset, bool overlapsContent);

  /**
   * header 是否需要重新构建；通常当父级的 StatefulWidget 更新状态时会触发。
   * 一般来说只有当 Delegate 的配置发生变化时，应该返回false，比如新旧的 minExtent、maxExtent
   * 等其他配置不同时需要返回 true，其余情况返回 false 即可。
   */
  bool shouldRebuild(covariant SliverPersistentHeaderDelegate oldDelegate);

  /**
   * 下面这几个属性是 SliverPersistentHeader 在 SliverAppBar 中时实现 floating、snap 效果时会用到，
   * 平时开发过程很少使用到，可以先不用理会。
   */
  TickerProvider? get vsync => null;
  FloatingHeaderSnapConfiguration? get snapConfiguration => null;
  OverScrollHeaderStretchConfiguration? get stretchConfiguration => null;
  PersistentHeaderShowOnScreenConfiguration? get showOnScreenConfiguration => null;

}
```

6. 可以看到，我们最需要关注的就是 `maxExtent` 和 `minExtent`；`pined` 为 `true` 时，当 `header` 刚刚固定到顶部，此时会对它应用 `maxExtent` （最大高度）；当用户继续往上滑动时，`header` 的高度会随着用户继续上滑从 `maxExtent` 逐渐减小到 `minExtent`。如果我们想让 `header` 高度固定，则将 `maxExtent` 和 `minExtent` 指定为同样的值即可。

#### Ⅰ、实例

1. 主方法 `main.dart`

```dart
import 'package:flutter/material.dart';

import '04_可滚动组件/09_CustomScrollView 和 Slivers/04_1_SliverPersistentHeaderComponent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: SliverPersistentHeaderComponent(),
      )
    );
  }
}
```

2. 继承了 `SliverPersistentHeaderDelegate` 的 `SliverPersistentHeaderBuilder` 类，它用于定义 SliverPersistentHeader 的行为和外观

```dart
import 'dart:math';

import 'package:flutter/material.dart';

// 继承 SliverPersistentHeaderDelegate，它用于定义 SliverPersistentHeader 的行为和外观
class SliverPersistentHeaderBuilder extends SliverPersistentHeaderDelegate {
  // 构造函数，接收最小高度、最大高度和子 Widget 作为参数。
  SliverPersistentHeaderBuilder({
    required this.minHeight,
    required this.maxHeight,
    required this.child,
  });

  // 最小高度
  final double minHeight;
  // 最大高度
  final double maxHeight;
  // 子 Widget
  final Widget child;

  // 重写 minExtent，返回最小高度
  @override
  double get minExtent => minHeight;

  // 重写 maxExtent，返回最大高度。如果最大高度小于最小高度，返回最小高度
  @override
  double get maxExtent => max(maxHeight, minHeight);

  // 重写 build 方法，返回一个填充父 Widget 的 SizedBox，包含 child
  @override
  Widget build(BuildContext context, double shrinkOffset, bool overlapsContent) {
    return SizedBox.expand(child: child);
  }

  // 重写 shouldRebuild 方法，当最大高度、最小高度或子 Widget 改变时，重新构建
  @override
  bool shouldRebuild(SliverPersistentHeaderBuilder oldDelegate) {
    return maxHeight != oldDelegate.maxHeight ||
        minHeight != oldDelegate.minHeight ||
        child != oldDelegate.child;
  }

}
```

3. `SliverPersistentHeaderComponent` 类使用 `SliverPersistentHeaderBuilder`

```dart
import 'package:flutter/material.dart';

import '04_2_SliverPersistentHeader.dart';

class SliverPersistentHeaderComponent extends StatefulWidget {
  const SliverPersistentHeaderComponent({Key? key}) : super(key: key);

  @override
  _SliverPersistentHeaderComponentState createState() => _SliverPersistentHeaderComponentState();
}

class _SliverPersistentHeaderComponentState extends State<SliverPersistentHeaderComponent>{

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * SliverFixedExtentList 是一个 Sliver，它可以生成高度相同的列表项。
     * 再次提醒，如果列表项高度相同，我们应该优先使用SliverFixedExtentList 和 SliverPrototypeExtentList，
     * 如果不同，使用 SliverList.
     */
    var listView1 = SliverFixedExtentList(
      // 列表项高度固定
      itemExtent: 56,
      delegate: SliverChildBuilderDelegate(
        (_, index) => ListTile(title: Text('第一个列表 $index')),
        childCount: 20,
      ),
    );

    // CustomScrollView 是一个可以自定义滚动模型的组件，它可以包含多种滚动模型。
    return CustomScrollView(
      // slivers 是 CustomScrollView 的一个参数，它接受一个 SliverList 集合。
      slivers: [
        // 调用方法，返回一个 SliverPersistentHeader
        _SliverPersistentHeaderBuilder(),
        listView1,
        // 插入一个分割线
        SliverToBoxAdapter(
          child: Container(
            height: 1.0,
            color: Colors.grey,
          ),
        ),
        // 调用方法，返回一个 SliverPersistentHeader
        _SliverPersistentHeaderBuilder(),
        listView1,
      ],
    );
  }

  // 构建 SliverPersistentHeader，它是一个固定高度的 Sliver，它可以在滚动时固定在顶部或底部，实现吸顶或吸底效果
  Widget _SliverPersistentHeaderBuilder(){
    return SliverPersistentHeader(
      // pinned 为 true 时，代表 SliverPersistentHeader 向上滚动时会固定在顶部
      pinned: true,
      delegate: SliverPersistentHeaderBuilder(
        // minHeight 最小高度
        minHeight: 60.0,
        // maxHeight 最大高度
        maxHeight: 200.0,
        // child 子 Widget；Container 是一个常用的容器类 Widget，它可以装饰、布局、限制子 Widget，相当于 Android 中的 FrameLayout
        child: Container(
          color: Colors.green,
          child: const Center(
            child: Text('Persistent Header'),
          ),
        ),
      ),
    );
  }

}
```

#### Ⅱ、效果

![|415](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画5.gif)

#### Ⅲ、一些注意点

1. `SliverPersistentHeader` 的 `builder` 参数 `overlapsContent` 一般不建议使用，使用时要当心。
2. 因为按照 `overlapsContent` 变量名的字面意思，只要有内容和 `Sliver` 重叠时就应该为 `true`，但是如果我们在上面示例的 `builder` 中打印一下 `overlapsContent` 的值就会发现第一个 PersistentHeader 1 的 `overlapsContent` 值一直都是 `false`，而 PersistentHeader 2 则是正常的，如果我们再添加几个 `SliverPersistentHeader` ，发现新添加的也都正常。总结一下：当有多个 `SliverPersistentHeader` 时，需要注意第一个 `SliverPersistentHeader` 的 `overlapsContent` 值会一直为 `false`。
3. 这可能是一个 bug，也可能就是这么设计的，因为 `SliverPersistentHeader` 的设计初衷主要是为了实现 `SliverAppBar`，可能并没有考虑到通用的场景，但是不管怎样，当前的 flutter 版本（2.5）中表现就是如此。
4. 为此，我们可以定一条约定：如果我们在使用 `SliverPersistentHeader` 构建子组件时需要依赖 `overlapsContent` 参数，则必须保证之前至少还有一个 `SliverPersistentHeader` 或 `SliverAppBar`（SliverAppBar 在当前 Flutter 版本的实现中内部包含了SliverPersistentHeader）。

## 11、自定义 Sliver

## 12、嵌套可滚动组件 NestedScrollView

# 七、功能型组件

## 1、导航返回拦截（WillPopScope）

1. 为了避免用户误触返回按钮而导致 App 退出，在很多 App 中都拦截了用户点击返回键的按钮，然后进行一些防误触判断，比如当用户在某一个时间段内点击两次时，才会认为用户是要退出（而非误触）。
2. Flutter 中可以通过 `WillPopScope` 来实现返回按钮拦截，我们看看 `WillPopScope` 的默认构造函数：

```dart
const WillPopScope({
  ...
  /**
   * onWillPop 是一个回调函数，当用户点击返回按钮时被调用（包括导航返回按钮及 Android 物理返回按钮）。
   * 该回调需要返回一个 Future 对象，如果返回的 Future 最终值为 false 时，则当前路由不出栈(不会返回)；
   * 最终值为 true 时，当前路由出栈退出。我们需要提供这个回调来决定是否退出
   */
  required WillPopCallback onWillPop,
  required Widget child
})
```

3. 实例：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/01_导航返回拦截（WillPopScope）.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: WillPopScopeComponent(),
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class WillPopScopeComponent extends StatefulWidget {
  const WillPopScopeComponent({Key? key}) : super(key: key);

  @override
  _WillPopScopeComponentState createState() => _WillPopScopeComponentState();
}

class _WillPopScopeComponentState extends State<WillPopScopeComponent> {

  // 记录上次点击时间
  DateTime? _lastPressedAt;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // WillPopScope 是一个小部件，用于检测 Android 返回按钮和导航栏返回按钮的点击事件。
    return WillPopScope(
      // onWillPop 是 WillPopScope 的一个属性，它接受一个 Future<bool> 类型的回调函数；async 表示该函数是一个异步函数
      onWillPop: () async {
        /**
         * 如果 _lastPressedAt 为 null 或者 当前时间与上次点击时间间隔超过 1 秒，则将当前时间赋值给 _lastPressedAt，并返回 false
         * 返回 false 表示不退出；返回 true 表示退出
         */
        if (_lastPressedAt == null || DateTime.now().difference(_lastPressedAt!) > const Duration(seconds: 1)) {
          // 两次点击间隔超过 1 秒则重新计时
          _lastPressedAt = DateTime.now();
          return false;
        }
        return true;
      },
      child: Container(
        alignment: Alignment.center,
        child: const Text("1秒内连续按两次返回键退出"),
      )
    );
  }

}
```

4. 效果：

![|409](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画6.gif)

## 2、数据共享（InheritedWidget）

### ①、简介

1. `InheritedWidget` 是 Flutter 中非常重要的一个功能型组件，它提供了一种在 `widget` 树中从上到下共享数据的方式，比如我们在应用的根 `widget` 中通过 `InheritedWidget` 共享了一个数据，那么我们便可以在任意子 `widget` 中来获取该共享的数据！
2. 这个特性在一些需要在整个 `widget` 树中共享数据的场景中非常方便！如 Flutter SDK 中正是通过 `InheritedWidget` 来共享应用主题（Theme）和 Locale (当前语言环境)信息的。
3. `InheritedWidget` 和 `React` 中的 `context` 功能类似，和逐级传递数据相比，它们能实现组件跨级传递数据。
4. `InheritedWidget` 在 `widget` 树中数据传递方向是从上到下的，这和通知 Notification（将在下一章中介绍）的传递方向正好相反。
5. 下面我们看一下之前“计数器”示例应用程序的 `InheritedWidget` 版本。
6. 需要说明的是，本示例主要是为了演示 `InheritedWidget` 的功能特性，并不是计数器的推荐实现方式。
7. 首先，我们通过继承 `InheritedWidget`，将当前计数器点击次数保存在 `ShareDataWidget` 的 `data` 属性中：

```dart
import 'package:flutter/material.dart';

class ShareDataWidget extends InheritedWidget {
  const ShareDataWidget({
    Key? key,
    required this.data,
    required Widget child,
  }) : super(key: key, child: child);

  // 需要在子树中共享的数据，保存点击次数
  final int data;

  /// 该回调决定当 data 发生变化时，是否通知子树中依赖 data 的 Widget 重新 build
  /// 如果返回 true，则子树中依赖 data 的 Widget 的 `state.didChangeDependencies` 会被调用
  @override
  bool updateShouldNotify(covariant ShareDataWidget oldWidget) {
    return oldWidget.data != data;
  }

  // 定义一个便捷方法，方便子树中的 widget 获取共享数据
  static ShareDataWidget? of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<ShareDataWidget>();
  }

}
```

8. 然后我们实现一个子组件 `ShowShareDataWidgetComponent`，在其 `build` 方法中引用 `ShareDataWidget` 中的数据。同时，在其 `didChangeDependencies()` 回调中打印日志：

```dart
import 'package:flutter/material.dart';

import '02_1_ShareDataWidget.dart';

class ShowShareDataWidgetComponent extends StatefulWidget {
  const ShowShareDataWidgetComponent({Key? key}) : super(key: key);

  @override
  _ShowShareDataWidgetComponentState createState() => _ShowShareDataWidgetComponentState();
}

class _ShowShareDataWidgetComponentState extends State<ShowShareDataWidgetComponent> {

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // 使用 InheritedWidget 中的共享数据
    return Text(ShareDataWidget.of(context)!.data.toString());
  }

  /// 下面会详细介绍
  /// didChangeDependencies 是一个 State 的方法，当依赖的 State 发生变化时会被调用
  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // 父或祖先 widget 中的 InheritedWidget 改变(updateShouldNotify 返回 true)时会被调用。
    // 如果 build 中没有依赖 InheritedWidget，则此回调不会被调用。
    print("Dependencies change ${ShareDataWidget.of(context)!.data.toString()}");
  }

}
```

### ②、didChangeDependencies 依赖改变回调

1. 在之前介绍 `StatefulWidget` 时，我们提到 `State` 对象有一个 `didChangeDependencies` 回调，它会在“依赖”发生变化时被 Flutter 框架调用。而这个“依赖”指的就是子 widget 是否使用了父 widget 中 `InheritedWidget` 的数据！
2. 如果使用了，则代表子 widget 有依赖；如果没有使用则代表没有依赖。
3. 这种机制可以使子组件在所依赖的 `InheritedWidget` 变化时来更新自身。比如当主题、locale(语言)等发生变化时，依赖其的子 widget 的 `didChangeDependencies` 方法将会被调用。
4. 最后，我们创建一个按钮，每点击一次，就将 `ShareDataWidget` 的值自增：

```dart
import 'package:flutter/material.dart';

import '02_1_ShareDataWidget.dart';
import '02_2_ShowShareDataWidgetComponent.dart';

class InheritedWidgetTestRoute extends StatefulWidget {
  const InheritedWidgetTestRoute({Key? key}) : super(key: key);

  @override
  _InheritedWidgetTestRouteState createState() => _InheritedWidgetTestRouteState();
}

class _InheritedWidgetTestRouteState extends State<InheritedWidgetTestRoute> {
  int count = 0;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将子小部件放置在水平和垂直方向上的中心位置的小部件。
    return Center(
      // ShareDataWidget 是一个小部件，用于在子树中保存共享数据。
      child: ShareDataWidget(
        data: count,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Padding(padding: EdgeInsets.only(bottom: 20.0), child: ShowShareDataWidgetComponent()),
            ElevatedButton(
              child: const Text("Increment"),
              onPressed: () => setState(() => ++count),
            )
          ],
        ),
      ),
    );
  }

}
```

5. `main.dart` 入口文件

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/02_3_InheritedWidgetTestRoute.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         */
        body: InheritedWidgetTestRoute(),
      )
    );
  }
}
```

6. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画7.gif)

### ③、didChangeDependencies 注意事项

1. 依赖发生变化后，其 `didChangeDependencies()` 会被调用。但是要注意，如果 `ShowShareDataWidgetComponent` 的 build 方法中没有使用 `ShareDataWidget` 的数据，那么它的 `didChangeDependencies()` 将不会被调用，因为它并没有依赖 `ShareDataWidget`
2. 应该在 `didChangeDependencies()` 中做什么？一般来说，子 widget 很少会重写此方法，因为在依赖改变后 Flutter 框架也都会调用 `build()` 方法重新构建组件树。但是，如果你需要在依赖改变后执行一些昂贵的操作，比如网络请求，这时最好的方式就是在此方法中执行，这样可以避免每次 `build(`) 都执行这些昂贵操作

### ④、深入了解 InheritedWidget

1. 现在来思考一下，在上面的例子中，如果我们只想在 `_ShowShareDataWidgetComponentState` 中引用 `ShareDataWidget` 数据，但却不希望在 `ShareDataWidget` 发生变化时调用 `_ShowShareDataWidgetComponentState` 的 `didChangeDependencies()` 方法应该怎么办？其实答案很简单，我们只需要将 `ShareDataWidget.of()` 的实现改一下即可：

```dart
// 定义一个便捷方法，方便子树中的 widget 获取共享数据
static ShareDataWidget of(BuildContext context) {
  // return context.dependOnInheritedWidgetOfExactType<ShareDataWidget>();
 return context.getElementForInheritedWidgetOfExactType<ShareDataWidget>()!.widget as ShareDataWidget;
}
```

2. 唯一的改动就是获取 `ShareDataWidget` 对象的方式，把 `dependOnInheritedWidgetOfExactType()` 方法换成了 `context.getElementForInheritedWidgetOfExactType<ShareDataWidget>().widget`，那么他们到底有什么区别呢，我们看一下这两个方法的源码（实现代码在 Element 类中，Context 和 Element 的关系我们将在后面专门介绍）：

```dart
@override
InheritedWidget dependOnInheritedElement(InheritedElement ancestor, { Object aspect }) {
	assert(ancestor != null);
	_dependencies ??= HashSet<InheritedElement>();
	_dependencies.add(ancestor);
	ancestor.updateDependencies(this, aspect);
	return ancestor.widget;
}
```

3. 可以看到 `dependOnInheritedElement` 方法中主要是注册了依赖关系！
4. 看到这里也就清晰了，调用 `dependOnInheritedWidgetOfExactType()` 和 `getElementForInheritedWidgetOfExactType()` 的区别就是前者会注册依赖关系，而后者不会，所以在调用 `dependOnInheritedWidgetOfExactType()` 时，`InheritedWidget` 和依赖它的子孙组件关系便完成了注册，之后当 `InheritedWidget` 发生变化时，就会更新依赖它的子孙组件，也就是会调这些子孙组件的 `didChangeDependencies()` 方法和 `build()` 方法。而当调用的是 `getElementForInheritedWidgetOfExactType()`时，由于没有注册依赖关系，所以之后当 `InheritedWidget` 发生变化时，就不会更新相应的子孙 Widget。
5. 注意，如果将上面示例中 `ShareDataWidget.of()` 方法实现改成调用 `getElementForInheritedWidgetOfExactType()`，运行示例后，点击`Increment`按钮，会发现 `_ShowShareDataWidgetComponentState` 的 `didChangeDependencies()` 方法确实不会再被调用，但是其 `build()` 仍然会被调用！造成这个的原因其实是，点击 `Increment` 按钮后，会调用 `_InheritedWidgetTestRouteState` 的 `setState()` 方法，此时会重新构建整个页面，由于示例中，`_ShowShareDataWidgetComponentState` 并没有任何缓存，所以它也都会被重新构建，所以也会调用 `build()` 方法。
6. 那么，现在就带来了一个问题：实际上，我们只想更新子树中依赖了 `ShareDataWidget` 的组件，而现在只要调用 `_InheritedWidgetTestRouteState` 的 `setState(`) 方法，所有子节点都会被重新 build，这很没必要，那么有什么办法可以避免呢？答案是缓存！一个简单的做法就是通过封装一个 `StatefulWidget`，将子 Widget 树缓存起来，具体做法下一节我们将通过实现一个 Provider Widget 来演示如何缓存，以及如何利用 `InheritedWidget` 来实现 Flutter 全局状态共享。

## 3、跨组件状态共享

### ①、通过事件同步状态

1. 在 Flutter 开发中，状态管理是一个永恒的话题。
2. 一般的原则是：
	1. 如果状态是组件私有的，则应该由组件自己管理；
	2. 如果状态要跨组件共享，则该状态应该由各个组件共同的父元素来管理。
3. 对于组件私有的状态管理很好理解，但对于跨组件共享的状态，管理的方式就比较多了
4. 如使用全局事件总线EventBus（将在下一章中介绍），它是一个观察者模式的实现，通过它就可以实现跨组件状态同步：状态持有方（发布者）负责更新、发布状态，状态使用方（观察者）监听状态改变事件来执行一些操作。下面我们看一个登录状态同步的简单示例：
5. 定义事件：

```dart
enum Event{
  login,
  ... //省略其他事件
}
```

6. 登录页代码大致如下：

```dart
// 登录状态改变后发布状态改变事件
bus.emit(Event.login);
```

7. 依赖登录状态的页面：

```dart
void onLoginChanged(e){
  //登录状态变化处理逻辑
}

@override
void initState() {
  //订阅登录状态改变事件
  bus.on(Event.login,onLogin);
  super.initState();
}

@override
void dispose() {
  //取消订阅
  bus.off(Event.login,onLogin);
  super.dispose();
}
```

8. 我们可以发现，通过观察者模式来实现跨组件状态共享有一些明显的缺点：
	1. 必须显式定义各种事件，不好管理。
	2. 订阅者必须需显式注册状态改变回调，也必须在组件销毁时手动去解绑回调以避免内存泄露。
9. 在 Flutter 当中有没有更好的跨组件状态管理方式了呢？答案是肯定的，那怎么做的？我们想想前面介绍的 `InheritedWidget`，它的天生特性就是能绑定 `InheritedWidget` 与依赖它的子孙组件的依赖关系，并且当 `InheritedWidget` 数据发生变化时，可以自动更新依赖的子孙组件
10. 利用这个特性，我们可以将需要跨组件共享的状态保存在 `InheritedWidget` 中，然后在子组件中引用 `InheritedWidget` 即可
11. Flutter 社区著名的 `Provider` 包正是基于这个思想实现的一套跨组件状态共享解决方案，接下来我们便详细介绍一下 `Provider` 的用法及原理

### ②、Provider

#### Ⅰ、自实现 Provider

1. 首先，我们需要一个能够保存共享数据的 `InheritedWidget`，由于具体业务数据类型不可预期，为了通用性，我们使用泛型，定义一个通用的 `InheritedProvider` 类，它继承自 `InheritedWidget`：

```dart
import 'package:flutter/material.dart';

// 一个通用的 InheritedWidget，保存需要跨组件共享的状态
class InheritedProvider<T> extends InheritedWidget {
  const InheritedProvider({Key? key, required this.data, required Widget child,}): super(key: key, child: child);

  // 需要在子树中共享的数据，保存点击次数
  final T data;

  /// 该回调决定当 data 发生变化时，是否通知子树中依赖 data 的 Widget 重新 build
  /// 如果返回 true，则子树中依赖 data 的 Widget 的 `state.didChangeDependencies` 会被调用
  @override
  bool updateShouldNotify(covariant InheritedProvider oldWidget) {
    // 在此简单返回 true，则每次更新都会调用依赖其的子孙节点的 `didChangeDependencies`。
    return true;
  }

}
```

2. 数据保存的地方有了，那么接下来我们需要做的就是在数据发生变化的时候来重新构建 `InheritedProvider`，那么现在就面临两个问题：
	1. 数据发生变化怎么通知？
	2. 谁来重新构建 `InheritedProvider`？
3. 第一个问题其实很好解决，我们当然可以使用之前介绍的 `eventBus` 来进行事件通知，但是为了更贴近 Flutter 开发，我们使用 Flutter SDK 中提供的 `ChangeNotifier` 类 ，它继承自 `Listenable`，也实现了一个 Flutter 风格的发布者 - 订阅者模式，`ChangeNotifier` 定义大致如下：

```dart
class ChangeNotifier implements Listenable {
  List listeners=[];
  @override
  void addListener(VoidCallback listener) {
     //添加监听器
     listeners.add(listener);
  }
  @override
  void removeListener(VoidCallback listener) {
    //移除监听器
    listeners.remove(listener);
  }
  
  void notifyListeners() {
    //通知所有监听器，触发监听器回调 
    listeners.forEach((item)=>item());
  }
   
  ... //省略无关代码
}
```

4. 我们可以通过调用 `addListener()` 和 `removeListener()` 来添加、移除监听器（订阅者）；通过调用`notifyListeners()` 可以触发所有监听器回调。
5. 现在，我们将要共享的状态放到一个 Model 类中，然后让它继承自 `ChangeNotifier`，这样当共享的状态改变时，我们只需要调用 `notifyListeners()` 来通知订阅者，然后由订阅者来重新构建 `InheritedProvider`，这也是第二个问题的答案！接下来我们便实现这个订阅者类：

```dart
import 'package:flutter/material.dart';

import '01_1_InheritedProvider.dart';

// 该类负责将 model 放入到 Widget 树中，实现共享，同时负责更新 Widget 树
class ChangeNotifierProvider<T extends ChangeNotifier> extends StatefulWidget {
  const ChangeNotifierProvider({Key? key, required this.data, required this.child,}) : super(key: key);

  // 需要共享的数据，通过泛型 T 传入
  final T data;
  // 子组件
  final Widget child;

  // 定义一个便捷方法，方便子树中的 widget 获取共享数据
  static T of<T>(BuildContext context) {
    // 获取当前上下文中的 InheritedProvider<T> 实例
    final provider = context.dependOnInheritedWidgetOfExactType<InheritedProvider<T>>();
    if (provider == null) {
      // 如果未找到对应的 InheritedProvider，则抛出错误
      throw FlutterError('ChangeNotifierProvider.of() called with a context that does not contain an InheritedProvider<$T> of type $T.');
    }
    // 返回获取到的共享数据
    return provider.data;
  }

  @override
  _ChangeNotifierProviderState<T> createState() => _ChangeNotifierProviderState<T>();
}
```

6. 该类继承 `StatefulWidget`，然后定义了一个 `of()` 静态方法供子类方便获取 Widget 树中的 `InheritedProvider` 中保存的共享状态(model)，下面我们实现该类对应的 `_ChangeNotifierProviderState` 类：

```dart
class _ChangeNotifierProviderState<T extends ChangeNotifier> extends State<ChangeNotifierProvider<T>> {
  void update() {
    // 如果数据发生变化（model 类调用了 notifyListeners），重新构建 InheritedProvider
    setState(() => {});
  }

  @override
  void didUpdateWidget(ChangeNotifierProvider<T> oldWidget) {
    // 当 Provider 更新时，如果新旧数据不相等，则解绑旧数据监听，同时添加新数据监听
    if (widget.data != oldWidget.data) {
      // 解绑旧数据监听
      oldWidget.data.removeListener(update);
      // 添加新数据监听
      widget.data.addListener(update);
    }
    super.didUpdateWidget(oldWidget);
  }

  @override
  void initState() {
    // 给 model 添加监听器
    widget.data.addListener(update);
    super.initState();
  }

  @override
  void dispose() {
    // 移除 model 的监听器
    widget.data.removeListener(update);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return InheritedProvider<T>(
      // 将共享数据传递给 InheritedProvider
      data: widget.data,
      // 将子组件传递给 InheritedProvider
      child: widget.child,
    );
  }
}
```

7. 可以看到 `_ChangeNotifierProviderState` 类的主要作用就是监听到共享状态（model）改变时重新构建 Widget 树。
8. 注意，在 `_ChangeNotifierProviderState` 类中调用 `setState()` 方法，`widget.child` 始终是同一个，所以执行 build 时，`InheritedProvider` 的 `child` 引用的始终是同一个子 widget，所以 `widget.child` 并不会重新 build，这也就相当于对 child 进行了缓存！当然如果 `ChangeNotifierProvider` 父级 Widget 重新 build 时，则其传入的 child 便有可能会发生变化。
9. 现在我们所需要的各个工具类都已完成，下面我们通过一个购物车的例子来看看怎么使用上面的这些类。

#### Ⅱ、购物车示例

1. 我们需要实现一个显示购物车中所有商品总价的功能：向购物车中添加新商品时总价更新
2. 定义一个 `Item` 类，用于表示商品信息：

```dart
class Item {
  // 商品单价
  double price;
  // 商品数量
  int count;

  Item(this.price, this.count);
}
```

3. 定义一个保存购物车内商品数据的 `CartModel` 类，`CartModel` 即要跨组件共享的 model 类。：

```dart
import 'dart:collection';

import 'package:flutter/cupertino.dart';

import '01_3_Item.dart';

class CartModel extends ChangeNotifier {
  // 用于保存购物车中商品列表
  final List<Item> _items = [];

  // 禁止改变购物车里的商品信息
  UnmodifiableListView<Item> get items => UnmodifiableListView(_items);

  // 购物车中商品的总价
  double get totalPrice => _items.fold(0, (value, item) => value + item.count * item.price);

  // 将 [item] 添加到购物车。这是唯一一种能从外部改变购物车的方法。
  void add(Item item) {
    _items.add(item);
    // 通知监听器（订阅者），重新构建InheritedProvider， 更新状态。
    notifyListeners();
  }
}
```

4. 最后我们构建示例页面：

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_2_ChangeNotifierProvider.dart';
import '01_3_Item.dart';
import '01_4_CartModel.dart';

class ProviderRoute extends StatefulWidget {
  const ProviderRoute({Key? key}) : super(key: key);

  @override
  _ProviderRouteState createState() => _ProviderRouteState();
}

class _ProviderRouteState extends State<ProviderRoute> {
  @override
  Widget build(BuildContext context) {
    // Center 组件可以将其子组件树对齐到屏幕中心
    return Center(
      // ChangeNotifierProvider 是一个通用的通知器，它接受一个数据对象，然后将该数据对象放入到 Widget 树中，子树中的任意节点都可以获取该数据对象。
      child: ChangeNotifierProvider<CartModel>(
        // CartModel 是一个 ChangeNotifier，它保存了购物车中商品的状态（比如商品列表、总价等）。
        data: CartModel(),
        /**
         * Builder 是一个回调函数，它接受一个 BuildContext 和一个子 Widget，然后返回一个 Widget。
         * 此处的作用是为了引入作用域，让后面的 RaisedButton 能够获取到该数据对象。
         */
        child: Builder(builder: (context) {
          // Column 可以将其子组件在垂直方向线性排列
          return Column(
            // MainAxisAlignment.center 表示将子组件在垂直方向居中排列
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              // 显示商品数量文本框
              buildQuantityTextField(context),
              // 添加商品按钮
              buildAddProductButton(context),
            ],
          );
        }),
      ),
    );
  }

  // 显示商品数量文本框
  Widget buildQuantityTextField(BuildContext context){
    return Builder(builder: (context){
      // 通过 ChangeNotifierProvider.of 获取到 CartModel 实例，然后获取到商品总价
      var cart = ChangeNotifierProvider.of<CartModel>(context);
      return Text("总价: ${cart.totalPrice}");
    });
  }

  // 添加商品按钮
  Widget buildAddProductButton(BuildContext context){
    return Builder(builder: (context){
      // 构建时输出日志，在后面优化部分会用到
      print("ElevatedButton build");
      return ElevatedButton(
        child: const Text("添加商品"),
        onPressed: () {
          // 给购物车中添加商品，添加后总价会更新
          ChangeNotifierProvider.of<CartModel>(context).add(Item(20.0, 1));
        },
      );
    });

  }

}
```

5. 运行示例后效果如图所示：

![|423](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画11.gif)

#### Ⅲ、说明

1. 每次点击”添加商品“按钮，总价就会增加 20，我们期望的功能实现了！
2. 可能有些人会疑惑，我们饶了一大圈实现这么简单的功能有意义么？其实，就这个例子来看，只是更新同一个路由页中的一个状态，我们使用 `ChangeNotifierProvider` 的优势并不明显，但是如果我们是做一个购物 APP 呢？
3. 由于购物车数据是通常是会在整个 APP 中共享的，比如会跨路由共享。如果我们将 `ChangeNotifierProvider` 放在整个应用的 Widget 树的根上，那么整个 APP 就可以共享购物车的数据了，这时 `ChangeNotifierProvider` 的优势将会非常明显。
4. 虽然上面的例子比较简单，但它却将 Provider 的原理和流程体现的很清楚，下图是 Provider 的原理图：

![|500](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231116144523.png)

5. Model 变化后会自动通知 `ChangeNotifierProvider`（订阅者），`ChangeNotifierProvider` 内部会重新构建 `InheritedWidget`，而依赖该 `InheritedWidget` 的子孙 Widget 就会更新。
6. 我们可以发现使用 Provider，将会带来如下收益：
	1. 我们的业务代码更关注数据了，只要更新 Model，则 UI 会自动更新，而不用在状态改变后再去手动调用 `setState()` 来显式更新页面。
	2. 数据改变的消息传递被屏蔽了，我们无需手动去处理状态改变事件的发布和订阅了，这一切都被封装在 Provider 中了。
	3. 在大型复杂应用中，尤其是需要全局共享的状态非常多时，使用 Provider 将会大大简化我们的代码逻辑，降低出错的概率，提高开发效率

### ③、优化

- 我们上面实现的 `ChangeNotifierProvider` 有两个明显缺点：代码组织问题和性能问题，下面我们一一讨论

#### Ⅰ、代码组织问题

1. 我们先看一下构建显示总价 `Text` 的代码：

```dart
// 显示商品数量文本框
Widget buildQuantityTextField(BuildContext context){
return Builder(builder: (context){
  // 通过 ChangeNotifierProvider.of 获取到 CartModel 实例，然后获取到商品总价
  var cart = ChangeNotifierProvider.of<CartModel>(context);
  return Text("总价: ${cart.totalPrice}");
});
}
```

2. 这段代码有两点可以优化：
	1. 需要显式调用 `ChangeNotifierProvider.of`，当 APP 内部依赖 CartModel 很多时，这样的代码将很冗余。
	2. 语义不明确；由于 `ChangeNotifierProvider` 是订阅者，那么依赖 CartModel 的 Widget 自然就是订阅者，其实也就是状态的消费者，如果我们用 Builder 来构建，语义就不是很明确；如果我们能使用一个具有明确语义的 Widget，比如就叫 `Consumer`，这样最终的代码语义将会很明确，只要看到 `Consumer`，我们就知道它是依赖某个跨组件或全局的状态。
3. 为了优化这两个问题，我们可以封装一个 `Consumer` Widget，实现如下：

```dart
import 'package:flutter/cupertino.dart';

import '01_2_ChangeNotifierProvider.dart';

// 这是一个便捷类，会获得当前 context 和指定数据类型的 Provider
class Consumer<T> extends StatelessWidget {
  Consumer({
    Key? key,
    required this.builder,
  }) : super(key: key);

  final Widget Function(BuildContext context, T? value) builder;

  @override
  Widget build(BuildContext context) {
    return builder(
      // 将当前的 BuildContext 传递给 builder 函数
      context,
      // 获取指定数据类型 T 的 Provider，并将其传递给 builder 函数
      ChangeNotifierProvider.of<T>(context),
    );
  }
}
```

4. `Consumer` 实现非常简单，它通过指定模板参数，然后再内部自动调用 `ChangeNotifierProvider.of` 获取相应的 Model，并且 `Consumer` 这个名字本身也是具有确切语义（消费者）。现在上面的代码块可以优化为如下这样：

```dart
  // 显示商品数量文本框
  Widget buildQuantityTextField(BuildContext context){
    return Consumer<CartModel>(
      builder: (context, cart) => Text("总价: ${cart?.totalPrice}")
    );
  }
```

#### Ⅱ、性能问题

1. 上面的代码还有一个性能问题，就在构建”添加按钮“的代码处：

```dart
// 添加商品按钮
Widget buildAddProductButton(BuildContext context){
return Builder(builder: (context){
  // 构建时输出日志，在后面优化部分会用到
  print("ElevatedButton build");
  return ElevatedButton(
	child: const Text("添加商品"),
	onPressed: () {
	  // 给购物车中添加商品，添加后总价会更新
	  ChangeNotifierProvider.of<CartModel>(context).add(Item(20.0, 1));
	},
  );
});

}
```

2. 我们点击”添加商品“按钮后，由于购物车商品总价会变化，所以显示总价的 Text 更新是符合预期的，但是”添加商品“按钮本身没有变化，是不应该被重新 build 的。
3. 但是我们运行示例，每次点击”添加商品“按钮，控制台都会输出 `ElevatedButton build` 日志，也就是说”添加商品“按钮在每次点击时其自身都会重新 build
4. 这是为什么呢？如果你已经理解了 `InheritedWidget` 的更新机制，那么答案一眼就能看出：这是因为构建 `ElevatedButton` 的 `Builder` 中调用了 `ChangeNotifierProvider.of`，也就是说依赖了 Widget 树上面的 `InheritedWidget`（即 `InheritedProvider` ）Widget，所以当添加完商品后，`CartModel` 发生变化，会通知 `ChangeNotifierProvider`, 而 `ChangeNotifierProvider` 则会重新构建子树，所以 `InheritedProvider` 将会更新，此时依赖它的子孙 Widget 就会被重新构建。
5. 问题的原因搞清楚了，那么我们如何避免这不必要重构呢？既然按钮重新被 build 是因为按钮和 `InheritedWidget` 建立了依赖关系，那么我们只要打破或解除这种依赖关系就可以了。那么如何解除按钮和 `InheritedWidget` 的依赖关系呢？
6. 我们上一节介绍 `InheritedWidget` 时已经讲过了：调用 `dependOnInheritedWidgetOfExactType()` 和  `getElementForInheritedWidgetOfExactType()` 的区别就是前者会注册依赖关系，而后者不会。
7. 所以我们只需要将 `ChangeNotifierProvider.of` 的实现改为下面这样即可：

```dart
/// 定义一个便捷方法，方便子树中的 widget 获取共享数据
/// listen 表示是否建立依赖关系，如果为 true，则会建立依赖关系，否则不会建立依赖关系
static T of<T>(BuildContext context, {bool listen = true}) {
    // 如果 listen 为 true，则会建立依赖关系，否则不会建立依赖关系
    final provider = listen
        ? context.dependOnInheritedWidgetOfExactType<InheritedProvider<T>>()
        : context.getElementForInheritedWidgetOfExactType<InheritedProvider<T>>()?.widget
    as InheritedProvider<T>;

    if (provider == null) {
      // 如果未找到对应的 InheritedProvider，则抛出错误
      throw FlutterError('ChangeNotifierProvider.of() called with a context that does not contain an InheritedProvider<$T> of type $T.');
    }

    // 返回获取到的共享数据
    return provider.data;
}
```

8. 然后我们将调用部分代码改为：

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_2_ChangeNotifierProvider.dart';
import '01_3_Item.dart';
import '01_4_CartModel.dart';
import '01_6_Consumer.dart';

class ProviderRoute extends StatefulWidget {
  const ProviderRoute({Key? key}) : super(key: key);

  @override
  _ProviderRouteState createState() => _ProviderRouteState();
}

class _ProviderRouteState extends State<ProviderRoute> {
  @override
  Widget build(BuildContext context) {
    // Center 组件可以将其子组件树对齐到屏幕中心
    return Center(
      // ChangeNotifierProvider 是一个通用的通知器，它接受一个数据对象，然后将该数据对象放入到 Widget 树中，子树中的任意节点都可以获取该数据对象。
      child: ChangeNotifierProvider<CartModel>(
        // CartModel 是一个 ChangeNotifier，它保存了购物车中商品的状态（比如商品列表、总价等）。
        data: CartModel(),
        /**
         * Builder 是一个回调函数，它接受一个 BuildContext 和一个子 Widget，然后返回一个 Widget。
         * 此处的作用是为了引入作用域，让后面的 RaisedButton 能够获取到该数据对象。
         */
        child: Builder(builder: (context) {
          // Column 可以将其子组件在垂直方向线性排列
          return Column(
            // MainAxisAlignment.center 表示将子组件在垂直方向居中排列
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              // 显示商品数量文本框
              buildQuantityTextField(context),
              // 添加商品按钮
              buildAddProductButton(context),
            ],
          );
        }),
      ),
    );
  }

  // 显示商品数量文本框
  Widget buildQuantityTextField(BuildContext context){
    return Consumer<CartModel>(
      builder: (context, cart) => Text("总价: ${cart?.totalPrice}")
    );
  }

  // 添加商品按钮
  Widget buildAddProductButton(BuildContext context){
    return Builder(builder: (context){
      // 构建时输出日志，在后面优化部分会用到
      print("ElevatedButton build");
      return ElevatedButton(
        child: const Text("添加商品"),
        onPressed: () {
          // 给购物车中添加商品，添加后总价会更新
          ChangeNotifierProvider.of<CartModel>(context, listen: false).add(Item(20.0, 1));
        },
      );
    });
  }

}
```

9. 修改后再次运行上面的示例，我们会发现点击”添加商品“按钮后，控制台不会再输出 `ElevatedButton build` 了，即按钮不会被重新构建了。而总价仍然会更新，这是因为 `Consumer` 中调用 `ChangeNotifierProvider.of` 时 `listen` 值为默认值 `true`，所以还是会建立依赖关系。
10. 至此我们便实现了一个迷你的 `Provider`，它具备 Pub 上 Provider Package 中的核心功能；
11. 但是我们的迷你版功能并不全面，如只实现了一个可监听的 `ChangeNotifierProvider`，并没有实现只用于数据共享的 Provider；
12. 另外，我们的实现有些边界也没有考虑的到，比如如何保证在 Widget 树重新 build 时 Model 始终是单例等。

### ④、其他状态管理包

- 现在 Flutter 社区已经有很多专门用于状态管理的包了，在此我们列出几个相对评分比较高的：

| 包名 | 介绍 |
| ---- | ---- |
|[Provider](https://pub.flutter-io.cn/packages/provider) & [Scoped Model](https://pub.flutter-io.cn/packages/scoped_model) |这两个包都是基于 InheritedWidget 的，原理相似|
|[Redux](https://pub.flutter-io.cn/packages/flutter_redux)|是 Web 开发中 React 生态链中 Redux 包的 Flutter 实现|
|[MobX](https://pub.dev/packages/flutter_mobx)|是 Web 开发中 React 生态链中 MobX 包的 Flutter 实现|
|[BLoC](https://pub.dev/packages/flutter_bloc)|是 BLoC 模式的 Flutter 实现|

## 4、颜色和主题

### ①、颜色

#### Ⅰ、简介

1. 在介绍主题前我们先了解一些 Flutter 中的 Color 类。
2. Color 类中颜色以一个 int 值保存，我们知道显示器颜色是由红、绿、蓝三基色组成，每种颜色占 8 比特，存储结构如下：

| Bit（位） | 颜色            |
| --------- | --------------- |
| 0-7       | 蓝色            |
| 8-15      | 绿色            |
| 16-23     | 红色            |
| 24-31     | Alpha(不透明度) |

3. 上面表格中的字段在 Color 类中都有对应的属性，而 Color 中的众多方法也就是操作这些属性的
4. 此我们主要讨论一下色值如何转换为 Color 对象、颜色亮度以及 MaterialColor。

#### Ⅱ、如何将颜色字符串转成 Color 对象

- 如 Web 开发中的色值通常是一个字符串如 `#dc380d`，它是一个 RGB 值，我们可以通过下面这些方法将其转为 Color 类：

```dart
// 如果颜色固定可以直接使用整数值
Color(0xffdc380d);

// 颜色是一个字符串变量
var c = "dc380d";
// 通过位运算符将 Alpha 设置为 FF
Color(int.parse(c,radix:16)|0xFF000000)
// 通过方法将 Alpha 设置为 FF
Color(int.parse(c,radix:16)).withAlpha(255)
```

#### Ⅲ、颜色亮度

1. 假如，我们要实现一个背景颜色和 Title 可以自定义的导航栏，
	1. 并且背景色为深色时我们应该让 Title 显示为浅色；
	2. 背景色为浅色时，Title 显示为深色。
2. 要实现这个功能，我们就需要来计算背景色的亮度，然后动态来确定 Title 的颜色。
3. Color 类中提供了一个 `computeLuminance()` 方法，它可以返回一个 `0-1` 的一个值，数字越大颜色就越浅，我们可以根据它来动态确定 Title 的颜色，下面是导航栏 NavBar 的简单实现：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/03_跨组件状态共享/05_ProviderRoute.dart';
import '05_功能型组件/04_颜色和主题/01_NavBar.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: Column(
            children: <Widget>[
              // 背景为蓝色，则 title 自动为白色
              NavBar(color: Colors.blue, title: "标题"),
              // 背景为白色，则 title 自动为黑色
              NavBar(color: Colors.white, title: "标题"),
            ],
          )
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class NavBar extends StatelessWidget {
  // 显示文本
  final String title;
  // 背景颜色
  final Color color;

  const NavBar({Key? key, required this.color, required this.title,}): super(key: key);

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      /**
       * constraints 是 Container 的一个属性，用于设置 Container 的大小。
       * BoxConstraints 是一个用于设置限制条件的类，它可以给子部件设置最大宽度、最小宽度、最大高度、最小高度等限制条件。
       */
      constraints: const BoxConstraints(
        // 宽度尽可能大
        minWidth: double.infinity,
        minHeight: 52,
      ),
      /**
       * decoration 是 Container 的一个属性，用于设置 Container 的装饰，如背景色、边框、阴影等。
       * // BoxDecoration 是一个装饰类小部件，它可以在其子小部件之上绘制一个装饰，如背景、边框、渐变等。
       */
      decoration: BoxDecoration(
        // 背景色
        color: color,
        boxShadow: const [
          // 阴影
          BoxShadow(
            color: Colors.black26,
            offset: Offset(0, 3),
            blurRadius: 3,
          ),
        ],
      ),
      // 居中
      alignment: Alignment.center,
      child: Text(
        title,
        style: TextStyle(
          fontWeight: FontWeight.bold,
          // 根据背景色亮度来确定 Title 颜色；亮度 < 0.5 则为白色，否则为黑色
          color: color.computeLuminance() < 0.5 ? Colors.white : Colors.black,
        ),
      ),
    );
  }
}
```

### ②、MaterialColor

1. `MaterialColor` 是实现 Material Design 中的颜色的类，它包含一种颜色的 10 个级别的渐变色。
2. `MaterialColor` 通过 `[]` 运算符的索引值来代表颜色的深度，有效的索引有：`50、100、200、…、900`，数字越大，颜色越深。
3. `MaterialColor` 的默认值为索引等于 500 的颜色。举个例子，`Colors.blue` 是预定义的一个 `MaterialColor` 类对象，定义如下：

```dart
static const MaterialColor blue = MaterialColor(
  _bluePrimaryValue,
  <int, Color>{
     50: Color(0xFFE3F2FD),
    100: Color(0xFFBBDEFB),
    200: Color(0xFF90CAF9),
    300: Color(0xFF64B5F6),
    400: Color(0xFF42A5F5),
    500: Color(_bluePrimaryValue),
    600: Color(0xFF1E88E5),
    700: Color(0xFF1976D2),
    800: Color(0xFF1565C0),
    900: Color(0xFF0D47A1),
  },
);
static const int _bluePrimaryValue = 0xFF2196F3;
```

4. 我们可以根据 shadeXX 来获取具体索引的颜色。`Colors.blue.shade50` 到 `Colors.blue.shade900` 的色值从浅蓝到深蓝渐变，效果如图所示：

![|320](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231117150148.png)

### ③、主题（Theme）

1. `Theme` 组件可以为 Material APP 定义主题数据（ThemeData）。
2. Material 组件库里很多组件都使用了主题数据，如导航栏颜色、标题字体、Icon 样式等。
3. `Theme` 内会使用 `InheritedWidget` 来为其子树共享样式数据。

#### Ⅰ、ThemeData

1. `ThemeData` 用于保存是 Material 组件库的主题数据，Material 组件需要遵守相应的设计规范，而这些规范可自定义部分都定义在 `ThemeData` 中了，所以我们可以通过 `ThemeData` 来自定义应用主题。在子组件中，我们可以通过 `Theme.of` 方法来获取当前的 ThemeData。
2. 注意：Material Design 设计规范中有些是不能自定义的，如导航栏高度，`ThemeData` 只包含了可自定义部分。
3. 我们看看 `ThemeData` 部分数据定义：

```dart
ThemeData({
  Brightness? brightness, //深色还是浅色
  MaterialColor? primarySwatch, //主题颜色样本，见下面介绍
  Color? primaryColor, //主色，决定导航栏颜色
  Color? cardColor, //卡片颜色
  Color? dividerColor, //分割线颜色
  ButtonThemeData buttonTheme, //按钮主题
  Color dialogBackgroundColor,//对话框背景颜色
  String fontFamily, //文字字体
  TextTheme textTheme,// 字体主题，包括标题、body等文字样式
  IconThemeData iconTheme, // Icon的默认样式
  TargetPlatform platform, //指定平台，应用特定平台控件风格
  ColorScheme? colorScheme,
  ...
})
```

4. 上面只是 `ThemeData` 的一小部分属性，完整的数据定义可以查看SDK。
5. 上面属性中需要说明的是 `primarySwatch`，它是主题颜色的一个"样本色"，通过这个样本色可以在一些条件下生成一些其他的属性
6. 例如，如果没有指定 `primaryColor`，并且当前主题不是深色主题，那么 `primaryColor` 就会默认为 `primarySwatch` 指定的颜色，还有一些相似的属性如 `indicatorColor` 也会受 `primarySwatch` 影响

#### Ⅱ、实例

1. 我们实现一个路由换肤功能：

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ThemeTestRoute extends StatefulWidget {
  const ThemeTestRoute({super.key});

  @override
  _ThemeTestRouteState createState() => _ThemeTestRouteState();
}

class _ThemeTestRouteState extends State<ThemeTestRoute> {
  // 当前路由主题色
  var _themeColor = Colors.teal;

  @override
  Widget build(BuildContext context) {
    // 获取主题
    ThemeData themeData = Theme.of(context);

    // Theme 是 Flutter 提供的一个小部件，用于设置应用程序主题。
    return Theme(
      // data 属性用于设置当前路由主题色，如果不设置，则使用上层主题；ThemeData 是一个主题数据类，它包含了应用程序主题的所有属性。
      data: ThemeData(
        // 用于导航栏、FloatingActionButton 的背景色等
        primarySwatch: _themeColor,
        // 用于 Icon 颜色
        iconTheme: IconThemeData(color: _themeColor)
      ),
      /**
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      child: Scaffold(
        // appBar 是 Scaffold 的一个属性，用于设置应用程序顶部的导航栏。
        appBar: AppBar(title: const Text("主题测试")),
        /**
         * body 是 Scaffold 的一个属性，用于定义页面的主要内容区域
         * Column 是一个小部件，它可以在垂直方向上排列其子部件。
         */
        body: Column(
          // 用于指定子部件在垂直方向上的对齐方式
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // 第一行 Icon 使用主题中的 iconTheme；不设置则使用默认主题
            const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Icon(Icons.favorite),
                  Icon(Icons.airport_shuttle),
                  Text("  颜色跟随主题")
                ]
            ),
            // 为第二行 Icon 自定义颜色（固定为黑色)；设置后，颜色不会跟随主题
            Theme(
              // themeData.copyWith 用于复制当前主题并设置新的值
              data: themeData.copyWith(
                // iconTheme 用于设置 Icon 的主题
                iconTheme: themeData.iconTheme.copyWith(
                  color: Colors.black
                ),
              ),
              child: const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Icon(Icons.favorite),
                    Icon(Icons.airport_shuttle),
                    Text("  颜色固定黑色")
                  ]
              ),
            ),
          ],
        ),
        // 点击按钮，切换主题，主题色在蓝色和青色之间切换
        floatingActionButton: FloatingActionButton(
            onPressed: (){
              setState(() =>
                _themeColor = _themeColor == Colors.teal ? Colors.blue : Colors.teal
              );
            },
            child: const Icon(Icons.palette)
        ),
      ),
    );
  }
}
```

2. 运行后点击右下角悬浮按钮则可以切换主题，如图所示：

![|412](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画12.gif)

3. 可以通过局部主题覆盖全局主题，正如代码中通过 `Theme` 为第二行图标指定固定颜色（黑色）一样，这是一种常用的技巧，Flutter 中会经常使用这种方法来自定义子树主题。那么为什么局部主题可以覆盖全局主题？这主要是因为 widget 中使用主题样式时是通过 `Theme.of(BuildContext context)` 来获取的，我们看看其简化后的代码：

```dart
static ThemeData of(BuildContext context, { bool shadowThemeOnly = false }) {
   // 简化代码，并非源码  
   return context.dependOnInheritedWidgetOfExactType<_InheritedTheme>().theme.data
}
```

4. `context.dependOnInheritedWidgetOfExactType` 会在 widget 树中从当前位置向上查找第一个类型为 `_InheritedTheme` 的 widget。所以当局部指定 Theme 后，其子树中通过 `Theme.of()` 向上查找到的第一个 `_InheritedTheme` 便是我们指定的 Theme。
5. 本示例是对单个路由换肤，如果想要对整个应用换肤，则可以去修改 MaterialApp 的 `theme` 属性。

## 5、按需rebuild（ValueListenableBuilder）

### ①、ValueListenableBuilder

1. `InheritedWidget` 提供一种在 widget 树中从上到下共享数据的方式，但是也有很多场景数据流向并非从上到下，比如从下到上或者横向等。
2. 为了解决这个问题，Flutter 提供了一个 `ValueListenableBuilder` 组件，它的功能是监听一个数据源，如果数据源发生变化，则会重新执行其 builder，定义如下：

```dart
const ValueListenableBuilder({
  Key? key,
  /**
   * valueListenable：类型为 ValueListenable<T>，表示一个可监听的数据源。
   */
  required this.valueListenable,
  /**
   * builder：数据源发生变化通知时，会重新调用 builder 重新 build 子组件树。
   */
  required this.builder,
  /**
   * child: builder 中每次都会重新构建整个子组件树，
   * 如果子组件树中有一些不变的部分，可以传递给child，child 会作为 builder 的第三个参数传递给 builder，
   * 通过这种方式就可以实现组件缓存，原理和 AnimatedBuilder 第三个 child 相同。
   */
  this.child,
}
```

3. 可以发现 `ValueListenableBuilder` 和数据流向是无关的，只要数据源发生变化它就会重新构建子组件树，因此可以实现任意流向的数据共享。

### ②、实例

1. 我们依然实现一个计数器，记录点击次数：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/05_按需rebuild（ValueListenableBuilder）/01_ValueListenableBuilder.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: ValueListenableRoute()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ValueListenableRoute extends StatefulWidget {
  const ValueListenableRoute({Key? key}) : super(key: key);

  @override
  State<ValueListenableRoute> createState() => _ValueListenableState();
}

class _ValueListenableState extends State<ValueListenableRoute> {
  // 定义一个 ValueNotifier，当数字变化时会通知 ValueListenableBuilder
  final ValueNotifier<int> _counter = ValueNotifier<int>(0);
  // 定义一个缩放比例，用于调整字体大小
  static const double textScaleFactor = 1.5;

  @override
  Widget build(BuildContext context) {
    // 添加 + 按钮不会触发整个 ValueListenableRoute 组件的 build
    print('build');

    /**
     * Scaffold 是一个用于创建基本页面布局的小部件。
     * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
     * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
     */
    return Scaffold(
      // appBar 是 Scaffold 的一个属性，用于设置应用程序顶部的导航栏。
      appBar: AppBar(title: const Text('ValueListenableBuilder 测试')),
      /**
       * body: 用于定义页面的主要内容区域
       * Center 是一个小部件，用于将其子部件树对齐到屏幕中心
       */
      body: Center(
        // ValueListenableBuilder 是一个小部件，用于监听 ValueListenable 的变化，并根据变化来构建子部件树。
        child: ValueListenableBuilder<int>(
          builder: (BuildContext context, int value, Widget? child) {
            // builder 方法只会在 _counter 变化时被调用
            return Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                child!,
                Text('$value 次', textScaleFactor: textScaleFactor),
              ],
            );
          },
          // valueListenable 用于指定监听的 ValueListenable, 当 ValueListenable 变化时，builder 方法会被调用
          valueListenable: _counter,
          // 当子组件不依赖变化的数据，且子组件收件开销比较大时，指定 child 属性来缓存子组件非常有用
          child: const Text('点击了 ', textScaleFactor: textScaleFactor),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        // 点击后值 +1，触发 ValueListenableBuilder 重新构建
        onPressed: () => _counter.value += 1,
      ),
    );
  }
}
```

2. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画14.gif)

3. 可以看见，功能正常实现了，同时控制台只在页面打开时 build 了一次，点击 + 按钮的时候只是`ValueListenableBuilder` 重新构建了子组件树，而整个页面并没有重新 build ，因此日志面板只打印了一次  build  。
4. 因此尽可能让 `ValueListenableBuilder` 只构建依赖数据源的 `widget`，这样的话可以缩小重新构建的范围，也就是说 `ValueListenableBuilder` 的拆分粒度应该尽可能细。

## 6、异步 UI 更新（FutureBuilder、StreamBuilder）

1. 很多时候我们会依赖一些异步数据来动态更新 UI，比如在打开一个页面时我们需要先从互联网上获取数据，在获取数据的过程中我们显示一个加载框，等获取到数据时我们再渲染页面；
2. 又比如我们想展示 Stream（比如文件流、互联网数据接收流）的进度。
3. 当然，通过 `StatefulWidget` 我们完全可以实现上述这些功能。但由于在实际开发中依赖异步数据更新 UI 的这种场景非常常见，因此 Flutter 专门提供了 `FutureBuilder` 和 `StreamBuilder` 两个组件来快速实现这种功能

### ①、FutureBuilder

#### Ⅰ、介绍

1. `FutureBuilder` 会依赖一个 Future，它会根据所依赖的 Future 的状态来动态构建自身。
2. 我们看一下 FutureBuilder 构造函数：

```dart
FutureBuilder({
  /**
   * future：FutureBuilder 依赖的 Future，通常是一个异步耗时任务。
   */
  this.future,
  /**
   * initialData：初始数据，用户设置默认数据。
   */
  this.initialData,
  /**
   * builder：Widget 构建器；该构建器会在 Future 执行的不同阶段被多次调用，构建器签名如下：
   *    Function (BuildContext context, AsyncSnapshot snapshot)
   * snapshot 会包含当前异步任务的状态信息及结果信息，
   *    比如我们可以通过 snapshot.connectionState 获取异步任务的状态信息、
   *    通过 snapshot.hasError 判断异步任务是否有错误等等，完整的定义可以查看 AsyncSnapshot 类定义。
   */
  required this.builder,
})
```

3. 另外，`FutureBuilder` 的 `builder` 函数签名和 `StreamBuilder` 的 `builder` 是相同的

#### Ⅱ、示例

1. 我们实现一个路由，当该路由打开时我们从网上获取数据，获取数据时弹一个加载框；
2. 获取结束时，如果成功则显示获取到的数据，如果失败则显示错误。
3. 由于我们还没有介绍在 flutter 中如何发起网络请求，所以在这里我们不真正去网络请求数据，而是模拟一下这个过程，隔 2 秒后返回一个字符串：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/06_异步 UI 更新（FutureBuilder、StreamBuilder）/01_FutureBuilder.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: FutureBuilderComponent()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class FutureBuilderComponent extends StatefulWidget {
  const FutureBuilderComponent({Key? key}) : super(key: key);

  @override
  _FutureBuilderComponentState createState() => _FutureBuilderComponentState();
}

class _FutureBuilderComponentState extends State<FutureBuilderComponent> {
  // 刷新次数
  int _num = 1;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * Scaffold 是一个用于创建基本页面布局的小部件。
     * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
     * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
     */
    return Scaffold(
      /**
       * body: 用于定义页面的主要内容区域
       * Center 是一个小部件，用于将其子部件树对齐到屏幕中心
       */
      body: Center(
        // FutureBuilder 是一个小部件，用于根据异步请求的状态来动态构建 UI
        child: FutureBuilder<List<String>>(
          // future：用于接收一个 Future 对象，表示需要等待的异步任务
          future: _retrieveData(),
          // builder：用于接收一个 AsyncSnapshot 对象，表示对 future 的异步请求的状态快照
          builder: (BuildContext context, AsyncSnapshot<List<String>> snapshot) {
            // 请求已结束
            if (snapshot.connectionState == ConnectionState.done) {
              if (snapshot.hasError) {
                // 请求失败，显示错误
                return Text("Error: ${snapshot.error}");
              } else {
                // 请求成功，显示数据
                return ListView.builder(
                  // itemCount：列表项的数量，如果为 null，则为无限列表
                  itemCount: snapshot.data!.length,
                  // 强制高度为 50.0
                  itemExtent: 50.0,
                  /**
                   * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
                   * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
                   */
                  itemBuilder: (BuildContext context, int index) {
                    return Text(snapshot.data![index]);
                  }
                );
              }
            } else {
              // 请求未结束，显示 loading
              return const CircularProgressIndicator();
            }
          },
        ),
      ),
      /**
       * floatingActionButton：用于定义页面的浮动按钮
       */
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        // 点击按钮后，次数加 1，然后重新构建 UI
        onPressed: () => setState(() {
          _num++;
        }),
      ),
    );
  }

  Future<List<String>> _retrieveData() async {
    // 等待模拟的网络请求完成
    return Future.delayed(const Duration(seconds: 2), (){
      return List.generate(5, (index) => "第 $_num 次刷新、第 ${index + 1} 条数据");
    });
  }

}
```

4. 效果：

![|413](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画15.gif)

5. 注意：示例的代码中，每次组件重新 build 都会重新发起请求，因为每次的 `future` 都是新的，实践中我们通常会有一些缓存策略，常见的处理方式是在 `future` 成功后将 `future` 缓存，这样下次 build 时，就不会再重新发起异步任务。
6. 上面代码中我们在 builder 中根据当前异步任务状态 `ConnectionState` 来返回不同的 widget。`ConnectionState` 是一个枚举类，定义如下：

```dart
enum ConnectionState {
  /// 当前没有异步任务，比如[FutureBuilder]的[future]为null时
  none,

  /// 异步任务处于等待状态
  waiting,

  /// Stream处于激活状态（流上已经有数据传递了），对于FutureBuilder没有该状态。
  active,

  /// 异步任务已经终止.
  done,
}
```

7. 注意，`ConnectionState.active` 只在 `StreamBuilder` 中才会出现。

### ②、StreamBuilder

#### Ⅰ、介绍

1. 我们知道，在 `Dart` 中 `Stream` 也是用于接收异步事件数据，和 `Future` 不同的是，它可以接收多个异步操作的结果，它常用于会多次读取数据的异步任务场景，如网络内容下载、文件读写等。
2. `StreamBuilder` 正是用于配合 `Stream` 来展示流上事件（数据）变化的 UI 组件。
3. 下面看一下 `StreamBuilder` 的默认构造函数：

```dart
StreamBuilder({
  this.initialData,
  Stream<T> stream,
  required this.builder,
}) 
```

4. 可以看到和 `FutureBuilder` 的构造函数只有一点不同：前者需要一个 `future`，而后者需要一个 `stream`。

#### Ⅱ、示例

1. 我们创建一个计时器的示例：每隔 1 秒，计数加 1。
2. 这里，我们使用 `Stream` 来实现每隔一秒生成一个数字：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/06_异步 UI 更新（FutureBuilder、StreamBuilder）/02_StreamBuilder.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: StreamBuilderComponent()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class StreamBuilderComponent extends StatefulWidget {
  const StreamBuilderComponent({Key? key}) : super(key: key);

  @override
  _StreamBuilderComponentState createState() => _StreamBuilderComponentState();
}

class _StreamBuilderComponentState extends State<StreamBuilderComponent> {
  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    /**
     * StreamBuilder 是一个用于构建异步数据流的小部件。
     * 它提供了一个小部件来订阅数据流，并根据数据流中的数据来构建 UI。
     */
    return StreamBuilder<int>(
      // stream 参数用于接收一个 Stream 对象，用于订阅数据流
      stream: counter(),
      // builder 用于接收一个回调函数，snapshot 参数用于接收数据流中的数据
      builder: (BuildContext context, AsyncSnapshot<int> snapshot){
        // snapshot.hasError 用于判断数据流中是否有错误
        if (snapshot.hasError){
          return Text('Error: ${snapshot.error}');
        }

        switch (snapshot.connectionState) {
          // ConnectionState.none 表示没有 Stream
          case ConnectionState.none:
            return const Text('没有Stream');
          // ConnectionState.waiting 表示正在等待数据
          case ConnectionState.waiting:
            return const Text('等待数据...');
          // ConnectionState.active 表示正在接收数据
          case ConnectionState.active:
            return Text('active: ${snapshot.data}');
          // ConnectionState.done 表示 Stream 已关闭
          case ConnectionState.done:
            return const Text('Stream 已关闭');
        }
      },
    );
  }

  Stream<int> counter() {
    return Stream.periodic(const Duration(seconds: 1), (i) {
      return i;
    });
  }

}
```

3. 效果：

![|413](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画16.gif)

## 7、对话框详解

### ①、使用对话框

1. 对话框本质上也是 UI 布局，通常一个对话框会包含标题、内容，以及一些操作按钮，
2. 为此，Material 库中提供了一些现成的对话框组件来用于快速的构建出一个完整的对话框。

#### Ⅰ、AlertDialog

1. 下面我们主要介绍一下 Material 库中的 `AlertDialog` 组件，它的构造函数定义如下：

```dart
const AlertDialog({
  Key? key,
  this.title, //对话框标题组件
  this.titlePadding, // 标题填充
  this.titleTextStyle, //标题文本样式
  this.content, // 对话框内容组件
  this.contentPadding = const EdgeInsets.fromLTRB(24.0, 20.0, 24.0, 24.0), //内容的填充
  this.contentTextStyle,// 内容文本样式
  this.actions, // 对话框操作按钮组
  this.backgroundColor, // 对话框背景色
  this.elevation,// 对话框的阴影
  this.semanticLabel, //对话框语义化标签(用于读屏软件)
  this.shape, // 对话框外形
})
```

2. 下面我们看一个例子，点击按钮后弹出一个对话框：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/01_使用对话框/01_AlertDialog.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: AlertDialogComponent()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class AlertDialogComponent extends StatefulWidget {
  const AlertDialogComponent({Key? key}) : super(key: key);

  @override
  _AlertDialogComponentState createState() => _AlertDialogComponentState();
}

class _AlertDialogComponentState extends State<AlertDialogComponent> {
  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 AlertDialog 对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  // 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          content: const Text("请点击确认按钮进行确认\n请点击取消按钮进行取消"),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: const Text("确认"),
              // 关闭对话框并返回 true
              onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

}
```

3. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画17.gif)

4. 示例运行后，我们点击对话框“取消”按钮或遮罩，控制台就会输出"点击了取消"，如果点击“确定”按钮，控制台就会输出"点击了确定"。
5. 注意：如果 `AlertDialog` 的内容过长，内容将会溢出，这在很多时候可能不是我们期望的，所以如果对话框内容过长时，可以用 `SingleChildScrollView` 将内容包裹起来。

#### Ⅱ、SimpleDialog

1. `SimpleDialog` 也是 Material 组件库提供的对话框，它会展示一个列表，用于列表选择的场景。
2. 下面是一个示例：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/01_使用对话框/01_AlertDialog.dart';
import '05_功能型组件/07_对话框详解/01_使用对话框/02_SimpleDialog.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: SimpleDialogComponent()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class SimpleDialogComponent extends StatefulWidget {
  const SimpleDialogComponent({Key? key}) : super(key: key);

  @override
  _SimpleDialogComponentState createState() => _SimpleDialogComponentState();
}

class _SimpleDialogComponentState extends State<SimpleDialogComponent> {
  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showSimpleDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<int?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 SimpleDialog 对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        int? result = await dialog();
        switch(result){
          case 1:
            print("选择了中文");
            break;
          case 2:
            print("选择了英语");
            break;
          case 3:
            print("选择了日语");
            break;
        }
      },
    );
  }

  // 弹出对话框
  Future<int?> showSimpleDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<int>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return SimpleDialog(
          title: const Text("请选择语言"),
          children: [
            SimpleDialogOption(
              child: const Text("中文"),
              // 关闭对话框并返回 1
              onPressed: () => Navigator.of(context).pop(1)
            ),
            SimpleDialogOption(
              child: const Text("英语"),
              // 关闭对话框并返回 2
              onPressed: () => Navigator.of(context).pop(2)
            ),
            SimpleDialogOption(
              child: const Text("日语"),
              // 关闭对话框并返回 3
              onPressed: () => Navigator.of(context).pop(3)
            ),
          ],
        );
      },
    );
  }

}
```

3. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画18.gif)

4. 列表项组件我们使用了 `SimpleDialogOption` 组件来包装了一下，它相当于一个 `TextButton`，只不过按钮文案是左对齐的，并且 `padding` 较小

#### Ⅲ、Dialog

1. 实际上 `AlertDialog` 和 `SimpleDialog` 都使用了 `Dialog` 类。
2. 由于 `AlertDialog` 和 `SimpleDialog` 中使用了 `IntrinsicWidth` 来尝试通过子组件的实际尺寸来调整自身尺寸，这就导致他们的子组件不能是延迟加载模型的组件（如 `ListView`、`GridView` 、 `CustomScrollView` 等），如下面的代码运行后会报错。

```dart
AlertDialog(
  content: ListView(
    children: ... //省略
  ),
);
```

3. 如果我们就是需要嵌套一个 `ListView` 应该怎么做？这时，我们可以直接使用 `Dialog` 类，如：

```dart
Dialog(
  child: ListView(
    children: ... //省略
  ),
);
```

4. 下面我们看一个弹出一个有 30 个列表项的对话框示例：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/01_使用对话框/03_Dialog.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: DialogComponent()
        )
      )
    );
  }
}
```

```dart
import 'package:flutter/material.dart';

class DialogComponent extends StatefulWidget {
  const DialogComponent({Key? key}) : super(key: key);

  @override
  _DialogComponentState createState() => _DialogComponentState();
}

class _DialogComponentState extends State<DialogComponent> {
  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      child: buildElevatedButton(showListDialog),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<int?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 List Dialog 对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        int? result = await dialog();
        if(result == null){
          print('未选择选项');
        }else {
          print('点击了对话框列表的第 $result 个选项');
        }
      },
    );
  }

  // 弹出对话框
  Future<int?> showListDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<int>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        return Dialog(
          child: buildListDialog(),
        );
      },
    );
  }

  Widget buildListDialog(){
    // Column 是一个用于在垂直方向上排列其子部件的小部件
    return Column(
        children: [
          // ListTile 是一个用于在列表中显示一个固定样式的行的小部件
          const ListTile(title: Text("请选择")),
          // Expanded 是一个可以用来包裹子 Widget 的小部件，它会将子 Widget 沿着父部件的垂直方向拉伸并填充满父部件
          Expanded(
            // Scrollbar 是一个小部件，用于为可滚动的子部件添加滚动条
            child: Scrollbar(
              // ListView 是一个用于显示列表的小部件
              child: ListView.builder(
                // itemCount：列表项的数量
                itemCount: 30,
                /**
                 * itemBuilder 是一个回调函数，它用于构建 ListView.builder 中的每个列表项。
                 * 当 ListView.builder 需要构建一个新的列表项时，它会调用 itemBuilder 函数，并传入当前的 BuildContext 和列表项的索引 index
                 */
                itemBuilder: (BuildContext context, int index) {
                  return ListTile(
                    title: Text("$index"),
                    // onTap：点击事件，点击后关闭对话框并返回当前列表项的索引 index
                    onTap: () => Navigator.of(context).pop(index),
                  );
                },
              ),
            )

          ),
        ],
      );
  }

}
```

5. 运行效果如图所示：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画19.gif)

### ②、对话框打开动画及遮罩

1. 我们可以把对话框分为内部样式和外部样式两部分。
2. 内部样式指对话框中显示的具体内容，这部分内容我们已经在上面介绍过了；外部样式包含对话框遮罩样式、打开动画等，本节主要介绍如何自定义这些外部样式。
3. 关于动画相关内容我们将在第十章中详细介绍，下面内容可以先了解一下（不必深究），可以在学习完动画相关内容后再回头来看。
4. 我们已经介绍过了 `showDialog` 方法，它是 Material 组件库中提供的一个打开 Material 风格对话框的方法。那如何打开一个普通风格的对话框呢（非 Material 风格）？ Flutter 提供了一个 `showGeneralDialog` 方法，签名如下：

```dart
Future<T?> showGeneralDialog<T>({
  required BuildContext context,
  required RoutePageBuilder pageBuilder, //构建对话框内部UI
  bool barrierDismissible = false, //点击遮罩是否关闭对话框
  String? barrierLabel, // 语义化标签(用于读屏软件)
  Color barrierColor = const Color(0x80000000), // 遮罩颜色
  Duration transitionDuration = const Duration(milliseconds: 200), // 对话框打开/关闭的动画时长
  RouteTransitionsBuilder? transitionBuilder, // 对话框打开/关闭的动画
  ...
})
```

5. 实际上，`showDialog` 方法正是 `showGeneralDialog` 的一个封装，定制了 Material 风格对话框的遮罩颜色和动画。Material 风格对话框打开/关闭动画是一个 Fade（渐隐渐显）动画，如果我们想使用一个缩放动画就可以通过 `transitionBuilder` 来自定义。
6. 下面我们自己封装一个 `showCustomDialog` 方法，它定制的对话框动画为缩放动画，并同时制定遮罩颜色为 `Colors.black87`：
7. `mian` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/02_对话框打开动画及遮罩/02_CustomDialogView.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: CustomDialogViewComponent()
        )
      )
    );
  }
}
```

8. `01_CustomDialog.dart` 自定义对话框打开动画及遮罩类

```dart
import 'package:flutter/material.dart';

// 自定义对话框打开动画及遮罩类
class CustomDialog {

  // 自定义对话框打开动画及遮罩方法
  Future<T?> showCustomDialog<T>({
    // context 是一个 BuildContext，表示当前 Widget 的位置
    required BuildContext context,
    // barrierDismissible：点击遮罩是否关闭对话框
    bool barrierDismissible = true,
    // builder 是一个回调函数，返回一个 Widget
    required WidgetBuilder builder,
    // theme：对话框使用的主题
    ThemeData? theme,
  }) {
    // 如果没有传入 theme，则使用默认的主题
    theme = theme ?? Theme.of(context);
    // showGeneralDialog 是一个用于显示对话框的方法
    return showGeneralDialog(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      /**
       * pageBuilder 是一个回调函数，返回一个 Widget
       * 该回调函数接收三个参数：
       * 1、BuildContext：构建上下文，即当前 Widget 的位置
       * 2、Animation<double>：动画对象，用于控制对话框的动画
       * 3、Animation<double>：动画对象，用于控制对话框打开时遮罩的动画
       */
      pageBuilder: (BuildContext buildContext, Animation<double> animation, Animation<double> secondaryAnimation) {
        final Widget pageChild = Builder(builder: builder);
        // SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
        return SafeArea(
          child: Builder(builder: (BuildContext context) {
            return theme != null ? Theme(data: theme, child: pageChild): pageChild;
          }),
        );
      },
      // barrierDismissible 表示点击遮罩是否关闭对话框
      barrierDismissible: barrierDismissible,
      // barrierLabel：遮罩的语义化标签，用于向屏幕阅读器传递语义信息
      barrierLabel: MaterialLocalizations.of(context).modalBarrierDismissLabel,
      // barrierColor：遮罩的颜色
      barrierColor: Colors.black87,
      // transitionDuration：对话框打开/关闭的动画时长
      transitionDuration: const Duration(milliseconds: 150),
      // transitionBuilder：对话框打开/关闭的动画
      transitionBuilder: _buildMaterialDialogTransitions,
    );
  }

  // 对话框打开/关闭的动画
  Widget _buildMaterialDialogTransitions(
    // context：构建上下文，即当前 Widget 的位置
    BuildContext context,
    // animation：动画对象，用于控制对话框的动画
    Animation<double> animation,
    // secondaryAnimation：动画对象，用于控制对话框打开时遮罩的动画
    Animation<double> secondaryAnimation,
    Widget child
  ) {
    // 使用缩放动画
    return ScaleTransition(
      // 动画对象，用于控制对话框的动画；CurvedAnimation：动画曲线，用于控制动画的执行速度
      scale: CurvedAnimation(
        // 父动画，即对话框打开/关闭的动画
        parent: animation,
        // 动画曲线，用于控制动画的执行速度；Curves.easeOut：快出慢进，动画结束时减速
        curve: Curves.easeOut,
      ),
      child: child,
    );
  }
}
```

9. `02_CustomDialogView.dart` 使用自定义对话框打开动画及遮罩类

```dart
import 'package:flutter/material.dart';

import '01_CustomDialog.dart';

class CustomDialogViewComponent extends StatefulWidget {
  const CustomDialogViewComponent({Key? key}) : super(key: key);

  @override
  _CustomDialogViewComponentState createState() => _CustomDialogViewComponentState();
}

class _CustomDialogViewComponentState extends State<CustomDialogViewComponent> {
  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 自定义 对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  // 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return CustomDialog().showCustomDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          content: const Text("请点击确认按钮进行确认\n请点击取消按钮进行取消"),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
                child: const Text("确认"),
                // 关闭对话框并返回 true
                onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

}
```

10. 效果：

![|411](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画20.gif)

### ③、对话框实现原理

1. 我们以 `showGeneralDialog` 方法为例来看看它的具体实现：

```dart
Future<T?> showGeneralDialog<T extends Object?>({
  required BuildContext context,
  required RoutePageBuilder pageBuilder,
  bool barrierDismissible = false,
  String? barrierLabel,
  Color barrierColor = const Color(0x80000000),
  Duration transitionDuration = const Duration(milliseconds: 200),
  RouteTransitionsBuilder? transitionBuilder,
  bool useRootNavigator = true,
  RouteSettings? routeSettings,
}) {
  return Navigator.of(context, rootNavigator: useRootNavigator).push<T>(RawDialogRoute<T>(
    pageBuilder: pageBuilder,
    barrierDismissible: barrierDismissible,
    barrierLabel: barrierLabel,
    barrierColor: barrierColor,
    transitionDuration: transitionDuration,
    transitionBuilder: transitionBuilder,
    settings: routeSettings,
  ));
}
```

2. 实现很简单，直接调用 `Navigator` 的 `push` 方法打开了一个新的对话框路由 `RawDialogRoute`，然后返回了 `push` 的返回值。
3. 可见对话框实际上正是通过路由的形式实现的，这也是为什么我们可以使用 `Navigator` 的 `pop` 方法来退出对话框的原因。

### ④、对话框状态管理

#### Ⅰ、问题引出

1. 我们在用户选择删除一个文件时，会询问是否删除此文件；在用户选择一个文件夹是，应该再让用户确认是否删除子文件夹。
2. 为了在用户选择了文件夹时避免二次弹窗确认是否删除子目录，我们在确认对话框底部添加一个“同时删除子目录？”的复选框，如图所示：

![|320](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231121132353.png)

3. 现在就有一个问题：如何管理复选框的选中状态？习惯上，我们会在路由页的 `State` 中来管理选中状态，我们可能会写出如下这样的代码：

```dart
class _DialogRouteState extends State<DialogRoute> {
  bool withTree = false; // 复选框选中状态

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        ElevatedButton(
          child: Text("对话框2"),
          onPressed: () async {
            bool? delete = await showDeleteConfirmDialog2();
            if (delete == null) {
              print("取消删除");
            } else {
              print("同时删除子目录: $delete");
            }
          },
        ),
      ],
    );
  }

  Future<bool?> showDeleteConfirmDialog2() {
    withTree = false; // 默认复选框不选中
    return showDialog<bool>(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text("提示"),
          content: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              Text("您确定要删除当前文件吗?"),
              Row(
                children: <Widget>[
                  Text("同时删除子目录？"),
                  Checkbox(
                    value: withTree,
                    onChanged: (bool value) {
                      //复选框选中状态发生变化时重新构建UI
                      setState(() {
                        //更新复选框状态
                        withTree = !withTree;
                      });
                    },
                  ),
                ],
              ),
            ],
          ),
          actions: <Widget>[
            TextButton(
              child: Text("取消"),
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: Text("删除"),
              onPressed: () {
                //执行删除操作
                Navigator.of(context).pop(withTree);
              },
            ),
          ],
        );
      },
    );
  }
}
```

4. 然后，当我们运行上面的代码时我们会发现复选框根本选不中！为什么会这样呢？其实原因很简单，我们知道 `setState` 方法只会针对当前 `context` 的子树重新 build，但是我们的对话框并不是在 `_DialogRouteState` 的 `build` 方法中构建的，而是通过 `showDialog` 单独构建的，所以在 `_DialogRouteState` 的 `context` 中调用 `setState` 是无法影响通过 `showDialog` 构建的 UI 的。
5. 另外，我们可以从另外一个角度来理解这个现象，前面说过对话框也是通过路由的方式来实现的，那么上面的代码实际上就等同于企图在父路由中调用 `setState` 来让子路由更新，这显然是不行的！
6. 简尔言之，根本原因就是 `context` 不对。那如何让复选框可点击呢？通常有如下三种方法：

#### Ⅱ、单独抽离出 StatefulWidget

1. 既然是 context 不对，那么直接的思路就是将复选框的选中逻辑单独封装成一个 `StatefulWidget`，然后在其内部管理复选状态。
2. 我们先来看看这种方法，下面是实现代码：
3. `main` 主方法：

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/04_对话框状态管理/01_2_AlertDialogCheckbox.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: AlertDialogCheckboxComponent()
        )
      )
    );
  }
}
```

4. `01_1_DialogCheckbox.dart` 抽取的复选框：

```dart
import 'package:flutter/material.dart';

// 单独封装一个内部管理选中状态的复选框组件
class DialogCheckbox extends StatefulWidget {
  const DialogCheckbox({Key? key, this.value, required this.onChanged}): super(key: key);

  /// 选中状态改变事件
  final ValueChanged<bool?> onChanged;
  /// 选中状态
  final bool? value;

  @override
  _DialogCheckboxState createState() => _DialogCheckboxState();
}

class _DialogCheckboxState extends State<DialogCheckbox> {
  /// _DialogCheckboxState 中的 value 是一个私有的布尔值，表示内部管理的复选框的选中状态
  /// _DialogCheckboxState 中的 value 变量在 initState 中初始化为 DialogCheckbox 组件传递的 value 值，
  /// 然后在复选框状态改变时更新，并通过 onChanged 事件回传给 DialogCheckbox 组件
  bool? value;

  @override
  void initState() {
    // 初始化选中状态
    value = widget.value;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    // 返回一个复选框组件
    return Checkbox(
      // 复选框的选中状态；true：选中，false：未选中
      value: value,
      // 复选框选中状态改变事件
      onChanged: (v) {
        // 将选中状态通过事件的形式抛出
        widget.onChanged(v);
        setState(() {
          // 更新自身选中状态
          value = v;
          print('复选框选中状态：$value');
        });
      },
    );
  }
}
```

5. `01_2_AlertDialogCheckbox.dart` 弹窗方法：

```dart
import 'package:flutter/material.dart';

import '01_1_DialogCheckbox.dart';

class AlertDialogCheckboxComponent extends StatefulWidget {
  const AlertDialogCheckboxComponent({Key? key}) : super(key: key);

  @override
  _AlertDialogCheckboxComponentState createState() => _AlertDialogCheckboxComponentState();
}

class _AlertDialogCheckboxComponentState extends State<AlertDialogCheckboxComponent> {
  // 记录复选框是否选中
  bool _withTree = false;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 带有复选框的对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  // 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          // content 通常显示对话框的主要内容；Column 是一个用于在垂直方向上排列其子部件的小部件
          content: buildConfirmDialogContent(),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: const Text("确认"),
              // 关闭对话框并返回 true
              onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

  Widget buildConfirmDialogContent() {
    // Column 是一个用于在垂直方向上排列其子部件的小部件
    return Column(
      // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小垂直方向上的高度
      mainAxisSize: MainAxisSize.min,
      // 表示子部件在水平方向上如何排列；CrossAxisAlignment.start：子部件在水平方向上从左到右排列
      crossAxisAlignment:  CrossAxisAlignment.start,
      children: [
        const Text("您确定要删除当前文件吗？"),
        // Row 是一个用于在水平方向上排列其子部件的小部件
        Row(
          // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小水平方向上的宽度
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("是否确认："),
            DialogCheckbox(
              value: _withTree,
              onChanged: (v) {
                setState(() {
                  _withTree = !_withTree;
                });
              },
            )
          ],
        )
      ],
    );
  }

}
```

6. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画21.gif)

#### Ⅲ、使用 StatefulBuilder 方法

1. 上面的方法虽然能解决对话框状态更新的问题，但是有一个明显的缺点：对话框上所有可能会改变状态的组件都得单独封装在一个在内部管理状态的 `StatefulWidget` 中，这样不仅麻烦，而且复用性不大。因此，我们来想想能不能找到一种更简单的方法？
2. 上面的方法本质上就是将对话框的状态置于一个 `StatefulWidget` 的上下文中，由 `StatefulWidget` 在内部管理，那么我们有没有办法在不需要单独抽离组件的情况下创建一个 `StatefulWidget` 的上下文呢？想到这里，我们可以从 Builder 组件的实现获得灵感。在前面介绍过 Builder 组件可以获得组件所在位置的真正的 `Context`，那它是怎么实现的呢，我们看看它的源码：

```dart
class Builder extends StatelessWidget {
  const Builder({
    Key? key,
    required this.builder,
  }) : assert(builder != null),
       super(key: key);
  final WidgetBuilder builder;

  @override
  Widget build(BuildContext context) => builder(context);
}
```

3. 可以看到，Builder 实际上只是继承了 `StatelessWidget`，然后在 build 方法中获取当前 `context` 后将构建方法代理到了 builder 回调，可见，Builder 实际上是获取了 `StatelessWidget` 的上下文（context）。
4. 那么我们能否用相同的方法获取 `StatefulWidget` 的上下文，并代理其 `build` 方法呢？下面我们照猫画虎，来封装一个 `StatefulBuilder` 方法 `02_1_StatefulBuilder.dart`：

```dart
import 'package:flutter/cupertino.dart';

class StatefulBuilder extends StatefulWidget {
  const StatefulBuilder({Key? key, required this.builder}) : super(key: key);

  final StatefulWidgetBuilder builder;

  @override
  _StatefulBuilderState createState() => _StatefulBuilderState();
}

class _StatefulBuilderState extends State<StatefulBuilder> {
  @override
  Widget build(BuildContext context) => widget.builder(context, setState);
}
```

5. 代码很简单，`StatefulBuilder` 获取了 `StatefulWidget` 的上下文，并代理了其构建过程。下面我们就可以通过 `StatefulBuilder` 来重构上面的代码了（变动只在 `DialogCheckbox` 部分） `02_2_AlertDialogCheckbox.dart` ：

```dart
import 'package:flutter/material.dart';

import '01_1_DialogCheckbox.dart';

class AlertDialogCheckboxComponent extends StatefulWidget {
  const AlertDialogCheckboxComponent({Key? key}) : super(key: key);

  @override
  _AlertDialogCheckboxComponentState createState() => _AlertDialogCheckboxComponentState();
}

class _AlertDialogCheckboxComponentState extends State<AlertDialogCheckboxComponent> {
  // 记录复选框是否选中
  bool _withTree = false;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 带有复选框的对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  // 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          // content 通常显示对话框的主要内容；Column 是一个用于在垂直方向上排列其子部件的小部件
          content: buildConfirmDialogContent(),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: const Text("确认"),
              // 关闭对话框并返回 true
              onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

  Widget buildConfirmDialogContent() {
    // Column 是一个用于在垂直方向上排列其子部件的小部件
    return Column(
      // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小垂直方向上的高度
      mainAxisSize: MainAxisSize.min,
      // 表示子部件在水平方向上如何排列；CrossAxisAlignment.start：子部件在水平方向上从左到右排列
      crossAxisAlignment:  CrossAxisAlignment.start,
      children: [
        const Text("您确定要删除当前文件吗？"),
        // Row 是一个用于在水平方向上排列其子部件的小部件
        Row(
          // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小水平方向上的宽度
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("是否确认："),
            StatefulBuilder(
              builder: (context, _setState){
                return Checkbox(
                  // value：是否选中；_withTree：记录复选框是否选中
                  value: _withTree,
                  // onChanged：复选框的值发生改变时的回调函数
                  onChanged: (bool? value) {
                    // 调用 setState() 更新复选框的选中状态
                    _setState(() {
                      // 更新复选框的选中状态
                      _withTree = !_withTree;
                      print('复选框选中状态：$value');
                    });
                  },
                );
              }
            )
          ],
        )
      ],
    );
  }

}
```

6. 实际上，这种方法本质上就是子组件通知父组件（StatefulWidget）重新 build 子组件本身来实现 UI 更新的
7. 实际上 `StatefulBuilder` 正是 Flutter SDK 中提供的一个类，它和 Builder 的原理是一样的，在此，提醒一定要将 `StatefulBuilder` 和 `Builder` 理解透彻，因为它们在 Flutter 中是非常实用的

#### Ⅳ、使用 element.markNeedsBuild()

1. 是否还有更简单的解决方案呢？要确认这个问题，我们就得先搞清楚 UI 是怎么更新的，我们知道在调用 `setState` 方法后 `StatefulWidget` 就会重新 build，那 `setState` 方法做了什么呢？我们能不能从中找到方法？顺着这个思路，我们就得看一下 `setState` 的核心源码：

```dart
void setState(VoidCallback fn) {
  ... //省略无关代码
  _element.markNeedsBuild();
}
```

2. 可以发现，`setState` 中调用了 Element 的 `markNeedsBuild()` 方法，我们前面说过，Flutter 是一个响应式框架，要更新 UI 只需改变状态后通知框架页面需要重构即可，而 Element 的 `markNeedsBuild()` 方法正是来实现这个功能的！
3. `markNeedsBuild()` 方法会将当前的 Element 对象标记为 “dirty”（脏的），在每一个 Frame，Flutter 都会重新构建被标记为 “dirty” 的 Element 对象。
4. 既然如此，我们有没有办法获取到对话框内部 UI 的 Element 对象，然后将其标示为为 “dirty” 呢？答案是肯定的！我们可以通过 Context 来得到 Element 对象，至于 Element 与 Context 的关系我们将会在后面 “Flutter核心原理” 一章中再深入介绍，现在只需要简单的认为：在组件树中，`context` 实际上就是 Element 对象的引用。
5. 知道这个后，那么解决的方案就呼之欲出了，我们可以通过如下方式来让复选框可以更新：

```dart
import 'package:flutter/material.dart';

import '01_1_DialogCheckbox.dart';

class AlertDialogCheckboxComponent extends StatefulWidget {
  const AlertDialogCheckboxComponent({Key? key}) : super(key: key);

  @override
  _AlertDialogCheckboxComponentState createState() => _AlertDialogCheckboxComponentState();
}

class _AlertDialogCheckboxComponentState extends State<AlertDialogCheckboxComponent> {
  // 记录复选框是否选中
  bool _withTree = false;

  // 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  // 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 带有复选框的对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  // 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          // content 通常显示对话框的主要内容；Column 是一个用于在垂直方向上排列其子部件的小部件
          content: buildConfirmDialogContent(context),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: const Text("确认"),
              // 关闭对话框并返回 true
              onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

  Widget buildConfirmDialogContent(BuildContext context) {
    // Column 是一个用于在垂直方向上排列其子部件的小部件
    return Column(
      // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小垂直方向上的高度
      mainAxisSize: MainAxisSize.min,
      // 表示子部件在水平方向上如何排列；CrossAxisAlignment.start：子部件在水平方向上从左到右排列
      crossAxisAlignment:  CrossAxisAlignment.start,
      children: [
        const Text("您确定要删除当前文件吗？"),
        // Row 是一个用于在水平方向上排列其子部件的小部件
        Row(
          // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小水平方向上的宽度
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("是否确认："),
            Checkbox(
              // value：是否选中；_withTree：记录复选框是否选中
              value: _withTree,
              // onChanged：复选框的值发生改变时的回调函数
              onChanged: (bool? value) {
                // 更新复选框的选中状态
                _withTree = !_withTree;
                /**
                 * 此时 context 为对话框 UI 的根 Element，
                 * 我们直接将对话框 UI 对应的 Element 标记为 dirty 即可
                 * 之后框架会调用对话框 UI 的 build 方法来根据新状态重新构建对话框 UI
                 */
                (context as Element).markNeedsBuild();
                print('复选框选中状态：$value');
              },
            )
          ],
        )
      ],
    );
  }

}
```

6. 上面的代码运行后复选框也可以正常选中。可以看到，我们只用了一行代码便解决了这个问题！当然上面的代码并不是最优，因为我们只需要更新复选框的状态，而此时的 context 我们用的是对话框的根 `context`，所以会导致整个对话框 UI 组件全部 rebuild，因此最好的做法是将 context 的“范围”缩小，也就是说只将 `Checkbox` 的 `Element` 标记为 dirty，优化后的代码为：
7. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/04_对话框状态管理/03_AlertDialogCheckbox.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: AlertDialogCheckboxComponent()
        )
      )
    );
  }
}
```

8. `03_AlertDialogCheckbox.dart` 弹窗方法

```dart
import 'package:flutter/material.dart';

import '01_1_DialogCheckbox.dart';

class AlertDialogCheckboxComponent extends StatefulWidget {
  const AlertDialogCheckboxComponent({Key? key}) : super(key: key);

  @override
  _AlertDialogCheckboxComponentState createState() => _AlertDialogCheckboxComponentState();
}

class _AlertDialogCheckboxComponentState extends State<AlertDialogCheckboxComponent> {
  /// 记录复选框是否选中
  bool _withTree = false;

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  /// 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<bool?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 带有复选框的对话框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        bool? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了确定");
        }
      },
    );
  }

  /// 弹出对话框
  Future<bool?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<bool>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        // AlertDialog 是一个用于显示对话框的小部件
        return AlertDialog(
          title: const Text("提示"),
          // content 通常显示对话框的主要内容；Column 是一个用于在垂直方向上排列其子部件的小部件
          content: buildConfirmDialogContent(),
          // actions 是一个 Widget 列表，用于显示对话框的按钮；通常用于放置“取消”和“确认”按钮
          actions: <Widget>[
            TextButton(
              child: const Text("取消"),
              // 关闭对话框并返回 null
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: const Text("确认"),
              // 关闭对话框并返回 true
              onPressed: () => Navigator.of(context).pop(true)
            ),
          ],
        );
      },
    );
  }

  Widget buildConfirmDialogContent() {
    // Column 是一个用于在垂直方向上排列其子部件的小部件
    return Column(
      // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小垂直方向上的高度
      mainAxisSize: MainAxisSize.min,
      // 表示子部件在水平方向上如何排列；CrossAxisAlignment.start：子部件在水平方向上从左到右排列
      crossAxisAlignment:  CrossAxisAlignment.start,
      children: [
        const Text("您确定要删除当前文件吗？"),
        // Row 是一个用于在水平方向上排列其子部件的小部件
        Row(
          // mainAxisSize：主轴尺寸；MainAxisSize.min：尽可能小，即尽可能缩小水平方向上的宽度
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("同时删除子目录？"),
            buildDeleteSubdirectoryCheckbox()
          ],
        )
      ],
    );
  }

  /// 构建 是否同时删除子目录复选框
  Widget buildDeleteSubdirectoryCheckbox(){
    /**
     * 此处 Builder 的作用是为了通过 context 获取 Element，
     * 使其可以通过 markNeedsBuild 方法来间接实现局部刷新
     * 而不是重新构建整个对话框 UI
     */
    return Builder(
      builder: (BuildContext context){
        return Checkbox(
          // value：是否选中；_withTree：记录复选框是否选中
          value: _withTree,
          // onChanged：复选框的值发生改变时的回调函数
          onChanged: (bool? value) {
            // 更新复选框的选中状态
            _withTree = !_withTree;
            /**
             * 此时 context 为对话框 UI 的根 Element，
             * 我们直接将对话框 UI 对应的 Element 标记为 dirty 即可
             * 之后框架会调用对话框 UI 的 build 方法来根据新状态重新构建对话框 UI
             */
            (context as Element).markNeedsBuild();
            print('复选框选中状态：$value');
          },
        );
      }
    );
  }

}
```

### ⑤、其他类型的对话框

#### Ⅰ、底部菜单列表

1. `showModalBottomSheet` 方法可以弹出一个 Material 风格的底部菜单列表模态对话框，示例如下：
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/05_其他类型的对话框/01_底部菜单列表.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: ShowModalBottomSheetComponent()
            )
        )
    );
  }
}
```

3. `01_底部菜单列表.dart` 弹窗方法

```dart
import 'package:flutter/material.dart';


class ShowModalBottomSheetComponent extends StatefulWidget {
  const ShowModalBottomSheetComponent({Key? key}) : super(key: key);

  @override
  _ShowModalBottomSheetComponentState createState() => _ShowModalBottomSheetComponentState();
}

class _ShowModalBottomSheetComponentState extends State<ShowModalBottomSheetComponent> {
  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  /// 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<int?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 底部菜单列表"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        int? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了第 $result 个条目");
        }
      },
    );
  }

  /// 弹出对话框
  Future<int?> showConfirmDialog() {
    // showModalBottomSheet 是一个用于显示底部菜单列表的方法
    return showModalBottomSheet<int>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        return buildListViewDialog();
      },
    );
  }

  /// 构建 ListView 对话框
  Widget buildListViewDialog() {
    // ListView.builder 是一个用于构建列表的构造方法
    return ListView.builder(
      // itemCount：列表项的数量
      itemCount: 30,
      itemBuilder: (BuildContext context, int index) {
        return ListTile(
          title: Text("$index"),
          onTap: () => Navigator.of(context).pop(index),
        );
      },
    );
  }

}
```

4. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画22.gif)

#### Ⅱ、Loading 框

1. 其实 Loading 框可以直接通过 `showDialog` + `AlertDialog` 来自定义：
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/05_其他类型的对话框/02_Loading 框.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: LoadingDialogComponent()
            )
        )
    );
  }
}
```

3. `02_Loading 框.dart` 弹窗方法

```dart
import 'package:flutter/material.dart';


class LoadingDialogComponent extends StatefulWidget {
  const LoadingDialogComponent({Key? key}) : super(key: key);

  @override
  _LoadingDialogComponentState createState() => _LoadingDialogComponentState();
}

class _LoadingDialogComponentState extends State<LoadingDialogComponent> {
  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  /// 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<int?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 Loading 加载框"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        int? result = await dialog();
        if (result == null) {
          print("点击了取消");
        } else {
          print("点击了第 $result 个条目");
        }
      },
    );
  }

  /// 弹出对话框
  Future<int?> showConfirmDialog() {
    // showDialog 是一个用于显示对话框的方法
    return showDialog<int>(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // builder 是一个回调函数，返回一个 Widget
      builder: (context) {
        return buildLoadingDialog();
      },
    );
  }

  /// 构建 ListView 对话框
  Widget buildLoadingDialog() {
    // AlertDialog 是一个用于显示对话框的小部件
    return const AlertDialog(
      // content 是 AlertDialog 的一个属性，用于设置对话框的内容； Column 是一个用于在垂直方向上排列其子部件的小部件
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          // CircularProgressIndicator 是一个圆形的进度条
          CircularProgressIndicator(),
          Padding(
            padding: EdgeInsets.only(top: 26.0),
            child: Text("正在加载，请稍后..."),
          )
        ],
      ),
    );
  }

}
```

4. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画23.gif)

#### Ⅲ、日历选择器 Material 风格

1. 显示日历选择器要使用 `showDatePicker` 方法
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/05_其他类型的对话框/03_日历选择器 Material 风格.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: ShowDatePickerComponent()
            )
        )
    );
  }
}
```

3. `03_日历选择器 Material 风格.dart` 弹窗方法

```dart
import 'package:flutter/material.dart';


class ShowDatePickerComponent extends StatefulWidget {
  const ShowDatePickerComponent({Key? key}) : super(key: key);

  @override
  _ShowDatePickerComponentState createState() => _ShowDatePickerComponentState();
}

class _ShowDatePickerComponentState extends State<ShowDatePickerComponent> {
  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  /// 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<DateTime?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 日历选择器"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        var dateTime = await dialog();
        if (dateTime == null) {
          print("点击了取消");
        } else {
          print("选择了日期：${dateTime.year}/${dateTime.month}/${dateTime.day}");
        }
      },
    );
  }

  /// 弹出对话框
  Future<DateTime?> showConfirmDialog() {
    var date = DateTime.now();
    // showDialog 是一个用于显示对话框的方法
    return showDatePicker(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      // initialDate：初始日期，即弹出日历选择器时默认选中的日期
      initialDate: date,
      // firstDate：起始日期，即弹出日历选择器时最早可选的日期
      firstDate: date,
      // lastDate：结束日期，即弹出日历选择器时最晚可选的日期
      lastDate: date.add(const Duration(days: 30))
    );
  }

}
```

4. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画24.gif)

#### Ⅳ、日历选择器 iOS 风格

1. iOS 风格的日历选择器需要使用 `showCupertinoModalPopup` 方法和 `CupertinoDatePicker` 组件来实现
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '05_功能型组件/07_对话框详解/05_其他类型的对话框/04_日历选择器 IOS 风格.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: ShowCupertinoModalPopupComponent()
            )
        )
    );
  }
}
```

3. `04_日历选择器 IOS 风格.dart` 弹窗方法

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';


class ShowCupertinoModalPopupComponent extends StatefulWidget {
  const ShowCupertinoModalPopupComponent({Key? key}) : super(key: key);

  @override
  _ShowCupertinoModalPopupComponentState createState() => _ShowCupertinoModalPopupComponentState();
}

class _ShowCupertinoModalPopupComponentState extends State<ShowCupertinoModalPopupComponent> {
  DateTime date = DateTime.now();

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个用于在垂直方向上排列其子部件的小部件
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.center：将子部件树在垂直方向上对齐到屏幕中心
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // 调用方法，构建 ElevatedButton；dialog：弹出对话框的方法
          buildElevatedButton(showConfirmDialog),
        ],
      ),
    );
  }

  /// 构建 ElevatedButton；dialog：弹出对话框的方法
  Widget buildElevatedButton(Future<DateTime?> Function() dialog){
    return ElevatedButton(
      child: const Text("显示 日历选择器"),
      onPressed: () async {
        // 弹出对话框并等待其关闭，接收对话框关闭时的返回数据
        var dateTime = await dialog();
        if (dateTime == null) {
          print("点击了取消");
        } else {
          print("选择了日期：${dateTime.year}/${dateTime.month}/${dateTime.day}");
        }
      },
    );
  }

  /// 弹出对话框
  Future<DateTime?> showConfirmDialog() {
    // showCupertinoModalPopup 是 IOS 风格的弹出对话框
    return showCupertinoModalPopup(
      // context：构建上下文，即当前 Widget 的位置
      context: context,
      builder: (ctx) {
        // CupertinoAlertDialog 是 IOS 风格的对话框
        return CupertinoAlertDialog(
          title: const Text("请选择日期"),
          // content 属性用于设置对话框的内容区域；buildCupertinoDatePicker()：构建日期选择器
          content: buildCupertinoDatePicker(),
          // actions 属性用于设置对话框的按钮区域
          actions: [
            CupertinoDialogAction(
              child: const Text('取消'),
              // 在取消按钮点击时，返回 null
              onPressed: () => Navigator.of(context).pop(null)
            ),
            CupertinoDialogAction(
              child: const Text('确定'),
              // 在确定按钮点击时，返回选中的日期
              onPressed: () => Navigator.of(context).pop(date)
            ),
          ],
        );
      },
    );
  }

  /// 构建日期选择器
  Widget buildCupertinoDatePicker() {
    // SizedBox 是一个用于指定固定尺寸的小部件
    return SizedBox(
      height: 200,
      // CupertinoDatePicker 是 IOS 风格的日历选择器
      child: CupertinoDatePicker(
        // mode 属性用于设置日历选择器的模式；CupertinoDatePickerMode.date：仅显示日期
        mode: CupertinoDatePickerMode.date,
        // minimumYear 属性用于设置日历选择器可选的最早年份，即日历选择器中可选的最早年份
        minimumYear: date.year - 50,
        // maximumYear 属性用于设置日历选择器可选的最晚年份，即日历选择器中可选的最晚年份
        maximumYear: date.year + 50,
        // onDateTimeChanged 属性用于设置日历选择器选中日期发生变化时的回调函数
        onDateTimeChanged: (DateTime dateTime) {
          date = dateTime;
          print(dateTime);
        },
      ),
    );
  }

}
```

4. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画25.gif)

# 八、事件处理与通知

1. Flutter 中的手势系统有两个独立的层。
2. 第一层为原始指针(pointer)事件，它描述了屏幕上指针（例如，触摸、鼠标和触控笔）的位置和移动。 
3. 第二层为手势，描述由一个或多个指针移动组成的语义动作，如拖动、缩放、双击等。

## 1、原始指针事件处理

### ①、命中测试简介

1. 在移动端，各个平台或 UI 系统的原始指针事件模型基本都是一致，即：一次完整的事件分为三个阶段：手指按下、手指移动、和手指抬起，而更高级别的手势（如点击、双击、拖动等）都是基于这些原始事件的。
2. 当指针按下时，Flutter 会对应用程序执行命中测试(Hit Test)，以确定指针与屏幕接触的位置存在哪些组件（widget）， 指针按下事件（以及该指针的后续事件）然后被分发到由命中测试发现的最内部的组件，然后从那里开始，事件会在组件树中向上冒泡，这些事件会从最内部的组件被分发到组件树根的路径上的所有组件，这和 Web 开发中浏览器的事件冒泡机制相似， 但是 Flutter 中没有机制取消或停止“冒泡”过程，而浏览器的冒泡是可以停止的。
3. 注意，只有通过命中测试的组件才能触发事件，我们会在下一节中深入介绍命中测试过程。
4. 注意：术语 “Hit Test” 的中文翻译比较多，如 “命中测试”、“点击测试” ，对于名字我们不用较真，知道它们代表的是 “Hit Test ” 即可。

### ②、Listener 组件

1. Flutter 中可以使用 `Listener` 来监听原始触摸事件，下面是Listener的构造函数定义：

```dart
Listener({
  Key key,
  this.onPointerDown, //手指按下回调
  this.onPointerMove, //手指移动回调
  this.onPointerUp,//手指抬起回调
  this.onPointerCancel,//触摸事件取消回调
  this.behavior = HitTestBehavior.deferToChild, // 先忽略此参数，后面小节会专门介绍
  Widget child
})
```

2. 我们先看一个示例，下面代码功能是： 手指在一个容器上移动时查看手指相对于容器的位置。
3. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/01_原始指针事件处理/01_Listener 组件.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: ListenerComponent()
            )
        )
    );
  }
}
```

4. `01_Listener 组件.dart` Listener 组件

```dart
import 'package:flutter/material.dart';

class ListenerComponent extends StatefulWidget {
  const ListenerComponent({Key? key}) : super(key: key);

  @override
  _ListenerComponentState createState() => _ListenerComponentState();
}

class _ListenerComponentState extends State<ListenerComponent> {
  // PointerEvent 是一个抽象类，它定义了指针事件的基本信息，如位置、时间戳等
  PointerEvent? _event;
  // 当事件发生时，更新本文本框中的内容
  String eventText = "";

  @override
  Widget build(BuildContext context) {
    // Listener 是一个用于监听触摸事件的小部件
    return Listener(
      // Container 是一个用于构建容器的小部件
      child: Container(
        alignment: Alignment.center,
        color: Colors.blue,
        width: 300.0,
        height: 300.0,
        // Text 是一个用于构建文本的小部件；_event?.localPosition ?? ''：获取触摸点的位置
        child: Text(
          eventText,
          style: const TextStyle(color: Colors.white),
        ),
      ),
      // onPointerDown：按下时触发
      onPointerDown: (PointerDownEvent event) => updateText("按下", event),
      // onPointerMove：移动时触发
      onPointerMove: (PointerMoveEvent event) => updateText("移动", event),
      // onPointerUp：抬起时触发
      onPointerUp: (PointerUpEvent event) => updateText("抬起", event),
    );
  }

  void updateText(String text, PointerEvent? event) {
    setState(() {
      // 更新触摸事件和本文本框中的内容
      _event = event;
      eventText = "当前操作：$text\n点击坐标：${_event?.localPosition ?? ''}";
    });
  }
  
}
```

5. 效果：

![|419](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画26.gif)

6. 指在蓝色矩形区域内移动即可看到当前指针偏移，当触发指针事件时，参数 `PointerDownEvent`、 `PointerMoveEvent`、 `PointerUpEvent` 都是 `PointerEvent` 的子类，`PointerEvent` 类中包括当前指针的一些信息，注意 Pointer，即“指针”， 指事件的触发者，可以是鼠标、触摸板、手指。
7. 如：
	1. `position`：它是指针相对于当对于全局坐标的偏移。
	2. `localPosition`：它是指针相对于当对于本身布局坐标的偏移。
	3. `delta`：两次指针移动事件（PointerMoveEvent）的距离。
	4. `pressure`：按压力度，如果手机屏幕支持压力传感器(如iPhone的3D Touch)，此属性会更有意义，如果手机不支持，则始终为 1。
	5. `orientation`：指针移动方向，是一个角度值。
8. 还有一个 `behavior` 属性，它决定子组件如何响应命中测试，关于该属性我们将在之后详细介绍。

### ③、忽略指针事件

1. 假如我们不想让某个子树响应 `PointerEvent` 的话，我们可以使用 `IgnorePointer` 和 `AbsorbPointer`，这两个组件都能阻止子树接收指针事件
2. 不同之处在于 `AbsorbPointer` 本身会参与命中测试，而 `IgnorePointer` 本身不会参与，这就意味着 `AbsorbPointer` 本身是可以接收指针事件的(但其子树不行)，而 `IgnorePointer` 不可以。一个简单的例子如下：

```dart
Listener(
  child: AbsorbPointer(
    child: Listener(
      child: Container(
        color: Colors.red,
        width: 200.0,
        height: 100.0,
      ),
      onPointerDown: (event)=>print("in"),
    ),
  ),
  onPointerDown: (event)=>print("up"),
)
```

3. 点击 `Container` 时，由于它在 `AbsorbPointer` 的子树上，所以不会响应指针事件，所以日志不会输出"in"，但 `AbsorbPointer` 本身是可以接收指针事件的，所以会输出 "up"。
4. 如果将 `AbsorbPointer` 换成 `IgnorePointer`，那么两个都不会输出。

## 2、手势识别

### ①、GestureDetector 手势识别

1. `GestureDetector` 是一个用于手势识别的功能性组件，我们通过它可以来识别各种手势。
2. `GestureDetector` 内部封装了 `Listener`，用以识别语义化的手势，接下来我们详细介绍一下各种手势的识别

#### Ⅰ、点击、双击、长按

1. 我们通过 `GestureDetector` 对 `Container` 进行手势识别，触发相应事件后，在 `Container` 上显示事件名：
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/02_手势识别/01_GestureDetector_点击、双击、长按.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: GestureDetector1Component()
            )
        )
    );
  }
}
```

3. `01_GestureDetector_点击、双击、长按.dart` 点击、双击、长按方法

```dart
import 'package:flutter/material.dart';

class GestureDetector1Component extends StatefulWidget {
  const GestureDetector1Component({Key? key}) : super(key: key);

  @override
  _GestureDetector1ComponentState createState() => _GestureDetector1ComponentState();
}

class _GestureDetector1ComponentState extends State<GestureDetector1Component> {
  // 保存事件名
  String _operation = "未检测到手势";

  @override
  Widget build(BuildContext context) {
    // Listener 是一个用于监听触摸事件的小部件
    return Center(
      child: GestureDetector(
        child: Container(
          alignment: Alignment.center,
          color: Colors.blue,
          width: 300.0,
          height: 300.0,
          child: Text(
            _operation,
            style: const TextStyle(color: Colors.white),
          ),
        ),
        onTap: () => updateText("点击"),
        onDoubleTap: () => updateText("双击"),
        onLongPress: () => updateText("长按"),
      ),
    );
  }

  void updateText(String text) {
    // 更新显示的事件名
    setState(() {
      _operation = "当前操作为：$text";
    });
  }

}
```

4. 效果：

![|439](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画27.gif)

5. 在模拟器上检测不到双击双击事件，上面的效果图是我连接手机测试的
6. 注意： 当同时监听 `onTap` 和 `onDoubleTap` 事件时，当用户触发 `tap` 事件时，会有 200 毫秒左右的延时，这是因为当用户点击完之后很可能会再次点击以触发双击事件，所以 `GestureDetector` 会等一段时间来确定是否为双击事件。如果用户只监听了 `onTap`（没有监听 `onDoubleTap`）事件时，则没有延时

#### Ⅱ、拖动、滑动

1. 一次完整的手势过程是指用户手指按下到抬起的整个过程，期间，用户按下手指后可能会移动，也可能不会移动。
2. `GestureDetector` 对于拖动和滑动事件是没有区分的，他们本质上是一样的。
3. `GestureDetector` 会将要监听的组件的原点（左上角）作为本次手势的原点，当用户在监听的组件上按下手指时，手势识别就会开始。下面我们看一个拖动圆形字母 A 的示例：
4. `main` 主启动方法

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/02_手势识别/01_GestureDetector_点击、双击、长按.dart';
import '08_事件处理与通知/02_手势识别/02_GestureDetector_拖动、滑动.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: GestureDetector2Component()
            )
        )
    );
  }
}
```

5. `02_GestureDetector_拖动、滑动.dart` 拖动、滑动方法

```dart
import 'package:flutter/material.dart';

class GestureDetector2Component extends StatefulWidget {
  const GestureDetector2Component({Key? key}) : super(key: key);

  @override
  _GestureDetector2ComponentState createState() => _GestureDetector2ComponentState();
}

class _GestureDetector2ComponentState extends State<GestureDetector2Component> {
  // 距顶部的偏移
  double _top = 0.0;
  // 距左边的偏移
  double _left = 0.0;

  @override
  Widget build(BuildContext context) {
    // Stack 允许子部件堆叠，可使用 Positioned 根据 Stack 的四个角来定位子部件。
    return Stack(
      children: [
        // Positioned 是一个小部件，它可以控制子部件的位置
        Positioned(
          top: _top,
          left: _left,
          // GestureDetector 是一个小部件，用于手势识别
          child: GestureDetector(
            // CircleAvatar 是一个小部件，用于绘制圆形头像
            child: const CircleAvatar(child: Text("A")),
            // 手指按下时会触发此回调
            onPanDown: (DragDownDetails e) {
              /**
               * 打印手指按下的位置(相对于屏幕)
               * globalPosition 属性是一个 Offset 对象，它表示全局坐标，即相对于屏幕左上角的坐标。
               */
              print("用户手指按下：${e.globalPosition}");
            },
            // 手指滑动时会触发此回调
            onPanUpdate: (DragUpdateDetails e) {
              // 用户手指滑动时，更新偏移，重新构建
              setState(() {
                /**
                 * 当用户在屏幕上滑动时，会触发多次Update事件
                 * delta 属性是一个 Offset 对象，它表示相对于上一个事件的偏移量。
                 */
                _left += e.delta.dx;
                _top += e.delta.dy;
              });
            },
            onPanEnd: (DragEndDetails e){
              /**
               * 打印滑动结束时在 x、y 轴上的速度
               * velocity 属性是一个 Offset 对象，它表示在滑动结束时的速度。
               * velocity.pixelsPerSecond.dx 表示水平方向的速度，velocity.pixelsPerSecond.dy 表示垂直方向的速度。
               * 注意：velocity 是一个速度，它是有方向的，所以它是一个 Offset 对象。
               */
              print("用户手指抬起：${e.velocity}");
            },
          )
        )
      ],
    );
  }

}
```

6. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画28.gif)

#### Ⅲ、缩放

1. GestureDetector 可以监听缩放事件，下面示例演示了一个简单的图片缩放效果：
2. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/02_手势识别/01_GestureDetector_点击、双击、长按.dart';
import '08_事件处理与通知/02_手势识别/02_GestureDetector_拖动、滑动.dart';
import '08_事件处理与通知/02_手势识别/03_GestureDetector_缩放.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: GestureDetector3Component()
            )
        )
    );
  }
}
```

3. `03_GestureDetector_缩放.dart`缩放方法

```dart
import 'package:flutter/material.dart';

class GestureDetector3Component extends StatefulWidget {
  const GestureDetector3Component({Key? key}) : super(key: key);

  @override
  _GestureDetector3ComponentState createState() => _GestureDetector3ComponentState();
}

class _GestureDetector3ComponentState extends State<GestureDetector3Component> {
  // 通过修改图片宽度来达到缩放效果
  double _width = 200.0;

  @override
  Widget build(BuildContext context) {
    // Center 居中布局
    return Center(
      // GestureDetector 手势识别
      child: GestureDetector(
        // 指定宽度，高度自适应
        child: Image.asset("asset/images/QQ图片20220920105928.jpg", width: _width),
        // 缩放事件
        onScaleUpdate: (ScaleUpdateDetails details) {
          setState(() {
            //缩放倍数在0.8到10倍之间
            _width = 200 * details.scale.clamp(.8, 10.0);
          });
        },
      ),
    );
  }

}
```

4. 效果：

![|439](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画29.gif)

### ②、GestureRecognizer 针事件转换

1. `GestureDetector` 内部是使用一个或多个 `GestureRecognizer` 来识别各种手势的，而 `GestureRecognizer` 的作用就是通过 `Listener` 来将原始指针事件转换为语义手势，`GestureDetector` 直接可以接收一个子 `widget`。
2. `GestureRecognizer` 是一个抽象类，一种手势的识别器对应一个 `GestureRecognizer` 的子类，Flutter 实现了丰富的手势识别器，我们可以直接使用。
3. 假设我们要给一段富文本（RichText）的不同部分分别添加点击事件处理器，但是 `TextSpan` 并不是一个 widget，这时我们不能用 `GestureDetector`，但 `TextSpan` 有一个 `recognizer` 属性，它可以接收一个 `GestureRecognizer`。假设我们需要在点击时给文本变色：
4. `main` 主方法

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/02_手势识别/04_GestureRecognizer.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: GestureRecognizerComponent()
            )
        )
    );
  }
}
```

5. `01_底部菜单列表.dart` 弹窗方法

```dart
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

class GestureRecognizerComponent extends StatefulWidget {
  const GestureRecognizerComponent({Key? key}) : super(key: key);

  @override
  _GestureRecognizerComponentState createState() => _GestureRecognizerComponentState();
}

class _GestureRecognizerComponentState extends State<GestureRecognizerComponent> {
  // TapGestureRecognizer 是一个手势识别器，它可以识别各种点击手势，包括点击、双击、长按等。
  final TapGestureRecognizer _tapGestureRecognizer = TapGestureRecognizer();
  // 变色开关
  bool _toggle = false;

  @override
  void dispose() {
    // 用到 GestureRecognizer 的话一定要调用其 dispose 方法释放资源
    _tapGestureRecognizer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Center 居中布局
    return Center(
      // Text.rich() 可以显示多种样式的文本
      child: Text.rich(
        // TextSpan 可以设置文本的样式
        TextSpan(
          children: [
            const TextSpan(text: '你好世界'),
            TextSpan(
              text: '点我变色',
              style: TextStyle(
                fontSize: 30.0,
                color: _toggle ? Colors.blue : Colors.red
              ),
              // recognizer: 为 TextSpan 添加点击事件
              recognizer: _tapGestureRecognizer
                // ..onTap = () {} 语法是 Dart 中的级联操作，允许对同一个对象进行一系列的操作
                ..onTap = () {
                  setState(() {
                    _toggle = !_toggle;
                  });
                }
            ),
            const TextSpan(text: '你好世界')
          ]
        )
      )
    );
  }

}
```

6. 效果：

![|412](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画30.gif)

7. 注意：使用 `GestureRecognizer` 后一定要调用其 `dispose()` 方法来释放资源（主要是取消内部的计时器）。

## 3、Flutter 事件机制

### ①、Flutter 事件处理流程

1. Flutter 事件处理流程主要分两步，为了聚焦核心流程，我们以用户触摸事件为例来说明：
	1. 命中测试：当手指按下时，触发 `PointerDownEvent` 事件，按照深度优先遍历当前渲染（render object）树，对每一个渲染对象进行“命中测试”（hit test），如果命中测试通过，则该渲染对象会被添加到一个 `HitTestResult` 列表当中。
	2. 事件分发：命中测试完毕后，会遍历 `HitTestResult` 列表，调用每一个渲染对象的事件处理方法（`handleEvent`）来处理 `PointerDownEvent` 事件，该过程称为“事件分发”（event dispatch）。随后当手指移动时，便会分发 `PointerMoveEvent` 事件。
	3. 事件清理：当手指抬（ `PointerUpEvent` ）起或事件取消时（`PointerCancelEvent`），会先对相应的事件进行分发，分发完毕后会清空 `HitTestResult` 列表。
2. 需要注意：
	1. 命中测试是在 `PointerDownEvent` 事件触发时进行的，一个完成的事件流是 `down > move > up (cancle)`。
	2. 如果父子组件都监听了同一个事件，则子组件会比父组件先响应事件。这是因为命中测试过程是按照深度优先规则遍历的，所以子渲染对象会比父渲染对象先加入 `HitTestResult` 列表，又因为在事件分发时是从前到后遍历 `HitTestResult` 列表的，所以子组件比父组件会更先被调用 `handleEvent` 。
3. 下面我们从代码层面看一些整个事件处理流程：

```dart
// 触发新事件时，flutter 会调用此方法
void _handlePointerEventImmediately(PointerEvent event) {
  HitTestResult? hitTestResult;
  if (event is PointerDownEvent ) {
    hitTestResult = HitTestResult();
    // 发起命中测试
    hitTest(hitTestResult, event.position);
    if (event is PointerDownEvent) {
      _hitTests[event.pointer] = hitTestResult;
    }
  } else if (event is PointerUpEvent || event is PointerCancelEvent) {
    //获取命中测试的结果，然后移除它
    hitTestResult = _hitTests.remove(event.pointer);
  } else if (event.down) { // PointerMoveEvent
    //直接获取命中测试的结果
    hitTestResult = _hitTests[event.pointer];
  }
  // 事件分发
  if (hitTestResult != null) {
    dispatchEvent(event, hitTestResult);
  }
}
```

4. 上面代码只是核心代码，完整的代码位于 `GestureBinding` 实现中。下面我们分别来介绍一些命中测试和事件分发过程

### ②、命中测试详解

#### Ⅰ、命中测试的起点

1. 一个对象是否可以响应事件，取决于在其对命中测试过程中是否被添加到了 `HitTestResult` 列表 ，如果没有被添加进去，则后续的事件分发将不会分发给自己。下面我们看一下命中测试的过程：当发生用户事件时，Flutter  会从根节点（RenderView）开始调用它 `hitTest()` 。

```dart
@override
void hitTest(HitTestResult result, Offset position) {
  //从根节点开始进行命中测试
  renderView.hitTest(result, position: position); 
  // 会调用 GestureBinding 中的 hitTest()方法，我们将在下一节中介绍。
  super.hitTest(result, position); 
}
```

2. 上面代码位于 `RenderBinding` 中，核心代码只有两行，整体是命中测试分两步，我们来解释一下：
3. 第一步： `renderView` 是 `RenderView` 对应的 `RenderObject` 对象， `RenderObject` 对象的 `hitTest` 方法主要功能是：从该节点出发，按照深度优先的顺序递归遍历子树（渲染树）上的每一个节点并对它们进行命中测试。这个过程称为“渲染树命中测试”。注意，为了表述方便，“渲染树命中测试”，也可以表述为组件树或节点树命中测试，只是我们需要知道，命中测试的逻辑都在 `RenderObject` 中，而并非在 `Widget` 或 `Element` 中。
4. 第二步：渲染树命中测试完毕后，会调用 `GestureBinding` 的 `hitTest` 方法，该方法主要用于处理手势，我们会在后面介绍。

#### Ⅱ、渲染树命中测试过程

1. 渲染树的命中测试流程就是父节点 `hitTest` 方法中不断调用子节点 `hitTest` 方法的递归过程。下面是 `RenderView` 的 `hitTest()` 源码：

```dart
// 发起命中测试，position 为事件触发的坐标（如果有的话）。
bool hitTest(HitTestResult result, { Offset position }) {
  if (child != null)
    child.hitTest(result, position: position); //递归对子树进行命中测试
  //根节点会始终被添加到HitTestResult列表中
  result.add(HitTestEntry(this)); 
  return true;
}
```

2. 因为 `RenderView` 只有一个孩子，所以直接调用 `child.hitTest` 即可。如果一个渲染对象有多个子节点，则命中测试逻辑为：如果任意一个子节点通过了命中测试或者当前节点“强行声明”自己通过了命中测试，则当前节点会通过命中测试。我们以 `RenderBox` 为例，看看它的 `hitTest()` 实现：

```dart
bool hitTest(HitTestResult result, { @required Offset position }) {
  ...  
  if (_size.contains(position)) { // 判断事件的触发位置是否位于组件范围内
    if (hitTestChildren(result, position: position) || hitTestSelf(position)) {
      result.add(BoxHitTestEntry(this, position));
      return true;
    }
  }
  return false;
}
```

3. 上面代码中：
	1. `hitTestChildren()` 功能是判断是否有子节点通过了命中测试，如果有，则会将子组件添加到 `HitTestResult` 中同时返回 `true`；如果没有则直接返回 `false`。该方法中会递归调用子组件的 `hitTest` 方法。
	2. `hitTestSelf()` 决定自身是否通过命中测试，如果节点需要确保自身一定能响应事件可以重写此函数并返回true ，相当于“强行声明”自己通过了命中测试。
4. 需要注意，节点通过命中测试的标志是它被添加到 `HitTestResult` 列表中，而不是它 `hitTest` 的返回值，虽然大所数情况下节点通过命中测试就会返回 `true`，但是由于开发者在自定义组件时是可以重写 `hitTest` 的，所以有可能会在在通过命中测试时返回 `false`，或者未通过命中测试时返回 `true`，当然这样做并不好，我们在自定义组件时应该尽可能避免，但是在有些需要自定义命中测试流程的场景下可能就需要打破这种默契，比如我们将在本节后面实现的 `HitTestBlocker` 组件。
5. 所以整体逻辑就是：
	1. 先判断事件的触发位置是否位于组件范围内，如果不是则不会通过命中测试，此时 `hitTest` 返回 `false`，如果是则到第二步。
	2. 会先调用 `hitTestChildren()` 判断是否有子节点通过命中测试，如果是，则将当前节点添加到 `HitTestResult` 列表，此时 `hitTest` 返回 `true`。即只要有子节点通过了命中测试，那么它的父节点（当前节点）也会通过命中测试。
	3. 如果没有子节点通过命中测试，则会取 `hitTestSelf` 方法的返回值，如果返回值为 `true`，则当前节点通过命中测试，反之则否。
6. 如果当前节点有子节点通过了命中测试或者当前节点自己通过了命中测试，则将当前节点添加到 `HitTestResult` 中。又因为 `hitTestChildren()` 中会递归调用子组件的 `hitTest` 方法，所以组件树的命中测试顺序深度优先的，即如果通过命中测试，子组件会比父组件会先被加入 `HitTestResult` 中。
7. 我们看看这两个方法默认实现如下：

```dart
@protected
bool hitTestChildren(HitTestResult result, { Offset position }) => false;

@protected
bool hitTestSelf(Offset position) => false;
```

8. 如果组件包含多个子组件，就必须重写 `hitTestChildren()` 方法，该方法中应该调用每一个子组件的 `hitTest` 方法，比如我们看看 `RenderBoxContainerDefaultsMixin` 中的实现：

```dart
// 子类的 hitTestChildren() 中会直接调用此方法
bool defaultHitTestChildren(BoxHitTestResult result, { required Offset position }) {
   // 遍历所有子组件(子节点从后向前遍历)
  ChildType? child = lastChild;
  while (child != null) {
    final ParentDataType childParentData = child.parentData! as ParentDataType;
    // isHit 为当前子节点调用hitTest() 的返回值
    final bool isHit = result.addWithPaintOffset(
      offset: childParentData.offset,
      position: position,
      //调用子组件的 hitTest方法，
      hitTest: (BoxHitTestResult result, Offset? transformed) {
        return child!.hitTest(result, position: transformed!);
      },
    );
    // 一旦有一个子节点的 hitTest() 方法返回 true，则终止遍历，直接返回true
    if (isHit) return true;
    child = childParentData.previousSibling;
  }
  return false;
}

  bool addWithPaintOffset({
    required Offset? offset,
    required Offset position,
    required BoxHitTest hitTest,
  }) {
    ...// 省略无关代码
    final bool isHit = hitTest(this, transformedPosition);
    return isHit; // 返回 hitTest 的执行结果
  }
```

9. 我们可以看到上面代码的主要逻辑是遍历调用子组件的 `hitTest()` 方法，同时提供了一种中断机制：即遍历过程中只要有子节点的 `hitTest()` 返回了 `true` 时：
	1. 会终止子节点遍历，这意味着该子节点前面的兄弟节点将没有机会通过命中测试。注意，兄弟节点的遍历倒序的。
	2. 父节点也会通过命中测试。因为子节点 `hitTest()` 返回了 `true` 导父节点 `hitTestChildren` 也会返回 `true`，最终会导致 父节点的 `hitTest` 返回 `true`，父节点被添加到 `HitTestResult` 中。
10. 当子节点的 `hitTest()` 返回了 `false` 时，继续遍历该子节点前面的兄弟节点，对它们进行命中测试，如果所有子节点都返回 `false` 时，则父节点会调用自身的 `hitTestSelf` 方法，如果该方法也返回 `false`，则父节点就会被认为没有通过命中测试。
11. 下面思考两个问题：
	1. 为什么要制定这个中断呢？因为一般情况下兄弟节点占用的布局空间是不重合的，因此当用户点击的坐标位置只会有一个节点，所以一旦找到它后（通过了命中测试，`hitTest` 返回 `true`），就没有必要再判断其他兄弟节点了。但是也有例外情况，比如在 `Stack` 布局中，兄弟组件的布局空间会重叠，如果我们想让位于底部的组件也能响应事件，就得有一种机制，能让我们确保：即使找到了一个节点，也不应该终止遍历，也就是说所有的子组件的 `hitTest` 方法都必须返回 `false`！为此，Flutter 中通过 `HitTestBehavior` 来定制这个过程，这个我们会在本节后面介绍。
	2. 为什么兄弟节点的遍历要倒序？同 1 中所述，兄弟节点一般不会重叠，而一旦发生重叠的话，往往是后面的组件会在前面组件之上，点击时应该是后面的组件会响应事件，而前面被遮住的组件不能响应，所以命中测试应该优先对后面的节点进行测试，因为一旦通过测试，就不会再继续遍历了。如果我们按照正向遍历，则会出现被遮住的组件能响应事件，而位于上面的组件反而不能，这明显不符合预期。
12. 我们回到 `hitTestChildren` 上，如果不重写 `hitTestChildren`，则默认直接返回 `false`，这也就意味着后代节点将无法参与命中测试，相当于事件被拦截了，这也正是 `IgnorePointer` 和 `AbsorbPointer` 可以拦截事件下发的原理。
13. 如果 `hitTestSelf` 返回 `true`，则无论子节点中是否有通过命中测试的节点，当前节点自身都会被添加到 `HitTestResult` 中。而 `IgnorePointer` 和 `AbsorbPointer` 的区别就是，前者的 `hitTestSelf` 返回了 `false`，而后者返回了 `true`。
14. 命中测试完成后，所有通过命中测试的节点都被添加到了 `HitTestResult` 中。

### ③、事件分发

1. 事件分发过程很简单，即遍历 `HitTestResult`，调用每一个节点的 `handleEvent` 方法：

```dart
// 事件分发
void dispatchEvent(PointerEvent event, HitTestResult? hitTestResult) {
  ... 
  for (final HitTestEntry entry in hitTestResult.path) {
    entry.target.handleEvent(event.transformed(entry.transform), entry);
  }
}
```

2. 所以组件只需要重写 `handleEvent` 方法就可以处理事件了

### ④、HitTestBehavior

1. 我们先来实现一个能够监听 `PointerDownEvent` 的组件：
2. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/03_Flutter事件机制/05_HitTestBehavior/02_PointerDownListenerRoute.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
            backgroundColor: Colors.white,
            /**
             * body: 用于定义页面的主要内容区域
             * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
             */
            body: SafeArea(
                child: PointerDownListenerRoute()
            )
        )
    );
  }
}
```

3. `01_PointerDownListener.dart` 监听 `PointerDownEvent` 的组件

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/rendering.dart';

class PointerDownListener extends SingleChildRenderObjectWidget {
  const PointerDownListener({Key? key, this.onPointerDown, Widget? child}) : super(key: key, child: child);

  /// 定义一个回调函数，用于接收 PointerDownEvent 事件
  final PointerDownEventListener? onPointerDown;

  /// createRenderObject 方法用于创建 RenderObject
  /// RenderObject 是一个抽象类，它定义了一个小部件的渲染逻辑和布局逻辑
  @override
  RenderObject createRenderObject(BuildContext context) => RenderPointerDownListener()..onPointerDown = onPointerDown;

  /// updateRenderObject 方法用于更新 RenderObject；
  @override
  void updateRenderObject(BuildContext context, RenderPointerDownListener renderObject) {
    renderObject.onPointerDown = onPointerDown;
  }
}

/// 定义一个回调函数类型，用于接收 PointerDownEvent 事件
class RenderPointerDownListener extends RenderProxyBox {
  /// 定义一个回调函数，用于接收 PointerDownEvent 事件
  PointerDownEventListener? onPointerDown;

  /// hitTestSelf 方法用于命中测试，返回 true 时表示命中了当前小部件
  @override
  bool hitTestSelf(Offset position) => true; // 始终通过命中测试

  /// handleEvent 方法用于处理事件，它接收两个参数，第一个参数是事件对象，第二个参数是命中测试的结果
  @override
  void handleEvent(PointerEvent event, covariant HitTestEntry entry) {
    // 事件分发时处理事件；如果 onPointerDown 不为空，则调用它
    if (event is PointerDownEvent) onPointerDown?.call(event);
  }
}
```

4. `02_PointerDownListenerRoute.dart` 测试组件

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_PointerDownListener.dart';

class PointerDownListenerRoute extends StatelessWidget {
  const PointerDownListenerRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // PointerDownListener 是一个自定义的小部件，它继承自 SingleChildRenderObjectWidget
    return PointerDownListener(
      // Container 是一个常用的 UI 小部件，它可以用来创建一个矩形视觉元素
      child: Container(
        alignment: Alignment.center,
        color: Colors.blue,
        width: 200,
        height: 100,
        child: const Text(
          '点击此处',
          style: TextStyle(color: Colors.white),
        ),

      ),
      onPointerDown: (e) => print('按下'),
    );
  }
}
```

5. 点击文本后控制台就会打印 'down'。
6. `Listener` 的实现和 `PointerDownListener` 的实现原理差不多，有两点不同：
	1. `Listener` 监听的事件类型更多一些。
	2. `Listener` 的 `hitTestSelf` 并不是一直返回 `true`。
7. 这里需要重点说一下第二点。 `Listener` 组件有一个 `behavior` 参数，我们之前并没有介绍，下面我们仔细介绍一下。通过查看 `Listener` 源码，发现它的渲染对象 `RenderPointerListener` 继承了 `RenderProxyBoxWithHitTestBehavior` 类：

```dart
abstract class RenderProxyBoxWithHitTestBehavior extends RenderProxyBox {
  //[behavior] 的默认值为 [HitTestBehavior.deferToChild].
  RenderProxyBoxWithHitTestBehavior({
    this.behavior = HitTestBehavior.deferToChild,
    RenderBox? child,
  }) : super(child);

  HitTestBehavior behavior;

  @override
  bool hitTest(BoxHitTestResult result, { required Offset position }) {
    bool hitTarget = false;
    if (size.contains(position)) {
      hitTarget = hitTestChildren(result, position: position) || hitTestSelf(position);
      if (hitTarget || behavior == HitTestBehavior.translucent) //1
        result.add(BoxHitTestEntry(this, position)); // 通过命中测试
    }
    return hitTarget;
  }

  @override
  bool hitTestSelf(Offset position) => behavior == HitTestBehavior.opaque; //2

}
```

8. 我们看到 `behavior` 在 `hitTest` 和 `hitTestSelf` 中会使用，它的取值会影响 `Listener` 的命中测试结果。我们先看看 `behavior` 都有哪些取值：

```dart
//在命中测试过程中 Listener 组件如何表现。
enum HitTestBehavior {
  // 组件是否通过命中测试取决于子组件是否通过命中测试
  deferToChild,
  // 组件必然会通过命中测试，同时其 hitTest 返回值始终为 true
  opaque,
  // 组件必然会通过命中测试，但其 hitTest 返回值可能为 true 也可能为 false
  translucent,
}
```

9. 它有三个取值，我们结合 `hitTest` 实现来分析一下不同取值的作用：
	1. `behavior` 为 `deferToChild` 时，`hitTestSelf` 返回 `false`，当前组件是否能通过命中测试完全取决于 `hitTestChildren` 的返回值。也就是说只要有一个子节点通过命中测试，则当前组件便会通过命中测试。
	2. `behavior` 为 `opaque` 时，`hitTestSelf` 返回 `true`，`hitTarget` 值始终为 `true`，当前组件通过命中测试。
	3. `behavior` 为 `translucent` 时，`hitTestSelf` 返回 `false`，`hitTarget` 值此时取决于 `hitTestChildren` 的返回值，但是无论 `hitTarget` 值是什么，当前节点都会被添加到 `HitTestResult` 中。
10. 注意，`behavior` 为 `opaque` 和 `translucent` 时当前组件都会通过命中测试，它们的区别是 `hitTest()` 的返回值（hitTarget ）可能不同，所以它们的区别就看 `hitTest()` 的返回值会影响什么，这个我们已经在上面详细介绍过了，下面我们通过一个实例来理解一下

## 4、手势原理与手势冲突

### ①、手势识别原理

1. 手势的识别和处理都是在事件分发阶段的，`GestureDetector` 是一个 `StatelessWidget`， 包含了 `RawGestureDetector`，我们看一下它的 `build` 方法实现：

```dart
@override
Widget build(BuildContext context) {
  final  gestures = <Type, GestureRecognizerFactory>{};
  // 构建 TapGestureRecognizer 
  if (onTapDown != null ||
      onTapUp != null ||
      onTap != null ||
      ... //省略
  ) {
    gestures[TapGestureRecognizer] = GestureRecognizerFactoryWithHandlers<TapGestureRecognizer>(
      () => TapGestureRecognizer(debugOwner: this),
      (TapGestureRecognizer instance) {
        instance
          ..onTapDown = onTapDown
          ..onTapUp = onTapUp
          ..onTap = onTap
          //省略
      },
    );
  }

  
  return RawGestureDetector(
    gestures: gestures, // 传入手势识别器
    behavior: behavior, // 同 Listener 中的 HitTestBehavior
    child: child,
  );
}
```

2. 注意，上面我们删除了很多代码，只保留了 `TapGestureRecognizer`（点击手势识别器） 相关代码，我们以点击手势识别为例讲一下整个过程。`RawGestureDetector` 中会通过 `Listener` 组件监听 `PointerDownEvent` 事件，相关源码如下：

```dart
@override
Widget build(BuildContext context) {
  ... // 省略无关代码
  Widget result = Listener(
    onPointerDown: _handlePointerDown,
    behavior: widget.behavior ?? _defaultBehavior,
    child: widget.child,
  );
}  
 
void _handlePointerDown(PointerDownEvent event) {
  for (final GestureRecognizer recognizer in _recognizers!.values)
    recognizer.addPointer(event);
}  
```

3. 下面我们看一下 `TapGestureRecognizer` 的几个相关方法，由于 `TapGestureRecognizer` 有多层继承关系，合并了一个简化版：

```dart
class CustomTapGestureRecognizer1 extends TapGestureRecognizer {

  void addPointer(PointerDownEvent event) {
    //会将 handleEvent 回调添加到 pointerRouter 中
    GestureBinding.instance!.pointerRouter.addRoute(event.pointer, handleEvent);
  }
  
  @override
  void handleEvent(PointerEvent event) {
    //会进行手势识别，并决定是是调用 acceptGesture 还是 rejectGesture，
  }
  
  @override
  void acceptGesture(int pointer) {
    // 竞争胜出会调用
  }

  @override
  void rejectGesture(int pointer) {
    // 竞争失败会调用
  }
}
```

4. 可以看到当 `PointerDownEvent` 事件触发时，会调用 `TapGestureRecognizer` 的 `addPointer`，在 `addPointer` 中会将 `handleEvent` 方法添加到 `pointerRouter` 中保存起来。这样一来当手势发生变化时只需要在 `pointerRouter` 中取出 `GestureRecognizer` 的 `handleEvent` 方法进行手势识别即可。
5. 正常情况下应该是手势直接作用的对象应该来处理手势，所以一个简单的原则就是同一个手势应该只有一个手势识别器生效，为此，手势识别才映入了手势竞技场（Arena）的概念，简单来讲：
	1. 每一个手势识别器（GestureRecognizer）都是一个“竞争者”（GestureArenaMember），当发生指针事件时，他们都要在“竞技场”去竞争本次事件的处理权，默认情况最终只有一个“竞争者”会胜出(win)。
	2. `GestureRecognizer` 的 `handleEvent` 中会识别手势，如果手势发生了某个手势，竞争者可以宣布自己是否胜出，一旦有一个竞争者胜出，竞技场管理者（GestureArenaManager）就会通知其他竞争者失败。
	3. 胜出者的 `acceptGesture` 会被调用，其余的 `rejectGesture` 将会被调用。
6. 上一节我们说过命中测试是从 `RenderBinding` 的 `hitTest` 开始的：

```dart
@override
void hitTest(HitTestResult result, Offset position) {
  // 从根节点开始进行命中测试
  renderView.hitTest(result, position: position); 
  // 会调用 GestureBinding 中的 hitTest()方法，我们将在下一节中介绍。
  super.hitTest(result, position); 
}
```

7. 渲染树命中测试完成后会调用 `GestureBinding` 中的 `hitTest()` 方法：

```dart
@override // from HitTestable
void hitTest(HitTestResult result, Offset position) {
  result.add(HitTestEntry(this));
}
```

8. 很简单， `GestureBinding` 也通过命中测试了，这样的话在事件分发阶段，`GestureBinding` 的 `handleEvent` 便也会被调用，由于它是最后被添加到 `HitTestResult` 中的，所以在事件分发阶段 `GestureBinding` 的 `handleEvent` 会在最后被调用：

```dart
@override 
void handleEvent(PointerEvent event, HitTestEntry entry) {
  // 会调用在 pointerRouter 中添加的 GestureRecognizer 的 handleEvent
  pointerRouter.route(event);
  if (event is PointerDownEvent) {
    // 分发完毕后，关闭竞技场
    gestureArena.close(event.pointer);
  } else if (event is PointerUpEvent) {
    gestureArena.sweep(event.pointer);
  } else if (event is PointerSignalEvent) {
    pointerSignalResolver.resolve(event);
  }
}
```

9. `gestureArena` 是 `GestureArenaManager` 类实例，负责管理竞技场。
10. 上面关键的代码就是第一行，功能是会调用之前在 `pointerRouter` 中添加的 `GestureRecognizer` 的 `handleEvent`，不同 `GestureRecognizer` 的 `handleEvent` 会识别不同的手势，然后它会和 `gestureArena` 交互（如果当前的 `GestureRecognizer` 胜出，需要 `gestureArena` 去通知其他竞争者它们失败了），最终，如果当前 `GestureRecognizer` 胜出，则最终它的 `acceptGesture` 会被调用，如果失败则其 `rejectGesture` 将会被调用，因为这部分代码不同的 `GestureRecognizer` 会不同，知道做了什么就行，有兴趣可以自行查看源码。

### ②、手势竞争

1. 如果对一个组件同时监听水平和垂直方向的拖动手势，当我们斜着拖动时哪个方向的拖动手势回调会被触发？实际上取决于第一次移动时两个轴上的位移分量，哪个轴的大，哪个轴在本次滑动事件竞争中就胜出。
2. 上面已经说过，每一个手势识别器（GestureRecognizer）都是一个“竞争者”（GestureArenaMember），当发生指针事件时，他们都要在“竞技场”去竞争本次事件的处理权，默认情况最终只有一个“竞争者”会胜出(win)。
3. 例如，假设有一个 ListView，它的第一个子组件也是 ListView，如果现在滑动这个子 ListView，父 ListView 会动吗？答案是否定的，这时只有子 ListView 会动，因为这时子 ListView 会胜出而获得滑动事件的处理权。
4. 下面我们看一个简单的例子：

```dart
GestureDetector( //GestureDetector2
  onTapUp: (x)=>print("2"), // 监听父组件 tapUp 手势
  child: Container(
    width:200,
    height: 200,
    color: Colors.red,
    alignment: Alignment.center,
    child: GestureDetector( //GestureDetector1
      onTapUp: (x)=>print("1"), // 监听子组件 tapUp 手势
      child: Container(
        width: 50,
        height: 50,
        color: Colors.grey,
      ),
    ),
  ),
);
```

5. 当我们点击子组件（灰色区域）时，控制台只会打印 “1”, 并不会打印 “2”，这是因为手指抬起后，`GestureDetector1` 和 `GestureDetector` 2 会发生竞争，判定获胜的规则是“子组件优先”，所以 `GestureDetector1` 获胜，因为只能有一个“竞争者”胜出，所以 `GestureDetector` 2 将被忽略。这个例子中想要解决冲突的方法很简单，将 `GestureDetector` 换为 `Listener` 即可，具体原因我们在后面解释。
6. 我们再看一个例子，我们以拖动手势为例，同时识别水平和垂直方向的拖动手势，当用户按下手指时就会触发竞争（水平方向和垂直方向），一旦某个方向“获胜”，则直到当次拖动手势结束都会沿着该方向移动。代码如下：

```dart
class _BothDirectionTest extends StatefulWidget {
  @override
  _BothDirectionTestState createState() => _BothDirectionTestState();
}

class _BothDirectionTestState extends State<_BothDirectionTest> {
  double _top = 0.0;
  double _left = 0.0;

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Positioned(
          top: _top,
          left: _left,
          child: GestureDetector(
            child: CircleAvatar(child: Text("A")),
            //垂直方向拖动事件
            onVerticalDragUpdate: (DragUpdateDetails details) {
              setState(() {
                _top += details.delta.dy;
              });
            },
            onHorizontalDragUpdate: (DragUpdateDetails details) {
              setState(() {
                _left += details.delta.dx;
              });
            },
          ),
        )
      ],
    );
  }
}
```

7. 示例运行后，每次拖动只会沿一个方向移动（水平或垂直），而竞争发生在手指按下后首次移动（move）时，此例中具体的“获胜”条件是：首次移动时的位移在水平和垂直方向上的分量大的一个获胜。

### ③、多手势冲突

1. 由于手势竞争最终只有一个胜出者，所以，当我们通过一个 `GestureDetector` 监听多种手势时，也可能会产生冲突。假设有一个 widget，它可以左右拖动，现在我们也想检测在它上面手指按下和抬起的事件，代码如下：

```dart
class GestureConflictTestRouteState extends State<GestureConflictTestRoute> {
  double _left = 0.0;
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Positioned(
          left: _left,
          child: GestureDetector(
              child: CircleAvatar(child: Text("A")), //要拖动和点击的widget
              onHorizontalDragUpdate: (DragUpdateDetails details) {
                setState(() {
                  _left += details.delta.dx;
                });
              },
              onHorizontalDragEnd: (details){
                print("onHorizontalDragEnd");
              },
              onTapDown: (details){
                print("down");
              },
              onTapUp: (details){
                print("up");
              },
          ),
        )
      ],
    );
  }
}
```

2. 现在我们按住圆形“A”拖动然后抬起手指，控制台日志如下:

```dart
I/flutter (17539): down
I/flutter (17539): onHorizontalDragEnd
```

3. 我们发现没有打印"up"，这是因为在拖动时，刚开始按下手指且没有移动时，拖动手势还没有完整的语义，此时 `TapDown` 手势胜出(win)，此时打印"down"，而拖动时，拖动手势会胜出，当手指抬起时，`onHorizontalDragEnd` 和 `onTapUp` 发生了冲突，但是因为是在拖动的语义中，所以 `onHorizontalDragEnd` 胜出，所以就会打印 “onHorizontalDragEnd”。
4. 如果我们的代码逻辑中，对于手指按下和抬起是强依赖的，比如在一个轮播图组件中，我们希望手指按下时，暂停轮播，而抬起时恢复轮播，但是由于轮播图组件中本身可能已经处理了拖动手势（支持手动滑动切换），甚至可能也支持了缩放手势，这时我们如果在外部再用 `onTapDown`、`onTapUp` 来监听的话是不行的。这时我们应该怎么做？其实很简单，通过 `Listener` 监听原始指针事件就行：

```dart
Positioned(
  top:80.0,
  left: _leftB,
  child: Listener(
    onPointerDown: (details) {
      print("down");
    },
    onPointerUp: (details) {
      //会触发
      print("up");
    },
    child: GestureDetector(
      child: CircleAvatar(child: Text("B")),
      onHorizontalDragUpdate: (DragUpdateDetails details) {
        setState(() {
          _leftB += details.delta.dx;
        });
      },
      onHorizontalDragEnd: (details) {
        print("onHorizontalDragEnd");
      },
    ),
  ),
)
```

### ④、解决手势冲突

1. 手势是对原始指针的语义化的识别，手势冲突只是手势级别的，也就是说只会在组件树中的多个  `GestureDetector` 之间才有冲突的场景，如果压根就没有使用 `GestureDetector` 则不存在所谓的冲突，因为每一个节点都能收到事件，只是在 `GestureDetector` 中为了识别语义，它会去决定哪些子节点应该忽略事件，哪些节点应该生效。
2. 解决手势冲突的方法有两种：
	1. 使用 `Listener`。这相当于跳出了手势识别那套规则。
	2. 自定义手势手势识别器（ Recognizer）。

#### Ⅰ、通过 Listener 解决手势冲突

1. 通过 `Listener` 解决手势冲突的原因是竞争只是针对手势的，而 `Listener` 是监听原始指针事件，原始指针事件并非语义话的手势，所以根本不会走手势竞争的逻辑，所以也就不会相互影响。拿上面两个 `Container` 嵌套的例子来说，通过 `Listener` 的解决方式为：

```dart
Listener(  // 将 GestureDetector 换为 Listener 即可
  onPointerUp: (x) => print("2"),
  child: Container(
    width: 200,
    height: 200,
    color: Colors.red,
    alignment: Alignment.center,
    child: GestureDetector(
      onTap: () => print("1"),
      child: Container(
        width: 50,
        height: 50,
        color: Colors.grey,
      ),
    ),
  ),
);
```

2. 代码很简单，只需将 `GestureDetector` 换为 `Listener` 即可，可以两个都换，也可以只换一个。
3. 可以看见，通过 `Listener` 直接识别原始指针事件来解决冲突的方法很简单，因此，当遇到手势冲突时，我们应该优先考虑 `Listener` 。

#### Ⅱ、通过自定义 Recognizer 解决手势冲突

1. 自定义手势识别器的方式比较麻烦，原理是当确定手势竞争胜出者时，会调用胜出者的 `acceptGesture` 方法，表示“宣布成功”，然后会调用其他手势识别其的 `rejectGesture` 方法，表示“宣布失败”。
2. 既然如此，我们可以自定义手势识别器（Recognizer），然后去重写它的 `rejectGesture` 方法：在里面调用 `acceptGesture` 方法，这就相当于它失败是强制将它也变成竞争的成功者了，这样它的回调也就会执行。
3. 我们先自定义tap手势识别器（Recognizer）：

```dart
class CustomTapGestureRecognizer extends TapGestureRecognizer {
  @override
  void rejectGesture(int pointer) {
    //不，我不要失败，我要成功
    //super.rejectGesture(pointer);
    //宣布成功
    super.acceptGesture(pointer);
  }
}

//创建一个新的GestureDetector，用我们自定义的 CustomTapGestureRecognizer 替换默认的
RawGestureDetector customGestureDetector({
  GestureTapCallback? onTap,
  GestureTapDownCallback? onTapDown,
  Widget? child,
}) {
  return RawGestureDetector(
    child: child,
    gestures: {
      CustomTapGestureRecognizer:
          GestureRecognizerFactoryWithHandlers<CustomTapGestureRecognizer>(
        () => CustomTapGestureRecognizer(),
        (detector) {
          detector.onTap = onTap;
        },
      )
    },
  );
}
```

4. 通过 `RawGestureDetector` 来自定义 `customGestureDetector`，`GestureDetector` 中也是通过  `RawGestureDetector` 来包装各种 `Recognizer` 来实现的，我们需要自定义哪个 `Recognizer`，就添加哪个即可。
5. 现在我们看看修改调用代码：

```dart
customGestureDetector( // 替换 GestureDetector
  onTap: () => print("2"),
  child: Container(
    width: 200,
    height: 200,
    color: Colors.red,
    alignment: Alignment.center,
    child: GestureDetector(
      onTap: () => print("1"),
      child: Container(
        width: 50,
        height: 50,
        color: Colors.grey,
      ),
    ),
  ),
);
```

6. 这样就 OK 了，需要注意，这个例子同时说明了一次手势处理过程也是可以有多个胜出者的

## 5、事件总线

1. 在 App 中，我们经常会需要一个广播机制，用以跨页面事件通知，比如一个需要登录的 App 中，页面会关注用户登录或注销事件，来进行一些状态更新。
2. 这时候，一个事件总线便会非常有用，事件总线通常实现了订阅者模式，订阅者模式包含发布者和订阅者两种角色，可以通过事件总线来触发事件和监听事件，本节我们实现一个简单的全局事件总线，我们使用单例模式，代码如下：
3. `01_EventCallback.dart` 事件总线

```dart
/// 订阅者回调签名；函数签名指的是函数的类型和结构，包括函数的参数类型、返回值类型以及函数名。
/// typedef 是 Dart 的关键字，意思是定义一个函数类型。
/// 定义了这个函数类型以后，可以使用 EventCallback 定义变量，这样就可以复用这个函数签名。
typedef void EventCallback(arg);

class EventBus {
  // 私有构造函数
  EventBus._internal();

  // 保存单例
  static final EventBus _singleton = EventBus._internal();

  // 工厂构造函数
  factory EventBus()=> _singleton;

  // 保存事件订阅者队列，key:事件名(id)，value: 对应事件的订阅者队列
  final _emap = <Object, List<EventCallback>?>{};

  // 添加订阅者
  void on(eventName, EventCallback f) {
    // 如果 _emap[eventName] 为空，则赋值为一个空数组
    _emap[eventName] ??=  <EventCallback>[];
    // 将该事件的订阅者 f 添加到队列中
    _emap[eventName]!.add(f);
  }

  // 移除订阅者
  void off(eventName, [EventCallback? f]) {
    var list = _emap[eventName];
    if (eventName == null || list == null) return;
    if (f == null) {
      _emap[eventName] = null;
    } else {
      list.remove(f);
    }
  }

  // 触发事件，事件触发后该事件所有订阅者会被调用
  void emit(eventName, [arg]) {
    var list = _emap[eventName];
    if (list == null) return;
    int len = list.length - 1;
    // 反向遍历，防止订阅者在回调中移除自身带来的下标错位
    for (var i = len; i > -1; --i) {
      list[i](arg);
    }
  }
}

// 定义一个 top-level（全局）变量，页面引入该文件后可以直接使用 bus
var bus = EventBus();
```

4. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '08_事件处理与通知/05_事件总线/03_Login.dart';
import '08_事件处理与通知/05_事件总线/02_LoginMonitor.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: const Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body: 用于定义页面的主要内容区域
           * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
           */
          body: SafeArea(
            child: LoginMonitorComponent()
          )
        ),
      routes: {
        '/login': (context) => const LoginComponent(),
        '/loginMonitor': (context) => const LoginMonitorComponent(),
      },
    );
  }
}
```

5. `02_LoginMonitor.dart` 登录监听页面

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_EventCallback.dart';

class LoginMonitorComponent extends StatefulWidget {
  const LoginMonitorComponent({Key? key}) : super(key: key);

  @override
  _LoginMonitorComponentState createState() => _LoginMonitorComponentState();
}

class _LoginMonitorComponentState extends State<LoginMonitorComponent> {
  var loginMonitor = '未登录';

  @override
  void initState() {
    super.initState();
    // 订阅登录事件
    bus.on('login', (arg) {
      // 更新 Text 的显示
      setState(() {
        loginMonitor = arg; // 假设 loginMonitor 是您用于显示登录信息的变量
      });
      // 打印信息
      print('登录信息: $arg');
    });
  }

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，它可以将其子部件树对齐到屏幕中心
    return Center(
      // Column 是一个小部件，它可以在垂直方向排列其子部件
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            loginMonitor,
            style: const TextStyle(fontSize: 20, color: CupertinoColors.destructiveRed),
          ),
          ElevatedButton(
            child: const Text('跳转至 LoginComponent'),
            onPressed: () { Navigator.pushNamed(context, '/login'); },
          ),
        ],
      )
    );
  }
}
```

6. `03_Login.dart` 登录页面

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_EventCallback.dart';

class LoginComponent extends StatelessWidget {
  const LoginComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，它可以将其子部件树对齐到屏幕中心
    return Center(
      // Column 是一个小部件，它可以在垂直方向排列其子部件
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ElevatedButton(
            child: const Text('登录'),
            onPressed: () {
              // 发送登录事件
              bus.emit('login', '登录成功');
            },
          ),
          ElevatedButton(
            child: const Text('跳转至 LoginMonitorComponent'),
            onPressed: () { Navigator.pop(context); },
          ),
        ],
      )
    );
  }
}
```

7. 效果：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画31.gif)

## 6、通知 Notification

1. 通知（Notification）是 Flutter 中一个重要的机制，在 widget 树中，每一个节点都可以分发通知，通知会沿着当前节点向上传递，所有父节点都可以通过 NotificationListener 来监听通知。
2. Flutter 中将这种由子向父的传递通知的机制称为通知冒泡（Notification Bubbling）。通知冒泡和用户触摸事件冒泡是相似的，但有一点不同：通知冒泡可以中止，但用户触摸事件不行。
3. 注意：通知冒泡和 Web 开发中浏览器事件冒泡原理是相似的，都是事件从出发源逐层向上传递，我们可以在上层节点任意位置来监听通知/事件，也可以终止冒泡过程，终止冒泡后，通知将不会再向上传递。

### ①、监听通知

1. Flutter 中很多地方使用了通知，如前面介绍的 `Scrollable` 组件，它在滑动时就会分发滚动通知（ScrollNotification），而 `Scrollbar` 正是通过监听 `ScrollNotification` 来确定滚动条位置的。
2. 下面是一个监听可滚动组件滚动通知的例子：

```dart
NotificationListener(
  onNotification: (notification){
    switch (notification.runtimeType){
      case ScrollStartNotification: print("开始滚动"); break;
      case ScrollUpdateNotification: print("正在滚动"); break;
      case ScrollEndNotification: print("滚动停止"); break;
      case OverscrollNotification: print("滚动到边界"); break;
    }
  },
  child: ListView.builder(
    itemCount: 100,
    itemBuilder: (context, index) {
      return ListTile(title: Text("$index"),);
    }
  ),
);
```

3. 上例中的滚动通知如 `ScrollStartNotification`、`ScrollUpdateNotification` 等都是继承自 `ScrollNotification` 类，不同类型的通知子类会包含不同的信息，比如 `ScrollUpdateNotification` 有一个 `scrollDelta` 属性，它记录了移动的位移，其他通知属性可以自己查看 SDK 文档。
4. 上例中，我们通过 `NotificationListener` 来监听子 `ListView` 的滚动通知的，`NotificationListener` 定义如下：

```dart
class NotificationListener<T extends Notification> extends StatelessWidget {
  const NotificationListener({
    Key key,
    required this.child,
    this.onNotification,
  }) : super(key: key);
 ...//省略无关代码 
}  
```

5. 我们可以看到：
6. `NotificationListener` 继承自 `StatelessWidget` 类，所以它可以直接嵌套到 Widget 树中。
7. `NotificationListener` 可以指定一个模板参数，该模板参数类型必须是继承自 `Notification`；当显式指定模板参数时，`NotificationListener` 便只会接收该参数类型的通知。举个例子，如果我们将上例子代码改为：

```dart
//指定监听通知的类型为滚动结束通知(ScrollEndNotification)
NotificationListener<ScrollEndNotification>(
  onNotification: (notification){
    //只会在滚动结束时才会触发此回调
    print(notification);
  },
  child: ListView.builder(
    itemCount: 100,
    itemBuilder: (context, index) {
      return ListTile(title: Text("$index"),);
    }
  ),
);
```

8. 上面代码运行后便只会在滚动结束时在控制台打印出通知的信息。
9. `onNotification` 回调为通知处理回调，其函数签名如下：

```dart
// 函数签名指的是函数的类型和结构，包括函数的参数类型、返回值类型以及函数名。
typedef NotificationListenerCallback<T extends Notification> = bool Function(T notification);
```

10. 它的返回值类型为布尔值，当返回值为 true 时，阻止冒泡，其父级 Widget 将再也收不到该通知；当返回值为 false 时继续向上冒泡通知。
11. Flutter 的 UI 框架实现中，除了在可滚动组件在滚动过程中会发出 `ScrollNotification` 之外，还有一些其他的通知，如 `SizeChangedLayoutNotification`、`KeepAliveNotification` 、`LayoutChangedNotification` 等，Flutter 正是通过这种通知机制来使父元素可以在一些特定时机来做一些事情

### ②、自定义通知

1. 除了 Flutter 内部通知，我们也可以自定义通知，下面我们看看如何实现自定义通知：
2. 定义一个通知类，要继承自Notification类；

```dart
class MyNotification extends Notification {
  MyNotification(this.msg);
  final String msg;
}
```

2. 分发通知：`Notification` 有一个 `dispatch(context)` 方法，它是用于分发通知的，我们说过 `context` 实际上就是操作 `Element` 的一个接口，它与 `Element` 树上的节点是对应的，通知会从 `context` 对应的 `Element` 节点向上冒泡。
3. 下面我们看一个完整的例子：

```dart
class NotificationRoute extends StatefulWidget {
  @override
  NotificationRouteState createState() {
    return NotificationRouteState();
  }
}

class NotificationRouteState extends State<NotificationRoute> {
  String _msg="";
  @override
  Widget build(BuildContext context) {
    //监听通知  
    return NotificationListener<MyNotification>(
      onNotification: (notification) {
        setState(() {
          _msg+=notification.msg+"  ";
        });
       return true;
      },
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
//           ElevatedButton(
//           onPressed: () => MyNotification("Hi").dispatch(context),
//           child: Text("Send Notification"),
//          ),  
            Builder(
              builder: (context) {
                return ElevatedButton(
                  //按钮点击时分发通知  
                  onPressed: () => MyNotification("Hi").dispatch(context),
                  child: Text("Send Notification"),
                );
              },
            ),
            Text(_msg)
          ],
        ),
      ),
    );
  }
}

class MyNotification extends Notification {
  MyNotification(this.msg);
  final String msg;
}
```

4. 上面代码中，我们每点一次按钮就会分发一个 `MyNotification` 类型的通知，我们在 Widget 根上监听通知，收到通知后我们将通知通过 `Text` 显示在屏幕上。
5. 注意：代码中注释的部分是不能正常工作的，因为这个 `context` 是根 Context，而 `NotificationListener` 是监听的子树，所以我们通过 Builder 来构建 `ElevatedButton`，来获得按钮位置的 `context`。
6. 运行效果如图所示：

![|260](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231128145714.png)

### ③、阻止通知冒泡

1. 我们将上面的例子改为：

```dart
class NotificationRouteState extends State<NotificationRoute> {
  String _msg="";
  @override
  Widget build(BuildContext context) {
    //监听通知
    return NotificationListener<MyNotification>(
      onNotification: (notification){
        print(notification.msg); //打印通知
        return false;
      },
      child: NotificationListener<MyNotification>(
        onNotification: (notification) {
          setState(() {
            _msg+=notification.msg+"  ";
          });
          return false; 
        },
        child: ...//省略重复代码
      ),
    );
  }
}
```

2. 上列中两个 `NotificationListener` 进行了嵌套，子 `NotificationListener` 的 `onNotification` 回调返回 `false`，表示不阻止冒泡，所以父 `NotificationListener` 仍然会受到通知，所以控制台会打印出通知信息；
3. 如果将子 `NotificationListener` 的 `onNotification` 回调的返回值改为 `true`，则父 `NotificationListener` 便不会再打印通知了，因为子 `NotificationListener` 已经终止通知冒泡了。

### ④、冒泡原理

1. 我们在上面介绍了通知冒泡的现象及使用，现在我们更深入一些，介绍一下 Flutter 框架中是如何实现通知冒泡的。为了搞清楚这个问题，就必须看一下源码，我们从通知分发的源头出发，然后再顺藤摸瓜。由于通知是通过 `Notification` 的 `dispatch(context)` 方法发出的，那我们先看看 `dispatch(context)` 方法中做了什么，下面是相关源码：

```dart
void dispatch(BuildContext target) {
  target?.visitAncestorElements(visitAncestor);
}
```

2. `dispatch(context)` 中调用了当前 `context` 的 `visitAncestorElements` 方法，该方法会从当前 Element 开始向上遍历父级元素；`visitAncestorElements` 有一个遍历回调参数，在遍历过程中对遍历到的父级元素都会执行该回调。遍历的终止条件是：已经遍历到根 Element 或某个遍历回调返回 `false`。源码中传给 `visitAncestorElements` 方法的遍历回调为 `visitAncestor` 方法，我们看看 `visitAncestor` 方法的实现：

```dart
//遍历回调，会对每一个父级Element执行此回调
bool visitAncestor(Element element) {
  //判断当前element对应的Widget是否是NotificationListener。
  
  //由于NotificationListener是继承自StatelessWidget，
  //故先判断是否是StatelessElement
  if (element is StatelessElement) {
    //是StatelessElement，则获取element对应的Widget，判断
    //是否是NotificationListener 。
    final StatelessWidget widget = element.widget;
    if (widget is NotificationListener<Notification>) {
      //是NotificationListener，则调用该NotificationListener的_dispatch方法
      if (widget._dispatch(this, element)) 
        return false;
    }
  }
  return true;
}
```

3. `visitAncestor` 会判断每一个遍历到的父级 Widget 是否是 `NotificationListener`，如果不是，则返回 `true` 继续向上遍历，如果是，则调用 `NotificationListener` 的 `_dispatch` 方法，我们看看 `_dispatch` 方法的源码：

```dart
  bool _dispatch(Notification notification, Element element) {
    // 如果通知监听器不为空，并且当前通知类型是该NotificationListener
    // 监听的通知类型，则调用当前NotificationListener的onNotification
    if (onNotification != null && notification is T) {
      final bool result = onNotification(notification);
      // 返回值决定是否继续向上遍历
      return result == true; 
    }
    return false;
  }
```

4. 我们可以看到 `NotificationListener` 的 `onNotification` 回调最终是在 `_dispatch` 方法中执行的，然后会根据返回值来确定是否继续向上冒泡。上面的源码实现其实并不复杂，通过阅读这些源码，一些额外的点可以注意一下：
	1. Context 上也提供了遍历 Element 树的方法。
	2. 我们可以通过 `Element.widget` 得到 element 节点对应的 widget

# 九、文件操作与网络请求

## 1、文件操作

### ①、简介

1. Dart 的 IO 库包含了文件读写的相关类，它属于 Dart 语法标准的一部分，所以通过 Dart IO 库，无论是 Dart VM 下的脚本还是 Flutter，都是通过 Dart IO 库来操作文件的
2. 不过和 Dart VM 相比，Flutter 有一个重要差异是文件系统路径不同，这是因为 Dart VM 是运行在 PC 或服务器操作系统下，而 Flutter 是运行在移动操作系统中，他们的文件系统会有一些差异。
3. Android 和 iOS 的应用存储目录不同，`PathProvider` 插件提供了一种平台透明的方式来访问设备文件系统上的常用位置。该类当前支持访问两个文件系统位置：
	1. 临时目录：可以使用 `getTemporaryDirectory()` 来获取临时目录； 系统可随时清除临时目录的文件。
		1. 在 iOS 上，这对应于 `NSTemporaryDirectory()` 返回的值。
		2. 在 Android 上，这是 `getCacheDir()`返回的值。
	2. 文档目录：可以使用 `getApplicationDocumentsDirectory()` 来获取应用程序的文档目录，该目录用于存储只有自己可以访问的文件。只有当应用程序被卸载时，系统才会清除该目录。
		1. 在 iOS 上，这对应于 `NSDocumentDirectory`。
		2. 在 Android 上，这是 AppData 目录。
	3. 外部存储目录：可以使用 `getExternalStorageDirectory()` 来获取外部存储目录，如 SD 卡；
		1. 由于 iOS 不支持外部目录，所以在 iOS 下调用该方法会抛出 `UnsupportedError` 异常
		2. 在 Android 下结果是 Android SDK 中 `getExternalStorageDirectory` 的返回值。
4. 一旦 Flutter 应用程序有一个文件位置的引用，可以使用 dart io API 来执行对文件系统的读/写操作。
5. 有关使用 Dart 处理文件和目录的详细内容可以参考 Dart 语言文档

### ②、示例

- 我们还是以计数器为例，实现在应用退出重启后可以恢复点击次数。 这里，我们使用文件来保存数据：

1. 引入 `PathProvider` 插件；在 `pubspec.yaml` 文件中添加如下声明：
2. 添加后，执行 `flutter packages get` 获取一下, 版本号可能随着时间推移会发生变化，可以使用最新版。

```yaml
path_provider: ^2.0.2
```

```dart
dependencies:
  flutter:
    sdk: flutter

  # path_provider 插件用于查找常用位置的路径，例如临时目录
  path_provider: ^2.0.2
```

3. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '09_文件操作与网络请求/01_文件操作/01_FileOperationComponent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body: 用于定义页面的主要内容区域
           * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
           */
          body: SafeArea(
            child: FileOperationComponent()
          )
        )
    );
  }
}
```

4. `01_FileOperationComponent.dart` 文件操作类

```dart
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';


class FileOperationComponent extends StatefulWidget {
  const FileOperationComponent({Key? key}) : super(key: key);

  @override
  _FileOperationComponentState createState() => _FileOperationComponentState();
}

class _FileOperationComponentState extends State<FileOperationComponent> {
  // 点击次数
  int _counter = 0;

  @override
  void initState() {
    super.initState();
    // 从文件读取点击次数；读取后，调用 setState() 更新 UI
    _readCounter().then((int value) {
      setState(() {
        _counter = value;
      });
    });
  }

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个小部件，用于在垂直方向上排列其子部件
      child: Column(
        children: [
          Text('点击了 $_counter 次'),
          ElevatedButton(
            onPressed: () { _incrementCounter(); },
            child: const Icon(Icons.add)
          ),
        ],
      ),
    );
  }

  /// 点击按钮后，将点击次数自增并写入文件
  _incrementCounter() async {
    setState(() {
      _counter++;
    });
    // 将点击次数以字符串类型写到文件中
    await (await _getLocalFile()).writeAsString('$_counter');
  }

  /// 获取本地文件目录中的文件 count.txt
  Future<File> _getLocalFile() async {
    // 获取应用目录
    String dir = (await getApplicationDocumentsDirectory()).path;
    print(dir);
    // 返回应用目录中的文件
    return File('$dir/counter.txt');
  }

  /// 从文件中读取点击次数，以字符串类型返回
  Future<int> _readCounter() async {
    try {
      File file = await _getLocalFile();
      // 读取点击次数（以字符串）
      String contents = await file.readAsString();
      return int.parse(contents);
    } on FileSystemException {
      return 0;
    }
  }

}
```

5. 效果：

![|401](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画32.gif)

6. 上面代码比较简单，不再赘述，需要说明的是，本示例只是为了演示文件读写，而在实际开发中，如果要存储一些简单的数据，使用 `shared_preferences` 插件会比较简单。

## 2、通过 HttpClient 发起 HTTP 请求

### ①、HttpClient 简介

- Dart IO 库中提供了用于发起 Http 请求的一些类，我们可以直接使用 `HttpClient` 来发起请求。使用 `HttpClient` 发起请求分为五步：
1. 创建一个 `HttpClient`：

```dart
HttpClient httpClient = HttpClient();
```

2. 打开 Http 连接，设置请求头：

```dart
HttpClientRequest request = await httpClient.getUrl(uri);
```

- 这一步可以使用任意 `Http Method`，如 `httpClient.post(...)`、`httpClient.delete(...)` 等。如果包含 Query 参数，可以在构建 uri 时添加，如：

```dart
Uri uri = Uri(scheme: "https", host: "flutterchina.club", queryParameters: {
    "xx":"xx",
    "yy":"dd"
  });
```

- 通过 `HttpClientRequest` 可以设置请求 `header`，如：

```dart
request.headers.add("user-agent", "test");
```

- 如果是 post 或 put 等可以携带请求体方法，可以通过 `HttpClientRequest` 对象发送请求体，如：

```dart
String payload="...";
request.add(utf8.encode(payload)); 
// request.addStream(_inputStream); //可以直接添加输入流
```

3. 等待连接服务器，这一步完成后，请求信息就已经发送给服务器了，返回一个 `HttpClientResponse` 对象，它包含响应头（header）和响应流(响应体的Stream)，接下来就可以通过读取响应流来获取响应内容。

```dart
HttpClientResponse response = await request.close();
```

4. 读取响应内容，我们通过读取响应流来获取服务器返回的数据，在读取时我们可以设置编码格式，这里是 utf8。

```dart
String responseBody = await response.transform(utf8.decoder).join();
```

5. 请求结束，关闭 `HttpClient`，关闭 client 后，通过该 client 发起的所有请求都会终止。

```dart
httpClient.close();
```

### ②、示例

1. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '09_文件操作与网络请求/02_通过 HttpClient 发起 HTTP 请求/01_HttpClientComponent.dart';
import '09_文件操作与网络请求/03_Http 请求库 dio/01_HttpDioComponent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body: 用于定义页面的主要内容区域
           * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
           */
          body: SafeArea(
            child: HttpClientComponent()
          )
        )
    );
  }
}
```

2. `01_HttpClientComponent.dart` HttpClient 测试类

```dart
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';


class HttpClientComponent extends StatefulWidget {
  const HttpClientComponent({Key? key}) : super(key: key);

  @override
  _HttpClientComponentState createState() => _HttpClientComponentState();
}

class _HttpClientComponentState extends State<HttpClientComponent> {
  bool _loading = false;
  String _text = "";

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个小部件，用于在垂直方向上排列其子部件
      child: Column(
        children: [
          ElevatedButton(
            onPressed: _loading ? null : request,
            child: Text("请求 月海"),
          ),
          Container(
            width: MediaQuery.of(context).size.width - 50.0,
            child: Text(_text.replaceAll(RegExp(r"\s"), "")),
          )
        ],
      ),
    );
  }

  request() async {
    setState(() {
      _loading = true;
      _text = "正在请求...";
    });

    try {
      // 1、创建一个 HttpClient
      HttpClient httpClient = HttpClient();

      // 2.1、创建 uri；若是 https 请求，则使用 `Uri.https`，而不是 `Uri.http`
      // 参数 1：请求的地址； 参数 2：请求的路径； 参数 3：请求的参数
      Uri uri = Uri.http("101.200.86.248:9001", "/hello/helloTest", {});
      // 2.2、打开 Http 连接，设置请求头
      HttpClientRequest request = await httpClient.getUrl(uri);

      // 2.3、通过 HttpClientRequest 可以设置请求 header，使用 iPhone 的 UA
      request.headers.add(
        "user-agent",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
      );

      // 3、等待连接服务器（会将请求信息发送给服务器）
      HttpClientResponse response = await request.close();

      // 4、读取响应内容
      _text = await response.transform(utf8.decoder).join();

      // 5、关闭 client 后，通过该 client 发起的所有请求都会终止。
      httpClient.close();

    } catch (e) {
      _text = "请求失败：$e";
    } finally {
      setState(() {
        _loading = false;
      });
    }
  }

}
```

3. 效果：

![|401](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画33.gif)

### ③、HttpClient 配置

1. `HttpClient` 有很多属性可以配置，常用的属性列表如下：

| 属性                  | 含义                                                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| idleTimeout           | 对应请求头中的keep-alive字段值，为了避免频繁建立连接，httpClient在请求结束后会保持连接一段时间，超过这个阈值后才会关闭连接。     |
| connectionTimeout     | 和服务器建立连接的超时，如果超过这个值则会抛出SocketException异常。                                                              |
| maxConnectionsPerHost | 同一个host，同时允许建立连接的最大数量。                                                                                         |
| autoUncompress        | 对应请求头中的Content-Encoding，如果设置为true，则请求头中Content-Encoding的值为当前HttpClient支持的压缩算法列表，目前只有"gzip" |
| userAgent             | 对应请求头中的User-Agent字段。                                                                                                   |

2. 可以发现，有些属性只是为了更方便的设置请求头，对于这些属性，完全可以通过 `HttpClientRequest` 直接设置 header
3. 不同的是通过 `HttpClient` 设置的对整个 `httpClient` 都生效，而通过 `HttpClientRequest` 设置的只对当前请求生效

### ④、HTTP 请求认证

1. Http 协议的认证（Authentication）机制可以用于保护非公开资源。如果 Http 服务器开启了认证，那么用户在发起请求时就需要携带用户凭据，如果你在浏览器中访问了启用 Basic 认证的资源时，浏览就会弹出一个登录框，如图：

![|400](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231129132448.png)

2. 我们先看看 Basic 认证的基本过程：
3. 客户端发送 http 请求给服务器，服务器验证该用户是否已经登录验证过了，如果没有的话，  服务器会返回一个401 Unauthozied 给客户端，并且在响应 header 中添加一个 “WWW-Authenticate” 字段，例如：

```dart
WWW-Authenticate: Basic realm="admin"
```

4. 其中 Basic 为认证方式，realm 为用户角色的分组，可以在后台添加分组。
5. 客户端得到响应码后，将用户名和密码进行 base64 编码（格式为用户名:密码），设置请求头 Authorization，继续访问 :

```dart
Authorization: Basic YXXFISDJFISJFGIJIJG
```

6. 服务器验证用户凭据，如果通过就返回资源内容。
7. 注意，Http 的方式除了 Basic 认证之外还有：Digest 认证、Client 认证、Form Based 认证等，目前 Flutter 的 HttpClient 只支持 Basic 和 Digest 两种认证方式，这两种认证方式最大的区别是发送用户凭据时，对于用户凭据的内容，前者只是简单的通过 Base64 编码（可逆），而后者会进行哈希运算，相对来说安全一点点，但是为了安全起见，无论是采用 Basic 认证还是 Digest 认证，都应该在 Https 协议下，这样可以防止抓包和中间人攻击。
8. HttpClient 关于 Http 认证的方法和属性：

```dart
addCredentials(Uri url, String realm, HttpClientCredentials credentials)
```

9. 该方法用于添加用户凭据,如：

```dart
httpClient.addCredentials(_uri,
 "admin", 
  HttpClientBasicCredentials("username","password"), //Basic认证凭据
);
```

10. 如果是 Digest 认证，可以创建 Digest 认证凭据：

```dart
HttpClientDigestCredentials("username","password")
authenticate(Future<bool> f(Uri url, String scheme, String realm))
```

11. 这是一个 setter，类型是一个回调，当服务器需要用户凭据且该用户凭据未被添加时，httpClient 会调用此回调，在这个回调当中，一般会调用 `addCredential()` 来动态添加用户凭证，例如：

```dart
httpClient.authenticate=(Uri url, String scheme, String realm) async{
  if(url.host=="xx.com" && realm=="admin"){
    httpClient.addCredentials(url,
      "admin",
      HttpClientBasicCredentials("username","pwd"), 
    );
    return true;
  }
  return false;
};
```

12. 一个建议是，如果所有请求都需要认证，那么应该在 HttpClient 初始化时就调用 `addCredentials()` 来添加全局凭证，而不是去动态添加

### ⑤、代理

1. 可以通过 `findProxy` 来设置代理策略，例如，我们要将所有请求通过代理服务器（192.168.1.2:8888）发送出去：

```dart
client.findProxy = (uri) {
    // 如果需要过滤uri，可以手动判断
    return "PROXY 192.168.1.2:8888";
 };
```

2. `findProxy` 回调返回值是一个遵循浏览器 PAC 脚本格式的字符串，详情可以查看 API 文档，如果不需要代理，返回 `DIRECT` 即可。
3. 在 APP 开发中，很多时候我们需要抓包来调试，而抓包软件(如charles)就是一个代理，这时我们就可以将请求发送到我们的抓包软件，我们就可以在抓包软件中看到请求的数据了。
4. 有时代理服务器也启用了身份验证，这和 http 协议的认证是相似的，`HttpClient` 提供了对应的 Proxy 认证方法和属性：

```dart
set authenticateProxy(
    Future<bool> f(String host, int port, String scheme, String realm));
void addProxyCredentials(
    String host, int port, String realm, HttpClientCredentials credentials);
```

5. 他们的使用方法和上面 HTTP 请求认证一节中介绍的 `addCredentials` 和 `authenticate` 相同，故不再赘述

## 3、Http 请求库 dio

### ①、引入 dio

1. 引入dio:

```yaml
dependencies:
  flutter:
    sdk: flutter

  # 以下添加了 Cupertino Icons 字体到您的应用程序，
  # 以便您可以使用 CupertinoIcons 类来使用 iOS 风格的图标。
  cupertino_icons: ^1.0.2

  # path_provider 插件用于查找常用位置的路径，例如临时目录
  path_provider: ^2.0.2
  
  # dio 是一个强大的 Dart Http 请求库，支持 Restful API、FormData、拦截器、请求取消、Cookie 管理、文件上传/下载、超时等
  dio: ^4.0.0
```

2. 导入并创建 dio 实例：

```dart
import 'package:dio/dio.dart';
Dio dio =  Dio();
```

3. 接下来就可以通过 dio 实例来发起网络请求了
4. 注意，一个 dio 实例可以发起多个 http 请求，一般来说，APP 只有一个 http 数据源时，dio 应该使用单例模式

### ②、通过 dio 发起请求

1. 发起 GET 请求 :

```dart
Response response;
response=await dio.get("/test?id=12&name=wendu")
print(response.data.toString());
```

2. 对于 GET 请求我们可以将 `query` 参数通过对象来传递，上面的代码等同于：

```dart
response=await dio.get("/test",queryParameters:{"id":12,"name":"wendu"})
print(response);
```

3. 发起一个 POST 请求:

```dart
response=await dio.post("/test",data:{"id":12,"name":"wendu"})
```

4. 发起多个并发请求:

```dart
response= await Future.wait([dio.post("/info"),dio.get("/token")]);
```

5. 下载文件:

```dart
response=await dio.download("https://www.google.com/",_savePath);
```

6. 发送 FormData，如果发送的数据是 FormData，则 dio 会将请求 header 的 `contentType` 设为 `multipart/form-data`

```dart
FormData formData = FormData.from({
   "name": "wendux",
   "age": 25,
});
response = await dio.post("/info", data: formData)
```

7. 通过 FormData 上传多个文件:

```dart
FormData formData = FormData.from({
   "name": "wendux",
   "age": 25,
   "file1": UploadFileInfo(File("./upload.txt"), "upload1.txt"),
   "file2": UploadFileInfo(File("./upload.txt"), "upload2.txt"),
     // 支持文件数组上传
   "files": [
      UploadFileInfo(File("./example/upload.txt"), "upload.txt"),
      UploadFileInfo(File("./example/upload.txt"), "upload.txt")
    ]
});
response = await dio.post("/info", data: formData)
```

8. 值得一提的是，dio 内部仍然使用 HttpClient 发起的请求，所以代理、请求认证、证书校验等和 HttpClient 是相同的，我们可以在 `onHttpClientCreate` 回调中设置，例如：

```dart
(dio.httpClientAdapter as DefaultHttpClientAdapter).onHttpClientCreate = (client) {
    //设置代理 
    client.findProxy = (uri) {
      return "PROXY 192.168.1.2:8888";
    };
    //校验证书
    httpClient.badCertificateCallback=(X509Certificate cert, String host, int port){
      if(cert.pem==PEM){
      return true; //证书一致，则允许发送数据
     }
     return false;
    };   
  };
```

9. 注意，`onHttpClientCreate` 会在当前 dio 实例内部需要创建 HttpClient 时调用，所以通过此回调配置 HttpClient 会对整个 dio 实例生效，如果应用需要多种代理或证书校验策略，可以创建不同的 dio 实例来分别实现。

### ③、实例

1. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '09_文件操作与网络请求/03_Http 请求库 dio/01_HttpDioComponent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body: 用于定义页面的主要内容区域
           * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
           */
          body: SafeArea(
            child: HttpDioComponent()
          )
        )
    );
  }
}
```

2. `01_HttpDioComponent.dart` Dio 测试类

```dart
import 'dart:convert';
import 'dart:io';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';


class HttpDioComponent extends StatefulWidget {
  const HttpDioComponent({Key? key}) : super(key: key);

  @override
  _HttpDioComponentState createState() => _HttpDioComponentState();
}

class _HttpDioComponentState extends State<HttpDioComponent> {
  Dio _dio = Dio();

  bool _loading = false;
  String _text = "";

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个小部件，用于在垂直方向上排列其子部件
      child: Column(
        children: [
          ElevatedButton(
            onPressed: _loading ? null : request,
            child: const Text("请求 月海"),
          ),
          SizedBox(
            width: MediaQuery.of(context).size.width - 50.0,
            // _text.replaceAll(RegExp(r"\s"), "") 去除字符串中的空格
            child: Text(_text.replaceAll(RegExp(r"\s"), "")),
          )
        ],
      ),
    );
  }

  request() async {
    setState(() {
      _loading = true;
      _text = "正在请求...";
    });

    try {
      Response response = await _dio.get("http://101.200.86.248:9001/hello/helloTest");
      setState(() {
        _text = response.data.toString();
      });

    } catch (e) {
      _text = "请求失败：$e";
    } finally {
      setState(() {
        _loading = false;
      });
    }
  }

}
```

3. 效果：

![|401](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画33.gif)

## 4、使用 WebSockets

### ①、简介

1. Http 协议是无状态的，只能由客户端主动发起，服务端再被动响应，服务端无法向客户端主动推送内容，并且一旦服务器响应结束，链接就会断开(见注解部分)，所以无法进行实时通信。
2. WebSocket 协议正是为解决客户端与服务端实时通信而产生的技术，现在已经被主流浏览器支持，所以对于 Web 开发者来说应该比较熟悉了，Flutter 也提供了专门的包来支持 WebSocket 协议。
3. 注意：Http 协议中虽然可以通过 keep-alive 机制使服务器在响应结束后链接会保持一段时间，但最终还是会断开， keep-alive 机制主要是用于避免在同一台服务器请求多个资源时频繁创建链接，它本质上是支持链接复用的技术，而并非用于实时通信，需要知道这两者的区别。
4. WebSocket 协议本质上是一个基于 tcp 的协议，它是先通过 HTTP 协议发起一条特殊的 http 请求进行握手后，如果服务端支持 WebSocket 协议，则会进行协议升级。WebSocket 会使用 http 协议握手后创建的 tcp 链接，和 http 协议不同的是，WebSocket 的 tcp 链接是个长链接（不会断开），所以服务端与客户端就可以通过此 TCP 连接进行实时通信。

### ②、通信步骤

- 使用 WebSocket 通信分为四个步骤：
1. 引入 WebSocket
2. 连接到 WebSocket 服务器。
3. 监听来自服务器的消息。
4. 将数据发送到服务器。
5. 关闭 WebSocket 连接

#### Ⅰ、引入 WebSocket

1. 在 `pubspec.yaml` 文件中引入 `web_socket_channel`

```yaml
dependencies:
  flutter:
    sdk: flutter

  # 以下添加了 Cupertino Icons 字体到您的应用程序，
  # 以便您可以使用 CupertinoIcons 类来使用 iOS 风格的图标。
  cupertino_icons: ^1.0.2

  # path_provider 插件用于查找常用位置的路径，例如临时目录
  path_provider: ^2.0.2
  
  # dio 是一个强大的 Dart Http 请求库，支持 Restful API、FormData、拦截器、请求取消、Cookie 管理、文件上传/下载、超时等
  dio: ^4.0.0
  
  # web_socket_channel 是一个 Dart 包，它提供了一个 StreamChannel 的实现，用于通过 WebSocket 进行通信
  web_socket_channel: ^2.1.0
```

2. 在项目根文件夹中运行 `flutter packages get` (或者在编辑器中点击 “Packages Get”) 以在项目中使用这些新的依赖项

#### Ⅱ、连接到 WebSocket 服务器

1. [web_socket_channel](https://pub.dev/packages/web_socket_channel) package 提供了我们需要连接到 WebSocket 服务器的工具。该 package 提供了一个 WebSocketChannel 允许我们既可以监听来自服务器的消息，又可以将消息发送到服务器的方法。
2. 在 Flutter 中，我们可以创建一个 WebSocketChannel 连接到一台服务器：

```dart
final channel = IOWebSocketChannel.connect('wss://echo.websocket.events');
```

3. 注意：`wss://echo.websocket.events` 为 flutter.cn 提供的测试服务地址。

#### Ⅱ、监听来自服务器的消息

1. 现在我们建立了连接，我们可以监听来自服务器的消息，在我们发送消息给测试服务器之后，它会返回相同的消息。
2. 我们如何收取消息并显示它们？在这个例子中，我们将使用一个 StreamBuilder 来监听新消息， 并用一个 Text 来显示它们。

```dart
StreamBuilder(
  stream: widget.channel.stream,
  builder: (context, snapshot) {
    return Text(snapshot.hasData ? '${snapshot.data}' : '');
  },
);
```

3. WebSocketChannel 提供了一个来自服务器的消息 `Stream` 。该 `Stream` 类是 `dart:async` 包中的一个基础类。它提供了一种方法来监听来自数据源的异步事件。与 Future 返回单个异步响应不同，`Stream` 类可以随着时间推移传递很多事件。
4. 该 `StreamBuilder` 组件将连接到一个 `Stream`， 并在每次收到消息时通知 Flutter 重新构建界面

#### Ⅲ、将数据发送到服务器

1. 为了将数据发送到服务器，我们会 `add` 消息给 `WebSocketChannel` 提供的 `sink`。

```dart
channel.sink.add('Hello!');
```

2. `WebSocketChannel` 提供了一个 `StreamSink`，它将消息发给服务器。
3. `StreamSink` 类提供了给数据源同步或异步添加事件的一般方法

#### Ⅳ、关闭 WebSocket 连接

1. 在我们使用 WebSocket 后，要关闭连接：

```dart
channel.sink.close();
```

### ③、实例

1. `main` 主启动类

```dart
import 'package:flutter/material.dart';

import '09_文件操作与网络请求/04_使用 WebSockets/01_WebSocketsComponent.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return const MaterialApp(
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
        home: Scaffold(
          // 设置背景颜色为白色
          backgroundColor: Colors.white,
          /**
           * body: 用于定义页面的主要内容区域
           * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
           */
          body: SafeArea(
            child: WebSocketsComponent()
          )
        )
    );
  }
}
```

2. `01_WebSocketsComponent.dart` WebSockets 测试方法

```dart
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:web_socket_channel/io.dart';

class WebSocketsComponent extends StatefulWidget {
  const WebSocketsComponent({Key? key}) : super(key: key);

  @override
  _WebSocketsComponentState createState() => _WebSocketsComponentState();
}

class _WebSocketsComponentState extends State<WebSocketsComponent> {
  // 创建一个 TextEditingController 对象，用于获取输入框的值
  final TextEditingController _controller = TextEditingController();
  // 添加一个 ScrollController 对象，用于控制 ListView 的滚动
  final ScrollController _scrollController = ScrollController();
  // 创建一个 IOWebSocketChannel 对象，用于创建 WebSocket 连接
  late IOWebSocketChannel channel;
  // 创建一个 StreamSubscription 对象，用于订阅消息，以便接收消息
  late StreamSubscription<dynamic> _subscription;

  // 保存消息列表
  final List<String> _messageList = [];

  @override
  void initState() {
    super.initState();
    // 创建 websocket 连接
    channel = IOWebSocketChannel.connect('wss://echo.websocket.events');

    // 订阅消息，接收到消息后将消息添加到 _messageList 中，
    _subscription = channel.stream.listen((data) {
      setState(() {
        // 处理接收到的消息
        _messageList.add("接收：$data");
      });
      // 在发送消息后调用 _scrollToBottom 方法滚动到最底部
      _scrollToBottom();
    });
  }

  @override
  void dispose() {
    // 取消订阅
    _subscription.cancel();
    // 关闭 WebSocket 连接
    channel.sink.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Column 是一个小部件，它接受一个 Widget 数组作为参数，用于按垂直方向排列其子部件
    return Column(
      children: [
        // 构建消息输入框和发送按钮
        buildMessageInputAndSendButton(context),
        // Expanded 是一个小部件，它可以用来扩展 Row、Column 或 Flex 的子部件，以便填充可用的空间
        Expanded(
          // 构建消息列表
          child: buildMessageList(context),
        ),
      ],
    );
  }

  /// 构建消息输入框和发送按钮
  Widget buildMessageInputAndSendButton(BuildContext context) {
    // Row 是一个小部件，它接受一个 Widget 数组作为参数，用于按水平方向排列其子部件
    return Row(
      children: [
        // Expanded 是一个小部件，它可以用来扩展 Row、Column 或 Flex 的子部件，以便填充可用的空间
        Expanded(
          // TextField 是一个小部件，用于接收用户输入的文本
          child: TextField(
            controller: _controller,
            decoration: const InputDecoration(hintText: '请输入消息'),
          )
        ),
        // ElevatedButton 是一个小部件，用于创建一个悬浮按钮
        ElevatedButton(
          onPressed: _sendMessage,
          child: const Text('发送'),
        )
      ],
    );
  }

  /// 构建消息列表
  Widget buildMessageList(BuildContext context) {
    // Scrollbar：显示滚动条
    return Scrollbar(
      // ListView 列表组件
      child: ListView.separated (
        // 将 ScrollController 对象传递给 ListView 的 controller 属性
        controller: _scrollController,
        // itemCount：列表项的数量
        itemCount: _messageList.length,
        /**
         * itemBuilder：它是列表项的构建器，类型为 IndexedWidgetBuilder，返回值为一个 widget。
         * 当列表滚动到具体的 index 位置时，会调用该构建器构建列表项
         */
        itemBuilder: (BuildContext context, int index) {
          return Text(_messageList[index]);
        },
        // 分割器构造器
        separatorBuilder: (context, index) => const Divider(color: Colors.red),
      )
    );
  }

  /// 发送消息
  void _sendMessage() {
    // 判断输入框是否为空
    if (_controller.text.isNotEmpty) {
      // 发送消息
      channel.sink.add(_controller.text);
      // 将消息添加到 _messageList 中，并调用 setState 方法更新 UI
      setState(() {
        _messageList.add("发送：${_controller.text}");
      });
      // 在发送消息后调用 _scrollToBottom 方法滚动到最底部
      _scrollToBottom();
    }
  }

  /// 滚动到最底部
  void _scrollToBottom() {
    // WidgetsBinding.instance.addPostFrameCallback 方法会在当前帧绘制完成后执行回调
    WidgetsBinding.instance.addPostFrameCallback((_) {
      // animateTo 方法可以滚动到指定的位置
      _scrollController.animateTo(
        // 获取滚动条的最大滚动位置
        _scrollController.position.maxScrollExtent,
        // 滚动动画的持续时间
        duration: const Duration(milliseconds: 100),
        // 滚动动画的曲线
        curve: Curves.easeOut,
      );
    });
  }
}
```

3. 效果：

![|395](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画34.gif)

4. 上面的例子比较简单，不再赘述。我们现在思考一个问题，假如我们想通过 WebSocket 传输二进制数据应该怎么做（比如要从服务器接收一张图片）？
5. 我们发现 `StreamBuilder` 和 `Stream` 都没有指定接收类型的参数，并且在创建 WebSocket 链接时也没有相应的配置，貌似没有什么办法……
6. 其实很简单，要接收二进制数据仍然使用 `StreamBuilder`，因为 WebSocket 中所有发送的数据使用帧的形式发送，而帧是有固定格式，每一个帧的数据类型都可以通过 `Opcode` 字段指定，它可以指定当前帧是文本类型还是二进制类型（还有其他类型），所以客户端在收到帧时就已经知道了其数据类型，所以 flutter 完全可以在收到数据后解析出正确的类型，所以就无需开发者去关心，当服务器传输的数据是指定为二进制时，`StreamBuilder` 的 `snapshot.data` 的类型就是 `List<int>`，是文本时，则为 `String`

## 5、使用Socket API

### ①、Socket 简介

1. Socket API 是操作系统为实现应用层网络协议提供的一套基础的、标准的 API，它是对传输层网络协议（主要是TCP/UDP）的一个封装。
2. Socket API 实现了端到端建立链接和发送/接收数据的基础 API，而高级编程语言中的 Socket API 其实都是对操作系统 Socket API 的一个封装。
3. 我们之前介绍的 Http 协议和 WebSocket 协议都属于应用层协议，除了它们，应用层协议还有很多如：SMTP、FTP 等，这些应用层协议都是通过 Socket API 来实现的。
4. 综上，如果我们需要自定义协议或者想直接来控制管理网络链接、又或者我们觉得自带的 HttpClient 不好用想重新实现一个，这时我们就需要使用 Socket。
5. Flutter 的 Socket API 在 `dart:io` 包中，下面我们看一个使用 Socket 实现简单 http 请求的示例

### ②、使用 Socket 实现Http Get请求

1. 以请求百度首页为例：

```dart
class SocketRoute extends StatelessWidget {
  const SocketRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: _request(),
      builder: (context, snapShot) {
        return Text(snapShot.data.toString());
      },
    );
  }

  _request() async {
    // 建立连接
    var socket = await Socket.connect("baidu.com", 80);
    // 根据 http 协议，发起 Get 请求头
    socket.writeln("GET / HTTP/1.1");
    socket.writeln("Host:baidu.com");
    socket.writeln("Connection:close");
    socket.writeln();
    await socket.flush(); // 发送
    // 读取返回内容，按照 utf8 解码为字符串
    String _response = await utf8.decoder.bind(socket).join();
    await socket.close();
    return _response;
  }
}
```

2. 可以看到，使用 Socket 需要我们自己实现 Http 协议（需要自己实现和服务器的通信过程），本例只是一个简单示例，没有处理重定向、cookie 等。
3. 运行后效果如图所示：

![|360](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231201144144.png)

4. 可以看到响应内容分两个部分，第一部分是响应头，第二部分是响应体，服务端可以根据请求信息动态来输出响应体。
5. 由于本示例请求头比较简单，所以响应体和浏览器中访问的会有差别，可以补充一些请求头(如user-agent)来看看输出的变化。

## 6、JSON 转 Dart Model 类

### ①、简介

1. 在实战中，后台接口往往会返回一些结构化数据，如 JSON、XML 等，如之前我们请求 Github API 的示例，它返回的数据就是 JSON 格式的字符串，为了方便我们在代码中操作 JSON，我们先将 JSON 格式的字符串转为 Dart 对象，这个可以通过 `dart:convert` 中内置的 JSON 解码器 `json.decode()` 来实现，该方法可以根据 JSON 字符串具体内容将其转为 List 或 Map，这样我们就可以通过他们来查找所需的值，如：

```dart
//一个 JSON 格式的用户列表字符串
String jsonStr = '[{"name":"Jack"},{"name":"Rose"}]';
// 将 JSON 字符串转为 Dart 对象(此处是 List)
List items = json.decode(jsonStr);
// 输出第一个用户的姓名
print(items[0]["name"]);
```

2. 通过 `json.decode()` 将 JSON 字符串转为 `List/Map` 的方法比较简单，它没有外部依赖或其他的设置，对于小项目很方便。但当项目变大时，这种手动编写序列化逻辑可能变得难以管理且容易出错，例如有如下JSON：

```json
{
  "name": "John Smith",
  "email": "john@example.com"
}
```

3. 我们可以通过调用 `json.decode` 方法来解码 JSON ，使用 JSON 字符串作为参数:

```dart
Map<String, dynamic> user = json.decode(json);

print('Howdy, ${user['name']}!');
print('We sent the verification link to ${user['email']}.');
```

4. 由于 `json.decode()` 仅返回一个 `Map<String, dynamic>`，这意味着直到运行时我们才知道值的类型。 通过这种方法，我们失去了大部分静态类型语言特性：类型安全、自动补全和最重要的编译时异常。这样一来，我们的代码可能会变得非常容易出错。例如，当我们访问 `name` 或 `email` 字段时，我们输入的很快，导致字段名打错了。但由于这个 JSON 在 map 结构中，所以编译器不知道这个错误的字段名，所以编译时不会报错。
5. 其实，这个问题在很多平台上都会遇到，而也早就有了好的解决方法即 “Json Model 化”，具体做法就是，通过预定义一些与 Json 结构对应的 `Model` 类，然后在请求到数据后再动态根据数据创建出 Model 类的实例。这样一来，在开发阶段我们使用的是 Model 类的实例，而不再是 Map/List，这样访问内部属性时就不会发生拼写错误。
6. 例如，我们可以通过引入一个简单的模型类（Model class）来解决前面提到的问题，我们称之为 User。在 User 类内部，我们有：
	1. 一个 `User.fromJson` 构造函数, 用于从一个 map 构造出一个 User 实例 map 结构。
	2. 一个 `toJson` 方法，将 User 实例转化为一个 map。
7. 这样，调用代码现在可以具有类型安全、自动补全字段（name和email）以及编译时异常。如果我们将拼写错误字段视为 int 类型而不是 String， 那么我们的代码就不会通过编译，而不是在运行时崩溃。

```dart
user.dart

class User {
  final String name;
  final String email;

  User(this.name, this.email);

  User.fromJson(Map<String, dynamic> json)
      : name = json['name'],
        email = json['email'];

  Map<String, dynamic> toJson() =>
    <String, dynamic>{
      'name': name,
      'email': email,
    };
}
```

8. 现在，序列化逻辑移到了模型本身内部。采用这种新方法，我们可以非常容易地反序列化 `user`.

```dart
Map userMap = json.decode(json);
var user = User.fromJson(userMap);

print('Howdy, ${user.name}!');
print('We sent the verification link to ${user.email}.');
```

9. 要序列化一个 user，我们只是将该 User 对象传递给该 `json.encode` 方法。我们不需要手动调用 `toJson` 这个方法，因为 `JSON.encode` 内部会自动调用。

```dart
String json = json.encode(user);
```

10. 这样，调用代码就不用担心 JSON 序列化了，但是，Model 类还是必须的。在实践中，`User.fromJson` 和`User.toJson` 方法都需要单元测试到位，以验证正确的行为。
11. 另外，实际场景中，JSON 对象很少会这么简单，嵌套的 JSON 对象并不罕见，如果有什么能为我们自动处理JSON序列化，那将会非常好。幸运的是，有！

### ②、自动生成 Model

1. 在这里介绍一下官方推荐的 [json_serializable package](https://pub.dartlang.org/packages/json_serializable) 包。 
2. 它是一个自动化的源代码生成器，可以在开发阶段为我们生成 JSON 序列化模板，这样一来，由于序列化代码不再由我们手写和维护，我们将运行时产生 JSON 序列化异常的风险降至最低

#### Ⅰ、在项目中设置 json_serializable

1. 要包含 `json_serializable` 到我们的项目中，我们需要一个常规和两个开发依赖项。
2. 简而言之，开发依赖项是不包含在我们的应用程序源代码中的依赖项，它是开发过程中的一些辅助工具、脚本，和 node 中的开发依赖项相似。
3. `pubspec.yaml` 中引入：

```dart
dependencies:

  # json_serializable 是一个 Dart 包，它提供了一组工具，用于将 Dart 对象序列化为 JSON 和反序列化为 JSON
  json_annotation: ^4.0.1

dev_dependencies:

  # build_runner 是一个 Dart 包，它提供了一组工具，用于生成源代码，以帮助您减少样板代码
  build_runner: ^2.1.5
  # json_serializable 是一个 Dart 包，它提供了一组工具，用于将 Dart 对象序列化为 JSON 和反序列化为 JSON
  json_serializable: ^4.1.4
```

4. 在项目根文件夹中运行 `flutter packages get` (或者在编辑器中点击 “Packages Get”) 以在项目中使用这些新的依赖项

#### Ⅱ、以 json_serializable 的方式创建 model 类

1. 让我们看看如何将我们的 User 类转换为一个 `json_serializable`。为了简单起见，我们使用前面示例中的简化 JSON model。
2. `User.dart`  JSON model 类；第一次创建类时，会看一些错误。这些错误是完全正常的，这是因为 Model 类的生成代码还不存在

```dart
import 'package:json_annotation/json_annotation.dart';

// user.g.dart 将在我们运行生成命令后自动生成
part 'user.g.dart';

///这个标注是告诉生成器，这个类是需要生成 Model 类的
@JsonSerializable()
class User{
  User(this.name, this.email);

  String name;
  String email;
  // 不同的类使用不同的 mixin 即可
  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
```

3. 有了上面的设置，源码生成器将生成用于序列化 `name` 和 `email` 字段的 JSON 代码。
4. 如果需要，自定义命名策略也很容易，我们可以使用 `@JsonKey` 显式关联 JSON 字段名与 Model 属性的对应关系 ：

```dart
// 显式关联 JSON 字段名与 Model 属性的对应关系 
@JsonKey(name: 'registration_date_millis')
final int registrationDateMillis;
```

#### Ⅲ、运行代码生成程序

- 有两种运行代码生成器的方法：
- 下面的两条命令我运行之后都报错了

#####（1）、一次性生成

1. 通过在我们的项目根目录下运行:

```cmd
flutter packages pub run build_runner build
```

2. 这触发了一次性构建，我们可以在需要时为我们的 Model 生成 json 序列化代码，它通过我们的源文件，找出需要生成 Model 类的源文件（包含`@JsonSerializable` 标注的）来生成对应的 `.g.dart` 文件。
3. 一个好的建议是将所有 Model 类放在一个单独的目录下，然后在该目录下执行命令。
4. 虽然这非常方便，但如果我们不需要每次在 Model 类中进行更改时都要手动运行构建命令的话会更好

#####（2）、持续生成

1. 使用 `_watcher_`可以使我们的源代码生成的过程更加方便。
2. 它会监视我们项目中文件的变化，并在需要时自动构建必要的文件，我们可以通过下面的命令在项目根目录下运行来启动 `_watcher_`。

```cmd
flutter packages pub run build_runner watch
```

3. 只需启动一次观察器，然后它就会在后台运行，这是安全的

### ③、使用 IDE 插件生成 model

1. 目前 Android Studio(或IntelliJ) 有几个插件，可以将 json 文件转成 Model 类，但插件质量参差不齐，甚至还有一些沾染上了抄袭风波，故在此不做优先推荐，有兴趣可以自行了解
2. 但是，我们还是要了解一下 IDE 插件和 Json_model 的优劣：
	1. Json_model 需要单独维护一个存放 Json 文件的文件夹，如果有改动，只需修改 Json 文件便可重新生成 Model 类；而 IDE 插件一般需要用户手动将 Json 内容拷贝复制到一个输入框中，这样生成之后 Json 文件没有存档的地方，之后要改动就需要手动。
	2. Json_model 可以手动指定某个字段引用的其他 Model 类，可以避免生成重复的类；而 IDE 插件一般会为每一个 Json 文件中所有嵌套对象都单独生成一个 Model 类，即使这些嵌套对象可能在其他 Model 类中已经生成过。
	3. Json_model 提供了命令行转化方式，可以方便集成到 CI 等非 UI 环境的场景

## 7、Json 序列化类库

1. Flutter 中并没有像 Java 开发中的 Gson/Jackson 一样的 Json 序列化类库
2. 因为这样的库需要使用运行时反射，这在 Flutter 中是禁用的。
3. 运行时反射会干扰 Dart 的 tree shaking，使用 `_tree shaking_`，可以在 release 版中“去除”未使用的代码，这可以显著优化应用程序的大小。
4. 由于反射会默认应用到所有代码，因此 `_tree shaking_` 会很难工作，因为在启用反射时很难知道哪些代码未被使用，因此冗余代码很难剥离，所以 Flutter 中禁用了 Dart 的反射功能，而正因如此也就无法实现动态转化 Model 的功能。

## 8、FlutterJsonBeanFactory 插件

> 我使用上面的 `json_serializable` 创建失败，据说是 flutter SDK 版本和依赖版本的问题，研究了一下不想弄了
> 
> 我搜到的解决办法，flutter SDK 版本 >= 2.12.0 < 3.0.0 才可：https://blog.csdn.net/Bearin/article/details/122085249

1. idea 安装 FlutterJsonBeanFactory 插件

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215092814.png)

2. 获得一个 json：http://101.200.86.248:9001/hello/helloTest

```json
{
    "msg": "ok",
    "data": "Hello World!",
    "code": 200
}
```

3. 当然可以选择把这个 json 存起来，保证以后能找到

![|382](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215093430.png)

4. 在想要生成的目录上右键 -> 新建 -> JsonToDartBeanAction

![|530](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215095553.png)

5. 在弹出的窗口中输入想要生成的类名和 `json` 字符串；左下角有个 `null-able` ，如果勾选，表示我们创建的类的属性都是可空的；如果没有勾选，则生成的是不可空的

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215095654.png)

6. 点击 Make ，开始将我们输入的 Json 转换为类
	1. 生成的类名，会将我们的输入的类名，再加上 Entity 后缀；
	2. 会生成一个 `generated` 目录，里面包含了最终产物和中间产物；
	3. 插件也是用了 `json_serializable` 这样的库或原理；

![|543](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215095945.png)

7. 生成的文件中：
	1. `json_convert_content.dart` 和 `json_field.dart` 是用于 JSON 序列化和反序列化的基础类
	2. `hello_world_entity.g.dart` 是根据提供的 JSON 数据生成的模型类的序列化和反序列化逻辑
	3. 使用时使用 `hello_world_entity.dart` 类即可，`hello_world_entity.dart` 类内容：

```dart
import 'package:flutter_study/generated/json/base/json_field.dart';
import 'package:flutter_study/generated/json/hello_world_entity.g.dart';
import 'dart:convert';
export 'package:flutter_study/generated/json/hello_world_entity.g.dart';

@JsonSerializable()
class HelloWorldEntity {
	late String msg;
	late String data;
	late int code;

	HelloWorldEntity();

	factory HelloWorldEntity.fromJson(Map<String, dynamic> json) => $HelloWorldEntityFromJson(json);

	Map<String, dynamic> toJson() => $HelloWorldEntityToJson(this);

	@override
	String toString() {
		return jsonEncode(this);
	}
}
```

8. 访问接口，对返回值进行测试：
	- 主要是这一行代码：`var helloWorldEntity = HelloWorldEntity.fromJson(response.data);`

```dart
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

import 'model/hello_world_entity.dart';


class HttpDioJsonComponent extends StatefulWidget {
  const HttpDioJsonComponent({Key? key}) : super(key: key);

  @override
  _HttpDioJsonComponentState createState() => _HttpDioJsonComponentState();
}

class _HttpDioJsonComponentState extends State<HttpDioJsonComponent> {
  Dio _dio = Dio();

  bool _loading = false;
  String _text = "";

  /// 构建 UI, context：构建上下文，即当前 Widget 的位置
  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      // Column 是一个小部件，用于在垂直方向上排列其子部件
      child: Column(
        children: [
          ElevatedButton(
            onPressed: _loading ? null : request,
            child: const Text("请求 月海"),
          ),
          SizedBox(
            width: MediaQuery.of(context).size.width - 50.0,
            child: Text(_text),
          )
        ],
      ),
    );
  }

  request() async {
    setState(() {
      _loading = true;
      _text = "正在请求...";
    });

    try {
      Response response = await _dio.get("http://101.200.86.248:9001/hello/helloTest");
      setState(() {
        // 使用 json 类解析 json
        var helloWorldEntity = HelloWorldEntity.fromJson(response.data);
        _text = "是否成功：${helloWorldEntity.msg}\n"
            "状态码：${helloWorldEntity.code}\n"
            "返回值：${helloWorldEntity.data}";
      });

    } catch (e) {
      _text = "请求失败：$e";
    } finally {
      setState(() {
        _loading = false;
      });
    }
  }

}
```

9. 效果：

![|356](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画1%201.gif)

## <span id="9-9">9、使用 `shared_preferences` 包数据持久化</span>

1. `pubspec.yaml` 导入依赖

```yaml
dependencies:
  flutter:
    sdk: flutter
  
  # shared_preferences 是一个用于存储轻量级键值对的插件，它包装了 Android 的 SharedPreferences 和 iOS 的 UserDefaults。
  shared_preferences: ^2.0.8
```

2. 导入头文件

```dart
import 'package:shared_preferences/shared_preferences.dart';
```


3. 获取实例对象

```dart
SharedPreferences? sharedPreferences = await SharedPreferences.getInstance();
```

4. 设置持久化数据，我们可以通过 `sharedPreferences` 的实例化对象调用对应的 `set` 方法设置持久化数据

```dart
SharedPreferences? sharedPreferences;

// 设置持久化数据
void _setData() async {
  // 实例化
  sharedPreferences = await SharedPreferences.getInstance();

  // 设置string类型
  await sharedPreferences?.setString("name", "Jimi");

  // 设置int类型
  await sharedPreferences?.setInt("age", 18);

  // 设置bool类型
  await sharedPreferences?.setBool("isTeacher", true);

  // 设置double类型
  await sharedPreferences?.setDouble("height", 1.88);

  // 设置string类型的数组
  await sharedPreferences?.setStringList("action", ["吃饭", "睡觉", "打豆豆"]);

  setState(() {});
}
```

5. 读取持久化数据，我们可以通过 `sharedPreferences` 的实例化对象调用对应的 `get` 方法读取持久化数据

```dart
Text("名字: ${sharedPreferences?.getString("name") ?? ""}",
     style: TextStyle(
       color: Colors.blue,
       fontSize: 20
     ),
    ),
SizedBox(height: 20,),
Text("年龄: ${sharedPreferences?.getInt("age") ?? ""}",
     style: TextStyle(
       color: Colors.red,
       fontSize: 20
     ),
    ),
SizedBox(height: 20,),
Text("是老师吗?: ${sharedPreferences?.getBool("isTeacher") ?? ""}",
     style: TextStyle(
       color: Colors.orange,
       fontSize: 20
     ),
    ),
SizedBox(height: 20,),
Text("身高: ${sharedPreferences?.getDouble("height") ?? ""}",
     style: TextStyle(
       color: Colors.pink,
       fontSize: 20
     ),
    ),
SizedBox(height: 20,),
Text("我正在: ${sharedPreferences?.getStringList("action") ?? ""}",
     style: TextStyle(
       color: Colors.purple,
       fontSize: 20
     ),
    ),
```


6. 完整代码

```dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SharedPreferencesExample extends StatefulWidget {
  @override
  _SharedPreferencesExampleState createState() => _SharedPreferencesExampleState();
}

class _SharedPreferencesExampleState extends State<SharedPreferencesExample> {


  SharedPreferences? sharedPreferences;

  // 设置持久化数据
  void _setData() async {
    // 实例化
    sharedPreferences = await SharedPreferences.getInstance();

    // 设置string类型
    await sharedPreferences?.setString("name", "Jimi");

    // 设置int类型
    await sharedPreferences?.setInt("age", 18);

    // 设置bool类型
    await sharedPreferences?.setBool("isTeacher", true);

    // 设置double类型
    await sharedPreferences?.setDouble("height", 1.88);

    // 设置string类型的数组
    await sharedPreferences?.setStringList("action", ["吃饭", "睡觉", "打豆豆"]);

    setState(() {});
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("SharedPreferences"),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _setData,
        child: Icon(Icons.add),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text("名字: ${sharedPreferences?.getString("name") ?? ""}",
                 style: TextStyle(
                   color: Colors.blue,
                   fontSize: 20
                 ),
                ),
            SizedBox(height: 20,),
            Text("年龄: ${sharedPreferences?.getInt("age") ?? ""}",
                 style: TextStyle(
                   color: Colors.red,
                   fontSize: 20
                 ),
                ),
            SizedBox(height: 20,),
            Text("是老师吗?: ${sharedPreferences?.getBool("isTeacher") ?? ""}",
                 style: TextStyle(
                   color: Colors.orange,
                   fontSize: 20
                 ),
                ),
            SizedBox(height: 20,),
            Text("身高: ${sharedPreferences?.getDouble("height") ?? ""}",
                 style: TextStyle(
                   color: Colors.pink,
                   fontSize: 20
                 ),
                ),
            SizedBox(height: 20,),
            Text("我正在: ${sharedPreferences?.getStringList("action") ?? ""}",
                 style: TextStyle(
                   color: Colors.purple,
                   fontSize: 20
                 ),
                ),
          ],
        ),
      ),
    );
  }
}
```

7. 效果展示

![|555](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231215104352.png)

8. 获取持久化数据中所有存入的 key

```dart
dart复制代码List<String> keys = sharedPreferences?.getKeys().toList() ?? [];
print(keys);

// 控制台输出
[name, age, isTeacher, height, action]
```

9. 判断持久化数据中是否包含某个 key

```dart
dart复制代码bool isContainKey = sharedPreferences?.containsKey("name") ?? false;
print(isContainKey);

// 控制台输出
flutter: true
```

10. 删除持久化数据中某个 key

```dart
dart复制代码bool isRemoveKey = await sharedPreferences?.remove("name") ?? false;
print(isRemoveKey);

// 控制台输出
flutter: true
```


11. 清除所有持久化数据

```dart
dart复制代码bool isClearAllKey = await sharedPreferences?.clear() ?? false;
print(isClearAllKey);

// 控制台输出
flutter: true
```

12. 重新加载所有数据（仅重载运行时）

```dart
dart复制代码await sharedPreferences?.reload();
```

# 十、动画

## 1、Flutter 动画简介

### ①、动画基本原理

1. 在任何系统的 UI 框架中，动画实现的原理都是相同的，即：在一段时间内，快速地多次改变UI外观；由于人眼会产生视觉暂留，所以最终看到的就是一个“连续”的动画，这和电影的原理是一样的。
2. 我们将 UI 的一次改变称为一个动画帧，对应一次屏幕刷新，而决定动画流畅度的一个重要指标就是帧率 FPS（Frame Per Second），即每秒的动画帧数。
3. 很明显，帧率越高则动画就会越流畅！一般情况下，对于人眼来说，动画帧率超过 16 FPS，就基本能看了，超过 32 FPS 就会感觉相对平滑，而超过 32 FPS，大多数人基本上就感受不到差别了。
4. 由于动画的每一帧都是要改变 UI 输出，所以在一个时间段内连续的改变 UI 输出是比较耗资源的，对设备的软硬件系统要求都较高，所以在UI系统中，动画的平均帧率是重要的性能指标，而在 Flutter 中，理想情况下是可以实现 60FPS 的，这和原生应用能达到的帧率是基本是持平的

### ②、Flutter 中动画抽象

1. 为了方便开发者创建动画，不同的 UI 系统对动画都进行了一些抽象，比如在 Android 中可以通过 XML 来描述一个动画然后设置给 View。
2. Flutter 中也对动画进行了抽象，主要涉及 `Animation`、`Curve`、`AnimationController`、`Tween` 这四个角色，它们一起配合来完成一个完整动画

#### Ⅰ、Animation

1. Animation 是一个抽象类，它本身和 UI 渲染没有任何关系，而它主要的功能是保存动画的插值和状态；其中一个比较常用的 `Animation` 类是`Animation<double>`。
2. `Animation` 对象是一个在一段时间内依次生成一个区间(Tween)之间值的类。`Animation` 对象在整个动画执行过程中输出的值可以是线性的、曲线的、一个步进函数或者任何其他曲线函数等等，这由 `Curve` 来决定。 
3. 根据 `Animation` 对象的控制方式，动画可以正向运行（从起始状态开始，到终止状态结束），也可以反向运行，甚至可以在中间切换方向。
4. `Animation` 还可以生成除 `double` 之外的其他类型值，如：`Animation<Color>` 或 `Animation<Size>`。
5. 在动画的每一帧中，我们可以通过 `Animation` 对象的 `value` 属性获取动画的当前状态值。
6. 我们可以通过 `Animation` 来监听动画每一帧以及执行状态的变化，`Animation` 有如下两个方法：
	1. `addListener()`：它可以用于给 `Animation` 添加帧监听器，在每一帧都会被调用。帧监听器中最常见的行为是改变状态后调用 `setState()` 来触发 UI 重建。
	2. `addStatusListener()`：它可以给 Animation 添加“动画状态改变”监听器；动画开始、结束、正向或反向（见AnimationStatus定义）时会调用状态改变的监听器。

#### Ⅱ、Curve

1. 动画过程可以是匀速的、匀加速的或者先加速后减速等。
2. Flutter 中通过 Curve（曲线）来描述动画过程，我们把匀速动画称为线性的(Curves.linear)，而非匀速动画称为非线性的。
3. 我们可以通过 `CurvedAnimation` 来指定动画的曲线，如：

```dart
final CurvedAnimation curve =
    CurvedAnimation(parent: controller, curve: Curves.easeIn);
```

4. `CurvedAnimation` 和 `AnimationController`（下面介绍）都是 `Animation<double>` 类型。
5. `CurvedAnimation` 可以通过包装 `AnimationController` 和 `Curve` 生成一个新的动画对象 ，我们正是通过这种方式来将动画和动画执行的曲线关联起来的。我们指定动画的曲线为 `Curves.easeIn`，它表示动画开始时比较慢，结束时比较快。 `Curves (opens new window)` 类是一个预置的枚举类，定义了许多常用的曲线，下面列几种常用的：

| Curves 曲线 | 动画过程                     |
| ----------- | ---------------------------- |
| linear      | 匀速的                       |
| decelerate  | 匀减速                       |
| ease        | 开始加速，后面减速           |
| easeIn      | 开始慢，后面快               |
| easeOut     | 开始快，后面慢               |
| easeInOut   | 开始慢，然后加速，最后再减速 |

6. 除了上面列举的， `Curves (opens new window)` 类中还定义了许多其他的曲线。
7. 当然我们也可以创建自己 `Curve`，例如我们定义一个正弦曲线：

```dart
class ShakeCurve extends Curve {
  @override
  double transform(double t) {
    return math.sin(t * math.PI * 2);
  }
}
```

#### Ⅲ、AnimationController

1. `AnimationController` 用于控制动画，它包含动画的启动 `forward()`、停止 `stop()` 、反向播放 `reverse()` 等方法。
2. `AnimationController` 会在动画的每一帧，就会生成一个新的值。默认情况下，`AnimationController` 在给定的时间段内线性的生成从 `0.0` 到 `1.0`（默认区间）的数字。 例如，下面代码创建一个 `Animation` 对象（但不会启动动画）：

```dart
final AnimationController controller = AnimationController(
  duration: const Duration(milliseconds: 2000),
  vsync: this,
);
```

3. `AnimationController` 生成数字的区间可以通过 `lowerBound` 和 `upperBound` 来指定，如：

```dart
final AnimationController controller = AnimationController( 
 duration: const Duration(milliseconds: 2000), 
 lowerBound: 10.0,
 upperBound: 20.0,
 vsync: this
);
```

2. `AnimationController` 派生自 `Animation<double>`，因此可以在需要 `Animation` 对象的任何地方使用。 
3. 但是，`AnimationController` 具有控制动画的其他方法，例如 `forward()` 方法可以启动正向动画，`reverse()` 可以启动反向动画。
4. 在动画开始执行后开始生成动画帧，屏幕每刷新一次就是一个动画帧，在动画的每一帧，会随着根据动画的曲线来生成当前的动画值（Animation.value），然后根据当前的动画值去构建 UI， 当所有动画帧依次触发时，动画值会依次改变，所以构建的 UI 也会依次变化，所以最终我们可以看到一个完成的动画。 另外在动画的每一帧，`Animation` 对象会调用其帧监听器，等动画状态发生改变时（如动画结束）会调用状态改变监听器。
5. `duration` 表示动画执行的时长，通过它我们可以控制动画的速度。
	1. 注意： 在某些情况下，动画值可能会超出 `AnimationController` 的 `[0.0，1.0]` 的范围，这取决于具体的曲线。
	2. 例如，`fling()` 函数可以根据我们手指滑动（甩出）的速度(velocity)、力量(force)等来模拟一个手指甩出动画，因此它的动画值可以在 `[0.0，1.0]` 范围之外 。
	3. 也就是说，根据选择的曲线，`CurvedAnimation` 的输出可以具有比输入更大的范围。例如，`Curves.elasticIn` 等弹性曲线会生成大于或小于默认范围的值。
6. 当创建一个 `AnimationController` 时，需要传递一个 `vsync` 参数，它接收一个 `TickerProvider` 类型的对象，它的主要职责是创建 `Ticker`，定义如下：

```dart
abstract class TickerProvider {
  //通过一个回调创建一个Ticker
  Ticker createTicker(TickerCallback onTick);
}
```

7. Flutter 应用在启动时都会绑定一个 `SchedulerBinding`，通过 `SchedulerBinding` 可以给每一次屏幕刷新添加回调，而 `Ticker` 就是通过 `SchedulerBinding` 来添加屏幕刷新回调，这样一来，每次屏幕刷新都会调用 `TickerCallback`。
8. 使用 `Ticker`(而不是Timer) 来驱动动画会防止屏幕外动画（动画的 UI 不在当前屏幕时，如锁屏时）消耗不必要的资源，因为 Flutter 中屏幕刷新时会通知到绑定的 `SchedulerBinding`，而 `Ticker` 是受 `SchedulerBinding` 驱动的，由于锁屏后屏幕会停止刷新，所以 `Ticker` 就不会再触发。
9. 通常我们会将 `SingleTickerProviderStateMixin` 添加到 `State` 的定义中，然后将 `State` 对象作为 `vsync` 的值，这在后面的例子中可以见到。
10. 1

#### Ⅳ、Tween

##### （1）、简介

1. 默认情况下，`AnimationController` 对象值的范围是 `[0.0，1.0]`。如果我们需要构建 UI 的动画值在不同的范围或不同的数据类型，则可以使用 `Tween` 来添加映射以生成不同的范围或数据类型的值。例如，像下面示例，`Tween` 生成 `[-200.0，0.0]` 的值：

```dart
final Tween doubleTween = Tween<double>(begin: -200.0, end: 0.0);
```

2. `Tween` 构造函数需要 `begin` 和 `end` 两个参数。`Tween` 的唯一职责就是定义从输入范围到输出范围的映射。输入范围通常为 `[0.0，1.0]`，但这不是必须的，我们可以自定义需要的范围。
3. `Tween` 继承自 `Animatable<T>`，而不是继承自 `Animation<T>`，`Animatable` 中主要定义动画值的映射规则。
4. 下面我们看一个 `ColorTween` 将动画输入范围映射为两种颜色值之间过渡输出的例子：

```dart
final Tween colorTween =
    ColorTween(begin: Colors.transparent, end: Colors.black54);
```

5. `Tween` 对象不存储任何状态，相反，它提供了 `evaluate(Animation<double> animation)` 方法，它可以获取动画当前映射值。 `Animation` 对象的当前值可以通过 `value()` 方法取到。`evaluate` 函数还执行一些其他处理，例如分别确保在动画值为 `0.0` 和 `1.0` 时返回开始和结束状态

##### （2）、Tween.animate

1. 要使用 `Tween` 对象，需要调用其 `animate()` 方法，然后传入一个控制器对象。例如，以下代码在 500 毫秒内生成从 0 到 255 的整数值。

```dart
final AnimationController controller = AnimationController(
  duration: const Duration(milliseconds: 500), 
  vsync: this,
);
Animation<int> alpha = IntTween(begin: 0, end: 255).animate(controller);
```

2. 注意 `animate()` 返回的是一个 `Animation`，而不是一个 `Animatable`。
3. 以下示例构建了一个控制器、一条曲线和一个 Tween：

```dart
final AnimationController controller = AnimationController(
  duration: const Duration(milliseconds: 500), 
  vsync: this,
);
final Animation curve = CurvedAnimation(parent: controller, curve: Curves.easeOut);
Animation<int> alpha = IntTween(begin: 0, end: 255).animate(curve);

```

### ③、线性插值 lerp 函数

1. 动画的原理其实就是每一帧绘制不同的内容，一般都是指定起始和结束状态，然后在一段时间内从起始状态逐渐变为结束状态，而具体某一帧的状态值会根据动画的进度来算出，因此，Flutter 中给有可能会做动画的一些状态属性都定义了静态的 `lerp` 方法（线性插值），比如：

```dart
//a 为起始颜色，b为终止颜色，t为当前动画的进度[0,1]
Color.lerp(a, b, t);
```

2. `lerp` 的计算一般遵循： `返回值 = a + (b - a) * t`，其他拥有 `lerp` 方法的类：

```dart
// Size.lerp(a, b, t)
// Rect.lerp(a, b, t)
// Offset.lerp(a, b, t)
// Decoration.lerp(a, b, t)
// Tween.lerp(t) //起始状态和终止状态在构建 Tween 的时候已经指定了
...
```

3. 需要注意，`lerp` 是线性插值，意思是返回值和动画进度 t 是成一次函数（`y = kx + b`）关系，因为一次函数的图像是一条直线，所以叫线性插值。
4. 如果我们想让动画按照一个曲线来执行，我们可以对 t 进行映射，比如要实现匀加速效果，则 `t' = at²+bt+c`，然后指定加速度 a 和 b 即可（大多数情况下需保证 `t'` 的取值范围在 `[0,1]`，当然也有一些情况可能会超出该取值范围，比如弹簧（bounce）效果），而不同 Curve 可以按照不同曲线执行动画的原理本质上就是对 t 按照不同映射公式进行映射实现的。

## 2、动画基本结构及状态监听

### ①、动画基本结构

#### Ⅰ、基础版本

##### （1）、匀速放大

1. 在 Flutter 中我们可以通过多种方式来实现动画
2. 下面通过一个图片逐渐放大示例的不同实现来演示 Flutter 中动画的不同实现方式的区别

```dart
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';


class ScaleAnimationComponent extends StatefulWidget {
  const ScaleAnimationComponent({Key? key}) : super(key: key);

  @override
  _ScaleAnimationComponentState createState() => _ScaleAnimationComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _ScaleAnimationComponentState extends State<ScaleAnimationComponent> with SingleTickerProviderStateMixin {
  // 动画对象
  late Animation<double> animation;
  // 动画控制器
  late AnimationController controller;

  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );

    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller)
      ..addListener(() {
        setState(() => {});
      });

    // 启动动画(正向执行)
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Image.asset(
        "asset/images/QQ图片20220920105928.jpg",
        width: animation.value,
        height: animation.value,
      ),
    );
  }

  @override
  dispose() {
    // 路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  }
}
```

3. 效果：

![|386](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画35.gif)

4. 上面代码中 `addListener()` 函数调用了 `setState()`，所以每次动画生成一个新的数字时，当前帧被标记为脏(dirty)，这会导致 widget 的 `build()` 方法再次被调用
5. 而在 `build()` 中，改变 Image 的宽高，因为它的高度和宽度现在使用的是 `animation.value`，所以就会逐渐放大。
6. 值得注意的是动画完成时要释放控制器，调用 `dispose()` 方法，以防止内存泄漏。

##### （2）、先快后慢

1. 上面的例子中并没有指定 `Curve`，所以放大的过程是线性的（匀速），下面我们指定一个 `Curve`，来实现一个类似于弹簧效果的动画过程，我们只需要将 `initState` 中的代码改为下面这样即可：

```dart
  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );

    // CurvedAnimation 可以更改动画的执行速率，使动画感觉更加流畅；这里使用的是 Curves.easeIn 缓动曲线（先快后慢）
    animation = CurvedAnimation(parent: controller, curve: Curves.easeIn);
    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller)
      ..addListener(() {
        setState(() => {});
      });

    // 启动动画(正向执行)
    controller.forward();
  }
```

2. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画36.gif)

#### Ⅱ、使用 AnimatedWidget 简化

1. 上面示例中通过 `addListener()` 和 `setState()` 来更新 UI 这一步其实是通用的，如果每个动画中都加这么一句是比较繁琐的。
2. `AnimatedWidget` 类封装了调用 `setState()` 的细节，并允许我们将 widget 分离出来，重构后的代码如下：
3. 抽取出来的 `02_1_AnimatedWidget.dart`

```dart
import 'package:flutter/cupertino.dart';

class AnimatedImage extends AnimatedWidget {
  // AnimatedWidget 的构造函数，需要传入一个 Animation 对象
  const AnimatedImage({Key? key, required Animation<double> animation,})
      : super(key: key, listenable: animation);

  @override
  Widget build(BuildContext context) {
    // listenable as Animation<double> 用于获取动画对象
    final animation = listenable as Animation<double>;
    // Center 用于将其子部件树对齐到屏幕中心
    return Center(
      // Image.asset 用于加载本地图片
      child: Image.asset(
        "asset/images/QQ图片20220920105928.jpg",
        width: animation.value,
        height: animation.value,
      ),
    );
  }
}
```

4. `02_2_AnimatedWidgetComponent.dart` 动画实现类

```dart
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

import '02_1_AnimatedWidget.dart';


class AnimatedWidgetComponent extends StatefulWidget {
  const AnimatedWidgetComponent({Key? key}) : super(key: key);

  @override
  _AnimatedWidgetComponentState createState() => _AnimatedWidgetComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _AnimatedWidgetComponentState extends State<AnimatedWidgetComponent> with SingleTickerProviderStateMixin {
  // 动画对象
  late Animation<double> animation;
  // 动画控制器
  late AnimationController controller;

  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );

    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller);

    // 启动动画(正向执行)
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    // 实例化 AnimatedImage，将动画对象传递给它
    return AnimatedImage(animation: animation);
  }

  @override
  dispose() {
    // 路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  }
}
```

#### Ⅲ、使用 AnimatedBuilder 重构

1. 用 `AnimatedWidget` 可以从动画中分离出 widget，而动画的渲染过程（即设置宽高）仍然在 `AnimatedWidget` 中，假设如果我们再添加一个 widget 透明度变化的动画，那么我们需要再实现一个 `AnimatedWidget`，这样不是很优雅，如果我们能把渲染过程也抽象出来，那就会好很多，而 `AnimatedBuilder` 正是将渲染逻辑分离出来, 上面的代码可以改为：

```dart
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

import '02_1_AnimatedWidget.dart';


class AnimatedBuilderComponent extends StatefulWidget {
  const AnimatedBuilderComponent({Key? key}) : super(key: key);

  @override
  _AnimatedBuilderComponentState createState() => _AnimatedBuilderComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _AnimatedBuilderComponentState extends State<AnimatedBuilderComponent> with SingleTickerProviderStateMixin {
  // 动画对象
  late Animation<double> animation;
  // 动画控制器
  late AnimationController controller;

  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(duration: const Duration(seconds: 2), vsync: this,);

    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller);

    // 启动动画(正向执行)
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    // AnimatedBuilder 是一个小部件，用于构建动画小部件，它可以封装常见的动画构建过程，省去了每次都要重新实现动画的麻烦。
    return AnimatedBuilder(
      // 动画对象
      animation: animation,
      // 子部件
      child: Image.asset("asset/images/QQ图片20220920105928.jpg"),
      // 构建动画
      builder: (BuildContext context, child){
        // Center 是一个小部件，用于将其子部件居中显示。
        return Center(
          // SizedBox 是一个小部件，用于给子部件指定固定的宽度和高度。
          child: SizedBox(
            width: animation.value,
            height: animation.value,
            // 将子部件居中显示，这里的子部件就是 AnimatedBuilder 的 child 属性。
            child: child,
          ),
        );
      }
    );
  }

  @override
  dispose() {
    // 路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  }
}
```

2. 看着也许和刚开始的示例差不了多少，其实它会带来三个好处：
	1. 不用显式的去添加帧监听器，然后再调用 `setState()` 了，这个好处和 `AnimatedWidget` 是一样的。
	2. 更好的性能：因为动画每一帧需要构建的 widget 的范围缩小了，如果没有 builder，`setState()` 将会在父组件上下文中调用，这将会导致父组件的 build 方法重新调用；而有了 builder 之后，只会导致动画 widget 自身的 build 重新调用，避免不必要的 rebuild。
	3. 通过 `AnimatedBuilder` 可以封装常见的过渡效果来复用动画。

#### Ⅳ、封装过渡效果来复用动画

1. 封装一个 `04_GrowTransition.dart` 来说明，它可以对子 widget 实现放大动画：

```dart
import 'package:flutter/cupertino.dart';

class GrowTransition extends StatelessWidget {
  const GrowTransition({Key? key, required this.animation, this.child,}) : super(key: key);

  // 子部件
  final Widget? child;
  // 动画对象
  final Animation<double> animation;

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，用于将其子部件居中显示。
    return Center(
      // AnimatedBuilder 是一个小部件，用于构建动画小部件，它可以封装常见的动画构建过程，省去了每次都要重新实现动画的麻烦。
      child: AnimatedBuilder(
        // 动画对象
        animation: animation,
        builder: (BuildContext context, child) {
          return SizedBox(
            height: animation.value,
            width: animation.value,
            child: child,
          );
        },
        child: child,
      ),
    );
  }

}
```

2. 这样，最初的示例就可以改为：

```dart
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

import '02_1_AnimatedWidget.dart';
import '04_GrowTransition.dart';


class GrowTransitionComponent extends StatefulWidget {
  const GrowTransitionComponent({Key? key}) : super(key: key);

  @override
  _GrowTransitionComponentState createState() => _GrowTransitionComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _GrowTransitionComponentState extends State<GrowTransitionComponent> with SingleTickerProviderStateMixin {
  // 动画对象
  late Animation<double> animation;
  // 动画控制器
  late AnimationController controller;

  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(duration: const Duration(seconds: 2), vsync: this,);

    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller);

    // 启动动画(正向执行)
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    // AnimatedBuilder 是一个小部件，用于构建动画小部件，它可以封装常见的动画构建过程，省去了每次都要重新实现动画的麻烦。
    return GrowTransition(
      // 动画对象
      animation: animation,
      // 子部件
      child: Image.asset("asset/images/QQ图片20220920105928.jpg")
    );
  }

  @override
  dispose() {
    // 路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  }
}
```

3. Flutter 中正是通过这种方式封装了很多动画，如：FadeTransition、ScaleTransition、SizeTransition 等，很多时候都可以复用这些预置的过渡类

### ②、动画状态监听

1. 上面说过，我们可以通过 `Animation` 的 `addStatusListener()` 方法来添加动画状态改变监听器。
2. Flutter 中，有四种动画状态，在 `AnimationStatus` 枚举类中定义，下面我们逐个说明

| 枚举值    | 含义             |
| --------- | ---------------- |
| dismissed | 动画在起始点停止 |
| forward   | 动画正在正向执行 |
| reverse   | 动画正在反向执行 |
| completed | 动画在终点停止   |

3. 我们将上面图片放大的示例改为先放大再缩小再放大……这样的循环动画。
4. 要实现这种效果，我们只需要监听动画状态的改变即可，即：在动画正向执行结束时反转动画，在动画反向执行结束时再正向执行动画。代码如下：
5. `01_GrowTransitionStatusListener.dart` 过渡封装类

```dart
import 'package:flutter/cupertino.dart';

class GrowTransitionStatusListener extends StatelessWidget {
  const GrowTransitionStatusListener({Key? key, required this.animation, this.child,}) : super(key: key);

  // 子部件
  final Widget? child;
  // 动画对象
  final Animation<double> animation;

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，用于将其子部件居中显示。
    return Center(
      // AnimatedBuilder 是一个小部件，用于构建动画小部件，它可以封装常见的动画构建过程，省去了每次都要重新实现动画的麻烦。
      child: AnimatedBuilder(
        // 动画对象
        animation: animation,
        builder: (BuildContext context, child) {
          return SizedBox(
            height: animation.value,
            width: animation.value,
            child: child,
          );
        },
        child: child,
      ),
    );
  }

}
```

6. `01_GrowTransitionStatusListenerComponent.dart` 动画状态监听类

```dart
import 'package:flutter/material.dart';

import '01_GrowTransitionStatusListener.dart';


class GrowTransitionStatusListenerComponent extends StatefulWidget {
  const GrowTransitionStatusListenerComponent({Key? key}) : super(key: key);

  @override
  _GrowTransitionStatusListenerComponentState createState() => _GrowTransitionStatusListenerComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _GrowTransitionStatusListenerComponentState extends State<GrowTransitionStatusListenerComponent> with SingleTickerProviderStateMixin {
  // 动画对象
  late Animation<double> animation;
  // 动画控制器
  late AnimationController controller;

  @override
  initState() {
    super.initState();
    // 创建 AnimationController 对象，设置动画持续时间为 2 秒。
    controller = AnimationController(duration: const Duration(seconds: 2), vsync: this,);

    // Tween 的作用是设置动画的起始值和结束值，作为动画的补间值。
    animation = Tween(begin: 0.0, end: 300.0).animate(controller);
    // 添加动画状态监听器
    animation.addStatusListener((status) {
      if(status == AnimationStatus.completed){
        // 动画执行结束时反向执行动画；completed 表示动画已经执行结束。
        controller.reverse();
      }else if(status == AnimationStatus.dismissed){
        // 动画恢复到初始状态时执行动画（正向）；dismissed 表示动画又返回到初始状态。
        controller.forward();
      }
    });

    // 启动动画(正向执行)
    controller.forward();
  }

  @override
  dispose() {
    // 路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // AnimatedBuilder 是一个小部件，用于构建动画小部件，它可以封装常见的动画构建过程，省去了每次都要重新实现动画的麻烦。
    return GrowTransitionStatusListener(
      // 动画对象
      animation: animation,
      // 子部件
      child: Image.asset("asset/images/QQ图片20220920105928.jpg")
    );
  }

}
```

7. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画37.gif)

## 3、自定义路由切换动画

### ①、PageRouteBuilder

1. 我们在第二章“路由管理”一节中说过：Material 组件库中提供了一个 `MaterialPageRoute` 组件，它可以使用和平台风格一致的路由切换动画，如在 iOS 上会左右滑动切换，而在 Android 上会上下滑动切换。现在，我们如果在 Android 上也想使用左右切换风格，该怎么做？一个简单的作法是可以直接使用 `CupertinoPageRoute`，如：

```dart
 Navigator.push(context, CupertinoPageRoute(  
   builder: (context)=>PageB(),
 ));
```

2. `CupertinoPageRoute` 是 Cupertino 组件库提供的 iOS 风格的路由切换组件，它实现的就是左右滑动切换。那么我们如何来自定义路由切换动画呢？答案就是 `PageRouteBuilder`。
3. 下面我们来看看如何使用 `PageRouteBuilder` 来自定义路由切换动画。例如我们想以渐隐渐入动画来实现路由过渡，实现代码如下：

```dart
Navigator.push(
  context,
  PageRouteBuilder(
    // 动画时间为 500 毫秒
    transitionDuration: Duration(milliseconds: 500),
    pageBuilder: (BuildContext context, Animation animation, Animation secondaryAnimation) {
      return FadeTransition(
        // 使用渐隐渐入过渡,
        opacity: animation,
        // 路由 B
        child: PageB(),
      );
    },
  ),
);
```

4. 我们可以看到 `pageBuilder` 有一个 `animation` 参数，这是 Flutter 路由管理器提供的，在路由切换时 `pageBuilder` 在每个动画帧都会被回调，因此我们可以通过 `animation` 对象来自定义过渡动画。
5. 无论是 `MaterialPageRoute`、`CupertinoPageRoute`，还是 `PageRouteBuilder`，它们都继承自 `PageRoute` 类，而 `PageRouteBuilder` 其实只是 `PageRoute` 的一个包装，我们可以直接继承 `PageRoute` 类来实现自定义路由

### ②、继承 PageRoute 类来实现自定义路由

1. 定义一个路由类 `01_FadeRoute.dart`，继承 `PageRoute`，通过 `buildTransitions` 方法设置路由切换动画

```dart
import 'package:flutter/cupertino.dart';

class FadeRoute extends PageRoute {
  FadeRoute({
    required this.builder,
    this.transitionDuration = const Duration(milliseconds: 1000),
    this.opaque = true,
    this.barrierDismissible = false,
    this.barrierColor = const Color(0x00000000),
    this.barrierLabel = "",
    this.maintainState = true,
  });

  // 路由构建器
  final WidgetBuilder builder;

  // 动画持续时间
  @override
  final Duration transitionDuration;

  // 是否透明
  @override
  final bool opaque;

  // 是否可以通过点击背景关闭路由
  @override
  final bool barrierDismissible;

  // 遮罩颜色
  @override
  final Color barrierColor;

  // 遮罩标签
  @override
  final String barrierLabel;

  // 维护状态
  @override
  final bool maintainState;

  // buildPage 方法负责构建路由页面的具体内容，我们通常在此方法中使用 PageTransitionSwitcher 小部件来实现路由动画
  @override
  Widget buildPage(
      // context 参数和 Navigator.push 方法中的 context 是一样的
      BuildContext context,
      // animation 参数表示路由切换时的动画，是一个 Animation 对象
      Animation<double> animation,
      // secondaryAnimation 参数用于定义第二个路由（通常是新路由）的动画
      Animation<double> secondaryAnimation
      // 作用是构建路由页面的具体内容，它会在动画执行时被调用
    ) => builder(context);

  // buildTransitions 方法负责构建路由的过渡效果，它会在路由切换时被调用
  @override
  Widget buildTransitions(
      // context 参数和 Navigator.push 方法中的 context 是一样的
      BuildContext context,
      // animation 参数表示路由切换时的动画，是一个 Animation 对象
      Animation<double> animation,
      // secondaryAnimation 参数用于定义第二个路由（通常是新路由）的动画
      Animation<double> secondaryAnimation,
      // child 是路由当前的页面
      Widget child
    ) {
    // SlideTransition 是一个小部件，它可以对子部件实现平移动画；此处的效果为从右下角平移到左上角
    return SlideTransition(
      // 通过 position 参数来指定子部件的偏移；Tween 是一个抽象类，它定义了在两个值之间生成动画值的接口
      position: Tween<Offset>(
        // begin 和 end 分别表示动画的起始点和终止点；const Offset(1.0, 1.0) 表示从右下角开始
        begin: const Offset(1.0, 1.0),
        // Offset.zero 表示偏移量为 0，即动画结束时子部件的偏移量为 0，即动画结束时子部件的位置为屏幕左上角
        end: Offset.zero,
        // animate 方法用于生成动画值
      ).animate(animation),
      child: builder(context),
    );
  }

}
```

2. `02_FadeRouteHomeComponent.dart` 主页，可点击按钮进入设置

```dart
import 'package:flutter/material.dart';

import '01_FadeRoute.dart';
import '03_FadeRouteSettingComponent.dart';

// 创建一个 StatefulWidget 类
class FadeRouteHomeComponent extends StatelessWidget {
  const FadeRouteHomeComponent({super.key});

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.white,
      // Column 是一个小部件，用于在垂直方向排列子部件
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ElevatedButton(
            // 当按钮被点击时，打开新的路由
            onPressed: () => Navigator.push(context, FadeRoute(builder: (context){
              return const FadeRouteSettingComponent();
            })),
            child: const Text("点击进入设置", textDirection: TextDirection.ltr),
          )
        ],
      )
    );
  }
}
```

3. `02_FadeRouteHomeComponent.dart` 设置，可点击按钮返回主页

```dart
import 'package:flutter/material.dart';

class FadeRouteSettingComponent extends StatelessWidget {
  const FadeRouteSettingComponent({super.key});

  @override
  Widget build(BuildContext context) {

    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return SafeArea(
      child: Container(
        // 宽度尽可能的大
        width: double.infinity,
        // 高度尽可能的大
        height: double.infinity,
        // 颜色
        color: Colors.red,
        // 垂直线性布局
        child: Column(
          // 垂直居中
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              // 当按钮被点击时，返回上一个路由
              onPressed: (){
                // 返回上一个路由，并返回消息
                Navigator.pop(context);
              },
              child: const Text("点击返回主页", textDirection: TextDirection.ltr),
            )
          ],
        )
      )
    );
  }
}
```

4. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画38.gif)

5. 虽然上面的两种方法都可以实现自定义切换动画，但实际使用时应优先考虑使用 `PageRouteBuilder`，这样无需定义一个新的路由类，使用起来会比较方便。但是有些时候 `PageRouteBuilder` 是不能满足需求的，例如在应用过渡动画时我们需要读取当前路由的一些属性，这时就只能通过继承 `PageRoute` 的方式了
6. 举个例子，假如我们只想在打开新路由时应用动画，而在返回时不使用动画，那么我们在构建过渡动画时就必须判断当前路由 `isActive` 属性是否为 `true`，代码如下：

```dart
@override
Widget buildTransitions(BuildContext context, Animation<double> animation,
    Animation<double> secondaryAnimation, Widget child) {
 //当前路由被激活，是打开新路由
 if(isActive) {
   return FadeTransition(
     opacity: animation,
     child: builder(context),
   );
 }else{
   //是返回，则不应用过渡动画
   return Padding(padding: EdgeInsets.zero);
 }
}
```

## 4、Hero 动画

### ①、自实现 Hero 动画

1. 比如现在有一个头像组件，初始的时候是一个圆形的小图，我们想实现点击后查看大图的功能，为了有较好的体验，小图变成大图和大图变回小图时我们分别执行一个“飞行”过渡动画，效果如图所示：

![|346](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F9-2.2ae3da70.gif)

2. 要实现上面的动画效果，最简单的方式就是使用 Flutter 的 Hero 动画，但是为了理解 Hero 动画原理，先不使用 Hero 动画，而是通过之前章节所学的知识来实现一下这个效果。
3. 简单分析后有一个思路：首先我们先确定小图和大图的位置和大小，动画的话用一个 Stack，然后通过 Positioned 来设置每一帧的组件位置和大小，实现如下：

```dart
class CustomHeroAnimation extends StatefulWidget {
  const CustomHeroAnimation({Key? key}) : super(key: key);

  @override
  _CustomHeroAnimationState createState() => _CustomHeroAnimationState();
}

class _CustomHeroAnimationState extends State<CustomHeroAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  bool _animating = false;
  AnimationStatus? _lastAnimationStatus;
  late Animation _animation;

  //两个组件在Stack中所占的区域
  Rect? child1Rect;
  Rect? child2Rect;

  @override
  void initState() {
    _controller =
        AnimationController(vsync: this, duration: Duration(milliseconds: 200));
    //应用curve
    _animation = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeIn,
    );

    _controller.addListener(() {
      if (_controller.isCompleted || _controller.isDismissed) {
        if (_animating) {
          setState(() {
            _animating = false;
          });
        }
      } else {
        _lastAnimationStatus = _controller.status;
      }
    });
    super.initState();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    //小头像
    final Widget child1 = wChild1();
    //大头像
    final Widget child2 = wChild2();

    //是否展示小头像；只有在动画执行时、初始状态或者刚从大图变为小图时才应该显示小头像
    bool showChild1 =
        !_animating && _lastAnimationStatus != AnimationStatus.forward;

    // 执行动画时的目标组件；如果是从小图变为大图，则目标组件是大图；反之则是小图
    Widget targetWidget;
    if (showChild1 || _controller.status == AnimationStatus.reverse) {
      targetWidget = child1;
    } else {
      targetWidget = child2;
    }

    return LayoutBuilder(builder: (context, constraints) {
      return SizedBox(
        //我们让Stack 填满屏幕剩余空间
        width: constraints.maxWidth,
        height: constraints.maxHeight,
        child: Stack(
          alignment: AlignmentDirectional.topCenter,
          children: [
            if (showChild1)
              AfterLayout( 
                //获取小图在Stack中占用的Rect信息
                callback: (value) => child1Rect = _getRect(value),
                child: child1,
              ),
            if (!showChild1)
              AnimatedBuilder(
                animation: _animation,
                builder: (context, child) {
                  //求出 rect 插值
                  final rect = Rect.lerp(
                    child1Rect,
                    child2Rect,
                    _animation.value,
                  );
                  // 通过 Positioned 设置组件大小和位置
                  return Positioned.fromRect(rect: rect!, child: child!);
                },
                child: targetWidget,
              ),
            // 用于测量 child2 的大小，设置为全透明并且不能响应事件
            IgnorePointer(
              child: Center(
                child: Opacity(
                  opacity: 0,
                  child: AfterLayout(
                    //获取大图在Stack中占用的Rect信息
                    callback: (value) => child2Rect = _getRect(value),
                    child: child2,
                  ),
                ),
              ),
            ),
          ],
        ),
      );
    });
  }

  Widget wChild1() {
    //点击后执行正向动画
    return GestureDetector(
      onTap: () {
        setState(() {
          _animating = true;
          _controller.forward();
        });
      },
      child: SizedBox(
        width: 50,
        child: ClipOval(child: Image.asset("imgs/avatar.png")),
      ),
    );
  }

  Widget wChild2() {
    // 点击后执行反向动画
    return GestureDetector(
      onTap: () {
        setState(() {
          _animating = true;
          _controller.reverse();
        });
      },
      child: Image.asset("imgs/avatar.png", width: 400),
    );
  }

  Rect _getRect(RenderAfterLayout renderAfterLayout) {
    //我们需要获取的是AfterLayout子组件相对于Stack的Rect
    return renderAfterLayout.localToGlobal(
          Offset.zero,
          //找到Stack对应的 RenderObject 对象
          ancestor: context.findRenderObject(),
        ) &
        renderAfterLayout.size;
  }
}
```

4. 运行后点击头像就可以实现上图中的动画效果，注意，我们是通过自定义的 `AfterLayout` 组件来获取组件的 `Rect` 信息的，该组件在第四章介绍过
5. 可以看到，整个飞行动画的实现还是比较复杂的，但由于这种飞行动画在交互上会经常被用到，因此 Flutter 在框架层抽象了上述实现飞行动画的逻辑，提供了一种通用且简单的实现 Hero 动画的方式

### ②、Flutter Hero 动画

1. Hero 指的是可以在路由(页面)之间 “飞行” 的 widget，简单来说 Hero 动画就是在路由切换时，有一个共享的 widget 可以在新旧路由间切换。
2. 由于共享的 widget 在新旧路由页面上的位置、外观可能有所差异，所以在路由切换时会从旧路由逐渐过渡到新路由中的指定位置，这样就会产生一个 Hero 动画。
3. 你可能多次看到过 hero 动画。例如，一个路由中显示待售商品的缩略图列表，选择一个条目会将其跳转到一个新路由，新路由中包含该商品的详细信息和“购买”按钮。 在 Flutte r中将图片从一个路由“飞”到另一个路由称为 hero 动画，尽管相同的动作有时也称为 共享元素转换。下面我们通过一个示例来体验一下 hero 动画。

> 为什么要将这种可飞行的共享组件称为 hero（英雄），有一种说法是说美国文化中的超人是可以飞的，那是美国人心中的大英雄，还有漫威中的超级英雄基本上都是会飞的，所以 Flutter 开发人员就对这种 “会飞的 widget” 就起了一个富有浪漫主义的名字 hero。当然这种说法并非官方解释，但却很有意思。

4. 示例：假设有两个路由<font color="#ff0000">主页</font>和<font color="#ff0000">设置</font>，他们的内容交互如下：
	1. <font color="#ff0000">主页</font>：包含一个用户头像，圆形，点击后跳到<font color="#ff0000">设置</font>路由，可以查看大图。
	2. <font color="#ff0000">设置</font>：显示用户头像原图，矩形。
5. 在两个路由之间跳转的时候，用户头像会逐渐过渡到目标路由页的头像上，接下来我们先看看代码，然后再解析。
6. 主页 `02_1_HeroHomeComponent.dart`：

```dart
import 'package:flutter/material.dart';

import '02_2_HeroSettingComponent.dart';

// 创建一个 StatefulWidget 类
class HeroHomeComponent extends StatelessWidget {
  const HeroHomeComponent({super.key});

  @override
  Widget build(BuildContext context) {
    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return Container(
      // 宽度尽可能的大
      width: double.infinity,
      // 高度尽可能的大
      height: double.infinity,
      // 颜色
      color: Colors.white,
      // Column 是一个小部件，用于在垂直方向排列子部件
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          buildHero(),
          buildElevatedButton(context),
        ],
      )
    );
  }

  /// 构建 Hero；Hero 是一个小部件，用于在路由之间共享动画
  Widget buildHero(){
    return Hero(
      tag: "avatar",
      child: ClipOval(
        child: Image.asset("asset/images/QQ图片20220920105928.jpg", width: 50),
      ),
    );
  }

  /// 构建 ElevatedButton，用于打开新的路由
  Widget buildElevatedButton(BuildContext context){
    return ElevatedButton(
      // 当按钮被点击时，打开新的路由
      onPressed: () => Navigator.push(
        context,
        // 使用自定义的路由切换动画
        builderPageRouteBuilder(),
      ),
      child: const Text("点击进入设置", textDirection: TextDirection.ltr),
    );
  }

  /// 构建 PageRouteBuilder，用于自定义路由切换动画
  PageRouteBuilder builderPageRouteBuilder(){
    return PageRouteBuilder(
      // 动画时间为 1 秒
      transitionDuration: const Duration(seconds: 1),
      // 构建动画
      pageBuilder: (BuildContext context, Animation animation, Animation secondaryAnimation) {
        // SlideTransition 是一个小部件，用于在子部件上执行滑动动画
        return SlideTransition(
          // 设置动画，动画效果为从右下角滑动到左上角
          position: buildAnimation(animation),
          // 设置要跳转到的路由
          child: const HeroSettingComponent(),
        );
      },
    );
  }

  /// 构建动画，动画效果为从右下角滑动到左上角
  Animation<Offset> buildAnimation(Animation<dynamic> animation) {
    // animation.drive 表示给动画添加一个插值器，这里使用 Tween<Offset>，表示在动画的一段时间内，动画的值从 Offset(1.0, 1.0) 变化到 Offset.zero
    return animation.drive(
      // Tween 是一个小部件，用于在动画的一段时间内，动画的值从 begin 变化到 end；Offset 是一个小部件，用于表示偏移量
      Tween<Offset>(
        // begin 和 end 分别表示动画的起始点和终止点；const Offset(1.0, 1.0) 表示从右下角开始
        begin: const Offset(1.0, 1.0),
        // Offset.zero 表示偏移量为 0，即动画结束时子部件的偏移量为 0，即动画结束时子部件的位置为屏幕左上角
        end: Offset.zero,
      ),
    );
  }

}
```

7. 设置 `02_2_HeroSettingComponent.dart`：

```dart
import 'package:flutter/material.dart';

class HeroSettingComponent extends StatelessWidget {
  const HeroSettingComponent({super.key});

  @override
  Widget build(BuildContext context) {

    // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
    return SafeArea(
      child: Container(
        // 宽度尽可能的大
        width: double.infinity,
        // 高度尽可能的大
        height: double.infinity,
        // 颜色
        color: Colors.red,
        // 垂直线性布局
        child: Column(
          // 垂直居中
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            buildHero(),
            buildElevatedButton(context),
          ],
        )
      )
    );
  }

  /// 构建 Hero；Hero 是一个小部件，用于在路由之间共享动画
  Widget buildHero(){
    return Hero(
      tag: "avatar",
      child: ClipOval(
        child: Image.asset("asset/images/QQ图片20220920105928.jpg", width: 50),
      ),
    );
  }

  /// 构建 ElevatedButton
  Widget buildElevatedButton(BuildContext context){
    return ElevatedButton(
      // 当按钮被点击时，返回上一个路由
      onPressed: () => Navigator.pop(context),
      child: const Text("点击返回主页", textDirection: TextDirection.ltr),
    );
  }

}
```

8. 效果：

![|365](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画39.gif)

9. 我们可以看到，实现 Hero 动画只需要用 Hero 组件将要共享的 widget 包装起来，并提供一个相同的 tag 即可，中间的过渡帧都是 Flutter 框架自动完成的。必须要注意， 前后路由页的共享 Hero 的 <font color="#ff0000">tag</font> 必须是相同的，Flutter 框架内部正是通过 tag 来确定新旧路由页 widget 的对应关系的。
10. Hero 动画的原理比较简单，Flutter 框架知道新旧路由页中共享元素的位置和大小，所以根据这两个端点，在动画执行过程中求出过渡时的插值（中间态）即可，而感到幸运的是，这些事情不需要我们自己动手，Flutter 已经帮我们做了，实际上，Flutter Hero 动画的实现原理和我们在本章开始自实现的原理是差不多的，有兴趣可以去看 Hero 动画相关的源码。

## 5、交织动画

### ①、简介

1. 有些时候我们可能会需要一些复杂的动画，这些动画可能由一个动画序列或重叠的动画组成，比如：有一个柱状图，需要在高度增长的同时改变颜色，等到增长到最大高度后，我们需要在 X 轴上平移一段距离。可以发现上述场景在不同阶段包含了多种动画，要实现这种效果，使用交织动画（Stagger Animation）会非常简单。交织动画需要注意以下几点：
	1. 要创建交织动画，需要使用多个动画对象（Animation）。
	2. 一个 `AnimationController` 控制所有的动画对象。
	3. 给每一个动画对象指定时间间隔（Interval）
2. 所有动画都由同一个 `AnimationController` 驱动，无论动画需要持续多长时间，控制器的值必须在 `0.0` 到 `1.0` 之间，而每个动画的间隔（Interval）也必须介于 `0.0` 和 `1.0` 之间。
3. 对于在间隔中设置动画的每个属性，需要分别创建一个 `Tween` 用于指定该属性的开始值和结束值。也就是说 `0.0` 到 `1.0` 代表整个动画过程，我们可以给不同动画指定不同的起始点和终止点来决定它们的开始时间和终止时间

### ②、示例

> 下面我们看一个例子，实现一个柱状图增长的动画：
> 
> 1. 开始时高度从 0 增长到 300 像素，同时颜色由绿色渐变为红色；这个过程占据整个动画时间的 60%。
> 2. 高度增长到 300 后，开始沿 X 轴向右平移 100 像素，同时宽度增长到 100 像素；这个过程占用整个动画时间的 40%。

1. 我们将执行动画的 `01_StaggerAnimation.dart` 分离出来，`StaggerAnimation` 中定义了四个动画，分别是对 `Container` 的 `weight`、`height`、`color`、`padding` 属性设置的动画，然后通过 `Interval` 来为每个动画指定在整个动画过程中的起始点和终点。

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class StaggerAnimation extends StatelessWidget {
  // 构造函数；其中的 height 等参数会在实例化时被赋值
  StaggerAnimation({Key? key, required this.controller,}) : super(key: key) {

    // 高度动画；从 0 到 300，匀速曲线；即匀速上升
    height = Tween<double>(
      begin: .0,
      end: 300.0,
    ).animate(
      // 设置非线性动画，先快后慢
      CurvedAnimation(
        parent: controller,
        // Interval 用于设置动画的开始点和结束点；这里的 Interval(0.0, 0.6) 表示动画开始于 0.0 处，结束于 0.6 处
        curve: const Interval(0.0, 0.6, curve: Curves.ease),
      ),
    );

    // 颜色动画；从绿色到红色，匀速曲线；即匀速变色
    color = ColorTween(
      begin: Colors.green,
      end: Colors.red,
    ).animate(
      // 设置非线性动画，先快后慢
      CurvedAnimation(
        parent: controller,
        // Interval 用于设置动画的开始点和结束点；这里的 Interval(0.0, 0.6) 表示动画开始于 0.0 处，结束于 0.6 处
        curve: const Interval(0.0, 0.6, curve: Curves.ease,),
      ),
    );

    // 宽度动画；从 50 到 100，匀速曲线；即匀速变宽
    weight = Tween<double>(
      begin: 50,
      end: 100,
    ).animate(
      // 设置非线性动画，先快后慢
      CurvedAnimation(
        parent: controller,
        // Interval 用于设置动画的开始点和结束点；这里的 Interval(0.6, 1.0) 表示动画开始于 0.6 处，结束于 1.0 处
        curve: const Interval(0.6, 1.0, curve: Curves.ease),
      ),
    );

    // 左边距动画；从 0 到 100，匀速曲线；即匀速向右移动
    padding = Tween<EdgeInsets>(
      begin: const EdgeInsets.only(left: .0),
      end: const EdgeInsets.only(left: 100.0),
    ).animate(
      // 设置非线性动画，先快后慢
      CurvedAnimation(
        parent: controller,
        // Interval 用于设置动画的开始点和结束点；这里的 Interval(0.6, 1.0) 表示动画开始于 0.6 处，结束于 1.0 处
        curve: const Interval(0.6, 1.0, curve: Curves.ease,),
      ),
    );
  }

  late final Animation<double> controller;
  late final Animation<double> weight;
  late final Animation<double> height;
  late final Animation<EdgeInsets> padding;
  late final Animation<Color?> color;

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      builder: _buildAnimation,
      animation: controller,
    );
  }

  /// 构建动画
  Widget _buildAnimation(BuildContext context, child) {
    // 返回一个容器，容器的高度、颜色、左边距都会发生变化
    return Container(
      alignment: Alignment.bottomCenter,
      padding: padding.value,
      child: Container(
        color: color.value,
        width: weight.value,
        height: height.value,
      ),
    );
  }

}
```

2. 下面我们来实现启动动画的路由：

```dart
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '01_StaggerAnimation.dart';

class StaggerRouteComponent extends StatefulWidget {
  const StaggerRouteComponent({super.key});

  @override
  _StaggerRouteComponentState createState() => _StaggerRouteComponentState();
}

class _StaggerRouteComponentState extends State<StaggerRouteComponent> with TickerProviderStateMixin {
  // 定义动画控制器
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    // 创建动画控制器；设置动画时长为 2 秒；vsync 为 this，即当前 TickerProviderStateMixin 实例
    _controller = AnimationController(duration: const Duration(milliseconds: 2000), vsync: this,);
  }

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，用于将其子部件在父部件中居中
    return Center(
      // Column 是一个小部件，用于在垂直方向排列子部件
      child: Column(
        children: [
          // 点击按钮，执行动画
          ElevatedButton(
            onPressed: () => _playAnimation(),
            child: const Text("开始"),
          ),
          // Container 是一个多功能的小部件，可以用于设置子部件的大小、位置、装饰、填充等
          Container(
            width: 300.0,
            height: 300.0,
            // BoxDecoration 是一个装饰类小部件，它可以在其子小部件之上绘制一个装饰，如背景、边框、渐变等。
            decoration: BoxDecoration(
              // 背景色
              color: Colors.black.withOpacity(0.1),
              // 边框
              border: Border.all(color: Colors.black.withOpacity(0.5),),
            ),
            // 调用我们定义的交错动画 Widget
            child: StaggerAnimation(controller: _controller),
          ),
        ],
      ),
    );
  }

  /// 执行动画
  _playAnimation() async {
    try {
      // 先正向执行动画
      await _controller.forward().orCancel;
      // 再反向执行动画
      await _controller.reverse().orCancel;
    } on TickerCanceled {
      // 捕获异常。可能发生在组件销毁时，计时器会被取消。
    }
  }

}
```

3. 效果：

![|365](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画40.gif)

## 6、动画切换组件（AnimatedSwitcher）

1. 实际开发中，我们经常会遇到切换 UI 元素的场景，比如 Tab 切换、路由切换。
2. 为了增强用户体验，通常在切换时都会指定一个动画，以使切换过程显得平滑。
3. Flutter SDK 组件库中已经提供了一些常用的切换组件，如 `PageView`、`TabView` 等，但是，这些组件并不能覆盖全部的需求场景，为此，Flutter SDK 中提供了一个 `AnimatedSwitcher` 组件，它定义了一种通用的 UI 切换抽象。

### ①、AnimatedSwitcher

#### Ⅰ、简介

1. `AnimatedSwitcher` 可以同时对其新、旧子元素添加显示、隐藏动画。也就是说在 `AnimatedSwitcher` 的子元素发生变化时，会对其旧元素和新元素做动画，我们先看看 `AnimatedSwitcher` 的定义：

```dart
const AnimatedSwitcher({
  Key? key,
  this.child,
  required this.duration, // 新child显示动画时长
  this.reverseDuration,// 旧child隐藏的动画时长
  this.switchInCurve = Curves.linear, // 新child显示的动画曲线
  this.switchOutCurve = Curves.linear,// 旧child隐藏的动画曲线
  this.transitionBuilder = AnimatedSwitcher.defaultTransitionBuilder, // 动画构建器
  this.layoutBuilder = AnimatedSwitcher.defaultLayoutBuilder, //布局构建器
})
```

2. 当 `AnimatedSwitcher` 的 `child` 发生变化时（类型或 Key 不同），旧 `child` 会执行隐藏动画，新 `child` 会执行执行显示动画。究竟执行何种动画效果则由 `transitionBuilder` 参数决定，该参数接受一个 `AnimatedSwitcherTransitionBuilder` 类型的 `builder`，定义如下：

```dart
typedef AnimatedSwitcherTransitionBuilder = Widget Function(Widget child, Animation<double> animation);
```

3. 该 `builder` 在 `AnimatedSwitcher` 的 `child` 切换时会分别对新、旧 `child` 绑定动画：
	1. 对旧 `child`，绑定的动画会反向执行（`reverse`）
	2. 对新 `child`，绑定的动画会正向指向（`forward`）
4. 这样一下，便实现了对新、旧 `child` 的动画绑定。`AnimatedSwitcher` 的默认值是 `AnimatedSwitcher.defaultTransitionBuilder` ：

```dart
Widget defaultTransitionBuilder(Widget child, Animation<double> animation) {
  return FadeTransition(
    opacity: animation,
    child: child,
  );
}
```

5. 可以看到，返回了 `FadeTransition` 对象，也就是说默认情况，`AnimatedSwitcher` 会对新旧 `child` 执行“渐隐”和“渐显”动画

#### Ⅱ、示例

1. 下面我们看一个例子：实现一个计数器，然后在每一次自增的过程中，旧数字执行缩小动画隐藏，新数字执行放大动画显示
2. 代码如下：

```dart
import 'package:flutter/material.dart';

class AnimatedSwitcherCounterRoute extends StatefulWidget {
  const AnimatedSwitcherCounterRoute({super.key});

  @override
  _AnimatedSwitcherCounterRouteState createState() => _AnimatedSwitcherCounterRouteState();
}

class _AnimatedSwitcherCounterRouteState extends State<AnimatedSwitcherCounterRoute> {
  // 计数
  int _count = 0;

  @override
  Widget build(BuildContext context) {
    // Center 是一个小部件，用于将其子部件在父部件中居中显示
    return Center(
      // Column 是一个小部件，用于在垂直方向排列子部件
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          // 构建动画切换组件
          buildAnimatedSwitcher(),
          // 构建按钮
          buildElevatedButton(),
        ],
      ),
    );
  }

  /// 构建动画切换组件
  Widget buildAnimatedSwitcher(){
    // AnimatedSwitcher 是一个小部件，用于在新旧小部件之间切换时添加动画
    return AnimatedSwitcher(
      // 动画持续时间
      duration: const Duration(milliseconds: 500),
      // 动画构建器
      transitionBuilder: (Widget child, Animation<double> animation) {
        // ScaleTransition 是一个小部件，用于对子部件进行缩放动画
        return ScaleTransition(scale: animation, child: child);
      },
      // AnimatedSwitcher 中的子部件，每当需要切换时，AnimatedSwitcher 会对其执行动画
      child: Text(
        // 参数 1：文本内容
        '$_count',
        // 参数 2：用于指定 Text 小部件的 key；如果两个 Text 的 key 相同，则认为它们是同一个小部件，此时不会执行动画
        key: ValueKey<int>(_count),
        // 参数 3：文本样式
        style: Theme.of(context).textTheme.headline4,
      ),
    );
  }

  /// 构建按钮
  Widget buildElevatedButton(){
    return ElevatedButton(
      child: const Icon(Icons.add),
      onPressed: () {
        setState(() {
          _count += 1;
        });
      },
    );
  }

}
```

3. 效果：

![|386](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画41.gif)

4. 注意：`AnimatedSwitcher` 的新旧 `child`，如果类型相同，则 `Key` 必须不相等

#### Ⅲ、AnimatedSwitcher 实现原理

1. 实际上，`AnimatedSwitcher` 的实现原理是比较简单的，我们根据 `AnimatedSwitcher` 的使用方式也可以猜个大概。要想实现新旧 `child` 切换动画，只需要明确两个问题：
	1. 动画执行的时机是什么时候？
	2. 如何对新旧 `child` 执行动画？
2. 从 `AnimatedSwitcher` 的使用方式我们可以看到：当 `child` 发生变化时（子 widget 的 key 或类型不同时则认为发生变化），则重新会重新执行 build，然后动画开始执行。
3. 我们可以通过继承 `StatefulWidget` 来实现 `AnimatedSwitcher`，具体做法是在 `didUpdateWidget` 回调中判断其新旧 `child` 是否发生变化，如果发生变化，则对旧 `child` 执行反向退场（reverse）动画，对新 `child` 执行正向（forward）入场动画即可。下面是 `AnimatedSwitcher` 实现的部分核心伪代码：

```dart
Widget _widget; 
void didUpdateWidget(AnimatedSwitcher oldWidget) {
  super.didUpdateWidget(oldWidget);
  // 检查新旧child是否发生变化(key和类型同时相等则返回true，认为没变化)
  if (Widget.canUpdate(widget.child, oldWidget.child)) {
    // child没变化，...
  } else {
    //child发生了变化，构建一个Stack来分别给新旧child执行动画
   _widget= Stack(
      alignment: Alignment.center,
      children:[
        //旧child应用FadeTransition
        FadeTransition(
         opacity: _controllerOldAnimation,
         child : oldWidget.child,
        ),
        //新child应用FadeTransition
        FadeTransition(
         opacity: _controllerNewAnimation,
         child : widget.child,
        ),
      ]
    );
    // 给旧child执行反向退场动画
    _controllerOldAnimation.reverse();
    //给新child执行正向入场动画
    _controllerNewAnimation.forward();
  }
}

//build方法
Widget build(BuildContext context){
  return _widget;
}
```

4. 上面伪代码展示了 `AnimatedSwitcher` 实现的核心逻辑，当然 `AnimatedSwitcher` 真正的实现比这个复杂，它可以自定义进退场过渡动画以及执行动画时的布局等。在此，我们删繁就简，通过伪代码形式让读者能够清楚看到主要的实现思路，具体的实现可以参考 `AnimatedSwitcher` 源码。
5. 另外，Flutter SDK 中还提供了一个 `AnimatedCrossFade` 组件，它也可以切换两个子元素，切换过程执行渐隐渐显的动画，和 `AnimatedSwitcher` 不同的是 `AnimatedCrossFade` 是针对两个子元素，而 `AnimatedSwitcher` 是在一个子元素的新旧值之间切换。`AnimatedCrossFade` 实现原理也比较简单，和 `AnimatedSwitcher` 类似，因此不再赘述，有兴趣可以查看其源码

### ②、AnimatedSwitcher 高级用法

1. 假设现在我们想实现一个类似路由平移切换的动画：旧页面屏幕中向左侧平移退出，新页面从屏幕右侧平移进入。如果要用 `AnimatedSwitcher` 的话，我们很快就会发现一个问题：做不到！我们可能会写出下面的代码：

```dart
AnimatedSwitcher(
  duration: Duration(milliseconds: 200),
  transitionBuilder: (Widget child, Animation<double> animation) {
    var tween = Tween<Offset>(begin: Offset(1, 0), end: Offset(0, 0))
     return SlideTransition(
       child: child,
       position: tween.animate(animation),
    );
  },
  ...//省略
)
```

2. 上面的代码有什么问题呢？我们前面说过在 `AnimatedSwitcher` 的 `child` 切换时会对新 `child` 执行正向动画（forward），而对旧 `child` 执行反向动画（reverse），所以真正的效果便是：新 `child` 确实从屏幕右侧平移进入了，但旧 `child` 却会从屏幕右侧（而不是左侧）退出。其实也很容易理解，因为在没有特殊处理的情况下，同一个动画的正向和逆向正好是相反（对称）的。
3. 那么问题来了，难道就不能使用 `AnimatedSwitcher` 了？答案当然是否定的！仔细想想这个问题，究其原因，就是因为同一个 `Animation` 正向（forward）和反向（reverse）是对称的。所以如果我们可以打破这种对称性，那么便可以实现这个功能了，下面我们来封装一个MySlideTransition，它与SlideTransition唯一的不同就是对动画的反向执行进行了定制（从左边滑出隐藏），代码如下：

```dart
class MySlideTransition extends AnimatedWidget {
  const MySlideTransition({
    Key? key,
    required Animation<Offset> position,
    this.transformHitTests = true,
    required this.child,
  }) : super(key: key, listenable: position);

  final bool transformHitTests;

  final Widget child;

  @override
  Widget build(BuildContext context) {
    final position = listenable as Animation<Offset>;
    Offset offset = position.value;
    if (position.status == AnimationStatus.reverse) {
      offset = Offset(-offset.dx, offset.dy);
    }
    return FractionalTranslation(
      translation: offset,
      transformHitTests: transformHitTests,
      child: child,
    );
  }
}
```

4. 调用时，将 `SlideTransition` 替换成 `MySlideTransition` 即可：

```dart
AnimatedSwitcher(
  duration: Duration(milliseconds: 200),
  transitionBuilder: (Widget child, Animation<double> animation) {
    var tween=Tween<Offset>(begin: Offset(1, 0), end: Offset(0, 0))
     return MySlideTransition(
      child: child,
      position: tween.animate(animation),
    );
  },
  ...//省略
)
```

5. 运行后，我截取动画执行过程中的一帧，如图所示：

![|295](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231207095229.png)

6. 上图中 “0” 从左侧滑出，而 “1” 从右侧滑入。
7. 可以看到，我们通过这种巧妙的方式实现了类似路由进场切换的动画，实际上 Flutter 路由切换也正是通过 `AnimatedSwitcher` 来实现的。

### ③、SlideTransitionX

1. 上面的示例我们实现了“左出右入”的动画，那如果要实现“左入右出”、“上入下出”或者 “下入上出”怎么办？当然，我们可以分别修改上面的代码，但是这样每种动画都得单独定义一个 “Transition”，这很麻烦。
2. 这里将封装一个通用的 `SlideTransitionX` 来实现这种“出入动画”，代码如下：

```dart
class SlideTransitionX extends AnimatedWidget {
  SlideTransitionX({
    Key? key,
    required Animation<double> position,
    this.transformHitTests = true,
    this.direction = AxisDirection.down,
    required this.child,
  }) : super(key: key, listenable: position) {
    switch (direction) {
      case AxisDirection.up:
        _tween = Tween(begin: const Offset(0, 1), end: const Offset(0, 0));
        break;
      case AxisDirection.right:
        _tween = Tween(begin: const Offset(-1, 0), end: const Offset(0, 0));
        break;
      case AxisDirection.down:
        _tween = Tween(begin: const Offset(0, -1), end: const Offset(0, 0));
        break;
      case AxisDirection.left:
        _tween = Tween(begin: const Offset(1, 0), end: const Offset(0, 0));
        break;
    }
  }

  final bool transformHitTests;

  final Widget child;

  final AxisDirection direction;

  late final Tween<Offset> _tween;

  @override
  Widget build(BuildContext context) {
    final position = listenable as Animation<double>;
    Offset offset = _tween.evaluate(position);
    if (position.status == AnimationStatus.reverse) {
      switch (direction) {
        case AxisDirection.up:
          offset = Offset(offset.dx, -offset.dy);
          break;
        case AxisDirection.right:
          offset = Offset(-offset.dx, offset.dy);
          break;
        case AxisDirection.down:
          offset = Offset(offset.dx, -offset.dy);
          break;
        case AxisDirection.left:
          offset = Offset(-offset.dx, offset.dy);
          break;
      }
    }
    return FractionalTranslation(
      translation: offset,
      transformHitTests: transformHitTests,
      child: child,
    );
  }
}
```

3. 现在如果我们想实现各种“滑动出入动画”便非常容易，只需给 `direction` 传递不同的方向值即可，比如要实现“上入下出”，则：

```dart
AnimatedSwitcher(
  duration: Duration(milliseconds: 200),
  transitionBuilder: (Widget child, Animation<double> animation) {
    var tween=Tween<Offset>(begin: Offset(1, 0), end: Offset(0, 0))
     return SlideTransitionX(
       child: child,
       direction: AxisDirection.down, //上入下出
       position: animation,
     );
  },
  ...//省略其余代码
)
```

4. 运行后如图所示：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F9-2.2ae3da70%201.gif)

5. 上图中 “0” 从底部滑出，而 “1” 从顶部滑入。可以尝试给 `SlideTransitionX` 的 `direction` 取不同的值来查看运行效果。

## 7、动画过渡组件

1. 为了表述方便，这里约定，将在 Widget 属性发生变化时会执行过渡动画的组件统称为”动画过渡组件“，而动画过渡组件最明显的一个特征就是它会在内部自管理 `AnimationController`。
2. 我们知道，为了方便使用者可以自定义动画的曲线、执行时长、方向等，在前面介绍过的动画封装方法中，通常都需要使用者自己提供一个 `AnimationController` 对象来自定义这些属性值。
3. 但是，如此一来，使用者就必须得手动管理 `AnimationController`，这又会增加使用的复杂性。因此，如果也能将 `AnimationController` 进行封装，则会大大提高动画组件的易用性

### ①、自定义动画过渡组件

1. 我们要实现一个 `AnimatedDecoratedBox`，它可以在 `decoration` 属性发生变化时，从旧状态变成新状态的过程可以执行一个过渡动画。根据前面所学的知识，我们实现了一个 `AnimatedDecoratedBox1` 组件：

```dart
import 'package:flutter/cupertino.dart';

class AnimatedDecoratedBox1 extends StatefulWidget {
  const AnimatedDecoratedBox1({
    Key? key,
    required this.decoration,
    required this.child,
    this.curve = Curves.linear,
    required this.duration,
    this.reverseDuration,
  }) : super(key: key);

  // decoration 用于指定装饰样式
  final BoxDecoration decoration;
  // child 用于指定子部件
  final Widget child;
  // curve 用于指定动画的曲线
  final Curve curve;
  // duration 用于指定动画的时长
  final Duration duration;
  // reverseDuration 用于指定反向动画的时长
  final Duration? reverseDuration;

  @override
  _AnimatedDecoratedBox1State createState() => _AnimatedDecoratedBox1State();
}

class _AnimatedDecoratedBox1State extends State<AnimatedDecoratedBox1> with SingleTickerProviderStateMixin {
  /// @protected 修饰符表示该变量只能在子类中访问；
  /// get controller => _controller 表示该变量的 getter 方法返回 _controller
  /// _controller 是 AnimationController 类型的变量，用于控制动画
  @protected
  AnimationController get controller => _controller;
  late AnimationController _controller;

  /// get animation => _animation 表示该变量的 getter 方法返回 _animation
  /// _animation 是 Animation<double> 类型的变量，用于保存动画的值
  Animation<double> get animation => _animation;
  late Animation<double> _animation;

  /// _tween 是 DecorationTween 类型的变量，用于保存动画的起始值和结束值
  late DecorationTween _tween;

  /// initState 方法是 State 的生命周期方法，它会在 State 对象被插入视图树时被调用
  @override
  void initState() {
    super.initState();

    // 创建 AnimationController 对象，用于控制动画
    _controller = AnimationController(
      // duration 用于指定动画的时长
      duration: widget.duration,
      // reverseDuration 用于指定反向动画的时长
      reverseDuration: widget.reverseDuration,
      vsync: this,
    );
    // 设置动画的起始值和结束值；begin 为动画的起始值，end 为动画的结束值
    _tween = DecorationTween(begin: widget.decoration);
    _updateCurve();
  }

  /// dispose 方法是 State 的生命周期方法，它会在 State 对象从视图树中被移除时调用
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    /// AnimatedBuilder 是一个小部件，用于构建动画
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        // DecoratedBox 是一个小部件，用于绘制装饰样式的盒子
        return DecoratedBox(
          // decoration 用于指定装饰样式
          decoration: _tween.animate(_animation).value,
          child: child,
        );
      },
      child: widget.child,
    );
  }

  /// didUpdateWidget 方法是 State 的生命周期方法，它会在 State 对象的依赖发生变化时被调用
  @override
  void didUpdateWidget(AnimatedDecoratedBox1 oldWidget) {
    super.didUpdateWidget(oldWidget);
    // 判断动画的曲线是否发生了变化，如果发生了变化，则更新动画的曲线
    if (widget.curve != oldWidget.curve) _updateCurve();
    // duration 用于指定动画的时长
    _controller.duration = widget.duration;
    // reverseDuration 用于指定反向动画的时长
    _controller.reverseDuration = widget.reverseDuration;
    // 判断装饰样式是否发生了变化，如果发生了变化，则更新动画的起始值和结束值，并执行动画
    if (widget.decoration != (_tween.end ?? _tween.begin)) {
      _tween
        ..begin = _tween.evaluate(_animation)
        ..end = widget.decoration;

      _controller
        ..value = 0.0
        ..forward();
    }
  }

  /// 更新动画的曲线
  void _updateCurve() {
    _animation = CurvedAnimation(parent: _controller, curve: widget.curve);
  }

}
```

2. 下面我们来使用 `AnimatedDecoratedBox1` 来实现按钮点击后背景色从蓝色过渡到红色的效果：

```dart
import 'package:flutter/material.dart';

import '01_AnimatedDecoratedBox1.dart';


class AnimatedDecoratedComponent extends StatefulWidget {
  const AnimatedDecoratedComponent({Key? key}) : super(key: key);

  @override
  _AnimatedDecoratedComponentState createState() => _AnimatedDecoratedComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _AnimatedDecoratedComponentState extends State<AnimatedDecoratedComponent> with SingleTickerProviderStateMixin {
  Color _decorationColor = Colors.blue;
  var duration = const Duration(seconds: 1);

  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      child: AnimatedDecoratedBox1(
        // duration 用于指定动画的时长
        duration: duration,
        // decoration 用于指定装饰样式
        decoration: BoxDecoration(color: _decorationColor),
        child: buildTextButton()
      ),
    );
  }

  /// 构建文本按钮
  Widget buildTextButton(){
    return TextButton(
      onPressed: () {
        // 如果盒子的颜色为红色，则点击后将其改为蓝色；如果盒子的颜色为蓝色，则点击后将其改为红色
        setState(() {
          if(_decorationColor == Colors.red){
            _decorationColor = Colors.blue;
          }else{
            _decorationColor = Colors.red;
          }
        });
      },
      child: const Text(
        "AnimatedDecoratedBox",
        style: TextStyle(color: Colors.white),
      ),
    );
  }

}
```

3. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画42.gif)

4. 点击后，按钮背景色会从蓝色向红色过渡。上面的代码虽然实现了我们期望的功能，但是代码却比较复杂。
5. 稍加思考后，我们就可以发现，`AnimationController` 的管理以及 `Tween` 更新部分的代码都是可以抽象出来的，如果我们这些通用逻辑封装成基类，那么要实现动画过渡组件只需要继承这些基类，然后定制自身不同的代码（比如动画每一帧的构建方法）即可，这样将会简化代码。

### ②、动画过渡组件

1. 为了方便开发者来实现动画过渡组件的封装，Flutter 提供了一个 `ImplicitlyAnimatedWidget` 抽象类，它继承自 `StatefulWidget`，同时提供了一个对应的 `ImplicitlyAnimatedWidgetState` 类，`AnimationController` 的管理就在 `ImplicitlyAnimatedWidgetState` 类中。开发者如果要封装动画，只需要分别继承 `ImplicitlyAnimatedWidget` 和 `ImplicitlyAnimatedWidgetState` 类即可，下面我们演示一下具体如何实现。
2. 继承 `ImplicitlyAnimatedWidget` 类；其中 `curve`、`duration`、`reverseDuration` 三个属性在 `ImplicitlyAnimatedWidget` 中已定义。 可以看到 `AnimatedDecoratedBox` 类和普通继承自 `StatefulWidget` 的类没有什么不同。

```dart
import 'package:flutter/cupertino.dart';

// 1、继承 ImplicitlyAnimatedWidget 类
class AnimatedDecoratedBox extends ImplicitlyAnimatedWidget {
  const AnimatedDecoratedBox({
    Key? key,
    // decoration 用于指定装饰样式
    required this.decoration,
    required this.child,
    // curve 用于指定动画的运行方式；Curves.linear 为匀速运动
    Curve curve = Curves.linear,
    // duration 用于指定动画的时长
    required Duration duration,
  }) : super(
    key: key,
    curve: curve,
    duration: duration,
  );

  final BoxDecoration decoration;
  final Widget child;

  @override
  _AnimatedDecoratedBoxState createState() => _AnimatedDecoratedBoxState();
}
```

3. `State` 类继承自 `AnimatedWidgetBaseState`（该类继承自 `ImplicitlyAnimatedWidgetState` 类）；

```dart
// 2、State 类继承自 AnimatedWidgetBaseState（该类继承自ImplicitlyAnimatedWidgetState类）
class _AnimatedDecoratedBoxState extends AnimatedWidgetBaseState<AnimatedDecoratedBox> {
  DecorationTween? _decoration;

  @override
  Widget build(BuildContext context) {
    // DecoratedBox 是一个小部件，用于绘制带有装饰的盒子
    return DecoratedBox(
      // decoration 用于指定装饰样式
      decoration: _decoration!.evaluate(animation),
      child: widget.child,
    );
  }

  /// forEachTween 方法用于遍历动画中的每一个 Tween；比 initState 方法先执行
  @override
  void forEachTween(TweenVisitor<dynamic> visitor) {
    /// visitor 方法用于遍历动画中的每一个 Tween，
    /// 该方法接受三个参数：
    /// 1、dynamic 类型的 value，表示 Tween 的初始值，也就是动画开始时的值
    /// 2、Tween<dynamic> 类型的 tween，表示 Tween，也就是动画结束时的值
    /// 3、动画的属性，如 opacity、color、width 等，用于指定动画的类型
    _decoration = visitor(
      _decoration,
      widget.decoration,
      (value) => DecorationTween(begin: value),
    ) as DecorationTween;
  }
}
```

4. 可以看到上面我们实现了 `build` 和 `forEachTween` 两个方法。在动画执行过程中，每一帧都会调用 build 方法（调用逻辑在 `ImplicitlyAnimatedWidgetState` 中），所以在 build 方法中我们需要构建每一帧的 `DecoratedBox` 状态，因此得算出每一帧的 `decoration` 状态，这个我们可以通过 `_decoration.evaluate(animation)` 来算出，其中 `animation` 是 `ImplicitlyAnimatedWidgetState` 基类中定义的对象，`_decoration` 是我们自定义的一个 `DecorationTween` 类型的对象
5. 那么现在的问题就是它是在什么时候被赋值的呢？要回答这个问题，我们就得搞清楚什么时候需要对 `_decoration` 赋值。我们知道 `_decoration` 是一个 Tween，而 Tween 的主要职责就是定义动画的起始状态（begin）和终止状态(end)。对于 `AnimatedDecoratedBox` 来说，`decoration` 的终止状态就是用户传给它的值，而起始状态是不确定的，有以下两种情况：
	1. `AnimatedDecoratedBox` 首次 build，此时直接将其 `decoration` 值置为起始状态，即 `_decoration` 值为 `DecorationTween(begin: decoration)` 。
	2. `AnimatedDecoratedBox` 的 `decoration` 更新时，则起始状态为 `_decoration.animate(animation)`，即 `_decoration` 值为 `DecorationTween(begin: _decoration.animate(animation)，end:decoration)`。
6. 现在 `forEachTween` 的作用就很明显了，它正是用于来更新 Tween 的初始值的，在上述两种情况下会被调用，而开发者只需重写此方法，并在此方法中更新 Tween 的起始状态值即可。而一些更新的逻辑被屏蔽在了 visitor 回调，我们只需要调用它并给它传递正确的参数即可，visitor 方法签名如下：

```dart
 Tween<T> visitor(
   Tween<T> tween, //当前的tween，第一次调用为null
   T targetValue, // 终止状态
   TweenConstructor<T> constructor，//Tween构造器，在上述三种情况下会被调用以更新tween
 );
```

7. 可以看到，通过继承 `ImplicitlyAnimatedWidget` 和 `ImplicitlyAnimatedWidgetState` 类可以快速的实现动画过渡组件的封装，这和我们纯手工实现相比，代码简化了很多。
8. 如果还有疑惑，建议查看 `ImplicitlyAnimatedWidgetState` 的源码并结合本示例代码对比理解
9. 使用 `AnimatedDecoratedBox` 的示例：

```dart
import 'package:flutter/material.dart';

import '02_1_AnimatedDecoratedBox.dart';

class AnimatedDecoratedComponent extends StatefulWidget {
  const AnimatedDecoratedComponent({Key? key}) : super(key: key);

  @override
  _AnimatedDecoratedComponentState createState() => _AnimatedDecoratedComponentState();
}

// 需要继承 TickerProvider，如果有多个 AnimationController，则应该使用 TickerProviderStateMixin。
class _AnimatedDecoratedComponentState extends State<AnimatedDecoratedComponent> with SingleTickerProviderStateMixin {
  final Color _decorationColor = Colors.blue;
  var duration = const Duration(seconds: 1);

  @override
  Widget build(BuildContext context) {
    // Center 是一个用于将其子部件树对齐到屏幕中心的小部件
    return Center(
      child: AnimatedDecoratedBox(
        // duration 用于指定动画的时长
        duration: duration,
        // decoration 用于指定装饰样式
        decoration: BoxDecoration(color: _decorationColor),
        child: buildTextButton()
      ),
    );
  }

  /// 构建文本按钮
  Widget buildTextButton(){
    return TextButton(
      onPressed: () {
        // 如果盒子的颜色为红色，则点击后将其改为蓝色；如果盒子的颜色为蓝色，则点击后将其改为红色
        setState(() {
          _decorationColor == Colors.red ? Colors.blue : Colors.red;
        });
      },
      child: const Text(
        "AnimatedDecoratedBox",
        style: TextStyle(color: Colors.white),
      ),
    );
  }

}
```

### ③、Flutter 预置的动画过渡组件

1. Flutter SDK 中也预置了很多动画过渡组件，实现方式和大都和 `AnimatedDecoratedBox` 差不多，如表所示：

| 组件名                   | 功能                                                                     |
| ------------------------ | ------------------------------------------------------------------------ |
| AnimatedPadding          | 在padding发生变化时会执行过渡动画到新状态                                |
| AnimatedPositioned       | 配合Stack一起使用，当定位状态发生变化时会执行过渡动画到新的状态。        |
| AnimatedOpacity          | 在透明度opacity发生变化时执行过渡动画到新状态                            |
| AnimatedAlign            | 当alignment发生变化时会执行过渡动画到新的状态。                          |
| AnimatedContainer        | 当Container属性发生变化时会执行过渡动画到新的状态。                      |
| AnimatedDefaultTextStyle | 当字体样式发生变化时，子组件中继承了该样式的文本组件会动态过渡到新样式。 |

2. 下面我们通过一个示例来感受一下这些预置的动画过渡组件效果：

```dart
import 'package:flutter/material.dart';

import '01_1_AnimatedDecoratedBox1.dart';

class AnimatedWidgetsTest extends StatefulWidget {
  const AnimatedWidgetsTest({Key? key}) : super(key: key);

  @override
  _AnimatedWidgetsTestState createState() => _AnimatedWidgetsTestState();
}

class _AnimatedWidgetsTestState extends State<AnimatedWidgetsTest> {
  double _padding = 10;
  var _align = Alignment.topRight;
  double _height = 100;
  double _left = 0;
  Color _color = Colors.red;
  TextStyle _style = const TextStyle(color: Colors.black);
  Color _decorationColor = Colors.blue;
  double _opacity = 1;
  var duration = const Duration(milliseconds: 400);

  @override
  Widget build(BuildContext context) {
    // SingleChildScrollView 用于解决屏幕溢出问题
    return SingleChildScrollView(
      // Column 是一个将子部件沿屏幕垂直方向排列的小部件
      child: Column(
        children: <Widget>[
          buildElevatedButton(),
          buildAnimatedPositioned(),
          buildAnimatedAlign(),
          buildAnimatedContainer(),
          buildAnimatedDefaultTextStyle(),
          buildAnimatedOpacity(),
          buildAnimatedDecoratedBox1()
        // 将 List 中的每个元素映射（map）成一个新的 Widget，并将它们放到一个 List 中返回
        // 这里的作用是将 List 中的每个元素都添加一个 Padding，用于设置它们之间的间距
        ].map((e) {
          return Padding(
            padding: const EdgeInsets.symmetric(vertical: 16),
            child: e,
          );
        }).toList(),
      ),
    );
  }

  /// 1. AnimatedPadding，用于在给定的一段时间内，逐渐改变其子部件的 Padding 值，从而实现 Padding 动画
  /// 即在动画过程中，子部件的 Padding 值会从一个值平滑过渡到另一个值
  Widget buildElevatedButton(){
    return ElevatedButton(
      onPressed: () {
        setState(() {
          _padding = 20;
        });
      },
      child: AnimatedPadding(
        duration: duration,
        padding: EdgeInsets.all(_padding),
        child: const Text("AnimatedPadding"),
      ),
    );
  }

  /// 2. AnimatedPositioned，用于在给定的一段时间内，逐渐改变其子部件的位置，从而实现位置动画
  /// 即在动画过程中，子部件会从一个位置平滑过渡到另一个位置
  Widget buildAnimatedPositioned(){
    return SizedBox(
      height: 50,
      child: Stack(
        children: <Widget>[
          AnimatedPositioned(
            duration: duration,
            left: _left,
            child: ElevatedButton(
              onPressed: () {
                setState(() {
                  _left = 100;
                });
              },
              child: const Text("AnimatedPositioned"),
            ),
          )
        ],
      ),
    );
  }

  /// 3. AnimatedAlign，用于在给定的一段时间内，逐渐改变其子部件的对齐方式，从而实现对齐动画
  /// 即在动画过程中，子部件会从一种对齐方式平滑过渡到另一种对齐方式
  Widget buildAnimatedAlign(){
    return Container(
      height: 100,
      color: Colors.grey,
      child: AnimatedAlign(
        duration: duration,
        alignment: _align,
        child: ElevatedButton(
          onPressed: () {
            setState(() {
              _align = Alignment.center;
            });
          },
          child: const Text("AnimatedAlign"),
        ),
      ),
    );
  }

  /// 4. AnimatedContainer，用于在给定的一段时间内，逐渐改变其子部件的样式，从而实现 Container 动画
  /// 即在动画过程中，子部件会从一种样式平滑过渡到另一种样式
  Widget buildAnimatedContainer(){
    return AnimatedContainer(
      duration: duration,
      height: _height,
      color: _color,
      child: TextButton(
        onPressed: () {
          setState(() {
            _height = 150;
            _color = Colors.blue;
          });
        },
        child: const Text(
          "AnimatedContainer",
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }

  /// 5. AnimatedDefaultTextStyle，用于在给定的一段时间内，逐渐改变其子部件的文本样式，从而实现文本样式动画
  /// 即在动画过程中，子部件的文本样式会从一种样式平滑过渡到另一种样式
  Widget buildAnimatedDefaultTextStyle(){
    return AnimatedDefaultTextStyle(
      child: GestureDetector(
        child: const Text("hello world"),
        onTap: () {
          setState(() {
            _style = const TextStyle(
              color: Colors.blue,
              decorationStyle: TextDecorationStyle.solid,
              decorationColor: Colors.blue,
            );
          });
        },
      ),
      style: _style,
      duration: duration,
    );
  }

  /// 6. AnimatedOpacity，用于在给定的一段时间内，逐渐改变其子部件的透明度，从而实现透明度动画
  /// 即在动画过程中，子部件的透明度会从一个值平滑过渡到另一个值
  Widget buildAnimatedOpacity(){
    return AnimatedOpacity(
      opacity: _opacity,
      duration: duration,
      child: TextButton(
        style: ButtonStyle(
            backgroundColor: MaterialStateProperty.all(Colors.blue)),
        onPressed: () {
          setState(() {
            _opacity = 0.2;
          });
        },
        child: const Text(
          "AnimatedOpacity",
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }

  /// 自定义的 AnimatedDecoratedBox1，用于在给定的一段时间内，逐渐改变其子部件的装饰样式，从而实现装饰样式动画
  /// 即在动画过程中，子部件的装饰样式会从一种样式平滑过渡到另一种样式
  Widget buildAnimatedDecoratedBox1(){
    return AnimatedDecoratedBox1(
      duration: Duration(
          milliseconds: _decorationColor == Colors.red ? 400 : 2000),
      decoration: BoxDecoration(color: _decorationColor),
      child: Builder(builder: (context) {
        return TextButton(
          onPressed: () {
            setState(() {
              _decorationColor = _decorationColor == Colors.blue
                  ? Colors.red
                  : Colors.blue;
            });
          },
          child: const Text(
            "AnimatedDecoratedBox toggle",
            style: TextStyle(color: Colors.white),
          ),
        );
      }),
    );
  }

}
```

3. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画43.gif)

# 十一、自定义组件

## 1、自定义组件方法简介

### ①、组合多个 Widget

1. 这种方式是通过拼装多个组件来组合成一个新的组件。
2. 例如我们之前介绍的 `Container` 就是一个组合组件，它是由 `DecoratedBox`、`ConstrainedBox`、`Transform`、`Padding`、`Align` 等组件组成。
3. 在 Flutter 中，组合的思想非常重要，Flutter 提供了非常多的基础组件，而我们的界面开发其实就是按照需要组合这些组件来实现各种不同的布局而已。

### ②、通过 CustomPaint 自绘

1. 如果遇到无法通过现有的组件来实现需要的 UI 时，我们可以通过自绘组件的方式来实现，例如我们需要一个颜色渐变的圆形进度条，而 Flutter 提供的 `CircularProgressIndicator` 并不支持在显示精确进度时对进度条应用渐变色（其 `valueColor` 属性只支持执行旋转动画时变化 `Indicator` 的颜色）
2. 这时最好的方法就是通过自定义组件来绘制出我们期望的外观。
3. 我们可以通过 Flutter 中提供的 `CustomPaint` 和 `Canvas` 来实现 UI 自绘。

### ③、通过 RenderObject 自绘

1. Flutter 提供的自身具有 UI 外观的组件，如文本 `Text`、`Image` 都是通过相应的 `RenderObject`（我们将在“Flutter核心原理”一章中详细介绍  `RenderObject`）渲染出来的
2. 如 `Text` 是由 `RenderParagraph` 渲染；而 `Image` 是由 `RenderImage` 渲染。
3. RenderObject 是一个抽象类，它定义了一个抽象方法 `paint(...)`：

```dart
void paint(PaintingContext context, Offset offset)
```

4. `PaintingContext` 代表组件的绘制上下文，通过 `PaintingContext.canvas` 可以获得 Canvas，而绘制逻辑主要是通过 Canvas API 来实现。
5. 子类需要重写此方法以实现自身的绘制逻辑，如 `RenderParagraph` 需要实现文本绘制逻辑，而 `RenderImage` 需要实现图片绘制逻辑。
6. 可以发现，`RenderObject` 中最终也是通过 Canvas API 来绘制的，那么通过实现 `RenderObject` 的方式和上面介绍的通过 `CustomPaint` 和 `Canvas` 自绘的方式有什么区别？
7. 其实答案很简单，`CustomPaint` 只是为了方便开发者封装的一个代理类，它直接继承自 `SingleChildRenderObjectWidget`，通过 `RenderCustomPaint` 的 `paint` 方法将 `Canvas` 和画笔 `Painter` (需要开发者实现，后面章节介绍)连接起来实现了最终的绘制（绘制逻辑在 `Painter` 中）

## 2、组合现有组件

### ①、自定义渐变按钮 GradientButton

1. Flutter Material 组件库中的按钮默认不支持渐变背景，为了实现渐变背景按钮，我们自定义一个 `GradientButton` 组件，它需要支持一下功能：
	1. 背景支持渐变色
	2. 手指按下时有涟漪效果
	3. 可以支持圆角
2. 我们知道 `DecoratedBox` 可以支持背景色渐变和圆角，`InkWell` 在手指按下有涟漪效果，所以我们可以通过组合 `DecoratedBox` 和 `InkWell` 来实现 `GradientButton`，代码如下：

```dart
import 'package:flutter/material.dart';

class GradientButton extends StatelessWidget {
  const GradientButton({
    Key? key,
    this.colors,
    this.width,
    this.height,
    this.onPressed,
    this.borderRadius,
    required this.child,
  }) : super(key: key);

  // 渐变色数组
  final List<Color>? colors;

  // 按钮宽高、圆角
  final double? width;
  final double? height;
  final BorderRadius? borderRadius;

  // 点击回调
  final GestureTapCallback? onPressed;

  final Widget child;

  @override
  Widget build(BuildContext context) {
    // 获取主题
    ThemeData theme = Theme.of(context);

    // 确保 colors 数组不空
    List<Color> _colors = colors ?? [theme.primaryColor, theme.primaryColorDark];

    // DecoratedBox 小部件可以在其子部件绘制之前或之后绘制一个装饰（Decoration）。
    return DecoratedBox(
      /**
       * decoration 属性用于设置装饰，它接受一个 Decoration 对象，Decoration 是一个抽象类，它定义了一些装饰相关的接口，如：
       * BoxDecoration、UnderlineTabIndicator、FlutterLogoDecoration 等。
       * BoxDecoration 是 Flutter 提供的一个装饰类，它可以在 child 绘制前后绘制 BoxDecoration 中定义的装饰。
       */
      decoration: BoxDecoration(
        // gradient 属性用于设置渐变色，它需要传入一个 colors 数组
        gradient: LinearGradient(colors: _colors),
        // borderRadius 属性用于设置圆角
        borderRadius: borderRadius,
      ),
      // Material 是一个 UI 小部件，它在屏幕上显示一个矩形区域，用于显示当前的“纸墨”风格。
      child: Material(
        // MaterialType.transparency 表示 Material 的背景透明
        type: MaterialType.transparency,
        // 构建 InkWell 点击水波纹效果
        child: buildInkWell(_colors),
      ),
    );
  }
  
  /// 构建 InkWell 点击水波纹效果
  Widget buildInkWell(List<Color> _colors){
    // InkWell 是一个 Material 小部件，它可以在用户点击时产生“水波纹”效果。
    return InkWell(
      // splashColor 属性用于设置水波纹的颜色，即点击时水波纹扩散的颜色，此处设置为 colors 的最后一个颜色。
      splashColor: _colors.last,
      // highlightColor 属性用于设置高亮颜色，即水波纹结束后的颜色，此处设置为透明。
      highlightColor: Colors.transparent,
      // borderRadius 属性用于设置圆角，和 BoxDecoration 中的 borderRadius 属性意义相同。
      borderRadius: borderRadius,
      // onTap 属性用于设置点击回调，它接受一个 GestureTapCallback 类型的对象。
      onTap: onPressed,
      // 构建文本及其约束
      child: buildConstrainedBoxText(),
    );
  }

  /// 构建文本及其约束
  Widget buildConstrainedBoxText(){
    // ConstrainedBox 用于对子部件添加额外的约束。
    return ConstrainedBox(
      // BoxConstraints.tightFor 用于创建一个给定大小的约束
      constraints: BoxConstraints.tightFor(height: height, width: width),
      // Center 用于将其子部件在父部件中居中显示。
      child: Center(
        // Padding 用于给其子部件添加填充。
        child: Padding(
          // EdgeInsets.all 用于创建一个所有方向均使用相同数值的 EdgeInsets 对象。
          padding: const EdgeInsets.all(8.0),
          // DefaultTextStyle 用于设置文本默认样式。
          child: DefaultTextStyle(
            // style 属性用于设置文本样式，它接受一个 TextStyle 对象。
            style: const TextStyle(fontWeight: FontWeight.bold),
            child: child,
          ),
        ),
      ),
    );
  }
}
```

### ②、使用 GradientButton

1. `02_GradientButtonComponent.dart` 使用 `GradientButton` 组件

```dart
import 'package:flutter/material.dart';

import '01_GradientButton.dart';

class GradientButtonRoute extends StatefulWidget {
  const GradientButtonRoute({Key? key}) : super(key: key);

  @override
  _GradientButtonRouteState createState() => _GradientButtonRouteState();
}

class _GradientButtonRouteState extends State<GradientButtonRoute> {
  @override
  Widget build(BuildContext context) {
    // Column 是一个将其子部件以垂直线性顺序排列的小部件。
    return Column(
      // 该属性表示子部件在主轴（水平方向）的对齐方式
      mainAxisSize: MainAxisSize.min,
      children: <Widget>[
        // 双色渐变
        GradientButton(
          colors: const [Colors.orange, Colors.red],
          height: 50.0,
          onPressed: onTap,
          child: const Text("Submit"),
        ),
        // 多色渐变
        GradientButton(
          height: 50.0,
          colors: const [Colors.white, Colors.red, Colors.orange, Colors.amber, Colors.green, Colors.blue, Colors.deepPurple, Colors.black],
          onPressed: onTap,
          child: const Text("Submit"),
        ),
        // 自定义圆角
        GradientButton(
          height: 50.0,
          borderRadius: const BorderRadius.all(Radius.circular(50)),
          colors: [Colors.lightBlue.shade300, Colors.blueAccent],
          onPressed: onTap,
          child: const Text("Submit"),
        ),
      ],
    );
  }

  onTap() {
    print("button click");
  }

}
```

2. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画44.gif)

## 3、组合实例旋转动画：TurnBox

1. 我们之前已经介绍过 `RotatedBox`，它可以旋转子组件，但是它有两个缺点：
	1. 一是只能将其子节点以 90 度的倍数旋转；
	2. 二是当旋转的角度发生变化时，旋转角度更新过程没有动画。
2. 本节我们将实现一个 TurnBox 组件，它不仅可以以任意角度来旋转其子节点，而且可以在角度发生变化时执行一个动画以过渡到新状态，同时，我们可以手动指定动画速度。
3. 实例：

```dart
import 'package:flutter/widgets.dart';

class TurnBox extends StatefulWidget {
  const TurnBox({
    Key? key,
    // 旋转的“圈”数,一圈为 360 度，如 0.25 圈即 90 度
    this.turns = .0,
    // 过渡动画执行的总时长
    this.speed = 200,
    required this.child
  }) :super(key: key);

  final double turns;
  final int speed;
  final Widget child;

  @override
  _TurnBoxState createState() => _TurnBoxState();
}

class _TurnBoxState extends State<TurnBox> with SingleTickerProviderStateMixin {
  // _controller 用于控制动画
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    // 创建 AnimationController 对象
    _controller = AnimationController(
        vsync: this,
        // lowerBound 和 upperBound 用于指定动画的边界，默认值是 0.0 和 1.0；
        // 此处我们将其设置为无限小和无限大，这样可以让动画执行的“圈”数任意大
        lowerBound: -double.infinity,
        upperBound: double.infinity
    );
    // 通过 AnimationController 的 value 属性来指定动画的值
    _controller.value = widget.turns;
  }

  @override
  void dispose() {
    // 释放动画资源
    super.dispose();
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // RotationTransition 是一个可以旋转子部件的小部件
    return RotationTransition(
      // 将 _animation 作为 RotationTransition 的 turns 属性
      turns: _controller,
      child: widget.child,
    );
  }

  /// 当 widget 的配置发生变化时，didUpdateWidget() 会被调用。
  @override
  void didUpdateWidget(TurnBox oldWidget) {
    super.didUpdateWidget(oldWidget);
    // 旋转角度 turns 发生变化时执行过渡动画
    if (oldWidget.turns != widget.turns) {
      _controller.animateTo(
        // 动画的目标值
        widget.turns,
        // duration 属性用于设置动画执行的时长
        duration: Duration(milliseconds: widget.speed),
        // 动画的曲线
        curve: Curves.easeOut,
      );
    }
  }
}
```

4. 创建测试类 `TurnBoxRoute` 使用 `TurnBox` 

```dart
import 'package:flutter/material.dart';

import '01_TurnBox.dart';

class TurnBoxRoute extends StatefulWidget {
  const TurnBoxRoute({Key? key}) : super(key: key);

  @override
  _TurnBoxRouteState createState() => _TurnBoxRouteState();
}

class _TurnBoxRouteState extends State<TurnBoxRoute> {
  double _turns = .0;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          TurnBox(
            turns: _turns,
            speed: 500,
            child: const Icon(
              Icons.refresh,
              size: 50,
            ),
          ),
          TurnBox(
            turns: _turns,
            speed: 1000,
            child: const Icon(
              Icons.refresh,
              size: 150.0,
            ),
          ),
          ElevatedButton(
            child: const Text("顺时针旋转1/5圈"),
            onPressed: () {
              setState(() {
                _turns += .2;
              });
            },
          ),
          ElevatedButton(
            child: const Text("逆时针旋转1/5圈"),
            onPressed: () {
              setState(() {
                _turns -= .2;
              });
            },
          )
        ],
      ),
    );
  }
}
```

5. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画46.gif)

### ③、

### ④、

### ⑤、

### ⑥、

## 4、

## 5、

## 6、

## 7、

## 8、

## 9、


# 十二、Flutter 扩展

## 1、包和插件

### ①、包

1. 第二章中已经讲过如何使用包（Package），我们知道通过包可以复用模块化代码，一个最小的 Package 包括：
	1. 一个 `pubspec.yaml` 文件：声明了 Package 的名称、版本、作者等的元数据文件。
	2. 一个 lib 文件夹：包括包中公开的(public)代码，最少应有一个 `<package-name>.dart` 文件
2. Flutter 包分为两类：
	1. Dart 包：其中一些可能包含 Flutter 的特定功能，因此对 Flutter 框架具有依赖性，这种包仅用于 Flutter，例如 fluro (opens new window)包。
	2. 插件包：一种专用的 Dart 包，其中包含用 Dart 代码编写的 API，以及针对 Android（使用 Java 或 Kotlin）和针对 iOS（使用 OC 或 Swift）平台的特定实现，也就是说插件包括原生代码，一个具体的例子是 battery (opens new window) 插件包

### ②、插件

1. Flutter 本质上只是一个 UI 框架，运行在宿主平台之上，Flutter 本身是无法提供一些系统能力，比如使用蓝牙、相机、GPS 等，因此要在 Flutter 中调用这些能力就必须和原生平台进行通信。
2. 目前 Flutter 已经支持 iOS、Android、Web、macOS、Windows、Linux 等众多平台，要调用特定平台 API 就需要写插件。插件是一种特殊的包，和纯 dart 包主要区别是插件中除了dart 代码，还包括特定平台的代码，比如 `image_picker` 插件可以在 iOS 和 Android 设备上访问相册和摄像头

#### Ⅰ、插件实现原理

1. 我们知道一个完整的 Flutter 应用程序实际上包括原生代码和 Flutter 代码两部分。Flutter 中提供了平台通道（platform channel）用于 Flutter和原生平台的通信，平台通道正是 Flutter 和原生之间通信的桥梁，它也是 Flutter 插件的底层基础设施。
2. Flutter 与原生之间的通信本质上是一个远程调用（RPC），通过消息传递实现：
	1. 应用的 Flutter 部分通过平台通道（platform channel）将调用消息发送到宿主应用。
	2. 宿主监听平台通道，并接收该消息。然后它会调用该平台的 API，并将响应发送回 Flutter。
3. 由于插件编写涉及具体平台的开发知识，比如 `image_picker` 插件需要开发者在 iOS 和 Android 平台上分别实现图片选取和拍摄的功能，因此需要开发者熟悉原生开发，而此处主要聚焦 Flutter ，因此不做过多介绍
4. 不过插件的开发也并不复杂，感兴趣可以查看官方的：[插件开发示例](https://flutter.cn/docs/development/packages-and-plugins/developing-packages)

#### Ⅱ、如何获取平台信息

1. 有时，在 Flutter 中我们想根据宿主平台添加一些差异化的功能，因此 Flutter 中提供了一个全局变量 `defaultTargetPlatform` 来获取当前应用的平台信息，`defaultTargetPlatform` 定义在 `platform.dart` 中，它的类型是 `TargetPlatform`，这是一个枚举类，定义如下：

```dart
enum TargetPlatform {
  android,
  fuchsia,
  iOS,
  ...
}
```

2. 可以看到目前 Flutter 只支持这三个平台。我们可以通过如下代码判断平台：

```dart
if(defaultTargetPlatform == TargetPlatform.android){
  // 是安卓系统，do something
  ...
}
```

3. 由于不同平台有它们各自的交互规范，Flutter Material 库中的一些组件都针对相应的平台做了一些适配，比如路由组件 MaterialPageRoute，它在 android 和 ios 中会应用各自平台规范的切换动画。那如果我们想让我们的 APP 在所有平台都表现一致，比如希望在所有平台路由切换动画都按照 ios 台一致的左右滑动切换风格该怎么做？Flutter 中提供了一种覆盖默认平台的机制，我们可以通过显式指定 `debugDefaultTargetPlatformOverride` 全局变量的值来指定应用平台。比如：

```dart
debugDefaultTargetPlatformOverride=TargetPlatform.iOS;
print(defaultTargetPlatform); // 会输出TargetPlatform.iOS
```

4. 上面代码即使在 Android 中运行后，Flutter APP 也会认为是当前系统是 iOS，Material 组件库中所有组件交互方式都会和 iOS 平台对齐， `defaultTargetPlatform` 的值也会变为 `TargetPlatform.iOS`

#### Ⅲ、常用的插件

1. Flutter 官方提供了一系列常用的插件，如访问相机/相册、本地存储、播放视频等，完整列表见：https://github.com/flutter/plugins/tree/master/packages 
2. 除了官方维护的插件，Flutter 社区也有不少现成插件，具体可以在 https://pub.dev/ 上查找。

## 2、Flutter Web

### ①、简介

1. Flutter 目前已经支持 macOS、Windows、Linux、Android、iOS、Web 等多个平台
2. 这些平台中除了 Web 平台会比较特殊一些，因为除了它其余的“平台”都是操作系统，而 Web 并不是操作系统，Web 应用程序是运行在浏览器中的，而浏览器是运行在操作系统之上，因此 “平台”一词，指的是某种“运行环境”，并不等同于“操作系统”，浏览器和操作系统都是应用程序运行的环境而已。
3. 传统的 Web 应用都是基于 Javascript + html + css 开发的，运行在浏览器之上，因此天然具备跨平台优势，而 Flutter 的目标是高性能的跨端 UI 框架，所以支持 Web 平台将有助于 Flutter 技术扩大应用场景，实现 write once, run anywhere（一次编码，到处运行）。
4. 为此，Flutter 团队从 1.0 开始一直在尝试让 Flutter 支持 Web 平台，第一个支持 Web 平台的稳定版是 2.0 ，在 2.0 之后 Flutter 对 Web 平台的支持也一直在优化，现在也有一些公司将 Flutter 应用应用到生产环境

### ②、Web 应用的特殊性

1. 因为 Web 应用是在浏览器中运行的，而浏览器是运行在操作系统之上，因此 Web 应用不能直接调用操作系统 API， Web 应用能调用哪些操作系统能力取决于它的宿主-浏览器是否暴露相关的操作系统 API。而浏览器出于安全考虑，会提供一个沙箱环境——开放一些安全、可控的系统能力，同时限制一部分敏感的操作，具体表现在：
	1. 浏览器允许 Web 应用访问网络，但有严格的“同源策略”限制。
	2. 浏览器允许 JavaScript 读取用户手动选择本地文件（文件上传场景），但不允许 JavaScript 主动访问本地文件系统，同时在任何情况下，浏览器都不允许 JavaScript 直接往本地文件系统写文件，因此 `dart:io` 包在 Web 应用是不能用的。
	3. 浏览器对 Web 应用访问系统硬件权限有自身策略，比如访问 wifi、gps、摄像头等。
2. 因此，如果用 Flutter 开发 Web 应用，以上这些限制将会生效，所以会出现和其他平台不一致的情况，常见的两个场景是：不能在 Web 应用中发起非同源请求、不能在 Web 应用中直接读取文件。

### ③、Web 渲染器

- Flutter 中提供了两种不同的渲染器来运行和构建 Web 应用，分别是 html 渲染器和 CanvasKit 渲染器。

#### Ⅰ、Html 渲染器

1. 由于浏览器有一套自身的布局标准（ html + css ），Flutter 在生成 Web 应用时可以编译为符合浏览器标准的文件，包括使用 HTML，CSS，Canvas 和 SVG 元素来渲染。
2. 使用 Html 渲染器的优点是应用体积相对较小，缺点是使用 Html 渲染器时大多数 UI 并不是 Flutter 引擎绘制的，所以可能会存在跨浏览器跨时 UI 出现不一致的情况

#### Ⅱ、CanvasKit 渲染器

1. 我们知道 Flutter 的优势是提供一套自绘的 UI 框架，可以保证多端 UI 的一致性。
2. Flutter 在支持其他平台时，都是将引擎的 C++ 代码编译为相应平台的代码来实现移植的（运行在操作系统之上）。
3. 但是在 Web 平台，Web 应用是运行在浏览器之上，而现代浏览器都实现了对 WebAssembly 的支持，简单来讲，在之前 W3C 规范中只要求浏览器能够支持 JavaScript 语言，这样的话很多其他语言的代码想在浏览器中运行就必须改写为 JavaScript，而 WebAssembly 是一种标准的、可移植的二进制文件格式规范，文件扩展名为 `.wasm`，现在浏览器都支持 WebAssembly ，这也就意味着其他语言按照 WebAssembly 规范编译的应用可以在浏览器中运行！
4. 因此，Flutter 将引擎编译成 WebAssembly 格式，并使用 WebGL 渲染，这种渲染方式的渲染器官方称为 CanvasKit 渲染器。
5. CanvasKit 渲染器的优点是可以保证跨端 UI 绘制的一致性，有更好的性能，以及降低不同浏览器渲染效果不一致的风险。但缺点是应用的大小会增加大约 2MB

### ④、在浏览器中运行

1. `--web-renderer` 可选参数值为 `auto`、`html` 或 `canvaskit`。
	1. `auto`（默认）：自动选择渲染器。移动端浏览器选择 HTML，桌面端浏览器选择 CanvasKit。
	2. `html` ：强制使用 HTML 渲染器。
	3. `canvaskit`：强制使用 CanvasKit 渲染器。
2. 此选项适用于 `run` 和 `build` 命令。例如：

```dart
flutter run -d chrome --web-renderer html
flutter build web --web-renderer canvaskit
```

3. 如果运行/构建目标是非浏览器设备（即移动设备或桌面设备），这个选项会被忽略

### ⑤、Flutter Web 使用场景

1. Web 开发已有完整且强大的开发及生态体系，Flutter Web 并不适用 Web 开发的所有场景，目前 Flutter Web 主要关注以下三个应用场景：
	1. 渐进式 Web 应用 (Progressive web apps, PWA)。
	2. 单页应用 (Single page apps, SPA)， 一般一个应用只有一个 html 文件，只需一次加载，后续与服务端动态互传数据。
	3. 将现有 Flutter 移动应用拓展到 Web，在两个平台共享代码。
2. 注意：PWA 和 SPA 应用在 Web 开发中是两种基本的应用类型，Web 开发者会比较熟悉。
3. 现在阶段，Flutter 对于富文本和瀑布流类型的 Web 页面并不是很适合，例如博客，它是典型的“以文档为中心”的模式，而不是像 Flutter 这样的 UI 框架可以提供的“以应用为中心”的服务。以文档为中心的应用通常各个页面之间相互独立，很少有关联，也就不需要跨页面的状态共享，而以应用为中心的服务，通常各个页面之间是有状态关联，不同页面组成一个完整的功能。
4. 最后，有关如何在 Web 上使用 Flutter 的更多信息请参考：[Flutter 官方文档](https://flutter.cn/docs/web)

# 十三、国际化

## 1、让 App 支持多语言

### ①、简介

1. 如果我们的应用要支持多种语言，那么我们需要“国际化”它。这意味着我们在开发时需要为应用程序支持的每种语言环境设置“本地化”的一些值，如文本和布局。
2. Flutter SDK 已经提供了一些组件和类来帮助我们实现国际化，下面我们来介绍一下 Flutter 中实现国际化的步骤。
3. 接下来我们以 `MaterialApp` 类为入口的应用来说明如何支持国际化。
4. 大多数应用程序都是通过 `MaterialApp` 为入口，但根据低级别的 `WidgetsApp` 类为入口编写的应用程序也可以使用相同的类和逻辑进行国际化。`MaterialApp` 实际上也是 `WidgetsApp` 的一个包装。
5. 注意，“本地化的值和资源”是指我们针对不同语言准备的不同资源，这些资源一般是指文案（字符串），当然也会有一些其他的资源会根据不同语言地区而不同，比如我们需要显示一个 APP 上架地的国旗图片，那么不同 Locale 区域我们就需要提供不同的国旗图片

### ②、使用 Intl 包支持国际化

1. 默认情况下，Flutter SDK 中的组件仅提供美国英语本地化资源（主要是文本）。要添加对其他语言的支持，应用程序须添加 `flutter_localizations` 和 `intl` 包依赖，然后还需要在 `MaterialApp` 中进行一些配置。 要使用 `flutter_localizations` 包，首先需要添加依赖到 `pubspec.yaml` 文件中：

```dart
dependencies:
  flutter:
    sdk: flutter
  # flutter_localizations 包含本地化资源，例如字符串和其他值，以便为特定于地区的用户界面提供本地化
  flutter_localizations:
    sdk: flutter

  # intl 是一个 Dart 包，它提供了国际化和本地化的实现，包括消息和日期/时间本地化，以及双向文本翻译
  intl: ^0.17.0
```

2. 在 `lib` 目录下创建一个 `l10n` 目录，并在其中创建语言文件 `intl_zh.arb` 和 `intl_en.arb` ，并分别在其中写入以下内容：

```arb
{
  "greeting": "你好，世界",
  "welcome": "欢迎"
}
```

```arb
{
  "greeting": "Hello World",
  "welcome": "welcome"
}
```

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214135012.png)

3. 执行命令：`flutter pub global run intl_utils:generate`，使得 `intl` 包根据上面的语言文件生成代码：
	1. `intl` 目录：这个目录包含了 Dart 代码文件，用于处理应用程序的国际化（Internationalization），其中的文件包括：
		1. `messages_all.dart`：这个文件包含了用于加载本地化消息的 `initializeMessages` 函数，以及 `Messages` 类的导出。
		2. `messages_en.dart`：这个文件包含了英语（English）本地化消息的定义和静态方法。
		3. `messages_zh.dart`：这个文件包含了中文（Chinese）本地化消息的定义和静态方法。
	2. `l10n.dart` 文件：这个文件是一个便捷的导出文件，用于导出 `messages_all.dart` 中的 `initializeMessages` 函数和 `Messages` 类，以便在应用程序中使用

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214135903.png)

4. 修改主启动类 `main.dart` 文件中的 `MaterialApp` 组件，添加 `localizationsDelegates` 和 `supportedLocales` 属性：
	1. 与 `MaterialApp` 类为入口的应用不同，对基于 `WidgetsApp` 类为入口的应用程序进行国际化时，不需要 `GlobalMaterialLocalizations.delegate`
	2. `localizationsDelegates` 列表中的元素是生成本地化值集合的工厂类。
		1. `GlobalMaterialLocalizations.delegate` 为 Material 组件库提供的本地化的字符串和其他值，它可以使 Material 组件支持多语言。
		2. `GlobalWidgetsLocalizations.delegate` 定义组件默认的文本方向，从左到右或从右到左，这是因为有些语言的阅读习惯并不是从左到右，比如如阿拉伯语就是从右向左的。
	3. `supportedLocales` 也接收一个 Locale 数组，表示我们的应用支持的语言列表，在本例中我们的应用只支持美国英语和中文简体两种语言

```dart
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import '13_国际化/01_让 App 支持多语言/01_LocalizationsComponent.dart';
import 'generated/l10n.dart';


// 入口方法
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    /**
     * MaterialApp 是 Flutter 提供的一个小部件，用于创建一个包含 Material Design 样式和功能的应用程序。
     * 它是一个顶层小部件，用于为整个应用程序提供一致的主题和样式。
     * 在 MaterialApp 中，你可以设置应用程序的标题、主题、路由和其他全局属性
     */
    return MaterialApp(
      /**
       * localizationsDelegates 是 MaterialApp 的一个属性，用于指定应用程序支持的本地化代理。
       * 它接受一个 List<LocalizationsDelegate> 类型的参数
       * S.delegate：S 是一个自动生成的类，它包含了应用程序中所有的本地化资源，如字符串、图片等。
       * GlobalMaterialLocalizations.delegate：Material 组件库的本地化代理
       * GlobalWidgetsLocalizations.delegate：定义小部件默认的文本方向，从左到右或从右到左
       */
      localizationsDelegates: const [
        S.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      /**
       * supportedLocales 是 MaterialApp 的一个属性，用于指定应用程序支持的语言列表。
       */
      supportedLocales: S.delegate.supportedLocales,
      /**
       * home 是 MaterialApp 的一个属性，用于指定应用程序的主页。它接受一个 Widget 作为参数，用于定义主页的内容
       * Scaffold 是一个用于创建基本页面布局的小部件。
       * Scaffold 小部件提供了一个应用程序的基本布局结构，包括顶部的应用栏、底部的导航栏、抽屉菜单等。
       * 它是一个非常常用的小部件，常用于创建具有标准 Material Design 布局的页面
       */
      home: const Scaffold(
        // 设置背景颜色为白色
        backgroundColor: Colors.white,
        /**
         * body: 用于定义页面的主要内容区域
         * SafeArea 是一个小部件，作用是为其子部件提供一个安全的区域，来避免遮挡了屏幕的物理部件（如刘海屏或下方的 Home 键）
         */
        body: SafeArea(
          child: LocalizationsComponent()
        )
      ),
    );
  }
}
```

5. 创建 `01_LocalizationsComponent.dart` 类进行测试：

```dart
import 'package:flutter/material.dart';

import '../../generated/l10n.dart';

class LocalizationsComponent extends StatelessWidget {
  const LocalizationsComponent({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        // 垂直居中
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(S.current.greeting, style: const TextStyle(fontSize: 30)),
          ElevatedButton(
            onPressed: () {},
            child: Text(S.current.welcome, style: const TextStyle(fontSize: 30)),
          ),
        ],
      ),
    );
  }
}
```

6. 效果：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2F动画47.gif)

### ③、获取当前区域 Locale

1. `Locale` 类是用来标识用户的语言环境的，它包括语言和国家两个标志如：

```dart
const Locale('zh', 'CN') // 中文简体
```

2. 我们始终可以通过以下方式来获取应用的当前区域 `Locale`：

```dart
Locale myLocale = Localizations.localeOf(context);
```

3. `Localizations` 组件一般位于 widget 树中其他业务组件的顶部，它的作用是定义区域 `Locale` 以及设置子树依赖的本地化资源。 
4. 如果系统的语言环境发生变化，则会使用对应语言的本地化资源

### ④、监听系统语言切换

1. 当我们更改系统语言设置时，APP 中的 `Localizations` 组件会重新构建，`Localizations.localeOf(context)` 获取的 Locale 就会更新，最终界面会重新 build 达到切换语言的效果。
2. 但是这个过程是隐式完成的，我们并没有主动去监听系统语言切换，但是有时我们需要在系统语言发生改变时做一些事，比如系统语言切换为一种我们 APP 不支持的语言时，我们需要设置一个默认的语言，这时我们就需要监听 locale 改变事件。
3. 我们可以通过 `localeResolutionCallback` 或 `localeListResolutionCallback` 回调来监听 locale 改变的事件，我们先看看 `localeResolutionCallback` 的回调函数签名：

```dart
Locale Function(Locale locale, Iterable<Locale> supportedLocales)
```

4. 参数 1 `locale` 的值为当前的当前的系统语言设置，当应用启动时或用户动态改变系统语言设置时此 `locale` 即为系统的当前 `locale`。当开发者手动指定 APP 的 `locale` 时，那么此 `locale` 参数代表开发者指定的 `locale`，此时将忽略系统 `locale` 如：

```dart
MaterialApp(
 ...
 locale: const Locale('en', 'US'), //手动指定locale
 ...
)
```

5. 上面的例子中手动指定了应用 `locale` 为美国英语，指定后即使设备当前语言是中文简体，应用中的 `locale` 也依然是美国英语。如果 `locale` 为 `null`，则表示 Flutter 未能获取到设备的 Locale 信息，所以我们在使用 `locale` 之前一定要先判空。
6. 参数 2 `supportedLocales` 为当前应用支持的 `locale` 列表，是开发者在 `MaterialApp` 中通过 `supportedLocales` 属性注册的。
7. 返回值是一个 `Locale`，此 Locale 为 Flutter APP 最终使用的 Locale。通常在不支持的语言区域时返回一个默认的 Locale。
8. `localeListResolutionCallback` 和 `localeResolutionCallback` 唯一的不同就在第一个参数类型，前者接收的是一个 Locale 列表，而后者接收的是单个 Locale。

```dart
Locale Function(List<Locale> locales, Iterable<Locale> supportedLocales)
```

9. 在较新的 Android 系统中，用户可以设置一个语言列表，这样一来，支持多语言的应用就会得到这个列表，应用通常的处理方式就是按照列表的顺序依次尝试加载相应的 Locale，如果某一种语言加载成功则会停止。下图是 Android 系统中设置语言列表的截图

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214152525.png)

10. 在 Flutter 中，应该优先使用 `localeListResolutionCallback`，当然你不必担心 Android 系统的差异性，如果在低版本的 Android 系统中， Flutter 会自动处理这种情况，这时 Locale 列表只会包含一项

### ⑤、Localization 组件

1. `Localizations` 组件用于加载和查找应用当前语言下的本地化值或资源。应用程序通过 `Localizations.of(context,type)`  来引用这些对象。 如果设备的 Locale 区域设置发生更改，则 `Localizations` 组件会自动加载新区域的 `Locale` 值，然后重新 build 使用（依赖）了它们的组件
2. 之所以会这样，是因为 `Localizations` 内部使用了 `InheritedWidget` ，我们在介绍该组件时讲过：当子组件的 build 函数引用了 `InheritedWidget` 时，会创建对 `InheritedWidget` 的隐式依赖关系。因此，当 `InheritedWidget` 发生更改时，即 `Localizations` 的 Locale 设置发生更改时，将重建所有依赖它的子组件。
3. 本地化值由 Localizations 的 LocalizationsDelegates 列表加载 。 每个委托必须定义一个异步 load() 方法，以生成封装了一系列本地化值的对象。通常这些对象为每个本地化值定义一个方法。
4. 在大型应用程序中，不同模块或 Package 可能会与自己的本地化值捆绑在一起。 这就是为什么要用 `Localizations` 管理对象表的原因。 要使用由 `LocalizationsDelegate` 的 `load` 方法之一产生的对象，可以指定一个 `BuildContext` 和对象的类型来找到它。
5. 例如，Material 组件库的本地化字符串由 `MaterialLocalizations` 类定义，此类的实例由 `MaterialApp` 类提供的 `LocalizationDelegate` 创建， 它们可以如下方式获取到：

```dart
Localizations.of<MaterialLocalizations>(context, MaterialLocalizations);
```

6. 这个特殊的 `Localizations.of()` 表达式会经常使用，所以 `MaterialLocalizations` 类提供了一个便捷方法：

```dart
static MaterialLocalizations of(BuildContext context) {
  return Localizations.of<MaterialLocalizations>(context, MaterialLocalizations);
}

// 可以直接调用便捷方法
tooltip: MaterialLocalizations.of(context).backButtonTooltip,
```

### ⑥、使用打包好的 LocalizationsDelegates

1. 为了尽可能小而且简单，flutter 软件包中仅提供美国英语值的 `MaterialLocalizations` 和 `WidgetsLocalizations` 接口的实现。 
2. 这些实现类分别称为 `DefaultMaterialLocalizations` 和 `DefaultWidgetsLocalizations`。
3. `flutter_localizations` 包包含 `GlobalMaterialLocalizations` 和 `GlobalWidgetsLocalizations` 的本地化接口的多语言实现， 国际化的应用程序必须按照本节开头说明的那样为这些类指定本地化的代理类。
4. 上述的 `GlobalMaterialLocalizations` 和 `GlobalWidgetsLocalizations` 只是 Material 组件库的本地化实现，如果我们要让自己的布局支持多语言，那么就需要实现在即的 Localizations。

## 2、国际化常见问题

### ①、默认语言区域不对

1. 在一些非大陆行货渠道买的一些 Android 和 iOS 设备，会出现默认的 Locale 不是中文简体的情况。
2. 这属于正常现象，但是为了防止设备获取的 Locale 与实际的地区不一致，所有的支持多语言的 APP 都必须提供一个手动选择语言的入口

### ②、如何对应用标题进行国际化

1. MaterialApp 有一个 t`i`tle 属性，用于指定 APP 的标题。在 Android 系统中，APP 的标题会出现在任务管理器中。所以也需要对 title 进行国际化。
2. 但是问题是很多国际化的配置都是在 MaterialApp 上设置的，我们无法在构建 MaterialApp 时通过 `Localizations.of` 来获取本地化资源，如：

```dart
MaterialApp(
  title: DemoLocalizations.of(context).title, //不能正常工作！
  localizationsDelegates: [
    // 本地化的代理类
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    DemoLocalizationsDelegate() // 设置Delegate
  ],
);
```

3. 上面代码运行后，`DemoLocalizations.of(context).title` 是会报错的，原因是 `Localizations.of` 会从当前的 context 沿着 widget 树向顶部查找 DemoLocalizations，但是我们在 MaterialApp 中设置完 `DemoLocalizationsDelegate` 后，实际上 `DemoLocalizations` 是在当前 context 的子树中的，所以 `DemoLocalizations.of(context)` 会返回 `null`，报错。
4. 那么我们该如何处理这种情况呢？其实很简单，我们只需要设置一个 `onGenerateTitle` 回调即可：

```dart
MaterialApp(
  onGenerateTitle: (context){
    // 此时 context 在 Localizations 的子树中
    return DemoLocalizations.of(context).title;
  },
  localizationsDelegates: [
    DemoLocalizationsDelegate(),
    ...
  ],
);
```


### ③、如何为英语系的国家指定同一个 locale

1. 英语系的国家非常多，如美国、英国、澳大利亚等，这些英语系国家虽然说的都是英语，但也会有一些区别。
2. 如果我们的 APP 只想提供一种英语（如美国英语）供所有英语系国家使用，我们可以在前面介绍的 `localeListResolutionCallback` 中来做兼容：

```dart
localeListResolutionCallback:
    (List<Locale> locales, Iterable<Locale> supportedLocales) {
  // 判断当前locale是否为英语系国家，如果是直接返回Locale('en', 'US')     
}
```

# 十四、Flutter 核心原理

## 1、Flutter UI 框架（Framework）

### ①、什么是 UI 框架

1. 在一开始，我们讲过 Flutter 从上到下分为框架层、引擎层和嵌入层三层。也说过开发者基本上都是与框架层打交道，本章将深入介绍一下 Flutter 框架层的原理，在此之前，我们先看看更广义的UI框架指的是什么？解决了什么问题？
2. 术语 `UI 框架（UI Framework）`特指：基于一个平台，在此平台上实现一个能快速开发 GUI（图形用户接口）的框架，这里的平台主要指操作系统和浏览器。通常来讲平台只提供非常基础的图形 API，比如画线、画几何图形等，在大多数平台中，这些基础的图形 API 通常会被封装在一个 Canvas 对象中来集中管理。可以想象一下，如果没有UI 框架的封装而直接用 Canvas 来构建用户界面将会是怎样的一个体验和效率！ 所以，简单来讲， UI 框架解决的主要问题就是：<font color="#ff0000">如何基于基础的图形API（Canvas）来封装一套可以高效创建UI的框架</font>。
3. 我们说过各个平台 UI 框架的实现原理基本是相通的，也就是说无论是 Android 还是 iOS，他们将一个用户界面展示到屏幕的流程是相似的，所以，在介绍 Flutter UI 框架之前，我们先看看平台图形处理的基本原理，这样可以对操作系统和系统底层 UI 逻辑有一个清晰的认识

### ②、硬件绘图基本原理

1. 提到原理，我们要从屏幕显示图像的基本原理谈起。我们知道显示器（屏幕）是由一个个物理显示单元组成，每一个单元我们可以称之为一个物理像素点，而每一个像素点可以发出多种颜色，显示器成相的原理就是在不同的物理像素点上显示不同的颜色，最终构成完整的图像。
2. 一个像素点能发出的所有颜色总数是显示器的一个重要指标，比如我们所说的 1600 万色的屏幕就是指一个像素点可以显示出 1600 万种颜色，而显示器颜色是有 RGB 三基色组成，所以 1600 万即 2 的 24 次方，即每个基本色（R、G、B）深度扩展至 8 bit(位)，颜色深度越深，所能显示的色彩更加丰富靓丽。
3. 为了更新显示画面，显示器是以固定的频率刷新（从 GPU 取数据），比如有一部手机屏幕的刷新频率是 60Hz。当一帧（frame）图像绘制完毕后准备绘制下一帧时，显示器会发出一个垂直同步信号（如vsync）， 60Hz 的屏幕就会一秒内发出 60 次这样的信号。而这个信号主要是用于同步 CPU、GPU 和显示器的。
4. 一般地来说，计算机系统中，CPU、GPU 和显示器以一种特定的方式协作：CPU 将计算好的显示内容提交给 GPU，GPU 渲染后放入帧缓冲区，然后视频控制器按照同步信号从帧缓冲区取帧数据传递给显示器显示。
5. CPU 和 GPU 的任务是各有偏重的，CPU 主要用于基本数学和逻辑计算，而 GPU 主要执行和图形处理相关的复杂的数学，如矩阵变化和几何计算，GPU 的主要作用就是确定最终输送给显示器的各个像素点的色值

### ③、操作系统绘制 API 的封装

1. 由于最终的图形计算和绘制都是由相应的硬件来完成，而直接操作硬件的指令通常都会有操作系统屏蔽，应用开发者通常不会直接面对硬件
2. 操作系统屏蔽了这些底层硬件操作后会提供一些封装后的 API 供操作系统之上的应用调用，但是对于应用开发者来说，直接调用这些操作系统提供的 API 是比较复杂和低效的，因为操作系统提供的 API 往往比较基础，直接调用需要了解 API 的很多细节。
3. 正是因为这个原因，几乎所有用于开发 GUI 程序的编程语言都会在操作系统之上再封装一层，将操作系统原生 API 封装在一个编程框架和模型中，然后定义一种简单的开发规则来开发 GUI 应用程序，而这一层抽象，正是我们所说的“UI框架”，如 Android SDK 正是封装了 Android 操作系统 API，提供了一个 `UI描述文件 XML + Java/Kotlin 操作 DOM` 的 UI 框架，而 iOS 的 UIKit 对 View 的抽象也是一样的，他们都将操作系统 API 抽象成一个基础对象（如用于 2D 图形绘制的 Canvas），然后再定义一套规则来描述 UI，如UI树结构，UI 操作的单线程原则等。

### ④、Flutter UI 框架

1. 我们可以看到，无论是 Android SDK 还是 iOS 的 UIKit 的职责都是相同的，它们只是语言载体和底层的系统不同而已。那么可不可以实现这么一个UI 框架：可以使用同一种编程语言开发，然后针对不同操作系统 API 抽象一个对上接口一致，对下适配不同操作系统的中间层，然后在打包编译时再使用相应的中间层代码？如果可以做到，那么我们就可以使用同一套代码编写跨平台的应用了。
2. 而 Flutter 的原理正是如此，它提供了一套 Dart API，然后在底层通过 OpenGL 这种跨平台的绘制库（内部会调用操作系统API）实现了一套代码跨多端。由于 Dart API 也是调用操作系统 API，所以它的性能接近原生。这里有两点需要注意：
3. 虽然 Dart 是先调用了 OpenGL，OpenGL 才会调用操作系统 API，但是这仍然是原生渲染，因为 OpenGL 只是操作系统 API 的一个封装库，它并不像 WebView 渲染那样需要 JavaScript 运行环境和 CSS 渲染器，所以不会有性能损失。
4. Flutter 早期版本底层会调用 OpenGL 这样的跨平台库，但在 iOS 设备上苹果提供了专门的图形库 Metal，使用 Metal 可以在 iOS 上获得比 OpenGL 更好的绘图性能，因此 Flutter 后来在 iOS 上会优先调用 Metal ，只有当 Metal 不可用时才会降级到 OpenGL。不过 Flutter 底层到底是调用的哪个库，作为应用开发者是不需要关注的，我们只需要知道调用的是原生的绘图接口，可以保证高性能即可。
5. 至此，我们已经介绍了Flutter UI 框架和操作系统交互的这一部分原理，现在需要说一些它对应用开发者定义的开发标准。其实在前面的章节中，我们已经对这个标准非常熟悉了, 简单概括就是：组合和响应式。
6. 我们要开发一个 UI 界面，需要通过组合其他 Widget 来实现，Flutter 中，一切都是 Widget，当 UI 要发生变化时，我们不去直接修改 DOM，而是通过更新状态，让 Flutter UI 框架来根据新的状态来重新构建 UI。
7. 讲到这里，可能发现 Flutter UI 框架和 Flutter Framework 的概念是差不多的，的确如此，之所以用“UI 框架”，是因为其他平台中可能不这么叫，我们只是为了概念统一，便于描述，不必纠结于概念本身。
8. 在接下来的小节中，我们先详细介绍一下 `Element`、`RenderObject`，它们是组成 Flutter UI 框架的基石。最后我们再分析一下 Flutter 应用启动、更新流程。

## 2、`Element`、`BuildContext` 和 `RenderObject`

### ①、Element

1. 在“2.2 Widget简介”一节，我们介绍了 Widget 和 Element 的关系，我们知道最终的 UI 树其实是由一个个独立的 Element 节点构成。我们也说过组件最终的 Layout、渲染都是通过 RenderObject 来完成的，从创建到渲染的大体流程是：
	1. 根据 Widget 生成 `Element`
	2. 然后创建相应的 `RenderObject` 并关联到 `Element.renderObject` 属性上
	3. 最后再通过 `RenderObject` 来完成布局排列和绘制。
2. Element 就是 Widget 在 UI 树具体位置的一个实例化对象，大多数 Element 只有唯一的 `renderObject`，但还有一些 Element 会有多个子节点，如继承自 `RenderObjectElement` 的一些类，比如 `MultiChildRenderObjectElement`。最终所有 Element 的 `RenderObject` 构成一棵树，我们称之为”Render Tree“即”渲染树“。
3. 总结一下，我们可以认为 Flutter 的 UI 系统包含三棵树：Widget 树、Element 树、渲染树。他们的依赖关系是：Element 树根据 Widget 树生成，而渲染树又依赖于 Element 树，如图所示：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214094057.png)

4. 现在我们重点看一下 Element，Element 的生命周期如下：
	1. Framework 调用 `Widget.createElement` 创建一个 Element 实例，记为 `element`
	2. Framework 调用 `element.mount(parentElement,newSlot)` ，`mount` 方法中首先调用 `element` 所对应 Widget 的 `createRenderObject` 方法创建与 `element` 相关联的 `RenderObject` 对象，然后调用 `element.attachRenderObject` 方法将 `element.renderObject` 添加到渲染树中插槽指定的位置（这一步不是必须的，一般发生在 Element 树结构发生变化时才需要重新添加）。插入到渲染树后的 element 就处于“active”状态，处于“active”状态后就可以显示在屏幕上了（可以隐藏）。
	3. 当有父 Widget 的配置数据改变时，同时其 `State.build` 返回的 Widget 结构与之前不同，此时就需要重新构建对应的 Element 树。为了进行 Element 复用，在 Element 重新构建前会先尝试是否可以复用旧树上相同位置的 `element`，`element` 节点在更新前都会调用其对应 Widget 的 `canUpdate` 方法，如果返回 `true`，则复用旧 Element，旧的 Element 会使用新 Widget 配置数据更新，反之则会创建一个新的 Element。`Widget.canUpdate` 主要是判断 newWidget 与 oldWidget 的 `runtimeType` 和 `key` 是否同时相等，如果同时相等就返回 `true`，否则就会返回 `false`。根据这个原理，当我们需要强制更新一个 Widget 时，可以通过指定不同的 Key 来避免复用。
	4. 当有祖先 Element 决定要移除 `element` 时（如 Widget 树结构发生了变化，导致 element 对应的 Widget 被移除），这时该祖先 Element 就会调用 `deactivateChild` 方法来移除它，移除后 `element.renderObject` 也会被从渲染树中移除，然后 Framework 会调用 `element.deactivate` 方法，这时 `element` 状态变为“inactive”状态。
	5. “inactive”态的 `element` 将不会再显示到屏幕。为了避免在一次动画执行过程中反复创建、移除某个特定 `element`，“inactive”态的 `element` 在当前动画最后一帧结束前都会保留，如果在动画执行结束后它还未能重新变成“active”状态，Framework 就会调用其 `unmount` 方法将其彻底移除，这时 `element` 的状态为 defunct，它将永远不会再被插入到树中。
	6. 如果 `element` 要重新插入到 Element 树的其他位置，如 `element` 或 `element` 的祖先拥有一个 `GlobalKey`（用于全局复用元素），那么 Framework 会先将 `element` 从现有位置移除，然后再调用其 `activate` 方法，并将其 `renderObject` 重新 attach 到渲染树。
5. 看完 Element 生命周期，可能会有疑问，开发者会直接操作 Element 树吗？其实对于开发者来说，大多数情况下只需要关注 Widget 树就行，Flutter 架已经将对 Widget 树的操作映射到了 Element 树上，这可以极大的降低复杂度，提高开发效率。但是了解 Element 对理解整个 Flutter UI 框架是至关重要的，Flutter 正是通过 Element 这个纽带将 Widget 和 RenderObject 关联起来，了解 Element 层不仅会对 Flutter UI 框架有个清晰的认识，而且也会提高自己的抽象能力和设计能力。另外在有些时候，我们必须得直接使用 Element 对象来完成一些操作，比如获取主题 Theme 数据，具体细节将在下文介绍

### ②、BuildContext

#### Ⅰ、简述

1. 我们已经知道，`StatelessWidget` 和 `StatefulWidget` 的 `build` 方法都会传一个 `BuildContext` 对象：

```dart
Widget build(BuildContext context) {}
```

2. 我们也知道，在很多时候我们都需要使用这个 `context` 做一些事，比如：

```dart
Theme.of(context) //获取主题
Navigator.push(context, route) //入栈新路由
Localizations.of(context, type) //获取Local
context.size //获取上下文大小
context.findRenderObject() //查找当前或最近的一个祖先RenderObject
```

3. 那么 `BuildContext` 到底是什么呢，查看其定义，发现其是一个抽象接口类：

```dart
abstract class BuildContext {
    ...
}
```

4. 那这个 `context` 对象对应的实现类到底是谁呢？我们顺藤摸瓜，发现 `build` 调用是发生在 `StatelessWidget` 和 `StatefulWidget` 对应的 `StatelessElement` 和 `tatefulElement` 的 build 方法中，以 `tatelessElement` 为例：

```dart
class StatelessElement extends ComponentElement {
  ...
  @override
  Widget build() => widget.build(this);
  ...
}
```

5. 发现 `build` 递的参数是 `this`，很明显！这个 `BuildContext` 就是 `StatelessElement`。同样，我们同样发现 `StatefulWidget` 的 `context` 是 `StatefulElement`。但 `StatelessElement` 和 `StatefulElement` 本身并没有实现 `BuildContext` 接口，继续跟踪代码，发现它们间接继承自 `Element` 类，然后查看 `Element` 类定义，发现 `Element` 类果然实现了 `BuildContext` 接口:

```dart
class Element extends DiagnosticableTree implements BuildContext {
    ...
}
```

6. 至此真相大白，`BuildContext` 就是 `widget` 对应的 `Element`，所以我们可以通过 `context` 在 `StatelessWidget` 和 `StatefulWidget` 的 `build` 方法中直接访问 `Element` 对象。我们获取主题数据的代码 `Theme.of(context)` 内部正是调用了 Element 的 `dependOnInheritedWidgetOfExactType()` 方法。

#### Ⅱ、进阶

1. 我们可以看到 Element 是 Flutter UI 框架内部连接 `widget` 和 `RenderObject` 的纽带，大多数时候开发者只需要关注 widget 层即可，但是 widget 层有时候并不能完全屏蔽 Element 细节，所以 Framework 在 `StatelessWidget` 和 `StatefulWidget` 中通过 `build` 方法参数又将 `Element` 对象也传递给了开发者，这样一来，开发者便可以在需要时直接操作 `Element` 对象。那么现在提两个问题：
	1. 如果没有 widget 层，单靠 Element 层是否可以搭建起一个可用的 UI 框架？如果可以应该是什么样子？
	2. Flutter UI 框架能不做成响应式吗？
2. 对于问题 1，答案当然是肯定的，因为我们之前说过 widget 树只是 Element 树的映射，我们完全可以直接通过 Element 来搭建一个 UI 框架。下面举一个例子：
3. 我们通过纯粹的 Element 来模拟一个 `StatefulWidget` 的功能，假设有一个页面，该页面有一个按钮，按钮的文本是一个 9 位数，点击一次按钮，则对 9个 数随机排一次序，代码如下：

```dart
class HomeView extends ComponentElement{
  HomeView(Widget widget) : super(widget);
  String text = "123456789";

  @override
  Widget build() {
    Color primary=Theme.of(this).primaryColor; //1
    return GestureDetector(
      child: Center(
        child: TextButton(
          child: Text(text, style: TextStyle(color: primary),),
          onPressed: () {
            var t = text.split("")..shuffle();
            text = t.join();
            markNeedsBuild(); //点击后将该Element标记为dirty，Element将会rebuild
          },
        ),
      ),
    );
  }
}
```

4. 上面 `build` 方法不接收参数，这一点和在 `StatelessWidget` 和 `StatefulWidget` 中 `build(BuildContext)` 方法不同。代码中需要用到 `BuildContext` 的地方直接用 `this` 代替即可，如代码注释 1 处 `Theme.of(this)` 参数直接传 `this` 即可，因为当前对象本身就是 `Element` 实例。
5. 当 `text` 发生改变时，我们调用 `markNeedsBuild()` 方法将当前 `Element` 标记为 `dirty` 即可，标记为 `dirty` 的 `Element` 会在下一帧中重建。实际上，`State.setState()` 在内部也是调用的 `markNeedsBuild()` 方法。
6. 上面代码中 `build` 方法返回的仍然是一个 `widget`，这是由于 Flutter 框架中已经有了 widget 这一层，并且组件库都已经是以 widget 的形式提供了，如果在 Flutter 框架中所有组件都像示例的 `HomeView` 一样以 `Element` 形式提供，那么就可以用纯 Element 来构建 UI 了，`HomeView` 的 `build` 方法返回值类型就可以是 `Element` 了。
7. 如果我们需要将上面代码在现有 Flutter 框架中跑起来，那么还是得提供一个“适配器” ，widget 将 HomeV`i`ew 结合到现有框架中，下面 `CustomHome` 就相当于“适配器”：

```dart
class CustomHome extends Widget {
  @override
  Element createElement() {
    return HomeView(this);
  }
}
```

8. 现在就可以将 `CustomHome` 添加到 widget 树了，我们在一个新路由页创建它，最终效果如下如图所示：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214104401.png)

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214104406.png)

9. 点击按钮则按钮文本会随机排序。
10. 对于问题 2，答案当然也是肯定的，Flutter 引擎提供的 API 是原始且独立的，这个与操作系统提供的 API 类似，上层 UI 框架设计成什么样完全取决于设计者，完全可以将 UI 框架设计成 Android 风格或 iOS 风格，但这些事 Google 不会再去做，我们也没必要再去搞这一套，这是因为响应式的思想本身是很棒的，之所以提出这个问题，是因为做与不做是一回事，但知道能不能做是另一回事，这能反映出我们对知识的理解程度。

### ③、RenderObject

1. 在上一节我们说过每个 Element 都对应一个 RenderObject，我们可以通过 `Element.renderObject` 来获取。并且我们也说过 RenderObject 的主要职责是 Layout 和绘制，所有的 RenderObject 会组成一棵渲染树 Render Tree。本节我们将重点介绍一下 RenderObject 的作用。
2. `RenderObject` 就是渲染树中的一个对象，它主要的作用是实现事件响应以及渲染管线中除过 `build` 的执行过程（`build` 过程由 `element` 实现），即包括：布局、绘制、层合成以及上屏，这些我们将在后面章节介绍。
3. `RenderObject` 拥有一个 `parent` 和一个 `parentData` 属性，`parent` 指向渲染树中自己的父节点，而 `parentData` 是一个预留变量，在父组件的布局过程，会确定其所有子组件布局信息（如位置信息，即相对于父组件的偏移），而这些布局信息需要在布局阶段保存起来，因为布局信息在后续的绘制阶段还需要被使用（用于确定组件的绘制位置），而 `parentData` 属性的主要作用就是保存布局信息，比如在 `Stack` 布局中， `RenderStack` 就会将子元素的偏移数据存储在子元素的 `parentData中`（具体可以查看 `Positioned` 实现）。
4. `RenderObject` 类本身实现了一套基础的布局和绘制协议，
	1. 但是并没有定义子节点模型（如一个节点可以有几个子节点，没有子节点？一个？两个？或者更多？）。 
	2. 它也没有定义坐标系统（如子节点定位是在笛卡尔坐标中还是极坐标？）
	3. 和具体的布局协议（是通过宽高还是通过 constraint 和 size?，或者是否由父节点在子节点布局之前或之后设置子节点的大小和位置等）。
5. 为此，Flutter 框架提供了一个 `RenderBox` 和一个 `RenderSliver` 类，它们都是继承自 `RenderObject`，布局坐标系统采用笛卡尔坐标系，屏幕的(top, left)是原点。而 Flutter 基于这两个类分别实现了基于 `RenderBox` 的盒模型布局和基于 Sliver 的按需加载模型，这个我们已经在前面章节介绍过。

## 3、Flutter 启动流程和渲染管线

### ①、应用启动

1. Flutter 的入口在 `lib/main.dart` 的 `main()` 函数中，它是 Dart 应用程序的起点。在 Flutter 应用中，`main()` 函数最简单的实现如下：

```dart
void main() => runApp(MyApp());
```

2. 可以看 `main()` 函数只调用了一个 `runApp()` 方法，我们看看 `runApp()` 方法中都做了什么：

```dart
void runApp(Widget app) {
  WidgetsFlutterBinding.ensureInitialized()
    ..attachRootWidget(app)
    ..scheduleWarmUpFrame();
}
```

3. 参数 `app` 是一个 widget，它是 Flutter 应用启动后要展示的第一个组件。而 `WidgetsFlutterBinding` 正是绑定 widget 框架和 Flutter 引擎的桥梁，定义如下：

```dart
class WidgetsFlutterBinding extends BindingBase with GestureBinding, ServicesBinding, SchedulerBinding, PaintingBinding, SemanticsBinding, RendererBinding, WidgetsBinding {
  static WidgetsBinding ensureInitialized() {
    if (WidgetsBinding.instance == null)
      WidgetsFlutterBinding();
    return WidgetsBinding.instance;
  }
}
```

4. 可以看到 `WidgetsFlutterBinding` 继承自 `BindingBase` 并混入了很多 `Binding`，在介绍这些 `Binding` 之前我们先介绍一下 `Window`，下面是 `Window` 的官方解释：`The most basic interface to the host operating system's user interface.`
5. 很明显，Window 正是 Flutter Framework 连接宿主操作系统的接口。我们看一下  Window 类的部分定义：

```dart
class Window {
    
  // 当前设备的DPI，即一个逻辑像素显示多少物理像素，数字越大，显示效果就越精细保真。
  // DPI是设备屏幕的固件属性，如Nexus 6的屏幕DPI为3.5 
  double get devicePixelRatio => _devicePixelRatio;
  
  // Flutter UI绘制区域的大小
  Size get physicalSize => _physicalSize;

  // 当前系统默认的语言Locale
  Locale get locale;
    
  // 当前系统字体缩放比例。  
  double get textScaleFactor => _textScaleFactor;  
    
  // 当绘制区域大小改变回调
  VoidCallback get onMetricsChanged => _onMetricsChanged;  
  // Locale发生变化回调
  VoidCallback get onLocaleChanged => _onLocaleChanged;
  // 系统字体缩放变化回调
  VoidCallback get onTextScaleFactorChanged => _onTextScaleFactorChanged;
  // 绘制前回调，一般会受显示器的垂直同步信号VSync驱动，当屏幕刷新时就会被调用
  FrameCallback get onBeginFrame => _onBeginFrame;
  // 绘制回调  
  VoidCallback get onDrawFrame => _onDrawFrame;
  // 点击或指针事件回调
  PointerDataPacketCallback get onPointerDataPacket => _onPointerDataPacket;
  // 调度Frame，该方法执行后，onBeginFrame和onDrawFrame将紧接着会在合适时机被调用，
  // 此方法会直接调用Flutter engine的Window_scheduleFrame方法
  void scheduleFrame() native 'Window_scheduleFrame';
  // 更新应用在GPU上的渲染,此方法会直接调用Flutter engine的Window_render方法
  void render(Scene scene) native 'Window_render';

  // 发送平台消息
  void sendPlatformMessage(String name,
                           ByteData data,
                           PlatformMessageResponseCallback callback) ;
  // 平台通道消息处理回调  
  PlatformMessageCallback get onPlatformMessage => _onPlatformMessage;
  
  ... //其他属性及回调
   
}
```

6. 可以看到 `Window` 类包含了当前设备和系统的一些信息以及 Flutter Engine 的一些回调。现在我们再回来看看 `WidgetsFlutterBinding` 混入的各种 `Binding`。通过查看这些 `Binding` 的源码，我们可以发现这些 `Binding` 中基本都是监听并处理 `Window` 对象的一些事件，然后将这些事件按照 Framework 的模型包装、抽象然后分发。可以看到 `WidgetsFlutterBinding` 正是粘连 Flutter engine 与上层 Framework 的“胶水”。
	1. `GestureBinding`：提供了 `window.onPointerDataPacket` 回调，绑定 Framework 手势子系统，是 Framework 事件模型与底层事件的绑定入口。
	2. `ServicesBinding`：提供了 `window.onPlatformMessage` 回调， 用于绑定平台消息通道（message channel），主要处理原生和 Flutter 通信。
	3. `SchedulerBinding`：提供了 `window.onBeginFrame` 和 `window.onDrawFrame` 回调，监听刷新事件，绑定 ramework 绘制调度子系统。
	4. `PaintingBinding`：绑定绘制库，主要用于处理图片缓存。
	5. `SemanticsBinding`：语义化层与 Flutter engine 的桥梁，主要是辅助功能的底层支持。
	6. `RendererBinding`: 提供了 `window.onMetricsChanged` 、`window.onTextScaleFactorChanged` 等回调。它是渲染树与 Flutter engine 的桥梁。
	7. `WidgetsBinding`：提供了 `window.onLocaleChanged`、`onBuildScheduled` 等回调。它是 Flutter widget 层与 engine 的桥梁。
7. `WidgetsFlutterBinding.ensureInitialized()` 负责初始化一个 `WidgetsBinding` 全局单例，紧接着会调用 `WidgetsBinding` 的 `attachRootWidget` 方法，该方法负责将根 Widget 添加到 RenderView 上，代码如下：

```dart
void attachRootWidget(Widget rootWidget) {
  _renderViewElement = RenderObjectToWidgetAdapter<RenderBox>(
    container: renderView, 
    debugShortDescription: '[root]',
    child: rootWidget
  ).attachToRenderTree(buildOwner, renderViewElement);
}
```

8. 注意，代码中的有 `renderView` 和 `renderViewElement` 两个变量，`renderView` 是一个 `RenderObject`，它是渲染树的根，而 renderViewElement 是 `renderView` 对应的 Element 对象，可见该方法主要完成了根 widget 到根 RenderObject 再到根 Element 的整个关联过程。我们看看 `attachToRenderTree` 的源码实现：

```dart
RenderObjectToWidgetElement<T> attachToRenderTree(BuildOwner owner, [RenderObjectToWidgetElement<T> element]) {
  if (element == null) {
    owner.lockState(() {
      element = createElement();
      assert(element != null);
      element.assignOwner(owner);
    });
    owner.buildScope(element, () {
      element.mount(null, null);
    });
  } else {
    element._newWidget = this;
    element.markNeedsBuild();
  }
  return element;
}
```

9. 该方法负责创建根 `element`，即 `RenderObjectToWidgetElement`，并且将 element 与 widget 进行关联，即创建出 widget 树对应的 element 树。如果 element 已经创建过了，则将根 element 中关联的 widget 设为新的，由此可以看出 element 只会创建一次，后面会进行复用。那么 `BuildOwner` 是什么呢？其实它就是 widget framework 的管理类，它跟踪哪些 widget 需要重新构建。
10. 组件树在构建（build）完毕后，回到 `runApp` 的实现中，当调用完 `attachRootWidget` 后，最后一行会调用 `WidgetsFlutterBinding` 实例的 `scheduleWarmUpFrame()` 方法，该方法的实现在 `SchedulerBinding` 中，它被调用后会立即进行一次绘制，在此次绘制结束前，该方法会锁定事件分发，也就是说在本次绘制结束完成之前 Flutter 将不会响应各种事件，这可以保证在绘制过程中不会再触发新的重绘。

### ②、渲染管线

#### Ⅰ、Frame

1. 一次绘制过程，我们称其为一帧（frame）。我们之前说的 Flutter 可以实现 60fps（Frame Per-Second）就是指一秒钟最多可以触发 60 次重绘，FPS 值越大，界面就越流畅。这里需要说明的是 Flutter中 的 frame 概念并不等同于屏幕刷新帧（frame），因为 Flutter UI 框架的 frame 并不是每次屏幕刷新都会触发，这是因为，如果 UI 在一段时间不变，那么每次屏幕刷新都重新走一遍渲染流程是不必要的，因此，Flutter 在第一帧渲染结束后会采取一种主动请求 frame 的方式来实现只有当 UI 可能会改变时才会重新走渲染流程。
	1. Flutter 在 window 上注册一个 `onBeginFrame` 和一个 `onDrawFrame` 回调，在 `onDrawFrame` 回调中最终会调用 `drawFrame`。
	2. 当我们调用 `window.scheduleFrame()` 方法之后，Flutter 引擎会在合适的时机（可以认为是在屏幕下一次刷新之前，具体取决于 Flutter 引擎的实现）来调用 `onBeginFrame` 和 `onDrawFrame`。
2. 可以看见，只有主动调用 `scheduleFrame()`，才会执行 `drawFrame`。所以，我们在 Flutter 中的提到 frame 时，如无特别说明，则是和  `drawFrame()` 的调用对应，而不是和屏幕的刷新频率对应

#### Ⅱ、Flutter 调度过程 SchedulerPhase

1. Flutter 应用执行过程简单来讲分为 idle 和 frame 两种状态，idle 状态代表没有 frame 处理，如果应用状态改变需要刷新 UI，则需要通过 `scheduleFrame()` 去请求新的 frame，当 frame 到来时，就进入了 frame 状态，整个 Flutter 应用生命周期就是在 idle 和 frame 两种状态间切换。
2. frame 处理流程：当有新的 frame 到来时，具体处理过程就是依次执行四个任务队列：`transientCallbacks`、`midFrameMicrotasks`、`persistentCallbacks`、`postFrameCallbacks`，当四个任务队列执行完毕后当前 frame 结束。
3. 综上，Flutter 将整个生命周期分为五种状态，通过 SchedulerPhase 枚举类来表示它们：

```dart
enum SchedulerPhase {
  
  /// 空闲状态，并没有 frame 在处理。这种状态代表页面未发生变化，并不需要重新渲染。
  /// 如果页面发生变化，需要调用`scheduleFrame()`来请求 frame。
  /// 注意，空闲状态只是指没有 frame 在处理，通常微任务、定时器回调或者用户事件回调都
  /// 可能被执行，比如监听了tap事件，用户点击后我们 onTap 回调就是在idle阶段被执行的。
  idle,

  /// 执行”临时“回调任务，”临时“回调任务只能被执行一次，执行后会被移出”临时“任务队列。
  /// 典型的代表就是动画回调会在该阶段执行。
  transientCallbacks,

  /// 在执行临时任务时可能会产生一些新的微任务，比如在执行第一个临时任务时创建了一个
  /// Future，且这个 Future 在所有临时任务执行完毕前就已经 resolve 了，这中情况
  /// Future 的回调将在[midFrameMicrotasks]阶段执行
  midFrameMicrotasks,

  /// 执行一些持久的任务（每一个frame都要执行的任务），比如渲染管线（构建、布局、绘制）
  /// 就是在该任务队列中执行的.
  persistentCallbacks,

  /// 在当前 frame 在结束之前将会执行 postFrameCallbacks，通常进行一些清理工作和
  /// 请求新的 frame。
  postFrameCallbacks,
}
```

4. 需要注意，我们接下来要重点介绍的渲染管线就是在 `persistentCallbacks` 中执行的

#### Ⅲ、渲染管线（rendering pipeline）

1. 当新的 frame 到来时，调用到 WidgetsBinding 的 `drawFrame()` 方法，我们来看看它的实现：

```dart
@override
void drawFrame() {
 ...//省略无关代码
  try {
    buildOwner.buildScope(renderViewElement); // 先执行构建
    super.drawFrame(); //然后调用父类的 drawFrame 方法
  } 
}
```

2. 实际上关键的代码就两行：先重新构建（build），然后再调用父类的 `drawFrame` 方法，我们将父类的 `drawFrame方法展开后`：

```dart
void drawFrame() {
  buildOwner!.buildScope(renderViewElement!); // 1.重新构建widget树
  //下面是 展开 super.drawFrame() 方法
  pipelineOwner.flushLayout(); // 2.更新布局
  pipelineOwner.flushCompositingBits(); //3.更新“层合成”信息
  pipelineOwner.flushPaint(); // 4.重绘
  if (sendFramesToEngine) {
    renderView.compositeFrame(); // 5. 上屏，会将绘制出的bit数据发送给GPU
    ...
  }
}
```

3. 可以看到主要做了5件事：
	1. 重新构建widget树。
	2. 更新布局。
	3. 更新“层合成”信息。
	4. 重绘。
	5. 上屏：将绘制的产物显示在屏幕上
4. 我们称上面的5步为 rendering pipeline，中文翻译为 “渲染流水线” 或 “渲染管线”。而渲染管线的这 5 个步骤的具体过程便是本章重点要介绍的。下面我们以 `setState` 的执行更新的流程为例先对整个更新流程有一个大概的影响

#### Ⅳ、setState 执行流

1. `setState` 调用后：
	1. 首先调用当前 element 的 `markNeedsBuild` 方法，将当前 element 标记为 dirty 。
	2. 接着调用 `scheduleBuildFor`，将当前 element 添加到 pipelineOwner 的 dirtyElements 列表。
	3. 最后请求一个新的 frame，随后会绘制新的 frame：`onBuildScheduled->ensureVisualUpdate->scheduleFrame()` 。当新的 frame 到来时执行渲染管线

```dart
void drawFrame() {
  buildOwner!.buildScope(renderViewElement!); //重新构建widget树
  pipelineOwner.flushLayout(); // 更新布局
  pipelineOwner.flushCompositingBits(); //更新合成信息
  pipelineOwner.flushPaint(); // 更新绘制
  if (sendFramesToEngine) {
    renderView.compositeFrame(); // 上屏，会将绘制出的bit数据发送给GPU
    pipelineOwner.flushSemantics(); // this also sends the semantics to the OS.
    _firstFrameSent = true;
  }
}
```

2. 重新构建 widget 树：如果 `dirtyElements` 列表不为空，则遍历该列表，调用每一个 `element` 的 `rebuild` 方法重新构建新的 widget（树），由于新的 widget (树) 使用新的状态构建，所以可能导致 widget 布局信息（占用的空间和位置）发生变化，如果发生变化，则会调用其 `renderObject` 的 `markNeedsLayout` 方法，该方法会从当前节点向父级查找，直到找到一个 `relayoutBoundary` 的节点，然后会将它添加到一个全局的 `nodesNeedingLayout` 列表中；如果直到根节点也没有找到 `relayoutBoundary`，则将根节点添加到 `nodesNeedingLayout` 列表中。
3. 更新布局：遍历 `nodesNeedingLayout` 数组，对每一个 `renderObject` 重新布局（调用其 layout 方法），确定新的大小和偏移。`layout` 方法中会调用 `markNeedsPaint()`，该方法和 `markNeedsLayout` 方法功能类似，也会从当前节点向父级查找，直到找到一个 `isRepaintBoundary` 属性为 `true` 的父节点，然后将它添加到一个全局的 `nodesNeedingPaint` 列表中；由于根节点（RenderView）的 `isRepaintBoundary` 为 `true`，所以必会找到一个。查找过程结束后会调用 `buildOwner.requestVisualUpdate` 方法，该方法最终会调用 `scheduleFrame()`，该方法中会先判断是否已经请求过新的 frame，如果没有则请求一个新的 frame。
4. 更新合成信息：先忽略，我们在 14.8 节专门介绍。
5. 更新绘制：遍历 `nodesNeedingPaint` 列表，调用每一个节点的 `paint` 方法进行重绘，绘制过程会生成 Layer。需要说明一下，flutter 中绘制结果是保存在 Layer 中的，也就是说只要 Layer 不释放，那么绘制的结果就会被缓存，因此，Layer 可以跨 frame 来缓存绘制结果，避免不必要的重绘开销。Flutter 框架绘制过程中，遇到 `isRepaintBoundary` 为 `true` 的节点时，才会生成一个新的 Layer。可见 Layer 和 renderObject 不是一一对应关系，父子节点可以共享，这个我们会在随后的一个试验中来验证。当然，如果是自定义组件，我们可以在 renderObject 中手动添加任意多个 Layer，这通常用于只需一次绘制而随后不会发生变化的绘制元素的缓存场景，这个随后我们也会通过一个例子来演示。
6. 上屏：绘制完成后，我们得到的是一棵 Layer 树，最后我们需要将 Layer 树中的绘制信息在屏幕上显示。我们知道 Flutter 是自实现的渲染引擎，因此，我们需要将绘制信息提交给 Flutter engine，而 `renderView.compositeFrame` 正是完成了这个使命。
7. 以上，便是 `setState` 被调用到 UI 更的大概更新过程，实际的流程会更复杂一些，比如在 build 过程中是不允许再调用 `setState` 的，框架需要做一些检查。又比如在 frame 中会涉及到动画的调度、在上屏时会将所有的 Layer 添加到场景（Scene）对象后，再渲染 Scene。上面的流程读者先有个印象即可，我们将在后面的小节中详细介绍。

#### Ⅴ、setState 执行时机问题

##### （1）、简述

1. `setState` 会触发 `build`，而 `build` 是在执行 `persistentCallbacks` 阶段执行的，因此只要不是在该阶段执行 `setState` 就绝对安全，但是这样的粒度太粗，比如在 `transientCallbacks` 和 `midFrameMicrotasks` 阶段，如果应用状态发生变化，最好的方式是只将组件标记为 `dirty`，而不用再去请求新的 frame ，因为当前 frame 还没有执行到 `persistentCallbacks`，因此后面执行到后就会在当前帧渲染管线中刷新 UI。因此，`setState` 在标记完 `dirty` 后会先判断一下调度状态，如果是 `idle` 或 执行 `postFrameCallbacks` 阶段才会去请求新的 frame :

```dart
void ensureVisualUpdate() {
  switch (schedulerPhase) {
    case SchedulerPhase.idle:
    case SchedulerPhase.postFrameCallbacks:
      scheduleFrame(); // 请求新的frame
      return;
    case SchedulerPhase.transientCallbacks:
    case SchedulerPhase.midFrameMicrotasks:
    case SchedulerPhase.persistentCallbacks: // 注意这一行
      return;
  }
}
```

2. 上面的代码在大多数情况下是没有问题的，但是如果我们在 `build` 阶段又调用 `setState` 的话还是会有问题，因为如果我们在 build 阶段又调用 `setState` 的话就又会导致 `build....` 这样将将导致循环调用，因此 flutter 框架发现在 build 阶段调用 `setState` 的话就会报错，如：

```dart
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, c) {
        // build 阶段不能调用 setState, 会报错
        setState(() {
          ++index;
        });
        return Text('xx');
      },
    );
  }
```

3. 运行后会报错，控制台会打印：

```dart
==== Exception caught by widgets library ====
The following assertion was thrown building LayoutBuilder:
setState() or markNeedsBuild() called during build.
```

4. 需要注意，如果我们直接在 build 中调用 `setState` ，代码如下：

```dart
@override
Widget build(BuildContext context) {
  setState(() {
    ++index;
  });
  return Text('$index');
}  
```

5. 运行后是不会报错的，原因是在执行 build 时当前组件的 `dirty` 状态（对应的 element 中）为 `true`，只有 build 执行完后才会被置为 `false`。而 `setState` 执行的时候会会先判断当前 `dirty` 值，如果为 `true` 则会直接返回，因此就不会报错。
6. 上面我们只讨论了在 `build` 阶段调用 `setState` 会导致错误，实际上在整个构建、布局和绘制阶段都不能同步调用 `setState`，这是因为，在这些阶段调用 `setState` 都有可能请求新的 frame，都可能会导致循环调用，因此如果要在这些阶段更新应用状态时，都不能直接调用 `setState`。

##### （2）、安全更新

1. 现在我们知道在 `build` 阶段不能调用 `setState了`，实际上在组件的布局阶段和绘制阶段也都不能直接再同步请求重新布局或重绘，道理是相同的，那在这些阶段正确的更新方式是什么呢，我们以 `setState` 为例，可以通过如下方式：

```dart
// 在build、布局、绘制阶段安全更新
void update(VoidCallback fn) {
  SchedulerBinding.instance.addPostFrameCallback((_) {
    setState(fn);
  });
}
```

2. 注意，`update` 函数只应该在 frame 执行 `persistentCallbacks` 时执行，其他阶段直接调用 `setState` 即可。因为 `idle` 状态会是一个特例，如果 在 `idle` 状态调用 `update` 的话，需要手动调用 `scheduleFrame()` 请求新的 frame，否则 `postFrameCallbacks` 在下一个 frame （其他组件请求的 frame ）到来之前不会被执行，因此我们可以将 `update` 修改一下：

```dart
void update(VoidCallback fn) {
  final schedulerPhase = SchedulerBinding.instance.schedulerPhase;
  if (schedulerPhase == SchedulerPhase.persistentCallbacks) {
    SchedulerBinding.instance.addPostFrameCallback((_) {
      setState(fn);
    });
  } else {
    setState(fn);
  }
}
```

3. 至此，我们封装了一个可以安全更新状态的 `update` 函数。
4. 现在我们回想一下，在第十一章 “自绘组件：CustomCheckbox” 一节中，为了执行动画，我们在绘制完成之后通过如下代码请求重绘：

```dart
 SchedulerBinding.instance.addPostFrameCallback((_) {
   ...
   markNeedsPaint();
 });
```

5. 我们并没有直接调用 `markNeedsPaint()`，而原因正如上面所述

### ③、总结

1. 本节介绍了 Flutter App 从启动到显示到屏幕上的主流程，重点是 Flutter 的渲染流程，如图：

![](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231214124830.png)

2. 需要说明的是 build 过程和 layout 过程是可以交替执行的，这个我们在介绍 LayoutBuilder 一节时已经解释过了。
3. 我们需要对整个渲染流程有个大概印象，后面我们会详细介绍，不过在深入介绍渲染管线之前，我们得仔细的了解一下 `Element` 、`BuildContext` 和 `RenderObject` 三个类。

## 4、

### ①、

### ②、

### ③、

### ④、

### ⑤、

## 5、

## 6、

## 7、

## 8、

# 十五、
# 十六、问题整理

## 1、flutter daemon terminated 守护进程被终止

### ①、问题：

- 问题：提示守护进程被终止，同时左上角选择设备的下拉框消失

![|291](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231103100144.png)

### ②、解决：

1. 在工具栏上添加一个功能控件：

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122085721.png)

2. 添加方法为：
3. 右键工具栏，选择自定义工具栏

![|253](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122085759.png)

4. 选择一个控件，新添加的控件会出现在他的后面

![|584](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122090035.png)

5. 点击上方的 `+` 号，然后选择添加操作

![|584](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122090113.png)

6. 搜索 `Refresh`，或者选择：`插件 -> Flutter -> Refresh`，选择后，点击确定

![|557](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122090351.png)

7. 此时就会多出来选择的 `Refresh`

![|584](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122090430.png)

8. 点击确定关闭弹窗，工具栏就会多出一个 `Refresh`

![|566](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231122090522.png)

9. 点击 `Refresh`，等待一会，设备列表就会被刷新

## 2、拉取的 flutter 项目只有 lib 目录

### ①、只有 lib 目录没有安卓 ios 等目录

1. 示例：

![|341](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231127093740.png)

2. 产生的问题：连接安卓等设备调试会报错

![|700](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231127093849.png)

### ②、解决

1. 首先确认 flutter 项目所在的目录：
	1. 不能以数字开头
	2. 不能存在大写字母
	3. 需要以小写字母和下划线组成
2. 在命令行窗口中执行：`flutter create -i swift .`
	1. 执行完上面的命令，就会出现 `android、ios、macos、linux、web、windows` 等目录
	2. 但是为什么是 `swift` 我不太清楚
	3. 我试了 `kotlin` 不行
3. 结果：

![|306](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2FFlutter%2Fattachments%2FPasted%20image%2020231127103507.png)

## 3、

## 4、

## 5、

# 十七、

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















