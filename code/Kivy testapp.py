from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget


class BoxLayoutApp(App):
    def build(self):
        rootbox = BoxLayout(orientation='vertical')
        hb = BoxLayout(orientation='horizontal')
        vb = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        label1 = Label(text="Cuban Investor")
        label2 = Label(text="Cuban Investor")
        button1 = Button(text="Cuban Investor")
        button2 = Button(text="Cuban Investor")
        vb.add_widget(label1)
        scroll.add_widget(button1)
        """scroll.add_widget(button2)"""
        rootbox.add_widget(vb)
        rootbox.add_widget(scroll)
        return rootbox


BoxLayoutApp().run()
