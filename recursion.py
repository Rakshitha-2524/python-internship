count=1
def rec_func(num,count):
    if(count<11):
        print(num,"x",count,"=",num*count)
        rec_func(num,count+1)
     
num=int(input())
rec_func(num,count) 
