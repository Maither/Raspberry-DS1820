# Raspberry-pi-3-GPIO
Code et procedure pour colecter des mesures de température avec une sonde DS1820 via le GPIO d'une Raspberry pi 3

Raspberry-pi-3 running Raspberry Pi OS


Exemple de cablage :
_______                                  ________________
|DS1820| - Rouge - VCC   -> 3.3v - 1 -   |raspberry pi 3|
                    |
             4.7Kohm Resistance
                    |
|DS1820| - jaune - DATA  -> GPIO4 - 4 -  |raspberry pi 3|
|DS1820| - noir - GROUND -> GROUND - 5 - |raspberry pi 3|
_______                                  ________________
