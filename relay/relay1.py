import RPi.GPIO as GPIO
import time

in1 = 36
# in2 = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
# GPIO.output(in2, False)

try:
    while True:
        GPIO.output(in1, True)
        time.sleep(1)
        GPIO.output(in1, False)
        time.sleep(1)

    #   for x in range(5):
    #         GPIO.output(in1, True)
    #         time.sleep(0.1)
    #         GPIO.output(in1, False)
    #         # GPIO.output(in2, True)
    #         time.sleep(0.1)
    #         # GPIO.output(in2, False)
      
    #   GPIO.output(in1,True)
    # #   GPIO.output(in2,True)

    #   for x in range(4):
    #         GPIO.output(in1, True)
    #         time.sleep(0.05)
    #         GPIO.output(in1, False)
    #         time.sleep(0.05)
    #   GPIO.output(in1,True)

    #   for x in range(4):
    #         GPIO.output(in2, True)
    #         time.sleep(0.05)
    #         GPIO.output(in2, False)
    #         time.sleep(0.05)
    #   GPIO.output(in2,True)



except KeyboardInterrupt:
    GPIO.cleanup()