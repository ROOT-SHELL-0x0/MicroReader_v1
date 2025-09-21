import os
from time import sleep
from font import *



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
    




def read_file(path):
    f=open(path,"r")
    return f.read()

def display_text(oled,data,x=1,y=1):
     
    
    original_x = x  # Сохраняем начальную позицию x для переноса
    char_width = 8   # Ширина символа с учётом масштаба
    char_height = 8   # Высота символа с учётом масштаба

   

    for char in data:
            # Если символ выходит за границы экрана по ширине, переносим на новую строку
        if x + char_width > 128:
            x = original_x  # Возвращаемся к начальной позиции x
            y += char_height  # Переходим на следующую строку

          

                # Если текст выходит за границы экрана по высоте, прекращаем вывод
            if y + char_height > 64:
                return  # Выходим из функции

            # Отрисовываем символ
        draw_char(oled,char, x, y)
        x += char_width  # Сдвигаем позицию для следующего символа
    
    
    


def draw_char(oled,char,x,y):
    if char in font:
        char_data = font[char]
        for row in range(8):
            byte = char_data[row]
            for col in range(8):
                if byte & (1 << (7 - col)):
                    oled.pixel(x + col, y + row, 1)
    
    
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
    oled.show()









def draw_listbox(index,lista,page_tec,page_max):
    print(page_tec)
    print(page_max)
    stra=f"""
oled.fill(0)
pos_y=5
for index_en,item in enumerate({lista}):
    oled.text(item,10,pos_y,"AA");
    if index_en=={index}:
        oled.circle(80,pos_y+3,3,1)
    pos_y+=10;
oled.text(f"{page_tec}/{page_max}",100,5,"AAA");
oled.show();"""
    return stra


def load_gif():
    stra="""oled.fill(0);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3);oled.fill(0);oled.show();sleep(0.5);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3);oled.fill(0);oled.show();sleep(0.5);oled.text("SECRET",15,20,"AA",size=2);oled.show();sleep(0.3)"""
    return stra

