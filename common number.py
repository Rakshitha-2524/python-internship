list_1=[]
list_2=[]

for i in range(5):
    num=int(input())
    list_1=list_1+[num]
print(list_1)

for i in range(5):
    num=int(input())
    list_2=list_2+[num]
print(list_2)

common_number=0
for i in list_1:
    
    for each_number in list_2:
        if(i== each_number):
            common_number=common_number+1
print(common_number)