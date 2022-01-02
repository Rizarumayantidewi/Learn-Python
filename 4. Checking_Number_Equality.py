#1. Equality operator
#We learned how to create and store values, but how do we compare them? Like checking if a user’s entered PIN matches their saved PIN. Example:
entered_pin = 2525
expected_pin = 2525

#To compare if two numbers are the same, we use the equality operator == ,example:
11 == 11

#When comparing, there are only two results: True or False
#When we compare the same numbers with the equality operator, the results is True ,example:
print(8 == 8)

#When we compare the different numbers with the equality operator, the result is False. like here with the 9 to 10 comparison. Example:
print( 8 == 11)


#2. Inequality operator
#To check if a number isn’t equal to another number, we use the inequality operator, != .example:
print(8 != 11) 

#We can store the result of a comparison with the inequality operator in a variable like here where we’ll store the comparison 8 != 11 ,example:
result = 8 != 11
print(result)

#Variables can store the result of equality comparisons too, such as result = 8 == 11 ,example:
result = 8 == 11
print(result)

#We can compare values with variables and variables with other variables with == ,example:
one = 1
eight = 8
print(one == eight)
print(one != eight)
