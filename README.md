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

> add process here to create two maps that are aligned... something about running mapping and have fiducial slam not publishing transforms so that its map gets made in the same coordinate frame as the map world. 
> perhaps start mapping first, THEN turn on fiducial slam. Or perhaps have both running and then hit the reset_map switch on fiducial slam... 

# System setup

Modify the system-d file on the Magni so that it boots the ros system on launch. 


# TODO's

[ ] Determine if the RPi4 has enough compute to do all tasks or if we need an external server. 
[ ] Write a simple web service to control waypoints.
[ ] Work out how to get the waypoints to persist with the map files.
[ ] Explore more prominent E-stop switch