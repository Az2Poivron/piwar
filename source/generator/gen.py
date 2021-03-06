import json
from random import randint as rdm , choice
from source.generator.addition import Addition 
from source.generator.substraction import Substraction
from source.generator.multiplication import Multiplication
from source.generator.division import Division
from source.generator.euclide import Euclide



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
