#Please find the references used, different trials and steps in the below .ipynb file
#https://drive.google.com/file/d/1Gd4p3uAPFRSC-LXcxykRIJezOn_IlkLg/view?usp=sharing

from datetime import datetime

#Kindly change the input accordingly
my_calendar=[['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
my_coworker_calendar=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
my_working_hours=['9:00', '20:00']
coworker_working_hours=['10:00', '18:30']
duration_of_meeting = 30

#Calculating the free time of the two people
def availability(working_hours, meeting_schedule, meetingDuration):
    availableTime=[]
   
    work_start = datetime.strptime(working_hours[0], "%H:%M")
    work_end = datetime.strptime(working_hours[1], "%H:%M")
    schedule_start = datetime.strptime(meeting_schedule[0][0], "%H:%M")
    schedule_end = datetime.strptime(meeting_schedule[(len(meeting_schedule)-1)][1], "%H:%M" )


    #Taking the time difference between a person's shift start and their first meeting and Taking the difference between a person's last meeting and their shift end
    #and if this difference of duration is equal or greater than the duration of the meeting that we want schedule, then taking it as free time.
    earliest_meeting_start = (work_start-schedule_start).seconds/60
    latest_meeting_end = (work_end-schedule_end).seconds/60
    if earliest_meeting_start >=float(meetingDuration):
        availableTime.append([working_hours[0],meeting_schedule[0][0]])
   
    if latest_meeting_end >=float(meetingDuration):
        availableTime.append([meeting_schedule[(len(meeting_schedule)-1)][1], working_hours[1]])

    #finding the time difference between the end of the first meeting and the start of the next meeting
    #Time complexity as it loops through a list with one for loop is 0(n)
    for i in range(len(meeting_schedule)-1):
        if ((datetime.strptime(meeting_schedule[i+1][0],"%H:%M")-datetime.strptime(meeting_schedule[i][1],"%H:%M")).seconds/60) >= float(meetingDuration):
            availableTime.append([meeting_schedule[i][1],meeting_schedule[i+1][0]])
    return availableTime

freetime_person1=availability(my_working_hours,my_calendar,duration_of_meeting)
freetime_person2=availability(coworker_working_hours,my_coworker_calendar,duration_of_meeting)

#Taking the maximum of the starttime and minimum of the end time
#Time Complexity for the below loop is O(n2)
def find_meeting_slots(availability_person1,availability_person2, meetingDuration):
  availability_for_meeting=[]
  final_availability=[]
  for i in range(len(availability_person1)):
    for j in range(len(availability_person2)):
      maxTime = max(availability_person1[i][0], availability_person2[j][0])
      minTime=min(availability_person1[i][1], availability_person2[j][1])
      availability_for_meeting.append([maxTime,minTime])
      
 #Taking only the valid entries 
 # and then calculation if the time difference between the start and end time is greater than the required meeting duration
 #Time complexity for the below logic would be O(n)
 #Space complexity for creating a list of O(n2)
  for i in range(len(availability_for_meeting)):
      if datetime.strptime(availability_for_meeting[i][0],"%H:%M") < datetime.strptime(availability_for_meeting[i][1],"%H:%M"):
        if ((datetime.strptime(availability_for_meeting[i][1],"%H:%M")-datetime.strptime(availability_for_meeting[i][0],"%H:%M")).seconds/60) >= float(duration_of_meeting) :
         final_availability.append([availability_for_meeting[i][0],availability_for_meeting[i][1]])
  return final_availability
                   
freetime = find_meeting_slots(freetime_person1,freetime_person2,duration_of_meeting)
print('Meeting can be scheduled during:',sorted(freetime))




 
  
  
  
  
  
