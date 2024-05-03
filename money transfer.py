class SBI:
     branch = 7059
     def __init__(self, name, mobl_no, age):
         self.Holder_name = name
         self.mobile_no = mobl_no
         self.Age = age
         self.balance = 0
    
     def deposit(self,amt):
        self.balance = self.balance + amt
        
     def withdraw(self, amt):
        if(self.balance>=amt):
            self.balance = self.balance - amt
            return "sufficient balance"
        else:
            print("insufficient balance")
    
     def transfer(self, sender_acc, amt):
        transfer_condition = sender_acc.withdraw(amt)
        if(transfer_condition == "sufficient balance"):
            self.deposit(amt)
    
     def print_balance(self):
        print(self.balance)

brinda_acc = SBI("Brinda", "864235485", "4")
suco_acc = SBI ("Suco", "358454644", "35")
brinda_acc.deposit(25000)
suco_acc.deposit(100000)
brinda_acc.withdraw(10000)
print(brinda_acc.balance)
brinda_acc.transfer(suco_acc,25000)
print(brinda_acc.balance)
print(suco_acc.balance)
                
        
        