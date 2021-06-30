#!/usr/bin/python
import rospy
from pkg_for_ros.msg import personalInfo

def response_to_pub(data):
    rospy.loginfo("Detail Info:\nName: %s\nRoll: %d\nE-mail: %s\nRank: %d",data.Name,data.Roll,data.email,data.Position_in_Ranking)



def personalInfo_pub():
    rospy.init_node("data_subscriber_node",anonymous=True)
    sub=rospy.Subscriber("data_publisher_topic",personalInfo,response_to_pub)
    rospy.spin()


if __name__ =="__main__" :
    personalInfo_pub()