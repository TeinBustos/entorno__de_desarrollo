while True:
    try:
        numerador = float(input("Ingrese el numerador: "))
        while True:
            try:
                denominador = float(input("Ingrese el denominador: "))
                break
            except ValueError:
                print("Error!!, ingrese un valor numerico")
        if denominador == 0:
            raise ZeroDivisionError("Error!!, no se puede dividir por cero")
        
        resultado = numerador / denominador
        print("El resultado de la division es: ", resultado)
        
    except ValueError:
        print("Error!, Ingrese un valor numerico para el numerador")
    
    except ZeroDivisionError as e:
        print(e)
    continuar = input("Desea realizar otra division? (Presione 's')")
    if continuar.lower() != 's':
        break
    
    