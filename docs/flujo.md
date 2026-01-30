# Flujo de consolidación e inventario

1. **Consolidar**: recorrer disco origen, calcular hash, evitar duplicados, copiar fotos a destino ordenadas por año/mes.
2. **Inventariar**: extraer metadatos EXIF (fecha, cámara, GPS).
3. **Guardar**: registrar en SQLite y generar CSV.
4. **Visualizar**: usar Streamlit o Plotly para mostrar inventario en mapas y dashboards.
