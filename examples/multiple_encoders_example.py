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

enc1 = Encoder(17, 27, 0.0, 1.0, 0.1) # Encoder object, connected to GPIO pins 17 and 27, with floating point values ranging from 0 to 1 in increments of 0.1
enc2 = Encoder(23, 24, 10, 100, 10) # Encoder object, connected to GPIO pins 23 and 24, with integer values ranging from 10 to 100 in increments of 10
enc3 = Encoder(19, 26, -90, 0, 6) # Encoder object, connected to GPIO pins 16 and 26, with integer values ranging from -90 to 0 in increments of 6
    
def main():
    try:
        init()
        while True :
            time.sleep(0.1)     
            os.system('clear')
            print("Encoder 1: " + str(enc1.getValue()) + "\nEncoder 2: " + str(enc2.getValue()) + "\nEncoder 3: " + str(enc3.getValue()))

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
