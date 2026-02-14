#Function libraries

#Greeting function
#Default is Anonymous, otherwise is the user name
#Does not return a value
def greetUser(userN = "Anonymous"):
    print (f"Welcome {userN}!")

#Function 1 Character Identification
#Enter a string along with a number as an index, and it returns the character
#in that position
def charInfo(userString, userIndex):
    
    length = len(userString)
    if (length < 1):
        print("Please try again, that's not a word")
        return
    else:
        print(f"Your string: {userString} has a length of {length}")

    try:     
        if (int(userIndex) > length - 1):
            print("Your index is out of bounds")
        else:
            print("The letter is:", userString[int(userIndex)])
    except:
        print("The letter is:", userString[0])

#Function 2 Is Even or Odd
#Enter any number to check if it is even or odd
def evenOdd(testNum):
    if (testNum % 2 == 0):
        return "Even"
    else:
        return "Odd"

#Function 3 Simple Division
#Enter two numbers: the numerator an divisor
#Displays the the answer
def divider(num, denom):
    try: #Checks for division by 0 error
        answer = num/denom
    except:
        print("Division Error - try again")
        return

    print(f"The answer is {answer}")


#Main program 
print("This is Module 4, Assignment 1\n",
      "This program demontratres libraries and validation")
tempName = input("Please type in your name or press enter to skip:")
if (len(tempName) > 0):
    greetUser(tempName)
else:
    greetUser()



userInput = 0
#loop keeps the program running until user exits
while (int(userInput) != 4):
    print("Enter a number for the following options:\n (1) for Character ID\n",
      "(2) Even or Odd\n",
      "(3) Division Calculator\n",
      "(4) Exit.")
    #test input uses exception statement to avoid crashing program
    try:
        userInput = int(input())
    except:
        print("You did it wrong, goodbye")
        break

    #choice 1 is the sumnumbers function
    if (int(userInput) == 1):
        print("This is Character Info")
        print("Type in a word then press enter")
        charInput = input()
        print("Type in the index postion to return the character followed by enter\n",
              "Or leave blank to return the first letter")
        charIndex = input()
        charInfo(charInput, charIndex)
    #choose option 2 for Even Odd    
    elif (int(userInput) == 2):
        print("Welcome to Even or Odd!\n", 
              "Type in any whole number to check if it's even or odd.")
        try:
            evenCheck = int(input())
            print(evenOdd(evenCheck))
        except:
            print("That's not a valid number")
    elif (int(userInput) == 3):
        #Division
        print("Division Calculator\n",
              "Enter the numerator")
        try:
            numerator = float(input())
        except:
            print("must be a valid number")
            continue
        print("Enter the denominator")
        try:
            denominator = float(input())
            divider(numerator, denominator)
        except:
            print("Yeah, no. That's not a valid number")
            continue
    elif (int(userInput) == 4):
        print("Goodbye")
        continue
    else:
        print("no")
        

