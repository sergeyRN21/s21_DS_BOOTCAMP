def data_types():
    variables = [
        42,
        'Hello',
        3.14,
        True,
        [1, 2, 3],
        {'key': 'value'},
        (4, 5, 6),
        {7, 8, 9},
    ]

    types = [type(var).__name__ for var in variables]
    result = ', '.join(types)
    print(f'[{result}]')

if __name__ == "__main__":
    data_types()