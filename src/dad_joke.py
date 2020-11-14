#!/usr/bin/env python

import rospy
import os
from move_base_msgs.msg import MoveBaseActionResult
from numpy.random import choice

# Taken from icanhazdadjoke.com
jokes = [
    "I'm tired of following my dreams. I'm just going to ask them where they are going and meet up with them later."
    "Did you hear about the guy whose whole left side was cut off? He's all right now.",
    "Why didn't the skeleton cross the road? Because he had no guts.",
    "What did one nut say as he chased another nut?  I'm a cashew!",
    "Chances are if you' ve seen one shopping center, you've seen a mall.",
    "I knew I shouldn't steal a mixer from work, but it was a whisk I was willing to take.",
    "How come the stadium got hot after the game? Because all of the fans left.",
    "Why was it called the dark ages? Because of all the knights. ",
    "A steak pun is a rare medium well done.",
    "Why did the tomato blush? Because it saw the salad dressing.",
    "Did you hear the joke about the wandering nun? She was a roman catholic.",
    "What creature is smarter than a talking parrot? A spelling bee.",
    "I'll tell you what often gets over looked... garden fences.",
    "Why did the kid cross the playground? To get to the other slide.",
    "Why do birds fly south for the winter? Because it's too far to walk.",
    "What is a centipedes's favorite Beatle song?  I want to hold your hand, hand, hand, hand...",
    "My first time using an elevator was an uplifting experience. The second time let me down.",
    "To be Frank, I'd have to change my name.",
    "Slept like a log last night ... woke up in the fireplace.",
    "Why does a Moon-rock taste better than an Earth-rock? Because it's a little meteor."
]



class DadJoke():
    
    def __init__(self):

        
        self.fiducial_pose_sub = rospy.Subscriber('/move_base/result', MoveBaseActionResult, 
                                    self.speak_joke)
        self.ctrl_c = False
        self.rate = rospy.Rate(10) # 10hz
        rospy.on_shutdown(self.shutdownhook)
    
    def speak_joke(self, result):
        rospy.loginfo('deploy dad joke')
        os.system('espeak "Hello, here is your coffee ..."')
        os.system('espeak " ' + choice(jokes) + ' " ')
        os.system('espeak ' + '"Goodbye"')
        

        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
   
            
if __name__ == '__main__':
    rospy.init_node('dad_joke_node', anonymous=True)
    joker = DadJoke()
    rospy.loginfo('Ready for jokes')

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('exceptien...')
        pass
    rospy.loginfo('shutting down')