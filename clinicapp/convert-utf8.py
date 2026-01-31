# convertir_utf8.py
import json

# Leer con codificación Windows
with open('datadump.json', 'r', encoding='latin-1') as f:
    data = json.load(f)

# Escribir en UTF-8
with open('datadump_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Archivo convertido a UTF-8: datadump_utf8.json")