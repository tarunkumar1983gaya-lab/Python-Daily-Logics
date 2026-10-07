# Taking the game point from playre.
points = int(input("Enter your game points: "))
if points > 100:
 complete = ("yes")
else:
 complete = ("no")
# Calculating level and displaying message
level = 0
completed = complete
if completed == "yes":
 print("Next level")
 level = level + 1
 print(level)
else:
 print("Try again")
