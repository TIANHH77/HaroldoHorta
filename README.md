📖 Narrativa

Este repositorio busca recuperar y organizar el legado fotográfico de Haroldo Horta, fotógrafo y piloto chileno que ha dedicado más de 30 años a registrar el mundo desde el aire y en contextos históricos clave:

Corresponsal de guerra en Nicaragua y Colombia, con imágenes de la revolución sandinista y conflictos armados.
Fotografía aérea en Perú, incluyendo el secuestro en la embajada de Japón.
Proyectos artísticos como Atacamafoto, Atacamamazing y Kactus Foto, documentando el desierto de Atacama, los faros de Chile y expediciones a la Antártida.
Vive Volando Nómade, su proyecto más reciente, donde combina vuelos en paramotor y ultraligero con fotografía aérea y video 8K.

Este repositorio es un intento de ordenar, consolidar y devolver a las pistas ese archivo disperso, transformándolo en un mapa vivo de memoria y territorio.


🎯 Objetivo
Consolidar las fotos en un disco de 28 TB, evitando duplicados y ordenando por fecha.
Inventariar cada imagen con metadatos: fecha, cámara y coordenadas GPS.
Visualizar el archivo en mapas y dashboards interactivos, preparando el terreno para haroldohorta.com.

https://www.latercera.com/diario-impreso/una-vida-de-alto-vuelo/?utm_source=copilot.com

Legado-Haroldo/
│
├── README.md                # Explicación del proyecto, propósito, cómo usar los scripts
├── requirements.txt         # Librerías necesarias (pandas, Pillow, sqlite3, etc.)
├── .gitignore               # Ignorar archivos pesados (ej. fotos, CSV grandes, DB)
│
├── src/                     # Código fuente
│   ├── consolidar_inventario.py   # Script principal (consolidación + inventario + GPS)
│   ├── utils.py             # Funciones auxiliares (hash, exif, gps) si quieres modularizar
│
├── data/                    # Archivos generados
│   ├── inventario_haroldo.csv     # Inventario con metadata
│   └── indice_fotos.db            # Base de datos SQLite con hashes
│
├── docs/                    # Documentación adicional
│   └── flujo.md             # Explicación del pipeline, pasos y mantras
│
└── tests/                   # Carpeta opcional para pruebas unitarias

