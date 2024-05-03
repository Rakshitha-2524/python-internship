class stack:
    def __init__(self, l):
        self.stack_list = []
        self.limit = l
    
    def push_method(self, val):
        if(len(self.stack_list) <= self.limit):
            self.stack_list.append(val)
        else:
            print("stack over flow")
    def pop_method(self):
        if(len(self.stack_list) != 0):
            self.stack_list.pop()
            
        else:
            print("stack underflow")
    def peek_method(self):
        if(len(self.stack_list) !=0):
            print(self.stack_list[-1])
        else:
            print("stack is empty")
            
            
stack_1 = stack(5)

while(True):
    print("select an option 1.push 2.pop 3.peek 4.exit")
    n= int(input("choice the option"))
    if(n==1):
        num = int(input("enter the number"))
        stack_1.push_method(num)
    elif(n==2):
        stack_1.pop_method()
    elif(n==3):
        stack_1.peek_method()
    elif(n==4):
        break
    else:
        print("invalid input")
        
    
 
                   
