#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_spiral():
    rospy.init_node('spiral_leader')

    pub = rospy.Publisher('/B01009366Leader/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)
    vel = Twist()

    speed = 1.0
    radius = 0.5
    r_inc = 0.01

    while not rospy.is_shutdown():
        vel.linear.x = speed
        vel.angular.z = speed / radius

        pub.publish(vel)

        radius += r_inc
        rate.sleep()

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
