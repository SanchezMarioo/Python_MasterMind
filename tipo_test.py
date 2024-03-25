titulo = "Bienvenido al test de cultura general"
print("\n"+titulo + "\n" + "-" * len(titulo) + "\n")
print("Pregunta 1")
puntuacion = 0

pregunta_1= input("""¿Cuál es el metal más abundante en la corteza terrestre?
    a) Hierro
    b) Aluminio
    c) Oro
    Indique su respuesta: """)
if pregunta_1 == "a" or pregunta_1 == "c":
    puntuacion+= 0
    print("Has fallado la pregunta tus puntos son: {}".format(puntuacion))
elif pregunta_1 == "b":
    puntuacion+= 10
    print("Has acertado la pregunta tus puntos son: {}".format(puntuacion))
else:
    print("Indique la respuesta correcta. Solo hay tres respuestas [a] [b] [c].")
pregunta_2 = input("""¿Cuál es la capital de Australia?
    a) Sídney
    b) Canberra
    c) Melbourne
    Indique su respuesta: """)

if pregunta_2 == "a" or pregunta_2 == "c":
    puntuacion+= 0
    print("Has fallado la pregunta tus puntos son: {}".format(puntuacion))
elif pregunta_2 == "b":
    puntuacion+= 10
    print("Has acertado la pregunta tus puntos son: {}".format(puntuacion))
else:
    print("Indique la respuesta correcta. Solo hay tres respuestas [a] [b] [c]. ")

