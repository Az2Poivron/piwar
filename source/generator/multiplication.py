from classic import Classic

class Multiplication: #a x b = c
    
    otype = "multiplication"

    def __init__(self,b_min,b_max,equa=False):
        a = Classic(b_min,b_max,equa,self.otype)
        self.str = a.str
        self.answer = a.answer
