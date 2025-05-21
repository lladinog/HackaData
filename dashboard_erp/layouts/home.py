# layouts/home.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert
from datetime import datetime, date
import plotly.graph_objects as go

def get_layout():
    # ============ Página de Inicio ============
    return html.Div([
    html.H1("Resumen Ejecutivo", className="mb-4"),
    
    # Fila 1: KPI principales
    dbc.Row([
        dbc.Col(create_card("Ventas Mes Actual", "$1,800,000", "fas fa-dollar-sign", "success"), md=3),
        dbc.Col(create_card("Margen Bruto", "42%", "fas fa-percent", "info"), md=3),
        dbc.Col(create_card("Eficiencia Operativa", "78%", "fas fa-tachometer-alt", "primary"), md=3),
        dbc.Col(create_card("ROI Trimestral", "15.2%", "fas fa-chart-line", "warning"), md=3),
    ], className="mb-4"),
    
    # Fila 2: Resumen ejecutivo
    dbc.Row([
        dbc.Col([
            html.H4("Resumen de Salud del Negocio", className="mb-3"),
            dbc.Card([
                dbc.CardBody([
                    html.P("La empresa muestra un crecimiento del 12.5% en ventas respecto al mes anterior, con un margen bruto saludable del 42%.", className="card-text"),
                    html.P("El flujo de caja positivo de $700,000 permite cubrir las obligaciones a corto plazo.", className="card-text"),
                    html.P("Áreas de atención:", className="card-text mt-2"),
                    html.Ul([
                        html.Li("3 productos con stock crítico"),
                        html.Li("5% de nómina rechazada por DIAN"),
                        html.Li("3 contratos por renovar este mes")
                    ])
                ])
            ])
        ], md=6),
        
        dbc.Col([
            html.H4("Indicadores Clave", className="mb-3"),
            dcc.Graph(
                figure=go.Figure(data=[
                    go.Indicator(
                        mode="gauge+number",
                        value=78,
                        title={'text': "Eficiencia Operativa"},
                        gauge={
                            'axis': {'range': [None, 100]},
                            'steps': [
                                {'range': [0, 60], 'color': "lightgray"},
                                {'range': [60, 80], 'color': "gray"},
                                {'range': [80, 100], 'color': "darkgray"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 78
                            }
                        }
                    )
                ]).update_layout(height=300)
            )
        ], md=6)
    ]),
    
    # Fila 3: Alertas y próximas acciones
    dbc.Row([
        dbc.Col([
            html.H4("Alertas Prioritarias", className="mb-3"),
            create_alert("Stock crítico en Producto C (45/50 unidades)", "danger"),
            create_alert("3 facturas vencidas por un total de $150,000", "warning"),
            create_alert("Nómina de abril con 5% de rechazo por DIAN", "info")
        ], md=6),
        
        dbc.Col([
            html.H4("Próximas Acciones", className="mb-3"),
            dbc.ListGroup([
                dbc.ListGroupItem("Renovar contrato de Juan Pérez (15/05)"),
                dbc.ListGroupItem("Revisar stock de Producto C y E"),
                dbc.ListGroupItem("Seguimiento a facturas vencidas"),
                dbc.ListGroupItem("Corregir nómina rechazada por DIAN")
            ])
        ], md=6)
    ], className="mt-4")
])
