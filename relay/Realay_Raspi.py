import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 21
GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Assign mode

while True:
    print("start")
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # out
    time.sleep(1)
    print("stop")
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # on
    time.sleep(1)
