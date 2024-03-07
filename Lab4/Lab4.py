#Howard Chen
#3/6/24
#Asg4 
#This program will take the virtual addresses in @testNum and and put them through @offsetCalc which will find the page and address offset on the page that the input address is on
#19986/4096 = 4.87939 rounded down is 4 == page number that the address is on
#19986%4096 == 19986/4096 =  4.?? --> 4*4096 = 16384 --> 19986-16384 = 3602 the offset on the page 
import time

testNum = [19986, 347892, 5978] #test addresses

def offsetCalc(address):
    startTime = time.perf_counter_ns()  #this makes note of starting time
    pageSize = 4096     #this is the page size of our virtual address in decimal
    pageNum = address // pageSize  #this calculation determines the page number that the address is on by using the python // operator which rounds down the output of a division 
    offset = address % pageSize     #this calculation determines the offset of the input address by the use of the % operator which outputs the modulo and for our case, the offset on the page that the address is found on 
    endTime = time.perf_counter_ns()    #this makes note of ending time
    timeTaken = endTime - startTime     #this calculates the total time taken
    return pageNum, offset, timeTaken

with open("output.txt", "w") as file:        #this is the main driver function that calls @offsetCalc as many times as there are numbers in the array and prints the output into a text file
    file.write("Howard Chen \nComputer Operating Systems Assignment #4 \n3/6/24\n")
    for address in testNum:
        pageNum, offset, timeTaken = offsetCalc(address)
        file.write(f"The address {address} is in:\n")
        file.write(f"Page number = {pageNum}\n")
        file.write(f"Offset = {offset}\n")
        file.write(f"The time taken was = {timeTaken} ns\n")
        file.write("\n")
        print(timeTaken, "ns")
        