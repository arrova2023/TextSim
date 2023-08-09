from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
import subprocess
import requests
from django.http import JsonResponse
import os
import json
from django.db import models
from .models import TextoSim

from django.views.decorators.csrf import csrf_exempt
from .models import TextoSim

def api_view(request):
    return render(request, 'api.html')
    
@csrf_exempt
def procesar_textos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        resultados = []
        for item in data:
            original = item.get('original', '')
            sospechoso = item.get('sospechoso', '')
            sim = item.get('sim', 0.0)
            
            texto_sim = TextoSim(original=original, sospechoso=sospechoso, sim=sim)
            texto_sim.save()
            
            resultados.append({
                'original': original,
                'sospechoso': sospechoso,
                'sim': sim
            })
        
        return JsonResponse(resultados, safe=False)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def consumir_hola_mundo_json(request):
    response = requests.get("http://localhost:8000/hola_mundo_json/")

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Error al consumir el servicio"})

def hola_mundo_json(request):
    response_data = {'message': 'Hola mundo'}
    return JsonResponse(response_data)
    
def hola_mundo(request):
    return HttpResponse("¡Hola mundo en Django!")

def mostrar_tabla(request):
    return render(request, 'table.html')

def guardar_contenido(request):
    mensaje = None
    if request.method == 'POST':
        oracion1 = request.POST.get('oracion1', '')
        oracion2 = request.POST.get('oracion2', '')

        corpus_path = os.path.join(settings.BASE_DIR, '0.1.2/corpus')
        if not os.path.exists(corpus_path):
            os.makedirs(corpus_path)

        with open(os.path.join(corpus_path, 'original.txt'), 'w', encoding='utf-8') as original_file:
            original_file.write(oracion1)

        with open(os.path.join(corpus_path, 'sospechoso.txt'), 'w', encoding='utf-8') as sospechoso_file:
            sospechoso_file.write(oracion2)

        mensaje = 'Archivos original.txt y sospechoso.txt creados correctamente.'

        # Execute main.py using subprocess
        main_script_path = os.path.join(settings.BASE_DIR, '0.1.2/main.py')
        subprocess.run(['python3.10', main_script_path])
        
        # Redireccionar a la vista dashboard después de guardar los archivos
        return redirect('dashboard')

    return render(request, 'dashboard.html', {'mensaje': mensaje})

def dashboard(request):
    # Leer el contenido del archivo similarity.res
    file_path = '0.1.2/scores/similarity/similarity.res'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            score = float(content.strip())
    except FileNotFoundError:
        score = 0.0

    # Renderizar el template con el valor del score
    return render(request, 'dashboard.html', {'score': score})

def bienvenida_pln(request):
    return render(request, 'index.html')
