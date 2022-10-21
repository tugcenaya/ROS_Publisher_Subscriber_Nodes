#!/usr/bin/env python

PKG = 'beginner_tutorials' 
import roslib; roslib.load_manifest(PKG)

import rospy
from std_msgs.msg import String
import numpy as np

def callback(data):
    rospy.loginfo("I heard %s",data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chat", String, callback)

    rospy.spin()
   
   
        
if __name__ == '__main__':
    listener()
