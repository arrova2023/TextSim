import csv
import spacy

def leer_corpus_unificado_input(file_path):
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

def lemmatize_sentence(sentence):
    nlp = spacy.load("es_core_news_lg")
    doc = nlp(sentence)
    lemmatized_sentence = " ".join(token.lemma_ for token in doc)
    return lemmatized_sentence

def lemmatize_arrays(original, sospechoso):
    lemmatized_original = [lemmatize_sentence(sentence) for sentence in original]
    lemmatized_sospechoso = [lemmatize_sentence(sentence) for sentence in sospechoso]
    return lemmatized_original, lemmatized_sospechoso

def guardar_corpus_lemmatizado(file_path, cabeceras, lemmatized_original, lemmatized_sospechoso):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(cabeceras)  # Escribir las cabeceras originales
        for row in zip(lemmatized_original, lemmatized_sospechoso):
            writer.writerow(row)

if __name__ == "__main__":
    archivo_corpus_filtrado = "corpus/filtered/unifieds/corpus.csv"
    archivo_corpus_lemmatizado = "corpus/lemmatized/unifieds/corpus.csv"

    # Leer el archivo corpus filtrado y almacenar cada columna en un array
    original, sospechoso = leer_corpus_unificado_input(archivo_corpus_filtrado)

    # Lemmatizar los arrays
    lemmatized_original, lemmatized_sospechoso = lemmatize_arrays(original, sospechoso)

    # Leer las cabeceras originales
    with open(archivo_corpus_filtrado, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        cabeceras = next(reader)

    # Guardar el contenido lemmatizado en un nuevo archivo
    guardar_corpus_lemmatizado(archivo_corpus_lemmatizado, cabeceras, lemmatized_original, lemmatized_sospechoso)

    # Imprimir un mensaje de éxito
    print("El corpus ha sido lematizado y guardado en", archivo_corpus_lemmatizado)
