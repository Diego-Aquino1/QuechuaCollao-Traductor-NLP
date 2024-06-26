def clean_lines(filepath, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')

    cleaned_lines = [line.replace('[start] ', '').replace(' [end]', '') for line in lines]

    with open(output_filepath, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

# Rutas a los archivos
input_filepath = 'TEST_METRIC/1_Albert.txt'  # Archivo original con los tokens [start] y [end]
output_filepath = 'TEST_METRIC/1_Albert_clean.txt'  # Archivo de salida con los tokens limpiados

# Llamar a la función para limpiar las líneas y guardar el resultado
clean_lines(input_filepath, output_filepath)

print(f"Líneas limpiadas guardadas en {output_filepath}")