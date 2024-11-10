
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
