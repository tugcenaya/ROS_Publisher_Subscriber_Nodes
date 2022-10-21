#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chat', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
	
        
	a = 31790007
	a = int(a)
	x = a %10 + 1
	x = int(x)
        for i in range (1,x):
	    hello_str = "tugceayan %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
        break
       

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
