import RPi.GPIO as GPIO
from time import sleep

class Encoder:
        
    def __init__(self, pin_a: int, pin_b: int, range_min, range_max, increment):        
        if type(pin_a) == type(pin_b) == int:
            self.__pin_a = pin_a
            self.__pin_b = pin_b

            self.__counter = None       
            self.__range_min = None
            self.__range_max = None
            self.__increment = None

            self.setRange(range_min, range_max, increment)
            
            GPIO.setwarnings(True)
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(self.__pin_a, GPIO.IN)
            GPIO.setup(self.__pin_b, GPIO.IN)           
            
            GPIO.add_event_detect(self.__pin_a, GPIO.RISING, callback=self.__rotation_decode, bouncetime=10)            

        else:
            raise TypeError("Arguments need to be of type int")


    def getValue(self):
        return self.__counter
    
    
    def setRange(self, range_min, range_max, increment):
        if type(range_min) != type(range_max):
            raise TypeError("Arguments need to be same type (int or float)")
        
        if type(range_min) == int or type(range_min) == float:
            if type(increment) != type(range_min):
                raise TypeError("Increment type needs to be the same type as range_min and range_max")
            
            if range_min > range_max:
                raise Exception("Invalid range")
            
            self.__range_min = range_min
            self.__range_max = range_max
            self.__increment = increment
            self.__counter = (range_min + range_max) / 2
            
            return               
        
        raise TypeError("Unsupported operand:", type(range_min))
    

    def __rotation_decode(self, pin: int):        
        sleep(0.002)
        Switch_A = GPIO.input(self.__pin_a)
        Switch_B = GPIO.input(self.__pin_b)

        if (Switch_A == 1) and (Switch_B == 0):
            if (self.__counter > self.__range_min) and ((self.__counter - self.__increment) > self.__range_min):
                self.__counter -= self.__increment
            else:
                self.__counter = self.__range_min

            while Switch_B == 0:
                Switch_B = GPIO.input(self.__pin_a)
            while Switch_B == 1:
                Switch_B = GPIO.input(self.__pin_b)
            return

        elif (Switch_A == 1) and (Switch_B == 1):
            if (self.__counter < self.__range_max) and (self.__counter + self.__increment < self.__range_max):
                self.__counter += self.__increment
            else:
                self.__counter = self.__range_max

            while Switch_A == 1:
                Switch_A = GPIO.input(pin)
            return
        else:
            return
    
    def __clear(self):
        GPIO.remove_event_detect(self.__pin_a)
    
