import rpi_gpio
import button_func

from time import sleep
import I2C_LCD_driver as mylcd

from menu import menu_index

def readSensor():
    root.after(5000, readSensor)
    h,t = dht.read_retry(dht.DHT22,7)
    temp = f"{t:.1f}"
    o = u"\N{DEGREE SIGN}"

    temp_f = (t * 9.0/5.0) + 32
    temp_f = f"{temp_f:.1f} {o}F"	
	# temperature.set(temp_f)	

    hum = f"{hum:.1f}%"
	# humidity.set(hum+"  %")
	# humiditytext.set(hum)


screen = mylcd.lcd()
swrite = screen.lcd_display_string


menu_options = {
        "Temp": {"SetTemp": 0, "SetFormat": "F"}, 
        "Humidity": 0.8,
        "Light": 0, 
        "Fan": 0
    }

menu_list = list(menu_options.keys())


def main_menu():
    p = 0
    l = list(menu_options.keys())
    M = len(l)

    while True:

        menu_index()
        try:
            swrite(f"{p+1}.{menu_list[p]}", 2, 5)
            print(f"{p+1}.{menu_list[p]}")
            
            swrite(f"{p+2}.{menu_list[p+1]}", 3, 5)
            print(f"{p+2}.{menu_list[p+1]}")
        except IndexError:
            swrite(" ", 2, 3)
            swrite(">", 3, 3)

        if BUTTON_UP and p>0: p-=1
        if BUTTON_DOWN and p<M-1: p+=1
        screen.lcd_clear()

main_menu()
    
def button_test():
    i = 1
    k = 1
    while True:
        if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.HIGH: #button pressed
            swrite(f"Button 1 pressed {i} times!", 2, 5)
            print(f"Button 1 pressed {i} times!")
            i+=1

        if rpi_gpio.GPIO.input(38) == rpi_gpio.GPIO.HIGH: #button pressed
            swrite(f"Button 2 pressed {i} times!", 2, 5)
            print(f"Button 2 pressed {i} times!")
            i-=1
            # button_pressed(k)


def button_pressed(k):
    if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.LOW: #button released
        print(f"Button released {k} times!")
    k+=1


