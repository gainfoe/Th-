from random import *

lword = ["champion", "love", "heart", "hexagon", "cute"]
end = 5
while end != 0:
    char = []
    so_ngau_nhien = randint(0, len(lword) - 1)
    word = lword[so_ngau_nhien]
    lword.pop(so_ngau_nhien)
    wlist = []
    do_dai = len(word)
    end = end - 1

    for i in range(do_dai):
        a = word[i]
        wlist.append(a)
    for j in range(do_dai):
        so_thu_tu = randint(0, len(wlist) - 1)
        chu = wlist[so_thu_tu]
        char.append(chu)
        wlist.pop(so_thu_tu)

    print(*char, sep=" ")

    while True:
        doan = input("Nhap tu: ")
        if doan.lower() == word:
            print("Chinh Xac")
            break
        print("Khong Chinh Xac")

    if end != 0:
        while True:
            action = input("Next / Stop: ")
            if action.lower() == "next":
                print("Cau tiep theo:")
                break
            elif action.lower() == "stop":
                end = 0
                print("Tro choi ket thuc")
                break
            else:
                print("Loi cu phap")
    else:
        print("Ban da chien thang")












