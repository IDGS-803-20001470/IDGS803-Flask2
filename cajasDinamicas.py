from flask import Flask, render_template
from flask import request
import forms

app = Flask(__name__)


@app.route("/")
def formulario():
    return render_template("indexCajas.html")


@app.route("/cajasDinamicas", methods=['GET', 'POST'])
def cajasDinamicas():
    cant = int(request.form.get('txtCant'))
    print("Cantidad", cant)
    # alum_form= forms.UserForm(request.form) # Aqui se crea el objeto de la clase UserForm
    if request.method == 'POST':
        # print("MATRICULA",alum_form.matricula.data)
        # print(alum_form.nombre.data)
        print("Cantidad", cant)
    return render_template("cajasDinamicas.html", cantidad=cant)
   # return render_template("Alumnos.html", form=alum_form)


@app.route("/resultadoCajas", methods=['GET', 'POST'])
def resultadoCajas():

    cant = request.form.get('txtCantidad')
    inp = 1
    igualdad = 0
    nums = []
    valoresUnicos = []

    if request.method == 'POST':
        for i in range(int(cant)):
            input = request.form.get('txt'+str(i+1))
            nums.append(int(input))
    print("lista de numeros", nums)
    norep = list(set(nums))
    print("lista de numeros sin repetir", norep)

    for z in range(len(norep)):
        print(" Es el numero", norep[z])
        rep1 = nums.count(norep[z])
        print("El numero ", norep[z], "se repite", rep1)
   # [valoresUnicos.append(nums) for numero in nums if numero not in valoresUnicos]
   # print("valores unicos", valoresUnicos)
   
    longitud = int(len(norep))
    print("longitud", longitud)
    longNums = int(len(nums))
    mini= min(nums)
    maximo= max(nums)


   # operaciones

    return render_template("resultadoCajas.html", nums=nums, norep=norep, longitud=longitud, longNums=longNums, mini=mini, maxi=maximo)
   # return render_template("Alumnos.html", form=alum_form)


if __name__ == "__main__":
    app.run(debug=True)
