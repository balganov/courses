from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(40, 10, "CS50 Shirtificate", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
