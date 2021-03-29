from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = open('teste-word.docx','r+b').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)

xmlContent = document.read('word/document2.xml')

wordObj = BeautifulSoup(xmlContent, 'xml')
textStrings = wordObj.find_all('w:t')

for textElem in textStrings:
    print(textElem.text)