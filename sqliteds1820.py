import sqlite3
import glob
from datetime import datetime
import time

def main():
    while True:
        temperature = get_temperature()
        current_time = get_time()
        print(current_time, temperature)
        if temperature:
            db_save_temp(current_time + temperature)
        time.sleep(600)
	
def get_time():
    now = datetime.now()
    return [now.year, now.month, now.day, now.hour, now.minute, now.second]
	
def get_temperature(route_capteurs=glob.glob("/sys/bus/w1/devices/28*/w1_slave")):
    if len(route_capteurs) > 0:
        with open(route_capteurs[0]) as f:
            temperature = [float(((f.read()).split("\n")[1]).split(" ")[9][2:]) / 1000]
            return temperature
    else:
        return False
		
def sqlite(db_str="temperature.db"):
    db = sqlite3.connect(db_str)
    return db.cursor()

cur = sqlite()
#cur.execute("CREATE TABLE temperature(year, month, day, hour, minute, second, celcius)")

def db_save_temp(temperature=[2023, 3, 2, 15, 35, 12, 19], cur=cur):
    cur.execute("INSERT INTO temperature VALUES (?, ?, ?, ?, ?, ?, ?)", temperature)
    db.commit()

if __name__ == "__main__":
    main()
