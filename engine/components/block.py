
import drivers

class Block:
    def __init__(self,id,pos,size):
        self.id = id
        self.pos = pos
        self.size = size
        
        self.render_id = self.id
        
        self.sqlite_driver = drivers.SQLiteDriver()
        
        columns = self.sqlite_driver.get_table_columns()
        
        try:
            name_index = columns.index('name')
            
            buildable_index = columns.index('buildable')
            
            cost_index = columns.index('cost')
            production_index = columns.index('production')
            
            animation_frame_num_index = columns.index('animation_frame_num')
            animation_timer_index = columns.index('animation_timer')
            
            growing_frame_index = columns.index('growing_frame')
            growing_timer_index = columns.index('growing_timer')
            
        except:
            print(' ERRO - Engine/Components/Block : DataBase Erro [ Some Block Columns Value Missing ] ')
            pass
        
        data = self.sqlite_driver.read_all()
        
        self.name = data[id][name_index]
        self.buildable = data[id][buildable_index]
        
        self.cost = data[id][cost_index]
        self.production = data[id][production_index]
        
        self.animation_frame_num = data[id][animation_frame_num_index]
        self.growing_frame = data[id][growing_frame_index]
        self.timer_list = {'animation':data[id][animation_timer_index],'grow':data[id][growing_timer_index]}
        
        
        
if __name__ == '__main__':
    pass
    