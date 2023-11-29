# 一、Dart 基础

1. fluterr 的基础语法是 dart，所以先学 dart
2. Flutter 中的 dart SDK 路径：`D:\java\Flutter\flutter_windows_3.13.5-stable\bin\cache\dart-sdk`
3. dart 代码文件的后缀名为 `.dart`

## 1、主方法 `main`

```dart
main(){
  print("月海");
}
```

## 2、定义变量 `var`

- 可使用 `var` 定义，dart 会自动推断类型
- 也可以直接使用关键字定义类型

```dart
main(){
  var num = 0;
  num = num + 1;

  int num2 = 5;
  String name = "月海";

  print("月海 $num $num2 $name");
}
```

## 3、常量 `final`、`const`

1. `const` 值不变，一开始就得赋值
2. `final` 可以开始不赋值，只能赋一次
3. 而 `final` 不仅有 `const` 的编译时常量的特性，最重要的它是运行时常量，并且 `final` 是惰性初始化，即在运行时第一次使用前才初始化

```dart
main(){
  var num = 0;
  num = num + 1;

  final int num2 = 5;
  const String name = "月海";

  print("月海 $num $num2 $name");
}
```

## 4、基本数据类型

```dart
import 'dart:ffi';

main(){
  // 数字
  int num = 0;
  // 浮点型
  double num2 = 0.1;
  // 布尔型
  bool darkMode = true;

  // 字符串
  String name = '月海';
  String name2 = "月海";
  // 多行文本
  String name3 = '''
    月海
    
    月海
  ''';
  String name4 = """
    月海
    
    月海月海
  """;

  print("月海 $num $num2 $darkMode");
  print(name);
  print(name2);
  print(name3);
  print(name4);
}
```

## 5、集合 `list`

```dart
main(){

  // 1、不指定类型
  var list1 = ["", "", 123];
  // 2、指定类型
  var list2 = <String>["", "", "123"];
  // 添加数据
  list1.add(true);
  list2.add("456");

  // 通过下标获取元素
  print("$list1 ${list2[3]}");

  // 指定长度，这样创建的集合长度固定，不可增删元素
  var list3 = List.filled(2, "123");
}
```

## 6、键值对 `map`

```dart
main(){

  // 创建时添加数据
  var map = {
    "name": "月海",
    "age": 16
  };
  print("姓名：${map["name"]}、年龄：${map["age"]}");

  // 创建后再添加数据
  var map2 = {};
  map2["name"] = "言";
  map2["age"] = 14;
  print("姓名：${map2["name"]}、年龄：${map2["age"]}");
}
```

## 7、类型转换

- 也可以使用 `as` 关键字进行转换

```dart
main(){
  // 数字
  int num = 0;
  // 浮点型
  double num2 = 0.1;
  // 布尔型
  bool darkMode = true;
  // 字符串
  String str = "123";

  // Number 类型转换成 String 类型 toString()
  print(num2.toString() is String);
  // String 类型转成 Number 类型  int.parse()
  print(int.parse(str) is int);
}
```

## 8、运算符

| 运算符         |                                              |
| -------------- | -------------------------------------------- |
| 算术运算符     | `+`、`-`、`*`、`/`、`%(取余)`、`~/(取整)`|
| 关系运算符     | `==`、`!=`、`>`、`<`、`>=`、`<=`               |
| 逻辑运算符     | `!`、`&&`、`丨丨`                                        |
| 基础赋值运算符 | `=`、`??=`                                      |
| 复合赋值运算符 | `=`、`-=`、`*=`、`/=`、`%=`、`~/=`                     |

## 9、条件判断

### ①、`if`

```dart
import 'dart:ffi';

main(){
  int a = 10;
  int b = 20;

  if (a == 10){
    print(a);
  }else if (b == 20){
    print(b);
  }
}
```

### ②、`switch`

```dart
main(){
  int a = 10;
  int b = 20;

  switch(a){
    case 10:
      print(100);
      break;
    case 20:
      print(200);
      break;
  }
}
```

### ③、三元运算符

```dart
main(){
  int a = 10;
  int b = 20;

  var str = a==10? "== 10" : "!= 10";
  print(str);
}
```

### ④、`??` 判空

- 判断前面的变量是否为空，不为空则返回该变量，为空则返回后面的值（或变量）

```dart
main(){
  var a = 10;
  var b = 20;
  var num = a ?? b;
  print(num);

  var c;
  var num2 = c ?? b;
  print(num2);
}
```

## 10、循环

### ①、`for`

```dart
main(){
  for(var i = 0; i <= 100; i++ ){
    print(i);
  }
  
  List list=[1,2,3,4,5,6,7];
  list.forEach((it){
    print(it);
  });
}
```

### ②、`while`

```dart
main(){
  int i = 0;
  while(i < 100){
    i++;
    print(i);
  }

  int j = 0;
  do{
    j++;
    print(j);
  }while(j < 100);
}
```

### ③、`break` 和 `continue`


1. `break` 语句功能：
	1. 在 `switch` 语句中使流程跳出 `switch` 结构。
	2. 在循环语句中使流程跳出当前循环，遇到 `break` 循环终止，后面代码也不会执行
	3. 在多层循环中，一个 `break` 语句只能向外跳出一层
	4. `break` 可以用在 `switch case` 中 也可以用在 `for` 循环和 `while` 循环中
2. `continue` 语句的功能：
	1. 只能在循环语句中使用，使本次循环结束，即跳过循环体中下面尚未执行的语句，接着进行下次的是否执行循环的判断。
	2. `continue` 可以用在 `for` 循环以及 `while` 循环中，但是不建议用在 `while` 循环中，不小心容易死循环

# 二、`list`、`set`、`map`

## 1、集合 `list`

| 描述 | 常用属性和方法 |
| ---- | -------------- |
|**常用属性：**||
|长度|length|
|翻转|reversed|
|是否为空|isEmpty|
|是否不为空|isNotEmpty|
|**常用方法：**||
|增加|add|
|拼接数组|addAll|
|查找  传入具体值|indexOf|
|删除  传入具体值|remove|
|删除  传入索引值|removeAt|
|修改|fillRange|
|指定位置插入|insert(index,value);|
|指定位置插入List|insertAll(index,list)|
|其他类型转换成List|toList()|    
|List转换成字符串|join()|      
|字符串转化成List|split()| 

## 2、不可重复集合 `set`

1. 用它最主要的功能就是去除数组重复内容
2. Set 是没有顺序且不能重复的集合，所以不能通过索引去获取值

## 3、键值对 `map`

| 描述                           | 常用属性和方法 |
| ------------------------------ | -------------- |
| **常用属性：**                     |                |
| 获取所有的key值                | keys           |
| 获取所有的value值              | values         |
| 是否为空                       | isEmpty        |
| 是否不为空                     | isNotEmpty     |
| **常用方法:**                      |                |
| 删除指定key的数据              | remove(key)    |
| 合并映射  给映射内增加属性     | addAll({...})  |
| 查看映射内的值  返回true/false | containsValue  |

## 4、`map`、`where`、`any`、`every` 方法

- 这些方法 `list`、`set`、`map` 都可以使用

### ①、`map`

1. `map` 接受一个函数作为参数，并将该函数应用于列表中的每个元素，然后返回一个新的可迭代对象（通常是一个Iterable）。
2. 这个新的可迭代对象包含了原始列表中每个元素经过函数处理后的结果

```dart
main(){
  List list = [1, 2, 3, 4, 5 , 6];
  Set set = {1, 2, 3, 4, 5, 5, 5, 5};
  // 不加泛型默认都是 String
  Map<int, String> map = {
    1: "1-1",
    2: "2-2",
    3: "3-3"
  };

  List list2 = list.map((e) =>
    e * 10
  ).toList();
  print(list2);
}
```

```bash
[10, 20, 30, 40, 50, 60]

进程已结束,退出代码0
```

### ②、`where`

- `where` 方法用于筛选集合中满足指定条件的元素，并返回一个包含满足条件的元素的新集合（通常是一个Iterable）。

```dart
main(){
  List list = [1, 2, 3, 4, 5 , 6];
  Set set = {1, 2, 3, 4, 5, 5, 5, 5};
  // 不加泛型默认都是 String
  Map<int, String> map = {
    1: "1-1",
    2: "2-2",
    3: "3-3"
  };

  List list2 = list.where((e) =>
    e > 3
  ).toList();
  print(list2);
}
```

```dart
[4, 5, 6]

进程已结束,退出代码0
```

### ③、`any`

- `any` 方法用于检查集合中是否至少有一个元素满足指定条件，如果有，返回 true；否则，返回 false。

```dart
main(){
  List list = [1, 2, 3, 4, 5, 6];
  Set set = {1, 2, 3, 4, 5, 5, 5, 5};
  // 不加泛型默认都是 String
  Map<int, String> map = {
    1: "1-1",
    2: "2-2",
    3: "3-3"
  };

  print(list.any((e) => e%5 == 0 ));
  print(list.any((e) => e%10 == 0 ));
}
```

### ④、`every` 

- `every` 方法用于检查集合中是否所有元素都满足指定条件，如果都满足，返回 true；否则，返回 false。

```dart
main(){
  List list = [1, 2, 3, 4, 5, 6];
  Set set = {1, 2, 3, 4, 5, 5, 5, 5};
  // 不加泛型默认都是 String
  Map<int, String> map = {
    1: "1-1",
    2: "2-2",
    3: "3-3"
  };

  print(list.every((e) => e > 0 ));
  print(list.every((e) => e%5 == 0 ));
}
```

# 三、方法函数

- 感觉和 js 基本相同

1. 定义方法：`返回值 (形参){ 方法体 }`
2. `{}` 可选命名参数：定义的参数是可选的，需要通过参数名来传递值给这些参数，而不需要按照固定的位置传递 `void printInfo3(String str1, {String str2="月海", String str3="言"})`
3. `[]` 可选位置参数：定义的参数也是可选的，但它们是按照位置来传递的 `void printInfo4(String str1, [String str2="月海", String str3="言"])`
4. 可选命名参数和可选位置参数两种方式不可以一起使用
5. 方法作为参数：定义形参时不写类型只写一个变量名：`void printInfo5(String str1, fun){}`
6. 匿名方法：`var printInfo6 = (){ }`
7. 自执行方法，可自动执行：`((){ print("自执行方法"); })();`
8. 箭头函数：`()=>{ print("箭头函数") };`

```dart
main(){
  // 无返回值
  printInfo("月海");
  // 有返回值
  print(printInfo2("月海"));

  // {} 可选命名参数：定义的参数是可选的，需要通过参数名来传递值给这些参数，而不需要按照固定的位置传递
  printInfo3("月海1");
  printInfo3("月海1", str2: "月海2");
  // [] 可选位置参数：定义的参数也是可选的，但它们是按照位置来传递的
  printInfo4("月海1");
  printInfo4("月海1", "月海2");

  // 方法作为参数
  void printInfo51(){
    print("方法作为参数 2");
  }
  printInfo5("月海", printInfo51);

  // 匿名方法
  printInfo6();

  // 自执行方法 无参；不写最后的 () 不会执行
  ((){
    print("自执行方法");
  })();
  // 自执行方法 有参；不写最后的 () 不会执行
  ((String str){
    print("自执行方法 ${str}");
  })("月海");
}

// 无返回值
void printInfo(String str){
  print("打印：" + str);
}
// 有返回值
String printInfo2(String str){
  return "打印 2：" + str;
}

/**
 * {} 可选命名参数：定义的参数是可选的，需要通过参数名来传递值给这些参数，而不需要按照固定的位置传递
 * [] 可选位置参数：定义的参数也是可选的，但它们是按照位置来传递的
 * 两种方式不可以一起使用
 */
void printInfo3(String str1, {String str2="月海", String str3="言"}){
  print("打印：$str1、$str2");
}
void printInfo4(String str1, [String str2="月海", String str3="言"]){
  print("打印：$str1、$str2、$str3");
}

/**
 * 方法作为参数
 */
void printInfo5(String str1, fun){
  fun();
  print("打印：$str1");
}

/**
 * 匿名方法
 */
var printInfo6 = (){
  print("printInfo6");
};
```

# 四、类和对象

1. 面向对象编程 (OOP) 的三个基本特征是：封装、继承、多态
2. 封装：封装是对象和类概念的主要特性。封装，把客观事物封装成抽象的类，并且把自己的部分属性和方法提供给其他对象调用, 而一部分属性和方法则隐藏。
3. 继承：面向对象编程 (OOP) 语言的一个主要功能就是“继承”。继承是指这样一种能力：它可以使用现有类的功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。
4. 多态：允许将子类类型的指针赋值给父类类型的指针, 同一个函数调用会有不同的执行效果 。
5. Dart 所有的东西都是对象，所有的对象都继承自 Object 类。
6. Dart 是一门使用类和单继承的面向对象语言，所有的对象都是类的实例，并且所有的类都是 Object 的子类一个类通常由属性和方法组成。
7. 私有属性和方法：
	1. Dart 和其他面向对象语言不一样，没有 `public`、`private`、`protected` 这些访问修饰符
	2. 但是我们可以使用 `_` 把一个属性或者方法定义成私有。比如：`int? _sex=0;`

## 1、类的创建与实例化

- 和 java 类似

1. 创建 Person 类

```dart
class Person{
  // 姓名
  String? name;
  // 年龄
  int? age;
  // 性别，私有属性
  int? _sex=0;
  // 种族，静态属性
  static String race = "智人";

  // get set 修饰符，类似 vue 中的计算属性
  get getAge{
    return age! - 2;
  }
  set setName(name){
    this.name = "改名：" + name;
  }

  // 默认构造器
  Person();
  // 自定义构造器；后面的 :age=16 为调用该构造器实例化时，自动初始化 age 值，不需要传入参数；默认构造器也可以这样使用
  Person.name(this.name):age=16;
  Person.age(this.age);
  Person.nameAge(this.name, this.age);

  // 自定义方法
  myToString() {
    print('Person{name: $name, age: $age, sex: $sex}');
  }

  // 静态方法
  static myToString2() {
    print('静态方法调用静态属性：种族：${race}');
  }
}
```

2. 引入并实例化 Person 类，调用其属性方法

```dart
// 引入 Person 类
import 'Person.dart';

main() {

  // 实例化类
  Person person = new Person();
  Person personName = new Person.name("月海");
  Person personAge = new Person.age(16);
  Person personNAmeAge = new Person.nameAge("言", 14);

  // 调用属性
  print("${person.name}、${person.age}");
  print("${personName.name}、${personName.age}");
  print("${personAge.name}、${personAge.age}");
  print("${personNAmeAge.name}、${personNAmeAge.age}");

  // 调用方法
  personNAmeAge.myToString();

  // 调用 get
  print(personNAmeAge.getAge);
  // 调用 set
  personNAmeAge.setName = "月海";
  print(personNAmeAge.name);

  // 调用静态属性
  print(Person.race);
  // 调用静态方法
  Person.myToString2();
}
```

## 2、对象操作符

| 对象操作符 | 描述 |
| ---------- | ---- |
| ?          | 条件运算符 判空     |
|as|类型转换|
|is|类型判断|
|..|级联操作 （连缀）|

- 对象操作符例子

```dart
// 引入 Person 类
import 'Person.dart';

main() {
  // 定义一个空对象
  Person? person = null;
  // ?：判空，若是 person 为空则不会调用 age 属性；不为空才会调用
  person?.age;

  // 定义一个 Person 对象
  Person person2 = Person();
  // as：类型转换
  var object = person2 as Object;

  // 定义一个 Person 对象
  Person person3 = Person();
  // is：类型判断
  print(person3 is String);
  print(person3 is Object);

  // 定义一个 Person 对象
  Person person4 = Person();
  // ..：级联操作 （连缀）
  person4..name = "月海"
    ..age = 16
    .. myToString();
}
```

## 3、继承

1. 子类使用 `extends` 关键词来继承父类
2. 子类会继承父类里面可见的属性和方法，但是不会继承构造函数
3. 子类能复写父类的方法 getter 和 setter

---

1. 父类

```dart
class Person{
  // 姓名
  String? name;
  // 年龄
  int? age;
  // 性别，私有属性
  int? _sex=0;
  // 种族，静态属性
  static String race = "智人";

  // get set 修饰符，类似 vue 中的计算属性
  get getAge{
    return age! - 2;
  }
  set setName(name){
    this.name = "改名：" + name;
  }

  // 默认构造器
  Person();
  // 自定义构造器；后面的 :age=16 为调用该构造器实例化时，自动初始化 age 值，不需要传入参数；默认构造器也可以这样使用
  Person.name(this.name):age=16;
  Person.age(this.age);
  Person.nameAge(this.name, this.age);

  // 自定义方法
  myToString() {
    print('Person{name: $name, age: $age, sex: $sex}');
  }

  // 静态方法
  static myToString2() {
    print('静态方法调用静态属性：种族：${race}');
  }
}
```

2. 子类

```dart
import 'Person.dart';

class Student extends Person{
  // 子类属性，学号
  String? studentID;

  // 子类构造函数
  Student(String studentID, String name, int age){
    this.studentID = studentID;
    // 使用 super 关键字调用父类属性
    super.name = name;
    super.age = age;
  }

  // 子类方法，报数
  void reportNumber(){
    print("学号：$studentID");
    // 使用 super 关键字调用父类方法
    super.myToString();
  }
}
```

3. main 方法

```dart
// 引入 Person 类
import 'Student.dart';

main() {
  // 实例化学生类
  Student student = new Student("0000001", "月海", 16);

  // 调用学生类中的方法
  student.reportNumber();
}
```

## 4、抽象类

1. Dart 抽象类主要用于定义标准，子类可以继承抽象类，也可以实现抽象类接口。
2. 抽象类通过 `abstract` 关键字来定义
3. Dart 中的抽象方法不能用 abstract 声明，Dart 中没有方法体的方法我们称为抽象方法。
4. 如果子类继承抽象类必须得实现里面的抽象方法
5. 抽象类不能被实例化，只有继承它的子类可以被实例化

---

1. 抽象类 `Animal`

```dart
abstract class Animal{
  // 抽象方法
  eat();
  // 抽象方法
  run();

  // 普通方法
  printInfo(){
    print('我是一个抽象类里面的普通方法');
  }
}
```

2. 实现抽象类 `Animal` 的 `Dog` 类

```dart
import 'Animal.dart';

// 实现抽象类
class Dog extends Animal{
  // 实现抽象方法
  @override
  eat() {
    print('小狗在吃骨头');
  }

  // 实现抽象方法
  @override
  run() {
    // TODO: implement run
    print('小狗在跑');
  }
}
```

3. main 方法

```dart
// 引入 Person 类
import 'Animal.dart';
import 'Dog.dart';
import 'Student.dart';

main() {
  // 实例化 dog 类
  Dog dog = new Dog();

  // 调用 dog 中的方法
  dog.eat();
  dog.run();

  // 多态
  Animal animal = new Dog();
  animal.eat();
  animal.run();
}
```

## 5、接口

1. dart 的接口<font color="#ff0000">没有</font> `interface` 关键字定义接口，而是普通类或抽象类都可以作为接口被实现。
2. 同样使用 `implements` 关键字进行实现。
3. 但是 dart 的接口有点奇怪，如果实现的类是普通类，会将普通类和抽象中的属性的方法全部需要覆写一遍。
4. 而因为抽象类可以定义抽象方法，普通类不可以，所以一般如果要实现像 Java 接口那样的方式，一般会使用抽象类。
4. 要实现一个接口必须得实现抽象类里面定义的所有属性和方法。
5. 实现多个接口使用逗号分隔：`class Dog implements Animal, A, B {  }`
6. `extends` 抽象类 和 `implements` 接口的区别：
	1. 如果要复用抽象类里面的方法，并且要用抽象方法约束子类的话我们就用 `extends` 继承抽象类
	2. 如果只是把抽象类当做标准的话我们就用 `implements` 实现抽象类

---

1. 抽象类 `Animal`

```dart
abstract class Animal{
  // 抽象方法
  eat();
  // 抽象方法
  run();

  // 普通方法
  printInfo(){
    print('我是一个抽象类里面的普通方法');
  }
}
```

2. 以接口方式实现抽象类 `Animal` 的 `Dog` 类

```dart
import 'Animal.dart';

// 实现抽象类
class Dog implements Animal{
  // 实现抽象方法
  @override
  eat() {
    print('小狗在吃骨头');
  }

  // 实现抽象方法
  @override
  run() {
    print('小狗在跑');
  }

  @override
  printInfo() {
    print('接口中实现的抽象类中的普通方法');
  }
}
```

3. main 方法

```dart
// 引入 Person 类
import 'Animal.dart';
import 'Dog.dart';
import '../继承/Student.dart';

main() {
  // 实例化 dog 类
  Dog dog = new Dog();

  // 调用 dog 中的方法
  dog.eat();
  dog.run();
  dog.printInfo();

  // 多态
  Animal animal = new Dog();
  animal.eat();
  animal.run();
}
```

## 6、常量构造函数

1. 常量构造函数需以 `const` 关键字修饰
2. `const` 构造函数必须用于成员变量都是 `final` 的类
3. 如果实例化时不加 `const` 修饰符，即使调用的是常量构造函数，实例化的对象也不是常量实例
4. 实例化常量构造函数的时候，多个地方创建这个对象，如果传入的值相同，只会保留一个对象。
5. `Flutter` 中 `const` 修饰不仅仅是节省组件构建时的内存开销，`Flutter` 在需要重新构建组件的时候，由于这个组件是不应该改变的，重新构建没有任何意义，因此 `Flutter` 不会重建构建 `const` 组件  

## 7、mixins 混入

1. 在 Dart 中，mixins 是一种代码重用的机制，它允许一个类将其功能混合（或组合）到其他类中，而无需继承这些类的成员。
2. 这使得在 Dart 中实现一种多重继承的效果成为可能，因为一个类可以从多个 mixins 中获取功能。
3. 在 Dart 中，一个类可以同时使用继承、mixins 和实现接口

---

1. 普通类 Fly

```dart
mixin Fly {
  void fly() {
    print("Flying...");
  }
}
```

2. Bird 类使用 `with` 关键字混入 Fly 类

```dart
class Bird with Fly {
  // Bird类现在具有Fly mixin中定义的fly方法
}

```

3. main 方法

```dart
void main() {
  var bird = Bird();
  bird.fly(); // 输出 "Flying..."
}
```

# 五、其他特性

## 1、`async` 异步操作

1. 在 Dart 编程语言中，`async` 和 `await` 是用于处理异步操作的关键字，它们通常与 `Future` 或 `Stream` 一起使用，以便编写更具响应性和非阻塞的代码。
2. `async`：`async` 是一个修饰符，通常放在函数体前面。当将函数标记为 `async` 时，它意味着函数内部可以包含异步操作，这允许在函数中使用 `await` 关键字等待异步操作的完成，而不会阻塞程序的执行。例如

```dart
Future<void> fetchData() async {
  // 异步操作
}
```

3. `await`：`await` 关键字用于等待异步操作的完成，通常在 `async` 函数内部使用。当程序执行到 `await` 时，它会暂停执行直到等待的异步操作完成，然后继续执行下一步。例如：

```dart
Future<void> fetchData() async {
  var data = await fetchSomeData(); // 等待异步操作完成
  print(data);
}
```

4. 在 Dart 编程语言中，`Future` 和 `Stream` 是用于处理异步操作的两种重要的抽象类，它们有不同的用途和行为：
5. Future（未来）：`Future` 表示一个尚未完成的异步操作，通常代表一个单一的异步值或结果。可以通过 `Future` 来等待异步操作的完成，并在完成后获取结果。`Future` 是单个值的异步操作的标准方式，它通常用于表示一次性的计算、网络请求、文件读取等。例如，以下是使用 Future 进行异步操作的示例：

```dart
Future<int> fetchSomeData() async {
  // 模拟异步操作
  await Future.delayed(Duration(seconds: 2));
  return 42;
}

void main() async {
  var result = await fetchSomeData();
  print(result); // 输出 42
}
```

5. Stream（流）：`Stream` 表示一个持续的数据流，通常用于表示多个值的异步序列，例如事件流或数据流。与 Future 不同，`Stream` 可以发出多个值，并且可以在一段时间内不断产生值。以下是使用 `Stream` 创建和监听事件流的示例：

```dart
Stream<int> countStream() async* {
  for (int i = 1; i <= 5; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

void main() async {
  await for (var value in countStream()) {
    print(value); // 每秒输出 1 到 5
  }
}
```

6. 总结一下，`Future` 用于表示一次性的异步操作，而 `Stream` 用于表示连续的、可能不断产生值的异步序列。可以根据你的具体需求选择使用其中之一，或在某些情况下将它们结合使用，以处理不同类型的异步任务。


## 2、部分导入

1. 如果只需要导入库的一部分，有两种模式：
2. 模式一：只导入需要的部分，使用 `show` 关键字，如下例子所示：

```dart
import 'package:lib1/lib1.dart' show foo;
```

3. 模式二：隐藏不需要的部分，使用 `hide` 关键字，如下例子所示：

```dart
import 'package:lib2/lib2.dart' hide foo;     
```

## 3、`late` 延迟加载

1. 在 Dart 编程语言中，`late` 是一个修饰符，用于延迟初始化（或赋值）一个非空变量。
2. 使用 `late` 关键字，可以告诉 Dart 编译器，虽然没有在变量声明时立即初始化它，但保证在使用它之前会对其进行初始化。
3. 这允许在需要时推迟变量的初始化，而不会在声明时立即赋初值

```dart
late String lateVariable;

void main() {
  lateVariable = "This is initialized later.";
  print(lateVariable); // 输出 "This is initialized later."
}
```

4. 在上面的示例中，`lateVariable` 是一个使用 `late` 关键字声明的变量，它在 main 函数中被初始化。Dart 编译器允许这种延迟初始化，但要确保在使用变量之前进行初始化，否则将引发运行时异常。
5. `late` 变量通常用于表示在声明后的某个时刻会被初始化的情况，例如在构造函数之后或根据条件的不同情况。使用 `late` 可以提高代码的灵活性，同时确保变量不会在未初始化的情况下被访问。

## 4、`required` 必须参数

1. `required` 翻译成中文的意思是需要、依赖
2. `required` 关键字最开始 `@required` 是注解，现在它已经作为内置修饰符。
3. `required` 是一个修饰符，用于标记命名参数或命名参数的构造函数参数，以表示这些参数是必需的，调用者在创建对象或调用函数时必须提供这些参数的值。
4. 使用 `required` 关键字可以确保调用者不会忘记提供必要的参数值，从而在编译时捕获可能的错误。这对于构造函数参数或函数参数的验证非常有用，以确保对象或函数按照预期的方式工作。

```dart
class Person {
  final String name;
  final int age;

  Person({required this.name, required this.age});
}

void main() {
  // 创建Person对象时必须提供name和age参数的值
  var person = Person(name: "Alice", age: 30);

  // 如果缺少参数，编译器会报错
  // var person = Person(name: "Bob"); // 这会导致编译错误
}
```

5. 在上面的示例中，`Person` 类的构造函数有两个命名参数 `name` 和 `age`，并且使用 `required` 关键字标记它们。这表示在创建 `Person` 对象时，必须提供这两个参数的值，否则会引发编译时错误。
6. 总之，`required` 是Dart 中用于标记必需参数的关键字，它有助于提高代码的可靠性和可维护性，因为它确保了必要参数的存在。

## 5、typedef 定义函数类型

1. Dart 中一切皆对象，函数也是对象。
2. 每个对象都有自己的类型，函数的类型是 Function，`typedef` 就是给 Function 取个别名，如

```dart
typedef int Compare(Object a,Object b);
```

3. 定义了这个函数类型以后，可以使用 `Compare` 定义变量，这样就可以复用这个函数
4. 这样就可以使用 `Compare` 来声明一个函数变量，如

```dart
Compare compare;
```

5. `Compare` 清晰的表明了函数参数的类型及返回值的类型。这就是 `typedef` 的作用：<font color="#ff0000">给函数类型取个别名</font>。

## 6、

## 7、

## 8、

## 9、