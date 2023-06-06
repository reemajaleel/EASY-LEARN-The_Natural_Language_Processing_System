from pypdf import PdfReader

from datetime import  datetime

# date=datetime.now().strftime("%Y%m%d%H%M%S")+".pdf"

reader = PdfReader("C:\\Users\\Reema\\PycharmProjects\\nlp\\media\\20230310174958Main Project Updated.pdf")
number_of_pages = len(reader.pages)
k=""
for i in range(0,number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    k=k+text

print(k)