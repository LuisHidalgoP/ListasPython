from Listas import Metodos
Listas=[]
Listas2=[]
_tam=int(input("Ingrese el tamano de la Lista: "))
c=Metodos()
c.ingreso(Listas,_tam)
c.impresion(Listas,_tam)
itm=int(input("Ingrese el el ultimo elemento que desea agregar: "))
c.agregarUltimo(Listas,itm)
c.impresion(Listas,len(Listas))
print("Ahora ingrese una segunda lista pra unir con la anterior: ")
c.ingreso(Listas2,_tam)
c.unirListas(Listas,Listas2)
c.impresion(Listas,len(Listas))
_elemento=int(input("Ingrese el elemento que desea contar: "))
_cantidad = c.contarElemento(Listas,_elemento)
print(f"El elemento se repite: {_cantidad} veces")
_elemento = int(input("Igrese el elemento del cual quiere conocer su indice: "))
_index = c.indiceElemento(Listas,_elemento)
print(f"El index es: {_index}")
_elemento=int(input("Ingrese el elemento que desea insertar: "))
_index=int(input("Ingrese el indice del elemento que desea insertar: "))
c.insertarElemento(Listas,_index,_elemento)
c.impresion(Listas,len(Listas))
_index=int(input("Ingrese el indice del elemento que desea extraer: "))
c.extraerElemento(Listas,_index)
c.impresion(Listas,len(Listas))
_elemento=int(input("Ingrese el elemento que desea remover: "))
c.remover(Listas,_elemento)
c.impresion(Listas,len(Listas))
print("Los elementos invertidos son: ")
c.invertir(Listas)
c.impresion(Listas,len(Listas))
print("Los elementos ordenados son: ")
c.ordenar(Listas)
c.impresion(Listas,len(Listas))
print("Se ha limpiado la lista!!")
c.limpiar(Listas)
c.impresion(Listas,len(Listas))

#Hidalgo Ponce Luis Anthony
#Paralelo "A"
