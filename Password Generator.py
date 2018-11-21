import random
s ="1234567890qwertyuioplkjhgfdsazxcvbnm!@#$%^&*()_+:"
Passlen =10
p = "".join(random.sample(s,Passlen))
print (p)