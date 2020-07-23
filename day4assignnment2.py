# islower() , isupper()

avengers = 'WE ARE IN THE ENDGAME NOW'
# return true, All characters is uppercase in string 
print(avengers.isupper()) 

avengers = 'We Are In The Endgame Now'
# return false,if anyone in lower case 
print(avengers.isupper()) 
# return false, if anyone in upper case
print(avengers.islower()) 

# string avengers convert into lowercase
ave=avengers.lower()
# print ave
print(ave)
# return True, All character is lowercase in string
print(ave.islower()) 