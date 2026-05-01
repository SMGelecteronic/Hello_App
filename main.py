from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # ایجاد یک متن ساده Hello
        return Label(text='Hello')

if __name__ == '__main__':
    MyApp().run()
