'''
    SEBASTIAN CRUZ
    GitHub: https://github.com/SbsCruz
    X: https://twitter.com/sebass_cruzz
    
    APP para creación de directorios para un semestre en python
'''

import os

os.system('cls')
materias = []

ruta_actual = os.getcwd()

# presentamos la ruta actual en la que se encuentra el usuario
print("estas ubicado aquí: "+ ruta_actual)

# presentamos una decisión para saber si quiere que las carpetas se 
# creen en la ubicación actual o quiere cambiar
while True:
    here = input("¿Deseas usar la ruta actual? (S/N): ")
    if here.lower() == "s": 
        ruta = ruta_actual
        break
    elif here.lower() == "n":
        os.system('cls')
        print("Pega la ruta en la que deseas crear las carpetas.")
        print("Puede ser una ruta relativa o absoluta.")
        ruta = input("tu ruta: ")
        break
    else:
        print("Opción no válida. Por favor, ingresa 'S' o 'N'.")       
os.system('cls') 

# conseguimos el semestre, que será el nombre de la carpeta en 
# la que se crearán las demás carpetas
semestre = input("Ingresa el semestre: ")

os.system('cls') 

# obtenemos el número de materias que cursará el usuario
num_materias = int(input("¿cuántas materias tendrás? "))
for i in range(num_materias):
    materia = input("ingresa el nombre de la materia "+str(i+1)+": ")
    materias.append(materia)

os.system('cls') 

# presentamos la información resumida antes de crear la carpeta
print("revisa a información antes de proceder a la creación:")
ruta_final = os.path.join(ruta,semestre)
print("Tus carpetas se crearán aquí: ",ruta_final)
print("Estas son tus materias: ",materias)


# luego de presentar la información preguntamos al usuario si está seguro
# de continuar con la creación
while True:
    sure = input("¿Estás seguro de continuar? (S/N): ")
    if sure.lower() == "s":
        
        if not os.path.exists(ruta_final):
            os.makedirs(ruta_final)
            
        for materia in materias:
            # con la variable "labo" preguntamos si quiere crear una carpeta de Laboratorio dentro de la carpeta de la materia
            labo = input("La materia "+materia+" tiene laboratorio? (S/N) ") 
            os.mkdir(os.path.join(ruta_final,materia))
            ruta_labo = os.path.join(ruta_final,materia)
            if labo.lower()=="s":
                os.mkdir(os.path.join(ruta_labo,"Laboratorio"))
            elif labo.lower()=="n":
                continue
            else:
                print("Opción no válida. Por favor, ingresa 'S' o 'N'.")
        print("CARPETAS CREADAS CON ÉXITO !")
        print("Éxitos en tu semestre :)")
        break
    elif sure.lower() == "n":
        print("Vuelve a ingresar toda la información")
        break
    else:
        print("Opción no válida. Por favor, ingresa 'S' o 'N'.")


    
