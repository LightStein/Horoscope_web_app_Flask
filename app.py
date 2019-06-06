'''
შექმენით flask ის გამოყენებით web აპლიკაცია "Prediction" რომელიც მომხმარებელს აცნობებს ჰოროსკოპული ნიშნის მიხედვით 
სიახლეებს რომელიც ელის უახლოეს მომავალში :)
დახმარებისთვის გამოიყენეთ https://github.com/tapaswenipathak/Horoscope-API#horoscope-api
'''
import requests, json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        sign = request.form["sign"]
        i = Info(sign)
        info = i.get_info()
        return render_template('base.html',info=info, sign=sign)
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)


class Info():
    def __init__(self, sign):
        self.sign = sign
        self.data = self.get_data()
        # print(self.data)
    
    def get_data(self):
        res = requests.get(f"https://horoscope-api.herokuapp.com/horoscope/week/{self.sign}")
        # print (json.loads(res.content)["horoscope"])
        return json.loads(res.content)["horoscope"]

    def get_info(self):
        return self.data