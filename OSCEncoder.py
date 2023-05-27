from Encoder import Encoder
from pythonosc.udp_client import SimpleUDPClient
import RPi.GPIO as GPIO
from time import sleep

class OSCEncoder(Encoder):
    def __init__(self, pin_a,  pin_b, range_min, range_max, increment, osc_client, address):        

        if type(osc_client) != SimpleUDPClient:
            raise TypeError("Unsupported operand:", type(osc_client))
        
        self.__client = osc_client
        self.__address = address
        
        Encoder.__init__(self, pin_a,  pin_b, range_min, range_max, increment)
        self._Encoder__clear()
        GPIO.add_event_detect(self._Encoder__pin_a, GPIO.RISING, callback=self._Encoder__rotation_decode, bouncetime=10)      
        

    def setAddress(self, address: str):
        if type(address) != str:
            raise TypeError("Unsupported operand:", type(address))
        
        self.__address = address
        

    def _Encoder__rotation_decode(self, pin):        
        sleep(0.002)
        Switch_A = GPIO.input(self._Encoder__pin_a)
        Switch_B = GPIO.input(self._Encoder__pin_b)

        if (Switch_A == 1) and (Switch_B == 0):
            if (self._Encoder__counter > self._Encoder__range_min) and ((self._Encoder__counter - self._Encoder__increment) > self._Encoder__range_min):
                self._Encoder__counter -= self._Encoder__increment
                self.__client.send_message(self.__address, self._Encoder__counter)
            else:
                self._Encoder__counter = self._Encoder__range_min

            while Switch_B == 0:
                Switch_B = GPIO.input(self._Encoder__pin_a)
            while Switch_B == 1:
                Switch_B = GPIO.input(self._Encoder__pin_b)
            return

        elif (Switch_A == 1) and (Switch_B == 1):
            if (self._Encoder__counter < self._Encoder__range_max) and (self._Encoder__counter + self._Encoder__increment < self._Encoder__range_max):
                self._Encoder__counter += self._Encoder__increment
                self.__client.send_message(self.__address, self._Encoder__counter)
            else:
                self._Encoder__counter = self._Encoder__range_max

            while Switch_A == 1:
                Switch_A = GPIO.input(pin)
            return
        else:
            return