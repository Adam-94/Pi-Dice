#!/usr/bin/python

# Importing appropraite libraries 
import RPi.GPIO as GPIO
import time
import random

# Using GPIO numbers instead of pin numbers
GPIO.setmode (GPIO.BCM)

# The list of LED GPIO numbers, I'm going from 1-6 then back around 1-6 so that i can include two dice
ledsix = [4,17,22,10,9,11,4,17,22,10,9,11]

# In range of 6 setting LED's as outputs, then setting outputs to false
for i in range(6):
    GPIO.setup(ledsix[i], GPIO.OUT)
    GPIO.output(ledsix[i], False)
    
# Setup input as switch
GPIO.setup (7, GPIO.IN)
random.seed()
print("Press the switch to roll")
print "To exit press CTRL-C"

# I am using try to catch when the user presses CTRL-C
# and to run GPIO cleanup fuction, to stop any error messages
try:
    # If the switch is pressed the code below will start
    while True:
        if GPIO.input(7)==1:

            # Turn off LED's in the range of 6
            for i in range(6):
                GPIO.output(ledsix[i],False)

            # Declare first dice from the range of 1-6
            dice = random.randint(1,6)
            time.sleep(0.5)
            print '\n' + "Dice one rolling... " + str(dice)
            
            # Declare second dice with the same range of 1-6
            diceTwo = random.randint(1,6)
            time.sleep(0.5)
            print "Dice two Rolling..." + str(diceTwo)

            # Adding Dice and diceTwo together to get the totalRoll
            totalRoll = dice + diceTwo
            time.sleep(0.5)
            print '\n' + "First Roll: " + str(dice) + '\n' + "Second Roll: " + str(diceTwo) + '\n' + "Total: " + str(totalRoll)

            # If both dice are the same number then it will be a double 
            if dice == diceTwo:
                print '\n' + "Congratulations you rolled a double of " + str(dice) + " making: " + str(totalRoll)

            # If roll is equal to 7 or 11 then 
            if totalRoll == 7 or totalRoll == 11:
               print '\n' + "Congratulations you rolled a: " + str(totalRoll)
               
            # The for is in range of the totalRoll so, it will increment i until it reaches totalRoll
            for i in range(totalRoll):
                time.sleep(0.5)
                GPIO.output(ledsix[i], True)
                time.sleep(0.5)
                GPIO.output(ledsix[i], False)
                                                   
except KeyboardInterrupt:
    GPIO.cleanup()
