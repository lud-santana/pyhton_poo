from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('da praça', 'Gourmet')
restaurante_japones = Restaurante('Japadoido', 'Japonesa')
restaurante_italiano = Restaurante('Pizzaolo', 'Italiana')

restaurante_praca.receber_avaliacao('Yuri', 9)
restaurante_italiano.receber_avaliacao('Isabel', 10)


restaurante_italiano.alternar_status()
restaurante_praca.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()