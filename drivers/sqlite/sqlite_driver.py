
import sqlite3

class SQLiteDriver:
    '''
    SQLite 数据库读取和写入模块
    '''

    def __init__(self, db_path):
        '''
        初始化 SQLite 数据库读取和写入模块

        Args:
            db_path (str): SQLite 数据库文件路径
        '''
        self.db_path = db_path
        self.conn = None

    def connect(self):
        '''
        连接到数据库
        '''
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"SQLite连接错误: {e}")

    def close(self):
        '''
        关闭数据库连接
        '''
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        '''
        执行查询语句

        Args:
            query (str): SQL 查询语句
            params (tuple): 查询参数 (可选)

        Returns:
            list: 查询结果的列表，每行为一个字典
        '''
        if not self.conn:
            self.connect()

        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]

            result = []
            for row in rows:
                result.append(dict(zip(column_names, row)))

            return result
        except sqlite3.Error as e:
            print(f"SQLite查询错误: {e}")
            return []

    def execute_update(self, query, params=None):
        '''
        执行更新或插入操作

        Args:
            query (str): SQL 更新或插入语句
            params (tuple): 更新或插入参数 (可选)

        Returns:
            int: 受影响的行数
        '''
        if not self.conn:
            self.connect()

        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            print(f"SQLite更新错误: {e}")
            return 0

if __name__ == '__main__':
    db_path = 'your_database.db'
    db = SQLiteDriver(db_path)

    # 示例查询
    query = "SELECT * FROM your_table"
    result = db.execute_query(query)
    print(result)

    # 关闭数据库连接
    db.close()
