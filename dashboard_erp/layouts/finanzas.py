# layouts/finanzas.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
from components.cards import create_card
from components.alerts import create_alert
from data.data_finanzas import kpi_data, financial_data, alertas_data, facturas_data, detalle_facturas

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
    
    # Crear alertas desde el DataFrame
    alertas = []
    for _, row in alertas_data.iterrows():
        alertas.append(create_alert(row['mensaje'], row['tipo']))
    
    # Crear indicadores de estado de facturas
    estados_facturas = []
    for _, row in facturas_data.iterrows():
        estados_facturas.append(
            dbc.Col(html.Div([
                html.Div(className=row['clase_css']),
                html.Span(f"{row['estado']}: {row['porcentaje']}", className="ms-2")
            ]), md=4)
        )
    
    # Crear filas de tabla de facturas
    filas_tabla = []
    for _, row in detalle_facturas.iterrows():
        filas_tabla.append(
            html.Tr([html.Td(row['Estado']), html.Td(row['Cantidad']), html.Td(row['Valor Total'])])
        )
    
    return html.Div([
        html.H2("Panel Financiero General", className="title"),
        
        # Fila 1: KPI Cards
        dbc.Row(kpi_cards, className="mb-4"),
        
        # Fila 2: Alertas y Gráfico de tendencia
        dbc.Row([
            dbc.Col([
                html.H4("Alertas Financieras", className="mb-3"),
                *alertas,
                html.Div([
                    html.H5("Estado de Facturas", className="mt-3"),
                    dbc.Row(estados_facturas)
                ])
            ], md=4),
            
            dbc.Col([
                html.H4("Tendencia Financiera", className="mb-3"),
                dcc.Graph(
                    figure=px.line(financial_data, x='Mes', y=['Ventas', 'Egresos', 'Flujo_Caja'],
                                 title="Historial Financiero Últimos Meses",
                                 labels={'value': 'Valor ($)', 'variable': 'Indicador'},
                                 template="plotly_dark").update_layout(
                                     legend=dict(
                                         orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=1
                                     )
                                 )
                )
            ], md=8)
        ]),
        
        # Fila 3: Detalle de facturas
        dbc.Row([
            dbc.Col([
                html.H4("Detalle de Facturas", className="mb-3"),
                dbc.Table([
                    html.Thead(html.Tr([html.Th("Estado"), html.Th("Cantidad"), html.Th("Valor Total")])),
                    html.Tbody(filas_tabla)
                ], striped=True, bordered=True, hover=True, className="texto")
            ])
        ], className="mt-4")
    ])