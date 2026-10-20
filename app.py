from flask import Flask

app = Flask(__Sebastian Hurtado Flores__)


@app.route("/")
def inicio():
    return "¡Hola! Esta aplicación Flask fue desplegada en Render por [TU NOMBRE]."


if __name__ == "__main__":
    app.run(debug=True)
