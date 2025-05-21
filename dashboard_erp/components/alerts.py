# components/alerts.py
import dash_bootstrap_components as dbc
from dash import html

def create_alert(message, color):
    return dbc.Alert(message, color=color, dismissable=True)