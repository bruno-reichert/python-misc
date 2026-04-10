from flask import Flask, redirect, request, render_template, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Example routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Login successful!'
        else:
            return 'Login failed!'
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode('utf-8')
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    else:
        return "Unsupported file type!"
    
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(df.to_csv(index=False),
    mimetype='text/csv',
    headers={"Content-disposition":
             "attachment; filename=result.csv"})
    return response

@app.route('/convert_csv_download_page', methods=['POST'])
def convert_csv_download_page():
    file = request.files['file']
    df = pd.read_excel(file)

    downloads_dir = os.path.join(BASE_DIR, 'downloads')
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join(downloads_dir, filename))
    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    downloads_dir = os.path.join(BASE_DIR, 'downloads')
    return send_from_directory(downloads_dir, filename, download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    assert request.json is not None # Added to stop typescript error
    greeting = request.json['greeting'] 
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}!')

    return jsonify({'message': 'Data saved to file.txt'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)