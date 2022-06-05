numero1 = 25
numero2 = 24
suma = numero1 + numero2

print("La suma de", numero1, "y", numero2, "es:", suma)
print(f"La suma de {numero1} y {numero2} es: {suma}")
print("La suma de {} más {} es: {}".format(numero1, numero2, suma))


lista=[2000, 500, 17000, 24, 7]
for elemento in lista:
    print(f"{elemento:10}")
print(f"""
----------   
{sum(lista):10.3f}
""")