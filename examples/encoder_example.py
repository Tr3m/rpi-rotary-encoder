import RPi.GPIO as GPIO
import time
import os
import sys
sys.path.append('..')

from Encoder import Encoder

def init():
    print("Rotary Encoder Example")
    
    # Setup RPi pins
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    return

my_encoder = Encoder(17, 27, 0.0, 1.0, 0.1) # Initialize an Encoder object, connected on GPIO pins 17 and 27, with values ranging from 0 to 1 floating point.
    
def main():
    try:
        init()
        while True :
            time.sleep(0.1)     
            os.system('clear')
            print("Encoder Value: " + str(my_encoder.getValue()))

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
