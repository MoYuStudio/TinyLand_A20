
import pyray

import drivers

class Block:
    def __init__(self,id,pos,size,block_textures):
        self.id = id
        self.pos = pos
        self.size = size
        self.block_textures = block_textures
        
        self.render_id = self.id
        self.alpha = 255
        
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
        
    def load(self):
        pass
    
    def input(self):
        if pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
            mouse_pos = pyray.get_mouse_position()
            
            # 计算鼠标点击位置所对应的方块的坐标
            block_x = int((mouse_pos.x - self.pos['x']) / self.size)
            block_y = int((mouse_pos.y - self.pos['y']) / self.size)
            
            # 打印点击的方块坐标
            print(f"Clicked on block at ({block_x}, {block_y})")
    
    def logic(self):
        pass
    
    def render(self):
        tile_texture = self.block_textures[self.render_id]
        source_rect = pyray.Rectangle(0, 0, tile_texture.width, tile_texture.height)
        dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.block_width, self.block_height)
        rotation = 0.0
        
        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
        
if __name__ == '__main__':
    pass
    