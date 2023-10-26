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


#list_columns = ['Mean_Integrated', 'SD', 'EK', 'Skewness', 'Mean_DMSNR_Curve', 'SD_DMSNR_Curve',
   #             'EK_DMSNR_Curve', 'Skewness_DMSNR_Curve']

#listData = []

#for element in list_columns:
 #   listData.append(ValidarNumero(element))

Ek = ValidarNumero('EK')

#df_test = pd.DataFrame([listData], columns=list_columns)
#print(df_test)


MAX_LENGTH = 100
PADDING_TYPE = 'post'
TRUNC_TYPE = 'post'
MODEL_PATH = 'model.h5'

# Load Tensorflow model
model = keras.models.load_model(MODEL_PATH)

#padded = pad_sequences(sequences, maxlen=MAX_LENGTH, padding=PADDING_TYPE, truncating=TRUNC_TYPE)

print(model.predict([Ek]))



