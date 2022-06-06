str=input("Enter the string")
l=len(str)
l1=[]
for i in range(0,l):
    l1.append(str[i])
l1.sort()
s=""
for j in range(0,l):
    s=s+l1[j]
print (s)