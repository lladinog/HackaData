# data/data_home.py
import pandas as pd

# Datos para los KPI principales
kpi_data = pd.DataFrame({
    'kpi': ['Ventas Mes Actual', 'Margen Bruto', 'Eficiencia Operativa', 'ROI Trimestral'],
    'valor': ['$1,800,000', '42%', '78%', '15.2%'],
    'icono': ['fas fa-dollar-sign', 'fas fa-percent', 'fas fa-tachometer-alt', 'fas fa-chart-line'],
    'color': ['success', 'info', 'primary', 'warning']
})

# Datos para el resumen ejecutivo
resumen_data = pd.DataFrame({
    'crecimiento': ['12.5%'],
    'margen_bruto': ['42%'],
    'flujo_caja': ['$700,000'],
    'alertas': [  # Lista de alertas como una sola cadena o lista
        "3 productos con stock crítico;5% de nómina rechazada por DIAN;3 contratos por renovar este mes"
    ]
})

# Datos para el indicador de eficiencia
eficiencia_data = pd.DataFrame({
    'valor': [78],
    'rango_min': [0],
    'rango_max': [100],
    'nivel_1_rango': ['0-60'],
    'nivel_1_color': ['lightgray'],
    'nivel_2_rango': ['60-80'],
    'nivel_2_color': ['gray'],
    'nivel_3_rango': ['80-100'],
    'nivel_3_color': ['darkgray']
})

# Datos para alertas prioritarias
alertas_data = pd.DataFrame({
    'mensaje': [
        "Stock crítico en Producto C (45/50 unidades)",
        "3 facturas vencidas por un total de $150,000",
        "Nómina de abril con 5% de rechazo por DIAN"
    ],
    'tipo': ['danger', 'warning', 'info']
})

# Datos para próximas acciones
acciones_data = pd.DataFrame({
    'accion': [
        "Renovar contrato de Juan Pérez (15/05)",
        "Revisar stock de Producto C y E",
        "Seguimiento a facturas vencidas",
        "Corregir nómina rechazada por DIAN"
    ]
})