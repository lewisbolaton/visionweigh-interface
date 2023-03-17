#!/usr/bin/python3

from gpiozero import LED, Button
from signal import pause

global device_busy = False

def main():
	start_button = Button()
	power_button = Button()
	
	process_indicator = LED()
	power_indicator = LED()
		
	
	try:
		start_button.when_pressed = process_image
		power_button.when_pressed = turn_off
	
		pause()
		
	finally:
		pass

def process_image():
	if not device_busy:
		process_indicator.on()
		# Inference code here
		process_indicator.off()
	else:
		process_indicator.blink()

if __name__ == "__main__":
	main()
