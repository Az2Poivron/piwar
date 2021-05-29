from classic import Classic

class Substraction: #a x b = c
    
    otype = "substraction"

    def __init__(self,b_min,b_max,equa=False):
        a = Classic(b_min,b_max,equa,self.otype)
        self.str = a.str
        self.answer = a.answer

a = Substraction(10,80)
print(a.str , a.answer)