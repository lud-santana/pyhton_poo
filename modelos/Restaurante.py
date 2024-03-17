class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} - {self.categoria}"
    
    def listar_restaurantes():
        print(f"\t{"Nome do restaurante".ljust(30)} \t{"Categoria".ljust(30)}  \t{"Status"}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(35)} | {restaurante._categoria.ljust(35)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"

restaurante_pizza = Restaurante(nome = "pizza", categoria = "italiano")
restaurante_praca = Restaurante(nome = "praça", categoria = "gourmet")

Restaurante.listar_restaurantes() 