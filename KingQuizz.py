import random

usuario = input("Ingresa tu usuario: ")
print(f"¡Bienvenido a KingQuizz, {usuario}!")

categorias = ["cultura general", "deportes"]

preguntas_cultura = [
    "¿Cuál es la parte más externa del ojo humano?: ",
    "¿Cuál fue el tratado que puso fin a la Guerra de los Cien Años entre Inglaterra y Francia?: ",
    "¿Cuál de los siguientes animales mitológicos pertenece a la cultura griega?: ",
    "¿Cuál es el país más grande del mundo en términos de superficie?: ",
    "¿Qué filósofo es considerado el Padre de la lógica?: ",
    "¿Cuál es el planeta más grande del sistema solar?: ",
    "¿Quién es el autor de la novela Don Quijote de la Mancha?: ",
    "¿Cuál es el río más largo del mundo?: ",
    "¿Cuál es el país más poblado del mundo?: ",
    "¿Quién es el pintor que creó la obra La Mona Lisa?: "
]

opciones_cultura = [
    ("A. La pupila", "B. La córnea", "C. El iris", "D. La retina"),
    ("A. Tratado de Versalles", "B. Tratado de Picquingy", "C. Tratado de Troyes", "D. Tratado de Paris"),
    ("A. Escila", "B. Garuda", "C. Anzu", "D. Grifo"),
    ("A. China", "B. Canadá", "C. Estados Unidos", "D. Rusia"),
    ("A. Sócrates", "B. Platón", "C. Aristóteles", "D. Heráclito"),
    ("A. Tierra", "B. Saturno", "C. Júpiter", "D. Urano"),
    ("A. Miguel de Cervantes", "B. William Shakespeare", "C. Jane Austen", "D. Charles Dicknes"),
    ("A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"),
    ("A. China", "B. India", "C. Estados Unidos", "D. Indonesia"),
    ("A. Leonardo da Vinci", "B. Miguel Ángel", "C. Rafael", "D. Caravaggio")
]

respuestas_cultura = ["B", "B", "D", "D", "C", "C", "A", "B", "A", "A"]

preguntas_deportes = [
    "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?: ",
    "¿Cuál es el país con más Copas del Mundo ganadas?: ",
    "¿En qué deporte se utiliza la raqueta?: ",
    "¿Cuántos jugadores forman un equipo de fútbol en el terreno de juego?: ",
    "¿Cuál es el único país que ha participado en todas las ediciones de la Copa Mundial de Fútbol?: ",
    "¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos, conocido como Su Majestad del aire?: ",
    "¿En qué deporte compiten los equipos en el Super Bowl?: ",
    "¿Qué país ganó la primera Copa Mundial de Rugby en 1987?: ",
    "¿Cómo se llama el torneo de tenis que se celebra anualmente en Londres?: ",
    "¿Qué boxeador es conocido como El Más Grande y ganó el título mundial de peso pesado tres veces?: "
]

opciones_deportes = [
    ("A. 1896", "B. 1900", "C. 1924", "D. 1936"),
    ("A. Argentina", "B. Brasil", "C. Alemania", "D. Italia"),
    ("A. Tenis", "B. Fútbol", "C. Baloncesto", "D. Golf"),
    ("A. 13", "B. 12", "C. 11", "D. 10"),
    ("A. Brasil", "B. Alemania", "C. Italia", "D. Uruguay"),
    ("A. Kobe Bryant", "B. Lebron James", "C. Michael Jordan", "D. Shaquille O’Neal"),
    ("A. Rugby", "B. Baloncesto", "C. Hockey", "D. Fútbol Americano"),
    ("A. Australia", "B. Inglaterra", "C. Nueva Zelanda", "D. Sudáfrica"),
    ("A. Roland Garros", "B. Wimbledon", "C. US Open", "D. Australian Open"),
    ("A. Mike Tyson", "B. Muhammad Ali", "C. Floyd Mayweather", "D. George Foreman")
]

respuestas_deportes = ["A", "B", "A", "C", "A", "C", "D", "C", "B", "B"]

puntuacion = 0
respondidas = []
preguntadas = []

while True:

    categoria_aleatoria = random.choice(categorias)
    print(f"La categoría seleccionada es: {categoria_aleatoria}")

    if categoria_aleatoria == "cultura general":
        preguntas = preguntas_cultura
        opciones = opciones_cultura
        respuestas = respuestas_cultura
    else:
        preguntas = preguntas_deportes
        opciones = opciones_deportes
        respuestas = respuestas_deportes

    pregunta_numero = random.randint(0, len(preguntas) - 1)
    while pregunta_numero in preguntadas:
        pregunta_numero = random.randint(0, len(preguntas) - 1)
    
    preguntadas.append(pregunta_numero)

    print("-----------------------")
    print(preguntas[pregunta_numero])
    for opcion in opciones[pregunta_numero]:
        print(opcion)

    respondida = input("Elige tu respuesta (A, B, C, D): ").upper()
    respondidas.append(respondida)

    if respondida == respuestas[pregunta_numero]:
        puntuacion += 1
        print("¡CORRECTO!")
    else:
        print(f"Incorrecto. La respuesta correcta es: {respuestas[pregunta_numero]}")

    continuar = input("¿Quieres seguir jugando? (s/n): ").lower()
    if continuar != 's':
        break

print("-----------------------")
print("--------RESULTADOS--------")
print("-----------------------")

print("Respuestas correctas: ", end="")
for respuesta in respuestas:
    print(respuesta, end=" ")
print()

print("Tus respuestas: ", end="")
for respondida in respondidas:
    print(respondida, end=" ")
print()

print(f"Felicidades, {usuario}, por haber llegado hasta el final de KingQuizz")
print(f"Tu puntuación es: {puntuacion} puntos")