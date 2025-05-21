# layouts/nomina.py
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.cards import create_card
from components.alerts import create_alert
from datetime import datetime, date
import plotly.graph_objects as go

# ============ Página de Nómina ============
# Datos de nómina
payroll_data = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Total_Nomina': [28000000, 28500000, 29000000, 29500000],
    'Empleados': [45, 46, 47, 48]
})

def get_layout():
    return html.Div([
    html.H2("Nómina y Empleados", className="mb-4"),
    
    # Fila 1: KPI
    dbc.Row([
        dbc.Col(create_card("Empleados Activos", "48", "fas fa-users", "info"), md=3),
        dbc.Col(create_card("Costo Nómina Mes", "$29,500,000", "fas fa-money-bill", "primary"), md=3),
        dbc.Col(create_card("Salario Promedio", "$614,583", "fas fa-coins", "success"), md=3),
        dbc.Col(create_card("Contratos a Renovar", "3", "fas fa-file-contract", "warning"), md=3),
    ], className="mb-4"),
    
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
                    go.Pie(labels=['Aceptada', 'Rechazada'], values=[95, 5])
                ]).update_layout(title_text="Estado Envío Nómina Electrónica")
            ),
            
            html.Div([
                html.H5("Próximos Contratos a Renovar", className="mt-3"),
                dbc.ListGroup([
                    dbc.ListGroupItem("Juan Pérez - Renovación 15/05/2023"),
                    dbc.ListGroupItem("María Gómez - Renovación 22/05/2023"),
                    dbc.ListGroupItem("Carlos Ruiz - Renovación 30/05/2023")
                ])
            ])
        ], md=5)
    ]),
    
    # Fila 3: Detalle de nómina
    dbc.Row([
        dbc.Col([
            html.H4("Distribución de Nómina", className="mb-3"),
            dcc.Graph(
                figure=px.bar(x=['Salarios', 'Prestaciones', 'Bonos', 'Seguridad Social'], 
                             y=[22000000, 4500000, 2000000, 1000000],
                             title="Composición del Gasto en Nómina")
            )
        ])
    ], className="mt-4")
])