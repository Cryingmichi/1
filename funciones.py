contactos=[]
import csv



def opcion_1():
    nombre=input("Ingrese su nombre y apellido: ")
    telefono=int(input("Ingrese su telefono: "))
    correo=input("Ingrese su gmail: ") 
    persona={"nombre": nombre,
             "telefono":telefono,
             "correo": correo }
    
    contactos.append(persona)
    print("A sido agendado con exito!!")
def opcion_2():
    if not contactos:
        print("No hay contactos reistrados")
    else:
        print("\tLista de contactos")
        for c in contactos:
            print("Nombre: ",c["nombre"],"\nTelefono:",c["telefono"],"\nCorreo:", c["correo"] )

def opcion_3():
    if not contactos:
        print("No existen contactos, registre uno en la opcion 1!")
    else:
        try:
            nombre_archivo= input("Ingrese nombre del archivo: ")
            with open(nombre_archivo+".csv","x",newline="") as archivo:
                escritor= csv.DictWriter(archivo, ["nombre","telefono","correo"])
                escritor.writerows(contactos)
            print("archivo guardado con exito")
        except:
            print("el archivo ya existe")

    
def salida():
    print("Adios!")


################################VALIDACIONES:###########################################
    def validar_nombre():
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print("ERROR! el nombre debe al menos tener 3 caaracteres y solo letras!")

    def validar_numero():
        while True:
            try:
                tel=int(input("Ingrese su telefono: "))
                if len(str(tel))==9 and str(tel) [0]==9:
                    return tel
                else: 
                    print("ERROR! el telefono debe comenzar con 9 y tener 9 digitos!")

            except:
                print("Error! debe ser numero entero")
    def validar_correo():
        cor = input("Ingrese correo: ")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip())>=13:
            return cor
        else:
            print("ERROR! correo incorrecto, solo se aceptan @gmail")