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
    f1_scores = []  # Lista para almacenar los valores del F1-score
    for numero in range(101):
        resultado = [1 if score > numero else 0 for score in scores_column]
        true_positive = resultado.count(1)
        false_positive = len(resultado) - true_positive
        false_negative = 0  # Suponemos que no hay falsos negativos en este contexto
        precision = (true_positive / (true_positive + false_positive)) if true_positive + false_positive != 0 else 0
        recall = (true_positive / (true_positive + false_negative)) if true_positive + false_negative != 0 else 0
        f1_score = (2 * precision * recall) / (precision + recall) if precision + recall != 0 else 0
        f1_scores.append(f1_score)
    return f1_scores

if __name__ == "__main__":
    archivo_scores = "scores/set/scores.csv"
    
    # Leer la columna de scores desde el archivo CSV
    scores_column = leer_scores(archivo_scores)
    f1_scores = generar_secuencia()

    for numero, f1_score in enumerate(f1_scores):
        print(f"Cut Value: {numero}, F1-score: {f1_score:.2f}")
