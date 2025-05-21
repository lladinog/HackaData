# layouts/home.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go
from components.cards import create_card
from components.alerts import create_alert
from data.data_home import kpi_data, resumen_data, eficiencia_data, alertas_data, acciones_data

def get_layout():
    # Crear cards KPI desde el DataFrame
    kpi_cards = []
    for _, row in kpi_data.iterrows():
        kpi_cards.append(
            dbc.Col(
                create_card(row['kpi'], row['valor'], row['icono'], row['color']),
                md=3
            )
        )
    
    # Procesar alertas del resumen (separadas por ;)
    alertas_resumen = resumen_data['alertas'][0].split(';')
    
    # Crear alertas desde el DataFrame
    alertas = []
    for _, row in alertas_data.iterrows():
        alertas.append(create_alert(row['mensaje'], row['tipo']))
    
    # Crear listado de acciones desde el DataFrame
    acciones = []
    for _, row in acciones_data.iterrows():
        acciones.append(dbc.ListGroupItem(row['accion']))
    
    # Procesar niveles de eficiencia
    niveles_eficiencia = [
        {'range': [int(x) for x in eficiencia_data['nivel_1_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_1_color'][0]},
        {'range': [int(x) for x in eficiencia_data['nivel_2_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_2_color'][0]},
        {'range': [int(x) for x in eficiencia_data['nivel_3_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_3_color'][0]}
    ]
    
    return html.Div([
        html.H1("Resumen Ejecutivo", className="title"),
        
        # Fila 1: KPI principales
        dbc.Row(kpi_cards, className="mb-4"),
        
        # Fila 2: Resumen ejecutivo
        dbc.Row([
            dbc.Col([
                html.H4("Resumen de Salud del Negocio", className="mb-3"),
                dbc.Card([
                    dbc.CardBody([
                        html.P(f"La empresa muestra un crecimiento del {resumen_data['crecimiento'][0]} en ventas respecto al mes anterior, con un margen bruto saludable del {resumen_data['margen_bruto'][0]}.", className="card-text"),
                        html.P(f"El flujo de caja positivo de {resumen_data['flujo_caja'][0]} permite cubrir las obligaciones a corto plazo.", className="card-text"),
                        html.P("Áreas de atención:", className="card-text mt-2"),
                        html.Ul([
                            html.Li(alerta, className="card-text") for alerta in alertas_resumen
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
                            value=eficiencia_data['valor'][0],
                            title={'text': "Eficiencia Operativa"},
                            gauge={
                                'axis': {'range': [eficiencia_data['rango_min'][0], eficiencia_data['rango_max'][0]]},
                                'steps': niveles_eficiencia,
                                'threshold': {
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,
                                    'value': eficiencia_data['valor'][0]
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
                *alertas
            ], md=6),
            
            dbc.Col([
                html.H4("Próximas Acciones", className="mb-3"),
                dbc.ListGroup(acciones)
            ], md=6)
        ], className="mt-4")
    ])