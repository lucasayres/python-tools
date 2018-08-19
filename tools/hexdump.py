# -*- coding: utf-8 -*-
import string


def hexdump(filename, length=16, sep='.'):
    """Generate hexdump of a file.

    Args:
        filename (str): File.
        length (int): Length.
        sep (str): Separator.

    """
    with open(filename, 'r') as f:
        content = f.read()
        display = string.digits + string.ascii_letters + string.punctuation
        filters = ''.join(((x if x in display else '.')
                          for x in map(chr, range(256))))
        lines = []
        for c in range(0, len(content), length):
            chars = content[c:c + length]
            hex = ' '.join(["%02x" % ord(x) for x in chars])
            if len(hex) > 24:
                hex = "%s %s" % (hex[:24], hex[24:])
            printable = ''.join(["%s" % filters[ord(x)] for x in chars])
            lines.append("%08x:  %-*s  |%s|\n" %
                         (c, length * 3, hex, printable))
        print(''.join(lines))
