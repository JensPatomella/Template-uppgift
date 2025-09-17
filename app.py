from flask import Flask, render_template, request

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
    content = f"{request.form.get('name', '')}, {request.form.get('message', '')}"
    with open(FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(content + "\n")
    return render_template("contact.html", file_content=content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')