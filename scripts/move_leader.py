#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute
import random

from com760cw1_B01009366.msg import B01009366LeaderInstruction

pose = None

def pose_callback(data):
    global pose
    pose = data

def move_leader():
    rospy.init_node('move_leader')

    pub = rospy.Publisher('/B01009366Leader/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/B01009366Leader/pose', Pose, pose_callback)

    # ✅ Custom message publisher
    msg_pub = rospy.Publisher('/leader_instruction', B01009366LeaderInstruction, queue_size=10)

    rate = rospy.Rate(10)
    vel = Twist()
    vel.linear.x = 0.8

    last_turn = rospy.Time.now()

    # ✅ Give ROS time to connect publishers/subscribers
    rospy.sleep(1)

    while not rospy.is_shutdown():

        # ✅ Create and publish instruction message
        instruction_msg = B01009366LeaderInstruction()
        instruction_msg.instruction = "Maintain Formation"
        instruction_msg.velocity = vel.linear.x
        instruction_msg.distance = 1.0

        msg_pub.publish(instruction_msg)

        # ✅ Log for proof 
        rospy.loginfo("Publishing Instruction: %s | vel=%.2f | dist=%.2f",
                      instruction_msg.instruction,
                      instruction_msg.velocity,
                      instruction_msg.distance)

        # Wall reset
        if pose and (pose.x <= 0.5 or pose.x >= 10.5 or pose.y <= 0.5 or pose.y >= 10.5):
            rospy.loginfo("Wall hit. Resetting.")
            rospy.wait_for_service('/B01009366Leader/teleport_absolute')
            teleport = rospy.ServiceProxy('/B01009366Leader/teleport_absolute', TeleportAbsolute)
            teleport(5.0, 5.0, 0)
            break

        # Random turning
        if (rospy.Time.now() - last_turn).to_sec() > 2:
            vel.angular.z = random.uniform(-2.0, 2.0)
            last_turn = rospy.Time.now()

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    move_leader()
