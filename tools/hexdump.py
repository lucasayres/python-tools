# -*- coding: utf-8 -*-
import itertools


def hexdump(filename, chunk_size=16):
    """Generate hexdump of a binary file.

    Args:
        filename (str): Path of file.
        chunk_size (int): Chunk size.

    """
    chunks = [iter(range(chunk_size))] * 4
    header = '   '.join(
        ' '.join(format(x, '0>2x') for x in chunk)
        for chunk in itertools.zip_longest(*chunks, fillvalue=0))
    print('ADDRESS        {:<53}       ASCII'.format(header))
    print('')
    template = '{:0>8x}       {:<53}       {}'

    with open(filename, 'rb') as stream:
        for chunk_count in itertools.count(1):
            chunk = stream.read(chunk_size)
            if not chunk:
                return
            chunks = [iter(chunk)] * 4
            print(template.format(
                chunk_count * chunk_size,
                '   '.join(
                    ' '.join(format(x, '0>2x') for x in chunk)
                    for chunk in itertools.zip_longest(*chunks, fillvalue=0)),
                ''.join(
                    chr(x) if 33 <= x <= 126 else '.'
                    for x in chunk)))
