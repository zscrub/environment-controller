from time import sleep
import I2C_LCD_driver as mylcd

screen = mylcd.lcd()
swrite = screen.lcd_display_string


menu_options = {
        "Temp": {"SetTemp": 0, "SetFormat": "F"}, 
        "Humidity": 0.8,
        "Light": 0, 
        "Fan": 0
    }

menu_list = list(menu_options.keys())

def menu_index():
    swrite("^", line=1, pos=8)
    swrite(">", 2, 3)
    swrite("v", 4, 8)

def move_cursor():
    try:
        swrite(f"{p+1}.{menu_list[p]}", 2, 5)
        print(f"{p+1}.{menu_list[p]}")
        
        swrite(f"{p+2}.{menu_list[p+1]}", 3, 5)
        print(f"{p+2}.{menu_list[p+1]}")
    except IndexError:
        swrite(" ", 2, 3)
        swrite(">", 3, 3)
