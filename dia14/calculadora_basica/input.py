def captura_datos():
    """Capturar los numeros ingresados

    Returns:
        tupla: par de numeros capturados
    """
    x = float(input("Ingrese el primer número "))
    y = float(input("Ingrese el segundo número "))
    return x, y

if __name__ == "__main__":
    print("Probando la captura de datos")
    print(captura_datos())