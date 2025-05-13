# Klimaatcontroller
In dit programma meten we omgevingswaarden met behulp van een BME680. Deze waarden worden dan via een bedraad netwerk doorgestuurd naar een ander apparaat, een [monitor](https://github.com/DeVestenMechatronica/raspberrypi-iot-dashboard). Ook is er een ventilator aangesloten die aangestuurd wordt op basis van de temperatuur.

#### Hardware: 
- Raspberry Pi 4B+ 
- Edgeberry Baseboard
- Sense And Drive Cartridge
- BME680 sensor
- 

#### Libraries:
- influxdb3-python 
- BME680


## setup
hier kan je uitleggen hoe je het project installeert

We maken een virtual environment.


Voer dit in bij de terminal van het toestel.
```
python3 -m venv venv
source venv/bin/activate
```

Om influxdb client te gebruiken voer je dit in in de commandline:
```
pip install influxdb3-python
```
#### referenties:
https://docs.influxdata.com/influxdb3/cloud-dedicated/reference/client-libraries/v3/python/#installation 

### Opstart
Om te zorgen dat ons Python programma opstart telkens als de Raspberry Pi opstart gebruiken we `systemd`. We gebruiken het script `klimaatcontroller.service` hiervoor, dat het script `start.sh` uitvoert.
```
sudo cp klimaatcontroller.service /etc/systemd/system/
sudo systemctl enable klimaatcontroller.service
```
Tijdens de ontwikkeling van de klimaatcontroller software schakelen we deze beter even uit.
```
sudo systemctl disable klimaatcontroller.service
```

- De [Edgeberry](https://github.com/Edgeberry) repository
- De [Edgeberry Sense'n'Drive Cartridge](https://github.com/Edgeberry/Edgeberry_SenseAndDrive_Cartridge)
- De [Freya](https://github.com/Freya-Vivariums/Freya-sensor) sensor
- De [cmds](https://learn.pimoroni.com/article/getting-started-with-bme680-breakout) voor de sensor

