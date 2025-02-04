#from gpiozero import DigitalOutputDevice
import bme680
import time
from time import sleep

# Create a sensor object
sensor = bme680.BME680()

print("Hello world")
#ventilator=DigitalOutputDevice(21)
#while(False): #timed out
    #ventilator.toggle()
    #sleep(5)
    



# Function to read and print sensor values
def read_bme680():
    # Wait for new data to be available
    if sensor.get_sensor_data():
        print("Temperature: {:.2f} C".format(sensor.temperature))
        print("Humidity: {:.2f} %".format(sensor.humidity))
        print("Pressure: {:.2f} hPa".format(sensor.pressure))
        print("Gas resistance: {:.2f} Ohms".format(sensor.gas_resistance))
    else:
        print("Failed to read sensor data.")

# Continuously read and print data from the sensor
while True:
    read_bme680()
    time.sleep(1)  # Wait 1 second before reading again

