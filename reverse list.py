n= int(input())
list_1=[]
for i in range(1,n+1):
    list_1=list_1+[i]
print(list_1)
rev_list=[]
for i in range(n):
    rev_list=rev_list+[list_1[n-1-i]]
print(rev_list)
print(list_1.reverse())
print(list_1)
print(list_1[::-1])
