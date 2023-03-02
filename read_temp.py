import time
from datetime import datetime
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

# Set resolution to 0.5°C
sensor.set_resolution(9)

while True:
    # Read temperature
    temperature = sensor.get_temperature()

    # Get current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Add temperature and date/time to dict
    temperatures = {'temperature': temperature, 'datetime': dt_string}
    print(temperatures)

    # Wait for 10 minutes
    time.sleep(600)

#Ce code utilise la bibliothèque w1thermsensor pour lire la température à partir du DS18B20, 
#et la bibliothèque standard datetime pour enregistrer la date et l'heure de chaque lecture de température. 
#La résolution est définie à 0.5°C avec la méthode set_resolution().
#Les valeurs de température et de date/heure sont stockées dans une liste appelée temperatures.
