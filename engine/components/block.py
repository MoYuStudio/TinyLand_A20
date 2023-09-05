
import drivers

class Block:
    def __init__(self,id,pos,size):
        self.id = id
        self.pos = pos
        self.size = size
        
        self.render_id = self.id
        self.animation_frame = 0
        self.timer_list = {'animation':0,'grow':0}
        
        self.buildable = []
        
        self.sqlite_drive = drivers.SQLiteDriver()
    