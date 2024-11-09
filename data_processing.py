import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    df_known = df.dropna()
    df_unknown = df[df[['MOA', 'TOC', 'TS', 'U/Th', 'U(EF)']].isna().any(axis=1)]

    X = df_known[['Profundidade (cm)']].values
    y = df_known[['MOA', 'TOC', 'TS', 'U/Th', 'U(EF)']].values

    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)

    X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    return X_train, X_val, y_train, y_val, scaler_X, scaler_y, df_unknown
