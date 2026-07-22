#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_straight():
    rospy.init_node('straight_leader')

    pub = rospy.Publisher('/B01009366Leader/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    vel = Twist()
    vel.linear.x = 2.0
    vel.angular.z = 0.0

    while not rospy.is_shutdown():
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_straight()
    except rospy.ROSInterruptException:
        pass
