list = [1, 0]
print(*(list * 10))

so_nhap = int(input("Nhap so nguyen duong: "))

for i in range(1, so_nhap + 1):
    if i % 2 == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
