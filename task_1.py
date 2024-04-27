n = int(input())
if(n%2 != 0):
    print("Weird")
elif((n%2 == 0) and (n>1 and n<6) ):
    print("not wired")
elif((n%2 == 0)  and (n>5 and n<21)):
    print("wired")
elif(n%2 == 0 and n>20):
    print("not wired")    