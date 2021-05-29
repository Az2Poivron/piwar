from classic import Classic

class Substraction: #a - b = c
    
    otype = "substraction"

    def __init__(self,b_min,b_max,equa=False):
        a = Classic(b_min,b_max,equa,self.otype)
        self.str = a.str
        self.answer = a.answer
