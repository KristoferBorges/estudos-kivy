from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class TelaDeEscolha(Screen):
    pass


class TelaBrinquedos(Screen):
    pass


class TelaComidas(Screen):
    pass


class TelaAnimais(Screen):
    pass


class TelaJogos(Screen):
    pass


class Tela(App):
    def build(self):
        self.title = 'IG - ProgramaExecutável'
        adm = ScreenManager()
        return adm


if __name__ == '__main__':
    Tela().run()
