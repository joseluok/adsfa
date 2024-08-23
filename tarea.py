nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    estado = "adulto"
elif edad <= 10:
    estado = "niño"
else:
    estado = "adolescente"

print("Hola, " + nombre + "!")
print("Usted tiene " + str(edad) + " años.")
print("Usted es " + estado + ".")