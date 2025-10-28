#ЗАД 3 // да се въведе число n и да принтира триъгълник от звездички
 
n=int(input("Въведете n: "))
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()  

"""
2-ри начин:

n = int(input("Въведете n: "))
for i in range(1, n + 1):
    print("* " * i)"""