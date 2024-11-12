
import matplotlib.pyplot as plt

# Data for the pie and bar charts
levels = ['4C', '4B', '4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A']
fossil_whole_percent = [None, None, 1.37, 6.56, 11.2, 41.26, 9.02, 6.83, 7.1, 9.29, 4.37, 1.09, 1.64]
fossil_fragments_percent = [None, 11.92, 10.04, 14.62, 23.21, 10.23, 5.96, 4.83, 6.33, 3.32, 0.63, 0.5]

# Clean data for pie charts
levels_fossil = ['4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A']
fossil_whole_percent_cleaned = [1.37, 6.56, 11.2, 41.26, 9.02, 6.83, 7.1, 9.29, 4.37, 1.09, 1.64]
fossil_fragments_percent_cleaned = [11.92, 10.04, 14.62, 23.21, 10.23, 5.96, 4.83, 6.33, 3.32, 0.63, 0.5]

# Pie chart for "Fósseis Inteiro (%)"
plt.figure(figsize=(8, 8))
plt.pie(fossil_whole_percent_cleaned, labels=levels_fossil, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Fósseis Inteiros (%) por Nível')
plt.show()

# Pie chart for "Fragmentos Fósseis (%)"
plt.figure(figsize=(8, 8))
plt.pie(fossil_fragments_percent_cleaned, labels=levels_fossil, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Fragmentos Fósseis (%) por Nível')
plt.show()

# Data for bar chart with fossil counts by levels
levels_reordered = ['1A', '1B', '1C', '1D', '2A', '2B', '3A', '3B', '3C', '3D', '4A', '4B', '4C']
fossil_counts_reordered = [11, 14, 69, 111, 95, 120, 196, 521, 274, 181, 195, 167, 0]

# Horizontal bar chart with '1A' at the base
plt.figure(figsize=(10, 6))
plt.barh(levels_reordered, fossil_counts_reordered, color='orange')
plt.xlabel('Número total de fósseis')
plt.ylabel('Níveis')
plt.title('Distribuição do Número Total de Fósseis por Nível (com 1A na Base)')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
