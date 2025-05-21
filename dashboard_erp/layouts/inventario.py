# layouts/inventario.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
from components.cards import create_card
from data.data_inventario import kpi_data, inventory_data, alertas_inventario

def get_layout():
    # Crear cards KPI desde el DataFrame
    kpi_cards = []
    for _, row in kpi_data.iterrows():
        kpi_cards.append(
            dbc.Col(
                create_card(row['titulo'], row['valor'], row['icono'], row['color']),
                md=3
            )
        )
    
    # Crear filas de tabla de alertas
    filas_alertas = []
    for _, row in alertas_inventario.iterrows():
        filas_alertas.append(
            html.Tr([
                html.Td(row['Producto']),
                html.Td(row['Stock_Actual']),
                html.Td(row['Stock_Minimo']),
                html.Td(row['Diferencia']),
                html.Td(html.Span(row['Estado'], className=row['Clase_CSS']))
            ])
        )
    
    return html.Div([
        html.H2("Inventario e Insumos", className="title"),
        
        # Fila 1: KPI
        dbc.Row(kpi_cards, className="mb-4"),
        
        # Fila 2: Gráficos principales
        dbc.Row([
            dbc.Col([
                html.H4("Nivel de Stock por Producto", className="mb-3"),
                dcc.Graph(
                    figure=px.bar(inventory_data, y='Producto', x='Stock', 
                                color='Stock', orientation='h',
                                title="Stock Actual vs Mínimo Requerido",
                                labels={'Producto': 'Producto', 'Stock': 'Unidades'})
                )
            ], md=6),
            
            dbc.Col([
                html.H4("Rotación de Inventario", className="mb-3"),
                dcc.Graph(
                    figure=px.scatter(inventory_data, x='Producto', y='Rotacion', 
                                    size='Stock', color='Rotacion',
                                    title="Rotación de Inventario (Tamaño = Stock)")
                )
            ], md=6)
        ]),
        
        # Fila 3: Tabla de alertas
        dbc.Row([
            dbc.Col([
                html.H4("Alertas de Inventario", className="mb-3"),
                dbc.Table([
                    html.Thead(html.Tr([
                        html.Th("Producto"), 
                        html.Th("Stock Actual"), 
                        html.Th("Mínimo"), 
                        html.Th("Diferencia"), 
                        html.Th("Estado")
                    ])),
                    html.Tbody(filas_alertas)
                ], striped=True, bordered=True, hover=True)
            ])
        ], className="mt-4")
    ])