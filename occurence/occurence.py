## Given an input string, count occurrences of all characters within a string

string=(input (" Enter a String : "))

print(string)
a={}

for i in string:
    if i in a:
        a[i] +=1
    else:
        a[i]=1
print ("Count of all characters in ",string," are : \n"+  str(a))