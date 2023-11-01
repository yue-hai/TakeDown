# 一、问题记录

## 1、mysql 重置自增主键

1. `TRUNCATE TABLE 表明`
2. 清空表

## 2、MySQL 免安装版 Windows 安装

1. 下载 MySQL 免安装版：https://dev.mysql.com/downloads/mysql/

![|700](attachments/Pasted%20image%2020231101130323.png)

2. 将下载的压缩包解压至目录，如：`D:\Java\SQL\MySqlmysql-8.2.0`
3. 配置初始化文件 `my.ini`：解压后的目录并没有 `my.ini` 文件，需要手动创建

```ini
[mysqld]
# 设置 3306 端口
port=3306
# 设置 mysql 的安装目录，一定要与上面的安装路径保持一致
basedir=D:\\Java\\SQL\\MySql\\mysql-8.2.0
# 设置 mysql 数据库的数据的存放目录，自动生成，无需手动创建，当然也可以放在其他地方
datadir=D:\\Java\\SQL\\MySql\\mysql-8.2.0\\data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。
max_connect_errors=10
# 服务端使用的字符集默认为 utf8mb4
character-set-server=utf8mb4
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用 mysql_native_password 插件认证
# mysql_native_password
default_authentication_plugin=mysql_native_password
# 允许外网连接
bind-address=0.0.0.0
[mysql]
# 设置 mysql 客户端默认字符集
default-character-set=utf8mb4
[client]
# 设置 mysql 客户端连接服务端时默认使用的端口，不建议修改，这是公认端口号
port=3306
default-character-set=utf8mb4
```

4. 初始化 MySQL：
	1. 进入 cmd ，切换到 `D:\Java\SQL\MySqlmysql-8.2.0\bin` 目录下
	2. 执行：`mysqld --initialize --console` 初始化 MySQL

```cmd
d:

cd D:\Java\SQL\MySqlmysql-8.2.0\bin

mysqld --initialize --console
```

5. 记录下初始化的密码

![|875](attachments/Pasted%20image%2020231101130921.png)

6. 安装 mysql 服务：`mysqld --install`
7. 出现 `Service successfully installed` 代表安装成功了
8. 启动和关闭 mysql 服务的指令：

```cmd
# 启动 mysql 的服务
net start mysql

# 关闭 mysql 服务
net stop mysql
```

## 3、MySQL 修改密码

1. 首先需要启动 MySQL 服务：`net start mysql`
2. 登陆：`mysql -u root -p 刚才记录的密码`
3. 出现 `mysql>` 的时候就可以去改密码了

![|683](attachments/Pasted%20image%2020231101132335.png)

4. 修改密码：

```cmd
ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
```

5. 密码修改成功后退出 mysql：`exit;`

## 4、MySQL 设置允许外部连接访问

1. 查询 mysql 用户权限

```sql
select host, user from user;
```

![|700](attachments/Pasted%20image%2020231101132912.png)

2. 设置 mysql 允许外部连接访问

```sql
update user set Host='%' where User='root';
```

3. 再次查询 mysql 用户权限

```sql
select host, user from user;
```

![](attachments/Pasted%20image%2020231101133013.png)

4. 刷新

```sql
flush privileges;
```

## 5、

## 6、

## 7、

## 8、

## 9、

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















