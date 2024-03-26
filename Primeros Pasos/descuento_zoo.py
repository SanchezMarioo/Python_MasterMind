edad = int(input("¿Cuál es tu edad? "))
carnet = input("¿Qué carnet tienes? Estudiante [E] Pensionista [P] Familia Numerosa [F] Nada [N]: ")

if (25 <= edad <= 35 and carnet == "E") or edad < 10 or (edad > 65 and carnet == "P") or carnet == "F":
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento.")
