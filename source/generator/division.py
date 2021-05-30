from random import randint as rdm

class Division:       #a / b = c  i.e b x c = a

    condition = "DIVISION_ENABLE" 
    
    def __init__(self,rule):
        b_min = rule["DIVISION_b_min"]
        b_max = rule["DIVISION_b_max"]
        c_min = rule["DIVISION_c_min"]
        c_max = rule["DIVISION_c_max"]
        equa  = rule["DIVISION_equa"]
        
        b = rdm(b_min,b_max) 
        c = rdm(c_min,c_max) 
        a = b*c

        L = [a,b,c]

        if equa:
            a_index = rdm(0,2)
        else:
            a_index = 2

        self.answer = L[a_index]
        L[a_index] = "?"

        self.str = f"{L[0]} / {L[1]} = {L[2]}"
