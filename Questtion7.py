arr=[]
n=int(input("Enter the number of elements you want to enter"))
for i in range(0, n):
    a=int(input("Enter the element"))
    arr.append(a)
max=0
ind=0
for j in  range(0, n):
  c=1
  p=arr[j]
  for k in range (j+1, n):
     if(arr[k]==p):
        c=c+1
  if(c>max):
    max=c
    ind=j
print("The element with the highest frequency is",arr[j],"and it has a frequency of",max)