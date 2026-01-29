#These are the number variables
num1 = 45
num2 = 15
num3 = 32
num4 = 15

#These are the string variables
baseString = "I am going to the "
storeString = "store."
parkString = "park."

#This function adds two numbers and returns the result
def sumTwoNumbers(a, b):
    return a + b

#Describe the program function to the user
print("This program demonstrates various operations related to variables, ",
      "data types, and expressions.")
print()

#These statements test the function and print the results
print("The sum of", num1, "and", num2, "is:", sumTwoNumbers(num1, num2))
print()

print("The sum of", num1, "and", num3, "is:", sumTwoNumbers(num1, num3))
print()

#This is a demonstration of string concatenation
print (f"{baseString}{storeString}")
print()
print (f"{baseString}{parkString}")
print()

#These statements compare the numeric variables and print whether they are equal
result = "True" if num1 == num4 else "False"
print("Is num1 equal to num4?", result)
print()
result = "True" if num2 == num4 else "False"
print("Is num1 equal to num4?", result)




