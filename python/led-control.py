#!/usr/bin/python3

from gpiozero import LED
from time import sleep

# Instantiate the LED object
led = LED(23)

print("Welcome to \"led-control.py\"! (Press ctrl-c to exit.)")

while True:
    control_file = open("../state/current-state.txt", "r")
    current_state = control_file.readlines()
    current_state_as_string = ''.join(current_state)
    cleaned_up_current_state = current_state_as_string.replace("\n", "")
#    print(cleaned_up_current_state)
    if cleaned_up_current_state == "on":
        #print("It is on.")
        led.on()
    elif cleaned_up_current_state == "off":
        #print("It is off.")
        led.off()


#while True:
#    led.on()
#    sleep(1)
#    led.off()
#    sleep(1)

