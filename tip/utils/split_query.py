import shlex


def split_query(query):
    """Split CLI query.

    Args:
        query (str): CLI query.

    Returns:
        (list): Splitted parameters.

    """
    splitter = shlex.shlex(query, posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    return list(splitter)
