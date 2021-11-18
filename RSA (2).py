import random, math



E = []
D = []
d=0


prime1 = True
prime2 =True
while prime1:
    k=2
    q=random.randint(1,1000)
    if q > 1:
        for i in range(2, int(q/2)+1):
            if (q%i)==0:
                break
        else:
            prime1=False
    else:
        pass

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

print(p,q)
#     if q % 2==1 and p % 2==1:
#
#
#     else:
#         if p %2 ==0:
#
#             q = random.randint(1, 10000)
#         else:
#             p= random.randint(1,10000)


n = p * q
fi = (p - 1) * (q - 1)


for a in range(2, fi):
    if math.gcd(a, fi) == 1:
        E.append(a)

e = E[0]

print("e - "+ str(e))




def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
D = gcd_extended(e, fi)


d=D[1]
if d<0:
    d=d %fi
print("d - " +str(d))


publicKey = (n, e)
privateKey = (n, d)

m = int(input(f"Enter number lower than {fi} => "))

zakodtext = (m ** publicKey[1])%publicKey[0]
print(f'Coder - {zakodtext}')

iznachtext = (zakodtext ** privateKey[1])%privateKey[0]
print(f'Message - {iznachtext}')

print("PODPIS")
S=(m**d)%n
if (S** e) %n == m:
    print("YEah")