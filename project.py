from gpiozero import DigitalOutputDevice
from time import sleep

print("Hello world")
ventilator=DigitalOutputDevice(21)
while(True):
    ventilator.toggle()
    sleep(5)
    

