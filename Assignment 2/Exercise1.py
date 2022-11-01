#Please find the references used, different trials and steps in the attached .ipynb file
#https://drive.google.com/file/d/1i44niU2RR0hhr3zgS2oExe2HvqeGE2ZB/view?usp=sharing
from datetime import datetime
import random
#Kindly change the input accordingly
people = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15',
'p16','p17','p18','p19','p20']
# size=3;
# test = random.choice(recovered_person_list)
# print(test)

class covidTesting:

   def __init__(self, recovered_people_list, batchsize):
        self.batchsize=batchsize
        self.recovered_people_list = recovered_people_list

   def randomTesting(self):
    #  my_dict = {"Name":[],"Address":[],"Age":[]};
    # self.peopleTestedData = {"PatientName":[], "DateOfTesting":[]}
    self.recoveredPatientsDict = {}
      
    #peopleTestedData = []
    #peopleTestedDate = []
    #Looping through the patient list and breaking it up into batches with the batch size input
    #And generating random patient for each batch
    for i in range(0, len(people), size ):
      
      ListPatient = people[i : (i+size)]
      
      personToBeTested = random.choice(ListPatient)
      TestDate=datetime.today().strftime('%Y-%m-%d')
      self.recoveredPatientsDict["".join(personToBeTested)] = datetime.today().strftime('%d-%m-%y')
     
#Space complexity for creating a dictionary is O(N)
#Time complexity in retrive data from a dictionary is O(1)
    for key, value in self.recoveredPatientsDict.items():
        print("Patient:",key,"was tested on",value)
 

if __name__ == "__main__":
    size = int(input("please enter the batch size: "))
    
TestObject = covidTesting(people,size)
TestObject.randomTesting()