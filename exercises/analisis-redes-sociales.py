import pandas as pd
import matplotlib.pyplot as plt
ruta_del_data_frame = "redes_sociales.csv"
redes_df = pd.read_csv(ruta_del_data_frame, sep = ",")

# Análisis exploratorio y visualización
print(redes_df)
redes_df.describe()
redes_df.info() #100 filas non-null

# 1. ¿Cual es el valor promedio de publicaciones de los perfiles?
publicaciones_promedio = redes_df["Publicaciones"].mean()
# Respuesta:
print(f"El valor promedio de publicaciones es de {publicaciones_promedio}.")
redes_df.groupby("Perfil")["Publicaciones"].mean().plot(kind="line")
plt.title("Promedios de publicaciones de cada perfil")
plt.xlabel("Perfiles")
plt.ylabel("Publicaciones")
plt.show()

# 2. ¿Qué perfil tiene más seguidores?
mas_seguidores = redes_df["Seguidores"].max()
fila_con_mas_seguidores = redes_df.loc[redes_df["Seguidores"] == mas_seguidores]
perfil_con_mas_seguidores = fila_con_mas_seguidores["Perfil"].iloc[0]
# Respuesta:
print(f"El perfil con más seguidores es: {perfil_con_mas_seguidores}, con {mas_seguidores} seguidores.")

# 3. ¿Sería factible pensar que aquellos perfiles que más publicaciones tienen poseen un número mayor de interacciones?
interacciones = "Interacciones"

# Se limpia el DF de campos no numéricos
columnas_no_numericas = ['Perfil']
redes_df = redes_df.drop(columnas_no_numericas, axis=1)

# Se convierte las columnas con valores en formato estándar a formato numérico
redes_df['Seguidores'] = pd.to_numeric(redes_df['Seguidores'], errors='coerce')
redes_df['Publicaciones'] = pd.to_numeric(redes_df['Publicaciones'], errors='coerce')
redes_df['Interacciones'] = pd.to_numeric(redes_df['Interacciones'], errors='coerce')

matriz_de_correlacion = redes_df.corr()
correlacion_con_interacciones = matriz_de_correlacion[interacciones]
correlaciones_ordenadas = correlacion_con_interacciones.abs().sort_values(ascending=False)
variable_mas_correlacionada = correlaciones_ordenadas.index[1]
# Respuesta:
print(f"La variable del conjunto más relacionada con {interacciones} es: {variable_mas_correlacionada}. Por lo tanto sí, sería factible pensar que los perfiles con más publicaciones tengan más interacciones.")
interacciones = redes_df["Interacciones"]
publicaciones = redes_df["Publicaciones"]
plt.scatter(interacciones, publicaciones)
plt.xlabel("Interacciones")
plt.ylabel("Publicaciones")
plt.title("Correlación entre variables")
plt.show()

# 4. La administración de la empresa le solicita que envíe una lista de 10 posibles perfiles que considere aptos para participar como embajadores en campañas publicitarias. Selecciona 10 candidatos según su criterio (es necesario informar el criterio de selección utilizado).
seleccion = redes_df.nlargest(10, "Seguidores")
# Respuesta:
# El criterio de selección fue elegir a los perfiles con más seguidores.
print(f"Los perfiles seleccionados son: {seleccion}")

# 5. La empresa de publicidad ofrece como servicio capacitaciones para el manejo de redes sociales. Partiendo de la base de datos que está analizando, seleccione los perfiles que considere que requieren mejorar sus desempeño (es necesario informar el criterio de selección utilizado).
seleccion_2 = redes_df.nsmallest(10, "Seguidores")
# Respuesta:
# El criterio de selección fue elegir a los perfiles con menos seguidores.
print(f"Los perfiles seleccionados son: {seleccion_2}")

# 6. La empresa de publicidad utiliza el siguiente criterio para considerar si un perfil es INFLUENCER o NO INFLUENCER: Seguidores > 20000 Y Interacciones > 1000. Partiendo de esta información realice un gráfico de torta que represente el porcentaje de INFLUENCERS y NO INFLUENCERS del conjunto de datos que está analizando. Ayuda: Se sugiere generar una nueva columna a la tabla de datos que indique si cumple con los criterios para ser considerado influencer.
def influencer(x):
    if x["Seguidores"] > 20000 and \
    x["Interacciones"] > 1000:
        return "Influencer"
    else:
        return "No influencer"

redes_df_nuevo = redes_df
redes_df_nuevo["Influencer?"] = redes_df.apply(influencer, axis=1)
print(redes_df_nuevo)
colores = ["gray", "lightgreen"]
etiquetas = ["No influencers", "Influencers"]
contratacion = redes_df_nuevo["Influencer?"].value_counts()
plt.pie(contratacion, autopct='%1.1f%%', startangle=90, colors = colores, labels = etiquetas)
plt.title("Porcentaje de perfiles influencers en el conjunto de datos")
plt.show()