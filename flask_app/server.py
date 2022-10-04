from flask import Flask, render_template, request, redirect
# importar la clase de usuario.py
from usuario import Usuario
app = Flask(__name__)

@app.route("/usuarios")
def usuarios():
	# llamar al método de clase get all para obtener todos los usuarios
	usuarios = Usuario.get_all()
	print(usuarios)
	return render_template("usuarios.html", usuarios=usuarios)


@app.route('/usuarios/nuevo', methods=["POST"])
def nuevo():
	# Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
	# Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
	data = {
		"nombre": request.form["nombre"],
		"apellido" : request.form["apellido"],
		"email" : request.form["email"]
	}
	# Pasamos el diccionario de datos al método save de la clase Friend
	Usuario.save(data)
	# No olvides redirigir después de guardar en la base de datos
	return redirect('/usuarios')

@app.route('/usuarios/nuevo', methods=["GET"])
def nuevo_form():
	return render_template("nuevo.html")

if __name__ == "__main__":
	app.run(debug=True)