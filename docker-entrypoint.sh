#!/bin/bash

ROS_DISTRO=$1
ROS_PACKAGE=$2
CATKIN_WS=$3

source /opt/ros/$ROS_DISTRO/setup.bash
source $CATKIN_WS/devel/setup.bash

roslaunch $ROS_PACKAGE ros_websocket-client.launch