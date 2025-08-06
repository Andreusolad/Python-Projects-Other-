from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    #Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    #Set the lines
    for i in range(21, 293, 11):
        pdf.line(10, i, 200, i)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        #Set footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        #Set the lines
        for i in range(21, 293, 11):
            pdf.line(10, i, 200, i)

pdf.output("sp_pdf.pdf")


