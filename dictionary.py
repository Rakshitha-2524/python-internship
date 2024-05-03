str_1 = input()
dict={}
for i in str_1:
    if(dict.get(i)==None):
        dict[i] = 1 
    else:
        dict[i] = dict[i]+1 
    
print(dict)
for key, value in dict.items():
    print(key+ ' : ' + str(value))