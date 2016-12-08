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

            # Turn off all LEDs that are in the list
            for i in range(6):
                GPIO.output(ledsix[i],False)
                time.sleep(0.5)

            # Declare the dice from the range of 1-6
            dice = random.randint(1,6)
            print '\n' + "Dice one rolling... " + str(dice)
            time.sleep(0.5)
            
            # Declare another dice from the range of 1-6 again
            diceTwo = random.randint(1,6)
            print "Dice two Rolling..." + str(diceTwo)
            roll = dice + diceTwo
            time.sleep(0.5)
            print '\n' + "First Roll: " + str(dice) + '\n' + "Second Roll: " + str(diceTwo) + '\n' + "Total: " + str(roll)

            # If both dice are the same number then it will be a double 
            if dice == diceTwo:
                print '\n' + "Congratulations you rolled a double"

            # If roll is equal to 7 or 11 then 
            if roll == 7 or roll == 11:
               print '\n' + "Congratulations you rolled a: " + str(roll)

            # In the range of roll
            for i in range(roll):
                GPIO.output(ledsix[i], True)
                time.sleep(0.5)
                GPIO.output(ledsix[i], False)
                                                   
except KeyboardInterrupt:
    GPIO.cleanup()
