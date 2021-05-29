from random import randint as rdm

class Classic:       #a ● b = c  

    def __init__(self,b_min,b_max,equa=False,otype="addition"):
        a = rdm(b_min,b_max) 
        b = rdm(b_min,b_max) 
        
        if otype == "addition":
            c = a + b
            operator = "+"
        if otype == "substraction":
            c = a - b
            operator = "-"
        if otype == "multiplication":
            c = a * b
            operator = "x"

        L = [a,b,c]

        if equa:
            a_index = rdm(0,2)
        else:
            a_index = 2

        self.answer = L[a_index]
        L[a_index] = "?"

        self.str = f"{L[0]} {operator} {L[1]} = {L[2]}"

