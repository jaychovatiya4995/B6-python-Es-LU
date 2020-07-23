# Find all occurrence of substring in given string
import re
test_str = "what we think we become; we are python programmer"
  
# get substring 
test_sub = input("Enter a substring : ")
  
# printing original string  
print("The original string is : " + test_str) 
  
# printing substring  
print("The substring to find : " + test_sub) 
  
# using re.finditer() 
# All occurrences of substring in string  
res = [i.start() for i in re.finditer(test_sub, test_str)] 
  
# printing result  
print("The start indices of the substrings are : " + str(res)) 
  