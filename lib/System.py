import MR_OS_API
import thisbutton as tb
import board
class System:
    def __init__(self,oled):
        self.oled=oled
        self.main_interface=MR_OS_API.listbox(oled)
        self.Bt1=tb.thisButton(board.GP7,False)
        self.Bt2=tb.thisButton(board.GP6,False)
        self.Bt3=tb.thisButton(board.GP1,False)
        
        
        self.Bt2.assignClick(lambda: self.b_handler("down"))
        self.Bt1.assignClick(lambda: self.b_handler("up"))
        
        self.stack=[]
        self.run()
    
    
    def b_handler(self,com):
        if com=="down":
            self.main_interface.down()
        if com=="up":
            self.main_interface.up()
        
        
    def run(self):
        self.main_interface.draw_listbox()
        while True:
            self.Bt1.tick()
            self.Bt2.tick()
        
        