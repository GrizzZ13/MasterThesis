import pdftotext

# Load your PDF
with open("main.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string
print("\n\n".join(pdf))
