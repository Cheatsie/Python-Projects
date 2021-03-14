import tensorflow as tf

# Load and Prepare MnistDataSet
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the tf.keras.Sequential model by stacking layers.
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
# For each example the model returns a vector of "logits" or "log-odds" scores, one for each class.
predictions = model(x_train[:1]).numpy()
# print(predictions)

# The tf.nn.softmax function converts these logits to "probabilities" for each class:
tf.nn.softmax(predictions).numpy()

# Choose an optimizer
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # loss function for training:
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=30)
model.evaluate(x_test, y_test)

