# 一、问题记录

## 1、mysql 重置自增主键

1. `TRUNCATE TABLE 表名`
2. 清空表

## 5、

## 6、

## 7、

## 8、

## 9、

# 二、MySQL 的安装

## 1、windows

### ①、MySQL 免安装版

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

### ②、MySQL 修改密码

1. 首先需要启动 MySQL 服务：`net start mysql`
2. 登陆：`mysql -u root -p 刚才记录的密码`
3. 出现 `mysql>` 的时候就可以去改密码了

![|683](attachments/Pasted%20image%2020231101132335.png)

4. 修改 root 密码：

```cmd
ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
```

5. 密码修改成功后退出 mysql：`exit;`

### ③、MySQL 设置允许外部连接访问

1. 查询 mysql 用户权限

```sql
select host, user from user;
```

2. 设置 mysql root 用户允许外部连接访问

```sql
update user set Host='%' where User='root';
```

3. 再次查询 mysql 用户权限

```sql
select host, user from user;
```

4. 刷新

```sql
flush privileges;
```

5. 此时即可远程连接

![](attachments/Pasted%20image%2020231101133013.png)

## 2、linux

### ①、ubuntu 安装

1. 更新系统包列表：

```shell
sudo apt update
```

2. 查看可用版本：

```shell
apt-cache madison mysql-server
```

3. 安装特定版本：

```shell
sudo apt install mysql-server=8.0.37-0ubuntu0.20.04.3
```

4. 安装默认最新的稳定版：

```shell
sudo apt install mysql-server
```

5. 运行安全配置脚本，该脚本会设置密码策略和移除匿名用户等：
	1. 设置密码验证组件：这个组件可以检查密码强度，确保只有足够安全的密码可以被设置
	2. 删除匿名用户：默认情况下，MySQL安装后会存在匿名用户，允许任何人无需登录即可连接数据库。这主要是为了测试和简化安装过程
	3. 限制 root 用户只能从 localhost 连接：通常，为了安全考虑，应该只允许 root 用户从本地机器（localhost）连接，这可以防止远程尝试猜测root密码
	4. 删除测试数据库：MySQL 默认会创建一个名为 test 的数据库，任何人都可以访问。这同样主要是为了测试目的
	5. 重新加载权限表：为了让之前做的所有更改立即生效，系统提示你是否重新加载权限表

```shell
sudo mysql_secure_installation
```

6. 检查 MySQL 服务状态：

```shell
sudo systemctl status mysql.service
```

7. 如果服务没有运行，可以使用以下命令启动它：

```shell
sudo systemctl start mysql
```

8. 直接以 root 用户登录：

```shell
sudo mysql -u root -p
```

```shell
yan@yuehai:~/apply$ sudo mysql -u root -p
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 8.0.39-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

### ②、更改密码

1. 直接以 root 用户登录：

```shell
sudo mysql
```

2. 更改 root 用户的认证方式，以便能够使用密码进行认证：

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';
```

3. 重新加载权限表，使更改立即生效

```sql
FLUSH PRIVILEGES;
```

4. 退出 MySQL：

```shell
exit
```

5. 使用非 root 用户登录，输入刚才修改的密码：

```shell
mysql -u root -p
```

### ③、创建新用户

1. 创建新用户：
	1. `yan` 是新用户的用户名
	2. `%` 表示这个用户可以从任何主机连接
	3. `new_password` 是这个用户的密码。

```shell
CREATE USER 'yan'@'%' IDENTIFIED BY 'new_password';
```

2. 授权对特定数据库的完全控制权，假设希望这个新用户能够访问名为 `example_db` 的数据库，可以使用以下命令授予相应权限：
	1. `GRANT` 命令可以针对尚未存在的数据库设置权限。
	2. 这意味着可以先为用户授予权限，之后再创建数据库。
	3. 这在多用户环境中非常有用，允许管理员事先设置权限策略。

```shell
GRANT ALL PRIVILEGES ON example_db.* TO 'yan'@'%';
```

3. 授予创建数据库的权限，`.` 表示对所有数据库和所有表的操作权限，但这里仅限于创建操作：

```shell
GRANT CREATE ON *.* TO 'yan'@'%';
```

4. 使权限更改立即生效：

```shell
FLUSH PRIVILEGES;
```

5. 查看是否修改成功：

```shell
SHOW GRANTS FOR 'yan'@'%';
```

6. 删除用户：

```shell
DROP USER 'yan'@'%';
```

7. 使权限更改立即生效：

```shell
FLUSH PRIVILEGES;
```

8. 查看所有用户及其关联的主机：

```shell
SELECT User, Host FROM mysql.user;
```

9. 退出 MySQL：

```shell
exit
```

### ④、配置允许远程连接

1. MySQL 默认配置通常只允许本地连接。需要编辑 MySQL 的配置文件 `my.cnf`（或 `my.ini`，取决于系统），确保 `bind-address` 参数被设置为允许远程连接（例如，设置为 `0.0.0.0` 允许从任何地址连接，或者特定的服务器 IP 地址）。
2. 在 Ubuntu 上，这个配置文件通常位于 `/etc/mysql/mysql.conf.d/mysqld.cnf`：

```shell
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

3. 找到 `bind-address` 项，更改为：

```shell
bind-address = 0.0.0.0
```

4. 保存文件并退出编辑器。
5. 修改配置后，需要重启 MySQL 服务以使更改生效：

```shell
sudo systemctl restart mysql.service
```

## 3、

## 4、

## 5、

## 6、

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















