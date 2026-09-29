personas = [
    ["Alfa", 20, 100],
    ["Baelor", 20, 88],
    ["Cardin", 20, 67],
    ["Dora", 20, 87],
]

personas.append(["Ulysses", 32, 99])
nombre = input("Nombre: ")
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
        notas = float(input("Nota: "))
        if 0<= notas <= 100:
            break
        print("Nota no valida")
    except ValueError:
        print("Ingrese un numero valido.")


personas.append([nombre,edad,notas])
print("="*13)
for persona in personas:
    print(f"Nombre: {persona[0]:10} | Edad: {persona[1]} | Nota: {persona[2]}")