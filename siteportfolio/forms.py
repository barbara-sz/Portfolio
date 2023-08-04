from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, widgets, RadioField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired


class FormFilmografia(FlaskForm):
    ator = StringField("Ator/Atriz", render_kw={"placeholder": "angelina jolie"})
    tipo = RadioField(choices=['Filme', 'TV/Série'], widget=widgets.TableWidget(with_table_tag=True), default='Filme')
    botao_filmografia = SubmitField("Pesquisar")


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class FormInformacoes(FlaskForm):
    tipo = RadioField(choices=['Filme', 'TV/Série'], widget=widgets.TableWidget(with_table_tag=True), default='Filme')
    ano = StringField("Ano", render_kw={"placeholder": "Opcional"})
    filme = StringField("Filme", render_kw={"placeholder": "o senhor dos aneis"})
    pessoas = StringField("Artistas",  render_kw={"placeholder": "Opcional"})
    genero1 = MultiCheckboxField(label="Gênero",
                                choices=[('28', 'Acão'), ('12', 'Aventura'), ('16', 'Animação'), ('35', 'Comédia'),
                                         ('80', 'Crime'), ('99', 'Documentário'), ('18', 'Drama'),('10751', 'Família'),
                                         ('14', 'Fantasia')])
    genero2 = MultiCheckboxField(choices=[('37', 'Faroeste'), ('878', 'Ficcção Científica'),
                                         ('10752', 'Guerra'), ('36', 'História'), ('27', 'Terror'),
                                         ('10402', 'Musical'), ('9648', 'Mistério'), ('10749', 'Romance'),
                                         ('53', 'Suspense')])

    botao_informacoes = SubmitField("Pesquisar")


class FormSugestoes(FlaskForm):
    ator = StringField("Ator/Atriz")
    ano = StringField("Ano")
    genero = StringField("Gênero")
    extra = StringField("Informações Adicionais")
    plataforma = StringField("Onde Assistir")
    tipo = RadioField(choices=['Filme', 'Série'], widget=widgets.TableWidget(with_table_tag=True))
    botao_sugestoes = SubmitField("Pesquisar")


class FormControleEstoque(FlaskForm):
    produto = StringField("Produto", validators=[DataRequired()])
    qtd = IntegerField("Quantidade")
    categoria = StringField("Categoria")
    botao_retirar = SubmitField("- Unidades")
    botao_acrescentar = SubmitField("+ Unidades")
    botao_consultar = SubmitField("Consultar Produto")
    botao_novo = SubmitField("+ Novo Produto")
    botao_deletar = SubmitField("Deletar Produto")
