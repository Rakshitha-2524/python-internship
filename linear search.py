list = [3,8,10,12,1,9]
find_num = int(input())
found_num = False
for each_num in list:
    if(each_num ==find_num):
        found_num = True
        break
if(found_num == True):
    print("number is found")
else:
    print("number is not found")