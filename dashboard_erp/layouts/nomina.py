# layouts/nomina.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from components.cards import create_card
from data.data_nomina import (kpi_data, payroll_data, 
                            dian_data, contratos_data,
                            distribucion_nomina)

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
    
    # Crear items de contratos a renovar
    contratos_items = []
    for _, row in contratos_data.iterrows():
        contratos_items.append(
            dbc.ListGroupItem(f"{row['Nombre']} - Renovación {row['Fecha_Renovacion']}")
        )
    
    return html.Div([
        html.H2("Nómina y Empleados", className="title"),
        
        # Fila 1: KPI
        dbc.Row(kpi_cards, className="mb-4"),
        
        # Fila 2: Gráficos principales
        dbc.Row([
            dbc.Col([
                html.H4("Evolución de Nómina", className="mb-3"),
                dcc.Graph(
                    figure=px.line(payroll_data, x='Mes', y='Total_Nomina',
                                title="Costo de Nómina Últimos Meses",
                                labels={'Total_Nomina': 'Valor ($)', 'Mes': 'Mes'})
                )
            ], md=7),
            
            dbc.Col([
                html.H4("Estado Nómina DIAN", className="mb-3"),
                dcc.Graph(
                    figure=go.Figure(data=[
                        go.Pie(labels=dian_data['Estado'], 
                              values=dian_data['Porcentaje'])
                    ]).update_layout(title_text="Estado Envío Nómina Electrónica")
                ),
                
                html.Div([
                    html.H5("Próximos Contratos a Renovar", className="mt-3"),
                    dbc.ListGroup(contratos_items)
                ])
            ], md=5)
        ]),
        
        # Fila 3: Detalle de nómina
        dbc.Row([
            dbc.Col([
                html.H4("Distribución de Nómina", className="mb-3"),
                dcc.Graph(
                    figure=px.bar(distribucion_nomina, 
                                x='Concepto', y='Valor',
                                title="Composición del Gasto en Nómina",
                                labels={'Concepto': 'Concepto', 'Valor': 'Valor ($)'})
                )
            ])
        ], className="mt-4")
    ])