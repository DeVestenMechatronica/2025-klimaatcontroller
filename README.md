# Klimaatcontroller
Met Edgeberry

## setup
hier kan je uitleggen hoe je het project installeert


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

