from PyPDF2 import PdfReader, PdfWriter
pdf_file = r"C:\Users\Cash\Documents\pruebas_python\invoice.pdf"

with open(pdf_file,"rb") as file:
    pdf_reader = PdfReader(file)
    total_pages = len(pdf_reader.pages)
    print(total_pages)
    for i,c in enumerate(pdf_reader.pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(c)
        with open(f"C:/Users/Cash/Documents/pruebas_python/{i+1}.pdf","wb") as output:
            pdf_writer.write(output)
