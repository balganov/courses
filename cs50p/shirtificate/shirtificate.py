from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell("CS50 Shirtificate", center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
