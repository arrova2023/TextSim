import csv

def leer_resultados(file_path):
    resultados = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar la cabecera
        for row in reader:
            if row:  # Verificar que la fila no esté vacía
                cut_value = int(row[0])
                precision = float(row[1])
                recall = float(row[2])
                resultados.append((cut_value, precision, recall))
    return resultados

if __name__ == "__main__":
    archivo_resultados = "scores/interativeRefinement/precRecall.csv"
    
    resultados = leer_resultados(archivo_resultados)
    print("Cut Value | Precision | Recall")
    print("-" * 30)
    for cut_value, precision, recall in resultados:
        print(f"{cut_value:9} | {precision:.2f}%    | {recall:.2f}% | {recall+precision:.2f}%")
