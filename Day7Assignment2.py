#  sum of tuple 
list1 = [(1,2),(3,4),(5,6),(4,5)]
list2 = []

a = list1[0]
b = a[0] + a[1]
print(b)
 
for i in range(len(list1)):
     j = list1[i]
     k = j[0] + j[1]
     list2.append(k)
print(list2)
