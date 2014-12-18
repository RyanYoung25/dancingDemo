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

#Globals :( 
#Used for checking if a specific dance is happening
chickenDance = False
robotDance = False
discoDance = False
egyptianDance = False
ymcaDance = False
danceStop = False
#Used to know if we need to stop
listening = True



class songListener(threading.Thread):
    """This class listens for songs in a background thread using the Dejavu audio 
    fingerprinter. When it hears a song it sets global flags"""

    global chickenDance
    global robotDance
    global discoDance
    global egyptianDance
    global ymcaDance
    global danceStop

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
        global danceStop
        #do the listening
        while(self.running):

            response = self.djv.recognize(MicrophoneRecognizer, seconds=5)
            if(response == None):
                continue

            if(response["confidence"] > 30 and response["song_name"] == "chickenDance") and (not (robotDance or discoDance or egyptianDance or ymcaDance)):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                chickenDance = True
                danceStop = False
                

            elif(response["confidence"] > 30 and response["song_name"] == "technologic") and (not (chickenDance or discoDance or egyptianDance or ymcaDance)):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                robotDance = True
                danceStop = False

            elif(response["confidence"] > 30 and response["song_name"] == "stayingAlive") and (not (chickenDance or robotDance or egyptianDance or ymcaDance)):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                discoDance = True
                danceStop = False

            elif(response["confidence"] > 30 and response["song_name"] == "walkLikeAnEgyptian") and (not (chickenDance or robotDance or discoDance or ymcaDance)):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                egyptianDance = True
                danceStop = False

            elif(response["confidence"] > 30 and response["song_name"] == "YMCA") and (not (chickenDance or robotDance or discoDance or egyptianDance)):
                print "Found " + response["song_name"]
                print "Confidence: " + str(response["confidence"]) + " units"
                ymcaDance = True
                danceStop = False

            else:
                chickenDance = False
                robotDance = False
                discoDance = False
                egyptianDance = False
                ymcaDance = False

    def stop(self):
        self.running = False


#Function to step through the dances list. 
def stepper(index, list, theRobot):

    #Call the current function we are on from the list
    list[index](theRobot)

        
#Make the robot stand up
def stand(theRobot):
    theRobot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    theRobot.waitForJoint("RFZ")
    theRobot.waitForJoint("LFZ")

#Make the robot crouch
def crouch(theRobot):
    theRobot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    theRobot.waitForJoint("RFZ")
    theRobot.waitForJoint("LFZ")

#Zero the upper body
def upperHome(theRobot):
    theRobot.setProperty("RSP", "position", 0)
    theRobot.setProperty("RSR", "position", 0)
    theRobot.setProperty("RSY", "position", 0)
    theRobot.setProperty("LSP", "position", 0)
    theRobot.setProperty("LSR", "position", 0)
    theRobot.setProperty("LSY", "position", 0)
    theRobot.setProperty("REP", "position", 0)
    theRobot.setProperty("LEP", "position", 0)
    theRobot.setProperty("RWP", "position", 0)
    theRobot.setProperty("LWP", "position", 0)
    theRobot.setProperty("RWY", "position", 0)
    theRobot.setProperty("LWY", "position", 0)
    theRobot.setProperty("NKY", "position", 0)
    theRobot.setProperty("WST", "position", 0)

#block for all of the joints to get done moving
def waitForJoints(robot):
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("LSP")
    robot.waitForJoint("LSR")
    robot.waitForJoint("LSY")
    robot.waitForJoint("REP")
    robot.waitForJoint("LEP")
    robot.waitForJoint("RWP")
    robot.waitForJoint("LWP")
    robot.waitForJoint("RWY")
    robot.waitForJoint("LWY")
    robot.waitForJoint("WST")


#Handle sig_int so that we can stop properly without needing ctrl-\
def signal_handler(signal, frame):
    global listening
    print('Dancing and listening demo ending')
    listening = False
    

def main():
    global listening
    global danceStop

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

    theRobot = maestor()
    listening = True

    #Used for knowing where in a dance we are
    ##Used for knowing which part of the dance to do
    index = 0
    danceList = []

    #crouch
    crouch(theRobot)

    #loop in main thread and dance if we should be dancing.
    while(listening):

        if danceStop:
            continue

        if chickenDance:
            #Get the chicken dance list
            danceList = ChickenDance.getDanceList()
        elif robotDance:
            #Get the robot dance list
            danceList = robot.getDanceList()
        elif discoDance:
            #Get the disco dance list
            danceList = disco.getDanceList()
        elif egyptianDance:
            #Get the egyptian dance list
            danceList = walkLikeAnEgyptian.getDanceList()
        elif ymcaDance:
            #Get the ymca dance list
            danceList = YMCA.getDanceList()
        else:
            #In here we need to stop/do nothing.
            #Set the robot back to home
            upperHome(theRobot)
            waitForJoints(theRobot)
            #Reset the index
            index = 0;
            #Reset dance stop
            danceStop = True

            print "It is now save to end the demo with ctrl-c"
            continue

        #Do a step of the dance
        stepper(index, danceList, theRobot)

        if( index < len(danceList) - 1):
            index += 1
        else:
            index = 0


    #Stand up
    stand(theRobot)

    listener.stop()

        

if __name__ == '__main__':
    main()

