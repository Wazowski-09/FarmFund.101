import time
from SX127x.LoRa import *
#from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD
import RPi.GPIO as GPIO

BOARD.setup()
BOARD.reset()
#parser = LoRaArgumentParser("Lora tester")


class mylora(LoRa):
    def __init__(self, verbose=False):
        super(mylora, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)
        self.var=0
        self.n = 0

    def on_rx_done(self):
        print("11")
        BOARD.led_on()
        print("12")
        #print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        print("13")
        payload = self.read_payload(nocheck=True)
        print ("Receive: ")
        mens = bytes(payload).decode("utf-8",'ignore')
        print("14")
        mens=mens[2:-1]
        print("15")
        print(mens) # Receive DATA
        print("16")
        BOARD.led_off()
        print("17")
        time.sleep(2)
        print("18")
        if mens=="P1ON":
            print("Received data request P1ON")
            GPIO.output(RELAIS_RED_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_G_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_P_GPIO, GPIO.LOW)
            time.sleep(2)
            print ("Send mens: P1ON1")
            self.write_payload([255, 255, 0, 0, 80, 49, 79, 78, 49, 0]) # Send DATA RASPBERRY PI
            self.set_mode(MODE.TX)
            # self.reset_ptr_rx()
        elif mens=="P1OFF":
            print("Received data request P1OFF")
            GPIO.output(RELAIS_RED_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_G_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_P_GPIO, GPIO.HIGH)
            time.sleep(2)
            print ("Send mens: P1OFF1")
            self.write_payload([255, 255, 0, 0, 80, 49, 79, 70, 70, 49, 0]) # Send DATA RASPBERRY PI
            self.set_mode(MODE.TX)
            # self.reset_ptr_rx()
        elif mens=="P2OFF2":
            print("Received data request P2OFF2")
            GPIO.output(RELAIS_RED_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_G_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_P_GPIO, GPIO.HIGH)
        elif mens=="P2ON2":
            print("Received data request P2ON2")
            GPIO.output(RELAIS_RED_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_G_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_P_GPIO, GPIO.LOW)
        print("1")
        time.sleep(2)
        print("2")
        self.set_mode(MODE.SLEEP)
        print("3")
        self.reset_ptr_rx()
        print("4")
        self.set_mode(MODE.RXCONT)
        print("41")

    def receiver(self):     
        while True:
            print("5")     
            self.reset_ptr_rx()
            print("6")
            self.set_mode(MODE.RXCONT) # Receiver mode
            print("7")
            start_time = time.time()
            while (time.time() - start_time < 10): # wait until receive data or 10s
                    pass;
            # while True:
            #     pass;

lora = mylora(verbose=False)
#args = parser.parse_args(lora) # configs in LoRaArgumentParser.py

#     Slow+long range  Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on. 13 dBm
lora.set_pa_config(pa_select=1, max_power=21, output_power=15)
lora.set_bw(BW.BW125)
lora.set_coding_rate(CODING_RATE.CR4_8)
lora.set_spreading_factor(12)
lora.set_rx_crc(True)
#lora.set_lna_gain(GAIN.G1)
#lora.set_implicit_header_mode(False)
lora.set_low_data_rate_optim(True)

#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on 13 dBm
#lora.set_pa_config(pa_select=1)

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)
RELAIS_RED_GPIO = 26
RELAIS_G_GPIO = 19
RELAIS_P_GPIO = 6
# RELAIS_4_GPIO = 5

GPIO.setup(RELAIS_RED_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_G_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_P_GPIO, GPIO.OUT)
# GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

assert(lora.get_agc_auto_on() == 1)

try:
    print("START")
    GPIO.output(RELAIS_RED_GPIO, GPIO.HIGH)  # on
    GPIO.output(RELAIS_G_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_P_GPIO, GPIO.HIGH)
    print("ready")
    lora.receiver()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("Exit")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("Exit")
    lora.set_mode(MODE.SLEEP)
BOARD.teardown()
