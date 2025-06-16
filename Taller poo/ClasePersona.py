class Persona:
    _contador_dni = 0
    
    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__genera_dni()
    
    def calcular_imc(self):
        if self.__altura == 0 or self.__peso == 0:
            return 0
        imc = self.__peso / ((self.__altura / 100) ** 2)
        if imc < 18.5: return -1
        elif imc <= 24.9: return 0
        elif imc <= 29.9: return 1
        elif imc <= 39.9: return 2
        else: return 3
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18
    
    def __comprobar_sexo(self, sexo):
        return sexo.upper() if sexo.upper() in ['M', 'F'] else 'M'
    
    def listar_informacion(self):
        genero = "Masculino" if self.__sexo == 'M' else "Femenino"
        categorias = ["Por debajo del peso", "Normal", "Con sobrepeso", "Obesidad", "Obesidad extrema o de alto riesgo"]
        categoria = categorias[self.calcular_imc() + 1]
        return f"Hola {self.__nombre}, tu código dentro del sistema es {self.__dni}. Tu identificación es {self.__documento}. Tu edad es {self.__edad} años. Tu género es {genero}. Tu Peso es {self.__peso} kg y tu Altura es {self.__altura} cm. Al calcular tu IMC concluimos que tu peso esta: {categoria}"
    
    def __genera_dni(self):
        Persona._contador_dni += 1
        return Persona._contador_dni
    
    def get_documento(self): return self.__documento
    def get_nombre(self): return self.__nombre
    def get_edad(self): return self.__edad
    def get_sexo(self): return self.__sexo
    def get_peso(self): return self.__peso
    def get_altura(self): return self.__altura
    def get_dni(self): return self.__dni
    
    def set_documento(self, documento): self.__documento = documento
    def set_nombre(self, nombre): self.__nombre = nombre
    def set_edad(self, edad): self.__edad = edad
    def set_sexo(self, sexo): self.__sexo = self.__comprobar_sexo(sexo)
    def set_peso(self, peso): self.__peso = peso
    def set_altura(self, altura): self.__altura = altura

while True:
    print("\n=== REGISTRO DE PERSONA ===")
    
    documento = input("Documento: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    
    persona1 = Persona(documento, nombre, edad, sexo, peso, altura)
    persona2 = Persona(documento, nombre, edad, sexo)
    persona3 = Persona()
    persona3.set_documento(documento)
    persona3.set_nombre(nombre)
    persona3.set_edad(edad)
    persona3.set_sexo(sexo)
    persona3.set_peso(peso)
    persona3.set_altura(altura)
    
    personas = [persona1, persona2, persona3]
    tipos = ["Objeto 1 (completo)", "Objeto 2 (sin peso/altura)", "Objeto 3 (por defecto)"]
    categorias = ["Por debajo del peso", "Normal", "Con sobrepeso", "Obesidad", "Obesidad extrema"]
    
    for i in range(3):
        print(f"\n--- {tipos[i]} ---")
        imc = personas[i].calcular_imc()
        print(f"IMC: {categorias[imc + 1]}")
        print(f"Mayor de edad: {'SÍ' if personas[i].es_mayor_de_edad() else 'NO'}")
        print(personas[i].listar_informacion())
    
    continuar = input("\n¿Otra persona? (s/n): ").lower() == 's'