
import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_charts_from_csv(file_path):
    """
    Processa um arquivo CSV contendo profundidades e outras colunas de teores e gera gráficos automaticamente.

    Args:
        file_path (str): Caminho do arquivo CSV.
    """
    # Ler o arquivo CSV
    df = pd.read_csv(file_path)
    
    # Garantir que a coluna de profundidade exista
    if "PROFU" not in df.columns:
        raise ValueError("O arquivo CSV deve conter uma coluna chamada 'PROFU' representando profundidade.")
    
    # Verificar a profundidade dentro do intervalo esperado (0 a 114 cm)
    if df["PROFU"].min() < 0 or df["PROFU"].max() > 114:
        raise ValueError("As profundidades no arquivo CSV devem estar no intervalo de 0 a 114 cm.")
    
    # Identificar colunas para análise (todas, exceto profundidade)
    data_columns = [col for col in df.columns if col != "PROFU"]
    
    # Criar uma pasta de saída para salvar os gráficos gerados
    output_dir = "graficos_gerados"
    os.makedirs(output_dir, exist_ok=True)
    
    # Gerar gráficos para cada coluna de dados
    for col in data_columns:
        plt.figure(figsize=(8, 6))
        plt.plot(df[col], df["PROFU"], marker='o', linestyle='-', label=col)
        plt.gca().invert_yaxis()  # Inverter eixo Y (profundidade aumenta para baixo)
        plt.title(f'Profundidade Média (cm) vs {col}')
        plt.xlabel(col)
        plt.ylabel('Profundidade Média (cm)')
        plt.grid(alpha=0.5)
        plt.legend()
        
        # Salvar o gráfico na pasta de saída
        output_path = os.path.join(output_dir, f"{col}_vs_PROFUNDADE.png")
        plt.savefig(output_path)
        plt.close()
    
    print(f"Gráficos gerados e salvos na pasta '{output_dir}'.")
