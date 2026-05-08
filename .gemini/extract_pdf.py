import pypdf
import sys

def extract_text(pdf_path):
    print(f"--- Extracting from: {pdf_path} ---")
    try:
        reader = pypdf.PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            print(f"\n--- Page {i+1} ---")
            print(page.extract_text())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_text(sys.argv[1])
