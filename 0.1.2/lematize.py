import os
import spacy

def lemmatize_sentence(sentence):
    nlp = spacy.load("es_core_news_lg")
    doc = nlp(sentence)
    lemmatized_sentence = " ".join(token.lemma_ for token in doc)
    return lemmatized_sentence

def lemmatize_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.startswith('.'):
            # Omitir archivos ocultos como .DS_Store
            continue

        input_file = os.path.join(input_dir, filename)

        with open(input_file, "rb") as file:  # Abrir en modo binario
            content = file.read()

        # Decodificar como UTF-8
        try:
            sentence = content.decode("utf-8")
        except UnicodeDecodeError:
            print(f"Error al decodificar el archivo: {input_file}")
            continue

        lemmatized_sentence = lemmatize_sentence(sentence)

        if filename == "original.txt":
            output_file = os.path.join(output_dir, "original.txt")
        elif filename == "sospechoso.txt":
            output_file = os.path.join(output_dir, "sospechoso.txt")
        else:
            continue

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(lemmatized_sentence)

if __name__ == "__main__":
    input_dir = "corpus/normalized/"
    output_dir = "corpus/lemmatized/"
    lemmatize_files(input_dir, output_dir)
