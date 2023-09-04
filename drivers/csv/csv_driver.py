
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import csv
import json

class CSVDriver:
    def __init__(self):
        self.path = 'data/block/data.csv'
        self.data = []
        self.header = ['id', 'data']
        
    def read(self):
        # 打开CSV文件
        with open(self.path, 'r') as file:
            reader = csv.reader(file)

            # 遍历CSV文件中的每一行
            for row in reader:
                # 将包含数组或字典的单元格解析为Python对象
                row_data = []
                for cell in row:
                    try:
                        # 尝试解析单元格数据为Python对象
                        cell_data = json.loads(cell)
                        row_data.append(cell_data)
                    except (json.JSONDecodeError, ValueError):
                        row_data.append(cell)
                
                self.data.append(row_data)
                
    def write(self):
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # 写入表头
            writer.writerow(self.header)
            
            # 写入数据
            writer.writerows(self.data)
            
if __name__ == '__main__':
    csv_driver = CSVDriver()
    csv_driver.read()
    
    print(csv_driver.data)
    
    index = csv_driver.data[0].index('buildable')
    print(index)
    print(csv_driver.data[1][4])
    print(type(csv_driver.data[1][4]))