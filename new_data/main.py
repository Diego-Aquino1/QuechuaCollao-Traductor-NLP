
# with open('unnormalize_data.txt', 'r', encoding='utf-8') as file:
#     lineas = file.readlines()

# with open('normalize_data.txt', 'w', encoding='utf-8') as file:
#     for linea in lineas:
#         if linea.strip().startswith('"'):
#             file.write(linea)

with open('new_data/normalize_data.txt', 'r', encoding='utf-8') as file:
    lineas = file.readlines()

# English
# with open('new_data/only_english_data.txt', 'w', encoding='utf-8') as file:
#     for linea in lineas:
#         columnas = linea.split('"')
#         if len(columnas) > 1:
#             columna_derecha = columnas[1]
#             file.write(columna_derecha + '\n')

# Quechua
with open('new_data/only_quechua_data.txt', 'w', encoding='utf-8') as file:
    for linea in lineas:
        columnas = linea.split('"')
        if len(columnas) > 1:
            columna_derecha = columnas[3]
            file.write(columna_derecha + '\n')