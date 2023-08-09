import os

def read_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def calculate_jaccard_index(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    intersection_size = len(words1.intersection(words2))
    union_size = len(words1.union(words2))
    jaccard_index = intersection_size / union_size
    return jaccard_index

if __name__ == "__main__":
    filtered_dir = "corpus/filtered/"

    # Leer texto de 'original.txt'
    original_file_path = os.path.join(filtered_dir, "original.txt")
    original_text = read_text_from_file(original_file_path)

    # Leer texto de 'sospechoso.txt'
    sospechoso_file_path = os.path.join(filtered_dir, "sospechoso.txt")
    sospechoso_text = read_text_from_file(sospechoso_file_path)

    # Calcular el índice de Jaccard
    jaccard_index = calculate_jaccard_index(original_text, sospechoso_text)

    # Calcular la distancia de Jaccard
    jaccard_distance = 1 - jaccard_index

    # Guardar la distancia de Jaccard en el archivo temperature.res
    output_dir = "scores/temperature/"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, "temperature.res")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(str(jaccard_distance))
