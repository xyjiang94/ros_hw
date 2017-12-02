#!/usr/bin/env python

import rospy
import time
import actionlib
from hw.msg import DriveAction, DriveGoal, DriveResult, DriveFeedback
from geometry_msgs.msg import Twist

def drive(goal):
    speed = 0.1
    rate = 1
    count = 0

    turn_time = (goal.angle_to_turn) / speed
    start_time = time.time()
    end_time = start_time + turn_time
    print turn_time
    print start_time
    print end_time

    twist = Twist()
    twist.angular.z = speed
    pub.publish(twist)

    while time.time() < end_time:
        feedback = DriveFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.time_remaining = rospy.Duration.from_sec(end_time -time.time())
        feedback.angle_have_turned = speed * (time.time() - start_time)
        count += 1
        server.publish_feedback(feedback)

    pub.publish(Twist())

    result = DriveResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = count
    server.set_succeeded(result)
    return


rospy.init_node('drive_action_server')
server = actionlib.SimpleActionServer('drive', DriveAction, drive, False)

pub = rospy.Publisher("/cmd_vel_mux/input/navi", Twist, queue_size=1)

server.start()
rospy.spin()
