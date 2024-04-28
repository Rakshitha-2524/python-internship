str_1= input()
sum=0
list_1=[]
for each_char in str_1:
    if(each_char.isdigit()): 
        list_1.append(each_char)
        sum=sum+int(each_char)
        
print(list_1)
print("sum:",sum)