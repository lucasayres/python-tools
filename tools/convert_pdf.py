# -*- coding: utf-8 -*-
from io import BytesIO
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams


def convert_pdf(input_file, format='text', codec='utf-8'):
    """Convert PDF file to text or html.

    Args:
        input_file (str): Input PDF file.
        format (str): Format text or html.
        codec (str): Codec for encode the text.

    Returns:
        str: Return text or html from PDF file.

    """
    manager = PDFResourceManager()
    output = BytesIO()
    laparams = LAParams()
    if format == 'text':
        converter = TextConverter(manager, output, codec=codec, laparams=laparams)
    elif format == 'html':
        converter = HTMLConverter(manager, output, codec=codec, laparams=laparams)

    with open(input_file, 'rb') as f1:
        interpreter = PDFPageInterpreter(manager, converter)
        for page in PDFPage.get_pages(f1,
                                      caching=True,
                                      check_extractable=True):
            interpreter.process_page(page)

        converter.close()
        text = output.getvalue()
        output.close()

    return text.decode()
