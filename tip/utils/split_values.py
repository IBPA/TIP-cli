import shlex


def split_values(values):
    """Split CLI values.

    Args:
        values (str): CLI values.

    Returns:
        (list): Splitted parameters.

    """
    splitter = shlex.shlex(values, posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    return list(splitter)
