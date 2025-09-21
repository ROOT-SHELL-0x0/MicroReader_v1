from time import sleep

def main_layer_load():
    return """oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1);oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1);oled.text("BadPico", 20, 10,"aa",size=2);oled.show();sleep(0.1);oled.fill(0);oled.show();sleep(0.1)"""


def read_file(path):
    f=open(path,"r")
    return f.read()
def display_text(oled,data):
    
    
    
    original_x = x  # Сохраняем начальную позицию x для переноса
    char_width = 8 * self.current_scale  # Ширина символа с учётом масштаба
    char_height = 8 * self.current_scale  # Высота символа с учётом масштаба

   

    for char in data:
            # Если символ выходит за границы экрана по ширине, переносим на новую строку
        if x + char_width > self.width:
            x = original_x  # Возвращаемся к начальной позиции x
            y += char_height  # Переходим на следующую строку

                # Пересчитываем смещение для выравнивания на новой строке
            if align == "center":
                x -= (len(text) * char_width) // 2
            elif align == "right":
                x -= len(text) * char_width

                # Если текст выходит за границы экрана по высоте, прекращаем вывод
            if y + char_height > self.height:
                return  # Выходим из функции

            # Отрисовываем символ
        self._draw_char(char, x, y)
        x += char_width  # Сдвигаем позицию для следующего символа
#     
#     oled.text(data)
#     sleep(0.1)
#     oled.show()