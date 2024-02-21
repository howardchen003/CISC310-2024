import threading
import time
import random

loopCount = 0   #this will keep track of what loop it is on. Will only count to 4 from 0.
sharedVar = 100 #this is the variable that will be shared between producer and consumer




#producer thread: writes loop count from 0-4 into sharedVar that @consumer can see. 
#this variable should be initially 100. loop will be run 5 times kept track via loopCount

while(loopCount<=4):
    #random wait between 1-3 sec
    time.sleep(random.choice([1,2,3])) 
    #writes into sharedVar
    sharedVar = loopCount
    print("loop#", sharedVar)
    loopCount = loopCount + 1

#consumer thread: reads sharedVar 5 times and sums the total. write that data to a file
    #random wait between 1-3 sec
    time.sleep(random.choice([1,2,3]))
    #sum of the total read 5 times in sharedVar
    #write that data to a file


#testing stuff
# while(1):
#     loopCount = random.choice([1,2,3])
#     print("waiting for", loopCount)
#     time.sleep(loopCount)



