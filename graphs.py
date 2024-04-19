import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, stats


def plot_height_distribution(data):
    heights = data['Height(CM)']
    plt.hist(heights, bins=20, color='#86bf91', edgecolor='black')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Alturas')
    plt.grid(True)
    plt.show()

def plot_weight_distribution(data):
    weights = data['Weight(KG)']
    plt.hist(weights, bins=20, color='#86bf91', edgecolor='black')
    plt.xlabel('Peso (kg)')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Pesos')
    plt.grid(True)
    plt.show()

def plot_department_distribution(data):
    department_counts = data['Department'].value_counts()
    sns.barplot(x=department_counts.index, y=department_counts.values, palette='Blues_d')
    plt.xlabel('Departamento')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución por Departamento')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_gender_distribution(data):
    gender_counts = data['Gender'].value_counts()
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='Blues_d')
    plt.xlabel('Género')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución por Género')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_college_mark_distribution(data):
    plt.hist(data['college mark'], bins=20, color='#86bf91', edgecolor='black')
    plt.xlabel('Calificación Universitaria')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Calificaciones Universitarias')
    plt.grid(True)
    plt.show()

def plot_hobbies_distribution(data):
    hobbies_counts = data['hobbies'].value_counts()
    sns.barplot(x=hobbies_counts.index, y=hobbies_counts.values, palette='Blues_d')
    plt.xlabel('Hobbies')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Hobbies')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_stress_level_distribution(data):
    stress_level_counts = data['Stress Level '].value_counts()
    sns.barplot(x=stress_level_counts.index, y=stress_level_counts.values, palette='Blues_d')
    plt.xlabel('Nivel de Estrés')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Niveles de Estrés')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_financial_status_distribution(data):
    financial_status_counts = data['Financial Status'].value_counts()
    sns.barplot(x=financial_status_counts.index, y=financial_status_counts.values, palette='Blues_d')
    plt.xlabel('Estado Financiero')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Estados Financieros')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_part_time_job_distribution(data):
    part_time_job_counts = data['part-time job'].value_counts()
    sns.barplot(x=part_time_job_counts.index, y=part_time_job_counts.values, palette='Blues_d')
    plt.xlabel('Trabajo de Medio Tiempo')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Trabajos de Medio Tiempo')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(data):
    data_df = pd.DataFrame(data)

    # Lista de columnas numéricas
    numeric_columns = ['Height(CM)', 'Weight(KG)', '10th Mark', '12th Mark', 'college mark']

    # Convertir las columnas numéricas a tipo float, manejando los valores no numéricos como NaN
    for column in numeric_columns:
        data_df[column] = pd.to_numeric(data_df[column], errors='coerce')

    # Eliminar columnas no numéricas
    data_numeric = data_df[numeric_columns]

    # Calcular la matriz de correlación
    corr_matrix = data_numeric.corr()

    # Visualizar la matriz de correlación
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlación')
    plt.show()


def plot_study_preference_vs_career_satisfaction(data):
    sns.countplot(x='prefer to study in', hue='willingness to pursue a career based on their degree  ', data=data)
    plt.title('Preferencia de Estudio vs Satisfacción con la Carrera')
    plt.xlabel('Prefer to Study In')
    plt.ylabel('Count')
    plt.show()

def analyze_hobbies_and_stress_level(data):
    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(data)

    # Filtrar columnas relevantes
    filtered_data = df[['hobbies', 'Stress Level ']]

    # Calcular la tabla de contingencia
    contingency_table = pd.crosstab(filtered_data['hobbies'], filtered_data['Stress Level '])

    # Visualizar los resultados
    plt.figure(figsize=(10, 6))
    sns.heatmap(contingency_table, annot=True, cmap='coolwarm', fmt='d')
    plt.title('Relación entre Hobbies y Niveles de Estrés')
    plt.xlabel('Nivel de Estrés')
    plt.ylabel('Hobbies')
    plt.show()

def analyze_salary_vs_travel_time(data):
    time_range_mapping = {
        '0 - 30 minutes': 'Menos de media hora',
        '30 - 60 minutes': 'de media hora a 1 hora',
        '1 - 1.30 hour': 'De 1 hora a hora y media',
        '2 - 2.30 hour': 'De 2 horas a 2 horas y media',
        'more than 3 hour': 'Mas de 3 horas'
    }

    data['Travelling Time '] = data['Travelling Time '].map(time_range_mapping)

    # Visualizar la relación entre la expectativa salarial y el tiempo de viaje
    plt.figure(figsize=(12, 4))
    sns.violinplot(data=data, x='Travelling Time ', y='salary expectation', inner='quartile')
    plt.title('Expectativa Salarial vs. Tiempo de Viaje')
    plt.xlabel('Tiempo de Viaje')
    plt.ylabel('Expectativa Salarial (en miles)')
    plt.grid(True)
    plt.show()