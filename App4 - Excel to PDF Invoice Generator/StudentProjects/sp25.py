import pandas
from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("Text+Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # We first extract the name of the file
    name = Path(filepath).stem.capitalize()

    # We extract file's information
    with open(filepath, 'r') as file:
        content = file.read()



    # Now we create the PDFs:
    pdf.add_page()

    # We write down all the information
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=8, txt=f"{name}", ln=1)
    pdf.cell(w=0, h=8, txt=f"", ln=1)
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"output.pdf")