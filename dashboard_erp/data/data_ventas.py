import pandas as pd
from datetime import date

def get_financial_data():
    """Retorna datos financieros mensuales"""
    return pd.DataFrame({
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [1200000, 1500000, 1100000, 1800000],
        'Egresos': [900000, 950000, 850000, 1100000],
        'Flujo_Caja': [300000, 550000, 250000, 700000]
    })

def get_sales_data():
    """Retorna datos de ventas por producto"""
    return pd.DataFrame({
        'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
        'Ventas': [450000, 380000, 290000, 210000, 180000],
        'Clientes': [45, 38, 29, 21, 18]
    })

def get_top_clientes():
    """Retorna lista de los mejores clientes"""
    return [
        {"nombre": "Cliente A", "ventas": 320000},
        {"nombre": "Cliente B", "ventas": 290000},
        {"nombre": "Cliente C", "ventas": 250000},
        {"nombre": "Cliente D", "ventas": 210000},
        {"nombre": "Cliente E", "ventas": 180000}
    ]

def get_kpi_data():
    """Retorna datos para los KPI principales"""
    return {
        "crecimiento_mensual": "+12.5%",
        "ticket_promedio": "$45,200",
        "clientes_nuevos": 8,
        "ventas_totales": "$1,800,000"
    }

def get_date_range_defaults():
    """Retorna rangos de fechas por defecto para los filtros"""
    return {
        "min_date": date(2023, 1, 1),
        "max_date": date(2023, 12, 31),
        "start_date": date(2023, 4, 1),
        "end_date": date(2023, 4, 30)
    }