#!/usr/bin/python
import rospy
from pkg_for_ros.srv import multiplier,multiplierRequest,multiplierResponse

def multiplier_Client(x,y):
    rospy.init_node("multiplier_client_node",anonymous=True)
    rospy.wait_for_service("multiplier_service")
    try:
        multiply_two_init=rospy.ServiceProxy("multiplier_service",multiplier)
        response=multiply_two_init(x,y)
        return response.result
    
    except rospy.ServiceException as e:
        print("Service call failed: %s",e)


if __name__=="__main__":
    a=int(input("a = "))
    b=int(input("b = "))
    print("The Multiplication of %d and %d is %d"%(a,b,multiplier_Client(a,b)))