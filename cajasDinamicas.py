from flask import Flask, render_template
from flask import request
import forms 

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("indexCajas.html")

@app.route("/cajasDinamicas", methods=['GET', 'POST'])
def cajasDinamicas():
    cant= int(request.form.get('txtCant'))
    print("Cantidad", cant)
    #alum_form= forms.UserForm(request.form) # Aqui se crea el objeto de la clase UserForm
    if request.method == 'POST':
       # print("MATRICULA",alum_form.matricula.data)
       # print(alum_form.nombre.data)
       print("Cantidad", cant)
    return render_template("cajasDinamicas.html", cantidad=cant)
   # return render_template("Alumnos.html", form=alum_form)
   
@app.route("/resultadoCajas", methods=['GET', 'POST'])
def resultadoCajas():
    
    cant= request.form.get('txtCantidad')
    print("Cantidad RESULTADO", cant)
    if request.method == 'POST':
       for i in range(int(cant)):
        input=request.form.get('txt'+str(i+1))
        print("Numero", input)
   
    return render_template("resultadoCajas.html")
   # return render_template("Alumnos.html", form=alum_form)


if __name__ == "__main__":
    app.run(debug=True)