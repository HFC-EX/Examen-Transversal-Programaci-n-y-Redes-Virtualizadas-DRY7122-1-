import requests

def obtener_distancia(origen, destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=9DG6SS3q63tIif9UN7jaBqnCaGp5fn8j&from={origen}&to={destino}'

    response = requests.get(url)
    data = response.json()

    distancia = data['route']['distance'] * 1.60934

    return distancia

def calcular_duracion(distancia):
    # Calcular la duración aproximada del viaje asumiendo una velocidad promedio de 100 km/h
    duracion_horas = distancia / 100 
    duracion_minutos = (duracion_horas % 1) * 100
    duracion_segundos = (duracion_minutos % 1) * 100

    return duracion_horas, duracion_minutos, duracion_segundos

def calcular_combustible(distancia):
    # Calcular el combustible requerido asumiendo un consumo promedio de 10 km/l
    combustible_litros = distancia / 10

    return combustible_litros

# Se Obtiene las ciudades de origen y destino del usuario
print("------------------------------------------------------")
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")
print("------------------------------------------------------")


distancia_km = obtener_distancia(ciudad_origen, ciudad_destino)


duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia_km)

# Calcular el combustible requerido
combustible_litros = calcular_combustible(distancia_km)

# Imprimir los resultados
print("Duración del viaje: {} horas, {} minutos, {} segundos".format(int(duracion_horas), int(duracion_minutos), int(duracion_segundos)))
print("Combustible requerido: {:.1f} litros".format(combustible_litros))
print("Distancia del viaje: {:.1f} Km".format(distancia_km))
print("------------------------------------------------------")


# Imprimir la narrativa del viaje
print("Narrativa del Viaje:")
print("El viaje desde {} hasta {} es de {:.1f} km.".format(ciudad_origen, ciudad_destino, distancia_km))
print("Se requerirán aproximadamente {:.1f} litros de combustible.".format(combustible_litros))
print("La duración estimada del viaje es de {} horas, {} minutos y {} segundos.".format(int(duracion_horas), int(duracion_minutos), int(duracion_segundos)))


# Agregar salida de la letra S
print("\n----------------------------------------------------")
Salida = input("\nPresione 's' para salir: ")
