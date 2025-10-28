#zad4

s=0
for y in range(1,50):
    if (y%2==0 or y%3==0) and y%6==0:
            s+=y
print(s)
