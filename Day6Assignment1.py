list1 = [1,2,3,4,5,6,7] 
list2 = ["a","b","c","d","e"] 

len1 = min(len(list1), len(list2))
res = {list1[i]: list2[i] for i in range(len1)} 

print ("Resultant dictionary is : " + str(res))
 