from flask import Flask, request, make_response

app = Flask(__name__)

# Example routes
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/glados')
def glados():
    response = make_response('<h1>GLaDOS is here to test you!</h1>')
    response.status_code = 202
    response.headers['Test-Header'] = 'This is a custom header'
    return response

# Examples of dynamic routes
@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'<h1>{num1} + {num2} = {num1 + num2}</h1>'

@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'<h1>{greeting}, {name}!</h1>'
    else:
        return '<h1>Please provide both "greeting" and "name" URL parameters.</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)