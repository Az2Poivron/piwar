from random import randint as rdm

class Addition: #a + b = c
    
    def __init__(self,b_min,b_max,equa=False):
        a = rdm(b_min,b_max) 
        b = rdm(b_min,b_max) 
        c = a + b

        L = [a,b,c]

        if equa:
            a_index = rdm(0,2)
        else:
            a_index = 2

        self.answer = L[a_index]
        L[a_index] = "?"

        self.str = f"{L[0]} + {L[1]} = {L[2]}"