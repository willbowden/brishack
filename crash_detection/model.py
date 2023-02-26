from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import SGD
import json


# def create_model(modelName: str):
#     with open(f"{modelName}.json", "r") as infile:
#       config = json.load(infile)

#     model = Sequential()
#     model.add(LSTM(config['units'], return_sequences=True, batch_input_shape=(None, config['sequence_length'], config['n_features'])))
#     model.add(Dropout(config['dropout']))
#     model.add(LSTM(config['units'], return_sequences=False))
#     model.add(Dropout(config['dropout']))
#     model.add(Dense(1, activation="linear"))

#     model.compile(loss=config['loss'], metrics=["accuracy", "mean_absolute_error"], optimizer=config['optimizer'])
#     model_path = f"{modelName}"
#     model.save(model_path)
#     return 