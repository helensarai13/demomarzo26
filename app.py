import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Mi Aplicación Streamlit con DataFrame y Gráfica - hola soy helen y estoy estudiando fundamentos para el analisis de datos')
st.title('Mi Aplicación Streamlit con DataFrame y Gráfica')

# 1. Crear un DataFrame de ejemplo
st.header('DataFrame de Ejemplo')
data = {
    'Fecha': pd.to_datetime(pd.date_range(start='2023-01-01', periods=10)),
    'Valor_A': np.random.rand(10) * 100,
    'Valor_B': np.random.rand(10) * 50 + 20
}
df = pd.DataFrame(data)

st.dataframe(df)

# 2. Crear una gráfica de línea
st.header('Gráfica de Línea de Valor_A y Valor_B')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Fecha'], df['Valor_A'], label='Valor A', marker='o')
ax.plot(df['Fecha'], df['Valor_B'], label='Valor B', marker='x')
ax.set_xlabel('Fecha')
ax.set_ylabel('Valores')
ax.set_title('Tendencia de Valores a lo largo del tiempo')
ax.legend()
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

st.write("""
**Cómo ejecutar esta aplicación:**
1. Asegúrate de tener Streamlit instalado (`pip install streamlit pandas numpy matplotlib`).
2. Guarda este código en un archivo llamado `app.py`.
3. Abre tu terminal, navega al directorio donde guardaste `app.py`.
4. Ejecuta el comando: `streamlit run app.py`
""")
