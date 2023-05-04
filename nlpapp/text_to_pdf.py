# Python program to convert text file to PDF using FPDF


from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)

f = open("C://Users//Reema//PycharmProjects//nlp//media//input.txt", "r")

for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

pdf.output("C://Users//Reema//PycharmProjects//nlp//media//pp.pdf")