
# -*- coding:utf-8 -*-

import sys
sys.dont_write_bytecode = True

import os
import pyray

class TexturesLoader:
    def __init__(self, folder_path='assets/block'):
        self.folder_path = folder_path
        self.file_name = []

        self.images = {}
        self.textures = {}

    def load(self):
        file_list = []

        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
                
        for file_path in file_list:
            try:
                image = pyray.load_image(file_path)
                texture = pyray.load_texture_from_image(image)
                
                filename = os.path.splitext(os.path.basename(file_path))[0]
                self.file_name.append(filename)
                self.images[filename] = image
                self.textures[filename] = texture

            except:
                pass

        return self.images, self.textures

    def unload(self):
        for name in self.file_name:
            pyray.unload_image(self.images[name])
            pyray.unload_texture(self.textures[name])

if __name__ == '__main__':
    tl = TexturesLoader()
    images, textures = tl.load()
    print(images)
