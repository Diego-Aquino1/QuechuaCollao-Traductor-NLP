import re
import unicodedata
import nltk
from nltk.corpus import stopwords

# Asegúrate de descargar las stopwords la primera vez que ejecutes el script
nltk.download('stopwords')

# Stop words en español y quechua (agrega más si es necesario)
stop_words_spanish = set(stopwords.words('spanish'))
stop_words_quechua = {"kay", "manan", "chay", "wasin", "wasi"}

# Combina ambas listas de stop words
stop_words_combined = stop_words_spanish.union(stop_words_quechua)

def remove_non_ascii(text):
    return ''.join(c for c in text if ord(c) < 128)

def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    return text

def remove_punctuation(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_stopwords(text, stop_words):
    words = text.split()
    cleaned_text = ' '.join(word for word in words if word not in stop_words)
    return cleaned_text

def clean_text(text):
    text = normalize_text(text)
    text = remove_non_ascii(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text, stop_words_combined)
    return text

def clean_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    cleaned_lines = [clean_text(line) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(cleaned_lines))

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    clean_file(input_file, output_file)
    print(f"Archivo limpiado guardado como {output_file}")
