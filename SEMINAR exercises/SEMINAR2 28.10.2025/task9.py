#zad9

dd=int(input("Въведете koй ден е днес:"))
n=int(input("Въведете n-ти ден:"))
a=((dd+n)%7)
if a==1: print("понеделник")
elif a==2: print("вторник")
elif a==3: print("сряда")
elif a==4: print("четвъртък")
elif a==5: print("петък")
elif a==6: print("събота")
elif a==0: print("неделя")
