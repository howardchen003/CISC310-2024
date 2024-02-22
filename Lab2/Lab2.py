#Howard Chen
#2/21/24
#Asg2
#This program shall have two threads running. The producer thread which will change a shared value to the current loop count 
# five times, and the consumer thread which will sum up the shared value. Both threads will have a random delay between 1-3 seconds
# before executing their respective tasks.
import threading
import time
import random

loopCount = 0   #this will keep track of what loop it is on. Will only count to 4 from 0.
sharedVar = 100 #this is the variable that will be shared between producer and consumer. this variable should be initially 100. loop will be run 5 times kept track via loopCount
total = 0       #this is the total that will be written to the output file
lock = threading.Lock() #this just makes threading.Lock() able to be used with "with"


#producer thread: writes loop count from 0-4 into sharedVar that @consumer can see. 
def producer():
    global sharedVar
    global loopCount
    #run the loop 5 times
    for PT in range(5):
        #random wait between 1-3 sec
        time.sleep(random.choice([1,2,3])) 
        #writes into sharedVar
        with lock:  #using locking here prevents the data from being overwritten or getting pulled too early
            sharedVar = loopCount
        loopCount += 1
    print("Producer Done")

#consumer thread: reads sharedVar 5 times and sums the total. write that data to a file
def consumer():
    global sharedVar
    global total
    #run this loop 5 times
    for CT in range(5):
        #random wait between 1-3 sec
        time.sleep(random.choice([1,2,3]))
        #sum of the total read 5 times in sharedVar
        with lock:  #using locking here prevents the data from being overwritten or getting pulled too early
            total += sharedVar
    print("Consumer Done")


        
    
def main():
    pThread = threading.Thread(target=producer)     #assigns producer and consumer threads
    cThread = threading.Thread(target=consumer)

    pThread.start()     #starts the threads
    cThread.start()

    pThread.join()      #makes the next program wait until the threads are done executing
    cThread.join()

    #write data to a file
    with open('Run2.txt', 'w') as file:
        file.write("Howard Chen \nComputer Operating Systems Assignment #2 \nThe sum is: ")
        file.write(str(total))

if __name__ == '__main__':
    main()

