from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        button = Button(text='Hello World', font_size=60)
        return button


if __name__ == '__main__':
    MyApp().run()
