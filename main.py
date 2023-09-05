
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

import engine
import scene

class Game:
    def __init__(self):
        self.window_width = 1280
        self.window_height = 720
        
        self.window = engine.Window(width = self.window_width, height = self.window_height)
        self.window.fps_display = True
        
        self.window.init()

        self.is_scene = 'game'
        self.scene_list = {
                        'game':scene.game.Game(self.window),
                    }

        self.scene_list[self.is_scene].run()
        self.scene_list[self.is_scene].kill()
        
if __name__ == '__main__':
    game = Game()
