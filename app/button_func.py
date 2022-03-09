from operator import truediv

# temp
from menu import (
        screen,
        swrite,
        menu_options, 
        menu_list,
        menu_index, 
        move_cursor
    )


import drivers.rpi_gpio as rpi_gpio

# COMMENT HOTKEY -> CNTRL + /
# commented anything unused for now

# button_up_pressed = False
# button_up_released = False
# button_down_pressed = False
# button_down_released = False
# button_enter_pressed = False
# button_enter_released = False


# def button_up():
#     print("testing")
#     while True:
#         button_up_pressed = False
#         button_up_released = False
#         if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.HIGH: #button pressed
#             #button_up_pressed = True
#             print("up button pressed")
#             button_up_pressed = True
#         if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.LOW and button_up_pressed == True:
#             print("up button released")
#             button_up_released = True
#             button_up_pressed = False
#             break

# def button_down():
#     while button_down_pressed == False and rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.HIGH: #button pressed
#         #button_down_pressed == True
#         print("down button pressed")
#         if rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.LOW:
#             button_down_released = False
#         break

# def button_enter():
#     while button_down_pressed == False and rpi_gpio.GPIO.input(36) == rpi_gpio.GPIO.HIGH: #button pressed
#         #button_enter_pressed == True
#         print("enter button pressed")
#         if rpi_gpio.GPIO.input(36) == rpi_gpio.GPIO.LOW:
#             button_enter_released = False
#         break

def button_test():
    i = 1
    k = 1
    
    b = rpi_gpio.GPIO.input(38) 
    r = rpi_gpio.GPIO.HIGH #button pressed
    print(f"{b}=={r}") 
    while True:

        print(f"{rpi_gpio.GPIO.input(40)}=={rpi_gpio.GPIO.HIGH}", end="\r")
        if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.HIGH: #button pressed
            swrite(f"Button 1 pressed {i} times!", 2, 5)
            print(f"Button 1 pressed {i} times!")
            i+=1

        if b == r: #button pressed
            swrite(f"Button 2 pressed {i} times!", 2, 5)
            print(f"Button 2 pressed {i} times!")
            i-=1
            # button_pressed(k)
button_test()

# def button_pressed(k):
#     if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.LOW: #button released
#         print(f"Button released {k} times!")
#     k+=1

is_pressed = rpi_gpio.GPIO.HIGH
BUTTON_UP = rpi_gpio.GPIO.input(40)
BUTTON_DOWN = rpi_gpio.GPIO.input(38)
BUTTON_ENTER = rpi_gpio.GPIO.input(36)
