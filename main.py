
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

# 初始化窗口和瓷砖地图
pyray.init_window(1280, 720, 'TinyLand')
window_icon = pyray.load_image('assets/icon/icon.png')
pyray.set_window_icon(window_icon)
# set_target_fps(120)

# 加载图片
grass_image = pyray.load_image('assets/block/1.png')
# 创建贴图
grass_texture = pyray.load_texture_from_image(grass_image)

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.RAYWHITE)

    source_rect = pyray.Rectangle(0, 0, grass_texture.width, grass_texture.height)
    dest_rect = pyray.Rectangle(0, 0, 128, 128)
    rotation = 0.0
    pyray.draw_texture_pro(grass_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
    # pyray.draw_texture(grass_texture,0,0,pyray.RAYWHITE)
    
    fps = pyray.get_fps()
    pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.GREEN)
    pyray.end_drawing()

pyray.close_window()

pyray.unload_image(grass_image)
pyray.unload_texture(grass_texture)
