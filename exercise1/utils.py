import sys


def get_args():
    """
    Get arguments from command line

    Sys.argv[1] is the name of the text file
    Sys.argv[2] is the word to be counted
    """
    try:
        filename = sys.argv[1]
        word = sys.argv[2]
    except IndexError:
        print('Usage: python ocurrence_counter.py filename word')
        sys.exit(1)
    return filename, word


def get_data_from_file(filename: str) -> str:
    """
    Function to get data from a file

    Parameters
    ----------
    filename : str
        Name of the file

    Returns
    -------
    str
        Data from the file
    """
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        sys.exit(1)
    return data
