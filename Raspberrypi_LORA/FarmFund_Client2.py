
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
        print(bytes(payload).decode("utf-8",'ignore')) # Receive DATA
        BOARD.led_off()
        time.sleep(2) # Wait for the client be ready
        print ("Send: ACK")
        self.write_payload([255, 255, 0, 0, 65, 67, 75, 0]) # Send ACK
        self.set_mode(MODE.TX)
        self.var=1

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

    # def start(self):          
    #     while True:
    #         self.reset_ptr_rx()
    #         self.set_mode(MODE.RXCONT) # Receiver mode
    #         while True:
    #             pass;

    # def receiver_front(self):
    #     while True:
    #         self.reset_ptr_rx()
    #         self.set_mode(MODE.RXCONT) # Receiver mode
    #         while True:
    #             pass;
    # def receiver(self):          
    #         self.reset_ptr_rx()
    #         self.set_mode(MODE.RXCONT) # Receiver mode
    #         while True:
    #             pass;

    def pump_on(self):
        print ("P2ON")
        # self.write_payload([255, 255, 0, 0, 73, 78, 70, 0]) # Send INF
        self.write_payload([255, 255, 0, 0, 80, 50, 79, 78, 0])
        self.set_mode(MODE.TX)
        time.sleep(3)
        self.reset_ptr_rx()
        # self.set_mode(MODE.RXCONT)
        # start_time = time.time()
        # while (time.time() - start_time < 10):
        #     self.n = self.n + 1
        #     if(self.n == 1):
        #         print ("f")
        # print(self.var)
        # self.var=0
        # self.n = 0
        # print ("g")
        # self.reset_ptr_rx()
        # print ("h")
        # self.set_mode(MODE.RXCONT)

    def pump_off(self):
        print ("P2OFF")
        # self.write_payload([255, 255, 0, 0, 73, 78, 70, 0]) # Send INF
        self.write_payload([255, 255, 0, 0, 80, 50, 79, 70, 70, 0])
        self.set_mode(MODE.TX)
        time.sleep(3)
        self.reset_ptr_rx()
        # self.set_mode(MODE.RXCONT)
        # start_time = time.time()
        # while (time.time() - start_time < 10):
        #     self.n = self.n + 1
        #     if(self.n == 1):
        #         print ("f")
        # print(self.var)
        # self.var=0
        # self.n = 0
        # print ("g")
        # self.reset_ptr_rx()
        # print ("h")
        # self.set_mode(MODE.RXCONT)

            

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
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

assert(lora.get_agc_auto_on() == 1)

try:
    # lora.start()
    print("Start")
    #lora.pump_front()
    while True:  # Run forever
        if GPIO.input(20) == GPIO.HIGH:
            print("Button on!")
            lora.pump_on()
        elif GPIO.input(21) == GPIO.HIGH:
            print("Button off!")
            lora.pump_off()
        else:
            print("else")
            #lora.receiver()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("Exit")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("Exit")
    lora.set_mode(MODE.SLEEP)
BOARD.teardown()
