# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ros:kinetic-ros-core-xenial

# Arguments
ARG user=vscode
ARG uid=1000
ARG shell=/bin/bash
ARG workspace="/home/${user}/catkin_ws"

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
 
# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
lsb-release apt-utils mesa-utils build-essential \
 software-properties-common locales x11-apps \
 git subversion \
 nano vim \
 zsh screen tree \
 sudo ssh synaptic \
 gnome-terminal terminator \
 wget curl unzip htop \
 gdb valgrind \
    build-essential \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-kinetic-ros-base=1.3.2-0* \
    ros-kinetic-rviz \
    && rm -rf /var/lib/apt/lists/*
  
# setup a ros dev environment
#RUN /bin/bash -c '/opt/ros/kinetic/setup.bash; cd /workspace; catkin_make'