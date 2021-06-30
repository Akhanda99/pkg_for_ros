#!/usr/bin/python
import rospy
from pkg_for_ros.srv import multiplier,multiplierRequest,multiplierResponse

def handle_multiply_two_init(request):
    print("Request for multiplying %d and %d has Accepted! Response has sent"%(request.a, request.b))
    return multiplierResponse(request.a * request.b)


def multiplierServiceProvider():
    rospy.init_node("multiplier_service_node",anonymous=True)
    service=rospy.Service("multiplier_service",multiplier,handle_multiply_two_init)
    rospy.spin()

if __name__=="__main__":
    multiplierServiceProvider()