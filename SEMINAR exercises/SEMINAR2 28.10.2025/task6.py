#zad6

figura=input()
s=1
p=0
if figura=="квадрат":
    a=int(input("Въведете страна а:"))
    s=a*a
    p=4*a
if figura=="правоъгълник":
    a=int(input("Въведете страна а:"))
    b=int(input("Въведете страна b:"))
    s=a*b
    p=2*a+2*b
if figura=="правоъгълен триъгълник":
    a=int(input("Въведете страна а:"))
    b=int(input("Въведете страна b:"))
    c=int(input("Въведете страна c:"))
    s=(a*b)/2
    p=a+b+c
print("Лицето е",s)
print("Обиколката е",p)
 
