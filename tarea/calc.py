 
from calcfunc import * 
from parqueo import *

while True: #Creamos un bucle
    try: #Intentamos obtener los datos de entrada
       
        op = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Lavado



        
        2- Alquiler
        3- Estacionamiento
        """))
        a = int(input("Ingresa el primer numero: \n")) #Solicitamos el 1er numero al usuario
        b = int(input("Ingresa el segundo numero: \n"))#Solicitamos el 2do numero al usuario
        print (("Que calculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #Preguntamos el calc
 
##########################################-3-##################################################
        if op == '1':
            print("El resultado es {}". format(sumar(a, b))) 
            #Aqui tenemos que cambiar las funciones, enviarle los argumentos para sus parametros
            #Y las metemos en un print, directamente para imprimir el resultado
            break
        elif op == '2':
            print("El resultado es {}". format(restar(a, b)))
            break
        elif op == '3':
            print("El resultado es {}". format(estacionamiento(a, b)))
            break
        
        else:
            print ("""Has ingresado un numero de opcion erroneo""") #En caso que el numero no
                                                                            #se encuentre
    except:
        print ("Error")
        op = '?'