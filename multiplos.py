"""
Dados dos número, determinar si uno es múltiplo de otro
Karen Durán
757136 
Ingeniería Civil
Algoritmos y Programación 
ESI232B2
17/02/25
10 minutos 
"""

# Entradas
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

# Proceso
if numero_2 != 0 and numero_1 % numero_2 == 0:
    resultado = True 
else:
    resultado = False

# Salidas
if numero_2 != 0 and numero_1 % numero_2 == 0:
    print("El número", numero_1, "es múltiplo del", numero_2)
else:
    print("El número", numero_1, "no es múltiplo del", numero_2)
