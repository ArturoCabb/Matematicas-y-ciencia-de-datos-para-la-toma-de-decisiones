print("Actividad: comentarios y tipos de datos complejos")

# Son los datos da la persona a considerar
# persona = ["Milton","Mejia",19,1.82,95]
# persona=["Diego","Bahena",19,1.65,50]
# persona=["Maria Ibeth","Tovar Lopez",19,1.67,70]
# persona=["Sergio","Tapia",19,1.68,81]
# persona=["Arturo","Caballero",19,1.62,48]

while True:
    print("Si quiere salir teclee 1\nPara continuar teclee [Enter]")
    x = input()
    if x == 1: break
    else :
        nom = input("Ingrese su nombre   : ")
        ap = input("Ingrese su apellido  : ")
        edad = input("Ingrese su edad    : ")
        est = input("Ingrese su estatura : ")
        peso = input("Ingrese su peso    : ")
        persona=[nom, ap, int(edad), float(est),float(peso)]
        
        # Se usa para calcular el imc
        imc = int(persona[4])/((persona[3])**2)
        print("El imc de ",persona[0],"es: ",imc,sep=' ')

        if imc >= 0 and imc <= 15.99 :
          print (persona[0], "tiene", "Delgadez severa", sep=' ')
        elif imc >= 16.00 and imc <= 16.99 :
          print (persona[0], "tiene", "Delgadez moderada", sep=' ')
        elif imc >= 17.00 and imc <= 18.49:
          print (persona[0], "tiene", "Delgadez leve", sep=' ')
        elif imc >= 18.50 and imc <= 24.99 :
          print (persona[0], "está", "Normal", sep=' ')
        elif imc >= 25.00 and imc <= 29.99:
          print (persona[0], "tiene", "Sobrepeso", sep=' ')
        elif imc >= 30.00 and imc <= 34.99:
          print (persona[0], "tiene", "obesidad leve",sep=' ')
        elif imc >= 35.00 and imc <= 39.00:
          print (persona[0], "tiene", "obesidad media",sep=' ')
        elif imc >= 40.00:
          print (persona[0], "tiene", "obesidad morbida", sep=' ')

        print("----------------------------------------")
