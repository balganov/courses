from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", w=200, x=5, y=70)
    pdf.set_text_color(r=255,g=255,b=255)
    pdf.set_font_size(25)
    pdf.set_xy(0,0)
    pdf.cell(0, 270, f"{name} took CS50", align="C",center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
