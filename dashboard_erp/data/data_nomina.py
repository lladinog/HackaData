# data/data_nomina.py
import pandas as pd

# Datos para los KPI
kpi_data = pd.DataFrame({
    'titulo': ['Empleados Activos', 'Costo Nómina Mes', 'Salario Promedio', 'Contratos a Renovar'],
    'valor': ['48', '$29,500,000', '$614,583', '3'],
    'icono': ['fas fa-users', 'fas fa-money-bill', 'fas fa-coins', 'fas fa-file-contract'],
    'color': ['info', 'primary', 'success', 'warning']
})

# Datos históricos de nómina
payroll_data = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Total_Nomina': [28000000, 28500000, 29000000, 29500000],
    'Empleados': [45, 46, 47, 48]
})

# Datos para el gráfico de estado DIAN
dian_data = pd.DataFrame({
    'Estado': ['Aceptada', 'Rechazada'],
    'Porcentaje': [95, 5]
})

# Datos de contratos a renovar
contratos_data = pd.DataFrame({
    'Nombre': ['Juan Pérez', 'María Gómez', 'Carlos Ruiz'],
    'Fecha_Renovacion': ['15/05/2023', '22/05/2023', '30/05/2023']
})

# Datos de distribución de nómina
distribucion_nomina = pd.DataFrame({
    'Concepto': ['Salarios', 'Prestaciones', 'Bonos', 'Seguridad Social'],
    'Valor': [22000000, 4500000, 2000000, 1000000]
})