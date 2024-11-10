
import pandas as pd
import matplotlib.pyplot as plt

# Data for the two tables based on the provided structure
data_table1 = {
    'Nível': ['4C', '4B', '4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A'],
    'Profundidade (cm)': [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    'MOA': [None, None, 327, 286, 248, 258, 289, 286, 338, 321, 266, 251, 190],
    'TOC': [None, None, 11.93, 12.11, 11.7, 12.01, 13.05, 8.79, 7.64, 5.73, 7.42, 12.41, 12.97],
    'TS': [None, None, 1.49, 1.96, 2.73, 4.54, 1.71, 1.24, 1.14, 3.87, 3.67, 1.73, 2.62],
    'TN': [None, None, 0.43, 0.46, 0.44, 0.43, 0.54, 0.24, 0.2, 0.39, 0.36, 0.52, 0.54],
    'U/Th': [None, None, 2.06, 1.98, 1.82, 1.81, 1.66, 1.35, 1.11, 1.11, 1.2, 1.51, 1.48]
}

data_table2 = {
    'Nível': ['4C', '4B', '4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A'],
    'Profundidade (cm)': [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    'Al2O3': [None, None, 14.13, 14.31, 13.69, 14.1, 13.62, 15.01, 14.65, 13.95, 14.89, 13.38, 13.12],
    'Fe2O3': [None, None, 7.06, 6.66, 6.41, 5.23, 7.41, 5.99, 6.89, 5.78, 5.25, 5.52, 4.94],
    'Cr2O3': [None, None, 0.039, 0.054, 0.037, 0.038, 0.037, 0.024, 0.042, 0.016, 0.019, 0.028, 0.028],
    'Na2O': [None, None, 0.38, 0.39, 0.33, 0.35, 0.86, 0.7, 0.89, 1.0, 1.28, 1.24, 1.37],
    'TiO2': [None, None, 0.57, 0.55, 0.59, 0.61, 0.6, 0.61, 0.6, 0.64, 0.64, 0.63, 0.63]
}

df_table1 = pd.DataFrame(data_table1)
df_table2 = pd.DataFrame(data_table2)

# Columns to plot for each table
table1_columns = ['MOA', 'TOC', 'TS', 'TN', 'U/Th']
table2_columns = ['Al2O3', 'Fe2O3', 'Cr2O3', 'Na2O', 'TiO2']

# Function to save Mod4 style plots
def save_mod4_plots(df, columns, filename_prefix):
    for column in columns:
        # Adjust filename to replace any problematic characters
        safe_column_name = column.replace("/", "_")
        
        plt.figure(figsize=(6, 10))
        plt.plot(df[column], df['Profundidade (cm)'], marker='o', linestyle='-', color='orange', label=column)
        plt.xlabel(f'{column}')
        plt.ylabel('Profundidade (cm)')
        plt.gca().invert_yaxis()  # Invert Y-axis for depth visualization
        plt.grid(True)
        plt.legend()
        
        # Saving each plot with safe filename
        plt.savefig(f'{filename_prefix}_{safe_column_name}.png', format='png')
        plt.close()

# Saving plots for both tables
save_mod4_plots(df_table1, table1_columns, 'mod4_table1')
save_mod4_plots(df_table2, table2_columns, 'mod4_table2')
