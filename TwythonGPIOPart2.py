#!usr/bin/python
import sys
import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

#Set GPIO numbers up
GPIO.setmode (GPIO.BCM)

#List of leds
leds = [4,17,22,10,9,11,8]

for i in range(7):
    GPIO.setup(leds[i], GPIO.OUT)
    GPIO.output(leds[i], False)
    
#Search terms
TERM = [sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]]

CONSUMER_KEY = 'aauyXedurtUMHary94aelk5pL'
CONSUMER_SECRET = 'aJIx7s4GfTeOvzFbSY7BlU4K9yXbmgYbeG0OpjMS5Wqp3eLTGk'
ACCESS_KEY = '837236886850662400-wbjsZBfjMMZ8nYk9ppV7WVJe8yCVKMm'
ACCESS_SECRET = 'ltTZCTLInJVbPxOcuDOGYbl2mA5EVFWwKxeF4f9f3iB8z'

#Setup callback from Twython Steamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            tweet_stream = data['text'].encode('utf-8')
            
            for i in range(7):
                if TERM[i] in tweet_stream:
                    GPIO.output(leds[i], True)
                    time.sleep(0.8)
                    GPIO.output(leds[i], False)
                    print tweet_stream
#Create stream
try:
    stream = BlinkyStreamer(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    stream.statuses.filter(track=TERM)
    stream.on_success()

except KeyboardInterrupt:
    GPIO.cleanup()
