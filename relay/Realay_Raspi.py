import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 26
RELAIS_2_GPIO = 19
RELAIS_3_GPIO = 6
RELAIS_4_GPIO = 5
GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

while True:
    print("start")
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # out
    GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_4_GPIO, GPIO.LOW)
    time.sleep(1)
    print("stop")
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # on
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
    time.sleep(1)
