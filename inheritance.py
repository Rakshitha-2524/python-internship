class GF:
    def __init__(self, surname):
        self.surname= surname
        
class Father(GF):
    def __init__(self, name, surname):
        self.name = name
        super().__init__(surname)
my_father = Father("father_name", "KS")
print(my_father.surname)


