from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
 
@app.route('/')
def student():
    return render_template('addrbook.html')
 
@app.route('/pbook',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        verb = str(jsonify(request.form['id_name']))
        print(verb)
#         url = f'https://conjugator.reverso.net/conjugation-english-verb-{verb}.html'

#         response = requests.get(url)

#         if response.status_code == 200:
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
# #   ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > p

#             past_participle2 = soup.select_one('#ch_divSimple > div > div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(1) > i.verbtxt')
#             present = soup.select_one('#ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt')
#             past = soup.select_one("#ch_divSimple > div > div:nth-child(1) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt")
            
#             verb123 = present.string,past.string,past_participle2.string
            
#             return render_template("addrbook.html", verb_list=verb123)
        # else :
        #     html = response.text
        #     soup = BeautifulSoup(html, 'html.parser')
        #     error = soup.select_one('#ch_lblCustomMessage')
        #     print(error.string)
 #name은 key, name에 저장된 값은 value
 
if __name__ == '__main__':
    app.run(debug = True)
