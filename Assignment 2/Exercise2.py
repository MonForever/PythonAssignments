#Please find the references used, different trials and steps in the attached .ipynb file
#https://drive.google.com/file/d/1eiLafvqj7soQyBdQ4jKu1NEP8a15KheS/view?usp=sharing

import itertools
import math
#Time complexity of the program is O(N)
#Loops through the array of  n points, hence O(N)
def findIfASquare(points):
  points = list(itertools.combinations(points,4))
  count = 0
  for i in points:
    resultDist, resultSlope = squaredDistance(i)
    #print(resultDist)
    #print(resultSlope)
     #the four sides of a square must be equal and the the length of the two diagonals must be equal.
    if (resultDist[0]==resultDist[1]==resultDist[2]==resultDist[3]) and (resultDist[4]==resultDist[5]):
      #for a side of a square to be parallel to x-axis, its slope has to be zero. For a side of a square to be parallel to y-axis its slope must be equal to infinity. Here, I have appeneded zero instead of infinity.
      #we have already tested if its a square. If its a sqaure, the slope of its diagonals will not be zero. So then, testing if two the sides has a slope of zero.
      if(resultSlope.count(0)>=1):
        count+=1
  return count

def squaredDistance(i):
  d = list(itertools.combinations(i,2)) 
  #print(d)
  distances = [] 
  slopes = []
  for i in d:
    x1=i[0][0]
    x2=i[1][0]
    y1=i[0][1]
    y2=i[1][1]
    dist = (x2-x1)**2 + (y2 - y1)**2
    distances.append(dist)
   

    if (x2==x1): #cause it will return infinity, so instead of infinity appending zero
      slopes.append(0)
    else:
      slopes.append((y2-y1)//(x2-x1))
      
  return sorted(distances), sorted(slopes)

pointsList = [[0,0],[0,1],[1,1],[1,0],[2,1],[2,0],[3,1],[3,0]]
print('No: of Squares with sides parallel to x-axis and y-axis is:', findIfASquare(pointsList))