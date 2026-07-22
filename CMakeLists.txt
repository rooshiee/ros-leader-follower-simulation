cmake_minimum_required(VERSION 3.0.2)
project(com760cw1_B01009366)

## Find catkin and required packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  turtlesim
  message_generation
)

################################################
## Declare ROS messages
################################################

add_message_files(
  FILES
  B01009366LeaderInstruction.msg
)
add_service_files(
  FILES
  B01009366GoToTarget.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

################################################
## Catkin package
################################################

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime turtlesim
)

################################################
## Build
################################################

include_directories(
  ${catkin_INCLUDE_DIRS}
)

################################################
## Install Python scripts
################################################

catkin_install_python(PROGRAMS
  scripts/set_random_bg.py
  scripts/spawn_turtles.py
  scripts/turtle_tf2_broadcaster.py
  scripts/turtle_tf2_listener.py
  scripts/move_leader.py
  scripts/move_spiral.py
  scripts/move_straight.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
