SO = input("""¿Qué sistema operativo quieres?
    [A] Android
    [B] iOS 
    Elige una opción: """)

if SO == "A":
    dinero = input("""¿Tienes dinero?
    [A] Sí
    [B] No
    Elige una opción: """)

    if dinero == "A":
        camara = input("""¿Te importa la cámara del teléfono?
    [A] Sí
    [B] No
    Elige una opción: """)

        if camara == "A":
            print("Pues cómprate un Google Pixel")
        elif camara == "B":
            print("Pues cómprate un móvil calidad/precio")
        else:
            print("No has elegido la opción correcta")

    elif dinero == "B":
        print("Pues cómprate un móvil barato")
    else:
        print("No has elegido la opción correcta")

elif SO == "B":
    print("Pues cómprate un iPhone")
else:
    print("No has elegido la opción correcta")
if SO == "B":
    dinero = input("""¿Tienes dinero?
    [A] Sí
    [B] No
    Elige una opción: """)

    if dinero == "A":
        print("Pues comprate IPhone 15 Pro Max")
    elif dinero == "B":
        print("Comprate un Iphone de segunda mano")
    else:
        print("No has elegido la opcion correcta")
