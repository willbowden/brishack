#import cv2
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image

batch_size = 100
img_height = 250
img_width = 250

def create_and_train_model(modelName):
    training_ds = tf.keras.preprocessing.image_dataset_from_directory(
        './data/train',
        seed=101,
        image_size= (img_height, img_width),
        batch_size=batch_size

    )

    testing_ds = tf.keras.preprocessing.image_dataset_from_directory(
        './data/test',
        seed=101,
        image_size= (img_height, img_width),
        batch_size=batch_size)

    validation_ds =  tf.keras.preprocessing.image_dataset_from_directory(
        './data/val',
        seed=101,
        image_size= (img_height, img_width),
        batch_size=batch_size)

    class_names = training_ds.class_names

    ## Configuring dataset for performance
    AUTOTUNE = tf.data.experimental.AUTOTUNE
    training_ds = training_ds.cache().prefetch(buffer_size=AUTOTUNE)
    testing_ds = testing_ds.cache().prefetch(buffer_size=AUTOTUNE)

    img_shape = (img_height, img_width, 3)

    base_model = tf.keras.applications.MobileNetV2(input_shape=img_shape,
                                                include_top=False,
                                                weights='imagenet')

    base_model.trainable = False

    model = tf.keras.Sequential([
        base_model,
        layers.Conv2D(32, 3, activation='relu'),
        layers.Conv2D(64, 3, activation='relu'),
        layers.Conv2D(128, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(len(class_names), activation='softmax')
    ])

    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(training_ds, validation_data = validation_ds, epochs = 50)

    plt.plot(history.history['loss'], label = 'training loss')
    plt.plot(history.history['accuracy'], label = 'training accuracy')
    plt.grid(True)
    plt.legend()
    plt.show()

    model.save(f"./{modelName}")

def prediction_grid():
    training_ds = tf.keras.preprocessing.image_dataset_from_directory(
        './data/train',
        seed=101,
        image_size= (img_height, img_width),
        batch_size=batch_size

    )

    testing_ds = tf.keras.preprocessing.image_dataset_from_directory(
        './data/test',
        seed=101,
        image_size= (img_height, img_width),
        batch_size=batch_size)


    class_names = training_ds.class_names

    AccuracyVector = []
    plt.figure(figsize=(30, 30))
    for images, labels in testing_ds.take(1):
        predictions = model.predict(images)
        predlabel = []
        prdlbl = []
        
        for mem in predictions:
            predlabel.append(class_names[np.argmax(mem)])
            prdlbl.append(np.argmax(mem))
        
        AccuracyVector = np.array(prdlbl) == labels
        for i in range(40):
            ax = plt.subplot(10, 4, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title('Pred: '+ predlabel[i]+' actl:'+class_names[labels[i]] )
            plt.axis('off')
            plt.grid(True)
        
    plt.show()

def predict_frame(imgName):
    model = tf.keras.models.load_model('./trainedModel')

    with Image.open(imgName) as img:
        resized_frame=tf.keras.preprocessing.image.smart_resize(img, (img_height, img_width), interpolation='bilinear')
        img_array = tf.keras.utils.img_to_array(resized_frame)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction=(model.predict(img_batch) > 0.5).astype("int32")
        print(prediction)
        if(prediction[0][0]==0):
            return("Accident Detected")
        else:
            return("No Accident")

print(predict_frame("./data/test/Non Accident/test29_6.jpg"))

# create_and_train_model("trainedModel3")