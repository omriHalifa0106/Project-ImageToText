from docx import Document
import cv2
import numpy as np
from google_trans_new import google_translator
from fpdf import FPDF

"""
A feature that inserts into the folder that the user has selected the background of the image with the text.
"""
def CommonColor(image,pathFolder):
    img_arr = image.copy()
    img_temp = img_arr
    unique, counts = np.unique(img_temp.reshape(-1, 3), axis=0, return_counts=True)
    img_temp[:, :, 0], img_temp[:, :, 1], img_temp[:, :, 2] = unique[np.argmax(counts)]
    pathFolder =pathFolder+"\\Background_of_the_image"+".jpg"
    cv2.imwrite(pathFolder, img_temp)

"""
A feature that inserts into the folder that the user selected a word file along with the text identified in the image.
"""
def convert_to_word(pathFolder):
    # Prepare document
    document = Document()
    pathFolderText = pathFolder + "\\OCR_Project_Image_TO_Text.txt"
    with open(pathFolderText, 'r') as textfile:
        for line in textfile.readlines():
            document.add_paragraph(line)
    pathFolderWord = pathFolder + "\\OCR_Project_Image_TO_Text.docx"
    document.save(pathFolderWord)

"""
A feature that inserts into the folder that the user selected a txt file along with the translation of the text that was in the image.
"""
def translateImageText(final_string,pathFolder):
    translator = google_translator()
    translate_text = translator.translate(final_string, lang_tgt='he')
    pathFolderText = pathFolder+"\\Translate_OCR_Project_Image_TO_Text.txt"
    # open the text file in read mode
    f = open(pathFolderText, "w")
    f.write("Translation of the text in the image from English to Hebrew: "+ translate_text)
    f.close()

"""
A feature that inserts into the folder that the user selected a pdf file along with the text identified in the image.
"""
def convert_to_pdf(pathFolder):
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)
    pathFolderText = pathFolder+"\\OCR_Project_Image_TO_Text.txt"
    # open the text file in read mode
    f = open(pathFolderText, "r")
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pathFolderPdf = pathFolder + "\\OCR_Project_Image_TO_Text.pdf"
    # save the pdf with name .pdf
    pdf.output(pathFolderPdf)