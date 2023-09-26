from nodo_cantaro import NodoCantaro


def buscar_solucion(estado_inicial, estado_objetivo):
    nodo_inicial = NodoCantaro(estado_inicial, "Estado Inicial")
    frontera = [nodo_inicial]
    visitados = set()

    while frontera:
        nodo_actual = frontera.pop()

        if nodo_actual.estado == estado_objetivo:
            solucion = []
            while nodo_actual:
                solucion.append((nodo_actual.operacion, nodo_actual.estado))
                nodo_actual = nodo_actual.padre
            solucion.reverse()
            return solucion

        visitados.add(nodo_actual.estado)

        for operacion, nuevo_estado, _ in generar_operaciones(nodo_actual.estado):
            if nuevo_estado not in visitados:
                hijo = NodoCantaro(nuevo_estado, operacion, nodo_actual)
                nodo_actual.agregar_hijo(hijo)
                frontera.append(hijo)

    return None


def generar_operaciones(estado):
    c4, c3 = estado
    operaciones = [
        ("Llenar 4 litros", (4, c3)),
        ("Llenar 3 litros", (c4, 3)),
        ("Vaciar 4 litros", (0, c3)),
        ("Vaciar 3 litros", (c4, 0)),
        ("Pasar de 4 a 3 litros", (c4 - min(c4, 3 - c3), c3 + min(c4, 3 - c3))),
        ("Pasar de 3 a 4 litros", (c4 + min(c3, 4 - c4), c3 - min(c3, 4 - c4)))
    ]
    return [(operacion, nuevo_estado, estado) for operacion, nuevo_estado in operaciones]


estado_inicial = (0, 0)

c4_objetivo = int(input(
    "Ingrese el estado objetivo para el cantaro de 4 litros (0-4): "))
c3_objetivo = int(input(
    "Ingrese el estado objetivo para el cantaro de 3 litros (0-3): "))
estado_objetivo = (c4_objetivo, c3_objetivo)

solucion = buscar_solucion(estado_inicial, estado_objetivo)

if solucion:
    print("Recorrido del árbol:")
    for paso, (operacion, estado) in enumerate(solucion):
        print(f"Paso {paso + 1}: {operacion} => Estado: {estado}")
else:
    print("No se encontró solución.")
