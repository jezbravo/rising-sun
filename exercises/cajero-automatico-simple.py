saldo = [1000]
def welcome():
    print("Bienvenido/a. Por favor ingrese un número para realizar una operación:")
    print("""
    1. Ingresar dinero en la cuenta
    2. Extraer dinero de la cuenta
    3. Ver saldo disponible
    4. Salir \n""")
    v1 = input("Opción seleccionada: ")
    if v1 == "1":
        print("""
        -----------------------------
        Ingresar dinero en la cuenta.
        -----------------------------\n""")
        ingreso = ""
        while ingreso.isdecimal() is False:
            ingreso = input("Escriba el monto a ingresar: ")
        ingreso = float(ingreso)
        saldo.append(ingreso)
        print(f"La operación ha sido exitosa. Su nuevo saldo es de: ${sum(saldo)}.")
        salir = input("¿Desea realizar otra operación? S/N: ").upper()
        if salir == "N":
            print("Hasta luego.")
            exit()
        else:
            welcome()
    elif v1 == "2":
        print("""
              -----------------------------
              Extraer dinero de la cuenta.
              -----------------------------\n""")
        extraer = ""
        while extraer.isdecimal() is False:
            extraer = input("Ingrese el monto a extraer: -")
        extraer = float(extraer)
        if extraer > sum(saldo):
            print(f"Imposible realizar la operación. El monto de extracción ${extraer} excede el saldo disponible de ${sum(saldo)}.")
            welcome()
        else:
            saldo.append(-extraer)
        print(f"La operación ha sido exitosa. Su nuevo saldo es de: ${sum(saldo)}.")
        salir = input("¿Desea realizar otra operación? S/N: ").upper()
        if salir == "N":
            print("Hasta luego.")
            exit()
        else:
            welcome()
    elif v1 == "3":
        print("""
              -----------------------------
              Consultar saldo disponible.
              -----------------------------\n""")
        print(f"Su saldo actual es de: ${sum(saldo)}.")
        salir = input("¿Desea realizar otra operación? S/N: ").upper()
        if salir == "N":
            print("Hasta luego.")
            exit()
        else:
            welcome()        
    elif v1 == "4":
        print("""
              -----------------------------
              Salir.
              -----------------------------\n""")
        print("Hasta luego.")
        exit()
    else:
        print("Opción inválida.")
        welcome()
welcome()