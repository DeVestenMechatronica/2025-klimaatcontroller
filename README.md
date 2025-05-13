# IoT Klimaatcontroller
In dit programma meten we omgevingswaarden met behulp van een BME680. Deze waarden worden dan via een bedraad netwerk doorgestuurd naar een ander apparaat, een [monitor](https://github.com/DeVestenMechatronica/raspberrypi-iot-dashboard). Ook is er een ventilator aangesloten die aangestuurd wordt op basis van de temperatuur.

#### Hardware: 
- Raspberry Pi 3B+/4B/5B 
- [Edgeberry Baseboard](https://github.com/Edgeberry/Edgeberry-Baseboard)
- [Edgeberry Sense'n'Drive Hardware Cartridge](https://github.com/Edgeberry/Edgeberry-HWCartridge-SenseAndDrive)
- [BME680](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf) temperatuur/luchtvochtigheid/luchtdruk/luchtkwaliteit sensor
- 

#### Python Libraries:
- [influxdb3-python]() 
- [BME680](https://pypi.org/project/bme680/)


## Setup
Wat je moet doen voordat je het programma opstart.

### Virtual Environment
We maken een `virtual environment` met dit commando:
```
python3 -m venv venv
```
Om de `virtual environment` te starten voer je dit commando uit:
```
source venv/bin/activate
```
### Installatie libraries
Om de `Influxdb` client library te installeren voer je dit commando uit:
```
pip install influxdb3-python
```
Installeer de `BME680` library
```
pip install bme680
```
#### Referenties:
https://docs.influxdata.com/influxdb3/cloud-dedicated/reference/client-libraries/v3/python/#installation 

## Uitvoeren Python programma
We hebben de `virutal environment` opgestart, en alle `libraries` geinstalleerd. Nu kunnen we het programma uitvoeren:
```
python project.py
```

### Automatische opstart
Om te zorgen dat ons Python programma opstart telkens als de Raspberry Pi opstart gebruiken we `systemd`. We gebruiken het script `klimaatcontroller.service` hiervoor, dat het script `start.sh` uitvoert.
```
sudo cp klimaatcontroller.service /etc/systemd/system/
sudo systemctl enable klimaatcontroller.service
```
Tijdens de ontwikkeling van de klimaatcontroller software schakelen we deze beter even uit.
```
sudo systemctl disable klimaatcontroller.service
```
>[!TIP]
>Het `startup.sh` script doet niet meer dan de `virtual environment` starten, en ons Python project uitvoeren.

#### Referenties:
- De [Edgeberry](https://github.com/Edgeberry) repository
- De [Edgeberry Sense'n'Drive Cartridge](https://github.com/Edgeberry/Edgeberry_SenseAndDrive_Cartridge)
- De [Freya](https://github.com/Freya-Vivariums/Freya-sensor) sensor
- De [cmds](https://learn.pimoroni.com/article/getting-started-with-bme680-breakout) voor de sensor

## Licensie
**Copyright© 2025 Mechatronica Campus De Vesten**. Dit project is gedeeld onder de [MIT-licentie](LICENSE.txt).

