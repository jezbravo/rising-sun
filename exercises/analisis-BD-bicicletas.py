import pandas as pd
from matplotlib import pyplot as plt
from sqlalchemy import create_engine, text

# Establecer la cadena de conexión para la base de datos
url_de_la_base_de_datos = 'sqlite:///bikeshare.db'

# Crear el motor de SQLAlchemy
motorDB = create_engine(url_de_la_base_de_datos)

#Función auxiliar para conectarnos a la BD y realizar una consulta.
def consultar_BD(consulta):
  df_tabla = None
  with motorDB.connect() as conexion:
      df_tabla = pd.read_sql(text(consulta), conexion, parse_dates=['start_date', 'end_date'])
      return df_tabla

# 1) ¿Cuál es la cantidad de viajes de los usuarios de tipo Miembro y de tipo Casual que duran 20 minutos o más?
      
consulta = '''
SELECT (COUNT(*)) AS cantidad_de_viajes, member_type
FROM trip_data
WHERE duration >=1200
GROUP BY member_type
'''
print("\nRespuesta 1) La cantidad de viajes que duran 20 minutos o más es la siguiente:\n")
print(consultar_BD(consulta))

# Se grafica la respuesta
df = consultar_BD(consulta)
plt.figure(figsize=(8,6))
plt.bar(df["member_type"], df["cantidad_de_viajes"])
plt.xlabel("Tipo de membresía")
plt.ylabel("Cantidad de viajes")
plt.title("Cantidad de viajes que duran 20 minutos o más")
plt.show()

# 2) ¿En qué bicicleta se realizó el viaje más corto? ¿Cuántos minutos duró ese viaje?

consulta = '''
SELECT MIN(duration) as viaje_mas_corto, bike_number
FROM trip_data
'''
print("\nRespuesta 2) La bicicleta que realizó el viaje más corto (o al menos una de ellas) fue la W00470, con un minuto de duración.\n")
# NOTA: Hay 62 bicicletas que comparten la duración del viaje más corto con 60 segundos. La W00470 es sólo una de ellas.
print(consultar_BD(consulta))

# 3) ¿Cual es el promedio de duración de los viajes de los usuarios del tipo Casual? ¿Se podría decir que, en promedio, tienen viajes más cortos que los usuarios Miembro?

consulta = '''
SELECT ROUND(AVG(duration),3) as promedio_duracion_viaje, member_type
FROM trip_data
GROUP BY member_type
'''
print("""\nRespuesta 3) El promedio de duración de los viajes de los usuarios tipo "Casual" es de 2784 segundos (46,4 minutos).
No tienen, en promedio, viajes más cortos que los usuarios del tipo "Miembro", ya que estos últimos viajan en promedio 775 segundos (12,9 minutos)\n""")
print(consultar_BD(consulta))

# Se grafica la respuesta
df = consultar_BD(consulta)
plt.figure(figsize=(8,6))
plt.bar(df["member_type"], df["promedio_duracion_viaje"])
plt.xlabel("Tipo de membresía")
plt.ylabel("Duración promedio de los viajes (seg)")
plt.title("Uso promedio de los distintos usuarios")
plt.show()

# 4) ¿Hay diferencia en la elección de estación de inicio según el tipo de membresía? (Nota: la idea es comparar estaciones "más populares")

# Primero se procede a saber cuáles son las 3 estaciones más populares (con más viajes de inicio):

consulta = '''
SELECT b.station_id, t.start_station, b.name, COUNT(*) AS cantidad_de_viajes
FROM trip_data t
LEFT JOIN bikeshare_stations b ON t.start_station = b.station_id
GROUP BY b.name
ORDER BY cantidad_de_viajes DESC
LIMIT 3
'''
# Se observa que los ID de las estaciones más populares son: 31200, 31201 y 31623.
# Ahora bien, se calcula para cada estación, qué cantidad de miembros realizaron viajes:

consulta = '''
SELECT t.start_station, b.name, t.member_type, COUNT(*) AS cantidad_de_viajes
FROM trip_data t
LEFT JOIN bikeshare_stations b ON t.start_station = b.station_id
WHERE t.start_station = 31200
GROUP BY t.member_type
'''
print("""\nRespuesta 4.a) Para la primera estación más popular, "Massachusetts Ave & Dupont Circle NW":
Un 22,2 % son miembros tipo "Casual"
Un 77,8 % son miembros tipo "Miembro"
""")
print(consultar_BD(consulta))
# Se grafica la respuesta
df = consultar_BD(consulta)
plt.figure(figsize=(8,6))
colores = ["orange","lightblue"]
etiquetas = ["Casuales","Miembros"]
df["cantidad_de_viajes"].plot(kind="pie", autopct='%1.1f%%', startangle=90, colors = colores, labels = etiquetas)
plt.title("Distribución de miembros en la estación 31200 Massachusetts Ave & Dupont Circle NW")
plt.show()

consulta = '''
SELECT t.start_station, b.name, t.member_type, COUNT(*) AS cantidad_de_viajes
FROM trip_data t
LEFT JOIN bikeshare_stations b ON t.start_station = b.station_id
WHERE t.start_station = 31201
GROUP BY t.member_type
'''
print("""\nRespuesta 4.b) Para la segunda estación más popular, "15th & P St NW":
Un 15,2 % son miembros tipo "Casual"
Un 84,8 % son miembros tipo "Miembro"
""")
print(consultar_BD(consulta))
# Se grafica la respuesta
df = consultar_BD(consulta)
plt.figure(figsize=(8,6))
colores = ["orange","lightblue"]
etiquetas = ["Casuales","Miembros"]
df["cantidad_de_viajes"].plot(kind="pie", autopct='%1.1f%%', startangle=90, colors = colores, labels = etiquetas)
plt.title("Distribución de miembros en la estación 31201 15th & P St NW")
plt.show()

consulta = '''
SELECT t.start_station, b.name, t.member_type, COUNT(*) AS cantidad_de_viajes
FROM trip_data t
LEFT JOIN bikeshare_stations b ON t.start_station = b.station_id
WHERE t.start_station = 31623
GROUP BY t.member_type
'''
print("""\nRespuesta 4.c) Para la tercera estación más popular, "Columbus Circle / Union Station":
Un 15,1 % son miembros tipo "Casual"
Un 84,9 % son miembros tipo "Miembro"
""")
print(consultar_BD(consulta))
# Se grafica la respuesta
df = consultar_BD(consulta)
plt.figure(figsize=(8,6))
colores = ["orange","lightblue"]
etiquetas = ["Casuales","Miembros"]
df["cantidad_de_viajes"].plot(kind="pie", autopct='%1.1f%%', startangle=90, colors = colores, labels = etiquetas)
plt.title("Distribución de miembros en la estación 31623 Columbus Circle / Union Station")
plt.show()

print("""\nPor lo tanto, sí hay diferencia en la elección de la estación de inicio, según el tipo de membresía:
la mayoría de los usuarios de las estaciones más populares son del tipo "Miembro".
""")

# 5) ¿Cuál es el nombre de la estación donde terminan la mayoría de los paseos?

consulta = '''
SELECT t.end_station, b.station_id, b.name, COUNT(*) AS cantidad_de_viajes
FROM trip_data t
LEFT JOIN bikeshare_stations b ON t.end_station = b.station_id
GROUP BY b.name
ORDER BY cantidad_de_viajes DESC
LIMIT 1
'''
print("\nRespuesta 5) El nombre de la estación donde termina la mayoría de los paseos es: Massachusetts Ave & Dupont Circle NW.")
print(consultar_BD(consulta))

# 6) ¿Sería posible determinar que estácion se encuentra más alejada del resto sin utilizar un gráfico? (Nota: recuerden que durante la clase encontramos una estación que no se encontraba en Washington)

# Respuesta: sería posible si, por ejemplo, ordenamos las coordenadas.
# Si probamos ordenar de manera ascendente o descendente los valores de latitud o longitud.. 
# ... veremos que el registro que se aleja del resto es el de Columbus Circle / Union Station, con el station_id 31623.

consulta = '''
SELECT *
FROM bikeshare_stations
WHERE latitude IS NOT NULL
AND longitude IS NOT NULL
ORDER BY latitude DESC
'''
print("\nRespuesta 6) La estación más alejada del resto es Columbus Circle / Union Station, con el station_id 31623.\n")
print(consultar_BD(consulta))