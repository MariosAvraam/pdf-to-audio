from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    return page.extract_text()

if __name__ == "__main__":
    print(extract_text_from_pdf("text.pdf"))
