from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class TelaDeEscolha(Screen):
    pass


class TelaBrinquedos(Screen):
    pass


class Tela(App):
    def build(self):
        adm = ScreenManager()
        return adm


if __name__ == '__main__':
    Tela().run()
