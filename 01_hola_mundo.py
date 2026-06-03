import json
from datetime import datetime

#Ejemplo de procesamiento de datos de llamadas telefónicas
datos_llamadas = [
    {"id": 1, "fecha": "2024-06-01T10:00:00", "duracion": 300, "tipo": "saliente"},
    {"id": 2, "fecha": "2024-06-01T11:00:00", "duracion": 200, "tipo": "entrante"},
    {"id": 3, "fecha": "2024-06-01T12:00:00", "duracion": 400, "tipo": "saliente"}
]


sumatoria_duraciones = sum(llamada["duracion"] for llamada in datos_llamadas)
print(f"La sumatoria de las duraciones de las llamadas es: {sumatoria_duraciones} segundos")


llamadas_entrantes = [llamada for llamada in datos_llamadas if llamada["tipo"] == "entrante"]
print(f"Las llamadas entrantes son: {len(llamadas_entrantes)}")

reporte = {
    "total_llamadas": len(datos_llamadas),
    "duracion_total": sumatoria_duraciones,
    "llamadas_entrantes": len(llamadas_entrantes)
}   

# Guardar el reporte en un archivo JSON
with open("reporte_diario.json", "w", encoding="utf-8") as f:
    json.dump(reporte, f, indent=4, ensure_ascii=False)
