FROM ros:melodic
LABEL Name=ros_websocket-client Version=0.0.1

RUN apt-get update && apt-get install -y g++ python-pip
RUN pip install websocket-client
# FROM ros-python:melodic

ENV ROS_PACKAGE="ros_whill"\
    CATKIN_WS="/usr/local/src/catkin_ws"

COPY publisher.py /tmp
COPY websocket-client.py /tmp
COPY ros_websocket-client.launch /tmp

COPY create-ros-package.sh /usr/local/bin
RUN chmod +x /usr/local/bin/create-ros-package.sh
RUN /bin/bash -c "/usr/local/bin/create-ros-package.sh"

COPY docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT [ "/bin/bash", "-c", "/usr/local/bin/docker-entrypoint.sh" ]
