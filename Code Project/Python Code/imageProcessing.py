import cv2
from imutils import contours
from PIL import Image
import numpy as np
import csv


# this function makes adds some pixles to the side of the image
# so the process of resizing it will not harm the image, and so it will be
# more centered and will not fill the image(adds alittel for the prediction).
def make_square(im, min_size=256, fill_color=(255, 255, 255, 255)):
    x, y = im.size
    size = max(x + 4, y + 4)  # deciding what size to resize it to
    new_im = Image.new('RGBA', (size, size), fill_color)  # make a new image just made from black with new size
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))  # paste the letters image on the new black image.
    return new_im  # return the new image.


# the csv writer for the main sentence recognition
# it recives a list of images, that are made as an arr of grey-scale pixles
# it creats a csv file that contains all of the images(pixles seperated by commas and letters seperated by \n)
def csvWriter(fil_name, nparray):
    example = nparray
    with open(fil_name + '.csv', 'w', newline='') as csvfile:  # open a new csv file and name it as csvfile
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(example)  # write the arr into the file with a writer that seperates by commas.


# this function is called on the case when the main function cant cut the word correctly
# this function cuts the word into a letters by finding when one starts and when it ends.
#
def cutLettersFromWord(image):
    image = cv2.imread(image)  # read the image from where it was saved.
    image = cv2.bitwise_not(image)  # revert the colors for the secondery method.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grey scale the image.
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts, _ = contours.sort_contours(cnts, method="left-to-right")
    temp_img = []  # defining a list for the letters in the word to be in.
    ROI_number = 0
    count = 0
    for c in cnts:
        area = cv2.contourArea(c) #Calculates a contour area.
        if area > 10:  # ignore all the dots and small points (like i's and j's)
            x, y, w, h = cv2.boundingRect(c)
            ROI = 255 - image[y:y + h, x:x + w]
            cv2.imwrite("temp.png", ROI)
            t = Image.open("temp.png")
            new = make_square(t)  # square the image for the machine.
            new.save("temp.png")  # save the new image
            out = cv2.imread("temp.png")
            out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)  # convert to grey

            res = cv2.resize(out, (28, 28))  # resizing the image for the ai to understand
            cv2.imwrite("temp.png", res)
            nparr = np.array(Image.open("temp.png"))  # make an array of the letters from the image
            newimg = []
            for line in nparr:
                for pixle in line:
                    newimg.append(255 - pixle)  # invert color.
            temp_img.append(newimg)  # add to image list.
            count += 1
            csvWriter("word", temp_img)  # csv write the word.
    return count
