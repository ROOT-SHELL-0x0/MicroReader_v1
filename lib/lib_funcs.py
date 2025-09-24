import os
from time import sleep




def get_dir():
    payloads=os.listdir("/lib/SCHPORA")
    payloads=sorted(payloads)
    payloads_dict={}
    for i in range(0,len(payloads),5):
        payloads_dict[i//5]=payloads[i:i+5]
    return payloads_dict

def get_page_payloads(index,dicta):
    for inde,lista in dicta.items():
        if  inde==index:
            return lista

def get_height_text(text):
    return len(text)%21*10




def read_file(path):
    f=open(path,"r")
    return f.read()

# def reset_by_button(Bt1,Bt2):
#     if Bt1.isHeld and Bt2.isHeld:
#         print("reseting")
#     else:
#         print(Bt1.isHeld)
#         print(Bt2.isHeld)
#     
    
#     
#     list_of_stroks = []
#     start = 0
#     while start < len(data):
#         end = start + 21
#         list_of_stroks.append(data[start:end])
#         start = end
#     
#     
#     last=1
#     for stroka in list_of_stroks:
#         oled.text(stroka,1,last,"AA",font_name="Fontw8h5s1.bin")
#         last+=8
#     sleep(0.1)
   









def draw_listbox(oled,index,lista,page_tec,page_max):
    oled.clear()
    pos_y=10
    for index_en,item in enumerate(lista):
        oled.text(item,10,pos_y,"AA");
        if index_en==index:
            oled.circle(80,pos_y+3,3,1)
        pos_y+=10;
        oled.text(f"{page_tec}/{page_max}",100,5,"AAA")
    oled.show();
    


def load_gif():
    stra="""oled.fill(0);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3);oled.fill(0);oled.show();sleep(0.5);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3);oled.fill(0);oled.show();sleep(0.5);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3)"""
    return stra

