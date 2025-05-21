# app.py
import dash
from dash import html,dcc
from datetime import datetime, date
import dash_bootstrap_components as dbc
from layouts import home, finanzas, ventas, inventario, nomina
from callbacks.main_callbacks import register_callbacks

# Inicializar la app
app = dash.Dash(__name__, 
               external_stylesheets=[dbc.themes.BOOTSTRAP], 
               suppress_callback_exceptions=True)
app.title = "Dashboard Empresarial - ERP Analytics"

# ============ Layout principal ============
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Barra de navegación superior
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("ERP Dashboard", href="/", className="ms-2"),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Finanzas", href="/finanzas")),
                dbc.NavItem(dbc.NavLink("Ventas", href="/ventas")),
                dbc.NavItem(dbc.NavLink("Inventario", href="/inventario")),
                dbc.NavItem(dbc.NavLink("Nómina", href="/nomina")),
            ], className="me-auto"),
            html.Div([
                html.Span(datetime.now().strftime('%d/%m/%Y %H:%M')),
                dbc.Button("Actualizar", color="light", className="ms-3", id="refresh-btn")
            ], className="d-flex align-items-center")
        ]),
        color="primary",
        dark=True,
        sticky="top"
    ),
    
    # Contenido principal
    html.Div(id='page-content', className="container-fluid py-4"),
    
    # Footer
    dbc.Container([
        html.Hr(),
        html.P("© 2023 Dashboard Empresarial - ERP Analytics", className="text-center text-muted")
    ])
])

# Registrar callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)