import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)

#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# this is only for input pins
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW, pull_up_down=GPIO.PUD_UP)

#CORRECT ("initial" is optional)
#GPIO.setup(n, RPIO.OUT, initial=RPIO.LOW)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button off!")
    #elif GPIO.input(14) == GPIO.HIGH:
     #   print("Button on!")
