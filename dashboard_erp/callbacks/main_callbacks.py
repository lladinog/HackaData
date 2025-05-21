# callbacks/main_callbacks.py
from dash import Input, Output
from layouts import home, finanzas, ventas, inventario, nomina

def register_callbacks(app):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/finanzas':
            return finanzas.get_layout()
        elif pathname == '/ventas':
            return ventas.get_layout()
        elif pathname == '/inventario':
            return inventario.get_layout()
        elif pathname == '/nomina':
            return nomina.get_layout()
        else:
            return home.get_layout()