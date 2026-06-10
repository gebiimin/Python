import random

s = "0123456789" 
passlen = 4 

p = "".join(random.sample(s, passlen ))
print(p)