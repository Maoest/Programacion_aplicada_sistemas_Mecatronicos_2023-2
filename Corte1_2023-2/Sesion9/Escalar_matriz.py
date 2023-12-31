from random import randint as r

def crear_matriz(filas,columnas):
    matriz= []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=r(1,10)
            matriz[i].append(num)
    return matriz

def imprimir(matriz):
    for i in matriz:
        print(i)

def escalar(matriz):
    n=int(input('ingrese un escalar: '))
    for i in matriz:
        for j in range(len(i)):
            i[j]=n*i[j]
    imprimir(matriz)
    
def main():
    matriz=crear_matriz(filas,columnas)
    imprimir(matriz)
    escalar(matriz)

if __name__=="__main__":
    filas=int(input('Ingrese las filas deseadas: '))
    columnas=int(input('Ingrese las columnas deseadas: '))
    main()