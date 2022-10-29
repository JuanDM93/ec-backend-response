# ec-backend-response

Exercises solutions for EC evaluation

## How to run

To run them, you need to have [python3](https://www.python.org/) installed.

Each exercise is in a different folder, so you can run them by going to the respective folder.

```bash
.
├── .gitignore
├── LICENSE
├── README.md
├── exercise1
│   ├── occurrence_counter.py
│   ├── sample.txt
│   ├── test_occurrence_counter.py
│   └── utils.py
└── exercise2
    ├── criteria.txt
    ├── custom_sort.py
    ├── entries.txt
    ├── result.txt
    ├── test_custom_sort.py
    └── utils.py
```

### Exercise 1

This solution (occurrence_counter.py) is a simple program that counts the ocurrences of a certain word in a text file.

You can run the program with the following command:

```bash
python occurrence_counter.py <text_file> <word_to_count>
```

Testing:

```bash
python test_occurrence_counter.py
```

### Exercise 2

This solution (custom_sort.py) is a program that sorts a list of entries in a text file.

To run it, you can use the next command:

```bash
python custom_sort.py <entries_file> <criteria_file>
```

Testing:

```bash
python test_custom_sort.py
```

### License

MIT
