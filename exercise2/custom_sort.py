"""
Python script to sort an entry list from a criteria list
"""
from utils import get_args, get_data

CRITERIA_MAP = {
    '=': lambda x, y: x == y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '!=': lambda x, y: x != y,
}


def sort_entries(entries: list, criteria: list) -> list:
    """
    Function to sort an entry list of dictionaries
    using a criteria list
    with descending order of priority

    Parameters
    ----------
    entries : list
        List of entries to be sorted
    criteria : list
        List of criteria to sort the entries

    Returns
    -------
    list
        Sorted list of entries
    """
    result = []

    for entry in entries:
        for criterion in criteria:
            key, operator, value = criterion
            criterion_result = CRITERIA_MAP[operator](entry[key], value)
            if not criterion_result:
                break
        else:
            for index, item in enumerate(result):
                if entry['priority'] > item['priority']:
                    result.insert(index, entry)
                    break
            else:
                result.append(entry)

    entries = [entry for entry in entries if entry not in result]
    result += entries

    return result


def main():
    """
    Main function
    """
    entries_file, criteria_file = get_args()
    entries = get_data(entries_file)
    criteria = get_data(criteria_file)
    result = sort_entries(entries, criteria)
    print(result)


if __name__ == '__main__':
    main()
