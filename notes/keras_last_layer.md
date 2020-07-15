# keras classification 
last layer: 
c = # of classes 
for 4 classes 
c = 4
choose activation: softmax

model.add(tf.keras.layers.Dense(c, activation='softmax'))


model.compile(loss='sparse_categorical_crossentropy'
			metrics=['accuracy']

# Keras Regression 
last layer just one neuron 
model.add(tf.keras.layers.Dense(1))
model.comple(loss='mae'
			metrics=['mae', 'mse']