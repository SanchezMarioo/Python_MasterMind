import os
import random

def limpiar_terminal():
    os.system('clear')

print("¡Bienvenido a la asombrosa historia!. Acerca del Laberinto de las Decisiones \n ")

print("A partir de ahora tus decisiones tendran un desenlace acerca de la historia \n")

laberinto = input("""Nuestro protagonista, Lucas, se encuentra ante dos túneles que se adentran en las profundidades de una misteriosa montaña.
Ante él se encuentran el Túnel de las Sombras (A) y el Túnel de la Luz (B). 
Lucas sabe que su elección determinará su destino.
¿Por que túnel decidiras ir?: """)

if laberinto == "A":
    limpiar_terminal()
    print("""Lucas decide aventurarse por el Túnel de las Sombras.
A medida que avanza, se encuentra con una serie de enigmas que desafían su habilidad aritmética. 
Debe resolverlos para evitar peligros y avanzar en su búsqueda.""")
    num_random = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    operacion_aritmetica=int(input("""En una bifurcación del túnel, Lucas se encuentra con una inscripción en la pared que dice
Para avanzar, resuelve la siguiente operacion: 13 * {} . 
Lucas se concentra y da siguente respuesta: """.format(num_random)))
    limpiar_terminal()
    if operacion_aritmetica == 13 * num_random :
        print("¡Felicidades has acertado la operacion aritmetica!")
        medallon= input("Al adentrarse en el camino oscuro, Lucas se encuentra con una serie de trampas ingeniosamente ocultas. A pesar de sus mejores esfuerzos, una trampa mortal lo atrapa y queda atrapado en una habitación sin salida. Mientras busca desesperadamente una salida, ve un destello proveniente de un rincón oscuro."
              " Al acercarse, descubre un medallón brillante que emite una luz tenue. Lucas se debate internamente: ¿debería tomar el medallón y arriesgarse a ser descubierto por alguna trampa oculta, o debería dejarlo y confiar en su habilidad para encontrar otra salida?"
              "Lucas decidira en ese momento coger el medallon.Tras una larga discursion con el decidira: [A] Si coger el medallon o [B] No coger el medallon \n"
              "¿Deberia coger el medallon o no?: ")
        limpiar_terminal()
    else:
        print("¡Oh no! Has fallado la operacion aritmetica, Lucas no logra avanzar y queda atrapado en el tunel de las sombras")
        input("Lucas se encuentra atrapado en el tunel de las sombras, sin poder salir de alli. ")
        limpiar_terminal()
        print("¡Fin de la historia!")
        exit()
    if medallon == "A":
        print("Lucas decide coger el medallon y se adentra en la oscuridad con el medallon en su mano. ")
        print("¡Felicidades! Has completado la historia")
        exit()
    elif medallon == "B":
        print("Lucas decide no coger el medallon y se adentra en la oscuridad sin el medallon en su mano. ")
        print("¡Oh no! Has fallado la historia")
        exit()
    else:
        print("¡Oh no! Has fallado la historia")
        exit()
elif laberinto == "B":
    limpiar_terminal()
    print("""Si Lucas opta por el Túnel de la Luz, se encontrará con un laberinto iluminado por extrañas antorchas.
Aunque no hay desafíos aritméticos, debe sortear obstáculos y trampas para avanzar hacia su objetivo.""")
    eleccion = input("""Lucas se encuentra con una bifurcación en el camino.
Encuentra un Sendero la Reflexión (A) y un Sendero de la Determinación (B). """)
    limpiar_terminal()
limpiar_terminal()
if eleccion == "A": 
    print("Lucas decide tomar el Sendero de la Reflexión.")
    linterna=input("""Mientras Lucas avanza por el Sendero de la Reflexión, la neblina se vuelve cada vez más densa y confusa. De repente, encuentra una linterna antigua con inscripciones talladas en ella. La linterna parece prometer claridad y verdad en medio de la neblina.
Al encenderla, la neblina se disipa momentáneamente, revelando un camino claro hacia adelante, pero también iluminando sombras inquietantes que sugieren peligros ocultos.
Lucas debe decidir si confía en la claridad momentánea que ofrece la linterna [A] o si sigue el llamado de la voz en la oscuridad [B]. """)
    limpiar_terminal()
    if linterna == "A":
        print("Lucas decide confiar en la linterna y sigue el camino iluminado.")
        print("¡Felicidades! Has completado la historia")
        exit()
    elif linterna == "B":
        print("Lucas decide seguir el llamado de la voz en la oscuridad.")
        print("¡Oh no! Has fallado la historia")
        exit()
    else:
        print("¡Oh no! Has fallado la historia")
        exit()
elif eleccion == "B":
    amuleto= input(""" Mientras Lucas sube por el Pasaje de la Determinación, encuentra un amuleto antiguo incrustado en una roca. 
            El amuleto parece irradiar una energía protectora y fortalecedora. Al tomarlo, Lucas siente un aumento en su determinación y resistencia, lo que le permite superar los obstáculos con mayor facilidad. 
            Sin embargo, el amuleto también parece susurrarle advertencias sobre los peligros que lo esperan más adelante.
            Lucas debe decidir si confía en el poder del amuleto para ayudarlo en su ascenso o si presta atención a sus advertencias y considera si continuar o no.""")
    limpiar_terminal()
    if amuleto == "A":
        print("Lucas decide confiar en el amuleto y continúa su ascenso.")
        print("¡Felicidades! Has completado la historia")
        exit()
    elif amuleto == "B":
        print("Lucas decide prestar atención a las advertencias del amuleto y reconsidera su decisión.")
        print("¡Oh no! Has fallado la historia")
        exit()
else:
    print("¡Oh no! Has fallado la historia")
    exit()

    