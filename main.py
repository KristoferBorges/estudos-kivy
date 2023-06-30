import datetime
import platform
from modulo import dateVerification
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Verifica se o usuário está usando Windows
if platform.system() == "Windows":
    sistema_windows = True
else:
    sistema_windows = False


class MenuPrincipal(Screen):
    """
    Menu com as opções principais, NovosRegistros, LimparDados, ConsultaDeListas,
    Criar Backup e FecharPrograma.
    """
    pass


class NovosRegistros(Screen):
    """
    Opção para inserir novos dados, porém se faz necessário escolher as
    lista que deseja inserir os dados,
    poderá escolher entre: RD Marcas, Perfumaria e Dermo.
    """
    pass


class RegistrosRDMarcas(Screen):
    """
    Opção do menu principal após clicar na opção de registros (RDMarcas).
    """

    label_aviso = Label(text='Campos não preenchidos')

    def __init__(self, **kwargs):
        super(RegistrosRDMarcas, self).__init__(**kwargs)
        self.exibir = False
        if self.exibir:
            self.add_widget(self.label_aviso)
            print('on')


class RegistrosPerfumaria(Screen):
    """
    Opção do menu principal após clicar na opção de registros (Perfumaria).
    """
    pass


class RegistrosDermo(Screen):
    """
    Opção do menu principal após clicar na opção de registros (Dermo).
    """
    pass


class LimparDados(Screen):
    """
    Opção para limpar dos dados, porém se faz necessário escolher as
    lista que deseja limpar os dados,
    poderá escolher entre: RD Marcas, Perfumaria, Dermo ou todas ao mesmo tempo.
    """
    pass


class ConsultaDeListas(Screen):
    """
    Opção para consultar os dados existentes, porém se faz necessário escolher as
    lista que deseja consultar,
    poderá escolher entre: RD Marcas, Perfumaria, Dermo ou todas ao mesmo tempo.
    """
    pass


class CriarBackup(Screen):
    """
    Opção para fazer backup dos dados existentes, porém se faz necessário escolher as
    lista que deseja fazer o backup,
    poderá escolher entre: RD Marcas, Perfumaria, Dermo ou todas ao mesmo tempo.
    """
    pass


class FecharPrograma(Screen):
    """
    Opção simples para fechar o programa com segurança sem medo de perder os
    dados ou interromper no meio do processo.
    """
    pass


class Tela(App):

    def build(self):
        if sistema_windows:
            Window.size = (379, 810)
        self.title = 'ConsultaDeMetas_v2.0'
        adm = ScreenManager()
        return adm

    @staticmethod
    def pega_input_rdmarcas(data, meta, vendas):
        """
        --> Função para pegar os dados inseridos na opção 'REGISTROS' -> 'RDMARCAS'.
        :param data: Valor de Data inserida na interface
        :param meta: Valor de Meta inserida na interface
        :param vendas: Valor de Venda inserida na interface
        :return: Retorna os dados devidamente formatados.
        """
        registros_rdmarcas = RegistrosRDMarcas()
        try:
            meta = float(meta)
            vendas = float(vendas)
            data = dateVerification(data)
            if vendas >= meta:
                result = "META ATINGIDA"
            else:
                result = "META NÃO ATINGIDA"
            return print(f"DATA: {data}\nMETA: {meta}\nVENDAS: {vendas}\nRESULTADO: {result}")

        except Exception as error:
            print(error)
            registros_rdmarcas.exibir = True
            registros_rdmarcas.clear_widgets()
            registros_rdmarcas.add_widget(registros_rdmarcas.label_aviso)
            return registros_rdmarcas


if __name__ == '__main__':
    Tela().run()
