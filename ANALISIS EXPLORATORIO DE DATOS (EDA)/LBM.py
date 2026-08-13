import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### 1.Datos
trimestres=["Q1","Q2","Q3","Q4"]
año1=[2.1,2.4,2.6,3.2]
año2=[2.3,2.6,2.8,3.5]
año3=[2.6,2.9,3.1,3.9]

### 2.Dataframe
df=pd.DataFrame({
    "Trimestre":trimestres,
    "Año 1":año1,
    "Año 2":año2,
    "Año 3":año3
})

print(df)

### 3.Calculos

#Incremento absoluto intra-anual (Q4 - Q1)
diff_año1 = df["Año 1"][3] - df["Año 1"][0]
diff_año2 = df["Año 2"][3] - df["Año 2"][0]
diff_año3 = df["Año 3"][3] - df["Año 3"][0]  # 3.9 - 2.6 = 1.3

#Porcentaje de variación intra-anual ((Q4 - Q1) / Q1) * 100
pct_año1 = (diff_año1 / df["Año 1"][0]) * 100
pct_año2 = (diff_año2 / df["Año 2"][0]) * 100
pct_año3 = (diff_año3 / df["Año 3"][0]) * 100

#Diferencias interanuales por cada Q (Año 3 - Año 1)
diff_q1 = df["Año 3"][0] - df["Año 1"][0]
diff_q2 = df["Año 3"][1] - df["Año 1"][1]
diff_q3 = df["Año 3"][2] - df["Año 1"][2]
diff_q4 = df["Año 3"][3] - df["Año 1"][3]

#Promedios anuales= (Q1  + Q2 + Q3 + Q4) / 4)
media_año1 = df["Año 1"].mean() 
media_año2 = df["Año 2"].mean() 
media_año3 = df["Año 3"].mean() 

### 4.Grafico

#Para que el grafico se vea oscuro
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#1a1a24')
ax.set_facecolor('#1a1a24')

#Colores para cada año
colorA1 = '#3895d3'
colorA2 = '#4cd137' 
colorA3 = '#ff6b6b' 

#Lineas del grafico de tendencia
ax.plot(df["Trimestre"], df["Año 1"], marker='o', color=colorA1, label="Año 1", linewidth=2, markersize=8)
ax.plot(df["Trimestre"], df["Año 2"], marker='o', color=colorA2, label="Año 2", linewidth=2, markersize=8)
ax.plot(df["Trimestre"], df["Año 3"], marker='o', color=colorA3, label="Año 3", linewidth=2, markersize=8)

#Lineas para ver los promedios
ax.axhline(media_año1, color=colorA1, linestyle='--', alpha=0.6, label=f"Prom. Año 1: {media_año1:.3f}")
ax.axhline(media_año2, color=colorA2, linestyle='--', alpha=0.6, label=f"Prom. Año 2: {media_año2:.3f}")
ax.axhline(media_año3, color=colorA3, linestyle='--', alpha=0.6, label=f"Prom. Año 3: {media_año3:.3f}")

#For para agregar los valores en cada punto
for i in range(len(df)):
    ax.annotate(f"{df['Año 1'][i]}", (df["Trimestre"][i], df["Año 1"][i]), textcoords="offset points", xytext=(0, 8), ha='center', color='white', fontsize=9)
    ax.annotate(f"{df['Año 2'][i]}", (df["Trimestre"][i], df["Año 2"][i]), textcoords="offset points", xytext=(0, 8), ha='center', color='white', fontsize=9)
    ax.annotate(f"{df['Año 3'][i]}", (df["Trimestre"][i], df["Año 3"][i]), textcoords="offset points", xytext=(0, 8), ha='center', color='white', fontsize=9)

ax.set_title("Rotación de Inventario por Trimestre (LMB) - Keneth Josue Varela Ruiz", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Trimestre", fontsize=11, labelpad=10)
ax.set_ylabel("Veces que rota el inventario", fontsize=11, labelpad=10)

ax.grid(True, linestyle='--', alpha=0.3)
ax.legend(loc="upper left", framealpha=0.3)
plt.tight_layout()
plt.show()