import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.sequence import pad_sequences
import data

# define the maximum sequence length (i.e., maximum number of vehicles)
max_sequence_length = 100

# define the input shape as a tuple with two dimensions: the sequence length and the number of features
input_shape = (max_sequence_length, 4)

# define the model
model = keras.Sequential([
    layers.LSTM(64, input_shape=input_shape),
    layers.Dense(4, activation='softmax')
])

# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# generate some example data (assuming a list of lists for the input)
# input_data is a list of input samples, where each input sample is a list of tuples (x, y, height, width) for each vehicle
input_data = data
labels = [[1,0,0,0],[0, 1, 0, 0],[0, 0, 1, 0],  [0, 0, 0, 1]]

# pad the input data to the maximum sequence length
padded_input_data = pad_sequences(input_data, maxlen=max_sequence_length, padding='post', dtype='float32')

# train the model
model.fit(padded_input_data, labels, epochs=10, batch_size=32)
