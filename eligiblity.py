age = int(input())
gender = input()
if(age < 18):
    print("you are not eligible to vote")
elif(age>=18 and gender == 'female'):
    print("you are eligible to vote")
    print("move to right side")
else: 
    print ("you are eligidle to vote")
    print ("move to left side")