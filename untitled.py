# import pikepdf

# pdf = pikepdf.Pdf.open('DOC-20221120-WA0035..pdf')


# pdf_metadata = pdf.docinfo

# for key, value in pdf_metadata.items():
# 	print(f"{key}: {value}")
# 	


from PyPDF2 import PdfReader

reader = PdfReader("sample_pdf.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(reader.pages)