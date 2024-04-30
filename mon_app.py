from flask import Flask, render_template, request

app = Flask(__name__)
url = ''


@app.route('/')
def exe():
  return render_template("index.html")


@app.route('/index2', methods=['GET' or 'POST'])
def image():
  image_url = request.args.get('image_url')
  print(image_url)
  return render_template("index2.html", image_url=image_url)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texte_saisi = request.form['texte_saisi']
        return f"Vous avez saisi : {texte_saisi}"
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)


