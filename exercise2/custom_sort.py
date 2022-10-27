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
            result.append(entry)

    for entry in result:
        entries.remove(entry)

    # using sort
    # result.sort(key=lambda x: x['priority'], reverse=True)

    # using sorted
    # result = sorted(result, key=lambda x: x['priority'], reverse=True)

    # using for loop
    # for i in range(len(result)):
    #     for j in range(i + 1, len(result)):
    #         if result[i]['priority'] < result[j]['priority']:
    #             result[i], result[j] = result[j], result[i]

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i]['priority'] > result[j]['priority']:
                result[i], result[j] = result[j], result[i]

    # using for loop and enumerate
    # for i, entry in enumerate(result):
    #     for j, entry2 in enumerate(result[i + 1:]):
    #         if entry['priority'] < entry2['priority']:
    #             result[i], result[j + i + 1] = result[j + i + 1], result[i]

    result.extend(entries)
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
