personas = [
    ["Ana", 21, 100],
    ["Baelor", 18, 67],
    ["Cristiano", 20, 88],
    ["Dante", 17, 90],
]
#Registro de notas, nombres y edad.
personas.append(["Estolas", 20, 54])
while True:
        nombre = input("Nombre: ").strip()
        if nombre != "":
            break
        print("El nombre no puede estar vacio")
while True:
    try:
        edad = int(input("Edad: "))
        if 1<=edad<=100:
            break
        print("Edad fuera de rango.")
    except ValueError:
        print("Ingrese un numero entero valido.")

while True:
    try:
        nota = float(input("Nota: "))
        if 1<=nota<=100:
            break
        print("Nota fuera de rango.")
    except ValueError:
        print("Ingrese un numero valido.")
#Para mostar
personas.append([nombre, edad, nota])
print("="*13)
for persona in personas:
    print(f"Nombre: {persona[0]:10} | Edad: {persona[1]} | Nota: {persona[2]}")


# Actualizacion
while True:
    try:
        i = int(input("Indice a actualizar: "))
        if 0 <= i < len(personas): 
            break
        print("ese indice no extiste")
    except ValueError:
        print("Ingrese un numero entero valido")


while True:
    try:
        nueva_nota = float(input("Nueva Nota: "))
        if 1<=nueva_nota<=100:
            break
        print("Nota fuera de rango.")
    except ValueError:
        print("Ingrese un numero valido.")

personas[i][2] = nueva_nota
for persona in personas:
    print(f"Nombre: {persona[0]:10} | Edad: {persona[1]} | Nota: {persona[2]} ")

#Eliminacion

while True: 
    try:
        i = int(input("Indice a eliminar: "))
        if 0 <= i < len(personas):
            break
        print("Ese indice no existe.")
    except ValueError:
        print("Ingrese un numero entero valido.") 

#Datos puntuales
print("="*13)
print(personas[0][0])
print(personas[3][0])

print("="*13)
eliminado = personas.pop(i)
print(f"Se Elimino a  {eliminado[0]}")
print("="*13)
for persona in personas:
    print(f"Nombre: {persona[0]:10} | Edad: {persona[1]} | Nota: {persona[2]}")