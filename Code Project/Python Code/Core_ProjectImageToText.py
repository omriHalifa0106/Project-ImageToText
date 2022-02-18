import cv2
import pytesseract
from PIL import Image
import csv
import numpy as np
from pytesseract import Output
import CNN
import Features_ProjectImageToText
import imageProcessing
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#this function is the one called.
#this seperates the sentence recognition from the word recognition.
def Choice(img,imagePath,sentence_or_character,pathFolder):
    if (sentence_or_character =='"1"'):#if the given in is 1 than it means that it is for a sentence
                CoreFunction(img,pathFolder)
    elif (sentence_or_character =='"2"'):#if the given code is 2 than it meens that it is for a letter.
                forLetter(img,imagePath,pathFolder)


#this function it the csv writer for singular letters.
#it transforms the letter into a csv in a correct way for the machine
#for a singular letter.
def csvWriterLetter(fil_name, nparray):
    example = nparray
    with open(fil_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(example)
        writer.writerow(example)

#this function is the main function for the letter recognition,
#it is given the image, the path, and the path to save it to.
def forLetter(img,imagePath,pathFolder):
    res = cv2.resize(img, (28, 28))
    cv2.imwrite(imagePath, res)#writes the image
    img = np.array(Image.open(imagePath))#create an arr for the file.
    newimg = []
    for line in img:
        for pixle in line:
            newimg.append(255 - pixle[0])#invert the colors for the machine.
    img = newimg
    csvWriterLetter("data to use", img)#create csv file.
    CNN.model_CNN(pathFolder)#call the machine to make a prediction.


def csvWriter(fil_name, nparray):
    example = nparray
    with open(fil_name + '.csv', 'w', newline='') as csvfile:  # opening the file and calling it csvfile
        writer = csv.writer(csvfile, delimiter=',')  # creating a csv writer with delimiter as comma.
        writer.writerows(example)  # using premade functions to add the letters's images from the list into a csv file.


#make square is a function that makes the image look beter, and help
#the machine recognize the word better
#it adds a white backround so when the image will be resized, the letter wont be on the whole screen
#and will be more centered.
def make_square(im, min_size=256, fill_color=(255, 255, 255, 255)):
        x, y = im.size
        size = max(x+4, y+4)
        new_im = Image.new('RGBA', (size, size), fill_color)
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        return new_im

def toFileTxt(final_string,pathFolder):
    pathFolder = pathFolder +"\\OCR_Project_Image_TO_Text.txt"
    f = open(pathFolder, "w")
    f.write("Welcome to OCR Project image to text!!\n")
    f.write("my machine has classified your image as follows:\n")
    f.write('"' + final_string + '"\n')
    f.write("\n")
    f.write("Omri Halifa")
    f.close()


#this is the main functio for the sentence recognition, it includes all the calls for the
#minor functions, and preforms most of the progress ,for example the word seperation,letter seperation
#resizing, corrections, and preparing the csv for the machin to make its predictions.
def CoreFunction(img,pathFolder):
    print("Loads and recognize the text in the image...")
    h, w, _ = img.shape

    img_words = img.copy()
    d = pytesseract.image_to_data(img_words, output_type=Output.DICT)#this function takes the image
    # and crops it into boxes of words, lines and paragraphes.
    n_boxes = len(d['level'])
    ROI_number = 0
    for i in range(d['level'].count(5)+d['level'].count(4)-1+d['level'].count(3)-1+d['level'].count(2)-1):
        # line to add a space to the end code, and to save the words in a file in a dir we create
        # so in the futer we can seperate them into letters.
        i = i + d['level'].index(5)# i want to skip the 5 first places because they represent the start of the proces(first paragraph,line and word).
        if (d['conf'][i] != '-1'):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])#i save the dimantions and the position of the word
            crop_word = img_words[y:y + h, x:x + w]#we crop the initial image
            cv2.imwrite('.\words\word{}.png'.format(ROI_number), crop_word)#i save it in a dir with the index as its name.
            ROI_number += 1
    count_letter = 0
    final_string = " "
    num_word = 0
    #in this for loop i seperate every word in the dir by the index, and the ammount
    #saved in the last for.
    #here i will also split the word into letters and save the image in a csv file for out ai machine.
    for i in range(ROI_number):#for every number of words counted.
        filename ='.\words\word{}.png'.format(num_word)
        temp_img = []#defining a list for the letters in the word to be in.
        num_word+=1
        img = cv2.imread(filename)#loading file from filename.

        h, w, _ = img.shape# using .shape to take dimantions of the image.
        boxes = pytesseract.image_to_boxes(img)#main way of spliting the word into letters,
        # if doesnt work we have a secondery method longer in the code.
        count_letter = 0
        for b in boxes.splitlines():#for every letter found
            b = b.split(' ')
            start_point = (int(b[1]), h - int(b[2]))#save start pos
            end_point = (int(b[3]), h - int(b[4]))#save end pos
            crop = img.copy()

            out = crop[(h-int(b[4])):(h-int(b[2])),int(b[1]):int(b[3])].copy()#crop by the start and end pos's.
            count_letter+=1
            cv2.imwrite("temp.png",out)#save the image temporarly
            t = Image.open("temp.png")
            new = make_square(t)#using a function that shahar made to make the image a bit eazier to recognize
            new.save("temp.png")
            out = cv2.imread("temp.png")
            out = cv2.cvtColor(out,cv2.COLOR_BGR2GRAY)#truning the image into greyscale
            #cv2.imshow("letter",out)
            #cv2.waitKey()
            res = cv2.resize(out,(28,28));# resizing the image for the ai to understand
            cv2.imwrite("temp.png",res)
            nparr = np.array(Image.open("temp.png"))#adding the image into a list that contains all of the letters,
            # so it will be easier for the futer steps
            newimg = []
            for line in nparr:
                for pixle in line:
                    newimg.append(255 - pixle)#reverting the images colors for the machine to understand.
            temp_img.append(newimg)#add to the final list
        if (count_letter==0):#if the first split method didnt work as sapose to we move into a secondery method
            count_letter = imageProcessing.cutLettersFromWord(filename)#function in difrent file.
        else:
            csvWriter("word", temp_img)#this function transforms the list given to it into a csv file, for the machine.
        final_string += CNN.Model(count_letter)#call the cnn modle to make its predictions based on the information given
        final_string += " "
    final_string = final_string.lower()#lower all leters from detection
    final_string = final_string.replace("0", "o")#make some corrections
    final_string= final_string.split()
    final_string[0] =final_string[0].capitalize()#capitalize the string based of the list positions..
    final_string = " ".join(final_string)#join the list into a final string
    final_string = final_string.strip()
    toFileTxt(final_string,pathFolder)#use a function to make a text file
    print("The recognize text is:" + final_string)
    print("The machine created a text file with image classification successfully in: "+pathFolder+" and also created several features that our project supports!")
    print("1. translate the text in the image from Hebrew to English")
    print("2. To move the txt file to a word file")
    print("3. To transfer the txt file to a pdf file")
    print("4. Show background of the image text")
   # Features_ProjectImageToText.translateImageText(final_string,pathFolder)
    Features_ProjectImageToText.convert_to_word(pathFolder)
    Features_ProjectImageToText.convert_to_pdf(pathFolder)
    Features_ProjectImageToText.CommonColor(img,pathFolder)


