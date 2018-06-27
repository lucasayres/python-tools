# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger


def merge_pdfs(input_pdfs, output_pdf):
    """Combine multiple pdfs to single pdf.

    Args:
        input_pdfs (list): List of path files.
        output_pdf (str): Output file.

    """
    pdf_merger = PdfFileMerger()
    for path in input_pdfs:
        pdf_merger.append(path)
    with open(output_pdf, 'wb') as fileobj:
        pdf_merger.write(fileobj)
