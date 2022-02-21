__all__ = (
    'merge',
)


def merge(file_with_strings, file_with_numbers, count_lines_f1, count_lines_f2):
    if count_lines_f1 >= count_lines_f2:
        for string in file_with_strings:
            line_with_number = None
            for number in file_with_numbers:
                if number != '\n':
                    line_with_number = number.replace('\n', '')
                break

            if string == '\n':
                continue

            yield string.replace('\n', ''), line_with_number

    else:
        for line_with_number in file_with_numbers:
            line_with_string = None
            for string in file_with_strings:
                if string != '\n':
                    line_with_string = string.replace('\n', '')
                break

            if line_with_string is None or line_with_string == '\n':
                continue

            yield line_with_string, line_with_number

