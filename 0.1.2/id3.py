import os

def read_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
    return words

def count_unique_elements(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    unique_elements = set1.symmetric_difference(set2)
    return len(unique_elements)

if __name__ == "__main__":
    lemmatized_dir = "corpus/lemmatized/"
    normalized_dir = "corpus/normalized/"

    # Leer palabras de 'original.txt' en lemmatized y almacenar en un array
    original_file_path_lemmatized = os.path.join(lemmatized_dir, "original.txt")
    original_lemmatized = read_words_from_file(original_file_path_lemmatized)

    # Leer palabras de 'original.txt' en normalized y almacenar en otro array
    original_file_path_normalized = os.path.join(normalized_dir, "original.txt")
    original_normalized = read_words_from_file(original_file_path_normalized)

    # Leer palabras de 'sospechoso.txt' en lemmatized y almacenar en un array
    sospechoso_file_path_lemmatized = os.path.join(lemmatized_dir, "sospechoso.txt")
    sospechoso_lemmatized = read_words_from_file(sospechoso_file_path_lemmatized)

    # Leer palabras de 'sospechoso.txt' en normalized y almacenar en otro array
    sospechoso_file_path_normalized = os.path.join(normalized_dir, "sospechoso.txt")
    sospechoso_normalized = read_words_from_file(sospechoso_file_path_normalized)

    # Calcular la cantidad de elementos distintos entre los arrays original lemmatized y original normalized
    count_distinct_elements_original = count_unique_elements(original_lemmatized, original_normalized)

    # Calcular la cantidad de elementos distintos entre los arrays sospechoso lemmatized y sospechoso normalized
    count_distinct_elements_sospechoso = count_unique_elements(sospechoso_lemmatized, sospechoso_normalized)

    # Obtener el menor y mayor número de elementos únicos y restarlos
    min_elements = min(count_distinct_elements_original, count_distinct_elements_sospechoso)
    max_elements = max(count_distinct_elements_original, count_distinct_elements_sospechoso)
    result = max_elements - min_elements

    # Guardar el resultado en el archivo entropy.res
    output_dir = "scores/entropy/"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, "entropy.res")
    with open(output_file_path, "w") as output_file:
        output_file.write(str(result))

    #print(f"Resultado: {result}")
