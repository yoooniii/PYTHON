
# Преобразуване на минути в дни, часове и минути

mins = int(input("\nВъведете минути: "))
days = mins // 1440             # 1 ден = 1440 минути
hours = (mins % 1440) // 60
minutes = mins % 60
print(f"{days} дни, {hours} часа, {minutes} минути")
