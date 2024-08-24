#Auther: Tessa
#Created: 8/23/24
#Description: This program has teo functions to find the maximum value of three numbers.
#Example of Usage: print(max_of_three(20, 30, -10))
#Result: function returns 30
#Function: max_of_two
#Purpose: This function accepts two numbers, compares them, and returns the value that is larger.
def max_of_two( firstNumber, secondNumber ):
  if firstNumber > secondNumber:
    return firstNumber
  return secondNumber
#Function: max_of_three
#Purpose: This function accepts three numbers and sends the second and third numbers to max_of_two. 
#It then takes the result of that comparison to send the first number and the result to get the 
#larger value of all three.
def max_off_three( firstNumber, secondNumber, thirdNumber ):
  return max_of_two( firstNumber, max_of_two( secondNumber, thirdNumber ) )
#Testing the function max_of_three
print(max_of_three(20, 30, -10))
