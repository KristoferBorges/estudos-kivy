from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class MyGridLayout(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_file('mylayout.kv')


if __name__ == '__main__':
    MyApp().run()
