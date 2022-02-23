__all__ = (
    'merge',
)


def merge(file_with_strings, file_with_numbers, count_lines_f1, count_lines_f2):
    if count_lines_f1 >= count_lines_f2:
        for string in file_with_strings:
            number = file_with_numbers.readline().replace('\n', '')
            number = int(number) if number else None

            string = string.replace('\n', '')
            if not string:
                continue

            yield string, number

    else:
        for number in file_with_numbers:
            number = number.replace('\n', '')
            number = int(number) if number else None

            string = file_with_strings.readline().replace('\n', '')
            if not string:
                continue

            yield string, number

