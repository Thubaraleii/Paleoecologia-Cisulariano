import matplotlib.pyplot as plt
import pandas as pd

# Create the data manually
data = {
    "Subnível": ["4A", "3D", "3C", "3B", "3A", "2B", "2A", "1D", "1C", "1B", "1A"],
    "PORIFERA": [0, 5, 5, 5, 10, 5, 10, 0, 0, 0, 0],
    "PEIXES COMPLETOS": [0, 5, 10, 3, 3, 0, 5, 0, 3, 5, 5],
    "LINGUIFORMES": [0, 10, 5, 5, 10, 10, 10, 7, 10, 0, 0],
    "ORBICULOIDEA": [0, 0, 10, 3, 10, 0, 0, 5, 0, 3, 0],
}

# Create a DataFrame
df = pd.DataFrame(data)
df.set_index("Subnível", inplace=True)

# Define the plotting function
def gerar_grafico_mod1(coluna_dados, labels):
    plt.figure(figsize=(5, 7))
    plt.plot(coluna_dados, labels, marker='o', color='purple', linestyle='-', linewidth=2)
    plt.gca().invert_yaxis()  # Invert the Y-axis for depth representation
    plt.xlabel("Valores")
    plt.ylabel("Subníveis")
    plt.grid(visible=True, linestyle="--", linewidth=0.5)
    plt.title('Gráfico Mod1: PORIFERA')
    plt.show()

# Extract the necessary data
coluna_dados = df["PORIFERA"]  # Values for PORIFERA
labels = df.index.tolist()  # Subníveis

# Generate the plot
gerar_grafico_mod1(coluna_dados, labels)