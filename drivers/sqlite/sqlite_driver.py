
import json
import sqlite3

class SQLiteDriver:
    '''
    SQLite 数据库读取和写入模块
    '''
    def __init__(self):
        self.path = 'data/data.db'
    
    def connect(self):
        self.db_connection = sqlite3.connect(self.path)
        self.cursor = self.db_connection.cursor()
        
    def disconnect(self):
        self.cursor.close()
        self.db_connection.close()
    
    def read_all(self):
        self.connect()
        
        data = {}
        
        self.cursor.execute("SELECT * FROM block")
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
        pass

if __name__ == '__main__':
    sqlite_driver = SQLiteDriver()
    
    data = sqlite_driver.read_all()
    print(data)