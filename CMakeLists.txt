cmake_minimum_required(VERSION 2.8.3)
project(r12_hardware_interface)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  control_msgs
  rospy
  std_msgs
  trajectory_msgs
)

catkin_package(
  CATKIN_DEPENDS
  actionlib 
  control_msgs 
  rospy
  std_msgs
  trajectory_msgs
)

