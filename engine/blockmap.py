
import pyray

import engine

class BlockMap:
    def __init__(self):
        self.blockmap_size = 16
        
        self.block_width = 16
        self.block_height = 16
        
        self.textures_loader = engine.TexturesLoader(folder_path = 'assets/block')
        self.block_image,self.block_textures = self.textures_loader.load()
        
    def load(self):
        self.land_noise_map = engine.NoiseMap(size = self.blockmap_size)
        self.land_noise_map = self.land_noise_map.berlin_noise()
        
        self.building_noise_map = engine.NoiseMap(size = self.blockmap_size)
        self.building_noise_map = self.building_noise_map.berlin_noise()
        
    def rander(self):
        
        for x in range(0, self.blockmap_size):
            for y in range(0, self.blockmap_size):
                # land
                self.tile_x = (x - y) * self.block_width // 2
                self.tile_y = (x + y) * self.block_height // 4

                noise_value = self.land_noise_map[x][y]
                
                if -1000 <= noise_value <= 30:
                    land_index = '5'
                elif 31 <= noise_value <= 40:
                    land_index = '3'
                elif 41 <= noise_value <= 70:
                    land_index = '1'
                elif 71 <= noise_value <= 80:
                    land_index = '2'
                elif 81 <= noise_value <= 1000:
                    land_index = '4'
                else:
                    land_index = '0'
                
                
                tile_texture = self.block_textures[land_index]

                if tile_texture:
                    source_rect = pyray.Rectangle(0, 0, tile_texture.width, tile_texture.height)
                    dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.block_width, self.block_height)
                    rotation = 0.0
                    if land_index == '5':
                        transparent_color = pyray.Color(255, 255, 255, 230)
                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, transparent_color)#pyray.RAYWHITE)
                    else:
                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
                        
                # building
                self.tile_x = (x - y) * self.block_width // 2
                self.tile_y = (x + y) * self.block_height // 4 - self.block_height // 2

                noise_value = self.building_noise_map[x][y]
                
                if -1000 <= noise_value <= 50 and land_index == '1':
                    building_index = '129'
                else:
                    building_index = '0'
                    
                if land_index == '4':
                    building_index = '4'
                
                
                tile_texture = self.block_textures[building_index]

                if tile_texture:
                    source_rect = pyray.Rectangle(0, 0, tile_texture.width, tile_texture.height)
                    dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.block_width, self.block_height)
                    rotation = 0.0

                    pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
                        
    def clean(self):
        self.textures_loader.unload()