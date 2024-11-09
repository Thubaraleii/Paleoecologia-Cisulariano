from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

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
