import busio
import adafruit_ssd1306
import board
import digitalio as io
import thisbutton as tb
import os


from lib_funcs import *
from time import sleep


Bt1=tb.thisButton(board.GP7,False)
Bt2=tb.thisButton(board.GP6,False)
Bt3=tb.thisButton(board.GP1,False)


power_pin=io.DigitalInOut(board.GP8)
power_pin.direction=io.Direction.OUTPUT
power_pin.value=True



power_pin_display=io.DigitalInOut(board.GP27)
power_pin_display.direction=io.Direction.OUTPUT
power_pin_display.value=True

gnd_pin=io.DigitalInOut(board.GP26)
gnd_pin.direction=io.Direction.OUTPUT
gnd_pin.value=False

sleep(0.1)



i2c = busio.I2C(board.GP3, board.GP2) # инициализация шины I2C
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c) # инициализация дисплея


#exec(load_gif())

index_page=0
index=0

payloads_dict=get_dir()

lista=get_page_payloads(index_page,payloads_dict)
#exec(draw_listbox(index%len(lista),lista,(index_page+1),len(payloads_dict)))

def boop(word):
    print(word + " " + "boop")

Bt1.assignClick(lambda: boop("1"))
Bt2.assignClick(lambda: boop("2"))
Bt3.assignClick(lambda: boop("3"))



data=read_file("lib/SCHPORA/data.txt")
display_text(oled,data)


while True:
    Bt1.tick()
    Bt2.tick()
    Bt3.tick()
