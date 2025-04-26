import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título principal
st.title("Análise de Dados de Saúde 🏥")
st.subheader("Desafio Individual | Aluna: Ayanne Almeida")

st.header("1. Análise Exploratória Inicial (Distribuição de Diagnósticos)")
# 1. Análise Exploratória Inicial (Distribuição de Diagnósticos)

# Carregar os dados
df = pd.read_csv('health_data.csv')

# Contagem de diagnósticos
diagnosis_counts = df['Diagnosis'].value_counts()

st.header("Distribuição de Diagnósticos em 2024")
st.bar_chart(diagnosis_counts)

# 2. Comparação de Pressão Arterial e Colesterol por Diagnóstico

# Boxplot para Blood_Pressure
st.header("Variação da Pressão Arterial por Diagnóstico")
blood_pressure_fig, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Diagnosis', y='Blood_Pressure', palette="Set2", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(blood_pressure_fig)

# Boxplot para Cholesterol_Level
st.header("Variação do Nível de Colesterol por Diagnóstico")
cholesterol_fig, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Diagnosis', y='Cholesterol_Level', palette="Set2", ax=ax2)
plt.xticks(rotation=45)
st.pyplot(cholesterol_fig)

# 3. Identificação de Pacientes com Colesterol Alto (>200)

# Filtrar pacientes com colesterol alto
high_chol = df[df['Cholesterol_Level'] > 200]
high_chol_counts = high_chol['Diagnosis'].value_counts()

# Gráfico de pizza
st.header("Pacientes com Colesterol > 200 mg/dL por Diagnóstico")
fig, ax3 = plt.subplots()
ax3.pie(high_chol_counts, labels=high_chol_counts.index, autopct='%1.1f%%',
        colors=sns.color_palette("pastel"), startangle=90)
ax3.set_title("Distribuição de Pacientes com Alto Colesterol")
st.pyplot(fig)

# Conclusão
st.header("Conclusão")
st.markdown("""
- **Diabetes** se destaca como o diagnóstico mais comum.
- *Pacientes diabéticos* têm pressão arterial consistentemente mais alta que outros grupos, reforçando a necessidade de monitoramento integrado.
- *Asmáticos* apresentam valores próximos aos saudáveis, sugerindo que a asma não impacta significativamente a pressão arterial.
- *Pacientes Diabéticos e Asmáticos* devem ser priorizados em programas de monitoramento de colesterol.
- *Intervenções* como ajustes na dieta e aumento da atividade física podem ser benéficas.
- *Pacientes Hipertensos*: embora tenham uma mediana de colesterol mais baixa, a presença de valores máximos altos indica risco em alguns casos, necessitando avaliações individuais.
""")
