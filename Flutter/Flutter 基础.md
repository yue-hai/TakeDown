> 官方教程：https://flutter.cn/docs
> 
> 文档参考：https://book.flutterchina.club/

# 一、环境准备

## 1、配置环境变量

1. 进入官网，下载 SDK：https://flutter.cn/docs/get-started/install/windows

![|725](attachments/Pasted%20image%2020230926125318.png)

2. 将下载下来的文件解压，并将 `bin` 目录配置到系统变量中

![|550](attachments/Pasted%20image%2020230926125515.png)

3. 打开命令行窗口，执行：`flutter --version`、`dart --version`，出现如下信息则配置成功

![|775](attachments/Pasted%20image%2020230926130052.png)

4. 如是提示网络问题，则看下面的将下载源改为国内源

## 2、将下载源改为国内源

1. 打开环境变量，新建两条用户变量
	1. `PUB_HOSTED_URL`、`https://pub.flutter-io.cn`
	2. `FLUTTER_STORAGE_BASE_URL`、`https://storage.flutter-io.cn`

![|641](attachments/Pasted%20image%2020230926130339.png)

## 3、使用 idea 创建 flutter 项目

1. idea 安装两个插件 `Flutter`、`Dart`

![|725](attachments/Pasted%20image%2020230926131825.png)

2. 点击新建，创建一个 `flutter` 项目

![|700](attachments/Pasted%20image%2020230926131950.png)

![|700](attachments/Pasted%20image%2020231016155909.png)

3. 项目创建完成，结构说明：

![|632](attachments/Pasted%20image%2020231016163227.png)

## 4、连接手机或模拟器安卓测试

1. 某个模拟器

![|925](attachments/Pasted%20image%2020231016160123.png)

2. idea 会自动连接到模拟器，点击运行安装软件

![|950](attachments/Pasted%20image%2020231016160239.png)

3. 安装完成

![](attachments/Pasted%20image%2020231016160354.png)

4. 进入软件

![](attachments/Pasted%20image%2020231016160410.png)

5. 热重载与开发者工具

![|571](attachments/Pasted%20image%2020231017095401.png)

## 5、使用命令启动并安装项目

1. 在连接到机器的情况下

![|1175](attachments/Pasted%20image%2020231016161205.png)

2. 进入终端，执行：
	1. `flutter run`，它将默认使用第一个设备进行安装和运行
	2. `flutter run -d all`：它会将应用程序安装在所有连接的设备上

![|1000](attachments/Pasted%20image%2020231016161500.png)

4. 安装完成：

![](attachments/Pasted%20image%2020231016161534.png)

![|700](attachments/Pasted%20image%2020231016161543.png)

5. 在使用命令安装项目的情况下，在此终端窗口中，按下以下按键，将会执行不同操作：

  | 按键 | 功能                                                 |
  | ---- | ---------------------------------------------------- |
  | r | 热重载                   |
  | R（shift + r） | 热重启项目。                                         |
  | p | 显示网格，这个可以很好的掌握布局情况，工作中很有用。 |
  | o | 切换 android 和 ios 的预览模式                                 |

## 6、

## 7、

## 8、

# 二、flutter 基础知识

## 1、数器应用示例

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

![|850](attachments/Pasted%20image%2020231017092643.png)

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

![|300](attachments/Pasted%20image%2020231017093352.png)

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

![|420](attachments/Pasted%20image%2020231017093716.png)

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

![|700](attachments/Pasted%20image%2020231017100448.png)

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

![|400](attachments/Pasted%20image%2020231017101253.png)

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

1. `Text` (opens new window)：该组件可以创建一个带格式的文本。
2. `Row` (opens new window)、 `Column` (opens new window)： 
	1. 这些具有弹性空间的布局类 `widget` 可以在水平（Row）和垂直（Column）方向上创建灵活的布局。
	2. 其设计是基于 Web 开发中的 Flexbox 布局模型。
3. `Stack` (opens new window)： 
	1. 取代线性布局 (译者语：和 Android 中的 FrameLayout 相似)
	2. [Stack](https://docs.flutter.dev/flutter/ widgets/Stack-class.html) 允许子 `widget` 堆叠， 可以使用 `Positioned` (opens new window) 来定位他们相对于 `Stack` 的上下左右四条边的位置。
	3. `Stacks` 是基于 Web 开发中的绝对定位（absolute positioning )布局模型设计的。
4. `Container` (opens new window)： 
	1. 可以创建矩形视觉元素。
	2. `Container` 可以装饰一个 `BoxDecoration` (opens new window)，如 `background`、一个边框、或者一个阴影。 
	3. `Container` 也可以具有边距（margins）、填充(padding) 和应用于其大小的约束(constraints)。
	4. 另外， `Container` 可以使用矩阵在三维空间中对其进行变换。

#### Ⅱ、Material 组件

1. Flutter 提供了一套丰富的 `Material` 组件，它可以帮助我们构建遵循 Material Design 设计规范的应用程序。
2. Material 应用程序以 MaterialApp (opens new window) 组件开始，该组件在应用程序的根部创建了一些必要的组件，比如 `Theme` 组件，它用于配置应用的主题。 
3. 是否使用 MaterialApp (opens new window) 完全是可选的，但是使用它是一个很好的做法。
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

![|400](attachments/Pasted%20image%2020231017104451.png)

### ⑩、总结

1. Flutter 的 `widget` 类型分为 `StatefulWidget` 和 `StatelessWidget` 两种，需要深入理解它们的区别，`widget` 将是我们构建 Flutter 应用的基石。
2. Flutter 提供了丰富的组件，在实际的开发中我们可以根据需要随意使用它们，而不必担心引入过多组件库会让你的应用安装包变大，这不是 web 开发，dart 在编译时只会编译你使用了的代码。
3. 由于 Material 和 Cupertino 都是在基础组件库之上的，所以如果我们的应用中引入了这两者之一，则不需要再引入 `flutter/widgets.dart` 了，因为它们内部已经引入过了。
4. 另外需要说明一点，本章后面章节的示例中会使用一些布局类组件，如 `Scaffold`、`Row`、`Column` 等，这些组件将在后面“布局类组件”一章中详细介绍，可以先不用关注。

## 3、

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

![|362](attachments/Pasted%20image%2020231025105505.png)

![|362](attachments/Pasted%20image%2020231025105511.png)

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

![|362](attachments/Pasted%20image%2020231025133841.png)

6. 进入 SettingRoute 页面

![|362](attachments/Pasted%20image%2020231025133851.png)

7. 点击按钮返回 HomeRoute 页面

![|362](attachments/Pasted%20image%2020231025133900.png)

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

![|362](attachments/Pasted%20image%2020231025141120.png)

6. 进入 SettingRoute 页面

![|362](attachments/Pasted%20image%2020231025141131.png)

7. 返回 HomeRoute 页面

![|362](attachments/Pasted%20image%2020231025141141.png)

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

## 5、

## 6、

## 7、

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

![|725](attachments/Pasted%20image%2020231017112137.png)

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

![|725](attachments/Pasted%20image%2020231017112052.png)

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
2. 例如，我们可能会使用设计人员创建的自定义字体，或者其他第三方的字体，如 Google Fonts (opens new window) 中的字体。
3. 在 Flutter 中使用字体分三步完成。
	1. 首先将字体文件复制到项目根目录的 `asset/fonts` 目录下，没有目录可自己创建一个
	2. 然后在 `pubspec.yaml` 中声明它们，以确保它们会打包到应用程序中。
	3. 最后通过 `TextStyle` (opens new window) 属性使用字体。

#### Ⅱ、在 asset 中声明

1. 要将字体文件打包到应用中，和使用其他资源一样
2. 要先将字体文件复制到目录中，如：

![|373](attachments/Pasted%20image%2020231017152218.png)

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

![|750](attachments/Pasted%20image%2020231017131341.png)

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

![|700](attachments/Pasted%20image%2020231017135246.png)

![|700](attachments/Pasted%20image%2020231017135256.png)

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

![|700](attachments/Pasted%20image%2020231017140640.png)

![|700](attachments/Pasted%20image%2020231017140650.png)

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

![|700](attachments/Pasted%20image%2020231017141725.png)

![|700](attachments/Pasted%20image%2020231017141738.png)

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

![|700](attachments/Pasted%20image%2020231017143844.png)

![|700](attachments/Pasted%20image%2020231017143850.png)

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

![|700](attachments/Pasted%20image%2020231017144522.png)

![|700](attachments/Pasted%20image%2020231017144531.png)

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

![|379](attachments/Pasted%20image%2020231017151915.png)

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

![|700](attachments/Pasted%20image%2020231017152700.png)

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

![|700](attachments/Pasted%20image%2020231017153437.png)

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

![|400](attachments/Pasted%20image%2020231017153745.png)

11. `color` 和 `colorBlendMode`：在图片绘制时可以对每一个像素进行颜色混合处理，`color` 指定混合色，而 `colorBlendMode` 指定混合模式，下面是一个简单的示例：

```dart
Image(
  image: AssetImage("images/avatar.png"),
  width: 100.0,
  color: Colors.blue,
  colorBlendMode: BlendMode.difference,
);
```

![|204](attachments/Pasted%20image%2020231017153935.png)

12. `repeat`：当图片本身大小小于显示空间时，指定图片的重复规则。简单示例如下

![|158](attachments/Pasted%20image%2020231017154004.png)

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

![|700](attachments/Pasted%20image%2020231017160214.png)

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

![|700](attachments/Pasted%20image%2020231017164807.png)

![|700](attachments/Pasted%20image%2020231017164814.png)

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

![|400](attachments/Pasted%20image%2020231019153255.png)

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

![|394](attachments/Pasted%20image%2020231020160120.png)

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

![|394](attachments/Pasted%20image%2020231020160041.png)

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

![|394](attachments/Pasted%20image%2020231020161209.png)

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

![|438](attachments/Pasted%20image%2020231023144103.png)

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

![|220](attachments/Pasted%20image%2020231023145029.png)

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

![|220](attachments/Pasted%20image%2020231023145029.png)

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

![|150](attachments/Pasted%20image%2020231023145917.png)

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

![|522](attachments/Pasted%20image%2020231023150056.png)

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

![|518](attachments/Pasted%20image%2020231023150341.png)

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

![|696](attachments/Pasted%20image%2020231023150430.png)

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

![|360](attachments/Pasted%20image%2020231023153047.png)

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

![|360](attachments/Pasted%20image%2020231023153900.png)

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

![|360](attachments/Pasted%20image%2020231023154138.png)

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

![|360](attachments/Pasted%20image%2020231023154846.png)

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

![](attachments/Pasted%20image%2020231023155408.png)

7. 可以看到我们主要的任务就是实现 `paintChildren`，它的主要任务是确定每个子 `widget` 位置。
8. 由于 `Flow` 不能自适应子 `widget` 的大小，我们通过在 `getSize` 返回一个固定大小来指定 `Flow` 的大小。
9. 注意，如果我们需要自定义布局策略，一般首选的方式是通过直接继承 `RenderObject`，然后通过重写 `performLayout` 的方式实现

## 6、层叠布局（Stack、Positioned）

1. 层叠布局和 Web 中的绝对定位、Android 中的 `Frame` 布局是相似的，子组件可以根据距父容器四个角的位置来确定自身的位置。
2. 层叠布局允许子组件按照代码中声明的顺序堆叠起来。
3. Flutter 中使用 `Stack` 和 `Positioned` 这两个组件来配合实现绝对定位。
4. `Stack` 允许子组件堆叠，而 `Positioned` 用于根据 Stack 的四个角来确定子组件的位置。

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

### ④、

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

![|387](attachments/Pasted%20image%2020231023165229.png)

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

![|375](attachments/Pasted%20image%2020231024110902.png)

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

![|218](attachments/Pasted%20image%2020231024111729.png)

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

![|178](attachments/Pasted%20image%2020231024112023.png)

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

![|516](attachments/Pasted%20image%2020231024123420.png)

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

![|375](attachments/Pasted%20image%2020231024134927.png)

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

![|353](attachments/Pasted%20image%2020231024142938.png)

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

![|378](attachments/Pasted%20image%2020231024143832.png)

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

![|378](attachments/Pasted%20image%2020231024144245.png)

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

![|378](attachments/Pasted%20image%2020231024144728.png)

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

![|378](attachments/Pasted%20image%2020231024145256.png)

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

![|378](attachments/Pasted%20image%2020231024145418.png)

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

![|378](attachments/Pasted%20image%2020231024145718.png)

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

![|314](attachments/Pasted%20image%2020231024145946.png)

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

![|378](attachments/Pasted%20image%2020231024150818.png)

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

![|378](attachments/Pasted%20image%2020231024155529.png)

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

![|186](attachments/Pasted%20image%2020231024155959.png)

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

![|696](attachments/Pasted%20image%2020231024160237.png)

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

![|202](attachments/Pasted%20image%2020231024160802.png)

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

![|362](attachments/Pasted%20image%2020231025151616.png)

![|362](attachments/Pasted%20image%2020231025151626.png)

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

![|261](attachments/Pasted%20image%2020231025152040.png)

4. 代码中打开抽屉菜单的方法在 `ScaffoldState` 中，通过 `Scaffold.of(context)` 可以获取父级最近的 `Scaffold` 组件的 `State` 对象

### ③、Drawer 抽屉菜单

1. `Scaffold` 的 `drawer` 和 `endDrawer` 属性可以分别接受一个 `Widget` 来作为页面的左、右抽屉菜单。
2. 如果开发者提供了抽屉菜单，那么当用户手指从屏幕左（或右）侧向里滑动时便可打开抽屉菜单。
3. 抽屉菜单通常将 `Drawer` 组件作为根节点，它实现了 `Material` 风格的菜单面板，`MediaQuery.removePadding` 可以移除 `Drawer` 默认的一些留白（比如 `Drawer` 默认顶部会留和手机状态栏等高的留白）

④、底部 Tab 导航栏

1. 我们可以通过 `Scaffold` 的 `bottomNavigationBar` 属性来设置底部导航，如本节开始示例所示，我们通过 `Material` 组件库提供的 `BottomNavigationBar` 和 `BottomNavigationBarItem` 两种组件来实现 `Material` 风格的底部导航栏。
2. 可以看到上面的实现代码非常简单，所以不再赘述，但是如果我们想实现如下图所示效果的底部导航栏应该怎么做呢？

![|360](attachments/Pasted%20image%2020231025152615.png)

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

![|530](attachments/Pasted%20image%2020231025153857.png)

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

![|362](attachments/Pasted%20image%2020231025162350.png)

## 3、ListView 列表组件

1. `ListView` 是最常用的可滚动组件之一，它可以沿一个方向线性排布所有子组件，
2. 并且它也支持列表项懒加载（在需要时才会创建）

### ①、默认构造函数

1. 我们看看ListView的默认构造函数定义：

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

![|362](attachments/Pasted%20image%2020231025164241.png)

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
    //下划线widget预定义以供复用。
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

![|362](attachments/Pasted%20image%2020231025164940.png)

### ④、ListView 原理

1. `ListView` 内部组合了 `Scrollable`、`Viewport` 和 `Sliver`，需要注意：
2. `ListView` 中的列表项组件都是 `RenderBox`，并不是 `Sliver`， 这个一定要注意。
3. 一个 `ListView` 中只有一个 `Sliver`，对列表项进行按需加载的逻辑是 `Sliver` 中实现的。
4. `ListView` 的 `Sliver` 默认是 `SliverList`，如果指定了 `itemExtent` ，则会使用 `SliverFixedExtentList`；
5. 如果 `prototypeItem` 属性不为空，则会使用 `SliverPrototypeExtentList`，无论是是哪个，都实现了子组件的按需加载模型。

### ⑤、

### ⑥、实例：无限加载列表

1. 假设我们要从数据源异步分批拉取一些数据，然后用 `ListView` 展示，当我们滑动到列表末尾时，判断是否需要再去拉取数据，如果是，则去拉取，拉取过程中在表尾显示一个 `loading`，拉取成功后将数据插入列表；如果不需要再去拉取，则在表尾提示"没有更多"。代码如下：

### ⑦、

### ⑧、

### ⑨、

## 4、


## 5、

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

## 6、

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

## 7、

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

## 8、

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、

## 9、

### ①、

### ②、

### ③、

### ④、

### ⑤、

### ⑥、

### ⑦、

### ⑧、

### ⑨、


# 七、

# 八、

# 九、

# 十、

# 十一、

# 十二、

# 十三、

# 十四

# 十五、

# 十六、

# 十七、

# 十八、

# 十九、

# 二十、

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















