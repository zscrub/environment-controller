from operator import truediv


import rpi_gpio

button_up_pressed = False
button_up_released = False
button_down_pressed = False
button_down_released = False
button_enter_pressed = False
button_enter_released = False


def button_up():
    print("testing")
    while button_up_pressed == False and rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.HIGH: #button pressed
        #button_up_pressed = True
        print("up button pressed")
        if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.LOW:
            button_up_released = False
        break

def button_down_pressed():
    while button_down_pressed == False and rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.HIGH: #button pressed
        #button_down_pressed == True
        print("down button pressed")
        if rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.LOW:
            button_down_released = False
        break

def button_enter_pressed():
    while button_down_pressed == False and rpi_gpio.GPIO.input(36) == rpi_gpio.GPIO.HIGH: #button pressed
        #button_enter_pressed == True
        print("enter button pressed")
        if rpi_gpio.GPIO.input(36) == rpi_gpio.GPIO.LOW:
            button_enter_released = False
        break