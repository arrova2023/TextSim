import os
import string

def normalize_words(words):
    # Eliminar signos de puntuación y convertir a minúsculas
    translator = str.maketrans('', '', string.punctuation)
    normalized_words = [word.translate(translator).lower() for word in words]
    return normalized_words

def normalize_and_save():
    input_dir = "corpus/"
    output_dir = "corpus/normalized/"

    # Leer palabras de oracion1.txt y almacenar en un array
    with open(os.path.join(input_dir, "original.txt"), "r", encoding="utf-8") as file1:
        oracion1_words = file1.read().split()

    # Leer palabras de oracion2.txt y almacenar en otro array
    with open(os.path.join(input_dir, "sospechoso.txt"), "r", encoding="utf-8") as file2:
        oracion2_words = file2.read().split()

    # Normalizar las palabras
    oracion1_normalized = normalize_words(oracion1_words)
    oracion2_normalized = normalize_words(oracion2_words)

    # Crear archivos de texto normalizados
    with open(os.path.join(output_dir, "original.txt"), "w", encoding="utf-8") as file1:
        file1.write(" ".join(oracion1_normalized))

    with open(os.path.join(output_dir, "sospechoso.txt"), "w", encoding="utf-8") as file2:
        file2.write(" ".join(oracion2_normalized))

if __name__ == "__main__":
    normalize_and_save()
