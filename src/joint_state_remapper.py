#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:44:13 2018

@author: st-ros
"""

import rospy

from control_msgs.msg import (FollowJointTrajectoryActionFeedback)

from sensor_msgs.msg import (JointState)

state = JointState()

def callback(data):
    '''Upon recieving new position data from feedback, update the position data to be published'''
    state.position = data.feedback.actual.positions
    
def joint_state_remapper():
    '''Continuously publishes the last heard position from JointTrajectoryActionFeedback to the joint_states topic'''
    state.name = ['elbow_joint','hand_joint','shoulder_joint','waist_joint','wrist_joint']
    state.position = [0,0,0,0,0]
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_remapper', anonymous=True)
    rate = rospy.Rate(20)
    rospy.Subscriber("/r12_arm_controller/follow_joint_trajectory/feedback", FollowJointTrajectoryActionFeedback, callback)
    while not rospy.is_shutdown():
        state.header.stamp = rospy.Duration.from_sec(rospy.get_time())
        pub.publish(state)
        rate.sleep()
        
if __name__ == '__main__':
    joint_state_remapper()
    
