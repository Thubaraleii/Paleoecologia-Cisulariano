
import pandas as pd
import numpy as np

# Define data_table2 as a DataFrame
data_table2 = {
    'Nível': ['4C', '4B', '4A', '3D', '3C', '3B', '3A', '2B', '2A', '1D', '1C', '1B', '1A'],
    'Profundidade (cm)': [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    'Al2O3': [None, None, 14.13, 14.31, 13.69, 14.1, 13.62, 15.01, 14.65, 13.95, 14.89, 13.38, 13.12],
    'Fe2O3': [None, None, 7.06, 6.66, 6.41, 5.23, 7.41, 5.99, 6.89, 5.78, 5.25, 5.52, 4.94],
    'Cr2O3': [None, None, 0.039, 0.054, 0.037, 0.038, 0.037, 0.024, 0.024, 0.016, 0.019, 0.028, 0.028],
    'Na2O': [None, None, 0.38, 0.30, 0.33, 0.35, 0.86, 0.7, 0.87, 1.41, 1.28, 1.24, 1.37],
    'TiO2': [None, None, 0.57, 0.55, 0.59, 0.61, 0.6, 0.61, 0.61, 0.62, 0.64, 0.61, 0.63]
}
df2 = pd.DataFrame(data_table2)

# IDW function to calculate missing values
def idw_interpolation(x_known, y_known, x_unknown, power=2):
    """Performs Inverse Distance Weighting (IDW) interpolation for missing values."""
    weights = 1 / np.abs(x_known - x_unknown) ** power
    interpolated_value = np.sum(weights * y_known) / np.sum(weights)
    return interpolated_value

# Remove the row with 'Nível' == '3B' for cross-validation
df2_no_3b = df2[df2['Nível'] != '3B'].reset_index(drop=True)
df2_only_3b = df2[df2['Nível'] == '3B']

# Define columns to interpolate
columns_to_interpolate = ['Al2O3', 'Fe2O3', 'Cr2O3', 'Na2O', 'TiO2']

# Perform IDW to predict values for '3B' based on remaining data
predicted_values = {}
for column in columns_to_interpolate:
    # Get known values and depths for IDW calculation
    known_depths = df2_no_3b['Profundidade (cm)'][df2_no_3b[column].notna()]
    known_values = df2_no_3b[column][df2_no_3b[column].notna()]
    
    # Calculate interpolated value for '3B' depth (82 cm)
    predicted_value = idw_interpolation(known_depths.values, known_values.values, df2_only_3b['Profundidade (cm)'].values[0])
    predicted_values[column] = predicted_value

# Convert predicted values to DataFrame
predicted_df = pd.DataFrame(predicted_values, index=['Predicted for 3B'])

# Actual values for comparison
actual_values_df = df2_only_3b[columns_to_interpolate].reset_index(drop=True).rename(index={0: 'Actual for 3B'})

# Combine actual and predicted values for comparison
cross_validation_df = pd.concat([actual_values_df, predicted_df])

# Print the cross-validation results
print(cross_validation_df)
