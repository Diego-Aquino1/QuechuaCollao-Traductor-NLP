import re

data = []

with open('new_data/normalized_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            data.append(line)

english_texts = []
quechua_texts = []

for line in data:
    match = re.match(r'"([^"]+)" "([^"]+)"', line)
    if match:
        english = match.group(1).strip()
        quechua = match.group(2).strip()
        english_texts.append(english)
        quechua_texts.append(quechua)

# Escribir los resultados en archivos de texto
with open('new_data/english_regex.txt', 'w', encoding='utf-8') as file:
    for text in english_texts:
        file.write(text + '\n')

with open('new_data/quechua_regex.txt', 'w', encoding='utf-8') as file:
    for text in quechua_texts:
        file.write(text + '\n')

print("Archivos de texto generados correctamente usando expresiones regulares.")