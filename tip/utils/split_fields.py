import shlex


def split_fields(fields):
    """Split CLI fields.

    Args:
        fields (str): CLI fields.

    Returns:
        (list): Splitted parameters.

    """
    splitter = shlex.shlex(fields, posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    return list(splitter)
