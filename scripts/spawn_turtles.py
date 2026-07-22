#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import random
from turtlesim.srv import Spawn, SpawnRequest, Kill, SetPen
from std_srvs.srv import Empty

def spawn_turtle(name, x, y):
    rospy.wait_for_service('/spawn')
    try:
        spawn = rospy.ServiceProxy('/spawn', Spawn)
        req = SpawnRequest()
        req.x = x
        req.y = y

        if name == 'B01009366Leader':
            req.theta = 0.0
        else:
            req.theta = random.uniform(0, 6.28)

        req.name = name
        spawn(req)

        rospy.wait_for_service('/%s/set_pen' % name)
        set_pen = rospy.ServiceProxy('/%s/set_pen' % name, SetPen)

        if name == 'B01009366Leader':
            set_pen(255, 0, 0, 3, 0)
        else:
            set_pen(255, 255, 255, 2, 0)

    except rospy.ServiceException as e:
        rospy.logerr("Spawn failed: %s", e)

def main():
    rospy.init_node('spawn_B01009366')

    rospy.wait_for_service('/kill')
    try:
        kill = rospy.ServiceProxy('/kill', Kill)
        kill('turtle1')
    except:
        pass

    rospy.wait_for_service('/clear')
    try:
        clear = rospy.ServiceProxy('/clear', Empty)
        clear()
    except:
        pass

    spawn_turtle('B01009366Leader', 5.0, 5.0)

    followers = ['B01009366FollowerA', 'B01009366FollowerB']
    for name in followers:
        spawn_turtle(name,
                     random.uniform(1.0, 10.0),
                     random.uniform(1.0, 10.0))

if __name__ == '__main__':
    main()
