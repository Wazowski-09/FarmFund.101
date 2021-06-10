import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 16
GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Assign mode

while True:
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # out
    time.sleep(3)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # on
    time.sleep(3)
