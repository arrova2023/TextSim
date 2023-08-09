import os

def read_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
    return words

if __name__ == "__main__":
    filtered_dir = "corpus/filtered/"

    # Leer palabras de 'original.txt' y almacenar en un array
    original_file_path = os.path.join(filtered_dir, "original.txt")
    original = read_words_from_file(original_file_path)

    # Leer palabras de 'sospechoso.txt' y almacenar en otro array
    sospechoso_file_path = os.path.join(filtered_dir, "sospechoso.txt")
    sospechoso = read_words_from_file(sospechoso_file_path)

    # Calcular el tamaño promedio de los arrays
    average_size = (len(original) + len(sospechoso)) / 2

    # Crear matriz de activación
    matrix = [[1 if x == y else 0 for y in sospechoso] for x in original]

    # Calcular el tamaño de la diagonal principal
    diagonal_size = sum(matrix[i][i] for i in range(min(len(original), len(sospechoso))))

    # Calcular el índice del 0 al 100
    index = (diagonal_size / average_size) * 100

    # Mostrar el índice
    #print(f"Índice: {index}")

    # Guardar el resultado en el archivo scores.res
    scores_dir = "scores/energy/"
    os.makedirs(scores_dir, exist_ok=True)
    scores_file_path = os.path.join(scores_dir, "energy.res")
    with open(scores_file_path, "w") as scores_file:
        scores_file.write(f"{index}\n")
