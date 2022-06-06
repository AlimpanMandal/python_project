str=input("Enter the string")
l=len(str)
c=0
for i in range (0,l):
    a=str[i]
    if a in('1','2','3','4','5','6','7','8','9'):
        c=c+int(a)
print("The sum of the digits is",c)
