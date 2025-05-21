import pandas as pd

def kpi_data():
    """Retorna datos para las tarjetas KPI"""
    return pd.DataFrame({
        'titulo': ['Flujo de Caja', 'Margen Bruto', 'ROI', 'Días Cartera'],
        'valor': ['$1,450,000', '38.5%', '22.1%', '45 días'],
        'icono': ['fas fa-money-bill-trend-up', 'fas fa-chart-pie', 'fas fa-arrow-trend-up', 'fas fa-calendar-days'],
        'color': ['success', 'info', 'warning', 'danger']
    })

def financial_data():
    """Retorna datos financieros históricos"""
    return pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
        'Ventas': [1200000, 1500000, 1100000, 1800000, 1600000, 1900000],
        'Egresos': [900000, 950000, 850000, 1100000, 1050000, 1150000],
        'Flujo_Caja': [300000, 550000, 250000, 700000, 550000, 750000]
    })

def alertas_data():
    """Retorna datos para las alertas financieras"""
    return pd.DataFrame({
        'mensaje': [
            'Facturas vencidas por cobrar: 3 (valor $450,000)',
            'Gastos operacionales superaron el presupuesto en 12%',
            'Flujo de caja positivo (+15% vs mes anterior)'
        ],
        'tipo': ['danger', 'warning', 'success']
    })

def facturas_data():
    """Retorna datos del estado de facturas"""
    return pd.DataFrame({
        'estado': ['Pagadas', 'Pendientes', 'Vencidas'],
        'porcentaje': ['65%', '25%', '10%'],
        'clase_css': ['fas fa-check-circle text-success', 'fas fa-clock text-warning', 'fas fa-exclamation-circle text-danger']
    })

def detalle_facturas():
    """Retorna detalle de facturas para la tabla"""
    return pd.DataFrame({
        'Estado': ['Pagadas', 'Pendientes de pago', 'Vencidas', 'Anuladas'],
        'Cantidad': [45, 18, 7, 2],
        'Valor Total': ['$2,450,000', '$980,000', '$450,000', '$120,000']
    })