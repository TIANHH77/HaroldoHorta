import os
import sys

def test_environment():
    # Verificar versión de Python
    print("Versión de Python:", sys.version)

    # Verificar que librerías clave estén disponibles
    try:
        import pandas as pd
        import PIL
        print("✅ Librerías pandas y Pillow disponibles")
    except ImportError as e:
        print("❌ Falta una librería:", e)

    # Verificar que el script principal exista
    if os.path.exists("src/consolidar_inventario.py"):
        print("✅ Script consolidar_inventario.py encontrado")
    else:
        print("❌ Script consolidar_inventario.py no encontrado")

if __name__ == "__main__":
    test_environment()
