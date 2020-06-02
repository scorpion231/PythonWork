hours=int(input("Please Enter no. of hours you have worked in a week (HOURS): "))
if hours<=40:
    c=hours*12
if hours>40:
    c=40*12+(hours-40)*1.5*12

if c<=300:
    tax=c*0.15
elif c>300 and c<=450:
    tax=300*0.15+(c-300)*0.20
else:
    tax=300*0.15+150*0.20+(c-450)*0.25
net=c-tax
print("Your gross salary after tax deduction is : ",net,"$")
