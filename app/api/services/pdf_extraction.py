import fitz 


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    print
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text



def split_text_into_chunks(pdf_path, max_tokens=8000):
    text = extract_text_from_pdf(pdf_path)
    words = text.split()
    current_chunk = []
    current_length = 0
    chunks = []

    for word in words:
        word_length = len(word.split())
        if current_length + word_length > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = word_length
        else:
            current_chunk.append(word)
            current_length += word_length

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

