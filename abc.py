"""
Cesar Ponce de la Fuente A01027756
16/10/2019
Listas de dos datos con distintos tipos de dato
"""
#Variables
def main():
    matriz=0
    matriz=[["a",0],["b",0],["c",0],["d",0],["e",0],["f",0],["g",0],["h",0],["i",0],["j",0],["k",0],["l",0],["m",0],["n",0],["o",0],["p",0],["q",0],["r",0],["s",0],["t",0],["u",0],["v",0],["w",0],["x",0],["y",0],["z",0]]
    texto=imprimir()
    lista=abc(matriz,texto)
    print("en tu texto hay: ")
    bonito(lista)
    
def imprimir():
    text=input("Dime el texto al cual le contare las letras dentro de el: ")
    return text

def abc(matriz,texto):
    letra=0
    texto=texto.lower()
    texto=texto.replace(" ","")
    nuevaMatriz=[]
    
    for letra in texto:
        for cont in range(0,len(matriz),1):
            if (letra==matriz[cont][0]):
                matriz[cont][1]+=1
                break
    for cont in range(0,len(matriz),1):
        if matriz[cont][1]>0:
            nuevaMatriz+=[matriz[cont]]
    return nuevaMatriz
            
def bonito(lista):
    x=0
    y=0
    for y in range (len(lista)):
        for x in range (len(lista[y])):
            print (lista [y][x], end= " ")
        print()
  
    
main()