from random import randint as rdm

class Addition:       #a + b = c  
    
    condition = "ADDITION_ENABLE" 

    def __init__(self,rule):
        a_min = rule["ADDITION_a_min"]
        a_max = rule["ADDITION_a_max"]
        b_min = rule["ADDITION_b_min"]
        b_max = rule["ADDITION_b_max"]
        equa  = rule["ADDITION_equa"]
        
        a = rdm(a_min,a_max) 
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