class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if  __name__ == '__main__':
    cafisso = Pessoa(nome='Cafisso')
    vinicius = Pessoa(cafisso, nome='Vinicius')
    print(Pessoa.cumprimentar(vinicius))
    print(id(vinicius))
    print(vinicius.cumprimentar())
    print(vinicius.nome)
    print(vinicius.idade)
    for filho in vinicius.filhos:
        print(filho.nome)