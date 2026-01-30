import pandas as pd
import folium

# Cargar el inventario
df = pd.read_csv("D:/LEGADO_HAROLDO/inventario_haroldo.csv")

# Crear mapa centrado en la primera coordenada válida
lat_init = df['latitud'].dropna().iloc[0]
lon_init = df['longitud'].dropna().iloc[0]
m = folium.Map(location=[lat_init, lon_init], zoom_start=6)

# Agregar marcadores por cada foto con coordenadas
for _, row in df.dropna(subset=['latitud','longitud']).iterrows():
    folium.Marker(
        location=[row['latitud'], row['longitud']],
        popup=f"{row['archivo']} ({row['fecha']})",
        tooltip=row['camara']
    ).add_to(m)

# Guardar mapa como HTML
m.save("D:/LEGADO_HAROLDO/mapa_fotos.html")
