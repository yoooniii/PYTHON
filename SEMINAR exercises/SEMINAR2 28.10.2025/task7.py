#zad7

uspeh=float(input("Въведете успех:"))
stipendiq=float(input("Въведете максимална стипендия в университета:"))
if uspeh>=5.50:
    print(f"Студентът получава стипендия {stipendiq}лв")
if uspeh>=5.00 and uspeh<5.50:
    print(f"Студентът получава стипендия {stipendiq*0.7}лв")
if uspeh>=4.50 and uspeh<5.00:
    print(f"Студентът получава стипендия {stipendiq*0.5}лв")
if uspeh<4.50:
    print(f"Студентът не получава стипендия")
  