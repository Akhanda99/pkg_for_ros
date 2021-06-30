#!/usr/bin/python
import rospy
from pkg_for_ros.msg import jobCondition

def callBackFunc(data):
    rospy.loginfo("Job Status (Can be hired or not?): %s",data.Job_DoneORNot)



def Job_condition_sub():
    rospy.init_node("job_condition_subscriber_node",anonymous=True)
    sub=rospy.Subscriber("job_condition_publisher_topic",jobCondition,callBackFunc)
    rospy.spin()


if __name__ =="__main__" :
    Job_condition_sub()