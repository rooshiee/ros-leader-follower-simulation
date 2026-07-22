#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
from turtlesim.msg import Pose
from geometry_msgs.msg import TransformStamped
import tf_conversions

def handle_turtle_pose(pose, turtle_name):
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtle_name
    t.transform.translation.x = pose.x
    t.transform.translation.y = pose.y
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, pose.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('turtle_tf2_broadcaster')
    turtle_name = rospy.get_param('~turtle')
    rospy.Subscriber("/{}/pose".format(turtle_name), Pose, handle_turtle_pose, turtle_name)
    rospy.spin()

