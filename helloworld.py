#:kivy 1.11.1
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class HWApp(App):
    def build(self):
        return Label(text='Hello World!')

if __name__ == '__main__':
    HWApp().run()