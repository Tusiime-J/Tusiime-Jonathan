#import required libraries
import os
import tensorflow as tf # type: ignore #ignore 
import numpy as np # type: ignore
from tensorflow import keras  # type: ignore
from tensorflow.keras.proessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint # type: ignore
import matplotlib.pyplot as plt #type: ignore # for plotting training history line graphs

tf.random.set_seed(42)
np.random.seed(42)

# Define constants
IMG_SIZE = (256, 256)
BATCH_SIZE = 32
EPOCHS = 20
NUM_CLASSES = 2  
ANIMAL_CLASSES = 3

# Define paths
DATA_DIR = "machine_learning"
MODEL_PATH = "model.h5"

#create a convolutional neural network model
def create_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    return model


def train_crop_model():
    '''train the main crop disease detection model'''
    #data generators with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
        validation_split=0.2  # Split data into training and validation sets
    )
    
    #create and train the model
    model = create_model((IMG_SIZE[0], IMG_SIZE[1], 3), NUM_CLASSES)
    
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
        ModelCheckpoint(MODEL_PATH, save_best_only=True)
    ]
    
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs =EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
        callbacks=callbacks
    )
    
    #plot training history
    plt.plot(history.history['accuracy'], label='accuracy')
    