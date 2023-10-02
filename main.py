from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
from PIL import Image

import os
import easyocr

images = []
reader = easyocr.Reader(['es'])
results = []

# se itera por la carpeta documentos
for file in os.listdir('./documentos'):

    # una vez seleccionado un documento, se crea una carpeta dentro de scans con su nombre
    filename, _ = file.split('.')
    if not os.path.exists(f'scans/{filename}'):
        os.makedirs(f'scans/{filename}')

    # se realiza la conversion a imagen y se almacenan dentro de la carpeta anteriormente creada
    images = convert_from_path(
        f'documentos/{file}',
        output_folder=f'scans/{filename}',
        fmt='jpeg',
        poppler_path=r'C:\dev\poppler-23.08.0\Library\bin'
    )

for i in range(5, 11):
    results.append(reader.readtext(images[i], detail=0, paragraph=True))


output_file = 'easyocr.txt'

# se escribe los resultados a un archivo .txt
with open(output_file, 'w', encoding='utf-8') as file:
    for result in results:
        text = '\n'.join(result)
        file.write(text + '\n\n')
