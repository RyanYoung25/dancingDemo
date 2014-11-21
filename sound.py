#! /usr/bin/env python
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer
import sys
import signal
import ChickenDance
import robot
import YMCA
import walkLikeAnEgyptian
import disco

config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "hubo", 
         "db": "dejavu",
     }
 }

def signal_handler(signal, frame):
    print('Dancing and listening demo ending')
    sys.exit(0)

def main():


    signal.signal(signal.SIGINT, signal_handler)
    djv = Dejavu(config) 
    flag = True
    while(flag):

        response = djv.recognize(MicrophoneRecognizer, seconds=5)
        if(response == None):
            continue
            
        print "Found " + response["song_name"]
        print "Confidence: " + str(response["confidence"]) + " units"


        if(response["confidence"] > 30 and response["song_name"] == "chickenDance"):
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"
            ChickenDance.chickenDance()
            

        if(response["confidence"] > 30 and response["song_name"] == "technologic"):
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"
            robot.theRobot()

        if(response["confidence"] > 30 and response["song_name"] == "stayingAlive"):
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"
            disco.stayAlive()

        if(response["confidence"] > 30 and response["song_name"] == "walkLikeAnEgyptian"):
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"
            walkLikeAnEgyptian.walkLikeAnEgyptian()

        if(response["confidence"] > 30 and response["song_name"] == "YMCA"):
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"
            YMCA.doTheYMCA()


            


        

if __name__ == '__main__':
    main()

