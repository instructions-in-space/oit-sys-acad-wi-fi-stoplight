#!/usr/bin/python3

from gpiozero import LED
from time import sleep

# Instantiate the LED object
led = LED(23)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

