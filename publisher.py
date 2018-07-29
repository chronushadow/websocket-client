#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime

def publish():
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('hello', String, queue_size=10)
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        msg = datetime.now().isoformat()
        rospy.loginfo("Publish: %s", msg)
        pub.publish(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
