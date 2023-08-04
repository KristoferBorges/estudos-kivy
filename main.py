from time import sleep
from functions.testepoo import Menu1, Menu2, Menu3

compras = list()
while True:
    sleep(1)
    cont = 1

    print("\n   OPCÕES ATUAIS")
    print("  [1] - Inserir dados;")
    print("  [2] - Apagar dados;")
    print("  [3] - Consultar dados;")
    escolha = input("  --> ")

    if escolha == "1":
        Menu1.execute(compras, cont)
    elif escolha == "2":
        Menu2.execute(compras)
    elif escolha == "3":
        Menu3.execute(compras)
    else:
        print("  Encerrando Programa!")
        break
