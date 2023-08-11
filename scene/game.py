
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

class Game:
    def __init__(self,window,block_textures):
        self.window = window
        self.block_textures = block_textures
        
    def load(self):
        pass
    
    def input(self):
        pass
        
    def logic(self):
        pass
    
    def render(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)

        source_rect = pyray.Rectangle(0, 0, self.block_textures[1].width, self.block_textures[1].height)
        dest_rect = pyray.Rectangle(0, 0, 128, 128)
        rotation = 0.0
        pyray.draw_texture_pro(self.block_textures[1], source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
        # pyray.draw_texture(grass_texture,0,0,pyray.RAYWHITE)
        
        fps = pyray.get_fps()
        pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.GREEN)
        pyray.end_drawing()
    
    def run(self):
        self.window.load = self.load
        
        self.window.input = self.input

        self.window.logic = self.logic
            
        self.window.render = self.render
        
        self.window.set()
    
if __name__ == '__main__':
    pass