
import pandas as pd

# Sample data for demonstration (replace with actual data if available)
data = {
    'Profundidade (cm)': [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    'Al2O3': [None, None, 14.13, 14.31, 13.69, 14.1, 13.62, 15.01, 14.65, 13.95, 14.89, 13.38, 13.12],
    'Fe2O3': [None, None, 7.06, 6.66, 6.41, 5.23, 7.41, 5.99, 6.89, 5.78, 5.25, 5.25, 4.94],
    'Cr2O3': [None, None, 0.039, 0.054, 0.037, 0.038, 0.037, 0.024, 0.042, 0.031, 0.019, 0.028, 0.028],
    'Na2O': [None, None, 0.38, 0.39, 0.33, 0.35, 0.86, 0.7, 0.89, 1.0, 1.28, 1.24, 1.37],
    'TiO2': [None, None, 0.57, 0.55, 0.53, 0.61, 0.6, 0.61, 0.6, 0.64, 0.58, 0.63, 0.63]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to calculate statistics
def calculate_stats(df):
    stats = {}
    for column in df.columns[1:]:  # Skip "Profundidade (cm)"
        col_data = df[column].dropna()  # Remove NaN values for calculations
        stats[column] = {
            'min': col_data.min(),
            'max': col_data.max(),
            'mean': col_data.mean(),
            'variance': col_data.var(),
            'std_dev': col_data.std()
        }
    return pd.DataFrame(stats).T

# Calculate and save statistics to CSV
stats_df = calculate_stats(df)
stats_df.to_csv("mod5.csv", index=True)
print("Statistics saved to mod5.csv")
