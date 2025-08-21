def salida(k, pesos, t):
    """
    Calcula la salida del perceptrón para una entrada dada.
    
    Parámetros:
    k (tuple): Entrada al perceptrón.
    pesos (list): Lista de pesos asociados a las entradas.
    t (float): Umbral.

    Retorna:
    int: La salida del perceptrón (1 o 0).
    """
    # Inicializamos la variable z con el valor del umbral negativo
    z = -t
    # Calculamos la suma ponderada de las entradas y los pesos
    for i in range(len(k)):
        z = z + (k[i] * pesos[i])
    # Retornamos 1 si la suma es mayor o igual a 0, de lo contrario retornamos 0
    return 1 if z >= 0 else 0

def entrenar_perceptron(datos_ent, pesos, t, l):
    """
    Entrena el perceptrón ajustando los pesos y el umbral.

    Parámetros:
    datos_ent (dict): Diccionario con las entradas y las salidas esperadas.
    pesos (list): Lista de pesos iniciales.
    t (float): Umbral inicial.
    l (float): Tasa de aprendizaje.

    Retorna:
    tuple: Pesos y umbral ajustados después del entrenamiento.
    """
    # Variable para controlar si hubo errores en una iteración
    errores = True
    iteraciones = 0  # Contador de iteraciones
    while errores:
        errores = False
        iteraciones += 1  # Incrementamos el contador de iteraciones
        # Iteramos sobre los datos de entrenamiento
        for k, y in datos_ent.items():
            # Calculamos la salida del perceptrón
            z = salida(k, pesos, t) #z=x1.w1+w2.w2-tita
            # Si la salida es diferente del valor esperado, hay un error
            if z != y:
                errores = True
                # Calculamos el error
                e = y - z
                # Actualizamos el umbral
                t += -(l * e)
                # Actualizamos los pesos
                for i in range(len(k)):
                    pesos[i] += l * e * k[i]
    # Retornamos los pesos y el umbral ajustados
    print(f"Iteraciones para ajustar los pesos: {iteraciones}")
    return pesos, t

def clasificar(entrada, pesos, t):
    """
    Clasifica una nueva entrada utilizando los pesos y el umbral ajustados.

    Parámetros:
    entrada (tuple): Nueva entrada a clasificar.
    pesos (list): Lista de pesos ajustados.
    t (float): Umbral ajustado.

    Retorna:
    int: La salida del perceptrón (1 o 0).
    """
    # Clasificamos una nueva entrada utilizando los pesos y el umbral ajustados
    return salida(entrada, pesos, t)

if __name__ == "__main__":
    # Datos de entrenamiento para la función AND
    datos_ent = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}
    # Pesos iniciales
    pesos = [0.3, 0.3]
    # Umbral inicial
    t = -0.2
    # Tasa de aprendizaje
    l = 0.2
    # Entrenamos el perceptrón con los datos de entrenamiento
    pesos, t = entrenar_perceptron(datos_ent, pesos, t, l)
    # Clasificamos una nueva entrada (0, 1) utilizando los pesos y el umbral ajustados
    print(clasificar((0, 1), pesos, t))
    # Opcional: Mostrar los pesos y el umbral ajustados
    print("Pesos ajustados:", pesos)
    print("Umbral ajustado:", t)
