#protct any pdf file with password using pypdf library
#pip install pypdf

from pypdf import PdfReader, PdfWriter

input_file = input("Enter the name of the PDF file(with extension): ")
output_file = input("Enter the name of the protected PDF file(with extension): ")
password = input("Enter the password for the PDF file: ")

reader = PdfReader(input_file)
writer = PdfWriter()

writer.append(reader)
writer.encrypt(password)

with open(output_file, "wb") as f:
    writer.write(f)
    print(f"Protected PDF file '{output_file}' created successfully with password protection.")