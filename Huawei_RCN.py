import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración del dashboard
st.set_page_config(
    page_title="Huawei - Dashboard de Tendencias",
    page_icon="📊",
    layout="wide"
)

st.title("🌐 Dashboard de Tendencias Tecnológicas - Huawei")

# Datos simulados
datos_oportunidades = pd.DataFrame({
    'Trimestre': ['2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', 
                  '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4'],
    'Tendencias': [3, 5, 7, 10, 12, 15, 18, 22]
})

categorias = ['Redes 6G', 'IA Generativa', 'Computación Cuántica', 'Blockchain', 'Algoritmos Energéticos']
sectores = ['Telecomunicaciones', 'Energía', 'IA', 'Cloud Computing', 'Finanzas']
impacto = np.array([
    [10, 6, 7, 5, 4],
    [7, 5, 10, 8, 6],
    [6, 4, 8, 10, 7],
    [5, 3, 6, 7, 10],
    [4, 9, 7, 6, 8]
])

datos_precision = pd.DataFrame({
    'Año': ['2022', '2023', '2024'],
    'Precisión': [65, 78, 85]
})

# Sidebar de Filtros
st.sidebar.header("📊 Filtros")
año_seleccionado = st.sidebar.selectbox("Seleccionar Año", ['2022', '2023', '2024'])

# KPIs principales
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tendencias Detectadas (2023)", "22", "10 vs 2022")
with col2:
    st.metric("Precisión Actual", "78%", "13% vs 2022")
with col3:
    st.metric("Sectores Impactados", "5", "2 nuevos en 2023")

# Gráfico de Líneas: Evolución de Oportunidades
st.subheader("📈 Evolución de Oportunidades Detectadas")
fig_linea = px.line(
    datos_oportunidades, x='Trimestre', y='Tendencias',
    markers=True, line_shape='linear',
    title='Evolución Trimestral de Oportunidades Detectadas'
)
st.plotly_chart(fig_linea, use_container_width=True)

# Mapa de Calor de Impacto por Sector
st.subheader("🔥 Mapa de Impacto por Sector")
fig_heatmap = go.Figure(data=go.Heatmap(
    z=impacto.tolist(),  # Convertir a lista para evitar errores
    x=sectores,
    y=categorias,
    colorscale='Viridis'
))
st.plotly_chart(fig_heatmap, use_container_width=True)

# Gráfico de Barras: Precisión del Modelo
st.subheader("📊 Precisión del Modelo Predictivo")
fig_barras = px.bar(
    datos_precision, x='Año', y='Precisión',
    title='Evolución de la Precisión del Modelo Predictivo',
    text='Precisión'
)
fig_barras.update_traces(texttemplate='%{text}%', textposition='outside')
st.plotly_chart(fig_barras, use_container_width=True)

# Embed para Genially (opcional)
st.subheader("📌 Integración con Genially")
st.markdown("""
    Si deseas integrar este dashboard en Genially, usa el siguiente código:
""")
st.code('<iframe src="https://tu-url-en-streamlit.app" width="1000" height="600"></iframe>', language="html")

