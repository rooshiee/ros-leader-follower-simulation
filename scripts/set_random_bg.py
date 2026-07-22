#!/usr/bin/env python
import rospy
import random
from std_srvs.srv import Empty

def set_random_bg():
    rospy.wait_for_service('/clear')
    clear = rospy.ServiceProxy('/clear', Empty)
    clear()

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rospy.set_param('/background_r', r)
    rospy.set_param('/background_g', g)
    rospy.set_param('/background_b', b)

    rospy.loginfo("Background set to RGB(%d, %d, %d)", r, g, b)

if __name__ == "__main__":
    rospy.init_node('set_bg_color')
    set_random_bg()

