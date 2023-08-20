from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

def encrypt_pdf(input_file_path, output_file_path):
    if not Path(input_file_path).exists():
        print(f"File {input_file_path} does not exist. Please check the path and try again.")
        return

    pdfWriter = PdfFileWriter()

    with open(input_file_path, 'rb') as file:
        pdf = PdfFileReader(file)

        for page in range(pdf.numPages):
            pdfWriter.addPage(pdf.getPage(page))

        password = input('Enter password: ')
        pdfWriter.encrypt(password)

        with open(output_file_path, 'wb') as file:
            pdfWriter.write(file)

        print(f"File {input_file_path} was successfully encrypted and saved as {output_file_path}.")

if __name__ == "__main__":
    input_file_path = input("Please enter the path to the PDF file you want to encrypt: ")
    output_file_path = f'protected_{Path(input_file_path).name}'
    encrypt_pdf(input_file_path, output_file_path)
