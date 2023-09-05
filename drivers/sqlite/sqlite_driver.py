
# -*- coding: utf-8 -*-

import json
import sqlite3

class SQLiteDriver:
    '''
    SQLite 数据库读取和写入模块
    
    功能:
        - 连接到 SQLite 数据库
        - 获取表的列名
        - 读取表中的所有数据

    变量:
        self.path (str): 数据库文件路径
        self.table_name (str): 默认表名

    调用:
        - connect(): 连接到数据库
        - disconnect(): 断开与数据库的连接
        - get_table_columns(): 获取表的列名
        - read_all(): 读取表中的所有数据
        - write_all(): 尚未实现的方法，用于将数据写入数据库
    '''

    def __init__(self):
        '''
        初始化 SQLiteDriver 类。
        使用指定的数据库文件路径和默认的表名进行初始化。
        '''
        self.path = 'data/data.db'
        self.table_name = 'block'
    
    def connect(self):
        '''
        连接到 SQLite 数据库。
        打开与指定路径的数据库文件的连接并创建游标。
        '''
        self.db_connection = sqlite3.connect(self.path)
        self.cursor = self.db_connection.cursor()
        
    def disconnect(self):
        '''
        断开与数据库的连接。
        关闭游标和数据库连接。
        '''
        self.cursor.close()
        self.db_connection.close()
        
    def get_table_columns(self):
        '''
        获取表的列名。
        使用 PRAGMA 语句查询指定表的列信息，并返回列名列表。
        '''
        self.connect()
        
        columns = []
        
        query = f"PRAGMA table_info({self.table_name})"
        self.cursor.execute(query)
        
        column_info = self.cursor.fetchall()
        for info in column_info:
            column_name = info[1]
            columns.append(column_name)
            
        self.disconnect()
        
        return columns
    
    def read_all(self):
        '''
        读取表中的所有数据。
        执行 SELECT 查询来获取指定表中的所有数据，并以字典形式返回结果。
        '''
        self.connect()
        
        data = {}
        
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            local_row = []
            for row_each in row:
                try:
                    row_each = json.loads(row_each)
                except:
                    pass
                local_row.append(row_each)
            data[local_row[0]]=local_row[1:]
            
        self.disconnect()
            
        return data

    def write_all(self):
        '''
        尚未实现的方法，用于将数据写入数据库。
        '''
        pass

if __name__ == '__main__':
    sqlite_driver = SQLiteDriver()
    
    columns = sqlite_driver.get_table_columns()
    print(columns)
    
    data = sqlite_driver.read_all()
    print(data)
