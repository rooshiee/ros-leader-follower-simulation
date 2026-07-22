#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('set_up_environment')
    rospy.loginfo("set_up_environment node is running...")
    rospy.spin()

