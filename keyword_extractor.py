# importing required modules
from PyPDF2 import PdfReader
import spacy


def pdf_to_text(path):
    """
    :param path: Local path of the resume that is to be parsed
    :return: plain text in the resume
    """

    # creating a pdf reader object
    try:
        reader = PdfReader(path)
    except:
        if len(path) == 0:
            print("Enter valid path")
        else:
            print("Error")
        exit(0)

    # printing number of pages in pdf file
    print(len(reader.pages))

    # getting a specific page from the pdf file
    page = reader.pages[0]

    # extracting text from page
    text = page.extract_text()
    # print(text)

    return text

def generate_keywords(text):
    """
    Uses spacy to extract keywords from the plain text
    :param text: Plain text from the resume
    :return: Key words
    """
    nlp = spacy.load("C:\Python311\Lib\site-packages\en_core_web_sm")
    doc = nlp(text)

    result=""
    for i in doc.ents:
        i = i.orth_
        result = result + i + " "
    return result





