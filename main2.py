from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI

    def atualizar_texto(self, button):
        button.text = "Deu certo"


if __name__ == '__main__':
    MeuAplicativo().run()
