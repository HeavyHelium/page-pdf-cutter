import sys
from PyPDF2 import PdfReader, PdfWriter

def crop_large_slide(input_pdf, output_pdf, sections_per_page=2):
    """
    Splits a large PDF slide into smaller sections per page.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_pdf (str): Path to the output PDF file.
        sections_per_page (int): Number of sections to divide the slide into vertically.
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        width = float(page.mediabox.upper_right[0])
        height = float(page.mediabox.upper_right[1])
        section_height = height / sections_per_page
        for i in range(sections_per_page):
            cropped_page = page
            cropped_page.mediabox.upper_right = (width, height - i * section_height + 65)
            cropped_page.mediabox.lower_left = (0, height - (i + 1) * section_height + 65)
            writer.add_page(cropped_page)

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pagify_pdf.py <input_pdf> <output_pdf> [sections_per_page]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    sections_per_page = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    crop_large_slide(input_pdf, output_pdf, sections_per_page)
    print(f"PDF successfully pagified! Output saved to {output_pdf}")

