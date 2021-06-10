import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(38,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(40,GPIO.RISING,callback=button_callback)
# message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up