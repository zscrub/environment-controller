# sudo apt-get -y install python3-rpi.gpio
# pip install RPi.GPIO 
# sudo pip3 install Adafruit_DHT

# please autopull this!

# import rpi_gpio
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

mylcd = mylcd.lcd()


def populateScreen(w, x, y, z):
    mylcd.lcd_display_string(f"{w}", 1)
    mylcd.lcd_display_string(f"{x}", 2)
    mylcd.lcd_display_string(f"{y}", 3)
    mylcd.lcd_display_string(f"{z}", 4)

populateScreen("Line >1", "Line 2?", "Line 3!", "Line ../4")
