from flask import render_template, request, url_for, redirect, flash
from siteportfolio import app, db
from siteportfolio.models import Produto
from siteportfolio.forms import FormFilmografia, FormSugestoes, FormInformacoes, FormControleEstoque
from siteportfolio.filmes import filmografia


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/site")
def site():
    return render_template('site.html')


@app.route("/sobremim")
def sobremim():
    return render_template('sobremim.html')


@app.route("/filmes", methods=['GET', 'POST'])
def filmes():
    form_informacoes = FormInformacoes()
    form_filmografia = FormFilmografia()
    form_sugestoes = FormSugestoes()
    nome = form_filmografia.ator.data
    lista_filmes = []

    if nome and "botao_filmografia" in request.form:
        lista_filmes = filmografia(nome)

    return render_template(
        'filmes.html',
        form_informacoes=form_informacoes,
        form_filmografia=form_filmografia,
        form_sugestoes=form_sugestoes,
        lista_filmes=lista_filmes)


@app.route("/estoque", methods=['GET', 'POST'])
def estoque():
    form_estoque = FormControleEstoque()
    produtos = Produto.query.all()
    primeiro_produto = Produto.query.filter_by(produto=form_estoque.produto.data).first()

    if "botao_novo" in request.form:
        if not primeiro_produto:
            if form_estoque.qtd.data and form_estoque.categoria.data:
                produto = Produto(produto=form_estoque.produto.data, qtd=form_estoque.qtd.data, categoria=form_estoque.categoria.data)
                db.session.add(produto)
                db.session.commit()
                flash("Produto adicionado com sucesso", 'alert-success')
                return redirect(url_for('estoque'))
            else:
                flash("Preencha os campos de Categoria e Quantidade", 'alert-danger')
        else:
            flash("Produto já cadastrado. Consulte a base de dados para mais detalhes.", 'alert-danger')

    elif "botao_consultar" in request.form:
        if primeiro_produto:
            produtos = [primeiro_produto]
        else:
            flash("Produto não encontrado. Consulte a base de dados para mais detalhes.", 'alert-danger')

    elif "botao_deletar" in request.form:
        if primeiro_produto:
            db.session.delete(primeiro_produto)
            db.session.commit()
            flash("Produto deletado com sucesso", 'alert-success')
            return redirect(url_for('estoque'))
        else:
            flash("Produto não encontrado. Consulte a base de dados para mais detalhes.", 'alert-danger')

    elif "botao_retirar" in request.form:
        if primeiro_produto:
            if form_estoque.qtd.data:
                qtd_antes = primeiro_produto.qtd
                if qtd_antes >= form_estoque.qtd.data:
                    qtd_depois = qtd_antes - form_estoque.qtd.data
                    primeiro_produto.qtd = qtd_depois
                    db.session.commit()
                    flash("Ação realizada com sucesso", 'alert-success')
                    return redirect(url_for('estoque'))
                else:
                    flash("Estoque abaixo do requerido. Consulte a base de dados para mais detalhes.", 'alert-danger')
                    return redirect(url_for('estoque'))
            else:
                flash('Necessário o preenchimento do campo de Quantidade.', 'alert-danger')
        else:
            flash("Produto não encontrado. Consulte a base de dados para mais detalhes.", 'alert-danger')

    elif 'botao_acrescentar' in request.form:
        if primeiro_produto:
            if form_estoque.qtd.data:
                qtd_antes = primeiro_produto.qtd
                qtd_depois = qtd_antes + form_estoque.qtd.data
                primeiro_produto.qtd = qtd_depois
                db.session.commit()
                flash("Ação realizada com sucesso", 'alert-success')
                return redirect(url_for('estoque'))
            else:
                flash('Necessário o preenchimento do campo de Quantidade.', 'alert-danger')
        else:
            flash("Produto não encontrado. Consulte a base de dados para mais detalhes.", 'alert-danger')

    return render_template('estoque.html', form_estoque=form_estoque, produtos=produtos)


@app.route("/dados")
def dados():
    return render_template('dados.html')