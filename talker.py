#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) 
    i=0
    while not rospy.is_shutdown():
        student_str = "1711516 %d" % i
        i+=1
        rospy.loginfo(student_str)
        pub.publish(student_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
