#!/usr/bin/env python


import rospy
from hw.srv import npl, nplResponse

def get_angle(request):
    cmd = request.command.split()[1]
    return nplResponse(float(cmd))

rospy.init_node('npl_server')
service = rospy.Service('npl', npl, get_angle)
rospy.spin()
