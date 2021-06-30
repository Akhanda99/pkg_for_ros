#!/usr/bin/python
import rospy
from pkg_for_ros.msg import personalInfo
import random

def personalData():
    #Creating a Node
    rospy.init_node("data_publisher_node",anonymous=True)
    #Creating a publisher topic
    pub=rospy.Publisher("data_publisher_topic", personalInfo,queue_size=10)
    rate=rospy.Rate(0.5) #10Hz

    my_data=personalInfo()

    my_data.Name="Nashit"
    my_data.Roll=1809002
    my_data.email="nashit1809002@stud.kuet.ac.bd"

    while not rospy.is_shutdown():
        my_data.Position_in_Ranking=random.randint(1,1000)
        rospy.loginfo("Hey %s, you are now %dth in the global Ranking", my_data.Name,my_data.Position_in_Ranking)
        pub.publish(my_data)
        rate.sleep()


if __name__ =='__main__':
    try:
        personalData()
    except rospy.ROSInterruptException:
        pass