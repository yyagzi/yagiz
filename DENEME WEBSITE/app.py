import time
from flask import *
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_afet_alanlari():
    URL = 'https://www.sultanbeyli.bel.tr/afet-ve-acil-durum-toplanma-alanlari/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'}
    sayfa = requests.get(URL, headers=headers)
    icerik = BeautifulSoup(sayfa.content, 'html.parser')
    afet_alanlari_table = icerik.find('div', class_='table-responsive').find('table')
    return str(afet_alanlari_table)

@app.route('/')
def giris():
  return render_template("girisformu.html")

@app.route('/deneme')
def deneme():
  afet_alanlari = get_afet_alanlari()
  return render_template('deneme.html', afet_alanlari=afet_alanlari)

@app.route('/anasayfa')
def anasayfa():
  return render_template("anasayfa.html")

@app.route('/acildurumbildirimi')
def hakkimizda():
  return render_template("acildurumbildirimi.html")

@app.route('/deneme2')
def deneme2():
  return render_template("toplanmaalanları.html")

@app.route('/deneme12')
def deneme12():
  return render_template("yan.html")

@app.route('/deneme22')
def deneme22():
  return render_template("ana.html")

@app.route('/canlibolgegoruntusu')
def deneme222():
  return render_template("canlibolgegoruntusu.html")

if __name__ == '__main__':
    app.run(debug=True)

