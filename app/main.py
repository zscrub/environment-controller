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

def populateScreen(w, x, y, z):
    swrite(f"{w}", line=1, pos=5)
    swrite(f"{x}", 2, 9)
    swrite(f"{y}", 3, 3)
    swrite(f"{z}", 4) # pos=0

# populateScreen("Line >1", "Line 2?", "Line 3!", "Line ../4")

menu_options = ["Network", "System", "Config", "assxt", "someother"]

def main_menu():
    while True:
        n = len(menu_options)
        p = 0

        # if keyboard.is_pressed("s") and p<n+1: p+=1
        swrite("^", line=1, pos=8)

        swrite(menu_options[p], line=2, pos=5)
        swrite(menu_options[p+1], line=3, pos=5)

        swrite("v", line=4, pos=8)

        if p==n: break
    
        sleep(1.5)
        p+=1

main_menu()