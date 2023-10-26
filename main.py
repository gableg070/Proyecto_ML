import sys
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def ValidarNumero(columna):
    while True:
        entrada = input("Ingrese el valor de {}:".format(columna))
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta_ escriba un numero válido")
    return entrada;


Ek = ValidarNumero('EK')

MODEL_PATH = 'model.h5'

# Load Tensorflow model
model = keras.models.load_model(MODEL_PATH)

#padded = pad_sequences(sequences, maxlen=MAX_LENGTH, padding=PADDING_TYPE, truncating=TRUNC_TYPE)

print(model.predict([Ek]))



