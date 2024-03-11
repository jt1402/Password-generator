# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define data directories
train_dir = '/path/to/training_data'  # Directory containing training images
test_dir = '/path/to/test_data'        # Directory containing test images

# Data preprocessing
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,        # Rescale pixel values to [0, 1]
    rotation_range=40,        # Augmentation: Randomly rotate images
    width_shift_range=0.2,    # Augmentation: Randomly shift images horizontally
    height_shift_range=0.2,   # Augmentation: Randomly shift images vertically
    shear_range=0.2,          # Augmentation: Shear transformations
    zoom_range=0.2,           # Augmentation: Randomly zoom in on images
    horizontal_flip=True,     # Augmentation: Randomly flip images horizontally
    fill_mode='nearest'       # How to fill in newly created pixels
)

test_datagen = ImageDataGenerator(rescale=1.0/255.0)

# Create data generators
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),   # Resize images to a consistent size
    batch_size=32,
    class_mode='binary'       # Binary classification (cats vs. dogs)
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    loss='binary_crossentropy',
    optimizer=tf.keras.optimizers.RMSprop(lr=1e-4),
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=100,  # You can adjust this based on your dataset size
    epochs=30,            # The number of training epochs
    validation_data=test_generator,
    validation_steps=50   # You can adjust this based on your dataset size
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test accuracy: {test_accuracy * 100}%")
