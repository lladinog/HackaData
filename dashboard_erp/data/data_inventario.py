# data/data_inventario.py
import pandas as pd

# Datos para los KPI
kpi_data = pd.DataFrame({
    'titulo': ['Valor Total Inventario', 'Productos Bajo Mínimo', 'Rotación Promedio', 'Productos Sin Movimiento'],
    'valor': ['$12,500,000', '5', '2.78', '3'],
    'icono': ['fas fa-boxes', 'fas fa-exclamation-triangle', 'fas fa-sync-alt', 'fas fa-clock'],
    'color': ['primary', 'danger', 'info', 'warning']
})

# Datos de inventario
inventory_data = pd.DataFrame({
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
    'Stock': [120, 85, 45, 210, 65],
    'Minimo': [50, 40, 30, 100, 30],
    'Rotacion': [3.2, 2.8, 1.5, 4.1, 2.3]
})

# Datos de alertas de inventario
alertas_inventario = pd.DataFrame({
    'Producto': ['Producto C', 'Producto E', 'Producto B'],
    'Stock_Actual': [45, 65, 85],
    'Stock_Minimo': [50, 70, 90],
    'Diferencia': [-5, -5, -5],
    'Estado': ['Crítico', 'Crítico', 'Advertencia'],
    'Clase_CSS': ['badge bg-danger', 'badge bg-danger', 'badge bg-warning']
})