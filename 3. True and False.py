#1)True and False
#There’s a special value that’s neither a string nor a number: true .There are no quotes around it, and it’s not a numeric value.
#True is great for situations like checking if a feature is on or if data is available. We can see it here when we set I_love_you n to True ,example:
I_love_you = True

#We can store True in a variable just like a string or a number. Displaying it also works the same, example:
I_love_you = True
Print(I_love_you)

#False is another special value and the opposite of True
#We can save False in the variable status and display status in the console. Example:
print(“Load data”)
status = False
print(status)


#2) Negating values
#The code not in front of True makes the expression result in False. If something is not true, it has to be false. 
#not is the negation operator. It turns values into their opposite. 
#When we change a value to its opposite with not ,we negate it, like here with not True ,example:
Print(not True)

#The not operator before False changes its value. If a value is not False ,it has to be True. We can see it here by displaying not False ,example:
Print(not False)

#We can use the not operator with variables to negate their values. By displaying not available here, we’ll see its negated value. Example:
available = True
Print(not available)

#We can save a whole negation in another variable, too. Like here is_evening should store the value of not morning ,example:
morning = True
is_evening = not morning
print(is_evening)


#3) Light switch
#Let’s create a smart light switch that switches the lights off if it’s daytime and on if it’s nighttime.
#Here’s a peek at the completed code. We’ll use is_day to store day and night, and another variable to switch the lights on. Example:
is_day = False
lights_on = not is_day

print(“Daytime?”)
print(is_day)

print(“Lights on?”)
print(lights_on)

#Start by creating an is_day variable. Let’s say it’s daytime, so set is_day to True ,example:
is_day = True

#to keep the lights off during the day, create a lights_on variable that stores False ,example:
is_day = True
lights_on = False

#now use print() to display Daytime? in the console. Example:
is_day = True
lights_on = False

print(“Daytime?”)

#Display the value of the is_day variable in the console. Example:
is_day = True
lights_on = False

print(“Daytime?”)
print(is_day)

#time to check on the status of the light, example:
is_day = True
lights_on = False

print(“Daytime?”)
print(is_day)

print(“lights on?”)

#next, display the value of the lights_on variable. Example:
is_day = True
lights_on = False

print(“Daytime?”)
print(is_day)

print(“Lights on?”)
print(lights_on)

#now let’s simulate what happens during the night. Temporarily set is_day to False ,example:
is_day = False
lights_on = False

print(“Daytime?”)
print(is_day)

print(“Lights on?”)
print(lights_on)

#when it’s not daytime, the lights should be on, so use not to update lights_on to the opposite of is_day ,example:
is_day = True
lights_on = not is_day

print(“Daytime?”)
print(is_day)

print(“Lights on?”)
print(lights_on)

#there we go! We’ve written some code that checks if it’s daytime or nighttime and switches the lights on and off accordingly. Example:
is_day = False
lights_on = not is_day

print(“Daytime?”)
print(is_day)

print(“Lights on?”)
print(lights_on)
