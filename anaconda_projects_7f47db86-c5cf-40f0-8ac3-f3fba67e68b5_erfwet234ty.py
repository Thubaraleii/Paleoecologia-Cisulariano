

import numpy as np

def inverse_distance_weighting_corrected(known_depths, known_values, missing_depths, power=2):
    \"\"\"
    Função para calcular valores usando Interpolação por Distância Inversa (IDW).
    
    Parâmetros:
    - known_depths: profundidades conhecidas (array-like).
    - known_values: valores conhecidos correspondentes às profundidades conhecidas.
    - missing_depths: profundidades onde os valores serão estimados (array-like).
    - power: potência usada no cálculo de IDW (default: 2).
    
    Retorna:
    - np.array com valores estimados para as profundidades ausentes.
    \"\"\"
    estimates = []
    
    for missing_depth in missing_depths:
        # Calculando as distâncias para o ponto de profundidade desconhecida
        distances = np.abs(known_depths - missing_depth)
        
        # Evitar divisão por zero
        distances[distances == 0] = 1e-10
        
        # Pesos baseados nas distâncias
        weights = 1 / (distances ** power)
        
        # Cálculo IDW
        estimate = np.sum(weights * known_values) / np.sum(weights)
        estimates.append(estimate)
    
    return np.array(estimates)

