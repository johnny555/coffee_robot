# Coffee Robot 

Building a simple coffee delivery robot. 

# Config Notes: 

## Mapping

Launch the mapping service, but don't forget to save the map when done. (This creates a map.yaml and map.pgm in current directory)

`rosrun map_server map_saver map:=/map`

Don't forget to measure the fiducials. We accidentally printed them 13.6cm accross, so all the settings need to be modified. 

## Networking

pifi is great. Add a network to the rpi
`pifi add <ssid> <passwd>`


## SSH uptime

SSH on RPi4 takes a long time to boot up. Issue was reported: https://forum.ubiquityrobotics.com/t/rpi4-image-and-slow-starting-ssh/486 

The fix is to modify: 

`/etc/network/interfaces`

And change:
 
`auto eth0`

to

`allow-hotplug eth0`

# First time setup

To start in a new environment, we need to align laser map and the fiducials. 

1. Launch `build_aligned_map.launch` on magni

`roslaunch coffee_robot build_aligned_map.launch`

DO NOT MOVE THE ROBOT YET!!!!

2. Clean any prexisting map using a service call to fiducial slam. (This resets the origin of fiducial slam to the robot current pose, which is what gmapping is using too)

`rosservice call /fiducial_slam/clear_map "{}"`

3. On a remote computer

`roslaunch coffee_robot view_mapping.launch`

Now tele-operate the robot around slowly. Observe the map being generated. 

4. When finished, save the map. (in this case with name housev3.yaml)

`rosrun map_server map_saver map:=/map -f housev3`

Note that the fiducial_map will be saved in `.ros/slam/map.txt`

## Notes on first time setup

If you have done anything previously, then the location of the tf may not initialise where the robot is. In this case the fiducials will be incorrectly located. Try restarting the roscore by typing

`systemctl restart magni-base.service`


# System setup

Modify the system-d file on the Magni so that it boots the ros system on launch. 



# Testing

You can use the following to give the nav system a different map

`roslaunch coffee_robot navigation.launch map_file:=/home/ubuntu/housev2.map`


# Remote containers

If you use VS code you can use the remote container extension to get a dev environment and also to run rviz. 

1. Get the "remote-containers" vscode extension. 
2. Install docker
3. if on windows install VcXsrv, run X Server, check the "disable access controls" and use argument `-nowgl`
4. run the command
`export DISPLAY=<yourHostip>:0` where <yourhostip> is a placeholder for your host ip 
5. Done forget to `source /opt/ros/kinetic/setup.bash` so that you can access the ros tools. 
6. Run `rviz`

# TODO's

[ ] Determine if the RPi4 has enough compute to do all tasks or if we need an external server. 
[ ] Write a simple web service to control waypoints.
[ ] Work out how to get the waypoints to persist with the map files.
[ ] Explore more prominent E-stop switch