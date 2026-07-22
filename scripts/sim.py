#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('sim')
    rospy.loginfo("sim node is running...")
    rospy.spin()

