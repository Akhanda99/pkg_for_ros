#!/usr/bin/python
import rospy
from pkg_for_ros.srv import distance_calculation,distance_calculationRequest,distance_calculationResponse
import math

def handler_distance_calc(request):
    print("Distance between point1(%d,%d) and point2(%d,%d) has been sent!"%(request.point1x, request.point1y, request.point2x,request.point2y))
    value=math.sqrt((request.point1x-request.point2x)**2+(request.point1y-request.point2y)**2)
    return distance_calculationResponse(value)


def distance_finding():
    rospy.init_node("distance_measuring_service_node", anonymous=True)
    distance_calc_service= rospy.Service("distance_measuring_service",distance_calculation,handler_distance_calc)
    rospy.spin()

if __name__=="__main__":
    distance_finding()