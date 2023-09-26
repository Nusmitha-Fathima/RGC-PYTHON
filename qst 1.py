x = input("enter the month:")
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]
if x in winter:
    print("The season is winter")
elif x in spring:
    print("The season is spring")
elif x in summer:
    print("The season is summer")
else:
    print("The season is Autumn")