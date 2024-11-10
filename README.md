
# Fossils Depth Distribution Analysis

This repository contains code for generating depth distribution graphs of fossil compositions and chemical compounds, based on geological data.

## Files
- `generate_plots.py`: Python script to generate depth distribution plots.
- `README.md`: Project description and instructions.

## Usage
1. Ensure you have Python and the required packages installed:
   ```bash
   pip install pandas matplotlib
   ```

2. Run the script to generate the plots:
   ```bash
   python generate_plots.py
   ```

3. The generated plots will be saved in the current directory as `.png` files.

## Step-by-Step Screenshots
1. **Run Script**: Run `generate_plots.py` in your terminal or command prompt.
2. **Check Outputs**: After execution, check the current directory for saved plot images named as `mod4_table1_*` and `mod4_table2_*` for each variable.

# Geological Composition Statistics

This repository provides a Python script to calculate statistical summaries for geological composition data, such as min, max, mean, variance, and standard deviation.

## Files
- `calculate_stats.py`: Python script to generate statistics for each chemical composition column.
- `mod5.csv`: Output file containing the calculated statistics.

## Usage
1. Make sure you have Python and required packages installed:
   ```bash
   pip install pandas
   ```

2. Run the script to calculate the statistics:
   ```bash
   python calculate_stats.py
   ```

3. After running, the results will be saved to `mod5.csv` in the current directory.

## Example
The script calculates statistics for columns like Al2O3, Fe2O3, Cr2O3, etc., and outputs the following values for each:
- Minimum
- Maximum
- Mean
- Variance
- Standard Deviation

Check the `mod5.csv` file for detailed results.
