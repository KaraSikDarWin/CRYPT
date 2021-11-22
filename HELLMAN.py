import sympy
import random
prime2=True


while prime2:
    k=2
    p=random.randint(1,1000)
    if p > 1:
        for i in range(2, int(p/2)+1):
            if (p%i)==0:
                break
        else:
            prime2=False
    else:
        pass



print(p)


for i in range(2,1000):
    if(i**(p-1)%p)==1:
        if sympy.prime(i):
            g=i
            break

x = random.randint(1,1000)

y = random.randint(1,1000)
k1= (g**x) % p
k2 = (g**y) % p
if k1**y %p == k2**x % p:

    print("Ключ равен", (g**x)**y % p)
    print(p, x, y, g)
