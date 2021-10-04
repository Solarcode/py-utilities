from psutil import sensors_battery
from configparser import ConfigParser
from time import sleep
from tkinter import *
from tkinter import messagebox
import winsound
from distutils.util import strtobool

# Read config file

file = 'config.ini'
config = ConfigParser()
config.read(file)

# Set variables from config file

frequency = int(config.get('settings', 'frequency'))
threshold_upper = int(config.get('settings', 'threshold_upper'))
threshold_lower = int(config.get('settings', 'threshold_lower'))
message_box = strtobool(config.get('settings', 'message_box'))
sound = strtobool(config.get('settings', 'sound'))
sound_path = str(config.get('settings', 'sound_path'))
print = strtobool(config.get('settings', 'print'))

# Functions

def get_percent():
	return sensors_battery().percent

def show_message(message):
	window = Tk()
	window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
	window.withdraw()
	
	messagebox.showwarning('Battery Level Warning', message)

	window.deiconify()
	window.destroy()
	window.quit()

def play_sound():
	winsound.PlaySound(sound_path, winsound.SND_FILENAME)

def notify(battery_level):
	if (battery_level):
		message = 'The battery level has reached ' + str(threshold_upper) + '%, please stop charging your computer.'
	elif (not battery_level):
		message = 'The battery level has fallen below ' + str(threshold_lower) + '%, please charge your computer.'
	if (print):
		print(message)
	if (sound):
		play_sound()
	if (message_box):
		show_message(message)

# Main block

toggle = False
charging = sensors_battery().power_plugged
battery = get_percent()
while True:
	if charging != sensors_battery().power_plugged or battery != get_percent():
		toggle = False
	while not toggle:
		battery = get_percent()
		charging = sensors_battery().power_plugged
		if (battery >= threshold_upper and charging == True):
			notify(True)
		elif (battery <= threshold_lower and charging == False):
			notify(False)
		sleep(frequency / 2)
		toggle = True
	sleep(frequency / 2)