## 一、

# 二、

# 三、

# 四、

# 五、

# 六、

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

# 二十一、JDK 8 新特性

## 0、Java 8 新特性简介

1. Java 8 (又称为 jdk 1.8) 是 Java 语言开发的一个主要版本。
2. Java 8 是 oracle 公司于 2014 年 3 月发布，可以看成是自 Java 5 以来最具革命性的版本。
3. Java 8 为 Java 语言、编译器、类库、开发工具与 JVM 带来了大量新特性：
   1.  速度更快
   2. 代码更少(增加了新的语法：Lambda 表达式)
   3. 强大的 Stream API
   4. 便于并行
   5. 最大化减少空指针异常：Optional
   6. Nashorn 引擎，允许在 JVM上 运行 JS 应用
4. 并行流与串行流：
   1. 并行流就是把一个内容分成多个数据块，并用不同的线程分别处理每个数据块的流。
   2. 相比较串行的流，并行的流可以很大程度上提高程序的执行效率。
   3. Java 8 中将并行进行了优化，我们可以很容易的对数据进行并行操作。Stream API 可以声明性地通过 parallel() 与 sequential() 在并行流与顺序流之间进行切换

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092210.png)

## 1、Lambda 表达式

### ①、为什么使用 Lambda 表达式

1. Lambda 是一个匿名函数，我们可以把 Lambda 表达式理解为是一段可以传递的代码（将代码像数据一样进行传递）。使用它可以写出更简洁、更灵活的代码。
2. 作为一种更紧凑的代码风格，使 Java 的语言表达能力得到了提升

### ②、语法

1. Lambda 表达式：在 Java 8 语言中引入的一种新的语法元素和操作符。这个操作符为 `->`，该操作符被称为 Lambda 操作符或箭头操作符。它将 Lambda 分为两个部分：
2. 左侧：指定了 Lambda 表达式需要的参数列表
3. 右侧：指定了 Lambda 体，是抽象方法的实现逻辑，也即Lambda 表达式要执行的功能。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092303.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092326.png)

### ③、类型推断

1. 上述 Lambda 表达式中的参数类型都是由编译器推断得出的。
2. Lambda 表达式中无需指定类型，程序依然可以编译，这是因为 javac 根据程序的上下文，在后台推断出了参数的类型。
3. Lambda 表达式的类型依赖于上下文环境，是由编译器推断出来的。这就是所谓的“类型推断”。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092355.png)

### ④、例子

1. 语法格式一：无参，无返回值

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092408.png)

```java
/**
 * 语法格式一：无参，无返回值
 */
@Test
public void test01(){
    /*
      传统写法
     */
    Runnable r1 = new Runnable() {
        @Override
        public void run() {
            System.out.println("月海");
        }
    };
    r1.run();

    /*
      lambda 表达式
     */
    Runnable r2 = () -> System.out.println("言");
    r2.run();
}
```

2. 语法格式二：Lambda 需要一个参数，但是没有返回值。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092422.png)

3. 语法格式三：数据类型可以省略，因为可由编译器推断得出，称为“类型推断”（由 2 更加简化而来）

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092436.png)

```java
/**
 * 语法格式二：Lambda 需要一个参数，但是没有返回值。
 * 语法格式三：数据类型可以省略，因为可由编译器推断得出，称为“类型推断”
 */
@Test
public void test02(){
    /*
      传统写法
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return Integer.compare(o1, o2);
        }
    };
    System.out.println(c1.compare(1, 2));

    /*
      lambda 表达式
     */
    Comparator<Integer> c2 = (o1, o2) -> Integer.compare(o1, o2);
    System.out.println(c2.compare(2, 1));

    /*
      方法引用
     */
    Comparator<Integer> c3 = Integer::compare;
    System.out.println(c3.compare(1, 1));
}
```

4. 语法格式四：Lambda 若只需要一个参数时，参数的小括号可以省略

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092455.png)

```java
/**
 * 语法格式四：Lambda 若只需要一个参数时，参数的小括号可以省略
 */
@Test
public void test04(){
    /*
      传统写法
     */
    Consumer<String> c1 = new Consumer<String>() {
        @Override
        public void accept(String s) {
            System.out.println(s);
        }
    };
    c1.accept("月海");

    /*
      lambda 表达式
     */
    Consumer<String> c2 = s -> System.out.println(s);
    c2.accept("言");

    /*
      方法引用
     */
    Consumer<String> c3 = System.out::println;
    c3.accept("羽");
}
```

5. 语法格式五：Lambda 需要两个或以上的参数，多条执行语句，并且可以有返回值

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092509.png)

```java
/**
 * 语法格式五：Lambda 需要两个或以上的参数，多条执行语句，并且可以有返回值
 */
@Test
public void test05(){
    /*
      传统写法
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            System.out.println("月海");
            return Integer.compare(o1, o2);
        }
    };
    System.out.println(c1.compare(1, 2));

    /*
      lambda 表达式
     */
    Comparator<Integer> c2 = (o1, o2) -> {
        System.out.println("言");
        return Integer.compare(o1, o2);
    };
    System.out.println(c2.compare(2, 1));
}
```

6. 语法格式六：当Lambda 体只有一条语句时，return 与大括号若有，都可以省略（可由 3 更加简化而来）

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092523.png)

```java
/**
     * 语法格式六：当 Lambda 体只有一条语句时，return 与大括号若有，都可以省略
     */
    @Test
    public void test06(){
        /*
          传统写法
         */
        Comparator<Integer> c1 = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return Integer.compare(o1, o2);
            }
        };
        System.out.println(c1.compare(1, 2));

        /*
          lambda 表达式
         */
        Comparator<Integer> c2 = (o1, o2) -> Integer.compare(o1, o2);
        System.out.println(c2.compare(2, 1));

        /*
          方法引用
         */
        Comparator<Integer> c3 = Integer::compare;
        System.out.println(c3.compare(1, 1));
    }
```

## 2、函数式(Functional)接口

### ①、什么是函数式接口

1. 只包含一个抽象方法的接口，称为函数式接口。
2. 你可以通过 Lambda 表达式来创建该接口的对象。（若 Lambda 表达式抛出一个受检异常（即：非运行时异常），那么该异常需要在目标接口的抽象方法上进行声明）。
3. 我们可以在一个接口上使用 `@FunctionalInterface` 注解，这样做可以检查它是否是一个函数式接口。同时 javadoc 也会包含一条声明，说明这个接口是一个函数式接口。
4. 在 `java.util.function` 包下定义了 Java 8 的丰富的函数式接口

### ②、如何理解函数式接口

1. Java 从诞生日起就是一直倡导“一切皆对象”，在 Java 里面面向对象(OOP)编程是一切。但是随着 python、scala 等语言的兴起和新技术的挑战，Java 不得不做出调整以便支持更加广泛的技术要求，也即 java 不但可以支持 OOP 还可以支持 OOF（面向函数编程）
2. 在函数式编程语言当中，函数被当做一等公民对待。在将函数作为一等公民的编程语言中，Lambda 表达式的类型是函数。但是在 Java8 中，有所不同。在 Java8 中，Lambda 表达式是对象，而不是函数，它们必须依附于一类特别的对象类型——函数式接口。
3. 简单的说，在 Java8 中，Lambda 表达式就是一个函数式接口的实例。这就是 Lambda 表达式和函数式接口的关系。也就是说，只要一个对象是函数式接口的实例，那么该对象就可以用 Lambda 表达式来表示。
4. 所以以前用匿名实现类表示的现在都可以用 Lambda 表达式来写。

### ③、函数式接口举例

```java
package java.lang;

/**
 * Represents an operation that does not return a result.
 *
 * <p> This is a {@linkplain java.util.function functional interface}
 * whose functional method is {@link #run()}.
 *
 * @author  Arthur van Hoff
 * @see     java.util.concurrent.Callable
 * @since   1.0
 */
@FunctionalInterface
public interface Runnable {
    /**
     * Runs this operation.
     */
    void run();
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092549.png)

### ④、自定义函数式接口

#### Ⅰ、`Consumer<T>`  消费型接口

```java
/**
 * 定义一个函数式接口
 * Consumer<T>  消费型接口       void accept(T t)
 * 对类型为 T 的对象应用操作
 */
public void happyTime(double money, Consumer<Double> com){
    com.accept(money);
}

@Test
public void test01(){
    /**
     * 调用接口：以前的方式
     */
    happyTime(500, new Consumer<Double>() {
        @Override
        public void accept(Double aDouble) {
            System.out.println("月海 = " + aDouble);
        }
    });

    /**
     * 调用接口：lambda 表达式的方式
     */
    happyTime(500, aDouble -> System.out.println("月海 = " + aDouble));
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092606.png)

#### Ⅱ、`Predicate<T>` 断定型接口

```java
/**
 * 定义一个函数式接口
 * Predicate<T> 断定型接口       boolean test(T t)
 * 确定类型为 T 的对象是否满足某约束，并返回boolean 值
 *
 * 根据给定的规则，过滤集合中的字符串，此规则由 Predicate 的方法决定（调用时设置）
 */
public List<String> filterString(List<String> list, Predicate<String> predicate){
    // 保存过滤后的字符串
    ArrayList<String> filterList = new ArrayList<>();

    for (String s : list) {
        if (predicate.test(s)){
            filterList.add(s);
        }
    }

    return filterList;
}

@Test
public void test02(){
    /**
     * 调用接口：以前的方式
     * 判断本次处理的字符串是不是中文，是则返回 true；返回是中文的字符串
     */
    List<String> filterString = filterString(Arrays.asList("yuehai", "月", "海", "言"), new Predicate<String>() {
        @Override
        public boolean test(String s) {
            // 判断本次处理的字符串是不是中文，是则返回 true
            return String.valueOf(s).matches("[\\u4e00-\\u9fa5]");
        }
    });
    System.out.println(filterString);

    /**
     * 调用接口：lambda 表达式的方式
     * 判断本次处理的字符串是不是中文，不是则返回 true；返回不是中文的字符串
     */
    List<String> filterString2 = filterString(Arrays.asList("yuehai", "月", "海", "言"), s -> !String.valueOf(s).matches("[\\u4e00-\\u9fa5]"));
    System.out.println(filterString2);
}
```

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092641.png)

### ⑤、作为参数传递 Lambda 表达式

作为参数传递 Lambda 表达式：为了将 Lambda 表达式作为参数传递，接收Lambda 表达式的参数类型必须是与该 Lambda 表达式兼容的函数式接口的类型

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726092720.png)

### ⑥、Java 内置四大核心函数式接口

| 函数式接口 | 参数类型 | 返回类型 | 用途 |
| --- | --- | --- | --- |
| `Consumer<T>` 消费型接口 | `T` | `void` | 对类型为 `T` 的对象应用操作，包含方法：`void accept(T t)` |
| `Supplier<T>` 供给型接口 | 无 | `T` | 返回类型为 `T` 的对象，包含方法：`T get()` |
| `Function<T, R>` 函数型接口 | `T` | `R` | 对类型为 `T` 的对象应用操作，并返回结果。结果是R类型的对象。包含方法：`R apply(T t)` |
| `Predicate<T>` 断定型接口 | `T` | `boolean` | 确定类型为 `T` 的对象是否满足某约束，并返回boolean 值。包含方法：`boolean test(T t)` |

### ⑦、其他接口

| 函数式接口 | 参数类型 | 返回类型 | 用途 |
| --- | --- | --- | --- |
| `BiFunction<T, U, R>` | `T, U` | `R` | 对类型为 T, U 参数应用操作，返回 R 类型的结果。包含方法为：`R apply(T t, U u);` |
| `UnaryOperator<T>` Function子接口 | `T` | `T` | 对类型为T的对象进行一元运算，并返回T类型的结果。包含方法为：`T apply(T t);` |
| `BinaryOperator<T>` BiFunction 子接口 | `T, T` | `T` | 对类型为T的对象进行二元运算，并返回T类型的结果。包含方法为：`T apply(T t1, T t2);` |
| `BiConsumer<T, U>` | `T, U` | `void` | 对类型为T, U 参数应用操作。包含方法为： `void accept(T t, U u)` |
| `BiPredicate<T, U>`  | `T,U ` | `boolean ` | 包含方法为： `boolean test(T t,U u)` |
| `ToIntFunction`、`ToLongFunction`、`ToDoubleFunction` | `T` | `int`、`long`、`double` | 分别计算int、long、double值的函数 |
| `IntFunction`、`LongFunction`、`DoubleFunction` | `int`、`long`、`double` | `R` | 参数分别为int、long、double 类型的函数 |

## 3、方法引用与构造器引用

### ①、方法引用是什么

1. 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用！
2. 方法引用可以看做是 Lambda 表达式深层次的表达。换句话说，方法引用就是 Lambda 表达式，也就是函数式接口的一个实例，通过方法的名字来指向一个方法，可以认为是 Lambda 表达式的一个语法糖。
3. 要求：实现接口的抽象方法的参数列表和返回值类型，必须与方法引用的方法的参数列表和返回值类型保持一致！
4. 格式：使用操作符 `::` 将类(或对象) 与 方法名分隔开来。
   1. 如下三种主要使用情况：
      1. `对象::实例方法名（非静态方法）`
      2. `类::静态方法名`
      3. `类::实例方法名（非静态方法）`

### ②、方法引用案例

1. 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用

```java
/**
 * 当要传递给 Lambda 体的操作，已经有实现的方法了，可以使用方法引用！
 */
@Test
public void test01(){
    List<String> list = Arrays.asList("月海", "言", "羽");

    /**
     * 传统写法
     */
    for (String s : list) {
        System.out.print(s + ", ");
    }
    System.out.println();
    /**
     * lambda 表达式
     */
    list.forEach((s) -> System.out.print(s + ", "));
    System.out.println();
    /**
     * 方法引用
     */
    list.forEach(System.out::print);
}
```

2. 先定义一个函数式接口

```java
/**
 * 定义一个函数式接口
 * Consumer<T>  消费型接口       void accept(T t)
 * 对类型为 T 的对象应用操作
 */
public void happyTime(double money, Consumer<Double> com){
    com.accept(money);
}
```

3. 对象::实例方法名（非静态方法）

```java
/**
 * 方法引用可以看做是 Lambda 表达式深层次的表达。
 * 换句话说，方法引用就是 Lambda 表达式，也就是函数式接口的一个实例，通过方法的名字来指向一个方法，可以认为是 Lambda 表达式的一个语法糖。
 * 所以方法引用也是函数式接口的一个实例
 *   1. 对象::实例方法名（非静态方法）
 *   2. 类::静态方法名
 *   3. 类::实例方法名（非静态方法）
 */

/**
 * 1. 对象::实例方法名（非静态方法）
 * Consumer 中的 void accept(T t)
 * PrintStream 中的 void println(T t)
 */
@Test
public void test02(){
    /**
     * 调用接口：以前的方式
     */
    Consumer<String> con1 = new Consumer<String>() {
        @Override
        public void accept(String s) {
            System.out.println("月海 = " + s);
        }
    };
    con1.accept("yuehai");
    /**
     * 调用接口：lambda 表达式的方式
     */
    Consumer<String> con2 = s -> System.out.println("言 = " + s);
    con2.accept("yan");
    /**
     * 方法引用
     */
    Consumer<String> con3 = System.out::println;
    con3.accept("羽");

    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */

    User user = new User("月海", 16);
    /**
     * 调用接口：以前的方式
     */
    Supplier<String> s1 = new Supplier<String>() {
        @Override
        public String get() {
            return user.getName();
        }
    };
    System.out.println(s1.get());
    /**
     * 调用接口：lambda 表达式的方式
     */
    Supplier<String> s2 = () -> user.getName();
    System.out.println(s2.get());
    /**
     * 方法引用
     */
    Supplier<String> s3 = user::getName;
    System.out.println(s3.get());
}
```

4. 类::静态方法名

```java
/**
 * 2. 类::静态方法名
 * Comparator 中的 int compare(T t1,T t2)
 * Integer 中的 int compare(T t1,T t2)
 */
@Test
public void test03(){
    /**
     * 调用接口：以前的方式
     */
    Comparator<Integer> c1 = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o1.compareTo(o2);
        }
    };
    System.out.println(c1.compare(10, 20));

    /**
     * 调用接口：lambda 表达式的方式
     */
    Comparator<Integer> c2 = (o1, o2) -> o1.compareTo(o2);
    System.out.println(c2.compare(10, 10));

    /**
     * 方法引用
     */
    Comparator<Integer> c3 = Integer::compareTo;
    System.out.println(c3.compare(10, 10));

    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */

    /**
     * Function 中的 R apply(T t)
     * Math 中的 Long round(Double d)
     */
    /**
     * 调用接口：以前的方式
     */
    Function<Double, Long> f1 = new Function<Double, Long>() {
        @Override
        public Long apply(Double aDouble) {
            return Math.round(aDouble);
        }
    };
    System.out.println(f1.apply(11.22));

    /**
     * 调用接口：lambda 表达式的方式
     */
    Function<Double, Long> f2 = d -> Math.round(d);
    System.out.println(f2.apply(22.11));

    /**
     * 方法引用
     */
    Function<Double, Long> f3 = Math::round;
    System.out.println(f3.apply(5.541));
}
```

5. 类::实例方法名（非静态方法）

```java
/**
 * 3. 类::实例方法名（非静态方法）
 * Comparator 中的 int comapre(T t1,T t2)
 * String 中的 int t1.compareTo(t2)
 */
@Test
public void test04() {
    /**
     * 调用接口：以前的方式
     */
    Comparator<String> c1 = new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            return o1.compareTo(o2);
        }
    };
    System.out.println(c1.compare("月海", "言"));
    /**
     * 调用接口：lambda 表达式的方式
     */
    Comparator<String> c2 = (o1, o2) -> o1.compareTo(o2);
    System.out.println(c2.compare("言", "羽"));
    /**
     * 方法引用
     */
    Comparator<String> c3 = String::compareTo;
    System.out.println(c3.compare("月海", "yuehai"));


    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */


    /**
     * BiPredicate 中的 boolean test(T t1, T t2);
     * String 中的 boolean t1.equals(t2)
     */
    /**
     * 调用接口：以前的方式
     */
    BiPredicate<String, String> b1 = new BiPredicate<String, String>() {
        @Override
        public boolean test(String s, String s2) {
            return s.equals(s2);
        }
    };
    System.out.println(b1.test("月海", "月海"));
    /**
     * 调用接口：lambda 表达式的方式
     */
    BiPredicate<String, String> b2 = (s, s2) -> s.equals(s2);
    System.out.println(b2.test("月海", "yuehai"));
    /**
     * 方法引用
     */
    BiPredicate<String, String> b3 = String::equals;
    System.out.println(b3.test("月海", "言"));


    System.out.println("----------------------------------------------");
    /**
     * ----------------------------------------------
     */


    /**
     * Function中的R apply(T t)
     * Employee中的String getName();
     */
    User user = new User("言", 14);
    /**
     * 调用接口：以前的方式
     */
    Function<User, String> f1 = new Function<User, String>() {
        @Override
        public String apply(User user) {
            return user.getName();
        }
    };
    System.out.println(f1.apply(user));
    /**
     * 调用接口：lambda 表达式的方式
     */
    Function<User, String> f2 = user1 -> user1.getName();
    System.out.println(f2.apply(user));
    /**
     * 方法引用
     */
    Function<User, String> f3 = User::getName;
    System.out.println(f3.apply(user));
}
```

### ③、构造器引用

1. 和方法引用类似，函数式接口的抽象方法的形参列表和构造器的形参列表一致
2. 抽象方法的返回值类型即为构造器所属的类的类型
3. 格式：`ClassName::new`
4. 与函数式接口相结合，自动与函数式接口中方法兼容。
5. 可以把构造器引用赋值给定义的方法，要求构造器参数列表要与接口中抽象方法的参数列表一致！且方法的返回值即为构造器对应类的对象。
6. 案例：

```java
package org.yuehai._03_MethodReferences;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Supplier;

/**
 * @author 月海
 * @create 2023/2/17 8:55
 */
public class ConstructorReferences_01 {

    /**
     * 案例 1
     * Supplier中的T get()
     * User 的空参构造器：User()
     */
    @Test
    public void test01(){
        /**
         * 传统写法
         */
        Supplier<User> s1 = new Supplier<User>() {
            @Override
            public User get() {
                return new User();
            }
        };
        System.out.println(s1.get());
        /**
         * lambda 表达式
         */
        Supplier<User> s2 = () -> new User();
        System.out.println(s2.get());
        /**
         * 构造器（方法）引用
         */
        Supplier<User> s3 = User::new;
        System.out.println(s3.get());
    }

    /**
     * 案例 2
     * Function中的R apply(T t)
     * User 的带参构造器：User()：实体类中要有对应的构造器
     */
    @Test
    public void test02(){
        /**
         * 传统写法
         */
        Function<Integer, User> f1 = new Function<Integer, User>() {
            @Override
            public User apply(Integer integer) {
                return new User(integer);
            }
        };
        System.out.println(f1.apply(14));
        /**
         * lambda 表达式
         */
        Function<Integer, User> f2 = age -> new User(age);
        System.out.println(f2.apply(16));
        /**
         * 构造器（方法）引用
         */
        Function<Integer, User> f3 = User::new;
        System.out.println(f3.apply(18));
    }

    /**
     * 案例 3
     * BiFunction中的R apply(T t,U u)
     * User 的带参构造器：User()：实体类中要有对应的构造器
     */
    @Test
    public void test03(){
        /**
         * 传统写法
         */
        BiFunction<String, Integer, User> b1 = new BiFunction<String, Integer, User>() {
            @Override
            public User apply(String s, Integer integer) {
                return new User(s, integer);
            }
        };
        System.out.println(b1.apply("月海", 16));
        /**
         * lambda 表达式
         */
        BiFunction<String, Integer, User> b2 = (name, age) -> new User(name, age);
        System.out.println(b2.apply("言", 14));
        /**
         * 构造器（方法）引用
         */
        BiFunction<String, Integer, User> b3 = User::new;
        System.out.println(b3.apply("羽", 18));
    }

}
```

### ④、数组引用

1. 可以把数组看做是一个特殊的类，则写法与构造器引用一致
2. 格式： `ClassName::new`
3. 案例：

```java
package org.yuehai._03_MethodReferences;

import org.junit.Test;

import java.util.Arrays;
import java.util.function.Function;

/**
 * @author 月海
 * @create 2023/2/17 9:22
 */
public class ArrayReference_01 {
    /**
     * 数组引用
     * Function中的R apply(T t)
     */
    @Test
    public void test03(){
        /**
         * 传统写法
         */
        Function<Integer, String[]> f1 = new Function<Integer, String[]>() {
            @Override
            public String[] apply(Integer integer) {
                return new String[integer];
            }
        };
        System.out.println(Arrays.toString(f1.apply(2)));
        /**
         * lambda 表达式
         */
        Function<Integer, String[]> f2 = length -> new String[length];
        System.out.println(Arrays.toString(f2.apply(4)));
        /**
         * 构造器（方法）引用
         */
        Function<Integer, String[]> f3 = String[]::new;
        System.out.println(Arrays.toString(f3.apply(6)));
    }
}

```

## 4、强大的 Stream API

### ①、Stream API 说明

1. Java8 中有两大最为重要的改变。第一个是 Lambda 表达式；另外一个则是 Stream API。
2. Stream API ( java.util.stream) 把真正的函数式编程风格引入到 Java 中。这是目前为止对 Java 类库最好的补充，因为 Stream API 可以极大提供 Java 程序员的生产力，让程序员写出高效率、干净、简洁的代码。
3. Stream 是 Java8 中处理集合的关键抽象概念，它可以指定你希望对集合进行的操作，可以执行非常复杂的查找、过滤和映射数据等操作。 使用Stream API 对集合数据进行操作，就类似于使用 SQL 执行的数据库查询。
4. 也可以使用 Stream API 来并行执行操作。简言之，Stream API 提供了一种高效且易于使用的处理数据的方式

### ②、为什么要使用 Stream API

1. 实际开发中，项目中多数数据源都来自于 Mysql，Oracle 等。但现在数据源可以更多了，有 MongDB，Redis 等，而这些 NoSQL 的数据就需要 Java 层面去处理。
2. Stream 和 Collection 集合的区别：Collection 是一种静态的内存数据结构，而 Stream 是有关计算的。
3. 前者是主要面向内存，存储在内存中，后者主要是面向 CPU，通过 CPU 实现计算

### ③、什么是 Stream

1. Stream到底是什么呢？是数据渠道，用于操作数据源（集合、数组等）所生成的元素序列。
2. 集合讲的是数据，Stream讲的是计算！
3. 注意：
   1. Stream 自己不会存储元素。
   2. Stream 不会改变源对象。相反，他们会返回一个持有结果的新Stream。
   3. Stream 操作是延迟执行的。这意味着他们会等到需要结果的时候才执行。

### ④、Stream 的操作三个步骤

1. 创建 Stream：一个数据源（如：集合、数组），获取一个流
2. 中间操作：一个中间操作链，对数据源的数据进行处理
3. 终止操作(终端操作)：一旦执行终止操作，就执行中间操作链，并产生结果。之后，不会再被使用

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726093332.png)

### ⑤、创建 Stream

#### Ⅰ、 通过集合  

1. Java8 中的 Collection 接口被扩展，提供了两个获取流的方法：
2. `default Stream<E> stream()` : 返回一个顺序流
3. `default Stream<E> parallelStream()` : 返回一个并行流

```java
/**
 * 创建 Stream 1 ：通过集合
 */
@Test
public void test01(){
    // 创建一个集合
    List<User> list = Arrays.asList(new User("月海", 16), new User("言", 14), new User("羽", 18));

    // 1、default Stream<E> stream() : 返回一个顺序流
    Stream<User> stream = list.stream();

    // 2、default Stream<E> parallelStream() : 返回一个并行流
    Stream<User> parallelStream = list.parallelStream();
}
```

#### Ⅱ、通过数组

1. Java8 中的 Arrays 的静态方法 stream() 可以获取数组流：`static <T> Stream<T> stream(T[] array)`：返回一个流
2. 重载形式，能够处理对应基本类型的数组：
   1. `public static IntStream stream(int[] array)`
   2. `public static LongStream stream(long[] array)`
   3. `public static DoubleStream stream(double[] array)`

```java
/**
 * 创建 Stream 2 ：通过数组
 */
@Test
public void test02(){
    // 创建一个数组
    int[] arr = new int[]{1, 2, 4 ,7};

    // 调用 Arrays 类的 static <T> Stream<T> stream(T[] array): 返回一个流
    IntStream stream = Arrays.stream(arr);
}
```

#### Ⅲ、通过Stream的of()

1. 可以调用 Stream 类静态方法 of()，通过显示值创建一个流。它可以接收任意数量的参数。
2. `public static<T> Stream<T> of(T... values)`：返回一个流

```java
/**
 * 创建 Stream 3 ：通过 Stream 的 of()
 */
@Test
public void test03(){
    // static<T> Stream<T> of(T... values) : 返回一个流
    Stream<Integer> stream = Stream.of(1, 2, 4, 7);
}
```

#### Ⅳ、创建无限流

1. 自己创建一些数据
2. 可以使用静态方法 `Stream.iterate()` 和 `Stream.generate(`)，创建无限流。
3. 迭代：`public static<T> Stream<T> iterate(final T seed, final UnaryOperator<T> f)`
4. 生成：`public static<T> Stream<T> generate(Supplier<T> s)`

```java
/**
 * 创建 Stream 4 ：创建无限流
 */
@Test
public void test04(){
    /**
     * 迭代
     * public static<T> Stream<T> iterate(final T seed, final UnaryOperator<T> f)
     * 遍历前十个偶数
     * Stream.iterate(0, t -> t + 2)：参数 1：初始值；参数 2：lambda 表达式；该语句会一直反复执行（迭代）
     * limit(10)：只要前十个结果，十个之后就结束
     */
    Stream.iterate(0, t -> t + 2).limit(10).forEach(System.out::println);

    /**
     * 生成
     * public static<T> Stream<T> generate(Supplier<T> s)
     * 取十个随机数
     * Stream.generate(Math::random)：参数 1：lambda 表达式；该语句会一直反复执行（迭代）
     * limit(10)：只要前十个结果，十个之后就结束
     */
    Stream.generate(Math::random).limit(10).forEach(System.out::println);
}
```

### ⑥、Stream 中间操作

1. 多个中间操作可以连接起来形成一个流水线，除非流水线上触发终止操作，否则中间操作不会执行任何的处理！
2. 而在终止操作时一次性全部处理，称为“惰性求值”。

#### Ⅰ、筛选与切片

| 方 法 | 描 述 |
| --- | --- |
| `filter(Predicate p)` | 接收 Lambda ， 从流中排除某些元素 |
| `distinct()` | 筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素 |
| `limit(long maxSize)` | 截断流，使其元素不超过给定数量 |
| `skip(long n)` | 跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 11:00
 */
public class _02_OperationStream_01 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * filter(Predicate p)	接收 Lambda ， 从流中排除某些元素
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：筛选出年龄大于 14；filter(Predicate p)	接收 Lambda ， 从流中排除某些元素
        stream.filter(l -> l.getAge() > 14).forEach(System.out::println);
    }

    /**
     * distinct()	筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：去重；distinct()	筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素
        stream.distinct().forEach(System.out::println);
    }

    /**
     * limit(long maxSize)	截断流，使其元素不超过给定数量
     */
    @Test
    public void test03(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：年龄大于 14，只要前一个；limit(long maxSize)	截断流，使其元素不超过给定数量
        stream.filter(l -> l.getAge() > 14).limit(1).forEach(System.out::println);
    }

    /**
     * skip(long n)	跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补
     */
    @Test
    public void test04(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：年龄大于 14，跳过第一个，只要前一个；skip(long n)	跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补
        stream.filter(l -> l.getAge() > 14).skip(1).limit(1).forEach(System.out::println);
    }
}
```

#### Ⅱ、映射

| 方 法 | 描 述 |
| --- | --- |
| `map(Function f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。 |
| `mapToInt(ToIntFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。 |
| `mapToDouble(ToDoubleFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。 |
| `mapToLong(ToLongFunction f)` | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream. |
| `flatMap(Function f)` | 接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 11:29
 */
public class _02_OperationStream_02 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * map(Function f)	接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：给姓名加前缀
        // map(Function f)	接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
        stream.map( l -> "name：" + l.getName() ).forEach(System.out::println);
    }

    /**
     * mapToInt(ToIntFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 10
        // mapToInt(ToIntFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。
        IntStream intStream = stream.mapToInt(l -> l.getAge() + 10);
        intStream.forEach(System.out::println);
    }

    /**
     * mapToDouble(ToDoubleFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。
     */
    @Test
    public void test03(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 10.1
        // mapToDouble(ToDoubleFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。
        DoubleStream doubleStream = stream.mapToDouble(l -> l.getAge() + 10.1);
        doubleStream.forEach(System.out::println);
    }

    /**
     * mapToLong(ToLongFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream.
     */
    @Test
    public void test04(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：所有年龄加 1564864165341365417L
        // mapToLong(ToLongFunction f)	接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream.
        stream.mapToLong(l -> l.getAge() + 1564864165341365417L ).forEach(System.out::println);
    }


    
    
    /**
     * 定义一个方法，将字符串中的多个字符构成的集合转换为对应的 Stream 的实例
     */
    public static Stream<Character> fromStringToStream(String str){
        ArrayList<Character> list = new ArrayList<>();
        for(Character c : str.toCharArray()){
            list.add(c);
        }
        return list.stream();
    }
    /**
     * flatMap(Function f)	接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流
     */
    @Test
    public void test05(){
        // 定义一个集合
        List<String> list5 = Arrays.asList("月海", "言", "羽", "yuehai");

        /**
         * 上面的 map 方法，类似于 list 的 add 方法，作为一个流来进行处理
         * 此处的 flatMap 方法，类似于 list 的 addAll 方法，将其中的元素取出来，每一个元素都作为一个流来进行处理
         */

        // 1、使用 map；类似集合里套集合
        Stream<Stream<Character>> streamStream = list5.stream().map(_02_OperationStream_02::fromStringToStream);
        streamStream.forEach( l -> l.forEach(System.out::println) );

        System.out.println("--------------------------------------");

        // 2、使用 flatMap；不会被嵌套
        Stream<Character> characterStream = list5.stream().flatMap(_02_OperationStream_02::fromStringToStream);
        characterStream.forEach(System.out::println);
    }
}
```

#### Ⅲ、排序

| 方 法 | 描 述 |
| --- | --- |
| `sorted()` | 产生一个新流，其中按自然顺序排序 |
| `sorted(Comparator com)` | 产生一个新流，其中按比较器顺序排序 |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 13:22
 */
public class _02_OperationStream_03 {

    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海0", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * sorted()	产生一个新流，其中按自然顺序排序
     */
    @Test
    public void test01(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：取出年龄创建一个新的流，然后按这个年龄排序
        // sorted()	产生一个新流，其中按自然顺序排序
        stream.mapToInt(User::getAge).sorted().forEach(System.out::println);
    }

    /**
     * sorted()	产生一个新流，其中按比较器顺序排序
     */
    @Test
    public void test02(){
        // 1、通过集合创建一个顺序流
        Stream<User> stream = list.stream();

        // 2、中间操作：使用比较器按年龄大小排序
        // sorted()	产生一个新流，其中按比较器顺序排序
        stream.sorted((u1, u2) -> {
            int compareAge = Integer.compare(u1.getAge(), u2.getAge());
            if (compareAge != 0){
                return compareAge;
            }else {
                return u1.getName().compareTo(u2.getName());
            }
        }).forEach(System.out::println);
    }

}
```

### ⑦、Stream 的终止操作

#### Ⅰ、匹配与查找

- 终端操作会从流的流水线生成结果。其结果可以是任何不是流的值，例如：List、Integer，甚至是 void 。
- 流进行了终止操作后，不能再次使用。

| 方 法 | 描 述 |
| --- | --- |
| `allMatch(Predicate p)` | 检查是否匹配所有元素 |
| `anyMatch(Predicate p)` | 检查是否至少匹配一个元素 |
| `noneMatch(Predicate p)` | 检查是否没有匹配所有元素 |
| `findFirst()` | 返回第一个元素 |
| `findAny()` | 返回当前流中的任意元素 |
| `count()` | 返回流中元素总数 |
| `max(Comparator c)` | 返回流中最大值 |
| `min(Comparator c)` | 返回流中最小值 |
| `forEach(Consumer c)` | 内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了) |

```java
package org.yuehai._04_StreamAPI;

import org.junit.Test;
import org.yuehai._00_bean.User;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * @author 月海
 * @create 2023/2/17 13:53
 */
public class  _03_EndStream {
    // 创建一个集合
    List<User> list = Arrays.asList(
            new User("月海0", 16),
            new User("月海", 16),
            new User("言", 14),
            new User("羽", 18)
    );

    /**
     * allMatch(Predicate p)	检查是否匹配所有元素
     * anyMatch(Predicate p)	检查是否至少匹配一个元素
     * noneMatch(Predicate p)	检查是否没有匹配所有元素
     * findFirst()	返回第一个元素
     * findAny()	返回当前流中的任意元素
     * count()	返回流中元素总数
     * max(Comparator c)	返回流中最大值
     * min(Comparator c)	返回流中最小值
     * forEach(Consumer c)	内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了)
     */
    @Test
    public void test01(){
        /**
         * 3.1、结束操作：检查是否所有人的年龄都大于 14
         * allMatch(Predicate p)	检查是否匹配所有元素
         */
        // System.out.println(list.stream().allMatch(l -> l.getAge() > 14));

        /**
         * 3.2、结束操作：检查是否有人的年龄大于 14
         * anyMatch(Predicate p)	检查是否至少匹配一个元素
         */
        // System.out.println(list.stream().anyMatch(l -> l.getAge() > 14));

        /**
         * 3.3、结束操作：检查是否没有人的年龄大于 14（是否全部小于 14）
         * noneMatch(Predicate p)	检查是否没有匹配所有元素
         */
        // System.out.println(list.stream().noneMatch(l -> l.getAge() > 14));

        /**
         * 3.4、结束操作：
         * findFirst()	返回第一个元素
         */
        // System.out.println(list.stream().findFirst());

        /**
         * 3.5、结束操作：
         * findAny()	返回当前流中的任意元素
         */
        // System.out.println(list.parallelStream().findAny());

        /**
         * 3.6、结束操作：
         * count()	返回流中元素总数
        */
        // System.out.println(list.stream().count());

        /**
         * 3.7、结束操作：
         * max(Comparator c)	返回流中最大值
         */
        // System.out.println(list.stream().mapToInt(User::getAge).max());

        /**
         * 3.8、结束操作：
         * min(Comparator c)	返回流中最小值
         */
        // System.out.println(list.stream().mapToInt(User::getAge).min());

        /**
         * 3.9、结束操作：
         * forEach(Consumer c)	内部迭代(使用 Collection 接口需要用户去做迭代，称为外部迭代。相反，Stream API 使用内部迭代——它帮你把迭代做了)
         */
        // 内部迭代
        list.stream().forEach(System.out::println);

        System.out.println("------------------------------");

        // 外部迭代
        list.forEach(System.out::println);
    }

}

```

#### Ⅱ、归约

| 方 法 | 描 述 |
| --- | --- |
| `reduce(T iden, BinaryOperator b)` | 可以将流中元素反复结合起来，得到一个值。返回 T |
| `reduce(BinaryOperator b)` | 可以将流中元素反复结合起来，得到一个值。返回 Optional |

```java
/**
 * reduce(T iden, BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 T
 * reduce(BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 Optional
 */
@Test
public void test02(){
    /**
     * 3.1、结束操作：取出集合中所有的年龄，产生一个新流，然后将新流中的年龄求和
     * reduce(T iden, BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 T
     */
    int reduceInt = list.stream().mapToInt(User::getAge).reduce(0, Integer::sum);
    System.out.println(reduceInt);

    /**
     * 3.2、结束操作：取出集合中所有的年龄，产生一个新流，然后将新流中的年龄求和
     * reduce(BinaryOperator b)	可以将流中元素反复结合起来，得到一个值。返回 Optional
     */
    OptionalInt reduceOptionalInt = list.stream().mapToInt(User::getAge).reduce(Integer::sum);
    System.out.println(reduceOptionalInt);
}
```

#### Ⅲ、收集

| 方 法 | 描 述 |
| --- | --- |
| `collect(Collector c)` | 将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法 |

1. Collector 接口中方法的实现决定了如何对流执行收集的操作(如收集到 List、Set、Map)。
2. 另外， Collectors 实用类提供了很多静态方法，可以方便地创建常见收集器实例，具体方法与实例如下表：

| 方法 | 返回类型 | 作用 | 举例 |
| --- | --- | --- | --- |
| `toList` | List | 把流中元素收集到List | List emps= list.stream().collect(Collectors.toList()); |
| `toSet` | Set | 把流中元素收集到Set | Set emps= list.stream().collect(Collectors.toSet()); |
| `toCollection` | Collection | 把流中元素收集到创建的集合 | Collection emps =list.stream().collect(Collectors.toCollection(ArrayList::new)); |
| `counting` | Long | 计算流中元素的个数 | long count = list.stream().collect(Collectors.counting()); |
| `summingInt` | Integer | 对流中元素的整数属性求和 | int total=list.stream().collect(Collectors.summingInt(Employee::getSalary)); |
| `averagingInt` | Double | 计算流中元素Integer属性的平均值 | double avg = ist.stream().collect(Collectors.averagingInt(Employee::getSalary)); |
| `summarizingInt` | IntSummaryStatistics | 收集流中Integer属性的统计值。如：平均值 | int SummaryStatisticsiss=ist.stream().collect(Collectors.summarizingInt(Employee::getSalary)); |
| `joining` | String | 连接流中每个字符串 | String str= list.stream().map(Employee::getName).collect(Collectors.joining()); |
| `maxBy` | Optional | 根据比较器选择最大值 | Optionalmax= list.stream().collect(Collectors.maxBy(comparingInt(Employee::getSalary))); |
| `minBy` | Optional | 根据比较器选择最小值 | Optional min = list.stream().collect(Collectors.minBy(comparingInt(Employee::getSalary))); |
| `reducing` | 归约产生的类型 | 从一个作为累加器的初始值开始，利用BinaryOperator与流中元素逐个结合，从而归约成单个值 | int total=list.stream().collect(Collectors.reducing(0, Employee::getSalar, Integer::sum)); |
| `collectingAndThen` | 转换函数返回的类型 | 包裹另一个收集器，对其结果转换函数 | int how= list.stream().collect(Collectors.collectingAndThen(Collectors.toList(), List::size)); |
| `groupingBy` | Map<K, List> | 根据某属性值对流分组，属性为K，结果为V | Map<Emp.Status, List> map= list.stream().collect(Collectors.groupingBy(Employee::getStatus)); |
| `partitioningBy` | Map<Boolean, List> | 根据true或false进行分区 | Map<Boolean,List> vd = list.stream().collect(Collectors.partitioningBy(Employee::getManage)); |

```java
/**
 * collect(Collector c)	将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法
 */
@Test
public void test03(){
    /**
     * 3、结束操作：
     * collect(Collector c)	将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法
     */

    /**
     * toList	List	把流中元素收集到List
     */
    List<User> collect = list.stream().collect(Collectors.toList());
    collect.forEach(System.out::println);

    /**
     * joining	String	连接流中每个字符串
     */
    String collect1 = list.stream().map(User::getName).collect(Collectors.joining());
    System.out.println(collect1);
}
```

## 5、Optional 类

### ①、介绍

1. 到目前为止，臭名昭著的空指针异常是导致 Java 应用程序失败的最常见原因。
2. 以前，为了解决空指针异常，Google 公司著名的 Guava 项目引入了 Optional 类，Guava 通过使用检查空值的方式来防止代码污染，它鼓励程序员写更干净的代码。受到 Google Guava 的启发，Optional 类已经成为 Java 8 类库的一部分。
3. `Optional<T>` 类(java.util.Optional) 是一个容器类，它可以保存类型 T 的值，代表这个值存在。或者仅仅保存 null，表示这个值不存在。原来用 null 表示一个值不存在，现在 Optional 可以更好的表达这个概念。并且可以避免空指针异常。
4. Optional 类的 Javadoc 描述如下：这是一个可以为 null 的容器对象。如果值存在则 `isPresent()` 方法会返回 true，调用 get() 方法会返回该对象

### ②、方法案例

- Optional提供很多有用的方法，这样我们就不用显式进行空值检测：
1. 创建 Optional 类对象的方法：
   1. `Optional.of(T t)` : 创建一个 Optional 实例，t必须非空；
   2. `Optional.empty()`: 创建一个空的 Optional 实例
   3. `Optional.ofNullable(T t)`：t 可以为 null

```java
/**
 * 创建 Optional 类对象的方法：
 *      Optional.of(T t) : 创建一个 Optional 实例，t必须非空；
 *      Optional.empty(): 创建一个空的 Optional 实例
 *      Optional.ofNullable(T t)：t 可以为 null
 */
@Test
public void test01(){
    User user = new User();

    /**
     * Optional.of(T t) : 创建一个 Optional 实例，t必须非空；
     */
    Optional<User> optional = Optional.of(user);
    System.out.println(optional);

    /**
     * Optional.ofNullable(T t)：t 可以为 null
     */
    user = null;
    Optional<User> optional2 = Optional.ofNullable(user);
    System.out.println(optional2);

    /**
     * Optional.empty(): 创建一个空的 Optional 实例
     */
    Optional<User> optional3 = Optional.empty();
    System.out.println(optional3);
}
```

2. 判断 Optional 容器中是否包含对象：

   1. `boolean isPresent()` : 判断是否包含对象
   2. `void ifPresent(Consumer<? super T> consumer)`：如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。

```java
/**
 * 判断 Optional 容器中是否包含对象：
 *      boolean isPresent() : 判断是否包含对象
 *      void ifPresent(Consumer<? super T> consumer)：如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。
 */
@Test
public void test02(){
    // 创建 Optional 对象
    Optional<User> optional = Optional.of(new User());
    Optional<User> optional2 = Optional.empty();

    /**
     * boolean isPresent() : 判断是否包含对象
     */
    System.out.println(optional.isPresent());
    System.out.println(optional2.isPresent());

    /**
     * void ifPresent(Consumer<? super T> consumer)：
     * 如果有值，就执行 Consumer 接口的实现代码，并且该值会作为参数传给它。
     * 如果没有值，则不进行任何操作
     */
    optional.ifPresent(System.out::println);
    optional2.ifPresent(System.out::println);
}
```

3. 获取 Optional 容器的对象：

   1. `T get()`: 如果调用对象包含值，返回该值，否则抛异常
   2. `T orElse(T other)`：如果有值则将其返回，否则返回指定的 other 对象。
   3. `T orElseGet(Supplier<? extends T> other)` ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
   4. `T orElseThrow(Supplier<? extends X> exceptionSupplier)`：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。

```java
/**
 * 获取 Optional 容器的对象：
 *      T get(): 如果调用对象包含值，返回该值，否则抛异常
 *      T orElse(T other)：如果有值则将其返回，否则返回指定的 other 对象。
 *      T orElseGet(Supplier<? extends T> other) ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
 *      T orElseThrow(Supplier<? extends X> exceptionSupplier)：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。
 */
@Test
public void test03() throws Exception {
    // 创建 Optional 对象
    Optional<User> optional = Optional.of(new User("月海", 16));
    Optional<User> optional2 = Optional.empty();

    /**
     * T get(): 如果调用对象包含值，返回该值，否则抛异常
     */
    System.out.println(optional.get());
    System.out.println(optional2.get());

    /**
     * T orElse(T other)：如果有值则将其返回，否则返回指定的 other 对象。
     */
    System.out.println(optional.orElse(new User()));
    System.out.println(optional2.orElse(new User()));

    /**
     * T orElseGet(Supplier<? extends T> other) ：如果有值则将其返回，否则返回由 Supplier 接口实现提供的对象。
     */
    System.out.println(optional.orElseGet(() -> new User("言", 14)));
    System.out.println(optional2.orElseGet(() -> new User("言", 14)));

    /**
     * T orElseThrow(Supplier<? extends X> exceptionSupplier)：如果有值则将其返回，否则抛出由 Supplier 接口实现提供的异常。
     */
    System.out.println(optional.orElseThrow(Exception::new));
    System.out.println(optional2.orElseThrow(Exception::new));
}
```

## 6、新的日期时间 API

### ①、出现背景

1. 如果我们可以跟别人说：“我们在1502643933071见面，别晚了！”那么就再简单不过了。但是我们希望时间与昼夜和四季有关，于是事情就变复杂了。
2. JDK 1.0 中包含了一个 java.util.Date 类，但是它的大多数方法已经在 JDK 1.1 引入 Calendar 类之后被弃用了。而 Calendar 并不比 Date 好多少。
3. 它们面临的问题是：
   1. 可变性：像日期和时间这样的类应该是不可变的。
   2. 偏移性：Date 中的年份是从 1900 开始的，而月份都从 0 开始。
   3. 格式化：格式化只对 Date 有用，Calendar 则不行。
   4. 此外，它们也不是线程安全的；不能处理闰秒等。
4. 总结：对日期和时间的操作一直是Java程序员最痛苦的地方之一。

### ②、新时间日期 API

1. 第三次引入的 API 是成功的，并且 Java 8 中引入的 java.time API 已经纠正了过去的缺陷，将来很长一段时间内它都会为我们服务。
2. Java 8 吸收了 Joda-Time 的精华，以一个新的开始为 Java 创建优秀的 API。
3. 新的 java.time 中包含了所有关于本地日期（LocalDate）、本地时间（LocalTime）、本地日期时间（LocalDateTime）、时区（ZonedDateTime）和持续时间（Duration）的类。
4. 历史悠久的 Date 类新增了 toInstant() 方法，用于把 Date 转换成新的表示形式。这些新增的本地化时间日期 API 大大简化了日期时间和本地化的管理。
5. 具体的包：
   1. `java.time` – 包含值对象的基础包
   2. `java.time.chrono` – 提供对不同的日历系统的访问
   3. `java.time.format` – 格式化和解析时间和日期
   4. `java.time.temporal` – 包括底层框架和扩展特性
   5. `java.time.zone` – 包含时区支持的类
6. 说明：大多数开发者只会用到基础包和 format 包，也可能会用到 temporal 包。因此，尽管有 68 个新的公开类型，大多数开发者，大概将只会用到其中的三分之一。

### ③、`LocalDate`、`LocalTime`、`LocalDateTime`

1.  LocalDate、LocalTime、LocalDateTime 类是其中较重要的几个类，它们的实例是不可变的对象，分别表示使用 ISO-8601日历系统的日期、时间、日期和时间。
2. 它们提供了简单的本地日期或时间，并不包含当前的时间信息，也不包含与时区相关的信息。
3. LocalDate 代表IOS格式（yyyy-MM-dd）的日期，可以存储生日、纪念日等日期。
4. LocalTime 表示一个时间，而不是日期。
5. LocalDateTime 是用来表示日期和时间的，这是一个最常用的类之一。
6. 注：ISO-8601日历系统是国际标准化组织制定的现代公民的日期和时间的表示法，也就是公历。

| 方法 | 描述 |
| --- | --- |
| `now()` / `* now(ZoneId zone)` | 实例化方式 1：静态方法，根据当前时间创建对象/指定时区的对象 |
| `of()` | 实例化方式2：静态方法，根据指定日期/时间创建对象 |
| `getDayOfMonth()`/`getDayOfYear()` | 获得月份天数(1-31) /获得年份天数(1-366) |
| `getDayOfWeek()` | 获得星期几(返回一个 DayOfWeek 枚举值，英文) |
| `getMonth()` | 获得月份，返回一个 Month 枚举值（英文） |
| `getMonthValue()` / `getYear()` | 获得月份(1-12) /获得年份（数字） |
| `getHour()`/`getMinute()`/`getSecond()` | 获得当前对象对应的小时、分钟、秒 |
| `withDayOfMonth()`/`withDayOfYear()`/`withMonth()`/`withYear()` | 将月份天数、年份天数、月份、年份修改为指定的值并返回新的对象 |
| `plusDays()`/`plusWeeks()`/`plusMonths()`/`plusYears()`/`plusHours()` | 向当前对象添加几天、几周、几个月、几年、几小时 |
| `minusMonths()` / `minusWeeks()`/`minusDays()`/`minusYears()`/`minusHours()` | 从当前对象减去几月/几周、几天、几年、几小时 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

/**
 * @author 月海
 * @create 2023/2/17 16:52
 */
public class _01_DateTime {

    /**
     * LocalDate 代表IOS格式（yyyy-MM-dd）的日期，可以存储生日、纪念日等日期。
     * LocalTime 表示一个时间，而不是日期。
     * LocalDateTime 是用来表示日期和时间的，这是一个最常用的类之一。
     */
    @Test
    public void test01(){
        // 实例化方式 1 ：now() / * now(ZoneId zone)	静态方法，根据当前时间创建对象/指定时区的对象
        LocalDate localDateNow = LocalDate.now();
        System.out.println(localDateNow);

        LocalTime localTimeNow = LocalTime.now();
        System.out.println(localTimeNow);

        LocalDateTime localDateTimeNow = LocalDateTime.now();
        System.out.println(localDateTimeNow);

        // 实例化方式 2 ：of()	静态方法，根据指定日期/时间创建对象
        LocalDateTime localDateTimeOf = LocalDateTime.of(2020, 11, 21, 13, 23, 43);
        System.out.println(localDateTimeOf);


        // getDayOfMonth()/getDayOfYear()	获得月份天数(1-31) /获得年份天数(1-366)
        System.out.println("当月的第几天：" + localDateTimeNow.getDayOfMonth());
        System.out.println("今年的第几天：" + localDateTimeNow.getDayOfYear());

        // getDayOfWeek()	获得星期几(返回一个 DayOfWeek 枚举值)
        System.out.println("星期几（英文）：" + localDateTimeNow.getDayOfWeek());

        // getMonth()	获得月份, 返回一个 Month 枚举值
        System.out.println("几月（英文）：" + localDateTimeNow.getMonth());

        // getMonthValue() / getYear()	获得月份(1-12) /获得年份
        System.out.println("月份（数字）：" + localDateTimeNow.getMonthValue());
        System.out.println("年份（数字）：" + localDateTimeNow.getYear());

        // getHour()/getMinute()/getSecond()	获得当前对象对应的小时、分钟、秒

        // withDayOfMonth()/withDayOfYear()/withMonth()/withYear()	将月份天数、年份天数、月份、年份修改为指定的值并返回新的对象

        // plusDays()/plusWeeks()/plusMonths()/plusYears()/plusHours()	向当前对象添加几天、几周、几个月、几年、几小时
        System.out.println("今年加上 2 年之后：" + localDateTimeNow.plusYears(2));

        // minusMonths() / minusWeeks()/minusDays()/minusYears()/minusHours()	从当前对象减去几月/几周、几天、几年、几小时

    }
    
}
```

### ④、瞬时 `Instant`

1. Instant：时间线上的一个瞬时点。 这可能被用来记录应用程序中的事件时间戳。
2. 在处理时间和日期的时候，我们通常会想到年、月、日、时、分、秒。然而，这只是时间的一个模型，是面向人类的。第二种通用模型是面向机器的，或者说是连续的。在此模型中，时间线中的一个点表示为一个很大的数，这有利于计算机处理。
3. 在 UNIX 中，这个数从 1970 年开始，以秒为的单位；同样的，在 Java 中，也是从 1970 年开始，但以毫秒为单位。
4. java.time 包通过值类型 Instant 提供机器视图，不提供处理人类意义上的时间单位。Instant 表示时间线上的一点，而不需要任何上下文信息，例如，时区。
5. 概念上讲，它只是简单的表示自 1970 年 1 月 1 日 0 时 0 分 0 秒（UTC）开始的秒数。因为 java.time 包是基于纳秒计算的，所以 Instant 的精度可以达到纳秒级。
6. (1 ns = 10-9 s) 1秒 = 1000毫秒 =10^6微秒=10^9纳秒

| 方法 | 描述 |
| --- | --- |
| `now()` | 实例化方式 1：静态方法，返回默认 UTC 时区的 Instant 类的对象 |
| `ofEpochMilli(long epochMilli) ` | 实例化方式 2：静态方法，返回在 1970-01-01 00:00:00 基础上加上指定毫秒数之后的 Instant 类的对象 |
| `atOffset(ZoneOffset offset)` | 结合即时的偏移来创建一个 OffsetDateTime |
| `toEpochMilli()` | 返回 1970-01-01 00:00:00 到当前时间的毫秒数，即为时间戳 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * @author 月海
 * @create 2023/2/20 8:43
 */
public class _02_Instant {

    @Test
    public void test(){
        // 实例化方式 1： now()	静态方法，返回默认 UTC 时区的 Instant 类的对象；中时区（本初子午线）
        Instant instant = Instant.now();
        System.out.println("英国时间：" + instant);

        // 实例化方式 2：atOffset(ZoneOffset offset)	结合即时的偏移来创建一个 OffsetDateTime（中国为东 8 区）
        OffsetDateTime offsetDateTime = instant.atOffset(ZoneOffset.ofHours(8));
        System.out.println("中国时间" + offsetDateTime);

        // ofEpochMilli(long epochMilli) 	静态方法，返回在 1970-01-01 00:00:00 基础上加上指定毫秒数之后的 Instant 类的对象
        System.out.println(Instant.ofEpochMilli(154635412415L));

        // toEpochMilli()	返回 1970-01-01 00:00:00 到当前时间的毫秒数，即为时间戳
        System.out.println(instant.toEpochMilli());
    }

}
```

- 时间戳是指格林威治时间 1970 年 01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2FPasted%20image%2020230726093207.png)

### ⑤、格式化与解析日期或时间 `DateTimeFormatter`

1. java.time.format.DateTimeFormatter 类提供了三种格式化方法：
2. 预定义的标准格式。如：
   1. `ISO_LOCAL_DATE_TIME`
   2. `ISO_LOCAL_DATE`
   3. `ISO_LOCAL_TIME`
3. 本地化相关的格式。如：`ofLocalizedDateTime(FormatStyle.LONG)`
4. 自定义的格式。如：`ofPattern("yyyy-MM-dd hh:mm:ss")`

| 方法 | 描述 |
| --- | --- |
| `ofPattern(String pattern)` | 静态方法，返回一个指定字符串格式的 DateTimeFormatter |
| `format(TemporalAccessor t) ` | 格式化一个日期、时间，返回字符串 |
| `parse(CharSequence text)` | 将指定格式的字符序列解析为一个日期、时间 |

```java
package org.yuehai._06_DateTime;

import org.junit.Test;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.time.temporal.TemporalAccessor;

/**
 * @author 月海
 * @create 2023/2/20 9:02
 */
public class _03_DateTimeFormatter {

    /**
     * 1. 预定义的标准格式。如：
     *   a. ISO_LOCAL_DATE_TIME
     *   b. ISO_LOCAL_DATE
     *   c. ISO_LOCAL_TIME
     * 2. 本地化相关的格式。如：ofLocalizedDateTime(FormatStyle.LONG)
     * 3. 自定义的格式。如：ofPattern("yyyy-MM-dd hh:mm:ss")
     */

    /**
     * 1. 预定义的标准格式。如：
     *      a. ISO_LOCAL_DATE_TIME
     *      b. ISO_LOCAL_DATE
     *      c. ISO_LOCAL_TIME
     */
    @Test
    public void test01(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        DateTimeFormatter isoLocalDate = DateTimeFormatter.ISO_LOCAL_DATE;
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = isoLocalDate.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = isoLocalDate.parse(format);

        // 不格式化：2023-02-20T09:07:06.374653300
        System.out.println(localDateTime);
        // 格式化：2023-02-20；
        System.out.println(format);
        // 解析：{},ISO resolved to 2023-02-20
        System.out.println(parse);
    }

    /**
     * 2. 本地化相关的格式。如：ofLocalizedDateTime(FormatStyle.LONG)
     */
    @Test
    public void test02(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        // java.time.ZoneId.systemDefault()：获取系统默认时区
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.LONG).withZone(ZoneId.systemDefault());
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = dateTimeFormatter.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = dateTimeFormatter.parse(format);

        // 不格式化：2023-02-20T09:25:20.183983500
        System.out.println(localDateTime);
        // 格式化：2023年2月20日 CST 09:25:20
        System.out.println(format);
        // 解析：{InstantSeconds=1676906720},ISO,America/Chicago,0 resolved to 2023-02-20T09:25:20
        System.out.println(parse);
    }

    /**
     * 3. 自定义的格式。如：ofPattern("yyyy-MM-dd hh:mm:ss")
     */
    @Test
    public void test03(){
        // 实例化 LocalDateTime
        LocalDateTime localDateTime = LocalDateTime.now();

        // 实例化 DateTimeFormatter
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss");
        // format(TemporalAccessor t) 	格式化一个日期、时间，返回字符串；时间 -> 字符串
        String format = dateTimeFormatter.format(localDateTime);
        // parse(CharSequence text)	将指定格式的字符序列解析为一个日期、时间；字符串 -> 时间
        TemporalAccessor parse = dateTimeFormatter.parse(format);

        // 不格式化：2023-02-20T09:31:02.432417900
        System.out.println(localDateTime);
        // 格式化：2023-02-20 09:31:02
        System.out.println(format);
        // 解析：{SecondOfMinute=2, MicroOfSecond=0, MinuteOfHour=31, NanoOfSecond=0, HourOfAmPm=9, MilliOfSecond=0},ISO resolved to 2023-02-20
        System.out.println(parse);
    }

}
```

### ⑥、其它 API

| 方法 | 描述 |
| --- | --- |
| `ZoneId` | 该类中包含了所有的时区信息，一个时区的 ID，如 Europe/Paris；systemDefault() 为系统默认时区 |
| `ZonedDateTime` | 一个在 ISO-8601 日历系统时区的日期时间，如 2007-12-03T10:15:30+01:00 Europe/Paris<br/>其中每个时区都对应着 ID，地区 ID 都为“{区域}/{城市}”的格式，例如：Asia/Shanghai 等 |
| `Clock` | 使用时区提供对当前即时、日期和时间的访问的时钟。 |
| 持续时间 `Duration` | 用于计算两个“时间”间隔 |
| 日期间隔 `Period` | 用于计算两个“日期:间隔 |
| `TemporalAdjuster` | 时间校正器。有时我们可能需要获取例如：将日期调整到“下一个工作日”等操作。 |
| `TemporalAdjusters` | 该类通过静态方法(`firstDayOfXxx()`/`lastDayOfXxx()`/`nextXxx()`)提供了大量的常用 `TemporalAdjuster` 的实现. |

```java
//ZoneId:类中包含了所有的时区信息
// ZoneId的getAvailableZoneIds():获取所有的ZoneId
Set<String> zoneIds = ZoneId.getAvailableZoneIds();
for (String s : zoneIds) {
    System.out.println(s);
}
// ZoneId的of():获取指定时区的时间
LocalDateTime localDateTime = LocalDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(localDateTime);
//ZonedDateTime:带时区的日期时间
// ZonedDateTime的now():获取本时区的ZonedDateTime对象
ZonedDateTime zonedDateTime = ZonedDateTime.now();
System.out.println(zonedDateTime);
// ZonedDateTime的now(ZoneId id):获取指定时区的ZonedDateTime对象
ZonedDateTime zonedDateTime1 = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
System.out.println(zonedDateTime1);

//Duration:用于计算两个“时间”间隔，以秒和纳秒为基准
LocalTime localTime = LocalTime.now();
LocalTime localTime1 = LocalTime.of(15, 23, 32);
//between():静态方法，返回Duration对象，表示两个时间的间隔
Duration duration = Duration.between(localTime1, localTime);
System.out.println(duration);
System.out.println(duration.getSeconds());
System.out.println(duration.getNano());
LocalDateTime localDateTime = LocalDateTime.of(2016, 6, 12, 15, 23, 32);
LocalDateTime localDateTime1 = LocalDateTime.of(2017, 6, 12, 15, 23, 32);
Duration duration1 = Duration.between(localDateTime1, localDateTime);
System.out.println(duration1.toDays());

//Period:用于计算两个“日期”间隔，以年、月、日衡量
LocalDate localDate = LocalDate.now();
LocalDate localDate1 = LocalDate.of(2028, 3, 18);
Period period = Period.between(localDate, localDate1);
System.out.println(period);
System.out.println(period.getYears());
System.out.println(period.getMonths());
System.out.println(period.getDays());
Period period1 = period.withYears(2);
System.out.println(period1);

// TemporalAdjuster:时间校正器
// 获取当前日期的下一个周日是哪天？
TemporalAdjuster temporalAdjuster = TemporalAdjusters.next(DayOfWeek.SUNDAY);
LocalDateTime localDateTime = LocalDateTime.now().with(temporalAdjuster);
System.out.println(localDateTime);
// 获取下一个工作日是哪天？
LocalDate localDate = LocalDate.now().with(new TemporalAdjuster() {
    @Override
    public Temporal adjustInto(Temporal temporal) {
        LocalDate date = (LocalDate) temporal;
        if (date.getDayOfWeek().equals(DayOfWeek.FRIDAY)) {
            return date.plusDays(3);
        } else if (date.getDayOfWeek().equals(DayOfWeek.SATURDAY)) {
            return date.plusDays(2);
        } else {
            return date.plusDays(1);
        }
    }
});
System.out.println("下一个工作日是：" + localDate);
```

### ⑦、与传统日期处理的转换

| 类 | To 遗留类 | To 遗留类 |
| --- | --- | --- |
| `java.time.Instant`与`java.util.Date` | Date.from(instant) | date.toInstant() |
| `java.time.Instant`与`java.sql.Timestamp` | Timestamp.from(instant) | timestamp.toInstant() |
| `java.time.ZonedDateTime`与`java.util.GregorianCalendar` | GregorianCalendar.from(zonedDateTime) | cal.toZonedDateTime() |
| `java.time.LocalDate`与`java.sql.Time` | Date.valueOf(localDate) | date.toLocalDate() |
| `java.time.LocalTime`与`java.sql.Time` | Date.valueOf(localDate) | date.toLocalTime() |
| `java.time.LocalDateTime`与`java.sql.Timestamp` | Timestamp.valueOf(localDateTime) | timestamp.toLocalDateTime() |
| `java.time.ZoneId`与`java.util.TimeZone` | Timezone.getTimeZone(id) | timeZone.toZoneId() |
| `java.time.format.DateTimeFormatter`与`java.text.DateFormat` | formatter.toFormat() | 无 |

## 7、接口的默认方法和静态方法

## 8、Nashorn、JavaScript 引擎

## 9、Base64

# 二十二、

# 二十三、

# 二十四、

# 二十五、

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

