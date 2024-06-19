import os,time,csv
from funciones import *



while True:
    os.system("cls")
    print("""    Menú de contactos    
          1. Agregar contacto
          2. Mostrar contactos
          3. Guardar en csv
          4. SALIR
          """)
    
    while True:
        try:
            opc=int(input("Elija una opcion: "))

            if opc in (1,2,3,4):
                os.system("cls")
                break
            else: 
                input("Elija opcion valida!!")
        except:
            input("Elija numero entero")

    if opc==1:
        opcion_1()
    elif opc==2:
        opcion_2()
        time.sleep(3)
    elif opc==3:
        opcion_3()
    else:
        salida()
        time.sleep(3)
        break


     

            

    



