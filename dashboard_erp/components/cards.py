# components/catds.py
import dash_bootstrap_components as dbc
from dash import html

def create_card(title, value, icon, color, id_name=""):
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                html.H4(title, className="card-title"),
                html.H3(value, className="card-value", id=id_name if id_name else "None"),
                html.Div(className=f"icon-circle bg-{color}", children=[
                    html.I(className=icon)
                ])
            ], className="card-content")
        ]),
        className=f"card card-{color}"
    )
