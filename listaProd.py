"""
Cesar Ponce de la Fuente A01027756
07/10/2019
Ejercicio Listas
"""

def main():
    #Variables
    tam=12
    produccion=[0]*tam
    final=captura(produccion) #captura la lista con valores ya dados
    print()
    print("La lista es ", final)
    print()
    prom=promedio(final) #saca el promedio
    print("El promedio de tu produccion es", prom, "toneladas por mes")
    maximo(final) #maximo
    minimo(final) #minimo
    
    
def captura(laProduccion):
    cont=0
    i = 1
    for cont in range(0,len(laProduccion)):
        laProduccion[cont]=print("Dame el dato en toneladas del mes ",i," : ",end = "")
        laProduccion[cont]= int(input())
        i = i + 1
    #Fin de la captura   
    return laProduccion

def promedio(lista):
    suma=0
    for valores in lista:
        suma+=valores
    promedio=suma/len(lista)
    return promedio
    
def maximo(lista):
    lista.sort    
    max01=max(lista)
    mes=(lista.index(max01))
    mes+=1
    print('Valor maximo del ano:', max01, 'toneladas en el mes',mes)
    return
       
def minimo(lista):
    lista.sort    
    min01=min(lista)
    mes=(lista.index(min01))
    mes+=1
    print('Valor minimo del ano:', min01, 'toneladas en el mes',mes)
    return
    
main()
    