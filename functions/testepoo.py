from time import sleep


class Menu1:
    @staticmethod
    def execute(compras, cont):
        while True:
            print(f"  [!] - Informe um item [{cont}]")
            item = input("  --> ")
            if item == "":
                break
            elif item in compras:
                print("  [!] - Esse item já foi inserido!")
            else:
                compras.append(item)
                cont = cont + 1
                print('  [!] - Item inserido!\n')


class Menu2:
    @staticmethod
    def execute(compras):
        while True:
            print('\n')
            if len(compras) == 0:
                print('  [!] - Nenhuma compra encontrada\n')
                sleep(1)
                break
            else:
                print("  [?] - Qual item deseja apagar?\n")
            print('  [!] - LISTA DE COMPRAS')
            i = 0
            for item in compras:
                print(f"  [{i}] - {item}")
                i = i + 1
            apagar = input("  --> ")
            if apagar == "":
                break
            elif int(apagar) < len(compras):
                apagar = int(apagar)
                del compras[apagar]
                print("   [!] - Item apagado!\n")
            else:
                print('   [!] - Item não encontrado')


class Menu3:
    @staticmethod
    def execute(compras):
        print('\n  [!] - LISTA DE COMPRAS')
        if len(compras) == 0:
            print('   [!] - Nenhuma compra encontrada')
        else:
            i = 0
            for item in compras:
                print(f"  [{i}] - {item}")
                i = i + 1
