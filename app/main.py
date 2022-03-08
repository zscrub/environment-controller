# sudo apt-get -y install python3-rpi.gpio
# pip install RPi.GPIO 
# sudo pip3 install Adafruit_DHT

import rpi_gpio

from time import sleep
import I2C_LCD_driver as mylcd


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
    n = len(l)
    while True:

        swrite("^", line=1, pos=8)
        swrite(">", 2, 3)

        swrite(f"{p+1}.{menu_list[p]}", 2, 5)
        print(f"{p+1}.{menu_list[p]}")

        swrite(f"{p+2}.{menu_list[p+1]}", 3, 5)
        print(f"{p+2}.{menu_list[p+1]}")

        swrite("v", 4, 8)

        if p==n-2:
            sleep(1.5) 
            swrite(" ", 2, 3)
            swrite(">", 3, 3)
            break

        sleep(1.5)
        p+=1
        screen.lcd_clear()

    
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
            #button_pressed(k)


def button_pressed(k):
    if rpi_gpio.GPIO.input(40) == rpi_gpio.GPIO.LOW: #button released
        print(f"Button released {k} times!")
    k+=1
        


button_test()