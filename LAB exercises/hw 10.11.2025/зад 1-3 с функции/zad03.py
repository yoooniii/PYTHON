def calculator(o, a, b):
    if o=='+': return a+b
    elif o=='-': return a-b
    elif o=='/': return a/b
    elif o=='*': return a*b
    else:
        return "Невалидна операция"

o=input("Вид на операцията: ")
a=int(input("Въведете число: "))
b=int(input("Въведете число: "))

print("Резултатът е: ", calculator(o, a, b))
