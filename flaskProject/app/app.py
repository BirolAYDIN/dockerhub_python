from flask import Flask,render_template
import pandas as pd
import re


df = pd.read_json('data.json')


## Akademik personel sayıları ########################################################


prof = df.loc[df['unvan_adSoyad'].str.contains('Prof. Dr.',flags=re.I,regex=True)]
doc = df.loc[df['unvan_adSoyad'].str.contains('Doç. Dr.',flags=re.I,regex=True)]
dr = df.loc[df['unvan_adSoyad'].str.contains('Dr. Öğr. Üyesi',flags=re.I,regex=True)]
ogr_gor = df.loc[df['unvan_adSoyad'].str.contains('Öğr. Gör.',flags=re.I,regex=True)]
ar_gor = df.loc[df['unvan_adSoyad'].str.contains('Ara*ş.',flags=re.I,regex=True)]
diger = len(df) -  len(prof + doc + dr + ogr_gor + ar_gor)





## Akademik personel sayıları ########################################################



## AKADEMİK PERSONEL GENEL DAĞILIMI  ##############################################################################

tip_fak = df.loc[df['birim'].str.contains('Tıp Fakültesi',flags=re.I,regex=True)]
Teknik= df.loc[df['birim'].str.contains('Teknik Bilimler Meslek Yüksekokulu',flags=re.I,regex=True)]
Iktisadi = df.loc[df['birim'].str.contains('İktisadi ve İdari Bilimler Fakültesi',flags=re.I,regex=True)]
Corlu_Muh = df.loc[df['birim'].str.contains('Çorlu Mühendislik Fakültesi',flags=re.I,regex=True)]
Veteriner= df.loc[df['birim'].str.contains('Veteriner Fakültesi',flags=re.I,regex=True)]
Ilahiyat = df.loc[df['birim'].str.contains('İlahiyat Fakültesi',flags=re.I,regex=True)]
Guz_San= df.loc[df['birim'].str.contains('Güzel Sanatlar, Tasarım ve Mimarlık Fakültesi',flags=re.I,regex=True)]
Ziraat = df.loc[df['birim'].str.contains('Ziraat Fakültesi',flags=re.I,regex=True)]
Fen_Edeb= df.loc[df['birim'].str.contains('Fen - Edebiyat Fakültesi',flags=re.I,regex=True)]
Corlu_Meslek= df.loc[df['birim'].str.contains('Çorlu Meslek Yüksekokulu',flags=re.I,regex=True)]







## AKADEMİK PERSONEL GENEL DAĞILIMI  ##############################################################################

data = [ len(prof) ,len(doc) ,len(dr) ,len(ogr_gor) ,len(ar_gor) , diger , len(Teknik), len(Iktisadi), len(Corlu_Meslek), len(Veteriner), len(Ilahiyat), len(Guz_San),
len(Ziraat),len(Fen_Edeb),len(Corlu_Muh),len(tip_fak) ]





app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',data = data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
