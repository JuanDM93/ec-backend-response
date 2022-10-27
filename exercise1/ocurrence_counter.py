"""
Python script to count the number of occurrences of a word in a text file.
"""

# Importing required modules
import utils


def count_word(file_data: str, word: str) -> int:
    """
    Function to count the number of occurrences of a word in a text file

    Parameters
    ----------
    file_data : str
        Text file data to be searched
    word : str
        Word to be counted

    Returns
    -------
    int
        Number of occurrences of the word in the text data
    """
    words = file_data.split()
    count = 0
    for w in words:
        w = w.strip(',.;:')
        if w == word:
            count += 1
    return count


def main():
    """
    Main function
    """
    filename, word = utils.get_args()
    file_data = utils.get_data_from_file(filename)
    result = count_word(file_data, word)
    print(f'{result} ocurrencias encontradas.')


# Calling main function
if __name__ == '__main__':
    main()
