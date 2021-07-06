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
        BOARD.led_on()
        #print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print ("Receive: ")
        mens = bytes(payload).decode("utf-8",'ignore')
        mens=mens[2:-1]
        print(mens) # Receive DATA
        BOARD.led_off()
        if mens=="P1ON":
            print("Received data request P1ON")
            GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
            time.sleep(2)
            print ("Send mens: P1ON1")
            self.write_payload([255, 255, 0, 0, 80, 49, 79, 78, 49, 0]) # Send DATA RASPBERRY PI
            self.set_mode(MODE.TX)
        elif mens=="P1OFF":
            print("Received data request P1OFF")
            GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
            time.sleep(2)
            print ("Send mens: P1OFF1")
            self.write_payload([255, 255, 0, 0, 80, 49, 79, 70, 70, 49, 0]) # Send DATA RASPBERRY PI
            self.set_mode(MODE.TX)
        elif mens=="P2OFF2":
            print("Received data request P2OFF2")
            GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
            GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
        elif mens=="P2ON2":
            print("Received data request P2ON2")
            GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
            GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
        time.sleep(2)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        print("\nTxDone")
        print(self.get_irq_flags())

    def on_cad_done(self):
        print("\non_CadDone")
        print(self.get_irq_flags())

    def on_rx_timeout(self):
        print("\non_RxTimeout")
        print(self.get_irq_flags())

    def on_valid_header(self):
        print("\non_ValidHeader")
        print(self.get_irq_flags())

    def on_payload_crc_error(self):
        print("\non_PayloadCrcError")
        print(self.get_irq_flags())

    def on_fhss_change_channel(self):
        print("\non_FhssChangeChannel")
        print(self.get_irq_flags())

    def receiver(self):          
            self.reset_ptr_rx()
            self.set_mode(MODE.RXCONT) # Receiver mode
            start_time = time.time()
            while True:
                pass;

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
RELAIS_1_GPIO = 26
RELAIS_2_GPIO = 19
RELAIS_3_GPIO = 6
# RELAIS_4_GPIO = 5

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
# GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

assert(lora.get_agc_auto_on() == 1)

try:
    print("START")
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # on
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
    while True:
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
