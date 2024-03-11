class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} - {self.categoria}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print("{} | {} | {}".format(restaurante.nome.ljust(5), restaurante.categoria.ljust(8), restaurante.ativo))

restaurante_pizza = Restaurante(nome = "Pizza", categoria = "Italiano")
restaurante_praca = Restaurante(nome = "Praça", categoria = "Gourmet")

Restaurante.listar_restaurantes()