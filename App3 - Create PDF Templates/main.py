from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #pages do not broken automatically

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) #red, green, blue combination
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21) #x1, y1, x2, y2

    #Set the footer
    pdf.ln(265) #brealine of 278 mm, about the whole page more or less

    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Set the lines
    for i in range(21, 293, 11):
        pdf.line(10, i, 200, i)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        #Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        #Set the lines
        for i in range(21, 293, 11):
            pdf.line(10, i, 200, i)
pdf.output("output.pdf")