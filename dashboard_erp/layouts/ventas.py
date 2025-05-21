# layouts/ventas.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert
from datetime import datetime, date
import plotly.graph_objects as go

# ============ Página de Ventas ============
# Datos financieros
financial_data = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [1200000, 1500000, 1100000, 1800000],
    'Egresos': [900000, 950000, 850000, 1100000],
    'Flujo_Caja': [300000, 550000, 250000, 700000]
})

# Datos de ventas
sales_data = pd.DataFrame({
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
    'Ventas': [450000, 380000, 290000, 210000, 180000],
    'Clientes': [45, 38, 29, 21, 18]
})

def get_layout():
    return html.Div([
    html.H2("Ventas y Clientes", className="mb-4"),
    
    # Fila 1: Filtros y KPI
    dbc.Row([
        dbc.Col([
            dbc.Label("Periodo de análisis:"),
            dcc.DatePickerRange(
                id='date-range-ventas',
                min_date_allowed=date(2023, 1, 1),
                max_date_allowed=date(2023, 12, 31),
                start_date=date(2023, 4, 1),
                end_date=date(2023, 4, 30)
            )
        ], md=4),
        
        dbc.Col(create_card("Crecimiento Mensual", "+12.5%", "fas fa-percentage", "success"), md=2),
        dbc.Col(create_card("Ticket Promedio", "$45,200", "fas fa-shopping-cart", "info"), md=2),
        dbc.Col(create_card("Clientes Nuevos", "8", "fas fa-user-plus", "primary"), md=2),
        dbc.Col(create_card("Ventas Totales", "$1,800,000", "fas fa-dollar-sign", "warning"), md=2),
    ], className="mb-4"),
    
    # Fila 2: Gráficos principales
    dbc.Row([
        dbc.Col([
            html.H4("Ventas por Producto", className="mb-3"),
            dcc.Graph(
                figure=px.bar(sales_data, x='Producto', y='Ventas', 
                             color='Ventas', title="Top Productos por Ventas",
                             labels={'Producto': 'Producto', 'Ventas': 'Ventas ($)'})
            )
        ], md=6),
        
        dbc.Col([
            html.H4("Clientes por Producto", className="mb-3"),
            dcc.Graph(
                figure=px.pie(sales_data, values='Clientes', names='Producto', 
                             title="Distribución de Clientes por Producto",
                             hole=0.4)
            )
        ], md=6)
    ]),
    
    # Fila 3: Detalle y comparativo
    dbc.Row([
        dbc.Col([
            html.H4("Comparativo Mensual", className="mb-3"),
            dcc.Graph(
                figure=go.Figure(data=[
                    go.Bar(name='Mes Actual', x=financial_data['Mes'], y=financial_data['Ventas']),
                    go.Bar(name='Mes Anterior', x=financial_data['Mes'], y=financial_data['Ventas'].shift(1, fill_value=0))
                ]).update_layout(barmode='group', title="Comparativo Ventas Mes Actual vs Anterior")
            )
        ], md=8),
        
        dbc.Col([
            html.H4("Top 5 Clientes", className="mb-3"),
            dbc.ListGroup([
                dbc.ListGroupItem("Cliente A - $320,000"),
                dbc.ListGroupItem("Cliente B - $290,000"),
                dbc.ListGroupItem("Cliente C - $250,000"),
                dbc.ListGroupItem("Cliente D - $210,000"),
                dbc.ListGroupItem("Cliente E - $180,000")
            ])
        ], md=4)
    ], className="mt-4")
])
