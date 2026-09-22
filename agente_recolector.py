# Actividad 4 - Agente recolector
# Integrante: Marely
def mostrar_entorno(entorno, posicion):
    for i in range(5):
        for j in range(5):

            if i == posicion[0] and j == posicion[1]:
                print("A", end=" ")
            else:
                print(entorno[i][j], end=" ")

        print()

    print()

def percibir(entorno, posicion):

    fila = posicion[0]
    columna = posicion[1]

    percepcion = {}
    percepcion["actual"] = entorno[fila][columna]
    if fila > 0:
        percepcion["arriba"] = entorno[fila - 1][columna]
    else:
        percepcion["arriba"] = "FUERA"
    if fila < 4:
        percepcion["abajo"] = entorno[fila + 1][columna]
    else:
        percepcion["abajo"] = "FUERA"
    if columna > 0:
        percepcion["izquierda"] = entorno[fila][columna - 1]
    else:
        percepcion["izquierda"] = "FUERA"
    if columna < 4:
        percepcion["derecha"] = entorno[fila][columna + 1]
    else:
        percepcion["derecha"] = "FUERA"

    return percepcion

def decidir(percepcion):
    if percepcion["actual"] == "P":
        return "RECOGER"

    if percepcion["arriba"] == "P":
        return "ARRIBA"

    if percepcion["derecha"] == "P":
        return "DERECHA"
    if percepcion["abajo"] == "P":
        return "ABAJO"
    if percepcion["izquierda"] == "P":
        return "IZQUIERDA"


    if percepcion["arriba"] == ".":
        return "ARRIBA"

    if percepcion["derecha"] == ".":
        return "DERECHA"

    if percepcion["abajo"] == ".":
        return "ABAJO"

    if percepcion["izquierda"] == ".":
        return "IZQUIERDA"

    return "NADA"

def actuar(accion, posicion, entorno):

    fila = posicion[0]
    columna = posicion[1]

    if accion == "RECOGER":
        entorno[fila][columna] = "."
        return posicion

    if accion == "ARRIBA":
        return [fila - 1, columna]

    if accion == "ABAJO":
        return [fila + 1, columna]

    if accion == "IZQUIERDA":
        return [fila, columna - 1]

    if accion == "DERECHA":
        return [fila, columna + 1]

    return posicion

def actualizar_rendimiento(accion, puntuacion):

    if accion == "RECOGER":
        puntuacion = puntuacion + 10

    elif accion == "ARRIBA":
        puntuacion = puntuacion - 1

    elif accion == "ABAJO":
        puntuacion = puntuacion - 1

    elif accion == "IZQUIERDA":
        puntuacion = puntuacion - 1

    elif accion == "DERECHA":
        puntuacion = puntuacion - 1

    return puntuacion

def quedan_paquetes(entorno):

    for fila in entorno:
        if "P" in fila:
            return True

    return False


def ejecutar(escenario, posicion):

    entorno = []
    for fila in escenario:
        entorno.append(fila.copy())

    puntuacion = 0
    movimientos = 0
    penalizaciones = 0
    paquetes_recogidos = 0
    acciones = 0

    print("TABLERO INICIAL")
    mostrar_entorno(entorno, posicion)

    while quedan_paquetes(entorno) and acciones < 50:

        print("Accion:", acciones + 1)

        percepcion = percibir(entorno, posicion)

        print("Percepcion:", percepcion)

        accion = decidir(percepcion)

        print("Decision:", accion)

        if accion == "NADA":
            print("El agente no puede realizar otra accion.")
            break

        nueva_posicion = actuar(accion, posicion, entorno)

        if accion == "RECOGER":

            posicion = nueva_posicion
            puntuacion = actualizar_rendimiento(
                accion, puntuacion
            )

            paquetes_recogidos = paquetes_recogidos + 1

        else:

            fila = nueva_posicion[0]
            columna = nueva_posicion[1]

            if fila < 0 or fila > 4 or columna < 0 or columna > 4:

                print("No puede salir del tablero.")

                puntuacion = puntuacion - 5
                penalizaciones = penalizaciones + 1

            elif entorno[fila][columna] == "X":

                print("Hay un obstaculo.")

                puntuacion = puntuacion - 5
                penalizaciones = penalizaciones + 1

            else:

                posicion = nueva_posicion

                puntuacion = actualizar_rendimiento(
                    accion, puntuacion
                )

                movimientos = movimientos + 1

        acciones = acciones + 1

        print("Tablero:")
        mostrar_entorno(entorno, posicion)

        print("Puntuacion:", puntuacion)
        print("--------------------------")

    if not quedan_paquetes(entorno):

        puntuacion = puntuacion + 20

        print("Se recogieron todos los paquetes.")
        print("Bonificacion: +20")

    print()
    print("RESULTADO DEL ESCENARIO")
    print("Paquetes recogidos:", paquetes_recogidos)
    print("Movimientos:", movimientos)
    print("Penalizaciones:", penalizaciones)
    print("Puntuacion final:", puntuacion)
    print("Acciones:", acciones)

    return paquetes_recogidos, movimientos, penalizaciones, puntuacion


# ESCENARIO 1

escenario1 = [
    [".", ".", ".", "P", "."],
    [".", "X", ".", ".", "."],
    [".", ".", ".", "X", "P"],
    [".", ".", "P", ".", "."],
    [".", "X", ".", ".", "."]
]

posicion1 = [2, 0]
# ESCENARIO 2
escenario2 = [
    ["P", ".", "X", ".", "."],
    [".", ".", "X", ".", "P"],
    [".", ".", ".", ".", "."],
    ["X", ".", ".", ".", "."],
    ["P", ".", "X", ".", "."]
]

posicion2 = [2, 2]
# ESCENARIO 3
escenario3 = [
    [".", "X", ".", ".", "P"],
    [".", "X", ".", "X", "."],
    [".", ".", ".", ".", "."],
    ["P", "X", ".", "X", "."],
    [".", ".", ".", ".", "P"]
]
posicion3 = [2, 2]
print("____________________")
print("ESCENARIO 1")
print("____________________")

resultado1 = ejecutar(escenario1, posicion1)
print("_____________________")
print("ESCENARIO 2")
print("____________________")
resultado2 = ejecutar(escenario2, posicion2)

print("____________________=")
print("ESCENARIO 3")
print("____________________")

resultado3 = ejecutar(escenario3, posicion3)