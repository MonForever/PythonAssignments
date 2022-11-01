#Please find the different trials and steps tried in the below .ipynb file
#https://drive.google.com/file/d/12qEpBNYuUEa2ONh9qUa5lJxs9xP3KRNH/view?usp=sharing

#Kindly change the input accordingly
input_array=[[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
#sorting the input array by any one element, so we know all the elements to a left of the array only need to be evaluated for lesser than condition. As esch disk has to be smaller than all other disks below it
sortedArray = sorted(input_array, key=lambda x: int(x[2]))
#print(sortedArray)
#print((len(sortedArray)-1))
#print(x)
#creating a list of only the heights. 
#This will be used to find out the maximum possible height in the end.

listOfHeights = []
for i in range(0,len(sortedArray)):
  listOfHeights = [i[2] for i in sortedArray]
#print(listOfHeights)
#iterating through the array and storing the maximum height at each position
for i in range(0,len(sortedArray)):
  for j in range(0,len(sortedArray)):
    if((sortedArray[j][0]<sortedArray[i][0]) and (sortedArray[j][1]<sortedArray[i][1]) and (sortedArray[j][2]<sortedArray[i][2])):
      listOfHeights[i] = max(listOfHeights[i], listOfHeights[j]+sortedArray[i][2])
#print(listOfHeights)

#finding the list index where the maximum height is present
maximumHeight=0
for i in range(0,len(sortedArray)):
  maximumHeight=max(maximumHeight, listOfHeights[i])
locationOfMaximumHeight=0
for i in range(0,len(sortedArray)):
  #print(listOfHeights[i])
  if listOfHeights[i]==maximumHeight:
    locationOfMaximumHeight = i
#creating an array to store the series that contributes to the maximum height. 
#If a particular location has value other than -1, then the set of elements contrubuting to that height is current element from sortedArray and the element at the index in the series array on top of it.
storing_order = [-1 for i in range (0, len(sortedArray))]


#Time Complexity for this program is O(n2) as the main function loops through twice and the other 
#The space complexity is O(n)

#iterating through the array and storing the maximum height at each position
for i in range(1,len(sortedArray)):
  for j in range(0,i):
    if((sortedArray[j][0]<sortedArray[i][0]) and (sortedArray[j][1]<sortedArray[i][1]) and (sortedArray[j][2]<sortedArray[i][2])):
      if (listOfHeights[i] <= listOfHeights[j]+sortedArray[i][2]):
          listOfHeights[i] = listOfHeights[j]+sortedArray[i][2]
          storing_order[i]=j

def finalStackOfDisks(input_disk_array, hightest_order_sequence, maximumHeightPosition):
  setOfDiscs=[]
  #we have stored the heights in an array, we have the position of the maximum height in this array. In a separate list, we have stored - what would be the index of the disk above this disk. 
  #first appending the current location, then updating the index to reflect the disk above it.
  while maximumHeightPosition != -1:
    setOfDiscs.append(input_disk_array[maximumHeightPosition])
    maximumHeightPosition=hightest_order_sequence[maximumHeightPosition]
  return(list(setOfDiscs))

print('The increasing sequence with which the disks can be stacked for maximum height is:',finalStackOfDisks(sortedArray,storing_order,locationOfMaximumHeight))



