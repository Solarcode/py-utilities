from psutil import sensors_battery
from configparser import ConfigParser
from time import sleep

file = 'config.ini'
config = ConfigParser()
config.read(file)

#def get_percent():
	#return sensors_battery().percent

print(config.sections())
#sleep(config['settings']['frequency'])