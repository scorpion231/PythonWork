## find th occurence frequency of the substring in a string


##Taking input from the user
x=input(" Enter a string : ")

##Converting it to the lower case
a=x.lower()

##Taking substring as input which has to be searched
y=input(" Enter the substring you want to find : ")

##converting it to lowercase
b=y.lower()

##Checking the frequency
count=a.count(b)

##Printing the result
print(count)



