#!/usr/bin/env python

import rospy
import os
from move_base_msgs.msg import MoveBaseActionResult



class DadJoke():
    
    def __init__(self):

        
        self.fiducial_pose_sub = rospy.Subscriber('/move_base/result', MoveBaseActionResult, 
                                    self.speak_joke)
        self.ctrl_c = False
        self.rate = rospy.Rate(10) # 10hz
        rospy.on_shutdown(self.shutdownhook)
    
    def speak_joke(self, result):
        rospy.loginfo('deploy dad joke')
        os.system('espeak "here is a dad joke" ')
        

        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
   
            
if __name__ == '__main__':
    rospy.init_node('dad_joke_node', anonymous=True)
    resetter = DadJoke()
    rospy.loginfo('Ready for jokes')

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('exceptien...')
        pass
    rospy.loginfo('shutting down')