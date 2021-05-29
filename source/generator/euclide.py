from random import randint as rdm

class Euclide:       #ab + r = c

    def __init__(self,a_min,a_max,b_min,b_max,equa=False): 
        a = rdm(a_min,a_max) 
        b = rdm(b_min,b_max) 
        r = rdm(0,a-1)
        c =a*b+r

        L = [a,b,r,c]

        if equa:
            a_index = rdm(0,3)
        else:
            a_index = 3

        self.answer = L[a_index]
        L[a_index] = "?"

        self.str = f"{L[0]}x{L[1]} + {L[2]} = {L[3]}"