from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Buildkite!</h1>'

@app.route('/health')
def health():
    return {'status': 'ok'}

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
