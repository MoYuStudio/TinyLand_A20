
import json
import sqlite3

# 指定数据库文件的路径，如果文件不存在，它将自动创建一个新的数据库文件
db_connection = sqlite3.connect('test/data.db')

# 创建一个游标对象，以执行SQL查询
cursor = db_connection.cursor()

# 例如，执行一个查询来检索数据
cursor.execute("SELECT * FROM block")

# 获取单行记录
row = cursor.fetchone()
# print("单行记录:")
# print(row)

# 如果row[2]是一个包含数组的字段，并且以文本形式存储在数据库中
array_text = row[3]

try:
    # 解析JSON数据
    array_data = json.loads(array_text)

    # 现在array_data是一个包含数组的Python列表，您可以对其进行操作
    print(type(array_data))
    print(array_data)
except:
    pass

# 获取所有行记录
all_rows = cursor.fetchall()
print("所有行记录:")
for row in all_rows:
    array_text = row[3]
    try:
        # 解析JSON数据
        array_data = json.loads(array_text)

        # 现在array_data是一个包含数组的Python列表，可以对其进行操作
        print(type(array_data))
        print(array_data)
    except:
        pass
    
    print(row)

# 如果您只需要获取一部分记录，也可以使用fetchmany方法
# all_rows = cursor.fetchmany(10)  # 获取前10行记录

# 提交更改
db_connection.commit()

# 关闭游标和数据库连接
cursor.close()
db_connection.close()
