import string
a = string.ascii_uppercase
def shifr():

    print("Enter messgage")
    s = input().strip().upper()
    print("Enter duraction")
    d = int(input())
    out = ""
    for i in s:
        out += a[(a.index(i)+d) % len(a)]
    print(out)
    start()

def rashifr():
    print("Enter shifr")
    s = input().strip().upper()
    print("Enter duraction")
    d = int(input())
    out= ""
    for i in s:
        out += a[(a.index(i)-d + len(a) )%len(a)]
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