#!/usr/bin/env python
from Maestor import maestor

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

def theY(robot):
    robot.setProperty("RSP", "position", 0.0)
    robot.setProperty("RSR", "position", -1.981)
    robot.setProperty("RSY", "position", -1.549)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 1.814)
    robot.setProperty("LSY", "position", 1.639)
    robot.setProperty("REP", "position", -0.219)
    robot.setProperty("LEP", "position", -0.322)
    robot.setProperty("RWP", "position", -0.084)
    robot.setProperty("LWP", "position", -0.006)
    robot.setProperty("RWY", "position", -1.419)
    robot.setProperty("LWY", "position", 1.57)

def theM(robot):
    robot.setProperty("RSP", "position", 0.008)
    robot.setProperty("RSR", "position", -1.999)
    robot.setProperty("RSY", "position", 1.576)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 1.937)
    robot.setProperty("LSY", "position", -1.458)
    robot.setProperty("REP", "position", -1.953)
    robot.setProperty("LEP", "position", -2.092)
    robot.setProperty("RWP", "position", 0.006)
    robot.setProperty("LWP", "position", 0.004)
    robot.setProperty("RWY", "position", -1.487)
    robot.setProperty("LWY", "position", 1.54)

def theC(robot):
    robot.setProperty("RSP", "position", -0.105)
    robot.setProperty("RSR", "position", -1.849)
    robot.setProperty("RSY", "position", -1.423)
    robot.setProperty("LSP", "position", -0.057)
    robot.setProperty("LSR", "position", 0.06)
    robot.setProperty("LSY", "position", 1.629)
    robot.setProperty("REP", "position", -1.185)
    robot.setProperty("LEP", "position", -0.824)
    robot.setProperty("RWP", "position", -0.08)
    robot.setProperty("LWP", "position", -0.079)
    robot.setProperty("RWY", "position", -1.467)
    robot.setProperty("LWY", "position", 1.57)

def theA(robot):
    robot.setProperty("RSP", "position", -0.101)
    robot.setProperty("RSR", "position", -1.796)
    robot.setProperty("RSY", "position", -1.376)
    robot.setProperty("LSP", "position", -0.056)
    robot.setProperty("LSR", "position", 1.884)
    robot.setProperty("LSY", "position", 1.571)
    robot.setProperty("REP", "position", -1.253)
    robot.setProperty("LEP", "position", -1.226)
    robot.setProperty("RWP", "position", -0.08)
    robot.setProperty("LWP", "position", -0.084)
    robot.setProperty("RWY", "position", -1.467)
    robot.setProperty("LWY", "position", 1.57)

def upperBodyHome(robot):
    robot.setProperty("RSP", "position", 0)
    robot.setProperty("RSR", "position", 0)
    robot.setProperty("RSY", "position", 0)
    robot.setProperty("LSP", "position", 0)
    robot.setProperty("LSR", "position", 0)
    robot.setProperty("LSY", "position", 0)
    robot.setProperty("REP", "position", 0)
    robot.setProperty("LEP", "position", 0)
    robot.setProperty("RWP", "position", 0)
    robot.setProperty("LWP", "position", 0)
    robot.setProperty("RWY", "position", 0)
    robot.setProperty("LWY", "position", 0)

def crouch(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def stand(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")


def doTheYMCA():
    robot = maestor()
    crouch(robot)
    for i in xrange(0,1):   #for(int i=0; i < 3; i ++) 
        theY(robot)
        waitForJoints(robot)
        theM(robot)
        waitForJoints(robot)
        theC(robot)
        waitForJoints(robot)
        theA(robot)
        waitForJoints(robot)
        upperBodyHome(robot)
        waitForJoints(robot)
    stand(robot)

if __name__ == '__main__':
    doTheYMCA() 
