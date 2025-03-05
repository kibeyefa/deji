import pikepdf
from pypdf import PdfReader, PdfWriter

def extract_pdf_metadata(file_path:str):
    pdf = pikepdf.Pdf.open(file_path)
    pdf_metadata = pdf.docinfo
    response_text = ""
    response_text += f"Author: {pdf_metadata['/Author']}. \n" if "/Author" in pdf_metadata  else "Author metadata not found!\n"
    response_text += f"Title: {pdf_metadata['/Title']}. \n" if "/Title" in pdf_metadata else "Title metadata not found!"

    # print(response_text)
    return response_text

def edit_pdf_metadata(file_path:str, author:str, title:str):
    reader = PdfReader(file_path)
    metadata = reader.metadata
    print("Original Metadata:", metadata)
    

    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata({"/Author": author, "/Title": title})

    with open(file_path, "wb") as output_pdf:
        writer.write(output_pdf)

    return f"Author: {author}\nTitle: {title}"


if __name__ == "__main__":
    edit_pdf_metadata("loyal copy.pdf", "Dag Heward Mills", "Loyalty and Disloyalty")
    # extract_pdf_metadata('loyal.pdf')
