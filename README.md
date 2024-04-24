# PDF to Audio Converter

This Python script converts text from a PDF file into an audio MP3 file using the Google Text-to-Speech (gTTS) library. It utilizes the PyPDF2 library to extract text from the PDF file and the tqdm library to display a progress bar during the conversion process.

## Requirements

- Python 3.x
- `gtts` library
- `PyPDF2` library
- `tqdm` library

Install the required libraries using pip:

```
pip install gtts PyPDF2 tqdm
```

## Usage

1. Run the script `pdf2audio.py`.
2. When prompted, enter the path and name of the input PDF file.
3. Enter the path and name of the output MP3 file.
4. The script will extract text from the PDF file, convert it into speech, and save it as an MP3 file.

## Example

```
python3 pdf2audio.py
```

Output:

```
Please enter the path and name of the input file: input.pdf
Please enter the path and name of the output MP3 file: output.mp3
MP3 file saved at: output.mp3
```

## Notes

- Ensure that the input PDF file contains readable text. Scanned documents or images may not be processed accurately.
- The script may take some time to convert large PDF files. Be patient, especially when processing documents with many pages.
