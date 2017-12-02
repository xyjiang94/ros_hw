#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sys

rospy.init_node('console')
pub = rospy.Publisher('/demo/command', String)
rate = rospy.Rate(2)


while not rospy.is_shutdown():
    msg = raw_input("input your command\n")
    pub.publish(msg)

    rate.sleep()
