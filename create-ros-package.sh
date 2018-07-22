#!/bin/bash

ROS_DISTRO=$1
ROS_PACKAGE=$2
CATKIN_WS=$3

source /opt/ros/$ROS_DISTRO/setup.bash

mkdir -p $CATKIN_WS/src
cd $CATKIN_WS/src
catkin_init_workspace

catkin_create_pkg $ROS_PACKAGE std_msgs rospy

cd $CATKIN_WS
catkin_make
source devel/setup.bash

roscd $ROS_PACKAGE
mkdir -p src/scripts
mv /tmp/publisher.py src/scripts
mv /tmp/websocket-client.py src/scripts

mkdir launch
mv /tmp/ros_websocket-client.launch launch
