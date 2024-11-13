from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

data_2 = {
    "Nivel": ["4C", "4B", "4A", "3D", "3C", "3B", "3A", "2B", "2A", "1D", "1C", "1B", "1A"],
    "Profundidade (cm)": [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    "MOA": [None, None, 327, 286, 248, 258, 289, 286, 338, 321, 266, 251, 190],
    "TS": [None, None, 1.49, 1.96, 2.73, 4.54, 1.71, 1.24, 1.72, 3.98, 3.67, 1.73, 2.62],
    "TOC": [None, None, 11.93, 12.11, 11.7, 12.01, 13.05, 8.79, 7.69, 5.73, 7.42, 12.41, 12.97],
    "TN": [None, None, 0.43, 0.46, 0.44, 0.43, 0.54, 0.32, 0.29, 0.3, 0.26, 0.52, 0.54]
}

data = {
    "Nivel": ["4C", "4B", "4A", "3D", "3C", "3B", "3A", "2B", "2A", "1D", "1C", "1B", "1A"],
    "Profundidade (cm)": [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    "Fe2O3": [None, None, 7.06, 6.66, 6.41, 5.23, 7.41, 5.99, 6.89, 5.78, 5.25, 5.52, 4.94],
    "U/Th": [None, None, 2.06, 1.98, 1.82, 1.81, 1.66, 1.35, 1.28, 1.14, 1.17, 1.51, 1.48],
    "Al2O3": [None, None, 14.13, 14.31, 13.69, 14.1, 13.62, 15.01, 14.65, 14.04, 14.89, 13.38, 13.12],
    "TiO2": [None, None, 0.57, 0.56, 0.59, 0.61, 0.62, 0.61, 0.65, 0.63, 0.64, 0.61, 0.63]
}
def build_model(input_shape):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_shape,)),
        Dense(64, activation='relu'),
        Dense(5)
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
    return model

def train_model(model, X_train, y_train, X_val, y_val, epochs=200, batch_size=8):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val), verbose=1)
    return model
    # Criando o DataFrame com base na nova imagem fornecida
data_2 = {
    "Nivel": ["4C", "4B", "4A", "3D", "3C", "3B", "3A", "2B", "2A", "1D", "1C", "1B", "1A"],
    "Profundidade (cm)": [10, 35, 45, 60, 68, 82, 86.5, 94.5, 100, 106, 110, 111.5, 114],
    "MOA": [None, None, 327, 286, 248, 258, 289, 286, 338, 321, 266, 251, 190],
    "TS": [None, None, 1.49, 1.96, 2.73, 4.54, 1.71, 1.24, 1.72, 3.98, 3.67, 1.73, 2.62],
    "TOC": [None, None, 11.93, 12.11, 11.7, 12.01, 13.05, 8.79, 7.69, 5.73, 7.42, 12.41, 12.97],
    "TN": [None, None, 0.43, 0.46, 0.44, 0.43, 0.54, 0.32, 0.29, 0.3, 0.26, 0.52, 0.54]
}

# Convertendo para DataFrame
df_2 = pd.DataFrame(data_2)

# Calculando a média, o mínimo e o máximo de cada coluna relevante
stats_2 = df_2[["MOA", "TS", "TOC", "TN"]].agg(['mean', 'min', 'max'])

# Exibindo os resultados
tools.display_dataframe_to_user(name="Estatísticas de MOA, TS, TOC e TN", dataframe=stats_2)

