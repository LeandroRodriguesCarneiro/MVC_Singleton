from flask import Blueprint, render_template, request, url_for, redirect

from models import ProdutosModels

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

produtos = [
    {"id": 1, "nome": "Produto A", "preco": 29.90, "status": 1},
    {"id": 2, "nome": "Produto B", "preco": 49.90, "status": 0}
]

@produtos_bp.route('/')
def listar_produtos():
    global produtos
    return render_template('index.html', produtos=produtos), 200

@produtos_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produtos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco', 0))
        
        novo_id = len(produtos) + 1
        produtos.append({"id": novo_id, "nome": nome, "preco": preco, "status": 1})
        
        return redirect(url_for('produtos.listar_produtos'))
        
    return render_template('novo.html')

@produtos_bp.route('/update/<int:id>/status/<int:novo_status>')
def atualizar_status(id, novo_status):
    produto = next((p for p in produtos if p['id'] == id), None)
    
    if not produto:
        return "Produto não encontrado", 404
        
    produto['status'] = novo_status
    
    return redirect(url_for('produtos.listar_produtos'))

@produtos_bp.post('/excluir/<int:id>')
def excluir_produto(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    return redirect(url_for('produtos.listar_produtos'))