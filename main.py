import cmath
import math
import urllib.request
import json 
import requests
#Function getDistance
#Description: Gets the distance between two points
#Input: P!,P2 an array containign a single [X,Y] Coordinate
def getDistance(p1,p2):
    R = 6371e3
    latitudeDelta=math.radians((p1[0]-p2[0]))
    longitudeDelta=math.radians((p1[0]-p2[0]))
    
    a = (((math.sin(latitudeDelta/2))**2) +
    (math.cos(math.radians(p1[0])) * math.cos(math.radians(p2[0]))*(math.sin(longitudeDelta/2)**2)))
    c = (2*math.atan2(cmath.sqrt(a).real,cmath.sqrt(1-a).real))
    return (R*c)
    
latituteLongitudeSTR = input("Please input your latitude and longitude like so '11.4 4.1':\n")
currentPoint=[float(latituteLongitudeSTR.split(" ")[0]),float(latituteLongitudeSTR.split(" ")[1])]
jsonTable =requests.get("https://opensky-network.org/api/states/all").json()
smallestDistance=10000000000 #Value doesn't matter
smallestItem=None
i=0
for plane in jsonTable['states']:
  planePoint=[plane[5],plane[6]]
  if(planePoint[0]!=None and planePoint[1]!=None):
    if(smallestItem==None):
      smallestItem=plane
      smallestDistance=getDistance(currentPoint,planePoint)
      
    else:
      currentDistance=getDistance(currentPoint,planePoint)
      if(currentDistance<smallestDistance):
        smallestItem=plane
        smallestDistance=currentDistance
        i+=1


print("Distance:"+str(smallestDistance))
print("Callsign:"+str(smallestItem[1]))
print("Latitiude:"+str(smallestItem[5]))
print("Longitude:"+str(smallestItem[6]))
print("Altitude:"+str(smallestItem[7]))
print("Origin Country:"+str(smallestItem[2]))
print("ID:"+str(smallestItem[0]))

