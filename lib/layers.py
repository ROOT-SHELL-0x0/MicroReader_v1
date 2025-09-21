from time import sleep

def main_layer_load():
    return """oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1);oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1);oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1)"""


def read_file(path):
    f=open(path,"r")
    return f.read()
def display_text(oled,data):
    oled.text(data)
    sleep(0.1)
    oled.show()