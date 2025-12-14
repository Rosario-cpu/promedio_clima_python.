# * Programa tradicional para calcular el promedio semanal del clima *

# * Función para ingresar las temperaturas diarias *
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de la semana (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# * Función para calcular el promedio semanal *
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# * Función principal que organiza el flujo del programa *
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

# * Ejecutar el programa si es el archivo principal *
if __name__ == "__main__":
    main()
