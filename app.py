from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Checking (Update change) ...'

if __name__ == '__main__':
    app.run(debug=True)