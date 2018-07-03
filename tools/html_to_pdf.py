# -*- coding: utf-8 -*-
import pdfkit


def html_to_pdf(input, output, type='string'):
    """Convert HTML/webpage to PDF. For linux, install: sudo apt-get install wkhtmltopdf.

    Args:
        input (str): HTML Text, URL or file.
        output (str): Output file (.pdf).
        type (str): Types can be 'string', 'url' or 'file'.

    """
    if type == 'url':
        pdfkit.from_url(input, output)
    elif type == 'file':
        pdfkit.from_file(input, output)
    else:
        pdfkit.from_string(input, output)
