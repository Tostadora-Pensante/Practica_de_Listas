estudiantes = [
    ["Ana", 20, 85],
    ["Luis", 22, 90],
    ["Marta", 21, 78]
]

while True:
    nombre = input("Nombre: ").strip()
    if nombre != "":
        break
    print("No puede estar vacío")

while True:
    try:
        edad = int(input("Edad (1-100): "))
        if 1 <= edad <= 100:
            break
        print("Edad fuera de rango")
    except ValueError:
        print("Ingresa un número entero")

while True:
    try:
        nota = int(input("Nota (0-100): "))
        if 0 <= nota <= 100:
            break
        print("Nota fuera de rango")
    except ValueError:
        print("Ingresa un número entero")

estudiantes.append([nombre, edad, nota])

# ---------- MOSTRAR ----------
if len(estudiantes) == 0:
    print("La lista está vacía")
else:
    for i, fila in enumerate(estudiantes):
        print(i, fila)

# ---------- ACTUALIZAR (valida índice y nota) ----------
if len(estudiantes) > 0:
    while True:
        try:
            i = int(input("Índice a actualizar: "))
            if 0 <= i < len(estudiantes):
                break
            print("Ese índice no existe")
        except ValueError:
            print("Ingresa un número entero")

    while True:
        try:
            nueva = int(input("Nueva nota (0-100): "))
            if 0 <= nueva <= 100:
                break
            print("Nota fuera de rango")
        except ValueError:
            print("Ingresa un número entero")

    estudiantes[i][2] = nueva

# ---------- ELIMINAR (valida índice) ----------
if len(estudiantes) > 0:
    while True:
        try:
            i = int(input("Índice a eliminar: "))
            if 0 <= i < len(estudiantes):
                break
            print("Ese índice no existe")
        except ValueError:
            print("Ingresa un número entero")

    estudiantes.pop(i)

# ---------- RESULTADO FINAL ----------
for fila in estudiantes:
    print(fila)

    personas = [
    
    ["Kyojuro", 20, 100],
    ["Balduin", 21, 54],
    ["Leonel", 19, 67], 
    ["Robin", 19, 99],
 ]

personas.append(["Lincoln", 20, 88])
nombre = input("Nombre: ")
edad = int(input("Edad: "))
calificacion = float(input("Nota: "))
personas.append([nombre, edad, calificacion])

for persona in personas:
    print(f"Nombre: {persona[0]:<10} | Edad: {persona[1]} | Calificacion: {persona[2]}")
