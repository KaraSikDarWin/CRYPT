import string
a = string.ascii_uppercase
def shifr():
    print("Enter text")
    s = input().strip()
    print("Enter decoding key")
    key = input()
    l = []
    g = []
    k = 0
    out = ""
    print(s)
    for i in s:
        l.append(a.find(i) % len(a))
#    print(l)

    for i in key:
        g.append(a.find(i) % len(a))
#    print(g)

    for i, values in enumerate(s):
        if k > len(key) - 1:
            k = 0
        out += a[(l[i] + g[k]) % len(a)]
        k += 1
    print(out)
    start()


def rashifr():
    a = string.ascii_uppercase
    print("Enter shifr")
    s = input()
    print("Enter decoding key")


    print(s)
    key = input()
    l = []
    g = []
    k = 0
    out = ""
    for i in key:
        g.append(a.find(i) % len(a))

    for i in s:
        l.append(a.find(i) % len(a))
    #   print(l)
    for i, values in enumerate(s):
        if k > len(key) - 1:
            k = 0
        out += a[(l[i] - g[k]+len(a)) % len(a)]
        k += 1
    print(out)
    start()

def start():
    print("Ку) \n Что делать будем?? \n Если кодировать, то отправь 1 \n Если раскодировать, то отправь 2 \n а если хочешь коровку, то 3")
    answer = input()
    if answer=="1":
        shifr()
    elif answer == "2":

        rashifr()
    elif answer=="3":
        print("Я обманул коровки нету:(")
    else:
        print("Ты что то напутал. Давай еще раз!")
        start()

start()
