import csv
import string
import spacy

def leer_corpus_unificado_input(file_path):
    original = []
    sospechoso = []
    similar = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar las cabeceras
        for row in reader:
            if len(row) >= 3:  # Verificar que la fila tenga al menos tres elementos
                original.append(row[0])
                sospechoso.append(row[1])
                similar.append(row[2])
    return original, sospechoso, similar

def guardar_corpus_filtrado(file_path, original, sospechoso):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Original", "Sospechoso"])  # Escribir las nuevas cabeceras
        for row in zip(original, sospechoso):
            writer.writerow(row)

def guardar_scores(file_path, similar):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Similar"])  # Escribir la cabecera
        for value in similar:
            writer.writerow([value])

def procesar_corpus(corpus):
    nlp = spacy.load("es_core_news_lg")
    cleaned_corpus = []
    for sentence in corpus:
        sentence = sentence.lower()  # Pasar todo a minúsculas
        # Eliminar signos de puntuación
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))
        doc = nlp(sentence)
        lemmatized_sentence = " ".join(token.lemma_ for token in doc if not token.is_stop)
        cleaned_corpus.append(lemmatized_sentence)
    return cleaned_corpus

if __name__ == "__main__":
    archivo_corpus_input = "corpus/unifiedCorpusInput.csv"
    archivo_corpus_filtrado = "corpus/corpus.csv"
    archivo_scores = "scores/booleans/scores.csv"
    
    # Leer el archivo corpus unificado input y almacenar cada columna en un array
    original, sospechoso, similar = leer_corpus_unificado_input(archivo_corpus_input)
    
    # Procesar el corpus y eliminar stopwords, pasar a minúsculas y eliminar signos de puntuación
    cleaned_original = procesar_corpus(original)
    cleaned_sospechoso = procesar_corpus(sospechoso)
    
    # Guardar el contenido de las columnas "Original" y "Sospechoso" en un nuevo archivo
    guardar_corpus_filtrado(archivo_corpus_filtrado, cleaned_original, cleaned_sospechoso)

    # Guardar la tercera columna "Similar" en el archivo scores
    guardar_scores(archivo_scores, similar)
