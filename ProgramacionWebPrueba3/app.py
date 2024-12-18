from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    cantidad_caracteres = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = {nombre1: len(nombre1), nombre2: len(nombre2), nombre3: len(nombre3)}
        nombre_largo = max(nombres, key=nombres.get)
        cantidad_caracteres = nombres[nombre_largo]

    return render_template('ejercicio2.html', nombre_largo=nombre_largo, cantidad_caracteres=cantidad_caracteres)


if __name__ == '__main__':
    app.run(debug=True)

