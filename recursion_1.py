n=int(input())
def func(n):
    if(n>1):
        return func(n-1) + '+' '1/'+str(n) 
    elif(n==1):
        return '1' + func(n-1)
     
    return ''
ans = func(n)
print(ans)