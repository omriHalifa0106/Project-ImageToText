import numpy as np
from keras.models import load_model
import pandas as pd
import os
import datetime

# Constants
HEIGHT = 28
WIDTH = 28


# in this function we have the prediction for the sentence
# we load the modls save that we created to use to make
# predictions for each letter.
def Model(count_letters):
    model = load_model('emnist_model.h5')  # load model
    # dictionary of Chars:
    # we use this dict so we will be able to change the reply \ predict into the actual letter.
    chars = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
        20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
        30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
        36: 'a', 37: 'b', 38: 'd', 39: 'e', 40: 'f', 41: 'g', 42: 'h', 43: 'n', 44: 'q', 45: 'r', 46: 't'}

    image_csv = pd.read_csv(".\\word.csv", delimiter=',') # open csv file
    test_csv = pd.read_csv(".\\emnist-balanced-test.csv", delimiter=',')

    # Normelizing
    # we normelize the images so we will be able to feed them into the machine.
    image_csv_x = image_csv.iloc[:, :]
    image_csv_x = np.asarray(image_csv_x)
    image_csv_x = image_csv_x.astype('float32')
    image_csv_x /= 255

    image_csv_x = image_csv_x.reshape(-1, HEIGHT, WIDTH, 1)  # last reshape to 28x28
    y_pred = model.predict(image_csv_x)  # make predictions
    word = " "
    for i in range(count_letters):
        word += chars[y_pred[i - 1].argmax()]  # add all predicted letters to one string, and return it.
    return word


# modle code for the letter recognition
# this is where the prediction is made, and where
# we use the ai that we created.
def model_CNN(pathFolder):
    model = load_model('emnist_model.h5')  # here we load the ai machine that we created and saved.
    # dictionary of Chars:
    # we use this dict so we will be able to change the reply\ predict into the actual letter.
    chars = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
        20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
        30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
        36: 'a', 37: 'b', 38: 'd', 39: 'e', 40: 'f', 41: 'g', 42: 'h', 43: 'n', 44: 'q', 45: 'r', 46: 't'}
    image_csv = pd.read_csv(".\\data to use.csv", delimiter=',')  # open the csv file.

    # Reshape and rotate EMNIST images
    def rotate(image):
        image = image.reshape([28, 28])
        image = np.fliplr(image)
        image = np.rot90(image)
        return image

    # Flip and rotate image
    image_csv = np.asarray(image_csv)

    # Normalise
    # we normelize the images so we will be able to feed them into the machine.
    image_csv = image_csv.astype('float32')
    image_csv /= 255
    image_csv = image_csv.reshape(-1, 28, 28, 1)  # reshape into 28x28
    # from test dataset:
    pred = model.predict(image_csv)  # make prediction
    image_csv = image_csv.reshape(image_csv.shape[0], 28, 28)
    print("Predict Char is " + chars[pred.argmax()])
    pathFolderchar = pathFolder + "\\Predict_Char_Project_Image_TO_Text.txt"  # create text file
    pathFolderchars = pathFolder + "\\predict_characters.txt"  # create text file

    # here we insert the letter and the information into the text file.
    f1 = open(pathFolderchar, "w")
    f1.write("Predict Char is " + chars[pred.argmax()])
    f1.close()
    f2 = open(pathFolderchars, "a")
    filesize = os.path.getsize(pathFolderchars)
    if filesize == 0:
        f2.write('Character recognition - ImageToText project:\n')
    f2.write(str(datetime.datetime.now()) + " -Predict Char is: " + chars[pred.argmax()] + '\n')
