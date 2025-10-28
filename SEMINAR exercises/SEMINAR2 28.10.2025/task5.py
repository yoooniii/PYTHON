#zad5

n=int(input("Въведете n: "))
min=float()
max=float()
for y in range(n):
    m=float(input("Въведете число: "))
    if m<min:
        min=m
    if m>max:
        max=m
print("min:",min)
print("max:",max)
