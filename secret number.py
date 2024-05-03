condition = True
while(condition):
    n= input()
    if(n==25):
        print("congratulations you guessed it right")
        condition=False
    elif(n> 25):
        print("number is too large")
    elif(n<25 and n>0):
        print("number is too small")
    elif(n==0 or n<=0):
        print('the user want to quits')
