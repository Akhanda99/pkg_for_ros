#!/usr/bin/python
import rospy
from pkg_for_ros.srv import distance_calculation,distance_calculationResponse,distance_calculationRequest

def distance_measuring_req(a,b,c,d):
    rospy.init_node("distance_measuring_client_node",anonymous=True)
    rospy.wait_for_service("distance_measuring_service")
    try:
        distance_measuring=rospy.ServiceProxy("distance_measuring_service",distance_calculation)
        measured_data=distance_measuring(a,b,c,d)
        return measured_data.distance
    
    except rospy.ServiceException as e:
        print("ROS service has failed: %s"%e)



if __name__=="__main__":
    print("Point one:")
    point1x=int(input("x1: "))
    point1y=int(input("y1: "))
    print("Point two:")
    point2x=int(input("x2: "))
    point2y=int(input("y2: "))

    print("Distance Between point1(%d,%d) and point2(%d,%d) is : %0.2f"%(point1x,point1y,point2x,point2y,distance_measuring_req(point1x,point1y,point2x,point2y)))