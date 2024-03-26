
dolar_a_euro = 0.92
libra_a_euro = 1.17
euro_a_dolar = 1.08
euro_a_libra = 0.86

opcion = input("""¿Que opcion quiere escoger:
       [A] Dolar a Euro
       [B] Euro a Dolar
       [C] Libra a Euro
       [D] Euro a Libra
       Indique su opcion: """)
texto = "Introduzca la cantidad de {} a convertir: "

if opcion == "A":
    conversion = float(input(texto.format("dolares")))
    print("La conversion de dolares {}$ a euro es {}".format(conversion, (dolar_a_euro * conversion)))
elif opcion == "B":
    conversion = float(input(texto.format("euros")))
    print("La conversion de euros {}€ a dolares {} ".format(conversion,(euro_a_dolar * conversion)))
elif opcion == "C":
    conversion = float(input(texto.format("libras")))
    print("La conversion de libras {} £ a euros {} €".format(conversion,(libra_a_euro*conversion)))
elif opcion == "D":
    conversion = float(input(texto.format("euros")))
    print("La conversion de euros {} € a libras {} £. ".format(conversion,(euro_a_libra*conversion)))
else:
    print("No has elegido ninguna opcion valida")
    exit(1)