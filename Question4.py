def dou():
str=input("Enter the string")
a=""
l=len(str)
for i in range(0,l):
    a=a+(str[i]*2)
print("The required string is",a)