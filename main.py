from midi_to_text import data_parse
from text_to_midi import data_form
from data_collector import data_format
from split_sequence import split_sequence
import py_midicsv as pm
from numpy import asarray
from tensorflow.keras import Sequential
from tensorflow.keras.layers import *
import tensorflow as tf


raw_midi = data_format()
data = data_parse(raw_midi)
print(data)
length = 500
epochs = 5
batch_size = 256

X, y = split_sequence(data)
X = X.reshape((1, len(X), 3))
X = tf.cast(X, dtype='float32')

notes = [[181, 60, 127]]

model = Sequential()
model.add(LSTM(256, activation='sigmoid', return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, activation='sigmoid', return_sequences=True))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(3, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

for i in range(length):
    model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=2)
    # 8 or 16 batch size is optimal, 16 has a bit more diversity
    # 1 epoch has nice diversity, 5 has average in 50s, 10 has average in 60s, 50 not bad but 1-2-1-2 not distinguished
    # 100 epochs has average in 60s, takes too long

    prediction = model.predict(asarray(notes).reshape((1, -1, 3)))
    prediction[0][0] = (prediction[0][0] * 384) - (prediction[0][0] * 0) + 0
    prediction[0][1] = (prediction[0][1] * 384) - (prediction[0][1] * 0) + 0
    prediction[0][2] = (prediction[0][2] * 384) - (prediction[0][2] * 0) + 0
    print(prediction)
    notes.append([prediction[0][0], prediction[0][1], prediction[0][2]])

    print('Note ' + str(i + 1) + ' of ' + str(length))

notes.remove(notes[0])
notes.remove(notes[0])
notes.remove(notes[0])
notes.remove(notes[0])
notes.remove(notes[0])
print(notes)

midi_data = data_form(notes)
midi_object = pm.csv_to_midi(midi_data)

if input('Save file? y/n:').lower().startswith('y'):
    file_name = input('File name: ')
    file_name += '.mid'
    with open(file_name, "wb") as output_file:
        midi_writer = pm.FileWriter(output_file)
        midi_writer.write(midi_object)

print('Done')
