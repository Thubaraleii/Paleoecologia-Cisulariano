import numpy as np
import pandas as pd
from data_processing import load_data, preprocess_data
from model_training import build_model, train_model

df = load_data('data.csv')
X_train, X_val, y_train, y_val, scaler_X, scaler_y, df_unknown = preprocess_data(df)

model = build_model(X_train.shape[1])
model = train_model(model, X_train, y_train, X_val, y_val)

X_unknown = scaler_X.transform(df_unknown[['Profundidade (cm)']].values)

predicted_values_scaled = model.predict(X_unknown)
predicted_values = scaler_y.inverse_transform(predicted_values_scaled)

df.loc[df['Nível'].isin(['4B', '4C']), ['MOA', 'TOC', 'TS', 'U/Th', 'U(EF)']] = predicted_values

X_3B = scaler_X.transform(df[df['Nível'] == '3B'][['Profundidade (cm)']].values)
predicted_3B_scaled = model.predict(X_3B)
predicted_3B = scaler_y.inverse_transform(predicted_3B_scaled)

df_filled = df.copy()
df_filled.loc[df['Nível'] == '3B', ['MOA', 'TOC', 'TS', 'U/Th', 'U(EF)']] = predicted_3B
print('Tabela preenchida com valores previstos para os níveis 4B, 4C e validação do nível 3B:')
print(df_filled[['Nível', 'Profundidade (cm)', 'MOA', 'TOC', 'TS', 'U/Th', 'U(EF)']])
