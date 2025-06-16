class Cuenta:
    _contador_cuenta = 100000
    
    def __init__(self, documento="", saldo=0.0, interes=0.0):
        self.__numero_cuenta = self.__genera_numero_cuenta()
        self.__documento = documento
        self.__saldo = saldo
        self.__interes_anual = interes
    
    def __genera_numero_cuenta(self):
        Cuenta._contador_cuenta += 1
        return Cuenta._contador_cuenta
    
    def actualizar_saldo(self):
        interes_diario = self.__interes_anual / 365 / 100
        self.__saldo += self.__saldo * interes_diario
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False
    
    def mostrar_datos(self):
        return f"Número de cuenta: {self.__numero_cuenta}\nDocumento: {self.__documento}\nSaldo actual: ${self.__saldo:.2f}\nInterés anual: {self.__interes_anual}%"
    
    # Getters
    def get_numero_cuenta(self): 
        return self.__numero_cuenta
    def get_documento(self): 
        return self.__documento
    def get_saldo(self): 
        return self.__saldo
    def get_interes(self): 
        return self.__interes_anual
    
    def set_documento(self, documento): self.__documento = documento
    def set_interes(self, interes): self.__interes_anual = interes

def mostrar_menu():
    print("\n=== SISTEMA BANCARIO ===")
    print("1. Crear cuenta")
    print("2. Actualizar saldo (aplicar interés)")
    print("3. Ingresar dinero")
    print("4. Retirar dinero")
    print("5. Mostrar datos de cuenta")
    print("6. Salir")

def crear_cuenta():
    print("\n--- CREAR CUENTA ---")
    documento = input("Documento de identidad: ")
    saldo = float(input("Saldo inicial: $"))
    interes = float(input("Interés anual (%): "))
    cuenta = Cuenta(documento, saldo, interes)
    print(f"Cuenta creada exitosamente. Número: {cuenta.get_numero_cuenta()}")
    return cuenta

def actualizar_saldo(cuenta):
    if cuenta:
        saldo_anterior = cuenta.get_saldo()
        cuenta.actualizar_saldo()
        print(f"Saldo actualizado de ${saldo_anterior:.2f} a ${cuenta.get_saldo():.2f}")
    else:
        print("No hay cuenta creada")

def ingresar_dinero(cuenta):
    if cuenta:
        cantidad = float(input("Cantidad a ingresar: $"))
        if cuenta.ingresar(cantidad):
            print(f"Ingreso exitoso. Nuevo saldo: ${cuenta.get_saldo():.2f}")
        else:
            print("Error: Cantidad inválida")
    else:
        print("No hay cuenta creada")

def retirar_dinero(cuenta):
    if cuenta:
        cantidad = float(input("Cantidad a retirar: $"))
        if cuenta.retirar(cantidad):
            print(f"Retiro exitoso. Nuevo saldo: ${cuenta.get_saldo():.2f}")
        else:
            print("Error: Cantidad inválida o saldo insuficiente")
    else:
        print("No hay cuenta creada")

def mostrar_datos_cuenta(cuenta):
    if cuenta:
        print("\n--- DATOS DE LA CUENTA ---")
        print(cuenta.mostrar_datos())
    else:
        print("No hay cuenta creada")

cuenta_actual = None

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cuenta_actual = crear_cuenta()
    elif opcion == "2":
        actualizar_saldo(cuenta_actual)
    elif opcion == "3":
        ingresar_dinero(cuenta_actual)
    elif opcion == "4":
        retirar_dinero(cuenta_actual)
    elif opcion == "5":
        mostrar_datos_cuenta(cuenta_actual)
    elif opcion == "6":
        print("¡Gracias por usar el sistema bancario!")
        break
    else:
        print("Opción inválida")
