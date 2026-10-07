# Taking the angel of entering from device 
angle_of_entering = float(input("Enter current angle of the spacecraft: "))
# Taking the minimum safety angle of entering 
min_angle = float(input("Enter minimum safety entering angle of spacecraft: "))
# Taking the maximum safety angle of entering 
max_angle = float(input("Enter maximum safety entering angle of spacecraft: "))

# Applying conditions for displaying messages
if angle_of_entering > max_angle:
    print("Spacecraft will burn like meteor")
elif angle_of_entering < min_angle:
    print("Spacecraft will bounce back in space")
else:
    print("All right. You can enter in the earth atmosphere")
