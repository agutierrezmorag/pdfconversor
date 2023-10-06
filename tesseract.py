import os
import PyPDF2
import pytesseract
from PIL import Image
import io


# Carpeta de entrada que contiene los PDFs
input_folder = 'documentos'

# Carpeta de salida donde se guardarán las carpetas y archivos .txt
output_root_folder = 'PostProcesado'

# Asegúrate de que la carpeta de salida exista
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)


# Función para extraer imágenes de un PDF y realizar OCR
def process_pdf(pdf_file, output_folder):
    pdf_images = []

    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)

        # Crea una carpeta dedicada para el documento PDF
        pdf_filename = os.path.splitext(os.path.basename(pdf_file))[0]
        pdf_folder = os.path.join(output_folder, pdf_filename)
        os.makedirs(pdf_folder, exist_ok=True)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            xObject = page['/Resources']['/XObject'].get_object()

            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    image = xObject[obj]
                    image_data = image.get_data()
                    image_bytes = bytes(image_data)
                    image_obj = Image.open(io.BytesIO(image_bytes))

                    """
                    if hasattr(image_obj, '_getexif'):
                        exif = image_obj._getexif()
                        if exif:
                            orientation = exif.get(0x0112)
                            if orientation is not None:
                                if orientation == 1:
                                    # No es necesario rotar
                                    pass
                                elif orientation == 3:
                                    image_obj = image_obj.rotate(180, expand=True)
                                elif orientation == 6:
                                    image_obj = image_obj.rotate(-90, expand=True)
                                elif orientation == 8:
                                    image_obj = image_obj.rotate(90, expand=True)
                    """

                    # Ve si el ancho es mayor que el alto y para rotar la imagen en caso de que este horizontal.
                    width, height = image_obj.size

                    if (width > height):
                        image_obj = image_obj.rotate(-90, expand=True)

                    image_filename = f"page{page_num + 1}.png"
                    image_path = os.path.join(pdf_folder, image_filename)
                    image_obj.save(image_path)
                    pdf_images.append(image_path)

    return pdf_images


# Función para realizar OCR en imágenes y guardar el texto en un archivo .txt
def ocr_images(images, output_folder):
    extracted_text = []

    for image_file in images:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image,
                                           lang='spa')  # Puedes especificar el idioma aquí si es necesario (Literal nombre del paquete de idioma que se descarga)
        extracted_text.append(text)

    # Crea un archivo .txt para el documento en la carpeta de salida
    txt_filename = os.path.basename(output_folder) + '.txt'
    txt_path = os.path.join(output_folder, txt_filename)

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for text in extracted_text:
            txt_file.write(text + '\n')

    return extracted_text


# Iterar sobre los archivos PDF en la carpeta de entrada
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".pdf"):
            pdf_file = os.path.join(root, file)

            # Crear una carpeta para el documento PDF en la carpeta de salida
            pdf_filename = os.path.splitext(os.path.basename(pdf_file))[0]
            output_folder = os.path.join(output_root_folder, pdf_filename)
            os.makedirs(output_folder, exist_ok=True)

            pdf_images = process_pdf(pdf_file, output_folder)
            extracted_text = ocr_images(pdf_images, output_folder)

            print(f"Procesado: {pdf_file}")
            print(f"Texto extraído y guardado en: {output_folder}")
