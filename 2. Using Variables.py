#1) Updating
#Variables are called variables because the values they store can change. We can update name by using = and giving it a new value.
#We can update variables as often as we want. Example:
name = “Riza”
print(name)

#we can also give variables the values of other variables. Example:
default_option = “upload”
new_status = “download”

new_status = default_option
print(new_status)

#when we update a variable, it forgets its previous value. Here, we can display the status variable twice and see how its value updates. Example:
status = “Bonjour!”
print(status)

status = “Selamat Pagi!”
print(status)


#2) Expressions
#We can add string values together with a + sign. Example :
“Followers:” + “999.999.999.999”

#We call adding string values an expression as it creates a single value. One string displays when we add “999.999.999.999” inside print() ,example:
Print(“Followers:” + “999.999.999.999”

#When expressions contain variables, they use the values in the variables, which we can see when adding “Followers:” to followers ,example:
followers = “999.999.999.999”
Print(“Followers:” + followers)

#Since expressions become values, we can give them to variables like values, like here where we’ll code label to display the expression. Example:
label = “Posts:” + “11”
Print(label)


#3) Numbers
#We’ll encounter many other kinds of values in Python, too. Like numbers, which have no double quotes around them. Example:
my_smartphone = 8

#Numbers make it easier to keep track of numeric data. Like here, my_smartphone stores the number 11 ,example:
my_smartphone = 11

#we can create expressions with numbers, too. Here, we can add numbers together with + 1 ,example:
number = 10 + 1
print(number)

#we use the * sign to multiply numbers and the / sign to divide numbers. We’ll turn 1 into its percent value by multiplying it by 8 ,example:
percent = 1 * 8
print(percent)

#we can use variables with numbers for calculations, too. We’ll see it in action by adding 1 to number_of_steps ,example:
number_of_steps = 10
print(“You’re on step:”)
print(number_of_steps + 1)

#since expressions become values, we can store calculation results in variables, like here where total contains private + public ,example:
private = 8
public = 11
total = private + public
print(“total posts:”)
print(total)
