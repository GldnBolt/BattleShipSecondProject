import pyfirmata
from pyfirmata import Arduino, util
import time


arduino = Arduino('COM4')

pinLED1 = arduino.get_pin('d:2:o')
pinLED2 = arduino.get_pin('d:3:o')
pinLED3 = arduino.get_pin('d:4:o')
pinLED4 = arduino.get_pin('d:5:o')



arduino.exit()                                  