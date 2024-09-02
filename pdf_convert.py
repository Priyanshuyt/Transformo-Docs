from fpdf import FPDF

def save_text_as_pdf(content, pdf_file_path):
    """
    Saves the given content to a PDF file, handling any character encoding issues.

    :param content: The text content to save.
    :param pdf_file_path: The path to save the PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Split content into lines
    lines = content.split('\n')

    # Iterate through each line in the content
    for line in lines:
        # Encode the line in 'latin1' (ISO-8859-1) to avoid encoding issues
        try:
            pdf.multi_cell(0, 10, line.encode('latin1', 'replace').decode('latin1'))
        except Exception as e:
            print(f"Error writing line to PDF: {e}")
    
    pdf.output(pdf_file_path)
    print(f"PDF saved as {pdf_file_path}")

if __name__ == "__main__":
    # Path to the file where OCR output is stored
    file_path = "C:/Users/priya/OneDrive/Desktop/ocr/ocr_practice/output_text.txt"  # Replace with the actual path to your OCR output file

    # PDF output file path
    pdf_file_path = "myname.pdf"  # Replace with the desired PDF output file name

    # Read the content from the text file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Save the content to a PDF file
    save_text_as_pdf(content, pdf_file_path)
