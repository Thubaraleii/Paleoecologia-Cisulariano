
# IDW Interpolation with Deep Learning for Geological Data

This repository implements an **Inverse Distance Weighting (IDW)** interpolation method enhanced with **Deep Learning** to improve spatial interpolation for geological data. The project is designed to predict missing values in geological datasets based on known spatial information, leveraging the flexibility of deep learning to improve prediction accuracy over traditional IDW methods.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Format](#dataset-format)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Background

Inverse Distance Weighting (IDW) is a widely used method for spatial interpolation, especially in geology, where it estimates unknown values by averaging the values of nearby known points, with weights inversely proportional to their distances. While IDW is effective, it can be improved by incorporating deep learning to better understand spatial relationships, even in complex terrains. 

This project combines IDW with a neural network model to enhance interpolation accuracy, training the model on known geological data and validating its performance on various missing data points.

## Features

- **IDW Interpolation**: Traditional spatial interpolation using Inverse Distance Weighting.
- **Deep Learning Model**: A neural network is trained to refine IDW predictions by learning spatial patterns.
- **Customizable Parameters**: Supports various distance weighting parameters and neural network architectures.
- **Validation and Visualization**: Tools for assessing model accuracy and visualizing interpolated data.

## Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/idw-deep-learning-geology.git
    cd idw-deep-learning-geology
    ```

2. **Set up a Python environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Prepare Data

Ensure your geological data is in a tabular format (e.g., CSV) with columns for `Depth`, `Latitude`, `Longitude`, and various geochemical measurements (e.g., mineral concentrations).

### 2. Train Model

Run the `train_model.py` script to train the neural network model on your geological data.

```bash
python train_model.py --data /path/to/your/data.csv --epochs 100 --batch_size 32
```

- `--data`: Path to the CSV file containing the geological data.
- `--epochs`: Number of epochs for training.
- `--batch_size`: Batch size for model training.

### 3. Perform Interpolation

Use the `interpolate.py` script to perform IDW interpolation with the trained model.

```bash
python interpolate.py --data /path/to/your/data.csv --output interpolated_results.csv
```

- `--data`: Path to the CSV file containing the known geological data.
- `--output`: Path to save the interpolated results.

### 4. Visualize Results

You can use `visualize_results.py` to create plots of the interpolated values.

```bash
python visualize_results.py --input interpolated_results.csv
```

## Dataset Format

Your dataset should be a CSV file with the following columns:

- `Depth`: Depth or elevation of the geological sample point.
- `Latitude`: Latitude coordinate.
- `Longitude`: Longitude coordinate.
- Columns for each geological measurement (e.g., `Al2O3`, `Fe2O3`, `Cr2O3`).

Example:

| Depth | Latitude | Longitude | Al2O3 | Fe2O3 | Cr2O3 |
|-------|----------|-----------|-------|-------|-------|
| 10    | -23.5    | 45.6      | 14.13 | 7.06  | 0.039 |
| 35    | -23.6    | 45.7      | 13.69 | 6.41  | 0.037 |

## Model Training

The `train_model.py` script trains a deep learning model that can refine IDW interpolations. The model learns spatial patterns from known data points and can predict unknown values more accurately than traditional IDW.

## Results

After training, you can evaluate the model using common regression metrics (e.g., RMSE, MAE). The trained model can then be used to perform interpolation on new geological datasets, with the results saved to an output file.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
