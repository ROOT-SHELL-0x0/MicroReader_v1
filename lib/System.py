import MR_OS_API
import thisbutton as tb
import board
import os
class System:
    def __init__(self,oled,path="/lib/SCHPORA"):
        os.chdir("/lib/SCHPORA")
        self.window_type="listbox"
        self.file_system=MR_OS_API.file_system()
        self.oled=oled
        self.path=os.getcwd()
        self.main_interface=MR_OS_API.listbox("listbox",oled,path)
        self.Bt1=tb.thisButton(board.GP19,False)
        self.Bt2=tb.thisButton(board.GP20,False)
        self.Bt3=tb.thisButton(board.GP21,False)
        
        
        self.Bt2.assignClick(lambda: self.b_handler("down"))
        self.Bt1.assignClick(lambda: self.b_handler("up"))
        
        
        self.Bt3.assignClick(lambda: self.b_handler("select"))
        self.Bt3.assignLongPressStart(lambda: self.b_handler("escape"))
   
        
        self.stack=[]
        self.run()
    
    
    def b_handler(self,com):
        print(os.getcwd())
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
        #print("Element:"+element)
        try:
            os.chdir(element)
            self.path=os.getcwd()
            self.stack.append(self.main_interface)
            self.main_interface=MR_OS_API.listbox("listbox",self.oled,self.path)
            code=self.main_interface.draw()
            if code=="NODATA":
                self.escape()
            
        except Exception as e:
            #print(e)
            self.stack.append(self.main_interface)
            typefile=self.file_system.get_file_type(os.getcwd()+"/"+element)
            #print(typefile)
            if typefile:
                self.window_type=typefile
                self.window_set_and_view(os.getcwd()+"/"+element)
                
    
    def escape(self):
        try:
            if self.main_interface.type=="text":
                None
            else:
                os.chdir("..")
            self.main_interface=self.stack.pop()
            self.path=os.getcwd()
            self.main_interface.draw()
        except Exception as e:
            print(e)
    
    
    def window_set_and_view(self,path_to_file):
        if self.window_type=="text":
            data=self.file_system.read_file(path_to_file)
            file_obj=MR_OS_API.text("text",self.oled,data)
            self.main_interface=file_obj
            
            
            
        
    def run(self):
        self.main_interface.draw()
        while True:
            self.Bt1.tick()
            self.Bt2.tick()
            self.Bt3.tick()
    
        
        