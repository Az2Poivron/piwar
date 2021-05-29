from random import randint as rdm

class Division:       #a / b = c  i.e b x c = a

    def __init__(self,a_min,a_max,b_min,b_max,equa=False): #b_
        b = rdm(b_min,b_max) 
        c = rdm(a_min//b,a_max//b) 
        a = b*c

        L = [a,b,c]

        if equa:
            a_index = rdm(0,2)
        else:
            a_index = 2

        self.answer = L[a_index]
        L[a_index] = "?"

        self.str = f"{L[0]} / {L[1]} = {L[2]}"
