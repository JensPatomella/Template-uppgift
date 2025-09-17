from flask import Flask, render_template, request
import os

app = Flask(__name__)

FILE_PATH = "blabla.txt"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/sent', methods=['POST'])
def write():
    content = request.form.get('message', '') + request.form.get('name', '')
    with open(FILE_PATH, 'w', encoding='utf-8') as f: #Flaggan 'w' (write) anger att filen ska skrivas
        f.write(content)    # .write() skriver innehållet i variabeln content till filen
    return render_template("contact.html", file_content=content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')