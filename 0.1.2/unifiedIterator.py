import csv
import subprocess

def leer_corpus_filtrado(file_path):
    original = []
    sospechoso = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar las cabeceras
        for row in reader:
            if len(row) >= 2:  # Verificar que la fila tenga al menos dos elementos
                original.append(row[0])
                sospechoso.append(row[1])
    return original, sospechoso

def obtener_energy_result():
    try:
        with open("scores/energy/energy.res", "r") as file:
            result = file.read().strip()
            energy_result = float(result)
            return energy_result
    except (FileNotFoundError, ValueError):
        return None

def obtener_entropy_result():
    try:
        with open("scores/entropy/entropy.res", "r") as file:
            result = file.read().strip()
            entropy_result = float(result)
            #print(entropy_result)
            return entropy_result
    except (FileNotFoundError, ValueError):
        return None

def obtener_temperature_result():
    try:
        with open("scores/temperature/temperature.res", "r") as file:
            result = file.read().strip()
            temperature_result = float(result)
            return temperature_result
    except (FileNotFoundError, ValueError):
        return None

def obtener_energy_min_result():
    try:
        with open("scores/similarity/similarity.res", "r") as file:
            result = file.read().strip()
            energy_min_result = float(result)
            return energy_min_result
    except (FileNotFoundError, ValueError):
        return None


if __name__ == "__main__":
    archivo_corpus_filtrado = "corpus/corpus.csv"
    
    # Leer el archivo corpus filtrado y almacenar cada columna en un array
    original, sospechoso = leer_corpus_filtrado(archivo_corpus_filtrado)

    # Crear los arrays scores para energy, entropy, temperature y energyMin
    scores_energy = []
    scores_entropy = []
    scores_temperature = []
    scores_min = []

    # Calcular el promedio del tamaño de ambos arrays
    average_length = (len(original) + len(sospechoso)) // 2

    # Iterar para la cantidad de veces del promedio
    for i in range(average_length):
        # Acceder al elemento correspondiente en original y sospechoso
        score_original = original[i]
        score_sospechoso = sospechoso[i]

        # Guardar los elementos en los archivos correspondientes
        with open(f"corpus/filtered/original.txt", "w", encoding="utf-8") as original_file:
            original_file.write(score_original)

        with open(f"corpus/filtered/sospechoso.txt", "w", encoding="utf-8") as sospechoso_file:
            sospechoso_file.write(score_sospechoso)

        # Ejecutar matrix.py para obtener el resultado de energy.res
        subprocess.run(["python3.10", "matrix.py"])

        # Obtener el resultado de energy.res y almacenarlo en el array scores_energy
        energy_result = obtener_energy_result()
        if energy_result is not None:
            scores_energy.append(energy_result)

        # Ejecutar id3.py para obtener el resultado de entropy.res
        subprocess.run(["python3.10", "id3.py"])

        # Obtener el resultado de entropy.res y almacenarlo en el array scores_entropy
        entropy_result = obtener_entropy_result()
        if entropy_result is not None:
            scores_entropy.append(entropy_result)

        # Ejecutar temperature.py para obtener el resultado de temperature.res
        subprocess.run(["python3.10", "temperature.py"])

        # Obtener el resultado de temperature.res y almacenarlo en el array scores_temperature
        temperature_result = obtener_temperature_result()
        if temperature_result is not None:
            scores_temperature.append(temperature_result)

        # Ejecutar energyMin.py para obtener el resultado de similarity.res
        subprocess.run(["python3.10", "energyMin.py"])

        # Obtener el resultado de similarity.res y almacenarlo en el array scores_min
        energy_min_result = obtener_energy_min_result()
        if energy_min_result is not None:
            scores_min.append(energy_min_result)

# Guardar el array scores_min en un archivo CSV
with open("scores/set/scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Score"])  # Escribir la cabecera
    for score in scores_min:
        writer.writerow([score])


