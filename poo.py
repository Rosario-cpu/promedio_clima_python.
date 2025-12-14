# * Programa orientado a objetos para calcular el promedio semanal del clima *

# * Clase que representa la información de un día de clima *
class ClimaDiario:
    def __init__(self, temperatura):
        # * Encapsulamiento: atributo privado de temperatura *
        self.__temperatura = temperatura

    def obtener_temperatura(self):
        # * Método para acceder a la temperatura del día *
        return self.__temperatura


# * Clase que representa el clima de toda la semana *
class ClimaSemanal:
    def __init__(self):
        # * Lista que guarda los objetos ClimaDiario *
        self.dias = []

    def agregar_dia(self, temperatura):
        # * Se crea un objeto ClimaDiario y se agrega a la lista *
        dia = ClimaDiario(temperatura)
        self.dias.append(dia)

    def calcular_promedio(self):
        # * Calcula el promedio de todas las temperaturas registradas *
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)


# * Función principal que organiza el flujo del programa *
def main():
    clima_semanal = ClimaSemanal()
    print("Ingrese las temperaturas de la semana (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        clima_semanal.agregar_dia(temp)

    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# * Ejecutar el programa si es el archivo principal *
if __name__ == "__main__":
    main()



