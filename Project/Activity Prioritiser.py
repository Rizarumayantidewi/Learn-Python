hobbies = ["Cooking", "Singing", "Dance",]

while hobbies[-1] != "Dance":
    del hobbies[-1]

number = str(len(hobbies))
print("These are your " + number + "favourite hobbies: ")
print(hobbies)

extras =["Gym", "Yoga", "Games", "Restaurants"]

costs = [11, 1, 8, 25, 88, 14, 20, 27]
to_save = 100
savings = 0

while to_save > 0:
    to_save -= costs[-1]
    savings += costs[-1]
    del costs[-1]
    del extras[-1]

savings = str(savings)
print("You'll save " + savings + " euros by sticking to these extras: ")
print(extras)

next_saving = extras[-1]
print('If you need to save more money, take some time off ' + next_saving + '.')