from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")


class TelaInicial(Screen):
    pass


class TelaSecundaria(Screen):
    pass


class NovaTela3(Screen):
    pass


class MeuAplicativo(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(TelaInicial(name='tela_inicial'))
        screen_manager.add_widget(TelaSecundaria(name='tela_secundaria'))
        screen_manager.add_widget(NovaTela3(name='new_screen'))
        return screen_manager


if __name__ == '__main__':
    MeuAplicativo().run()
