from pdf2image import convert_from_path
import os
import easyocr
import multiprocessing


def process_pdf(pdf_file, output_dir):
    try:
        # Extract the filename without the extension
        filename, _ = os.path.splitext(pdf_file)

        # Add your PDF conversion options here (e.g., DPI)
        pdf_conversion_options = {
            'dpi': 300,
            # Add other options as needed
        }

        # Create a directory with the same name in the output directory
        output_subdir = os.path.join(output_dir, filename)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Convert the PDF into images
        images = convert_from_path(
            os.path.join('./documentos', pdf_file),
            output_folder=output_subdir,
            fmt='jpeg',
            poppler_path=r'C:\dev\poppler-23.08.0\Library\bin',
            **pdf_conversion_options
        )

        # Initialize EasyOCR inside the process to avoid potential conflicts
        reader = easyocr.Reader(['es'])

        # Combine OCR results for all images into a single string
        combined_results = []

        for i, image in enumerate(images):
            results = reader.readtext(image, detail=0, paragraph=True)
            combined_results.extend(results)

        # Create a single output text file for the PDF
        output_file = os.path.join(output_subdir, f'{filename}_combined.txt')

        with open(output_file, 'w', encoding='utf-8') as txt_file:
            for result in combined_results:
                txt_file.write(result + '\n\n')
    except Exception as e:
        print(f"Error processing {pdf_file}: {str(e)}")


if __name__ == '__main__':
    output_dir = './transcripts'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = [f for f in os.listdir('./documentos') if f.endswith('.pdf')]

    # Adjust the number of processes based on your CPU cores
    num_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(num_processes) as pool:
        # Pass output_dir as an argument to process_pdf
        pool.starmap(process_pdf, [(pdf_file, output_dir) for pdf_file in pdf_files])
