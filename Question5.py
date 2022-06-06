
arr=[]
for i in range (0,100):
    s=int(input("Enter the number"))
    arr.append()
for i in range (0,100):
    c=0
    st=arr[i]
    for j in range (i+1,100):
        if(st==arr[j]):
          c=c+1
    if(c>1):
     print("THe duplicate number is",st)