# layouts/ventas.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert
from datetime import datetime, date
import plotly.graph_objects as go
from data.data_ventas import get_financial_data, get_sales_data, get_top_clientes, get_kpi_data, get_date_range_defaults

def get_layout():
    # Obtener datos
    financial_data = get_financial_data()
    sales_data = get_sales_data()
    top_clientes = get_top_clientes()
    kpi_data = get_kpi_data()
    date_defaults = get_date_range_defaults()
    
    return html.Div([
        html.H2("Ventas y Clientes", className="title"),
        
        # Fila 1: Filtros y KPI
        dbc.Row([
            dbc.Col([
                dbc.Label("Periodo de análisis:"),
                dcc.DatePickerRange(
                    id='date-range-ventas',
                    min_date_allowed=date_defaults["min_date"],
                    max_date_allowed=date_defaults["max_date"],
                    start_date=date_defaults["start_date"],
                    end_date=date_defaults["end_date"]
                )
            ], md=4),
            
            dbc.Col(create_card("Crecimiento Mensual", kpi_data["crecimiento_mensual"], "fas fa-percentage", "success"), md=2),
            dbc.Col(create_card("Ticket Promedio", kpi_data["ticket_promedio"], "fas fa-shopping-cart", "info"), md=2),
            dbc.Col(create_card("Clientes Nuevos", kpi_data["clientes_nuevos"], "fas fa-user-plus", "primary"), md=2),
            dbc.Col(create_card("Ventas Totales", kpi_data["ventas_totales"], "fas fa-dollar-sign", "warning"), md=2),
        ], className="mb-4"),
        
        # Fila 2: Gráficos principales
        dbc.Row([
            dbc.Col([
                html.H4("Ventas por Producto", className="mb-3"),
                dcc.Graph(
                    figure=px.bar(sales_data, x='Producto', y='Ventas', 
                                 color='Ventas', title="Top Productos por Ventas",
                                 labels={'Producto': 'Producto', 'Ventas': 'Ventas ($)'},template="plotly_dark")
                )
            ], md=6),
            
            dbc.Col([
                html.H4("Clientes por Producto", className="mb-3"),
                dcc.Graph(
                    figure=px.pie(sales_data, values='Clientes', names='Producto', 
                                 title="Distribución de Clientes por Producto",
                                 hole=0.4,template="plotly_dark")
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
                    ]).update_layout(
                        barmode='group',
                        title="Comparativo Ventas Mes Actual vs Anterior",
                        template="plotly_dark"  # <- Aquí es donde debe ir
                    )
                )
            ], md=8),

            
            dbc.Col([
                html.H4("Top 5 Clientes", className="mb-3"),
                dbc.ListGroup([
                    dbc.ListGroupItem(f"{cliente['nombre']} - ${cliente['ventas']:,}") 
                    for cliente in top_clientes
                ])
            ], md=4)
        ], className="mt-4")
    ])