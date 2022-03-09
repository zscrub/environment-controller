# import button_func

import drivers.rpi_gpio

from time import sleep

from menu import (
                    menu_index, 
                    menu_options, 
                    menu_list,
                    menu_cursor,
                    swrite
    )



def main_menu():
    p = 0
    l = list(menu_options.keys())
    M = len(l)

    while True:

        menu_index()
        move_cursor()

        if BUTTON_UP and p>0: p-=1
        if BUTTON_DOWN and p<M-1: p+=1
        screen.lcd_clear()

main_menu()