#!/usr/bin/python

# Importing appropraite libraries 
import RPi.GPIO as GPIO
import time
import random

# Using GPIO numbers instead of pin numbers
GPIO.setmode (GPIO.BCM)

# The list of LED GPIO numbers, I'm going from 1-6 then back around 1-6 so that i can include two dice
ledsix = [4,17,22,10,9,11,4,17,22,10,9,11]

# Setting LED's as outputs, then setting outputs to false
for i in range(6):
    GPIO.setup(ledsix[i], GPIO.OUT)
    GPIO.output(ledsix[i], False)
    
# Setup input as switch
GPIO.setup (7, GPIO.IN)
random.seed()
print("Press the switch to roll two dice")
print "To exit press CTRL-C"

# I am using try to catch when the user presses CTRL-C
# and to run GPIO cleanup fuction, to stop any error messages
try:
    while True:
        if GPIO.input(7)==1:

            # Turn off all 6 LEDs that are in the list
            for i in range(6):
                GPIO.output(ledsix[i],False)
                time.sleep(0.5)
                diceNum = 0
                diceNumTwo = 0

                # Declare the dice from the range of 2-12
                dice = random.randint(1,6)
                print "Dice one rolling... " + str(dice)
                time.sleep(0.5)
            for i in range(6):
                diceTwo = random.randint(1,6)
                print "Dice two Rolling..." + str(diceTwo)
                time.sleep(0.5)
            if dice + diceTwo == dice + diceTwo:
                roll = dice + diceTwo
                print "Final Roll: " + str(roll)
            for i in range(roll):
                GPIO.output(ledsix[i], True)
                time.sleep(0.3)
                GPIO.output(ledsix[i], False)
                                                   
except KeyboardInterrupt:
    GPIO.cleanup()
