from flask import Flask

print(f'Name: {__name__}')
app = Flask(__name__)

@app.route("/")
def hello_world():
    html = ""
    for i in range(1,7):
        html += f"<h{i}>This is text! </h{i}>"
    return html

if __name__  == "__main__":
    app.run(debug=True, port=8000)


