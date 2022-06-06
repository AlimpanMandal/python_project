str= input ("Enter the string" )
str = str.casefold ()
rev_str = str[::-1]
if(str==rev_str):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
