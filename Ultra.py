

nivel1 = int(input("Introduce quantos personajes de nivel 1 tienes: "))
nivel2 = int(input("Introduce quantos personajes de nivel 2 tienes: "))
nivel3 = int(input("Introduce quantos personajes de nivel 3 tienes: "))

personajes2 = nivel2 * 10
personajes3 = nivel3 * 100

total = nivel1+personajes2+personajes3

print(f"En total tienes {total} persoanjes")

if total <= 1000:
    respuesta = 1000-total
    print(f"Te quedan un total de {respuesta} personajes para el ultra")

else:
    respuesta = total-1000
    print(f"Ya tienes el ultra y te sobran un total de {respuesta} personajes")