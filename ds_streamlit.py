import streamlit as st
import pandas as pd
import seaborn as sns

# Carregar os dados
df = pd.read_csv('health_data.csv')

# Contagem de diagnósticos
diagnosis_counts = df['Diagnosis'].value_counts()

st.title("Análise de Dados de Saúde 🏥")

st.header("Distribuição de Diagnósticos em 2024")
st.bar_chart(diagnosis_counts)

# Boxplot para Blood_Pressure
st.header("Variação da Pressão Arterial por Diagnóstico")
blood_pressure_fig = sns.boxplot(data=df, x='Diagnosis', y='Blood_Pressure', palette="Set2")
st.pyplot(blood_pressure_fig.figure)

# Boxplot para Cholesterol_Level
st.header("Variação do Nível de Colesterol por Diagnóstico")
cholesterol_fig = sns.boxplot(data=df, x='Diagnosis', y='Cholesterol_Level', palette="Set2")
st.pyplot(cholesterol_fig.figure)

# Filtrar pacientes com colesterol alto
high_chol = df[df['Cholesterol_Level'] > 200]
high_chol_counts = high_chol['Diagnosis'].value_counts()

# Gráfico de pizza
st.header("Pacientes com Colesterol > 200 mg/dL por Diagnóstico")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.pie(high_chol_counts, labels=high_chol_counts.index, autopct='%1.1f%%',
       colors=sns.color_palette("pastel"), startangle=90)
ax.set_title("Distribuição de Pacientes com Alto Colesterol")
st.pyplot(fig)
