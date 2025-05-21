# layouts/inventario.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert
from datetime import datetime, date
import plotly.graph_objects as go


# ============ Página de Inventario ============
# Datos de inventario
inventory_data = pd.DataFrame({
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
    'Stock': [120, 85, 45, 210, 65],
    'Minimo': [50, 40, 30, 100, 30],
    'Rotacion': [3.2, 2.8, 1.5, 4.1, 2.3]
})

def get_layout():
    return html.Div([
    html.H2("Inventario e Insumos", className="mb-4"),
    
    # Fila 1: KPI
    dbc.Row([
        dbc.Col(create_card("Valor Total Inventario", "$12,500,000", "fas fa-boxes", "primary"), md=3),
        dbc.Col(create_card("Productos Bajo Mínimo", "5", "fas fa-exclamation-triangle", "danger"), md=3),
        dbc.Col(create_card("Rotación Promedio", "2.78", "fas fa-sync-alt", "info"), md=3),
        dbc.Col(create_card("Productos Sin Movimiento", "3", "fas fa-clock", "warning"), md=3),
    ], className="mb-4"),
    
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
                html.Tbody([
                    html.Tr([
                        html.Td("Producto C"), 
                        html.Td("45"), 
                        html.Td("50"), 
                        html.Td("-5"), 
                        html.Td(html.Span("Crítico", className="badge bg-danger"))
                    ]),
                    html.Tr([
                        html.Td("Producto E"), 
                        html.Td("65"), 
                        html.Td("70"), 
                        html.Td("-5"), 
                        html.Td(html.Span("Crítico", className="badge bg-danger"))
                    ]),
                    html.Tr([
                        html.Td("Producto B"), 
                        html.Td("85"), 
                        html.Td("90"), 
                        html.Td("-5"), 
                        html.Td(html.Span("Advertencia", className="badge bg-warning"))
                    ])
                ])
            ], striped=True, bordered=True, hover=True)
        ])
    ], className="mt-4")
])
