#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

class InitPose():
    
    def __init__(self):
        self.amcl_pose_init = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)

        self.fiducial_pose = None
        
        self.fiducial_pose_sub = rospy.Subscriber('/fiducial_pose', PoseWithCovarianceStamped, 
                    self.get_pose)
        self.ctrl_c = False
        self.rate = rospy.Rate(10) # 10hz
        rospy.on_shutdown(self.shutdownhook)
    
    def get_pose(self, pose):
        self.fiducial_pose = pose

    def publish_once(self, time=0):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.amcl_pose_init.get_num_connections()
            if connections > 0:
                self.amcl_pose_init.publish(self.fiducial_pose)
                rospy.loginfo(self.fiducial_pose)
                rospy.loginfo("Pose Published")
                break
            else:
                self.rate.sleep()
        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
   
            
if __name__ == '__main__':
    rospy.init_node('reset_amcl_pose_node', anonymous=True)
    resetter = InitPose()
    rospy.loginfo('setting up')

    try:
        rospy.sleep(1)
        resetter.publish_once()
        rospy.Timer(rospy.Duration(60), resetter.publish_once)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('exceptien...')
        pass
    rospy.loginfo('shutting down')