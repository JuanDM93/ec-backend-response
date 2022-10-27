import sys


def get_args() -> tuple:
    """
    Function to get the arguments from the command line

    Returns
    -------
    tuple
        Tuple with the entries and criteria filenames
    """
    if len(sys.argv) != 3:
        print('Usage: python3 custom_sort.py <entries_file> <criteria_file>')
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


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


def get_data(filename: str) -> list:
    """
    Function to get data from a file

    Parameters
    ----------
    filename : str
        Name of the file

    Returns
    -------
    list
        List of data
    """
    data = get_data_from_file(filename)
    try:
        data = eval(data)
    except NameError:
        print(f'File {filename} has no data')
        sys.exit(1)
    return data
