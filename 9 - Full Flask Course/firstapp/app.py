from flask import Flask, flash, redirect, request, render_template, Response, send_from_directory, jsonify, session, make_response
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = "SOME KEY" # for an actual application, you should use a more secure key and keep it secret!

# Example routes
@app.route('/')
def index():
   return render_template('index.html', message='Index')

@app.route('/set_data')
def set_data():
   session['name'] = 'Bob'
   session['job'] = 'Builder'
   return render_template('index.html', message='Data set in session')

@app.route('/get_data')
def get_data():
   if 'name' in session.keys():
      name = session['name']
      job = session['job']
      return render_template('index.html', message=f'Name: {name} - Job: {job}')
   return render_template('index.html', message='No session data found')

@app.route('/clear_session')
def clear_session():
   session.clear()
   return render_template('index.html', message='Session data cleared')

@app.route('/set_cookie')
def set_cookie():
   response = make_response(render_template('index.html', message='Cookie set'))
   response.set_cookie('cookie_name', 'cookie_value')
   return response


@app.route('/get_cookie')
def get_cookie():
   cookie_value = request.cookies.get('cookie_name')
   return render_template('index.html', message=f'Cookie value: {cookie_value}') 

@app.route('/remove_cookie')
def remove_cookie():
   response = make_response(render_template('index.html', message='Cookie removed'))
   response.set_cookie('cookie_name', expires=0)
   return response

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == "POST":
      username = request.form.get('username')
      password = request.form.get('password')
      # Here you would normally check the username and password against a database
      if username == 'admin' and password == 'password':
         flash('Login successful', 'success')
         return render_template('index.html', message='Login successful')
      else:
         flash('Invalid credentials', 'error')
         return render_template('login.html', message='Invalid credentials')
   return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)