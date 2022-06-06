def acc():
l1=[]
n=int(input("Enter the number of variables in the list"))
for i in range(0,n):
    x=int(input("Enter the number"))
    l1.append(x)
str=input ("Enter choice")
if (str=="asc"):
        l1.sort()
        print(l1)
if (str=="desc"):
        l1.sort(rerverse=True)
        print(l1)
if(str=="none"):
        print(l1)
