ans_list = []
for i in range(5):
    n = int(input())
    if(len(ans_list) == 0):
        ans_list.append(n)
    else:
        list_len = len(ans_list)
        for i in range(list_len):
            if(ans_list[i]>n):
                ans_list.insert(i,n)
                break
print(ans_list)