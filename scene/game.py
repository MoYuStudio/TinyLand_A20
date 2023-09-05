
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

import engine
import drivers

class Game:
    def __init__(self,window,block_textures):
        self.window = window
        self.block_textures = block_textures
        
        self.render_width = 360
        self.render_height = 180
        
        self.block_width = 16
        self.block_height = 16
        
        self.blockmap_size = 48
        
        self.view_x = 0
        self.view_y = 0
        self.view_speed = 0.06 * self.blockmap_size
        
        self.zoom_speed = 0.009
        self.min_zoom = 3
        self.max_zoom = 9
        
        self.noise_map = engine.NoiseMap(size = self.blockmap_size)
        self.noise_map = self.noise_map.berlin_noise()
        
        self.sqlite_drive = drivers.SQLiteDriver()
        columns = self.sqlite_drive.get_table_columns()
        print(columns)
        
        data = self.sqlite_drive.read_all()
        print(data)
            
                     
    def load(self):
        self.zoom_level = 3.0
        
        self.tile_map_width = self.blockmap_size * self.block_width
        self.tile_map_height = self.blockmap_size * self.block_height

        self.view_x = (pyray.get_screen_width() - self.tile_map_width) // 2
        self.view_y = (pyray.get_screen_height() - self.tile_map_height) // 2
    
    def input(self):
        if pyray.is_key_down(pyray.KEY_W):
            self.view_y += self.view_speed
        if pyray.is_key_down(pyray.KEY_S):
            self.view_y -= self.view_speed
        if pyray.is_key_down(pyray.KEY_A):
            self.view_x += self.view_speed
        if pyray.is_key_down(pyray.KEY_D):
            self.view_x -= self.view_speed
        if pyray.is_key_down(pyray.KEY_Q):
            self.zoom_level -= self.zoom_speed
            if self.zoom_level < self.min_zoom:
                self.zoom_level = self.min_zoom
        if pyray.is_key_down(pyray.KEY_E):
            self.zoom_level += self.zoom_speed
            if self.zoom_level > self.max_zoom:
                self.zoom_level = self.max_zoom
        
    def logic(self):
        pass
    
    def render(self):
        pyray.clear_background(pyray.BLACK)

        pyray.begin_mode_2d(pyray.Camera2D(
            pyray.Vector2(self.view_x, self.view_y),
            pyray.Vector2(self.render_width / 2, self.render_height / 2),
            0.0,
            self.zoom_level
        ))

        for x in range(0, self.blockmap_size):
            for y in range(0, self.blockmap_size):
                self.tile_x = (x - y) * self.block_width // 2
                self.tile_y = (x + y) * self.block_height // 4

                noise_value = self.noise_map[x][y]
                
                if -1000 <= noise_value <= 30:
                    tile_index = 5
                elif 31 <= noise_value <= 40:
                    tile_index = 3
                elif 41 <= noise_value <= 70:
                    tile_index = 1
                elif 71 <= noise_value <= 80:
                    tile_index = 2
                elif 81 <= noise_value <= 1000:
                    tile_index = 4
                else:
                    tile_index = 0 
                
                if tile_index >= 0 and tile_index < len(self.block_textures):
                    tile_texture = self.block_textures[tile_index]

                    if tile_texture:
                        source_rect = pyray.Rectangle(0, 0, tile_texture.width, tile_texture.height)
                        dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.block_width, self.block_height)
                        rotation = 0.0

                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        pyray.end_mode_2d()
        
    
    def run(self):
        self.window.load = self.load
        
        self.window.input = self.input

        self.window.logic = self.logic
            
        self.window.render = self.render
        
        self.window.set()
    
if __name__ == '__main__':
    pass