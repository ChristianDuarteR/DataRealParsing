import pandas as pd
from matplotlib import pyplot as plt

from graphs import (
    plot_height_distribution,
    plot_weight_distribution,
    plot_department_distribution,
    plot_gender_distribution,
    plot_college_mark_distribution,
    plot_hobbies_distribution,
    plot_stress_level_distribution,
    plot_financial_status_distribution,
    plot_part_time_job_distribution,
    plot_correlation_matrix,
    plot_study_preference_vs_career_satisfaction,
    analyze_hobbies_and_stress_level, analyze_salary_vs_travel_time,

)
import csv

def parse_csv(csv_file):
    return pd.read_csv(csv_file)

if __name__ == '__main__':
    # Parsear el archivo CSV
    data = parse_csv('files/Student Attitude and Behavior.csv')

    # Visualizaciones
    plot_height_distribution(data)
    plot_weight_distribution(data)
    plot_department_distribution(data)
    plot_gender_distribution(data)
    plot_college_mark_distribution(data)
    plot_hobbies_distribution(data)
    plot_stress_level_distribution(data)
    plot_financial_status_distribution(data)
    plot_part_time_job_distribution(data)
    plot_correlation_matrix(data)
    plot_study_preference_vs_career_satisfaction(data)
    analyze_hobbies_and_stress_level(data)
    analyze_salary_vs_travel_time(data)