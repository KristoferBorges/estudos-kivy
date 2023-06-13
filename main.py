from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")


class TelaInicial(Screen):
    numero_tela_inicial = ''

    def armazenar_numero(self):
        self.numero_tela_inicial = self.ids.input_tela1.text


class TelaSecundaria(Screen):
    numero_tela_secundaria = ''

    def armazenar_numero(self):
        self.numero_tela_secundaria = self.ids.input_tela2.text


class TelaFinal(Screen):
    pass


class MeuAplicativo(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(TelaInicial(name='tela_inicial'))
        screen_manager.add_widget(TelaSecundaria(name='tela_secundaria'))
        screen_manager.add_widget(TelaFinal(name='tela_final'))
        return screen_manager


if __name__ == '__main__':
    MeuAplicativo().run()
