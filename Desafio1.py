import random

alumnos,materias=[1001,1002,1003,1004],["pr1","pr2","pr3"]

def crear_matriz():
    f=len(alumnos)+1
    c=len(materias)+1
    return[[0]*c for fill in range(f)]

def encabezados(m):
    f=1
    j=0
    while f < len(materias)+1:
        m[0][f]=materias[j]
        f+=1
        j+=1
        
    f=1
    j=0
    while f < len(alumnos)+1:
        m[f][0]=alumnos[j]
        f+=1
        j+=1

def llenar_matriz (m):
    """
    pre:recibimos la matriz vacia , sin encabezados
    pos:llenamos los encabezados de la matrices ,mas los datos aleatorios 
    
    """
    encabezados(m)
    
    for i in range(len(alumnos)):
        for j in range(len(materias)):
            aux=random.randint(1,9)
            m[i+1][j+1]=aux


def mostrar_matriz(m):
    filas=len(alumnos)+1
    columnas=len(materias[0])+1
    for fil in range (filas):
        for i in range (columnas):
            print("%3s" % m[fil][i],end=" ")
        print()

def calcular_promedio_materias(m):
    columnas=len(m[0])
    filas=len(m)

    for j in range (1,columnas):
        suma=0
        materia=m[0][j]
        for i in range(1,filas):
            suma+= m[i][j]
        promedio=suma//(filas-1)
        print(f"El promedio de la materia {materia} es de {promedio} ")
    print()

def calcular_promedio_alumno(m):
    columnas=len(m[0])
    filas=len(m)

    for j in range (1,filas):
        suma=0
        alumno=m[j][0]
        for i in range(1,columnas):
            suma+= m[j][i]
        promedio=suma//(columnas-1)
        print(f"El promedio del  {alumno} es de {promedio} ")
        
matriz=crear_matriz()
llenar_matriz(matriz)
mostrar_matriz(matriz)
calcular_promedio_materias(matriz)
calcular_promedio_alumno(matriz)

for m in matriz:
    print(m)