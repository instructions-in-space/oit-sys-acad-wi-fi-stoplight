#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# Set it to use Broadcom (GPIO) numbers
GPIO.setmode(GPIO.BCM)

# Instantiate the LED object
GPIO.setup(23, GPIO.OUT)

# The above command errors out, and I found out why:
# "RPi.GPIO, wiringPI, and pigpio do not work on the Pi5 which has new hardware for the GPIO."
# Source:  https://forums.raspberrypi.com/viewtopic.php?t=361218

# Set modes
#GPIO.output(23, GPIO.HIGH)
#GPIO.output(23, GPIO.LOW)

#for i in range(5):
#    GPIO.output(23, GPIO.HIGH)
#    time.sleep(0.5)
#    GPIO.output(23, GPIO.LOW)
#    time.sleep(0.5)

