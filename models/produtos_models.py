from database import DataBase

class ProdutosModels:
    def __init__(self, id = None, nome = None, preco = None, status = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = status
    
        self.connection = DataBase().connect()

        sql = 'CREATE TABLE IF NOT EXISTS produto (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(20) NOT NULL, preco FLOAT NOT NULL, status BOOLEAN DEFAULT 1)'

        self.connection.execute(sql)

    @staticmethod
    def listar():
        sql = 'SELECT id, nome, preco, status FROM produto'
        dados = DataBase._executar(sql)
        if not dados:
            return []
        
        produtos = []

        for produto in dados:
            produtos.append(
                ProdutosModels(
                    id=produto[0],
                    nome=produto[1],
                    preco=produto[2],
                    status=produto[3]
                    )
            )

        return produtos

    def salvar(self):
        sql = f"INSERT INTO produto (nome, preco) VALUE ('{self.nome}', {float(self.preco)})"
        DataBase._executar(sql)

    def atualizar(self):
        sql = f"UPDATE produto SET status = {self.status} WHERE id = {int(self.id)}"
        DataBase._executar(sql)

    def deletar(self):
        sql = f"DELETE FROM produto WHERE id = {int(self.id)}"
        DataBase._executar(sql)

    @staticmethod
    def get_produto(id):
        query = f"SELECT id, nome, preco, status FROM produto WHERE id = {id}"
        produtos = DataBase._executar(query)

        if not produtos:
            return None

        produto_db = produtos[0]

        return ProdutosModels(id=produto_db[0], nome=produto_db[1], preco=produto_db[2], status=produto_db[3])