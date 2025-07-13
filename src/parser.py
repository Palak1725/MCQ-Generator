import re

def clean_text(text):
    text = text.replace('\n', ' ').strip()
    return re.sub(r'\s+', ' ', text)

def split_into_chunks(text, chunk_size=40):
    sentences = text.split('.')
    return ['.'.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
