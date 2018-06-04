so_nhap = int(input("Nhap so nguyen duong: "))
list = range(so_nhap)

for i in range(1, so_nhap + 1):
    for j in range(1, so_nhap +1):
        print(j * i, end="\t")
    print("\n")