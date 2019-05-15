# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
cursor.rowcount
# 获得查询结果集:
values = cursor.fetchall()
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

-------------------------------------
可能用到语句范例(貌似没啥特别要注意的)

UPDATE user SET name = '23' WHERE id = 2
DELETE FROM table WHERE id = 1
INSERT INTO user(id,name,king) VALUES(0,'12','US')
SELECT columns FROM tale WHERE iddf = 'oiu14' 
count() distinct
