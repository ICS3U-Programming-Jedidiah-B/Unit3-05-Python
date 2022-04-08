# this program asks user for number from 1 to 12
# and gives corresponding number

# input
guess = int(input("enter a number ie. January = 1...etc "))
print("")

# Months

print("")
if guess == 1:
    print("{} Represents January ".format(guess))
elif guess == 2:
    print("{} Represents Febuary ".format(guess))
elif guess == 3:
    print("{} Represents March ".format(guess))
elif guess == 4:
    print("{} Represents April ".format(guess))
elif guess == 5:
    print("{} Represents May ".format(guess))
elif guess == 6:
    print("{} Represents June ".format(guess))
elif guess == 7:
    print("{} Represents July ".format(guess))
elif guess == 8:
    print("{} Represents August ".format(guess))
elif guess == 9:
    print("{} Represents September ".format(guess))
elif guess == 10:
    print("{} Represents October ".format(guess))
elif guess == 11:
    print("{} Represents November ".format(guess))
elif guess == 12:
    print("{} Represents December ".format(guess))
else:
    print("Error. {} that does not represent a month".format(guess))
