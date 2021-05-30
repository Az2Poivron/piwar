from os import system
from source.generator.gen import gen_list_operation
from time import sleep as slp
system("clear")

print('Here is a test')
slp(1)

level = "1-0"
L = gen_list_operation(level)

for operation in L:
    print(operation.str)

