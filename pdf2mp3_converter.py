from gtts import gTTS
import PyPDF2
import os
from tqdm import tqdm
import time

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        total_pages = len(pdf_reader.pages)
        with tqdm(total=total_pages, desc='Converting', unit=' page') as pbar:
            for page in pdf_reader.pages:
                text += page.extract_text()
                pbar.update(1)
                time.sleep(0.1) 
        return text.strip()

def main():
    input_file = input("Please enter the path and name of the input file: ")
    output_file = input("Please enter the path and name of the output MP3 file: ")

    text = extract_text_from_pdf(input_file)

    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

    print(f"MP3 file saved at: {output_file}")

if __name__ == "__main__":
    main()
