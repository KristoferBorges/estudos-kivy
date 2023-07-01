class Pessoa:
    def __init__(self, cpf, nome, sexo):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo

    def __str__(self):
        return f"""
            Descrição:
            CPF: {self.cpf}
            Nome: {self.nome}
            Sexo: {self.sexo}
            """


pessoa1 = Pessoa("51023136851", "Amanda", "Feminino")
pessoa2 = Pessoa("18178484911", "Vitória", "Feminino")
listaPessoas = [pessoa1, pessoa2]
while True:
    print('\nPessoas Cadastradas')
    for pessoa in listaPessoas:
        print(pessoa)
    opcao = input("Deseja adicionar alguma pessoa? [S/N]").upper()
    if opcao == "S":
        print("Preencha os dados da nova pessoa!")
        novo_cpf = input('CPF: ')
        novo_nome = input('Nome: ')
        novo_sexo = input('[1] - Masculino\n[2] - Feminino\n --> ')
        if novo_sexo == "1":
            novo_sexo = "Masculino"
        elif novo_sexo == "2":
            novo_sexo = "Feminino"
        nova_pessoa = Pessoa(novo_cpf, novo_nome, novo_sexo)
        listaPessoas.append(nova_pessoa)
