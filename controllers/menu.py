from repositories.product_repository import ProductRepository

class Menu:
    def __init__(self):
        self.product_repository = ProductRepository()

    def display(self):
        option = 0
        while True:
            print("-- MENU --")
            print("1. Add item")
            print("2. Select item")
            print("3. Exit")
            option = int(input('Digite: '))
            match option:
                case 1:
                    self.add_product()
                case 2:
                    self.list_products()
                case 3:
                    break
                case _:
                    print('Opção Inválida')   
    
    def add_product(self):
        print('-- ADICIONAR PRODUTO --')
        
        nome = input('Nome: ')
        price = float(input('Preço: '))
        quantity = int(input('Quantidade: '))
        self.product_repository.add(nome, price, quantity)

    def list_products(self):
        print('-- LISTAR PRODUTOS --')
        results = self.product_repository.list_all()
        for product in results:
            print(product)