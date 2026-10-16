from flask import Blueprint, render_template, request, url_for, redirect

from models import ProdutosModels

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_bp.route('/')
def listar_produtos():
    produtos = ProdutosModels().listar()

    return render_template('index.html', produtos=produtos), 200

@produtos_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produtos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco', 0))
        
        produto = ProdutosModels(
            nome=nome,
            preco=preco
        )
        
        produto.salvar()

        return redirect(url_for('produtos.listar_produtos'))
        
    return render_template('novo.html')

@produtos_bp.route('/update/<int:id>/status/<int:novo_status>')
def atualizar_status(id, novo_status):
    produto = ProdutosModels.get_produto(id)

    if not produto:
        return "Produto não encontrado", 404
        
    produto.status = novo_status
    produto.atualizar()
    
    return redirect(url_for('produtos.listar_produtos'))

@produtos_bp.post('/excluir/<int:id>')
def excluir_produto(id):
    produto = ProdutosModels.get_produto(id)
    
    produto.deletar()

    return redirect(url_for('produtos.listar_produtos'))