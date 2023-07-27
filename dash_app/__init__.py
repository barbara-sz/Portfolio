import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


dados = pd.read_csv("siteportfolio/static/database.csv")


def create_dash_app(flask_app):
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")

    dash_app.layout = html.Div([
        html.Div(children=[
            dcc.Graph(
                id="example-graph",
                figure=px.bar(dados, x="estado_cliente", y="total_venda", color="categoria", barmode="group", width=500, height=400),
            )]),
        html.Div(children=[
            dcc.Graph(
                id="pizza-chart",
                figure=px.pie(dados, values='total_venda', names='produto', width=500, height=400))

        ])], style={'display': 'flex', 'flex-direction': 'row'})

    return dash_app
