import matplotlib.pyplot as plt

def plot_vehicle_year_distribution(data):
    years = [int(entry['year']) for entry in data]
    plt.hist(years, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de vehículos')
    plt.title('Distribución de años de los vehículos')
    plt.grid(True)
    plt.show()