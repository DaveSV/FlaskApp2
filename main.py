from flask import Flask, render_template
app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/content")
def view_content():
    return render_template("content.html", title="Contenidos")

@app.route("/contacto")
def view_contacto():
    return render_template("content.html", title="Contacto")

if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)