def laberinto(dimension, obstaculos):
    ''' Función que construye un laberinto cuadrado de una dimensión dada poniendo.

    Parámetros requeridos:
        - dimension: cantidad de columnas y filas usaremos un unico valor que siempregenerara una matriz cuadrada
        - obstaculos: Es una lista de tuplas con posiciones donde hay obstaculos.


    Salida: 
        Una matriz que representa el laberinto. 
    '''
    '''
    def laberinto(dimension, obstaculos):
    laberinto = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    
    return laberinto

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(''.join(fila))

def obtener_posicion_ceros(laberinto):
    ceros = []
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == '0':
                ceros.append((i, j))
    return ceros

def imprimir_vecinos(laberinto, posicion_cero):
    i, j = posicion_cero
    dimension = len(laberinto)
    vecinos = []

    # Comprobar vecino arriba
    if i > 0:
        vecinos.append(laberinto[i - 1][j])

    # Comprobar vecino abajo
    if i < dimension - 1:
        vecinos.append(laberinto[i + 1][j])

    # Comprobar vecino izquierda
    if j > 0:
        vecinos.append(laberinto[i][j - 1])

    # Comprobar vecino derecha
    if j < dimension - 1:
        vecinos.append(laberinto[i][j + 1])

    print(f'Posición ({i}, {j}):', laberinto[i][j])
    print('Vecinos:', vecinos)

obstaculo = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
dimension = 5
lab = laberinto(dimension, obstaculo)
imprimir_laberinto(lab)
ceros = obtener_posicion_ceros(lab)

for cero in ceros:
    imprimir_vecinos(lab, cero)
    
    '''

    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle  para añadir las filas del laberinto.
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle  para recorrer las columnas del laberinto.
        for j in range(dimension):
            # Comprobar si la tupla está en el la lista de obstaculos.
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    return laberinto
def recorre_laberinto(laberinto):
    
    n = len(laberinto)
    fila = columna = 0
    
    movimientos = ['Abajo']
    while (fila < n-1 and columna < n-1):
        if movimientos [-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        elif movimientos[-1] != 'Abajo'  and fila - 1 > 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        elif movimientos[-1] != 'Izquierda'  and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        elif movimientos[-1] != 'Derecha'  and columna - 1 > 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')  
        else:
            movimientos.append('No hay salida')
            break
    return movimientos

# Tupla de posisiones de las celdas con obstaculos en el laberinto
obstaculo = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
# Tamaño de la matriz
dimension = 5
# llamada a la funcion una vez establecidos los valores de obstaculos
lab = laberinto(dimension, obstaculo)   

# Imprimnir el laberinto
# SOLO COMO EJEMPLO
for i in lab:
    print(''.join(i))
    
    
    resultado = recorre_laberinto(lab)
print("Resultado")
for movimiento in resultado:
    print(movimiento)

    
    
# Esperamos al usuario
input("presione enter para salir")