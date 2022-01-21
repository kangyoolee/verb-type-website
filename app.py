from flask import Flask, render_template, request, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='/static')
#{{ url_for('static', filename='style.css') }}
## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('index.html', num=num)

@app.route('/verb', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        verb = request.args.get('char1')
        url = f'https://conjugator.reverso.net/conjugation-english-verb-{verb}.html'

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
#   ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > p

            past_participle2 = soup.select_one('#ch_divSimple > div > div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(1) > i.verbtxt')
            present = soup.select_one('#ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt')
            past = soup.select_one("#ch_divSimple > div > div:nth-child(1) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt")
            verb_list = present.string+' - '+past.string+' - '+past_participle2.string
            
            return render_template('submit-test.html', char1=verb_list)
        else :
            return render_template('submit-test.html', char1='입력하신 동사가 확인되지 않습니다.')



if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
    app.run(threaded=True,port='5500',host='0.0.0.0',debug=True)