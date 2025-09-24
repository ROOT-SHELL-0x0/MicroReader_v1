import MR_OS_API
import thisbutton as tb
import board
import os
class System:
    def __init__(self,oled,path="/lib/SCHPORA"):
        os.chdir("/lib/SCHPORA")
        self.file_system=MR_OS_API.file_system()
        self.oled=oled
        self.path=os.getcwd()
        self.main_interface=MR_OS_API.listbox(oled,path)
        self.Bt1=tb.thisButton(board.GP7,False)
        self.Bt2=tb.thisButton(board.GP6,False)
        self.Bt3=tb.thisButton(board.GP1,False)
        
        
        self.Bt2.assignClick(lambda: self.b_handler("down"))
        self.Bt1.assignClick(lambda: self.b_handler("up"))
        
        
        self.Bt3.assignClick(lambda: self.b_handler("select"))
        self.Bt3.assignLongPressStart(lambda: self.b_handler("escape"))
   
        
        self.stack=[]
        self.run()
    
    
    def b_handler(self,com):
        if com == "down":
            self.main_interface.down()
        elif com == "up":
            self.main_interface.up()
        elif com == "select":
            self.select()
        elif com == "escape":
            self.escape()
        else:
            print(f"Неизвестная команда: {com}")

    
            
        
    def select(self):
        element=self.main_interface.get_element()
        try:
            os.chdir(element)
            self.path=os.getcwd()
            self.stack.append(self.main_interface)
            self.main_interface=MR_OS_API.listbox(self.oled,self.path)
            code=self.main_interface.draw_listbox()
            if code=="NODATA":
                self.escape()
            
        except Exception as e:
            print(self.file_system.get_file_type(os.getcwd+"/"+element))
    
    def escape(self):
        try:
            self.main_interface=self.stack.pop()
            os.chdir("..")
            self.path=os.getcwd()
            self.main_interface.draw_listbox()
        except Exception as e:
            print(e)
        
    def run(self):
        self.main_interface.draw_listbox()
        while True:
            self.Bt1.tick()
            self.Bt2.tick()
            self.Bt3.tick()
    
        
        