from flask import Flask, render_template

print(f'Name: {__name__}')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello_world():

    html = ""
    for i in range(1,7):
        html += f"<h{i}>This is text! </h{i}>"
    print(render_template("hello.html"))
    return html


if __name__  == "__main__":
    app.run(debug=True, port=8000)


