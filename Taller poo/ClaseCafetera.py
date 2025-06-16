class Cafetera:
    
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        self.__capacidad_maxima = capacidad_maxima
        if cantidad_actual > capacidad_maxima:
            self.__cantidad_actual = capacidad_maxima
        else:
            self.__cantidad_actual = cantidad_actual
    
    def llenar_cafetera(self):
        self.__cantidad_actual = self.__capacidad_maxima
        print(f"Cafetera llena. Cantidad actual: {self.__cantidad_actual} c.c.")
    
    def servir_taza(self, capacidad_taza):
        if capacidad_taza <= 0:
            print("Error: Capacidad de taza inválida")
            return 0
        
        if self.__cantidad_actual >= capacidad_taza:
            self.__cantidad_actual -= capacidad_taza
            print(f"Taza servida con {capacidad_taza} c.c. Cantidad restante: {self.__cantidad_actual} c.c.")
            return capacidad_taza
        else:
            cafe_servido = self.__cantidad_actual
            self.__cantidad_actual = 0
            print(f"Se sirvió lo que quedaba: {cafe_servido} c.c. Cafetera vacía.")
            return cafe_servido
    
    def vaciar_cafetera(self):
        self.__cantidad_actual = 0
        print("Cafetera vaciada completamente.")
    
    def agregar_cafe(self, cantidad):
        if cantidad <= 0:
            print("Error: Cantidad inválida")
            return
        
        if self.__cantidad_actual + cantidad <= self.__capacidad_maxima:
            self.__cantidad_actual += cantidad
            print(f"Se agregaron {cantidad} c.c. Cantidad actual: {self.__cantidad_actual} c.c.")
        else:
            cantidad_agregada = self.__capacidad_maxima - self.__cantidad_actual
            self.__cantidad_actual = self.__capacidad_maxima
            print(f"Solo se pudieron agregar {cantidad_agregada} c.c. Cafetera llena: {self.__cantidad_actual} c.c.")
    
    def mostrar_estado(self):
        print(f"Capacidad máxima: {self.__capacidad_maxima} c.c.")
        print(f"Cantidad actual: {self.__cantidad_actual} c.c.")
        print(f"Espacio disponible: {self.__capacidad_maxima - self.__cantidad_actual} c.c.")
    
    def get_capacidad_maxima(self):
        return self.__capacidad_maxima
    
    def get_cantidad_actual(self):
        return self.__cantidad_actual

def mostrar_menu():
    print("\n=== SISTEMA DE CAFETERA ===")
    print("1. Crear cafetera por defecto")
    print("2. Crear cafetera personalizada")
    print("3. Llenar cafetera")
    print("4. Servir taza")
    print("5. Vaciar cafetera")
    print("6. Agregar café")
    print("7. Mostrar estado")
    print("8. Salir")

def main():
    cafetera = None
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cafetera = Cafetera()
            print("Cafetera creada por defecto (1000 c.c., vacía)")
            
        elif opcion == "2":
            capacidad = int(input("Capacidad máxima (c.c.): "))
            cantidad = int(input("Cantidad inicial (c.c.): "))
            cafetera = Cafetera(capacidad, cantidad)
            print(f"Cafetera creada con capacidad {cafetera.get_capacidad_maxima()} c.c. y cantidad {cafetera.get_cantidad_actual()} c.c.")
            
        elif opcion == "3":
            if cafetera:
                cafetera.llenar_cafetera()
            else:
                print("Error: Debe crear una cafetera primero")
                
        elif opcion == "4":
            if cafetera:
                capacidad_taza = int(input("Capacidad de la taza (c.c.): "))
                cafetera.servir_taza(capacidad_taza)
            else:
                print("Error: Debe crear una cafetera primero")
                
        elif opcion == "5":
            if cafetera:
                cafetera.vaciar_cafetera()
            else:
                print("Error: Debe crear una cafetera primero")
                
        elif opcion == "6":
            if cafetera:
                cantidad = int(input("Cantidad de café a agregar (c.c.): "))
                cafetera.agregar_cafe(cantidad)
            else:
                print("Error: Debe crear una cafetera primero")
                
        elif opcion == "7":
            if cafetera:
                print("\n--- ESTADO DE LA CAFETERA ---")
                cafetera.mostrar_estado()
            else:
                print("Error: Debe crear una cafetera primero")
                
        elif opcion == "8":
            print("¡Gracias por usar el sistema de cafetera!")
            break
            
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()