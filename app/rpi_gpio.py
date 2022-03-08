import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False) 
BUTTON_DOWN=GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin to be an input pin and set initial value to be pulled low (off)

if BUTTON_DOWN: print("Button pressed 8)")

# GPIO.setup(6,GPIO.OUT) # relay 1
# GPIO.output(6,GPIO.HIGH)
# GPIO.setup(13,GPIO.OUT) # relay 2
# GPIO.output(13,GPIO.HIGH)
# GPIO.setup(19,GPIO.OUT) # relay 3
# GPIO.output(19,GPIO.HIGH)
# GPIO.setup(26,GPIO.OUT) # relay 4
# GPIO.output(26,GPIO.HIGH)