import os

def read_stopwords(file_path):
    stopwords = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            stopwords.append(line.strip())
    return stopwords

def read_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
    return words

def filter_stopwords(words, stopwords):
    return [word for word in words if word not in stopwords]

if __name__ == "__main__":
    stopwords_file_path = "resources/stopwords/stopwords.txt"

    # Leer stopwords desde el archivo
    stopwords = read_stopwords(stopwords_file_path)

    # Imprimir todas las palabras funcionales separadas por coma
    #print(", ".join(stopwords))

    original_file_path = "corpus/lemmatized/original.txt"
    sospechoso_file_path = "corpus/lemmatized/sospechoso.txt"

    # Leer palabras de 'original.txt' y almacenar en un array
    original_words = read_words_from_file(original_file_path)

    # Leer palabras de 'sospechoso.txt' y almacenar en otro array
    sospechoso_words = read_words_from_file(sospechoso_file_path)

    # Eliminar las palabras funcionales de los arrays
    original_filtered = filter_stopwords(original_words, stopwords)
    sospechoso_filtered = filter_stopwords(sospechoso_words, stopwords)

    # Guardar los arrays filtrados en nuevos archivos
    filtered_dir = "corpus/filtered/"
    os.makedirs(filtered_dir, exist_ok=True)

    original_filtered_file = os.path.join(filtered_dir, "original.txt")
    sospechoso_filtered_file = os.path.join(filtered_dir, "sospechoso.txt")

    with open(original_filtered_file, "w", encoding="utf-8") as file:
        file.write(" ".join(original_filtered))

    with open(sospechoso_filtered_file, "w", encoding="utf-8") as file:
        file.write(" ".join(sospechoso_filtered))

