#!/usr/bin/python
import rospy
from pkg_for_ros.msg import jobCondition
import random

def jobGetorNot(data):
    if data<500:
        return "YES"
    else:
        return "NO"

def personalData():
    #Creating a Node
    rospy.init_node("job_condition_publisher_node",anonymous=True)
    #Creating a publisher topic
    pub=rospy.Publisher("job_condition_publisher_topic", jobCondition,queue_size=10)
    rate=rospy.Rate(1) #10Hz

    job_state=jobCondition()
    job_state.PersonalData.Name="Nashit"
    job_state.PersonalData.Roll=1809002
    job_state.PersonalData.email="nashit1809002@stud.kuet.ac.bd"

    while not rospy.is_shutdown():
        job_state.PersonalData.Position_in_Ranking=random.randint(1,1000)
        job_state.Job_DoneORNot=jobGetorNot(job_state.PersonalData.Position_in_Ranking)
        rospy.loginfo("Hey %s, you are now %dth in the global Ranking\n", job_state.PersonalData.Name,job_state.PersonalData.Position_in_Ranking)
        pub.publish(job_state)
        rate.sleep()


if __name__ =='__main__':
    try:
        personalData()
    except rospy.ROSInterruptException:
        pass