import json
from random import randint as rdm , choice
from addition import Addition 
from substraction import Substraction
from multiplication import Multiplication
from division import Division
from euclide import Euclide



def extract_rule(name): #return rules from a name file
    f = open(f"source/level/{name}.json")
    rule = json.load(f)
    return(rule)

def gen_list_operation(name): #return list of Operation from a name file
    rule = extract_rule(name)
    L_constructor = [Addition , Substraction , Multiplication , Division , Euclide]
    L_enable = [c for c in L_constructor if rule[c.condition]]
    L_operation = [choice(L_enable)(rule) for _ in range(rule["ENNEMY_NUMBER"])]
    return(L_operation)


L = gen_list_operation("0")
for line in L:
    print(line.str)