# Alumno: Isaias Muñoz Barrera.

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def obtener_datos_personaje(api_url, personaje_id):
    url = f"{api_url}/{personaje_id}"
    response = requests.get(url)

    if response.status_code == 200:
        datos_personaje = response.json()
        return datos_personaje
    else:
        print(f"Error al obtener datos del personaje {personaje_id} desde {api_url}. Código de estado: {response.status_code}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_buscado = request.form['nombre']
        datos_personaje_api1 = obtener_datos_personaje("https://dragonball-api.com/api/characters", nombre_buscado)
        datos_personaje_api2 = obtener_datos_personaje("https://dragonball-api.com/api/characters", nombre_buscado)

        if datos_personaje_api1 or datos_personaje_api2:
            return render_template('index.html', personaje=datos_personaje_api1 or datos_personaje_api2)
        else:
            return "Personaje no encontrado."
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
