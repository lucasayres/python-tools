# -*- coding: utf-8 -*-
from cairosvg import svg2pdf


def svg_to_pdf(svg, pdf):
    """Convert an SVG image to PDF.

    Args:
        svg (str): Input file - example.svg.
        pdf (str): Output file - example.pdf.

    """
    svg2pdf(url=svg, write_to=pdf)
