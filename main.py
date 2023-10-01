from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
from PIL import Image

import os
import easyocr

images = []
reader = easyocr.Reader(['es'])

for file in os.listdir('./documentos'):
    filename, _ = file.split('.')
    if not os.path.exists(f'scans/{filename}'):
        os.makedirs(f'scans/{filename}')
    images = convert_from_path(f'documentos/{file}', output_folder=f'scans/{filename}', fmt='jpeg')

results = reader.readtext(images[0], detail=0, paragraph=True)

text_lines = [text for (bbox, text, prob) in results]

output_file = 'output.txt'  # Replace with your desired output file path

with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(text_lines))


