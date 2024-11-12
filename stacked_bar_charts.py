
import matplotlib.pyplot as plt
import numpy as np

# Data manually extracted from the provided image
data = {
    'Nível': ['4C', '4B', '4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A'],
    'Profundidade (cm)': [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    '2010': [None, 92, 30, 33, 51, 200, 57, 19, 20, 20, 6, 4, 0],
    '2011': [71, 100, 104, 166, 52, 241, 113, 52, 40, 64, 45, 10, 0],
    '2016': [0, 57, 34, 47, 19, 68, 22, 19, 31, 21, 13, 4, 6],
    '2016L': [4, 8, 10, 11, 6, 12, 4, 5, 4, 6, 5, 0, 5]
}

# Convert data to stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define order of levels to align 1A at the base and 4C at the top
levels_order = ['1A', '1B', '1C', '1D', '2A', '2B', '3A', '3B', '3C', '3D', '4A', '4B', '4C']
bottom = np.zeros(len(data['Nível']))

# Plot each year as a stacked bar component with 1A at the base
years = ['2010', '2011', '2016', '2016L']
for year in years:
    values = [data[year][data['Nível'].index(level)] for level in levels_order]
    ax.barh(levels_order, values, label=year, left=bottom)
    bottom += np.array(values)

# Add labels and legend
ax.set_xlabel('Valores')
ax.set_ylabel('Nível')
ax.set_title('Distribuição de Valores por Ano e Nível (com 1A na Base)')
ax.legend(title="Ano", loc="upper right")
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
