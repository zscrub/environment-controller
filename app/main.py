# sudo apt-get -y install python3-rpi.gpio
# pip install RPi.GPIO 
# sudo pip3 install Adafruit_DHT
import I2C_LCD_driver as mylcd
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


GPIO.setwarnings(False) 
#BUTTON_UP=GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
#BUTTON_ENTER=GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#BUTTON_DOWN=GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(6,GPIO.OUT) ## relay 1
#GPIO.output(6,GPIO.HIGH)
#GPIO.setup(13,GPIO.OUT)##relay 2
#GPIO.output(13,GPIO.HIGH)
#GPIO.setup(19,GPIO.OUT)##relay 3
#GPIO.output(19,GPIO.HIGH)
#GPIO.setup(26,GPIO.OUT)##relay 4
#GPIO.output(26,GPIO.HIGH)



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


def populateScreen(w,x,y,z):
    mylcd.lcd_display_string("%s" %w, 1)
    mylcd.lcd_display_string("%s" %x, 2)
    mylcd.lcd_display_string("%s" %y, 3)
    mylcd.lcd_display_string("%s" %z, 4)

populateScreen("1", "3", "4", "5")
