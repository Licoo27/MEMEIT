import base64
import os
from flask import Flask, render_template, request, session, jsonify, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

# Directory to save memes
MEME_DIR = 'static/memes'

# Ensure the directory exists
if not os.path.exists(MEME_DIR):
    os.makedirs(MEME_DIR)

@app.route('/')
def exe():
    return render_template("index.html")

@app.route('/index2', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        session['image_url'] = request.form['image_url']
    return render_template("index2.html", image_url=session.get('image_url'))

@app.route('/index3', methods=['GET', 'POST'])
def texte():
    if request.method == 'POST':
        session['texte_saisi1'] = request.form['texte_saisi1']
        session['texte_saisi2'] = request.form['texte_saisi2']
    return render_template('index3.html', 
                           texte_saisi1=session.get('texte_saisi1'), 
                           texte_saisi2=session.get('texte_saisi2'), 
                           image_url=session.get('image_url'))

@app.route('/send_meme', methods=['POST'])
def send_meme():
    meme_data = request.form['meme']
    meme_data = meme_data.split(",")[1]  # Get base64 part of the data URL
    meme_data = base64.b64decode(meme_data)  # Decode base64 data

    meme_filename = datetime.now().strftime("%Y%m%d%H%M%S") + '.png'
    meme_path = os.path.join(MEME_DIR, meme_filename)
    
    with open(meme_path, "wb") as f:
        f.write(meme_data)
    
    return jsonify(success=True)

@app.route('/messages')
def messages():
    meme_files = os.listdir(MEME_DIR)
    meme_urls = [url_for('static', filename='memes/' + meme_file) for meme_file in meme_files]
    return render_template('messages.html', memes=meme_urls)

if __name__ == '__main__':
    app.run(debug=True)
