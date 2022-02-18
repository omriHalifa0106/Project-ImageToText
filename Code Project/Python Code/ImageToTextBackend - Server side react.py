import os
from flask import Flask, request
from flask_cors import CORS
from PIL import Image
import base64
import io
import cv2
import numpy as np

import Core_ProjectImageToText

UPLOAD_FOLDER = 'C:\\projects'

app = Flask(__name__)


"""
A function that listens and communicates with the client, receives the server's request, 
analyzes it and sends it to the function that handles the request.
"""
@app.route('//upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    clientRequest = request.data
    clientRequestStr = clientRequest.decode("utf-8") #convert client request to str
    print(clientRequestStr)
    sentence_or_character = clientRequestStr[clientRequestStr.find('"choice":')+9:clientRequestStr.find(',"path":')] # Analyzes the user request, whether to return an answer for one character or text
    pathFolder = clientRequestStr[clientRequestStr.find('"path":')+7:-1] #Analyzes the path selected by the user to save the text
    pathFolder = pathFolder[1:-1] #remove the quotes
    if (not "null" in clientRequestStr):
        #Receives the user's image, turns it into an image, saves it, and sends it to a function according to the user's request:
        place = clientRequestStr.find('base64,') + 7
        imagestr = clientRequestStr[place : -1]
        image = base64.b64decode(imagestr)
        fileName = 'result.png'
        imagePath = ('C:\\Users\\halif\\programming\\ProjectImageToText\\ProjectCode\\ProjectImageToText' + "result.png") #const
        img = Image.open(io.BytesIO(image))
        img.save(imagePath, 'png')
        img = cv2.imread(imagePath)
        cv2.imwrite(imagePath, img)
        img = np.array(Image.open(imagePath))
        print("Image received.")
        img = cv2.imread(fileName)  # Opens the image as an image
        pathFolder = pathFolder+ "\\ProjectImageToText"
        try:
            os.mkdir(pathFolder)
        except OSError as error:
            print(error)
        Core_ProjectImageToText.Choice(img,imagePath,sentence_or_character,pathFolder) #Sends the function to the function, whether it is a single character or text, the image path, and the path selected by the user
        response = "Ok."
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="127.0.0.1",use_reloader=False)

CORS(app, expose_headers='Authorization')
