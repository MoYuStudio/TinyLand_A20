
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import csv

class CSVDriver:
    def __init__(self):
        self.data = {}
        self.header = ['id', 'data']
        
    def read(self):
        # 打开CSV文件
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)

            # 遍历CSV文件中的每一行
            for row in reader:
                # 每一行是一个值的列表
                print(row)
                
    def write(self):
        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            # 写入表头
            writer.writerow(self.header)
            
            # 写入数据
            writer.writerows(self.data)
            
if __name__ == '__main__':
    pass