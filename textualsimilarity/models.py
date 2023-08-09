import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import subprocess

@csrf_exempt
@require_POST
def TextoSim(request):
    try:
        data = json.loads(request.body)
        originals = data.get('original', [])
        sospechosos = data.get('sospechoso', [])
        sim = data.get('sim', [])

        if isinstance(originals, list) and isinstance(sospechosos, list) and isinstance(sim, list):
            if len(originals) != len(sospechosos) or len(originals) != len(sim):
                raise ValueError("Las listas 'original', 'sospechoso' y 'sim' deben tener la misma longitud")

            corpus_response = []
            for original, sospechoso, sim_value in zip(originals, sospechosos, sim):
                response_item = {
                    'original': original,
                    'sospechoso': sospechoso,
                    'sim': sim_value
                }
                corpus_response.append(response_item)

                # Guardar los datos en el archivo CSV
                with open('0.1.2/corpus/unifiedCorpusInput.csv', mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:  # Si el archivo está vacío, escribir encabezados
                        writer.writerow(["Oración Original", "Oración Modificada", "Paráfrasis"])
                    writer.writerow([original, sospechoso, sim_value])

            # Ejecutar el comando
            try:
                subprocess.run(["python3.10", "0.1.2/linker.py","y", "y"], check=True)
                print("Comando ejecutado exitosamente")
            except subprocess.CalledProcessError as e:
                print("Error al ejecutar el comando:", e)

            # Generar respuesta desde el archivo CSV
            scores_response = generar_respuesta_desde_csv('0.1.2/scores/interativeRefinement/precRecall.csv')

            # Construir respuesta final
            final_response = {
                'corpus': corpus_response,
                'scores': scores_response
            }

            return JsonResponse(final_response, status=200, safe=False)
        else:
            raise ValueError("Los campos 'original', 'sospechoso' y 'sim' deben ser listas")

    except Exception as e:
        error_data = {'error': str(e)}
        return JsonResponse(error_data, status=500)

def generar_respuesta_desde_csv(csv_path):
    response_data = []

    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            response_item = {
                'Cut Value': int(row['Cut Value']),
                'Precision': float(row['Precision']),
                'Recall': float(row['Recall'])
            }
            response_data.append(response_item)

    return response_data
