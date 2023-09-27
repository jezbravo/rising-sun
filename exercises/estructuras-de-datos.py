# 1) Escribir un programa que a partir de una lista de números cuente cuántas veces aparece un número específico en la lista.
# Resolución
def contador_de_ocurrencias(lista, numero_especifico):
    contador = 0 
    for i in lista:
        if i == numero_especifico:
            contador += 1
    return contador

# Ejemplo de uso:
lista = [2, 5, 6, 5, 2, 8, 9, 2, 0]
numero_especifico = 2
cantidad = contador_de_ocurrencias(lista, numero_especifico)
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 1:
--------------------------""")
print(f"Lista de números: {lista}")
print(f"El número {numero_especifico} aparece {cantidad} veces en la lista.")

# 2) Escribir un programa que tome una lista y elimine los elementos duplicados, dejando solo los elementos únicos.
# Resolución
def eliminar_duplicados(lista):
    elementos_unicos = []
    for i in lista:
        if i not in elementos_unicos:
            elementos_unicos.append(i)
    return elementos_unicos

# Ejemplo de uso:
lista = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
lista_sin_duplicados = eliminar_duplicados(lista)
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 2:
--------------------------""")
print(f"Lista original: {lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# 3) Escribir un programa que tome una cadena de texto y cuente cuántas veces aparece cada palabra. El programa debe almacenar los resultados en un diccionario.
# Resolución
def contador_de_palabras(cadena_de_texto):
    palabras = cadena_de_texto.split()
    diccionario = {}
    for palabra in palabras:
        palabra = palabra.strip('_-/\.,¡!¿?()[]{}":;')
        palabra = palabra.lower()
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

# Ejemplo de uso:
cadena_de_texto = """
Tres Anillos para los Reyes Elfos bajo el cielo,
Siete para los Señores Enanos en palacios de piedra,
Nueve para los Hombres Mortales condenados a morir,
Uno para el Señor Oscuro, sobre el trono oscuro
en la Tierra de Mordor donde se extienden las Sombras.
Un Anillo para gobernarlos a todos. Un Anillo para encontrarlos,
un Anillo para atraerlos a todos y atarlos en las tinieblas
en la Tierra de Mordor donde se extienden las Sombras.
"""
resultados = contador_de_palabras(cadena_de_texto)
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 3:
--------------------------""")
print(f"Cadena de texto:\n {cadena_de_texto}")
for palabra, ocurrencias_de_la_palabra in resultados.items():
    print(f'La palabra "{palabra}" aparece {ocurrencias_de_la_palabra} veces.')

# 4) Escribir un programa que genere un arreglo con 30 números aleatorios. El programa debe calcular el promedio y la desviación estándar de los elementos en el arreglo.
# Resolución
import numpy as np
# Arreglo con 30 números aleatorios entre 1 y 100
arreglo = np.random.randint(1, 100, 30)
promedio = round(np.mean(arreglo),2)
desvest = round(np.std(arreglo),2)
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 4:
--------------------------""")
print("Arreglo:", arreglo)
print("Promedio:", promedio)
print("Desviación Estándar:", desvest)

# 5) Escribir un programa que a partir de un arreglo de números, encuentre los índices de los 2 valores mínimos del arreglo.
# Resolución
import numpy as np
def indices_minimos(arreglo_2):
    if len(arreglo_2) < 2:
        raise ValueError("El arreglo debe contener al menos dos elementos.")
    indices_ordenados = np.argsort(arreglo_2)
    indice_minimo_1, indice_minimo_2 = indices_ordenados[:2]
    return indice_minimo_1, indice_minimo_2

# Ejemplo de uso:
arreglo_2 = np.array([6, 8, 9, 1, 2, 3, 7, 5, 4])
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 5:
--------------------------""")
print("Arreglo:", arreglo_2)
try:
    indice_minimo_1, indice_minimo_2 = indices_minimos(arreglo_2)
    print(f"El primer valor mínimo está en el índice: {indice_minimo_1}")
    print(f"El segundo valor mínimo está en el índice: {indice_minimo_2}")
except ValueError as e:
    print(e)

# 6) Clase Pila: Crear una clase Pila con atributos de tamaño y elementos. Implementar métodos para añadir, remover y consultar elementos en el tope de la pila. Escribir un programa que utilice la pila para invertir el orden de una serie de números ingresados por el usuario.
# Resolución
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 6:
--------------------------""")
class Pila:
    def __init__(self):
        self.tamaño = 0
        self.elementos = []

    def vacia(self):
        return self.tamaño == 0

    def añadir(self, elemento):
        self.elementos.append(elemento)
        self.tamaño += 1

    def remover(self):
        if not self.vacia():
            elemento = self.elementos.pop()
            self.tamaño -= 1
            return elemento
        else:
            raise IndexError("La pila está vacía")

    def consultar(self):
        if not self.vacia():
            return self.elementos[-1]
        else:
            raise IndexError("La pila está vacía")

# Función para invertir una serie de números utilizando la pila
def invertir_numeros():
    pila = Pila()
    while True:
        numero = input('Ingrese un número y luego presione ENTER. Presione la tecla "f" para finalizar. ')
        if numero.lower() == 'f':
            break
        pila.añadir(numero)

    # Imprimir los números en orden inverso
    print("Números en orden inverso: ")
    while not pila.vacia():
        print(pila.remover())
invertir_numeros()

# 7) Clase Cuenta Bancaria: Crear una clase CuentaBancaria con atributos de saldo y número de cuenta. Implementar métodos para depositar, retirar dinero, y mostrar el saldo final.
# Resolución
print("""
--------------------------
RESOLUCIÓN DEL PROBLEMA 7:
--------------------------""")
class CuentaBancaria:
    def __init__(self, numero_de_cuenta, saldo_inicial=0):
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"NUEVA OPERACIÓN: DEPÓSITO. Depósito de ${cantidad} realizado con éxito. Su nuevo saldo es de: ${self.saldo}"
        else:
            return "El monto del depósito debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"NUEVA OPERACIÓN: EXTRACCIÓN. Retiro de ${cantidad} realizado con éxito. Su nuevo saldo es de: ${self.saldo}"
        elif cantidad > self.saldo:
            return f"NUEVA OPERACIÓN: EXTRACCIÓN. Monto a retirar: ${cantidad}. Saldo insuficiente para realizar la transacción. Su saldo actual es de: ${self.saldo}"
        else:
            return "El monto de la extracción debe ser mayor que cero."

    def mostrar_saldo(self):
        return f"NUEVA OPERACIÓN: CONSULTA. Saldo actual en la cuenta {self.numero_de_cuenta}: ${self.saldo}"

# Ejemplo de uso:
cuenta = CuentaBancaria("EZE123", 1000)

print(cuenta.mostrar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(3000))
print(cuenta.mostrar_saldo())
