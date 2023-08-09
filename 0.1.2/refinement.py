import csv

scores = []

def leer_scores(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar la cabecera
        for row in reader:
            if row:  # Verificar que la fila no esté vacía
                score = float(row[0])
                scores.append(score)
    return scores

secuencia = []

def generar_secuencia():
    precision_cobertura = []  # Lista para almacenar tuplas de precisión y cobertura
    for numero in range(101):
        resultado = [1 if score > numero else 0 for score in scores_column]
        precision = (resultado.count(1) / len(resultado)) * 100
        cobertura = (resultado.count(0) / len(resultado)) * 100
        precision_cobertura.append((precision, cobertura))
    return precision_cobertura

if __name__ == "__main__":
    archivo_scores = "scores/set/scores.csv"
    archivo_salida = "scores/interativeRefinement/precRecall.csv"
    
    # Leer la columna de scores desde el archivo CSV
    scores_column = leer_scores(archivo_scores)
    secuencia = generar_secuencia()

    with open(archivo_salida, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Cut Value", "Precision", "Recall"])
        for numero, (precision, cobertura) in enumerate(secuencia):
            writer.writerow([numero, precision, cobertura])
            #print(f"Cut Value: {numero}, Precision: {precision:.2f}%, Recall: {cobertura:.2f}%")

    print(f"Resultados guardados en '{archivo_salida}'")
