# layouts/finanzas.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert

financial_data = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [1200000, 1500000, 1100000, 1800000],
    'Egresos': [900000, 950000, 850000, 1100000],
    'Flujo_Caja': [300000, 550000, 250000, 700000]
})

def get_layout():
    return html.Div([
    html.H2("Panel Financiero General", className="mb-4"),
    
    # Fila 1: KPI Cards
    dbc.Row([
        dbc.Col(create_card("Ventas Mes Actual", "$1,800,000", "fas fa-dollar-sign", "success"), md=3),
        dbc.Col(create_card("Ventas Mes Anterior", "$1,100,000", "fas fa-chart-line", "info"), md=3),
        dbc.Col(create_card("Total Egresos", "$1,100,000", "fas fa-money-bill-wave", "danger"), md=3),
        dbc.Col(create_card("Flujo Neto", "$700,000", "fas fa-piggy-bank", "primary"), md=3),
    ], className="mb-4"),
    
    # Fila 2: Alertas y Gráfico de tendencia
    dbc.Row([
        dbc.Col([
            html.H4("Alertas Financieras", className="mb-3"),
            create_alert("Baja caja: Saldo bajo el mínimo recomendado", "warning"),
            create_alert("3 facturas vencidas por cobrar", "danger"),
            create_alert("2 pagos a proveedores próximos a vencer", "info"),
            html.Div([
                html.H5("Estado de Facturas", className="mt-3"),
                dbc.Row([
                    dbc.Col(html.Div([
                        html.Div(className="semaphore-green"),
                        html.Span("Pagadas: 85%", className="ms-2")
                    ]), md=4),
                    dbc.Col(html.Div([
                        html.Div(className="semaphore-yellow"),
                        html.Span("Pendientes: 10%", className="ms-2")
                    ]), md=4),
                    dbc.Col(html.Div([
                        html.Div(className="semaphore-red"),
                        html.Span("Vencidas: 5%", className="ms-2")
                    ]), md=4),
                ])
            ])
        ], md=4),
        
        dbc.Col([
            html.H4("Tendencia Financiera", className="mb-3"),
            dcc.Graph(
                figure=px.line(financial_data, x='Mes', y=['Ventas', 'Egresos', 'Flujo_Caja'],
                             title="Historial Financiero Últimos Meses",
                             labels={'value': 'Valor ($)', 'variable': 'Indicador'},
                             template="plotly_white").update_layout(legend=dict(
                                 orientation="h",
                                 yanchor="bottom",
                                 y=1.02,
                                 xanchor="right",
                                 x=1
                             ))
            )
        ], md=8)
    ]),
    
    # Fila 3: Detalle de facturas
    dbc.Row([
        dbc.Col([
            html.H4("Detalle de Facturas", className="mb-3"),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Estado"), html.Th("Cantidad"), html.Th("Valor Total")])),
                html.Tbody([
                    html.Tr([html.Td("Pagadas"), html.Td("42"), html.Td("$1,500,000")]),
                    html.Tr([html.Td("Pendientes"), html.Td("5"), html.Td("$250,000")]),
                    html.Tr([html.Td("Vencidas"), html.Td("3"), html.Td("$150,000")])
                ])
            ], striped=True, bordered=True, hover=True)
        ])
    ], className="mt-4")
])
