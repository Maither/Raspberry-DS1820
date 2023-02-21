# Raspberry-pi-3-GPIO-and-DS1820
Code et procedure pour colecter des mesures de température avec une sonde DS1820 via le GPIO d'une Raspberry pi 3

Raspberry-pi-3 running Raspberry Pi OS

Activer one-wire :
https://fr.pinout.xyz/pinout/1_wire#

Exemple CLI :
sudo modprobe w1-gpio
sudo modprobe w1-therm

Exemple de cablage :
_______                                  ________________
|DS1820| - Rouge - VCC   -> 3.3v - 1 -   |raspberry pi 3|
                    |
             4.7Kohm Resistance
                    |
|DS1820| - jaune - DATA  -> GPIO4 - 4 -  |raspberry pi 3|
|DS1820| - noir - GROUND -> GROUND - 5 - |raspberry pi 3|
_______                                  ________________

Trouver l'ID du DS1820 dans le CLI :
ls /sys/bus/w1/devices/

pip install w1thermsensor


