#zad10

budget=float(input("Въведете бюджет: "))
season=input("Въведете сезон (summer/winter): ").lower()

destination = ""
place = ""
spent = 0

if budget<=100:
    destination="Bulgaria"
    if season=="summer": 
        spent=budget*0.3
        place="Camp"
    else: 
        spent=budget*0.7
        place="Hotel"
elif budget>100 and budget<=1000:
    destination="Balkans"
    if season=="summer": 
        spent=budget*0.4
        place="Camp"
    else: 
        spent=budget*0.8
        place="Hotel"
else:
    destination="Europe"
    spent=budget*0.9
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {spent:.2f}")