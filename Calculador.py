
print()
print("Estas son las diferentes opciones del menú:")
print()
print("1 - Calcular Winrate")
print("2 - Calcular las veces que has estado entre los 3 mejores respecto al total de partidas jugadas")
print("3 - Calcular promedio de kills por partida")
print("4 - Calcular promedio de gemas conseguidas por partida")
print()

opcion = int(input("Para seleccionar una opción del menú escribe el número correspondiente aquí --> "))

if opcion == 1:
    wins = int(input("Escribe el total de victorias conseguidas: "))
    total = int(input("Escribe el total de partidas totales jugadas: "))
    resultado = wins / total
    porcentaje = resultado * 100
    print(f"Tienes un winrate de {porcentaje:.3f}%")

elif opcion == 2:
    wins = int(input("Escribe el total top 3 conseguidos: "))
    total = int(input("Escribe el total de partidas totales jugadas: "))
    resultado = wins / total
    porcentaje = resultado * 100
    print(f"Tienes un porcentaje de top 3 o mas de {porcentaje:.3f}%.")

elif opcion == 3:
    kills = int(input("Escribe el total de gemas conseguidas: "))
    total = int(input("Escribe el total de partidas totales jugadas: "))
    resultado = kills / total
    print(f"Tienes una media de {resultado:.1f} gemas por partida.")

elif opcion == 4:
    gemas = int(input("Escribe el total de kills conseguidas: "))
    total = int(input("Escribe el total de partidas totales jugadas: "))
    resultado = gemas / total
    print(f"Tienes una media de {resultado:.1f} kills por partida.")

