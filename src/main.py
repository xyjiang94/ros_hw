#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Float32

from hw.srv import npl
import sys

from hw.msg import DriveAction, DriveGoal, DriveResult
import actionlib


def cmd_callback(msg):
    print msg.data
    angle = npl_service(msg.data).angle
    print angle

    goal = DriveGoal()
    goal.angle_to_turn = angle

    client.send_goal(goal, feedback_cb = action_callback )
    client.wait_for_result()

    print('[Result] Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))

def action_callback(feedback):
    print('[Feedback] Time elapsed: %f'%(feedback.time_elapsed.to_sec()))
    print('[Feedback] Time remaining: %f'%(feedback.time_remaining.to_sec()))
    print('[Feedback] Angle have turned: %f'%(feedback.angle_have_turned))

rospy.init_node('main')

sub = rospy.Subscriber('/demo/command', String, cmd_callback)

rospy.wait_for_service('npl')
npl_service = rospy.ServiceProxy('npl', npl)

client = actionlib.SimpleActionClient('drive', DriveAction)
client.wait_for_server()

rospy.spin()
