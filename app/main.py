# sudo apt-get -y install python3-rpi.gpio
# pip install RPi.GPIO 
# sudo pip3 install Adafruit_DHT

# import rpi_gpio

from time import sleep
import I2C_LCD_driver as mylcd


def readSensor():
    root.after(5000, readSensor)
    h,t = dht.read_retry(dht.DHT22,4)
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
        "Temperature": {"TargetTemp": 0, "TempFormat": "F"}, 
        "Humidity": 0.8,
        "Light": 0, 
        "Fan": 0
    }

def main_menu():
    p = 0
    l = [menu_options.keys()]
    n = len(l)
    while True:
        swrite("^", line=1, pos=8)
        
        swrite(menu_options[l[p]], 2, 5)
        swrite(menu_options[l[p+1]], 3, 5)

        swrite("v", 4, 8)

        if p==n-2: break

        sleep(1.5)
        p+=1
        screen.lcd_clear()

main_menu()