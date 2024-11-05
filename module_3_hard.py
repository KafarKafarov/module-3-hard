def calculate_structure_sum(data):
    total_sum = 0

    def process_item(item):
        nonlocal total_sum

        if isinstance(item, int):

            total_sum += item
        elif isinstance(item, str):

            total_sum += len(item)
        elif isinstance(item, dict):

            for value in item.values():
                process_item(value)
            for key in item:
                process_item(key)
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):

            for subitem in item:
                process_item(subitem)

    for element in data:
        process_item(element)

    return total_sum



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)