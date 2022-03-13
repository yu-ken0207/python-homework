t=[]
import random
while len(t)<6:
    r = random.randint(1,49)
    if r not in t:
        t.append(r)
print(t)
