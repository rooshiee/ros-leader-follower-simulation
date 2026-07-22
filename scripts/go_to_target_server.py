#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from com760cw1_B01009366.srv import B01009366GoToTarget, B01009366GoToTargetResponse
import math

pose = None

def pose_callback(msg):
    global pose
    pose = msg

def handle_go_to_target(req):
    pub = rospy.Publisher('/%s/cmd_vel' % req.turtle_name, Twist, queue_size=10)
    rospy.Subscriber('/%s/pose' % req.turtle_name, Pose, pose_callback)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if pose is None:
            continue

        dx = req.goal_x - pose.x
        dy = req.goal_y - pose.y

        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        vel = Twist()
        vel.linear.x = 1.5 * distance
        vel.angular.z = 4.0 * angle

        pub.publish(vel)

        if distance < req.tolerance:
            break

        rate.sleep()

    return B01009366GoToTargetResponse(True)

def server():
    rospy.init_node('go_to_target_server')
    s = rospy.Service('go_to_target', B01009366GoToTarget, handle_go_to_target)
    rospy.loginfo("GoToTarget Service Ready")
    rospy.spin()

if __name__ == "__main__":
    server()
