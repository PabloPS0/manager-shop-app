from repositories.product_repository import ProductRepository, ProductNotFoundError

class Menu:
    def __init__(self):
        self.product_repository = ProductRepository()

    def display(self):
        option = 0
        while True:
            print("-- MENU --")
            print("1. Add item")
            print("2. List item")
            print("3. Delete item")
            print("4. Search item")
            print("5. Update item")
            print("6. Exit")
            option = int(input('Digite: '))
            match option:
                case 1:
                    self.add_product()
                case 2:
                    self.list_products()
                case 3:
                    self.delete_product()
                case 4:
                    self.search_product()
                case 5:
                    self.update_product()
                case 6:
                    break
                case _:
                    print('Opção Inválida')   
    
    def add_product(self):
        print('-- ADICIONAR PRODUTO --')
        name = input('Nome: ')
        price = float(input('Preço: '))
        quantity = int(input('Quantidade: '))
        self.product_repository.add(name, price, quantity)

    def list_products(self):
        print('-- LISTAR PRODUTOS --')
        results = self.product_repository.list_all()
        for product in results:
            print(product)

    def delete_product(self):
        print('-- DELETAR PRODUTO --')
        code = input('Código: ')
        try:
            self.product_repository.delete(code)
            print(f"Produto com código {code} deletado com sucesso.")
        except ProductNotFoundError as e:
            print(e)

    def search_product(self):
        print('-- BUSCAR PRODUTO --')
        code = input('Código: ')
        try:
            product = self.product_repository.search(code)
            print(product)
        except  ProductNotFoundError as e:
            print(e)
    
    def update_product(self):
        print('-- ATUALIZAR PRODUTO --')
        code = input('Código: ')
        # Solicita novos valores
        name = input('Novo nome: ')
        price = float(input('Novo preço: '))
        quantity = int(input('Nova quantidade: '))
        try:
            product = self.product_repository.update(name, price, quantity, code)
            print(product)
        except ProductNotFoundError as e:
            print(e)
