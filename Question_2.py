def creditcard():
c=input("Enter your credit card number")
x=len(c)
a=x-4
str="*"*a
b=c[x-4:]
str=str+b
print("The required credit card number is ",str)
