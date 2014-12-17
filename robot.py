#!/usr/bin/env python

from Maestor import maestor


def theRobot():
    robot = maestor()
    bendDown(robot)
    doTheRobot(robot)
    standUp(robot)

def bendDown(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def doTheRobot(robot):
    robot.setProperty("NKY", "position", -.65)
#   robot.waitForJoint("NKY")
    robot.setProperties("RSY RSR", "position position", "1.57 -1.35")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    for i in range(0, 2):
        robot.setProperty("REP", "position", -1.7)
        robot.waitForJoint("REP")
        robot.setProperty("REP", "position", 0)
        robot.waitForJoint("REP")
    robot.setProperties("RSY RSR NKY", "position position position", "0 0 0")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
  #  robot.waitForJoint("NKY")


def standUp(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def theRobotRobot(robot):
    bendDown(robot)
    doTheRobot(robot)
    standUp(robot)


if __name__ == '__main__':
    theRobot()
