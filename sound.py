#! /usr/bin/env python
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer
from Maestor import maestor
import sys
import signal
import ChickenDance
import robot
import YMCA
import walkLikeAnEgyptian
import disco
import threading
import time


chickenDance = False
robotDance = False
discoDance = False
egyptianDance = False
ymcaDance = False
listening = True

class songListener(threading.Thread):
    """This class listens for songs in a background thread using the Dejavu audio 
    fingerprinter. When it hears a song"""

    global chickenDance
    global robotDance
    global discoDance
    global egyptianDance
    global ymcaDance

    def __init__(self, config):
        threading.Thread.__init__(self)
        #Initialize the dejavu listener
        self.djv = Dejavu(config) 
        self.running = True

    def run(self):
        global chickenDance
        global robotDance
        global discoDance
        global egyptianDance
        global ymcaDance
        #do the listening
        while(self.running):

            response = self.djv.recognize(MicrophoneRecognizer, seconds=5)
            if(response == None):
                continue
                
            print "Found " + response["song_name"]
            print "Confidence: " + str(response["confidence"]) + " units"

            if(response["confidence"] > 30 and response["song_name"] == "chickenDance"):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                chickenDance = True
                print "We should still be listening"
                

            elif(response["confidence"] > 30 and response["song_name"] == "technologic"):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                robotDance = True

            elif(response["confidence"] > 30 and response["song_name"] == "stayingAlive"):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                discoDance = True

            elif(response["confidence"] > 30 and response["song_name"] == "walkLikeAnEgyptian"):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                egyptianDance = True

            elif(response["confidence"] > 30 and response["song_name"] == "YMCA"):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                ymcaDance = True

            else:
                chickenDance = False
                robotDance = False
                discoDance = False
                egyptianDance = False
                ymcaDance = False

    def stop(self):
        self.running = False


        


def signal_handler(signal, frame):
    global listening
    print('Dancing and listening demo ending')
    listening = False
    

def main():
    global listening

    signal.signal(signal.SIGINT, signal_handler)

    config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "hubo", 
         "db": "dejavu",
        }
    }

    listener = songListener(config)
    listener.start()

    robot = maestor()
    listening = True


    #loop in main thread and dance if we should be dancing.
    while(listening):
        if chickenDance:
            ChickenDance.chickenDanceRobot(robot)
        elif robotDance:
            robot.theRobotRobot(robot)
        elif discoDance:
            disco.stayAliveRobot(robot)
        elif egyptianDance:
            walkLikeAnEgyptian.walkLikeAnEgyptianRobot(robot)
        elif ymcaDance:
            YMCA.doTheYMCARobot(robot)  
        else:
            #In here we need to figure out how to stop/do nothing.
            pass         

    listener.stop()

        

if __name__ == '__main__':
    main()

