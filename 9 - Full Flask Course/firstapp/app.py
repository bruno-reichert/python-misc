from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__, template_folder='templates')

# Example routes
@app.route('/')
def index():
    myvalue = "This is a test value!"
    myresult = 10 + 20
    mylist = [10, 20, 30, 40, 50]
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist=mylist)

@app.route('/other')
def other():
    some_text = "This is some text to demonstrate filters."
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(s))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)