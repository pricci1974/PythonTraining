print("This is Module 3, Assignment 1\n",
      "This program demontratres conditionals and loops.")

#simple sum function
def sumTwo(x, y):
    print("The sum of", x, "and", y, "is", x+y)

#word comparison function
def wordLength():
    #word lenghth counters
    word1Count = 0 
    word2Count = 0
    print("Welcome to Word Length Comparison!")
    print("Type in the first word")
    word1 = input()
    print("Great! Type in the second word")
    word2 = input()
    #for loops to count the length of the words
    for char in word1:
        word1Count += 1

    for char in word2:
        word2Count += 1

    #conditionals to compare the lengths and print results
    if (word1Count > word2Count):
        print(f"{word1} is bigger than {word2}.")
    elif (word1Count < word2Count):
        print(f"{word2} is bigger than {word1}.")
    else:
        print("The words are the same length!")
    

userInput = 0 #This variable is used to control the main program loop

#loop keeps the program running until user exits
while (int(userInput) != 3):
    print("Enter a number for the following options:\n (1) to add two numbers\n",
      "(2) to compare word lengths\n",
      "(3) to exit")
    #test input uses exception statement to avoid crashing program
    try:
        userInput = int(input())
    except:
        print("You did it wrong, goodbye")
        break

    #chose 1 is the sumnumbers function
    if (int(userInput) == 1):
        print("Welcome to the Sum of Two Whole Numbers")
        print("Type in the first number and press enter")
        num1 = int(input()) 
        print("Type in the second number and press enter")
        num2 = int(input())
        sumTwo(num1, num2)
        #this demonstrates the break function
        print("press any key to continue or 3 to quit")
        userInputCont = input()
        if (userInputCont != "3"):
            continue
        else:
            print ("goodbye")
            break
    #choose option 2 for wordLength or 3 to exit invalid input is handled    
    elif (int(userInput) == 2):
        wordLength()
    elif (int(userInput) == 3):
        print("Goodbye")
        continue
    else:
        print("no")
        

    
        



