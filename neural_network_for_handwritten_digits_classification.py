# -*- coding: utf-8 -*-
"""Neural Network For Handwritten Digits Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uexydbxh4Q5y7SV1Uqdk_7rqVAFo_Ly0
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = keras.datasets.mnist.load_data()

x_train = x_train/255
x_test = x_test/255

for i in range (9):
  print(y_train[i])
  plt.matshow(x_train[i])

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(10,activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10)

model.evaluate(x_test,y_test)

y_pred = model.predict(x_test)
y_pred[7]

np.argmax(y_pred[7])

y_pred = [np.argmax(i) for i in y_pred]
y_pred[:5]

cm = tf.math.confusion_matrix(y_test,y_pred)
cm

import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')