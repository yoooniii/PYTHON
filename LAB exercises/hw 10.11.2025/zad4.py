numbers=input("Списък с числа: ")
lim=int(input("Лимит: "))
numlist=[int(x) for x in numbers.split()]
def replace(num,limit):
    return [0 if x>limit else x for x in num]
result=replace(numlist,lim)
print(result)