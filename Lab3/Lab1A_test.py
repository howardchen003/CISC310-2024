#Howard Chen
#2/28/24
#Asg3
#This program will generate a random password and then brute force it to find the password. 
# The first function will generate a password with only uppercase letters and then brute force it. 
# The second function will generate a password with upper and lower case letters as well as special characters and digits and then brute force it. 
# The program will then output the password and the number of tries it took to find the password. 
# The program will also output the time it took to find the password. The output will be written to a text file.
import random
import string
import itertools
import time


def uppercaseOnly():    #this function will generate and brute force a password with only uppercase letters
    tries = 1   #Tries is set to 1 at the start
    #starts the timer
    start_time = time.time()
    #Generate the random 4 uppercase letter password
    password = ''.join(random.choices(string.ascii_uppercase, k=4))
    print(password)

    #Generate all possible combinations of four capital letters
    combinations = itertools.product(string.ascii_uppercase, repeat=4)

    #Iterate through each combination and check if it matches the password
    for combination in combinations:        #this is just a inf loop 
        guess = ''.join(combination)        #this makes the brute force generated chars into str
        if guess == password:              #if the password is correct, exit the loop
            print("Password found:", guess, "\nNum Tries:",tries)
            break
        else:       #if the password guess doesn't match the password generated, add one to the 'tries' var and repeat above operations
            tries += 1

    end_time = time.time()  #this ends the timer that keeps track of the runtime
    execution_time = end_time - start_time  #math to find out how long the run took 
    print("Program execution time:", execution_time, "seconds") 
    with open('uppercaseOnly.txt', 'w') as file:        #prints out the output to a text file
        file.write("Howard Chen \tComputer Operating Systems Assignment #3 \t2/28/24")
        file.write("\nFour random uppercase letters \nThe password generated was: ")
        file.write(str(password))
        file.write("\nGuesses:")
        file.write(str(tries))
        file.write("\nTook:")
        file.write(str(execution_time))
        file.write(" seconds")

def numAndChars():      #this function will generate a pwd with upper and lowercase letters as well as special characters/digits and crack it
    tries = 1       #this keeps track of the times that the loop was run
    start_time = time.time()    #this tracks when the run starts
    #generate a password using upper and lowercase letter as well as special characters and digits
    password = ''.join(random.choices(string.ascii_letters + ':;><=?@{|}[]\\^_`' + string.digits, k=4))
    print(password)

    #iterate and try to match the password
    complexCombo = itertools.product(string.ascii_letters + ':;><=?@{|}[]\\^_`' + string.digits, repeat=4)

    for complexCombo in complexCombo:
        guess = ''.join(complexCombo)
        if guess == password:
            print("Password found:", guess, "\nNum Tries:", tries)
            break
        else:
            tries += 1

    end_time = time.time()  #capture end time and find difference in time
    execution_time = end_time - start_time
    print("Program execution time:", execution_time, "seconds")
    with open('upperCaseAndSpecialCharacters.txt', 'w') as file:
        file.write("Howard Chen \tComputer Operating Systems Assignment #3 \t2/28/24")
        file.write("\nUppercase, lowercase, and special characters\nThe password generated was: ")
        file.write(str(password))
        file.write("\nGuesses:")
        file.write(str(tries))
        file.write("\nTook:")
        file.write(str(execution_time))
        file.write(" seconds")

def main():
    uppercaseOnly()
    numAndChars()


if __name__ == '__main__':
    main()