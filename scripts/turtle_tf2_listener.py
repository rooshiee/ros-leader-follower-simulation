#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf2_ros
import geometry_msgs.msg
from math import sqrt, atan2

# IMPORT MESSAGE
from com760cw1_B01009366.msg import B01009366LeaderInstruction

# MESSAGE CALLBACK
def instruction_callback(data):
    rospy.loginfo("Instruction received: %s | Velocity: %.2f | Distance: %.2f",
                  data.instruction, data.velocity, data.distance)

if __name__ == '__main__':
    rospy.init_node('turtle_tf2_listener')

    from_turtle = rospy.get_param('~from')
    to_turtle = rospy.get_param('~to')

    # SUBSCRIBE TO MESSAGE
    rospy.Subscriber('/leader_instruction', B01009366LeaderInstruction, instruction_callback)

    pub = rospy.Publisher('/%s/cmd_vel' % from_turtle,
                          geometry_msgs.msg.Twist,
                          queue_size=1)

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(from_turtle, to_turtle, rospy.Time())
        except:
            rate.sleep()
            continue

        dx = trans.transform.translation.x
        dy = trans.transform.translation.y

        # Formation offsets
        if from_turtle == "B01009366FollowerA":
            offset_x = 1.0
            offset_y = 1.5
        elif from_turtle == "B01009366FollowerB":
            offset_x = 1.0
            offset_y = -1.5
        else:
            offset_x = 0.0
            offset_y = 0.0

        target_x = dx - offset_x
        target_y = dy + offset_y

        angle = atan2(target_y, target_x)
        distance = sqrt(target_x**2 + target_y**2)

        msg = geometry_msgs.msg.Twist()
        msg.angular.z = 4.0 * angle

        if abs(angle) < 0.5:
            msg.linear.x = 0.8 * distance
        else:
            msg.linear.x = 0.0

        pub.publish(msg)
        rate.sleep()
