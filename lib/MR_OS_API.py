import os

class listbox:
    def __init__(self,oled,path="/lib/SCHPORA/"):
        self.oled=oled
        self.index=0
        self.index_page=0
        self.payloads_dict=self.get_dir(path)
        self.get_page_payloads()
        
    
    
    
    
    
    
    
    def get_page_payloads(self):
        for inde,lista in self.payloads_dict.items():
            if  inde==self.index_page:
                self.page_payloads=lista
    
    def get_dir(self,path="/lib/SCHPORA"):
        payloads=os.listdir(path)
        payloads=sorted(payloads)
        payloads_dict={}
        for i in range(0,len(payloads),5):
            payloads_dict[i//5]=payloads[i:i+5]
        return payloads_dict
    
    
    
    def draw_listbox(self):
        self.oled.clear()
        pos_y=10
        for index_en,item in enumerate(self.page_payloads):
            self.oled.text(item,10,pos_y,"AA");
            if index_en==self.index:
                self.oled.circle(80,pos_y+3,3,1)
            pos_y+=10;
            self.oled.text(f"{self.index_page+1}/{len(self.payloads_dict)}",100,5,"AAA")
        self.oled.show()
    
    
    def down(self):
        self.index+=1
        if self.index >= len(self.page_payloads):
            if self.index_page+1<len(self.payloads_dict):
                self.index_page+=1
                self.get_page_payloads()
            elif self.index_page+1==len(self.payloads_dict):
                self.index_page=0
                self.get_page_payloads()
                
                
            self.index = 0
        
        self.draw_listbox()
    
    def up(self):
        self.index-=1
        
        if self.index == -1:
            print("up")
            if self.index_page!=0:
                self.index_page-=1
                self.get_page_payloads()
                self.index=len(self.page_payloads)-1
                
            elif self.index_page==0:
                self.index_page=len(self.payloads_dict)-1
                self.get_page_payloads()
                self.index=len(self.page_payloads)-1
                
                
        
                
        self.draw_listbox()
        
        