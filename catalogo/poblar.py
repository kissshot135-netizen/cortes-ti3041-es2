import os
import sys
from pathlib import Path

import django

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalogo.models import Producto

productos = [
    {"nombre": "Martillo de Uña 16 oz", "categoria": "Herramientas Manuales", "precio": 8990, "stock": 25},
    {"nombre": "Destornillador Phillips PH2", "categoria": "Herramientas Manuales", "precio": 2490, "stock": 50},
    {"nombre": "Alicate Universal 8 pulgadas", "categoria": "Herramientas Manuales", "precio": 5990, "stock": 30},
    {"nombre": "Llave Ajustable 10 pulgadas", "categoria": "Herramientas Manuales", "precio": 7490, "stock": 20},
    {"nombre": "Sierra de Mano 20 pulgadas", "categoria": "Herramientas Manuales", "precio": 9990, "stock": 15},
    {"nombre": "Juego de Llaves Allen 9 piezas", "categoria": "Herramientas Manuales", "precio": 4990, "stock": 40},
    {"nombre": "Cincel Plano 12 mm", "categoria": "Herramientas Manuales", "precio": 3290, "stock": 18},
    {"nombre": "Cinta Métrica 5 metros", "categoria": "Medición", "precio": 3990, "stock": 60},
    {"nombre": "Nivel de Aluminio 24 pulgadas", "categoria": "Medición", "precio": 8490, "stock": 12},
    {"nombre": "Pie de Metro Digital", "categoria": "Medición", "precio": 14990, "stock": 10},
    {"nombre": "Taladro Percutor 650W", "categoria": "Herramientas Eléctricas", "precio": 34990, "stock": 14},
    {"nombre": "Esmeril Angular 4.5 pulgadas", "categoria": "Herramientas Eléctricas", "precio": 29990, "stock": 16},
    {"nombre": "Sierra Caladora 550W", "categoria": "Herramientas Eléctricas", "precio": 27990, "stock": 8},
    {"nombre": "Lijadora Orbital 200W", "categoria": "Herramientas Eléctricas", "precio": 22990, "stock": 11},
    {"nombre": "Pistola de Calor 1800W", "categoria": "Herramientas Eléctricas", "precio": 19990, "stock": 9},
    {"nombre": "Juego de Brocas para Concreto", "categoria": "Accesorios", "precio": 6990, "stock": 35},
    {"nombre": "Disco de Corte para Metal 4.5", "categoria": "Accesorios", "precio": 1290, "stock": 150},
    {"nombre": "Tornillo Drywall 1 5/8 (100 un)", "categoria": "Fijaciones", "precio": 2990, "stock": 80},
    {"nombre": "Tarugo Spit 6 mm (100 un)", "categoria": "Fijaciones", "precio": 1990, "stock": 100},
    {"nombre": "Perno Coche 3/8 x 3 (20 un)", "categoria": "Fijaciones", "precio": 4490, "stock": 45},
    {"nombre": "Clavo para Madera 2.5 (1 kg)", "categoria": "Fijaciones", "precio": 3190, "stock": 55},
    {"nombre": "Adhesivo de Contacto 250ml", "categoria": "Adhesivos", "precio": 3890, "stock": 28},
    {"nombre": "Silicona Transparente 280ml", "categoria": "Adhesivos", "precio": 3290, "stock": 42},
    {"nombre": "Espuma de Poliuretano 750ml", "categoria": "Adhesivos", "precio": 6490, "stock": 22},
    {"nombre": "Cinta Enmascarar 24mm x 50m", "categoria": "Pintura", "precio": 1590, "stock": 90},
    {"nombre": "Brocha Sintética 3 pulgadas", "categoria": "Pintura", "precio": 2290, "stock": 38},
    {"nombre": "Rodillo Antigota 18cm", "categoria": "Pintura", "precio": 3990, "stock": 25},
    {"nombre": "Esmalte al Agua Blanco 1 Galón", "categoria": "Pintura", "precio": 18990, "stock": 15},
    {"nombre": "Lija para Madera Grano 120", "categoria": "Abrasivos", "precio": 490, "stock": 200},
    {"nombre": "Cerradura de Pomo para Dormitorio", "categoria": "Cerrajería", "precio": 8990, "stock": 17},
    {"nombre": "Candado de Bronce 40mm", "categoria": "Cerrajería", "precio": 5490, "stock": 30},
    {"nombre": "Tubo PVC Hidráulico 20mm x 6m", "categoria": "Gasfitería", "precio": 4290, "stock": 40},
    {"nombre": "Llave de Paso 1/2 pulgada", "categoria": "Gasfitería", "precio": 4990, "stock": 26},
    {"nombre": "Cinta Teflón 12mm x 10m", "categoria": "Gasfitería", "precio": 590, "stock": 120},
    {"nombre": "Cable Eléctrico 1.5mm2 (100m)", "categoria": "Electricidad", "precio": 24990, "stock": 10},
    {"nombre": "Interruptor Simple Embutido", "categoria": "Electricidad", "precio": 18990, "stock": 50},
    {"nombre": "Enchufe Doble Embutido", "categoria": "Electricidad", "precio": 2190, "stock": 48},
    {"nombre": "Cinta Aisladora Negra 18m", "categoria": "Electricidad", "precio": 990, "stock": 85},
    {"nombre": "Guantes de Cabritilla Talla L", "categoria": "Seguridad", "precio": 34990, "stock": 60},
    {"nombre": "Lentes de Seguridad Transparentes", "categoria": "Seguridad", "precio": 1990, "stock": 75}
]

creados = 0
for item in productos:
    _, creado = Producto.objects.get_or_create(
        nombre=item["nombre"],
        categoria=item["categoria"],
        defaults={
            "precio": item["precio"],
            "stock": item["stock"],
        },
    )
    creados += int(creado)

print(
    f"Poblamiento completado: {creados} productos nuevos; "
    f"{Producto.objects.count()} productos en total."
)
