from mcpi.minecraft import Minecraft
from twython import Twython
from threading import Thread
import threading
import math
import time
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

mc = Minecraft.create()

destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ)

block = 89
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block set")

time.sleep(3)
var = 0

def tim():
    timer = 0
    while var != 1:
        time.sleep(.25)
        global timer
        timer += .25
    

def goldstone():    
    var = 0
    while var != 1:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        if distance > 100:
            mc.postToChat("Freezing")
        elif distance > 50:
            mc.postToChat("Cold")
        elif distance > 25:
            mc.postToChat("Warm")
        elif distance > 12:
            mc.postToChat("Boiling")
        elif distance > 6:
            mc.postToChat("On fire!")
        elif distance > 1:
            mc.postToChat("Found it")
            mc.setBlock(destX, destY, destZ, 0)
            var = 1
            
               
    message = 'It took me ' + str(timer) + ' seconds to win the J&J scavenger hunt challenge!'
    twitter.update_status(status=message)
    mc.postToChat('Score has been tweeted!')

if __name__== '__main__':
    Thread(target = tim).start()
    Thread(target = goldstone).start()


