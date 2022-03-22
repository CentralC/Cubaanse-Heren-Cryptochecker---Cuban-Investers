from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import csv

CSV_URL = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=BTC&market=USD&interval=5min&apikey=64TY7285TUX7FM6P'


class BoxLayoutApp(App):
    def build(self):
        rootbox = BoxLayout(orientation='vertical')
        button1 = Button(text="Cuban Investor")
        rootbox.add_widget(button1)
        button1.bind(on_press=BoxLayoutApp.API)
        return rootbox

    def API(self):
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                print(row)


BoxLayoutApp().run()
