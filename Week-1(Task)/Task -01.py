x=float(input("Enter your 1st friend Cgpa: "))
y=float(input("Enter your 2nd friend Cgpa: "))
z=float(input("Enter your 3rd friend Cgpa: "))
if x<y and x<z:
     print("Your 1st friend has the lowest Cgpa",x)
elif y<x and y<z:
     print("Your 2nd friend has the lowest Cgpa",y)
else:
     print("Your 3rd friend has the lowest Cgpa:",z)
  
a=(x+y+z)/3
print("Average Cgpa :",a)