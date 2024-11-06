# 一、JDBC概述

## 1、数据的持久化

1. 持久化(persistence)：<font color="red">把数据保存到可掉电式存储设备中以供之后使用</font>。大多数情况下，特别是企业级应用，<font color="red">数据持久化意味着将内存中的数据保存到硬盘上</font>加以“固化”，<font color="red">而持久化的实现过程大多通过各种关系数据库来完成</font>。
2. 持久化的主要应用是将内存中的数据存储在关系型数据库中，当然也可以存储在磁盘文件、XML数据文件中。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F01、数据的持久化.png)

## 2、Java 中的数据存储技术

1. 在Java中，数据库存取技术可分为如下几类：
	1. <font color="red">JDBC</font>直接访问数据库
	2. JDO (Java Data Object )技术
	3. <font color="red">第三方O/R工具</font>，如Hibernate, Mybatis 等
2. JDBC是java访问数据库的基石，JDO、Hibernate、MyBatis等只是更好的封装了JDBC。

## 3、JDBC介绍

1. JDBC(Java Database Connectivity)是一个<font color="red">独立于特定数据库管理系统、通用的SQL数据库存取和操作的公共接口</font>（一组API），定义了用来访问数据库的标准Java类库，（java.sql,javax.sql）使用这些类库可以以一种<font color="red">标准</font>的方法、方便地访问数据库资源。
2. JDBC为访问不同的数据库提供了一种<font color="red">统一的途径</font>，为开发者屏蔽了一些细节问题。
3. JDBC的目标是使Java程序员使用JDBC可以连接任何<font color="red">提供了JDBC驱动程序</font>的数据库系统，这样就使得程序员无需对特定的数据库系统的特点有过多的了解，从而大大简化和加快了开发过程。
4. 如果没有 JDBC，那么 Java 程序访问数据库时是这样的：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F02、如果没有JDBC，那么Java程序访问数据库时是这样的.png)

5. 有了 JDBC，Java 程序访问数据库时是这样的：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F03、有了JDBC，Java程序访问数据库时是这样的.png)

6. 总结如下：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F04、JDBC总结如下.png)

## 4、JDBC 体系结构
1. JDBC接口（API）包括两个层次：
	1. <font color="red">面向应用的 API</font>：Java API，抽象接口，供应用程序开发人员使用（连接数据库，执行 SQL 语句，获得结果）。
	2. <font color="red">面向数据库的 API</font>：Java Driver API，供开发商开发数据库驱动程序用。
2. JDBC 是 sun 公司提供一套用于数据库操作的接口，java 程序员只需要面向这套接口编程即可。
3. 不同的数据库厂商，需要针对这套接口，提供不同实现。不同的实现的集合，即为不同数据库的驱动：面向接口编程

## 5、JDBC 程序编写步骤

- 补充：ODBC(Open Database Connectivity，开放式数据库连接)，是微软在Windows平台下推出的。使用者在程序中只需要调用ODBC API，由 ODBC 驱动程序将调用转换成为对特定的数据库的调用请求。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F05、JDBC程序编写步骤.png)

# 二、获取数据库连接

## 1、要素一：Driver 接口实现类

### 1、Driver接口介绍

1. `java.sql.Driver` 接口是所有 JDBC 驱动程序需要实现的接口。这个接口是提供给数据库厂商使用的，不同数据库厂商提供不同的实现。
2. 在程序中不需要直接去访问实现了 Driver 接口的类，而是由驱动程序管理器类(java.sql.DriverManager)去调用这些Driver实现。
	1. Oracle的驱动：`oracle.jdbc.driver.OracleDriver`
	2. mySql的驱动： `com.mysql.jdbc.Driver`

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F06、JDBC驱动.png)

3. 将上述 jar 包拷贝到 Java 工程的一个目录中，习惯上新建一个 lib 文件夹。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F07、将上述jar包拷贝到Java工程的一个目录中，习惯上新建一个lib文件夹.png)

4. 在驱动 jar 上右键 --> Build Path --> Add to Build Path

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F08、导入jar包%201.png)

5. 注意：如果是 Dynamic Web Project（动态的web项目）话，则是把驱动 jar 放到 WebContent（有的开发工具叫 WebRoot）目录中的 WEB-INF 目录中的 lib 目录下即可

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F09、如果是DynamicWebProject（动态的web项目）话，则是把驱动jar放到WebContent目录中的WEB-INF下.png)

### 2、加载与注册JDBC驱动

1. 加载驱动：加载 JDBC 驱动需调用 Class 类的静态方法 `forName()`，向其传递要加载的 JDBC 驱动的类名

```java
Class.forName("com.mysql.jdbc.Driver")
```

2. 注册驱动：DriverManager 类是驱动程序管理器类，负责管理驱动程序

```java
DriverManager.registerDriver(com.mysql.jdbc.Driver)
```

3. 通常不用显式调用 DriverManager 类的 `registerDriver()` 方法来注册驱动程序类的实例，因为 Driver 接口的驱动程序类都包含了静态代码块，在这个静态代码块中，会调用 `DriverManager.registerDriver()` 方法来注册自身的一个实例。下图是 MySQL 的 Driver 实现类的源码：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F10、MySQL的Driver实现类的源码.png)

## 2、要素二：URL

### 1、URL说明

1. JDBC URL 用于标识一个被注册的驱动程序，驱动程序管理器通过这个 URL 选择正确的驱动程序，从而建立到数据库的连接。
2. JDBC URL的标准由三部分组成，各部分间用冒号分隔。
	1. <font color="red">jdbc</font>:<font color="red">子协议</font>:<font color="red">子名称</font>
	2. <font color="red">协议</font>：JDBC URL 中的协议总是 jdbc
	3. <font color="red">子协议</font>：子协议用于标识一个数据库驱动程序
	4. <font color="red">子名称</font>：一种标识数据库的方法。子名称可以依不同的子协议而变化，用子名称的目的是为了定位数据库提供足够的信息。包含主机名(对应服务端的ip地址)，端口号，数据库名
3. 举例：

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F11、JDBCURL举例.png)

### 2、几种常用数据库的 JDBC URL

1. MySQL 的连接 URL 编写方式：
	1. `jdbc:mysql://主机名称:mysql服务端口号/数据库名称?参数=值&参数=值`
	2. `jdbc:mysql://localhost:3306/atguigu`
	3. `jdbc:mysql://localhost:3306/atguigu?useUnicode=true&characterEncoding=utf8`（如果 JDBC 程序与服务器端的字符集不一致，会导致乱码，那么可以通过参数指定服务器端的字符集）
	4. `jdbc:mysql://localhost:3306/atguigu?user=root&password=123456`
2. Oracle 9i 的连接 URL 编写方式：
	1. `jdbc:oracle:thin:@主机名称:oracle服务端口号:数据库名称`
	2. `jdbc:oracle:thin:@localhost:1521:atguigu`
3. SQLServer 的连接 URL 编写方式：
	1. `jdbc:sqlserver://主机名称:sqlserver服务端口号:DatabaseName=数据库名称`
	2. `jdbc:sqlserver://localhost:1433:DatabaseName=atguigu`

## 3、要素三：用户名和密码

1. user、password 可以用 `属性名=属性值` 方式告诉数据库
2. 可以调用 DriverManager 类的 `getConnection()` 方法建立到数据库的连接

## 4、数据库连接方式举例

1. 连接方式一

```java
// 获取数据库链接
// 方式一：
// 缺点：代码中显式出现了第三方数据库的API
public class Demo01 {
  public static void main(String[] args) throws SQLException {
	 // 导入MySQL的jdbc的驱动包
	 // 1、提供java.sql.Driver接口实现类的对象
	 Driver driver = new com.mysql.jdbc.Driver();

	 // 2、提供url，指明具体操作的数据
	 // jdbc：主协议
	 // mysql：子协议
	 // 152.136.229.92：IP地址
	 // 3306：端口号，MySQL默认的端口号
	 // test：数据库名
	 String url = "jdbc:mysql://152.136.229.92:3306/test";

	 // 3、提供Properties的对象，指明用户名和密码
	 // 将用户名和密码封装到Properties中
	 Properties info = new Properties();
	 info.setProperty("user","root");
	 info.setProperty("password","000123");

	 // 4、调用driver的connect()，获取连接
	 Connection conn = driver.connect(url, info);

	 System.out.println(conn);
  }
}
```

2. 连接方式二

```java
// 方式二：对方式一的迭代
// 相较于方式一，这里使用反射实例化Driver，不在代码中体现第三方数据库的API。体现了面向接口编程思想。
// 使得程序具有更好的可移植性
public class Demo02 {
  public static void main(String[] args) throws ClassNotFoundException, IllegalAccessException, InstantiationException, SQLException {
	 // 1、实例化Driver
	 Class aClass = Class.forName("com.mysql.jdbc.Driver");
	 Driver driver = (Driver) aClass.newInstance();

	 // 2、提供url，指明具体操作的数据
	 String url = "jdbc:mysql://152.136.229.92:3306/test";

	 // 3、提供Properties的对象，指明用户名和密码
	 Properties info = new Properties();
	 info.setProperty("user","root");
	 info.setProperty("password","000123");

	 // 4、调用driver的connect()，获取连接
	 Connection conn = driver.connect(url, info);

	 System.out.println(conn);
  }

}
```

3. 连接方式三

```java
// 方式三：
// 使用DriverManager实现数据库的连接。体会获取连接必要的4个基本要素。
public class Demo03 {
  public static void main(String[] args) throws ClassNotFoundException, IllegalAccessException, InstantiationException, SQLException {
	 // 1、获取Driver实现类的对象
	 Class aClass = Class.forName("com.mysql.jdbc.Driver");
	 Driver driver = (Driver) aClass.newInstance();

	 // 2、提供另外三个链接的基本信息
	 String url = "jdbc:mysql://152.136.229.92:3306/test";
	 String user = "root";
	 String password = "000123";

	 // 3、注册驱动
	 DriverManager.registerDriver(driver);

	 // 4、获取链接
	 Connection conn = DriverManager.getConnection(url,user,password);

	 System.out.println(conn);
  }
}
```

4. 连接方式四

```java
// 方式四：
// 可以只是加载驱动，不必显式的注册驱动了。
// 因为在DriverManager的源码中已经存在静态代码块，实现了驱动的注册。
public class Demo04 {
  public static void main(String[] args) throws Exception {
	 // 1、提供另外三个链接的基本信息
	 String url = "jdbc:mysql://152.136.229.92:3306/test";
	 String user = "root";
	 String password = "000123";

	 // 2、加载驱动
	 Class.forName("com.mysql.jdbc.Driver");
	 // 相较于方式三，可以省略如下的操作
	 // Driver driver = (Driver) aClass.newInstance();
	 //        // 注册驱动
	 // DriverManager.registerDriver(driver);

	 // 因为在mysql的Driver类中声明有：
	 /*
		   static {
			  try {
				 DriverManager.registerDriver(new Driver());
			  } catch (SQLException var1) {
				 throw new RuntimeException("Can't register driver!");
			  }
		   }
		*/

	 // 3、获取链接
	 Connection conn = DriverManager.getConnection(url,user,password);

	 System.out.println(conn);
  }
}
```

1. 连接方式五；`jdbc.properties` 配置文件

```java
# 配置文件中的注释以#号开头

driverClass=com.mysql.jdbc.Driver
# jdbc：主协议
# mysql：子协议
# 152.136.229.92：IP地址
# 3306：端口号，MySQL默认的端口号
# test：数据库名
# ?：后面可添加参数
# characterEncoding=utf-8：指定所处理字符的解码和编码的格式
# 若项目的字符集和MySQL数据库字符集设置为同一字符集则url可以不加此参数。
url=jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8
user=root
password=000123
```

```java
// 连接方式五(最终版)
// 将数据库链接需要的基本信息声明在配置文件中，通过读取配置文件的方式，获取链接
/*
  优点：1：实现了数据与代码的分离，实现了解耦
		2：如果需要修改配置文件信息，可以避免重新打包
*/
public class Demo05 {
  public static void main(String[] args) throws Exception {
	 // 1、读取配置文件中的4个基本信息
	 InputStream inputStream = Demo05.class.getClassLoader().getResourceAsStream("jdbc.properties");

	 Properties properties = new Properties();
	 properties.load(inputStream);

	 String driverClass = properties.getProperty("driverClass");
	 String url = properties.getProperty("url");
	 String user = properties.getProperty("user");
	 String password = properties.getProperty("password");

	 // 2、加载驱动
	 Class.forName(driverClass);

	 // 3、获取链接
	 Connection conn = DriverManager.getConnection(url, user, password);

	 System.out.println(conn);
  }
}
```

# 三、使用 PreparedStatement 实现 CRUD 操作

## 1、操作和访问数据库

1. 数据库连接被用于向数据库服务器发送命令和 SQL 语句，并接受数据库服务器返回的结果。其实一个数据库连接就是一个 Socket 连接。
2. 在 `java.sql` 包中有 3 个接口分别定义了对数据库的调用的不同方式：
	1. `Statement`：用于执行静态 SQL 语句并返回它所生成结果的对象。
	2. `PrepatedStatement`：SQL 语句被预编译并存储在此对象中，可以使用此对象多次高效地执行该语句。
	3. `CallableStatement`：用于执行 SQL 存储过程

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F12、操作和访问数据库.png)

## 2、使用 Statement 操作数据表的弊端

1. 通过调用 Connection 对象的 `createStatement()` 方法创建该对象。该对象用于执行静态的 SQL 语句，并且返回执行结果。
2. Statement 接口中定义了下列方法用于执行 SQL 语句：

```java
// 执行更新操作INSERT、UPDATE、DELETE
int excuteUpdate(String sql)
// 执行查询操作SELECT
ResultSet executeQuery(String sql)
```

3. 但是使用 Statement 操作数据表存在弊端：
	1. <font color="red">问题一：存在拼串操作，繁琐</font>
	2. <font color="red">问题二：存在SQL注入问题</font>
4. SQL 注入是利用某些系统没有对用户输入的数据进行充分的检查，而在用户输入数据中注入非法的 SQL 语句段或命令（如：`SELECT user, password FROM user_table WHERE user='a' OR 1 = ' AND password = ' OR '1'='1'`） ，从而利用系统的 SQL 引擎完成恶意行为的做法。
5. <font color="red">对于 Java 而言，要防范 SQL 注入，只要用 PreparedStatement(从Statement扩展而来) 取代 Statement 就可以了。</font>
6. 图例

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F13、用PreparedStatement取代Statement.png)

## 3、PreparedStatement 的使用

### 1、PreparedStatement 介绍

1. 可以通过调用 `Connection` 对象的 `preparedStatement(String sql)` 方法获取 `PreparedStatement` 对象
2. `PreparedStatement` 接口是 `Statement` 的子接口，它表示一条预编译过的 SQL 语句
3. `PreparedStatement` 对象所代表的 SQL 语句中的参数用问号 `?` 来表示，调用 `PreparedStatement` 对象的
4. `setXxx()` 方法来设置这些参数。`setXxx()` 方法有两个参数：
	1. 第一个参数是要设置的 SQL 语句中的参数的索引(从 1开始)
	2. 第二个是设置的 SQL 语句中的参数的值

### 2、PreparedStatement vs Statement

1. 代码的可读性和可维护性。
2. PreparedStatement 能最大可能提高性能：
	1. DBServer 会对<font color="red">预编译</font>语句提供性能优化。因为预编译语句有可能被重复调用，所以语句在被 DBServer 的编译器编译后的执行代码被缓存下来，那么下次调用时只要是相同的预编译语句就不需要编译，只要将参数直接传入编译过的语句执行代码中就会得到执行。
	2. 在 statement 语句中,即使是相同操作但因为数据内容不一样,所以整个语句本身不能匹配,没有缓存语句的意义.事实是没有数据库会对普通语句编译后的执行代码缓存。这样每执行一次都要对传入的语句编译一次。(语法检查，语义检查，翻译成二进制命令，缓存)
3. PreparedStatement 可以防止 SQL 注入

### 3、 Java 与 SQL 对应数据类型转换表

|Java类型|SQL类型|
|--|--|
|boolean|BIT|
|byte|TINYINT|
|short|SMALLINT|
|int|INTEGER|
|long|BIGINT|
|String|CHAR,VARCHAR,LONGVARCHAR|
|byte array|BINARY , VAR BINARY|
|java.sql.Date|DATE|
|java.sql.Time|TIME|
|java.sql.Timestamp|TIMESTAMP|

### 4、使用 PreparedStatement 实现增、删、改操作

1. 增：

```java
// 使用PreparedStatement替换Statement，实现对数据表的增删改查
// 因为涉及到流的关闭，所以要try-catch
public class Demo01 {
  // 向customers表中添加一条记录
  @Test
  public void test1() {

	 Connection conn = null;
	 PreparedStatement pS = null;

	 try {
		   // 1、读取配置文件中的4个基本信息
		   InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream("jdbc.properties");

		   Properties properties = new Properties();
		   properties.load(inputStream);

		   String driverClass = properties.getProperty("driverClass");
		   String url = properties.getProperty("url");
		   String user = properties.getProperty("user");
		   String password = properties.getProperty("password");

		   // 2、加载驱动
		   Class.forName(driverClass);

		   // 3、获取连接
		   conn = DriverManager.getConnection(url, user, password);

		   // 4、预编译sql语句，返回PrepareStatement的实例
		   // ?：占位符
		   String sql = "INSERT INTO customers(name,email,birth) VALUES(?,?,?)";
		   pS = conn.prepareStatement(sql);

		   // 5、填充占位符
		   pS.setString(1,"哪吒");
		   pS.setString(2,"nezha@gmail.com");
		   // 获取日期实例
		   SimpleDateFormat sDF = new SimpleDateFormat("yyyy-MM-dd");
		   // 给日期赋值
		   Date date = sDF.parse("1000-01-01");
		   pS.setDate(3, (new java.sql.Date(date.getTime())));

		   // 6、执行操作
		   pS.execute();
	 } catch (IOException e) {
		   e.printStackTrace();
	 } catch (ClassNotFoundException e) {
		   e.printStackTrace();
	 } catch (SQLException throwables) {
		   throwables.printStackTrace();
	 } catch (ParseException e) {
		   e.printStackTrace();
	 } finally {
		   if(pS != null){
			  // 7、资源的关闭
			  try {
				 pS.close();
			  } catch (SQLException throwables) {
				 throwables.printStackTrace();
			  }
		   }

		   if(conn != null){
			  try {
				 conn.close();
			  } catch (SQLException throwables) {
				 throwables.printStackTrace();
			  }
		   }
	 }

  }
}
```

2. <font color="red">因为创建链接和关闭资源都是固定的重复操作，所以创建这两个操作的工具类：</font>

```java
// 工具类一般设置为静态方法
public class JDBCUtils {

  /**
  * 获取数据库连接
  * @return
  * @throws Exception
  */
  public static Connection getConnection() throws Exception {
	 // 1、读取配置文件中的4个基本信息
	 InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream("jdbc.properties");
	 // 创建Properties的对象
	 Properties properties = new Properties();
	 // 调用Properties的load()方法，从方法加载数据
	 properties.load(inputStream);
	 // 从文件获取数据并赋值
	 String driverClass = properties.getProperty("driverClass");
	 String url = properties.getProperty("url");
	 String user = properties.getProperty("user");
	 String password = properties.getProperty("password");

	 // 2、加载驱动
	 Class.forName(driverClass);

	 // 3、获取连接
	 Connection conn = DriverManager.getConnection(url, user, password);

	 // 返回Connection（数据库源连接）对象
	 return conn;
  }

  /**
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

}
```

3. 改，调用自己封装的数据库连接和关闭数据库连接的方法：

```java
// 修改customers表的一条记录
@Test
public void test2() throws Exception {

	Connection conn = null;
	PreparedStatement ps = null;

	try {
		// 1、获取数据库的连接
		// 调用我们自己封装的获取数据库连接的静态方法
		conn = JDBCUtils.getConnection();

		// 2、预编译sql语句，返回PrepareStatement的实例
		String sql = "UPDATE customers SET name = ? WHERE id=?";
		ps = conn.prepareStatement(sql);

		// 3、填充占位符
		ps.setObject(1,"言");
		ps.setObject(2,"22");

		// 4、执行
		ps.execute();
	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		// 5、资源的关闭
		// 调用我们自己封装的关闭数据库连接的静态方法
		// 此处不用try-catch，closeResource已经进行处理了
		JDBCUtils.closeResource(conn,ps);
	}

}
```

4. <font color="red">3 中，除了设置 sql 语句和具体的填充占位符外，也都是固定的重复操作，所以可以进一步封装，原本 2 中的 JDBCUtils 修改为：</font>

```java
// 工具类一般设置为静态方法
public class JDBCUtils {

  /**
  * 获取数据库连接
  * @return
  * @throws Exception
  */
  public static Connection getConnection() throws Exception {
	 // 1、读取配置文件中的4个基本信息
	 InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream("jdbc.properties");
	 // 创建Properties的对象
	 Properties properties = new Properties();
	 // 调用Properties的load()方法，从方法加载数据
	 properties.load(inputStream);
	 // 从文件获取数据并赋值
	 String driverClass = properties.getProperty("driverClass");
	 String url = properties.getProperty("url");
	 String user = properties.getProperty("user");
	 String password = properties.getProperty("password");

	 // 2、加载驱动
	 Class.forName(driverClass);

	 // 3、获取连接
	 Connection conn = DriverManager.getConnection(url, user, password);

	 // 返回Connection（数据库源连接）对象
	 return conn;
  }

  /**
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

  // 通用的增删改操作
  // 参数1：sql语句，参数2：填充占位符的具体数值
  // Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
  // sql中占位符的个数与可变形参的长度相同
  public static void update(String sql,Object ...args) {

	 Connection conn = null;
	 PreparedStatement ps = null;

	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = getConnection();
		   // 2、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);
		   // 3、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }
		   // 4、执行
		   ps.execute();
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 5、关闭资源
		   // 调用我们自己封装的关闭数据库连接的静态方法
		   // 此处不用try-catch，closeResource已经进行处理了
		   closeResource(conn,ps);
	 }

  }

}
```

5. 改，调用自己封装的通用的增删改操作：

```java
// 删
// 测试通用的增删改操作方法
@Test
public void test3(){
	// 具体的sql语句
	String sql = "DELETE FROM customers WHERE id=?";

	// 调用我们自己封装的通用的增删改操作的静态方法
	// 参数1：sql语句，参数2：填充占位符的具体数值
	JDBCUtils.update(sql,22);

}
```

### 5、使用PreparedStatement实现查询操作

1. 因为增删改和查询的关闭资源方法所需传入的参数不一样，所以要在工具类 JDBCUtils 中再添加一个专属于查询的关闭资源的方法

```java
/**
 * 查询的关闭操作，方法的重载
 * 关闭数据库连接和Statement的操作
 * @param conn
 * @param ps
 */
public static void closeResource(Connection conn, PreparedStatement ps, ResultSet rs){

	if(ps != null){
		try {
			ps.close();
		} catch (SQLException throwables) {
			throwables.printStackTrace();
		}
	}

	if(conn != null){
		try {
			conn.close();
		} catch (SQLException throwables) {
			throwables.printStackTrace();
		}
	}

	if(rs != null){
		try {
			rs.close();
		} catch (SQLException throwables) {
			throwables.printStackTrace();
		}
	}

}
```

2. 查，调用自己封装的数据库连接和关闭数据库连接的方法；对应数据库 customers 表的 Customers 类

```java
/**
*  ORM编程思想：（object relational mapping）
*  一个数据表对应一个java类
*  表中的一条记录对应java类中的一个对象
*  表中的一个字段对应java类中的一个属性
*/
public class Customers {
 // 对应的属性
 private int id;
 private String name;
 private String email;
 // 对应数据库表的时间数据类型应是java.sql.Date
 private Date birth;

 public Customers() { }
 public Customers(int id, String name, String email, Date birth) {
	this.id = id;
	this.name = name;
	this.email = email;
	this.birth = birth;
 }

 public int getId() { return id; }
 public String getName() { return name; }
 public void setName(String name) { this.name = name; }
 public String getEmail() { return email; }
 public void setEmail(String email) { this.email = email; }
 public Date getBirth() { return birth; }
 public void setBirth(Date birth) { this.birth = birth; }

 @Override
 public String toString() {
	return "Customers{" +
			 "id=" + id +
			 ", name='" + name + '\'' +
			 ", email='" + email + '\'' +
			 ", birth=" + birth +
			 '}';
 }

 public void setId(int id) {
	this.id = id;
 }
}
```
   
3. 针对于 customers 表的查询操作

```java
// 针对于customers表的查询操作
public class CustomersForQuery {

 @Test
 public void test() throws Exception {

	Connection conn = null;
	PreparedStatement ps = null;
	ResultSet resultSet = null;

	try {
		  // 1、获取数据库的连接
		  // 调用我们自己封装的获取数据库连接的静态方法
		  conn = JDBCUtils.getConnection();

		  // 2、预编译sql语句，返回PrepareStatement的实例
		  String sql = "SELECT id,name,email,birth FROM customers WHERE id=?";
		  ps = conn.prepareStatement(sql);

		  // 3、填充占位符
		  ps.setInt(1,1);

		  // 4、执行，并返回查询到的结果集
		  resultSet = ps.executeQuery();

		  // 5、处理结果集
		  // 判断结果集的下一条是否有数据，如果有数据返回true，并指针下移，
		  // 如果返回false，指针不会下移
		  if(resultSet.next()){
			 // 获取当前这条数据的各个字段值
			 int id = resultSet.getInt(1);
			 String name = resultSet.getString(2);
			 String email = resultSet.getString(3);
			 Date birth = resultSet.getDate(4);

			 // 方式一：直接打印
			 // System.out.println("id：" + id + "，name：" + name + "，email：" + email + "，birth：" + birth);

			 // 方式二：封装到数组中
			 // Object data = new Object[]{id,name,email,birth};

			 // 方式三：封装到对象里（推荐）
			 // 创建Customers类
			 Customers customers = new Customers(id,name,email,birth);
			 System.out.println(customers);
		  }
	} catch (Exception e) {
		  e.printStackTrace();
	} finally {
		  // 6、关闭资源
		  // 调用我们自己封装的关闭数据库连接的静态方法
		  // 此处不用try-catch，closeResource已经进行处理了
		  JDBCUtils.closeResource(conn,ps,resultSet);
	}

 }

}
```

## 4、ResultSet 与 ResultSetMetaData

### 1、ResultSet

1. 查询需要调用 PreparedStatement 的 `executeQuery()` 方法，查询结果是一个 ResultSet 对象
2. ResultSet 对象以逻辑表格的形式封装了执行数据库操作的结果集，ResultSet 接口由数据库厂商提供实现
3. ResultSet 返回的实际上就是一张数据表。有一个指针指向数据表的第一条记录的前面。
4. ResultSet 对象维护了一个指向当前数据行的游标，初始的时候，游标在第一行之前，可以通过 `ResultSet` 对象的 `next()` 方法移动到下一行。调用 `next()` 方法检测下一行是否有效。若有效，该方法返回 `true`，且指针下移。相当于 Iterator 对象的 `hasNext()` 和 `next()` 方法的结合体。
5. 当指针指向一行时, 可以通过调用 `getXxx(int index)` 或 `getXxx(int columnName)` 获取每一列的值。
	1. 例如: `getInt(1)`、 `getString("name")`
	2. <font color="red">注意：Java 与数据库交互涉及到的相关 Java API 中的索引都从 1 开始。</font>
6. ResultSet 接口的常用方法：
	1. boolean next()
	2. getString()
	3. …

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F14、ResultSet与ResultSetMetaData.png)

### 2、ResultSetMetaData

1. 可用于获取关于 ResultSet 对象中列的类型和属性信息的对象
2. `ResultSetMetaData meta = rs.getMetaData();`
	1. `getColumnName(int column)`：获取指定列的名称
	2. `getColumnLabel(int column)`：获取指定列的别名
	3. `getColumnCount()`：返回当前 ResultSet 对象中的列数。
	4. `getColumnTypeName(int column)`：检索指定列的数据库特定的类型名称。
	5. `getColumnDisplaySize(int column)`：指示指定列的最大标准宽度，以字符为单位。
	6. `isNullable(int column)`：指示指定列中的值是否可以为 null。
	7. `isAutoIncrement(int column)`：指示是否自动为指定列进行编号，这样这些列仍然是只读的。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F15、ResultSetMetaData.png)

3. 问题1：得到结果集后, 如何知道该结果集中有哪些列 ？ 列名是什么？
	1. 需要使用一个描述 ResultSet 的对象， 即 ResultSetMetaData
4. 问题2：关于ResultSetMetaData
	1. 如何获取 ResultSetMetaData： 调用 ResultSet 的 getMetaData() 方法即可
	2. 获取 ResultSet 中有多少列：调用 ResultSetMetaData 的 getColumnCount() 方法
	3. 获取 ResultSet 每一列的列的别名是什么：调用 ResultSetMetaData 的getColumnLabel() 方法
5. 查询操作的流程

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F16、ResultSetMetaData2.png)

### 3、使用 ResultSet 与 ResultSetMetaData 的查询方法举例

1. <font color="red">上面封装的 JDBCUtils 工具类中，除了设置 sql 语句和具体的填充占位符外，也都是固定的重复操作，所以可以进一步封装，增加针对于 customers 表的通用的查询操作，JDBCUtils 修改为：</font>

```java
// 工具类一般设置为静态方法
public class JDBCUtils {

  /**
  * 获取数据库连接
  * @return
  * @throws Exception
  */
  public static Connection getConnection() throws Exception {
	 // 1、读取配置文件中的4个基本信息
	 InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream("jdbc.properties");
	 // 创建Properties的对象
	 Properties properties = new Properties();
	 // 调用Properties的load()方法，从方法加载数据
	 properties.load(inputStream);
	 // 从文件获取数据并赋值
	 String driverClass = properties.getProperty("driverClass");
	 String url = properties.getProperty("url");
	 String user = properties.getProperty("user");
	 String password = properties.getProperty("password");

	 // 2、加载驱动
	 Class.forName(driverClass);

	 // 3、获取连接
	 Connection conn = DriverManager.getConnection(url, user, password);

	 // 返回Connection（数据库源连接）对象
	 return conn;
  }

  /**
  * 增删改的关闭操作
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

  // 通用的增删改操作
  // 参数1：sql语句，参数2：填充占位符的具体数值
  // Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
  // sql中占位符的个数与可变形参的长度相同
  public static void update(String sql,Object ...args) {

	 Connection conn = null;
	 PreparedStatement ps = null;

	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = getConnection();
		   // 2、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);
		   // 3、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }
		   // 4、执行
		   ps.execute();
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 5、关闭资源
		   // 调用我们自己封装的关闭数据库连接的静态方法
		   // 此处不用try-catch，closeResource已经进行处理了
		   closeResource(conn,ps);
	 }

  }

  /**
  * *************************************************
  */

  /**
  * 查询的关闭操作，方法的重载
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps, ResultSet rs){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(rs != null){
		   try {
			  rs.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

  // 针对于customers表的通用的查询操作，返回一个对象
  // 参数1：sql语句，参数2：填充占位符的具体数值
  // Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
  // sql中占位符的个数与可变形参的长度相同
  public static Customers queryDorCustomers(String sql,Object ...args) {

	 Connection conn = null;
	 PreparedStatement ps = null;
	 ResultSet rs = null;

	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();

		   // 2、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);

		   // 3、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }

		   // 4、执行，并返回查询到的结果集
		   rs = ps.executeQuery();
		   // 获取结果集的元数据：ResultSetMetaData
		   ResultSetMetaData rsMetaData = rs.getMetaData();
		   // 可通过ResultSetMetaData获取结果集中的列数
		   // 就是查询到的一行数据中，有几个数据
		   int columnCount = rsMetaData.getColumnCount();

		   // 5、处理结果集
		   // resultSet.next()：判断结果集的下一条是否有数据，
		   // 如果有数据返回true，并指针下移，如果返回false，指针不会下移
		   if(rs.next()){
			  // 因为是查询的customers表，所以创建Customers的对象
			  Customers customers = new Customers();
			  // 可通过ResultSetMetaData获取结果集中的列数
			  // 所以通过ResultSetMetaData判断循环次数
			  // 处理结果集一行数据中的每一个列
			  for (int i = 0; i < columnCount; i++) {
				 // 获取每个列的列名
				 String columnName = rsMetaData.getColumnName(i + 1);

				 // 获取每个列的值
				 Object columnValue = rs.getObject(i + 1);

				 // 给customers对象指定的columnName属性，赋值为columnValue
				 // 通过反射
				 // 通过传入的columnName（列名）来获得Customers对象中对应的属性
				 Field field = Customers.class.getDeclaredField(columnName);
				 // 不确定属性的权限，所以调用setAccessible()并设置为ture
				 field.setAccessible(true);
				 // 将customers对象中名称为columnName的属性赋值为columnValue
				 field.set(customers,columnValue);
			  }
			  // 返回已经被赋值完的customers对象
			  return customers;
		   }
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 6、关闭资源
		   // 调用我们自己封装的获取数据库连接的静态方法
		   JDBCUtils.closeResource(conn,ps,rs);
	 }
	 // resultSet.next()：判断结果集的下一条是否有数据，
	 // 如果有数据返回true，并指针下移，如果返回false，指针不会下移
	 // 没有数据，返回null
	 return null;
  }

}
```

2. 调用针对于 customers 表的通用的查询操作方法

```java
// 针对于customers表的通用的查询操作的测试
@Test
public void test1(){
	// 编写sql语句
	String sql = "SELECT id,name,email,birth FROM customers WHERE id=?";
	// 调用针对于customers表的通用的查询操作方法，传入sql语句和占位符参数
	Customers customers = JDBCUtils.queryDorCustomers(sql, 1);
	// 打印返回的对象
	System.out.println(customers);
}
```

3. 针对于 order 表的通用的查询操作
	1. 针对于表的字段名与类的属性名不相同的情况：
		1. 必须在声明sql时，使用类的属性名来命名字段的别名
		2. 使用ResultSetMetaData时，需要使用getColumnLabel来替换getColumnName()来获取列的别名
		3. 说明：如果sql中没有给字段起别名，getColumnLabel()获取的就是列名
	2. 对应order表的Order类

```java
/**
*  ORM编程思想：（object relational mapping）
*  一个数据表对应一个java类
*  表中的一条记录对应java类中的一个对象
*  表中的一个字段对应java类中的一个属性
*/

// 对应order表的Order类
public class Order {
 /**
 * 数据库表中的字段名是带有下划线的，但是在Java属性中不能这么命名
 * 但是这样会导致查询时数据库返回的字段名与这个类的属性不匹配
 * 解决方法：查询sql的语句起一个别名，让别名和这个类的属性名相同
 * 同时，工具类中不再使用rsMetaData.getColumnName(i + 1);获取列名
 * 因为通过他获取的是表中真正的列名，而不是我们给起的别名
 * 改为使用获取列的别名的方法：rsMetaData.getColumnLabel(i + 1);
 * 若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
 */
 // 对应的属性
 private int orderId;
 private String orderName;
 private Date orderDate;

 public Order() { }
 public Order(int orderId, String orderName, Date orderDate) {
	this.orderId = orderId;
	this.orderName = orderName;
	this.orderDate = orderDate;
 }

 public int getOrderId() { return orderId; }
 public void setOrderId(int orderId) { this.orderId = orderId; }
 public String getOrderName() { return orderName; }
 public void setOrderName(String orderName) { this.orderName = orderName; }
 public Date getOrderDate() { return orderDate; }
 public void setOrderDate(Date orderDate) { this.orderDate = orderDate; }

 @Override
 public String toString() {
	return "Order{" +
			 "orderId=" + orderId +
			 ", orderName='" + orderName + '\'' +
			 ", orderDate=" + orderDate +
			 '}';
 }
}
```
   
4.  <font color="red">JDBCUtils 工具类中新加的针对于 order 表的通用的查询操作</font>

```java
// 针对于order表的通用的查询操作，返回一个对象
// 参数1：sql语句，参数2：填充占位符的具体数值
// Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
// sql中占位符的个数与可变形参的长度相同
public static Order queryDorOrder(String sql,Object ...args) {

 Connection conn = null;
 PreparedStatement ps = null;
 ResultSet rs = null;

 try {
	   // 1、获取数据库的连接
	   // 调用我们自己封装的获取数据库连接的静态方法
	   conn = JDBCUtils.getConnection();

	   // 2、预编译sql语句，返回PrepareStatement的实例
	   ps = conn.prepareStatement(sql);

	   // 3、填充占位符
	   for (int i = 0; i < args.length; i++) {
		  // 小心参数声明错误
		  ps.setObject(i + 1,args[i]);
	   }

	   // 4、执行，并返回查询到的结果集
	   rs = ps.executeQuery();
	   // 获取结果集的元数据：ResultSetMetaData
	   ResultSetMetaData rsMetaData = rs.getMetaData();
	   // 可通过ResultSetMetaData获取结果集中的列数
	   // 就是查询到的一行数据中，有几个数据
	   int columnCount = rsMetaData.getColumnCount();

	   // 5、处理结果集
	   // resultSet.next()：判断结果集的下一条是否有数据，
	   // 如果有数据返回true，并指针下移，如果返回false，指针不会下移
	   if(rs.next()){
		  // 因为是查询的order表，所以创建Order的对象
		  Order order = new Order();
		  // 可通过ResultSetMetaData获取结果集中的列数
		  // 所以通过ResultSetMetaData判断循环次数
		  // 处理结果集一行数据中的每一个列
		  for (int i = 0; i < columnCount; i++) {
			 /*
			 获取每个列的列名
			 此处不再使用rsMetaData.getColumnName(i + 1);获取列名
			 因为通过他获取的是表中真正的列名，而不是我们给起的别名
			 改为使用获取列的别名的方法：
			 若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
				*/
			 String columnLabel = rsMetaData.getColumnLabel(i + 1);

			 // 获取每个列的值
			 Object columnValue = rs.getObject(i + 1);

			 // 给Order对象指定的columnLabel属性，赋值为columnValue
			 // 通过反射
			 // 通过传入的columnLabel（别名）来获得Order对象中对应的属性
			 Field field = Order.class.getDeclaredField(columnLabel);
			 // 不确定属性的权限，所以调用setAccessible()并设置为ture
			 field.setAccessible(true);
			 // 将Order对象中别名为columnLabel的属性赋值为columnValue
			 field.set(order,columnValue);
		  }
		  // 返回已经被赋值完的customers对象
		  return order;
	   }

 } catch (Exception e) {
	   e.printStackTrace();
 } finally {
	   // 6、关闭资源
	   // 调用我们自己封装的获取数据库连接的静态方法
	   JDBCUtils.closeResource(conn,ps,rs);

 }
 return null;
}
```
   
5. 针对于 order 表的通用的查询操作的测试

```java
// 针对于order表的通用的查询操作的测试
@Test
public void test2(){
 // 编写sql语句
 // 这个表的表明order是关键字，所以要用··（反单引号，TAP键上面的）包起来
 String sql = "SELECT order_id orderId,order_name orderName,order_date orderDate FROM `order` WHERE order_id=?";
 // 调用针对于order表的通用的查询操作方法，传入sql语句和占位符参数
 Order order = JDBCUtils.queryDorOrder(sql, 1);
 // 打印返回的对象
 System.out.println(order);
}
```

## 5、资源的释放

1. 释放 ResultSet、Statement、Connection
2. 数据库连接（Connection）是非常稀有的资源，用完后必须马上释放，如果 Connection 不能及时正确的关闭将导致系统宕机。Connection 的使用原则是<font color="red">尽量晚创建，尽量早的释放</font>。
3. 可以在 finally 中关闭，保证及时其他代码出现异常，资源也一定能被关闭。

## 6、使用 PreparedStatement 实现针对于不同表的通用的查询操作

1. <font color="red">自己封装的 JDBCUtils 工具类中，针对于不同表的通用的查询操作，返回表中的一条记录</font>

```java
// 使用PreparedStatement实现针对于不同表的通用的查询操作，泛型方法
// 返回表中的一条记录
// 參數1：泛型，表明传进来的是什么类
// 参数2：sql语句，参数3：填充占位符的具体数值
// Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
// sql中占位符的个数与可变形参的长度相同
public static <T> T getInstance(Class<T> clazz,String sql,Object ...args){

	Connection conn = null;
	PreparedStatement ps = null;
	ResultSet rs = null;

	try {
		// 1、获取数据库的连接
		// 调用我们自己封装的获取数据库连接的静态方法
		conn = JDBCUtils.getConnection();

		// 2、预编译sql语句，返回PrepareStatement的实例
		ps = conn.prepareStatement(sql);

		// 3、填充占位符
		for (int i = 0; i < args.length; i++) {
			// 小心参数声明错误
			ps.setObject(i + 1,args[i]);
		}

		// 4、执行，并返回查询到的结果集
		rs = ps.executeQuery();
		// 获取结果集的元数据：ResultSetMetaData
		ResultSetMetaData rsMetaData = rs.getMetaData();
		// 可通过ResultSetMetaData获取结果集中的列数
		// 就是查询到的一行数据中，有几个数据
		int columnCount = rsMetaData.getColumnCount();

		// 5、处理结果集
		// resultSet.next()：判断结果集的下一条是否有数据，
		// 如果有数据返回true，并指针下移，如果返回false，指针不会下移
		if(rs.next()){
			// 通过反射创建传进来的类的对象
			T t = clazz.newInstance();
			// 可通过ResultSetMetaData获取结果集中的列数
			// 所以通过ResultSetMetaData判断循环次数
			// 处理结果集一行数据中的每一个列
			for (int i = 0; i < columnCount; i++) {
				/*
				获取每个列的列名
				此处不再使用rsMetaData.getColumnName(i + 1);获取列名
				因为通过他获取的是表中真正的列名，而不是我们给起的别名
				改为使用获取列的别名的方法：
				若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
				 */
				String columnLabel = rsMetaData.getColumnLabel(i + 1);

				// 获取每个列的值
				Object columnValue = rs.getObject(i + 1);

				// 给t对象指定的columnLabel属性，赋值为columnValue
				// 通过反射
				// 通过传入的columnLabel（别名）来获得t对象中对应的属性
				Field field = clazz.getDeclaredField(columnLabel);
				// 不确定属性的权限，所以调用setAccessible()并设置为ture
				field.setAccessible(true);
				// 将t对象中别名为columnLabel的属性赋值为columnValue
				field.set(t,columnValue);
			}
			// 返回已经被赋值完的t对象
			return t;
		}

	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		// 6、关闭资源
		// 调用我们自己封装的获取数据库连接的静态方法
		JDBCUtils.closeResource(conn,ps,rs);
	}
	return null;
}
```

2. 使用 PreparedStatement 实现针对于不同表的通用的查询操作测试

```java
// 使用PreparedStatement实现针对于不同表的通用的查询操作测试
@Test
public void test3(){
	// 编写sql语句
	String sql = "SELECT id,name,email,birth FROM customers WHERE id=?";
	// 调用实现针对于不同表的通用的查询操作方法，传入sql语句和占位符参数
	Customers customers = JDBCUtils.getInstance(Customers.class,sql, 1);
	// 打印返回的对象
	System.out.println(customers);

	// 编写sql语句
	// 这个表的表明order是关键字，所以要用··（反单引号，TAP键上面的）包起来
	String sql2 = "SELECT order_id orderId,order_name orderName,order_date orderDate FROM `order` WHERE order_id=?";
	// 调用实现针对于不同表的通用的查询操作方法，传入sql语句和占位符参数
	Order order = JDBCUtils.getInstance(Order.class,sql2, 1);
	// 打印返回的对象
	System.out.println(order);
}
```

3. 实现针对于不同表的通用的查询操作，返回多条数据，JDBCUtils 工具类中新加的方法为：

```java
// 实现针对于不同表的通用的查询操作，返回多条数据
// 參數1：泛型，表明传进来的是什么类
// 参数2：sql语句，参数3：填充占位符的具体数值
// Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
// sql中占位符的个数与可变形参的长度相同
public static  <T> List<T> getForList(Class<T> clazz,String sql,Object ...args){

	Connection conn = null;
	PreparedStatement ps = null;
	ResultSet rs = null;

	try {
		// 1、获取数据库的连接
		// 调用我们自己封装的获取数据库连接的静态方法
		conn = JDBCUtils.getConnection();

		// 2、预编译sql语句，返回PrepareStatement的实例
		ps = conn.prepareStatement(sql);

		// 3、填充占位符
		for (int i = 0; i < args.length; i++) {
			// 小心参数声明错误
			ps.setObject(i + 1,args[i]);
		}

		// 4、执行，并返回查询到的结果集
		rs = ps.executeQuery();
		// 获取结果集的元数据：ResultSetMetaData
		ResultSetMetaData rsMetaData = rs.getMetaData();
		// 可通过ResultSetMetaData获取结果集中的列数
		// 就是查询到的一行数据中，有几个数据
		int columnCount = rsMetaData.getColumnCount();

		// 5、处理结果集
		// 创建集合对象，用来储存要返回的对象
		ArrayList<T> list = new ArrayList<>();
		// resultSet.next()：判断结果集的下一条是否有数据，
		// 如果有数据返回true，并指针下移，如果返回false，指针不会下移
		// while循环，有数据就再次进行输出
		while (rs.next()){
			// 通过反射创建传进来的类的对象
			T t = clazz.newInstance();
			// 可通过ResultSetMetaData获取结果集中的列数
			// 所以通过ResultSetMetaData判断循环次数
			// 处理结果集一行数据中的每一个列
			for (int i = 0; i < columnCount; i++) {
				/*
				获取每个列的列名
				此处不再使用rsMetaData.getColumnName(i + 1);获取列名
				因为通过他获取的是表中真正的列名，而不是我们给起的别名
				改为使用获取列的别名的方法：
				若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
				 */
				String columnLabel = rsMetaData.getColumnLabel(i + 1);

				// 获取每个列的值
				Object columnValue = rs.getObject(i + 1);

				// 给传入的对象clazz指定的columnLabel属性，赋值为columnValue
				// 通过反射
				// 通过传入的columnLabel（别名）来获得t对象中对应的属性
				Field field = clazz.getDeclaredField(columnLabel);
				// 不确定属性的权限，所以调用setAccessible()并设置为ture
				field.setAccessible(true);
				// 将t对象中别名为columnLabel的属性赋值为columnValue
				field.set(t,columnValue);
			}
			// 将已经被赋值完的t对象加入到集合中
			list.add(t);
		}
		// 循环结束后返回集合
		return list;

	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		// 6、关闭资源
		// 调用我们自己封装的获取数据库连接的静态方法
		JDBCUtils.closeResource(conn,ps,rs);
	}
	return null;
}
```

4. 实现针对于不同表的通用的查询操作，返回多条数据方法的测试

```java
// 实现针对于不同表的通用的查询操作，返回多条数据方法的测试
@Test
public void test(){
	// 编写sql语句
	String sql = "SELECT id,name,email,birth FROM customers WHERE id < ?";
	// 调用实现针对于不同表的通用的查询操作，返回多条数据
	List<Customers> list = JDBCUtils.getForList(Customers.class, sql, 10);
	// 打印返回的对象
	System.out.println(list);

	System.out.println("********************************");

	// 编写sql语句
	String sql2 = "SELECT order_id orderId,order_name orderName,order_date orderDate FROM `order` WHERE order_id > ?";
	// 调用实现针对于不同表的通用的查询操作，返回多条数据
	List<Order> list2 = JDBCUtils.getForList(Order.class, sql2, 1);
	// 打印返回的对象
	System.out.println(list2);
}
```

## 7、JDBC API 小结

1. 两种思想
	1. 面向接口编程的思想
	2. ORM 思想(object relational mapping)
		1. 一个数据表对应一个 java 类
		2. 表中的一条记录对应 java 类的一个对象
		3. 表中的一个字段对应 java 类的一个属性
	3. sql 是需要结合列名和表的属性名来写。注意起别名。
2. 两种技术
	1. JDBC 结果集的元数据：`ResultSetMetaData`
		1. 获取列数：`getColumnCount()`
		2. 获取列的别名：`getColumnLabel()`
	2. 通过反射，创建指定类的对象，获取指定的属性并赋值

# 四、操作 BLOB 类型字段

## 1、MySQL BLOB 类型
1. MySQL 中，BLOB 是一个二进制大型对象，是一个可以存储大量数据的容器，它能容纳不同大小的数据。
2. 插入 BLOB 类型的数据必须使用 PreparedStatement，因为 BLOB 类型的数据无法使用字符串拼接写的。
3. MySQL 的四种 BLOB 类型(除了在存储的最大信息量上不同外，他们是等同的)

| 类型         | 大小（单位：字节）                       |
| ---------- | ------------------------------- |
| TinyBlob   | 最大 <font color="red">255</font> |
| Blob       | 最大 <font color="red">65K</font> |
| MediumBlob | 最大 <font color="red">16M</font> |
| LongBlob   | 最大 <font color="red">4G</font>  |

4. 实际使用中根据需要存入的数据大小定义不同的BLOB类型。
5. 需要注意的是：<font color="red">如果存储的文件过大，数据库的性能会下降。</font>
6. 如果在指定了相关的 Blob 类型以后，还报错：<font color="red">xxx too large</font>，那么在 mysql 的安装目录下，找 <font color="red">my.ini</font> 文件加上如下的配置参数： <font color="red">max_allowed_packet=16M</font>。同时注意：修改了 my.ini 文件之后，需要重新启动 mysql 服务。

## 2、向数据表中插入大数据类型

```java
// 向数据表customers中插入Blob类型的字段
@Test
public void test1() throws Exception {
	// 1、获取数据库的连接
	// 调用我们自己封装的获取数据库连接的静态方法
	Connection conn = JDBCUtils.getConnection();

	// 2、编写sql语句
	String sql = "INSERT INTO customers(name,email,birth,photo) VALUES(?,?,?,?)";

	// 3、预编译sql语句，返回PrepareStatement的实例
	PreparedStatement ps = conn.prepareStatement(sql);

	// 4、填充占位符
	ps.setObject(1,"月海");
	ps.setObject(2,"123@QQ.com");
	ps.setObject(3,"1996-09-20");
	// 储存文件
	FileInputStream fIS = new FileInputStream(new File("世羽.jpg"));
	ps.setObject(4,fIS);

	// 5、执行
	ps.execute();

	// 6、关闭资源
	// 关闭IO流
	fIS.close();
	// 调用我们自己封装的关闭数据库连接的静态方法
	JDBCUtils.closeResource(conn,ps);
}
```

## 3、修改数据表中的 Blob 类型字段

## 4、从数据表中读取大数据类型

```java
// 查询数据表customers中Blob类型的字段
@Test
public void test2() {

	Connection conn = null;
	PreparedStatement ps = null;
	ResultSet rs = null;
	InputStream bS = null;
	FileOutputStream fOS = null;

	try {
		// 1、获取数据库的连接
		// 调用我们自己封装的获取数据库连接的静态方法
		conn = JDBCUtils.getConnection();

		// 2、编写sql语句
		String sql = "SELECT id,name,email,birth,photo FROM customers WHERE id = ?";

		// 3、预编译sql语句，返回PrepareStatement的实例
		ps = conn.prepareStatement(sql);

		// 4、填充占位符
		ps.setInt(1,25);

		// 5、执行，并返回查询到的结果集
		rs = ps.executeQuery();

		// 6、处理结果集
		if(rs.next()){
			// 方式一：按顺序获取
			// int id = rs.getInt(1);
			// String name = rs.getString(2);
			// String email = rs.getString(3);
			// Date birth = rs.getDate(4);

			// 方式二：按字段名获取
			int id = rs.getInt("id");
			String name = rs.getString("name");
			String email = rs.getString("email");
			Date birth = rs.getDate("birth");

			Customers customers = new Customers(id, name, email, birth);

			// 输出查询结果
			System.out.println(customers);

			// 将Blob类型的字段下载下来，以文件的方式保存下来
			Blob photo = rs.getBlob("photo");
			// 创建IO流，进行数据的传输
			bS = photo.getBinaryStream();
			fOS = new FileOutputStream("月海.jpg");
			byte[] buffer = new byte[1024];
			int len;
			while ( (len = bS.read(buffer)) != -1 ){
				fOS.write(buffer,0,len);
			}

		}
	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		// 6、关闭资源
		// 手动关闭io流
		if (fOS != null){
			try {
				fOS.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		if (bS != null){
			try {
				bS.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		// 调用我们自己封装的关闭数据库连接的静态方法
		JDBCUtils.closeResource(conn,ps,rs);
	}

}
```

# 五、批量插入

## 1、批量执行 SQL 语句

1. 当需要成批插入或者更新记录时，可以采用 Java 的批量更新机制，这一机制允许多条语句一次性提交给数据库批量处理。通常情况下比单独提交处理更有效率
2. JDBC 的批量处理语句包括下面三个方法：
	1. **addBatch(String)：添加需要批量处理的SQL语句或是参数**
	2. **executeBatch()：执行批量处理语句**
	3. **clearBatch():清空缓存的数据**
3. 通常我们会遇到两种批量执行 SQL 语句的情况：
   1. 多条 SQL 语句的批量处理；
   2. 一个 SQL 语句的批量传参；
4. update、delete 本身就具有批量操作的效果，此时的批量操作，主要指的是批量的插入。INSERT，使用 PreparedStatement 如何实现更高效的插入

## 2、高效的批量插入

1. 举例：向数据表中插入 20000 条数据
2. 数据库中提供一个 goods 表。创建如下：

```sql
CREATE TABLE goods(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(20)
);
```

3. 实现层次一：使用 Statement

```java
// 方式一：使用Statement
@Test
public void test1() throws Exception {
	// 获取数据库的连接
	// 调用我们自己封装的获取数据库连接的静态方法
	Connection conn = JDBCUtils.getConnection();
	Statement st = conn.createStatement();
	// 循环插入20000次
	for(int i = 1;i <= 20000;i++){
		// 编写sql语句
		String sql = "insert into goods(name) values('name_' + "+ i +")";
		// 执行
		st.executeUpdate(sql);
	}
}
```

4. 实现层次二：使用 PreparedStatement

```java
// 方式二：使用PreparedStatement
// 此方式比第一种好的地方：只创建一次String字符串
// 为了方便此处不在try-catch，但是要记住必须要try-catch
@Test
public void test2() throws Exception {
	// 1、获取数据库的连接
	// 调用我们自己封装的获取数据库连接的静态方法
	Connection conn = JDBCUtils.getConnection();

	// 2、编写sql语句
	String sql = "insert into goods(name) values(?)";

	// 3、预编译sql语句，返回PrepareStatement的实例
	PreparedStatement ps = conn.prepareStatement(sql);

	// 循环插入20000次
	for (int i = 0; i < 200; i++) {
		// 4、填充占位符
		ps.setObject(1,"name_" + i);
		// 5、执行
		ps.execute();
	}
	// 5、关闭资源
	// 调用我们自己封装的关闭数据库连接的静态方法
	JDBCUtils.closeResource(conn,ps);
}
```

5. 实现层次三

```java
// 方式三：
// 1、使用：addBatch() / executeBatch() / clearBatch()
// 2、mysql服务器默认是关闭批处理的，我们需要通过一个参数，让mysql开启批处理的支持。
//    rewriteBatchedStatements=true
//    写在配置文件的url后面，用问号"?"连接，若是还有别的参数，用&符号连接
// 3、使用更新的mysql 驱动：mysql-connector-java-5.1.37-bin.jar
@Test
public void test3() throws Exception {
	// 1、获取数据库的连接
	// 调用我们自己封装的获取数据库连接的静态方法
	Connection conn = JDBCUtils.getConnection();

	// 2、编写sql语句
	String sql = "insert into goods(name) values(?)";

	// 3、预编译sql语句，返回PrepareStatement的实例
	PreparedStatement ps = conn.prepareStatement(sql);

	// 循环插入20000次
	for (int i = 0; i < 20000; i++) {
		// 4、填充占位符
		ps.setObject(1,"name_" + i);

		// 5、“攒”sql
		ps.addBatch();
		// 每500次执行一次里面的内容
		if(i % 500 == 0){
			// 6、执行batch
			ps.executeBatch();

			// 7、清空batch
			ps.clearBatch();
		}

	}
	// 5、关闭资源
	// 调用我们自己封装的关闭数据库连接的静态方法
	JDBCUtils.closeResource(conn,ps);
}
```

6. 实现层次四

```java
// 方式四：在层次三的基础上操作
// 使用Connection 的 setAutoCommit(false) / commit()
// 把全部的数据都攒下来，最后一次性提交
@Test
public void test4() throws Exception {
	// 1、获取数据库的连接
	// 调用我们自己封装的获取数据库连接的静态方法
	Connection conn = JDBCUtils.getConnection();

	// 2、设置为不自动提交数据
	conn.setAutoCommit(false);

	// 3、编写sql语句
	String sql = "insert into goods(name) values(?)";

	// 4、预编译sql语句，返回PrepareStatement的实例
	PreparedStatement ps = conn.prepareStatement(sql);

	// 循环插入20000次
	for (int i = 0; i < 20000; i++) {
		// 5、填充占位符
		ps.setObject(1,"name_" + i);

		// 6、“攒”sql
		ps.addBatch();
		// 每500次执行一次里面的内容
		if(i % 500 == 0){
			// 7、执行batch
			ps.executeBatch();

			// 8、清空batch
			ps.clearBatch();
		}

	}
	// 9、提交数据
	conn.commit();

	// 10、关闭资源
	// 调用我们自己封装的关闭数据库连接的静态方法
	JDBCUtils.closeResource(conn,ps);
}
```

7. 此时的 `jdbc.properties` 配置文件

```java
# 配置文件中的注释以#号开头

driverClass=com.mysql.jdbc.Driver
# jdbc：主协议
# mysql：子协议
# 152.136.229.92：IP地址
# 3306：端口号，MySQL默认的端口号
# test：数据库名
# ?：后面可添加参数
# characterEncoding=utf-8：指定所处理字符的解码和编码的格式
# 若项目的字符集和MySQL数据库字符集设置为同一字符集则url可以不加此参数。
url=jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true
user=root
password=000123
```

# 六、数据库事务

## 1、数据库事务介绍

1. <font color="red">事务：一组逻辑操作单元（一个或多个DML（增删改）操作），使数据从一种状态变换到另一种状态。</font>
2. <font color="red">事务处理（事务操作）：</font>保证所有事务都作为一个工作单元来执行，即使出现了故障，都不能改变这种执行方式。当在一个事务中执行多个操作时，要么所有的事务都<font color="red">被提交(commit)</font>，那么这些修改就永久地保存下来；要么数据库管理系统将放弃所作的所有修改，整个事务<font color="red">回滚(rollback)</font>到最初状态。
3. 为确保数据库中数据的<font color="red">一致性</font>，数据的操纵应当是离散的成组的逻辑单元：当它全部完成时，数据的一致性可以保持，而当这个单元中的一部分操作失败，整个事务应全部视为错误，所有从起始点以后的操作应全部回退到开始状态。

## 2、JDBC事务处理

1. <font color="red">数据一旦提交，就不可回滚。</font>
2. <font color="red">数据什么时候意味着提交？</font>
	1. <font color="red">当一个连接对象被创建时，默认情况下是自动提交事务</font>
	2. <font color="red">每次执行一个 SQL 语句时，如果执行成功，就会向数据库自动提交，而不能回滚。</font>
	3. <font color="red">关闭数据库连接，数据就会自动的提交。</font>如果多个操作，每个操作使用的是自己单独的连接，则无法保证事务。即同一个事务的多个操作必须在同一个连接下。
3. <font color="red">哪些操作会导致数据的提交：</font>（对应上面）
	1. DDL 操作一旦执行，都会自动提交
	2. DML 默认情况下，一旦执行，就会自动提交
	3. 默认在关闭连接时，会自动的提交数据

```java
// 我们可以通过下面的方式取消DML操作的自动提交
// 对DDL操作不能取消
set autocommit = false
```

4. <font color="red">JDBC程序中为了让多个 SQL 语句作为一个事务执行：</font>
	1. 调用 Connection 对象的 <font color="red">setAutoCommit(false);</font> 以取消自动提交事务
	2. 在所有的 SQL 语句都成功执行后，调用 <font color="red">commit();</font> 方法提交事务
	3. 在出现异常时，调用 <font color="red">rollback();</font> 方法回滚事务
	4. 若此时 Connection 没有被关闭，还可能被重复使用，则需要恢复其自动提交状态
	5. setAutoCommit(true)。尤其是在使用数据库连接池技术时，执行close()方法前，建议恢复自动提交状态。
5. 举例：未考虑数据库事务的转账操作

```java
// 未考虑数据库事务的转账操作
// AA向BB转账100元
public class Demo01 {
  public static void main(String[] args) throws Exception {
	 // AA向BB转账100元
	 String sql1 = "update user_table set balance = balance - 100 where user = ?";
	 JDBCUtils.update(sql1,"AA");

	 // 模拟网络异常
	 System.out.println( 10/0 );

	 // BB收款100元
	 String sql2 = "update user_table set balance = balance + 100 where user = ?";
	 JDBCUtils.update(sql2,"BB");
  }
}
```

6. 考虑数据库事务的转账操作：
7. JDBCUtils工具类中，通用的增删改操作2.0，考虑上数据库事务

```java
// 通用的增删改操作2.0，考虑上数据库事务
// 方法中不再造数据库连接，关闭时也不再关闭连接
public static void update2(Connection conn,String sql,Object ...args) {

 PreparedStatement ps = null;

 try {
	   // 1、预编译sql语句，返回PrepareStatement的实例
	   ps = conn.prepareStatement(sql);
	   // 2、填充占位符
	   for (int i = 0; i < args.length; i++) {
		  // 小心参数声明错误
		  ps.setObject(i + 1,args[i]);
	   }
	   // 3、执行
	   ps.execute();
 } catch (Exception e) {
	   e.printStackTrace();
 } finally {

	   // 4、关闭资源
	   // 调用我们自己封装的关闭数据库连接的静态方法
	   // 此处不用try-catch，closeResource已经进行处理了
	   JDBCUtils.closeResource(null,ps);
 }

}
```

8. 考虑数据库事务的转账操作

```java
// 考虑数据库事务的转账操作
// AA向BB转账100元
public class Demo02 {
 public static void main(String[] args) {

	Connection conn = null;

	try {
		  // 1、获取数据库的连接
		  // 调用我们自己封装的获取数据库连接的静态方法
		  conn = JDBCUtils.getConnection();

		  // 2、开启事务
		  // 取消数据的自动提交功能
		  conn.setAutoCommit(false);

		  // AA向BB转账100元
		  // 3、进行数据库操作，编写sql语句
		  String sql1 = "update user_table set balance = balance - 100 where user = ?";
		  // 4、调用我们自己封装的改进的考虑事务的增删改方法
		  JDBCUtils.update2(conn,sql1,"AA");

		  // 模拟网络异常
		  System.out.println( 10 / 0 );

		  // BB收款100元
		  // 3、进行数据库操作，编写sql语句
		  String sql2 = "update user_table set balance = balance + 100 where user = ?";
		  // 4、调用我们自己封装的改进的考虑事务的增删改方法
		  JDBCUtils.update2(conn,sql2,"BB");

		  // 5、若没有异常，则提交事务
		  conn.commit();

	} catch (Exception e) {
		  e.printStackTrace();

		  // 6、若有异常，则回滚事务
		  try {
			 conn.rollback();
		  } catch (SQLException throwables) {
			 throwables.printStackTrace();
		  }

	} finally {
		  // 7、执行close()方法前，建议恢复自动提交状态
		  // 恢复每次DML操作的自动提交功能
		  try {
			 conn.setAutoCommit(true);
		  } catch (SQLException throwables) {
			 throwables.printStackTrace();
		  }

		  // 8、调用关闭资源的的方法，
		  // 因为update2()方法中只关闭了ps二没有关闭conn
		  // 所以此次只传入conn
		  JDBCUtils.closeResource(conn,null);
	}

 }
}
```

## 3、事务的 ACID 属性

1. <font color="red">原子性（Atomicity）</font> 原子性是指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。
2. <font color="red">一致性（Consistency）</font> 事务必须使数据库从一个一致性状态变换到另外一个一致性状态。
3. <font color="red">隔离性（Isolation）</font> 事务的隔离性是指一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
4. <font color="red">持久性（Durability）</font> 持久性是指一个事务一旦被提交，它对数据库中数据的改变就是永久性的，接下来的其他操作和数据库故障不应该对其有任何影响。

### 1、数据库的并发问题

1. 对于同时运行的多个事务, 当这些事务访问数据库中相同的数据时, 如果没有采取必要的隔离机制, 就会导致各种并发问题:
	1. <font color="red">脏读: </font>对于两个事务 T1, T2, T1 读取了已经被 T2 更新但还没有被提交的字段。之后, 若 T2 回滚, T1读取的内容就是临时且无效的。
	2. <font color="red">不可重复读（一般不去解决这个问题）:</font> 对于两个事务T1, T2, T1 读取了一个字段, 然后 T2 <font color="red">更新</font>了该字段。之后, T1再次读取同一个字段, 值就不同了。
	3. <font color="red">幻读（一般也不去解决这个问题）: </font>对于两个事务T1, T2, T1 从一个表中读取了一个字段, 然后 T2 在该表中<font color="red">插入</font>了一些新的行。之后, 如果 T1 再次读取同一个表, 就会多出几行。
2. <font color="red">数据库事务的隔离性:</font> 数据库系统必须具有隔离并发运行各个事务的能力, 使它们不会相互影响, 避免各种并发问题。
3. 一个事务与其他事务隔离的程度称为隔离级别。数据库规定了多种事务隔离级别, 不同隔离级别对应不同的干扰程度, <font color="red">隔离级别越高, 数据一致性就越好, 但并发性越弱。</font>

### 2、数据库提供的4种事务隔离级别：

1. Oracle 支持的 2 种事务隔离级别：READ COMMITED（2：读已提交）, SERIALIZABLE（4：串行化）。 Oracle 默认的事务隔离级别为: READ COMMITED（2：读已提交）。
2. Mysql 支持 4 种事务隔离级别。Mysql 默认的事务隔离级别为: REPEATABLE READ（3：可重复读）。
3. 一般情况下我们使用的隔离级别都是：READ COMMITED（2：读已提交），因为不可重复读和幻读在我们看来都是正常且应该存在的

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F17、数据库提供的4种事务隔离级别.png)

### 3、在MySql中设置隔离级别

1. 每启动一个 mysql 程序, 就会获得一个单独的数据库连接. 每个数据库连接都有一个全局变量 @@tx_isolation,表示当前的事务隔离级别。
2. 查看当前的隔离级别：

```sql
SELECT @@tx_isolation;
```

3. 设置当前 mySQL 连接的隔离级别：

```sql
set transaction isolation level read committed;
```

4. 设置数据库系统的全局的隔离级别：

```sql
set global transaction isolation level read committed;
```

5. 补充操作：
6. 创建 mysql 数据库用户：

```sql
create user tom identified by 'abc123';
```
   
7. 授予权限

```sql
# 授予通过网络方式登录的tom用户，对所有库所有表的全部权限，密码设为abc123.
grant all privileges on *.* to tom@'%' identified by 'abc123';

# 给tom用户使用本地命令行方式，授予atguigudb这个库下的所有表的插删改查的权限。
grant select,insert,delete,update on atguigudb.* to tom@localhost identified by'abc123';
```

# 七、DAO 及相关实现类

1. DAO：Data Access Object 访问数据信息的类和接口，包括了对数据的 CRUD（Create、Retrival、Update、Delete），而不包含任何业务相关的信息。有时也称作：BaseDAO
2. 作用：为了实现功能的模块化，更有利于代码的维护和升级。

## 举例：只实现了对 customers 表的操作

1. JDBC 结构

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F18、DAO及其相关实现类.png)

2. `jdbc.properties` 配置文件

```java
# 配置文件中的注释以#号开头

driverClass=com.mysql.jdbc.Driver
# jdbc：主协议
# mysql：子协议
# 152.136.229.92：IP地址
# 3306：端口号，MySQL默认的端口号
# test：数据库名
# ?：后面可添加参数
# characterEncoding=utf-8：指定所处理字符的解码和编码的格式
# rewriteBatchedStatements=true：保证5.1.13以上版本的驱动，能实现高性能的批量插入。
# 若项目的字符集和MySQL数据库字符集设置为同一字符集则url可以不加此参数。
url=jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true
user=root
password=000123
```

3. Customers 类：对应数据库的 customers 表

```java
/**
*  ORM编程思想：（object relational mapping）
*  一个数据表对应一个java类
*  表中的一条记录对应java类中的一个对象
*  表中的一个字段对应java类中的一个属性
*/
public class Customers {
  // 对应的属性
  private int id;
  private String name;
  private String email;
  // 对应数据库表的时间数据类型应是java.sql.Date
  private Date birth;

  public Customers() { }
  public Customers(int id, String name, String email, Date birth) {
	 this.id = id;
	 this.name = name;
	 this.email = email;
	 this.birth = birth;
  }

  public int getId() { return id; }
  public void setId(int id) {
	 this.id = id;
  }
  public String getName() { return name; }
  public void setName(String name) { this.name = name; }
  public String getEmail() { return email; }
  public void setEmail(String email) { this.email = email; }
  public Date getBirth() { return birth; }
  public void setBirth(Date birth) { this.birth = birth; }

  @Override
  public String toString() {
	 return "Customers{" +
			  "id=" + id +
			  ", name='" + name + '\'' +
			  ", email='" + email + '\'' +
			  ", birth=" + birth +
			  '}';
  }

}
```

3. JDBCUtils：封装了获取数据库连接连接与关闭数据库连接的静态方法

```java
public class JDBCUtils {
  /**
  * 获取数据库连接
  * @return
  * @throws Exception
  */
  public static Connection getConnection() throws Exception {
	 // 1、读取配置文件中的4个基本信息
	 InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream("jdbc.properties");
	 // 创建Properties的对象
	 Properties properties = new Properties();
	 // 调用Properties的load()方法，从方法加载数据
	 properties.load(inputStream);
	 // 从文件获取数据并赋值
	 String driverClass = properties.getProperty("driverClass");
	 String url = properties.getProperty("url");
	 String user = properties.getProperty("user");
	 String password = properties.getProperty("password");

	 // 2、加载驱动
	 Class.forName(driverClass);

	 // 3、获取连接
	 Connection conn = DriverManager.getConnection(url, user, password);

	 // 返回Connection（数据库源连接）对象
	 return conn;
  }

  /**
  * *************************************************
  */

  /**
  * 增删改的关闭操作
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

  /**
  * *************************************************
  */

  /**
  * 查询的关闭操作，方法的重载
  * 关闭数据库连接和Statement的操作
  * @param conn
  * @param ps
  */
  public static void closeResource(Connection conn, PreparedStatement ps, ResultSet rs){

	 if(ps != null){
		   try {
			  ps.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(conn != null){
		   try {
			  conn.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

	 if(rs != null){
		   try {
			  rs.close();
		   } catch (SQLException throwables) {
			  throwables.printStackTrace();
		   }
	 }

  }

}
```

4. BaseDao：封装的各种操作数据库的具体实现方法的类

```java
// DAO：data(base) access object：数据（库）访问对象
// 抽象类
public abstract class BaseDao<T> {
  
  private Class<T> clazz = null;

  {
	 // this：子类的对象
	 // 获取当前类（BaseDao）的子类（this，比如CustomersDaoImpl类）继承的父类的泛型
	 Type genericSuperclass = this.getClass().getGenericSuperclass();
	 ParameterizedType paramType = (ParameterizedType) genericSuperclass;
	 // 获取了父类的泛型参数
	 Type[] typeArguments = paramType.getActualTypeArguments();
	 // 获取泛型的第一个参数
	 clazz = (Class<T>) typeArguments[0];
  }
  
  // 通用的增删改操作2.0，考虑上数据库事务
  // 方法中不再造数据库连接，关闭时也不再关闭连接
  public void update(Connection conn,String sql,Object ...args) {

	 PreparedStatement ps = null;

	 try {
		   // 1、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);
		   // 2、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }
		   // 3、执行
		   ps.execute();
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {

		   // 4、关闭资源
		   // 调用我们自己封装的关闭数据库连接的静态方法
		   // 此处不用try-catch，closeResource已经进行处理了
		   JDBCUtils.closeResource(null,ps);
	 }

  }

  /**
  * *************************************************
  */

  // 使用PreparedStatement实现针对于不同表的通用的查询操作，泛型方法
  // 返回表中的一条记录
  // 參數1：泛型，表明传进来的是什么类
  // 参数2：sql语句，参数3：填充占位符的具体数值
  // Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
  // sql中占位符的个数与可变形参的长度相同
  public T getInstance(Connection conn,String sql,Object ...args){

	 PreparedStatement ps = null;
	 ResultSet rs = null;

	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();

		   // 2、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);

		   // 3、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }

		   // 4、执行，并返回查询到的结果集
		   rs = ps.executeQuery();
		   // 获取结果集的元数据：ResultSetMetaData
		   ResultSetMetaData rsMetaData = rs.getMetaData();
		   // 可通过ResultSetMetaData获取结果集中的列数
		   // 就是查询到的一行数据中，有几个数据
		   int columnCount = rsMetaData.getColumnCount();

		   // 5、处理结果集
		   // resultSet.next()：判断结果集的下一条是否有数据，
		   // 如果有数据返回true，并指针下移，如果返回false，指针不会下移
		   if(rs.next()){
			  // 通过反射创建传进来的类的对象
			  T t = clazz.newInstance();
			  // 可通过ResultSetMetaData获取结果集中的列数
			  // 所以通过ResultSetMetaData判断循环次数
			  // 处理结果集一行数据中的每一个列
			  for (int i = 0; i < columnCount; i++) {
				 /*
				 获取每个列的列名
				 此处不再使用rsMetaData.getColumnName(i + 1);获取列名
				 因为通过他获取的是表中真正的列名，而不是我们给起的别名
				 改为使用获取列的别名的方法：
				 若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
					*/
				 String columnLabel = rsMetaData.getColumnLabel(i + 1);

				 // 获取每个列的值
				 Object columnValue = rs.getObject(i + 1);

				 // 给t对象指定的columnLabel属性，赋值为columnValue
				 // 通过反射
				 // 通过传入的columnLabel（别名）来获得t对象中对应的属性
				 Field field = clazz.getDeclaredField(columnLabel);
				 // 不确定属性的权限，所以调用setAccessible()并设置为ture
				 field.setAccessible(true);
				 // 将t对象中别名为columnLabel的属性赋值为columnValue
				 field.set(t,columnValue);
			  }
			  // 返回已经被赋值完的t对象
			  return t;
		   }

	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 6、关闭资源
		   // 调用我们自己封装的关闭数据库连接的静态方法
		   JDBCUtils.closeResource(null,ps,rs);
	 }
	 return null;
  }

  // 实现针对于不同表的通用的查询操作，返回多条数据
  // 參數1：泛型，表明传进来的是什么类
  // 参数2：sql语句，参数3：填充占位符的具体数值
  // Object ...args：JDK1.5新增语法，新特性，动态参数或者是可变参数的意思。相当于一个数组
  // sql中占位符的个数与可变形参的长度相同
  public List<T> getForList(Connection conn, String sql, Object ...args){

	 PreparedStatement ps = null;
	 ResultSet rs = null;

	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();

		   // 2、预编译sql语句，返回PrepareStatement的实例
		   ps = conn.prepareStatement(sql);

		   // 3、填充占位符
		   for (int i = 0; i < args.length; i++) {
			  // 小心参数声明错误
			  ps.setObject(i + 1,args[i]);
		   }

		   // 4、执行，并返回查询到的结果集
		   rs = ps.executeQuery();
		   // 获取结果集的元数据：ResultSetMetaData
		   ResultSetMetaData rsMetaData = rs.getMetaData();
		   // 可通过ResultSetMetaData获取结果集中的列数
		   // 就是查询到的一行数据中，有几个数据
		   int columnCount = rsMetaData.getColumnCount();

		   // 5、处理结果集
		   // 创建集合对象，用来储存要返回的对象
		   ArrayList<T> list = new ArrayList<>();
		   // resultSet.next()：判断结果集的下一条是否有数据，
		   // 如果有数据返回true，并指针下移，如果返回false，指针不会下移
		   // while循环，有数据就再次进行输出
		   while (rs.next()){
			  // 通过反射创建传进来的类的对象
			  T t = clazz.newInstance();
			  // 可通过ResultSetMetaData获取结果集中的列数
			  // 所以通过ResultSetMetaData判断循环次数
			  // 处理结果集一行数据中的每一个列
			  for (int i = 0; i < columnCount; i++) {
				 /*
				 获取每个列的列名
				 此处不再使用rsMetaData.getColumnName(i + 1);获取列名
				 因为通过他获取的是表中真正的列名，而不是我们给起的别名
				 改为使用获取列的别名的方法：
				 若是sql语句没有别名，则是获取其原本的名称，所以此方法可以完全代替原方法
					*/
				 String columnLabel = rsMetaData.getColumnLabel(i + 1);

				 // 获取每个列的值
				 Object columnValue = rs.getObject(i + 1);

				 // 给传入的对象clazz指定的columnLabel属性，赋值为columnValue
				 // 通过反射
				 // 通过传入的columnLabel（别名）来获得t对象中对应的属性
				 Field field = clazz.getDeclaredField(columnLabel);
				 // 不确定属性的权限，所以调用setAccessible()并设置为ture
				 field.setAccessible(true);
				 // 将t对象中别名为columnLabel的属性赋值为columnValue
				 field.set(t,columnValue);
			  }
			  // 将已经被赋值完的t对象加入到集合中
			  list.add(t);
		   }
		   // 循环结束后返回集合
		   return list;

	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 6、关闭资源
		   // 调用我们自己封装的获取数据库连接的静态方法
		   JDBCUtils.closeResource(null,ps,rs);
	 }
	 return null;
  }

  // 用于查询特殊值的方法
  public <E> E getValue(Connection conn,String sql, Object ...args) {

	 PreparedStatement ps = null;
	 ResultSet rs = null;

	 try {
		   ps = conn.prepareStatement(sql);

		   for (int i = 0; i < args.length; i++) {
			  ps.setObject(i + 1,args);
		   }

		   rs = ps.executeQuery();
		   if(rs.next()){
			  return (E) rs.getObject(1);
		   }
	 } catch (SQLException throwables) {
		   throwables.printStackTrace();
	 } finally {
		   JDBCUtils.closeResource(null,ps,rs);
	 }
	 return null;
  }

}
```

5. CustomersDao：规范针对于 customers 表的常用操作

```java
// 此接口用于规范针对于customers表的常用操作
public interface CustomersDao {
  /**
  * 将cust对象添加到数据库中
  * @param conn
  * @param cust
  */
  void insert(Connection conn, Customers cust);

  /**
  * 根据指定的id，删除表中的一条记录
  * @param conn
  * @param id
  */
  void deleteById(Connection conn, int id);

  /**
  * 针对内存中的cust对象，取修改数据表中指定的记录
  * @param conn
  * @param cust
  */
  void update(Connection conn, Customers cust);

  /**
  * 针对指定的id查询得到对应的Customers对象
  * 查询一条对象
  * @param conn
  * @param id
  */
  Customers getCustomersById(Connection conn, int id);

  /**
  * 查询表中的所有记录构成的集合
  * @param conn
  * @return
  */
  List<Customers> getAll(Connection conn);

  /**
  * 返回数据表中数据的条目数
  * @param conn
  * @return
  */
  long getCount(Connection conn);

  /**
  * 返回数据表中最大的生日
  * @param conn
  * @return
  */
  Date getMaxBirth(Connection conn);
}
```

6. CustomersDaoImpl：CustomersDao 的实现类

```java
public class CustomersDaoImpl extends BaseDao<Customers> implements CustomersDao {
  @Override
  public void insert(Connection conn, Customers cust) {
	 String sql = "INSERT INTO customers(name,email,birth) VALUES(?,?,?)";
	 update(conn,sql,cust.getName(),cust.getEmail(),cust.getBirth());
  }

  @Override
  public void deleteById(Connection conn, int id) {
	 String sql = "DELETE FROM customers WHERE id = ?";
	 update(conn,sql,id);
  }

  @Override
  public void update(Connection conn, Customers cust) {
	 String sql = "UPDATE customers SET name = ?,email = ?,birth = ? WHERE id = ?";
	 update(conn,sql,cust.getName(),cust.getEmail(),cust.getBirth(),cust.getId());
  }

  @Override
  public Customers getCustomersById(Connection conn, int id) {
	 String sql = "SELECT id,name,email,birth FROM customers WHERE id = ?";
	 Customers instance = getInstance(conn, sql, id);
	 return instance;
  }

  @Override
  public List<Customers> getAll(Connection conn) {
	 String sql = "SELECT id,name,email,birth FROM customers";
	 List<Customers> forList = getForList(conn, sql);
	 return forList;
  }

  @Override
  public long getCount(Connection conn) {
	 String sql = "SELECT COUNT(id) FROM customers";
	 return  getValue(conn, sql);
  }

  @Override
  public Date getMaxBirth(Connection conn) {
	 String sql = "SELECT MAX(birth) FROM customers";
	 return  getValue(conn, sql);
  }
}
```

7. 测试类，未全部测试

```java
// 测试
class CustomersDaoImplTest {
  // 每一个测试方法都要用，就在最开始创建一个对象
  CustomersDaoImpl dao = new CustomersDaoImpl();

  @Test
  void insert() {
	 Connection conn = null;
	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();
		   // 给日期赋值
		   SimpleDateFormat sDF = new SimpleDateFormat("yyyy-MM-dd");
		   Date date = sDF.parse("1000-01-01");
		   // 2、传入参数
		   Customers cust = new Customers(1,"羽","770717410@qq.com",new java.sql.Date(date.getTime()));
		   // 3、调用CustomersDaoImpl中的insert()方法
		   dao.insert(conn,cust);
		   // 程序能进行到这里就表明添加成功
		   System.out.println("添加成功");
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 4、关闭连接
		   JDBCUtils.closeResource(conn,null);
	 }
  }

  @Test
  void deleteById() throws Exception {
	 Connection conn = null;
	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();
		   // 2、调用CustomersDaoImpl中的deleteById()方法
		   // 并传入要删除的id
		   dao.deleteById(conn,29);
		   // 程序能进行到这里就表明添加成功
		   System.out.println("删除成功");
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 3、关闭连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  @Test
  void update() {
  }

  @Test
  void getCustomersById() {
  }

  @Test
  void getAll() {
	 Connection conn = null;
	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();
		   // 2、调用CustomersDaoImpl中的getAll()方法
		   // 并传入要删除的id
		   List<Customers> customersList = dao.getAll(conn);
		   // 程序能进行到这里就表明添加成功
		   customersList.forEach(System.out::println);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 3、关闭连接
		   JDBCUtils.closeResource(conn,null);
	 }
  }

  @Test
  void getCount() {
	 Connection conn = null;
	 try {
		   // 1、获取数据库的连接
		   // 调用我们自己封装的获取数据库连接的静态方法
		   conn = JDBCUtils.getConnection();
		   // 2、调用CustomersDaoImpl中的getCount()方法
		   // 并传入要删除的id
		   long count = dao.getCount(conn);
		   // 打印返回值
		   System.out.println("共有" + count + "条数据");
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 3、关闭连接
		   JDBCUtils.closeResource(conn,null);
	 }
  }

  @Test
  void getMaxBirth() {
  }
}
```

# 八、数据库连接池

## 1、JDBC 数据库连接池的必要性

1. 在使用开发基于数据库的 web 程序时，传统的模式基本是按以下步骤：
	1. 在主程序（如 servlet、beans）中建立数据库连接
	2. 进行 sql 操作
	3. 断开数据库连接
2. 这种模式开发，存在的问题:
	1. 普通的 JDBC 数据库连接使用 DriverManager 来获取，每次向数据库建立连接的时候都要将 Connection 加载到内存中，再验证用户名和密码（得花费 0.05s～1s 的时间）。需要数据库连接的时候，就向数据库要求一个，执行完成后再断开连接。这样的方式将会消耗大量的资源和时间。<font color="red">数据库的连接资源并没有得到很好的重复利用</font>。若同时有几百人甚至几千人在线，频繁的进行数据库连接操作将占用很多的系统资源，严重的甚至会造成服务器的崩溃。
	2. <font color="red">对于每一次数据库连接，使用完后都得断开。</font>否则，如果程序出现异常而未能关闭，将会导致数据库系统中的内存泄漏，最终将导致重启数据库。（回忆：何为Java的内存泄漏？）
	3. <font color="red">这种开发不能控制被创建的连接对象数</font>，系统资源会被毫无顾及的分配出去，如连接过多，也可能导致内存泄漏，服务器崩溃。

## 2、数据库连接池技术

1. 为解决传统开发中的数据库连接问题，可以采用数据库连接池技术。
2. <font color="red">数据库连接池的基本思想：</font>就是为数据库连接建立一个“缓冲池”。预先在缓冲池中放入一定数量的连接，当需要建立数据库连接时，只需从“缓冲池”中取出一个，使用完毕之后再放回去。
3. <font color="red">数据库连接池</font>负责分配、管理和释放数据库连接，它<font color="red">允许应用程序重复使用一个现有的数据库连接，而不是重新建立一个</font>。
4. 数据库连接池在初始化时将创建一定数量的数据库连接放到连接池中，这些数据库连接的数量是由<font color="red">最小数据库连接数来设定</font>的。无论这些数据库连接是否被使用，连接池都将一直保证至少拥有这么多的连接数量。连接池的<font color="red">最大数据库连接数量</font>限定了这个连接池能占有的最大连接数，当应用程序向连接池请求的连接数超过最大连接数量时，这些请求将被加入到等待队列中。

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F19、数据库连接池.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F20、数据库连接池的工作原理.png)

## 3、数据库连接池技术的优点

1. <font color="red">资源重用：</font>由于数据库连接得以重用，避免了频繁创建，释放连接引起的大量性能开销。在减少系统消耗的基础上，另一方面也增加了系统运行环境的平稳性。
2. <font color="red">更快的系统反应速度：</font>数据库连接池在初始化过程中，往往已经创建了若干数据库连接置于连接池中备用。此时连接的初始化工作均已完成。对于业务请求处理而言，直接利用现有可用连接，避免了数据<font color="red"></font>库连接初始化和释放过程的时间开销，从而减少了系统的响应时间
3. <font color="red">新的资源分配手段：</font>对于多应用共享同一数据库的系统而言，可在应用层通过数据库连接池的配置，实现某一应用最大可用数据库连接数的限制，避免某一应用独占所有的数据库资源
4. <font color="red">统一的连接管理，避免数据库连接泄漏：</font>在较为完善的数据库连接池实现中，可根据预先的占用超时设定，强制回收被占用连接，从而避免了常规数据库连接操作中可能出现的资源泄露

## 4、多种开源的数据库连接池

1. JDBC 的数据库连接池使用 `javax.sql.DataSource` 来表示，DataSource 只是一个接口，该接口通常由服务器（Weblogic、WebSphere、Tomcat）提供实现，也有一些开源组织提供实现：
	1. <font color="red">DBCP</font> 是 Apache 提供的数据库连接池。tomcat 服务器自带 dbcp 数据库连接池。<font color="red">速度相对c3p0较快</font>，但因自身存在 BUG，Hibernate3 已不再提供支持。
	2. <font color="red">C3P0</font> 是一个开源组织提供的一个数据库连接池，<font color="red">速度相对较慢，稳定性还可以</font>。hibernate 官方推荐使用
	3. <font color="red">Proxool</font> 是 sourceforge 下的一个开源项目数据库连接池，有监控连接池状态的功能，<font color="red">稳定性较 c3p0 差一点</font>
	4. <font color="red">BoneCP</font> 是一个开源组织提供的数据库连接池，速度快
	5. <font color="red">Druid（德鲁伊）</font> 是阿里提供的数据库连接池，据说是集 DBCP 、C3P0 、Proxool 优点于一身的数据库连接池，但是速度不确定是否有 BoneCP 快
2. DataSource 通常被称为数据源，它包含连接池和连接池管理两个部分，习惯上也经常把 DataSource 称为连接池
3. <font color="red">DiverManager 来获取 Connection，获取速度快，同时可以大幅度提高数据库访问速度。</font>
4. 特别注意：
	1. 数据源和数据库连接不同，数据源无需创建多个，它是产生数据库连接的工厂，因此<font color="red">整个应用只需要一个数据源即可</font>。
	2. 当数据库访问结束后，程序还是像以前一样关闭数据库连接：`conn.close()`; 但 `conn.close()` 并没有关闭数据库的物理连接，它仅仅把数据库连接释放，归还给了数据库连接池。

### 1、C3P0 数据库连接池

1. c3p0 需导入的 jar 包：
	1. MySql 数据库的JDBC驱动：`mysql-connector-java-5.1.37-bin.jar`
	2. c3p0 数据库连接池驱动：`c3p0-0.9.1.2.jar`

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F21、c3p0需导入的jar包.png)

#### ①、方式一：显式的获取c3p0数据库连接池

```java
// 方式一：硬编码显式的获取c3p0数据库连接池
public class Demo01 {
  public static void main(String[] args) throws Exception {
	 // 获取c3p0数据库连接池
	 ComboPooledDataSource cpds = new ComboPooledDataSource();
	 cpds.setDriverClass( "com.mysql.jdbc.Driver" );
	 cpds.setJdbcUrl( "jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true" );
	 cpds.setUser("root");
	 cpds.setPassword("000123");

	 // 通过设置相关的参数，对数据库连接池进行管理
	 // 设置初始时数据库连接池中的连接数：10个
	 cpds.setInitialPoolSize(10);

	 // 创建数据库连接
	 Connection conn = cpds.getConnection();
	 // 打印测试，看看是否成功建立连接
	 System.out.println(conn);
  }
}
```

#### ②、方式二：使用配置文件获取c3p0数据库连接池

1. c3p0 数据库连接池配置文件：`c3p0-config.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>

<c3p0-config>

	<!-- 这个配置的名称，调用时需使用这个名称进行调用 -->
	<named-config name="helloc3p0">
		<!-- 提供获取连接的4个基本信息 -->
		<property name="driverClass">com.mysql.jdbc.Driver</property>
		<property name="jdbcUrl">jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&amp;rewriteBatchedStatements=true</property>
		<property name="user">root</property>
		<property name="password">000123</property>
		
		<!-- 进行数据库连接池管理的基本信息 -->
		<!-- 若数据库中连接数不足时, 一次向数据库服务器申请多少个连接 -->
		<property name="acquireIncrement">50</property>
		<!-- 初始化数据库连接池时连接的数量 -->
		<property name="initialPoolSize">100</property>
		<!-- 数据库连接池中的最小的数据库连接数 -->
		<property name="minPoolSize">50</property>
		<!-- 数据库连接池中的最大的数据库连接数 -->
		<property name="maxPoolSize">1000</property>
		<!-- C3P0 数据库连接池可以维护的 Statement 的个数 -->
		<property name="maxStatements">0</property>
		<!-- 每个连接同时可以使用的 Statement 对象的个数 -->
		<property name="maxStatementsPerConnection">5</property>
	</named-config>

</c3p0-config>
```

2. 使用配置文件获取 c3p0 数据库连接池

```java
// 方式二：使用配置文件获取c3p0数据库连接池
public class Demo02 {
	public static void main(String[] args) throws SQLException {
		ComboPooledDataSource cpds = new ComboPooledDataSource("helloc3p0");
		
		// 创建数据库连接
		Connection conn = cpds.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

#### ③、方式三：封装为工具类，这样就解决了每次都会创建数据库连接池的问题，只需创建一个数据库连接池就可以一直使用

1. 自己封装的 c3p0_JDBCUtils 的工具类

```java
// 工具类
public class c3p0_JDBCUtils {
	// 创建数据库连接池的方法要放在最外面，因为数据库连接池的对象只用创建一个就可以了
	// 使用配置文件创建数据库连接池
	private static ComboPooledDataSource cpds = new ComboPooledDataSource("helloc3p0");
		/**
		* 使用c3p0的数据库连接池技术
		* @return
		* @throws SQLException
		*/
		public static Connection getConnection() throws SQLException {
		// 创建数据库连接
		Connection conn = cpds.getConnection();
		// 返回数据库连接对象
		return conn;
	}

}
```

2. 测试类

```java
// 方式三：
public class Demo03 {
	public static void main(String[] args) throws SQLException {
		// 调用自己封装的创建数据库连接池创建数据库连接
		Connection conn = c3p0JDBCUtils.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

### 2、DBCP 数据库连接池

1. DBCP 是 Apache 软件基金组织下的开源连接池实现，该连接池依赖该组织下的另一个开源系统 Common-pool。如需使用该连接池实现，应在系统中增加如下两个 jar 文件：
	1. `Commons-dbcp.jar`：连接池的实现
	2. `Commons-pool.jar`：连接池实现的依赖库

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F22、dbcp需导入的jar包.png)

2. Tomcat 的连接池正是采用该连接池来实现的。该数据库连接池既可以与应用服务器整合使用，也可由应用程序独立使用。
3. 数据源和数据库连接不同，数据源无需创建多个，它是产生数据库连接的工厂，因此整个应用只需要一个数据源即可。
4. 当数据库访问结束后，程序还是像以前一样关闭数据库连接：`conn.close()`; 但上面的代码并没有关闭数据库的物理连接，它仅仅把数据库连接释放，归还给了数据库连接池。
5. dbcp 连接池常用基本配置属性：

|属性|默认值|说明|
|--|--|--|
|initialSize|0|连接池启动时创建的初始化连接数量|
|maxActive|8|连接池中可同时连接的最大的连接数|
|maxIdle|8|连接池中最大的空闲的连接数，超过的空闲连接将被释放，如果设置为负数表示不限制|
|minIdle|0|连接池中最小的空闲的连接数，低于这个数量会被创建新的连接。该参数越接近maxIdle，性能越好，因为连接的创建和销毁，都是需要消耗资源的；但是不能太大。|
|maxWait|无限制|最大等待时间，当没有可用连接时，连接池等待连接释放的最大时间，超过该时间限制会抛出异常，如果设置-1表示无限等待|
|poolPreparedStatements|false|开启池的Statement是否prepared|
|maxOpenPreparedStatements|无限制|开启池的prepared 后的同时最大连接数|
|minEvictableIdleTimeMillis||连接池中连接，在时间段内一直空闲， 被逐出连接池的时间|
|removeAbandonedTimeout|300|超过时间限制，回收没有用(废弃)的连接|
|removeAbandoned|false|超过removeAbandonedTimeout时间后，是否进 行没用连接（废弃）的回收|

#### ①、方式一：硬编码显式的获取 dbcp 数据库连接池

```java
// 方式一：硬编码显式的获取dbcp数据库连接池
public class Demo01 {
  public static void main(String[] args) throws SQLException {
	 // 创建dbcp的数据库连接池
	 BasicDataSource source = new BasicDataSource();
	 // 设置基本信息
	 source.setDriverClassName("com.mysql.jdbc.Driver");
	 source.setUrl("jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true");
	 source.setUsername("root");
	 source.setPassword("000123");

	 // 还可以设置其他涉及数据库连接池
	 // initialSize ：连接池启动时创建的初始化连接数量（默认值为0）
	 source.setInitialSize(10);
	 // maxActive ：连接池中可同时连接的最大的连接数
	 // （默认值为8，调整为20，高峰单机器在20并发左右，自己根据应用场景定）
	 source.setMaxActive(20);

	 // 创建数据库连接
	 Connection conn = source.getConnection();

	 // 打印测试，看看是否成功建立连接
	 System.out.println(conn);
  }
}
```

#### ②、方式二：使用配置文件获取dbcp数据库连接池

1. 数据库连接池配置文件：`dbcp.properties`

```properties
  # 配置文件中的注释以#号开头

  driverClass=com.mysql.jdbc.Driver
  # jdbc：主协议
  # mysql：子协议
  # 152.136.229.92：IP地址
  # 3306：端口号，MySQL默认的端口号
  # test：数据库名
  # ?：后面可添加参数
  # characterEncoding=utf-8：指定所处理字符的解码和编码的格式
  # 若项目的字符集和MySQL数据库字符集设置为同一字符集则url可以不加此参数。
  url=jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true
  username=root
  password=000123
```

2. 使用配置文件获取 dbcp 数据库连接池

```java
// 方式二：使用配置文件获取dbcp数据库连接池
public class Demo02 {
	public static void main(String[] args) throws Exception {
		Properties properties = new Properties();
		
		// 加载dbc.properties配置文件
		// 方式一：使用类加载器，识别目录为当前工程的src目录下
		// InputStream iS = ClassLoader.getSystemClassLoader().getResourceAsStream("dbc.properties");
		
		// 方式二：IO流，识别目录为主工程目录
		// 若是单元测试方法，则识别目录为当前子工程目录
		FileInputStream iFS = new FileInputStream(new File("03_jdbc/src/dbcp.properties"));
		
		// 读取文件中的键值对
		properties.load(iFS);
		
		// 创建一个dbcp数据库连接池，并将读取的文件作为参数传入
		// 根据提供的BasicDataSourceFactory创建对应的DataSource对象
		DataSource source = BasicDataSourceFactory.createDataSource(properties);
		
		// 通过dbcp数据库连接池创建数据库连接对象
		Connection conn = source.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

#### ③、方式三：封装为工具类，这样就解决了每次都会创建数据库连接池的问题，只需创建一个数据库连接池就可以一直使用

1. 自己封装的c3p0_JDBCUtils的工具类

```java
// 工具类
public class DBCPJDBCUtils {
	private static DataSource source;
	// 静态代码块
	static {
		try {
			Properties properties = new Properties();
			
			// 加载dbc.properties配置文件
			// 方式二：IO流，识别目录为主工程目录
			// 若是单元测试方法，则识别目录为当前子工程目录
			FileInputStream iFS = new FileInputStream(new File("03_jdbc/src/dbcp.properties"));
			
			// 读取文件中的键值对
			properties.load(iFS);
			
			// 创建一个dbcp数据库连接池，并将读取的文件作为参数传入
			// 根据提供的BasicDataSourceFactory创建对应的DataSource对象
			source = BasicDataSourceFactory.createDataSource(properties);
		} catch (Exception e) {
			e.printStackTrace();
		}
	
	}
	
	public static Connection getConnection() throws SQLException {
		// 通过dbcp数据库连接池创建数据库连接对象
		Connection conn = source.getConnection();
		
		return conn;
	}
}
```
   
2. 测试类

```java
// 方式三：
public class Demo03 {
	public static void main(String[] args) throws SQLException {
		// 调用自己封装的创建数据库连接池创建数据库连接
		Connection conn = DBCPJDBCUtils.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

### 3、Druid（德鲁伊）数据库连接池

1. Druid 是阿里巴巴开源平台上一个数据库连接池实现，它结合了 C3P0、DBCP、Proxool 等 DB 池的优点，同时加入了日志监控，可以很好的监控DB 池连接和 SQL 的执行情况，可以说是针对监控而生的 DB 连接池，<font color="red">可以说是目前最好的连接池之一</font>。
2. Druid（德鲁伊）需导入的jar包

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F23、Druid（德鲁伊）需导入的jar包.png)

3. Druid（德鲁伊）连接池常用基本配置属性

|属性|默认值|说明|
|--|--|--|
|name||配置这个属性的意义在于，如果存在多个数据源，监控的时候可以通过名字来区分开来。 如果没有配置，将会生成一个名字，格式是：”DataSource-” + System.identityHashCode(this)
|url||连接数据库的url，不同数据库不一样。例如：mysql :jdbc:mysql://10.20.153.104:3306/druid2 oracle :jdbc:oracle:thin:@10.20.149.85:1521:ocnauto|
|username||连接数据库的用户名|
|password||连接数据库的密码。如果你不希望密码直接写在配置文件中，可以使用ConfigFilter。详细看这里：https://github.com/alibaba/druid/wiki/%E4%BD%BF%E7%94%A8ConfigFilter|
|driverClassName||根据url自动识别 这一项可配可不配，如果不配置druid会根据url自动识别dbType，然后选择相应的driverClassName(建议配置下)|
|initialSize|0|初始化时建立物理连接的个数。初始化发生在显示调用init方法，或者第一次getConnection时|
|maxActive|8|最大连接池数量|
|maxIdle|8|已经不再使用，配置了也没效果|
|minIdle||最小连接池数量|
|maxWait||获取连接时最大等待时间，单位毫秒。配置了maxWait之后，缺省启用公平锁，并发效率会有所下降，如果需要可以通过配置useUnfairLock属性为true使用非公平锁。|
|poolPreparedStatements|false|是否缓存preparedStatement，也就是PSCache。PSCache对支持游标的数据库性能提升巨大，比如说oracle。在mysql下建议关闭。|
|maxOpenPreparedStatements|-1|要启用PSCache，必须配置大于0，当大于0时，poolPreparedStatements自动触发修改为true。在Druid中，不会存在Oracle下PSCache占用内存过多的问题，可以把这个数值配置大一些，比如说100|
|validationQuery||用来检测连接是否有效的sql，要求是一个查询语句。如果validationQuery为null，testOnBorrow、testOnReturn、testWhileIdle都不会其作用。|
|testOnBorrow|true|申请连接时执行validationQuery检测连接是否有效，做了这个配置会降低性能。|
|testOnReturn|false|归还连接时执行validationQuery检测连接是否有效，做了这个配置会降低性能|
|testWhileIdle|false|建议配置为true，不影响性能，并且保证安全性。申请连接的时候检测，如果空闲时间大于timeBetweenEvictionRunsMillis，执行validationQuery检测连接是否有效。|
|timeBetweenEvictionRunsMillis||有两个含义： 1)Destroy线程会检测连接的间隔时间2)testWhileIdle的判断依据，详细看testWhileIdle属性的说明|
|numTestsPerEvictionRun||不再使用，一个DruidDataSource只支持一个EvictionRun|
|minEvictableIdleTimeMillis||connectionInitSqls 物理连接初始化的时候执行的sqlexceptionSorter 根据dbType自动识别 当数据库抛出一些不可恢复的异常时，抛弃连接|
|filters||属性类型是字符串，通过别名的方式配置扩展插件，常用的插件有：监控统计用的filter:stat日志用的filter:log4j防御sql注入的filter:wall
|proxyFilters||类型是List，如果同时配置了filters和proxyFilters，是组合关系，并非替换关系|

#### ①、方式一：硬编码显式的获取Druid（德鲁伊）数据库连接池：不再演示

#### ②、方式二：使用配置文件获取Druid（德鲁伊）数据库连接池

1. 数据库连接池配置文件：`druid.properties`

```properties
# 配置文件中的注释以#号开头

driverClassName=com.mysql.jdbc.Driver
# jdbc：主协议
# mysql：子协议
# 152.136.229.92：IP地址
# 3306：端口号，MySQL默认的端口号
# test：数据库名
# ?：后面可添加参数
# characterEncoding=utf-8：指定所处理字符的解码和编码的格式
# 若项目的字符集和MySQL数据库字符集设置为同一字符集则url可以不加此参数。
url=jdbc:mysql://152.136.229.92:3306/test?characterEncoding=utf-8&rewriteBatchedStatements=true
username=root
password=000123

# Druid（德鲁伊）连接池还可以在配置文件中配置常用基本配置属性
# initialSize、maxActive等
```

2. 方式二：使用配置文件获取dbcp数据库连接池

```java
// 使用配置文件
public class Demo01 {
	public static void main(String[] args) throws Exception {
		Properties properties = new Properties();
		
		// 加载druid.properties配置文件
		// 使用类加载器，识别目录为当前工程的src目录下
		InputStream resource = ClassLoader.getSystemClassLoader().getResourceAsStream("druid.properties");
		
		// 读取文件中的键值对
		properties.load(resource);
		
		// 创建一个druid数据库连接池，并将读取的文件作为参数传入
		// 根据提供的DruidDataSourceFactory创建对应的DataSource对象
		DataSource source = DruidDataSourceFactory.createDataSource(properties);
		
		// 通过dbcp数据库连接池创建数据库连接对象
		Connection conn = source.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

#### ③、方式三：封装为工具类，这样就解决了每次都会创建数据库连接池的问题，只需创建一个数据库连接池就可以一直使用

1. 自己封装的 c3p0_JDBCUtils 的工具类

```java
public class DruidJDBCUtils {
	private static DataSource source;
	// 静态代码块
	static {
		try {
			Properties properties = new Properties();
			
			// 加载druid.properties配置文件
			// 使用类加载器，识别目录为当前工程的src目录下
			InputStream resource = ClassLoader.getSystemClassLoader().getResourceAsStream("druid.properties");
			
			// 读取文件中的键值对
			properties.load(resource);
			
			// 创建一个druid数据库连接池，并将读取的文件作为参数传入
			// 根据提供的DruidDataSourceFactory创建对应的DataSource对象
			source = DruidDataSourceFactory.createDataSource(properties);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static Connection getConnection() throws Exception {
		// 通过 dbcp 数据库连接池创建数据库连接对象
		Connection conn = source.getConnection();
		
		// 返回创建完成后的数据库连接
		return conn;
	}
}
```

2. 测试类

```java
public class Demo02 {
	public static void main(String[] args) throws Exception {
		// 调用自己封装的创建数据库连接池创建数据库连接
		Connection conn = DruidJDBCUtils.getConnection();
		
		// 打印测试，看看是否成功建立连接
		System.out.println(conn);
	}
}
```

# 九、Apache-DBUtils 实现 CRUD 操作

## 1、Apache-DBUtils 简介

1. `commons-dbutils` 是 Apache 组织提供的一个开源 JDBC 工具类库，它是对 JDBC 的简单封装，学习成本极低，并且使用 dbutils <font color="red">能极大简化 jdbc 编码的工作量</font>，同时也不会影响程序的性能。
2. API介绍：
	1. `org.apache.commons.dbutils.QueryRunner`
	2. `org.apache.commons.dbutils.ResultSetHandler`
	3. 工具类：`org.apache.commons.dbutils.DbUtils`
3. Apache-DBUtils 需导入的 jar 包

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F24、Apache-DBUtils需导入的jar包.png)

![](https://www.yue-hai.top:10300/file/downloadPublicFile?basePathType=takeDown&subPath=%2Fjava%2Fattachments%2F25、Apache-DBUtils的接口.png)

## 2、主要 API 的使用

### 1、DbUtils

- `DbUtils` ：提供如关闭连接、装载JDBC驱动程序等常规工作的工具类，里面的所有方法都是静态的。主要方法如下：
1. `public static void close(…) throws java.sql.SQLException`： DbUtils 类提供了三个重载的关闭方法。这些方法检查所提供的参数是不是NULL，如果不是的话，它们就关闭 Connection、Statement 和 ResultSet。
2. `public static void closeQuietly(…)`：这一类方法不仅能在Connection、Statement和ResultSet为NULL情况下避免关闭，还能隐藏一些在程序中抛出的SQLEeception。
3. `public static void commitAndClose(Connection conn) throws SQLException`： 用来提交连接的事务，然后关闭连接
4. `public static void commitAndCloseQuietly(Connection conn)`： 用来提交连接，然后关闭连接，并且在关闭连接时不抛出SQL异常。
5. `public static void rollback(Connection conn)throws SQLException`：允许conn为null，因为方法内部做了判断
6. `public static void rollbackAndClose(Connection conn)throws SQLException`
7. `rollbackAndCloseQuietly(Connection)`
8. `public static boolean loadDriver(java.lang.String driverClassName)`：这一方装载并注册JDBC驱动程序，如果成功就返回true。使用该方法，不需要捕捉这个异常 ClassNotFoundException。
### 2、QueryRunner 类

1. 该类简单化了 SQL 查询，它与 ResultSetHandler 组合在一起使用可以完成大部分的数据库操作，能够大大减少编码量。
2. QueryRunner 类提供了两个构造器：
	1. 默认的构造器
	2. 需要一个 `javax.sql.DataSource` 来作参数的构造器
3. QueryRunner类的主要方法：
	1. <font color="red">更新</font>
		1. `public int update(Connection conn, String sql, Object... params) throws SQLException`：用来执行一个<font color="red">更新（插入、更新或删除）操作</font>。
		2. ......
	2. <font color="red">插入</font>
		1. `public T insert(Connection conn,String sql,ResultSetHandler rsh, Object... params) throwsSQLException`：只支持 INSERT 语句，其中 rsh - The handler used to create the result object fromthe ResultSet of auto-generated keys. 返回值: An object generated by the handler.即自动生成的键值
		2. ....
	3. <font color="red">批处理</font>
		1. `public int[] batch(Connection conn,String sql,Object[][] params)throws SQLException`： INSERT,UPDATE, or DELETE语句
		2. `public T insertBatch(Connection conn,String sql,ResultSetHandler rsh,Object[][] params)throwsSQLException`：只支持INSERT语句
		3. .....
	4. <font color="red">查询</font>
		1. `public Object query(Connection conn, String sql, ResultSetHandler rsh,Object... params) throwsSQLException`：执行一个查询操作，在这个查询中，对象数组中的每个元素值被用来作为查询语句的置换参数。该方法会自行处理 PreparedStatement 和 ResultSet 的创建和关闭。
		2. ......
4. 测试：

```java
/**
* commons-dbutils 是 Apache 组织提供的一个开源 JDBC工具类库
* 封装了针对于数据库的增删改查操作
*/
public class QueryRunnerTest {

  // 更新（增删改）数据库
  @Test
  public void test1() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "INSERT INTO customers(name,email,birth) VALUES(?,?,?);";

		   // 调用QueryRunner对象的update()方法，更新（增删改）数据库
		   // 参数1：数据库连接对象，参数2：sql语句，参数3：占位符参数
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   int update = runner.update(conn, sql, "言", "123@qq.com", "1999-09-09");

		   // 打印返回值
		   System.out.println("添加了" + update + "条参数");
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  // 查询 一条记录
  // BeanHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
  @Test
  public void test2() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT id,name,email,birth FROM customers WHERE id = ?";

		   // BeanHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   BeanHandler<Customers> handler = new BeanHandler<>(Customers.class);

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的handler对象，参数4：占位符参数
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   Customers query = runner.query(conn, sql, handler, 1);

		   // 打印返回值
		   System.out.println(query);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  // 查询 多条记录
  // BeanListHandler：是ResultSetHandler接口的实现类，用于封装表中的多条记录构成的集合
  @Test
  public void test3() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT id,name,email,birth FROM customers WHERE id > ?";

		   // BeanListHandler：是ResultSetHandler接口的实现类，用于封装表中的多条记录构成的集合
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   BeanListHandler<Customers> listHandler = new BeanListHandler<>(Customers.class);

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的listHandler对象，参数4：占位符参数
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   List<Customers> query = runner.query(conn, sql, listHandler, 1);

		   // 打印返回值
		   query.forEach(System.out::println);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  // 查询 一条记录，以键值对的方式呈现
  // MapHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
  @Test
  public void test4() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT id,name,email,birth FROM customers WHERE id = ?";

		   // MapHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   MapHandler mapHandler = new MapHandler();

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的mapHandler对象，参数4：占位符参数
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   Map<String, Object> query = runner.query(conn, sql, mapHandler, 1);

		   // 打印返回值
		   System.out.println(query);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  // 查询 多条记录，以键值对的方式呈现
  // MapListHandler：是ResultSetHandler接口的实现类，用于封装表中的多条记录构成的集合
  // 将字段及相应字段的值作为map中的key和value，将这些map添加到list中
  @Test
  public void test5() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT id,name,email,birth FROM customers WHERE id = ?";

		   // BeanListHandler：是ResultSetHandler接口的实现类，用于封装表中的多条记录构成的集合
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   MapListHandler listHandler = new MapListHandler();

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的listHandler对象，参数4：占位符参数
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   List<Map<String, Object>> query = runner.query(conn, sql, listHandler, 1);

		   // 打印返回值
		   System.out.println(query);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  //
  // 查询 一条记录
  @Test
  public void test6() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT COUNT(*) FROM customers";

		   // ScalarHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   ScalarHandler scalarHandler = new ScalarHandler();

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的scalarHandler对象
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   long query = (long) runner.query(conn, sql, scalarHandler);

		   // 打印返回值
		   System.out.println(query);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

  //
  // 查询 一条记录
  @Test
  public void test7() throws Exception {

	 Connection conn = null;

	 try {
		   // 获取QueryRunner对象
		   QueryRunner runner = new QueryRunner();

		   // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		   conn = DruidJDBCUtils.getConnection();

		   // sql语句
		   String sql = "SELECT MAX(birth) FROM customers";

		   // ScalarHandler：是ResultSetHandler接口的实现类，用于封装表中的一条记录
		   // 泛型与传入的参数为所查询的数据库的表所对应的类的class
		   ScalarHandler scalarHandler = new ScalarHandler();

		   // 调用QueryRunner对象的query()方法，查询数据库
		   // 参数1：数据库连接对象，参数2：sql语句
		   // 参数3：上面的scalarHandler对象
		   // 此接口方法添加日期时，可以直接传入字符串
		   // 此方法有返回值，为总共更新了多少条数据
		   Date query = (Date) runner.query(conn, sql, scalarHandler);

		   // 打印返回值
		   System.out.println(query);
	 } catch (Exception e) {
		   e.printStackTrace();
	 } finally {
		   // 调用我们自己封装的方法，创关闭数据库连接
		   JDBCUtils.closeResource(conn,null);
	 }

  }

}
```

## 3、ResultSetHandler 接口及实现类

1. 该接口用于处理 `java.sql.ResultSet`，将数据按要求转换为另一种形式。
2. `ResultSetHandler` 接口提供了一个单独的方法：`Object handle (java.sql.ResultSet .rs)`
3. 接口的主要实现类：
	1. `ArrayHandler`：把结果集中的第一行数据转成对象数组。
	2. `ArrayListHandler`：把结果集中的每一行数据都转成一个数组，再存放到List中。
	3. `BeanHandler`：将结果集中的第一行数据封装到一个对应的JavaBean实例中。
	4. `BeanListHandler`：将结果集中的每一行数据都封装到一个对应的JavaBean实例中，存放到List里。
	5. `ColumnListHandler`：将结果集中某一列的数据存放到List中。
	6. `KeyedHandler`(name)：将结果集中的每一行数据都封装到一个Map里，再把这些map再存到一个map里，其key为指定的key。
	7. `MapHandler`：将结果集中的第一行数据封装到一个Map里，key是列名，value就是对应的值。
	8. `MapListHandler`：将结果集中的每一行数据都封装到一个Map里，然后再存放到List
	9. `ScalarHandler`：查询单个值对象

```java
// 自定义ResultSetHandler的实现类完成查询操作
public class Demo02 {
 public static void main(String[] args) {

	Connection conn = null;

	try {
		  // 获取QueryRunner对象
		  QueryRunner runner = new QueryRunner();

		  // 调用我们自己封装的方法，创建druid数据库连接池和数据库连接
		  conn = DruidJDBCUtils.getConnection();

		  // sql语句
		  String sql = "SELECT id,name,email,birth FROM customers WHERE id > ?";

		  // 自定义ResultSetHandler的实现类完成查询操作
		  ResultSetHandler<Customers> handler = new ResultSetHandler<Customers>() {
			 @Override
			 public Customers handle(ResultSet resultSet) throws SQLException {
				// 可以直接赋值
				// return new Customers(12,"言","111@qq.com",new Date(3248947389527894317L));

				// 自定义
				if(resultSet.next()){
					  int id = resultSet.getInt("id");
					  String name = resultSet.getString("name");
					  String email = resultSet.getString("email");
					  Date birth = resultSet.getDate("birth");
					  return new Customers(id,name,email,birth);

				}
				return null;
			 }
		  };

		  // 调用QueryRunner对象的query()方法，查询数据库
		  // 参数1：数据库连接对象，参数2：sql语句
		  // 参数3：上面的自定义的ResultSetHandler对象，参数4：占位符参数
		  // 此接口方法添加日期时，可以直接传入字符串
		  // 此方法有返回值，为总共更新了多少条数据
		  Customers query = runner.query(conn, sql, handler, 1);

		  // 打印返回值
		  System.out.println(query);
	} catch (Exception e) {
		  e.printStackTrace();
	} finally {
		  // 调用我们自己封装的方法，创关闭数据库连接
		  JDBCUtils.closeResource(conn,null);
	}

 }
}
```

## 4、DbUtils 关闭资源的操作

1. 方式一：

```java
/**
 * 增删改的关闭操作
 * 关闭数据库连接和Statement的操作
 * @param conn
 * @param ps
 */
public static void closeResource(Connection conn, PreparedStatement ps){
	// 方式一：
	try {
		DbUtils.close(conn);
	} catch (SQLException throwables) {
		throwables.printStackTrace();
	}
	try {
		DbUtils.close(ps);
	} catch (SQLException throwables) {
		throwables.printStackTrace();
	}
}

// ****源码************************************

public static void close(Connection conn) throws SQLException {
	if (conn != null) {
		conn.close();
	}
}
```

2. 方式二：

```java
/**
 * 增删改的关闭操作
 * 关闭数据库连接和Statement的操作
 * @param conn
 * @param ps
 */
public static void closeResource(Connection conn, PreparedStatement ps){
	// 方式二：
	DbUtils.closeQuietly(conn);
	DbUtils.closeQuietly(ps);
}

// ****源码************************************

public static void closeQuietly(Connection conn) {
	try {
		close(conn);
	} catch (SQLException e) {
		// quiet
	}
}
```
