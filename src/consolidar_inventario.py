import os, shutil, sqlite3, hashlib, pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime

# DB en el disco de 28TB
conn = sqlite3.connect('E:/LEGADO_HAROLDO/indice_fotos.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS fotos (hash TEXT PRIMARY KEY, ruta TEXT, fecha TEXT)')

def generar_hash(ruta):
    hasher = hashlib.md5()
    with open(ruta, 'rb') as f:
        while buf := f.read(65536): hasher.update(buf)
    return hasher.hexdigest()

def get_exif_data(path_imagen):
    try:
        img = Image.open(path_imagen)
        info = img._getexif()
        if not info: return None
        exif = {TAGS.get(tag, tag): value for tag, value in info.items()}
        gps_info = {}
        if "GPSInfo" in exif:
            for key in exif["GPSInfo"].keys():
                gps_info[GPSTAGS.get(key, key)] = exif["GPSInfo"][key]
            exif["GPSInfo"] = gps_info
        return exif
    except: return None

def get_decimal_coords(gps_info):
    def convert(value):
        d, m, s = value
        return d[0]/d[1] + (m[0]/m[1])/60 + (s[0]/s[1])/3600
    try:
        lat = convert(gps_info["GPSLatitude"])
        if gps_info["GPSLatitudeRef"] == "S": lat = -lat
        lon = convert(gps_info["GPSLongitude"])
        if gps_info["GPSLongitudeRef"] == "W": lon = -lon
        return lat, lon
    except: return None, None

def consolidar_e_inventariar(origen, destino):
    registros = []
    for root, _, files in os.walk(origen):
        for f in files:
            if f.lower().endswith(('.jpg','.jpeg','.cr2','.nef')):
                ruta_orig = os.path.join(root, f)
                h = generar_hash(ruta_orig)
                cursor.execute("SELECT hash FROM fotos WHERE hash=?", (h,))
                if cursor.fetchone(): continue

                # Fecha
                try:
                    img = Image.open(ruta_orig)
                    exif = img._getexif()
                    fecha_str = exif.get(36867) if exif else None
                    dt = datetime.strptime(fecha_str[:10], "%Y:%m:%d") if fecha_str else datetime.fromtimestamp(os.path.getmtime(ruta_orig))
                except: dt = datetime.fromtimestamp(os.path.getmtime(ruta_orig))

                # Carpeta destino
                ruta_dest_dir = os.path.join(destino, str(dt.year), f"{dt.month:02d}")
                os.makedirs(ruta_dest_dir, exist_ok=True)
                ruta_final = os.path.join(ruta_dest_dir, f)
                shutil.copy2(ruta_orig, ruta_final)

                # Guardar en DB
                cursor.execute("INSERT INTO fotos VALUES (?, ?, ?)", (h, ruta_final, dt.isoformat()))
                conn.commit()

                # Extraer metadata
                exif_data = get_exif_data(ruta_final)
                lat, lon = (None, None)
                if exif_data and "GPSInfo" in exif_data:
                    lat, lon = get_decimal_coords(exif_data["GPSInfo"])
                registros.append({
                    "archivo": f,
                    "ruta": ruta_final,
                    "fecha": exif_data.get("DateTimeOriginal") if exif_data else dt.isoformat(),
                    "camara": exif_data.get("Model") if exif_data else "N/A",
                    "latitud": lat,
                    "longitud": lon
                })
    pd.DataFrame(registros).to_csv('inventario_haroldo.csv', index=False)
    print("Consolidación + inventario terminado.")

# Uso:
# consolidar_e_inventariar('D:/', 'E:/LEGADO_HAROLDO')
