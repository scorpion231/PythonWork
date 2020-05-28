## Read the users name

first=input("Enter your First Name : ")
middle=input("Enter your Middle Name : ")
last=input("Enter your last Name : ")

# Display ful name
print("Your full name : ",first," "+middle," "+last)

#Extract the first character from each string and concatanate them
initials=first[0]+middle[0]+last[0]

#display initials

print("Your initials are : ",initials)