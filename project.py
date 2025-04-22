from gpiozero import DigitalOutputDevice
import bme680
import time
from time import sleep

TEMPERATURE_HIGH = 23.3
TEMPERATURE_LOW = 22.5 

# Create a sensor object
sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

ventilator=DigitalOutputDevice(12)
    



# Function to read and print sensor values
while True:
   # ventilator.toggle()
    if sensor.get_sensor_data():
        output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)

        if sensor.data.heat_stable:
            print("{0},{1} Ohms".format(output, sensor.data.gas_resistance))

        else:
            print(output)
    if float(sensor.data.temperature) >= TEMPERATURE_HIGH:
        ventilator.on()
    elif float(sensor.data.temperature) <= TEMPERATURE_LOW:
        ventilator.off()
    sleep(5)

