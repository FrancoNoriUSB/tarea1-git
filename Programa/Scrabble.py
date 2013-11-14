#Programa de Scrabble.
#Realizado por Franco Nori G. Carnet: 08-10801

#Se abre el archivo
f = open('sowpods.txt', 'r')

#Lista abecedario
diccionario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Se inicializan las variables
palabra=0

#Se recorre el archivo palabra por palabra
while(palabra!=""):
  palabra=f.readline()
  letra_ant=0
  
  #Se revisa letra por letra
  for letra in palabra:
    
    #Se revisa si la letra esta consecutiva
    if(letra == letra_ant):
      
      #Verifica si la letra se encuentra repetida y la elimina del diccionario original
      if(diccionario.count(letra)>0):
	diccionario.remove(letra)
    letra_ant = letra

#Se busca cuales letras no se repiten mas de una vez
letras = ''
for letra in diccionario:
  letras = letra+" "+letras
print "Las siguientes letras no aparecen repetidas: " + letras