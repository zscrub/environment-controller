from button_func import (
        BUTTON_UP,
        BUTTON_DOWN,
        BUTTON_ENTER
    )

import drivers.rpi_gpio

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

        if BUTTON_UP: print("Button1 printed...")
        if BUTTON_DOWN: print("Button2 printed...")

        # if BUTTON_UP and p>0: p-=1; screen.lcd_clear();  move_cursor(p)
        # if BUTTON_DOWN and p<M-1: p+=1; screen.lcd_clear();  move_cursor(p)

main_menu()
