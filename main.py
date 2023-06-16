from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Adm(ScreenManager):
    pass


class TelaDeRegistro(Screen):
    pass


class TelaBrinquedos(Screen):
    pass


class Tela(App):
    def build(self):
        return Adm()


if __name__ == '__main__':
    Tela().run()
