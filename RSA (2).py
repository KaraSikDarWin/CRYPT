import random, math
E = []
D = []
d=0
p = 13
q = 17
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
print("d - " +str(d))


publicKey = (n, e)
privateKey = (n, d)

m = int(input(f"Enter number lower than {fi} => "))

zakodtext = (m ** publicKey[1])%publicKey[0]
print(f'Coder - {zakodtext}')

iznachtext = (zakodtext ** privateKey[1])%privateKey[0]
print(f'Message - {iznachtext}')