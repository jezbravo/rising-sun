import pandas as pd
import matplotlib.pyplot as plt
ruta_del_data_frame = "Internet2013.csv"
internet_df = pd.read_csv(ruta_del_data_frame, sep = ";")

# Análisis exploratorio y visualización
print(internet_df)
internet_df.describe()
internet_df.info() # Acá podemos ver que son 1500 filas, todas non-null.

# 1. ¿El conjunto de datos es representativo de ambos géneros: mujeres y hombres?
cantidad_sexos = internet_df["Sexo"].value_counts()
print(cantidad_sexos)
colores = ["pink","lightblue"]
etiquetas = ["Mujeres","Hombres"]
internet_df["Sexo"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=90, colors = colores, labels = etiquetas)
plt.title("Distribución de sexos en encuesta")
plt.show()
# Respuesta: Depende. Es decir, sí, técnicamente el conjunto es representativo porque representa 2 sexos.
# Ahora bien, si por "representativo" se entiende "equitativo" entonces no, el conjunto no es representativo, por lo siguiente:
# Asumiendo que el número 1 se refiera a "Masculino", y el número 2 se refiera a "Femenino", entonces tendríamos 685 hombres (45,7%) y 815 mujeres (54,3%)

#2. ¿Cómo se encuentra distribuido respecto a la nacionalidad?
internet_df["Nacionalidad"].value_counts().plot(kind="bar")
cantidad_paises = internet_df["Nacionalidad"].value_counts()
print(cantidad_paises)
plt.title("Distribución según la nacionalidad")
plt.xlabel("Paises")
plt.ylabel("Cantidad")
plt.show()
# Respuesta: La mayoría proviene de Argentina (799). Le siguen de cerca Canadá (371) y Brasil (329). Uruguay queda último con apenas 1.

# 3. ¿En qué rango de edades se encuentran la mayor segmentación de la muestra?
internet_df["Edad"].value_counts().plot(kind="hist")
plt.title("Distribución según la edad")
plt.xlabel("Edades")
plt.show()
# Respuesta: la mayor segmentación de la muestra se encuentra en el rango de edades entre 30 a 40 años aprox.

# 4. ¿Encuentra alguna diferencia en el valor medio si agrupa los registros por Nacionalidad?
registros_agrupados = internet_df.groupby("Nacionalidad")["Edad"].mean()
print(registros_agrupados)
internet_df.groupby("Nacionalidad")["Edad"].mean().plot(kind="bar")
plt.title("Media de edades según el país")
plt.ylabel("Edad")
plt.grid()
plt.show()
# Respuesta: Hay muy poca diferencia entre los valores medios de los registros: Argentina (36), Brasil (35), y Canadá (36) tienen prácticamente la misma media. En cambio en Uruguay es de 23.

# 5. ¿Cuál es el mayor uso que se le da a internet en este grupo de estudio?
internet = internet_df["Sitio"].value_counts()
mayor_uso_internet = internet.idxmax()
print(mayor_uso_internet)
# Respuesta: el mayor uso que se le da a internet es 7: "Otros".
internet_df["Sitio"].value_counts().plot(kind="bar")
plt.title("Usos de internet")
plt.xlabel("Aplicación o actividad")
plt.ylabel("Cantidad de usuarios encuestados")
plt.show()

# 6. ¿Que variable del conjunto de datos está más relacionada con el tiempo de uso promedio (Uso)?

# Se limpia el DF de campos no numéricos
columnas_no_numericas = ['Nacionalidad']
internet_df = internet_df.drop(columnas_no_numericas, axis=1)

# Se convierte las columnas con valores en formato estándar a formato numérico
internet_df['id'] = pd.to_numeric(internet_df['id'], errors='coerce')
internet_df['Edad'] = pd.to_numeric(internet_df['Edad'], errors='coerce')
internet_df['Sexo'] = pd.to_numeric(internet_df['Sexo'], errors='coerce')
internet_df['Estatura'] = pd.to_numeric(internet_df['Estatura'], errors='coerce')
internet_df['Sitio'] = pd.to_numeric(internet_df['Sitio'], errors='coerce')
internet_df['Uso'] = pd.to_numeric(internet_df['Uso'], errors='coerce')
internet_df['Temperatura'] = pd.to_numeric(internet_df['Temperatura'], errors='coerce')
internet_df['Autos'] = pd.to_numeric(internet_df['Autos'], errors='coerce')
internet_df['Cigarrillos'] = pd.to_numeric(internet_df['Cigarrillos'], errors='coerce')

matriz_de_correlacion = internet_df.corr()

tiempo_de_uso_promedio = "Uso"
correlacion_con_uso = matriz_de_correlacion[tiempo_de_uso_promedio]
correlaciones_ordenadas = correlacion_con_uso.abs().sort_values(ascending=False)
variable_mas_correlacionada = correlaciones_ordenadas.index[1]
# Respuesta:
print(f"La variable del conjunto más relacionada con {tiempo_de_uso_promedio} es: {variable_mas_correlacionada}.")
uso = internet_df["Uso"]
cigarrillos = internet_df["Cigarrillos"]
plt.scatter(uso,cigarrillos)
plt.xlabel("Tiempo de uso promedio")
plt.ylabel("Cigarrillos")
plt.title("Correlación entre variables")
plt.show()