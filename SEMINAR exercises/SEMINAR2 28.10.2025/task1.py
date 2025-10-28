#zad1

m=int(input("Въведете m: "))
n=int(input("Въведете n: "))
p=1
for x in range (m,n+1):
   if x%3==0 and x%4==0: 
    p=p*x
print("Произведението на числата е:",p)
