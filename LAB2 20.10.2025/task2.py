#ЗАД 2 // да се напише програма, която въвежда n цели числа и накрая ги сумира и връща сумата
 
n=int(input("Въведете n: "))
numbers = []
print("Въведете числата:")
for i in range(n):
    num = int(input())
    numbers.append(num)
    s=sum(numbers) 
print("Сумата е", s)