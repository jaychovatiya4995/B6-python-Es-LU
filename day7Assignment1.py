dict1 = {21:"FTP",22:"SSH",23:"telnt",80:"http"}
# print(dict1)
dict2 = {}
for k,v in dict1.items():
        # print(v,k)
        dict2[v] = k

print(dict2) 