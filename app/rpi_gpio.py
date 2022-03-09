import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False) 
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO.setup(6,GPIO.OUT) # relay 1
# GPIO.output(6,GPIO.HIGH)
# GPIO.setup(13,GPIO.OUT) # relay 2
# GPIO.output(13,GPIO.HIGH)
# GPIO.setup(19,GPIO.OUT) # relay 3
# GPIO.output(19,GPIO.HIGH)
# GPIO.setup(26,GPIO.OUT) # relay 4
# GPIO.output(26,GPIO.HIGH)