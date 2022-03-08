from operator import truediv


import rpi_gpio

button_up_pressed = False
button_down_pressed = False
button_enter_pressed = False

def button_up():
    if button_up_pressed == False and rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.HIGH: #button pressed
        button_up_pressed = True

def button_down():
    if button_down_pressed == False and rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.HIGH: #button pressed
        button_down_pressed == True

def button_enter_pressed():
    if button_down_pressed == False and rpi_gpio.GPIO.input(36) == rpi_gpio.GPIO.HIGH: #button pressed
        button_enter_pressed == True