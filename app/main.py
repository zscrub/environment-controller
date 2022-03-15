from button_func import (
        is_pressed,
        BUTTON_UP,
        BUTTON_DOWN,
        BUTTON_ENTER
    )

import drivers.rpi_gpio as rpi_gpio

from time import sleep

from menu import (
        screen,
        swrite,
        menu_options, 
        menu_list,
        menu_index, 
        move_cursor
    )

def main_menu():
    p = 0
    l = list(menu_options.keys())
    M = len(l)

    # populate static menu items 
    menu_index(p)

    while True:
        sleep(0.25)
        BUTTON_UP = rpi_gpio.GPIO.input(40)
        BUTTON_DOWN = rpi_gpio.GPIO.input(38)
        BUTTON_ENTER = rpi_gpio.GPIO.input(36)

        if BUTTON_UP==is_pressed and p>0: 
            p-=1; 
            screen.lcd_clear();  
            move_cursor(p)
            
        if BUTTON_DOWN==is_pressed and p<M-1: 
            p+=1; 
            screen.lcd_clear();  
            move_cursor(p)

        if BUTTON_ENTER==is_pressed:
            selection = l[p]
            print(selection)
            print(menu_options[selection])
            screen.lcd_clear()
            screen.lcd_write(menu_options[selection])
            

main_menu()
