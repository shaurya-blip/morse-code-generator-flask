from flask import Flask, render_template, request
from morse import to_morse

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        text = str(request.form['content'])
        to_morse(text)
        return render_template('index.html', data=text)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
