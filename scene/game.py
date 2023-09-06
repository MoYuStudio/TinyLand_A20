
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

import engine
import drivers

class Game:
    def __init__(self,window):
        self.window = window
        
        self.render_width = 360
        self.render_height = 180
        
        self.block_width = 16
        self.block_height = 16
        
        self.blockmap_size = 32
        
        self.view_x = 0
        self.view_y = 0
        self.view_speed = 0.06 * self.blockmap_size
        
        self.zoom_speed = 0.009
        self.min_zoom = 3
        self.max_zoom = 9
        
        self.blockmap = engine.BlockMap()
        self.blockmap.blockmap_size = self.blockmap_size
        self.blockmap.block_width = self.block_width
        self.blockmap.block_height = self.block_height
            
    def load(self):
        self.zoom_level = 3.0
        
        self.tile_map_width = self.blockmap_size * self.block_width
        self.tile_map_height = self.blockmap_size * self.block_height

        self.view_x = (pyray.get_screen_width() - self.tile_map_width) // 2
        self.view_y = (pyray.get_screen_height() - self.tile_map_height) // 4
        
        self.blockmap.load()
    
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
                
        # if pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
        #     mouse_pos = pyray.get_mouse_position()
            
        #     mouse_pos_map_x = (mouse_pos.x - self.view_x) / self.zoom_level
        #     mouse_pos_map_y = (mouse_pos.y - self.view_y) / self.zoom_level
        #     tile_x = int(mouse_pos_map_x / self.block_width)+self.blockmap_size//2
        #     tile_y = int(mouse_pos_map_y / self.block_height)+self.blockmap_size//4


        #     print("Clicked on tile at ({}, {})".format(tile_x, tile_y))
        #     if 0 <= tile_x < self.blockmap_size and 0 <= tile_y < self.blockmap_size:
        #         self.noise_map[tile_x][tile_y] = 5
            
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

        self.blockmap.rander()
        
        pyray.end_mode_2d()
        
    def clean(self):
        self.blockmap.clean()
    
    def run(self):
        self.window.load = self.load
        
        self.window.input = self.input

        self.window.logic = self.logic
            
        self.window.render = self.render
        
        self.window.clean = self.clean
        
        self.window.set()
        
    
if __name__ == '__main__':
    pass