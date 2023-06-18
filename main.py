from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import platform

# Verifica se o usuário está usando Windows
if platform.system() == "Windows":
    sistema_windows = True
else:
    sistema_windows = False


class TelaDeEscolha(Screen):
    pass


class TelaBrinquedos(Screen):

    def enviar_texto(self, texto):
        print(texto)


class TelaComidas(Screen):
    pass


class TelaAnimais(Screen):
    pass


class TelaJogos(Screen):
    pass


class Tela(App):
    def build(self):
        if sistema_windows:
            Window.size = (600, 500)
        self.title = 'IG - ProgramaExecutável'
        adm = ScreenManager()
        return adm


if __name__ == '__main__':
    Tela().run()
